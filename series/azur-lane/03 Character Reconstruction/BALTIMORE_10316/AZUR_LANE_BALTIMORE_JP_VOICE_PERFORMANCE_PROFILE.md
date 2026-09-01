---
series: AZUR_LANE
artifact_type: specialist_synthesis
scope: BALTIMORE_10316_JP_VOICE_PERFORMANCE
generation: V1
status: canonical
source_boundary: JP client AZL 9.3.386 / CV 1243; 100/100 mapped Baltimore JP spoken-text WAV utterances; one separately classified non-text review WAV excluded from mapped-dialogue analysis; 100/100 fetched derivative SHA-256 values verified against canonical WAV manifest
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
semantic_authority: CN
performed_locale: JP
asset_downloader_version: 4.7.1
vgmstream_version: r2083
audio_client_version: AZL 9.3.386 / CV 1243
performed_voice_scope: quantitative acoustic realization, timing, projection, context-conditioned state transitions, and simulation constraints
direct_perceptual_listening_status: not directly auditioned in this analysis environment; waveform-derived quantitative analysis complete
ear_dependent_timbre_status: open
identity_quarantine: retained
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Baltimore JP Voice Performance Profile

## Acoustic State, Relationship Realization, and Simulation Constraints

## 0. Authority, verdict, and use

This document is the canonical V1 specialist authority for the **quantitative Japanese performed-voice realization of Baltimore / ボルチモア / group ID 10316** under the source boundary above.

It supplements, but does not replace:

- `AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH.md` for the integrated semantic/behavioral model;
- `AZUR_LANE_BALTIMORE_RELATIONSHIP_STATE_SYNTHESIS.md` for Commander CMD0–CMD5 and named-peer modifiers;
- `AZUR_LANE_BALTIMORE_MULTILINGUAL_SPEECH_PROFILE.md` for JP textual register and the parallel CN/JP/EN/TW/KR locale model;
- `AZUR_LANE_BALTIMORE_NOVEL_SITUATION_SIMULATION_AUDIT.md` for adversarial C1–C3 simulation and weakest-link confidence controls.

Authority remains layered:

```text
CN originating text / narrative / observed behavior
    → semantic character reconstruction

JP published text
    → Japanese linguistic realization

JP published mapped WAVs
    → Japanese performed realization

this specialist profile
    → quantitative acoustic state rules and performance constraints
```

Japanese performance does **not** become Baltimore's originating semantic authority. The performed layer may strengthen, bound, or refine how an already-supported state is realized; it may not manufacture motives or relationships absent from the textual/narrative corpus.

### Canonical verdict

`BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE_PASS_WITH_TWO_AXIS_ACOUSTIC_MODEL_AND_EAR_DEPENDENT_TIMBRE_OPEN`

The strongest current conclusion is:

> **Baltimore's Japanese performance is best modeled by at least two substantially independent measurable dimensions — activation/projection and temporal continuity/fragmentation — interpreted only after semantic, situational, and relationship state have been resolved. Combat/directive activation is usually projected and temporally compact; romantic-role or ceremonial significance is more reliably associated with temporal fragmentation than with a single pitch direction; established intimacy increases behavioral ease without eliminating localized contact/startle reactivity; and self-authored presentation or task-framed performance remains comparatively organized.**

This pass **STRENGTHENS** the R6 distinction between relationship security/embodied comfort and romantic-role/ceremonial fluency. It does not require a revision of H1–H10 or the R8 simulation architecture.

### Perceptual limitation

This analysis environment can inspect and measure decoded waveforms but does not provide a human-equivalent direct audition channel. Accordingly, this profile makes strong claims about:

- F0 placement and robust pitch excursion;
- timing and pause structure;
- temporal continuity/fragmentation;
- active RMS level;
- speaking-rate proxy;
- measurable context-conditioned state transitions.

It does **not** claim exact ear-dependent qualities such as husky, airy, breathy, smoky, nasal, chesty, smiling, whispery, vocal-fry-heavy, or actor-specific aesthetic impressions. Those remain OPEN pending direct perceptual review.

---

# 1. Source lock and corpus integrity

## 1.1 Canonical performed corpus

The source surface contains:

- **100/100 mapped spoken-text JP utterances**;
- **0 unresolved spoken-text records** in Baltimore's current performed publication surface;
- **1 separately classified non-text review WAV**, excluded from the 100-line speech analysis;
- seven represented skin IDs: `103160`, `103161`, `103162`, `103163`, `103164`, `103165`, `103168`.

The mapped distribution is:

| Skin | Mapped utterances |
|---|---:|
| `103160` | 38 |
| `103161` | 9 |
| `103162` | 10 |
| `103163` | 8 |
| `103164` | 8 |
| `103165` | 16 |
| `103168` | 11 |
| **Total** | **100** |

The current publication manifest classifies the 100 spoken records as:

- base-secretary / skin dialogue: 78;
- combat: 11;
- affinity: 7;
- relationship-specific: 2;
- profile: 1;
- oath: 1.

## 1.2 Technical derivative state

All 100 analyzed WAVs are:

- RIFF/WAVE;
- PCM signed 16-bit little-endian (`pcm_s16le`);
- 44.1 kHz;
- mono;
- decoded with `vgmstream r2083`;
- `signal_processing: NONE`;
- not normalized;
- not resampled;
- not trimmed by the derivative publication pipeline;
- not denoised or concatenated.

Total mapped spoken duration is **979.66 seconds / 16.33 minutes**.

## 1.3 Batch retrieval and byte verification

The Drive folder could not be retrieved as one raw folder object, so the analysis used deterministic batching over individual published WAV derivatives.

This is a retrieval detail, not an evidence downgrade. Before exhaustive analysis:

- the canonical WAV manifest was parsed;
- the exact 100 `mapping_status=MAPPED` filenames were enumerated;
- all 100 corresponding Drive derivatives were fetched;
- every local derivative SHA-256 was recomputed;
- **100/100 hashes matched the manifest**;
- missing mapped files: **0**;
- hash mismatches: **0**.

The source therefore supports an exhaustive rather than sampled quantitative pass.

## 1.4 Identity quarantine remains separate

The nine-scene Musashi/Honoka narrative false-join quarantine remains fully in force. It does not contaminate this 100-line performed corpus, which is keyed to Baltimore's published character-text audio surface. The audio pass therefore neither repairs nor relaxes the upstream `900330` / `900301` narrative actor-mapping problem.

The readiness score **82.91** likewise remains only the frozen pre-remediation generated score.

---

# 2. Quantitative measurement method

All 100 mapped WAVs were measured under one fixed procedure.

## 2.1 Pitch

- Praat-style autocorrelation F0 tracking;
- time step: 10 ms;
- F0 search range: 75–700 Hz;
- principal placement statistic: median F0;
- robust pitch excursion: p10–p90 F0 span expressed in semitones.

Raw extrema are not used as the principal range measure because momentary tracker errors and octave events make them unstable.

## 2.2 Activity and timing

Activity estimation uses:

- 25 ms RMS windows;
- 10 ms hop;
- per-clip adaptive activity threshold:
  `min(p20 + 0.30*(p90-p20), p90-12 dB)`;
- short inactive gaps up to 80 ms bridged before pause analysis.

From that activity mask the pass measures:

- active-speech duration;
- leading/trailing silence;
- internal inactive duration;
- internal-pause ratio;
- substantial pause count;
- substantial pause duration.

A substantial pause is **≥250 ms**.

This procedure is standardized inside the Baltimore pass. It is conceptually aligned with the prior Takao/St. Louis performed-voice work but should not be represented as byte-identical hidden implementation reuse.

## 2.3 Level

Active-speech RMS is reported in dBFS.

Cross-skin level differences are secondary evidence because separate recording/mastering sessions may influence absolute level. Same-context or within-skin contrasts are stronger than interpreting a skin median as an emotional property.

## 2.4 Speaking-rate proxy

The rate measure is:

> Japanese content characters per active-speech second.

It is not morae/sec or syllables/sec.

## 2.5 Interpretation discipline

Acoustic measurements are not psychological labels by themselves.

The required order is:

```text
semantic state
→ situation / relationship state
→ JP textual realization
→ measurable acoustic realization
→ bounded performance interpretation
```

Never invert this into:

```text
high F0 → embarrassment
many pauses → insecurity
low F0 → intimacy
loudness → anger
```

Those shortcuts fail against Baltimore's own corpus.

---

# 3. Corpus center

Across all 100 mapped spoken utterances:

| Metric | Corpus median |
|---|---:|
| Median F0 | **255.6 Hz** |
| Robust p10–p90 pitch span | **10.17 st** |
| Internal-pause ratio | **0.188** |
| Pauses ≥250 ms | **2** |
| Active RMS | **−18.47 dBFS** |
| Rate proxy | **5.29 JP chars / active second** |
| Utterance duration | **8.88 s** |

These are descriptive centers, not a prescription for a single generic Baltimore voice.

The most important corpus-level statistical result is that pitch placement and fragmentation are only weakly associated:

- median F0 vs internal-pause ratio: **Pearson r ≈ −0.236**;
- robust pitch span vs internal-pause ratio: **r ≈ 0.076**.

In other words, **activation/projection and temporal fragmentation are largely separate dimensions**.

Pause count is strongly confounded by opportunity:

- substantial-pause count vs clip duration: **r ≈ 0.902**;
- substantial-pause count vs Japanese content-character count: **r ≈ 0.704**.

Therefore raw pause counts cannot be interpreted as emotion without duration, pause ratio, text structure, and context.

---

# 4. Skin-level breadth audit

Skin summaries are useful breadth controls, not personality labels.

| Skin | Analytical context | N | Median F0 | Pitch span | Pause ratio | Active level | Rate proxy |
|---|---|---:|---:|---:|---:|---:|---:|
| `103160` | base + post-oath extra state | 38 | 266.7 | 9.96 st | 0.187 | −17.55 | 5.33 |
| `103161` | school / sports-club activity | 9 | 281.2 | 10.76 st | 0.161 | −17.51 | 5.94 |
| `103162` | darker/cool presentation + sport/social play | 10 | 244.4 | 10.50 st | 0.184 | −17.85 | 5.40 |
| `103163` | formal dress / dance / unfamiliar presentation | 8 | 258.9 | 9.86 st | 0.198 | −20.35 | 4.64 |
| `103164` | travel / leisure / exploration | 8 | 241.7 | 10.26 st | 0.178 | −19.53 | 5.34 |
| `103165` | race-queen helper / competition / cheering | 16 | 263.0 | 10.18 st | 0.176 | −18.65 | 5.81 |
| `103168` | bridal / established committed intimacy | 11 | 241.9 | 9.91 st | **0.312** | −18.72 | **4.61** |

The bridal/committed skin is notable not because it becomes globally high-pitched, but because its **temporal fragmentation is much greater** than the other skin centers while its median F0 is among the lowest.

Conversely, the school/sports and race-helper skins are comparatively activated and fast while remaining temporally organized.

This is already enough to reject a one-axis model in which visible femininity, romance, or intimacy simply raises pitch.

---

# 5. Executive performed-state model

The strongest measurable model is:

```text
activation / projection
        ×
temporal continuity / fragmentation
        +
semantic state
        +
relationship / role / presentation context
        ↓
JP performed realization
```

A further contextual distinction from R5–R7 remains crucial:

```text
self-authored / task-legible presentation
        versus
externally scripted / identity-prescriptive romantic or ceremonial role
```

That distinction is **not** a third acoustic axis by itself. It is a causal/contextual variable that helps explain why similar outward presentation can occupy different parts of the two-dimensional acoustic space.

### Core performed rules

1. **Clear action or command tends to preserve temporal organization even at high activation.**
2. **High F0 is not an embarrassment signature.** Combat, HP warning, skill activation, and touch/startle can all be high.
3. **Romantic significance is not a monotonic F0 ladder.** It more consistently changes segmentation, phrase connection, rate, and the relationship between deliberate speech and localized spikes.
4. **Relationship security does not eliminate physiological/contact reactivity.** Baltimore can be behaviorally comfortable and still produce sharp high-F0 touch/startle responses.
5. **Embodied intimacy becomes easier faster than ceremonial/identity labeling becomes effortless.** R6's two-axis relationship model receives independent acoustic support.
6. **Self-authored presentation remains comparatively fluent.** Conspicuous outfit or femininity alone does not generate persistent disorganization.
7. **Ordinary defeat does not acoustically resemble identity collapse.**
8. **Fragmentation is multifunctional.** It can mark romantic self-exposure, deliberate comedic/rhetorical timing, long expository structure, physical reaction, or performance rehearsal.

---

# 6. Professional baseline and action fluency

Baltimore's ordinary professional voice is neither monotone nor uniformly low.

Representative base lines include:

- `login`: ~306.0 Hz, pause ratio 0.115 — immediate work-start framing;
- `mission`: ~253.4 Hz, 0.186 — checks the mission list and operationalizes the task;
- `main:0`: ~240.7 Hz, 0.141 — direct competence/role statement;
- `detail`: ~273.2 Hz, 0.242 — longer reasoning about choosing what can/should be done;
- `expedition`: ~295.3 Hz, 0.161 — volunteers for the next assignment.

The wide placement range demonstrates that professional competence is **not a fixed pitch target**.

The stable feature is better described as:

> **When the role is clear, Baltimore can move directly into organized utterance structure. Activation then depends on urgency, enthusiasm, and projection demand rather than uncertainty about what she is supposed to do.**

This provides performed support for H2 competence identity and H6 distributed/actionable competence without changing their semantic content.

---

# 7. Combat, challenge, and projected action

Combat is Baltimore's clearest high-activation / high-continuity state.

Across the 11 combat-category records:

- median F0: **288.8 Hz**;
- median pause ratio: **0.086**;
- median substantial-pause count: **0**;
- active level: ~**−16.59 dBFS**.

The four `battle` slots are even more projected:

- median F0: **320.1 Hz**;
- median pause ratio: **0.049**;
- median substantial-pause count: **0**.

Diagnostic base lines:

| Record | Median F0 | Pause ratio | Interpretation |
|---|---:|---:|---|
| `103160:battle:0` | **392.5 Hz** | **0.046** | fleet formation command; very high projection, compact timing |
| `103160:hp_warning:0` | **374.1 Hz** | **0.000** | urgent concentration command; no internal fragmentation |
| `103160:skill:0` | **354.4 Hz** | **0.091** | decisive attack timing |

The race-helper battle line (`103165:battle:0`) likewise reaches ~344.8 Hz with a pause ratio of 0.051.

This matters for R5's challenge/combat activation channel:

> **Activation in competent action is acoustically energetic without being temporally disorganized.**

The performed corpus therefore strengthens the distinction between **forward-pressure activation** and **loss of cognitive organization**. High activation does not mean panic.

---

# 8. Ordinary defeat is not performed as identity collapse

Baltimore's two mapped `lose` records center around:

- median F0: ~249.7 Hz;
- median pause ratio: ~0.116.

The base loss line — `正しい道でも躓きがあるものだな……` — is ~278.0 Hz with a pause ratio of only **0.051** and no substantial internal pause.

The race-helper loss line — encouragement to the Commander not to remain discouraged — is lower (~221.3 Hz) but still comparatively continuous (0.182).

This does not prove how Baltimore responds to grave irreversible failure. R5/R8 correctly leave that C4 domain open.

It does support a narrower C1/C2 performed rule:

> **Routine defeat or setback is localized and kept cognitively organized rather than acoustically rendered as broad self-collapse.**

This is consistent with H7's bounded low ego-defense around ordinary/correctable failure.

---

# 9. Affinity progression: the first major acoustic discontinuity is role recognition, not affection itself

The base affinity sequence is especially informative because it moves from moral/professional familiarity into explicitly romantic framing.

| State | Median F0 | Pitch span | Pause ratio | Pauses ≥250ms | Rate |
|---|---:|---:|---:|---:|---:|
| Feeling 1 | 231.7 | 11.30 st | 0.152 | 1 | 5.32 |
| Feeling 2 | 226.7 | 8.62 st | 0.182 | 2 | 6.28 |
| Feeling 3 | 231.5 | 8.64 st | 0.195 | 3 | 6.04 |
| Feeling 4 | **278.4** | 10.56 st | **0.319** | **6** | 5.22 |
| Feeling 5 | **221.3** | 7.99 st | 0.225 | 5 | 4.81 |

Feeling 1–3 remain low-to-mid in placement and progressively but modestly segmented while Baltimore moves from correction/moral concern to broad availability and help.

Feeling 4 is qualitatively different. She readily accepts shopping; the acoustic disruption arrives when the event is categorized as `デート`:

> `ついでにデートも？構わな……ちょ、ちょっと待て！デートって、あのデートか！？`

The line rises to ~278.4 Hz while fragmentation increases sharply.

Feeling 5 then demonstrates why a one-axis shyness model fails. While explicitly wrestling with “more girlish” behavior and the Commander's effect on her composure, median F0 drops to ~221.3 Hz rather than continuing upward.

Thus:

> **Romantic-role recognition can destabilize timing and sometimes raise activation, but sustained self-monitoring does not require high pitch.**

This is one of the strongest acoustic confirmations of the R6 two-axis model.

---

# 10. CMD3 oath: declarative commitment and ceremonial disruption coexist

The base oath record (`103160:propose:0`) measures approximately:

- median F0: **254.9 Hz**;
- robust span: **15.45 semitones**;
- pause ratio: **0.226**;
- substantial pauses: **6**;
- active level: **−18.56 dBFS**;
- rate proxy: **4.21 chars/active-s**.

Textually the line contains two different operations:

1. clear, sincere lifelong commitment;
2. uncertainty/reactivity around what happens after the ring/ceremony.

The unusually broad pitch span plus relatively slow active delivery are compatible with that mixed state, but the waveform alone cannot assign each micro-transition without direct listening/alignment.

The safe performed rule is:

> **Oath significance does not erase Baltimore's capacity for strong declarative commitment, but ceremonial execution creates additional temporal and pitch variation.**

Do not model CMD3 as either a flat solemn voice or a continuous panic performance.

---

# 11. CMD4 established intimacy: security changes permission and baseline behavior more than it creates one fixed acoustic target

The post-oath extra-state material is particularly valuable because it shows established closeness while retaining Baltimore's recognizable reactivity.

## 11.1 Matched base/post-oath context comparisons

| Context | Base | Post-oath extra state | Implication |
|---|---|---|---|
| `home` | 292.4 Hz / pause 0.116 | 255.7 Hz / 0.295 | post-op care expands into checking + invitation to accompany; longer/more relational line, not simple softness |
| `login` | 306.0 / 0.115 | 280.8 / 0.252 | work remains energetic but becomes explicitly shared |
| `touch2` | 364.2 / 0.252 | 302.4 / 0.224 | contact reactivity persists but pitch activation is reduced in this pair |
| `touch` | 360.5 / 0.289 | 266.5 / 0.315 | changed content prevents a pure relationship-only causal attribution |
| `feeling5` | 221.3 / 0.225 | 255.6 / 0.291 | established bodily ease coexists with renewed disruption when the relationship is verbally categorized |

The post-oath `feeling5` line is especially diagnostic. Baltimore asks to lean on the Commander because she is tired — an embodied intimacy act executed without needing a ritualized romantic script — but becomes nervous when “that kind of relationship” is explicitly named. It has **11 substantial pauses** and a pause ratio of ~0.291.

By contrast, the post-oath headtouch line `好きなだけ撫でればいいさ！` is ~306.5 Hz with **0.000 internal-pause ratio** under the fixed detector.

That asymmetry is extremely important:

> **Established physical permission can be direct and temporally fluent even while explicit relationship categorization remains self-monitoring-sensitive.**

This is performed evidence for R6's separation of relationship security/embodied comfort from romantic-role fluency.

---

# 12. CMD5 committed self-authored intimacy: lower average activation, high verbal significance, preserved local startle

The bridal/committed skin (`103168`) is the strongest current CMD5 performed witness.

Its skin center is:

- N = 11;
- median F0: **241.9 Hz**;
- median robust span: **9.91 st**;
- median pause ratio: **0.312**;
- median substantial-pause count: **5**;
- median active level: **−18.72 dBFS**;
- median rate: **4.61 chars/active-s**.

It has one of the lowest skin-level F0 centers and by far the highest skin-level fragmentation.

That combination directly rejects:

```text
more romance → higher pitch
```

and also rejects:

```text
secure intimacy → no hesitation
```

## 12.1 Deliberate confession

`103168:feeling5:0`:

- ~234.9 Hz;
- pause ratio **0.384**;
- **11 substantial pauses**;
- rate ~4.50.

The text explicitly says Baltimore cannot keep escaping because she is embarrassed/nervous, deliberately composes herself, and says `愛してる`.

The best model is not “she remains too shy to act.” It is:

> **high relational significance + deliberate self-regulation + successful affectionate action through residual fragmentation.**

## 12.2 Marriage label

`103168:unlock:0`:

- ~241.9 Hz;
- pause ratio **0.330**;
- **11 substantial pauses**;
- rate ~4.09.

The disruption centers on verbalizing `ケッコン` and being teased about the category.

This is a clean CMD5 example of persistent **role-label friction after relationship security is already high**.

## 12.3 Hand request and chosen proximity

`103168:login:0` — asking for the Commander's hand — sits around ~229.4 Hz with a pause ratio of ~0.346.

`103168:home:0` — inviting the Commander to rest beside her — is ~247.0 Hz / 0.324.

`103168:main:2` — asking the Commander to come closer while removing a petal — is ~237.4 Hz / 0.312.

The behavior is increasingly agentic even though the timing remains segmented.

## 12.4 Contact/startle remains available

The same committed skin contains:

- ordinary touch: ~**362.8 Hz**, pause ratio 0.150;
- special touch: ~**349.5 Hz**, pause ratio 0.171.

Thus the corpus supports:

> **Security and agency do not extinguish localized bodily/startle activation.**

A simulator that makes established Baltimore permanently low-pitched and unreactive would therefore be less faithful, not more mature.

---

# 13. Touch/startle is a special high-activation state, not a romance meter

Across the six mapped `touch2` records:

- median F0: **360.9 Hz**;
- robust pitch span: **12.54 st**;
- pause ratio: ~0.197;
- rate proxy: ~3.24 chars/active-s.

The highest-F0 utterance in the whole corpus is `103165:touch2:0` at approximately **450 Hz**. Other high points include:

- `103162:touch2:0`: ~399.5 Hz;
- base `touch2`: ~364.2 Hz;
- `103161:touch2:0`: ~357.6 Hz;
- bridal ordinary touch: ~362.8 Hz;
- bridal special touch: ~349.5 Hz.

These occur across very different costume/relationship contexts.

Therefore:

> **A sharp contact/startle response is a reusable performed event, not a direct estimate of romantic insecurity or relationship stage.**

Relationship state can modulate its magnitude in some matched material, but it does not remove the response class.

This is a major anti-caricature rule for voice simulation.

---

# 14. Self-authored presentation is acoustically distinct from compulsory romantic-role fluency

R5/R6 argued that Baltimore's presentation discomfort is not generalized modesty; self-authorship, task legibility, and practice matter.

The voice corpus strengthens this.

## 14.1 Race-helper / competition context (`103165`)

Despite conspicuous presentation and race-queen framing:

- skin median F0: ~263.0 Hz;
- pause ratio: **0.176**;
- rate: **5.81**.

Baltimore talks about taking the helper responsibility seriously, cheering, racing, movement, and doing the job without regret. The skin is more temporally continuous and faster than the committed bridal skin.

Its most extreme disruption is localized — especially `touch2` — rather than generalized across the role.

## 14.2 Dark/cool sport-social presentation (`103162`)

This skin centers around ~244.4 Hz / pause 0.184. Baltimore can discuss Bremerton's styling advice, tennis competence, inviting the Commander, and playing with a deliberately “cool” persona without persistent timing collapse.

## 14.3 Travel/leisure (`103164`)

This is one of the lowest-F0 skin centers (~241.7 Hz) while remaining relatively continuous (0.178). Baltimore discusses travel styles, sightseeing, companions, sport curiosity, and role-play jokes fluidly.

## 14.4 Formal dress / dance (`103163`)

This context provides the useful exception. The skin center itself is not dramatically fragmented (~0.198), but specific unfamiliar-role moments spike:

- dance rehearsal/home: ~324.7 Hz;
- back/exposure surprise: ~351.9 Hz / pause ~0.301;
- explicit concern over whether the dress looks strange: lower F0 but self-monitoring text.

The safe conclusion is:

> **Presentation difficulty is event- and authorship-sensitive, not clothing-category-sensitive.**

This independently STRENGTHENS the R5 H4 revision without converting it into a universal acoustic rule.

---

# 15. Peer/action lines: direct relational concern can remain highly continuous

The two relationship-specific base lines are short but useful controls:

- Wichita warning: ~275.6 Hz, pause ratio ~0.077;
- combination/team line: ~287.4 Hz, pause ratio 0.000, very high rate proxy.

These lines support an action-oriented peer register in which care/coordination can be direct and compressed.

However, most of R6's named-peer relationship evidence is narrative/social text rather than mapped voiced dialogue. Therefore this performed corpus does **not** license a full acoustic Bremerton-vs-Memphis-vs-Enterprise-vs-Hornet voice matrix.

Simulation must keep the order:

```text
R6 determines relationship modifier
→ R7 determines JP wording/register
→ this profile selects a compatible performed state where evidence exists
```

Do not invent peer-specific timbres or prosodic signatures from textual relationship differences alone.

---

# 16. High- and low-F0 counterexamples

The highest-F0 records are not a single emotion class. They include:

- touch/startle;
- battle command;
- HP warning;
- skill execution;
- formal-presentation surprise;
- committed-intimacy contact surprise.

Likewise, the lowest-F0 records include:

- reflective/moral MVP language;
- Feeling 5 self-monitoring;
- race-helper loss encouragement;
- bridal attractiveness/self-presentation question;
- moral/professional affinity lines;
- travel conversation.

Consequences:

- **REJECT** `high pitch = embarrassment`.
- **REJECT** `low pitch = intimacy`.
- **REJECT** `combat intensity = temporal chaos`.
- **REJECT** `romantic maturity = uniformly low pitch`.

---

# 17. Fragmentation counterexamples

The most fragmented lines include strongly romantic material, but not only romantic material.

Examples include:

- bridal explicit confession — pause ratio ~0.384;
- bridal marriage-label line — ~0.330;
- post-oath relationship-label Feeling 5 — ~0.291 with 11 substantial pauses;
- base date-label Feeling 4 — ~0.319;

But high fragmentation also appears in:

- `103161:main:2` receiving a drink and exhaling — **0.422**;
- `103162:win_mvp:0` extended dark-role joke — **0.373**;
- long profile/introduction material;
- performed comic/persona rehearsal.

Therefore:

> **Fragmentation is a temporal architecture, not an emotion label.**

Romantic-role self-monitoring is one recurring cause; utterance length, rhetorical staging, physical reaction, role-play, and deliberate reaction space are others.

This is why the profile uses semantic context plus acoustic shape rather than statistical threshold alone.

---

# 18. Final performed-state matrix

| State | Activation/projection | Temporal continuity | Current interpretation |
|---|---|---|---|
| routine professional action | moderate, variable | moderate-high | clear role; organized execution |
| urgent command / combat | high–very high | **high** | outward projection and action commitment |
| ordinary setback | low-moderate to moderate | high | localized failure; no identity collapse evidence |
| shared activity / competition | moderate-high | high | activation without social disorganization |
| self-authored presentation | moderate, context-sensitive | generally high | role accepted as task/play/performance |
| contact/startle | often very high | short localized disruption | bodily/reactive event, not relationship-stage meter |
| CMD2 romantic-label recognition | moderate-high | low-moderate | category recognition can disrupt phrase connection |
| CMD3 oath | moderate | moderate-low | declarative commitment + ceremonial transition |
| CMD4 established embodied comfort | moderate, variable | often higher for direct permission; can fragment when relationship is named | security rises faster than role-label fluency |
| CMD5 chosen affection / verbal significance | often low-moderate | often low | deliberate intimacy through residual nervousness |
| CMD5 local contact/startle | high | moderate-high after initial spike | security does not erase reactivity |
| unfamiliar formal-role rehearsal | variable, can spike | variable | self-monitoring/practice-dependent |

---

# 19. Relationship-security versus romantic-role-fluency audit

R6 proposed two partially independent Commander axes:

```text
RELATIONSHIP SECURITY / EMBODIED COMFORT
ROMANTIC-ROLE / CEREMONIAL FLUENCY
```

The performed corpus independently supports that architecture.

### Evidence for rising security/comfort

- post-oath permission for headtouch is temporally direct;
- leaning when tired is initiated by Baltimore;
- post-operation checking becomes accompaniment-seeking;
- work becomes explicitly shared;
- CMD5 Baltimore requests a hand, proximity, shared rest, and explicit affection.

### Evidence that role-label friction can remain

- Feeling 4 `デート` recognition sharply disrupts timing;
- Feeling 5 introspection remains slow/segmented without needing high pitch;
- oath ritual transition increases pitch range and segmentation;
- post-oath “that kind of relationship” wording renews hesitation after embodied comfort is already present;
- bridal `ケッコン` wording remains highly segmented;
- explicit confession is slow and fragmented but successfully completed.

### R6 claim transition

`RELATIONSHIP_SECURITY_VS_ROMANTIC_ROLE_FLUENCY`:

**STRENGTHEN** — from high textual/behavioral confidence to high multimodal confidence within the mapped JP character-text domain.

The correction is not “Baltimore is secretly more shy than text suggests.” It is:

> **Her performed Japanese voice preserves the same asymmetry already visible in behavior: she can increase agency and bodily closeness while conventional romantic labels and rituals continue to consume extra temporal organization.**

---

# 20. Impact on H1–H10 and R8 simulation

No semantic hypothesis requires reversal.

| Claim | Performed-pass transition | Reason |
|---|---|---|
| H1 protective practical idealism | PRESERVE | acoustic data does not alter semantic moral model |
| H2 competence through useful action | STRENGTHEN, performed realization only | task/command states remain organized across activation levels |
| H3 phase-dependent risk appetite | STRENGTHEN, bounded | combat activation is high and compact; audio does not itself prove decision risk magnitude |
| H4 self-authorship-sensitive presentation | STRENGTHEN | conspicuous self-authored/task-framed skins remain comparatively fluent; formal-role exceptions are localized |
| H5 sincere/self-aware hero performance | PRESERVE | role-play and projected lines coexist; performance does not imply parody |
| H6 distributed competence | PRESERVE | audio adds delivery evidence, not new authority structure |
| H7 low ego-defense ordinary failure | STRENGTHEN, ordinary-failure boundary only | mapped loss lines do not acoustically collapse; grave failure stays OPEN |
| H8 action-mediated care | PRESERVE + SUPPORT | post-op care and direct peer concern remain action-oriented; refusal edge still OPEN |
| H9 safe-challenge activation | STRENGTHEN, performed realization | competition/action skins support energetic organized activation |
| H10 moral anger/escalation | PRESERVE | mapped character-text audio lacks enough severe anger cases to alter R5 causal ceiling |

R8's weakest-link rule remains unchanged. Acoustic confidence cannot upgrade an underlying C4/C5 semantic uncertainty.

For example:

- a severe unjust-order conflict remains C4 even if Baltimore's command-state acoustics are well modeled;
- surrendered-atrocity response remains open even if moral rhetoric has known pitch/timing patterns;
- grave guilt remains open even though ordinary defeat is acoustically bounded.

---

# 21. Simulation-facing performed-voice recipe

A high-fidelity JP Baltimore generation pipeline should execute in this order:

```text
1. Resolve semantic situation from R4/R5/R8.
2. Resolve relationship state/modifier from R6.
3. Resolve Japanese wording/register from R7.
4. Determine performed state on:
      A. activation/projection
      B. temporal continuity/fragmentation
5. Apply state-compatible pitch/timing/rate tendencies.
6. Preserve uncertainty where no performed analogue exists.
7. Do not invent timbre/prosody qualities requiring direct audition.
```

## 21.1 High-confidence construction rules

### Professional / task state

- organized cadence;
- moderate pitch placement with substantial legitimate variation;
- urgency may elevate projection without introducing hesitation.

### Combat / command

- high projection is allowed and often expected;
- internal timing should stay compact;
- do not render high F0 as panic.

### Ordinary failure

- keep the response localized;
- do not automatically add long broken pauses or voice-collapse behavior.

### CMD2 label shock

- disruption may occur at the **category change** rather than throughout the whole interaction;
- shopping/shared activity can be fluent before `デート` becomes salient.

### CMD3 oath

- permit clear commitment statements;
- ceremonial transition may broaden pitch movement and segment timing;
- avoid constant stammering from first word to last.

### CMD4 established intimacy

- physical permission and shared routine can be direct;
- explicit relationship labeling may still reintroduce segmentation;
- touch/startle spikes remain possible.

### CMD5 committed intimacy

- do not equate maturity with total acoustic smoothness;
- deliberate affection may be lower/mid in average pitch yet highly segmented;
- the key developmental signal is successful affectionate agency through residual disruption.

### Self-authored presentation / competition

- preserve energetic organized delivery;
- do not add generalized embarrassment merely because clothing is conspicuous or feminine.

### Unfamiliar formal-role presentation

- allow localized self-monitoring, rehearsal, or surprise;
- do not propagate one reaction across the entire context.

---

# 22. Negative constraints / low-fidelity voice patterns

A simulator should reject or strongly penalize the following:

1. **Constant high-pitched Baltimore.** Her corpus spans low/mid reflective speech, high projected action, and localized spikes.
2. **Constantly low “tomboy” Baltimore.** Combat and contact can rise dramatically.
3. **High pitch as a universal shyness classifier.** The highest lines are dominated by touch/startle and action projection.
4. **Low pitch as a universal intimacy classifier.** Low records include moral, travel, loss, and self-reflective material.
5. **Every romantic line stammered from beginning to end.** Baltimore often speaks coherently within phrases; significance is frequently expressed through phrase-level segmentation.
6. **Established intimacy erases embarrassment/startle.** CMD5 retains high-F0 contact reactions.
7. **Revealing/feminine clothing automatically causes weak or hesitant speech.** Race-helper and other presentation contexts falsify that.
8. **Combat activation rendered as panic or cognitive collapse.** Combat is among the most temporally compact states.
9. **Many pauses automatically interpreted as insecurity.** Pause count is strongly related to duration/text length and can serve rhetoric, comedy, physical response, or role-play.
10. **Skin medians treated as personality modes.** Skin selection and recording-session effects are confounds.
11. **JP acoustic realization used to overwrite CN semantic authority.** The authority layers remain distinct.
12. **Invented ear-dependent descriptors.** No “husky,” “breathy,” “warm,” “smiling,” “raspy,” etc. without direct perceptual evidence.

---

# 23. What this pass can and cannot say about timbre

## Established quantitatively

The mapped corpus supports stable quantitative statements about:

- relative pitch placement;
- robust within-line pitch excursion;
- temporal segmentation;
- active speech level;
- rate proxy;
- context-conditioned transitions between compact projection and segmented relational/presentation states.

## Still OPEN

Without a direct listening channel this pass does not establish:

- perceived timbral weight or brightness;
- breathiness/airiness;
- rasp/fry/creak;
- resonance placement;
- perceived softness independent of RMS level;
- “smiling voice” quality;
- exact emotional color of individual pauses;
- fine emphasis placement at syllable/mora level;
- actor-specific aesthetic descriptors;
- whether a listener would characterize a state as warm, cool, teasing, tender, stern, husky, boyish, etc.

A later direct perceptual audit could add those descriptors **without reopening the quantitative corpus lock**.

---

# 24. Monograph impact

The active-provisional monograph should now treat Baltimore as having:

```text
TEXTUAL_BEHAVIORAL_MODEL: ESTABLISHED C1–C3 WITH BOUNDED C4–C5 EDGES
RELATIONSHIP_MODEL: ESTABLISHED CMD0–CMD5 + NAMED-PEER MODIFIERS
MULTILINGUAL_TEXT_MODEL: ESTABLISHED CN/JP/EN/TW/KR
JP_QUANTITATIVE_PERFORMED_VOICE_MODEL: ESTABLISHED
EAR_DEPENDENT_TIMBRE_MODEL: OPEN
```

The most important addition is not a new personality trait. It is a new realization layer:

> **JP Baltimore should be generated by resolving behavioral/relationship state first and then selecting a compatible activation × continuity acoustic state. Romantic development is audible primarily as changing organization and state-routing, not as a simple monotonic pitch shift.**

No R4–R8 semantic claim should be silently rewritten from acoustics alone.

---

# 25. Final verdict and promotion handoff

### Final verdict

`BALTIMORE_JP_VOICE_PERFORMANCE_PROFILE_PASS_WITH_TWO_AXIS_ACOUSTIC_MODEL_AND_EAR_DEPENDENT_TIMBRE_OPEN`

The 100/100 mapped JP spoken-text surface is now exhaustively measured and provenance-verified.

The pass establishes:

- a complete quantitative JP performed layer over the current mapped speech corpus;
- combat/directive high-projection + high-continuity behavior;
- bounded ordinary-failure realization;
- affinity-stage differentiation;
- CMD2 category/label disruption;
- CMD3 oath significance with mixed declarative control and ceremonial disruption;
- CMD4 increased embodied permission without total loss of reactivity;
- CMD5 deliberate affection through residual temporal fragmentation;
- strong acoustic support for the R6 relationship-security versus romantic-role-fluency distinction;
- strong support for R5's self-authorship-sensitive presentation model;
- contact/startle as a distinct high-activation performed event;
- explicit anti-caricature rules for JP simulation.

It leaves only ear-dependent timbral/aesthetic interpretation open inside the performed-voice responsibility.

### Next canonical boundary

The next logical corpus operation is **claim integration / promotion readiness**, not another broad character reread. The current map already anticipates a claim-revision ledger and final promotion audit.

Recommended sequence:

1. integrate the performed-voice constraints into the active-provisional monograph;
2. create/update the Baltimore claim-revision ledger if materially useful for tracing R0–R8 → performed-layer transitions;
3. run a **final promotion audit** asking whether the monograph can move from `active_provisional` to `canonical` while explicitly retaining:
   - C4–C5 abstention boundaries;
   - ear-dependent timbre as OPEN unless separately auditioned;
   - the nine-scene identity quarantine;
   - the frozen pre-remediation 82.91 readiness score.

No new parallel Baltimore reconstruction root is warranted.
