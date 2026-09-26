---
title: "Mushoku Tensei - Character state and readiness ledger"
artifact_id: MT_CHARACTER_STATE_AND_READINESS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.9"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V09 only; prior history preserved, V09 updates; publication/audit separate."
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
