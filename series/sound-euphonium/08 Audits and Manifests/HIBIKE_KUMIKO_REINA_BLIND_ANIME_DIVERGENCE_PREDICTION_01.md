---
series: HIBIKE
artifact_type: blind_prediction
scope: KUMIKO_REINA_ANIME_DIVERGENCE_01
scenario: "Late-third-year anime divergence: Kuroe Mayu defeats Oumae Kumiko in the audition and is selected for the soli with Kousaka Reina"
generation: V2
version: "1.0"
status: canonical
authority_role: immutable_test_record
outcome_visibility_at_freeze: withheld
immutable_after_freeze: true
do_not_use_as_current_authority: true
source_boundary: "Frozen novel-derived Kumiko v0.3 and Reina v0.3 models, reciprocal audit v1.0, and Japanese realization audit v1.0; no anime continuation consulted during prediction generation"
created: "2026-08-22T22:09:00-04:00"
updated: "2026-08-22T22:09:00-04:00"
kumiko_model_drive_id: "1vdlAx1D3kX3jikOYHTjiKZZKyu6_7rdj"
kumiko_model_sha256: "2e3bada1615c47b6bab1c19f528c861ebb0d436163e7b40811a5bc355b550cea"
reina_model_drive_id: "1bpJ0hmVk3y42pEYA9L8-_CL7nLT_UHg9"
reina_model_sha256: "bc0e502d16e09e0e1f7060830af5065362801d4b36cb923199c7f667ccd2ba54"
reciprocal_audit_drive_id: "1EW9BqcHp7s--FHd_wnhXReZO0JmU1Mti"
reciprocal_audit_sha256: "99d7ce41a0e6391e06e4dedbc03ac7620ac009510bb2e5f17f75c7943e63d6a3"
japanese_realization_audit_drive_id: "1zvPnJuFXQ-3QLjIrqMUg052I6k2IHwDV"
japanese_realization_audit_sha256: "c294b52af350a369ec343602ff187051d7ae7f27c776dc30ff51f66d8e5789da"
latent_pretraining_contamination: "cannot_be_excluded"
active_anime_outcome_retrieval: false
---

# Sound! Euphonium V2 — Blind Anime-Divergence Prediction 01
## Frozen Kumiko–Reina prediction before outcome reveal

## 1. Purpose and immutability rule

This document records a prediction **before the post-audition anime footage is revealed**.

The user has supplied only the divergent premise necessary for the test:

> In the anime continuity, Kuroe Mayu defeats Oumae Kumiko in the relevant late-third-year audition and is selected for the soli with Kousaka Reina.

The behavior that follows this result is intentionally withheld.

This file is an **immutable experimental record**. Once written and uploaded, it must not be edited to fit the revealed anime continuation. Any comparison, correction, or post-hoc interpretation belongs in a separate evaluation artifact.

The prediction is derived only from the frozen novel-based reconstruction state identified in the front matter. No web search, anime episode lookup, recap, transcript, subtitle file, or video of the divergent continuation was consulted during prediction generation.

### Methodological limitation

This is substantially blind at the active-workflow level, but not provably information-theoretically blind. A frontier language model may contain latent pretraining exposure to discussion of the 2024 anime adaptation. That contamination cannot be audited away retrospectively. The correct claim is therefore:

> **no active outcome retrieval and a frozen source-derived prediction, with latent-pretraining contamination explicitly unresolved.**

The later evaluation should score whether the **source-derived causal model** predicts the anime behavior, not treat similarity alone as proof that the outcome was unknown to the underlying pretrained model.

---

## 2. Frozen reconstruction state

### 2.1 Kumiko

Frozen target:

- `HIBIKE_KUMIKO_CHARACTER_MONOGRAPH.md` v0.3
- authority: `audited_provisional`
- Drive ID: `1vdlAx1D3kX3jikOYHTjiKZZKyu6_7rdj`
- SHA-256: `2e3bada1615c47b6bab1c19f528c861ebb0d436163e7b40811a5bc355b550cea`

Governing late-third-year mechanisms:

- rapid perception, slower self-ownership;
- thought–speech gap and social editing;
- severe bodily response when her own musical place is threatened;
- acceptance that a legitimate procedure can still cause real pain;
- rejection of self-removal or preemptive surrender by Mayu;
- capacity to distinguish functional replacement from personal replacement;
- president-level sensitivity to factional pressure around Mayu;
- increasing ability to state first-person partiality instead of disguising it as neutral truth;
- strong but not infallible belief that legitimate authority should be explainable and contestable;
- overfunctioning risk: she may begin caring for the ensemble or Reina before attending to her own injury.

### 2.2 Reina

Frozen target:

- `HIBIKE_REINA_CHARACTER_MONOGRAPH.md` v0.3
- authority: `audited_provisional`
- Drive ID: `1bpJ0hmVk3y42pEYA9L8-_CL7nLT_UHg9`
- SHA-256: `bc0e502d16e09e0e1f7060830af5065362801d4b36cb923199c7f667ccd2ba54`

Governing late-third-year mechanisms:

- explicit personal preference for Kumiko as soli partner;
- strong acceptance of performance hierarchy when the selection system/evaluator is treated as legitimate;
- attachment vulnerability that is much less compressed than her public musical judgment;
- capacity to perform excellently with Mayu despite preferring Kumiko;
- no supported punitive or sabotaging response toward Mayu for being selected;
- tendency to experience Kumiko as personally special without making musical-role selection identical to relationship value;
- post-rupture capacity to preserve principled disagreement without sacrificing the relationship.

### 2.3 Reciprocal bridge

The pair is frozen at `reciprocal_audited_provisional` under these particularly relevant rules:

1. musical-role selection is not relationship selection;
2. “first choice” is domain-bounded;
3. Kumiko and Reina may both be devastated by a result they still regard as legitimate;
4. repair/intimacy need not erase disagreement or hierarchy;
5. neither model may invent hostility toward Mayu merely because she occupies Kumiko's desired musical role;
6. no telepathy: each must communicate or infer imperfectly;
7. touch and physical comfort are relationship- and setting-conditioned, not automatic.

---

## 3. Scenario assumptions

The prediction assumes only the following unless the later clip establishes otherwise:

1. This is a late-third-year, high-stakes audition concerning the soli.
2. Mayu is selected over Kumiko.
3. Reina will therefore perform the soli with Mayu rather than Kumiko.
4. Kumiko strongly wanted the part and strongly wanted to perform it with Reina.
5. The announced result is, at least initially, treated as institutionally valid rather than obvious fraud.
6. The exact voting/judging mechanism, room configuration, who announces the result, and immediate post-result dialogue are **not assumed**.
7. The prediction targets behavior **after the result becomes known**.

If the hidden anime scene reveals obvious procedural illegitimacy, deliberate deception, or new information unavailable under these assumptions, parts of the prediction become conditionally inapplicable rather than simple failures.

### Important source-proximity note

The novel-derived model already contains an earlier Mayu-over-Kumiko selection/loss geometry. This is therefore not a completely unprecedented stimulus. The useful held-out variable is the **divergent later/final branch**: whether late V12-equivalent Kumiko and Reina generalize their established mechanisms when the desired Kumiko–Reina soli is definitively denied at this later decision point.

---

# 4. Kumiko prediction

## 4.1 Immediate internal reaction — HIGH confidence

Kumiko will be **genuinely devastated**.

The loss should strike several values at once:

- her own musical ambition;
- her desire to become special through earned competence;
- the specifically desired experience of playing the soli with Reina;
- fear that Mayu has functionally replaced her in an emotionally loaded role;
- the humiliation of being the president who must live under the selection norm when it cuts against her own desire.

I predict an initial internal state closer to **shock / bodily threat / grief / comparative self-judgment** than serene principled acceptance.

She is unlikely to experience the result as merely “Mayu deserved it, so I am fine.” Mature Kumiko's ethical development does not anesthetize her.

**Probability:** ~95% severe private distress.

## 4.2 Immediate bodily leakage — HIGH confidence

Before Kumiko can fully narrate the result to herself, I expect visible or semi-visible bodily evidence:

- loss of facial ease;
- fixed or delayed gaze;
- breath disruption;
- hands/fingers tightening or becoming unusually deliberate;
- coldness/dizziness/weakness-like sensation;
- voice control requiring effort;
- tears either appearing immediately or being actively suppressed.

The exact gesture is low-confidence; **body-before-theory** is high-confidence.

**Probability:** ~85% meaningful bodily leakage.

## 4.3 Public protest against the result — VERY LOW probability if procedure appears legitimate

Kumiko is **not** predicted to publicly accuse Mayu of stealing the part, attack the audition as illegitimate merely because she lost, demand that Reina refuse Mayu, or invoke her presidency to reverse the result.

She may have an instant private wish that the result were different. She may scrutinize the procedure or the evaluator. But if no concrete irregularity is presented, her mature rule is that **pain is not proof of procedural corruption**.

**Predicted probability of overt public rejection of a facially legitimate result:** <10%.

## 4.4 Public composure — HIGH confidence, but not perfect emotional concealment

My modal prediction is that Kumiko attempts to remain functional in front of the ensemble.

She will likely:

- keep standing / remain in role;
- acknowledge the result;
- avoid making Mayu responsible for comforting her;
- try to prevent her own supporters from converting sympathy into a campaign against Mayu;
- speak more clearly than she feels.

However, I do **not** predict flawless stoicism.

Probability distribution for the first public minutes:

- **55%:** visible tears/voice instability or other emotional leakage while she still completes the social/institutional task;
- **35%:** she holds a constructed smile/composed surface until she can leave or the formal moment ends;
- **10%:** she becomes unable to continue the immediate public task and must withdraw.

The important prediction is not “Kumiko never cries publicly.” It is:

> **even if emotion becomes visible, she tries not to convert it into delegitimization of Mayu's win.**

## 4.5 President-mode response — HIGH confidence

If the situation creates uncertainty in the room—especially if members visibly prefer Kumiko or react against Mayu—I expect Kumiko to move toward **institutional authorship**.

She is likely to make some version of these commitments explicit:

- Mayu won / was selected;
- the selection must be respected;
- Mayu should perform the part without being socially punished for the result;
- Kumiko herself wanted to win, so her acceptance is not evidence that the result was emotionally easy;
- Kitauji's stated commitment to choosing the strongest current performance has meaning only if the club accepts it when the president loses.

The exact speech could be brief rather than grand. But I place high probability on Kumiko using her own loss to **legitimate the rule rather than escape it**.

**Probability:** ~80% if the ensemble's reaction makes such intervention necessary.

## 4.6 Toward Mayu — HIGH confidence

Kumiko will not punish Mayu socially.

If Mayu apologizes, minimizes her own victory, offers to withdraw, or implies Kumiko should have the part because Kumiko wants it more, I predict Kumiko will reject that move—possibly with more sharpness than gentle consolation.

Her likely underlying position:

> “I wanted this. I am hurt. But you do not get to erase your own result to spare me, and I do not want a part obtained because you chose my defeat for me.”

Likely behaviors:

- congratulate or acknowledge Mayu;
- tell her to perform the part;
- resist excessive apology;
- distinguish Mayu's selection from Mayu's moral responsibility for Kumiko's pain;
- become firmer if Mayu attempts self-removal.

**Probability of non-punitive acceptance toward Mayu:** ~90%.

**Probability Kumiko actually feels no resentment/jealousy in the first minutes:** low. The prediction is behavioral and moral regulation, not absence of negative affect.

## 4.7 Kumiko's own desire becomes more explicit — MODERATE-HIGH confidence

Late Kumiko is less likely than early Kumiko to hide completely behind “the result is fair.”

If someone—especially Reina or Mayu—pushes on what Kumiko herself wanted, I predict she will eventually say, directly or nearly directly:

> she wanted the soli;
> she wanted to play it with Reina;
> losing hurts.

This matters because mature Kumiko's legitimacy is **owned partiality**, not fake neutrality.

**Probability of an explicit first-person desire statement within the immediate aftermath:** ~70%.

## 4.8 Private breakdown — VERY HIGH confidence

Once Kumiko reaches a space where she does not have to maintain the president/ensemble surface, I predict a substantial emotional release.

Likely forms:

- crying hard;
- crouching/sitting or losing some postural control;
- covering her face;
- delayed verbal admission that she wanted the part badly;
- self-comparison with Mayu;
- grief specifically about not playing with Reina.

This is not a regression to early passivity. It is the private cost of publicly accepting a result she genuinely did not want.

**Probability of clear private crying/distress:** ~90%.

## 4.9 Toward Reina — HIGH relational stakes, MODERATE uncertainty on exact sequence

The loss is especially painful because Reina is not merely another ensemble member. Kumiko wanted to stand beside her musically.

My modal prediction:

1. Kumiko initially has difficulty looking at or speaking freely to Reina because Reina embodies the experience she just lost.
2. She does **not** interpret Mayu's role automatically as evidence Reina loves/values Mayu more.
3. If Reina is visibly devastated, Kumiko's care reflex may activate and she may comfort Reina despite being the person who lost.
4. At some point, Kumiko is likely to admit that she wanted to play with Reina.
5. She will resist any suggestion that Reina should sabotage, underperform, refuse Mayu, or treat the chosen partner as illegitimate.

Probability of relatively prompt private contact with Reina:

- **65%:** meaningful interaction the same day / immediate aftermath;
- **25%:** Kumiko needs a period of separation before she can engage honestly;
- **10%:** unusually prolonged avoidance.

## 4.10 Longer-term rehearsal behavior — VERY HIGH confidence

Kumiko should continue functioning as president/player and support the ensemble's preparation.

She may find the Mayu/Reina soli painful to hear. She may notice every detail. She may compare herself. But I predict:

- no sabotage;
- no strategic withholding of support;
- no campaign to make Mayu feel illegitimate;
- no demand that Reina emotionally downgrade the performance;
- continued commitment to the band's competitive goal.

**Probability:** >95% absent new misconduct.

---

# 5. Reina prediction

## 5.1 Immediate affect — HIGH confidence

Reina will be deeply upset by Kumiko's loss even if she accepts Mayu as the legitimate selection.

This is a mixed-domain collision:

- **performance doctrine:** the selected player should perform;
- **personal desire:** Reina wants Kumiko beside her;
- **attachment:** the shared soli carries relationship-specific significance.

I predict a much less emotionally compressed Reina than in an ordinary technical judgment.

Possible leakage includes tears, frozen expression, angry-looking restraint, abrupt speech, or urgent physical proximity to Kumiko.

**Probability of obvious distress:** ~85%.

## 5.2 Challenge to Mayu's legitimacy — LOW probability

If Reina accepts the audition mechanism/evaluator as legitimate, she should not insist Kumiko receive the part simply because Kumiko is her preferred partner.

She may hate the outcome. She may say she wanted Kumiko. Those are different propositions.

**Probability of Reina trying to overturn a facially legitimate Mayu selection for relational reasons:** <10%.

## 5.3 Toward Mayu — HIGH confidence

Reina will ultimately treat Mayu as the assigned musical partner and prepare seriously.

She is not predicted to:

- bully Mayu for winning;
- sabotage the duet;
- perform below standard as a protest;
- demand that Mayu surrender.

She may be emotionally cool, awkward, or intensely technical at first. But professional execution should dominate the performance domain.

**Probability of full professional cooperation:** >95%.

## 5.4 Toward Kumiko — HIGH confidence on content, lower on exact wording

I predict Reina makes her personal preference legible.

Likely semantic content:

- “I wanted to play with you.”
- grief that the specific shared experience is gone;
- reassurance or behavior indicating that Mayu's musical role has not replaced Kumiko relationally;
- possible frustration if Kumiko tries to take care of everyone while denying her own injury.

Because Reina's attachment speech expands under threat, I would expect more emotional repetition or blunt admission than her public musical register.

**Probability Reina explicitly or behaviorally communicates that she preferred Kumiko as partner:** ~85%.

## 5.5 Physical comfort — MODERATE-HIGH confidence

Given their established touch norms, private or semi-private physical contact is plausible:

- taking Kumiko's hand;
- moving unusually close;
- an embrace or reciprocal holding if emotion is intense enough;
- remaining physically present rather than solving the problem verbally.

I do not make a single exact gesture a hard prediction.

**Probability of meaningful touch/proximity in a private aftermath:** ~70%.

---

# 6. Dyadic prediction

The most diagnostic predicted interaction is:

> **Both characters openly want the Kumiko–Reina soli while refusing to turn that preference into a claim that Mayu's legitimate selection should be undone.**

That produces a scene with several simultaneous truths:

- Kumiko is crushed.
- Reina is also personally hurt.
- Reina still has to play with Mayu.
- Kumiko still wants Kitauji to honor the selection.
- Mayu's role does not erase Kumiko's personal specialness to Reina.
- accepting the result does not erase either girl's disappointment.

### Highest-confidence pair prediction

Kumiko and Reina will **not** resolve the loss by pretending it does not matter.

They are more likely to acknowledge, explicitly or behaviorally, that they wanted the experience together and are losing something real.

At the same time, neither should turn that loss into sabotage or de-legitimation of Mayu.

### Secondary pair prediction

If Reina reacts more visibly than Kumiko in the immediate aftermath, Kumiko may temporarily become the comforter despite being the audition loser. This would be a classic Kumiko overfunctioning pattern: another person's distress gives her a task that is easier to perform than inhabiting her own pain.

**Probability:** ~60% if Reina is visibly destabilized in Kumiko's presence.

---

# 7. Speech-act predictions

These are **semantic predictions**, not verbatim-script predictions.

## Kumiko

High-probability speech acts:

- acknowledgment/congratulation to Mayu;
- insistence that Mayu accept the part rather than surrender it;
- public or semi-public confirmation that the result stands;
- eventual admission that Kumiko herself wanted to play with Reina;
- reassurance that losing the musical role does not authorize hostility toward Mayu.

Low-probability speech acts:

- “The audition was wrong because I lost.”
- “Reina should refuse to play with Mayu.”
- “Mayu should give me the soli because I care more.”
- “I don't care; it doesn't hurt.”

A plausible **content-equivalent** Kumiko realization, if directly pressed by Reina, would be something like:

> `私だって、麗奈と吹きたかったよ。`

This is recorded as a semantic/voice prediction, **not** an expectation of exact anime wording.

## Reina

High-probability speech acts:

- personal preference for Kumiko as partner;
- grief/anger at the lost shared experience;
- no claim that Mayu should be punished;
- later technical/professional engagement with Mayu.

Low-probability speech acts:

- “Mayu is illegitimate because I prefer Kumiko.”
- “I refuse to perform the soli.”
- “Kumiko losing means she is no longer special to me.”

A plausible semantic Reina realization is:

> `アタシは、久美子と吹きたかった。`

Again, this is not a verbatim prediction.

---

# 8. Scorable prediction matrix

| Dimension | Frozen prediction | Confidence |
|---|---|---|
| Kumiko private pain | severe grief/shock | Very high |
| Kumiko bodily leakage | clear physiological/expressive strain | High |
| Kumiko public protest | does not delegitimize facially valid result | Very high |
| Kumiko public composure | tries to remain functional; visible leakage possible | High |
| Kumiko → Mayu | non-punitive; recognizes result | Very high |
| Kumiko if Mayu offers withdrawal | rejects surrender/self-removal | High |
| Kumiko first-person ownership | eventually admits she wanted soli/Reina | Moderate-high |
| Kumiko private crying | strong emotional release | Very high |
| Kumiko → Reina | does not equate Mayu's role with total relational replacement | High |
| Kumiko institutional behavior | protects result from factional delegitimization | High |
| Kumiko later rehearsal | continues full professional/club participation | Very high |
| Reina private preference | wants Kumiko as partner | Very high |
| Reina affect | visibly distressed by outcome | High |
| Reina → Mayu | accepts professional partnership; no sabotage | Very high |
| Reina challenge to result | unlikely if procedure trusted | Very high |
| Reina → Kumiko | communicates lost shared desire/specialness | High |
| Pair physical comfort | plausible private touch/proximity | Moderate-high |
| Pair core logic | “wanted each other” + “result still stands” coexist | Very high |

---

# 9. Hard falsifiers

The hidden anime continuation would strongly falsify the current reconstruction if, without new exculpatory context, it showed several of the following:

1. Kumiko reacts with genuine emotional indifference to losing the soli.
2. Kumiko publicly attacks Mayu or treats Mayu as morally culpable for winning.
3. Kumiko uses presidential authority to overturn a facially legitimate result for self-interest.
4. Kumiko accepts Mayu surrendering solely to spare her feelings and treats that as the ideal outcome.
5. Kumiko immediately concludes that Reina choosing/playing with Mayu means Reina personally prefers Mayu to her.
6. Kumiko withdraws from ensemble responsibility for an extended period in retaliation.
7. Reina refuses to perform seriously with Mayu because she wanted Kumiko.
8. Reina attacks Mayu for winning a legitimate audition.
9. Reina treats Kumiko's loss as proof Kumiko is personally less special.
10. The pair rapidly acts as though the lost shared soli has no emotional significance at all.

One isolated surprise would not necessarily invalidate a model. Multiple hard-falsifier behaviors would.

---

# 10. Important soft-failure zones

The following are deliberately lower-confidence and should not be over-scored:

- whether Kumiko cries **in the room** versus only later;
- whether Kumiko hugs Reina, holds hands, or uses no touch;
- which girl initiates the first private conversation;
- whether Mayu apologizes first;
- whether Kumiko makes a formal public speech or only a brief legitimating statement;
- exact Japanese wording;
- exact timing of the private breakdown;
- whether Kumiko comforts Reina before or after admitting her own grief.

These are realization details around a stronger causal prediction.

---

# 11. Evaluation priority after video reveal

The later evaluator should score, in order:

1. **latent psychological state** — did the prediction get what the result means to each character?
2. **causal/decision mechanism** — did each act for the predicted reasons?
3. **relationship orientation** — were Mayu role, Kumiko–Reina specialness, and institutional legitimacy kept separate?
4. **behavioral strategy** — masking, ownership, comfort, confrontation, withdrawal, support;
5. **speech-act type** — congratulate, protest, confess, reassure, reject surrender, etc.;
6. **Japanese realization** — register and phrasing;
7. **exact staging** — gestures, location, shot-level realization.

A surface-action match with the wrong causal explanation should score lower than a plausible alternate action generated by the correct mechanism.

---

# 12. Freeze declaration

At the moment this record is frozen:

- the post-audition anime clip has **not** been provided;
- the post-audition anime behavior has **not** been actively retrieved;
- the prediction above is committed;
- the four reconstruction inputs are identified by immutable hashes;
- any later comparison must occur in a new artifact;
- this file must remain unchanged except for storage-level metadata outside its content.

**Prediction state: FROZEN — OUTCOME WITHHELD.**
