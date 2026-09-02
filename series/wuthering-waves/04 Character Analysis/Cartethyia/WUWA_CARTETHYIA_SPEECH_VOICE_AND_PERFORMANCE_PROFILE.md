---
series: WUWA
artifact_type: character_speech_performance_profile
scope: CARTETHYIA_SOURCE_3_6_0
generation: V0.2
status: active_provisional
release_state: mutable_active
source_boundary: "Pinned Wuthering Waves 3.6.0 / Arikatsu resource 3.6.6 four-language text at commit 353f2eaed119bc9f680eab92807d20ac75a79b40 and installed-client V0.5.1 performance media; human-listening conclusions are limited to explicitly reviewed cohorts"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Cartethyia — Speech and Performance Profile

Scope: literary speech analysis over the full four-language text surface, a bounded 12-FLAC archive feasibility pilot, and a 23-moment/92-FLAC matched story cohort. Chinese is the source-language textual authority; Japanese, Korean, and English are official localization/performance witnesses. The audio is playable and PCM-verified, but this pass did not perform a human listening review, so it does not invent emotion or acting-direction labels.

## Character-distinctive speech behavior

### Formal courtesy is a learned public instrument

In public or uncertain company, Cartethyia prefers complete questions, permission requests, honorific role names, and practical reassurance. She calls Rover “Laureate” early in Avinoleum, asks after physical safety, explains unfamiliar terrain, and apologizes for inconvenience. Fleurdelys intensifies this into a solemn, declarative register suitable to a sacred warrior.

This formality is not her unfiltered baseline. `FavorWord_140907_Content` says maintaining Fleurdelys' composed manners and tone is difficult. The archive and post-integration story repeatedly let the mask slip through small interjections, self-correction, embarrassment, and laughter.

### Her strongest rhetorical move is the ethical reversal

Cartethyia answers a role imposed on her by reversing its purpose:

- a creature made as a threat becomes the prison of its maker;
- “death” becomes the delivery mechanism for humanity into Leviathan;
- a sword is not passive obedience but a promise to defy and rescue its bearer;
- faith is not obedience but accumulated human deeds and a force that can demand liberation.

The sentences often take an antithetical form: not X, but Y; even if X, I choose Y. The four official texts align closely on the core truth-seeking line:

| Witness | `Main_Linaxita_2_4_1003_1` |
|---|---|
| Chinese | `我宁可最后成为清醒的恶人，也不要做什么都不知道的徘徊者。` — she prefers becoming a clear-eyed villain to wandering in ignorance |
| Japanese | Even if she were a villain, she wants to live understanding who she is rather than wander knowing nothing |
| Korean | Retains the “awake/clear-eyed villain” versus ignorant wanderer antithesis |
| English | “I'd rather know I'm a villain than remain a wanderer, lost in a world without understanding.” |

The agreement makes this a high-confidence characterization claim, not an English-only flourish. Source locator: `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/flowState/flowstate.json#/7280/Actions!/1/Params/TalkItems/0`.

### Hesitation marks exposure, not weak conviction

Ellipses and self-corrections cluster around identity, shame, grief, and direct bids for closeness: “I am afraid... but not of the answer,” “Fl… No, I'm Cartethyia,” and “Will you keep me company?” Once she decides on an action, syntax tightens into imperatives and short declarations: “No retreat,” “I am not useless,” “Fire me into Leviathan's heart.”

This distinction matters for simulation. Hesitation should occur at the threshold of disclosure; it should not make her indecisive after a moral decision has been made.

### Theatrical language is both inheritance and chosen play

The public turned Fleurdelys into an unfinished martyrdom drama, but Cartethyia also genuinely likes performance. She remembers Carnevale dancing, is embarrassed by a play about her life, and frames apparent death as a final stage light. The source line `我已走到结局，请点亮舞台最后的光，照亮我吧！` is stage-specific; Japanese and Korean preserve the spotlight/final-light image, while English adds “one last swan song, and then the lights go out.”

Theatricality therefore has two meanings: propaganda can overwrite her, but performance can also be reclaimed as humor, fellowship, and self-authored story. Her later joke that the staged death might become a Carnevale play is not tonal incoherence; it is appropriation of the script that once appropriated her.

### Private warmth appears through concrete invitations

Cartethyia rarely jumps straight to abstract affection. She offers hot bread, asks whether Rover wants to see her dance, proposes flying and looking over the city, sings a farewell song, and asks someone to remain beside her. The move from object/activity to emotional disclosure is characteristic: shared experience creates the safe frame in which she can be explicit.

### Trusted teasing is reciprocal and challenge-responsive

With trusted companions she can be impish, competitive, and mildly pouty. The line translated in English as “your provocations work far too well on me” varies productively:

- Chinese says goading works well on her.
- Japanese reframes it as fighting spirit rising most in hardship.
- Korean says provocation will make her stronger.
- English foregrounds playful warning.

All four support challenge-responsiveness; only English makes the flirtatious/playful surface maximally explicit. The safe characterization is “trusted provocation energizes her,” not “she always flirts when challenged.” Source: `…/flowstate.json#/7358/Actions!/5/Params/TalkItems/18`.

## Register by context

| Context | Likely register | Evidence-backed features |
|---|---|---|
| Stranger/dependent in danger | Courteous, practical, reassuring | Safety questions, explanations, offers of aid, minimal self-focus |
| Public/institutional | Formal and symbolic, but increasingly critical | Complete declarations, duty vocabulary, later separation of faith from obedience |
| Trusted peer | Softer, concrete, self-correcting | Ellipses, laughter, food/activity invitations, embarrassment, playful challenges |
| Fleurdelys battle/public persona | Solemn, elevated, terminal | Declaratives, sacred/mission language, theatrical finality |
| Moral decision under crisis | Compressed and imperative | Short clauses, vows, “no retreat,” willingness to act against another's request |
| Post-crisis repair | Reflective, self-deprecating, civic | Jokes about performance; admits unsuitability for office while accepting responsibility |

## Multilingual cautions

- English sometimes increases idiomatic drama (“swan song”) where Chinese uses a stage-light image. Preserve the shared theatrical function but do not back-project every English metaphor into Chinese authority.
- Japanese occasionally makes implicit motivation explicit, as in wanting to live after understanding who she is. Treat it as an official interpretive witness, not a replacement source.
- Korean frequently tracks the Chinese antithesis closely in the selected lines, but archive audio-text joins for early records were originally marked unavailable before Korean semantic ingestion. The current V0.3.0-ko text surface resolves the records; old manifest status remains historical.
- Name choice is consistent across witnesses: she selects Cartethyia because it is the name given at the first meeting, not because Fleurdelys' memories are erased.

## Performed-voice archive feasibility pilot

The pilot covers `FavorWord_140901_Content`–`140903_Content`: hot bread/home/dance, embarrassment at a dramatized life, and a promise to fight beside—and someday set right—the Rover. Event IDs are 883390758, 883390757, and 883390756. Each event resolves to one language-specific media object, verified WEM hash, decoded PCM identity, and FLAC SHA-256 in `VOICE/analysis_audio_samples_v0_1/analysis_audio_sample_manifest.json`.

Canonical physical home: `_voice_media/character/analysis_audio_samples_v0_1/samples/cartethyia/`.

### Timing and pause structure

Silence detection used FFmpeg at `-40 dB`, minimum 0.15 seconds. These are reproducible measurements, not emotion labels.

| Record | EN duration / silence | JA | KO | ZH |
|---|---:|---:|---:|---:|
| 140901 | 38.50 s / 33.0% | 46.02 s / 29.0% | 43.40 s / 24.7% | 40.38 s / 37.9% |
| 140902 | 36.58 s / 31.1% | 39.90 s / 24.3% | 34.32 s / 20.1% | 40.01 s / 34.5% |
| 140903 | 31.39 s / 36.3% | 39.97 s / 37.3% | 40.30 s / 33.2% | 38.23 s / 48.9% |

The measurements establish that the recordings are not simply time-scaled equivalents: localization/performance choices redistribute silence and total duration. The Chinese 140903 witness has the highest silence proportion in the cohort; Korean 140902 the lowest. Without listening and clause-aligned timing, it would be improper to call that “shy,” “confident,” or any other psychological state.

### Exact media witnesses

| Record | EN media | JA media | KO media | ZH media |
|---|---:|---:|---:|---:|
| 140901 | 136634715 | 303349445 | 907952735 | 414196496 |
| 140902 | 285977387 | 180716913 | 339567358 | 565409646 |
| 140903 | 770757753 | 545270490 | 586090821 | 454329066 |

Friendly filenames are never the identity. The event path, event ID, media ID, WEM SHA-256, canonical PCM SHA-256, FLAC SHA-256, language, favor record, text key, and source locator form the provenance chain.

## The Maiden and the Knight across four official performances

The required extension now exists at `_voice_media/character/performance_cohorts/Cartethyia/v0_2/`: 23 matched semantic moments crossing amnesiac uncertainty, early trust, fear, truth-seeking, private warmth, food and bodily loss, grief, ritual farewell, integration, self-sacrifice, Fleurdelys confrontation, chosen identity, reciprocal defiance, playful challenge, knight-errant futurity, civic faith, and rebuilding. The 92 FLAC files total 28,104,983 bytes. Every language witness round-trips to the canonical PCM identity recorded in the V0.5.1 production ledger.

This is a prepared human-listening cohort, not an acting result. The exact sample/provenance structure and review protocol are in `WUWA_CARTETHYIA_FOUR_DUB_LISTENING_LEDGER.md` and `COHORT_MANIFEST.json`.

| Language | Hypothesis to test | Required counterexample search | Current result |
|---|---|---|---|
| Chinese | More context-adaptive movement between ordinary, ceremonial, and crisis registers | Scenes that remain consistently maiden- or knight-centered across context changes | **OPEN_requires_human_listening** |
| Japanese | More maiden-weighted solemnity/formality | Playful/private and post-crisis lines that clearly break the proposed center | **OPEN_requires_human_listening** |
| Korean | May occupy a midpoint, or may not form a stable single center | Any coherent independent center; failure of the midpoint hypothesis is allowed | **OPEN_requires_human_listening** |
| English | More knight-weighted directness/playfulness | Ceremonial, grief, and self-erasure lines that resist that center | **OPEN_requires_human_listening** |

Localization wording and acting delivery are separate evidence dimensions. A textual metaphor, punctuation mark, or longer waveform cannot by itself prove vocal affect. Any accepted tendency must recur across at least three distinct contexts, retain its counterexamples, and remain language-scoped. No current performance finding may be transferred into universal personality.

The archive pilot and story cohort together prove performed-voice analysis is technically feasible. They do not yet prove which official performance is most maiden-centered, knight-centered, flexible, or internally divided.
