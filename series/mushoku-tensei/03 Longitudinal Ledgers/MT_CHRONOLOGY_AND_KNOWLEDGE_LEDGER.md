---
title: "Mushoku Tensei - Chronology and knowledge ledger"
artifact_id: MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER
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

# Chronology and knowledge ledger

## Responsibility

Owns story-event ordering and who knows, believes, suspects or misbelieves a proposition at a particular point. It preserves uncertain age and interval claims by witness/continuity.

## Record format

`chronology ID | event/observation | witness | anchor | inferred interval | age claims | certainty/conflicts; knowledge ID | proposition | holder | epistemic state | disclosure/concealment | story state | reader access | source basis | uncertainty`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append anchored events and proposition changes; reconcile conflicts visibly. Never backfill a character’s earlier knowledge from a later disclosure or force an unsupported exact calendar. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

Witness `MT-LNJP-V01`; observation IDs resolve in the [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). Ages are reported anchors in this volume, not a formula for subjective or moral age. Exact elapsed months and calendar dates are not inferred beyond the text.

| Chronology ID | Story order and age/interval anchor | Evidence and certainty |
| --- | --- | --- |
| `MT-T-001` | First-life narrator reports age 34, years of isolation, an eviction after the parents' funeral, then the rescue attempt/death. | `001–002`, **character report** for biography and motive; accident as represented event. Other students' ultimate fate is not certified. |
| `MT-T-002` | Reborn infant discovers language and household over months; healing is observed before the vow to live seriously. | `003`, order explicit; the reincarnation mechanism and prior subjective continuity are unresolved. |
| `MT-T-003` | Roughly two years after rebirth he reads and practices; at age three the damaging indoor magic attempt triggers the hiring of Roxy. | `005–006`, explicit rounded anchor. Capacity increases over practice days, but the exact growth law is unknown. |
| `MT-T-004` | At age five he receives gifts, graduates after a roughly two-year teaching period, first crosses the village boundary and then becomes Sylphie's friend. | `007–010`, age and general order explicit; the exact birthdays of the other children are not given here. |
| `MT-T-005` | At age six he has taught Sylphie for about a year; the bathroom violation, apology, wary friendship, Zenith and Lilia pregnancies and births follow. | `011–014`; pregnancy/birth interval is narrated in compressed months, not converted into a date. |
| `MT-T-006` | At age seven he confronts a training plateau and asks about university; one month after a request for work, Paul sends him to Roa. | `015–016`; Paul's letter specifies five years apart, which is a planned interval, **not** a completed interval at V01 exit. |
| `MT-T-007` | The Zenith extra appears after the separation ending but recounts her youth, past marriage and domestic period before the departure. | `014`, publication/spine order differs from story time; do not read it as a later event after departure. |

| Knowledge ID / proposition | Holder and epistemic state at the V01 boundary | Basis / limit |
| --- | --- | --- |
| `MT-K-001` Prior-life memory and reincarnation | Rudeus has represented memories and infers rebirth; family, Roxy and Sylphie are not shown knowing their content. Reader has first-person access. | `001–003`; no omniscient mechanism or universal subjective-age rule. |
| `MT-K-002` Magic/manual capacity | The textbook asserts near-fixed initial mana; Rudeus observes his own changing endurance, offers multiple hypotheses; Sylphie later also improves. | `005,011`; observation narrows the manual's simple rule, not proof of unbounded capacities for all. |
| `MT-K-003` Rudeus's fear of crossing gate | Rudeus reports fear linked to past injury. Roxy believes he fears a horse; his parents do not receive a full explanation in V01. | `008`; his later gate test establishes local change only. |
| `MT-K-004` Sylphie's identity and wishes | Rudeus misclassifies Sylphie's sex until the boundary violation; she had communicated refusal. Later she asks for ordinary treatment and opposes his leaving. | `009,011–012,016`; his error about sex does not cancel her known refusal. Romance is his inference, not her declared future agreement. |
| `MT-K-005` Pregnancy and allegation | Paul admits likely paternity; Rudeus knowingly invents the coercion allegation; Zenith hears it, then Rudeus privately tells her it was a lie. Lilia's later focalized account attributes initiation of the recent encounter to herself while recalling earlier force. | `013–014`; participant reports are distinguished; the precise earlier conduct is not excused by later feelings. |
| `MT-K-006` Separation plan | Paul and Rolls discuss Sylphie's dependency; Rudeus learns the five-year terms only after waking in the carriage. Sylphie sees the removal and protests; her father's precise explanation is withheld. | `016`; adult prediction and future effect remain unverified. |
| `MT-K-007` Roxy's later progress | Rudeus and reader learn from her letter that she reports Shiron court work and water-king level after leaving. | `015`; no direct inspection of her offstage life or later LN. |

The age claims “34” and later self-characterization as mentally over 40 belong to Rudeus's own arithmetic and rhetoric (`001,006,013`); age at this volume's close is seven in his new life (`MT-T-006`). Physical development, remembered experience, social treatment and demonstrated judgment remain separate variables. Do not enter a sum as a world fact.

## V02 chronology and knowledge changes — 2026-09-26 UTC

Input audited V01 commit `eaf159559c6fc76ddd820178d7588545f08c351d`. Numbers below refer to [V02 observations](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V02-`. The V01 rows remain fixed historical states.

| Chronology ID | Anchor/order through V02 | Evidence / uncertainty |
| --- | --- | --- |
| `MT-T-008` | Arrival: Rudeus seven, Eris nine; pursuit prologue precedes explanatory reset to arrival. | `001–004`; age explicit, opening narrative order differs from event order. |
| `MT-T-009` | Abduction/employment → about a month of instruction → roughly another half year → rest-day system; first outing/history account names K414. | `003–007,010`; rounded summaries not forced to exact dates. |
| `MT-T-010` | Roughly one year since arrival: Eris ten; dance, gifts, sphere observation. Later Rudy nine/two years since arrival, language study and letter. | `008–011`; Ghislaine's half-year conversational acquisition can fall within his year of study. |
| `MT-T-011` | Rudeus ten/Eris twelve: birthday and boundary episode, then staff demonstration and catastrophe. | `012–017`; planned holy spell interrupted. Extra explicitly dates displacement year K417 (`part0027` p54–55). |
| `MT-T-012` | Epilogue: Roxy arrives six months after regional disappearance. | `018`; travel chronology explicit; no exact arrival date invented. |
| `MT-T-013` | Extra: a century-later cult frame returns to K417 for Vigo/Ghislaine battle, then traces cult formation. | `019`; V02 itself contains this future reach. Main cast does not gain that later knowledge. |

| Knowledge ID / proposition | Holder, update and reader access | Evidence / boundary |
| --- | --- | --- |
| `MT-K-008` Abduction plan vs reality | Rudy/Philip know staged design; Eris does not. Rudy discovers real danger. Philip later reports Thomas's betrayal and managed official attribution. | `001–004`; investigation not directly witnessed; reader must not infer Eris learns every backstage fact. |
| `MT-K-009` Eris's reasons and limits | Rudy guesses repeatedly; her return to dance practice, gift initiative and direct refusal provide action/speech. Ghislaine's romantic interpretations are conjectural. | `008,011–014`; no blanket mind-reading. |
| `MT-K-010` Language and history | Rudy learns through books, Ghislaine and Roxy; embedded cosmology/history remain attributed. Roxy letter confirms effort and reports likeness distress. | `010–011`; no external historical verification. |
| `MT-K-011` Household lineage and sons | Political secrecy and succession customs become available to Rudy by gradual report, culminating in Philip's explanation. | `012–013`; Hilda's interior motives not independently narrated. |
| `MT-K-012` Disaster cause | Roxy/Perugius compare light to summoning; others suspect, speculate or identify an unexplained deviation. Rudy has not caused the represented anomaly by completing his planned spell. | `015–017`; no culprit/mechanism established; no later-franchise explanation permitted. |
| `MT-K-013` Missing versus dead | Roxy sees separate boards and Paul's message; reader learns Norn with Paul as his report, wives/Aisha missing. | `018`; Rudy's reception of message unshown; absence from death list is not proof of safety. |
| `MT-K-014` Ghislaine's survival and purpose | Reader/Vigo encounter her after displacement; she asks after children and receives geographic information. | `019`; no demonstrated reunion or confirmed route success. Vigo never learns eventual fate in this extra. |
| `MT-K-015` Legend versus experience | Vigo's memorial and later collective cult recast Ghislaine's intervention; reader has causal account unavailable to later worshippers. | `019`; no claim that Ghislaine knows or authorizes cult. |

**Unresolved witness details:** anomaly direction differs within Roxy scene (`part0020` p379 east / p476 west). Extra commander spelling varies (`part0027` p172/214 クライン, p207 クラウン), with loose troop recounting around p136/145–146. Preserve these as source irregularities; neither silently normalize nor construct additional characters/events. These details do not block the recovered event order. Physical ages, remembered past and self-attributed total age remain distinct.


## V03 updates — 2026-09-26 UTC

Prior V01/V02 bodies remain historical and unchanged. Current scope is Japanese LN V01–V03; input is audited V02 head `687a13ac1a661270ab566c9e1a6028acd607d846`. Observation suffixes below resolve in [V03's diagnostic readings](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V03-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Chronology ID | Story-time anchor / order | Observation / uncertainty |
| --- | --- | --- |
| `MT-T-014` | V03 begins immediately after displacement, before V02's six-month Roxy epilogue; Ruijerd rescues children in northeastern Demon Continent. | `001–004`; no precise intervening day count beyond narrated travel. |
| `MT-T-015` | At guild registration Rudeus is 10, Eris 12 and Ruijerd 566; Rowin reports Roxy as 44. | `003,007`; private summed remembered age is not current bodily age. |
| `MT-T-016` | First town: initial jobs, three days to E rank, later three-week summary to D rank, forest/exposure and departure; Rudy says nearly two months there. | `010–017`; preserve rounded spans without forcing exact consistency or hidden days. |
| `MT-T-017` | Post-reunion travel progresses through month summaries to approximately one year; A-rank Dead End reaches Wenport. | `019–020`; no exact new birthday/date or completed sea crossing. |
| `MT-T-018` | Extra returns to the initial Fittoa event: monster arrives at palace, Derrick dies and unnamed girl arrives. | `022`; publication order differs from story time; narrator directly dates simultaneity. |

| Knowledge ID / proposition | Holder and update | Evidence / boundary |
| --- | --- | --- |
| `MT-K-016` Hitogami | Rudy experiences two dreams and receives useful route/job advice; divine identity, motives, limits and culprit claims unverified. | `001,009`; no blanket cosmology admission. |
| `MT-K-017` Roxy / family | Parents learn earlier pupil news; Rudy learns family/telepathy history and promises contact. | `003`; no completed later communication established. Paul's message still not shown received by Rudy. |
| `MT-K-018` Ruijerd history / code | Ruijerd reports spears/son/persecution; Rudy reconstructs child/warrior norms from speech and behavior. | `004,011,014–015`; report and interpretation distinct; other Superd absence not extinction. |
| `MT-K-019` Guild scheme | Rudy knows rules but disputes classification; Nokopara exposes job swapping and its institutional effect; party change does not erase prior acts. | `007,012,016`; actual rule vs actor's self-exemption. |
| `MT-K-020` Rescue motive | Rudy/reader know deliberate gratitude-maximizing delay; Kurt supplies an independent self-responsibility account; Ruijerd credits respect for warrior pride. | `014`; no full confession represented, favorable interpretation mistaken. |
| `MT-K-021` Flood preparation | Rudy/reader know contemplated town devastation; Ruijerd later speaks of readiness to kill the extortionist. | `016,018`; scope of shared knowledge limited, no flood executed. |
| `MT-K-022` Identity/public blame | Disguise supports acceptance; reveal with threat causes panic; guards assign agency to Ruijerd and innocence to children despite Rudy's protest. | `006,017`; not independent factfinding or a pure hair-only test. |
| `MT-K-023` Consultation | Party adopts reporting/advice; Eris supplies overlooked market practice; Rudy withholds reputation allocation. | `019–020`; more communication not complete transparency. |
| `MT-K-024` Palace cause/newcomer | Narrator says monster teleported; Derrick considers conspiracy then receives rescue as answered prayer. Girl is unnamed and white-haired. | `021–022`; no proved divine mechanism, later identity or Rudy knowledge. |

Source-appraisal variation: Rudy first attributes an attack's partial hit to his aim, later considers evasion (`014–015`); retain changed explanation. Ruijerd initially senses fighting, then the party finds six dead veterans; precise opportunity for earlier intervention is not supplied (`015`). Neither licenses an invented rescue choice. V02 source irregularities remain as recorded, not silently repaired.


## V04 updates — 2026-09-26 UTC

Prior V01–V03 bodies remain historical and unchanged. Current scope is Japanese LN V01–V04; input is audited V03 head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Observation suffixes below resolve in [V04's diagnostic readings](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V04-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Chronology | Anchor / order | Evidence / uncertainty |
| --- | --- | --- |
| `MT-T-019` | Wenport: Rudeus11 after recent birthday, Eris13; about one year since displacement. | `001`; resolves age at new admission, does not rewrite V03 freeze. |
| `MT-T-020` | Eye gift → roughly one week calibration → staff-sale encounter; fifteen-day wait before arranged crossing. | `002–005,008`; do not add overlapping summaries as exact calendar. |
| `MT-T-021` | Port rescue/capture → week of confinement, Geese arrives around fifth day, fire/attack ends detention. | `009–015`; Ruijerd's concurrent rescues/negotiations explain delay. |
| `MT-T-022` | Three-month rainy-season residence, week/month markers; Eris soon14 at departure. | `016–021`; no subsequent birthday narrated. |
| `MT-T-023` | Forest road approximately one month, mountain passage three days, then Millis border. | `022`; capital/home not yet reached. |
| `MT-T-024` | Roxy interlude overlaps port training, leaves after three days; narrator offers longer-stay counterfactual. | `006–007`; narrative order differs from event overlap, not a completed meeting. |
| `MT-T-025` | Fitts extra returns to catastrophe and approximately the following year; later escape announced. | `023–026`; not simply events after main ending, no completed foreign journey. |

| Knowledge / proposition | Holder / update | Evidence and limit |
| --- | --- | --- |
| `MT-K-025` Fare/alternatives | Party learns institutional price; Rudy conceals staff sale, Ruijerd later challenges and changes decision. | `001,005`; anti-terror explanation guessed, no all-party informed consensus. |
| `MT-K-026` Hitogami/Kishirika | Rudy gets advice, claimed counterfactual and observed eye gift; distrust persists. | `002–003`; useful outcome not proof of benevolent providence or all historical claims. |
| `MT-K-027` Eye/ability | Practice reveals branching/timing limits; battle reveals interpretation/physical gaps. | `003–004,014`; future sight not omniscience or guaranteed victory. |
| `MT-K-028` Missed meeting | Roxy holds distorted rumor and fear; reader sees Ruijerd's actual curiosity and overlapping training. | `006–007`; neither knows full near encounter, no message reception by Rudy. |
| `MT-K-029` Gallus plan | Initial rescue/gratitude story → hostage disclosure and later reconstruction reveal faction sabotage/abduction. | `005,009–015`; initial trust not retroactively informed, alleged buyer identities remain partial. |
| `MT-K-030` Killing self-account | Rudy claims no previous murderous intent while authorizing killings; reader retains V03 flood preparation. | `009`; personal animus/direct killing distinctions possible but not explicit reconciliation. |
| `MT-K-031` Arrest/care need | Gyes misreads scene, Gustav doubts and orders no harm, Ruijerd assumes warrior self-sufficiency. | `011–012,019`; reader has disparate access, no blanket innocent-history claim. |
| `MT-K-032` Boreas labor | Rudy suspects connection between noble demand and household servants but explicitly lacks origins, tells Eris nothing. | `015`; source-grounded suspicion, not established household acquisition history. |
| `MT-K-033` Ghislaine/family letters | Gyes's childhood account challenged by pupils; Rudy remembers forgotten search/letter plans. | `016,018`; no current Ghislaine encounter or completed family communication. |
| `MT-K-034` Sacred beast/history | Lakrana translates gratitude and denial of Rudy-as-hero, reports long maturation/world-saving tradition. | `020`; translation/tradition not independently proved prophecy or chronology. |
| `MT-K-035` Geese/Great Powers | Geese reports party breakup and old Ruijerd rescue; ranking/history supplied by companions. | `022`; unnamed couple remains unnamed; automatic updates only reported. |
| `MT-K-036` Fitts/rumor | Narrator supplies alias and displacement history; nobles misattribute Eris-tutor biography; identity phrase interrupted. | `023–025`; no explicit earlier name. Boy presentation differs from V03 girl description; do not repair using foreknowledge. |
| `MT-K-037` Court threat/relief | Reader sees Grabel/Darius planning, Fitts kills attacker, official inquiry fails; nightmares cease afterward. | `024–026`; Rudy knows none of this here, single cause of relief unestablished. |

Appraisal and textual details stay distinct: suspect biography is not a missing source, and roughly timed episodes need not share an exact calendar. V02 source irregularities and earlier knowledge rows remain preserved.


## V05 updates — 2026-09-26 UTC

Prior V01–V04 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V05; frozen published input is audited V04 head `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. Observation suffixes below resolve in [V05's diagnostic readings](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V05-`. The [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) owns the historical cumulative synthesis; publication/audit remain separate from this preparation snapshot.

| Chronology | Anchor / order | Observation / limit |
| --- | --- | --- |
| `MT-T-026` | Milishion arrival at Rudy's stated eleven/about 1.5 years after displacement; fight then next-day reunion, later week before departure. | `001,007–015,020`; approximate time language retained. |
| `MT-T-027` | Paul retrospective: Norn aged three at the disaster, illness stop roughly two months, search/Millis work then month of neglect before reunion. | `004–006,015`; overlapping summaries not additive exact calendar. |
| `MT-T-028` | Eris interlude returns to first reunion day; Cliff twelve between Rudy/Eris, rescue before comfort scene. | `017–019`; later source age formulation recorded beside V04 near fourteen, not silently forced into a birthday. |
| `MT-T-029` | Departure → reported two months to Westport → passage to Central Continent/Eastport extra. | `020–022,025`; rounded two-year/roughly twelve-year language not precise birth date. |
| `MT-T-030` | Roxy return around group's Millis departure, stays three days, confirms missed meeting then searches northwest. | `023–024`; no exact shared calendar inferred. |
| `MT-T-031` | Ariel leaves capital, rumors/inquiry after about one month; successive border/testimony/report/correction opportunity. | `026–028`; announced later consequence not present event. |

| Knowledge | Holder / change | Observation / limit |
| --- | --- | --- |
| `MT-K-038` Apparent abduction | Rudy believes child kidnapped; reader later knows rescue party, Paul first assumes disguised enemy. | `002–003,007`; each acts before recognition. |
| `MT-K-039` Disaster/notices | Paul assumes son informed; Rudy not; Eris saw notices and assumes he knew. Region-wide facts reach Rudy after fight. | `006–007,017`; message existence not receipt, some omissions remain real. |
| `MT-K-040` Paul history | Reader receives care/search/assault memory before son's understanding. | `004–006`; feared deaths and revenge hypothesis not established. |
| `MT-K-041` Vera/Shela | Paul/reader have abuse/protection account; Rudy still uses sexual/dislike explanations. | `010`; apology not complete new knowledge, no recovery certification. |
| `MT-K-042` Family development | Paul tells domestic negotiation, Sylphie's prior study, Philip letter; current missing fates unknown. | `012,020`; reports not direct new women's interiority; no alias resolution. |
| `MT-K-043` Geese | Jail arrangement newly reported, old-party tie disclosed, why he withheld news still evasive. | `009,020`; V04 freeze preserved. |
| `MT-K-044` Letter | Rui knows old friend as Gash; Rudy/Paul initially cannot identify; letter and Therese later establish role/handwriting. | `014–015,021–022`; first nickname guesses not all facts. |
| `MT-K-045` Acceptance | Village/knight distinguish personal gratitude from group belief; Rudy learns publicity/passage limits. | `016,021–022`; no general reform. |
| `MT-K-046` Eris adventure | Reader knows independent rescue before Rudy learns from Therese; Cliff miscredits teaching and ease of win. | `017–019,022`; inner fear/knight help qualify surface. |
| `MT-K-047` Roxy | Testimony resolves missed encounter; her effortless-pupil account remains partial; parents' care becomes perceptible. | `023–024`; no new telepathy or meeting. |
| `MT-K-048` Restaurant | Rudy guesses failing shop/thug; owner viewpoint reveals general/recruitment/martial identity and closure. | `025`; downstream facts not automatically Rudy knowledge. |
| `MT-K-049` Ariel inquiry | Bruno observes killing but infers identity; Gustav asserts death, lookout contradicts, Gustav knowingly leaves report. | `026–028`; final framing confirms falsehood, disguise mechanism inferred, later politics not narrated. |

Source interpretation distinguishes event, report, prediction and chosen ignorance. The continuing absence of confirmed family locations or Fitts's earlier name is not a missing extraction route.


## V06 updates — 2026-09-26 UTC

Prior V01–V05 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V06; frozen input is final audited V05 head `3dc6b173b044abdafc013dc989bd96914620d13d`. Observation suffixes below resolve in [V06's diagnostic readings](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V06-`. The [V06 disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews altered premises; the V01–V05 cumulative checkpoint remains historical. Publication/audit remain separate from this preparation snapshot.

| Chronology | Anchor / order | Observation / limit |
| --- | --- | --- |
| `MT-T-032` | Opening guild card says twelve; route/search summaries give roughly two years after displacement and months of travel. | `001–004`; not a verified exact birthday/calendar. |
| `MT-T-033` | Shirone letter precedes Aisha rescue, false invitation, prison day and overlapping liberations; escorted family then separates. | `004–013`; retrospective explanation supplies earlier concurrent actions, not a second rescue. |
| `MT-T-034` | Road training/recognition precede mountain attack; later Eris identifies recognition as fifteenth birthday. | `014–018,023`; travel-month and age approximations retained without forced reconciliation. |
| `MT-T-035` | Recovery → three-day aftermath/Asura entry → about a month north → camp, intimacy/departure, week of distress and northbound search. | `018–026`; source order and reported intervals, no invented exact date. |
| `MT-T-036` | Eris's retrospective section revisits V02–V06; Zanoba and Lilia histories precede present action. | `010,024,030–031`; REVEALED_NOT_NEW, not current change in childhood. |
| `MT-T-037` | Roxy interlude reports Lilia/Aisha already with Paul; final extra returns to their earlier escorted journey. | `027–031`; book order is not a universal time sequence; estimated delivery time not completed delivery. |

| Knowledge | Holder / change | Observation / limit |
| --- | --- | --- |
| `MT-K-050` Advice / Roxy | Hitogami supplies ordered instruction; Rudy assumes court employment, writes early and partially briefs companions. | `002,004,007`; instruction, interpretation and actual outcome distinct. |
| `MT-K-051` Aisha identity | Rudy thinks alias effective; Aisha recognizes him; extra confirms knowledge while Lilia misreads it. | `006,013,029`; exact proposed test partly Rudy inference; every private thought not shared. |
| `MT-K-052` Court plans | Ginger, soldiers, Zanoba and Ruijerd act with unequal information; Rudy learns motives/history later. | `007–011`; no earlier omniscient strategy, no guaranteed alternative history. |
| `MT-K-053` Orsted | Recognizes companions, denies Paul-son expectation, detects absence of aversion, attacks at Hitogami name. | `015–016`; anomaly observed, causal world explanation unknown. |
| `MT-K-054` Curse claims | Hitogami claims aversion, visibility limits, transfer/attenuation; Rudy notices inconsistency and later tells Rui with caution. | `017,019`; attributed useful account, not independently settled law; social prejudice remains. |
| `MT-K-055` Healing / strength | Eris reports Nanahoshi's intervention and Orsted's healing; Rudy recovers, feels dreamlike; Eris reads resolve where he intends escape. | `016,018,024`; intervention motive and psychological cause unresolved. |
| `MT-K-056` Training account | Eris reports one hit on distracted Rui; Rudy earlier claimed none. | `014,016,024`; retain differing knowledge/scope, not silently harmonized statistic. |
| `MT-K-057` Home deaths / Darius | Staff report family deaths; Ghislaine verifies parents, Alphonse names kidnap patron and prospective transfer risk. | `021–022`; exact death circumstances and political causation partly withheld/inferred. |
| `MT-K-058` Records | Rudy misreads crossing-out, asks clerk, learns Sylphie reported alive without contact address; updates Lilia/Aisha. | `021`; record presence not complete biography, high confidence survival report not observed encounter. |
| `MT-K-059` Eris departure | Eris intends training/future partnership, withholds destination; Rudy reads note as rejection; Alphonse obeys nondisclosure. | `023–026`; reader knows more, Eris not shown knowing his resulting interpretation. |
| `MT-K-060` Reconstruction | Rudy first sees desolation, later builds defenses and observes recovering settlements. | `021,026`; no-rebuilding first impression revised; Eris death is planned cover. |
| `MT-K-061` Search lead | Kishirika reports Zenith alive near Rapan with unclear circumstances; Roxy probes, chooses to trust and plans delivery. | `027–028`; Rudy has not received it, dungeon explanation conjectural, rescue unobserved. |
| `MT-K-062` Departure party | Roxy assumes Kishirika sails; narrator/Elinalise learn she stays due restriction. | `028`; particular misinformation, not total incompetence. |
| `MT-K-063` Lilia history | Reader gains resistance, aftermath, paternal alternative and maternal self-questioning; present family does not receive this full narration. | `030–031`; affection and confidence in plan are different propositions. |

Neither the source's ending order nor reader access transfers knowledge to a character. New testimony revises current interpretation without altering the V01–V05 freezes.


## V07 updates — 2026-09-26 UTC

Prior V01–V06 bodies remain historical and unchanged. The current source boundary is Japanese LN V01–V07. The entering freeze used audited V06 head `0e72e531278055c0dbb7a6054285337a1cc37a93`; later repository reconciliation does not change that analytical input. Observation suffixes resolve in [V07](../02%20Sequential%20Readings/MT_V07_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V07-`. The [recognition checkpoint](../05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md) owns the focused comparison. Publication and exact-head audit are separate from content acceptance.

| Chronology | Anchored sequence | Observation / limit |
| --- | --- | --- |
| `MT-T-038` | Caravan arrival and initial work → grizzly crisis → routines summarized over about three months. | `001–007`; source intervals, no forced absolute calendar. |
| `MT-T-039` | Ruins job/misunderstanding → winter around six months in town → failed expedition, Mimir death and overnight Sara rescue. | `008–017`; simultaneous party preparations disclosed after Rudy returns. |
| `MT-T-040` | Around a year in Rosenburg, shopping and failed intimacy → nighttime drinking/professional help, next morning's missed job, dawn collision and departure. | `018–025`; late Sara section revisits this same sequence. |
| `MT-T-041` | Epilogue compresses more than a year of changing towns at two-to-three-month intervals; Elinalise hears of his reported location. | `026–027`; Rudy sheet labels fifteen, Sara's late account sixteen; do not backdate sheet ages to every earlier scene. |
| `MT-T-042` | Extra begins with third-year Ariel, revisits flight and second-year election strategy, then returns to present recruitment plans. | `028–030`; next-year first dispatch proposed, not accomplished; no exact synchronization with every main-story scene. |

| Knowledge | Holder / proposition change | Observation / limit |
| --- | --- | --- |
| `MT-K-064` Dead End / purpose | Rudy does not correct the assumption that his party was annihilated; tells a substantially real mother-search purpose. | `001–002`; partial truth and withheld relational history coexist. |
| `MT-K-065` Sara category | Sara recognizes contrary evidence about Rudy yet initially refuses its implication; later compares different smiles. | `006,012`; not simply absence of information, no universal class-belief reversal. |
| `MT-K-066` Ruins | Rudy's architectural reconstruction is inference, Timothy supplies reported history, Mimir supplies unavailable exorcism expertise. | `008`; do not certify complete historical reconstruction. |
| `MT-K-067` Two entrances | Parties assume separate routes/jobs; confrontation produces corrected account of their connection. | `010`; misunderstanding resolved, unequal customary share is a separate matter. |
| `MT-K-068` Search evidence | Rudy confirms Mimir's remains; Sara earring prompts false death inference, living captive corrects it. | `014–016`; her survival labor is disclosed separately; physical evidence has differing force. |
| `MT-K-069` Family affiliation | Rudy reassures Sara that his remembered noble relatives are unconnected to her village loss, while internally considering possible Boreas involvement and his Notos family connection. | `018`; relief-giving speech contains known contrary evidence; actual political obstruction remains conjecture. |
| `MT-K-070` Bodily difficulty | Rudy newly interprets earlier signs; Sara initially lacks the relevant explanation; Elise proposes fear/trust mechanism. | `020,022,025`; observed difficulty, self-interpretation and professional opinion are different certainty levels. |
| `MT-K-071` Affection / rejection | Sara's later focalization establishes love and intended confession; Rudy believes her defensive debt-only claim and reaffirms presumed Eris rejection. | `020,025`; reader correction does not reach him. |
| `MT-K-072` Confidants | Soldat hears Rudy's account but lacks Eris's intention; Suzanne asks before involving Timothy; Elise later discloses sensitive information. | `021–025`; partial but useful advice, distinct permission and privacy structures. |
| `MT-K-073` Collision / repair | Sara hears real insult, imagines a night of shared mockery that did not occur, then learns bodily explanation too late for planned conversation. | `023–025`; factual correction does not retract actual harm or automatically produce reconciliation. |
| `MT-K-074` Search message | Elinalise hears group-dragon rumor and reported-location lead while carrying the mother's-location message. | `027`; hearsay not new witnessed combat; no receipt by Rudy, rescue or verified present condition. |
| `MT-K-075` Public school account | Ariel's insults are audible to beast girls but not human bystanders; attendants distribute a selective account of the resulting attack. | `028–029`; audience ignorance is deliberately produced; competence and reputational narrative are separate. |
| `MT-K-076` Recruitment | Third-year group discusses Zanoba, Cliff, Galfarion and Rudy; Fitts responds with conspicuous recognition. | `030`; neither identity resolution nor invitation delivery established here. |

The late source explicitly corrects some motives and leaves others attributed. Narration's future-oriented comments about lingering adventurers are bounded statements about that represented group, not a universal causal law or new current knowledge for the protagonists.


## V08 updates — 2026-09-26 UTC

Prior V01–V07 bodies remain historical and unchanged. Current source boundary: Japanese LN V01–V08. Immutable entering input was final audited V07 `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. Numeric observation suffixes resolve in [V08](../02%20Sequential%20Readings/MT_V08_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V08-`. The [consent and institutional-power checkpoint](../05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md) owns the targeted comparison. Content acceptance, publication/audit and integration to main remain separate states.

| Chronology | Anchored order | Observation and limit |
| --- | --- | --- |
| `MT-T-043` | Official opening year422/five years after displacement; northern dragon trip occupies seven days before message arrival. | `001–003`; bard framing mediates account, no literal one-day expedition. |
| `MT-T-044` | Winter delay, invitation/inquiry/refusal, dream advice and farewell → spring journey/enrollment; Rudy explicitly fifteen. | `003–007`; spring423 plausible inference, not explicit date imposed on every scene. |
| `MT-T-045` | Enrollment and library/dormitory events → school routine → failed craft teaching → market purchase. | `008–016`; interludes interrupt sequence with recollection. |
| `MT-T-046` | Juli learns for about a month; broken figure revealed → defeat, roughly day-long confinement and release → epilogue routine. | `016–028`; epilogue says three months since enrollment, earlier intervals do not cleanly sum; preserve tension. |
| `MT-T-047` | Sylphiette's second interlude revisits current school relations; meal extra returns to routine, westbound epilogue thread unresolved. | `026–030`; exact synchronization not forced, no narrated arrival. |

| Knowledge | Holder and change | Observation and limit |
| --- | --- | --- |
| `MT-K-077` Official closure | Eris reported dead and funding ended; analyst's admitted V06 evidence contradicts death. | `001`; institutional record not ontological closure. |
| `MT-K-078` Search delivery | Rudy actually receives Elinalise's Zenith-location report and her reassurance. | `002–003`; location, condition and rescue remain different claims. |
| `MT-K-079` Choice advice | Invitation explained; initial refusal changes after Hitogami promises cure route and threatens regret. | `004–005`; adviser purpose/outcome unverified. |
| `MT-K-080` Curse | Elinalise reports necessity and enjoyment; illness represented; Rudy guesses crystal mechanism. | `005`; partial bodily evidence not complete causal theory. |
| `MT-K-081` School knowledge | Rudy misreads Fitts, learns rules/status/kinship and receives books; political explanation of Zanoba partly inferred. | `006–009`; Cliff's Eris report and Silent stories remain attributed. |
| `MT-K-082` Identity roles | Sylphiette appears alongside named Fitts; hair/glasses clues and permission to use Fitts suggest role/disguise. | `010,026`; no explicit mechanism or comprehensive attribution; maintain uncertainty. |
| `MT-K-083` Sylphiette history | Own account credits multiple teachers, service relationships and reported parental deaths. | `010–011`; history/recollection not all newly occurring change. |
| `MT-K-084` Craft assumptions | Rudy learns mana/precision limits; consultation changes goal structure; Zanoba's prior idea was inhibited. | `013`; group diagnosis not proof slavery necessary. |
| `MT-K-085` Juli | Parents both sold, seller's blame unverified; child learning partly confirms possibility; greater language skill than expected. | `014–016`; no parental life/death verdict or universal age law. |
| `MT-K-086` Disciple concealment | Zanoba's viewpoint reveals fear of reporting failure and distinction from Roxy fixation. | `018`; source interior access does not supply Rudy this whole account. |
| `MT-K-087` Available objection | Elinalise challenges retaliation; Rudy later recognizes crime and imagines Ruijerd's criticism. | `019,022`; ethical reasons available without governing choice. |
| `MT-K-088` Captive information | Rudy minimizes assault in explanation; washable marks represented as permanent; frightened denial prevents complaint. | `021–025`; controllers' knowledge differs from targets/public. |
| `MT-K-089` Undisclosed name | Sylphiette has not named herself; Ariel/Luke assumed she had; jealousy is her interpretation. | `026–027`; Rudy not shown knowingly rejecting a declared identity. |
| `MT-K-090` Child fear | Rudy sees fear but initially counts only direct hitting; remembered threats/captivity supply wider context. | `028,030`; confidence/compliance remain partly inferred without Juli POV. |
| `MT-K-091` Open identities/causes | Watchers and six-armed traveler described without full named resolution; cure/displacement remain unresolved. | `029`; plausible earlier-person links are inference, no future meeting admitted. |


## V09 updates — 2026-09-26 UTC

Prior V01–V08 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V09; immutable input final audited V08 `210894fd2b5894b7e499bab80251e8f5ea761138`. Observation suffixes resolve in [V09](../02%20Sequential%20Readings/MT_V09_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V09-`. The [disclosure and recovery checkpoint](../05%20Checkpoint%20Syntheses/MT_V09_DISCLOSURE_AND_RECOVERY_CHECKPOINT.md) owns targeted cross-domain review. Newly disclosed past states are not newly occurring changes. Acceptance, publication/audit and main integration remain separate.

| Chronology | Order / anchor | Limit and observations |
| --- | --- | --- |
| `MT-T-048` | Cliff's pre-Rudy school retrospect → rescue/mediation → seasonal challengers and Badigadi duel. |001–009; opening backstory is not all newly occurring. |
| `MT-T-049` | One month after duel settlement → mask encounter/research agreement → routine nearly a year into school; Rudy explicitly16. |009–016; relative anchors do not erase V08 interval tension. |
| `MT-T-050` | Cliff reports six months' fruitless research → Soldat visit/false Fitts → partial response → plan/reunion → closing morning. |018–029; short response and later reported recovery distinct. |
| `MT-T-051` | Late Sylphiette0 returns to recruitment/entrance/library/dorm, then rejoins closing morning. |030–032; disclosure permission predates Rudy's enrollment. |
| `MT-T-052` | Extra frame Eris17/Nina18/Jino14; approximately two-year arrival flashback, then Nina's school trip overlaps duel. |033–035; not every extra scene simultaneous with main ending; later rivalry only prolepsis. |

| Knowledge | Holder and change | Observation / provenance limit |
| --- | --- | --- |
| `MT-K-092` Cliff appraisal | Cliff accepts Rudy's ability while retaining dislike; narrator corrects his earlier Zanoba analogy. |001; diligence and accurate liking are different. |
| `MT-K-093` Mediation | Fitts challenges Rudy's authority to decide, Elinalise discloses reason, Cliff accepts condition. |004–005; imagined child mistreatment explicitly corrected, cure promise not cure. |
| `MT-K-094` Identity | Sylphiette identifies herself as Fitts; Ariel separately performs Fitts in town. |006/019/021; current source resolution, no rewriting earlier boundary or every appearance. |
| `MT-K-095` Duel conditions | Rudy/opponent know preparation and no-evasion condition; spectators lack full terms. |008/035; public superiority inference too broad, Badigadi breaks conditional counterblow promise. |
| `MT-K-096` Mask/origin | Fear precedes explanation; Japanese and remembered face establish special connection. |010–011; Orsted absent now, not eliminated threat; reincarnation and transfer distinct. |
| `MT-K-097` Nanahoshi testimony | Reports circles, Orsted travel, no mana/aging and unnamed specialist; Rudy withholds accident context. |011–012; no identified expert or independent circle visit. |
| `MT-K-098` Causal allegation | Tentative disaster association heard without Japanese context; explanation supplies involuntary-transfer claim. |013; causation, intention and culpability distinct; mechanism unknown. |
| `MT-K-099` Research bargain | Initial broad information promise becomes restricted answers and nontechnical book; early trials fail. |016; safety not independently established, future inheritance only promise. |
| `MT-K-100` Curse lead | Rudy labels Hitogami-derived claims uncertain; Cliff sees research utility. |018; no validated curse mechanism or cure. |
| `MT-K-101` Privacy/health | Rudy infers Fitts's gender/body and protects secret after attempted teacher coercion; response ends. |017/019; teacher preserves privacy, inference and complete health change separate. |
| `MT-K-102` Political misreading | Rudy reads visits as surveillance; external account supplies friends' relationship aim. |020–021/027; no intentional hostility established by suspicion. |
| `MT-K-103` Earlier permission | Ariel had authorized disclosure before enrollment; Sylphiette's fears/false wife assumption inhibit it. |022/030; revised past explanation, not new permission at romance crisis. |
| `MT-K-104` Staging and recognition | Rudy lacks rain/quest plan, recognizes friend through cumulative cues, later hears and accepts explanation. |023–026; later assent not prior information. |
| `MT-K-105` Advice and substance | Luke's empathy coexists with false body explanation; risk advice reaches Sylphiette but is incompletely relayed. |027–029; open offer not covert dosing, willingness not full information/capacity proof. |
| `MT-K-106` Morning accounts | Rudy reports recovery and inadequate care; Sylphiette reports pain, happiness and useful support but uncertain equality. |029/032; distinct dimensions, no long-term clinical/ethical certification. |
| `MT-K-107` Earlier rescue | Sylphiette retrospectively confirms accidental garment fall, initial expectation of competence and later intervention. |031; deliberate resilience-test description unwarranted. |
| `MT-K-108` Eris/Nina | Eris's Rudy ideal persists; Nina misreads students and duel conditions but changes practice. |033–035; Eris not shown knowing his rejection story; future rivalry not achieved now. |


## V10 updates — 2026-09-26 UTC

Prior V01–V09 bodies remain historical and unchanged. Current boundary: Japanese LN V01–V10; immutable input audited V09 `40018b5caedfba456da199ed2fea613ec991015a`. Observation suffixes resolve in [V10](../02%20Sequential%20Readings/MT_V10_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V10-`. The [V01–V10 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md) owns cumulative review. Revealed earlier events, present changes and explicit prolepsis retain different times. Draft acceptance, publication/audit and main integration remain separate.

| Chronology | Order / anchor | V10 observation and limit |
| --- | --- | --- |
| `MT-T-053` | Recovery resolve → Ariel audience/marriage declaration → house investigation/renovation; Rudy states sixteen second-life years; roughly three weeks to household discussion. |001–008; age/history distinct, surprise framing does not replace event order. |
| `MT-T-054` | Reception/kinship/duel → two months married and new school year, Rudy second year; Juli roughly one year since purchase. |011–016; explicit relative markers, no forced reconciliation of all earlier school intervals. |
| `MT-T-055` | Letter received → a month later major experiment → roughly week of care → redesign and later successful test. |017–021; no precise calendar constructed by adding every summary. |
| `MT-T-056` | Celebration → sisters arrive that night, about a month after letter and earlier than forecast → next-day escort departure. |022–026; actual arrival overrides expectation, not retroactive certainty at sending. |
| `MT-T-057` | Extra returns roughly one year before Rudy receives letter, to East Port delegation/escort origin. |030–034; sisters nine at letter sending, anticipated ten; Rudy fifteen at sending and predicted16/17 at receipt are Paul's time-relative claims, not uniform present ages. |
| `MT-T-058` | Eris interlude: half-year solitary routine and three-year separation references; narrator announces North Saint recognition one year later. |027–029; future fact explicitly narrated in V10, separate from main present and character knowledge. |
| `MT-T-059` | Edition paratext: electronic2016-03-25, print-basis2016-03-31; OPF literal2016-03-25T04:00:00+00:00. |Reading A/C, colophon spine27p5–9; publication timing is not story chronology or independent WN admission. |

| Knowledge | Holder and change | V10 observation / provenance limit |
| --- | --- | --- |
| `MT-K-109` Marriage/service | Rudy declares marriage, Sylphie accepts while retaining Ariel service; patronage replaces formal subordination. |002; no automatic agreement to later protective plans. |
| `MT-K-110` House/response | Rudy consults friends but avoids future wife, imagines anger; external sentence gives anticipation, she later reveals already knowing surprise. |003/007; his imagined response not her actual state. |
| `MT-K-111` Automaton | Team reclassifies attacker after actual spell/attack results; workshop supports layered mechanism inquiry. Former-owner account remains hypothesis. |004–006; later quiet establishes operational result, not all reconstructed history. |
| `MT-K-112` Performed narration | Renovation account with apparently external ascriptions is revealed as Rudy performance. |007; do not elevate that segment's every thought attribution to independent omniscience. |
| `MT-K-113` Known boundaries/harm | Sylphie states public-touch limit, Rudy apologizes then repeats; his first-night reappraisal expressly acknowledges serious harm. |007–010/015/018; knowledge available without consistently governing action; V09 freeze unchanged. |
| `MT-K-114` Former world | Sylphie asks about earlier world; Nanahoshi supplies false explanation, Rudy avoids full clarification. |011; no informed spouse knowledge inferred from the question or later affection. |
| `MT-K-115` Kinship/history | Sylphie recognizes grandmother from family testimony; Elinalise later reports stigma, raising/withdrawal history. |012; private exchange unheard, self-blame not deserved persecution. |
| `MT-K-116` Duel/protection | Safety terms disclosed but purpose initially withheld; Ariel/Luke care interpretation displaces Rudy's rivalry assumption. Ariel prevention plan discussed without Sylphie. |013; later explanation not prior shared purpose, Rudy counterplan remains private. |
| `MT-K-117` Cliff appraisal/theory | Rudy expects rejection after kinship disclosure; Cliff instead renews care/research, proposes curse/item analogy. |014; imagined rejection false as observed outcome, theory not cure. |
| `MT-K-118` Reciprocal learning | Partial disruption learning and Rudy healing failure observed; explanation through missing recipient sensation is his hypothesis. |016; no established universal reincarnation limit or complete mastery. |
| `MT-K-119` Family letter | Rudy learns planned sister transfer, risk reasoning and rescue prospects; shares letter/asks Sylphie household agreement. |017–018; unlocated escort initially guessed, Zenith not rescued by receiving news. |
| `MT-K-120` Failure/safety | Nanahoshi safety theory given, Rudy cannot assess; actual experiment fails, she initially concludes return impossible. |019; failure, safety-trigger explanation and universal impossibility have different warrant. |
| `MT-K-121` Care/interpretation | Rudy guesses resilience/solitude needs; friends supply different practical observations; Zanoba admits not fully understanding. |020; no professional diagnosis or universal care prescription. |
| `MT-K-122` Design revision/result | Known gap disclosed; several contributors produce layered circle; PET bottle appears. |021; successful material test not human transfer, catastrophe solution or all safety proven. |
| `MT-K-123` Celebration | Intoxicated Sylphie speech interpreted by Rudy; Nanahoshi complaint interrupted and intended thanks guessed. |022; alcohol not truth guarantee or established mental-health remedy; complaint not completed resolution. |
| `MT-K-124` Eris explanation | Ruijerd tentatively proposes misunderstanding; Rudy now imagines intended training but lacks confirmation. |023; reader already knew more, possibility not received actual Eris message. |
| `MT-K-125` Arrival/capacity | Rudy learns Aisha overnight planning after initially reading laziness; girls exhausted, Ruijerd contribution causal. |024; cleverness not complete self-care; Roxy fear here reported, direct access follows extra. |
| `MT-K-126` Old tension | Ruijerd discomfort and Badigadi encounter prompt detailed Rudy conjecture; direct facts remain sparse. |025; no invented revenge/atrocity history or definite Eris cause. |
| `MT-K-127` Norn trust | Ruijerd says she heard/understood Rudy hardships, yet she states distrust; extra supplies feared loss of father and learned alcohol fear. |026/030–032; no violence by Paul against Norn claimed; child/father exception remains her appraisal. |
| `MT-K-128` Roxy correction | Previously heard escort information initially fails to guide feared-identity appraisal; Lilia connection enables recognized mistake. |033–034; fear persists after factual correction, duty acts despite it. |
| `MT-K-129` Historical access/prolepsis | Ruijerd reflects on son with explicitly unknown method; Paul weighs reports and Norn visible reliance; Gal explains curriculum and narrator supplies future certification. |029/032/034; conjecture, direct interiority, testimony and narrated future kept distinct; none automatically Rudy knowledge. |

Preserve earlier interval tensions and the distinction between physical age, remembered biography, social treatment and demonstrated judgment. No later witness is needed to record V10's own explicit prolepsis. Its future time does not make the announced result a current capability.
