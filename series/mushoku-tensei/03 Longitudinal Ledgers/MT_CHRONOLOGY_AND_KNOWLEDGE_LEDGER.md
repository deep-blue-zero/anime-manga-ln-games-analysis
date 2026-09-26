---
title: "Mushoku Tensei - Chronology and knowledge ledger"
artifact_id: MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER
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
