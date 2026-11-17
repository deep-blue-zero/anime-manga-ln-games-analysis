---
series: BLUE_ARCHIVE
artifact_type: sequential_deep_reading
scope: GROUP_2101_2102
generation: V1
source_story_ids: ["BA:group:2101", "BA:group:2102"]
status: canonical
source_boundary: "Complete canonical Japanese group stories BA:group:2101 and BA:group:2102 at electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; four scenes, 222 structured utterances including three location units, 219 canonical text anchors, zero choice groups; no other supplemental source admitted by this reading"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Abydos committee group story deep reading

## Calling people to stay and making ordinary work answerable

The complete two-part sequence, `呼ばれた人は残ってください（１）` and `呼ばれた人は残ってください（２）`, expands Abydos from an institution surviving spectacular coercion into a peer group that must organize paid work, recognize another member's labor, enjoy one another's company, and bear responsibility for mundane errors. The strongest local thesis is that **mutual concern does not ensure reliable cooperation: the group sincerely wants to help Ayane, but confidence, figurative interpretation, and incomplete checking turn that intention into additional administrative and financial work for her**. Ayane's planned snacks and drinks are positive evidence of desired conviviality, not merely a device for measuring combat failure.

This reading inspects both complete canonical objects. It proposes their scoped admission for peer routine, work, care, written register, comic violence, and institutional accountability. It supplies neither a placement between main-story chapters nor a character reconstruction model. The final main-story states remain those established by the [V001 C003 checkpoint](../MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C003_CHECKPOINT.md), alongside the separately preserved [C002 checkpoint](../MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C002_CHECKPOINT.md).

## 1. Source witness and complete inspection

The source root is the pinned ingestion generation `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/`. Its manifest names `electricgoat/ba-data`, branch `jp`, commit `a038020f1f5ac02dcfe76962426d38f86414cdd8`, game version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, and parser `0.2.0`. The source-facing reading uses Japanese canonical text, not a character projection, translation, franchise memory, or plot summary.

| Complete source object | Canonical path relative to that generation | Inspection and source records |
|---|---|---|
| `BA:group:2101`, raw group `2101` | `02_CANONICAL_STORIES/GROUP/CLUB_011_001/EPISODE_001_2101.md` | Both scenes complete: scene 001 `u:0001-0082`, scene 002 `u:0001-0030`; 112 structured utterances, including two rendered location units; 110 canonical text anchors; 140 raw records; zero choice groups. |
| `BA:group:2102`, raw group `2102` | `02_CANONICAL_STORIES/GROUP/CLUB_011_001/EPISODE_002_2102.md` | Both scenes complete: scene 001 `u:0001-0028`, scene 002 `u:0001-0082`; 110 structured utterances, including one rendered location unit; 109 canonical text anchors; 123 raw records; zero choice groups. |

The shared raw table is `DB/ScenarioScriptExcelTable1.json`, SHA-256 `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`. Per-utterance records in `03_STRUCTURED_DATA/utterances.jsonl` retain `source_record_key`, raw Korean speaker label, normalized Japanese label, text, raw group, commit, and table hash. For example, `BA:group:2102:scene:002:u:0053` routes to `ScenarioScriptExcelTable1.json:DataList[105172]`; its anomalous Ayane label is present in the structured witness, not repaired here. `03_STRUCTURED_DATA/stories.jsonl` supplies the two canonical paths and their `source_type=group` classifications. Canonical file SHA-256 values at inspection are `f46c86fae0e12b8182075d878f5085dd9e0710b2af672acb20c7d0949d962d4b` for part 1 and `666b631848466531c25c3cd4464dcacd97ab85ded9242d080dba3c5e30b5eaa1` for part 2. Raw acquisition files remain outside analytical Git.

The numeric path's `CLUB_011_001` is a source route, not an independently resolved club identity. Metadata still records `club_id_resolved=null` and `unresolved_pending_participant_membership_audit`. The text itself identifies the Countermeasures Committee, its classroom, and the five familiar members, making the local institutional identification secure without silently resolving the entire club taxonomy. Person IDs are `BA_PERSON_AYANE`, `BA_PERSON_HOSHINO`, `BA_PERSON_NONOMI`, `BA_PERSON_SERIKA`, and `BA_PERSON_SHIROKO`; this source does not establish swimsuit or other playable-variant conditions. Its one Shiroko is the committee member in this scene; no counterpart appearance is printed.

## 2. Chronology and knowledge boundaries

`00_MANIFESTS/RELEASE_CHRONOLOGY.csv` gives both stories no release date and `story_chronology_confidence=unresolved`. Their numbers establish the documentary route. They do not establish where the sequence falls against C002's refused student-council presidency or C003's accepted presidency.

The sequence has its own supported relative order. Part 1 opens with four students walking toward their cleaning job; its narration explicitly moves back one day to the committee classroom (`:2101:scene:001:u:0020`). The discussion there produces the cleaning assignment. The students later report that Ayane is resting and return to their present journey (`u:0056-0082`). Part 2 alternates the working group's interpretation of the job with Ayane's recovery, message receipt, preparations, and calls. Quoted messages connect those strands, but the text does not timestamp every cut. The return and classroom confrontation follow the damage reports (`:2102:scene:002:u:0049-0082`).

Thus **local before/after relations are supported; inter-source development order remains OPEN**. Familiar behavior in this unordered group scene may broaden a situated repertoire. It cannot prove regression after C003, pre-C002 habits, Hoshino's lasting recovery, or a transition in council office. Ayane's private worry and snack plan initially belong to her and the audience, not to the absent working group. Her communication of instructions does not transmit the students' hidden interpretation back to her.

## 3. Narrative reconstruction

Serika complains about heat and distance as the group walks. Nonomi reports that their map has taken them roughly thirty kilometers, while Shiroko starts to treat that distance as ordinary and Hoshino performs age-related discomfort. Serika corrects them and reluctantly includes herself in the cause of Ayane's anger (`:2101:scene:001:u:0002-0019`). The distance is a character estimate, not measured travel data.

The previous day's committee meeting had requested future activity plans. Hoshino submits a lottery scheme, Shiroko an abduction/forced-transfer scheme, Nonomi a weekend picnic, and Serika an investment brochure for implausible renewable oil farming. Ayane's prolonged silence escalates into an outburst; paid gym cleaning becomes her concrete alternative to such plans (`u:0020-0078`). Ayane is now unwell and absent. The four arrive at an illegally altered gym occupied by threatening thugs. The seniors interpret cleaning its garbage as removing villains and begin fighting (`:2101:scene:002:u:0002-0030`).

Meanwhile Ayane feels guilty about not attending, tries to maintain the requirement that others do their share, and plans to welcome them with refreshments. Hoshino's quoted message reports arrival and requests permission to stop early; Ayane, understanding ordinary cleaning, sends an instruction to finish. The workers understand the reply as confirmation of continuing combat and frame perseverance as friendship (`:2102:scene:001:u:0001-0028; scene:002:u:0002-0017`).

Ayane buys snacks and drinks. A first caller, whose words are not printed independently, apparently reports nonarrival and a penalty; a second, explicitly labeled facility manager, reports drone destruction of a different gym, shared responsibility, and an intended apportioned damages claim. The group returns, acknowledges the wrong gym and explosive miscalculation, and faces Ayane. Serika tries to manage the apology. Ayane orders everyone except Serika to remain; the reversal resolves the title's suspense but does not print the subsequent disciplinary conversation, payment, injury outcome, or reconciliation (`:2102:scene:002:u:0018-0082`).

## 4. Scene argument

### 4.1 Planning exposes different wishes, including pleasure

The four proposals disclose distinct ways of responding to an institution under pressure. Hoshino offers a spectacular financial shortcut; Shiroko offers a technically elaborated coercive recruitment solution; Serika trusts promotional certainty while aiming at useful earnings. Nonomi's picnic, however, states a desire for everyone to gain mental breathing room (`:2101:scene:001:u:0035-0038,0058`). It is a proposal for a form of life, not simply failure to discuss debt. The committee's administrative demand makes it poorly timed, but does not discredit leisure itself.

The reading should preserve both assessments: Ayane reasonably needs actionable work, and Nonomi reasonably values shared recreation. No picnic occurs in this sequence, and neither the plan's feasibility nor everyone's assent is shown. Its literary contribution is the group's capacity to imagine enjoyment together, even while comic incompatibility defeats that particular proposal.

Serika's moral position is deliberately fallible. She accurately identifies the seniors' mismatch with the activity-planning request, then discovers that her own apparently serious plan also fails scrutiny (`u:0040-0052`). `ポンジー石油` creates conspicuous comic suspicion around a promised sure profit, but the text prints no actual investment, identified fraud operator, financial loss, or legal adjudication. Her earnest wish to be useful coexists with inadequate verification. That tension adds more than the label “responsible one” can accommodate.

### 4.2 Care recognizes labor without redistributing it successfully

Nonomi worries that Ayane works too hard alone; Serika links her illness to stress; Hoshino proposes demonstrating that they can manage without her (`:2101:scene:001:u:0073-0079`). Their recognition is meaningful. Hoshino's motive is not simply escaping work: she says she really does want to show they can do it, then immediately asks to be carried. The comic register keeps effort and evasiveness together instead of revealing one as the hidden truth of the other.

Serika's stress explanation is a peer's interpretation. Part 2 directly supplies Ayane's headache and subsiding fever, but no clinical cause (`:2102:scene:001:u:0001-0002`). Ayane herself is torn between guilt over absence and the need for others to act responsibly (`u:0007-0016`). Her eventual refreshments are prepared materially, not merely imagined (`scene:002:u:0018-0021`). Care here involves wanting the workers to feel welcomed; their enjoyment is anticipated, not shown as consummated. The unanswered possibility of a pleasant return is part of the ending's loss.

### 4.3 Shared language conceals different tasks

The pivotal error is not an explicit malicious order from Ayane. Her assignment is ordinary gym garbage cleaning for the next day's festival (`:2101:scene:001:u:0070-0072; scene:002:u:0019-0020`). At the wrong site, the group converts the noun `ゴミ` into an enemy classification. Shiroko makes the reinterpretation explicit as `ゴミ掃除（悪党退治）` (`scene:002:u:0027`), and the seniors' mutual agreement reinforces it. Serika expresses repeated uncertainty, but the fighting begins before the task identity is verified.

Hoshino's quoted message requests confirmation of the destination while describing its bad state and demanding labor in terms still compatible with literal cleaning (`:2102:scene:001:u:0022-0026`). It never tells Ayane that they have found an occupied gym or begun combat. Ayane's quoted reply insists on effort and completion (`scene:002:u:0008-0010`); it therefore cannot establish informed authorization to destroy a building. The group mistakes a reply about persistence for a reply about task identity. Their care for Ayane supplies motivational commitment while their incompatible premises remain unchecked.

### 4.4 The climax makes failed work administratively visible

The combat sounds produce comic escalation, but the story does not end with triumphant villain disposal. Calls restore the ordinary job's institutional consequences: the intended gym remains unserved, a different facility has been damaged, and the person handling coordination must hear both complaints (`:2102:scene:002:u:0025-0048`). The manager acknowledges some responsibility on the extremist sports group's side and proposes apportioned liability. That is a speaker's report and intended claim, not a neutral legal ruling or a paid amount.

Hoshino's admission that it was another gym and Shiroko's admission of mistaken drone explosive quantity corroborate substantial error (`u:0055,0060`); they do not independently verify every reported item destroyed. The final fear of Ayane is relational and procedural rather than evidence that physical punishment takes place. Her retained authority can summon and exclude, but the text stops before any sanction is enacted.

The title culminates in a grammatical reversal. Naming Serika first appears to single her out; `以外の皆さん、全員です` then excludes her from the retained group (`u:0073-0082`). This differentiates culpability or treatment without providing Ayane's complete rationale. Serika did participate in the failed expedition, and Ayane did reject her investment plan, so exemption must not be rewritten as total innocence. It may acknowledge her attempted restraint and apology, but that explanation remains an inference.

## 5. Character and directed relationship repertoire

| Subject or direction | Observed addition | Limit and counterevidence |
|---|---|---|
| Ayane | Arranges paid work, experiences guilt when illness prevents attendance, holds the expectation that peers act, and prepares a welcoming return; administrative authority culminates in selective summons. `:2101:scene:001:u:0066-0078; :2102:scene:001:u:0001-0016; scene:002:u:0018-0048,0073-0081`. | Concern and discipline coexist. Their medical cause, subsequent sanctions, completed liability response, and council office are not established. |
| Serika | Corrects extreme exertion and age jokes, recognizes her own share, wants serious useful activity, accepts responsibility in apology, and tries to stop seniors worsening the confrontation. `:2101:scene:001:u:0003-0019,0040-0052; :2102:scene:002:u:0050-0065`. | Credulity about the brochure and participation in the unverified task prevent an infallible-accountant persona. Final exemption is not complete exoneration. |
| Hoshino | Recognizes Ayane's burden, wants to show collective competence, asks about her health in a message, and keeps languid self-presentation during both work and accountability. `:2101:scene:001:u:0069-0079; :2102:scene:001:u:0022-0026; scene:002:u:0052,0055-0058`. | Concern coexists with lottery shortcuts, incomplete reporting, and desire to excuse the mistake. No placement against crisis recovery or presidency is proven. |
| Nonomi | Values a shared picnic as emotional breathing room, worries about Ayane's solitary effort, and publicly commits to continuing for her. `:2101:scene:001:u:0035-0038,0058,0073; :2102:scene:002:u:0012-0013`. | Playful caretaking does not supply reliable navigation or task verification. The picnic remains a desired experience, not an achieved leisure event. |
| Shiroko | Treats thirty kilometers as comparatively manageable; develops a coercive plan in technical terms; quickly translates cleaning into suppression; later acknowledges a drone explosive error. `:2101:scene:001:u:0007-0009,0030-0034,0057; scene:002:u:0015-0027; :2102:scene:002:u:0005,0060`. | Technical readiness is distinguishable from ethical legitimacy and situational judgment. The story supplies no new solitary-sacrifice episode or counterpart identity. |
| Ayane → Serika | Ayane first scrutinizes Serika along with the seniors, privately addresses hope to her and the seniors, then excludes her from the final summons. `:2101:scene:001:u:0043-0052; :2102:scene:001:u:0007; scene:002:u:0078-0081`. | Hoshino's `ベタベタ`/disappointment account is Hoshino's teasing interpretation, not direct proof of Ayane's exclusive preference (`:2101:scene:001:u:0060-0064`). |
| Serika → Ayane | Serika recognizes strain, tries to maintain the seriousness of the work, restrains the seniors' excuses, and begins with apology rather than denial. `:2101:scene:001:u:0040-0044,0074-0075; :2102:scene:002:u:0061-0065`. | Her knowledge does not prevent the group's error. Reciprocal concern is supported; permanent privileged intimacy, romance, and future reconciliation are not. |
| Seniors → Ayane | They want her recognition and invest effort under an interpretation they believe useful; fear of disappointing her helps drive continuation. `:2101:scene:001:u:0073-0079; :2102:scene:002:u:0011-0016`. | Sincere motive can amplify harm when information is poor. Quoted instructions cannot make Ayane informed author of their combat plan. |
| Committee → outsiders | Threatening occupiers are treated as removable villains; facility complaint makes local civic property and restitution claims visible. `:2101:scene:002:u:0007-0030; :2102:scene:002:u:0039-0048`. | No injuries, fatalities, arrest, legal ownership proof, completed compensation, or final cleanup result is printed. |

## 6. Institution, power, and Sensei

The committee conducts meetings, solicits activity plans, finds paid employment, communicates with clients, and answers a facility manager. Ayane's administrative labor connects these acts. The local crisis is a failure of verification and distributed work inside an affectionate institution; it is not an occasion to replace the students with a competent adult by analytical fiat.

The [C002 checkpoint](../MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C002_CHECKPOINT.md) identifies student governance, differentiated support, and collective participation as substantive competence. This group sequence adds a contrary ordinary case: competence is domain dependent and vulnerable to information mismatch. It complicates an idealized version of that account while preserving the rejection of universal adult dependency. C003's later main-source apology and office acceptance remain valid at their own known boundary; this unordered scene does not reverse them.

Violence has comic narration and exaggerated threats, but the intended damages claim prevents treating it as entirely consequence free. Conversely, no casualties or irreversible bodily outcome justify importing the ethical weight of a death scene. The proportionality problem is specific: a task understood as routine service becomes a building-destroying attack without confirmation of the worksite or authorized aim. The manager's recognition of shared blame also prevents simply converting the complaint into total innocence for the occupiers.

**Sensei has no printed appearance, speech, inward thought, instruction, or choice group in either story.** The group uses a MomoTalk-named application internally, but these are quoted in-story messages; no separate `source_type=momotalk` object is inspected or admitted here. Zero player branches means no choice-space delta. Student action and fallibility are therefore evidenced independently of Sensei; adult restraint, rescue, approval, knowledge, romance, and a completed mentoring response cannot be credited to an absent actor.

## 7. Written Japanese and source-label discipline

The analysis inspects written dialogue, quoted messages, stage sounds, and typography. It makes no claim about performed pitch, timing, breath, acting, or audio delivery.

Ayane's shift from familiar `セリカちゃん` to the full-name `黒見セリカさん` marks a disciplinary turn that Serika immediately notices (`:2101:scene:001:u:0043-0044`). Serika calls it suddenly using `敬語`, although politeness already appears elsewhere; the secure contrast is the heightened formal/full-name address in this context, not a wholly new grammatical capacity. Ayane's repeated ellipses delay response before the emphatic outburst; her private `心を鬼にして、アヤネ` stages self-address that makes strictness effortful (`:2102:scene:001:u:0010`).

Hoshino's `おじさん`, `うへ～`, elongated endings, and age claims persist under discomfort, concern, and accountability. Serika twice refuses the age premise (`:2101:scene:001:u:0010-0011; :2102:scene:002:u:0016-0017`). The age performance is therefore a negotiated group joke, not a literal description or proof of indifference. Nonomi's stars and bright responses accompany both picnic wishes and punitive combat language (`:2101:scene:001:u:0016,0035-0036; scene:002:u:0017,0028`); a cheerful written form does not settle ethical softness.

`ちゃんと`, `仕事`, `掃除`, `範疇`, and `最後まで` link administration to the misunderstanding. The force of the plot lies in shared words carrying incompatible referents. Hoshino's quoted message begins with health concern and shifts to labor limitation; Ayane's quoted response combines insistence with an apology for nonattendance. These are not alternative replies. The closing `呼ばれた人だけ` / `以外` constructs the exemption through delayed qualification rather than retrospective narration.

Three local attributions require quarantine:

| Source locator | Witness and problem | Permitted use |
|---|---|---|
| `BA:group:2102:scene:002:u:0014` | Raw speaker `세리카`, normalized Serika: `アヤネを失望させるわけにはいかない、最後までやり遂げる。` Its terse register may resemble Shiroko elsewhere. | Preserve the printed assignment; do not use resemblance to silently reassign. Ensemble commitment is supported independently by Nonomi's secure preceding lines. Avoid treating this one line as decisive Serika language-baseline evidence. |
| `BA:group:2102:scene:002:u:0015` | Raw speaker `시로코`, normalized Shiroko: `……そうね。ならもう迷うことは無いわ、突撃！！` The diction differs from nearby secure Shiroko lines. | Preserve and flag; no inferred swap with u:0014. The attack continues regardless of exact attribution. |
| `BA:group:2102:scene:002:u:0053` | Raw speaker `아야네`, normalized Ayane: `アヤネちゃんただいま～。` It addresses Ayane as if from a returning member. | Returning-group greeting is contextual inference. Do not assert Ayane greets herself or repair it to Hoshino. Nonomi's secure following return and Hoshino's wrong-gym admission independently establish group arrival. |

The first gym threat has `？？？` and no person ID (`:2101:scene:002:u:0007`); later `チンピラA` and `チンピラB` retain local role labels. The manager is `施設の管理人`, also with no person ID. These role actors may receive source-scoped coverage rows, but must not be merged with earlier generic delinquents or property administrators. The first telephone caller has no independently printed speech, so Ayane's replies alone support a reported notice rather than a new characterized speaking person.

## 8. Counterreadings and bounded behavioral delta

**“Ayane is merely the angry straight character.”** Silence, outburst, final summons, and the group's fear support that comic function. But her private guilt, deliberately difficult insistence, and actual purchase of refreshments supply another dimension: she wants competent shared work and a pleasant return. Removing those passages would flatten both her motive and the ending's interrupted hospitality.

**“The group is only exploiting Ayane.”** Its reliance on her and its return of additional costs support an unequal-labor reading. Against a claim of simple unconcern stand Nonomi's explicit worry, Hoshino's desire to demonstrate competence and health inquiry, collective commitment, and Serika's apology. The strongest mechanism is caring intent combined with poor information and execution, not a secure diagnosis of malicious exploitation.

**“Serika is the sole competent or innocent member.”** Her corrections and exemption make this attractive. The implausible investment, admission of involvement, unsuccessful restraint, and apology prevent that absolute claim. Conversely, exemption does not mean no discernible distinction in her conduct: she repeatedly tries to contain escalation. Her repertoire now includes attempted mediation and fallible judgment in an ordinary peer setting.

**“The seniors knowingly carry out Ayane's punitive combat order.”** Their metaphorical reading makes this an intentional comic inference inside the group. Ayane's literal assignment, limited message information, later surprise, and Hoshino's wrong-gym admission contradict treating it as established authorization. Shiroko's technical readiness did not verify the task; collective agreement did not verify shared knowledge.

**“The joke proves broad student incapacity or post-crisis regression.”** It proves a coherent local failure, with social and material consequences. It does not erase successful main-story governance and offers no chronology needed for a regression claim. Equally, earlier competence cannot be used to dismiss the failure as irrelevant. Both can belong to one institution with changing pressures and domains.

**Behavioral/reconstruction delta:** observed repertoire and one source-bounded failure mechanism are added: incomplete task communication → collectively reinforced interpretation → effort justified as care → additional administrative liability. The sequence is read retrospectively, not held out. No model rule or prediction was frozen before exposure; `NO_DIAGNOSTIC_OPPORTUNITY`. No standalone model, validated general decision rule, prospective success/failure score, or new durable claim ID follows from this packet.

## 9. Proposed seven-ledger deltas and coverage

These deltas are proposals for the integrating owner; this document alone does not declare shared indexes reconciled. Preserve the main-story frontier and historical source witnesses. Append a clearly scoped `GROUP_2101_2102` contextual delta rather than overwriting dated first-pass observations.

| Maintained surface | Proposed delta and evidence |
|---|---|
| [Character state ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md) | Add Ayane's administrative guilt, insistence, and prepared hospitality; Serika's correction, fallible investment judgment, partial responsibility, and mediation; Hoshino's concern plus evasive performance; Nonomi's desired picnic/care; Shiroko's technical action with task-verification failure. Use §5's individual locators. Preserve office/recovery states and do not promote reconstruction readiness. |
| [Relationship state ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_RELATIONSHIP_STATE_LEDGER.md) | Add directed Ayane→Serika scrutiny/exemption and Serika→Ayane accountability; seniors→Ayane concern/recognition-seeking with asymmetric workload; ensemble's unverified agreement. Keep Hoshino's `ベタベタ` as teasing testimony, not relationship fact. `:2101:scene:001:u:0040-0079; :2102:scene:001:u:0007-0016; scene:002:u:0012-0016,0050-0081`. |
| [School club institution ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SCHOOL_CLUB_INSTITUTION_LEDGER.md) | Add meetings, employment procurement, illness-covering, quoted task messages, wrong-site work, and reported penalty/damages claim as an ordinary institutional failure. Do not record a paid claim, a legal award, completed cleanup, full destruction audit, or change in council office. `:2101:scene:001:u:0027-0052,0066-0078; scene:002:u:0019-0030; :2102:scene:002:u:0027-0048,0055-0060`. |
| [Sensei role and ethics ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md) | Record `NO_PRINTED_SENSEI_APPEARANCE` and zero choices across both complete objects. Peer care, initiative, failure, and correction occur without an observed adult intervention; neither rescue nor approval is supplied. Quoted in-story MomoTalk is not separate MomoTalk-class admission. |
| [Japanese voice and address ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md) | Add full-name discipline/familiar care in Ayane, repeated negotiated `おじさん` performance, Serika's corrective and apologetic turns, Nonomi's play/care language, and incompatible meanings of `ゴミ掃除`. Quarantine :2102 scene002 u:0014-0015 and u:0053; retain quote/message versus staged dialogue and written-only limits. See §7. |
| [Motif theme and callback ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_MOTIF_THEME_AND_CALLBACK_LEDGER.md) | Add proposal/work, care/rest, picnic/snacks, literal/metaphorical cleaning, shared words/unshared premises, and title-delayed exemption. Relate ordinary welcome to C002's welcome/reply as a comparison, not a chronology or intentional callback claim. `:2101:scene:001:u:0035-0038,0058,0073-0079; scene:002:u:0019-0030; :2102:scene:001:u:0015-0016; scene:002:u:0018-0024,0073-0082`. |
| [Claim revision ledger](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CLAIM_REVISION_LEDGER.md) | `BA-C006` **PRESERVE REJECTED**, with ordinary failure as a countercase to idealized universal competence rather than proof of adult replacement; `BA-C015` **REVISE / COMPLICATE locally**, because means and liability matter in work as well as crisis; `BA-C017` **STRENGTHEN locally**, distinguishing shared words from relevant shared information and meaningful revision opportunity. `BA-C018` **OPEN for transfer**: refreshments broaden ordinary hospitality, but no consumed welcome or coalition outcome extends its specific Shiba Seki claim. Sensei-specific BA-C001–C004, C007–C011 and intervention-specific C016 receive **PRESERVE / NO DIRECT TEST** here. No new durable claim ID. |

The [coverage index](../../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) has separate rows for **Ayane, Shiroko, Nonomi, Serika, and Hoshino** whose group columns were `ROUTE_NOT_VERIFIED` at the assignment snapshot. On scoped admission, each should become `ANALYZED — BA:group:2101/:2102 complete`, with the remaining group objects explicitly outside this packet. Their main columns, all other source-class columns, model-status assignments, and performed-voice status are not upgraded by it. Sensei's row receives no direct group-person appearance; the complete reading supplies an absence-boundary observation only. Narrow local role actors are proposed for thugs A/B and the facility manager; reconciliation must compare existing role rows before assigning new subject IDs or changing totals.

## 10. Admission decision and remaining debts

**Decision proposed: ADMIT_WITH_LIMITS** for exactly the two complete `group` objects. Their analytical value is **HIGH** for the Abydos ordinary peer/work question: omission would leave Ayane's convivial desire, Serika's nonidealized accountability, and the care/verification failure less visible. This judgment is about what the complete reading contributes. Comic genre and smaller scale have not been used to lower its value. The event priority inventory is not changed, because these are group stories.

| Gap in the [source gap impact register](../../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) | Actual contribution and remaining limitation |
|---|---|
| `G01` ordinary/private breadth | Partially reduce unread peer/routine breadth for these five people. Picnic desire, anticipated refreshments, jokes, illness concern, and minor accountability are affirmative evidence. No private Sensei dyad, completed leisure outing, or full ordinary corpus coverage. |
| `G03` Serika service/peer/reciprocity | Add a complete familiar-group work failure, self-inclusion, apology, and attempted mediation. This does not supply customer interaction, unfamiliar-group response, bond/MomoTalk variants, or a general private persona. |
| `G07` story-world chronology | Record supported internal one-day flashback/assignment/message/return order; retain unresolved placement against C002/C003 and documentary release date. No longitudinal edge is created. |
| `G09` speaker/choice attribution | Add the three exact source-label warnings and distinguish narrated/quoted messages from separate thread objects. Zero choices removes branch ambiguity for this packet only. Generic roles and the first unprinted caller remain narrowly bounded. |
| `G10` performed voice | Unchanged: written Japanese inspected; no audio, timing, breath, or acted delivery inspected. |
| `G11` Hoshino Yume/office | Ordinary concern and languid speech broaden repertoire. They do not authenticate the Yume record, place the scene in an office transition, prove lasting stabilization, or cure grief. |
| `G12` identity/variant | Record no explicit playable-variant condition or counterpart appearance. Do not turn a blank variant field into proof that every main-state variant is excluded or interchangeable. |
| `G13` office/technical outcomes | Add locally corroborated wrong-site and explosive error alongside the manager's reported destruction and intended liability. Payment, sanctions, item audit, injury outcomes, and office status remain unprinted. |

Remaining substantive questions are whether comparable peer scenes show redistribution of Ayane's work, whether Serika's checking and apologetic repertoire recur outside this familiar group, how Nonomi's wishes for ordinary enjoyment are realized elsewhere, and how the committee distinguishes metaphor, authorization, and target verification in other contexts. Those are further reading questions, not frozen predictions. Main-story source witnesses and their earlier epistemic boundaries remain preserved.

## 11. Evidence locator map

All shorthand below expands with the exact `BA:group:2101` or `BA:group:2102` prefix; utterance ranges include the individually preserved canonical anchors. Location-only `u:0001` units are rendered as headings where present.

| Finding | Primary Japanese locator |
|---|---|
| Heat, reported distance, physical baseline, age-performance correction, Serika self-inclusion | `BA:group:2101:scene:001:u:0002-0019` |
| Explicit one-day flashback and activity proposals | `BA:group:2101:scene:001:u:0020-0052` |
| Nonomi's desired shared breathing room and disputed guilt | `BA:group:2101:scene:001:u:0056-0065` |
| Ayane's work assignment, peers' concern, desire to demonstrate competence | `BA:group:2101:scene:001:u:0066-0082` |
| Threatening occupiers and conversion of garbage cleaning into suppression | `BA:group:2101:scene:002:u:0007-0030` |
| Ayane illness, guilt, effortful strictness, planned welcome | `BA:group:2102:scene:001:u:0001-0016` |
| Quoted Hoshino message and bounded information | `BA:group:2102:scene:001:u:0017-0028` |
| Quoted Ayane reply, peer commitment, attribution warnings | `BA:group:2102:scene:002:u:0002-0017` |
| Purchased refreshments and first unprinted caller's apparent notice | `BA:group:2102:scene:002:u:0018-0036` |
| Facility manager's reported damage, shared responsibility, intended claim | `BA:group:2102:scene:002:u:0037-0048` |
| Group return, disputed greeting, wrong-site and explosive admissions | `BA:group:2102:scene:002:u:0049-0060` |
| Serika apology/mediation and title's exemption reversal | `BA:group:2102:scene:002:u:0061-0082` |

## Integration acceptance — 2026-10-01

[Phase 2 cycle 001](../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md) accepts exactly the source IDs declared above with **ADMIT_WITH_LIMITS**. The cycle owns final ledger, coverage and readiness adjudication; proposals in this reading remain source-facing contribution history. No cross-source chronology or performed-voice evidence is added.
