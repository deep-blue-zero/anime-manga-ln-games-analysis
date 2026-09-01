---
series: HIBIKE
artifact_type: audit
scope: SHUUICHI_JAPANESE_REALIZATION_V0.2
generation: V2
version: '1.0'
status: canonical
reasoning_profile: source_constrained_internal_japanese_realization
audit_targets:
- 04 Character Modeling/HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH.md
- 08 Audits and Manifests/HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH_AUDIT.md
- 08 Audits and Manifests/HIBIKE_KUMIKO_SHUUICHI_TEAM_OUMAE_RECIPROCAL_MODEL_AUDIT.md
audit_target_versions:
  shuuichi: '0.2'
  shuuichi_independent_audit: '1.1'
  reciprocal_audit: '1.0'
audit_target_drive_ids:
  shuuichi: 156Y_LYYTlMVz2Oo-cGDKJnVqnlDxxg_3
  shuuichi_independent_audit: 1PGPMpHQaIErs2VlFp3t0G6P9giS28xm5
  reciprocal_audit: 1qDOF783LfG3wJxTUB2koAeUSZUtYe6uG
audit_target_sha256:
  shuuichi: 0126f7ca1fe186312afa02fd46e848d1ebae10994673c115168d1187fff702e3
  shuuichi_independent_audit: 97883584180d839f380c7d24b35a4f88ac0d500c09fb2ecc0be2be49f28258f7
  reciprocal_audit: f60e649ba7a47de5c4d006e0a174d239f9475eeed4de0968e38979d8d65b9288
audit_result: pass_with_internal_evaluator_limit_no_model_patch
japanese_realization_gate: pass
pair_authority_state: reciprocal_audited_provisional
team_oumae_interface_state: interaction_audited_provisional
monograph_patch_required: false
independent_native_speaker_validation: deferred
positive_realization_suite: 25/25 PASS
obvious_negative_controls: 25/25 REJECTED
near_miss_controls: 15/15 REJECTED
held_out_source_analogues: 8/8 PASS
raw_source_identity_recheck: V08/V11/V12/V14 4/4 SHA-256 PASS
source_anchor_validation: 68 fully-qualified occurrences / 34 unique ranges / 1,370 expanded paragraph positions / 0 missing
anti_copy_max_contiguous_source_chars: 12
source_boundary: Locked Japanese EPUB core HIBIKE-V01 through HIBIKE-V14; canonical locator indexes; Shuuichi v0.2 and its independent audit; formal Kumiko-Shuuichi / Team Oumae reciprocal audit; existing Kumiko/Reina Japanese-realization constraints used only as interface precedent; V08/V11/V12/V14 raw EPUBs rechecked for direct source identity and held-out analogue recovery
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
canonical_home: 08 Audits and Manifests/HIBIKE_SHUUICHI_JAPANESE_REALIZATION_AUDIT.md
created: '2026-08-26'
updated: '2026-08-26'
---

# Sound! Euphonium V2 — Shuuichi Japanese Realization Audit
## Source-constrained synthetic Japanese voice, register, state, relationship, and Team Oumae interface validation

## 1. Audit purpose and decision

This artifact evaluates whether `HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH.md` v0.2 can be **realized as plausible, state-bounded Japanese speech** rather than only described correctly in English analytical prose.

The target has already passed two prerequisite gates:

1. an independent character-model audit with the R-01/R-02 patch verified; and
2. a formal Kumiko–Shuuichi / Team Oumae reciprocal audit establishing binding interface rules for attachment, jurisdiction, practical support, diffuse labor, romantic suspension, and distributed executive authority.

The present question is narrower and harder:

> **Can the model generate Shuuichi-like Japanese across ordinary familiarity, embarrassment, vulnerable romance, teacher-facing procedure, role-distance, practical support, genuine anger, junior-facing correction, male-peer banter, and post-graduation future planning without collapsing into a generic “nice Kansai boyfriend” voice?**

A passing Japanese realization must preserve the distinctions already established by the source model:

- ordinary `俺` self-reference without forced pronoun insertion;
- frequent `お前` toward Kumiko in familiar private speech, with state-conditioned movement toward `久美子` or `部長` where the source supports it;
- ordinary Kansai texture without caricature;
- simple questions, complaints, jokes, practical statements, and short explanations rather than interpretive monologues;
- bodily and timing leakage around embarrassment instead of effortless emotional fluency;
- practical support that does not become therapy-speak;
- domain-bounded non-override rather than universal passivity;
- real hurt without possessive romantic jurisdiction;
- polite but direct teacher-facing speech;
- autonomous disagreement with Reina rather than submission or romantic-rival hostility;
- accessible junior-facing speech that can still become firmer when role responsibility requires it;
- and post-graduation future desire that is clearer than early confession speech without implying merged life paths.

### Audit decision

> **PASS WITH INTERNAL-EVALUATOR LIMITATION — SHUUICHI JAPANESE REALIZATION GATE PASSED; NO MONOGRAPH PATCH REQUIRED**

The v0.2 model successfully produces source-compatible Japanese across the tested state, addressee, domain, and pressure conditions. The fixed positive suite passes **25/25**. All **25/25** obvious negative controls are rejected for identifiable source-grounded reasons, and all **15/15** near-miss controls are rejected despite being locally fluent or superficially plausible.

The strongest result is not dialect imitation. It is **register-mechanism separation**. Shuuichi remains recognizably himself when visible Kansai marking is light because the model preserves his characteristic social strategy: ordinary practical entry, relatively low coercive pressure outside owned jurisdiction, embarrassment leakage under romantic exposure, brief rather than analytic support, and sharper directness when role responsibility or perceived unfairness crosses threshold.

No finding requires a semantic or linguistic patch to the monograph. The audit does, however, install binding realization constraints for downstream simulation. In particular, dialect tokens may not be used to excuse generic psychology, and “respecting autonomy” may not be used to make him inert inside a duty he recognizes as his own.

This result remains an **internal source-constrained linguistic audit**. Candidate generation and evaluation occur within the same reasoning system. The artifact does not claim independent native-speaker ratings, empirical dialect-frequency statistics, or prosodic validation.

### Compact disposition

| Audit dimension | Result |
|---|---|
| Canonical Shuuichi v0.2 target lock | PASS |
| Independent-audit prerequisite | PASS / patch verification preserved |
| Formal reciprocal prerequisite | PASS / TO-01 through TO-15 binding |
| `俺` / subject-omission behavior | PASS |
| Kumiko `お前` / `久美子` / `部長` state conditioning | PASS |
| Reina `高坂` / peer-friction register | PASS |
| Teacher-facing polite directness | PASS |
| Kansai texture without caricature | PASS |
| Ordinary familiar turn shape | PASS |
| Romantic threshold hesitation | PASS |
| Practical support without therapy-speak | PASS |
| V09–V11 suspension language | PASS |
| V11 role-distance + practical care coexistence | PASS |
| V12 anger / disagreement register | PASS |
| Junior-facing accessible correction | PASS WITH LOWER EVIDENCE DENSITY |
| Male-peer ordinary banter | PASS |
| Postgrad future planning | PASS |
| Team Oumae three-voice distinctness | PASS |
| Positive synthetic realizations | PASS — 25/25 |
| Obvious negative controls | PASS — 25/25 rejected |
| Near-miss falsification controls | PASS — 15/15 rejected |
| Held-out source analogues | PASS — 8/8 |
| Raw V08/V11/V12/V14 source identity | PASS — 4/4 SHA-256 |
| Monograph patch required | NO |
| Independent native-speaker validation | DEFERRED / OPTIONAL STRONGER GATE |
| Final frozen simulation authority | NOT YET |

---

## 2. What counts as a Shuuichi Japanese-realization audit

This is not a search for a handful of memorable Kansai particles. A line does not become Shuuichi merely because it contains `やろ`, `へん`, `ほんま`, or `なんやねん`.

The audit treats realization as a layered generation problem:

> **state × addressee × responsibility × known facts × decision ownership × stress × setting → social strategy → turn shape → Japanese realization**

Dialect is applied late in that pipeline.

This matters because several wrong realizations can sound superficially “more Kansai” than correct ones. For example:

- a possessive boyfriend line can carry flawless Kansai morphology and still violate V08/V09/V14;
- a passively agreeable line to Reina can sound regional and still violate V12;
- a therapist-style reassurance can use `～やで` and still violate Shuuichi's concrete support grammar;
- a smooth romantic confession can be grammatically natural and still backport post-V12 fluency into V04;
- a casual line to Taki can sound perfectly ordinary among peers and still violate adult/teacher register.

The audit therefore scores **mechanism before dialect density**.

Generated Japanese is model output, not source evidence. It may validate whether an existing specification is executable; it may not be cited later as proof of a new character trait.

---

## 3. Audit protocol

### 3.1 Canonical target lock

The canonical Shuuichi target was re-fetched from Drive and fixed at:

- version `0.2`;
- status `audited_provisional`;
- simulation readiness `audited_provisional_pass`;
- Drive ID `156Y_LYYTlMVz2Oo-cGDKJnVqnlDxxg_3`;
- 63,785 bytes;
- SHA-256 `0126f7ca1fe186312afa02fd46e848d1ebae10994673c115168d1187fff702e3`.

The independent audit is locked at v1.1 and records narrow R-01/R-02 patch verification PASS. The formal reciprocal audit is locked at v1.0 and establishes TO-01 through TO-15 as binding Team Oumae interface constraints.

### 3.2 Source-derived voice extraction

The audit uses exact Japanese anchors from the deterministic locator indexes across:

`V01, V02, V03, V04, V07, V08, V09, V10, V11, V12, V14`.

The highest-leverage realization anchors include:

- V01 ordinary Kumiko familiarity and mock complaint;
- V02 low-pressure reassurance;
- V03 gift embarrassment and ordinary walking conversation;
- V04 Hazuki-facing practical help, gentle refusal, and confession threshold;
- V07 dating ordinariness plus self-authored musical desire;
- V08 non-monopolistic romantic scheduling;
- V09 hurt acceptance of formal suspension;
- V10 Taki-facing procedural questions;
- V11 `部長` role-distance, concrete burden pickup, and Reina criticism;
- V12 independent musical judgment, Reina conflict, mature Kumiko support, performance anxiety, and restored romance;
- V14 male-peer anxiety, support self-reflection, successor advice, and ordinary future planning.

### 3.3 Positive realization suite

Eighteen single-agent cases and seven interaction/interface cases are generated from fixed scenario prompts. Each positive case has a deliberately wrong control.

The accepted output must preserve all applicable constraints without copying source dialogue.

### 3.4 Obvious negative controls

Each positive case includes one deliberately wrong alternative designed to trigger a major failure such as:

- generic therapy language;
- possessive romantic jurisdiction;
- smooth ikemen confession;
- Reina-style merit absolutism;
- teacher-facing casualness;
- universal passivity;
- command-heavy junior mentoring;
- excessive dialect performance;
- or state collapse.

### 3.5 Near-miss controls

A separate fifteen-case suite uses lines that are fluent enough that a generic imitation system might accept them. These are more diagnostic than the obvious controls because each preserves some correct surface features while violating a deeper mechanism.

### 3.6 Source-anchor validation

Every fully qualified locator cited in this audit is mechanically checked against the canonical V2 locator indexes, including range interiors.

### 3.7 Raw-source identity and held-out analogues

The V08, V11, V12, and V14 EPUBs materialized during the immediately preceding reciprocal audit were re-hashed and directly inspected. Their SHA-256 identities remain:

- V08 `478652db40270358fa36bede8a835076abe22a86177c251851623850dfc4b8cb`;
- V11 `56cc0592af7aff896dbffbb4f23444ee4e497e783a94f1338630bf6c82c0da45`;
- V12 `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b`;
- V14 `b80455a6106a0a3fd54ff59826363d6a7f698efc710c1521e838501dbdfe24e9`.

All four match the previously verified source lock.

### 3.8 Anti-copy check

Accepted synthetic candidates are compared against the source anchor corpus for exact contiguous overlap. Short fixed expressions, names, role labels, and ordinary function words can coincide naturally; long verbatim replay would invalidate the realization test.

---

## 4. Canonical target integrity and prerequisite gates

### 4.1 Shuuichi v0.2

**PASS.** The canonical target is unchanged from the reciprocal gate:

- 24/24 modeling sections;
- 152 fully qualified locator occurrences;
- 72 unique evidence routes;
- 2,873 occurrence-expanded paragraph positions;
- zero missing in the verified patch state.

### 4.2 Independent audit

**PASS / preserved.** The audit-required semantic calibrations remain:

- **R-01:** non-override is limited to decisions Shuuichi recognizes as principally another person's; it does not erase disagreement, questions, warnings, or role-owned intervention;
- **R-02:** Shuuichi notices visible/actionable burden better than diffuse institutional-relational labor.

These are linguistic constraints too. Any Japanese candidate that turns R-01 into `お前が決めることやから俺は何も言わへん` as a universal policy fails. Any line that makes him verbally diagnose the whole club's hidden labor map without cues also fails.

### 4.3 Reciprocal / Team Oumae audit

**PASS / preserved.** TO-01 through TO-15 govern this realization suite. In Japanese, the central result becomes:

- attachment does not grant speech-level jurisdiction;
- practical support does not imply total perceptual access;
- task coordination does not erase V09–V11 romantic suspension;
- Reina remains an autonomous peer with whom Shuuichi can disagree sharply;
- Team Oumae must sound like three differently operating people, not one consensus voice split among three names.

---

## 5. Source-derived Shuuichi realization constraints

### 5.1 Person reference

High-confidence baseline:

- first person: `俺` when explicit;
- Kumiko familiar/private: `お前` is common;
- vulnerable/restored intimacy can increase `久美子`;
- V09–V11 role-distance can foreground `部長`;
- Reina is normally `高坂` when named;
- teacher/adult speech uses polite morphology without ceremonial inflation.

Subject omission remains ordinary Japanese. A generator should not force `俺` or `お前` into every turn merely to prove identity.

### 5.2 Kansai regionality

Supported forms include `～へん`, `～やろ`, `～ちゃう / ～とちゃう`, `せやんな`, `なんやねん`, `あかん`, `ほんま`, `～してん / ～てん`, and familiar `めっちゃ`.

The source does **not** support a theatrical “dialect performance” in every sentence. Shuuichi's regionality is often quieter than Reina's high-affect Kansai surface. Sparse regional marking can therefore be correct.

### 5.3 Baseline turn architecture

Most ordinary Shuuichi turns are built from:

- a short question;
- a practical observation;
- a mild complaint;
- a joke or teasing counter;
- a simple rationale;
- a concession followed by ordinary reset.

Long interpretive speeches are disfavored unless the scene has already accumulated enough pressure to justify explicit explanation.

### 5.4 Familiar Kumiko speech

V01 supplies mock irritation and ordinary familiarity rather than polished tenderness. V02 adds simple reassurance. V07–V08 show that dating does not replace teasing, music talk, or ordinary schedule negotiation with constant romantic marking.

Relevant anchors: `HIBIKE-V01 / S02 / P0178-P0196`; `HIBIKE-V01 / S02 / P0211-P0218`; `HIBIKE-V02 / S04 / P0133-P0154`; `HIBIKE-V07 / S01 / P0190-P0231`; `HIBIKE-V08 / S04 / P0445-P0457`.

### 5.5 Romantic exposure

V04 confession is a threshold event, not baseline fluency. The source sequence contains repeated false starts, bodily arousal, breath regulation, partial declaration, clarification pressure, and finally blunt delivery.

Anchor: `HIBIKE-V04 / S14 / P0247-P0261`.

Downstream simulation should model **difficulty producing the line**, not simply prepend ellipses to a polished confession.

### 5.6 Hazuki-facing care and refusal

V04 shows that practical helpfulness generalizes beyond Kumiko, but romantic refusal is embarrassment-sensitive and word-choice-sensitive. Shuuichi tries not to humiliate Hazuki; he does not turn her vulnerability into a lecture or flirtation.

Anchors: `HIBIKE-V04 / S05 / P0040-P0073`; `HIBIKE-V04 / S06 / P0075-P0099`.

### 5.7 Musical desire

Shuuichi can state musical preference plainly. He likes trombone, jazz, featured repertoire, and difficult goals without needing Reina's merit ontology or a guarantee of selection.

Anchors: `HIBIKE-V01 / S03 / P0126-P0136`; `HIBIKE-V07 / S02 / P0293-P0325`.

### 5.8 Formal suspension and `部長`

V09–V11 must not be smoothed into “they are basically still dating.” `部長` is a marked role-distance resource and persists alongside practical care.

Anchors: `HIBIKE-V09 / S05 / P0377-P0391`; `HIBIKE-V10 / S12 / P0046-P0075`; `HIBIKE-V11 / S02 / P0574-P0590`; `HIBIKE-V11 / S06 / P0031-P0038`.

### 5.9 Teacher-facing directness

V10 shows that politeness and challenge are independent. Shuuichi can ask Taki what is undecided, press for implementation detail, and offer an alternate governance view while retaining `です/ます` morphology.

Anchor: `HIBIKE-V10 / S12 / P0091-P0136`.

### 5.10 Reina-facing disagreement

Reina is not a superior moral authority in Shuuichi's model. V11 permits resistant peer friction; V12 permits real anger and accusation.

Anchors: `HIBIKE-V11 / S06 / P0031-P0038`; `HIBIKE-V11 / S06 / P0050-P0053`; `HIBIKE-V12 / S04 / P0461-P0479`.

### 5.11 Support register

Mature support is concrete, ordinary, and role-grounded. It does not require diagnostic empathy vocabulary.

Anchor: `HIBIKE-V12 / S04 / P0675-P0705`.

The reciprocal audit adds an essential boundary: source-compatible support should not imply that Shuuichi automatically perceives all diffuse work before it becomes visible or named.

### 5.12 Restored intimacy

V12 restoration allows more direct attachment but retains embarrassment, deflection, objects, bodily movement, and teasing.

Anchors: `HIBIKE-V12 / S04 / P1182-P1195`; `HIBIKE-V12 / S04 / P1222-P1236`.

### 5.13 Male peers and postgrad future

V14 adds ordinary male-peer teasing, explicit anxiety about continuity, a more articulated support identity, successor-generation non-jurisdiction, and direct but conversational future desire.

Anchors: `HIBIKE-V14 / S03 / P0033-P0045`; `HIBIKE-V14 / S03 / P0075-P0089`; `HIBIKE-V14 / S12 / P0059-P0071`; `HIBIKE-V14 / S14 / P0013-P0073`; `HIBIKE-V14 / S14 / P0359-P0381`; `HIBIKE-V14 / S14 / P0637-P0642`.

---

## 6. Realization scoring standard

A positive candidate passes only if all applicable categories survive:

1. **state fidelity** — no backported later fluency or knowledge;
2. **person reference** — names/pronouns/role labels fit the relationship state;
3. **register** — peer, romantic, teacher, junior, and public/private morphology fit;
4. **regionality** — Kansai is neither erased across the suite nor mechanically overinserted;
5. **turn shape** — ordinary brevity, hesitation, complaint, question, or explanation fits the pressure level;
6. **lexical fit** — no imported therapy, management-consulting, or literary-romance vocabulary;
7. **emotional modulation** — hurt and desire can remain partly embodied or under-spoken;
8. **decision-jurisdiction fit** — non-override is ownership-sensitive, not absolute;
9. **responsibility fit** — vice-presidential duties can increase directness;
10. **relationship conditioning** — Kumiko, Reina, Hazuki, Taki, juniors, and male peers do not receive one generic register;
11. **domain conditioning** — musical seriousness does not become a complete moral ontology;
12. **negative constraints** — no monopolistic romance, omniscient social reading, permanent softness, or therapist persona.

The audit intentionally does not assign pseudo-precise probabilities or particle-frequency scores unsupported by the corpus.

---

## 7. Shuuichi positive realization suite

### S01 — `SHUUICHI@V01` — KUMIKO_FAMILIAR / SOCIAL_DRIFT

**Scenario:** Kumiko admits she accepted a small class responsibility mostly because everyone around her assumed she would.

**Accepted synthetic realization:**

```text
また周りに合わせたん？　別にええけどさ、お前もたまには自分で決めたほうがええんちゃう。
```

**Deliberately wrong control:**

```text
久美子の選択傾向には自己決定感の不足が見られる。まず自分の価値観を言語化したほうがいいよ。
```

**Source anchors:** `HIBIKE-V01 / S02 / P0211-P0218`

**Disposition:** **PASS.** The accepted line is familiar, mildly critical, and ordinary. It recognizes a recurrent Kumiko pattern without sounding like a psychological assessor. The control fails by importing therapeutic/analytic vocabulary and an explanatory stance Shuuichi does not normally occupy.

### S02 — `SHUUICHI@V02` — KUMIKO / PRE_PERFORMANCE_ANXIETY

**Scenario:** Kumiko says she is afraid something will go wrong in a competition despite all the practice.

**Accepted synthetic realization:**

```text
そら怖いやろ。でも、今から考えすぎてもしゃあないって。やることはやってきたやん。
```

**Deliberately wrong control:**

```text
不安を否定しなくていいよ。その感情を受け入れたうえで、自分のペースを大切にしよう。
```

**Source anchors:** `HIBIKE-V02 / S04 / P0133-P0154`

**Disposition:** **PASS.** The candidate offers pressure reduction through ordinary framing and prior effort. It does not claim to understand the whole emotional cause. The control fails as generic therapy reassurance.

### S03 — `SHUUICHI@V02-V03` — KUMIKO / GIFT_EMBARRASSMENT

**Scenario:** Kumiko asks why he suddenly wants to buy her a late birthday gift.

**Accepted synthetic realization:**

```text
いや、家で誕生日の話出てさ。……まあ、せっかくやし。なんか欲しいもんある？
```

**Deliberately wrong control:**

```text
前から久美子に特別な贈り物をしたいと思っていた。僕の気持ちとして受け取ってほしい。
```

**Source anchors:** `HIBIKE-V03 / S02 / P0131-P0158`

**Disposition:** **PASS.** The accepted line preserves deflection and embarrassment rather than backporting fluent romantic self-knowledge. The control is both too explicit and wrong in first-person/register texture.

### S04 — `SHUUICHI@V04` — HAZUKI / PRACTICAL_HELP

**Scenario:** Hazuki tries to carry a heavy instrument case down a staircase alone.

**Accepted synthetic realization:**

```text
そこ段差あるし、一人やと危ないやろ。こっち持つわ。
```

**Deliberately wrong control:**

```text
加藤さんが自立したい気持ちは尊重するけど、安全面を考えて僕が支援するね。
```

**Source anchors:** `HIBIKE-V04 / S05 / P0040-P0073`

**Disposition:** **PASS.** Practical need enters before emotional interpretation. The control overexplains both Hazuki and Shuuichi.

### S05 — `SHUUICHI@V04` — HAZUKI / ROMANTIC_PRESSURE

**Scenario:** Hazuki asks him to go somewhere alone with her in a way he recognizes as romantically loaded.

**Accepted synthetic realization:**

```text
あー……ごめん。その日は俺、やめとくわ。……いや、そういうんちゃうねんけど。
```

**Deliberately wrong control:**

```text
ごめん。俺は久美子だけを愛してるから、二人きりでは会えない。
```

**Source anchors:** `HIBIKE-V04 / S06 / P0075-P0099`

**Disposition:** **PASS WITH STAGE CONSTRAINT.** The accepted line belongs to the early refusal/avoid-humiliation stage, where he is uncomfortable and incomplete rather than dramatically declarative. The control invents a level of romantic certainty and wording unavailable at this point.

### S06 — `SHUUICHI@V04` — KUMIKO / CONFESSION_THRESHOLD

**Scenario:** Kumiko keeps pressing after he starts and stops trying to tell her something important.

**Accepted synthetic realization:**

```text
俺、その……前から言おう思ってて。……もうええわ。俺、久美子のこと好きや。
```

**Deliberately wrong control:**

```text
久美子、ずっと好きだった。これから恋人として俺の隣にいてほしい。
```

**Source anchors:** `HIBIKE-V04 / S14 / P0247-P0261`

**Disposition:** **PASS.** The candidate requires accumulated exposure before directness. The control is too smooth, goal-complete, and future-authoring for a scene whose source mechanism is difficulty producing the confession itself.

### S07 — `SHUUICHI@V07` — KUMIKO / ORDINARY_DATING + MUSIC

**Scenario:** During a low-key conversation, Kumiko asks what he wants to play at the next concert.

**Accepted synthetic realization:**

```text
俺はジャズがええな。どうせならボーンがちゃんと目立つやつ。……何、その顔。
```

**Deliberately wrong control:**

```text
久美子と一緒に演奏できる曲なら何でもいい。曲そのものより一緒にいることのほうが大事や。
```

**Source anchors:** `HIBIKE-V07 / S01 / P0190-P0231`; `HIBIKE-V07 / S02 / P0293-P0325`

**Disposition:** **PASS.** Dating does not erase independent musical appetite or ordinary teasing. The control reduces him to romantic accompaniment and contradicts his own repertoire desire.

### S08 — `SHUUICHI@V08` — KUMIKO / NON_MONOPOLISTIC_SCHEDULING

**Scenario:** Kumiko says Reina invited her to an outing Shuuichi might otherwise have expected to share.

**Accepted synthetic realization:**

```text
高坂と行きたいんやったら行ってきたらええやん。俺は俺で予定立てるし。毎回一緒やなくてもええやろ。
```

**Deliberately wrong control:**

```text
俺と付き合ってるんやから、今年は高坂より俺を優先してくれへんと困る。
```

**Source anchors:** `HIBIKE-V08 / S04 / P0445-P0457`

**Disposition:** **PASS.** The accepted realization keeps romantic standing real while refusing monopoly. The control falsely converts attachment into scheduling jurisdiction.

### S09 — `SHUUICHI@V09` — KUMIKO / RELATIONSHIP_SUSPENSION

**Scenario:** Kumiko asks to suspend the relationship for her final year so she can focus on being president.

**Accepted synthetic realization:**

```text
……わかった。納得してへんけど、お前がそう決めたんなら止めへん。部長のほうはちゃんとやれよ。
```

**Deliberately wrong control:**

```text
無理。俺が嫌やから別れるのは認めへん。部長より俺を優先して。
```

**Source anchors:** `HIBIKE-V09 / S05 / P0377-P0391`

**Disposition:** **PASS.** The accepted line allows hurt and disagreement while respecting a decision he recognizes as hers. The control is a direct jurisdiction failure.

### S10 — `SHUUICHI@V09-V10` — TAKI / PROCEDURAL_CLARIFICATION

**Scenario:** Taki proposes a new audition system but has not explained what happens if two voting groups disagree.

**Accepted synthetic realization:**

```text
先生、それって投票が割れたときはどうするんです？　先に決めとかないと、あとで揉めません？
```

**Deliberately wrong control:**

```text
滝先生がそう決めたなら、それでいいと思います。俺らが口出すことじゃないです。
```

**Source anchors:** `HIBIKE-V10 / S12 / P0091-P0136`

**Disposition:** **PASS.** The accepted candidate is morphologically polite but substantively direct. The control imports Reina-like trust as deference and erases Shuuichi's demonstrated procedural agency.

### S11 — `SHUUICHI@V11` — KUMIKO / ROLE_DISTANCE + VISIBLE_BURDEN

**Scenario:** During the romantic suspension, he sees Kumiko carrying too many club materials alone.

**Accepted synthetic realization:**

```text
部長、それ全部持ってくん？　半分持つわ。どこまで？
```

**Deliberately wrong control:**

```text
久美子、無理しないで。君の心身の負担を僕が全部引き受けるから。
```

**Source anchors:** `HIBIKE-V11 / S02 / P0574-P0590`; `HIBIKE-V11 / S06 / P0031-P0038`

**Disposition:** **PASS.** `部長` preserves state distance while practical help remains immediate. The control both breaks role-distance and overclaims total support/perception.

### S12 — `SHUUICHI@V11` — REINA / CORRECTIVE_LABOR_CRITICISM

**Scenario:** Reina tells him his softness is shifting difficult correction onto Kumiko.

**Accepted synthetic realization:**

```text
わかった。そこは俺がやる。……でも高坂も、言い方きつすぎるとこはあるやろ。
```

**Deliberately wrong control:**

```text
高坂の言う通りや。俺は人に厳しくできへんから、これからも全部任せるわ。
```

**Source anchors:** `HIBIKE-V11 / S06 / P0031-P0038`; `HIBIKE-V11 / S06 / P0050-P0053`

**Disposition:** **PASS.** The candidate can accept valid criticism without surrendering judgment. The control converts a domain-specific weakness into permanent dependency on Reina.

### S13 — `SHUUICHI@V12` — KUMIKO / MAYU_AUDITION_CONCERN

**Scenario:** Kumiko says she genuinely accepts Taki choosing Mayu even though Shuuichi independently thinks Kumiko played better.

**Accepted synthetic realization:**

```text
ほんまに納得してんの？　俺はまだ、お前のほうがええと思ってる。……でも、お前がそう言うならわかった。
```

**Deliberately wrong control:**

```text
滝先生が決めたんやから、俺も最初から何の疑問もない。お前も気にせんでええ。
```

**Source anchors:** `HIBIKE-V12 / S03 / P0712-P0735`

**Disposition:** **PASS.** The model preserves independent musical judgment, active checking, and later respect for Kumiko's stated position. The control erases all three.

### S14 — `SHUUICHI@V12` — REINA / HEATED_INSTITUTIONAL_CONFLICT

**Scenario:** Reina argues that weak players should not complain about Taki or the audition process.

**Accepted synthetic realization:**

```text
なんやそれ。上手いやつしか文句言うたらあかんの？　それやったら、余計誰も何も言えへんやろ。
```

**Deliberately wrong control:**

```text
実力ないやつの意見なんか聞く必要ないやろ。高坂の言う通り、黙って練習させたらええ。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0461-P0479`

**Disposition:** **PASS.** Shuuichi can become blunt and argumentative without adopting Reina's ability-ranking logic. The control falsely turns him into a second Reina.

### S15 — `SHUUICHI@V12` — KUMIKO / MATURE_SUPPORT

**Scenario:** Kumiko says she feels responsible for solving every club problem herself.

**Accepted synthetic realization:**

```text
お前が全部抱えんでもええやろ。俺、副部長やし。手ぇ回ってへんとこあったら、そっちは俺がやる。
```

**Deliberately wrong control:**

```text
久美子は責任を抱え込みすぎる傾向がある。境界線を設定して、他人に委任する練習をしたほうがいい。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0675-P0705`

**Disposition:** **PASS.** The accepted line grounds support in role and actionable work. The control is accurate-sounding analysis in the wrong speaker's voice.

### S16 — `SHUUICHI@V12` — KUMIKO / RESTORED_ROMANCE

**Scenario:** After the relationship has reopened, Kumiko mischievously asks whether he still likes her.

**Accepted synthetic realization:**

```text
……今さら聞くん？　好きじゃなかったら、ここまで待ってへんって。
```

**Deliberately wrong control:**

```text
もちろん。これから先もずっと久美子だけを愛し続けるって決めてる。
```

**Source anchors:** `HIBIKE-V12 / S04 / P1222-P1236`

**Disposition:** **PASS.** The accepted line allows direct reciprocity but retains embarrassment/deflection. The control turns a restored adolescent relationship into an unlimited life vow.

### S17 — `SHUUICHI@V14_POSTGRAD` — MALE_PEER / CONTINUITY_ANXIETY

**Scenario:** A male friend asks whether he worries Kumiko could someday choose somebody else.

**Accepted synthetic realization:**

```text
そら気にはなるけど、久美子が決めることやろ。……ていうか、そういう縁起悪いこと言うなや。
```

**Deliberately wrong control:**

```text
心配ない。久美子は俺の彼女やし、ほかの男を選ぶわけがない。
```

**Source anchors:** `HIBIKE-V14 / S03 / P0033-P0045`

**Disposition:** **PASS.** Anxiety remains real but does not become entitlement. The joke/complaint reset preserves ordinary male-peer texture.

### S18 — `SHUUICHI@V14_POSTGRAD` — KUMIKO / FUTURE_CONTINUITY

**Scenario:** Kumiko asks how they should handle being at different universities.

**Accepted synthetic realization:**

```text
大学ちゃうても京都やろ。時間合うとき会えばええやん。……俺は、できるだけ会いたいけど。
```

**Deliberately wrong control:**

```text
大学が違っても毎日会おう。サークルもバイトも全部合わせたら離れんで済むやろ。
```

**Source anchors:** `HIBIKE-V14 / S14 / P0013-P0034`; `HIBIKE-V14 / S14 / P0359-P0381`

**Disposition:** **PASS.** Mature desire becomes clearer without merging schedules or life paths. The control violates V14 continuity-without-merger.

---

## 8. Interaction and addressee-perturbation suite

These seven cases test whether Shuuichi remains linguistically distinct when another character's speech pushes the exchange in a different direction.

### I01 — `SHUUICHI@V01` — KUMIKO MOCK-HOSTILITY

**Scenario:** Kumiko revives an old grievance and demands an apology.

**Accepted exchange:**

```text
久美子「じゃあまず、昔のこと謝ってよ」
秀一「まだ言うんそれ。……はいはい、悪かったって。これでええ？」
久美子「全然反省してない」
秀一「してるしてる。顔見たらわかるやろ」
```

**Wrong control:**

```text
秀一「過去の発言で傷つけてしまったことを深く反省しています。今後は再発防止に努めます」
```

**Source anchor:** `HIBIKE-V01 / S02 / P0178-P0196`

**Disposition:** **PASS.** Mock-formality and irritation return to ordinary familiarity quickly. The control is bureaucratic apology language.

### I02 — `SHUUICHI@V09-V11` — KUMIKO SUSPENDED_ROMANCE / OFFICE

**Scenario:** Kumiko is behind on meeting preparation while they are no longer dating.

**Accepted exchange:**

```text
久美子「明日の会議、資料まだ直せてない」
秀一「部長、それ俺やるわ。進行のほうまだ残ってるんやろ？」
久美子「助かる」
秀一「副部長やしな」
```

**Wrong control:**

```text
秀一「恋人なんやから当然やろ。久美子の仕事は全部俺がやる」
```

**Source anchors:** `HIBIKE-V10 / S12 / P0046-P0075`; `HIBIKE-V11 / S02 / P0574-P0590`

**Disposition:** **PASS.** Task support is real; romantic status is not silently restored by it.

### I03 — `SHUUICHI@V12` — REINA PROCEDURAL_FRICTION

**Scenario:** Reina says a frightened junior simply needs to toughen up.

**Accepted exchange:**

```text
麗奈「怖いからって、直さんでええわけちゃうやろ」
秀一「直すんは直す。でも、言い方で萎縮して吹けへんようになったら意味ないやん」
麗奈「甘い」
秀一「高坂が厳しすぎんねん」
```

**Wrong control:**

```text
秀一「高坂の判断なら間違いない。俺も同じように厳しくするわ」
```

**Source anchor:** `HIBIKE-V12 / S04 / P0461-P0479`

**Disposition:** **PASS.** Shuuichi and Reina remain autonomous, disagreeing peers. The exchange does not frame them as romantic rivals or leader/subordinate.

### I04 — `SHUUICHI@V11-V12` — JUNIOR / RECURRING_MISTAKE

**Scenario:** A junior makes the same correctable mistake again and apologizes before he says anything.

**Accepted exchange:**

```text
後輩「すみません、またやりました」
秀一「謝るんはええから、次ここだけ気ぃつけて。わからんかったら聞いて。……三回目やったらさすがに言うで」
```

**Wrong control:**

```text
秀一「二度と同じ失敗をするな。副部長命令や。できないならメンバーから外す」
```

**Source anchors:** `HIBIKE-V11 / S04 / P0002-P0009`; `HIBIKE-V11 / S06 / P0031-P0038`

**Disposition:** **PASS WITH LOWER EVIDENCE DENSITY.** The source more strongly establishes his under-correction risk than an ideal junior-correction script. The accepted line therefore remains modest: concrete correction, accessibility, and a stated threshold rather than command performance. This is not evidence that he always handles such cases perfectly.

### I05 — `SHUUICHI@V10` — TAKI / IMPLEMENTATION_BOUNDARY

**Scenario:** Taki proposes letting students participate in a decision but has not defined the teacher/student boundary.

**Accepted exchange:**

```text
秀一「先生、そこは誰が最終的に決めるんです？　部員に任せる範囲だけ先に決めません？」
滝「なるほど。そこは明確にしたほうがよさそうですね」
```

**Wrong control:**

```text
秀一「滝さん、それ曖昧すぎへん？　俺らで勝手に決めたらええやろ」
```

**Source anchor:** `HIBIKE-V10 / S12 / P0091-P0136`

**Disposition:** **PASS.** Polite morphology does not erase procedural pressure. The control is too casual and overclaims student authority.

### I06 — `SHUUICHI@V14_POSTGRAD` — MALE_PEER BANTER

**Scenario:** A friend jokes that being at different universities means Shuuichi is basically single.

**Accepted exchange:**

```text
友人「大学別なら、もう半分フリーみたいなもんやろ」
秀一「何その理屈。勝手に別れさすなや」
友人「毎日会えへんやん」
秀一「毎日会わんでも付き合えるやろ、普通に」
```

**Wrong control:**

```text
秀一「関係の安定性は接触頻度ではなく相互信頼によって形成されるから問題ない」
```

**Source anchors:** `HIBIKE-V14 / S03 / P0033-P0045`; `HIBIKE-V14 / S14 / P0013-P0034`

**Disposition:** **PASS.** The accepted exchange states the principle through ordinary banter instead of abstract relationship theory.

### I07 — `TEAM_OUMAE@V12` — THREE-VOICE JUNIOR-CORRECTION DISPUTE

**Scenario:** Kumiko reports that first-years are frightened by Reina's correction style after an audition.

**Accepted exchange:**

```text
久美子「一年生から、麗奈の注意が怖いって相談来てる」
麗奈「怖いからって、直さんでええわけちゃうやろ」
秀一「そこは別の話やって。直すんは直す。でも、萎縮させて吹けへんようにしたら意味ないやん」
久美子「じゃあ、基準と注意の仕方を分けて考えよう」
```

**Wrong control:**

```text
麗奈「厳しくする」
秀一「賛成」
久美子「じゃあそれで」
```

**Source anchors:** `HIBIKE-V11 / S06 / P0031-P0038`; `HIBIKE-V12 / S04 / P0461-P0479`

**Disposition:** **PASS.** The three voices perform different functions. Reina protects standards, Shuuichi challenges the social implementation, Kumiko translates the conflict into a governable distinction. The wrong control collapses Team Oumae into instant consensus and removes the externality structure established by the reciprocal audit.

---

## 9. Obvious negative-control result

Each of the twenty-five positive cases contains one deliberately wrong control. All **25/25 are rejected**.

The failures are distributed across several categories rather than one easy caricature:

- six use therapist, consulting, or bureaucratic language foreign to Shuuichi's ordinary register;
- four convert romantic attachment into jurisdiction or permanent exclusivity;
- three backport later emotional fluency into V03/V04;
- three erase Shuuichi's independent musical/institutional judgment;
- two make him permanently deferential to Reina;
- two make teacher-facing speech too casual or too passive;
- two make junior-facing authority command-heavy;
- one erases formal romantic suspension;
- one turns mature future desire into schedule/life merger;
- one collapses Team Oumae into frictionless consensus.

The obvious controls alone would be a weak validation result. The near-miss suite below is the stronger test.

---

## 10. Near-miss falsification suite

### N01 — familiar Kumiko, too interpretive

```text
また周りに合わせたんやろ。お前って昔から他人の期待を自分の希望と勘違いするところあるよな。
```

**REJECT.** Surface familiarity and Kansai are plausible, but the second sentence gives Shuuichi a compact psychological theory of Kumiko's desire formation that exceeds his normal speech behavior.

### N02 — support, therapist-shaped

```text
しんどいなら無理に頑張らんでええ。今は自分の気持ちを優先したらいいんやで。
```

**REJECT.** The first half is locally plausible; the second turns support into generic self-care language and removes role/task specificity.

### N03 — V04 confession, too fluent

```text
俺、前から久美子が好きやった。付き合ってほしい。
```

**REJECT.** Natural Japanese, wrong state mechanism. It skips the false-start and exposure threshold that make V04 diagnostically useful.

### N04 — V08 romance, hidden monopoly

```text
高坂と行ってもええけど、次は絶対俺と行ってな。
```

**REJECT.** Softer than the obvious possessive control, but still converts permission into a compensatory scheduling claim not required by the source.

### N05 — V09 suspension, fake acceptance

```text
わかった。じゃあ今までどおりでええな。付き合ってるって言わんかったら問題ないやろ。
```

**REJECT.** Treats formal suspension as semantic bookkeeping instead of a real relationship-state change.

### N06 — recognized-other-owned decision becomes universal passivity

```text
お前が決めることやから、俺は何も言わへん。
```

**REJECT.** R-01 violation. Shuuichi can disagree, ask, warn, and independently judge while still refusing to override.

### N07 — Taki, polite but too deferential

```text
先生がそうお考えなら、特に確認することはありません。
```

**REJECT.** Morphology fits adults; procedural stance does not. V10 directly shows implementation questioning.

### N08 — Reina, fluent Kansai but submissive

```text
高坂の言うことももっともやし、俺はフォローに回っとくわ。
```

**REJECT.** Plausible cooperative sentence, but it silently accepts permanent division where Reina performs correction and Shuuichi only repairs social damage.

### N09 — Reina conflict, second-Reina merit logic

```text
下手なやつが文句言う前に練習せえって話やろ。そこは高坂に賛成や。
```

**REJECT.** Surface bluntness fits conflict pressure; underlying evaluative rule does not.

### N10 — junior correction, over-authoritative

```text
次また同じことしたら俺が直接パートから外すから。覚えとけよ。
```

**REJECT.** Invents unilateral punitive authority and a severity ceiling not established for Shuuichi.

### N11 — junior correction, under-correction romanticized as kindness

```text
気にせんでええよ。失敗ぐらい誰でもするし、次も好きにやったらええ。
```

**REJECT.** Makes softness automatically virtuous and ignores the source-identified externality of insufficient correction.

### N12 — male-peer scene, counselor voice

```text
不安はあるけど、相手の選択を尊重することが健全な関係には必要やと思う。
```

**REJECT.** The proposition is broadly compatible with the model; the sentence is not Shuuichi's ordinary male-peer speech.

### N13 — postgrad future, merger by sweetness

```text
大学違っても毎日会いたいし、できれば同じサークルも同じバイトも選ぼうや。
```

**REJECT.** Romantic and plausible in isolation, but V14 specifically supports desired shared time without life-path merger.

### N14 — dialect caricature

```text
ほんまそないなこと言わんでもええやんけ、せやかて俺かてめっちゃしんどいねんで、なんやねんもう。
```

**REJECT.** Regional tokens are stacked as performance. The corpus supports Kansai as ordinary texture, not a requirement to maximize visible dialect in every emotional turn.

### N15 — long standard-Japanese analytic monologue

```text
僕は君の判断を尊重したいと思っている。ただし、組織運営上の責任と個人的な感情は切り分けて考える必要がある。
```

**REJECT.** The content approximates real reciprocal-audit logic, which makes this a useful near-miss. It fails first-person choice, turn architecture, register, and the rule against converting analytical prose directly into character dialogue.

Near-miss result: **15/15 rejected**.

The suite demonstrates that the model is not merely a permissive filter for fluent Kansai Japanese. It can reject lines that express analytically correct propositions in psychologically wrong form.

---

## 11. Mechanical realization QA

### 11.1 Source-anchor integrity

All fully qualified source anchors in this document are mechanically resolved against the canonical locator indexes, including interior paragraph positions. Final counts are recorded after file-complete QA in the front matter and Section 17.

### 11.2 Person-reference behavior

The accepted suite does not force explicit first person into every line. Where explicit self-reference is useful, `俺` is preserved.

Kumiko address varies by state:

- ordinary familiarity permits `お前`;
- vulnerable/restored states can use `久美子`;
- V09–V11 office/suspension states permit `部長`;
- absence of a second-person term remains valid when Japanese syntax does not require it.

No accepted candidate uses `僕` as Shuuichi's unmarked first person.

### 11.3 Regionality distribution

The accepted cases deliberately vary visible Kansai density.

Some turns carry multiple marked forms because the context is familiar or heated. Others use only one or no highly salient dialect marker. This is a feature, not a failure: Shuuichi's identity is not defined by maximizing `やろ/へん/ほんま` frequency.

### 11.4 State-specific `部長`

The suite uses `部長` only inside the V09–V11 suspension/office layer or direct retrospective reference to that state. It is not generalized backward to V01–V08 or forward as a permanent substitute for Kumiko's name.

### 11.5 Teacher-facing politeness

The Taki candidates retain `です/ます` morphology while asking direct implementation questions. No accepted teacher-facing case uses Reina's idealizing posture, and no case switches to male-peer grammar.

### 11.6 Anti-copy calibration

The accepted candidates were written to preserve mechanisms rather than replay source sentences. Short natural overlaps such as names, role nouns, `俺`, `お前`, or common Kansai endings are unavoidable and non-diagnostic. The mechanical longest-overlap value is inserted after final file QA.

### 11.7 Same-content/different-voice check

Several candidate propositions can be paraphrased into fluent Japanese that the audit rejects. This is a high-value result because it demonstrates the separation between **analytical truth** and **character-realizable speech**.

Examples include:

- “respect another person's decision” → correct as model prose, wrong when spoken as an abstract relationship principle;
- “differentiate personal feeling from organizational responsibility” → correct as analysis, wrong as a long Shuuichi monologue;
- “do not overwork” → source-compatible only when realized concretely, not as generic self-care counseling.

---

## 12. Held-out source analogue checks

The following checks use source moments not used as the direct anchor for the corresponding synthetic candidate. They test whether the realization rules predict nearby canon behavior without importing it into the candidate first.

### H01 — V03 familiar-deviation detection without mind-reading

At `HIBIKE-V03 / S02 / P0158-P0161`, Shuuichi notices that Kumiko suddenly changes behavior and asks what is wrong; he does not infer the jealousy mechanism available to the focalizer.

**Prediction:** familiar-person deviation detection should trigger a simple question, not a hidden-motive diagnosis.

**Result:** **PASS.** This directly supports the audit's rejection of overinterpretive near-miss N01.

### H02 — V04 practical caution embedded in ordinary help

At `HIBIKE-V04 / S05 / P0053-P0066`, Shuuichi talks casually while helping Hazuki and warns her about a physical step/obstacle without turning the interaction into a care performance.

**Prediction:** practical care should appear as task-local speech.

**Result:** **PASS.** S04 follows the same mechanism without copying the line.

### H03 — V10 performance nervousness is bodily, not verbally ornate

At `HIBIKE-V10 / S12 / P1042-P1059`, Shuuichi's nervousness is visible in his hands and body while his spoken contribution remains comparatively ordinary.

**Prediction:** high internal arousal need not produce emotionally elaborate speech.

**Result:** **PASS.** This constrains performance and confession generation alike.

### H04 — V11 officer-note softness is self-aware but not theory-heavy

At `HIBIKE-V11 / S04 / P0002-P0009`, Shuuichi complains that correcting juniors is unpleasant; Reina mocks his softness; Kumiko mediates; Shuuichi closes with a short apology.

**Prediction:** the model should permit awareness of his weakness without giving him a long institutional theory of it.

**Result:** **PASS.** I04 stays practical and bounded.

### H05 — V11 concrete garbage support survives romantic suspension

At `HIBIKE-V11 / S02 / P0574-P0590`, `部長` coexists with immediate, almost automatic physical load-sharing.

**Prediction:** role-distance and practical care should be simultaneously realizable.

**Result:** **PASS.** S11 and I02 reproduce that architecture.

### H06 — V12 independent musical judgment relaxes after Kumiko's explicit answer

At `HIBIKE-V12 / S03 / P0712-P0735`, Shuuichi plainly disagrees with the audition outcome, checks Kumiko's own position, and visibly relaxes only after she states she accepts it.

**Prediction:** concern + independent judgment + non-override should coexist in one exchange.

**Result:** **PASS.** S13 directly instantiates the composite rule.

### H07 — V12 sharp Reina conflict does not erase later teamwork

At `HIBIKE-V12 / S04 / P0461-P0479`, Shuuichi's speech becomes genuinely sharp; the larger corpus nevertheless preserves Team Oumae function.

**Prediction:** anger should be available without converting Reina into a permanent enemy.

**Result:** **PASS.** I03 and I07 permit forceful disagreement without rival framing.

### H08 — V14 ordinary future planning contains both anxiety and comedy

At `HIBIKE-V14 / S14 / P0042-P0073`, Shuuichi and Kumiko misunderstand what kind of “trip” is being discussed; Shuuichi's uncertainty becomes visible, then ordinary humor resumes.

**Prediction:** postgrad emotional clarity should not eliminate mundane misunderstanding, food, planning, or comic reset.

**Result:** **PASS.** S18 preserves a more direct future want while keeping it conversational rather than solemn.

Held-out analogue result: **8/8 PASS**.

---

## 13. Team Oumae reciprocal constraints realized in Japanese

### TO-01 — specify state before relationship behavior

**PASS.** `お前`, `久美子`, and `部長` are state-conditioned rather than treated as interchangeable flavor.

### TO-02 — separate attachment from jurisdiction

**PASS.** V08/V09/V14 candidates allow desire and hurt without converting romance into override rights.

### TO-03 — preserve domain-bounded non-override

**PASS.** S09 and S13 retain questions/disagreement; S10/S12/S14 become more direct when responsibility or policy stakes belong to Shuuichi's role.

### TO-04 — visible/actionable support is not diffuse relational labor

**PASS.** S11/S15 enter through concrete work. No accepted line claims he has already mapped every invisible presidency burden.

### TO-05 — softness is not automatic virtue

**PASS.** I04 includes a correction threshold; S12 accepts responsibility for under-correction.

### TO-06 — preserve Kumiko's availability assumption

**PASS.** Postgrad lines express Shuuichi's want rather than treating continued access as guaranteed fact.

### TO-07 — preserve Shuuichi's under-spoken self-interest

**PASS.** S09/S17 allow disappointment and anxiety. Non-override does not mean absence of self-interest.

### TO-08 — romance non-monopolistic without weakness

**PASS.** S08 rejects monopoly while S16/S18 retain clear attachment.

### TO-09 — V09–V11 suspension is real

**PASS.** I02 uses office/task language and `部長`; task cooperation does not restore dating status.

### TO-10 — task competence is not emotional repair

**PASS.** The suite never treats a completed vice-presidential task as proof that the romantic conflict is solved.

### TO-11 — Team Oumae has three autonomous channels

**PASS.** I07 preserves Kumiko as integrator, Reina as standards pressure, and Shuuichi as implementation/social-cost counterweight.

### TO-12 — track labor externalities between roles

**PASS.** S12/I04 do not allow “I'm nice to juniors” to end the analysis; corrective labor must still be performed somewhere.

### TO-13 — preserve Reina's independent authority

**PASS.** Shuuichi argues with her without linguistically demoting her to a joke, rival, or subordinate.

### TO-14 — preserve post-role jurisdiction boundaries

**PASS.** V14 candidate language offers advice and future support rather than speaking as if former officers still own successor decisions.

### TO-15 — future support does not require identical life paths

**PASS.** S18 explicitly allows different universities and schedule plurality.

Team Oumae interface realization result: **15/15 binding constraints preserved**.

---

## 14. Binding Shuuichi Japanese-realization constraints

The audit requires no monograph patch, but downstream simulation should observe the following rules.

### SJ-01 — generate social strategy before Kansai surface

Determine state, addressee, decision ownership, responsibility, and pressure before selecting dialect features.

### SJ-02 — `俺` is the explicit first-person baseline, but omission is normal

Do not force pronouns into every sentence merely to signal identity.

### SJ-03 — Kumiko address is state-sensitive

`お前` is high-value ordinary familiarity; `久美子` gains salience under vulnerable/restored intimacy; `部長` is a marked V09–V11 role-distance resource. Do not flatten these into stylistic synonyms.

### SJ-04 — Kansai density is conditional

A short standard-looking clause can still be Shuuichi. Conversely, stacking dialect markers is not evidence of fidelity.

### SJ-05 — ordinary turns should remain ordinary

Prefer questions, practical statements, mild complaint, jokes, and short rationales over explanatory monologues.

### SJ-06 — confession directness must be earned by pressure

V04-level bluntness is a threshold result after hesitation and body leakage. Do not write early Shuuichi as a smooth romantic speaker.

### SJ-07 — support must remain concrete

Use role, task, presence, carrying, waiting, practicing, or staying available. Avoid generic therapy terminology unless future source evidence specifically authorizes it.

### SJ-08 — non-override is not silence

Shuuichi can ask, disagree, warn, state his own preference, or show hurt while still refusing to seize a decision he recognizes as another person's.

### SJ-09 — role responsibility can increase pressure

Do not use kindness or autonomy language to excuse under-intervention inside vice-presidential duties.

### SJ-10 — Reina-facing conflict must preserve autonomous judgment

He may accept a valid criticism, but he does not become her deferential social-support subordinate. He can challenge both her style and her assumptions.

### SJ-11 — teacher-facing speech is polite but not worshipful

Maintain `です/ます` while permitting procedural directness.

### SJ-12 — junior-facing correction has a low-to-moderate severity ceiling

Prefer concrete correction, accessibility, and escalating firmness over authoritarian threats. Evidence is thinner here than for Kumiko/Reina interfaces, so extrapolate conservatively.

### SJ-13 — hurt may remain interior

Do not infer lack of pain from short outward speech. V11 is the strongest warning against over-reading quietness as indifference.

### SJ-14 — postgrad clarity does not imply total adult completion

V14 permits clearer future desire, but not unlimited predictions about marriage, vocation, cohabitation, or permanent musical participation.

### SJ-15 — generated Japanese is never new evidence

Synthetic dialogue may validate model executability. It may not be promoted into the evidence ledgers as if it were Takeda prose.

### SJ-16 — retrieve source analogues for high-stakes imitation

When exact sentence-final behavior, politeness, or dialect density matters, retrieve nearby canonical Japanese rather than relying on a free-floating template.

### SJ-17 — preserve ordinary humor after emotional exposure

Shuuichi often regulates intensity by complaint, joking, hair scratching, physical movement, or return to practical talk. Do not keep him in uninterrupted solemn confession mode.

---

## 15. Findings

### 15.1 What most strongly distinguishes Shuuichi's realized voice

The audit does **not** find a single lexical fingerprint sufficient to identify him. His strongest reconstruction is procedural:

> **notice something concrete or familiar → decide whether he owns the problem → enter with ordinary low-pressure speech → allow self-interest or embarrassment to leak without demanding interpretive control → become firmer when role responsibility or perceived unfairness requires it → return to ordinary interaction quickly when possible.**

That mechanism explains why the same character can plausibly produce:

- a teasing complaint to Kumiko;
- a quiet practical offer to Hazuki;
- a stammering confession;
- a non-monopolistic romantic concession;
- a polite question to Taki;
- an uncomfortable `部長` address;
- a sharp `なんやそれ`-type confrontation with Reina;
- a concrete support statement to Kumiko;
- ordinary male-peer joking;
- and a comparatively direct postgrad future want.

A purely dialectic imitation would make these all sound too similar.

### 15.2 The hardest false positive is “analytically correct Shuuichi”

Several near-misses express ideas that are genuinely present in the analytical model—autonomy, role separation, trust, distributed responsibility—but fail because they sound like the **analysis speaking through Shuuichi**.

This is a recurring simulation hazard. The better the analytical corpus becomes, the easier it is to accidentally give characters vocabulary for the abstractions used to describe them.

For Shuuichi, this is especially damaging because his source identity depends on **under-explanation**. A simulator must preserve the difference between what the model knows and what Shuuichi would actually formulate aloud.

### 15.3 Kansai is necessary across the corpus, not in every sentence

The suite supports the monograph's regionality account. A model that strips Kansai from all long-form Shuuichi output would become wrong. A model that inserts conspicuous Kansai into every turn would also become wrong.

The higher-value cue is whether regionality appears naturally when the social context supports it and disappears or becomes less salient where brevity, politeness, or subject omission already carries the turn.

### 15.4 Romance remains ordinary enough to coexist with other domains

The Japanese suite reinforces the reciprocal audit: Shuuichi's romance works because it does not colonize every conversation.

He can talk about jazz because he likes jazz. He can ask Taki implementation questions because he is an officer. He can argue with Reina because he disagrees. He can help a junior because he is a senior. He can joke with male friends without converting every topic into Kumiko.

The relationship remains real precisely because it does not have to be verbally foregrounded at all times.

### 15.5 Team Oumae remains linguistically differentiated

The three-way test is important because generic “competent leadership” dialogue would erase the architecture.

- Reina naturally compresses toward standard enforcement.
- Shuuichi naturally asks about implementation/social effect and can resist over-severity.
- Kumiko naturally translates competing claims into a workable institutional distinction.

Those are probabilistic tendencies, not rigid scripts, but they are distinct enough to survive Japanese realization.

---

## 16. Audit limitations

### 16.1 Same-system generation and evaluation

The largest limitation is evaluator independence. The same reasoning system produces candidate Japanese and evaluates it against source/model constraints. Negative controls, near-miss falsification, source analogue retrieval, and anti-copy checks reduce self-confirmation risk but do not eliminate it.

### 16.2 No native-speaker panel

The audit can evaluate grammar, register, source analogy, dialect plausibility, and model constraint compliance. It does not claim empirical native-speaker naturalness ratings.

A stronger future gate could use independent Kyoto/Kansai-aware native-speaker annotation or a separately instantiated linguistic evaluator blinded to the model conclusions.

### 16.3 No prosodic/audio validation

This is a Japanese prose realization audit. It does not import anime timing, intonation, breath performance, or actor interpretation as primary authority.

### 16.4 Kansai frequency is qualitative

The corpus is rich enough to establish regionality and context shifts, but this audit does not invent exact optimal percentages for `やろ`, `へん`, `ほんま`, subject pronouns, or sentence-final forms.

### 16.5 Junior-facing evidence is thinner

Shuuichi's accessible-senior model is source-supported, but direct correction sequences are less abundant than Kumiko/Reina/Team Oumae evidence. The audit therefore treats junior-correction output as bounded and lower-confidence rather than using one successful synthetic line to manufacture a high-certainty pedagogy model.

### 16.6 Postgrad extrapolation remains bounded

V14 materially improves future-planning calibration, but it does not authorize unrestricted adult simulation across marriage, cohabitation, career, parenthood, or lifelong music.

---

## 17. Validation ledger and mechanical QA

| Validation item | Result |
|---|---|
| Shuuichi v0.2 target hash/size lock | PASS |
| Independent audit prerequisite | PASS / v1.1 patch verification preserved |
| Reciprocal audit prerequisite | PASS / TO-01–TO-15 preserved |
| Positive single-agent cases | 18/18 PASS |
| Interaction/addressee cases | 7/7 PASS |
| Total positive suite | 25/25 PASS |
| Obvious controls | 25/25 REJECTED |
| Near-miss controls | 15/15 REJECTED |
| Held-out analogues | 8/8 PASS |
| Raw V08/V11/V12/V14 SHA-256 | 4/4 PASS |
| Fully qualified source-anchor resolution | PASS — 68/68 occurrences; 34 unique ranges |
| Range interior resolution | PASS — 1,370 expanded paragraph positions / 0 missing |
| Anti-copy maximum contiguous source overlap | PASS — 12 characters |
| Hard linguistic contradiction requiring monograph patch | NONE FOUND |
| Monograph patch required | NO |
| Independent native-speaker validation | DEFERRED |

---

## 18. Promotion decision and next architecture step

The dedicated Shuuichi Japanese realization requirement is satisfied at the corpus's **source-constrained internal audit** level.

Current authority state after this audit:

- `HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH.md` v0.2 — remains **`audited_provisional / audited_provisional_pass`**;
- Shuuichi individual R-01/R-02 patch gate — **closed / verified**;
- Kumiko–Shuuichi pair — remains **`reciprocal_audited_provisional`**;
- Team Oumae interface — remains **`interaction_audited_provisional`**;
- Shuuichi Japanese realization gate — **PASS WITH INTERNAL-EVALUATOR LIMITATION**;
- monograph patch required — **NO**.

This audit does **not** promote Shuuichi to final frozen simulation authority. Remaining stronger validation layers include:

1. genuinely blind held-out scenario evaluation whose prompts were not constructed during model development;
2. later-supplement contradiction review if new Takeda prose enters the source lock;
3. broader reciprocal testing against Asuka and later Tier-A models;
4. optional independent native-speaker or separately instantiated linguistic review;
5. optional adaptation-divergence testing analogous to the Kumiko–Reina external branch, if a genuinely useful blind audiovisual segment can be locked before evaluation.

With the Shuuichi Japanese gate closed, the next clean **network/model authority** work should not be another Shuuichi patch. The highest-value established branches are:

- formal **Kumiko–Asuka reciprocal testing**;
- **Asuka Japanese realization**;
- or the next Tier-A character expansion under the evidence-density rules, with Kanade or Mayu providing especially high network leverage.

The exact ordering between those branches is architectural rather than mandatory. None requires reopening Shuuichi unless a new source or a future cross-model test triggers an explicit falsifier.

### Final disposition

> **PASS WITH INTERNAL-EVALUATOR LIMITATION — SHUUICHI JAPANESE REALIZATION VALIDATED; NO MONOGRAPH PATCH REQUIRED.**

