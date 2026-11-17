---
series: BLUE_ARCHIVE
artifact_type: sequential_deep_reading
scope: GROUP_3401_3403
generation: V1
status: canonical
source_story_ids: ["BA:group:3401", "BA:group:3402", "BA:group:3403"]
source_boundary: "Complete canonical Japanese group objects at electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; 3 scenes, 313 structured utterances including 0 locations, 313 canonical text anchors, 617 raw records, 15 formal choice groups and 18 displayed options"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# BLUE ARCHIVE — GROUP 3401–3403: Kisaki’s morning, projected purpose and frightened children

A complete source-facing reading of 山海経のちょっと特別な朝（１）–（３）. Ordinary pleasure and the wish for private rest are preserved before the rumor plot; witness interpretation, actual public conflict and a bounded repair have different evidential grades.

## 1. Complete source witness

The entire canonical Japanese objects named below, their story/utterance metadata, choice records where present and raw script/control records were inspected. They belong to the pinned source class `group`; no projection bundle, localization, plot synopsis or later franchise knowledge substitutes for the complete sequence. Primary provenance is `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`, ingestion generation `BA_REFRESH_20260928T032248159554Z`. Source routes below are relative to `corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/`.

All use `DB/ScenarioScriptExcelTable1.json`, immutable raw SHA-256 `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`. That actual raw hash was independently checked; the structured witnesses agree. Counts distinguish raw controls, structured utterances, locations and canonical text anchors. **Total: 3 scenes, 313 structured utterances including 0 locations, 313 text anchors, 617 raw records, 15 formal choice groups/18 displayed options.**

| Complete story and title | Canonical route relative to the generation | Counts and canonical SHA-256 |
|---|---|---|
| `BA:group:3401` — `山海経のちょっと特別な朝（１）` | `02_CANONICAL_STORIES/GROUP/CLUB_024_001/EPISODE_001_3401.md` | 1 scenes; 91 utterances/91 text anchors; 184 raw; 0 choices. `2fb1a401fbf16af998871f496e78864d7c8da002dc4710bfa1cf4cdee4292f3a`. |
| `BA:group:3402` — `山海経のちょっと特別な朝（2）` | `02_CANONICAL_STORIES/GROUP/CLUB_024_001/EPISODE_002_3402.md` | 1 scenes; 87 utterances/87 text anchors; 150 raw; 11 choices. `ee245ed577f4b93a84dd3bb2f0f90019051859004310e71979b297c37c68a7c1`. |
| `BA:group:3403` — `山海経のちょっと特別な朝（３）` | `02_CANONICAL_STORIES/GROUP/CLUB_024_001/EPISODE_003_3403.md` | 1 scenes; 135 utterances/135 text anchors; 283 raw; 4 choices. `0f66c9e280bc7fa3af9165f07bfdc44a1af7de0ab6dfa9408297413acd185973`. |

`03_STRUCTURED_DATA/stories.jsonl`, `utterances.jsonl` and `choices.jsonl` retain exact source IDs, selection groups, person/variant joins and `source_record_key` locators. Raw and canonical bytes are not copied into analytical Git. Numeric IDs and folder prefixes are retrieval routes. All story release dates in this packet are null; metadata club joins remain unresolved. The text's actual local club identity, chronology and audiences are addressed below. Exact locators abbreviate only the stated story prefix and scene number.

**ADMIT_WITH_LIMITS accepted in cycle 004** for exactly these complete objects and their pinned written witnesses. This reading changes no shared admission, census, reconstruction status or publication by itself.

## 2. Complete speaking and source mode roster

| Printed source label | Source speaker and person join | Actual objects and utterance modes |
|---|---|---|
| `Narration` (raw ``) | `BA_SPEAKER_NARRATION`; `` | 3402, 3403; narration. |
| `System` (raw ``) | `BA_SPEAKER_SYSTEM`; `` | 3403; system. |
| `先生` (raw ``) | `BA_SPEAKER_SENSEI`; `` (person join unresolved) | 3402, 3403; sensei_internal. |
| `京劇部員` (raw `경극부 부원`) | `BA_SPEAKER_UACBD_UADF9_UBD80_UBD80_UC6D0`; `` (person join unresolved) | 3401; dialogue. |
| `京劇部員たち` (raw `경극부 부원들`) | `BA_SPEAKER_UACBD_UADF9_UBD80_UBD80_UC6D0_UB4E4`; `` (person join unresolved) | 3401; character_narration. |
| `レイジョ` (raw `레이죠`) | `BA_SPEAKER_UB808_UC774_UC8E0`; `BA_PERSON_REIZYO` | 3401, 3403; character_narration, dialogue. |
| `ルミ` (raw `루미`) | `BA_SPEAKER_UB8E8_UBBF8`; `BA_PERSON_CH0135` | 3401, 3403; dialogue. |
| `梅花園の園児たち` (raw `매화원 원생들`) | `BA_SPEAKER_UB9E4_UD654_UC6D0_UC6D0_UC0DD_UB4E4`; `` (person join unresolved) | 3403; character_narration. |
| `梅花園の園児たち` (raw `매화원 학생들`) | `BA_SPEAKER_UB9E4_UD654_UC6D0_UD559_UC0DD_UB4E4`; `` (person join unresolved) | 3403; character_narration. |
| `武術研究部員` (raw `무술연구부 부원`) | `BA_SPEAKER_UBB34_UC220_UC5F0_UAD6C_UBD80_UBD80_UC6D0`; `` (person join unresolved) | 3401; dialogue. |
| `ミナ` (raw `미나`) | `BA_SPEAKER_UBBF8_UB098`; `BA_PERSON_CH0138` | 3403; dialogue. |
| `生徒A` (raw `산해경 모브 학생 A`) | `BA_SPEAKER_UC0B0_UD574_UACBD_UBAA8_UBE0C_UD559_UC0DD_A`; `` (person join unresolved) | 3401, 3403; dialogue. |
| `生徒B` (raw `산해경 모브 학생 B`) | `BA_SPEAKER_UC0B0_UD574_UACBD_UBAA8_UBE0C_UD559_UC0DD_B`; `` (person join unresolved) | 3401, 3403; dialogue. |
| `カグヤ` (raw `카구야`) | `BA_SPEAKER_UCE74_UAD6C_UC57C`; `` (person join unresolved) | 3401, 3403; character_narration, dialogue. |
| `ココナ` (raw `코코나`) | `BA_SPEAKER_UCF54_UCF54_UB098`; `BA_PERSON_CH0137` | 3402, 3403; character_narration, dialogue. |
| `キサキ` (raw `키사키`) | `BA_SPEAKER_UD0A4_UC0AC_UD0A4`; `BA_PERSON_CH0139` | 3401, 3402, 3403; character_narration, dialogue. |
| `玄龍門の構成員` (raw `현룡문 부원`) | `BA_SPEAKER_UD604_UB8E1_UBB38_UBD80_UC6D0`; `` (person join unresolved) | 3402; character_narration. |
| `玄龍門の構成員A` (raw `현룡문 부원 A`) | `BA_SPEAKER_UD604_UB8E1_UBB38_UBD80_UC6D0_A`; `` (person join unresolved) | 3403; character_narration, dialogue. |
| `玄龍門の構成員A&B` (raw `현룡문 부원 A&B`) | `BA_SPEAKER_UD604_UB8E1_UBB38_UBD80_UC6D0_A_B`; `` (person join unresolved) | 3403; character_narration. |
| `玄龍門の構成員B` (raw `현룡문 부원 B`) | `BA_SPEAKER_UD604_UB8E1_UBB38_UBD80_UC6D0_B`; `` (person join unresolved) | 3403; character_narration, dialogue. |

Person joins, speaking roles and playable variants are distinct. Empty joins are preserved rather than filled from expected character identity. Mode and local identity cautions below govern how this roster may enter coverage. All inspected raw `VoiceId` fields are zero: the evidence is written Japanese, not performed delivery, pitch, acting or a claim that the game lacks audio.

## 3. Coherent sequence, institutions and priority

The actual local setting is Shanhaijing/`山海経` and `白虎公園`, with Genryumon/`玄龍門`, Genbu/`玄武商会`, the Peking Opera Club/`京劇部`, Martial Arts Research Club/`武術研究部` and Plum Blossom Garden/`梅花園`. Folder `CLUB_024_001` does not authorize a single shared club membership. Kisaki is called `門主`; Rumi is Reijo's commercial-association chair; Kaguya is expressly the opera club director; Kokona gives her Garden educational role (3402 u0021). Directly printed Mina introduces `近衛ミナ` (3403 u0050), with CH0138. Their numeric identifiers do not supply chronology.

The three objects form one rumor-to-meeting sequence: private movement is witnessed and interpreted, Kokona brings the circulating reports, and the planned morning exercise draws competing groups. That causal ordering is local. Kaguya reports an activity-restraint period after `例の事件` (3401 u0024) without naming its exact source event; neither an event ID nor a date can be supplied by familiarity.

**Priority:** high for ordinary/private breadth in Kisaki, Reijo, Kaguya, Rumi, Kokona and Mina, plus a concrete conflict between respectful attention and projection. Its first evidence is pleasurable exercise, a wish to sleep in and freedom from escort—not a crisis test required to justify those experiences. **Functions:** leisure, rumor propagation, hoped-for affiliation, authority performance, children frightened by adult-like peer conduct and a bounded collective repair. **Workflow:** full reading complete; admission proposed pending parent acceptance.

## 4. Complete scene argument

### 3401: solitude, two confident misreadings, and a rumor left uncorrected

Kisaki counts through movements, enjoys exercise and the feeling of freedom without a guard, and likes not being seen (u0001–0005). Early rising is also something that happens to her; she sometimes wishes to sleep late (u0006). These are positive embodied pleasure and a small unmet wish. They are not a public communication or covert training recruitment.

Reijo and Kaguya observe the same movement through different interests. Reijo calls it kung fu and rejoices at finding an unlikely comrade. She openly dislikes Genryumon's noise, discourtesy and self-law attitude, while making Kisaki a qualified exception who can understand and support them (u0009–0011/u0016–0023). Both criticism and affectionate exception are her testimony, not an audited institution-wide conduct finding.

Kaguya interprets movement as opera practice and a response to loyalty (u0012–0015/u0024–0030). She fears her club might have been abandoned after a restriction; Kisaki's exercise becomes imagined assurance that they can perform openly again. No actual restriction is rescinded, and Kisaki has said nothing to that effect. The observation is real enough to produce a belief; the purpose and sanction status are projected.

When Reijo tells Rumi, Rumi doubts privately that Kisaki has a kung-fu interest but chooses not to correct the delighted reporter (u0031–0039). Reijo seeks wider martial companionship (u0040–0044). Rumi values her energy and contemplates sending Kisaki snacks if the report is true (u0045–0049). Warmth, skepticism and nonintervention coexist. The snack is a prospective offer, not a delivered gift. Rumi's silence is consequential to the local information chain without proving responsibility for every later rumor.

Opera members question distant observation and how Kisaki would know their unique dance. Kaguya insists her eyes are reliable, invokes Kisaki's supposed all-knowing nature, then says some movements need instruction (u0050–0065). The distance admission at u0052 is canonically a member but raw text-bearing Kaguya. Authority reverence substitutes for checking purpose; “all-knowing” is her assertion, not evidence of omniscience.

Anonymous students discuss the spreading exercise story and possible harm to Kisaki's standing (u0066–0069). Martial researchers ask Reijo for help and invite her to join, but she declines membership because of association work while accepting cooperation and instruction (u0070–0082). Enthusiasm does not dissolve commitments. Kaguya gathers opera members at the park to show reverence and their dance (u0083–0091). These are separate organizational mobilizations around an intention Kisaki has not voiced.

### 3402: life beyond work, joke and rumor, then a voluntary children's commitment

Sensei arrives as Kisaki says the day's work is finished. She explains efficient use of limited time and says people do not live in order to work (u0001–0008). She does not simply hate her role: someone must do necessary tasks, so she finishes them efficiently. Her remarks about workaholics and an incompetent busy superior are general propositions in her dialogue, not a diagnosis of a named colleague. Rest in her private room may give the organization rest too (u0009–0015). Personal relief and administrative restraint become compatible ideas.

Kokona interrupts despite a constituent's boundary warning, then apologizes for the breach and formally introduces herself as a first-year Garden educational member (u0017–0021). She scolds Sensei for taking precious time, while Kisaki permits the visit (u0022–0024). Her concern does not reflect Kisaki's own prohibition; the scene distinguishes outsiders' interpretations of the ruler's time from its holder's wishes.

The question concerns `ばんざい体操` and expanding rumors. Secret height-extension methods, Saya's alleged requests, Genbu's purported secret recipe and an underground sealed “something” that would make the school strongest appear as **Kokona's accounts of rumor** (u0026–0042). They are not inspected requests, observed cuisine, a released entity, demonstrated physiological effects or proof of power over Genbu. Kisaki says rumors remain rumors, then explicitly states another reason for her exercise (u0043/u0048–0049).

Sensei's probing choices lead into a teasing exchange. Kisaki leaves room to hope for growth but rejects being characterized as believing exercise automatically makes her taller, asks what sort of student Sensei thinks she is, then says she teased too much and apologizes (u0051–0060). The written joke cannot be flattened into an actual growth treatment, cruel punishment or complete denial of wanting to be taller. The apology is a local repair of excess teasing.

Kokona is still present and relays a second, expressly uncertain report: kung-fu and opera partisans are in a hidden dispute (u0061–0068). Kisaki's parenthetical worry follows (u0069–0070). The next episode will directly depict the conflict; that later depiction does not turn all the other height and underground rumors true.

Kokona requests participation for herself and the Garden children, having stopped the exercise after hearing it did not affect height (u0071–0074). Kisaki accepts for the children as Shanhaijing's future (u0077–0080). This is a commitment she herself makes, distinct from the earlier unrequested specialist accompaniment. Sensei's general health praise is a scripted claim, not practical health guidance. When Kisaki extends the invitation, she also says the adult cannot escape and should not look so gloomy; narration establishes they are to exercise together (u0081–0087). Agreement for children does not imply unrestricted privacy relinquishment to every arriving group.

### 3403: specialist pride frightens children, and protection itself has an effect to repair

The meeting directly exceeds the planned Garden exercise. Reijo and Kaguya announce incompatible accompaniment/instruction, argue that their eyes establish Kisaki's practice and make their own lifetime effort depend on being correct (u0006–0039). The initial apparent speaker reversals at u0017–0021 are derived display/text seams, not evidence that the two suddenly exchange beliefs. Each frames the shared movement through her own craft. Their private near-insults show restrained rivalry without a spoken insult at those exact units (u0032/u0037).

Kisaki directly says it is neither (u0042), but more people arrive. Mina uses a dramatic quotation, declares herself wherever Kisaki is, and offers loyalty regardless of kung fu/opera (u0049–0055). Two constituents comment that no one has fallen, consider photographing Kisaki's cuteness and discuss a 5,000-yen sharing price (u0051–0061). These jokes depict subordinate interests beyond uniform loyalty. They do not establish completed image sale, permission to photograph or actual fallen casualties. Mina's order for quiet is canonically constituentA at u0060 but raw text-bearing Mina.

Rumi arrives and again plans a nutritious snack (u0062–0063). Kisaki thanks Sensei for averting a near-faint at u0065, but the exact assistance is not narrated. Do not invent catching, medical intervention or a rescue operation. Sensei's choices encourage meeting the crowd's expectation; Kisaki says those three's expectation need not be met (u0066–0072). Her specific resistance limits the adult's broad suggestion.

Reijo and Kaguya propose force when words fail (u0073–0077). Kisaki restates that she came for ordinary exercise with children; u0078 is canonically Kaguya but raw Kisaki. Each competitor absorbs the correction into her own specialty and continues pressing (u0079–0088). They seek Kisaki's participation, yet do not accept her account of what she is doing. No actual fight is printed.

The children and Kokona express fear (u0089–0091). Kisaki orders the dispute to stop, says she respects the participants' wishes but not imposing them at children's expense, and asks them to judge their aspiration against the school's future (u0093–0099). The response is not mere authoritarian rejection of craft. She offers Genryumon protection for aspirations that nourish children and warns of proper measures if they harm them (u0102–0104). These are conditional commitments, not punishments enacted or a full policy code.

Apologies follow from the disputants (u0101/u0106–0107). Rumi says enough, since the children are also frightened (u0108 raw Rumi/canonical Kisaki). Kisaki then addresses their tears and apologizes for raising her voice (u0110–0113). Protection and its intimidating delivery are both recognized within the story. An account of flawless calming leadership would miss this self-correction.

Sensei's handkerchief offer prompts Kokona's dignity/address correction: she insists she is a lady and should be called instructor, not `ちゃん`; the formal choice accepts `ココナ教官` (u0114–0116/choice003). The offer is tagged `sensei_internal`, so audible dialogue/actual transfer must remain qualified. Kokona's expressed preference and the authored addressed response are nevertheless secure textual objects.

Rumi proposes shared exercise; Mina joins enthusiastically while constituents wonder what preparation means. Kisaki acknowledges that such a day is sometimes needed and begins it (u0117–0128). She loses the initial solitude, but also chooses the collective moment after objections and repair. Sensei's attempt to leave is again restrained in the closing exchange (u0129–0131/choice004). Narration affirms a lively start, but its final “number increased or perhaps did not” is explicitly rumor-like and hedged (u0132–0134). Do not claim verified attendance growth, enduring health benefit, resumed opera permission or ended rivalry.

## 5. Ordinary value, directed relations and counterreadings

A ruler's exercise may be simply enjoyable. Kisaki's pleasure, sleep-in wish and efficient work/rest distinction have value even if nobody later misreads them. The story exposes the difficulty of having those wishes interpreted as an office signal. It also makes a group morning possible without proving the ruler wanted every intrusion.

Reijo seeks craft companionship and retains respect for a criticizable institution's leader; Kaguya seeks non-abandonment and a place for her art; Rumi offers pragmatic affection while avoiding correction; Mina brings theatrical loyalty; Kokona seeks shared activity, then articulates fear and a professional form of address. Each motive is locally specific. No one becomes only “rumor spreader,” “loyal subordinate” or “protective ruler.”

Directed relations include Kisaki → herself private rest/exercise; Reijo → Rumi excited disclosure / Rumi → Reijo withheld correction; researchers → Reijo accepted cooperation/refused membership; Kaguya → peers reassurance founded on inference; Kokona → Kisaki voluntary children's request; Kisaki → children promised participation and protective intervention/apology; Rumi → group de-escalation; Sensei → Kokona addressed acknowledgment; Mina → Kisaki loyalty. These are different acts, not one reciprocal relationship.

**Counterreadings:** Rumi's snacks and tolerance show warmth but do not make the rumor accurate. Kisaki's intervention really interrupts escalation and draws apologies, while her loudness still frightens children. Reijo/Kaguya actually care about their disciplines and recognition, but the interests distort interpretation. Collective exercise really begins in the narrative; the final participation trend remains unconfirmed. Kisaki's permission for Garden participation is clear, while initial private solitude and later refusal of the three specialists' expectations remain equally clear.

## 6. Exact controls, choices, modes and identity limits

**15 display/text actor discrepancies** are listed below. Offsets mean `DB/ScenarioScriptExcelTable1.json:DataList[index]` / structured `source_record_index`, not upstream `Id`. Preserve the locked canonical label and qualify person-level evidence by the text-bearing command; this is a derived attribution limit, not automatically an upstream source error.

| Exact object/scene/anchor and DataList offset | Earlier display command | Text-bearing command |
|---|---|---|
| `3401:s1:u0031 / 110666` | `5;레이죠;03` | `1;루미;02;…` |
| `3401:s1:u0052 / 110699` | `5;경극부 부원;06` | `3;카구야;10;…` |
| `3402:s1:u0066 / 110880` | `1;코코나;02` | `3;키사키;10;…` |
| `3403:s1:u0017 / 110958` | `1;카구야;05` | `5;레이죠;05;…` |
| `3403:s1:u0018 / 110959` | `5;레이죠;05` | `1;카구야;05;…` |
| `3403:s1:u0020 / 110963` | `1;카구야;05` | `5;레이죠;05;…` |
| `3403:s1:u0021 / 110964` | `5;레이죠;05` | `1;카구야;05;…` |
| `3403:s1:u0051 / 111042` | `4;현룡문 부원 B;04` | `2;현룡문 부원 A;06;…` |
| `3403:s1:u0057 / 111061` | `2;현룡문 부원 A;00` | `4;현룡문 부원 B;02;…` |
| `3403:s1:u0060 / 111064` | `2;현룡문 부원 A;03` | `5;미나;11;…` |
| `3403:s1:u0069 / 111084` | `1;카구야;05` | `5;레이죠;07;…` |
| `3403:s1:u0070 / 111085` | `5;레이죠;07` | `1;카구야;13;…` |
| `3403:s1:u0078 / 111106` | `2;카구야;17` | `5;키사키;10;…` |
| `3403:s1:u0100 / 111140` | `2;카구야;04` | `4;레이죠;04;…` |
| `3403:s1:u0108 / 111156` | `3;키사키;05` | `1;루미;00;…` |


The consequential repairs of interpretation are 3401 u0031 (Rumi's question) and u0052 (Kaguya's distant observation), plus 3403 u0017–0021/u0069–0070 (disputants' actual sides), u0060 (Mina's quiet order), u0078 (Kisaki's purpose), u0100 (Reijo's reply) and u0108 (Rumi's intervention).

There are fifteen formal choice groups/eighteen displayed options: eleven in3402 (three two-option groups and eight single options), four single options in3403. All structured records have `branch_effect_known:false`. In3402, raw110768/110788/110857 hold the paired alternatives; no selection-conditioned response establishes different story outcomes. Do not concatenate paired teacher alternatives or treat fixed single prompts as evidence of free player refusal.

Seven `sensei_internal` units are retained exactly. In3402 u0059/raw110873 and u0067/raw110881, raw Japanese and commands use quoted `[ns]`. In3403 u0003/110919, u0027/110974, u0105/111153, u0114/111167 and u0129/111188, the same control accompanies quoted text, including the handkerchief offer and departure remark that elicit replies. Their parser mode is not silently replaced with spoken dialogue; neither does it establish telepathy or prove those practical offers occurred only in private thought. Teacher action claims must name this audience/mode debt.

Other parenthetical lines—Rumi3401 u0039, Kisaki3402 u0069–0070, Kaguya/Reijo3403 u0032/u0037—are structurally dialogue but private-style wording. Group `#na` lines, including children and `A&B` replies, are not separate biographies. Kisaki's conditional warning at3403 u0104 is character-narration, not an executed sanction.

Kaguya prints full `漆原カグヤ` yet has an empty person join; retain a source-local named identity without manufacturing a metadata/person crosswalk. Reijo prints `鹿山レイジョ` (3403 u0012) and retains REIZYO, not the earlier unnamed Shanhaijing chief. Mina/CH0138 is directly named here; no prior generic Genryumon executive is retrospectively merged merely by office. KisakiCH0139, KokonaCH0137 and RumiCH0135 preserve their joins. Anonymous opera/research/Genryumon/student roles and collective Garden children retain local scope, not cross-event human identity. All voice evidence remains written Japanese.

## 7. Main baseline and all seven ledger proposals

The [V100 C002 checkpoint](../MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C002_CHECKPOINT.md), section2 E006–E012, distinguishes Kisaki's named gate-master intervention and Shanhaijing evacuation from a complete local outcome. The analytical coverage index similarly has thin private breadth for that office and a title/self-address limit for unnamed Genryumon roles. This packet adds an independently read ordinary morning; it does not locate it before/after the crisis or settle anonymous executive identity. Existing EVENT80000 E120/E121 observations of Kisaki and Reijo remain independent evidence at their own pin/locators.

| Ledger | Proposed exact addition | Boundary |
|---|---|---|
| [Character](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md) | Kisaki: solitary pleasure, wish to sleep late, work/rest ethic, playful apology, protected children and loudness apology (3401 u0001–0006;3402 u0003–0015/u0060;3403 u0093–0113). Reijo: companionship, Genryumon criticism/exception, declined membership and projected expertise. Rumi: affection plus withheld correction/intervention. Kokona: activity wish/fear/dignity. Mina: direct named loyalty. Kaguya: named unjoined art/loyalty/inference sample. | No operational model or automatic title/person merge. Motive and effectiveness remain distinct; ordinary value not conditioned on crisis utility. |
| [Relationship](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_RELATIONSHIP_STATE_LEDGER.md) | Add directed evidence in section5, with refusal respected by researchers (3401 u0080–0082), Kisaki purpose overridden by specialists (3403 u0078–0088), protection/apology and Rumi intervention (u0093–0113). | No universal loyalty, permanent rivalry cessation, unqualified consent to visibility or accepted photographic sale. |
| [Institution](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SCHOOL_CLUB_INSTITUTION_LEDGER.md) | Actual multiple institutions, Kaguya's reported activity restraint, Genryumon conditional protection and children-as-future language; separate commercial work from invited research membership. | Restriction rescission inferred by Kaguya is not enacted. No verified legal self-rule, sanctions, height projects or strongest-school mechanism. |
| [Sensei](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md) | Visits/rest talk, rumor-probing/teasing exchange, broad crowd-expectation suggestion that Kisaki limits, qualified comfort/address repair and reluctant participation (3402 choices;3403 choices001–004/u0114). | No sole-cause conflict solution, demonstrated catching/medical rescue or guaranteed audible inward-tagged prompts. |
| [Japanese](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md) | Kisaki `妾／其方／じゃ` with marked private/playful/public shifts, `門主` versus personal names; Reijo/Kaguya craft rhetoric and suppressed insults; Kokona `教官` correction; Mina dramatic quotation; exact raw actor/mode receipts. | Written register only; Japanese ruby segmentation and [ns] modes cannot establish performed delivery or universal competence. |
| [Motif/theme](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_MOTIF_THEME_AND_CALLBACK_LEDGER.md) | Leisure converted into public sign; interested observation becomes rumor; institutional dignity versus personal wish; protecting children and apologizing for the means; collective activity without verified trend. | Exercise not intrinsically a secret craft/policy. Role interests do not prove every rumor true or every expression manipulative. |
| [Claim revision](../../03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CLAIM_REVISION_LEDGER.md) | BA-C001/C016: scoped student wishes/peer agency and fallible assistance; BA-C008: observed movements ≠ specialist purpose ≠ rumor ≠ conditional policy ≠ hedged trend. BA-C017: local refusal/visibility and respectful address comparison. | BA-C005/C006 remain rejected. BA-C007 has a limited visiting/listening/pressure instance, not a Schale legitimacy proof; BA-C009/C015/C018/C019 receive no new chapter adjudication. |

## 8. Coverage, source-gap impact and readiness

The [contextual index](../../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CONTEXTUAL_CHARACTER_COVERAGE_INDEX.md) can receive these three complete objects for Kisaki, Reijo, Rumi, Kokona and directly named Mina, plus source-local named Kaguya with an unresolved join. [Analytical coverage](../../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) should preserve existing main states and separate named/generic identities. Anonymous role buckets must be counted locally; collective child/club/A&B responses are not invented individuals. Parent acceptance owns the eventual exact census.

For the [gap register](../../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md), narrow **G01/G06** for private wishes, craft companionship, familial educational care and multi-institution ordinary relations. **G07** keeps unknown event/date placement and unnamed prior incident; **G09** keeps fifteen actor seams, seven [ns] modes, private parentheses and alternative choices; **G10** performed voice remains absent; **G12** retains Kaguya's unjoined named identity, Mina/unnamed chief distinction and collective roles; **G13** retains unverified institution rules, rumor claims, photography outcome, actual effects and participation trend. The other named priority gaps receive no closure from this morning.

Observed mechanism: reverence and craft enthusiasm make witnesses confident about a purpose they have not asked its holder to confirm. Respect for those aspirations can coexist with an enforceable limit when children are frightened, followed by apology for protective loudness. Reconstruction requires additional quiet contexts, actual refusals and distinct institutional results. The entire local outcome is known to this reader: **NO_DIAGNOSTIC_OPPORTUNITY**. Neither a global leadership invariant nor a forecast of stronger attendance is admitted.

## Parent acceptance — cycle 004

[Cycle004](../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_004_CHECKPOINT.md) accepts exactly the declared complete group objects after full contributor primary inspection, parent review of the complete delivered argument, actual canonical-hash verification and consequential Japanese/raw/choice tests. All seven ledger effects and coverage/gap limits are reconciled by that cycle. Earlier proposal wording records the handoff and is not current pending admission. Accepted priority is **HIGH**: Kisaki wants solitude, exercise, freedom and sleep; Reijo and Kaguya value craft. Child fear, apologies, rumor interruption and restrictions preserve conflicting experiences; attendance remains expressly hedged. Priority controls review order; every group object is required. Independent vignette-local roles remain separate even when their generic labels match. Private-source availability, narrative chronology, written attribution and unprinted outcomes remain bounded; no operational model, performed voice, retrospective forecast validation or main-history replacement follows.
