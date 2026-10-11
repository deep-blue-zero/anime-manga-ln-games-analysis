---
series: BLUE_ARCHIVE
artifact_type: sequential_deep_reading
scope: GROUP_1201_1203
generation: V1
source_story_ids: ["BA:group:1201", "BA:group:1202", "BA:group:1203"]
status: canonical
source_boundary: "Complete canonical Japanese group objects BA:group:1201 through BA:group:1203 at electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; four scenes, 259 structured utterances including two location units, 257 canonical text anchors, zero choice groups; no other supplemental object admitted by this reading"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# C&C group stories deep reading

## Enjoyed service, delegated authority, and the limit of profitable roles

The complete packet comprises `Cleaning&Clearing`, `Maid&Made（１）`, and `Maid&Made（２）`. It gives C&C a situated ordinary repertoire beyond combat: cleaning, playful enthusiasm, grooming, a cherished jacket, welcoming customers, and enthusiasm for temporary service. Its central argument is that **an institutional cover can become an enjoyable real activity without making that activity the compulsory permanent identity of its members**. Yuuka's accounting concern is legitimate, her reliance and gratitude are explicit, and her proposed conversion of profitable work into an enduring occupation still meets Neru's refusal.

The packet also exposes a peer-governance problem. Asuna accepts a job under the group's stated delegation rule during Neru's absence; its formal validity does not make Neru's practical consent unproblematic. The reading proposes scoped admission for these complete `group` objects, preserves substantial speaker-label uncertainty, and does not claim a full C&C monograph, a universal Yuuka rule, or a placement against Pavane's main-story crises.

## 1. Complete source scope and provenance

All three canonical objects were read in full in source generation `BA_REFRESH_20260928T032248159554Z`, using Japanese text rather than a derived person bundle. The primary witness is `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. All raw groups route to `DB/ScenarioScriptExcelTable1.json`, SHA-256 `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`.

| Source ID and raw group | Complete canonical path relative to the pinned generation | Structured coverage and canonical SHA-256 |
|---|---|---|
| `BA:group:1201`, `1201` | `02_CANONICAL_STORIES/GROUP/CLUB_002_001/EPISODE_001_1201.md` | One scene, `u:0001-0081`; 81 utterances including one location, 80 text anchors, 122 raw records. `4e04aef73b77538311c0d10be87b9276dca6198f4f22398ae65ffa7907203fe0`. |
| `BA:group:1202`, `1202` | `02_CANONICAL_STORIES/GROUP/CLUB_002_001/EPISODE_002_1202.md` | Two scenes, scene 001 `u:0001-0004`, scene 002 `u:0001-0086`; 90 utterances including one location, 89 text anchors, 156 raw records. `3c2b03cc00f385dcc5fd6900e3497732a23b54b1dcce06fad3af61786f466540`. |
| `BA:group:1203`, `1203` | `02_CANONICAL_STORIES/GROUP/CLUB_002_001/EPISODE_003_1203.md` | One scene, `u:0001-0088`; 88 utterances/text anchors, 180 raw records. `7643a8ed00bd7d960e672472f1b672bb26a9116f738bd5b30143546422276228`. |

There are **259 structured utterances, 257 canonical text anchors, and zero choice groups** across four scenes. Location units are rendered as headings. The canonical source contract retains individually recoverable IDs even though these linked club episodes are analyzed together. `03_STRUCTURED_DATA/stories.jsonl` establishes their paths and group classification; `utterances.jsonl` preserves per-unit raw label and `source_record_key`. For example, `:1201:scene:001:u:0042` is raw `유우카` at `ScenarioScriptExcelTable1.json:DataList[106882]`, notwithstanding the attribution problem discussed below. No transcript or raw acquisition file is copied into analytical Git.

The numeric club resolution remains `unresolved_pending_participant_membership_audit`; the reading does not resolve it by prefix. **C&C** is directly named on the truck, in the dialogue, and in the clubroom location. Seminar and Yuuka's accounting role are explicitly named. Secure person routes are `BA_PERSON_AKANE`, `BA_PERSON_ASUNA`, `BA_PERSON_KARIN`, `BA_PERSON_NERU`, and `BA_PERSON_YUUKA`. The existing coverage index sometimes renders Neru as **Nel**; this is the same `ネル`/`BA_PERSON_NERU` subject, not a new person. No additional playable variant, Toki appearance, Rio/Himari presence, or precise command hierarchy is supplied.

## 2. Placement and local chronology

Release dates are absent and story-world placement is unresolved in `RELEASE_CHRONOLOGY.csv`. Group IDs and this review queue do not establish a before/after relation with Pavane C001, C002, the Final arc, or any other group package. Main-source states and quarantines remain those of the [Pavane C001 checkpoint](../MAIN/VOLUME_002_%E6%99%82%E8%A8%88%E3%81%98%E3%81%8B%E3%81%91%E3%81%AE%E8%8A%B1%E3%81%AE%E3%83%91%E3%83%B4%E3%82%A1%E3%83%BC%E3%83%8C/BLUE_ARCHIVE_MAIN_V002_C001_CHECKPOINT.md) and [C002 checkpoint](../MAIN/VOLUME_002_%E6%99%82%E8%A8%88%E3%81%98%E3%81%8B%E3%81%91%E3%81%AE%E8%8A%B1%E3%81%AE%E3%83%91%E3%83%B4%E3%82%A1%E3%83%BC%E3%83%8C/BLUE_ARCHIVE_MAIN_V002_C002_CHECKPOINT.md), whose original witness is preserved.

Within `1201`, an earlier damaging operation precedes the displayed repair receipt; a new assignment precedes the narrator's compressed report/invoice arrival and Yuuka's final complaint (`scene:001:u:0047-0081`). Within `1202`, Yuuka's request precedes an explicit one-hour cut and Neru's discovery of the signed contract (`scene:002:u:0046-0079`). `1203` continues that maid-café undertaking: preparations, opening, and an explicit one-week cut precede the financial report and occupational proposal (`scene:001:u:0001-0088`). These relative relations are secure. The request's reference to making up for recent costs aligns with the first story's problem, but no exact mission/date proves that every mention is one single incident.

Neru is absent from the initial café negotiation and learns it from peers. Asuna's signature is reported and acknowledged, not a displayed executed instrument whose clauses can be inspected. Bystanders' special-force talk is rumor within their conversation; later C&C discussion independently makes the maid disguise/agent distinction explicit. The story does not establish which school population knows the concealed work or its authorizing principals.

## 3. Narrative and scene argument

### 3.1 Ordinary cleaning has real pleasures and a damaged public image

The first story places a C&C-marked truck on campus. Akane hums and invites cleaning in securely attributed lines (`:1201:scene:001:u:0002-0007`). A cluster of unusually assigned complaints and responses contrasts pleasure in cleaning with dislike of it, but exact ownership of several lines is uncertain (`u:0008-0015`). Students discuss whether maid activity is genuine service or a special-force disguise (`u:0016-0022`). Neru securely tells them not to treat the group as a spectacle; Karin corrects that clearing people away is not what cleaning meant (`u:0023-0028`). Asuna's delight in finding a large dust accumulation supplies another independent, concrete ordinary enthusiasm (`u:0029`).

The argument is not that appearances are wholly false. Cleaning can be sincerely liked even while maid costume has operational functions. The episode's joke depends on both meanings remaining available. Nor should the delight be discarded as harmless padding: it differentiates what members enjoy when they are not simply opponents in a main-story security assignment.

Yuuka's arrival produces another attribution-damaged exchange about welcome and the club's public image (`u:0030-0046`). Securely attributed later lines introduce a receipt for building repairs and an explicit accountant's complaint: the operation had expensive precision machinery, the group had been warned, resources are finite, and aftermath matters (`u:0047-0067`). Akane acknowledges the operation was spectacular and promises improvement. Yuuka then expressly says that C&C is relied upon, commissions another task, and asks for clean, quiet execution. The compressed ending reports another unexpectedly large bill (`u:0068-0081`). No amount is printed; no itemized audit proves every damage claim. The final comic failure is still evidence that promised improvement has not satisfied this accountant's reported standard.

### 3.2 A request crosses from civic duty into delegated commitment

In `1202`, Yuuka enters the clubroom and wonders whether her institutional position makes her unwelcome; Karin distinguishes surprise from rejection (`scene:002:u:0002-0005`). Yuuka repeatedly qualifies what she wants: a request, perhaps a mission in one sense, but not the usual mission (`u:0010-0019`). This hesitation matters. The ledger should not flatten her accounting, security, and civic-service interactions into one authoritarian register.

Her reason is a planned electronics-district festival whose student cafés have skewed toward coding experiences and engineering experiments. Merchants have asked Seminar for alternatives. Yuuka questions whether this is really within Seminar's remit, then accepts an obligation because it is within the Millennium district (`u:0020-0033`). The story supports a situated jurisdictional judgment and concern for an enjoyable civic event, not a universal statutory description of Seminar powers. Her comparison with Hyakkiyako/Trinity festivals is her appraisal, not an independently inspected attendance statistic.

She becomes conspicuously polite when asking C&C to run a maid café for a week; Karin notices the register shift. Existing costumes, prior infiltration, and compensation for recent trouble support the appeal (`u:0036-0047`). Costume fit and prior operational access do not by themselves prove willing service labor, a fact the following protest exposes.

An hour later, Neru explicitly refuses. Karin reports acceptance, budgets, a signed contract, and withdrawal costs; Asuna says she signed. Akane states the established rule that Asuna decides when Neru is absent (`u:0048-0079`). This is a real internal delegation, not an invented claim that Asuna forged Neru's consent. But the practical consequence is that the leader discovers a commitment she dislikes after others have made it harder to reverse. Asuna's reasons include the job looking interesting and a share of revenue; pleasure and incentive are distinct. Neru's resistance is pressured by procedure and peer determination, not shown as freely enthusiastic conversion.

### 3.3 A jacket, a hairstyle, and a café reveal limits within participation

`1203` gives ordinary preparation enough detail to differentiate participation from surrender. Akane styles Neru's hair and praises her appearance; Karin seems pleased by the assignment and admits as much after Neru notices. Neru insists that she will keep her sukajan jacket and threatens to leave rather than remove it. Akane accepts that boundary and negotiates the hairstyle; Neru permits it (`scene:001:u:0001-0026`). Thus a pressured job still contains a specific retained preference. The jacket is an observed attachment and condition, not a complete explanation of Neru's childhood, identity, or affect.

Neru corrects operational `コールサイン・ゼロワン` to Asuna's ordinary name (`u:0027-0028`). Asuna brings customers before the shop is ready. A crowd is reported in the dialogue; Karin/Akane infer that the other unusual cafés explain demand (`u:0029-0042`). That explanation is an actor inference, not independently measured market behavior. Karin's excited slips from `標的` and a truncated `処…` into customers/service carry the group's operational language into hospitality; Akane tells her to avoid that speech before customers (`u:0043-0046`). The text does not show harm to patrons. Asuna opens while Neru is still asking for preparation time and delivers the welcome (`u:0047-0050`). Actual café opening is printed; the detailed week of service is compressed away.

### 3.4 Gratitude does not settle who may define the job

After an explicit week, Yuuka marvels at earnings, interrupts her own optimization thought to thank C&C, and says the money looks sufficient to cover recent mission damages (`u:0051-0059`). The arithmetic and transfers are not independently shown. Her gratitude is nevertheless a direct act that contradicts a persona defined solely by anger or rejection.

She then frames stopping as waste/loss, praises how cute/suitable they were, and proposes quitting agent work for permanent maid work, including further festivals and exclusive Millennium service (`u:0060-0082`). This is an occupational proposal grounded partly in profitable contribution and partly in her positive appraisal of their appearance. It is not an enacted directive or formal abolition of C&C. Neru's prolonged silence culminates in an explicit refusal/threat; the story ends there (`u:0083-0088`). Profitable role performance has not established consent to permanent reclassification. The moment resembles the main method's interest in assigned function versus personhood, but it neither retests Alice's hazard nor proves that these situations have identical coercive stakes.

## 4. Character and directed relationship additions

| Subject/direction | Admitted situated repertoire | Boundary |
|---|---|---|
| Yuuka → C&C | Complains about reported material consequences, acknowledges dependence, requests nonstandard civic help with marked politeness, thanks successful contribution, and proposes expansion on financial grounds. `:1201:scene:001:u:0047-0080; :1202:scene:002:u:0010-0047; :1203:scene:001:u:0052-0085`. | Praise/gratitude complicate permanent irritability; profitable reclassification complicates pure recipient-centered benevolence. Neither universal mercy nor universal control is established. |
| Neru → peers/Yuuka | Secure resistance to being publicly watched, to the café assignment, to jacket removal, and to permanent occupational change; limited acceptance of styling and actual participation. `:1201:scene:001:u:0023; :1202:scene:002:u:0049-0066,0072-0086; :1203:scene:001:u:0002-0028,0048,0062,0069-0087`. | Participation does not prove total pleasure, and refusal does not mean she performed no service. Threatened violence at the close is not an enacted assault. |
| Asuna → group | Enjoys unusual dust, accepts an appealing assignment under delegated authority, recruits a crowd, and confidently starts service. `:1201:scene:001:u:0029; :1202:scene:002:u:0067-0079; :1203:scene:001:u:0029-0038,0047-0050`. | Enthusiasm has effects on others' preparation and choices. No general intuition, luck, or commercial-skill model is validated. |
| Akane → Neru/group | Secure cleaning pleasure, courtesy in acknowledging costs, styling care, appearance appreciation, and acceptance of the jacket boundary. `:1201:scene:001:u:0003-0007,0052-0053,0062-0065; :1203:scene:001:u:0001,0009-0025,0045`. | Gentle written forms coexist with insistence about hair and appearance. Damaged first-story labels cannot supply a general coarse-speech persona. |
| Karin → Neru/group | Explains commitment/contract consequences, accepts the stated delegation, visibly enjoys preparation/service, and stumbles between operative/customer vocabulary. `:1202:scene:002:u:0060-0062; :1203:scene:001:u:0004-0007,0022,0034,0039,0043-0046`. | Contract fidelity does not erase the leader's objection. No inference of violence against customers or a full private self follows. |
| Seminar ↔ C&C | Funding, accountability, reliance, nonstandard civic procurement, and possible monetization of the club's appearance coexist. | Receipts, budgets, and contract are discussed, not available for complete audit. No unseen Rio order, formal restructuring, or completed restitution is added. |

## 5. Written language and attribution cautions

This is written Japanese analysis only. Humming marks and elongated spelling do not establish sung pitch or acted delivery. Secure samples include Akane's musical/bright cleaning forms, Neru's `あたし`/coarse refusal, Asuna's excited invitations, Karin's plain operational speech, and Yuuka's accountant vocabulary and request-specific politeness. Interpretation uses repeated secure contexts rather than one isolated marker.

Yuuka's `お願いしたいこと` distinguishes request from habitual mission; Karin's `どうして急に敬語に` explicitly recognizes her approach shift (`:1202:scene:002:u:0010-0019,0038-0039`). `ご相談` and positive appearance/earnings evaluations return when she proposes occupational change (`:1203:scene:001:u:0068-0082`). Softness does not remove the pressure created by prior commitments or material incentive. Conversely, her secure thanks at `u:0055-0059` is not an obligatory façade inferred from anger.

The first story contains extensive label discontinuity. The following ranges remain source-facing warnings, not instructions to silently swap speakers:

| Locator range | Witness issue and use limit |
|---|---|
| `BA:group:1201:scene:001:u:0008-0014` | Akane tags suddenly carry coarse complaints and a request to the leader; a Neru tag asks whether the leader likes cleanliness. Ensemble contrast is recoverable, but exact complaint/pleasure ownership and individual register are not secure. |
| `BA:group:1201:scene:001:u:0030-0046` | An Asuna tag rebukes Asuna's apparent railing activity; Karin carries a coarse visitor complaint; Akane/Neru/Yuuka tags repeatedly alternate incompatible reply positions and diction. Public-image discussion and visitor friction are usable as an exchange; do not fix precise culpability or voice by expected personality. |
| `BA:group:1202:scene:002:u:0052,0082-0084` | Neru-tagged replies seem to answer her own refusal/complaint; the final Akane-tagged pair alternates plain/polite persuasion. Retain raw labels and mark individual ownership uncertain rather than repairing to Asuna/Karin. The signed contract/delegation is independently printed in secure surrounding passages. |
| `BA:group:1203:scene:001:u:0035,0080` | Asuna-tagged surprise follows her recruitment explanation; Karin-tagged `あらあら` resembles another local speaker's register. These are cautions, not proof of erroneous labels; crowd arrival and the later proposal remain independently supported. |

The structured records confirm that the suspect labels are in the witness. An unknown initial visitor is strongly continuous with Yuuka's immediate clubroom arrival in `1202`, but exact `？？？` lines remain labeled unknown; the initial unknown in `1201` similarly introduces the arriving visitor without a retroactive label repair. Two campus bystanders (`ミレニアムの生徒A/B`) are local roles, not identified students or universally reliable institutional narrators.

## 6. Counterreadings, power, and reconstruction disposition

**“Maids are a fake cover, so the ordinary material is irrelevant.”** Neru's explicit cover complaint supports the operational interpretation; Akane's pleasure, Karin's admission, Asuna's enthusiasm, and actual customer welcome establish that performed service can also be a desired real experience. Neither meaning eliminates the other.

**“Yuuka is only a hostile accountant.”** Damage complaints and the final expansion proposal make accounting central. Reliance, civic concern, difficult asking, thanks, and positive appraisal prevent hostility from becoming the total person. Conversely, those virtues do not erase pressure on Neru or the attempt to turn temporary enjoyment into profitable permanence.

**“Asuna's signature invalidates every Neru objection.”** The local delegation rule supports procedural acceptance. It does not prove Neru had meaningful input into the assignment or that the contract's exact terms eliminate every exit. Her jacket negotiation and final refusal distinguish bounded participation from consent to any subsequent role.

**“Comedy means destruction and coercion have no consequences.”** Repair receipts, invoices, a compensation rationale, budgets, and withdrawal concerns provide material consequences. Their comic rendering does not settle exact loss or enforceability, and the main crisis's injuries must not be imported here. The closing threat has no printed strike or injury.

The Pavane checkpoints establish role-concentrated enforcement, opposition, cooperation, and incomplete accountability. These group scenes broaden ordinary comparison without changing those chronology-bound histories. C&C is not only a security obstacle or rescue coalition; Seminar's accountant is not only an emergency power actor. The packet exposes opportunities and limits inside familiar institutional relations.

**Observed behavioral delta:** request under civic obligation → delegated acceptance before leader's return → pressured temporary participation with a retained personal boundary → enjoyable/profitable service → proposal of permanent role conversion → refusal. This is a bounded repertoire/mechanism, not a validated general rule. No model or prediction was frozen before opening the stories; `NO_DIAGNOSTIC_OPPORTUNITY`. No model promotion, prospective score, or new durable claim ID is proposed.

## 7. Proposed seven-ledger deltas

The integrator owns shared ledgers and admission. Append this packet's contextual delta while preserving prior first-pass dates, witnesses, main states, and claim history.

| Ledger | Proposed effect |
|---|---|
| Character state | Add the five subjects' secure ordinary repertoire in §4. Yuuka gains reliance, civic asking, gratitude and profit-led expansion alongside accounting anger; C&C gains pleasure, performance, delegated decisions and bounded refusal. Do not change office, Toki status, injuries, or reconstruction category. |
| Relationship state | Add Yuuka→C&C accounting/request/gratitude/expansion; Asuna→Neru delegated commitment and resistance; Akane→Neru styling with an accepted jacket boundary; Karin→team contract framing and enjoyed service. Retain label cautions and no global friendship/romance conclusion. |
| School club institution | Add C&C's service/agent distinction, funding and aftermath concerns, local delegation rule, electronics-district civic request and temporary café. Revenue/repair capacity are reports; no legal contract audit or permanent restructuring. |
| Sensei role and ethics | **No material direct delta:** no printed Sensei appearance, speech, choice, inward thought, instruction, or knowledge. Zero branches. Civic work and peer tensions have no observed teacher author. |
| Japanese voice and address | Add secure role/request/register contrasts, `メイド`/`エージェント`, `依頼`/`任務`, `契約`/`サイン`, `事後処理`, and `ご主人様` versus operative slips. Carry all §5 warnings; no performed voice. |
| Motif theme callback | Add service as cover and pleasure, cleanliness versus destruction, hair/jacket as negotiated presentation, contract versus willing participation, fiscal value versus chosen occupation. Comparison with main assigned-function questions is explicitly analogical, not a proved callback or chronology edge. |
| Claim revision | `BA-C017` **STRENGTHEN / COMPLICATE locally**: delegated/formal commitment does not settle meaningful participation or limits of later consent. `BA-C015` **PRESERVE / SCOPED ANALOGY**: means/aftermath matter, but Abydos's survival claim is not retested directly. `BA-C006` **PRESERVE REJECTED**: student civic work succeeds without a printed adult replacement; this is one case, not universal competence. `BA-C019` and `BA-C020` **PRESERVE / NO DIRECT TEST**: role/value analogies do not adjudicate game production/belonging or Alice's real hazard. Sensei-specific claims receive no direct test. No new claim ID. |

## 8. Coverage, admission, and open debts

**ADMIT_WITH_LIMITS proposed** for exactly `BA:group:1201`, `:1202`, and `:1203`. Analytical value is **HIGH** for Yuuka/C&C ordinary institutional and peer comparison. Cleaning, grooming, appearance preferences, enjoyment and welcomes have affirmative value independent of plot-state change. Their value is not conditional on explaining combat behavior.

On acceptance, the group coverage cells for **Yuuka, Akane, Karin, Asuna, and Neru/Nel** should record these three complete objects as analyzed. Other group objects and private/voice classes are outside this reading. The two bystanders may be reconciled as narrowly source-scoped role actors without merging with other generic student A/B rows. No Sensei person appearance or bond/MomoTalk/character-data admission is created.

| Gap | Contribution and remaining limitation |
|---|---|
| `G01` ordinary/private breadth | Partial reduction for five subjects: pleasure in service, preparation, an accessory boundary, request/gratitude, and minor peer governance. No complete private dyads or full group corpus. |
| `G02` Yuuka council/club transfer | A complete civic-service/contract/revenue context broadens the main role envelope. Request-specific register, reliance and gratitude are observed; expansion pressure and refused permanence are contrary cases. No arbitrary private-setting rule or operational model. |
| `G07` chronology | Internal hour/week and mission/report relations are supported; placement against main and other supplemental stories remains unresolved. |
| `G09` attribution | The precise damaged or uncertain ranges in §5 remain quarantined for individual voice/action. Zero player choices simplifies this packet only. |
| `G10` performed voice | Unchanged; typography and text do not supply acting. |
| `G12` identity/variant | Same source persons; no Toki or playable-variant conditions admitted. Generic bystanders remain separate from known students. |
| `G13` contract/outcome | Signature, delegation, spending and revenue are dialogue/narrative reports; contract terms, legal validity, paid damages and permanent role change are unverified or unprinted. |

Open questions concern recurrence of Yuuka's request/gratitude repertoire outside C&C, how delegated authority protects members' later refusals, and whether individual desires for cleaning, presentation, service or operational work persist elsewhere. Neither profit nor one objection resolves those whole-person questions. No rejection of quieter unread material follows.

## 9. Evidence locator map

| Finding | Exact primary route |
|---|---|
| Real cleaning pleasure, public cover discussion, spectacle objection | `BA:group:1201:scene:001:u:0002-0029` with u:0008-0014 caution |
| Damaged visitor exchange | `BA:group:1201:scene:001:u:0030-0046` |
| Repair costs, warned equipment, reliance, new request, invoice coda | `BA:group:1201:scene:001:u:0047-0081` |
| Clubroom welcome, request/mission qualification | `BA:group:1202:scene:001:u:0001-0004; scene:002:u:0002-0019` |
| Civic festival problem and Seminar's situated obligation | `BA:group:1202:scene:002:u:0020-0033` |
| Polite maid-café request | `BA:group:1202:scene:002:u:0034-0047` |
| One-hour cut, refusal, contract, Asuna signature, delegation | `BA:group:1202:scene:002:u:0048-0086` with u:0052,0082-0084 caution |
| Hair, jacket boundary, service pleasure and name correction | `BA:group:1203:scene:001:u:0001-0028` |
| Recruitment, crowd, operative slips, actual opening | `BA:group:1203:scene:001:u:0029-0050` with u:0035 caution |
| One-week cut, revenue appraisal, direct gratitude | `BA:group:1203:scene:001:u:0051-0059` |
| Permanent occupational proposal and refusal | `BA:group:1203:scene:001:u:0060-0088` with u:0080 caution |

## Integration acceptance — 2026-10-01

[Phase 2 cycle 001](../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md) accepts exactly the source IDs declared above with **ADMIT_WITH_LIMITS**. The cycle owns final ledger, coverage and readiness adjudication; proposals in this reading remain source-facing contribution history. No cross-source chronology or performed-voice evidence is added.
