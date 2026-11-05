---
series: BLUE_ARCHIVE
artifact_type: sequential_deep_reading
scope: GROUP_1501_1503
generation: V1
source_story_ids: ["BA:group:1501", "BA:group:1502", "BA:group:1503"]
status: canonical
source_boundary: "Complete canonical Japanese group sequence BA:group:1501 through BA:group:1503 at electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; six scenes, 165 structured utterances including six location units, 159 canonical text anchors, zero choice groups; Eimi's printed speaker route retains an empty person join"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Veritas group story deep reading

## Private records, ordinary embarrassment, and answerable knowledge

The complete `Trouble & Trackers（１）–（３）` sequence begins with an ordinary disappointment about body-measurement records and ends with an inaccurate rumor continuing after a correction notice. Its central thesis is that **technical capacity and a club's truth-seeking identity do not establish the right to alter or disclose another person's information**. Yuuka refuses to misuse her own authority while nevertheless leaving a weak security practice; Veritas members turn concern about their own records into unauthorized changes and publication; Chihiro answers their competence-based pride with a demand for hacker ethics. Correction is necessary but does not erase the social aftermath.

Ordinary evidence is substantive here: embarrassment, snacks, peer persuasion, the desire to impress Sensei, technical curiosity, minor retaliation, teasing, and the unpleasant persistence of a rumor. This reading proposes admission of all three complete `group` objects. Their quiet origin is neither a reason to omit the first episode nor a reason to downgrade their contribution to the institution's ethical and personal repertoire.

## 1. Complete inspection and exact witness

All sources were read in Japanese at the pinned generation `BA_REFRESH_20260928T032248159554Z`. The raw witness is `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw groups `1501`, `1502`, and `1503` all route to `DB/ScenarioScriptExcelTable1.json`, SHA-256 `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`.

| Complete source | Canonical path relative to the generation | Counts and canonical SHA-256 |
|---|---|---|
| `BA:group:1501` | `02_CANONICAL_STORIES/GROUP/CLUB_005_001/EPISODE_001_1501.md` | One scene, `u:0001-0043`; 43 structured utterances including one location, 42 text anchors, 50 raw records. `70056b3766c7eec10544e4791c06f9f3b8cd5eb6a6ad257847bcde48e288257b`. |
| `BA:group:1502` | `02_CANONICAL_STORIES/GROUP/CLUB_005_001/EPISODE_002_1502.md` | Three scenes: `u:0001-0019`, `u:0001-0036`, `u:0001-0015`; 70 structured utterances including three locations, 67 text anchors, 129 raw records. `65b261f56895803944be8b6297ead632ee9e8f1baed361055f98fc2269ccd472`. |
| `BA:group:1503` | `02_CANONICAL_STORIES/GROUP/CLUB_005_001/EPISODE_003_1503.md` | Two scenes: `u:0001-0042`, `u:0001-0010`; 52 structured utterances including two locations, 50 text anchors, 88 raw records. `3e69f37a341ee3f69f58cea53563890cecabc511e80abe056c3fcfc3d457857d`. |

Total: **165 structured utterances, six location units, 159 canonical text anchors, six scenes, zero choices**. Location-only units appear as headings in the canonical rendering. No isolated person bundle substitutes for the narrative. `03_STRUCTURED_DATA/stories.jsonl` provides the class/path; `utterances.jsonl` retains raw Korean labels, mapped Japanese labels, text, raw group and per-record locators. For example, `:1502:scene:001:u:0002` routes to `ScenarioScriptExcelTable1.json:DataList[107171]`, and `:1503:scene:001:u:0022` to `DataList[107340]`. Primary acquisition remains outside analytical Git.

Veritas is directly named in the locations and Maki's club description (`:1501:scene:001:u:0026`). The numeric `CLUB_005_001` route still has unresolved generic club resolution and is not independently treated as an institutional identification. Secure structured person IDs are `BA_PERSON_MAKI`, `BA_PERSON_HARE`, `BA_PERSON_KOTAMA`, `BA_PERSON_YUUKA`, and **`BA_PERSON_CH0160` for Chihiro**, verified by `PERSON_REGISTRY.csv`. Do not invent a `BA_PERSON_CHIHIRO` replacement for that source ID.

**Eimi is a material metadata exception:** `エイミ`, raw `에이미`, speaker ID `BA_SPEAKER_UC5D0_UC774_UBBF8`, speaks in `1502` scenes 001 and 003, but her utterances have `person_id=""`, and the story's person list omits her. `PERSON_REGISTRY.csv` separately contains `BA_PERSON_EIMI`/`和泉元エイミ`/`エイミ`. The reading preserves the empty join and uses the printed named speaker rather than dropping her from coverage or silently claiming the join was repaired. Her named analytical row can carry the scene with this mapping limitation; upstream normalization remains a separate source-domain task. The printed two campus students in `1503` are local generic roles and are not merged with other student A/B appearances.

## 2. Chronology, branches, and knowledge

All three release dates are absent and their cross-source story chronology remains unresolved. Their group IDs and this assigned reading order provide no relation to Pavane C001/C002, the Final arc, or other group scenes. Those main checkpoints retain their own chronological and source-witness boundaries. The packet instead supports internal relations: today's measurement follows Maki's reported preceding week of effort; the operation follows planning; the classroom/office reactions follow publication; Chihiro returns on the incident's evening; a hallway coda is explicitly several days after the incident (`:1501:scene:001:u:0004-0009; :1503:scene:001:u:0021,0027; scene:002:u:0002`).

The scene cuts interleave Yuuka/Eimi's office work with the group's interception and upload. Dialogue links those strands, but no precise timestamp for every technical operation is printed. Chihiro is unknown to the attackers during the contest; she later describes inspecting the academic-record server and recognizes their conduct. Their subsequent inference that the vice-president was the opponent is supported by the matching account, not by a displayed complete technical audit.

Sensei is an imagined audience in Maki's persuasion, not a present actor or proven recipient of records. `[USERNAME]先生` is a source placeholder; no actual username is supplied. There are no Sensei choice alternatives, branch convergence, or separate MomoTalk thread objects in this packet.

## 3. Narrative and scene argument

### 3.1 A record threatens Maki's self-image

Maki is disappointed that her measured weight did not fall despite reported snack restriction and evening running. Hare initially checks whether she means an instrument problem. Kotama answers through input/output/data language; a Maki-tagged third-person remark about late-work snacks has an attribution caution (`:1501:scene:001:u:0002-0017`). No actual measured weight or independent record of diet/activity is supplied. Kotama's simplified comparison is character rhetoric, not medical advice or a validated model of bodily change.

Maki's grievance soon concerns persistence and audience: she fears this record will remain in school history as a stain and lifelong impediment. Hare questions whether anyone would pay that much attention and treats a measurement as temporary (`u:0018-0024`). The story therefore establishes competing attitudes toward an ordinary record. Neither Maki's prediction of permanent disgrace nor Hare's minimal concern is an omniscient social fact. The several-days coda later gives Maki's worry about persistent reputational effects an ironic counterpart, attached to a false record she helps expose about someone else.

Maki invokes Veritas as guardians of truth and justice while proposing alteration of academic data (`u:0025-0027`). The contradiction is immediate, not a hidden eventual betrayal. Kotama calls the purpose falsification at the close, and Hare calls it a drone stability test; Maki retains the grander slogan (`u:0040-0043`). Different motives cooperate without sharing one ethical justification.

### 3.2 Persuasion uses appearance and technical curiosity

Maki recruits Kotama by claiming an attractive record will impress Sensei. Kotama reluctantly agrees in the language of helping a junior, then explicitly denies wanting to impress the teacher (`:1501:scene:001:u:0028-0033`). This supports denial/affection or appearance coding as a situated possibility; it does not prove the denied motive as an objective fact, a romantic relationship, actual teacher scrutiny, or a general private persona.

Hare says she does not care about the measurement. Maki changes the appeal to a newly built hacking drone needing real-world testing; Hare acknowledges insufficient operational data and agrees to one use (`u:0034-0038`). Technical curiosity is a positive personal interest here, yet does not justify unauthorized deployment. Maki then treats limited agreement as commitment without withdrawal (`u:0039`). This is peer momentum and persuasion, not evidence of a threat or fully coerced assent. The different stated aims must remain distinct when later synthesis describes the club's motives.

### 3.3 Yuuka's fairness and weak security coexist

In the office, Eimi brings the last scales back. Yuuka recalls attempts to distort previous measurements through inventions and defines the test as accurate current development data. She admits wanting to interfere with the scale after eating snacks while accompanying the Game Development Department, but rejects Eimi's suggestion that her authority could simply modify records (`:1502:scene:001:u:0002-0015`). Her emphatic reason is that an official's abuse would damage school norms and that Seminar's accountant must be fairer than anyone else.

This is direct ordinary evidence of temptation constrained by a public-role norm. It neither proves the whole institutional measurement policy legitimate nor makes Yuuka immune to embarrassment. Her willingness to admit enjoying company/snacks and dissatisfaction complicates the image of a detached accounting machine. It is a self-report, not an observed snack session or a measured diet.

Eimi then requests access to enter records. Yuuka supplies an unchanged initial password, which works (`u:0016-0019`). The narrative juxtaposes a refusal to abuse authority with a security practice vulnerable to interception. The two qualities can coexist: normative intention is not operational infallibility. A fictional password and stated “highest” security are not general evidence about real systems, and this reading derives no reusable security procedure from the technical dialogue.

### 3.4 Protection of one's privacy becomes violation of others'

Kotama reports intercepting the office exchange; Hare deploys the drone, and Maki reports gaining editing authority. They discuss implausibly flattering revised measurements. Maki then proposes setting Yuuka's weight to **100 kg** as a small revenge for past interference (`:1502:scene:002:u:0002-0026`). This is a false-data proposal. The later published value corroborates that the false value reaches the circulated record; it does not establish Yuuka's actual mass, body composition, health, or any real measurement.

A counterattack interrupts them. Hare asks for log deletion and disconnection, but Maki refuses to abandon the valuable data and copies it to an unidentified node. The system text explicitly says files are being copied from `student_data` to `social_network`; Hare identifies the destination as a publicly visible SNS server (`u:0027-0036`). In the office, Eimi observes everyone's measurement records on the school SNS; Yuuka confirms and rejects the displayed false value (`scene:003:u:0002-0015`). These observations support publication within the school-network context. They do not establish global Internet distribution, how many students actually read every record, or the permanence of every copy.

The ethically decisive shift is from one's own embarrassment to information about others. Maki initially objects to school retention as privacy invasion, yet her panic over losing accessed data results in nonconsensual exposure. The disclosure is accidental as a destination choice, while the underlying access, falsification, retention, and retaliation are deliberate. Those distinct forms of intent should not be compressed into either pure accident or purposeful publication of every student's data.

### 3.5 Internal competence pride meets an ethical limit

In `1503`, the group struggles against countermeasures. Hare admits defensive coding is not her specialty and reports that attempts are anticipated; the group retreats when identity exposure becomes likely (`scene:001:u:0002-0020`). Their withdrawal is a locally reported operational limit and avoidance of consequences, not a completed ethical recognition.

On the incident's evening, Chihiro returns and describes defending the server against an unusually fast attacker. The members recognize their encounter, but attempt to restore club prestige: losing to their vice-president is acceptable because no outsider surpassed Veritas (`u:0021-0039`). Chihiro explicitly interrupts that self-congratulation with `他人の個人情報をなんだと思ってるの？` and a demand for hacker ethics; Maki begs pardon (`u:0040-0042`). The club's authority can correct its own members rather than simply defend their interests against Seminar. Exact sanctions, physical punishment, complete restitution, and the content/results of subsequent instruction are not printed.

### 3.6 A correction notice does not close the reputation problem

Several days later two students repeat the 100 kg rumor and invent equipment or holographic explanations to reconcile it with Yuuka's appearance. Yuuka rejects them and reports that she immediately announced the earlier information was false, yet rumors have grown. She still demands to know the perpetrator (`:1503:scene:002:u:0002-0010`).

This is a bounded observed persistence: these students repeat the falsehood, and Yuuka reports a correction notice. It does not prove that everyone believes it or that official records remain changed. Chihiro's discovery also has not demonstrably informed Yuuka; the teacher, all students, and other institutional actors cannot be assigned the vice-president's knowledge. The scene ends with unresolved answerability rather than a successfully closed privacy incident.

## 4. Character and directed relationship additions

| Subject/direction | Secure contextual contribution | Limit |
|---|---|---|
| Maki | Concern about her own image/record, persuasive adaptation to peers' interests, explicit retaliatory false-data proposal, panic retention/upload, club-pride recovery, and apology under correction. `:1501:scene:001:u:0004-0009,0018-0043; :1502:scene:002:u:0011-0036; :1503:scene:001:u:0006-0019,0027-0042`. | No actual weight, eating history diagnosis, global fraud disposition, universal technical ability, or durable moral reform. |
| Hare | Skepticism about record significance, curiosity about drone data, technical specialization limits, attempted shutdown, and disappointment about competence. `:1501:scene:001:u:0019-0024,0034-0038; :1502:scene:002:u:0007-0010,0018,0026,0029,0033-0035; :1503:scene:001:u:0005-0017,0025`. | Curiosity coexists with participating in unauthorized access. A local failure does not determine every domain's rank or validate a real security technique. |
| Kotama | Data-first rhetoric, body/virtual-self deflection, teacher-facing denial, interception, explicit recognition of falsification, and operational warning. `:1501:scene:001:u:0010-0016,0028-0033,0041; :1502:scene:002:u:0002-0005,0019,0027-0028; :1503:scene:001:u:0002-0003,0015-0016,0026,0034`. | Stated reluctance/help to a junior is not proved absence or presence of the denied desire. Surveillance capacity is bounded by this represented incident. |
| Yuuka | Admits personal temptation and snacks/company, refuses self-serving record abuse, leaves initial credentials, reacts to false publication, and reports corrective notice with ongoing social harm. `:1502:scene:001:u:0004-0019; scene:003:u:0003-0015; :1503:scene:002:u:0007-0009`. | Public-role fairness does not establish secure practice, full record repair, catch of offenders, or an actual 100 kg measurement. |
| Printed Eimi → Yuuka | Performs measurement cleanup/record entry, asks about administrative editing capacity, notices published records, and accepts the false number before Yuuka rejects it. `:1502:scene:001:u:0002,0005,0009,0012,0015-0019; scene:003:u:0002-0014`. | Person join remains empty. Her suggested meal management is a character response to false information, not a grounded medical judgment or authorial recommendation. |
| Chihiro → Veritas members | Reports technical defense, recognizes the culprits, refuses their club-prestige consolation, and insists on other people's information and ethics. `:1503:scene:001:u:0022-0042`. | Vice-president title is explicitly supplied at u:0034/u:0038. No inspected punishment, privacy-restoration outcome, or proof of universal invulnerability. |
| Maki → Kotama/Hare | Recruits through different incentives and attempts to foreclose withdrawal after limited agreement. `:1501:scene:001:u:0028-0039`. | Persuasive pressure does not erase their stated reasons or become an adult coercion model. |
| Veritas ↔ Seminar | Unauthorized intervention exposes weak security and creates a problem defended/corrected partly by Veritas's own vice-president. | Concern for knowledge freedom does not authorize falsification; institutional weakness does not authorize exposure. No completed interinstitutional hearing is printed. |

## 5. Written Japanese and speaker limits

No performed voice is inspected. The text distinguishes Maki's expansive `あたし`/mission enthusiasm, Hare's plain specialization and limits, Kotama's polite data/virtual-world formulations, Yuuka's role-duty emphasis, and Chihiro's direct ethical rebuke. These are situated samples, not whole-person voice specifications.

`真理の守護者`, `正義`, and `知識の自由` occur beside `身体測定の記録を偽造するために` and the drone-test motive (`:1501:scene:001:u:0026,0040-0043`). The collective slogan contains divergent aims and an explicit contradiction. Kotama's denial about Sensei and virtual-self claim are responsive self-presentations, not objective explanations supplied by a narrator. Yuuka's `セミナーの会計は、誰よりも公正でないといけない` is a publicly anchored self-standard rather than proof she always meets it (`:1502:scene:001:u:0013-0014`).

The system-folder narration verifies the represented direction of copying but supplies no complete underlying logs. `副部長` grounds Chihiro's immediate role, and her `他人の個人情報` shifts the issue from who won to whose information was affected. In the coda, `噂`, `かもしれない`, and the escalating explanations mark gossip/hypothesis; they cannot authenticate the false bodily claim.

| Exact locator | Attribution or interpretation caution |
|---|---|
| `BA:group:1501:scene:001:u:0012` | Maki's raw/mapped tag speaks about Maki's recent soda/chip intake in the third person. Preserve label and mark ownership uncertain; do not silently assign to Hare/Kotama or treat it as an authenticated dietary record. |
| `BA:group:1503:scene:001:u:0004` | Hare's raw/mapped tag asks `ハレ先輩助けて`; likely a requesting peer in the exchange, but no reassignment is authorized. Secure Maki requests at u:0006-0007 and Hare's technical replies independently establish the help sequence. |
| `BA:group:1503:scene:001:u:0037-0038` | Maki-tagged polite collective defeat and Kotama-tagged plain response differ from surrounding usual registers. Keep as warnings, not a proved swap; group self-congratulation is secure at u:0039 and correction at u:0040. |
| `BA:group:1502` Eimi turns | Printed named speaker is secure; source `person_id` is empty. Neither source-person metadata omissions nor registry availability authorize silently repairing all source records. |

## 6. Counterreadings and bounded behavioral delta

**“This is only a weight joke.”** The joke's false number and exaggerated rumor are central, but the complete sequence addresses retention anxiety, desired self-presentation, ordinary peer motives, official restraint, unauthorized disclosure, correction and residual harm. Omitting those would erase the argument that smaller concerns can reveal how an institution treats others' agency.

**“Veritas exists to defend freedom of information, so this exposes an evil club.”** Maki's slogan is contradicted by the plan, and participants knowingly pursue falsification. Chihiro's internal defense and explicit correction prevent treating misconduct as the uncontested norm of every member. This establishes a contested institution, not universal ethical competence or permanent corruption.

**“Yuuka caused the incident through bad security, so the disclosure is legitimate.”** Weak practice contributes to access. It does not transfer consent to falsify or publish records. Her refusal to abuse authority is positive evidence independent of her security failure; equally, positive intention does not repair the failure by itself.

**“The attack failed, so no records were changed or harmed.”** The editing rights and proposed false value precede publication, which Eimi and Yuuka observe; the coda confirms circulation of that value. Final retreat does not annul that outcome. Yet no source permits treating the circulated false value as truth or asserting a permanently corrupted official database.

**“Chihiro's superiority proves Veritas unbeatable.”** Her own account says the attacker nearly overcame her. The group's consolation is explicitly rejected by her ethical reply. Technical superiority over these colleagues in one incident is neither a global hierarchy nor an ethical answer.

**“The correction restores everything.”** Yuuka's notice is reported and several students still repeat the falsehood. No inspection establishes deletion, repair, offender disclosure to Yuuka, complete reputational recovery, or future recurrence. This is a reason to keep the outcome open, not invent permanent trauma.

The [Pavane C001](../MAIN/VOLUME_002_%E6%99%82%E8%A8%88%E3%81%98%E3%81%8B%E3%81%91%E3%81%AE%E8%8A%B1%E3%81%AE%E3%83%91%E3%83%B4%E3%82%A1%E3%83%BC%E3%83%8C/BLUE_ARCHIVE_MAIN_V002_C001_CHECKPOINT.md) and [C002](../MAIN/VOLUME_002_%E6%99%82%E8%A8%88%E3%81%98%E3%81%8B%E3%81%91%E3%81%AE%E8%8A%B1%E3%81%AE%E3%83%91%E3%83%B4%E3%82%A1%E3%83%BC%E3%83%8C/BLUE_ARCHIVE_MAIN_V002_C002_CHECKPOINT.md) checkpoints record Veritas mainly through technical support, seized tools and dangerous coalition work, with role/private limits. This packet supplies ordinary motivations and ethical conflict rather than retrospectively changing those scenes. It sharpens the distinction among technical access, reliable data, and legitimate use; no ordering licenses a development arc from prank to main heroism.

**Observed mechanism:** anxiety about one's record → differently motivated peer enlistment → unauthorized access/false-data proposal → panic preservation in response to counterattack → publication → internal ethics correction → rumor persistence. The packet also supplies a positive countermechanism in Yuuka's explicit refusal to exploit her editing authority. No rule or prediction was frozen before exposure; `NO_DIAGNOSTIC_OPPORTUNITY`. No operational model, diagnostic score, or new durable claim ID is created.

## 7. Proposed seven-ledger deltas

The integrating owner retains shared mutable surfaces. Append source-scoped contextual entries while preserving main-story and historical first-pass boundaries.

| Ledger | Proposed effect |
|---|---|
| Character state | Add Maki's record/image concern and panic retention, Hare's independent technical curiosity and limits, Kotama's teacher-facing denial/data rhetoric, Yuuka's restraint plus fallible security, printed Eimi's concrete work/report/reaction, and Chihiro's ethics correction. §4 supplies exact locators. No reconstructed medical state or model promotion. |
| Relationship state | Add Maki→Hare/Kotama different incentives/limited agreement; Chihiro→members correction; Yuuka↔Eimi workflow and false-data reaction; Veritas↔Seminar unauthorized data interaction. Sensei is only imagined audience, not an enacted dyad. |
| School club institution | Add Veritas's contested truth/justice identity, observed member misuse versus vice-presidential defense; Seminar accuracy/fairness self-standard and vulnerable access practice; record publication and unresolved response. No full security audit, policy charter, legally adjudicated privacy claim, or completed restoration. |
| Sensei role and ethics | **Indirect material only:** Maki invokes Sensei's imagined reaction to favorable appearance data, Kotama denies that motive (`:1501:scene:001:u:0031-0033`). No Sensei appearance, choices, actual data viewing, approval, attraction, or knowledge. This cannot become a teacher act or relationship progression. |
| Japanese voice and address | Add §5's secure slogans versus admitted purpose, duty/temptation formulations, specialization limits, ethical shift and rumor epistemics. Preserve all attribution/join warnings, `[USERNAME]` placeholder, and written-only boundary. |
| Motif theme callback | Add measurement/image, truth/falsification, virtual self/material record, freedom/privacy, ability/ethics, copying/rumor, correction without immediate social closure. The school-body joke is not admitted as physiological fact. |
| Claim revision | `BA-C017` **STRENGTHEN locally** on relevant information and control over one's life: others' unauthorized false/public data narrow that control. `BA-C014` **PRESERVE / SCOPED ANALOGY**: access/capacity differs from legitimacy, but the original extra-federal coercion apparatus is not directly retested. `BA-C006` **PRESERVE REJECTED**: student authority corrects student misconduct without printed adult replacement, with real fallibility intact. Sensei legitimacy/restraint families and Alice-specific `BA-C019/C020` receive **PRESERVE / NO DIRECT TEST**. No durable new ID or general cybersecurity claim. |

## 8. Admission, coverage, and remaining debts

**ADMIT_WITH_LIMITS proposed** for exactly the three complete `group` objects. Value is **CORE for the specific Veritas data-ethics/ordinary-peer account**, because omission would produce a materially cleaner but inaccurate institutional portrait. This is a bounded contribution judgment after complete inspection, not a global ranking or event index mutation.

On acceptance, group coverage should record `1501-1503` complete for **Maki, Hare, and Kotama**; `1502-1503` for **Yuuka**; `1503` for **Chihiro/BA_PERSON_CH0160**; and `1502` for **printed Eimi**, with its empty source-person join stated. The sequence's complete inspection is preserved even where a person is absent from a particular episode. Other group and private/profile objects remain unreviewed here. Sensei receives an indirect represented-audience observation, not a direct person appearance. Campus students A/B remain narrow roles with no automatic identity merge.

| Source-gap ID | Actual change and remaining boundary |
|---|---|
| `G01` ordinary/private breadth | Partial reduction through full peer/body-image/curiosity/snack/embarrassment/teasing contexts. No comprehensive private dyads, independent daily-life corpus, or full written persona baseline. |
| `G02` Yuuka decision transfer | Add refusal to exploit authority in a personally tempting records context and a concrete security countercase. Public norm and operational competence are distinguished; no arbitrary private-world rule or complete pilot validation. |
| `G07` chronology | Same-day and several-days internal relations supported; position against main or other side sources unresolved. |
| `G09` attribution | Exact label warnings and Eimi's empty person join added. Zero player branches; hearsay and unknown audiences remain explicit. |
| `G10` performed voice | Unchanged; no acting, acoustic or prosodic evidence. |
| `G12` identity/variant | Preserve Chihiro's actual ID, Eimi's join gap, and local student-role identities. No costume/variant continuity or new person inferred from registry naming. |
| `G13` safety/technical outcome | Publish/retreat/correction are source-bounded actions/reports, not full repair, deleted copies, offender disclosure, policy efficacy or a permanent security guarantee. |

Open questions concern whether Chihiro's corrective norm recurs elsewhere, how Hare's experimental interest is governed, how Maki/Kotama's private self-presentation differs outside this peer audience, and how Yuuka's dignity and institutional safeguards are restored. The story supplies no complete answer. Remaining unread ordinary material stays eligible regardless of whether it develops a large plot.

## 9. Evidence locator map

| Finding | Exact primary route |
|---|---|
| Measurement disappointment and contrasting responses | `BA:group:1501:scene:001:u:0002-0017` with u:0012 caution |
| Retained-record anxiety and privacy grievance | `BA:group:1501:scene:001:u:0018-0024` |
| Veritas ideal, teacher-facing persuasion, drone curiosity, distinct stated aims | `BA:group:1501:scene:001:u:0025-0043` |
| Yuuka's temptation, fairness refusal, office work and default access | `BA:group:1502:scene:001:u:0002-0019` |
| Interception, reported editing rights, flattering/retaliatory false-data proposals | `BA:group:1502:scene:002:u:0002-0026` |
| Counterattack, panic copy, SNS destination | `BA:group:1502:scene:002:u:0027-0036` |
| Observed school-SNS publication and false 100 kg rejection | `BA:group:1502:scene:003:u:0002-0015` |
| Defensive limits, retreat and represented log deletion | `BA:group:1503:scene:001:u:0002-0020` with u:0004 caution |
| Evening reveal and vice-president identification | `BA:group:1503:scene:001:u:0021-0039` with u:0037-0038 caution |
| Explicit privacy ethics correction and apology | `BA:group:1503:scene:001:u:0040-0042` |
| Several-days rumor and reported correction notice | `BA:group:1503:scene:002:u:0002-0010` |

## Integration acceptance — 2026-10-01

[Phase 2 cycle 001](../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md) accepts exactly the source IDs declared above with **ADMIT_WITH_LIMITS**. The cycle owns final ledger, coverage and readiness adjudication; proposals in this reading remain source-facing contribution history. No cross-source chronology or performed-voice evidence is added.
