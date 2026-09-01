---
title: "Gakuen Idolmaster V2 - Institution and Idol-System Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.5"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-08-24 - Phase 6 side-character synthesis institutional routing integrated"
status: "active; cumulative through Phase 6 side-character synthesis"
---

# INSTITUTION AND IDOL-SYSTEM LEDGER

| system ID | English label | Japanese | scope | explicit rule/fact | continuity role |
| --- | --- | --- | --- | --- | --- |
| `INST-HATSU` | regular performance | `初` | `P1` | intermediate/final exams gate participation | first Produce objective |
| `INST-NIA` | NEXT IDOL AUDITION | `N.I.A.` | `P2` | multi-school fan-vote competition | follows successful P1 state |
| `INST-FINALE` | N.I.A. final | `FINALE` | `P2` | top three enter public final; winner performs victory live | N.I.A. endpoint |
| `INST-HIF-OLD` | old-rules summer H.I.F. | `H.I.F.` | `U1/D summer` | separate solo/unit structures | precedes winter reform at rule level |
| `INST-HIF-REFORM` | reformed winter H.I.F. | `H.I.F.` | `P3/D 028-037` | solo/unit division abolished; stricter selection | later regime |
| `INST-HIF-SEL` | winter Selection | `選抜試験 / セレクション` | `P3` | three exams; higher cutoff | qualification for main tournament |
| `INST-HIF-ROUNDS` | prescribed/free rounds | `課題曲 / 自由曲` | `P3 final` | same-song differentiation plus idol-suited free song; aggregate score | final structure |
| `INST-PRIMA` | Prima Stella | `プリマステラ / 一番星` | `all H.I.F. tracks` | title awarded according to route/era rules | champion-state anchor; always scoped |
| `INST-PRODUCER-EVAL` | Producer evaluation | `積み重ねてきたプロデュース` | `P3 final` | accumulated production is tested | culmination of partnership |
| `INST-U1-CHAMP` | U1 summer champion | `花海咲季` | `U1` | Saki wins after Re;IRIS unit victory | track endpoint |
| `INST-DSAKI-CHAMP` | Saki Dear summer champion | `花海佑芽` | `D-SAKI` | Ume wins summer H.I.F. | incumbent for Saki winter route |
| `INST-P3C-INC` | common winter incumbent | `十王星南` | `P3-C` | Sena is current Prima Stella/top idol | incumbent for common routes |
| `INST-REV` | REVERSI winner structure | `REVERSI` | `P3-REV` | unit wins but one member receives singular Prima Stella | route-specific awardee |
| `INST-HATSUBOSHI-REQUEST` | Hatsuboshi Request System | `初星依頼制度` | `floating institutional` | industry work allocated via internal auditions; compensated | C0 system/C2 date |


## Title-scope rule

Prima Stella is a singular title inside a ceremony/track. The corpus authenticates different holders in different routes; the ledger never constructs one unsupported universal succession.


## Phase 2 additions — shared narrative and institutional spine

| system ID | English label | Japanese | scope | explicit rule/fact | primary evidence | continuity role |
| --- | --- | --- | --- | --- | --- | --- |
| `INST-P-COURSE` | Producer Course dual status | `プロデューサー科` | `G-INST` | the Producer is simultaneously a Hatsuboshi student and an institutionally recognized Producer | `LOC-INST-001` | fixed institutional premise; separates producer function from credentialed status |
| `INST-P-BASE` | Producer activity base | `活動拠点` | `U1` | a P-course student receives a classroom as an operational base | `LOC-INST-002` | C0 within U1; evidence of school-provided production infrastructure |
| `INST-CLASS-CELL` | class as production cell | `クラス / アイドル事務所` | `E-001`, school culture | the class can function like an agency and a cooperative bloc in interclass competition | `LOC-INST-003`, `LOC-INST-004` | C1 internally/C2 globally; social-organizational layer |
| `INST-UNIT-ROLE-FLEX` | differentiated unit roles | `センター / リーダー` | `U1` | center may vary by song; leadership may be allocated by trust and coordination rather than stage prominence | `LOC-INST-009`, `LOC-INST-010` | C1 within U1; separates performance role, leadership, and production authority |
| `INST-PUBLIC-RESULT-RECORD` | disclosed performance record | `履歴書に記載 / 学内外に開示` | old-rules H.I.F./Selection | Selection results become durable public/professional records | `LOC-INST-008` | C0 within U1 institutional regime; creates opportunity and stigma risk |
| `INST-P-CURRICULUM` | Producer technical and strategic curriculum | `プロデュース / 勝ち筋 / サポート` | `P3` shared Produce Events | Producers study performance technique, opponent/event tendencies, strategy, repertoire fit, and complete support | `LOC-INST-018`, `LOC-INST-019` | C3 lesson branches collectively establish curriculum range, not one additive classroom biography |
| `INST-P-CARE-COMPETENCY` | embodied care as production skill | `ケガや不調を見抜く / 栄養 / ストレス` | `P3` shared Produce Events | throat, injury, fatigue, nutrition, stress, and presentation management are treated as trainable Producer knowledge | `LOC-INST-021`, `LOC-INST-022` | institutional ideal; later ethical analysis must test care/control boundary |
| `INST-PAID-WORK-ALLOCATION` | paid work allocation | `初星依頼制度 / 学内オーディション / 報酬` | floating institutional | Hatsuboshi receives industry requests and allocates compensated work through internal auditions | `LOC-INST-023` | C0 system/C2 date; school acts as labor intermediary and opportunity gatekeeper |
| `INST-STUDENT-COUNCIL-AGENCY` | student-council pseudo-agency | `疑似的なアイドル事務所` | `E-005` | Sena uses student government to recruit and develop possible top idols and successors | `LOC-INST-024`, `LOC-INST-026` | C1 within event/C2 globally; exceptional institutional experiment |
| `INST-P-CREDENTIAL-BOUNDARY` | restricted non-P-course Producer authority | `契約で縛れない / 小さな権限` | `E-005` | an idol may perform producer-like functions without receiving full P-course powers, benefits, or facility access | `LOC-INST-025` | defines credentialed authority by exception |
| `INST-100PRO-NETWORK` | school–industry network | `100プロ` | `P3` | a major professional agency is heavily involved in winter H.I.F.; exact role is not specified | `LOC-INST-027` | C0/C1 within P3 institutional state; do not infer sponsorship, judging control, or contracts |
| `INST-IDOL-STRENGTHENING` | comparative Producer–idol development program | `アイドル強化月間` | floating event system | Producers are compared through how brightly they develop their idols | `LOC-INST-028` | C0 system/C2 date; reinforces Producer accountability |
| `INST-AUDIENCE-ECOSYSTEM` | public and labor ecology of performance | `ファン / お客さん / 開催に携わった方々` | `E-003`, `U1` | performance is addressed to concrete audiences and depends on organizers, workers, and surrounding community | `LOC-INST-029`, `LOC-INST-030` | C1 internally/C2 globally; limits purely ranking-centered interpretation |
| `INST-PRIMA-SCARCITY` | singular title after collective work | `一番星は、あくまでひとり` | old and reformed H.I.F. | unit victory/cooperation does not eliminate singular final recognition | `LOC-INST-011`, `LOC-INST-012`, `LOC-INST-017` | structural tension between cooperative formation and individual scarcity |
| `INST-PLURAL-MERIT` | plural standards of idol excellence | `技術 / 表現 / 個性 / 数値では計れない力` | shared institutional pedagogy | Hatsuboshi recognizes technique, accuracy, affect, individuality, audience connection, adaptability, and charisma | `LOC-INST-019`, `LOC-INST-020` | evaluative ontology; does not imply consistent or fair application |
| `INST-MATERIAL-ACCESS` | economic support and unequal developmental time | `学費 / バイト / 支援` | `U1` and character-dependent | material conditions can determine sleep, lesson time, and ability to pursue idol work | `LOC-INST-031` | C1 within U1/C4 outside; character-specific distribution requires later passes |
| `INST-TEACHER-CONTINUITY` | continuing pedagogical relation | `先生` | `P3` shared lesson branch | Asari frames herself as the Producer's teacher even after the Producer advances beyond school stages | `LOC-INST-032` | institutional continuity beyond any one title result |

## Phase 2 institutional synthesis rule

The cumulative evidence supports treating Hatsuboshi as a **hybrid developmental institution**: school, production incubator, competitive sorting mechanism, labor intermediary, public venue, and industry pipeline. This is an analytical synthesis, not an in-world legal classification. Later phases must test who benefits, who is sorted out, and whether the institution's corrective mechanisms work consistently.

## Phase 3 — Saki as an institutional test case

| evidence ID | institutional proposition | Saki sources | continuity scope | pressure / qualification | status |
| --- | --- | --- | --- | --- | --- |
| INST-SAKI-001 | Producer selection can target feared future potential rather than current completion | `adv_dear_hski_001–003` | D/P1-SAKI | creates deep trust but concentrates interpretive authority in the Producer | high |
| INST-SAKI-002 | idol development can require redesign of an already optimized athletic body | P1 `after-step-1-normal-01..03` | P1 conditional | body care and self-instrumentalization are difficult to separate | high |
| INST-SAKI-003 | N.I.A. makes popularity and fan cultivation part of competitive capacity | P2; `dear 013–020` | P2/D-SAKI | fan relation can become circular access and instrumental muscle | high |
| INST-SAKI-004 | reformed H.I.F. tests individuality through common prescribed material and self-selected free material | P3/D-SAKI; `dear 029–036`; `cidol 018–019` | P3-SAKI | technical fairness depends on judging consistency and access to specialized collaborators | high on rule; fairness open |
| INST-SAKI-005 | Project Stardust shows elite development as a network of experts, rivals, family, and Producer resources | `dear 024–035`; supplemental Training Center source | D-SAKI | Saki is not a resource-poor underdog; institution and family compound advantage | high |
| INST-SAKI-006 | the title system can turn succession into an active public challenge rather than terminal closure | `dear 036–037`; U1 | D-SAKI/U1 separately | still preserves singular scarcity and leader hierarchy | high, track-scoped |
| INST-SAKI-007 | Hatsuboshi can make a durable shared field that prevents Saki from escaping Ume by changing disciplines | D-SAKI at academy; H.I.F. structure | D-SAKI | family relation, not the institution alone, supplies the motive | strong inference |
| INST-SAKI-008 | institutional support does not equal psychological security | complete Saki core | cross-track | elite resources coexist with plateau anxiety and identity collapse | high bounded observation |

## Phase 3 — Kotone institutional/labor update

| institution/process | Kotone evidence | implication | open question |
| --- | --- | --- | --- |
| Hatsuboshi tuition + student labor | early debt/overwork route | access to elite training can itself produce financial pressure that degrades measured performance | what scholarships/formal support were institutionally available before Producer intervention? |
| producer curriculum | rest/work substitution, debt/budget navigation, performance coaching | “production” can extend into material-life case management | where should managerial authority stop? |
| N.I.A. public market | rankings, paid work, audience/fan mobility | popularity can create income and visibility while also forcing service labor | how often can students refuse market-fit work? |
| paid idol work | broad Produce Event work ecology | commercial work is developmental training and material support, not merely extraction | what labor protections/compensation norms apply? |
| H.I.F. ticket economy | Dear 024 | ticket price becomes explicit performance obligation in Kotone's ethics | does the institution encourage customer-service logic that can overburden performers? |
| succession | Sena → Kotone successor proposal | institution can tempt seniors to convert juniors into solutions for unfinished institutional problems | how does the school mediate succession without possession? |


## Paratext integration — Producer educational position and production rationale

| evidence ID | proposition | source class / claim type | evidence | bounded use | status |
| --- | --- | --- | --- | --- | --- |
| `INST-P-LEVEL-001` | GakumasP is a first-year Producer Course student | `S1 / A` | `LOC-INST-033`, `LOC-INST-034`, `LOC-INST-035` | fixes first-year/course status; does not alone specify formal post-secondary institution name | canonical narrative fact |
| `INST-IDOL-LEVEL-001` | principal idol education is separately described through `中等部` / `高等部` | `S1 / A` | `LOC-INST-036`, `LOC-INST-037` | rejects same-level-classmate flattening | canonical narrative fact |
| `INST-P-COURSE-S2` | `プロデューサー科` is formal first-party setting terminology with its own curriculum | `S2 / B` | `PARA-S2-001`, `PARA-S2-002` | formal course terminology | canonical setting metadata |
| `INST-P-SPECIALIZED-UNIV` | creator taxonomy places GakumasP in `初星学園専門大学のプロデューサー科` | `S3 / C` + `S4 / D` corroboration | `PARA-S3-001`, `PARA-S4-001` | use as creator-stated/formally reported taxonomy; S2 exact compound not independently recovered in current audit | strong, source-labeled |
| `INST-P-DISTANCE-DESIGN` | teacher and same-level classmate models were rejected to balance physical closeness with professional/psychological distance | `S3 / C` | `PARA-S3-001`, `PARA-S3-002` | explains design intent; does not dictate every relationship reading | strong creator rationale |
| `INST-P-PIPELINE-ORIGIN` | Producer Course was conceived as a training pipeline responding to producer labor demand associated with Idol Course graduates/100pro | `S3 / C` | `PARA-S3-003` | production-history/worldbuilding rationale; do not infer unstated contracts or universal employment outcomes | strong creator rationale |
| `INST-P-LIMINALITY` | Producer occupies structured liminality: student + credentialed authority + object of ongoing evaluation | `E` | synthesis of rows above + existing Phase 2 S1 | analytical model only | high-confidence inference |

### Source-boundary rule

`初星学園専門大学` must not be silently presented as if it were recovered verbatim from the frozen ADV corpus. The current audit directly recovers `プロデューサー科`, first-year status, `大学`, and `中等部/高等部` distinctions from S1; the full specialized-university compound is creator-stated in S3 and corroborated by launch reporting.


## Phase 3 — Mao as an institutional test case

| evidence ID | institutional proposition | Mao sources | continuity scope | pressure / qualification | status |
| --- | --- | --- | --- | --- | --- |
| `INST-MAO-001` | institutional training can reopen categories that prior professional/adult gatekeepers treated as mutually exclusive | Dear 001–010; P1 | D/P1-MAO | reconstruction is substantially Producer-directed; not proof Hatsuboshi always supports plural identity | high bounded observation |
| `INST-MAO-002` | Producer authority includes aesthetic diagnosis as well as schedule/technical management | Dear 003–009; P1/pevents | D/P-MAO | accurate care can still be interpretive control | high |
| `INST-MAO-003` | dorm seniority functions as a care-transmission structure | cidol 009; Dear 032; U1 | modular/U1/D-MAO | care can become over-responsibility and hide the senior's own needs | high |
| `INST-MAO-004` | N.I.A. can force school hierarchy into market-horizontal rivalry | Dear 012; P2 | D/P2-MAO | senior/junior asymmetry does not disappear automatically | high |
| `INST-MAO-005` | 100Pro exposes a credential/resource boundary between student production and professional-agency production | Dear 021–026 | D-MAO | external agency has legitimate expertise/resources; conflict is not school-good/industry-bad | very high |
| `INST-MAO-006` | P-course formation can become part of a producer's professional pathway rather than merely an in-school role | Dear 022, 024–026, 037 | D-MAO | route-specific 100Pro outcome; do not universalize graduate placement | high within D-MAO |
| `INST-MAO-007` | shared institutional repertoire can operate as intergenerational pedagogy | cidol 007 `Campus mode!!` | C-MAO | modular story; Mao's inheritance reading is personal, not universal song doctrine | high textually |
| `INST-MAO-008` | singular title can be personally reauthored as generative visibility | Dear 036 | D-MAO | Mao's Prima Stella ethic does not abolish title scarcity or prove institutional benevolence | high as Mao ethic |

## Phase 3 Lilja institutional deltas

| topic | source | finding | classification |
| --- | --- | --- | --- |
| novice pedagogy | Dear 001-009; P1 | institution/Producer can make an initially weak performer legible through structured incremental training rather than only elite selection | S1/A |
| effort governance | Dear 013-016; pevent school_004 | body/rest regulation is part of Producer responsibility; hard work is not institutionally treated as self-justifying | S1/A |
| differentiated pedagogy | Dear 024-025 | Shion's logic-first, one-variable-at-a-time teaching demonstrates that pedagogy can be matched to learner cognition rather than intuitive talent | S1/A |
| talent taxonomy | Dear 024-026 | school-salient technical skill, persistence, visual charisma, and audience transmissiveness are separable dimensions | S1/A + analysis |
| H.I.F. narrative framing | Dear 029-030 | relationship history/public streaming can shape human judges' interpretive predispositions even when popularity is formally non-scoring | S1/A; ethically open |
| migration support | pevent school_004; cidol005/018 | Producer care includes environmental/cultural/family-distance support for a student living in Japan for first time | S1/A |
| external work | sales pevents | cultural biography can become promotional labor resource and sales differentiation | S1/A |
| winter H.I.F. | Dear 035-036 | unified unit victory can coexist with singular individual Prima Stella selection | D-LILJA C1/C3 result |
## China institutional delta — support, privilege, and public legitimacy

| issue | evidence | current finding | status |
| --- | --- | --- | --- |
| inherited capital as idol resource | Dear 006, 011, 032 | Kuramoto name/money/appearance/upbringing are explicitly treated as usable resources; the text does not pretend background advantage disappears at school | canonical textual finding |
| abuse boundary | Dear 006, 011 | China rejects `濫用` and commanded affection/votes while accepting legitimate production support | canonical textual finding |
| `本来の実力` doctrine | Dear 020, 032 | Hatsuboshi figures explicitly include `己を支えるすべての力` within a debuted idol's effective ability | canonical **institutional doctrine**, not neutral analytical truth |
| distributive fairness | China versus resource-poor peers | support-as-ability can naturalize unequal access to capital, staff, media and production | OPEN analytical problem for Phase 8 |
| election legitimacy | Dear 021–027 | institutional succession is made contestable: Sena withholds overt installation and China accepts direct voter comparison | strong D-CHINA finding |
| leadership model | Dear 023–027 | China explicitly adopts a Liu-Bang-like model: governing by assembling stronger specialists rather than embodying every competence | strong route finding |
| horizontal redistribution | Dear 032 | China uses Kuramoto resources to strengthen Hiro's competitive performance as well as her own | strong but frequency untested |
| student/Producer hierarchy | Dear 002 onward + paratext correction | China calls GakumasP `先生`, but he remains a first-year Producer-Course student under the project's institutional model | relation-specific authority; not ordinary adult-manager model |
## Hiro institutional deltas — Phase 3

| issue | Hiro evidence | institutional implication | status |
| --- | --- | --- | --- |
| aptitude vs destiny | entry practical weakness + later HIF viability | Hatsuboshi does not treat poor initial fit as automatic exclusion | strong |
| body stewardship | special conditioning, weight/rest/flexibility management | idol production includes health/sustainability jurisdiction, not only stage craft | strong; ethics open |
| measurable ability vs charisma | Sena low current rating plus `スター性/カリスマ/オーラ/神格` | institutional evaluation recognizes an appeal dimension not reducible to technical scores | route doctrine; Phase 8 comparison needed |
| popularity -> responsibility | fans can respond before conventional skill catches up | audience recognition creates an obligation to develop rather than exemption from craft | strong |
| crisis as production technology | Producer deliberately engineers credible reputational/relationship stakes | school/Producer system can instrumentalize psychological pressure for performance | strong evidence; normative status OPEN |
| constructed persona | `owl` discussion + goddess/cute Hiro | production/styling can construct a truthful public artifact without simply mirroring private self | strong route doctrine |
| Prima Stella legitimacy | D-HIRO `瞬間最大風速` victory | title can ratify a peak relational/performance moment rather than stable superiority across every dimension | D-HIRO scoped; not universal institution rule |
| genius opportunity cost | father/Producer Dear 020 | institution competes with alternative elite life paths; chosen vocation need not maximize conventional human-capital efficiency | strong character-family debate |

## Phase 3 — Rinami institutional deltas

| issue | evidence | current institutional reading | normative/open pressure |
| --- | --- | --- | --- |
| market-fit production | Dear 001–005; P1 | institution/Producer can materially reshape how an existing student's relational qualities become market legible | production can recover capacity without proving the old form was false |
| produced naturalness | Dear 003; P1 | “natural” idol expression may itself require rehearsal, framing and selective elicitation | authenticity cannot be equated with absence of production |
| late-bloomer retention | Dear 001–003, 028–032 | Hatsuboshi can retain and develop a third-year who already failed publicly rather than sort her out early | later audit should compare how often system permits such recovery |
| competition and care | P2/N.I.A.; Dear 017–019 | competitive systems can create self-owned ambition without requiring hostility toward rivals/fans | zero-sum structures still create moral discomfort and unequal stakes |
| developmental-environment design | Dear 032–033 H.O.F. | Producer can mobilize event/rivals/stage context around psychological-development goals | effectiveness + retrospective consent do not settle advance-consent/governance question |
| Producer restraint | Dear 027; CIDOL 007 | route provides positive examples where Producer refuses to command return or withholds his design image to preserve idol authorship | compare against more manipulative interventions elsewhere |
| romance/profession overlap | Dear 010/037 + Producer-course paratext | institutional relationship permits intense personal attachment inside specialized production authority | user/student-producer proximity does not erase asymmetry; policy/governance remains open |
| technique as hospitality | Dear 031–036 | professional craft is framed as a means of whole-body fanservice/love, not merely competitive scoring | may encourage totalizing service expectations if boundaries fail |

## Phase 3 Sumika institutional deltas

| system ID | English label | Japanese | scope | explicit rule/fact | continuity role |
| --- | --- | --- | --- | --- | --- |
| `SYS-SUMIKA-01` | expectation as productive/disciplinary force | `期待` | D-SUMIKA / N.I.A. / HIF | fans, peers, rivals and institution generate expectations that can motivate, isolate, or overdetermine performance | central Phase-8 merit/formation problem |
| `SYS-SUMIKA-02` | post-injury capacity reconstruction | strength work / mental support / dance remediation | D-SUMIKA STEP3 | idol production coordinates physical and psychological rebuilding rather than treating talent as fixed | enabling institutional power |
| `SYS-SUMIKA-03` | authentic-history packaging | REVERSI profile/history production | Dear 029–030 | true private history is selected and framed to alter public/judge interpretation | intimacy -> public/competitive capital |
| `SYS-SUMIKA-04` | developmental distance control | Producer strong direction vs deliberate withdrawal | CIDOL 012 | Producer changes intervention level to elicit Sumika's preferences/authorship | sophisticated pedagogy + governance risk |
| `SYS-SUMIKA-05` | N.I.A. popularity ecology | rankings/followers/rumor | Dear 011–019 | rapid visibility changes peer relations and exposes idol to rumor/manipulation | institution generates social externalities |
| `SYS-SUMIKA-06` | fan expectation doctrine | `ファンの期待に応える` | Dear 024–026 | expectation matters but overfitting it can suppress the performer's own desire | prevents simple customer-sovereignty model |


## Phase 3 Ume institutional deltas

| system ID | label | scope | explicit analytical fact | institutional pressure |
| --- | --- | --- | --- | --- |
| `SYS-UME-01` | supplementary-admit development | P1[UME] | Hatsuboshi can admit exceptional physical potential without ordinary entrance-legibility and then build idol literacy around it | admission exception itself is a form of institutional selection |
| `SYS-UME-02` | family resource infrastructure | P1/D/M | Hanami athletic upbringing, nutrition/training expertise and family networks materially scaffold Ume's body | merit narrative must not erase unequal pre-school resources |
| `SYS-UME-03` | public competition as emotional pedagogy | P2/D-UME | wins/losses teach recognition, grief, respect and responsibility rather than only rank | competition can form ethics but can also overorganize self-worth |
| `SYS-UME-04` | Producer as developmental environment designer | P1→D | Producer widens Ume's comparison set through rivals, peers, fans and repertoire | effective intervention still raises authority/overidentification questions |
| `SYS-UME-05` | fan support as vocational obligation | D/CIDOL | Ume learns to treat received attention as strength to return at greater scale | strong reciprocity rhetoric can become totalizing service pressure |
| `SYS-UME-06` | song/repertoire inheritance | CIDOL/D-UME | becoming an idol includes learning prior repertoire and rereading older personal songs as the self changes | institutional culture is inherited, not invented anew by each route |

## Phase 3 Misuzu institutional deltas

| system ID | label | scope | explicit analytical fact | institutional pressure |
| --- | --- | --- | --- | --- |
| `SYS-MISUZU-01` | visible effort is not universal merit | P1/M | Misuzu can plan, train efficiently and improve while refusing conspicuous grind as identity | institutions may misread low-display effort as unseriousness |
| `SYS-MISUZU-02` | individualized production environment | P1→D | Producer clears paths and times interventions around a performer who understands her own pace | environmental design can support autonomy but also become paternalistic |
| `SYS-MISUZU-03` | strategic exploitation of a lost period | Dear 024–026 | Producer knowingly uses Misuzu's temporary overtraining phase to build fundamentals before stopping it | effective pedagogy raises manipulation/consent questions |
| `SYS-MISUZU-04` | solo/unit coexistence | SyngUp!/Begrazia/CIDOL | former-unit attachment, temporary reunion, solo identity and new-unit collaboration can coexist | institution need not force one permanent group ontology |
| `SYS-MISUZU-05` | competition as communication | Rinha/Temari/HIF | rivalry can transmit recognition and permit honest conflict where caretaking previously suppressed it | competition is productive but can intensify possessive identity |
| `SYS-MISUZU-06` | Prima Stella as lineage, not personality template | Dear 036 | title can pass to a self-paced, openly greedy winner who rejects honor-student imitation | legitimacy must tolerate stylistic plurality |
| `SYS-MISUZU-07` | student council as relational infrastructure | modular/CIDOL | Misuzu partially values institutional office as a future gathering space for old relations | governance roles can be used as social continuity infrastructure |

## Phase 3 Sena institutional deltas

### Prima Stella as constitutional office

Sena treats Prima Stella as more than an award. It is a visible office whose legitimacy depends on setting a horizon, surviving challenge, and making the academy's highest claim publicly contestable. A crown protected by distance is less legitimate than a crown held against rivals capable of taking it.

### Measurement as administrative technology

Sena's eye makes ability legible and supports targeted training, scouting, and resource allocation. Phase 3 strengthens its practical value while rejecting its conversion into total human truth. Parameters describe current visible capacity; they do not contain consent, support, narrative, future growth, audience reciprocity, or institutional conditions.

### Differentiated production

Sena does not produce one ideal type repeatedly. Kotone, Ume, China, Misuzu, Saki, and others require different environments and challenge structures. This supports Hatsuboshi as a formation system rather than a simple ranking machine.

### H.I.F reform

Her custom-song and summit design turns the competition into an argument about what each idol can uniquely make visible. The institution can therefore produce art and self-definition, not only comparative scores.

### Privilege and execution capacity

Family capital, elite childhood training, student-council authority, social networks, and inherited institutional access help Sena convert judgment into reality. These resources should be treated as causal infrastructure, neither ignored nor used to dismiss the labor and insight they enable.

### Founder-centered risk

Sena's reforms are developmental and still potentially monarchical. She selects, names, challenges, protects, withholds, and redesigns the field. Later phases must ask whether Hatsuboshi can preserve the plural ecology she creates without requiring her continuing interpretive sovereignty.

### Reformer succession question

The mature institutional test is not merely who succeeds Sena as top idol. It is whether rules, producers, rivals, and students can continue generating contestability after her personal office ends.

## Phase-3 Tsubame institutional delta — 2026-08-16

Tsubame demonstrates how **subordinate office and subordinate identity must be distinguished**. As vice president and reputed No.2, her institutional position mirrors the Sena hierarchy, but maturation does not require abolishing the role. She becomes capable of representing Hatsuboshi in her own style through external competition, inherited repertoire, junior training, administrative competence, and winner's responsibility.

Her route also adds an institutional ethical test: developmental systems can legitimately challenge a talented person without treating humiliation, ranking, or Producer insight as self-justifying. Producer's engineered Misuzu confrontation is effective but remains normatively contestable.

## Phase 3 Hiro AV — nonmetric charisma, risk, and sustainable production

### Nonmetric charisma and the danger of miracle extraction

Hiro's AV pass confirms that conventional technical measures do not exhaust idol attraction. Her low-force voice, fragile body, unusual musical environments, and crisis-linked concentration can generate a `神格` reception mode. The institutional correction is not “metrics are false”; it is that accurate partial measurements become unjust when promoted into total forecasts.

The same evidence creates a governance risk. If emergency reliably produces an exceptional peak, a school/Producer may become tempted to treat emergency as infrastructure. Hiro's consent and enjoyment are relevant but not sufficient to close the problem because production authority controls information, opportunity, load, and the future being wagered.

Current institutional rule:

> **Recognize nonmetric charisma without converting bodily precarity or relational fear into a permanent production requirement. Build a sustainable ordinary floor rather than governing entirely through peak miracles.**

Status: **canonical provisional finding through Phase 3 Hiro AV; adversarial Phase 8 audit required.**

## Mao audiovisual institutional delta — 2026-08-17

| evidence ID | institutional proposition | AV strengthening | pressure / qualification | status |
| --- | --- | --- | --- | --- |
| `INST-MAO-AV-001` | institutional production can reopen categories prior adult/professional systems treated as mutually exclusive | cute/cool/actor/prince states become a usable repertoire across Dear and principal performances | reconstruction remains strongly Producer-mediated | **STRENGTHEN** |
| `INST-MAO-AV-002` | Producer authority includes aesthetic interpretation and role authorship | image, costume, song, choreography, partnership, and future contract visibly depend on coauthorship | enabling interpretation can become enclosure | **STRENGTHEN / OPEN** |
| `INST-MAO-AV-003` | shared repertoire functions as intergenerational pedagogy | `Campus mode!!` communication/3DMV make Mao both inheritor and translator for Kotone/future entrants | one modular communication does not prove uniform institutional practice | **STRENGTHEN** |
| `INST-MAO-AV-004` | 100Pro exposes legitimate resource/credential advantages outside student production | Dear 021–026 acts the external offer as materially serious rather than villainous | Mao's route-specific refusal should not be generalized into anti-industry doctrine | **STRENGTHEN** |
| `INST-MAO-AV-005` | singular title can be personally interpreted as generative visibility | Dear 036 succession, crowd address, trophy, and red-prince staging make Mao's ethic public | title scarcity and hierarchy are not abolished | **STRENGTHEN / BOUNDED** |
| `INST-MAO-AV-006` | dorm seniority is a received-and-repaid care structure | `雪解けに` and `キミとセミブルー` show care, coordination, and hidden senior desire in acted form | service identity can delay Mao's own need disclosure | **STRENGTHEN** |

<!-- PHASE4_EVENTS_001_005_2026-08-23 -->
## Phase 4 — Events 001–005 institutional additions

**Authority:** `GKM_EVENTS_001_005_DEEP_READING.md` — Drive `1jb1bUXahrykBDIrdw3VJGdCHSZEGoIe0`.

- **Class as developmental-production unit — STRENGTHEN.** Class membership carries collective activities, inter-class competition, mutual liability, and internally generated developmental practices. Class 1-1 and 1-2 demonstrate different viable social technologies rather than one prescribed teamwork temperament.
- **Producer co-development — STRENGTHEN.** `アイドル強化月間` explicitly addresses Producer Course and Idol Course together and frames producer skill as something the institution trains and tests alongside idol growth.
- **Third-year summer school — PROMOTE.** Voluntary two-night/three-day summer program: training on the first two days, beach live on the final day, plus bounded leisure; framed by third-years as scarce late-school opportunity.
- **Public performance ecology — PROMOTE.** Event 003 connects the school live to local businesses, temporary labor, family/community memory, spectators, and commercial activity; stage and surrounding service ecosystem are mutually reinforcing.
- **Student-council pseudo-agency — PROMOTE.** Sena receives permission to make the student council function as a restricted `疑似的なアイドル事務所` and produce freshmen.
- **Producer Course jurisdiction — STRENGTHEN/PROMOTE.** In conflict with Sena's cross-role production, Producer Course students have priority; Sena cannot contractually bind idols, has reduced institutional benefits, and faces facility restrictions. Producer authority therefore includes concrete contract/resource/facility dimensions.
- **Cross-role safeguards — PROMOTE.** Hatsuboshi permits experimentation but recognizes conflict-of-interest risks when an elite idol/student-council president accumulates production authority.
- **Succession doctrine — PROMOTE.** Sena explicitly frames recruitment as cultivating a successor to `一番星` and a future guide for Hatsuboshi. Event 005 simultaneously exposes the limit of vertical succession when Saki and Ume resist or escape the successor model.

<!-- PHASE4_EVENTS_006_012_2026-08-23 -->
## Phase 4 — Events 006–012 institutional additions

**Authority:** `GKM_EVENTS_006_012_DEEP_READING.md` — Drive `12qIoWXbSo45TffFLiTA1WvKgB9wpRLJo`.

- **Student-council work can operate as experiential production training.** Event 006 gives juniors responsibility for designing a school event while senior advice supplies recipient/safety constraints rather than a finished answer.
- **Private family assets can enter school-event production through permission and stewardship.** China's family hot spring/resource access is analytically relevant as inherited privilege and as a resource she converts into shared hospitality; neither fact cancels the other.
- **Idol professional formation includes non-stage work.** Events 007–011 include amusement-park hospitality, retail/service management, food production, public/social-media exposure, and client-requested theater.
- **Recipient/audience experience repeatedly governs success.** Event 006 asks what users should feel; E007 converts fear into audience reassurance; E008 converts accidental exposure into answerable stage opportunity; E010 rejects a technically effortful but bad gift; E011 evaluates theater by whether the audience enjoyed it.
- **Client demand is negotiable rather than absolute.** Event 011's role reversal satisfies the client while expanding Mao's performer authorship.
- **Public social-media circulation can outpace official publicity control.** Event 008's viral clips expose unplanned personality before the trio deliberately converts attention into performance value.
- **Student-council authority retains discretionary elasticity.** Sena's Event 010 stage favor is bounded evidence that personal gratitude can be translated into institutional access; preserve for governance audit without escalating it into a corruption claim.

<!-- PHASE4_EVENTS_013_020_2026-08-23 -->
## Phase 4 — Events 013–020 institutional additions

**Authority:** `GKM_EVENTS_013_020_DEEP_READING.md` — Drive `1pyVYENC8kCbXvQtYU60pVdYad8yxCobF`.

## 13.1 Senior escort / regional-live program

Events 015, 018, and 019 collectively establish a recurring program architecture:

- normally a third-year idol leads two first-year idols;
- the group travels to a regional venue;
- participants take meaningful responsibility for set list, staging, MC, and local adaptation;
- the program combines professional performance with sightseeing/local research that can feed the show;
- program administration can survive contingencies, including replacing an unavailable senior leader with an exceptional first-year;
- the pedagogical goal is not merely junior observation. Juniors are expected to produce, adapt, and sometimes lead.

This should be promoted to the institution ledger as a concrete mechanism for **distributed production education**.

## 13.2 Sports festival as spectacle and training

Event 014 establishes:

- near-universal participation rules;
- school-assigned competition events;
- national broadcast;
- a class-live reward;
- class-level scoring that makes individual weakness socially consequential;
- explicit confidentiality/professionalism expectations even around school-event planning.

The school deliberately makes non-idol athletic performance part of public idol education. The event therefore tests public composure, teamwork, class identity, and marketable personality alongside physical ability.

## 13.3 Publicity club and ordinary-life recruitment media

Event 017 establishes that:

- student publicity media are institutionally supported;
- performers may be paid even for school-linked PR work;
- the school lends production equipment;
- peer-operated cameras may be preferred to professional distance when “daily life” is the desired object;
- student-council work includes live-event planning, municipal collaboration, and special idol-activity budgeting.

The school does not merely sell stage excellence to prospective students. It sells an integrated life-world.

## 13.4 First-year leadership can be formally trusted under pressure

Event 019 is an important exception case. The escort program is senior-led by design, but the student council selects Saki as emergency substitute because her observed adaptive capacity outweighs nominal year hierarchy.

This strengthens an institutional pattern seen elsewhere: Hatsuboshi's hierarchy is real but not mechanically seniority-bound when performance evidence supports exceptional responsibility.

---

<!-- PHASE4_EVENTS_021_PLUS_2026-08-23 -->
## Phase 4 — Events 021+ institution/system additions

**Authority:** `GKM_EVENTS_021_PLUS_DEEP_READING.md` — Drive `1kYHscRZA5RSTT6l5TGyaAUMLmeu9uQ6T`.

- **Senior workload correction (E021):** Rinami can use peer/council authority to remove Sena and Tsubame from council work and coordinate temporary training prohibition when duty reflexes block rest. Treat as observed corrective practice, not formal written policy.
- **China succession (E025):** Kuramoto China is explicitly named the **next student-council president**.
- **Next-council cohort (E025):** Ume and Misuzu are established current junior council members; Hiro is explicitly a next-council officer candidate. Do not infer final titles beyond China's presidency.
- **Workflow redesign (E025):** juniors propose an idol-specific scheduling application from Ume's parents' company to reduce coordination failures and enable shared progress visibility. Event does not prove final school-wide adoption.
- **Living repertoire (E024):** `ENDLESS DANCE` is described as a Hatsuboshi song socially monopolized by association with Sena; Ume/Misuzu/Sena's live visibly reopens it to other performers, including Temari's later setlist request.
- **Producer-project maturation (E024):** Sena's approximately year-long student-council production project ends with explicit recognition that she learned from her idols and that succession need not require her withdrawal.
- **External representative selection (E026):** an outside cover-live operator can request Hatsuboshi idols; headmaster and Sena participate in recommending representatives based on respect, ability, and reliability.
- **Event-029 branch possibility:** Producer Course student producing Asari-sensei as idol is internally coherent but continuity-gated; do not promote to baseline institutional history.

**Phase-4 institutional synthesis:** succession is continuity of responsibility/cultural possibility, not identity replacement.


<!-- PHASE5_SUPPORT_SERIES_01_2026-08-23 -->
## Phase 5 — Support Series 1 institutional additions

**Authority:** `GKM_SUPPORT_SERIES_01_DEEP_READING.md` — Drive `1bIaJl--tZuINAqz_mhNfufWMLjnEibwz`.

- **Middle-school → high-school training continuity:** S0001 directly shows internal middle-school students anticipating external high-school entrants and intensified competition.
- **Individualized physical loading:** S0009 shows Ume's extreme running plan independently aligned between Saki's notes and the professional trainer because of Ume's athletic history. Workload size therefore cannot be treated as a universal effort metric.
- **Turn-taking constrains training zeal:** S0008 China's desire for immediate retry is refused because lesson rotation still applies; persistence does not override institutional pacing.
- **Joint Class 1-1 / 1-2 lessons:** S0010 directly confirms ordinary cross-class training outside event-specific projects.
- **Dorm late-return process:** S0003 shows a formal permission/notification mechanism; Mao uses it, Kotone appears less reliable about compliance.
- **Dorm common space:** S0008 describes ordinary communal eating/study use and its evening social density.
- **Student-council renewal:** S0011 Sena/Rinami review incoming students before recruitment; S0012 Tsubame independently considers Saki for recommendation based on ability, learning speed, and etiquette.
- **Trainer pedagogy is differentiated:** vocal trainer encourages volunteering; visual trainer removes an overperformed archetype and asks Rinami to use relational imagination; dance trainer gives body-specific correction and workload boundaries.
- **Producer absence:** no Producer dialogue appears in the 26-script Series-1 support boundary. This tranche is peer/trainer/dorm/council ecology rather than Producer-mediated development.

<!-- PHASE5_SUPPORT_SERIES_02_PART_001_025_2026-08-23 -->
## Phase 5 — Support Series 2 Part 001–025 institutional additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_001_025_DEEP_READING.md` — Drive `1j7SzxEJ0KnP4GNYlvxEqNsJE3rSXFlPM`.

1. **Producer Course age/status heterogeneity — STRENGTHEN:** Asari states that many Producer Course students are older than the protagonist and that multiple currently active producers are enrolled.
2. **Producer-course peer ecology — OPEN:** same-age friendship may be structurally difficult, but the exact player response to Asari's friendship question is not preserved; do not promote “Producer has no friends” as fact.
3. **Dorm labor:** cleaning duties are shared obligations and Mao monitors compliance as dorm leader.
4. **Cafeteria governance:** menu variety/nutrition is institutionally managed and student input is solicited; idols nevertheless negotiate health against stress and preference.
5. **Joint class instruction:** cross-class swimming/visual lessons are normal institutional surfaces.
6. **Self-presentation curriculum:** friend photography and pose/expression analysis are explicitly educational tasks tied to idol self-presentation.
7. **Student-council recruitment:** Sena's scouting/persuasion occurs during ordinary class transitions, not only formal meetings.
8. **Community embeddedness:** festival vendors know Sena, offer goods in gratitude, and treat her as a trusted local/school figure; student-council legitimacy has an external social component.
9. **Academic coexistence:** third-year idols continue ordinary academic subjects alongside training and council work; Mao's weak rote memorization and Rinami's study routines are not extracurricular exceptions.

**Institutional caution:** Sena's personal offer to fund Kotone should not be generalized into a formal school financing mechanism.

<!-- PHASE5_SUPPORT_SERIES_02_PART_026_050_2026-08-23 -->
## Phase 5 — Support Series 2 Part 026–050 institutional additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_026_050_DEEP_READING.md` — Drive `1N8cUGstn4VM0sTfLJ_IQVhKfxKDIyL-j`.

- **Trainer error-correction is purpose-sensitive.** Dance trainer tells Kotone rehearsal exists for the audience/performance rather than for rehearsal itself; visual trainer expands Saki toward recovery/visual development; vocal trainer deliberately returns advanced Temari to fundamentals.
- **Dorm infrastructure produces relationships.** Shared kitchens, refrigerator/food routines, inherited games, shopping for cleaning supplies, and dorm-leader safety work create repeated cross-character contact.
- **Student-council succession includes skill transfer.** Sena explicitly assigns Tsubame to train Ume/China in next-year workflows; succession is not title-only replacement.
- **Practical expertise is distributed across rank.** Misuzu can teach Rinami Japanese cooking; China has practiced fish preparation Sena lacks; Sumika teaches Mao publicity; Kotone teaches cost-efficient shopping logic.
- **Publicity is part of idol labor.** Sumika/Mao support material treats short-form posing/video circulation as an operational skill with audience-growth consequences.

Institutional implication: Hatsuboshi's developmental ecology does not merely increase workload; it repeatedly changes the *form* of effort through technical correction, peer expertise, and institutional handoff.

<!-- PHASE5_SUPPORT_SERIES_02_PART_051_074_2026-08-24 -->
## Phase 5 — Support Series 2 Part 051–074 institutional additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_051_074_DEEP_READING.md` — Drive `1ltF2IUHs9HJZdHB8zTW2XsIbqmRyTPhP`.

| institutional surface | evidence | promoted implication |
| --- | --- | --- |
| student-council succession | `0069` Sena/Tsubame/Rinami divide handoff work; `0077` Ume proposes new summer/garden practices | continuity is procedural **and** generative; successor legitimacy does not require imitating seniors |
| cross-course technical collaboration | `0059` ordinary-course game club recruits Hiro as app-development adviser | Idol Course expertise circulates across school subcultures; institutional ecology is not socially siloed |
| recruitment/public relations | `0054` Mao/Sumika rehearse comedy specifically to make school life approachable to applicants | school self-presentation includes controlled informality and student-performed accessibility |
| dorm governance | `0065` Mao's management fatigue is visible to Misuzu; first-year cohort produces workload | dorm leadership is real labor with fatigue cost, not ceremonial status |
| fan reciprocity | `0069` Sena/Mao attend to wrapping, cards, letters; Mao writes replies | popularity is institutionally/socially mediated through reciprocal attention, not only ranking |
| trainer/senior safety norm | `0056` Tsubame stops Hiro; `0079` Tsubame ends Kotone practice after observed fatigue | professional effort is invalid when it crosses recipient-specific health limits; senior care can include enforced stopping |
| tea/community social use | `0074` China/Misuzu plan tea comparison in council room | formal institutional rooms also support low-stakes relationship culture |
| community volunteer work | `0060` council is asked to collect fallen chestnuts for cleanup; Hiro assists | council/community interface includes mundane maintenance, not only performances/events |

**System-level synthesis:** rank is porous because expertise remains domain-specific; juniors can teach seniors, and institutional inheritance is healthiest when inherited procedure leaves room for new rituals.

<!-- PHASE5_SUPPORT_SERIES_03_PART_001_025_2026-08-24 -->
## Phase 5 — Support Series 3 Part 001–025 institution / idol-system additions

### Student council as dual civic-production apparatus

`story_0015` is direct S1 evidence that **Sena's current-year student council** is intentionally organized as a `疑似的なアイドル事務所` while retaining real council obligations. Do not generalize this to all Hatsuboshi student councils across years.

Initial roles stated in the support story:
- Juo Sena — president;
- Amaya Tsubame — vice president;
- Himesaki Rinami — secretary;
- Hataya Misuzu — accounting audit (`会計監査`);
- Hanami Ume / Kuramoto China — first-year council members, with more specific duties routed elsewhere when explicitly sourced.

### Producer Course professional ecology

`story_0019–0020` establish that Producer Course development includes horizontal peer/professional networking and inherited experience. Asari explicitly says producer-to-producer connections can later benefit assigned idols.

Asari's profession model: modern producers are both generalists and specialists, and should appear as reliable problem-solving `魔法使い` to their idols **even when the visible certainty is partly a performed role (`ふり`)**. This is professional reassurance, not permission to falsify evidence.

### Hardship support

`story_0024` explicitly names a `苦学生救済の制度`. Rinami offers to investigate it with Kotone after identifying that excessive paid work is undermining school performance. Exact eligibility, payment, or benefit type is not stated.

### Dormitory as developmental infrastructure

`story_0005/0007/0022` reinforce dorm life as a cross-year observation/support surface: newcomer orientation, cleaning competence, work-fatigue detection, food/sleep/safety, and senior intervention become visible there in ways not available onstage.

### Trainer/program authority

`story_0023` shows Saki stopping Ume from using new equipment before the trainer arrives because doing so would violate the planned program. Saki's high self-directed optimization therefore remains compatible with deference to professional training design.

<!-- PHASE5_SUPPORT_SERIES_03_PART_026_050_2026-08-24 -->
## Phase 5 — Support Series 3 Part 026–050 institutional deltas

### Student-council memory transmission

`story_0030` shows an informal institutional lineage: a graduated council senior once protected anxious newcomer Rinami during external festival duty by sharing a private fireworks viewing place. Rinami later gives that place to China and explicitly asks her to give it to a future junior. This is **institutional continuity through remembered interpersonal care**, not a formal rule.

### Producer calibration — Sena

`story_0032` contains Sena's explicit admission that she scouted Ume/China/Misuzu by looking overwhelmingly at talent and ability and was unprepared for their personalities. This is direct evidence that elite idol evaluation and producer readiness are different competencies.

The same story shows China's grandfather's H.I.F expectation being relayed through the principal to Sena. Preserve as a source-bounded example of family expectation entering production planning; do not generalize to all students.

### `Campus mode!!` succession infrastructure

`story_0044`–`0046` establish that the song is:

1. treated by students as an expression of Hatsuboshi itself;
2. a scarce performance opportunity rather than automatic repertoire access;
3. a generational comparison surface;
4. taught laterally and downward by students who themselves learned from seniors;
5. explicitly described by Mao/Rinami as a baton they received and must pass on.

Institutional repertoire therefore survives through **peer/senior pedagogy**, not only trainer instruction or official assignment.

### Public-role load

`story_0038` distinguishes Sena's stage confidence from the separate pressure of representing Prima Stella/president as the incoming class's target and ideal. `story_0048` further shows that extreme popularity creates logistical and dietary burden even when fan affection is welcome.

### Dorm tradition

`story_0040` explicitly states that bonfire sweet-potato fire control is passed down by successive dorm seniors. Treat mundane food practice as part of the dorm's memory-bearing developmental culture.

<!-- PHASE5_SUPPORT_SERIES_03_PART_051_075_2026-08-24 -->
## Phase 5 — Support Series 3 Part 051–075 institution / idol-system deltas — 2026-08-24

### Student council as coordination layer

Support stories `0056`, `0061`, `0062`, `0066`, `0069`, and `0070` strengthen the council as a router between **commercial schedule, school welfare, junior development, civic duty, and personal knowledge**. Tsubame absorbs council load from overworked Sena; mentors China; evaluates first-year civic disposition; the council considers support for Hiro's popularity/readiness mismatch; it conducts festival patrol; and Kotone already receives work-related accommodations.

### Ordinary-course contact

`story_0060` adds Mashiro Yu, ordinary-course second-year and broadcast-club president. Idol-course students therefore remain embedded in a broader school ecology whose members do not share idol-course behavioral norms.

### Popularity can outrun technical readiness

`story_0066` makes Hiro an institutional problem case: performance is technically marginal by Sena's standard while affective appeal and popularity are real. Support infrastructure must sometimes manage **demand generated before the performer can safely sustain it**.

### Work/school time poverty

`story_0070` preserves Kotone's employment as a material constraint: understaffed shifts, academic red marks, retest risk, existing council accommodations, and senior tutoring all interact. Do not psychologize the problem into poor discipline.

### Civic ritual / local reciprocity

`story_0069` strengthens recurring festival patrol, a customary fireworks-viewing place, and vendor recognition/provisioning. Hatsuboshi council labor is embedded in a local commercial/community network.

### Mentorship is student-distributed

Tsubame's custom China worksheets and cross-domain instruction further demonstrate that student development is not trainer-only. Senior students materially supply bureaucracy, academics, fundamentals, and professional expectation.


<!-- PHASE5_SUPPORT_SERIES_03_PART_076_102_2026-08-24 -->
## Phase 5 closure - institutional deltas

### Succession is person-specific before it is bureaucratic

- Tsubame explicitly asks Misuzu to support China/Ume after the seniors leave.
- Mao says dorm leadership is repayment of care she received from prior dorm seniors.
- Sena accepts the possibility of returning after graduation to help juniors/community activity.
- the third-year sports-festival closing live is framed as encouragement to the students who will carry Hatsuboshi next.

Institutional continuity is therefore partly a chain of people remembering how they were treated and reproducing the useful function for later recipients.

### H.I.F. is also a reputation and talent market

Final support evidence shows H.I.F. operating simultaneously as First Star competition, school-reputation stage, Rinha return site, media/broadcast surface, and external scouting opportunity for rival institutions. Phase 8 should treat H.I.F. as governance + symbolic reputation + labor/talent market, not only a performance bracket.

### Adaptive trainer pedagogy

`story_0100` has the specialist trainers explicitly recognize that rising student ability can outgrow group-instruction defaults. They self-audit pedagogy, discuss individualized limits, and identify Producer Course students as absorbing some tailoring work. Staff development is therefore part of the academy's developmental system.

### First Star as representative stewardship

`story_0104` makes explicit that First Star represents an era of Hatsuboshi and that the holder's conduct affects the school's evaluation. Sena's title pursuit carries representative obligation, not merely personal supremacy.

### Broadcasting and ordinary-course permeability

Mashiro Yu's broadcast role becomes a self-authored school-wide vocation. Ordinary-course students can therefore mediate idol visibility and institutional memory without becoming idol-course students themselves.

**Phase 5 institutional source pass complete: 498/498 support scripts / 9,777/9,777 messages.**

<!-- PHASE6_RELATIONSHIP_SYSTEMS_II_2026-08-24 -->
## Phase 6 — Relationship Systems II institutional routing — 2026-08-24

**Canonical relational synthesis:** `GKM_RELATIONSHIP_SYSTEMS_II_RIVALRY_FRIENDSHIP_CLASS_AND_SUCCESSION.md` — Drive `1sN6rcZPUBmkJaYPpyhPUMRSI29gZHQqK`.

This section adds no new institutional source object. It consolidates already-read institutional evidence into the current Phase-6 relation model.

### Class networks

- Class 1-1 is best modeled as a **competitive federation / competitive-legibility environment**: rivalry, comparison, skill judgment, and ordinary peer access coexist.
- Class 1-2 develops a stronger **affiliative-resilience / mutual-aid** pattern, especially around the self-authored Worst Three identity.
- Joint lessons and ordinary-course contact keep both classes permeable; class identity is a medium-strength network, not an enclosure.

### Seniority and expertise

Seniority creates real responsibility, expectation, and intervention rights, but does not create global competence. Tsubame can impose a safety stop while learning embodied technique from Ume; Sena can create opportunities while needing correction about consent or person-reading; Mao/Rinami/Tsubame transmit different senior-care grammars. **Rank is institutionally meaningful and epistemically porous.**

### Succession / inheritance

The governing succession model is **function transfer with re-authored form**. Evidence already routed elsewhere includes:

- China as explicit next student-council president;
- junior council members/candidates inheriting work while proposing new methods;
- Tsubame asking Misuzu to support China/Ume;
- `Campus mode!!` as generational baton plus peer pedagogy;
- Rinami passing an inherited festival-viewing practice to China for later transmission;
- Mao's dorm leadership as repayment/reproduction of care once received from older students;
- graduating seniors remaining available as alumni rather than being erased by succession.

Institutional continuity therefore depends on **remembered relational treatment becoming future practice**, not only written office procedure.

### Producer as a bounded institutional-relational node

The Producer occupies institutional liminality: credentialed developmental authority while still a Producer Course student who is evaluated, networked, and professionally socialized. Route-bounded Producer relationships provide diagnosis, scheduling/material coordination, confidence scaffolding, and coauthorship, but should not be concatenated into one simultaneous biography.

Producer Course peer networking and Asari's `魔法使い` framing reinforce that confidence can be a professional care performance rather than omniscience. The institutional risk is **interpretive monopoly**: one high-centrality producer deciding that insight or belief substitutes for the idol's authorization or for independent peer/family/senior expertise.

> **Healthy production is orchestration without social replacement.**

For mature reconstruction, institutional status should always be paired with **domain authority + refusal rights + redundant social support**.



<!-- PHASE6_SIDE_CHARACTER_SYNTHESIS_INSTITUTIONAL_ROUTING_2026-08-24 -->
## Phase 6 - side-character synthesis institutional routing

**Canonical synthesis:** `GKM_SIDE_CHARACTERS_FAMILIES_STAFF_GOKUGETSU_AND_EXTERNAL_PRESSURES.md` - Drive `1s-sOAHkQK9qgZaXwtP36ev3kWU6uq7W6`.

This is a synthesis-only institutional update; it introduces no new Source Lock object or locator.

- **Institution is not one actor.** Kunio, Asari, trainers, student government, Producer Course students, H.I.F. organizers, rival schools, media, and industry actors hold different powers. Do not convert one person's decision into total Hatsuboshi policy without evidence.
- **Adaptive pedagogy is part of institutional health.** Trainers explicitly self-audit when student ability outgrows group defaults; successful development can force the institution to revise its teaching model.
- **External standards keep Hatsuboshi falsifiable.** Gokugetsu and its associated rivals/scouts supply alternative technical, ethical, and professional standards rather than functioning only as villains.
- **H.I.F. is a multi-audience interface.** It is simultaneously competition, public record, school-reputation surface, media event, emotional return site, and external talent-observation / recruitment market.
- **Media permeability has refusal boundaries.** Mashiro Yu demonstrates that ordinary-course/broadcast actors can mediate idol visibility and institutional memory while retaining a distinct vocation and the right to refuse work.
- **Professionalization is not authorship supremacy.** Ryuusei/100Pro-style offers can be rational and resource-rich without automatically overriding the performer's judgment about a constitutive producing relationship.
- **Family infrastructure affects institutional merit.** Money, equipment, household labor, migration support, debt, networks, and fallback options materially change how much risk a student can absorb.

Phase-8 institutional synthesis should therefore evaluate systems through the people who administer and contest them, not only through stated rules.

**Next Phase-6 operation:** `GKM_KAYA_RINHA_SOURCE_CROSSWALK.md`.
