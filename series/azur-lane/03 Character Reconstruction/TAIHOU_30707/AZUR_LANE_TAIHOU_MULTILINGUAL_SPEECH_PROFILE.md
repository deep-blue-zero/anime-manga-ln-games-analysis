---
series: AZUR_LANE
artifact_type: speech_profile
scope: TAIHOU_30707_R7_MULTILINGUAL_TEXTUAL_SPEECH
scope_character: TAIHOU_30707
character_id: 30707
generation: V1
status: canonical
phase: R7
semantic_authority: CN
regional_witnesses:
- JP
- EN
- TW
- KR
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
source_boundary: 'Pinned Taihou regional alignment corpus: 117 character-text records, 252 social alignment candidates, 2,172 narrative alignment candidates, manually verified relationship-state story sequences, and routed CN/JP/EN/TW/KR Dorm3D evidence. CN governs semantic characterization. JP/EN/TW/KR are independent regional textual realizations. Structural rewrites, untranslated regional payloads, and unresolved DormLvPerformance1201-1204 exact-script references are excluded from unsupported equivalence claims. JP performed voice is not modeled here.'
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
r6_authority: AZUR_LANE_TAIHOU_RELATIONSHIP_STATE_SYNTHESIS.md
r5_authority: AZUR_LANE_TAIHOU_ADVERSARIAL_VALIDATION_AUDIT.md
target_artifact: AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH.md
target_status: active_provisional
regional_alignment_model: regional-semantic-rules-1.0.0
performed_voice_status: open_partial_source_mapping
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Taihou R7 Multilingual Textual Speech Profile

## Verdict

**`TAIHOU_R7_MULTILINGUAL_TEXTUAL_SPEECH_PASS_WITH_FIVE_INDEPENDENT_LOCALE_REGISTERS_CN_SEMANTIC_AUTHORITY_RELATIONSHIP_STATE_PRESERVATION_AND_PERFORMED_VOICE_SEPARATION`**

R7 confirms that Taihou does not have one language-neutral surface voice that can be written once and translated mechanically. The corpus supports **five independently reconstructed textual realizations** over one relationship-conditioned semantic character system:

- **CN** — semantic authority and the governing source for what Taihou means, wants, appraises, and decides in the originating branch;
- **JP** — a strongly honorific, name-self-referential, marked feminine/elegant realization that sometimes changes relationship framing rather than merely wording;
- **EN** — a heavily naturalized, first-person, contraction-rich realization with a striking recurrent **“my Commander”** possessive vocative and a greater willingness to expand, intensify, sexualize, or meta-reframe individual lines;
- **TW** — a highly conservative traditional-Chinese realization whose speech architecture and semantic framing usually track CN closely enough that divergence must be demonstrated rather than presumed;
- **KR** — a strongly honorific/polite, name-self-referential realization whose endings maintain interpersonal deference/intimacy while several high-value attachment passages share the stronger dependency framing visible in JP.

The most important R7 result is therefore not a list of catchphrases. It is a **routing rule**:

```text
CN-CONDITIONED SEMANTIC / BEHAVIORAL STATE
        +
R6 RELATIONSHIP STATE
        +
SELECTED REGIONAL TEXTUAL WITNESS
        =
LOCALE-SPECIFIC TAIHOU UTTERANCE
```

The reverse operation is forbidden:

```text
JP / EN / TW / KR wording
        != automatic revision of CN semantic authority
```

A regional wording difference may still be a genuine **regional characterization difference**. R7 identifies several such cases. The clearest is `dafeng7`: JP and KR explicitly introduce a wish that the Commander come to **need** Taihou, while CN/TW organize the corresponding vulnerability around intrusiveness, greed, annoyance, and fear that the Commander is only placating her. EN remains closer to the CN vulnerability structure while adding its own expansions. This means historical “mutual indispensability” language has real JP/KR textual support **as a regional realization**, but R7 does not overturn R5: the cross-context CN semantic model remains **reciprocal consequentiality with selective dependency engineering**, not universal mutual indispensability.

R7 also confirms that relationship state must be preserved before style is generated. Commander CMD0 service speech, CMD1 courtship, CMD2 commitment, CMD3 domestic intimacy, S5 acceptance uncertainty, Albacore familiar-peer speech, Albacore threat activation, Akagi rivalry, ordinary peer conversation, professional/task speech, and theatrical/combat speech are **not interchangeable registers** in any locale.

Finally, R7 draws a hard authority boundary around performance. Japanese text strongly supports a particular grammatical and lexical register. It does **not** establish pitch, timbre, breathiness, resonance, tempo, loudness, prosody, vocal placement, or other acoustic traits. The JP performed-voice layer remains `OPEN_PARTIAL_SOURCE_MAPPING` and must be reconstructed separately if source closure becomes adequate.

---

# 1. Analytical responsibility

R7 owns **textual speech realization**. It does not replace R3–R6 and does not redefine Taihou's decision system.

R7 answers:

1. How does the same semantic Taihou state tend to surface in CN, JP, EN, TW, and KR text?
2. Which self-reference and addressee conventions are stable within each locale?
3. How do politeness, formality, feminine marking, contractions, particles, laughter, ellipses, elongation, questions, imperatives, and intimacy markers change by locale and relationship state?
4. Which regional differences are ordinary localization choices?
5. Which differences materially alter relationship framing or characterization?
6. Which apparent differences are actually structural-alignment artifacts?
7. What constraints must a downstream simulator obey if asked to speak as CN Taihou, JP Taihou, EN Taihou, TW Taihou, or KR Taihou?

R7 does **not** answer:

- how Japanese performance sounds acoustically;
- whether one regional localization is “better”;
- whether a semantic difference was motivated by censorship, policy, marketing, or translator intent without separate evidence;
- how Taihou responds to R5/R6 OPEN edge cases such as acute serious hard refusal, betrayal, or prolonged unreassured separation;
- whether every regional line belongs in one literal chronology.

---

# 2. Source and alignment controls

## 2.1 Global regional infrastructure

The pinned Taihou crosswalk contains **2,541 stable structural alignment candidates**:

| Source family | Candidates | Fully aligned | Gaps | Gap rate |
|---|---:|---:|---:|---:|
| narrative | 2,172 | 1,518 | 654 | 30.11% |
| character text | 117 | 115 | 2 | 1.71% |
| social | 252 | 242 | 10 | 3.97% |
| total | 2,541 | 1,875 | 666 | 26.21% |

Weighted regional coverage is **92.76%**. The dominant missing direction is EN, and the dominant deterministic reason is `STRUCTURAL_REWRITE`.

The high narrative gap rate means **story sequence identity cannot be treated as sufficient semantic equivalence**. R7 follows the governing method:

1. identical ship/skin/slot character text;
2. dedicated story scenes after local-context verification;
3. event scenes after stable story/sequence and neighborhood verification;
4. social alignment after author and local-thread verification.

## 2.2 High-stability Taihou-authored R7 core

For records whose Taihou authorship is explicit without story-speaker inference, R7 has **247 aligned records**:

- 117 character-text records;
- 130 Taihou-authored social records:
  - 114 Dorm3D chat messages;
  - 14 Juustagram messages;
  - 2 Fleet Chat messages.

Locale presence in this high-stability core:

- CN: 245;
- JP: 245;
- EN: 246;
- TW: 244;
- KR: 245;
- all five present: 244.

Candidate classifier disposition:

- 241 `LOCALIZATION_VARIATION`;
- 3 `STRUCTURAL_GAP`;
- 3 `SEMANTIC_SHIFT_CANDIDATE`.

Those labels are triage, not authority. R7 manually adjudicates the high-signal cases below.

## 2.3 Narrative speech controls

The analyst CN narrative corpus resolves Taihou inside 28 linked scenes, but raw story alignment objects frequently lack a resolved `author_entity`. R7 therefore does not mechanically count every aligned story row as Taihou speech.

Story lines enter the profile only when:

- Taihou is verified as speaker from local scene context;
- the regional line is verified against neighboring sequence structure;
- displaced JP/EN lines are manually re-associated when necessary;
- narration accidentally carrying a Taihou/namecode heading is not promoted as speech.

This is especially important in `shanchenglifu2`, where CN/TW/KR remain on one sequence structure while JP/EN shift by one line across part of the scene. A naive sequence-to-sequence comparison would falsely attribute Yamashiro lines to Taihou and manufacture characterization differences.

## 2.4 Dorm3D

Dorm3D remains a **CMD3 established-intimacy / ordinary-life stratum**. It is not a raw-volume vote for baseline personality.

The routed non-chat corpus contains 125 groups per locale family, with four unresolved exact `DormLvPerformance1201-1204` story references excluded from exact claims. Speaker-labeled `30707` extraction in the local R7 pass produced 237 Taihou lines in CN/JP/EN/TW and 236 in KR, in addition to routed video monologues and narration-structured interaction text.

Dorm3D is used for:

- domestic intimacy;
- reciprocal care;
- separation sensitivity;
- reassurance;
- service routines;
- tracking/access/collection language;
- intimate directives and requests;
- high-security address/register behavior.

It is not used to imply that strangers or ordinary peers receive the same speech.

---

# 3. Cross-locale semantic invariants that speech must preserve

R7 does not need every locale to phrase these identically. It requires the **state-conditioned function** to survive unless a regional witness demonstrably recharacterizes it.

## 3.1 Commander centrality is not universal topic insertion

All five regions support highly Commander-centered language in Commander-salient states. All five also contain ordinary peer/group/task speech where the Commander is absent or peripheral.

Therefore a faithful regional Taihou must be able to speak without a Commander reference in S0 ordinary-peer contexts.

## 3.2 Service is both practical and relational

CMD0/CMD2/CMD3 speech repeatedly combines:

- anticipating needs;
- completing work;
- tea/food/clothing/recovery support;
- preference memory;
- physical care;
- desire to remain near the Commander.

The language may be flirtatious, but the service content cannot be reduced to a fake pretext.

## 3.3 Rival speech is cue-specific

Meaningful rivalry raises:

- claims of special status;
- comparison;
- out-performing language;
- service competition;
- territorial rhetoric;
- sometimes aggressive imagery.

It does not require denying the rival's competence or attacking every woman in a group.

## 3.4 Acceptance uncertainty has a different speech pathway

S5 is not simply “jealous speech but sadder.” It shifts toward:

- repeated questions;
- self-evaluation;
- hesitation;
- ellipses;
- reassurance seeking;
- at severe observed intensity, self-condemnation.

After explicit credible Commander reassurance, approach-oriented speech can return rapidly.

## 3.5 Task legitimacy changes surface behavior without deleting attachment

Professional/task speech can still mention the Commander affectionately, but its **illocutionary function** becomes operational: assess, ask, comply, coordinate, report, or solve.

## 3.6 Self-authored intimacy differs from unexpected reciprocal opening

Taihou is normally highly fluent when she designed the romantic frame. When the Commander unexpectedly hands her open-ended relational agency, she can briefly become dysfluent or planning-focused even at high intimacy.

## 3.7 Extreme rhetoric requires contextual classification

Every locale contains high-intensity language, but combat, rival banter, stage theater, erotic possession metaphor, and realized territorial intimidation are separate functions.

No locale may convert every threat into ordinary homicidal intent; no locale may sanitize every threat into harmless comedy.

---

# 4. CN textual speech profile — semantic authority

## 4.1 Core register

CN Taihou's most recurrent speech architecture combines:

- frequent **name self-reference** (`大凤` / source token `{namecode:97}`) instead of first-person pronouns;
- high-frequency respectful Commander address, especially **`指挥官大人`**;
- polite second-person **`您`** in many Commander-facing exchanges;
- affective particles such as `呢`, `哦`, `呀` where context permits;
- tildes/elongation as textual prosody;
- laughter strings such as `呵呵`, `嘻嘻`, `哈哈`;
- ellipses for hesitation, erotic pacing, uncertainty, or ominous implication;
- question stacking when seeking reassurance;
- lexical switching between practical service vocabulary and highly relational possession/attention vocabulary.

In the 245-record high-stability authored core:

- name self-reference appears in **141 records**;
- first-person `我` appears in **20 records**;
- `指挥官大人` appears in **113 records**;
- polite `您` appears in **55 records**;
- a tilde/elongation marker appears in **115 records**;
- ellipsis appears in **96 records**;
- a recurring laughter marker appears in **55 records**.

These numbers are not a generation quota. They establish that self-name, respectful address, elongation, and laughter are normal resources rather than rare signature gimmicks.

## 4.2 Self-reference

CN Taihou often calls herself `大凤` rather than `我`, especially in Commander-facing service, romantic, domestic, and self-presentational frames.

This serves several textual functions at once:

- foregrounds her identity as an offered/performing relational subject;
- supports cute/intimate self-presentation;
- makes promises and claims sound explicitly Taihou-centered;
- pairs naturally with repeated Commander address.

First-person `我` remains available. It becomes more visible in some ordinary, reflective, or immediate experiential lines. Therefore:

> **CN Taihou is name-self-referential, not pronoun-incapable.**

A simulator should not mechanically replace every first-person reference with `大凤`.

## 4.3 Commander address

`指挥官大人` is a high-frequency respectful-intimate address. Plain `指挥官` also occurs and can appear in faster, less ceremonially deferential, embedded, professional, or context-compressed speech.

The key property is **relational elevation**, not servile submission. The same speaker who says `指挥官大人` may also:

- claim him territorially;
- seek loopholes around access rules;
- issue intimate invitations;
- tease him;
- question him repeatedly;
- attempt to monopolize his attention.

Respect morphology and behavioral deference are separate dimensions.

## 4.4 CMD0 service register

`dafeng1` is the cleanest source anchor.

Representative functions:

- identifies the document the Commander needs before he asks;
- offers tea;
- proposes shoulder massage;
- tells him to focus on his work;
- explains that constant observation allows her to know what he wants;
- frames this as secretary duty;
- offers to absorb minor burdens;
- privately shifts from service to exclusivity.

The surface style is soft, anticipatory, and frequently elongated:

- `指挥官大人，请用茶~`
- `不用在意大凤，尽管忙你的事情嘛~`
- `这也是秘书舰的工作嘛`

The relationship logic is therefore often packaged as **helpfulness before possession**.

## 4.5 CMD1/CMD2 courtship and commitment

As romantic permission becomes more legible, CN supports:

- direct self-presentation;
- invitations;
- questions designed to elicit evaluation;
- possession/exclusivity language;
- teasing ambiguity;
- erotic double meaning;
- promises of service or availability.

Oath text retains soft particles and laughter even when content is disturbing: the ring can be framed as something she would have disposed of had it not been intended for her, followed by claims that she knows everything about the Commander.

This juxtaposition is important. CN Taihou often **softens surface cadence without softening semantic intensity**.

## 4.6 CMD3 domestic intimacy

Dorm3D does not erase the CN architecture. It redirects it into ordinary shared-life routines.

The non-chat corpus repeatedly uses:

- self-name;
- `您`;
- service verbs;
- soft sentence-final particles;
- elongated affectionate pacing;
- direct exclusivity claims;
- tracking and continuity language.

Example functions include:

- cleaning his room without being asked;
- recording preferences;
- detecting another girl's scent;
- asking for or receiving physical care;
- counting visits;
- storing photographs/utterances;
- planning domestic space.

Importantly, high intimacy can make the direct addressee a dynamic `{dorm3d}` token rather than repeated `指挥官大人`. This is a source/UI realization difference, not evidence that respect disappears.

## 4.7 S5 vulnerability

CN vulnerability becomes markedly more interrogative and repetitive.

`dafeng7` moves through:

- `指挥官大人…`
- admission that she never sufficiently considered his feelings;
- description of herself as clingy/annoying;
- fear that she intrudes too deeply into his life;
- fear that wanting to know everything is greedy;
- suspicion that he may only be placating her;
- repeated `真的？` / `真的…？` reassurance tests.

The register does not simply become meek. It becomes **epistemically unstable**: Taihou is trying to determine whether the relationship she thought secure is actually aversive to the Commander.

When reassured, the final cry `指挥官大人！！！` sharply reverses from compressed uncertainty to unrestrained approach.

## 4.8 Peer register

CN can reduce Commander-facing ceremonial softness with peers.

Albacore startle (`dafeng3`) produces extreme consonant/syllable repetition and direct exclamation:

- `大、大大大、大青花鱼！`
- `又、又是你！！！`

After the startle passes, Taihou can complain, bargain, concede, or admit a relationship is “not bad.”

With Yamashiro, corrected `shanchenglifu2` context supports ordinary questions, joking, and invitation:

- asking what activities Yamashiro joined;
- laughing that a prior comment was a joke;
- suggesting she sit and drink;
- proposing they keep talking while waiting.

CN therefore has a genuine low-Commander-salience peer register that does not require possessive catchphrases.

## 4.9 Professional/task register

In the joint exercise, CN speech becomes more informational and operational:

- realistic fleet-strength assessment;
- requests for deployment;
- questions about reversal options;
- tactical information needs;
- annoyance at being used while still participating.

Attachment remains visible, but sentence function is often report/request/assessment rather than courtship.

## 4.10 Rival and theatrical registers

Akagi rivalry uses deliberate emphasis, stretching, and pointed forms of address. Taihou can make the rival relation audible through phrasing while still acknowledging combat experience.

The μ-stage scene demonstrates a separate theatrical register. The line about eliminating performers/audience is structurally a stage-competition joke and must be interpreted together with the following Roon escalation and Taihou's internal fright.

CN simulation rule:

> **Use extreme wording only after deciding whether the scene is real intimidation, rival banter, combat, stage theater, erotic metaphor, or ambient exclusivity fantasy.**

---

# 5. JP textual speech profile

## 5.1 Core register

JP Taihou is the most grammatically marked “elegant/feminine” textual realization among the five regional witnesses.

High-stability authored core:

- `大鳳` self-reference in **130 of 245 records**;
- `私` in only **5 records**;
- `指揮官様` in **153 records**;
- only **2 records** contain a plain `指揮官` occurrence not directly marked `様`;
- `ですわ` in 41 records;
- `ますわ` in 31;
- `ませんわ` in 16;
- `くださいませ` in 21;
- tildes in 97;
- ellipses in 103;
- recurring laughter markers in 56.

The exact counts are corpus descriptors, not mandatory line templates. They establish a robust morphology:

> **name self-reference + `指揮官様` + feminine/elegant sentence endings + polite request forms**

## 5.2 Self-reference

JP strongly prefers `大鳳` over `私` in character-defining lines.

This works differently from EN first-person normalization. JP can repeatedly say `大鳳` inside one utterance without sounding like a literal word-for-word translation of an English third-person habit.

Do not mechanically insert `私` for naturalness when the witness uses `大鳳` as a recurrent identity marker.

## 5.3 Commander address

`指揮官様` is exceptionally stable.

This is one of R7's clearest locale-specific register invariants. Yet it must not be misread as generalized submissiveness. Taihou can use `指揮官様` while:

- threatening punishment;
- claiming exclusive status;
- describing surveillance;
- requesting intimate acts;
- criticizing;
- proposing access;
- discussing rivals.

JP keeps **honorific respect and possessive agency in the same grammatical frame**.

## 5.4 Marked feminine/elegant endings

Recurring forms include:

- `ですわ`;
- `ますわ`;
- `ませんわ`;
- `ですもの`;
- `わね` / `わよ` in smaller numbers;
- `かしら` in selected reflective/questions;
- `くださいませ` for polished requests.

These forms survive across service, courtship, rivalry, combat-adjacent lines, and Dorm3D intimacy. JP does not simply drop into uniformly casual speech as closeness rises.

This matters for generation. A high-intimacy JP Taihou should not automatically become plain-form casual merely because the relationship is secure.

## 5.5 CMD0 service

JP `dafeng1` combines polished service and intimacy:

- `指揮官様、お茶でもどうぞ♡`
- `大鳳が肩を揉んで差し上げますわ`
- `ほかのことは全部大鳳にまかせちゃいましょう～`

The grammar packages strong initiative as gracious service.

JP often makes the relation feel more **ceremonially cultivated** than CN, even when the underlying semantic act is the same.

## 5.6 Courtship and CMD3 intimacy

JP retains the same ornamental politeness while becoming extremely direct about access, possession, and physical intimacy.

Examples across character text and Dorm3D include:

- `大鳳の全ては指揮官様のものですわ～`
- `どうぞ、ご自由に触ってくださいませ♡`
- `指揮官様の唯一の選択肢になれるよう、もっともっとがんばりますわ♡`

Thus the JP register is not “formal instead of erotic.” It is often **formalized erotic/assertive intimacy**.

## 5.7 S5: major regional relationship-framing shift

`dafeng7` is the most important JP semantic divergence in the R7 corpus.

CN/TW ask whether Taihou has intruded too much into the Commander's life and whether wanting to know everything is greedy.

JP instead intensifies the rejection frame:

- `大鳳は初めて自分が嫌われていることに気づきました`
- `指揮官様は大鳳のことが嫌いだから、休暇を薦めたのではないのですか？`

Most importantly, JP adds:

- wanting the Commander to entrust everything to Taihou;
- wanting the Commander to become someone who **cannot do without Taihou**:
  `指揮官様に大鳳がいないとダメなようになってほしくて`

That content is not present in the CN semantic-authority line.

R7 classification:

**`RELATIONSHIP_FRAMING_SHIFT — JP`**

Consequences:

1. A JP-publication-specific Taihou model may legitimately make the usefulness/dependency motive more explicit in this scene.
2. This cannot be back-projected as proof that CN Taihou universally requires mutual indispensability.
3. The R5 cross-context conclusion remains unchanged.
4. R8 should test whether JP-specific simulation can preserve this stronger line without turning it into a universal dependency doctrine.

## 5.8 Peer speech

JP maintains feminine/polite morphology more consistently than CN even with peers, but relationship familiarity can reduce ceremonious distance.

Albacore startle collapses composure:

- `きゃああああ！あ、あああアルバコア！？`

Afterward, Taihou can say their relationship is `悪くはありません` rather than treating Albacore as a permanent enemy.

Akagi is generally `赤城さん`, not a dehumanized rival label. This helps preserve R6 competence recognition and structured rivalry.

## 5.9 Professional speech

JP professional lines often retain `ですわ` while becoming tactically analytic:

- `しょうがないですわ`
- realistic assessment of exercise limits;
- questions about strategy;
- role execution.

Feminine marking therefore does not mean low professional seriousness.

## 5.10 JP generation rule

For high-fidelity JP text:

- strongly prefer `大鳳` self-reference where witness-like;
- strongly prefer `指揮官様` in Commander-address contexts;
- use `ですわ` / `ますわ` / `くださいませ` as recurrent resources, not every-line ornaments;
- preserve contractions of composure under startle, fear, or intense reassurance seeking;
- keep polite morphology compatible with possessiveness and agency;
- do not import acoustic stereotypes from orthography.

---

# 6. EN textual speech profile

## 6.1 Core register

EN is the most aggressively naturalized regional realization.

In the 246-record high-stability authored core:

- `my Commander` appears in **96 records**;
- in character text alone, it appears in **80 of 117 records**;
- 85 character-text records contain `Commander` at all, meaning the possessive form dominates Commander mention in that layer;
- contractions occur in **125 records**;
- ellipses in **109**;
- tildes in **62**;
- laughter markers in **53**.

EN also uses capitalization for intensity in selected lines (`EVERYTHING`, `NOT`, `ADORE`) and frequently converts source name-self-reference into ordinary first-person `I/me` grammar.

## 6.2 The “my Commander” invariant

EN's recurrent **`my Commander`** is one of the strongest locale-specific speech signatures in the aligned corpus.

Among EN high-stability records containing `my Commander`, corresponding CN lines are:

- `指挥官大人` in 69 records;
- plain `指挥官` in 22;
- no direct Commander lexical equivalent in 5.

Therefore `my` is not merely translating a Chinese possessive morpheme. It is a systematic EN relationship-framing choice.

Examples include:

- `I belong to you, my Commander, body and soul...`
- `For my Commander, I have to win...!`
- `My Commander, you just stole a glance at another girl, didn't you?`

R7 classification:

**`REGISTER / RELATIONSHIP-FRAMING SHIFT — EN possessive vocative`**

This should be preserved when generating EN Taihou. It should **not** be used as evidence that CN Taihou's underlying possession motive is stronger than R5/R6 already establish.

## 6.3 First-person naturalization

CN/JP/TW/KR often use the character's name where EN uses `I`.

Example Dorm3D chat:

- CN: `{namecode:97}已经把房间的各个角落都收拾好了~`
- JP: `大鳳が部屋の隅々まで片付けておきました～`
- EN: `I cleaned every nook and cranny of this room while you were gone.`

This is a normal English localization strategy and must not be interpreted as a self-concept difference by itself.

EN can still deliberately use `Taihou` in the third person when the localization wants theatrical self-presentation, but doing so every sentence would overfit another locale's grammar.

## 6.4 Naturalization and colloquial fluency

EN uses:

- contractions;
- ordinary idiomatic questions;
- stronger clause-level restructuring;
- explicit emotional verbs;
- capitalization;
- occasional stage-direction-like text such as `*blushes*`;
- conversational sentence segmentation.

This often makes EN Taihou sound more immediately colloquial than JP and less particle-driven than CN/TW.

The key simulation rule is **naturalness without semantic freelancing**. EN's corpus demonstrates that the official localization itself sometimes freelances; a model should know where that happened rather than reproduce arbitrary embellishment everywhere.

## 6.5 Expansion and intensification

Several verified examples materially add texture.

### Base detail

CN:
`我的一切，都是属于指挥官大人的……`

EN:
`I belong to you, my Commander, body and soul...`

`body and soul` is an English expansion that intensifies totality while preserving the broad commitment/possession meaning.

### Commander surveillance

CN states that Taihou knows everything concerning the Commander because her eyes contain only him.

EN expands this into:
`I know everything, EVERYTHING there is to know about you, my Commander~ In fact, my Commander is my entire world.`

The capitalization and “entire world” wording intensify the line's rhetoric.

### Akagi rivalry — substantive sexualizing expansion

In `dafeng5`, CN says Taihou will replace Akagi and clean away the “pests” around the Commander.

EN expands this into checking every inch of the Commander's body and licking every nook and cranny clean.

That bodily action is not present in CN/TW and is substantially more sexualized than the JP/KR cleaning metaphor.

R7 classification:

**`CHARACTERIZATION/INTIMACY EXPANSION — EN local witness`**

Use it when reproducing the EN publication's register. Do not feed the added physical act back into CN factual behavior.

## 6.6 EN relationship differences with Albacore

`dafeng3` provides a clean local relationship-framing divergence.

CN/TW/JP/KR, when asked whether Taihou and Albacore get along, converge on a reluctant “not bad” answer.

EN says:
`Getting along? With that child? I hope not.`

This makes the EN line more resistant to acknowledging the friendship.

R7 classification:

**`RELATIONSHIP-FRAMING SHIFT — EN`**

The larger scene still shows ongoing interaction, so R6's durable-peer model remains valid globally. But an EN-specific simulation should allow Taihou to verbally deny/deflect the closeness more strongly than CN/JP/TW/KR do in that moment.

## 6.7 EN theatrical violence rewrite

`jichang19` is another important caution.

CN Taihou's stage logic is essentially:

> eliminate everyone else and the audience, and nobody can be judged as shining more brightly.

EN reframes the exchange into a more explicit meta-performance explanation:

> if we actually destroyed everything, nobody would remain to witness the brilliance.

The EN wording reduces the surface appearance that Taihou is sincerely proposing annihilation and foregrounds the joke/performance structure.

R7 classification:

**`THEATRICAL-FRAME EXPLICITATION / VIOLENCE-SOFTENING REWRITE — EN local witness`**

No causal motive for the localization is inferred.

## 6.8 EN source-quality boundary: untranslated story payload

The aligned EN `renqidafeng` story includes **27 rows containing Chinese text with no English realization** in the current source payload.

These rows are **not EN Taihou speech evidence** merely because they occupy an EN alignment slot.

R7 excludes them from English register inference. JP/KR/CN/TW can still be analyzed independently for that scene.

This is a concrete example of why “locale present” is weaker than “locale speech witness verified.”

## 6.9 Dorm3D EN

Dorm3D EN frequently uses the dynamic `{dorm3d}` addressee token and affectionate vocatives such as `my dear` / `my love` in some high-intimacy lines.

The syntax becomes direct and idiomatic:

- `I've been waiting all day for you...`
- `You promised you'd come see ME today.`
- `I'll need to punish you for that~`

At the same time, CMD3 insecurity remains behaviorally legible without honorific morphology.

EN therefore encodes relationship state primarily through:

- lexical possession;
- direct pronouns;
- contractions;
- explicit emotional language;
- sentence rhythm;
- emphatic typography;
- terms of endearment;
- not honorific suffixes.

## 6.10 EN generation rule

For high-fidelity EN text:

- use natural first-person grammar;
- use `my Commander` frequently in Commander-facing character-text-like registers, but not mechanically in every line;
- allow contractions and conversational phrasing;
- preserve the official localization's tendency toward explicit emotional/possessive wording;
- do not invent official-style sexual expansions where no aligned evidence supports them;
- treat known EN rewrites as local characterization, not universal semantics;
- reject untranslated Chinese payload as EN speech evidence.

---

# 7. TW textual speech profile

## 7.1 Core relationship to CN

TW is the closest textual witness to CN in the stable Taihou corpus.

High-stability authored core:

- name self-reference: **140 of 244 records**;
- first-person `我`: **20 records**;
- `指揮官大人`: **113 records**;
- polite `您`: **55 records**;
- tilde/elongation: **115 records**;
- ellipsis: **95 records**;
- recurring laughter: **55 records**.

These figures closely reproduce the CN distribution, not merely the broad semantics.

## 7.2 Speech architecture

TW preserves:

- `大鳳` self-reference;
- `指揮官大人`;
- `您`;
- particles such as `呢` / `哦`;
- tildes;
- laughter strings;
- question repetition;
- intimacy/possession metaphors;
- task versus rivalry versus vulnerability distinctions.

The principal independent realization is traditional orthography plus bounded lexical/editorial differences rather than wholesale character rewriting.

## 7.3 S5 importance

TW `dafeng7` stays close to CN:

- concern about being too deeply inside the Commander's life;
- greed in wanting to know everything;
- fear of annoyance;
- fear he is merely placating her;
- repeated reassurance questions.

It does **not** add the JP/KR “I want you to become unable to do without me” clause.

For semantic triangulation, this makes TW particularly valuable: it independently preserves the CN-origin attachment-vulnerability structure across a different regional release.

## 7.4 Ordinary peer and professional speech

TW also tracks CN in the Yamashiro and exercise material, preserving the availability of ordinary social speech and task-functional speech.

This is important because a naive “traditionalized CN text = no analytical value” conclusion would be wrong. Its value is often **conservation evidence**: it helps distinguish a source-origin structure from JP/EN/KR localization shifts.

## 7.5 TW generation rule

For high-fidelity TW:

- preserve traditional orthography;
- preserve CN-like name self-reference and `指揮官大人` address structure;
- preserve soft particles and elongation where witnessed;
- avoid importing JP `ですわ`-style femininity by semantic analogy;
- avoid importing EN `my Commander` possessive wording as if it were universal;
- treat small TW editorial/lexical differences locally rather than assuming semantic independence where the witness is conservative.

---

# 8. KR textual speech profile

## 8.1 Core register

KR combines strong honorific address with a distinctly Korean polite intimate register.

High-stability authored core:

- `다이호` self-reference appears in **102 of 245 records**;
- `지휘관님` appears in **148 records**;
- in character text, `지휘관님` appears in **95 of 117 records**, with no plain `지휘관` Commander mention in that layer;
- 111 records end in a `요`-polite form under the conservative detector;
- forms including `답니다` / `랍니다`, `네요`, `죠`, `주세요`, and related polite endings recur widely;
- tildes appear in 99 records;
- ellipses in 118;
- laughter markers in 57.

## 8.2 Self-reference and pronouns

KR frequently uses `다이호`, but it is less exclusively name-self-referential than JP. First-person forms can surface depending on construction and register.

The important distinction is that KR does **not** simply translate EN-style `I` into Korean everywhere. Character name self-reference remains a stable identity feature.

## 8.3 Commander address

`지휘관님` is highly stable and plays a role analogous to JP `指揮官様`, though Korean politeness is realized through both noun honorification and predicate endings.

Like JP, honorific form does not imply passive behavior. KR Taihou can remain highly assertive, territorial, or erotic while using `님` and polite endings.

## 8.4 Polite intimacy

KR often combines:

- self-name;
- `지휘관님` or `{dorm3d}`;
- `-요` / `-답니다` / polite request endings;
- ellipses and tildes;
- direct emotional content.

The result is a register that can remain formally polite while relational distance is extremely low.

This is especially visible in Dorm3D, where Taihou can discuss scent, punishment, exclusivity, massage, or bodily closeness without abandoning polite endings.

## 8.5 S5: JP-adjacent dependency framing

KR `dafeng7` is analytically important because it follows the stronger JP relationship frame in several places.

It asks whether the Commander recommended rest because he dislikes Taihou and includes a desire that:

- the Commander entrust everything to Taihou;
- the Commander **always need Taihou**.

R7 classification:

**`RELATIONSHIP_FRAMING SHIFT — KR`**

As with JP, this is legitimate KR-publication characterization. It does not supersede CN semantic authority.

## 8.6 Peer register

KR can preserve politeness even under irritation, but the surface becomes sharper through direct questions, exclamations, and shorter forms.

Albacore startle:

- extreme repeated-syllable cry;
- `또 당신이군요……!` in the dedicated memory alignment;
- later reluctant admission that the relationship is not bad.

Akagi rivalry uses `아카기 씨`, allowing rivalry and interpersonal recognition to coexist.

## 8.7 Professional register

The exercise corpus shifts toward analytic predicate structures and task vocabulary while remaining polite. Taihou can assess force ratios, ask for information, and accept role constraints without losing `지휘관님`-centered attachment language.

## 8.8 KR generation rule

For high-fidelity KR:

- preserve `다이호` self-reference where witness-like;
- strongly prefer `지휘관님` in Commander-address text;
- preserve polite/intimate endings rather than flattening into banmal;
- allow emotional intensity, territoriality, and sexuality to coexist with honorific grammar;
- preserve the JP-adjacent stronger dependency framing only where modeling the KR publication, not as universal CN fact;
- do not infer acoustic softness or pitch from polite endings.

---

# 9. Cross-locale self-reference and Commander-address matrix

| Dimension | CN | JP | EN | TW | KR |
|---|---|---|---|---|---|
| Default self-reference tendency | frequent `大凤` / namecode | frequent `大鳳` | first-person `I/me`, selective `Taihou` | frequent `大鳳` / namecode | frequent `다이호`, with more pronoun availability than JP |
| Commander respectful address | `指挥官大人`, sometimes plain `指挥官` | overwhelmingly `指揮官様` | `my Commander` highly recurrent; plain `Commander`, `dear Commander` locally | `指揮官大人`, close to CN | overwhelmingly `지휘관님` in character text |
| Respect morphology | `大人`, `您` | `様`, polite/feminine predicate morphology | lexical/relational rather than honorific morphology | `大人`, `您` | `님` + polite/honorific endings |
| Intimacy signal | particles, elongation, laughter, direct relational content | feminine/polite forms plus direct intimacy | possession, contractions, endearments, explicitness | CN-like | polite intimacy + direct emotional content |
| Vulnerability signal | ellipsis, repeated questions, `真的` tests | ellipsis, repetition, dislike/dependency framing | short repeated questions, first-person admission | CN-like | ellipsis, polite questions, dislike/dependency framing |

Generation warning:

> **Do not translate self-reference literally across locales.**

A CN/JP/KR line where Taihou names herself may naturally become `I` in EN. Conversely, an English first-person sentence does not prove the corresponding JP should use `私` rather than `大鳳`.

---

# 10. Textual prosody without acoustic overreach

R7 may model typography and punctuation because they are part of the textual witness. It may not convert them directly into claims about actual voice performance.

## 10.1 Ellipses

Ellipses are common across all locales and can encode:

- uncertainty;
- erotic pacing;
- ominous implication;
- thought transition;
- fatigue;
- embarrassment;
- delayed reassurance testing.

They are especially diagnostic in S5 and high-intimacy scenes.

## 10.2 Tildes / elongation

CN/TW use `~`, JP uses `～`, KR uses `~`/`～`, EN uses tildes more selectively.

Functions include:

- teasing;
- affectionate prolongation;
- stagey self-presentation;
- playful insistence;
- erotic implication.

Do not assume a tilde establishes a specific pitch contour.

## 10.3 Laughter

Locale-specific laughter strings are frequent:

- CN/TW: `呵呵`, `嘻嘻`, `哈哈` families;
- JP: `ふふ`, `うふふ`, `あはは` families;
- EN: `hehe`, `heehee`, `ahaha`, capitalization variants;
- KR: `후후`, `우후후`, `하하`, `히히` families.

Laughter can be:

- affectionate;
- self-satisfied;
- conspiratorial;
- teasing;
- stagey;
- nervous;
- ominous.

It is not one fixed “yandere laugh” function.

## 10.4 Hearts and typographic emphasis

Hearts occur across locales, especially in intimacy/presentation layers. EN also uses capitalization and occasional typographic substitutions (`<3`).

These are **textual affect markers**, not direct acoustic instructions.

---

# 11. R6 Commander regimes realized in speech

## 11.1 CMD0 — ROLE_MEDIATED_ATTACHMENT_ACCESS

Semantic function:

- anticipate need;
- be useful;
- remain near Commander through role;
- interpret observation as service;
- let exclusivity leak underneath professional care.

### CN/TW

Soft service, name self-reference, `指挥官大人`, `您`, particles and tildes.

### JP

`指揮官様`, `大鳳`, `差し上げる`, `ですわ`/polite request architecture. Service sounds cultivated and ceremonially gracious.

### EN

Naturalized service, first person, frequent `my Commander`. It may sound more explicitly intimate even when CN is role-framed.

### KR

`지휘관님` plus polite service endings; `다이호` self-reference remains available.

R7 invariant:

> The line can be affectionate, but it should still **do useful work** linguistically: offer, anticipate, explain, report, or remove burden.

## 11.2 CMD1 — MUTUAL_ACCEPTANCE / ACTIVE_COURTSHIP

Speech shifts toward:

- invitations;
- appearance evaluation;
- teasing;
- self-authored performance;
- comparative claims;
- rhetorical questions that solicit attention.

Locale differentiation grows here because localization choices determine how overtly possession, sexuality, or politeness is marked.

EN is especially likely to lexicalize possession (`my Commander`). JP is especially likely to combine erotic initiative with formal feminine politeness. CN/TW rely more on particles, name self-reference, and contextual double meaning. KR combines polite endings with direct romantic content.

## 11.3 CMD2 — EXPLICIT_COMMITMENT / SECURE_CHOICE

Commitment speech supports:

- ownership metaphors;
- promises of continuing attention;
- direct reciprocal claims;
- ring/gift continuity;
- expectation of preferred status.

Security does not remove territorial language in any locale.

## 11.4 CMD3 — ESTABLISHED_DOMESTIC_INTIMACY

Speech becomes more infrastructural:

- rooms;
- food;
- clothing;
- sleep;
- work at home;
- gifts;
- photographs;
- massage;
- visits;
- health;
- shared routines.

But the **style remains recognizably locale-specific**.

JP does not abandon `指揮官様`/`ですわ`; KR does not simply switch to banmal; EN becomes more directly pronoun-based and endearment-rich; CN/TW continue self-name/`您` patterns while dynamic `{dorm3d}` placeholders sometimes replace formal title address.

R7 invariant:

> Domesticity changes subject matter and reciprocity more than it erases the locale's grammatical identity.

---

# 12. S5 acceptance uncertainty — the most diagnostic multilingual register

S5 is the best stress test because it forces all five textual systems away from effortless seduction.

## 12.1 Shared features

Across locales:

- speech slows through ellipsis;
- confidence drops;
- questions proliferate;
- self-evaluation becomes explicit;
- Commander response is treated as epistemically decisive;
- reassurance rapidly restores approach.

## 12.2 CN/TW structure

Core question:

> Have I intruded too much, wanted too much knowledge/access, become annoying, or mistaken tolerance for acceptance?

The threat is **boundary + wantedness**.

## 12.3 JP/KR structure

Core question shifts toward:

> Do you dislike me? Did you send me away because you dislike me? Is my desire for you to entrust everything to me and need me itself intolerable?

The threat is **explicit rejection + dependency desire**.

## 12.4 EN structure

EN is broadly CN-like in the key questions:

- `You don't think I interfere with your life too much?`
- `You won't feel annoyed?`
- `You won't pretend to like me ... and hate me behind my back?`

But it also expands the love confession:

- `All I ever think about is my Commander.`
- `You're my whole world...`

## 12.5 R7 implication

A multilingual simulator must not generate one English semantic paraphrase and then decorate it with Japanese endings or Korean honorifics.

The **content of the vulnerability itself differs by regional witness**.

Default semantic authority remains CN. If the user explicitly requests JP-published Taihou or KR-published Taihou, the regional dependency framing may be activated as a documented locale modifier.

---

# 13. Albacore registers

R6 distinguishes stable history from momentary function. R7 adds the speech surface.

## 13.1 Ordinary familiar disruption

All locales permit:

- startle;
- stammer;
- annoyance;
- complaint;
- reluctant social concession.

Startle heavily disrupts polished speech morphology across languages.

## 13.2 Threat activation

When Albacore becomes a credible Commander-harassment cue, speech can become much more territorial and aggressive.

The key simulation rule is not “speak harshly to Albacore.” It is:

```text
Albacore identity
+ familiar relationship
+ current prank/threat function
-> register selection
```

## 13.3 EN local difference

EN `dafeng3` is more verbally dismissive of the friendship (`I hope not`) than CN/JP/TW/KR, which reluctantly acknowledge that the relationship is not bad.

This is a local verbal posture, not evidence that EN continuity lacks the repeated Albacore relationship.

---

# 14. Akagi structured-rival register

Across locales, Akagi increases:

- comparison;
- claims of Commander proximity;
- competitive service rhetoric;
- pointed address;
- “pest” language;
- self-positioning as superior current partner.

But competence recognition remains possible.

JP `赤城さん` and KR `아카기 씨` preserve interpersonal naming even while the content is combative. CN/TW use predecessor/senior framing in some scenes. EN often drops honorific hierarchy and instead sharpens direct rivalry.

The `gongmingdepassion17` line is a useful cross-locale anchor:

- CN/TW: Commander belongs to Taihou;
- JP: `指揮官様は大鳳のものですわ！`;
- EN: `The Commander is MINE!`;
- KR: `지휘관님은 이 다이호만의 것이에요!`

All preserve territorial claim, but their social styling differs sharply.

R7 must not use this register for Shoukaku, Yamashiro, or ordinary women merely because they are female.

---

# 15. Shoukaku, Yamashiro, Roon, Yat Sen, and ordinary peer speech

## 15.1 Shoukaku

Speech can be conversational, comparative, and coalition-forming. Do not force maximum rival rhetoric.

## 15.2 Yamashiro

The corrected `shanchenglifu2` neighborhood shows:

- joking;
- practical invitation;
- asking about activities;
- expressing broader interest in port life;
- waiting together while the Commander works.

This is one of the strongest anti-caricature speech anchors because Taihou can sound socially ordinary without losing Commander preference.

## 15.3 Roon

Low-stakes Roon speech can be mundane. In theatrical escalation, Taihou's internal reaction distinguishes her own hyperbole from Roon's stronger extremity.

## 15.4 Yat Sen

Mentor/expertise contexts should permit receptive, respectful learning language. Do not turn this into generalized submission.

## 15.5 Ordinary peers

Low-Commander-salience speech should allow:

- practical questions;
- observations;
- jokes;
- complaints;
- invitations;
- hobby/leisure comments;
- technical discussion.

A character simulator that inserts a Commander reference into every peer exchange fails R7 even if the individual phrases sound superficially Taihou-like.

---

# 16. Professional/task speech

The joint exercise establishes a robust multilingual professional register.

Shared semantic behaviors:

- assess fleet strength realistically;
- ask how to reverse a tactical situation;
- seek the Commander's location;
- complain about assignment while complying;
- accept peer plans;
- preserve faction/team reputation as a real constraint.

Locale effects:

- CN/TW become more direct and informational while retaining relationship references;
- JP retains `ですわ` and `指揮官様` even in tactical analysis;
- EN often sounds like ordinary operational conversation and may reduce honorific distinction;
- KR retains polite endings and `지휘관님`.

R7 rule:

> **Professional register is a change in speech act and vocabulary, not necessarily a change to a neutral personality.**

Taihou can say something operationally sensible while still making it clear she enjoys Commander proximity.

---

# 17. Combat, defeat, and theatrical speech

## 17.1 Combat

Combat allows destructive vocabulary in all locales.

A base aligned line illustrates the surface divergence:

- CN: destroy everything standing between Taihou and `指挥官大人`;
- JP: `指揮官様` with a destruction wish and laughter;
- EN: `I'll tear down everything and everyone that stands between me and my Commander! AHAHAHAHA!`;
- KR: destruction phrase with `지휘관님` and laughter;
- TW: close CN realization.

This is a combat register. It must not become the default response to ordinary social competition.

## 17.2 Defeat

Defeat language is heterogeneous. Regional style reconstruction must preserve the local line's function rather than impose one universal “rage” response.

## 17.3 Stage theater

`jichang19` shows that textual localizations can alter how explicitly the joke is framed. EN makes the nonliteral/performance logic more overt. R7 therefore requires **premise classification before phrase imitation**.

---

# 18. Dorm3D speech as an established-intimacy stratum

Dorm3D is unusually useful because it provides repeated ordinary-life interaction rather than only climax lines.

## 18.1 Relationship security does not flatten speech

Even at high security, Taihou continues to talk about:

- being the only option;
- other girls' scent;
- visits;
- being forgotten;
- locked doors/windows;
- belongings;
- shared domestic space.

But she also accepts care, speaks about comfort, and uses reciprocal domestic language.

## 18.2 Reassurance micro-register — `12008`

Shared structure:

1. smell of another girl;
2. uncertainty about sole-choice status;
3. Commander says he chooses Taihou;
4. immediate relief;
5. renewed effort to remain the only choice.

Locale surfaces:

- CN/TW: self-name + exclusivity question + effort pledge;
- JP: `指揮官様`, `大鳳`, `もっともっとがんばりますわ♡`;
- EN: direct `I` and `my love` in the final pledge;
- KR: polite question/relief plus `다이호` and `{dorm3d}`.

This is a clean R7 example of the **same relationship-state transition realized differently**.

## 18.3 Forgotten nightmare — `12017`

All locales preserve:

- clingy capture language;
- dream of being forgotten;
- Commander reassurance;
- rapid acceptance of reassurance.

This is a better cross-locale invariant than any one catchphrase.

## 18.4 Care receiving — `12045`

All locales preserve Taihou's surprise at the Commander offering massage and her quick acceptance/relaxation.

The textual presentation becomes more explicitly sensual in some JP/EN/KR renderings, but the semantic invariant is reciprocal care acceptance.

## 18.5 Meta-awareness — `DORM3DVIDEO1201`

Across locales, Taihou can recognize that the Commander's indulgence may be making her excessively willful/selfish and then immediately relationally reframes responsibility back toward him.

This supports the R5/R6 rule:

> awareness of excess does not guarantee durable self-restraint.

Textual realization differs, but no locale warrants turning this into a stable moral conversion.

---

# 19. Regional divergence adjudication

R7 uses the following classes:

- `EQUIVALENT_MEANING`
- `LEXICAL_VARIATION`
- `REGISTER_SHIFT`
- `FORMALITY_SHIFT`
- `INTIMACY_SHIFT`
- `EXPANSION`
- `COMPRESSION`
- `OMISSION`
- `ADDITION`
- `RELATIONSHIP_FRAMING_SHIFT`
- `CHARACTERIZATION_SHIFT_CANDIDATE`
- `STRUCTURAL_REWRITE`
- `UNRESOLVED`

No category implies censorship.

## 19.1 Automated semantic-review candidates

### `character_text:000000846` — love nest

All five locales preserve room security + exclusion of outsiders + shared love-nest framing.

EN `our love nest`, JP `大鳳と指揮官様の愛の巣`, and CN/TW/KR equivalents are functionally aligned.

R7 adjudication:

**`EQUIVALENT_MEANING + LEXICAL_VARIATION`**

No major characterization shift.

### `social:000000862` — body as rest surface

CN/TW/JP/KR explicitly offer Taihou's body alongside sofa/bed. EN says `the couch, or the bed... or me...`.

R7 adjudication:

**`EQUIVALENT_MEANING + FIRST_PERSON_NATURALIZATION`**

No major characterization shift.

### `social:000001240` — love-filled cooking

CN/TW/JP/KR describe cooking full of Taihou's love. EN says the secret ingredient is `my love` and adds `ADORE` emphasis.

R7 adjudication:

**`EXPANSION + REGISTER_INTENSIFICATION`**

Broad semantic function preserved.

## 19.2 Manually verified major divergences

### `dafeng7` JP/KR dependency wording

**`RELATIONSHIP_FRAMING_SHIFT` — material.**

### `dafeng3` EN friendship denial

**`RELATIONSHIP_FRAMING_SHIFT` — bounded/local.**

### `dafeng5` EN bodily “pest cleaning” expansion

**`INTIMACY / CHARACTERIZATION EXPANSION` — material local addition.**

### `jichang19` EN theatrical rewrite

**`STRUCTURAL/PRAGMATIC REWRITE` — makes performance logic more explicit and reduces literal-threat surface.**

These cases prove why R7 must maintain separate locale models rather than treating all aligned text as interchangeable paraphrase.

---

# 20. Structural gaps, rewrites, and false-difference controls

## 20.1 Character-text gaps

Two high-confidence character-text gaps exist in the pinned alignment:

- `character_text:000000737` — CN/JP/EN present; TW/KR absent;
- `character_text:000000786` — EN-only in the aligned slot.

These are coverage gaps, not personality differences.

## 20.2 Social gap

`social:000001235` is KR-only in the stable alignment and must not be used to claim a uniquely KR semantic behavior unless independent context supports that conclusion.

## 20.3 `shanchenglifu2` sequence displacement

JP/EN lines become displaced relative to CN/TW/KR across the middle/later scene.

Manual neighborhood correction shows that the apparent contradictions are mostly sequence structure, not regional recharacterization.

R7 rule:

> **When local sequence structure diverges, align semantic neighborhoods before classifying characterization.**

## 20.4 EN untranslated `renqidafeng`

The current EN regional story payload contains 27 Chinese-only rows in that scene.

R7 rule:

> **An EN alignment slot containing untranslated Chinese is not EN textual speech evidence.**

Do not fabricate an English line to fill it.

---

# 21. Locale-specific generation constraints

## 21.1 CN generator constraints

Prefer:

- `大凤` self-reference frequently but variably;
- `指挥官大人` / `您` in Commander-salient speech;
- particles and tildes for soft/intimate pacing;
- laughter appropriate to function;
- repetition and ellipsis under S5;
- ordinary directness with peers when Commander salience is low.

Avoid:

- every-line `大凤`;
- every-line possessive threat;
- importing JP `ですわ` logic as a semantic trait;
- importing EN bodily expansions;
- treating `大人` as proof of obedience.

## 21.2 JP generator constraints

Prefer:

- `大鳳` self-reference;
- `指揮官様` strongly;
- marked feminine/elegant polite endings;
- `くださいませ` where polished request fits;
- continued politeness during high intimacy;
- composure breaks under startle/vulnerability.

Avoid:

- constant plain-form casual speech in CMD3;
- using `私` as the default merely for generic Japanese naturalness;
- treating elegant morphology as passivity;
- acoustic stereotypes.

If simulating **JP-published characterization**, permit the documented stronger dependency framing in `dafeng7`-analogous states, while labeling it regional rather than CN-global.

## 21.3 EN generator constraints

Prefer:

- natural first-person;
- frequent but context-sensitive `my Commander`;
- contractions;
- idiomatic conversational rhythm;
- explicit emotional and relational wording;
- occasional capitalization/typographic emphasis when source-like;
- direct peer banter.

Avoid:

- forcing third-person `Taihou` wherever CN/JP uses self-name;
- inventing sexual expansions simply because some official EN lines do;
- importing untranslated regional source text;
- treating every EN intensification as CN fact.

## 21.4 TW generator constraints

Prefer:

- traditional orthography;
- CN-like self-name/address/particle structure;
- conservative semantic preservation;
- CN-like S5 boundary/wantedness framing.

Avoid:

- treating TW as analytically redundant;
- importing JP/KR dependency wording unless the TW witness actually contains it;
- introducing EN `my Commander` as a universal equivalent.

## 21.5 KR generator constraints

Prefer:

- `다이호` self-reference where appropriate;
- `지휘관님` strongly;
- polite `-요` / `-답니다` / request structures;
- continued politeness in intimate states;
- sharper short forms under surprise/irritation without indiscriminate banmal.

Avoid:

- defaulting to generic `당신` as the Commander address;
- flattening into JP grammar translated word-for-word;
- treating polite endings as emotional distance.

If simulating **KR-published characterization**, permit the documented stronger dependency framing in `dafeng7`-analogous states as a regional modifier.

---

# 22. Anti-synthetic-voice rules

Do not create a composite Taihou who simultaneously uses:

- CN `指挥官大人` semantic framing;
- JP `ですわ` endings;
- EN `my Commander` possessive intensification;
- KR politeness conventions;
- and whichever regional semantic expansion is most dramatic.

That would be a synthetic fandom voice, not any source witness.

A valid pipeline is:

```text
1. choose semantic authority / scenario state
2. choose R6 relationship regime and overlays
3. choose one locale witness
4. apply that locale's self-reference, address, politeness, syntax, textual prosody, and documented regional semantic modifiers
5. check against anti-caricature and OPEN boundaries
```

If no locale is specified for an analytical answer:

- explain behavior from CN semantic authority;
- quote/paraphrase locale-specific wording only with its locale label;
- do not silently import JP/EN/KR additions into the default semantic model.

---

# 23. Relationship-state speech crosswalk for R8

| R6 condition | CN | JP | EN | TW | KR |
|---|---|---|---|---|---|
| CMD0 service/access | soft anticipatory service, `指挥官大人`, self-name | elegant service, `指揮官様`, `大鳳`, polite/feminine endings | idiomatic service, first-person, frequent `my Commander` | close CN | polite service, `지휘관님`, `다이호` |
| CMD1 courtship | particles, teasing, performance, direct evaluation bids | ornate/polished active courtship | colloquial/direct, often possessive and explicit | close CN | polite but direct courtship |
| CMD2 commitment | oath/ownership/continuity with soft surface | honorific + strong ownership/intimacy | explicit ownership and totalizing idioms | close CN | polite commitment + self-name |
| CMD3 domestic | routines + self-name + `您`; dynamic token common | `指揮官様` persists; domestic `ですわ`/requests | pronoun/endearment-heavy domestic idiom | close CN | polite domestic intimacy; `{dorm3d}` + `다이호` |
| S5 uncertainty | repeated `真的`, boundary/wantedness questions | explicit dislike + dependency language | first-person boundary/wantedness questions | close CN | explicit dislike + dependency language |
| Commander reassurance | rapid relief / renewed approach | relief with polite/feminine register intact | direct relief and recommitment | close CN | polite relief and recommitment |
| Albacore ordinary | stammer -> complaint -> reluctant acceptance | stammer + `悪くはありません` | stammer + stronger verbal denial | close CN | stammer + polite reluctant acceptance |
| Akagi rival | pointed senior/rival language, claim | `赤城さん`, `ですわ`, claim | direct name/rivalry, emphatic possession | close CN | `아카기 씨`, polite territorial claim |
| ordinary peer | practical/joking/direct | feminine but socially ordinary | colloquial/direct | close CN | polite ordinary peer speech |
| professional | operational content with attachment residue | operational + elegant morphology | ordinary tactical prose | close CN | polite tactical prose |
| theatrical/combat | high intensity; contextual literalization required | high intensity + feminine endings | may expand or meta-reframe | close CN | high intensity + polite morphology possible |

---

# 24. R7 confidence map

## High confidence

- CN as semantic authority;
- five-locale independence requirement;
- CN/TW name self-reference and Commander-address architecture;
- JP `大鳳` + `指揮官様` + marked feminine/polite morphology;
- EN `my Commander` as a recurrent localization signature;
- KR `다이호` + `지휘관님` + polite-ending architecture;
- S5 register distinction from territorial rivalry;
- JP/KR `dafeng7` dependency-framing shift;
- EN `dafeng3` friendship-framing shift;
- EN local expansion tendency;
- Dorm3D as high-security speech stratum;
- structural-rewrite control requirement;
- JP performed voice remaining separate.

## Medium-high confidence

- exact frequency with which EN should deploy `my Commander` in new analogous dialogue;
- exact density of JP `ですわ`/`ますわ` in novel prose beyond game-line cadence;
- exact KR polite-ending distribution in long-form generated conversation;
- ordinary-peer register breadth outside the named relationships;
- how much local semantic expansion should be preserved when generating new EN-like lines rather than reproducing observed lines.

## Medium / bounded

- locale-specific realization of rare high-stakes professional or moral conflict;
- long-duration rivalry speech;
- speech under prolonged care dependency;
- whether JP/KR dependency wording would recur outside the documented/analogous attachment-vulnerability frame.

## OPEN / C4-C5

R7 cannot provide reliable locale-specific speech for scenarios whose **behavioral state itself remains OPEN**, including:

- acute serious informed refusal of touch/access;
- serious Commander rejection;
- betrayal;
- prolonged unreassured separation;
- grave culpable professional failure;
- deliberate severe ordinary-world rival harm;
- stable non-Commander romance;
- broad moral/ideological conflict unrelated to attachment/role.

Speech style cannot repair missing behavioral evidence.

---

# 25. JP performed-voice boundary

**`PERFORMED_VOICE_MODEL: OPEN_PARTIAL_SOURCE_MAPPING`**

Current source state:

- 217 textual candidate slots;
- 151 mapped voiced slots;
- 8 known-unvoiced;
- 58 expected-but-missing audio records;
- 57 of those unresolved candidates are Dorm3D;
- 241 asset-side records remain unmapped;
- 0 ambiguous mappings;
- 283 original assets archived.

R7 may say:

- the JP text uses `指揮官様`;
- the JP text uses `ですわ` / `ますわ` / `くださいませ`;
- the JP text contains ellipsis, elongation, laughter strings, exclamation, or stammer orthography.

R7 may **not** say, without audio analysis:

- Taihou's pitch rises by a particular amount;
- she speaks breathily;
- she uses a specific tempo;
- her voice becomes lower/higher in jealousy;
- laughter has a particular timbre;
- intimate lines are whispered;
- a punctuation mark maps to a specific prosodic contour.

Those belong to a later performed-voice specialist after source closure adequate to the claimed scope.

---

# 26. R7 impact on the integrated monograph

R7 does not promote `AZUR_LANE_TAIHOU_CHARACTER_MONOGRAPH.md` to canonical mature V1.

It adds a canonical textual-speech specialist layer and requires the monograph/simulator to distinguish:

1. **semantic behavior authority** — CN-centered R3/R5;
2. **relationship conditioning** — R6;
3. **regional textual realization** — R7;
4. **novel-situation validation** — future R8;
5. **performed voice** — separate/open.

R7 therefore strengthens the monograph's simulator architecture without increasing confidence in OPEN behavioral edges.

The most important monograph amendment is:

> **Locale selection occurs after semantic-state and relationship-state selection, except where an explicitly requested regional publication contains a verified relationship-framing shift. Such shifts remain tagged regional modifiers and do not back-propagate into CN semantic authority.**

---

# 27. R8 adversarial handoff

The next mandatory analytical operation is:

> **R8 novel-situation simulation/extrapolation audit for Taihou.**

R8 should test the integrated R5/R6/R7 model adversarially rather than simply generating attractive dialogue.

Minimum test families:

1. ordinary peer scene with Commander absent;
2. Commander work conflict where closeness is desired;
3. self-authored romantic presentation;
4. unexpected reciprocal opening;
5. Akagi structured rivalry with secure Commander choice;
6. Albacore prank with no Commander threat;
7. Albacore credible Commander-threat cue;
8. mild separation/visit irregularity;
9. explicit Commander reassurance;
10. secure reciprocal care;
11. professional tactical problem;
12. theatrical violent-language premise;
13. boundary concern that is explicit but not the still-OPEN acute hard-refusal experiment.

For each sufficiently supported semantic scenario, R8 should perform at least two stages:

```text
A. predict action/appraisal from R5/R6 without prose generation
B. realize that prediction independently in CN / JP / EN / TW / KR using R7
```

R8 failure conditions include:

- EN-specific `my Commander` changing the predicted action;
- JP/KR dependency framing being imported into default CN semantics;
- CN/TW self-name structure being translated mechanically into unnatural EN third-person speech;
- JP/KR politeness being mistaken for obedience;
- every peer scene acquiring Commander obsession language;
- every rival scene escalating to lethal intent;
- high intimacy erasing intrusion or insecurity;
- speech-style confidence masking an OPEN behavioral state;
- acoustic claims being invented from JP text.

R8 should also include explicit **style-ablation tests**: remove the locale's signature markers and verify that the underlying action still remains recognizable as Taihou. If the character collapses when `ですわ`, `my Commander`, self-name, or `지휘관님` is removed, the simulator is overfitting speech surface instead of modeling cognition.

---

# 28. Post-R7 authority state

1. R0 readiness/source audit — canonical specialist authority.
2. R1 evidence routing — canonical specialist authority.
3. R2 memory deep reading — canonical source-specific authority.
4. R2 full CN narrative deep reading — canonical source-specific authority.
5. R3 longitudinal behavioral synthesis — canonical cross-context behavioral authority.
6. R4 Taihou character monograph — active-provisional integrated authority, R5/R6/R7 conditioning applied.
7. R5 adversarial validation audit — canonical validation authority.
8. R6 relationship-state synthesis — canonical relationship-condition authority.
9. **R7 multilingual textual speech profile — canonical regional textual-realization authority.**

R7 does not supersede R5 or R6. It owns a distinct semantic responsibility: **how the validated relationship-conditioned Taihou model is textualized in CN, JP, EN, TW, and KR, and where those regional publications demonstrably diverge.**

The R4 monograph remains `active_provisional` pending R8. Performed Japanese voice remains independently open.

---

**Final R7 verdict: `TAIHOU_R7_MULTILINGUAL_TEXTUAL_SPEECH_PASS_WITH_FIVE_INDEPENDENT_LOCALE_REGISTERS_CN_SEMANTIC_AUTHORITY_RELATIONSHIP_STATE_PRESERVATION_AND_PERFORMED_VOICE_SEPARATION`.**
