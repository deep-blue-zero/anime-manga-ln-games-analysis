---
series: AZUR_LANE
artifact_type: specialist_synthesis
scope: ST_LOUIS_10213_JP_VOICE_PERFORMANCE
generation: V1
status: canonical
source_boundary: 71/71 mapped spoken JP utterances after St. Louis audio reconciliation; JP client AZL 9.3.386 / CV 1243
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
semantic_authority: CN
performed_locale: JP
direct_perceptual_listening_status: not directly auditioned in this analysis environment
ear_dependent_timbre_status: open
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — St. Louis JP Voice Performance Profile

## Acoustic Performance, Social Register, Relationship State, and Simulation Constraints

# 0. Authority and boundary

This is the canonical V1 specialist authority for the **quantitative/acoustic Japanese performed layer** of St. Louis / group 10213.

It supplements the CN-semantic character monograph and the multilingual speech profile. It does not move semantic authority away from CN.

The environment used here can inspect and measure decoded WAV waveforms directly but does not provide a human-equivalent auditory playback channel. Therefore the profile makes strong claims about pitch placement/range, timing, continuity, active level, rate proxy, and context-conditioned acoustic state transitions, while leaving exact ear-dependent adjectives such as breathy, smoky, husky, airy, smiling, or vocal-fry-heavy OPEN.

# 1. Corpus and method

The final spoken corpus contains **71 mapped JP utterances** with zero unresolved spoken text records after `link1/link2` reconciliation. Five `drop_descrip` fields are known unvoiced, and the remaining vote record is a non-dialogue campaign placeholder.

All 71 WAVs were measured once under a fixed corpus-wide procedure and then interpreted in three sequential passes:

1. **Pass 1 — anchor contrasts:** routine baseline, peer care, affinity, oath, touch, combat;
2. **Pass 2 — breadth challenge:** all four non-base skin contexts, leisure, presentation, driving, drinking, and cruise intimacy;
3. **Pass 3 — exhaustive adversarial audit:** every remaining line, outliers, mundane controls, and alternate causes of pause fragmentation.

Measurement configuration:

- Praat autocorrelation F0;
- 10 ms pitch step;
- 75–700 Hz bounds;
- median F0 as pitch-placement statistic;
- p10–p90 robust pitch span in semitones;
- 25 ms energy windows / 10 ms hop for activity;
- adaptive within-clip threshold;
- internal-pause ratio after short-gap bridging;
- substantial pauses ≥250 ms;
- active RMS in dBFS;
- Japanese content characters per active second as a rate proxy, not morae/sec.

Corpus center:

- median F0: **308.6 Hz**;
- median p10–p90 pitch span: **11.0 st**;
- median internal-pause ratio: **0.278**;
- median active level: **-17.2 dBFS**;
- median rate proxy: **4.96 chars/active-s**;
- analyzed duration: **13.07 min**.

# 2. Executive performed-state model

The most defensible measurable model is again two-dimensional:

```text
activation / projection
        ×
temporal continuity / fragmentation
        +
text + scene + relationship context
        ↓
performed state
```

For St. Louis, however, this state space is populated very differently from Takao's.

> **St. Louis's intimacy and flirtation are usually not realized as acute vocal destabilization. Her strongest systematic pitch elevation belongs to projection, combat, excitement, or isolated presentation uncertainty; sustained intimacy often moves toward lower or ordinary pitch placement while retaining deliberate temporal shaping.**

This is a major anti-caricature constraint. The performed corpus does not support "flirty character = constantly breathless/high-pitched" or "sexual contact = embarrassed spike."

# 3. Diagnostic state contrasts

| Analytical state | N | Median F0 | F0 span (st) | Pause ratio | Active level dBFS | Rate proxy |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary duty / routine | 5 | 314.1 | 10.9 | 0.222 | -16.2 | 5.36 |
| Peer care / restraint | 3 | 291.5 | 10.8 | 0.179 | -16.7 | 5.42 |
| Base playful/flirt | 4 | 308.6 | 12.4 | 0.231 | -17.4 | 4.64 |
| Late base affinity | 2 | 307.2 | 11.5 | 0.337 | -17.6 | 4.21 |
| Oath | 1 | 291.5 | 10.6 | 0.461 | -17.8 | 4.99 |
| Base combat | 5 | 351.6 | 10.5 | 0.088 | -16.6 | 4.72 |
| Cruise intimacy | 7 | 289.5 | 13.3 | 0.307 | -18.4 | 4.57 |

The key contrasts are robust enough to guide simulation.

## 3.1 Combat/projection

The base combat subset centers around **351.6 Hz**, substantially above routine duty, with a median pause ratio of only **0.088**. `Lucky Lou!` is the corpus maximum at about **437.6 Hz** and is also the loudest sampled utterance.

Thus high pitch in St. Louis is not an embarrassment marker. It frequently marks **projection, animation, and concise performance energy**.

## 3.2 Sober peer care

The peer-care control sits lower, around **291.5 Hz**, with relatively continuous timing. Two of the lowest-F0 lines in the entire corpus are:

- `102130:feeling2:0` — counterfactual grief/concern about Helena and Kolombangara: ~267.7 Hz;
- `102130:main:2` — advice to Arizona not to remain trapped in past sorrow: ~274.6 Hz.

This provides a useful performed boundary:

> **When St. Louis stops managing atmosphere playfully and addresses grief, vulnerability, or another person's welfare directly, pitch placement can settle markedly downward without loss of fluency.**

## 3.3 Intimacy is usually controlled, not destabilized

Base special touch is about **299.7 Hz**, actually below the base-skin median. The cruise special-touch line is about **296.0 Hz**, essentially at the cruise skin center.

The cruise-intimacy analytic subset centers at roughly **289.5 Hz**, below ordinary routine duty, despite being the most explicitly physical/romantic group in the corpus.

This strongly rejects a Takao-like transfer rule. For St. Louis:

```text
sexual / romantic closeness
≠ automatic high-pitch embarrassment
```

Instead, closeness is frequently something she **initiates, frames, and controls through implication**.

# 4. Affinity and oath

| Record | Median F0 | Span | Pause ratio | Pauses ≥250ms | Level | Rate |
|---|---:|---:|---:|---:|---:|---:|
| `102130:feeling1:0` | 290.2 | 9.5 | 0.148 | 1 | -18.0 | 4.63 |
| `102130:feeling2:0` | 267.7 | 9.6 | 0.147 | 2 | -17.1 | 6.09 |
| `102130:feeling3:0` | 341.6 | 8.6 | 0.304 | 2 | -17.0 | 5.25 |
| `102130:feeling4:0` | 295.9 | 12.2 | 0.398 | 6 | -18.1 | 4.44 |
| `102130:feeling5:0` | 318.6 | 10.8 | 0.277 | 4 | -17.2 | 3.98 |
| `102132:feeling5:0` | 314.6 | 9.6 | 0.473 | 10 | -18.7 | 4.99 |
| `102133:feeling5:0` | 288.1 | 9.5 | 0.387 | 9 | -17.9 | 6.16 |
| `102134:feeling5:0` | 280.7 | 10.9 | 0.307 | 9 | -18.7 | 4.57 |

The affinity labels themselves are not a simple romantic ladder because early stages contain Helena/history material. That is analytically important.

- Feeling 1–2 are low-pitch and concern Helena/history rather than simple attraction.
- Feeling 3 jumps upward because its line ends in a surprised `ダメ！？` after offering bedroom cleaning.
- Feeling 4 is heavily segmented, but the text is deliberate teasing about the Commander's hidden secrets; fragmentation here cannot safely be called insecurity.
- Feeling 5 is a direct date invitation and remains around ordinary pitch.

The oath sits at about **291.5 Hz** with the highest pause ratio of the base character material, **0.461**. The combination is not a high-pitch confession. It is better described acoustically as **lower/mid placement plus expanded, segmented ritual timing**.

Thus:

> **Relationship significance changes St. Louis's pacing more reliably than it raises her pitch.**

But even that statement requires context: pause count is highly correlated with utterance length, and St. Louis uses pauses for deliberate teasing/rhetorical control as well as significance.

# 5. Teasing as temporal control

St. Louis's JP text repeatedly uses implication → reaction space → playful qualification or retraction:

- `別のことでも考えちゃった？うふふ♡`
- `なんてね。ふふふ`
- `本当に…？`
- `…指揮官くん♡`

The acoustic corpus is consistent with this: intimate and teasing lines often carry **moderate-to-high temporal fragmentation without corresponding high F0**.

This does not prove a specific perceptual "teasing tone" by ear. It does support a simulation rule:

> **Do not render St. Louis's teasing as a fast uninterrupted stream. She often creates temporal room for implication and the other person's reaction, then completes the social move.**

# 6. Presentation uncertainty is a genuine exception

The Spring/Chinese-dress special-touch record `102131:touch2:0` is about **360.9 Hz**, well above that skin's median, with slow active articulation and substantial fragmentation.

Textually, however, the issue is not moral outrage at touch. She asks whether the unfamiliar clothing has been worn incorrectly: `あら、ここの着かた間違ってる？本当に…？`

This suggests a useful boundary:

> **St. Louis can become acoustically more disrupted when her normally confident self-presentation is made uncertain.**

The cruise material provides the counterexample: when she controls the intimate frame, even explicit physical contact remains near or below baseline.

This is C2 rather than C1 because the presentation-uncertainty evidence is narrow.

# 7. Luck, failure, and stress in performance

The performed corpus independently sharpens the textual luck model.

`102130:lose:0` — `今日は戦闘に適さないようね……` — sits around **340.0 Hz** and has effectively no internal pause under the fixed detector. This is not an acoustic collapse.

Likewise the HP-warning line is elevated and compact, and the MVP line is strongly projected while explicitly denying that victory is luck alone.

Contrast this with Takao's lower, fragmented defeat realization. For St. Louis the current evidence supports:

> **A routine bad outcome is more likely to be localized and kept moving than acoustically treated as identity failure.**

R5 still supplies an important exception: under serious alternate-source burden she apologizes for dragging others down. Therefore this is a normal-failure rule, not proof of invulnerability to guilt.

# 8. Relationship-specific projection

The repaired Helena `link1` warning sits at ~336.5 Hz: serious, projected, but not extreme.

The `Lucky unit` `link2` line reaches ~392.6 Hz and is the fastest line in the corpus by the current character-rate proxy.

Together they demonstrate that peer relationship content itself spans protective seriousness and buoyant group animation. A simulator should not give St. Louis one generic "older-sister" delivery around Helena.

# 9. Skin-level breadth challenge

| Skin | Analytical context | N | Median F0 | F0 span (st) | Pause ratio | Active level | Rate proxy |
|---|---|---:|---:|---:|---:|---:|---:|
| `102130` | Base / standard | 28 | 315.8 | 10.7 | 0.223 | -16.7 | 4.90 |
| `102131` | Spring / Chinese-dress presentation | 5 | 330.5 | 10.0 | 0.318 | -18.2 | 4.70 |
| `102132` | Snow / drinking leisure | 8 | 314.7 | 9.2 | 0.332 | -17.6 | 5.04 |
| `102133` | Luxury driving / party | 12 | 293.2 | 12.1 | 0.330 | -17.0 | 5.24 |
| `102134` | Cruise / interactive intimacy | 18 | 293.4 | 11.7 | 0.276 | -17.5 | 4.69 |

These skin medians are not personality states by themselves; each skin selects different scenarios and may come from different recording sessions. They are therefore secondary evidence.

Even with that caution, two patterns survive within-context controls:

1. the most explicitly intimate cruise skin (`102134`) centers low relative to base;
2. its special-touch line is only about **+0.15 semitones** above its own skin median, while the Spring clothing-uncertainty line is about **+1.5 semitones** above its skin median.

The difference is small enough that exact numeric effect size should not be fetishized, but directionally it reinforces the text-based distinction between **controlled intimacy** and **uncertain presentation**.

# 10. Exhaustive Pass-3 counterexamples

The exhaustive sweep produced several constraints.

## Counterexample A — high F0 is often non-romantic

The highest lines are attack/skill, Lucky-unit projection, combat/cruise battle, and presentation uncertainty.

**Result:** REJECT `high pitch = flirtation/embarrassment`.

## Counterexample B — low F0 is often non-intimate

Helena counterfactual grief and Arizona care are the corpus lows.

**Result:** REJECT `low pitch = intimacy`.

## Counterexample C — fragmentation is not vulnerability

Substantial-pause count correlates about **0.95** with duration and **0.84** with text length. St. Louis also uses rhetorical segmentation during jokes and implication.

**Result:** REJECT `many pauses = insecurity`.

## Counterexample D — F0 and fragmentation are substantially independent

The correlation between median F0 and pause ratio is only about **-0.14**.

**Result:** preserve the two-axis state model.

## Counterexample E — sexual boundary lines need not signal discomfort

Base and cruise `touch2` remain near ordinary pitch and are linguistically teasing/controlled rather than panicked.

**Result:** distinguish local norm-setting and consensual flirt framing from embarrassment.

# 11. Final performed-state matrix

| State | Activation / projection | Temporal continuity | Contextual interpretation |
|---|---|---|---|
| routine duty | moderate | moderate-high | socially composed baseline |
| sober peer care | low-moderate | high | seriousness / welfare focus |
| buoyant group animation | high | high | social energy, not insecurity |
| combat/skill projection | high-very high | high | concise outward projection |
| routine defeat | high-moderate | high | localized setback, no collapse |
| deliberate teasing | moderate | moderate/fragmented | implication/reaction management |
| sustained intimacy | low-moderate | moderate | controlled closeness |
| oath/significant commitment | low-moderate | low | expanded ceremonial/relational timing |
| presentation uncertainty | potentially high | low-moderate | narrow observed destabilizer |

# 12. Simulation-facing rules

## P1 — Do not acoustic-caricature flirtation

Intimate St. Louis is often **less**, not more, pitch-elevated than combat or animated social performance.

## P2 — Use pauses as social architecture, not automatic shyness

A pause may create implication, invite reaction, mark ritual significance, or segment long text.

## P3 — Serious care should reduce ornamental play

When another person's welfare becomes the real topic, performance can settle downward and become more continuous.

## P4 — Combat should project without importing social hesitation

High activation and compact timing are compatible.

## P5 — Ordinary defeat should not become melodramatic collapse

Her normal loss line remains compact and externalizes the local condition.

## P6 — Physical intimacy does not automatically fluster her

If St. Louis controls the frame, she can remain acoustically composed even during explicit contact.

## P7 — Uncertain self-presentation is a stronger candidate destabilizer

When she is unsure whether she herself has presented something incorrectly, greater disruption is plausible.

## P8 — Preserve seriousness switching

The R5 narrative evidence shows that grave risk suppresses playful social ornamentation. The acoustic peer-care controls point in the same direction.

# 13. Representative evidence matrix

| Record | JP text | Median F0 | Span | Pause ratio | Level | Rate |
|---|---|---:|---:|---:|---:|---:|
| `102130:main:2` | アリゾナ、あの時のことを忘れられなくても、あまり引きずらないほうがいいわ | 274.6 | 8.3 | 0.223 | -16.5 | 6.40 |
| `102130:login:0` | 指揮官くん、運ってのは流れるものなのよ？流れが来ているうち、思いっきりやっちゃって | 311.0 | 13.5 | 0.347 | -16.2 | 6.02 |
| `102130:couple_encourage:0` | ヘレナ、今度は勝敗ばかり見ちゃダメよ | 336.5 | 12.9 | 0.119 | -16.7 | 4.76 |
| `102130:couple_encourage:1` | ラッキーユニットってことかしら♪ | 392.6 | 8.3 | 0.283 | -15.7 | 7.85 |
| `102130:feeling2:0` | ヘレナがいたら、コロンバンガラでの戦いは違う結末になったかもしれないわね…… | 267.7 | 9.6 | 0.147 | -17.1 | 6.09 |
| `102130:feeling4:0` | うふふ、指揮官くんが部屋に隠しているヒミツ、ぜーんぶわ・か・る・わ～ | 295.9 | 12.2 | 0.398 | -18.1 | 4.44 |
| `102130:feeling5:0` | ふぅ……後片付けはいっつも面倒ね…指揮官くん、どこかでデートしない？ | 318.6 | 10.8 | 0.277 | -17.2 | 3.98 |
| `102130:propose:0` | あら、どうしたの？急にプレゼントなんて…うふふ、なるほど、これね……じゃあ、指揮官くん、これ、つけてくれるかしら？ | 291.5 | 10.6 | 0.461 | -17.8 | 4.99 |
| `102130:touch2:0` | こういうの、外でするものじゃないわよ。指揮官くん♡ | 299.7 | 8.1 | 0.293 | -16.6 | 5.68 |
| `102131:touch2:0` | あら、ここの着かた間違ってる？本当に…？ | 360.9 | 7.9 | 0.368 | -18.2 | 3.71 |
| `102133:feeling5:0` | パーティーもいいけど、指揮官くんと二人っきりでいるのはもっといいわね…もういっそ二人でパーティーをこっそり抜けて、ドライブでも楽しまない？なんてね。ふふふ | 288.1 | 9.5 | 0.387 | -17.9 | 6.16 |
| `102134:feeling5:0` | 肌をなぞる指揮官くんの指、熱い太陽よりも火照らせそう。……こうしてべったりくっついて一緒に波音に耳を傾ける時間がずっとずっと続いてほしいわ。ふふふ | 280.7 | 10.9 | 0.307 | -18.7 | 4.57 |
| `102134:touch2:0` | もう、指揮官くんったらせっかちね……こっちも我慢しなくていいってことかしら♥ | 296.0 | 12.1 | 0.203 | -18.5 | 4.71 |
| `102130:lose:0` | 今日は戦闘に適さないようね…… | 340.0 | 8.9 | 0.000 | -16.6 | 4.86 |
| `102130:skill:0` | ラッキールー♪ | 437.6 | 12.6 | 0.184 | -14.6 | 4.72 |

# 14. Confidence

**C1 direct acoustic:** all measurements and exact record-level differences.

**C2 strong reconstruction:** combat projection vs intimacy, sober-care lowering, controlled physical intimacy, teasing as context-dependent temporal shaping, normal defeat without collapse.

**C3 constrained extrapolation:** how an unseen social embarrassment or serious interpersonal confrontation would alter the acoustic state.

**OPEN:** direct perceptual timbre, exact breathiness, fry, smile quality, and actor-aesthetic descriptors.

# 15. Canonical performed-voice principle

> **St. Louis's Japanese performance is socially controlled rather than uniformly seductive or coy. Projection and excitement can raise her pitch sharply; serious care can lower and simplify it; teasing often works through deliberate temporal space; intimate contact is frequently handled without acoustic destabilization; and the clearest non-combat disruption appears when her normally assured self-presentation itself becomes uncertain. Model who controls the social frame before choosing the performed state.**
