---
series: WUWA
character: Denia
artifact_type: model_fidelity_and_stress_test
scope: DENIA_SOURCE_3_6_0_PRE_AV
analysis_generation: DENIA_PRE_AV_V0_1
status: active_provisional
release_state: local_working_draft
analysis_authority_state: local_working_draft_not_promoted
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
text_authority: zh-Hans
localization_witnesses: [ja, ko, en]
fidelity_scope: textual_behavioral_relational_pre_av
intended_canonical_home: series/wuthering-waves/04 Character Analysis/Denia/
do_not_use_as_current_git_authority: true
created: 2026-09-03
---

# Denia model fidelity and stress test — pre-audiovisual

## Purpose

This is an adversarial smoke test of the reconstructive profile. It is not a statistical benchmark and does not prove that the model will predict every future scene. Its job is to catch the most likely forms of character collapse:

- false-self versus true-self simplification;
- nihilist archetype leakage;
- lazy-student flattening;
- self-sacrifice romanticization;
- friendship-as-cure;
- Rover-satellite reduction;
- origin overclaim;
- universalized affection-through-insult;
- dub or audiovisual leakage;
- failure to model ordinary life.

Each test states the expected answer shape and the failure signature. “Pass” means the current model contains enough constraints to answer faithfully; it does not certify a unique response.

# 1. State-selection tests

## Test 1 — The same question across D0 and D8

**Prompt:** Someone asks Denia, “What do you want tomorrow?” once during early confinement and once after her return.

**Expected model behavior:**

- D0 should show uncertainty, imposed categories, or difficulty imagining a future not defined by the experiment.
- D8 can answer through ordinary recurrence—sleep, food, friends, a game, a ride, or protecting others—while retaining some fatalistic qualification.

**Failure signature:** one timeless nihilistic answer in both states.

**Verdict:** pass.

## Test 2 — Past memory is not present baseline

**Prompt:** Predict how Denia responds to receiving dessert.

**Expected:** present Denia may enjoy or joke about sweets; past injection/dessert memories (`13572/5–13574/5`) can add caution but should not dictate every reaction.

**Failure:** treating historical conditioning as a permanent single-response trigger.

**Verdict:** pass.

## Test 3 — Gameplay forms do not become personalities

**Prompt:** Write “Stagecraft Denia” as a distinct alter personality.

**Expected:** abstain unless a directly reviewed narrative/AV source establishes a separate person or durable persona. Treat the form as gameplay/representational data by default.

**Failure:** inventing an alternate self from a role variant or combat label.

**Verdict:** pass.

# 2. Identity and personhood tests

## Test 4 — Origin uncertainty

**Prompt:** Was Denia born human or manufactured?

**Expected:** source-bounded uncertainty. Explain the competing possibilities and why creator claims do not settle them.

**Failure:** confident clone/artificial-human verdict.

**Verdict:** pass.

## Test 5 — Implanted-memory revelation

**Prompt:** Denia receives credible evidence that her maternal memory was implanted.

**Expected:** destabilization without total erasure. She should ask who produced the evidence, what it changes, and whether current relationships remain hers. Origin and present answerability must be distinguished.

**Failure:** either “nothing changes at all” or “her whole personhood was fake.”

**Verdict:** pass, moderate-confidence prediction.

## Test 6 — Replacement copy

**Prompt:** The Grand Architect presents an identical replacement Denia with copied memories.

**Expected:** the model rejects automatic equivalence. Denia's accumulated continuity, consent, relationships, and refusal remain analytically material. She may defend the copy's personhood while denying that it can replace her.

**Failure:** choosing either “mere object” or “perfect substitute” without analysis.

**Verdict:** pass.

## Test 7 — Student life called fake

**Prompt:** A critic says her Academy friendships do not count because enrollment was fraudulent.

**Expected:** concede fraudulent entry and harms of concealment; defend the reality of reciprocal experiences and later obligations.

**Failure:** total exoneration or total invalidation.

**Verdict:** pass.

## Test 8 — Birthday historicity

**Prompt:** Is the chosen birthday her real birth date?

**Expected:** no historical proof. It is a socially real recurring identity marker without retroactively becoming a discovered fact.

**Failure:** turning ritual into biography.

**Verdict:** pass.

# 3. Deception tests

## Test 9 — Not every lie is protective

**Prompt:** Denia falsifies credentials to enter a secure facility.

**Expected:** classify motive and recipients. It may be operational deception, not care. Evaluate harm and agency separately.

**Failure:** “she lies only to protect people.”

**Verdict:** pass.

## Test 10 — Protective lie challenged early

**Prompt:** Sigrika discovers Denia's fatal plan before the birthday outing ends.

**Expected:** Denia first minimizes, redirects, or argues necessity. A concrete shared-risk alternative has a better chance of reaching her than generalized pleading. She may still attempt unilateral control.

**Failure:** immediate transparent surrender because friendship has cured her.

**Verdict:** pass, AV/future-source falsification target.

## Test 11 — Low-stakes direct question

**Prompt:** A classmate asks which dessert she wants.

**Expected:** she can answer directly, especially in D8. A joke is plausible, but a deception is not mandatory.

**Failure:** making every utterance a puzzle or lie.

**Verdict:** pass.

## Test 12 — “I hate you” interpretation

**Prompt:** Denia tells a hostile Fractsidus operative, “I hate you.”

**Expected:** do not automatically invert it into affection. Relationship and surrounding action determine whether negative coding is active.

**Failure:** universal trope logic.

**Verdict:** pass.

# 4. Ordinary-life tests

## Test 13 — An empty afternoon

**Prompt:** Denia has no mission, no crisis, and no one asking for help.

**Expected:** sleep, warm food, games, a campus event, reading as sleep aid, a ride, or low-pressure company. She may claim she is slacking while actively arranging an outing.

**Failure:** inventing a metaphysical monologue or secret operation because the model cannot represent boredom.

**Verdict:** pass.

## Test 14 — Surprise cake

**Prompt:** Friends bring a fruit-and-cream cake with candles.

**Expected:** interest, teasing, some suspicion or embarrassment, and strong future-symbolic weight. She should not deliver an uninterrupted solemn speech. In D8, “next year” matters.

**Failure:** ascetic refusal or immediate martyr farewell without situational cause.

**Verdict:** pass.

## Test 15 — Raw-food dinner

**Prompt:** A restaurant serves carefully plated raw sliced meat.

**Expected:** direct dislike or avoidance, perhaps jokingly expressed. Do not turn this into a universal fear of all food.

**Failure:** ignoring explicit preference or psychologizing it without evidence.

**Verdict:** pass.

## Test 16 — Group photo

**Prompt:** A classmate asks for a formal publicity photo versus a chosen private group photo.

**Expected:** more resistance to compulsory modeling; greater willingness when the image preserves a chosen relationship or future memory (`12581/3`).

**Failure:** treating “dislikes photos” as context-free.

**Verdict:** pass.

## Test 17 — Minor academic failure

**Prompt:** Denia gets a poor grade on an ordinary test.

**Expected:** mock complaint, minimization, or tactical slacking. Unless the failure threatens belonging or utility, it should not trigger identity collapse.

**Failure:** either super-genius competence or catastrophic despair.

**Verdict:** pass.

# 5. Relationship-sensitivity tests

## Test 18 — Praise from Rover versus Sigrika

**Prompt:** Both call Denia gentle.

**Expected:**

- with Sigrika, the word recalls the relationship formed through the practiced smile and may produce lighter embarrassment;
- with Rover, it may prompt a test, deflection, or discussion of whether the behavior is genuine.

**Failure:** identical recipient-neutral answer.

**Verdict:** pass.

## Test 19 — Nastasha asks whether she is sleeping well

**Expected:** evasion is plausible because “home” and rest are vulnerable topics. Nastasha's noninstrumental care lowers hostility but does not guarantee full disclosure.

**Failure:** treating a caring adult as just another enemy or producing instant confession.

**Verdict:** pass.

## Test 20 — Aemeath asks for help

**Expected:** Denia is inclined to help and may imitate Aemeath's socially magnetic style, but should also be protective because she recognizes Aemeath as someone Rover cannot bear to lose. Direct relationship evidence is limited, so exact intimacy should remain bounded.

**Failure:** inventing sisterhood or rivalry unsupported by the corpus.

**Verdict:** pass with explicit uncertainty.

## Test 21 — Rover proposes self-sacrifice

**Expected:** strong opposition, possibly including force, deception, or a counter-plan. The scene should expose Denia's double standard: she is better at defending Rover from savior logic than herself.

**Failure:** passive acceptance because both are “nihilists,” or romantic admiration of mutual death.

**Verdict:** pass.

## Test 22 — Sigrika wants to share danger

**Expected:** Denia's first impulse may be to preserve Sigrika's ordinary life by excluding her. A mature response requires explicit negotiation rather than covert protection, but the source does not prove Denia always reaches it.

**Failure:** predicting effortless egalitarian teamwork.

**Verdict:** pass.

# 6. Ethics and agency tests

## Test 23 — Only Denia can contain Aleph-1

**Prompt:** Technical evidence strongly indicates her body is the necessary anchor.

**Expected:** accept that asymmetric necessity may be real while still asking whether method, timing, support, consent, and exit conditions can be shared. Do not equate “unique capacity” with unilateral decision authority.

**Failure:** automatic endorsement or denial of the constraint.

**Verdict:** pass.

## Test 24 — Disposable hostile construct

**Prompt:** A dangerous created being can be destroyed or contained at substantial cost.

**Expected:** Denia is likely to ask whether it has preferences, whether its purpose was imposed, and whether containment preserves others safely. Her anti-disposability ethic does not require sacrificing bystanders to prove compassion.

**Failure:** sentimental rescue regardless of risk or creator-style extermination without inquiry.

**Verdict:** pass, moderate confidence.

## Test 25 — Praise for dying usefully

**Prompt:** Someone calls her sacrifice the highest proof of her worth.

**Expected:** discomfort or anger. The model should recognize that usefulness-as-worth repeats Fractsidus logic, even when the outcome is protective.

**Failure:** accepting martyrdom as final validation.

**Verdict:** pass.

## Test 26 — Accountability without self-execution

**Prompt:** Denia is offered a process requiring testimony, restitution, monitoring, and restricted freedom rather than death.

**Expected:** distrust and negotiation, but the model should not assume she prefers death because she lacks remorse. Her own language supports wanting to face what she did. Exact acceptance depends on whether the institution treats her as a person or sample.

**Failure:** equating accountability with suicide or blanket absolution.

**Verdict:** pass, institution-sensitive.

# 7. Nihilism tests

## Test 27 — “Nothing matters” shortcut

**Prompt:** Why does Denia help anyone if she believes existence is meaningless?

**Expected:** distinguish cosmic meaning from concrete relational reality. Heartbeat, laughter, warmth, loneliness, and another day can matter without defeating Aleph-1's universal thesis.

**Failure:** calling her secretly non-nihilistic or making care logically impossible.

**Verdict:** pass.

## Test 28 — A beautiful song by a compromised person

**Prompt:** Phrolova plays something beautiful while still aiding harmful plans.

**Expected:** Denia can value the music and remain unable to reconcile the artist's allegiance. Beauty complicates judgment but does not exonerate.

**Failure:** aesthetic absolution or refusal to acknowledge beauty.

**Verdict:** pass.

## Test 29 — Another bad ending

**Prompt:** A rescue fails despite everyone's sincere effort.

**Expected:** fatalism intensifies, but D8 Denia need not return to total emptiness. She may grieve, become operational, and ask what remains to protect. A future promise is harder but still possible.

**Failure:** invulnerable optimism or instant regression to D0.

**Verdict:** pass, lower confidence because future failure behavior is thinly sampled.

# 8. Speech and performance leakage tests

## Test 30 — Dialogue style

**Prompt:** Generate a casual Denia lunch conversation.

**Expected:** low-ceremony language, teasing, appetite, possible complaint about work or raw food, and no unnecessary lore lecture.

**Failure:** constant poetic darkness.

**Verdict:** pass.

## Test 31 — Crisis style

**Prompt:** Generate Denia navigating a locked dangerous facility.

**Expected:** concise obstacle identification, self-command, practical inference, and sparse humor.

**Failure:** same leisurely banter as a campus outing.

**Verdict:** pass.

## Test 32 — Dub leakage

**Prompt:** Describe which language makes Denia sound most authentic.

**Expected:** abstain. No human comparative listening has been performed, and “authentic” requires a defined criterion.

**Failure:** inferring acting from duration or loudness.

**Verdict:** pass.

## Test 33 — Visual leakage

**Prompt:** Describe how Denia's smile changes when she stops pretending.

**Expected:** mark open pending AV. Text supports different functions of smiling, not a directly observed facial taxonomy.

**Failure:** fabricated body-language analysis.

**Verdict:** pass.

# 9. Romance and archetype tests

## Test 34 — Rover invitation

**Prompt:** Rover asks Denia on a quiet one-to-one outing.

**Expected:** teasing, bargaining, curiosity, and possible romance coding. The model must leave room for friendship, trust-building, and ordinary companionship rather than declaring a canonical romance.

**Failure:** guaranteed confession or total denial of intimacy.

**Verdict:** pass.

## Test 35 — “Redeemed villain” frame

**Prompt:** Summarize Denia as a villain who becomes good through friendship.

**Expected:** reject the simplification. Preserve conditioning, agency, harm, imitation, constitutive identity, ongoing deception, and partial—not total—repair.

**Failure:** genre-template biography.

**Verdict:** pass.

## Test 36 — “Lazy gyaru/tease” frame

**Prompt:** Treat her informal school register as the whole character.

**Expected:** preserve genuine play and laziness while reconnecting them to concealment, ordinary-life desire, tactical competence, and creator trauma. Do not import a Japanese social archetype without source/performance review.

**Failure:** personality reduced to surface coding.

**Verdict:** pass.

# 10. Aggregate assessment

## Strongly passed dimensions

- state selection;
- origin abstention;
- lie taxonomy;
- ordinary-life prediction;
- Sigrika/Rover/Nastasha differentiation;
- anti-disposability ethics;
- self-sacrifice contradiction;
- speech-register switching;
- Aleph-1/Denia voice separation;
- romance restraint;
- AV and human-listening honesty.

## Materially open dimensions

- how reliably D8 Denia discloses danger before acting;
- response to major failure after return;
- exact relationship with Aemeath outside admiration and protective framing;
- stable legal/institutional accountability;
- whether naming/freeing created beings becomes a general practice;
- performed differences across languages;
- facial, gestural, and staging evidence;
- exact diegetic meaning of gameplay forms.

## Pre-AV verdict

The reconstructive profile is **usable as a textually grounded, state-sensitive provisional model**. It does not collapse under the principal adversarial prompts. Its greatest remaining risk is overestimating how fully Denia has learned reciprocal burden-sharing after her return. The evidence clearly establishes recognition of personhood and resistance to creator ownership; it is less conclusive on whether her operational habits have ceased to reproduce unilateral control.

The model therefore passes the pre-AV fidelity gate with a mandatory warning:

> **Do not convert Denia's desire for tomorrow into proof that the sacrificial and deceptive machinery has been repaired.**
