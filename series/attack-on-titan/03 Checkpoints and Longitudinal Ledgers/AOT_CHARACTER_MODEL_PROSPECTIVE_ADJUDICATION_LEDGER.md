---
series: AOT
artifact_type: claim_revision_ledger
ledger_type: prospective_character_model_adjudication
scope: V20-V34
generation: V2
status: active_provisional
version: '2.4'
date: '2026-08-26'
source_boundary: Prospective adjudication against frozen V01-V19 register through canonical V34; fifteen completed holdout tranches
construction_register: AOT_CHARACTER_MODEL_PROSPECTIVE_PREDICTION_REGISTER_V01-V19.md
construction_register_drive_id: 1mitpIqQSR3RqzBiAqEeZxPrT-jPlODo8
construction_register_frozen: true
prediction_text_mutated: false
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Attack on Titan — Character Model Prospective Adjudication Ledger
## Completed sequential holdout tranches: Volumes 20-34

## 0. Function and immutability rule

This is the rolling adjudication home for the prospective character-model predictions frozen at the end of the V01–V19 analytical boundary.

The prediction text remains authoritative and immutable in:

`AOT_CHARACTER_MODEL_PROSPECTIVE_PREDICTION_REGISTER_V01-V19.md`

This ledger does **not** rewrite predictions after seeing outcomes. It only records whether later canonical evidence fairly tests them and how the model performed.

Allowed outcome states:

`PASS | PARTIAL | FAIL | NOT_TESTED | CONFOUNDED`

A prediction absent from the evaluated table below remains `NOT_TESTED` at the V20 boundary.

Volume 20 is the first true holdout volume because the register was frozen in Drive before the V20 CBZ was fetched for analytical review.

## 1. Summary

Volume 20 is an unusually strong first holdout.

It tests the V19-boundary models under nearly continuous crisis, so the evidence is strongest for:
- command;
- tactical reasoning;
- partner/former-comrade relationships;
- sacrifice decisions;
- high-stakes written Japanese;
- response to model failure.

It is weak as a test of ordinary-life behavior.

Current result distribution for **fairly or partially tested** predictions:

| Outcome | Count |
|---|---:|
| PASS | 18 |
| PARTIAL | 2 |
| FAIL | 0 |
| CONFOUNDED | 0 |
| NOT_TESTED | all other frozen predictions |

The lack of a FAIL in one volume should not be overinterpreted. More importantly, V20 reveals several **model limitations that the frozen predictions did not need to count as failures**: Bertolt's new high-agency state remains fallible; Armin can freeze before recovering; Levi's local tactical dominance can be negated by a support-system intervention.

## 2. Adjudicated predictions

| Prediction | Character/domain | Result | V20 test | Canonical V20 evidence | Adjudication rationale |
|---|---|---|---|---|---|
| `AOT-PP-JEAN-01` | Jean — fear/practical leadership | **PASS** | Armin cannot yet solve the Colossal problem; Jean must organize the interior group under acknowledged uncertainty. | `AOT_V20_E002`, `AOT_V20_E013` | Jean does not deny danger or pretend certainty. He orders experimentation, creates observation space for Armin, and yields once Armin has a stronger model. This closely matches the frozen prediction. |
| `AOT-PP-ARMIN-01` | Armin — anomaly-driven model reconstruction | **PASS** | The current Colossal model provides no route; Armin notices visible thinning and connects it to earlier experiments. | `AOT_V20_E012`, `AOT_V20_E016` | Armin reconstructs a causal model from anomaly, prior evidence, resource constraints and mechanics, then revises the plan. |
| `AOT-PP-ARMIN-02` | Armin — negotiation/manipulation coexist | **PASS** | Armin needs Eren to follow a plan that will expose Armin to likely death. | `AOT_V20_E015`, `AOT_V20_E018` | He knowingly uses the sea promise and his history of honesty to mislead Eren about survival. The test is stronger than an enemy-only case because it shows manipulation can extend to the closest trusted relation under existential stakes. |
| `AOT-PP-ARMIN-04` | Armin — moral injury does not erase severe reasoning | **PARTIAL** | Armin conducts severe self-sacrificial reasoning while emotionally invested in the sea and Eren. | `AOT_V20_E014-E018` | V20 strongly supports continued severe reasoning under emotional cost, but the frozen condition specifically concerned moral injury after causing/enabling death. This is not the same state, so only PARTIAL. |
| `AOT-PP-BERTOLT-01` | Bertolt — V19 self-authored mission state persists | **PASS** | Immediate continuation of the V19 battle; Reiner is not available to make each decision. | `AOT_V20_E017`, `AOT_V20_E020` | Bertolt independently evaluates Armin, Eren, the Reiner front and the next objective. He does not revert to waiting for Reiner. |
| `AOT-PP-BERTOLT-02` | Bertolt — Reiner attachment changes sequence, not mission | **PASS** | Reiner remains endangered in the operation's immediate continuation. | V19 transition carried into V20; `AOT_V20_E020` | Bertolt's concern for Reiner affects sequencing but the larger objective persists. V20 confirms the independent mission state after that resequencing. |
| `AOT-PP-BERTOLT-03` | Bertolt — recognition and lethal commitment coexist | **PASS** | Bertolt watches Armin knowingly endure lethal heat. | `AOT_V20_E017` | Bertolt recognizes Armin's intelligence and suffering and says 「今 楽にしてやる」 while continuing the lethal thermal attack. Recognition does not reopen the mission. |
| `AOT-PP-ERWIN-01` | Erwin — probabilistic command under catastrophic uncertainty | **PASS** | Exterior force is trapped; no low-cost plan exists. | `AOT_V20_E003-E006` | Erwin identifies a high-cost probabilistic route, includes himself in the risk, and leads the charge rather than waiting for certainty. |
| `AOT-PP-ERWIN-02` | Erwin — guilt/private dream coexist with executive function | **PASS** | Dead comrades and basement proximity become maximally salient while command is still required. | `AOT_V20_E003-E006` | Erwin privately indicts motive and still constructs/executes command. |
| `AOT-PP-ERWIN-03` | Erwin — truth-object has unusually strong pull | **PASS** | The basement is physically near while the counterattack requires Erwin to relinquish his chance to see it. | `AOT_V20_E004-E005` | He explicitly says he wants to go to the basement; trusted intervention by Levi overrides the pull, exactly as the frozen prediction allowed. |
| `AOT-PP-ERWIN-04` | Erwin — public/private register split | **PASS** | Private Levi exchange versus public charge speech. | `AOT_V20_E004-E006` | Private speech is first-person desire/doubt; public speech uses collective meaning, repetition and imperative command. |
| `AOT-PP-LEVI-01` | Levi — chooser ownership under uncertainty, direct command exception | **PASS** | Erwin cannot release the basement dream; time is acute and tactical geometry is clearer. | `AOT_V20_E005` | The frozen exception predicted direct command when the objective is clear and time acute. Levi says 「俺は選ぶぞ」 and chooses for Erwin. |
| `AOT-PP-LEVI-02` | Levi — objective over vengeance | **PASS** | Levi has Zeke extracted and personally promised to kill the Beast. | `AOT_V20_E008-E010` | He does not immediately kill Zeke when power transfer and saving one Scout are strategically superior. |
| `AOT-PP-LEVI-03` | Levi — informed high-trust relation to Erwin survives impurity | **PASS** | Levi fully knows Erwin's private dream and must decide whether to keep trusting his command role. | `AOT_V20_E004-E006`, `AOT_V20_E011` | Trust not only survives; it becomes the basis for terminal decision-sharing and the later vow. |
| `AOT-PP-MIKASA-01` | Mikasa — imminent shifter threat produces preemption | **PASS** | Reiner is a known former comrade and active shifter threat. | `AOT_V20_E019` | Mikasa participates in immediate lethal/disabling action and says 「ライナー 出て」 during the attack. |
| `AOT-PP-MIKASA-03` | Mikasa — objective correction can override punitive momentum | **PARTIAL** | Mikasa works inside a coordinated Reiner-neutralization plan and accepts division of objectives. | `AOT_V20_E013`, `AOT_V20_E019` | The objective-oriented behavior is consistent, but V20 does not show the exact frozen transition from punitive momentum to commander correction. |
| `AOT-PP-EREN-02` | Eren — close-companion intervention, with larger-objective exception | **PASS** | Armin is being burned alive while Eren must remain hidden for the plan to work. | `AOT_V20_E015`, `AOT_V20_E018`, `AOT_V20_E020-E022` | This is a direct test of the frozen exception. Eren suppresses immediate rescue because revealing himself would destroy Armin's plan. |
| `AOT-PP-EREN-03` | Eren — recognition alone does not inhibit lethal opposition | **PASS** | Bertolt is a known former comrade and still the active existential opponent. | `AOT_V20_E021` | Eren executes the capture/kill-intended strike and says 「殺った」 without human recognition producing restraint. |
| `AOT-PP-X01` | Cross-model — recognition is not universal violence inhibitor | **PASS** | Multiple former-comrade conflicts under irreconcilable objectives. | `AOT_V20_E017`, `AOT_V20_E019`, `AOT_V20_E021` | Bertolt/Armin, Mikasa/Reiner, and Eren/Bertolt independently confirm the predicted coexistence of recognition and lethal action. |
| `AOT-PP-X04` | Cross-model — model revision beats stereotype consistency | **PASS** | Armin's failed situation model and Bertolt's apparently complete battlefield model. | `AOT_V20_E012-E020` | Armin succeeds by revising from new evidence; Bertolt loses after premature closure. The relevant consistency is update behavior, not always reaching the same answer. |

## 3. New model constraints revealed by V20

These are **not retroactive rewrites** of the frozen predictions. They are evidence for later model revision.

### 3.1 Bertolt: authored calm is not omniscience

The V19 transition predicted persistence of independent agency and that prediction passes. V20 adds a separate limit: Bertolt can reason carefully, inventory the visible battlefield, and still close the model too early. His high-agency state should therefore not be simulated as perfect situational perception.

### 3.2 Armin: model revision can be preceded by freeze

Armin's strength is not instantaneous insight. V20 shows a meaningful period in which Jean must carry practical command. The stable capacity is eventual evidence-conditioned reconstruction, not immunity to overwhelm.

### 3.3 Levi: local mastery remains system-dependent

Levi's Beast duel is overwhelming at the individual combat layer, yet Cart intervention prevents strategic closure. Character competence should never be modeled outside logistical/support context.

### 3.4 Erwin: another person can become the mechanism of self-authorship

The V01-V19 model treated agency as authorship under constraint. V20 adds a relational case: Erwin cannot choose cleanly while the basement is within reach, and Levi's decision makes action possible. Agency is not always maximized by leaving the burden with the nominal chooser.

### 3.5 Eren: collective discipline can override immediate rescue

The frozen model explicitly allowed this exception, and V20 supplies the strongest observed case. This is a major correction against “Eren always rushes in when a friend is endangered.”

## 4. Validation coverage limits after V20

V20 is almost entirely crisis evidence. It does not materially validate:
- ordinary leisure;
- domestic preference;
- romance;
- boredom;
- low-stakes social fluency;
- routine civilian speech.

High PASS counts for Levi, Erwin, Mikasa or Bertolt therefore **must not** be converted into unrestricted simulation readiness.

## 5. Next adjudication rule

Volume 21 and later should be scored only when a frozen prediction's state vector is sufficiently comparable.

Do not:
- count a scene twice merely because several superficial traits match;
- turn supportive but non-comparable evidence into PASS;
- treat absence as FAIL;
- reinterpret the prediction wording after outcome knowledge.

Do:
- preserve `PARTIAL` where only part of the condition is tested;
- use `CONFOUNDED` when relationship, knowledge state or role has materially changed;
- add explicit failure rows if later canon contradicts the frozen model.

## 6. Volume 21 adjudication tranche

Volume 21 shifts validation away from continuous battlefield optimization toward scarce-resource choice, grief, attachment, inheritance, and post-defeat state change. This produces fewer fair tests than V20 but one especially valuable `CONFOUNDED` case.

### V21 event summary

| Outcome | New V21 adjudication events |
|---|---:|
| PASS | 3 |
| PARTIAL | 3 |
| FAIL | 0 |
| CONFOUNDED | 1 |

Cumulative **adjudication-event** tally through V21: 21 PASS, 5 PARTIAL, 0 FAIL, 1 CONFOUNDED. This is not an unrestricted accuracy percentage and not a count of unique predictions.

| Prediction | Result | V21 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | serum advocacy + sea-memory argument | `AOT_V21_E003`, `AOT_V21_E006` | Eren remains categorical/direct under high stakes while also making blunt autobiographical self-critique; he does not become a one-note freedom slogan generator. |
| `AOT-PP-MIKASA-04` | **PASS** | serum confrontation | `AOT_V21_E002-E005` | Extreme attachment is expressed heavily through action, weapon readiness, tears, and short direct speech rather than extended abstract exposition. |
| `AOT-PP-LEVI-04` | **PASS** | serum choice | `AOT_V21_E002`, `AOT_V21_E007` | Levi's overt speech remains compressed while memory/action reveal dense attachment, grief, and mercy. Terseness is decisively not evidence of emotional absence. |
| `AOT-PP-EREN-02` | **PARTIAL** | Armin is dying and Eren aggressively intervenes in serum allocation | `AOT_V21_E003`, `AOT_V21_E006` | Strong support for attachment overriding institutional deference, but Levi controls the serum and Eren lacks the direct physical rescue path specified by the frozen condition. |
| `AOT-PP-HANGE-03` | **PARTIAL** | Hange's fresh bereavement and serum decision | `AOT_V21_E005` | Overwhelming grief coexists with disciplined institutional reasoning, but the frozen condition specifically concerned a personally charged investigation/target rather than resource allocation. |
| `AOT-PP-X03` | **PARTIAL** | Bertolt's helpless-death panic after V19/V20 calm high-agency state | `AOT_V21_E008` | Supports state-dependent repertoires and rejects "later state reveals earlier self as fake," but this is a situational collapse rather than a clean developmental transition. |
| `AOT-PP-BERTOLT-01` | **CONFOUNDED** for this V21 event | restrained, mission-defeated Bertolt calls for help before being eaten | `AOT_V21_E008` | V20 already supplied a fair PASS under the frozen D0 conditions. V21 changes physical agency, mission viability, escape options, and imminent-death state too radically to score as failure. Prior PASS remains intact. |

### V21 model-revision constraints

1. **Public-utility rhetoric may be attachment-laden.** Eren, Floch, Hange, and Levi all make public arguments shaped by different relationship access.
2. **Mercy may mean non-restoration.** Levi's care for Erwin includes refusing to return him to the dream/hell after accepted relinquishment.
3. **Hange's affective repertoire is broader than technical-command evidence implied.**
4. **Armin's selection produces survivor/replacement burden rather than automatic entitlement.**
5. **Bertolt demonstrates why state-vector comparison is mandatory.** Helpless death is not comparable to autonomous mission combat.
6. **Grisha and Floch enter/expand the modeling surface, but neither has enough ordinary temporal breadth for unrestricted simulation.**

### Next adjudication rule after V21

Volume 22 must continue event-level scoring without editing frozen V01-V19 prediction wording. A later scene may add a new PASS/PARTIAL/FAIL/CONFOUNDED event for a prediction already tested; preserve earlier fair tests rather than replacing them.

## 7. Volume 22 adjudication tranche

Volume 22 tests the frozen model in a post-battle, post-basement environment dominated by model revision, public truth, inherited memory, survivor critique, and the fulfilled sea horizon. The state shift makes several tests necessarily `PARTIAL`; no frozen wording is changed.

### V22 event summary

| Outcome | New V22 adjudication events |
|---|---:|
| PASS | 4 |
| PARTIAL | 4 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V22: **25 PASS, 9 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This is not an unrestricted accuracy percentage and not a count of unique predictions.

| Prediction | Result | V22 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | high-stakes royal-blood inference and sea/freedom confrontation | `AOT_V22_E019-E020`, `AOT_V22_E032` | Eren continues to use direct, categorical vocabulary under high stakes while the final freedom formulation remains a genuine question rather than polished analytical exposition. |
| `AOT-PP-EREN-03` | **PARTIAL** | newly humanized external enemy becomes the object of the sea question | `AOT_V22_E016`, `AOT_V22_E022-E023`, `AOT_V22_E032` | Recognition that the enemy is human does not produce automatic restraint; Eren imagines total enemy killing as a possible route to freedom. There is no immediate comparable combat decision against a known individual/former comrade, so the frozen condition is only partially tested. |
| `AOT-PP-ARMIN-01` | **PARTIAL** | post-basement world model and survivor-value uncertainty | `AOT_V22_E026-E027`, `AOT_V22_E031` | Armin responds to a shattered world model by preserving empirical openness and unobserved possibilities rather than defending the old closed model. The frozen condition concerned operational enemy anomalies, so transfer is supportive but not exact. |
| `AOT-PP-LEVI-01` | **PARTIAL** | retrospective dispute over the serum counterfactual | `AOT_V22_E025-E027` | Levi refuses to manufacture certainty about the `correct` choice because the unchosen future is unknowable. No subordinate is presently making the frozen decision, so this is principle-confirming rather than a fresh full behavioral test. |
| `AOT-PP-HANGE-01` | **PARTIAL** | uncertain Founding-Titan / royal-blood mechanics after basement | `AOT_V22_E016-E019` | Hange participates in a provisional mechanistic model and preserves uncertainty. The key Dina-contact evidence is privately withheld by Eren, preventing the experiment/update portion of the frozen prediction. |
| `AOT-PP-YMIR-02` | **PASS** | newly revealed first-person explanation of Ymir's costly return | `AOT_V22_E014-E015` | Ymir explicitly combines self-authorship with chosen debt and personal relation; severe self-cost is not grounded in abstract universal duty. This closely matches the frozen prediction despite being retrospective testimony newly exposed in V22. |
| `AOT-PP-X03` | **PASS** | Eren's sea-state development | `AOT_V22_E027`, `AOT_V22_E031-E032` | The childhood sea/freedom horizon remains historically real, but inherited evidence transforms its meaning. Later Eren modifies rather than invalidates earlier Eren. |
| `AOT-PP-X04` | **PASS** | Hange/Armin epistemic adaptation after basement | `AOT_V22_E016-E019`, `AOT_V22_E027`, `AOT_V22_E031` | Characters defined partly by revision adapt to a world model that invalidates earlier assumptions; consistency lies in update behavior, not in defending prior conclusions. |

### V22 model-revision constraints

1. **Eren's protection can include selective secrecy.** Care for Historia does not automatically imply giving her full authorship over the risk when Eren fears institutional exploitation.
2. **Freedom-seeking continuity does not establish Titan-programmed desire.** Eren's pre-inheritance childhood drive remains counterevidence to a simple programming model.
3. **Armin's optimism is epistemic rather than naive.** `可能性` rests on acknowledged ignorance, not confidence that outside people are benign.
4. **Floch develops survivor standing into political scrutiny.** Self-described weakness can become the basis for judging elite decisions rather than a reason for silence.
5. **Kruger is not a pure relativist.** His truth skepticism coexists with evidence-sensitive plausibility testing and highly directive mission language.
6. **Ymir's self-authorship includes chosen debt.** Freedom does not require refusing every costly obligation.

### Next adjudication rule after V22

Volume 23 must continue event-level scoring against the unchanged V01-V19 register. In particular, do not use later political knowledge to retroactively convert Eren's V22 sea question into a settled policy statement.

## 8. Volume 23 adjudication tranche

Volume 23 greatly expands character evidence but supplies relatively few exact holdout tests because focalization shifts to Marley and adult Reiner is temporally/role-distant from the V19 battle state. Conservative state-vector matching is therefore essential.

### V23 event summary

| Outcome | New V23 adjudication events |
|---|---:|
| PASS | 1 |
| PARTIAL | 3 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V23: **26 PASS, 12 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This is not an unrestricted accuracy percentage and not a count of unique predictions.

| Prediction | Result | V23 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-X03` | **PASS** | adult Reiner's Marley return and childhood fold preserve several historically real Reiner states | `AOT_V23_E008`, `AOT_V23_E027-E032` | V23 strongly supports the frozen rule that later development modifies rather than invalidates earlier states. Soldier Reiner remains psychologically real; young ideological Reiner is also shown as sincerely motivated rather than fake prehistory. |
| `AOT-PP-REINER-02` | **PARTIAL** | Reiner remembers and individuates the 104th while continuing to function as a Marleyan Warrior | `AOT_V23_E008`, `AOT_V23_E027` | Strong support for genuine attachment coexisting with hostile institutional role. The frozen condition centered on an active encounter/endangerment inside mission; V23 is post-mission memory, so PARTIAL is cleaner than PASS. |
| `AOT-PP-X01` | **PARTIAL** | human recognition of former comrades persists without ending Warrior participation | `AOT_V23_E027` | Recognition clearly coexists with continued role participation and renewed Paradis-operation planning, but V23 supplies no direct Reiner-vs-104th lethal encounter. |
| `AOT-PP-ZEKE-01` | **PARTIAL** | Zeke uses casual familiarity with Colt while maintaining rank/information asymmetry | `AOT_V23_E015-E016` | The casual-surface/unequal-authority component is supported, but this scene does not cleanly test severe coercion toward a subordinate. |

### V23 model-revision constraints

1. **Reiner's states accumulate rather than replace one another.** Childhood belief, soldier attachment, Warrior function, trauma, family performance, and mentorship remain simultaneously relevant.
2. **Insight can exceed perceived agency.** Reiner recognizes Gabi's future as dark but intervenes indirectly through Falco rather than openly breaking the system.
3. **Gabi reasons inside ideology.** High conviction is not evidence of passive scripting; she actively connects stigma, merit, family/community status, and violence.
4. **Falco supplies procedural restraint before ideological conversion.** He can protect an enemy prisoner without accepting that enemy's view of him.
5. **Zeke's humor can control disclosure.** Friendly register should not be translated into informational openness.
6. **Ordinary evidence expands without dissolving structural coercion.** Family warmth and peer play are part of the system's reproduction, not proof that the system is benign.

### Next adjudication rule after V23

Volume 24 must continue event-level scoring against the unchanged V01-V19 register. V23's temporal shift is a warning against treating adult Reiner's present state as a simple continuation of V19 combat conditions; score comparable state vectors, not shared character names.

## 9. Volume 24 adjudication tranche

Volume 24 is a distinctive holdout because much of its strongest Reiner evidence is **publication-later but diegetically earlier**. The adjudication rule remains epistemic rather than chronological: newly revealed flashback evidence may fairly test a frozen model if the prediction concerned underlying behavioral architecture and the scene's state vector is comparable.

### V24 event summary

| Outcome | New V24 adjudication events |
|---|---:|
| PASS | 2 |
| PARTIAL | 3 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V24: **28 PASS, 15 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or a count of unique predictions.

| Prediction | Result | V24 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-REINER-03` | **PASS** | newly revealed Marcel-selection / post-Marcel role crisis | `AOT_V24_E006-E010` | The frozen model predicted discontinuity or role slippage under severe conflict. V24 provides direct holdout evidence: `ライナーは死んだ` and `俺がマルセルに…なるから…` are explicit role substitution rather than smoothly integrated remorse. The scene is diegetically old but was epistemically unavailable when the register was frozen. |
| `AOT-PP-X03` | **PASS** | childhood ideological Reiner, constructed-Marcel Reiner, genuine trainee Reiner, adult suicidal Reiner, and current Warrior Reiner coexist | `AOT_V24_E003-E019`, `AOT_V24_E034` | V24 strongly supports the frozen rule that development adds/changes states instead of exposing every earlier state as fake. It explains role construction while preserving later soldier and mentor behavior as psychologically real. |
| `AOT-PP-REINER-02` | **PARTIAL** | Reiner maintains devil language while living socially among 104th and later meets Eren again | `AOT_V24_E016-E018`, `AOT_V24_E034` | Strong support for genuine attachment/social reality coexisting with hostile mission role, but V24 ends before a new present-tense lethal former-comrade confrontation is executed. |
| `AOT-PP-REINER-04` | **PARTIAL** | Reiner/Bertolt mission entrustment | `AOT_V24_E018` | `頼んだぞ相棒 / 任せろ` fits blunt familiar entrustment, but Bertolt is not specifically shown deferring a decisive task in the way required for a full frozen-condition test. |
| `AOT-PP-EREN-04` | **PARTIAL** | adult Eren uses calm extended reflection and practical relational speech under cover | `AOT_V24_E020-E023`, `AOT_V24_E030` | This materially expands the voice repertoire, but the frozen prediction targeted acute high-stakes action/identity decisions. A clandestine controlled conversation is a different state, so this is useful PARTIAL evidence rather than a contradiction. |

### V24 model-revision constraints

1. **Publication-later flashback can be legitimate holdout evidence.** The key is whether the information was unavailable at freeze time and whether the frozen rule actually covers the revealed mechanism.
2. **Reiner role replacement is now explicit rather than inferred.** `ライナーは死んだ / 俺がマルセルになる` should become a high-priority state transition in future models.
3. **Adult Eren has a reflective clandestine register.** Do not mis-score this as falsifying categorical combat speech; scenario state matters.
4. **Care and deception coexist.** Eren's treatment of Falco is the clearest current example and should constrain simplistic sincerity models.
5. **Self-authorship is morally non-monotonic.** Eren explicitly permits hope or deeper hell beyond self-chosen movement.
6. **Reiner's suicide interruption is relationally conditional.** Candidate responsibility is an anti-suicide tether in one scene, not a global recovery claim.
7. **Gabi can assimilate counterevidence into the existing worldview.** Models should allow gradual rather than instant belief revision.

### Next adjudication rule after V24

Volume 25 must continue event-level scoring against the unchanged V01-V19 register. The V24 basement encounter is unresolved at the boundary; no V25 reaction may be backfilled into V24. Preserve the distinction between newly revealed historical evidence and current-state behavior when assigning PASS/PARTIAL/CONFOUNDED.



## 10. Volume 25 adjudication tranche

Volume 25 provides an unusually clean test of the frozen recognition model because Eren explicitly reconstructs Reiner's humanity, childhood coercion, suffering, and similarity immediately before continuing into lethal opposition. Other tests remain state-qualified.

### V25 event summary

| Outcome | New V25 adjudication events |
|---|---:|
| PASS | 3 |
| PARTIAL | 2 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V25: **31 PASS, 17 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or a count of unique predictions.

| Prediction | Result | V25 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-03` | **PASS** | explicit causal/human recognition of Reiner followed by lethal continuation | `AOT_V25_E007-E015` | This is close to the frozen D0 condition: a known former comrade is fully recognized as human and structurally conditioned, but objective incompatibility remains. Recognition does not inhibit severe force. |
| `AOT-PP-MIKASA-04` | **PASS** | reunion, return plea, and civilian/child moral condemnation under active combat | `AOT_V25_E020`, `AOT_V25_E024` | Mikasa's speech remains concise, direct, concrete, and relationally dense rather than turning into extended abstract exposition. |
| `AOT-PP-X01` | **PASS** | Eren/Reiner mutual/causal recognition immediately before violence | `AOT_V25_E007-E015` | V25 is a strong canonical stress test of the frozen cross-model claim that empathy/recognition is not a universal violence inhibitor. |
| `AOT-PP-EREN-04` | **PARTIAL** | prolonged reflective basement speech followed by categorical `進み続ける / 駆逐` closure | `AOT_V25_E008-E014` | Acute action voice remains categorical, but the controlled pre-action state supports a broader reflective repertoire than the V19 construction set. State mismatch makes PARTIAL more appropriate than either PASS or FAIL. |
| `AOT-PP-JEAN-02` | **PARTIAL** | adapted human combat plus explicit civilian-harm limit | `AOT_V25_E022`, `AOT_V25_E029` | Jean preserves a human moral threshold inside lethal combat, but the volume does not provide the frozen condition's not-yet-certain individual kill decision. |

### V25 model-revision constraints

1. **Empathy can precede planned violence.** Eren's understanding of Reiner should not be simulated as a de-escalation switch.
2. **Later integration can follow earlier Reiner fracture.** Coherent retrospective confession does not invalidate V11/V24 discontinuity.
3. **Mikasa protection and moral approval are independent variables.**
4. **Shared battlefield allegiance does not imply Jean/Floch political agreement.**
5. **Fresh victimization can reinforce an inherited ideology.** Gabi's state now includes personal bereavement, not propaganda alone.
6. **Eren's current combat cognition is strongly evidence-sensitive.** The War Hammer inference expands the action/reasoning model outside the frozen personality tests.

### Next adjudication rule after V25

Volume 26 must continue event-level scoring against the unchanged V01-V19 register. Volume 27 is the approximately-75% checkpoint boundary: complete the V27 deep reading first, append its fair holdout events, then produce the provisional V01-V27 checkpoint before any V28 source exposure.


## 11. Volume 26 adjudication tranche

Volume 26 is a mixed holdout: the Liberio aftermath provides unusually strong moral-injury and prisoner/proportionality tests, while Chapter 106 adds retrospective context and a current Eren/Armin epistemic break. New Gabi/Falco/Reiner/Volunteer evidence is diagnostically important but is **not counted in the frozen-register tally** when no V01-V19 prediction covered that exact character/state.

### V26 event summary

| Outcome | New V26 adjudication events |
|---|---:|
| PASS | 4 |
| PARTIAL | 1 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V26: **35 PASS, 18 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or a count of unique predictions.

| Prediction | Result | V26 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | present-day prison mirror after unilateral Liberio operation and institutional confinement | `AOT_V26_E028-E030` | The high-stakes voice remains direct and categorical: `戦わなければ / 勝てない / 戦え / 戦え`. V26 strengthens the frozen prediction while adding a new constraint: the imperative can be self-directed rather than only aimed at enemy/action outside the self. |
| `AOT-PP-ARMIN-04` | **PASS** | Armin has personally used the Colossal Titan in a mass-casualty harbor attack and then conducts post-operation moral/strategic accounting | `AOT_V26_E007`, `AOT_V26_E026-E027` | This is the first clean test of the frozen condition. Armin names soldiers/civilians killed, judges the military port destruction as something they `やるしかなかった`, and remains capable of counterfactual strategy and reconciliation-oriented reasoning rather than becoming indifferent or functionally collapsing. |
| `AOT-PP-ARMIN-03` | **PARTIAL** | Armin's prior interpersonal model of Eren fails after Liberio | `AOT_V26_E026-E027` | Armin explicitly says he had intended to understand Eren better than anyone, even Mikasa, but now `もう…わからない`. This cleanly shows recognition of diagnostic model failure and confidence downgrade, but V26 does not yet show a completed replacement model, so PARTIAL is more disciplined than PASS. |
| `AOT-PP-JEAN-02` | **PASS** | Gabi has just killed Sasha and is captured with Falco; retaliatory execution is immediately available | `AOT_V26_E015-E017` | Jean resists throwing the children from the airship and asks whether doing so would end `この…殺し合い`. The human-killing threshold remains morally active even under direct bereavement, a stronger test than V25's partial result. |
| `AOT-PP-LEVI-02` | **PASS** | Zeke is physically accessible during extraction despite Levi's intense personal hostility and prior kill-vow | `AOT_V26_E017` | Levi preserves the larger extraction/containment objective and keeps Zeke under hostile supervision rather than converting access into revenge. Objective reprioritization again overrides punitive satisfaction without implying forgiveness or trust. |

### V26 model-revision constraints

1. **Self-authorship and self-coercion must coexist in the Eren model.** The frozen voice prediction passes, but the mirror adds a new internal-command mechanism that was not explicit at V19.
2. **Armin's moral-injury prediction now has a direct positive holdout.** Severe reasoning and guilt/self-implication coexist after Armin himself becomes the mass-casualty weapon.
3. **Interpersonal model revision can begin as admitted uncertainty.** Armin's `もう…わからない` is not failure to reason; it is a refusal to preserve false confidence before a replacement Eren model exists.
4. **Jean's proportionality survives personal loss.** The prisoner-child scene should strongly constrain revenge-first simulations.
5. **New V26 character constraints do not retroactively become frozen predictions.** Gabi's grief-to-action, Falco's attachment-over-information, Reiner's dependent-child tether, and Volunteer/Paradis dependence belong in the mutable modeling ledgers but not in the V01-V19 holdout score unless an actual frozen prediction is fairly tested.
6. **Cooperation is not trust.** Zeke's extraction and Volunteer support should remain relationship-state variables, not generic alliance labels.
7. **V26's ordinary evidence is narrow but unusually diagnostic.** Sasha/Nicolo food contact improves low-stakes control; it does not erase the crisis-heavy bias of the corpus.

### Next adjudication rule after V26

Volume 27 is the final holdout volume before the approximately-75% checkpoint. Score only genuinely comparable events against the unchanged V01-V19 register, then freeze the V20-V27 adjudication state for checkpoint synthesis. Do not expose the analysis to Volume 28 before `AOT_CHECKPOINT_75P_V01-V27_SYNTHESIS.md` is complete.


## 12. Volume 27 adjudication tranche

Volume 27 closes the pre-checkpoint holdout window. It provides strong new voice, ordinary-peer, moral-injury, and relationship-selectivity tests, but scenario matching is kept conservative: nearby thematic evidence is not scored when the frozen condition is materially different. In particular, Historia's V27 self-sacrifice decision is **not** counted against `HISTORIA-01`, whose frozen condition concerns Historia responding to another valued person's self-erasure; Hange's command self-doubt is likewise not forced into the grief-investigation prediction.

### V27 event summary

| Outcome | New V27 adjudication events |
|---|---:|
| PASS | 6 |
| PARTIAL | 4 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V27: **41 PASS, 22 PARTIAL, 0 FAIL, 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or a count of unique predictions.

| Prediction | Result | V27 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | adult Eren moves across affectionate railroad memory, prison confrontation, and post-escape command | `AOT_V27_E013-E014`, `AOT_V27_E005`, `AOT_V27_E043` | High-stakes/current voice remains direct and categorical without becoming one-note slogan speech. `お前らが大事`, `教えて下さいよ!!`, and `それだけだ` show distinct speech acts inside a stable direct register. |
| `AOT-PP-MIKASA-02` | **PARTIAL** | Eren takes autonomous politically dangerous action without Mikasa physically vetoing him; she instead seeks explanation/information | `AOT_V27_E012`, `AOT_V27_E015-E016`, `AOT_V27_E037`, `AOT_V27_E044` | This supports selective rather than automatic intervention, but the present sovereignty crisis is higher-stakes than the frozen low-to-moderate-stakes condition. |
| `AOT-PP-MIKASA-04` | **PASS** | acute Zackly explosion plus relational/political uncertainty | `AOT_V27_E021`, `AOT_V27_E037-E038` | Mikasa remains sparse and action-forward: refusal of Louise's intimacy, attempted information-seeking, and immediate bodily protection of Armin carry more state information than extended abstract speech. |
| `AOT-PP-ARMIN-03` | **PARTIAL** | V26's admitted Eren-model failure is followed by V27 succession contingency plus continued dialogue confidence | `AOT_V27_E016`, `AOT_V27_E036-E037`, `AOT_V27_E044` | Armin no longer treats his old Eren model as sufficient and builds a severe fallback, but he has not yet directly tested the replacement relational model against Eren. |
| `AOT-PP-ARMIN-04` | **PASS** | after V26 Colossal moral injury, Armin reasons through replacing Eren's Founder while still seeking dialogue | `AOT_V27_E016`, `AOT_V27_E036-E037` | This is a second clean event showing guilt/self-implication does not produce indifference or strategic paralysis. |
| `AOT-PP-JEAN-03` | **PARTIAL** | Jean challenges the old Eren model through Mikasa/Armin/Sasha costs | `AOT_V27_E015` | The register is exactly the predicted concrete social-cost accounting, but Jean is speaking about Eren to peers rather than confronting Eren directly. |
| `AOT-PP-JEAN-04` | **PASS** | publication-later railroad flashback under low immediate threat | `AOT_V27_E013-E014` | Adult Jean still converts awkward affection into irritation/peer friction instead of speaking as a permanently polished leader. |
| `AOT-PP-HISTORIA-04` | **PASS** | identity/sacrifice dispute over royal-blood reproduction and Beast succession | `AOT_V27_E001-E002` | Historia directly calls the system wrong and impermissible before accepting burden. High-stakes voice does not revert to Christa-style saintly euphemism. |
| `AOT-PP-LEVI-03` | **PASS** | morally compromised but strategically necessary Zeke explains Ragako and presses the time constraint | `AOT_V27_E029-E031` | Levi continues cooperation/containment without purity assumptions and can accept one true constraint (`time is short`) while rejecting motive and preserving hostility. |
| `AOT-PP-LEVI-04` | **PARTIAL** | Levi compresses Ragako moral salience into naming/correction rather than confession | `AOT_V27_E029-E031` | The anti-caricature rule is strongly supported, but this is retrospective victim-accounting rather than a clean immediate command-amid-loss scene. |

### V27 non-scored but model-critical constraints

1. **Historia sacrifice is a real model complication without being a fair `HISTORIA-01` test.** Her own acceptance of burden revises derived character rules, but the frozen prediction's scenario concerns another person's self-erasure.
2. **Hange command self-doubt is not forced into `HANGE-03`.** V27 shows personal destabilization plus continued investigation, but not the frozen grief/anger-investigation condition.
3. **Gabi/Falco/Kaya evidence is not retroactively promoted into V01-V19 predictions.** Their V27 worldview-stress, causal correction, and posthumous-Sasha inheritance belong in mutable ledgers and checkpoint synthesis.
4. **Floch/Yelena/Eren network evidence constrains later simulations but does not prove Eren authored Zackly's assassination.**
5. **The absence of FAIL events should not be read as proof of a complete model.** Several important V27 changes concern characters/states that the V19 register did not predict, and multiple frozen rules remain untested.

### Checkpoint freeze rule after V27

The V20-V27 holdout window is now closed for `AOT_CHECKPOINT_75P_V01-V27_SYNTHESIS.md`. The frozen V01-V19 register remains unchanged. The checkpoint should summarize both successes and coverage limits, distinguish repeated event tests from unique predictions, and use the event tally only as one diagnostic rather than as an unrestricted accuracy metric.

**Do not expose the analysis to Volume 28 before the V01-V27 checkpoint is complete.**


## 13. Volume 28 adjudication tranche

Volume 28 is the first post-checkpoint holdout tranche. The V01-V19 prediction register remains unchanged. Eligibility is kept conservative: major V28 evidence for Gabi, Falco, Nicolo, Kaya, Floch, Grisha, Shadis, Artur Blouse, and Ksaver is routed to the mutable model ledgers rather than retroactively inventing frozen predictions. `X03` and `X04` are not double-counted when the same evidence is already captured by character-specific tests.

### V28 event summary

| Outcome | New V28 adjudication events |
|---|---:|
| PASS | 6 |
| PARTIAL | 1 |
| FAIL | 0 |
| CONFOUNDED | 0 |

Cumulative **adjudication-event** tally through V28: **47 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

| Prediction | Result | V28 test | Evidence | Rationale |
|---|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | Eren's high-stakes autonomy/relationship confrontation with Armin and Mikasa | `AOT_V28_E015-E021` | Eren explicitly uses `オレは自由だ`, `自由意志`, `無知`, and `奴隷` in direct categorical speech while still answering causal questions and constructing a detailed interpersonal theory. The register is high-stakes and freedom-centered without collapsing into one-note slogan generation. |
| `AOT-PP-MIKASA-04` | **PASS** | Mikasa's bond is attacked as biological servitude under immediate transformation threat | `AOT_V28_E019-E022` | Her speech stays sparse and Eren-specific; action and visual shock carry the decisive state information. This is a cleaner relational-threat test than V27. |
| `AOT-PP-ARMIN-03` | **PASS** | V27's residual dialogue hypothesis is directly tested against current Eren | `AOT_V28_E017-E024` | Armin questions Eren's causal model, experiences diagnostic failure, then shifts to adversarial value-testing rather than insisting the old intimate model should still work. This completes the V26-V27 PARTIAL trajectory without rewriting those prior events. |
| `AOT-PP-LEVI-02` | **PASS** | Zeke transforms Levi's own subordinates while escape/containment remains the higher objective | `AOT_V28_E026-E031`, `AOT_V28_E036` | Levi kills the transformed threats, pursues Zeke, and restores containment. Punitive rage remains afterward, but mission priority clearly outranks the emotionally easier alternative of paralysis or indiscriminate vengeance. |
| `AOT-PP-LEVI-04` | **PASS** | immediate command/combat amid irreversible loss of subordinates | `AOT_V28_E025-E031` | Terse operational speech coexists with explicit dead-comrade/Erwin memory and rage at Zeke. The clean frozen condition is now met: brevity demonstrably does not equal emotional emptiness. |
| `AOT-PP-HANGE-01` | **PARTIAL** | spinal-fluid wine mechanism conflicts with the inherited paralysis model | `AOT_V28_E012-E014` | Hange identifies the source weakness (`ジークがそう言っただけだ`), revises the working model, states uncertainty, and implements precaution. The crisis does not permit a controlled experiment before action, so the frozen experiment/test component is not fully observed. |
| `AOT-PP-ZEKE-01` | **PASS** | Zeke exercises command over poisoned subordinates and attempts to escape Levi | `AOT_V28_E026-E030` | Conversational/regretful surface (`やりたくなかった`, `悲しいよ`, `決別`) coexists with covert poisoning, remote transformation, and epistemic claims that others lack real choice. Surface informality plainly does not imply equal decision authority. |

### V28 non-scored but model-critical constraints

1. **Eren's Ackerman/Bertolt claims remain actor testimony, not adjudicated ontology.** Scoring `EREN-04` concerns voice form, not truth of his causal claims.
2. **Mikasa's restraint of Armin is not used to prove the host-compulsion theory.** It is behavior requiring multiple hypotheses.
3. **Hange receives PARTIAL rather than PASS because the frozen prediction explicitly includes experiment/controlled test construction.** Emergency precaution is strongly consistent but not identical.
4. **Zeke's newly revealed childhood/motive architecture cannot retroactively become frozen predictions.** It updates readiness and mutable rules.
5. **No FAIL event is manufactured from Historia's absence or other untested characters.** Lack of a matching condition remains NOT_TESTED.
6. **`X04` is not separately scored from Armin/Hange evidence.** Doing so would double-count the same model-revision events and artificially improve the headline tally.
7. **The zero-FAIL record remains coverage-limited.** V28 still tests only a subset of the frozen register, heavily weighted toward crisis/relationship/voice domains.

### Next adjudication rule after V28

Volume 29, if opened after V28 integration, remains a fresh holdout tranche. Preserve all V20-V28 event results exactly as recorded; do not convert earlier PARTIAL events to PASS merely because the same prediction later passes. Continue to score events, not retrospective narrative fit, and keep the V01-V19 prediction text immutable.

## 14. Volume 29 adjudication tranche

Volume 29 is the second post-checkpoint holdout tranche. The frozen V01-V19 prediction text remains unchanged. Scoring is conservative: Mikasa, Jean, Zeke, Pieck, Gabi, Falco, Onyankopon, Nile, Pixis, Yelena, and Hange all receive meaningful mutable-ledger updates, but they are not promoted to additional headline events where a genuinely new frozen condition is absent or would double-count the same evidence.

| Prediction | Result | V29 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-EREN-03` | PASS | deeply recognized former comrade Reiner remains mission threat; Eren says `来いよ……ライナー` and continues lethal engagement | clean recurrent test of recognition without de-escalation after major state change |
| `AOT-PP-EREN-04` | PASS | high-stakes alliance/identity and combat decisions retain direct categorical `オレはやる / 進み続ける` and compressed challenge register | score concerns voice/decision architecture; terminal sincerity toward euthanasia remains OPEN |
| `AOT-PP-ARMIN-01` | PASS | Eren's latest explicit claims conflict with prior model; Armin integrates Founder mechanics, Yelena incentives, prior behavior, and limited-Rumbling alternative | strong causal model revision with explicit hedge `嘘だと思う` |
| `AOT-PP-ARMIN-02` | PASS | coercive Yelena interaction rewards apparent ideological alignment | Armin performs admiration/world-savior support while privately rejecting euthanasia; strategic dialogue includes deception |
| `AOT-PP-REINER-02` | PASS | Eren remains hostile target but Reiner possesses person-level recognition and mirrored suffering | `もういい / もう眠れ` empathy coexists with continued capture-oriented combat |

**V29 event result:** **5 PASS / 0 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Cumulative **adjudication-event** tally through V29: **52 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V29 methodological note: motive uncertainty can coexist with prediction success

`AOT-PP-EREN-04` can pass even though Eren's terminal objective is less certain after V29. The frozen prediction concerns recurrent behavior/voice under high-stakes freedom and obstruction conditions, not whether every explicit proposition transparently states his hidden plan. This separation is important: a model can become more accurate about **how a character behaves** while becoming more appropriately uncertain about **why this particular strategic presentation is occurring**.

### V29 unscored high-value model evidence

- Mikasa deliberately leaves the scarf while keeping the reason for Eren's cruelty unresolved.
- Jean preserves skepticism, accountability, and attachment simultaneously.
- Zeke's trust dependency and Paths-like firsthand experience deepen developmental/command modeling.
- Pieck's explicit comrade-over-state trust hierarchy substantially improves relational reconstruction.
- Gabi's devil ontology receives explicit person-level replacement.
- Falco supplies unusually strong ordinary-future preference evidence.
- Onyankopon directly falsifies a monolithic Volunteer-euthanasia category.

These belong in mutable ledgers/readiness rather than retroactively expanding the frozen prediction register.

## 15. Volume 30 adjudication tranche

Volume 30 is the third post-checkpoint holdout tranche. The frozen V01-V19 prediction text remains unchanged. Eligibility is especially conservative because many of V30's largest analytical gains concern Grisha, Ymir Fritz, Colt, Porco, and new Paths/future-memory mechanics that were not represented by frozen prediction conditions. Those belong in mutable ledgers rather than retroactive scoring.

| Prediction | Result | V30 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | Founder-contact betrayal, Grisha-memory intervention, and Ymir confrontation produce categorical but functionally varied high-stakes language: `到底受け入れられない`, `オレがこの世に生まれたからだ`, `立てよ 父さん`, `お前が決めていい` | strongest post-freeze demonstration that Eren's recurrent categorical freedom/existence register is robust across interlocutors and speech acts without reducing him to a single slogan; score does **not** assume complete terminal-motive transparency |
| `AOT-PP-ZEKE-01` | **PASS** | Colt's direct brother appeal is explicitly understood by Zeke immediately before Zeke screams and converts Falco/others | conversational empathy and regret coexist with absolute decision asymmetry and biological command, directly matching the frozen surface-informality/authority warning |

**V30 event result:** **2 PASS / 0 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Cumulative **adjudication-event** tally through V30: **54 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V30 methodological constraints

1. **Armin's V29 strategic-deception hypothesis is now substantially vindicated by Eren's direct admission**, but this is not a new `ARMIN-01` score because V29 already scored the model-revision event; V30 is outcome adjudication, not a second independent Armin event.
2. **`EREN-03` is not double-counted** for the continuing Reiner battle that began in V29.
3. **`X03` is not separately scored** from the Eren/Zeke material because doing so would reuse the same event evidence.
4. **Grisha/Ymir/Colt/Porco evidence cannot become retroactive frozen predictions.** It improves readiness and negative constraints instead.
5. **Future-memory revelation is not a prediction-success shortcut.** The register was frozen without this mechanism; no later causal twist may be used to reinterpret old predictions into inevitability.
6. **Zero FAIL remains coverage-limited.** V30 is dominated by ontology, inherited causality, and characters/states outside the frozen register.

## 16. Volume 31 adjudication tranche

Volume 31 is the fourth post-checkpoint holdout tranche. The frozen V01-V19 prediction text remains unchanged. Eligibility is conservative because many of the volume's largest gains concern Gabi, Connie, Floch, Onyankopon, Annie's retrospective self-accounting, coalition architecture, and Eren's newly explicit Rumbling target—areas where either no frozen prediction exists or the exact frozen condition is not freshly instantiated.

| Prediction | Result | V31 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-ARMIN-03` | **PASS** | Eren's Founder broadcast directly falsifies Armin's residual V29 limited-Rumbling reconstruction by announcing outside-world extermination; Armin names the act `前代未聞の大虐殺` and joins the stop-Eren coalition | independent post-V28 model-revision test: Armin does not preserve a preferred intimate model once the counterevidence is diagnostic |
| `AOT-PP-ARMIN-04` | **PASS** | amid inherited Liberio moral injury plus genocide/command collapse/Connie-Falco crisis, Armin reaches explicit overload, narrows the problem, and then makes a severe self-sacrificial intervention rather than becoming indifferent or durably nonfunctional | clean state-sensitive confirmation: guilt/overload can impair executive integration without erasing severe reasoning or action |

**V31 event result:** **2 PASS / 0 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Cumulative **adjudication-event** tally through V31: **56 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V31 unscored high-value model evidence

1. **Eren's broadcast strongly confirms his categorical high-stakes voice architecture**, but `EREN-04` had just received a clean V30 PASS and another headline score would add little beyond recurrence.
2. **Mikasa's scarf reclamation strongly supports action-carried relationship modeling**, but it does not cleanly satisfy the frozen low/moderate-stakes `MIKASA-02` condition and `MIKASA-04` is already multiply tested.
3. **Jean's beneficiary/refusal arc is highly diagnostic**, but the frozen Jean conditions do not map cleanly enough to justify stretching them: his four-shot rescue is not the `JEAN-02` opponent-threat condition and his Eren cost-accounting occurs largely in Eren's absence.
4. **Annie's father/return confession strongly validates the logic behind `ANNIE-01`**, but V31 gives retrospective self-accounting rather than a fresh superior/peer loyalty-test under the exact frozen condition; it therefore improves mutable readiness without manufacturing a PASS.
5. **Levi's cooperation field is promising but injury-bounded.** Presence with Hange/Pieck/Magath is insufficient for another `LEVI-03` event without more active decision evidence.
6. **No FAIL is created from missing conditions.** V31 is rich in ethics/coalition evidence but still uneven against the frozen register.

## 17. Volume 32 adjudication tranche

Volume 32 is the thirteenth post-freeze holdout tranche. The V01-V19 register remains unchanged. Scoring stays conservative despite extensive Annie, Jean, Connie, Eren, Magath, Falco and coalition evidence because only freshly instantiated frozen conditions are eligible.

| Prediction | Result | V32 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-ARMIN-02` | **PASS** | facing Samuel/Daz at the harbor under existential time pressure, Armin first attempts a no-bloodshed solution by fabricating a plausible escaped-Cart/Marley-remnant story and performing categorical pro-Rumbling loyalty so the flying boat can be released intact | clean independent recurrence: dialogue orientation includes deliberate deception/leverage when sincere disclosure would defeat the communicative objective; force follows only after the ruse collapses |
| `AOT-PP-HISTORIA-04` | **PASS** | in a post-V16 identity/sacrifice dispute with Eren, Historia directly calls outside-world extermination wrong, rejects the implication that outsiders are all enemies, and says silence would leave her unable to live `胸を張って` | direct self-authored Historia voice under sacrifice pressure; the response is morally owned and non-Christa-deferential without requiring softness or saintly self-erasure |

**V32 event result:** **2 PASS / 0 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Cumulative **adjudication-event** tally through V32: **58 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V32 unscored high-value model evidence

1. **Eren's private annihilation commitment plus friend-care memories** strongly improve terminal-value reconstruction but do not warrant another immediate `EREN-04` score.
2. **Annie's withdrawal after Liberio becomes unsavable** validates father-return centrality but is motive-collapse/exhaustion rather than the exact frozen `ANNIE-01` superior/peer loyalty condition.
3. **Jean's beneficiary fantasy and refusal** are highly diagnostic but do not cleanly instantiate a frozen Jean condition.
4. **Connie's killing of Samuel/Daz** is crucial moral-injury evidence without a matching frozen prediction.
5. **Falco's first Jaw loss of control** is body/competence evidence outside the V19 construction set.
6. **No FAIL is manufactured from absent conditions.**

## 18. Volume 33 adjudication tranche

Volume 33 is the fourteenth post-freeze holdout tranche. The V01-V19 prediction register remains unchanged. Scoring is conservative: major Annie, Mikasa, Hange, Reiner, Jean, Connie, Falco, Kiyomi, Karina and Fort Salta evidence improves mutable models, but only exact freshly instantiated frozen conditions are counted.

| Prediction | Result | V33 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-EREN-04` | **PASS** | private Ramzi motive disclosure plus the Paths confrontation preserve categorical high-stakes `自由 / 止まらない / 進み続ける / 戦え` language while also allowing apology, shame and relational distinction | clean recurrent voice test after V31-V32 deliberately avoided redundant Eren scoring; direct categorical action language remains robust without reducing him to one slogan |
| `AOT-PP-ARMIN-03` | **PASS** | Armin enters Paths still prioritizing dialogue; Eren explicitly says discussion is unnecessary and refuses to stop; Armin returns recognizing negotiation hope has been crushed and assumes commander responsibility | fresh diagnostic interpersonal-model failure: Armin updates instead of insisting the preferred communicative lever must work |
| `AOT-PP-LEVI-04` | **PASS** | Hange's imminent death/command transfer produces compressed `心臓を捧げよ / じゃあな ハンジ`, followed by continued terse operational speech | clean independent command-amid-loss recurrence: brevity remains compatible with attachment and grief |

**V33 event result:** **3 PASS / 0 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Cumulative **adjudication-event** tally through V33: **61 PASS, 23 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This remains an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V33 unscored high-value model evidence

1. Armin's dialogue-before-force again supports `ARMIN-02`, but the Paths appeal is sincere rather than a fresh manipulation/deception event and V32 already supplied a clean independent test.
2. Hange's succession strongly supports distributed trust, but it is a terminal transfer of overall command rather than the exact `HANGE-02` parallel-objective/local-specialist condition.
3. Mikasa's sparse relationship speech supports `MIKASA-04`, but the scene is more relational than tactical and another headline score would add little.
4. Reiner's hypothesis about Eren wanting to be stopped is valuable actor evidence but not a clean `REINER-02` event; it remains interpretive/self-projective until independently supported.
5. Annie's withdrawal/broadened attachment field does not satisfy `ANNIE-01`'s exact superior/peer coercive loyalty-test condition.
6. Falco's flight hypothesis lies outside the V19 frozen construction set and belongs in mutable readiness/behavior ledgers.
7. No FAIL is manufactured from absent conditions.

## 19. Next tranche discipline

Volume 34 remains locked until V33 integration and administrative verification are complete. Preserve all V20-V33 event results exactly. Do not use V33's final coalition arrival, Beast-shaped body, Falco flight hypothesis, Annie withdrawal, Mikasa non-kill intent, Reiner hypothesis, or Fort Salta vow to infer any V34 outcome before the V34 source is opened.



## 20. Volume 34 adjudication tranche

Volume 34 is the fifteenth and final sequential post-freeze holdout tranche. The V01-V19 prediction register remains immutable. Ending density does not relax eligibility: only conditions that are freshly and cleanly instantiated are scored.

| Prediction | Result | V34 condition / observed event | Adjudication note |
|---|---|---|---|
| `AOT-PP-MIKASA-01` | **PASS** | Eren is an active transformation-capable catastrophic opponent, seconds-to-act conditions apply, and Mikasa's prior relationship is maximally strong; she enters the Titan and decapitates him | strongest available stress test of relationship-not-vetoing lethal preemption; V34 adds the new constraint that lethal action can coexist with retained love/grief |
| `AOT-PP-ARMIN-04` | **PASS** | after mass-death disclosure, participation in Eren's death and longstanding moral injury, Armin immediately faces armed post-Titan crisis and later diplomatic responsibility | guilt remains behaviorally active while severe reasoning and responsibility continue; terminal confirmation in a political rather than battlefield domain |
| `AOT-PP-EREN-01` | **PARTIAL** | Eren explicitly self-personalizes responsibility for catastrophic harm with Armin present, but he is terminal and the frozen severe-guilt exception is active | guilt architecture is confirmed; recovery-through-shared-positive-objective is not fairly testable, so PASS would overclaim and FAIL would ignore the predicted exception |

**V34 event result:** **2 PASS / 1 PARTIAL / 0 FAIL / 0 CONFOUNDED**.

Final cumulative **adjudication-event** tally through V34: **63 PASS, 24 PARTIAL, 0 FAIL, and 1 CONFOUNDED**. This is an event tally rather than an unrestricted accuracy percentage or count of unique predictions.

### V34 unscored high-value model evidence

1. `EREN-04` receives major private-voice exception/refinement evidence, but another repetitive headline score would obscure the more useful state transition.
2. `MIKASA-04` remains strongly supported, but the decisive event is already represented by the cleaner `MIKASA-01` test.
3. Levi's Zeke kill is not scored as `LEVI-02` because personal vengeance and mission objective align, preventing clean discrimination.
4. Armin's Muller argument supports dialogue orientation but does not require the deception/manipulation component central to `ARMIN-02`.
5. Falco's successful flight lies outside the frozen V19 construction set and stays mutable model evidence.
6. No FAIL is manufactured from absent final-volume conditions.

## 21. Sequential holdout closure

The V01-V19 register remains frozen permanently as construction evidence. V20-V34 now form the completed sequential holdout history. Future character-model work may cite this ledger, but should not append post-series retrospective events as if they were new manga-volume holdout tranches. Full-series model validation must use the reconstruction/validation method, cross-model consistency checks, scenario-distance labels, and any genuinely new external holdout sources separately from this completed sequential tally.
