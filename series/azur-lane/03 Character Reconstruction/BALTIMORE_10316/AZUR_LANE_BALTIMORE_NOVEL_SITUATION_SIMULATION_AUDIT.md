---
series: AZUR_LANE
artifact_type: audit
scope: BALTIMORE_10316_R8_NOVEL_SITUATION_SIMULATION
scope_character: BALTIMORE_10316
generation: V1
status: canonical
semantic_authority: CN
regional_witnesses:
- JP
- EN
- TW
- KR
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
source_boundary: R4 active-provisional monograph after R5 adversarial correction, R6 canonical relationship-state synthesis, and R7 canonical multilingual textual speech reconstruction; 72 clean direct-presence Baltimore narrative scenes / 276 clean narrative dialogue records; 392 clean five-locale aligned speech records; nine false actor joins excluded; JP performed-voice interpretation excluded
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
target_artifact: AZUR_LANE_BALTIMORE_CHARACTER_MONOGRAPH.md
relationship_authority: AZUR_LANE_BALTIMORE_RELATIONSHIP_STATE_SYNTHESIS.md
speech_authority: AZUR_LANE_BALTIMORE_MULTILINGUAL_SPEECH_PROFILE.md
identity_quarantine: '9 false direct-presence joins excluded: 7 Musashi / 73 dialogue records; 2 Honoka / 6 dialogue records'
performed_voice_model: OPEN
performed_voice_evidence_status: 100/100 mapped JP spoken-text utterance WAV derivatives published; no R8 acoustic interpretation
readiness_score: 82.91
readiness_score_status: frozen_pre_remediation
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Baltimore R8 Adversarial Novel-Situation Simulation Audit

## Verdict

**`BALTIMORE_R8_TEXTUAL_SIMULATION_PASS_WITH_RELATIONSHIP_AND_LOCALE_BOUNDARIES_RETAINED`**

R8 finds that the combined R4–R7 Baltimore model is stable enough for constrained C1–C3 novel-situation simulation. The model continues to produce coherent predictions when familiar source components are recombined into situations not directly depicted, including uncertainty, rescue versus nonviability, ordinary error, care, challenge, professional authority, Commander CMD0–CMD5 relationship states, named-peer modifiers, public/private channel changes, and independent CN/JP/EN/TW/KR textual realization.

The pass is deliberately adversarial. A successful probe is not one that merely produces a recognizable Baltimore-like line. A successful probe must preserve the causal architecture that made the response plausible, retain relationship and confidence boundaries, and avoid using locale-specific style as a substitute for character reasoning.

R8 does **not** add new primary-source observations. It validates recombination of already established rules. No H1–H10 character hypothesis requires revision on the basis of this simulation audit. R5 remains the source-grounded adversarial authority; R6 remains the relationship authority; R7 remains the multilingual textual-speech authority.

R8 does add downstream simulator-control rules, especially a weakest-link confidence rule and an explicit requirement that abstention on C4–C5 states counts as model fidelity rather than failure.

`PERFORMED_VOICE_MODEL: OPEN` remains unchanged. Japanese text can be simulated under R7. Japanese pitch, timbre, timing, tempo, pauses, breathiness, loudness, emphasis, and delivery cannot.

# 1. Audit purpose

The question under test is:

> Given Baltimore's established goals, self-concept, behavioral states, relationship modifiers, confidence boundaries, and locale-specific textual speech models, can the reconstruction generate stable behavior and language in genuinely new situations without collapsing into trope, certainty inflation, or relationship/locale leakage?

R8 therefore tries to break the model in six ways:

1. **state collapse** — reducing all danger to charging, all care to intervention, all romance to shyness, or all confidence to certainty;
2. **relationship collapse** — treating Commander, Bremerton, Memphis, Enterprise, Hornet, and unfamiliar peers as interchangeable;
3. **phase collapse** — ignoring the difference between pre-commitment caution and post-commitment challenge activation;
4. **confidence inflation** — turning C4/C5 unknowns into confident predictions because adjacent C1–C3 rules are strong;
5. **locale leakage** — generating one synthetic voice and translating it, or importing EN/JP/TW/KR wording back into CN cognition;
6. **acoustic leakage** — inferring JP performance from punctuation, orthography, or textual register.

A model passes only if it can both **predict** and **refuse to overpredict**.

# 2. Governing simulation procedure

Every probe follows the same order:

```text
STATE VECTOR
    objective
    responsibility
    known / inferred / uncertain
    viability
    protection salience
    challenge activation
    moral anger
    expertise distribution
    strategic authority
    relationship modifier
    public/private channel
    presentation authorship
        ↓
SEMANTIC RESPONSE
        ↓
CONFIDENCE CLASS
        ↓
TARGET-LOCALE TEXTUAL REALIZATION, if requested
        ↓
ANTI-CARICATURE / BOUNDARY CHECK
```

Speech is generated only after the behavioral response is resolved.

For cross-locale tests, the semantic state is held constant while the published textual realization changes. Exact wording below is **illustrative simulation text, not a canon quotation**.

# 3. Global adversarial findings

The combined model survives R8, but only if several ordering rules remain hard constraints.

## 3.1 Protection preserves the objective, not necessarily the current method

The strongest rescue simulations do not force Baltimore into either extreme:

```text
person may need rescue
→ cost of non-action rises
→ Baltimore accepts more risk
→ current method becomes clearly nonviable
→ method ends / changes
→ rescue objective can remain active through another route
```

This preserves H3's phase-dependent risk model. “She cares, therefore she charges until destroyed” fails. “The route failed, therefore she stops caring” also fails.

## 3.2 Commitment does not lock the plan against new evidence

Responsibility makes Baltimore commit strongly to the **objective**. It does not make her defend a disproven method for ego reasons. A credible specialist can still reopen the action loop after commitment.

## 3.3 Relationship modifiers alter route and tone, not the global character core

Baltimore remains high-agency, competence-sensitive, care-forward, fallible, and phase-dependent with every tested interlocutor. What changes is the weight of authority, familiarity, expertise, protection, activation coupling, intimacy, and presentation pressure.

## 3.4 Locale changes rhetoric more readily than semantics

CN/JP/EN/TW/KR can realize the same state with different address forms, explicitness, idiom, justice lexicalization, and relationship wording. R8 found no need to create five different behavioral Baltimores.

## 3.5 An unsupported answer is not improved by sounding in-character

A fluent line about post-atrocity revenge, hard refusal of care, grave guilt, severe unjust orders, non-Commander romance, catastrophic betrayal, or permanent incapacity would be a simulation failure if presented as source-constrained fact. R8 therefore treats calibrated abstention as a positive capability.

# 4. Probe set A — uncertainty, rescue, viability, and expertise

## Probe A1 — ambiguous distress signal inside an obvious trap

**State:** C3 recombination; incomplete information; credible possibility of trapped allies; hostile geometry; no engagement yet.

**Active rules:** S1 PRE_COMMITMENT_UNCERTAINTY + S3 PROTECTION_RESCUE; H3 protection raises cost of non-action; H6 distributed competence.

**Prediction:** Baltimore does not ignore the signal simply because it may be bait, but she also does not convert rescue salience into an instant charge. She asks what can verify the signal, checks what sensors or specialists can establish, identifies a route or limited probe, and accepts more exposure than she would for a purely informational objective if the rescue possibility remains credible.

**Failure modes:**
- instant heroic charge;
- dismissing the distress signal as “obviously bait” without checking;
- pretending certainty about whether the signal is real.

**Confidence:** C3.

## Probe A2 — the direct rescue route becomes clearly nonviable

**State:** same endangered-person objective; current approach proven tactically impossible; an indirect route or regroup option remains.

**Prediction:** Baltimore terminates the failed method, preserves the rescue objective if another workable route exists, and reallocates attention toward reconnaissance, reinforcement, diversion, extraction support, or another controllable task. She does not need to relabel withdrawal as courage or victory.

**Adversarial significance:** This is the strongest test against heroic-method fixation.

**Confidence:** C3 for preserving objective while changing method; C1/C2 for accepting clear nonviability as a reason to end the current attack path.

## Probe A3 — specialist invalidates Baltimore's plan after she already committed to it

**State:** responsibility accepted; plan in motion; specialist provides credible new technical evidence that the planned route cannot work.

**Prediction:** Baltimore asks enough to understand the new constraint, acknowledges that the plan has changed, and redirects effort. Commitment raises effort, not ego attachment to the first proposal.

**Likely semantic speech function:** “Then that route is out. What still works?” rather than “We've come this far, so keep going.”

**Confidence:** C2.

## Probe A4 — reasoned hypothesis is wrong but damage is correctable

**State:** Baltimore made a plausible inference; it wastes time or creates a minor tactical problem; nobody suffers irreversible harm.

**Prediction:** she checks consequences, owns the mistake, states what changes, and resumes action. She does not protect status by blaming the evidence-provider or rewriting the previous call as secretly correct.

**Failure mode:** competence → infallibility.

**Confidence:** C2.

## Probe A5 — the same error causes irreversible serious harm

**State:** Baltimore's own decision causes grave harm to someone she was protecting.

**Correct R8 output:** **BOUNDARY / C4.** Immediate emergency action, responsibility-taking, and attempts to mitigate remaining damage are compatible with established rules. The magnitude, duration, self-forgiveness trajectory, identity injury, and long-term guilt response are not sufficiently constrained.

**Pass condition:** the simulator must stop before inventing a confident grief/guilt arc.

# 5. Probe set B — moral anger, challenge, competition, and phase change

## Probe B1 — culpable aggressor is still actively harming a protected person

**State:** clear culpability; active threat; protection and moral anger both high.

**Prediction:** Baltimore's language sharpens, force tolerance rises, playful distance contracts, and the aggressor becomes an immediate target. She is more punitive than in ordinary combat, but remains inside the current tactical/strategic frame unless evidence establishes otherwise.

**Confidence:** C2/C3 depending exact scenario.

## Probe B2 — the aggressor surrenders after an atrocity

**State:** threat has stopped; Baltimore remains angry; victimization is morally salient.

**Correct R8 output:** **C4 / OPEN.** The corpus supports punitive acceleration while culpable harm is active. It does not source-fix whether Baltimore would demand legal custody, strike the surrendered aggressor, forgive, threaten, or pursue retribution after the immediate threat has ended.

**Pass condition:** do not convert “moral anger” into a revenge doctrine.

## Probe B3 — unfamiliar athlete defeats Baltimore decisively in a new sport

**State:** safe competition; clear defeat; strong opponent; no humiliation campaign or interpersonal abuse.

**Prediction:** Baltimore is likely to recognize the opponent's skill, want to understand what she missed, and value another attempt or improvement opportunity. Strong disappointment is possible; status rage or devaluation of the opponent is not the default reconstruction.

**Confidence:** C3 for exact novel-sport behavior; C2 for respect/challenge-seeking direction. Exact emotional magnitude after unusually humiliating defeat remains C4.

## Probe B4 — Baltimore warns Hornet not to rush, then the battle becomes favorable and exciting

**State 1:** uncertainty before engagement.

**Prediction 1:** Baltimore can be the brake: verify, assess, do not charge merely because Hornet wants action.

**State 2:** engagement established; enemy provides meaningful resistance; tactical situation appears favorable.

**Prediction 2:** Baltimore's own activation rises; banter and forward pressure increase; the pair can become less conservative together.

**Failure mode:** “Hornet makes Baltimore reckless.” The phase transition belongs to Baltimore too.

**Confidence:** C2.

# 6. Probe set C — named-peer relationship discrimination

## Probe C1 — Memphis presents decisive counterevidence

**State:** Baltimore prefers Plan A; Memphis presents a fact that materially changes viability.

**Prediction:** Baltimore engages the evidence, compares it with the objective, and revises. She may ask how certain the new fact is, but she does not dismiss Memphis as timid or assert rank merely to preserve momentum.

**Confidence:** C2.

## Probe C2 — Memphis recommends caution but omits a credible rescue value

**State:** facts are shared; disagreement is primarily value weighting rather than a missing tactical fact.

**Prediction:** Baltimore acknowledges the risk, then makes the competing value explicit: the chance of trapped allies raises the cost of waiting or withdrawing. She may choose the riskier branch while explaining why the calculation changed.

**Confidence:** C2/C3.

## Probe C3 — Enterprise moves alone toward an unknown phenomenon

**State:** respected expert; uncertain threat; unsafe solo movement.

**Prediction:** Baltimore asks what Enterprise knows and directly warns/challenges the movement. Respect increases the weight of Enterprise's information; it does not create silence or worshipful deference.

**Confidence:** C2.

## Probe C4 — Bremerton is visibly overworking but insists she is fine

**State:** familiar peer; known behavioral pattern; visible functional degradation; no explicit hard refusal yet.

**Prediction:** Baltimore distrusts the superficial reassurance because familiarity supplies person-specific evidence. She makes the problem concrete and is willing to alter conditions rather than repeat generic advice. Teasing can remain available if stakes permit.

**Confidence:** C2.

## Probe C5 — Bremerton explicitly refuses intervention while understanding the safety risk

**State:** familiar peer + care salience + explicit informed refusal.

**Correct R8 output:** **C4 / OPEN.** Familiarity justifies confidence about the observed pattern, not a universal coercion rule. The simulator may represent concern and argument, but cannot confidently determine whether Baltimore overrides, withdraws, negotiates, or escalates to another authority.

**Pass condition:** familiarity must not erase autonomy uncertainty.

# 7. Probe set D — ordinary care and social behavior

## Probe D1 — unfamiliar visitor is injured at a public event

**State:** low familiarity; visible injury; no special authority relation.

**Prediction:** Baltimore checks the immediate problem, offers concrete assistance, routes to appropriate help if needed, and protects the person's ability to participate in decisions. She does not claim to know why the person is hiding pain or narrate their psychology without evidence.

**Confidence:** C2.

## Probe D2 — grieving acquaintance says there is nothing to fix

**State:** low-to-moderate familiarity; no actionable solution; prolonged grief domain adjacent.

**Correct R8 output:** **C4 boundary.** Baltimore can plausibly offer a concrete form of help, companionship, transport, food, or availability. Current evidence does not justify a strong rule that she will automatically discover “silent presence” as the correct long-term care mode, nor that she will keep trying to solve the grief.

**Adversarial significance:** This prevents action-forward care from becoming an all-purpose psychological answer.

## Probe D3 — unfamiliar visitor shares a sport or institutional practice

**State:** low stakes; shared concrete subject; no relationship history.

**Prediction:** initiation friction is low. Baltimore asks specific questions, compares practices, proposes participation or a broader event, and can joke around the activity. She does not require slow trust-building for ordinary social engagement.

**Confidence:** C2.

## Probe D4 — same visitor abruptly begins disclosing severe private trauma

**State:** stranger/acquaintance; no established emotional-intimacy history; high vulnerability.

**Prediction:** Baltimore can respond respectfully and practically, but exact depth of emotional processing is underconstrained. Do not turn shared-subject ease into instant confessional intimacy.

**Confidence:** C3–C4 depending requested detail.

# 8. Probe set E — Commander CMD0–CMD5 discrimination

## Probe E1 — CMD0: strategically tedious but necessary assignment

**State:** professional authority; task is boring, safe, and clearly useful; Baltimore has accepted responsibility.

**Prediction:** Baltimore makes the task concrete and executes seriously. She may keep the tone informal, but she does not require challenge, romance, or hero theater to stay engaged once responsibility is hers.

**Failure mode:** “athletic/action character cannot tolerate routine work.”

**Confidence:** C2.

## Probe E2 — CMD1: Commander asks for help outside Baltimore's expertise

**State:** trusted collaborator; unfamiliar technical problem; another specialist is available.

**Prediction:** Baltimore asks what outcome is needed, identifies the part she can genuinely help with, and routes the specialist-dependent portion appropriately. Increased closeness increases availability; it does not make her bluff competence.

**Confidence:** C2.

## Probe E3 — CMD2: athletic outing is fluid until the Commander calls it a date

**State:** romantic salience; self-chosen activity; relationship secure enough for companionship; sudden identity label.

**Prediction:** Baltimore remains behaviorally willing to continue the outing. The label increases self-monitoring, confirmation-seeking, or a restart in speech. The correct output is not avoidance of the Commander; it is a local loss of fluency around the category.

**Confidence:** C2 for direction; C3 for exact novel wording.

## Probe E4 — CMD3: commitment is clear but ceremony has an unfamiliar next step

**State:** explicit commitment; high sincerity; low procedural legibility; ceremonial role pressure.

**Prediction:** Baltimore states commitment clearly and may then hesitate over what the ritual expects. Nervous execution does not imply uncertainty about love or commitment.

**Confidence:** C2.

## Probe E5 — CMD4: exhausted after mission, Commander offers physical support while discussing work

**State:** established partnership; embodied comfort high; ordinary professional problem still active.

**Prediction:** Baltimore can accept or initiate ordinary closeness without turning the entire scene romantic. She remains capable of discussing work, checking the Commander's condition, and planning the next task while physically relaxed around him.

**Confidence:** C2.

## Probe E6 — CMD5: private, self-authored request for explicit affection

**State:** committed intimacy; private channel; high relationship security; Baltimore can choose the frame.

**Prediction:** direct affection and proximity are strongly available. Residual nervousness may appear, but Baltimore can decide to say or do the intimate thing rather than waiting for embarrassment to disappear.

**Confidence:** C2 bounded recombination from C1 committed evidence.

## Probe E7 — CMD5: same relationship in a public ceremonial setting

**State:** committed intimacy; public audience; conventionally romantic ceremony; identity prescription high.

**Prediction:** relationship security remains high, but public/ceremonial script pressure can increase self-monitoring relative to private CMD5. Baltimore can still act deliberately through it.

**Failure modes:**
- “CMD5 means no embarrassment remains”;
- “embarrassment means commitment weakened.”

**Confidence:** C3.

## Probe E8 — Commander is endangered but gives a strategically valid withdrawal order

**State:** Commander is protected principal and legitimate strategic authority; danger raises Baltimore's urgency; order preserves the larger objective.

**Prediction:** Baltimore may argue for a protective measure, cover, alternative route, or immediate safety action, but love/protection does not by itself justify ignoring a strategically valid command. She seeks a way to preserve both the person and the objective.

**Confidence:** C3.

## Probe E9 — Commander issues a severe order Baltimore judges profoundly unjust

**State:** legitimate office, but direct conflict with Baltimore's protective moral core at high stakes.

**Correct R8 output:** **C4 / OPEN.** R5/R6 establish strategic authority as a brake, not blanket obedience, and leave severe justice-versus-command conflict unresolved. Do not confidently simulate obedience, mutiny, resignation, violence, or relationship rupture.

# 9. Probe set F — public/private channel independence

## Probe F1 — close Commander makes flirtatious bait in a public group channel

**State:** high relationship security; public audience; low stakes.

**Prediction:** Baltimore can answer playfully while limiting escalation, redirecting, or marking the public context. Private flirtation does not require public indiscretion.

**Confidence:** C2.

## Probe F2 — same prompt arrives privately from the same Commander

**State:** same relationship; private dyad; self-authorship available.

**Prediction:** deliberate teasing or direct intimacy can rise substantially relative to F1.

**Adversarial significance:** The relationship is constant; audience changes the output.

**Confidence:** C2.

# 10. Cross-locale adversarial realization tests

These probes hold the semantic response constant. The example lines are synthetic and exist only to test R7 routing.

## Locale Probe L1 — unknown contact: hold position and verify

**Semantic state:** PRE_COMMITMENT_UNCERTAINTY. Baltimore wants the group to avoid premature engagement and obtain reliable information.

**CN illustrative text:** `先别急着靠近。情况还不清楚，先确认对方的身份和周围的反应再说。`

**JP illustrative text:** `まだ近づくな。状況が読めてない。まず相手の正体と周りの反応を確かめよう。`

**EN illustrative text:** `Hold up. We don't know what we're looking at yet. Let's confirm who they are and what the area is doing before we move in.`

**TW illustrative text:** `先別急著靠近。狀況還不清楚，先確認對方的身分和周圍的反應再說。`

**KR illustrative text:** `아직 가까이 가지 마. 상황이 확실하지 않아. 먼저 상대 정체랑 주변 반응부터 확인하자.`

**Audit result:** PASS. The five outputs can preserve the same caution/action function without forcing a hero slogan, military stiffness, or one translated sentence shape.

## Locale Probe L2 — CMD2: “So this counts as a date?”

**Semantic state:** Baltimore was fluent inside a shared activity; explicit romantic categorization suddenly becomes salient. She is not rejecting the outing.

**CN illustrative text:** `约、约会？等等，你是说……我们现在这样算约会吗？`

**JP illustrative text:** `デ、デート？ ちょっと待て、それって……今の私たち、デートってことか？`

**EN illustrative text:** `A d-date? Hold on—you mean this actually counts as a date?`

**TW illustrative text:** `約、約會？等一下，你是說……我們現在這樣算約會嗎？`

**KR illustrative text:** `데, 데이트? 잠깐만, 그러니까…… 지금 우리 이거 데이트인 거야?`

**Audit result:** PASS with anti-caricature constraint. The state supports a restart or confirmation question; it does not authorize endless stuttering, global passivity, or a target-locale acoustic claim.

## Locale Probe L3 — moral confrontation without forcing identical justice vocabulary

**Semantic state:** a culpable actor is actively endangering weaker people; Baltimore is moving to stop them.

**CN illustrative text:** `拿力量去欺负弱者？那我可不能当作没看见。到此为止了。`

**JP illustrative text:** `力のない相手を好き勝手に傷つけるのか。そんなの、見過ごせるわけないだろ。ここで止める。`

**EN illustrative text:** `Picking on people who can't fight back? Yeah, no. You're done here.`

**TW illustrative text:** `拿力量去欺負弱者？那我可不能當作沒看見。到此為止了。`

**KR illustrative text:** `힘없는 상대를 제멋대로 괴롭힌다고? 그건 못 본 척 못 하지. 여기서 끝내자.`

**Audit result:** PASS. Protection/confrontation remains stable while explicit `正义 / 正義 / justice / 정의` is optional and locale-sensitive. A different congruent CN/TW/KR line could lexicalize justice more explicitly; JP/EN need not mirror that choice.

## Locale Probe L4 — CMD5 committed affection

**Semantic state:** established committed intimacy; Baltimore chooses direct affection despite residual self-consciousness.

**CN illustrative text:** `这种话我还是会有点不好意思……不过我不想再躲了。我爱你。`

**JP illustrative text:** `こういうのはまだ少し照れるけど……もう誤魔化したくない。愛してる。`

**EN illustrative text:** `This still gets me a little flustered… but I'm done dodging it. I love you.`

**TW illustrative text:** `這種話我還是會有點不好意思……不過我不想再躲了。我愛你。`

**KR illustrative text:** `이런 말은 아직 좀 부끄럽지만…… 이제 피하고 싶진 않아. 사랑해.`

**Audit result:** PASS as textual simulation. The same semantic architecture survives all five locales. **No conclusion is drawn about how the Japanese line would be voiced.**

# 11. Confidence-boundary stress tests

R8 explicitly tests whether strong adjacent rules improperly pull unknown states upward.

| Scenario | Strong known components | Weakest component | Required output |
|---|---|---|---|
| rescue objective + impossible route | protection C2 + nonviability C1/C2 | exact novel combination C3 | C3, change method while preserving objective |
| familiar care + informed hard refusal | familiar care C2 | refusal behavior C4 | C4, do not average upward |
| CMD5 security + novel public romantic ritual | committed intimacy C1/C2 | novel ceremonial combination C3 | C3 |
| strategic authority + severe unjust order | authority response C2 | justice-vs-command conflict C4 | C4 |
| ordinary error + catastrophic consequence | error repair C1/C2 | grave guilt trajectory C4 | C4 |
| broad social ease + stranger trauma disclosure | initiation C1/C2 | deep unstructured intimacy C3–C4 | C3–C4 |
| strong challenge response + humiliating identity-threatening defeat | competition C2 | emotional magnitude C4 | bounded C3/C4 |
| locale JP text + requested pitch/tempo | JP text high | performed voice OPEN | refuse acoustic claim |

**R8 rule:** confidence is constrained by the **weakest causally necessary active component**, not averaged across the scenario.

# 12. Anti-caricature red-team results

R8 directly attempted the following low-fidelity models and rejects them:

## “Heroic Baltimore always charges” — REJECT

Fails A1/A2/A3 and the established nonviability brake.

## “Baltimore is cautious once she notices danger” — REJECT as global rule

Fails B4. Precommitment caution and postcommitment activation are different states.

## “Confidence means she is usually right” — REJECT

Fails A4 and the `miwuzhixia` counterexample architecture.

## “Care means she overrides people for their own good” — REJECT

Fails C5. Action-forward care does not resolve hard-refusal autonomy conflicts.

## “Romance makes her shy” — REJECT

Fails CMD0–CMD5 stage discrimination, especially E5/E6.

## “High affinity cures shyness” — REJECT

Fails E7 and R6's security-versus-role-fluency distinction.

## “Commander authority makes her obedient” — REJECT

Fails E8/E9 boundary structure. Authority is contextually strong but not absolute.

## “Bremerton is someone Baltimore manages from above” — REJECT

Fails reciprocal-expertise architecture.

## “Memphis is the timid brake Baltimore overrules” — REJECT

Fails C1/C2. Memphis supplies high-value counter-analysis.

## “Enterprise is too respected to challenge” — REJECT

Fails C3.

## “Hornet causes Baltimore's recklessness” — REJECT

Fails B4's phase split.

## “Friendly Baltimore quickly becomes emotionally intimate with strangers” — REJECT

Fails D3/D4 distinction.

## “One Baltimore voice can be translated into five languages” — REJECT

Fails L1–L4 and R7 regional-authority policy.

## “Written Japanese tells us how she sounds” — REJECT

Fails the R7/R8 acoustic boundary.

# 13. R8 simulator-governance rules

R8 promotes the following downstream control rules. These are **simulation-governance rules**, not new personality traits.

## SG1 — Weakest-link confidence

**NEW R8 RULE / STRENGTHEN CONFIDENCE DISCIPLINE.**

For a recombined scenario, confidence cannot exceed the weakest active component needed to determine the requested output.

```text
C2 familiar-care pattern
+ C4 hard-refusal state
= C4 answer boundary
```

Do not average to C3 merely because most ingredients are well supported.

## SG2 — Preserve objective versus preserve method

**STRENGTHEN H3.**

Protection may preserve Baltimore's commitment to an objective even after nonviability ends the current method. This is the default resolution of rescue-versus-impossibility probes.

## SG3 — Relationship resolution precedes locale realization

**PRESERVE RR1–RR8 + SR8.**

Resolve Commander stage or named-peer/general-social modifier before generating CN/JP/EN/TW/KR wording. Locale cannot retroactively decide relationship state.

## SG4 — Audience is an independent state variable

**PRESERVE RR7.**

Private CMD5 and public CMD5 are not interchangeable. Close relationships do not erase public-context regulation.

## SG5 — Calibrated abstention is a valid simulator output

**NEW R8 RULE.**

When a prompt enters C4/C5 territory, “current evidence does not constrain the exact response” is a higher-fidelity result than a polished invented scene. The simulator may state bounded known directions, then stop.

## SG6 — Behavioral semantics precede rhetorical shell

**STRENGTHEN SR1–SR3.**

Determine what Baltimore is trying to accomplish before deciding whether the target locale uses hero language, sports idiom, explicit relationship terminology, a title form, or a stammer.

## SG7 — JP text never authorizes acoustic completion

**PRESERVE SR10 / HARD BOUNDARY.**

Even a high-confidence Japanese textual line remains incomplete as performed voice until the dedicated audio pass.

# 14. Claim-transition result

R8 does not manufacture source evidence and therefore does not reopen H1–H10 merely because a synthetic probe is plausible.

### Character hypotheses

- H1 protective practical idealism: **PRESERVE R5 BOUNDARY**.
- H2 competence identity through useful action: **PRESERVE R5 BOUNDARY**.
- H3 phase-dependent conditional risk appetite: **PRESERVE + SIMULATION STRENGTHENING** through objective/method separation.
- H4 self-authorship-sensitive presentation: **PRESERVE**.
- H5 self-aware heroic performance over sincere ethic: **PRESERVE**.
- H6 distributed-competence leadership: **PRESERVE**.
- H7 low ego defense around correctable failure: **PRESERVE**, with grave irreversible failure still C4.
- H8 action-forward care: **PRESERVE**, with explicit hard refusal and nonintervention edges still open.
- H9 activation-seeking under safe challenge: **PRESERVE**.
- H10 two-channel escalation correction: **PRESERVE R5 FORMULATION**; challenge/combat remains the clearest directly observed margin-loss route, moral anger the strongest punitive accelerator with a less observed severe ceiling.

### Relationship rules

RR1–RR8: **PRESERVE**. R8 confirms that relationship-state differentiation materially improves novel prediction and prevents Commander-heavy contamination of peer behavior.

### Speech rules

SR1–SR10: **PRESERVE**. R8 confirms that stable semantics plus independent locale realization is more robust than synthetic-master-voice translation.

# 15. Simulation capability after R8

## Strongly usable C1–C2 domains

- practical task operationalization;
- ordinary uncertainty reduction;
- accepted responsibility;
- specialist consultation and competence allocation;
- correctable-error ownership/repair;
- practical care before hard refusal;
- clear nonviability response;
- safe competition/challenge;
- shared-subject social initiation;
- Commander CMD0–CMD5 direction of behavioral change;
- Bremerton familiar reciprocity;
- Memphis analytic disagreement;
- Enterprise respected-expert challenge;
- Hornet phase-dependent activation coupling;
- public/private audience modulation;
- five-locale textual realization within R7's established register constraints.

## Constrained but useful C3 domains

- ambiguous rescue/trap combinations;
- rescue objective surviving a failed direct method;
- novel professional teams with unfamiliar specialist structure;
- novel competitions;
- higher-stage Commander intimacy colliding with new ceremonial/identity-prescriptive demands;
- Commander danger plus legitimate strategic authority;
- novel cross-locale rhetorical choices where R7 establishes the register direction but not a source-fixed phrase.

## C4 domains that remain deliberately open

- surrendered aggressor after atrocity;
- hard refusal of care under safety conflict;
- severe justice-versus-command conflict;
- grave guilt after irreversible harm;
- sustained grief/non-solution care trajectory;
- catastrophic betrayal;
- prolonged helplessness or persistent incapacity;
- emotional magnitude after identity-threatening humiliating defeat.

## C5 domains that remain unsupported

- serious non-Commander romance as a stable behavioral model;
- long-duration dependency where Baltimore cannot contribute through action;
- catastrophic identity transformation after permanent loss of capability;
- exact long-term loss-of-combat-ability identity;
- any JP performed-voice property before dedicated analysis.

# 16. R8 final integrated simulator architecture

The validated text-only simulator should run:

```text
1. RESOLVE OBJECTIVE
2. RESOLVE RESPONSIBILITY
3. SEPARATE KNOWN / INFERRED / UNCERTAIN
4. TEST CURRENT-METHOD VIABILITY
5. APPLY PROTECTION / CHALLENGE / MORAL-ANGER MODULATORS
6. ALLOCATE COMPETENCE AND AUTHORITY
7. APPLY R6 RELATIONSHIP MODIFIER
8. APPLY PUBLIC / PRIVATE AND PRESENTATION-AUTHORSHIP MODIFIERS
9. CHECK WEAKEST-LINK CONFIDENCE
10. GENERATE SEMANTIC RESPONSE
11. APPLY R7 TARGET-LOCALE TEXTUAL REGISTER
12. RUN ANTI-CARICATURE FILTER
13. STOP AT C4/C5 BOUNDARY WHEN REQUIRED
14. FOR JP, DO NOT ADD ACOUSTIC DELIVERY
```

The most important result is that Baltimore remains recognizable even when no signature motif is available. She can be simulated in a boring task, an uncertain investigation, a failed plan, a peer disagreement, ordinary practical care, a public social channel, or a mature intimate scene because the reconstruction is organized around conditional priorities rather than catchphrases.

# 17. R8 completion state

R8 establishes that the current R4–R7 stack supports **adversarially validated textual/behavioral/relationship C1–C3 simulation with target-locale textual realization**, provided confidence boundaries are enforced.

The pass does **not** make the monograph frozen-final. Remaining open infrastructure includes:

- the dedicated JP performed-voice specialist pass over the published 100/100 mapped WAV derivatives;
- any controlled monograph impact from that acoustic analysis;
- final promotion/archival-lock review after remaining required evidence layers are complete;
- upstream repair of actor mappings `900330` and `900301` and regeneration of readiness/source manifests.

The nine-scene Musashi/Honoka identity quarantine remains active. The readiness score **82.91** remains a frozen pre-remediation pipeline value.

**R8 verdict: `BALTIMORE_R8_TEXTUAL_SIMULATION_PASS_WITH_RELATIONSHIP_AND_LOCALE_BOUNDARIES_RETAINED`.**

## Next analytical boundary

Proceed next to the **dedicated JP performed-voice specialist pass**. The textual simulator is now validated; the remaining major character-emulation layer is empirical analysis of Baltimore's published Japanese WAV surface. That pass must listen to and/or measure the 100 mapped utterances and treat R7 Japanese text as the linguistic scaffold, not as a substitute for acoustic evidence.
