---
title: "Mushoku Tensei - Character state and readiness ledger"
artifact_id: MT_CHARACTER_STATE_AND_READINESS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.14"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V14 only; prior history preserved, V14 updates; publication/audit separate."
---

# Character state and readiness ledger

## Responsibility

Owns observed state changes, local character keys, evidence coverage and bounded model readiness by domain. It does not create global entity IDs or duplicate the operational reconstruction model.

## Record format

`state event ID | local key | source observation refs | prior state | observed change | change kind | new information versus disposition | persistent features | uncertainty; readiness: local key | state/source boundary | contexts | supported domains | missing contexts | counterexamples | validation | model path`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append source-bearing state events; revise current readiness only when an evidence review warrants it, preserving the prior state and reasoning. Leave global IDs null until curation establishes them. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

All events are bounded to `MT-LNJP-V01` and cite observations in the [accepted V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). Local keys are **not** global character IDs. Each current assessment retains its stated V01 evidential limits; prior zero state above remains historical.

| State event ID / local key | Prior → observed change and kind | Basis / uncertainty |
| --- | --- | --- |
| `MT-S-001` / `Rudeus` | Reported isolation and fear → daily magic practice and ability; changed activity/skill, not demonstrated global ethical reform. | `001,003,005`; self-reported prior biography and short experimental series limit causal and population inference. |
| `MT-S-002` / `Rudeus` | Home/garden limit → accompanied trip, then voluntarily steps beyond gate; situational avoidance reduced. | `008`; no clinical diagnosis or proof that every social setting is now safe. |
| `MT-S-003` / `Rudeus` | Protector/teacher role → overrides Sylphie's refusal, recognizes wrong, apologizes, then later imagines shaping her future; conflicting boundary responses. | `009,011–012,015`; recognition and temporary restraint observed, durability untested. |
| `MT-S-004` / `Lilia` | Suspicion/aversion of infant → respect and extreme debt framing after family meeting; belief/relationship revision. | `004,013`; her own earlier employment history and self-blame matter. The proposed future service by Aisha is not Aisha's consent. |
| `MT-S-005` / `Roxy` | Teacher with limited local prospects → recognized village worker, departure for further practice, later reports higher rank and another teaching post. | `006–008,015`; letter is her report, not independently observed offstage experience. |
| `MT-S-006` / `Paul` | Headstrong teacher initially acts on accusation → apologizes and in a later case asks about Sylphie's refusal; partial parenting practice change. | `010–012`; later forced removal `016` is substantial contrary evidence to a generalized noncoercion rule. |
| `MT-S-007` / `Zenith` | Betrayal and contemplated departure → chooses Lilia's continued place and feeds Aisha; chosen care with unresolved religious tension. | `013–014`; her first-person extra supplies reasons but not a durable harmony guarantee. |
| `MT-S-008` / `Sylphie` | Isolated target → initiates friendship/learning, practices silent magic, asserts refusal, remains cautious, protests separation. | `009,011–012,016`; strong observable action, little direct interior narration. |
| `MT-S-009` / `Ghislaine` | New arrival as a sword expert → requests literacy/number instruction as part of exchange. | `016`; her self-account and full instructional practice are not yet present. |

### Current bounded readiness

| Local key | Supported domains through V01 | Missing contexts / standalone model decision |
| --- | --- | --- |
| `Rudeus` | Study/experimental response, failure management, selected family care, conflict rhetoric, fear at gate, some ethical self-correction. | No stable response model across independent contexts, sustained consent practice, employment, equal-power intimacy, or later consequences. **Standalone operational model deferred.** His claim to a numerical mental age is self-description only. |
| `Lilia` | Safety/pay decision, household labor, changed judgment of Rudeus, self-blame in crisis. | Thin access to life outside house and later motherhood. Model deferred. |
| `Roxy` | Adaptive pedagogy, paid work, treatment of error, chosen continued education. | Offstage new post is only letter report; broader relational contexts absent. Model deferred. |
| `Paul` | Sword teaching, mistaken discipline and apology, expressed dependence concern, coercive separation. | Competing motives and untested consequences prevent a general parenting rule. Model deferred. |
| `Zenith` | Faith, family boundary, practical healing/care, response to betrayal, chosen feeding of Aisha. | Extra is a first-person self-account; future stability and work outside house sparsely observed. Model deferred. |
| `Sylphie` | Independent learning request, repeated practice, refusal and avoidance, abandonment protest. | Her developing goals and peer world beyond Rudeus are not sufficiently accessible. Model deferred. |
| `Ghislaine`, `Norn`, `Aisha`, `Rolls` | Limited encounter or represented need/choice only. | No standalone reconstruction warranted; retain local keys without global enrollment. |

## V02 state events and current readiness — 2026-09-26 UTC

The preceding table is the preserved **V01** readiness snapshot, not the latest assessment. V02 source observations are in [the complete V02 reading](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings); numbers below resolve as `MT-E-LNJP-V02-NNN`. Input is audited V01 commit `eaf159559c6fc76ddd820178d7588545f08c351d`.

| State event / local key | Prior → represented change / kind | Evidence, persistent feature and limit |
| --- | --- | --- |
| `MT-S-010` / Rudeus | Prospective employee → practicing tutor, coordinator and language learner. COMPETENCE / CONTEXT_CHANGE. | `001–003,006–012`: preparation, adapting instruction, using others' expertise, social access; manipulation persists. No global maturation score. |
| `MT-S-011` / Rudeus | V01 uneven self-restraint → one gift-related restraint, later violation, recognition/apology, commitment framed as future reward. UNRESOLVED persistence. | `006,009,014`: recognition is real, transfer failed at least once; renewed promise has no subsequent comparable opportunity here. |
| `MT-S-012` / Eris | Resists younger tutor → chooses learning, develops distinct skills, initiates gifts and celebration, asserts boundaries. RELATIONSHIP / COMPETENCE_CHANGE. | `002–009,012,014`: voice and force persist; defensive blows distinguished from arbitrary aggression. No direct complete interior account. |
| `MT-S-013` / Ghislaine | V01 rank/request only → demonstrated protector, effective teacher and learner with ordinary thought and ambitions. REVEALED_NOT_NEW plus COMPETENCE_CHANGE. | `001,003,006–011`: patient study changes practical options; rank did not prevent fraud/hunger. Own biased judgments remain. |
| `MT-S-014` / Ghislaine | Household protective routine → displaced, disoriented combat and urgent search. CONTEXT_CHANGE. | `017,019`: survives initial displacement; berserk violence interrupts a generic controlled-protector rule. Eventual homecoming unestablished. |
| `MT-S-015` / Roxy | Distant reported teacher → authored guide, observed refusal/exit, then self-chosen search. REVEALED_NOT_NEW / KNOWLEDGE / CONTEXT_CHANGE. | `010,015,018`: independent goals, teaching doubt, revised assumptions about camp grief. Hope is not successful recovery. |
| `MT-S-016` / Hilda | Apparent hostility → protective embrace; Philip supplies an explanation in separation from sons. RELATIONSHIP_CHANGE / REVEALED_NOT_NEW. | `012–013`; behavior direct, motive/backstory mediated. Do not diagnose or equate marriage pressure with freely granted choice. |
| `MT-S-017` / Philip, Sauros | Kinship employers → differentiated political and affective roles. REVEALED_NOT_NEW. | `004–005,008,012–013`: gratitude, violence, succession strategy and care overlap; outcomes after disaster unknown. |
| `MT-S-018` / Paul, Norn, Zenith, Lilia, Aisha | Stable household at prior boundary → Paul reports Norn with him, others missing, organizes search. KNOWLEDGE / CONTEXT_CHANGE. | `018`; public message read by Roxy, not shown received by Rudy. No observation of all persons' current states. |
| `MT-S-019` / Vigo | Mercenary identifies acquired homeland as worth dying for → survives intervention and memorializes rescuer. CONTEXT / SELF-APPRAISAL_CHANGE. | `019`; independent extra narrative, no invented knowledge of Ghislaine's eventual fate. |

| Local key / domain | Current readiness through V02 | Counterevidence / validation debt / operational home |
| --- | --- | --- |
| Rudeus: ordinary study, tutoring, coordination | BOUNDED_PROVISIONAL; multiple tasks and relationships now represented. | Retrospective fit only; severe context change at ending. Sexual restraint, politics and post-disaster adaptation not DOMAIN_READY. No standalone model promoted; V02 K/L names the next calibration review. |
| Ghislaine: teaching/learning, protective household work | BOUNDED_PROVISIONAL; action, dialogue, interiority and ordinary preferences available. | Accurate advice coexists with biased appraisals; disorientation/indiscriminate combat limits transfer. No tested operational model. |
| Eris: task-specific learning and chosen reciprocity | BOUNDED_PROVISIONAL for observed household contexts. | Limited interior access; performance, consent, cooperation and dependence must remain separate. Novel situations INSUFFICIENT_EVIDENCE. |
| Roxy: instruction, workplace refusal, route deliberation | BOUNDED_PROVISIONAL. | Relationship idealization and fallible assumptions; no successful-search evidence or out-of-domain validation. |
| Hilda, Philip, Sauros, Paul | Supported local actions and reported constraints; broad reconstruction INSUFFICIENT_EVIDENCE. | Uneven focalization and missing aftermath. |
| Sylphie, Zenith, Lilia, Norn, Aisha | V01 readiness limits preserved; new availability/knowledge statuses only where sourced. | No current inner states inferred from absence, missing-person status or Rudy's recollection. |
| Orsted, Perugius, Gal, Kishirika, Arumanfi, Vigo and other new figures | Encounter-specific actions only. | No generic persona, prophecy or unshown future imported. Global IDs remain null; no registry enrollment. |


## V03 updates — 2026-09-26 UTC

Prior V01/V02 bodies remain historical and unchanged. Current scope is Japanese LN V01–V03; input is audited V02 head `687a13ac1a661270ab566c9e1a6028acd607d846`. Observation suffixes below resolve in [V03's diagnostic readings](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V03-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Event / local key | Prior → represented change / kind | Basis, persistence and limits |
| --- | --- | --- |
| `MT-S-020` / Rudeus | Household tutor → displaced party coordinator, language mediator and novice worker. CONTEXT_CHANGE / COMPETENCE_CHANGE. | `001–007,013`: skills useful but excessive magic, unfamiliar prices/rules and dependence prevent generic mastery. |
| `MT-S-021` / Rudeus | Apparent control of mockery/performance → direct intimidation revives fear; money worry reveals earlier parental burdens. REVEALED_NOT_NEW / KNOWLEDGE_CHANGE. | `007,009,011–012`; village-gate improvement never established universal recovery. No diagnosis. |
| `MT-S-022` / Rudeus | Manufactured gratitude seems manageable → delayed rescue causes Gablin's death, defensive justification then acknowledgment. KNOWLEDGE_CHANGE / UNRESOLVED disposition. | `014–015`; others' false favorable explanation does not certify his motive; relief and regret coexist. |
| `MT-S-023` / Rudeus | Exposure of job scheme → contemplates betrayal and prepares town flood, interrupted by Ruijerd; accepts protection without payment. CONTEXT / RELATIONSHIP_CHANGE. | `016–018`; no flood executed; incomplete disclosure, actual gratitude, continuing outburst. |
| `MT-S-024` / Rudeus | Private decisions → consultative travel routine and limited skill calibration. COMPETENCE / RELATIONSHIP_CHANGE. | `019–020`; hidden decisions and externally stopped violations remain, not blanket ethical reform. First bounded model linked below. |
| `MT-S-025` / Eris | Household pupil → frightened displaced partner, adaptable camper and protective companion. CONTEXT_CHANGE. | `002,005,008–009,012`; affection and care coexist with severe retaliation and overconfidence in Rudy. |
| `MT-S-026` / Eris | Limited participation/language → supplies market research, asserts privacy grievance, initiates language study, improves combat. COMPETENCE / AGENCY_CHANGE. | `019–020`; task-specific learning, no universal compliance or full interior access. |
| `MT-S-027` / Ruijerd | Feared stranger → disclosed former leader and protector with reparative goal. REVEALED_NOT_NEW. | `002–005`; war history attributed, current threats observed, survival of other Superd unknown. |
| `MT-S-028` / Ruijerd | Categorical killing/protection → agreed restraint, recognition of workers and young warriors, costly scapegoat performance and unconditional escort. KNOWLEDGE / RELATIONSHIP_CHANGE. | `011–015,017–018`; mistaken credit to Rudy, unstable child/warrior boundary and threatening tactics limit general reform. |
| `MT-S-029` / Ruijerd | Disguised outcast → shaved appearance, consultation and nonlethal duels. CONTEXT / PRACTICE_CHANGE. | `018–020`; some welcome and respect, continued exclusion; no eradicated prejudice. |
| `MT-S-030` / Roxy, Rowin, Rokari | Earlier teacher/absent daughter → parents' concern and communication exclusion disclosed; gifts and news exchanged. REVEALED_NOT_NEW. | `003`; Roxy not directly encountered now, earlier letters not current location guarantee. |
| `MT-S-031` / Jalil, Veskel, Kurt, Meisel | New local actors with work, fear, gratitude and independent judgments. ENCOUNTER / KNOWLEDGE_CHANGE. | `008,010,012–014,017`; good work does not erase wrongs; sincere thanks can coexist with incomplete knowledge or prejudice. |
| `MT-S-032` / Ariel, Derrick, Luke, unnamed girl | Court comfort/loyalty → fatal defense, Ariel accepts crown ambition, unnamed arrival saves her. CONTEXT / COMMITMENT_CHANGE. | `021–022`; Derrick dies; future government and newcomer's identity withheld. No Sylphie state update inferred. |

| Local key / domain | Current readiness through V03 | Operational home / calibration debt |
| --- | --- | --- |
| Rudeus: learning, ordinary coordination, familiar-party relations, written public/private register | BOUNDED_PROVISIONAL; source variety now supports explicit conditional rules. | [First reconstruction model](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md) and [evidence index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md). Retrospective fitting, no clean holdout, no DOMAIN_READY claim. |
| Rudeus: high-stakes judgment and boundary respect | Diagnostic failures and one comparable restraint observed; reliable extrapolation INSUFFICIENT_EVIDENCE. | Do not convert outside enforcement or thanks into internal moral reliability. Model negative constraints apply. |
| Eris: task-specific learning, travel cooperation/refusal, care | BOUNDED_PROVISIONAL across household and journey. | Contradictory violence and idealization; full motives unavailable. Standalone operational calibration still deferred. |
| Ruijerd: protection, warrior classifications, practical teaching, reputation | BOUNDED_PROVISIONAL within V03; repeated ordinary and conflict cases. | History largely his report; variable category boundaries and mistaken appraisals. No broad persona promoted. |
| Roxy / Ghislaine / Paul / absent family | V02 domain limits retained; Roxy history newly reported. | No direct new present conduct of Ghislaine/Paul/Zenith/Lilia/Aisha/Norn/Sylphie; do not fill gaps from the extra's unnamed girl. |
| Ariel, Derrick, Luke and other local people | Encounter-specific support; broad modeling INSUFFICIENT_EVIDENCE. | Derrick has direct interiority but one bounded episode; future political capability untested. |

Global character/entity IDs remain null. The living model is a new limited analytical responsibility, not a mature monograph or automatic registry enrollment. V05 must review its calibration and missing domains.


## V04 updates — 2026-09-26 UTC

Prior V01–V03 bodies remain historical and unchanged. Current scope is Japanese LN V01–V04; input is audited V03 head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Observation suffixes below resolve in [V04's diagnostic readings](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V04-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Event / local key | Prior → represented change / kind | Basis, persistence and limit |
| --- | --- | --- |
| `MT-S-033` / Rudeus | Wenport arrival → gifted foresight, practiced calibration and corrected confidence. COMPETENCE / KNOWLEDGE_CHANGE. | `001–005`: expertise accepted in some decisions, secret staff sale requires interruption; power does not ensure interpretation. |
| `MT-S-034` / Rudeus | Prior mixed restraint → actual unpoliced care/restraint during illness, followed by pressure. PRACTICE_CHANGE / persistence UNRESOLVED. | `008`; later intrusion `018/021` prevents universal transfer. |
| `MT-S-035` / Rudeus | Smuggling collaborator → rescuer participating in killing, then wrongly accused prisoner. CONTEXT_CHANGE / conflicting SELF_ACCOUNT. | `009–012`; personal reluctance to kill differs from assistance, orders and prior flood preparation. |
| `MT-S-036` / Rudeus | Resentful escape planning → immediate child rescue, chosen aid and joint survival. CONTEXT / PRACTICE_CHANGE. | `013–014`; no engineered delay, no sole victory; fear and limited self-sacrifice remain. |
| `MT-S-037` / Rudeus | Honored guest → daily guard, learner, maker and companion; privacy intrusion continues. CONTEXT / KNOWLEDGE_CHANGE. | `015–022`; recognizes others' independent development and his protector's excessive expectations. |
| `MT-S-038` / Eris | Confident trainee → gift-related grievance and dependent illness; continued practice. CONTEXT_CHANGE. | `003–004,008`; gains in spoken language do not imply literacy; physical aptitude/task limits distinct. |
| `MT-S-039` / Eris | Travel pupil/companion → nonviolent defense of Ghislaine, peer teacher/friend and partial restraint in quarrel. COMPETENCE / RELATIONSHIP_CHANGE. | `016,018,021–022`; still retaliates, reconciliation partly unobserved. First bounded model below. |
| `MT-S-040` / Ruijerd | Earlier consultation → costly relational correction, revised smuggling position and agreed village assistance. PRACTICE / KNOWLEDGE_CHANGE. | `005,017`; asks others, does not fully abandon pride appraisal. |
| `MT-S-041` / Ruijerd | Trusted protector → killer of captors and rescuer of many, but mistaken about Rudeus's independent capacity. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `009,011,015,019`; warrior classification distributes care unevenly; cultural claims not universal facts. |
| `MT-S-042` / Roxy | Chosen search → new party, own memories/goals, rumor-driven missed encounter and costly mistakes. CONTEXT / REVEALED_NOT_NEW. | `006–007`; real ability and ongoing romantic wishes coexist; no reunion. |
| `MT-S-043` / Geese | New prisoner → warm practical helper, weak fighter, skilled cook and temporary companion. REVEALED_NOT_NEW. | `012,014,022`; old loss self-reported, no named former couple or permanent Dead End membership. |
| `MT-S-044` / Gyes | Misidentification/harsh detention → apology, cooperation and reconsidered sister judgment; still protects daughter's privacy. KNOWLEDGE / PRACTICE_CHANGE. | `011,015–018`; apology not complete institutional repair, childhood account not erased. |
| `MT-S-045` / Fitts | Displaced child → competent court worker/defender with nightmares, dependence and later specific relief. CONTEXT / COMPETENCE_CHANGE. | `023–026`; alias retained, earlier identity unresolved; nightmare cessation not full recovery or proof of cause. |
| `MT-S-046` / Ariel, Luke | Earlier crisis → daily care, political preparation and repeated danger. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `023–026`; Ariel's teasing/utility and Luke's failed support coexist with actual comfort; no successful reign/escape narrated. |

| Local key / domain | Current readiness through V04 | Operational route / debt |
| --- | --- | --- |
| Rudeus: learning, party coordination, written register | BOUNDED_PROVISIONAL; new source checks revise existing rules. | [Model](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md)/[index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md); V04 read after V03 rules, no clean holdout or registered outcome prediction. |
| Rudeus: high-stakes judgment / durable boundary respect | Reliable extrapolation INSUFFICIENT_EVIDENCE. | Actual aid/restraint plus continuing harm; avoid universal coward, strategist, predator-only or benevolent-only outputs. |
| Eris: learning, particular loyalties/refusal, peer interaction | BOUNDED_PROVISIONAL; repeated household/travel contrasts warrant a first restricted model. | [Model](../04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md)/[index](../04%20Character%20Analysis/eris/EVIDENCE_INDEX.md). Peer repair one extended cluster; retrospective fit, no DOMAIN_READY. |
| Ruijerd, Roxy | BOUNDED_PROVISIONAL for observed work/care/appraisal domains, not general predictive reliability. | Shared ledger remains operational boundary; V05 cumulative review to examine model activation/calibration. |
| Geese, Gyes, Fitts, Ariel, Luke | Supported particular choices/contexts; broader reconstruction INSUFFICIENT_EVIDENCE. | Biographical reports, alias limits and sparse comparison prevent broad personas. |
| Ghislaine and absent family/Sylphie | Prior readiness retained; Ghislaine's childhood newly reported, no current encounter. | No state inferred from unresolved identities, memories or absence. |

Global IDs remain null; no curation enrollment, mature monograph or unqualified simulation readiness is claimed.


## V05 updates — 2026-09-26 UTC

Prior V01–V04 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V05; frozen published input is audited V04 head `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. Observation suffixes below resolve in [V05's diagnostic readings](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V05-`. The [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) owns the historical cumulative synthesis; publication/audit remain separate from this preparation snapshot.

| Event / local key | Prior → represented change / kind | Evidence and limit |
| --- | --- | --- |
| `MT-S-047` / Rudeus | Coordinating arrival → misidentified rescue/father fight, first whole-region disclosure. CONTEXT / KNOWLEDGE_CHANGE. | `001–003,007`; immediate duty and missed hearing coexist; actual information differs from Paul's assumption. |
| `MT-S-048` / Rudeus | Hurt withdrawal → received care, embodied perspective reversal and particular reunion. RELATIONSHIP / KNOWLEDGE_CHANGE. | `008–013`; intellectual apology initially unusable; no general cure or durable consent proof. |
| `MT-S-049` / Rudeus | Repaired dyad → revised search/return plan, partial empathy, later cook-directed outburst. PRACTICE / CONTEXT_CHANGE. | `010,012,014–016,020–022,025`; misreading and excessive authority persist. |
| `MT-S-050` / Paul | V01 history → newly reported pre-disaster correction and observed retrospective care/search. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `004–005`; assault motive admitted, Norn need concrete, multiple people's resources causal. |
| `MT-S-051` / Paul | Active search → uncertainty, drinking/neglect and excessive demand at reunion. CONTEXT_CHANGE. | `005–007,015`; feared family deaths not facts, no diagnosis; initiates blow. |
| `MT-S-052` / Paul | Challenged assumption → listens, revises child/capability appraisal, apologizes, resumes work/offers options. KNOWLEDGE / RELATIONSHIP / PRACTICE_CHANGE. | `009–015,020`; relapse history and unrepaired Norn/Eris relations prevent global reform. |
| `MT-S-053` / Eris | Observed companion → independent wish, notice knowledge, skill and first human killing disclosed. REVEALED_NOT_NEW / COMPETENCE / CONTEXT_CHANGE. | `017–019`; thought access newly available, taunt/violence/support limits retained. |
| `MT-S-054` / Eris | Protective anger → awkward comfort, continued dissent, meal and debt-based passage. RELATIONSHIP_CHANGE. | `008,013,015,020,022`; no automatic forgiveness, bruise encounter partly unavailable. |
| `MT-S-055` / Ruijerd | Warrior-demand tension → listens/supports reunion, restrains Eris, reconnects with old beneficiary. PRACTICE / REVEALED_NOT_NEW. | `008,013–016,021–022`; degree of force unresolved, institutional expertise limited. |
| `MT-S-056` / Roxy | Search near miss → parental reunion, admitted identification error, continuing search. KNOWLEDGE / RELATIONSHIP_CHANGE. | `023–024`; telepathy unchanged, pupil idealization persists; no present pupil reunion. |
| `MT-S-057` / Sylphie | Missing post-separation development → Paul reports exercise, several teachers and silent healing before catastrophe. REVEALED_NOT_NEW. | `012`; not current encounter or proof forced ban necessary; identity/location still unknown. |
| `MT-S-058` / Vera, Shela | Rudy's sexual/dislike account → reader receives trauma history and observes protective/administrative work. REVEALED_NOT_NEW. | `010,014–015`; Paul report bounded; fear continues alongside competence. |
| `MT-S-059` / Norn | Earlier infant → displaced child attached to father, rejects attacking brother. CONTEXT / REVEALED_NOT_NEW. | `004–007,015,020`; refusal survives men's reunion, age estimates not forced precise. |
| `MT-S-060` / Geese | Helpful traveler → old-party mediator and renewed searcher; jail initiative reported. REVEALED_NOT_NEW / PRACTICE_CHANGE. | `009,020`; jinx/withholding motives incomplete. |
| `MT-S-061` / Therese | Rescued knight → authority/kinship assistance and personal demon exception. KNOWLEDGE / RELATIONSHIP_CHANGE. | `019,021–022`; retains prejudice; not universal ally. |
| `MT-S-062` / Cliff | Praised novice → failed coordination, admiration, refused proposal and reported relocation. CONTEXT / KNOWLEDGE_CHANGE. | `018–019`; pride persists, destination not supplied here. |
| `MT-S-063` / Fitts, Ariel, Luke | Announced flight → testimony of border/attack and corrected death rumor. CONTEXT / KNOWLEDGE_CHANGE. | `026–028`; Fitts identity unresolved, resourceful defense needs allies; later rule unknown. |
| `MT-S-064` / Randolph | Struggling inherited business → shame and accepted recruitment after outburst. CONTEXT / DECISION_CHANGE. | `025`; martial status does not settle welfare of new career. |
| `MT-S-065` / Gustav | Confident investigator → mistaken report, recognized contradiction and chosen noncorrection. KNOWLEDGE / PRACTICE_CHANGE. | `026–028`; self-interest explicit, announced political effects not yet narrated. |

| Local key / domain | Current readiness and home | Calibration limit |
| --- | --- | --- |
| Rudeus / learning, coordination, register and particular repair | BOUNDED_PROVISIONAL; [model1.2](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md). | Six new diagnostic checks; durable boundaries/high-stakes reliability insufficient, no clean holdout. |
| Eris / practical learning, loyalty/refusal, independent appraisal | BOUNDED_PROVISIONAL; [model1.1](../04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/eris/EVIDENCE_INDEX.md). | Four new checks; general regulation/peer-repair transfer unproved. |
| Paul / caregiving, capability expectations, correction | First BOUNDED_PROVISIONAL [model](../04%20Character%20Analysis/paul/RECONSTRUCTION_MODEL.md)/[index](../04%20Character%20Analysis/paul/EVIDENCE_INDEX.md). | Relation-conditioned rules, no durable sobriety or universal noncoercion. |
| Ruijerd / protection, classification, instruction, friendship | First BOUNDED_PROVISIONAL [model](../04%20Character%20Analysis/ruijerd/RECONSTRUCTION_MODEL.md)/[index](../04%20Character%20Analysis/ruijerd/EVIDENCE_INDEX.md). | History/testimony limits, no infallible judgment or hidden-motive certainty. |
| Roxy / professional pride, teaching/search, communication | First BOUNDED_PROVISIONAL [model](../04%20Character%20Analysis/roxy/RECONSTRUCTION_MODEL.md)/[index](../04%20Character%20Analysis/roxy/EVIDENCE_INDEX.md). | Family repair local; no reliable search forecast or general romance persona. |
| Others / admitted contexts | Preserve bounded ledger descriptions; no new broad package. | Sylphie/Zenith/Lilia partly reported; Geese motive gaps; court aliases/limited comparison; affected-person access uneven. |

No DOMAIN_READY, mature monograph or global enrollment. The checkpoint documents why the cumulative argument stays there and why these three operational responsibilities are newly distinct.


## V06 updates — 2026-09-26 UTC

Prior V01–V05 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V06; frozen input is final audited V05 head `3dc6b173b044abdafc013dc989bd96914620d13d`. Observation suffixes below resolve in [V06's diagnostic readings](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V06-`. The [V06 disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews altered premises; the V01–V05 cumulative checkpoint remains historical. Publication/audit remain separate from this preparation snapshot.

| Event / local key | Prior → represented change / kind | Evidence and limit |
| --- | --- | --- |
| `MT-S-066` / Rudeus | Revised V05 travel → partial family detour disclosure, ordinary experimentation and inaccurate court plan. CONTEXT / KNOWLEDGE_CHANGE. | `001–004`; age twelve, advice interpreted beyond wording, learning not omniscience. |
| `MT-S-067` / Rudeus | Immediate rescue → concealed brotherhood, trap and dependence on independent rescuers. CONTEXT / RELATIONSHIP_CHANGE. | `005–013`; particular loyalty/refusal, self-credit minimized, Aisha misread. |
| `MT-S-068` / Rudeus | Confident approach → catastrophic defeat, external survival, qualified disclosure and modest technical adaptation. CONTEXT / KNOWLEDGE / PRACTICE_CHANGE. | `015–020`; dreamlike aftermath self-reported, no general recovery or verified curse cosmology. |
| `MT-S-069` / Rudeus | Return with imagined future → family loss, decision-right advocacy, misunderstood departure and self-condemnation. CONTEXT / RELATIONSHIP_CHANGE. | `021–026`; useful reconstruction and renewed search survive distress; Eris's intention unavailable. |
| `MT-S-070` / Eris | V05 learner/companion → sustained practice and warrior recognition, then protective intervention and traumatic defeat. COMPETENCE / CONTEXT_CHANGE. | `014–018`; local recognition not universal invulnerability; birthday fifteen retrospectively identified. |
| `MT-S-071` / Eris | Earlier outward confidence → disclosed inferiority, fear of replacement and repeated idealization. REVEALED_NOT_NEW. | `024`; access changes now, motives do not suddenly originate now; own claims sometimes incorrect. |
| `MT-S-072` / Eris | Grief and dependence → seeks family bond, chooses training, rejects noble role and withholds destination. RELATIONSHIP / DECISION_CHANGE. | `021–025`; intended future partnership differs from received message; no achieved training outcome. |
| `MT-S-073` / Ruijerd | Protective companion → practical care, hostage rescue, defeat and demand for relevant disclosure. PRACTICE / CONTEXT_CHANGE. | `002,010,014–019`; warrior designation can coexist with care; not infallible classification. |
| `MT-S-074` / Ruijerd | Reputation work under uncertainty → qualified hope, reciprocal recognition and independent departure. KNOWLEDGE / RELATIONSHIP_CHANGE. | `019–020`; curse report not proof, local acceptance not general reform. |
| `MT-S-075` / Roxy | Continuing search → chance opportunity, qualified location lead and divided information mission. KNOWLEDGE / DECISION_CHANGE. | `027–028`; gives up reward/reunion, mistakes persist; lead not rescue or delivered message. |
| `MT-S-076` / Lilia | Earlier domestic history → assault consequences, insecure gratitude and self-questioned maternal purpose disclosed. REVEALED_NOT_NEW. | `030–031`; father supplied alternative, no clinical diagnosis or retroactive consent. |
| `MT-S-077` / Lilia | Captive protector → rescued mother, proposed service arrangement and rare expressed affection. CONTEXT / RELATIONSHIP_CHANGE. | `008,012,029–031`; certainty of love leaves control intact; no complete reform. |
| `MT-S-078` / Aisha | Imposed education/detention → communication initiative, rescue, identity recognition and changed admiration. KNOWLEDGE / RELATIONSHIP_CHANGE. | `005–006,013,029,031`; cleverness and consent to service remain age/context limited. |
| `MT-S-079` / Zanoba | Craft collector with later-disclosed violent history → coercive rescuer and would-be pupil, then exile. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `009–010`; narrow sensitivity is not general empathy; affectionate act injures. |
| `MT-S-080` / Ginger and soldiers | Hostage-constrained service → independent overlapping rescue plans and escorted return. CONTEXT / AGENCY_CHANGE. | `007–010`; different information, motives and methods; not mere royal obedience. |
| `MT-S-081` / Ghislaine and Alphonse | Returned retainers → incompatible welfare/domain commitments, Eris's choice and continuing reconstruction. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `021–022,026`; neither speaks for all her wishes; reconstruction real despite initial impression. |
| `MT-S-082` / Paul, Sylphie, Zenith | Prior absence → historical affected-person evidence and differentiated survival/location reports. KNOWLEDGE_CHANGE / REVEALED_NOT_NEW. | `021,027–030`; no new directly observed present Paul choice, Sylphie address absent, Zenith circumstances unknown. |
| `MT-S-083` / Orsted, Nanahoshi, Hitogami | Unknown relevant actors → attack/intervention and competing attributed explanations. REVEALED_NOT_NEW. | `015–019`; action known more firmly than identity mechanism/motive; no broad persona. |

| Local key / domain | Current readiness and home | Calibration limit |
| --- | --- | --- |
| Rudeus / learning, coordination, written register, particular repair | BOUNDED_PROVISIONAL; [model 1.3](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md). | Add ST12–15 and checks V18–23; global despair not objective no-growth verdict, no reliable high-stakes or consent transfer. |
| Eris / practical learning, loyalty, refusal and independent appraisal | BOUNDED_PROVISIONAL; [model 1.2](../04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/eris/EVIDENCE_INDEX.md). | Add ST07–08 and checks V10–13; new interiority not infallibility, peer-repair transfer remains untested. |
| Ruijerd / care, classification, training, friendship | BOUNDED_PROVISIONAL; [model 1.1](../04%20Character%20Analysis/ruijerd/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/ruijerd/EVIDENCE_INDEX.md). | Add ST05–06 and checks V06–08; hope is not metaphysical verification or universal reform. |
| Roxy / work, qualified inquiry and search coordination | BOUNDED_PROVISIONAL; [model 1.1](../04%20Character%20Analysis/roxy/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/roxy/EVIDENCE_INDEX.md). | Add ST05 and checks V06–08; no reliable forecasting, broad romance persona or completed mission. |
| Paul / prior observed domains | BOUNDED_PROVISIONAL; [model 1.1](../04%20Character%20Analysis/paul/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/paul/EVIDENCE_INDEX.md). | New historical source check V06; no invented current behavioral transition or fresh opportunity for rules001–006. |
| Lilia, Aisha, Zanoba / represented contexts | Richer bounded ledger descriptions; new broad package deferred. | Concentrated new focalization needs transfer checks; targeted checkpoint owns distinct explanatory finding. |
| Other actors / missing or hidden domains | Preserve earlier bounds; no global enrollment or new general persona. | Motive gaps, hearsay and unseen future remain explicit. |

No domain becomes DOMAIN_READY. No generated scenario or sexualized minor scenario supplies evidence.


## V07 updates — 2026-09-26 UTC

Prior V01–V06 bodies remain historical and unchanged. The current source boundary is Japanese LN V01–V07. The entering freeze used audited V06 head `0e72e531278055c0dbb7a6054285337a1cc37a93`; later repository reconciliation does not change that analytical input. Observation suffixes resolve in [V07](../02%20Sequential%20Readings/MT_V07_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V07-`. The [recognition checkpoint](../05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md) owns the focused comparison. Publication and exact-head audit are separate from content acceptance.

| Event / local key | Prior → represented change / kind | Evidence and limit |
| --- | --- | --- |
| `MT-S-084` / Rudeus | Northbound purpose amid rejection → accepts work invitation, renews life-directed action through companions' solidarity. CONTEXT / RELATIONSHIP_CHANGE. | `001–005`; death indifference and useful ability coexist; no comprehensive recovery. |
| `MT-S-085` / Rudeus | Isolated applicant → regular training, paid temporary work, publicity and increasingly valued company. PRACTICE / RELATIONSHIP_CHANGE. | `007–013`; formal nonmembership persists, specialist dependence and pleasure remain uneven. |
| `MT-S-086` / Rudeus | Winter routine → undertakes solo search, corrects assumed Sara death and returns her alive. KNOWLEDGE / CONTEXT_CHANGE. | `014–017`; Mimir's death confirmed; Sara's own survival work causal; reward imagery follows rescue. |
| `MT-S-087` / Rudeus | Friendly shopping and concealed attraction → bodily difficulty, interpreted rejection, aggression, disclosure and interrupted suicidal action. CONTEXT / REVEALED_NOT_NEW. | `018–024`; prior bodily signs newly interpreted, no medical diagnosis or blame for involuntary response. |
| `MT-S-088` / Rudeus | Crisis support → mobile temporary work with Soldat, explicit avoidance of a single-party attachment, unresolved regret. PRACTICE / RELATIONSHIP_CHANGE. | `024,026`; practical change is real, cure and romantic repair unobserved; Sara's actual intentions unavailable. |
| `MT-S-089` / Sara | Noble-category distrust → contrary rescue/search evidence acknowledged but initially discounted, then recognizes different uses of smiling. KNOWLEDGE / APPRAISAL_CHANGE. | `006,010–012`; history of parental loss disclosed retrospectively, no general reconciliation with nobles. |
| `MT-S-090` / Sara | Guarded cooperation → advocates return, survives injury, offers thanks and initiates companionship/purchase. RELATIONSHIP / PRACTICE_CHANGE. | `009,011–012,016–019`; skilled effort, indebtedness and pleasure are distinguishable. |
| `MT-S-091` / Sara | Concealed affection → misreads difficulty as undesirability, defensively denies affection, then seeks explanation and plans apology. REVEALED_NOT_NEW / KNOWLEDGE_CHANGE. | `020,023,025`; late focalization establishes love without making every belief correct. |
| `MT-S-092` / Sara | Anger with false imagined mockery → corrected bodily information, regret and fear of pursuit after departure. KNOWLEDGE / DECISION_CHANGE. | `025`; no successful conversation, no offstage reunion or unconditional permanent refusal. |
| `MT-S-093` / Soldat | Misunderstanding/apology and repeated hostile provocation → accepts blows, listens, obtains help, interrupts crisis and accompanies. CONTEXT / RELATIONSHIP_CHANGE. | `010–011,021–024,026`; explicitly apologizes for earlier conduct; broad gender assumptions and misreading Eris remain. |
| `MT-S-094` / Suzanne and Timothy | Mixed leadership and party survival decisions → preparation to resume search, reciprocal thanks and consent-sensitive mediation. CONTEXT / PRACTICE_CHANGE. | `003–004,010,014,017,023,025`; neither knows everything or guarantees repair. |
| `MT-S-095` / Elise | Professional encounter → compassionate interpretation, then disclosure to Sara with protective anger. CONTEXT / KNOWLEDGE_CHANGE. | `022,025`; explanation is attributed, own information incomplete, privacy cost remains. |
| `MT-S-096` / Ariel, Fitts and attendants | Dangerous flight and school entry → engineered public conflict, election victory and recruitment planning. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `028–030`; retrospective second-year operation precedes third-year present; no executed future dispatch. |
| `MT-S-097` / Elinalise | V06 message mission → obtains Rudy's reported location. KNOWLEDGE_CHANGE. | `027`; hearsay battle report, message not delivered and mother not shown rescued. |

| Local key / domain | Current readiness / home | Calibration limits |
| --- | --- | --- |
| Rudeus / practical learning, selected coordination, contextual speech and help receipt | BOUNDED_PROVISIONAL; [model 1.4](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md). | ST16–20 and checks V24–30; ability, pleasure, bodily response and intimate security cannot substitute for one another. |
| Sara / team obligation, category revision, ordinary reciprocity and defensive communication | First BOUNDED_PROVISIONAL [model 1.0](../04%20Character%20Analysis/sara/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/sara/EVIDENCE_INDEX.md). | Six contextual rules, six states and seven retrospective checks; no clean holdout or universal romantic persona. |
| Eris, Ruijerd, Roxy, Paul / existing admitted domains | Existing bounded packages reviewed; no material operational revision. | Rudy's present memories, fear and guesses are not new direct choices by those people; V06 ceilings preserved. |
| Soldat, Suzanne, Timothy, Elise, Ariel, Fitts and others | Source-bound descriptions maintained here and in other ledgers; standalone packages deferred. | Material actions and partial interior access warrant analysis but no redundant or broad model on this transaction. |

No DOMAIN_READY, mature monograph, generated scenario evidence or global enrollment. Sara's independent work and changing appraisal make her new operational responsibility distinct from simply modeling Rudy's interlocutor.


## V08 updates — 2026-09-26 UTC

Prior V01–V07 bodies remain historical and unchanged. Current source boundary: Japanese LN V01–V08. Immutable entering input was final audited V07 `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. Numeric observation suffixes resolve in [V08](../02%20Sequential%20Readings/MT_V08_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V08-`. The [consent and institutional-power checkpoint](../05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md) owns the targeted comparison. Content acceptance, publication/audit and integration to main remain separate states.

| Event / local key | Prior → represented change / kind | Observation and constraint |
| --- | --- | --- |
| `MT-S-098` / Rudeus | Mobile work/search → receives Elinalise's message, considers travel and school, changes plan after dream promise. KNOWLEDGE / CONTEXT_CHANGE. | `001–005`; location report is not rescued mother; cure promise unverified. |
| `MT-S-099` / Rudeus | Adventurer → university special student, wins exam, needs local rules and social witnesses. CONTEXT / PRACTICE_CHANGE. | `006–009`; technical transfer coexists with misreading and public vulnerability. |
| `MT-S-100` / Rudeus | New enrollment → research partnership, study routine, technique sharing and selective privacy respect. RELATIONSHIP / PRACTICE_CHANGE. | `008,012`; bodily difficulty persists; Fitts identity unresolved. |
| `MT-S-101` / Rudeus | Failed craft teacher → accepts production reframing, purchases and teaches child. KNOWLEDGE / PRACTICE_CHANGE. | `013–016`; adaptive means coexist with ownership and projected despair. |
| `MT-S-102` / Rudeus | Angered by figure loss → planned victory, abusive captivity, reduced anger after repair possibility, enforced submission. CONTEXT / REVEALED_NOT_NEW. | `019–025`; hears objection, recognizes crime, retains control. |
| `MT-S-103` / Rudeus | Apparent restored order → school pleasure, notices Juli's fear, offers choice after meal disagreement. PRACTICE / KNOWLEDGE_CHANGE. | `028–030`; limited correction, no emancipation or general repair. |
| `MT-S-104` / Zanoba | Reunited disciple → persistent but unsuccessful craft pupil, hesitates to suggest helper. CONTEXT / REVEALED_NOT_NEW. | `007,013–014`; strength not precision, hierarchy inhibits information. |
| `MT-S-105` / Zanoba | Purchaser/teacher's assistant → names child after brother, cares, fears reporting broken figure, welcomes revenge. RELATIONSHIP / REVEALED_NOT_NEW. | `016,018,022`; interior access differentiates art devotion and Rudy's Roxy fixation. |
| `MT-S-106` / Zanoba | Reverent follower → increasing care and explicit disagreement about Juli's meal demands. PRACTICE / REVEALED_NOT_NEW. | `028,030`; brother-based care mechanism is Rudy's guess; ownership persists. |
| `MT-S-107` / Sylphiette | Former village pupil → present service, training, study, friendship and reported bereavement. REVEALED_NOT_NEW / CONTEXT_CHANGE. | `010`; multiple mentors; service simile not legal slavery; exclude unassigned Fitts acts. |
| `MT-S-108` / Sylphiette | Affection and imagined marriage → desire for exclusivity qualified by fear of losing Rudy. REVEALED_NOT_NEW. | `011`; hypothetical accommodation is not future consent. |
| `MT-S-109` / Sylphiette | Possible reunion → withheld name, fear of delayed disclosure, actual refusal and equality/recruitment conflict. KNOWLEDGE / CONTEXT_CHANGE. | `026–027`; attendants' premise corrected; disguise mechanism unresolved. |
| `MT-S-110` / Fitts role | Recognition of prospective recruit → examiner, research helper and defender; later participant in punishment and selective privacy exchange. CONTEXT / RELATIONSHIP_CHANGE. | `006,008–009,012–013,023–025,030`; actions retained under source attribution, no automatic identity merge. |
| `MT-S-111` / Juliette | Enslaved, hungry child → purchased, treated, named and taught; intermittent skill, fear, chosen effort and smile. CONTEXT / PRACTICE_CHANGE. | `014–016,028,030`; no focalized interior, manumission or free labor agreement. |
| `MT-S-112` / Linia and Pursena | Informal school rulers/property destroyers → defeated, confined, assaulted and intimidated into subordinate status; later sociability. CONTEXT / RELATIONSHIP_CHANGE. | `007,017–025,028`; wrongdoing does not cancel victimization; later ease not retroactive consent. |
| `MT-S-113` / Elinalise, Ariel and Luke | Messenger arrives; school ties and desires develop; attendants correct assumption about disclosed name. KNOWLEDGE / CONTEXT_CHANGE. | `003–005,010,019,026–029`; separate individual acts, no universal benevolence or offstage knowledge. |

| Local package / domain | Readiness and current route | Calibration and limit |
| --- | --- | --- |
| Rudeus / practical learning, contextual coordination, teaching and selected speech | BOUNDED_PROVISIONAL [model1.5](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md). | Nine rules; ST21–26; V31–37 retrospective checks; selective boundary respect is not general reliability. |
| Zanoba / craft, masterhood, constrained disclosure and pupil care | First BOUNDED_PROVISIONAL [model1.0](../04%20Character%20Analysis/zanoba/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/zanoba/EVIDENCE_INDEX.md). | Five rules, four states, six retrospective tests; dissent countercase; no generalized political/parental persona. |
| Sylphiette / explicit self-account, learning, attachment, service and inhibited disclosure | First BOUNDED_PROVISIONAL [model1.0](../04%20Character%20Analysis/sylphiette/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/sylphiette/EVIDENCE_INDEX.md). | Five rules, five states, six retrospective tests; only explicitly attributable V01/V08 behavior, Fitts actions excluded pending identity mechanism. |
| Eris, Paul, Roxy, Ruijerd, Sara | Existing bounded packages reviewed without material update. | V08 reports/memories/imagined judgment supply no new direct sequence by them; previous ceilings retained. |
| Fitts, Juliette, Elinalise, Ariel, other students | Source-bound descriptions here; standalone operational packages deferred. | Identity, viewpoint and sampling limits named in reading; no global registry changes. |

No DOMAIN_READY, mature monograph, clean holdout or generated-scenario evidence. New revelations of prior habits are not automatically new dispositions.


## V09 updates — 2026-09-26 UTC

Prior V01–V08 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V09; immutable input final audited V08 `210894fd2b5894b7e499bab80251e8f5ea761138`. Observation suffixes resolve in [V09](../02%20Sequential%20Readings/MT_V09_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V09-`. The [disclosure and recovery checkpoint](../05%20Checkpoint%20Syntheses/MT_V09_DISCLOSURE_AND_RECOVERY_CHECKPOINT.md) owns targeted cross-domain review. Newly disclosed past states are not newly occurring changes. Acceptance, publication/audit and main integration remain separate.

| Event / local key | Prior → represented state / change kind | Observation and limit |
| --- | --- | --- |
| `MT-S-114` / Rudeus | School routine → accepts quiet request, adjusts lesson expectations, rescues victim before recognition. PRACTICE. |001–003; reputation from abuse can enable useful intervention without erasing its history. |
| `MT-S-115` / Rudeus | Presumed unsuitable couple → enables discussion, revises forecast and discloses own difficulty. KNOWLEDGE/RELATIONSHIP. |004–005; no cure or guaranteed future for either couple. |
| `MT-S-116` / Rudeus | Feared challenger → negotiates conditional strike, survives and gains disproportionate reputation. CONTEXT/KNOWLEDGE. |007–009; spell power not unrestricted combat superiority. |
| `MT-S-117` / Rudeus | Increased confidence → mask-triggered collapse, safety clarification and origin recognition. CONTEXT/KNOWLEDGE. |010–013; no general cowardice or complete recovery. |
| `MT-S-118` / Rudeus | Research partner → routine learning, unequal information bargain and valued companionship. PRACTICE/RELATIONSHIP. |015–018; failed aura training, experimental failure, privacy applied selectively. |
| `MT-S-119` / Rudeus | Attraction/partial response → protects secret, recognizes Sylphiette and discloses illness. KNOWLEDGE/RELATIONSHIP. |019–026; old dependence acknowledged, equality unmeasured. |
| `MT-S-120` / Rudeus | Persistent difficulty → morning recovery claim, gratitude and acknowledged insufficient care. HEALTH/RELATIONSHIP. |028–029/032; immediate report, not all-trauma cure or ethical closure. |
| `MT-S-121` / Sylphiette | Unresolved Fitts role → explicit self-identification and scene-specific reassignment. REVEALED_NOT_NEW. |006/030–031; Ariel also performs role; selected entrance/dorm events confirmed retrospectively. |
| `MT-S-122` / Sylphiette | Partial causal information → grief/attack, restraint and contextual correction. CONTEXT/KNOWLEDGE. |013; attempted violence not excused, hypothesis still uncertain. |
| `MT-S-123` / Sylphiette | Delayed name/jealousy → support and pressure enable a plan and confession. CONTEXT/RELATIONSHIP. |014/021–025; permission preexisted, delay not entirely imposed. |
| `MT-S-124` / Sylphiette | Reciprocal declaration → seeks help, acts with incomplete disclosure, perceives useful care and uncertain equality. PRACTICE/RELATIONSHIP. |026–028/032; own pain and satisfaction both retained. |
| `MT-S-125` / Cliff | Diligent proud newcomer → defeats, reluctant factual update, rescue and thanks. REVEALED_NOT_NEW/KNOWLEDGE. |001/003; accepting ability differs from liking or seeking instruction. |
| `MT-S-126` / Cliff | Idealized attraction → private agreement, care promise, qualified listening and persistent research. RELATIONSHIP/PRACTICE. |004–005/018; curse cure unachieved, theory still a lead. |
| `MT-S-127` / Nanahoshi | Rudy's masked threat image → named other-world transfer survivor, different return goal and guarded account. REVEALED_NOT_NEW. |010–013; testimony and observed recognition have different warrant. |
| `MT-S-128` / Nanahoshi | Negotiated cooperation → repeated preliminary trials, resource limits and selective answers. PRACTICE/RELATIONSHIP. |016/020; not full mutual disclosure or established safety. |
| `MT-S-129` / Zanoba | Craft pupil/caregiver → accepts manageable work, helps seating and staff retrieval, proposes invasion of privacy. PRACTICE/REVEALED_NOT_NEW. |002/008/015/017/023; care neither universally reliable nor emancipatory. |
| `MT-S-130` / Eris | Departure for training → arrival and current practice newly disclosed, unusual rank award and persistent Rudy-oriented goal. REVEALED_NOT_NEW/PRACTICE. |033–034; no knowledge of Rudy's abandonment interpretation or reconciliation. |
| `MT-S-131` / Nina | Rivalry/jealousy → school visit, defeat, mistaken power estimate and changed practice. KNOWLEDGE/PRACTICE. |034–035; improved conduct does not verify premise; future rivalry proleptic. |
| `MT-S-132` / Ariel and Luke | Recruitment/service frame → support personal goal, release stated debt, apply pressure and offer mixed advice. REVEALED_NOT_NEW/PRACTICE. |021–023/027/030; empathy, strategic use and error coexist. |
| `MT-S-133` / Elinalise, Juli and students | Negotiated relationship, continued learning and school routines. RELATIONSHIP/PRACTICE. |004–005/009/015/018; separate purposes; ownership and bodily boundaries unresolved. |

| Package/domain | Current bounded route | Calibration and debt |
| --- | --- | --- |
| Rudeus | [model1.6](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md) | Nine rules; new ST27–33/testsV38–45; local recovery and selective autonomy, no adult domestic/general moral persona. |
| Sylphiette | [model1.1](../04%20Character%20Analysis/sylphiette/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/sylphiette/EVIDENCE_INDEX.md) | Existing five rules plus narrow006, ST06–09/testsV07–13; confirmed identity does not license blanket Fitts assignment. |
| Zanoba | [model1.1](../04%20Character%20Analysis/zanoba/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/zanoba/EVIDENCE_INDEX.md) | Five rules, ST05/testsV07–09; ordinary craft/care contradictions, no universal restraint. |
| Eris | [model1.3](../04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/eris/EVIDENCE_INDEX.md) | Six rules, ST09–10/testsV14–17; training continuity, rule004 remains untested here. |
| Cliff | First [model1.0](../04%20Character%20Analysis/cliff/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/cliff/EVIDENCE_INDEX.md) | Five rules/four states/six retrospective tests; pride, study, care, qualified help-seeking. |
| Nanahoshi | First [model1.0](../04%20Character%20Analysis/nanahoshi/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/nanahoshi/EVIDENCE_INDEX.md) | Five rules/three states/six retrospective tests; return-oriented research, cooperation and disclosure limits. |
| Roxy, Ruijerd, Paul, Sara | Existing packages reviewed: no material update. | Reports, recollections and imagined judgments do not add direct sequences; prior ceilings retained. |
| Ariel, Luke, Nina, Elinalise, Juli and others | Source-bound ledger descriptions; standalone packages deferred. | Narrow sampling, limited affected-person access or concentrated extra; no global enrollment/DOMAIN_READY. |


## V10 updates — 2026-09-26 UTC

Prior V01–V09 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V10; immutable input audited V09 `40018b5caedfba456da199ed2fea613ec991015a`. Observation suffixes resolve in [V10](../02%20Sequential%20Readings/MT_V10_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V10-`. The [V01–V10 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md) owns cumulative review. Revealed earlier events, present changes and explicit prolepsis retain different times. Draft acceptance, publication/audit and main integration remain separate.

| Event / local key | Prior → represented state / change kind | V10 observation and limit |
| --- | --- | --- |
| `MT-S-134` / Rudeus | Reported recovery → marriage, house, patronage and public commitment. CONTEXT/RELATIONSHIP. |001–013; consultation initially avoided, independent wife purposes and distributed labor retained. |
| `MT-S-135` / Rudeus | New household → daily work, reciprocal lessons, explicit rebukes and shared family decision. PRACTICE. |015–018; real restraint and repeat known-boundary violation, no global reform. |
| `MT-S-136` / Rudeus | Routine → crisis helper receiving care, research collaborator and reunited brother/friend. CONTEXT/KNOWLEDGE. |019–026; bottle limited, Eris account possible not confirmed, Norn distrust persists. |
| `MT-S-137` / Sylphiette | Recognized partner → wife retaining service, savings, lessons, requests and shared household work. RELATIONSHIP/PRACTICE. |002/007–010/015–018/020/025; preference can be spoken, insecurity/equality remain distinct. |
| `MT-S-138` / Sylphiette | Supportive advice → recommends punitive enforcement of guest attendance. REVEALED_NOT_NEW. |009; different trigger from grief/missing context, proposal not executed harm. |
| `MT-S-139` / Zanoba | Craft pupil → protects automaton against master, assaults Cliff, requests meaningful research responsibility. PRACTICE/KNOWLEDGE. |004–006/011; independent contribution within deference, social competence not ethical reliability. |
| `MT-S-140` / Zanoba | Craft/care roles → practical helper, honest emotional companion and source of layered-design idea. PRACTICE. |020–021; no complete understanding of Rudy feelings, no sole invention or emancipation. |
| `MT-S-141` / Cliff | Proud student/care promise → diagnostic inquiry, continued fidelity after disclosure and effective collaborative correction. KNOWLEDGE/PRACTICE. |004–005/014/021–022; admits limits, cure remains hypothesis/unachieved. |
| `MT-S-142` / Nanahoshi | Guarded collaborator → chosen sociability with explicit privacy/alcohol limits. RELATIONSHIP/PRACTICE. |011/015; not complete withdrawal or changed return goal. |
| `MT-S-143` / Nanahoshi | Long-prepared test → actual failure, global impossibility inference and acute distress. CONTEXT. |019–020; perceived risk and self-injury represented, no diagnosis or demonstrated impossible return. |
| `MT-S-144` / Nanahoshi | Supported recovery → identifies gap, implements collective redesign, bottle success, thanks and complaint. KNOWLEDGE/PRACTICE. |021–022; not human return, cure or grievance-free community. |
| `MT-S-145` / Elinalise | Family identity concealed → recognition, reported descendant history, acceptance and practical relief for Sylphie. REVEALED_NOT_NEW/RELATIONSHIP. |007/011–015; historical stigma not deserved, private exchange not fully heard. |
| `MT-S-146` / Ariel | Political patron → marriage support, reciprocal affiliation and proposed prevention of Sylphie participation. PRACTICE. |002/011/013; protective concern and unilateral control coexist; plan not enacted future. |
| `MT-S-147` / Luke | Presumed rival → requests duel and care, loyalty clarified by comrades. KNOWLEDGE/REVEALED_NOT_NEW. |002/013; coercive appeal/withheld purpose retained, exact inner motives not wholly accessible. |
| `MT-S-148` / Paul | Absent searcher → received letter explains delegation and differentiated care for Norn. KNOWLEDGE. |017; sending-time ages/plans not present certainty, no rescued Zenith. |
| `MT-S-149` / Paul | Letter result → extra reveals earlier risk deliberation and escort trust decision. REVEALED_NOT_NEW. |030/034; visible child reliance and prior conduct influence judgment, no infallibility. |
| `MT-S-150` / Ruijerd | Earlier escort report → extra reveals protective restraint, listening, limited understanding and undertaking. REVEALED_NOT_NEW. |031–034; son-training explanation conjectural, child's first wish not fulfilled. |
| `MT-S-151` / Ruijerd | Undertaking → completed escort, tentative mediation and resumed independent search. PRACTICE/RELATIONSHIP. |023–026/034; tense motives partly unknown, no automatic family repair. |
| `MT-S-152` / Roxy | Fear reported → direct extra supplies learned fear, duty-driven challenge and corrected judgment. REVEALED_NOT_NEW/KNOWLEDGE. |033–034; fear persists after recognition, no broad cowardice or prejudice cure. |
| `MT-S-153` / Eris | Training aim → solitary routine, painful avoidance and escalating obstruction encounter. PRACTICE/REVEALED_NOT_NEW. |027–029; no departure clarification received, later certification only explicit prolepsis. |
| `MT-S-154` / Ghislaine | Mentor → challenges Gal and values knowledge beside slowed martial progress. PRACTICE/REVEALED_NOT_NEW. |029; continued questioning despite threat, no universal tactical superiority. |
| `MT-S-155` / Norn | Prior rejection → safety/attachment reasons disclosed; accepts escort, still distrusts brother. REVEALED_NOT_NEW/RELATIONSHIP. |026/030–032; understands risk yet fears separation, factual context insufficient for trust. |
| `MT-S-156` / Aisha | Skilled younger sister → route ingenuity, all-night calculation and exhaustion; earlier contempt disclosed. PRACTICE/REVEALED_NOT_NEW. |024/030; task competence not adult self-care or ethical superiority. |
| `MT-S-157` / Lilia | Caregiver → extra shows rebuke of cruel speech alongside prescribed daughter hierarchy. REVEALED_NOT_NEW. |030/033; checks abuse without removing unequal service assumptions. |
| `MT-S-158` / Juliette | Owned pupil → curiosity, learning, improved nutrition and noticed adult distress; fear remains. PRACTICE. |001/005–006/011/020; concrete choices/care, no manumission or full interior access. |
| `MT-S-159` / Badigadi | Convivial guest → support, disruption and interruption of complaint; old tension surfaces. PRACTICE/REVEALED_NOT_NEW. |011/022/025; unknown Ruijerd history cannot be supplied from Rudy conjecture. |

| Package/domain | Current route and readiness | Calibration and debt |
| --- | --- | --- |
| Rudeus / practical, relational and bounded domestic choices | BOUNDED_PROVISIONAL [model1.7](../04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/rudeus/EVIDENCE_INDEX.md); first [V01–V10 monograph](../04%20Character%20Analysis/rudeus/CHARACTER_MONOGRAPH.md). |9rules/37states/52checks; monograph explains interactions, does not confer reliable ethics or complete adult persona. |
| Sylphiette / learning, service, household requests and hierarchy | [model1.2](../04%20Character%20Analysis/sylphiette/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/sylphiette/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |7/12/18; punitive007 distinguished from grief006; requests do not eliminate insecurity. |
| Zanoba / craft, deference and practical care | [model1.2](../04%20Character%20Analysis/zanoba/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/zanoba/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/7/13; non-pupil care006 narrow, assault/ownership retained. |
| Cliff / work, revision and chosen commitment | [model1.1](../04%20Character%20Analysis/cliff/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/cliff/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |5/7/9; actual technical correction, no curse cure. |
| Nanahoshi / research, privacy, sociability and bounded crisis | [model1.1](../04%20Character%20Analysis/nanahoshi/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/nanahoshi/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/6/10; broad invariant persistence rejected, no clinical rule or human return. |
| Eris / training, vulnerability and written directness | [model1.4](../04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/eris/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/11/20; defense/peer-repair exact triggers untested; no present rank from prolepsis. |
| Paul / differentiated care and delegation | [model1.2](../04%20Character%20Analysis/paul/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/paul/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/6/9; letter and retrospective decision not guaranteed future parenting. |
| Ruijerd / protection, listening, care and independent aims | [model1.2](../04%20Character%20Analysis/ruijerd/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/ruijerd/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/8/11; incomplete understanding admitted, old tension unknown. |
| Roxy / duty, fear and proposition-specific correction | [model1.2](../04%20Character%20Analysis/roxy/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/roxy/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/6/11; fear not extinguished, no new family-channel test. |
| Elinalise / practical work, refusal and family disclosure | First [model1.0](../04%20Character%20Analysis/elinalise/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/elinalise/EVIDENCE_INDEX.md), BOUNDED_PROVISIONAL. |6/5/8; independent contexts justify activation, kinship single-cluster and curse/history limited. |
| Sara / existing V07 domains | [model1.0](../04%20Character%20Analysis/sara/RECONSTRUCTION_MODEL.md) unchanged after review. |No fresh direct opportunity, absence not a validation pass. |
| Norn, Aisha, Ariel, Luke, Ghislaine, Lilia, Juli and others | Maintain substantial source-bounded ledger analysis; broad model deferred. |Checkpoint names ordinary/context/access debts; no popularity or count criterion, no invented family/peer future. |

All global IDs remain null. No DOMAIN_READY or clean holdout. The cumulative checkpoint and new monograph own distinct arguments; this ledger retains observed chronology and current readiness. Newly disclosed past states are not changes that began at V10 narrative present.


## V11 updates — 2026-09-27 UTC

Prior V01–V10 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V11; immutable input audited V10 `4823e7f9cecff45d86f3045304b5825c79bcb628`. Observation suffixes resolve in [V11](../02%20Sequential%20Readings/MT_V11_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V11-`. The [V11 checkpoint](../05%20Checkpoint%20Syntheses/MT_V11_KNOWLEDGE_AND_DUTY_CHECKPOINT.md) owns targeted knowledge/duty review. Revealed earlier events and current changes retain different times; semantic acceptance, publication/audit and main integration remain separate.

| State / local key | Prior → V11 represented state / kind | Observations / persistent feature / limit |
| --- | --- | --- |
| `MT-S-160` / Rudeus | Receiving sisters → differentiates educational choices, hears fairness objection and unseen effort. PRACTICE/KNOWLEDGE. |001–004; promises honored, comparison pressure not controlled, family-stability rationale narrower than universal autonomy. |
| `MT-S-161` / Rudeus | Projected bullying → corrected inquiry, admitted ignorance and sustained presence. KNOWLEDGE/PRACTICE. |007–010; threatening first approach persists as countercase; lacks Norn's full explanation. |
| `MT-S-162` / Rudeus | Domestic routine → teaching/writing difficulty, pregnancy joy and declared fidelity. CONTEXT/PRACTICE. |011–014; collaborative authorship, no demonstrated general parenting competence. |
| `MT-S-163` / Rudeus | Initial stay decision → chooses rescue with household support and newly shortened route. CONTEXT/KNOWLEDGE. |015–022; no sole-helper fact, no reliable forecast or guaranteed return. |
| `MT-S-164` / Rudeus | Desert newcomer → mutual reliance, explicit external impairment, corrected cultural appraisal and successful flight. CONTEXT/KNOWLEDGE. |023–031; ordinary choices and induced state distinct; retreat not universal nonlethal doctrine. |
| `MT-S-165` / Norn | Distrust → independently disclosed fear, prior reflection, changed appraisal and accepted comfort. REVEALED_NOT_NEW/KNOWLEDGE/RELATIONSHIP. |007–010; not brother's sole achievement or certainty of future safety. |
| `MT-S-166` / Norn | New trust → chosen friends, refused introduction, requested teaching and authored contribution. PRACTICE. |011; talent/readership unverified, autonomous choices extend beyond closeness. |
| `MT-S-167` / Norn | Rescue demand → self-blame while waiting, religious return, objection and chosen preparation. CONTEXT/PRACTICE. |016/020/032–034; no sole responsibility for adult decision, diagnosis or proven durable relief. |
| `MT-S-168` / Aisha | Capable traveler → exam bargain, fairness disclosure, wages and independent leisure negotiated. KNOWLEDGE/PRACTICE. |001/003/012/020; hidden effort and childhood dependency; sibling belittling persists. |
| `MT-S-169` / Sylphiette | Wife/guard → expresses independent service priority, pregnancy insecurity, accepts departure with fears. REVEALED_NOT_NEW/CONTEXT. |002/014/020; no universal consent or abolished work purpose. |
| `MT-S-170` / Zanoba | Researcher/friend → assaults Ginger, later offers non-directive support and receives regular correction. PRACTICE/REVEALED_NOT_NEW. |005/016/021; actual counsel qualifies total deafness, not assault or hierarchy. |
| `MT-S-171` / Ginger | Escort returns → asks to teach Juli, injured defending register, explains vow and supplies recurring counsel. PRACTICE/REVEALED_NOT_NEW. |005/013/021; corrections corroborated, broad exit/independent-life model still insufficient. |
| `MT-S-172` / Juliette | Owned pupil → completed craft, pleasure in recognition, language learning and testimony about Ginger. PRACTICE. |005/013/021; ownership unchanged, no adult-equivalent consent inferred. |
| `MT-S-173` / Nanahoshi | Guarded research partner → staged plan, bounded social care and restricted teleport map disclosure. KNOWLEDGE/RELATIONSHIP. |002/013/019; earlier memory claim revised; secret records preexist present disclosure, return still goal. |
| `MT-S-174` / Cliff | Cure research/commitment → partial device, accepts travel limit, proposes before cure, counsels Norn. PRACTICE/RELATIONSHIP. |013/017/033–034; helpfulness coexists with dismissive tone and explicitly unverified political fantasy. |
| `MT-S-175` / Elinalise | Rescue intention → tells Cliff, new commitment changes separation preference, shorter route permits revised plan. CONTEXT/RELATIONSHIP. |016–020; no fickleness trait from changed available options, cure absent. |
| `MT-S-176` / Elinalise | Traveler → practical protector, enforces/receives boundaries, affirms grandchild care and escalates dispute. PRACTICE. |022–031; desert/language limits, own unwanted touch, no infallibility. |
| `MT-S-177` / Carmelita | Grateful but skeptical warrior → cultural testimony, grief, vengeance demand and withdrawal. KNOWLEDGE/CONTEXT. |027/029–031; parentage reported, precise attachment unknown, silence not reconciliation. |
| `MT-S-178` / Tonto | Quiet guard → explains name and shows interest in magic, then killed in ambush. PRACTICE/CONTEXT. |029–030; thin but independent ordinary presence, no unseen final thought. |
| `MT-S-179` / Garvan and Baribadom | Apparent indifference → returned search reported, employment, shared long trust and survival command. KNOWLEDGE/REVEALED_NOT_NEW. |027–031; Rudy's guesses about callousness/personnel remain guesses. |
| `MT-S-180` / Linia, Pursena and Ariel | Gift plan/report → investigation, revised account, rebuke and accepted farewell. KNOWLEDGE/PRACTICE. |006/018; later correction required, no invented recipient interiority or comprehensive prior repair. |

| Package / domain | Current decision | Calibration / remaining debt |
| --- | --- | --- |
| Rudeus | Revise model/index1.8, BOUNDED_PROVISIONAL. | Family inquiry, new knowledge and impaired state separated; V01–V10 monograph retained as historical bounded synthesis. |
| Sylphiette | Revise model/index1.3. | Service priority, pregnancy and departure agreement; affection not blanket bodily permission. |
| Zanoba | Revise model/index1.3. | Violence in service hierarchy, tolerated ordinary counsel and non-directive help require different triggers. |
| Cliff | Revise model/index1.2. | Partial device, commitment before cure and pastoral help; no forecast accuracy. |
| Nanahoshi | Revise model/index1.2. | Prior account corrected by disclosed records; no universal truthfulness or new destination goal. |
| Elinalise | Revise model/index1.1. | Travel competence/limits, mutual boundaries and kinship; no universal restraint or complete biography. |
| Norn | First [model1.0](../04%20Character%20Analysis/norn/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/norn/EVIDENCE_INDEX.md). | Bounded fear/appraisal, learning/peer agency and faith; six rules, five states, eight retrospective checks. |
| Aisha | First [model1.0](../04%20Character%20Analysis/aisha/RECONSTRUCTION_MODEL.md), [index](../04%20Character%20Analysis/aisha/EVIDENCE_INDEX.md). | Bounded planning, role/fairness and negotiated wants; five rules, four states, seven retrospective checks; access mostly Rudy-mediated. |
| Eris, Paul, Roxy, Ruijerd, Sara | Reviewed: no material operational update; earlier packages unchanged. | Memories, testimony and absent present actions do not supply new direct opportunities. Norn's recollections revise her account without silently granting the absent people new knowledge. |
| Ginger, Juli, travel cast and others | Expanded ledger descriptions; full operational packages deferred. | Ginger's repeated correction is now supported, but alternative contexts/exit remain thin; travel cast concentrated in one expedition. |

All global IDs remain null; none DOMAIN_READY. The [V11 checkpoint](../05%20Checkpoint%20Syntheses/MT_V11_KNOWLEDGE_AND_DUTY_CHECKPOINT.md) owns activation and disclosure review. New knowledge of earlier events is not automatically present personality change.


## V12 updates — 2026-09-27 UTC

Prior V01–V11 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V12; immutable input audited V11 `0670b4dfc16a7a5a6c0e35dc62d520f90758a3a5`. Observation suffixes resolve in [V12](../02%20Sequential%20Readings/MT_V12_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V12-`. The [V12 checkpoint](../05%20Checkpoint%20Syntheses/MT_V12_LOSS_AND_HOUSEHOLD_CHECKPOINT.md) owns targeted loss/household review. Revealed earlier events and current changes retain different times; semantic acceptance, publication/audit and main integration remain separate.

| State / local key | Prior → V12 state / kind | Observations / limitation |
| --- | --- | --- |
| `MT-S-181` / Rudeus | Arrival → corrected reunion expectations, tested book, reckless rescue then controlled inquiry. KNOWLEDGE/PRACTICE. |001–014; improvement local, withheld motive and inaccurate appraisal persist. |
| `MT-S-182` / Rudeus | Coordinated combat → sensory interpretation failure, lost hand, bereavement and withdrawal. CONTEXT. |015–021; grief self-judgment not diagnosis or sole-cause finding. |
| `MT-S-183` / Rudeus | Receives care → renewed function, affair acknowledged, proposal and consultation. PRACTICE/RELATIONSHIP. |020–025/029–030; relief not cure, possible-pregnancy premise corrected, violent intention unexecuted but recurrent. |
| `MT-S-184` / Rudeus | Home return → misreads Aisha, accepts correction, parenthood and grave undertaking. KNOWLEDGE/PRACTICE. |026–034; responsibility continuing, not completed moral transformation. |
| `MT-S-185` / Paul | Exhausted searcher → reunion joy/apology, patient leadership and ordinary maintenance. CONTEXT/PRACTICE. |001–006/011–012; original companion quarrel unknown, ignored Lilia protest remains. |
| `MT-S-186` / Paul | Sees Zenith → rash attack, force, revised cooperation, protects son and dies. CONTEXT/TERMINAL_EVENT. |013–017; death closes present behavior, not historical accountability or all interpretation. |
| `MT-S-187` / Roxy | Missing → independent survival and life review, rescued before recognizing pupil. REVEALED_NOT_NEW/CONTEXT. |007–009; month of work precedes rescue, no telepathic bond established. |
| `MT-S-188` / Roxy | Rejoined expedition → tactical authority, correction and shared bereavement. PRACTICE/KNOWLEDGE. |009–020; first learns marriage in companion discussion. |
| `MT-S-189` / Roxy | Comfort/desire → confession, temporary arrangement refused, conditional proposal and teaching job. RELATIONSHIP/PRACTICE. |020–024/030/032; denies pregnancy, care and opportunism coexist. |
| `MT-S-190` / Sylphiette | Waiting pregnant spouse → asserts decision, welcomes Roxy, discloses fear, becomes mother. RELATIONSHIP/CONTEXT. |030/032–033; bodily limits persist, public agreement not equal power. |
| `MT-S-191` / Norn | Waiting sister → grief, care for Aisha, marriage objection, ongoing attachment/learning request. KNOWLEDGE/PRACTICE. |026–027/029–031; legitimate hurt and overstepping distinguished. |
| `MT-S-192` / Aisha | Household worker → capable reception, restrained joy, reunion, criticism and birth assistance. PRACTICE/KNOWLEDGE. |027/031/033; service performance not transparent emotion or adult independence. |
| `MT-S-193` / Lilia | City support → chooses ongoing care, reunites with Aisha, skilled midwifery. PRACTICE. |004/022/027/033; attachment and reproduced hierarchy coexist. |
| `MT-S-194` / Zenith | Located in crystal → awake with altered communication, learning/actions/preferences observed. CONTEXT/KNOWLEDGE. |013/016/018/032; cause, experience and prognosis unknown; personhood not negated by narrator label. |
| `MT-S-195` / Elinalise | Reunion/apology → protective combat, independent refusal, marriage persuasion and shared blame. PRACTICE/KNOWLEDGE. |002/013–015/019/024/028; denied pregnancy claim does not independently prove exact intent. |
| `MT-S-196` / Geese and Talhand | Search collaborators → complementary planning/protection, bereavement and independent future. PRACTICE. |003/006/010/015/019/022/028; labor for Paul not merely debt to Rudeus; motives not uniform. |
| `MT-S-197` / Vera and Shierra | City support → scrolls, boundaries, mourning and chosen departure. PRACTICE. |009–010/028; romantic meaning of loyalty unverified. |

| Package | Current maintenance decision | Debt |
| --- | --- | --- |
| Rudeus1.9; Paul1.3; Roxy1.3 | Targeted model/index revisions. | Separate grief, combat, prior knowledge and later interpretation; Paul's posthumous voice unavailable. |
| Sylphiette1.4; Elinalise1.2; Norn1.1; Aisha1.1 | Targeted model/index revisions. | Independent aims and refusals, unequal information and family costs; no universal tolerance rule. |
| Zanoba1.3; Cliff1.2; Nanahoshi1.2; Eris1.4; Ruijerd1.2; Sara1.0 | Reviewed, no material operational update; exact earlier files preserved. | No direct equivalent present opportunity; reports/memories not enough for new general rule. |
| Lilia, Zenith and expedition cast | Expanded evidence/state ledger; new operational packages deferred. | Concentrated contexts and uneven interior access; do not force package symmetry. |

All models BOUNDED_PROVISIONAL; no DOMAIN_READY or global enrollment. Rudeus monograph remains V01–V10. The [V12 checkpoint](../05%20Checkpoint%20Syntheses/MT_V12_LOSS_AND_HOUSEHOLD_CHECKPOINT.md) owns maintenance reasoning.


## V13 updates — 2026-09-27 UTC

Prior V01–V12 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V13; immutable input audited V12 `e1018971ce195163277565ca1e4e7e298332bb21`. Observation suffixes resolve in [V13](../02%20Sequential%20Readings/MT_V13_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V13-`. No new specialist checkpoint is required; the cumulative V15 checkpoint remains prospective. Revealed earlier events and current changes retain different times; semantic acceptance, publication/audit and main integration remain separate.

| State / local key | Prior → V13 state / kind | Observations / limitation |
| --- | --- | --- |
| `MT-S-198` / Rudeus | Grieving new parent → repeated care, research, teaching and skill acquisition. PRACTICE/CONTEXT. |003/007–008/012–016; capacity and interpreted intention remain distinct, no universal competence. |
| `MT-S-199` / Rudeus | Family authority assumed → corrections about privacy, work, permission and dependence. KNOWLEDGE/PRACTICE. |004–010/015/020/032; some apologies and changed judgments, repeated intrusive conduct persists. |
| `MT-S-200` / Rudeus | Anticipates Sara rejection → admits avoidance/rebound, repairs companionship. RELATIONSHIP. |025–027; romance explicitly closed; future fidelity promise immediately qualified in thought. |
| `MT-S-201` / Roxy | New spouse/teacher → professional recognition, specialist instruction and successful escort leadership. PRACTICE. |002/004/010/015–016/024; teaching exhaustion and own work choice matter. |
| `MT-S-202` / Roxy | Household insecurity → voiced limits, birthday preparation and reported fuller acceptance. RELATIONSHIP. |017–018/021/023; report after hat scene, not retroactive proof of comfort. |
| `MT-S-203` / Sylphiette | New mother/co-spouse → continuing paid work, explicit bodily principle, welcome and negotiated terms. PRACTICE/RELATIONSHIP. |004/015/017–018/020/023/025/027–028/032; insecurity and agency coexist; no unlimited marriage permission. |
| `MT-S-204` / Norn | Requested lessons → wanted but difficult training, authorship, birthday recognition. PRACTICE. |008–009/014/020–022; injuries and unwanted affection not erased by desire to learn. |
| `MT-S-205` / Norn | Reader/brother incompletely informed → established council work disclosed. REVEALED_NOT_NEW. |028/032; work already over a year old, not caused by latest sword lessons or permission. |
| `MT-S-206` / Aisha | Skilled household worker → garden expertise, defended secret, sibling celebration and Lucy care. PRACTICE. |010/014/020–022/028; withheld grief not excluded by cheer, blackmail and dependence remain. |
| `MT-S-207` / Zenith | Altered communication → initiates childcare, recurring smiles and family recognition. OBSERVED_CHANGE. |007/012/022/028; experience, cause and recovery remain unknown. |
| `MT-S-208` / Lilia | Caregiver enforcing rank → matching gifts recognize both daughters while service hierarchy persists. PRACTICE. |020/022; local flexibility, no complete institutional reversal. |
| `MT-S-209` / Sara | Missed V07 apology → professional advancement, intended repair, explicit friendship and romance boundary. PRACTICE/RELATIONSHIP. |025–026; current aims not hidden renewed courtship; offstage career mainly report. |
| `MT-S-210` / Cliff | Ongoing researcher → concrete prosthetic collaboration, dependence critique and modest wedding. PRACTICE. |003/006/013/018–019; advice not mind access; drug use/knowledge unshown. |
| `MT-S-211` / Zanoba | Doll research → prosthetic hand/leg work, shared array construction, craft recognition. PRACTICE. |003/013–014/031; own purpose retained, autonomous doll/core unfinished. |
| `MT-S-212` / Elinalise | Returning partner → marriage preparation, practical help and intimate mediation. PRACTICE. |018–019/028; Cliff declines funding, no assumed administration of received drug. |
| `MT-S-213` / Nanahoshi | Researcher with prior distress → continuing illness, social correction/care, experimental breakthrough. PRACTICE/CONTEXT. |029–031/033; progress and joy not cure or abandonment of return aim. |
| `MT-S-214` / Linia and Pursena | Graduation approaches → chosen duel to avoid imposed marriage, separate intended departures. PRACTICE. |030; plans not completed careers; same-bus account rumor. |
| `MT-S-215` / Eris | Intensive training → accepts counter-style problem, reciprocal exchange and purposeful rest. PRACTICE. |034–037; Rudeus uninformed; further-year result belongs narrator projection. |
| `MT-S-216` / Nina and Isolte | Uneven initial appraisal → complementary skills, mediation and shared training. PRACTICE. |034–037; unconscious Isolte not consulted initially, prejudice only locally corrected. |
| `MT-S-217` / Suzanne | Former party companion → married parent, daughter loss and independent work/care arrangements reported. REVEALED_NOT_NEW. |011/026; premature daughter died after birth, outward lightness not grief absence. |

| Package | Current decision | Debt |
| --- | --- | --- |
| Rudeus1.10; Roxy1.4; Sylphiette1.5; Norn1.2; Aisha1.2 | Revise existing model/index pairs. | Specific permission, independent work and hidden information, not global family harmony. |
| Sara1.1; Cliff1.3; Zanoba1.4; Elinalise1.3; Nanahoshi1.3; Eris1.5 | Revise existing model/index pairs. | New opportunity for repair, collaboration, illness and reciprocal learning; reports/projections qualified. |
| Paul1.3; Ruijerd1.2 | Reviewed, byte-preserved. | Remembrance/attributed teaching not new present conduct. |
| Other named people | Ledger coverage; standalone models deferred. | Uneven contextual/interior access; do not manufacture symmetrical packages. |

All models remain BOUNDED_PROVISIONAL with null global IDs. No DOMAIN_READY. Rudeus monograph remains V01–V10; the required V15 cumulative checkpoint is still prospective.


## V14 updates — 2026-09-27 UTC

Prior V01–V13 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V14; immutable input audited V13 `eece6816d98e076847e65507bc9e83d03b1ed77d`. Observation suffixes resolve in [V14](../02%20Sequential%20Readings/MT_V14_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V14-`. The targeted V14 testimony/agency checkpoint is new; the cumulative V15 checkpoint remains prospective. Revealed earlier events and current changes retain different times; semantic acceptance, publication/audit and main integration remain separate.

| State / local key | Prior → V14 state / kind | Observations / limitation |
| --- | --- | --- |
| `MT-S-218` / Rudeus | Researcher/parent → practical listener and organizer for Nanahoshi. PRACTICE. |006–017; attachment enables empathy without identical aims; help distributed. |
| `MT-S-219` / Rudeus | Wants learning and return → coerced captive, endangered fighter, returned diarist. PRACTICE/CONTEXT. |018–027; collective survival, lethal intent and collateral injury; resolve not completed durable change. |
| `MT-S-220` / Rudeus | Trusts detailed oracle → receives elder testimony, finds rat, conceals danger. KNOWLEDGE. |028–034; present young self does not acquire elder experience; diary unread, letter begun. |
| `MT-S-221` / Roxy | Working spouse → excluded visitor, logistical helper and speaker asking openness. CONTEXT/PRACTICE. |002/011/015/026/033; stated agreement within racial exclusion; pregnancy hinted, future death only report. |
| `MT-S-222` / Sylphiette | Working mother → costly healer, recovering caregiver, continuing Ariel aide. PRACTICE. |001/009–011/015/022/026/033; jealousy/fear and direct preference coexist; no perpetual marital permission. |
| `MT-S-223` / Zanoba | Researcher/craft admirer → host connection and endangered protector. PRACTICE. |004/008/016/019–025; own purposes, injury and instrumental treatment of Kishirika retained. |
| `MT-S-224` / Cliff | Newly married researcher → duty advocate, charitable searcher, healer and new eye user. PRACTICE. |012/014/017/019–022; eye currently uncontrolled, curse cure incomplete. |
| `MT-S-225` / Elinalise | Partner with concealed history → selective disclosure and tactical care. REVEALED_NOT_NEW/PRACTICE. |005/012/014/019–022; Cliff already knew before marriage; ancient memory gap persists. |
| `MT-S-226` / Nanahoshi | Ill researcher → Draine diagnosis, continuing treatment and clarified homeward attachment. CONTEXT/REVEALED. |007/011/013/023; tea management not permanent cure; elder future report not present outcome. |
| `MT-S-227` / Eris | Intensive trainee → adaptive victory, Sword King/full transmission, intended return. PRACTICE. |035–036; planned sacrifice is intention, no reunion or actual Orsted victory. |
| `MT-S-228` / Perugius | Proposed expert contact → limited teacher/patron, racial gatekeeper, rescuer through revenge. REVEALED/PRACTICE. |003–008/012/021/024–026; one concession does not end prejudice; displacement inference bounded. |
| `MT-S-229` / Atofe and Moore | New power center → coercive reward regime with useful aid and effective opposition. REVEALED. |017–021; help and coercion coexist; not all guards willing. |
| `MT-S-230` / Ariel | Facilitates visit → materially assists expedition and faces unresolved royal test. PRACTICE. |001/014/026; rings unused, king answer not established. |
| `MT-S-231` / Nina and Gino | Training peers → distinct ambition, defeat/disappointment and renewed effort. PRACTICE. |035–036; continued work exceeds Eris departure plot. |
| `MT-S-232` / elder visitor | Claims later Rudeus identity and branch history, demonstrates powers, dies. ATTRIBUTED/OBSERVED. |029–032; identity support and rat warning strong locally; no younger model overwrite or new operational package. |

Eight model/index pairs revised: Rudeus1.11, Roxy1.5, Sylphiette1.6, Zanoba1.5, Cliff1.4, Elinalise1.4, Nanahoshi1.4, Eris1.6. Paul1.3, Ruijerd1.2, Norn1.2, Aisha1.2 and Sara1.1 are reviewed and byte-preserved: no material new operational opportunity. New prominent figures stay ledger-level pending sufficient contexts and architecture need. All models BOUNDED_PROVISIONAL, null global IDs; no DOMAIN_READY or clean forecast. [V14 checkpoint](../05%20Checkpoint%20Syntheses/MT_V14_TESTIMONY_AND_AGENCY_CHECKPOINT.md) governs testimony distinctions; V15 cumulative review remains due.
