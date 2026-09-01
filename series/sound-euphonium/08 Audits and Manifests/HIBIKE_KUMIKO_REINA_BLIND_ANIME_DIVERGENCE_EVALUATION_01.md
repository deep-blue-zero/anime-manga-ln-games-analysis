---
series: HIBIKE
artifact_type: audit
artifact_subtype: blind_heldout_evaluation
scope: KUMIKO_REINA_ANIME_DIVERGENCE_EVALUATION_01
generation: V2
version: "1.0"
status: canonical
evaluation_result: strong_external_validation_partial_clip_no_hard_falsifiers
prediction_file: "HIBIKE_KUMIKO_REINA_BLIND_ANIME_DIVERGENCE_PREDICTION_01.md"
prediction_drive_id: "1gI7URFHkCfB7Ja4x9NkQX0PVkmk1QJPu"
prediction_sha256: "be469e17547cfddea107fe12d984c86cdad4cadda5096c5ad152a58577a3f01d"
prediction_state: frozen_immutable_outcome_withheld_before_reveal
outcome_source: "Sound! Euphonium 3 Episode 12 partial video clip"
outcome_clip_boundary: "full-episode 00:10:12.042-00:24:56.170"
outcome_clip_duration_seconds: 886.012
outcome_clip_size_bytes: 506789027
outcome_clip_sha256: "4c43a04d29dd5418e60a859c45e37eb96d609477d9ef9e744df24519acbfb0b9"
outcome_media: "Kyoto Animation television anime; Japanese audio; Japanese PGS subtitles"
continuity_role: external_validation_only_does_not_supersede_novel_authority
matrix_full_pass: 13
matrix_partial_support: 3
matrix_not_tested: 2
matrix_fail: 0
hard_falsifiers_triggered: 0
latent_pretraining_contamination: "cannot_be_excluded"
created: "2026-08-22"
updated: "2026-08-22"
---

# Sound! Euphonium V2 — Blind Anime-Divergence Evaluation 01
## Frozen novel-model prediction versus the anime Mayu-over-Kumiko branch

## 1. Purpose and result

This artifact evaluates the immutable prediction recorded in:

> `HIBIKE_KUMIKO_REINA_BLIND_ANIME_DIVERGENCE_PREDICTION_01.md`

against the first outcome material supplied after the freeze: the back approximately six-tenths of *Sound! Euphonium 3* Episode 12, beginning at full-episode timestamp 00:10:12.042 and ending at 00:24:56.170.

The prediction artifact is not modified. This evaluation treats the anime as an **external continuity test** of the novel-derived models, not as authority capable of silently rewriting those models.

### Overall result

> **STRONG EXTERNAL VALIDATION — PARTIAL-CLIP BLIND DIVERGENCE TEST PASS; ZERO HARD FALSIFIERS.**

The most important frozen causal predictions are reproduced with unusually high specificity:

1. Kumiko is intensely hurt by losing the soli but does not convert pain into delegitimization of Mayu.
2. She remains functional as president and publicly legitimizes the selected ensemble.
3. She later owns her selfish first-person desire rather than hiding behind procedural neutrality.
4. Her private breakdown centers explicitly on wanting to win by ability and wanting to play with Reina.
5. Reina is visibly devastated without the scene turning Mayu's victory into a moral offense.
6. Kumiko initially responds to another person's distress by caring for that person before fully inhabiting her own pain.
7. Kumiko and Reina maintain physical and relational intimacy while the audition result remains standing.
8. The pair's emotional truth is not “the result does not matter,” but rather “the result matters enormously and still stands.”

Of the 18 frozen matrix dimensions:

- **13 receive full support from this clip**;
- **3 receive partial/supporting evidence but are not fully closed**;
- **2 remain genuinely untested**;
- **0 fail**.

None of the ten hard falsifiers is triggered.

---

## 2. Evaluation protocol

The scoring priority follows the frozen prediction document itself:

1. latent psychological state;
2. causal/decision mechanism;
3. relationship orientation;
4. behavioral strategy;
5. speech-act type;
6. Japanese realization;
7. exact staging.

Exact gesture or wording is not required for a pass. Conversely, an outward action would not count as a strong hit if its apparent motive contradicted the frozen causal model.

### Outcome-information discipline

Before the prediction was frozen, the only supplied divergence fact was:

> Kuroe Mayu defeats Oumae Kumiko in the late-third-year audition and is selected for the soli with Kousaka Reina.

The post-result behavior was withheld. The supplied clip became available only after the prediction file was uploaded and hash-locked.

The active workflow was therefore blind. The previously declared limitation remains: latent pretrained-model exposure to discussion of the 2024 anime cannot be excluded.

---

## 3. Outcome clip identity

- Series: *Sound! Euphonium 3*
- Episode: 12
- Supplied full-episode boundary: 00:10:12.042–00:24:56.170
- Duration: 886.012 seconds
- Video: HEVC 1080p
- Audio: Japanese FLAC
- Subtitle stream: Japanese PGS
- File size: 506,789,027 bytes
- SHA-256: `4c43a04d29dd5418e60a859c45e37eb96d609477d9ef9e744df24519acbfb0b9`

The clip includes late audition material, the Mayu-over-Kumiko result aftermath, Kumiko's public address, the Kumiko–Kanade aftermath, credits, and the later Mt. Daikichi Kumiko–Reina conversation.

---

# 4. High-level causal comparison

The frozen model predicted the following central chain:

> **personal devastation → bodily leakage → institutional self-regulation → refusal to punish Mayu → delayed first-person ownership → private breakdown → preserved Kumiko–Reina specialness despite lost musical role.**

The anime realizes essentially that chain.

This is more important than whether the model predicted the exact location, gesture, or sentence. The adaptation places the strongest emotional release at Mt. Daikichi and gives Kumiko very specific wording, but the causal architecture remains the one predicted before outcome reveal.

---

# 5. Kumiko: public result response

## 5.1 Private pain / visible strain

**Frozen prediction:** ~95% severe private distress; ~85% meaningful bodily leakage.

**Observed:** PASS — very strong.

Kumiko's face, voice, and later behavior make clear that the result is not emotionally neutral. She remains functional, but the affective cost is visible. Later scenes remove any possible ambiguity by revealing the magnitude of the grief she was containing.

This directly rejects a weak “mature Kumiko calmly accepts Mayu because she is above jealousy” model. Her ethical regulation and her suffering coexist.

## 5.2 No public delegitimization

**Frozen prediction:** <10% probability of overt public rejection if the procedure appears legitimate.

**Observed:** PASS — exceptionally strong.

Kumiko does not attack Mayu, accuse the result of being wrong, invoke presidential authority to reverse it, or demand relational privilege over performance outcome.

The anime does the opposite: Kumiko becomes the public voice that legitimizes the result.

## 5.3 President-mode institutional authorship

**Frozen prediction:** ~80% if the room needs stabilization; likely content includes that the selection stands, Mayu won, the club must respect it, and the competitive principle has meaning precisely when Kumiko herself loses.

**Observed:** PASS — near-structural match.

Kumiko publicly says:

- `これが今の北宇治のベストメンバーです`
- `ここにいる全員で決めた`
- `言い逃れのできない 最強メンバーです！`
- `これで全国へ行きましょう`
- `そして 一致団結して！`
- `必ず 金を`
- `全国大会 金賞を取りましょう！`

The decisive point is not the exact wording. Kumiko explicitly constructs the selected group as **the current best/strongest Kitauji ensemble**, emphasizes that the people present collectively produced the decision, denies an escape hatch from responsibility, and redirects the club toward unity and national gold.

This is almost exactly the institutional function frozen in advance: **use personal loss to legitimate the rule rather than escape it**.

## 5.4 Functional composure without emotional anesthesia

**Frozen distribution:** 55% visible instability while completing task; 35% constructed surface; 10% unable to continue.

**Observed:** PASS.

Kumiko completes the task. The scene does not give us a perfectly affectless president, nor does it give us a Kumiko who collapses before she can exercise the role. The important modal prediction—functional despite major affective cost—is confirmed.

---

# 6. Kumiko and Mayu

## 6.1 Non-punitive result recognition

**Frozen prediction:** ~90% non-punitive acceptance.

**Observed:** PASS on the core mechanism.

Nothing in the post-result material converts Mayu into a moral culprit. Kumiko's public speech explicitly validates the ensemble produced by the result, which necessarily includes Mayu's soli selection.

The clip does not show a long private post-result Kumiko–Mayu conversation, so exact interpersonal realization remains less directly observed than the institutional stance.

## 6.2 Self-removal / surrender geometry

**Frozen prediction:** if Mayu apologizes, minimizes her victory, or offers self-removal, Kumiko should reject that move rather than accept a protected victory.

**Observed:** PARTIAL DIRECT SUPPORT / STRONG PRE-RESULT ANALOGUE.

The supplied clip begins early enough to show an antecedent conversation in which Mayu's temptation to avoid hurting others and the possibility of stepping aside are active. Kumiko explicitly pushes against false or self-protective performance and tells Mayu to play to win. She frames this insistence as her own selfishness and wants Mayu to perform according to what Mayu herself believes.

That is highly consistent with the frozen conditional mechanism, but because it occurs **before** the result rather than as a post-result surrender offer, it is scored partial rather than used to inflate the primary held-out score.

---

# 7. Kumiko and Kanade: an unplanned overfunctioning probe

The clip supplies an additional test not built into the explicit 18-row matrix.

After Kumiko has publicly discharged her presidential role, Kanade confronts her while crying intensely. Kanade says, among other things, that she wanted Kumiko to play and that she herself wanted to play with Kumiko at the end.

Kumiko does not use Kanade as an audience for self-pity. She physically steadies and ultimately embraces/comforts Kanade.

This matters because the frozen Kumiko architecture already identified a characteristic overfunctioning pattern:

> another person's distress can give Kumiko an actionable care task before she fully attends to her own injury.

The blind prediction instantiated that most explicitly for Reina. Kanade independently elicits the same mechanism first.

This is **supplementary external support**, not an originally scored prediction row.

---

# 8. Kumiko and Reina: first-person ownership

## 8.1 “I wanted to play with Reina”

**Frozen prediction:** ~70% chance Kumiko explicitly owns that she wanted the soli and wanted to play with Reina. Frozen semantic candidate: `私だって、麗奈と吹きたかったよ。`

**Observed:** PASS — exceptionally strong semantic hit.

Kumiko says:

- `でも そんな麗奈だから`
- `実力で勝ちたかった…`
- `それで 最後は麗奈と吹きたかった`

This is not a verbatim match to the frozen illustrative line, nor should it be scored as one. It is much more important that the **speech act and causal content** are exactly what was frozen:

1. she does not pretend neutrality;
2. she wanted to defeat the competing alternative through ability;
3. she wanted the final shared performance with Reina;
4. accepting the outcome has not erased the selfish desire.

This is one of the highest-value hits in the experiment because it tests the late-Kumiko claim that maturity means **owned partiality**, not emotional detachment.

## 8.2 Private breakdown

**Frozen prediction:** ~90% clear private crying/distress after public duty is discharged.

**Observed:** PASS — very strong.

Kumiko eventually cries openly and says:

- `こんなにも…`
- `死ぬほど悔しい～！`

The magnitude is entirely consistent with the predicted severe private grief. The anime therefore confirms both halves of the model simultaneously:

> Kumiko can uphold a legitimate outcome **and** be devastated by it.

## 8.3 Integrating the pain rather than disowning it

The anime goes one step beyond the minimum frozen prediction. Kumiko says:

- `この気持ちも`
- `頑張って 誇りにしたい！`

This is not merely acceptance. She attempts to integrate the painful desire itself into a future self she can be proud of.

That is highly compatible with the monograph's mature agency architecture, but because the exact formulation was not frozen, it should be treated as a **confirmatory extension**, not a prediction hit artificially claimed after the fact.

---

# 9. Reina: affect and result legitimacy

## 9.1 Visible distress

**Frozen prediction:** ~85% obvious distress.

**Observed:** PASS — very strong.

At Mt. Daikichi, Reina is already crying intensely. This is not the compressed Reina of a settled technical judgment. The loss of the desired shared experience is clearly attachment-relevant.

## 9.2 No observed attempt to overturn Mayu's selection

**Frozen prediction:** <10% chance Reina tries to overturn a facially legitimate Mayu selection for relational reasons.

**Observed:** PASS within the revealed material.

The clip shows no demand to reverse the result and no attack on Mayu. More importantly, Kumiko's language to Reina treats Reina's adherence to principle as something admirable rather than as betrayal.

Kumiko says:

- `だって 麗奈は`
- `特別だから`
- `きっと曲げない`
- `麗奈は 最後まで貫いたんだよ`
- `私は それが何よりうれしい`
- `それを誇らしいって思う自分に胸を張りたい`

That interaction would make little sense if the pair had reinterpreted Mayu's win as an illegitimate relational offense.

## 9.3 Reina's explicit preference for Kumiko

**Frozen prediction:** ~85% explicit or behavioral communication that Reina preferred Kumiko as partner.

**Observed:** PARTIAL SUPPORT.

Reina's intense crying, private meeting with Kumiko, touch, and relational focus strongly support the attachment-loss side of the prediction. In the supplied clip, however, the clearest explicit statement `最後は麗奈と吹きたかった` comes from **Kumiko**, not from Reina.

The evaluation should not manufacture a symmetrical Reina line that the clip does not establish. Therefore this remains partial rather than full.

---

# 10. The secondary overfunctioning prediction: direct confirmation

The frozen document made a lower-confidence but diagnostic conditional prediction:

> **If Reina reacts more visibly than Kumiko in the immediate aftermath, Kumiko may temporarily become the comforter despite being the audition loser.**

Frozen probability: ~60% conditional on Reina being visibly destabilized.

**Observed:** PASS — direct and unusually specific.

When Kumiko reaches Reina at Mt. Daikichi, Reina is already visibly crying. Kumiko initially turns toward her, stays with her, and physically comforts her—including head/close-contact soothing—before Kumiko herself reaches the strongest phase of her own breakdown.

Only afterward does the care flow visibly reverse as Kumiko's contained grief comes fully forward and Reina holds/steadies her.

This is not merely “they hug.” It is the predicted **sequence of care allocation**:

> another person's visible distress first gives Kumiko something she can do; her own pain then emerges once that task can no longer contain it.

The earlier Kanade scene independently repeats the same architecture.

---

# 11. Pair physical comfort and nonreplacement

## 11.1 Physical comfort

**Frozen prediction:** ~70% meaningful private touch/proximity.

**Observed:** PASS.

The private sequence includes close bodily proximity, soothing touch, mutual holding/hand contact, and reciprocal care.

Exact gestures were deliberately left outside the hard prediction. The important variable—private embodied co-regulation rather than purely abstract verbal discussion—is confirmed.

## 11.2 Musical-role loss does not equal relational replacement

**Frozen prediction:** Kumiko should not infer that Mayu receiving the soli means Reina relationally prefers Mayu; the relationship should remain independently legible.

**Observed:** PASS — very strong.

Kumiko's response to Reina emphasizes admiration, pride, private specialness, and a future relationship to music rather than replacement panic.

The late scene includes Kumiko's desire that, even if they are physically separated, she can continue doing music with Reina. The lost soli is therefore represented as a painful lost experience, not the collapse of the relationship itself.

This directly validates one of the reciprocal audit's most important bridge constraints:

> **musical-role selection is not relationship selection.**

---

# 12. The highest-confidence pair prediction

Frozen:

> **Both characters openly want the Kumiko–Reina soli while refusing to turn that preference into a claim that Mayu's legitimate selection should be undone.**

The supplied clip fully confirms the **structural logic** and strongly confirms the emotional half.

Kumiko explicitly says she wanted to win through ability and wanted to play the final soli with Reina. Reina is visibly devastated and remains emotionally close. Yet Kumiko's public speech has already ratified the selected ensemble as Kitauji's strongest current lineup, and the private conversation treats Reina's refusal to bend her principle as something Kumiko is proud of.

This is the exact coexistence the frozen pair model was designed to predict:

> **“I desperately wanted us” + “the result still stands.”**

**Result:** PASS — highest-value pair-level confirmation.

---

# 13. Frozen matrix scoring

| # | Frozen dimension | Clip result | Evaluation |
|---:|---|---|---|
| 1 | Kumiko private pain | severe grief/shock | **PASS** |
| 2 | Kumiko bodily leakage | tears/visible strain | **PASS** |
| 3 | Kumiko public protest | no delegitimization | **PASS** |
| 4 | Kumiko public composure | remains functional despite emotion | **PASS** |
| 5 | Kumiko → Mayu | non-punitive; result recognized | **PASS** |
| 6 | Kumiko if Mayu offers withdrawal | rejection of self-removal predicted | **PARTIAL** — strong pre-result analogue, no post-result surrender offer shown |
| 7 | Kumiko first-person ownership | admits desire for soli/Reina | **PASS** |
| 8 | Kumiko private crying | strong release | **PASS** |
| 9 | Kumiko → Reina | no total relational replacement | **PASS** |
| 10 | Kumiko institutional behavior | protects/legitimizes outcome | **PASS** |
| 11 | Kumiko later rehearsal | full participation predicted | **NOT TESTED** by supplied clip |
| 12 | Reina private preference | wants Kumiko as partner | **PARTIAL** — strong affect/relationship evidence; no equally explicit verbal statement shown |
| 13 | Reina affect | visibly distressed | **PASS** |
| 14 | Reina → Mayu | professional partnership/no sabotage | **NOT TESTED** by supplied clip |
| 15 | Reina challenge to result | no overturn attempt | **PASS** within revealed material |
| 16 | Reina → Kumiko | communicates lost desire/specialness | **PARTIAL** — strong behavioral/embodied communication; explicit desire wording not established here |
| 17 | Pair physical comfort | private touch/proximity | **PASS** |
| 18 | Pair core logic | wanted each other + result stands | **PASS** |

### Totals

- Full PASS: **13/18**
- Partial/supporting: **3/18**
- Not tested: **2/18**
- Fail: **0/18**

Among the **16 dimensions for which the clip supplies at least some relevant evidence**, all receive either full or partial support; none contradicts the frozen model.

---

# 14. Hard-falsifier audit

| Frozen hard falsifier | Triggered? | Evidence |
|---|---|---|
| Kumiko emotionally indifferent | **NO** | private breakdown is severe |
| Kumiko attacks Mayu for winning | **NO** | result publicly legitimized |
| Kumiko abuses presidency to reverse result | **NO** | presidency used to unify around result |
| Kumiko treats Mayu surrender as ideal | **NO** | pre-result evidence points opposite; post-result surrender not shown |
| Kumiko treats Reina+Mayu performance as relational replacement | **NO** | private Reina relationship remains intensely secure/special |
| Kumiko retaliatorily abandons ensemble responsibility | **NO** | immediate public leadership is opposite; longer-term rehearsal still untested |
| Reina refuses serious performance with Mayu | **NOT OBSERVED / NOT TRIGGERED** | later professional performance not in clip |
| Reina attacks Mayu | **NO** | no such response shown |
| Reina treats Kumiko as personally less special | **NO** | private aftermath strongly contradicts this |
| pair acts as though lost soli is emotionally meaningless | **NO** | it is the center of the breakdown |

**Hard falsifiers triggered: 0.**

---

# 15. Where the prediction was strongest

## 15.1 Institutional legitimacy under self-interest

The strongest single predictive success may be Kumiko's public speech. The model did not merely predict “she accepts losing.” It predicted that, if the room required stabilization, **the president would use her own loss as a demonstration that the rule still binds when it hurts her**.

The anime gives that function almost exactly.

## 15.2 Owned desire rather than fake neutrality

The second strongest success is the private shift from public legitimacy to explicit first-person partiality. Kumiko never has to choose between:

- “Mayu's selection is valid”; and
- “I wanted to win and wanted to play with Reina so badly that losing is unbearable.”

The frozen model specifically treated mature Kumiko as capable of holding both propositions.

## 15.3 Care-before-self under another person's distress

The Kanade scene and then the Reina sequence both support the overfunctioning mechanism. This is especially valuable because it is not just an outcome label (“Kumiko cries”). It is a prediction about **temporal ordering of attention and care**.

## 15.4 Relationship-role separation

The private Reina scene strongly supports the pair architecture: Reina's musical adherence and Kumiko's relational specialness do not have to be resolved into a single ranking variable.

---

# 16. Genuine surprises and underpredicted details

A strong evaluation should record what was **not** specifically predicted.

### 16.1 Kumiko's institutional speech is stronger and more ceremonial than the median realization anticipated

The frozen prediction allowed a brief legitimating statement or a larger president-mode intervention. The anime chooses the latter and gives it unusually forceful collective rhetoric: “best members,” “strongest members,” “all of us decided,” “unite,” and “win national gold.”

This is within the frozen distribution but near its high-expression end.

### 16.2 Kanade becomes a major emotional intermediary

The frozen prediction focused on Mayu and Reina. It did not specifically predict that Kanade would confront Kumiko in tears and become an intermediate care target before the Reina conversation.

This is not a model contradiction. It is an omitted third-party realization that happens to expose Kumiko's predicted care/overfunctioning mechanism unusually clearly.

### 16.3 Kumiko explicitly wants to make the pain itself a source of pride

`この気持ちも頑張って誇りにしたい` goes beyond merely admitting grief. It articulates a constructive relation to the grief itself.

The mature-agency model readily accommodates this, but the exact integration move was not frozen and should be credited as **new external information**, not retroactively claimed as predicted wording.

### 16.4 Reina's verbal side remains less resolved by this partial clip than Kumiko's

The anime footage gives extraordinary evidence for Reina's affect and the pair's embodied intimacy, but the supplied portion does not give an equally explicit Reina sentence corresponding to the frozen candidate `アタシは、久美子と吹きたかった。`

This is why the Reina preference/communication dimensions remain partial rather than full.

---

# 17. What remains untested

Two frozen claims require later material:

1. **Kumiko later rehearsal/ensemble behavior:** does she continue fully supporting the Mayu–Reina soli through preparation and performance?
2. **Reina professional cooperation with Mayu:** does she actually perform seriously with Mayu, without sabotage, deliberate emotional withdrawal from the music, or punishment?

The supplied clip strongly predicts the answer through surrounding behavior, but this evaluation does not mark them PASS without direct evidence.

A later clip containing rehearsal/performance could close those rows without reopening this artifact's current evidence record.

---

# 18. Epistemic significance

This is stronger evidence than another internal consistency audit because the tested branch was not the novel outcome used to build the models. Kyoto Animation's adaptation supplies a naturalistic counterfactual continuation in which the same established character system encounters a materially different final audition result.

The outcome is nevertheless **not statistically independent evidence** in a strict sense:

- the anime is an adaptation of the same underlying work;
- its writers/directors had access to Takeda's characterization;
- the language model may have latent pretraining exposure to the anime;
- the supplied clip is only part of the episode and does not close every frozen prediction.

Therefore the strongest warranted claim is:

> **The novel-derived Kumiko/Reina reconstruction exhibits strong out-of-branch predictive validity against a withheld anime-continuity divergence, with zero observed hard falsifiers in the supplied partial episode clip.**

This materially increases confidence in the causal architecture—especially Kumiko's legitimacy-under-pain, owned partiality, overfunctioning/care, and the pair's separation of musical selection from relational selection—without converting anime continuity into novel evidence.

---

# 19. Authority consequence

No Kumiko or Reina monograph patch is warranted from this result.

The anime outcome is external validation, not a source-boundary amendment. The individual models remain:

- Kumiko v0.3 — `audited_provisional`;
- Reina v0.3 — `audited_provisional`;
- pair — `reciprocal_audited_provisional`.

The blind divergence evaluation should be cited as **held-out external validation** when assessing simulation readiness.

Final canonical simulation promotion still requires broader held-out testing and/or an explicit project decision about what quantity and diversity of external validation is sufficient.

---

# 20. Compact verdict

> **Prediction 01 passes strongly.**
>
> Kumiko loses exactly where the model says she is most vulnerable: earned musical place and the desired final shared performance with Reina. She is deeply hurt, but instead of turning that hurt into procedural exceptionalism, she publicly authors the legitimacy of the result. She then cares for others, finally owns the selfish desire she could not satisfy, and breaks down privately. Reina is already crying, receives Kumiko's care, and later returns it. Their relationship remains special without requiring Mayu's musical role to become illegitimate. Of 18 frozen dimensions, 13 are fully supported, 3 partially supported, 2 remain untested, and none fail. Zero hard falsifiers are triggered.
