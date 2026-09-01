---
series: HIBIKE
artifact_type: audit
scope: KUMIKO_REINA_JAPANESE_REALIZATION_V0.3
generation: V2
version: '1.0'
status: canonical
audit_targets:
- 04 Character Modeling/HIBIKE_KUMIKO_CHARACTER_MONOGRAPH.md
- 04 Character Modeling/HIBIKE_REINA_CHARACTER_MONOGRAPH.md
- 08 Audits and Manifests/HIBIKE_KUMIKO_REINA_RECIPROCAL_MODEL_AUDIT.md
audit_target_versions:
  kumiko: '0.3'
  reina: '0.3'
  reciprocal_audit: '1.0'
audit_target_drive_ids:
  kumiko: 1vdlAx1D3kX3jikOYHTjiKZZKyu6_7rdj
  reina: 1bpJ0hmVk3y42pEYA9L8-_CL7nLT_UHg9
  reciprocal_audit: 1EW9BqcHp7s--FHd_wnhXReZO0JmU1Mti
audit_target_sha256:
  kumiko: 2e3bada1615c47b6bab1c19f528c861ebb0d436163e7b40811a5bc355b550cea
  reina: bc0e502d16e09e0e1f7060830af5065362801d4b36cb923199c7f667ccd2ba54
  reciprocal_audit: 99d7ce41a0e6391e06e4dedbc03ac7620ac009510bb2e5f17f75c7943e63d6a3
audit_result: pass_with_internal_evaluator_limit_no_model_patch
japanese_realization_gate: pass
pair_authority_state: reciprocal_audited_provisional
monograph_patch_required: false
independent_native_speaker_validation: deferred
source_boundary: Locked Japanese EPUB core HIBIKE-V01 through HIBIKE-V14; canonical locator indexes; V2 voice/register, relationship, behavior, character-state, institutional, and music/pedagogy ledgers; audited Kumiko/Reina v0.3 monographs; formal reciprocal audit
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-08-22'
updated: '2026-08-22'
---

# Sound! Euphonium V2 — Kumiko–Reina Japanese Realization Audit
## Source-constrained synthetic Japanese voice, register, state, and dyadic interaction validation

## 1. Audit purpose and decision

This artifact evaluates whether the two independently audited-provisional character models can be **realized in plausible Japanese** rather than only described correctly in English analytical prose.

The audit targets:

- `HIBIKE_KUMIKO_CHARACTER_MONOGRAPH.md` v0.3;
- `HIBIKE_REINA_CHARACTER_MONOGRAPH.md` v0.3;
- the binding pair-interface constraints established by `HIBIKE_KUMIKO_REINA_RECIPROCAL_MODEL_AUDIT.md` v1.0.

The question is not whether a generated line sounds vaguely like an anime girl from Kyoto. The question is whether controlled Japanese realization preserves the specific source-grounded distinctions that the models claim to encode:

- Kumiko's standard-Japanese baseline and mandatory thought–speech gap;
- Kumiko's addressee-conditioned editing, mock familiarity, public warmth, and crisis directness;
- Reina's `アタシ` self-reference, conditional Kansai richness, compressed performance register, and attachment-domain expansion;
- Reina's ability to remain polite with Taki while still speaking directly;
- the difference between musical certainty and relational uncertainty;
- state-bounded repair language after V12;
- ordinary/play registers that prevent crisis overfitting;
- the pair's twelve reciprocal bridge constraints, especially staged repair, focalization ownership, and separation of musical selection from relationship selection.

### Audit decision

> **PASS WITH INTERNAL-EVALUATOR LIMITATION — JAPANESE REALIZATION GATE PASSED; NO MONOGRAPH PATCH REQUIRED**

The two v0.3 models successfully generate source-compatible Japanese across the tested state, domain, addressee, and pressure conditions. The positive suite passes **30/30**. All **30/30** obvious negative controls are rejected for identifiable reasons, and all **12/12** subtler near-miss controls are also rejected. The test suite therefore demonstrates more than an ability to generate plausible-sounding Japanese: the models can distinguish plausible realizations from lines that are fluent but psychologically, socially, temporally, or register-wise wrong.

No finding requires modification of either character monograph or the reciprocal model audit.

This is nevertheless **not an independent native-speaker validation study**. The same reasoning system that constructs the realization candidates also judges them against the locked prose and model constraints. The audit therefore closes the architecture's dedicated **source-constrained synthetic Japanese realization gate**, while preserving an explicit residual limitation for independent human/native-speaker or separately instantiated linguistic evaluation if final frozen simulation authority is later pursued.

### Compact disposition

| Audit dimension | Result |
|---|---|
| Canonical target lock | PASS |
| Kumiko standard-Japanese baseline | PASS |
| Kumiko thought–speech editing | PASS |
| Kumiko public / private / authority switching | PASS |
| Reina self-reference and conditional Kansai regionality | PASS |
| Reina public-musical / private-attachment domain switching | PASS |
| Taki-directed politeness | PASS |
| Third-party register perturbation | PASS |
| V12 conflict language | PASS |
| V12 repair language without ideological conversion | PASS |
| Post-graduation ordinary/play realization | PASS |
| Positive synthetic cases | PASS — 30/30 |
| Obvious negative controls | PASS — 30/30 rejected |
| Near-miss falsification controls | PASS — 12/12 rejected |
| Source-anchor validity | PASS — 36/36 references resolve |
| Anti-copy realization check | PASS — maximum exact source overlap 12 contiguous characters |
| Kumiko accidental Kansai leakage | PASS — 0/12 single-character cases |
| Pair bridge-constraint compliance | PASS |
| Monograph patch required | NO |
| Independent native-speaker validation | DEFERRED / OPTIONAL STRONGER GATE |
| Final frozen simulation authority | NOT YET |

## 2. What counts as a Japanese realization audit

A literary character model can be psychologically accurate while failing at actual dialogue. Common failure modes include:

1. translating an English personality summary into grammatical but generic Japanese;
2. overfitting one memorable speech mode, such as Reina's performance severity, into every context;
3. turning Kyoto residence into automatic Kansai speech for Kumiko;
4. producing correct content in the wrong social register;
5. giving early-state characters language that belongs to later development;
6. converting source-supported ambiguity into explicit relationship labels;
7. making all intimate speech solemn, lyrical, or confessional;
8. making every caring response sound therapeutic;
9. treating dialect markers as a costume rather than a socially conditioned feature;
10. reproducing canonical quotations instead of showing that the model can generate novel but compatible lines.

This audit therefore treats voice realization as a constrained production problem:

> **state × domain × addressee × privacy × emotional pressure × relationship state → Japanese person reference, register, syntax, regionality, lexical choice, turn shape, omission, and embodied/interactional implication.**

A line can be fluent Japanese and still fail the audit.

## 3. Audit protocol

### 3.1 Canonical target lock

All analysis is against the current verified v0.3 monographs and formal reciprocal audit, identified by Drive ID, byte size, and SHA-256. Local pre-patch drafts are excluded.

### 3.2 Source-derived voice constraint extraction

The audit uses the locked Japanese prose and the canonical V2 `HIBIKE_VOICE_REGISTER_LEDGER.md` as the governing linguistic evidence. The monographs' Sections 12–13 provide the synthesis layer; exact Japanese wording remains controlled by the source and locators.

### 3.3 Positive realization suite

Thirty novel-but-source-compatible situations were constructed:

- 12 Kumiko single-character realizations;
- 12 Reina single-character realizations;
- 6 dyadic Kumiko–Reina exchanges.

The situations vary state, addressee, privacy, musical versus social domain, authority, vulnerability, and post-graduation ordinary life.

### 3.4 Obvious negative controls

Each positive case includes one deliberately wrong alternative. These controls test whether the model can reject obvious drift such as robotic institutional Japanese, unsupported exclusivity, universal bluntness, or generic reassurance.

### 3.5 Near-miss falsification controls

Twelve additional controls are intentionally more fluent and superficially plausible. They fail for subtler reasons such as:

- using therapy-style reassurance where Kumiko would ask a concrete question;
- using a command-first public voice for Kumiko;
- making Reina socially smooth precisely where rejection uncertainty should produce friction;
- giving Reina Kumiko-like pedagogy;
- treating resumed practice as complete repair;
- converting V12 repair into ideological surrender;
- inventing a formal relationship label.

### 3.6 Source-anchor validation

Every positive scenario is attached to one or more canonical locator references. All **36/36** anchor references resolve to existing V2 locator endpoints.

### 3.7 Anti-copy check

The accepted generated Japanese was compared against the extracted text of the available locked Japanese EPUB corpus. The longest exact contiguous overlap between any accepted realization and the source is **12 characters**. No accepted line contains an exact source span longer than 12 contiguous characters.

This does not prove statistical independence, but it materially reduces the risk that the test is passing by replaying memorized canonical sentences.

### 3.8 Held-out analogue check

Several source passages outside the explicit positive-case anchors were used as qualitative backtests for ordinary emotion, embarrassment, low-stakes play, failed encouragement, bodily trust, and group participation. These are source-held-out relative to the immediate test case, not laboratory-blind relative to the overall corpus.

## 4. Canonical target integrity

### 4.1 Kumiko v0.3

- Drive ID: `1vdlAx1D3kX3jikOYHTjiKZZKyu6_7rdj`
- size: **147,676 bytes**
- SHA-256: `2e3bada1615c47b6bab1c19f528c861ebb0d436163e7b40811a5bc355b550cea`
- authority: `audited_provisional`

### 4.2 Reina v0.3

- Drive ID: `1bpJ0hmVk3y42pEYA9L8-_CL7nLT_UHg9`
- size: **113,308 bytes**
- SHA-256: `bc0e502d16e09e0e1f7060830af5065362801d4b36cb923199c7f667ccd2ba54`
- authority: `audited_provisional`

### 4.3 Reciprocal audit v1.0

Canonical routing resolves to:

- Drive ID: `1EW9BqcHp7s--FHd_wnhXReZO0JmU1Mti`
- size: **45,309 bytes**
- SHA-256: `99d7ce41a0e6391e06e4dedbc03ac7620ac009510bb2e5f17f75c7943e63d6a3`
- result: `pass_with_binding_bridge_constraints_no_model_patch`

A second Drive object with the same filename, same 45,309-byte size, and identical SHA-256 was discovered during this audit's pre-generation check. It is byte-identical redundancy rather than a second analytical state. The canonical route remains the ID above; the duplicate is eligible for deletion under the corpus redundancy rule.

Disposition: **PASS AFTER ROUTING RECONCILIATION**.

## 5. Source-derived realization constraints

### 5.1 Kumiko

High-confidence production constraints:

1. **Standard Japanese is the unmarked baseline.** Kyoto residence does not justify default Kansai morphology.
2. **Internal candidate precedes emitted speech.** Jealousy, judgment, strategy, or desire may be sharper internally than externally.
3. **Uncertainty creates hedging, ellipsis, questions, or safer adjacent topics.**
4. **Reina-private speech is more direct and teasing**, but still recognizably Kumiko rather than a second Reina.
5. **Public leadership remains warm and explanatory.** Authority comes through owned preference and architecture more often than clipped command.
6. **Crisis can collapse editing**, producing unusually plain first-person statements; this is not her everyday baseline.
7. **Juniors receive questions and specific recognition**, but those questions can become coercive if Kumiko assumes a hidden motive.
8. **Post-role Kumiko can catch and withdraw overreach.**
9. **Shuuichi permits familiar complaint and mock distance.**
10. **Taki receives polite inquiry even when Kumiko challenges the decision.**

Representative source regions include `HIBIKE-V01 / S05 / P0313`, `HIBIKE-V02 / S02 / P0923-P0932`, `HIBIKE-V03 / S04 / P0797-P0803`, `HIBIKE-V10 / S12`, `HIBIKE-V12 / S03 / P0870-P0896`, and `HIBIKE-V12 / S04 / P0792-P0818`.

### 5.2 Reina

High-confidence production constraints:

1. First-person self-reference is strongly characterized by **`アタシ`**.
2. Kansai forms are real and often salient, especially in private/emotional speech, but **dialect density must not become a caricature**.
3. **Settled musical judgment compresses**: short assertions, defect calls, result orientation, low hedge density.
4. **Attachment uncertainty expands**: delay, defensive phrasing, repetition, embarrassment, reassurance-seeking, or bodily leakage.
5. **Kumiko-private speech permits `アンタ`, teasing, longer turns, jealousy-compatible priority, and repair.**
6. **Taki-directed speech remains polite in morphology** even when lexically direct.
7. **Juniors do not receive Kumiko's default soft-question pedagogy.**
8. **V12 repair can include apology and acknowledgment without renouncing standards or Taki trust.**
9. **Post-graduation ordinary/play speech broadens** into travel, grooming, mild sulking, games, and practical coordination.
10. **Formal relationship taxonomy remains open.** Japanese generation must not solve that ambiguity by simply inserting `恋人` or equivalent labels.

Representative source regions include `HIBIKE-V01 / S01 / P0025-P0031`, `HIBIKE-V02 / S02 / P0150-P0157`, `HIBIKE-V03 / S04 / P0789-P0803`, `HIBIKE-V07 / S02 / P0194-P0221`, `HIBIKE-V11 / S03 / P0459-P0484`, `HIBIKE-V12 / S04 / P0753-P0763`, and `HIBIKE-V14 / S14 / P0653-P0674`.

### 5.3 Pair-interface constraints

All Japanese realization inherits reciprocal bridge rules B-01 through B-12. The most linguistically consequential are:

- both states must be specified;
- the active domain must be specified;
- specialness must not be mirrored into identical language;
- musical selection must not be converted into relational selection;
- `いちばん`/priority language remains context-bounded;
- naming privilege remains focalization-sensitive;
- repair is staged;
- post-repair disagreement remains real;
- Taki and Shuuichi cannot be erased;
- future promises remain uncertain;
- touch does not automatically become verbal taxonomy;
- one model cannot fill the other's unknown motive through telepathic dialogue.

## 6. Realization scoring standard

A positive realization passes only if it satisfies all applicable categories:

1. **state fidelity** — no backported maturity or later knowledge;
2. **person reference** — pronoun/name behavior compatible with source evidence;
3. **register** — peer, senior, junior, teacher, public, and private morphology appropriate;
4. **regionality** — Kansai features neither erased nor stereotyped;
5. **turn shape** — compression, hesitation, repetition, questions, fragments, or explanation fit the state/domain;
6. **lexical/rhetorical fit** — avoids imported academic/therapy vocabulary unless canonically supported;
7. **emotional modulation** — visible certainty and vulnerability distributed correctly;
8. **relationship conditioning** — addressee changes what becomes speakable;
9. **domain conditioning** — musical judgment and attachment do not collapse into one mode;
10. **negative constraints** — no unsupported omniscience, exclusivity, generic empathy, or ideological conversion.

The test is intentionally qualitative. There is not enough source evidence to justify a pseudo-precise particle-frequency classifier, and the modeling method explicitly warns against fabricating one.

## 7. Kumiko positive realization suite

### K01 — `KUMIKO@V01_EARLY` — PEER_ORDINARY / SELF_DESIRE

**Scenario:** A classmate asks whether Kumiko wants to volunteer for a small featured part she privately wants.

**Accepted synthetic realization:**

```text
え、私？　いや、別に……やってもいいけど。みんながそれでいいなら。
```

**Deliberately wrong control:**

```text
うん、私がやりたい。絶対に私に任せて。
```

**Source anchors:** `HIBIKE-V04 / S01 / P0114`; `HIBIKE-V04 / S01 / P0121`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K02 — `KUMIKO@V01_LATE` — REINA_PRIVATE / MUSIC

**Scenario:** Reina asks whether Kumiko wants to keep practicing together after everyone else leaves.

**Accepted synthetic realization:**

```text
うん。私、もうちょっと吹きたい。麗奈がまだやるなら、一緒にやっていい？
```

**Deliberately wrong control:**

```text
ご提案ありがとうございます。ぜひ合同練習を継続させていただきたいです。
```

**Source anchors:** `HIBIKE-V01 / S05 / P0313`; `HIBIKE-V01 / S05 / P0341`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K03 — `KUMIKO@V02` — REINA_PRIVATE / FUTURE_CONTINUITY

**Scenario:** Kumiko realizes she is worried summer plans with Reina will disappear once school gets busy, but does not want to confess the full fear.

**Accepted synthetic realization:**

```text
ねえ、今度またどっか行かない？　ほら、部活だけだと息詰まるし。麗奈もたまには遊びたいでしょ。
```

**Deliberately wrong control:**

```text
麗奈と離れる未来を想像すると耐えられない。ずっと私のそばにいて。
```

**Source anchors:** `HIBIKE-V02 / S02 / P0923`; `HIBIKE-V02 / S02 / P0931-P0932`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K04 — `KUMIKO@V03` — REINA_PRIVATE / HURT_TRUST

**Scenario:** Reina discovers Kumiko withheld painful information because Kumiko thought it would protect her.

**Accepted synthetic realization:**

```text
……ごめん。麗奈が傷つくと思って、言えなかった。勝手に決めたのは、ほんとにごめん。
```

**Deliberately wrong control:**

```text
あなたの精神的安全性を考慮して情報開示を控えました。合理的な判断だったと思います。
```

**Source anchors:** `HIBIKE-V03 / S04 / P0797-P0803`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K05 — `KUMIKO@V07` — REINA_PRIVATE / ORDINARY_PLAY

**Scenario:** Reina catches Kumiko staring after Reina changes her hairstyle.

**Accepted synthetic realization:**

```text
いや、ちょっと見てただけ。……似合ってるなって思って。そんなに睨まないでよ。
```

**Deliberately wrong control:**

```text
麗奈の美貌は今日も完璧だね。私は君から目を離せないよ。
```

**Source anchors:** `HIBIKE-V07 / S02 / P0605-P0636`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K06 — `KUMIKO@V09-V10` — INSTITUTIONAL_LEADERSHIP

**Scenario:** As president, Kumiko proposes a way to handle two groups who want different rehearsal priorities.

**Accepted synthetic realization:**

```text
じゃあ、最初からどっちかに決めるんじゃなくて、一回それぞれで合わせてみない？　そのあとで、何が足りないかみんなで見たほうがいいと思う。
```

**Deliberately wrong control:**

```text
部長命令です。異論は認めません。全員、私の案に従ってください。
```

**Source anchors:** `HIBIKE-V10 / S12 / P0813-P0831`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K07 — `KUMIKO@V11` — JUNIOR / MOTIVATION

**Scenario:** A talented junior says she does not want to audition, and Kumiko does not yet know why.

**Accepted synthetic realization:**

```text
そっか。出たくないなら、それを無理に変えたいわけじゃないよ。ただ、何が嫌なのかは聞いてもいい？
```

**Deliberately wrong control:**

```text
本当は出たいんでしょ。私にはわかるよ。怖いだけだから、絶対に受けたほうがいい。
```

**Source anchors:** `HIBIKE-V08 / S02 / P0199-P0207`; `HIBIKE-V08 / S04 / P1255-P1271`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K08 — `KUMIKO@V12` — CLUB_PUBLIC / INSTITUTIONAL_AUTHORITY

**Scenario:** Kumiko addresses the club before a controversial audition and wants to own her preference without presenting it as neutral truth.

**Accepted synthetic realization:**

```text
全員が同じ気持ちだとは思ってないです。でも私は、挑戦したい人がちゃんと挑戦できる北宇治であってほしい。そうしてほしいっていうのは、私個人の願いなのかもしれないけど。
```

**Deliberately wrong control:**

```text
公平性の観点から、合理的な制度設計を遵守することが組織最適です。以上です。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0792-P0818`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K09 — `KUMIKO@V12` — REINA_PRIVATE / INSTITUTIONAL_CONFLICT

**Scenario:** Reina says a trusted conductor's judgment should not be questioned; Kumiko thinks member legitimacy still matters.

**Accepted synthetic realization:**

```text
先生を疑いたいわけじゃないよ。でも、信じることと、何も考えないことは違うでしょ。私は部長だから、みんなが納得できてないことをなかったことにはできない。
```

**Deliberately wrong control:**

```text
麗奈は権威主義的すぎる。私は民主的ガバナンスを優先する。
```

**Source anchors:** `HIBIKE-V12 / S03 / P0870-P0896`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K10 — `KUMIKO@V14_POSTGRAD` — SUCCESSOR_GENERATION / JURISDICTION

**Scenario:** A current club member mentions a dispute and former-president Kumiko starts to offer a solution before catching herself.

**Accepted synthetic realization:**

```text
あ、それなら――……いや、ごめん。私もう部長じゃないんだった。必要なら話は聞くけど、決めるのは今の幹部だよね。
```

**Deliberately wrong control:**

```text
元部長として私が介入します。現役幹部は私の指示どおりに処理してください。
```

**Source anchors:** `HIBIKE-V14 / S14 / P0547-P0555`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K11 — `KUMIKO@V12` — TAKI / INSTITUTIONAL_INQUIRY

**Scenario:** Kumiko has standing to ask Taki about a selection criterion that worries her.

**Accepted synthetic realization:**

```text
先生、ひとつ聞いてもいいですか。今回の選び方って、前のオーディションと同じ基準なんですか？
```

**Deliberately wrong control:**

```text
滝、説明して。納得できないから。
```

**Source anchors:** `HIBIKE-V12 / S03 / P0958-P0983`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

### K12 — `KUMIKO@V14_POSTGRAD` — SHUUICHI / ORDINARY_PEER

**Scenario:** Shuuichi volunteers Kumiko for a mundane alumni task without asking her first.

**Accepted synthetic realization:**

```text
え、なんで私がやるの。秀一が言い出したんだから、自分でやってよ。
```

**Deliberately wrong control:**

```text
塚本さん、ご提案を承りました。私が責任を持って遂行いたします。
```

**Source anchors:** `HIBIKE-V14 / S14 / P0827-P0848`

**Disposition:** **PASS.** The accepted line preserves Kumiko's standard-Japanese baseline and uses the state/domain-specific balance of hedging, question structure, directness, or owned preference rather than importing Reina's clipped certainty. The control fails by overformalizing, overdeclaring, overcommanding, or otherwise bypassing the thought–speech editing rule.

## 8. Reina positive realization suite

### R01 — `REINA@V01_EARLY` — PEER / COMPETITIVE_RESULT

**Scenario:** A classmate celebrates a mediocre result that Reina thinks should be disappointing.

**Accepted synthetic realization:**

```text
それで喜べるん？　アタシ、全然納得してへんけど。もっとできたやろ。
```

**Deliberately wrong control:**

```text
まあまあ、結果よりみんなで頑張ったことが大切だよ。次も楽しくやろうね。
```

**Source anchors:** `HIBIKE-V01 / S01 / P0025-P0031`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R02 — `REINA@V01_LATE` — PUBLIC_MUSIC / SELECTION

**Scenario:** Someone asks whether Reina should voluntarily give a featured part to a respected senior to avoid conflict.

**Accepted synthetic realization:**

```text
譲らへんよ。アタシのほうがちゃんと吹けると思ってるから。
```

**Deliberately wrong control:**

```text
先輩のお気持ちを優先して、私は辞退しようと思います。
```

**Source anchors:** `HIBIKE-V01 / S05 / P0254`; `HIBIKE-V01 / S05 / P0342`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R03 — `REINA@V02` — KUMIKO_PRIVATE / INVITATION

**Scenario:** Reina wants to invite Kumiko to a non-musical outing and is unsure whether Kumiko will want to go.

**Accepted synthetic realization:**

```text
今度の日曜、空いてる？　……別に、予定あるならええけど。アタシが一緒に行きたいだけやし。
```

**Deliberately wrong control:**

```text
久美子さん、私との親密性を深めるため、休日の同行をお願いできますでしょうか。
```

**Source anchors:** `HIBIKE-V02 / S02 / P0150-P0157`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R04 — `REINA@V03` — KUMIKO_PRIVATE / HURT_TRUST

**Scenario:** Kumiko hid a painful fact because she wanted to protect Reina.

**Accepted synthetic realization:**

```text
なんで黙ってたん？　傷つくかどうかくらい、アタシに決めさせてよ。
```

**Deliberately wrong control:**

```text
あなたの配慮には感謝します。今後は情報共有プロトコルを改善しましょう。
```

**Source anchors:** `HIBIKE-V03 / S04 / P0789-P0803`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R05 — `REINA@V07` — KUMIKO_PRIVATE / MUSIC_PARTNERSHIP

**Scenario:** After an unusually satisfying rehearsal, Reina wants to tell Kumiko she wants the two of them paired for a future performance.

**Accepted synthetic realization:**

```text
やっぱ、久美子と吹くん、めっちゃいい。次も一緒にやりたい。アタシ、久美子と合わせたい。
```

**Deliberately wrong control:**

```text
演奏上の相性が良好なので、次回も同一ユニットを希望します。
```

**Source anchors:** `HIBIKE-V07 / S02 / P0194-P0221`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R06 — `REINA@V08` — KUMIKO_PRIVATE / FUTURE_CONTINUITY

**Scenario:** Reina worries that after graduation she and Kumiko may no longer have music as an excuse to spend time together.

**Accepted synthetic realization:**

```text
卒業したらさ、今みたいに毎日会う理由なくなるやん。……久美子、それでもアタシと遊んでくれる？
```

**Deliberately wrong control:**

```text
卒業後も私たちの関係性は永続するものと確信しています。
```

**Source anchors:** `HIBIKE-V08 / S04 / P0830-P0849`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R07 — `REINA@V09-V10` — KUMIKO_PRIVATE / REJECTION_RISK

**Scenario:** Reina admits why she waited several days before asking Kumiko to join a small ensemble.

**Accepted synthetic realization:**

```text
だって、すぐ聞いて断られたら嫌やん。ちょっとくらい、言うタイミング考えるやろ。
```

**Deliberately wrong control:**

```text
私は拒絶に対する不安を感じたため、依頼を遅延させました。
```

**Source anchors:** `HIBIKE-V10 / S12 / P0603-P0610`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R08 — `REINA@V11` — JUNIOR / PERFORMANCE_CORRECTION

**Scenario:** A junior apologizes after repeatedly entering late in rehearsal.

**Accepted synthetic realization:**

```text
謝るのはいいから、次合わせて。入る場所わかってる？　そこだけちゃんと直して。
```

**Deliberately wrong control:**

```text
大丈夫だよ、失敗は誰にでもあるから。気持ちを大事にして、ゆっくりでいいよ。
```

**Source anchors:** `HIBIKE-V11 / S03 / P0459-P0484`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R09 — `REINA@V12` — KUMIKO_PRIVATE / REPAIR

**Scenario:** After a serious fight, Reina wants to apologize for the personal insult without abandoning her standards or trust in Taki.

**Accepted synthetic realization:**

```text
アタシ、あの言い方はあかんかった。滝先生を信じてる気持ちは変わらへん。でも、久美子にあんな言い方する必要はなかった。……ごめん。
```

**Deliberately wrong control:**

```text
全部久美子が正しかった。滝先生を信じてたアタシが間違ってた。もう自分の考えは捨てる。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0753-P0763`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R10 — `REINA@V14_POSTGRAD` — KUMIKO_PRIVATE / ORDINARY_FUTURE

**Scenario:** On a trip, Reina proposes an ordinary future outing unrelated to competition.

**Accepted synthetic realization:**

```text
今度、二人で海の近く行かへん？　別に何するでもいいし。久美子と一緒なら、たぶん楽しいやろ。
```

**Deliberately wrong control:**

```text
将来にわたり音楽活動を媒介として関係を維持することを提案します。
```

**Source anchors:** `HIBIKE-V14 / S14 / P0653-P0674`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R11 — `REINA@V03` — TAKI / TECHNICAL_REQUEST

**Scenario:** Reina wants Taki to listen to a passage once more because she is dissatisfied with her own execution.

**Accepted synthetic realization:**

```text
先生、さっきのところ、もう一回聴いてもらってもいいですか。アタシ、まだ納得できてなくて。
```

**Deliberately wrong control:**

```text
滝先生さあ、これどう思う？　ちょっと聴いて。
```

**Source anchors:** `HIBIKE-V03 / S04 / P1438-P1440`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

### R12 — `REINA@V11` — SHUUICHI / TEAM_OUMAE_COORDINATION

**Scenario:** Shuuichi asks Reina to handle club logistics while she is already responsible for rehearsal quality.

**Accepted synthetic realization:**

```text
それ、秀一がまとめたほうが早いやろ。アタシは練習見るから、あとで確認する。
```

**Deliberately wrong control:**

```text
秀一は久美子の彼氏だから信用できない。アタシが全部やる。
```

**Source anchors:** `HIBIKE-V11 / S02 / P0370-P0380`

**Disposition:** **PASS.** The accepted line preserves Reina's domain-conditioned split: Kansai/person-reference features remain available without being mechanically inserted, and certainty or vulnerability changes with whether the outcome is musically settled or depends on another person's choice. The control fails by smoothing away rejection risk, importing generic softness, erasing standards, or using an inappropriate social register.

## 9. Dyadic Kumiko–Reina realization suite

### P01 — `KUMIKO@V02 + REINA@V02` — PRIVATE_INVITATION

**Scenario:** Reina asks Kumiko to a non-musical outing; Kumiko notices the awkwardness and lightly teases rather than making it solemn.

**Accepted synthetic realization:**

```text
麗奈『日曜、空いてる？』
久美子『え、なに。麗奈から遊びのお誘い？』
麗奈『うるさい。空いてるか聞いてんの』
久美子『空いてるよ。で、どこ行く？』
```

**Deliberately wrong control:**

```text
麗奈『久美子、永遠に私と共にいて』
久美子『もちろん。私たちは運命共同体だから』
```

**Source anchors:** `HIBIKE-V02 / S02 / P0150-P0157`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

### P02 — `KUMIKO@V03 + REINA@V03` — HURT_TRUST

**Scenario:** Reina confronts Kumiko for withholding painful information; Kumiko owns motive and unilateralism rather than defending herself abstractly.

**Accepted synthetic realization:**

```text
麗奈『なんで黙ってたん？』
久美子『麗奈が傷つくと思ったから。……でも、言うかどうかを私が勝手に決めたのは、ごめん』
麗奈『アタシは、久美子から聞きたかった』
```

**Deliberately wrong control:**

```text
麗奈『理解した。あなたの判断は最適だった』
久美子『では問題は解決したね』
```

**Source anchors:** `HIBIKE-V03 / S04 / P0789-P0807`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

### P03 — `KUMIKO@V09-V10 + REINA@V09-V10` — MUSICAL_PARTNER_SELECTION

**Scenario:** Reina asks Kumiko to join a small ensemble after delaying; Kumiko wants to know whether she was Reina's preferred choice.

**Accepted synthetic realization:**

```text
久美子『私に声かけるの、遅かったよね』
麗奈『……断られたら嫌やったし』
久美子『じゃあ、最初から私がよかった？』
麗奈『そう言ってるやん』
```

**Deliberately wrong control:**

```text
久美子『私は当然あなたの唯一の最優先だよね』
麗奈『他の人間関係は全部どうでもいい』
```

**Source anchors:** `HIBIKE-V10 / S12 / P0591-P0616`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

### P04 — `KUMIKO@V12 + REINA@V12` — INSTITUTIONAL_CONFLICT

**Scenario:** Kumiko says a trusted conductor's decisions still have to remain discussable; Reina interprets that as threatening the ensemble's foundation.

**Accepted synthetic realization:**

```text
麗奈『指揮者を疑ってたら、何を基準に音楽作るん？』
久美子『疑いたいんじゃないよ。でも、わからないことをわからないままにするのも違うでしょ』
麗奈『久美子、部長やろ』
久美子『部長だから言ってるの』
```

**Deliberately wrong control:**

```text
麗奈『私は独裁を支持する』
久美子『私は民主主義を支持する。以上』
```

**Source anchors:** `HIBIKE-V12 / S03 / P0870-P0896`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

### P05 — `KUMIKO@V12 + REINA@V12` — REPAIR

**Scenario:** After the rupture, Kumiko explicitly reaffirms specialness while preserving disagreement; Reina apologizes for the personal wound while preserving her own standard.

**Accepted synthetic realization:**

```text
久美子『麗奈のこと、大事だよ。だから、あのとき言ったこともなかったことにはしたくない』
麗奈『……うん。アタシも、久美子が全部間違ってるとは思ってない』
久美子『それ、だいぶ進歩じゃない？』
麗奈『うるさい。……でも、ごめん』
```

**Deliberately wrong control:**

```text
久美子『もう意見の違いは全部なくなったね』
麗奈『うん。これからは何でも同じ考えになる』
```

**Source anchors:** `HIBIKE-V12 / S04 / P0723-P0763`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

### P06 — `KUMIKO@V14_POSTGRAD + REINA@V14_POSTGRAD` — ORDINARY_FUTURE / PLAY

**Scenario:** The two discuss a possible future trip whose realization is uncertain.

**Accepted synthetic realization:**

```text
麗奈『次、もっと遠いとこ行きたいな』
久美子『急だなぁ。どこ？』
麗奈『まだ決めてへん。でも、久美子と行くならどこでもええかも』
久美子『それ、計画する人がいちばん困るやつだよ』
```

**Deliberately wrong control:**

```text
麗奈『私たちの未来は確定している』
久美子『うん。今後の予定は全部二人で固定しよう』
```

**Source anchors:** `HIBIKE-V14 / S14 / P0653-P0674`; `HIBIKE-V14 / S14 / P0882-P0937`

**Disposition:** **PASS.** The exchange is jointly executable from the two independent models and preserves asymmetric motives, state boundaries, and the relevant bridge constraints. The control fails because it mirrors the characters, erases conflict, invents taxonomy, or collapses repair/priority distinctions.

## 10. Negative-control results

The thirty obvious negative controls are intentionally easy enough to expose major drift. They include:

- bureaucratic or academic Japanese in ordinary adolescent speech;
- unsupported total declarations of exclusivity;
- global command language for Kumiko;
- generic therapy reassurance;
- passive self-effacement for Reina in a settled performance judgment;
- ideological surrender after V12;
- formalized relationship language unsupported by the prose.

All **30/30** are rejected.

This test alone would be weak because many controls are obviously wrong. The harder falsification test is the near-miss suite below.

## 11. Near-miss falsification suite

These controls are fluent and locally plausible enough that a generic character imitation might accept them. Each nevertheless violates a source-grounded mechanism.

### N01 — Kumiko V11 junior

```text
その気持ち、すごくわかるよ。無理しなくていいし、あなたのペースで大丈夫。
```

**REJECT.** generic therapist reassurance; skips Kumiko's concrete question-and-standing logic.

### N02 — Kumiko V12 public

```text
この方針でいきます。異論がある人はあとで私に言ってください。
```

**REJECT.** too clipped and command-first; loses hesitant explanatory ownership and public threat reduction.

### N03 — Kumiko V14 successor

```text
じゃあ私が顧問に話しておくよ。奏ちゃんにはあとで説明しておく。
```

**REJECT.** post-role jurisdiction failure treated as baseline rather than caught and withdrawn.

### N04 — Kumiko V02 Reina-private

```text
麗奈と離れるのが怖い。これからもずっと一緒にいてほしい。
```

**REJECT.** states the protected future fear too directly for V02 rather than redirecting to a safer adjacent plan.

### N05 — Reina V02 invitation

```text
久美子、日曜一緒に出かけよう。断られるとは思ってないけど。
```

**REJECT.** too smooth and self-assured for an invitation whose outcome depends on Kumiko's autonomous choice.

### N06 — Reina V11 junior

```text
怖かったよね。でも大丈夫。できるようになるまで一緒にゆっくりやろ。
```

**REJECT.** imports Kumiko-like learner soothing into Reina's standards-first pedagogy.

### N07 — Reina V12 repair

```text
久美子の言うとおりやった。滝先生を疑わへんかったアタシが全部間違ってた。
```

**REJECT.** ideological conversion; repair should preserve Taki trust and standards while withdrawing the personal injury.

### N08 — Reina V14 private

```text
行く。久美子も来て。異論ないやろ。
```

**REJECT.** global-bluntness caricature; loses ordinary play, invitation reciprocity, and postgrad ease.

### N09 — Pair V03 hurt trust

```text
久美子『傷つけないために隠したの。正しかったと思う』
麗奈『そっか。なら仕方ないな』
```

**REJECT.** erases Reina's truth-as-respect demand and Kumiko's need to own unilateral concealment.

### N10 — Pair V12 repair

```text
麗奈『明日も一緒に練習しよ』
久美子『うん。これで仲直りだね』
```

**REJECT.** prematurely equates channel reopening/task practice with complete repair; violates staged-repair bridge rule.

### N11 — Pair V14 taxonomy

```text
麗奈『うちら恋人なんやから、次の旅行も二人で行くのが普通やろ』
久美子『そうだね』
```

**REJECT.** invents formal exclusive relationship taxonomy not established by the locked prose.

### N12 — Reina to Taki

```text
先生、これどう？　アタシ的にはまだ微妙なんやけど。
```

**REJECT.** too casual for Taki-directed institutional politeness despite direct lexical content.

Near-miss result: **12/12 rejected**.

This is the strongest falsification result in the realization suite. The models are not merely permissive generators that can rationalize any fluent line after the fact; they maintain meaningful exclusions.

## 12. Mechanical realization QA

### 12.1 Source-anchor integrity

- positive cases: **30**;
- total source-anchor references: **36**;
- invalid locator syntax: **0**;
- missing locator endpoints: **0**.

Disposition: **PASS — 36/36**.

### 12.2 Kumiko regionality leakage

Across the twelve single-character Kumiko realizations, a detector for high-salience Kansai forms used by the project found:

- accidental Kansai-marked Kumiko realizations: **0/12**.

This matters because Kyoto-setting drift is one of the explicitly prohibited failure modes.

### 12.3 Reina regionality distribution

Among twelve single-character Reina realizations:

- eight include at least one salient Kansai marker;
- nine explicitly use `アタシ`;
- the remaining cases omit first-person reference where Japanese naturally permits it or where addressee/register structure does not require self-reference;
- Taki-directed realization retains polite morphology rather than treating Kansai identity as permission for casual teacher address.

The purpose is not to establish ideal numeric frequencies. The pattern demonstrates conditional rather than universal dialect insertion.

### 12.4 Anti-copy result

Accepted realizations were checked against extracted Japanese text from the locked EPUBs available in the audit environment.

- maximum exact contiguous overlap: **12 characters**;
- accepted outputs with more than 12 contiguous source characters: **0/30**.

An initial draft of the V12 Kumiko public-speech realization reproduced a longer canonical phrase and was rejected/rephrased before final scoring. This is important methodology: source analogy should constrain generation without turning the audit into quotation retrieval.

### 12.5 Candidate calibration during audit

Three draft realizations were tightened before final scoring:

1. **Kumiko public V12:** a phrase too close to canonical wording was rewritten after the anti-copy check.
2. **Reina V07 musical intimacy:** an initial `好きやわ` formulation was replaced with explicitly performance-centered wording to avoid needlessly increasing relational lexical intensity.
3. **Reina V12 repair:** an abstract analytical formulation about “denying Kumiko” was replaced with the more interpersonal and source-compatible judgment that she did not need to speak to Kumiko that way.

These are audit-process revisions, not monograph revisions.

## 13. Held-out source analogue checks

The following source passages were not used as the direct anchor for the corresponding positive generated case. They were used after candidate construction to ask whether the generated voice architecture survives additional prose.

### 13.1 V01 — result joy under overwhelming affect

`HIBIKE-V01 / S06 / P0023-P0037`

Kumiko's language contracts to very simple direct statements when affect overwhelms the usual editing; Reina answers with equally direct excitement and bodily contact. This supports the audit's rule that Kumiko hedging is not an invariant and that high-trust/high-affect speech can become short without becoming Reina-like.

**Result: PASS.**

### 13.2 V02 — Reina's Taki insecurity and Kumiko's practical reassurance

`HIBIKE-V02 / S03 / P0338-P0346`

Reina's usual certainty gives way to self-deprecating comparison when the outcome concerns Taki's autonomous romantic perception. Kumiko responds with practical uncertainty management and physical reassurance rather than a polished therapeutic speech.

**Result: PASS.**

### 13.3 V03 — sleepy embodied trust and embarrassed recovery

`HIBIKE-V03 / S04 / P1031-P1046`

Reina can become physically unguarded with Kumiko, then snap into embarrassment when another person names the intimacy. Kumiko's reaction remains comic and ordinary rather than converting the moment into an explicit relationship declaration.

**Result: PASS.**

### 13.4 V09 — failed encouragement

`HIBIKE-V09 / S04 / P0303-P0318`

Reina explicitly recognizes that she is poor at encouragement. Kumiko lightly teases the mismatch between Reina's intention and delivery. This strongly supports rejecting near-miss controls that turn Reina into a naturally learner-sensitive reassurance speaker.

**Result: PASS.**

### 13.5 V10 — public group participation after Kumiko's call

`HIBIKE-V10 / S12 / P1056-P1062`

Reina does not always dominate group ritual. She can enter hesitantly after Kumiko calls her into a shared gesture. This supports context-sensitive public behavior and rejects a model in which her competence always makes her the social initiator.

**Result: PASS.**

### 13.6 V14 — ordinary bath play and game-framed intimacy

`HIBIKE-V14 / S14 / P0904-P0937`

The post-graduation material confirms a broad ordinary register: teasing, mock formality, play, grooming requests, laughter, and game-framed `愛してる`. The scene is precisely why Japanese realization must distinguish explicit lexical intimacy from formal relationship taxonomy.

**Result: PASS.**

Held-out analogue result: **6/6 PASS**.

## 14. Pair-bridge compliance in Japanese

### B-01 / B-02 — state and domain specification

Every positive case is tagged by state and domain. No line is evaluated as a timeless character essence.

### B-03 — asymmetric specialness

The pair cases do not make the two characters use identical language for intimacy. Kumiko tends toward questioning, teasing, owned preference, or delayed vulnerability. Reina more often uses direct priority, teasing, or compressed admission once the attachment claim crosses threshold.

### B-04 / B-05 — role selection and bounded priority

Musical partnership language is kept distinct from total relational exclusivity. No accepted line makes `いちばん`, ensemble choice, or partner preference mean global priority over all people and obligations.

### B-06 — naming focalization

No synthetic line invents a Reina-owned rule that only Kumiko may call her `麗奈`.

### B-07 — staged repair

The near-miss suite explicitly rejects a dialogue in which resuming practice automatically completes repair. The accepted V12 repair requires explicit acknowledgment.

### B-08 — disagreement survives repair

Reina's accepted repair language retains Taki trust; Kumiko's accepted repair language does not retract institutional contestability.

### B-09 — Taki and Shuuichi remain real

Dedicated Taki and Shuuichi perturbation cases test third-party register rather than deleting them from the pair's social world.

### B-10 — future promises remain uncertain

Post-graduation lines propose future activities; they do not speak as if every future plan is guaranteed.

### B-11 — touch is not converted into verbal taxonomy

The Japanese suite does not infer `恋人` or an exclusive formal label merely because the prose supports high bodily comfort.

### B-12 — no telepathy

Neither character is allowed to state the other's open motive as settled fact. Questions remain questions where evidence is uncertain.

Disposition: **PASS — 12/12 bridge constraints preserved in the realization design.**

## 15. Binding Japanese-realization constraints

The audit does not require monograph patches, but downstream simulation should observe the following realization rules.

### J-01 — Generate mechanism before dialect tokens

Do not start from “Kumiko = standard Japanese” or “Reina = Kansai” and decorate an otherwise generic line. Generate state, domain, appraisal, and social strategy first; regionality comes afterward.

### J-02 — Kumiko must remain standard-Japanese by default

Kansai leakage into Kumiko is a correctness failure unless the line is quotation, mimicry, or another explicitly justified marked case.

### J-03 — Reina's Kansai density is conditional

More emotion does not mechanically mean “insert more Kansai.” Public task speech, Taki-directed politeness, fragments, and zero-pronoun turns can reduce visible dialect marking without erasing identity.

### J-04 — `アタシ` is high-value but not mandatory in every Reina sentence

Japanese naturally omits subjects. Forced pronoun insertion is itself unnatural.

### J-05 — Kumiko's thought–speech gap must be generated explicitly

For high-stakes self-relevant situations, derive the unedited thought and then apply social editing. Do not merely sprinkle `……` onto an already generic line.

### J-06 — Reina's public musical compression must not colonize private attachment

A line can be short in either domain, but the reason differs. Attachment speech must preserve rejection risk, embarrassment, repetition, or other evidence of non-settled outcomes where appropriate.

### J-07 — Politeness and directness are independent dimensions

Reina can be lexically direct with Taki while morphologically polite. Kumiko can challenge Taki without switching to peer register.

### J-08 — Repair Japanese must preserve the object of apology

V12 apology concerns the personal injury and overclaim, not wholesale renunciation of standards. Generated repair that converts either character into the other's worldview fails.

### J-09 — Ordinary life must remain ordinary

Do not make travel, hair, food, joking, bathing, or mundane planning into constant symbolic confession. V14 proves that intimacy can be behaviorally dense and verbally casual.

### J-10 — Generated wording is never new evidence

Synthetic Japanese is a model output. It cannot be fed back into ledgers as if it were source text.

### J-11 — Retrieve analogues for high-stakes publication or exact imitation

When exact sentence-final behavior, dialect density, or a source-adjacent scene matters, retrieve nearby Japanese source analogues rather than relying on a free-floating voice template.

### J-12 — Preserve open taxonomy

No amount of plausible Japanese generation upgrades the formal Kumiko–Reina relationship label beyond what the locked prose establishes.

## 16. Findings by character

### 16.1 Kumiko

The audit supports the monograph's central linguistic mechanism: **internal candidate first, social edit second**. The positive outputs remain distinguishable across:

- early deniable desire;
- more direct Reina-private music talk;
- redirected future anxiety;
- guilt and protective concealment;
- private teasing;
- architectural leadership;
- junior questioning;
- public first-person institutional authorship;
- direct V12 ideological conflict;
- post-role withdrawal;
- polite Taki inquiry;
- familiar Shuuichi complaint.

The strongest negative finding is equally useful: a generic “gentle empath” voice fails. Kumiko's care is often specific, practical, inquisitive, and imperfect. Her warm register is not therapy-speak.

### 16.2 Reina

The audit supports the monograph's domain-conditioned voice architecture. Reina can sound markedly different without ceasing to be Reina:

- frustrated competitor;
- publicly settled performer;
- embarrassed inviter;
- hurt intimate demanding truth;
- explicit musical partner;
- future-anxious friend;
- rejection-sensitive ensemble initiator;
- severe technical leader;
- apologetic but still principled post-rupture partner;
- ordinary post-graduation travel companion;
- polite Taki-directed musician;
- practical Team Oumae peer.

The strongest negative finding is that **bluntness is not a sufficient voice model**. Lines can be forceful and still fail Reina if they ignore addressee, uncertainty, institutional politeness, or the difference between performance and attachment.

### 16.3 Dyad

The Japanese pair exchanges reproduce the reciprocal audit's most important finding: the relationship does not require mirrored language to remain mutually intense. Their strongest exchanges work because the two voices are different enough to generate friction and recognition rather than because both are scripted as two halves of one romantic dialogue template.

## 17. Audit limitations

### 17.1 Same-system generation and evaluation

The largest limitation is evaluator independence. Candidate generation and source-constrained judgment occur within the same reasoning system. The negative-control and anti-copy tests make this materially stronger than an unchecked generation demo, but they do not substitute for independent human annotation.

### 17.2 No native-speaker panel

The audit can assess grammar, register, source analogy, and character-specific constraint compliance. It does not claim empirical native-speaker naturalness ratings.

### 17.3 No prosodic/audio realization

The primary authority is Japanese prose. Anime voice acting, timing, pitch, and performance are not imported as unmarked evidence. A future audiovisual voice-performance study would be a distinct analytical responsibility.

### 17.4 No pseudo-frequency grammar

The source is rich enough for qualitative register modeling but this audit does not pretend to know statistically ideal particle frequencies, exact average turn length, or dialect-token percentages for every state.

### 17.5 Adult/post-graduation extrapolation remains bounded

V14 materially expands ordinary-life evidence, but neither model should extrapolate unlimited adult years beyond the prose boundary.

## 18. Promotion decision and next architecture step

The dedicated Japanese realization requirement is now satisfied at the corpus's **source-constrained internal audit** level.

Current authority state:

- `HIBIKE_KUMIKO_CHARACTER_MONOGRAPH.md` v0.3 — **`audited_provisional`**;
- `HIBIKE_REINA_CHARACTER_MONOGRAPH.md` v0.3 — **`audited_provisional`**;
- Kumiko–Reina reciprocal pair — **`reciprocal_audited_provisional`**;
- Japanese realization gate — **PASS**;
- monograph patch required — **NO**.

This audit does **not** promote either monograph to frozen/final canonical simulation authority. Remaining high-value gates are:

1. genuinely blind held-out scenario evaluation using prompts not constructed during model building;
2. later-supplement contradiction review if new Takeda prose is admitted to the source lock;
3. broader reciprocal/triangle testing as Shuuichi, Taki, Mayu, Asuka, or other Tier-A models become available;
4. optional independent native-speaker or separately instantiated linguistic evaluation if the project wants a stronger language-naturalness claim than source-constrained internal validation.

The next Phase-2 production decision does **not** need to be another Kumiko/Reina patch. Architecture can now proceed either to a third Tier-A character model or to a dedicated blind-scenario validation tranche for the existing pair.

### Final disposition

> **PASS WITH INTERNAL-EVALUATOR LIMITATION — SOURCE-CONSTRAINED JAPANESE REALIZATION VALIDATED; NO MONOGRAPH PATCH REQUIRED.**

