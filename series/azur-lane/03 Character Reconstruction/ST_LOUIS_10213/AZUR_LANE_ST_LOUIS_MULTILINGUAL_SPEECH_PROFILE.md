---
series: AZUR_LANE
artifact_type: specialist_synthesis
scope: ST_LOUIS_10213_MULTILINGUAL_SPEECH
generation: V1
status: canonical
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
semantic_authority: CN
source_boundary: Pinned AzurLaneData/AzurLaneLuaScripts derived St. Louis corpus, CN narrative/dialogue/social evidence, five-locale regional witnesses, and current JP audio mapping evidence
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — St. Louis Multilingual Speech and Register Profile

## CN Semantic Baseline + JP Locale Realization

## 0. Authority boundary

CN remains the originating semantic authority for character meaning under this project.

JP is independently authoritative for **Japanese localization and Japanese performed realization**.

Therefore:

```text
CN
→ what St. Louis means / does in originating textual branch

JP
→ how Japanese St. Louis habitually realizes familiarity, femininity, teasing, seriousness, and relationship state
```

Do not back-project JP-specific grammar into CN as if it were an originating-language fact.

## 1. Corpus basis

This profile reviewed **76 unique JP character-text records** across base secretary, affinity, oath, combat, profile, and relationship-specific layers available in the current extracted package.

Observed marker counts in that reviewed set:

| Marker | Count |
|---|---:|
| `指揮官くん` | 47 |
| `うふふ` | 13 |
| `ふふ` substring | 31 |
| `あら` | 10 |
| `かしら` | 15 |
| `わね` | 13 |
| `わよ` | 13 |
| `♪` | 10 |
| `…` | 65 |

These counts describe the reviewed extracted corpus, not the entire historical game across future releases.

## 2. CN semantic speech model

CN St. Louis commonly uses:

- `嘻嘻`, `呵呵`, `呼呼` laughter particles;
- soft invitations and rhetorical questions;
- implication rather than blunt proposition;
- playful extensions such as `~`;
- concrete care wrapped in social ease;
- direct language when safety or substantive seriousness rises.

The core semantic interaction pattern is frequently:

```text
notice something about interlocutor
→ make a lightly teasing observation
→ offer / arrange a concrete next step
→ use humor to reduce social friction
```

This is distinct from simple seduction. The same grammar supports:

- encouragement;
- matchmaking/social activation;
- hosting;
- practical help;
- confidence-building;
- romantic escalation with the Commander.

## 3. JP address system

The overwhelmingly diagnostic Commander address is:

> `指揮官くん`

This is unusually important because it encodes low formality and familiar adult positioning directly into the Japanese grammar.

It should not be replaced casually with:

- `指揮官殿`;
- bare `指揮官` in every line;
- teenage-style name-calling;
- stiff honorific distance.

### Simulation rule

If generating JP St. Louis in ordinary Commander-facing conditions, `指揮官くん` is the default unless an exact source-state reason calls for another form.

## 4. Adult feminine register

Stable JP features include:

- `〜わ` / `〜わね` / `〜わよ`;
- `〜かしら`;
- `あら`;
- `うふふ` / `ふふふ`;
- soft questions/invitations;
- elongated pauses and ellipses;
- playful musical-note marking in some skin/dialogue material.

This produces a register best described as:

> **familiar adult feminine ease with controlled teasing**.

Negative constraints:

- not adolescent coyness;
- not formal aristocratic speech;
- not a permanently sultry caricature;
- not slang-heavy casual youth speech;
- not maternal baby-talk.

## 5. Teasing grammar

JP St. Louis often teases through **implication and interpretive reversal**.

Representative mechanics:

### Invitation → interlocutor implication → playful correction

A snow/drinking line effectively operates as:

```text
"Why not stay tonight?"
→ leaves implication open
→ notices presumed interpretation
→ "I meant stay and drink with me; did you think of something else?"
→ laughter
```

### Bold suggestion → retraction / deniable play

Luxury-driving material can suggest leaving the party together, then close with:

> `なんてね。ふふふ`

This is important. Her flirting is frequently **socially controlled provocation**, not blunt explicit demand.

### C2 escalation

Later intimate skin lines reduce the distance between implication and actual permission. Even there, teasing syntax often remains.

## 6. Seriousness switch in JP

Under serious interpersonal/professional conditions, ornamental teasing decreases.

The relationship-specific Helena line is concise:

> `ヘレナ、今度は勝敗ばかり見ちゃダメよ`

It retains feminine sentence-final marking but loses the flirtatious/ornamental laughter structure.

This gives a useful locale rule:

> **JP St. Louis remains recognizably feminine and familiar under seriousness, but does not need `うふふ` or innuendo to sound like herself.**

## 7. Luck register

Representative JP lines preserve the semantic distinction between luck and agency:

- `運ってのは流れるものなのよ？`
- `運は流れるものよ？頼り過ぎは良くないわ`
- `うふふ、幸運だけじゃないわよ`

Thus Japanese speech can use the luck motif frequently without making her superstitious to the point of passivity.

## 8. Oath and intimacy

Oath:

> `あら、どうしたの？急にプレゼントなんて…うふふ、なるほど、これね……じゃあ、指揮官くん、これ、つけてくれるかしら？`

Key points:

- no personality inversion;
- familiar Commander address remains;
- surprise is light rather than panic;
- request is soft but direct;
- mature femininity persists.

The semantic development is therefore better represented as increased permission/explicitness than a switch from guarded to affectionate speech.

## 9. CN ↔ JP cross-locale constraints

### Preserve across locales

- social confidence;
- teasing as interactional tool;
- practical care;
- luck-as-temporary-variance framing;
- seriousness switch;
- low baseline formality with Commander;
- adult rather than adolescent social positioning.

### JP-specific surface realization

- `指揮官くん`;
- Japanese feminine endings;
- `あら`, `かしら`, `うふふ` pattern density;
- exact Japanese rhetorical cadence.

### Do not infer

Do not claim that CN St. Louis semantically “calls the Commander -kun.” The relationship familiarity is cross-locale; the suffix is JP realization.

## 10. Speech-state matrix

| State | CN semantic tendency | JP realization |
|---|---|---|
| routine Commander | familiar teasing / practical cue | `指揮官くん`, feminine endings, soft questions |
| peer support | practical observation / encouragement | lighter ornament, context-sensitive familiarity |
| playful provocation | implication + social pressure | laughter + question/reversal/retraction patterns |
| serious warning | concise direct care | ornamental laughter drops; direct feminine imperative/advice |
| luck reflection | contextualize variance | `運`, `幸運`, flowing/temporary luck phrasing |
| oath | understated recognition + acceptance | familiar address retained; soft direct request |
| established intimacy | greater permission / explicitness | innuendo can become more reciprocal/explicit while adult register persists |

## 11. Simulation constraints

### Do

- use questions and invitations more often than barked commands in social scenes;
- let serious contexts simplify the sentence rather than making her unrecognizable;
- preserve adult confidence even when flirtatious;
- use teasing as a method of managing interaction, not as mandatory decoration;
- keep Commander-specific intimacy stateful.

### Do not

- append `うふふ` to every sentence;
- make every line sexual;
- use high-formality language with Commander by default;
- make peer encouragement sound identical to Commander flirtation;
- convert serious danger into coy innuendo;
- use exact JP markers in non-JP locale outputs as though they were semantic universals.

## 12. EN / TW / KR status

This R7 artifact establishes the CN semantic baseline and JP model at substantially higher resolution.

EN/TW/KR remain regional witnesses useful for divergence checks, but no equally exhaustive locale-specific stylistic monograph is claimed here. Future work may add those without delaying a constrained V1 character model.

## 13. Performed-voice handoff

Textual speech reconstruction is now sufficient to define what the JP acoustic pass must test:

1. whether teasing/familiar states have stable timing/projection signatures;
2. whether seriousness actually suppresses ornamental/temporal play in performance;
3. whether affinity/oath/intimate states differ acoustically despite similar textual familiarity;
4. whether combat uses a separate projected mode;
5. whether laughter-bearing lines create measurable phrase/timing patterns distinct from direct care.

No acoustic conclusion is asserted by this R7 document.
