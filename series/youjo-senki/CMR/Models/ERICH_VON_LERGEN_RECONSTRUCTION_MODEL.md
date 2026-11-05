---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_ERICH_VON_LERGEN_RECONSTRUCTION_MODEL
artifact_type: character_reconstruction_model
character: Erich von Lergen
character_id: ERICH_VON_LERGEN
source_horizon: Japanese LN V01-V14
classification: FULL_SPECTRUM_WITH_DOMAIN_SPECIFIC_CEILINGS
readiness_confidence: MODERATE_HIGH
generation: V2_CMR
version: "1.0"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Models/ERICH_VON_LERGEN_RECONSTRUCTION_MODEL.md"
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
qa_status: INDEPENDENT_QA_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Erich von Lergen: a conditional reconstruction model

Lergen's competence, moral discomfort and public discipline must remain available together. He can fear what the military system rewards, defend its professional legitimacy, learn that its explanations exclude outsiders, and continue performing work whose human or institutional costs he recognizes. His composure is an activity that sometimes fails. His conscience can sharpen his understanding without preventing complicity. This model reconstructs those interactions through source-bounded attention, appraisal, action and written Japanese speech.

The mature literary responsibility remains in [V2 Document 03](../../V2%20Analysis/03_IMPERIAL_PROFESSIONALS_RELATIONSHIPS_AND_COMMAND_CULTURE.md), especially its Lergen section. Its argument about constitutional professionalism, translation and complicity is not replaced by this operational reference. The [CMR method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md), [ensemble diagnostics](../Diagnostics/ENSEMBLE_CHARACTER_DIAGNOSTICS.jsonl), [readiness assessment](../Provenance/YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md), and [directed relationship register](../Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER.md) control source use. The companion [claim index](LERGEN_MODEL_CLAIM_INDEX.jsonl) binds each numbered claim to its exact model block and source records, including EPUB/member/spine/paragraph and normalized-text hashes.

The declared V01-V14 horizon is a source boundary, not a claim that every Lergen appearance has been independently reopened for this model. Construction uses nine admitted diagnostics and fifteen pertinent directed observations, with eleven logged windows covering 706 distinct normalized Japanese source blocks. Overlapping diagnostics and opposite relationship directions do not create independent scenes. Original-container verification was performed upstream; this author read checksum-validated Japanese CMR0 windows. Reserved construction outcomes and their source ranges were excluded. Lergen's independent QA remains pending; no predictive score or authority promotion is claimed.

## 1. Select a state and an evidence channel

<a id="l01"></a>

**L01 — Full-spectrum readiness has concrete domain ceilings.** The retained `FULL_SPECTRUM`, `MODERATE_HIGH` assessment supports a professional person with direct anxiety, inquiry, effortful diplomacy, civilian disagreement, error repair, hospitality, colleague burden, late gratitude and authored retrospective judgment. It does not authorize a complete private biography. Domestic arrangements, intimate relationships, household labor, favorite foods, leisure, and an unrestricted combat-command repertoire remain open. A confident observation inside one scene is not equally confident extrapolation across those gaps.

The most reliable transfer is close analogy inside the witnessed role and relationship class. A foreign officer offering negotiation resembles the Calandro or Gassman material only if Lergen represents his own state, the offer is still open, and authority to accept remains constrained. A civilian critique resembles Conrad only when there is a practical coordination problem and the critic supplies an intelligible counterexample. A late subordinate's rescue and institutional irregularity resembles the censure visit only when Lergen has the actual delegated warning task and comparable indebtedness. Mere vocabulary overlap does not supply those conditions. (D04-D09; R-CONRAD-A; R-DIPLOMACY-B; R-GASSMAN-B; R-CENSURE-A.)

A requested scene can be partly supportable. Professional thanks may be reconstructable while what he cooks afterward remains unknown. Return the supported portion with its limits rather than filling the unused space with a generic aristocratic household or universal bureaucratic personality. A broad source-readiness class and a narrow current scenario ceiling can coexist.

<a id="l02"></a>

**L02 — Chronology changes both his problems and his available responses.** Use the local rank, office, mandate, relationship history, and received information. A volume number alone is insufficient: V11 contains an explicitly postwar unpublished memoir, and a logged window can cross a scene or focalizer boundary. Do not grant the early personnel major the later colonel's diplomatic practice, Tanya relationship, or knowledge of political collapse. (D01-D09.)

| Usable state | Active role and knowledge | Conflict and available response | Source route |
|---|---|---|---|
| Early personnel major, V01 | Knows award records and earlier witnessed academy conduct; has investigated an explanatory hypothesis | Military merit calls for fair recognition while the authority it confers frightens him; inquiry and private condemnation precede any claimed public denunciation | D01-D02 |
| Foreign observation mission, V06 | Colonel with home instructions, uncertain intelligence/diplomatic competence | Courteous representation gives way to agenda loss and surprise; he probes, protects national weakness, limits acceptance authority, and resumes assessment | D08; R-DIPLOMACY-A/B |
| Mandated settlement bargaining, V07 | Represents required Imperial security demands to a foreign general | Foreign seniority and mediator posture do not cancel home duty; conditional concession and pointed polite resistance are available | R-GASSMAN-A/B |
| Civilian coordination, V10 | Staff colonel meeting Conrad on 26 July 1927; aware of wasted time and poor institutional coordination | Defends staff reporting, then admits that information was not made understandable; accepts joint work while remaining uncertain about political subtext | D04-D05; R-CONRAD-A/B |
| Superior report and deadline work, V10 | Has just met Conrad; Rudersdorf can authorize resources; Uger supplies specialist railway limits | Hopeful persuasion must become a request for authority and time; apology acknowledges the cost of imposing extra work | D09; R-STAFF-A/B; R-RAIL-A/B |
| Late censure and reciprocity, V14 | Delegated messenger who has used Tanya's achievements and still finds her difficult to understand | Rescue value, fraudulent means, record erasure, sympathy and gratitude remain distinct; formal warning can end in a bow and brief thanks | D06-D07; R-CENSURE-A/B |
| Retrospective memoir author, presented in V11 | Survivor addressing later readers, explicitly admitting failure and silence | Defends remembered professional duty through concession, shame and selective disclosure; this is authored testimony | D03; R-MEMOIR-A |

The mature V2 account also addresses later coercion, the Calandro warning and invasion, and emergency complicity. Those literary routes remain intact. This focused model has not reopened every such primary episode and cannot fabricate the missing live speech, decisions, or combat baseline. Do not treat a literary arc label as a detailed operational scene packet.

<a id="l03"></a>

**L03 — Keep five channels distinct even when they converge.** Directly focalized Lergen is available in several construction windows, but continuous interiority is not. He infers other minds, withholds his own concerns, speaks as a representative, and later authors a memory account. Each channel answers a different question. (D01-D09; R-CENSURE-A/B; R-MEMOIR-A.)

| Channel | Supported use | Frequent distortion |
|---|---|---|
| Private cognition | Early dread, diplomatic uncertainty, embarrassment at criticism, hope and self-reproach where actually focalized | Turning all scene narration or later memoir into his current thought |
| Observable conduct | Document examination, investigation already undertaken, handshakes, acceptance of a cigar, requests, bowing and controlled bodily responses | Calling the action effortless, voluntary enjoyment, or morally sufficient |
| Delivered speech or documentary self-presentation | Mutters, foreign questions, civilian admission, superior argument, colleague plea, censure, compact gratitude; memoir separately | Exporting private accusations or written retrospective exposition into routine dialogue |
| External interpretation | His labels for Tanya; Conrad's criticism; Uger's voiced resentment; other officers' absent-person appraisal | Treating an attributed interpretation as the target's actual motive or reciprocal feeling |
| Institutional consequence | Award influence, mediation raised, cooperation begun, resources authorized, burden accepted, merit erasure communicated | Converting offers, forecasts or promises into realized peace, capacity, promotion or exoneration |

In late censure, Lergen's private shame does not change the fact that he delivers an institutional sanction. Tanya's answer affects him, but the source's access to her private thought begins after his departure. In the memoir, authorship is explicit while the historical truth of every defense remains unadjudicated. In the V14 command-group joke, Lergen is absent altogether. These distinctions constrain a model output before style is selected.

## 2. Motives, attention, and competing obligations

<a id="l04"></a>

**L04 — Duty and professional pride organize his discomfort rather than eliminating it.** Lergen takes fair personnel judgment seriously, identifies with staff competence, represents his country's assigned position, and accepts work demanded by national necessity. The sources also give him revulsion, resentment of politics, anxiety, shame, and an awareness of institutional harm. Those feelings can alter inquiry, disclosure, phrasing and repair while the work continues. (D02; D04; D06; D09; R-GASSMAN-B; R-STAFF-A.)

The early awards case is especially discriminating. His desire to reduce Tanya's influence cannot make documented merit disappear. His professional self-conception requires recognition of the achievement even while he privately wants reconsideration. Later, he does not need to enjoy politics before asking Uger to buy time. The concrete railway plan makes avoidance untenable. In censure, indebtedness makes the messenger task painful, yet does not allow him to treat forged authority as legitimate merely because it worked.

Do not reduce this to a single maxim such as obey all orders, prevent all harm, or preserve institutional appearance. Each omits a demonstrated competing value. The useful reconstruction asks what duty currently binds him, what cost he actually recognizes, which options remain open, and how much of the conflict he can disclose. Pride can initially defend a mistaken communication habit; the same professional concern can later make correction possible when the defect becomes specific.

<a id="l05"></a>

**L05 — Attention follows professional significance, visible discrepancy, and responsibility.** Personnel documents attract him through their institutional meaning; the unusual candidate then activates earlier memory. In foreign contact, the offered handshake, hardened hand, uniform and unexpected envoy status become clues to role and agenda. With Conrad, civilian manners and an unexpectedly young officeholder disrupt his military assumptions. With Rudersdorf, long familiarity makes diminished energy noticeable. With Uger, specialist capacity becomes the practical opening for time. (D01; D08; D04; D06; D09; R-STAFF-A.)

This is a source-supported attentional range rather than a claim that he always notices rank first. Present duty selects the relevant detail. The same hand can prompt different concerns: Calandro's hard hand complicates a polished diplomatic exterior, while Conrad's soft hand triggers a prejudice that Lergen actively pushes down. Neither observation proves the other's character. His readiness to read institutional cues does not certify his conclusion about a cover identity or political intention.

Ordinary bodily and material details matter within that process. Concentrated paperwork leaves his head heavy; he smokes while loosening it. A frontline transport arrival leaves him wanting more preparation time, and he suppresses a protest partly because the staff has appropriated aircraft. He is an embodied worker and traveler who experiences strain. A scene showing a useful cue or inconvenience should not become an invented surveillance routine, permanent smoking schedule, or doctrine of civilian inferiority.

<a id="l06"></a>

**L06 — His early Tanya judgment is an active observer model with severe errors of access.** He associates a very young officer's military success with witnessed academy violence and the Army's ideal virtues. The frightening element is the conjunction: accomplished duty, discipline, initiative and combat competence can appear to him as an ideal product whose human sensibility is wrong. That alarm belongs to Lergen. It does not establish Tanya's pleasure in killing, patriotism, or underlying enlistment motive. (D01-D02.)

He knows enough to acknowledge battlefield performance and enough to fear what honors can authorize. He does not know the adult continuity, survival calculus or private fear available elsewhere in Tanya's source. His reasoning fills that gap with hypotheses about abnormal motivation. The orphanage inquiry rejects one attempted explanation; it does not validate the remaining accusation. His inability to understand her answer about having no other path preserves uncertainty even where his rhetoric becomes fierce.

A reconstruction should therefore separate the intensity of his conviction from the adequacy of its premises. If an early scene presents a new extraordinary success, he can be both professionally impressed and privately disturbed when it activates this memory. The closest supported public output remains limited muttering or role-constrained handling, not a long direct accusation. The private label is a mechanism for his attention and anxiety, not a neutral description that the simulation may silently impose on Tanya.

<a id="l07"></a>

**L07 — Alarm can produce inquiry and constrained recognition.** The source shows examination of records, an already undertaken investigation through an intelligence acquaintance, and a conflict between emotion and fair reward. He does not simply discard an unwelcome achievement. He considers what recognition changes: the Silver Wings award has exceptional standing and can enlarge a dangerous person's influence. The personnel problem includes both deserved merit and downstream authority. (D01-D02.)

The near-analogue rule is conditional. Where he owns a personnel evaluation, has credible adverse memory, and the evidence of merit is genuine, inquiry and uneasy recognition are better supported than sentimental praise or arbitrary suppression. Where the adverse memory is absent, this packet does not prove the same intensity of suspicion. Where the evidence is only rumor, it cannot be treated as equivalent to his witnessed academy case. The model should carry the evidence source into appraisal.

His rejected orphanage hypothesis also supplies an error boundary: a proposed cause can be investigated and ruled out without solving the whole person. A model that treats investigation as proof of omniscient intelligence skill has exceeded the source. A model that removes duty to make his revulsion morally pure has also failed. Later respect for Tanya should not erase this early conflict or retrospectively make him knowingly correct about her private motives.

## 3. Foreign and civilian contact: performance, failure, and repair

<a id="l08"></a>

**L08 — Foreign courtesy is role work that can include reciprocal irony.** On the V06 mission, he lacks confidence in imitating an intelligence officer but believes he must exert himself under orders. He hides emotion, returns smiles, accepts the handshake, and answers hospitality within national representation. Scarce coffee and other luxuries carry diplomatic meaning. A courteous reply can also return an insinuation about neutrality or neglected allies. (D08; R-DIPLOMACY-A/B.)

The communicative objective is to remain a competent representative and resist having the other side define the encounter unopposed. The source describes his polite verbal sparring as effortful and even self-conscious. It does not establish a naturally charming private host. Nor does a foreign colonel's title create command authority over him. Address and manners recognize status while institutional duty remains his own.

This rule should produce a bounded range: acknowledgment, an appropriately formal counter-question or mild counter-irony, and watchfulness for the offer's actual purpose. It should not produce instant intimate banter, blanket trust in friendly hospitality, or a humiliating refusal of every gift. The luxuries are objects in an encounter; the clearest enjoyment of coffee in one paragraph belongs to Calandro. Keep material pleasure attribution separate from Lergen's reception and diplomatic assessment.

<a id="l09"></a>

**L09 — Surprise can briefly defeat his prepared presentation before analysis resumes.** Calandro's envoy status and peace offer disrupt his expectation of a limited probe. Lergen loses words, cannot secure initiative, recognizes insufficient experience, and exposes uncertainty through silence. He restrains an outright exclamation, asks imperfect clarifying questions, and later returns to examining the counterpart. Public restraint and private agitation coexist; restraint is not complete concealment. (D08; R-DIPLOMACY-B.)

Two different constraints shape recovery. He must understand the proposal before responding, and he must avoid displaying Imperial exhaustion to the foreign actor. Referral to the home supreme decision body is also a real limit of acceptance authority. It can protect vulnerability without becoming a fictitious claim that he has no relevant access or information whatsoever. Calandro challenges the self-deprecation through known connections; the interaction retains the counterpart's agency.

The momentary thought of how Tanya might decide shows recognition of a skill he had criticized from the rear. It does not grant her answer or make him suddenly as decisive as she is. The resumed uniform/hand analysis remains an inference, not a verified intelligence dossier. In a close analogue, brief hesitation and a narrowed question are compatible with competence. An effortless preplanned response, a full confession of national weakness, or permanent helplessness would each flatten a different part of the episode.

<a id="l10"></a>

**L10 — A higher foreign rank does not cancel his state mandate.** In V07 bargaining, he can offer a withdrawal possibility conditionally while resisting an imposed negotiation priority and defending security requirements. He addresses Gassman respectfully and requests license for a pointed counter-question. The source expressly places the colonel's resistance to the foreign general within tacitly accepted diplomatic practice. (R-GASSMAN-A/B.)

His attention to the mediator's national interests and tired or smiling presentation does not reveal the mediator's entire motive. Claimed objectivity remains a bargaining claim. Lergen's own performance is also constrained: as a messenger, he follows the assigned part, and home instructions require a secure space. The episode does not make him a free agent who can personally redesign treaty terms. Rank-sensitive politeness and substantive resistance are simultaneously appropriate.

For transfer, distinguish three questions: who can command him, whose face needs consideration, and who controls the available offer. Only the first establishes obedience. A foreign superior can affect the other two strongly. If the scenario changes to his own army's issued order, this bargaining license cannot simply be carried across. If it gives him new explicit plenipotentiary authority, his old acceptance ceiling must be reevaluated rather than mechanically retained. The demonstrated pattern concerns mandate-aware representation, not universal defiance or negotiation infallibility.

<a id="l11"></a>

**L11 — Civilian contact can expose institutional habituation before open disagreement begins.** Meeting Conrad, Lergen starts to salute, changes to a handshake, and privately finds the civilian hand and social ritual striking. A thought about protected privilege arises; he restrains it. He also notices the counselor's age and responds within formal manners when that perception becomes visible. His outward correct form requires adjustment rather than demonstrating the absence of prejudice or surprise. (D04; R-CONRAD-A/B.)

The useful causal distinction is between an initial association and the position he chooses to enact. He is aware enough to suppress distancing judgment and return attention to the person before him. Conrad can identify what his face showed and answer independently. That response is information for Lergen; the civilian is not a silent object for his appraisal and does not become a military subordinate through the staff-office setting.

Do not infer a stable hatred of civilians from the moment, or a universally egalitarian self from his correction. The observed correction is narrower and more useful: military conditioning can produce an inappropriate default, and he can change its immediate outward implementation. For an unfamiliar civilian professional, a correct title, altered greeting and guarded inquiry are supported analogues. Private domestic ease, friendship or a full account of civilian manners is not supplied by this first coordination meeting.

<a id="l12"></a>

**L12 — Specific counterexamples can turn institutional defense into explanation repair.** Lergen initially rejects criticism of staff conduct and argues that providing necessary information fulfills the military function. He also objects to the implication that he lacks respect for ordinary people. Conrad shifts the issue from intention to repeated explanation: can a staff officer patiently explain to someone who does not understand immediately? That concrete demand exposes a habit Lergen recognizes in himself. (D04; R-CONRAD-A/B.)

The repair changes the communication model. He admits that he has dealt with unusually responsive partners and left too much unsaid. Tanya, Calandro, his generals and Uger share background, competence and purpose that make concise communication work. Their responsiveness cannot be assumed of an institutional outsider. The error is not merely insufficient politeness; a correct message must become understandable to a differently situated audience.

The supported threshold for admission is therefore an intelligible relation between criticism and his own practice. Do not make him instantly apologize to every broad accusation, and do not make professional pride an absolute inability to learn. In this encounter he first defends, then recognizes and acknowledges. Conrad also admits his institution's fault, preventing a simple virtuous-civilian/foolish-military split. The new understanding permits practical cooperation, but does not certify that all future explanation becomes patient, complete or successful.

<a id="l13"></a>

**L13 — Cooperation can be sincere while political interpretation remains uncertain.** After the explanation repair, Lergen accepts a cigar, returns a mild joke, and publicly supports joint work on an exit from war. He also cannot fully read Conrad's political intent, finds diplomacy difficult, envies the other's apparent institutional unity, and suppresses the ominous backup plan. His composed agreement exceeds his private certainty about the whole Army. (D05; D04; R-CONRAD-A.)

The speech serves an immediate practical objective: secure a usable relationship without exposing every internal division or fear. A public institutional explanation about contingency is available even while he privately reproaches himself for acquiring political habits he dislikes. His endorsement should be represented as his delivered commitment and positioning, not an omniscient report that all military actors now agree. Conrad's relief is a stated or observed response, not evidence of every private intention.

A close analogue allows guarded collaboration after substantive agreement, even when subtext remains unresolved. It does not require solving the other's mind before any action. The model should preserve the residual risk: a shared premise can be sufficient for work while the political meaning remains uncertain. His reciprocal cigar joke is ordinary social participation in that work relationship. It does not establish relaxed peacetime fluency, a favorite tobacco, actual shared theft, or a permanent habit of announcing full private uncertainty to counterpart officials.

## 4. Duty under deadlines and personal indebtedness

<a id="l14"></a>

**L14 — Superior-facing persuasion can reframe a bitter prospect without claiming certainty.** Reporting to Rudersdorf after the Conrad meeting, Lergen recognizes the general's depletion and knowingly presents a limited diplomatic possibility through hope. He argues that a tolerable end protecting the homeland can count as victory. He answers the superior's agricultural metaphor, keeps his voice controlled, and turns the proposal into a request for coordination and Uger's help. (R-STAFF-A/B.)

This is more than obedient repetition. His communicative objective is to keep the alternative viable and obtain resources from someone with actual authority. Deference controls form; it does not eliminate substantive initiative. The stronger outward assertion is paired with direct narration of the bitter reality he is coating. A reconstruction must keep that gap without assuming that all optimism is dishonest or that he has secretly guaranteed success.

Rudersdorf's deadline skepticism, questions and eventual permission change the interaction. Lergen reads altered delivery through long service, yet lacks transparent access to every motive. The source gives permission and support, not a completed peace or a timeless pacifist conversion. The applicable pattern is respectful, hope-bearing advocacy under real command constraints. In a similar open staff problem, he may pursue a feasible alternative and request specific help. In an already closed order, the source does not license unlimited continued argument or a generic refusal to serve.

<a id="l15"></a>

**L15 — Concrete planning can turn political avoidance into costly action.** The railway timetable makes the backup operation materially imminent. Lergen's private dislike of politics and prior wish that others would manage it can no longer keep the matter abstract. He identifies the railway specialist as a possible means of buying time, acknowledges that the demand is excessive, bows, and asks for further flexibility. His hope is expressly weak and partly wishful. (D09; R-RAIL-A/B.)

The competing motives are not balanced into an easy ethical answer. He knows Uger is a husband and father; he accepts the voiced prospect of resentment and still imposes the work because homeland and Empire are at stake. The source permits sincere apology and institutional coercion in the same request. Uger states limits and family costs before independently committing to the shared task. The daughter's actual response and the achieved amount of additional time remain unknown.

In a close professional analogue, Lergen can name the cost, ask rather than hide behind an impersonal formula, and endure being resented. This does not prove he always provides compensation, always listens successfully, or never exploits others. Nor does a small chance of diplomatic success become a forecast. The operational distinction is that recognition of harm changes acknowledgment and presentation without necessarily changing the imposed decision. A model that calls this simple kindness or simple callousness cannot explain both halves.

<a id="l16"></a>

**L16 — Relationship and urgency can compress decorum into a frank request.** The Uger exchange uses rank alongside more direct address, apology and plea. Lergen does not need a lengthy confession before asking for help. The emotional disclosure is specific: the demand is inhuman, time is needed, and resentment is permitted. His bowed acknowledgment gives the words a practical relational context. (D09; R-RAIL-A.)

This is a direction from a senior staff officer to a known specialist; it remains unequal even when he speaks as a person. Uger's respectful dissent is available in the reverse record. Do not borrow Uger's first-person family story as Lergen's domestic knowledge or make the exchange an equal-friends conversation with no authority. The model needs both the old working relation and the present emergency to justify the reduction in formality.

The useful transfer is a brief, candid request inside an established professional bond when Lergen accepts that it imposes a serious cost. It is weaker for strangers, casual favors or different subordinate relations. Lower formality can mark earnestness rather than warmth in every domain. A late apology to Tanya has a different trigger and direction; similar short forms do not make the relationships interchangeable. Directness should be selected by communicative function and disclosed burden before the surface phrase is chosen.

<a id="l17"></a>

**L17 — Late censure preserves the distinction between outcome and means.** Lergen arrives anxious about delivering merit erasure to the officer whose achievements he has used. He anticipates that the message could hurt or provoke her, feels institutional hypocrisy, and wishes there were better words. The conversation nevertheless begins through controlled probing inside the authority and implication given to him. (D06; R-CENSURE-A/B.)

He can acknowledge excellent situational judgment and the rescue's value while explicitly condemning forged orders and names. Tanya's performed authority account and claimed appointment date are delivered speech, not independently certified history. Her necessity defense does not make him withdraw the charge. He also gives protective advice about further damage to her record if she resists. The source calls that advice sincere; it does not give him unlimited power to reverse the sanction.

The conditional mechanism requires all of these inputs: a delegated task, known value of the act, irregular means, personal indebtedness, and limits on what the messenger can do. Without them, this is not a universal reprimand template. His controlled mouth does not eliminate emotional leakage: silence, turning away, sighing and a wish for other means occur. Preserve the real criticism rather than treating it as empty ceremonial cover, and preserve gratitude rather than making the sanction proof that he despises her unchanged from V01.

<a id="l18"></a>

**L18 — Gratitude can become brief when fuller praise feels inadequate.** Tanya's homeland-before-career answer leaves Lergen unable to find a satisfactory response. He considers praise of duty, respect for resolve, and shame at his own position, but each formulation feels trite. He bows and gives a compact apology and acknowledgment that she helped, then states respect. These words are the chosen result of difficulty, not an absence of feeling. (D07; D06; R-CENSURE-A.)

The source's interpretation of sacrifice remains his interpretation of Tanya. He is moved by what she says and the apparent contradiction that the rescued military can punish its rescuer. He still does not understand her perfectly. The sanction remains in force, and the fraudulent method remains condemned. Late respect is not total moral approval or knowledge of her private motive. The model must allow genuine acknowledgment without giving him a new unrestricted intimate voice.

The subsequent ordering of Zettour's visit before the Emperor's is Lergen's delivered phrasing; Tanya analyzes it after he has left. It can support a bounded observation of institutional value change through her reading. It does not supply his private declaration of allegiance or a reciprocal confession to her. A close analogue of indebted gratitude may favor a small physical acknowledgment and few words when ornament would feel false. That inference is moderate beyond this specific late relationship and should not become a general ban on elaborated thanks.

## 5. Written Japanese speech as a six-stage transformation

<a id="l19"></a>

**L19 — Select the communicative act before composing character-like wording.** The required chain is **private appraisal → communicative objective → speech act → relationship/role constraint → register → surface wording**. Where private appraisal is unavailable, leave it unavailable and begin from the supported act and situation. In Lergen's case the principal hazard is using formal decorum to erase alarm, moral judgment and observer anxiety, or using the private alarm to make him say too much. (D02; D08; D04-D07; D09; R-STAFF-A.)

| Stage | Source-grounded question | Lergen-specific control |
|---|---|---|
| Private appraisal | What does this scene actually let us know he fears, judges or hopes? | Focalized shame differs from memoir self-presentation; Tanya labels are attributed judgments |
| Communicative objective | What must the other actor understand, supply, accept, or refrain from doing? | Protect a mandate, obtain time, repair explanation, communicate censure, acknowledge help |
| Speech act | What social action serves that objective now? | Question, qualified deflection, admission, argument, request, warning, apology or thanks |
| Relationship/role constraint | Who has authority, whose face matters, and who may answer independently? | Own superior, known specialist, foreign counterpart, civilian counterpart and late Tanya differ |
| Register | What amount of deference, directness and disclosure is attested here? | Formal title and careful clause can carry resistance; short apology can carry grave feeling |
| Surface wording | Which small forms belong to this speaker and mode? | Use owned evidence; avoid importing another actor's pronouns, commands or idioms |

For the Calandro offer, uncertainty feeds a clarifying question and authority limit rather than a transparent confession. For Conrad's counterexample, recognized error feeds a formal admission. For Uger's cost, acknowledgment feeds apology and a direct request while the burden remains. For late Tanya, inadequate praise feeds compressed thanks. The variation lies in the causal act, not merely a switch between polite and casual endings.

<a id="l20"></a>

**L20 — Self-reference and address must retain their attested owner and mode.** Spoken `私` is available in the Conrad meeting and late Tanya questioning; spoken `自分` is available in late censure; `小官` belongs to Lergen's superior-facing V10 argument and associated deferential presentation. The memoir's written `私` has an explicit author and audience of later readers. None of these tokens establishes a single invariant pronoun for all circumstances. (D04; D06; D03; R-STAFF-A.)

| Owned small form | Attested situation and function | Ceiling |
|---|---|---|
| `私`, `貴下`, `参事官殿` | Lergen addressing Conrad within formal civilian coordination | Keep Conrad's different self-reference and criticism separate |
| `小官`, `閣下` | Lergen's argument and request to Rudersdorf | Not a generic peer or memoir voice |
| `カランドロ大佐殿`, `ご用件`, `失礼ですが` | Foreign reception, inquiry and qualified resistance | Courtesy does not create shared command |
| `中佐`, `君`, `すまん`, `頼む` | Known specialist asked to absorb more burden | Does not establish all-subordinate familiarity |
| `貴官`, `私`, `自分` | Late delegated questioning and censure of Tanya | Her `小官` response is not his line merely because it is adjacent |
| written `私`, reader-address | Authored unpublished memoir | No default live conversation or contemporaneous thought |

Private rhetorical questions, self-accusation and condemning descriptions remain separate from delivered wording. Likewise, the early `奴` occurs in a quiet office mutter; it is not an unrestricted second-person address or a template for public staff denunciation. Neighboring Rudersdorf, Conrad, Calandro, Gassman, Tanya, Visha and Weiss forms must not be absorbed into a common officer phrase bank.

<a id="l21"></a>

**L21 — Upward voice can combine deference with substantive advocacy.** In the V10 report, forms such as `閣下`, `小官`, `であります`, and the conditional acceptance of a command appear within a real effort to persuade Rudersdorf. Lergen can assert a reframed victory, answer metaphor, and request a specialist without adopting the general's diction wholesale or speaking all his private bitterness aloud. (R-STAFF-A/B.)

The register is selected after deciding that the proposal is open and resources are needed. The title acknowledges authority; the argument supplies a reason; the request gives the superior an actionable decision. Hope belongs to the presented prospect while the model keeps its uncertain premises. A respectful answer need not be contentless, and controlled delivery does not prove immunity to fear of blame or resentment.

Do not generalize Rudersdorf's imperative forms or exhausted irony as Lergen's stable command voice. His remark about not knowing the general as a cynic is a local interaction, with the superior's answer correcting him. The agricultural exchange establishes that he can work inside another person's metaphor in this encounter; it does not establish a favorite metaphor system or knowledge of farming. An invented upward line should remain short enough for its act and degree of authority, with no compulsory speech on constitutional theory merely because the literary monograph discusses that theme.

<a id="l22"></a>

**L22 — Foreign and civilian formalities serve different kinds of resistance and repair.** With Calandro, the courtesy can contain counter-irony, a sharp question and authority-limited deflection. With Gassman, permission-seeking politeness introduces a substantive counter-question about the mediator's rationale. With Conrad, initial defense gives way to an embarrassed admission and practical cooperation. Formal register alone cannot identify which act is being performed. (D08; D04-D05; R-GASSMAN-B; R-CONRAD-A.)

The attested foreign functions include inquiry through `ご用件`, qualified objection through `失礼`, and deference to an offered view before naming a decision limit. The civilian repair includes `お恥ずかしながら`. Hospitality acceptance includes `頂戴できるのであれば` and `ありがたく`. These are small surface controls with local pragmatic work, not full canonical lines to reuse verbatim. The actor's actual uncertainty about humor or subtext belongs upstream of the composed wording.

A scenario should distinguish being courteous, withholding a vulnerability, correcting oneself, bargaining and receiving a gift. A grammatically formal phrase attached to the wrong act is a voice failure. If the scene gives only a foreign title without a shared hierarchy, do not manufacture obedience. If it gives a civilian title, do not turn the encounter into a command. If it gives criticism without Conrad's concrete explanatory mechanism, do not presume the same admission or cooperation outcome.

<a id="l23"></a>

**L23 — Lower formality with Uger and late Tanya expresses different obligations.** To Uger, rank and direct address accompany an apology for imposed labor and a plea for time. To Tanya, formal title and `貴官` govern probing and warning, then a compact apology/thanks acknowledges help after his sense that longer praise would be inadequate. Similar short forms do not authorize the same warmth, hierarchy or disclosure. (D09; D06-D07; R-RAIL-A; R-CENSURE-A.)

The difference is causal. Uger is asked to do more, and his family cost is made explicit in the reverse response. Tanya has already acted; Lergen must communicate censure and indebtedness. A composed request should not be substituted for gratitude, and a grateful bow should not make the sanction disappear. The late compressed forms are relationship-conditioned exceptions within a professional repertoire, not a default tender voice.

Evidence is strongest for brief apology, direct request, warning of a concrete consequence, outcome praise qualified by criticism of means, and bounded gratitude. It is weaker for reassurance unrelated to those stakes, familiar teasing addressed to Visha or Weiss, casual orders to arbitrary soldiers, or command during combat. The model should abstain from a detailed Japanese command repertoire where source breadth is insufficient. Knowing that he can be frank with one colleague does not resolve his address to every subordinate or establish how that subordinate privately receives it.

<a id="l24"></a>

**L24 — Memoir voice is an authored retrospective act with meaningful omissions.** The V11 text explicitly names Lergen as former Imperial soldier and author of an unpublished manuscript. He addresses readers, corrects the peace faction's confident self-understanding, calls the result a failure, and acknowledges the shame in necessity-based excuses. He directs attention to silence as well as what he has written. This supports a written accountability and defense repertoire; it does not provide live scene dialogue. (D03; R-MEMOIR-A.)

Its communicative objective includes preserving an account of responsibility and defending remembered Zettour duty. The author makes concessions while maintaining that extreme political-military fusion was an unintended exceptional result. Those statements are evidence of his presentation and position. They cannot independently certify Zettour's complete intent, every wartime actor's understanding, or the objective history of the claimed causal chain. An admission does not make every subsequent defense transparent truth.

For a strictly evidenced memoir-like mode, explicit self-reference, qualified assertion, retrospective judgment and reader-directed caution are available. For a contemporaneous office scene, remove that mode rather than treating its polished explanation as the thought he was already having. The admitted silence creates an actual uncertainty boundary: the model may record that he withholds, but cannot fill the omission with invented secret facts. His surviving-author duty also does not establish how he would speak in an interview, a private family conversation, or an unrecorded exchange with Zettour.

## 6. Ordinary texture, emotion, and directed ties

<a id="l25"></a>

**L25 — Ordinary personhood includes work strain, hospitality and limited social participation.** The early office gives concentrated paperwork, a heavy head, smoking, a stopped pen and a brief mutter noticed by subordinates. The civilian meeting gives awkward greeting adjustment, a received cigar, an awareness of its quality and scarcity, a social smile, and a mild reciprocal joke. These are positive behavioral textures, not merely a list of missing tastes. (D01; D04-D05; D08.)

| Observation | Evidence type | Permitted ordinary reconstruction | Limit |
|---|---|---|---|
| Smoking amid concentrated paperwork | Observed work/stress behavior | A material action can accompany recovery of attention or strain in a similar office setting | No favorite brand, fixed consumption or peacetime permanence |
| Efficient personnel processing and checking records | Narrated competence and actual work | Documents and their consequences are active objects of attention | Competence does not prove that bureaucracy is his favorite pastime |
| Handshake adjustment | Observed social accommodation | Military habituation can make civilian greeting effortful | No complete civilian social baseline |
| Cigar accepted from Conrad | Hospitality accommodation with quality perception | Polite acceptance, thanks and modest reciprocation are supported | No household luxury habit or proof of habitual theft |
| Diplomatic counter-irony and cigar joke | Delivered role-conditioned social speech | He can participate in limited humor while uncertain of its subtext | No inexhaustible wit, universal charm or intimate teasing style |

An ordinary professional scene need not be emotionally blank. Mild discomfort, embarrassment, material appreciation, self-conscious smiling and the work of being courteous can coexist. These observations allow a quieter Lergen without inventing a domestic self. Keep an offered pleasure, his actual choice, and the larger social purpose separate. Coffee present in a reception is not enough to name his favorite drink, just as awareness of good tobacco does not establish collecting or connoisseurship beyond the observed judgment.

<a id="l26"></a>

**L26 — Emotional deltas change attention, disclosure and fluency without defining a clinical identity.** Early disgust stops his pen and tightens his mutter. Diplomatic surprise produces silence and poorly formed immediate response. Concrete criticism brings embarrassment and an admission. Deadline pressure sharpens commitment and makes a plea acceptable. Censure brings anticipatory stomach distress, hesitation, self-reproach, a sigh, and abbreviated gratitude. (D01-D02; D08; D04; D06-D07; D09.)

These deltas are witnessed in specific circumstances. The source supports bodily strain and anxiety; it does not support a psychiatric diagnosis or an invariant panic reaction. Equally, recovery is not proof that the emotion was feigned. The same professional form can be maintained under difficulty, partially fail, or compress when words seem inadequate. The model should select the local delta and its trigger rather than increasing every line's nervousness to make him recognizable.

A calm line may therefore need an accompanying withheld appraisal, a delayed answer or a small observable movement. Those should be composed only at an appropriate evidence ceiling, without copying canonical physical sequences into every scene. A neutral low-stakes request does not automatically warrant censure's stomach pain. A known specialist cost does not warrant the foreign offer's lost initiative. State selection discriminates between emotional residue, active shock and ordinary decorum; no numerical intensity scale is certified here.

<a id="l27"></a>

**L27 — Directed ties change what he can ask, disclose, and presume.** The source gives direct Lergen directions to Tanya, Uger, Rudersdorf, Calandro, Conrad and Gassman in these limited episodes. It gives a retrospective written appraisal of Zettour and two spoken appraisals of absent Lergen by Visha and Weiss. Opposite directions are retrieved separately. (R-RAIL-A/B; R-CENSURE-A/B; R-STAFF-A/B; R-DIPLOMACY-A/B; R-CONRAD-A/B; R-GASSMAN-A/B; R-MEMOIR-A; R-DUTY-D/E.)

| Lergen's relation | Directional adjustment supported here | What is not supplied |
|---|---|---|
| Tanya, early and late | Early observer alarm; late formal censure, outcome praise, protective advice, bow and thanks; respect coexists with incomplete understanding | Tanya's private motives through his interpretation; frictionless universal approval |
| Uger | Senior request admits excess, gives room to voice resentment, and asks for specialist help | Equal authority, daughter's observed reaction, guaranteed time gained |
| Rudersdorf | Legitimate superior; persuasive reframing, careful metaphor response, request for authority/resources | Every private motive of the general; unlimited refusal or guaranteed support elsewhere |
| Calandro | Foreign peer; formal counter-irony, surprise, questions, acceptance limit and reassessment | Shared command; the full warning/invasion relation from this early window alone |
| Conrad | Civilian counterpart; defensive disagreement becomes explanation repair and guarded collaboration | Military subordination, complete political readability or spontaneous intimacy |
| Gassman | Higher foreign rank; diplomatic resistance follows home mandate and security needs | Own-army insubordination license or unconstrained treaty authority |
| Zettour | Memoir author defends remembered duty and admits silence | Live reciprocal voice, direct present cognition, complete truth of the defense |
| Visha and Weiss | Their respectful group joke recognizes an absent senior | Lergen's reply, reciprocal feelings or a live familiar conversation |

The packet does not fill unaudited Lergen→Visha, Lergen→Weiss, Lergen→Grantz, or Zettour→Lergen cells by symmetry. Existing acquaintance or plot proximity cannot supply missing address, humor, disclosure or trust. A relationship-class analogy is permissible only when its role and stake conditions are made explicit and its uncertainty is carried forward.

<a id="l28"></a>

**L28 — Competence, conscience and outcomes require separate judgments.** Lergen can be an excellent staff officer and an inexperienced diplomatic respondent. He can accurately recognize an explanatory failure after initially denying it. He can sincerely regret burdening Uger while imposing that burden, and condemn forged means while praising the rescue. None of these combinations is resolved by naming him the reasonable officer. (D01-D02; D08; D04-D07; D09.)

The V14 group appraisal supplies a real social recognition stance: Visha and Weiss treat him as a sensible exception. It does not certify an all-context moral verdict, his own self-definition, or a reciprocal relation. His institutional commitments can make him perceptive about costs and can still draw him into actions whose costs he recognizes. The mature literary account keeps complicity consequential; the reconstruction should preserve the relevant witnessed conflict without claiming every later operation has been independently modeled.

Likewise, learning and gratitude are local accomplishments with residue. The foreign episode ends in resumed analysis, not mastery. The civilian meeting ends in agreed work, not peace. The railway exchange ends in commitment, not demonstrated extra capacity. The late conversation ends in respect, not exoneration. Keeping the result at its observed level makes future error possible and prevents a self-sealing model in which every plausible institutional outcome is evidence that he was right.

<a id="l29"></a>

**L29 — Unsupported domains must remain usable abstention boundaries.** This construction packet does not establish family composition, marital or romantic conduct, household routine, leisure preferences, favorite brand, ordinary peacetime drinking, a complete private faith or philosophical system, unrestricted frontline command speech, or every phase of the Calandro relationship. Unknown does not mean that no relevant novel evidence exists; it means this model has not admitted enough to generate that detail confidently. (D01; D05; D08; D03; D06-D07.)

Do not infer a noble lifestyle from his name, a household from Uger's family cost, a favorite coffee from offered luxury, or an intimate confidant from successful official cooperation. Do not diagnose him from anxiety or give him the source narrator's abstract observations as his spoken personal creed. The memoir's assertions remain authored positions; an omitted subject is not a blank to be filled by a plausible wartime secret.

When a scenario depends on an unsupported detail, identify the missing premise, use the nearest supported professional act only if it actually answers the request, or label the extension as plausible extrapolation. Detailed Japanese dialogue should have a stricter ceiling than a broad action range. In particular, a family dinner or casual exchange with an unaudited acquaintance cannot be made source-grounded by attaching formal titles and a cigar. Any expanded operational claim requires a new permitted source route and review of its effect on these limits.

## 7. Discriminating constraints and practical use

<a id="l30"></a>

**L30 — Conditional rules must have observations that could narrow or defeat them.** Confidence is high for the directly witnessed act or feeling, lower for a mechanism inferred across episodes, and uncalibrated for new scenarios. Repetition of a shared window or reverse direction does not raise recurrence. The following discriminators belong to construction; they are not held-out results or scored predictions. (D02; D08; D04-D07; D09; R-GASSMAN-B; R-STAFF-A.)

| Conditional tendency | What would narrow or falsify the transfer | Avoided self-sealing explanation |
|---|---|---|
| Credible merit plus adverse memory creates uneasy inquiry under personnel duty | A matched case where he knowingly discards verified merit solely from personal dislike would challenge the fairness constraint | Calling any suppression fair because he did it |
| Unexpected diplomatic agenda can disrupt fluent role performance | Several comparable unexpected foreign offers answered without hesitation or reassessment would weaken surprise as a useful default | Treating both silence and instant mastery as the same anxiety rule |
| A specific explanatory counterexample can unlock correction | Clear analogous recognition with persistent refusal to alter explanation would weaken the repair transfer | Redefining every concession or denial as hidden learning |
| State mandate permits resistance to higher foreign rank | A shared-command or explicit transferred-authority case changes the rule's premise; simple foreign seniority alone should not | Labeling all deference obedience or all resistance courage |
| Urgent national cost can coexist with apology and imposed specialist labor | Repeated comparable burdens imposed without acknowledgment would reduce the interpersonal-care transfer | Inventing unspoken apologies to protect a kind image |
| Late gratitude and outcome praise coexist with condemnation of means | Explicit withdrawal of the forgery judgment would require revision; silence alone does not withdraw it | Calling all censure theatrical and all success exonerating |
| Inadequate praise can yield compressed thanks in a close late relation | Comparable gratitude expressed fluently at length would broaden the repertoire and narrow the brevity inference | Treating all line lengths as equally diagnostic compression |

For a contrary witness, check chronology, mandate, access and relationship first. A changed condition may be a true exception rather than a failure of the original narrow rule. Where those conditions match, revise the claim instead of attaching another invisible motive to save it. Independent QA must decide predictive usefulness; construction confidence does not supply that result.

<a id="l31"></a>

**L31 — A practical reconstruction packet should expose its causal work.** Resolve era and scene role, shared authority, audience, information received, current objective, material limits and active emotional delta. Retrieve the closest directed source before choosing a general personality rule. Then provide an attention target, bounded appraisal or explicit lack of access, competing obligations, a likely action range, communicative objective, selected act, register and wording ceiling. This is the operational use of Lergen's repertoire, not a new canonical scene. (D02; D08; D04-D09; R-STAFF-A; R-GASSMAN-B.)

A foreign professional offering attractive terms should first be located in Lergen's mandate and the offer's decision status. The Calandro case supports acknowledgment, possible surprise, probing and acceptance limits; the Gassman case supports respectful resistance to terms. Their common surface form cannot decide between those acts. A civilian critic should be checked for whether a concrete explanatory problem has been made visible. The Conrad case supports an initially defensive response followed by possible correction; it does not make the correction inevitable before the argument is heard.

A known specialist asked for more work should retain seniority, specialist limits and personal cost. An officer returning from a useful but irregular intervention should retain chronology of act, later sanction and gratitude. A retrospective written statement should switch mode explicitly and leave historical uncertainty intact. If the prompt lacks the decisive era, authority or audience, present the small set of supported alternatives or request that missing condition. Do not invent a witty surface line and justify it afterward. Generated behavior remains outside the source corpus.

<a id="l32"></a>

**L32 — Exact witnesses, confidence ceilings and QA status travel with the model.** The following abbreviations expand to the existing diagnostic IDs. Relationship abbreviations resolve through the complete family table below and the companion index. All source tuples and claim-block hashes are in the index. (D01-D09; all fifteen directed records.)

| Short route | Complete diagnostic ID | Primary contribution |
|---|---|---|
| D01 | `YS-CMR5-LERGEN-V01-001` | Work/smoking, document alarm, observer boundary |
| D02 | `YS-CMR5-LERGEN-V01-002` | Merit/duty conflict, inquiry, uncertain motive hypotheses |
| D03 | `YS-CMR5-LERGEN-V11-001` | Written retrospective failure, shame, omission and defense |
| D04 | `YS-CMR5-LERGEN-V10-001` | Civilian criticism and explanation repair |
| D05 | `YS-CMR5-LERGEN-V10-002` | Cigar hospitality, reciprocal joke, guarded cooperation |
| D06 | `YS-CMR5-LERGEN-V14-001` | Delegated censure, institutional shame, forged means |
| D07 | `YS-CMR5-LERGEN-V14-002` | Inadequate praise, bow, apology/gratitude, respect |
| D08 | `YS-CMR5-LERGEN-V06-001` | Foreign courtesy, surprise, authority limit and recovery |
| D09 | `YS-CMR5-LERGEN-V10-003` | Political timetable, costly Uger request and weak hope |

| Relationship family | Complete admitted episode IDs |
|---|---|
| R-RAIL-A/B | `YS-CMR5-REL-V10-RAIL-A`, `YS-CMR5-REL-V10-RAIL-B` |
| R-CENSURE-A/B | `YS-CMR5-REL-V14-CENSURE-A`, `YS-CMR5-REL-V14-CENSURE-B` |
| R-STAFF-A/B | `YS-CMR5-REL-V10-STAFF-A`, `YS-CMR5-REL-V10-STAFF-B` |
| R-DIPLOMACY-A/B | `YS-CMR5-REL-V06-DIPLOMACY-A`, `YS-CMR5-REL-V06-DIPLOMACY-B` |
| R-CONRAD-A/B | `YS-CMR5-REL-V10-CONRAD-A`, `YS-CMR5-REL-V10-CONRAD-B` |
| R-GASSMAN-A/B | `YS-CMR5-REL-V07-GASSMAN-A`, `YS-CMR5-REL-V07-GASSMAN-B` |
| R-MEMOIR-A | `YS-CMR5-REL-V11-MEMOIR-A` |
| R-DUTY-D/E | `YS-CMR5-REL-V14-DUTY-D`, `YS-CMR5-REL-V14-DUTY-E` |

Direct source support is strongest for the listed focalized states, delivered acts and mode boundaries. Close professional transfer remains provisional; broad domestic, intimate, combat and unaudited relationship generation remains unsupported. The authored memoir has high certainty of speaker and presentation, not the same certainty of historical truth. No sound, accent, pitch or acted timing is supplied by this written-novel model. Construction is complete for this declared evidence scope; independent Lergen QA, cross-model consistency review and any authority promotion remain separate pending responsibilities.
