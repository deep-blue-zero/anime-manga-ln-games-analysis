---
title: "Mushoku Tensei - Character state and readiness ledger"
artifact_id: MT_CHARACTER_STATE_AND_READINESS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.5"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V05 only; prior history preserved, V05 candidate updates; publication/audit separate."
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
