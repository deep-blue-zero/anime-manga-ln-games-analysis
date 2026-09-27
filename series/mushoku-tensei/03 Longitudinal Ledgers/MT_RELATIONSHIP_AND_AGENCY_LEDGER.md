---
title: "Mushoku Tensei - Relationship and agency ledger"
artifact_id: MT_RELATIONSHIP_AND_AGENCY_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.10"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V10 only; prior history preserved, V10 updates; publication/audit separate."
---

# Relationship and agency ledger

## Responsibility

Owns directional relationships, independent goals, initiative, refusal, constraints, trust, obligation, dependency, power and repair. Neither reciprocal feeling nor romance is presumed.

## Record format

`relationship event ID | A | B/group | direction | observation refs | goals | knowledge | choices/constraints | initiative/refusal/repair | prior state/change | reciprocity evidence | uncertainty`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Record A-to-B and B-to-A separately when supported. Append events and update current states with links; preserve prior directional history and distinguish choice from pressure. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

`MT-LNJP-V01` only. Observation numbers below resolve in the [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). These are directional relations, not reciprocal labels or global registry entries.

| Event ID / direction | Initiative, goal, constraints, and change | Basis / uncertainty |
| --- | --- | --- |
| `MT-R-001` `Roxy → Rudeus` | Accepts paid teaching, adapts instruction, accompanies him outside and offers a limited protective keepsake; leaves for her own advancement. | `006–008,015`; she does not claim to know his trauma or promise indefinite availability. |
| `MT-R-002` `Rudeus → Roxy` | Learns and respects her; also objectifies and steals intimate property. Gratitude and boundary violation coexist. | `006–008,015`; her later letter notices theft, but does not establish prior consent. |
| `MT-R-003` `Rudeus → Sylphie` | Intervenes in bullying and shares literacy/magic, then overrides refusal, tries to manage her response and imagines shaping her future; both care and control are observed. | `009,011–012,015–016`; his romance reading is not her reported goal. |
| `MT-R-004` `Sylphie → Rudeus` | Seeks friendship and instruction, refuses physical exposure, resumes some shared activity while retaining distance, voices desire for ordinary treatment, opposes separation. | `009,011–012,016`; no direct adult preference or consent to future partnership is established. |
| `MT-R-005` `Paul → Rudeus` | Provides training, errs and apologizes after a one-sided accusation; later forcibly arranges paid tutoring and a five-year no-contact term to break perceived dependency. | `006,010,012,016`; good intentions and job benefit do not equal advance consent. |
| `MT-R-006` `Rudeus → Paul` | Seeks approval and instruction, challenges unfair punishment, admires sword competence but criticizes sexual/family conduct; accepts some reasoning only after removal. | `006,010,015–016`; partial post hoc understanding is not agreement to the method. |
| `MT-R-007` `Lilia → household` | Chooses rural employment for pay/safety, supplies professional/daily care, reports her pregnancy and offers to leave, later commits to continued service. | `004,013–014`; employer power, limited money and earlier harm constrain available choices. |
| `MT-R-008` `Zenith → Lilia/Aisha` | Anger and threatened rupture coexist with concern for travel/child; permits Lilia to stay and chooses to feed Aisha when needed. | `013–014`; her faith-related conflict remains explicit. |
| `MT-R-009` `Lilia → Zenith/Rudeus` | Feels she betrayed Zenith, credits Rudeus with protecting her and resolves to bind the unborn child to his service. | `013`; her debt narrative is her own appraisal, not a fair contract on Aisha's behalf. |
| `MT-R-010` `Rudeus → Lilia/Zenith` | Values Lilia's understated care and fears her dangerous departure; fabricates a coercion claim to influence Zenith and later admits the fabrication to her. | `013–014`; need to distinguish care for them from taking control of their information. |
| `MT-R-011` `Rolls/Paul → Sylphie` | Rolls discusses her isolation with Paul; Paul chooses separation to expand her independence; at departure Rolls speaks to her, exact counsel not reported. | `009,016`; Sylphie's protest and her own alternatives are not fully represented. |
| `MT-R-012` `Ghislaine ↔ Rudeus` | Proposed reciprocal instruction: sword teaching for reading and arithmetic; at the V01 ending only the arrangement and her request are known. | `016`; neither party's later teaching is observed. |

**V01 directional limit:** The house calls Lilia “family” while her wage and servant history persist; the word does not erase employment dependency. Sylphie's closeness is not evidence of unrestricted access to her body or her future. The five-year separation is Paul's decision, with its effectiveness and consent unresolved. Later evidence must be linked as new events rather than silently converted into current V01 motives.

## V02 directed events — 2026-09-26 UTC

The V01 events remain historical. New evidence numbers below refer to [V02 canonical observations](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V02-`. Current scope V01–V02; input audited commit `eaf159559c6fc76ddd820178d7588545f08c351d`.

| Event / direction | Initiative, constraints and changed options | Evidence / reciprocity and limit |
| --- | --- | --- |
| `MT-R-013` Rudeus → Eris | Engineers fear to obtain employment/cooperation, rescues and teaches, later coordinates rest and adaptive practice. | `001–008`; helpful outcomes do not prove the staged scheme necessary. Financial/class asymmetry is complex: pupil's household employs him, he controls practical knowledge. |
| `MT-R-014` Eris → Rudeus | Rejects teacher, later grants familiar address, returns to practice, wants to give a book, initiates birthdays and staff gift. | `004,007–009,012`; choices establish reciprocity beyond obedience, not unrestricted physical permission. |
| `MT-R-015` Rudeus → Eris | Particular restraint while she cherishes gifts; later exceeds limited permission, recognizes disregard and apologizes. | `009,014`; regained hope becomes entitlement to a future prize in his account. No demonstrated transfer of new vow yet. |
| `MT-R-016` Eris → Rudeus | Stops a violation, leaves, returns to forgive on this occasion and sets a five-year limit. | `014`; no irrevocable contract over future intimacy; her return does not ratify the violation. |
| `MT-R-017` Ghislaine → Rudeus | Protects life, cautions against overconfidence, adapts sword instruction and considers another teacher conditional on his wishes. | `003,006–007,011,017`; gratitude and fallible appraisal both present. |
| `MT-R-018` Rudeus → Ghislaine | Patient literacy/magic instruction, formal learner recognition, food reserved while she works; also sexualizes her and exploits her distraction role. | `006–012`; her artistic wish to record herself differs from his intention. Respect is not complete mutual understanding. |
| `MT-R-019` Ghislaine → Eris | Longstanding teaching/protection, personal ring, later urgent search. | `006–009,011,017,019`; duty persists on holiday; disorientation produces harmful force beyond controlled rescue. |
| `MT-R-020` Eris → Ghislaine | Admires expertise, listens to experience, treasures ring, seeks additional practice. | `006–009,011`; relationship predates Rudy and retains independent significance. |
| `MT-R-021` Roxy → Rudeus | Creates substantial guide, maintains correspondence, independently chooses search for him. | `010,015,018`; he is a respected pupil, not her declared lover. Idealization can obscure his limits. |
| `MT-R-022` Rudeus → Roxy | Gratitude and study depend on her labor; likeness made and sold without demonstrated permission disturbs her on arrival. | `010`; narrator's comedy does not settle her experience. |
| `MT-R-023` Philip/Sauros/Hilda → Rudeus/Eris | Resources, belonging and gratitude coexist with violence, gendered performance and proposed marital/political recruitment. | `004–005,008,012–013`; Hilda's grief is Philip-reported, her embrace observed. Affection need not be fictitious for constraints to be real. |
| `MT-R-024` Roxy → prince/court | Refuses coercion, uses contract/relative status, leaves at term end and repels attack. | `015`; court's judgment protects its interests as recorded; no broad equality guarantee. |
| `MT-R-025` Paul → scattered family/Rudeus | Protects Norn per message, requests assistance, prioritizes missing wives/Aisha and assigns Rudy a northern search. | `018`; Rudy not shown reading message. Trust and delegated burden coexist; necessity remains untested. |
| `MT-R-026` Ghislaine → Vigo / Vigo → Ghislaine | Her search-driven intervention enables his survival; he recognizes a protective purpose, accompanies her and later memorializes her. | `019`; their immediate directions partly coincide, their goals and later knowledge differ. Cult does not establish her endorsement. |

**Reviewed limits:** no new direct Sylphie→Rudeus event; his recollection is not her choice. No missing-person listing proves death. Relationship states after displacement are not simply household states moved intact to a new place.


## V03 updates — 2026-09-26 UTC

Prior V01/V02 bodies remain historical and unchanged. Current scope is Japanese LN V01–V03; input is audited V02 head `687a13ac1a661270ab566c9e1a6028acd607d846`. Observation suffixes below resolve in [V03's diagnostic readings](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V03-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Directed event | Initiative / constraint / changed options | Observation / limit |
| --- | --- | --- |
| `MT-R-027` Rudeus → Ruijerd | Chooses provisional trust, offers reputation work, controls disguise and partial information, negotiates killing limit but uses fear himself. | `002,004,006,011–013`; empathy and instrumental dependence coexist. |
| `MT-R-028` Ruijerd → Rudeus/Eris | Rescues, escorts, teaches, feeds/protects; also kills and intimidates under protective code. | `002,005,011–012`; care does not guarantee proportionate force or good category judgment. |
| `MT-R-029` Ruijerd → Rudeus | Takes public blame and later offers escort without reputation repayment; credits incomplete protective account. | `017–018`; sacrifice changes choices, not complete absolution or knowledge. |
| `MT-R-030` Rudeus → Ruijerd | Chooses continued help after payment condition removed; identifies shared exclusion but differentiates histories. | `018–020`; gratitude genuine; concealed publicity allocation persists. |
| `MT-R-031` Rudeus → Eris | Comforts fear and refrains in one comparable opportunity, yet later intrudes and requires others' enforcement. | `009,020`; recognition distinct from durable respect. |
| `MT-R-032` Eris → Rudeus | Yields outing, values gift, protects him from grip, expresses excessive faith, raises grievance and gives advice. | `008–009,012,019–020`; care, refusal and pressure coexist; not unrestricted permission. |
| `MT-R-033` Party → each member | Consultation channel includes Eris, preserves leader's final decision, changes practical plans; shared training and enforcement. | `019–020`; not equal information/authority or always followed. |
| `MT-R-034` Roxy/parents → travelers; Rudy → parents | Guide/pendant enable access; parents supply money/sword without demanding daughter return; pupil provides news and promises contact. | `003`; promise not completed communication; absent Roxy motives not recreated. |
| `MT-R-035` Rudeus/Ruijerd → Jalil/Veskel; pair → clients/party | Killing/threats constrain bargain; pair supplies actual skilled work and publicity, later flees; Rudy releases and thanks them. | `011–013,016–017`; useful labor not freely negotiated contract or repaired past harm. |
| `MT-R-036` Trio ↔ Kurt/Meisel/clients | Service and rescue elicit genuine gratitude; delay causes irreversible loss; incomplete knowledge shapes credit and later fear. | `010,014,016–017`; sincere praise not moral verification. |
| `MT-R-037` Derrick → Ariel / Ariel → Derrick | Urges crown, risks and loses life protecting; she initially doubts him, seeks help, then accepts dying request. | `021–022`; reciprocity changes, future rule untested. Political program not pure universal good. |
| `MT-R-038` Institutions/public → party | Guild enables work but polices reporting; extortion exploits violation; guards assign innocence/guilt by age and feared identity. | `007,016–017`; wrongdoing and discriminatory blame both actual dimensions. |

No direct new Sylphie→Rudeus, missing-family reunion or successful Roxy-search event is established. The extra's unnamed arrival supplies no authorized identity shortcut.


## V04 updates — 2026-09-26 UTC

Prior V01–V03 bodies remain historical and unchanged. Current scope is Japanese LN V01–V04; input is audited V03 head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Observation suffixes below resolve in [V04's diagnostic readings](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V04-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Directed event | Initiative / constraint / changed options | Observations and limit |
| --- | --- | --- |
| `MT-R-039` Rudeus → Ruijerd | Refuses abandonment, proposes costly staff sacrifice in secret, accepts challenged meaning and smuggling revision. | `001,005`; loyalty not complete disclosure. |
| `MT-R-040` Ruijerd → Rudeus/Eris | Protects gift relationship, changes practical plan, yet assigns warrior independence after capture. | `005,011,019`; care and excessive expectation coexist. |
| `MT-R-041` Rudeus → Eris | Recognizes effort grievance; supplies unpoliced illness care/restraint then pressures terms; conceals dangerous job. | `004,008–009`; affection/promise not general consent practice. |
| `MT-R-042` Eris → Rudeus | Voices asymmetry, seeks care, defends against mistreatment and admires teaching. | `004,008,015,018`; limited permission/dependence and retaliation distinguished. |
| `MT-R-043` Eris → Ghislaine / Gyes | Defends independent mentor loyalty without striking; supplies concrete later learning evidence. | `016,018`; no new present Ghislaine action; Gyes's earlier hurt not erased. |
| `MT-R-044` Eris ↔ Minitoona/Tersena | Teaches, plays, resists insults, partially limits retaliation; girls initiate reconciliation, mutual tearful farewell. | `018,021`; friendship self-directed, discussion partly inaccessible, no total nonviolence. |
| `MT-R-045` Roxy ↔ Elinalise/Talhand | Shared search, care, incompatible priorities and errors shape route/missed contact. | `006–007`; Roxy own damage/omission retained, others' reported curse/history not disproved by her appraisal. |
| `MT-R-046` Rudeus/Ruijerd → captives | Healing/release/protection joined to killing, gratitude demand and missing aftercare plan. | `009–011`; beneficiaries' thanks not full assessment of means. |
| `MT-R-047` Gyes/Lakrana → Rudeus | Mistaken coercion → apology, gratitude/hospitality; Gyes later enforces daughter's boundary. | `011–012,015,018,020`; different episodes have different factual grounds. |
| `MT-R-048` Rudeus → village | Resentment yields to immediate rescue and chosen aid; later asks consent for paid guard work. | `013,015,017`; civic help not personal innocence or universal self-sacrifice. |
| `MT-R-049` Geese → Rudeus/party | Vest, tactical aid, cooking and social negotiation secure temporary companionship. | `012,014,022`; not permanent party entry, old biography attributed. |
| `MT-R-050` Rudeus → Geese | Performance shifts to gratitude, suspicion/resentment partly recognized, advocacy for teaching Eris. | `012,022`; genuine debt does not authenticate every report. |
| `MT-R-051` Geese → Eris | Refuses requested cooking instruction using superstition arising from reported loss. | `022`; combat-only explanation withdrawn, personal pain does not prove causal rule. |
| `MT-R-052` Sacred beast ↔ Rudeus | Independent combat help, translated food provision and everyday affection; Rudy adjusts expectations of child understanding. | `014,020`; no hero prophecy confirmed or complete understanding presumed. |
| `MT-R-053` Ariel → Fitts / Fitts → Ariel | Shelter/search bargain and political use, coercive teasing then shared comfort; fearful service develops chosen renewed defense. | `023–026`; hoped unconditional acceptance untested, care does not erase dependence. |
| `MT-R-054` Luke → Fitts / court → trio | Luke offers practical comfort/help but fails ally during unwanted invitation; gossip becomes strength recognition after attack. | `023–026`; recognition does not end danger or establish fair hierarchy. |

Missing-family/Sylphie relationships receive no invented current events. Boreas servitude is now questioned, not established as uniformly supplied by abduction. The extra's alias remains separate from any unverified earlier name.


## V05 updates — 2026-09-26 UTC

Prior V01–V04 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V05; frozen published input is audited V04 head `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. Observation suffixes below resolve in [V05's diagnostic readings](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V05-`. The [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) owns the historical cumulative synthesis; publication/audit remain separate from this preparation snapshot.

| Directed event | Initiative / constraint / options | Observation and limit |
| --- | --- | --- |
| `MT-R-055` Rudeus → Paul | Entertaining account, accusation and retaliation → receives care, initiates reenacted reunion, accepts options and aid. | `007–012`; actual omissions and false inferences differ; later broad excuse is not the analyst's verdict. |
| `MT-R-056` Paul → Rudeus | Assumes knowledge and capacity, strikes → listens/apologizes, supplies money, options and warning. | `006–007,009,011–014,020`; repair does not prove permanent reform. |
| `MT-R-057` Paul ↔ Norn / Norn → Rudeus | Bodily care and attachment; daughter protects father and refuses brother despite pressure. | `004–007,015,020`; her experienced history differs from the men's shared account. |
| `MT-R-058` Eris → Rudeus | Protective rage, awkward comfort and disagreement with forgiveness; independent information unshared. | `008,013,017`; care does not give a veto over his relationships. |
| `MT-R-059` Rudeus → Eris | Accepts hunt, credits comfort, states respect for refusal, discloses Fittoa loss, permits meal with a condition. | `002,012–015,020`; intention is not durable consent practice; she may disagree. |
| `MT-R-060` Ruijerd → party / old friend → Ruijerd | Listens, directs care and restrains Eris; old rescue becomes a letter and welcome. | `008,013–014,021`; extent of force partly unknown; friendship is not an institutional solution by itself. |
| `MT-R-061` Geese → Paul/Rudeus | Corrects father, reports jail rescue plan, continues search. | `009,020`; omitted news and jinx motives remain partial. |
| `MT-R-062` Vera → Shela / Rudeus → women | Diverts attention and shields; Rudy apologizes for infidelity accusation yet misreads gaze/fear. | `010`; practical care and continuing distress are not sexual availability. |
| `MT-R-063` Shela/Vera/Alphonse → search/family | Funds, schedules, refugee help and resources expand options. | `005,010,014–015`; collective work is not Paul's sole achievement. |
| `MT-R-064` Zenith/Lilia/Paul → Sylphie; women ↔ household | Reported teaching and negotiated domestic terms. | `012`; past report, not current encounter or proof of coercion's necessity. |
| `MT-R-065` party → village / village → party | Effective hunt and publicity offer; thanks given but figurine and religious acceptance refused. | `016`; personal gratitude does not entail general reform. |
| `MT-R-066` Eris ↔ Cliff | Intervenes, strikes, judges coordination, refuses proposal; Cliff admires and misreads. | `018–019`; refusal is unambiguous; talent grants no entitlement. |
| `MT-R-067` Eris ↔ Therese | Child rescue with knight assistance; misread credit creates personal gratitude. | `019,022`; heroic appearance conceals fear and support. |
| `MT-R-068` Therese → party | Jurisdiction, kinship and debt win passage and medicine; demon prejudice and uncomfortable handling remain. | `021–022`; exception helps without universal acceptance. |
| `MT-R-069` Roxy ↔ parents | Spoken welcome doubted; tears/shared hug change immediate departure. | `023`; communication difference unchanged; three-day stay is not permanent repair. |
| `MT-R-070` Roxy → pupil/missing people / companions | Corrects missed identity, values pupil, prioritizes remaining search with others. | `024`; embarrassment and biased praise coexist with care. |
| `MT-R-071` Gustav → client | Accepts paid inquiry, delivers false certainty, recognizes error but withholds repair. | `026–028`; later harm announced, precise consequence not yet known. |
| `MT-R-072` Ariel ↔ officials | Voice/presence restore loyalty; shared cover permits risky discretion; guards join. | `026`; official testimony idealizes, no impartial reform proved. |
| `MT-R-073` Fitts ↔ guards/wards | Support magic protects wards; allies die protecting caster. | `027`; power is not invulnerability, witness's identity inference fails. |
| `MT-R-074` Rudeus → Randolph / Shagall → Randolph | Excessive criticism followed by unseen business closure and recruitment. | `025`; shame visible, later career benefit unestablished. |

The repaired father–son relation does not transfer automatically to Norn, Eris or the women present. Missing relatives retain prior independent stakes; no offstage consent, romance or identity is invented.


## V06 updates — 2026-09-26 UTC

Prior V01–V05 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V06; frozen input is final audited V05 head `3dc6b173b044abdafc013dc989bd96914620d13d`. Observation suffixes below resolve in [V06's diagnostic readings](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V06-`. The [V06 disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews altered premises; the V01–V05 cumulative checkpoint remains historical. Publication/audit remain separate from this preparation snapshot.

| Directed event | Initiative / constraint / available options | Observation and limit |
| --- | --- | --- |
| `MT-R-075` Rudeus → companions | Requests detour help and accepts ideas while withholding adviser; later broadly discloses to Rui after direct question. | `002,004,019`; cooperation not initial informed agreement; Eris not present for full night disclosure. |
| `MT-R-076` Ruijerd → Rudeus | Immediate bodily care, hostage rescue, defense, relevant inquiry and equal farewell. | `002,010,016,019–020`; care survives warrior status, power has limits. |
| `MT-R-077` Rudeus → Ruijerd | Protective secrecy → qualified hope, privacy for tears, acknowledged autonomy and valued pendant. | `002,019–020`; no full metaphysical certainty, no right to extend escort indefinitely. |
| `MT-R-078` Eris → Ruijerd / Ruijerd → Eris | Sustained practice, meaningful recognition, farewell instruction and guarded emotion. | `014,020,024`; new report of training hit qualifies Rudy's account; no invulnerability. |
| `MT-R-079` Rudeus → Aisha | Prompt rescue/care and defense against assigned role coexist with esteem management and misleading conditional offer. | `005–006,012–013`; not pure exploitation or perfect honesty. |
| `MT-R-080` Aisha → Rudeus | Seeks aid, questions reputation, recognizes alias, chooses admiration and later service interest. | `006,013,029`; age, upbringing and overcredited rescue limit fully independent judgment. |
| `MT-R-081` Lilia → Rudeus / Rudeus → Lilia | Lilia offers devotion and proposed daughter service; Rudeus rejects sole credit and the proposal, supplies funds and travel advice. | `011–012`; Lilia knows the escorts and court, while gratitude and subordinate dependence persist. |
| `MT-R-082` Lilia → Aisha | Teaches useful skills, protects from immediate threat, imposes future role; rare praise/embrace. | `012,029–031`; affection real, choices constrained. |
| `MT-R-083` Aisha → Lilia | Resists unexplained purpose, teases through superior information, welcomes unexpected affection. | `029,031`; changed admiration does not validate all prior controls. |
| `MT-R-084` Ginger / soldiers → captives / Zanoba | Separate plans under hostage pressure; craft interest recruits force, freed families enable action. | `007–010`; lethal methods and withheld information remain, not one Rudy plan. |
| `MT-R-085` Zanoba ↔ Rudeus | Craft admiration creates pupil/master authority; liberation bargained for, later gratitude/fear and injury coexist. | `009–011`; no harmless eccentric or universally benevolent teacher. |
| `MT-R-086` Orsted → party / Nanahoshi → Orsted | Initial departure turns to attack at Hitogami name; intervention followed by reported healing. | `015–018`; motives/knowledge mechanism unresolved, help does not erase attempted killing. |
| `MT-R-087` Hitogami ↔ Rudeus | Negotiated advice, beneficial outcome, challenged omission and partially accepted explanation. | `002,011,017`; noticed contradiction survives; actual motive not established. |
| `MT-R-088` Rudeus → Eris | Credits training yet retains child framing; care/promise, respects solitude and choice; assumes shared future then rejection. | `014,018,021–023,026`; boundary failures and hidden fear remain. |
| `MT-R-089` Eris → Rudeus | Protects/tends, idealizes capacity, sees vulnerability, seeks family and chooses distance to train. | `016,018,023–025`; burden self-theory contradicted by actual care; destination deliberately withheld. |
| `MT-R-090` Ghislaine / Alphonse → Eris | Personal welfare versus domain restoration, competing proposals, training accompaniment versus cover story. | `021–022,025–026`; no single retainer speaks her full intentions. |
| `MT-R-091` Rudeus / Alphonse → reconstruction | Practical defenses and continuing domain work despite personal rupture. | `026`; initial desolation not absence of all rebuilding; no proof equitable recovery. |
| `MT-R-092` Roxy → missing family / companions | Gives up reward and reunion, questions vague lead, joins split message mission. | `027–028`; others contribute ideas/access; no completed delivery. |
| `MT-R-093` Kishirika / Badigadi / Elinalise / Talhand → search | Sight, private transport access and divided travel expand possibilities; personal preferences persist. | `027–028`; Roxy misknows sailing party, restriction remains general. |
| `MT-R-094` Paul → Lilia / father → Lilia | Historical assault and flight versus refusal to force marriage and alternative employment route. | `030`; causal setting not excuse, later family attachment not retroactive consent. |

Reciprocity is tested by information and options, not only declarations of love or thanks. The two central departures have different communication structures and cannot be collapsed into a universal abandonment pattern.


## V07 updates — 2026-09-26 UTC

Prior V01–V06 bodies remain historical and unchanged. The current source boundary is Japanese LN V01–V07. The entering freeze used audited V06 head `0e72e531278055c0dbb7a6054285337a1cc37a93`; later repository reconciliation does not change that analytical input. Observation suffixes resolve in [V07](../02%20Sequential%20Readings/MT_V07_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V07-`. The [recognition checkpoint](../05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md) owns the focused comparison. Publication and exact-head audit are separate from content acceptance.

| Directed event | Initiative / constraint / change | Observation and limit |
| --- | --- | --- |
| `MT-R-095` Suzanne → Rudeus | Notices isolation, invites work, later rebukes excessive risk and thanks him; asks Sara about disclosure to Timothy. | `001–003,017,025`; care practical and fallible, no all-knowing substitute parent. |
| `MT-R-096` Counter Arrow → Rudeus | Makes room for a temporary specialist, shares danger and returns to aid him; future search preparations show duty beyond one rescuer. | `004,007,009,014,017`; formal nonmembership differs from absence of attachment. |
| `MT-R-097` Rudeus → Counter Arrow | Low-fee publicity work becomes sought company and accepted dependence, then attachment avoided after rupture. | `007–009,017,024,026`; stated search reason partly masks relational flight, not proof search is fake. |
| `MT-R-098` Sara → Rudeus | Class suspicion yields to differentiated judgment, advocacy for rescue, thanks, invitations and affection. | `006,009,011–012,016–020,025`; not merely grateful payment, transition gradual and privately contested. |
| `MT-R-099` Rudeus → Sara | Trains with, rescues, shops with and feels attraction toward her while framing favor through game/reward analogies and hiding uncertainty. | `003,014–020`; concern and objectification coexist; his reassuring lineage claim contains known contrary evidence. |
| `MT-R-100` Sara → Rudeus | Perceived undesirability prompts defensive denial; real overheard insult, imagined ridicule, explanatory inquiry and intended apology follow. | `020,023,025`; ignorance of condition matters, love does not make all beliefs true. |
| `MT-R-101` Rudeus → Sara | Interprets denial as rejection, disparages her publicly, flees and regrets the result without learning her actual intended confession. | `020–026`; hurt does not erase responsibility; no completed mutual clarification. |
| `MT-R-102` Sara → self / companions | Own survival skills, debt repayment, equipment choice and repair deliberation establish action outside Rudy's knowledge. | `016,018–019,025`; fear eventually inhibits pursuit; no total passivity or invulnerability. |
| `MT-R-103` Soldat → Rudeus | Hostility and norm enforcement → tolerates blows, listens, arranges assistance, interrupts crisis and offers mobile companionship. | `010–011,021–024,026`; apology acknowledges prior harm; stereotypes/mistaken Eris belief remain. |
| `MT-R-104` Rudeus → Soldat | Fear/resentment and aggression → private disclosure, thanks, accepted help and continuing temporary work. | `011,021–024,026`; intimacy in one friendship does not cure romantic fear. |
| `MT-R-105` Timothy / Suzanne → party | Formal/practical leadership, reconciliation with another party, retreat decision, dawn search preparation and mediated inquiry. | `003–004,010,014,017,025`; decisions balance multiple lives, no unlimited rescue obligation inferred. |
| `MT-R-106` Elise → Rudeus | Professional attention, gratitude connected to aid for a child, practical advice and advocacy. | `022,025`; no cure, diagnostic certainty or loss of commercial context. |
| `MT-R-107` Elise → Sara / Sara → confidants | Elise reproaches and reveals private information without knowing Sara's repair intention; Sara sought Suzanne/Timothy's help and later fears pursuing Rudy. | `025`; correction, privacy cost and misreading coexist; mediation fails to create a meeting. |
| `MT-R-108` Rudeus → children / local workers | Free healing, snow clearing, limits negotiated through payment and public recognition. | `013,022`; help concrete, social coercion and commercial institutions persist. |
| `MT-R-109` Rudeus → remembered Roxy / Eris | Roxy remains a revered source of care and imagined highest-stakes rejection; Eris remains wrongly interpreted departure. | `005,020,022,026`; remembered/imagined women are not new direct choices by them. |
| `MT-R-110` Elinalise → Rudeus / mother search | Actively follows reputation and a geographical lead carrying message from prior search. | `027`; arrival, receipt and rescue unobserved. |
| `MT-R-111` Fitts → Ariel / Ariel → Fitts | Loyalty includes anger at bullying; Ariel converts protection/capacity into political strategy and seeks future supporters. | `028–030`; emotional loyalty and instrumental use both present, alias identity remains unresolved. |
| `MT-R-112` Ariel / attendants / Fitts → beast princesses and public | Coordinated provocation, force and selective account produce school advantage. | `029`; prior aggression does not make every tactic proportionate or public belief informed. |
| `MT-R-113` School allies → potential recruits | Discuss capable students and outsiders, with Fitts visibly invested in Rudy's name. | `030`; proposal not acceptance, recognition not completed identity proof. |

Reciprocity requires separate directional records. Affection, gratitude, practical reliance and correct understanding do not appear or disappear together; no later reunion or offstage consent is supplied.


## V08 updates — 2026-09-26 UTC

Prior V01–V07 bodies remain historical and unchanged. Current source boundary: Japanese LN V01–V08. Immutable entering input was final audited V07 `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. Numeric observation suffixes resolve in [V08](../02%20Sequential%20Readings/MT_V08_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V08-`. The [consent and institutional-power checkpoint](../05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md) owns the targeted comparison. Content acceptance, publication/audit and integration to main remain separate states.

| Directed event | Initiative, constraint and change | Observation / limit |
| --- | --- | --- |
| `MT-R-114` Elinalise → Rudy | Delivers news, accompanies, offers professional/contextual knowledge and objects to retaliation. | `002–005,019,029`; assurance not independent Zenith verification. |
| `MT-R-115` Rudy → Soldat | Shares work and farewell, acknowledges possible membership absent search. | `002–003`; attachment survives chosen nonmembership. |
| `MT-R-116` Hitogami → Rudy | Withheld explanation and cure promise redirect decision. | `004`; benefit/purpose unverified, advice not mutual trust. |
| `MT-R-117` Fitts → Rudy | Exam, books, testimony, research and private approach supply distinct forms of help. | `006,008–009,012,025`; no automatic Sylphiette attribution or pure corrective role. |
| `MT-R-118` Rudy → Fitts | Misreads attention, expresses gratitude, shares technique, seeks advice and accepts privacy boundary. | `006–013,025`; closeness not recognition/cure. |
| `MT-R-119` Rudy → Zanoba | Resumes teaching, persists after failure, accepts production reframing, retaliates for figure. | `007,013,018–022`; pedagogy and violence are separate choices. |
| `MT-R-120` Zanoba → Rudy | Reverence/fear inhibit disclosure, shared revenge delights, later meal disagreement voiced. | `013,018,022,030`; deference conditional rather than absolute. |
| `MT-R-121` Fitts / buyers → Juli | Attend distress, purchase, treat, name and plan instruction. | `014–016`; collective care with collective participation in ownership. |
| `MT-R-122` Rudy → Juli | Blocks blow, projects despair, offers death, teaches, rejects branding, initially misunderstands fear. | `015–016,028–030`; better lesson does not release ownership. |
| `MT-R-123` Zanoba → Juli | Brother-linked naming, pupil recognition, growing care and defense against meal demands. | `016,028,030`; complete psychological cause inferred by Rudy, not confirmed. |
| `MT-R-124` Juli → buyers/teachers | Says she does not want to die, learns, fears displeasure, acts after a promise of no anger and smiles after effort. | `015–016,028,030`; no inward monologue or unrestricted agreement. |
| `MT-R-125` Linia/Pursena → Zanoba | Rank contest includes defeated disciple and destroyed figure. | `017–018`; property harm real, later violence not authorized. |
| `MT-R-126` Rudy → Linia/Pursena | Defeat, capture, assault/deprivation, threats and imposed superior status. | `019–025`; non-graphic agency record, later friendliness not retrospective permission. |
| `MT-R-127` Fitts / Zanoba → captives | Fitts urges release and provides practical help, yet also marks the captives; Zanoba proposes extreme punishments that Rudy rejects. | `022–024`; distinguish proposed/rejected injuries from executed acts. |
| `MT-R-128` Captives → Rudy/public | Submit to end danger, deny harm under fear; later social contact confers anti-bullying advantage. | `023–025,028`; no free-allegiance assumption. |
| `MT-R-129` Sylphiette → Rudy | Memories, affection, imagined exclusivity, withheld name and desire for equality. | `010–011,026–027`; only explicitly attributable self-account, no resolved Fitts substitution. |
| `MT-R-130` Ariel / attendants → Sylphiette | Care, encouragement and time offered within service and recruitment aims. | `010,026–027`; political utility does not prove false affection. |
| `MT-R-131` Sylphiette → Ariel/attendants | Loyal service, friendship, awareness of use, actual refusal and concern about instrumental approach. | `010,026–027`; not legal slavery or complete passivity. |
| `MT-R-132` Luke / Ariel → Rudy | Initially blame under assumed disclosed identity; premise corrected through Sylphiette's admission. | `007,026`; correction known to readers/attendants not full shared clarification. |
| `MT-R-133` Zanoba / Fitts → teacher and pupil | Challenge overloaded meal demands and supply a different view of the demands on her. | `030`; collaborative improvement remains within existing authority. |

Fitts is retained as a source-attributed role/name, not newly asserted as a separate biological person or silently merged with Sylphiette. The identity arrangement remains a specific open question. C015 asks whether subsequent contact permits meaningful refusal and repair rather than merely continued interaction.


## V09 updates — 2026-09-26 UTC

Prior V01–V08 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V09; immutable input final audited V08 `210894fd2b5894b7e499bab80251e8f5ea761138`. Observation suffixes resolve in [V09](../02%20Sequential%20Readings/MT_V09_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V09-`. The [disclosure and recovery checkpoint](../05%20Checkpoint%20Syntheses/MT_V09_DISCLOSURE_AND_RECOVERY_CHECKPOINT.md) owns targeted cross-domain review. Newly disclosed past states are not newly occurring changes. Acceptance, publication/audit and main integration remain separate.

| Event / direction | Initiation, refusal, information and costs | Observation / open limit |
| --- | --- | --- |
| `MT-R-134` Rudy → Cliff |Rescues before recognizing, accepts thanks, mediates then leaves pair to talk.|003–005; later liking not precondition of rescue. |
| `MT-R-135` Cliff → Elinalise |Defends with poorly calibrated fight, proposes cure/marriage, accepts constraint and works.|003–005/018; promise not achieved cure or authority over her choices. |
| `MT-R-136` Elinalise → Cliff/Rudy |States refusal/reason, requests privacy, later chooses relationship and manages conversation.|004–005/018; independent motive, future unknown. |
| `MT-R-137` Fitts/Sylphiette → Rudy |Advises mediation, helps survival/research, desires recognition, reserves duty resources.|004/008/014–016; scene attribution confirmed where explicit, not every Fitts use. |
| `MT-R-138` Rudy → Fitts/Sylphiette |Values presence beyond productivity, protects secret, offers privacy, recognizes/confesses/discloses.|016/019/024–026; gratitude-conditioned choice, imagined coercion not carried out. |
| `MT-R-139` Sylphiette → Rudy |Stages encounter, explicitly requests help, names self, accepts disclosed difficulty and seeks aid.|023–028; concealment, royal pressure and initiative coexist. |
| `MT-R-140` Rudy ↔ Sylphiette, distinct mornings |His relief and harm acknowledgment; her pain, happiness and helpfulness goal with uncertain equality.|029/032; no undifferentiated mutual-consent/recovery score. |
| `MT-R-141` Ariel → Sylphiette |Releases stated debt, supports personal departure, also exerts guilt/royal threat.|021–023/027/030; earlier disclosure permission, no newly invented prohibition. |
| `MT-R-142` Sylphiette → Ariel/Rudy |Wants friend and beloved without betraying either; later asks Rudy's help with explicit opt-out.|021/026; own goals stated, political future unestablished. |
| `MT-R-143` Luke → Rudy/Sylphiette |Empathetic defense despite dislike, then wrong body explanation and drug advice.|027; generosity/understanding differ from reliable information. |
| `MT-R-144` Nanahoshi → Rudy |Names origin, offers bargain, uses mana, limits answers and asks room for her own goal.|011–012/016/020; return not achieved; withheld methods constrain exchange. |
| `MT-R-145` Rudy → Nanahoshi |Withholds accident detail, rejects shared return goal, cooperates and questions risk.|011–013/016/020; dislike need not prevent work, no safety validation. |
| `MT-R-146` Sylphiette ↔ Nanahoshi |Missing context/grief cause attack; explanation and apologies de-escalate; jealousy persists.|013–014; no established romantic rivalry or resolved catastrophe. |
| `MT-R-147` Rudy/Zanoba → Juli |Task expectations adjusted, manageable craft roles and seating provided, commands and ownership persist.|002/015/017; fear and learning both visible, no inner consent access. |
| `MT-R-148` Rudy → school others |Opposes bullying, benefits from feared reputation, intrudes on Linia and pressures teacher.|009/017/019; uneven power accountability, fear not acceptance. |
| `MT-R-149` Rudy ↔ Soldat |Chooses ordinary visit/stories, retains prior commitments and declines later outing.|018; independent friendship, not solely therapeutic instrument. |
| `MT-R-150` Eris → absent Rudy / training peers |Affection and perceived insufficiency motivate training; Nina's rivalry not initially reciprocated.|033–034; no knowledge of his rejection account, no repaired communication. |
| `MT-R-151` Nina → Eris/Rudy |Jealousy and imagined capture motivate trip; defeat/misinterpretation alter practice and hostility.|034–035; capture contemplated not executed, later full rivalry only narrated future. |

Directions remain separate even where a pair is named. Service, employment, affection and legal ownership are not interchangeable. No third party can provide another person's bodily permission; later gratitude cannot retroactively fill a missing choice.


## V10 updates — 2026-09-26 UTC

Prior V01–V09 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V10; immutable input audited V09 `40018b5caedfba456da199ed2fea613ec991015a`. Observation suffixes resolve in [V10](../02%20Sequential%20Readings/MT_V10_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V10-`. The [V01–V10 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md) owns cumulative review. Revealed earlier events, present changes and explicit prolepsis retain different times. Draft acceptance, publication/audit and main integration remain separate.

| Directed event | Initiative, purpose, information and changed options | Observation / reciprocity and limit |
| --- | --- | --- |
| `MT-R-152` Rudy → Sylphie | Proposes marriage, provides a house, voices abandonment fear and promises shared work; consultation is selective, former-world information concealed, a known public boundary later repeated. |002–003/007–011/015/018/025. Love, care, local restraint and entitlement coexist; no total contract of access. |
| `MT-R-153` Sylphie → Rudy | Accepts marriage, keeps service, contributes savings, advises guests/clothing, states public and disappearance boundaries, agrees to household care and requests postponed intimacy. |002/007–010/015/018/020/025. Independent wishes matter; concern about pleasing him and fertility anxiety qualify equal-security claims. |
| `MT-R-154` Sylphie → Ariel | Insists on continuing a valued role rather than being released simply because of marriage. |002/008. Prior friendship and political work retain purposes beyond the couple; no universal uncoerced-service finding. |
| `MT-R-155` Ariel → Sylphie/Rudy | Demands clarity, accepts marriage and offers reciprocal patronage; later protective concern shapes the duel's concealed purpose. |002/011/013. Friendship, calculation and influence remain distinct; Rudy does not become a readily controlled subordinate. |
| `MT-R-156` Luke → Rudy/Sylphie | Participates in reception and duel, tests the prospective protector under an undisclosed arrangement. |011/013. His protective loyalty is represented; complete shared understanding of the encounter is absent. |
| `MT-R-157` Rudy → Zanoba | Requests help, accepts a research proposal, acknowledges craft limits and considers safety; remains master within an unequal arrangement. |004–006/020–021. Honest appraisal can enable another's work without dissolving devotion or dependence. |
| `MT-R-158` Zanoba → Rudy | Protects him, contests immediate orders to preserve the automaton, asks for his own task, cares during the crisis, and admits emotional incomprehension. |004–006/011/020–021. Help is not limited to craft utility; candor matters, while hierarchy and harmful force remain. |
| `MT-R-159` Zanoba → Cliff / Cliff → group | Zanoba strikes Cliff over the diversion; Cliff later proposes useful investigation and contributes to redesign despite initial dismissal. |005/021. Technical cooperation follows injury without an established complete repair; each actor's choice remains distinct. |
| `MT-R-160` Rudy/Zanoba → Juli | Protect, include and teach her while organizing her labor and retaining ownership. |005–006/011/015/020. Care changes conditions, not legal freedom. |
| `MT-R-161` Juli → adults | Startles at touch, participates in learning/social life and notices Rudy's condition during the crisis. |001/011/015/020. Useful perception is her contribution; no interior or unrestricted consent account is invented. |
| `MT-R-162` Elinalise → Rudy/group | Supplies housing contacts, helps convivial inclusion and manages practical social relations beyond romance. |007/011–012. Independent work and boundaries warrant a bounded model; aid does not entail unlimited availability. |
| `MT-R-163` Elinalise → Sylphie | Requests private speech, discloses kinship and reported separation/stigma history, responds emotionally to recognition. |012. The conversation's full contents are unavailable; not every historical consequence is independently verified. |
| `MT-R-164` Sylphie → Elinalise | Recognizes her grandmother and accepts the new familial relation. |012. Particular recognition is meaningful without retroactively erasing concealment, distance or social harm. |
| `MT-R-165` Cliff → Elinalise | Hears the history, continues commitment and pursues curse research. |014. Acceptance and effort are actual; cure and complete technical understanding are not. |
| `MT-R-166` Elinalise → Cliff | Shares consequential history and receives continued commitment within the chosen relationship. |012/014. Her disclosure is a choice, not a debt owed to everyone or proof all vulnerability has ended. |
| `MT-R-167` Nanahoshi → Rudy/collaborators | Accepts some sociability, suffers after failure, identifies the design gap, implements shared redesign, apologizes and offers thanks while keeping her return aim. |011/019–022. Broader connection does not make her choose Rudy's ultimate purpose; her interrupted complaint remains unresolved. |
| `MT-R-168` Rudy → Nanahoshi | Participates in research, responds to perceived crisis, seeks others' help and proposes a useful architectural arrangement. |019–022. His risk and care theories remain fallible; assistance neither certifies safety nor entitles him to suppress her grievance. |
| `MT-R-169` Sylphie/Zanoba/Cliff/Juli → research and care group | Supply household labor, transport, technical insight, changed judgments or attention; Cliff distinguishes gratitude from future collaborative obligation. |020–022. Different contributions and consent to continued work remain visible; no one rescuer owns the outcome. |
| `MT-R-170` Ruijerd → Rudy / Rudy → Ruijerd | Offers a cautious alternative account of Eris, delivers sisters and entrusts them to the couple; Rudy welcomes him and can consider the account while retaining hurt and speculative suspicions. |023–026. Neither verifies Eris's intent through fresh contact; Badigadi's cryptic encounter does not supply a shared history. |
| `MT-R-171` Paul → Rudy/sisters | Letter distinguishes the girls' needs and seeks care; the extra shows risk appraisal, uncertainty about an old acquaintance and eventual delegation. |017/030/034. Confidence in a gifted son coexists with explicit caution; rescue of Zenith remains unverified. |
| `MT-R-172` Aisha → party/Rudy/Norn | Plans caravan travel, welcomes her brother and contributes materially; earlier persuasion of Norn includes contempt. |024/030. Ability and affection do not remove fatigue or excuse humiliating the less gifted sister. |
| `MT-R-173` Norn → Paul/Ruijerd/Rudy | Prefers her father, seeks and responds to Ruijerd's protection, requests continued comfort and later refuses confidence in Rudy despite contextual understanding. |026/030–032/034. Attachment and distrust have represented reasons; no automatic transfer of trust between protectors. |
| `MT-R-174` Ruijerd → Norn/sisters | Stops an aggressor, listens to refusal, considers unsafe-home possibility, acknowledges limits, adjusts reassurance and fulfills escort. |024/026/031–032/034. He still urges acceptance of separation; responsive care is not realization of every first preference. |
| `MT-R-175` Lilia → daughters / Roxy → Norn/Ruijerd | Lilia restrains contempt while preserving rank distinction; Roxy acts as guard despite fear, then corrects the mistaken appraisal while fear persists. |030/033. Distinct actors and constraints: hierarchy enforcement, duty and belief correction cannot be merged into one family attitude. |
| `MT-R-176` Eris → absent Rudy/dojo / Ghislaine → Eris/Gal | Eris sustains training through admiration and avoided longing while relying on dojo resources; Ghislaine challenges apparent neglect and defends knowledge as a worthwhile gain. |027–029. No new communication with Rudy or restored mutual understanding; Gal's instruction and explicit future certification differ from current achievement. |

Current household belonging does not settle every directional relationship. The newcomer who trusts Ruijerd can distrust Rudy; a wife can welcome a gift yet retain a public boundary; a collaborator can value help and still have an unheard grievance. The [V01–V10 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md) integrates these differences without converting gratitude, affection, work, service and ownership into equivalent ties.
