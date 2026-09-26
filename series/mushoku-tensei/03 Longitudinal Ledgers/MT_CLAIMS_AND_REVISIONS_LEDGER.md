---
title: "Mushoku Tensei - Claims and revisions ledger"
artifact_id: MT_CLAIMS_AND_REVISIONS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.6"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V06 only; prior history preserved, V06 candidate updates; publication/audit separate."
---

# Claims and revisions ledger

## Responsibility

Owns load-bearing analytical propositions, alternatives, prospective tests, and dated revision history. A volume reading owns its underlying observations; this ledger links them and records change of assessment.

## Record format

`claim ID | formulation | witness/range | class | support | counterevidence | alternatives | confidence basis | current assessment | revision events | affected homes`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append revisions with prior and new formulation, evidence, input boundary, and dependent homes. Never overwrite a historical freeze. A test needs an opportunity and a disconfirming observation; absent opportunity means UNTESTED. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

The historical initial state above is preserved. Current scope is **MT-LNJP-V01 only**, the [accepted V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md), observations `MT-E-LNJP-V01-001`–`016`. No V02 or later witness contributes. These are new bounded formulations, not revisions of nonexistent pre-V01 claims. Confidence concerns the stated V01 scope, not the series. `OPEN` means insufficient discriminating evidence, not a prediction of later outcomes.

| Claim ID | Current V01 formulation / class | Support; significant contrary or limiting evidence | Assessment and next test |
| --- | --- | --- | --- |
| `MT-C-001` | Rudeus's learning progress is produced through repeated experiment **and** material/relational support, not solely innate genius. `STRONG_INFERENCE` | `005–008,015`: books, parental reading, paid tutor, village practice, correction after failed trials. His unusual early silent casting is real, but its population-wide cause is not determined. | `OPEN` to developmental and individual alternatives; do not infer unlimited mana growth from a few trials. Reassess with separately verified later instruction/constraints. |
| `MT-C-002` | Ability and movement improve while consent-sensitive restraint remains uneven in V01. `STRONG_INFERENCE` | `005,008,011–013,016`: gate crossing and care; violation of Sylphie's refusal, theft, manipulation, possessive fantasy. He apologizes and temporarily self-interrupts, so “no recognition at all” is false. | Preserve dimensional formulation; comparable later refusals and costly restraint would discriminate durable change. No whole-series trajectory declared. |
| `MT-C-003` | V01's other focalizers materially qualify Rudeus's self-account. `STRONG_INFERENCE` | `004,010,013,014,016`: Lilia's fear and work, Paul's defensive motive and error, Lilia's self-blame, Zenith's independent reason for care. These viewpoints can themselves rationalize and are not omniscient. | Preserve as a formal claim; compare later viewpoints without flattening disagreement. |
| `MT-C-004` | The Sylphie boundary scene combines a clear refusal and persistent distress with a comic reveal frame. `STRONG_INFERENCE` | `011` and image `text/part0019.html`: explicit protest, further override, apology and later avoidance; comedic surprise and Paul's partial normalization. Later play does not settle the injury. | V01 conclusion is mixed, with a definite wrongful override under the stated consent criterion; reception/creator intent unavailable. |
| `MT-C-005` | The family meeting achieves immediate protection by a knowingly fabricated allegation and Zenith's choice; its means and consequence remain ethically distinct. `STRONG_INFERENCE` | `013–014`: risk of departure, Rudeus's lie and subsequent disclosure, Lilia's distinct past assault and recent invitation, Zenith's extra on what changed her mind. No external verification of all backstory. | A local protective outcome cannot certify a general truthfulness or victim-centered rule; examine later consequences only if authorized. |
| `MT-C-006` | Paul's stated concern about dependency has evidence, but V01 does not validate his forced five-year separation as necessary or effective. `STRONG_INFERENCE` for concern and coercion; `UNRESOLVED` for outcome | `012,015–016`: Sylphie's pleas, Rudeus's possessive fantasy, Paul's ambush/no-contact order and doubt. Sylphie's own future opportunity is not observed. | Keep justification and outcome separate; no V02 inference. |
| `MT-C-007` | Roxy, Lilia, Zenith and Sylphie each have choices, labor and/or constraints not reducible to Rudeus's improvement. `STRONG_INFERENCE` | `004,006–009,011–016`: employment, self-education, domestic care, refusal and protest. Access remains uneven, especially Sylphie's interiority. | Preserve plurality without inventing offstage agency. |

**Revision register:** V01 was the first narrative unit, so earlier analytical claims were absent. During V01, provisional character reports were corrected rather than promoted: Lilia's aversion is not simply dislike of children (`004`); the supposed fabricated injury of the bullying child is withdrawn after later information (`010`); a manual's fixed-capacity assertion is contradicted by Rudeus's observed short-term trials without establishing a universal replacement rule (`005`). Future material revises these IDs with a dated prior formulation and dependent-home review; the V01 entering freeze remains intact.

## V02 revision register — 2026-09-26 UTC

Input: audited V01 commit `eaf159559c6fc76ddd820178d7588545f08c351d`. The V01 formulations above remain historical. Current scope is V01–V02, with V02 observations owned by [the V02 reading](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings); numbers below mean `MT-E-LNJP-V02-NNN`. No later source contributes. Publication/audit of this transaction is tracked separately in the current entrypoint.

| Revision ID / claim | Prior → current bounded formulation | Transition; evidence and counterreading | Confidence / discriminating test / dependencies |
| --- | --- | --- | --- |
| `MT-CR-008` / `MT-C-001` | V01 supported learning → repeated instruction, resources and institutions causally support competence in both volumes. | STRENGTHEN; `001,006–012,017`. Unusual aptitude remains real; failed chantless teaching and limited sword aptitude reject effortless transfer. | Strong inference, high within scope. Compare performance when supports change; character/form ledgers. |
| `MT-CR-009` / `MT-C-002` | V01 uneven consent-sensitive restraint → recognition, particular restraint and continued entitlement coexist through V02. | STRENGTHEN; `003,005,006,009,014`. The gift-night restraint is a real negative case to absolute incapacity; the later violation defeats a generalized change claim. | Strong inference, high. Future promise is not demonstrated persistence or irrevocable consent; normative/relationship/state ledgers. |
| `MT-CR-010` / `MT-C-003` | V01 alternative focalizers qualify Rudy → V02 widens access while making some alternative judgments contestable. | STRENGTHEN; `011,015–019`. Ghislaine's minimization and romantic guesses, Roxy's idealization and powerful observers' suspicion prevent treating alternate access as truth certification. | Strong formal inference, high. Track each disclosure's holder and limits; knowledge/form ledgers. |
| `MT-CR-011` / `MT-C-004,005` | V01 Sylphie boundary/family-meeting findings → unchanged historical conclusions. | PRESERVE; no new direct testimony about Sylphie's injury or the household allegation's later consequences. V02 `014` is comparison, not replacement evidence. | No-material-revision after review. Do not infer offstage reconciliation; normative/relationship ledgers. |
| `MT-CR-012` / `MT-C-006` | V01 separation's efficacy wholly open → the job now yields learning, work and relationships, and Rudy positively reappraises the support. | REVISE; `002,006–012`. No controlled alternative demonstrates that ambush/no-contact terms caused or were necessary for these benefits; Sylphie's outcome still unknown. | High for represented benefits/reappraisal, unresolved for necessity and other child's development. State/relationship/knowledge ledgers. |
| `MT-CR-013` / `MT-C-007` | V01 secondary aims irreducible to protagonist growth → Eris, Ghislaine and Roxy add substantial independent choice, labor and limits. | STRENGTHEN; `005–019`. Hilda's backstory remains Philip-mediated; many absent people lack current access. | Strong inference, high. Do not invent unseen autonomy; state/relationship/form ledgers. |
| `MT-CR-014` / `MT-C-008` | New claim: adaptive teaching works by matching task, existing competence, motivation and resources. | OPEN as longitudinal claim; `006–008,010–011`. Rudeus's insistence that kidnapping was prerequisite is an untested counterfactual; rest, explanation and shared practice demonstrably matter. | Strong V02 inference, no universal teaching law. Test changed learners/settings and failed transfer; state/form/normative ledgers. |
| `MT-CR-015` / `MT-C-009` | New claim: status and narrative accounts distribute credibility, opportunity and control, with consequential mistakes. | OPEN; `004–005,008,010,012–013,015–019`. Kinship protects and recruits; official rescue account and later cult select different meanings. Institutions can enable refusal as well as constrain it. | Strong V02 pattern, not a total social theory. Test who can contest an account and at what cost; all relevant topical ledgers. |
| `MT-CR-016` / `MT-C-010` | New claim: displacement separates agency from secure knowledge of outcomes. | OPEN; `017–019`. Search choices and Ghislaine's survival are represented; destinations, reunions and cause remain partly or wholly unknown. | High for bounded observation, working hypothesis for longitudinal structure. Compare message reception and route choices; chronology/relationship/form ledgers. |

No registered entering outcome prediction existed. V02 answers questions without manufacturing successful forecasts. A new targeted maintenance review is frozen in V02 Section L; V05/V10/V15 cumulative reviews remain due.


## V03 updates — 2026-09-26 UTC

Prior V01/V02 bodies remain historical and unchanged. Current scope is Japanese LN V01–V03; input is audited V02 head `687a13ac1a661270ab566c9e1a6028acd607d846`. Observation suffixes below resolve in [V03's diagnostic readings](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V03-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Revision / claim | Prior → current formulation | Transition / basis / counterevidence | Confidence, test and dependencies |
| --- | --- | --- | --- |
| `MT-CR-017` / `MT-C-001` | Socially supported competence → selective transfer that can coexist with disastrous appraisal. | REVISE; `003,005,007,013–015,019–020`. Strong magic and paid work do not establish reliable rescue timing. | High bounded inference. Test changed support/feedback; state, model001–004, form. |
| `MT-CR-018` / `MT-C-002` | Recognition/restraint mixed → actual V03 comparable restraint but recurring misconduct and external enforcement. | STRENGTHEN; `008–009,011–012,014,016,018–020`. Reject both no change and complete ethical reform. | High. Test unpoliced restraint and costly disclosure; normative/relationship/model005–008. |
| `MT-CR-019` / `MT-C-003` | Multiple fallible focalizers → also distinguish omniscient local facts from character prayer/history and mistaken absolution. | STRENGTHEN; `001,010,014–018,021–022`. Alternative voice not universal truth. | High formal inference. Track holder/proposition; knowledge/form. |
| `MT-CR-020` / `MT-C-004,005` | Historical V01 findings unchanged. | PRESERVE; no direct new evidence about those original events/affected persons' later appraisals. | No material revision. Later comparison not rewrite. |
| `MT-CR-021` / `MT-C-006` | Employment benefited learning without proving forced separation necessary → remains bounded. | PRESERVE; `003,005,019` show additional uses of skills, not necessity of coercive method. | High for benefit, unresolved causal counterfactual; state/relationship. |
| `MT-CR-022` / `MT-C-007` | Secondary people have own aims → clients, workers, companions and palace actors affect outcomes outside Rudy's intentions. | STRENGTHEN; `002–005,008,010,013,017–022`. Some remain thinly focalized. | High. Test agency beyond instrumental usefulness; state/relationship/form. |
| `MT-CR-023` / `MT-C-008` | Adaptive teaching depends on fit/resources → context and learner differences remain necessary across travel. | REVISE; `005,013,019–020`. Nonverbal combat instruction works for Eris, not Rudy; excess praise fails. | High. No universal recipe; model001–002/state/form. |
| `MT-CR-024` / `MT-C-009` | Public accounts distribute credibility → performance, reports and identity can both create access and misassign responsibility. | STRENGTHEN; `006–007,010–018,020–022`. Genuine service changes particular judgments; not all trust false. | High. Compare informed/partial recognition and costs; all topical homes. |
| `MT-CR-025` / `MT-C-010` | Displacement separates agency/secure knowledge → destinations and palace consequence now known, cause and many fates still open. | REVISE; `001,003,009,022`. No inferred message reception or newcomer identity. | High local facts, unresolved causes; chronology/form. |
| `MT-CR-026` / `MT-C-011` | New: optimizing gratitude/status can narrow attention to others' immediate danger. | OPEN; `006,012–014,016`, with V02:003 comparison. Cooperative routine is substantial countercase to all planning being manipulative. | Strong bounded inference, not fixed universal trait. Test abandoning an advantageous script before outside interruption; model003/006, normative/form. |
| `MT-CR-027` / `MT-C-012` | New: reciprocal reliance and consultation reduce private decision burden, imperfectly. | OPEN; `018–020`. Useful contribution immediate; secrecy, leader authority and outside enforcement qualify it. | Moderate process claim. Test inconvenient dissent and pre-harm consultation; model007–008/state/relationship. |

The V03 checkpoint activates a bounded living Rudeus model with retrospective contrast tests. No unregistered question becomes a prediction success. No model is DOMAIN_READY. V05 cumulative review remains due.


## V04 updates — 2026-09-26 UTC

Prior V01–V03 bodies remain historical and unchanged. Current scope is Japanese LN V01–V04; input is audited V03 head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Observation suffixes below resolve in [V04's diagnostic readings](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V04-`. Publication and final exact-head audit remain separate from this preparation snapshot.

| Revision / claim | Prior → current formulation | Transition / source / strongest qualification | Test and dependencies |
| --- | --- | --- | --- |
| `MT-CR-028` / `MT-C-001` | Selective supported competence → gifts, practice, interpretation and complementary roles jointly matter. | STRENGTHEN; `001,003–005,008,010,013–014,017,022,026`; extraordinary aptitude real, not universally sufficient. | High bounded inference; new task/support contrast; state/form/models. |
| `MT-CR-029` / `MT-C-002` | Actual restraint with recurring misconduct → new unpoliced restraint/immediate help, later pressure and intrusion. | STRENGTHEN; `008–010,013,018,021,025`; care neither cancels harm nor becomes fictitious because harm persists. | High; comparable unpoliced transfer; normative/relationships/model005. |
| `MT-CR-030` / `MT-C-003` | Fallible perspectives → corrections include self-inconsistency, mistaken benevolent trust and hopeful dependency judgment. | STRENGTHEN; `006–007,009,011–012,019–020,023–026`; independent narration may establish local facts, not every motive. | High; holder/proposition audit; form/knowledge. |
| `MT-CR-031` / `MT-C-004,005` | V01 findings → unchanged historical formulation. | PRESERVE; no direct new affected-person account of those original events. | No-material revision; comparisons retained separately. |
| `MT-CR-032` / `MT-C-006` | Job benefits without necessity proof → remains bounded. | PRESERVE; new uses of teaching not controlled counterfactual; unresolved alias not Sylphie outcome evidence. | Necessity unresolved; state/knowledge. |
| `MT-CR-033` / `MT-C-007` | Independent aims → substantial peer world, Roxy search, Geese work and court agency. | STRENGTHEN; `006–007,016–026`; limited access to captives/assassin/absent people still matters. | High; ordinary choices beyond protagonist utility; Eris model/state/relations/form. |
| `MT-CR-034` / `MT-C-008` | Task/learner fit → also access to instruction and socially valued work. | REVISE; `003–006,016–018,021–023`; Geese refuses instruction, anatomy limits imitation, Eris initiates teaching. | High; new learner/teacher contexts; models/state/form. |
| `MT-CR-035` / `MT-C-009` | Accounts distribute access/blame → recognition can also impose burdens or fail against institutional barriers. | STRENGTHEN; `001,005–007,011,014–016,019,022–026`; actual goodwill remains real. | High; whether informed recognition changes constraints; all topical homes. |
| `MT-CR-036` / `MT-C-010` | Destinations known, causes/fates open → expanded dispersed survivor histories, continued failed information transfer. | REVISE; `006–007,015–016,023–026`; future court escape announced not completed, no Rudy reunion/message. | High local observation; track actual reception; chronology/form. |
| `MT-CR-037` / `MT-C-011` | Gratitude optimization can narrow rescue attention → reward wording alone cannot identify delayed-help mechanism. | REVISE; `003,009–010,013–014`; immediate fire rescue is countercase, explicit gratitude demand persists. | High; compare sequence before motive shorthand; model003/normative. |
| `MT-CR-038` / `MT-C-012` | Reliance/consultation reduce burden imperfectly → can also transfer burden through miscalibrated trust/dependency. | REVISE; `005,011–014,017–022,024–026`; actual corrected choices prevent an all-coercion reading. | Strong bounded inference; costly disclosure/expressed needs; models/relations/state. |
| `MT-CR-039` / `MT-C-013` | New: perceived usefulness distributes belonging and obligation, sometimes narrowing choice. | OPEN; `018–022,024–025`; Geese's lost role, Eris's desired task, warrior expectations and Fitts's fear; voluntary gifts/care challenge exclusively transactional account. | Moderate cross-context thematic inference. Test affection/help independent of performance; existing ledgers sufficient, specialist review V05. |

V04 checks interrogate previously fixed model rules, but no outcome prediction was registered and prior familiarity remains. New Eris model is retrospectively fitted. V05 cumulative checkpoint must assess V01–V05 and artifact responsibilities, not just count supportive rows.


## V05 updates — 2026-09-26 UTC

Prior V01–V04 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V05; frozen published input is audited V04 head `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. Observation suffixes below resolve in [V05's diagnostic readings](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V05-`. The [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) owns the historical cumulative synthesis; publication/audit remain separate from this preparation snapshot.

| Revision / claim | Prior → current formulation | Transition / evidence / strongest qualification | Test / dependencies |
| --- | --- | --- | --- |
| `MT-CR-040` / `MT-C-001` | Distributed competence → ability, coordination, interpretation and care remain distinct. | STRENGTHEN; `001–006,012,018–019,025,027`; exceptional endowment remains real. | Changed support/task; models/state/form. |
| `MT-CR-041` / `MT-C-002` | Local restraint and continued harm → particular repair and broader refusal-respecting intention, with incomplete transfer. | REVISE; `007–015,022,025`; misreading women and the cook outburst counter global maturation; intention is not a persistence test. | New unpoliced boundary/repair; normative/models. |
| `MT-CR-042` / `MT-C-003` | Fallible perspectives → distinguish corrective fact, attributed explanation and deliberate noncorrection. | STRENGTHEN; `004,007,010,017–019,023–028`; the source can establish falsehood without every speaker being infallible. | Holder/proposition audit; knowledge/form. |
| `MT-CR-043` / `MT-C-004` | V01 Sylphie boundary → preserved historical finding. | PRESERVE; no new direct account of that violation; competence report is not retroactive consent. | No material revision; normative. |
| `MT-CR-044` / `MT-C-005` | V01 household crisis → Paul confirms earlier assault/motive and reports later domestic negotiation. | REVISE; `004,012`; new agency report does not excuse originating betrayal/deception; no new women's interiority. | Direct later account if admitted; normative/relations. |
| `MT-CR-045` / `MT-C-006` | Job benefits and open necessity → Sylphie's education after separation now reported too. | REVISE; `012`; several teachers/supports, no controlled alternative to the coercive ban. | Keep outcome and necessity separate; state/knowledge. |
| `MT-CR-046` / `MT-C-007` | Independent aims → new care, work, refusal, adventure and political choice across the ensemble. | STRENGTHEN; `004–005,008–020,023–028`; access remains uneven. | Ordinary decisions outside Rudy's benefit; models/relations. |
| `MT-CR-047` / `MT-C-008` | Task/learner/access → magic rank differs from coordination and attributed teacher credit. | STRENGTHEN; `012,018–019,024–025`; Cliff's skills are real, Eris learned but can be reckless. | Transfer and misattribution; models/form. |
| `MT-CR-048` / `MT-C-009` | Accounts distribute access/burden → shared performance can enable care while concealment/falsehood retain costs. | REVISE; `007,011,014–016,019,021–022,025–028`; performance alone is not manipulation. | Who can contest/consent; models/normative/form. |
| `MT-CR-049` / `MT-C-010` | Dispersed knowledge → actual family disclosure, notices seen but unshared, partial escape evidence. | REVISE; `007,009,012,017,020,024,026–028`; fates, cause and alias remain unresolved. | Actual message holder; chronology/knowledge. |
| `MT-CR-050` / `MT-C-011` | Sequence-sensitive gratitude mechanism → immediate aid can still fail at hearing and identification. | STRENGTHEN; `002–003,016`; no engineered delay, no claim that all helping has pure motives. | Comparable order of decision; model003/normative. |
| `MT-CR-051` / `MT-C-012` | Reliance can help or overburden → repair needs received care and shared information, not confidence alone. | STRENGTHEN; `006,008–015,017,020,023,027`; offered choice and notice failure are both actual. | Inconvenient needs/disclosure; models/relations. |
| `MT-CR-052` / `MT-C-013` | Usefulness/belonging working theme → repeated capacity-to-duty inference with nontransactional care countercases. | STRENGTHEN; `006,008–015,017,023–027`; Norn, parents and comfort prevent an exclusively exchange-based account. | Help after failure/refusal; checkpoint/models/relations. |
| `MT-CR-053` / `MT-C-014` | NEW: responsibility for an account changes when error becomes available to correction. | OPEN; `028` versus `007,010,017,027`; explicitly known omission differs from unavailable facts; one especially diagnostic case. | Recognized error/repair cost, not blame for all partial knowledge; knowledge/normative/form. |

All substantive transitions above are strong bounded inferences unless explicitly a report, intention or unresolved proposition. C014 is a working longitudinal hypothesis from one explicit deliberate-omission case, supported by contrast rather than presumed universality. V05 registered questions, not predictions; no retrospective forecast success is claimed. The cumulative checkpoint narrows models and adds Paul/Ruijerd/Roxy without DOMAIN_READY or new source lanes.


## V06 updates — 2026-09-26 UTC

Prior V01–V05 bodies remain historical and unchanged. Current source boundary is Japanese LN V01–V06; frozen input is final audited V05 head `3dc6b173b044abdafc013dc989bd96914620d13d`. Observation suffixes below resolve in [V06's diagnostic readings](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V06-`. The [V06 disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews altered premises; the V01–V05 cumulative checkpoint remains historical. Publication/audit remain separate from this preparation snapshot.

| Revision / claim | Prior → current formulation | Transition / evidence / strongest qualification | Test / dependencies |
| --- | --- | --- | --- |
| `MT-CR-054` / `MT-C-001` | Distributed competence → useful action can survive dependence, defeat and global negative self-appraisal. | STRENGTHEN; `003,005,010,016,018,026–028`; unusual aptitude real, collective outcomes not sole strategy. | Changed task/support; models/state/form. |
| `MT-CR-055` / `MT-C-002` | Local repair/intention without general transfer → further refusal/aid alongside continued intrusion and recognized vulnerability insufficiently acted on. | REVISE; `005–008,012,014,018,023`; no total absence of care or general maturation. | Comparable unpoliced choices; normative/models. |
| `MT-CR-056` / `MT-C-003` | Fallible viewpoints and correction → Eris corrects breakup explanation while misjudging capacity; supernatural accounts useful before verified. | REVISE; `004,013,015,017,021,024–029`; local narrator confirmations distinguished from characters' theories. | Holders/truth/confidence separately; all knowledge-dependent homes. |
| `MT-CR-057` / `MT-C-004` | V01 Sylphie refusal/comic frame → historical conclusion preserved. | PRESERVE; `021` supplies survival report, no new account of original violation; `023–024` comparative only. | No retroactive consent or new Sylphie interiority; normative. |
| `MT-CR-058` / `MT-C-005` | Household protection, harmful means and later negotiation → Lilia's history/self-questioning give new affected-person access. | REVISE; `012,029–031`; prior assault independently focalized, maternal love coexists with imposed service; original meeting findings retained. | Whether expressed care changes available choice, not whether love exists; normative/relations/checkpoint. |
| `MT-CR-059` / `MT-C-006` | Educational benefit without necessity proof → unchanged causal limit. | PRESERVE; `014,024,029` add practice/outcomes, not a controlled alternative validating Paul's coercive separation. | Teaching opportunities not retrospective necessity; state/model. |
| `MT-CR-060` / `MT-C-007` | Ensemble has independent aims/work → overlapping rescue, refusal, training and information missions. | STRENGTHEN; `010,020,022,025,027–031`; unequal options and partial access remain. | Meaningful choice outside protagonist benefit; relations/models. |
| `MT-CR-061` / `MT-C-008` | Task/learner/access fit → recipes, trained spell defense, sword instruction and disruption practice preserve instruction/feedback limits. | STRENGTHEN; `003,005,007,014,016,018,024`; quantity/future sight cannot replace learned execution. | Changed learner/task feedback; models/form. |
| `MT-CR-062` / `MT-C-009` | Accounts distribute access and shared performance can enable care → protective secrecy can obstruct correction and reciprocal choice. | REVISE; `002,006,013,019,025–026`; motives not all exploitative, explicit decision rights also observed. | Who can contest premises before consequence; models/relations/form. |
| `MT-CR-063` / `MT-C-010` | Dispersed disaster news → corrected record reading and organized but incomplete information delivery. | STRENGTHEN; `021,026–028`; cause/fates not universally known, lead not rescue. | Actual receipt and qualification; chronology/knowledge. |
| `MT-CR-064` / `MT-C-011` | Gratitude mechanism depends on intervention order → prompt rescue again, with technical/interpretive limits. | STRENGTHEN; `005–006`; later admiration management does not retroactively make rescue delayed staging. | Comparable decision sequence; model003/normative. |
| `MT-CR-065` / `MT-C-012` | Reliance needs care/shared information → perceived competence and burden can mutually intensify while useful support remains. | REVISE; `018–020,024–026`; vulnerability recognition can prompt mistaken self-exclusion, not only repair. | Explicit need and communicated interpretation; models/relations/checkpoint. |
| `MT-CR-066` / `MT-C-013` | Usefulness distributes belonging → burden self-theory, political utility and assigned service diverge from actual affection/contribution. | STRENGTHEN; `010,020,022,025,029–031`; reciprocal friendship/embrace counter exclusively transactional theory. | Refusal/failure without loss of care, meaningful alternatives; relations/normative. |
| `MT-CR-067` / `MT-C-014` | Known error alters responsibility → distinguish prompt inquiry, purposeful withholding and unrecognized received error. | REVISE; `019,021,025–026`; Eris conceals destination but is not shown knowing she caused a rejection interpretation. | Actual knowledge/opportunity before blame; knowledge/normative/form. |

Strong bounded inference applies to the specified contrasts; reports remain reports. No new numbered claim is needed: these disclosures refine existing responsibilities. The V06 checkpoint adds a focused dependency review, preserving the V01–V05 checkpoint and all historical formulations. No registered outcome prediction or clean holdout is claimed.
