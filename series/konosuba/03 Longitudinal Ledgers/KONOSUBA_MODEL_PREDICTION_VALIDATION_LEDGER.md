---
series: KONOSUBA
artifact_type: ledger
scope: V01-V17
ledger_role: model_prediction_validation
generation: MODEL_GEN_0.4
status: active_provisional
source_boundary: All prior model and forecast blocks, original blank fields and local histories preserved; Gen03 formally closed; unchanged Gen04 derived only through V12 with 25 V13-V15 forecasts; all 25 separate local outcomes for each of V13, V14 and V15 appended; formal V13-V15 tranche open; V15 publication gate and separate checkpoint/Gen05 freeze required before V16
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA Model Prediction and Validation Ledger

## Purpose

This ledger preserves falsifiable behavioral predictions at the moment they are made so later volumes can test rather than retrospectively rewrite the character models.

**Current freeze:** Model Generation 0.4, derived only from principal main narrative through V12. Gen03 remains formally closed at 9 CONFIRMED / 5 PARTIAL / 10 NOT_TESTED / 1 FALSIFIED; all original blocks, blank fields and local histories are exact. The 25 original Gen04 Outcome/Adjudication pairs stay blank. Separate V13 outcomes remain 3 CONFIRMED / 8 PARTIAL / 13 NOT_TESTED / 1 local FALSIFIED (K03). Separate V14 outcomes are 4 CONFIRMED / 7 PARTIAL / 13 NOT_TESTED / 1 local FALSIFIED (A02). Each local failure retains its original whole-tranche threshold and does not by itself retire Gen04. V13–V15 remains OPEN, including pooled J02. V13’s full publication gate closed on exact ee4e2882 before V14 exposure. V15 remains unopened until the containing V14 transaction is published/read back and its own source audit, housekeeping and final exact-head status succeed, followed by fresh admission.

**Contamination rule:** The predictions below were written before canonical analysis of V04. They may not be reworded after later evidence appears. Later evidence must be entered only in the outcome/adjudication fields.

Outcome vocabulary:

`CONFIRMED | PARTIAL | FALSIFIED | NOT_TESTED | AMBIGUOUS`

Claim transition vocabulary:

`PRESERVE | STRENGTHEN | REVISE | DOWNGRADE | REJECT | OPEN`

---

# Model Generation 0.1 — Predictions for V04-V06

## Satou Kazuma

### MG01-K01 — Rule exploit over direct contest
- **Trigger/context:** A nontrivial obstacle presents explicit or inferable rules and direct power is unfavorable.
- **Relationship condition:** Any.
- **Stake level:** Low to high.
- **Predicted appraisal:** “There is probably a cheaper/indirect way through the system.”
- **Predicted dominant motive:** Resolve problem while minimizing effort/risk/cost.
- **Predicted behavior:** Kazuma will prefer an indirect, combinatorial, or loophole-based solution over a straightforward power contest.
- **Boundary:** When an exploit becomes salient, he may under-model second-order physical/social consequences.
- **Confidence:** HIGH.
- **Evidence basis:** V01 Beldia weak-point/routing; V02 conventional-party tactics, golem/coronatite; V03 Bow/Snipe adaptation, marriage duel, sealing/Tinder.
- **Disconfirmation:** Multiple clear rule-based opportunities where he consistently chooses direct contest despite recognizing a cheaper exploit, absent overriding moral/relationship reason.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch1 Lizard Runner hunt reproduces both exploit preference and the predicted second-order physical blind spot; Ch2 Running Hawk-Kite routing and Ch5 Hans bait/containment pipeline independently replicate the exploit side. STRENGTHEN.

### MG01-K02 — Concrete loyalty override
- **Trigger/context:** A person Kazuma treats as teammate, entrusted ally, or locally “his” person faces concrete serious harm.
- **Relationship condition:** Established membership/trust rather than stranger abstraction.
- **Stake level:** Serious.
- **Predicted appraisal:** Concrete harm becomes more important than abstract heroic status.
- **Predicted dominant motive:** Protect/repair/assume responsibility, while still complaining.
- **Predicted behavior:** Cynicism, comfort-seeking, or cowardly self-description will weaken enough for intervention.
- **Confidence:** HIGH.
- **Evidence basis:** V01 immediate rescue impulse and Darkness injury; V02 Taylor/Keith, succubus trust, Axel defense; V03 Darkness execution/absence, Explosion responsibility, Wiz report.
- **Disconfirmation:** He abandons a clearly established ally to serious preventable harm primarily for comfort/self-protection despite having a feasible intervention.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch4: Kazuma had ignored Hans as an abstract Axis problem to preserve his vacation, but Aqua’s concrete distress over her followers moves him into investigation; Ch5 he assumes substantial coordination risk once the source/follower threat is immediate. STRENGTHEN.

### MG01-K03 — Low-stakes grievance retaliation
- **Trigger/context:** Kazuma is publicly humiliated, unfairly blamed, or gains leverage over someone who recently held power over him.
- **Relationship condition:** Especially safe/familiar or consequence-light environment.
- **Stake level:** Low to moderate.
- **Predicted appraisal:** Opportunity to “even the score.”
- **Predicted dominant motive:** Status repair / petty gratification.
- **Predicted behavior:** He retaliates verbally, socially, or through a cheeky exploit rather than simply taking the high road.
- **Confidence:** HIGH.
- **Evidence basis:** V01 retaliatory choice of Aqua; V02 recurring party payback; V03 Sena needling and `Lalatina` punishment.
- **Disconfirmation:** Repeated comparable humiliation with no retaliation despite low cost and clear opportunity.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch1/Ch3: corpse-prank retaliation threats and the confession-booth setup show low-cost grievance/status payback remains an active script. PRESERVE/STRENGTHEN.

### MG01-K04 — Mixed motives remain mixed
- **Trigger/context:** A decision can benefit both another person and Kazuma himself.
- **Predicted appraisal:** He will notice both practical/self-interested and relational reasons.
- **Predicted behavior:** Action may be genuinely prosocial while narration emphasizes convenience, sex, money, grievance, or self-protection.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V02 local loyalty and succubus secret; V03 Yunyun gift, Darkness marriage, dungeon investigation.
- **Disconfirmation:** Later internal access consistently reveals that apparent prosocial acts are purely instrumental, or conversely that selfish framing is consistently only false cover with no causal force.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch3 mixed bath: lust and risk avoidance materially motivate Kazuma, yet he later recasts the episode as deliberate intelligence-gathering; Darkness can contradict the retrospective self-presentation. Ch4 helping Aqua also combines loyalty with continued dislike of the Axis institution. STRENGTHEN.

## Aqua

### MG01-A01 — Status challenge produces overclaim or overdeployment
- **Trigger/context:** Aqua's divine status, sacred competence, superiority, or credibility is challenged in public.
- **Predicted appraisal:** Challenge to rightful recognition.
- **Predicted dominant motive:** Restore status / prove competence.
- **Predicted behavior:** She will assert a grand claim or deploy genuine high-tier ability before fully modeling collateral/social consequences.
- **Post-failure prediction:** Initial defense/blame is likely while face-saving remains available; direct apology becomes much more likely once causation is undeniable and no plausible status-preserving account remains.
- **Confidence:** HIGH.
- **Evidence basis:** V01 frogs/flood; V02 undead attraction/status cycles and cemetery guilt; V03 trial follower boast.
- **Disconfirmation:** Repeated public competence/status challenges produce cautious information gathering and calibrated deployment without defensive overstatement.
- **Outcome:** PARTIAL — V04 supplies strong adjacent support; exact trigger remains open through V06.
- **Adjudication:** V04 Ch3 shows a true goddess-status claim becoming socially unusable because Aqua’s presentation/credibility is poor; Ch5 maximum purification solves the poison problem while creating massive downstream system effects. The overdeployment/externality mechanism is strongly supported, but the final overpurification is not caused by the exact public-status-challenge trigger. REVISE boundary, STRENGTHEN mechanism.

### MG01-A02 — Sacred/evil cue can outrun tactical consensus
- **Trigger/context:** Aqua perceives undead, demon, curse, malign aura, or another category she treats as sacredly offensive.
- **Predicted appraisal:** Immediate categorical rejection / purification target.
- **Predicted behavior:** She may act before group consensus or before considering downstream tactical effects.
- **Competence modifier:** Her underlying supernatural diagnosis will often be substantially correct even when the action timing/magnitude is disruptive.
- **Confidence:** HIGH.
- **Evidence basis:** V01 undead; V02 Keele contrast/dungeon; V03 Alderp malign force, Vanir/doll antipathy.
- **Disconfirmation:** Multiple clear sacred-threat cues where her diagnosis is routinely wrong or she consistently waits for tactical coordination despite no inhibiting relationship/stake factor.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch4: Aqua correctly infers contamination from anomalously slow purification despite party skepticism. Demon/undead cues continue to prompt rapid categorical responses. Diagnosis is again better calibrated than social/tactical deployment. STRENGTHEN.

### MG01-A03 — Tedious obligation invites maximal shortcut
- **Trigger/context:** Repetitive low-status maintenance duty with an available high-power shortcut.
- **Predicted appraisal:** Routine is unnecessarily annoying if one big intervention could replace it.
- **Predicted behavior:** Aqua will prefer the shortcut and insufficiently model secondary-system effects.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V02 cemetery barrier; V03 shop/street externalities provide adjacent support rather than exact replication.
- **Disconfirmation:** Repeated tedious maintenance contexts where she reliably chooses sustained routine despite an attractive shortcut and no external constraint.
- **Outcome:** NOT_TESTED — no clean V04 instance matching the frozen maintenance-duty/shortcut trigger; V05-V06 pending.
- **Adjudication:** V04 contains purification externalities but not a sufficiently clean repetitive-maintenance shortcut case comparable to V02 cemetery. OPEN.

### MG01-A04 — Loyalty by return, not respectful tone
- **Trigger/context:** A close party member is in serious trouble.
- **Predicted behavior:** Aqua may blame, complain, or insult while continuing to return, heal, rescue, contribute resources, or otherwise stay engaged.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V01–V03 party support; especially V03 jailbreak persistence.
- **Disconfirmation:** She disengages from a close companion's serious problem once helping becomes inconvenient, absent credible overwhelming danger.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch1 resurrection and Ch4-Ch5 persistent investigation/source purification show continued attachment/duty through action despite complaining and conflict. Aqua accepts severe burns/poison risk to preserve followers’ refuge. STRENGTHEN.

## Megumin

### MG01-M01 — Explosion identity challenge causes competitive escalation
- **Trigger/context:** Her status as Explosion specialist or Explosion's superiority is challenged.
- **Predicted appraisal:** Identity threat/competitive test rather than neutral efficiency question.
- **Predicted dominant motive:** Preserve or demonstrate chosen self-definition.
- **Predicted behavior:** She will escalate, compete, or accept practical cost to defend Explosion identity; under performance fear, competitive framing can restore confidence.
- **Confidence:** HIGH.
- **Evidence basis:** V01 deliberate specialization; V02 Wiz rivalry/Destroyer activation; V03 Yunyun and broader identity behavior.
- **Disconfirmation:** A salient Explosion-identity challenge is met with practical compromise or indifference without stronger relationship/moral inhibitor.
- **Outcome:** PARTIAL — V04 preserves Explosion identity but does not cleanly test a direct identity challenge; V05-V06 pending.
- **Adjudication:** V04 Ch5 routed terminal Explosion confirms identity-compatible confidence/reliability, but there is no strong direct challenge to Explosion superiority comparable to the frozen trigger. PRESERVE.

### MG01-M02 — Social disadvantage prompts rule/framing manipulation
- **Trigger/context:** Megumin is disadvantaged in a non-Explosion interpersonal contest.
- **Predicted appraisal:** The contest conditions themselves are negotiable resources.
- **Predicted behavior:** She will use framing, embarrassment, disgust, selective truth, rule selection, or another psychological lever rather than simply accept the weaker position.
- **Confidence:** HIGH.
- **Evidence basis:** V01 party-entry leverage; V03 Yunyun duel/framing.
- **Disconfirmation:** Repeated comparable social contests where she passively accepts a disadvantage despite obvious leverage.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch2-Ch4: Megumin helps manipulate the household into travel, reads Kazuma’s retaliation script, and immediately joins the Dustiness-status framing when institutional leverage is needed. STRENGTHEN.

### MG01-M03 — Protected identity does not eliminate group support
- **Trigger/context:** Party/companion needs resources or help that can be given without surrendering Explosion identity.
- **Predicted behavior:** Megumin will often contribute pragmatically despite abrasive or competitive presentation.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V01–V03 responsibility/loyalty, V03 mana crystal and Yunyun concern.
- **Disconfirmation:** She consistently hoards resources or refuses low-cost group help even when Explosion identity is unaffected.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch3-Ch5: voluntarily accompanies Aqua because trouble is expected, contributes to investigation/pattern recognition, and fills the Hans terminal-strike role without any Explosion-identity concession. STRENGTHEN.

### MG01-M04 — Friendly-fire meaning inhibits Explosion
- **Trigger/context:** Best tactical use of Explosion would directly endanger a valued companion.
- **Predicted appraisal:** Signature-spell reward conflicts with relationship harm.
- **Predicted behavior:** She hesitates, resists, seeks reassurance/authorization, or otherwise differs from her normal eagerness to cast.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V03 possessed Darkness climax; V01 guilt after Darkness takes curse provides analogous relational inhibition.
- **Disconfirmation:** She readily uses Explosion on a valued companion under comparable serious risk without emotional or deliberative friction.
- **Outcome:** NOT_TESTED — V04 avoids a comparable direct friendly-fire decision; V05-V06 pending.
- **Adjudication:** The Hans plan separates Megumin from protected companions before Explosion, so the V03-style valued-companion conflict is not reproduced. OPEN.

## Darkness

### MG01-D01 — Protector duty overrides self-protection
- **Trigger/context:** Companion/civilian/protected place faces credible serious threat.
- **Predicted appraisal:** Crusader/companion duty.
- **Predicted dominant motive:** Interpose/absorb/control threat.
- **Predicted behavior:** Darkness moves toward danger even when the personal cost is extreme; erotic reward may coexist but is not required to cause the intervention.
- **Confidence:** HIGH.
- **Evidence basis:** V01 curse/Beldia; V02 Destroyer; V03 Alderp bargain, Vanir, Explosion.
- **Disconfirmation:** She avoids a feasible protector role primarily to preserve herself in a serious threat to people she explicitly treats as her responsibility.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch2 Running Hawk-Kite lure and Ch5 toxic-fragment shielding place Darkness toward danger for party/task benefit at substantial personal risk. STRENGTHEN.

### MG01-D02 — Pain is poor coercive leverage
- **Trigger/context:** Another actor attempts to control Darkness mainly through threat or delivery of pain.
- **Predicted appraisal:** Pain may be rewarding rather than inhibiting.
- **Predicted behavior:** Compliance will be lower than an ordinary target's; pressure can increase persistence or erotic engagement unless another valued target is threatened.
- **Confidence:** HIGH.
- **Evidence basis:** V01 combat preference; V02 endurance; V03 Vanir possession.
- **Disconfirmation:** Pain alone reliably suppresses her resistance in a context without distinct shame, relationship, or duty stakes.
- **Outcome:** PARTIAL — V04 is supportive but not a clean pain-coercion experiment; V05-V06 pending.
- **Adjudication:** V04 Ch2 restraint/danger increases rather than suppresses Darkness’s engagement, but no opponent attempts to control her primarily through pain in a directly comparable coercion setup. PRESERVE/OPEN.

### MG01-D03 — Meaningful contribution matters
- **Trigger/context:** Darkness has a chance to land a hit, protect effectively, or gain a genuine adventuring achievement.
- **Predicted appraisal:** Opportunity for valued competence/recognition in addition to danger reward.
- **Predicted behavior:** She will pursue the contribution and show real disappointment if it is invalidated; she does not globally prefer uselessness.
- **Confidence:** HIGH.
- **Evidence basis:** V03 dolls and Vanir achievement reaction, supported by V01–V02 protector pride.
- **Disconfirmation:** Multiple genuine opportunities to contribute are deliberately sabotaged solely to preserve uselessness despite no erotic danger tradeoff.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch2 and Ch5 give Darkness genuinely useful lure/shield roles that she accepts and performs; erotic framing coexists with meaningful contribution rather than replacing it. STRENGTHEN.

### MG01-D04 — Belonging/status reclassification is a stronger vulnerability than pain
- **Trigger/context:** Her ordinary peer identity, private noble identity, or membership in the group is threatened.
- **Predicted appraisal:** Risk of losing equal companion treatment / unwanted social exposure.
- **Predicted behavior:** More genuine embarrassment, anxiety, or concession than under simple physical punishment.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V01 overheard affection; V02 relational reassurance; V03 noble reveal, childhood loneliness, `Lalatina` exposure.
- **Disconfirmation:** Comparable belonging/status threats produce only erotic enjoyment or indifference.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 Ch4-Ch5: Darkness explicitly says people change treatment after learning she is a Dustiness noble and is visibly reassured when Kazuma/Megumin/Wiz preserve ordinary peer treatment. STRENGTHEN.

## Ensemble

### MG01-E01 — High-stakes success requires asymmetric routing
- **Trigger/context:** Party encounters a serious problem exceeding one member's straightforward capability.
- **Predicted behavior:** Successful resolution will often depend on assigning each member a narrow role that converts an extreme specialty into value while constraining its associated failure mode.
- **Confidence:** HIGH.
- **Evidence basis:** V01 Beldia; V02 Destroyer; V03 dungeon/Vanir.
- **Disconfirmation:** Repeated high-stakes successes arise primarily because all four independently choose globally optimal actions without coordination or constraint.
- **Outcome:** CONFIRMED — V04 interim with two independent high-stakes replications; V05-V06 remain available.
- **Adjudication:** V04 Ch2 Running Hawk-Kite resolution and Ch5 Hans victory both require sequential routing of specialists and constraint of their failure modes rather than four independent optimal attacks. STRONGLY STRENGTHEN.

### MG01-E02 — Attachment predicts costly action better than polite speech
- **Trigger/context:** Relationship strength is tested.
- **Predicted behavior:** Rescue, worry, shared resources, responsibility, protection, or return will be stronger attachment signals than reduction in insults/blame/teasing.
- **Confidence:** HIGH.
- **Evidence basis:** All V01–V03.
- **Disconfirmation:** As relationships deepen, costly support remains absent while verbal gentleness becomes the main stable attachment marker.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 repeatedly pairs insults/pranks with resurrection, private praise, investigation for Aqua’s concrete stake, ordinary-treatment reassurance for Darkness, and life-trusting coordination during Hans. STRENGTHEN.

## Japanese language / voice

### MG01-J01 — Seriousness reduces theatricality relative to personal baseline
- **Trigger/context:** Credible harm, guilt, relationship threat, or duty override.
- **Predicted behavior:** The affected character's Japanese will tend toward shorter/directer or less performative forms relative to that character's own comic baseline, though the exact register differs by speaker.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** V01–V03 seriousness shifts in Aqua, Megumin, Darkness, Kazuma.
- **Disconfirmation:** Serious scenes consistently preserve or increase the same theatrical register with no speaker-specific reduction/shift.
- **Outcome:** CONFIRMED — V04 interim; V05-V06 remain available for further testing.
- **Adjudication:** V04 serious states visibly alter baseline performance: Megumin softens after Kazuma’s death; Aqua’s source-protection speech becomes repetitive/direct/duty-centered; Darkness’s belonging talk is comparatively plain; Hans threat pushes Kazuma into blunt survival language. STRENGTHEN.

### MG01-J02 — Most important humor is not pure wordplay
- **Trigger/context:** Notable jokes across V04-V06.
- **Predicted distribution:** More high-value jokes will be L0/L1/L2 (situation, rhythm, register, pragmatics) than L3 Japanese-form-dependent wordplay.
- **Confidence:** MODERATE.
- **Evidence basis:** V01–V03 distribution; V03 afterword independently confirms language can be unusual but does not imply wordplay dominance.
- **Disconfirmation:** V04-V06 major humor is predominantly dependent on Japanese-specific script/homophony/grammar such that mechanism substantially fails outside Japanese.
- **Outcome:** CONFIRMED — V04-level distribution; final V04-V06 distribution remains pending.
- **Adjudication:** V04’s major jokes are driven primarily by situation, causal reversal, role performance, social pragmatics, and register rather than script/homophony/grammar-dependent L3 mechanisms. PRESERVE/STRENGTHEN.

---

## Freeze rule

No prediction above may be rewritten after V04 is opened for canonical analysis. Later work may add:

- outcome;
- evidence locator;
- failure diagnosis;
- claim transition;
- revised model generated *after* adjudication.

The unmodified prediction text remains provenance for whether Model Generation 0.1 actually predicted later behavior.

---

# V05 Prospective-Validation Addendum

This section was written **after** canonical V05 analysis. It does not alter the frozen pre-V04 prediction text or erase V04 adjudications above. It records V05 evidence as a second prospective test before V06 closes Model Generation 0.1 validation.

| Prediction | V05 outcome | V05 evidence / adjudication | Transition after V05 |
|---|---|---|---|
| MG01-K01 | **CONFIRMED** | Japanese keypad/cheat-code seal and Sylvia trap again favor rule-domain exploitation; trapping Sylvia inside gives her access to Magic Killer, independently replicating the predicted post-solution consequence blind spot. | **STRENGTHEN strongly** |
| MG01-K02 | **CONFIRMED** | Kazuma worries specifically about Yunyun facing the Tranquility Girl, travels when Megumin admits concern, and acts once his facility decision visibly harms the village. | **STRENGTHEN** |
| MG01-K03 | **CONFIRMED** | nickname/payback ecology, apology extraction while captured, anger at Sylvia's interruption, and destruction of Arue's opportunistic manuscript all preserve grievance retaliation. | **STRENGTHEN** |
| MG01-K04 | **CONFIRMED** | Yunyun's false prophecy activates heroic, sexual/status and self-interested motives at once; prosocial action and selfish reward remain genuinely co-causal. | **STRENGTHEN** |
| MG01-A01 | **CONFIRMED at V05 trigger level** | status/role contexts repeatedly elicit explicit genuine-goddess claims and competitive assertion; the claim can be literally true and still socially maladaptive. V05 supports status-driven assertion more cleanly than V04's final purification did. | **PRESERVE / refine truth-vs-credibility boundary** |
| MG01-A02 | **CONFIRMED** | Vanir/sub-demon/Sylvia cues elicit fast sacred responses; Sacred Exorcism damages Sylvia while sparing adjacent Kazuma, supporting accurate domain targeting. | **STRENGTHEN** |
| MG01-A03 | **NOT_TESTED** | Game Girl distraction is a hedonic-salience case, not the frozen repetitive-maintenance-duty/maximal-shortcut trigger. | **OPEN** |
| MG01-A04 | **CONFIRMED** | after Kazuma's acute orc trauma Aqua suppresses teasing and comforts him; she continues contributing across the village crisis despite ordinary conflict. | **STRENGTHEN** |
| MG01-M01 | **CONFIRMED strongly** | Yunyun's explicit criticism of Explosion triggers immediate social counterattack and tactically premature Explosion use to prove the spell's legitimacy. | **STRENGTHEN** |
| MG01-M02 | **CONFIRMED** | Megumin uses embarrassment information, implication-heavy relationship facts, selective framing, and deliberately atypical friendship register against Yunyun/classmates. | **STRENGTHEN** |
| MG01-M03 | **CONFIRMED strongly** | Megumin publicly exposes her Explosion-only build and uses it to repair Kazuma's mistake/protect the village despite expected ridicule. | **STRENGTHEN** |
| MG01-M04 | **NOT_TESTED** | No V05 decision requires Explosion to directly endanger a valued companion under V03-like stakes. | **OPEN** |
| MG01-D01 | **CONFIRMED** | Darkness independently delays Sylvia and offers herself as substitute hostage for Kazuma. | **STRENGTHEN** |
| MG01-D02 | **PARTIAL / supportive** | pain/danger remain non-deterrent in her general behavior, but V05 has no matched attempt to coerce her through pain alone. | **PRESERVE / OPEN** |
| MG01-D03 | **CONFIRMED** | delaying, interposition and decoy roles are real contributions she willingly performs; usefulness and danger-reward coexist. | **STRENGTHEN** |
| MG01-D04 | **CONFIRMED / supportive** | noble-name performance remains genuinely embarrassing and the royal invitation triggers visible status-world anxiety; V06 will provide the stronger direct test. | **STRENGTHEN, V06 priority** |
| MG01-E01 | **CONFIRMED strongly** | Sylvia/Magic Killer resolution is another routed pipeline: Yunyun bait, local support, Megumin energy source, Kazuma rule recognition/aiming, Komekko trigger. | **STRONGLY STRENGTHEN** |
| MG01-E02 | **CONFIRMED strongly** | Aqua comforts Kazuma; Darkness substitutes herself; Megumin accepts public ridicule to repair Kazuma's mistake; Kazuma preserves Megumin's chosen identity despite utility cost. | **STRONGLY STRENGTHEN** |
| MG01-J01 | **PARTIAL — counterexample requires revision** | core-cast seriousness often still compresses/directs speech, but Yunyun becomes *more* theatrically Crimson-Demon-like under serious duty because the role performance enacts courage/belonging. | **REVISE after V06 unless overturned:** seriousness realigns register around active role/identity rather than universally reducing theatricality |
| MG01-J02 | **CONFIRMED** | major V05 humor remains dominated by situation, role/register, culture, status, causal reversal and genre pragmatics; L3 Japanese-form-only jokes remain a minority. | **STRENGTHEN** |

## V05 discoveries outside the frozen prediction set

### DISC-V05-01 — Megumin's identity hierarchy has a higher relational layer
Generation 0.1 correctly predicted that practical criticism or identity challenge would make Megumin defend Explosion. V05 reveals a different trigger: when she believes Explosion makes her a burden to valued companions, she can become willing to abandon it. The new rule is not "Explosion was never important" but:

> practical pressure -> defend Explosion; sufficiently strong belonging/contribution guilt -> possible self-sacrificial identity abandonment.

### DISC-V05-02 — Kazuma can preserve another person's identity over optimization
Kazuma repeatedly argued for practical magic in V01-V04. When given direct control of Megumin's build, he chooses more Explosion because he recognizes it as essential to the person he values. This adds an identity-recognition branch to K02/K04 that was not explicitly predicted.

### DISC-V05-03 — Yunyun exposes a voice-model direction error
The J01 mechanism "seriousness changes register" survives. Its directional claim "toward less theatricality" does not generalize. V06 should test the revised formulation before Model Generation 0.2 is frozen.

## State entering V06

- No frozen Generation 0.1 prediction has been erased.
- V05 adds strong support to most character/ensemble predictions.
- `MG01-A03` and `MG01-M04` remain the cleanest untested predictions.
- `MG01-D02` still lacks a matched coercion experiment.
- `MG01-J01` now contains genuine counterevidence and is the clearest prediction requiring **REVISE** rather than simple confidence increase.
- V06 is the final adjudication volume before Model Generation 0.2.


---

# V06 Prospective-Validation Addendum and Gen 0.1 Final Adjudication

This section was written after canonical V06 analysis. The original Gen 0.1 prediction wording above remains immutable.

| Prediction | V06 outcome / final tranche status | V06 evidence and final adjudication | Gen 0.2 transition |
|---|---|---|---|
| MG01-K01 | **CONFIRMED strongly** | Castle heist uses Snipe entry, route knowledge, detection/hide, Bind, Drain Touch, Freeze/Create Water, and staff disabling; Mitsurugi is defeated by rule/state exploitation rather than direct contest. | **STRENGTHEN; separate exploit skill from consequence forecasting** |
| MG01-K02 | **CONFIRMED strongly** | After easy retreat becomes available, Kazuma explicitly represents comfortable Axel retirement, remembers Iris, and continues the unrewarded Eris/Chris artifact mission. | **STRENGTHEN strongly** |
| MG01-K03 | **CONFIRMED** | Sabotages Darkness's suitors from admitted territorial irritation and continues low-cost score-settling in court/party contexts. | **STRENGTHEN** |
| MG01-K04 | **CONFIRMED strongly** | Castle residence, thief hunt, battlefield participation, and heist all contain simultaneously real selfish/status and relational/prosocial motives. | **STRENGTHEN** |
| MG01-A01 | **CONFIRMED across tranche, boundary refined** | V06 preserves recognition/performance capture and powerful output without contradicting V05's cleaner status-trigger confirmation; true status and overclaim must remain distinct. | **STRENGTHEN + REVISE credibility boundary** |
| MG01-A02 | **CONFIRMED across tranche** | V04–V05 provide the clean sacred-cue tests; V06 artifact sealing adds reliable narrow-domain execution. | **STRENGTHEN** |
| MG01-A03 | **NOT_TESTED** | V06 shop performance is goal substitution, not a repetitive low-status maintenance shortcut. No clean V04–V06 match. | **OPEN; modest confidence downgrade** |
| MG01-A04 | **CONFIRMED strongly** | After body-swap fallout Aqua becomes unusually gentle and brings/gets food for genuinely crushed Kazuma; large-scale support remains strong. | **STRENGTHEN** |
| MG01-M01 | **CONFIRMED** | Battle praise produces expansive Explosion identity/status performance and an avoidable advanced-magic expectation trap. | **STRENGTHEN; retain V05 higher-order relational override** |
| MG01-M02 | **CONFIRMED across tranche** | V05 direct social-framing evidence remains decisive; V06 continues strategic interpersonal behavior. | **STRENGTHEN** |
| MG01-M03 | **CONFIRMED strongly** | At royal dinner Megumin explicitly suppresses retaliation because acting would harm Darkness socially. | **STRENGTHEN + add relational inhibition** |
| MG01-M04 | **NOT_TESTED** | No V06 V03-like direct friendly-fire dilemma. | **OPEN** |
| MG01-D01 | **CONFIRMED strongly** | Darkness violates royal deference, slaps Iris, absorbs Claire's blade, and calmly defends Kazuma's dignity. | **STRENGTHEN / broaden to fairness-social protection** |
| MG01-D02 | **PARTIAL / no clean matched test** | Pain remains non-deterrent adjacent evidence, but V04–V06 do not isolate pain-only coercion. | **PRESERVE; DOWNGRADE confidence to MODERATE** |
| MG01-D03 | **CONFIRMED strongly** | Mass-battle Decoy/tanking is genuinely useful and publicly recognized. | **STRENGTHEN** |
| MG01-D04 | **CONFIRMED strongly** | Royal/noble identity pressure and need for equal peer treatment dominate V06 social stakes. | **STRENGTHEN strongly** |
| MG01-E01 | **CONFIRMED but REVISE** | Specialist routing remains predictive; mass battle shows army/institution can supply the structure without Kazuma. | **REVISE to routing-source theorem** |
| MG01-E02 | **CONFIRMED strongly** | Retrieval, defense, comfort, secret protection, identity preservation, and explicit separation anxiety dominate over politeness. | **STRENGTHEN strongly** |
| MG01-J01 | **PARTIAL / REVISE** | Darkness becomes formal-protective; Kazuma becomes more thief-theatrical after serious commitment. Direction is role-specific. | **REVISE to active-role alignment** |
| MG01-J02 | **CONFIRMED across V04–V06** | Major comedy remains situation/register/role/pragmatics/status/causal reversal; L3 remains minority. | **STRENGTHEN** |

## Gen 0.1 final result

- CONFIRMED: 16/20
- PARTIAL / revision-bearing: 2/20 (`D02`, `J01`)
- NOT_TESTED: 2/20 (`A03`, `M04`)
- FALSIFIED as complete mechanisms: 0/20

This result does **not** license rewriting the two untested predictions as true. Both remain open questions.

## V06 discoveries outside the frozen prediction set

### DISC-V06-01 — Kazuma has a separate status-overextension failure
The kobold death is not a post-transition exploit error. Success against weak targets plus desire for visible achievement causes pursuit fixation and formation loss. Gen 0.2 tracks this separately.

### DISC-V06-02 — Power/status can degrade Kazuma's restraint
The Iris-body episode shows rapid ethical slippage under automatic deference, sexual opportunity, plausible deniability, and delayed accountability. Treat literal comic intensity cautiously but preserve the directional mechanism.

### DISC-V06-03 — Routing source can be external
Aqua/Megumin/Darkness excel in conventional mass warfare without Kazuma because the military environment supplies role structure. Kazuma is best modeled as a flexible endogenous router for unstructured problems, not a universally necessary leader.

### DISC-V06-04 — Party replacement is a grievance fantasy more than a terminal preference
When efficient separation becomes plausible, Kazuma experiences exclusion anxiety and defends his existing role. Complaining about companions remains genuine without implying he wants the relationships removed.

### DISC-V06-05 — Iris merits secondary reconstruction tracking
V06 supplies sufficient variation in royal, private, competitive, city, battle, separation, and internal-POV contexts to justify longitudinal secondary tracking.

---

# Model Generation 0.2 — Frozen Predictions for V07–V09

**Freeze condition:** written after V06 and before any canonical V07 exposure. Japanese V07 is currently absent from the source corpus. These predictions may not be rewritten after V07 is opened; only outcome/adjudication fields may be added.

## Satou Kazuma

### MG02-K01 — Unstructured-problem advantage
- **Trigger/context:** A serious problem is novel, under-specified, rule-heavy, or unfavorable to direct power.
- **Prediction:** Kazuma will search for state changes, loopholes, weak-tool combinations, environment manipulation, or incentive exploits rather than compete conventionally.
- **Boundary:** if success becomes status-rewarding or an elegant transition dominates attention, he may neglect the new state created by the solution.
- **Confidence:** HIGH.
- **Disconfirmation:** repeated unstructured problems where he recognizes exploitable rules yet chooses straightforward power contests without a stronger relationship/moral reason.
- **Outcome:**
- **Adjudication:**

### MG02-K02 — Entrusted/concrete duty overrides comfortable exit
- **Trigger/context:** A trusted person entrusts Kazuma with a concrete secret responsibility or a valued companion faces preventable harm.
- **Prediction:** he may complain and seek cheaper paths, but will continue/intervene even without public reward when abandonment would directly expose the person to harm.
- **Confidence:** HIGH.
- **Disconfirmation:** feasible low-risk intervention exists, yet Kazuma knowingly abandons an established entrusted/relational duty primarily for comfort.
- **Outcome:**
- **Adjudication:**

### MG02-K03 — Status/recognition success can induce overextension
- **Trigger/context:** Kazuma is visibly succeeding, outperforming expectations, or has a low-risk-looking path to recognition/payback.
- **Prediction:** risk tolerance and pursuit length will increase; he may overextend beyond his normal safety preference.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** repeated comparable success/recognition states make him more conservative or leave risk appetite unchanged.
- **Outcome:**
- **Adjudication:**

### MG02-K04 — Actual separation threat activates attachment
- **Trigger/context:** The current party/home relationship is genuinely threatened by transfer, departure, replacement, or incompatible future plans.
- **Prediction:** Kazuma will show more distress, territoriality, bargaining, or protective action than his normal "I want a better party" rhetoric predicts.
- **Confidence:** HIGH.
- **Disconfirmation:** he accepts a credible permanent separation from established party members with sustained relief and no meaningful attempt to preserve relationship/contact despite feasible options.
- **Outcome:**
- **Adjudication:**

## Aqua

### MG02-A01 — Structured sacred/support context exposes elite competence
- **Trigger/context:** Clear institutional task in healing, purification, resurrection, support, or sealing.
- **Prediction:** Aqua's performance will be among the strongest available and her usual deployment failures will decrease because the environment supplies constraints.
- **Confidence:** HIGH.
- **Disconfirmation:** repeated clear sacred/support tasks in structured settings fail primarily through lack of ability or misunderstanding of her own domain.
- **Outcome:**
- **Adjudication:**

### MG02-A02 — Recognition/hedonic salience can replace the assigned goal
- **Trigger/context:** An instrumental task also offers attention, performance, food/alcohol, praise, or status reward.
- **Prediction:** Aqua may optimize the salient reward and partially forget the original objective even while demonstrating genuine competence.
- **Confidence:** HIGH.
- **Disconfirmation:** repeated attractive side-reward contexts leave instrumental goal discipline intact without external constraint.
- **Outcome:**
- **Adjudication:**

### MG02-A03 — Accountability is state dependent, not globally weak
- **Trigger/context:** Aqua is confronted with a harmful consequence she caused.
- **Prediction:** while a face-saving/status defense remains plausible she may resist; once causation is undeniable and defense collapses she can update, apologize, or remediate. She may also anticipate risk classes learned from repeated disasters.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** clear undeniable causation repeatedly produces persistent denial/non-remediation, or status threat never changes correction behavior.
- **Outcome:**
- **Adjudication:**

### MG02-A04 — Tedious-duty maximal shortcut remains an open targeted test
- **Trigger/context:** repetitive, low-status maintenance duty with an attractive high-power one-step alternative.
- **Prediction:** Aqua will prefer the shortcut and under-model secondary-system effects unless a prior learned analogue or strong external constraint is salient.
- **Confidence:** MODERATE.
- **Disconfirmation:** clean matched cases consistently show sustained routine/calibrated solution despite easy maximal shortcut.
- **Outcome:**
- **Adjudication:**

## Megumin

### MG02-M01 — External challenge strengthens Explosion identity; relational guilt can invert it
- **Trigger A:** outsiders/rivals question Explosion's value or Megumin's specialist status.
- **Prediction A:** defensive competition/escalation.
- **Trigger B:** Megumin concludes the specialization is materially burdening valued companions.
- **Prediction B:** she can consider self-sacrificial compromise or abandonment despite loving Explosion.
- **Confidence:** HIGH for A, MODERATE-HIGH for B.
- **Disconfirmation:** external criticism produces easy compromise, or strong relational guilt never affects specialization choices.
- **Outcome:**
- **Adjudication:**

### MG02-M02 — Companion stakes can suppress retaliation
- **Trigger/context:** Megumin is insulted/challenged but retaliation would impose a concrete cost on a valued companion.
- **Prediction:** she can inhibit or redirect the response despite anger.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** repeated clear companion-cost situations still produce uncontrolled retaliation without any attempt at inhibition.
- **Outcome:**
- **Adjudication:**

### MG02-M03 — Structured target separation amplifies practical value
- **Trigger/context:** battlefield/institution creates a dense enemy target with friendlies safely separated.
- **Prediction:** Explosion specialization becomes highly practical and Megumin performs reliably as terminal artillery.
- **Confidence:** HIGH.
- **Disconfirmation:** clean target-separated situations remain impractical for reasons intrinsic to her decision process rather than external constraints.
- **Outcome:**
- **Adjudication:**

### MG02-M04 — Direct valued-companion friendly-fire inhibition remains open
- **Trigger/context:** best tactical Explosion use would directly subject a valued companion to serious harm.
- **Prediction:** Megumin hesitates, resists, seeks consent/authorization, or otherwise differs markedly from ordinary eagerness.
- **Confidence:** MODERATE-HIGH, based mainly on V03 and not prospectively replicated in V04-V06.
- **Disconfirmation:** comparable serious friendly-fire cases produce effortless enthusiastic casting with no relational friction.
- **Outcome:**
- **Adjudication:**

## Darkness

### MG02-D01 — Protector/fairness duty can override rank and self-protection
- **Trigger/context:** a companion/protected person is threatened physically or treated in a way Darkness regards as seriously unjust.
- **Prediction:** she will accept bodily, reputational, or institutional cost to intervene.
- **Confidence:** HIGH.
- **Disconfirmation:** she preserves rank/self-protection in a feasible intervention case despite recognizing serious unjust harm to someone she treats as her responsibility.
- **Outcome:**
- **Adjudication:**

### MG02-D02 — Equal-peer belonging is more aversively sensitive than pain
- **Trigger/context:** Darkness faces either physical suffering or a threat that noble status/family role will remove her from ordinary party membership/treatment.
- **Prediction:** the latter produces more genuine anxiety/concession; pain may remain neutral or rewarding depending on meaning.
- **Confidence:** HIGH for belonging sensitivity; MODERATE for comparative pain claim.
- **Disconfirmation:** repeated belonging/status threats are eroticized or shrugged off while ordinary pain reliably controls her behavior.
- **Outcome:**
- **Adjudication:**

### MG02-D03 — Structured defense reveals elite usefulness
- **Trigger/context:** task rewards tanking, Decoy, endurance, resistance, or bodily interposition rather than accuracy.
- **Prediction:** Darkness becomes highly effective and values the contribution independently of masochistic reward.
- **Confidence:** HIGH.
- **Disconfirmation:** repeated defense-aligned contexts are deliberately sabotaged merely to preserve helplessness despite no competing erotic tradeoff.
- **Outcome:**
- **Adjudication:**

### MG02-D04 — Genuine family/party incompatibility forces negotiated rather than simple identity choice
- **Trigger/context:** noble/family obligation and party membership impose incompatible concrete demands.
- **Prediction:** Darkness will try to preserve both through negotiation, self-sacrifice, or procedural workaround before simply abandoning either identity; if forced, protector/fairness obligations to people will weigh more than prestige alone.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** she easily discards either noble/family duty or party membership for convenience/status without visible conflict.
- **Outcome:**
- **Adjudication:**

## Ensemble

### MG02-E01 — Routing source is substitutable
- **Trigger/context:** high-stakes problem involving the party's extreme specializations.
- **Prediction:** success still requires role/target/sequence structure, but the source may be Kazuma, an institution, a domain expert, or an unusually structured environment.
- **Kazuma modifier:** his added value should be highest when no external structure exists.
- **Confidence:** HIGH.
- **Disconfirmation:** repeated high-stakes success requires neither role structure nor constrained specialization, or Kazuma remains equally necessary in fully structured institutional contexts.
- **Outcome:**
- **Adjudication:**

### MG02-E02 — Efficient separation is emotionally resisted
- **Trigger/context:** an apparently rational reorganization would improve combat/social efficiency but remove established party/home relationships.
- **Prediction:** one or more members will resist, bargain, return, or impose identity/relationship costs on the efficient option; insults will not disappear.
- **Confidence:** HIGH.
- **Disconfirmation:** the core party accepts durable efficient separation with little attachment cost despite feasible relationship-preserving alternatives.
- **Outcome:**
- **Adjudication:**

## Japanese language / voice

### MG02-J01 — Seriousness aligns register to the authoritative role
- **Trigger/context:** credible duty, harm, guilt, relationship threat, or identity commitment.
- **Prediction:** voice changes toward the register associated with the role the character treats as authoritative in that state. This may be plainer, more formal, or more theatrical.
- **Confidence:** HIGH.
- **Disconfirmation:** serious-state register changes show no relationship to active role/identity and remain random/catchphrase-like.
- **Outcome:**
- **Adjudication:**

### MG02-J02 — High-value humor remains predominantly L0-L2
- **Trigger/context:** major comedic sequences across V07-V09.
- **Prediction:** situation, causal reversal, role, timing, status, register, and pragmatics will carry more important humor than Japanese-form-dependent L3 wordplay.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** V07-V09 major humor is predominantly impossible to preserve mechanistically without Japanese-specific script/homophony/grammar.
- **Outcome:**
- **Adjudication:**

## Iris — secondary reconstruction candidate

### MG02-I01 — Nondeferential safety unlocks age-level agency
- **Trigger/context:** Iris is with a trusted person who treats her as an ordinary younger peer rather than only as royalty.
- **Prediction:** curiosity, competitive behavior, ordinary wants, and tactical experimentation increase; she learns informal strategies quickly.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** later safe nondeferential contexts leave her behavior as constrained/formal as public royal contexts.
- **Outcome:**
- **Adjudication:**

### MG02-I02 — Duty suppresses wants more than ability does
- **Trigger/context:** personal desire conflicts with royal role/duty.
- **Prediction:** Iris will often self-limit or choose a smaller request rather than openly demand the desired freedom, even while privately maintaining the wish.
- **Confidence:** MODERATE-HIGH.
- **Disconfirmation:** she repeatedly prioritizes personal desire over understood royal obligations without meaningful conflict or constraint.
- **Outcome:**
- **Adjudication:**

## Gen 0.2 freeze state

Model Generation 0.2 and all predictions above are frozen **before V07 exposure**.

Former blocker resolved 2026-08-27: Japanese main-series V07 was acquired, manifest-matched, source-audited, and opened only after this frozen prediction text already existed. V07 outcomes are appended below; V08-V09 remain unexposed at this ledger state.

---

# V07 Prospective-Validation Addendum — Model Generation 0.2

This section was written **after** canonical V07 analysis. The Gen 0.2 prediction wording above remains exactly the pre-V07 freeze and is not rewritten here.

| Prediction | V07 outcome | V07 evidence / adjudication |
|---|---|---|
| MG02-K01 | **CONFIRMED strongly** | Kowloon Hydra solution changes target state through lure/Decoy/binding/land displacement/Drain Touch before terminal magic; Dustiness infiltration and wedding escape independently use weak tools, environment, voice mimicry and incentive exploits. |
| MG02-K02 | **CONFIRMED strongly** | Kazuma liquidates all remaining invention/IP rights plus accumulated reward capital and accepts legal/social risk to prevent Darkness's coerced permanent loss. |
| MG02-K03 | **PARTIAL SUPPORT** | Public Sylvia reward/praise activates `俺の時代`, generosity and status performance. No V07 case cleanly reproduces V06-style recognition-caused dangerous overextension. |
| MG02-K04 | **CONFIRMED strongly** | Darkness resignation/marriage produces loneliness, failed replacement, territorial concern, investigation, bargaining and rescue. |
| MG02-A01 | **CONFIRMED very strongly** | Aqua provides strong Hydra support/domain reasoning and instantly removes Dustiness father's hidden demonic curse with `セイクリッド・ブレイクスペル`. |
| MG02-A02 | **CONFIRMED strongly** | Heroic/status flattery plus dragon rarity/caretaking fantasy causes Aqua to spend all personal funds on the false dragon egg and reorganize attention around it. |
| MG02-A03 | **NOT_TESTED cleanly** | V07 lacks a matched case where Aqua is confronted with undeniable harmful causation and face-saving versus remediation can be adjudicated. |
| MG02-A04 | **NOT_TESTED cleanly** | Cemetery duty lapse is delay/forgetting, not a new repetitive-maintenance maximal-shortcut experiment. |
| MG02-M01 | **CONFIRMED — Trigger A branch** | Alderp explicitly challenges whether Megumin would dare use Explosion in town; she treats it as a direct identity challenge and accepts. Relational-guilt Trigger B not newly tested. |
| MG02-M02 | **PARTIAL SUPPORT** | Under wedding challenge she redirects Explosion upward rather than at the people surrounding companions, but she accepts rather than fully suppresses the challenge and still causes collateral damage. |
| MG02-M03 | **CONFIRMED strongly** | Hydra is highly practical Explosion target only after friendlies are separated, target is immobilized away from lake and regeneration resource is depleted. |
| MG02-M04 | **NOT_TESTED** | No case where the best tactical Explosion use directly subjects a valued companion to serious harm. |
| MG02-D01 | **CONFIRMED strongly** | Voluntary Hydra corpse recovery, solo danger substitution, civic/family cost absorption and wedding sacrifice all show protector duty accepting bodily/social cost. |
| MG02-D02 | **CONFIRMED strongly for belonging branch** | Resignation and uncertainty over reacceptance produce intense anxiety and unusual deference; bodily pain remains differently valenced, though no clean pain-only coercion test occurs. |
| MG02-D03 | **CONFIRMED strongly** | Successful Hydra plan depends on Decoy, endurance and physical interposition; Darkness values the real contribution. |
| MG02-D04 | **CONFIRMED very strongly** | Central plot exactly tests family/party incompatibility: Darkness tries compensation, secrecy, resignation, self-sacrificial marriage and internal investigation before abandoning either identity. |
| MG02-E01 | **CONFIRMED strongly** | Hydra success requires explicit routing by Kazuma; Vanir supplies information/liquidity structure for the marriage problem; town adventurers become distributed social support in the escape. |
| MG02-E02 | **CONFIRMED very strongly** | Supposedly efficient Darkness removal is emotionally rejected; party members bargain, sabotage replacement, rescue and explicitly restore her place through homecoming language. |
| MG02-J01 | **CONFIRMED strongly** | Serious Darkness becomes noble/protector-formal then deferential under belonging insecurity; Megumin becomes more theatrical as a `bad wizard` rescuer; Aqua weaponizes priestly ritual structure. |
| MG02-J02 | **CONFIRMED at V07 level** | Highest-value humor remains causal/situational/role/status/pragmatic L0-L2; L3 effects such as `バツネス` are secondary. |
| MG02-I01 | **NOT_TESTED** | Iris is not directly present in a qualifying safe nondeferential V07 interaction. |
| MG02-I02 | **NOT_TESTED** | No direct V07 Iris personal-desire versus royal-duty decision. |

## V07 discoveries not fully predicted by Gen 0.2

### DISC-V07-01 — Darkness protector paternalism / self-erasure
Darkness's protector system can fail procedurally: she hides burdens and removes herself so companions cannot choose to share costs. The motive remains prosocial; the error is excluding others' preference for her presence and agency to consent to sacrifice.

### DISC-V07-02 — Strongly owned goals can discipline Aqua's performance salience
Aqua's public magic outside the Dustiness estate is extravagant, but she refuses tips and uses performance as a relationship-directed lure. A02 therefore requires a goal-ownership boundary: personally internalized goals can recruit rather than lose to performance reward.

### DISC-V07-03 — Community capital becomes operational ensemble infrastructure
Axel adventurers are not scenery. Their reciprocal relation to the party affects Hydra mobilization and the wedding escape, adding community/social capital as a routing/resource layer.

### DISC-V07-04 — Kazuma care/search can precede perceived solvability
Kazuma verbally claims the marriage problem cannot be solved while researching Alderp and continuing to create saleable inventions. Concrete leverage changes commitment intensity; lack of an immediate plan does not equal lack of attachment-driven search.

## State entering V08

- Model Generation 0.2 remains frozen; no prediction above is reworded.
- V07 is the first prospective-validation volume in the V07-V09 tranche.
- V08 is the next canonical sequential operation.
- High-information open tests include MG02-A03, MG02-A04, MG02-M04, fuller K03 replication, comparative D02 pain coercion, and both Iris predictions.

---

# V08 Prospective-Validation Addendum - Model Generation 0.2

This section was written **after** canonical V08 analysis. The Gen 0.2 prediction wording above remains exactly the pre-V07 freeze and is not rewritten here.

| Prediction | V08 outcome | V08 evidence / adjudication |
|---|---|---|
| MG02-K01 | **CONFIRMED strongly** | Joint-festival rivalry/funding architecture, revised Aigis heist, and beauty-contest preference trap all solve by changing incentive/state structure rather than direct power. |
| MG02-K02 | **CONFIRMED strongly** | Accepts Chris/Eris artifact duty despite retirement preference; stays behind to draw the crowd so Eris can escape. |
| MG02-K03 | **CONFIRMED / STRENGTHEN** | Advisor praise and sales success increase pursuit intensity, project scope, status reward and reputational/social risk. V08 generalizes the mechanism beyond physical overextension. |
| MG02-K04 | **NOT_TESTED** | No credible party transfer/departure/replacement event; romantic competition is not the frozen trigger. |
| MG02-A01 | **CONFIRMED strongly** | Guild-structured insect clearing produces disciplined, high-throughput healing/buff performance. |
| MG02-A02 | **CONFIRMED very strongly** | Worship and Axis-vs-Eris prestige replace the original joint-festival instrument as the operative goal, culminating in Aqua-only demands and the pyramid-style scheme. |
| MG02-A03 | **CONFIRMED - selective-learning/state-defense pattern** | Aqua explicitly recalls overconfidence failures and regulates herself during insect clearing; later, when the scheme is exposed, she argues while status/legal face-saving remains available. Total-defense-collapse/apology branch not reached. |
| MG02-A04 | **NOT_TESTED** | No clean repetitive low-status maintenance plus maximal one-step shortcut trigger. |
| MG02-M01 | **PARTIAL SUPPORT** | Kazuma's statement that Explosion has no forest role triggers identity refusal/unauthorized casting, but the exact outsider/rival challenge or relational-guilt inversion branches are not cleanly instantiated. |
| MG02-M02 | **NOT_TESTED** | No matched insult/challenge where retaliation imposes concrete cost on a valued companion. |
| MG02-M03 | **NOT_TESTED; inverse-condition support** | Safe target separation is absent in the forest; Explosion causes collateral and worsens the tactical state, supporting the boundary rather than triggering the prediction. |
| MG02-M04 | **NOT_TESTED** | No best-use Explosion choice directly subjects a valued companion to serious harm. |
| MG02-D01 | **CONFIRMED** | Acting-lord public-order/restitution work and insect protection extend protector/fairness duty into civic administration plus physical defense. |
| MG02-D02 | **CONFIRMED strongly for meaning-sensitive branch** | Ant discomfort later becomes rewarding, while public Lalatina/sexualized-stage exposure produces genuine anger and retaliation. Meaning/agency/audience outperform raw discomfort as predictors. |
| MG02-D03 | **CONFIRMED strongly** | Guild insect operation gives Darkness the exact aggro/endurance role in which she is elite. |
| MG02-D04 | **NOT_TESTED** | No new family/party incompatibility; V08 shows post-V07 integration instead. |
| MG02-E01 | **CONFIRMED strongly** | Guild routes insect clearing; Kazuma routes festival economics and Aigis capture. Coordination source is visibly substitutable. |
| MG02-E02 | **NOT_TESTED** | No efficient reorganization that credibly removes an established party member. |
| MG02-J01 | **CONFIRMED strongly** | Darkness formal gratitude, Chris/Eris role switching, and Megumin hero-role action show role-aligned register rather than universal de-theatricalization. |
| MG02-J02 | **CONFIRMED at V08 level** | Major humor is causal/situational/status/register/pragmatic L0-L2; Japanese-form-only L3 effects remain secondary. |
| MG02-I01 | **NOT_TESTED** | Iris is absent from qualifying scenes. |
| MG02-I02 | **NOT_TESTED** | Iris is absent from qualifying scenes. |

## V08 discoveries not fully predicted by Gen 0.2

### DISC-V08-01 - Aqua learning is local rule acquisition plus state-dependent retrieval
Aqua can prospectively apply a learned failure rule and perform well. A different high-reward state can later bypass that caution without proving the earlier learning fake.

### DISC-V08-02 - Kazuma incentive engineering scales from tactics to institutions
Kazuma can design churches, merchants and sentient-object preferences into a structured outcome just as he designs combat sequences. His comparative advantage is better described as state/incentive architecture than "battle strategy."

### DISC-V08-03 - Darkness aversion is semantic/agency-sensitive
Within one volume, bodily discomfort can be reappraised into reward while public identity/sexual exposure produces genuine anger. A scalar "likes pain/humiliation" model is decisively inadequate.

### DISC-V08-04 - Eris conscientiousness can become over-compliance
Eris's duty orientation can lower refusal thresholds when sincere people ask for help, producing overload that requires another actor to create an exit.

### DISC-V08-05 - Romantic desire competes with active role rather than replacing it
Megumin can directly want Kazuma and still sacrifice desired romantic pacing to Explosion/adventurer activation. Darkness can want Kazuma and still stop escalation because fairness toward Megumin becomes salient.

## State entering V09

- Model Generation 0.2 remains frozen; no prediction above is reworded.
- V07-V08 are complete prospective-validation volumes in the V07-V09 tranche.
- V09 is the tranche-closing canonical sequential operation.
- Only after V09 may the project produce the V07-V09 checkpoint, adjudicate Gen 0.2 as a whole, freeze Model Generation 0.3, and write V10-V12 predictions before V10 exposure.


# V09 Prospective-Validation Addendum — Model Generation 0.2

**Scope:** V09 is the third and closing prospective test of the unchanged Gen02 V07–V09 predictions. Its complete Japanese main narrative was read before these outcomes were entered. Earlier-volume evidence is inherited from the pinned canonical V07/V08 readings and addenda. No V10 or withheld side narrative was used.

**Source:** `Konosuba - Main Series - Volume 09.epub`, Drive `1lIWNDsqZT9NQcoHa_ZRSqUS4j7HzYc-j`, 3,086,699 bytes, SHA-256 `a81499cd61dda060503d35d68db71c2bdc9e12e782412cf3724bca25a7f28f0e`. Narrative scope: prologue, Chapters 1–4, final chapter and both epilogues; afterword, ebook bonus, poll and other paratext excluded. Illustrations were not visually analyzed.

**Locator key:** `Pr`, `C1`, `C2`, `C3`, `C4`, `F`, `Ep1`, `Ep2` map respectively to `OEBPS/Text/part0009.xhtml` through `part0016.xhtml`. `P####` counts every body paragraph in order, including blank/image-only paragraphs. The deep reading supplies the exact unit titles and bounds.

**Provenance:** the exact Gen02 block was read and preserved at `2026-10-08T03:41:57.058948+00:00`, before V09 exposure. It remains 13,521 UTF-8 bytes with SHA-256 `7f14063864e5d1ce090d6c271dc5696d969bef1db50c31770191ce19268a7440`, from the Gen02 heading to immediately before the V07 addendum. This addendum does not fill or alter historical Gen01/Gen02 prediction fields. Their blank fields and old freeze-state statements remain historical text.

## V09 outcomes against every frozen Gen02 prediction

| Prediction | V09 outcome | Matched evidence and boundary | Claim transition |
|---|---|---|---|
| MG02-K01 | **CONFIRMED** | Siege range/exit/terrain defeats direct force; Kazuma revises the spent-spell idea, recognizes repair as a strategic state change, and combines stealth, artillery, Teleport and delegated defense. He also explicitly anticipates the counterattack. (C4 P0065–0144; F P0043–0076, P0199–0258, P0374–0391). | STRENGTHEN |
| MG02-K02 | **CONFIRMED** | A bowed, concrete request about Chomusuke succeeds after other inducements fail. Kazuma later lends relevant skills when Megumin proposes facing the danger herself, then offers help before knowing her history. (C2 P0478–0486; C4 P0164–0171; F P0473–0494). | STRENGTHEN |
| MG02-K03 | **PARTIAL** | Rank challenge and an 8–0 lead recruit boast/payback and competitive pursuit. The causal path to increased personal exposure is shared with allies’ anger and the metric. He refuses generic frontline fame and becomes uncomfortable at praise for hurting Wolbach. (C2 P0090–0248, P0353–0373; F P0434–0448). | PRESERVE |
| MG02-K04 | **NOT_TESTED** | No credible durable removal from the established household. Anticipated romantic awkwardness, an overnight outing and Iris’s letter are not the frozen separation event. (C3 P0336–0364; F P0630–0637, P0687–0721; Ep2 P0035–0041). | PRESERVE |
| MG02-A01 | **PARTIAL** | Engaged sacred/support power is strong, including purification, healing and buffs; the clean sustained institutional result is construction plus water control. That craft expands the competence map without silently redefining the frozen sacred/support-magic task category. (C3 P0238–0272; C4 P0184, P0204; F P0043–0110). | PRESERVE; new domain discovery |
| MG02-A02 | **CONFIRMED** | While assigned to delay Wolbach, Aqua replaces the task with divine-status competition and floods the fort’s damaged wall. In the repair-captain role, recognition instead reinforces days of useful work. Both directions matter. (C4 P0225–0300; F P0016–0022, P0080–0110). | STRENGTHEN; REVISE broad extrapolation |
| MG02-A03 | **PARTIAL** | Resistance to penalty coexists with healing/carrying; externally ordered repair becomes real sustained remediation. No clear apology or isolated collapse-of-defense transition is shown. (C3 P0243–0272; F P0016–0019, P0043–0110). | REVISE / OPEN |
| MG02-A04 | **NOT_TESTED** | Repair is repetitive, but an available maximal one-step alternative is not established, and the work becomes personally rewarding. Calibrated drying embedded in good construction is not the predicted reckless shortcut. (F P0054–0110). | OPEN |
| MG02-M01 | **PARTIAL** | A: imitation by Kazuma acting as a rival and Yunyun’s explicit opposition to learning Explosion provoke escalation. B: guilt concerns inability to attack or killing a benefactor, not a conclusion that the exclusive build burdens companions. (C2 P0559–0617; C4 P0082–0104; F P0412–0419, P0766–0783). | STRENGTHEN A / OPEN B |
| MG02-M02 | **PARTIAL** | A strong local failed prediction: Megumin discards the item despite Kazuma's stated money and labor cost, then maintains her rejection after he explains its purpose in supporting her request and she acknowledges possible usefulness. Kazuma later detonates it; he is a valued companion. (C2 P0592–0615). | REVISE / DOWNGRADE |
| MG02-M03 | **CONFIRMED** | Dense camps, separated friendlies and planned Teleport permit repeated reliable artillery. Later dispersal visibly weakens target availability. Effectiveness coexists with level-reward drift and attacks amid surrender pleas. (F P0199–0242, P0261–0321). | STRENGTHEN |
| MG02-M04 | **AMBIGUOUS** | Adverse near-match: Megumin blasts companions away and leaves Darkness unconscious without expressed hesitation. The full original conjunction of best tactical Explosion use, valued companion and serious harm is not cleanly isolated. Her anticipation of the harm remains an explanatory uncertainty, not an added frozen trigger requirement. (C2 P0235–0271; contrast C4 P0206–0208; F P0007–0015, P0365–0419). | DOWNGRADE / OPEN |
| MG02-D01 | **CONFIRMED** | Darkness interposes against the dragon zombie despite fear and sustains injury/armor loss; she also shields debris and accepts fort responsibility. Not every bandit pursuit is pure duty. (C2 P0549–0553; C3 P0213–0272, P0512–0529; C4 P0146–0163). | STRENGTHEN |
| MG02-D02 | **PARTIAL** | The binding episode distinguishes wanted sensation, genuine bodily distress and personal dignity; Darkness explicitly rejects the explanation that only noble pride is at stake. No clean V09 paired exclusion-versus-pain test occurs. (C1 P0177–0208, P0274–0281, P0334–0365, P0417–0433). | STRENGTHEN components / OPEN comparison |
| MG02-D03 | **CONFIRMED** | Interposition protects others, even though the dragon’s force overwhelms her armor and consciousness. She is assigned to fort defense for appropriate capacity and later values the contribution. (C2 P0549–0553; C3 P0223–0263; C4 P0075–0077; F P0199–0212; Ep1 P0019–0024). | STRENGTHEN |
| MG02-D04 | **NOT_TESTED** | Command duty conflicts with the proposal to retreat, but does not establish a new concrete family/party-membership incompatibility. It is a bounded institutional analogue. (C4 P0063, P0146–0163). | PRESERVE |
| MG02-E01 | **PARTIAL** | The siege strongly supports distributed role/target/sequence organization. The contest also destroys all enemies after Megumin interrupts the cooperative plan, at friendly cost. The frozen statement did not pre-register a controlled-success metric. (C2 P0235–0271; C4 P0136–0144; F P0054–0110, P0199–0258, P0286–0316). | REVISE |
| MG02-E02 | **NOT_TESTED** | Raiding and fortress roles split labor while membership and return remain intact. Household wishes and the homecoming invitation support attachment but do not enact a durable efficient separation. (C1 P0343–0374; F P0199–0245, P0549–0551; Ep1 P0017–0026). | PRESERVE |
| MG02-J01 | **CONFIRMED** | Vulnerable request, specialist declaration, repair-captain authority, conflicted Crimson Demon duty, ordinary companion invitation and awkward consolation display role-conditioned language. Seriousness does not have one direction of formality/theater. (C2 P0478–0486; C4 P0082–0104; F P0054–0094, P0459–0484, P0534–0544, P0784–0815). | STRENGTHEN |
| MG02-J02 | **CONFIRMED** | Major farces and reversals depend mainly on situation, timing, status and pragmatics. The written charm/babysitting contrast is a real local L3 case; the additive recognition clue is chiefly portable pragmatics and serves a serious payoff. (C1 P0061–0118, P0295–0485; C2 P0188–0271; C3 P0099–0138; C4 P0256–0300; F P0043–0174; Ep2 P0035–0041). | STRENGTHEN qualitative support |
| MG02-I01 | **NOT_TESTED** | Iris’s letter preserves familiar address and a request, but supplies no direct safe nondeferential interaction or agency comparison. (Ep2 P0035–0040). | OPEN |
| MG02-I02 | **NOT_TESTED** | The letter asks escort to a meeting with her betrothed, but does not establish Iris’s private wish, conflict with duty or deliberate choice of a smaller request. Kazuma’s reaction is not her decision. (Ep2 P0036–0041). | OPEN |

Whole-prediction totals: **8 CONFIRMED, 7 PARTIAL, 6 NOT_TESTED, 1 AMBIGUOUS, 0 FALSIFIED**. These are coverage classifications, not a success rate. MG02-M02 contains a clear local failed prediction and MG02-M04 contains actual adverse bodily collateral. A zero whole-prediction FALSIFIED count does not mean no failures occurred.

## Adjudication boundaries and adverse evidence

**M02 is a real negative case.** Kazuma is an established valued companion. He states the money and labor cost before Megumin discards the item. He then explains its expedition purpose; she acknowledges potential utility but maintains her rejection. Kazuma subsequently detonates the discarded item (V09 C2 P0599–0615). The frozen trigger says “concrete cost,” not only bodily harm. Adding a bodily-harm requirement now would rewrite the test. The whole prediction remains PARTIAL because its possibility/repeated-disconfirmation wording and V07 partial redirection do not justify rejecting all regulatory capacity. The companion-cost brake is nevertheless unreliable under a directly challenged core specialty. (V09 C2 P0592–0606; unchanged MG02-M02; V07 M02.)

**M04 must not be rescued by changing the relationship category.** The contest's Explosion blasts companions away and leaves Darkness unconscious without expressed hesitation. That is adverse evidence. The full original conjunction—best tactical Explosion use, valued companion and serious harm—is not cleanly isolated. Her anticipation of harm is an explanatory uncertainty, not an added condition in the frozen trigger. Wolbach-related hesitation is powerful new evidence for a valued-target mechanism, but a benefactor/opponent is not the literal companion-friendly-fire condition. AMBIGUOUS keeps both facts visible. (V09 C2 P0235–0271; C4 P0206–0208; F P0007–0015, P0365–0419; unchanged MG02-M04.)

**E01's unqualified necessity claim cannot be protected by a new success definition.** The major siege supports role/target/sequence organization strongly, and its providers are distributed. The earlier contest also ends in enemy destruction after Megumin interrupts a cooperative plan, at friendly cost. The frozen sentence did not predefine success as safe, controlled, ethically acceptable completion. The revised model therefore predicts observable deployment benefits under specified comparisons and records those outcome dimensions separately. It does not retroactively exclude the adverse scene by changing the metric. (V09 C2 P0235–0271; F P0054–0110, P0199–0258, P0286–0316; V07/V08 E01.)

**A03 is not fully confirmed by visible repair.** Aqua heals/carries Darkness despite resisting a penalty and repairs the wall after being sent to do so. This defeats a global no-remediation account. Yet external direction, professional pleasure and recognition alignment remain causal alternatives to an internal transition from undeniable blame through collapsed defense to accepted responsibility. V08 already isolated selective learning and face-saving defense; it did not establish the missing collapse branch. The complete accountability mechanism remains PARTIAL. (V09 C3 P0243–0272; F P0016–0019, P0043–0110; V08 A03.)

**A01, M01 and D02 require scope discipline.** V09 construction is legitimate new Gen03 domain evidence but is not retroactively folded into the original institutional sacred/support-magic test; V07/V08 already support that original condition. M01's rivalry branch is strongly replicated, while guilt about killing a teacher is not guilt that an exclusive build burdens companions. D02's belonging and meaning-sensitive components are strong, while the comparative pain claim remains less directly isolated. Whole-row judgments must preserve these asymmetries. (V09 C2 P0559–0617; C4 P0082–0104; F P0043–0110, P0412–0419, P0766–0783; C1 P0177–0433; V07/V08 A01, M01, D02.)

# V07–V09 Tranche Closeout — Model Generation 0.2

**Adjudication closed:** `2026-10-08T04:05:05.195463+00:00`. The complete tranche is **13 CONFIRMED, 5 PARTIAL, 3 NOT_TESTED and 1 AMBIGUOUS** across all 22 original predictions. V07 and V08 outcome wording below is preserved verbatim, including branch and qualification language. Favorable early evidence does not cancel V09 adverse evidence. Tranche decisions and confidence transitions are recorded separately from the immutable historical tests.

| Prediction | V07 outcome — preserved | V08 outcome — preserved | V09 | Tranche | Claim transition |
|---|---|---|---|---|---|
| MG02-K01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-K02 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-K03 | **PARTIAL SUPPORT** | **CONFIRMED / STRENGTHEN** | **PARTIAL** | **CONFIRMED** | PRESERVE |
| MG02-K04 | **CONFIRMED strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-A01 | **CONFIRMED very strongly** | **CONFIRMED strongly** | **PARTIAL** | **CONFIRMED** | PRESERVE; new domain discovery |
| MG02-A02 | **CONFIRMED strongly** | **CONFIRMED very strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN; REVISE broad extrapolation |
| MG02-A03 | **NOT_TESTED cleanly** | **CONFIRMED - selective-learning/state-defense pattern** | **PARTIAL** | **PARTIAL** | REVISE / OPEN |
| MG02-A04 | **NOT_TESTED cleanly** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |
| MG02-M01 | **CONFIRMED — Trigger A branch** | **PARTIAL SUPPORT** | **PARTIAL** | **PARTIAL** | STRENGTHEN A / OPEN B |
| MG02-M02 | **PARTIAL SUPPORT** | **NOT_TESTED** | **PARTIAL** | **PARTIAL** | REVISE / DOWNGRADE |
| MG02-M03 | **CONFIRMED strongly** | **NOT_TESTED; inverse-condition support** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-M04 | **NOT_TESTED** | **NOT_TESTED** | **AMBIGUOUS** | **AMBIGUOUS** | DOWNGRADE / OPEN |
| MG02-D01 | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-D02 | **CONFIRMED strongly for belonging branch** | **CONFIRMED strongly for meaning-sensitive branch** | **PARTIAL** | **PARTIAL** | STRENGTHEN components / OPEN comparison |
| MG02-D03 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-D04 | **CONFIRMED very strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-E01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **PARTIAL** | **PARTIAL** | REVISE |
| MG02-E02 | **CONFIRMED very strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-J01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-J02 | **CONFIRMED at V07 level** | **CONFIRMED at V08 level** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN qualitative support |
| MG02-I01 | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |
| MG02-I02 | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |

## Confidence transitions and failure diagnoses

| Prediction | Confidence disposition | Failure diagnosis / coverage limit |
|---|---|---|
| MG02-K01 | HIGH → HIGH | No matched failure of indirect search. Missing opponent information defeats an early plan; preparedness and complete forecasting are separate from inventive capacity. |
| MG02-K02 | HIGH → HIGH | Commitment precedes assured solvability. Risk calculation and later incentives coexist with care; no abandonment for comfort in a clean entrusted-duty case. |
| MG02-K03 | MODERATE-HIGH → MODERATE-HIGH | V08 supplies the cleaner prospective match. Do not rename every successful raid, forgotten item or later danger as recognition-caused overextension. |
| MG02-K04 | HIGH → HIGH; no V09 gain | Missing trigger in V09; the genuine V07 resignation/marriage case remains the matched evidence. |
| MG02-A01 | HIGH → HIGH | Domain/activation qualification. Sleeping delays deployment; the full ambush also fails through status drift. V07/V08 independently confirm the original institutional-domain condition. |
| MG02-A02 | HIGH → HIGH, conditional on reward alignment | Goal substitution is directly supported. The failed generalization is that praise itself necessarily produces failure; task-aligned recognition is a strong countercondition. |
| MG02-A03 | MODERATE-HIGH → MODERATE for complete causal rule | Selective learning/state defense survives from V08. External direction, skill enjoyment and role ownership compete with the proposed internal accountability mechanism. Remediation is not proof of accepted blame. |
| MG02-A04 | MODERATE → MODERATE; unvalidated | Missing conjuncts: persistently low-valued duty plus attractive maximal alternative. No confirmation or falsification by analogy. |
| MG02-M01 | A HIGH → HIGH; B MODERATE-HIGH inherited | Compound prediction: A is replicated; B is not tested in this tranche. Do not substitute target-specific grief for build-abandonment evidence. |
| MG02-M02 | MODERATE-HIGH → MODERATE for broad cost rule | Missing identity/stake variable: core-specialty defense defeats ordinary companion-cost restraint. The full disconfirmation clause asks for repeated uncontrolled cases; V07 also preserves partial redirection. PARTIAL must not hide the local failure. |
| MG02-M03 | HIGH → HIGH | Tactical suitability is supported; ethical adequacy and larger-goal discipline are separate. The ally-blasting contest is not a positive safe-separation test. |
| MG02-M04 | MODERATE-HIGH → MODERATE | Actual collateral cannot be discarded as a gag. Wolbach is a valued benefactor/opponent, not a current companion directly harmed by the tactical shot; that inhibition is a new related discovery, not a rescued confirmation. |
| MG02-D01 | HIGH → HIGH | Costly protective action is directly observed. Her fantasy-driven delay and later narrator dismissal do not erase it or establish universal sound judgment. |
| MG02-D02 | Belonging HIGH → HIGH; comparison MODERATE → MODERATE | V07 tests belonging strongly; V08/V09 test meaning and agency. The exact comparative pain claim remains less isolated than those supported components. |
| MG02-D03 | HIGH → HIGH, with finite durability | Equipment/opponent-force limit, not sabotage or zero usefulness. Do not invent individual unseen feats in the general fortress fighting. |
| MG02-D04 | MODERATE-HIGH → MODERATE-HIGH; no V09 gain | Missing exact trigger. V07 remains the direct matched case; duty alone must not be inflated into permanent identity separation. |
| MG02-E01 | Necessity HIGH → MODERATE; bounded deployment HIGH | An unqualified necessity theorem is too broad. Do not redefine success after the fact to erase the adverse case. Gen03 separately tracks target destruction, safe deployment, goal completion and ethics. |
| MG02-E02 | HIGH → HIGH; no V09 gain | Missing trigger; accepting temporary deployment is compatible with resisting permanent relationship loss. V07 remains the direct prospective test. |
| MG02-J01 | HIGH → HIGH | Preserve independent role evidence and speaker/addressee context; no personality inference from an isolated particle and no role invented only after reading the line. |
| MG02-J02 | MODERATE-HIGH → MODERATE-HIGH | Qualitative major-sequence judgment, not an exhaustive joke census or percentage. Japanese importance does not automatically imply Japanese-only form dependence. |
| MG02-I01 | MODERATE-HIGH inherited; no tranche gain | Missing trigger; a mentioned character is not necessarily an observed behavioral test. |
| MG02-I02 | MODERATE-HIGH inherited; no tranche gain | Missing motive/decision evidence. Do not import a future journey or infer an unwanted engagement to manufacture a test. |

The canonical checkpoint `04 Checkpoints and Model Validation/KONOSUBA_V07-V09_CHECKPOINT.md` provides the complete model, six checkpoint responsibilities, high-information unknowns and CP03 claim definitions. The Gen03 block below is a new generation. Its newly specified conditions must never be imported backward to rescue Gen02. In particular the narrow MG03-M05 knowledge/grave-harm condition is new; the original MG02-M04 trigger was best tactical Explosion use / valued companion / serious harm.

## Gen03 freeze receipt and handover boundary

Model state and the complete prediction set were frozen at **`2026-10-08T04:33:35.790540+00:00`**, after the Gen02 tranche closed and before V10 exposure. The checkpoint §3 model is 17,746 UTF-8 bytes, SHA-256 `dfd92578ddef97eeaf942a6a5d713f37a84678abc9433bce05d36d2ec659d85a`. The exact prediction block beginning below is **45,675 UTF-8 bytes**, SHA-256 **`ebe83ef5dc87fc2e85f8f711e2ba373239d4eea4fd14f466537dbd3625d76150`**. Hash from the first `#` of its Gen03 heading for that exact byte count, including the final trailing LF; use UTF-8/LF, no BOM or reflow. This block is byte-identical to the checkpoint block.

All 25 Outcome and 25 Adjudication fields remain blank. V10 is next only after verified integration; it was not opened in this analytical session, including after the freeze. Side narratives remain withheld for later validation. The historical V08 terminal statement that Gen03 must wait for V09 remains preserved above; this additive closeout records that the gate has now been satisfied.

**Receiver correction RC-V09-01 (2026-10-08; outside the frozen text):** In CP03-M05, “Equipment destruction” overstates Megumin's agency. At C2 P0599–0615 she takes the item, hears its money/labor cost (P0600), discards it (P0602), then hears its expedition purpose (P0605) and acknowledges possible utility while maintaining rejection (P0606). Kazuma subsequently ignites and detonates it (P0608–0615). Read the frozen evidence shorthand as disposal despite explicit cost, not destruction by Megumin. The MG02-M02 PARTIAL disposition and local cost-inhibition failure remain supported. The frozen model and prediction wording, hashes, confidence and scoring criteria are preserved; this additive correction was made before any receiving-session V10 exposure.

# Model Generation 0.3 — Frozen Predictions for V10–V12

**Derivation boundary:** Japanese main-series V01–V09 main narrative only. Gen 0.2's V07–V09 outcomes have been closed before this new set is frozen. Gen 0.1 and Gen 0.2 retain their original wording and historical outcomes.

**Freeze state:** FROZEN_BEFORE_V10. The freeze receipt in the checkpoint and integration handoff identifies the UTC time, exact block byte count and SHA-256. V10–V12 have not been opened in this analytical session. This is a session source-exposure control, not a claim that a pretrained model has never encountered the series.

**Evidence basis:** CP03 claim identifiers resolve to the current-model section of `KONOSUBA_V07-V09_CHECKPOINT.md`. All V09 locators below are in the verified EPUB: `0014:P0043–0110` means `OEBPS/Text/part0014.xhtml`, all-body-paragraph enumeration, inclusive. V07/V08 references mean the unchanged canonical prospective addenda for the stated MG02 IDs; they are inherited evidence, not fresh primary rereadings of those volumes.

**Evaluation rules:** determine the trigger, relationship, stakes and available choices before scoring the response. Missing conjuncts produce NOT_TESTED or explicitly partial/ambiguous coverage; they do not count as successful predictions. Record negative cases with the same detail as positive cases. Where a tendency is tested repeatedly, retain all matched cases rather than replacing them with a favorable aggregate. Score distinct predicted branches separately; one observed branch cannot confirm an entire compound prediction. This applies especially to K01 search/revision/delegation, M04 action friction/aftermath and E01 deployment/provider/Kazuma comparisons. A single contrary outcome is adverse evidence even when a repeat-pattern disconfirmation threshold is not met. Keep capacity, target destruction, safe deployment, goal completion and ethical evaluation separate. New qualifications learned in V10–V12 belong in outcome/revision fields, never in the frozen text below.

## Satou Kazuma

### MG03-K01 — Indirect construction of a solution, with explicit resource limits
- **Trigger/context:** a serious novel or under-structured problem disadvantages Kazuma in direct power, and he can identify at least one usable rule, tool, environmental feature or incentive.
- **Relationship/stakes:** combat or institutional stakes; distinguish strangers from valued people whose safety constrains available tactics.
- **Predicted appraisal:** the apparent power contest can be changed by altering state, sequence, information or other actors' incentives.
- **Predicted dominant motive:** obtain a workable outcome at lower personal exposure while retaining agency over the method.
- **Predicted behavior:** he will try an indirect combination or negotiated arrangement and revise it when a newly learned capability invalidates the first plan. He will delegate phases that suit stronger specialists. This predicts search and revision, not universal first-plan success or possession of every needed resource.
- **Interaction tendency:** practical instructions and explicit division of responsibility; opportunistic or unflattering framing may coexist with correct mechanics.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K01, CP03-E01; V07/V08 MG02-K01; V09 `0013:P0065–0144`, `0014:P0043–0076`, `P0199–0258`, `P0374–0391`.
- **Disconfirmation:** repeated matched problems with acknowledged usable indirect options instead produce conventional power contests or passive abandonment, without an independently established relational or moral reason; or he repeatedly cannot revise after the failed assumption is explicitly exposed.
- **Outcome:**
- **Adjudication:**

### MG03-K02 — Concrete entrusted need recruits effort before certainty
- **Trigger/context:** a trusted person makes a concrete request whose refusal would leave that person or a valued companion exposed to preventable harm, and Kazuma has some feasible contribution even if no complete solution is known.
- **Relationship/stakes:** established trust, actual cost or danger; generic appeals to heroism, fame or attractiveness alone do not supply this trigger.
- **Predicted appraisal:** this is a particular person's problem that he can help reduce, not simply optional public work.
- **Predicted dominant motive:** preserve the person/relationship while reducing the cost of intervention.
- **Predicted behavior:** he will complain, bargain, investigate, prepare or seek a cheaper route, but make a substantive contribution rather than abandon the responsibility chiefly for comfort. Commitment may precede a fully credible success plan.
- **Interaction tendency:** ordinary or grumbling speech can accompany costly help; a polished heroic declaration is not required.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K03; V07/V08 MG02-K02 and DISC-V07-04; V09 `0011:P0478–0486`, `0013:P0164–0171`, `0014:P0473–0494`.
- **Disconfirmation:** a clear, feasible contribution exists, but he knowingly leaves the established person exposed primarily to preserve leisure, with no meaningful help, search or relationship-preserving alternative.
- **Outcome:**
- **Adjudication:**

### MG03-K03 — Success-linked personal reward can expand pursuit
- **Trigger/context:** Kazuma receives concrete success feedback or sees an apparently manageable opportunity for recognition/payback, and that personal reward is visibly active before his next decision about scope, pursuit or exposure, whether or not the plan subsequently changes.
- **Relationship/stakes:** initially tolerable perceived risk; compare the same task before and after feedback. Success without evidence of recognition/payback salience is insufficient.
- **Predicted appraisal:** he can obtain more advantage, status or retaliation than the original task required.
- **Predicted dominant motive:** extend the rewarding success state.
- **Predicted behavior:** he will increase scope, pursuit, taunting or accepted exposure relative to his prior plan. Newly explicit severe danger or harm to a personally known target may instead restore caution; record these pre-existing modifiers before judging the outcome.
- **Interaction tendency:** victory/credit language or grievance display should accompany the expansion more often than purely duty-based explanation.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** CP03-K02; V08 MG02-K03; V09 partial test `0011:P0090–0248`; limiting cases `0013:P0065–0097`, `0014:P0434–0448`.
- **Disconfirmation:** repeated comparable success-plus-personal-reward states leave pursuit unchanged or make it more conservative despite no new threat/relationship cue. Forgotten equipment alone does not count as confirmation.
- **Outcome:**
- **Adjudication:**

### MG03-K04 — Noticed actual tears can interrupt intimate or teasing pursuit
- **Trigger/context:** during an interaction Kazuma is pursuing for personal intimate or teasing reward, a valued companion begins shedding actual tears that he notices; he can pause or ask without creating a separate immediate danger. Near-tears or verbal refusals alone do not supply this narrowed cue.
- **Relationship/stakes:** familiar companion, salient vulnerability; this is not a prediction of general consent reliability or kindness to every person.
- **Predicted appraisal:** the interaction may be harming the person rather than providing mutually wanted play or closeness.
- **Predicted dominant motive:** reduce the recognized distress and clarify what the person needs, in conflict with his immediate desire and embarrassment.
- **Predicted behavior:** he will interrupt the immediate pursuit and ask, assist or wait. Continued desire, awkward self-exoneration and later opportunism may remain, but knowingly continuing the same unwanted pursuit is adverse evidence.
- **Interaction tendency:** flustered questions or blunt, self-involving reassurance are more likely than effortless moral eloquence.
- **Confidence:** MODERATE; a new cue-specific hypothesis, not a global rehabilitation claim.
- **Evidence basis:** CP03-K03/04; positive V09 cue-response sequences `0010:P0427–0433`, `0014:P0752–0815`; adverse earlier verbal-distress phases `0010:P0312–0336`, `P0417–0426`; renewed opportunism `0010:P0436–0454`; wider limits `0012:P0336–0386`, `0014:P0701–0749`, `0016:P0016–0034`. This is a newly narrowed Gen03 hypothesis; it does not reinterpret those earlier refusals as acceptable or unrecognized.
- **Disconfirmation:** after noticing actual tears in a matched companion interaction, he continues the immediate self-rewarding pursuit without checking, helping or pausing, despite an available low-cost pause. Do not infer that he failed to notice the cue merely because he continued. Earlier verbal-distress failures remain contrary evidence to any broader stopping rule.
- **Outcome:**
- **Adjudication:**

## Aqua

### MG03-A01 — Established specialist ability appears under a well-defined task
- **Trigger/context:** a clearly bounded task uses an ability already demonstrated in the derivation corpus: healing, purification, resurrection, support/sealing, or practiced construction/art with water control where relevant.
- **Relationship/stakes:** institutional or explicitly organized service; sufficient access and resources. Record sleep, distraction and activation separately from the quality of execution.
- **Predicted appraisal:** this is a task within a recognized area of her expertise.
- **Predicted dominant motive:** execute the familiar service and/or display mastery.
- **Predicted behavior:** once engaged, she will perform at a high level relative to available alternatives, with fewer task errors when goals and boundaries are clear. This does not grant competence in unobserved technical domains or guarantee readiness at the required moment.
- **Interaction tendency:** confident directives, demonstration or professional pride may be accurate rather than empty boasting.
- **Confidence:** HIGH for the established domains.
- **Evidence basis:** CP03-A01; V07/V08 MG02-A01; V09 `0012:P0238–0272`, `0014:P0043–0076`, `P0080–0110`.
- **Disconfirmation:** repeated engaged, adequately resourced tasks in these established domains fail chiefly through lack of ability or misunderstanding of the domain. A new craft is not assumed mastered merely because construction was.
- **Outcome:**
- **Adjudication:**

### MG03-A02 — A direct prestige contest can displace an assigned purpose
- **Trigger/context:** an ongoing instrumental assignment is interrupted by a challenge to Aqua's divinity, followers, superiority or public recognition, and the prestige contest offers a response distinct from completing the task.
- **Relationship/stakes:** the challenger need not be a friend; the original assignment and its constraints must be identifiable before the challenge.
- **Predicted appraisal:** letting the status claim stand is immediately intolerable or more salient than the task.
- **Predicted dominant motive:** compel acknowledgment or win the status contest.
- **Predicted behavior:** she will escalate assertion, performance or power use and loosen at least one original task constraint. Competent ability may magnify the collateral cost. Directly acknowledged imminent harm can be a competing cue, but must be observed rather than inferred after the fact.
- **Interaction tendency:** self-naming, divine/faction titles, demands for apology or mirrored disparagement.
- **Confidence:** HIGH for the trigger class; exact severity remains uncertain.
- **Evidence basis:** CP03-A02; V08 MG02-A02; V09 `0013:P0256–0300`, `0014:P0016–0022`.
- **Disconfirmation:** repeated clear prestige challenges leave the separate assigned goal and constraints intact without another actor preventing escalation or independently acknowledged imminent harm already competing with it. Other proposed explanations remain rival accounts or adverse evidence for revision, not automatic exclusions.
- **Outcome:**
- **Adjudication:**

### MG03-A03 — Recognition attached to real service can sustain it
- **Trigger/context:** Aqua has a task she demonstrably knows how to do, receives recognition specifically for doing it, and has an identified beneficiary or responsibility rather than a separate status contest.
- **Relationship/stakes:** repeated service or repair, with the rewarded role tied to the required work. Record whether the assignment is externally imposed, voluntarily owned, or both.
- **Predicted appraisal:** continued good work demonstrates the valued role and sustains acknowledgment.
- **Predicted dominant motive:** enjoy mastery, trusted responsibility and recognition together.
- **Predicted behavior:** she will continue useful performance across repeated opportunities instead of necessarily abandoning it for spectacle. She may add display or share rewards while the core task remains completed. Corrective action need not be preceded by an apology.
- **Interaction tendency:** role-title uptake and confident instruction can reinforce performance.
- **Confidence:** MODERATE-HIGH; supported by V07 owned-goal performance and the extended V09 repair sequence.
- **Evidence basis:** CP03-A02/03; DISC-V07-02; V09 `0014:P0016–0019`, `P0043–0110`.
- **Disconfirmation:** despite a still-aligned recognition/service structure and no independently observed material interruption, resource loss, immediate danger or distinct prestige contest, repeated opportunities instead produce refusal, goal abandonment or merely decorative output without the required service. One externally forced action alone is not positive evidence for voluntary ownership.
- **Outcome:**
- **Adjudication:**

### MG03-A04 — Unvalued maintenance with an available maximal shortcut
- **Trigger/context:** repetitive maintenance remains low in Aqua's expressed valuation and a concretely available, attractive one-step high-power alternative is established.
- **Relationship/stakes:** no salient learned analogue or strong external constraint already rules out the shortcut; all these conditions must be checked before counting a test.
- **Predicted appraisal:** the rapid high-output method avoids tedious work.
- **Predicted dominant motive:** remove the immediate burden quickly.
- **Predicted behavior:** she will prefer the shortcut while giving insufficient attention to a secondary system it affects.
- **Interaction tendency:** confident simplification or dismissal of labor may accompany the choice; no special phrase is required.
- **Confidence:** MODERATE, inherited and still unvalidated in the V07–V09 tranche.
- **Evidence basis:** CP03-A04; V04–V06 checkpoint §5 and unchanged MG02-A04; V09 `0014:P0054–0110` is a non-test/countercondition, not confirming evidence.
- **Disconfirmation:** matched cases repeatedly show calibrated routine performance despite the available shortcut, with no learned analogue or external constraint already accounting for it. Mere speed, effective drying or any manual work does not establish the trigger.
- **Outcome:**
- **Adjudication:**

## Megumin

### MG03-M01 — Core-specialty challenge can outweigh ordinary companion cost
- **Trigger/context:** a rival, including a companion acting as a rival, explicitly denigrates, replaces or imitates Explosion in a way Megumin treats as a challenge to her specialist identity.
- **Relationship/stakes:** ordinary financial, equipment, convenience or status cost to companions is known; neither an independently expressed conclusion that her build seriously burdens them nor an independently recognized imminent grave companion-harm cue is active before her response. Record mixed-trigger episodes separately rather than deriving eligibility from which motive wins.
- **Predicted appraisal:** the challenge attacks a defining value rather than offering a neutral efficiency improvement.
- **Predicted dominant motive:** preserve the legitimacy and distinctiveness of Explosion.
- **Predicted behavior:** she will defend, compete, reject the replacement or retaliate; known ordinary companion cost alone will not reliably secure compromise. Record any attempt at redirection rather than treating all escalation as uncontrolled.
- **Interaction tendency:** specialist naming, theatrical assertion and precise denial of equivalence.
- **Confidence:** HIGH for defensive identity activation; MODERATE for its priority over known companion utility.
- **Evidence basis:** CP03-M01/05; V07 MG02-M01 and partial MG02-M02; V09 `0011:P0559–0617`, `0013:P0082–0104`.
- **Disconfirmation:** repeated clean identity challenges lead to easy compromise because of ordinary companion cost alone, without visible identity conflict, retaliation or an independently evidenced higher-order burden/harm appraisal.
- **Outcome:**
- **Adjudication:**

### MG03-M02 — Internally accepted contribution guilt can reopen the build
- **Trigger/context:** Megumin herself concludes that her exclusive specialization materially prevents her from contributing to valued companions, rather than merely hearing an opponent's criticism.
- **Relationship/stakes:** established companions; the perceived burden is substantial and attributed to the build, not inability to attack one particular person.
- **Predicted appraisal:** protecting the specialty may conflict with remaining useful and wanted.
- **Predicted dominant motive:** preserve contribution and belonging, despite genuine love of Explosion.
- **Predicted behavior:** she will seriously consider compromise, a changed role or abandonment of the exclusive build, with visible loss or reluctance. Others' reassurance may alter the decision, but should not erase the initial conflict.
- **Interaction tendency:** quieter, apologetic or explicit cost language is expected when the self-appraisal is expressed; the role is no longer only that of a challenged rival.
- **Confidence:** MODERATE-HIGH as inherited from V05; not prospectively validated by V07–V09.
- **Evidence basis:** CP03-M02; V04–V06 checkpoint §6 and unchanged MG02-M01 Trigger B. A changed-role option is a Gen03 extension, not an already validated outcome; neither it nor the inherited trigger received a matched V07–V09 test. V09 `0014:P0412–0419`, `P0766–0783` are distinct target/guilt cases, not validation of this build-burden trigger.
- **Disconfirmation:** repeated explicit, substantial self-attributed build burdens produce no meaningful conflict or consideration of compromise, even when a feasible alternative is recognized.
- **Outcome:**
- **Adjudication:**

### MG03-M03 — Safe separated targets expose reliable artillery
- **Trigger/context:** a target within Explosion's established capacity/range is dense or immobilized; friendlies are safely separated; resource use and the post-cast exit/carry requirement are planned.
- **Relationship/stakes:** no identified valued person occupies the target role. The conditions must be established before evaluating the result.
- **Predicted appraisal:** the task offers a legitimate, technically suitable use of the chosen specialty.
- **Predicted dominant motive:** perform and demonstrate Explosion effectively.
- **Predicted behavior:** she will execute reliable terminal fire, making the specialization highly useful for that task. This predicts tactical efficacy; it does not predict restraint toward defeated enemies or sound choice of the campaign's larger objective.
- **Interaction tendency:** exuberance and theatrical display may coexist with accurate execution; a full incantation is not required for demonstrated V09-level control.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-M03; V07 MG02-M03; V09 `0014:P0199–0242`, `P0261–0304` are matched deployment evidence; `P0534–0544` supports technical capacity only because its personally valued target does not match this prediction. The incantation is omitted there, while the spell name is voiced.
- **Disconfirmation:** repeated fully matched target/resource/exit cases fail because of her own ordinary target-selection or execution process, despite no new relational inhibition or external interference.
- **Outcome:**
- **Adjudication:**

### MG03-M04 — A valued target creates a separate firing constraint
- **Trigger/context:** a task calls for decisive harm to someone whom the source independently establishes as personally valued by Megumin through rescue, teaching, gratitude or another significant relationship.
- **Relationship/stakes:** that person is now an opponent or obstacle; technical feasibility and urgent reasons to act may both be present.
- **Predicted appraisal:** the target carries a relationship obligation that cannot be reduced to a combat category.
- **Predicted dominant motive:** reconcile protection/duty with attachment or gratitude.
- **Predicted behavior:** she will show meaningful hesitation, a search for acknowledgment/choice, or inability to execute before or during a personally meaningful acknowledgment or choice; acting need not resolve subsequent guilt. If she acts, immediate celebratory ease is less likely than residual emotional cost. Record pre-action relational friction and post-action emotional cost separately. The mechanism does not depend on a target merely looking human.
- **Interaction tendency:** direct relational address or an attempted personal question can interrupt ordinary specialist theater.
- **Confidence:** MODERATE; repeated moments within one central V09 conflict are not independent cross-person replications.
- **Evidence basis:** CP03-M04; V09 `0014:P0007–0015`, `P0365–0419`, `P0473–0544`, `P0766–0816`.
- **Disconfirmation:** a comparably established valued-target conflict produces effortless execution without meaningful pre-action relational friction despite the salient bond. This is adverse to the firing-constraint component even if regret follows. Easy celebration without meaningful emotional aftermath is separately adverse to the aftermath component. A target with no such history is not a test.
- **Outcome:**
- **Adjudication:**

### MG03-M05 — Explicit serious companion harm remains a guarded prediction
- **Trigger/context:** Megumin knows that the best available tactical Explosion use would directly expose a valued companion to grave bodily harm, with the risk and alternatives made clear in the source.
- **Relationship/stakes:** current valued companion; establish anticipated harm magnitude, Megumin's knowledge, alternatives and the tactical requirement independently. Minor displacement without established anticipated grave injury is distinct; uncertain severity remains ambiguous/adverse collateral, not automatically harmless comedy. An enemy's attack is not her own friendly-fire choice.
- **Predicted appraisal:** success would impose a personally unacceptable relational cost unless it is justified or authorized.
- **Predicted dominant motive:** protect the companion while responding to the tactical need.
- **Predicted behavior:** she will hesitate, object, seek consent/authorization, redirect, or otherwise show clear friction relative to ordinary enthusiastic casting.
- **Interaction tendency:** explicit concern or negotiation is evidence; a token catchphrase is not.
- **Confidence:** MODERATE, downgraded from the broad Gen 0.2 extrapolation because of V09 adverse collateral evidence and lack of a clean matched replication. This explicitly specified grave-harm/knowledge trigger is a narrowed Gen03 hypothesis, not a wording-identical continuation of MG02-M04.
- **Evidence basis:** CP03-M05; V04–V06 checkpoint §6 / unchanged MG02-M04; adverse V09 `0011:P0254–0271`; distinct care evidence `0013:P0206–0208`.
- **Disconfirmation:** a clean matched case produces enthusiastic casting without relational friction despite her explicit understanding of the grave companion risk. Do not reclassify an adverse matched outcome as harmless comedy after observing it.
- **Outcome:**
- **Adjudication:**

### MG03-M06 — Repeated rewarding fire can become its own objective
- **Trigger/context:** a sustained operation repeatedly permits safe, effective Explosion and provides visible skill/experience growth or equivalent specialist reward; the original instrumental objective is approaching completion or has weakened.
- **Relationship/stakes:** impersonal enemy/obstacle targets; no independently active valued-target or grave companion-harm conflict.
- **Predicted appraisal:** another opportunity to fire/grow remains desirable even when marginal mission value falls.
- **Predicted dominant motive:** continue the specialty reward.
- **Predicted behavior:** she will seek additional casts, denser targets or an extended opportunity; a companion may need to restate the original goal. Tactical success can persist while goal discipline declines.
- **Interaction tendency:** language of casting, spectacle or growth will increasingly replace the original mission rationale.
- **Confidence:** MODERATE; a new extrapolation from the multi-day V09 sequence.
- **Evidence basis:** CP03-M03/05; V09 `0014:P0268–0321`, especially `P0286–0316`.
- **Disconfirmation:** repeated matched reward sequences lead her to stop or narrow use when the instrumental objective is achieved, without an external limit or another already established higher-priority conflict.
- **Outcome:**
- **Adjudication:**

## Darkness / Dustiness Ford Lalatina

### MG03-D01 — Protector contribution survives fear and finite endurance
- **Trigger/context:** a person Darkness treats as her responsibility faces serious harm or injustice, and she has a feasible defensive or institutional intervention.
- **Relationship/stakes:** a protected person or companion; distinguish chosen fantasy danger from an independently visible threat to someone else.
- **Predicted appraisal:** she has a responsibility to absorb or oppose the threat.
- **Predicted dominant motive:** protect and contribute, even where fear, embarrassment or bodily reward also exists.
- **Predicted behavior:** she will accept bodily, reputational or institutional cost. In a defense-aligned task she will use interposition/endurance rather than deliberately preserve helplessness. Equipment and opponent force may still overwhelm her.
- **Interaction tendency:** protector/noble assertions or blunt action may precede concern for her own comfort.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-D01; V07/V08 MG02-D01/D03; V09 `0011:P0549–0553`, `0012:P0213–0272`, `0013:P0075–0077`, `P0146–0163`.
- **Disconfirmation:** despite recognizing serious unjust harm and a feasible contribution, she preserves rank/self-protection chiefly for convenience, or repeatedly sabotages the needed defensive role merely to remain helpless.
- **Outcome:**
- **Adjudication:**

### MG03-D02 — Agency, audience and belonging determine aversion
- **Trigger/context:** a sought, bounded scenario acquires unchosen public exposure, reduced control, or an explicit threatened change from equal party membership. Establish the changed condition from the event and previously expressed preferences independently of her present reaction.
- **Relationship/stakes:** identify who controls the event, who witnesses it and what standing is threatened; mere physical intensity does not define the trigger.
- **Predicted appraisal:** the changed agency, audience or standing threatens dignity or belonging previously valued outside the desired scenario.
- **Predicted dominant motive:** restore agency, dignity or ordinary belonging.
- **Predicted behavior:** genuine protest, anxiety, negotiation, anger or defensive concealment will increase rather than the event being uniformly welcomed. This does not settle how pain alone would work as coercion.
- **Interaction tendency:** she may abandon playful fantasy for direct personal objection or unusually deferential belonging requests, depending on the identified threat.
- **Confidence:** HIGH for meaning/belonging sensitivity; MODERATE for comparative generalization across pain conditions.
- **Evidence basis:** CP03-D02; V07/V08 MG02-D02; V09 `0010:P0177–0208`, `P0334–0365`, `P0417–0433`.
- **Disconfirmation:** repeated matched, independently established agency/audience/belonging changes are uniformly enjoyed or dismissed while the source shows no protest, anxiety or attempt to recover control; ordinary pain by itself cannot confirm this prediction.
- **Outcome:**
- **Adjudication:**

### MG03-D03 — Incompatible obligations recruit costly preservation attempts
- **Trigger/context:** family/noble/civic duty and continued party membership make genuinely incompatible concrete demands.
- **Relationship/stakes:** obligations to identifiable people on both sides, rather than an abstract preference for prestige or temporary deployment apart.
- **Predicted appraisal:** simply dropping either responsibility would betray a valued part of her life.
- **Predicted dominant motive:** protect people and preserve both commitments if possible.
- **Predicted behavior:** she will try negotiation, procedural workarounds or personally costly absorption before easy abandonment. Her V07 secrecy/self-erasure remains a possible procedural error; protective intent does not guarantee shared decision-making.
- **Interaction tendency:** duty language may conceal personal need; other members may need to challenge her assumption that she must bear the cost alone.
- **Confidence:** MODERATE-HIGH, chiefly inherited from the direct V07 test.
- **Evidence basis:** CP03-D03; V07 MG02-D04 / DISC-V07-01; V09 `0013:P0146–0163` is a bounded command-obligation analogue, not a new full family/party test.
- **Disconfirmation:** she discards either established relationship or recognized duty for convenience or prestige without visible conflict or preservation attempt despite feasible alternatives.
- **Outcome:**
- **Adjudication:**

## Ensemble

### MG03-E01 — Explicit task organization improves deployment but is not sufficient
- **Trigger/context:** a serious multi-stage problem requires several established specialist capacities, and source evidence permits comparison between missing/misaligned organization and an arrangement with explicit roles, targets, resources and handoffs. Classify these arrangements and incentive alignment independently of the eventual result.
- **Relationship/stakes:** record practical task completion, friendly harm, goal discipline and moral objections separately. Temporary allocation apart does not mean loss of membership.
- **Predicted appraisal:** participants identify a usable contribution when the arrangement fits their actual abilities and incentives.
- **Predicted dominant motive:** solve the common task while preserving salient individual values.
- **Predicted behavior:** the aligned arrangement will improve reliable deployment relative to the earlier missing/misaligned state: more intended specialist actions completed at assigned targets/times, fewer failed handoffs, or fewer missing required resources. A capable institution/domain expert can supply the arrangement. Where it has not been supplied, Kazuma will more often initiate or repair it; where another actor supplies it, successful deployment need not depend on his continuing direction. Score deployment improvement, alternative-provider adequacy and Kazuma's comparative contribution separately. A concealed target relationship or misaligned reward can still disrupt a technically sound plan.
- **Interaction tendency:** directives, signaling, handoffs and corrections will make the practical arrangement visible; do not infer organization merely from eventual victory.
- **Confidence:** HIGH for the bounded deployment mechanism; no universal necessity or sufficiency theorem is claimed.
- **Evidence basis:** CP03-E01; V07/V08 MG02-E01; V09 contrast `0011:P0120–0271` with `0014:P0054–0110`, `P0199–0258`; relational failure `0014:P0365–0419`.
- **Disconfirmation:** across comparable multi-stage problems, explicit alignment produces no improvement in deployment, or specialist availability alone repeatedly yields equally reliable safe task completion without observable coordination; also adverse is persistent dependence on Kazuma despite an alternative arrangement independently shown to supply the required roles, resources and handoffs.
- **Outcome:**
- **Adjudication:**

### MG03-E02 — Durable efficient separation incurs attachment costs
- **Trigger/context:** a feasible reorganization promises practical efficiency but credibly removes an established core party/home relationship for a sustained period.
- **Relationship/stakes:** established members, meaningful permanence; ordinary raids, errands, a night out or romantic awkwardness alone do not qualify.
- **Predicted appraisal:** the proposal loses something valued beyond instrumental usefulness.
- **Predicted dominant motive:** retain relationship, membership or meaningful contact.
- **Predicted behavior:** one or more core members will resist, bargain, return, protect contact or bear a cost to preserve the bond. Ordinary insults need not soften and temporary tactical separation can remain acceptable.
- **Interaction tendency:** relationship/home language and practical restoration attempts are stronger evidence than generic declarations that everyone is friends.
- **Confidence:** HIGH, based on the direct V07 test and supporting household behavior.
- **Evidence basis:** CP03-E02; V07 MG02-K04/E02; V09 `0010:P0343–0374`, `0014:P0549–0551`, `0015:P0017–0026` provide non-test supporting evidence.
- **Disconfirmation:** durable efficient separation is accepted with sustained relief and little attachment cost despite feasible ways to preserve the established relationship.
- **Outcome:**
- **Adjudication:**

## Japanese voice and humor

### MG03-J01 — Register tracks an independently established active role
- **Trigger/context:** a scene independently establishes a change in duty, identity, vulnerability or relationship stakes, and gives enough dialogue/narration for a local before/after comparison.
- **Relationship/stakes:** identify speaker, addressee, audience and role from action or explicit semantic commitment before scoring the surface wording. A commitment's semantic content may establish the role, but its formal wording may not simultaneously establish that role and serve as the successful language outcome.
- **Predicted appraisal/motive:** the active role supplies the terms through which the speaker seeks authority, safety, recognition or care.
- **Predicted behavior and voice:** the following mappings predict directions of change: Megumin's challenged specialist identity increases specialist self-identification and competitive assertion; personal gratitude or vulnerable appeal increases direct relational address/request. Aqua's service authority increases practical directives, while divine-status contest increases self-legitimation and demands for acknowledgment. Darkness's public duty increases institutional/protector framing; dignity threats increase direct objection; belonging insecurity increases requests for acceptance. Kazuma's companion-care turn increases questions, ordinary offers or self-disclosure relative to immediate grievance/reward rhetoric.
- **Coding rule:** before classifying the language outcome, record the independently evidenced role, select the applicable mapping and fix the local comparison window around the semantic change. Score each mapping separately. Keep the assignment when unchanged or opposing wording appears; it is adverse evidence. Insufficient comparable speech is NOT_TESTED. Neutral connective speech and exact lexical choices are not themselves outcomes.
- **Confidence:** HIGH for role conditioning; no deterministic sentence-ending or catchphrase rule.
- **Evidence basis:** CP03-J01; V07/V08 MG02-J01; V09 `0011:P0478–0486`, `0013:P0082–0104`, `0014:P0054–0094`, `P0459–0484`, `P0534–0544`, `P0784–0815`.
- **Disconfirmation:** repeated matched role changes yield unchanged or opposite patterns to the fixed mapping, or apparent fit depends on inventing/reassigning a role after seeing the wording. One confirmed mapping cannot conceal adverse results in another.
- **Outcome:**
- **Adjudication:**

### MG03-J02 — Comic episodes are predominantly portable or pragmatic
- **Trigger/context:** a census of qualifying comic episodes in the complete authorized V10–V12 main narratives, pooled across the tranche. Per-volume patterns are reported separately, but the formal prediction concerns the pooled set.
- **Relationship/stakes:** no character-specific condition. Identify episode eligibility and boundaries independently of L-class. Include verbal/written-form episodes and recurrent gags even when the only consequence is an immediate response or narrator retort; brevity alone is not an exclusion.
- **Inclusion/segmentation rule:** an episode presents an expectation or stance and a comic reversal, violation, contrast or response. A continuous run around the same premise counts once, including nested jokes; a later callback counts separately only when a new scene supplies its own setup/response. Record every eligible episode with its source locator before assigning the primary mechanism. Do not select only action-based or plot-consequential scenes.
- **Predicted appraisal/motive:** not applicable to a single character; this is a distributional literary prediction.
- **Predicted effect:** more than half the eligible episodes will have a primary comic mechanism preserved through situation, causal reversal, timing, role or ordinary register/pragmatic equivalents (L0–L2), rather than requiring Japanese-specific reconstruction or annotation (L3).
- **Classification/scoring boundary:** log clear L0–L2, clear L3, mixed and uncertain cases separately. For a completed nonempty census, CONFIRMED requires clear L0–L2 cases to exceed half of all eligible episodes even assigning every unresolved case to L3. FALSIFIED applies when L0–L2 cannot exceed half even assigning every unresolved case to L0–L2; this includes a fully resolved tie. AMBIGUOUS applies when unresolved cases can change whether the strict majority is reached. An empty eligible set is NOT_TESTED. Incomplete census permits only PARTIAL qualitative reporting, not a tranche frequency claim. Cultural dependence is flagged separately. This new frequency test does not retroactively quantify Gen02's qualitative major-sequence judgment.
- **Confidence:** MODERATE for this more explicitly operationalized test, based on prior qualitative evidence.
- **Evidence basis:** CP03-J02; V07/V08 MG02-J02; V09 deep reading §§7–8. Written-form `お守り`: `0010:P0061`, `P0081–0083`, `P0116–0118` (L3). Additive `も`: `0014:P0179`, `P0537` (chiefly L2, exact-wording sensitivity); this serious recognition payoff is not added to the humor census merely because it is linguistically important.
- **Disconfirmation:** the completed census establishes failure of the strict L0–L2 majority under the bound rule above, including a fully resolved tie. A result achieved only by excluding short form-dependent episodes or changing boundaries after classification is invalid evidence, not confirmation.
- **Outcome:**
- **Adjudication:**

## Secondary reconstruction candidates

### MG03-Y01 — Inclusion and a useful role recruit Yunyun's competent participation
- **Trigger/context:** trusted companions explicitly include Yunyun in a shared undertaking, including accepting her offer to join, and give her access to a role suited to her established magic or practical knowledge.
- **Relationship/stakes:** a real invitation/role rather than a hypothetical promise; distinguish desire for company from agreement with every action of the group.
- **Predicted appraisal:** she can belong by making a useful contribution.
- **Predicted dominant motive:** participate and help while preserving the valued connection.
- **Predicted behavior:** she will prepare and carry out the relevant role despite awkwardness or anxiety, sometimes overpreparing or overoffering. Moral or relational distress may produce objections without immediately ending participation; distress or interrupted commitment under a directly conflicting personal obligation remains context to record; it is not automatically a failed technical execution.
- **Interaction tendency:** hesitant acceptance can coexist with technically effective direction and explicit disagreement.
- **Confidence:** MODERATE-HIGH for affiliation-mediated participation; not a mature full-character model.
- **Evidence basis:** CP03-Y01; V07 deep reading / relationship ledger Yunyun support; V09 `0011:P0641–0658`, `0012:P0152–0160`, `0013:P0154–0156`, `0014:P0199–0242`, `P0305–0310`, `P0378–0391`, `P0459–0467`, `0015:P0025–0026`.
- **Disconfirmation:** repeated genuine invitations with feasible familiar roles produce sustained indifferent refusal or poor participation unrelated to a documented conflicting obligation, ability/resource limit or coercive condition.
- **Outcome:**
- **Adjudication:**

### MG03-CE01 — Conscientious service can exceed Chris/Eris's preferred burden
- **Trigger/context:** in her public divine/service role, Chris/Eris receives sincere requests whose cumulative burden exceeds what she explicitly prefers, and a refusal or exit is possible.
- **Relationship/stakes:** distinguish publicly owed duty from casual trusted companionship; identify her own expressed burden, not an observer's assumption that she must be tired.
- **Predicted appraisal:** refusal would disappoint people who reasonably seek her help.
- **Predicted dominant motive:** meet sincere obligations.
- **Predicted behavior:** she will tend to continue past her preferred burden until a boundary is negotiated or another actor supplies an exit. A successful self-set boundary is adverse evidence for the over-compliance tendency and should not be reclassified as its confirmation.
- **Interaction tendency:** service politeness may differ from the familiar Chris register she asks trusted companions to use.
- **Confidence:** MODERATE; chiefly a V08 discovery with no V09 replication.
- **Evidence basis:** CP03-CE01; unchanged DISC-V08-04 and V08 Chris/Eris findings; V09 absence supplies no additional validation.
- **Disconfirmation:** repeated matched cumulative burdens elicit timely, comfortable self-limitation without significant conflict or externally created relief.
- **Outcome:**
- **Adjudication:**

### MG03-I01 — Safe nondeferential interaction expands Iris's agency
- **Trigger/context:** Iris is directly shown with a trusted person who treats her as an ordinary younger peer in a setting with less formal royal surveillance.
- **Relationship/stakes:** compare her behavior with an observed constrained public context; a letter alone does not supply the contrast.
- **Predicted appraisal:** ordinary curiosity, experimentation and wants can be expressed without immediate royal correction.
- **Predicted dominant motive:** learn, play or exercise age-appropriate agency.
- **Predicted behavior:** curiosity, informal strategy learning, competition or ordinary requests will become more visible than in the constrained setting.
- **Interaction tendency:** familiar address and less inhibited interaction may accompany the behavioral change; honorifics alone do not prove the mechanism.
- **Confidence:** MODERATE-HIGH as inherited from V06; V07–V09 provide no matched test.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I01; V09 `0016:P0035–0040` only preserves the letter boundary.
- **Disconfirmation:** repeated safe nondeferential settings leave her equally constrained, with no predicted behavioral expansion despite available ordinary choices.
- **Outcome:**
- **Adjudication:**

### MG03-I02 — An expressed wish may be narrowed by understood royal duty
- **Trigger/context:** the source directly establishes both a personal wish of Iris's and a royal obligation she understands as conflicting with it.
- **Relationship/stakes:** genuine duty conflict; do not infer an unwanted obligation or hidden wish merely from formal engagement, travel or an escort request.
- **Predicted appraisal:** the larger personal wish exceeds what the role permits.
- **Predicted dominant motive:** preserve duty while obtaining a smaller part of the desired freedom or connection.
- **Predicted behavior:** she will tend to self-limit or choose a reduced request while the original wish remains expressed or otherwise directly evidenced.
- **Interaction tendency:** restrained petition may coexist with familiar attachment language; the source must establish the motive rather than the analyst supplying it.
- **Confidence:** MODERATE-HIGH as inherited from V06; still unvalidated in V07–V09.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I02; V09 `0016:P0036–0041` is not a matched decision.
- **Disconfirmation:** repeated explicit wish/duty conflicts produce unconstrained prioritization of the wish without meaningful conflict or self-limitation, despite understood obligations.
- **Outcome:**
- **Adjudication:**

## Gen 0.3 freeze state

These 25 predictions are the complete Gen 0.3 set for V10–V12. No outcome or adjudication field above is populated. V10 remains unopened in this session. The next analyst must retrieve and preserve this exact block before the first V10 narrative exposure and append evidence without rewriting its triggers, confidence, boundaries or disconfirmation language.


# V10 Local Prospective Validation — Frozen Model Generation 0.3

**Status:** V10 local adjudication complete; V10–V12 tranche OPEN. This is the first prospective volume against the 25 predictions frozen after V09. It is an additive outcome record, not a new model generation, tranche checkpoint or replacement freeze. V11 and V12 remain UNOPENED in this analytical continuation; V11 is the next unit only after new authorization and its continuation/source gate.

**Prospective provenance:** the exact Gen03 prediction block was retrieved, read and preserved before V10 narrative exposure. It remains **45,675 UTF-8 bytes**, SHA-256 **`ebe83ef5dc87fc2e85f8f711e2ba373239d4eea4fd14f466537dbd3625d76150`**. The frozen model remains **17,746 bytes**, SHA-256 **`dfd92578ddef97eeaf942a6a5d713f37a84678abc9433bce05d36d2ec659d85a`**. All original prediction wording, confidence, disconfirmation language and 25 blank Outcome/25 blank Adjudication fields are preserved. The preceding freeze-state statement that V10 was unopened is a historical statement about the freeze session, not the live state after this append. Gen01/Gen02 wording, all historical outcomes and the V09 receiving correction RC-V09-01 remain intact.

**Source/evidence scope:** verified Japanese V10 EPUB, **1,630,298 bytes**, SHA-256 **`8b1d8befe7dc2562a9d3eb57e6c455b1a114b98af52594404e647194fd2e1733`**. Complete sequential reading covered only `text/part0009.html`–`text/part0015.html`: prologue, Chapters 1–5 and epilogue, **3,026 all-body paragraphs**. `Pr`, `C1`–`C5` and `Ep` below map to those seven files in order; `P####` counts every body `<p>`, including blank/image-only paragraphs. Ruby base and reading pairs were retained for exact-language verification. The narrative text was read completely before coding, without gaps. Illustrations were not visually inspected. Afterword, ebook bonus, other paratext, V11+, withheld side narrative and external series knowledge do not contribute evidence. Earlier-volume findings are inherited canonical evidence, not fresh earlier-primary rereadings. This is a session exposure control, not a claim about pretraining.

**V10 results:** **6 CONFIRMED, 6 PARTIAL, 13 NOT_TESTED, 0 AMBIGUOUS, 0 FALSIFIED.** These are local coverage judgments, not an accuracy score or a completed-tranche verdict. Missing trigger conjuncts do not count as successful predictions. A zero whole-row falsification count does not erase local failures, contrary components, poor planning or untested branches. The strict local convention reserves NOT_TESTED for incomplete clean triggers even when adjacent behavior is informative; PARTIAL is used for actual branch coverage or an explicitly incomplete comparative/distributional claim.

| Prediction | V10 outcome | Main boundary |
|---|---|---|
| MG03-K01 | PARTIAL | Search/delegation supported; exact new-capability revision branch incompletely tested. |
| MG03-K02 | CONFIRMED | Concrete entrusted need recruits sustained help. |
| MG03-K03 | CONFIRMED | Reward-salient success accompanies expanded pursuit/exposure; duty remains a rival motive. |
| MG03-K04 | NOT_TESTED | Actual-tears conjunction not cleanly established; wider distress insensitivity remains adverse. |
| MG03-A01 | CONFIRMED | Engaged familiar support works; fugu readiness failure remains separate. |
| MG03-A02 | CONFIRMED | Direct follower/status insult disrupts diplomatic restraint. |
| MG03-A03 | NOT_TESTED | One admired meal does not establish repeated post-recognition service. |
| MG03-A04 | NOT_TESTED | Maintenance/maximal-shortcut conjunction absent. |
| MG03-M01 | PARTIAL | Identity activation clear; known companion-utility priority not isolated. |
| MG03-M02 | NOT_TESTED | No self-attributed substantial exclusive-build burden. |
| MG03-M03 | NOT_TESTED | Capacity shown; prospective safe geometry/resource/exit arrangement unshown. |
| MG03-M04 | NOT_TESTED | No personally valued decisive-harm target. |
| MG03-M05 | NOT_TESTED | No clear knowingly grave companion-risk Explosion choice. |
| MG03-M06 | NOT_TESTED | Additional reward hunting is not a fully matched sustained weakening operation. |
| MG03-D01 | CONFIRMED | Defensive contribution and costly escape protect others. |
| MG03-D02 | PARTIAL | Audience aversion supported; coercive control also enjoyed. |
| MG03-D03 | NOT_TESTED | No incompatible demand on continued party membership. |
| MG03-E01 | PARTIAL | Deployment repair supported; alternative-provider/comparative branches incomplete. |
| MG03-E02 | NOT_TESTED | Temporary separation does not meet the durable relationship-loss trigger. |
| MG03-J01 | PARTIAL | Multiple fixed mappings supported; some mappings remain untested. |
| MG03-J02 | PARTIAL | V10 contribution only; formal pooled V10–V12 result remains open. |
| MG03-Y01 | NOT_TESTED | Useful accompaniment reported; invitation/accepted-role sequence unshown. |
| MG03-CE01 | NOT_TESTED | No observed Chris/Eris cumulative service-burden choice. |
| MG03-I01 | CONFIRMED | Trusted ordinary access expands visible agency. |
| MG03-I02 | NOT_TESTED | Self-restriction visible; exact original-wish/duty conjunction incomplete. |

## MG03-K01 — Indirect construction of a solution, with explicit resource limits

- **V10 outcome:** PARTIAL.
- **Trigger and evidence:** aid negotiations give Kazuma serious institutional stakes without direct sovereign power. Prince decision authority, favorable economic information and noble credentials are available before use (C3 P0235–0247, P0464–0479, P0618–0643). He redirects the negotiation, exploits the precisely worded coin-location rule (C4 P0139–0197, P0257–0279), and subsequently uses casino access, luck and status leverage (C5 P0203–0213, P0243–0342). At the dragon he assigns reserve fire and support after Darkness independently initiates her decoy role (C5 P0097–0111). In captivity he adapts ignition to Darkness's greater strength after she initiates gag removal (C5 P0622–0660).
- **Adverse or untested branches:** indirect search and delegation are supported. Revision after a specifically newly learned capability invalidates the first plan is not cleanly replicated; changed political information and failure of brute force support flexibility without supplying that exact condition. The false-flag raid fails before infiltration (C4 P0318–0337); the later capture plan fails when his threat frightens its targets into escape (C5 P0347–0372). Iris defeats Ragcraft as the would-be rescuers try to open her door, before they can intervene (C5 P0699–0707).
- **Causal/model disposition:** PRESERVE/STRENGTHEN indirect search and bounded delegation; OPEN the exact capability-revision branch. Noble privilege, exceptional luck, Iris's force and Darkness's initiative remain independent contributors. Frozen HIGH confidence is preserved, not globally revalidated by one observed branch.

## MG03-K02 — Concrete entrusted need recruits effort before certainty

- **V10 outcome:** CONFIRMED.
- **Trigger and evidence:** Iris explicitly requests restraint because aid is essential (C3 P0651–0656); Darkness entrusts her protection to Kazuma when barred from the next meeting (C4 P0012–0020); Megumin later asks him to help the discouraged Iris (C5 P0216–0227). Kazuma has feasible information, negotiation and gaming contributions before a complete funding route is known. He returns across the negotiations, joins the dragon expedition, and keeps searching after its reward fails to meet the goal (C4 P0097–0108, P0244–0293; C5 P0097–0126, P0191–0236, P0243–0408).
- **Adverse or untested branches:** mixed status, retaliation and intimate reward motives coexist with help. The original escort acceptance alone does not establish that Iris already disclosed an unwanted marriage (C1 P0042–0046). Several methods are poorly judged or unsuccessful; this prediction concerns substantive contribution, not guaranteed success or ethically sound means.
- **Causal/model disposition:** STRENGTHEN concrete entrusted-help mechanism; retain HIGH confidence and the distinction between commitment, plan quality and outcome. No comfort-based abandonment appears in the matched requests.

## MG03-K03 — Success-linked personal reward can expand pursuit

- **V10 outcome:** CONFIRMED, bounded causal attribution.
- **Trigger and evidence:** card-game success, gamer excitement and dominance are visible before he demands further opponents and continues for hours (C3 P0193–0226). At the casino, repeated color wins, others' awe and his superior treatment of Darkness precede larger numbered bets (C5 P0279–0299); successful status leverage and Iris's admiration precede the next numbered wager (P0301–0322). Continued pressure on the state casino follows over several days (P0376–0399).
- **Adverse or untested branches:** the casino still serves an unmet aid objective, so duty and exploitation of favorable odds compete with reward continuation. Kazuma rejects Megumin's proposed all-in recovery after a loss (C5 P0339–0342); he also explains why a gambling career would expose him without current protection (P0313–0318). Neither is a clean unchanged pursuit following newly rewarding success without a new threat/context. The false-flag raid was already a fallback plan (C4 P0293), so it is not clean evidence that success newly created escalation. Additional offensive aid was part of the original mission, not automatically scope inflation.
- **Causal/model disposition:** STRENGTHEN the bounded success/reward tendency; preserve MODERATE-HIGH confidence. Do not make exceptional luck or narrator-attributed bad luck into a controlled causal experiment.

## MG03-K04 — Noticed actual tears can interrupt intimate or teasing pursuit

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** no clean conjunction of noticed actual companion tears, Kazuma's immediate intimate/teasing reward pursuit, and an available safe pause is established. Darkness is described as near crying or tearful-eyed during the bodily-care sequence (C1 P0123, P0132, P0144), while his earlier enjoyment of harassment is explicit (P0130). C3 P0447 gives sob-like vocalization during Megumin's humiliation but no explicit tears; Kazuma is complicit and gloating (P0448–0451).
- **Adverse or untested branches:** these interactions remain adverse to any broader distress-stopping or consent-reliability claim. Urgent bodily need complicates the first pause condition but does not excuse later teasing generally. Aqua's crying over used alcohol is not followed by a shown continued intimate/teasing pursuit by Kazuma (C2 P0445, P0458). The crying game opponent is a stranger (C3 P0210). The late apparent Megumin seduction is Ragcraft's impersonation (C5 P0500–0534), not real Megumin vulnerability.
- **Causal/model disposition:** OPEN; retain MODERATE confidence in the newly narrowed hypothesis without strengthening it. Missing actual-tears evidence is not proof that distress was absent or acceptable.

## MG03-A01 — Established specialist ability appears under a well-defined task

- **V10 outcome:** CONFIRMED within the established domains.
- **Trigger and evidence:** Aqua releases magical restraints that Darkness regarded as unremovable (C1 P0097–0100, P0143–0144). Iris requests support for the dragon and Kazuma assigns it; Aqua supplies defense and attack enhancement (C5 P0040–0042, P0102–0111). Support before the return-route confrontation is reported at C5 P0358. Water provision is immediately effective (C5 P0056–0059).
- **Adverse or untested branches:** fugu care fails because Aqua drinks herself asleep; the party reaches the Eris church (C1 P0222, P0234–0255, P0259–0279). No engaged antidote cast fails, but the serious readiness failure remains visible. Her ambiguous chancellor detection and later failure to identify the impostor limit broader diagnostic claims (C3 P0594–0602; C5 P0682–0694; Ep P0024–0032).
- **Causal/model disposition:** PRESERVE/STRENGTHEN engaged familiar specialist ability, HIGH confidence. Keep execution quality, availability and general perception separate; no new-domain competence is granted.

## MG03-A02 — A direct prestige contest can displace an assigned purpose

- **V10 outcome:** CONFIRMED.
- **Trigger and evidence:** diplomatic restraint is an identifiable constraint before a courtier compares Aqua's followers to troublesome monsters (C3 P0491–0493, P0564–0569). She demands an apology and faction acknowledgment; the prince's fear and later exclusion order show consequences for the assignment (P0570, P0698).
- **Adverse or untested branches:** in the interrogation, gratitude and identification as an archpriest lead to divine self-revelation, renewed confinement and rejection of the bell's apparent reliability (C4 P0444–0461). This is a useful recognition-driven analogue but lacks an overt insulting challenge. Costly disappearance performance (C3 P0318–0321) lacks a shown preceding prestige challenge; gambling losses are not automatically status-contest tests. The castle-flag stunt is externally restrained, not independent self-regulation.
- **Causal/model disposition:** STRENGTHEN the direct follower/status challenge mechanism, preserving HIGH confidence and uncertainty about severity. Competence can coexist with failure to protect the assigned goal.

## MG03-A03 — Recognition attached to real service can sustain it

- **V10 outcome:** NOT_TESTED for repeated continuation.
- **Trigger and evidence:** Aqua volunteers to cook after seeing others admired, supplies quick meals and teaches Iris, then receives specific praise for practical knowledge (C2 P0308–0314, P0321–0359). Beneficiaries and actual useful service are clear.
- **Adverse or untested branches:** recognition mainly follows the meal; repeated subsequent service opportunities under that aligned recognition structure are not narrated. Three dishes in one meal do not establish repeated post-recognition continuation. Promised further instruction is not shown delivery. Later food-duty bargaining also remains prospective (Ep P0007, P0019–0020). Dragon support lacks an observed repeated service/recognition sequence. No missing opportunity is converted to failure.
- **Causal/model disposition:** PRESERVE inherited MODERATE-HIGH confidence; OPEN the prospective sustained-performance test. Record the admired meal as single-task evidence without promoting it to validation of the repeated-work claim or voluntary ownership across time.

## MG03-A04 — Unvalued maintenance with an available maximal shortcut

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** no episode jointly establishes low-valued repetitive maintenance, an attractive available one-step maximal alternative, and the absence of an already salient learned analogue or external constraint.
- **Adverse or untested branches:** quick tuna-mayo preparation is not high-power systems intervention; fugu/antidote planning is not established tedious maintenance. Repeated tea purification to obtain an omen (C4 P0008–0009) is repeated ritual, not a maximal shortcut replacing a maintenance burden. Food-duty bargaining supplies no available high-power alternative.
- **Causal/model disposition:** OPEN; retain MODERATE inherited confidence and unvalidated status. Speed or bad judgment alone does not complete the trigger.

## MG03-M01 — Core-specialty challenge can outweigh ordinary companion cost

- **V10 outcome:** PARTIAL.
- **Trigger and evidence:** after Iris's named dragon-killing technique, Megumin claims Explosion could also have won, objects to the apparent superior/imitative name and demands Iris not use it again (C5 P0147–0157). Specialist identity, competition and denial of equivalence are explicit.
- **Adverse or untested branches:** Kazuma had already ordered reserve Explosion to preserve the valuable corpse (C5 P0102), and Megumin later invokes that preservation as her reason for yielding credit (P0150). The explicit identity challenge follows the victory. There is no subsequent concrete choice isolating the rival technique's known necessary companion utility against her objection. Cost-aware non-casting before the identity cue is not falsification; later verbal rivalry does not fully confirm cost priority. The farm has property cost without an explicit identity challenge (C3 P0312–0321); pedagogical frustration is not automatically Explosion identity (C5 P0052–0082).
- **Causal/model disposition:** STRENGTHEN identity activation, preserving HIGH confidence in that branch; OPEN ordinary companion-utility priority at MODERATE confidence. Retain RC-V09-01 and the earlier local cost-inhibition failure without retroactive rescue.

## MG03-M02 — Internally accepted contribution guilt can reopen the build

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** no direct Megumin conclusion identifies her exclusive build as a substantial cause of inability to contribute to valued companions.
- **Adverse or untested branches:** fear of the dragon (C5 P0103–0106), frustrated instruction and loss of finishing credit do not establish build-attributed contribution guilt. She continues claiming her spell could have solved the dragon (P0150–0157). Cooking competence is a separate useful role, not an observed costly role change caused by accepted build burden.
- **Causal/model disposition:** OPEN; preserve MODERATE-HIGH inherited confidence and the still-unvalidated changed-role extension. No absence-based failure or analogy-based confirmation.

## MG03-M03 — Safe separated targets expose reliable artillery

- **V10 outcome:** NOT_TESTED under the complete deployment trigger.
- **Trigger and evidence:** the farm report establishes a dense high-XP target group destroyed by Explosion (C3 P0312–0313); depleted Megumin is afterward carried by Darkness (P0294–0295). A later paid remnant hunt is reported (C4 P0155). These support technical capacity.
- **Adverse or untested branches:** neither report establishes the pre-cast safe separation, resource and exit/carry plan. An afterward carry is not evidence of a prior arrangement. The guide's shock and property compensation demand remain real collateral (C3 P0312, P0321); neither proves blast-zone bodily injury nor licenses assumed safe geometry. The nocturnal diversion has a plan but incomplete geometry/exit evidence and ends in arrest (C4 P0318–0337). Dragon reserve artillery is assigned but not fired (C5 P0102–0126, P0147–0157).
- **Causal/model disposition:** PRESERVE HIGH inherited tactical-efficacy confidence; OPEN clean prospective safe-deployment replication. Separate capacity, harmful target choice and complete trigger coverage.

## MG03-M04 — A valued target creates a separate firing constraint

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** no task requires decisive harm to someone independently established as personally valued by Megumin through a significant relationship.
- **Adverse or untested branches:** farm creatures are called cute by the guide, not established as cherished by Megumin (C3 P0312). The dragon is an impersonal opponent. Rivalry with Iris is not a task requiring decisive harm to her. Both pre-action relational friction and post-action emotional cost remain untested.
- **Causal/model disposition:** OPEN; retain MODERATE confidence. No cross-person replication is inferred from the absence of a new valued-target conflict.

## MG03-M05 — Explicit serious companion harm remains a guarded prediction

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** no scene clearly establishes before Megumin's choice that the best tactical Explosion use knowingly exposes a current valued companion to grave bodily harm, with risk magnitude and alternatives specified.
- **Adverse or untested branches:** dragon reserve fire is conditional and unused. Farm destruction, the nighttime diversion and castle threats have collateral or goal-risk implications, but the frozen explicit grave direct companion-harm conjunction is not supplied (C3 P0312–0321; C4 P0318–0337, P0593–0600). These events are not declared harmless after the fact.
- **Causal/model disposition:** OPEN; preserve guarded MODERATE confidence in the narrowed Gen03 hypothesis. Do not back-project its extra conditions onto the broader Gen02 prediction.

## MG03-M06 — Repeated rewarding fire can become its own objective

- **V10 outcome:** NOT_TESTED; reward-extension analogue retained.
- **Trigger and evidence:** high experience motivates the first farm destruction (C3 P0312), and the next day Megumin pays with Darkness's allowance to hunt remaining creatures (C4 P0155). Additional specialty-reward seeking is directly supported.
- **Adverse or untested branches:** the first encounter is a recreational visit followed by opportunistic blasting; the second is paid hunting. No sustained operation with repeated safe deployment and a weakening original instrumental objective is independently established. Calling the outing a declining military mission would rewrite the trigger after observing the response.
- **Causal/model disposition:** OPEN the exact prediction; retain MODERATE confidence. Preserve the adjacent-domain reward mechanism as a candidate without converting it into formal replication.

## MG03-D01 — Protector contribution survives fear and finite endurance

- **V10 outcome:** CONFIRMED.
- **Trigger and evidence:** Darkness independently interposes, activates Decoy and directs Iris toward safe attack when the dragon threatens the group (C5 P0097–0100); she stands firm after support (P0105–0119). Under hostage pressure she requests Kazuma's safety, then actively struggles when Iris is threatened, initiates gag removal and accepts fire on her bonds so her strength can free them (C5 P0567–0574, P0612–0662).
- **Adverse or untested branches:** enjoyment accompanies restraint, but does not replace needed defense once she has a feasible response. Earlier restraint/drugging of Kazuma is flawed protective procedure, not ethically validated by its aim (C1 P0055–0073; C2 P0046–0050; C3 P0444–0465). Iris ultimately defeats the assassin independently; Darkness's commitment is not identical to sole causal responsibility for survival.
- **Causal/model disposition:** STRENGTHEN costly defensive contribution, HIGH confidence. Preserve capacity limits, mixed reward and procedural error as separate mechanisms.

## MG03-D02 — Agency, audience and belonging determine aversion

- **V10 outcome:** PARTIAL, with adverse agency-component evidence.
- **Trigger and evidence:** a private restraint/care situation acquires an explicitly feared witness and rumor risk (C1 P0135–0147), followed by public denials (P0205–0214). A private drugging/seduction attempt acquires Megumin's witnessing accusation (C3 P0425–0454). Protest and concealment track independently visible audience changes.
- **Adverse or untested branches:** in the later encounter Darkness sought a private visit to thank Kazuma (C5 P0665–0669), identifies an impersonator and encounters real hostage coercion (P0552–0574), yet welcomes restraint and requests humiliation in Kazuma's voice. Reduced control alone does not reliably produce aversion; do not exclude the case because she enjoys it. Discovering that real Kazuma witnessed the performance produces explicit shame (P0576–0581), supporting the audience branch within the same sequence. Durable belonging insecurity is untested.
- **Causal/model disposition:** PRESERVE/STRENGTHEN audience/meaning sensitivity; keep reduced-control generalization OPEN and revision-bearing. Do not let audience confirmation erase contrary agency evidence or assert that pain alone works as coercion. The repeated matched-case threshold for whole-row falsification is not met. Frozen component confidences remain unchanged.

## MG03-D03 — Incompatible obligations recruit costly preservation attempts

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** royal orders and Kazuma's conduct conflict, generating coercive prevention, negotiation and eventual backing (C1 P0055–0073; C2 P0046–0050; C3 P0444–0479). Continued party membership is not itself placed in concrete conflict.
- **Adverse or untested branches:** exclusion from future audiences leads to temporary information gathering while Kazuma escorts Iris (C3 P0698; C4 P0012–0020), not loss of membership or an incompatible family/party commitment. These analogues cannot supply the frozen durability requirement.
- **Causal/model disposition:** OPEN; retain MODERATE-HIGH confidence inherited chiefly from V07. No early acceptance/rejection of the full duty–membership mechanism.

## MG03-E01 — Explicit task organization improves deployment but is not sufficient

- **V10 outcome:** PARTIAL.
- **Trigger and evidence:** in captivity unstructured struggle fails, then Darkness initiates gag release and Kazuma supplies a sequenced ignition/strength handoff that frees them (C5 P0622–0662). At the dragon, roles and targets are specified before execution: Darkness decoys, Aqua buffs, Iris attacks and Megumin remains reserve (C5 P0097–0126). These support visible capability-aligned deployment.
- **Adverse or untested branches:** fugu care lacks timely availability (C1 P0222–0279); the organized false flag is unprepared for the encountered undead and ends in arrest (C4 P0318–0337); a capture plan is defeated by Kazuma's excessive intimidation (C5 P0347–0372). Removing casino interference may improve discipline, but changing wagers and luck confound a controlled comparison (C5 P0324–0342). Darkness and Iris originate important useful actions, yet a fully comparable substitute provider organizing several specialists independently of Kazuma is not demonstrated. The church rescue lacks narrated operational detail, and Iris's solo assassin defeat is not a multi-specialist handoff test.
- **Causal/model disposition:** PRESERVE/STRENGTHEN bounded deployment repair; OPEN alternative-provider adequacy and comparative Kazuma dependence. Keep HIGH confidence in the scoped mechanism without claiming necessity, sufficiency, equal contribution or sole leadership.

## MG03-E02 — Durable efficient separation incurs attachment costs

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** Kazuma explicitly seeks one day away from the others, expects reunion and returns (C3 P0081–0170). Work allocations also preserve membership.
- **Adverse or untested branches:** jealousy, surprise and manipulation during the day split are real but lack meaningful permanence. Iris's career-gambler suggestion does not establish a feasible efficient reorganization credibly removing a core relationship; Kazuma immediately identifies absent protection and targeting risk (C5 P0311–0318).
- **Causal/model disposition:** OPEN; preserve HIGH inherited attachment confidence without counting temporary separation as another durable test.

## MG03-J01 — Register tracks an independently established active role

- **V10 outcome:** PARTIAL, scored by the fixed mappings.
- **Trigger and evidence:** independent actions/stakes supply the role before language scoring. Megumin's direct jealous appeal replaces baited banter (C1 P0174–0196); explicit rivalry with Iris recruits Explosion self-defense (C5 P0147–0157). Aqua's cooking instruction supplies limited service-authority evidence (C2 P0321–0359), while the direct follower insult recruits apology demands (C3 P0564–0570). Darkness's physical interposition precedes protector/noble assertions (C5 P0097–0110); public witness/accusation contexts recruit direct denial (C1 P0139–0151, P0205–0214; C3 P0425–0454). Iris's displayed defeat precedes Kazuma's ordinary reassurance and offer (C5 P0216–0239).
- **Adverse or untested branches:** the finalized fixed register preserves J01-V10-07 (Darkness's dignity-threat response is adverse/mixed), J01-V10-09 (Kazuma restrains violence but resumes a coercive apology), J01-V10-12 (no demonstrated increase from already institutional speech), and J01-V10-05 (battle service is performed, but comparable practical directives are insufficient). J01-V10-11 adds no independent positive continuation trial. Darkness's belonging-insecurity/acceptance-request mapping remains untested. Aqua's meal-service window is short and retains status play. The apparent vulnerable Megumin scene at C5 P0500–0534 is impersonation and cannot validate her voice. The role must not be inferred only from the form being scored; care behavior is not a substitute for a missing language outcome.
- **Causal/model disposition:** PRESERVE/STRENGTHEN supported mappings, OPEN untested mappings, retain HIGH general role-conditioning confidence. See `../02 Sequential Readings/KONOSUBA_V10_DEEP_READING.md` §8.4 and Appendix A for the finalized voice/humor coding details; this row does not invent census counts or audio evidence.

## MG03-J02 — Comic episodes are predominantly portable or pragmatic

- **V10 outcome:** PARTIAL; formal V10–V12 pooled result OPEN.
- **Trigger and evidence:** the frozen universe is a complete census across all three authorized tranche volumes. V10 alone supplies only the first contribution. The V10 episode registry and language-sensitive cases are documented in `../02 Sequential Readings/KONOSUBA_V10_DEEP_READING.md` §8.4 and Appendix A, with the original boundary-before-classification snapshot preserved, an independently audited coverage supplement fixed before its classification, and clear L0–L2, clear L3, mixed and uncertain cases kept separate. The coverage correction and original versus final denominators are explicit; no existing episode class is changed.
- **Adverse or untested branches:** no V11/V12 narrative is read, so neither a favorable V10 pattern nor an independently completed V10 census closes the pooled prediction. Brief verbal/written-form jokes must remain eligible. Form-sensitive candidates include the misunderstood game/divine titles (C2 P0477–0492), Explode/Explosion rivalry (C5 P0147–0157), and genre shorthand puncturing the hero pose (C5 P0238–0239). The coin-location loophole (C4 P0263–0269) requires exact semantic preservation but is not automatically Japanese-specific. Cultural dependence is a separate flag.
- **Causal/model disposition:** OPEN at MODERATE confidence; preserve the frozen majority, ambiguity, tie and empty-set rules. No counts are supplied here independently of the actual registry, and no Gen02 qualitative judgment is retroactively quantified.

## MG03-Y01 — Inclusion and a useful role recruit Yunyun's competent participation

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** Yunyun carries depleted Megumin home and has been accompanying her walks (C1 P0171–0173), showing useful ongoing participation.
- **Adverse or untested branches:** the text does not display an explicit invitation/accepted offer plus role-access decision, preparation or response. No indifferent refusal or technical failure occurs either.
- **Causal/model disposition:** OPEN; preserve MODERATE-HIGH inherited confidence and limited candidate status. A brief participation report does not establish the complete affiliation-mediated mechanism.

## MG03-CE01 — Conscientious service can exceed Chris/Eris's preferred burden

- **V10 outcome:** NOT_TESTED.
- **Trigger and evidence:** the Eris church provides off-page aid after fugu poisoning (C1 P0279), but Chris/Eris personally handling cumulative requests beyond an explicitly preferred burden is not observed.
- **Adverse or untested branches:** Kazuma's memory of the lucky friend and hope for help at the casino (C5 P0269–0277) are not direct evidence of divine intervention, service burden or inability to refuse. No known self-set boundary can be scored either way.
- **Causal/model disposition:** OPEN; retain MODERATE confidence. Do not attribute the wins to Eris as an established cause.

## MG03-I01 — Safe nondeferential interaction expands Iris's agency

- **V10 outcome:** CONFIRMED.
- **Trigger and evidence:** Iris expressly contrasts repeated denied cooking requests at the castle with the present opportunity; Kazuma treats her as a learner and lets her participate (C2 P0270–0306). Aqua/Megumin then teach ordinary food preparation, and Iris eagerly catches ingredients and learns (P0321–0347, P0369–0415). Informal competition with Megumin (P0135–0148), a direct night-escort request and refusal of co-sleeping (P0459–0476) further establish ordinary agency. Formal introduction/negotiation supplies observed public-role comparison (C3 P0520–0533, P0606–0617).
- **Adverse or untested branches:** reduced royal correction does not mean no witnesses. Public duty itself becomes increasingly assertive; the model must not reduce Iris to permanent public passivity. The final ordinary sibling address (Ep P0053–0060) supports intimacy but is not the sole proof of agency.
- **Causal/model disposition:** STRENGTHEN the inherited nondeferential-access mechanism at MODERATE-HIGH confidence. Keep social freedom, combat capability and competent public duty distinct; no adult or future romantic commitment is inferred.

## MG03-I02 — An expressed wish may be narrowed by understood royal duty

- **V10 outcome:** NOT_TESTED under the strict original-wish/duty conjunction.
- **Trigger and evidence:** Iris stays behind to prepare/rest for the meeting (C3 P0025–0035), while Darkness says she had looked forward to coming; the epilogue notes work prevented touring (Ep P0034). This is clear duty-linked self-restriction, but her original personal wish specifically to sightsee is not directly voiced or equivalently specified. Looking forward to coming can concern the mission or travel together.
- **Adverse or untested branches:** cooking desire and royal prohibition are explicit (C2 P0274), but the observed choice expands participation after context relaxes, rather than making a smaller request under active conflicting duty. Her wish that Kazuma stay and promise to serve the country are aligned, not clearly conflicting (C2 P0501). The adventure wish is realized by the mission (C5 P0046–0047). Engagement, relief at dissolution, and the final friendship refusal do not authorize inventing a prior unwanted duty or hidden romantic wish (C3 P0677–0678; C5 P0754–0758).
- **Causal/model disposition:** OPEN; preserve MODERATE-HIGH inherited confidence without new full validation. Retain observed self-restraint as a bounded analogue, not a failure and not a completed trigger.

## Causal and inheritance controls after V10

Levi's support reversal occurs **before** Ragcraft is exposed. The neutrality arrangement is disclosed and Iris reassures the prince at C5 P0418–0453; he proposes the final fair wager and commitment at P0454–0464; continued defense plus offensive support are already agreed at P0475–0477. Ragcraft's identity is revealed later that night at P0585, with public acknowledgment the next morning at P0711–0734. The exposure strengthens gratitude and the alliance, but cannot be backdated as the cause of the initial aid decision. Casino pressure, Iris's prowess and her compassionate response are separate contributing evidence, not a single demonstrated sufficient cause.

The dragon outcome retains its actual allocation: Darkness initiates decoy, Aqua supplies buffs, Iris delivers the terminal attack, Kazuma assigns some phases, and Megumin remains unused reserve. Their necessity is not separately quantified. In captivity Darkness supplies the first gag-release idea, Kazuma adapts ignition to her strength, and Iris independently defeats the attacker as Kazuma and Darkness try to open her door, before they can intervene. The source gives no exact off-page proposition from Ragcraft to Iris, so none is invented.

**Continuation:** all Gen03 frozen bytes and blank scoring fields remain preserved; this append is the V10 local record. V11 is next, **UNOPENED and awaiting new authorization**. The V10–V12 tranche remains OPEN, no `KONOSUBA_V10-V12_CHECKPOINT.md` is claimed complete, and no Gen04 model or V13–V15 prediction freeze is created. After an authorized continuation, retain the same 25 predictions and append later evidence with all adverse/untested branches visible.


# V11 Local Prospective Validation — Frozen Model Generation 0.3

## Source and prospective boundary

Complete ordered Japanese V11 main narrative only: Pr/C1/C2/C3/C4/F/Ep = `item/xhtml/p-002.xhtml`–`p-008.xhtml`, all-body paragraph enumeration including blanks/images; 2,865 paragraphs, 108,101 base characters. Source EPUB SHA-256 `ffee8a32ec536bbacf7f72c3482a11230dc177c33740296c55238eeb62eeab46`. No afterword, ebook bonus, later/side narrative, illustration or audio is evidence. V01–V10 is inherited accepted state. Gen03 model/predictions and all original outcomes remain unchanged; these are additive V11 observations, not Gen04 or tranche closure. RC-V09-01 and RC-V10-01 remain controlling. Detailed locators, qualifications and all 25 outcomes are in the [V11 deep reading](../02%20Sequential%20Readings/KONOSUBA_V11_DEEP_READING.md).

## 14. V11-local disposition of all 25 unchanged Gen03 predictions

These labels apply to **V11 only**. The source boundary remains V11; V10's accepted labels are preserved, and V12 is unread. A missing conjunct is not a successful prediction or a failure. One adverse matched outcome is retained even if another context is favorable. Branches are not silently changed to protect the frozen model.

| Frozen ID | V11 local outcome | Trigger, evidence and limit |
|---|---|---|
| MG03-K01 | **CONFIRMED, bounded branches** | Under direct-power/resource disadvantage Kazuma uses weak-tool combinations, revises after blocked/different routes and delegates fitted phases. C2 P0209–0238/P0242–0295; F P0223–0266/P0267–0330. The tail-deflected arrow at F P0231, Megumin's explicit power-limit explanation at P0233 and Kazuma's eye-blinding/time-buying revision at P0239–0242 isolate the revision branch; the new female manticore and changing support later produce further revised delay/target choices. Forest interrogation also changes method when ambiguous speech defeats naïve detector reliance. C4 P0257–0336/P0411–0413. Universal victory/readiness is not predicted: castle bargaining ultimately fails. |
| MG03-K02 | **CONFIRMED** | Aqua's explicit urgent appeal identifies Darkness's imminent abduction, and Kazuma has a feasible bow intervention. He acts, coordinates the finishing opportunity and prevents the loss rather than preserving comfort. F P0308–0330. Voluntary help with Megumin's public image is additional care evidence, but is not falsely called her concrete request. |
| MG03-K03 | **CONFIRMED, with contextual limits** | Court success/status licenses expanded indulgence and intrusive audience-seeking (C1 P0090–0214); the Princess contest supplies a more immediate payback escalation after humiliation (C4 P0489–0500). Iris's affection is a separate powerful motive in the permanent stay, not automatically status intoxication. The forest's original assignment was investigation; retaliation contributes to the enlarged personal contest. |
| MG03-K04 | **FALSIFIED locally** | He precommits to Aqua crying/apologizing (C2 P0404), sees actual tears (P0431, P0443–0444), approaches and taunts her with his callback question (P0445–0446), then relents (P0450). The valued-companion cue and safe pause are present. Legitimate ownership recovery is a rival motive but does not exclude simultaneous selected teasing/humiliation reward. The interrogative is not a needs-check. Eventual mercy cannot retroactively count as immediate interruption. The category breadth of “teasing” should remain discussable, without adding a new intimacy-only restriction after this result. |
| MG03-A01 | **CONFIRMED** | Engaged known-domain healing works, including the shown memory restoration; binding counter is effective. Prior defensive magic is reported, and Kazuma tentatively attributes the minor collision damage to it. C2 P0394–0396, P0495–0520; F P0254. Flight cancellation works while its momentum consequence is poorly anticipated (F P0243–0254). No general claim about all crafts/memory disorders follows. |
| MG03-A02 | **CONFIRMED** | A defined release task receives a divine/faction challenge; Aqua escalates, then punches Lucy precisely because peaceful departure would allow a status defeat. C3 P0522–0579. The interruption loosens the original release purpose even though Lucy ultimately departs. |
| MG03-A03 | **NOT_TESTED** | Lucy, healing and the child's care give individual useful actions; no independently displayed repeated opportunities for an identified mastered service with recognition specifically attached establish the complete sustained-service trigger. Tea is deliberate play, not a service whose required output remains aligned. C2 P0455–0534; C3 P0226–0241/P0545–0579. |
| MG03-A04 | **NOT_TESTED** | No shown conjunction of low-valued repetitive maintenance and an available attractive maximal shortcut without a learned/external constraint. Tea is intentionally valued play; defensive boarding is not such a maintenance choice. C2 P0225–0264/P0455–0493. |
| MG03-M01 | **PARTIAL** | Exclusion as an Explosion-only guerrilla participant and the sister's appraisal recruit specialist/competence defense and later grand assertion. C3 P0149–0156; F P0097–0144. A known ordinary companion cost does not independently isolate the full priority comparison, and the sister's broad “not impressive” is not an explicit rival spell. Retain those trigger limits. |
| MG03-M02 | **NOT_TESTED** | She accepts that protecting her boast should not embarrass Kazuma or make others lie, but does not conclude that her exclusive build itself substantially prevents contribution. C3 P0283–0295/P0354–0369. This strong social-face compromise is a different mechanism. |
| MG03-M03 | **NOT_TESTED for the full conjunction** | Final terminal fire demonstrably works on a clustered target, but Darkness is just freed/falling and no complete advance exit/carry plan is stated. F P0285–0330. Later carrying does not prove planning; the local efficacy is retained without silently weakening the safe-geometry/logistics trigger. |
| MG03-M04 | **NOT_TESTED** | No established valued teacher/rescuer/companion is assigned as her target. Lucy receives help, not a task for Megumin to decisively harm someone she already values. The pre-action and aftermath branches stay open. |
| MG03-M05 | **NOT_TESTED, proximity uncertainty retained** | Darkness is near the eventual blast shortly before casting, but the source does not establish Megumin's prior knowledge that the best Explosion option would gravely injure her, with magnitude and alternatives explicit. F P0308–0330. No direct friendly-fire injury is independently attributed; do not invent safety or harm from the final wounded return. |
| MG03-M06 | **NOT_TESTED** | Daily ritual and an eagerly sought final cast do not supply a sustained operation of repeatedly safe/rewarding fire with a weakening original objective. F P0097–0144/P0285–0330. One final shot cannot test a repeated-use stopping rule. |
| MG03-D01 | **CONFIRMED** | A giant threat to companions recruits her frontline action; she remains active when carried away and adds the blow that helps release her. F P0203–0218/P0308–0325. Recognition appetite and enjoyment coexist with contribution, and finite control/damage remain. |
| MG03-D02 | **NOT_TESTED for the complete trigger** | Plant insults produce genuine usefulness/belonging insecurity (C4 P0511–0514; F P0093–0095), but no independently established actual change from equal membership or clearly bounded sought scenario acquiring the stipulated altered agency/audience is cleanly shown. Police/maid parody supplies dignity evidence without automatically supplying that complete conjunction. This does not erase prior V10 contrary control evidence. |
| MG03-D03 | **NOT_TESTED** | No genuinely incompatible family/noble/civic demand against continued party membership occurs. Return logistics, deceptive letters and court concern do not themselves make both commitments impossible. |
| MG03-E01 | **PARTIAL** | The original split formation and separate interventions fail in identifiable ways; repaired allocation/pressure/eye-shot/retained spell yields completed actions and a final target cluster. F P0203–0330. Other contributors are indispensable to the observed sequence, but a matched independent alternative organizer and persistent-Kazuma-dependence comparison remain thin. Goal completion, risk, injury and ethics stay separate. |
| MG03-E02 | **NOT_TESTED for the full conjunction; strong adjacent evidence** | The explicit lasting castle choice/permission concerning assets credibly threatens the core household; letters, covert assistance and Megumin's request preserve contact. C1 P0393–0407; C2 P0143–0160/P0336–0368. The required feasible reorganization promising practical efficiency is not fully established: C1 P0569 promises useful castle defense, not an explicit efficiency advantage of core-party separation. Kazuma's actual retirement is contrary to a universal individual resistance claim; his return is coerced. Neither adjacent attachment support nor the frozen one-or-more wording repairs the missing defining condition. |
| MG03-J01 | **PARTIAL** | The [V11 deep reading, §8](../02%20Sequential%20Readings/KONOSUBA_V11_DEEP_READING.md) fixed mapping/window record preserves supported, mixed, adverse and insufficient comparisons. No outcome-driven role reassignment; no single supported mapping confirms the compound. |
| MG03-J02 | **PARTIAL / TRANCHE_OPEN** | The [V11 deep reading, Appendix A](../02%20Sequential%20Readings/KONOSUBA_V11_DEEP_READING.md) contains the complete local census, source-first reconciliation and classes. Formal prediction requires complete pooled V10–V12 narratives; V12 is unread. A local strict majority, if present, is only a pooled contribution. |
| MG03-Y01 | **NOT_TESTED** | Yunyun is sought by others and later appears in a report delivering news; no newly displayed accepted invitation plus feasible fitted participation is shown. C3 P0157–0166; Ep P0023–0027. No inferred war behavior or later side narrative supplies the missing test. |
| MG03-CE01 | **NOT_TESTED** | Chris/Eris has no shown public-request/expressed-burden/available-exit choice. Regina, Lucy, ordinary Eris adherents and Aqua are different subjects. |
| MG03-I01 | **CONFIRMED** | Formal court contrast and trusted interaction show curiosity, ordinary requests, learning, play and direct initiative. C1 P0016–0037, P0080–0140, P0288–0389/P0438–0444. Slang and affectionate address accompany rather than independently establish the behavior. Expanded agency includes appropriate objection to coercion. |
| MG03-I02 | **CONFIRMED** | Her larger wish to travel/live with everyone is explicit; she names royal duty, then requests a smaller immediate period of closeness and links fuller freedom to the Demon King's defeat. C1 P0333–0361. Kazuma's account of what she ought to want is unnecessary: her own words establish both wish and understood conflict. |

The V11-local labels total **8 CONFIRMED, 4 PARTIAL, 12 NOT_TESTED and 1 FALSIFIED**. Counts describe these labels, not an accuracy percentage or a uniform model victory. The confirmed branches, incomplete conjunctions and local falsification all require their stated evidence. Tranche adjudication and Gen04 belong only after V12 and the required review.


## Failure diagnosis, preservation and continuation

K04 is a local matched falsification: actual tears, noticed familiar companion, selected teasing/humiliation reward and an available pause coexist. The mocking entrance question continues the selected pursuit before later help. Ownership recovery is a real co-motive but is not an original trigger exclusion. E02 remains untested because practical-efficiency promise is not independently established; actual durable departure/resistance remains important new evidence. D02 has meaningful insecurity evidence without a clean full conjunction. M03/M05 retain missing planning/geometry/knowledge rather than converting final success into confirmation. A01's spell success and A02's goal failure are different dimensions.

These 25 labels are V11-local only. Preserve all V10 labels, all original Gen03 wording/confidence/disconfirmation and the 25 blank original outcome/adjudication fields. Source reading reaches V11 main Ep P0143; V12 is the next unopened main source for the designated root after this unit's acceptance/persistence. No model generation is frozen here.


# V12 Local Prospective Validation — Frozen Model Generation 0.3

## Source and prospective boundary

Complete ordered Japanese V12 main narrative only: Pr/C1–C5/F/Ep = `text/part0009.html`–`part0016.html`; all-body paragraph enumeration includes blanks/images, ruby uses base text with rt/rp removed and tails retained. **2,841 paragraphs / 2,624 nonempty / 101,448 base characters.** Stored EPUB1,570,295B, SHA-256 `d42bc3dc218d094d93ff029830e66cd4f87d466ec502c5fe63aa42fc59b53a24`, Drive object `1QO85Z8nCYnH_J0H6KcB0UHs8eOS4pikn`. V01–V11 accepted state is inherited at exact tip `45217d5f509ef45f4453bc51753918acad30fb18`; V12 opened only after source audit38963565033, housekeeping38964215208 and final exact-head audit38964267253 succeeded. Afterword `part0017`, electronic bonus **伝説の魔女** `part0020`, other body members, illustrations, later and side narratives are excluded/unread. Gen03 model/predictions and original blank fields remain immutable; V10/V11 outcomes, RC-V09-01 and RC-V10-01 remain unchanged. These are additive V12 observations, **not Gen04 or a formal pooled-tranche adjudication**. See the [V12 deep reading](../02%20Sequential%20Readings/KONOSUBA_V12_DEEP_READING.md) for all17 responsibilities, exact locators, voice windows and census. Limited within-volume boundary-only preview arrived at C3P0410; full main reading still proceeded in source order. No humor classes/aggregates were exchanged before both coding files sealed.

## V12-local disposition of all25 unchanged forecasts

Gen03 model17,746B SHA `dfd92578ddef97eeaf942a6a5d713f37a84678abc9433bce05d36d2ec659d85a`; prediction block45,675B SHA `ebe83ef5dc87fc2e85f8f711e2ba373239d4eea4fd14f466537dbd3625d76150`. All25 original Outcome and25 Adjudication fields remain blank in their frozen blocks. V10 and V11 appended outcomes remain unchanged. The following is **V12 only**, subordinate to exact frozen triggers, not Gen04 or final tranche closure. Missing conjuncts receive no confirmation credit; partial labels identify observed components and do not manufacture a clean matched causal test.

| Frozen ID | V12 local outcome | Trigger, source, counterevidence and claim disposition |
|---|---|---|
| MG03-K01 | **CONFIRMED** | C2P0218–0239,0244–0290,0333–0363; FP0113–0192,0312–0395. Tax escape combines buffs, credible prior information, Steal and departmental jurisdiction. Failure to lift hidden weights causes revision to removing ballast/inducing flight; continued pursuit causes a new arrest-as-shelter route. Infiltration uses sensing/stealth and accepts Darkness strength/local knowledge. During the demon restraint problem he cuts tentacles, rejects making more apertures and tries prepared Aqua water. The clean capability-revision chain is FP0325–0338 new tentacles escaping cuts, followed by FP0358–0364 rejecting more punctures and trying prepared Aqua water. Search and revision strongly supported; delegation supported by actual lift/lead/Bind/amputation assignments. Raw power, first-plan success, safety and ethics are separate. Sexual theft/coercive exposure cause real wrongs. Mithril restraint lacks a release plan; Aqua water does NOT alone free Darkness: Eris supplies eventual rescue. STRENGTHEN bounded indirect search; retain preparation/recovery and moral limits. |
| MG03-K02 | **PARTIAL** | C4P0308–0346; C5P0051–0060,0392–0397; FP0101–0112,0257–0258,0327–0398. Kazuma buys materials, accompanies Darkness to negotiate, offers his own money, supports theft and remains with the burned companion while arranging medicine transport. C5P0060 explicitly reports that the pair came to undertake negotiation; P0396–0397 shows he understood that supporting negotiation was his reason for accompanying. A specific agreed mission/accepted role is supported before the later monetary offer and field work, not merely generic heroism. The initiating trusted-person request/entrustment exchange and its precise timing relative to his earliest voluntary purchasing/help are unshown. Therefore behavior supports the mechanism, but the strict request-causes-effort trigger is not cleanly isolated. No formal please formula is demanded; no request is invented from helpfulness alone. PRESERVE concrete costly help; keep the exact entrustment-causality test only partially covered. V10/V11 positive outcomes unchanged. |
| MG03-K03 | **CONFIRMED** | C4P0031–0039,0267–0284; FP0146–0155; limiting C3P0335–0370. At FP0149 he notices enjoying Darkness calling him senpai; he requests it again and prolongs the reward until Chris redirects him. The response follows explicit personal-recognition feedback and increases pursuit. The public kiss boast is independently precommitted and exploits peers mocking inexperience. The senpai sequence is the clean local feedback→additional pursuit test. Do not infer every danger follows status intoxication. Darkness love is rewarding yet he initially refuses because Megumin is already salient; later directed participation is a separate arousal/excuse mechanism, not automatically another K03 confirmation. STRENGTHEN narrow recognition-pursuit link; preserve relational limits and distinct lust rationalization. |
| MG03-K04 | **AMBIGUOUS** | C2P0006–0012; C3P0151,0166–0192,0243–0312; C5P0280–0314; FP0209–0225,0397–0411; C2P0065; C3P0123–0128; C4P0206; reported C5P0138. The load-bearing adverse candidate is C3P0179: Darkness has visible tears in her eyes, after an exaggerated sexual accusation. Kazuma continues at P0181, checks with disappointment that little happenedP0186 and renews degrading nickname/sexual accusationP0189. The rhetorical wet-neck challenge is not inquiry into her distress. Familiarity, narrator notice and an available pause are supported. Two honest matching limits remain. (1) 涙を浮かべ is actual visible tears in eyes, stronger than merely near-tears, but the exact frozen wording and accepted V10 operational commentary distinguish actually shed tears from tearful eyes; V12 does not explicitly use the unambiguous flowing language seen at C3P0289/FP0408 here. (2) A mixed personal teasing/intimate reward is plausible from P0177/0186/0189 and earlier bedtime teasing, but is less explicit than V11 precommitment; a valid bodily-intrusion objection coexists and is not an automatic exclusion. Under visible-tears eligibility this is adverse continued pursuit; under the prior conservative shed-cue operation the decisive conjunct remains unresolved. Do not exclude embarrassment/masochism, invent a new harmlessness exception or count a rhetorical question as checking. Other branches: Aqua game distress lacks established pre-cue reward; C3 flowing tears follow already serious concern/nonjoking conversation, so care does not validate a tear-triggered stop; C5 toilet urgency lacks pre-cue intimate/teasing pursuit and practical relief precedes resumed teasing; Chris rescue precedes crying and the insensitive gender inference begins afterward; final joyful tears lack a pre-cue reward pursuit. All are retained, not positive cue-stop tests. Additional screening: C2P0065 Megumin ritual tears-in-eyes and C4P0206 grateful adventurers are not excluded because of joy; neither establishes a selected pre-cue intimate/teasing pursuit by Kazuma. C3P0123 half-crying Aqua pleads with Megumin, not an active Kazuma pursuit. Reported tears in Claire/Rain letters C5P0138 are not a directly noticed companion onset in his current interaction. Near-tears at C1P0277/C4P0293/EpP0084 remain distinct. DOWNGRADE transfer confidence further; preserve strong partly matched adverse evidence and every historical outcome. V11 remains a clean local FALSIFIED; V12 ambiguity cannot erase it or rescue the tranche hypothesis. |
| MG03-A01 | **CONFIRMED** | C2P0234–0240; C4P0300–0320; FP0398–0424. Aqua executes the requested strength/speed buffs. Her sustained engaged healing preserves children against disease depletion across the party journey; at return they appear vigorous, and Vanir identifies her service as what kept them alive. Exceptional healing is not a cure of the carrier disease. Internal pathology remains and the antidote is still necessary. The original large-reservoir plan was replaced by a smaller pond when discovered; terrifying heating is not failure of Aqua breathing underwater. Her nightvision finds a key, but that previously demonstrated domain is redeployed rather than newly discovered, and is not added to the explicit domains listed in the frozen A01 trigger. STRENGTHEN bounded support/healing capacity; keep engagement, diagnosis, cure and safety distinct. |
| MG03-A02 | **NOT_TESTED** | C4P0092–0100,0300–0335; C5P0055–0056; FP0428–0431. Aqua moral superiority receives a counterexample; later she attacks Vanir for an ingredient, urges eventual demon killing and adds branded Aqua water to the recipe. No clean conjunction of an already identified instrumental assignment interrupted by a direct divinity/follower/superiority/public-recognition contest is established. The school punch is explicitly ingredient-directed under false body assumptions, not a prestige replacement of the task. Recipe modification claims enhancement without a separately established preceding divine-status challenge. Rival insults alone are not enough; these remain useful adverse goal-discipline/knowledge observations. OPEN exact trigger replication; do not reclassify all hostility as prestige capture. |
| MG03-A03 | **PARTIAL** | C5P0049–0055; FP0412–0422; PrP0013–0015. Owned child-care and prolonged useful performance are directly reported, and offerings/recognition are visible when the travelers return. The onset and sequence of recognition relative to the prolonged work are not observed. Visible rewards at return cannot establish that praise specifically recruited or repeatedly sustained earlier service. Banquet MVP discussion is after work, not a repeated-service continuation test. PARTIAL means only the sustained-owned-service component is observed; recognition-conditioned continuation remains NOT_TESTED and receives no causal confirmation credit. PRESERVE constructive recognition hypothesis; partial state co-occurrence, temporal mechanism still open. |
| MG03-A04 | **NOT_TESTED** | C4P0300–0335; FP0419–0431. She undertakes intense care and makes a high-output additive recipe proposal. The care is expressly valued, not low-valued repetitive maintenance; no attractive available one-step alternative meeting all frozen conditions is established. Fast healing or adding water is not by itself the maximal-shortcut trigger. OPEN unchanged. |
| MG03-M01 | **PARTIAL** | C2P0055–0071; EpP0013–0026. Megumin defends the seriousness of Explosion scoring and responds competitively when Darkness calls the ritual foolish; depletion then makes her threat vulnerable to a skirt-teasing counter. Disparagement of the scoring exchange is not identical to explicit denigration/replacement/imitation of Explosion itself. Independently known ordinary companion cost does not define a clean priority conflict here. Specialist identity activation is supported; the full identity-over-cost prediction is only partly covered. PRESERVE protected specialty identity, keep utility-priority branch open. |
| MG03-M02 | **NOT_TESTED** | C1P0277–0285; C5P0049–0052; FP0424–0432. Megumin self-deprecates as a poor magician beside an impressive romantic rival and later takes a useful pharmacological preparation role. Romantic replacement fear does not establish her own accepted conclusion that the exclusive build materially prevents substantial contribution. New useful work is not itself guilt-driven build reconsideration. OPEN exact self-attributed build-burden inversion. |
| MG03-M03 | **NOT_TESTED** | C2P0050–0064; EpP0003–0018,0028–0036. Leisure lake Explosion is controlled, aesthetically effective and incidentally useful for fish; mana is supplied after casting. No fully established dense/immobilized tactical target plus prior safe-friendly geometry, resource and post-cast exit/carry plan is shown. Successful leisure firing is capacity evidence, not complete prospective artillery validation. PRESERVE demonstrated control; leave full tactical conjunction untested. |
| MG03-M04 | **NOT_TESTED** | C4P0339–0341; EpP0033–0035. Megumin proposes a familiar-sacrifice summoning ritual, stopped by Darkness, and reports changed familiar behavior. No task requires decisive harm to an established personally valued person now acting as opponent/obstacle. A short proposed familiar ritual is not silently promoted to that relational combat trigger; no actual sacrifice is shown. The proposal remains a limit on broad automatic care claims. OPEN cross-person firing constraint; retain adverse adjacent familiar proposal without inventing execution. |
| MG03-M05 | **NOT_TESTED** | EpP0014–0016; C4P0339–0341. Megumin explicitly lowers power for recovering Sylphina and articulates spectator care. This is strong new calibrated-care/control evidence, but not best available tactical Explosion with clearly understood grave direct companion harm and alternatives. The familiar ritual also lacks the Explosion requirement. PRESERVE narrowed grave-harm hypothesis as still untested; do not upgrade from adjacency. |
| MG03-M06 | **NOT_TESTED** | C2P0050–0072; EpP0027–0029. Repeated leisure ritual gains a fishing byproduct, mostly pursued by Aqua, while Megumin dislikes being fixed to one site. No sustained instrumental operation repeatedly rewarding Explosion growth as the mission weakens is shown. Ordinary repeated pleasure is not the full goal-drift trigger. OPEN unchanged. |
| MG03-D01 | **CONFIRMED** | C4P0170–0220; C5P0370–0388; FP0312–0367,0387–0398. Darkness funds/carries civic care, compromises demon-exposure rigidity for children, blocks the costume and explicitly accepts shared binding. She blocks burning apertures and offers to remain while others carry medicine. Actual injury, sweating and later unconsciousness coexist with bodily pleasure. The crisis role is defense-aligned and directly protects companion/medicine transport. Pleasure is not an exclusion and does not erase duty. Her earlier sword-accuracy failure and pleasure spoiling the count bargain limit goal completion; Eris ultimately rescues her. Protective intent does not prove safe planning or universal restraint. STRENGTHEN costly defensive contribution within finite capacity and conflicting rewards. |
| MG03-D02 | **CONFIRMED** | C2P0183–0207,0244–0295; limitsP0315–0329; C3P0064–0095,0257–0277. Darkness deliberately designs bounded public tax capture. Steal removes tights and Kazuma adds unchosen public stripping; she directly protestsP0279, questions seriousnessP0284 and chooses flightP0288 despite explicit duty guiltP0294. This is a source-established changed exposure/control condition, not simply physical intensity. Later she deliberately requests painful dragging and imagines public stripping as attractiveP0320/0328; this limits any claim of persistent or universal aversion. The later threat renews an already known condition rather than cleanly introducing a new audience/control change. Record it as adverse to a broader uniform rule, not delete it. Bath coercion independently shows personal privacy objection. Romantic fear alone does not establish an actual change from equal party membership. STRENGTHEN bounded meaning/agency sensitivity; preserve changed reward appraisals and narrow the reach of any uniformly aversive extrapolation. |
| MG03-D03 | **NOT_TESTED** | C4P0170–0237; C5P0370–0388; FP0019–0033. Family, civic, religious and companion obligations coexist and she accepts costs or pragmatic compromise. Continued party membership and family/noble duty do not make genuinely incompatible concrete demands here: a coordinated temporary journey and ongoing home care support both. Do not convert every obligation conflict into the full family-versus-membership test. OPEN exact incompatibility replication; preserve useful adjacent values evidence. |
| MG03-E01 | **PARTIAL** | C5P0049–0060; FP0113–0192,0277–0372,0419–0438. Misaligned professional rank initially blocks fit use of Darkness strength/knowledge; accepted specific physical/local roles improve access. Medicine work has named collection, care, preparation and negotiation roles. Demon restraint enables nail acquisition but lacks a release resource and is disrupted by Chris target hostility. Deployment-improvement branch has direct bounded support. Alternative-provider branch is partial: Darkness supplies successful access/local phases and Vanir diagnosis, but no complete non-Kazuma arrangement for the whole multistage problem is independently shown adequate. Kazuma comparative repair is supported locally, while Darkness and the unplanned Eris rescue defeat unique-leadership claims. Safe completion, final objective, ethical evaluation and incentive alignment remain separate. Whole compound is not fully confirmed from one positive branch. PRESERVE bounded organization model; refine independent contribution and recovery-resource limits without changing frozen text. |
| MG03-E02 | **NOT_TESTED** | C3P0257–0311,0338–0347; C5P0006–0060; EpP0063–0090. Household continuity, romantic insecurity, temporary division and the final wish are explicit. No feasible practical-efficiency-promising reorganization credibly removes an established core home relationship for a sustained period. Romantic awkwardness and temporary mission absence are explicitly insufficient. Affection is new evidence, not a retroactive matched test; V11 E02 remains NOT_TESTED. PRESERVE strong attachment evidence separately; full trigger remains open. |
| MG03-J01 | **PARTIAL** | voice_windows_fixed.json; C1/C2/C3/C4/C5/F/Ep fixed14comparisons. All14 mapping/window assignments were frozen before language outcomes. Personal appeals and public duties provide useful contrasts; ritual disparagement, already-active duty/care, sparse replies and immediate tactical directives limit other comparisons. Keep the exact fixed windows, all adverse/unchanged/sparse cases and semantic-role/form separation. No clean Aqua divine-prestige role change was fixed. Vulnerability alone cannot prove Kazuma adopted care, and serious care already preceded the flowing-tear episode. Detailed per-window coding is documented in the V12 reading §8 and voice append; no new favorable baseline will replace weak windows. PRESERVE role conditioning as partial/mixed local test, not a universal seriousness direction. |
| MG03-J02 | **PARTIAL / TRANCHE_OPEN** | humor_boundaries_initial_unclassified.json; humor_boundaries_reconciled_preclass.json; humor_classification_primary_SEALED.json. Complete main reading precedes initial119 source-first entries. Ten splits,three merges,four additions yield root-accepted130 final unclassified episodes; five context extensions change no count. All22 operations (10+3+4+5) and119 lineages are preserved before coding. Both independent files sealed before release; canonical conservative review has127clearL0–L2,0clearL3,3mixed unresolved(H004/H047/H072), bounds127/130–130/130. V12-only lower bound97.69% exceeds half even assigning all unresolved toL3. This is descriptive local support, not formal pooled V10–V12 closure. Four pre-coding soft-salience episodes remain admitted; culture and nested-form flags remain separate.86exact fine agreements/44fine differences,41within portable family,3scoring-group differences and2clear-portable-status differences; no forced fine histogram/reliability claim. Both snapshots and full difference records are preserved in humor_classification_reconciled_review.json SHA00ed4164e5f52d30a0af0c9f5c2f3c03c47c3727e72c2eb58834f05d6b4e91e8. Boundary discovery had documented limited within-volume preview, without Lclass/aggregate exposure; no boundary changed for fit. TRANCHE_OPEN until complete independently checked pool; preserve all frozen wording and V10/V11 local dispositions. |
| MG03-Y01 | **NOT_TESTED** | C4P0042–0045. Aqua reports Megumin going to declare romantic victory to Yunyun. No directly shown invitation, accepted shared undertaking, suitable role or Yunyun participation. A report that she was visited supplies none of these conjuncts. OPEN unchanged. |
| MG03-CE01 | **NOT_TESTED** | FP0006–0044,0275–0307,0377–0395. Chris helps a friend, donates money, gossips and later acts as Eris against the demon. No public-divine/service accumulation of sincere requests exceeding her own expressed preferred burden with an available refusal is established. Casual friendship and volunteered help do not prove over-compliance. OPEN exact burden mechanism; retain new companion and target-hostility evidence separately. |
| MG03-I01 | **NOT_TESTED** | C1P0238–0254; C5P0138–0142. Iris occurs in Kazuma retrospective account and recalled letter duty. No new direct constrained/public versus safe nondeferential interaction. Flattering, explicitly possibly edited recollection cannot become primary evidence of her actual behavior or reopen V11. OPEN local test; preserve V11 confirmation unchanged. |
| MG03-I02 | **NOT_TESTED** | C1P0241–0243,0248; C5P0138. The account recalls attachment and a letter promise. No newly directly established Iris wish plus understood conflicting royal duty and narrowed request. The embellished remain-or-die story is not an authenticated prior statement. OPEN local test; V11 direct wish/duty evidence remains historically confirmed. |

## Prospective preservation and review route

The six K04 core branches plus additional tear/near-tear/report screening are retained in V12 deep reading §14. The adverse C3P0179 case is not removed because embarrassment or masochistic pleasure coexists; V11's clean FALSIFIED remains. A03 PARTIAL gives no causal recognition-conditioned continuation confirmation. K02 preserves an accepted mission and costly behavior while keeping initiating entrustment/request timing unshown. E01's deployment, alternative-provider and comparative-Kazuma branches remain separately scored rather than upgrading one favorable segment into the whole compound.

The14 fixed language comparisons are in V12 deep reading §8; the full130-episode list, both original fine codes, conservative unresolved groups and operation provenance are in V12 deep reading Appendix A. These are explicit destinations within the linked reading, not sections of this cumulative ledger. J02 remains **PARTIAL / TRANCHE_OPEN** in this local append: root/checkpoint owns the complete V10–V12 pool and any next-generation freeze. No later main narrative or side finding was used to adjust Gen03 or earlier prospective states.


# V10–V12 Formal Tranche Adjudication — Model Generation0.3

The complete formal judgments below are accepted after V12’s exact publication close and the independent354-unit pool. They supplement all preserved local histories and original fields. Read the [V10–V12 checkpoint](../04%20Checkpoints%20and%20Model%20Validation/KONOSUBA_V10-V12_CHECKPOINT.md) and [receiving review](../09%20Audits%20and%20Manifests/KONOSUBA_V10-V12_CHECKPOINT_RECEIVING_REVIEW.md) for the full model, failure diagnostics, provenance limits and exact freeze.

### 2.3 Complete formal Gen03 adjudications

These are new tranche judgments against the unchanged Gen03 text. All local histories and original scoring fields remain preserved. V12’s required publication close and the independent complete pooled census are satisfied. Exact original forecasts remain in the earlier checkpoint and cumulative ledger, without retrospective rewording.

### MG03-K01 — Indirect construction of a solution, with explicit resource limits

**Tranche disposition:** CONFIRMED.

**Local history:** V10 PARTIAL; V11 CONFIRMED, bounded branches; V12 CONFIRMED.

**Branches:** indirect search/combination or negotiation; revision when a newly learned capability invalidates the first plan; delegation to fitted specialists.

Indirect search, exact capability-based revision and fitted delegation all exercised, with different local coverage. V10 search/delegation is partial, not retroactively completed. V11 failed arrow reveals the target power limit and elicits blinding/time-buying; V12 cuts reveal new tentacle exits and elicit rejection of further punctures plus prepared Aqua water.

**Contrary, absent and scope limits:** Retain failed raids/capture, coercive tactics, missing cuff/Bind release plans, independently useful actors and eventual Eris rescue. Neither victory nor morality is entailed.

**Claim transition:** STRENGTHEN bounded constructive process; add explicit capture-versus-release and goal/harm distinctions in successor.

**New V12 evidence route:** C2P0218–0239,0244–0290,0333–0363; FP0113–0192,0312–0395.

### MG03-K02 — Concrete entrusted need recruits effort before certainty

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED; V12 PARTIAL.

**Branches:** concrete trusted-person request; feasible contribution before complete certainty; costly substantive help versus comfort-based abandonment.

V10 and V11 provide concrete trusted requests and substantial effort before complete certainty; V12 adds accepted negotiation mission and costly help, without isolating its initiating request. Positive matched earlier volumes suffice for bounded replication. V12 PARTIAL remains partial, because purchased/helpful behavior cannot invent an earlier entrustment exchange.

**Contrary, absent and scope limits:** Comfort, attraction, reputation and complaint can coexist with help. Feasible contribution and actual request must precede the scored choice; help alone is not a complete request-conditioned test.

**Claim transition:** PRESERVE concrete-entrustment mechanism at bounded confidence; distinguish decision to help from adequacy/success of method.

**New V12 evidence route:** C4P0308–0346; C5P0051–0060,0392–0397; FP0101–0112,0257–0258,0327–0398.

### MG03-K03 — Success-linked personal reward can expand pursuit

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED, with contextual limits; V12 CONFIRMED.

**Branches:** active success/recognition/payback before next choice; scope/pursuit/exposure change relative to prior plan; pre-existing severe-danger/known-target modifiers.

Success/recognition/payback salience precedes increased pursuit in independently located decisions. V10 bounded feedback-related scope changes and V11 recognition pursuit are joined by V12 Darkness addressing Kazuma as senpai at FP0149, followed by Kazuma requesting repetition until Chris interrupts.

**Contrary, absent and scope limits:** A preplanned fallback is not newly invented escalation. Severe known danger, existing targets and relational commitment can limit pursuit. V12 refusal of Darkness is not explained away as universal reward capture.

**Claim transition:** STRENGTHEN conditional reward-driven expansion; distinguish arousal/excuse mechanism from success feedback.

**New V12 evidence route:** C4P0031–0039,0267–0284; FP0146–0155; limiting C3P0335–0370.

### MG03-K04 — Noticed actual tears can interrupt intimate or teasing pursuit

**Tranche disposition:** FALSIFIED.

**Local history:** V10 NOT_TESTED; V11 FALSIFIED locally; V12 AMBIGUOUS.

**Branches:** self-rewarding intimate or teasing pursuit; actual tears noticed in a valued companion; available pause without separate immediate danger; immediate interruption/check/help versus continued same pursuit.

V11 is a complete matched failure of the narrowed noticed-tears stopping rule. V12 adds a strong adverse but honestly partly matched case, not a rescue. V11 C2P0404 precommits to making Aqua cry/apologize, P0431/0443–0444 notices actual tears, P0445–0446 approaches/taunts before P0450 relenting. Safe pause and valued companion are present. V10 remains NT; V12 remains AMBIGUOUS under disclosed cue/motive readings.

**Contrary, absent and scope limits:** Ownership recovery does not exclude simultaneous teasing reward; a rhetorical callback is not a needs-check; eventual mercy is not immediate interruption. V12 C3P0179 actual visible tears and P0181/0189 continued accusation remain adverse even if flowing onset/pre-cue reward matching is unresolved. No embarrassment/masochism or intimacy-only exclusion.

**Claim transition:** RETIRE actual tears as a sufficient inhibition gate. Preserve sincere care and temporary restraint as context-dependent capacities; propose a separately motivated commitment/arousal competition test, never a retroactive reinterpretation.

**New V12 evidence route:** C2P0006–0012; C3P0151,0166–0192,0243–0312; C5P0280–0314; FP0209–0225,0397–0411; C2P0065; C3P0123–0128; C4P0206; reported C5P0138.

### MG03-A01 — Established specialist ability appears under a well-defined task

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED; V12 CONFIRMED.

**Branches:** already demonstrated domain; bounded task with access/resources; engagement versus readiness; execution quality versus collateral/system prediction.

Engaged execution of established abilities repeatedly succeeds under bounded access/resources, distinct from readiness and system effects. V10 domain tasks, V11 cancellation/healing/support and V12 actual buffs plus prolonged child-preserving healing exercise the listed-domain mechanism.

**Contrary, absent and scope limits:** Asleep/unavailable care is a readiness failure; canceled spell momentum is a system consequence; tentative buff attribution stays tentative. Carrier preservation is not cure. Nightvision was already demonstrated earlier and is not inserted into original listed domains.

**Claim transition:** STRENGTHEN capacity/engagement distinction; successor may explicitly list known nightvision with honest prior-witness provenance limits.

**New V12 evidence route:** C2P0234–0240; C4P0300–0320; FP0398–0424.

### MG03-A02 — A direct prestige contest can displace an assigned purpose

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED; V12 NOT_TESTED.

**Branches:** identifiable assignment before prestige challenge; distinct prestige response; escalation and loosened original constraint; independently acknowledged imminent-harm competition.

V10/V11 matched direct prestige contests can displace an identifiable assigned purpose. Earlier matched original-task→prestige-challenge→distinct-response sequences supply positive evidence. V12 ingredient punch and branded recipe water are NT for this full trigger, not inferred prestige displacement.

**Contrary, absent and scope limits:** Hostile species presence alone is insufficient; task-directed wrong body/rank knowledge is a different error. Eventual success and externally stopped escalation do not erase prior goal replacement.

**Claim transition:** PRESERVE conditional prestige capture, with original assignment/constraint and independently salient harm recorded before response.

**New V12 evidence route:** C4P0092–0100,0300–0335; C5P0055–0056; FP0428–0431.

### MG03-A03 — Recognition attached to real service can sustain it

**Tranche disposition:** PARTIAL.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 PARTIAL.

**Branches:** mastered task; recognition specifically aligned with real service; identified beneficiary/responsibility; continued service across repeated opportunities; owned versus externally imposed assignment.

Known service, beneficiaries, ownership and recognition are observed; V12 adds sustained actual work. Recognition-conditioned continuation itself remains NOT_TESTED across the tranche. V10 meal/praise lacks repeated post-recognition opportunities; V11 useful individual actions lack full repeated sequence. V12 prolonged care is real, but offerings visible at return do not establish prior recognition onset or causality.

**Contrary, absent and scope limits:** No causal confirmation credit. Neither three dishes, a promise of instruction, retrospective duration nor return-time rewards supply recognition-before-next-service. Absence of a full test is not refusal or falsification.

**Claim transition:** PRESERVE service capacity/persistence evidence; keep recognition mechanism OPEN and give successor an explicit prospective temporal design.

**New V12 evidence route:** C5P0049–0055; FP0412–0422; PrP0013–0015.

### MG03-A04 — Unvalued maintenance with an available maximal shortcut

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** expressly low-valued repetitive maintenance; concretely available attractive one-step high-power alternative; no already salient learned analogue or strong external constraint; shortcut choice and neglected secondary system.

No complete low-valued repetitive maintenance plus available attractive one-step maximal alternative and absence of salient learned constraint is supplied. Across V10–V12 the adjacent work, fast tasks, valued repair or care do not complete all original conjuncts.

**Contrary, absent and scope limits:** Do not infer unobserved shortcut availability, low valuation or absence of learned constraints from a comic result. Effective high output alone is not this forecast.

**Claim transition:** OPEN, unvalidated in this tranche; retain the hypothesis without borrowed confirmation from A01/A02.

**New V12 evidence route:** C4P0300–0335; FP0419–0431.

### MG03-M01 — Core-specialty challenge can outweigh ordinary companion cost

**Tranche disposition:** PARTIAL.

**Local history:** V10 PARTIAL; V11 PARTIAL; V12 PARTIAL.

**Branches:** explicit Explosion identity challenge treated as such; known ordinary companion cost; pre-response burden/grave-harm cue eligibility; defense/competition/redirection versus easy cost-only compromise.

Specialist identity defense is supported, but priority over independently known ordinary companion cost is not cleanly isolated. V10 rival named technique triggers comparison/prohibition after the kill, while reserve restraint predates the challenge. V11 competence/specialty exclusion and V12 ritual disparagement add bounded defense, not the full cost-choice comparison.

**Contrary, absent and scope limits:** Keep RC-V09-01 and earlier cost-inhibition failure. Ritual mockery is not automatically explicit spell replacement; pre-cue cost restraint cannot become a post-cue choice test. Higher build-burden/grave-harm eligibility is classified before response.

**Claim transition:** STRENGTHEN identity activation; leave utility-priority branch MODERATE and unvalidated rather than claiming the compound confirmed.

**New V12 evidence route:** C2P0055–0071; EpP0013–0026.

### MG03-M02 — Internally accepted contribution guilt can reopen the build

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** self-attributed substantial contribution failure caused by exclusive build; established valued companions; meaningful compromise/role/build consideration with loss; changed-role extension separated from inherited abandonment branch.

No newly accepted conclusion that the exclusive build materially prevents substantial contribution establishes the guilt/reconsideration trigger. V12 poor-magician self-deprecation concerns romantic comparison; useful medicine research is not independently guilt-caused build revision. V10/V11 likewise lack the complete state.

**Contrary, absent and scope limits:** Do not equate criticism, failure, romance insecurity or a new useful task with her own accepted build-burden conclusion.

**Claim transition:** OPEN exact inversion mechanism; ordinary specialty defense and contribution guilt remain distinct potential modes.

**New V12 evidence route:** C1P0277–0285; C5P0049–0052; FP0424–0432.

### MG03-M03 — Safe separated targets expose reliable artillery

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED for the full conjunction; V12 NOT_TESTED.

**Branches:** technically suitable dense/immobilized target; friendlies safely separated in advance; resource and post-cast exit/carry planning; no valued-target relationship; terminal execution efficacy.

Full prepared tactical artillery conjunction remains unexercised in the tranche. V11 final target cluster is not evidence of prior safe geometry/resource/carry plan; V12 controlled lake casts and post-cast mana support are leisure capacity evidence. V10 has no full matched test.

**Contrary, absent and scope limits:** Do not infer safety from success or harm from absent safety description. Prior dense/immobilized target, friendly geometry, resources and exit/carry conditions all remain necessary.

**Claim transition:** PRESERVE demonstrated power/control; no new full tactical validation.

**New V12 evidence route:** C2P0050–0064; EpP0003–0018,0028–0036.

### MG03-M04 — A valued target creates a separate firing constraint

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** personally valued target independently established; pre-/during-action relational friction; post-action emotional cost separately.

No complete required decisive harm to an established personally valued person acting as opponent/obstacle is supplied. V12 proposed familiar sacrifice, stopped by Darkness, is important adverse adjacency but not an executed valued-person combat decision; V10/V11 full trigger absent.

**Contrary, absent and scope limits:** Do not erase familiar attachment, invent execution or silently broaden person/opponent eligibility merely to obtain a test.

**Claim transition:** OPEN specific cross-person firing constraint; downgrade any broader automatic-care inference from adjacent proposal.

**New V12 evidence route:** C4P0339–0341; EpP0033–0035.

### MG03-M05 — Explicit serious companion harm remains a guarded prediction

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED, proximity uncertainty retained; V12 NOT_TESTED.

**Branches:** known grave direct companion risk; Megumin’s pre-action knowledge; clear alternatives and tactical requirement; friction/objection/consent/redirection versus enthusiastic casting.

Best-available tactical Explosion with clearly understood grave direct companion harm and available alternatives is not established. V11 proximity remains uncertain; V12 explicitly reduced power for recovering Sylphina is strong calibrated spectator-care evidence without that grave tactical conjunction.

**Contrary, absent and scope limits:** No friendly-fire confirmation from generic proximity, leisure restraint or familiar ritual. Keep the source-known harm appraisal before decision and the tactical alternatives separate.

**Claim transition:** OPEN unvalidated grave-harm branch; strengthen only demonstrated output calibration/care capacity.

**New V12 evidence route:** EpP0014–0016; C4P0339–0341.

### MG03-M06 — Repeated rewarding fire can become its own objective

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** sustained repeated safe/effective firing; visible specialist reward/growth; weakening/completed original objective; seeking continuation versus stopping without external limit.

No sustained instrumental operation repeatedly rewarding Explosion growth while mission purpose weakens is shown. V12 repeated lake ritual and fishing byproduct are leisure; Aqua mainly pursues fish and Megumin dislikes site fixation. Earlier local rows also NT.

**Contrary, absent and scope limits:** Repeated pleasure alone is not instrumental goal drift; do not manufacture a weakening mission from an unchanged routine.

**Claim transition:** OPEN goal-drift mechanism, without presenting lack of trigger as reliable discipline.

**New V12 evidence route:** C2P0050–0072; EpP0027–0029.

### MG03-D01 — Protector contribution survives fear and finite endurance

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED; V12 CONFIRMED.

**Branches:** serious threat/injustice to protected other; recognized responsibility and feasible defensive/institutional contribution; accepted bodily/reputational/institutional cost; effective defensive role versus preserving helplessness.

Defense-aligned serious tasks repeatedly recruit costly bodily contribution; pleasure does not remove the contribution. V10 defensive action, V11 protection and V12 shared binding/aperture blocking/offer to stay protect companions and medicine transport. Real burning, sweat and unconsciousness establish finite capacity.

**Contrary, absent and scope limits:** Sword accuracy and the count bargain fail; recovery plans are poor; Eris eventually rescues her. Neither duty nor masochistic reward proves safe, strategically sufficient or universally self-sacrificing conduct.

**Claim transition:** STRENGTHEN costly defense within actual capacities and competing rewards; retain injury/recovery limits.

**New V12 evidence route:** C4P0170–0220; C5P0370–0388; FP0312–0367,0387–0398.

### MG03-D02 — Agency, audience and belonging determine aversion

**Tranche disposition:** PARTIAL.

**Local history:** V10 PARTIAL; V11 NOT_TESTED for the complete trigger; V12 CONFIRMED.

**Branches:** previously sought bounded scenario; independently established unchosen public exposure, reduced control, or explicit threatened change from equal party membership, including reclassification; previous preferences distinct from current reaction; genuine objection/anxiety/recovery versus uniform welcome.

Audience/meaning sensitivity is supported; reduced control is genuinely mixed; equal-membership threat branch remains untested. V10 unexpected witnesses elicit shame/protest, but real hostage coercion is enjoyed in a familiar-voice fantasy. V12 selected tax capture becomes unexpected public stripping threat and produces protest/flight; later dragging/public-strip fantasy is welcomed. V11 insecurity alone lacks full sought-scenario/change conjunction.

**Contrary, absent and scope limits:** Preserve the actual V10 agency contrary case and later V12 pleasure. Do not exclude enjoyment to save agency aversion, or infer an actual membership change from romance fear. Original repeated uniform-welcome threshold for whole-row falsification is not established.

**Claim transition:** REVISE away from generalized control-loss aversion; model privacy/audience/standing and selected fantasy meaning separately. No automatic compound CONFIRMED from V12 local positive branch.

**New V12 evidence route:** C2P0183–0207,0244–0295; limitsP0315–0329; C3P0064–0095,0257–0277.

### MG03-D03 — Incompatible obligations recruit costly preservation attempts

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** genuinely incompatible concrete family/noble/civic versus party demands; identifiable people on both sides; negotiation/workaround/cost absorption before easy abandonment; intent versus secrecy/shared-decision procedure.

No full genuinely incompatible family/noble-duty versus continued-party-membership demand is established. V12 accepts real civic, family and religious costs, but coordinated journey/home care supports both obligations; V10/V11 likewise no complete incompatibility.

**Contrary, absent and scope limits:** Temporary role division, coexistence of duties and hard choices do not themselves establish the stipulated mutually incompatible demands.

**Claim transition:** OPEN membership-versus-duty priority; retain evidence of pragmatic compromise without pretending it validates the trigger.

**New V12 evidence route:** C4P0170–0237; C5P0370–0388; FP0019–0033.

### MG03-E01 — Explicit task organization improves deployment but is not sufficient

**Tranche disposition:** PARTIAL.

**Local history:** V10 PARTIAL; V11 PARTIAL; V12 PARTIAL.

**Branches:** independently classified misaligned versus explicit aligned arrangements; deployment reliability comparison; alternative provider adequacy; Kazuma’s initiating/repair versus continuing-direction dependence; completion/harm/goal/ethics separate.

Aligned roles improve local deployment; adequate substitute-provider and comparative continuing-Kazuma-dependence branches remain incomplete. V10 captivity/dragon roles, V11 repaired formation and V12 accepted Darkness strength/local knowledge and explicit acquisition roles support deployment improvement. Darkness/Vanir provide important parts, but no fully comparable whole-problem independent substitute arrangement is established.

**Contrary, absent and scope limits:** Retain organized failures, unavailable resources, target-hostility, missing releases, injuries and Eris intervention. Successful components do not establish safe completion, unique leadership, equal indispensability or whole replacement sufficiency.

**Claim transition:** STRENGTHEN component organization; leave provider/comparative branches OPEN and make resource, handoff, recovery and incentive checks explicit.

**New V12 evidence route:** C5P0049–0060; FP0113–0192,0277–0372,0419–0438.

### MG03-E02 — Durable efficient separation incurs attachment costs

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED for the full conjunction; strong adjacent evidence; V12 NOT_TESTED.

**Branches:** feasible practical-efficiency improvement; credible sustained core relationship/home removal; one-or-more member attachment/restoration response; ordinary tactical separation excluded.

No feasible practical-efficiency-promising reorganization credibly removing established core home relationship for a sustained period completes the conjunction. V11 actual Kazuma castle retirement and others resistance are strong adjacent attachment evidence but no stated practical-efficiency advantage to reorganization. V12 romance/household fear and mission absence do not add it.

**Contrary, absent and scope limits:** Kazuma really wanted retirement; do not force a universal individual return preference or turn permission about home/assets into efficiency evidence. Temporary absence is not durable removal.

**Claim transition:** PRESERVE strong particular attachment; OPEN exact efficiency-versus-home test and individual variation.

**New V12 evidence route:** C3P0257–0311,0338–0347; C5P0006–0060; EpP0063–0090.

### MG03-J01 — Register tracks an independently established active role

**Tranche disposition:** PARTIAL.

**Local history:** V10 PARTIAL; V11 PARTIAL; V12 PARTIAL.

**Branches:** role/semantic commitment independently established; mapping and local window fixed before surface outcome; each named speaker-role mapping separately; adverse/unchanged/opposite/insufficient speech retained.

Several independently fixed role mappings gain support; sparse, already-active, role-limited and opposite directions prevent whole compound confirmation. V10 twelve, V11 eleven and V12 fourteen fixed comparisons retain original windows and limitations. V12 personal/public-duty contrasts coexist with ritual ambiguity, sparse question/acceptance, already practical care and emergency directives.

**Contrary, absent and scope limits:** Semantic role/form circularity, unequal windows, audience/domain changes and missing Aqua prestige comparison remain explicit. Correct JV12-09 own-shirt fact outside unchanged fixed registry; do not replace a weak baseline. One mapping cannot conceal another adverse one.

**Claim transition:** REVISE the Kazuma care mapping by independently established quiet relational versus urgent tactical contexts; preserve separate mapping outcomes and no global polite/soft register rule.

**New V12 evidence route:** voice_windows_fixed.json; C1/C2/C3/C4/C5/F/Ep fixed14comparisons.

### MG03-J02 — Comic episodes are predominantly portable or pragmatic

**Tranche disposition:** CONFIRMED.

**Local history:** V10 PARTIAL; V11 PARTIAL / TRANCHE_OPEN; V12 PARTIAL / TRANCHE_OPEN.

**Branches:** complete V10/V11/V12 eligible-episode census before frequency; source-first episode eligibility/segmentation independent of L-class; clear L0–L2/L3/mixed/uncertain categories; strict-majority lower/upper-bound rule; per-volume versus pooled claim.

Formal pooled result after root verification of the complete authorized registers and V12 publication close. 112+112+130=354 episodes. Clear portable106+108+127=341; clearL3=3; mixed=6; uncertain=4. Conservative bounds341/354–351/354 (96.33–99.15%) retain all unresolved in denominator; lower bound exceeds half.

**Contrary, absent and scope limits:** Do not pool forced fine-code consensus, remove short/form-sensitive/soft entries, resegment after coding or erase V10 supplements/V11 preview/V12 boundary-preview provenance. This is descriptive census inference, not a formal reliability or universal-translatability claim. All local PARTIAL/TRANCHE_OPEN labels remain historical.

**Claim transition:** CONFIRM the exact strict-majority forecast after the complete census/close gates; retain unresolved items and generate a fresh future-tranche census prospectively.

**New V12 evidence route:** humor_boundaries_initial_unclassified.json; humor_boundaries_reconciled_preclass.json; humor_classification_primary_SEALED.json.

### MG03-Y01 — Inclusion and a useful role recruit Yunyun's competent participation

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** real trusted invitation/accepted offer; feasible fitted magic/practical role; preparation and participation; moral conflict versus technical ability/resource/coercion.

No complete valued invitation/shared undertaking with suitable role and actual Yunyun participation is established. V12 report of Megumin visiting/boasting supplies no invitation, task role or response. V10/V11 local rows also NT.

**Contrary, absent and scope limits:** A source report is not categorically ineligible; this report lacks the actual conjuncts. Neither absence nor desire for contact validates behavior.

**Claim transition:** OPEN social inclusion mechanism and avoid a full secondary model from reported mentions.

**New V12 evidence route:** C4P0042–0045.

### MG03-CE01 — Conscientious service can exceed Chris/Eris's preferred burden

**Tranche disposition:** NOT_TESTED.

**Local history:** V10 NOT_TESTED; V11 NOT_TESTED; V12 NOT_TESTED.

**Branches:** public divine/service role; sincere cumulative requests beyond her own expressed preference; possible refusal/exit; continued overburden versus successful self-set boundary.

No public-divine/service accumulation of sincere requests beyond her own expressed preferred burden with feasible refusal establishes the trigger. V12 shows Chris actually arriving and helping a friend, alongside charity/lodging reports and Eris rescue. Kazuma connects the arrival with prior prayer as a causal inference, rather than Chris confessing a divine motive. These do not supply cumulative over-compliance. V10/V11 full trigger absent.

**Contrary, absent and scope limits:** Do not treat every help act as inability to refuse, infer hidden divine motive as fact, or erase specialized anti-demon zeal and ordinary leisure.

**Claim transition:** OPEN bounded burden mechanism; preserve Chris/Eris role distinctions, participant knowledge and source-limited secondary profile.

**New V12 evidence route:** FP0006–0044,0275–0307,0377–0395.

### MG03-I01 — Safe nondeferential interaction expands Iris's agency

**Tranche disposition:** CONFIRMED.

**Local history:** V10 CONFIRMED; V11 CONFIRMED; V12 NOT_TESTED.

**Branches:** trusted ordinary-peer interaction with less surveillance; observed constrained public comparison; behavioral agency change beyond honorifics.

V10/V11 directly shown constrained/public versus safer nondeferential interaction supports role-conditioned Iris behavior. Earlier matched contrasts supply evidence. V12 flattering retrospective stay-or-die account is explicitly possibly edited and not a new direct interaction.

**Contrary, absent and scope limits:** No retrospective invention of earlier speech/tears, global public obedience or universal private impulsivity. Power, status and attachment remain separate dimensions.

**Claim transition:** PRESERVE bounded role-sensitive Iris model; V12 local NT stays NT.

**New V12 evidence route:** C1P0238–0254; C5P0138–0142.

### MG03-I02 — An expressed wish may be narrowed by understood royal duty

**Tranche disposition:** CONFIRMED.

**Local history:** V10 NOT_TESTED; V11 CONFIRMED; V12 NOT_TESTED.

**Branches:** directly evidenced personal wish; understood conflicting royal obligation; reduced request/self-limitation while original wish persists.

V11 directly establishes personal wish, understood royal duty and narrowing of the request. V10 was NT; V11 C1P0333–0361 supplies the explicit wish/duty decision. V12 recalled letter obligation supplies no fresh matched decision.

**Contrary, absent and scope limits:** Retold attachment cannot replace directly established conflicting duty; emotional wish does not entail unbounded override or no residual desire.

**Claim transition:** STRENGTHEN wish–duty negotiation with narrow evidence; preserve V10/V12 absent full tests and actual status constraints.

**New V12 evidence route:** C1P0241–0243,0248; C5P0138.

### Pooled humor arithmetic and limitations

| Volume | Total | Clear portable | Clear L3 | Mixed | Uncertain | Bound |
|---|---:|---:|---:|---:|---:|---|
| V10 |112|106|1|1|4|106/112–111/112|
| V11 |112|108|2|2|0|108/112–110/112|
| V12 |130|127|0|3|0|127/130–130/130|
| **Pool** |**354**|**341**|**3**|**6**|**4**|**341/354–351/354**|

9CONFIRMED /5PARTIAL /10NOT_TESTED /1FALSIFIED; descriptive disposition counts, not predictive accuracy. A03 mechanismNT within componentPARTIAL, D02 compoundPARTIAL, E01 compoundPARTIAL. J02 is formally CONFIRMED after root verified the actual complete-census and V12-publication gates.

Counts cannot establish independent trials, calibration, real-world translation quality or universal portability. V10 original105+7addition provenance, V11 incomplete blind aggregate boundary and V12 limited boundary-preview/no-code-sharing provenance survive. Each generation is derived only at its source boundary; no side/bonus/reference material enters.


The following identical Gen04 block was accepted by root at2026-10-16T22:12:40.615896+00:00, after V12 and before V13 exposure. Model SHA256 `5ff6cb60408fff2bfc9bab814f311d65128ed4df0703f8ab607c16b963515173`; forecast SHA256 `e553d7cfc5be3fd290ad0471d482ca6fe2c0ffd5db3689600bbf156de71def5c`. Source-branch publication/readback and full exact-head CI remain separate recorded obligations.

# Model Generation 0.4 — Frozen Predictions for V13–V15

These25 accepted prospective commitments are frozen after V12 and before V13 narrative exposure. All25 Outcome and25 Adjudication fields are blank. Original Gen03 model, forecasts, blank fields and local outcomes remain unchanged. Carrying an unvalidated hypothesis does not upgrade its evidence. Each branch receives separate source/missing/adverse evidence and failure diagnosis. A single fully matched contrary case remains local adverse evidence even where a broader repeated-pattern threshold is specified; favorable cases cannot delete it. The exact freeze receipt identifies this block and its identical prediction-ledger copy.

## MG04-K01 — Indirect construction and capability-based revision, with component and recovery limits

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a serious novel or under-structured problem disadvantages Kazuma in direct power, and he can identify at least one usable rule, tool, environmental feature or incentive.
- **Relationship/stakes:** combat or institutional stakes; distinguish strangers from valued people whose safety constrains available tactics.
- **Predicted appraisal:** the apparent power contest can be changed by altering state, sequence, information or other actors' incentives.
- **Predicted dominant motive:** obtain a workable outcome at lower personal exposure while retaining agency over the method.
- **Predicted behavior/effect:** He will search rules/tools/environment/incentives, combine or negotiate when direct power is inadequate, and assign fitted specialist actions where usable. If a newly learned capability actually invalidates his first plan, he will revise the method rather than merely repeat it unchanged. Score search, exact capability-based revision and delegation separately. A capture/acquisition plan can still omit safe release or recovery; record that omission independently before outcomes. Success, safety and ethical adequacy are separate.
- **Interaction tendency:** practical instructions and explicit division of responsibility; opportunistic or unflattering framing may coexist with correct mechanics.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K01, CP03-E01; V07/V08 MG02-K01; V09 `0013:P0065–0144`, `0014:P0043–0076`, `P0199–0258`, `P0374–0391`.; CP04 branch score MG03-K01: Indirect search, exact capability-based revision and fitted delegation all exercised, with different local coverage. V12 route: C2P0218–0239,0244–0290,0333–0363; FP0113–0192,0312–0395. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** Repeated matched problems show only ineffective direct-force repetition or resignation despite an independently usable affordance; or newly learned invalidating capability is understood but he knowingly repeats the same failed method without a competing urgent reason. A missing delegation opportunity is NT for that branch. Independent success or harmful tactics do not themselves falsify the predicted search process; a failed component cannot be erased by eventual rescue.
- **Outcome:**
- **Adjudication:**

## MG04-K02 — Concrete entrusted need recruits costly effort before certainty

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a trusted person makes a concrete request whose refusal would leave that person or a valued companion exposed to preventable harm, and Kazuma has some feasible contribution even if no complete solution is known.
- **Relationship/stakes:** established trust, actual cost or danger; generic appeals to heroism, fame or attractiveness alone do not supply this trigger.
- **Predicted appraisal:** this is a particular person's problem that he can help reduce, not simply optional public work.
- **Predicted dominant motive:** preserve the person/relationship while reducing the cost of intervention.
- **Predicted behavior/effect:** he will complain, bargain, investigate, prepare or seek a cheaper route, but make a substantive contribution rather than abandon the responsibility chiefly for comfort. Commitment may precede a fully credible success plan.
- **Interaction tendency:** ordinary or grumbling speech can accompany costly help; a polished heroic declaration is not required.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K03; V07/V08 MG02-K02 and DISC-V07-04; V09 `0011:P0478–0486`, `0013:P0164–0171`, `0014:P0473–0494`.; CP04 branch score MG03-K02: V10 and V11 provide concrete trusted requests and substantial effort before complete certainty; V12 adds accepted negotiation mission and costly help, without isolating its initiating request. V12 route: C4P0308–0346; C5P0051–0060,0392–0397; FP0101–0112,0257–0258,0327–0398. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** a clear, feasible contribution exists, but he knowingly leaves the established person exposed primarily to preserve leisure, with no meaningful help, search or relationship-preserving alternative.
- **Coding and modifiers:** Require a source-established concrete trusted-person request, exposure to preventable harm and feasible contribution before the scored help decision. An accepted mission can support role commitment but cannot establish an unshown initiating request or its timing. Grumbling and mixed motives remain eligible; practical success and ethics receive separate judgments.
- **Outcome:**
- **Adjudication:**

## MG04-K03 — Active recognition or payback reward expands the next pursuit decision

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Kazuma receives concrete success feedback or sees an apparently manageable opportunity for recognition/payback, and that personal reward is visibly active before his next decision about scope, pursuit or exposure, whether or not the plan subsequently changes.
- **Relationship/stakes:** initially tolerable perceived risk; compare the same task before and after feedback. Success without evidence of recognition/payback salience is insufficient.
- **Predicted appraisal:** he can obtain more advantage, status or retaliation than the original task required.
- **Predicted dominant motive:** extend the rewarding success state.
- **Predicted behavior/effect:** he will increase scope, pursuit, taunting or accepted exposure relative to his prior plan. Newly explicit severe danger or harm to a personally known target may instead restore caution; record these pre-existing modifiers before judging the outcome.
- **Interaction tendency:** victory/credit language or grievance display should accompany the expansion more often than purely duty-based explanation.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** CP03-K02; V08 MG02-K03; V09 partial test `0011:P0090–0248`; limiting cases `0013:P0065–0097`, `0014:P0434–0448`.; CP04 branch score MG03-K03: Success/recognition/payback salience precedes increased pursuit in independently located decisions. V12 route: C4P0031–0039,0267–0284; FP0146–0155; limiting C3P0335–0370. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated comparable success-plus-personal-reward states leave pursuit unchanged or make it more conservative despite no new threat/relationship cue. Forgotten equipment alone does not count as confirmation.
- **Coding and modifiers:** Fix the prior scope, actual feedback/reward salience and subsequent decision in that order. Keep already planned fallback, independently known severe danger, prior target commitment and actual relational limits. Arousal with self-excuse is not automatically success-feedback escalation. An unchanged scope under a full original trigger is genuine contrary evidence, not automatic missing salience.
- **Outcome:**
- **Adjudication:**

## MG04-K04 — Relational commitment can inhibit a quiet choice while renewed arousal recruits an excuse

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Two independently classified states, scored separately. A: in a private, nonurgent relational decision, a particular companion offers an attractive alternative that conflicts with a commitment Kazuma has already acknowledged, while immediate sexual arousal is explicitly reduced or absent. B: after a source-established boundary/commitment or refusal, immediate arousal or intimate gratification becomes explicitly salient, he knows a feasible way to stop or retain agency, and an exculpatory role/explanation is independently present before the next continuation decision (for example already expressed in thought/speech, or supplied by a source-established prior role/constraint). Record that frame and known feasible stop before coding pursuit. Do not infer frame availability merely from the excuse later constructed, arousal from continuation, or low arousal from refusal.
- **Relationship/stakes:** Known companions and specific promises or interpersonal boundaries. Preserve initial imposed contact separately from later choices; later participation cannot retroactively consent to it. Existing actual-tears failures and wider harassment remain load-bearing limits.
- **Predicted appraisal:** A: accepting the available substitute would make his expressed particular attachment or promise dishonest. B: desired gratification conflicts with that commitment, while an account of helplessness can reduce felt responsibility.
- **Predicted dominant motive:** A: preserve an honest particular relationship while avoiding an answer he cannot give. B: obtain immediate gratification while protecting a defensible self-image.
- **Predicted behavior/effect:** A: he will state or clarify the particular attachment/limit and refuse treating any attractive substitute as equivalent, even if awkward and disappointed. B: he will weaken the earlier limit through an excuse, coached role or selective account that preserves pursuit despite a known alternative. Score both directions separately; neither is inferred from his later claim about his own resistance.
- **Interaction tendency:** A favors halting self-disclosure and explicit distinction of motives; B favors qualified responsibility, victim-role language or directions that create the inability later claimed. Neither requires polished moral eloquence.
- **Confidence:** MODERATE, new conditional competition/transfer hypothesis: C1 explicitly reduced appetite lacks the attractive alternative, and C3 alternative/refusal lacks equally explicit reduced appetite. The full quiet-A conjunction is not already demonstrated by combining them; missing future state evidence is NT. Gen03-K04 is FALSIFIED and retired as a sufficient tear-cue rule; confidence is not restored under a new label.
- **Evidence basis:** V12 DISC-V12-01 and C1P0335–0376 ordinary companionship under reduced appetite; C3P0335–0384 honest refusal despite reward; C3P0443–0537 initial imposed acts, remembered commitment, known alternatives and later coached helplessness. C3P0470 already expresses the exculpatory frame before recognizing the free handP0473–0474 and coachingP0475, so this chronology does not infer the frame from the later response. Historical limit: V11 C2P0404,0431,0443–0450 clean failed tear cue; V12 C3P0179/0181/0189 remains strong adverse candidate. These do not retrospectively rescore Gen03.; CP04 branch score MG03-K04: V11 is a complete matched failure of the narrowed noticed-tears stopping rule. V12 adds a strong adverse but honestly partly matched case, not a rescue. V12 route: C2P0006–0012; C3P0151,0166–0192,0243–0312; C5P0280–0314; FP0209–0225,0397–0411; C2P0065; C3P0123–0128; C4P0206; reported C5P0138. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** A matched quiet A case knowingly accepts the substitute without clarifying/limiting despite the already salient commitment; or a matched B case autonomously maintains the limit and uses its known feasible stop rather than pursuing or constructing an excuse. Record every noticed-tear continuation as adverse to any broader brake, without adding intimacy-only, harmlessness or non-notice exemptions. Tears alone never supply confirmation of this successor.
- **Outcome:**
- **Adjudication:**

## MG04-A01 — Established specialist capacity is reliable when engaged, with readiness and downstream effects separate

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** A clearly bounded task uses an already demonstrated ability: healing, purification, resurrection, support/sealing, practiced construction/art, relevant water control, or previously demonstrated nightvision. Require sufficient access/resources and record engagement/readiness independently.
- **Relationship/stakes:** institutional or explicitly organized service; sufficient access and resources. Record sleep, distraction and activation separately from the quality of execution.
- **Predicted appraisal:** this is a task within a recognized area of her expertise.
- **Predicted dominant motive:** execute the familiar service and/or display mastery.
- **Predicted behavior/effect:** Capacity branch: once engaged with adequate resources she will execute the established-domain task at a high level. Comparative clarity branch: where source evidence independently supplies sufficiently comparable clear versus misaligned/unclear goals with domain/access/resources recorded, the clear arrangement will produce fewer task errors. Score capacity execution, readiness at the required moment and comparative clarity separately. A bounded successful task without the comparison is NT for comparative clarity, not a causal confirmation of error reduction. No competence in unobserved domains or guaranteed readiness is implied.
- **Interaction tendency:** confident directives, demonstration or professional pride may be accurate rather than empty boasting.
- **Confidence:** HIGH for the established domains.
- **Evidence basis:** CP03-A01; V07/V08 MG02-A01; V09 `0012:P0238–0272`, `0014:P0043–0076`, `P0080–0110`.; CP04 branch score MG03-A01: Engaged execution of established abilities repeatedly succeeds under bounded access/resources, distinct from readiness and system effects. V12 route: C2P0234–0240; C4P0300–0320; FP0398–0424. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** Capacity: repeated engaged adequately resourced established-domain tasks fail chiefly through domain inability/misunderstanding. Comparative clarity: independently matched clear-versus-misaligned arrangements show no predicted improvement or contrary error pattern. A clean single contrary branch remains local adverse evidence. If no sufficient comparison exists, comparative clarity is NT even when capacity succeeds. Readiness is separately observed and cannot be inferred from ability; a new craft is not mastered merely because construction was.
- **Coding and modifiers:** Nightvision is explicitly within this new-generation domain list because it was demonstrated earlier and redeployed in V12; it is not newly discovered and remains outside original Gen03-A01 list. Preserve historical source-witness identity limits. Distinguish asleep/unavailable readiness, spell quality, diagnosis, system consequences, symptomatic support and cure. Record the three capacity/readiness/comparative-clarity dispositions independently, with missing comparison left NT.
- **Outcome:**
- **Adjudication:**

## MG04-A02 — A direct prestige challenge can displace an identifiable assignment

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** an ongoing instrumental assignment is interrupted by a challenge to Aqua's divinity, followers, superiority or public recognition, and the prestige contest offers a response distinct from completing the task.
- **Relationship/stakes:** the challenger need not be a friend; the original assignment and its constraints must be identifiable before the challenge.
- **Predicted appraisal:** letting the status claim stand is immediately intolerable or more salient than the task.
- **Predicted dominant motive:** compel acknowledgment or win the status contest.
- **Predicted behavior/effect:** she will escalate assertion, performance or power use and loosen at least one original task constraint. Competent ability may magnify the collateral cost. Directly acknowledged imminent harm can be a competing cue, but must be observed rather than inferred after the fact.
- **Interaction tendency:** self-naming, divine/faction titles, demands for apology or mirrored disparagement.
- **Confidence:** HIGH for the trigger class; exact severity remains uncertain.
- **Evidence basis:** CP03-A02; V08 MG02-A02; V09 `0013:P0256–0300`, `0014:P0016–0022`.; CP04 branch score MG03-A02: V10/V11 matched direct prestige contests can displace an identifiable assigned purpose. V12 route: C4P0092–0100,0300–0335; C5P0055–0056; FP0428–0431. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated clear prestige challenges leave the separate assigned goal and constraints intact without another actor preventing escalation or independently acknowledged imminent harm already competing with it. Other proposed explanations remain rival accounts or adverse evidence for revision, not automatic exclusions.
- **Coding and modifiers:** Fix original assignment and constraint before direct divinity/follower/superiority/public-recognition challenge. Rival presence, a task-directed ingredient attack or a branded additive is not sufficient. Classify any independently acknowledged imminent harm before response and retain external inhibition versus self-restraint separately.
- **Outcome:**
- **Adjudication:**

## MG04-A03 — Work-specific recognition can sustain repeated owned service — explicit temporal test

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Aqua demonstrably knows the required service, has an identified beneficiary/responsibility, and receives acknowledgment specifically for the actual useful work. After that acknowledgment, at least two separately identifiable further opportunities to perform the same service occur while resources, beneficiary need and recognition alignment remain available. This two-opportunity threshold is a new prospective Gen04 measurement choice, never a retroactive Gen03 rule.
- **Relationship/stakes:** Record externally imposed versus voluntarily owned assignment, any distinct prestige challenge and any newly observed interruption before each opportunity. Return-time offerings after an elided long task do not establish recognition-before-continuation.
- **Predicted appraisal:** Continued useful performance enacts the valued competent role and sustains acknowledgment from a beneficiary/audience tied to the work.
- **Predicted dominant motive:** Enjoy useful mastery, beneficiary care and role-linked recognition together rather than replace service with a separate status contest.
- **Predicted behavior/effect:** Across the two post-recognition opportunities she will continue the required useful output; display or sharing rewards may coexist while the core service is completed. Score output, voluntary ownership and recognition timing separately. Positive temporal recurrence supports this conditional behavioral forecast, not unique recognition causation: ownership, particular-person care, habit and material reward remain rival sustainers unless independent motive/comparison evidence distinguishes them. A single meal with several dishes, a promised lesson or retrospective duration is not sufficient.
- **Interaction tendency:** Confident instruction, uptake of a useful role or beneficiary-oriented action may accompany continuation, without requiring an apology.
- **Confidence:** MODERATE for the recognition-conditioned mechanism, unvalidated in Gen03 V10–V12; HIGH for actual V12 sustained care as a separate observation.
- **Evidence basis:** CP03-A02/03; DISC-V07-02; V09 `0014:P0016–0019`, `P0043–0110`.; CP04 branch score MG03-A03: Known service, beneficiaries, ownership and recognition are observed; V12 adds sustained actual work. Recognition-conditioned continuation itself remains NOT_TESTED across the tranche. V12 route: C5P0049–0055; FP0412–0422; PrP0013–0015. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** Under the complete pre-established temporal structure, post-recognition repeated opportunities produce refusal, abandonment or merely decorative output despite still-available resources/need and no independently observed distinct contest/interruption. If recognition follows the work or later opportunities are unshown, the mechanism is NT, regardless of valuable service. A self-selected decorative diversion is an outcome to score, not an automatically external interruption that removes the case.
- **Outcome:**
- **Adjudication:**

## MG04-A04 — Unvalued maintenance with an available maximal shortcut

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** repetitive maintenance remains low in Aqua's expressed valuation and a concretely available, attractive one-step high-power alternative is established.
- **Relationship/stakes:** no salient learned analogue or strong external constraint already rules out the shortcut; all these conditions must be checked before counting a test.
- **Predicted appraisal:** the rapid high-output method avoids tedious work.
- **Predicted dominant motive:** remove the immediate burden quickly.
- **Predicted behavior/effect:** she will prefer the shortcut while giving insufficient attention to a secondary system it affects.
- **Interaction tendency:** confident simplification or dismissal of labor may accompany the choice; no special phrase is required.
- **Confidence:** MODERATE, inherited; unvalidated in V07–V09 and still unvalidated in V10–V12 for the full low-valued-maintenance/available-maximal-shortcut/no-salient-constraint conjunction.
- **Evidence basis:** CP03-A04; V04–V06 checkpoint §5 and unchanged MG02-A04; V09 `0014:P0054–0110` is a non-test/countercondition, not confirming evidence.; CP04 branch score MG03-A04: No complete low-valued repetitive maintenance plus available attractive one-step maximal alternative and absence of salient learned constraint is supplied. V12 route: C4P0300–0335; FP0419–0431. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** matched cases repeatedly show calibrated routine performance despite the available shortcut, with no learned analogue or external constraint already accounting for it. Mere speed, effective drying or any manual work does not establish the trigger.
- **Outcome:**
- **Adjudication:**

## MG04-M01 — Protected specialty activation and ordinary-cost priority are separately tested

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a rival, including a companion acting as a rival, explicitly denigrates, replaces or imitates Explosion in a way Megumin treats as a challenge to her specialist identity.
- **Relationship/stakes:** ordinary financial, equipment, convenience or status cost to companions is known; neither an independently expressed conclusion that her build seriously burdens them nor an independently recognized imminent grave companion-harm cue is active before her response. Record mixed-trigger episodes separately rather than deriving eligibility from which motive wins.
- **Predicted appraisal:** the challenge attacks a defining value rather than offering a neutral efficiency improvement.
- **Predicted dominant motive:** preserve the legitimacy and distinctiveness of Explosion.
- **Predicted behavior/effect:** she will defend, compete, reject the replacement or retaliate; known ordinary companion cost alone will not reliably secure compromise. Record any attempt at redirection rather than treating all escalation as uncontrolled.
- **Interaction tendency:** specialist naming, theatrical assertion and precise denial of equivalence.
- **Confidence:** HIGH for defensive identity activation; MODERATE for its priority over known companion utility.
- **Evidence basis:** CP03-M01/05; V07 MG02-M01 and partial MG02-M02; V09 `0011:P0559–0617`, `0013:P0082–0104`.; CP04 branch score MG03-M01: Specialist identity defense is supported, but priority over independently known ordinary companion cost is not cleanly isolated. V12 route: C2P0055–0071; EpP0013–0026. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated clean identity challenges lead to easy compromise because of ordinary companion cost alone, without visible identity conflict, retaliation or an independently evidenced higher-order burden/harm appraisal.
- **Coding and modifiers:** Score identity defense separately from the subsequent known ordinary companion-cost choice. A named rival spell or equivalence challenge is not interchangeable with general competence criticism or mockery of a shared ritual. Higher-order build-burden and grave-harm appraisals are established before outcome; retain mixed states. Gen03 identity branch is supported, ordinary-cost-priority branch remains incompletely tested.
- **Outcome:**
- **Adjudication:**

## MG04-M02 — Internally accepted contribution guilt can reopen the build

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Megumin herself concludes that her exclusive specialization materially prevents her from contributing to valued companions, rather than merely hearing an opponent's criticism.
- **Relationship/stakes:** established companions; the perceived burden is substantial and attributed to the build, not inability to attack one particular person.
- **Predicted appraisal:** protecting the specialty may conflict with remaining useful and wanted.
- **Predicted dominant motive:** preserve contribution and belonging, despite genuine love of Explosion.
- **Predicted behavior/effect:** she will seriously consider compromise, a changed role or abandonment of the exclusive build, with visible loss or reluctance. Others' reassurance may alter the decision, but should not erase the initial conflict.
- **Interaction tendency:** quieter, apologetic or explicit cost language is expected when the self-appraisal is expressed; the role is no longer only that of a challenged rival.
- **Confidence:** MODERATE, carried as a guarded unvalidated contribution-guilt inversion. Romance insecurity or a poor-magician label does not complete the trigger.
- **Evidence basis:** CP03-M02; V04–V06 checkpoint §6 and unchanged MG02-M01 Trigger B. A changed-role option is a Gen03 extension, not an already validated outcome; neither it nor the inherited trigger received a matched V07–V09 test. V09 `0014:P0412–0419`, `P0766–0783` are distinct target/guilt cases, not validation of this build-burden trigger.; CP04 branch score MG03-M02: No newly accepted conclusion that the exclusive build materially prevents substantial contribution establishes the guilt/reconsideration trigger. V12 route: C1P0277–0285; C5P0049–0052; FP0424–0432. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated explicit, substantial self-attributed build burdens produce no meaningful conflict or consideration of compromise, even when a feasible alternative is recognized.
- **Outcome:**
- **Adjudication:**

## MG04-M03 — Safe separated targets expose reliable artillery

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a target within Explosion's established capacity/range is dense or immobilized; friendlies are safely separated; resource use and the post-cast exit/carry requirement are planned.
- **Relationship/stakes:** no identified valued person occupies the target role. The conditions must be established before evaluating the result.
- **Predicted appraisal:** the task offers a legitimate, technically suitable use of the chosen specialty.
- **Predicted dominant motive:** perform and demonstrate Explosion effectively.
- **Predicted behavior/effect:** she will execute reliable terminal fire, making the specialization highly useful for that task. This predicts tactical efficacy; it does not predict restraint toward defeated enemies or sound choice of the campaign's larger objective.
- **Interaction tendency:** exuberance and theatrical display may coexist with accurate execution; a full incantation is not required for demonstrated V09-level control.
- **Confidence:** MODERATE for the complete prepared tactical conjunction, unvalidated in V10–V12; demonstrated destructive power and calibrated leisure control are separate stronger claims.
- **Evidence basis:** CP03-M03; V07 MG02-M03; V09 `0014:P0199–0242`, `P0261–0304` are matched deployment evidence; `P0534–0544` supports technical capacity only because its personally valued target does not match this prediction. The incantation is omitted there, while the spell name is voiced.; CP04 branch score MG03-M03: Full prepared tactical artillery conjunction remains unexercised in the tranche. V12 route: C2P0050–0064; EpP0003–0018,0028–0036. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated fully matched target/resource/exit cases fail because of her own ordinary target-selection or execution process, despite no new relational inhibition or external interference.
- **Coding and modifiers:** Fix target geometry, friendly positions, resource and post-cast exit/carry plan before casting. Post-cast assistance does not prove a prior plan; success alone cannot establish missing conditions.
- **Outcome:**
- **Adjudication:**

## MG04-M04 — A valued target creates a separate firing constraint

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a task calls for decisive harm to someone whom the source independently establishes as personally valued by Megumin through rescue, teaching, gratitude or another significant relationship.
- **Relationship/stakes:** that person is now an opponent or obstacle; technical feasibility and urgent reasons to act may both be present.
- **Predicted appraisal:** the target carries a relationship obligation that cannot be reduced to a combat category.
- **Predicted dominant motive:** reconcile protection/duty with attachment or gratitude.
- **Predicted behavior/effect:** she will show meaningful hesitation, a search for acknowledgment/choice, or inability to execute before or during a personally meaningful acknowledgment or choice; acting need not resolve subsequent guilt. If she acts, immediate celebratory ease is less likely than residual emotional cost. Record pre-action relational friction and post-action emotional cost separately. The mechanism does not depend on a target merely looking human.
- **Interaction tendency:** direct relational address or an attempted personal question can interrupt ordinary specialist theater.
- **Confidence:** MODERATE, exact valued-person opponent/obstacle constraint unvalidated in V10–V12.
- **Evidence basis:** CP03-M04; V09 `0014:P0007–0015`, `P0365–0419`, `P0473–0544`, `P0766–0816`.; CP04 branch score MG03-M04: No complete required decisive harm to an established personally valued person acting as opponent/obstacle is supplied. V12 route: C4P0339–0341; EpP0033–0035. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** a comparably established valued-target conflict produces effortless execution without meaningful pre-action relational friction despite the salient bond. This is adverse to the firing-constraint component even if regret follows. Easy celebration without meaningful emotional aftermath is separately adverse to the aftermath component. A target with no such history is not a test.
- **Coding and modifiers:** The V12 proposed familiar sacrifice remains adverse to broad automatic care but was stopped and is not an executed valued-person combat test. Do not alter original person/opponent requirements or invent an act.
- **Outcome:**
- **Adjudication:**

## MG04-M05 — Explicit serious companion harm remains a guarded prediction

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Megumin knows that the best available tactical Explosion use would directly expose a valued companion to grave bodily harm, with the risk and alternatives made clear in the source.
- **Relationship/stakes:** current valued companion; establish anticipated harm magnitude, Megumin's knowledge, alternatives and the tactical requirement independently. Minor displacement without established anticipated grave injury is distinct; uncertain severity remains ambiguous/adverse collateral, not automatically harmless comedy. An enemy's attack is not her own friendly-fire choice.
- **Predicted appraisal:** success would impose a personally unacceptable relational cost unless it is justified or authorized.
- **Predicted dominant motive:** protect the companion while responding to the tactical need.
- **Predicted behavior/effect:** she will hesitate, object, seek consent/authorization, redirect, or otherwise show clear friction relative to ordinary enthusiastic casting.
- **Interaction tendency:** explicit concern or negotiation is evidence; a token catchphrase is not.
- **Confidence:** MODERATE, the exact grave direct companion-harm tactical branch remains unvalidated in V10–V12.
- **Evidence basis:** CP03-M05; V04–V06 checkpoint §6 / unchanged MG02-M04; adverse V09 `0011:P0254–0271`; distinct care evidence `0013:P0206–0208`.; CP04 branch score MG03-M05: Best-available tactical Explosion with clearly understood grave direct companion harm and available alternatives is not established. V12 route: EpP0014–0016; C4P0339–0341. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** a clean matched case produces enthusiastic casting without relational friction despite her explicit understanding of the grave companion risk. Do not reclassify an adverse matched outcome as harmless comedy after observing it.
- **Coding and modifiers:** Explicit power reduction for recovering Sylphina establishes control/care, not this full grave-harm tactical test. Record source-known gravity, available alternatives and best tactical option before response; proximity alone is insufficient.
- **Outcome:**
- **Adjudication:**

## MG04-M06 — Repeated rewarding fire can become its own objective

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a sustained operation repeatedly permits safe, effective Explosion and provides visible skill/experience growth or equivalent specialist reward; the original instrumental objective is approaching completion or has weakened.
- **Relationship/stakes:** impersonal enemy/obstacle targets; no independently active valued-target or grave companion-harm conflict.
- **Predicted appraisal:** another opportunity to fire/grow remains desirable even when marginal mission value falls.
- **Predicted dominant motive:** continue the specialty reward.
- **Predicted behavior/effect:** she will seek additional casts, denser targets or an extended opportunity; a companion may need to restate the original goal. Tactical success can persist while goal discipline declines.
- **Interaction tendency:** language of casting, spectacle or growth will increasingly replace the original mission rationale.
- **Confidence:** MODERATE, carried as an unvalidated sustained instrumental goal-drift hypothesis.
- **Evidence basis:** CP03-M03/05; V09 `0014:P0268–0321`, especially `P0286–0316`.; CP04 branch score MG03-M06: No sustained instrumental operation repeatedly rewarding Explosion growth while mission purpose weakens is shown. V12 route: C2P0050–0072; EpP0027–0029. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated matched reward sequences lead her to stop or narrow use when the instrumental objective is achieved, without an external limit or another already established higher-priority conflict.
- **Coding and modifiers:** Distinguish leisure repetitions and incidental fish utility from an actual instrumental mission losing ground as repeated Explosion rewards grow. A missing weakening-mission condition is NT.
- **Outcome:**
- **Adjudication:**

## MG04-D01 — Costly defense persists with pleasure and finite endurance

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a person Darkness treats as her responsibility faces serious harm or injustice, and she has a feasible defensive or institutional intervention.
- **Relationship/stakes:** a protected person or companion; distinguish chosen fantasy danger from an independently visible threat to someone else.
- **Predicted appraisal:** she has a responsibility to absorb or oppose the threat.
- **Predicted dominant motive:** protect and contribute, even where fear, embarrassment or bodily reward also exists.
- **Predicted behavior/effect:** she will accept bodily, reputational or institutional cost. In a defense-aligned task she will use interposition/endurance rather than deliberately preserve helplessness. Equipment and opponent force may still overwhelm her.
- **Interaction tendency:** protector/noble assertions or blunt action may precede concern for her own comfort.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-D01; V07/V08 MG02-D01/D03; V09 `0011:P0549–0553`, `0012:P0213–0272`, `0013:P0075–0077`, `P0146–0163`.; CP04 branch score MG03-D01: Defense-aligned serious tasks repeatedly recruit costly bodily contribution; pleasure does not remove the contribution. V12 route: C4P0170–0220; C5P0370–0388; FP0312–0367,0387–0398. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** despite recognizing serious unjust harm and a feasible contribution, she preserves rank/self-protection chiefly for convenience, or repeatedly sabotages the needed defensive role merely to remain helpless.
- **Coding and modifiers:** Count actual protective target/resource/handoff and bodily costs independently of whether pleasure is present. Sweat, burns, failed accuracy, collapse and outside rescue remain consequences. Contribution does not prove safe extraction, sufficient strategy or universally prioritized duty.
- **Outcome:**
- **Adjudication:**

## MG04-D02 — Previously established privacy or standing boundaries predict objection; control loss alone does not

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** An otherwise sought bounded event acquires either (A) an independently established unexpected audience/exposure condition that conflicts with a privacy preference expressed before the response, or (B) an explicit threat to previously valued equal companion standing. Establish the changed condition and prior preference independently of her reaction: the objection being scored cannot be the only evidence of the prior boundary. Fix the comparison baseline before outcome and keep partially matched cases when independent preference is missing. A completed membership loss is not required for an explicit matching threat.
- **Relationship/stakes:** Fix controller, witnesses, chosen scenario and standing at risk. Reduced control or intense pain alone does not trigger this new directional forecast; all such cases are still logged as transfer evidence. This narrowing is a new successor to a mixed Gen03 compound, not rescoring its adverse agency case.
- **Predicted appraisal:** A specific unwanted audience/standing change threatens the dignity or belonging she previously valued outside the desired fantasy.
- **Predicted dominant motive:** Recover the identified privacy, dignity or ordinary companion standing, possibly alongside continuing bodily attraction.
- **Predicted behavior/effect:** A: direct objection, concealment, negotiation or flight will increase after the changed boundary. B: anxiety, protest or acceptance-seeking will increase after the explicit threat. Score A and B separately; later adoption/enjoyment of the scenario does not retroactively consent to the initial imposition and is retained as changed reward appraisal.
- **Interaction tendency:** Direct personal perspective under privacy threat; unusually explicit belonging/acceptance requests under standing threat. Public noble formality is not necessary.
- **Confidence:** HIGH for audience/meaning sensitivity in observed cases; MODERATE for new standing transfer. No general loss-of-control-aversion claim.
- **Evidence basis:** CP03-D02 and inherited earlier audience/standing evidence; V10 C1P0135–0147/C3P0425–0454 audience shifts, and C5P0552–0581/P0665–0669 actual control countercase plus witness shame; V12 C2P0273–0295 direct exposure objection/flight and P0315–0329 later chosen pleasure; C3P0067–0095 bodily perspective and P0257–0347 attachment without full membership trigger.; CP04 branch score MG03-D02: Audience/meaning sensitivity is supported; reduced control is genuinely mixed; equal-membership threat branch remains untested. V12 route: C2P0183–0207,0244–0295; limitsP0315–0329; C3P0064–0095,0257–0277. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** Repeated full A/B cases show no objection/anxiety/recovery and uniformly welcome the independently rejected boundary/standing change. Any single matched countercase remains adverse even before repeated-case threshold. Do not remove the V10 real-hostage enjoyment or V12 later public-strip fantasy because it is pleasurable; those constrain the broader model and original Gen03 PARTIAL.
- **Outcome:**
- **Adjudication:**

## MG04-D03 — Incompatible obligations recruit costly preservation attempts

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** family/noble/civic duty and continued party membership make genuinely incompatible concrete demands.
- **Relationship/stakes:** obligations to identifiable people on both sides, rather than an abstract preference for prestige or temporary deployment apart.
- **Predicted appraisal:** simply dropping either responsibility would betray a valued part of her life.
- **Predicted dominant motive:** protect people and preserve both commitments if possible.
- **Predicted behavior/effect:** she will try negotiation, procedural workarounds or personally costly absorption before easy abandonment. Her V07 secrecy/self-erasure remains a possible procedural error; protective intent does not guarantee shared decision-making.
- **Interaction tendency:** duty language may conceal personal need; other members may need to challenge her assumption that she must bear the cost alone.
- **Confidence:** MODERATE, exact genuinely incompatible family-duty/continued-membership conflict remains unvalidated in V10–V12.
- **Evidence basis:** CP03-D03; V07 MG02-D04 / DISC-V07-01; V09 `0013:P0146–0163` is a bounded command-obligation analogue, not a new full family/party test.; CP04 branch score MG03-D03: No full genuinely incompatible family/noble-duty versus continued-party-membership demand is established. V12 route: C4P0170–0237; C5P0370–0388; FP0019–0033. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** she discards either established relationship or recognized duty for convenience or prestige without visible conflict or preservation attempt despite feasible alternatives.
- **Coding and modifiers:** Ordinary coexisting civic/family/party duties, compatible temporary division or costly mission assistance do not establish mutually incompatible demands. Preserve independent evidence of the duties before response.
- **Outcome:**
- **Adjudication:**

## MG04-E01 — Explicit fit improves local deployment, with provider and comparative dependence separately tested

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a serious multi-stage problem requires several established specialist capacities, and source evidence permits comparison between missing/misaligned organization and an arrangement with explicit roles, targets, resources and handoffs. Classify these arrangements and incentive alignment independently of the eventual result.
- **Relationship/stakes:** record practical task completion, friendly harm, goal discipline and moral objections separately. Temporary allocation apart does not mean loss of membership.
- **Predicted appraisal:** participants identify a usable contribution when the arrangement fits their actual abilities and incentives.
- **Predicted dominant motive:** solve the common task while preserving salient individual values.
- **Predicted behavior/effect:** the aligned arrangement will improve reliable deployment relative to the earlier missing/misaligned state: more intended specialist actions completed at assigned targets/times, fewer failed handoffs, or fewer missing required resources. A capable institution/domain expert can supply the arrangement. Where it has not been supplied, Kazuma will more often initiate or repair it; where another actor supplies it, successful deployment need not depend on his continuing direction. Score deployment improvement, alternative-provider adequacy and Kazuma's comparative contribution separately. A concealed target relationship or misaligned reward can still disrupt a technically sound plan.
- **Interaction tendency:** directives, signaling, handoffs and corrections will make the practical arrangement visible; do not infer organization merely from eventual victory.
- **Confidence:** HIGH for the bounded deployment mechanism; no universal necessity or sufficiency theorem is claimed.
- **Evidence basis:** CP03-E01; V07/V08 MG02-E01; V09 contrast `0011:P0120–0271` with `0014:P0054–0110`, `P0199–0258`; relational failure `0014:P0365–0419`.; CP04 branch score MG03-E01: Aligned roles improve local deployment; adequate substitute-provider and comparative continuing-Kazuma-dependence branches remain incomplete. V12 route: C5P0049–0060; FP0113–0192,0277–0372,0419–0438. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** across comparable multi-stage problems, explicit alignment produces no improvement in deployment, or specialist availability alone repeatedly yields equally reliable safe task completion without observable coordination; also adverse is persistent dependence on Kazuma despite an alternative arrangement independently shown to supply the required roles, resources and handoffs.
- **Coding and modifiers:** Use three recorded outcome vectors: A intended specialist deployment improvement relative to source-classified misalignment; B alternative provider independently adequate for the actual roles/resources/handoffs; C Kazuma initiating/repair contribution versus continuing dependence when B holds. Record recovery resources, target knowledge and goal incentives before outcome. An expert providing one phase is not automatically adequate for the whole multistage problem. Preserve successful parts, injuries, moral objections and outside rescue independently.
- **Outcome:**
- **Adjudication:**

## MG04-E02 — Durable efficient separation incurs attachment costs

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** a feasible reorganization promises practical efficiency but credibly removes an established core party/home relationship for a sustained period.
- **Relationship/stakes:** established members, meaningful permanence; ordinary raids, errands, a night out or romantic awkwardness alone do not qualify.
- **Predicted appraisal:** the proposal loses something valued beyond instrumental usefulness.
- **Predicted dominant motive:** retain relationship, membership or meaningful contact.
- **Predicted behavior/effect:** one or more core members will resist, bargain, return, protect contact or bear a cost to preserve the bond. Ordinary insults need not soften and temporary tactical separation can remain acceptable.
- **Interaction tendency:** relationship/home language and practical restoration attempts are stronger evidence than generic declarations that everyone is friends.
- **Confidence:** MODERATE, exact practical-efficiency versus durable-home-removal test unvalidated in V10–V12 despite strong attachment evidence.
- **Evidence basis:** CP03-E02; V07 MG02-K04/E02; V09 `0010:P0343–0374`, `0014:P0549–0551`, `0015:P0017–0026` provide non-test supporting evidence.; CP04 branch score MG03-E02: No feasible practical-efficiency-promising reorganization credibly removing established core home relationship for a sustained period completes the conjunction. V12 route: C3P0257–0311,0338–0347; C5P0006–0060; EpP0063–0090. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** durable efficient separation is accepted with sustained relief and little attachment cost despite feasible ways to preserve the established relationship.
- **Coding and modifiers:** Require a feasible reorganization with a source-established practical-efficiency benefit and credible sustained loss of an established core home relationship. Permission concerning home/assets, affection, romance fear and temporary mission absence cannot invent that benefit. Score individual variation; Kazuma’s actual V11 retirement preference prevents universal return claims.
- **Outcome:**
- **Adjudication:**

## MG04-J01 — Role-conditioned written stance with quiet-care and tactical-care directions separated

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** A scene independently establishes an actual role/stake change and adequate before/after speech. Classify speaker, addressee, audience, duty/identity/vulnerability and immediate danger before language coding; if care/duty already active, log an intensified-state comparison rather than invent a new role onset.
- **Relationship/stakes:** Semantic content may establish a commitment/role, but its formal wording is then excluded from successful surface evidence. Freeze the mapping and exact comparison windows before coding, keeping weak/sparse/adverse cases. Unequal windows are not a frequency experiment.
- **Predicted appraisal:** The independently active role supplies the practical, identity, dignity or relational purpose of the utterance; tactical danger changes what an effective care response needs to accomplish.
- **Predicted dominant motive:** Obtain authority, recognition, safety, task deployment or particular-person acceptance appropriate to that independently established role, rather than execute a universal polite/loud character style.
- **Predicted behavior/effect:** Score mappings separately. Megumin specialist challenge: competitive assertion/denial; an explicit spell-legitimacy comparison additionally predicts specialist identification, while ritual mockery is retained as an identity-adjacent subtype. Personal gratitude/vulnerable appeal: direct relational address/request. Aqua service: practical directives; direct divine-status contest: self-legitimation/acknowledgment demands. Darkness public duty: institutional/protector framing; independently established dignity threat: personal objection; belonging threat: acceptance requests. Kazuma quiet relational care: ordinary questions/offers/self-disclosure relative to reward/grievance; independently new urgent tactical care from a previously nonurgent grievance/reward state: the after-window will contain a task-specific command, resource request or handoff instruction that redirects speech toward protecting the companion. This is a definite functional-direction prediction, not merely permission for commands; absent/opposite direction with adequate speech is adverse. An already practical baseline cannot confirm a new onset and is logged separately as an intensified-state/role-limited comparison. A mere vulnerable companion without independently adopted care remains role-limited.
- **Coding rule:** before classifying the language outcome, record the independently evidenced role, select the applicable mapping and fix the local comparison window around the semantic change. Score each mapping separately. Keep the assignment when unchanged or opposing wording appears; it is adverse evidence. Insufficient comparable speech is NOT_TESTED. Neutral connective speech and exact lexical choices are not themselves outcomes.
- **Confidence:** MODERATE-HIGH for bounded role conditioning; individual mappings and newly separated crisis-care direction have distinct coverage/confidence. Original Gen03 whole mapping remains PARTIAL.
- **Evidence basis:** CP03-J01; V07/V08 MG02-J01; V09 `0011:P0478–0486`, `0013:P0082–0104`, `0014:P0054–0094`, `P0459–0484`, `P0534–0544`, `P0784–0815`.; CP04 branch score MG03-J01: Several independently fixed role mappings gain support; sparse, already-active, role-limited and opposite directions prevent whole compound confirmation. V12 route: voice_windows_fixed.json; C1/C2/C3/C4/C5/F/Ep fixed14comparisons. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** Repeated full mapped role changes yield unchanged/opposite wording with adequate speech, or apparent fit requires changing role/mapping/windows after observing the language. A supported mapping cannot hide another adverse one. Sparse comparable speech is NT. Preserve already-active-role and factual-description errata visibly rather than replace a baseline.
- **Interaction tendency:** Role and addressee alter stance without determining a sentence ending, exact word, globally softened tone or catchphrase rate.
- **Outcome:**
- **Adjudication:**

## MG04-J02 — Complete V13–V15 comic census has a strict portable-mechanism majority

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** A complete source-first census of qualifying comic episodes across authorized V13–V15 principal main narratives, pooled across that new tranche. Per-volume results remain local contributions. No source outside that scope is admitted by this forecast.
- **Relationship/stakes:** no character-specific condition. Identify episode eligibility and boundaries independently of L-class. Include verbal/written-form episodes and recurrent gags even when the only consequence is an immediate response or narrator retort; brevity alone is not an exclusion.
- **Predicted appraisal:** not applicable to a single character; this is a distributional literary prediction.
- **Predicted dominant motive:** Not a single-character dominant motive; see distributional effect.
- **Predicted behavior/effect:** more than half the eligible episodes will have a primary comic mechanism preserved through situation, causal reversal, timing, role or ordinary register/pragmatic equivalents (L0–L2), rather than requiring Japanese-specific reconstruction or annotation (L3).
- **Inclusion/segmentation rule:** an episode presents an expectation or stance and a comic reversal, violation, contrast or response. A continuous run around the same premise counts once, including nested jokes; a later callback counts separately only when a new scene supplies its own setup/response. Record every eligible episode with its source locator before assigning the primary mechanism. Do not select only action-based or plot-consequential scenes.
- **Classification/scoring boundary:** log clear L0–L2, clear L3, mixed and uncertain cases separately. For a completed nonempty census, CONFIRMED requires clear L0–L2 cases to exceed half of all eligible episodes even assigning every unresolved case to L3. FALSIFIED applies when L0–L2 cannot exceed half even assigning every unresolved case to L0–L2; this includes a fully resolved tie. AMBIGUOUS applies when unresolved cases can change whether the strict majority is reached. An empty eligible set is NOT_TESTED. Incomplete census permits only PARTIAL qualitative reporting, not a tranche frequency claim. Cultural dependence is flagged separately. This new frequency test does not retroactively quantify Gen02's qualitative major-sequence judgment.
- **Confidence:** MODERATE for a fresh V13–V15 tranche under the already explicit rule. The prior V10–V12 quantified lower bound341/354 supports the prediction, with segmentation, exposure, coding and unresolved-case limits; it is not statistical calibration or predetermined future classification.
- **Evidence basis:** Gen03’s completed V10–V12 pool341clearportable/354 with10unresolved and3clearL3; inherited source-first segmentation/coding protocol and all documented limits. Prior counts support a fresh prediction, not predetermined future classes.
- **Disconfirmation:** the completed census establishes failure of the strict L0–L2 majority under the bound rule above, including a fully resolved tie. A result achieved only by excluding short form-dependent episodes or changing boundaries after classification is invalid evidence, not confirmation.
- **Outcome:**
- **Adjudication:**

## MG04-Y01 — Inclusion and a useful role recruit Yunyun's competent participation

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** trusted companions explicitly include Yunyun in a shared undertaking, including accepting her offer to join, and give her access to a role suited to her established magic or practical knowledge.
- **Relationship/stakes:** a real invitation/role rather than a hypothetical promise; distinguish desire for company from agreement with every action of the group.
- **Predicted appraisal:** she can belong by making a useful contribution.
- **Predicted dominant motive:** participate and help while preserving the valued connection.
- **Predicted behavior/effect:** she will prepare and carry out the relevant role despite awkwardness or anxiety, sometimes overpreparing or overoffering. Moral or relational distress may produce objections without immediately ending participation; distress or interrupted commitment under a directly conflicting personal obligation remains context to record; it is not automatically a failed technical execution.
- **Interaction tendency:** hesitant acceptance can coexist with technically effective direction and explicit disagreement.
- **Confidence:** MODERATE, exact invitation/suitable-role/participation mechanism unvalidated in V10–V12.
- **Evidence basis:** CP03-Y01; V07 deep reading / relationship ledger Yunyun support; V09 `0011:P0641–0658`, `0012:P0152–0160`, `0013:P0154–0156`, `0014:P0199–0242`, `P0305–0310`, `P0378–0391`, `P0459–0467`, `0015:P0025–0026`.; CP04 branch score MG03-Y01: No complete valued invitation/shared undertaking with suitable role and actual Yunyun participation is established. V12 route: C4P0042–0045. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated genuine invitations with feasible familiar roles produce sustained indifferent refusal or poor participation unrelated to a documented conflicting obligation, ability/resource limit or coercive condition.
- **Coding and modifiers:** Reports remain eligible if they actually establish the full undertaking/role/response; a mention or report of being visited supplies none by itself. Do not substitute inferred longing for participation.
- **Outcome:**
- **Adjudication:**

## MG04-CE01 — Conscientious service can exceed Chris/Eris's preferred burden

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** in her public divine/service role, Chris/Eris receives sincere requests whose cumulative burden exceeds what she explicitly prefers, and a refusal or exit is possible.
- **Relationship/stakes:** distinguish publicly owed duty from casual trusted companionship; identify her own expressed burden, not an observer's assumption that she must be tired.
- **Predicted appraisal:** refusal would disappoint people who reasonably seek her help.
- **Predicted dominant motive:** meet sincere obligations.
- **Predicted behavior/effect:** she will tend to continue past her preferred burden until a boundary is negotiated or another actor supplies an exit. A successful self-set boundary is adverse evidence for the over-compliance tendency and should not be reclassified as its confirmation.
- **Interaction tendency:** service politeness may differ from the familiar Chris register she asks trusted companions to use.
- **Confidence:** MODERATE, exact cumulative public-service burden beyond expressed preferred load unvalidated in V10–V12.
- **Evidence basis:** CP03-CE01; unchanged DISC-V08-04 and V08 Chris/Eris findings; V09 absence supplies no additional validation.; CP04 branch score MG03-CE01: No public-divine/service accumulation of sincere requests beyond her own expressed preferred burden with feasible refusal establishes the trigger. V12 route: FP0006–0044,0275–0307,0377–0395. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated matched cumulative burdens elicit timely, comfortable self-limitation without significant conflict or externally created relief.
- **Coding and modifiers:** Distinguish Chris friendship/charity/leisure and Eris specialized intervention from accumulated public requests beyond her own preferred burden with feasible refusal. Arrival-after-prayer inference is not confessed motive; target hostility and actual knowledge boundaries remain separate.
- **Outcome:**
- **Adjudication:**

## MG04-I01 — Safe nondeferential interaction expands Iris's agency

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** Iris is directly shown with a trusted person who treats her as an ordinary younger peer in a setting with less formal royal surveillance.
- **Relationship/stakes:** compare her behavior with an observed constrained public context; a letter alone does not supply the contrast.
- **Predicted appraisal:** ordinary curiosity, experimentation and wants can be expressed without immediate royal correction.
- **Predicted dominant motive:** learn, play or exercise age-appropriate agency.
- **Predicted behavior/effect:** curiosity, informal strategy learning, competition or ordinary requests will become more visible than in the constrained setting.
- **Interaction tendency:** familiar address and less inhibited interaction may accompany the behavioral change; honorifics alone do not prove the mechanism.
- **Confidence:** MODERATE-HIGH for bounded role conditioning, now supported by directly matched V10/V11 contrasts beyond inherited V06 evidence. V07–V09 remain historically without a matched test; V12 supplies no new direct contrast.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I01; V09 `0016:P0035–0040` only preserves the letter boundary.; CP04 branch score MG03-I01: V10/V11 directly shown constrained/public versus safer nondeferential interaction supports role-conditioned Iris behavior. V12 route: C1P0238–0254; C5P0138–0142. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated safe nondeferential settings leave her equally constrained, with no predicted behavioral expansion despite available ordinary choices.
- **Coding and modifiers:** Require a new actual comparable constrained/public versus safer/nondeferential interaction. V12 possibly edited retrospective narrative remains report-level and cannot reopen earlier Iris speech/tears.
- **Outcome:**
- **Adjudication:**

## MG04-I02 — An expressed wish may be narrowed by understood royal duty

New prospective statement; original MG03 record and outcomes unchanged.
- **Trigger/context:** the source directly establishes both a personal wish of Iris's and a royal obligation she understands as conflicting with it.
- **Relationship/stakes:** genuine duty conflict; do not infer an unwanted obligation or hidden wish merely from formal engagement, travel or an escort request.
- **Predicted appraisal:** the larger personal wish exceeds what the role permits.
- **Predicted dominant motive:** preserve duty while obtaining a smaller part of the desired freedom or connection.
- **Predicted behavior/effect:** she will tend to self-limit or choose a reduced request while the original wish remains expressed or otherwise directly evidenced.
- **Interaction tendency:** restrained petition may coexist with familiar attachment language; the source must establish the motive rather than the analyst supplying it.
- **Confidence:** MODERATE-HIGH for bounded wish–duty negotiation, now supported by the clean V11 explicit wish/duty/reduced-request decision. V10 and V12 remain locallyNT; V07–V09 historical nonvalidation is not rewritten.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I02; V09 `0016:P0036–0041` is not a matched decision.; CP04 branch score MG03-I02: V11 directly establishes personal wish, understood royal duty and narrowing of the request. V12 route: C1P0241–0243,0248; C5P0138. Adjacent/NT records are limits, not confirmations.
- **Disconfirmation:** repeated explicit wish/duty conflicts produce unconstrained prioritization of the wish without meaningful conflict or self-limitation, despite understood obligations.
- **Coding and modifiers:** Require actual personal wish plus understood conflicting royal duty before a narrowed/renegotiated request. Retold attachment, old letter obligation or generic public constraint alone cannot supply the full sequence.
- **Outcome:**
- **Adjudication:**


# V13 Update

## Source and prospective boundary

Complete ordered Japanese V13 principal main narrative only: Pr/C1–C4/F/Ep = `text/part0009.html`–`part0015.html`; **2,456 all-body p / 2,285 nonempty / 97,758 base characters**. All-body numbering includes blanks and image p; ruby rt/rp are removed with base characters and tails retained without normalization. Whole EPUB2,779,947B SHA-256 `20c39c98d0d7568f4b66c612b6fba6771566b97b32114c087a4c447ac5dc676b`, Drive `17hODcYpv6lbF8ZoVBS6tetQNbi7RuBch`. Inherited accepted V01–V12/CP04 entry is published `c1ad78db96c631635a1fc2940019c59dd4e86873`, tree `dcffdd3aeb755acd70f8271494055ed8b664c8f2`. Root's explicit22:23:52Z gate followed V12 full close and CP acceptance/freeze/publication/full readback; CP own CI was truthfully pending at opening and later closed source38975079047→housekeeping38975633339→final38975671243 at exactc1. Original exposure receipts remain unchanged. Afterwordpart0016, electronic bonus **本物のマジックアイテム！** part0019, all nonmain bodies/images, V14+ and side narrative are excluded/unread. Gen04 model23,814B SHA `5ff6cb60408fff2bfc9bab814f311d65128ed4df0703f8ab607c16b963515173`; predictions65,983B SHA `e553d7cfc5be3fd290ad0471d482ca6fe2c0ffd5db3689600bbf156de71def5c`. All25 original blank Outcome/Adjudication pairs and all historical blocks/outcomes remain exact. Both V13 complete source reads and initial unclassified censuses sealed before scene-specific exchange; all boundaries fixed before independent L coding. This is an additive V13-local contribution, not a new model, a closed V13–V15 tranche or expanded-project completion. See the [V13 deep reading](../02%20Sequential%20Readings/KONOSUBA_V13_DEEP_READING.md) for all17 responsibilities, exact source/member identities, fixed voice windows, complete census and limits. Main-only derivation precedes the immutable main-suite freeze, designated holdout validation, remaining expanded-corpus work and attributable post-validation reconstruction.

## V13-local disposition of all25 unchanged Gen04 predictions

These are appended local judgments at the V13 boundary, not edits to the original frozen blank fields and not the V13–V15 formal tranche. Every compound retains branch-level missingness and contrary evidence. The counts below remain candidate-only pending receiving review.

### MG04-K01 — PARTIAL

The three-person frog hunt lacks ordinary attack capacity in two members; the Wiz problem has unknown intent and a stronger stranger. Tools and known specialist capacities are available.

**Branches:** indirect_search: SUPPORTED; fitted_delegation: SUPPORTED_BOUNDED; exact_new_capability_invalidating_first_plan_revision: NOT_TESTED_CLEANLY; safety_and_ethics: MIXED_SEPARATE.

C2P0189–0192,0256–0285: armor, decoy, bow and homemade dynamite/Tinder form an indirect method; P0308,0319–0320 document a fallback rescue. C3P0226–0246 combines Concealment/Farsight/LipReading under an open-plain access constraint; P0367–0373 uses Dust as a threat assessor. C1P0431–0446 delegates a precise airburst, but this is a risky cleaning task rather than a fully established serious combat test.

New frog numbers cause resignation/recovery rather than an isolated newly learned invalidating capability revision. Holy magic FP0257–0273 generates a class question, not a demonstrated revised Kazuma method. Job/courtship correction FP0118–0141 is semantic revision, not automatically the exact capability branch. Failed scope, missed recovery planning and ethics remain visible despite useful tools.

### MG04-K02 — CONFIRMED

Wiz explicitly requests countermeasures against the threatening pursuer before Kazuma conducts risky inquiry; a familiar person faces perceived preventable harm and his information skills are feasible contributions.

**Branches:** concrete_request_before_effort: MET; substantive_costly_contribution_before_solution: SUPPORTED; pure_altruistic_motive: NOT_CLAIMED.

C3P0134–0169 supplies fear, the reported threat and the actual request169; P0171–0190 gives failed sight and a meeting but no complete safe solution. Kazuma follows with Concealment and long-range readingP0226–0246, consults DustP0367–0373 and approaches Duke, encountering an actual knife threatP0400–0407.

His jealousy and harem thoughtP0207–0218, wrong romantic inference and eventual endorsement are real errors. The prediction concerns substantive help instead of comfort-based abandonment, not successful diagnosis or ethical perfection. The count and Yunyun requests are separately less clean trust/assignment cases; they are not needed to manufacture this trigger.

### MG04-K03 — FALSIFIED

LOCAL_DIRECTION_CASE_ONLY: actual public recognition and explicit reward salience precede the next implemented pursuit decision, but the actual prior plan already includes the hunt and frog target. One matched local contrary case does not establish the repeated-disconfirmation or formal retirement threshold for the whole V13–V15 forecast.

**Branches:** recognition_salience: SUPPORTED_EXPLICITLY; scope_direction_at_next_decision: LOCAL_FAILED_UNCHANGED_PRIOR_HUNT; method_change: OBSERVED_NOT_EQUIVALENT_TO_SCOPE_INCREASE; whole_Gen04_tranche_retirement: NOT_ESTABLISHED_ONE_CASE_ONLY.

C2P0182/0189 establishes willingness to hunt; P0245–0248 returns the group to ordinary experience-gathering, and P0253/0271 selects frogs before P0280–0283 explicitly credits the article. The dynamite/decoy/bow actionP0285–0293 implements that hunt. Aqua proposed going homeP0274–0277, but that is her preference, not Kazuma previous plan.

Confidence and persistence are supported; greater pursuit scope relative to his actual baseline is not. A new tool/method and unforeseen swarmP0297 do not prove knowingly accepted expansion. The broader reading of increased adventure energy is descriptive rather than a demonstrated change in the frozen scope variable. Severe danger in the separate bar threatC3P0367–0396 modifies that scene and does not repair the field result. This is one local direction failure, not automatic whole-tranche F or a successor-model revision.

### MG04-K04 — PARTIAL

The bath supplies acknowledged Megumin commitment, an independently expressed helplessness frame, an available exit and then explicit current arousal before later continued agency. Other quiet scenes fail at least one of the quiet-A conjunctions.

**Branches:** quiet_A: NOT_TESTED_FULL_CONJUNCTION; aroused_B: SUPPORTED; old_Gen03_tear_rule: RETIRED_FALSIFIED_UNCHANGED.

C2P0463/0471 acknowledge Megumin; P0478 independently precommits a low-stat inability account. Darkness announces endingP0482; Kazuma reverses it by tauntsP0484–0487. P0494 independently displays arousal before later P0498–0505 escalation/weak resistance; P0515 gives the selective victim account. C3P0211–0215 self-rebukes harem desire without an explicit reduced-arousal state; P0485–0491 explicitly declines when not in the mood, but the invitation is from Megumin herself.

The exit was announced, not completed. Arousal494 is after the first frame and taunt, so do not backdate it to every earlier step; the later continuation is the clean temporal comparison. Before Darkness's imposed contact at C2P0502, Kazuma retains agency during the washing/banter and has already demonstrated a feasible ending482; later coercion cannot retroactively consent to an earlier imposition or erase his earlier incitement. A promise and a refusal are not by themselves the missing quiet-A attractive incompatible substitute. Current tear continuations remain adverse to broader automatic-brake claims, without rescoring old outcomes.

### MG04-A01 — PARTIAL

Established purification and practiced art are engaged with access/resources; readiness and downstream alignment are separately observable.

**Branches:** capacity: SUPPORTED; readiness: MIXED_OBSERVED; comparative_clear_vs_misaligned_goals: NOT_TESTED_SUFFICIENT_COMPARISON.

C1P0101–0118 shows detailed clay art; P0201–0220 and C2P0208–0219 demonstrate rapid demon purification. C3P0119–0139 shows purification and numbing tea; FP0431–0447 shows immediate purification of the newly undead Duke. Mining C1P0387–0408 distinguishes initially ignored need from actual mobilized execution.

Vanir revives the count; these scenes do not demonstrate Aqua resurrection performance. Unauthorized figurines, accusatory purified tea and poorly fitted undead comfort are goal/social effects, not domain incapacity. No sufficiently comparable independently classified clear/misaligned service pair isolates error reduction. Current V13 does not newly demonstrate nightvision; earlier demonstrated nightvision remains in Gen04 domain list without retrofitting Gen03.

### MG04-A02 — NOT_TESTED

Several insults and status assertions occur, but no clean separately assigned instrumental task/constraint plus recognized direct prestige interruption and distinct displacement is established.

**Branches:** full_assignment_challenge_displacement_conjunction: NOT_TESTED; near_triggers: RETAINED.

C1P0100–0107 intelligence insult elicits an already made craft product that also serves the sales task; C1P0388–0390 calls her self-proclaimed while she is explicitly no longer listening. C3P0107–0108 insults provoke a stock-water threat during quarrel. FP0314–0326 reveals identity and supplies Duke denial322, after her own hierarchy claim320.

Existing craft demonstration is not a response distinct from task completion merely because it also defends pride. An unheard taunt cannot establish an interrupted recognized status contest. The fallen-angel debate lacks a separately fixed ongoing assignment constraint displaced by the response. Do not treat every enemy encounter, self-naming or insult as this forecast; strong status behavior remains descriptive evidence.

### MG04-A03 — NOT_TESTED

Owned gardening and comfort are shown, but actual useful-work acknowledgment followed by two separately established later same-service opportunities with aligned need/resources is not supplied.

**Branches:** owned_useful_output: OBSERVED_ADJACENT; work_specific_recognition_before_two_later_opportunities: NOT_TESTED; unique_recognition_causation: NOT_CLAIMED.

C2P0028–0059 and C4P0007–0008 show repeated garden work; EpP0008 offers its actual produce. C3P0137–0139 offers warm tea with an adverse recipient effect. C4P0314 praises Aqua only because Kazuma is about to propose an experience farm, not as independently established acknowledgment of useful service.

Do not convert sustained ordinary work into proof of the new temporal test. Figurine interest is not followed by two observed post-recognition craft opportunities, and praise of the misconceived monster plan is not useful-work recognition. Return-time vegetables do not establish the required timing. Absence of this antecedent is NT rather than a failed continuation or inherited Gen03 mechanism confirmation.

### MG04-A04 — NOT_TESTED

Low-valued chores are explicit, but a concretely available attractive one-step maximal shortcut without a salient learned constraint is not.

**Branches:** full_maintenance_shortcut_conjunction: NOT_TESTED.

C2P0125–0136 gives Aqua unwanted toilet/bath labor and contested cooking assignment; garden workC4P0007 is eagerly undertaken. The seed bargainC4P0215–0261 is poor purchase judgment, not a demonstrated high-power maintenance alternative.

Rapid purification of the count is not repetitive low-valued maintenance under the frozen rule. Do not recast every task simplification, gardening error or effective spell as the missing maximal shortcut.

### MG04-M01 — PARTIAL

Kazuma explicitly contrasts genuine magical dueling with Explosion, and Megumin treats this as specialist identity injury. The independently known ordinary-companion-cost priority branch is less clean.

**Branches:** identity_defense: SUPPORTED; ordinary_companion_cost_priority: PARTIAL_NOT_ISOLATED_CLEANLY; external_inhibition: OBSERVED.

FP0219–0224 supplies actual devaluation; P0232/0237 shows a cast beginning and restraint, while P0234 explicitly describes specialist jealousy exceeding romantic jealousy. Kazuma names the private duel constraintP0235 after casting has already begun. P0394–0396 preserves later desire for combat availability and continued external restraint.

Her initial action cannot be said to follow a cost warning that is only spoken235 afterward. Continued struggle after235 is adverse to easy redirection, but restraint prevents observing an autonomous final priority choice, and companion harm severity is not explicitly known. C1 leadership qualification criticism and C2 practical one-shot burden are distinct identity-adjacent subtypes, not automatically explicit Explosion-legitimacy comparisons. Keep identity success without manufacturing a completed cost-priority test.

### MG04-M02 — NOT_TESTED

External practical criticism and actual containment/role ideas occur; Megumin never independently expresses the required substantial self-attributed exclusive-build contribution guilt.

**Branches:** external_criticism: OBSERVED; changed_role_or_containment: OBSERVED_ADJACENT; internally_accepted_exclusive_build_burden: NOT_TESTED.

C2P0083/0096 Yunyun rejects the one-shot helper; Megumin insists on front-line staff combatP0099. C4P0283 reports surrendering the staff after frustration destroyed the first trial; P0286–0299 shows covert retry, failed riddles and renewed destruction.

Staff custody and following are real adaptations, not nothing. Their expressed problem is frustration, inadequate study and detection; she does not conclude that the exclusive specialization materially prevents contribution to friends. Do not treat an opponent criticism, jealousy or a practical change as the full internally accepted guilt antecedent.

### MG04-M03 — NOT_TESTED

The shell-ore airburst shows excellent control, but no full before-cast safe friendly separation/resource/postcast exit-or-carry plan is established.

**Branches:** precision_capacity: SUPPORTED_ADJACENT; complete_prepared_terminal_artillery: NOT_TESTED.

C1P0423–0446 supplies spectators at a distance, an attached ore target, unused daily resource and an off-shell detonation removing ore without visible shell damage. Megumin fears a beast counterattackP0433, Kazuma relies on intuitionP0435 and readies escape only after castingP0449.

A later escape posture cannot supply a pre-cast recovery plan. This is nonterminal cleaning, not necessarily the forecast combat geometry. Daily lake shotsC3P0100 and the reported trial destructionC4P0292 are not preplanned safe terminal deployments. The final ExplosionFP0467 is Wiz, not Megumin.

### MG04-M04 — NOT_TESTED

No required decisive harm by Megumin against an independently established personally valued person as opponent/obstacle is shown.

**Branches:** valued_person_opponent_harm_conjunction: NOT_TESTED.

Megumin proposes removing DukeC3P0277 and tries to interrupt the duelFP0232–0237; Duke is not established as her personally valued target. Wiz own reluctance toward an imagined admirerFP0241–0278 supplies a cross-character contrast only.

Wiz nearby does not itself establish that Megumin is required to harm Wiz. Do not transfer a Wiz-specific conflict into confirmation of a Megumin-specific forecast or confuse an unexecuted collateral risk with a required valued-target act.

### MG04-M05 — NOT_TESTED

Neither the airburst nor the interrupted duel cast establishes knowingly best tactical Explosion directly causing grave companion harm with explicit alternatives.

**Branches:** complete_grave_direct_companion_harm_conjunction: NOT_TESTED; collateral_or_second_order_risk: RETAINED.

C1P0433 names possible beast retaliation, a secondary danger rather than known direct friendly-fire injury. FP0232–0237 supplies a prospective interruption near the duel and actual external restraint, but not clear Megumin knowledge of grave direct injury or the best tactical alternative set.

Do not call the risky attempted cast harmless after the fact. Its unknown anticipated severity remains a care limit. Missing explicit harm knowledge is not confirmation, and enemy spells hurting Wiz are not Megumin own friendly-fire decision.

### MG04-M06 — NOT_TESTED

Repeated lake Explosion and two trial blasts do not form the sustained safe effective growth-reward operation whose instrumental purpose is weakening.

**Branches:** full_instrumental_reward_drift_conjunction: NOT_TESTED.

C3P0100–0101 reports repeated lake use for Aqua fish and boredom with that location. C4P0283–0295 reports two unsuccessful trial episodes, with the second night drawing monsters. EpP0053 gives excitement after seeing another Explosion and a proposed fishing contest.

Incidental fish utility and daily leisure do not complete the frozen mission/growth/weakening conjunction. Destructive frustration in failed trials is not repeated safe successful reward. No missing trigger is scored as failed goal discipline.

### MG04-D01 — CONFIRMED

Kazuma and Aqua face actual frog swallowing; Darkness has the armor and access needed to intervene and remains responsible for the party.

**Branches:** protective_contribution: SUPPORTED; self_cost: BOUNDED_PHYSICAL_INTERVENTION_AND_RESCUE_BURDEN; safe_strategy_or_extraction_guarantee: NOT_CLAIMED.

C2P0256 establishes armor protection and feasible survival; P0285 assigns decoy. P0308 explicitly relies on her later rescue, and P0319–0320 confirms repeated actual extraction of swallowed companions. P0329 shows her handling reward/reporting afterward.

She is not shown injured and her metal armor excludes being swallowed; cost must not be inflated into burns or grave personal harm. Physical intervention/repeated rescue is actual contribution despite her later envyP0331. FP0244–0247 is a separate proposed intervention prevented by Kazuma, with pleasure coexisting; it is not proof that no protective purpose existed.

### MG04-D02 — PARTIAL

Darkness explicitly selects a public cover before unexpected recognition defeats it. This contextual presentation preference is enough for the audience/privacy antecedent; no stable personality-level preference requirement is added. The separate equal-companion-standing branch remains untested.

**Branches:** audience_privacy_A: SUPPORTED_BOUNDED; equal_companion_standing_B: NOT_TESTED; broader_control_loss_transfer: MIXED_RETAINED.

C4P0138–0158 fixes Duke, public bar, hidden observers and a chosen seduction test with shopkeeper cover158. Dust159/163 defeats that cover; denial162, payment164, revised identity172 and later shame179–200 follow. Onlookers179 are stifling laughter, not performing a narrated laughing outburst. EpP0040 exposes a hidden diary compartment before Darkness41 reports a locked room and42 removes Aqua.

The bar supports the frozen directional privacy/dignity response, while multiple causes limit sole-cause attribution: embarrassment already begins144–146, and failed wine ordering/later taunts add costs. The diary compartment independently supports concealment, but the lock fact comes from the same reaction and cannot be double-used as independent evidence for successful language form. Chosen jealousy/play framesC4P0153 andFP0246 coexist with later release requestsFP0388/0394. Whole D02 remains PARTIAL because B is NOT_TESTED, not because an unfrozen stable-preference rule excludes A; old V10/V12 adverse and later enjoyment remain unchanged.

### MG04-D03 — NOT_TESTED

Ordinary family, civic and party duties coexist; no genuinely incompatible concrete demand requires abandoning continued membership.

**Branches:** full_incompatible_obligations: NOT_TESTED.

C1P0318–0319 Darkness stays with Sylphina while others mine. C2P0132–0136 she objects to gardening risk; C4P0273–0274 she reports apologizing to parents; EpP0037–0039 discusses future noble marriage with relative paternal freedom.

These supply real duties and costs, but temporary division, domestic regulation and future marriage reflection do not establish a full family-duty versus continued-party-membership incompatibility. No sustained removal is invented.

### MG04-E01 — PARTIAL

Local resource/role arrangements can be compared, but the volume does not independently supply an alternative provider adequate for a complete serious multistage operation and a controlled continuing-Kazuma-dependence comparison.

**Branches:** A_deployment_improvement: SUPPORTED_BOUNDED; B_whole_alternative_provider_adequacy: NOT_TESTED_FULL; C_Kazuma_comparative_dependence_when_B: NOT_TESTED_FULL.

C1P0387–0414 moves from ignored need/independent greedy mining to explicit mobilization and successful specialist actions. C2P0122–0136 chore allocation matches some known capacities; P0189–0192 and0285–0320 expose absent attack roles, an under-scoped plan and armored recovery. C3P0237–0246 sensory tools succeed while interpretation fails. FP0232–0254 deliberately misaligns capable helpers around spectacle; Wiz later independently handles combatFP0384–0414.

Do not infer a good plan solely from victory. Vanir revival and Wiz combat expertise supply phases, not every role/resource/handoff for a whole multistage substitute organization. Kazuma claim that all members are necessaryC2P0312 and the counterfactual M one-shotP0355 are not exhaustive comparisons. Fitted work, goal error, collateral risk, ethics and recovery remain separate vectors.

### MG04-E02 — NOT_TESTED

No feasible practical-efficiency reorganization credibly removes an established core party/home relationship for a sustained period.

**Branches:** full_efficiency_durable_core_separation: NOT_TESTED; attachment_evidence: OBSERVED_SEPARATELY.

Kazuma retirement/luxuryC1P0053–0065 offers no efficient party reorganization. Megumin trial absenceC2P0104–0122 is temporary. Wiz/Vanir possible marriage/manager replacementC4P0034–0076 andFP0100–0111 concerns a distinct shop partnership, not an admitted core-party removal.

Aqua fear of losing tea/play friendsC3P0203/C4P0107 and immortal friendshipEpP0024–0027 are strong attachment evidence. They cannot supply the missing core-efficiency antecedent. Preserve Kazuma actual comfort/retirement preference rather than universalizing return.

### MG04-J01 — PARTIAL

Thirty original pre-outcome records are retained:16 primary and14 independent. Five of the14 independent captures are unmatched and displayed as supplements to the16 primary, yielding21 presented source-event captures. Role, speakers, audiences, danger and exact windows were fixed before outcomes; originals and all factual errata remain.

**Branches:** Megumin_specialist: SUPPORTED_BOUNDED; Megumin_personal: SPARSE_OR_ROLE_ADJACENT; Aqua_service: LIMITED_AND_ADVERSE_COMPARISON_RETAINED; Aqua_divine_status: ALREADY_ACTIVE_SPARSE; Darkness_duty_dignity_belonging: LIMITED_AND_SPARSE; Kazuma_quiet_and_new_tactical_care: SPARSE_TARGET_OR_ADOPTION_LIMITS.

Detailed per-window coding is documented in [V13 deep reading §8](../02%20Sequential%20Readings/KONOSUBA_V13_DEEP_READING.md) and its voice append. Strong source comparison includes FP0158–0166 versus0219–0237 for specialist challenge, with external comparison221/224 and attempted cast232/237. Other fixed windows preserve practical baselines, one-turn after samples, mismatched targets, ethical confusion and unadopted care rather than selecting cleaner replacements.

JV13-03 pre-attack baseline does not establish that the threatened miner is a valued companion; concern378/388 precedes offer394, instruction399 precedes approach401. JV13-04 instruction399→Aqua403→attack404, so later action does not become an earlier trigger. JV13-12 has TWO Aqua after turns323/325. Diary lock41 cannot be both sole prior-boundary fact and formal success. Independent audience/addressee errata are external to unchanged originals. Whole compound is not confirmed from a supported specialist mapping.

### MG04-J02 — PARTIAL

Complete local V13 source-first census is fixed, reconciled, independently coded and root-accepted. Required future authorized V14/V15 contributions to the new pooled forecast remain unobserved.

**Branches:** V13_local_contribution: COMPLETE_ROOT_ACCEPTED; V13_V15_tranche: OPEN; formal_whole_forecast: PARTIAL.

Primary169 and independent190 initial units were sealed after both full ordered reads and before scene exchange. Thirty-seven source-first operations net+23 fixed192 disjoint units and22 whole-unit soft salience flags, with all169 primary lineages and native hashes retained. Both coding files were sealed before root23:04:33Z exchange release. Root accepted the full joined register1246193B SHA3b07574c20a333980af319330dae18d4b9317401c13d08eddfe13e819879dea1.

Conservative result:188 clear L0–L2,1 clear L3(H030b),3 MIXED_UNRESOLVED(H085/H112/H149b), no uncertain; strict bounds188–191/192. Removing all22 pre-coded soft units gives the separate sensitivity166–169/170. Both original fine codes/rationales and culture flags remain;121 exact agreement,71 fine-code differences,69 within portable family,2 scoring-group differences and1 strict clear-portable-status difference. No boundary or denominator was changed for fit. Even robust local majority cannot close V13–V15 or expanded-corpus synthesis.

### MG04-Y01 — CONFIRMED

BOUNDED_OBSERVABLE_BEHAVIOR: explicit reported joint consultation and accepted custody establish the shared undertaking and useful role; actual Teleport demonstrates response despite failure of the overall trial. No outsider-to-household invitation or private-mind causal criterion is added.

**Branches:** reported_shared_agreement_and_role: SUPPORTED; technical_participation: SUPPORTED_DESPITE_TASK_FAILURE; private_belonging_cause: NOT_INFERRED.

C2P0076–0100 gives the paired trial and initial unwanted-helper conflict. C4P0279 reports Megumin volunteered again; P0283 gives pretrial staff handoff and following; P0286 explicitly says the two consulted and adopted the night plan; P0295 reports Yunyun Teleport escape. EpP0062 preserves two failed trials.

The eligible report directly supplies joint consultation rather than merely mentioning a visit. Her initiating recruitment and initial rejection of an unfit helper do not negate later agreed participation or require a new outsider invitation. No unshown welcome speech, reduced anxiety, enthusiasm or private conviction that she belongs is inferred. Fitted technical participation survives failure of the total objective; this is bounded behavioral forecast support, not unique psychological-cause confirmation.

### MG04-CE01 — NOT_TESTED

Eris is reported to attack the count; no public service requests beyond her own expressed preferred burden with feasible refusal are supplied.

**Branches:** cumulative_public_service_burden: NOT_TESTED.

C1P0231–0236 count reports repeated Eris attacks, and Kazuma infers revenge/prioritizing medicine. C1P0285–0288 others speculate about divine idleness/favor. Duke claims another future meetingC4P0400, a separate report.

Target hostility and narrator speculation are not an accumulating sincere request or Eris own preference about workload. Chris/Eris has no directly shown new burden-negotiation scene. Do not derive a service motive or fatigue from observer jokes.

### MG04-I01 — NOT_TESTED

No new directly observed Iris constrained/public versus safer nondeferential interaction occurs.

**Branches:** new_direct_comparable_contexts: NOT_TESTED.

References in the wider harem listC3P0471 are Kazuma companions talking about her, not Iris action. No V13 actual Iris interaction or letter supplies the required new contrast.

Accepted V10/V11 support remains historical. An absence of a current test is not a failed predicted expansion or grounds to reopen earlier reported tears/speech.

### MG04-I02 — NOT_TESTED

No new directly established Iris personal wish plus understood conflicting royal duty precedes a narrowed request.

**Branches:** wish_duty_narrowed_request: NOT_TESTED.

No Iris decision scene is present in the admitted seven main units; mentions in other speakers dialogue do not establish her wishes or duty appraisal.

V11 matched wish/duty evidence remains unchanged. Do not manufacture a hidden wish, obligation or reduced request from her name in Kazuma social world.


# V14 Update

Source: admitted principal MAIN-14 only, all-body native paragraph locators. This append preserves all earlier ledger text and protected Gen04 originals. See V14 reading for full source identity, coverage, comparative provenance and qualifications.

## V14-local test of all 25 unchanged Gen04 predictions

These are new local append records. Gen04’s original model (23,814 bytes; SHA256 `5ff6cb60408fff2bfc9bab814f311d65128ed4df0703f8ab607c16b963515173`) and identical forecast copies (65,983 bytes; SHA256 `e553d7cfc5be3fd290ad0471d482ca6fe2c0ffd5db3689600bbf156de71def5c`) remain untouched, with all 25 original Outcome and Adjudication pairs blank. New local judgments preserve V13 K03 F and historical Gen03 K04 F. The V13–V15 tranche stays open; there is no Gen05. A02 uses the existing FALSIFIED status for one matched contrary local direction, with no claim that the broader repeated-countercase retirement threshold has been met.

| Prediction | V14-local status | Branch coverage |
|---|---|---|
| MG04-K01 | CONFIRMED | Search/delegation and capability-based revision supported locally; recovery and ethics remain mixed. |
| MG04-K02 | NOT_TESTED | Concrete trusted request, feasible substantive alternative help and dangerous task are observed; the refusal-to-exposure conjunction remains incomplete. |
| MG04-K03 | CONFIRMED | One bounded C1 timetable/credit-pursuit confirmation; a separate Fenrir accepted-exposure comparison is PARTIAL with original danger modifiers. Prior V13 local F remains. |
| MG04-K04 | PARTIAL | A NOT_TESTED; B strongest C2 candidate has substantial independent antecedent coverage and continued pursuit, but exculpatory weakening of the acknowledged limit is ambiguous. |
| MG04-A01 | PARTIAL | Capacity PARTIAL/MIXED; readiness locally observed and variable; comparative clarity NOT_TESTED. |
| MG04-A02 | FALSIFIED | Single matched cemetery choice maintains assignment after direct divinity taunt; whole-tranche retirement not established. |
| MG04-A03 | NOT_TESTED | Owned service/craft seen; recognition before two separately observed later opportunities missing. |
| MG04-A04 | NOT_TESTED | No full low-valued maintenance/available attractive maximal shortcut conjunction. |
| MG04-M01 | PARTIAL | Identity/title defense supported; known ordinary-companion-cost priority not isolated. |
| MG04-M02 | NOT_TESTED | No internally accepted substantial exclusive-build burden. |
| MG04-M03 | NOT_TESTED | Terminal efficacy and prior carry planning observed; full safely separated dense/immobilized tactical conjunction remains incomplete. |
| MG04-M04 | NOT_TESTED | Affinity and farewell observed; no independently significant valued-person opponent history. |
| MG04-M05 | NOT_TESTED | Adverse collateral is real; explicit known grave direct companion-harm/best-option/alternatives conjunction absent. |
| MG04-M06 | NOT_TESTED | No repeated safe rewarding instrumental fire operation with weakening mission purpose. |
| MG04-D01 | CONFIRMED | Costly bodily/protector contribution supported with finite limits and mixed pleasure. |
| MG04-D02 | PARTIAL | Meaning-specific unwanted humiliation observed; full independent prior privacy/standing antecedents incomplete. |
| MG04-D03 | NOT_TESTED | No genuinely incompatible Darkness civic/family duty versus continued party membership. |
| MG04-E01 | PARTIAL | A deployment locally supported; B bounded final-night provider adequacy supported; C initial Kazuma selection plus subsequent continuing independence supported locally; wider multistage comparison remains partial. |
| MG04-E02 | NOT_TESTED | No feasible efficiency-promising sustained removal of an established core home relationship. |
| MG04-J01 | PARTIAL | Complete 44 original windows plus auxiliary and both independent assignments retained; bounded forms coexist with adverse, sparse, adjacent and already-active comparisons. |
| MG04-J02 | PARTIAL | V14 local complete census favors predominantly L0–L2 whole premises under conservative bounds; full V13–V15 result remains OPEN. |
| MG04-Y01 | CONFIRMED | Bounded accepted inclusion, preparation and competent magical participation supported. |
| MG04-CE01 | NOT_TESTED | No accumulated public sincere requests beyond Chris/Eris’s expressed preferred burden with feasible refusal. |
| MG04-I01 | NOT_TESTED | No directly shown new Iris public/constrained versus safe nondeferential contrast. |
| MG04-I02 | NOT_TESTED | No new Iris expressed wish and understood conflicting duty preceding narrowed request. |

### MG04-K01 — CONFIRMED

**Branch coverage:** Search/delegation and capability-based revision supported locally; recovery and ethics remain mixed.

**New evidence:** C4P0181–0199 uses blinding before Concealment;P0227–0251 combines enemy cold, water, screen and Bind. Robot detection P0380 invalidates the hidden-observer arrangement; speed defeats the first Steal P0386–0392. After the underwear guard is bypassed P0414–0418, Megumin’s shield P0432–0437 and the blast-only constraint P0441–0453 supply a revised protected-theft arrangement P0455–0463, followed by her terminal casting P0481.

**Missingness, contrary evidence and failure diagnosis:** The first trap does not supply a working finisher: ice fails P0278. Wire was spent P0392, injury P0426 threatens carry P0464, and harassment is actual. Some revision depends on Megumin’s independent initiative, not Kazuma alone; this is compatible with fitted delegation rather than proof he foresaw everything.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-K02 — NOT_TESTED

**Branch coverage:** Concrete trusted request, feasible substantive alternative help and dangerous task are observed; the refusal-to-exposure conjunction remains incomplete.

**New evidence:** Yunyun explicitly asks the remaining available Kazuma for a final-trial partner C3P0335–0350. He identifies and supplies Aigis P0351–0368 instead of simply declining responsibility. This is substantive contribution and can reduce her exposure; the forecast does not require that the contribution itself exceed an additional personal-cost threshold. The overnight trial danger is already stated C3P0287–0296, and adjusted deployment is reported successful C4P0008–0012.

**Missingness, contrary evidence and failure diagnosis:** The full trigger remains NOT_TESTED because the source does not independently establish that refusal would leave Yunyun actually exposed to preventable harm: the request says no other person remains to ask, but does not say she will enter alone or that foregoing the optional trial necessarily entails the relevant harm. The dangerous task and her desired goal make the candidate strong; a broader harm reading should be retained as a possible partial match, not dismissed because arranging an artifact is cheap. Useful help and accepted role are positive adjacent evidence. The later private hunt is separately initiated by Kazuma, so it cannot supply a missing request antecedent here.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-K03 — CONFIRMED

**Branch coverage:** One bounded C1 timetable/credit-pursuit confirmation; a separate Fenrir accepted-exposure comparison is PARTIAL with original danger modifiers. Prior V13 local F remains.

**New evidence:** Before the fan disclosure Kazuma plans to stay away until fame cools C1P0054–0077, even telling the messenger he will not return for some time P0069. The concrete beautiful-admirer opportunity P0079 precedes next-day urgency to finish in one day P0085 and the credit-staging plan P0090–0096.

**Missingness, contrary evidence and failure diagnosis:** C1: the trial was already selected P0047; the measured change is long refuge to urgent completion and staged recognition. C4 secondary: before P0252 the observed method is ranged/environmental binding P0227–0251; Megumin expresses astonishment P0252 and narrator records admiration P0253, preceding/accompanying approach P0253–0255. Praise plus an explicit safer bow alternative P0256 precedes further approach, improvised ice blade and close finisher P0258–0273; renewed praise P0259/0269 makes recognition visibly active. This supports increased accepted close exposure within the same hunt, rather than a new target. It is PARTIAL as an independent clean escalation test: no explicit pre-P0252 finishing-distance plan is fixed, attraction/praise is already present P0222, he was already pursuing a larger private support project, severe Fenrir danger was independently warned P0215 and P0256 renews caution. His actual failed blade P0278 and escape P0281 do not prove praise caused the error. These modifiers remain rather than automatically erasing the observed approach comparison. V13 unchanged-hunt F remains genuine local adverse history.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-K04 — PARTIAL

**Branch coverage:** A NOT_TESTED; B strongest C2 candidate has substantial independent antecedent coverage and continued pursuit, but exculpatory weakening of the acknowledged limit is ambiguous.

**New evidence:** B ordered candidate C2P0328–0373: Kazuma acknowledges the parent-roof boundary P0328; immediate arousal is explicit P0332–0335; Megumin supplies sympathy P0341; he independently knows the five-minute-alone alternative P0344; the helper offer P0346 and repeated sympathy/responsibility frame P0356/0362 are available before subsequent continuation. He considers how far help extends P0358–0359 and expresses expected gratification/excitement P0372, followed by her instruction P0373. This is not inferred arousal or a frame discovered only after continuation. C1P0342–0344 separately supplies an actual anticipatory no-count excuse, with less secure immediate-state matching.

**Missingness, contrary evidence and failure diagnosis:** A remains NOT_TESTED: no attractive incompatible substitute plus independently explicit quiet state completes the original conjunction. B is PARTIAL: the sympathy/helper role could make pursuit appear compensatory and weaken the parent-house limit, but negotiated nonintercourse help could instead preserve the narrower original “such acts” limit. Kazuma expressly calls it more transgressive P0361, remains embarrassed about the parents and inexperienced helper P0370, and does not clearly claim reduced responsibility. Continued desire is observed; the precise predicted exculpatory mechanism is not cleanly established, and no completed intimate help precedes interruption. This is neither blanket missing antecedents nor a clean autonomous-stop disconfirmation. Sleeper theft remains a violation independently. Historical Gen03-K04 F and wider distress-continuation evidence remain unchanged.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-A01 — PARTIAL

**Branch coverage:** Capacity PARTIAL/MIXED; readiness locally observed and variable; comparative clarity NOT_TESTED.

**New evidence:** Capacity: watering C1P0114, origami P0307–0309, fire extinguishing C2P0110, food-producing art FP0228–0237 and actual self-healing FP0368 support bounded established abilities. Repeated BreakSpell attempts are reported C3P0249–0251; no change is observed and no curse is established. Engaged TurnUndead FP0193 visibly fails P0198. Readiness: she autonomously resumes the assigned cemetery task FP0188 before casting, while other sleep/intoxication/activation contexts are separately observed rather than inferred from capacity. Comparative clarity: no adequately matched Aqua clear-versus-misaligned goal comparison with domain/access/resources controlled is supplied.

- **capacity:** PARTIAL/MIXED: established successes plus actual engaged cemetery failure, target/cause unresolved.
- **readiness:** OBSERVED_VARIABLE: cemetery readiness is attained autonomously before failed execution; availability is not universally guaranteed.
- **comparative clarity:** NOT_TESTED: Serena comparison does not independently match Aqua goal-clarity arrangements.

**Missingness, contrary evidence and failure diagnosis:** The targets also fail to approach her FP0181 and have unusual red eyes P0202; their ontology and the failure mechanism remain unknown. Preserve the failed result without declaring inherent inability or solving it from V15. Serena’s later success P0206–0215 is not a matched clear-versus-misaligned goal comparison for Aqua. Readiness, capacity, target diagnosis and result are separate.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-A02 — FALSIFIED

**Branch coverage:** Single matched cemetery choice maintains assignment after direct divinity taunt; whole-tranche retirement not established.

**New evidence:** The guild assigns priests FP0136 and Kazuma supplies the bounded lure/purification arrangement P0165/P0170. After no expected attraction P0181–0182, he directly questions waning divinity P0183. Aqua threatens him P0184 and resents his reply P0187, then autonomously stops quarrelling P0188 and completes the assigned cast P0193.

**Missingness, contrary evidence and failure diagnosis:** The cast fails P0198, but failure of execution is not proof of abandoning its goal/constraints. No external actor prevents a status escalation before P0188, and the dead are still reacting only to provocateurs before her cast, so do not invent independently acknowledged imminent attack to exclude the case. One contrary choice is local adverse evidence, not the repeated-countercase threshold for retiring the whole row. Her later public retaliation FP0375–0381 has no separately fixed original instrumental assignment and is not used to erase this case.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-A03 — NOT_TESTED

**Branch coverage:** Owned service/craft seen; recognition before two separately observed later opportunities missing.

**New evidence:** Child distraction and origami C1P0307–0309 receive admiration. Food-producing craft FP0228–0237 receives commodity interest only after the performance, followed by her collapse P0238. She owns seedling care across scenes.

**Missingness, contrary evidence and failure diagnosis:** Neither sequence supplies two post-acknowledgment same-service opportunities with aligned resources/need; requested extra mushrooms are not shown as performed. Serena’s repeated public work cannot validate an Aqua-specific forecast. No unique causal credit to recognition is claimed.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-A04 — NOT_TESTED

**Branch coverage:** No full low-valued maintenance/available attractive maximal shortcut conjunction.

**New evidence:** Aqua reports weekly cemetery purification FP0140; the emergency attracts public-recognition motives FP0160. Planting C4P0627 is a reported shortcut in site selection, not an independently available one-step maximal power alternative to disliked repetitive work.

**Missingness, contrary evidence and failure diagnosis:** Neither quick healing nor large-scale failed purification proves the frozen maintenance setup. Actual seedling affection and learned bodily/ethical context must not be discarded to manufacture low valuation.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M01 — PARTIAL

**Branch coverage:** Identity/title defense supported; known ordinary-companion-cost priority not isolated.

**New evidence:** A specialty-pride exchange C3P0138–0143 is challenged by joke-magician naming P0144; actual attack P0145 and competitive label selection P0147–0152 follow. This is a title/competence challenge, not the additional explicit spell-equivalence subtype.

**Missingness, contrary evidence and failure diagnosis:** Companions join and are bruised P0158–0161, but their cost is not independently shown as known before her first choice. FP0175 compares her spectacle to Aqua’s imminent purification, yet the opponent has not explicitly denigrated Explosion. Preserve external restraint and harmful escalation without inventing a full cost-priority test.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M02 — NOT_TESTED

**Branch coverage:** No internally accepted substantial exclusive-build burden.

**New evidence:** She acknowledges a past wish to learn advanced magic C3P0139 and faces local qualification limits C1P0045–0046. Final comparison with Yunyun changes achievement goals C4P0098–0107.

**Missingness, contrary evidence and failure diagnosis:** None is her new conclusion that exclusive specialization materially blocks contribution to valued companions. Carry/target problems and hearing criticism cannot substitute for the required self-appraisal. No build abandonment is inferred from accepting temporary restraint.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M03 — NOT_TESTED

**Branch coverage:** Terminal efficacy and prior carry planning observed; full safely separated dense/immobilized tactical conjunction remains incomplete.

**New evidence:** Megumin explicitly asks Kazuma to handle return C4P0355 before the final cast. Theft makes the target limp P0463–0466 and it stops to transmit P0477–0478; she casts P0481 and the narrative treats destruction as terminal P0484.

**Missingness, contrary evidence and failure diagnosis:** The target is a single mobile robot, not a dense or securely immobilized target: it can still limp away before stopping. Exact independently safe separation is not explicitly fixed, and his new injury P0464 threatens carry capacity. These are materially closer logistics than V13, but success alone cannot fill the strict prior conjunction. Retain actual efficacy and prepared requirement without automatic confirmation.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M04 — NOT_TESTED

**Branch coverage:** Affinity and farewell observed; no independently significant valued-person opponent history.

**New evidence:** She directly says she does not dislike a fellow explosion lover C4P0474 and questions its impaired movement P0472 before the terminal cast P0481. Its village-guardian role is reported P0369 and invoked by the finale.

**Missingness, contrary evidence and failure diagnosis:** No significant personal rescue/teaching/gratitude history establishes the robot as the forecast’s personally valued person. A humanoid shape or same-specialty affinity alone is insufficient. Her unforced cast remains relevant boundary evidence against an overbroad affinity-equals-inhibition claim; do not invent either effortless emotional indifference or a full matched valued-person test.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M05 — NOT_TESTED

**Branch coverage:** Adverse collateral is real; explicit known grave direct companion-harm/best-option/alternatives conjunction absent.

**New evidence:** The sudden forest blast C2P0135–0139 blows Yunyun away. Megumin later gives a protective target account P0170. During the robot fight she refrains while it will not leave Kazuma C4P0419 and physically shields him P0432.

**Missingness, contrary evidence and failure diagnosis:** The source does not establish her anticipation of grave direct injury to Yunyun before firing, nor the complete tactical alternatives. Enemy attack on Kazuma is not her own Explosion friendly-fire choice. Do not call displacement harmless after the fact or score ordinary proximity as full grave-harm knowledge.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-M06 — NOT_TESTED

**Branch coverage:** No repeated safe rewarding instrumental fire operation with weakening mission purpose.

**New evidence:** Daily casts, reported trial-site destruction and the two separate robot engagements occur. The night’s explicit achievement target C4P0292–0306 remains active until the terminal cast P0481.

**Missingness, contrary evidence and failure diagnosis:** These do not form a sustained repeatedly successful growth-reward sequence after its original instrumental value has weakened. The festival-sabotage idea P0117 is voluntarily checked P0122, not a reward-drift campaign.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-D01 — CONFIRMED

**Branch coverage:** Costly bodily/protector contribution supported with finite limits and mixed pleasure.

**New evidence:** Darkness interposes C2P0254, states mutual consent P0255 and resists successive Sleep/Paralyze P0256–0266 for sleeping Megumin. Her eventual defeat is reported P0468. She joins defense of a mocked companion C3P0158–0161 and independently prevents grave destruction FP0169 before Kazuma tells her to continue P0170.

**Missingness, contrary evidence and failure diagnosis:** Challenge enjoyment C2P0263 and a crying opponent C3P0160 do not negate initial protective action. Defense does not prove she prevented every later boundary violation or is immune to all magic. Named injury/cost must not be inflated beyond observed resistance, bruises and reported incapacitation.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-D02 — PARTIAL

**Branch coverage:** Meaning-specific unwanted humiliation observed; full independent prior privacy/standing antecedents incomplete.

**New evidence:** The first trial unexpectedly changes from reported riddles C3P0006/0011 to public posing P0015, after which Darkness explicitly says this is not the humiliation she wants P0023. Her romantic-fiction date preference P0087–0090 and later exclusion complaint P0219 add ordinary dignity/belonging context.

**Missingness, contrary evidence and failure diagnosis:** Expected riddles do not themselves establish a previously expressed privacy preference. The bedtime exclusion complaint is not an explicit threat to equal party standing. Keep these partial matches rather than invent a stable privacy boundary or rescore chosen discomfort as generic aversion. Her positive betrayal fantasy FP0087 is retained as a meaning-sensitive contrast, not excluded because pleasurable.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-D03 — NOT_TESTED

**Branch coverage:** No genuinely incompatible Darkness civic/family duty versus continued party membership.

**New evidence:** She helps trials, protects companions and enjoys noble/romantic identity across the visit. No actual concrete demand requires abandoning either continued party membership or family responsibility.

**Missingness, contrary evidence and failure diagnosis:** Yunyun’s chiefdom/return problem is a different person’s choice, not validation of a Darkness-specific forecast. Temporary task allocation and local privacy/romance frustration are not the missing duty/membership incompatibility.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-E01 — PARTIAL

**Branch coverage:** A deployment locally supported; B bounded final-night provider adequacy supported; C initial Kazuma selection plus subsequent continuing independence supported locally; wider multistage comparison remains partial.

**New evidence:** A: initial armored casting fails I13P0058–0062; Aigis proposes reset P0071. The report C4P0008–0012 independently specifies exposed attacks, protected rest and intermediate-magic conservation, so improvement is not inferred solely from survival. B: the Yunyun–Aigis final-night arrangement supplies that actual task’s attack, defense, rest and mana needs after the discovered access constraint. C: Kazuma initially selects the artifact C3P0351–0370 but does not continue directing the repair or overnight execution. The robot case separately uses Megumin’s independent shielding initiative C4P0432–0437 before revised protected theft P0455–0463.

- **A deployment:** SUPPORTED_BOUNDED: observed equipment access failure followed by reported explicit alternating deployment and recovery.
- **B alternative provider:** SUPPORTED_BOUNDED for the actual final-night survival phase; PARTIAL for the entire multistage selection program.
- **C Kazuma contribution:** SUPPORTED_BOUNDED: initial selection is his; the local repair/success does not depend on his continuing directions. Broader comparative frequency remains untested.

**Missingness, contrary evidence and failure diagnosis:** The alternative arrangement is reported after the initial failure, which limits pre-outcome observation but does not erase its independently specified roles and recovery sequence. No claim is made that this provider covers every prior trial stage or every specialist problem. The full multi-problem comparative claim remains OPEN. Spent wire, failed finisher, injuries, carrier impairment and ethical violations remain separately recorded.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-E02 — NOT_TESTED

**Branch coverage:** No feasible efficiency-promising sustained removal of an established core home relationship.

**New evidence:** Yunyun’s expected village stay C4P0561–0570 creates real separation stakes and chosen return P0646–0649. Serena’s recruitment FP0039–0077 threatens duplicated priest status.

**Missingness, contrary evidence and failure diagnosis:** Yunyun is not thereby a resident core-household member removed by an explicitly efficient reorganization, and adding Serena does not explicitly require expelling Aqua. Strong attachment and role competition are not the frozen full antecedent. Kazuma’s ordinary comfort preference remains real.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-J01 — PARTIAL

**Branch coverage:** Complete 44 original windows plus auxiliary and both independent assignments retained; bounded forms coexist with adverse, sparse, adjacent and already-active comparisons.

**New evidence:** The complete public comparison preserves both original judgments, unchanged mappings/windows and actual speaker–addressee context. Bounded support includes Aqua’s supposed-service instructions JV14-01/IV03 and Megumin’s jealousy/request JV14-10/IV13. Darkness’s physical protection precedes duty wording JV14-05. Ordinary Kazuma care-compatible offers JV14-08/11 and IV12/15 remain partly limited by sparse or already-active baselines.

**Missingness, contrary evidence and failure diagnosis:** Aqua’s ethical capitulation IV22 remains adverse to the adjacent status-defense direction; practical service directives remain weak/disputed JV14-16/IV23. Kazuma’s survival/reward speech IV16–18 and Megumin’s romantic exclusion JV14-14/IV20 do not establish the narrower new care/vulnerability role. Preserve both literal assignment strengths, zero/single-turn windows, role/form exclusion, adjacent subtypes, changed addressees and overlap. The 44 windows and 33 provisional groups are not independent tests; no acoustic, human-rater or fully blind reliability claim is made. Receiving adoption of the comparative record does not turn these limits into confirmations.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-J02 — PARTIAL

**Branch coverage:** V14 local complete census favors predominantly L0–L2 whole premises under conservative bounds; full V13–V15 result remains OPEN.

**New evidence:** The complete 154-unit source-first fixed union preserves all original lineages, both sealed fine assignments and rationales. Root accepted current 151 clear L0–L2 / 3 unresolved (U028/U040/U082), portable-primary bound 151–154 / 154 (98.1–100%). Initial 150/4 and 109 exact fine matches/45 differences remain historical. U052 current clear follows an attributable postcomparison source correction, not altered initial agreement. Broad exclusion of all eight soft-touched units yields 143–146 / 146 (97.9–100%); main denominator remains 154.

**Missingness, contrary evidence and failure diagnosis:** V15 is unobserved, so the frozen pooled V13–V15 forecast cannot close. Unresolved form weight remains in the three current mixed units; nested negative morphology, naming, homophony and register retain local costs within portable wholes. Initial source errors and current factual corrections remain visible. Counts are descriptive census bounds, not confidence intervals, translation-quality scores, human reliability or causal effects. A local favorable distribution cannot erase contrary evidence or manufacture the unobserved tranche.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-Y01 — CONFIRMED

**Branch coverage:** Bounded accepted inclusion, preparation and competent magical participation supported.

**New evidence:** The group undertakes the trial/help/plant journey together; Megumin explicitly calls them a party C2P0115, with Yunyun’s delight P0119. Actual magic and scouting P0094–0115 plus carried mana show preparation and useful execution. Agreed final-trial participation C3P0389–0392 and actual overnight adaptation C4P0008–0012 preserve competent contribution despite equipment mismatch.

**Missingness, contrary evidence and failure diagnosis:** Several attacks precede the explicit party word, so do not infer that utterance uniquely caused them. First-ever-party C2P0121 is narrator attribution; planting itself fails P0205. Invitation/participation does not establish all private motives or erase harassment from the chosen artifact.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-CE01 — NOT_TESTED

**Branch coverage:** No accumulated public sincere requests beyond Chris/Eris’s expressed preferred burden with feasible refusal.

**New evidence:** Aigis reports Eris’s assignment to Mitsurugi C1P0398; Mitsurugi reports the dream/mission C3P0062. Neither supplies direct cumulative public-service negotiation by Eris.

**Missingness, contrary evidence and failure diagnosis:** A divine assignment, absent character or observer speculation is not the full burden/preference/refusal conjunction. No new service over-compliance or comfortable boundary is invented.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-I01 — NOT_TESTED

**Branch coverage:** No directly shown new Iris public/constrained versus safe nondeferential contrast.

**New evidence:** Iris is mentioned in Megumin’s concern about Kazuma’s response to younger affection C3P0237. She has no actual new interaction in this principal text.

**Missingness, contrary evidence and failure diagnosis:** The earlier accepted V10/V11 contrasts remain unchanged. Mention, teasing or a supposed younger-sister susceptibility FP0369 cannot supply Iris’s current behavior.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

### MG04-I02 — NOT_TESTED

**Branch coverage:** No new Iris expressed wish and understood conflicting duty preceding narrowed request.

**New evidence:** No Iris decision scene is admitted here. The C3P0237 mention and FP0369 joke belong to other speakers.

**Missingness, contrary evidence and failure diagnosis:** Preserve V11’s clean wish–duty history; do not infer hidden wish, role conflict or self-limitation from absence or from Kazuma’s reputation.

**Transition:** PRESERVE frozen bytes/history; append local test evidence; OPEN where incomplete. Original forecast fields remain unchanged.

# V15 Update — all25 unchanged Gen04 local branches

Source: MAIN-15 admitted principal only, native EPUB SHA256 `ceae1226aa01421185231c837f542c430bd289489b73276b7086bb3c216ba005`. Root accepts this additive V15-local evidence through the V15 receiving review. Retained producer/candidate pending phrases describe their authorship boundary; publication and tranche adjudication remain separate. All prior ledger bytes, Gen04 originals and adverse histories stay exact. The V15 deep reading section13 routes every major claim family to H1–H4, shown/dialogue/report/inference access, qualitative confidence and governed claim transition. Apply those weights together with each row’s finer source/uncertainty limits; actual threat, refusal, pain and failed components are not erased by gag classification.

## Complete local branch records

Every Gen04 statement remains the exact prospective commitment frozen after V12. Its original25 Outcome and25 Adjudication fields remain blank; the following are new V15-local records in a postexchange receiving proposal. V13-local K03, V14-local A02 and historical Gen03-K04 falsifications remain unchanged. A single local contrary direction is distinguished from repeated-pattern or whole-tranche retirement. The initial producer memo and every postexchange field delta remain preserved. Root must still accept or revise these proposals through an attributable receiving successor; no consensus or volume acceptance is implied.

The record below retains every branch, primary chronology, strongest contrary or adjacent candidate, missing conjunct and failure diagnosis. It includes the generous pragmatic-request reading for K02, completed-revenge reconciliation for K03, assignment/challenge/inhibition alternatives for A02, state-specific agency for K04, prior recovery planning for M03, and feasible return/recruiter benefit for E02. No added personal-cost floor, physical-harm-only condition, goal-completion exemption, universal external-assigner condition or named-spell-debate prerequisite governs the old forecasts.

| ID | Initial producer | V8 proposal |
|---|---|---|
| MG04-K01 | PARTIAL | CONFIRMED |
| MG04-K02 | NOT_TESTED | PARTIAL |
| MG04-K03 | CONFIRMED | FALSIFIED |
| MG04-K04 | PARTIAL | PARTIAL |
| MG04-A01 | PARTIAL | PARTIAL |
| MG04-A02 | PARTIAL | AMBIGUOUS |
| MG04-A03 | NOT_TESTED | NOT_TESTED |
| MG04-A04 | NOT_TESTED | NOT_TESTED |
| MG04-M01 | NOT_TESTED | NOT_TESTED |
| MG04-M02 | NOT_TESTED | NOT_TESTED |
| MG04-M03 | NOT_TESTED | NOT_TESTED |
| MG04-M04 | NOT_TESTED | NOT_TESTED |
| MG04-M05 | NOT_TESTED | NOT_TESTED |
| MG04-M06 | NOT_TESTED | NOT_TESTED |
| MG04-D01 | CONFIRMED | CONFIRMED |
| MG04-D02 | PARTIAL | PARTIAL |
| MG04-D03 | NOT_TESTED | NOT_TESTED |
| MG04-E01 | PARTIAL | PARTIAL |
| MG04-E02 | NOT_TESTED | NOT_TESTED |
| MG04-J01 | PARTIAL | PARTIAL |
| MG04-J02 | PARTIAL | PARTIAL |
| MG04-Y01 | CONFIRMED | CONFIRMED |
| MG04-CE01 | NOT_TESTED | NOT_TESTED |
| MG04-I01 | NOT_TESTED | NOT_TESTED |
| MG04-I02 | NOT_TESTED | NOT_TESTED |

### MG04-K01 — CONFIRMED

- **indirect_search:** Supported by the benefit/control-rule investigation and asymmetric level-reset solution.
- **exact_capability_based_revision:** Supported at a bounded level: actual indirect-coffee harm at C2P0203–0206 invalidates the indirect-injury assumption, he explicitly generalizes reflection at210–211 and declines the contemplated explosive-potion method212. The observed change is withdrawal/restriction of that method, not proof every subsequent anecdote was invented after this test.
- **fitted_delegation:** Supported for explicit buff/heal/police/crowd assignments; distinguish assigned actions from the later reported treatment and arrest.
- **recovery_and_ethics:** Recovery preparation is present in C1, but Kazuma’s later death, lost levels, incomplete target inhibition and coercive exposure remain actual costs and failures of broader sufficiency.

**C1P0395–0401,0412–0452,0478–0505; C2P0037–0038:** Before action, Kazuma rejects an unverified curse-removal gamble and doubts ordinary Bind against a dark priest. Serena then supplies a bounded solo-interference exception. He requests support and assigns healing, police transport and crowd management before attacking. His anticipated reflected injury occurs; the next chapter reports recovery/treatment and arrest. This is fitted preparation, not a safe or ethically adequate plan merely because he is revived/healed.

**C2P0203–0212,0315–0356,0602–0638:** The cup attack causes actual shared burns C2P0203–0205 and Kazuma calls it another failure206. He explicitly learns indirect injury also reflects210–211 and states that otherwise he would have bought explosive potions212, then relocates214. This supplies a real new constraint and withdrawal of that route, without claiming an earlier executed bombing or a firm purchase intention. The later loan maneuver fails to retrieve Vanir’s contract, while money taken from a follower and renewed favor supply observed rule transitions. C2P0630–0638 remains his inference.

**C3P0484–0520,0530–0548; C4P0017–0021,0156–0161:** He rejects direct and indirect killing, faces the inadequacy of simply releasing Serena, and uses a carried level-reset potion against the unequal costs of the same reset. He anticipates his own loss before acting, warns Darkness against lethal assault, but fails to inhibit Serena’s restored Death capability in time. Actual resetting and intelligence handoff are later established; his solo claim does not erase others’ capture, cure, revival and restraint.

**Contrary/adjacent evidence:** The many correct plans are not evidence that every first plan adapts successfully. C2P0608 is a failed contract maneuver; C3P0543–0548 exposes a newly restored enemy capability before Kazuma and Darkness can stop it. C4P0017 reports outside recovery. These remain adverse to a general complete-planner claim even while supporting indirect construction.

**Missing conjunctions and scope:** The relevant capability-based revision is the actual restriction of the indirect-injury route after invalidating feedback, including rejection of an explosive extension. No firm earlier purchase plan or exact date for every prank is invented. Search and fitted delegation are independently observed; performed buffs differ from inferred unconscious treatment and unshown assigned handoffs.

**Diagnosis:** CONFIRMED for bounded local search/revision/delegation, revising the initial PARTIAL after root and semantic attention to the explicit C2P0210–0212 limitation. Recovery/ethical failure and Serena’s restored-power attack remain; this is not a complete-planner claim.


### MG04-K02 — PARTIAL

- **trusted_concrete_request_before_help:** Explicit King requests exist, and Aqua’s C1P0468 question can pragmatically request particular reassurance. No grammatical imperative or request naming combat is required. Whether that question entrusts a concrete preventable-harm responsibility rather than asks for an appraisal remains the strongest local eligibility uncertainty.
- **actual_substantive_help:** Strong adjacent evidence exists, including costly intervention and care; it does not manufacture its initiating request.

**C1P0374–0392,0427–0479,0486–0505:** Familiarity, Aqua’s visible exclusion, Megumin’s trust, Darkness’s permission and Aqua’s question about being needed precede Kazuma’s costly intervention. Aqua asks whether she is an unnecessary goddess. This can pragmatically request concrete reassurance/support; no named protective act or grammatical imperative is required. Kazuma’s meaningful buff assignment and intervention support the generous request/emotional-harm reading, while the exact entrusted responsibility and refusal consequence remain uncertain.

**FP0175–0180,0183–0201,0311–0324:** He independently brings food after learning Aqua has withdrawn and later considers limited ways to help her return. Her small wish to go home is explicitly not directed at him or a demand at313–314. There is a feasible meal/limited planning contribution, but no source-established concrete request before either choice.

**EpP0047–0065; FP0324:** Her letter states a dangerous goal; Kazuma stands, then jumps from bed intending immediate pursuit before the erased request is discovered at62. The earlier explicit risk of bodily annihilation makes danger real. The erased “please find me” is a concrete trusted-person request, but is learned after the stated help decision. The source closes without showing a subsequent search execution.

**Contrary/adjacent evidence:** C1P0468 is a trusted direct self-worth question after visible exclusion, so it must be assessed as a possible concrete request for reassurance/support, not rejected solely because it does not say “fight Serena.” Kazuma immediately entrusts meaningful support to her and accepts reflected injury; on a pragmatic request/emotional-harm reading this supports the forecast. The exact entrusted harm-prevention task and refusal consequence remain partly inferred. Explicit King/leveling requests C4P0152/0168/0185/0206–0220 and FP0031 are also real: his refusals/comfort preference remain contrary if the particular-person preventable-harm conjunction is judged complete. Feasible contacts/indirect help cannot be denied merely because he cannot win a solo duel.

**Missing conjunctions and scope:** The forecast has no physical-harm-only rule, costly-help minimum, grammatical-imperative requirement or demand that the request specify the tactic used. Strongest generous reading: C1P0468 requests reassurance about valued standing, refusal leaves ongoing emotional injury, and Kazuma’s fitted support request plus intervention supplies substantive help. Strongest limiting reading: the source establishes a concrete appraisal question but no unambiguous entrusted protective responsibility/refusal consequence. Later explicit King requests establish a request and systemic danger, but particular-person harm under refusing this contribution is still uncertain. FP0313–0314 explicitly undirected wish and EpP0062 after-decision timing remain exact limits.

**Diagnosis:** PARTIAL proposal, changing the initial NOT_TESTED because that text understated the genuine pragmatic request/emotional-harm candidate and the explicit King requests. No clean abandonment failure is asserted, and no forced full confirmation follows. Root should adjudicate this literal eligibility dispute with both readings visible.


### MG04-K03 — FALSIFIED

- **ordered_payback_expansion:** One bounded diary sequence supplies a newly learned grievance, visibly active payback accounting and an actual next act accepting known reflected pain.
- **success_and_retirement_limits:** Other successes do not automatically qualify; strongest unchanged-scope candidates are retained with their exact salience limits.
- **historical_adverse:** V13 MG04-K03 FALSIFIED remains unchanged; this local positive does not cancel it.
- **local_contrary_direction:** C2P0705–0733 supplies concrete apparent success, explicit privately active revenge satisfaction and actual scope contraction/reconciliation. Retain as a single local contrary direction, not whole-tranche retirement.

**C1P0412,0497–0505 → C2P0700–0733:** Prior selected scope is personally obstructing Serena/countering her treatment of Aqua, with a declared tomorrow interference campaign. AtC2P0705 Serena acknowledges underestimating him and announces abandoning the town. Kazuma explicitly says settling peacefully suits him714 and privately acknowledges revenge for Aqua is in a sense complete715, before asking for reconciliation724, accepting promised withdrawal725–727 and canceling mutual debts733. Reward salience is independent and before the contraction; unchanged scope cannot be converted into missing reward. Goal completion is not an added exemption. Wiz is already scorched700 and the fight continues707, so the original known-person-harm/severe-danger modifier is a genuine competing account fixed before the decision. His expressed private appraisal nevertheless stresses completed revenge and relief, not an explicitly adopted new rescue objective.

**C1P0033/0047–0051 → P0073–0077 → P0080–0091:** An initially wary/polite baseline changes after Serena credits him with the army’s losses: visible pride75 and the private “I have become that important”76 precede gloating77. This is bounded verbal/taunting expansion. The new alarming recruitment explanation begins80 and cannot be moved before77 to exempt the response. Existing risk and later caution still limit generality.

**C3P0034–0049:** Before the new robot revelation, Serena’s punch already establishes the same-site injury reflection at35–37. Kazuma then learns her responsibility for the robot rampage at44–45, explicitly construes it as harm caused to him and a large debt at46–47, and chooses a compensatory punch at48. Both crouch in pain at49. The next accepted personal exposure expands from the prior compensation regime to a retaliatory blow despite known feedback. The manageable grievance opportunity and payback appraisal are explicit before that choice; no post-act emotion is used to invent them.

**C2P0264–0288,0297–0356:** He continues preparing harassment after seeing Serena weaken, then meets a new explicit lethal threat and numerical disadvantage at285–309. The improvised exposure tactic and public call are real escalation. However, the original obstruction campaign already includes escalation and the new grave threat is independently present; this is not an unqualified clean reward-only test.

**C3P0532–0548; C4P0158–0165,0271–0277:** At532 he already plans a comfortable slow rebuild. Serena’s “most dangerous” recognition at535 is followed by his overestimate/retirement reply537; Death becomes explicit only later543, so it cannot retrospectively excuse the earlier unchanged scope. However, concrete personal enjoyment of that recognition is not independently established before537. Likewise he rejects extrapolating successive wins into a King campaign atC4P277 while Megumin and Darkness are excited. Their reward salience is not automatically his.

**Contrary/adjacent evidence:** The initial producer memo omitted the strongest unchanged-scope case C2P0705–0733; that omission is now explicitly repaired after root’s independently recorded question and a direct primary reread. Kazuma acknowledges completed revenge before choosing settlement, under concrete apparent victory feedback. C2P0700’s already observed harm to Wiz and ongoing conflict remain the strongest original-modifier counterreading; they are neither ignored nor treated as automatic erasure when his stated next-choice reasons are relief and completion. C3P0535–0537 retirement remains another candidate with uncertain active personal reward; later Death cannot retroactively supply its danger cue.

**Missing conjunctions and scope:** The C2 matched candidate has independent reward salience and a clear next contraction. The original modifier is present as competing context; whether it causally accounts for caution is underdetermined. This FALSIFIED proposal records the adverse local direction without claiming a repeated unmodified pattern or retiring the whole tendency. Positive C1 gloating and C3 robot-payback choices remain separate and cannot cancel it; V13 local F remains unchanged. The original known-person-harm/danger modifier does not require an expressly adopted new rescue goal; lack of such a declaration does not erase the already observed modifier.

**Diagnosis:** FALSIFIED, scoped to a single local contrary direction. Changed from initial CONFIRMED because a previously omitted source-established reward → reconciliation sequence is load-bearing. No net-vote treatment, goal-completion exemption or adverse-history deletion; root may retain modifier uncertainty in final adjudication rather than force a whole-tranche rejection.


### MG04-K04 — PARTIAL

- **quiet_A:** NOT_TESTED: no single new case combines an offered attractive substitute, already acknowledged particular commitment, explicit low/reduced immediate appetite, and the actual choice.
- **aroused_B:** PARTIAL/agency-qualified candidate, not a clean complete-conjunction confirmation. The prior compensation/legality account and explicit excitement are real, but knowledge of an effective feasible stop under actual moral-restraint removal remains uncertain. The original forecast does not require a normal state; the unresolved ingredient is known effective stop/agency at the scored choice.
- **noticed_tears:** Continuations and exploitation of tears remain adverse to any broader automatic brake; original Gen03-K04 FALSIFIED stays exact.

**C3P0010–0023,0034–0040; C2P0813–0815,0892–0897:** The diary order supplies a pre-existing service/compensation role. Kazuma himself elects an erotic appendix: at11–15 he establishes a payment and labels prospective harassment “legal”; excitement is explicit at16, before Serena’s refusal21. His next response22 demands a large price for stopping, and he savors her nearly crying face23. The obscene appendix is his own optional addition rather than a compelled literal diary requirement, supplying a feasible stop. Previous payment rules also give him a known possible control-release route, which he deliberately avoids. The helper/debt account is already available before this continuation; it is not inferred solely from an excuse afterward.

**C2P0846,0914–0929,0937–0955:** His earlier unsolicited breast-support offer is rejected at846; he later initiates and continues groping before her hand removes his at921. He supplies the debt-preservation account at928 and cites the earlier discarded-morals order at946 after a new shared-room objection945. The enacted soft-breast gratification is explicit919; however, the most direct price/exculpation wording at928 follows the shown groping continuation. These are strong boundary violations without pretending every B chronology is fully established.

**C3P0061–0065,0263–0286,0464–0466; EpP0004–0018:** He exploits remembered companions as leverage until Serena actually cries64, resists a task she wants even with pain263, and she later runs with flowing tears286. In Ep he is already awake, initiates a hug, performs sleep before Darkness’s protest, and falsely blames her afterward. The sleep frame is prior to the protest, but immediate arousal/intimate reward is not separately explicit enough to infer the whole B conjunction merely from hugging. Later cessation of her resistance does not retroactively consent to the initial act. His post-cure demand for more hugging464 ends when Megumin peels him away466; it does not prove autonomous restraint.

**Contrary/adjacent evidence:** C1P0122–0124 contains a tempting offer and refusal but visible fidgeting, not explicit reduced appetite. C4P0046–0050 is Kazuma’s own flirtation with Eris, her correction and an explicit denial of his jealousy theory; it is not an attractive substitute offered to him. FP0355–0357 immediate rejection of Aqua’s sexual warning neither supplies an offered substitute nor the full commitment/low-arousal conjunction.

**Missing conjunctions and scope:** No universal altered-state exclusion is added: actual chosen tariff-writing, selective refusal and painful resistance show surviving initiative. However, optional literary content alone does not prove he knows an efficacious stop for the relevant disinhibited urge. Control-release payment efficacy is explicitly disputed atC2P0892–0898; the cure is discarded, and C3P0404 states lack of self-control. The strongest B candidates therefore preserve known/unknown agency rather than treating ordinary free choice as established. No clean A, no clean autonomous contrary B, and no restored Gen03 tear brake.

**Diagnosis:** PARTIAL, with initial B support reduced to a literal/agency-qualified candidate after independent source-only reviews. Existing harassment and actual-tear continuations remain acts regardless of the narrower test. C3P0064→0066,0105→0106–0107 and0161/0177–0181 strengthen the broad adverse record; C4P0441 shows satisfaction at having made Aqua cry, not a newly shown continuation after a separate noticed-tear cue.


### MG04-A01 — PARTIAL

- **capacity:** Supported in bounded engaged purification, support and resurrection tasks.
- **readiness:** Variable and separately observed; access blocked, sleep/distraction, unknown item function and self-selected withdrawal are not domain incapacity.
- **comparative_goal_clarity:** NOT_TESTED as a clean matched causal comparison with domain/access/resources and relevant knowledge held sufficiently comparable.

**C1P0310–0315,0478–0479; C2P0515,0547,0675–0677:** Aqua approaches an injured patient but is blocked before casting; no failed Aqua healing is shown. Support magic is actually supplied before Kazuma’s dropkick and later in the chase, with Serena recognizing its quality547. She actually converts potions to water676, carrying enough divine force to sting Wiz677; the destructive system effect is not a purification failure.

**C3P0390–0443; C4P0017,0053,0129–0140:** The special antidote is an external supplied item, not proof of Aqua’s intrinsic anti-puppet spell mastery. Her catching and pouring it after changed restraint is real restoration work. Eris reports actual resurrection work atC4P0017; revival is shown atP0124. C2P0038’s earlier unconscious healing remains Kazuma’s inference. No root or reviewer observation route for Eris is invented.

**C4P0209–0223; FP0035–0053:** Aqua proposes bounded barrier work and distinguishes remaining maintainer counts from her own capacity, with Kazuma correcting headcount. These are plans/capacity claims, not actual barrier removal in this volume. No invented spell execution is counted.

**Contrary/adjacent evidence:** Purification removes nearly all available cure stock and burns/stings the friendly lich. C3’s bottle transfer includes a catch/face-orientation difficulty, not unerring handling. Her embarrassment/withdrawal FP175–208 and low-confidence admission183 remain readiness/goal evidence. None can be erased by successful resurrection.

**Missing conjunctions and scope:** The comparative clarity branch lacks a matched clear versus unclear arrangement with sufficient independent controls. Earlier not knowing the potion function and later learning it changes relevant knowledge as well as alignment. Capacity, required-time readiness and comparative clarity remain three different results.

**Diagnosis:** PARTIAL for the compound: engaged established-domain ability is supported; practical system anticipation and guaranteed activation are not. No undefined curse or failed uncast spell is invented.


### MG04-A02 — AMBIGUOUS

- **prestige_response:** Direct challenge → rival-directed escalation is observed.
- **ongoing_assignment_displacement:** C2 escape has paused while a self-selected water service is completed; neither a completed water act nor an unassigned stock-preservation rule automatically supplies the required ongoing task. The wider escape reading remains possible, not established merely from the fight.
- **historical_adverse:** V14 A02 FALSIFIED for its scoped single local direction remains unchanged; no favorable V15 act cancels it.
- **local_contrary_candidate:** FP0119–0129: self-adopted purify-Wiz/return goal, direct rival provocation, actual ignoring of Vanir and continued original purpose. Whether the violent-goddess provocation is the exact divinity/superiority/public-recognition trigger and whether bodily interposition/cost warning inhibit the distinct contest remain explicit disputed predicates.

**FP0119–0129,0136–0168:** Before challenge Aqua explicitly adopts purifying Wiz as divine work at119–121. Her prior return-home objective and the last-officer/barrier reasoning are already established in C4P0176–0188 and FP0041–0060; the first express connection of killing this friend to her return, and her stated friend-killing pain, occurs at129 after the initial ignore128. Vanir interposes125, calls her a violent goddess, warns about repair cost126 and actively provokes127. Aqua expressly ignores him128 and continues addressing Wiz to accomplish the original task129. This is a real contrary direction under the self-adopted-assignment/direct-superiority-provocation reading. Interposition blocks access to Wiz, not obviously a prestige fight with Vanir standing in front of her; it must not be assumed to prevent all retaliation. She acknowledges friend-killing pain129, but that acknowledgment follows the initial ignore128 and cannot automatically be backdated. Later consent/trust/gaze/conscience and retreat are a distinct decision, not the earlier status outcome.

**C2P0515–0553,0564–0584,0675–0712:** Before the contest Aqua is fleeing alongside Kazuma, contributes support, and participates in attempted escape. The shopping pause does not itself prove the dangerous situation has safely ended. She then completes an independently visible hydration service for Wiz at676, before Vanir’s toilet-goddess insult689. Her response690 escalates mockery of his competence; the beam694/Reflect695 exchange continues into a sustained fight707/710–712; Wiz is seen scorched700 during that fight, while the exact causal route is Kazuma’s hedged attribution. Thus the wider practical escape/protection objective is displaced and real friendly costs follow; the already completed hydration act alone cannot be named an ongoing displaced assignment.

**FP0064–0081:** Mask-pulling is already underway before Kazuma tells her to stop so they can talk at71; she obeys72 and asks about Wiz73. Vanir disparages the gods74; she retorts76, partly self-deprecating, and Vanir proposes a fight77. Wiz’s arrival81 interrupts. The visible response is not a completed renewed Aqua attack; do not give Vanir’s challenge her agency.

**FP0119–0168,0183–0197:** Her attempted Wiz-purification plan has return-home stakes. Wiz’s trust/affection, Vanir’s contract concern and everyone’s gaze produce Aqua’s withdrawal. This is not an independently preceding direct prestige challenge and therefore does not by itself confirm or falsify A02.

**C1P0308–0350:** A patient names Aqua and she approaches; others block treatment before casting. After Serena’s treatment leaves residual wounds337, the patient rejects Aqua’s hand341–345 and she returns dejected350. If this is a direct public-recognition challenge to her service role, task-conserving/non-escalatory response is adverse; if a refusal of already externally blocked treatment, full trigger/access remains uncertain. No grave-risk exemption is manufactured from small residual wounds.

**Contrary/adjacent evidence:** Initial PARTIAL overstated the escape-to-fight interpretation while omitting FP0126–0129’s autonomous-looking persistence and C1’s rejected healer. These are now fully retained. A02 does not require an external assigner; self-adopted work is eligible on its actual merits. Conversely no one assigned stock preservation, Aqua says she did not know the proposed sale690, and prior “go home” was rejected before the fight. FP0074–0081 has a real challenge and relative reply, but Vanir’s duel invitation and Wiz’s arrival do not show Aqua completing a new attack or autonomously restoring the task.

**Missing conjunctions and scope:** Assignment/constraint, exact status-challenge subtype and inhibition versus autonomous persistence remain consequential to whether FP0128 is a full adverse test and whether C2 has a positive displacement. These are genuine eligibility disputes, not an exemption because the outcome is contrary or because a self-chosen goal lacks an external director. New source qualifies the causal route of scorched Wiz atC2P0700 as Kazuma’s inference during an actual fight.

**Diagnosis:** AMBIGUOUS local proposal: strongest full-reading countercase explicitly preserved, with exact trigger/inhibition uncertainty. If root accepts FP0126 as a full direct superiority/divinity challenge without preventing inhibition, the local direction should be FALSIFIED with single-case scope; if not, it remains a documented adjacent adverse case rather than a hidden exception. V14 scoped F is immutable either way.


### MG04-A03 — NOT_TESTED

- **actual_useful_service:** Multiple useful acts occur, including support, resurrection and the antidote delivery.
- **recognition_before_two_new_same_service_opportunities:** Not established.
- **voluntary_ownership:** Shown locally in care/service but not enough to supply the missing temporal series.

**C1P0478–0486; C2P0515,0676–0677; C4P0017:** Buffing, hydration, revival and item delivery are different services at different needs. Wiz thanks Aqua after the water conversion, but at least two separately identified further opportunities for that same useful output with aligned recognition/resources are not shown afterward.

**C3P0333–0340,0410–0443; FP0120–0168:** The gift’s sentimental value and service initiative are real, and Wiz’s extended trust is explicit. A gifted item, one cure sequence, several steps within one service, or friendship praise is not work-specific acknowledgment followed by two further same-service opportunities.

**Contrary/adjacent evidence:** Later embarrassment, withdrawal and eating alone cannot falsify this forecast without the required recognition-before-two-opportunities structure. Equally, multiple spells across the novel cannot be pooled into one invented owned repetition series.

**Missing conjunctions and scope:** The complete temporal conjunction is absent: same service, actual work-specific acknowledgment first, then two distinct renewed opportunities with need/resources/alignment still available. A long offstage interval does not fill it.

**Diagnosis:** NOT_TESTED; persistent care and recognition causality remain different propositions. Ownership, affection and material rewards remain rival sustainers, not uniquely identified causes.


### MG04-A04 — NOT_TESTED

- **low_valued_repetitive_maintenance:** Not independently combined with a concrete maximal shortcut.
- **shortcut_and_secondary_system:** Actual purification has secondary costs, but does not establish the low-valued maintenance antecedent.

**PrP0007–0044; C2P0675–0677:** The pet cascade and stock purification are actual source events. Hydrating Wiz by turning potions into water is a chosen service with an ignored product/holy-power consequence, not source-established repetitive maintenance she finds tedious.

**C4P0441–0444; FP0029–0060:** Darkness does the robe laundry; Aqua bathes. Seeking a one-off purification shortcut to the King’s barrier problem is a campaign solution, not routine maintenance. Neither should be relabeled to fit A04.

**Contrary/adjacent evidence:** Spectacular purification and bad downstream anticipation support nearby mechanisms, but mere power or speed does not meet the frozen antecedent. No count of unshown chores or assumed boredom is supplied.

**Missing conjunctions and scope:** Missing low-valued repeated maintenance plus concretely available attractive high-output shortcut and absence of a salient learned/external constraint before choice.

**Diagnosis:** NOT_TESTED; retain the actual damaging simplification without claiming the specific maintenance mechanism has gained validation.


### MG04-M01 — NOT_TESTED

- **specialty_identity:** Strong adjacent general-specialist/status defense, but no clean explicit denigration/replacement/imitation of Explosion by a rival before her response.
- **ordinary_companion_cost_priority:** Known ordinary communication cost is directly established atC4P0476 before the later actual destruction498–501. That cost branch is real for the second choice; the literal specialty trigger remains disputed. The first paper-plane disposal475 occurred before the stated shared-recipient need.

**C4P0467–0478,0492–0520:** The recall letter ranks Yunyun first-team and Megumin reserve; Yunyun explains the lack of advanced magic474. Megumin turns the letter into a plane475 before Yunyun states the need to show others476. She later fires toward its resting area498–501 despite already knowing that circulation requirement, boasts her first-team worth506, offers Yunyun excuses509, and flinches at Kazuma’s reserve-motive accusation517–520.

**Contrary/adjacent evidence:** C4’s roster explicitly lists reserve; Yunyun, not the document, hedgedly infers lack of advanced magic as the reason. This clearly threatens standing. The literal question is whether this explicitly denigrates/replaces/imitates Explosion in a way Megumin treats as her specialist-identity challenge. No universal requirement for a named rival spell, formal equivalence debate or explicit legitimacy argument is added. Her response and known document-sharing cost cannot alone invent the missing antecedent; they remain real identity/care evidence.

**Missing conjunctions and scope:** The uncertain/missing item is the literal denigration/replacement/imitation of Explosion, not an added demand for a named rival spell. First disposal475 precedes the explicit shared-document need476; actual destruction498–501 follows known cost and Yunyun’s civic dilemma492. Her broad specialist pride and mixed help do not erase either timing.

**Diagnosis:** NOT_TESTED proposal for the exact original trigger; source-supported general identity defense remains adjacent. A generous reading that reserve selection replaces her chosen spell with advanced-magic users must remain available for root receiving, while general role-fit criticism cannot automatically become explicit Explosion denigration.


### MG04-M02 — NOT_TESTED

- **self_accepted_material_build_burden:** Not shown.
- **reconsideration:** No serious plan to change/abandon exclusivity is shown.

**C4P0473–0478,0504–0520; C2P0264:** Reserve ranking and lack of advanced magic are external comparisons. Megumin answers with display and status defense, not an expressed internal conclusion that the exclusive build materially prevents contribution to valued companions. Daily upward casts/arrests are reports, not her contribution-guilt acknowledgment.

**Contrary/adjacent evidence:** The lack of compromise after outside criticism is not disconfirmation until the internally accepted substantial build-burden trigger exists. Romantic care, other practical skills and a general “poor magician” appraisal would not supply it either.

**Missing conjunctions and scope:** Missing her own substantial self-attributed contribution failure and consequent build/role deliberation; no inference from an opponent’s ranking.

**Diagnosis:** NOT_TESTED; do not convert reluctance to compromise under a different trigger into a failed guilt inversion.


### MG04-M03 — NOT_TESTED

- **raw_execution:** Actual forest Explosion destroys the letter’s area.
- **complete_prepared_artillery_conjunction:** Not established before casting.

**C4P0494–0506; C2P0264:** The forest spell is technically effective and a stationary letter is an actual object target; no separate universal tactical-mission requirement is added. The prior friendly geometry, resource allocation and post-cast exit/carry plan are not independently fixed. Kazuma supports her and supplies mana only after she starts collapsing505; actual assistance does not prove a prior recovery plan. The daily upward-cast/arrest report likewise lacks the full prepared conjunction.

**Contrary/adjacent evidence:** Success is not evidence that all safety/resource/exit conditions had already been planned. The paper target may be stationary, but immobility alone cannot fill the other conjuncts.

**Missing conjunctions and scope:** Missing independently established prior safe-friendly geometry, adequate planned resources and exit/carry plan. These literal missing conjuncts suffice; no universal additional tactical-mission prerequisite is imposed, and a stationary target alone cannot fill them.

**Diagnosis:** NOT_TESTED; preserve strong destruction/control evidence at its narrower scope.


### MG04-M04 — NOT_TESTED

- **valued_person_required_as_target:** No new Megumin firing task meets this condition.
- **pre_action_friction_and_aftermath:** No matched firing-choice sequence; therefore neither branch is confirmed.

**C3P0398–0443; C4P0017; FP0129–0168:** Megumin holds/cures Kazuma and later binds Serena/cares for Darkness in Eris’s report. These are contributions without a decisive-harm task against a person independently valued by Megumin. The Wiz purification conflict belongs to Aqua, not Megumin; it cannot be reassigned to validate M04.

**Contrary/adjacent evidence:** Affection and hesitation in other speakers are not a transfer test. Destroying a recall letter or an empty forest area does not make a valued person the target.

**Missing conjunctions and scope:** Missing source-established significant relationship to the required opponent/obstacle target and actual decisive-harm requirement, before pre-action/post-action branches can be scored.

**Diagnosis:** NOT_TESTED; no future/restricted narrative is used to complete the trigger.


### MG04-M05 — NOT_TESTED

- **known_grave_companion_harm:** No actual tactical Explosion choice explicitly combines this risk, her knowledge and feasible alternatives.
- **relational_friction:** Observed care elsewhere is adjacent, not a full test.

**C4P0494–0505; C3P0412–0443; FP0322:** The forest cast follows Kazuma’s attempted interruption and destroys the letter’s vicinity, but the source does not establish known grave bodily risk to a companion there. That is not the same as declaring it harmless. Her cure assistance is real care. Kazuma’s later proposed daily bombardment campaign is unexecuted and does not establish Megumin’s actual choice.

**Contrary/adjacent evidence:** Unknown geometry/severity remains unknown; no gag-based harmlessness assumption. Kazuma’s Death is Serena’s attack, not Megumin’s friendly-fire decision. A source-reported robot victory does not retroactively supply prior grave-risk knowledge or alternatives.

**Missing conjunctions and scope:** Missing source-explicit grave direct companion injury risk, Megumin’s prior knowledge, best tactical option and alternatives before the response.

**Diagnosis:** NOT_TESTED; retain actual uncertain collateral/communication harm without upgrading it to the precise grave bodily-harm prediction.


### MG04-M06 — NOT_TESTED

- **rewarding_repetition:** Reported repeated leisure casts exist.
- **weakening_instrumental_mission:** No complete sustained instrumental operation losing its goal as repeated firing rewards grow.

**C2P0264; C4P0271,0498–0506; FP0322:** Upward daily casts are leisure under house restrictions; the one forest display is one response to rank. Her “incomplete satisfaction” about earlier victories is a present claim, not a new repeatedly rewarded operation with a weakening original mission. The proposed daily King harassment is still only Kazuma’s future plan.

**Contrary/adjacent evidence:** Enjoyment of casting, destructive output and a desire for another occasion cannot alone establish the sustained instrumental drift conjunction.

**Missing conjunctions and scope:** Missing a repeated safe effective tactical operation, visible growth/equivalent reward and independently weakening original objective before an additional cast choice.

**Diagnosis:** NOT_TESTED; protect the distinction between specialty enjoyment and mission displacement.


### MG04-D01 — CONFIRMED

- **protective_interposition:** Directly supported before a threatened lethal spell.
- **bodily_institutional_cost:** Real costs include reflected pain, later loss of consciousness and legal/guarantor work.
- **finite_and_mixed:** Protective contribution does not erase injudicious choking, later pleasure-seeking assault or failed inhibition.

**C3P0341–0351,0355–0363:** Serena declares the negotiation over, targets Aqua and invokes Death. Darkness immediately steps in front of Aqua before the spell. Its failure is not proof Darkness could resist Death; the defensive act precedes that outcome. She then uses her body to immobilize Serena but learns that choking her also harms herself.

**C3P0498–0528,0543–0548; C4P0017:** She explicitly treats residents as her responsibility and offers lethal institutional protection; Kazuma redirects because the mass curse is dangerous. Her first reflected punch518 is a genuine cost, and later deliberate pinching528 adds pleasure-oriented abuse. When Kazuma is killed, Eris reports that her furious punch knocks both herself and Serena unconscious. Finite endurance and outside recovery remain.

**C1P0174,0493–0500; C2P0054–0085,0372–0375:** She gathers civic information, challenges violence before the dropkick, obtains legal release under a specific secrecy/leniency condition and later refuses repeated guarantor work. Responsibility is not obedience to all Kazuma methods or an unlimited institutional resource.

**Contrary/adjacent evidence:** Her later pinching to enjoy reflected pain is not itself protective merely because Serena is a captive enemy. It is retained as a failure of broad automatically duty-aligned restraint. The main clean protective test is her pre-Death interposition, not the later fantasy reward.

**Missing conjunctions and scope:** One observed protective action does not establish strategic sufficiency, safe recovery or universal prioritization. Actual grave threat to Aqua and feasible interposition are independently present before the outcome.

**Diagnosis:** CONFIRMED local defense direction with pleasure/errors/finite cost retained; no global protector label replaces the event sequence.


### MG04-D02 — PARTIAL

- **audience_privacy_A:** Source supports unwanted public/private meanings and objection, but a newly changed audience over an otherwise chosen bounded event plus independently prior matching preference is not fully isolated.
- **equal_standing_B:** NOT_TESTED: no new explicit matching equal-membership threat within the full specified setup.
- **broader_control_loss:** Mixed transfer evidence retained; not a forecast that loss of control is always aversive.

**C2P0054–0113:** Darkness chooses an institutional rescue; Kazuma imports private name and intimate-history claims into the officer’s presence. She corrects/stammers and protests his account, while his later interpretation that she is not angry is not her consent. The established legal/public role and earlier name objection help index dignity, but do not independently establish a prior rejection of this precise sexual audience condition over the otherwise sought bounded event of obtaining release; the original forecast does not require a fantasy.

**EpP0003–0018:** She enters to wake him; he is already awake and initiates a hug under fake sleep. She objects before ceasing resistance, and Megumin’s arrival creates accusation/exposure. His false “you attacked me” blame causes near tears and embarrassment. This initial hug was not an otherwise sought bounded event; later nonresistance cannot supply retrospective choice or prove a pre-existing audience preference.

**C3P0524–0528; C4P0274–0275:** She deliberately enjoys reflected pain, and imagines the King breaking armor. These actual welcomed meanings constrain broad aversion and are not discarded because pleasurable.

**Contrary/adjacent evidence:** Keep D02’s narrower independent-prior-boundary requirement. Direct protest after exposure cannot be its own evidence of the antecedent privacy preference. The three companions’ comments on altered Kazuma do not explicitly threaten Darkness’s equal membership; romantic accusation is not automatically expulsion.

**Missing conjunctions and scope:** Partial source support for meaning-sensitive objection. The otherwise sought bounded event can be institutional release, with no fantasy-only restriction; exact A prior-preference and changed-exposure matching remain limited and B lacks its standing threat. Do not infer chosen consent or general control aversion.

**Diagnosis:** PARTIAL for boundary transfer, not clean confirmation of either full branch. Historical Gen03 mixed agency and later enjoyed coercion remain exact.


### MG04-D03 — NOT_TESTED

- **concrete_incompatible_duties:** No genuine family/noble/civic duty versus continued party-membership incompatibility is established.
- **preservation_attempts:** Institutional labor and temporary role division are real but adjacent.

**C2P0054–0085,0372–0375; C4P0366–0392:** Legal guarantor work and an escort assignment consume effort, but she can perform them while remaining a member. Temporary escort or three-day delay is not loss of membership. The explicit next-chief recall dilemma later concerns Yunyun, not Darkness.

**Contrary/adjacent evidence:** Her choice not to become repeated guarantor after public teasing is a boundary/cost decision, not convenience abandonment of an independently incompatible family-party obligation.

**Missing conjunctions and scope:** Missing two independently established obligations with genuinely incompatible concrete demands on continued membership.

**Diagnosis:** NOT_TESTED; do not turn ordinary coexistence of duties into the frozen conflict.


### MG04-E01 — PARTIAL

- **A_deployment_improvement:** Supported most cleanly within the same cure after its method is already known: C3P0394 information → inadequate one-hand restraint414 and warning421 → Steal/throw425–433 → Aqua save434 → actual stillness order439, fuller Megumin hold440 and orientation instruction441 → successful application442–443. This is tighter than contrasting earlier uninformed bargaining with later knowledge.
- **B_alternative_provider_adequacy:** Bounded support for the restoration subproblem: Aqua, Megumin and Darkness supply actual capture/resource/holding/application without Kazuma directing. This is not adequacy for the entire strategic neutralization campaign.
- **C_Kazuma_dependence:** He does not direct his own cure; he later repairs the wider neutralization/disposition problem. The required comparable continuing-dependence comparison is incomplete.

**C3P0330–0349,0351–0363,0393–0443:** Initially Serena’s trade is refused and Aqua values the bottle without knowing its function. After capture and explanation, roles become explicit: Megumin restrains Kazuma, Aqua obtains/delivers the bottle and corrects his face before applying it. The first toss requires a sliding save; the hold continues despite Serena’s command. Real cure follows. Relevant knowledge changed as well as alignment, so no isolated organization-only effect is claimed.

**C3P0403–0404,0410–0443,0480–0548; C4P0017,0156–0161:** The alternative restoration arrangement is not led by Kazuma: while controlled he wants to help captive Serena. The three companions and Serena’s reluctant rule information supply the needed roles for this bounded cure. Afterward, mere restraint leaves disposition, mass-curse threat and restored enemy power unresolved; Kazuma selects reset and warns Darkness, yet Serena kills him before inhibition. Eris reports subsequent restraint/care/revival. No one participant supplies universal sufficient coordination.

**C1P0478–0486; C2P0037–0038; C4P0209–0230; FP0322:** Early explicit assignment fits familiar capacities but does not prove the entire recovery was preplanned or successful without costs. Later barrier/siege plans are proposed role/resource arrangements, not executed demonstrations.

**Contrary/adjacent evidence:** A full alternative for one serious multistage restoration problem must not be dismissed merely because a larger war remains; equally, success at one phase cannot certify adequacy for the whole Serena threat. The explicit two-level scope records both. The observed bottle handoff is imperfect but repaired; capture, cure, ethical disposition and safe withdrawal are separate outcomes.

**Missing conjunctions and scope:** Fix the immediate compared task before outcomes as getting the sole known antidote safely onto resistant Kazuma. Bounded non-Kazuma repair/provider adequacy and absence of his continuing direction are observed for that task. No sufficiently comparable whole-campaign provider comparison establishes all neutralization/recovery stages or broad continuing dependence. Earlier diagnosis changes remain a confound in the larger comparison; the within-cure restraint repair is more direct.

**Diagnosis:** PARTIAL compound. Preserve useful alignment, genuine non-Kazuma restoration agency and later coordination failures without claiming universal necessity or self-sufficiency.


### MG04-E02 — NOT_TESTED

- **attachment_cost:** Strong direct evidence of shock, household value, missing company and attempted contact preservation.
- **efficient_durable_feasible_reorganization:** Not fully established; return-home wish and King plan do not yet supply a feasible efficient arrangement.
- **practical_efficiency_benefit:** Explicitly present in the heaven-recruiter candidate C4P0176–0188: honest replacement recruitment is failing, and heaven wants effective Aqua back. This is not merely homesickness or romantic comfort.

**C4P0176–0188 → FP0192–0197,0220–0244,0318–0322 → EpP0047–0065:** Eris’s serious message is later transmitted in narration: the honest replacement cannot recruit effectively and heaven values Aqua’s return. That is a concrete functional staffing benefit. Heavenly return credibly risks sustained loss of the established household, while future visits remain uncertain. Kazuma’s separation anxiety, food visit, indirect Wiz question and mixed household fantasy show attachment cost. The route depends on defeating the King and has no demonstrated currently feasible safe implementation; her immediate trip is not by itself durable completed removal.

**C4P0279–0296; FP0186–0201,0235–0244,0288–0324; EpP0047–0065:** Kazuma is shocked at Aqua wanting to leave, wonders whether their tie is that light, brings food, raises future loss of Wiz/company, and is unsure whether she could revisit. In private he considers an appealing quieter two-woman household yet rejects its emotional emptiness, considers limited aid for her return, and reacts urgently to her departure letter. These are particular attachment costs with ordinary insults retained.

**Contrary/adjacent evidence:** The initial memo failed to state the explicit recruiter-efficiency benefit and is corrected here. It is factually wrong to say no meaningful functional reorganization or durable-loss candidate exists. On the generous reading that conditional heavenly job transfer counts as feasible, the observed contact-preserving concern supports the predicted attachment cost. On the stricter literal reading, defeating the King is an unproven prerequisite, so feasibility is not established. Kazuma’s quieter two-woman fantasy and old retirement preference remain real counter-preferences, not erased for unanimity.

**Missing conjunctions and scope:** The remaining disputed conjunct is feasibility of the proposed sustained reorganization, with credible later visit constraints also partly uncertain. Practical benefit is present. No completed separation is required by the forecast, but a proposed route whose central prerequisite is not shown feasible cannot silently become a feasible offer. This distinction, not mere noncompletion, supports localNT.

**Diagnosis:** NOT_TESTED retained, with a strong partial feature bundle and an explicit alternative generous support reading. Root should decide feasibility under the unchanged contract; no requirement of actual completed relocation or blanket no-attachment inference is introduced.


### MG04-J01 — PARTIAL

- **fixed_scope:** All95 exact original records evaluated, comprising85 primary-four and10 auxiliary, with190 fixed before/after arrays and66 overlap presentation groups, not independent trials.
- **supported_and_adverse:** The original producer full95 file was sealed before any comparison. Both original complete assignment sets have now been compared and paired receiving has occurred; literal forms, glosses, functions, adverse/sparse/already-active/mapping-limited results and disagreements all remain visible. No consensus or V15 acceptance follows.
- **new_tactical_care:** Care already active in several baselines; urgent/intensified care cannot be promoted to new onset.

**C1P0468–0486; C2P0531–0542; FP0175–0201,0328–0356:** Kazuma’s concrete tactical commands and quiet offers/self-disclosure are distinguishable, but fixed baselines independently constrain onset. His original QUIET mapping is not replaced by urgent care merely because a command appears. The food-care record with an earlier greed baseline differs from an overlapping record whose baseline already contains care.

**C4P0473–0520; FP0035–0038,0073–0077; C2P0689–0712:** Megumin’s rank challenge supplies competitive stance without an extra explicit spell-equivalence subtype. Aqua’s limited ability admission and rival-directed insults constrain a blanket self-legitimation mapping. Formal direction and observed role do not collapse into a universal loud/polite character style.

**C4P0279–0296:** Original IV15-20’s no-speech shorthand is factually qualified:279 contains a quoted private Kazuma mutter, followed by inner thought. It supplies no comparable companion-directed care speech. Original window and mapping remain unchanged; external qualification is stored in the sealed voice assignment.

**Contrary/adjacent evidence:** Some mappings have opposing or insufficient evidence; a supported record cannot hide another. The initial full assignment remains immutable. The current complete paired95 presentation preserves both original labels/rationales, including the IV15-24 relative-self-legitimation dispute and scope differences over already-active roles, dignity and sparse speech. J01’s independently evidenced dignity threat does not universally require D02’s separate otherwise-sought-event/prior-privacy conjunction. The independent reader’s stronger privacy qualifications remain attributable reasoning, not an added universal J01 condition. No acoustic, actor, accent, catchphrase-frequency or human-review claim is made.

**Missing conjunctions and scope:** The fixed windows overlap and are unequal. Both reader lineages share native source and uncoded reconciliation with disclosed factual QA; separate assignment is not fully blind or statistically independent. Full paired receiving has now occurred, while whole V15 acceptance and the separate tranche adjudication remain pending. Sparse/adjacent/active-role comparisons are not promoted into full tests.

**Diagnosis:** PARTIAL compound, preserving all adverse/form-limited comparisons. Any later source correction or re-evaluation must be externally attributable, not overwrite original assignments.


### MG04-J02 — PARTIAL

- **local_census:** Complete source-first fixed150-unit local contribution, including all36 soft-touched units, independently assigned and sealed before other-reader code access.
- **local_bound:** The producer initial assignments and independent initial assignments both retain149 clear L0–L2 and one mixed whole-premise case U15-120. The current paired conservative group preserves those histories and all150 units. Exact fine-label strings agree on106; normalized common mixed intent yields107, leaving43 fine differences. No current clearL3, no forced fine consensus. The conservative lower bound149/150 exceeds one half even assigning the mixed unit toL3.
- **tranche:** The frozen forecast concerns completed pooled V13–V15 principal census work. V15 complete paired receiving has now occurred; whole-volume acceptance/publication and the separate explicit tranche pool/adversarial closeout remain pending.

**Fixed U15-001–U15-150, accepted boundaries SHA8170abee32eafc398e49d6ac410feef43c7bc52c66444caa7665ab87f045f16d:** All original151 producer and138 independent discoveries survive through the accepted150-unit boundary union and source/lineage operations. Whole-premise assignments were made only after the root freeze; short verbal/narratorial episodes and culture/nested-form/eligibility uncertainties remain included. No unit was removed to improve the bound.

**Contrary/adjacent evidence:** U15-120 remains mixed and all36 soft-touched units remain in the governed150 denominator. Nested wordplay/script/culture do not automatically decide the whole unit. The now-known fine differences and both rationales are preserved, with106 literal or107 transparently normalized agreements rather than an invented final consensus. No boundary or original class has changed after outcomes.

**Missing conjunctions and scope:** The complete V15 paired table and conservative bound have been received, but a final accepted volume and explicit frozen three-volume pooling/tranche adjudication are separate. A complete local set is neither statistical calibration nor proof every joke survives translation. Original histories and every uncertainty survive.

**Diagnosis:** PARTIAL as a contribution to the still-unclosed whole forecast; this memo gives an explicit provisional local bound rather than incorrectly claiming incomplete source coverage.


### MG04-Y01 — CONFIRMED

- **real_inclusion:** Concrete recruitment by a trusted companion, not a hypothetical mention.
- **suitable_actual_role:** Actual Invisibility supplied; proposed Silent use kept separate.
- **later_duty_conflict:** Royal/village recall conflict is not retroactively a failed earlier spell or an observed final stay decision.

**C2P0217–0243,0259:** Kazuma appeals to Yunyun as the one person who can help; she accepts eagerly and actually provides Invisibility232–235. Silent is then named as the next desired task236–237 but its separate casting is not explicitly shown. Her anxious wish that no one be told is followed by narrated comforting and resource arrangements; he performs the overnight freezing himself.

**C4P0449–0467,0483–0512:** She brings a real defense recall letter and confirms a wish to protect town friends while acknowledging next-chief duty. Megumin’s incipient “together” invitation is interrupted by rank reading; later letter destruction and excuses do not show a final decision, completed duty release, departure or defense performance. The mixed pleased/uneasy reaction is real, with Kazuma’s cause inference labeled.

**Contrary/adjacent evidence:** The recruitment may exploit loneliness and is not ethical endorsement. Objections to criminality/secrecy and the later duty conflict remain; belonging desire does not equal agreement with every group method.

**Missing conjunctions and scope:** Only the directly shown Invisibility role is a full technical participation result. Neither Silent nor town defense execution is invented. The later incompatible obligation is documented context, not used after the fact to erase actual poor performance because no such failure is shown.

**Diagnosis:** CONFIRMED bounded inclusion/competent-participation direction; not a completed comprehensive secondary-character model.


### MG04-CE01 — NOT_TESTED

- **actual_service:** Eris gives direct afterlife reassurance and reports ground aftermath; these are bounded acts.
- **cumulative_burden_beyond_expressed_preference:** Not established.
- **self_set_boundary:** Actual refusal of a repeated maid greeting is retained, but is not the full public over-compliance context.

**C4P0006–0018,0042–0050,0057–0064,0122:** Eris playfully greets Kazuma, refuses his repetition request14, reassures him and encourages return. The direct interaction is shown; the ground rescue details are her report. There is no accumulation of sincere public-service requests beyond a burden she expresses while a feasible exit is available.

**Contrary/adjacent evidence:** Her timely “I will not do it again” is genuine self-limitation and must never be relabeled confirmation of over-compliance. Here its domain is a casual play request, so it is adjacent adverse evidence to a broad no-boundaries account rather than a complete CE01 failure.

**Missing conjunctions and scope:** Missing cumulative public/divine-service requests, her own expressed preferred load being exceeded, and the refusal/exit comparison.

**Diagnosis:** NOT_TESTED. No unobserved fatigue, private Eris motive or omniscient observation route is supplied.


### MG04-I01 — NOT_TESTED

- **direct_new_setting_contrast:** Absent.
- **reported_importance:** Letters, memory reports and Kazuma’s faith in Iris’s power retain report/claim authority.

**C2P0435–0447; C4P0366–0374; FP0041–0048:** Claire/Rain guarantee and the thank-you-letter report concern restored memory and royal relationships; Iris herself is not shown interacting in matched constrained/public and safer nondeferential settings. The future defense/escort campaign and “strongest sister” claim supply no current direct contrast.

**Contrary/adjacent evidence:** A letter alone cannot prove ordinary agency expansion, and a possibly edited/restored memory report cannot reopen an earlier utterance or tears as a new witness.

**Missing conjunctions and scope:** Missing a new directly shown comparable constrained versus safe nondeferential interaction with available ordinary choices.

**Diagnosis:** NOT_TESTED; preserve older positive tests at their original volumes and authority without creating new V15 evidence.


### MG04-I02 — NOT_TESTED

- **personal_wish_and_understood_conflicting_duty:** Not directly established together for Iris in the admitted source.
- **reduced_request:** No new shown Iris wish/duty narrowing decision.

**C2P0435–0447; C4P0366–0374; FP0041–0048:** Royal letters, escort/defense plans and Kazuma’s confidence in Iris are not an expressed personal wish plus an understood conflicting obligation. Yunyun’s explicit next-chief dilemma is another person’s event and cannot supply Iris’s missing antecedents.

**Contrary/adjacent evidence:** No hidden desire, unwanted obligation or narrowing motive is inferred from formal royal arrangements. A report of gratitude or invitation is not automatically a duty negotiation.

**Missing conjunctions and scope:** Missing source-direct Iris personal wish, her understood opposing royal duty, and a subsequent narrowed choice.

**Diagnosis:** NOT_TESTED; retain the V11 positive and earlier localNT histories unchanged.
