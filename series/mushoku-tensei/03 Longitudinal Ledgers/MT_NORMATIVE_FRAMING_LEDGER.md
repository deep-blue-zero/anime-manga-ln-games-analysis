---
title: "Mushoku Tensei - Normative framing ledger"
artifact_id: MT_NORMATIVE_FRAMING_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.8"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V08 only; prior history preserved, V08 updates; publication/audit separate."
---

# Normative framing ledger

## Responsibility

Owns diagnostic non-graphic framing records and comparisons across conduct, affected-person access, consent, power, narrative tone, consequences, and later opportunities. It does not own a total morality score or infer creator intent from a scene alone.

## Record format

`normative event ID | observation refs | represented event | ages/uncertainty | knowledge/capacity | power/alternatives | consent/boundaries | focalizer/affected-person access | formal cues | consequences | strongest readings and counterreadings | scope/criterion | claim refs; comparison ID | related event IDs | matched issue | differences | change/continuity | limits`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append diagnostic event records under MT_NORMATIVE_FRAMING_PROTOCOL; compare only warranted cases. Update shared proposition changes in the claims ledger, keeping normative events linked rather than duplicated. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

The source is `MT-LNJP-V01`; IDs link the [canonical reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). This ledger uses non-graphic descriptions. “Wrong” identifies an analyst **value judgment** under the named criterion, not an asserted universal audience response or author intention. Narrator, focal person, other-character response and implied pattern are separate.

| Event ID / evidence | Conditions, access, tone, consequence | Strongest reading / counterreading / bounded judgment |
| --- | --- | --- |
| `MT-N-001` `001–002` | An adult reports trauma, family neglect and sexualized fantasy; he makes a costly rescue after anticipating regret. Only his account of prior family/school is available. | Rescue warrants credit for the actual intervention; his own stated motive complicates pure-altruism rhetoric without invalidating aid. Suffering explains but does not absolve unrelated misconduct. |
| `MT-N-002` `004,008` | Infant with retained adult memories behaves in ways that Lilia experiences as sexually intrusive; Roxy's property is later stolen and disclosed as a farewell punch line. Lilia receives focalized aversion; Roxy's direct response to the original theft is limited, though her letter later mentions it. | Lilia's reaction supplies meaningful affected-person access. The cut from sincere gratitude to a theft gag can distance readers from his reverence, but also treats the violation lightly. Under a bodily/property-boundary criterion, gratitude does not authorize appropriation. No global endorsement conclusion. |
| `MT-N-003` `006–008` | Roxy and Rudeus each damage valued property/put others at risk through magic. Zenith corrects Roxy over her tree; Roxy repairs it; Rudeus's indoor damage leads to instruction rather than expulsion. Roxy's storm briefly harms the horse before healing. | Comic errors are accompanied by material consequences and repair; the scenes do not establish that high ability licenses careless practice. Rudeus's parental protection and a paid teacher's responsibility differ, so strict penalty symmetry is an inadequate test. |
| `MT-N-004` `009–010` | Bullying targeted at a child for ancestry/appearance; Rudeus intervenes, then Paul strikes him on an inaccurate account and apologizes after hearing him. Sylph's immediate fear and Paul's interior failure are visible. | V01 criticizes prejudicial targeting and unhearing discipline through action and corrective focalization. Rudeus's own “fight back” advice initially overlooks larger threats. The apology establishes local recognition, not guaranteed nonviolence. |
| `MT-N-005` `011–012` | Sylphie, approximately Rudeus's peer in bodily childhood, explicitly resists undressing; he overrides her, briefly pauses, then overrides again. She cries, remains wary of touch and asks for ordinary interaction; Paul names her refusal and instructs apology. The image at `text/part0019.html` emphasizes comic surprise. | **Value judgment:** the override is wrong under a clear-refusal/bodily-autonomy criterion, independent of his claimed aim to prevent cold or later shock at her sex. **Formal inference:** distress and continuing distance criticize the act, while the gender-reveal joke and quick reconciliation accommodate its comic treatment. She does not grant retroactive consent by remaining a friend. No explicit passage is reproduced. |
| `MT-N-006` `012,015` | He fantasizes about directing Sylphie's future affection after her abandonment fear, recognizes a disturbing implication and checks himself; no completed grooming plan is represented. Her independent preference is for normal treatment and presence, not future partnership terms. | Present self-interruption is evidence of awareness, not proof of lasting restraint. Her isolation increases asymmetry and makes promises of care consequential. **Working hypothesis:** romantic-game framing risks reducing her agency; later comparable decisions would test whether he respects her independent alternatives. |
| `MT-N-007` `013–014` | Paul's affair breaches Zenith's explicit exclusivity expectation. Lilia risks losing income and a safe home. Rudeus knowingly makes a false specific coercion accusation, then retracts it privately; Lilia reports recent initiative and earlier forced conduct. Zenith states her own fear and eventual choice to care for both infants. | Under a truthful, consent-sensitive deliberation criterion, inventing coercion is wrong even when the immediate protective aim is legitimate. The earlier forced act deserves separate scrutiny; Lilia's self-blame for the recent affair does not ratify it. Zenith's mercy has her own reasons and costs; “case solved” is an incomplete ethical closure. |
| `MT-N-008` `014–015` | Lilia, midwife, Zenith and Rudeus supply birth/infant care; Zenith feeds Aisha when Lilia is absent despite unresolved faith and hurt. Ordinary labor is shown, not merely a reward for the protagonist's intervention. | Particular chosen care can be affirmed without assuming the family hierarchy is freely negotiated or all future conflict settled. Aisha's future service is Lilia's plan, not the child's agreement. |
| `MT-N-009` `010,016` | Paul fears dependency and arranges employment/education; he strikes, binds and removes his seven-year-old son without hearing him, imposes five years without Sylphie contact, while she tries to stop it. His motive and reservations get a later viewpoint. | Concern about dependence is supported; necessity/proportionality of this force and absolute duration is **unresolved**. His earlier lesson about listening and apology creates a visible contradictory paternal practice, not automatic proof of either hypocrisy as stable essence or justified exceptionalism. Outcomes unavailable at V01. |

**Matched-case comparison `MT-NC-001`:** `MT-N-004` versus `MT-N-009` tests Paul's principle that the strong should listen and not use force casually; his first error is admitted, his later force is deliberated but still unconsented. Difference in purpose and duration matters; the shared asymmetry does too. **Comparison `MT-NC-002`:** `MT-N-005` versus `MT-N-006` separates completed physical override from subsequent fantasy and restraint, avoiding an invented equivalence. V01 supports scene/volume-level findings only. No percentage, morality score, reader effect or creator intention is claimed.

## V02 normative records and comparisons — 2026-09-26 UTC

Source observation numbers resolve in [V02](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V02-`. All accounts are non-graphic. Current scope V01–V02; V01 conclusions are preserved. Judgments name analyst criteria and do not assert audience effect or creator intent.

| Event / observations | Conduct, conditions, framing and consequences | Bounded evaluation / consequential alternative |
| --- | --- | --- |
| `MT-N-010` / `001–004` | Rudy seven/Eris nine; staged abduction approved by father becomes actual danger. Rudy uses withheld complete healing, false threats and conditional aid; genuine rescue skills remain insufficient without Ghislaine. | Wrong under noncoercive-care criterion. Emergency cooperation may justify quiet/coordination, not manufactured fear or the initial scheme. Narrator's later necessity claim lacks a counterfactual test. |
| `MT-N-011` / `005` | Patriarchs demand humiliating gendered request; Rudy ends routine after mixed motives, including noticing Eris's aversion and fearing retaliation. Comedy exposes adult preferences. | Specific reform observed; broad autonomy principle unproved. Her coerced performance is not freely expressed agreement. |
| `MT-N-012` / `006` | Sleeping child's bodily boundary violated; she responds defensively. Prose and split illustration supply comic sexualized framing. | Wrong under bodily-autonomy criterion; defensive blow differs from arbitrary aggression. Comic treatment can minimize harm even when resistance is represented. |
| `MT-N-013` / `006–008,011–012` | Patient practice, practical examples, wage protection, rest, food saved for working guard, collaborative dance and gifts. | Positive care under attentive-help criterion; employment, self-interest and status also operate. These benefits are genuine without cancelling misconduct. |
| `MT-N-014` / `009` | After Eris tenth birthday, seeing her cherish gifts interrupts intended touching while asleep. He actually refrains. | Diagnostic local restraint, not absence of opportunity. Later override prevents generalization; no supernatural efficacy inferred from ring metaphor. |
| `MT-N-015` / `012–013` | Succession custom separates sons from mother per Philip; affection becomes marriage pressure and political proposal involving daughter. | Wrong to treat a child's choices as bargaining assets. Protective provision and grief explain behavior without making coercion voluntary. Hilda backstory mediated. |
| `MT-N-016` / `014` | Rudy ten/Eris twelve; he exceeds limited permission, she stops him/leaves; self-reproach recognizes care and limits of game scripts. Apology and particular forgiveness followed by future-boundary promise and his guaranteed-reward interpretation. | Clear violation under consent criterion. Recognition and stated restraint are real, durable transfer UNTESTED. Future consent remains revisable; entitlement persists. No graphic quotation or generated scenario. |
| `MT-N-017` / `015` | Fifteen-year-old prince uses unwanted contact, threats and private force against Roxy; her perspective names aversion, contract allows refusal, she departs/defends herself. | Clear coercion under autonomy criterion. Institutional response is framed around losing valuable employee, not stated general justice. Her teacher self-blame should not absorb prince's agency. |
| `MT-N-018` / `016–017` | Revenge/suspicion leads to preemptive attack; oath backed by recognized rank ends it, no apology. Rudy then shields Eris from catastrophe. | Suspicion is insufficient justification for lethal attack. Actual protection deserves specific credit; it is not redemption by cancellation. Prestige distributes credibility unevenly. |
| `MT-N-019` / `018` | Refugees grieve despite food, information incomplete; Paul organizes family search, Roxy chooses to seek overlooked Rudy. | Care through practical choice under uncertainty. Trust in Rudy also assigns burden; no result yet verifies appropriateness. Material sufficiency does not settle wellbeing. |
| `MT-N-020` / `019` | Ghislaine's search-driven disorientation and powerful violence coincide with military deception; Vigo survives, others die, cult celebrates rescue. | Protective intent and beneficiary gratitude do not establish justified indiscriminate force. Narrative shows contingencies and conflicting purposes; later heroic label is not a complete ethical account. |

**`MT-NC-003`:** V01 `MT-N-005/006` versus V02 `MT-N-012/014/016`: compare refusal, sleeping vulnerability, actual restraint, recognition and future commitment. Different age/relationship stages matter; persistence is not established merely by repeated apologies. `MT-C-002` strengthened.

**`MT-NC-004`:** V02 `MT-N-010` versus `MT-N-013`: engineered helplessness and adaptive education both precede improved cooperation, but only the latter's actual mechanisms are observed across routine tasks. Do not infer the former necessary from temporal priority. `MT-C-008` opened.

**`MT-NC-005`:** `MT-N-016` versus `MT-N-017`: each includes refusal and sexual entitlement; access differs sharply, as do authority, age, contractual protection and consequences. This supports a specific framing comparison, not a mechanically identical penalty standard or complete endorsement verdict.

**`MT-NC-006`:** V01 `MT-N-009` versus V02 `MT-N-010/015`: adult protection and future opportunity coexist with imposed choices. New job benefits revise the outcome question but do not prove coercion necessary. `MT-C-006,009` updated.


## V03 updates — 2026-09-26 UTC

Prior V01/V02 bodies remain historical and unchanged. Current scope is Japanese LN V01–V03; input is audited V02 head `687a13ac1a661270ab566c9e1a6028acd607d846`. Observation suffixes below resolve in [V03's diagnostic readings](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V03-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Event / observations | Conduct, affected access and consequence | Analyst criterion / alternative and limit |
| --- | --- | --- |
| `MT-N-021` / `002–005` | Children receive rescue, hospitality, news and material help; Ruijerd's threat at gate coexists with care. | Attentive help merits local credit; protection is not blanket license for violence. Histories remain attributed. |
| `MT-N-022` / `008` | Kurt ignores avoidance/damages hood; Eris attacks beyond incapacitation and others also suffer. Rudy delays while pleased, then stops and heals; adult initially treats harmless. | Proportionality: initial intrusion does not justify unlimited retaliation. Stress/affection explain without absolving; no total access to her motives. |
| `MT-N-023` / `009` | Rudeus recognizes Eris's fear, comforts and explicitly refrains from exploitation. | Genuine comparable restraint under autonomy criterion; temporary condition and later violations limit persistence. |
| `MT-N-024` / `006,012` | Identity plan and coercive job swap involve withheld information, threats and uninformed guild/clients. Eris stops protector's intimidation but demands faith. | Informed agency criterion: pragmatic benefit does not make agreement uncoerced. Slower alternatives were known. |
| `MT-N-025` / `011` | Ruijerd kills restrained man for kicking child; no-killing agreement achieved through reputation and children's fear. | Proportionate protection criterion rejects killing as automatic response. Later reported exploitation not his prior reason or retroactive justification. |
| `MT-N-026` / `010,013` | Returned pet, respected small payment, skilled pest control and equipment care meet real needs. | Attentive work deserves credit independently of fraud. Three days' good work not complete reform or compensation. |
| `MT-N-027` / `014` | Deliberate delay to maximize gratitude, expert warning ignored, Gablin killed; gratitude and mistaken praise follow. | Preventable-harm criterion: failed calculation culpable without intent to kill. Survivor's responsibility does not erase rescuer's independent choice. |
| `MT-N-028` / `015` | After death, comedy explicitly eases narrator distress; later consultation before harder battle improves judgment. | Formal relief neither repairs harm nor proves creator approval; actual local learning retained. |
| `MT-N-029` / `016` | Extortion pressure, evasion and perceived dead end culminate in flood decision/power gathering, interrupted. | Protective goal does not justify threatened indiscriminate harm; distinguish preparation from accomplished harm and earlier jokes. Imagined demand against Eris is Rudy projection. |
| `MT-N-030` / `017–018` | Ruijerd acts villain to free companions, public terror and official scapegoating; subsequent unconditional protection and chosen gratitude. | Prejudice wrong without innocence fiction; character's own coercion retained. Trust is not full confession or absolution. |
| `MT-N-031` / `019–020` | Meeting permits grievance and practical contribution; privacy violations persist but blocked, chore burden transferred; hidden decisions continue. | Agency and responsibility: meaningful social safeguard, incomplete internal change. Identity/misconduct equivalence in narrator summary is contestable. |
| `MT-N-032` / `020` | Nonlethal agreed duels, skill recognition and conversation produce limited respect; expulsions still occur. | Consent and proportionate conduct support particular encounters; no prejudice cure. |
| `MT-N-033` / `021` | Attractive court appearance conceals exploitative conduct; Derrick worries about reputation/political foes. | Status does not authorize use of less powerful people. Strategic criticism not complete affected-person access. |
| `MT-N-034` / `022` | Derrick sacrifices life, Ariel seeks care/accepts duty, unnamed girl saves her, dying man sees prayer fulfilled. | Care and courage locally supported; no successful-government proof or verified providential bargain. |

**`MT-NC-007`:** V02 N014/N016 → V03 N023/N031: distinguish actual comparable restraint, renewed intrusion and enforcement. Neither total incapacity nor settled consent practice fits. C002/model005.

**`MT-NC-008`:** V02 N010 → V03 N024/N027: staged/managed helplessness recurs despite previous near-fatal failure. Later irreversible death disproves safe transfer, not an intention to kill. C011/model003.

**`MT-NC-009`:** V03 N025/N027/N029: spontaneous protective killing, instrumental delayed rescue and prepared mass harm differ in actor, motive, opportunity and execution. No flat violence score; each has a specific responsibility question.

**`MT-NC-010`:** N023 versus N031: voluntary restraint and outside containment must not be credited to the same internal change mechanism; affected person's labor and continuing refusal remain visible. C002/C012.

**`MT-NC-011`:** N026/N030/N032: actual beneficial service, threatening identity performance and agreed duels produce different recognition. No pure hair-only experiment and no need to erase misconduct to condemn group persecution.


## V04 updates — 2026-09-26 UTC

Prior V01–V03 bodies remain historical and unchanged. Current scope is Japanese LN V01–V04; input is audited V03 head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Observation suffixes below resolve in [V04's diagnostic readings](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V04-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Event / observations | Conduct, capacity/power, access, tone and consequence | Analyst criterion / strongest qualification |
| --- | --- | --- |
| `MT-N-035` / `001,005` | Eleven-year-old Rudy's secret gift sacrifice challenged by protector; shared reasons change plan, Eris absent. | Informed agency: self-sacrifice can disregard others' stakes; correction real, transparency incomplete. |
| `MT-N-036` / `002` | Intrusion on Kishirika protested; extraordinary gift delivered painfully without Rudy's understood agreement; comic/toughness framing. | Bodily autonomy: help/reward not permission. Apparent age and reported biography distinct; non-graphic account only. |
| `MT-N-037` / `003–004` | Immediate stranger rescue, practice and sparring; teacher uses defeat to check pride, Eris voices unequal effort. | Attentive aid/pedagogy: real help, contested timing, gift and effort both causal; no guaranteed repair. |
| `MT-N-038` / `006–007` | Roxy search with fallible fear, companion diversion, destructive interruption/repair and omitted requests. | Responsibility proportional to each actual choice; no single-person blame or invented search success. |
| `MT-N-039` / `008` | Rudy11/Eris13; unpoliced illness restraint with promise/trust, then pressure over dependent care and limited permission. | Autonomy: actual restraint credited; later pressure not freely expanded blanket consent. Fantasy/comedy centers his struggle. |
| `MT-N-040` / `009–010` | Children rescued/healed, captors killed with Rudy's agreement/no-escape instruction; personal nonkilling self-account. | Proportionate force: rescuer's good purpose does not prove every killing necessary; delegated violence not innocence. |
| `MT-N-041` / `010,021` | Injured children receive practical help but gratitude demanded, gendered pain standard and sexualized appraisal; later spontaneous thanks. | Attentive noncoercive care: benefits real, consent/gratitude not interchangeable, visual inference no forensic finding. |
| `MT-N-042` / `011–012,019` | False arrest/mistreatment, failed hearing, comic jail advertisement; Ruijerd assumes warrior self-care; elder disputes. | Fair hearing/care: false accusation wrong despite prior collaboration; competence assumption not proof of actual capacity. |
| `MT-N-043` / `013–014` | Fire escape interrupted by immediate rescue, resentment subordinated, cooperative survival; allies killed, Gallus captured alive. | Preventable-harm/aid: unlike V03 no deliberate rescue delay; reward talk does not erase sequence. Victory not sole achievement or cancellation. |
| `MT-N-044` / `015` | Abduction market, treaty breach/bribery reports, formal apology and Eris retaliation; Boreas link suspected only. | Anti-coercion/proportionality: system matters; apology not full repair, harmful prior response not license for unlimited revenge. |
| `MT-N-045` / `016,021` | Eris holds back from striking Gyes; later partly moderates fight with younger friend and reconciles. | Proportionate response: distinct relation-conditioned restraint, no general nonviolence; partial friend account acknowledged. |
| `MT-N-046` / `017–020` | Asked-for village assistance, daily rescues, respect for pupil's teaching paired with voyeuristic concealment stopped by father. | Credit actual service/agency; external restraint not internal reform. False earlier accusation distinct from legitimate new privacy concern. |
| `MT-N-047` / `022` | Geese helps with vest/skill yet refuses Eris teaching based on reported old loss; care and exclusion. | Fair opportunity: grief explains superstition, not proof that teaching causes ruin. His own labor insecurity has independent stakes. |
| `MT-N-048` / `023–025` | Fitts about10, dependent displaced subordinate; Luke comforts, Ariel sexualized pressure explicitly difficult to refuse, then genuine shared comfort. | Autonomy: withdrawing as joke does not erase pressure; later comfort neither false nor evidence pressure necessary. Fitts's hope not tested guarantee. |
| `MT-N-049` / `024,026` | Enslaved young-presenting assassin exploited by Darius then sent to kill; Fitts lethal defense, injury/self-aid, status gain and ongoing attacks. | Slavery defeats inference of consent from acquiescence; exact assassin age unverified. Defense necessity differs from captive execution, no universal violence endorsement. |

**`MT-NC-012`:** N016/N023/N031 → N039/N046: new comparable unpoliced restraint, then pressure and external privacy enforcement. Real local change, incomplete transfer; C002/model005.

**`MT-NC-013`:** N027 → N037/N041/N043: engineered rescue delay, immediate aid and explicit gratitude demand coexist across different situations. Motive vocabulary alone cannot classify causal action; C011/model003.

**`MT-NC-014`:** N029 → N040/N042: prepared V03 flood, V04 denial of murderous intent, delegated killing and unexecuted jail escape thoughts differ. Preserve tension rather than adding completed violence or innocence.

**`MT-NC-015`:** N030/N035/N042/N048: supportive reliance can ease burden or impose it through warrior expectations and patron dependency. Distinct powers/ages/urgencies preclude exact equivalence; C012/C013.

**`MT-NC-016`:** N022 → N045: Eris's excessive retaliation compared with nonviolent mentor defense and partly moderated peer fight. Changed relation and actual actions matter; not all violence gone.

**`MT-NC-017`:** N016/N017/N039/N048: unwanted conduct, limited permission and dependent care recur across actors; affected-person access and comic framing differ. Neither gender nor protagonist status supplies a different consent rule. No overall endorsement or audience-effect claim.


## V05 updates — 2026-09-26 UTC

Prior V01–V04 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V05; frozen published input is audited V04 head `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. Observation suffixes below resolve in [V05's diagnostic readings](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V05-`. The [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) owns the historical cumulative synthesis; publication/audit remain separate from this preparation snapshot.

| Event / observations | Conduct, knowledge, power and framing | Criterion / strongest limit |
| --- | --- | --- |
| `MT-N-050` / `002–003` | Prompt child aid after bad experience, refusal to hear and misidentified rescuers; comic disguise. | Duty to aid and fair hearing both apply; no engineered delay, no automatically justified force. |
| `MT-N-051` / `004` | Paul confirms old assault and retaliatory motive, recalls remorse. | Bodily autonomy/agency; younger-self label is no excuse, current service no cancellation. |
| `MT-N-052` / `005–006` | Dependent child's care and collective rescue using privilege/force, deaths/opposition, later neglect. | Effective care credited; legal ownership is not moral consent; method criticism retained. |
| `MT-N-053` / `007` | Father assumes knowledge, strikes first; son retaliates excessively; Norn intervenes. | Asymmetric initiation and mutual excess; grief/talent do not justify force. |
| `MT-N-054` / `008,013` | Eris threatens revenge, Rui intervenes and causes bruise; comfort helps. | Proportionate force/care; exact restraint unseen, gendered duty and chosen concern coexist. |
| `MT-N-055` / `009,011` | Mediation, rest, care and shared reenactment enable mutual repair. | Informed participation differs from manufactured danger; no universal forgiveness. |
| `MT-N-056` / `010` | Survivor history accessible to reader; women work/protect, Rudy misreads and polices dress, men ignore discomfort. | Noncoercive attention/recognition; Paul's recovery appraisal is not proof, no diagnosis. |
| `MT-N-057` / `012` | New refusal-respecting resolve, reported negotiated household and education. | Intention is not persistence; later arrangement is not retroactive consent or necessity proof. |
| `MT-N-058` / `015,020` | Norn/Eris refusals remain after meal; father presses unity through fear. | Third parties' agency; time may help, without a guarantee. |
| `MT-N-059` / `018` | Eris intervenes then excessively hits Cliff; adult stops worse; she accepts reckless provocation. | Proportionality; comedy can lighten attention but does not erase action. |
| `MT-N-060` / `019` | Eris's first lethal rescue needs knight; fleeing attacker also killed; public calm/private fear. | Threat-specific necessity; bravery does not justify every killing. |
| `MT-N-061` / `016,021–022` | Thanks and valid letter fail to gain general acceptance; personal obligation wins an exception. | Equal treatment; real help without institutional reform; forgery problem does not excuse categorical hostility. |
| `MT-N-062` / `022` | Affectionate familial handling uncomfortable to Rudy; medicine improves Eris's options. | Welcome touch and care dependency differ; biological theory remains self-report. |
| `MT-N-063` / `023–024` | Parents' care perceived through tears; Roxy admits missed meeting, then chooses further search. | Particular recognition without cure/pure-motive claims; nostalgia does not exonerate Nokopara. |
| `MT-N-064` / `025` | Rudy abuses cook using status, companions remove him, he regrets; owner's view shows business loss. | Proportionality/repair; critique content does not license humiliation, later benefit unproved. |
| `MT-N-065` / `026–028` | Official risks aid, guards die in protection; investigator recognizes false claim then chooses noncorrection. | Particular loyalty is not impartial justice; known error creates a distinct repair responsibility. |

**`MT-NC-018`:** N027/N043/N050: delayed rescue versus immediate aid; promptness does not guarantee knowledge. C011 remains sensitive to the sequence of decisions.

**`MT-NC-019`:** N042/N048/N052–055: warrior, patron and capacity burdens versus concrete care. Different powers and urgencies retained; C012/C013.

**`MT-NC-020`:** N039/N046/N055–057/N064: particular restraint, new resolve and family repair versus other misconduct. No moral balance sheet or general cure; C002.

**`MT-NC-021`:** N026/N030/N061: personal service and scapegoat recognition versus religious/official exclusion; benefit does not equal group acceptance.

**`MT-NC-022`:** N010/N027/N055: concealed staging/delay versus mutually requested reunion. Performance alone cannot define coercion; C009.

**`MT-NC-023`:** N053/N063/N065: missed facts, resisted recognition and knowingly uncorrected error require different responsibility judgments; C003/C014.

**`MT-NC-024`:** N022/N045/N054/N059–060: Eris's loyalty, partial restraint, care, retaliation and defense operate under different conditions. No always-violent or always-justified rule.

Criteria remain analyst judgments, separate from character law, narrator comedy, author intention or reception. No explicit sexual reconstruction or simulated scenario involving minors is used.


## V06 updates — 2026-09-26 UTC

Prior V01–V05 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V06; frozen input is final audited V05 head `3dc6b173b044abdafc013dc989bd96914620d13d`. Observation suffixes below resolve in [V06's diagnostic readings](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V06-`. The [V06 disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews altered premises; the V01–V05 cumulative checkpoint remains historical. Publication/audit remain separate from this preparation snapshot.

| Event / observation | Conduct, conditions, affected access and framing | Criterion / bounded conclusion |
| --- | --- | --- |
| `MT-N-066` / `002,004` | Protective withholding, partial route briefing and interpreted advice; companions cooperate without full premise. | Informed participation; concern is plausible, consultation incomplete. |
| `MT-N-067` / `005–006` | Prompt nonlethal child rescue, technical failure and unresentful care; later identity/esteem management. | Aid and proportionality credited; later motive cannot rewrite intervention order, criticism of past conduct remains accurate. |
| `MT-N-068` / `007–008` | Slave-market indifference/objectification, royal coercion, family hostages and threatened sexual captivity. | Bodily freedom/agency; specific familial aid does not generalize, constrained soldiers not freely complicit in every act. |
| `MT-N-069` / `008–010` | Refuses slander of Roxy; craft admiration, instrumental apprenticeship, tolerated royal violence and effective force-based liberation. | Particular loyalty separate from universal virtue; beneficiaries do not erase victims or unequal accountability. |
| `MT-N-070` / `012–013` | Rudy rejects child separation/sexualized service, yet uses misleading identity and possession analogy; child recognizes him. | Welfare and choice; refusal is real, gratitude does not justify theft or make every assigned role voluntary. |
| `MT-N-071` / `014,018` | Recognition and care coexist with unwanted touching and continued intrusive attention. | Limited permission remains limited; protection/near death does not certify durable change. Non-graphic comparison only. |
| `MT-N-072` / `015–016` | Orsted attacks at information disclosure; companions protect, Rudy improvises and attempts indiscriminate force while gravely impaired. | Attacker responsible; no deserved punishment for curiosity. Prevention of collateral harm is not restraint; differs from deliberate V03 flood plan. |
| `MT-N-073` / `019–020` | Qualified disclosure, privacy around tears, mutual recognition and accepted independent departure. | Care and autonomy; truth of report not settled by good emotional result. |
| `MT-N-074` / `021–022` | Death reports and political sacrifice proposal; Ghislaine resists, Rudy returns decision authority to Eris. | Affected-person choice against instrumentalization; rebuilding needs remain real, motive includes possessiveness. |
| `MT-N-075` / `023–025` | Bereaved adolescent initiates intimacy; younger bodily age/adult memory/tutoring role, hesitation and parental scripts complicate choices. | Non-graphic agency/consent analysis; later love cannot authorize earlier violations, mutual future not actually agreed. |
| `MT-N-076` / `025–026` | Eris deliberately conceals destination for training; inadequate note misread as rejection. | Right to leave distinguished from communication responsibility; no evidence she knows resultant despair. |
| `MT-N-077` / `027–028` | Reward/reunion forgone for search; borrowed funds settle damage, private exception enables separate message mission. | Real costs and care without pure-motive or institutional-reform claim; news not yet delivered. |
| `MT-N-078` / `029–030` | Child's constrained service enthusiasm; Lilia history explicitly establishes assault resistance/aftermath and paternal alternative. | Bodily autonomy and meaningful options; context/later attachment do not excuse earlier harm, skill gains not necessity proof. |
| `MT-N-079` / `031` | Genuine maternal protection taken as validation of assigned future; rare embrace meets child's emotional need. | Love does not justify every choice; warm local repair retains control and untested future alternatives. |

**`MT-NC-025`:** N027/N050/N067 contrast delayed gratitude optimization, mistaken immediate aid and successful immediate aid with costs. Later image management does not erase the order of rescue.

**`MT-NC-026`:** N039/N046/N057/N070–071/N075 compare particular restraint/resolve and renewed boundary failure. Relationship, opportunity, vulnerability and actual action remain separate; no sexualized generated test.

**`MT-NC-027`:** N029/N072 compare deliberated protective devastation with impaired high-output attack. Neither is harmless intent, but they are not interchangeable evidence for one trigger rule.

**`MT-NC-028`:** N055/N066/N073/N076 compare mutually understood performance, protective secrecy, qualified disclosure and intentionally compressed departure information. Benevolent motive cannot replace shared premises; known error still differs from unknown interpretation.

**`MT-NC-029`:** N051/N057/N078–079 compare acknowledged assault/domestic continuity, new affected-person history and parenting. Later attachment does not alter past consent; a father choosing an alternative undermines inevitability arguments.

**`MT-NC-030`:** N061/N069/N074/N077 compare personal exception, court utility, proposed sacrifice and private maritime access. Effective benefit is distinct from fair institutions or general reform.

**`MT-NC-031`:** N048/N055/N063/N073/N079 compare care across unequal roles. Affection can be nontransactional while dependency or assigned usefulness persists; warmth alone does not resolve authority.

These are explicit analyst criteria, not claims about universal reader response, authorial intention or reception. Differences in power and knowledge remain part of each comparison.


## V07 updates — 2026-09-26 UTC

Prior V01–V06 bodies remain historical and unchanged. The current source boundary is Japanese LN V01–V07. The entering freeze used audited V06 head `0e72e531278055c0dbb7a6054285337a1cc37a93`; later repository reconciliation does not change that analytical input. Observation suffixes resolve in [V07](../02%20Sequential%20Readings/MT_V07_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V07-`. The [recognition checkpoint](../05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md) owns the focused comparison. Publication and exact-head audit are separate from content acceptance.

| Event / observation | Conduct, conditions, affected access and framing | Criterion / bounded conclusion |
| --- | --- | --- |
| `MT-N-080` / `001–005` | Suzanne invites a distressed younger traveler; party refuses to abandon one another, prompting Rudy's intervention. | Care and survival; meaningful recognition without responsibility to cure him or make all dangers acceptable. |
| `MT-N-081` / `006,012,018` | Sara's class mistrust arises from parental loss and reported noble nonresponse; Rudy gives reassurance despite known possible family connection. | Fair appraisal and informed trust; history explains distrust without proving every generalization, actual obstruction remains conjectural. |
| `MT-N-082` / `008–010,014,017` | Dangerous expedition, specialists and divided obligations; retreat carries an agreed penalty except for Rudy; later search weighs other lives. | Distributed responsibility; willingness to rescue matters, unlimited self-sacrifice is not the only ethical choice. |
| `MT-N-083` / `010–011,024` | Soldat apologizes for one misunderstanding but repeatedly provokes, damages property and tells Rudy to die; later explicitly apologizes for provocation. | Earlier abuse and later care both actual; later benefit does not turn abusive conduct into necessary treatment. |
| `MT-N-084` / `013,022` | Rudy heals children freely partly because unpaid medical costs could expose them to enslavement; Elise identifies a child-related reason for gratitude. | Access to aid and freedom; prompt assistance credited, commercial child labor and coercive institutions remain separate harms. |
| `MT-N-085` / `014–017` | Search, recovery of remains and rescue; Sara's own evasive/medical work keeps her alive. Rudy's reward fantasy follows action. | Care and bodily autonomy; gratitude does not authorize intimacy, rescue not solely his agency. |
| `MT-N-086` / `018–020,025` | Friendly purchase and attraction culminate in unsuccessful intimacy; adolescent ages, unclear alcohol capacity and concealed motives limit interpretation. | Non-graphic agency analysis: involuntary response is not wrongdoing, debt is not consent, later account establishes affection but not every shared understanding. No precise incapacity diagnosis. |
| `MT-N-087` / `021` | Rudy threatens a bartender and hits Soldat; self-recognition recalls previous abusive patterns. Soldat accepts blows and listens. | Actual aggression remains his action despite distress; received patience does not make intimidation harmless or compulsory. |
| `MT-N-088` / `022,025` | Elise combines paid effort, gratitude and useful interpretation, then reveals private bodily information while angry at Sara. | Compassion, accuracy and privacy require separate assessment; no infallible therapist or purely cynical worker model. |
| `MT-N-089` / `023–025` | Rudy's public demeaning speech is real; Sara's imagined prolonged ridicule is false. Her earlier denial was defensive, his condition unknown to her. | Harm, knowledge and repair opportunity distinguished; partial correction does not erase actual insult or force forgiveness. |
| `MT-N-090` / `024,026` | Soldat interrupts a suicidal act and offers accompaniment with no membership demand; Rudy accepts mobility and postpones bodily recovery efforts. | Immediate protection and usable choice; no romantic cure, permanent safety guarantee or clinical diagnosis. |
| `MT-N-091` / `025` | Suzanne seeks permission before telling Timothy; inquiry and apology planned but departure prevents conversation, fear inhibits pursuit. | Consent to disclosure and accessible repair; neither missed contact nor fear proves lack of love or accomplished reconciliation. |
| `MT-N-092` / `028–029` | Ariel responds to bullying by designing species/sex-targeted provocation inaudible to humans, Fitts defeats and humiliates opponents, attendants circulate selective account. | School protection/political ambition do not erase degrading means or manufactured reputational advantage; actual prior bullying remains. |
| `MT-N-093` / `030` | Recruitment plans treat strong people as political resources; Fitts has an independent emotional response. | Instrumental aims do not exhaust participants' motives, planned invitation not accepted allegiance. |

**`MT-NC-032`:** N076/N086/N089/N091 compare Eris's departure with Sara's conflict. Concealed destination and a defensive untrue motive are different acts; reader access, actual insult, witness inquiry and timing differ. No generic abandonment rule replaces these facts.

**`MT-NC-033`:** N055/N073/N080/N083/N090 compare care that enables renewed action. Earlier provocation is not retroactively therapeutic, and accepting one kind of help does not establish global security.

**`MT-NC-034`:** N050/N067/N085 compare prompt aid and later gratitude imagery with V03 delayed intervention. Initiative and mixed motives can coexist; consent remains separate from indebtedness.

**`MT-NC-035`:** N066/N076/N081/N088/N091/N092 distinguish protective secrecy, known contrary evidence, unauthorized intimate disclosure, permission-sensitive mediation and manufactured audience ignorance. C014 records the changed knowledge responsibilities.

**`MT-NC-036`:** N061/N069/N074/N084/N092 compare personal aid and effective protection with continuing institutional harm or coercive tactics. Local benefit does not establish fair systems or necessary means.

The criteria are explicit analyst judgments, not claims about universal readers or creator intent. Non-graphic choice summaries preserve youth, power, uncertainty and affected-person access; no generated sexual scenario is evidence.


## V08 updates — 2026-09-26 UTC

Prior V01–V07 bodies remain historical and unchanged. Current source boundary: Japanese LN V01–V08. Immutable entering input was final audited V07 `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. Numeric observation suffixes resolve in [V08](../02%20Sequential%20Readings/MT_V08_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V08-`. The [consent and institutional-power checkpoint](../05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md) owns the targeted comparison. Content acceptance, publication/audit and integration to main remain separate states.

| Event / observation | Conduct, power, affected access and framing | Criterion and bounded judgment |
| --- | --- | --- |
| `MT-N-094` / `001–003` | Official funding closure and reported death coexist with scattered survivors; messenger finally arrives. | Administrative finality does not establish survivor welfare; truthful delivery credited without rescue claim. |
| `MT-N-095` / `004–005` | Conditional cure promise redirects choice; sleeping touch violates access; curse and pleasure accounts remain distinct. | Informed choice/bodily autonomy; involuntary condition not fault, chosen intrusion remains misconduct. |
| `MT-N-096` / `006–009,017` | School privilege, bullying and false accusation; Fitts supplies testimony backed by force, politically favored students avoid expulsion. | Protection meaningful; selective enforcement and intimidation not fair process. |
| `MT-N-097` / `010–011,026–027` | Sylphiette values care and knows instrumental use; fears losing love, wants equality, actually refuses one suggestion. | Constrained agency; imagined accommodation not future consent, slave simile not legal status. |
| `MT-N-098` / `012,025` | Rudy shares technique and honors collaborator's refusal/private restriction. | Real local respect; comparison with captives disproves automatic generalization. |
| `MT-N-099` / `013–014` | Collaborative production plan uses slave purchase; group rebukes sexist remark while accepting ownership. | Better diagnosis does not legitimate objective; legal normality not consent or necessity. |
| `MT-N-100` / `014–015` | Market neglect, fetters and threatened blow; Fitts cares, Rudy blocks blow then offers death through projected despair. | Aid credited; child refusal of death cannot authorize purchase/labor. |
| `MT-N-101` / `016` | Treatment, food, naming, no branding and pupil status within continued ownership. | Improved conditions distinct from freedom; unintelligible naming question not informed choice. |
| `MT-N-102` / `018–020` | Broken property, planned retaliation, explicit Elinalise objection, overwhelming victory. | Proportionality and bodily security; no-killing decision limits one harm without licensing others. |
| `MT-N-103` / `021` | Bound girls assaulted under medical pretext; fear/anger explicit, youth/power imbalance retained non-graphically. | Consent absent; no intercourse/no cure does not erase assault; graphic reproduction unnecessary. |
| `MT-N-104` / `022` | Repairable figure reduces anger; acknowledged criminality followed by deterrence; mutilation/sale rejected. | Selective limits real, recognition insufficient; repaired object not repair owed to persons. |
| `MT-N-105` / `023` | Consultation follows minimized account; Fitts urges release, yet day-long deprivation and threats have produced submission, followed by further punishment. | Captive agreement not free affiliation; help-seeking can coordinate abuse. |
| `MT-N-106` / `024–025` | Washable marks described as permanent; fear helps silence complaint; narration closes pleasantly. | Reversible injury and coercive fear differ; public quiet not informed vindication. |
| `MT-N-107` / `026–027` | Withheld name, attendants' false assumption, recruitment interest and fear of instrumental appearance. | Clarification responsibility without forcing disclosure; affection and political use coexist. |
| `MT-N-108` / `028` | Juli fears teachers despite care; girls' sociability and status shield Rudy from bullying. | Direct blows not sole harm route; later contact not retroactive consent; ownership persists. |
| `MT-N-109` / `030` | Overloaded meal demand challenged by Zanoba/Fitts, followed by offered choice, effort and praise. | Better instruction and possible joy credited; observer cannot certify free consent or full confidence. |

**`MT-NC-037`:** N092/N096/N102–106 compare school bullying, strategic humiliation and captive punishment. Prior wrongdoing supplies responsibility for property harm, not permission for assault; unequal enforcement remains visible.

**`MT-NC-038`:** N098/N103/N105 compare respected privacy with violated bodily autonomy. The interests differ in scale, but same-volume conduct establishes selective use of permission rather than universal inability to understand refusal.

**`MT-NC-039`:** N084/N099–101/N109 compare free aid, purchase, protection and teaching. Improvement of a child's situation is real without becoming a free labor agreement; no counterfactual proof of enslavement's necessity.

**`MT-NC-040`:** N097/N101/N107–109 compare service, ownership and pupil care without collapsing legal status. Affection may be chosen within dependency; hypothetical marriage concessions and a child's smile cannot certify future/free agreement.

**`MT-NC-041`:** N089/N104/N106/N108 compare actual interpersonal injury with correction of information, repaired property and public silence. C015 records the missing repair outcome; complaint constrained by fear cannot validate closure.

These are explicit analyst criteria. No creator-intention, universal reception, diagnosis or generated sexual scenario is claimed.
