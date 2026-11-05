---
title: "Yuri Is My Job! — Volume 1: Performance, Recognition, and the Problem of Trust"
artifact_id: WATAYURI_V01_DEEP_READING
artifact_type: sequential_deep_reading
series: "Yuri Is My Job! / 私の百合はお仕事です！"
generation: WATAYURI_BOOTSTRAP_V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: false
created: "2026-09-28"
base_commit: bc596633e8fc53e50f14892ad29f77017f166a05
canonical_home: "series/watayuri/02 Sequential Readings/WATAYURI_V01_DEEP_READING.md"
source_boundary: "Japanese V01, mainline Shifts 01–06 through i156; packaged Shift 6.5 and edition paratext separately classified; no later-volume evidence"
execution_scope: single_operation
recommended_reasoning_class: SUBSTANTIVE_ANALYSIS
source_inspection_state: COMPLETE_FOR_DECLARED_SCOPE
prospective_mainline_endpoint: "V01 / Shift 06 / i156"
---

# Yuri Is My Job! — Volume 1 deep reading

**Navigation:** [Source and coverage](#source-receipt) · [Chapter close readings](#close-reading) · [Supplement](#supplement) · [Relationship records](#relationships) · [Claims](#claims) · [Predictions](#predictions) · [Readiness](#readiness) · [Frozen exit](#exit-state) · [Integration handoff](#handoff).

## 1. The volume’s governing problem

Volume 1 begins with a girl who thinks she knows how to be seen and ends with two girls who do not know how to interpret each other. Shiraki Hime’s opening project is to make a desirable impression so reliably that nobody will refuse her. Her experience at Café Liebe initially appears to test the strength of that project against one unusually resistant person. By the final conversation, however, the problem has changed: an impression can succeed as a performance while leaving another person unable to distinguish a genuine wish from an instrumental line. Being convincing and becoming trustworthy are not the same achievement. [V01/01/i005–009; V01/02/i050–059; V01/06/i149–156.]

The café is not simply a place where false public selves conceal true private selves. Its publicly fictional sisterhood produces real obligations, real assistance, real affronts, and real questions about attachment. Conversely, leaving the salon does not automatically make a person’s speech candid or easy to understand. Hime continues to manage impressions backstage; Mitsuki’s private rebukes disclose hostility without explaining its entire history; and Kanoko’s familiarity with Hime’s façade does not give her unrestricted access to Hime’s changing desires. The distinction that matters is not merely **performance versus reality**, but **which part of an interaction is performed, which consequences are real, who recognizes the performance, and what remains unreadable**. [V01/02/i043–059; V01/04/i103–108; V01/05/i123–132; V01/06/i149–156.]

The final identity disclosure is therefore more than a surprise concerning someone’s name. Hime has begun to distinguish the allegedly destructive person from her childhood from the unexpectedly non-exposing person in front of her. The last page makes those two classifications refer to the same individual. It invalidates their separation without yet deciding the truth, motive, or moral meaning of the earlier incident. The correct V01 exit is an unresolved collision of interpretations, not a completed reconciliation. [V01/05/i126–129; V01/06/i153–156.]

**Authority and coverage.** This is the canonical V01 reading on the Watayuri series branch once the coordinated V01 transaction is published and validated. The source-reading producer directly inspected the stated Japanese EPUB; the receiving integration review verified the complete handoff and branch state but could not independently materialize the 102,785,359-byte EPUB in this workspace. The mainline freeze is Shift 06/i156; Shift 6.5 is supplementary. The nine cumulative ledgers and source/current-state maps own mutable state. Section 16 preserves the original producer handoff as a historical receipt, not a live list of incomplete repository tasks.

<a id="source-receipt"></a>
## 2. Source receipt, admission, and entering state

### 2.1 Exact witness and verification

| Field | Verified value or bounded result |
| --- | --- |
| Source-map key | `V01` |
| Exact Drive filename | `Yuri Is My Job! - Volume 01 [Japanese].epub` |
| Drive object | `14sEQcf_V-iYCgyxgXcLYN5jCZXLE2Hlc` |
| Source folder | `1bKsOEQiLKU41cgW1Ht2Pt4qFj0nCdWwi` |
| Retrieved size | **102,785,359 bytes**, agreeing with the pinned source map and live metadata |
| SHA-256 of downloaded EPUB | `6da3ccf414cdecc8c1458b62be7aef6d9324db1b9938ef0caebd2b8763e8ebb9` |
| Hash comparison | Exact match to the pinned manifest-derived local-source hash; this independently verifies the bytes retrieved in this run, not every future revision of the Drive object |
| Package | EPUB 3; fixed/pre-paginated layout; right-to-left page progression |
| Structural result | 348 ZIP entries; ZIP CRC check passed; all 170 spine items resolved to an image |
| Image dimensions | 1441 × 2048 pixels for each of the 170 spine images |
| Package title/language | `私の百合はお仕事です！： 1`; `ja` |
| Creator/publisher | 未幡 / Miman; 一迅社 / Ichijinsha, also supported by the visible colophon |
| Colophon identifier | ISBN `978-4-7580-7693-7`; a witness identifier, not an independent edition-history investigation |
| Execution date and route | 2026-09-28; authenticated Drive retrieval → local byte/structure checks → direct visual reading of Japanese manga images |
| Excluded routes | No OCR, translation edition, anime performance, external plot summary, later numbered volume, interview, or reception source used |

The package root is `item/standard.opf`, located through `META-INF/container.xml`. Its metadata modification timestamp is `2017-06-13T00:00:00Z`; that field is **not** treated here as an independently verified publication date. Structural checks establish the practical witness and locator scheme; they are not a claim to have run a complete EPUB standards-conformance suite.

The pinned source map had correctly left remote byte verification unresolved. The downloaded witness matched its recorded local-source hash. The producer's source operation passed **STRUCTURALLY_VERIFIED → ADMITTED → INSPECTED** with the component boundaries below. The synchronized source map records those stages; **CLOSED** refers to the complete V01 transaction only after its exact branch result is validated.

### 2.2 Citation and page convention

A citation such as **`V01/04/i103–105`** means this exact Drive witness, Shift 04, image members `item/image/i-103.jpg` through `item/image/i-105.jpg`. The corresponding wrappers are `item/xhtml/p-103.xhtml` through `p-105.xhtml`. The image number is the principal locator, not an assumed printed page number.

For numbered images, **one-based EPUB spine index = image number + 2**. Printed pagination agrees with that offset at inspected anchors, including i014/p.16, i044/p.46, i103/p.105, and i162/p.164. The file nevertheless consistently cites image numbers. Cover, blank, and colophon use their actual image names rather than invented page numbers.

The EPUB places even-numbered images on the right and the following odd-numbered images on the left. Thus i058–059 form a facing-page pair, whereas i155 → i156 crosses a page turn under the package’s assigned spread layout. The two- and four-page reading montages used during inspection were navigation aids, **not** evidence of original spread adjacency. Formal claims below follow the source’s spine/spread assignments and panel sequence.

Observation IDs **O01–O17**, claims **WY1-C01–C14**, and the other `WY1-` records are introduced in this file. They are proposed durable IDs, not references to pre-existing ledger entries. An observation ID identifies a contextual passage, not an assertion that every interpretation attached to that passage is equally certain.

### 2.3 Complete coverage and component boundaries

| Component | Image members / spine positions | Inspection and use |
| --- | --- | --- |
| Front cover | `cover.jpg`; spine 1 | Visually inspected; edition/cover art, not a dated story event |
| Blank | `i-white.jpg`; spine 2 | Visually inspected; no narrative content |
| Shift 01 — ようこそリーベ女学園へ！ | i001–036; spine 3–38 | Complete textual/visual reading; i004 is the contents page within this span |
| Shift 02 — ごきげんよう、お姉さま | i037–060; spine 39–62 | Complete textual/visual reading |
| Shift 03 — お連れの方はご友人ですの？ | i061–084; spine 63–86 | Complete textual/visual reading |
| Shift 04 — みなさんでお給仕を始めましょう？ | i085–108; spine 87–110 | Complete textual/visual reading |
| Shift 05 — 嘘なんてありませんわ | i109–132; spine 111–134 | Complete textual/visual reading |
| Shift 06 — 何を信じたら良いんですの？ | i133–156; spine 135–158 | Complete textual/visual reading; mainline endpoint is i156 |
| Logo divider | i157; spine 159 | Inspected; not a narrative continuation |
| Shift 6.5 — 果乃子の部活はお仕事です！ | i158–161; spine 160–163 | Complete reading, recorded as a separately bounded packaged short; not silently placed after the mainline cliffhanger |
| Afterword | i162–163; spine 164–165 | Visually inspected and classified as creator/production paratext; not used to establish character biography or story causality |
| Edition “EXTRA PAGES” | i164–167; spine 166–169 | Inspected: underlying cover art, menu guide, spine/flaps/catalogue, back-cover material; not promoted to mainline events |
| Colophon | `i-okuduke.jpg`; spine 170 | Inspected for witness identification |

**Coverage qualifications.** Every mainline page was directly examined, including text, reaction panels, and scene transitions. Key wording and identity evidence were reread at individual-page scale. This is an analytical reading, not a certified transcription: peripheral handwritten production notes and catalogue listings were not exhaustively transcribed and support no literary conclusion here. No missing mainline image or unread mainline section was identified.

**Source correction SQ01.** The navigation entry for Shift 05 says `嘘なんでありませんわ`; the visible title on i110 says `嘘なんてありませんわ`, agreeing with the contents page. The visible manga title controls. This is a packaging/navigation discrepancy, not a story contradiction.

**Admission decision.** The six numbered main chapters are the admitted primary narrative tranche. The packaged short is available for explicitly marked supplementary observations only; its precise chronology remains open. The afterword and edition extras retain paratext status. The absence of a “bonus” label in V01’s filename did not establish the absence of extra components.

### 2.4 Entering state and knowledge controls

At the V01 entering-state commit, the current-state file and all nine longitudinal ledgers contained **no inspected narrative volume, no narrative claims, no established cast assessment, and no prior predictions**. The owner-approved sequential lock was open. V01 therefore had no previous-volume synopsis or inherited developmental state to reproduce. The later cumulative ledger additions do not change this frozen entering state.

An entering-state record was made before narrative image inspection. Only V01 was admitted for this operation. No later volume was fetched or opened; no adaptation or external account was used to resolve uncertainty. The retrospective column in this reading therefore contains only **retrospection supplied inside V01**, not later-series explanations. This is an evidence-bounded prospective run, not a claim that pretrained familiarity has been experimentally erased.

**Prior-prediction adjudication: not applicable.** There are no inherited predictions. Changes in interpretation as the volume supplies more information are recorded as within-volume evidential development, not falsely presented as forecasts frozen before those scenes were read.

<a id="close-reading"></a>
## 3. Sequential, form-sensitive close reading

### 3.1 Shift 01: an accomplished performer enters somebody else’s performance

<a id="o01"></a>
#### O01 — The public angel and the private production process

**Source:** V01/01/i001–009, especially i005–008. **Evidence status:** visible interaction plus Hime’s internal narration; the classmates’ judgments remain their judgments.

The opening academy tableau gives the reader an idealized environment before the ordinary-school sequence explains the protagonist’s approach to social life. Its immaculate “school” is part of the café’s representational world, not independent proof that the staff attend such an institution. Hime’s anxious interior response already interrupts the image of effortless refinement. The book then makes a related interruption in her everyday life: classmates read her as naturally cute and good, while her narration describes a deliberately maintained presentation.

This contrast is more precise than a revelation that Hime is “secretly bad.” The pages show her monitoring an audience, arranging an apparently modest response, and obtaining the response she wants. The presentation looks spontaneous to its audience because its production has been concealed. The reader is allowed to see that production, including exaggerated, scheming facial caricatures that do not match the public girl’s beautiful expression. The formal contrast gives us privileged access to intention, but it does not establish that every considerate action is wholly insincere.

Hime states a wealthy-marriage ambition and imagines being loved and selected by everyone as the route toward it. She can dismiss a romance fantasy privately while accommodating it socially. At this point, a strong claim is that admiration functions as both an instrumental resource and a measure of success. A weaker, premature claim would be that wealth exhausts her motivational life. Later embarrassment, gratitude, friendship, and the wish to be liked by one resistant coworker will not fit neatly into that reduction. [V01/01/i007–009; compare V01/03/i080–084 and V01/06/i153–154.]

Her competence is also specific. She is good at making herself the center of a legible, pleasing social scene. Nothing here establishes competence at remembering a shared fictional setting, coordinating a duet, taking orders, or distinguishing a customer’s interpretation from a coworker’s consent. The subsequent café failures do not negate the opening evidence; they reveal the narrowness of the skill she has generalized.

<a id="o02"></a>
#### O02 — Recruitment converts a virtue claim into a practical obligation

**Source:** V01/01/i010–019, i036. **Evidence status:** depicted encounter; Mai’s injury and fracture statements are character reports.

Hime’s collision with Mai is followed by a courteous offer of assistance. Mai makes that offer costly to withdraw: Hime’s cuteness is presented as useful, her professed helpfulness becomes a reason to cooperate, and Sumika’s intimidating intervention makes departure still harder. Hime is not physically incapable of saying no, but the scene does not present refusal as socially costless. Her habitual investment in appearing good is precisely what allows another person to mobilize that appearance against her.

The recruitment sequence consequently mirrors Hime’s own social technique. Both sides use appealing surface conduct to organize another person’s response. The asymmetry lies in information and institutional control: Hime does not yet understand the work she is being recruited to perform, whereas Mai knows the role she intends to assign. Hime’s later attempted stomachache exit meets an answering display of injury-related need. The comedy comes from competing performances, but the resulting work obligation is not imaginary.

At the chapter’s end, Mai reports a fracture and a longer recovery, overturning Hime’s assumption that this was a one-day substitution. That is an established extension of the demand **as communicated to Hime**. It is not medical verification, and V01 does not establish that Mai engineered the collision or fabricated the injury. “Manipulative recruitment pressure” is supported; “proven injury scam” is not. [V01/01/i011–014, i019, i036.]

<a id="o03"></a>
#### O03 — Beauty, role fluency, and the first address error

**Source:** V01/01/i015–035. **Evidence status:** setting and performance directly depicted; Hime’s evaluations of others are focalized interpretations.

The apparently elegant refuge is revealed as a concept café in which staff perform students of Liebe Girls’ Academy. Hime receives the role-name Shirasagi Hime, distinct from Shiraki Hime. Sumika’s transition from intimidating street presentation to refined senior demonstrates that clothing, address, posture, and audience can reorganize the same actor’s meaning. Her close approach is not automatically tenderness: backstage familiarity with coercive pressure can coexist with an onstage composition that invites the guests to enjoy intimacy.

Mitsuki initially appears to Hime as the beautiful, kind elder who belongs to this atmosphere. The reader can see why the impression works. Refined address, reassurance, decorative framing, and a head pat align a socially protective action with a visually compelling figure. Hime’s response includes a visibly affected, admiring reaction. The page licenses the importance of the encounter, but not a unique diagnosis of romantic attraction. Admiration of beauty, pleasure at being praised, and attraction remain distinguishable possibilities. [V01/01/i016–018, i029–032.]

The decisive failure is linguistic and institutional. Hime calls Mitsuki “elder sister” in a way that feels personally apt to her without knowing that the designation has a specific meaning in the café’s fiction. Her successful self-introduction has won applause; her subsequent improvisation creates a commitment she cannot yet interpret. This is the first sharp demonstration that winning an audience is not the same as understanding the scene one has joined.

Backstage, Mitsuki rejects the familiarity and rebukes her. Hime treats the contrast as access to the elder’s real feelings. That reaction is intelligible, but the analyst must not simply adopt it. A private rebuke establishes that Mitsuki can be angry and that the public reassurance did not transparently express the whole relationship. It does not yet establish the origin of the anger, the absence of all kindness, or a permanent “true personality” concealed beneath a false public shell. The volume’s later movement depends on keeping those questions open. [V01/01/i033–035.]

### 3.2 Shift 02: an audience can ratify a relationship without resolving a refusal

<a id="o04"></a>
#### O04 — The sisterhood becomes a public continuity problem

**Source:** V01/02/i039–047, especially i043–046. **Evidence status:** present dialogue, in-world exposition, and the displayed public report.

Kanoko’s first conversation with Hime supplies an important qualification to the opening solitude of the self-fashioner. Hime already has a friend with whom ordinary conversation is less tightly controlled, even though she withholds the embarrassing details and location of the job. This is not a protagonist who has literally no relationships outside universal admiration. The extent of this friendship’s knowledge and reciprocity still needs to be tested.

At the café, Mai explains why the earlier address cannot simply be forgotten. The guests have noticed it, and a public report has helped preserve their expectations. The established Schwestern convention promises a special older/younger-student relationship, represented through the exchange of matching crosses. The explanatory page attributes the café’s model to the in-world novel *乙女の心臓*. These are facts about the manga’s represented cultural and institutional world; no external literary-history identification is needed to use them. [V01/02/i044–045.]

The public audience functions as a memory system. Hime’s fleeting improvisation persists after the shift and becomes something subsequent performances must answer. Mai’s proposed pairing is therefore not simply a generous opportunity for friendship. It is also a managerial repair for a continuity problem. Although she nominally leaves the final decision to the two participants, the possible decisions are already burdened by customer expectations and workplace consequences.

A useful distinction follows: the café can need a coherent relationship **as an offered experience**, while the people performing it have not agreed on a corresponding private relationship. The story does not allow those two kinds of agreement to be treated as interchangeable.

<a id="o05"></a>
#### O05 — Refusal, public pressure, and a successful but damaged pact

**Source:** V01/02/i050–060, with i052–059 decisive. **Evidence status:** private refusal and subsequent public conduct directly shown; deeper motives remain underdetermined.

Mitsuki refuses the proposed pairing backstage, framing Hime’s inexperience as a burden. Hime experiences this not only as a practical objection but as the intolerable fact of not being chosen. The refusal exposes a vulnerability in the universal-approval program: someone else’s independent decision is being treated as a problem her charm ought to solve.

Her response moves the issue to the salon. She solicits attention, recruits the customers’ appreciation, and eventually asks about the refused cross in public. This is more consequential than an innocent misunderstanding. By this point, she has heard a refusal. The shift of audience changes what it would cost Mitsuki to sustain it. The private disagreement becomes a public scene in which an outright rejection would disrupt the welcoming sisterly world the staff are maintaining. [V01/02/i050–057.]

Mitsuki does participate in the resulting public settlement. The cross exchange is enacted and the audience celebrates the new sisters. That is a genuine change in the public role-state. It is not proof that the preceding refusal was insincere or that the subsequent assent expresses an unconstrained private desire. Hime’s strategy succeeds at producing the visible selection she wanted while helping create a more antagonistic private situation.

The tie-adjusting composition is especially important. A socially legible act of elder-sister care provides an intimate distance at which a hostile aside can be delivered. The page does not first show “fake closeness,” then cut to a separate real event. Public closeness and private rejection occupy the same encounter. The audience’s congratulations and Mitsuki’s declaration of hatred are both actual parts of it. [V01/02/i058–059.]

Nor should the hatred line be dismissed as automatically meaning its opposite. The evidence supports a hostile utterance and a serious rupture. It leaves open whether that utterance exhausts Mitsuki’s feelings or whether other grievances are active. V01 later supplies a reason to reopen the causal account; it does not license a retrospective assertion that the line was never hostile.

### 3.3 Shift 03: the workplace’s fiction becomes a friend’s apparent rejection

<a id="o06"></a>
#### O06 — A protected friendship encounters a new information boundary

**Source:** V01/03/i061–067; compare V01/02/i039–040. **Evidence status:** institutional instruction, school interaction, and Kanoko’s interior narration.

Mai’s secrecy rule is intended to preserve the fictional academy from disruptive real-world familiarity. Hime is independently happy not to advertise an embarrassing job. These motives overlap without being identical. The same omission can serve management’s staging needs and the employee’s image-management needs.

The school passage makes Kanoko more than an abstract “best friend.” She struggles when classmates ask about Hime’s earlier life, and Hime intervenes. The intervention both helps an uncomfortable friend and protects Hime’s own image; the text does not force a choice between those effects. In their private conversation, Hime encourages more assertiveness. Kanoko cannot finish telling Hime she is cute, while her later internal narration and phone-image viewing make the intensity of her attention explicit. This is stronger evidence of attachment than a blush considered in isolation. It still does not settle a sexual identity or a reciprocal romantic status. [V01/03/i063–066.]

The public café image produces the next misunderstanding. Kanoko finds the information Hime has withheld and interprets the omission in the context of their friendship. What she lacks is not recognition of Hime’s appearance but an adequate model of why a familiar person would hide this part of her life. The business wants publicity and secrecy at once, with different intended audiences. The episode exposes the instability of that division rather than merely depicting a foolish visitor. [V01/03/i061, i067.]

<a id="o07"></a>
#### O07 — Names and sisterhood allocate access

**Source:** V01/03/i068–076. **Evidence status:** depicted service encounter; the hostile-visitor vignette at i071 is explanatory/hypothetical, not an additional actual incident.

Hime is instructed to treat Kanoko as a stranger. From management’s perspective, this maintains the café’s world. From Kanoko’s perspective, a friend is denying their connection. The reader sees both frameworks, which makes the failure more painful and more intelligible than a simple case of one girl choosing to be cruel.

The café’s rules of address intensify the mismatch. Kanoko’s familiar “Hime-chan” is obstructed while Mitsuki can address Hime with the intimacy authorized by their sister role. A previously meaningful friendship practice loses permission in the same space where a newly encountered person seems to possess a privileged bond. The role thus distributes not merely words but visible access: who may recognize Hime, summon her, and stand close to her. [V01/03/i072–075.]

Kanoko’s reaction supports distress at displacement and an exclusivity concern. It does not prove that she correctly understands the private relationship she is observing. In fact, the reader knows that the admired sisterhood was established over a backstage refusal. Kanoko is threatened by a public representation whose private status differs sharply from the one she imagines.

The spill makes the incompatibility material. Hime’s alarmed apology uses Kanoko’s name and breaks the stranger fiction; concern overtakes the immediate performance demand. Mitsuki then handles the customer-facing response. The accident should not be inflated into a proven deliberate attack. What matters is the rapid crossing of frames: fictional estrangement, perceived relational exclusion, bodily mishap, familiar concern, and professional damage control. [V01/03/i075–076.]

<a id="o08"></a>
#### O08 — Recruitment recognizes genuine care while putting it to work

**Source:** V01/03/i077–084. **Evidence status:** Kanoko’s stated responsibility, manager intervention, visible reaction, and subsequent application.

Kanoko takes responsibility rather than presenting herself as the wronged customer. Mai notices the care for Hime in that response and recasts employment as a way to help her. The second recruitment repeats the first recruitment’s structure with a different resource: Hime’s helpful image was usable leverage; Kanoko’s genuine concern is usable leverage. This parallel does not erase the difference between them or prove that all assistance is a trick.

The uniform reveal then gives Kanoko an unexpectedly intense experience of being seen. Hime calls her cute, and the reaction is large enough to interrupt Kanoko’s processing of the conversation. The scene establishes the special force of Hime’s evaluation for Kanoko. It does not establish that Hime intends the same meaning that Kanoko receives. [V01/03/i079–081.]

The next-day application also matters for agency. Kanoko is not simply dragged into a permanent role by one startled response. She returns and expresses willingness, even while Hime suspects that management has pressured her. Hime’s own idea that a replacement might let her leave is not the arrangement Mai offers: the two will work together. Kanoko is capable of a decision Hime did not predict, and Hime’s assumed privileged understanding of her friend is already incomplete. [V01/03/i082–084.]

### 3.4 Shift 04: being adorable is not the whole job

<a id="o09"></a>
#### O09 — Training exposes the limits of Hime’s existing expertise

**Source:** V01/04/i085–102. **Evidence status:** instructional scenes, actual service attempts, competing character judgments.

Kanoko receives the café-name Amamiya Kanoko. She understands the difference between a performed relationship and the real friendship status that may or may not accompany it. This initially reassures her about Hime’s sisterhood, but her reassurance is also motivated: the interpretation that preserves her own special relationship is emotionally convenient. Her perception is neither simply correct nor simply jealous error. [V01/04/i087–089.]

The chapter gives unusually concrete content to the word “job.” Orders require more than a charming introduction. Hime must sustain the fictional setting, understand unfamiliar menu language, record requests accurately, and coordinate with the kitchen. A successful greeting can coexist with a failure to receive the information needed to serve a table. Mitsuki’s role performance itself can make instructional content difficult for a newcomer to separate from decorative language. [V01/04/i090–094, i099–102.]

Kanoko’s quieter attempt shows another route to acceptance. Her hesitation fits the audience’s expectations of a shy first-year, and the customers make room for it. Sumika’s intervention likewise resists the notion that a new first-year must already perform polished senior competence. Hime is troubled because she is accustomed to treating superior presentation as evidence of superior performance. Here, visible awkwardness can be socially successful and practically adequate. [V01/04/i094–101.]

The comparison has limits. Kanoko’s simple order and Hime’s more elaborate multi-item order are not identical tests under controlled conditions. The defensible conclusion is not that Kanoko is globally more competent. It is that Hime’s preferred route—concealing uncertainty while sustaining a perfect impression—can obstruct the practical task, whereas acknowledged inexperience can invite cooperation.

Kanoko offers to practice together. Hime receives the offer partly as an unwanted classification: being grouped with the newcomer seems to lower her standing. This reaction exposes an additional cost of universal admiration as a self-model. Assistance is harder to accept when needing it threatens the identity the assistance is meant to support. [V01/04/i097–100.]

<a id="o10"></a>
#### O10 — Assistance is real; its relational meaning remains contested

**Source:** V01/04/i102–108, especially i103–105. **Evidence status:** concrete assistance, gratitude, and explicit but potentially incomplete explanations.

Mitsuki has actually attended to the order Hime failed to record and supplies a usable record. The help is not merely an attractive gesture for spectators; it solves a backstage work problem. It also shows that her public harshness cannot be reduced to indifference to whether Hime succeeds. The source establishes attention and assistance more securely than it establishes affection.

Hime thanks her and tries to interpret the act as personal kindness. Mitsuki insists that helping is the elder sister’s role and rejects the broader inference. That explanation has evidentiary weight, but it is not a metaphysical proof that the help contains no private investment. A role can be a genuine reason for action, a socially available explanation, or a limit placed on how the recipient may interpret an action. V01 has not yet distinguished all three here. [V01/04/i103–107.]

Kanoko’s response complicates the easy picture of her as an unconditional defender. She criticizes Hime for relying on a senior instead of becoming competent herself. The friend who worries about Mitsuki’s treatment can nonetheless share the demand for better work. Care for Hime does not always take the form Hime would prefer. [V01/04/i106–108.]

No repair should be closed at this point. There is a practical repair of a failed order and an expression of gratitude; there is not a settled private friendship, an apology for the earlier pressure, or an agreement about what the sister role means outside service. Keeping those outcomes separate is essential to the next chapter.

### 3.5 Shift 05: the pursuit of approval acquires a history

<a id="o11"></a>
#### O11 — A performance improves because it accommodates a real limitation

**Source:** V01/05/i109–124, especially i111–116 and i119–124. **Evidence status:** school and café conduct, Hime’s intentions, publicly and privately qualified praise.

The school-club invitation scene re-establishes Hime’s fluent everyday method. She refuses without making herself appear rejecting, using deference and an explanation that preserves the inviter’s regard. The café is difficult not because she has suddenly lost the ability to act but because one person’s judgment remains resistant to a technique that ordinarily works. Her inner insistence that she must be this universally desirable person places the problem above the level of a minor workplace irritation. [V01/05/i111–114.]

Her next attempt contains a genuine improvement. She asks customers to speak slowly and clearly because she is inexperienced. The request is attractively packaged, but it communicates a real need and helps the practical exchange. Performance is not defeated by honesty; a limited admission becomes usable within the role. This is one of the volume’s strongest counterexamples to a simple equation between Hime’s acting and deception. [V01/05/i115–116.]

Hime then pursues Mitsuki’s attention and asks to be praised as a younger sister. Mitsuki answers with an effective elder-sister performance, including touch, praise, and an acknowledgment of defeat within the interaction. Hime is visibly affected by the beauty and force of that response even while congratulating herself on having succeeded. The performer does not remain safely outside the scene she has engineered. She can be both strategic initiator and affected recipient. [V01/05/i119–122.]

The private aftermath prevents a simple victory. Mitsuki asks what Hime was doing, while Sumika urges recognition of the day’s good work. Mitsuki grants the performance-specific point: Hime was good **as the younger sister**. Hime wants the evaluation to reach the private person. Mitsuki’s qualification stops that inference. Actual improvement and continued relational opacity coexist; the volume does not require one to cancel the other. [V01/05/i123–124.]

<a id="o12"></a>
#### O12 — Kanoko’s objection and the remembered cost of exposure

**Source:** V01/05/i125–129, with the childhood recollection at i126–129. **Evidence status:** present disagreement plus Hime-focalized memory; no independent childhood account has yet been supplied.

Kanoko finds Hime’s investment in being liked by this particular harsh person strange. From her perspective, one disagreeable person need not determine Hime’s worth. Hime cannot accept the exception so easily. The disagreement reveals that Kanoko knows the outward-image strategy without necessarily knowing all of the fear attached to it.

The childhood recollection provides that fear with a concrete form. A classmate’s statement exposes a discrepancy between Hime’s public affection and what she allegedly said in private; other children subsequently distance themselves. The sequence presents the experience through Hime’s remembering and interpretive narration. It establishes a remembered social rupture and Hime’s interpretation of it as the destruction of her performance. It does not yet supply a full independent account of what was said, why it was repeated, or what either child thought the other understood. [V01/05/i126–129.]

Hime’s present conclusion is nonetheless clear: the people most likely to expose her must not be permitted to dislike her. Universal approval becomes a protective rule against the recurrence of exclusion. This expands the opening wealthy-marriage explanation without necessarily replacing it. Her self-presentation can serve aspiration, pride, ordinary social reward, and protection from a remembered loss at the same time.

The memory should not be used to excuse all of Hime’s current conduct. A fear of rejection helps explain why she pressures Mitsuki; it does not transform that pressure into respect for a refusal. Equally, recognizing Hime’s instrumental behavior should not erase the pain represented in the memory. The reading needs both causal understanding and a record of who bears the costs of her chosen response.

<a id="o13"></a>
#### O13 — The curtain exposes a failure of audience knowledge

**Source:** V01/05/i129–132. **Evidence status:** depicted misaddressed conversation and reveal; the full motive for Hime’s denial remains inferential.

Hime speaks toward the changing-space curtain, assuming Kanoko is the listener. She says that the desire to be liked by Mitsuki is an act and a lie. When Kanoko appears elsewhere, that assumed audience collapses: Mitsuki is behind the curtain.

The formal device gives material shape to a central limitation in Hime’s social method. She can control a face, a line, and sometimes a visible audience. She cannot guarantee the identity or knowledge of every person who receives the line. A backstage partition creates privacy without guaranteeing the kind of privacy she presumes. The withheld face is not just suspense decoration; it withholds exactly the information on which her communicative strategy depends.

It would be too quick to call this confession the final truth about all of Hime’s feelings. It is addressed to a friend who has just said her behavior is unlike her. Restoring their familiar account of Hime is a plausible motive. The later explicit statement that wanting Mitsuki’s regard is not a lie will revise the adequacy of the denial. That does not make the present statement inconsequential. Mitsuki hears a categorical disavowal, not the analyst’s charitable explanation of why Hime might have made it. [V01/05/i125–132; V01/06/i153–154.]

### 3.6 Shift 06: unchanged conduct can mean uncertainty, not indifference

<a id="o14"></a>
#### O14 — Hime predicts catastrophe and misreads ordinary ambiguity through it

**Source:** V01/06/i133–148. **Evidence status:** Hime’s forecast and anxiety directly narrated; others’ unspoken knowledge is not fully available.

Hime returns expecting that discovery will lead to exposure. Kanoko offers protection, but Hime decides she must handle the situation herself. This is not pure passivity. Her action remains organized by the belief that the dangerous person must be managed before a wider audience turns against her. [V01/06/i135–139.]

The unsettling fact is that Mitsuki continues much as before: enforcing the work setting, maintaining the public role, offering assistance, and issuing private corrections. Hime’s causal model does not predict this continuity. She is not reassured simply because no catastrophe has yet occurred; she searches ordinary interactions for signs that it is already happening elsewhere. Sumika’s remark and Kanoko’s conversation become threatening possibilities without becoming confirmed acts of betrayal. [V01/06/i140–147.]

The reader should not convert Hime’s fears into objective information-state updates. No scene here establishes that Kanoko has sold her out or that Sumika has been told the entire private confession. Nor does the absence of changed visible behavior prove that nobody else knows anything. The narrow result is that Hime’s expected public exposure has not been shown and that uncertainty is impairing her work.

Mitsuki brings her backstage for a direct conversation, while Mai makes space for the others to cover practical work. The movement is away from audience-mediated pressure and toward an exchange in which each participant can ask what the other is doing. It is a change of method, not yet a resolution. [V01/06/i147–149.]

<a id="o15"></a>
#### O15 — The question becomes which words can be believed

**Source:** V01/06/i149–154. **Evidence status:** explicit private statements and Hime’s internal revision; hidden motives remain open.

Mitsuki asks Hime to stop the act and explains that she knows Hime lies. Hime asks about exposure; Mitsuki states she will not do it. The promise is not retrospective proof of every private conversation, but it directly defeats the claim that immediate public exposure is the only response available to someone who has seen through Hime.

Hime then asks why Mitsuki’s treatment has not changed. Mitsuki’s answer changes the interpretive frame: she does not know which of Hime’s words to believe. What Hime had classified as the elder’s consistent, perhaps inexplicable disposition is at least partly an inability to determine how to respond. **Stable behavior can be produced by unresolved uncertainty.** [V01/06/i150–152.]

Hime’s resulting recognition is unusually important because it makes the difficulty reciprocal. Until now, she has repeatedly complained that Mitsuki changes between kindness and harshness and is therefore hard to understand. She now sees that her own mixture of strategic appeal and categorical denial can produce a corresponding problem for Mitsuki. The opacity is not solely a flaw in the person she is observing. Her own conduct helps create it. [V01/06/i151–153.]

Her statement that wanting Mitsuki’s regard is not a lie is therefore a local act of clarification. It need not mean that she has stopped acting forever, repudiated the wealthy-marriage ambition, or resolved every mixed motive. The narrower development is substantial enough: she attempts to distinguish a genuine wish from the general performance that has made it hard to identify. The statement is not framed as a declaration of romantic love. It concerns wanting to be liked and understood by this person. [V01/06/i154.]

There is also a limit to the repair. We have a non-exposure promise, recognition of a communication problem, and an attempted clarification. We do not have a comprehensive apology, agreement about the earlier sister-pact pressure, or demonstrated durability of changed behavior. The next page will immediately subject the provisional improvement to a more difficult test.

<a id="o16"></a>
#### O16 — The same person occupies the “good present” and “bad past” categories

**Source:** V01/06/i153–156, especially i155–156. **Evidence status:** present identity disclosure and visible identification; the explanation of the childhood event remains unresolved.

Hime treats Mitsuki’s non-exposure as evidence that she differs from the child who hurt her. In explaining the comparison, she names Yano Mitsuki. The person listening identifies herself as that same Yano Mitsuki and produces identification. The source does not leave the basic identity equivalence as a merely visual resemblance: a spoken claim and visible document converge. [V01/06/i155–156.]

Mitsuki also states that she had considered the possibility that Hime was pretending not to recognize her. That supplies a new higher-order information problem. One participant did not know who the other person was; the other could not tell whether this apparent ignorance was genuine or another act. The reader may now revisit earlier uncertainties as potentially history-conditioned, but the exact moment of Mitsuki’s recognition has not been dated by this disclosure. It must not be retroactively assigned to the first meeting as a settled fact.

The page turn from Hime’s naming of the remembered antagonist to the present identification joins two causal stories without reconciling them. Hime’s present evidence of restraint belongs to the same person as her remembered evidence of exposure. Neither can responsibly be discarded merely to produce a cleaner character judgment. The final page does not prove that the childhood report was malicious, that Hime’s recollection is wholly false, or that Mitsuki’s present restraint is a disguise for revenge.

It also does not depict the aftermath. There is no post-disclosure response from Hime sufficient to establish forgiveness, renewed rejection, or a new relationship agreement. The volume ends at an identity correction that makes earlier explanations inadequate and creates a stronger demand for further evidence.

The identification additionally separates the café’s hierarchy from ordinary biography: the card places Mitsuki in high-school year one, whereas Ayanokōji’s café role is a second-year student. The seniority Hime has been experiencing is an institutional performance relation, not something that can simply be read as a corresponding real-world school-year difference. [V01/02/i042; V01/06/i156.]

<a id="supplement"></a>
## 4. Separately bounded packaged material

<a id="o17"></a>
### O17 — Shift 6.5: support labor and an assumed “together”

**Source:** V01/6.5/i158–161. **Admission:** packaged supplementary short, fully inspected. **Chronology:** a school-club consultation; its exact placement relative to the six main chapters is not established here. It is not treated as an event occurring after i156.

Kanoko’s focalization makes visible the work of supporting Hime’s preferred self-presentation. Hime considers clubs for how they might enrich an attractive future profile, entertaining an overseas-literature option without a corresponding demonstrated interest in reading. Kanoko notices the mismatch and offers to investigate and help anyway. Her cooperation is not based on believing every part of the image. She can see its artificiality and still want to contribute to it. [V01/6.5/i158–159.]

That support should not be confused with proof that Kanoko shares Hime’s stated life project. The short establishes a willingness to assist and accompany Hime, not an independently endorsed theory of marriage or social status. Likewise, recognizing what a literature club does is not enough evidence to assign Kanoko a stable literary preference.

The final exchange qualifies a wholly one-sided account. Hime has assumed that the club they are selecting is one they will join together. Kanoko is not being regarded simply as research labor to discard after a choice has been made. The surprise is that Hime’s matter-of-fact expectation supplies precisely the shared future Kanoko had been trying to secure indirectly. Kanoko’s inward willingness to follow her anywhere remains more expansive than the specific mutual arrangement Hime articulates. [V01/6.5/i160–161.]

The episode therefore strengthens **within this supplementary lane** the evidence for attachment expressed as assistance and for Hime’s ordinary inclusion of Kanoko. It does not settle romance, reciprocity of intensity, or a final club choice. Hime’s dismissal of small part-time earnings also cannot be used to invent an exact date for the episode or to erase the constraints of the café recruitment. Keep the chronology open rather than forcing a convenient before/after placement.

### 4.1 Paratext use and exclusions

The afterword’s production discussion and prototype drawings remain statements about making the manga, not previously unseen stages of the characters’ fictional childhoods. The menu guide at i165 is useful edition apparatus but is not evidence that Hime or another character likes any listed food. Cover and back-cover compositions can frame the contrast between elegant closeness and antagonism, but they are not additional episodes of touching, conflict, or reconciliation. Publisher catalogues and promotional material introduce no further admitted works.

No mainline claim below depends on assigning chronological authority to the afterword, cover images, or the packaged short. Supplementary evidence is identified explicitly wherever it enters a record.

<a id="relationships"></a>
## 5. Directional relationship and attachment records

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_RELATIONSHIP_AND_ATTACHMENT_LEDGER.md`.

The records below are initial V01 additions. Their common prospective boundary is **i156**, not a later explanation of that page. Public role-state, private acknowledgment, desired state, and inferred attachment are recorded separately. A reciprocal friendship does not imply equal intensity; a performed couple-like image does not establish a private couple.

### Pair HM — Hime and Mitsuki

**WY1-REL01A — Hime → Mitsuki.** Hime’s working model moves from beautiful and kind elder, to unexpectedly hostile coworker, to real helper whose explanations remain frustrating, to someone who has not exposed her, and finally to the same person she remembers as having exposed her in childhood. Her belief about Mitsuki’s feelings is not resolved by that sequence: private hostility has been expressed, role-qualified approval has been given, and uncertainty about Hime’s words has been acknowledged. Hime wants to be chosen and liked; by i154 she expressly distinguishes that wish from a lie. The public label is Schwestern/elder sister. No reciprocal private affection, romantic commitment, or settled post-revelation trust is established. Her repeated pursuit crosses a stated refusal at i050–051; the resulting public pact cannot be used to erase that boundary. **Confidence:** high for the succession of expressed judgments and acts; moderate for the relative weight of attraction, approval-seeking, and fear. **Links:** [O03](#o03), [O05](#o05), [O10](#o10), [O11](#o11), [O15](#o15), [O16](#o16); WY1-C03/C05/C09/C10/C11.

**WY1-REL01B — Mitsuki → Hime.** Mitsuki resists the pairing, censures work failures and overfamiliarity, nevertheless supplies concrete assistance, and maintains the public sister role. In the final exchange she says she will not expose Hime and cannot tell which words to believe. She also reveals that she had considered Hime’s apparent nonrecognition potentially feigned. Her model of Hime therefore includes both practical unreliability and epistemic uncertainty, not simply “a novice I dislike.” Her private desired relationship is not stated sufficiently to settle. Neither staged possessive lines nor onstage touch establish romantic exclusivity. The final identity is certain within the scene; the timing and full meaning of her recognition remain open. **Confidence:** high for conduct and explicit statements; low-to-moderate for concealed affect and childhood-conditioned motive. **Links:** [O05](#o05), [O10](#o10), [O11](#o11), [O15](#o15), [O16](#o16); WY1-C03/C05/C10/C11.

**Current rupture/repair state:** public pair established; private relationship contested. A practical order error is repaired in Shift 04. A communication repair is attempted in Shift 06. The childhood identity disclosure reopens the explanatory problem before any sustained repair can be observed. Record neither “reconciled” nor “secretly mutually in love.”

### Pair HK — Hime and Kanoko

**WY1-REL02A — Hime → Kanoko.** Hime treats Kanoko as a familiar friend, intervenes when she is socially uncomfortable, speaks relatively freely with her, thanks her for support, and assumes more understanding than the scenes warrant. Concealing the café’s details combines embarrassment with an institutional restriction; it is not presented as a wish to end the friendship. Hime also misjudges Kanoko’s willingness to work and is unsettled when Kanoko criticizes her conduct or questions her investment in Mitsuki. Her accepted relationship is friendship; no matching claim of romantic desire appears. **Supplementary addition only:** the club short shows an ordinary assumption that they will choose and join something together. **Confidence:** high for friendship and practical inclusion; open for comparative priority or romantic content. **Links:** [O04](#o04), [O06](#o06), [O08](#o08), [O10](#o10), [O12](#o12), [O14](#o14); supplementary [O17](#o17); WY1-C07/C12/C14.

**WY1-REL02B — Kanoko → Hime.** Kanoko’s attention is unusually concentrated: she struggles to tell Hime she is cute, restores her mood by looking at Hime’s images, reacts strongly to Hime calling her cute, and experiences the café’s stranger treatment and sister privileges as threatening. She wants proximity and access to Hime and is willing to support her façade. She can nevertheless criticize her work, question her pursuit of Mitsuki, return to apply for the job, and offer protection. The evidence supports strong attachment, displacement distress, and a live exclusivity concern. Romantic attachment is a plausible working hypothesis, not a settled self-description or evidence of reciprocity. Photo viewing establishes intense attention; it does not by itself establish how every image was obtained or a general practice of nonconsensual surveillance. **Confidence:** high for selective attachment and observable distress; moderate for romantic interpretation and the generality of exclusivity expectations. **Links:** [O06](#o06)–[O08](#o08), [O10](#o10), [O12](#o12), [O14](#o14); supplementary [O17](#o17); WY1-C07/C12/C14.

**Current rupture/repair state:** the public stranger misunderstanding is followed by Kanoko entering the workplace, but all private meanings are not thereby settled. Kanoko’s reading of Hime’s pursuit of Mitsuki remains incomplete. Hime’s attempt to reassure her through the curtain is misaddressed, not a successful clarification to Kanoko. Neither friend has yet supplied the other with a complete account of the changing relationship network.

### Pair MS — Mitsuki and Sumika

**WY1-REL03A — Mitsuki → Sumika.** Mitsuki participates in practiced senior/junior banter and physical staging with Sumika, objects to her teasing and apparent diversion from work, and responds when Sumika presses the case for recognizing Hime’s improvement. The private relationship label and any romantic desire are unestablished. Public performance is not evidence that the two are privately paired. **Confidence:** high for repeated collaboration and friction; open for private attachment. **Links:** V01/01/i021–027; V01/04/i095–096; V01/05/i118–124; V01/06/i140–141; WY1-C02/C13.

**WY1-REL03B — Sumika → Mitsuki.** Sumika uses teasing both as customer-facing material and as pressure on Mitsuki’s handling of the junior. She can challenge severity, defend the usefulness of an imperfect first-year, and encourage praise backstage. Her interpretation that Mitsuki is merely embarrassed is a character reading, not privileged proof. The evidence supports a coworker able to influence the scene and question the pedagogy; it does not establish the source or full emotional meaning of that familiarity. **Confidence:** high for mediation; moderate for its benevolent versus scene-management motives. **Links:** V01/04/i095–096; V01/05/i118–124; WY1-C13.

**Workplace ties not inflated into dyadic syntheses.** Mai’s leverage over Hime and recruitment of Kanoko are preserved in the performance and agency records below. Their significance in V01 is demonstrably organizational; the available evidence does not require an independent attachment theory for every managerial tie.

<a id="performance"></a>
## 6. Persona, role, and performance records

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_PERSONA_ROLE_AND_PERFORMANCE_LEDGER.md`.

| Record | Actor / setting / audience | Conscious script and observed leakage | Concealment, recognition, and private effect | Evidence / confidence |
| --- | --- | --- | --- | --- |
| **WY1-PER01** | Hime; ordinary school; classmates and club recruiters | Deliberately cute, modest, considerate presentation; skilled refusal that preserves regard | Most classmates treat the presentation as natural. Reader and Kanoko have different access. A remembered exposure makes audience approval protective as well as rewarding. | O01/O06/O11/O12; high for deliberate performance, moderate for a complete motive hierarchy |
| **WY1-PER02** | Hime and Mitsuki; salon versus backstage; guests, each other, manager | Sister-role address, cross exchange, touch, praise, correction; Hime repeatedly tries to convert role approval into private approval | The audience ratifies a pair that had been privately refused. Later help is real while the permitted interpretation of that help remains contested. | O03–O05/O10–O11/O15; high |
| **WY1-PER03** | Sumika; street, staff area, salon | Abrupt shift from casual/intimidating presentation to refined senior; teasing and physical positioning recur with different social meanings | Hime recognizes the same person beneath costume/register change. Sumika’s apparent leisure can itself furnish the senior role and help organize other performers. | O02/O03/O09/O11; high for switching, moderate for how much every intervention is deliberately planned |
| **WY1-PER04** | Mai; recruitment and management versus fictional student hierarchy | Cute, junior-looking in-role presentation coexists with operational authority and staff direction | Actual managerial power is not reducible to fictional school seniority. Reputation and concern for another person are separately recruited as labor motivations. Injury fraud remains unproven. | O02/O04/O08/O14; high for authority and leverage; open for unstated motive |
| **WY1-PER05** | Kanoko; customer, ordinary friend, then first-year worker | Familiar attachment initially clashes with stranger etiquette; later real hesitation is received as an appropriate first-year quality | Her lack of polished speech need not be hidden to serve the scene. Hime’s praise has effects on her beyond its literal informational content. | O06–O09; high |
| **WY1-PER06** | Hime; backstage curtain; intended Kanoko, actual Mitsuki | Familiar-friend account of the self: everything about wanting Mitsuki’s regard is dismissed as acting | Audience identity is misrecognized. A line meant for one relationship becomes damaging evidence in another. Later candid clarification cannot erase that it was heard. | O13/O15; high for misaddress, moderate for why Hime disavows the wish |

The central pattern is not that a performance is either sincere or false. A single act may be strategically chosen, institutionally required, genuinely helpful, and emotionally consequential. These rows preserve those combinations instead of assigning one permanent authenticity label to each character.

<a id="information"></a>
## 7. Consequential propositions and information asymmetry

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_INFORMATION_DISCLOSURE_AND_MISREADING_LEDGER.md`.

| Proposition ID and bounded wording | Represented status at the V01 boundary | Knowledge, belief, and higher-order belief | Consequence / correction / evidence |
| --- | --- | --- | --- |
| **WY1-INF01 — Hime deliberately manages her ordinary image.** | Established by interior narration and conduct. This does not make every action or statement false. | Hime knows; reader is informed at the opening. Kanoko knows enough to discuss the performance. Mitsuki explicitly recognizes lying by the final conversation; the exact acquisition time of her knowledge is not fixed. The other staff’s awareness of café acting is not equivalent to knowledge of Hime’s entire ordinary strategy. | Hime’s fear of broader discovery organizes her choices. O01/O06/O12–O16. |
| **WY1-INF02 — Public Schwestern status and private reciprocal affection are the same fact.** | Rejected as an automatic equivalence. Public status is established; private reciprocity is not. | Hime sometimes tries to convert one into the other. Kanoko initially sees privileged intimacy without its private history. Guests witness a coherent relationship presentation, not the refusal. | Public pressure establishes the pair; private conflict persists. O04/O05/O07/O10. |
| **WY1-INF03 — Hime’s stranger treatment of Kanoko expresses personal rejection.** | Inadequate account of the depicted act. A workplace instruction directly explains the performance; embarrassment and self-protection also matter. | Hime knows the rule; Kanoko initially lacks the relevant explanation and personalizes the encounter. Staff know more about its operational context. | Distress, address conflict, and the spill follow. Entry into the workplace supplies more context, but no exhaustive mutual clarification is shown. O06–O08. |
| **WY1-INF04 — Mitsuki’s assistance proves either private affection or no private investment.** | Neither exclusive inference is established. Practical help is a fact; emotional interpretation remains open. | Hime treats assistance as kindness; Mitsuki insists on the sister-role explanation. Kanoko reads excessive reliance and criticizes Hime. | A repaired order does not close the relationship rupture. O10. |
| **WY1-INF05 — The listener behind the curtain is Kanoko.** | False in the depicted scene. | Hime assumes Kanoko is present. Mitsuki receives the disavowal. Kanoko’s appearance elsewhere corrects Hime’s and the reader’s immediate audience model. | An intended reassurance becomes a different interlocutor’s evidence of insincerity. O13. |
| **WY1-INF06 — Being seen through must produce immediate public exposure and rejection.** | Hime’s generalized rule is not borne out by the present sequence. Her childhood memory gives it a basis, not universal validity. | Hime predicts exposure; Kanoko offers protection. Mitsuki states she will not expose her. Hime’s suspicions about other staff are not independent confirmation that they were told. | Anxiety impairs work; the private conversation introduces another possible response. O12/O14/O15. |
| **WY1-INF07 — Mitsuki’s unchanged treatment means she has no uncertainty about Hime.** | Contradicted by Mitsuki’s explicit uncertainty about which words to trust. | Hime mistakes behavioral continuity for a settled internal position. Mitsuki’s answer corrects that inference. | Hime recognizes reciprocal opacity and attempts clarification. O15. |
| **WY1-INF08 — Ayanokōji Mitsuki and the remembered Yano Mitsuki are different people.** | Corrected by the final identity disclosure and identification. | Hime fails to recognize the identity until i156. Mitsuki had considered apparent ignorance possibly feigned; the scene changes that higher-order belief. The exact onset of Mitsuki’s recognition remains open. | Earlier present/past classifications must now refer to the same subject without pretending earlier Hime knew it. O12/O16. |
| **WY1-INF09 — Hime’s wish for Mitsuki’s regard is nothing but a lie.** | Hime’s categorical denial at i130 is revised by her express clarification at i154 and the surrounding interior narration. Mixed motives remain possible. | Mitsuki has heard both the disavowal and the subsequent clarification. Kanoko is not shown receiving a complete corrected account of the misaddressed exchange. | Repair requires distinguishing particular wishes, not merely the global categories “actor” and “liar.” O13/O15. |

These are deliberately material propositions. The ledger need not enumerate every piece of exposition or silently translate a character’s fear into a represented fact. Later evidence should append changed epistemic states to these IDs rather than overwrite what Hime, Mitsuki, Kanoko, or the reader could know at earlier points.

<a id="agency"></a>
## 8. Agency, boundaries, rupture, and repair

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_AGENCY_BOUNDARY_RUPTURE_AND_REPAIR_LEDGER.md`.

| Event ID | Act, available alternatives, and constraint | Boundary / consequence | Repair disposition and rival account |
| --- | --- | --- | --- |
| **WY1-AG01** | Mai recruits Hime after the collision; Hime attempts departure and later an illness excuse, showing that refusal/exit is imaginable but pressured. Sumika helps obstruct easy withdrawal. | Hime’s helpful image is made costly to contradict; the work and its duration are not fully understood at entry. | No injury-fraud finding. Practical staffing need and opportunistic leverage may coexist. O02. |
| **WY1-AG02** | Mitsuki privately refuses the proposed pair. Hime can hear and accept that refusal, but instead moves the issue into public performance. | Audience pressure changes the cost of refusal. Public sisterhood results without resolving private assent. | No apology or explicit repair of this boundary crossing is completed in V01. Do not reclassify it as harmless because the audience enjoys it. O05. |
| **WY1-AG03** | Hime follows the stranger instruction with Kanoko, then breaks role in alarm after the spill. | Workplace performance conflicts with friendship recognition; the mishap makes the cost visible. | Immediate apology/customer assistance addresses the accident, not every relational misunderstanding. The spill is not established as intentional aggression. O07. |
| **WY1-AG04** | Kanoko accepts responsibility, is invited to help Hime, and returns to apply. Hime’s questioning and Mai’s interview provide evidence of an express decision, not merely passive absorption. | Genuine care becomes a staffing resource; Hime cannot simply dictate Kanoko’s choice. | Record willingness and managerial persuasion together. No invented contract terms, wages, or permanent obligation. O08. |
| **WY1-AG05** | Kanoko offers practice; Hime resists the implied incompetence and tries to perform alone. Mitsuki records the failed order and supplies practical help. | Hime’s preferred self-image impedes accepting support; an actual service failure is remedied. | **Task repaired; relationship not repaired.** Gratitude occurs, followed by disagreement over the meaning of assistance. O09/O10. |
| **WY1-AG06** | Hime asks customers for slower, clearer orders and obtains a better work result. | Acknowledged need becomes compatible with a pleasing performance; less concealment can improve practical agency. | Improvement is recognized, though Mitsuki limits praise to the role. It does not prove that every later task will be handled well. O11. |
| **WY1-AG07** | Mitsuki initiates a private conversation; Hime eventually asks directly about exposure and unchanged behavior instead of relying only on audience pressure. | Specific questions replace some speculative mind-reading. Mitsuki states a non-exposure commitment. | **Communication repair attempted.** No sustained post-repair behavior is available before the identity disclosure. O14/O15. |
| **WY1-AG08** | Hime says her wish for Mitsuki’s regard is not a lie; Mitsuki discloses her identity after Hime names the remembered antagonist. | Present sincerity claim and past grievance now belong to the same relationship. | **Rupture/repair OPEN at i156.** No final forgiveness, rejection, apology, or reconciliation is depicted. O15/O16. |

The record avoids a global verdict such as “toxic.” It locates who initiates a pressure, whose refusal or need is at issue, what actual option is evidenced, and what the immediate act does or fails to repair. Explanation of a fear is not endorsement of the conduct it motivates; genuine care does not eliminate the possibility of possessive or coercive consequences.

<a id="chronology"></a>
## 9. Chronology, memory, and retrospection

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_CHRONOLOGY_MEMORY_AND_RETROSPECTION_LEDGER.md`.

| Record | Presentation time / event class | Diegetic ordering and confidence | Interpretation boundary |
| --- | --- | --- | --- |
| **WY1-T01** | Opening and chapter-opening academy tableaux; depicted/in-role or introductory compositions | Not every introductory composition establishes an additional chronological event. School-frame exposition and repeated poses must be distinguished from the subsequent scene sequence. | Do not infer a second actual academy or extra unrecorded shifts merely from framing images. V01/01/i001–004; V01/02/i037–038. |
| **WY1-T02** | Ordinary school → collision/recruitment → first café work; depicted present | High confidence in this narrative order. Hime’s age fifteen and spring setting are stated at the first chapter’s close. Exact calendar dates are not supplied. | The initial staffing expectation is extended through Mai’s fracture/recovery report; the medical fact is not independently verified. V01/01/i005–036. |
| **WY1-T03** | Sister-role formation → Kanoko’s discovery/visit → application → shared work; depicted present | High confidence in sequence; the next-day transition after the visit is explicit at i082. No exact total elapsed-day count is imposed. | Online visibility connects scenes without giving Kanoko knowledge of all backstage events. V01/02/i043–060; V01/03/i061–084; V01/04/i085–108. |
| **WY1-T04** | Childhood material anticipated at i109 and expanded at i126–129; remembered/reported past | Primary-school period is supported by Hime’s framing; it precedes the middle-school friendship context with Kanoko. Exact grade, date, complete prior friendship sequence, and event duration remain open. | Chronological placement is more secure than Hime’s complete causal/moral explanation. No separate Mitsuki account has yet been read. |
| **WY1-T05** | Curtain discovery → later work anxiety → private clarification and identity disclosure; depicted present | High confidence in the narrative sequence. The final conversation identifies the current Mitsuki with the named person in the recollection. | Link the identity now; do not change Hime’s earlier knowledge state or backdate Mitsuki’s recognition without evidence. V01/05/i130–132; V01/06/i133–156. |
| **WY1-T06** | Packaged Shift 6.5 school-club consultation; supplementary depicted episode | The scene belongs to the school-life setting. Its exact placement relative to recruitment, work shifts, and the mainline cliffhanger is **OPEN**. | Publication order is not diegetic order. Preserve any future chronology reconciliation explicitly. V01/6.5/i158–161. |

The final disclosure is a **within-V01 revelation**, not permission to replace the earlier memory with an unwritten, supposedly definitive version. Later retrospective evidence must distinguish changes to event facts, motives, interpretations, and the distribution of knowledge.

<a id="speech"></a>
## 10. Written Japanese speech, address, and register

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_JAPANESE_SPEECH_ADDRESS_AND_REGISTER_LEDGER.md`.

These are observations about manga wording and lettering. No claim about acoustic pitch, timbre, breath, timing in seconds, or voice-actor delivery is made. Exact excerpts are kept short; the supplied English explanations are analytical glosses, not an official translation.

### WY1-JP01 — Image, acting, and lying are not one word

Hime’s opening account uses **ソトヅラ** for outward presentation and **演技** for acting. Later accusations and disavowals use **嘘**. These terms enter related but non-identical judgments: cultivating an appearance, consciously performing, and asserting something untrue are not automatically the same act. Her truthful request for slower orders is performed attractively; her curtain disavowal claims that a particular wish is false; Mitsuki later cannot tell which particular words deserve belief. **Locators:** V01/01/i007–008, internal narration; V01/05/i115–116 and i130; V01/06/i149–154. **Confidence:** high for the lexical distinction; the precise sincerity of every line remains a claim-level question. **Links:** WY1-C01/C02/C08/C10.

### WY1-JP02 — “Elder sister” changes from Hime’s interpretation into an institutional address

Hime’s early **お姉様** is followed by correction because the café assigns special consequences to sister terminology. After the pact, sister address is required or encouraged in circumstances where it had earlier been rejected. The apparent inconsistency is partly a change in role-state, not simply an arbitrary mood. Hime’s internal designation of the striking elder as **おねーさん** also should not be treated as identical to the café’s formal bond. **Locators:** V01/01/i032–035; V01/02/i043–046; V01/03/i068–069. **Confidence:** high for the contextual shift. **Links:** WY1-INF02; WY1-PER02.

### WY1-JP03 — Public elegance and private rebuke do not uniquely disclose a complete self

Mitsuki’s salon language participates in the refined student script; private corrections include markedly more confrontational address, including **あんた／アンタ**. The hostile aside on i059 is directed into the intimate distance created by the public sister scene. It is an actual adverse utterance, not a line that the analyst may automatically translate into affection. Later private speech can also acknowledge uncertainty. The recurrent contrast supports role-conditioned switching, not the rule that every backstage sentence is an unqualified final truth. **Locators:** V01/02/i058–059, bottom aside on i059; V01/04/i107, central rebuke; V01/06/i149–152. **Confidence:** high for switching, open for the full affect behind it. **Links:** WY1-C02/C05/C10.

### WY1-JP04 — Familiar naming becomes contested access

Kanoko’s **ひめちゃん** marks an established familiar relationship. In the café, that familiar form encounters a rule while Mitsuki’s use of **陽芽** is supported by the new sister relationship. The contrast has consequences because Kanoko sees another person authorized to occupy an intimate position while her own familiar recognition is blocked. It does not prove that dropping an honorific always means romantic intimacy or that Hime has privately transferred her affection. **Locators:** V01/03/i072–076, especially the address correction at i074 and familiar name in the accident response at i076. **Confidence:** high. **Links:** WY1-REL02B; WY1-INF03.

### WY1-JP05 — Hesitation is relationship- and situation-conditioned

Kanoko’s interrupted attempt to tell Hime she is cute differs from her relatively direct criticism of Hime’s work and her questioning of the Mitsuki pursuit. Her difficulty is not an invariant inability to express disagreement. With customers, halting self-introduction is received as appealing first-year behavior. Written interruption, ellipsis, incomplete phrases, and reactions support these contrasts; they do not establish a clinical condition or an acoustic delivery profile. **Locators:** V01/03/i064–066 and i080–081; V01/04/i100–101, i106–108; V01/05/i125–126. **Confidence:** high for contextual variation, moderate for a generalized speech policy. **Links:** WY1-C07/C12.

### WY1-JP06 — Hime’s practical register improves when it tells the listener what she needs

The order-taking failure is not remedied solely by prettier speech. Hime explicitly asks for slower, clearer ordering and promises to repeat information as needed. This is a pragmatic change in how a listener is enlisted to cooperate. Her desire to be praised remains present, but a genuine task limitation becomes communicable rather than concealed. **Locators:** V01/04/i099–103; V01/05/i115–116, order-taking balloons. **Confidence:** high. **Links:** WY1-AG06; WY1-C08.

### WY1-JP07 — The ending separates a sincerity question from an identity assertion

Mitsuki’s **どの言葉を信じればいいのか** names uncertainty about which words to believe. Hime’s subsequent clarification addresses the wish to be liked, not a total guarantee that she will never perform again. The final emphatic identification as **矢野美月** settles a different question: who the current interlocutor is. A statement can resolve identity while leaving intention and history unresolved. **Locators:** V01/06/i152, central statement; i154, Hime’s clarification; i156, identification and final large balloon. **Confidence:** high. **Links:** WY1-INF07/INF08/INF09; WY1-C10/C11.

**Idiolect limit.** V01 supports repeated, condition-dependent features, especially for Hime and Mitsuki. It does not support a complete speech generator for unfamiliar situations. Names, honorifics, and punctuation should be carried forward with audience and role-state attached, not extracted into a decontextualized list of “character catchphrases.”

<a id="visual"></a>
## 11. Manga form, staging, gaze, and embodied interaction

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_VISUAL_FORM_STAGING_AND_GAZE_LEDGER.md`.

### WY1-VIS01 — The visible performance and its production occupy different graphic registers

Hime’s attractive public face repeatedly coexists with exaggerated scheming, panicked, or frustrated interior representations. The visual discrepancy gives the reader access to effort and intention that the in-scene audience lacks. It makes her accomplished and comic without requiring the “uglier” caricature to be a literal hidden physical self. The device becomes more consequential when the apparently attractive line is itself an attempt to hide uncertainty. **Locators:** V01/01/i007–009; V01/02/i052–056; V01/05/i113–120. **Interpretive alternative:** an exaggerated expression can mark comic emphasis without uniquely specifying motive. **Confidence:** high for the repeated contrast. **Links:** WY1-C01/C08.

### WY1-VIS02 — Ornamental intimacy is not a reliable detector of falseness

Flowers, decorative borders, enlarged faces, and idealized poses support the academy atmosphere and the staff’s successful interactions. Similar emphasis also accompanies Kanoko’s strongly affected response to Hime’s praise. The same visual vocabulary can frame a commercial performance and a genuine response to recognition. It should not be converted into a rigid code in which flowers mean “fake” and plain panels mean “real.” **Locators:** V01/01/i021–023; V01/02/i044, i058; V01/03/i079–081; V01/05/i120–122. **Alternative:** some ornamental images are introductions or idealized illustrations rather than continuous diegetic action. **Confidence:** high for recurrence; psychological interpretation remains scene-specific. **Links:** WY1-C02/C07.

### WY1-VIS03 — Nearness can carry contrary messages at once

Sumika’s positioning and Mitsuki’s tie adjustment show why proximity cannot be read as transparent affection. The sister tableau provides bodily nearness and a public image of care; the hostile aside at i059 uses that same nearness to reach Hime without becoming the audience’s shared message. The relevant evidence is the arrangement of bodies, the congratulating spectators, and the segregated dialogue, not an inferred vocal timbre. **Locators:** V01/01/i013, i025–026; V01/02/i058–059. **Alternative:** later closeness may carry different meanings; this configuration does not define all touch in the series. **Confidence:** high. **Links:** WY1-AG02; WY1-C03.

### WY1-VIS04 — Objects make role-state and work-state retrievable

The crosses externalize a publicly recognized relation. The tray, order notes, and usable replacement slip externalize actual service demands and failures. The final identification externalizes a correction that might otherwise remain a claim of resemblance. These objects do different kinds of evidentiary work: a cross certifies the café’s represented pact, not private love; a correct order records assistance, not its entire motive; an identification confirms identity, not moral innocence. **Locators:** V01/02/i044, i050, i059; V01/04/i099–105; V01/06/i156. **Confidence:** high. **Links:** WY1-C03/C05/C11.

### WY1-VIS05 — A withheld face is a withheld audience model

At the curtain, Hime addresses an unseen presumed listener. The return of Kanoko and the reveal of Mitsuki reorganize the scene’s information without requiring the spoken words to change. The full-page confrontation at i132 concentrates the consequences of that misrecognition in the newly visible interlocutor. The mechanism is not simply “surprise”: the face has been withheld at precisely the point where Hime’s choice of language depends on knowing whose face it is. **Locators:** V01/05/i130–132. **Alternative:** the page does not reveal everything Mitsuki knew before overhearing. **Confidence:** high. **Links:** WY1-INF05/INF08.

### WY1-VIS06 — Present and remembered faces invite comparison before explanation is complete

Hime’s fear-driven comparison places the current elder and the remembered child in an interpretive relation before the final identification settles their shared identity. The resemblance supports the narrative’s preparation, but earlier similarity must not be turned into a claim that Hime consciously recognized her. The present panels remain focalized through a character whose categorization is still wrong. **Locators:** V01/05/i126–129; V01/06/i137, i153–156. **Confidence:** high for the formal comparison; exact earlier recognition by Mitsuki remains open. **Links:** WY1-T04/T05; WY1-C09/C11.

### WY1-VIS07 — The last page turn joins categories rather than resolving the relationship

Under the EPUB’s spread assignments, i155’s naming of the remembered antagonist is followed across a page turn by i156’s identification, Hime’s surprise, and Mitsuki’s enlarged declaration. The effect is to force two previously separated interpretations onto one person. The enlargement gives the disclosure terminal weight, but the “to be continued” endpoint withholds the response that would determine the next relational state. **Locators:** V01/06/i155–156; EPUB spine/spread metadata. **Alternative:** reader software can change the physical experience of a turn; the sequential withholding remains even in single-page display. **Confidence:** high for source sequence and design, bounded for actual reader-interface experience. **Links:** WY1-C11.

The formal record does not infer motives from a single eye shape, blush, or pose. It uses contrasts across audience states, repeated compositions, linked wording, and subsequent actions. It also keeps manga form distinct from anime framing, camera motion, or voice performance.

<a id="claims"></a>
## 12. Initial claims and counterreadings

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md`.

All claims below are **first eligible at V01**. They are initial records, not transitions from an earlier corpus claim. Their prospective wording must be preserved when later evidence changes the mature interpretation. Confidence concerns the bounded formulation, not an entire character or relationship. Future changes use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`, with the new evidence and affected homes named.

| Claim ID | Exact bounded formulation | Supporting observations | Counterevidence, limit, or live alternative | V01 confidence / disposition |
| --- | --- | --- | --- | --- |
| **WY1-C01** | Hime’s practiced individual impression management does not transfer automatically to a shared role system or practical service competence. | O01/O03/O09/O11 | She learns and performs better; the claim is a domain distinction, not global incompetence. | High; supported interpretation |
| **WY1-C02** | Performance in V01 can carry genuine help, truthful information, and real emotion; backstage access does not guarantee complete candor or self-knowledge. | O03/O05/O10/O11/O13/O15 | Some performances do deceive, and private rebukes can communicate real hostility. Neither direction of the distinction is absolute. | High; supported interpretation |
| **WY1-C03** | The public sister pact is established through a sequence that includes a private refusal and audience-mediated pressure, not demonstrated private reciprocity. | O04/O05 | Mitsuki ultimately participates; that participation establishes the role-state but does not erase the preceding refusal or identify every motive. | High; supported interpretation |
| **WY1-C04** | The café’s public visibility and restrictions on real-world familiarity can create relational misunderstandings across audience boundaries. | O04/O06/O07 | Hime’s embarrassment and Kanoko’s attachment also contribute; management’s rule alone is not the complete cause. | High; supported interpretation |
| **WY1-C05** | Mitsuki’s practical assistance is established more securely than either “she privately loves Hime” or “she has no private investment.” | O10/O11/O15 | She explicitly invokes role obligation and voices hostility; those statements constrain rather than fully settle motive. | High for assistance; motive OPEN |
| **WY1-C06** | Mai uses reputational and relational leverage in recruitment, but V01 does not establish fabricated injury or a staged accident. | O02/O08 | An actual staffing problem could coexist with opportunism. The absence of proof of fraud is not proof that every report is true. | High for leverage; injury truth OPEN |
| **WY1-C07** | Kanoko shows intense selective attachment and distress at apparent displacement; romantic attachment is plausible but neither labeled nor reciprocally settled in V01. | O06/O07/O08/O12 | Friendship, admiration, insecurity, and a desire for continuity can explain parts of the pattern. No single blush settles its category. | High for attachment; moderate romantic hypothesis |
| **WY1-C08** | Hime’s improved order-taking shows that communicating a real limitation can strengthen rather than destroy an attractive performance. | O09/O11 | One successful adjustment does not establish a general abandonment of concealment or equal performance across all tasks. | High; supported interpretation |
| **WY1-C09** | Hime’s remembered exclusion makes universal approval partly a defense against exposure, without canceling her wealth aspiration or proving the memory’s entire causal account. | O01/O12/O14 | Pride, pleasure in admiration, and instrumental ambition remain active. Only one childhood perspective is supplied. | High for her present interpretation; history OPEN |
| **WY1-C10** | The late private conversation makes their incomprehension reciprocal: Hime’s mixed messages also leave Mitsuki uncertain how to respond. | O13/O15 | This does not equalize every responsibility or negate the impact of Mitsuki’s harsh conduct. Hime’s clarification has no demonstrated long-term success yet. | High; supported interpretation |
| **WY1-C11** | The final identity disclosure joins Hime’s adverse childhood category and favorable present category in one person while leaving the childhood motive and relationship outcome unresolved. | O12/O15/O16 | Changed behavior over time, missing context, and mistaken interpretation remain alternatives. Identity is not itself exoneration or condemnation. | High for identity and unresolvedness |
| **WY1-C12** | Hime and Kanoko’s friendship includes genuine support and disagreement, but each overestimates some aspect of her understanding of the other. | O06/O08/O10/O12/O13/O14 | Some misunderstandings arise from incomplete information rather than a stable failure of empathy. Friendship need not be either wholly mutual in intensity or wholly exploitative. | High; supported interpretation |
| **WY1-C13** | Sumika’s teasing and apparent role-leisure can perform scene-management and mediating work; “merely lazy” is inadequate to her V01 conduct. | O03/O09/O11; VIS03 | Not every tease is benevolent, and sustained practical workload is not quantified. Her private motives remain undercovered. | Moderate-to-high; bounded interpretation |
| **WY1-C14** | In the packaged short, Hime assumes shared activity with Kanoko, while Kanoko’s willingness to assist and follow her is especially expansive. | O17 only | The episode’s chronology is unsettled. It establishes neither a completed club choice nor romance, and must not overwrite the i156 mainline state. | High within supplemental boundary |

**Within-volume revisions, not inherited-claim adjudications.** The chapter sequence narrows the early “private harshness = complete true self” reading, revises “Hime’s wealth ambition fully explains universal approval,” and rejects the assumed separation of present Mitsuki from childhood Yano. Those are recorded as V01’s own evidential progression. They are not presented as corrections to nonexistent earlier canonical volume files.

<a id="predictions"></a>
## 13. Prospective predictions and adjudication conditions

These forecasts were formulated from the completed V01 source boundary. **All remain OPEN.** They authorize no further reading. V02 is the next potential evidentiary opportunity after V01 integration and separate continuation authorization; if a test situation is absent, the forecast stays open rather than being scored as a failure or success. These are source-bounded forecasts and model tests, not a certified blind benchmark.

| Prediction ID | Forecast / rationale at V01 | Confirmation condition | Disconfirmation or revision condition | Initial confidence / route |
| --- | --- | --- | --- | --- |
| **WY1-PR01** | A fuller account of the childhood disclosure will qualify the explanation that Mitsuki’s purpose was simply to hurt Hime. Present non-exposure and uncertainty make a single uncomplicated malicious motive insufficiently secure. | New direct testimony or depicted context identifies a consequential motive, assumption, or misunderstanding omitted from Hime’s current explanation. | Independent contextual evidence supports the simple harmful-purpose account without meaningful qualification; alternatively, evidence shows present restraint results from a change that leaves the earlier account intact. | Moderate; chronology, information, HM relationship, C09/C11 |
| **WY1-PR02** | The next substantial private exchange about the relationship will require distinguishing Hime’s particular sincere wishes from her general practice of acting, rather than treating “she acts” as sufficient resolution. | A subsequent exchange explicitly tests, clarifies, or changes trust in a particular statement or intention. | The issue is affirmatively resolved without that distinction, or new evidence shows the i154 clarification itself was wholly instrumental in a way that requires revising C10. | Moderate; information, speech, agency, C02/C10 |
| **WY1-PR03** | Credible growth in Hime–Mitsuki private closeness would trouble Kanoko even if Hime’s practical work competence improves. | A scene supplies both a credible private-closeness cue and Kanoko’s evaluative response, with concern or an attempt to preserve her access not reducible to a current work failure. | Comparable, understood private closeness is repeatedly or explicitly accepted without the predicted concern, or Kanoko gives a different well-supported account of her earlier distress. | Moderate; HK relationship, C07/C12 |
| **WY1-PR04** | Under an unfamiliar work demand, Hime’s willingness to acknowledge a specific limitation will be more useful than façade-only concealment, provided the other participants can cooperate. | A reasonably comparable task shows clarification/requested help improving the practical outcome, not merely increasing applause. | Comparable task evidence repeatedly shows no such benefit, or role/institutional constraints make candor materially worse and require narrowing the rule. | Moderate, conditional; agency and reconstruction test, C01/C08 |
| **WY1-PR05** | If the sister role continues while private conflict remains unresolved, it will continue to supply reasons or opportunities for practical support without thereby settling private affection. | An actual assistance event occurs during a still-contested private state and is connected to the role or its responsibilities. | Explicit abandonment, sustained refusal of those responsibilities, or source evidence that the supposed support was not real requires rejection or revision. If the pair ends immediately, test conditions must be reconsidered rather than assumed. | Moderate; role and HM relationship, C03/C05 |

**Non-predicted outcomes.** No claim is made here about the end of the series, a future romantic pairing, the length of a conflict, publication completion, or any character’s eventual moral judgment. Those outcomes are neither established by the source inventory nor needed to preserve a useful V01 hypothesis set.

<a id="readiness"></a>
## 14. Cast discovery and reconstruction-readiness checkpoint

**Canonical destination:** `03 Longitudinal Ledgers/WATAYURI_CAST_AND_RECONSTRUCTION_READINESS.md`.

These are local, evidence-bounded decisions, not global registry enrollment or A–E capability grades. **First observed volume: V01 for all five subjects. Last repository-closed volume at the supplied base: none. Source inspected in this contribution: V01.** The latter must not be confused with the former before integration.

### WY1-CAST-HIME — 白木陽芽 / Shiraki Hime

**Identity:** ordinary name introduced in the school sequence; café role 白鷺陽芽 / Shirasagi Hime. The name distinction is documented rather than collapsed into two characters. **Evidence density:** high within this volume across school performance, friendship, labor, private thought, remembered exclusion, practical failure, and a local attempt at sincere clarification. [V01/01/i005, i020; O01–O16.]

**Working reconstruction seed:** when ordinary admiration can be obtained without apparent loss, Hime tends to choose the socially pleasing response, including graceful refusal. When rejection threatens her universal-approval rule, she intensifies the effort to be chosen and may recruit an audience rather than respect a private refusal. When fear of exposure dominates, she treats ambiguous conduct as potentially hostile. A direct assurance and a concrete explanation can permit a more candid question or wish. These are condition-dependent rules, not assertions that she always lies or cannot care. O08, O11, and O15 are important limits on a rigid manipulator model.

**Everyday evidence:** Hime’s handling of classmates and club invitations is available, as is the supplementary club-profile conversation. There is not enough evidence for a complete leisure, food, domestic, or moral-preference inventory. Serving an item does not make it a favorite; a strategically attractive club is not an intrinsic interest.

**Separate gate decisions:** a character evidence ledger is **justified as a next-stage retrieval candidate**, with this reading already supplying initial evidence; no additional standalone file is created here. An operational model remains **DEFERRED** pending more direct history, repeated cross-state tests, and genuine held-out validation. A mature monograph is **DEFERRED**, principally because the final identity changes the interpretation of the central relation. Portable/crossover simulation is **DEFERRED**. **Next need:** her response to the shared-past disclosure and whether she can preserve specific candor under renewed threat.

### WY1-CAST-MITSUKI — 矢野美月 / Yano Mitsuki; café 綾小路美月 / Ayanokōji Mitsuki

**Identity:** the real-name equivalence is first established for Hime and the reader at i156. Earlier records must preserve the café-name knowledge boundary. **Evidence density:** high for present conduct and role switching, sharply limited for independent childhood perspective and concealed motive. [O03/O05/O10/O11/O15/O16.]

**Working reconstruction seed:** she enforces the café’s role requirements, distinguishes role praise from broader personal approval, responds sharply to Hime’s confusing conduct, and can provide real assistance while the relationship is strained. When uncertainty becomes a practical problem, she can initiate direct private questioning. A model that predicts only rejection would miss the assistance; a model that predicts every rebuke is concealed love would ignore explicit boundaries and underdetermination.

**Separate gate decisions:** evidence-ledger candidate **justified**, but any historical section must preserve Hime’s remembered account as such. Operational model **DEFERRED**, because the volume ends exactly where a major latent condition becomes visible. Monograph **DEFERRED**; portable simulation **DEFERRED**. **Next need:** her account of the earlier relationship, the timing of recognition, and the content of her desired present relationship. The final card’s real school year also warns against carrying café seniority into ordinary biography.

### WY1-CAST-KANOKO — 間宮果乃子 / Mamiya Kanoko; café 雨宮果乃子 / Amamiya Kanoko

**Identity:** surname established in the ordinary-school scene; café role-name assigned on entry. **Evidence density:** substantial for selective attachment, social inhibition, response to praise, support behavior, work participation, and disagreement with Hime. Supplementary focalization adds a distinct support-labor context. [V01/03/i063; V01/04/i087; O06–O10/O12/O14/O17.]

**Working reconstruction seed:** unfamiliar social attention can inhibit her speech, whereas concern for Hime can produce initiative, visits, employment, criticism, and offers of protection. Apparent restriction of her access to Hime can become distressing before she understands its cause. She is not simply passive, and familiarity with Hime’s acting does not guarantee recognition of every sincere change. The romantic hypothesis must remain distinguishable from the observed attachment pattern.

**Separate gate decisions:** evidence-ledger candidate **justified**, with mainline and supplementary lanes separate. Operational model **DEFERRED**; monograph **DEFERRED**; portable simulation **DEFERRED**. **Next need:** less Hime-centered ordinary behavior, her own articulated values and relationship expectations, and evidence of how she responds when another bond is privately rather than merely theatrically significant.

### WY1-CAST-SUMIKA — 橘純加 / Tachibana Sumika, source-used café identity

**Identity boundary:** use the name supplied in V01’s café context; no uninspected ordinary surname is imported. **Evidence density:** recurring but concentrated in the workplace, with a brief street presentation. Role competence, teasing, audience awareness, and some mediation are supported; private life and interior motivation remain thin. [V01/02/i042; O02/O03/O09/O11; WY1-REL03A/B.]

**Working reconstruction seed:** she can change register and presentation quickly, use teasing to sustain the salon, and challenge an overly narrow account of how a novice should perform. This does not establish that all apparent indolence is strategically useful or that every interpretation she offers of Mitsuki is correct.

**Separate gate decisions:** **retain distributed evidence in the current ledgers**; a dedicated evidence file is deferred until it provides retrieval value beyond these records. Operational model, monograph, and portable simulation are **DEFERRED** independently. **Next need:** private goals, ordinary choices, and further evidence distinguishing role persona, managerial assistance, and personal attachment.

### WY1-CAST-MAI — 御子柴舞 / Mikoshiba Mai, introduced manager

**Identity boundary:** retain the name introduced by the source without inventing a separate undisclosed legal/café naming distinction. Her fictional student positioning is not her actual managerial rank. **Evidence density:** substantial for operational behavior and recruitment; limited for private motives, biography, and independent verification of the injury account. [V01/02/i042; O02/O04/O08/O14; WY1-PER04.]

**Working reconstruction seed:** she notices socially usable traits, reframes help as participation in the café’s work, and protects the shared fiction while managing practical staffing needs. Different recruits supply different motivations. This supports opportunistic organizational skill, not a universal claim of fraud or benevolence.

**Separate gate decisions:** **retain distributed institutional evidence**; dedicated evidence ledger deferred pending a broader need. Operational model, monograph, and portable simulation are **DEFERRED**. **Next need:** less instrumentally framed conduct, her account of the business’s priorities, and any later source resolving the injury or employment arrangement.

**Validation status for all seeds:** the rules above are explanatory hypotheses checked against the inspected V01 scenes, not held-out predictions that have already passed. No operational reconstruction, full monograph, or cross-series simulation is declared validated merely because this deep reading is substantial.

<a id="exit-state"></a>
## 15. Frozen exit state, open questions, and synthesis routing

### 15.1 Mainline exit at V01/06/i156

Hime, Mitsuki, Kanoko, Sumika, and Mai are established as the relevant inspected cast. The café’s Schwestern mechanism, role-name distinctions, audience expectations, secrecy rule, and practical service requirements have all been demonstrated. Hime and Mitsuki occupy the public sister relationship; their private relation remains unsettled. Kanoko has joined the workplace, bringing an existing friendship and selective attachment into its role system. [O03–O10.]

Hime has improved a specific aspect of work, encountered a limit to the belief that performance guarantees approval, and recognized that her own mixed signals make her difficult for Mitsuki to understand. She has not abandoned her general self-fashioning project or the wealthy-marriage ambition. Mitsuki has supplied practical help, a non-exposure statement, an account of uncertainty, and her real identity. None of those facts supplies a complete private motive or a completed reconciliation. [O11–O16.]

The final correction is exact and consequential: the remembered Yano Mitsuki and the present Ayanokōji Mitsuki are the same person. The volume gives no post-revelation exchange adequate to close the relationship outcome. That is the frozen mainline boundary. The separately packaged short cannot be used to provide a falsely reassuring “afterward.”

### 15.2 Questions intentionally left unresolved

The main open historical issue is the childhood disclosure: what preceded it, what was said in context, what Mitsuki intended, and how each child understood the other. The main present issue is how the newly shared identity knowledge changes trust and the meaning of the sister role. A related question is when Mitsuki recognized Hime and what she thought Hime knew. These are required questions for later interpretation, not evidence gaps to fill from summaries or model memory.

Kanoko’s attachment category, the range of her exclusivity expectations, and Hime’s awareness of their unequal intensity remain open. Mitsuki’s private desired relationship and the private character of her bond with Sumika remain open. Mai’s injury report and broader motives remain unverified. The exact placement of Shift 6.5 remains open. None of these unresolved story questions prevents a complete, honestly bounded V01 reading.

### 15.3 Specialist routing without premature new artifacts

The material supplies recurring questions for future synthesis: **performance and authenticity** (C01/C02/C08/C10); **public institutions and private boundaries** (C03/C04/C06); **recognition, disclosure, and trust** (C09/C10/C11); **friendship, attachment, and unequal understanding** (C07/C12/C14); and **visual/address systems that distribute intimacy** (JP02/JP04; VIS02/VIS03/VIS05/VIS07).

These are routing responsibilities, not assertions that five mature specialist studies now exist. The present volume reading and nine cumulative homes can preserve the evidence without producing empty specialist files. A later specialist should make an argument across recurring evidence and counterevidence, not merely collect every instance of a word or pose.

<a id="handoff"></a>
## 16. Original integration handoff and transaction manifest (historical)

This section records the producer-stage packet at transfer time, including its then-pending publication state and the pinned before-blobs. Its forward-looking instructions are historical after the coordinated V01 transaction. Consult the current entrypoint and Git history for the live branch and publication state.

### 16.1 Assignment, base, and preservation contract

| Field | Record |
| --- | --- |
| Transfer ID | `WATAYURI-V01-20260928-READING-01` |
| Requested output | One downloadable Markdown V01 analysis under the supplied pinned protocols |
| Repository | `deep-blue-zero/anime-manga-ln-games-analysis` |
| Immutable analytical base | `bc596633e8fc53e50f14892ad29f77017f166a05` |
| Canonical entrypoint | `series/watayuri/CURRENT_STATE_AND_CORPUS_MAP.md` |
| Delivered artifact | `WATAYURI_V01_DEEP_READING.md`, version 0.1, complete text rather than an abstract |
| Intended permanent home | `series/watayuri/02 Sequential Readings/WATAYURI_V01_DEEP_READING.md` |
| Producer stage | Source retrieval/verification, direct Japanese manga reading, interpretation, proposed cumulative records, and handoff authoring |
| Receiver stage | Authorized semantic acceptance and targeted integration; no assumption that a receiving session has already accepted the assignment |
| Continuation | `single_operation`; no V02 analysis performed or authorized by the “next” route alone |
| Current-branch drift | Not assessed; this contribution deliberately uses the user-specified immutable base. The receiver must compare it with the actual current target before applying changes. |
| Publication | No commit, branch write, merge, Drive edit, or generated global-index change performed |
| Integrity | The source hash is in §2. The delivered file’s final byte count and SHA-256 are supplied with the download response; a file cannot contain its own ordinary whole-file hash without changing that hash. |

Preserve the six-chapter argument, the distinction between observation and interpretation, the original i156 freeze, the packaged-short boundary, exact locators, competing readings, and proposed IDs. Repair demonstrated errors by explicit errata or claim dispositions. Do not shorten the analysis merely to make integration easier, substitute a later retrospective account for an earlier knowledge state, or recreate existing ledgers wholesale from this packet.

### 16.2 Required targeted integration deltas

Paths below are relative to `series/watayuri/`. The listed blobs identify the pinned before-state, not a promise that a moving branch still has the same contents. The nine ledgers at this base have schemas and zero narrative evidence rows. The proposed entries above supply actual additions, not an instruction to invent rows after the fact.

| Target path | Required change on acceptance | Pinned blob / status |
| --- | --- | --- |
| `02 Sequential Readings/WATAYURI_V01_DEEP_READING.md` | Add the accepted reading under this artifact ID and intended home; authority promotion must be explicit. | New reading named by the pinned architecture; no prior narrative reading is identified by its entrypoint |
| `03 Longitudinal Ledgers/WATAYURI_RELATIONSHIP_AND_ATTACHMENT_LEDGER.md` | Add the six directional records in §5, preserving separate public/private and A→B/B→A states. | `a9653f0ddee0a16f6e179bb2a64b4d1d76f9165f` |
| `03 Longitudinal Ledgers/WATAYURI_PERSONA_ROLE_AND_PERFORMANCE_LEDGER.md` | Add PER01–PER06 from §6; keep actual audience, intended audience, and private effect separate. | `ff2bd9ff67fbe4cb335a8e9344a53e0593bfca78` |
| `03 Longitudinal Ledgers/WATAYURI_INFORMATION_DISCLOSURE_AND_MISREADING_LEDGER.md` | Add INF01–INF09 from §7 with the staged knowledge changes, not only the final answers. | `fd3b7a25b3359715d0ac4becbe4e3fe95557cc06` |
| `03 Longitudinal Ledgers/WATAYURI_AGENCY_BOUNDARY_RUPTURE_AND_REPAIR_LEDGER.md` | Add AG01–AG08 from §8; distinguish task repair, communication attempt, and unresolved relationship repair. | `baeccf8180b473a4afb18ec0fcc068c109d9d8cc` |
| `03 Longitudinal Ledgers/WATAYURI_CHRONOLOGY_MEMORY_AND_RETROSPECTION_LEDGER.md` | Add T01–T06 from §9; retain the memory perspective and open placement of the short. | `8bed3e6e9e4d24cabc268514fb61f496c90f64b0` |
| `03 Longitudinal Ledgers/WATAYURI_JAPANESE_SPEECH_ADDRESS_AND_REGISTER_LEDGER.md` | Add JP01–JP07 from §10, preserving exact context and exclusion of acoustic inference. | `f70a21a1b13daf812d38d62124027a91d6cc01e1` |
| `03 Longitudinal Ledgers/WATAYURI_VISUAL_FORM_STAGING_AND_GAZE_LEDGER.md` | Add VIS01–VIS07 from §11; do not convert montage adjacency into original spreads. | `1d00b0d5f68ec3050a1bdd37ae8bd54f8f3181bf` |
| `03 Longitudinal Ledgers/WATAYURI_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md` | Add C01–C14 and PR01–PR05 from §§12–13. No prior predictions exist; all new forecasts remain OPEN. | `0cb262595b3116e0faca7695b98645fc5cd45402` |
| `03 Longitudinal Ledgers/WATAYURI_CAST_AND_RECONSTRUCTION_READINESS.md` | Add the five source-identified cast records and separate gate decisions from §14. Update last-closed only when closure is real. | `017a53800dd58a170c622917432a7843ed5a608c` |
| `00 Frameworks and Methods/WATAYURI_SOURCE_AND_SCOPE_MAP.md` | Append the dated retrieved-byte match, structural result, exact component/image map, SQ01, admission boundaries, and actual inspection receipt. Do not promote V02–V14 or unrelated supplements. | `1542918e370c15b36e6dd436a8ebe43fc06d8b98` |
| `CURRENT_STATE_AND_CORPUS_MAP.md` | Link the accepted reading and updated homes; replace the zero-narrative state only after the full transaction is accepted and synchronized. Record the V01 endpoint, separate supplement coverage, remaining open questions, and informational V02 route. | `b73928f10739e6ce562c152758fb9ff7180ff4ea` |

**Scope:** twelve named analytical/state targets in total, comprising the new reading, nine existing cumulative homes, the source map, and the entrypoint. Existing methods and the synthesis architecture do not require a substantive rewrite for this reading. The navigation typo is a source-receipt note, not a reason to alter the primary EPUB.

The source object is already routed by the pinned source map. Reusing it is not a new private-media publication. Any genuinely new Drive-reference or other semantic obligation identified during integration must follow the then-current obligation map. Do not add raw manga images, extracted source text dumps, the EPUB, temporary montages, or this session’s source cache to Git.

### 16.3 Acceptance and remaining mandatory work

The receiver must obtain the complete current target files, check source/authority eligibility, and assess drift against this pinned base before making targeted changes. If another session has already added V01 or advanced a ledger, reconcile the contributions rather than replacing its work with the zero-row assumptions of this base. Source-check high-impact claims and representative locators, especially the public refusal/pact, practical assistance, childhood memory, final trust dialogue, and identity disclosure. A full automatic reread is not required merely because authorship changes; a substantive discrepancy does require the relevant source to be reopened.

After semantic acceptance, apply the synchronized local updates and the correct authority state, then run the applicable repository preflight, integration audit, and exact-result readback. Continuing series work routes through the authorized `series/watayuri` workflow, but this packet neither verifies an existing live branch nor creates one. Branch publication and merge to `main` are separate outcomes and must each be recorded truthfully.

Global character discovery and generated routing outputs remain with their designated owners. No global character enrollment, capability grade, unrelated catalogue churn, or historical tracked-path-list regeneration is requested by this file. Ordinary addition inside this existing registered root is not by itself a reason to rewrite global inventories.

**Mandatory before a repository CLOSED claim:** acceptance; current-base reconciliation; source receipt adoption; the nine cumulative updates; entrypoint synchronization; applicable validation; and an actual recoverable commit/publication result under the governing workflow. **Not a V01 closure prerequisite:** resolving future story questions, creating a mature monograph, reading V02, or obtaining anime audiovisual evidence.

### 16.4 Governing inputs and stable retrieval routes

All repository references in this subsection are to the supplied commit, not a moving default branch.

| Input | Pinned identity / responsibility |
| --- | --- |
| [Watayuri source and scope map](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/bc596633e8fc53e50f14892ad29f77017f166a05/series/watayuri/00%20Frameworks%20and%20Methods/WATAYURI_SOURCE_AND_SCOPE_MAP.md) | Exact witness routing and source-stage distinctions; blob recorded above |
| [Watayuri analytical method](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/bc596633e8fc53e50f14892ad29f77017f166a05/series/watayuri/00%20Frameworks%20and%20Methods/WATAYURI_ANALYTICAL_METHOD.md) | Prospective reading and evidentiary discipline; blob `aa9d5f772dbeacb670bb50091336ab9816e3843c` |
| [Watayuri synthesis architecture](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/bc596633e8fc53e50f14892ad29f77017f166a05/series/watayuri/00%20Frameworks%20and%20Methods/WATAYURI_SYNTHESIS_ARCHITECTURE.md) | Nine cumulative responsibilities and atomic closeout; blob `0f206f99eaf56fbeb8190789508bebb76f75ad3f` |
| [Watayuri reconstruction specification](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/bc596633e8fc53e50f14892ad29f77017f166a05/series/watayuri/00%20Frameworks%20and%20Methods/WATAYURI_CHARACTER_RECONSTRUCTION_SPEC.md) | Separate evidence/model/monograph/portability gates; blob `a73f06cc8be4ae07a7f3dfc2f14a7f9feba6ba77` |
| [Current state and corpus map](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/bc596633e8fc53e50f14892ad29f77017f166a05/series/watayuri/CURRENT_STATE_AND_CORPUS_MAP.md) | Open initiation lock and empty narrative entering state |
| Exact Japanese V01 witness, Drive ID `14sEQcf_V-iYCgyxgXcLYN5jCZXLE2Hlc` | Primary literary evidence; access-controlled source remains on the evidence plane |

Global authority, initiation, continuation, reasoning/topology, handoff, publication, and discovery distinctions were taken from the pinned repository’s `AGENTS.md`, authority records, corresponding source policies, pre-commit guidance, branch lifecycle policy, and `characters/README.md`. These govern the work; they are not evidence about fictional people. Before actual publication, the receiver must use the full live governing contract rather than treating this summary as its replacement.

### 16.5 Producer receipt and next operation

**Source processing and inspection:** complete for the declared V01 mainline and separately described packaged material. The source byte match, structural checks, and actual visual-reading route are recorded above. **Authoring:** complete for this delivered version. **Local artifact checks:** UTF-8/YAML and internal-reference/locator checks; these are not repository CI or independent semantic review. **Repository checks:** NOT RUN. **Receiver acceptance:** PENDING. **Published commit:** none. **Repository high-water advancement by this session:** none.

The next required operation is **accept and integrate this V01 transaction**. After that closure is verified, the next sequential source operation is **V02 source verification and a single-volume transaction**, subject to authorization. V02 is an informational route only; no later source has been consumed to make V01 appear more certain than it is.

---

**End of the V01 prospective reading. Mainline freeze: Shift 06, i156. Supplementary coverage: Shift 6.5, i158–161, separately bounded.**
