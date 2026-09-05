---
series: WUWA
character: Lynae
artifact_type: analysis_packet_entrypoint
scope: LYNAE_SOURCE_3_6_0_PRE_AV
generation: V0.1-pre-av
status: active_provisional
authority_state: local_working_draft_not_promoted
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
drive_character_bridge: 1OCxQve4YIlSCQhhq7shQjgdqeF0DreIt
drive_voice_view: 1GWCEfknQjwNwhcHP9GaRg3mXQgnuggFh
intended_canonical_home: series/wuthering-waves/04 Character Analysis/Lynae/
governing_protocol: WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md V0.2
created: 2026-09-02
do_not_use_as_current_git_authority: true
---

# Lynae reconstruction packet — pre-audiovisual V0.1

## Purpose

This packet is the first source-grounded reconstruction of playable **Lynae / 琳奈 / リンネー / 린네** against the frozen *Wuthering Waves* 3.6.0 evidence generation.

It is deliberately **pre-audiovisual**. The current WUWA reconstruction protocol requires materially available audiovisual evidence to receive an evidence-hierarchy pass, targeted acquisition, and direct review before the final integrated character monograph is hardened. No such Lynae video/image tranche has yet been materialized in the evidence package. This packet therefore establishes the textual, contextual, longitudinal, relationship, ordinary-life, speech, and currently reproducible acoustic baseline that the later AV pass should test.

It is also **not a human voice-performance reading**. The Drive voice package contains nearly complete four-language official audio, but the current evidence has zero structured human-performance annotations. Human listening is an optional terminal addendum under the V0.2 reconstruction protocol.

Nothing in this directory has been committed, pushed, merged, or promoted to repository authority.

## Governing method

The packet follows the current WUWA method stack:

- `00 Frameworks and Methods/WUWA_ANALYTICAL_METHOD.md`
- `00 Frameworks and Methods/WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md` V0.2
- `00 Frameworks and Methods/WUWA_CHARACTER_FOLDER_CONTRACT.md`
- `00 Frameworks and Methods/WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md`
- `00 Frameworks and Methods/WUWA_LONGITUDINAL_STORY_ANALYSIS_ARCHITECTURE.md`
- `00 Frameworks and Methods/WUWA_NARRATIVE_DEEP_READING_PROTOCOL.md`

Its source-facing organization also borrows two useful features from the Gakuen Idolmaster Hanami Saki core reading:

1. a large interpretive reading that keeps source families, chronology, and rival explanations visible;
2. a separate evidence/falsification matrix that makes later AV or source updates test claims rather than merely accumulate confirming examples.

The WUWA character-folder contract remains controlling: specialist artifacts are split only where Lynae's evidence density makes repeated independent retrieval useful.

## Source boundary

Pinned semantic authority:

- Arikatsu source commit: `353f2eaed119bc9f680eab92807d20ac75a79b40`
- normalized generation: `arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko`
- primary textual witness: `zh-Hans`
- official localization witnesses: `ja`, `ko`, `en`
- installed-client audio: official raw media evidence routed through canonical semantic occurrences

Lynae Drive evidence reports:

| surface | bounded count / state |
|---|---:|
| playable role | `1509` |
| candidate source occurrences | 1,136 |
| accepted playable-Lynae solo occurrences | 1,128 |
| rejected candidates | 6 |
| unresolved identity candidates | 2 |
| accepted voiced story/message occurrences | 824 |
| accepted explicitly unvoiced occurrences | 304 |
| favor stories | 5 |
| favor/archive words | 64 |
| contextual scenes / selected raw flow rows | 251 |
| contextual text keys | 3,886 |
| WavesLine records | 21 |
| quest-reference wrappers | 162 across 32 quest IDs |
| semantic voice lines | 888 |
| semantic voice lines with complete four-language media | 885 |
| render associations | 3,616 |
| unique PCM/FLAC objects | 3,490 |
| structured human-performance annotations | 0 |
| materialized Lynae AV tranche | none |

The 32 quest IDs are **reference coverage**, not a claim that all 32 complete quest graphs or the whole game graph have been extracted.

## Identity boundary

The analysis concerns **playable Lynae**.

Technical story speaker `100085` and message speaker `300087` are accepted. Generic speaker `178` is not globally mapped to Lynae; five exact hidden-speaker occurrences in flow row `10107` are contextually accepted.

Six candidate occurrences are rejected, including four recorded-mission lines belonging to the **original identity-holder named Lynae** and two clinical-introduction lines attributed to Luuk Herssen. Two generic candidates remain unresolved and excluded:

- `flowstate.json#/10832/Actions!/5/Params/TalkItems/28`
- `flowstate.json#/12103/Actions!/3/Params/TalkItems/0`

The original identity-holder must not be collapsed into playable Lynae.

## Audio boundary

The voice package contains 888 semantic lines. Three PhoneMessage semantic lines at flow row `16402` have localized text but unresolved runtime dispatch:

- `Zuoyequnxing_88_1`
- `Zuoyequnxing_88_3`
- `Zuoyequnxing_88_4`

Their installed variants exist; absence of extracted playback is **not** evidence that the audio pack is missing or that the lines are silent.

The currently materialized machine features cover duration, signal level, peak level, sample rate, and a simple silence fraction. They do not satisfy every baseline required by `WUWA_MACHINE_VOICE_ANALYSIS_PROTOCOL.md`—notably robust F0, speaking-rate, pause-density, spectral/breathiness proxies, and protocol-level clustering/normalization are not present here. Accordingly this packet records a **partial machine acoustic baseline**, not the completion state `machine_voice_profiled`.

## Audiovisual boundary

`ASSET_REFERENCE_INDEX.json` is a locator/reference index only. It is not direct visual evidence.

No claim in this packet about:

- facial expression;
- gaze;
- gesture;
- posture;
- blocking;
- camera placement;
- shot composition;
- lighting;
- animation performance;
- costume symbolism;
- performed body language

is treated as established unless it follows from text rather than visual observation. The AV nomination artifact identifies the scenes and official media types that should be collected later.

## Packet contents and analytical responsibility

### 1. `WUWA_LYNAE_CHARACTER_DEEP_DIVE_PRE_AV.md`

The principal source-facing literary/character reading. It establishes the current thesis, developmental architecture, source-family reading, ethical tensions, longitudinal changes, narrative motifs, rival interpretations, and explicit limits.

### 2. `WUWA_LYNAE_EVIDENCE_AND_FALSIFICATION_MATRIX.md`

A claim-level apparatus. Each claim is typed as source fact, stable observation, strong inference, or candidate thesis; it records strongest evidence, counterevidence, extrapolation limits, and what later audiovisual or source material could falsify or revise it.

### 3. `WUWA_LYNAE_RELATIONSHIP_AND_STATE_PROFILE.md`

The canonical candidate home for developmental states, relationship states, recipient-specific behavior, and transition evidence. It prevents the reconstruction from treating “Lynae” as one timeless social register.

### 4. `WUWA_LYNAE_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`

Mundane evidence: food, mobility, hobbies, study, rest, silence, shopping, color/aesthetic taste, play, practical competence, boredom, volunteering, and low-stakes social initiative. Entries distinguish source fact, analytical implication, and extrapolation limit.

### 5. `WUWA_LYNAE_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`

Textual speech/register analysis plus the reproducible acoustic accounting currently supportable from Drive. It contains no human acting labels and does not claim protocol-complete machine voice profiling.

### 6. `WUWA_LYNAE_RECONSTRUCTIVE_PROFILE_PRE_AV.md`

A compact operational model for bounded unfamiliar-situation prediction. It includes state selection, core drives, behavior rules, exceptions, recipient modifiers, confidence, and mandatory abstentions.

### 7. `WUWA_LYNAE_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`

Adversarial tests of the reconstructive profile against ordinary time, praise, failure, boredom, rules, friends, crisis, ambiguous intimacy, identity threats, and localization traps.

### 8. `WUWA_LYNAE_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md`

Phase-8 AV hierarchy/nomination work: what cutscenes, in-engine sequences, trailers/showcases, and official images should be collected, what each can actually prove, and which textual claims they should test.

## Current completion assessment

| reconstruction dimension | state |
|---|---|
| identity adjudication | substantially complete within frozen package; 2 explicit unresolved candidates preserved |
| textual/contextual reconstruction | **complete enough for `textually_reconstructed` within the declared 3.6.0 Lynae package** |
| ordinary-life extraction | complete enough for standalone profile |
| relationship/state reconstruction | complete enough for standalone profile |
| textual speech analysis | complete enough for provisional profile |
| machine acoustic processing | extensive but **not protocol-complete** |
| `machine_voice_profiled` | **not claimed** |
| AV hierarchy/nomination | **completed as a plan**, pending actual media collection |
| direct AV analysis | not performed |
| `audiovisually_hardened` | **not claimed** |
| integrated reconstruction completion | **not claimed** |
| human performance review | not performed; optional |
| compiled predictive reconstruction | provisional pre-AV profile produced |
| fidelity testing | pre-AV adversarial test produced |

“Textually reconstructed” here means source-bounded reconstruction from the accepted character evidence package, not proof that candidate discovery found every completely unmarked hidden utterance in the full client.

## Recommended reading order

1. `WUWA_LYNAE_CHARACTER_DEEP_DIVE_PRE_AV.md`
2. `WUWA_LYNAE_EVIDENCE_AND_FALSIFICATION_MATRIX.md`
3. `WUWA_LYNAE_RELATIONSHIP_AND_STATE_PROFILE.md`
4. `WUWA_LYNAE_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`
5. `WUWA_LYNAE_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md`
6. `WUWA_LYNAE_RECONSTRUCTIVE_PROFILE_PRE_AV.md`
7. `WUWA_LYNAE_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md`
8. `WUWA_LYNAE_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md`

## Promotion boundary

If these artifacts are later promoted into Git, they should **not** be committed in isolation.

The WUWA governance documents currently require the same analytical transaction to update, as applicable:

- `WUWA_LYNAE_CURRENT_STATE.md`;
- `07 Evidence and Indexes/WUWA_CHARACTER_INDEX.md`;
- `WUWA_CLAIM_EVIDENCE_INDEX.md`;
- relevant longitudinal state/relationship/open-question ledgers;
- `CURRENT_STATE_AND_CORPUS_MAP.md`;
- revision controls;
- corpus manifest/audit.

This packet therefore remains local working material until the owner authorizes a coordinated repository transaction.

## One-sentence working thesis

**Lynae is best reconstructed as a person learning to turn survival without roots into a life capable of accumulating “dead weight”: possessions, trust, obligations, friends, and futures that matter precisely because she can no longer treat departure as the default answer.**

That thesis is strong but still pre-AV. The later audiovisual pass should be designed to attack it, not decorate it.
