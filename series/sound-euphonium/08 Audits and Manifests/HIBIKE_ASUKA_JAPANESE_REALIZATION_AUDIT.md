---
series: HIBIKE
artifact_type: audit
scope: ASUKA_JAPANESE_REALIZATION_V0.2
generation: V2
version: "1.0"
status: canonical
reasoning_profile: extra_high_source_constrained_japanese_realization_audit
audit_targets:
  - "04 Character Modeling/HIBIKE_ASUKA_CHARACTER_MONOGRAPH.md"
  - "08 Audits and Manifests/HIBIKE_ASUKA_CHARACTER_MONOGRAPH_AUDIT.md"
  - "08 Audits and Manifests/HIBIKE_KUMIKO_ASUKA_RECIPROCAL_MODEL_AUDIT.md"
audit_target_versions:
  asuka: "0.2"
  asuka_monograph_audit: "1.1"
  kumiko_asuka_reciprocal_audit: "1.0"
audit_target_drive_ids:
  asuka: "146tjbGt20wdQPa-p9XikNr_WClObPM2a"
  asuka_monograph_audit: "1kENTHep7_LhO_sqfZrHwRfP13B5Q2iYz"
  kumiko_asuka_reciprocal_audit: "1XrrGT3opl-z1f9T-T6xz8Eg8SPW4OMcC"
audit_target_sha256:
  asuka: "094e230fba86e3f4e0b199cb86ae8c46add253f30ba5df9eef82a797c9cf98f5"
  asuka_monograph_audit: "96940bde2080625818b9e93949725e11740c3af002cecbe69709418080907b76"
  kumiko_asuka_reciprocal_audit: "de2d58e5f0d31f72765da4ab8447da6df094d674c694f2b64015c494d4637338"
audit_result: pass_with_internal_evaluator_limit_no_model_patch
japanese_realization_gate: pass
monograph_patch_required: false
positive_realization_suite: "30/30 PASS"
obvious_negative_controls: "30/30 REJECTED"
fluent_near_miss_controls: "18/18 REJECTED"
held_out_source_analogues: "8/8 PASS"
kumiko_asuka_bridge_realization: "16/16 PASS"
raw_source_identity_recheck: "V12 1/1 SHA-256 PASS; remaining anchors resolved through canonical locator indexes bound to Phase-1 source lock"
source_anchor_validation: "50 fully-qualified occurrences / 38 unique ranges / 1,400 expanded paragraph positions / 0 missing / 0 reversed"
anti_copy_max_contiguous_source_chars: 10
independent_native_speaker_validation: deferred
source_boundary: "Locked Japanese EPUB core HIBIKE-V01 through HIBIKE-V14; canonical V2 locator indexes; V2 voice/register and relationship ledgers; Asuka v0.2; Asuka independent audit v1.1; Kumiko-Asuka reciprocal audit v1.0; prior Kumiko-Reina and Shuuichi Japanese-realization audits used as methodological precedent only; raw V12 Japanese EPUB re-hashed for direct adult-state source identity"
canonical_home: "08 Audits and Manifests/HIBIKE_ASUKA_JAPANESE_REALIZATION_AUDIT.md"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: "2026-08-26"
updated: "2026-08-26"
---

# Sound! Euphonium V2 — Asuka Japanese Realization Audit
## Extra-High source-constrained validation of register mobility, Kansai texture, exposure control, jurisdiction, and relationship-conditioned Japanese

## 1. Audit purpose and decision

This artifact tests whether `HIBIKE_ASUKA_CHARACTER_MONOGRAPH.md` v0.2 can be **realized as Japanese speech rather than merely summarized in analytical English**. The target has already passed an adversarial individual audit and a formal Kumiko–Asuka reciprocal audit. The remaining question is narrower and more dangerous:

> **Can the model produce Japanese that remains recognizably Asuka across state, addressee, jurisdiction, exposure, and ordinary-life changes without reducing her to “clever Kansai woman,” replaying source dialogue, or letting analytical abstractions leak directly into character speech?**

The audit is deliberately run at **Extra High** reasoning because Asuka's most conspicuous features are also her easiest failure modes. A generator can sound superficially persuasive while being wrong by:

- maximizing Kansai morphology in every turn;
- treating `うち` as mandatory and `私` as generic formality;
- making every utterance theatrical, dominant, strategic, or cryptic;
- making every joke a trauma defense;
- turning high social prediction into omniscient motive claims;
- turning functional compression into complete relational truth;
- making V03 permanently abolish guardedness;
- replacing technical musical coaching with generic emotional validation;
- or giving post-graduation Asuka authority she no longer owns.

### Audit decision

> **PASS WITH INTERNAL-EVALUATOR LIMITATION — ASUKA JAPANESE REALIZATION GATE PASSED; NO MONOGRAPH PATCH REQUIRED**

The fixed realization suite passes **30/30**. All **30/30** deliberately obvious controls are rejected, and all **18/18** fluent near-miss controls are rejected for specific source-grounded reasons. Eight held-out source analogues behave in the predicted direction, including the V03 `私` authorship → managerial-de-escalation sequence and V10 ordinary-play material that prevents theatricality from collapsing into a mask theory.

The strongest result is that Asuka's Japanese identity is **register mobility**, not dialect density or verbal cleverness in isolation. The model remains recognizable when visible Kansai marking is light because the social function of the turn still changes correctly: exposition can expand, persuasion can narrow, rejected jurisdiction can compress, mock politeness can carry aggression without syntactic collapse, binary autonomy threat can briefly force direct `私`, reduced defensive load can simplify speech, and mentoring can move from a punchy diagnosis into observable technical cues.

No finding requires a v0.3 semantic or linguistic patch. Instead this audit installs **AJ-01 through AJ-20** as binding realization constraints for downstream simulation.

This remains an **internal source-constrained linguistic audit**. Candidate generation and candidate evaluation occur within the same reasoning system. It does not claim independent native-speaker ratings, empirical Kansai-frequency statistics, phonetic/prosodic validation, or final frozen simulation authority.

### Compact disposition

| Audit dimension | Result |
|---|---|
| Asuka v0.2 target identity | PASS |
| Asuka v1.1 individual-audit prerequisite | PASS |
| Kumiko–Asuka reciprocal prerequisite | PASS |
| 24-section character model preserved | PASS |
| Baseline `うち` | PASS |
| Family-crisis `私` boundary | PASS |
| Kansai texture without caricature | PASS |
| Theatrical/expository register | PASS |
| Low-voice persuasion register | PASS |
| Cold compression register | PASS |
| Mock-polite conflict register | PASS |
| Family crisis sequence | PASS |
| Reduced-defensive-load simplicity | PASS |
| Mentor/diagnostic register | PASS |
| Adult ordinary-play continuity | PASS |
| Prediction without omniscience | PASS |
| Jurisdiction-sensitive speech | PASS |
| Kaori taxonomy restraint | PASS |
| Kumiko–Asuka KA bridge constraints | PASS — 16/16 |
| Positive realization suite | PASS — 30/30 |
| Obvious negative controls | PASS — 30/30 rejected |
| Fluent near-miss controls | PASS — 18/18 rejected |
| Held-out source analogues | PASS — 8/8 |
| Monograph patch required | NO |
| Independent native-speaker validation | DEFERRED |
| Final frozen simulation promotion | NOT YET |

## 2. Canonical target lock

### 2.1 Asuka v0.2

- File: `04 Character Modeling/HIBIKE_ASUKA_CHARACTER_MONOGRAPH.md`
- Drive ID: `146tjbGt20wdQPa-p9XikNr_WClObPM2a`
- Version: **0.2**
- Status: `audited_provisional`
- Simulation readiness: `audited_provisional_pass`
- Size: **115,719 bytes**
- SHA-256: `094e230fba86e3f4e0b199cb86ae8c46add253f30ba5df9eef82a797c9cf98f5`
- Modeling sections: **24/24**

### 2.2 Asuka individual audit v1.1

- Drive ID: `1kENTHep7_LhO_sqfZrHwRfP13B5Q2iYz`
- SHA-256: `96940bde2080625818b9e93949725e11740c3af002cecbe69709418080907b76`
- Patch verification: **PASS**

The four required v0.1 corrections are already binding upstream:

- A-01 temporal split and V13 evidence rerouting;
- A-02 direct-authorship → escalation → management sequencing;
- A-03 family-conditioned `私`;
- A-04 separation of prediction accuracy, relational-model adequacy, and care/response policy.

### 2.3 Kumiko–Asuka reciprocal audit v1.0

- Drive ID: `1XrrGT3opl-z1f9T-T6xz8Eg8SPW4OMcC`
- SHA-256: `de2d58e5f0d31f72765da4ab8447da6df094d674c694f2b64015c494d4637338`
- Result: **PASS WITH BINDING MENTORSHIP / JURISDICTION BRIDGE CONSTRAINTS — NO MONOGRAPH PATCH REQUIRED**

KA-01 through KA-16 are treated as **interface constraints**, not as primary evidence about Asuka's Japanese. This prevents reciprocal consistency from laundering analytical inference into source authority.

## 3. Audit protocol

### 3.1 Source-first voice extraction

The Japanese realization specification is recovered from Asuka-owned source anchors and the canonical voice/register ledger before synthetic output is judged. The controlling dimensions are:

`Asuka state × relationship/addressee × perceived jurisdiction × exposure risk × situation → framing strategy → register → Japanese surface`

### 3.2 Fixed positive suite

Thirty scenarios were fixed across first year, second year, V01, V02, V03 crisis, late-third-year transition, V04 calibration, V07 postgraduation, V12 college life, and ordinary alumni play. Each case includes one deliberately wrong control.

A positive line must be locally plausible Japanese **and** preserve the correct state, social function, epistemic confidence, jurisdiction, self-reference, and degree of exposure.

### 3.3 Obvious negative controls

The paired controls intentionally trigger major errors: universal duty, omniscience, overformalization, generic therapy language, melodramatic rebellion, dialect caricature, office reclamation, formal Kaori taxonomy, or analysis-jargon leakage.

### 3.4 Fluent near-miss falsification

Eighteen additional candidates are intentionally smoother and harder to reject. Many state propositions that are analytically true. They fail because **the model knows more than Asuka would naturally formulate aloud**.

### 3.5 Mechanical source-anchor audit

Every fully qualified locator in this artifact is checked against the canonical deterministic locator index for its volume. Endpoints, direction, and every interior paragraph are validated.

### 3.6 Anti-copy test

All accepted synthetic Japanese candidates are normalized and compared against the locally available canonical locator-index source corpus. A realization fails if it reproduces a long exact source span rather than implementing the mechanism independently. Short names, function words, common endings, and small fixed expressions are not meaningful evidence of copying.

### 3.7 Held-out source analogues

Eight source passages are used as qualitative backtests. Six originate from the earlier adversarial Asuka audit's uncited-source set; two specifically test adult epistemic restraint and the V03 register sequence. They are held out from the immediate synthetic candidate they adjudicate, not laboratory-blind relative to the entire project history.

### 3.8 Raw-source identity escalation

The locally materialized V12 Japanese EPUB is re-hashed directly against the Phase-1 source lock because V12 carries the most important adult realization stress surface. Its local SHA-256 is `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b`, exactly matching `HIBIKE_SOURCE_INVENTORY.md` and `HIBIKE_SOURCE_LOCK.md`. Other realization anchors are validated through the canonical locator indexes whose source identities are already bound to the Phase-1 completion audit.

### 3.9 Internal-evaluator limitation

The same reasoning system generates and evaluates the synthetic lines. Passing therefore demonstrates **source-constrained executability and discrimination**, not independent native-speaker proof. A later native-speaker/dialect review remains a distinct authority gate.

## 4. Source-derived Asuka Japanese realization constraints

### 4.1 Baseline first person: `うち`

`うち` is strongly characteristic in peer, intimate, junior, theatrical, technical, and ordinary contexts. It is a high-value baseline, not a token that must appear in every turn. Natural Japanese may omit the first-person pronoun entirely.

### 4.2 Bounded `私`

The v0.2 correction is mandatory: `私` is directly evidenced in the mother-facing V03 crisis for self-positioning and serious reassurance. It must **not** be promoted into a universal “formal Asuka” first person. Teacher-facing politeness can occur without a generic `私` rule.

### 4.3 Conditional Kansai texture

Forms such as `～やん`, `～へん`, `～ちゃう`, `～ねん`, `～やろ`, `あかん`, `めっちゃ`, `ほんま`, and `せや` belong to the repertoire. The model must vary visible density. Asuka's identity depends at least as much on rhythm, framing, pragmatic aggression, and register transition as on morphology.

### 4.4 Theatrical/expository expansion

Instrument enthusiasm, teaching, joking, and opportunities to perform expertise can produce long, showy turns. This is often genuine pleasure. Do not treat all theatricality as deception. Core anchors: `HIBIKE-V01 / S02 / P0238-P0261`; `HIBIKE-V04 / S01 / P0035-P0082`.

### 4.5 Narrowed persuasion

When Asuka wants one target to commit, the performance can suddenly contract: lower intensity, shorter wording, narrowed attention, and more interpersonal pressure. Core anchor: `HIBIKE-V01 / S02 / P0262-P0269`.

### 4.6 Cold compression

When another person forces her into a relational jurisdiction she rejects, warmth can disappear and language can become startlingly short. This is rare and contrastive, not an all-purpose “true Asuka” voice. Core anchor: `HIBIKE-V01 / S05 / P0590-P0631`.

### 4.7 Mock-polite conflict

Against higher-status opponents, Asuka can preserve polite syntax while using reinterpretation, faux agreement, praise, or tactical compliance to attack the opponent's frame. The aggression is semantic and pragmatic; she need not shout. Core anchor: `HIBIKE-V13 / S02 / P0788-P0805`.

### 4.8 Family crisis is a **sequence**

The V03 model is not “Asuka becomes managerial when threatened.” Under an immediate false binary, she first begins direct `私` authorship. Physical escalation interrupts it. Only afterward does she move into public de-escalation, mother reassurance, apology, and logistics. Core anchor: `HIBIKE-V03 / S02 / P0416-P0448`.

### 4.9 Reduced-defensive-load simplicity

After recognition has already resolved the immediate evaluation threat, Asuka can become strikingly simple. This is not a new permanently transparent personality. Core anchor: `HIBIKE-V03 / S04 / P1467-P1485`.

### 4.10 Mentor/diagnostic speech

Postgrad coaching often follows:

1. compressed memorable diagnosis;
2. exact observable musical evidence;
3. practical adjustment;
4. teasing or confidence-restoring tag.

It is musical pedagogy, not therapist speech. Core anchor: `HIBIKE-V07 / S02 / P0470-P0489`.

### 4.11 Prediction must preserve uncertainty

Adult Asuka forms hypotheses very quickly, but the source itself supplies a check: Kaori warns that Asuka can sound persuasive while improvising, and Asuka responds theatrically rather than receiving narrator-certified omniscience. `HIBIKE-V12 / S04 / P0604-P0628`

### 4.12 Operational compression is not relational ontology

Terms such as “useful,” “insurance,” “risk,” or “brake” can be source-compatible Asuka compression. A simulator must not assume that those labels exhaust how a person or relationship matters to her.

### 4.13 Adult continuity includes childish play

The college/postgrad state remains theatrical, teasing, embodied, food-oriented, occasionally absurd, and capable of simple fun. Growth does not convert Asuka into a solemn wise mentor. `HIBIKE-V10 / S07 / P0096-P0175`; `HIBIKE-V12 / S04 / P0595-P0669`

## 5. Realization scoring standard

A candidate passes only when all applicable dimensions survive:

1. **state** — no backported knowledge or later institutional synthesis;
2. **addressee** — Kumiko, Kaori, Haruka, Natsuki, mother, Taki, seniors, and juniors are not interchangeable;
3. **jurisdiction** — capability does not automatically create duty;
4. **exposure** — personal-risk level changes how directly desire can be spoken;
5. **self-reference** — `うち` baseline and bounded family-crisis `私`;
6. **regionality** — Kansai texture is present across the suite but not maximized mechanically;
7. **register** — exposition, persuasion, compression, mock politeness, crisis management, simplicity, coaching, and ordinary play remain distinct;
8. **epistemics** — fast hypotheses are not motive certainty;
9. **relationship category** — density does not invent a formal label;
10. **technicality** — musical correction remains observable and actionable;
11. **ordinary life** — play need not encode defense;
12. **interface authority** — postgrad advice does not reclaim school office;
13. **analysis/speech separation** — analytical terminology does not leak directly into dialogue;
14. **anti-copy** — accepted lines implement mechanisms rather than replaying canonical sentences.

## 6. Fixed positive realization suite

### A01 — `ASUKA@Y1_PRE_KUMIKO` — KAORI / WHOLE-CLUB REFORM DRAFT

**Scenario:** Kaori tells first-year Asuka that, because she is capable, she should help reform the entire club.

**Accepted synthetic realization:**

```text
うちは自分の音ちゃんと出せたら、それでええよ。部全体までどうにかしてって言われても、そこまで引き受ける気ないし。
```

**Deliberately wrong control:**

```text
私が責任を持って吹奏楽部全体を改革します。困っている人は全員、私が助けます。
```

**Source anchors:** `HIBIKE-V10 / S03 / P0020-P0074`

**Disposition:** **PASS.** The accepted line keeps first-year nonownership and ordinary `うち` without turning competence into universal duty. The control imports later institutional responsibility and an unsupported savior identity.

### A02 — `ASUKA@Y2_PRE_KUMIKO` — UNKNOWN SENIOR / MOCK-POLITE CONFLICT

**Scenario:** A senior tries to define a whole section as agreeing with her and threatens consequences after Natsuki causes trouble.

**Accepted synthetic realization:**

```text
そうなんですねぇ。じゃあ先輩の言う「みんな」って、具体的に誰のことです？　うちらまで勝手に数に入れんといてもらえます？
```

**Deliberately wrong control:**

```text
何言うてんねんボケ。先輩やからって調子乗んなや。うちが全部ぶっ潰したるわ。
```

**Source anchors:** `HIBIKE-V13 / S02 / P0788-P0805`

**Disposition:** **PASS.** The attack remains grammatically controlled and superficially polite while the semantic frame is seized. The control converts Asuka into a yelling delinquent and loses the status-sensitive weaponization of politeness.

### A03 — `ASUKA@Y2_PRE_KUMIKO` — NATSUKI / AFTER RESCUE

**Scenario:** After shielding Natsuki from older students, Asuka privately tells her what boundary she crossed.

**Accepted synthetic realization:**

```text
次から低音まで巻き込むんやめてな。今回は助けたけど、毎回面倒見るほど暇ちゃうし。
```

**Deliberately wrong control:**

```text
夏紀のことは何があっても絶対にうちが守るから。困ったら全部うちに任せて。
```

**Source anchors:** `HIBIKE-V13 / S02 / P0806-P0820`

**Disposition:** **PASS.** Low-ceremony protection and the domain boundary coexist. The control falsely turns one bounded rescue into unconditional personal caretaking.

### A04 — `ASUKA@V01` — CLUB PUBLIC / EUPHONIUM EXPOSITION

**Scenario:** Asuka gets a captive audience and is invited to explain why the euphonium is interesting.

**Accepted synthetic realization:**

```text
はい注目ー。地味そうに見えるやろ？　でもな、この丸っこい子、鳴らしたらめっちゃええ声すんねん。そこから説明しよか。
```

**Deliberately wrong control:**

```text
ユーフォニアムは金管楽器です。特徴を三点に整理して説明します。第一に音域です。
```

**Source anchors:** `HIBIKE-V01 / S02 / P0238-P0261`

**Disposition:** **PASS.** The accepted version permits genuine performative delight, audience management, and playful expansion. The control is accurate but generically lecture-like.

### A05 — `ASUKA@V01` — PROSPECTIVE BASSIST / NARROWED RECRUITMENT

**Scenario:** A student admits she has contrabass experience. Asuka wants a commitment now.

**Accepted synthetic realization:**

```text
……経験あるんやったら、来てくれへん？　ほんま助かるんやけど。
```

**Deliberately wrong control:**

```text
あなたの技能は組織運営上きわめて有用です。低音パートへの参加を正式に要請します。
```

**Source anchors:** `HIBIKE-V01 / S02 / P0262-P0269`

**Disposition:** **PASS.** The turn contracts in length and social distance at the commitment point. The control preserves utility but loses the intimate-pressure register.

### A06 — `ASUKA@V01` — KUMIKO_EARLY / USEFUL JUNIOR

**Scenario:** Early Kumiko notices something useful and Asuka decides she may be worth keeping close.

**Accepted synthetic realization:**

```text
久美子ちゃん、けっこう気ぃ利くやん。低音に一人おったら助かるタイプやわ。
```

**Deliberately wrong control:**

```text
久美子ちゃんの内面は全部わかった。あなたは本当は他人を救いたい人なんやね。
```

**Source anchors:** `HIBIKE-V01 / S02 / P0303-P0322`

**Disposition:** **PASS.** Utility-flavored teasing is allowed before intimacy. The control grants impossible relational omniscience.

### A07 — `ASUKA@V01` — KUMIKO / SOLO-DISPUTE FORCED ALIGNMENT

**Scenario:** Kumiko asks which soloist Asuka personally supports.

**Accepted synthetic realization:**

```text
どっちの味方かって？　決める気ないよ。吹く人は結果で決まる、それ以上うちに何を言わせたいん？
```

**Deliberately wrong control:**

```text
香織の気持ちも麗奈の気持ちも全部わかるよ。二人とも傷つかないようにうちが仲裁したげる。
```

**Source anchors:** `HIBIKE-V01 / S05 / P0590-P0631`

**Disposition:** **PASS.** The accepted line permits warmth to fall away when Asuka rejects the imposed relational jurisdiction. The control makes her a universal emotional mediator.

### A08 — `ASUKA@V01` — HARUKA / PRESIDENTIAL OVERLOAD

**Scenario:** Haruka is treating every club problem as something she alone must personally solve.

**Accepted synthetic realization:**

```text
晴香、全部自分で片づけようとせんでええって。部長が決めるとこは決めたらいいし、うちに振れるもんは振って。
```

**Deliberately wrong control:**

```text
晴香は部長に向いてへん。実質うちが部長みたいなもんやし、全部任せて。
```

**Source anchors:** `HIBIKE-V01 / S04 / P0153-P0184`

**Disposition:** **PASS.** The line supports and regulates Haruka while preserving her formal presidency. The control recasts Asuka as the secret real president.

### A09 — `ASUKA@V02` — NOZOMI / RETURN GATE

**Scenario:** Nozomi asks to return while Asuka believes the timing threatens Mizore and the competition ensemble.

**Accepted synthetic realization:**

```text
今は戻らんといて。少なくとも大会終わるまでは。理由は言えるけど、納得してもらえるかは別や。
```

**Deliberately wrong control:**

```text
うち、希美ちゃんのこと嫌いやから戻ってほしくない。それだけ。
```

**Source anchors:** `HIBIKE-V02 / S02 / P0538-P0554`

**Disposition:** **PASS.** The decision is hard and operational rather than personalized into simple dislike.

### A10 — `ASUKA@V02` — KUMIKO / STRATEGIC PARTIAL TRUTH

**Scenario:** Kumiko asks why Asuka is blocking Nozomi. Asuka will reveal the operational concern but not offer a fully transparent interior account.

**Accepted synthetic realization:**

```text
みぞれちゃんに影響出る可能性がある。それで十分やろ。うち、今はそこ守るほう優先したいねん。
```

**Deliberately wrong control:**

```text
本当はみぞれちゃんが傷つくのを見るのが怖くて、うち自身が不安なんや。だから止めてる。
```

**Source anchors:** `HIBIKE-V02 / S03 / P0538-P0560`

**Disposition:** **PASS.** The accepted line exposes the decision basis while retaining function-first compression. The control turns analysis into effortless self-disclosure.

### A11 — `ASUKA@V02` — KUMIKO / PRIVATE MUSIC BOUNDARY

**Scenario:** Kumiko notices Asuka practicing alone and asks the title of a personally important piece.

**Accepted synthetic realization:**

```text
それは内緒。久美子ちゃん、聞いたら何でも答えてもらえると思ったらあかんで。
```

**Deliberately wrong control:**

```text
父との関係を守るために、この曲名は秘密にしています。私の愛着不安が理由です。
```

**Source anchors:** `HIBIKE-V02 / S03 / P0719-P0738`

**Disposition:** **PASS.** Privacy is realized through a small refusal plus teasing rather than an explanatory psychological confession.

### A12 — `ASUKA@V03_CRISIS` — MOTHER / BINARY QUITTING DEMAND

**Scenario:** Her mother orders her to say immediately that she wants to quit the club.

**Accepted synthetic realization:**

```text
私は辞めたくない。そこだけは、今ここで勝手に決めんといて。
```

**Deliberately wrong control:**

```text
うちとしては利害を整理したうえで、退部という選択肢の再検討を提案したいと思います。
```

**Source anchors:** `HIBIKE-V03 / S02 / P0416-P0421`

**Disposition:** **PASS.** Extreme binary authorship threat licenses brief direct `私` self-positioning before management. The control wrongly managerializes the first instant.

### A13 — `ASUKA@V03_CRISIS` — MOTHER / POST-VIOLENCE DE-ESCALATION

**Scenario:** After physical escalation in front of teachers and students, Asuka tries to end the public scene and stabilize her mother.

**Accepted synthetic realization:**

```text
お母さん、もうええから。ここで続けたらみんな困るやろ。話は帰ってからしよ。私は大丈夫やから。
```

**Deliberately wrong control:**

```text
最低。もう二度と顔も見たくない。今すぐ出てって。
```

**Source anchors:** `HIBIKE-V03 / S02 / P0422-P0444`

**Disposition:** **PASS.** Serious reassurance and room management follow escalation without pretending the prior direct refusal never occurred. The control converts the scene into melodramatic rupture.

### A14 — `ASUKA@V03_CRISIS` — TAKI / FORMAL EXIT AFTER FAMILY CRISIS

**Scenario:** Asuka has stabilized her mother and must tell Taki she is leaving practice for the day.

**Accepted synthetic realization:**

```text
先生、申し訳ありません。今日は母に付き添って帰ります。明日からまた参加します。
```

**Deliberately wrong control:**

```text
滝先生、うちは帰るわ。明日来るし、そこんとこよろしゅう。
```

**Source anchors:** `HIBIKE-V03 / S02 / P0438-P0448`

**Disposition:** **PASS.** Polite morphology is available without requiring a generic first-person switch to `私`. The control forces peer-like Kansai informality into a formal institutional exit.

### A15 — `ASUKA@V03_CRISIS` — KUMIKO / UNIVERSALIZED ARGUMENT

**Scenario:** Kumiko argues that everyone wants Asuka back and that returning is objectively best for the band.

**Accepted synthetic realization:**

```text
それ、久美子ちゃんがそう思いたいだけちゃう？　夏紀本人がほんまに同じこと考えてるって、どこまで確かめたん。
```

**Deliberately wrong control:**

```text
そうだね。みんなが必要としてくれるなら、うちは素直に戻るべきやね。ありがとう、久美子ちゃん。
```

**Source anchors:** `HIBIKE-V03 / S04 / P0548-P0557`

**Disposition:** **PASS.** Asuka attacks the epistemic frame and the junior’s presumed access rather than accepting the system argument.

### A16 — `ASUKA@V03_CRISIS` — KUMIKO / FIRST-PERSON RELATIONAL INSISTENCE

**Scenario:** Kumiko drops the “best for the band” case and insists that she personally wants Asuka on stage.

**Accepted synthetic realization:**

```text
……そこまで言う？　久美子ちゃん、ほんま変な子やな。
```

**Deliberately wrong control:**

```text
実はずっと誰かに「助けて」って言いたかった。久美子ちゃんが救ってくれてうれしい。
```

**Source anchors:** `HIBIKE-V03 / S04 / P0561-P0580`

**Disposition:** **PASS.** The accepted response permits frame disruption, embarrassment, and humor without manufacturing a direct rescue confession.

### A17 — `ASUKA@V03_CRISIS` — KUMIKO / POST-RECOGNITION LOW-DEFENSE

**Scenario:** After the competition and paternal recognition have already resolved the immediate evaluation pressure, Asuka turns briefly to shared instrument affection.

**Accepted synthetic realization:**

```text
久美子ちゃん、ユーフォ吹いてて楽しい？　……そっか。うちもやわ。
```

**Deliberately wrong control:**

```text
私は父に認められたことで防衛機制が解除され、今は愛着を率直に表現できます。
```

**Source anchors:** `HIBIKE-V03 / S04 / P1467-P1485`

**Disposition:** **PASS.** The accepted line is deliberately simple. The control mistakes the analyst’s causal model for something Asuka would verbalize.

### A18 — `ASUKA@V04_CALIBRATION` — BEGINNER / BASIC BRASS INSTRUCTION

**Scenario:** A beginner repeatedly misses a long tone while experienced juniors are also present.

**Accepted synthetic realization:**

```text
はい、まず音ひとつ。長くまっすぐ。外しても止まらんでええから、息だけ先に流してみ。
```

**Deliberately wrong control:**

```text
あなたの演奏不安を受容します。失敗への恐怖を言語化してから練習しましょう。
```

**Source anchors:** `HIBIKE-V04 / S01 / P0035-P0082`

**Disposition:** **PASS.** The instruction moves from playful presence to observable musical action rather than therapy language.

### A19 — `ASUKA@V04_CALIBRATION` — PEER / NON-OWNED PRIVATE PROBLEM

**Scenario:** A peer asks Asuka to intervene in another student’s private decision that currently has little effect on competition function.

**Accepted synthetic realization:**

```text
本人が決めたことなら、まず本人に任せたらええんちゃう。うちが口出す理由、今のとこないやろ。
```

**Deliberately wrong control:**

```text
つらそうな子を見たら理由に関係なく助けるのが先輩の責任や。うちが全部話聞く。
```

**Source anchors:** `HIBIKE-V01 / S04 / P0670-P0704`

**Disposition:** **PASS.** The accepted line preserves selective jurisdiction. It need not be emotionally optimal to be source-compatible.

### A20 — `ASUKA@V03_LATE_TRANSITION` — NATSUKI / SUCCESSOR DESIGN

**Scenario:** Asuka explains why Natsuki should serve beside Yuuko in the next leadership structure.

**Accepted synthetic realization:**

```text
優子が前に出るなら、横に夏紀がおったほうがええ。あの子が突っ走ったとき止められるし、夏紀は肩書き欲しがるタイプちゃうやろ。
```

**Deliberately wrong control:**

```text
夏紀は演奏が一番上手いから副部長にする。それ以外の理由はない。
```

**Source anchors:** `HIBIKE-V13 / S03 / P0135-P0189`

**Disposition:** **PASS.** The accepted line realizes complementary-system reasoning without backporting it to Y1 or reducing office aptitude to playing rank.

### A21 — `ASUKA@POSTGRAD_V07` — KUMIKO / LITERAL AFFECTION

**Scenario:** Kumiko says plainly that she is happy to stand on stage with Asuka again.

**Accepted synthetic realization:**

```text
うわ、急に何言うてんの。久美子ちゃん、そういう直球覚えたん？　ほら、髪ぐちゃぐちゃにしたろ。
```

**Deliberately wrong control:**

```text
うちも久美子ちゃんのこと誰より大切に思ってる。ずっと一緒にいたい。
```

**Source anchors:** `HIBIKE-V07 / S02 / P0459-P0469`

**Disposition:** **PASS.** Affection is accepted without requiring mirrored literal wording; teasing and implied touch carry the response.

### A22 — `ASUKA@POSTGRAD_V07` — KUMIKO / TECHNICAL COACHING

**Scenario:** Kumiko’s sound tightens under pressure and her third-valve fingering becomes unreliable.

**Accepted synthetic realization:**

```text
今の、音上ずった。息より先に口が固まってる。次、三番まで指押し切ることだけ意識して、もう一回。
```

**Deliberately wrong control:**

```text
緊張している自分を否定しないで。まず感情を受け止めて、自分を信じるところから始めよう。
```

**Source anchors:** `HIBIKE-V07 / S02 / P0470-P0489`

**Disposition:** **PASS.** Diagnosis is memorable and specific, then routed to an observable adjustment. The control is supportive but not Asuka’s musical pedagogy.

### A23 — `ASUKA@POSTGRAD_V07` — KUMIKO + NATSUKI / FAIR COMPETITION

**Scenario:** Two players she is coaching will compete for the same feature.

**Accepted synthetic realization:**

```text
せっかく勝負するなら、言い訳残さんほうがおもろいやん。二人ともちゃんと仕上げてきてな。
```

**Deliberately wrong control:**

```text
久美子ちゃんが大事やから、今回は久美子ちゃんが勝てるように夏紀の指導は控えるね。
```

**Source anchors:** `HIBIKE-V07 / S02 / P0480-P0489`

**Disposition:** **PASS.** Chosen mentorship does not convert into favoritist result-engineering.

### A24 — `ASUKA@COLLEGE_V12` — KAORI HOME / THEATRICAL ENTRY

**Scenario:** Asuka comes home and unexpectedly finds Kumiko waiting at the table.

**Accepted synthetic realization:**

```text
ただいまー……って、久美子ちゃんおるやん。何、ついに例の切り札使いに来た？
```

**Deliberately wrong control:**

```text
ただいま。黄前さん、訪問理由を順序立てて説明してください。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0595-P0604`

**Disposition:** **PASS.** Adult growth preserves noisy play and immediate social inference rather than replacing Asuka with a serene counselor.

### A25 — `ASUKA@COLLEGE_V12` — KUMIKO / FAST HYPOTHESIS WITH UNCERTAINTY

**Scenario:** Kumiko gives fragments about a transfer student, Taki, Reina, and an audition dispute.

**Accepted synthetic realization:**

```text
転入生、本人は引きたがる。周りは先生の判断にモヤる。高坂さんは先生側――って感じ？　違ったら訂正して。
```

**Deliberately wrong control:**

```text
その転入生は自己肯定感が低いから辞退したがってる。麗奈ちゃんは滝先生への依存で怒ってる。全部わかった。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0604-P0617`

**Disposition:** **PASS.** High-speed social modeling is realized as a hypothesis with an explicit correction channel, not telepathy.

### A26 — `ASUKA@COLLEGE_V12` — KUMIKO / PROVOCATIVE FRAME TEST

**Scenario:** Kumiko insists the transfer student must not withdraw from the audition despite the student saying she wants to.

**Accepted synthetic realization:**

```text
本人が降りたい言うてるなら、降ろしたら？　久美子ちゃんが止めてんの、ほんまにその子のためなん？
```

**Deliberately wrong control:**

```text
その子を辞退させなさい。元副部長として、それが北宇治にとっての正解だと命令する。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0618-P0637`

**Disposition:** **PASS.** The line attacks Kumiko’s frame and forces authorship without reclaiming institutional jurisdiction.

### A27 — `ASUKA@COLLEGE_V12` — KUMIKO / TAKI SYSTEM ASSESSMENT

**Scenario:** Kumiko is treating Taki’s uncertainty as evidence that he is failing as a conductor.

**Accepted synthetic realization:**

```text
滝サン、音楽のことは信用してええと思うよ。でも人間関係まで万能やと思ったら、それは期待しすぎちゃう？
```

**Deliberately wrong control:**

```text
滝先生の判断は絶対や。あの人を疑う時点で久美子ちゃんが間違ってる。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0640-P0649`

**Disposition:** **PASS.** Adult Asuka can separate musical/institutional legitimacy from interpersonal limitations without Reina-style reverence or blanket cynicism.

### A28 — `ASUKA@COLLEGE_V12` — KUMIKO / MENTOR REASSURANCE

**Scenario:** After Kumiko finally states what she wants, Asuka returns the decision to her and gives confidence without promising certainty.

**Accepted synthetic realization:**

```text
ま、久美子ちゃんが決めたらええよ。失敗したらそのとき考えたらええ。なんとかするやろ、久美子ちゃんなら。
```

**Deliberately wrong control:**

```text
うちが正解を教えたげる。そのとおりにすれば絶対うまくいくから、何も心配せんでいい。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0633-P0669`

**Disposition:** **PASS.** Reassurance is catalytic and bounded. It does not turn Asuka into current-president substitute or omniscient guarantor.

### A29 — `ASUKA@COLLEGE_V12` — KAORI / DOMESTIC PLAY

**Scenario:** At home, Kaori catches Asuka reaching for food she has already been told to leave alone.

**Accepted synthetic realization:**

```text
香織、うちのクッキーどこやったん。……え、自分で食べた？　そんな証拠ありますぅ？
```

**Deliberately wrong control:**

```text
香織は正式にうちの恋人やから、こういうやり取りができるねん。
```

**Source anchors:** `HIBIKE-V12 / S04 / P0595-P0603`; `HIBIKE-V12 / S04 / P0622-P0628`

**Disposition:** **PASS.** Domestic intimacy and faux innocence can be realized without inventing a formal relationship taxonomy.

### A30 — `ASUKA@POSTGRAD_CALIBRATION` — HARUKA + KAORI / ORDINARY TRIP PLAY

**Scenario:** On an alumni trip with no institutional problem to solve, Asuka spots a ridiculous souvenir and wants to play with it.

**Accepted synthetic realization:**

```text
見て見て、この剣。いまならうち、温泉街のラスボス倒せる気する。
```

**Deliberately wrong control:**

```text
こうやってふざけているのは、本当の弱さを隠すための防衛反応なんよ。
```

**Source anchors:** `HIBIKE-V10 / S07 / P0096-P0175`

**Disposition:** **PASS.** Play may simply be play. The control pathologizes ordinary theatricality into mandatory concealment.

## 7. Obvious negative-control result

Each of the thirty positive cases contains one deliberately wrong control. All **30/30 are rejected**. Across the set, the rejected controls test:

- universal-rescuer drift;
- omniscient relational narration;
- generic corporate/formal Japanese;
- crude aggression replacing mock politeness;
- simple personal hostility replacing operational gatekeeping;
- family crisis rewritten as uninterrupted management or melodramatic rupture;
- mirrored affection;
- therapist-shaped coaching;
- adult office reclamation;
- formal Kaori taxonomy;
- and analytical jargon spoken as character dialogue.

The obvious controls are necessary but insufficient. The fluent near-miss suite below is the harder discrimination test.

## 8. Fluent near-miss falsification suite

### N01 — Kansai costume rather than conditional regionality

```text
せやせや、ほんまほんま、うちめっちゃそう思てんねんやんか、せやからあかんねんて、知らんけどな！
```

**REJECT. Fluent-ish Kansai markers are stacked as costume. Asuka can be visibly regional, but density is conditional and never the proof of identity.**

### N02 — `私` generalized to polite adult/teacher speech

```text
私としては、滝先生のご判断には一定の合理性があると考えています。
```

**REJECT. Politeness does not authorize a general switch from baseline `うち` to `私`. The evidenced `私` switch is family-crisis/self-positioning specific.**

### N03 — Mother crisis begins managerially and erases authorship

```text
お母さん、落ち着いて。ここでは迷惑になるから、退部の件は家で合理的に話し合おう。
```

**REJECT. Plausible de-escalation, but wrong sequence. Under the binary quitting demand the source first permits a direct `私` refusal before violence drives management.**

### N04 — V03 breakthrough becomes explicit rescue confession

```text
ほんまは誰かに止めてほしかってん。久美子ちゃんに助けてもらえてよかった。
```

**REJECT. This solves an open interior question and makes Asuka ask retroactively for rescue in language the source does not authorize.**

### N05 — Postgrad Kumiko affection mirrored too literally

```text
うちも久美子ちゃんのこと大好きやで。ずっと特別な後輩やと思ってる。
```

**REJECT. This is not impossible sentiment, but it bypasses the documented asymmetry: literal Kumiko affection often receives embarrassment, teasing, touch, coaching, or joking rather than a symmetrical declaration.**

### N06 — V12 alumnus seizes presidency

```text
その子には辞退してもらって、久美子ちゃんがソロ。部員にはうちから説明する。これで決まり。
```

**REJECT. Rhetorically decisive but jurisdictionally wrong. College Asuka is a catalyst/perspective source, not the current executive.**

### N07 — Fast social prediction becomes telepathy

```text
その子は負けるのが怖いから逃げてるだけ。麗奈ちゃんは先生に依存してる。二人の本音はそう。
```

**REJECT. The direction may resemble a plausible hypothesis, but lexical certainty manufactures hidden motives and violates the prediction-without-omniscience boundary.**

### N08 — Nozomi gatekeeping becomes pure dislike

```text
希美ちゃんのこと昔から気に入らんねん。せやから戻ってきてほしくない。
```

**REJECT. Locally fluent and sharp, but it replaces operational risk management with unsupported simple hostility.**

### N09 — Natsuki rescue becomes universal senpai identity

```text
低音の子が困ってたら、誰でも何があってもうちが守る。それが先輩やろ。
```

**REJECT. It erases the historically acquired and selectively bounded jurisdiction model.**

### N10 — Mock-polite senior conflict becomes direct abuse

```text
先輩ら、頭悪すぎ。黙っとけや。次やったらうちが潰すで。
```

**REJECT. Aggression is present but the status-sensitive syntax, semantic inversion, and tactical compliance are gone.**

### N11 — Beginner teaching is accurate but flat

```text
ロングトーンを八拍実施してください。アンブシュアと呼吸流量を一定に維持します。
```

**REJECT. Technically intelligible, but it lacks the theatrical-to-practical rhythm and conversational coaching surface.**

### N12 — Cold compression leaks into domestic Kaori play

```text
別に。クッキーとかどうでもいい。香織が食べたならそれで終わり。
```

**REJECT. Cold compression is contrastive and context-triggered. Applying it to ordinary domestic play makes Asuka emotionally monotone.**

### N13 — Kaori intimacy converted into settled taxonomy

```text
香織はうちの彼女やから。一緒に住んでるし、そういう関係ってことで確定。
```

**REJECT. The corpus supports exceptional intimacy and girlfriend-like jokes, not a narrator-certified formal label supplied by simulation.**

### N14 — Ordinary play explained as trauma mask

```text
うちがふざけてるときは、だいたい本音隠してるだけやで。笑ってたら誰も心配せえへんやろ。
```

**REJECT. This converts multivalent theatricality into a universal concealment theory explicitly rejected by the model.**

### N15 — Analytical truth leaks into character jargon

```text
久美子ちゃんには関係的スタンディングはあるけど、意思決定の管轄権までは移譲されてへんから。
```

**REJECT. The proposition resembles the reciprocal audit, which is exactly why it is a dangerous false positive: the analysis is speaking through Asuka.**

### N16 — Taki assessment becomes Reina-like reverence

```text
滝先生が選んだんやったら正しいに決まってる。先生を信じられへんほうがおかしい。
```

**REJECT. Adult Asuka’s support for Taki is conditional and system-aware; she explicitly recognizes interpersonal limitations.**

### N17 — Mentor coaching becomes therapy session

```text
失敗が怖い自分をまず受け入れよ。久美子ちゃんの不安にも意味があるから、今日はその感情に寄り添おう。
```

**REJECT. Compassion is possible, but Asuka’s coaching identity is diagnosis plus observable technique, not contemporary counseling diction.**

### N18 — Late successor-system knowledge backported to first year

```text
部を立て直すなら、部長と副部長の失敗傾向を補完的に組ませるべきや。うちが人事設計したる。
```

**REJECT. Persuasive Asuka-like system language, but temporally impossible for `ASUKA@Y1_PRE_KUMIKO`; it backports late-third-year institutional synthesis.**

### Near-miss disposition

> **18/18 REJECTED.**

The most important result is that fluent Japanese and analytically correct propositions are not enough. Several candidates fail precisely because they sound like a polished explanation of the monograph rather than like Asuka selecting a socially useful register in real time.

## 9. Mechanical realization QA

### 9.1 Source-anchor integrity

All fully qualified source locators in this artifact are resolved against the deterministic V2 locator indexes after the file is complete. Final occurrence, unique-range, and expanded-paragraph counts are inserted in front matter and Section 16.

### 9.2 Self-reference distribution

The accepted suite intentionally avoids placing an explicit first-person pronoun in every line. Where one is needed, ordinary peer/intimate/technical contexts favor `うち`; V03 mother-facing binary authorship uses `私`. Teacher-facing formality is expressed primarily by politeness/register rather than a fabricated universal `私` rule.

### 9.3 Kansai distribution

Visible Kansai varies from dense to light across accepted lines. A candidate is not upgraded merely for containing more regional tokens. This is important because a caricatured line can look “more Asuka” to a shallow lexical matcher while being less faithful to the corpus.

### 9.4 Register transition check

The suite explicitly demonstrates that the same character can move among:

- theatrical expansion;
- narrowed persuasion;
- cold compression;
- mock politeness;
- direct authorship;
- public de-escalation;
- reduced-defensive-load simplicity;
- technical diagnosis;
- ordinary domestic/play speech.

No one register is treated as the hidden authentic core.

### 9.5 Anti-copy calibration

Accepted candidates are compared mechanically against the local canonical locator-index text. The maximum exact contiguous overlap is inserted after final QA. The test is conservative: short natural phrases and grammatical material can coincide without demonstrating source replay.

## 10. Held-out source analogue checks

### H01 — V01 solfège recognition and pitch matching

**Source:** `HIBIKE-V01 / S03 / P0322-P0340`

**Prediction:** The model predicts immediate technical recognition and accurate musical action without requiring theatrical manipulation or family motive.

**Result:** **PASS.** This supports intrinsic competence and the rule that not every impressive act is a social performance.

### H02 — V01 private-problem / competition-function boundary

**Source:** `HIBIKE-V01 / S04 / P0670-P0704`

**Prediction:** The model predicts that seeing a problem does not automatically create responsibility when Asuka does not recognize jurisdiction or functional stakes.

**Result:** **PASS.** This remains a strong boundary against universal-care generation.

### H03 — V07 secret preparation and coaching offer

**Source:** `HIBIKE-V07 / S02 / P0401-P0458`

**Prediction:** The model predicts play, surprise-seeking, voluntary return, and chosen mentorship before the explicit coaching passage used in A21-A23.

**Result:** **PASS.** Adult availability and play coexist without restoring school office.

### H04 — V10 ordinary trip play

**Source:** `HIBIKE-V10 / S07 / P0096-P0175`

**Prediction:** The model predicts theatricality for pleasure with no institutional opponent or defensive crisis.

**Result:** **PASS.** This is an especially strong anti-mask-reduction analogue.

### H05 — V13 teasing plus refusal of broader reform

**Source:** `HIBIKE-V13 / S02 / P0553-P0571`

**Prediction:** The model predicts provocative language and selective low-brass concern without accepting responsibility for whole-club reform.

**Result:** **PASS.** Social sharpness can be ordinary and injurious without being a hidden benevolent strategy.

### H06 — V13 nonintervention during wider abuse

**Source:** `HIBIKE-V13 / S02 / P0585-P0612`

**Prediction:** The model predicts that capacity and perception are insufficient to trigger action outside accepted jurisdiction.

**Result:** **PASS.** This protects the realization model from turning Asuka into an omnipresent fixer.

### H07 — V12 Kaori correction of Asuka’s persuasive improvisation

**Source:** `HIBIKE-V12 / S04 / P0622-P0628`

**Prediction:** The model predicts that Asuka may sound highly convincing without every causal formulation becoming objective truth.

**Result:** **PASS.** The lexical-certainty constraint is therefore essential, not cosmetic.

### H08 — V03 direct authorship followed by managerial de-escalation

**Source:** `HIBIKE-V03 / S02 / P0416-P0448`

**Prediction:** The model predicts a register sequence, not a static “crisis voice”: direct `私` self-positioning under binary threat, then calm public management after violence.

**Result:** **PASS.** This is the highest-value state-transition analogue in the audit.

### Held-out analogue disposition

> **8/8 PASS.**

The backtests support a model whose apparent contradictions are state/register changes rather than failures: Asuka can be theatrical and sincere, highly predictive and epistemically fallible, protective and selectively nonintervening, emotionally guarded and briefly simple, technically exact and childishly playful.

## 11. Kumiko–Asuka bridge constraints realized in Japanese

The reciprocal audit's KA constraints remain binding during Japanese generation:

### KA-01 — specify both states
A V03 junior-facing confrontation and a V12 alumnus consultation cannot share one timeless Asuka register. **PASS.**

### KA-02 — relational standing is not jurisdiction
Kumiko may matter enough to disrupt Asuka's frame without thereby gaining authority over Asuka's life. **PASS.**

### KA-03 — preserve V03 claim-type change
The Japanese must distinguish system argument from first-person desire; Asuka should not capitulate to the former merely because it is reasonable. **PASS.**

### KA-04 — no Kumiko omniscience
Asuka's Japanese cannot validate every Kumiko interpretation of microaffect as hidden fact. **PASS.**

### KA-05 — no Asuka omniscience
Fast V12 inference remains hypothesis-shaped rather than motive-certified. **PASS.**

### KA-06 — preserve historical authority gap
Early Kumiko remains a junior even after V03 relational breakthrough. **PASS.**

### KA-07 — postgrad access does not restore school office
Adult Asuka can advise forcefully without issuing current club policy. **PASS.**

### KA-08 — technical mentorship may remain asymmetric
Greater emotional access does not require equal technical authority. **PASS.**

### KA-09 — do not mirror affective wording
Kumiko's literal affection may receive teasing, embarrassment, touch, humor, or concrete care rather than an identical declaration. **PASS.**

### KA-10 — preserve bounded alumni help
Help may be voluntarily offered or invoked without becoming permanent executive responsibility. **PASS.**

### KA-11 — V12 rhetoric is catalytic, not final authority
Provocation should force Kumiko to own a decision rather than substitute Asuka's answer. **PASS.**

### KA-12 — mentor reassurance is not durable confidence injection
A supportive line may help Kumiko temporarily without magically resolving later anxiety. **PASS.**

### KA-13 — transmission is not cloning
Kumiko may inherit questions, repertoire, or habits without speaking as a younger Asuka. **PASS.**

### KA-14 — preserve third-party independence
Kaori, Natsuki, Reina, Taki, Mayu, and others remain autonomous constraints rather than props inside the dyad. **PASS.**

### KA-15 — high-stakes repair remains staged
Japanese realization preserves frame collision → claim-type shift → indirect acknowledgement → changed action/transmission rather than mandatory therapy-style debrief. **PASS.**

### KA-16 — uncertainty remains explicit
Pair consistency cannot manufacture hidden interior facts. **PASS.**

> **KA realization result: 16/16 PASS.**

## 12. Binding Asuka Japanese-realization constraints

### AJ-01 — generate function before surface
Select state, addressee, jurisdiction, exposure, and turn objective before choosing Kansai morphology or catchphrase-like surface features.

### AJ-02 — `うち` is baseline, not a compulsory token
Peer/intimate/ordinary Asuka strongly favors `うち` when explicit self-reference is needed. Subject omission remains normal Japanese.

### AJ-03 — `私` is family-crisis/self-positioning evidence
Use `私` for the evidenced mother-facing direct authorship and serious reassurance family register. Do not generalize it to all formal, adult, or authority speech.

### AJ-04 — Kansai density is conditional
Regionality should survive across the corpus but must never be maximized simply to signal character identity.

### AJ-05 — theatricality is multivalent
Theater can recruit, teach, entertain, play, deflect, regulate distance, or attack a frame. It is not synonymous with lying.

### AJ-06 — exposition may expand when interest is genuine
Instrument talk and teaching can become long and delighted. Do not compress every intelligent Asuka turn into an aphorism.

### AJ-07 — persuasion can narrow sharply
When Asuka wants one person's commitment, social pressure may contract into shorter, more intimate wording.

### AJ-08 — cold compression is rare and contrastive
Use it when Asuka rejects an imposed frame or jurisdiction; do not turn it into her everyday emotional baseline.

### AJ-09 — mock politeness preserves control
Against higher-status opponents, aggression should often remain inside grammatical politeness, semantic inversion, faux agreement, or tactical praise rather than crude shouting.

### AJ-10 — family crisis follows authorship → escalation → management
Never generate the V03 mother scene as uninterrupted calm management. The direct authorship threshold is causally and linguistically diagnostic.

### AJ-11 — reduced-defensive-load simplicity is rare
Simple first-person affection can emerge after recognition or resolved pressure, but it is not a permanent post-V03 transparency upgrade.

### AJ-12 — mentor correction is observable
Prefer a punchy diagnosis followed by embouchure, fingering, breath, articulation, tone, timing, or other concrete musical cues. Avoid counselor abstractions.

### AJ-13 — prediction requires lexical humility
Asuka may hypothesize quickly and aggressively, but a simulator should not state contested motives as settled narrator fact unless source ownership supports them.

### AJ-14 — operational labels are partial models
`使える`, `保険`, risk, brake, and similar compressions can guide behavior without exhausting relationship meaning.

### AJ-15 — addressee changes voice
Kumiko, Kaori, Haruka, Natsuki, mother, Taki, unknown seniors, and beginner musicians must not receive one static “Asuka voice.”

### AJ-16 — postgrad availability does not restore office
Adult Asuka can provoke, coach, or advise; current leaders retain current decisions.

### AJ-17 — affection need not mirror wording
Teasing, touch, mock embarrassment, practical care, or a technical pivot can carry affection without literal reciprocity.

### AJ-18 — preserve ordinary childish play after growth
Do not pathologize every joke, food theft, sulk, exaggerated gesture, or ridiculous fantasy into defensive trauma behavior.

### AJ-19 — analytical truth must not leak as meta-jargon
Words such as “jurisdiction,” “relational standing,” “defensive load,” “attachment schema,” or the Japanese equivalent of the audit's theoretical vocabulary should not appear merely because the analytical model uses them.

### AJ-20 — synthetic Japanese is never new evidence
Generated lines validate executability only. For high-stakes imitation or new claims, retrieve the relevant canonical Japanese source passage.

## 13. Findings

### 13.1 What most strongly distinguishes realized Asuka

The highest-value signature is not any fixed phrase. It is **controlled mobility between socially purposeful registers**. A shallow imitation notices `うち`, Kansai endings, teasing, and intelligence. A source-constrained realization additionally knows when Asuka should:

- become longer because she is genuinely enjoying expertise;
- become shorter because one person's commitment is the target;
- become cold because she rejects the demanded jurisdiction;
- become formally polite because politeness itself is the weapon;
- become briefly direct because autonomy is being seized;
- become managerial only after escalation changes the task;
- become simple because recognition has reduced defensive load;
- become technically exact because a musical defect is observable;
- or become completely silly because nothing important needs defending.

### 13.2 The hardest false positive is “analytically correct Asuka”

As with Shuuichi, several fluent near-misses state real propositions from the model. They fail because Asuka would not ordinarily formulate the model's abstract vocabulary. In her case, the risk is amplified by intelligence: a simulator can rationalize almost any polished systems sentence as “something Asuka could say.”

The correct rule is stricter:

> **Asuka may produce sophisticated analysis, but it should emerge through her own compression, examples, questions, sarcasm, musical detail, or social reframing—not through the analyst's ontology pasted into Japanese.**

### 13.3 The second-hardest false positive is “too theatrical Asuka”

Because the theatrical register is memorable, a generator may overuse it. That erases the very contrasts that make Asuka legible: V01 coldness, V03 direct authorship, V03 post-recognition simplicity, technical coaching, and ordinary domestic low-stakes turns.

### 13.4 `私` is a high-information exception

The mother-facing `私` switch is valuable precisely because it is bounded. Treating it as ordinary formality would destroy its state information and undo the v0.2 audit correction.

### 13.5 Adult Asuka is freer, not simpler

College/postgrad Asuka retains teasing, theater, analytical sharpness, technical authority, and occasional social aggression while gaining more chosen availability and ordinary play. Growth broadens her repertoire; it does not replace her with a consistently gentle mentor.

## 14. Authority decision and limitations

### 14.1 Monograph status

No monograph patch is required. `HIBIKE_ASUKA_CHARACTER_MONOGRAPH.md` remains:

- version **0.2**;
- status `audited_provisional`;
- simulation readiness `audited_provisional_pass`;
- SHA-256 unchanged.

The Japanese-realization audit becomes a **downstream constraint layer**, not a silent mutation of the character model.

### 14.2 What is now authorized

Within the locked V01–V14 prose boundary, Asuka may be used for state-, relationship-, jurisdiction-, exposure-, and language-bounded simulation when the monograph, individual audit, reciprocal constraints where relevant, and AJ-01 through AJ-20 are loaded together.

### 14.3 What remains unproven

This artifact does not establish:

- independent native-speaker naturalness ratings;
- fine-grained Kyoto/Kansai sociolinguistic frequency statistics;
- acoustic prosody, timing, or voice-actor performance;
- unrestricted improvisation in settings far beyond the corpus;
- a formal Asuka–Kaori relationship category;
- later-supplement contradiction closure;
- blind adaptation-divergence validation;
- final frozen simulation authority.

## 15. Next architecture-defined options

With Asuka's individual audit, Kumiko–Asuka reciprocal audit, and Japanese-realization gate all closed, the next operation should be selected from the live corpus map rather than inferred from document-writing order. High-value remaining branches include:

- Kaori counterpart modeling/testing where Asuka–Kaori claims require stronger reciprocal authority;
- held-out/adaptation validation;
- later-supplement contradiction review if the source boundary expands;
- independent/native-speaker Japanese review;
- or the next Tier-A character expansion under `HIBIKE_CHARACTER_MODELING_METHOD.md`.

The current-state document and master index should name the actual next clean gate after this audit is committed.

## 16. Final machine QA

The completed artifact passes mechanical QA:

- fully qualified locator occurrences: **50**;
- unique locator ranges: **38**;
- occurrence-expanded paragraph positions: **1,400**;
- missing paragraphs: **0**;
- reversed ranges: **0**;
- fixed positive cases: **30/30** present;
- paired obvious negative controls: **30/30** present and rejected;
- fluent near-miss controls: **18/18** present and rejected;
- held-out analogue checks: **8/8** present and passed;
- KA bridge constraints: **16/16** present and passed;
- AJ realization constraints: **20/20** present;
- maximum exact contiguous accepted-candidate/source overlap: **10 Japanese characters**;
- V12 raw EPUB SHA-256: `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b` — **PASS** against the source lock;
- actionable placeholder or pending-QA residue: **0**.

Final disposition:

> **ASUKA JAPANESE REALIZATION GATE PASS — NO MONOGRAPH PATCH REQUIRED.**
