---
series: AZUR_LANE
artifact_type: audit
scope: ST_LOUIS_10213_RECONSTRUCTION_READINESS
generation: V1
status: canonical
source_boundary: "Pinned Azur Lane multilingual extracted character corpus, current source-status augmentation, and JP audio mapping state"
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: "1.0.0"
source_build_id: "AZL-2026-08-22-4cca5c24-cc8e9fdf"
semantic_authority: CN
regional_witnesses: [JP, EN, TW, KR]
readiness_grade: C
readiness_score: 57.3
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Azur Lane — St. Louis Reconstruction Readiness Audit

## 0. Purpose

This audit begins the St. Louis (`ST_LOUIS_10213`) character-reconstruction workflow under `AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md` v1.0.0.

It executes the method's pre-generation checklist and Phases R0–R4 sufficiently to establish the correct analytical posture before a V1 monograph is allowed to accumulate broad claims.

The current conclusion is:

> **St. Louis has a moderate but usable Grade-C corpus. A constrained active-provisional monograph is justified; a Takao-level full behavioral simulator is not yet justified.**

The correct next objective is to strengthen a bounded model through adversarial validation, relationship synthesis, multilingual speech reconstruction, and JP performed-voice closure rather than filling gaps with trope assumptions.

---

# 1. Canonical locations

## Analysis evidence package

`02 Extracted Character Corpora/ST_LOUIS_10213/`

Drive ID: `16v2JMgqsUlAL-rqik4RcpLeXn4a-VQ-C`

## Reconstruction home

`03 Character Reconstruction/ST_LOUIS_10213/`

Drive ID: `18QiLSV6PhZbD1A95FBIEGG2Kk_7d9111`

## Governing reconstruction method

`00 Frameworks and Methods/AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md`

Drive ID: `1vSc1nloVuYFcVYtln3czUwUYWSP75XlnknHE7i3h48o`

---

# 2. Phase R0 — Corpus and readiness audit

## 2.1 Readiness

Current readiness:

- Grade: **C — moderate usable corpus**
- Score: **57.3 / 100**
- model: `readiness-2.1.0`

Component scores:

- narrative depth: 11.25
- dedicated-story depth: 0.0
- dialogue breadth: 13.12
- social-context diversity: 2.5
- relationship-context diversity: 10.0
- regional coverage: 13.51
- source-system diversity: 6.92

The Grade-C posture in the governing method supports:

- constrained character profile;
- high-confidence observed patterns;
- limited conditional decision rules;
- speech tendencies where evidence is sufficient.

It does **not** justify broad claims about domains poorly represented in the corpus.

## 2.2 Composition warnings

Three warnings materially govern interpretation:

### `COMMANDER_HEAVY`

Approximately **79.2%** of normalized character dialogue is Commander-facing.

Implication:

Commander flirtation and skin interaction cannot simply be projected onto peer social behavior.

### `SKIN_HEAVY`

Approximately **62.3%** of the normalized character dialogue corpus is non-base-skin material.

Implication:

Skin scenarios are valuable for stable recurring mechanisms but cannot outvote narrative/peer behavior merely through volume.

### `MANY_UNALIGNED_RECORDS`

Regional structural gaps:

- 171 / 980 stable candidates;
- 17.45% raw gap rate;
- dominant gap family: narrative;
- dominant missing direction: `missing_CN`;
- dominant deterministic explanation: `STRUCTURAL_REWRITE`.

Implication:

CN semantic reconstruction should prioritize scenes actually present in the CN originating branch. Regional narrative material without CN correspondence can inform locale characterization but should not silently become CN semantic authority.

---

# 3. Source-system closure

Current source-system state:

| Layer | Status | Reconstruction consequence |
|---|---|---|
| narrative story | PRESENT — 18 linked records | usable, but no dedicated St. Louis developmental story |
| character memory | NOT_FOUND | major limitation; no character-centered arc equivalent to Takao's seven-part memory |
| base dialogue | PRESENT — 29 | strong baseline/Commander material |
| non-base skins | PRESENT — 48 | rich but context-biased |
| interactive skin | PRESENT — 20 capability records | useful for intimate context, not global personality frequency |
| affinity | PRESENT — 8 | Commander-state modeling possible |
| oath | PRESENT — 1 | commitment state represented |
| combat | PRESENT — 7 | limited combat voice/behavior |
| relationship-specific | PRESENT — 2 | Helena/Lucky-unit evidence |
| Juustagram | PRESENT — 5 linked posts | useful peer/social controls |
| Fleet Chat | NOT_FOUND | no evidence, not parser failure |
| Dorm3D chat | NOT_FOUND | no evidence, not parser failure |
| Island relationship | NOT_FOUND | no evidence |
| Dorm3D non-chat | SUPPORTED_NOT_FOUND | parser boundary closed; explicit absence |
| Island non-relationship | SUPPORTED_NOT_FOUND | parser boundary closed; explicit absence |

There is no unresolved Dorm3D/Island parser gap blocking St. Louis reconstruction.

---

# 4. JP performed-voice source readiness

Current JP audio state:

- readiness: `AUDIO_PARTIAL`;
- candidate text/audio-reference slots: 77;
- mapped voiced slots: 69;
- known unvoiced text slots: 5;
- expected text slots without mapped audio: 3;
- unmatched archived audio assets: 7;
- affinity: 8 / 8 mapped;
- oath: 1 / 1 mapped;
- combat: 7 / 7 mapped.

The three unresolved text-side records are:

- `102130:couple_encourage:0`;
- `102130:couple_encourage:1`;
- `102134:vote:0`.

The unmatched asset set contains `link1` and `link2`, making the relationship-specific mappings obvious high-priority audit candidates, but no join should be forced until source metadata confirms it.

Performed voice therefore remains an **analytical closure task**, not a source-acquisition blocker.

---

# 5. Phase R1 — Evidence map

## 5.1 Strongest narrative/peer anchors

### Boise / 树城 — `boyixi3`, `boyixi6`

High-value evidence for:

- personalized gift-giving;
- reading another person's insecurity;
- playful social pressure;
- information asymmetry used as a game;
- betting/commitment enforcement;
- confidence-building that can become overbearing.

Especially important adversarial fact:

St. Louis admits that **regardless of who won the bet, she intended Boise to perform the same exposure task**. This means her teasing cannot be reduced to harmless verbal play. She sometimes engineers social outcomes.

### Honolulu — `huonululu2`

High-value evidence for:

- close familiarity;
- deliberate introduction/facilitation with the Commander;
- recognizing Honolulu's limited social circle;
- teasing as a method of social activation;
- fashion/self-presentation encouragement;
- explicit admission that she enjoys teasing Honolulu.

The scene itself notes that St. Louis understands Honolulu's personality extremely well.

### Helena — `hailunna1`, `hailunna7`, relationship-specific dialogue

High-value evidence for:

- affectionate older-sister framing;
- checking on Helena's work;
- explaining Helena's behavior to the Commander;
- urging the Commander to take care of Helena;
- discouraging Helena from overcommitting herself to victory;
- protective concern that survives into high-stakes/alternate narrative material.

### New Year ensemble — `xiaotianexinnian3–7`

Useful peer/leisure controls for:

- playful competitiveness;
- social curiosity;
- fashion interest;
- willingness to participate in unfamiliar cultural customs;
- dinner/group leisure;
- confidence in Cleveland's resilience;
- light pressure toward group participation.

### VOICE / alternate-history material — `yihailiusheng12–17`, `yihailiusheng9`

Treat cautiously as structurally unusual/alternate-context evidence.

Useful recurring mechanisms include:

- admitting concern rather than masking it;
- bringing an expert into a worried group;
- separating wartime seriousness from legitimate leisure;
- desire to travel and enjoy the saved world;
- practical understanding of logistics technology;
- apologizing when injured and becoming a burden;
- prioritizing Helena's survival/mission under catastrophe.

These claims should be strengthened only when they agree with ordinary-source evidence.

## 5.2 Social system

Five Juustagram appearances provide small but useful controls:

- concern when Honolulu is distressed;
- safety awareness around dangerous food;
- memory of Honolulu's embarrassing octopus incident;
- confidence-building advice to Boise about showing her face;
- noticing how Louisville changes when cooking.

The sample is small; it supports mechanisms rather than broad social-frequency claims.

---

# 6. Phase R2 — Anchor-reading result

No dedicated St. Louis memory sequence exists.

Therefore the reconstruction must be triangulated from **distributed appearances**, with Boise/Honolulu/Helena carrying disproportionate weight because they contain sustained interpersonal action rather than one-line cameo behavior.

The absence of a dedicated story limits confidence in:

- private self-concept;
- deep developmental history;
- sustained internal conflict;
- long-form failure/recovery;
- private grief;
- what she does when her usual social confidence fails.

This absence is a genuine evidence limitation, not an invitation to infer from archetype.

---

# 7. Phase R3 — Preliminary context ledgers

## Professional / task-oriented

Observed:

- delivers reports;
- understands secretary burden;
- can discuss logistics technology in practical terms;
- responds to uncertain technical risk by bringing an expert;
- accepts host-defined roles during a party rather than insisting on helping;
- recognizes that luck is not a substitute for competence.

Preliminary rule:

> **St. Louis is socially relaxed but not unserious about practical competence.**

Confidence: C2 within observed domains.

## Peer-social

Observed:

- initiates contact easily;
- facilitates interaction among shy people;
- uses teasing to lower/raise social stakes deliberately;
- gives gifts with recipient-specific utility;
- likes lively gatherings;
- moves easily between hospitality, banter, advice, and mild provocation.

Preliminary rule:

> **Her default peer strategy is active social steering rather than passive observation.**

Confidence: C2.

## Commander baseline

Observed:

- familiar from the beginning;
- lightly flirtatious;
- uses luck as a recurring playful frame;
- offers practical care;
- establishes public/private intimacy boundaries without presenting physical closeness itself as taboo.

Confidence: C1/C2.

## Commander affection / intimacy

Observed:

- domestic access and teasing increase;
- invitations become direct (date, drinking, driving, travel, physical proximity);
- later skin states can be explicitly sexual/physically intimate;
- oath is accepted with composure rather than a shy identity break.

Important constraint:

This evidence is very skin-heavy and Commander-specific.

## Combat / crisis

Observed:

- luck vocabulary persists;
- victory is explicitly not attributed to luck alone;
- defeat can be reframed as a bad day rather than catastrophic self-condemnation;
- relationship-specific line warns Helena not to sacrifice everything for victory;
- alternate catastrophic evidence prioritizes Helena's survival and mission.

Confidence: C2 for luck framing; C3 for broad high-stakes crisis psychology because sustained canonical crisis evidence is limited.

## Leisure

Observed:

- likes lively events;
- drinks alcohol in skin context;
- enjoys parties and travel;
- is willing to rest and socialize;
- can become competitive in trivial play;
- offers to help with food preparation at a gathering but there is **no evidence of high cooking skill**.

Confidence: C2 for social leisure; OPEN for general culinary competence.

---

# 8. Phase R4 — Provisional cognitive model

## 8.1 Governing hypothesis

St. Louis is best provisionally reconstructed as:

> **a socially confident, relationship-oriented operator who uses humor, teasing, practical care, and deliberate social orchestration to keep people connected and moving, while treating luck as temporary opportunity rather than a substitute for competence.**

This is deliberately more mechanism-specific than labels such as "flirtatious older sister".

## 8.2 Four provisional operating systems

### A. Social connection / atmosphere management

Activated by:

- awkward groups;
- shy friends;
- reunions/parties;
- emotional stagnation;
- interpersonal distance.

Typical outputs:

- initiate contact;
- introduce people;
- make a joke;
- provoke a response;
- redirect attention;
- encourage participation;
- turn uncertainty into a socially actionable interaction.

### B. Practical care

Activated by:

- overwork;
- discomfort;
- danger;
- loneliness;
- another person's insecurity.

Typical outputs:

- useful gifts;
- checking in;
- arranging support;
- warmth/food/drink/physical comfort;
- asking others to look after someone;
- encouraging rest or connection.

Care is frequently wrapped in teasing rather than solemnity.

### C. Playful provocation / social pressure

Activated when St. Louis believes another person is too withdrawn, hesitant, or overcontrolled.

Typical outputs:

- bets;
- jokes;
- flirtatious pressure;
- engineered encounters;
- provocative clothing suggestions;
- selective withholding of information;
- calling out obvious avoidance.

Adversarial warning:

> **Her social confidence can overrun another person's preferred pace.**

Boise and Honolulu are evidence against portraying all of her teasing as perfectly calibrated or purely consensual fun.

### D. Luck / contingency framing

Stable ideas include:

- luck flows rather than staying with one person;
- favorable timing should be exploited;
- bad outcomes do not prove permanent failure;
- victory is not "just luck";
- one should not over-rely on luck.

Provisional function:

> **Luck language helps St. Louis accept variance without surrendering agency.**

This is closer to opportunistic resilience than fatalism.

---

# 9. Preliminary relationship models

## Helena

High-confidence functional model:

> **protective older sister + interpreter + social advocate.**

St. Louis praises Helena, explains her tendencies, tries to prevent overcommitment, and repeatedly pushes the Commander/others to support her.

Risk:

She may interpret Helena for others in ways that reduce Helena's own control over self-presentation.

## Honolulu

High-confidence functional model:

> **close friend whose shyness St. Louis deliberately challenges through teasing and social exposure.**

The relationship is affectionate, familiar, and asymmetrical in social initiative.

## Boise

Moderate/high-confidence functional model:

> **confidence-building target + friend St. Louis actively engineers into greater exposure.**

St. Louis is observant and generous, but also manipulative in the literal low-stakes sense that she designs the bet so the behavioral outcome occurs regardless of winning.

## Commander

Provisional state model:

### C0 — familiar/playful baseline

Low formality and immediate teasing. Physical attraction/intimacy is not treated as inherently shocking.

### C1 — personal access

Domestic space, private knowledge, one-on-one outings, and deliberate teasing become more central.

### C2 — explicit romantic/physical intimacy

Direct invitations, exclusivity, drinking/driving/travel imagery, physical closeness, and sexualized reciprocity become explicit.

### Oath

Commitment is received with composure and a request for the Commander to place the ring. This does not look like a personality inversion.

Important limitation:

The Commander arc is dialogue/skin-heavy and should not be treated as a complete narrative romance biography.

---

# 10. Preliminary CN speech model

Stable CN surface tendencies include:

- frequent `呵呵 / 嘻嘻 / 哎呀 / 啊呀 / 呼呼`;
- sentence-final `哦 / 呢 / 吧 / 呀`;
- rhetorical questions;
- playful prolongation with `~`;
- deliberate segmentation for teasing emphasis, e.g. `指·挥·官`;
- mixing English identity markers such as `Lucky Lou`, `hello`, `OK`;
- invitations framed as questions that are often socially pressuring rather than uncertain;
- teasing followed by explicit "just kidding" or laughter as a pressure-release mechanism.

Underlying speech mechanism:

> **She often says something socially provocative, watches the reaction, then controls the intensity through laughter, a rhetorical retreat, or a practical next step.**

---

# 11. Preliminary JP speech model

The stable JP aligned text is highly marked.

Across 76 inspected non-placeholder JP dialogue records:

- `指揮官くん`: 47 occurrences across 43 lines;
- `うふふ`: 13 lines;
- `ふふふ`: 14 lines;
- broader `ふふ` family: 31 lines;
- `あら`: 10 lines;
- `かしら`: 15 lines;
- `わ`: 51 occurrences across 44 lines;
- `♪`: 10 occurrences across 9 lines;
- heart symbols: 2 occurrences in inspected records.

The most important register feature is **`指揮官くん`**.

Unlike a formal Commander-address system, JP St. Louis uses a familiar `-kun` frame from baseline onward. Combined with feminine endings, laughter, and soft directives, JP gives her a strongly familiar adult-feminine / teasing register.

Common structures include:

- `〜かしら`;
- `〜わ / 〜わよ`;
- `〜してちょうだい`;
- `〜てもいいわよ`;
- rhetorical questions that presume intimacy;
- laughter before or after a provocative line.

Cross-locale caution:

> JP encodes familiarity and adult femininity more grammatically than CN. CN carries much of the same social function through particles, laughter, playful pacing, and innuendo. Do not replace the CN semantic model with JP surface grammar.

---

# 12. Initial adversarial tests

## Hypothesis: "St. Louis is always carefree"

**REJECT.**

She directly admits concern about dangerous technology, brings in an expert, expresses battle caution regarding Helena, and in high-stakes material prioritizes survival/mission.

## Hypothesis: "St. Louis believes luck determines outcomes"

**REJECT.**

She explicitly says luck is temporary, should not be over-relied upon, and that victory is not achieved through luck alone.

## Hypothesis: "Her teasing is always harmless"

**REJECT.**

Boise's bet is intentionally structured so that the same exposure occurs regardless of outcome. Honolulu also identifies teasing as part of St. Louis's motive.

## Hypothesis: "She is flirtatious with everyone"

**OPEN / unsupported as global claim.**

Commander-facing material strongly supports a flirtatious intimate register. Peer scenes support teasing and confidence-building, but not universal sexual flirtation.

## Hypothesis: "She is only a social butterfly and lacks practical cognition"

**REJECT.**

She reasons about logistics technology, worries about technical risk, seeks expert input, handles reports, and distinguishes luck from skill.

---

# 13. Current simulation boundary

At Grade C, St. Louis is currently suitable for **constrained simulation**, especially:

### Better-supported

- casual peer conversation;
- social gatherings/dinners;
- teasing among friends;
- hospitality and care;
- confidence-building interventions;
- Commander baseline/romantic states where explicitly specified;
- leisure/travel/party scenarios;
- routine work and practical discussion;
- mild competition;
- reactions to shy or socially hesitant people.

### Moderate / caution

- high-stakes protection;
- formal leadership;
- serious technical-policy discussion;
- novel friendships with highly atypical personalities.

### Weak / do not overclaim

- sustained grief/depression;
- private shame without witnesses;
- ideological doctrine;
- long-duration domestic routine;
- intense anger/hostility;
- romantic behavior toward non-Commander characters;
- manipulation under genuinely high stakes;
- how she behaves after major interpersonal rejection.

A robust general behavioral simulator is **not yet established**.

---

# 14. Remaining workflow

## R5 — Adversarial validation

Required next:

- search all anchor scenes for counterexamples to social-confidence and care rules;
- test whether "teasing as care" explains too much;
- distinguish playful coercion from actual disregard for autonomy;
- test luck framing under real failure/stress rather than only game lines.

## R6 — Relationship synthesis

Priorities:

1. Helena;
2. Honolulu;
3. Boise;
4. Commander;
5. Cleveland/party-group behavior if evidence supports a distinct rule.

## R7 — Multilingual speech

JP is already strong enough for an initial model.

Still required:

- systematic CN/JP/EN/TW/KR aligned comparison;
- identify whether EN or KR materially changes flirtation/familiarity;
- separate lexical localization from character-state change.

## R8 — Simulation extrapolation

Only bounded C1–C3 rules should be emitted until R5–R7 close.

## R9 — Monograph

A mutable active-provisional V1 monograph is being opened as the canonical topical home.

## R10 — Performed voice

Recommended after text-model stabilization.

St. Louis's audio is already close enough to closure that a Takao-style mapping cleanup is likely efficient:

- audit `link1/link2` against the two relationship-specific lines;
- classify `vote` and gift/UI streams;
- produce one-WAV-per-utterance derivatives;
- then run the same three-pass acoustic analysis sequence.

---

# 15. Final readiness verdict

`ST_LOUIS_MONOGRAPH_BUILD_APPROVED_CONSTRAINED_SCOPE`

The build should proceed, but with a deliberately narrower authority claim than Takao V1.

The correct standard is:

> **Build only the St. Louis we can explain conditionally from evidence; leave the low-evidence interior life OPEN rather than manufacturing it from the flirtatious-older-sister surface archetype.**
