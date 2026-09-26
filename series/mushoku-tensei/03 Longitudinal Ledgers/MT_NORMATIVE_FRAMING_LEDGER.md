---
title: "Mushoku Tensei - Normative framing ledger"
artifact_id: MT_NORMATIVE_FRAMING_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V04 only; prior history preserved, V04 candidate updates; publication/audit separate."
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
