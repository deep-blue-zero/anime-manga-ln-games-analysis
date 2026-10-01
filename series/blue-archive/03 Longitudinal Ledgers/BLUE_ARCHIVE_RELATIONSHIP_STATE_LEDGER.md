---
series: BLUE_ARCHIVE
artifact_type: ledger
scope: RELATIONSHIP_STATE
generation: V1
status: active_provisional
checkpoint_boundary: MAIN_V001_C003 checkpoint canonical; latest forward MAIN_S2_V003_C001 checkpoint canonical
source_boundary: "All 480 canonical main units through BA:main:series2:003:001:014 plus BA:main:001:003:043 backfill at audited electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; no unopened main unit in pinned snapshot; 100 supplemental objects admitted with limits in cycles001–003; other supplemental sources unadmitted"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-10-01
---

# BLUE ARCHIVE RELATIONSHIP STATE LEDGER

Track only relationships or ensembles with actual narrative state. Co-occurrence is not sufficient.

## Current boundary

All **480 / 480** canonical main units inventoried in the [2026-09-28 source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) at `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8` now have admitted readings. Earlier completed readings retain their declared V1 witness; this reconciliation does not substitute source text. The final backfill reading is `MAIN_V001_C003 E043` / `BA:main:001:003:043`, governed by the [V001 C003 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C003_CHECKPOINT.md). The latest forward released unit in this pinned snapshot remains `MAIN_S2_V003_C001 E014` / `BA:main:series2:003:001:014`, governed by the [S2 V003 C001 checkpoint](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_003/BLUE_ARCHIVE_MAIN_S2_V003_C001_CHECKPOINT.md). No unopened main unit remains in the pinned snapshot; extending it requires a release and provenance recheck.

Cycles001–003 admit exactly **100 supplemental objects with limits:43 group,26 event,13 bond,13 MomoTalk and5 character_data**. [Cycle003](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_003_CHECKPOINT.md) and the exact object crosswalk own admission. Current combined coverage is **23 PARTIAL_MODEL /394 UNMODELED /417 analytical subjects**, every standalone model NONE. Unadmitted sources, performed voice and main chronology retain their existing boundaries.

## Historical baselines and sequential deltas

The initial tables and observations below preserve their Prologue and early Abydos evidence boundaries. All ensuing unit and checkpoint entries retain the knowledge available at their stated reading position, including their uses of “current,” “now,” “unopened,” provisional identities and unresolved questions. These historical states are not a consolidated 480-unit endpoint; consult the relevant later deltas and chapter checkpoints for subsequent developments. Historical source witnesses and denominators remain unchanged.

| Relationship / ensemble | Current state | Last material transition | Confidence | Evidence |
|---|---|---|---|---|
| SENSEI ↔ RIN | reciprocal administrative partnership / provisional institutional trust | Rin entrusts Sensei with a device the GSC cannot operate; Sensei repairs the authorization failure and returns control to Rin's institution | high for functional relationship | E001 `scene:002-003`; E002 `scene:004`, `scene:006` |
| SENSEI ↔ ARONA | playful/supportive partnership now normalized into ordinary Schale work | Prologue system partnership → Arona triages an incoming request → Sensei decides to travel → Arona joins; both are implicated in the resulting navigation failure | high for current working relationship | Prologue E002 `scene:006`; V001 C001 E001 `scene:001` |
| SENSEI ↔ WAKAMO | asymmetrical and unresolved first-contact disturbance | Wakamo abruptly loses composure and retreats; later remains privately preoccupied while Sensei shows no comparable investment | medium for asymmetry; motive open | E002 `scene:003`, `scene:006` |
| SENSEI ↔ INITIAL STUDENT REPRESENTATIVES | role recognition → competence trust → future-access network | after the operation, Hasumi/Chinatsu/Yuuka invite Sensei into Trinity/Gehenna/Millennium contexts | high | Prologue E001 `scene:004-005`; E002 `scene:006` |
| SENSEI ↔ AYANE / ABYDOS COUNTERMEASURES COMMITTEE | petition → operational partnership → disclosure/solidarity → ordinary governance with student veto → crisis-specific delegated command → student-led investigation/ethics → independently competent emergency response | E018 has no Sensei presence: Ayane/Shiroko/Nonomi/Serika detect, classify, reason about, and respond to the restaurant explosion on their own, further separating student competence from adult replacement | high for structural ensemble; adult knowledge of E018 event not shown | V001 C001 E001–E018 |
| SENSEI ↔ SHIROKO | rescue/guest-guide → reciprocal assistance → competence recognition → explicit trust advocacy → complementary emergency collaboration | E006 Shiroko uses locally grounded security/tactical knowledge around information obtained through Sensei's authority and reports tactical-system rescue status | high for observed early relationship | V001 C001 E002–E006 |
| SENSEI ↔ HOSHINO | operational/approval trust → confidence around unsolved burden → relational environment associated with greater openness, but not total disclosure | E017 Nonomi says earlier Hoshino disliked interschool involvement and has softened, `きっと先生のおかげ`; Sensei is present in the classroom while the later Black Suit layer remains outside his visible participation | medium-high for Nonomi's observed change/attribution; causal exclusivity and Sensei awareness of Black Suit OPEN | V001 C001 E003–E017 |
| SENSEI ↔ SERIKA | outsider rejection / boundary conflict → emergency protective commitment → explicit gratitude + reciprocal obligation + accepted continuity, with full trust still open | E007 Serika voluntarily thanks Sensei, calls the rescue a `借り` she will repay, says `また明日ね`, and ends with a softened `先生`; she still does not explicitly reverse `認めてない` | high for transition; mature trust category open | V001 C001 E004–E007 |
| HELMET GANG ↔ UNKNOWN ABYDOS SPONSOR | externally supplied / evaluatively subordinate proxy relation | E007 sponsor says a main battle tank had been sent and dismisses the gang as failed lower-tier delinquents; exact contractual form remains open | high for reader-level structural relation; sponsor identity unresolved | V001 C001 E007 `scene:001-002` |
| KAISER PMC DIRECTOR ↔ 便利屋68 | explicit paid commission with asymmetric/fragmented strategic knowledge and strong client-status pressure | E012 resolves the immediate client label as `カイザーPMC理事`; Aru admits she knows little about the client beyond `超大物` and accepts renewed performance obligations | high for immediate operational relation; sponsor motive/terms/larger hierarchy remain OPEN | V001 C001 E007–E012 |
| 便利屋68 ↔ HELMET GANG | violent replacement in the same Abydos contract chain | E007 contractor removes the failed gang; E008 reveals Problem Solver 68 then hires additional personnel for its own assault rather than simply inheriting a fixed force | high for organizational relation | V001 C001 E007–E008 |
| ABYDOS COUNTERMEASURES COMMITTEE ENSEMBLE | five-student revival institution with formal procedure, internal vetoes, shared debt responsibility, distributed defense/governance roles, investigative competence, ethical self-limits, and rapid emergency coordination | E018 shows decentralized crisis response without Hoshino physically present: Ayane senses/classifies, Shiroko constrains speculation, Nonomi prioritizes movement, Serika supplies local-person concern, and Ayane contacts Hoshino while deploying | high for present distributed competence | V001 C001 E002–E018 |

| SERIKA ↔ NONOMI | peer care increasingly expressed through food/material support | after Serika admits losing lunch-savings to a scam, Nonomi immediately offers to buy her lunch rather than shame her | high for E008 beat | V001 C001 E008 |
| SERIKA ↔ HARUKA | compassion/hospitality followed by asymmetric violent role conflict | E008 Serika rejects Haruka's poverty shame; E009 Haruka responds to target recognition by offering to `始末` Abydos while Serika later condemns the attackers as `恩知らず` | high for observed transition; later reconciliation status open | V001 C001 E008–E009 |
| ARU ↔ MUTSUKI / KAYOKO / HARUKA (Problem Solver 68 ensemble) | self-styled hierarchy with real loyalty/cooperation, differentiated deference, teasing/reality checks, practical care, and now a documented internal command-interpretation hazard | E018 Mutsuki normalizes friendship, Kayoko attempts containment, while Haruka literalizes Aru's identity rhetoric into demolition before Aru can affirm or correct it; loyalty and corrective mechanisms are real but not sufficient | high for E008–E018 pattern; deeper history open | V001 C001 E008–E018 |
| ABYDOS ↔ 便利屋68 | remembered hospitality + contractual hostility + repeated low-stakes social contact + growing adversarial respect + explicit instability between enemy and friend | E018 the Shiba Seki proprietor already calls PS68 Abydos's friends; Aru fears continued warmth will make everyone `仲良し`, while Mutsuki sees no problem. Haruka then destroys the shared contact zone, but Abydos has not yet identified PS68 as responsible | high for audience-visible relational softening; mutual friendship/self-recognition and post-blast status OPEN | V001 C001 E008–E018 |
| ARU ↔ ABYDOS | positive personal judgment + active contract hostility + aspirational admiration + explicit defensive denial of emerging friendship | E018 Aru reacts to being called Abydos's friend by insisting `友だちなんかじゃない`, but immediately admits Shiba Seki's warmth makes friendship feel likely; the denial therefore marks relational threat to her outlaw self-concept rather than absence of affinity | high for Aru's current perception; reciprocity from Abydos remains OPEN | V001 C001 E009–E018 |
| 便利屋68 ↔ HIRED DAY-LABOR MERCENARIES | subcontractor ↔ time-bounded wage labor | E009 mercenaries complain about negotiated-down hourly pay, reject overtime, and leave at `定時` when the day's pay ends despite Aru's order to remain | high for labor relation; individual mercenary identities unresolved | V001 C001 E009 |

| MUTSUKI ↔ SENSEI | casual cross-group social access plus hostile-side recognition of Sensei's tactical consequence | E012 Mutsuki says PS68 cannot defeat Abydos alone while `あの「シャーレ」の先生` is with them, extending E010 social familiarity into operational respect | high for observed E010–E012 relation; mechanism/affect beyond this OPEN | V001 C001 E010–E012 |
| MUTSUKI ↔ AYANE | role-partition claim versus boundary/accountability rejection | Mutsuki says personal friendliness can coexist with commissioned attacks; Ayane answers `今さら公私を区別` and refuses future casualness after the assault | high for clean core lines; exact attribution of two entrance-interruption lines quarantined | V001 C001 E010 |
| ABYDOS ↔ KAISER LOAN | recurring high-interest creditor/debtor relation now documented as financially supporting a hostile proxy immediately after an Abydos collection | E016 `集金記録` lists ¥7.88m collected at Abydos and immediately afterward a ¥5m `任務補助金` to the Kata-Kata Helmet Gang; exact banknote identity, motive, HQ command, and Kaiser PMC relation remain open | high for recorded transactions; larger hierarchy/motive OPEN | V001 C001 E010–E016 |
| HIFUMI ↔ ABYDOS COUNTERMEASURES COMMITTEE | rescue → gratitude → voluntary local guidance → evidentiary expertise → consent overextension / imposed `ファウスト` leadership → post-raid evidence cooperation → partial relational repair and future voluntary contact | E016 Nonomi apologizes for dragging Hifumi into the strange situation, Hifumi says she also had fun and hopes to meet again, Hoshino proposes a future visit, while Hifumi still rejects the `ファウスト` label and Ayane defends that present boundary | high for warmth and boundary evidence; later enjoyment does not erase earlier consent problem | V001 C001 E011–E016 |
| HIFUMI ↔ NONOMI | immediate positive shared-interest affinity | Nonomi recognizes Momo Friends and names Mister Nikolai as her favorite; Hifumi enthusiastically reciprocates and discusses the first edition of `善悪の彼方` | high for observed shared-interest beat; depth beyond this scene open | V001 C001 E011 |
| HIFUMI ↔ TRINITY | active student affiliation plus institutional reporting/reputational consciousness | E016 Hifumi plans to report the Kaiser/criminal evidence and Abydos situation to the Tea Party; Hoshino questions what such escalation would accomplish and warns that Abydos cannot control giant-school intervention | high for Hifumi's reporting intent; Tea Party prior knowledge/action remains OPEN | V001 C001 E011–E016 |
| HOSHINO ↔ HIFUMI | situational trust grounded in expertise → overextension of reciprocal obligation → symbolic responsibility assignment → affectionate post-crisis political instruction | E016 Hoshino invites future social contact, calls Hifumi `純真で良い子`, and explains why a weak school may be unable to control nominally supportive action by a giant academy; Hifumi adapts rather than rupturing the relationship | high for observed relation; no formal mentorship claim yet | V001 C001 E011–E016 |
| BLACK MARKET THUGS ↔ HIFUMI / TRINITY | predatory categorization of school affiliation as ransom value | thugs identify Hifumi as Trinity, call the school wealthy, and attempt to monetize affiliation through kidnapping and ransom | high for coercive relation; wealth superlative remains actor claim | V001 C001 E011 |
| ABYDOS ↔ BLACK MARKET | investigators/visitors → observers of parallel finance/security → direct armed antagonists of a shadow-bank institution | E014 the committee disables bank alarms, neutralizes guards, threatens staff, obtains the target records, and triggers roadblocks/Market Guard pursuit; the relationship is now overt conflict, not observation | high for E011–E014 environment; exact governance/weapon-supplier relation OPEN | V001 C001 E011–E014 |

| KAISER LOAN ↔ BLACK MARKET SHADOW BANK | recurring cash-collection apparatus ↔ shadow-finance interface now under seized-document investigation | E013 observes the monthly transfer and signed paperwork; E014 obtains the targeted `集金記録`, but the record contents/ownership/legal meaning remain unshown | high for observed transaction and document acquisition; exact provenance/use/ownership OPEN | V001 C001 E013–E014 |

| SERIKA ↔ SHIBASEKI RAMEN MASTER | employer/customer-community relation with explicit personal attachment | E018 Serika reacts to the restaurant's destruction by worrying `大将……無事でいて……！`; proprietor status remains unresolved | high for attachment; physical outcome OPEN | V001 C001 E005, E008–E018 |
| 便利屋68 ↔ SHIBASEKI RAMEN | repeated hospitality/contact-zone relation that is actively softening factional boundaries | proprietor treats PS68 as Abydos friends and offers extra noodles; Aru identifies the warmth itself as causing friendship drift; Haruka then destroys the site through misinterpreted loyalty | high for E018 social function; future rebuilding/reconciliation OPEN | V001 C001 E008–E018 |

## Explicit non-findings

- No Prologue relationship justifies a mature romance, friendship, mentorship, dependency, or rivalry synthesis yet.
- Wakamo's reaction is **not** assigned a motive from later franchise knowledge.
- Arona's emotional warmth and assistant role do not by themselves establish a parental, romantic, or metaphysical relationship category.
- Ayane/Sensei now have face-to-face functional partnership, but no mature friendship, dependency, or mentorship claim is warranted.
- Shiroko/Sensei shared-drink/carrying embarrassment does **not** by itself establish romance; the current relationship is reciprocal assistance.
- E002–E004 contain recurring speaker-label anomalies; E006 has one quarantined self-address anomaly. E008 resolves Aru/Mutsuki/Kayoko/Haruka but has two quarantined meeting mappings. E009 adds quarantined `u:0003` and impossible Aru self-address `u:0052`; `u:0032` is treated cautiously. E010 explicitly establishes the attackers as Gehenna students through Ayane's research; E008's uniform-only inference is therefore superseded by stronger local evidence.
- Hoshino/Sensei now have a functional approval/operations baseline only; do not promote `お墨付き` into mature mentorship, dependency, or parental authority.

## E015 delta — authority, prediction, admiration, and accidental transfer

- **Hoshino ↔ Shiroko:** Shiroko predicts Hoshino will oppose keeping the cash before Hoshino rules, showing a legible normative pattern rather than arbitrary authority; Shiroko obeys `委員長としての命令`.
- **Hoshino ↔ Serika:** strong substantive disagreement is resolved institutionally without requiring unanimity; Serika remains inside the committee after protesting.
- **Hoshino ↔ Nonomi:** Nonomi confirms she previously proposed the gold-card shortcut and now explains Hoshino's refusal as protecting Abydos's identity.
- **Ayane ↔ Serika:** Ayane again functions as a procedural brake, this time against converting suspected restitution into actual expropriation.
- **Aru ↔ Abydos:** familiar adversaries become anonymous aspirational icons, then the identities collapse when Aru learns `覆面水着団` was Abydos.
- **Mutsuki ↔ Aru:** Mutsuki deliberately delays truth because the misunderstanding is funny, then eventually reveals it.
- **Problem Solver 68 ↔ Abydos:** Abydos unintentionally leaves the rejected cash where PS68 finds it; this is accidental material transfer, not intentional financing or gift.
- **Hifumi ↔ Abydos:** Hifumi witnesses both the committee's transgression and its self-restraint, while explicitly retaining outsider epistemic distance.

## E016 delta — evidence, repair, and asymmetric support

- **Abydos ↔ Kaiser Loan:** documentary relationship now includes a recorded ¥5m Helmet Gang mission subsidy immediately after the Abydos collection entry.
- **Hifumi ↔ Abydos:** Nonomi apologizes for drawing Hifumi into the incident; Hifumi reports enjoyment and future willingness to meet, but continued rejection of `ファウスト` prevents retroactive consent flattening.
- **Ayane ↔ Hifumi:** Ayane explicitly stops the others when Hifumi is uncomfortable with the `ファウスト` teasing.
- **Hoshino ↔ Hifumi:** affectionate political instruction emerges around power asymmetry and support.
- **Hoshino ↔ Nonomi:** Nonomi challenges Hoshino's pessimistic risk weighting and preserves the possibility of genuine help.
- **Abydos ↔ Tea Party/Trinity:** a potential support/reporting route is introduced, but Hoshino frames it as a sovereignty problem because Abydos may lack the power to constrain a giant academy's intervention.


## E017 relationship delta

- **ARU ↔ CLIENT:** contract is intentionally designed to prevent client dependency from becoming command; advance payment is rejected because it could make refusal harder.
- **PS68 ↔ ABYDOS:** adversarial respect and tactical escalation coexist; Kayoko explicitly says Abydos cannot be underestimated and identifies low numbers as its major weakness.
- **PS68 ↔ PREFECT TEAM / HINA:** future collision is anticipated; Kayoko models Hina as the decisive force multiplier and a Hina-less team as manageable with planning. This is Kayoko's assessment, not direct Hina evidence.
- **HOSHINO ↔ NONOMI:** physical comfort, trust, and historical witnessing deepen; Nonomi can describe how Hoshino changed over time.
- **NONOMI ↔ SENSEI:** warm public familiarity adds a private `今度、誰もいない時に` teasing register; romance remains OPEN.
- **HOSHINO ↔ BLACK SUIT:** preexisting relationship becomes explicit through `今度は` / `再度`; earlier offer was unwelcome, and the renewed offer is framed as one Hoshino cannot refuse.
- **HOSHINO ↔ COMMITTEE:** distributed ordinary governance permits Hoshino to rest, but Black Suit reveals a burden he has not yet been shown sharing.

## E018 relationship delta — friend/enemy instability and destroyed contact zone

- **PS68 ↔ Abydos:** external recognition and Aru's own fear confirm that ordinary contact is eroding pure-enemy categorization before either side formally reconciles.
- **Aru ↔ Haruka:** extreme loyalty now has a concrete failure mode: inferred ideological need becomes action without explicit confirmation.
- **Aru ↔ Mutsuki:** Mutsuki can tolerate friendship/role contradiction that Aru experiences as identity threat.
- **Aru ↔ Kayoko:** containment remains real but is too slow to prevent the act.
- **Serika ↔ Shiba Seki proprietor:** personal attachment is explicit.
- **PS68 ↔ Shiba Seki:** the restaurant is a shared social bridge; its destruction removes the very space producing relational de-escalation.
- **Abydos ↔ perpetrators:** no character-level perpetrator identification yet; preserve audience/character epistemic split until E019.

## E019 delta — contact-zone collapse, persona pressure, and new armed relation

- **Abydos ↔ PS68:** E018's unstable enemy/friend contact becomes direct morally charged hostility after Abydos finds PS68 at the ruins and Aru claims villain responsibility.
- **Aru ↔ Mutsuki:** Mutsuki's fluent knowledge of Aru's persona becomes pressure to perform the identity she praises.
- **Aru ↔ Haruka:** the command-interpretation failure remains unrepaired; Haruka continues extreme service while Aru adopts the result rather than clarifying it.
- **Serika ↔ Shiba Seki proprietor:** proprietor survives with light injuries; Serika's relational anger persists despite favorable casualty outcome.
- **Prefect Team ↔ PS68:** direct formal armed intervention begins through mortar fire; motive/jurisdiction remain OPEN.


## E020 delta — jurisdictional protection, cross-school trust, and internal accountability

- **SENSEI ↔ CHINATSU:** Prologue relation reactivates explicitly through `久しぶり`; Chinatsu's prior experience has matured into strong operational trust/reputation—once she recognizes Sensei, she says withdrawal should have followed immediately.
- **SENSEI ↔ ABYDOS:** E020 strengthens autonomy-enabling partnership. Sensei raises the hand-over option, but Shiroko/Ayane make and justify the sovereignty decision; Sensei's practical value makes their refusal enforceable without appropriating their decision-right.
- **ABYDOS ↔ 便利屋68:** relationship becomes `third-party protection without forgiveness`: Abydos refuses Gehenna seizure while still insisting PS68 must answer locally for Shiba Seki and unresolved sponsor questions.
- **ABYDOS ↔ GEHENNA PREFECT TEAM:** first direct relation is armed extraterritorial conflict; after Prefect defeat, Ayane pushes the interaction back toward formal identification/dialogue. Long-term settlement remains OPEN.
- **IORI ↔ CHINATSU:** internal Prefect Team differentiation becomes explicit: Iori privileges mission execution/force while Chinatsu repeatedly raises explanation, situational caution, civilian risk, and Schale recognition.
- **IORI ↔ AKO:** Ako's remote entrance immediately changes Iori's posture; the reflection-letter remark establishes accountability/supervision without yet revealing the exact command fault.
- **KAYOKO ↔ PREFECT TEAM:** `うちの風紀` confirms shared academy familiarity; depth/history beyond recognition remains OPEN.

## Chapter 1 checkpoint reconciliation - `MAIN_V001_C001`

Canonical chapter synthesis authority is `BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md`. Use that checkpoint for the reconciled E001-E020 chapter state while retaining this ledger's unit-local deltas for longitudinal evidence and revision history. Chapter 2 must inherit the checkpoint epistemic firewalls, especially the unresolved Hoshino/Black Suit causation, Kaiser hierarchy, Haruka/Aru responsibility distinction, and Gehenna order-chain questions.

## C002 E001 relationship delta — alliance without absolution

- **Abydos ↔ Problem Solver 68:** the sides form an unexpected defensive alliance against forced seizure. Abydos protection does not erase PS68 responsibility for Shiba Seki or settle the sponsor question; alliance is jurisdictional and tactical, not absolution.
- **Sensei ↔ Problem Solver 68:** Aru explicitly makes defense of Sensei reciprocal repayment for Abydos's trust, materially strengthening the emergent relation without resolving her lie about the explosion.
- **Sensei ↔ Abydos:** the committee asks Sensei to command a coalition it chose to form. Entrusted tactical authority remains downstream of student-authored policy.
- **Ako ↔ Hina:** subordinate initiative becomes concealed initiative. Ako expects discipline if Hina learns of the operation and lies about her location when Hina calls; Hina immediately presses the unauthorized cross-district deployment.
- **Ako ↔ Kayoko:** Kayoko reads Ako's conduct as an institutional pattern and correctly identifies Schale as the operation's real objective, though Ako says Kayoko's staging hypothesis is only half-right.
- **Gehenna Prefect Team ↔ Abydos/PS68:** the relation expands from disputed arrest to a coalition defense against custody of Sensei; formal purpose no longer maps cleanly onto the force actually deployed.
- **Gehenna ↔ Trinity:** a prospective treaty is introduced as Ako's strategic horizon. Its terms, status, and Tea Party knowledge remain OPEN.

## C002 E002 relationship delta — apology, warning, and unresolved history

- **Hina ↔ Ako:** becomes accountable hierarchy: Hina names the scope violation, suspends Ako, and defers the full explanation until return.
- **Hina ↔ Abydos:** moves from inherited armed conflict to formal apology, non-incursion promise, and voluntary withdrawal. This is prospective restraint, not established trust or total exoneration.
- **Hina ↔ Hoshino:** a prior asymmetrical knowledge relation opens; Hina remembers first-year Hoshino and an unspecified incident, while Hoshino appears not to recognize the connection.
- **Hina ↔ Sensei:** begins through discretionary warning rather than custody. Hina transfers sensitive Kaiser information without claiming the response.
- **Sensei ↔ Abydos:** Sensei promises Shiroko to disclose the warning to everyone later, reinforcing transparency toward the group.
- **Abydos ↔ PS68:** PS68 escapes during the transition. The tactical alliance ends without adjudicating responsibility, sponsor, or friendship.

## C002 E003 relationship delta — farewell without severance

- **Abydos ↔ PS68:** direct hostility becomes nonaggression, material reparation, and possible future return; no full-group reconciliation or responsibility adjudication occurs.
- **Sensei ↔ PS68:** a failed enemy contract is separated from future friendship/partnership. Sensei neither detains nor condemns the departing group.
- **Aru ↔ Haruka:** Haruka's perceived life debt becomes explicit, deepening care while leaving dangerous command interpretation unrepaired.
- **PS68 ↔ Shiba Seki:** all remaining bag money is left for repair, and future ramen return preserves relation beyond the destroyed site.
- **Serika ↔ proprietor:** threatened closure reveals that employment is secondary to community attachment and concern for his continued presence.

## C002 E004 relationship delta — shared fate, privacy, and mistrust

- **Shiroko ↔ Hoshino:** moves to direct mistrust; Shiroko calls the sleep account a lie and requests privacy, while Hoshino deflects without resolving the suspicion.
- **Nonomi ↔ Shiroko/Hoshino:** Nonomi first rejects a hidden dyad in a `運命共同体`, then recognizes personal limits on forced disclosure. Mediation preserves concern without extracting a confession.
- **Sensei ↔ committee:** Nonomi explicitly asks Sensei to remain amid multiplying threats; both response variants affirm presence rather than promised victory.
- **Committee ensemble:** the cadastral reveal supplies shared institutional knowledge after a scene defined by uneven personal knowledge, sharpening the difference between governable facts and protected interiority.

## C002 E005 relationship delta — affirmation beside surveillance

- **Shiroko ↔ Hoshino:** public respect and private mistrust coexist: Shiroko praises Hoshino's decisive care while secretly holding a withdrawal form obtained from her bag.
- **Sensei ↔ Shiroko:** opens a confidential evidence relationship grounded in admitted wrongdoing and uncertainty; temporary secrecy creates a future clarification obligation.
- **Sensei ↔ committee:** Sensei completes promised disclosure of Hina's warning, and the committee collectively chooses investigation.
- **Hoshino ↔ former president:** a two-person final council is revealed; Hoshino's mocking description carries unresolved attachment, ignorance, and burden.
- **Current committee ↔ former council:** victim-blaming gives way to a constrained-choice interpretation without erasing consequences of the sales.

## C002 E006 relationship delta — epistemic reassurance

- **Shiroko ↔ Ayane:** Shiroko preserves Ayane's justified agency while accepting that new title evidence can revise the earlier premise.
- **Abydos ↔ Gehenna Prefect Team:** the committee now suspects Gehenna knew boundary facts it did not; information asymmetry explains wording without repairing trust or legitimizing Ako.
- **Committee ensemble:** Serika questions, Ayane reconstructs, Shiroko adjudicates conduct, and Hoshino returns the group to verification—distributed reasoning rather than one authoritative voice.

## C002 E007 relationship delta — elder memory within a new generation

- **Hoshino ↔ committee:** Hoshino mediates inherited desert/civic memory to members who have never visited; the knowledge gap deepens her elder role without resolving her secrecy.
- **Abydos ↔ other academies:** historical sand-festival visitors establish a former cross-school social relation now preserved mainly as story.
- No new Sensei or withdrawal-form relationship state is supplied.

## C002 E008 relationship delta — residents recast as intruders

- **Abydos ↔ facility security:** first contact is an unannounced capture attack; guards call the local expedition `侵入者` on land once governed by Abydos.
- **Committee ensemble:** Ayane detects/classifies and Hoshino authorizes defense; no internal disagreement is shown.
- Affiliation and longer-term relationship remain OPEN.

## C002 E009 relationship delta — bounded command under corporate encirclement

- **Abydos ↔ Kaiser PMC:** affiliation is confirmed and the relation becomes combined-arms encirclement; professionalism does not create consent or legitimacy.
- **Ayane ↔ Sensei:** Ayane retains threat judgment/withdrawal policy and requests Sensei's tactical instructions, preserving delegated rather than substitutive authority.
- No withdrawal-form relational change occurs.

## C002 E010 relationship delta — proxy employer and targeted debtor

- **Kaiser director ↔ Hoshino:** he knows her office, debt succession, and Gematria interest, turning private history into direct leverage.
- **Kaiser director ↔ PS68/Helmet Gang:** direct hiring admission establishes the common client behind both proxy pressures.
- **Kaiser director ↔ Gematria:** knowledge that Gematria targeted Hoshino is explicit; affiliation/command remains OPEN.
- **Sensei ↔ committee:** bounded command support fails to secure escape under comms degradation; no blame or relational rupture is shown.

## C002 E011 relationship delta — coerced exit and institutional belonging

- **Kaiser director ↔ Abydos:** creditor relation becomes explicit domination; he manufactures repayment impossibility and offers abandonment as release.
- **Students ↔ Abydos:** Nonomi/Serika/Shiroko reaffirm school/city belonging precisely when personal exit is offered.
- **Hoshino ↔ committee:** Hoshino ends a futile exchange and protects the group from further manipulation, while her withdrawal-form contradiction remains hidden.
- **Hina ↔ Hoshino:** Hina's relation is intelligence-based rather than prior personal meeting; present curiosity about why Hoshino stayed remains private.
- **Director ↔ former president/Hoshino:** prior observation/acquaintance is established; exact history remains open.

## C002 E012 relationship delta — care, secrecy, and sacrificial recruitment

- **HOSHINO ↔ FORMER PRESIDENT:** remembered predecessor/successor conflict centers on miracle, realism, and office responsibility; affection, identity, and fate remain incompletely specified.
- **HOSHINO ↔ COUNTERMEASURES COMMITTEE:** present people make the damaged school lovable, but Hoshino withholds a sacrifice plan, promises disclosure, then leaves governing information behind.
- **SENSEI ↔ HOSHINO:** private confrontation secures material disclosure and an adult promise, while compromised evidence, narrowed refusal, and the subsequent departure complicate agency-preserving care.
- **SHIROKO ↔ HOSHINO:** trust and alarm coexist; Shiroko seeks conversation but previously searched Hoshino's bag without consent.
- **BLACK SUIT ↔ HOSHINO:** repeated recruitment over two years culminates in debt relief conditioned on exit and employment; no signed acceptance or exact hierarchy is established.
- **BLACK SUIT ↔ KAISER DIRECTOR:** Hoshino says the director appeared afraid of Black Suit; apparent leverage is established as observation, not a formal org relation.

## C002 E013 relationship delta — completed transaction, replicated sacrifice

- **HOSHINO ↔ BLACK SUIT:** proposal becomes signed transaction and transport; Black Suit claims personal receipt of Hoshino's student rights, while validity and hierarchy remain OPEN.
- **HOSHINO ↔ SENSEI:** prior adult distrust becomes explicit trust sufficient to entrust Shiroko's support; this is relational confidence, not transferred ownership of Shiroko.
- **HOSHINO ↔ SHIROKO:** protective concern is mirrored by Shiroko's one-person rescue impulse, revealing reciprocal care and shared self-sacrificial risk.
- **AYANE ↔ SHIROKO / COMMITTEE:** Ayane interrupts solo action and makes coordinated response the condition of rescue/defense.
- **KAISER ↔ ABYDOS COMMUNITY:** the relation becomes overt invasion, indiscriminate city attack, eviction, school occupation, and announced corporate absorption.
- **COMMITTEE ↔ ABYDOS CIVILIANS:** civilian evacuation becomes an explicit governing/protective obligation.

## C002 E014 relationship delta — differentiated conspirators and chosen allies

- **BLACK SUIT ↔ KAISER:** affiliation is rejected; the relationship is interest-aligned cooperation between differentiated actors.
- **BLACK SUIT ↔ HOSHINO:** apparent employment bargain is exposed as acquisition for research/analysis; Hoshino recognizes adult deception.
- **PS68 ↔ ABYDOS:** former opponents/repairing acquaintances become voluntary defensive allies when Hoshino and the school are endangered.
- **ARU ↔ SENSEI:** Aru initiates `協業` and treats Sensei as a partner who can align with her plan.
- **KAYOKO ↔ AYANE/COMMITTEE:** hard-nosed acknowledgment of despair is paired with practical restoration of action.
- **HOSHINO ↔ YUME:** Yume-senpai is named in Hoshino's guilt sequence; identification with the former president remains strong inference, not yet closed fact.
- **ABYDOS ↔ GENERAL STUDENT COUNCIL / OTHER SCHOOLS:** prior petitions/nonintervention define institutional abandonment, while PS68 immediately disproves universal relational abandonment.

## C002 E015 relationship delta — client refusal and protective standing

- **PS68 ↔ KAISER DIRECTOR:** former employment is rejected as ownership; betrayal is embraced as autonomous outlaw choice.
- **ARU ↔ SENSEI:** ease of working together becomes Aru's explicit reason for present alignment.
- **SENSEI ↔ HOSHINO:** `my precious student` and a return demand assert protection against capture; wording remains subject to the nonpossession test.
- **ABYDOS ↔ PS68:** coalition produces a bounded tactical victory and restores rescue planning without resolving prior harms into perfect friendship.
- **AYANE ↔ COMMITTEE:** despair yields to coordinated regrouping rather than impulsive pursuit.
- **SENSEI ↔ BLACK SUIT:** first direct face-to-face encounter begins at an unspecified location; terms and power balance remain OPEN.

## C002 E016 relationship delta — co-option refused, responsibility chosen

- **SENSEI ↔ GEMATRIA/BLACK SUIT:** direct negotiation becomes explicit ideological opposition after two cooperation refusals and rejection of Hoshino-for-school exchange.
- **SENSEI ↔ HOSHINO:** unsigned advisor consent preserves a procedural/relational claim; rescue aims at return and accountability rather than rights transfer.
- **SENSEI ↔ COMMITTEE:** Sensei returns with actionable intelligence and a coalition idea; students welcome, interpret, and plan rather than receive a completed adult solution.
- **BLACK SUIT ↔ HOSHINO:** research-object relation is specified through mystic/fear experimentation at the desert lab.
- **BLACK SUIT/GEMATRIA ↔ KAISER:** separate actors remain; Gematria claims it can resolve PMC, suggesting leverage without collapsing hierarchy.
- **COMMITTEE ↔ HOSHINO:** anticipated `welcome home`, scolding, and reply make restored accountable membership the rescue goal.

## C002 E017 relationship delta — plural aid and compromised access

- **SENSEI ↔ IORI:** Sensei complies with a humiliating foot-contact taunt to obtain access; comic framing does not erase adult/student boundary and consent concerns.
- **SENSEI ↔ HINA:** Hina interprets the approach as self-abasement for students, asks the need, and later supplies bounded reinforcement interdiction.
- **HIFUMI ↔ NAGISA:** Hifumi's report activates trust/affection and delegated support; Nagisa also anticipates reciprocal love and strategic debt.
- **SHIBA SEKI ↔ PS68:** repair money, a request to continue, shared meal, and reopened stall turn incomplete reparation into renewed community practice.
- **PS68 ↔ ABYDOS:** gratitude and hospitality deepen voluntary aid, while Aru's persona capture prevents a simple free-choice account.
- **ABYDOS ↔ EXTERNAL COALITION:** Abydos retains mission/route authorship while supporters provide interdiction, heavy support, force, and intelligence channels.

## C002 E018 relationship delta — enabling fire and promised return

- **HIFUMI/TRINITY SUPPORT ↔ ABYDOS:** indirect heavy fire creates a corridor; Abydos chooses and commands the follow-through.
- **PS68 ↔ ABYDOS:** voluntary rearguard action replaces Shiroko's emerging solo sacrifice; gratitude becomes a future ramen promise.
- **ARU ↔ PS68 PERSONA:** public heroic commitment again captures private fear and makes reconsideration difficult.
- **KAYOKO/MUTSUKI/HARUKA ↔ ARU:** group responses reinforce the commitment rather than reopening consent, even while sustaining collective courage.
- **ABYDOS ↔ ORIGINAL SCHOOL:** present students physically reach the buried institutional center for the first time in this reading sequence.
- **GEMATRIA ↔ KAISER / SITE:** Gematria requested the lab; Kaiser concentrates force around it, preserving cooperation without organizational merger.

## C002 E019 relationship delta — reciprocal homecoming

- **COMMITTEE ↔ HOSHINO:** collective rescue culminates in welcome/reply; belonging is reciprocally spoken rather than imposed.
- **SENSEI ↔ HOSHINO:** Sensei's address is part of the recognition sequence, but students remain coequal causal/relational rescuers.
- **HOSHINO ↔ UNNAMED SENIOR:** remembered senior values ordinary daily presence and anticipates Hoshino's future juniors; Yume/former-president identity remains inferential.
- **SCHale ↔ ABYDOS:** helicopter/logistical support enables extraction without replacing student breach and reunion.
- **KAISER DIRECTOR ↔ COMMITTEE:** the director admits deliberate punishment/morale-breaking and resentment of their joy; students explicitly refuse psychic defeat.
- **COALITION ↔ RESCUE:** external holding/support is converted into actual passage, while supporter outcomes remain unreported.

## C002 E020 relationship delta — recognition without takeover

- **SENSEI ↔ COUNTERMEASURES COMMITTEE:** public certification repairs formal vulnerability; continuing support is requested without Sensei occupying student office.
- **HOSHINO ↔ COMMITTEE:** Hoshino's presidency refusal is honored while membership, correction, and ordinary affection resume.
- **SHIBA SEKI ↔ ABYDOS/PS68:** repaired contact survives as a reopened stall, renewed customers, and Serika's employment.
- **ABYDOS ↔ KAISER CORPORATION:** immediate attack recedes, but debt and majority land ownership preserve structural antagonism.
- **KAISER CORPORATION ↔ DIRECTOR:** corporation dismisses him to deny connection; prior multi-entity leadership evidence remains.
- **COMMITTEE ↔ BLACK SUIT/SCHALE:** Sensei/Hoshino information becomes shared research, then unresolved investigation is entrusted to Schale.

## MAIN V001 C002 checkpoint relationship state

- **Sensei ↔ Hoshino/Abydos:** protection becomes legitimate where it restores reciprocal membership and self-government; privacy, veto, possession language, and bodily boundaries remain accountability tests.
- **Black Suit ↔ Kaiser:** interest-aligned cooperation is canonical; membership/common organization is rejected.
- **Abydos ↔ PS68:** conflict matures through imperfect reparation, hospitality, voluntary aid, gratitude, and projected future contact.
- **Abydos ↔ external coalition:** differentiated support opens routes while local mission authorship remains with the committee.
- **Hoshino ↔ Yume/former president:** one strongly continuous relational hypothesis remains unpromoted until the source explicitly joins name and office.

## V002 C001 E001 relationship delta — petition, sibling correction, incomplete dispute

- **GAME DEVELOPMENT CLUB ↔ SENSEI/SCHALE:** the club sends an urgent, game-framed request; Sensei arrives, but help is not yet specified or delivered. Petition does not imply agreement with every proposed action.
- **MOMOI ↔ MIDORI:** sibling correction, teasing, apology, and shared asset concern coexist in the injury exchange; their complementary creative jobs are directly stated. Do not turn one comic exchange into a stable antagonism or care hierarchy.
- **MOMOI/MIDORI ↔ YUZU:** Yuzu is named as absent president/planner, not observed interacting; no dyadic rule is licensed.
- **CLUB ↔ STUDENT COUNCIL/YUUKA:** abolition ultimatum and earlier `襲撃` are presently Momoi's report. Yuuka's answer and the council's rationale are pending.
- **ARONA ↔ SENSEI:** request is read and institutional context supplied; Sensei's prior Millennium knowledge is choice-variable.

## V002 C001 E002 relationship delta — contested standing, conditional time

- **YUUKA ↔ GAME DEVELOPMENT CLUB:** not simple persecution or reconciliation. Yuuka articulates resource/result conditions and harsh criticism, then grants a two-week prize-linked extension. Club survival and the quality of her treatment must be judged separately.
- **MOMOI ↔ MIDORI:** Midori proposes a lower-odds comparison and corrects Momoi's blame claim while remaining loyal to the club. The sister relationship accommodates disagreement without rupture.
- **YUUKA ↔ SENSEI:** mutual recognition and Yuuka's later embarrassment are visible; prior relationship and the meaning of her wish for a calmer next meeting remain OPEN.
- **MOMOI ↔ SENSEI:** a request for help becomes designation as `切り札` before full danger/access rationale is offered. Sensei asks questions; informed assent is not yet shown.

## V002 C001 E003 relationship delta — disagreement within shared search

- **MOMOI ↔ MIDORI:** Midori's challenge becomes more precise (Himari's hedge versus coordinate evidence), while Momoi supplies a substantive reason and both remain in the same expedition. Differing confidence does not equal broken solidarity.
- **MOMOI/MIDORI ↔ SENSEI:** Momoi directs hiding and accepts Sensei's factory cue; Midori requests combat command only when encirclement emerges. The teacher is an invited participant/possible tactical coordinator, not yet owner of their creative mission.
- **CLUB ↔ VERITAS/HIMARI:** coordinates/help and metaphor are reported by Momoi, not directly spoken by Veritas or Himari; no lasting alliance terms are established.
- **GROUP ↔ ROBOTS:** observed patrol/convergence creates an immediate adversarial practical relation, but robot intent, command, and identity are unknown.
## V002 C001 E004 relationship delta — rescue before belonging

- **MOMOI/MIDORI ↔ SENSEI:** Sensei's body buffers their fall, and Midori thanks them; the facility grants the sisters derivative access as Sensei's `生徒`. That automated classification does not settle prior consent, school registration, or personal obligation.
- **SISTERS ↔ ALICE:** clothing and removal from the robot site are concrete care. Naming is tentatively affirmed; Momoi's subsequent recruitment invitation has no shown informed acceptance. Dependent stranger and potential club resource are simultaneous, ethically unsettled relations.
- **MOMOI ↔ MIDORI:** they disagree about the newcomer and the proposed false-student route while preserving shared rescue. Corrupt labels prevent precise allocation of every club-room argument.
- **GROUP ↔ FACTORY/ROBOTS:** robots stop pursuing at its threshold; the gate recognizes Sensei and derives companions' access. No builder, ownership, allegiance, or motive is established.

## V002 C001 E005 relationship delta — critique, teaching, recognition

- **MOMOI ↔ MIDORI:** the sisters disagree about Alice's false-member plan and game quality yet cooperate under a shared concern for Yuzu's club refuge. Midori's participation is not settled agreement with the means.
- **CLUB ↔ ALICE:** Alice agrees to play, receives guidance, persists through punishing design and gives a positive, tearful response. No informed consent to official club membership or identity work is shown.
- **YUZU ↔ ALICE:** Yuzu's first direct contact is grateful recognition of the player's words/tears, after hidden observation. This does not reveal why Yuzu hid or establish a prior relationship.
- **MOMOI/MIDORI ↔ YUZU:** Momoi reports club-loss housing stakes; Yuzu independently shows longing for positive game reception. Neither fact alone certifies the other or supplies Yuzu's full private situation.

## V002 C001 E006 relationship delta — chosen company, manufactured legibility

- **YUZU ↔ ALICE:** Yuzu welcomes her and offers games; Alice tries an RPG party-join reply and asks if it fits. This is reciprocal contact with correction, not merely technical training.
- **CLUB ↔ ALICE:** Alice anticipates continued play and declares herself a joining `仲間` after receiving an ID. Her voiced belonging is real within the scene, but does not establish knowledge of the card's altered provenance or formal club admission.
- **MOMOI ↔ MIDORI:** Momoi calls game-derived speech refined and proceeds to weapon planning; Midori says it remains skewed. Their differing evaluation continues within cooperation.
- **CLUB ↔ VERITAS:** Momoi reports Veritas roster work in a self-corrected hacking phrase; no Veritas member appears or confirms the relationship.

## V002 C001 E007 relationship delta — preference, gift, test

- **ALICE ↔ ENGINEERING CLUB:** Alice chooses a named railgun against initial practical advice. Utaha honors the choice after a lift/discharge and late combat test, while Kotori voices budget objection and Hibiki offers safer alternatives/adaptation. This is conditional institutional inclusion, not unqualified acceptance.
- **GAME DEVELOPMENT CLUB ↔ ENGINEERING CLUB:** Momoi requests a weapon, Utaha offers prototypes, then changes the terms for the expensive one. The unit ends with a gift, not an enduring alliance or proof the damaged ceiling is repaired.
- **MOMOI/MIDORI ↔ ALICE:** the sisters witness capability beyond their assumptions; Momoi presses the gift and Midori asks whether Utaha really permits the transfer. Alice's chosen weapon remains distinct from the sisters' initial plan to equip her.
- **UTAHA/HIBIKI/KOTORI:** the engineering trio differs in decision roles—Utaha decides, Hibiki designs/records, Kotori explains and protests cost.

## V002 C001 E008 relationship delta — a recruit speaks under club pressure

- **YUUKA ↔ GAME DEVELOPMENT CLUB:** Yuuka follows the reported fourth-member claim with a visit rather than automatically accepting or rejecting it. She says membership counts if Alice came by her own will; Momoi argues headcount. Procedure and adversarial affect coexist, and no ruling occurs here.
- **ALICE ↔ CLUB:** Alice rehearses a plausible school/programmer story for a review whose stakes Momoi and Midori understand. She previously voiced `仲間`, but this scene does not show full knowledge of registration provenance or that she can refuse without losing support; do not collapse script performance into informed agreement.
- **MOMOI ↔ MIDORI:** Momoi treats safety as achieved and diverts toward raid play; Midori insists the pending review may decide club survival. Their difference is about risk appraisal within a shared protective goal, not evidence of disloyalty.
- **ALICE ↔ YUUKA:** first direct contact includes Alice's `妖怪` insult, Momoi's attempted `妖精` repair and Yuuka's irritation. Yuuka nevertheless addresses Alice and announces questions; no settled personal antagonism or acceptance is established.

## V002 C001 E009 relationship delta — conditional approval, shared responsibility

- **YUUKA ↔ ALICE:** Yuuka notices suspicious identity/work answers and Momoi's stare, yet treats Alice's game interest as genuine enough for club belonging. This is a bounded acceptance, not a trusted biography or proof of uncoerced status enrollment.
- **YUUKA ↔ GAME DEVELOPMENT CLUB:** actual formal recognition, budget and room use are granted through this term; Yuuka also holds the club to results by month-end and cites a missed heads' meeting. The relationship is neither pure persecution nor unconditional rescue.
- **MOMOI/MIDORI ↔ ALICE:** Momoi displays the card and appears to pressure Alice during questioning; Midori fears exposure. Their care and club-survival incentive remain interwoven, while Alice's game delight is not reducible to the manufactured record.
- **YUZU ↔ CLUB/ALICE:** Yuzu apologizes, offers to join the risk and says she wants to protect a room shared with the others. Alice celebrates her party entry. This gives Yuzu an independent direct commitment, not just Momoi's prior report of her need for a refuge.
- **MOMOI ↔ YUZU/MIDORI:** exact allocation of blame in `u:0082-0090` is corrupt. Secure lines establish Yuzu's apology/offer and the group's final collective commitment, not which sister missed a substitute meeting due to a drop-rate event.

## V002 C001 E010 relationship delta — chosen exposure and requested command

- **YUZU ↔ CLUB:** Yuzu's E009 offer becomes observed presence in the ruins; she checks the group, notices robots and calls Alice to act. The tactical retreat/push dispute is label-corrupt, so a Yuzu-specific reversal or command cannot be asserted.
- **ALICE ↔ SENSEI:** Alice directly promises protection and asks whether Sensei will trust and accompany her. Sensei affirmatively accepts in either variant, and Alice celebrates their party bond. The promise's fulfillment and full risk disclosure remain untested.
- **MIDORI ↔ SENSEI:** Midori voices the teacher's distinctive vulnerability and only then requests tactical command. Care and functional delegation are not contradictory; neither makes Sensei sovereign over the club's aim.
- **MOMOI ↔ SENSEI:** Momoi warns the teacher to duck before the explosion; the teacher reports being okay. A concrete protective action, not a global relationship rule.
- **GROUP ↔ ROBOTS/FACTORY:** first strike succeeds by group appraisal, a second wave approaches, and a disputed rationale favors breaking through. The exact tactic author, robot command, factory/G.Bible connection and result remain OPEN.

## V002 C001 E011 relationship delta — recognized stranger and protective retreat

- **ALICE ↔ TERMINAL/SYSTEM:** the interface calls her `AL-1S`, claims voice-confirmed eligibility and says welcome back; Alice asks whether it knows her. This is a direct institutional-machine encounter, not proof of benevolent relation, original identity or equal personhood with the system.
- **ALICE ↔ CLUB:** her felt familiarity and the terminal's recognition are witnessed amid the club's prize-object search. Momoi continues the transfer; Alice's own identity question receives no answer. The club's instrumental aim and duty to attend to her self-knowledge remain in tension.
- **MOMOI ↔ CLUB/ALICE/YUZU/SENSEI:** Momoi offers a card, protests save deletion, secures the data carrier and allocates Yuzu to protect Sensei while she and Alice cover the rear. Her extraction plan values both the claimed prize file and group survival; completion is unobserved.
- **YUZU ↔ ALICE/SENSEI:** Yuzu asks if `AL-1S` is Alice, connects the cable, and is assigned to protect Sensei. A mislabeled reply at `u:0047` cannot prove exactly when or how Yuzu was told the body-mark story.
- **GROUP ↔ ROBOTS:** a robot appears, emits opaque speech and fires after a loud moment; why it arrived and whether it is angry are unverified. Escape has begun, not concluded.

## V002 C001 E012 relationship delta — people before prize, contested coalition

- **MOMOI ↔ MIDORI/ALICE/YUZU:** Momoi explicitly prioritizes their safety over even the club's survival when C&C security is disclosed. Midori's shared-place appeal changes the decision conditions, and Momoi joins a limited retrieval plan. This is negotiation, not proof risk was removed.
- **MIDORI ↔ CLUB/ALICE/YUZU:** Midori names the room as a place for everyone together, giving Alice and Yuzu explicit standing in her reason to act. This broadens her earlier concern beyond output metrics.
- **ALICE ↔ PARTY:** Alice offers companionship as the strongest RPG power and supports the alliance. The analogy expresses an attachment; it does not demonstrate tactical sufficiency or solve her `AL-1S` history.
- **VERITAS ↔ GAME DEVELOPMENT DEPARTMENT:** shared need for Mirror creates a coalition, but Veritas seeks return of its confiscated tool and the club seeks file access. Goals overlap without being identical or lawful by default.
- **YUUKA ↔ AKANE/C&C:** Yuuka commissions store protection on a tip she attributes to Himari; Akane accepts a time-bounded defense and distinguishes Nel's destructive specialty from guarding. The coming conflict has two student sides with articulated responsibilities.
- **SENSEI ↔ ENGINEERING CLUB:** Hare asks Sensei to recruit less-close specialists; Utaha accepts, while secure Hibiki/Kotori lines provide partial personal motives. No evidence Sensei controls engineers or approves every tactic. Late Alice-labeled engineer exchange is quarantined.

## V002 C001 E013 relationship delta — decoy debt and inverted defense

- **ALICE ↔ CLUB/YUZU/MOMOI:** Alice is detained as part of the plan; Yuzu promises a prompt rescue and Momoi voices fear that failed support would make confinement purposeless. Their concern is direct, but neither Alice's detailed consent nor rescue is shown.
- **YUUKA ↔ ALICE:** Yuuka refuses Akane's playful sixth-maid request and orders Alice held as an alleged attacker. That is a bounded custody decision, not proof Yuuka knows the decoy arrangement or that Alice is medically safe.
- **YUUKA ↔ ENGINEERS:** Yuuka suspects an overt engineer repair trap and orders a non-Engineering replacement. The replacement's disguised engineering provenance defeats that screen; both her caution and the coalition's deception are real.
- **MOMOI/MIDORI/SENSEI ↔ AKANE/NOAH:** their entry is enabled by a system that rejects defenders' fingerprints and traps Akane and reportedly Noah. The opposition is not an abstract security score; persons are confined, with emergency access outcome unshown.
- **MIDORI ↔ SENSEI:** Midori asks physical handholding in the dark and later seeks tactical advice. One retreat choice elicits student resistance; coordinated trust includes disagreement, not blanket obedience.
- **AKANE ↔ C&C:** she calls offline `01`/Asuna and receives an anonymous `02` message claiming the club is in range. Do not infer the sender's identity, weapon or completed rescue.

## V002 C001 E014 relationship delta — allied cover, defender escape, unexpected welcome

- **UTAHA/HIBIKI ↔ CLUB:** Utaha takes Karin's rooftop attention with her chair, while she credits Hibiki's distant indirect fire; Momoi/Midori observe stopped sniping and hurry. No permanent safety or victory is proven.
- **KARIN ↔ CLUB/ENGINEERS:** Karin targets the club and appraises Utaha's chair, then faces a threat from a separate angle. Her anti-club certainty is qualified by actual counterplay, not by a shown surrender.
- **AKANE ↔ YUUKA/COALITION:** Akane destroys the shutter, reports facility damage reluctantly to Yuuka, asks the club location and pursues. A failed call/outage interrupts coordination, not her willingness to act.
- **MIDORI ↔ SENSEI:** Midori cautions the teacher about dark footing, continuing concrete situational care under risk without a Sensei choice or new intimacy claim.
- **ASUNA ↔ SENSEI/CLUB:** Asuna says she waited to meet both, corrects her address to `先生`, then declares her enjoyment of combat. This is a first direct opposed encounter, not evidence of private familiarity or a fight result.

## V002 C001 E015 relationship delta — Alice chooses reunion

- **ALICE ↔ MOMOI/MIDORI/CLUB:** after leaving the reflection room, Alice changes from an initial store-directed quest to the endangered twins and says companions should not be abandoned. They visibly recommit with her. This supports reciprocal action, not a completed Mirror mission or full prior consent record.
- **MOMOI ↔ SENSEI:** Momoi apologizes for the students' inadequate strength despite Sensei's aid. Sensei's encouragement or self-blame is branch-conditioned; the apology is not evidence Sensei authored the decoy or controls the institution.
- **YUUKA ↔ CLUB/SENSEI:** Yuuka names formal suspension/confinement and a possible Schale complaint, instead of Momoi's imagined mild room restriction. Her opposition is an institutional accountability act, with adjudication unshown.
- **ASUNA ↔ TWINS/C&C:** Asuna privately admires the twins' teamwork while opposing their escape; later reports severe hit effects, with Akane checking and protecting her. Adversarial respect and physical vulnerability coexist.
- **KARIN ↔ UTAHA/HIBIKI/AKANE:** rooftop contact and interruption of Karin's support persist, but scene 3/8 labels flip too extensively to assign a club-belonging argument or junior's motive to either rooftop speaker. External Akane/Hare reports support tactical consequence only.

## V002 C001 E016 relationship delta — a threatened party is protected by Yuzu

- **YUZU ↔ ALICE/MOMOI/MIDORI/SENSEI:** Yuzu knowingly steps before Nel and uses a false council identity/emergency to redirect her. The group survives the immediate hiding crisis, and Yuzu says she is glad to help. E013's rescue promise now has performed protection, not yet safe extraction or a proof she is generally fearless.
- **NEL ↔ YUZU:** Nel responds to an apparent colleague and articulates `度胸` as a combat value. Their encounter is based on Yuzu's deception; it is not a verified new friendship or proof Nel knows her real affiliation. Personalized praise/farewell labels later flip and are not person-voice evidence.
- **ALICE ↔ PARTY:** Alice holds Mirror, but Yuzu insists `G.Bible` remains the aim; Alice offers rearguard coverage and the twins move toward another fight. Fellowship continues as distributed work under danger, not achieved rescue.
- **SENSEI ↔ PARTY:** Momoi seeks advice while hidden and Alice later asks for direction. Sensei's only printed response is internal thought wishing for everyone's safe return; do not convert it to a spoken order.

## V002 C001 E017 relationship delta — contract ends, belonging stays conditional

- **NEL ↔ AKANE/C&C:** Akane apologizes for the failed job she planned; Nel rejects reputation as the important issue. She reports Rio withdrew their assignment but commissions Akane to research the game club from her own interest. This is changed duty plus continuing attention, not verified revenge or friendship.
- **MOMOI/MIDORI ↔ ALICE/YUZU:** Momoi names the great-game result as how all can remain in their room and fears Yuzu's dorm return and Alice's uncertain future. Alice asks whether she must leave; Momoi reassures her. The promise is relationally meaningful but not an institutional guarantee.
- **MIDORI ↔ SENSEI/ALICE:** Midori hopes Sensei/Schale would aid Alice if the club fails; Sensei gives no answer or commitment in this unit. Do not enter a confirmed fallback guardianship.
- **MAKI/VERITAS ↔ CLUB/SEMINAR:** Maki delivers an openable file and reports returning Mirror to Seminar. The joint operation has reached handoff, but its personal/disciplinary aftermath and Bible contents remain unknown.

## V002 C001 E018 relationship delta — Yuzu's circle and Alice as appreciative player

- **ALICE ↔ GAME CLUB:** Alice gives a repeated-play, first-person account of enjoying the club's game because she feels Momoi/Midori/Yuzu's love and dreams within its companion world. Her reception is a real relationship effect, not a vote from the whole market or a guarantee for the sequel.
- **YUZU ↔ MOMOI/MIDORI:** Yuzu says severe criticism drove her into the club; the sisters arrived six months earlier as enthusiastic players and collaborators. The flashback depicts their praise and explicit identification, strengthening her reported causal history without making every anonymous turn a clean named quotation.
- **YUZU ↔ ALICE:** Alice's `面白い` fulfilled Yuzu's personal dream of building with close companions and being appreciated. Yuzu wants this shared practice to continue even after poor ranking and Bible disappointment.
- **CLUB ↔ SHARED WORK:** Momoi responds to Yuzu/Alice by starting `TSC2` under a stated six-day interval. This is renewed cooperation, not submitted output, official recognition or solved separation risk.

## V002 C001 E019 relationship delta — publication and bounded opposition

- **YUZU ↔ CLUB/AUDIENCE:** Yuzu supports web publication despite the older hostile-response history, because actual viewers/players complete a work for her. She says companions make criticism bearable; the initial mixed comments have not yet tested that belief over time.
- **ALICE ↔ MIDORI/CLUB:** Alice's proposed beam against a commenter is refused by Midori, then Alice accepts a fight and incurs real harm. The group finds her and turns to retreat; concern and constraint coexist, not unconditional approval of her force.
- **MOMOI ↔ SENSEI/CLUBROOM:** Momoi rejects fighting from the room to avoid harming Sensei or their physical shared place. This is a concrete protective choice, with the later battle's collateral damage still unresolved.
- **NEL ↔ YUZU/ALICE/SENSEI:** Nel says she knows Yuzu deceived her yet praises it; she attributes student coordination to Sensei and seeks to test Alice, expressly denying revenge. After the blast she declines pursuit. This is opponent respect/interest under force, not friendship or a verified romance.
- **C&C ↔ NEL:** Karin/Akane consider tracking the wounded group, but Nel stops them. Later teasing about Sensei/height is speculative within the team, not an admitted preference or relationship.

## V002 C001 E020 relationship delta — belonging negotiated under a deadline

- **ALICE ↔ CLUB/NEL:** maid clothing and Nel's message frighten Alice even after Midori judges her body repaired. She trusts Sensei as a possible refuge but grieves losing the daily club, then welcomes the bounded reprieve. The final machine text is not her communicated knowledge.
- **YUZU ↔ CLUB/SENSEI:** Yuzu believes she could return to the dorm with the three friends and Sensei in her life, despite possible renewed insults. Her statement shows a broadened support network, not a demonstrated move.
- **MOMOI/MIDORI ↔ ALICE:** under imagined expulsion they offer room, bed and food; Yuzu warns of possible consequences. The offers make attachment concrete while exposing resource/legal limits. Scene-label corruption prevents clean attribution of every later celebratory phrase.
- **YUUKA ↔ CLUB:** she interrupts their mistaken grief with congratulations, apologizes for `ガラクタ` and thanks them for remembered play. She remains the council's conditional administrator, directing later paperwork; apology does not erase adversarial institutional history.
- **SENSEI ↔ ALICE:** the teacher's Schale thought and Alice's stated trust point toward an available relationship, but no relocation or accepted spoken contract occurs.

## MAIN_V002_C001 checkpoint relationship reconciliation

The club's shared work and room become a conditional home for Alice and Yuzu; the apparent ranked loss exposes their distinct separation risks before the special prize preserves co-presence for now. Yuuka changes from gatekeeper/opponent to apologetic conditional administrator, not an unrestricted ally. Nel's independent interest, non-pursuit and “see you again” remain charged/ambiguous, not friendship or romance. Sensei is a support possibility, but E020 Schale placement was internal and unacted. [Checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_002_時計じかけの花のパヴァーヌ/BLUE_ARCHIVE_MAIN_V002_C001_CHECKPOINT.md) governs; do not transfer audience-only `Divi:Sion` text into the group's relationships.

## V002 C002 E001 relationship delta — truce collapses over Alice

- **RIO ↔ HIMARI:** both testify to planning the prior Mirror/C&C test, but Himari explicitly corrects Rio's `同盟` to `休戦`. Their opposed interpretations of Alice end cooperation; Rio attempts detention and Himari evades AMAS. This is a changed tactical relationship, not evidence they were friends or that the full prior operation was consensual for Alice/club.
- **RIO/HIMARI ↔ ALICE:** both classify the absent Alice through inherited terms, but one “weapon” and one “cute junior” reading collide. Alice does not hear them and her own bonds/choices are not overwritten by either researcher's label.
- **HIMARI ↔ unknown C&C figure:** her interrupted `5番目のC&C` guess follows apparent escape. It is not a confirmed identity, encounter result or new named relationship.

## V002 C002 E002 relationship delta — ordinary friendship conditions

- **YUZU ↔ CLUB:** Yuzu's shyness under praise and her refusal to overuse `ハメ技` against friends coexist with precise, assertive action against an apparently unfair opponent. The game-fun concern is an explicit relationship-sensitive limit; the one exception does not abolish it.
- **ALICE ↔ YUZU:** Alice looks to Yuzu's winning record, loses her own match and watches Yuzu's successful rematch. She accepts a new tactic as part of play; no mentorship contract or future implementation is shown.
- **SENSEI ↔ CLUB:** the invitation brings Sensei into relaxed play and brainstorming; the club solicits ideas, but no authored design or adult rescue is established. The four friends' next-prize promise remains their shared aspiration.
- **RIO/HIMARI ↔ CLUB:** no contact or information transfer is represented. The E001 covert conflict stays outside the club's knowledge in this unit.

## V002 C002 E003 relationship delta — a dispute contained, a quest shared

- **MOMOI ↔ MIDORI:** a production disagreement over grand spectacle versus feasible/used labor escalates to an invitation for Sensei to choose. The twins accept Yuzu's match procedure, but no winner, design concession or restored consensus is shown.
- **YUZU ↔ TWINS/SENSEI:** Yuzu recognizes Sensei's discomfort, interrupts the demand for an adult verdict, and explains a club custom. She can act as mediator while remaining shy under praise; the custom's fairness is not proven.
- **ALICE ↔ SENSEI:** Alice wants Sensei as a party companion and enjoys a Sensei-themed item/guardian image. In campus play she deliberately makes them both level-one apprentices; Sensei mirrors her `前進` principle and credits her. The relationship is reciprocal game-language support, not a literal omnipotent protector.
- **RIO/HIMARI ↔ CLUB:** no E001 secret reaches the group; the covert confrontation remains a separate unresolved track.

## V002 C002 E004 relationship delta — translated companionship, bounded attention

- **ALICE ↔ SUMIRE:** they say they often meet while Sumire jogs and affirm one another as exercise/adventure companions. Their sustained-effort ideals overlap, but RPG stats and bodily training are not identical beliefs. Only this jogging relation is directly evidenced.
- **ALICE ↔ ASUNA/KARIN/NEL:** Alice welcomes the two C&C students into a future adventure while remaining frightened by Karin's report that Nel seeks her. Her invitation is not an actual party or proof of reconciliation with Nel; Karin's “fond of Alice” is appraisal.
- **SENSEI ↔ KARIN:** Sensei's compliment elicits Karin's discomfort at being looked at, followed by an apology. The later compliment is internal and unheard; no romance inference follows.
- **ASUNA ↔ KARIN/RIO:** Asuna discloses a reported Rio task despite Karin's secrecy reminder. The Gehenna inquiry's outcome and their knowledge of E001's covert operation remain unknown.

## V002 C002 E005 relationship delta — Nel reclassified without erasing friction

- **ALICE ↔ MILLENNIUM PEERS/ENGINEERS:** anonymous students recognize and encourage Alice, including snack-gift play; engineers accept her affection for the railgun. The narrated social welcome is plural but not an individually mapped bond or evidence of finished creative output.
- **ALICE ↔ NEL:** a reported repeated arcade relationship is now visible. Alice says the former enemy is now an ally/game companion; Nel wants rematches and coaching. Their play/understanding is real, but Alice fears losing her Sensei day and complains of hunger/time, while Nel insists on more play. Residual maid-outfit aversion persists.
- **NEL ↔ AKANE:** Akane enforces an agreed game-time limit and recalls a mission notice, limiting Nel's recreational persistence. This does not identify the mission or prove every earlier match was forced.
- **ALICE ↔ SENSEI:** Alice says their adventure was fun, admits the idea quest failed and asks for future adventures; the sole reply agrees. Sensei's `u:0088` thought cannot be treated as spoken before Alice's reaction.

## V002 C002 E006 relationship delta — supported visit, sudden inaccessible state

- **YUZU ↔ CLUB:** Yuzu struggles to reach Veritas; Momoi/Midori/Alice offer encouragement and Alice physical support. This is a fresh ordinary support instance, not proof Yuzu is comfortable in unfamiliar rooms.
- **ALICE ↔ CLUB/SENSEI:** the room knows Alice as their friend; her pause and protocol speech alarm them. Yuzu notices change, Sensei inwardly calls to her, but no dialogue establishes that Alice hears them, recognizes them in this state or has rejected them.
- **VERITAS ↔ CLUB/SENSEI:** Maki brings both groups to examine a find with unclear risk. The combined gathering is not a consented Alice-identity experiment on the present evidence, even though E001 gives the audience separate covert-test knowledge.
- **RIO/HIMARI ↔ ALICE:** absent and unmentioned in the room; their E001 interpretations do not become the club's understanding merely because an AL-1S line appears.

## V002 C002 E007 relationship delta — emergency separates danger from culpability

- **ALICE ↔ CLUB:** her protocol-state speech and weapon charging endanger nearby friends, but no direct line establishes her awareness/consent or that her ordinary affection is gone. Midori/Yuzu's alarm about Momoi is not yet a medical outcome.
- **NEL/C&C ↔ ALICE/CLUB:** Nel's arrival interrupts the danger, and C&C's team acts to contain it. This adds a protective crisis role to E005's arcade bond, without proving a fixed friendship contract or full Alice recovery.
- **SENSEI ↔ GROUP:** Sensei thanks C&C and checks Veritas/club members. The care path is distributed across Maki's interference, C&C's intervention and student calls, not a solo adult command.
- **RIO/HIMARI ↔ INCIDENT:** neither appears or is reported in the room. Audience E001 knowledge does not establish that C&C came under their Alice-test order.

## V002 C002 E008 relationship delta — injury and self-isolation

- **MOMOI ↔ MIDORI/CLUB:** Momoi's two-day unconsciousness explains Midori/Yuzu's acute concern; the source does not show a recovery or definitive prognosis.
- **ALICE ↔ MOMOI/CLUB:** Alice secludes herself, refuses contact and calls Momoi's injury her fault despite amnesia for her actions. This is a real relational rupture and guilty appraisal, not proof she knowingly chose the protocol attack. Midori/Yuzu keep reaching out.
- **SENSEI ↔ ALICE:** Sensei volunteers to handle a conversation and asks Alice about seclusion/food through printed choices. Inwardly labeled entry lines cannot be laundered into secure spoken permission; their care does not immediately resolve guilt.
- **RIO ↔ CLUB/SENSEI:** Rio enters as president and asserts she has “truth” to share. Her E001 research/containment position is audience background, not yet a disclosed shared account in this room. Himari remains absent.

## V002 C002 E009 relationship delta — denial of friendship versus protective refusal

- **RIO ↔ ALICE/CLUB:** Rio publicly tells Alice and friends the AL-1S/Divi:Sion theory, casts former friendship as suspect and urges Alice's disappearance/halo destruction. Her speech is an intervention in an existing bond, not proof the bond was false. Alice expresses wanting ordinary shared quests. Himari's E001 dissent is still absent from the room.
- **NEL ↔ ALICE:** the former duelist/arcade companion now refuses to abduct Alice as an uninformed same-school student. Her reason is explicit, though neither a formal friendship promise nor an unlimited protection guarantee follows.
- **RIO ↔ NEL/C&C:** Rio's claim of feeling-free obedience fails in Nel's direct refusal. Rio describes Nel's disobedience as habitual and calls Toki as a contingency; those appraisals are her interested account, not independent trait measurement.
- **TOKI ↔ NEL/C&C/SENSEI:** Toki greets “seniors” and Sensei, states C&C callsign zero four, and rear-ambushes Nel. This establishes a hostile first shown interaction, not a completed rivalry, personal motive or proof she was Himari's E001 unknown encounter.
- **SENSEI/MIDORI/YUZU ↔ ALICE:** Midori contests imposed identity, Sensei's choice rejects a purely rationality-based framing and Yuzu seeks help. No displayed rescue or resolution of Alice's fear occurs.

## V002 C002 E010 relationship delta — removal under threatened harm

- **RIO/TOKI/AMAS ↔ NEL/GROUP:** Toki follows Rio's equipment authorization and restrains Nel while AMAS holds the others. Toki's role obedience contrasts with Nel's prior refusal; neither determines the entire C&C team's values.
- **ALICE ↔ FRIENDS/SENSEI:** Alice names Momoi, Midori, Yuzu, Nel, Sensei and others in fearing future injury, thanks them for shared adventures, and departs with Rio. The farewell expresses attachment and self-sacrifice under pressure, not repudiation of prior friendship or secure consent to halo destruction.
- **MIDORI/YUZU/SENSEI ↔ ALICE:** Midori invokes her hero sword, Sensei directly asks for discussion rather than unquestioning belief in Rio, and Yuzu remains afraid/help-seeking. The inability to intervene is narrated AMAS restraint, not indifference or a voluntary surrender of their bond.
- **RIO ↔ SENSEI:** Rio asks the adult to enact her exclusionary risk calculus and offers a future apology if hurt. Sensei's printed objection protects student status but is not accepted. Rio's acknowledgment of adult distress is not a correction of Alice's treatment.

## V002 C002 E011 relationship delta — refusing a coerced ending

- **MOMOI ↔ MIDORI/CLUB:** Momoi's awake return relieves Midori's immediate uncertainty but does not medically certify recovery. Their familiar teasing and Midori's intense response coexist with the new Alice emergency.
- **MOMOI ↔ ALICE:** Momoi says Rio's classification is secondary to her refusal to lose Alice this way, rejects the farewell as a final ending and initiates retrieval. This is an expressed bond and proposal, not proof the safety question is irrelevant or that reunion has occurred.
- **NEL ↔ ALICE/MOMOI/C&C:** Nel asks whether Alice understood the threatened halo destruction, refuses a comforting excuse for her own defeat and endorses Momoi's aim. Akane and another C&C voice align; exact Karin/Asuna assent at `u:0087` is attribution-cautioned.
- **YUZU/MIDORI ↔ ALICE:** Midori asks whether the accusation might be true; Yuzu admits uncertainty but seeks Alice's own account and a conversation with Rio. Doubt does not mean abandonment.
- **SENSEI ↔ GROUP:** Hare asks for guidance, Momoi asks for help, and Sensei inwardly accepts thinking of a method. No audible promise or enacted rescue is shown.

## V002 C002 E012 relationship delta — internal dissent and task-bound coalition

- **YUUKA/NOA ↔ RIO/ALICE:** the Seminar pair rejects Rio's abduction/halo aim and provides records/coordinates, while saying their positions limit further direct help. Opposition to a leader is visible; they do not yet encounter or recover Alice.
- **ENGINEERING ↔ ALICE/CLUB:** Utaha frames Supernova as Engineering's taken invention; colleagues imply she is masking a friend-rescue motive. The latter is teasing through corrupt labels, not a verified private confession. Engineering volunteers access support.
- **NEL/C&C ↔ CLUB/SENSEI:** Nel offers C&C as a frontal diversion so the club/Engineering/Sensei can enter behind. This extends E011's solidarity into an assigned risk, not guaranteed success or unrestricted obedience.
- **VERITAS ↔ COALITION:** Maki/Kotama promise remote defense hacking; other members' precise field placement is not shown.
- **MOMOI/SENSEI ↔ ALICE:** Momoi names Alice's retrieval as the objective; Sensei's choice affirms participation. Momoi's “runaway” rhetoric does not make Alice's E010 departure free, and final Sensei `心の声` is not an audible command.

## V002 C002 E013 relationship delta — Himari's dissent and coalition execution

- **HIMARI ↔ RIO/ALICE:** Himari directly rejects Rio's confinement/halo aim at Eridu; Rio accepts the act description but hopes for understanding. Alice is silent nearby in the facility-side sequence; neither agreement nor Himari's freedom status is shown.
- **VERITAS ↔ RESCUE PARTY:** train access and local network intervention make their E012 support operative. Hare warns that monitoring may miss surprises; help is not a promise of total safety.
- **C&C ↔ TOKI/RIO:** C&C's noisy front draws Toki, who greets seniors by name/callsign. The confrontation is underway, not a result or proof she is free of Rio's direction.
- **SENSEI/CLUB/ENGINEERING ↔ ALICE:** the party reaches Eridu, but no direct renewed Alice contact occurs. The silent Alice cue must not be treated as seeing or hearing her friends.

## V002 C002 E014 relationship delta — same-team opposition and separated rescue branches

- **TOKI ↔ C&C/RIO:** Toki addresses the others as seniors and reports Rio ordered suppression of disobedient C&C. Her obedience is visible, not proof that C&C shares Rio's judgment or that she understands every team movement. Akane's polite challenge and Asuna's casual teasing mark opposition; an Asuna-labeled formal surrender line is voice-uncertain.
- **NEL ↔ TOKI/ALICE:** Nel appears at the front, wants a rematch after E009–E010 and says defeating Toki first will prevent interception before helping Alice. This adds a tactical reason alongside wounded pride; neither victory nor Alice contact follows.
- **CLUB/ENGINEERING/VERITAS/SENSEI ↔ ALICE:** Momoi and the rear group emerge at the surface, and Hare navigates toward Alice's *probable* tower location. The bond motivates pursuit, not a represented reunion, consent conversation or secure restoration of place.

## V002 C002 E015 relationship delta — forced separation, undischarged care

- **TOKI/RIO ↔ NEL/C&C:** Toki uses Rio-given Eridu authority to physically divide Nel from her coordinated teammates. It is a tactical separation under institutional command, not a change in C&C loyalty or proof Nel has lost.
- **RIO ↔ SENSEI/CLUB:** Rio says prior persuasion failed and casts Alice as the one who must be sacrificed. Sensei's alternative choice can state opposition, but alternatives cannot be combined; the party remains in conflict with her new weapon.
- **MOMOI ↔ ALICE/RIO:** Momoi, personally injured in the incident Rio invokes, insists on returning Alice. This makes her refusal informed by lived harm rather than ignorance of it, while Alice herself is absent and no safe reunion occurs.
- **VERITAS ↔ COALITION:** the communication cut interrupts the support relation. It does not show abandonment by Veritas or complete loss of all later contact.

## V002 C002 E016 relationship delta — relying on juniors versus acting alone

- **HIMARI ↔ RIO:** Himari can recognize the plan's sophistication while rejecting its self-righteousness. Her “walk at others' pace” and “confide in juniors” diagnosis is an adversarial relational appraisal, not proof of Rio's every private habit.
- **EIMI ↔ HIMARI:** Eimi comes to Himari after recalling the pudding condition and says she would rather eat together. Himari explicitly enjoys waiting for rescue by her junior; the bond is direct but its formal roster/history remain unspecified here.
- **HIMARI/EIMI ↔ VERITAS/OTHER JUNIORS:** Himari says she has many dependable juniors as Veritas struggles and Mirror startup appears. The editing implies a wider support network; precise coordination and messages between branches are unshown.
- **CHIHIRO ↔ REAR PARTY:** Chihiro arrives when the weapon slows and checks whether everyone is safe. Her helpful contact is direct, but no Alice encounter or durable safety is established.

## V002 C002 E017 relationship delta — aid crosses club lines

- **CHIHIRO ↔ HIMARI/VERITAS/SENSEI:** Chihiro credits Himari's Mirror preparation, asks Veritas to hold the link and takes Sensei navigation. “Vice-president”/former-leader address gives local hierarchy, while exact earlier device-seizure intent is only inferred.
- **SUMIRE ↔ ALICE/CHIHIRO/SENSEI:** Sumire says news of Alice moved her to help. Chihiro thanks her for access assistance; E004 training acquaintance now has a costly rescue action, not a formal membership change.
- **ENGINEERING ↔ MOMOI/CLUB:** Engineering defeats a local obstacle, then stops from exhaustion and entrusts continuation to Momoi's group. Momoi thanks them; Utaha gives her an unnamed object. Trust/handoff is shown, not a guarantee of later function.
- **RIO ↔ COALITION/ALICE:** Chihiro reports displacing Rio from network control; Rio and Alice are absent from this exchange. No renewed consent conversation or final relation repair occurs.

## V002 C002 E018 relationship delta — reunion restores the rescue priority

- **C&C ↔ NEL/TOKI:** Karin/Asuna return to Nel despite Toki's split. Rio orders Toki away, so no group win over her is established. Akane reminds Nel that Alice retrieval, not finishing a grudge match, is the purpose; Nel accepts.
- **C&C ↔ SENSEI/CLUB:** the groups meet at the tower exterior. Akane recounts the first fight; Sensei's understanding is mediated by her report. They share the rescue objective without having reached Alice.
- **RIO ↔ TOKI:** Rio explicitly does not blame Toki for the setback, takes prediction responsibility, orders regrouping and authorizes the higher-grade suit. Toki's obedience is visible, not a complete private motive.
- **RIO ↔ SENSEI/ALICE:** Rio singles Sensei out as a possible variable and invokes a suit originally meant for her “Princess” target. This is her interpretation and contingency, not proof Sensei alone caused the coalition's progress or Alice consented to being an enemy.

## V002 C002 E019 relationship delta — trust under failed counter

- **SENSEI ↔ NEL:** Nel explicitly trusts Sensei's rooftop direction and takes the physical risk; Sensei notices her injury afterward. Trust does not prove the tactic fully works or establish an audible version of earlier inward `u:0019`.
- **RIO ↔ C&C/TOKI:** Rio says the suit was also prepared for C&C defection and orders Toki to recover Sensei, revealing institutional distrust alongside her larger threat story. Toki follows orders; her private view of C&C or Alice remains narrow.
- **CHIHIRO/MOMOI ↔ SENSEI/PARTY:** Chihiro cues Momoi to exploit a gap, Momoi acts and the capture target escapes by Toki's report. Their support rebuts a sole-Sensei account; exact device/action is not printed.
- **ALICE ↔ RESCUERS:** no Alice contact or consent conversation. Survival/escape from this engagement keeps recovery possible but does not restore belonging.

## V002 C002 E020 relationship delta — care, challenge and shared inference

- **C&C ↔ NEL:** Akane, Karin and Asuna worry about an unconscious/deeply injured captain; Nel wakes but rejects reassurance and insists on helping. Concern is direct, while her capacity to continue safely is unverified.
- **NEL ↔ GAME DEVELOPMENT DEPARTMENT/ALICE:** Nel challenges Momoi/Midori's despair and explicitly names Alice rescue as their common reason for coming. This is solidarity under danger, not proof Alice knows/consents or that injured Nel is obliged to fight.
- **YUZU ↔ GROUP:** Yuzu overcomes hesitation enough to report a brief hit and propose a trap, shifting from protected companion to informational/tactical contributor. The content has not yet been shared on-page.
- **RIO/TOKI ↔ COALITION:** Rio dismisses their plan without demonstrated knowledge of its mechanics; Toki obeys. Nel calls for a rematch, which is intention rather than a completed contest.

## V002 C002 E021 relationship delta — Yuzu recognized, team consent and misattribution corrected

- **NEL ↔ YUZU/GAME DEVELOPMENT DEPARTMENT:** Nel accepts Yuzu's risky proposal because she sees a friend-courage trait in her; the nickname `おでこ` and Yuzu's surprised response suggest growing recognition. Akane retrospectively interprets Nel as changed since meeting the club. Label anomalies around `u:0031/0037-0039` prevent exact attribution of every joking line.
- **NEL ↔ C&C:** Akane warns about injury, Nel says she will not force help, Akane and Asuna assent to their leader. Their coordinated roles enable local victory, but hierarchy and Nel's fitness remain live qualifications.
- **RIO ↔ SENSEI/AKANE:** Rio imagines the plan as Sensei's and morally blames them for injured Nel's participation; Akane directly rejects that command attribution. Rio's “zero” prediction is then defeated locally.
- **MOMOI/YUZU/CHIHIRO ↔ RESCUERS:** Yuzu credits Momoi's earlier elevator idea, Chihiro executes the hack, and C&C turns it into a tactical opening. Alice is still absent and cannot be assigned knowledge of this coalition action.

## V002 C002 E022 relationship delta — Alice present but unreachable

- **NEL/C&C ↔ CLUB/SENSEI:** Nel is numb and unable to move, asks after her teammates and tells the younger group to bring Alice back; Sensei thanks her and proceeds. This is a handoff, not proof of Nel's recovery or full C&C injury status.
- **CLUB ↔ ALICE/KEY:** Momoi/Midori/Yuzu reach Alice but get no secure answer from her. Key denies their name for her, claims isolation and warns against unplugging. Preserve Key as separate provisional speaker; neither its threat nor the printed `u:0051` Alice-label anomaly is Alice consent.
- **RIO ↔ ALICE/SENSEI:** Rio concedes the guard battle but maintains her threat forecast until Key activation forces self-doubt. She then proposes stopping the system alone; Sensei's secure choices challenge overlooked-help assumptions. Her earlier E001 Himari consultation prevents a literal “spoke to no one” claim, but Alice/club exclusion remains.
- **YUUKA/NOA ↔ COALITION/RIO:** Yuuka orders Noa to cut power at the 99%-report frontier. This widens the responding network beyond Rio and the tower party; impact remains unseen.

## V002 C002 E023 relationship delta — aid with accountability and volunteered risk

- **YUUKA/NOA ↔ SENSEI/CLUB/RIO:** Noa says Yuuka chose help beyond the agreed coordinates; Key reports cutoff success. Yuuka still accuses Rio of budget diversion and promises later reckoning. Support does not erase institutional dispute.
- **ENGINEERING ↔ COALITION/KEY:** the club returns with modified Avant-Garde-kun and engages followers, contradicting Key's zero-force claim. Their group contribution is visible; individual design credits have label tension.
- **HIMARI ↔ RIO/ALICE:** Himari returns from isolation, says she anticipated further Rio trouble, and proposes waking Alice rather than sacrificing her or Rio. Rio confirms equipment and voices serious risk; reconciliation or full trust is not shown.
- **YUZU ↔ ALICE/SENSEI:** Yuzu volunteers for the dangerous retrieval conditional on helping Alice. Sensei's own `u:0073` assent is inward. Alice remains without secure response, so friendship motivates action without confirmed reciprocity in this state.

## V002 C002 E024 relationship delta — directly answered friendship

- **ALICE ↔ MOMOI/MIDORI/YUZU:** Alice now responds in the dive, fears her presence hurts them and asks whether she can continue adventures together. Momoi cites concrete shared work and offers a revisable job, Midori returns Alice's no-abandonment maxim, and Yuzu calls her `仲間（友達）`. Alice chooses to remain Alice/their hero; reciprocity is shown in-space, not yet physically reunited or safe.
- **ALICE ↔ KEY:** Key uses real injury footage to press an exclusive guilt and “Princess” fate. Alice rejects that purpose and chooses her own name/class; Key's silence does not establish permanent severance.
- **SENSEI ↔ ALICE/CLUB:** secure choices support the club's no-abandonment and possibility language; many apparent assurances are inward. Sensei neither creates Alice's decision alone nor proves her external awakening.
- **RIO ↔ ALICE/COALITION:** Rio is surprised by what she regards as impossible and questions her calculation; her prior coercive act, possible accountability and future response remain unresolved.

## V002 C002 E025 relationship delta — return without universal closure

- **ALICE ↔ CLUB/SENSEI:** Alice speaks during group game study and asks Sensei to sit beside her; Momoi, Midori and Yuzu continue ordinary co-play. This confirms a returned, reciprocal social relation after the dive but not every future safety condition.
- **RIO ↔ YUUKA/NOA/HIMARI/ALICE:** Rio leaves a resignation declaration and apology, then is absent. Yuuka objects that apology is insufficient; Himari handles facility closure. The text does not show Rio's reconciliation with any of them or a completed adjudication.
- **NEL ↔ TOKI/C&C:** Nel objects to the former opponent attending her discharge party and remains angry about injury, then reluctantly frames Toki as carrying out orders. Asuna welcomes Toki; social inclusion begins, but forgiveness/formal role status remain unproved.
- **SENSEI ↔ C&C/CLUB:** invited to the celebration and later club play. One C&C two-option branch converges; no composite personality inference or sole-author rescue credit.

## MAIN V002 C002 checkpoint reconciliation — belonging is observed, not guaranteed

The [C002 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_002_時計じかけの花のパヴァーヌ/BLUE_ARCHIVE_MAIN_V002_C002_CHECKPOINT.md) records Alice–club as a real reciprocal relationship before classification, through coercive separation and her own chosen return. It does not substitute for next-term recognition or residual safety work. Nel–Toki has an uneasy social opening, not full forgiveness/formal reassignment; Rio–Seminar ends in absence and an insufficient apology, not repaired trust.

## V003 C001 E001 relationship delta — Seia addresses an unanswered Sensei

- **SEIA → SENSEI:** Seia explains her view of the treaty/paradise and urges Sensei to witness the coming bitter truth. Sensei has no printed response or choice; familiarity, trust, hierarchy and actual acceptance cannot be inferred from her address alone.
- **TRINITY ↔ GEHENNA (reported):** Seia describes long mutual distrust and a proposed peace process. No institution speaks or acts in this unit; present interschool relation and treaty implementation remain unconfirmed.

## V003 C001 E002 relationship delta — group friction and an earlier invitation

- **KOHARU ↔ HANAKO/AZUSA/HIFUMI:** Koharu's teacher blame and committee excuse meet Hanako/Azusa challenge; her fear of lost membership surfaces. Hanako's provocation and Koharu's protest are visible, while individual comic lines have label uncertainty. Hifumi seeks a cooperative path rather than joining the blame.
- **HIFUMI ↔ SENSEI:** Hifumi asks for help and Sensei's secure choice says they will try. No tutoring result or unconditional rescue promise.
- **NAGISA/MIKA ↔ SENSEI:** at the earlier terrace, Nagisa introduces herself as host and Mika is named. No meeting purpose, trust relation or Sensei reply yet; `u:0004` attribution is suspect.

## V003 C001 E003 relationship delta — ten-year claim, host conflict and new teacher tie

- **NAGISA ↔ MIKA:** Mika reports childhood familiarity of ten years and repeatedly tests Nagisa's host stiffness. Nagisa asserts present host control, erupts at interruptions, then apologizes. This is one co-present repair; it does not establish durable hostility or their entire history.
- **TEA PARTY ↔ SENSEI:** Nagisa offers the restricted seat, asks Sensei to advise a temporary remedial club using Schale's exceptional authority, and Sensei accepts conditionally. Nagisa promises escort/possible dispatch; future role execution unshown. Mika's friendliness and newspaper report do not prove comprehensive trust.
- **SENSEI ↔ HIFUMI:** narrated roster recognition and a greeting follow prior V001 contact. Hifumi says the circumstances were unavoidable but does not identify them; avoid retrofitting E002's later group position into the present visit.
- **NAGISA/MIKA ↔ SEIA (reported):** they call Seia absent/hospitalized and normally current host. No direct Seia response or hospital evidence; E001 monologue timing remains unplaced.

## V003 C001 E004 relationship delta — pressured leadership and first disciplinary encounters

- **NAGISA → HIFUMI:** Nagisa praises her love/merit and asks her to guide the club as temporary president; Hifumi protests average grades and her own jeopardy. Hifumi's eventual plan does not prove initial eagerness or define their full reciprocal history.
- **SENSEI ↔ HIFUMI:** Hifumi confesses missed testing and feels judged; Sensei says she need not apologize to them, accepts a working partnership and follows her plan. Neither absolution from school duty nor successful rescue is implied.
- **KOHARU ↔ HIFUMI/SENSEI/HANAKO:** Koharu's stranger caution makes the visitors' entry awkward; Hanako's disputed emergence and swimsuit argument draw emphatic objection. No enduring dyad rule or valid sentence follows.
- **HASUMI/MASHIRO ↔ AZUSA:** Mashiro reports capture and Hasumi arrives with her. Azusa voices resistance/torture expectation; no interrogation, personal motive or student-club interaction yet.

## V003 C001 E005 relationship delta — authorized transfer and exposed peer

- **HASUMI → KOHARU/SENSEI:** Hasumi corrects Koharu's objection, interpreting Tea Party/Schale authority as permitting the two detainees' transfer. Koharu yields to her senior, not to an independently shown rule text.
- **KOHARU ↔ REMEDIAL PEERS:** Koharu publicly stigmatizes Hanako/Azusa and the “fool” club, then is announced as the fourth member herself. The text shows shock/embarrassment, not apology, reconciliation or permanent hostility.
- **HIFUMI ↔ FOUR/SENSEI:** Hifumi confirms all four are present and asks Sensei for help; both pledge to try. Hanako addresses her as president, Azusa adds a classroom-holdout boast. No learning plan or durable group trust yet.

## V003 C001 E006 relationship delta — task cooperation before friendship

- **HIFUMI → GROUP/SENSEI:** Hifumi sets all-four success and Sensei scheduling/tutoring remit, then corrects Koharu's solo-exit assumption. This is a leadership action, not proof peers accept it or tutoring succeeds.
- **HANAKO ↔ AZUSA/KOHARU:** Hanako asks Azusa's permission for `ちゃん` and calls the three companions; Koharu rejects imposed seniority/familiarity. Hanako accepts the no-seniority norm. Address consent is bounded; no stable closeness or hostility yet.
- **AZUSA ↔ PEERS:** Azusa accepts transfer disclosure, describes cooperation as mutual benefit and says she is unfamiliar with seniority. Her position avoids pretending intimacy, not a perpetual ban on relationship growth.
- **KOHARU ↔ GROUP:** Koharu predicts quick solo success and departs despite Hifumi's correction. Her institutional status anxiety now meets a collective exam rule; actual future choice remains open.

## V003 C001 E007 relationship delta — collaborative study under shared threat

- **HANAKO/AZUSA ↔ PEERS:** a question-and-answer study exchange covers several subjects, supporting group-level cooperation after E006's task-bound agreement. Repeated label/turn inversions prevent secure line-by-line tutor/learner assignments or proof of friendship.
- **HIFUMI → GROUP/SENSEI:** Hifumi observes apparent ability and motivation, expresses relief and confides Tea Party's first-failure camp instruction to Sensei. She withholds the feared third-failure consequence when asked; trust/disclosure is partial, not a demonstrated plan to mislead.
- **SENSEI ↔ GROUP:** Sensei privately approves and wishes all four well, asks about the camp and consequence. No one is shown responding to a specific lesson or test intervention; group support is not outcome.

## V003 C001 E008 relationship delta — common fate despite unequal marks

- **HIFUMI → GROUP:** Hifumi initially anticipates group rescue, passes herself, challenges Azusa's “near miss,” asks Koharu about her hidden ability and reacts to Hanako's two points. Her surprise marks a correction of prior appraisals, not rejection of the peers or an implemented new teaching plan.
- **HANAKO/AZUSA/KOHARU ↔ HIFUMI:** each failed result exposes Hifumi to the E006 shared condition despite her own pass. Azusa quips, Koharu calls the paper difficult, Hanako says studious appearance is not grades; none supplies a secure motive or acceptance of camp yet.
- **SENSEI ↔ HIFUMI/GROUP:** Hifumi asks Sensei to announce results; Sensei inwardly encourages her. Her private report credits Sensei's prior explanation on material she recognized, not demonstrated identical benefit for all four.

## V003 C001 E009 relationship delta — Nagisa's recruitment and Sensei's boundary

- **NAGISA → SENSEI:** she admits using Sensei in building a group “box,” apologizes, invites rebuke, then asks for the unknown traitor to be found. Disclosure and apology are real, but subsequent exam leverage prevents treating them as unconditional trust or repair.
- **SENSEI → NAGISA/STUDENTS:** Sensei raises the terminal risk, acknowledges that disclosure complicates the idea of pure covert use, then reserves an independent approach. Neither suspect-hunting consent nor completed protection of the four is shown.
- **NAGISA → FOUR/HIFUMI/MIKA:** Nagisa treats the four as possible suspects collectively; none is identified or present. She guesses Hifumi leaked the danger and values that tendency; Hifumi's exact knowledge of the whole plan is unshown. Mika's absence/chess aside says little about what she knew or approved.

## V003 C001 E010 relationship delta — group practice without full trust claim

- **AZUSA ↔ HIFUMI/PEERS:** Hifumi counters Azusa's combat-camp model; Azusa explicitly pledges second-exam study and no burden on others while retaining a security-preparation register. No peer has accepted the imagined defense plan, and the listed mines are not deployed.
- **HANAKO ↔ HIFUMI/KOHARU:** Hanako's cleanup proposal is adopted by Hifumi and tolerated by Koharu; later Koharu protests Hanako's swimsuit and narrator confirms Hanako changes. One negotiated boundary does not prove either durable intimacy or antagonism.
- **SENSEI ↔ GROUP:** Hifumi expects Sensei's week-long presence and receives a supportive singleton reply; Sensei then asks the students to connect with each other and call if needed. Exact room arrangement and availability in practice remain open.

## V003 C001 E011 relationship delta — work assignment and pool persuasion

- **HIFUMI ↔ KOHARU/HANAKO/AZUSA:** Hifumi delegates cleaning, Koharu demonstrates lobby work, Hanako proposes bedding and pool tasks, and Azusa accepts corridor work then joins pool preparation. This is observed collaboration, not proof of academic parity or knowledge of Nagisa's plan.
- **HANAKO ↔ AZUSA/KOHARU:** Hanako's play invitation elicits Azusa's present-effort reply; Koharu initially objects on exam relevance and swimwear, then grants local permission. No durable closeness or coercive control is established.
- **SENSEI ↔ GROUP:** Sensei appears as inward observer with one singleton reaction; the narrator credits the group for cleaning. No demonstrated adult-led tactical, scholastic or safety decision.

## V003 C001 E012 relationship delta — secrecy, refusal and care

- **NAGISA → HIFUMI/SENSEI:** Hifumi recalls Nagisa recruiting her as a secret peer informant because of her Schale link, treating Sensei as a proposed “lid” and threatening Hifumi with the fallback. The direction of pressure is now explicit; Hifumi's assignment is not voluntary enthusiasm.
- **HIFUMI ↔ SENSEI:** Hifumi seeks a night conversation, shares the expulsion/traitor burden and rejects sorting classmates; Sensei calls her kind, offers to handle the issue and invites her own contribution. She reports relief, while actual protection and her future decisions remain unknown.
- **HANAKO ↔ AZUSA:** Hanako notices poor rest and asks Azusa not to overdo guard duty; Azusa admits unfamiliar-place sleep difficulty but claims training endurance. Concern is shown, not proven intimacy or a diagnosis. Azusa thinks Hifumi is walking, not shown to know her confidential conversation.

## V003 C001 E013 relationship delta — study delegation and shared taste

- **HIFUMI ↔ GROUP:** Hifumi prepares/announces a practice exam, acknowledges poor collective position despite her own local pass, proposes targeted peer help and further checks. The group hears a study plan, not her private Nagisa assignment; no official score recovery yet.
- **HIFUMI ↔ AZUSA:** Azusa's explicit delight in Peroro and related goods lets Hifumi answer as an enthusiast and offer reward motivation. This is a new shared-interest contact, not confirmed durable trust or a completed academic bargain; some adjacent labels flip.
- **HIFUMI ↔ HANAKO:** Hifumi reports discovering Hanako's stronger past first-year answer and proposes investigating the current difficulty together with Sensei; Hanako tentatively acknowledges. Cause and consent to any particular tutoring method are open.
- **AZUSA ↔ KOHARU/HANAKO:** Azusa organizes morning washing while Koharu protests handling; Hanako teases. The scene's levity does not erase Koharu's expressed boundary. Hifumi was allowed extra rest on Azusa's pressure hypothesis.
- **SENSEI ↔ HIFUMI:** Hifumi credits late-night preparation help; Sensei credits her effort. The public teacher/student partnership does not disclose or settle their private E012 undertaking.

## V003 C001 E014 relationship delta — provisional trust and embarrassment

- **AZUSA ↔ KOHARU:** a shared-topic geometry question and help create a moment of respect/offer to ask again, though role-label inversions prevent secure attribution of each line. Hanako's shower innuendo is rejected by Koharu; study reciprocity is not equivalent to consent or durable intimacy.
- **HANAKO ↔ KOHARU:** Hanako's book teasing visibly embarrasses Koharu, who protests and becomes tearful. The probable apology/stop request at `u:0044-0045` is label-conflicted; repair cannot be assumed complete.
- **HIFUMI ↔ KOHARU:** Hifumi offers a possible confiscation account and warns of an inventory issue, which Koharu adopts; her benevolent framing is not independent evidence.
- **SENSEI ↔ KOHARU:** Sensei offers to go with her, and they depart together. Hanako anticipates a softer Hasumi reaction, but no actual encounter or return has yet tested that expectation.

## V003 C001 E015 relationship delta — trusted adult, private senior

- **KOHARU ↔ SENSEI:** she moves from embarrassing denial to saying Sensei thinks about her and offers a “secret” spy account. She expects teacher discretion, but no independently verified mission or explicit secrecy pact follows. Sensei later asks if she is all right after partial overhearing; she says yes.
- **SENSEI ↔ HASUMI:** Hasumi questions their entry despite Koharu's access bar, accepts Sensei's misleading book-for-lessons explanation, then requests and receives privacy for committee business. This is a temporary social/procedural accommodation, not exoneration or verified student-care coordination.
- **HASUMI ↔ KOHARU:** Hasumi directly restates the grade bar and speaks to Koharu alone. Fragmented overhearing contains a raised `それではダメなんです！`, but its subject/decision remain unavailable. Koharu's later `大丈夫` does not close the interaction's effects.

## V003 C001 E016 relationship delta — questioned knowledge

- **AZUSA ↔ HIFUMI:** Azusa recognizes Hifumi lost morning rest preparing the mock and offers washing help; Hifumi politely refuses. Recognition of labor is secure, further physical care is not enacted.
- **HANAKO ↔ AZUSA:** Hanako recognizes Azusa's tentative fifth-rule recollection and asks whether she met Seia; Azusa says she only recalls hearing it. Hanako's `vanitas`/transfer thought remains unfinished, so neither contact nor hidden provenance is established. Their lobby watch exchange remains sparse.
- **HIFUMI ↔ SENSEI/HANAKO:** Hifumi privately shares the discovered paper bundle with Sensei, infers deliberate failures and wonders why; Hanako is not present to answer. Hifumi's notice of Sensei's morning absence does not tell her about Mika.
- **MIKA ↔ SENSEI:** Mika meets Sensei at the filled pool and says she wondered how they were doing. This is a check-in, not evidence of a new disclosure about Nagisa, Seia or the alleged traitor.

## V003 C001 E017 relationship and checkpoint delta — allegiance tested

- **MIKA ↔ SENSEI:** Mika says she independently came, reports initiating Sensei's teacher invitation and probes whether they accepted Nagisa's traitor request. Sensei refuses the hunt and declares alliance with students including Mika; she feels pleased yet questions whether “all students” makes concrete allegiance empty. Her Azusa-protection request has no printed acceptance or plan.
- **MIKA ↔ NAGISA/AZUSA:** Mika says Nagisa opposed her invitation and does not know of this visit; she identifies Azusa as Nagisa's suspected target while wanting protection. This is an interested triangular account, not confirmed Nagisa knowledge or Mika–Azusa prior interaction.
- **AZUSA ↔ SAORI/UNKNOWN:** an unlocated intercut shows silent named Saori, unknown voices asking about progress and Azusa saying the plan proceeds. No secure voice assignment to Saori, relationship type, plan content or chronology is supplied.
- **HIFUMI ↔ GROUP:** absent from this scene; her E012 refusal to suspect classmates and E013–E016 study work remain intact, not knowledge of Mika's disclosure.

The V003 C001 checkpoint is the canonical relationship synthesis. Readiness becomes 21 partial / 34 unmodeled across 55 with Saori's new minimal row.

## V003 C002 E001 relationship delta — attempted reconciliation and constrained adult

- **MIKA ↔ AZUSA/ARIUS:** Mika admits secretly forging Azusa's admission as a hoped-for symbol of reconciliation, while acknowledging she knows Azusa only incompletely. Protection is requested but the student's knowledge/consent and reciprocal trust are unshown.
- **MIKA ↔ NAGISA/SEIA:** she claims Nagisa/Seia opposed an Arius overture, fears Nagisa's ETO power, and reverses her earlier Seia hospitalization account with a halo-breaking allegation. These are Mika's relationship/political narratives; neither Seia nor Nagisa replies here.
- **MIKA ↔ SENSEI:** she asks for trust and Azusa protection but says the account is one-sided, then poses a protect-versus-investigate binary. Sensei asks whether she will be all right, which she reads as personal concern; no formal alliance or protection bargain is accepted.
- **HASUMI ↔ COMMITTEE:** in an insert Hasumi rages at Gehenna/Pandemonium while Tsurugi/Mashiro and generic members are present. The interrupted declaration and unknown occasion prevent a durable treaty-position or Koharu-hostage inference. Tsurugi now has a direct silent appearance, not a relational model.

## V003 C002 E002 relationship delta — intermediary, misfire and missed conversations

- **AZUSA ↔ BULLIED STUDENT/MARIE:** Marie carries an absent student's thanks and reports Azusa's intervention. Azusa acknowledges resistance to group bullying, but the student's experience and the exact Justice escalation are not directly witnessed here. Azusa's trap leaves Marie coughing and startled; she receives Azusa's apology and still conveys the message. No injury assessment, lasting relationship or damage finding follows.
- **HANAKO ↔ MARIE/SISTERHOOD:** the two recognize each other and Hanako escorts Marie, who leaves an unfinished concern. Hanako minimizes their connection as `少しだけご縁`; no recruitment status, Seia knowledge or private history is disclosed. Marie is newly tracked `UNMODELED`.
- **HIFUMI ↔ HANAKO/SENSEI:** Hifumi asks Sensei to talk about Hanako, after her E016 old-paper report. The E002 concern remains unvoiced when Hanako arrives first; Hifumi's embarrassed reaction and scolding end with a clothing change, not an evaluation of Hanako's grades or intent.
- **HANAKO ↔ AZUSA/SENSEI:** Hanako seeks Sensei about Azusa, following Marie's visit, but is interrupted before saying why. The swimsuit tableau is a misunderstanding corrected by narration, not a verified intimate relationship or disclosure.
- **GROUP ↔ STUDY:** Hifumi praises Koharu's displayed mark and Azusa's near threshold, and the Momo Friends incentive matters to Azusa. A further shared mock and laundry proposal show ordinary cohabitation but neither homogeneous agreement nor joint academic success.

## V003 C002 E003 relationship delta — trust expands unevenly

- **HANAKO ↔ AZUSA:** Hanako's E002 intended consultation is now explicitly about Azusa's nights, apparent anxiety and health. She intends to talk to Azusa, not to denounce her; the student is absent and has not answered. Her later paperwork suspicion is a separate institutional inference, not proof she regards Azusa as guilty.
- **HIFUMI ↔ HANAKO:** Hifumi reveals shared expulsion exposure, confronts Hanako using the old answer-sheet report, and receives a self-confession plus apology/effort pledge. This expands mutual knowledge and accountability but not Hanako's private reason. Hifumi also shares Nagisa's coercive task with Hanako; Azusa/Koharu are not shown receiving it.
- **HANAKO ↔ SENSEI:** Hanako sees the adult's help as good faith under a misused authority, thanks them, and accepts their thanks for future effort. Neither concludes a standing alliance or adjudicates the adult's E015 deception.
- **KOHARU ↔ GROUP:** Koharu notices Hifumi/Hanako/Sensei together late and misreads the tableau; no hearing of secret sanctions or actual relationship change is represented.
- **HANAKO ↔ NAGISA/MIKA:** she infers Nagisa may have designed the club and discounts Mika as likely architect. Her Koharu-hostage guess converges independently with Mika E001, not from a shown conversation with Mika or the selection record.

## V003 C002 E004 relationship delta — disclosed affection, partial disclosure

- **AZUSA ↔ HIFUMI/KOHARU/GROUP:** Azusa calls study with Koharu and Hifumi's help enjoyable; Hifumi hugs her and Azusa complains of slight breathlessness. Shared ordinary life gains direct reciprocal evidence. This is not automatic knowledge of Azusa's secret plan or a settled school identity.
- **HANAKO ↔ AZUSA:** Hanako follows E003's concern with a direct request to reduce night watch and share trap-setting, and Azusa agrees to take care. The resulting assurance has not been tested; their trust remains exposed to the E002 Marie counterexample and Azusa's own future-betrayal fear.
- **AZUSA ↔ SENSEI:** Sensei calls her kind after she says she wants no peers hurt; Azusa pushes back against child treatment and voices possible betrayal. Adult approval is not a full confession, safety audit or protective bargain.
- **HIFUMI ↔ HANAKO/PAST:** Hanako repeats secondhand masked-swimsuit lore while Hifumi is silent; no new clubmate knowledge of Hifumi's V001 criminal-role label is shown.
- **GROUP ↔ LEISURE:** Koharu resists sexualized framing and suggests rest, but admits interest in a nearby walk; Sensei agrees and Azusa prepares. Narrator confirms they set out, not what they do or whether any rule is violated.

## V003 C002 E005 relationship delta — reciprocal secrecy, pressure and coercion

- **HASUMI ↔ KOHARU:** Koharu respects/fears Hasumi and worries about her reduced eating; Hasumi urges study, says she wants Koharu back in Justice Realization and expects Sensei help. Koharu wants to stay with her and promises effort while doubting quick improvement. This is direct relational support under the existing grade bar, not proof of Koharu's E015 claimed spy role.
- **HASUMI ↔ SENSEI/GROUP:** they meet at the dessert shop in reciprocal embarrassment. Hasumi suggests both ignore the other's deviation: group camp outing versus her parfaits. Sensei normalizes hunger and praises Koharu's mark, but no formal exception or promise to carry Koharu through the exam is voiced.
- **MAKOTO ↔ IROHA/HASUMI:** Makoto repeatedly ignores Iroha's corrections and objectifies Hasumi; Iroha attempts to preserve factual role assignment and de-escalate. No durable treaty relationship can be inferred from this one broken meeting.
- **ICHIKA ↔ HASUMI:** Ichika supplies a field alert and revises scale/target as data arrive; Hasumi initially overinterprets treaty risk, then hears the four-person aquarium account. Phone relationship is professional, private breadth absent.
- **GOURMET RESEARCH ↔ FUUKA:** Haruna/Junko/Akari/Izumi coordinate the tuna escape; Fuuka is gagged and vocalizes protest while Haruna falsely attributes consent. No voluntary cooking agreement or outcome is shown. All named newcomers remain `UNMODELED`.

## V003 C002 E006 relationship delta — temporary co-action, split flight

- **HASUMI ↔ KOHARU:** Hasumi invites/accepts Koharu beside her in a live response; Koharu is proud to join. Their bond carries through the academic access bar, but formal membership and grade condition remain unresolved.
- **HASUMI ↔ SENSEI/REMEDIAL GROUP:** Hasumi asks for a joint response to manage treaty optics, Sensei agrees with safety-first qualification, and Azusa/Hanako accept while Hifumi is surprised. This is a temporary coalition, not a newly defined club command hierarchy or completed safe operation.
- **HASUMI/ICHIKA ↔ TSURUGI:** Ichika says Tsurugi cannot be held once activated; Hasumi asks to stop her and later pursues. Tsurugi's direct vocal encounter with Junko supplies a narrow field cue, not full psychophysical characterization.
- **GOURMET RESEARCH:** Junko proposes separate flight, Haruna/Akari take it up and Izumi fears being abandoned. Akari appears staggering when Junko encounters her, then Junko meets Tsurugi. No durable betrayal/friendship break or final fate is shown.
- **FUUKA ↔ GROUP:** no E006 appearance; E005 gagged non-consent and safety question stay open.

## V003 C002 E007 relationship delta — a bridge between institutions

- **SENSEI ↔ HASUMI/HINA:** Hasumi entrusts Sensei with handoff to reduce Trinity–Gehenna friction; Hina recognizes the same political tactic from Gehenna's side. Sensei agrees, then speaks confidentially with Hina; exact briefing and durable cross-school agreement are unprinted.
- **SENSEI ↔ HINA:** Hina questions neutrality, retracts the accusation, receives a sensitive briefing and Hina's peace-treaty argument, then asks if Sensei will protect the club. Sensei explicitly says yes. Trust is reciprocal enough for disclosure but Hina calls the teacher's easy trust a bad trait; no motive for that aside is stated.
- **KOHARU ↔ HASUMI/GROUP:** Hasumi thanks the group and Koharu savors first combat beside her, feeling useful. This deepens belonging despite her formal grade bar. Hanako gently returns her to academic effort; no reinstatement or official pass.
- **GOURMET RESEARCH ↔ GEHENNA AUTHORITY:** Haruna/Junko/Akari expect/undergo transfer; Hina postpones Haruna's explanation, Akari asks Sena for an arm exam, and Fuuka is relieved. Izumi absent, no full reconciliation or medical outcome.
- **SENA ↔ HINA:** Hina identifies Sena's Emergency Medicine role as less politically exposed, Sena calls Hina Prefect chair and focuses on loading/injury language. One professional encounter, no private breadth; Sena new `UNMODELED`.

## V003 C002 E008 relationship delta — self-named friendship and renewed pressure

- **AZUSA ↔ HIFUMI:** Azusa accepts Hifumi's choice of Peroro Doctor, thanks her and explicitly calls it the first present she has received from a friend. Hifumi credits Azusa's work and is pleased, although surprised by the intensity of Azusa's vow. This is a direct current friendship appraisal, not evidence of lifelong gift retention or an explanation of E017's plan.
- **HIFUMI ↔ HANAKO:** Hifumi is relieved by Hanako's 69-point mock and says she still does not know Hanako's prior burden; Hanako thanks her in a label-unstable exchange. Care is clear, but intimacy does not equal motive disclosure.
- **REMEDIAL GROUP ↔ SENSEI:** all four celebrate mock passes and resume study, with Sensei announcing results/encouraging. The prospective official examination and collective-sanction threat remain separate from club morale.
- **NAGISA ↔ SENSEI/MIKA:** Nagisa again solicits a traitor judgment; Sensei maintains their own-method boundary. She asks about Mika's contact, but no answer, disclosure or changed alliance is shown. Nagisa's possible knowledge source is unknown.

## V003 C002 E009 relationship delta — affection inside coercive sorting

- **NAGISA ↔ HIFUMI:** Nagisa directly says she values and likes Hifumi yet fears an alleged criminal-leader identity. This is an internally conflicted attachment, not evidence Hifumi led the group or that Nagisa knows her heart. V001's imposed “Faust” role remains separate from present private motives.
- **NAGISA ↔ KOHARU/HASUMI:** Nagisa describes Koharu as leverage to constrain Hasumi's Gehenna hostility. No evidence Koharu consented, Hasumi was told, or the leverage mechanism was formally documented.
- **NAGISA ↔ SENSEI:** Sensei refuses suspicion as a use of time, starts to defend Hifumi and diagnoses selective distrust; Nagisa interrupts, insists on expulsion and then says each will strive in their own way. This is adversarial but not a permanent interpersonal rupture or a cancellation of her sanction plan. Choice `009` alternatives should not be merged into one spoken bargain.
- **REMEDIAL GROUP:** the four are absent from this conversation. E008's real friendship and mock hope coexist with Nagisa's portrayal; no group member is shown hearing this rationale or the threatened next step.

## V003 C002 E010 relationship delta — separation fear and equalized warning

- **AZUSA ↔ CLUB:** Hifumi's imagined graduation prompts Azusa's sadness; Hanako says their same-school ties could continue, and Koharu offers future classroom contact. These are authentic prospective care gestures, not a completed reunion or proof Azusa's future course.
- **SENSEI/HIFUMI/HANAKO ↔ KOHARU/AZUSA:** Hanako's expulsion reference elicits first-heard shock; Sensei explains from the beginning and Hifumi apologizes for concealment. The hidden sanction is now at least partly shared, while exact unprinted explanation and separate Nagisa/Mika intelligence remain partitioned.
- **AZUSA ↔ GROUP:** Azusa takes a lead in timekeeping, departure and route breakthrough. Others follow while frightened or joking. This is situated emergency coordination, not a permanent command hierarchy.
- **CLUB ↔ GEHENNA STRANGERS:** generic thugs target the Trinity uniforms for prospective ransom. The party passes after a confrontation, with no durable tie, known casualty or new character identity.

## V003 C002 E011 relationship delta — uneasy aid and renewed captivity

- **SENSEI/REMEDIAL CLUB ↔ GOURMET RESEARCH:** Haruna/Akari choose to guide the group through Gehenna, presenting it as thanks for an earlier encounter, while Junko/Izumi coordinate remotely under pursuit. Sensei thanks them and Hifumi is confused. The temporary help does not erase earlier aquarium conflict, establish a durable alliance or certify everyone's safety after the vehicle enters the river.
- **FUUKA ↔ GOURMET RESEARCH:** Fuuka is bound/gagged in the car trunk and later explicitly asks to get out. Akari's loan/friendship and Haruna's cheering glosses are false against her protest. No consent repair or release is shown.
- **REMEDIAL GROUP ↔ EACH OTHER/SENSEI:** chaotic diversion separates Azusa/Hanako from Hifumi/Koharu and Sensei for a time. All reunite at the advertised venue by 2:45, with Sensei expressing relief; later all share the lost-paper failure. Exact routes and enduring post-failure support remain open.
- **NAGISA ↔ GROUP:** a recorded message delivers instructions and an asserted monitoring claim but is not interactive. No one receives a direct answer from her, and her relationship to the unknown Hot Spring tip is not established.

## V003 C002 E012 relationship delta — shared fear and peer rest

- **KOHARU ↔ CLUB/HASUMI:** Koharu now directly voices the “traitor” suspicion and fears a lost Justice Realization future. Hifumi, Azusa and Hanako respond with concern, not a resolution of her committee status. Her breakdown is not evidence that she rejects their friendship.
- **HIFUMI ↔ HANAKO:** Hifumi takes responsibility for finding a last-chance method and is visibly exhausted. Hanako offers help with Koharu's study and Hifumi's burden, urging rest. This deepens E003/E008 reciprocal care without disclosing Hanako's own hidden motive.
- **SENSEI ↔ NAGISA/GROUP:** Sensei inwardly blames their Nagisa words; Hanako says the teacher acted for the students based on an account she heard. The exact account and present dialogue remain unprinted. Attempts to find Nagisa/Mika fail, so no new direct relational settlement with either occurs.
- **AZUSA ↔ CLUB:** Azusa says a premature farewell turned into a return to camp and stays quiet amid Koharu's anger. Silence cannot establish agreement, guilt or plan change.
## V003 C002 E013 relationship delta — visible club care, private command

- **HANAKO ↔ REMEDIAL CLUB:** Hifumi directly credits Hanako's patient teaching, while Hanako credits the students' work and recommends rest. Her perfect mock marks and noticeboard watch coexist with E003's still-private earlier motive. Silent tags near the private exchange do not establish that she knows its content.
- **AZUSA ↔ HIFUMI/KOHARU/HANAKO/SENSEI:** Azusa accepts the group's rest counsel and joins a spoken commitment to pass. Her later Saori call is not shown to the others; the apparent coexistence of club belonging and hidden obligation is not proof she has chosen the latter.
- **SAORI ↔ AZUSA:** Saori gives a fixed next-morning order and invokes shared `vanitas vanitatum` language. Azusa raises risk/unfinished preparation, then says she will prepare. This supports an asymmetrical command relation with room for hesitation, not unqualified enthusiasm, completed obedience or freely consented violence.
- **SAORI/AZUSA ↔ NAGISA/SEIA:** Saori names Nagisa's halo as target and compares the requested act with Seia. The episode gives no direct Nagisa/Seia encounter and no independent Seia-event verification.
## V003 C002 E014 relationship delta — confession receives a counteroffer

- **AZUSA ↔ CLUB/SENSEI:** Azusa confesses false papers, original Arius mission and hidden counterdecision, shakes and asks to be hated. Hifumi/Koharu are shocked and confused; Sensei rejects her claim of sole fault. Hanako first presses the betrayal and later apologizes, recognizes her confession/attachment and offers a joint path. The club's final trust outcome is not yet tested in action.
- **AZUSA ↔ ARIUS/SAORI/NAGISA:** Azusa says she has falsely reassured Arius while intending to protect Nagisa, a self-described double-agent position. E013 Saori's command and E014 Azusa testimony support conflict, but no completed defection, direct Nagisa contact or rescue is shown.
- **HANAKO ↔ AZUSA/CLUB:** Hanako's painful interrogation gives way to empathy through a self-identifying account of elite pressure and attempted departure. Her specific inference that Azusa stayed for shared ordinary joy is tentatively accepted by Azusa. Hanako now asks the group to let her devise a way to defend Nagisa and pass together; no tactic or unanimous operational commitment is yet printed.
- **KOHARU ↔ HASUMI/JUSTICE:** Koharu wants to explain; Hanako argues Hasumi might lack context and incur expulsion for helping. This is fear for a mentor/committee bond, not a confirmed Hasumi refusal or rule.
- **MIKA ↔ ARIUS/NAGISA:** Azusa says Arius deceived Mika but lacks details; Hanako posits future blame-shifting. Mika's own E001 forged-admission and reconciliation account remains distinct and unadjudicated.
## V003 C002 E015 relationship delta — coercive performance and active defection

- **HANAKO ↔ NAGISA:** Hanako reaches Nagisa's refuge, commands her to stay still and confronts her over Hifumi/Koharu. Nagisa admits she may have hurt Hifumi yet refuses regret. Hanako's staged Hifumi-friendship message deliberately shocks her; promised later clarification is not observed. This is adversarial pressure, not reconciled dialogue.
- **AZUSA ↔ NAGISA:** Azusa says she secured Nagisa through close-range full-magazine fire and expects temporary unconsciousness. Protective strategic aim and serious direct violence coexist; no healing, consent or safe custody is shown.
- **AZUSA ↔ ARIUS:** Arius commander expects its “spy,” then team IV reports her betrayal and ambush. Azusa says she took their target and needs to reach the exam. This is observed active defection from Arius's immediate mission, not proof she defeated the force.
- **HANAKO ↔ AZUSA:** Hanako assigns diversion; Azusa reports old traps/trenches and accepts a later regrouping point. Their co-plan is underway but the future rendezvous and “real traitor” hypothesis remain untested.
- **HIFUMI ↔ NAGISA:** Hifumi is absent. Nagisa's conditional remorse is spoken to Hanako; Hanako's false message cannot be imputed to Hifumi or treated as a relationship-ending statement.
## V003 C002 E016 relationship delta — shared stand, hidden target

- **AZUSA/HANAKO/HIFUMI/KOHARU ↔ ARIUS:** Azusa leads the enemy into a prepared camp defense; Hanako recognizes attrition, and the commander faces a four-student gym stand. The late dialogue tags are corrupted, so exact individualized battle declarations and durable hierarchy remain open. No defeat or reconciliation is printed.
- **AZUSA ↔ NAGISA:** Arius says Azusa carried the target into camp; Azusa says Nagisa is hidden. Location is narrowed, but care, consciousness and consent remain unknown after E015's gunfire.
- **REMEDIAL CLUB ↔ SENSEI:** Sensei is present and answers “waiting,” with final encouragement inward. This supports shared exposure/solidarity, not sole adult command or demonstrated rescue.
- **ARIUS COMMANDER ↔ “SQUAD”:** he reports contact and says Squad has a separate task; neither specific members nor their action are shown. The line cannot be used to import later relations or motives.
## V003 C002 E017 relationship delta — Mika names the hidden alliance

- **MIKA ↔ NAGISA/SEIA:** Mika says she targeted Nagisa to stop a real peace treaty, intended her removal/confinement, and ordered Seia attacked while denying lethal instruction. Their prior friendship and Seia's condition cannot neutralize the direct hostile order; neither target is present to answer.
- **MIKA ↔ ARIUS/AZUSA:** Mika claims she secretly supported Arius as future armed backing for hostship and war, and explicitly intends Azusa as scapegoat for Nagisa's assault. The corrupted `u:0055-0060` labels caution exact speech attribution but not the surrounding Mika-context plan. Azusa's interrupted Seia response gives no full counter-history.
- **MIKA ↔ SENSEI/REMEDIAL CLUB:** Mika admits deceiving Sensei about treaty nature, asks for Nagisa, threatens to eliminate obstacles, and recognizes Schale resistance as troublesome. Hifumi credits Sensei's earlier command against a local Arius group; no observed Mika defeat or negotiated settlement.
- **KOHARU ↔ HASUMI/JUSTICE:** Koharu says she sent Hasumi a message. Hanako expects Justice action, while Mika claims a stand-down; the reply and actual decision are absent.
- **SISTERHOOD ↔ CONFLICT:** an Arius student identifies approaching cathedral-side students questioningly as Sisterhood. This suggests autonomous intervention but does not yet prove membership, alliance or outcome.
## V003 C002 E018 relationship delta — surrender without completed repair

- **HANAKO ↔ SISTERHOOD:** Hanako says a small promise enabled intervention; Sisterhood declares it will cross custom and seek Mika's custody. Mika asks what Hanako paid, but Hanako does not answer. No durable bargain terms or individual Sakurako/Marie authorship can be reconstructed from conflicted labels.
- **MIKA ↔ SEIA:** Mika admits concern/relief when Hanako reports Seia lives but remains unconscious and wounded. Mika's accident/frailty account is self-defense, and no Seia response, apology exchange or verified medical record appears.
- **MIKA ↔ SENSEI/CLUB:** after defeat Mika calls Sensei the overlooked variable, says inviting Schale was her mistake, surrenders and recalls genuine happiness at a prior supportive sentence. Sensei's current echoes are inward; Mika declines current dialogue. Surrender does not repair Nagisa/Seia/club harm.
- **MIKA ↔ AZUSA/SAORI:** Mika warns Azusa of Trinity nonprotection and Saori pursuit; Azusa acknowledges risk and vows to resist. Threat is unproven future, not an accomplished estrangement or capture.
- **SISTERHOOD ↔ TEA PARTY:** the declaration explicitly calls intervention in Tea Party infighting contrary to prior custom. Its institutional independence is exercised here, but legal authority, arrest completion and future relation are open.
## V003 C002 E019 relationship delta — shared academic vindication

- **FOUR REMEDIAL STUDENTS ↔ EACH OTHER:** after night-long strain, Azusa pushes the group to the venue; Hifumi steadies Koharu, and all pledge to persist. Narrator certifies all four third official passes. This is joint academic success, not proof of identical study contribution or future permanent club identity.
- **KOHARU ↔ HASUMI/JUSTICE:** a Justice member welcomes the group and relays Hasumi's encouragement, apology and promise of later repair. Hasumi's direct knowledge/action and Koharu's grade-based return remain unprinted.
- **SENSEI ↔ CLUB:** Sensei accompanies and offers two singleton prompts. The result fulfills a pass-oriented promise in outcome, but neither exclusive adult causation nor formal disciplinary settlement is shown.
- **HANAKO ↔ AZUSA:** Hanako says Azusa taught her not to give up, reversing E013's teacher-credit direction. It marks mutual influence without resolving their distinct Arius/elite-track futures.

## V003 C002 E020 relationship delta — reported distance and threatened return

- **SEIA ↔ REMEDIAL CLUB:** in a locationless Sensei-addressed frame Seia credits the four's own pass and interprets their likely individual continuities. She does not exchange speech with them, and her future readings are not their confirmed post-exam choices.
- **SEIA ↔ MIKA/NAGISA:** Seia reports Mika imprisoned and fears they may never meet; she expects Nagisa to sign. Neither party replies. Seia's earlier injury report is not resolved by this framed voice.
- **SAORI ↔ AZUSA:** Saori addresses absent Azusa with an inescapability/body-memory claim. This contests Azusa's E014 declared defection and E018 resistance but shows no capture, submission or future contact.
- **SAORI ↔ HIYORI/MISAKI/ATSUKO:** Saori commands preparation and quiets discussion; Hiyori voices anxiety, Misaki gives a suffering-as-life response and mediates a possible “princess” question. Atsuko appears silently, but exact sign content and whether Misaki-tagged silence should be reassigned remain uncertain. These are narrow group dynamics, not a complete hierarchy or private relationship model.

## V003 C002 canonical checkpoint reconciliation

The [C002 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C002_CHECKPOINT.md) recognizes the four-student collective pass, Azusa–Hifumi gift and Hanako–Azusa reciprocal influence as actual relationship evidence. It does not assert permanent club identity, a repaired Mika–Seia/Nagisa bond, completed Hasumi–Koharu reinstatement or Azusa's safety from Saori. C003 E001 remains unopened.

## V003 C003 E001 relationship delta — retention without conscription

- **MARIE ↔ HANAKO:** Marie says she sought Sakurako's help to keep Hanako from leaving and apologizes for not understanding her; Hanako apologizes for worry and says she no longer plans withdrawal. This is reciprocal care/repair, not a formal enrollment record.
- **SAKURAKO/SISTERHOOD ↔ HANAKO:** Sakurako expects future political assistance, explicitly disclaims forced Sisterhood membership and unreasonable demands. Hanako accepts “that much” while making a deliberately false nudity-rule joke. Scope/duration of future help unknown.
- **SENSEI ↔ HANAKO:** Sensei claims her as a student and asks whether she dislikes the arrangement; these are spoken singleton choices supporting a consent boundary, not control over Sisterhood.
- **SEIA ↔ AZUSA/MIKA/MINE:** dream-framed Seia/visitor exchange suggests advice sought amid a lethal assignment; exact act and conversation unresolved. Sakurako says Mine hid Seia from a Tea Party information channel contaminated by Mika, preserving the earlier separation without direct Mine voice.
- **HIFUMI ↔ AZUSA:** Hifumi is silently present when an inspector calls Azusa; no assistance, testimony or ruling yet.

## V003 C003 E002 relationship delta — apology and a prison threshold

- **AZUSA ↔ SEIA/MINE:** Azusa says Seia advised a fake-death explosion and designated Mine, whom Azusa trusted for concealment. Seia's represented refusal to endorse Azusa's ideas coexists with offered wisdom; Seia's continued sleep remains a cost and no direct present reply appears.
- **SAKURAKO/SISTERHOOD ↔ AZUSA:** Sakurako publicly guarantees/regularizes Azusa's Trinity papers, naming her a formal student; this is an institutional protective act, not a personal fully observed bond.
- **NAGISA ↔ HIFUMI:** in a Hifumi-sourced retrospective Nagisa apologizes for suspicion, and Hifumi says she does not hate her. Nagisa's self-comparison and an italic “friendship game” echo show how the injured relation cannot be called fully reset.
- **NAGISA ↔ HANAKO/SENSEI:** Hanako says Nagisa apologized to her; Sensei wishes to help, neither line proving broader restoration. Hanako doubts a single Gehenna-hatred explanation for Mika.
- **NAGISA ↔ MIKA:** direct Trinity-prison visit begins; Mika is surprised Nagisa came, Nagisa asks about conditions. No forgiveness, confession expansion or release is printed.

## V003 C003 E003 relationship delta — contact without mind access

- **NAGISA ↔ MIKA:** the prison conversation confirms childhood closeness, Mika's surprise at the visit and Nagisa's hurt/anger at targeting her and Seia. Nagisa says her original hunt sought to spare Mika isolation if she fell; Mika insists hatred/suspect betrayal are sufficient motives. Nagisa leaves without reconciliation.
- **MIKA ↔ SENSEI:** Mika says Sensei has repeatedly sought a prison visit and she refused, interpreting noncompulsion as consistent with Sensei. This is Mika's report, not access records or completed visit.
- **HANAKO ↔ MIKA:** Hanako raises an unproven gentler-first-plan/panic and Nagisa-protection theory, provoking Mika's resistance and Seia-survival doubt. Hanako promises secrecy then shares with Sensei, admits hurt and considers apology; trust boundary not repaired.
- **SENSEI ↔ HANAKO/STUDENTS:** Sensei's choices argue for teacher trust despite betrayal risk and continued effort, while the key “believe paradise” and future Nagisa/Mika visits are inward. Hanako accepts mutual outreach without knowing outcome; no actual new visit.

## V003 C003 E004 relationship delta — formal and private channels

- **HASUMI/MASHIRO ↔ KOHARU/JUSTICE:** Hasumi thinks of Koharu for a callout then remembers she is ill at home; Mashiro says she remains remedial-club assigned. Care/recognition is not yet reinstatement.
- **HANAKO ↔ SISTERHOOD:** Hanako works for days sorting documents; Marie apologizes for her fright, Hinata banter is label-unstable. Practical help continues without an observed new bargain.
- **SENSEI ↔ MAKOTO/IROHA:** Makoto mistakes first formal encounter for anti-Prefect alliance; Iroha corrects on Sensei's behalf. No mutual political alignment is shown.
- **SENSEI ↔ AKO/HINA:** Ako is startled by untracked Trinity visit, Hina escorts Sensei and connects their perspective-taking to trust. Sensei explicitly says they trust Hina; Hina says only Sensei knows of her wish to rest. This is a bounded private disclosure, not actual retirement.

## V003 C003 E005 relationship delta — friendship after exam

- **HIFUMI ↔ AZUSA:** Azusa retains/values Hifumi's first-friend Peroro gift; a future outing is discussed. Azusa's wound-aware critique still affirms Hifumi's preferred happy ending. No completed outing.
- **HANAKO/HIFUMI/AZUSA ↔ KOHARU:** Hanako invites her as a continuing club companion; Koharu says she will stay with Justice and welcomes visits. Reciprocal attachment is not an official reinstatement.
- **FOUR STUDENTS ↔ SENSEI:** they wish to talk after the ceremony; Sensei is separately in the cathedral hall. No encounter in this unit.
- **SHINON ↔ FEDERAL COUNCIL:** Shinon airs and skeptically glosses a prior-day Rin/Momoka/Ayumu clip, a mediated public relation, not private motive access.

## V003 C003 E006 relationship delta — recognition and divided duty

- **Tsurugi/Hinata ↔ Sensei:** Tsurugi identifies Sensei to rival security members, then responds modestly; Hinata de-escalates and guides a tour. Inward thanks/replies remain representation-cautioned.
- **Hinata ↔ Sisterhood/Sakurako:** Hinata says she and others follow Sakurako's instruction to help guide/guard, and articulates a tentative organizational turn after the earlier crisis. No new mandate document.
- **Hina ↔ Ako/Makoto:** Ako worries about Hina personally after prospective ETO constraints on Makoto; Hina assures committee continuity but defers the personal issue. Makoto's airship/car taunt sustains antagonism, not alliance.
- **Saori ↔ Squad/Atsuko:** Saori assigns Misaki/Hiyori teams, addresses Atsuko `姫` and asks her to endure discomfort; the silent gesture cannot specify her consent, task details or feelings. Group coordination is direct, outcome open.
- **Azusa ↔ Hifumi/Koharu/Hanako:** Azusa abruptly leaves without explaining while peers speculate. Her Saori suspicion is inward; no spoken warning or return occurs here.

## V003 C003 E007 relationship delta — searching and rescue under attack

- **HIFUMI/KOHARU/HANAKO ↔ AZUSA/JUSTICE:** Hifumi seeks absent Azusa and Koharu fears for seniors; Hanako tries to prevent risky separation. Her safety estimate is not proof of either party's condition.
- **HINA ↔ AKO/SENSEI:** Hina inwardly deems Ako safe and shifts attention to Sensei while Arius troops block her. No direct reunion or successful rescue by Hina.
- **MAKOTO ↔ IROHA/ARIUS:** Makoto claims a prior Arius alliance and false treaty assent; Iroha questions trust and calls her deceived. The airship gift/boxes dramatize asymmetry, without inspected agreement or known personal outcomes. Ibuki is present on the gift vessel but her fate is unshown.
- **ARONA/HINATA/HASUMI/TSURUGI ↔ SENSEI:** Arona reports attempted protection, Hinata extracts Sensei, Hasumi prioritizes evacuation, and Tsurugi stays to hold attackers. These are distinct acts, not a single savior story.
- **HASUMI ↔ TSURUGI:** Tsurugi checks Hasumi's retaliation impulse; Hasumi accepts the correction and protects Sensei while Tsurugi engages. Later strange-opponent encounter has unclear continuity.
- **MIKA ↔ NAGISA:** Mika's unlocated `ナギちゃん？` expresses alarm, not evidence of Nagisa's status or Mika's physical presence.

## V003 C003 E008 relationship delta — handoff across rival schools

- **MAESTRO ↔ ARIUS/ATSUKO:** Maestro accepts limited aid in exchange for underground guidance, cites copied guardians and royal-blood activation. Arius student addresses Atsuko about a successful “doll” transaction. Her exact consent/task remains opaque.
- **HINA ↔ HIYORI/MISAKI:** Hiyori reports being defeated before mimesis appeared; Misaki sees Hina reach the escape group. No stable post-combat relation or capture.
- **HASUMI/TSURUGI/HINATA ↔ SENSEI/HINA:** three choose rear-guard protection and ask Hina to take Sensei; Hina accepts. Sensei objects then begins moving. Cooperation is bounded to crisis, not a repaired Gehenna–Trinity relationship.
- **HINA ↔ SENSEI:** Hina visibly injured yet directs Sensei to stay close and promises to open a route; Sensei notices the wound. No completed exit or clinical status.

## V003 C003 E009 relationship delta — protective escape and contested belonging

- **HINA/SENA ↔ SENSEI:** Hina rallies to bring emergency vehicle/Sena; Sena takes Sensei, diagnoses a non-vital but bleeding gunshot and starts first aid. Misaki reports escape; no final recovery.
- **SAORI ↔ SENSEI:** Saori identifies Sensei as predicted obstacle, fires or commands fire in a context where she later says a bullet hit; Sena independently confirms gunshot. Her expectation of death is not outcome.
- **SAORI ↔ AZUSA:** Azusa returns to demand why Sensei was targeted; Saori weaponizes “killer/no home” and futility, challenges her to fight. No duel result or proved rejection from Trinity.
- **ATSUKO ↔ HIYORI/SAORI:** Hiyori mediates silent Atsuko's apparent view that Sensei disrupted plan and Azusa mattered; exact sign content and unnamed forecast source remain uncertain.
- **SEIA ↔ SENSEI:** Seia introduces herself in an expressly uncertain dream and says time is twisted; no verified waking meeting, physical location or causality.
- **HINA ↔ HIYORI/MISAKI:** Hiyori intercepts again, Misaki calls Hina fallen, but Hina acts thereafter. No permanent defeat or reconciled force relation.

## V003 C003 E010 relationship delta — coerced belonging and reciprocal suspicion

- **SAORI ↔ AZUSA:** Saori wins an initial frontal exchange, then alternates tactical correction, exclusive-home claim and halo-destruction challenge. Azusa asks purpose, infers force motive while Saori asks whether she will flee; no exit, reconciliation or final duel is shown.
- **SAORI ↔ SENSEI:** Saori calls Sensei a lying adult and believes they were disposed of. E009 Sena's immediate treatment remains the last medical observation, not displaced by her claim.
- **SEIA ↔ SENSEI:** in dream framing Seia explains promise mechanics while admitting observation through Sensei's dream, not prior omniscience; no physical meeting.
- **ATSUKO ↔ SAORI/AZUSA:** Atsuko gestures a possible intervention, Saori tells “Princess” not now; tag inversion and no sign transcription keep the proposal uncertain.
- **TRINITY RESERVES ↔ GEHENNA RESERVES/AKO:** each blames the other for Arius violence; Ako simultaneously orders casualty rescue and urgent Hina search despite her wound. No school-to-school perpetrator finding.

## V003 C003 E011 relationship delta — separation for local duties

- **HIFUMI ↔ AZUSA/HANAKO/KOHARU:** Hifumi chooses to search Azusa and urges friends to answer separate emergency duties; she promises contact if found, but no sighting/return occurs.
- **MARIE/SAKURAKO ↔ HANAKO:** Marie says Sakurako privately designated Hanako as acting Sisterhood commander if absent and guarantees it to officers. Hanako accepts coordination; written mandate and Sakurako's fate unverified.
- **KOHARU ↔ JUSTICE:** a member calls her back and she identifies confiscated-items room as post; current participation is observed, formal club-status change not.
- **SENA ↔ RESCUE KNIGHTS/SUZUMI:** Sena's Gehenna ambulance is defended by Trinity healers and vigilante; care crosses school border before they learn Sensei's identity. No ongoing intergroup arrangement or hospital handoff.
- **SUZUMI ↔ REISA:** Reisa briefly calls for a shared vigilante moment; Suzumi departs on patrol, so no joint action shown.
- **MIKA ↔ NAGISA/SEIA:** Mika's unlocated speech to Nagisa invokes Seia's story frame; it supplies neither contact nor medical knowledge.

## V003 C003 E012 relationship delta — concern without direct contact

- **HANAKO ↔ SENSEI:** Hanako asks urgently about Sensei and hears relayed treatment/unconsciousness status. Relief and worry coexist; no visit or direct Sensei reply.
- **HANAKO ↔ MARIE/SISTERHOOD:** an analyst supplies preliminary launch/video information; Hanako identifies the apparent guardians and exposes her own severe but explicitly tentative theory to Marie. Marie does not confirm it.
- **HINA ↔ HANAKO/EVIDENCE:** the analyst's non-ramjet result corrects Hina's earlier inward guess without a direct meeting or moral judgment of Hina.
- **TRINITY ↔ GEHENNA:** Sisters reportedly still fight Gehenna while evidence suggests launch inside Trinity district; neither fact proves a school sanctioned the Arius strike.

## V003 C003 E013 relationship delta — protective exclusion versus unfinished promise

- **AZUSA ↔ HIFUMI:** Azusa meets Hifumi, thanks her and says goodbye while insisting a “good” friend cannot follow into her intended lethal act. Hifumi disputes her self-blame, asks her not to go and cites a still-unfulfilled group sea promise and Peroro viewing. This is an acute unilateral separation, not certified termination of friendship or a completed pursuit.
- **AZUSA ↔ SAORI:** Azusa announces an intent to destroy Saori's halo. Saori is not present, and no attack or outcome is shown.
- **AZUSA ↔ SENSEI/SEIA/CLUB:** she assigns herself responsibility for Sensei's shooting, Seia's coma and risks to the club. This exposes guilt and protective motive, not sole causal proof; her gratitude confirms the club's emotional importance alongside formal Trinity membership.
- **SEIA ↔ HANAKO/HIFUMI:** Seia comments on their inferred understanding without direct contact in this unit; neither hears her verdict here.

## V003 C003 E014 relationship delta — tutor, pursuer and gift

- **SAORI ↔ AZUSA:** Saori claims ownership of Azusa's training and predicts her moves; Azusa ambushes her, escapes local capture, challenges the origin of Arius hatred and apparently uses the plush as a deceptive carrier. The conflict does not end with a confirmed death, conversion or reunion.
- **AZUSA ↔ HIFUMI:** Hifumi is absent but her first-friend gift remains physically and emotionally salient. Saori threatens Hifumi and misreads the dropped plush as pure sentimental bait; Azusa's later apology to Hifumi does not disclose Hifumi's knowledge or reaction.
- **SAORI ↔ ATSUKO/MISAKI/HIYORI:** Saori protects/warns Atsuko, but her order to pursue draws the team into traps and collapse. Misaki interprets Atsuko's gestures and reports inability to move; no final condition or team split is established.
- **AZUSA ↔ ATSUKO:** Atsuko blocks Azusa and makes an untranscribed gesture; Azusa refuses. The offer's content and their prior bond cannot be reconstructed from the sign alone.

## V003 C003 E015 relationship delta — a teacher challenges Seia's withdrawal

- **SENSEI ↔ SEIA:** in the dream frame, Sensei asks whether Seia actually saw the sequel, offers an interpretation that fear kept her in dreams and says they must return to students. Seia resists, warns of an unhealed body, then chooses to observe the remainder. The exchange shows influence without proving fear caused coma, either person physically woke, or future rescue succeeded.
- **SEIA ↔ AZUSA:** Seia says she warned Azusa repeatedly and now reads hope as failed. Azusa is not present to confirm the exact warnings or accept that verdict; E014's outcome remains untouched.
- **SENSEI ↔ STUDENTS:** Sensei inwardly prioritizes help and promises to return, an intention rather than direct contact with Hifumi, Azusa or other students in this unit.

## V003 C003 E016 relationship delta — protection and refused instrumentality

- **AZUSA ↔ SAORI/ATSUKO:** Seia says Atsuko shields Saori from Azusa's detonation; both survive injured. Saori now vows retaliation. Azusa recognizes their survival and remains intent on stopping Saori; no final reconciliation or death.
- **MIKA ↔ PATER FACTION:** militants release/approach Mika expecting her to command war in their name; she refuses while admitting personal dislike. They turn hostile. The relation is not support or lawful restoration of her Tea Party authority.
- **KOHARU ↔ MIKA/JUSTICE:** a Justice member says Koharu may not yet return formally but sends her toward prison; she intervenes against group assault on Mika. Moral choice is direct, official reinstatement absent.
- **HANAKO ↔ PATER/SISTERHOOD:** Hanako challenges the faction's collusion theory and war procedure, and they order her seized; custody unshown. Marie learns Sakurako is gravely ill by report, no contact.
- **SENSEI ↔ SERINA/HANAE/SEIA:** Serina/Hanae address awakened Sensei and Hanae opposes movement for medical reasons. Seia's questions accompany the crosscut, without proof of physical contact or waking recovery for her.

## V003 C003 E017 relationship delta — indirect repair, direct protection

- **KOHARU ↔ MIKA/SENSEI:** Koharu defends Mika despite uncertainty and receives Sensei's direct praise; Mika witnesses. No formal Justice reinstatement or durable Mika–Koharu alliance is established.
- **SENSEI ↔ MIKA:** Sensei checks her wellbeing and listens while she struggles to explain her refusal, then inwardly promises help. No confession hearing, absolution or medical rest clearance.
- **MIKA ↔ SEIA/NAGISA:** Mika apologizes to Seia and wants to meet both friends; Seia, in crosscut, admits she underestimated Mika and says she forgives her. This is not a delivered bilateral exchange or Nagisa's reconciliation.
- **MIKA ↔ ARIUS/GEHENNA:** apparent recollection supplies an initial tea/friendship proposal for Arius, later possible anti-Gehenna instrumentalization and host rationale. Her present hatred remains but she declines militants' proxy command; neither feeling nor faction loyalty is settled.
- **SENSEI ↔ TRINITY PARTIES:** Tea Party/Sisterhood/Justice voices recognize Sensei's reappearance, while Hanako/Marie/Koharu respond; their willingness to rely on Sensei is not a completed joint plan.

## V003 C003 E018 relationship delta — friends re-form around Azusa

- **HIFUMI ↔ AZUSA:** Hifumi says Azusa fights alone and repeats the “different place” exclusion, then commits to reach her and tell her directly she disagrees. No new face-to-face contact or accepted reply yet.
- **HIFUMI ↔ KOHARU/HANAKO/SENSEI:** Koharu speaks from loneliness and refuses to abandon Azusa; Hanako pledges to accompany, and Sensei praises Hifumi's leadership/offers continued help. The group's plan is joint, not executed.
- **SENSEI ↔ SENA/INJURED ALLIES:** Sensei thanks Sena for care, checks Hasumi/Tsurugi/Chinatsu/Ako/Iori and accepts Ako's request to look for Hina. Medical status and search result remain open.
- **AZUSA ↔ SAORI:** a renewed direct challenge invokes Atsuko's injury and Azusa's willingness to kill; neither embraces the other or wins in the printed unit.
- **SEIA ↔ TRINITY/GEHENNA:** she narrates growing mutual reliance, but no specific bilateral accord or Seia physical meeting is shown.

## V003 C003 E019 relationship delta — crossing worlds, allowing rest

- **HIFUMI ↔ AZUSA:** Hifumi directly reaches Azusa, asserts she will be beside her despite rejection and uses Faust mask history to refuse the separate-world premise. Azusa hears and questions whether it is a lie; acceptance/long-term repair still open.
- **HIFUMI ↔ ABYDOS:** Hoshino, Shiroko, Nonomi, Serika and Ayane arrive in solidarity and reprise shared Black Market lore with comic exaggeration. No standing command hierarchy under “Faust” is established.
- **SENSEI ↔ HINA:** Hina admits exhaustion, comparison to Hoshino and wanting recognition; Sensei thanks/apologizes and permits rest. She retracts “retirement,” rejoins Ako and waits for direction. No proof wounds healed or her need fully resolved.
- **SENSEI/HIFUMI ↔ TRINITY/GEHENNA ALLIES:** Justice/Prefect actors assemble around them; tag inversions obscure some exact lines, and arrival is not a signed peace agreement.
- **AZUSA/SAORI ↔ JUSTINA/ETO:** Saori's claim of endless guardians is challenged by Sensei's rival ETO declaration and reported control confusion; no finished side-switch or surrender.

## V003 C003 E020 relationship delta — accepted help across schools

- **HINA ↔ HASUMI/TSURUGI/CHINATSU/IORI:** Hina sets a western task, Iori accepts, Hasumi offers Justice aid and Tsurugi is present; Hina agrees. Hasumi recalls prior joint work with Chinatsu without naming its exact earlier scene here.
- **HINA ↔ HOSHINO/SERIKA:** Hoshino offers Abydos help, requests name rather than title; Serika points out Hoshino's reciprocal title habit. Hina accepts their help but no deep personal exchange or battle result occurs.
- **SENSEI ↔ COALITION:** Sensei is not directly heard in E020. The students' assent should not be retroactively turned into an explicit order from Sensei.
- **AZUSA ↔ HIFUMI/SAORI:** not directly advanced in this short unit; E019 acceptance/confrontation remain open.

## V003 C003 E021 relationship delta — prior familiarity, current information aid

- **AKO ↔ AYANE/ABYDOS:** Ako offers opponent data and greets Ayane by full name; Ayane recognizes her, Iori jokes of a reunion and Nonomi approves friendly relations. No formal alliance charter or verified handoff result.
- **HOSHINO/SHIROKO/SERIKA/CHINATSU ↔ COALITION:** readiness/support cues precede Hoshino's move order; outcomes absent.
- **SEIA ↔ SENSEI:** Seia credits Sensei with rejecting a coercive proof question and says she was wrong; this is an intellectual response, not new physical dialogue or Seia's medical recovery.
- **AZUSA ↔ HIFUMI/SAORI:** no direct change in this unit; E019 contact and duel outcome remain open.

## V003 C003 E022 relationship delta — Saori confronts Azusa's separate path

- **SAORI ↔ AZUSA:** Saori's inward shared-suffering memory turns to a spoken threat to negate Azusa's Trinity experience; Azusa urges surrender and privately resolves not to lose. Their former common life is acknowledged, not reconciled; no final duel result.
- **HANAKO/KOHARU ↔ AZUSA:** both answer Saori on the validity of Azusa's acquired life, with Koharu anchoring it in the group's pass/effort. This is direct peer defense, not proof they can ensure Azusa's safety.
- **HIYORI/MISAKI ↔ SAORI:** they address their leader; Hiyori states their means are exhausted and they have lost. No Saori assent or Arius institutional capitulation.
- **SENSEI/HIFUMI ↔ AZUSA:** no new speech in this short unit; E019 contact remains the last direct relational step.

## V003 C003 E023 relationship delta — farewell and accompanied confrontation

- **AZUSA ↔ HIFUMI/HANAKO/KOHARU:** Hifumi wants to follow, but Azusa asks her to rest because of injury; Azusa addresses all three by name, receives their care and says she will return. The farewell directly supports peer belonging, not guaranteed return or Hifumi's medical clearance.
- **AZUSA ↔ SENSEI:** Sensei's singleton choice to come elicits Azusa's thanks; later inward cues are not additional dialogue. Accompaniment is chosen after Azusa elects pursuit, so neither party's agency is erased.
- **AZUSA ↔ SAORI:** Azusa proposes ending it, Saori demands a last battle and challenges a one-on-one win, Azusa says she is not alone, and Saori identifies Sensei as the adult ally. The pair remain adversarial without completed duel or reconciliation.
- **MISAKI/HIYORI ↔ SAORI:** their near-ending assessment is interrupted by Misaki's “not yet” and Saori's underground allusion; no shared plan's substance is printed.

## V003 C003 E024 relationship delta — Atsuko challenges Saori's inherited path

- **ATSUKO ↔ SAORI:** Atsuko asks Saori to stop and flee with her, saying shared hatred was learned rather than truly theirs. Saori fears an unnamed woman and return to Arius, initially balking. Neither assent nor safe joint escape is printed.
- **ATSUKO ↔ AZUSA:** Atsuko credits Azusa's insight and recognizes her learning, adult encounter and found place. Azusa's silent response does not license a full reconciliation claim.
- **SENSEI ↔ AZUSA/MAESTRO:** Azusa warns to flee; Sensei responds with choices/card, Maestro interprets and thanks the adult after an unprinted transition. Exact protection/defeat mechanics remain open.
- **SQUAD ↔ OUTSIDE SEARCH:** narration confirms the search failed; the later Squad fragment shows Saori coughing and uncertain destination, but `u:0011-0015` speaker labels are unreliable.

## V003 C003 E025 relationship delta — talk invited, safety withheld

- **NAGISA ↔ MIKA ↔ SEIA:** Nagisa hears a Mika letter; Seia is addressed and directly invites the three to discuss unsaid truths. Speaker faults around adjacent banter bar exact reciprocal emotion; no completed forgiveness or restored former intimacy.
- **MINE ↔ SERINA/RESCUE KNIGHTS:** Mine returns, apologizes for disappearance and receives an emotional welcome. The encounter is direct, with later duty/medical details open.
- **HIFUMI/AZUSA/KOHARU/HANAKO ↔ SENSEI:** the same four explain their renewed remedial status and react to Sensei's inwardly described collapse. Their prior pass and friendship persist, but exact administrative facts rest on their reports.
- **ATSUKO ↔ AZUSA/SQUAD:** Atsuko inwardly wishes Azusa happiness and may never see her again. The anonymous order targets escaped “royal blood” and permits harm to others; no delivered farewell, actual capture or stable Squad refuge.

## V003 C003 checkpoint relationship reconciliation

The [C003 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C003_CHECKPOINT.md) retains both Azusa's threatened lethal separation and Hifumi/peer intervention; the former does not erase the latter. Atsuko offers Saori a shared exit from taught hatred, but no clear assent or secure refuge follows. Hina accepts practical help from Justice/Abydos without proof of lasting friendship or treaty. Seia directly invites Nagisa/Mika to talk after prison/attack history, not completed forgiveness or legal relief. Sensei accompanies Azusa after her own decision, not as sole author of her future. C004 E001 unopened.

## V003 C004 E001 relationship delta — Atsuko offered herself, promise betrayed

- **ATSUKO ↔ SAORI/MISAKI/HIYORI:** Atsuko offers surrender to spare the three; Misaki warns of death, Saori protests and inwardly questions purpose without her. No assent to Saori's defense plan or safe release.
- **ATSUKO ↔ BEATRICE:** Atsuko demands a name-bound pledge to spare Squad. Beatrice directly promises then orders their killing, establishing immediate bad faith; ritual and capture outcomes remain pending.
- **SQUAD ↔ ARIUS PURSUERS:** encirclement and firing order are direct. The `u:0065-0067` ellipses do not establish who was hit or killed.
- **SENSEI/AZUSA ↔ SQUAD:** no direct interaction in this episode; C003 relationship findings remain prior authority.

## V003 C004 E002 relationship delta — uncomfortable external accountability

- **NAGISA ↔ MINE/SAKURAKO:** Mine presses Tea Party accountability/Seia care and later worries Azusa was interrogated; Sakurako shares inquiry work and counters overreach. Label inversions limit exact turns, but tension and independent oversight are secure.
- **NAGISA ↔ MIKA:** Nagisa resists route-concealment suspicion, chooses trust and plans a hearing defense; neither Mika's truthfulness nor the hearing result is shown.
- **NAGISA/SAKURAKO/SENSEI ↔ REMEDIAL FOUR:** Nagisa admits causal responsibility for their burden, Sakurako says Hanako's contract ended, and Sensei agrees to keep working with leaders. The four are absent from this meeting; their consent/response unshown.
- **MINE ↔ SEIA/AZUSA:** Mine reports treating Seia and defends Azusa from an assumed interrogation, then hears it was voluntary by Nagisa's account. Her care is direct claim, accusation not demonstrated fact.

## V003 C004 E003 relationship delta — visiting, attendance and misread care

- **NAGISA ↔ MIKA:** Nagisa reports social punishment and wants to defend Mika; Mika initially declines a hearing to avoid harming Nagisa's authority, then agrees after Sensei's intervention. Nagisa has not yet learned the decision on-page, and the hearing has not occurred.
- **MIKA ↔ SEIA:** Seia declined Mika's meal because she felt ill, while Mika reads it as hatred and says she has not apologized. Sensei cites Seia's earlier personal forgiveness and proposes a meeting; Seia has not consented to join the hearing or spoken directly with Mika here.
- **SENSEI ↔ MIKA/SEIA:** Sensei visits Mika, offers to seek Seia and listens to Seia's current illness/vision account. The visit produces Mika's attendance agreement, not restored trust, forgiveness procedure or safety.
- **MIKA ↔ CROWD/JUSTICE:** hostile protest and Justice restraint are directly shown; individual stone-throwing and property destruction are Nagisa's reports, not observed perpetrator identities.

## V003 C004 E004 relationship delta — mutual intent before meeting

- **SEIA ↔ MIKA:** Seia recognizes that her prior forgiveness was dream-delivered, not received by Mika; she acknowledges mutual failure to apologize, requests a private meeting and intends hearing attendance. Mika already agreed in E003, but the two have not met here.
- **SENSEI ↔ SEIA:** Sensei questions risky lucid-dream/Gematria pursuit, proposes collective evidence gathering and prompts attention to Mika. Seia accepts the redirection; no clinical recovery or solved vision follows.
- **SENSEI ↔ NAGISA:** narration confirms Sensei relays the planned Mika/Seia attendance, and Nagisa thanks them. This closes the E003 communication gap, not the hearing result.
- **SEIA ↔ GEMATRIA FIGURES:** apparent Black Suit/Maestro/Beatrice contact occurs in her lucid-dream perspective; do not promote it to a verified real-world meeting or allegiance.

## V003 C004 E005 relationship delta — contested adult targets and a first greeting

- **BEATRICE ↔ MAESTRO/BLACK SUIT/GOLCONDA:** in-frame Beatrice claims to repurpose their work, Maestro objects, Golconda mediates and Black Suit accepts lack of veto while seeking her plan. Their Sensei stances diverge; no single collective decision to kill Sensei is shown.
- **BEATRICE ↔ SQUAD:** she calls Squad disposable and claims she offered reprieve for killing Sensei. No direct Squad receipt, consent, attack or reprieve follows.
- **BEATRICE ↔ MIKA:** she credits Mika's Arius visit and Trinity invitation as inspirations; this is Beatrice's use of Mika's actions, not proof Mika understood her agenda.
- **MIKA ↔ SEIA:** Mika arrives and says hello; a Mika-tagged `……ミカ` next turn is suspect. The requested reunion starts at a greeting but no apology or private conversation is printed.
- **SEIA ↔ SENSEI:** Seia inwardly fears for Sensei after the claimed Squad task and wants to warn someone, but physical communication is not shown.

## V003 C004 E006 relationship delta — meeting starts under illness

- **MIKA ↔ SEIA:** Mika arrives for the requested private talk, notices Seia's shaking, asks for help and stays distressed. Seia audibly says Mika is not to blame for the present crisis. No substantive apology, reciprocal forgiveness or durable repair is printed.
- **SEIA ↔ BEATRICE:** Beatrice directly addresses Seia as an eavesdropper within a basilica perception/dream crosscut. Reciprocal contact is stronger than E005's passive overhearing, but physical location and mechanism remain unaudited.
- **SEIA ↔ SENSEI:** she calls for Sensei to flee; Sensei later inwardly thinks they may have heard her. This is suggestive crosscut, not certain transmission or comprehension.
- **SENSEI ↔ SAORI:** Sensei sees Saori in an empty-feeling town reached from an anonymous email; Saori is silent. Meeting intent and Beatrice-task compliance remain open.

## V003 C004 E007 relationship delta — shame, threat and bounded trust

- **MIKA ↔ SEIA/NAGISA/SENSEI:** Mika believes tomorrow's shared hearing dream is gone after Seia's illness and crowd hostility. Her conclusion that Seia never forgave her is not Seia's present testimony; escape threatens the planned process.
- **MIKA ↔ SAORI/SQUAD:** Mika makes Saori the sole cause of all harm and threatens those dear to her. This is a dangerous intention, not demonstrated Saori sole authorship or accomplished revenge.
- **SAORI ↔ ATSUKO/PEERS:** Saori pleads for Atsuko, reports other members missing and blames her own failed protection. No reunion/casualty count yet.
- **SENSEI ↔ SAORI:** Saori offers total obedience and a lethal bomb against herself; Sensei asks equal conversation, chooses aid despite being shot and disarms her instead. This is bounded trust, not exoneration.
- **SEIA ↔ MIKA/CROWD:** anonymous voices accuse Mika during Seia's medical crisis, while others object; the accusation has no established cause.

## V003 C004 E008 relationship delta — choosing the same boat

- **HIYORI ↔ SAORI:** Hiyori says she refused an Arius return offer in exchange for Saori's whereabouts; Saori offers to let her take it, and Hiyori resists being presumed likely to betray. The bond survives the offer but their future safety does not follow.
- **HIYORI ↔ SENSEI:** she initially fears punishment and a rumored dungeon, then hears Sensei explicitly offer rescue help. Her terror does not establish Sensei's intent.
- **MISAKI ↔ SAORI/HIYORI:** Misaki's edge-side threat and futility challenge confront Saori's determined rescue response; Misaki agrees to accompany the group. No completed jump, lasting recovery or uncoerced independent enthusiasm is inferred.
- **SQUAD ↔ SENSEI:** Misaki and Saori acknowledge an amnesty-for-killing-Sensei offer, while Sensei judges they have not acted on it here and remains with them. Conditional trust is not a guarantee.

## V003 C004 E009 relationship delta — travel together under pursuit

- **SQUAD ↔ ARIUS PURSUERS:** two role-labeled pursuers recognize Squad and order combat; the subsequent dialogue treats them as beaten, without printed blow-by-blow or casualty status.
- **SQUAD ↔ SENSEI:** Sensei asks about the route, then remains with the group through an offscreen clash. Hiyori's “adult power” appraisal suggests help but cannot isolate Sensei's exact causal contribution.
- **SAORI/MISAKI/HIYORI:** all continue toward the entrance despite unstable individual line labels; E008's immediate alliance persists, not verified district access.

## V003 C004 E010 relationship delta — former allies face each other

- **SQUAD ↔ SENSEI:** Misaki/Hiyori rely on Sensei's presence; Saori orders Squad to clear danger before Sensei follows. No printed combat teamwork here.
- **MIKA ↔ SAORI/SQUAD:** Mika directly confronts Saori after E007's revenge threat, calling her apparent shock a “witch” look. No shot, attack or negotiation is printed.
- **SQUAD ↔ BEATRICE/PURSUERS:** the group anticipates preparation/elite guards, but Mika is the only newly visible obstacle; the predicted force is still hypothetical in this unit.

## V003 C004 E011 relationship delta — parted at the passage

- **MIKA ↔ SAORI/SQUAD:** Mika attacks and threatens equal loss, then hears Arius pursuers also intend to dispose of Squad. Her `私のもの` refusal to hand them over preserves her own claim, not proof of forgiveness or safety.
- **MIKA ↔ SEIA:** Mika says Seia's supposed death grieved her despite anger and denies intending lethal harm; her account is not a completed apology to Seia.
- **SENSEI ↔ MIKA:** Sensei arrives, tells Mika to return/wait and promises later explanation, then goes into catacombs with Squad. Mika reacts with shock and does not explicitly agree.
- **SENSEI ↔ SQUAD:** the group enters the underground route together, under deadline, while Mika and Arius pursuers remain outside; no district arrival.

## V003 C004 E012 relationship delta — pursued care, recalled coercion

- **MIKA ↔ SENSEI/SQUAD:** Mika recognizes Sensei's rescue motive but still promises to chase Squad for revenge and fears Sensei's disapproval. E011's refusal to yield Squad was not forgiveness.
- **HIYORI ↔ AZUSA/SAORI:** Hiyori recalls first meeting Azusa at a coercive training site and Saori running toward an abused child; the exact intervention/result is cut off.
- **SENSEI ↔ SAORI/MISAKI/HIYORI:** Sensei brings medicine; Misaki administers it, accepts rest and rotates watch, allowing Sensei/Hiyori to sleep. This is distributed care, not verified recovery.
- **SEIA ↔ MIKA/SENSEI:** Seia self-blames for hurting Mika, plans apology with Nagisa/others and warns Sensei from a liminal state; no delivered warning or meeting yet.

## V003 C004 E013 relationship delta — rescue bargain and self-disclosure

- **SAORI ↔ ATSUKO/SQUAD:** Misaki says Saori took Atsuko away from a feared sacrifice; Saori's italic account frames obeying Madame as the price of altering Atsuko's fate and aiding others. The bargain's text and performance remain unverified.
- **MISAKI/HIYORI ↔ ATSUKO:** Hiyori recalls envy; Misaki admits concealing interest and directly remembers Atsuko's kindness/laughter. This is specific attachment, not proof of royal records.
- **SENSEI ↔ SQUAD:** Sensei asks for a painful childhood account and then assents to Saori's corridor search. Hiyori is startled by Sensei's expression, so willingness to tell is not complete trust or erased adult fear.
- **MIKA ↔ ARIUS GUARDS:** Mika asks a route question and receives an attack order; she reacts in pain. No meeting with Squad/Beatrice or resulting guard fate is shown.

## V003 C004 E014 relationship delta — predator, teacher and recurrent pursuer

- **BEATRICE/MADAME ↔ SQUAD/ATSUKO:** Beatrice explicitly calls Saori obedient after admitting the apparent failed occupation still fulfilled her hidden path objective; Saori recognizes the Atsuko-saving promise as bad faith. Beatrice's surveillance/path capacities remain her own claims.
- **BEATRICE ↔ SENSEI:** communication is direct and adversarial. She offers knowledge for leaving Atsuko, calls Sensei enemy after a refusal, and schedules a basilica confrontation; Sensei does not accept her exchange. Inner condemnation is not confirmed audible.
- **SENSEI ↔ SQUAD:** a Justina follower orders disposal, Sensei inwardly urges action and Saori responds. No combat outcome is printed in that sequence.
- **MIKA ↔ SENSEI/SQUAD:** Mika reappears, says a try at beating the Sensei-led group failed and praises Sensei's strength. The skipped clash does not resolve forgiveness, bodily harm or her next allegiance.

## V003 C004 E015 relationship delta — care imagined as conditional

- **MIKA ↔ SENSEI:** Mika calls herself an irredeemable bad/problem student and predicts Sensei will stop meeting her if expelled; Sensei does not say that. One choice either gives probable Seia reassurance or asks her to return without harm. Mika rejects restraint and leaves.
- **MIKA ↔ SAORI/SQUAD:** Saori says they subdued Mika locally, but Mika insists Saori cannot enjoy Sensei's protection without cost. Continued pursuit is explicit, not a completed attack.
- **SQUAD ↔ SENSEI:** after Mika departs, the group treats Arius/Justina/Mika as compounding risks and continues toward the alleged corridor. Mis-tagged Hiyori lines prevent exact speaker assignments.

## V003 C004 E016 relationship delta — Mika separates Saori from adult aid

- **MIKA ↔ SAORI:** Mika claims calibrated collapse to spare Sensei while leaving Saori isolated; Saori faces her on the opposite side of the debris. No duel or injury result yet.
- **SENSEI ↔ SAORI/SQUAD:** Sensei dodges the falling column and reports immediate safety with Misaki/Hiyori, while Saori confirms she is across a blocked passage. Remote concern is visible, physical aid not yet available.
- **MISAKI/HIYORI ↔ SAORI:** they ask for her safety and try to clear/route around rubble; passage remains blocked by their account. The exact tactical warning speaker is compromised by Hiyori-tag errors.

## V003 C004 E017 relationship delta — Saori entrusts Atsuko, confronts Mika

- **SAORI ↔ SENSEI/SQUAD/ATSUKO:** Saori asks Sensei not to return and to reach Atsuko; Misaki asks Sensei to decide after presenting the detour risk. Sensei goes, but no Atsuko meeting or Saori safety follows.
- **MIKA ↔ SAORI:** Mika's target talk oscillates, then she seeks a witch/hound execution script. Saori accepts her anger and a causal part in her loneliness/loss, and fights back. The duel remains unresolved.
- **BEATRICE ↔ SEIA:** Beatrice addresses Seia in the liminal frame, names Color and taunts her inability to return; Seia says she will seek a way out. This is exchange, not physical recovery or proof of Beatrice's theory.

## V003 C004 E018 relationship delta — early good faith, later betrayal, present restraint

- **MIKA ↔ ARIUS/SAORI:** a pre-coup encounter directly shows Mika offering gradual reconciliation and secret transfer; Saori says she could not decide alone, then Beatrice orders intelligence exploitation. Saori later confesses deception and Mika acknowledges she once wanted that future, without erasing her later coup choices.
- **SAORI ↔ AZUSA/SQUAD:** Saori reports originally choosing Azusa as a reconciliation symbol, later as spy/Seia-attack participant, and now asks whether Azusa found an answer to happiness. Her retrospective self-blame for Atsuko/Hiyori/Misaki is broad but not their full agency map.
- **MIKA ↔ SAORI:** injured Saori offers herself for retaliation; Mika refuses because killing would deny her own possibility of mercy. Local violence stops, but pardon, affection, safety and school outcomes remain open.
- **SENSEI ↔ SAORI/MIKA:** Saori tells Mika Sensei confiscated halo bombs; both react to Sensei's arrival. No route or voiced version of the inner thought is supplied.

## V003 C004 E019 relationship delta — one rescue party, an offered future

- **SENSEI ↔ SAORI/MISAKI/HIYORI:** Sensei explicitly says Atsuko's rescue will continue with Saori. Misaki admits she could not dissuade them and Hiyori welcomes injured Saori; reunion is real, intervening route unknown.
- **SENSEI ↔ MIKA:** Sensei apologizes for not explaining/facing her, gives student-life risk as reason to aid Saori, proposes joint Trinity return after Atsuko and offers help/chances. Mika doubts her own eligibility; no acceptance, pardon or school decision is shown.
- **BEATRICE ↔ SQUAD/SENSEI/ATSUKO:** Beatrice cuts off the exchange, advances the rite and orders Barbara to silence Sensei. Threat relation intensifies without printed result.
- **SEIA ↔ UNKNOWN VOICE:** a daydream speaker perceives Seia and asks why she arrived; identity and benevolence unknown.

## V003 C004 E020 relationship delta — Squad faces title-linked saint

- **BARBARA ↔ SQUAD/SENSEI:** a title-linked Justina saint force is directly experienced by Saori/Hiyori/Misaki after Beatrice's order; no Barbara dialogue, personal motive, damage or outcome is printed. Her relation to Sensei is an ordered threat, not a developed reciprocal bond.
- **SQUAD ↔ ATSUKO:** rescue remains urgent, but the saint pressure supplies no new Atsuko contact or safety update.

## V003 C004 E021 relationship delta — split, proximity, confrontation

- **MIKA ↔ SAORI/SENSEI:** Mika tells Saori to go save Atsuko and thanks Sensei for the chance language. Sensei asks her to be careful. This is bounded cooperation after an unresolved duel, not a settled reconciliation or pardon.
- **SAORI/SQUAD ↔ ATSUKO:** Saori calls to Atsuko in the sanctuary and Misaki judges her apparently unconscious. Contact/proximity is direct; extraction and recovery are not.
- **BEATRICE ↔ SENSEI:** Beatrice directly greets Sensei as enemy in the sanctuary exchange. Hostility is explicit; its physical and ritual consequences await evidence.

## V003 C004 E022 relationship delta — teacher with students against Madame

- **BEATRICE ↔ SENSEI:** Beatrice offers a shared absolute-adult horizon and asks for assent; Sensei rejects the premise and names teacher-for-students as role. The conflict is ethical and tactical, not an agreed account of either's powers.
- **SENSEI ↔ SAORI/HIYORI/MISAKI:** Sensei promises presence and joint effort; the three answer and aim to save Atsuko. This is explicit coalition under pressure, with the clash itself skipped.
- **BEATRICE ↔ SQUAD/ATSUKO:** Misaki/Hiyori reappraise Madame's form as monstrous, while Beatrice treats an unspecified “small sacrifice” as necessary in the established Atsuko ritual context. She orders Barbara and all basilica troops back for protection; response unshown.

## V003 C004 E023 relationship delta — Mika forgives absent Squad

- **MIKA ↔ SAORI/SQUAD:** Mika directly forgives them and hopes for their healing/future after admitting she wanted equal pain. The speech occurs apart from Squad; Saori's hearing or reciprocal forgiveness is not evidenced.
- **MIKA ↔ SENSEI/KOHARU:** Mika fondly remembers their earlier rescue and believes Sensei will help Squad, yet excludes herself from a happy ending. This does not negate the previous direct chance offer.
- **MIKA ↔ APPROACHING FORCE:** she tells unnamed plural addressees they cannot pass and promises to hold them. E022's summons makes reinforcements plausible, but composition, confrontation and success are not printed.

## V003 C004 E024 relationship delta — Squad reunites, Gematria retrieves

- **SAORI/HIYORI/MISAKI ↔ ATSUKO:** they find Atsuko badly hurt, call to her and receive direct waking speech. Saori thanks her for living; Atsuko reassures Saori and recognizes all three. This repairs immediate contact, not health or future security.
- **BEATRICE ↔ SAORI/SQUAD:** Beatrice selects Saori as replacement sacrifice; Saori offers herself and Misaki protests. Beatrice then falls after omitted combat, leaving the coercive relation locally interrupted.
- **SENSEI ↔ SQUAD/BEATRICE:** Sensei names students precious and opposes Beatrice's teaching; Saori credits Sensei's help. No audited combat method.
- **GOLCONDA ↔ BEATRICE/SENSEI:** Golconda self-identifies in the present, intends to take Beatrice back and warns Sensei not to interfere. Departure/custody are not separately shown.

## V003 C004 E025 relationship delta — reciprocal future and Mika return

- **SAORI ↔ SENSEI/SQUAD:** Saori asks Sensei to choose punishment; Misaki protests the lone burden, and Atsuko asks about her unknown desires/future. Sensei offers an answer she must find herself. Saori reports first felt permission to exist, not settled guilt or treatment.
- **ATSUKO ↔ SENSEI:** she thanks Sensei and offers a mask-device explanation; Sensei presents conditional future mask use/care as alternatives. Her serious injury is not erased.
- **SENSEI ↔ MIKA:** Sensei comes to her while she expects abandonment/death, repeats alliance and takes out the adult card. Mika is surprised but still warns against the saint threat; rescue outcome awaits the next unit.
- **MINE/RESCUE KNIGHTS ↔ ARIUS STUDENTS:** Mine names them as needing care and orders treatment even while preparing to create wounded in battle. This is declared inclusive rescue, not confirmed delivered care.

## V003 C004 E026 relationship delta — Tea Party contact restored

- **MIKA ↔ SEIA/NAGISA:** direct living reunion, teasing, love, thanks and mutual apology are printed; exact apology attribution becomes unstable around `u:0109-0117`. No exhaustive causal reconciliation or hearing result.
- **MIKA ↔ KOHARU:** Koharu quietly preserves and sends Mika's surviving accessories; Mika recognizes her effort and thanks her while acknowledging earlier harm. Koharu is absent from the handoff reception.
- **AZUSA ↔ SQUAD:** Azusa asks rescue of Atsuko and the others as former family despite their attacks/crimes; this is her ongoing attachment, not reciprocal forgiveness or Squad rejoining.
- **STUDENTS ↔ SENSEI/MIKA:** Ichika/Justice find them, Hasumi routes withdrawal, Seia/Nagisa/Sisterhood/Rescue Knights mobilize, Hanako/Ui search route evidence. The distributed care has a completed finding but not all downstream safety outcomes.

## V003 C004 E027 relationship delta — Squad separates without severing care

- **SAORI ↔ MISAKI/HIYORI/ATSUKO:** Saori leaves Misaki in charge; Misaki feels the burden and Atsuko expects eventual return. Separation is real, future reunion not shown.
- **ATSUKO/MISAKI/HIYORI ↔ SENSEI/AZUSA:** Atsuko cites Azusa's flower resistance and Sensei's watchful care as reasons to persist, without a direct present meeting with either.
- **SAORI ↔ BLACK MARKET EXECUTIVE:** he exploits her precarious status with claimed deductions and blackmail; she departs with no wage. The exact contractual basis is uninspected.
- **HARUKA ↔ ARU/PS68:** Haruka intimidates the executive under a misread Aru instruction; Aru protests, Mutsuki laughs and Kayoko anticipates consequences. No bomb result or corrected trust pattern is shown.

## MAIN V003 C004 checkpoint relationship reconciliation

The [canonical C004 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C004_CHECKPOINT.md) fixes the chapter-local relationships: Saori leaves Beatrice's coercive bargain, reunites with Atsuko then voluntarily separates to seek a life answer; Mika refuses to kill Saori, personally forgives Squad and directly reconnects with Seia/Nagisa; Sensei stands with Squad and returns for Mika while students return rescue to Sensei/Mika. Interpersonal repair is meaningful but not the same as Squad's secure home, Saori's rejoining or Mika's school hearing result. V004 C001 E001 unopened.

## V004 C001 E001 relationship delta — Rin delegates after restraint

- **RIN ↔ SENSEI:** she recognizes useful Schale action yet corrects Sensei's paperwork and initially keeps the SRT problem federal. After reported failures she explicitly requests assistance and temporarily takes over the reports. Respect, irritation and division of labor coexist.
- **AYUMU ↔ RIN/SENSEI:** Ayumu repeatedly escalates new reports and proposes Schale's help; this is advice from an administrative colleague, not authority over the protesting students.
- **ARONA ↔ SENSEI:** Arona tries to reassure Sensei about Rin's invitation before the correction session; her hospitality forecast is optimistic, not corroborated by Rin's purpose.
- **SRT GROUP ↔ GSC/VALKYRIE:** their occupation and reported force defeat create an adversarial operational relation, but no student has spoken or been individually identified.

## V004 C001 E002 relationship delta — fractured command and refused adult

Within RABBIT, Miyako seeks disciplined negotiation and resource restraint; Saki contests her command and Moe invokes the absent president to loosen obligation, while Miyu needs protection rather than elite shaming. This is friction inside a still-acting squad, not proven dissolution. Kanna begins dismissive of Kirino/Fubuki, then thanks them after their result; no reward/transfer is granted. Sensei takes operational responsibility and publicly credits the two students, but RABBIT rejects contact: Miyako's direct adult distrust cannot be flattened to Kanna's loss-irritation gloss. Shinon/Mai's broadcast and Kanna's camera objection remain a press–police boundary, not personal enmity.

## V004 C001 E003 relationship delta — loyalty without one motive

Saki identifies strongly with SRT and resists Kanna's intimidation, yet her admission softens the flawless-rule persona. Moe says she would gladly part with the current RABBIT members, so squad solidarity cannot be inferred from shared protest; this remains one interview statement, not a completed separation. Miyu reports Miyako sometimes caring for her despite limited closeness overall; transfer threatens recognition more than safety. Miyako acknowledges Sensei's skill but rejects praise from a near-stranger and treats his welfare question as possible quid pro quo. Kanna thanks Sensei for cooperation while predicting council control; Kaya enters before any answer.

## V004 C001 E004 relationship delta — Kaya courts Sensei

Kaya thanks Schale for absorbing federal burdens, values RABBIT's elite potential and asks Sensei to persuade them toward Valkyrie; after an apparent response to Sensei's inward objection, she professes respect for students' dreams and offers Schale broad disposition discretion with Defense Office support. This is a political/administrative approach, not proof Sensei accepts a coercive bargain or that the students trust either actor. Kaya reports Rin's post-FOX talks; Rin does not speak here. `u:0057` seems to address Kaya as Defense head under a Kaya tag, so Kanna's exact reaction is quarantined.

## V004 C001 E005 relationship delta — no gratitude bargain

All four reunite and fear the coming decision. Miyako apologizes, but Saki rejects her claim of leader-only responsibility after closure. Sensei's represented release and lodging offer do not buy loyalty: Miyako refuses Schale, says they remain opposed and still distrust Sensei, while Sensei accepts that without a condition of thanks. Saki calls the next encounter adversarial, Moe says they were already enemies, and Miyu fears being left behind. The squad remains together enough to choose park camping, despite E003's divergent motives and internal tension; actual arrival and durable cohesion are open.

## V004 C001 E006 relationship delta — care suspected as bargain

Sensei returns to check the squad; Saki and Moe have fortified the public park, with danger to Sensei and potential bystanders. Miyako initially insists they need no help, then admits hunger. The four briefly want ramen, but Sensei's transfer question confirms their fear that food could be leverage; they jointly refuse school conversion. Miyako accepts only an address note, while Sora later offers disposal goods on Sensei's arrangement. Moe takes the chance, Saki protests shame then will eat, Miyu fears dependence, and Miyako privately names humiliation. No trust or alliance is established; Sora is a friendly transactional contact with no prior relationship evidence.

## V004 C001 E007 relationship delta — aid remains unwelcome but ideas travel

Saki/Moe argue over lunch and Miyu is denied her choice; Miyako tries to restrain them while making a premium selection. The squad recognizes temporary food access yet still attributes possible humiliating intent to Sensei. When Sensei notices hygiene distress, Saki/Miyako threaten distance and reject Schale's shower over privacy/distrust. Nonetheless Miyako accepts the drum-bath concept and commands Moe to seek drums. This is selective use of an idea, not trust, thanks or new Schale membership.

## V004 C001 E008 relationship delta — authority challenge and mutual rescue

Saki attacks Miyako's federally appointed captaincy, takes temporary command and discovers theory/practice difficulty; Miyako warns, then cooperates and later credits Saki for success. Saki chooses Miyu's rescue over cargo, personally retrieves her and still scolds her fear. This is care under tension, not full equality or solved distrust. Sensei's barrel disguise suggestion is accepted for the rescue even though Saki says she dislikes following them. Later the squad objects to Sensei's presence during its bath and escalates to an order for a missile; no strike is printed. Unidentified neighbors interpret RABBIT as resource-taking outsiders and arm themselves, but no direct encounter yet.

## V004 C001 E009 relationship delta — Kirino offers help, unknown actor intervenes

Kirino checks whether released RABBIT students have harmed Sensei and offers 24-hour Valkyrie contact if needed; she admires Sensei on the basis of their constrained reassurance. The four students do not speak and no relationship repair is shown. A later unknown speaker targets Sensei by name and releases smoke; this establishes an adversarial contact but not their relation to RABBIT, the E008 neighbors or Kirino. Sensei is unconscious at the cut; no ally response is printed.

## V004 C001 E010 relationship delta — coercion, coordination, refusal

Decartes treats Sensei as an instrument to control RABBIT, while Sensei says the students are not subordinates. Miyako and Saki initially dismiss a stranger's phone claim, then the food lure brings the squad; this does not prove foreknowledge of Sensei's safety. The squad coordinates under threat and reports no injuries. Miyako initially seeks compensation in goods, but Saki/Miyu opt to leave and Miyako orders no spoils. Sensei's offered purchase is choice-conditioned and declined; RABBIT's resistance to adult financial support remains local and unresolved. Decartes's invitation is refused.

## V004 C001 E011 relationship delta — visible help and narrow gratitude

Saki, Moe and Miyu question continuing the camp; Miyako continues alone at the drain, preserving the SRT ideal but not persuading the others by speech. Sensei joins the practical task, Saki takes over a shovel, and Miyu helps; narration confirms group labor. Miyako accepts help despite prior rejection and thanks Sensei, while Saki frames the effort as unrewarded and Moe keeps teasing. This shifts local interaction from adversarial refusal toward acknowledged aid, not full trust, housing acceptance or squad agreement about its future.

## V004 C001 E012 relationship delta — supportive address versus desired rupture

Sensei asks Rin, other council members and Kaya for park repair help, but receives no authorized aid. Rin is frank about limits and declines persuasion. Kaya speaks warmly to Sensei and asks them to keep looking after RABBIT, then tells an unnamed partner she had expected the relationship to damage itself and end. This direct asymmetry qualifies trust in her earlier courtesy without identifying a prior plot. Kanna appears anxious in Kaya's progress review; Kaya uses responsibility/SRT-fate pressure and suggests additional aligned-interest actors. No new relationship with the unidentified expert is specified beyond Kaya's own “best partner” label.

## V004 C001 E013 relationship delta — food, discretion and bounded reliance

Sensei withholds RABBIT details from an unnamed seller even when offered extra food, then brings purchased/leftover inari to the squad. Moe and Saki suspect contamination or spoilage before the group shares it; Miyu initially doubts Sensei paid. Miyako accepts the food, remembers seniors and later treats Sensei's presence as a reason against her worst Black Market scenario. This is narrow reliance under damaged supplies, not full trust or proof Sensei can prevent future harm. The seller's familiar role address and fondness for former colleagues do not identify any personal tie to the squad.

## V004 C001 E014 relationship delta — supply initiative under scrutiny

Moe takes supply initiative and displays a prior commercial relation with a Kaiser Industry salesman. Saki initially doubts then briefly praises her plan; Miyako and Miyu question old purchasing/accounting after the VVIP disclosure. Moe deflects rather than proving a funding source. Sensei questions rust minimization and private bombs but does not stop the proposal. The failed call leaves the group still dependent on a hoped auction route, with no restored armaments or resolved intra-squad trust.

## V004 C001 E015 relationship delta — Decartes seeks refuge among former rivals

RABBIT's former captor/rival Decartes appeals for help after claiming 所確幸 scattered; Miyako initially invokes nonintervention in private civil disputes and Moe taunts the group name, so no alliance forms. Decartes warns they share the same Public Security threat, which becomes locally credible when an officer appears. Saki's practical resource priority challenges Moe's maximized-firepower impulse. Sensei's attentive pause and conditional Kanna guess do not create a verified understanding of the unseen raid or a completed defense pact.

## V004 C001 E016 relationship delta — debt, delay and student initiative

Kanna is adversarial toward RABBIT but grants Sensei's time request because she acknowledges owing them; she withdraws for now and leaves a month-end force condition. Sensei does not command RABBIT to leave or fight, instead shares a hypothesis and supports their chosen investigation. Miyako moves from threatened leader to declaring Clover Operation; Saki/Miyu voice practical objections before accepting the SRT role claim, while Moe tests a reporting alternative. None of this resolves Kanna's duty conflict or the squad's formal standing.

## V004 C001 E017 relationship delta — RABBIT acts without Sensei inside

The squad deliberately leaves Sensei out of the risky route; Sensei's paired rear-line response is supportive, not command in the archive. Moe guides Miyako/Saki/Miyu remotely, Saki spots the document, Miyako interprets it and credits Saki, and Miyu's door closure creates an immediate shared problem. Saki teases Moe's three-minute decode but depends on it. The temporary absence of guards does not dissolve intra-team pressure or prove Valkyrie complicity beyond the found record.

## V004 C001 E018 relationship delta — acknowledged captaincy after distress

Miyu's door mistake and severe self-blame prompt Miyako's protection and Saki's accountability challenge; the team does not resolve it by assigning all blame or denying the error. Sensei encourages Miyako from outside, while teammates voice reliance on her. Miyako devises the alarm-led exit and corridor maneuvers; Saki explicitly retracts past disparagement and says she is captain now, with Moe/Miyu affirming trust. Miyako credits collective work, so the relationship change is mutual recognition rather than solitary-hero elevation. Fubuki is locally decoyed and Kirino fails to stop them; neither forms a new durable alliance.

## V004 C001 E019 relationship delta — adversaries part without settlement

Miyako confronts Kanna with the found record; Kanna moves from threat to a bitter defense of compromised duty, not a full confession or apology. Sensei addresses Kanna's fear of losing everything and urges self-directed choice, with inner-thought label seams. Miyako says their ideals differ by choices made and hopes for a better next meeting. Kanna lets the squad extract and anticipates an incident report, but no reconciliation or lawful disposition is reached. Back at camp, Miyako entrusts Clover and adult follow-up to Sensei after the squad's own completed mission.

## V004 C001 E020 relationship delta — gratitude outside, instrumentalization within

RABBIT sees Chronos coverage and hears of inquiry/cancellation by Moe; Miyu fears retaliation, Saki expects public attention to occupy police, and Miyako hopes to remain at camp. Decartes says their group is returning and thanks the squad, yet the bone “karaage” quarrel reopens hostility without a printed attack. Kaya sees RABBIT as possible coup assets and frames FOX members as seniors; Yukino/Niko/Otogi/Kurumi express different degrees of readiness/reluctance. RABBIT never hears this proposal in the scene and gives no consent. The E012 expert and E013 vendor are not individually identified by this reveal.

## V004 C001 checkpoint reconciliation — bounded trust and rival senior claim

Miyako thanks Sensei after drainage, later trusts them with Clover and adult follow-up; that does not retroactively consent to E008 privacy intrusion or settle formal housing. Saki moves from challenging Miyako's appointed captaincy to affirming her actual E018 result, while Miyako still credits team cooperation. Kanna grants Sensei a temporary reprieve, then defends compromised policing under Miyako's evidence challenge, without reconciliation. Decartes alternates hostility and gratitude but no stable alliance follows. Kaya/FOX discuss RABBIT as juniors and possible coup resources without RABBIT's knowledge or consent. Next chapter remains unopened.

## V004 C002 E001 relationship delta — loyalty under dissent

Yukino's dream of public FOX teamwork includes Niko moderating Otogi/Kurumi's camera quarrel and Yukino checking injuries (`scene:001:u:0011-0016;u:0043-0054`). In the waking operation she receives role reports, dismisses Kurumi's civilian concern as irrelevant and tells Niko she may quit rather than alter the mission (`u:0092-0113`). Niko says `FOX2、承知しました`; Kurumi ends her report. This is continued subordinate cooperation under visible moral friction, not unanimous conviction. FOX plans a `ウェルカムパーティー` for RABBIT without any shown contact, knowledge or consent (`u:0114-0130`). The chapter-one anonymous vendor is not assigned by Niko's inari plan.

## V004 C002 E002 relationship delta — thanks without surrender of duty

Sensei's visit thanks RABBIT for an off-page rescue, while Miyako says they did only SRT duty and Moe adds her own missile-fire motive (`scene:001:u:0046-0068`). Sensei offers steak after the squad first declines further reward; the students invite Sensei to eat and jointly prepare a grill (`u:0069-0097`). Acceptance of a meal does not show consent to any FOX approach, abandonment of the park protest or erasure of Chapter 1's adult boundary problems. Exact public Sensei wording is uncertain where `心の声` receives replies, and paired choices are alternatives. E003 unopened.

## V004 C002 E003 relationship delta — gratitude becomes withheld risk

The shared steak is eaten; RABBIT's suspicion that it might be `餌` is joking/uneasy, not proven deception by Sensei (`scene:001:u:0001-0017`). Once the group sees masked carriers and recognizes possible SRT gear, Saki says they may owe Sensei an apology. Miyu wants prompt disclosure, while Miyako chooses culprit search and recovery before telling Sensei, partly to spare an already busy teacher (`u:0066-0113`). This creates an asymmetric knowledge state after a warm meal: RABBIT has a serious but unverified suspicion and Sensei has no printed briefing. Motive can be considerate and still cost informed partnership. E004 unopened.

## V004 C002 E004 relationship delta — admired senior becomes close opponent

The former FOX ideal from E002 becomes a physical encounter: Yukino, initially `？？？`, restrains/instructs Miyako and addresses her as `月雪小隊長`; Miyako recognizes `ユキノ先輩` (`scene:001:u:0045-0064`). This is direct contact, not reconciliation, consent to a welcome party or proof of the senior's entire strategy. Miyako has not told Sensei the E003 gear suspicion, and Sensei is absent. Exact speaker labels at `u:0060/0062` conflict with the apparent junior response; retain the role uncertainty. E005 unopened.

## V004 C002 E005 relationship delta — warmth and ultimatum

FOX feeds and praises the captive juniors while Yukino makes their shared SRT identity depend on becoming reliable weapons (`scene:001:u:0028-0069;u:0083-0106`). Niko's inari taste suggests a prior link to RABBIT, but vendor identity is not directly confirmed. Saki/Moe feel relief at presumed FOX purchase; Miyako instead challenges the Schale/tower operations and receives a refusal. Yukino addresses Sensei courteously, then says she hates adults like them while granting a delay (`u:0115-0126`); neither mutual trust nor a settled schism follows. Miyako receives a coordinate but no shown acceptance. E006 unopened.

## V004 C002 E006 relationship delta — delayed truth and inherited regard

RABBIT tells Sensei the FOX/Schale concern and apologizes; Sensei's paired reassurance resists their self-blame, while Miyu's food repayment is not enacted (`scene:001:u:0002-0012`). Trust gains disclosure but the stolen object is still unknown. The squad's affectionate/competitive portraits show durable regard for FOX; Miyako's explicit question about obeying a changed Yukino shows that regard no longer resolves alignment (`u:0019-0076`). Kaya publicly summons Sensei, who neither accepts nor declines in print (`u:0101-0109`). E007 unopened.

## V004 C002 E007 relationship delta — apparent sympathy as political setup

Kaya praises Rin's burden and invites a shortcut; Rin refuses coercive authority, after which Kaya states she has long found Rin an obstacle (`scene:001:u:0053-0076`). The exchange is an explicit rupture, with the letter and officer intervention following; no reconciliation or lawful succession is established. Ayumu challenges suspicions about Rin while other members criticize her. Heine appears receptive to a false Rin/FOX story and reports Sports Association disappointment, showing rumor's local effect without representing all members. Kaya plans Sensei as a guest for the post-vote broadcast encounter, but Sensei is absent (`u:0115-0138`). E008 unopened.

## V004 C002 E008 relationship delta — invitation becomes failed bargain

Ayumu and Momoka warn Sensei about Rin's confinement and the chamber's pro-Kaya turn; Momoka calls the invitation a trap, while Sensei still goes (`scene:001:u:0003-0027`). Kaya treats Sensei courteously, admits an unauthorized Schale intrusion, offers relief and broad indemnity for council attribution, then calls Sensei childish after refusal (`scene:002:u:0002-0071`). This is a direct alignment failure, not a forced alliance or immediate fight. Rin is absent; her custody is reported through others. E009 unopened.

## V004 C002 E009 relationship delta — hostile patronage rejected

Miyako intervenes when Kaiser moves on Decartes; a guard threatens RABBIT, then the General halts escalation because he reports Kaya ordered SRT spared (`scene:001:u:0072-0119`). His offer of supplies coexists with admitted hatred and a desire to use future allies; Miyako declines indebtedness (`u:0120-0154`). The squad acknowledges some strategic force in his argument but has not adopted it. Saki and Moe tentatively revisit FOX service because restored schooling and winter supply matter; Miyu is noncommittal, Miyako has not posed her final question (`u:0155-0181`). E010 unopened.

## V004 C002 E010 relationship delta — conditional loyalty and institutional friction

Kaya pressures a Defense deputy over a train crisis despite having barred morning reports; Momoka resists urgency with lunch and operational knowledge, while Aoi refuses a finance exception (`scene:001:u:0009-0085`). Their actions frustrate her, but the unit does not prove coordinated sabotage. Kaya praises Yukino's obedience, then defers school restoration and asks her to keep following orders for FOX/RABBIT; Yukino complies without receiving the promised school (`u:0089-0106`). A Human Resources chief's recruited Red Winter group ceases to be a useful ally when Minori targets Kaya, with assault reported but mechanics unseen (`u:0107-0154`). E011 unopened.

## V004 C002 E011 relationship delta — Kanna and Kirino recognize different strengths

Kirino vouches for a resident, but the Kaiser guard rejects her personal guarantee. Kanna uses paperwork to open passage, then warns Kirino that smoke would not protect her against armed guards (`scene:001:u:0002-0070`). At the cafe Sensei affirms Kanna's earlier principled help, while Kanna describes sanction and doubt. Kirino refuses Kanna's self-denigration, and Kanna names Kirino's civilian trust as a strength she herself cannot replicate (`u:0085-0127`). This is local mutual recognition, not reinstatement or full restoration of confidence. Both head toward protest disorder; outcome unshown. E012 unopened.

## V004 C002 E012 relationship delta — senior bond replaces park companionship

Miyako thanks Sensei in a letter, says hearing the teacher's voice might unsettle her, and leaves before they meet (`scene:001:u:0007-0028`). The bond matters enough to avoid, not enough to prevent departure; Sensei only finds the letter/partly tidies the camp. Yukino directly accepts RABBIT as FOX detachment, and Niko/Kurumi/Otogi welcome the juniors with food, beds, showers and an immediate training order (`scene:002:u:0009-0042`). Miyako's lingering silence to Saki's worry means affiliation is settled locally while trust in its aims is not. E013 unopened.
## V004 C002 E013 relationship state delta — planned subway attack

Kaya tries to direct Cherino as another president and receives jovial noncooperation; Ayumu/Heine witness how little command that relationship affords (`scene:001:u:0002-0054`). The General bargains with Kaya from payment pressure to a prepared attack after she offers Kaiser rail revenue; obligations and threat are spoken, with no concession signed (`scene:002:u:0002-0024;u:0054-0066`). Yukino openly disputes civilian harm before answering Kaya's pressured order as FOX1, leaving a recorded moral objection inside a functional chain of command (`u:0039-0051;u:0067-0071`). The newly subordinated RABBIT is absent and cannot yet be presumed to have endorsed or rejected this order. Sensei is likewise absent. E014 unopened.
## V004 C002 E014 relationship state delta — trust and camp route

Sora offers her own meal; Sensei declines and returns hungry, a bounded care/boundary exchange (`scene:002:u:0017-0023`). Niko/Otogi/Kurumi identify themselves as Kaya-aligned opponents, yet feed Sensei and debate the teacher's trust; Sensei eats and affirms the teacher/student relationship (`scene:003:u:0033-0084`). Sensei cites the seniors' trust in Yukino; their pauses/qualified assent and Otogi's prior-friend statement establish bond plus tension, not rupture (`u:0085-0093`). Niko, as deputy, gives Sensei RABBIT's classified camp route against Kurumi's objection and asks concealment from Yukino; she hopes change may extend from RABBIT to FOX (`u:0098-0112`). No reunion is printed. E015 unopened.
## V004 C002 E015 relationship state delta — comfort and personal justice

Miyako initially misreads Miyu's unease as blame for park hardship and apologizes; Miyu corrects her, then Miyako offers rest rather than addressing the decision-transfer worry (`scene:001:u:0014-0026`). Saki and Moe separately tell Miyako the new arrangement feels hollow; Saki asks Miyako the person whether her unchanged justice survives. Miyako asserts satisfaction as detachment captain and exits without an answer (`u:0027-0044`). Sensei enters the secured site and speaks with her for the first time since the E012 letter; she recognizes the teacher, asks how and declares arrest at a joke (`u:0050-0058`). Actual custody and reconciliation remain open. E016 unopened.
## V004 C002 E016 relationship state delta — Miyako refuses the station mission

Miyako and Sensei finally talk after E012's avoided call. She initially recasts the visit as persuasion, then acknowledges she did not want to hear the teacher's responsibility question; she guides the teacher to a secret exit and accepts a promise of backup (`scene:001:u:0001-0003;scene:002:u:0002-0049`). That is renewed trust without a printed decision to rejoin Sensei. Yukino orders the RABBIT detachment to aid a civilian station detonation; Miyako directly challenges Yukino as deviating from SRT and disputes her command authority (`u:0050-0084`). Niko/Kurumi/Otogi react after this rupture, but no definite side is spoken. E017 unopened.
## V004 C002 E017 relationship state delta — solo return and station coalition

Miyako returns to Sensei and requests tactical counsel, but has not asked Saki/Moe/Miyu to leave their newly comfortable camp (`scene:001:u:0002-0044`). Her aim toward FOX is to stop them before they cannot return, showing continued senior care while opposing their mission. Sensei offers confidence and is later asked to command, with no action outcome yet. Decartes initially treats the pair as suspects despite prior help, then accepts Miyako's warning because the station shelters his comrades; she gives him rounds and he summons members (`scene:002:u:0010-0069`). Two members answer, while complete group presence remains open. E018 unopened.
## V004 C002 E018 relationship state delta — Life Safety opens the station

Kanna joins the station fight on behalf of Kirino/Fubuki and the public, claims a Life Safety legal route despite Public Security suspension, and asks Sensei to care for the juniors (`scene:001:u:0018-0081`). Miyako worries Kanna's defiance may have consequences; Kanna says responsibility and justice are her own decision. Kirino/Fubuki work through familiar station spaces; Miyako thanks and praises Kirino, who takes pride in the bureau despite her ordinary food motive (`scene:002:u:0001-0040`). Decartes and former comrades fight alongside by action but some flee; Fubuki likes his ideal then recoils at the possession demand, so no durable alliance beyond the current encounter is proved. E019 unopened.
## V004 C002 E019 relationship state delta — RABBIT reunites below station

Miyako shields Sensei from a possible breach grenade, sends a drone ahead and worries that FOX may be waiting (`scene:001:u:0001-0043`). Saki/Miyu/Moe confront her for leaving them; Miyako admits she did not want to ask them to give up warm shelter/equipment for her justice. They reject being chosen for, claim the SRT ideal together and directly trust her; she accepts and resumes issuing gear-check orders (`u:0044-0069`). This is a voluntary squad reunion, not a printed formal FOX discharge. Sensei's presence and naming prompt support rather than create their assent. E020 unopened.
## V004 C002 E020 relationship state delta — forward FOX defense falls

Yukino orders Otogi/Kurumi/Niko to retreat if RABBIT reaches the operation room, withholding her reason despite their wish to back her; Niko assents under command (`scene:001:u:0032-0047`). Kurumi and Niko's personal-name slips expose loyalty beneath role discipline. Kurumi fights Saki as a training senior but worries when Saki claims Otogi may be down; Otogi's healthy radio answer triggers a local opening, then FOX3 falls (`scene:002:u:0010-0054`). Miyu unexpectedly gets behind Otogi and says her unnoticed presence lets her help her team; Niko reports FOX4 down, with exact method unprinted (`u:0055-0074`). Niko warns Moe of injury from a physical breach, yet maintains the blockade; Moe forces the door and receives Saki's praise. E021 unopened.
## V004 C002 E021 relationship state delta — Yukino's button threat

Yukino tells Niko/Kurumi/Otogi to retreat if RABBIT reaches her, receives no further Niko answer and concludes she will stand alone. Her withholding of extra explanation and readiness to die suggest concern for them but do not disclose every motive (`scene:001:u:0006-0013;u:0030-0037`). Miyako asks Yukino to surrender, receives a self-destruct threat and still chooses with Sensei's support to continue; Saki/Moe/Miyu voice commitment, not an already safe victory (`u:0023-0046`). FOX3/FOX4 can still report despite combat defeat. E022 unopened.
## V004 C002 E022 relationship state delta — device secured and FOX surrenders

Kurumi/Otogi/Niko return to Yukino instead of obeying the retreat order. Kurumi calls her a friend before captain; Niko refuses both sacrificing a friend and shifting guilt to juniors, and the group shares the SRT refrain (`scene:001:u:0011-0042`). Miyako disarms Yukino's command claim by trusting the senior would not abandon juniors, while Yukino insists her threat was genuine and then reflects on inherited authority (`scene:002:u:0021-0050`). Sensei offers a future for students to learn/seek support; Yukino declares FOX surrender to Miyako (`u:0051-0084`). These are relational reversals without official aftermath or absolution. E023 unopened.
## V004 C002 E023 relationship state delta — Kaya detained after failed coup

The General tells Kaya FOX failed and claims a Kaiser SOF reserve, but RABBIT advances; Kaya's paid-service pressure does not gain rescue (`scene:001:u:0005-0033`). Miyako/Sensei confront her, and she tries to trade Schale independence/resources for help; Sensei directs accountability to students rather than personal forgiveness (`scene:002:u:0006-0025`). Heine comes as ally, trusts Kaya over SRT, then hears older FOX recording and recognizes denial/injury betrayal, demanding impeachment (`u:0026-0059`). FOX's surrender now yields evidence cooperation, but formal arrangements/offscreen transfer are not shown. E024 unopened.
## V004 C002 E024 relationship state delta — chapter epilogue

Miyako writes to confined Niko, reports RABBIT's status and sends a modest bento/inari through Sensei despite facility rules; Niko values the juniors' well-being and plans to share with Yukino/Otogi/Kurumi (`scene:002:u:0002-0036;scene:003:u:0024-0044`). This maintains senior-junior affection without excusing FOX's conduct. RABBIT lives together in the park and freely uses Sensei's Schale help; Moe/Saki banter over showers, Miyako requests one (`scene:003:u:0002-0023`). Kanna receives public credit and early work return by Miyako's account; Kirino declines a Guard transfer by report. Mai/Decartes's broadcast conceals or misstates several relations. Checkpoint due.

## V004 C002 chapter checkpoint — relationship reconciliation

The [chapter checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_004_カルバノの兎編/BLUE_ARCHIVE_MAIN_V004_C002_CHECKPOINT.md) preserves a real RABBIT-to-FOX transfer followed by RABBIT's self-directed reunion, not an uninterrupted refusal. Miyako's rejection of Yukino's mission and FOX's final surrender coexist with continuing senior-junior affection; Miyako writes to confined Niko and the seniors plan to include Yukino in the gift. Sensei's relationship with RABBIT becomes practical support and accountability without absorbing their initiative. Heine's support for Kaya breaks after the recording; legal disposition is not inferred from that rupture. Kanna's official credit and restoration are Miyako's report. V005 C001 E001 unopened.

## V005 C001 E001 relationship state delta — local oppositions and invitations

Nagusa confronts Arata's troupe; the latter calls her 百花繚乱 from her haori, while she rejects the inferred affiliation and claims to have returned something unspecified (`scene:001:u:0001-0042`). Arata is addressed as leader, but her followers' enthusiasm exceeds her own. Niya calls Sensei politely and playfully, offers a festival invitation and mentions a private favor without defining it; Chise's two lines establish presence in the call context, not independent agreement or a Sensei visit (`scene:002:u:0004-0020`). Kuzunoha's address to a would-be rescuer and Sensei's thought of `彼女` imply a prior concern but no current physical meeting or identified third party (`u:0021-0026`). E002 unopened.

## V005 C001 E002 relationship state delta — defended resident and first help

Yukari presses two thugs on behalf of a wallet-losing resident even after that resident asks her to stop; recovered evidence changes the resident's stated belief (`scene:001:u:0003-0029`). The thugs call associates and threaten her and Sensei (`u:0028-0031`). Yukari asks the newcomer who they are and accepts Sensei's offered help (`u:0032-0034`, `choice:001`). This is first direct contact and a pending alliance under threat, not durable trust, a completed defense or Niya reunion. The resident and thugs are incidental roles. E003 unopened.

## V005 C001 E003 relationship state delta — guide and household pursuit

The resident thanks Yukari and Sensei after the thugs withdraw, then assumes her outfit denotes 百花繚乱 before mentioning dissolution; Yukari withholds her uncertain status (`scene:001:u:0001-0025`). She thanks Sensei, momentarily misreads ordinary help through Renge-senpai's reported scam warning, accepts the teacher's identification and initiates a Hyakkiyako tour that narration confirms (`u:0026-0046`). A household servant calls her `お嬢様`, reports leaving the estate after the order news and chases her; relationship and authority are reported, not a complete household history (`u:0079-0089`). Yukari flees after an incomplete farewell. E004 unopened.

## V005 C001 E004 relationship state delta — Niya asks, Yukari intervenes

Niya welcomes Sensei with Kaho/Chise, uses Chise's rehearsals and Shizuko's festival as shared context, and asks for help with a reported Hyakka Ryouran gap while saying she may still hide things (`scene:001:u:0002-0110`). Sensei offers help in principle; Niya treats it as accepted, but terms are not fixed. Kaho respects Niya yet presses her to contribute to recovery work and cautions her phrasing; she reacts warmly to Chise's verse/rehearsal (`u:0012-0045;u:0112-0117`). Yukari, who just fled a servant, enters to ask Onmyou head Niya for counsel and declares Hyakka Ryouran membership (`u:0120-0125`); Niya's response is only puzzled. E005 unopened.

## V005 C001 E005 relationship state delta — witness bargain and personal agency

Niya recognizes a possible 勘解由小路 family connection; Yukari briefly accuses Sensei of preplanned help, then asks Onmyou to witness a challenge against Nagusa (`scene:001:u:0001-0042`). Yukari admires Kikyou's intelligence and reports Ayame/Renge/Kikyou/Nagusa disagreements around succession; only Niya's past Nagusa contact is locally confirmed (`u:0029-0080`). Niya forces Yukari to face political risk and tests whether the appeal invokes family power; Yukari chooses an individual request and worries about burdening Onmyou (`u:0102-0124`). Sensei offers to help; Niya offers witness roles for both, Kaho cautions, and Niya later says the connection may help Sensei seek Kuzunoha knowledge (`u:0125-0161`). No contest or relationship repair follows yet. E006 unopened.

## V005 C001 E006 relationship state delta — remembered praise and missed senior

Yukari tells Sensei Hyakka Ryouran is her aspiration and chosen place. An apparently earlier stand encounter shows Nagusa checking Yukari's safety and praising her courage while Kikyou/Renge pursue the troublemakers; the remembered warmth supports her present attachment without confirming all present loyalties (`scene:001:u:0012-0068`). She expects Renge and Kikyou to endorse a challenge because they were angry at Nagusa's absence, but that is Yukari's projection (`u:0090-0097`). Sensei/Yukari reach Renge's door and only find her youth-journey notice, with no present conversation or consent (`scene:002:u:0002-0018`). E007 unopened.

## V005 C001 E007 relationship state delta — senior esteem and new visitors

Yukari recalls Renge's affection for Kikyou, Nagusa and herself alongside a wish for ordinary friends outside Hyakka; she interprets the present trip as a response to that wish, without current Renge confirmation (`scene:001:u:0001-0036`). A Kaho-supplied list directs Sensei/Yukari through clubs. Yukari describes what Renge means to her before learning descriptive details are needed for strangers; she later recasts sharp member comments as high praise (`scene:002:u:0002-0026;scene:005:u:0009-0019`). The visitors Kaede/Mimori/Tsubaki arrive at the end; reason and relation to the search are unprinted, with one speaker-label inversion (`scene:005:u:0020-0025`). E008 unopened.

## V005 C001 E008 relationship state delta — Shugyoubu meets Yukari, Renge returns

Sensei introduces Yukari and Shugyoubu; Yukari praises its neighborhood watch, while Mimori compares its help to Hyakka and later asks about an unplaced familiarity. Yukari evades rather than explaining a prior bond (`scene:001:u:0001-0049`). The troupe attacks Yukari for a different haori wearer's prior action; Shugyoubu stands with her. Renge arrives, names herself and joins the response; after Arata retreats, named participants report safety and Renge recognizes Yukari (`u:0053-0084;scene:002:u:0001-0011`). No reconciliation/succession request yet. E009 unopened.

## V005 C001 E009 relationship state delta

Yukari admires Renge’s youth search and asks for succession support; Renge calls it 戯言 (scene:001:u:0037-0070). Renge feels Nagusa abandoned members to search for Ayame, while an earlier-memory inset recalls Nagusa’s praise and Kikyou’s teasing with tag inversions (u:0076-0081;u:0105-0115). Renge proposes force; after an omitted clash she refuses to return and leaves with Shugyoubu while Yukari remains still (u:0120-0129;scene:002:u:0001-0022). Sensei asks her to listen and is refused. Present rupture is clear; permanent estrangement is unproved. E010 unopened.

## V005 C001 E010 relationship state delta

Yukari’s image of responsible Renge makes the refusal painful; she resolves to seek Kikyou and predicts Kikyou will persuade her childhood friend Renge (scene:001:u:0001-0021). Renge’s position is not changed by Yukari’s hope. Sensei promises continued accompaniment and helps negotiate a next-day meeting when the household servant insists on a late-day return (u:0022-0055). The servant initially questions Sensei’s proximity but accepts Yukari’s explanation and Schale identification; care/duty is directly stated, deeper family motive is not. Renge’s quoted abandonment line is retrospective (u:0049-0052). E011 unopened.

## V005 C001 E011 relationship state delta

Sensei interrupts the troupe, helps the anonymous student withdraw and checks her right arm; she initially says rescue was unnecessary but notices the care and asks who the teacher is (scene:001:u:0021-0057). Sensei apologizes for a possibly intrusive question, and a narrated walk lets her ask about Hyakka and hear Yukari’s proposed challenge (u:0058-0092). At her residential stop, Sensei asks about return; she calls the timing shrewd and refuses, later describing fear of the remaining members’ judgment (scene:002:u:0002-0016). Sensei regrets the early question and still lacks her name (u:0022-0024). No member has directly condemned her here. E012 unopened.

## V005 C001 E012 relationship state delta

Yukari recalls Kikyou’s protective ice-cream and tooth-brushing admonitions and expects support; present Kikyou greets her warmly but refuses the requested Nagusa challenge witness role (scene:001:u:0011-0025;scene:002:u:0004-0008;u:0052-0065). Kikyou’s account of Nagusa returning Ayame’s 証 and her abandoned-members judgment wounds Yukari’s hope (u:0067-0079). She challenges Yukari’s ability; Yukari calls for a mock, then accepts a strategist-seat succession contest with her (u:0080-0115). Sensei urges calm, Shizuko is alarmed, and neither stops the declaration. Shizuko’s festival request to Yukari is refused, with no wider relationship outcome. E013 unopened.

## V005 C001 E013 relationship state delta

Kikyou humiliates Yukari as a family heir playing at Hyakka; Yukari reveals she knew the odds yet wanted shared days back, then apologizes and leaves (scene:001:u:0019-0056). Afterward Kikyou says she acted to spare Yukari greater injury and that Nagusa is needed, while Sensei and Shizuko challenge deciding Yukari’s belonging for her (u:0057-0094). The protective claim neither repairs the immediate hurt nor proves Kikyou’s affection absent. Shizuko asks Sensei to search, not yet shown successful. Shuro addresses Arata’s frustrated group and offers help; their consent/relation is unshown (u:0113-0119). E014 unopened.

## V005 C001 E014 relationship state delta

Shizuko chooses to continue searching for Yukari despite an imminent festival deadline, then finds her and urges dialogue with Kikyou rather than merely asking for the miko dance (scene:001:u:0013-0059;u:0108-0121). Yukari thanks her but says she fled home and internalizes part of Kikyou’s accusation, despite denying play intent; she agrees to be miko (u:0122-0133). No Kikyou/Yukari conversation follows. Yukari’s earlier meeting with Nagusa is presented as the moment she chose Hyakka beside an admired senior, though the encounter itself does not show formal induction (u:0079-0095). Sensei is separate and hears Shuro’s greeting before any answered Shizuko call (u:0134-0157). E015 unopened.

## V005 C001 E015 relationship state delta

Shuro addresses Sensei as a desired rumored teacher and claims an earlier message was withheld, but no ongoing relationship or binding teacher/student status is established (scene:001:u:0001-0043). Shizuko worries when Sensei misses calls, meets the adult and reports Yukari’s apology-by-proxy; Yukari avoids facing Sensei and says she deceived them, a self-reproach the evidence does not fully validate (u:0044-0082). Sensei rejects Shizuko’s self-blame and entrusts Yukari’s immediate care to her; Shizuko accepts and promises miko preparation (u:0083-0106). Sensei asks Michiru, Izuna and Tsukuyo’s group to find Nagusa for a student’s sake; Michiru accepts, with no Nagusa contact yet (u:0107-0122). E016 unopened.

## V005 C001 E016 relationship state delta

Nagusa directly calls Ayame her childhood friend and says she expected to stay at her side; member praise then transferred replacement expectations to Nagusa after Ayame’s disappearance (scene:001:u:0001-0042). Sensei arrives on the Ninja Research Club lead, recognizes her from E011 and receives her self-name. Nagusa says Yukari should return to family ritual; Sensei asks whether that is right for someone who entered Hyakka admiring her (u:0043-0062). Nagusa explains she cannot replace Ayame and expects the other members to understand later, without directly reconciling with Renge, Kikyou or Yukari (u:0063-0075). Shuro and the troupe enter the scene at the festival cue, with no verified alliance terms (u:0081-0093). E017 unopened.

## V005 C001 E017 relationship state delta

Kikyou contacts Renge about the contest; Renge rejects further concern, while Kikyou names their friendship, jokes sharply and later asks her to check on Yukari in an italic recalled call segment (scene:001:u:0031-0055;u:0115-0118). Mimori, Kaede and Tsubaki notice Renge’s distress and argue she still cares; Tsubaki ends her trial to let her speak, and Renge accepts help (u:0056-0125). No Yukari meeting occurs before attackers arrive. Shizuko repeatedly checks Yukari’s readiness for the miko role while the servant praises her family return; Yukari insists on duty but hesitates (u:0002-0030). Izuna invokes Sensei’s trust to steady Michiru, who then orders protection of attendees (u:0143-0160). Chise redirects Niya toward frightened staff (u:0185-0201). E018 unopened.

## V005 C001 E018 relationship state delta

In an earlier meeting Kikyou welcomes Nagusa back, asks her to address depleted members, then receives an offer to hold Ayame’s 証; Kikyou says she admired Nagusa herself and had not sought a substitute Ayame (scene:001:u:0009-0037). Their misunderstanding remains unrepaired. In current fire, Sensei and Nagusa aid a resident but disagree over risk to strangers; Sensei notes Nagusa has nevertheless come along (u:0038-0059). Renge arrives, names accumulated questions and asks Nagusa to cooperate against monsters, but immediately mistakes her larger-threat retreat warning for abandonment (u:0084-0104). No reconciliation occurs before the giant figure. E019 unopened.

## V005 C001 E019 relationship state delta

Renge asks whether Nagusa as former acting chair can use the emblem; Nagusa says her arm and missing 百蓮 stop her, then again says she is not Ayame (scene:001:u:0036-0050). Shuro claims an earlier Great Snowfield encounter with Nagusa and publicly frames her as a shameful fraud; Nagusa begs her to stop (u:0051-0123). A book-mediated display shows fear of colleagues’ disappointment. Kikyou arrives and asks if it is Nagusa’s true feeling; Shuro asserts complete selfishness, while Nagusa says it was not that simple at first (u:0124-0188). The immediate shock is real; a final reconciled interpretation is not. Sensei calls Tsubaki to act next (u:0198-0199). E020 unopened.

## V005 C001 E020 relationship state delta

Kikyou and Shugyoubu oppose Shuro publicly, while Shuro alleges she helped turn Kikyou’s care for Yukari, Renge’s youth concern and Yukari’s succession hope into damaging choices; these relationships are not thereby reduced to manipulation alone (scene:001:u:0005-0075). Nagusa’s Ayame analogy indicates suspected previous harm but gives no repair or shared account (u:0083-0094). The servant expresses household honor demands; Yukari wonders whether her family wanted only a shame-erasing miko. The anonymous voice amplifies the fear, but no family member is present to answer and Yukari has not accepted revenge (scene:002:u:0014-0060). E021 unopened.

## V005 C001 E021 relationship state delta

Kikyou presses Nagusa for vital information, hears the Ayame testimony, then directly shows the emblem Nagusa left with her (scene:001:u:0019-0048;u:0092-0100). Nagusa’s shame makes her call her persona fake; Kikyou counters by asking for Nagusa herself, yet explicitly says she still cannot forgive the earlier departure and waiting (u:0101-0140). Kikyou admits she did not mean her harsh Yukari words and wants to apologize; Renge likewise wants another conversation and apology, but neither reaches Yukari here (u:0121-0151). Sensei adds an inward plea, and Nagusa agrees to try rescue. Shuro’s public retelling of Yukari’s pain is not Yukari’s own statement; she stays silent (u:0065-0083). E022 unopened.

## V005 C001 E022 relationship state delta

Niya admits error to Sensei, who shares fault and asks her to face the present situation together; she agrees, and Chise/Ninja Research Club aid the route (scene:001:u:0006-0059). Yukari rejects the damage she sees, while Shuro claims to represent and voice her feelings and blames her for the faceless thing; Yukari falls into guilt, without granting Shuro authority or choosing harm (scene:002:u:0001-0063). Nagusa and Sensei appear at the stage demanding Yukari, but no direct response from her or reunification is shown (u:0068-0070). E023 unopened.

## V005 C001 E023 relationship state delta

Shuro claims Ayame rejected Nagusa’s friendship, but the words are only Shuro’s purported quote; Nagusa protests part of the taunt and then descends into self-blame (scene:001:u:0038-0053;u:0077-0092). The book display affirms Yukari’s earlier account that Nagusa showed her a wanted Hyakka path, even as Nagusa interprets her own performed role as having harmed Yukari (u:0064-0084). Sensei attempts to reach Yukari despite restraint and answers Shuro’s identity condemnation; Yukari has not awakened or responded. No reconciliation/rescue is shown (u:0111-0140). E024 unopened.

## V005 C001 E024 relationship state delta

Sensei recalls Nagusa’s attention to each junior and promises help repairing fights, while Yukari says she remains hurt yet wants to make up with the group (scene:001:u:0019-0078). Renge/Kikyou arrive and respond to Yukari, but the requested apologies are still undelivered in direct dialogue (u:0088-0096). Nagusa says she fears losing all three, explicitly asks them and Sensei for help, and receives immediate assent (scene:002:u:0047-0052; interleaved u:0143-0173). Their joint battle and Shuro’s concession are real cooperation, not completed long-term reconciliation. E025 unopened.

## V005 C001 E025 relationship state delta

Kikyou begins but withdraws a talk with Nagusa, whom Renge calls still awkward, so E024 teamwork has not repaired all grievance (scene:001:u:0011-0022). Yukari offers public thanks, receives tentative reciprocation, then challenges Nagusa and accepts defeat while reaffirming admiration (u:0023-0064). She names Hyakka the group’s home and invites return; no full mutual apology is voiced yet and the group has not arrived. E026 unopened.

## V005 C001 E026 relationship state delta

Niya repeats guilt over minimizing the warning, and Sensei praises her protective invitation; she resolves to support Schale through archive work, not a full absolution (scene:001:u:0058-0074;u:0149). Yukari tells Nagusa/Kikyou/Renge she considered her miko choice deeply and that household servants understood; Renge advocates respecting her decision (u:0103-0116). The four proceed to lanterns, with Nagusa addressing Ayame inwardly but no fully voiced mutual apology scene (u:0118-0130). Shuro cries to Kokuriko, who warmly accepts her failed assignment and invites continuing collaboration, a direct hostile mentor/subordinate bond (u:0131-0147). C001 checkpoint due.

## V005 C001 canonical checkpoint reconciliation

Kikyou says she admired Nagusa herself and still resents abandonment; Renge and Kikyou intend apologies to Yukari, and Yukari seeks reconciliation, but their full repair conversation remains unprinted. Nagusa asks for help and receives assent, Yukari reaffirms admiration after a lost challenge, and the four proceed to lanterns. Shuro/Kokuriko directly show a warm subordinate-leader bond with continuing hostile aim. C002 E001 next.

## V005 C002 E001 relationship state delta

Dream-Ayame comforts crying Nagusa, then delivers the same never-friend sentence Shuro alleged. The abrupt nightmare transition says Nagusa fears rejection, not that historical Ayame rejected her (scene:001:u:0011-0031). Awake Nagusa apologizes to absent Ayame and blames herself, with no direct current contact or new repair (u:0032-0041). E002 unopened.

## V005 C002 E002 relationship state delta

Kokuriko directly worries about absent Shuro and asks Azami to greet her; Azami says Shuro is safe, then later tells Shuro Kokuriko may cast her away, which is not supported by the leader’s direct words (scene:001:u:0017-0024;u:0035-0054). Shuro anxiously seeks Kokuriko’s approval, and Azami exploits it while offering help and a future joint story. The eventual leader response is unshown. E003 unopened.

## V005 C002 E003 relationship state delta

The four jointly repel Arata; Nagusa openly credits those fighting beside her (scene:002:u:0001-0012). Dessert tasting shows Renge teasing Kikyou, Kikyou caring over Yukari’s cream/teeth, Nagusa joining with a meatball suggestion, and Umika reciprocating festival thanks (u:0034-0053). After the arm mishap Renge urges hospital care, Kikyou asks to see the bandage and Yukari offers a family treatment route; Nagusa minimizes it. Their concern is direct; care result remains future (u:0075-0093). E004 unopened.

## V005 C002 E004 relationship state delta

The servant warmly welcomes Yukari and acts on her request for Nagusa, a direct supportive household response despite the miko exit (scene:001:u:0009-0023). Renge worries over the doctor’s arm account, Kikyou challenges the examination and Yukari presses for treatment; Nagusa confirms 黄昏 origin but remains restrained (u:0040-0081). She asks all three to hear the frightening unspoken Ayame story, an opening to trust not yet the content itself (u:0082-0085). E005 unopened.

## V005 C002 E005 relationship state delta

Nagusa confesses both her Ayame rejection memory and fear that her juniors would be disappointed; Yukari explicitly refuses blame and credits her search (scene:001:u:0089-0098). Kikyou and the others defend a more charitable reading of Ayame and propose rescue, but their manipulation theory is not proven, and the Renge-like u:0103-0104 line is Yukari-tagged. Nagusa does not consent to an immediate group trip, citing danger and institutional duty (u:0099-0107). Kokuriko's remembered interposition between Ayame and Nagusa does not expose Ayame's interior motive. E006 unopened.

## V005 C002 E006 relationship state delta

Kikyou acknowledges Hyakka’s debt to Onmyou; Renge/Yukari greet Sensei warmly and Nagusa more quietly (scene:001:u:0001-0023). Hyakka members support Nagusa’s mission decision. Kaho’s affection for Chise coexists with her insistence that Chise stay for the festival; Sensei promises a later trip (u:0084-0090;u:0110-0115). E007 unopened.

## V005 C002 E007 relationship state delta

Kikyou helps Yukari with cold, the four share local food and a bath, and Yukari explicitly wants time with her seniors. Kikyou initially refuses bathing on mission grounds then agrees for one hour, while Renge teases her startle (scene:001:u:0002-0010;scene:003:u:0040-0054,u:0068-0103,u:0123-0133). Yukari/Kikyou notice Nagusa’s tension; she discloses fear of aiming at an unspecified person, not its resolution (u:0104-0136). Azami hosts them while withholding her E002 allegiance. E008 unopened.

## V005 C002 E008 relationship state delta

Shuro taunts Nagusa’s childhood-friend hope, and Nagusa counters with a direct cause question without receiving an answer (scene:001:u:0026-0040). Nagusa says she will act for the group; Kikyou, Renge, Yukari and Sensei reach her and interrupt the encounter (scene:002:u:0001-0016). A voice the group recognizes is Ayame-tagged and greets them, but relationship restoration and actual identity remain open (u:0025-0032). E009 unopened.

## V005 C002 E009 relationship state delta

The Ayame-labeled figure apologizes to Nagusa and calls her a dear friend, while Nagusa is ready to accept reassurance after conflicting memory (scene:001:u:0015-0019,u:0062-0076). Kikyou stops easy absolution, foregrounds Nagusa’s injury and chooses to trust the deputy’s crisis conduct until a full account is given; this is conditional relation repair, not a legal verdict (u:0077-0085). Yukari hopes the misunderstanding clears; Azami serves food without disclosing her E002 allegiance. E010 unopened.

## V005 C002 E010 relationship state delta

Ayame-labeled figure offers captive Shuro food without requiring disclosure, yet Shuro refuses leeks as they keep urging/approaching; no feeding is printed (scene:001:u:0058-0090). Kikyou draws Sensei and juniors aside, excluding Nagusa out of concern; Renge defends the figure’s rescue act, Yukari expresses both doubt and desire to preserve Nagusa’s smile (u:0091-0140). Sensei urges limited judgment and further engagement; Kikyou retains suspicion and has not forgiven Nagusa’s injury (u:0141-0159). E011 unopened.

## V005 C002 E011 relationship state delta

The Ayame-labeled figure says she believes Nagusa and wants her help for a final chair mission; Nagusa accepts, while Kikyou defers to her without abandoning suspicion (scene:001:u:0041-0060). Shuro is brought against her will and nonconsensually searched for a dangerous book; her private manuscript is read aloud over protest, Sensei apologizes and later encourages writing (u:0061-0125). The protective reason and privacy cost are both visible; no feeding or redemption outcome. E012 unopened.

## V005 C002 E012 relationship state delta

Shuro’s fear of Kokuriko rejection repeats the abandonment vulnerability Azami exploited; Kokuriko’s direct C001 comfort still constrains the feared verdict (scene:001:u:0010-0018). Kikyou worries about Sensei staying with Shuro/Azami and names his self-sacrificing habit; he reassures via choice lines, no harm yet (u:0019-0029). Kokuriko claims family/Hyakka kinship with Yukari, who rejects becoming like her and cites seniors’ promise; Kokuriko threatens punishment, no strike yet (u:0094-0113). E013 unopened.

## V005 C002 E013 relationship state delta

Shuro denies true fear, but inwardly worries Kokuriko discarded her and dreads an unnamed former place; actual Kokuriko intent remains unknown (scene:002:u:0015-0046). Sensei rescues the student who had just threatened him; she does not accept moral reform and acknowledges his vulnerability (u:0047-0059). Renge blames Azami for letting him go, while Kikyou turns suspicion on her and Azami acknowledges discovery (u:0060-0076). Yukari/Nagusa relation outcomes remain offscreen. E014 unopened.

## V005 C002 E014 relationship state delta

Kikyou directly accuses Azami; Azami compliments her, drops cover and taunts the group’s separation from Sensei/Nagusa, confirming antagonistic relation rather than trusted host (scene:001:u:0001-0035). Nagusa asks Ayame to flank Kokuriko, then the companion vanishes/voices never-with-you claim, rupturing Nagusa’s recent trust; Kokuriko presses her memory conflict (scene:002:u:0001-0029). No resolution of actual Ayame bond. E015 unopened.

## V005 C002 E015 relationship state delta

The Ayame-labeled speaker claims she has always hated Nagusa’s dependence and others’ repeated requests, directly harming Nagusa; authenticity and enduring past motive remain open (scene:001:u:0030-0049). Nagusa argues Kokuriko deceived her and tries to talk, while the speaker rejects her. Earlier warm companion is labeled a fear-made something by this same speaker, no independent group perception. The repeated friend-denial line closes via narrator tag (u:0050-0053). E016 unopened.

## V005 C002 E016 relationship state delta

Kokuriko offers tea and praises Shuro despite two failures, contradicting Shuro’s fear of immediate disposal; she later evades Shuro’s distress about creature betrayal and personal origin (scene:001:u:0001-0018,u:0035-0058). Shuro recalls Sensei’s rescue yet cannot reconcile it with enmity, guessing whim rather than receiving his inward motive (u:0020-0034). The earlier Ayame-like companion’s seeming subjectivity troubles her. E017 unopened.

## V005 C002 E017 relationship state delta

Kaho presses Niya to do festival paperwork; their banter shows work accountability (scene:001:u:0001-0021). The Ayame-shaped visitor apologizes for absence and invokes endangered Hyakka/Sensei; Niya orders help but then challenges the visitor based partly on her known Ayame’s unwillingness to abandon colleagues (u:0022-0069). The visitor’s non-caring reply breaks the impersonation without settling original Ayame’s relationship history. E018 unopened.

## V005 C002 E018 relationship state delta

Renge and Kikyou quarrel over force versus planning while confined; Yukari tries to calm them, and they attend to waking Sensei (scene:001:u:0001-0030). Juniors protect Nagusa from self-blame, but Kikyou's blame of Ayame and Nagusa's refusal expose unresolved interpretations of the original bond (u:0037-0049). Shuro weaponizes the pleasant Ayame account and threatens abandonment; Sensei's E013 rescue interrupts her all-acted defense, though she says it will not change loyalty to Kokuriko (u:0050-0094). Her later Kuzunoha offer is tied to hopes of Kokuriko approval, not a verified generous rescue. E019 unopened.

## V005 C002 E019 relationship state delta

Shuro uses Sensei's physical vulnerability to compel the group while criticizing his rescue of her; Sensei asserts a duty to protect children, which she rejects as impossible or meaningless for a vulnerable adult (scene:001:u:0015-0032;choice:001-002). Nagusa's confidence in the snowfield route contrasts with Shuro's suspicion at the apparently ruined temple, where Shuro threatens the party before the change (scene:002:u:0001-0027). The Kuzunoha-labeled speaker greets Nagusa as a familiar junior, and Nagusa says she fulfilled the speaker's wish to bring Sensei; reciprocal recognition is present, while trust and identity testing remain future (u:0028-0035). E020 unopened.

## V005 C002 E020 relationship state delta

The elder speaker chides Sensei for late response to her letter yet acknowledges many students wait for him, with his substantive answer interrupted by Shuro (scene:001:u:0008-0018;choice:001-003). Nagusa asks why Ayame was not granted Kuzunoha's recognition; the speaker rejects the no-one-would-hurt counterfactual and challenges Nagusa's perfect-Ayame image (u:0034-0075). Nagusa accepts that only Ayame knows her full self and wants to be by her side even if rejected; reunion is future, not achieved (u:0076-0096). Shuro rejects honest-understanding assurances and voices lost-book fear; advice about a book of her own does not reconcile them (u:0097-0114). E021 unopened.

## V005 C002 E021 relationship state delta

The Ayame-tagged account describes praise, minimization of requests and colleagues expecting a quick return to the usual chair, a burden narrative without individual guilt findings for every past student (scene:001:u:0001-0032). It depicts Nagusa's earlier Kuzunoha skepticism and an Ayame-labeled resentful inner response, but the montage's original-person fidelity remains uncertain (u:0033-0048). In the present exchange, Azami flatters/recruits the story-form's regret and hatred into a gaze-based threat; the figure says she will stop answering others, then stays silent after the attack instruction, so no precise consent or outcome is shown (u:0049-0076). E022 unopened.

## V005 C002 E022 relationship state delta

Kaho prioritizes Chise's safety, then issues crowd-protection orders as Onmyou members report pressure; Shizuko's ignorance of eyes is relayed, not direct coordination yet (scene:001:u:0001-0056). Sensei's reported preemptive request creates a protective link to Niya/Onmyou through the Ninjas, though they admit they failed to help during her shadow fight and act only after she is confined (u:0057-0107). Niya trusts them with a message; Kaho interprets it and asks them to bring Shizuko, with no response from Shizuko yet (u:0108-0118). E023 unopened.

## V005 C002 E023 relationship state delta

Kaho offers Festival Operations Committee members a route to leave; Umika, Fina and Shizuko voluntarily remain, with differing reasons around prior helplessness, future festivals and collective preparation (scene:001:u:0006-0032). The Ninjas join and Kaho entrusts Chise with singing under a promise to shield the stage, untested at cutoff (u:0033-0044). Azami tries to dominate confined Niya with fear-book theory; Niya rebuts through a communal festival and the observed thinning weakens Azami's certainty, though the antagonist warns it will end (scene:002:u:0001-0075). E024 unopened.

## V005 C002 E024 relationship state delta

Niya thanks the returned group, while Yukari/Nagusa treat her injury despite her minimization and Sensei says none can do everything alone (scene:001:u:0001-0030). Niya/Nagusa self-blame for Ayame, and Kikyou/Renge/Yukari insist on shared responsibility; details learned in the omitted briefing are not audited (u:0031-0039). Niya appeals to Shuro's authorship and resentment of mocking readers to induce a new story; Shuro resists Kokuriko disloyalty verbally but writes, leaving motives and long-term bond unsettled (u:0084-0154). E025 unopened.

## V005 C002 E025 relationship state delta

Azami threatens Shuro for humiliating her tale; Kokuriko protects Shuro and rebukes Azami, complicating Shuro's disposal fear without defining their relation (scene:001:u:0001-0031). Kokuriko calls Nagusa a junior and attacks her bond with Ayame; Nagusa rejects senior status and reaffirms staying with Ayame, while Kikyou shields her from the verbal attack (u:0041-0075). No reconciliation, surrender or Ayame meeting. E026 unopened.

## V005 C002 E026 relationship state delta

Renge/Kikyou/Yukari voice role anxieties under Kokuriko's imposed darkness; the claims reveal possible insecurities without proving loved ones reject them (scene:001:u:0011-0033). Sensei argues mutual understanding can be pursued through questions/learning despite uncertainty, while Kokuriko calls it empty hope (u:0027-0037). Nagusa cannot substitute for Ayame but chooses to extend a hand and call herself her best friend; Kokuriko admits prior pressure on Ayame and reports her siding with the antagonist, without Ayame's direct reply here (u:0038-0071). Sensei agrees to witness Nagusa's risky confrontation. E027 unopened.

## V005 C002 E027 relationship state delta

Nagusa offers to take Ayame's chair burden rather than demand comprehension; Ayame refuses the understanding premise but accepts a formal challenge (scene:001:u:0001-0028). Ayame fears being unrecognized without office/earnestness and treats Nagusa's presence-is-enough reply as tactics (u:0029-0054). In an italic apparent aftermath Nagusa apologizes for missed distress and pledges to hold hands/share pain, while Ayame says she disliked Nagusa's crying face; this does not settle all past friendship or exclusive blame (u:0055-0071). E028 unopened.

## V005 C002 E028 relationship state delta

Niya/Kaho's medical rest and Sensei's visit show practical care; Niya's Shuro praise was tactical as well as genuine reading, while Shuro and other antagonists vanished (scene:001:u:0002-0052). The Ninja Club's claim that Nagusa's friendship must have prevented Ayame wrongdoing is wishful and cannot undo the witnessed crisis (scene:002:u:0011-0024). Nagusa reports Ayame physically back but asleep, declines forced awakening and stays near her without claiming to know her thoughts; shared gardening continues among Hyakka (scene:003:u:0002-0046). C002 checkpoint due.

## V005 C002 canonical checkpoint reconciliation

The chapter moves from isolated idealization to offered presence: Nagusa asks to take Ayame's chair burden and later waits beside her unawakened body, with no reciprocal current assent. Hyakka members share responsibility; Sensei, Ninjas and festival workers provide bounded help. Kokuriko protects Shuro from Azami, but their special tie and Shuro's future allegiance remain unknown. The E028 public created-Ayame account and friendship-guarantees-innocence reassurance do not settle original Ayame's moral or physical identity. 274/480; V006 C001 E001 next.

## V006 C001 E001 relationship state delta

Maia measures herself against Squad's chosen path but no member speaks or is shown with her (scene:001:u:0007-0012). Role-labeled employer/lender/boss interactions are exploitative or rejecting by represented speech, without full bargaining records (u:0017-0027). Subaru offers Maia rest, names both students and promises Arius belonging; Maia responds, but trust history and institution-wide capacity are not established (u:0046-0056). E002 unopened.

## V006 C001 E002 relationship state delta

The Remedial Club's familiar teasing and Koharu's boundary protests continue, with no romantic or disciplinary event enacted (scene:001:u:0001-0010,u:0049-0060). Reisa asks Suzumi to affirm her creed, and Suzumi gently corrects her; Ui and Shimiko share a chair/member study check complicated by source-label drift; Kazusa, Natsu, Yoshimi and Airi show a Sweets Club group-study attempt without outcome (u:0061-0089). Hasumi describes Justice Committee time pressure, Ichika accepts that duty and helps Mashiro approach ethics study, not resolve the disagreement (u:0109-0118). Sensei spots a privacy need; Hinata and Marie persuade Sakurako to accommodate it, a concrete collaborative correction (u:0119-0130). Two shy unnamed students ask Sensei for time without saying why. No new relationship commitment beyond what is shown; E003 unopened.

## V006 C001 E003 relationship state delta

The two Arius transfer students share a room, deliberated about transfer, gently correct one another and jointly ask Sensei about exams and those remaining at Arius (scene:001:u:0001-0085,u:0130-0166). They report welcoming Trinity peers and café companionship under a rural-transfer cover, while only part of the Tea Party is said to welcome them institutionally (u:0030-0044,u:0115-0123). Their concern for stayers and Squad is direct; no present reciprocal contact with either is shown (u:0130-0145,u:0194-0196). Sensei apologizes for inattention, initially startles them by reaching for their heads, slows and explains, then spontaneously ruffles their heads; B later explicitly asks him to continue. The two contacts and responses should not be flattened into general trust or general consent (u:0064-0100,u:0167-0177). His adult-role promise is relational assurance awaiting material follow-through. E004 unopened.

## V006 C001 E004 relationship state delta

Atsuko has Sensei's number saved, jokes with him and insists serious matters be discussed face to face with all of Squad; he first misreads her point as interception risk and then agrees (scene:001:u:0001-0042). She says Saori remains contactable and sometimes seen, reports Misaki's mixed reaction, and asks Sensei to help with Saori, which he accepts (u:0043-0062). Saori visibly joins Hiyori, Misaki and Atsuko at the ship; Hiyori clings to togetherness, while Misaki offers her temporary leadership back, without an opened durable command settlement (u:0086-0101). Saori responds empathetically to anonymous transfer students' adaptation burden, not through direct acquaintance here (u:0117-0122). The group presses Sensei on the purpose of study and only provisionally receives his answer. Nagisa enters as meeting sponsor before any reconciliation with Squad. E005 unopened.

## V006 C001 E005 relationship state delta

Nagisa and Squad exchange names across an old adversarial history. Hiyori panics, Misaki distrusts the undisclosed sponsor, Saori agrees to hear her out, and Atsuko steadies the group without suppressing objection (scene:001:u:0001-0043). Nagisa hosts food/tea; Hiyori visibly enjoys it, but Misaki asks why Nagisa already knows the transfers' consultation and does not accept a bare intelligence explanation (u:0044-0115). Sensei offers his own fact-check and trust request, but her concern is not conclusively resolved. Nagisa apologizes for Trinity's historic wrong; Atsuko apologizes for Squad's terror, while Saori acknowledges more owed words but defers them (u:0119-0193). Atsuko offers bounded trust because Nagisa recognizes paternalism risk; raw u:0211 attribution is unstable, so no group-wide unqualified consent follows (u:0194-0224). E006 unopened.

## V006 C001 E006 relationship state delta

Saori is again called leader and Squad jokes about Misaki's interim role, but Misaki directly reproaches Saori's disappearances; the command arrangement is still relational rather than formalized (scene:001:u:0001-0020). Nagisa requests Sensei teach Arius students, Saori accepts an escort role despite worry that her Arius history adds danger, and Atsuko welcomes Sensei's presence (u:0021-0049). Separately Subaru calls for applause for Maia, thanks her for returning, asks for her account and validates her exclusion rather than dismissing outside beauty (u:0050-0102). She says she would not stop Maia going to Trinity, while Maia's anxious denial and solidarity with Subaru do not settle private preference (u:0103-0112). Subaru's directed anger at Saori/Squad marks a conflict that has not yet reached the travelers; no mutual exchange or resolution occurs (u:0113-0115). E007 unopened.

## V006 C001 E007 relationship state delta

Atsuko and Saori consider Nagisa's indirect exam-paper route; Misaki's pay question and doubts about Tea Party show bounded cooperation, not allegiance (scene:001:u:0001-0046). Maia and two excited students coax embarrassed Subaru to play; she does, and Maia feels more fully home, adding an ordinary supportive interaction alongside Subaru's E006 resentment (u:0047-0079). Saori knows Subaru by memory but describes conversation with her as oddly misaligned; the two have not yet met here (u:0098-0115). Saori expresses fear of Sensei being harmed, begins an apology, and Sensei redirects to his report of transfers' thanks. Misaki/Atsuko keep Squad wrongdoing clear (u:0119-0151). Alarmed Arius residents voice anger and fear at Squad's reported entry; Subaru chooses an uncertain reception with safeties engaged, not a completed attack (u:0174-0215). E008 unopened.

## V006 C001 E008 relationship state delta

Subaru and Saori meet directly for the first time in this run; their old communication mismatch appears in Saori's premature conclusion and Subaru's angry interpretation, against residents' remembered special treatment and abandonment grievance (scene:001:u:0001-0068). Sensei's polite contact is provisional: Subaru welcomes him only for now and challenges whether his student-duty argument applies to Arius (u:0069-0099). Anxious residents wonder if they may live as students. Subaru rejects Squad's worth, orders safeties released, and Squad prepares; Atsuko says she need not remain only protected while Misaki directs Sensei back and requests command (u:0100-0132). This is open antagonism, not completed mutual trust, forced teaching or a settled exclusion. E009 unopened.

## V006 C001 E009 relationship state delta

Squad wins a narrow contest by Saori's account but remains resented by residents; at least one resident is reported unconscious after shots strongly implied to be Atsuko's response to insults against Sensei, and others cower (scene:001:u:0001-0033). Sensei does not address that harm before starting class in the represented text. He suddenly entrusts Squad with teaching, catching Misaki and Saori unprepared; Saori accepts, Maia questions, and residents engage unevenly (u:0034-0095). Misaki, Atsuko and Hiyori also teach, and narration notes Hiyori's strongest reception and some reduced wariness (u:0096-0149). This is local contact, not resident forgiveness or consent to the prior force. Subaru gives no spoken postclass assessment. Saori offers Sensei a rough place to sleep and asks for a private consultation, topic pending (u:0150-0157). E010 unopened.


## V006 C001 E010 relationship state delta

Saori and Sensei move from classroom praise to a requested, assented scar encounter: she touches the wound trace, apologizes and collapses crying, and he comforts her while asking for future deliberation (scene:001:u:0001-0140). This is a meaningful dyadic opening, with enduring injury and no collective Arius or legal absolution. She thanks him, asks to sleep beside him, retracts it as a joke, and privately calls it half true after leaving; no shared night or mutual romance is shown (u:0159-0175). Saori reports slightly more Arius conversation after class, but Subaru tells Maia a narrow defeat does not erase Arius hatred (u:0141-0149,u:0176-0187). Maia trusts Subaru enough to ask about food, is frightened by the mercenary account, then asks for music. Subaru says students' eating/laughter sustain her and wants a limited refuge for abandoned children, while her coercive work may also endanger others (u:0188-0303). Saori's unknown encounter at the end has no identifiable relationship yet. E011 unopened.


## V006 C001 E011 relationship state delta

Arius students accept Sensei's outing enough to follow him and sometimes obey shared-space requests; they explicitly contrast this with earlier adults' blows/threats. Their curiosity, play and attention do not retrospectively settle E008-E009 coercion or turn them into compliant enrolled pupils (scene:001:u:0102-0166). Maia feels a memory jolt; Subaru speaks for her to Sensei and asserts her prior counseling role, with Maia acquiescing but inner state not resolved (u:0041-0057). Squad is left behind because wanted status limits exposure; residents remain worried about trusting them and Misaki wishes to join. Subaru probes Sensei's conception of Squad but is interrupted (u:0067-0092). A passerby temporarily mistakes Subaru and Sensei for fellow teachers; Subaru denies it (u:0093-0101). At the park she serious-mindedly asks about giving up life, receives Sensei's non-guarantee answer, then tests whether he could be her reason; he hopes to be, without exclusivity, promise of rescue or identified immediate crisis (u:0185-0232). E012 unopened.


## V006 C001 E012 relationship state delta

Maia seeks Subaru to help a child's kitten; Subaru catches it after a gunshot, but the child cries harder and an older sister rebukes the risk. Crowd Arius stigma triggers Maia's distress. Subaru helps her stand and reassures her, while privately withdrawing from the E011 hope Sensei offered (scene:001:u:0001-0082). Arius residents credit Subaru for tea, strengthening their reported reliance without identifying a funding stream (u:0083-0088). Suzumi/Reisa greet the Arius group; A/B laugh with Reisa, whereas C/D remain silent and later say hopeful talk angers them. Suzumi worries she offended them, Sensei asks for patience, and Subaru privately validates C/D but intensifies the Trinity grievance frame (u:0091-0235). The outing closes with A affirmative and C hesitant. Mine/Serina arrive at Arius after Squad has remained there, with rescue relationship still unestablished (u:0236-0252). C001 checkpoint next.


## V006 C002 E001 relationship state delta

Sensei gathers Squad, Maia and Rescue Knights, asks Mine's team to conceal Trinity/Knights names, and Serina persuades a reluctant Mine. Mine accepts Serina/Hanae calling her 先輩 and appreciates its friendliness (scene:001:u:0001-0056). Serina worries about working with Squad; Atsuko self-calls Squad Arius outsiders, briefly teases a Hanae stay and retracts it. Maia is overwhelmed by the visitors' energy (u:0057-0081). Subaru identifies the Trinity volunteers, permits them to work discreetly if not Tea Party/Sisterhood agents and offers help, yet retains a false impression that Mine is absent after the group plays along (scene:002:u:0006-0071). Mine privately admits Arius anger unsettles her and she cannot claim full understanding. Sensei listens and shares a bounded belief/teacher ethic; she leans briefly against him for rest, without a wider relationship conclusion (u:0080-0133). Multiple people hear a trumpet-like disturbance; no aggressor relationship established. C002 E002 unopened.


## V006 C002 E002 relationship state delta

Arius students queue for Rescue Knights supplies and ask about food, clean water and kits, with gratitude but no displayed full community assent to Trinity service (scene:001:u:0001-0026). Maia challenges math's usefulness and remembers outside humiliation; Sensei apologizes as an adult, while Misaki offers a hard-edged selective-attention response and speaks of living because Sensei urged her to try. She also rebukes his tempting hope, and their lifetime quip is rejected rather than accepted as a pledge (u:0027-0086). Saori shares a gentler possible reading of her old futility phrase, with an explicit chance that reconciliation never comes; Squad reacts supportively (u:0087-0098). Subaru, Mine and Squad respond to sudden visible entities, with Mine promising protection and Saori defending Arius as alma mater; no joint combat outcome or trust repair yet (u:0099-0130). C002 E003 unopened.


## V006 C002 E003 relationship state delta

Misaki tries to move Atsuko back, Mine warns others, and Squad/Knights cry out in the first represented impact, with injuries unexamined (scene:001:u:0001-0012). Mine's encounter with anonymous historical/child voices changes her private view of Arius anger, but no Arius student's own new testimony or consent to her services is shown during this passage (u:0013-0072). She recalls Sensei's real belief answer, rejects a false memory that he commanded belief, and uses an imagined Sensei encouragement to formulate her own smaller rescue promise; this is her inner relation to him, not a new shared dialogue (u:0073-0132). By revealing Rescue Knights/団長 she alters the public relationship under E001's cover, but no response from Arius residents or battle outcome follows yet (u:0133-0137). C002 E004 unopened.


## V006 C002 E004 relationship state delta

Serina/Hanae urgently care for collapsed Mine and disclose captain/order labels to residents; student B recognizes Mine from Madam's departure and reacts with fear (scene:001:u:0001-0015). Sensei/Squad prioritize passage for the Knights; Subaru allows it for now despite conflict, a bounded cooperation. Sena joins by Sensei's call and coordinates planned transport with the Knights, without completed arrival (u:0042-0080). Mine's brief awakening turns toward Sensei: she credits his words for return, asks him to keep Arius students' ordinary life intact and receives his promise. She lapses again (u:0081-0145). A retrospective shows Nagisa's personal request to Mine, including Mine's frank discomfort with Tea Party pressure but lack of personal animus; this refines rather than erases Trinity–Arius legitimacy tension (u:0102-0129). Atsuko/Saori share a grave but explicitly provisional angel/world-end reading with Sensei (u:0151-0156). C002 E005 unopened.


## V006 C002 E005 relationship state delta

Subaru convenes residents, shares her own uncertainty and asks them to report trumpet hearing, then voices an unproved Trinity/Sensei cause. Students split in their relationship to Sensei's lessons: C/D resent them and Squad, while A/B value being heard or studying instead of violent training (scene:001:u:0001-0124). Maia challenges the blame, but her hopeful answer rests on asking Sensei; angry students call this outside influence and demand Subaru prove allegiance. They directly articulate pain at Saori/Squad leaving despite their former admiration (u:0125-0190). Subaru asks Maia's hearing status, apologizes, orders her escorted out of the basilica and bars return there, then dismisses others and stays with Maia. Maia begs not to be abandoned and Subaru sobs, without a clear reconciliation or final motive (u:0191-0233). The command damages trust even if a protective reason may later emerge; all-Arius exile is not shown. C002 E006 unopened.


## V006 C002 E006 relationship state delta

Misaki pushes back against Sensei's reassuring language; Atsuko refuses to let him bear sole responsibility and proposes shared thought about Squad's future (scene:001:u:0001-0024). Residents C/D resent his class notice, while D still considers bringing Maia a blanket; Subaru's stern sleep order suppresses that care and the group follows her toward Porta Pacis despite A/B's concern over missed lessons (u:0049-0088,u:0165-0179). Maia, isolated and despairing, turns toward Sensei. He gives practical comfort and a place to sleep without extracting her account; she cries, sleeps and remains at the next class (u:0089-0164,u:0180-0184). This establishes a bounded night of trust, not a settled repair with Subaru or a permanent care arrangement. Sensei calls Subaru without an answer (u:0185-0190). C002 E007 unopened.


## V006 C002 E007 relationship state delta

Atsuko deliberately lowers Maia's princess distance, asks to be called by given name and initiates a handshake; Maia's hesitant honorific shows the hierarchy is not instantly undone (scene:001:u:0034-0044). Squad question Atsuko's previously unshared information; she apologizes and Saori judges disclosure may have endangered them, leaving its exact source unresolved (u:0045-0052). Sensei recruits Ui/Shimiko as knowledge partners; Shimiko's offer of magazine records gives Hiyori a concrete welcome and Sensei vouches for Atsuko's former Royal Blood identity before Ui speaks (u:0053-0097). Ui and Atsuko contribute differing partial histories without displaying records; this is cooperation under acknowledged archival limits, not reconciled institutional trust. Atsuko speculates Subaru found something; direct Subaru response absent (u:0159-0170). C002 E008 unopened.


## V006 C002 E008 relationship state delta

Maia says she heard trumpets and thinks Subaru did not, but becomes distressed when asked about her overnight arrival. Sensei signals waiting, Hiyori recommends speaking to a trusted person and offers privacy, and Ui/Shimiko offer to suspend their call (scene:001:u:0119-0163). Maia instead asks the group to hear her, checks with Sensei and recounts last night in narration; listeners respond with sympathy, without a printed account of every event (u:0164-0193). This is her chosen audience, not compulsory disclosure or guaranteed repair with Subaru. Ui's conjecture identifies hearers as potentially open to outside knowledge, and Shimiko warns others might mark them enemies; neither social division nor supernatural selection is confirmed as causally proven (u:0194-0238). At the gate Subaru tells residents to fortify and goes forward alone; fear and obedience coexist, but no completed encounter follows (u:0088-0118). C002 E009 unopened.


## V006 C002 E009 relationship state delta

D/C return to Subaru after fortifying, ask her to name a group that can stand beside Squad, and accept ニコメディアトゥループ without understanding its meaning. She yields to their request while limiting the name to those gathered (scene:001:u:0036-0065). Maia fears Sensei cannot be forgiven, but he insists on speaking; she reads future possibility and wants to emulate both him and Subaru despite the prior-night exclusion (u:0066-0080). Saori doubts Maia's Subaru loyalty; Misaki describes Subaru's unconscious influence over followers, and Atsuko acknowledges her work while judging effort insufficient. Squad affirms Saori as their leader (u:0081-0090). These are voiced evaluations rather than closure of Maia–Subaru trust or a meeting between leaders. Subaru's later anonymous voice encounter has no identified relationship partner (u:0119-0139). C002 E010 unopened.


## V006 C002 E010 relationship state delta

Saori directly states she seeks conversation despite residents' resentment, but defenders construe Subaru's order as barring entry and the contact escalates to gunfire; neither side gets a face-to-face meeting with Subaru (scene:001:u:0001-0025). Subaru tells C/D that talk is a tactic and reinforces anti-Sensei blame, then privately says she lied and should apologize; no apology or precise lie target is shown (scene:002:u:0015-0035). Her nest ethic and private admission that she drove Maia away coexist with judgment that Sensei/Squad threaten the home. This narrows her responsibility but does not repair trust (u:0036-0057). A/B doubt the clash and recall Sensei's goodness despite continuing defense (u:0072-0077). The voice offering force is unidentified, so no stable relational tie to it is modeled (u:0064-0071). C002 E011 unopened.


## V006 C002 E011 relationship state delta

Misaki and Atsuko insist Arius peers under entity attack cannot be abandoned, and Saori leads defense even after conflict with the gate guards; the fight yields retreat rather than victory (scene:001:u:0009-0023; scene:002:u:0001-0010). A/B reach Sensei through a white-flag MomoTalk lead, ask after Maia and thank him for her shelter. Their route offer reciprocates his aid and their mixed lesson appraisal while they continue to value Subaru as the senior who held residents together (scene:002:u:0011-0059). The group descends to Subaru despite warnings and experiences of pressure. She recognizes Sensei's purpose but asks to move first; contact is restored, not repaired trust, forgiveness or a resolved Maia relation (u:0060-0086). E/F and A/B remain local anonymous roles. Chapter 2 checkpoint next.


## V006 C003 E001 relationship state delta

Subaru confronts Sensei over differential care for Mika/Squad versus Arius stayers, while his recollection shows two interim Tea Party representatives asking him to let Trinity handle its own affairs. Their claimed mandate and Sensei's affirmative answer are unseen (scene:001:u:0016-0043). Subaru grants he may have little direct blame but says his trust left returnees unseen and refuses to forgive a possibly innocent person. She asserts Arius autonomy yet voices a collective rejection of outside lessons despite documented resident disagreement (u:0044-0093). She offers a conditional no-harm pledge if Sensei takes Squad away forever; neither agrees on page. Saori asks about the path's endpoint, keeping dialogue open at the cutoff (u:0094-0116). Maia is not directly addressed in the demand, so her belonging remains unresolved. C003 E002 unopened.


## V006 C003 E002 relationship state delta

Saori admits she was Arius's strict instructor and Subaru the kind centurion, validates Subaru's lost-children care, then asks where her method leads. She offers an insider appeal to see alternatives rather than an outside order (scene:001:u:0001-0049). Sensei's earlier equal-talk/chance lines return in Saori's inner account; no new Sensei speech in this scene produces her change (u:0050-0059). Subaru invokes Squad's flight and resents Saori's plan to surrender as a moral posture that erases stayers. Saori accepts past wrongdoing but says her life is now precious. Subaru hears that against her own nest burden and becomes volatile; no forgiveness or mutual agreement occurs (u:0060-0139). Squad place Sensei behind them as danger rises (u:0140-0151). C003 E003 unopened.


## V006 C003 E003 relationship state delta

Saori/Squad worry over her harm while residents react to a darkening sky and sound, but no resolution of their clash with Subaru follows (scene:001:u:0001-0020). Saori's call seems not to reach Subaru. Maia's direct “Subaru senior” call draws a startled reply about where she has been, although she accompanied the group. Atsuko interprets this as Subaru refusing to look at Maia, a relational charge rather than proof of literal invisibility (u:0021-0033). Atsuko then rejects Subaru's exclusive claim to be Arius, labels her a trumpet phenomenon and says she will explain; no mutual acceptance or Maia–Subaru repair is shown (u:0034-0040). C003 E004 unopened.


## V006 C003 E004 relationship state delta

Atsuko thanks Saori, Sensei, Misaki and Hiyori for giving her a self beyond sacrificial Royal Blood symbolism, then confronts Subaru with privileged knowledge rather than letting Subaru alone speak as Arius (scene:001:u:0001-0033). She judges Subaru's Maia exclusion a loss of legitimacy and calls Maia's turn to Sensei consequential, without establishing the supernatural counterfactual (u:0049-0064). Subaru's faint response suggests she hears some appeal but no repair is confirmed. Hiyori prompts Maia to speak. Maia says she still loves and trusts Subaru along with Arius and Sensei, yet corrects that not everything is okay and asks for help to make Arius a better school (u:0065-0090). Her attachment does not cancel the earlier injury; Subaru's answer remains unopened. C003 E005 next.

## V006 C003 E005 relationship state delta

Maia gives Subaru her dropped harmonica and asks to hear her again someday. Subaru inwardly faces unwanted consequences but disappears before accepting Maia's E004 request (scene:001:u:0001-0012). Residents' Subaru-like third-figure report prompts Sensei and Squad to seek her; it is not a direct Subaru answer (u:0013-0022). Atsuko finds a way to address Subaru during an apparently prayer-like gesture, acknowledges Trinity harm, invites her to share the burden and seek Sensei's help. Subaru answers with a collective demand for judgment, refusing reconciliation on those terms (u:0050-0087). Atsuko asks Sensei and Maia to join an Arius-style intervention; both agree, but no resulting repair or coercive action is shown (u:0088-0094). C003 E006 unopened.

## V006 C003 E006 relationship state delta

The retrospective shows Subaru and Saori as argumentative mission partners from first year, with Subaru challenging Saori's speed doctrine and later doing care work for students affected by her training. Saori thanked Subaru, despite sparse emotional expression (scene:001:u:0001-0057). Subaru wakes near Sensei and weeps; he waits, hears her self-reproach, acknowledges her effort and does not promise success (u:0058-0111). Saori, Misaki, Hiyori and Atsuko invite her into a shared future. Maia answers Subaru's muddy-clothes resignation with a limited appeal to avoid further harm, which Subaru accepts; this is a small repair, not a completed reconciliation or school reform (u:0112-0135). Serina/Hanae are relieved as Mine wakes; Serina first prioritizes rest while Mine insists on the exam (u:0136-0149). C003 E007 unopened.

## V006 C003 E007 relationship state delta

Serina asks whether Subaru hates Trinity caregivers; Subaru thanks them for real care while requesting time for Arius students to sort old distrust. Serina accepts the discomfort without insisting on instant affection (scene:001:u:0016-0037). Mine and Subaru discuss past/future Arius, then Mine pushes study; Maia models willingness and Subaru says she may learn from Maia, reversing the old mentor flow (u:0038-0071). Trinity student A/B praise Arius transfer A/B's CQB expertise and invite them to lead a new study club; the latter are startled and one tentatively greets the group, with office consent uncertain (u:0072-0097). Maia asks Subaru about a self-made nest and Subaru agrees to try, not to a guaranteed reform (u:0098-0105). C003 E008 unopened.

## V006 C003 E008 relationship state delta

Sensei praises Nagisa's labor. She offers educational space for Arius and describes a Trinity she wants students to treasure, crediting his prior lesson (scene:001:u:0001-0056). He apologizes for distrusting and speaking harshly to her; she says her remedial-group responsibility remains but his exceptional severity hurt. She asks him to turn, leans against his back, then proposes mutual care and a limited no-reopening pact over tea (u:0057-0101). She welcomes his report on interim representatives and contemplates improving Mika's treatment, but neither action occurs (u:0102-0126). Private teasing and interruption by Mika/Seia end in a present four-person tea. Mika/Seia spar warmly while Nagisa worries about what they heard; Seia's relationship to Sensei includes a joking rebuke (u:0127-0182). No durable political reconciliation proven. C003 E009 unopened.

## V006 C003 E009 relationship state delta

Konoka speaks informally with Saori in custody, tests her regret, announces all-Squad parole and warns that it is not innocence. Saori accepts responsibility but is uneasy about the lenient-seeming result; Konoka rejects her severe halo pledge (scene:001:u:0001-0086). Hina's own petition followed Sensei personally asking her, despite anger over his injury; her passage is not proof she appeared in the interview (u:0061-0071). Hifumi and peers welcome Arius students for study. Azusa and Maia are pleased to meet again, but Azusa refuses to impersonate her at the exam. Hanako helps after Koharu's bluff fails and teases her; Atsuko/Hanako mutually choose friendly ちゃん address while explicitly not being old acquaintances (u:0087-0161). Sensei resumes teaching and handles student avoidance humor; no grade outcome (u:0162-0209). C003 E010 unopened.

## V006 C003 E010 relationship state delta

Subaru tells Sensei she still resists exams but will trust Arius students' voices and him; Sensei thanks her and Maia, acknowledging that teacher confidence also depends on student trust. He sees students off, awaits them, then hosts a celebratory outing before results (scene:001:u:0019-0086). Maia struggles to address Atsuko without 姫様, and Atsuko welcomes the less-ranked name. At tea Atsuko asks Subaru/Nicomedia to take public-order duty; Subaru queries the freedom to decline, criticizes the phrasing, accepts, and ultimately pledges maximum cooperation despite risk (u:0087-0205). Atsuko attributes Mine's endurance to conviction but evades Subaru's criticism of harmful rescue (u:0206-0241). Hiyori/Maia bond over near-fail marks, while Saori calls Sensei a benefactor after full-mark self-report (u:0254-0293). Chapter checkpoint next.

## V100 C001 E001 relationship state delta

An unidentified voice addresses Sensei directly and commands him to forget earlier stories, but Sensei does not answer and no relationship history or physical encounter is shown (scene:001:u:0001-0019). The speech cannot be attributed to an existing adversary or allied group on this evidence. Prior relation states from V006 C003 checkpoint remain the current supported ones. V100 C001 E002 unopened.

## V100 C001 E002 relationship state delta

Kuzunoha addresses Seia as a fellow prophet, offers a painful bargain and says not to seek her after returning; Seia accepts while feeling she has no other choice. Their actual ongoing relationship is not shown (scene:001:u:0036-0049). Gematria members dispute Beatrice's rite and Sensei's place in their plans; she turns blame on Sensei, then confesses signaling Color, straining the meeting without a resolved response (scene:002:u:0035-0067). Sensei fears Arona was hurt and checks her; she reassures him and pledges protection. Seia shares a fatal vision without knowing timing (scene:003:u:0002-0032). Rin challenges the evidentiary weakness but agrees to investigate partly out of trust in the president's appointment of Sensei; she retains an address boundary around リンちゃん (scene:004:u:0002-0021). E003 unopened.

## V100 C001 E003 relationship state delta

The Abydos committee debate trespass versus asking Sensei. Ayane fears burdening him, while Serika/Nonomi insist he can choose; Ayane plans contact. Shiroko reports he recently initiated a safety check (scene:002:u:0002-0033). The Game Development Club debates genre, welcomes Alice's reported normal check and worries about Key; Alice's exaggerated threat is in a play register. The hidden Key/Kei passage addresses her as Alice and chooses to watch, but she does not know of it on page (scene:003:u:0002-0050). Himari scolds absent Rio through her data, Eimi probes the warning, and Toki reports Rio's release to freedom plus C&C seniors' kindness while feeling unsure. Himari accepts Toki's volunteered help and intends Schale contact (scene:004:u:0002-0053). E004 unopened.

## V100 C001 E004 relationship state delta

Sakurako speaks to an absent Justina predecessor with uncertain regret/responsibility questions, then asserts Sisterhood succession; no direct relation to a current Arius leader appears (scene:001:u:0002-0021). Mika accepts the hearing outcome without objection, but the gate crowd protests and dehumanizes her; Azusa says Mika's reported rescue of Atsuko/Squad removes her personal reason to hate and rejects many-on-one aggression (scene:002:u:0002-0017; scene:005:u:0002-0035). Hifumi/Azusa share intense Peroro interest, with Hanako/Koharu pulled into a harmless viewing trip that yields a wrong item (scene:003:u:0002-0043; scene:004:u:0002-0022). Sweets-club peers rally after Airi is pushed, with Natsu/Kazusa/Yoshimi confronting protesters as Ichika/Justice move to stop fighting; their final custody/injuries unknown (scene:005:u:0046-0127). E005 unopened.

## V100 C001 E005 relationship delta

Miyako offers continuing civic help to the shop proprietor, who reciprocates with fresh food; this is one local service/gift encounter, not an established dependency (scene:001:u:0007-0030). Squad members share the meal and prospective cider; Moe/Saki deny needing Sensei, while Miyu asks for occasional contact, leaving their collective stance mixed (scene:002:u:0002-0029). Kaya's caller is unheard and cannot be assigned a relationship (scene:003:u:0002-0007). Beatrice breaks with Maestro, Golconda and Black Suit over Color and absolute power; Black Suit withdraws Gematria membership and Golconda attacks at his request, but the group's future and her location/fate are not shown (scene:004:u:0002-0035).

## V100 C001 E006 relationship delta

Rin's dream presents the missing president as someone who called her リンちゃん despite her formal protest; it is remembered/dreamed relation, not present contact (scene:001:u:0001-0018). Ayumu attends Rin's fatigue and fears institutional backlash; Momoka reports the data and dreads workload while remaining present (scene:002:u:0002-0044). Aoi disputes Rin's mandate sharply but acknowledges her ability and asks her to sleep, so opposition does not erase concern (u:0045-0079). Kaya offers solidarity and a Schale/Sensei route while an unseen private addressee remains unknown; Rin accepts her contact/escort offer, no Sensei interaction yet (u:0086-0106).

## V100 C001 E007 relationship delta

Nagisa distrusts Rin's council but Seia wants to talk with Sensei; Mika promises restraint partly because Sensei is expected. Iroha questions Makoto's opaque plan; the unnamed Genryumon master answers a subordinate and chooses observation (scene:001:u:0001-0049). Arona conveys Rin's brief, accepts Sensei's thanks and continues research; two Kaiser PMC soldiers exploit his apparent council/Valkyrie trust and seize him (u:0050-0080; choice:001-004). Kaya and Kaiser General are direct conspirators for the abduction, then split: she wants Schale dissolved and he says Kaiser does not. The Kaiser President directs the General's corporate takeover; the General orders Kaya hidden and Sensei confined/shot, but transfer/injury remain pending (u:0081-0111).

## V100 C001 E008 relationship delta

Hoshino and Nonomi disclose to Ayane/Serika that Shiroko lacks earlier memory, while Nonomi had hesitated to tell the story; no Shiroko consent or response to disclosure is shown (scene:001:u:0012-0023). The team repeatedly warns Shiroko against a solo desert detour, and she promises distance/safety but continues. Hoshino, Nonomi, Serika and Ayane escalate from worry to calls; Shiroko briefly reconnects silently, leaving their knowledge limited (u:0024-0040; u:0065-0085). Arona tells Sensei she protects him and urges escape, then senses an approach; Sensei calls for her after apparent Chest power trouble, with communication state unverified (u:0041-0064). PMC captors continue coercion, but no shot wounds him in the printed scene.

## V100 C001 E009 relationship delta

Kanna reaches and frees Sensei, whose choices recognize her and notice her wound; she minimizes pain but relies on Kirino/Fubuki to escape immediate guards (scene:001:u:0015-0064; choice:001-007). She refuses to command their rule-breaking as though risks were equal, apologizes and accepts Fubuki's doughnut joke, while Kirino avows justice (u:0065-0083). Rin urgently orders Momoka to search for Sensei but continues the committee; Kaya is also missing to them (u:0084-0099). Sakurako and Seia each want Sensei for undisclosed concerns, while Makoto mistrusts the council and walks out. Aoi challenges Rin with suspicion and a formal vote; no proof of Rin's collusion is shown (u:0100-0155).

## V100 C001 E010 relationship delta

Aoi and Rin remain at odds yet agree to speak the next day; Aoi dismisses Momoka/Ayumu and Rin apologizes to them, leaving her alone when Kaiser enters. No evidence Aoi collaborated with Kaiser is printed (scene:001:u:0001-0032). Kaiser President directs General and asserts control over Rin/council, but Rin's later personal custody is unshown (u:0033-0043). Kanna returns Sensei's devices, credits his teaching and praises Kirino/Fubuki's justice; he inwardly affirms Kanna's present principles despite her shame (u:0064-0077). Arona reconnects in distress and Sensei offers reassurance/care before proposing renewed command; no broader device-control relation is proven (u:0078-0087).

## V100 C001 E011 relationship delta

Fubuki recognizes Sensei's command but argues the group needs reinforcement; Kirino considers the wounded member and initiates combat when discovered (scene:001:u:0001-0006). After survival, Fubuki again voices material concern. Kanna returns to movement and orders everyone out, continuing with Sensei, Kirino and Fubuki rather than leaving them here (scene:002:u:0001-0005). No new long-term bond or command hierarchy is established.

## V100 C001 E012 relationship delta

Sensei thanks Arona for a costly brief connection. Rabbit Squad responds to his request despite Saki/Moe's prideful disclaimers; Miyu observes their rush and Miyako states the rescue directly, strengthening the squad–Sensei support relation without a formal dependency claim (scene:001:u:0001-0014; u:0029-0033; choice:001-002). Miyako greets Kanna with thanks for prior help, and Kanna is surprised the park squad can operate. Miyako asks Life Safety members to follow her tactical direction and Kirino/Fubuki agree, a local alliance for escort rather than institutional merger (u:0041-0057).

## V100 C001 E013 relationship delta

Miyako credits Kanna for saving Sensei and the squad shelters wounded Kanna; Moe's confidence in spontaneous recovery is reassurance, not a health report (scene:001:u:0001-0008). Public Security A/B/C choose to help Kanna/Sensei despite no command, and B says aiding Kanna suffices; no legal protection is shown (u:0071-0079; scene:002:u:0014-0017). Sensei asks Miyako to command while he supports, and she accepts. Sora recognizes/helpfully offers food to the rescuers, with a tag seam around recognition (scene:001:u:0080-0083; scene:002:u:0003-0009). Momoka/Ayumu supply Rin's room lead and ask Sensei to rescue her; he agrees, without reunion yet (scene:002:u:0024-0034).

## V100 C001 E014 relationship delta

Black Suit, Maestro and Golconde continue cooperative inquiry after Beatrice's removal, yet their reported projects and forecasts remain self-interested. Black Suit declines concern for Kaiser's OOPArt and doubts the corporate President's control (scene:001:u:0001-0020). Sensei reaches Rin; she tolerates his old nickname because only he now uses it, Ayumu is relieved, and Rin blames herself. This is direct reunion without proven health or authority recovery (scene:002:u:0006-0014). Miyako/Saki confront General; Miyako relies on Rabbit4 and Miyu fires before a printed result. The General's final status and group safety remain unknown (u:0015-0025).

## V100 C001 E015 relationship delta

A flood of unsent-to-Sensei-now-delivered messages shows Seia, Sakurako, Trinity, Millennium, Rin and Abydos trying to reach him during disappearance; their accounts reflect concern and separate information needs, without a shared meeting (scene:001:u:0009-0022). FOX seniors coordinate to secure Kaya and an unidentified item; Yukino expects to ask Kaya after she wakes, not that they have her full trust or knowledge (u:0029-0040). Francis says he and Decalcomanie will watch Sensei and assaults his role in words; Sensei inwardly refuses. Arona accepts Sensei's request to contact all known students and reports doing so, while responses remain unshown (u:0041-0080).

## V100 C002 E001 relationship delta

Yuuka and Noa divide immediate work while Rio remains missing by their report; Hanako asks differing Trinity factions to cooperate, and PS68 receives Sensei's contact (scene:001:u:0001-0020). On Schale's roof Black Suit gives Sensei his account of Color, Anubis and Plenapates, and Sensei says they will stop the towers. This is adversarial information exchange, not acceptance of every claim. Black Suit warns Sensei not to overuse the adult card after it is drawn; no card expenditure or aid from him appears (scene:002:u:0002-0042).

## V100 C002 E002 relationship delta

The flashback shows Hoshino/Nonomi's first Shiroko care, including the scarf; the present shows Hoshino's search urgency and Nonomi persuading her toward joined action, not diminished concern (scene:002:u:0002-0047). Kayoko comes on Sensei's request; Hanako supports Ayane's hope of finding Shiroko, with a self-introduction tag seam (u:0048-0100). Tea Party members promise local protection together, and Sena's joking request for Chinatsu to return to Emergency Medicine is directly retracted as a joke amid a serious aid commitment (scene:007:u:0012-0030). District actors pledge cooperation under Rin's coordination and Sensei oversight, while actual execution and trust durability are open (u:0031-0062). Kaho/Niya share tentative lore with Seia, who seeks Kuzunoha for students affected by Color; no meeting with her results (u:0063-0117).

## V100 C002 E003 relationship delta

PS68 volunteers the risky Abydos decoy with the Abydos team; Kayoko's correction of Haruka keeps group survival explicit, while Nonomi consents to use of the old train without giving the full family/company story (scene:001:u:0001-0033). Nel and Tsurugi's role rivalry draws C&C/Justice allies into an unnecessary fight; Yuuka makes them decide by a quick game for timetable reasons, with no later bond or final role shown (u:0034-0101). Rabbit and Game Development meet at Slumpia, Hina praises Miyu's ability amid tag errors and Alice tells Hina Sensei calls her reliable. Yuzu is encouraged by Midori/Momoi and acknowledged as lead by Miyako (u:0102-0160). These are first-team trust overtures, not battle-tested cohesion.

## V100 C002 E004 relationship delta

Saori reunites with Arius Squad, receives teasing/concern and joins their intention to answer Sensei, while prior estrangement is not fully resolved by one meeting (scene:001:u:0001-0029). Yuuka/Noa recall Koyuki and press her disputed responsibility; Noa's intimidating precision is Koyuki's situated report, not a complete relationship model (scene:002:u:0002-0045). Juri/Fuuka serve evacuees, and Gourmet's practical food help elicits Fuuka's explicit thanks despite her rejection of Haruna's easy friendship framing (scene:003:u:0002-0035). Hifumi/Azusa plan a Peroro film after patrol, with prior combat boast unaudited; Niya/Kaho entrust ninjas with a discreet search and Sensei asks for contact if found, not proof the chair trusts them (u:0039-0128).

## V100 C002 E005 relationship delta

Rin, Ayumu and Momoka jointly brief Sensei on command and risk; Sensei thanks them, while Rin insists the hard work remains (scene:001:u:0001-0015; choice:001). The assembled group answers Sensei's inward readiness call, a coordination scene rather than proof all individual bonds or later compliance are stable (u:0016-0020). Local defenders and attackers remain assigned distinct responsibilities from E002-E004.

## V100 C002 E006 relationship delta

Ayane coordinates Abydos and PS68 by rendezvous/railway roles; Kayoko receives Aru's go-ahead to start the train while Mutsuki/Aru answer the apparent interruption (scene:001:u:0001-0016). This shows command cooperation at launch, not completed rescue or proof of durable trust under the coming fight. No Sensei interaction in this short unit.

## V100 C002 E007 relationship delta

Shun directs Kokona to guide civilians and Kokona accepts. Rumi greets Kisaki with surprise; Kisaki offers an executive-chief dispatch to thin defenses, and Genryumon students obey her order (scene:001:u:0001-0015). These are crisis coordination contacts, without the executive's arrival or proof of district-level mutual trust. The two student labels cannot be identified with the earlier V100 C001 E007 subordinate.

## V100 C002 E008 relationship delta

Tomoe expresses concern for absent Cherino and Shigure asks Nodoka about her; Nodoka thinks she has not reached the shelter, so none has direct current contact with her here (scene:001:u:0005-0007/0014-0018). Nodoka provides a shelter route, while Momiji/Meru share book plans under tag seams (u:0007-0013). The charge participants share slogans, not individualized ties or a combat result.

## V100 C002 E009 relationship delta

Eimi checks front and parachute teams; Tsurugi's side responds ready, while Akane/Karin/Nel report C&C progress and willingness to begin (scene:001:u:0001-0011). This is operational cooperation after E003 rivalry, not proof of lasting interpersonal repair. The Tsurugi self-address line may represent Ichika but cannot secure a personal support-pattern claim.

## V100 C002 E010 relationship delta

Kaho leads mixed Hyakki participants into defense; Tsubaki/Chise/Fina/Chimimouryou answer. Shizuko and Umika coordinate festival-committee shelter support (scene:001:u:0001-0009). Shared mobilization does not prove lasting faction reconciliation or actual rescue results.

## V100 C002 E011 relationship delta

Ako presses Prefects to act without Hina; Iori asks her location and Chinatsu inwardly offers a more charitable interpretation of their reputation (scene:001:u:0001-0010). Ako/Satsuki spar over Pandemonium, but Sena directly credits Satsuki's evacuee guidance. Satsuki denies joining the battle, offers a failed hypnosis encouragement, and Ako launches defense (u:0011-0043). The scene shows bounded cross-faction aid, not resolved rivalry.

## V100 C002 E012 relationship delta

Midori cautions Alice, Saki questions the forward pair and Miyako voices confidence; this is team concern rather than proof they are safe (scene:001:u:0001-0005). Kotori's technical praise and Alice's `UZQueen` framing support Yuzu before a mission she finds pressuring. Utaha pulls Kotori back to analysis while Yuzu launches (u:0006-0021). No outcome-level trust test appears.

## V100 C002 E013 relationship delta

Justice and old-library staff coordinate evacuation despite Ui's discomfort; Suzumi/Reisa and After School Sweets offer help when attackers appear (scene:001:u:0001-0030). Nagisa/Seia support Hasumi rather than override her, and Seia cautions Mika after a radio assurance (u:0031-0050). These are immediate protective contacts, not proof of eventual safety or repaired prior faction tensions.

## V100 C002 E014 relationship delta

Mika hears Koharu is trapped and intervenes; Koharu directly says Mika saved/helped her, and Hasumi thanks her for that act while student bystanders still accuse her (scene:001:u:0019-0031; scene:002:u:0001-0020). Koharu's `dear friend` designation comes from Mika in a label-shift zone but is contextually clear. Justice takes Koharu onward; the event supports local gratitude, not comprehensive trust restoration or exoneration.

## V100 C002 E015 relationship delta

Saori anticipates Hanako's distrust, but Hanako accepts Arius Squad for rear defense because they answered Sensei and share an unnamed important friend; Saori understands while Misaki/Hiyori react with surprise/anxiety (scene:001:u:0007-0024). This is a bounded cooperative assignment, not blanket amnesty. Mine/Marie offer Hanako support; Sakurako's attire draws Hinata/Marie/Hanako reactions under major label drift, leaving any long-term relationship shift open (u:0001-0006/0025-0059).

## V100 C002 E016 relationship delta

Utaha, Sumire and Engineering/Veritas staff join Millennium defense while Hibiki notes overload. Himari denies operating the unexpected AMAS but accepts its apparent help, without identified source or established trust in it (scene:001:u:0001-0014). No individualized AMAS bond follows from a machine label.

## V100 C002 E017 relationship delta

Yuuka/Noa praise Koyuki's solved cipher yet insist she join the Hod/barrier task over her protest, a situational coercion/need tension rather than proven renewed trust (scene:001:u:0001-0018). Chihiro challenges Kasumi's demolition purpose; Kasumi openly centers hot springs while Kotama doubts the site's geology (u:0019-0036). Engineering/Veritas and Hot Spring Club cooperate only with a divergent goal visible.

## V100 C002 E018 relationship delta

Ninjas recommit to Sensei's request while surrounded; Makoto/Iroha/Toramaru intervene because Ibuki asked to protect her admired ninjas, by the participants' accounts (scene:001:u:0001-0061). Ibuki says the earlier pudding grievance is past; the ninjas thank her and she offers remote encouragement, with no injury by their report. Makoto/Iroha depart while the ninja club continues (scene:002:u:0001-0025). This is a bounded rescue/repair, not general institutional alliance.
\n+## V100 C002 E019 relationship delta
\n+Gourmet Research invites Hifumi/Azusa to Shiratori defense; the unusual Kaitenger team assists and exits before their identities are understood (scene:001:u:0010-0033; scene:002:u:0001-0006). Toki follows Himari's new coordinates and thanks her for suit work. Eimi offers help, but Toki says she is used to fighting alone; Eimi and Himari then discuss possible longing for C&C and guilt over Rio orders (u:0007-0032). Their concern is shown; Toki's private motive and renewed C&C standing remain unconfirmed.

## V100 C002 E019 relationship delta

Gourmet Research invites Hifumi/Azusa to Shiratori defense; Kaitenger assists and exits before their identities are understood (scene:001:u:0010-0033; scene:002:u:0001-0006). Toki follows Himari's coordinates and thanks her for suit work. Eimi offers help, but Toki says she is used to fighting alone; Eimi/Himari discuss possible C&C longing and guilt over Rio orders (u:0007-0032). Concern is shown; Toki's private motive and C&C standing remain unconfirmed.

## V100 C002 E020 relationship delta

Valkyrie student B takes front-gate duty and asks others to hold the rear; delinquents and Love's Helmet Gang step in, while Wakamo pledges personal protection to Sensei (scene:001:u:0009-0022). This is situational aid without shown trust repair or battle outcome. Rin directs the imminent countdown and Sensei affirms her request (scene:002:u:0001-0006; choice:001), supporting their procedural cooperation only.

## V100 C002 E021 relationship delta

Rin and Momoka share the sky observation in Sensei's presence; Sensei internally questions both success and a Shiroko sighting (scene:001:u:0001-0005). The Shiroko-tagged figure does not speak or interact. No renewed Sensei/Shiroko relationship state, identification history or motive can be inferred from this silent appearance alone.

## V100 C003 E001 relationship delta

Nagusa first points a gun at the ninjas by mistake, then denies her office, becomes distressed when Michiru challenges the disguise, self-identifies and gives them an old scroll for Sensei while asking secrecy (scene:001:u:0013-0090). The exchange is contact and a bounded entrusted task, not trust restoration or successful Ayame contact. Shiroko-tagged speaker tells Sensei to leave because she does not want to hurt him, even while asserting a death-guiding role; Sensei pursues her despite Rin's warning, and Ayane recognizes her (u:0091-0129). Her identity relation and future conduct remain open.

## V100 C003 E002 relationship delta

Seia and Abydos students discuss Shiroko without a complete mechanism; Seia/Serika reject blame, Ayane is distressed and Nonomi asks about restoration (scene:002:u:0002-0026). Sensei apologizes, Rin reassures him and then blames herself; Hoshino redirects both toward retrieving Shiroko and preventing another victim, with Nonomi/Ayane joining (u:0053-0099). This is situated solidarity and a rescue plan, not proof of cure, full absolution or a tested capture method. Black Suit frees Maestro pending possible recall as Gematria dissolves (scene:001:u:0019-0031).

## V100 C003 E003 relationship delta

Himari asks Chihiro/Veritas to hack Rio's Eridu missile and Engineering assists despite reluctance; after the pass-through, Himari criticizes absent Rio and Yuuka objects to treating her as gone (scene:001:u:0007-0020; scene:002:u:0002-0023). Hanako brings Sisterhood, library and Tea Party interpretation to Millennium, with explicit uncertainty. Black Suit privately probes Sensei's willingness to pay, then supplies an Abydos lead after warning of bodily danger; no Gematria membership or agreed price results (u:0027-0113).

## V100 C003 E004 relationship delta

Black Suit gives Sensei increasingly specific alleged technical history after E003's severe-risk warning, naming the Atrahasis Ark, Kaiser's alleged Abydos excavation and the Utnapishtim ship. He frames Sensei as the Shittim Chest owner uniquely able to operate after Sanctum towers are gone (scene:001:u:0001-0040). This is informational dependence on a former antagonist's testimony, not proven trust, a completed bargain or direct Kaiser/Black Suit current cooperation.

## V100 C003 E005 relationship delta

Rin brings a remembered President statement to Abydos; Hoshino interprets the desert search, while Ayane worries about Kaiser private property and possible PMC return. Hoshino/Nonomi/Serika prioritize Shiroko rescue, with Ayane reluctantly aiding and later asking Sensei to command (scene:001:u:0002-0015; scene:002:u:0002-0048). Himari promises broader team arrival and on-site identifies the machine before Sensei asks to enter (scene:003:u:0001-0015). This is coordinated crisis action, not legal title settlement or a repaired Kaiser relationship.

## V100 C003 E006 relationship delta

Sensei agrees to summon technical/tactical personnel; Chihiro asks Himari to account for fatigue (scene:001:u:0001-0013; choice:001). Yuuka objects to Alice leaving Millennium under unresolved Rio risk, while Noa says she sent Game Development to a ship she judges safer and asks Yuuka to watch them; this is a situational safety disagreement with tag drift (u:0023-0047). Kei addresses Alice as princess, says she rejected Kei, urges her to leave and calls the warning a wish that Alice live (u:0076-0094). The reported past rejection and predicted harm remain untested here.

## V100 C003 E007 relationship delta

A small AMAS corrects Himari's calculation and becomes strongly identified as Rio's remote voice. Himari confronts her over alleged Toki isolation and Alice abduction, rejects her help and says Toki could join her if C&C would not accept her (scene:001:u:0042-0094). Hanako's parable and Seia's objection lead Himari to ask Rio's interface for aid during crisis and defer censure; no explicit Rio acceptance or forgiveness is printed (u:0095-0129). Rin, Sensei and Hanako discuss a reported ancient question and incomplete meaning, not a completed personal repair (u:0130-0164).

## V100 C003 E008 relationship delta

Yuuka recognizes Rio behind AMAS and forbids approach to Alice/Game Development; Himari supervises, threatens drone destruction if suspicious and allows Rio to seek an emergency return plan (scene:001:u:0035-0050). Sensei volunteers overall lead and Rin joins to share danger; Ayumu and other school representatives join for distinct duties, while Momoka yields to Ayumu's emotional appeal after refusing (u:0076-0102). Ayumu asks Rin to rest and she accepts in the group's interest (u:0126-0138). Cooperation does not settle Rio accountability or guarantee readiness.

## V100 C003 E009 relationship delta

Noa promises to guard Millennium while Yuuka travels; Abydos peers refuse to send Ayane alone, and PS68's Aru/Mutsuki show concern for Kayoko behind bravado (scene:001:u:0002-0054). Yuzu proposes the whole Game Development Club join Alice; Alice admits fear/Kei persistence and asserts her own chosen club/hero identity, receiving peer support (scene:002:u:0002-0079). Hanako/Remedial, Hina/Ako, Tea Party, SRT and Arius divide departing/ground roles (u:0080-0152). Aoi apologizes to Rin, who states nonresentment and entrusts a contingency, without formal reinstatement (u:0153-0179).

## V100 C003 E010 relationship delta

Rin leads the roster and Sensei accepts operator responsibility; Yuuka warns Game Development against rash action. Fuuka protests being listed with Gourmet and having her truck aboard, so her assignment is not simple voluntary cooperation (scene:001:u:0001-0073). Arona pleads with Sensei to reconsider unknown bodily burden, and Sensei reassures her while still committing to protect students (u:0074-0109). The remembered president says mutual incomprehension can coexist with valued relation; Rin defers her personal answer until return (u:0110-0130). Crew notices Sensei's pallor/shaking after launch, with no recovery yet (u:0145-0179).

## V100 C003 E011 relationship delta

The italic federal-president voice addresses Sensei as a trusted adult and asks him to preserve `絆` and shared memories. The scene's uncertain status does not establish a present reunion or Sensei's answer (scene:001:u:0001-0023). Aboard the ship, Yuuka, Hanako, Rio and Himari share a suddenly inconsistent ark reading; concern and technical theorizing are direct, but their ability to overcome it is untested (u:0024-0039). Rio-tagged self-address at u0030 cannot establish who called to her.

## V100 C003 E012 relationship delta

Yuzu/Momoi/Midori fear a repeat of Alice's danger; Sensei asks them to hear Alice fully and inwardly trusts her choice (scene:001:u:0024-0038; choice:001; u:0100). Alice acknowledges fear and avoidance toward Kei, apologizes, asks for help and extends the right to self-definition to Kei. Kei first refuses on risk grounds, then participates in the activation; this supports new cooperation, not a fully observed durable reconciliation (u:0044-0089/u:0104-0106/u:0141-0147). Alice asks Rio to show her face, calls her `リオ先輩`/`仲間` and thanks her present aid; Rio's words toward her earlier harm break off. `許す必要はありません` makes the invitation distinct from formal forgiveness or institutional accountability (u:0108-0134).

## V100 C003 E013 relationship delta

Rio urges Alice as hero to save their world; Alice replies she will answer comrades' expectations, and the club then worries over her unconsciousness and moves her toward care (scene:001:u:0021-0046, source-ordered u:0116). After barrier penetration, Himari credits Rio's idea and Sensei may echo that, a bounded shift in Rio/Himari relations without settled accountability or completed rescue (u:0075-0091; choice:003). Kei refuses Alice's erasure and speaks of disappearing instead; Alice murmurs Kei and tears are observed, but the aftermath of their relationship and Kei's existence remain unknown (u:0092-0114).

## V100 C003 E014 relationship delta

Ayane supports Hoshino/Nonomi/Serika on eastern defense, while Yuuka reluctantly supports Game Development and warns them not to overextend with Alice asleep (scene:001:u:0016-0021/u:0034-0041). Gourmet offers help and an addressed Ako-support voice joins, but Fuuka again protests her involvement, so group deployment does not prove her consent (u:0022-0033). A crew voice entrusts Sensei with overall ship defense; he inwardly accepts the three-group coalition, not a guaranteed victory (u:0042-0043).

## V100 C003 E015 relationship delta

Abydos peers react to a Shiroko-labelled appearance, and Hoshino checks Sensei after a grenade alarm/blast; the figure disappears before any sustained conversation or rescue (scene:001:u:0004-0026; choice:001). Engineering asks shipboard help to attempt restart so everyone can return (u:0027-0040). Himari explicitly criticizes Rio's distrust, Rio acknowledges it while prioritizing passenger lives, and Himari thanks her contingency work despite saying she dislikes her. Rio accepts a cooperative investigation, not an absolution or settled apology (u:0051-0076).

## V100 C003 E016 relationship delta

Ground allies across Gehenna, Millennium, SRT, Trinity and Arius react to changed sky and continue duty; Mika reports Seia left after sensing danger, not a directly witnessed vision here (scene:001:u:0053-0084). Abydos fears the obstructing Shiroko bought time, then another Shiroko-labelled voice and Sensei report joint travel to Area 4. The two appearances' identity relation is unresolved (u:0091-0110; choice:001). This Shiroko calls Prenapates her abductor and aims at him; Sensei asks her to back away when her shots miss (u:0111-0131). The control-room A.R.O.N.A. voice addresses/authenticates Sensei, but its relation to the prior Arona remains unproved (u:0132-0138).

## V100 C004 E001 relationship delta

The control-room OS and familiar Arona directly recognize/interact as two voices of an A.R.O.N.A. type; exact shared-Chest architecture remains their explanation (scene:001:u:0031-0052). Familiar Arona reports a biometric match between Prenapates and Sensei and says the other is no longer alive, sharpening Sensei's confrontation with a counterpart (u:0053-0066). Alternate Shiroko says she killed her Sensei, was brought here by him and kidnapped local Shiroko; local Shiroko vehemently denies she would kill Sensei or end the world (u:0067-0104). Separate time-axis Shiroko histories must not be merged into one behavioral model. Prenapates asks Sensei what he will do without a reply (u:0105-0107).

## V100 C004 E002 relationship delta

Aru urges PS68 to continue for Sensei/Kayoko, and Hina/Rabbit coordinate ground defense (scene:001:u:0001-0022). Rio saves time at 9 seconds, says she cannot overcome the system alone and asks for help; Himari thanks her while explicitly retaining dislike (u:0023-0049). Engineering/Veritas exchange design and navigation help for a shared terminal plan (u:0050-0084). Haruna presses Fuuka's driving skill under an earlier false space-food pretext; Fuuka protests then drives, a current constrained decision rather than retrospective assent to boarding (u:0085-0099/u:0118-0127). Himari checks Alice's condition and asks care; Alice reports she is fine and Sword intact, not medically cleared (u:0105-0117).

## V100 C004 E003 relationship delta

Sensei answers Prenapates with a plan to combine everyone's strength; local Shiroko affirms continuation and later asks him at the confrontation, receiving his resolve to fight together (scene:001:u:0001-0009/u:0065-0066; choice:001-002). Toki calls Himari/Sensei/allies before taking Abi-Eshuh into a solo hold. Himari and Rio reconnect and ask retreat/support; Toki refuses under distance/time pressure, with no result or death shown (u:0025-0052). Fuuka/Gourmet share a dangerous pursued descent with no arrival yet (u:0053-0064).

## V100 C004 E004 relationship delta

Rio voices urgency for Toki as Toki pants in the unseen ground clash; no reunion or injury confirmation follows (scene:001:u:0001-0010). Fuuka delivers Gourmet to the lower system; Ayane cues Abydos east, Yuuka cues Game Development west, and Haruna/Akari/Junko complete lower demolition with Veritas/ship reporting the cut (u:0011-0047). Alice acts with her club after regained wakefulness, but no Kei or clinical state is examined. The coordination is achieved, not a settled long-term alliance or blanket consent for Fuuka.

## V100 C004 E005 relationship delta

Rio urges Toki to withdraw, Toki confesses she wanted to fight with Schale/C&C and asks for a sacrifice code; Rio refuses and admits she failed to seek others' hands (scene:001:u:0006-0035). Asuna, Akane, Karin and Neru arrive and Neru rebukes Toki's farewell, offering direct senior support rather than a completed extraction (u:0036-0045). Noa says she dispatched early after Seia's request and her own hunch; Seia thanks that trust and tells Rio an easy answer may exist. The mechanism of her foresight remains unverified (u:0046-0062). Yuuka calls Rio back to present duties amid label drift (u:0067-0072).

## V100 C004 E006 relationship delta

Gourmet decides to help Sensei and Izumi offers to carry silent Fuuka; Abydos/Ayane decline to leave before retrieving Sensei/local Shiroko, while Game Development/Yuuka condition escape on his return (scene:001:u:0013-0048). C&C reports Toki escorted and plans to wait for Sensei with wider vigilance (u:0049-0057). Sensei trusts allies, local Shiroko says group victory suffices, and familiar Arona promises protection against alternate Shiroko/control-room OS support. The hostile side targets Sensei as the coalition's pivot (u:0058-0097). These are active ties under danger, not completed reunion or evacuation.

## V100 C004 E007 relationship delta

An OS voice says her teacher gave his own escape sequence to Shiroko and fears for his fall, then hears a Sensei inward request to help another child in his place and a farewell; the counterpart referent remains context-sensitive (scene:001:u:0001-0006; scene:002:u:0017-0034). Familiar Arona apparently transfers the control-room OS's data despite enemy alignment; that OS asks why and interprets the act as Sensei seeing her as a student to help (u:0035-0044). Familiar Arona grieves inability to save her Sensei; control-room A.R.O.N.A. offers joint protection and familiar Arona trusts her because Sensei did (u:0045-0068). No completed rescue or relationship future yet.

## V100 C004 E008 relationship delta

OS voices report Sensei safely returned to students, but no physical reunion or health examination is shown (scene:001:u:0011-0019). Local Shiroko gives alternate Shiroko an unnamed precious Task Force keepsake, offers a possible shared future outing and says Sensei can handle coexistence trouble; alternate voices gratitude and farewell, without permanent location fixed (u:0020-0060). Familiar Arona stops the control-room OS from leaving alone, names her Plana, offers home and hand-holding, and Plana accepts while choosing `アロナ先輩` over sister address (u:0061-0094).


## V100 C004 E009 relationship state delta

Shinon/Mai remain a Chronos reporting pair; interruptions constrain what their program airs but do not identify an editor or source (scene:001:u:0001-0032). Kaya and Kaiser General recommit to a transactional pact after damage to both sides, with no proven trust or contract scope (u:0033-0048). Alice and Game Development friends treat Key as a possible companion; Alice says she has not met Key since disappearance, and they share hope on seeing `Kei.sav` without confirming contact (u:0049-0079). Toki is alive and briefly meets the club/Eimi, but says Rio remains missing and C&C contact is uncertain (u:0080-0098). Himari protects Alice's hope while refusing false certainty, then modifies the model to hold memory/data (u:0099-0141). No new readiness promotion; 368/480, E010 unopened.


## V100 C004 E010 relationship state delta

Hifumi/Koharu/Hanako/Azusa remain together at a test, with outcome open (scene:001:u:0001-0008). Atsuko/Misaki/Hiyori support Saori's independent travel and request continued contact; she leaves on a job call, with material security unresolved (u:0009-0031). Abydos peers and the master welcome local Shiroko to an ordinary group meal (u:0032-0065). Arona/Plana now share an enacted homecoming and senior address (u:0066-0077). Ayumu and Momoka support Rin before the vote; Rin thanks them, subject to tag inversions (u:0078-0095). Niya mediates a letter for Sensei; the alleged Kuzunoha author is not independently met. Rin's possible president correspondence remains her inference from the unsigned paper (u:0096-0131). No new readiness promotion; 369/480, E011 unopened.


## V100 C004 E011 relationship state delta

Plana and Arona now share a routine, affectionate senior address and reciprocal care, while Sensei greets both and receives both support pledges (scene:001:u:0001-0023; choice:001-005). Plana privately worries her presence burdens Arona through the Chest, a guilt/care inference rather than measured harm (u:0024-0027). She recognizes the federal president's absence in this world, with no direct contact with Rin or president in this unit (u:0028-0029). No readiness promotion; 370/480, E012 unopened.


## V100 C004 E012 relationship state delta

Francis speaks in rivalry with Sensei and Black Suit, announces a visit to an unnamed expelled Gematria old friend, and receives Decalcomania's interjections; actual contact with the friend is unseen (scene:001:u:0001-0012). Plana thinks through her relation to familiar Arona as similar yet distinct and addresses the federal president without a printed reply (u:0013-0020). No relationship with the president is independently staged. No readiness promotion; 371/480, chapter checkpoint pending.


## V100 C004 canonical checkpoint reconciliation

The [V100 C004 checkpoint](../02%20Sequential%20Readings/MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C004_CHECKPOINT.md) reconciles E001-E012 at **371 / 480** canonical main units. The coalition's east/west/lower-device intervention severs the ship/Ark link at one second; the OS reports temporary ground-Sanctum cancellation, while E008 OS voices report present Sensei safely returned after E007's dangerous fall. Plana is the existing control-room OS subject, distinct from familiar Arona; local and alternate Shiroko remain distinct. The exact duel, Ark/ship damage, Prenapates' fate, Sensei medical status, the alternate's durable status and wider casualty audit are unverified. E009-E012 supply civic repair reports, ambiguous `Kei.sav`, homecoming, pending Rin vote, unauthenticated Kuzunoha/president letters, Francis's unperformed Gematria plan and Plana's privately asserted president hypothesis. No new readiness promotion or standalone model: **21 PARTIAL_MODEL / 182 UNMODELED across 203**. No durable new claim ID, frozen analytical prediction, held-out diagnostic (`NO_DIAGNOSTIC_OPPORTUNITY`) or side-source admission. The 43 inserted V001 C003 units remain **DEFER** for their own ordered backfill. Next forward source: `BA:main:series2:000:001:001` / `MAIN_S2_V000_C001_E001`.


## S2 V000 C001 E001 relationship state delta

Decalcomania speaks in first-person plural “we” about an unnamed fallen circle and addresses a telescreen whose speech is absent; no actual interlocutor identity, agreement, recruitment or alliance is verified (scene:001:u:0004-0029). His later enthusiastic assent to repeated narrator questions is self-directed as printed, not a demonstrated coalition or contact with Francis (u:0030-0082). No readiness promotion; 372/480, E002 unopened.


## S2 V000 C001 E002 relationship state delta

Momoka praises Rin's filmed work; Aoi/colleagues call her the recognizable council face despite her camera reluctance (scene:002:u:0002-0019). Ayumu delivered an unsigned envelope from the mailbox and worries whether it contained harm, but does not know its source (u:0020-0026). Rin shares its photos and her cautious president-handwriting inference with Aoi/Momoka/Ayumu; they recognize old shared moments but not the lake, so no direct president contact is established (u:0027-0052). No readiness promotion; 373/480, E003 unopened.


## S2 V000 C001 E003 relationship state delta

Within the dream, an unidentified girl apparently regards Sensei while an unidentified narrator speaks for the scene; no reliable identity or waking contact is established (scene:001:u:0041-0050). Awake Arona and Plana worry about Sensei's distress and sleep, propose a checkup, meal reminders and returning to bed; Sensei thanks them and asks about the strange device (u:0051-0068; choice:002-005). Their care is directly staged, unlike the dream's absent student world. No readiness promotion; 374/480, E004 unopened.


## S2 V000 C001 E004 relationship state delta

Rei worries for labelled members and checks decompression, A reassures her, B explains the current and C voices a fear; this is a local team relationship only (scene:001:u:0001-0019). They jointly examine a recovered shard, A warns against prolonged viewing, and Rei sets a temporary stop while maintaining an unspecified superior's mission (u:0020-0036). No school, sponsor, family or outside contact is identified. Add four narrow UNMODELED subjects; 375/480, S2 V001 C001 E001 unopened.


## S2 V000 C001 canonical checkpoint reconciliation

The [S2 V000 C001 checkpoint](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_000/BLUE_ARCHIVE_MAIN_S2_V000_C001_CHECKPOINT.md) reconciles all four sequential readings at **375 / 480**. Decalcomania claims a new route to authority through an unheard telescreen without demonstrated power; Rin's unsigned “letter” proves to be a photo envelope with no message, including an unlocated monochrome lake; Sensei's monochrome city and unidentified girl are in a narrator-driven dream, followed by waking Arona/Plana care; Rei's dive team retrieves a shard she names a shining trapezohedron without composition, hazard or sponsor verification. No causal bridge between screen, photograph, dream and shard is printed. Four directly speaking dive-team subjects were added as narrow UNMODELED: **21 PARTIAL_MODEL / 186 UNMODELED across 207**. No durable new claim ID, standalone model, frozen analytical prediction, held-out diagnostic (`NO_DIAGNOSTIC_OPPORTUNITY`) or side-source admission. The 43 inserted V001 C003 episodes remain **DEFER** for ordered backfill. Next forward source: `BA:main:series2:001:001:001` / `MAIN_S2_V001_C001_E001`.


## S2 V001 C001 E001 relationship state delta

Aoi treats Rin as both senior/colleague and someone whose health matters, enlisting Sensei privately after other officials fail (scene:001:u:0001-0023). Rin resists help, but Aoi shifts a deadline and Ayumu/Momoka take named work, allowing Rin to agree to rest (scene:002:u:0008-0037). Sensei uses teasing `リンちゃん`/date language; Rin denies the label yet agrees to a Saturday meeting to observe Sensei's own habits (u:0038-0054). Appointment is future; romance and durable behavior change unproved. No readiness promotion; 376/480, E002 unopened.


## S2 V001 C001 E002 relationship state delta

Aoi's reported uniform removal pushes Rin toward an actual Saturday outing; Sensei supplies food, film and arcade diversion while Rin repeatedly denies the date label (scene:001:u:0002-0022). The Lamini vendor knows Sensei as a repeat visitor and recognizes Rin from public media, then raises local water trouble; Rin answers as acting official despite being off duty (scene:002:u:0007-0048). Rin remembers street-food and Othello time with the missing president, but these are recalled not present interactions. After her game win, Rin asks Sensei to accompany her to an unnamed person from her past (scene:003:u:0034-0069). Add vendor UNMODELED; 377/480, E003 unopened.


## S2 V001 C001 E003 relationship state delta

Rin visits imprisoned Kaya on her day off, offers a written alternative, praises persistence, loses one chess game and asks for another; Kaya accepts and later is called an old difficult friend (scene:001:u:0002-0045/u:0088-0101). Kaya says she is isolated from FOX and has few visitors, but this is her account. Their shared president-comparison and Rin's people-not-pieces warning show disagreement as well as surviving rapport (u:0046-0059). Sensei accompanies and asks about the FOX item, but no release, forgiveness or future coup alliance occurs. No readiness promotion; 378/480, E004 unopened.


## S2 V001 C001 E004 relationship state delta

Sensei walks Rin to the council and asks her to protect the rest day; she thanks them and leaves before inspecting the ark alone (scene:001:u:0001-0018). Rin's private plea to the absent president reveals dependence on reassurance, while a recollection depicts first-year Rin deflecting a hypothetical disappearance into work terms (scene:002:u:0016-0039). A later president-claiming voice addresses her, but Rin does not recognize/authenticate it in printed text (u:0040-0057). No demonstrated reunion or repaired attachment. No readiness promotion; 379/480, E005 unopened.


## S2 V001 C001 E005 relationship state delta

Rin asks Aoi to witness the visitor, but Aoi calls her president and worries over Rin's all-night absence; Sumomo/Momoka/Heine/Ayumu align socially with the visitor while differing on remembered appearance (scene:001:u:0012-0043). Rin leans on Sensei, who finds the visitor unfamiliar but urges listening before judgment (u:0061-0072). The claimant speaks as an old friend yet Rin rejects familiarity. No authenticated reunion or proven betrayal by council colleagues. Add claimant separately as UNMODELED; 380/480, E006 unopened.


## S2 V001 C001 E006 relationship state delta

The claimant invites Rin's cooperation even if Rin thinks her false, and Rin recognizes familiar phrasing without accepting identity (scene:002:u:0037-0047). Sensei's recounted history is unprinted; the claimant acknowledges Schale in words after reviewing its documents (scene:001:u:0001; scene:002:u:0015-0024). Nagisa, Makoto and Cherino each make limited verbal concessions to tailored appeals, while Momoka receives a reprimand and future sample offer. Officers praise the claimant; Rin silently fears continued reliance (scene:003:u:0002-0100). No authenticated reunion, Hina assent or demonstrated durable trust; 381/480, E007 unopened.


## S2 V001 C001 E007 relationship state delta

Plana volunteers a warning and asks Sensei to distrust the claimant; Sensei's inner view is gentler, and Arona directly disputes Plana's identity/ability shortcut (scene:001:u:0003-0033). Plana seeks Sensei's permission and fresh biometric contact for pairing; the pinky-promise touch recalls an unspecified memory (u:0034-0063). After the overload Sensei's alternatives prioritize Arona/Plana's safety or thank Plana, and Arona tries to salvage a core but holds a data-empty almond seed (u:0095-0120; choice:012). Rin arrives with purpose unheard. No repaired claimant relationship or proven betrayal; 382/480, E008 unopened.


## S2 V001 C001 E008 relationship state delta

Rin asks Sensei to accompany a discreet inquiry; Sensei offers Schale contacts through alternative choices and later suggests stopping for cold/night, but she asks for another thirty minutes (scene:001:u:0001-0029; scene:002:u:0037-0041). A Valkyrie officer trusts Sensei's explanation after initial rumor suspicion (u:0025-0036). Mai initially pursues a scoop, accepts Sensei's confidentiality request, then provides Rin a secondhand lead after sharply doubting the swap theory (u:0042-0089). None of these contacts corroborates the missing president yet; 383/480, E009 unopened.


## S2 V001 C001 E009 relationship state delta

Orwell greets Sensei as a prior acquaintance; Sensei privately asks whether he is Golconda/Francis and then Decalcomania, but the speaker's answers leave continuity ambiguous (scene:001:u:0012-0017/u:0040-0045). Decalcomania separately interjects four times, while Orwell narrates Francis and Decalcomania's alleged changed interpretations of Sensei. Rin is present on entry but has no printed answer to the monologue. The Mai-sourced witness is not established; no alliance, attack or reconciliation occurs. 384/480, E010 unopened.


## S2 V001 C001 E010 relationship state delta

Rin challenges Orwell about the missing president; his 'damaged' speculation wounds/alarms her, and Sensei threatens a firm protective boundary if he touches their student, after which Orwell apologizes (scene:001:u:0017-0030). Rin remains unconvinced by simulacrum rhetoric and supplies the black-swan answer (u:0031-0050). Arona and Plana negotiate a possible alternating secretary/work arrangement, with Arona initially possessive then accepting (u:0061-0076). Sensei agrees to attempt the evidence plan yet expressly rejects teaming up with Orwell; his account access remains an offer only (u:0077-0087). 385/480, BA:main:series2:002:001:001 unopened.


## S2 V002 C001 E001 relationship state delta

Students A/B resent Iori's intervention, but Ako's dress-code hypothetical makes them reconsider unbounded Prefect power (scene:002:u:0002-0044). Chinatsu echoes Ako/Hina's policy; Hina praises her and Chinatsu thanks her, a direct mentor/team recognition (u:0045-0055). Student B voices transient admiration and an abandoned membership idea (u:0062-0068). Ako and Makoto clash over equipment, budget and activity expenses; Hina says she cannot overlook a genuinely negligent motive, without issuing a sanction yet (u:0069-0081). 386/480, E002 unopened.


## S2 V002 C001 E002 relationship state delta

Makoto first praises the juniors then bristles at their implication Gehenna is not great; Mayumi blames his administration and presses his Schale/Trinity rationale (scene:001:u:0015-0048). Ako welcomes criticism of Makoto until Shoko extends it to Prefects; Iori defends warning before force against Mayumi's charge (u:0049-0067). Hina and Shoko disagree openly about freedom versus license and the Prefects' boundary, with no fight or concession beyond Hina accepting the word 'ambiguous' (u:0068-0085). The committee vows future action but no alliance or institutional response is shown. 387/480, E003 unopened.


## S2 V002 C001 E003 relationship state delta

A rocket-jump student treats Mayumi's damage complaint casually and leaves before Prefects; Karen steadies Mayumi toward volunteer work, and Shoko checks she is all right (scene:001:u:0001-0018). An unnamed Pandemonium third-year offers qualified warning and encouragement, but Mayumi rejects the warning, Shoko backs her and Karen restores morale (u:0025-0063). Shoko positions herself as planner and Mayumi/Karen invite her proposal, which stops at authority/symbol language (u:0064-0078). No senior alliance or demonstrated persuasion of other students. 388/480, E004 unopened.


## S2 V002 C001 E004 relationship state delta

The committee directly invites Sensei and tests informal rapport; Mayumi requests help, Karen praises Sensei's openness and Shoko uses formal presentation with label drift in banter (scene:001:u:0001-0039). Sensei denies a negative council rumor and approves Mayumi's care for Gehenna, without adjudicating every restoration claim (u:0030-0039; choice:004-005). Shoko asks for Sensei to stand beside them publicly; Sensei agrees to help students and the three react warmly before Mayumi rushes onward (u:0069-0093). No performed endorsement speech, audience reaction or lasting alliance terms yet. 389/480, E005 unopened.


## S2 V002 C001 E005 relationship state delta

Mayumi/committee enlist Sensei's presence at a public pitch; nearby students explicitly treat Sensei involvement as a reason to trust the range (scene:001:u:0001-0034/u:0089-0097). Karen doubts the point scheme's manageability and later warns Sensei against reflexive help; Shoko eyes data/control and jokes Sensei's reputation bears failed permitting risk (u:0062-0088/u:0136-0144). Sensei remains with them and agrees to seek retroactive authorization after discovering none exists, without granting the committee a guarantee. Attendees A/B ask for use, give registration details and inspect the site; no durable loyalty shown. 390/480, E006 unopened.


## S2 V002 C001 E006 relationship state delta

Makoto rejects the committee's bid, then credits its ability to win Sensei's backing and permits activity to honor Sensei while claiming a future favor (scene:001:u:0001-0088). Iroha questions Makoto's chaos-design boast and offers to handle remaining administration, not shown complete (u:0027-0028/u:0089-0092). Shoko/Mayumi/Karen celebrate Sensei's decisive appeal, with speech tags partly drifting (u:0098-0108). Hina declines to block the group, trusts Sensei's presence but remains watchful, then asks Sensei for time and shares tea (u:0109-0124). No Makoto-Hina reconciliation or verified workload drop. 391/480, E007 unopened.


## S2 V002 C001 E007 relationship state delta

Karen interrupts two sukeban threatening a lone Gehenna student, calls the target a new friend, checks injury/property and is thanked; the student voices possible committee application but does not join on page (scene:001:u:0001-0060). Sensei witnesses and praises Karen, performs a requested head pat through a choice, and completes MomoTalk registration; narrator confirms a safe escort after repeated threats (u:0061-0090/u:0127). Karen credits Mayumi love of Gehenna and enjoys the committee team, while admitting Shoko supplied the control language (u:0094-0126). No romance or quantified membership gain. 392/480, E008 unopened.


## S2 V002 C001 E008 relationship state delta

Sensei visits as the committee runs a busy line; Mayumi asks them to stand beside the hours announcement, and Karen says that presence helped (scene:001:u:0035-0044/u:0077-0078). Students react with mixed protest/curiosity and one queue dispute is settled by Karen, local not universal support (u:0026-0034/u:0045-0075). Sensei raises concern about Gehenna identity; Mayumi partially concedes plural paths, Shoko favors coordination, and Karen promises no forced change (u:0097-0110). Sensei remains supportive of student choice but refuses an invented pledge in their name (u:0111-0121). 393/480, E009 unopened.


## S2 V002 C001 E009 relationship state delta

Sensei buys for Karen/Shoko/Mayumi and joins their disappointed assessment; the first owner pleads before Haruna/Gourmet Research, and Sensei asks for reconsideration (scene:001:u:0013-0075). The committee's bargaining with Gourmet fails, a blast follows, and Mayumi calls the conduct terrorism; no legal finding or exact physical actor is printed (u:0076-0135). Sensei offers Shoko an equal-second-chance principle, which she considers; no first-shop reconciliation occurs (u:0136-0142). The group eats elsewhere and that second shop agrees to partner, without identified individual owner (u:0143-0153). 394/480, E010 unopened.


## S2 V002 C001 E010 relationship state delta

Shoko deliberately approaches Meg alone and asks Sensei to reassure her; Meg trusts Sensei, takes the selected map and promises to consult Kasumi (scene:001:u:0021-0078). Kasumi hears Meg, recognizes Shoko's intent and agrees for Meg while warning of no repeat, a bounded confirmation of their decision relationship (u:0094-0128). Kasumi and Shoko trade teasing/cryptic threats without a known referent or escalated act (u:0129-0139). Sensei's visible guilt and later concern for Shoko's self-pressure surprise and hurt her; narration ends with silence (u:0082-0088/u:0145-0164). No permanent rupture or policy change. 395/480, E011 unopened.


## S2 V002 C001 E011 relationship state delta

Iroha reads Makoto's status anxiety, Satsuki checks on him, Chiaki photographs/plans coverage and Ibuki's happiness about quiet softens him (scene:001:u:0001-0065). Ako/Iori/Chinatsu share relief and see Hina sleeping; Ako relays Hina's retirement wish without a present Hina decision (u:0066-0089). Karen hands Iori the approved form, then tests Prefect legitimacy and offers combat; Iori declines after recalling Hina's boundary, and Karen leaves (u:0090-0131). No fight, abolition or repaired alliance. 396/480, E012 unopened.


## S2 V002 C001 E012 relationship state delta

Mayumi asks Sensei to cheer/watch the committee's new help desk; Karen calls their presence reassuring (scene:001:u:0030-0044). Interviewee A pushes back on intrusive questions; petitioner B seeks assistance and tells a mediated account, with no relationship outcome yet (u:0045-0052/u:0069-0092). Karen startles Shoko in the classroom, then listens when Shoko/Mayumi reject a damaging door break and apologizes before Sensei (scene:002:u:0017-0061). Sensei gives mild praise in a choice and recalls another story, without revealing it. 397/480, E013 unopened.


## S2 V002 C001 E013 relationship state delta

Shoko knows Erika/Kirara names; they recognize the committee, speak with the group and recall a one-time broadcast (scene:001:u:0001-0058). Mayumi invites them to join, but they remain Kirakira Club members; Erika respectfully differs about the weight of a great-Gehenna banner and diversity of cultural life (u:0064-0084). Shoko plans Pandemonium negotiation while Erika/Kirara encourage her, with no granted room access (u:0093-0100). Shoko puts a payment/refill offer in Sensei's mouth; Sensei's printed choice objects, limiting assent (u:0017-0021/u:0101-0104). 398/480, E014 unopened.


## S2 V002 C001 E014 relationship state delta

Makoto initially resists committee petitioners but responds to Shoko's Pandemonium-support pitch and grants broadcasting; Karen dislikes feeling like his agent while Shoko says it is planned (scene:001:u:0002-0088). Chiaki photographs the alliance; Satsuki warns Shoko about room accidents and former head, and Shoko defers an unfinished question to Satsuki (u:0087-0100). Makoto tells Iroha he expects credit/blame asymmetry, which she dislikes (u:0106-0114). In the room, Sensei checks on Shoko and offers to remain, but she declines and stays alone (scene:002:u:0015-0054). 399/480, E015 unopened.


## S2 V002 C001 E015 relationship state delta

Mayumi meets Sensei at the range, accepts help with heavy cleanup and thanks them after narrator-confirmed work; Sensei admires her affection for Gehenna and hopes her smile endures (scene:001:u:0001-0062). Shoko reports broadcast upgrades to Makoto, who enjoys the claimed no-Pandemonium-budget benefit; she proposes his speech and he embraces it, with Chiaki and Ibuki approving (u:0063-0084). There is no printed Sensei participation in that later negotiation, aired speech or verified maintenance handover. 400/480, E016 unopened.


## S2 V002 C001 E016 relationship state delta

Makoto expects Sensei's admiration at a crowded speech, but Sensei is startled by the transmission and war declaration (scene:001:u:0001-0063). Kasumi calls to Meg amid apparent freezing, with the referent unresolved; Izumi/Junko note someone still, without identified target (u:0029-0044). Hina publicly aligns with Makoto and Ako praises her, while Iori/Chinatsu question the turn and Mayumi/Karen are bewildered (u:0073-0102). These are on-scene positions under an unexplained event, not durable reconciliations, converted identities or executed alliance operations. 401/480, E017 unopened.


## S2 V002 C001 E017 relationship state delta

Iori/Chinatsu ask Sensei to help understand Hina; Hina/Ako do not see the problem, so Sensei takes the distressed pair to rest/inquiry (scene:001:u:0001-0079). Iroha confronts Makoto, Chiaki escorts worried Ibuki outside, and Iroha privately trusts Sensei to investigate; Sensei suggests she stay with unchanged Iori/Chinatsu (u:0080-0136). Sena asks Sensei's support for war preparation but receives no endorsement; Fuuka/Juri and Erika/Kirara offer normal help (u:0137-0198). Satsuki enters their inquiry group unaffected by her account and offers a distinct historical lead (u:0212-0241). 402/480, C002 E001 unopened.


## S2 V002 C002 E001 relationship state delta

Satsuki breaks her earlier silence to tell Sensei/Iori/Chinatsu/Iroha a private historical account and admits she does not know how to reverse the change (scene:001:u:0001-0042). She sees Makoto's enemy-focused drive as unusually serious and wants him back; Iori challenges her exception but accepts help (u:0043-0070). The group agrees to try within Gehenna first, with Schale reserved and Sensei offering discreet support; Iroha/Chinatsu/Iori thank or trust Sensei (u:0071-0136). Iori's private plea for her seniors confirms continuing loyalty despite opposing their current program (u:0137-0143). 403/480, E002 unopened.


## S2 V002 C002 E002 relationship state delta

Sena remembers Chinatsu's move from Emergency Medicine to Prefects, reveals private pride and disappointment, and continues to trust her former trainee; Chinatsu respects Sena and clarifies she did not leave from dissatisfaction (scene:001:u:0017-0059). Their current conflict is explicit when Sena expects wartime medical support and Chinatsu questions civilian harm (u:0048-0080). Sena ends gently and hopes Chinatsu finds the right path; Chinatsu sees familiar trust but resolves to restore her (u:0081-0094). No rupture, acquiescence or successful reversal is shown. 404/480, E003 unopened.


## S2 V002 C002 E003 relationship state delta

Mayumi/Karen question Shoko's new war endorsement and insist range training was for recreation; Shoko invokes their own work and shared authorship to press them (scene:001:u:0001-0070). A Pandemonium senior summons Shoko to Makoto, then cheerfully tells Mayumi/Karen old Gehenna should return; they confront her prior warning, but she says she changed her mind (u:0071-0108). No committee agreement, strategy meeting or reconciled trust follows. The senior is continuous with S2 V002 C001 E003 by Karen's recognition, while local A-D are new unlinked roles. 405/480, E004 unopened.


## S2 V002 C002 E004 relationship state delta

Makoto/Hina/Ako/Shoko coordinate in a strategy room, though Makoto/Hina acknowledge resistance among their own colleagues; Shoko urges tighter internal control (scene:001:u:0002-0043). A Pandemonium member and Prefect officer jointly pressure a student to surrender ammunition, a direct coercive institution-student interaction (u:0044-0063). Three second-years speak from fear, curiosity and target fantasies without clear consent. Mayumi/Karen privately question the leadership's version of unity and decide to seek an answer, not yet confronting it (u:0064-0098). 406/480, E005 unopened.


## S2 V002 C002 E005 relationship state delta

Karen/Mayumi move their E004 private doubt into a direct confrontation with Makoto, but depart after he insists on the campaign; no committee assent or dissolution follows (scene:001:u:0007-0046). Iroha explicitly breaks with Makoto and Pandemonium, Makoto permits departure while invoking a lost successor possibility, and Ibuki's immediate protest reveals the personal cost within their circle (u:0047-0090). Chiaki/Satsuki tend Ibuki; their support does not settle Iroha's future ties. Shoko urges Makoto to treat Iroha as a suspect, but he refuses to cede disposition, showing adviser access with a boundary (u:0091-0106). 407/480, E006 unopened.


## S2 V002 C002 E006 relationship state delta

Pandemonium's messenger threatens Kasumi for questioning a warehouse order, then treats Meg's enthusiasm as Hot Spring Club assent, overriding Kasumi's hesitation (scene:001:u:0001-0034). Kasumi both defers to Meg's present words and doubts whether her friend's current war preference is genuinely hers; she avoids simply replacing Meg's judgment with her own (u:0035-0079). Sensei notices the strain, listens despite visible exhaustion, shares a narrated situational account and respects Kasumi's wish to postpone private history. Kasumi then commits to helping Meg and offers Sensei cooperation; no change in Meg's outlook or practical joint action yet (u:0048-0109). 408/480, E007 unopened.


## S2 V002 C002 E007 relationship state delta

Mayumi/Karen seek Sensei privately, share anxiety about Gehenna and their committee's possible complicity, and accept his handholding/reassurance enough to weep and recover (scene:001:u:0001-0066). Their mutual bond survives disagreement with Makoto and becomes a joint promise to stop this course (u:0067-0070). Shoko is absent: they perceive a split and her adviser work, acknowledge they have not properly talked with her, and ask Sensei to try. This is a pending relationship repair attempt, not a resolved reconciliation or final rupture (u:0071-0080). 409/480, E008 unopened.


## S2 V002 C002 E008 relationship state delta

Makoto notes Iroha's absence as a practical burden; Chiaki sees him lonely, Satsuki scarce and Ibuki subdued, adding the council's lived cost to E005's split without speaking for absent members (scene:001:u:0001-0014). Chiaki approaches Shoko through shared-secretary rapport, but their interview reveals opposed views of Gehenna's quiet and the projected conversion of other schools. Shoko ends the exchange after Chiaki asks about her desired life beyond order (u:0019-0082). Chiaki remains in Pandemonium and privately worries; no organized opposition or Shoko reconciliation is printed (u:0083-0090). 410/480, E009 unopened.


## S2 V002 C002 E009 relationship state delta

Satsuki invites Sensei into a protected workroom, says he is its first outsider, seeks his cooperation as a subject because other students face too much risk, and shares coffee and institutional history. He acknowledges a prior willingness to help but no experiment occurs (scene:001:u:0001-0038/u:0061-0064). Satsuki calls Makoto a joint disposer of old materials and speculates that he trusted her not to misuse information; Makoto does not speak here and the motive is not established (u:0044-0056). The unnamed former bureau member and alleged external group cannot be turned into definite relationship edges (u:0041/u:0058-0060). 411/480, E010 unopened.


## S2 V002 C002 E010 relationship state delta

Karen distrusts the Prefects/Pandemonium students and Iori distrusts the Restoration Committee; Chinatsu and Iroha make Sensei's convening and shared concern sufficient for provisional cooperation, without erasing suspicion (scene:001:u:0001-0023). Mayumi/Karen find value alignment with Iori/Chinatsu over limits on war; Chiaki joins the group despite her E008 private uncertainty, and Satsuki arrives with a clue. Shoko is absent and still disagreed with; Ibuki is intentionally not included as too young, according to Satsuki/Iroha (u:0035-0065). Chiaki's broadcast-room idea earns Satsuki/Iroha's praise, a local competence-recognition shift, not yet a successful mission (u:0078-0094). 412/480, E011 unopened.


## S2 V002 C002 E011 relationship state delta

Ibuki misses Iroha and finds Makoto busy and Satsuki/Chiaki absent. Iroha returns only to check on Ibuki, offers to bring her along and provide familiar care, but honors Ibuki's choice to stay with Makoto so he will not be lonely. They make a conditional reunion promise, without resolving the Makoto/Iroha split (scene:001:u:0001-0063). Ibuki presses Makoto about missing Iroha beyond his claim of work competence; the later unknown-log intrusion and headache are followed by his assurance that Ibuki is blameless and may stay by choice (u:0064-0110). This repairs an immediate Ibuki/Makoto interaction, not the whole council relationship. 413/480, E012 unopened.


## S2 V002 C002 E012 relationship state delta

Shoko meets Mayumi/Karen in person and refuses their understanding of restoration, threatening them if they continue; old familiar banter briefly resurfaces but does not erase the split (scene:001:u:0037-0081). Hina confronts her Prefect subordinates, Iroha and the committee as suspected dissenters, then draws Sensei aside. In private she still seeks his approval and fears he will dislike her, while he cannot endorse conquest; she nevertheless moves to keep him from the others (u:0082-0176). This is a live Hina/Sensei trust breach and proposed separation, not completed custody or full Hina recovery. 414/480, E013 unopened.


## S2 V002 C002 E013 relationship state delta

Makoto visits confined Sensei, admits reluctant consent and tries to persuade him that Gehenna domination would benefit all; Sensei recalls Makoto's earlier free-Gehenna wish, prompting pain and withdrawal rather than agreement (scene:001:u:0001-0027). Shoko visits across the cell boundary, says she caused the recommendation to confine him, and expects hatred. Sensei instead continues concern for her judgment and possible self-reproach; she angrily rejects his gaze (u:0028-0071). The relationship is strained and emotionally exposed, not reconciled; Sensei remains incarcerated. 415/480, E014 unopened.


## S2 V002 C002 E014 relationship state delta

The coalition's concern for detained Sensei coexists with a reported prior strategy: members trust his assigned roles but fear Hina and the consequences of exposure (scene:001:u:0001-0041). Fuuka pushes back against Pandemonium/Prefect ration messengers; Juri supports kitchen work but reports hazards. Haruna/Akari work beside the Lunch Club while voicing pro-war values that Fuuka/Junko/Izumi reject; Haruna/Akari later discourage Makoto from punishing Fuuka because she is indispensable, not from political solidarity (u:0042-0144). Ako and Makoto recognize a supply dependency and dispute responsibility, then Makoto pivots to a destructive weapon proposal. No direct Fuuka-coalition contact is shown (u:0114-0174). 416/480, E015 unopened.


## S2 V002 C002 E015 relationship state delta

The coalition uses a covert entry phrase and worries that surveillance of them has increased. Karen/Iori still spar verbally, but the disagreement regulates haste rather than breaking cooperation (scene:001:u:0001-0049). Iroha recruits Erika/Kirara for their broadcast experience; they affirm friendship with her and with students at other schools, and volunteer despite risk (u:0050-0080). Satsuki recognizes Erika's proposed technical route, then Chiaki's warning leads Iori/Iroha to move immediately. The recipient of Iroha's intended additional contact remains unnamed (u:0081-0114). 417/480, E016 unopened.


## S2 V002 C002 E016 relationship state delta

Kasumi personally reaches Sensei through the cell-floor tunnel and says Meg's changed state also motivates her. Their contact renews E006's offer of cooperation, without a confirmed safe handoff (scene:001:u:0001-0021). Junior Prefects oppose their seniors while apologizing, and Iori/Chinatsu commit to confronting Hina to uphold the line that defined their service (u:0022-0046). Iroha coordinates diverse allies and asks Chiaki to shepherd Sensei; Satsuki reassures her despite admitted technical risks (u:0047-0083). Current enemy response is engaged but the relationship with Hina is not yet tested in direct battle (u:0084-0093). 418/480, E017 unopened.


## S2 V002 C002 E017 relationship state delta

Iori/Chinatsu confront Hina as injured subordinates who still value the boundary she taught them; Ako tries to shield Hina from their challenge and argues for her relief through unified war. Their disagreement is ethical and personal, not a completed reconciliation (scene:001:u:0001-0076). Sensei reaches Iori and accepts the next stage while Kasumi stays to the rear and Chiaki escorts him; Karen/Mayumi step in to support the exhausted Prefects (u:0077-0111). Makoto acknowledges Iroha/Chiaki as dissenters. Shoko's Thunder Emperor declaration widens the breach with Mayumi/Karen beyond committee tactics (u:0112-0135). 419/480, E018 unopened.


## S2 V002 C002 E018 relationship state delta

Shoko reveals to Mayumi/Karen that her committee partnership served the Emperor agenda, rupturing their prior trust; Sensei's concern about her own agency produces anger rather than reconciliation (scene:001:u:0001-0088). Technical allies bring relief then fear as third-years suffer, and Iroha's mix of reproach and affection becomes an immediate appeal to Makoto. He recognizes her voice, rejects the Emperor and apologizes after local recovery; their bond resumes in practice amid Iroha's protests, with formal Pandemonium status uninspected (u:0091-0292). Shoko admits deliberately steering her former colleagues and Mayumi rejects her greatness; Karen threatens a blow, but no strike or sanction is printed (u:0293-0320). 420/480, E019 unopened.


## S2 V002 C002 E019 relationship state delta

Hina publicly accepts wrongdoing toward her own subordinates and tries to resign; Makoto intercedes while she insists her decisions remain hers. Their exchange joins institutional responsibility with individual agency, without a settled allocation of liability (scene:001:u:0020-0064). Hina privately apologizes to Iori, Chinatsu and Ako, recalls firing on them, and commends the juniors for resisting according to her former teaching. They return to shared work, with emotional trust rebuilding in speech rather than fully repaired (u:0107-0139). Mayumi/Karen reclaim their committee purpose after Shoko's betrayal; Shoko's later status is not shown (u:0089-0106). Sensei thanks and encourages Makoto while he names the harm he inflicted, giving homework to be himself without speaking for the victims' forgiveness (u:0162-0188). Iroha notices his shaken condition and seeks his familiar self, while Makoto resists reducing his recovery to willpower alone (u:0189-0236). The group assembles for Sensei's photo offer, not a documented enduring alliance settlement (u:0237-0247). 421/480, E020 unopened.


## S2 V002 C002 E020 relationship state delta

Fuuka serves the Gourmet group despite irritation; Haruna apologizes to Fuuka/Juri, and Akari apologizes for constraining others. Izumi says their altered conduct was frightening. Fuuka makes future meals conditional on no repeat, and Izumi sets a dining boundary, so the group resumes conversation without erasing the harm (scene:001:u:0001-0054). Sena tells Chinatsu she regrets her medical rhetoric and is proud of the junior's resistance to Hina; probable tag drift at u:0077-0079 should not be mined for exact voice, but the exchange ends with mutual thanks (u:0055-0088). Meg's trust in Kasumi does not become blind deference: Kasumi asks her to define what she wants, and Meg chooses continuing life with Kasumi and the club (u:0096-0126). Kasumi privately withholds the Bodensatz worry from Meg in this scene (u:0127-0138). 422/480, E021 unopened.


## S2 V002 C002 E021 relationship state delta

Hina risks a more shameful confession to Sensei than her public E019 apology: she liked part of preparing violence and fears unfitness as chair. Sensei answers with trust in her history of guarding a line and acknowledgment of shared human weakness; she asks for continued presence and he agrees (scene:001:u:0001-0047). This deepens a supportive bond without a blanket absolution for harmed students. Sensei visits Shoko in confinement, brings her preferred sweets and promises to wait for her to move forward; she refuses remorse but gives him the Arashi name and privately cries. The relationship has contact and limited disclosure, not reconciliation or accepted accountability (u:0048-0085). Hina and Makoto share an Arashi/Emperor concern; Makoto withholds the Ibuki implication in a private thought, so no printed Hina-Ibuki confrontation follows (u:0086-0102). 423/480, checkpoint next.


## S2 V003 C001 E001 relationship state delta

Arona first defends, then apologizes for missed boarding; Sensei shares the lapse and invites Arona/Plana to search for small treasures. Their simultaneous delight and shell exchange show ordinary cooperative play, while tag drift blocks detailed voice attribution (scene:001:u:0001-0034). Arona reacts protectively to `S.O.S.`, Sensei asks for more evidence, and Plana reluctantly points to the council-president claimant as an information source (u:0035-0050). The claimant cooperates with Sensei's request to investigate the object but then orders all Odysseia ships back on her own claimed authority. No renewed trust or identity authentication between her and Sensei is proved by his consultation (u:0051-0076). 424/480, E002 unopened.


## S2 V003 C001 E002 relationship state delta

Mai presses Sensei for an explanation; the claimant intervenes to protect his confidential student contacts and offers Mai a future interview. Mai accepts and holds her junior from chasing the claimant, with no interview yet (scene:001:u:0015-0043). Sensei thanks the claimant and worries whether joining him cost her work time; she says the visit gives her a break, then makes an unexplained correction about a prior Odysseia visit (u:0041-0054). Sumika recognizes Sensei from a Pandemonium-linked encounter, fears a complaint, and asks him to validate today's escort after he reassures her (u:0071-0091). Minato and Ami receive the claimant and Sensei formally, with Minato welcoming the latter by reputation. Their acceptance of the claimant as president is present social recognition, not identity proof (u:0102-0125). 425/480, E003 unopened.


## S2 V003 C001 E003 relationship state delta

Minato and the claimant politely disagree on whether to tour first; Sensei's willingness resolves the immediate conflict. Sumika worries which authority outranks the other, but no formal jurisdiction decision is made (scene:001:u:0001-0018). Ami manages Sammy with affectionate discipline and later leaves to retrieve him when his escape causes trouble (u:0019-0033/u:0058-0073). Minato presents Odysseia's food and cruise clubs; Sumika's dessert story embarrasses the captain, with some speaker drift (u:0039-0057). Mitsuki welcomes Sensei and the claimant, then tries to wager a ship on their approval; Ami interrupts and requests they ignore further bets, a familiar corrective relationship by her account (u:0084-0125). The claimant enjoys the tour despite delay, and accepts Minato's invitation to curry dinner (u:0135-0153). 426/480, E004 unopened.


## S2 V003 C001 E004 relationship state delta

Mitsuki serves the claimant and Sensei curry and intends to tell kitchen students their praise; a habanero prank idea is stopped before action. Sumika admires the claimant's clean clothes, while Minato/Ami tease and police propriety (scene:001:u:0002-0042). Minato dismisses Sumika and others for private business, then relaxes; Ami scolds her but Sensei says she is easier to speak with, showing a less formal working rapport (u:0043-0061). Minato explains seafaring taboos and Sensei respectfully asks about their limits (u:0062-0084). When shown the ball, Minato recognizes her own former object, Sammy interrupts and Ami corrals him, linking school inquiry to their shared care for the cat (u:0085-0105). No full trust or emergency finding follows. 427/480, E005 unopened.


## S2 V003 C001 E005 relationship state delta

Minato apologizes to Sensei/claimant for the misleading toy; the claimant expresses relief, Sensei addresses Sammy as owner and the cat accepts contact. Ami calls Sammy broadly loved (scene:001:u:0001-0017). Minato and Ami share worry over Sammy's worsening condition and student distress. Embedded speakers A/B favor shore care, C/D fear abandoning their long-term companion to unfamiliar carers, without a reconciled collective choice (u:0018-0064). Minato turns to the claimant and Sensei because she cannot decide through familiar rules. The claimant presses sole captain accountability; Sensei interrupts to offer investigative help, and the claimant agrees to a bounded week, establishing a temporary cooperative inquiry without taking the decision away from Minato (u:0065-0094). 428/480, E006 unopened.


## S2 V003 C001 E006 relationship state delta

Sensei sees Sammy welcomed by students across ships; laundry A/B worry for his cough even as they fear the storm taboo (scene:001:u:0001-0026). Cruise loading members warn Sammy away from a railing, then become vulnerable to Mitsuki's punishment threat after his slip. The text does not show disciplinary follow-through (scene:002:u:0002-0025). Trident members tease Sumika about appointing herself supervisor, but Sammy's sudden slip makes Sumika nearly fall. Sensei catches the crisis; she thanks him and then notices the strong impact may have hurt him. His reported weakness leaves the rescue relationship open to a care response next (scene:003:u:0002-0037). 429/480, E007 unopened.


## S2 V003 C001 E007 relationship state delta

Sanae treats Sensei, jokes sharply about Trident patients and gives rest advice. Sumika apologizes to him yet quickly asks that her vice leader not hear of the near fall; no completed concealment is shown (scene:001:u:0002-0026). In frustration Sumika shakes Sammy and blames him; Sanae intervenes for his welfare, then Sumika voices fear that sending him away might make his last days worse (u:0027-0047). Their positions both contain care but differ on inference and authority. The claimant arrives, asks after Sensei's back and invites him to Island; Sensei accepts in choice-space. Her concern is present, but the supposed Island difficulty is still an expectation (u:0048-0059). 430/480, E008 unopened.


## S2 V003 C001 E008 relationship state delta

Ami pushes Minato to decide as rumor grows; Minato rejects equating Sammy's removal with the end of misfortune and still feels the school pressure. Sensei and the claimant arrive; Sensei limits Schale blame for his injury and encourages a public correction (scene:001:u:0001-0035). Minato then discloses both her principled awareness and her intimate attachment to Sammy, whom she calls a long-time friend after recalling the toy she made (u:0036-0070). The claimant offers to bear external resentment and take Sammy; Minato yields verbally. That shifts proposed responsibility but does not establish Sammy's consent, a trustworthy care handoff or settled student relations (u:0071-0087). 431/480, E009 unopened.


## S2 V003 C001 E009 relationship state delta

Students prepare to part from Sammy, disagreeing about shore care and the claimant's intervention while no one defies the removal decision. Gift givers are affectionate but revise excessive offerings, and Sumika faces their practical requests (scene:001:u:0001-0047). Narration records displeased looks at the claimant, who smiles; she later tells Sensei she took this hostility deliberately to spare his trusted-teacher relationship and push Minato beyond her captain role (u:0048-0086). Sensei asks how office constrains the claimant herself, and she admits she cannot imagine life as a normal student. He promises to support a future chosen wish, strengthening their present personal rapport without resolving her identity dispute or the cat's welfare (u:0087-0107). 432/480, E010 unopened.


## S2 V003 C001 E010 relationship state delta

Minato and Ami coordinate with the claimant over departure, yet Minato regrets not asking sooner and the claimant minimizes her own role. The Island member's ordinary-walk observation does not disclose Sammy's intent (scene:002:u:0002-0034). Odysseia and Trident students hide Sammy to retain time with him, turning quiet affection into local obstruction. Minato's account of school obedience is destabilized by their action (u:0056-0087). Minato risks a bow pursuit and falls into the sea; Sammy approaches, and she interprets this as worry for her, thanks him and apologizes. Their reciprocal bond is her articulated reading of a visible act, not a tested transfer preference (u:0088-0126). 433/480, E011 unopened.


## S2 V003 C001 E011 relationship state delta

Minato asks the claimant to reverse Sammy's removal despite predicted public ripples, saying her fear remains but she cannot expel a friend merely to keep taboo. The claimant accepts her answer (scene:001:u:0015-0045). Ami remains concerned about students who believe Sammy brings misfortune; Minato proposes that ordinary closeness may persuade over time, an untested relationship strategy (u:0046-0055). The claimant says she has lost Odysseia goodwill and asks Sensei for a local ice cream; he responds, but purchase is not shown. Sanae later calls Sensei urgently about Sammy's critical night, making care the live issue; no outcome is known (u:0056-0073). 434/480, E012 unopened.


## S2 V003 C001 E012 relationship state delta

Sumika is shocked by Sammy's deterioration and objects to the taboo; Sanae limits her intervention to Island authority while caring for the cat. Minato blames herself, and Sanae urges presence rather than single-cause counterfactuals (scene:002:u:0006-0017, u:0025-0026). Ami shares attachment but asks Minato to honor the major death-at-sea taboo. Sensei tries to redirect the discussion; Minato asks him to let Odysseia decide (u:0018-0031). Minato publicly names Sammy a friend and proposes a final voyage based on memories of his favored shipboard life, offering classmates leave without penalty. Collective acceptance and Sammy's current preference remain unknown (u:0032-0053). 435/480, E013 unopened.


## S2 V003 C001 E013 relationship state delta

Mai attempts to explain an unusual voyage from outside, but receives only a relayed 'seeing off a friend' purpose. Onboard, Minato speaks directly to weakly vocal Sammy and shows him the sea (scene:001:u:0001-0014; scene:002:u:0002-0016). Mitsuki and Trident students insist on joining; their participation supports a broader relationship beyond Island, while guest approval and all-club turnout remain unshown (u:0017-0043). Minato points to the school loving Sammy and carries him to his usual place; narration surrounds him with friends as his voyage ends (u:0044-0055). Five new narrow roles, 21 partial / 283 unmodeled across 304, 436/480. E014 unopened.


## S2 V003 C001 E014 relationship state delta

Sumika and a Trident peer continue automatic Sammy-care habits while grieving; Sensei visits privately and asks to be received as a friend, a label Sumika tentatively accepts (scene:001:u:0001-0027). Sumika's right-foot reminder is explicitly protective toward Sensei despite admitted superstition (u:0033-0037). Minato says all are outwardly well, keeps Sammy's cushion and credits Sensei, while her general claims of satisfaction lack independent voices (u:0038-0062). The claimant seeks Sensei to discuss Odysseia, praises Minato, then leaves an unexplained 'real captain' challenge when the train arrives (u:0063-0093). Two new narrow roles, 21 partial / 285 unmodeled across 306, 437/480. Backfill E001 next.


## V001 C003 E001 backfill relationship state delta

Francis addresses the Dweller as an expelled colleague and tries to warn/help it; the Dweller rejects his advice violently and claims solitary true-Gematria standing (scene:001:u:0001-0062). Yume and Hoshino share excitement, failed digging, mutual blame and a notebook disagreement in an earlier layer; label drift prevents assigning every comic turn (u:0063-0112). In the present committee, Shiroko/Nonomi retrieve a withdrawn Hoshino, then Ayane leads a shared debt briefing. Serika hopes to buy the claims, while a sudden sellout defeats that plan; the group reacts to Nephthys attribution, without revealing its decision-maker or effect on Nonomi (scene:002:u:0002-0104). Three new narrow subjects, 21 partial / 288 unmodeled across 309, 438/480. E002 unopened.


## V001 C003 E002 backfill relationship state delta

In an earlier encounter, Hoshino recognizes Nonomi as a Nephthys successor, threatens her and then sees she is frightened; no later durable hostility can be inferred from that slice alone (scene:001:u:0023-0068). In the present, Nonomi admits her family's company connection. Ayane says she suspected it from card and railway access, Serika is shocked but affirms Nonomi staying, and others' exact prior knowledge is blurred by swapped speaker labels (u:0069-0110). Nonomi asks Ayane to examine rights and says she does not know her family's purchase motive, creating an unclosed personal/institutional tension (u:0111-0138). Three new narrow subjects, 21 partial / 291 unmodeled across 312, 439/480. E003 unopened.


## V001 C003 E003 backfill relationship state delta

Ayane speaks for Abydos territorial consent and asks Sensei to command pursuit; Nonomi insists Highlander should have consulted first (scene:001:u:0032-0069). The twins rely on speed and their administrator, then face local defeat. Suou distances herself from them while apologizing as supervisor, describing internal mutual checks rather than school unity (scene:002:u:0001-0029). She singles out Nonomi as possibly informed by Nephthys; Nonomi's hesitant reply does not prove acquaintance or purchase control. Hoshino allows the twins to go under a promised later explanation (u:0030-0049). Four new narrow subjects, 21 partial / 295 unmodeled across 316, 440/480. E004 unopened.


## V001 C003 E004 backfill relationship state delta

Hoshino rescues Yume, then scolds her trust; Yume asks him to maintain aid and counts on his protection. The exchange establishes disagreement inside strong mutual reliance (scene:001:u:0001-0063). After her loss, Hoshino avoids closing her room. Nonomi offers family funds, receives a protective/sovereignty objection and promises to return under her own name (u:0064-0116). On a later visit she finds Hoshino distressed, mentions incomplete Yume reports, sees the decayed school and questions a privileged Highlander path, without a completed transfer in this episode (u:0117-0188). In the present Hoshino admits Suou and twins after an impatient bell, leaving trust unresolved (u:0189-0216). Two new narrow scammers, 21 partial / 297 unmodeled across 318, 441/480. E005 unopened.


## V001 C003 E005 backfill relationship state delta

Suou disciplines the twins and apologizes to Sensei for earlier miscommunication; the twins' casual challenge increases Abydos tension (scene:001:u:0001-0040). Nonomi recognizes the Nephthys executive who cared for her, but he appears with investors she did not expect and does not answer why her family backs the railway (u:0061-0106). Sensei asks for proof before dialogue and supports Ayane's Committee standing; Hoshino clarifies the old council's nominal persistence (u:0061-0078, u:0107-0132). The representative produces an alleged Yume-signed paper, provoking Hoshino without revealing the relationship's historical legal terms (u:0133-0137). Four narrow visitor roles, 21 partial / 301 unmodeled across 322, 442/480. E006 unopened.


## V001 C003 E006 backfill relationship state delta

Hoshino recognizes Yume's handwriting and says she had collected every remnant of her, making the unknown contract personally destabilizing (scene:001:u:0008-0025). Sensei protects deliberation time against investor pressure while Hoshino hesitates; the creditors' impatience does not produce a signature (u:0031-0071). Ayane asks for older council history. Hoshino discloses the 33-day absence, halo-destroyed discovery and her own knowledge gap; Nonomi tries to shield her, then Shiroko follows when the date match sends her out (u:0084-0158). Same-day contract is not proven cause of Yume's loss. 21 partial / 301 unmodeled across 322, 443/480. E007 unopened.


## V001 C003 E007 backfill relationship state delta

Shiroko asks Hoshino to stop hiding distress from the group. Hoshino uses humor to escape and says she needs to be alone; Shiroko pursues, fails to catch her and relays a tomorrow promise, so concern remains active (scene:001:u:0001-0040). Nonomi risks a call to her longtime Nephthys attendant; he offers money/card support while withholding business facts and blaming unspecified past damage, leaving familial trust strained (u:0041-0074). Sensei asks the group to rest and returns to Schale to investigate, while Arona worries about his overnight work and Plana later calls out over gas anomaly (u:0075-0167). 21 partial / 301 unmodeled across 322, 444/480. E008 unopened.


## V001 C003 E008 backfill relationship state delta

Plana asks Sensei to rest, protects him during Schale explosion, then is unconscious by Arona report; Arona worries and Sensei awareness fades. Their later states are open (scene:001:u:0001-0030). The committee cannot reach Sensei or Hoshino; Hoshino privately intends to return (u:0031-0045). Earlier, Yume thanks a stern newly enrolled Hoshino for stopping violence, and he later protects her from threatening locals and returns next day to help with petition despite denying concern. Her wish to be called senior suggests growing closeness, not a completed council appointment (u:0046-0131). Four narrow roles, 21 partial / 305 unmodeled across 326, 445/480. E009 unopened.


## V001 C003 E009 backfill relationship state delta

Yume and Hoshino tease each other over a notebook and whale design; Yume hopes Hoshino will inherit the diary, while Hoshino deflects its appearance and remains close despite earlier council refusals (scene:001:u:0017-0062). Their lost-item trip shows Yume taking risk for another person and Hoshino supplying a reserve compass (u:0063-0084). In the later historical cut Yume and Hoshino promise mutual protection; Hoshino accepts council membership, and Yume embraces her and wants a photo (u:0110-0155). In the present Ayane and Serika act without Hoshino's permission, Shiroko and Nonomi are already in the room, and Hoshino rebukes cabinet opening; the objection must remain part of the relationship record (u:0085-0109, u:0156-0198). No new subjects: 21 partial / 305 unmodeled across 326, 446/480. E010 unopened.


## V001 C003 E010 backfill relationship state delta

Hoshino acknowledges anger toward Yume and herself, reports a harsh festival-poster rebuke, then says she sent Yume away after rescuing her from thugs and intended to apologize before the disappearance (scene:001:u:0006-0048). This is retrospective self-reproach, not proof her rebuke caused Yume's death. She searched and recovered remains/equipment but still seeks the missing notebook for an explanation (u:0049-0072). Nonomi's conditional Nephthys worry threatens her sense of belonging without establishing family culpability. The executive arrives as her earlier-called `執事さん` and promises only a railway discussion; Hoshino and Shiroko leave the room together (u:0073-0087). No new subjects: 21 partial / 305 unmodeled across 326, 447/480. E011 unopened.


## V001 C003 E011 backfill relationship state delta

The Nephthys caretaker offers Nonomi a stronger card and Highlander return; Shiroko names her discomfort, Suou blames her Abydos choice, and Serika later refuses any solution that sacrifices her membership (scene:001:u:0005-0026; scene:005:u:0032-0043). Hoshino considers Yume contract continuation as the immediate protective path, but the executive's alternate invalidation proposal would erase the two-person council's authority, putting her history at stake (scene:001:u:0114-0124; scene:005:u:0044-0061). After visitors leave she gathers peers to deliberate, with Shiroko reinforcing collective possibility and Ayane calling rest (scene:005:u:0062-0081). Three new role actors: 21 partial / 308 unmodeled across 329, 448/480. E012 unopened.


## V001 C003 E012 backfill relationship state delta

Hoshino/Nonomi meet self-named Shiroko in the cold, offer a scarf, shelter and uniform, and later correct her scrap/truck scheme through apology rather than abandonment. Duel-for-enrollment terms are recalled, but no result is shown; Shiroko still has boundary-testing humor in the present (scene:001:u:0002-0115). Nonomi credits Shiroko with helping her stay in Abydos and Hoshino smile. Ayane/Serika's remembered arrival broadens the original three into five (u:0116-0178). Shiroko and Nonomi press Hoshino about the Yume council name; he admits some grief but asks peers to prioritize locating/destroying the gun and reaching the assembly. They accept the immediate plan without dissolving either bond or institution (u:0179-0220). News of Sensei's injury reaches them only at the close (u:0221-0234). One scrap-dealer role: 21 partial / 309 unmodeled across 330, 449/480. E013 unopened.


## V001 C003 E013 backfill relationship state delta

Nonomi approaches her former caretaker seeking a corporate solution that would preserve both Abydos institutions. He shames her with unspecified old damage, receives an apology under pressure, admits using the Schale/fund collision, and recasts her as hostage; the board authorization he invokes is uninspected (scene:001:u:0028-0127). Nonomi's message asks peers to forget her and keep Yume council, but its distressed/mediated form cannot erase her E012 wish to remain (u:0128-0141). Hoshino fears losing another loved person and assigns future liability to herself alone; Shiroko challenges her in a familiar relational language rather than accepting exclusion, and Serika/Ayane react with concern (u:0142-0180). No new subject: 21 partial / 309 unmodeled across 330, 450/480. E014 unopened.


## V001 C003 E014 backfill relationship state delta

Hoshino tells Shiroko that Nonomi saved her when she perceived the world as hostile, and now frames Nonomi's rescue as her own turn. She excludes the Committee from responsibility despite their shared history (scene:001:u:0011-0034). Shiroko openly names their memory asymmetry about Yume, then says Hoshino is also one of `みんな`; Hoshino apologizes but persists. Ayane angrily invokes an earlier departure pattern and Sensei's help in reuniting them, while Serika joins the intervention. The immediate contest has no printed resolution (u:0035-0055). No new subjects: 21 partial / 309 unmodeled across 330, 451/480. E015 unopened.


## V001 C003 E015 backfill relationship state delta

Yume historically prized daily time with Hoshino and asked her to stay beside/protect future juniors. Hoshino now calls Ayane/Serika Abydos's future, asks them to protect later students, and leaves despite their attack. She asks them to apologize to Sensei and says Nonomi/Shiroko/Ayane/Serika can continue as a team (scene:001:u:0001-0049). Shiroko checks on peers, is reported most injured and cannot identify a next step; Ayane says they failed to stop Hoshino (u:0050-0060). Hoshino privately vows not to repeat her earlier mistake with Nonomi, but rescue has not happened (u:0066-0069). No new subjects: 21 partial / 309 unmodeled across 330, 452/480. E016 unopened.


## V001 C003 E016 backfill relationship state delta

Sensei returns from hospital because of a promise, calms Serika/Ayane/Shiroko, asks to sort facts and receives their shared resolve to save Nonomi and Hoshino. Shiroko's wish that Hoshino not have to deny Yume's council is accepted by Sensei (scene:001:u:0030-0110; choice:001-010). Ayane volunteers for president in a three-student vote and announces preservation of Committee name; Serika jokes about forceful leadership while endorsing her. Ayane recasts absent Hoshino as secretary to limit her asserted solo contract power, and Sensei offers to locate Nonomi (u:0111-0174; choice:011-015). Group departs together; no rescue or Hoshino acceptance yet (u:0175-0192). One doctor role: 21 partial / 310 unmodeled across 331, 453/480. E017 unopened.


## V001 C003 E017 backfill relationship state delta

Sensei reports Nonomi's station location, and Shiroko thanks him, believing their rescue/contract/Hoshino aims can converge. An earlier Serika-abduction recollection has Shiroko and Sensei explaining Hoshino's unspoken worry; Serika reacts with embarrassed thanks, not present Nonomi participation (scene:001:u:0011-0049; choice:001). Ayane acts as on-site president, Shiroko predicts Hoshino's route, and Serika urges pursuit (scenes:002-007). Ayane tracks Hoshino pulling rapidly away; Shiroko runs after her without contact (scenes:009-010). Five narrow roles: 21 partial / 315 unmodeled across 336, 454/480. E018 unopened.


## V001 C003 E018 backfill relationship state delta

Suou tells the fund about Nephthys betrayal, then President reveals her former PMC tie; executive calls her ungrateful for Nephthys support, with current allegiance unresolved (scene:001:u:0017-0028). President turns on both investor representatives and Nephthys to pursue gun information and asserts subsidiary control under armed pressure (u:0029-0128). Sensei and the Committee choose to help surrounded Highlander students despite limited time; twins/student thank or accept assistance, but they still do not understand the dispute (scenes:002-006; choice:001). Hoshino is separately seen standing after General falters; no exchange with the Committee proves reconciliation (scene:006:u:0002-0028). No new subjects: 21 partial / 315 unmodeled across 336, 455/480. E019 unopened.


## V001 C003 E019 backfill relationship state delta

Nonomi confronts the former caretaker over Kaiser collusion and rejects his power-for-Abydos rationale, while Suou invokes a doubtful past-violence analogy (scene:001:u:0010-0027). Hoshino reaches Nonomi, asks about injury and considers council invalidation to secure release; Nonomi offers to leave Abydos to remove hostage value and begs her not to sacrifice herself. No formal withdrawal follows (scene:003:u:0002-0047). Sensei/Ayane/Shiroko/Serika arrive before noon to contest Hoshino's solitary act; President rejects their voice and orders Nonomi taken. Final cut shows Hoshino and Nonomi still together and group pursuit beginning (scenes:004-006). One PMC B role: 21 partial / 316 unmodeled across 337, 456/480. E020 unopened.

## V001 C003 E020 backfill relationship delta

Nonomi is with the group after the assembly and protests her card seizure; card possession now passes visibly to Suou, but her physical custody and card use afterward are unshown (scene:001:u:0010-0018). Shiroko, Serika, Ayane, Nonomi and Sensei urge Hoshino to stay and plan with them, invoking both Nonomi safety and old council continuity (u:0058-0067; choice:001). Hoshino apologizes and thanks them for guarding Yume memory, yet refuses joint action in order to assign blame to herself; that is a renewed relationship rupture rather than durable reconciliation (u:0068-0084). Suou shifts from corporate intermediary to direct Hoshino challenger, but the cause of President/pilot distress and Suou's precise action remain unprinted (u:0031-0048).

## V001 C003 E021 backfill relationship delta

Nonomi hears her caretaker's apology and past-glory account, states she can say nothing further, then parts to pursue Hoshino; remorse is shown, absolution is not (scene:001:u:0010-0032). Serika counters Shiroko's self-blame, while Ayane/Nonomi/Shiroko name Hoshino's threatened lone liability and Yume-shadow pattern (u:0033-0049). Nonomi argues the group must solve it themselves rather than recruit only a stronger fighter (scene:002:u:0015-0019). The executive nevertheless provides location and branch information; Hikari, Nozomi and clerk volunteer rail help after being aided, and the group boards together (u:0026-0109). Their aid is a concrete but risky reciprocity, not proof Hoshino is yet reached or reconciled.

## V001 C003 E022 backfill relationship delta

Nozomi/Hikari choose to shield the Abydos group with a timed rail diversion; Nonomi thanks them, Shiroko physically prioritizes Sensei, and the group escapes after a difficult dismount (scene:001; scene:002:u:0016-0021). Hikari faces PMC and asks not to be shot, using banter to conceal the passengers; release or capture is not shown (scene:002:u:0005-0015). Ayane coordinates the continuation toward Hoshino from branch controls, but direct contact/reconciliation with Hoshino has not occurred (scene:003). Their cooperation is a present event, not proof the long-term Hoshino solo pattern has changed.

## V001 C003 E023 backfill relationship delta

Hoshino and Suou directly confront one another at the Valley gun. Hoshino rejects a long origin explanation, asks why Suou summoned her and persists in a Yume-framed destruction plan (scene:001:u:0032-0044). Suou says Hoshino was her true target, frames years of shifting affiliations as a path toward this fight, and offers a notebook-location clue if beaten (u:0049-0058). This is Suou's self-account and deliberate challenge, not proof of her employment history or notebook control. Nonomi remains connected through the gold card Suou holds; the dialogue at u:0010-0012 does not prove Nonomi physically at the Valley. Battle begins only as a declared intent, with outcome unshown (u:0059-0061).

## V001 C003 E024 backfill relationship delta

Hoshino wants Suou moved aside before younger peers arrive; Suou resists, so their fight remains active (scene:001:u:0001-0008). The Abydos/Sensei group actually arrives, sees the gun and then runs toward Hoshino gunfire, making their E022 pursuit concrete but not yet reuniting them (u:0018-0041,0059-0064). Arona expresses worry over Plana's exhaustion and pain; Plana wakes to report being watched, an uncertain external threat rather than a diagnosed condition (u:0042-0058). The students' group response does not yet change Hoshino's stated solitary plan.

## V001 C003 E025 backfill relationship delta

Hoshino gains the apparent upper hand against Suou and asks about prior connection/notebook, receiving evasion and a retracted clue (scene:001:u:0001-0018). Serika welcomes Hoshino back, while Sensei, Nonomi, Serika, Shiroko and Ayane reach her to oppose the planned solo destruction (u:0022-0037; choice:001). Nonomi explicitly compares Hoshino's unilateral school exit to the former pattern. Ayane threatens capture if talk fails and asserts her president address to Hoshino; no fight with peers or consent to return has occurred (u:0035-0044). This is direct contact, not reconciliation.

## V001 C003 E026 backfill relationship delta

Hoshino's force leaves Ayane, Nonomi, Serika and Shiroko exhausted, and she asks Shiroko to stop after the group failed (scene:001:u:0001-0014). Shiroko refuses and frames a personal contest as the condition for listening to Hoshino; this is direct attachment conflict, not reconciliation or durable separation (u:0012-0018). Sensei is present in inward reaction only, with no printed mediation. Card/gun custody and group membership remain unresolved.

## V001 C003 E027 backfill relationship delta

Shiroko credits Sensei in her strength, Nonomi admits guilt projected onto Hoshino, and Shiroko/Serika/Ayane ask for Hoshino's story and shared responsibility (scene:001:u:0001-0039). Hoshino discloses grief and briefly accepts the return invitation, including Ayane's presidency and affectionate address (u:0040-0062). Suou's threat and Dweller interruption make her leave again; she thanks peers but calls suffering her own (u:0063-0088). Sensei requests a relevant helper; the later Hina encounter strongly links her to that unnamed response, and Hina directly resists Hoshino's plan (u:0155-0186). None is durable reconciliation or a completed fight result.

## V001 C003 E028 backfill relationship delta

Hina directly opposes Hoshino, predicts her opening search and intercepts again after Hoshino thinks she escaped (scene:001:u:0002-0023). This is protective force in service of stopping a risky solo plan, but Hoshino does not consent and the encounter has no outcome. Sensei and Abydos peers are absent from printed action here; the prior help request remains contextual, not a shown real-time command to Hina. No relationship reconciliation or custody transition is evidenced.

## V001 C003 E029 backfill relationship delta

Hoshino tries to exclude Hina as an unrelated outsider, while Hina insists she is connected and refuses to give up. Hoshino guesses Sensei's request but receives no answer in this exchange (scene:001:u:0005-0013). Both are visibly winded on the train; Hoshino plans to push Hina off to end pursuit, but no fall or injury occurs in print (u:0015-0025). Their opposition persists without a mediated conversation or consent to return.

## V001 C003 E030 backfill relationship delta

Historical Hoshino lashes out at Yume, intends to return and finds her absent with a grateful farewell-like memo and broken message. Hoshino then repeatedly questions Yume's errand and blames her own words, despite no demonstrated fatal causal chain (scene:001:u:0001-0045). Present Hoshino remembers a shared Yume visit near Great Oasis and still prioritizes gun destruction over checking Hina after their reported fall (u:0046-0058). Hina reappears and names Yume, opening a new conversation whose content is deferred (u:0059-0066).

## V001 C003 E031 backfill relationship delta

Hina stops Hoshino physically, explains Sensei asked her, and brings her own investigated Yume/Thunder Emperor stake to the conversation (scene:001:u:0001-0045). She praises Hoshino's staying/protection despite opposing her solo plan; Hoshino begins reconsidering what she protects (u:0046-0055). An earlier Black Suit offer would have removed Hoshino from Abydos for debt relief, but she refuses (u:0056-0075). Hikari/Nozomi and Abydos/Sensei reappear together to intercept the gun; how the twins rejoined is not printed (u:0076-0093). No durable Hoshino consent or gun resolution yet.

## V001 C003 E032 backfill relationship delta

Hina keeps Hoshino down and tries to reason that Sensei/group can solve the gun threat; Hoshino instead fixates on Yume's irreversibility and lost words (scene:001:u:0001-0025). Dweller's unseen replies draw Hoshino into counterfactual isolation while Hina wonders whom she addresses (u:0026-0041). Suou is down after the group's intervention and the twins speak to her, but her later recovery/custody remain unknown (u:0086-0088). Sensei/peers see a new disturbance and worry about Hoshino/Hina, without contact established at cut (u:0081-0093).

## V001 C003 E033 backfill relationship delta

Peers and Sensei call to altered Hoshino, who still murmurs Yume/notebook; Hina says she could not stop the change (scene:001:u:0031-0048). Arona/Plana worry for Sensei and Hoshino; Sensei inwardly rejects Hoshino's halo destruction (u:0049-0078). Shiroko vows to save Ayane, Serika, Nonomi, Hoshino and Sensei, but frames herself as the only possible actor (u:0079-0089). Sensei then loses consciousness and an unidentified soft voice calls him, with no confirmed contact/recovery (u:0090-0100). Relationship intent is direct; outcomes remain open.

## V001 C003 E034 backfill relationship delta

Sensei encounters a Yume-labeled supportive voice in a likely vision and resolves to help a reachable child; that relation is an experience, not a historical Sensei/Yume acquaintance (scene:001:u:0001-0033). He meets Dweller directly and contests the game-end claim (u:0034-0040). Two Shirokos appear to interact as counterparts, one affirming the other's strength and offering help for Hoshino; exact individual tags are unreliable (u:0041-0054). Hoshino says others cannot understand her suffering, while a Shiroko voice says she does and offers combat; no reconciliation follows yet (u:0055-0064).

## V001 C003 E035 backfill relationship delta

Plana warns other-time-axis Shiroko that local Shiroko summoned Color; the counterpart responds and accepts responsibility for helping, while Ayane/Nonomi/Serika recognize her arrival (scene:001:u:0001-0027). The counterpart meets altered Hoshino's assertion of inaccessible suffering with recognition, creating a possible point of contact but no restoration yet (scene:002:u:0001-0003). Sensei's inward plea for Shiroko to stop is repeated; his medical state is not updated. The Dweller's Set plan stalls, but his antagonism continues (u:0004-0020).

## V001 C003 E036 backfill relationship delta

Local/counterpart Shiroko disagree about Hoshino's halo and whether prior resolve equals current wish. Both attend to the notebook-like form and possible remaining Hoshino anchor (scene:001:u:0001-0042). Plana asks Arona to hold her hand during a feared sleep/resource sacrifice; Arona pledges to wait, while Plana asks concealment from Sensei, leaving an ethical information gap (u:0043-0067). Hina returns to aid the group, and Sensei's failed reach hands communication to Committee/counterpart. A Shiroko includes the other as Abydos in familiar banter (u:0068-0084; scene:002). No Hoshino response yet.

## V001 C003 E037 backfill relationship delta

Nonomi, local Shiroko, Ayane and Serika reach Hoshino with differentiated appeals: unexpressed Yume feelings, accident/rescue memory, concern for self-punishment, and an ordinary return invitation (scene:001:u:0001-0052). Counterpart Shiroko proposes carrying Yume memory forward; Hoshino recognizes her own kept-weapons grief, and counterpart admits uncertainty about letting go (u:0053-0082). Sensei supports Hoshino's knowledge of Yume without claiming access to lost facts; Hoshino then encounters a Yume-labeled greeting in a notebook-like experience (u:0099-0119). Outcome and durable repair are not yet printed.

## V001 C003 E038 backfill relationship delta

Within the altered encounter Hoshino receives a Yume-labeled future letter that asks whether she cares for juniors and accepts friends' help; Hoshino cries and feels inadequate (scene:001:u:0001-0021). The Yume-like voice knows her efforts, comforts her and produces a laugh, then acknowledges her wish to meet while sending her back to protect juniors (u:0022-0049). This is meaningful inner contact but does not establish Yume physically returned or that Hoshino has rejoined peers externally. That relationship outcome awaits the next units.

## V001 C003 E039 backfill relationship delta

Hoshino's first external exchange after the altered contact names all four current Committee juniors, recognizes counterpart Shiroko separately, and addresses Hina personally before joining them against the threat (scene:001:u:0001-0009). This is observable relationship repair in action but does not prove durable recovery after crisis. Arona credits Plana's process discovery; the two OSs jointly support Sensei, while Plana interprets his message and Arona reacts to her sharpness (u:0024-0038,0070-0078). Sensei's adult duty extends concern to suffering children generally, with no battle outcome yet (u:0043-0052).

## V001 C003 E040 backfill relationship delta

Hoshino shows concern for Hina's ability to stand and quietly addresses a senior about finding treasure; the latter is plausibly Yume but remains an unlabelled addressee (scene:001:u:0003-0021). Current and counterpart Shiroko argue playfully about a gifted mask and competing nicknames; Serika and Ayane mediate the shared-name confusion (u:0035-0044). Hoshino's familiar response to the messy group scene adds ordinary-company evidence following E039's explicit cooperative greeting (u:0045-0049). No durable reconciliation or counterpart departure is shown.

## V001 C003 E041 backfill relationship delta

Nonomi handles everyone's laundry; Hoshino sleeps against Hina until Sensei helps wake her; Hina leaves after the group thanks her and promises later gun investigation (scene:001:u:0034-0103). At the regular meeting Hoshino apologizes to juniors/Sensei, they affirm her return and ask her someday to tell them about Yume (u:0104-0158). In private exchange Hoshino names persistent regret and gratitude for current friends and counterpart Shiroko, then says holding loss need not block grasping offered hands (u:0159-0176). Counterpart Shiroko spares Dweller and disconnects from Plana/Arona; future relationship status is open (u:0177-0212).

## V001 C003 E042 backfill relationship delta

Ayane notices Hoshino accepts the presidency while local Shiroko and Serika argue over an unsuccessful oasis dig; the swimsuit-order joke shows ordinary friction within a functioning Committee (scene:001:u:0008-0029). Makoto and Hina jointly handle the legacy despite Ayane's expectation of hostility, with private reconciliation unknown (u:0030-0037). Suou works among Highlander/Nephthys staff but her inner shift remains silent (u:0051-0068). Ayane, Hoshino, Serika and Sensei lack counterpart Shiroko's location and hope to thank her on return; this is a continuing bond without contact (u:0079-0086; choice:001).

## V001 C003 E043 backfill relationship delta

Serika serves at the Master’s busy restaurant, and the Committee responds to local Shiroko chasing theft; Sensei follows her (scene:001:u:0001-0032). He meets counterpart Shiroko, asks about shelter/food, offers ramen without pressing when she declines, and does not demand her trauma account (u:0033-0048). He gives a smartphone and invites future contact; she agrees but no call is printed (u:0065-0074). She later joins local Shiroko, Hoshino and Committee for a Binah approach, saying `今回だけ`; co-presence and action are observed, durable membership is not (u:0078-0113).

## Phase 2 cycle 001 contextual delta — 2026-10-01

[Accepted cycle and exact admission](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md). Witness a038020f, generation BA_REFRESH_20260928T032248159554Z; all 34 objects completely inspected. Main480 remains unchanged. Internal relative sequence only; no cross-source timeline, performed voice or prospective test.

| Direction / packet | Accepted relation and contrary case | Exact routes |
|---|---|---|
| Abydos peers→Ayane / Ayane→peers | Genuine worry/health concern and intent to help meet terse incomplete reporting, wrong work and additional liability. Ayane wants competent work and a pleasant return; strict summons exempts Serika without proving total innocence. Prepared hospitality is not an observed consumed welcome. | GROUP2101–2102 §§3–8;2102 scene001 u0010;scene002 u0014/u0015/u0053 labels limited. |
| Yuuka→C&C | Accounting complaint, admission of reliance, polite civic request, gratitude and profit-led expansion coexist; proposal of permanent conversion meets Neru's refusal. | GROUP1201 u0047–0080;1202 scene002 u0010–0047;1203 u0051–0088. |
| C&C peers→Neru | Asuna's delegated commitment precedes the leader's objection; contract pressure does not erase it. Akane's styling care respects the jacket limit; Karin enjoys service and frames prior commitment. | GROUP1202 scene002 u0049–0086;1203 u0001–0028/u0043–0050. |
| Maki→Hare/Kotama;Chihiro→members;Yuuka↔printed Eimi | Recruitment uses different peer interests; vice-president rejects prestige consolation for other people's privacy. Office cooperation and false-record reactions are observed; no full interinstitutional repair. | GROUP1501 u0028–0043;1502 scene001/003;1503 scene001 u0022–0042. |
| Kazusa→Reisa | Explicit aversion and label refusal coexist with initiated concern and aid; no secret-friendship or romance title is imposed by the analysis. | EVENT816 E003 u0030;E009 u0026–0033;E012 u0031–0046;E013 u0025–0029;E015 u0041–0046. |
| Reisa→Kazusa/Sensei/Suzumi | Familiar rival mythology changes under trusted correction and a heard boundary; protective withdrawal carries explicit reunion happiness and sadness, privately entrusted to Sensei. E017 counters permanent cessation. Suzumi's support coexists with a nickname limit. | EVENT816 E005/E010;E011 u0011–0032 (u0027 confidentiality);E014 u0011–0022;E017 u0025–0047. |
| Club→Kazusa;Kazusa→Sensei | Belonging is affirmed before disclosure, but copying the old identity is intrusive; Yoshimi restores listening yet enjoys teasing. Adult help includes photograph loss, critique and later ease. | EVENT816 E006 u0046–0073;E009 u0016–0033;E015 u0022–0026;E016 u0002–0014. |
| Nine gift dyads | Each giver has a distinct craft/preference and reception; the counterpart-like Shiroko visitor reassures the adult. Seia's attention trap, Satsuki's stated recruitment and Kisaki's undisclosed addition preserve information limits. No universal affection or blanket consent follows. | EVENT80000 E117–125 complete readings;E119 u0027–0042;E124 receipt/room-law sequence;E125 u0056–0079. |

The exact object crosswalk, packet readings and cycle checkpoint preserve all branch, label and identity warnings. Ordinary pleasure is affirmative evidence; it does not substitute for unprinted outcomes. No new durable claim/rule ID or standalone model is created.

## Phase 2 cycle 002 contextual delta — 2026-10-01

[Exact35-object acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_002_CHECKPOINT.md); pinned a038020f witness.17 scenes,893 structured utterances,102 choices,177 full-thread messages,3 profiles and229 written records (228 nonempty). Main480 and all historical knowledge boundaries remain unchanged.

| Direction | Accepted relation | Witness / limit |
|---|---|---|
| Serika → Sensei | Requesting, protecting, fairly compensating, choosing closeness, thanking, offering reciprocal ramen, demanding privacy and later withdrawing a gift. Inward wishes are not shared knowledge. | [Serika §§1–5](../02%20Sequential%20Readings/BOND/SERIKA/BLUE_ARCHIVE_SERIKA_PRIVATE_CONTEXTUALIZATION_CHECKPOINT.md); Momo130080170 Answers266/267 are alternate nonviewing/deletion claims; no verified privacy check. |
| Sensei → Serika | Useful labor, collapse support and repair network coexist with inaccurate instruction, visit/gaze ambiguity, unnecessary pulling, exceeded speed request, an unfulfilled reciprocal turn and unwanted childish praise. | [Serika §§1–5](../02%20Sequential%20Readings/BOND/SERIKA/BLUE_ARCHIVE_SERIKA_PRIVATE_CONTEXTUALIZATION_CHECKPOINT.md); swim003 narrated inaudibility limits intentional-disregard claims for later speech, without canceling the prior request. |
| Serika → visitors / repairer → Serika | Actual lost-child reunion, courteous audience adaptation, elder/customer guidance, guilt and refusal of full specialization; actual bag repair acknowledges valued ownership. | NewYear003 u0029–0071; base020 u0037–0081. Healing and later durability are claims, not established outcomes. |
| Gourmet → Izumi / Fuuka; Hina → Sensei | Unreliable care, teasing, valued shared pleasure and aid without effective recipient control; custody apology followed by another prejudgment. | [Gourmet §§3–12](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1101_1104_DEEP_READING.md); no timeless friendship verdict, blanket permission or resolved final accusation. |

No new durable claim/rule ID, model artifact, held-out test or forecast. Ordinary pleasure is affirmative evidence. Source/branch/chronology/identity and outcome limits remain in the linked complete readings.

## Phase 2 cycle 003 contextual delta — 2026-10-01

[31 complete group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_003_CHECKPOINT.md) at the pinned a038020f witness. Ordinary tastes, chosen leisure, work, belonging, pleasure and objections have affirmative standing. Every effect is contextual and source-specific; no unproved main chronology or readiness promotion follows.

| Complete packet | Accepted scoped contribution | Canonical argument |
|---|---|---|
| GROUP1301–1303 | Cherino→Marina demands/perks/threat and rejection; Marina→Cherino constrained fabrication plus ambition; Tomoe→Cherino public validation/care; Tomoe→Marina code warning; Marina→Nodoka benefit promise, insult, targeted coercion; Nodoka→Marina refusal and later revolution invitation. No free costume consent or universal leader devotion. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1301_1303_DEEP_READING.md) |
| GROUP1401–1403 | Engineering peers' mutually enjoyed project; Utaha→juniors calming/delegation; engineers→Nel concealed property error plus actual help; Nel→engineers thanks then suspicion/demand/retaliation; Momoi→Nel liability claim and engineers→Momoi promised repair; Asuna→Nel personal-style question and Nel→Asuna stated boundary. Do not infer universally altruistic help or total bad faith. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1401_1403_DEEP_READING.md) |
| GROUP1601–1602 | Fuuka→Izumi meal boundary; Izumi→Lunch Club participation without membership; Juri→Fuuka reassurance/help, Fuuka→Juri questioning harmful work; Iori→club intimidating then favorable then revised evaluation; Juri→Iori praise/welcome and mistaken sleep account; Fuuka→Iori warning and later concealment idea. No lasting enmity or complete mutual repair shown. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1601_1602_DEEP_READING.md) |
| GROUP1701–1703 | Patients→nurses comfort/envy/praise and later complaint; Serina/Hanae→patients differentiated aid and boundaries. Hanae→Serina inquiry pressure; Serina→Hanae quiet and timely-warning corrections. Students→intruder force, conditional help, betrayal response and offered care; intruder→students fear/deception/apology. No all-recipient satisfaction or enduring reconciliation. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1701_1703_DEEP_READING.md) |
| GROUP1801–1802 | Hasumi→Tsurugi worry/relief, Mashiro→peers practical support and recipient perspective, Nagisa→committee imposed exchange. Literature students→Mashiro curiosity; tea guests→Hasumi praise then fear; sweets peers→Tsurugi anxious/limited approach; Tsurugi→sweets reported pleasure/welcome. Do not collapse directed experiences into mutual comfort. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1801_1802_DEEP_READING.md) |
| GROUP1901–1902 | Ako→Hina report/encouragement and Hina→Ako bounded scheduling; Makoto→Ako/Prefects preselected subordination; Iroha→Makoto reluctant execution, Iroha→Ibuki concern/protection, Ibuki→senior cheerful effort; Prefects→Iroha protests and Iroha→Prefects role/personal justification. Haruna→debating Prefects pleasure is distinct from Fuuka→captors unshared rescue wish. No final reconciliation. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_1901_1902_DEEP_READING.md) |
| GROUP2001–2002 | Airi→peers companionship/feeding/help; Yoshimi→Kazusa teasing after refusal; Kazusa→Yoshimi requests to stop; peers→Natsu refusal followed by rescue; Natsu→peers persuasion and later plea. Cite `2001:u0032,u0036–u0047,u0060–u0079;2002:u0050–u0078,u0105–u0109`. Preserve directed asymmetries and rescue cost; no universal boundary-respecting friendship. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2001_2002_DEEP_READING.md) |
| GROUP2201 | Aru→team offers hopeful opportunity, then commands; Haruka→Aru praises/complies; Kayoko→Aru cautions; Mutsuki→Aru teases and joins retaliation. Reported recommending acquaintance→Aru exclusivity claim `u0028` is not a globally joined relationship or proven historic trust network. No JTF–PS68 encounter is completed. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2201_DEEP_READING.md) |
| GROUP2301–2302 | Pina→guests admits/help; Shizuko→guests first objects, then explicitly invites; Mimori→Shizuko apologizes/offers lunch; committee→Umika welcomes, critiques specific ideas and promises shared work. `2301:u0030–u0055;2302:u0013–u0022,u0119–u0136`. Critique and encouragement coexist; no universal consent from mere hospitality. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2301_2302_DEEP_READING.md) |
| GROUP2401–2402 | Kaede admires/emulates distinct seniors; Mimori provides food/encouragement, then objects to alteration; Tsubaki objects to diverted animals. Sensei offers bounded creative guidance and does not cancel peer accountability `2401:choice007;2402:u0085–u0093,choice003`. No imagined praise as observed reciprocity, no universal withdrawal of teacher help. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2401_2402_DEEP_READING.md) |
| GROUP2403–2404 | Prior opted-out patrol, renewed loneliness, apologies and conditional reinvitation coexist `2404:u0104–u0124`. Seniors protect Kaede from actual threats; Shizuko gives practical care, Kaede chooses tailing instead of asking; Sensei accompanies but student peers effect protection. No permanent refusal, automatic acceptance or sole-teacher rescue. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2403_2404_DEEP_READING.md) |
| GROUP2501–2502 | Momoi pressures Yuzu then accepts nonintervention; Yuzu later volunteers and seeks apology to Momoi. Friends praise but do not fully heed request for crowd help. Opponent makes conditional apology then delivers it; fan requests impose stress. `2501:u0059–u0069;2502:u0072–u0107`. No universal consent from joining a party or from handle disclosure. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2501_2502_DEEP_READING.md) |
| GROUP2601–2602 | Rumi→Kokona correction/accommodation and misleading instruction; Rumi→Shun stated customer confidentiality; Kokona→Shun service plus breach; Shun→Kokona thanks then reprimand; Sensei→Shun listening/disclosure with uncertainty. Preserve children→peers rumor relay and original privacy request; no secrecy as permission to frighten or sexual allegation as fact. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_2601_2602_DEEP_READING.md) |
| GROUP3101–3103 | Add directed Yuuka→Noa dependence/gratitude/demand and Noa→Yuuka affection/help/selective disclosure; Himari→Chihiro nickname/defense and Chihiro→Himari practical care/correction. Yuuka→Himari is reliance on design prestige without a shown direct solicitation. Sensei relationship teasing at `3103 u:0021-0024` is voice-limited and one-sided; no mutual adult/student state transition. | [Full argument and exact locators](../02%20Sequential%20Readings/GROUP/BLUE_ARCHIVE_GROUP_3101_3103_DEEP_READING.md) |

All previous main and cycle001–002 entries retain their dated information boundary. These complete outcomes were already exposed: `NO_DIAGNOSTIC_OPPORTUNITY`. BA-C005/C006 rejected dispositions remain; comparisons qualify situated claims rather than introducing a new universal law or frozen forecast.
