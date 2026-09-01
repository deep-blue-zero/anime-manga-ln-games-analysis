---
series: AZUR_LANE
artifact_type: specialist_synthesis
scope: TAKAO_30311_JP_VOICE_PERFORMANCE
generation: V1
status: canonical
source_boundary: JP client AZL 9.3.386 / CV 1243; 114 mapped Takao JP performed-voice WAV utterances; 8 confirmed unvoiced textual fields; 1 classified non-text gift/UI reaction excluded from mapped-dialogue analysis
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
semantic_authority: CN
performed_locale: JP
asset_downloader_version: 4.7.1
vgmstream_version: r2083
audio_client_version: AZL 9.3.386 / CV 1243
performed_voice_scope: quantitative acoustic realization, timing, projection, context-conditioned state transitions
direct_perceptual_listening_status: not directly auditioned in this analysis environment
ear_dependent_timbre_status: open
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Takao JP Voice Performance Profile

## Acoustic Performance, Contextual State Transitions, and Simulation Constraints

## 0. Authority, scope, and use

This document is the current V1 specialist authority for **Takao / 高雄 / group ID 30311's Japanese performed-voice realization** under the source boundary stated above.

It supplements, but does not replace, `AZUR_LANE_TAKAO_CHARACTER_MONOGRAPH.md`.

Authority is intentionally layered:

```text
CN originating text / narrative / observed behavior
    → semantic character reconstruction

JP published text
    → Japanese linguistic realization

JP mapped source audio
    → Japanese performed realization

this specialist profile
    → acoustic and context-conditioned performance rules
```

The profile may strengthen or refine an existing psychological claim when the audio independently supports how that state is realized. It does **not** make Japanese performance the originating semantic authority.

This artifact is `canonical` for the acoustic/performance responsibility defined in its front matter. That does **not** mean every conceivable property of the voice has been solved. In particular, this environment did not directly audition the clips through a human-style listening channel. Claims that require ear-dependent judgments such as exact timbral adjectives, perceived breathiness, vocal-fry quality, "smiling voice," or actor-specific aesthetic impressions remain OPEN unless separately reviewed.

The canonical claim here is narrower and stronger:

> **Takao's mapped Japanese performance corpus is complete enough to reconstruct stable quantitative performance tendencies, context-conditioned state changes, and anti-caricature constraints across professional, combat, affinity, embarrassment, leisure, presentation, protection, oath, and established-intimacy conditions.**

---

# 1. Source condition and corpus completeness

The analysis uses **114 mapped performed utterances** decoded from the verified JP client source archive.

Technical derivative state:

- source audio: CRI HCA streams inside original client `.b` bundles;
- derivative format: RIFF/WAVE, PCM signed 16-bit;
- sample rate: 44.1 kHz for all mapped Takao derivatives;
- channels: mono for all mapped Takao derivatives;
- signal processing: NONE;
- trimming: false;
- normalization: false;
- resampling: false;
- mapped WAV QA: PASS;
- one additional `present_like` asset is archived as a classified gift/UI reaction without a published JP dialogue record and is excluded from the 114-line mapped-dialogue analysis.

The source package therefore supports utterance-level tracing:

```text
JP text record
→ voice key / client resource
→ original source bundle + subsong
→ PCM WAV
→ Drive ID / checksum
→ acoustic measurements
```

The eight Takao skin IDs represented in the mapped corpus are:

- `303110` — base / standard, including corrected post-oath extra-state material;
- `303112` — beach / competition / leisure;
- `303113` — calligraphy / Chinese-dress;
- `303114` — school / unfamiliar self-presentation;
- `303115` — modeling / photography;
- `303116` — 艦忍 / action-protection;
- `303117` — 心法 / deliberate performance;
- `303118` — bridal / established-intimacy control.

These descriptors are analytical routing labels, not assertions about official skin titles.

---

# 2. Three-pass analytical method

The performed-voice reconstruction used three sequential reasoning passes over one fixed evidence corpus.

## Pass 1 — diagnostic anchors

The first pass emphasized high-information contrasts:

- professional baseline;
- affinity progression;
- oath;
- base → post-oath matched pairs;
- contact/self-exposure;
- combat / command / defeat.

Its purpose was to discover candidate state variables.

## Pass 2 — breadth and skin challenge

The second pass expanded to 64 clips spanning all eight skin IDs and deliberately tested whether the initial rules survived:

- leisure;
- competition;
- school;
- calligraphy;
- modeling;
- protection/action;
- deliberate performance;
- bridal domestic/relational material.

This pass produced the key distinction between **activation** and **temporal disruption**.

## Pass 3 — exhaustive adversarial audit

The third pass measured and reviewed the remaining 50 mapped utterances, bringing the sweep to **all 114 mapped clips**.

Its purpose was not to accumulate confirmation. It was to identify:

- counterexamples;
- mundane controls;
- skin-specific exceptions;
- alternate causes of pause fragmentation;
- cases where high pitch does not mean embarrassment;
- cases where procedural control coexists with high activation.

The exhaustive pass revised one important formulation:

```text
Pass-2 shorthand:
activation × self-monitoring

Final measurable model:
activation / projection
        ×
temporal continuity / fragmentation
```

"Self-monitoring," "strain," "rhetorical timing," and other psychological causes are inferred only after the acoustic pattern is combined with source context and text.

---

# 3. Measurement definitions

All 114 mapped utterances were reprocessed under one standardized measurement configuration.

## 3.1 Pitch

- Praat-style autocorrelation F0 tracking;
- frame step: 10 ms;
- analysis bounds: 75–700 Hz;
- baseline pitch statistic: median F0;
- robust pitch excursion: p10–p90 span expressed in semitones;
- raw minima/maxima are not used as the principal range measure because octave errors and transient tracking artifacts make them unstable.

## 3.2 Timing and activity

Within-clip energy gating was used to estimate:

- active-speech duration;
- leading and trailing silence;
- internal pause ratio;
- substantial pause count;
- substantial pause duration.

A "substantial" pause is ≥250 ms in the analysis used for the three-pass comparisons.

## 3.3 Level

Active-speech RMS level is reported in dBFS.

Cross-skin level differences are treated cautiously because different recording/mastering sessions may be a confound. Same-source or exact matched pairs are stronger evidence.

## 3.4 Speaking-rate proxy

The rate measure is:

> Japanese content characters per active-speech second.

It is **not** claimed to be syllables/sec or morae/sec.

## 3.5 Corpus center

Across all 114 mapped utterances:

- corpus median F0: **226.0 Hz**;
- median robust p10–p90 pitch span: **9.9 semitones**;
- median internal-pause ratio: **0.290**;
- median active level: **-17.7 dBFS**;
- median rate proxy: **6.05 JP characters / active second**;
- total analyzed mapped duration: **17.5 minutes**;
- median utterance duration: **8.8 seconds**.

These corpus-wide medians are descriptive baselines, not a definition of the "correct" Takao voice in every state.

---

# 4. Skin-level exhaustive summary

| Skin ID | Analytical context | N | Median F0 | Median p10–p90 span | Median internal-pause ratio | Median active level | Median rate proxy |
|---|---|---:|---:|---:|---:|---:|---:|
| `303110` | Base / standard + post-oath extra-state | 37 | 223.4 | 8.3 st | 0.267 | -13.2 dBFS | 6.37 |
| `303112` | Beach / competition / leisure | 9 | 263.8 | 11.2 st | 0.325 | -17.7 dBFS | 6.01 |
| `303113` | Calligraphy / Chinese-dress | 8 | 227.2 | 11.3 st | 0.293 | -18.7 dBFS | 6.44 |
| `303114` | School / unfamiliar self-presentation | 9 | 232.1 | 11.1 st | 0.318 | -16.0 dBFS | 5.82 |
| `303115` | Modeling / photography | 10 | 226.5 | 11.0 st | 0.304 | -17.9 dBFS | 5.44 |
| `303116` | 艦忍 / action-protection | 16 | 218.1 | 9.7 st | 0.295 | -18.0 dBFS | 6.26 |
| `303117` | 心法 / deliberate performance | 11 | 227.3 | 10.4 st | 0.302 | -18.0 dBFS | 5.73 |
| `303118` | Bridal / established-intimacy control | 14 | 214.3 | 9.8 st | 0.280 | -19.3 dBFS | 6.28 |

Several things are immediately visible.

First, skin means are not personalities. Each skin selects different scenarios and therefore different state distributions.

Second, the **bridal / established-intimacy skin (`303118`) has the lowest skin-level median F0, 214.3 Hz**, despite containing battle, mission, mail, embarrassment, domestic, and relationship content rather than only quiet love declarations.

Third, the **beach skin (`303112`) has the highest skin-level median F0, 263.8 Hz**. Leisure therefore cannot be equated with low activation.

Fourth, the action/protection skin (`303116`) has a comparatively low overall median F0, 218.1 Hz, even though it contains danger and combat. Operational organization is not acoustically identical to elevated pitch.

---

# 5. Executive performed-voice model

The strongest current formulation is:

> **Takao's Japanese performance is not governed by a single "stern ↔ soft" or "calm ↔ emotional" axis. It is better modeled as the interaction of activation/projection and temporal continuity/fragmentation. Context then determines whether a given combination corresponds to competent action, competition, command, physical strain, romantic self-exposure, surprise, presentation anxiety, or secure intimacy.**

The most important state rules are:

1. **Clear procedure preserves organization, not necessarily low activation.**
2. **Projected command and acute embarrassment can both raise F0 dramatically, but command remains compact and action-organized while embarrassment is more likely to show disfluency, slower active delivery, or self-correction.**
3. **Sustained emotional self-exposure often manifests more through temporal fragmentation than through high pitch.**
4. **Oath/commitment is not acoustically identical to established intimacy.**
5. **Secure intimacy lowers relational activation and reduces the amplitude of embarrassment without removing modesty or Takao's formal/martial identity.**
6. **Protective action can precede self-conscious awareness; embarrassment may occur only after the danger has been handled.**
7. **Leisure and trivial competition can produce substantial activation without loss of control.**
8. **Failure can produce low-pitch fragmentation; pause-heavy delivery is therefore not automatically evidence of relational vulnerability.**

---

# 6. Stable baseline: professional and competence-centered Takao

Takao's ordinary working voice is dynamic rather than monotone.

Professional/task-oriented lines commonly occupy the low-to-mid 200 Hz region, but there is meaningful pitch range inside individual utterances. For example, the base `detail` proverb about persistent training sits near 191 Hz median F0 while still spanning about 7.8 semitones robustly. The base `login` command-awaiting line sits substantially higher, near 255 Hz.

This variation matters:

> **Professional control is better identified by organized cadence and task orientation than by one narrow pitch target.**

The exhaustive residual sweep reinforces this. Mail, mission, expedition, upgrade, homecoming, profile, and routine secretary lines form a large body of ordinary competent speech that is neither permanently low nor theatrically severe.

### C2 performed rule

When Takao has a clear professional role:

```text
goal is explicit
→ action selection is immediate
→ timing tends to remain coherent
→ pitch may vary with urgency/projection
→ little evidence of generalized social hesitation
```

This independently strengthens the monograph's claim that duty is easier for Takao than ambiguity.

---

# 7. Procedure, ambiguity, and the performance of self-control

The monograph states that Takao proceduralizes uncertainty. The performed corpus strongly supports this, with one important clarification.

Procedure does **not** necessarily lower F0.

It lowers **behavioral ambiguity**.

Examples:

- beach competition can be highly activated while remaining coherent;
- calligraphy urgency can raise pitch without creating romantic-style disorganization;
- modeling becomes more controlled when posing/smiling is reframed as a trainable technique;
- the 心法/performance costume becomes manageable when Takao gives herself a method;
- mission and protective lines can be rapid and highly direct.

The corrected rule is:

> **A clear procedure restores organized action and speech sequencing. The acoustic activation level then depends on the task itself.**

This distinction prevents an important error:

```text
WRONG:
clear task → low voice

BETTER:
clear task → organized performance
competition / command / urgency may still elevate projection
```

---

# 8. Affinity progression: vulnerability appears in timing before it becomes a new vocal identity

The five base affinity stages show no monotonic "more affection = higher/lower F0" curve.

| Stage | Record | Median F0 | Pause ratio | Pauses ≥250 ms | Active level | Rate proxy |
|---|---|---:|---:|---:|---:|---:|
| Feeling 1 | `303110:feeling1:0` | 202.0 | 0.188 | 1 | -12.9 | 6.38 |
| Feeling 2 | `303110:feeling2:0` | 231.0 | 0.285 | 1 | -11.5 | 7.14 |
| Feeling 3 | `303110:feeling3:0` | 205.3 | 0.204 | 2 | -14.2 | 6.37 |
| Feeling 4 | `303110:feeling4:0` | 216.6 | 0.366 | 6 | -15.8 | 6.49 |
| Feeling 5 | `303110:feeling5:0` | 207.4 | 0.384 | 6 | -14.9 | 6.67 |

The decisive change appears at Feeling 4–5.

Feeling 1–3 have relatively modest fragmentation.

Feeling 4–5 approximately double the substantial-pause count to six each, while the active speech-rate proxy remains broadly in Takao's normal range.

This implies:

> **Takao does not simply become globally slower or verbally incompetent when affection becomes threatening to her self-concept. She continues to articulate competently when speaking, but the utterance becomes harder to launch and connect across emotionally exposed phrases.**

That is a much more precise realization of the monograph's "romantic self-exposure disrupts fluency" rule.

### Important anti-caricature constraint

Do not render every affectionate Takao line as stammering high-pitched embarrassment.

Her deeper vulnerability can be:

- moderate or even low in pitch;
- articulate within phrases;
- heavily fragmented between phrases.

---

# 9. Oath is a commitment state, not merely "more intimacy"

The oath record `303110:propose:0` has approximately:

- median F0: **244.9 Hz**;
- internal-pause ratio: **0.387**;
- active level: **−13.1 dBFS**;
- rate proxy: **7.06**;
- robust pitch span: **8.3 st**.

This is a distinctive combination:

> **high relational significance + substantial hesitation + strong declarative energy.**

The oath is therefore not acoustically equivalent to later established intimacy.

A useful transition model is:

```text
growing affection
→ increasing temporal difficulty

oath / explicit commitment
→ hesitation + strong declarative mobilization

established intimacy
→ lower relational activation + increased normalization
```

This distinction should be preserved in simulation.

---

# 10. Established intimacy: lower mobilization, not personality erasure

The corrected `_ex1100` mappings create five exact base → established-intimacy comparisons.

| Matched state | Base F0 | Established-intimacy F0 | F0 shift | Active-level shift | Pitch-span shift |
|---|---:|---:|---:|---:|---:|
| Feeling 5 | 207.4 | 196.5 | -0.9 st | -3.2 dB | -0.3 st |
| Login | 255.2 | 209.4 | -3.4 st | -5.6 dB | +0.0 st |
| Normal touch | 226.6 | 177.7 | -4.2 st | -3.6 dB | +0.2 st |
| Special touch | 369.1 | 301.4 | -3.5 st | -5.6 dB | -4.8 st |
| Head touch | 251.6 | 219.0 | -2.4 st | -0.1 dB | -3.1 st |

All five matched pairs shift downward in median F0.

The mean matched shift is approximately **−2.9 semitones**.

Four of the five also move downward substantially in active level. Pitch range narrows in several pairs but not universally.

The strongest individual example is ordinary touch:

- base: about 226.6 Hz;
- post-oath extra: about 177.7 Hz.

The text also changes from startled misidentification to confident recognition:

> she knows it is the Commander and no longer needs to mobilize as though contact is an unexpected threat.

This supports the rule:

> **Relationship security reduces the amount of vocal mobilization Takao needs to manage closeness.**

It does **not** mean intimacy makes her uniformly quiet or passive.

The bridal corpus independently reproduces the same result:

- skin-level median F0: **214.3 Hz**, lowest of the eight groups;
- ordinary domestic/relational lines often sit near the low 200s;
- battle, mission, and mail competence remain intact;
- embarrassment still produces bounded excursions.

### C2 conclusion

Established intimacy:

```text
does not remove modesty
does not remove formal/martial identity
does not remove competitive or command activation

it does:
reduce surprise cost
lower relational baseline activation
make closeness easier to integrate into ordinary functioning
```

This is one of the strongest findings in the full audio corpus.

---

# 11. Contact and embarrassment: there is no single "embarrassed voice"

The highest-F0 utterances in the corpus demonstrate why pitch cannot be interpreted by itself.

Extremes include:

- `303110:skill:0` `悪・即・斬！` — ~490 Hz;
- Fourth Squadron command — ~442 Hz;
- calligraphy special-touch disruption — ~414 Hz;
- school caught-unprepared login — ~387 Hz;
- 心法 special touch — ~380 Hz;
- modeling special touch — ~372 Hz;
- base special touch — ~369 Hz.

The first two are command/attack projection, not embarrassment.

Therefore:

> **high F0 is a general activation/projection signal, not an embarrassment label.**

## 11.1 Acute boundary/surprise embarrassment

Base special touch is a prototypical acute reaction:

- median F0 ~369 Hz;
- robust span ~15.1 st;
- slower rate proxy ~4.67.

The reaction combines surprise, boundary violation, and a disfluent text.

## 11.2 Sustained self-presentation difficulty

Other lines are not pitch-extreme at all.

Modeling lines about being stared at or remaining in an embarrassing outfit can sit near ordinary pitch while preserving greater temporal fragmentation.

Thus:

```text
acute surprise
→ often high activation / large excursion

sustained awareness of being evaluated
→ may remain near ordinary pitch
→ timing can carry more of the disruption
```

## 11.3 Relationship security reduces excursion amplitude

Within-skin/context normalized special-touch behavior is particularly revealing.

The bridal special-touch objection remains a genuine normative objection, but its F0 excursion above its skin baseline is much smaller than the corresponding base/calligraphy/modeling cases.

So:

> **secure intimacy does not abolish embarrassment. It reduces the acoustic cost and recovery burden of embarrassment.**

---

# 12. Personal scrutiny: the deeper trigger is being seen without a settled presentation procedure

The school, modeling, and 心法 material narrows Takao's self-consciousness trigger beyond "femininity."

The school skin provides a nonsexual control:

- ordinary school conversation remains close to baseline;
- intentionally asking how her hairstyle looks is manageable;
- being caught before she is prepared produces one of the corpus's largest F0 excursions.

The modeling skin gives the same mechanism:

- pose-holding and smiling become manageable when reframed as training;
- becoming the object of evaluation is harder;
- direct contact sharply escalates activation.

The 心法/performance skin goes further:

- Takao can deliberately "perform naturalness";
- sustained eye-contact vulnerability generates heavy phrase fragmentation without requiring high pitch;
- direct unexpected contact again produces acute high activation.

The best current psychological-performance link is:

> **Takao is destabilized less by femininity or sociality themselves than by becoming the object of personal evaluation when she has not established a confident procedure for how she should present or respond.**

This is strong C2 reconstruction because it recurs across multiple independent skins and aligns with the preexisting textual model of self-cultivation as uncertainty management.

---

# 13. Protection and delayed self-consciousness

The 艦忍/action material demonstrates a sequential rule that is highly useful for novel-context prediction.

In a danger context Takao can:

1. identify the threat;
2. physically protect the Commander;
3. complete the safety action;
4. only then notice intimate bodily proximity;
5. become embarrassed afterward.

The clearest record is `303116:touch:0`, where protection precedes awareness of contact.

Acoustically it combines substantial activation and fragmentation, but the text establishes the temporal order.

### C2 transition rule

```text
danger
→ protective action first
→ safety confirmation
→ awareness of physical intimacy
→ delayed self-conscious reaction
```

A simulator should not make Takao freeze before protecting someone merely because the necessary protective action is physically intimate.

---

# 14. Combat, command, and defeat

Combat is not one generic vocal mode.

## 14.1 Ordinary battle declaration

Ordinary battle lines can remain close to the corpus center.

The four skin-specific `battle` lines do not all exhibit extreme F0.

## 14.2 Projected command / attack calls

The most extreme examples are highly compressed projected utterances:

- `悪・即・斬！` ≈ 490 Hz;
- `第四戦隊、付いてまいれ！` ≈ 442 Hz.

These combine high activation with decisive task organization.

## 14.3 Defeat / physical-failure realization

Defeat moves in the opposite direction.

Base defeat:

- ~205 Hz;
- high temporal fragmentation;
- text immediately resolves toward "next time I won't lose."

Action-skin defeat:

- ~201 Hz;
- one of the highest pause ratios in the corpus;
- short text marked by failure/strain.

This proves that:

> **low pitch + fragmentation is not specific to romantic vulnerability.**

The contextual cause differs.

It also strengthens the monograph's failure model: the performed line registers the cost of failure, while the semantic response remains oriented toward recovery rather than resentment.

---

# 15. Leisure and competition

The exhaustive skin results decisively reject "off-duty Takao = subdued Takao."

The beach skin has the highest median F0 of the eight groups: **263.8 Hz**.

The same setting contains:

- recognition that rest is necessary;
- ordinary beach conversation;
- volleyball challenge;
- swimming/competition references;
- obsessive sandcastle rematch energy.

The stable rule is:

> **Takao can relax, but a clear competitive frame can immediately reactivate serious effort even in trivial leisure domains.**

This strongly reinforces the textual `practice → rematch → improvement` pattern.

---

# 16. Skin-specific boundary conditions

## `303112` — beach / competition

Best evidence that leisure and activation coexist.

Do not render rest as emotional flatness.

## `303113` — calligraphy

Best evidence that a non-martial activity can become a competence domain.

Task urgency can raise F0 sharply without embarrassment.

## `303114` — school

Best nonsexual test of presentation uncertainty.

Being unexpectedly caught unprepared matters more than voluntarily asking for evaluation.

## `303115` — modeling

Best sustained evidence for self-presentation difficulty.

Also demonstrates that turning posing/smiling into trainable techniques restores organization.

## `303116` — action / protection

Best evidence for protection preceding self-consciousness.

Also demonstrates that danger need not produce high-pitch panic.

## `303117` — 心法 / performance

Best evidence that deliberately performing "naturalness" differs from actually feeling natural.

Sustained eye-contact vulnerability is temporally fragmented without necessarily being pitch-extreme.

## `303118` — bridal

Best independent control for established intimacy.

Shows low relational activation without loss of martial, operational, or modest behavior.

---

# 17. Japanese samurai register in performance

The existing JP textual model remains authoritative for:

- `拙者`;
- `指揮官殿`;
- relationship-sensitive `そなた`;
- archaizing forms such as `〜ぬ`;
- martial lexical framing.

The acoustic analysis does not justify replacing that textual description with an actor-impression label such as "period-drama voice."

What can be said more securely is:

> **the archaic/martial linguistic register survives across low-activation intimacy, high-activation command, leisure, embarrassment, and domestic contexts. Acoustic state changes modulate the delivery without requiring Takao to abandon the underlying Japanese register.**

This strongly supports the monograph's anti-parody rule:

> intimacy should not turn Takao into a different character voice.

A future direct auditory/perceptual review may refine how theatrical, naturalized, restrained, or stylized the archaic grammar sounds to the ear. That remains OPEN here.

---

# 18. Stable versus state-dependent variables

| Dimension | Stable tendency | State-dependent behavior | Confidence |
|---|---|---|---|
| Martial/formal JP register | persists across contexts | lexical/address realization changes with relationship state | C1/C2 |
| Pitch placement | corpus center around low-to-mid 200s | large excursions under command, acute surprise, competition, some presentation states | C1 |
| Pitch range | generally broad enough to reject "monotone" | expands in some acute contact/protective-surprise states | C1 |
| Temporal continuity | competent/task speech often organized | fragments under sustained vulnerability, defeat/strain, rhetorical timing, some self-presentation states | C1/C2 |
| Active level | ordinary variation by recording/context | matched post-oath pairs often lower than base | C1/C2 |
| Active speaking rate | broadly stable around ~6 JP chars/s | slows in several acute embarrassment/presentation reactions; can accelerate in urgent protection | C1/C2 |
| Combat realization | task-focused | ranges from ordinary battle assertion to extreme projected command | C2 |
| Intimacy realization | does not erase formal identity | secure states reduce relational mobilization | C2 |
| Embarrassment | domain-specific | multiple acoustic strategies; no single embarrassed register | C2 |

---

# 19. Performed-state transition model

The best current state machine is:

```text
CLEAR PROFESSIONAL DUTY
→ organized delivery
→ activation tracks urgency, not ambiguity

NOVEL BUT PROCEDURALIZABLE TASK
→ initial uncertainty
→ convert to training / technique
→ organization returns

COMPETITION
→ increased activation
→ coherent goal-directed delivery

SUDDEN PERSONAL SCRUTINY
→ activation rises
→ fluency may break depending on surprise and preparedness

SUSTAINED RELATIONAL SELF-EXPOSURE
→ pitch may remain ordinary
→ temporal fragmentation rises

OATH / COMMITMENT
→ fragmentation remains high
→ declarative energy rises

ESTABLISHED INTIMACY
→ relational activation baseline falls
→ closeness becomes easier to integrate into ordinary cadence

BOUNDARY VIOLATION INSIDE ESTABLISHED INTIMACY
→ embarrassment remains
→ excursion is more bounded

DANGER
→ protect first
→ verify safety
→ only then process intimate proximity

DEFEAT / STRAIN
→ lower placement + fragmentation can appear
→ text returns rapidly toward recovery orientation
```

---

# 20. Simulation-facing realization rules

These rules describe performed-state realization. They are not instructions to imitate a real voice actor's identity.

## V1 — Do not make baseline Takao flat

Professional Takao can use meaningful pitch movement.

"Disciplined" does not mean monotone.

## V2 — Separate activation from hesitation

High projection can be extremely fluent.

Heavy hesitation can occur at moderate pitch.

## V3 — Command should become compact before it becomes theatrical

Projected attack/command is characterized by decisiveness and concentration of energy.

Do not add romantic-style stammering to crisis command.

## V4 — Romantic vulnerability should often interrupt timing rather than destroy articulation

Feeling 4–5 remain articulate within active phrases.

Use phrase-level hesitation, not generalized incompetence.

## V5 — Oath is mobilized commitment

Do not render oath as the same settled mode used for mature domestic intimacy.

## V6 — Established intimacy lowers cost, not identity

Takao can remain formal, martial, modest, and direct while sounding less mobilized by closeness.

## V7 — Embarrassment requires trigger specificity

Strong triggers include:

- sudden intimate contact;
- unexpected scrutiny;
- being caught unprepared;
- provocative evaluation;
- sustained emotional self-exposure.

Ordinary peer interaction does not require the same performance.

## V8 — Protection overrides embarrassment in action order

If physical closeness is required to protect someone:

```text
act first
embarrassment later
```

## V9 — Leisure can be activated

Competition can produce serious projection even in trivial settings.

## V10 — Do not infer emotion from one acoustic variable

Especially avoid:

```text
high pitch = embarrassment
low pitch = intimacy
many pauses = vulnerability
quiet = affection
```

All require textual and situational context.

---

# 21. Negative constraints / anti-caricature

The complete performed corpus rejects the following simplified models.

### REJECT: "Takao has one stern voice"

Her corpus spans low settled intimacy, ordinary professional speech, high command projection, competitive activation, sustained vulnerability, acute embarrassment, physical strain, and playful/rhetorical timing.

### REJECT: "High pitch means she is flustered"

Some of the highest F0 values are attack/command calls.

### REJECT: "If she is in control, her voice must be low"

Task control and high activation coexist.

### REJECT: "If she pauses, she is romantically insecure"

Defeat, rhetoric, long explanation, and scene structure can also fragment timing.

### REJECT: "Romance turns her into a permanently soft/shy alternate personality"

Established-intimacy lines preserve Takao's martial language and operational competence.

### REJECT: "Leisure suppresses her intensity"

Competition can strongly activate her.

### REJECT: "Embarrassment disappears after oath"

It remains, but its amplitude and recovery regime change.

---

# 22. Adversarial findings and counterexamples

The exhaustive Pass 3 specifically sought evidence that could break the model.

## Counterexample A — high-F0 practical requests

Beach/calligraphy practical lines can be high in pitch without relational embarrassment.

**Disposition:** preserves the procedure rule but rejects "procedure = low pitch."

## Counterexample B — low-F0 fragmented defeat

Defeat shows that fragmentation is not unique to romantic vulnerability.

**Disposition:** revise the measurable second axis to temporal continuity/fragmentation.

## Counterexample C — ordinary-pitch presentation discomfort

Several modeling/self-presentation lines are not pitch-extreme.

**Disposition:** embarrassment can be temporally, not only pitch, marked.

## Counterexample D — low bridal baseline with preserved command

Established intimacy does not lower every type of utterance. Battle and mission competence remain available.

**Disposition:** relational baseline is lower; global personality activation is not.

## Counterexample E — beach as highest-median skin

Leisure can be highly activated.

**Disposition:** strongly preserves the monograph's competition rule and rejects subdued-off-duty caricature.

No counterexample found in the 114 mapped utterances requires rejection of Takao's central semantic character model.

---

# 23. Representative evidence matrix

| Function | Record | WAV | Median F0 | F0 span (st) | Pause ratio | Active level | Rate proxy |
|---|---|---|---:|---:|---:|---:|---:|
| Professional maxim | `303110:detail:0` | `TAKAO_303110_DETAIL_DETAIL_S001_9d90f840.wav` | 191.5 | 7.8 | 0.262 | -13.9 | 5.93 |
| Affinity vulnerability | `303110:feeling4:0` | `TAKAO_303110_FEELING4_FEELING4_S014_9d90f840.wav` | 216.6 | 9.6 | 0.366 | -15.8 | 6.49 |
| Affinity survival promise | `303110:feeling5:0` | `TAKAO_303110_FEELING5_FEELING5_S015_9d90f840.wav` | 207.4 | 8.4 | 0.384 | -14.9 | 6.67 |
| Oath | `303110:propose:0` | `TAKAO_303110_PROPOSE_PROPOSE_S076_9d90f840.wav` | 244.9 | 8.3 | 0.387 | -13.1 | 7.06 |
| Established love integration | `303110:feeling5:0#ex1100` | `TAKAO_303110_FEELING5_FEELING5_EX1100_S018_9d90f840.wav` | 196.5 | 8.1 | 0.361 | -18.1 | 6.29 |
| Established recognition/touch | `303110:touch:0#ex1100` | `TAKAO_303110_TOUCH_TOUCH_1_EX1100_S088_9d90f840.wav` | 177.7 | 10.2 | 0.356 | -19.2 | 6.37 |
| Base acute special-touch embarrassment | `303110:touch2:0` | `TAKAO_303110_TOUCH2_TOUCH_2_S089_9d90f840.wav` | 369.1 | 15.1 | 0.260 | -12.9 | 4.67 |
| Established-intimacy special touch | `303110:touch2:0#ex1100` | `TAKAO_303110_TOUCH2_TOUCH_2_EX1100_S096_9d90f840.wav` | 301.4 | 10.3 | 0.220 | -18.4 | 5.11 |
| Fourth Squadron command | `303110:couple_encourage:1` | `TAKAO_303110_COUPLE_ENCOURAGE_LINK2_S003_3cfa0544.wav` | 441.8 | 7.8 | 0.189 | -11.6 | 6.29 |
| Attack call | `303110:skill:0` | `TAKAO_303110_SKILL_SKILL_S010_3cfa0544.wav` | 490.4 | 8.3 | 0.389 | -10.8 | 5.49 |
| Base defeat/recovery | `303110:lose:0` | `TAKAO_303110_LOSE_LOSE_S004_3cfa0544.wav` | 205.3 | 10.0 | 0.412 | -13.2 | 6.92 |
| School caught unprepared | `303114:login:0` | `TAKAO_303114_LOGIN_LOGIN_S036_9d90f840.wav` | 387.0 | 9.7 | 0.318 | -15.2 | 4.56 |
| Calligraphy task disruption | `303113:touch2:0` | `TAKAO_303113_TOUCH2_TOUCH_2_S091_9d90f840.wav` | 414.5 | 14.0 | 0.249 | -15.7 | 4.92 |
| Modeling object-of-evaluation | `303115:detail:0` | `TAKAO_303115_DETAIL_DETAIL_S005_9d90f840.wav` | 227.5 | 11.6 | 0.344 | -18.6 | 5.62 |
| Protect first, notice contact later | `303116:touch:0` | `TAKAO_303116_TOUCH_TOUCH_1_S085_9d90f840.wav` | 278.6 | 16.8 | 0.401 | -18.4 | 4.95 |
| Sustained relational vulnerability | `303117:feeling5:0` | `TAKAO_303117_FEELING5_FEELING5_S016_9d90f840.wav` | 214.0 | 8.6 | 0.343 | -18.8 | 5.93 |
| Bridal ordinary peace | `303118:main:0` | `TAKAO_303118_MAIN_MAIN_1_S052_9d90f840.wav` | 201.8 | 9.9 | 0.236 | -20.6 | 6.25 |
| Bridal 'good wife' embarrassment | `303118:main:1` | `TAKAO_303118_MAIN_MAIN_2_S060_9d90f840.wav` | 234.1 | 10.3 | 0.418 | -19.9 | 5.14 |
| Bridal special-touch boundary | `303118:touch2:0` | `TAKAO_303118_TOUCH2_TOUCH_2_S095_9d90f840.wav` | 245.2 | 11.1 | 0.282 | -22.3 | 4.85 |

The complete 114-line acoustic matrix was generated from the mapped WAV corpus under the standardized Pass-3 procedure. The table above is deliberately representative rather than exhaustive; full reproducibility comes from the WAV manifest, source bundle provenance, and stated measurement procedure.

---

# 24. Confidence and authority

## C1 — direct acoustic observations

Examples:

- exact median F0;
- robust pitch span;
- pause/activity measurements;
- active level;
- rate proxy;
- matched base/post-oath acoustic differences.

## C2 — strong reconstruction

Examples:

- relationship security lowers relational mobilization;
- clear procedure preserves organization;
- sustained vulnerability often manifests in timing rather than high pitch;
- acute command and acute embarrassment occupy different performance regimes despite both allowing high F0;
- protection can precede delayed embarrassment;
- mature intimacy reduces embarrassment amplitude without removing modesty.

## C3 — constrained extrapolation

Novel-scene predictions that combine the above rules.

## OPEN

- exact perceived timbre;
- perceived warmth/brightness beyond measurable spectral proxies;
- breathiness as an ear-dependent quality;
- vocal fry;
- detailed actor-style aesthetics;
- claims requiring direct human auditory comparison rather than waveform-level evidence.

---

# 25. Relationship-state realization

The audio independently validates the monograph's C0/C1/C2 relationship-state separation.

## C0 — baseline / early affinity

- professional distance;
- organized functional delivery;
- little evidence of generalized shyness.

## C1 — growing affection

- vulnerability becomes temporally costly;
- Feeling 4–5 show increased phrase fragmentation;
- relational self-exposure is harder than professional difficulty.

## Oath — commitment transition

- high significance;
- strong declarative mobilization;
- hesitation remains present.

## C2 — established intimacy

- lower relational activation;
- less surprise cost;
- ordinary companionship and recognition are more normalized;
- embarrassment remains but is more bounded.

This is one of the clearest places where the performed layer adds information the text alone could only imply.

---

# 26. Implications for novel-context reconstruction

## Novel professional problem

Expected:

- organized speech;
- activation proportional to urgency;
- little romantic-style hesitation unless a relationship trigger intrudes.

## Novel hobby with a clear skill structure

Expected:

- rapid proceduralization;
- possibility of strong competitive activation;
- no need to become timid merely because the activity is unfamiliar.

## Novel public presentation

If Takao has rehearsed a procedure:

- organized but potentially elevated activation.

If she is unexpectedly evaluated before she is ready:

- stronger disruption;
- possible F0 excursion or temporal fragmentation.

## Novel romantic disclosure

Early/mid relationship:

- ordinary articulation within phrases;
- heavier inter-phrase hesitation.

Oath-like commitment:

- hesitation plus declarative force.

Established relationship:

- lower relational mobilization;
- directness becomes easier;
- modesty still constrains boundaries.

## Novel rescue involving physical closeness

Expected ordering:

```text
protect
→ stabilize
→ notice proximity
→ react
```

Do not make embarrassment block the rescue.

## Novel defeat

Possible acoustic realization:

- reduced pitch placement;
- temporal fragmentation;
- rapid semantic turn toward correction/recovery.

Do not interpret this as helplessness.

---

# 27. What this profile changes—and what it does not

It **does** close the old claim that no systematic Takao audio/performance audit exists.

It **does** provide stable quantitative performed-state rules.

It **does** sharpen the simulation model.

It **does not** alter:

- CN semantic authority;
- the core martial/duty/self-cultivation architecture;
- the JP textual register model;
- the established anti-caricature rules.

Most importantly:

> **the performed evidence strengthens the monograph's core claim that Takao's awkwardness is about specific forms of uncertainty and self-exposure, not generalized social incapacity.**

---

# 28. Residual open domain: direct perceptual timbre

The previous monograph's `PERFORMED_VOICE_MODEL: OPEN` was too broad after this work.

The correct post-analysis status is:

```text
PERFORMED_VOICE_MODEL:
ACOUSTIC / TIMING / STATE-TRANSITION LAYER — RESOLVED

DIRECT PERCEPTUAL TIMBRE LAYER — OPEN
```

The remaining OPEN layer should not block character simulation where the task is to predict:

- when she becomes more activated;
- when she pauses;
- when she projects;
- when she remains organized;
- how intimacy changes relational activation;
- how embarrassment differs from command.

It only blocks unsupported ear-dependent adjectives or actor-specific vocal aesthetics.

---

# 29. Canonical performed-voice principle

> **Takao does not possess a "stern voice" plus an "embarrassed voice." Her Japanese performance is a conditional system. Clear goals preserve organization; urgency and competition can raise projection without hesitation; sustained self-exposure can fragment timing without extreme pitch; acute scrutiny/contact can produce large activation excursions; oath combines hesitation with declarative force; and secure intimacy lowers the vocal cost of closeness without erasing discipline, modesty, or martial identity.**

For simulation:

> **Model the state transition before selecting the acoustic realization.**

