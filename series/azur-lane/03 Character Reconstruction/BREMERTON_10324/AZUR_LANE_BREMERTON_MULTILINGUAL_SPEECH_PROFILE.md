---
series: AZUR_LANE
scope_character: BREMERTON_10324
generation: V1
semantic_authority: CN
azurlane_data_commit: 4cca5c2437007b62d30a6235fcfc0c0203231378
story_lua_witness_commit: d93f83db24195981c5f5ca90ac5e29ce0580b12c
source_package_generated_at: '2026-08-23T18:55:47.426186Z'
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
artifact_type: specialist_synthesis
scope: BREMERTON_10324_R7_MULTILINGUAL_SPEECH_REGISTER
status: canonical
source_boundary: Five-locale aligned character package; direct re-audit of 108 JP character-dialogue records; CN semantic authority from pinned originating scripts; EN/TW/KR treated as regional witnesses with unresolved phrase-level candidates retained
---

# Azur Lane — Bremerton R7 Multilingual Speech and Register Profile

## 0. Authority split

This profile does **not** collapse five branches into one “true script.”

```text
CN → originating semantic authority
JP → Japanese linguistic realization
EN / TW / KR → independent regional witnesses
```

Package-level alignment is strong: 1,675 regional candidates, 1,579 complete, 96 structural gaps, and 15 semantic-review candidates. Narrative alignment is 1,366 / 1,368.

The generated phrase-level crosswalk was not separately published in the current Drive package, so this pass does not manufacture EN/TW/KR wording for the 15 review candidates. Those remain branch-specific `OPEN` items. The stable semantic model and the directly re-audited JP register are nevertheless well constrained.

## 1. Cross-branch stable semantic speech behavior

Across the source architecture Bremerton repeatedly speaks to **move interaction forward**. Stable content functions include:

- direct question;
- low-friction invitation;
- specific offer;
- practical suggestion;
- check-in;
- referral or request for someone else's expertise;
- reassurance without excessive solemnity;
- operational warning when stakes rise;
- playful acknowledgment of her own uncertainty or weakness.

This functional layer is more stable than any one regional slang choice.

## 2. JP corpus statistics

Direct audit of the 108 Japanese character-dialogue records:

| Feature | Count |
|---|---:|
| `アタシ` | 31 |
| `指揮官` | 60 |
| `ってカンジ` | 6 |
| `かな` | 19 |
| `艦船通信` | 14 |
| `相談` | 14 |
| `DM` | 2 |
| question marks | 72 |
| exclamation marks | 77 |
| `～` | 23 |
| explicit `デート` | 3 |

Counts are descriptive, not a requirement to insert a marker into every generated line.

## 3. JP baseline register

### First person

`アタシ` is the characteristic casual first-person form. It should be preferred when the sentence naturally requires a pronoun, but Japanese pro-drop means most generated lines should **not** force it unnecessarily.

### Address

`指揮官` is frequent and direct. Bremerton often uses address to pull the other person into the action/question rather than as honorific distance.

### Formality

Baseline JP is low-formality, contemporary, conversational speech:

- contractions/casual copular forms;
- direct interrogatives;
- sentence-final softeners;
- stretched vowels/wave-dash playfulness;
- frequent exclamation/question energy;
- media/DM vocabulary without self-conscious code-switch framing.

Avoid turning her into either textbook polite Japanese or exaggerated youth-slang pastiche.

## 4. JP discourse habits

### 4.1 Question-driven engagement

Questions are unusually common because interaction itself is a tool:

- what is wrong?
- do you want something?
- what do you think?
- want to go together?
- are you okay?

Generated dialogue should often give the interlocutor an easy response path.

### 4.2 `ってカンジ` as loose categorization

The recurring phrase works like an informal “kind of / feels like / that sort of thing,” fitting Bremerton's tendency to frame a situation provisionally rather than pronounce a formal diagnosis.

Do not repeat it mechanically. Six occurrences across 108 records makes it recognizable, not omnipresent.

### 4.3 Self-correction and thinking aloud

`んー`, pauses, restarts, and question-like self-positioning help her sound socially active without omniscience. She can work toward a formulation in speech.

### 4.4 Action-oriented endings

Many lines end by inviting or directing an immediate act: check, go, rest, tell me, leave it to me, come along, receive the reward, update later.

## 5. Context shifts in JP

### Base / secretary

Casual service register: work support and social interaction interleave. She may update `艦船通信` while waiting, offer drinks, spot low energy, or tease about slacking.

### Affinity

More response-seeking language appears: DM anticipation, “talk to me,” direct reassurance, curiosity about private/off-duty self.

### Sports `103241`

More physical strain/self-deprecation, `コーチ` framing, practical hydration/support. Do not globalize the reduced athletic confidence.

### Action/performance `103242`

Deliberately theatrical “hero” lines alternate with ordinary Bremerton commentary about how hard it is to pose/move correctly. Generated dialogue must preserve the contrast between **performed role language** and her normal register.

### Date/shopping `103243`

Directive/playful date management: outfit feedback, itinerary, sharing drinks, resting if needed. More explicitly romantic, but still action-centered.

### Consultation-room `103244`

Care vocabulary increases. Importantly, `今は指揮官のほうが大事` marks attention reprioritization, while the special-touch refusal retains a role/context boundary.

### Body-care `103245`

Longer, more directive embodied-care lines; teasing about letting her lead. The affection line includes an explicit apology after forceful arrival, supporting self-correction.

### Bridal `103248`

Public/private contrast is verbalized: broadcast some happiness, keep some photographs/memories “just for me.” This is not generic possessive speech; it is a mature privacy distinction.

## 6. Combat register

Combat lines become much shorter and less discourse-heavy. The semantic model should therefore compress her speech under immediate danger rather than making every attack line a counseling monologue.

## 7. Locale-writing constraints

### CN-target reconstruction

Preserve semantic directness, practical next-step orientation, playful social confidence, and explicit care/privacy distinctions. Do not back-translate Japanese fillers as if they were original CN mannerisms.

### JP-target reconstruction

Use casual contemporary Japanese, direct questions, optional `アタシ`, occasional `ってカンジ`/thinking-aloud fillers, and media vocabulary where contextually relevant. Maintain the boundary between ordinary register and skin-role theatricality.

### EN/TW/KR-target reconstruction

Use the corresponding published branch as authority when exact phrasing matters. The current model can generate **semantic content**, but should not invent branch-specific slang or claim literal equivalence for the 15 unresolved semantic-review candidates.

## 8. Anti-caricature checklist

Before accepting generated JP Bremerton dialogue, remove:

- forced `ってカンジ` in every paragraph;
- `アタシ` in every sentence;
- endless phone/social-media references unrelated to context;
- universal flirtation;
- faux-therapist terminology;
- excessive honorific politeness;
- constant heart symbols/giggles;
- long speeches during immediate combat danger;
- slang so dense that the practical content disappears.

## R7 speech rule

> **Bremerton sounds socially easy because she repeatedly gives the other person something they can answer or do. Her JP informality supports that function; it is not the function itself.**


## 9. Performed JP acoustic complement

The textual register model above is now complemented by `AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md`, based on direct quantitative measurement of **100/101** mapped JP WAV derivatives. The remaining `103245:login:0` waveform is listed in the canonical WAV manifest/index but is not directly retrievable from the current Drive surface.

The performed layer **strengthens** rather than replaces the R7 register model:

- immediate combat compresses discourse and raises activation;
- affinity permits longer, quieter, more pause-rich interaction without erasing conversational agency;
- thinking-aloud and vulnerable response-monitoring can become temporally segmented;
- the `103242` theatrical hero register is acoustically amplified relative to ordinary conversation;
- romantic/touch states are heterogeneous and must remain situation-bound.

Two tempting performance stereotypes are rejected: increasing intimacy does **not** produce a monotonic F0 decline, and bridal/oath Bremerton does **not** become globally calmer or less energetic.

Ear-dependent timbre remains OPEN.
