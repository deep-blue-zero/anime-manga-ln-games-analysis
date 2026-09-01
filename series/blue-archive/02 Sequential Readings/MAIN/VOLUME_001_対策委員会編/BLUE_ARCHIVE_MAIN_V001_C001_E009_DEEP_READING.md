---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E009
generation: V1
status: active_provisional
source_boundary: Canonical Japanese main-story unit BA:main:001:001:009, 対策委員会編 第9話『恩知らずの血戦』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-16
---

# BLUE ARCHIVE — MAIN V001 C001 E009 DEEP READING
## 対策委員会編 — 第9話「恩知らずの血戦」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the eleventh canonical main-story object in analytical order and the ninth object in `対策委員会編`:

- story ID: `BA:main:001:001:009`;
- analytical scope: `MAIN_V001_C001_E009`;
- source title: `第9話;恩知らずの血戦`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第9話`;
- raw group IDs: `11090`, `11095`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- record count: **104**;
- promoted utterance count: **76**;
- normalized choice groups: **1**;
- canonical scene count: **2**;
- normalized person IDs: Aru, Ayane, Haruka, Hoshino, Kayoko, Mutsuki, Nonomi, Serika, Shiroko;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_009.md`;
- complete source-side convenience rendering: `09話_恩知らずの血戦.md`.

### Canonical scene structure

1. `BA:main:001:001:009:scene:001` — immediate continuation from Shibaseki Ramen through target recognition, Aru's hesitation, mobilization of hired mercenaries, Abydos detection of the approaching force, face-to-face confrontation, and the order to attack. Primary text-bearing span: `ScenarioScriptMain1ExcelTable.json:DataList[1571]–[1644]`, with gaps for control/choice records.
2. `BA:main:001:001:009:scene:002` — the hired mercenaries end work at the paid time boundary, forcing Problem Solver 68 to retreat; Abydos begins shifting from immediate defense toward investigation of Aru and the organization. Primary text-bearing span: `DataList[1646]–[1672]`.

### Choice-space

There is one normalized Sensei choice group:

- `BA:main:001:001:009:scene:001:choice:001` — `出動だー！` — raw `DataList[1623]`.

It is a singleton and follows Ayane's explicit request `先生、出動命令を！`. It therefore does not represent route branching. Its structural importance lies in **domain-specific delegated command**: E008 showed that Sensei's opinion in ordinary committee deliberation can be vetoed by Ayane, while E009 shows Ayane explicitly asking Sensei to issue a sortie order during an armed emergency.

### Source-integrity cautions

E009's principal Aru/Mutsuki/Kayoko/Haruka conflict sequence is substantially usable, but the promoted source retains several local attribution irregularities that must not be silently repaired:

1. `scene:001:u:0003` / `DataList[1573]` is mapped to Nonomi: `あなたたちも学校の復興、頑張ってね！私も応援してるから！`. In immediate context this is semantically unstable because Nonomi herself belongs to the school being revived. The line is excluded from fine-grained Nonomi voice inference.
2. `scene:001:u:0052` / `DataList[1638]` is mapped to Aru: `はあ……社長。ここでそういう風に言っちゃうと、余計薄っぺらさが際立つ……。` The self-address `社長` is internally implausible and is excluded from Aru voice inference.
3. `scene:001:u:0032` / `DataList[1613]` is mapped to Mutsuki as `アル様！わっ、私、頑張りますから！`, immediately before Haruka's `ひとり残らず、ぶっ潰しちゃいますっ！`. This could be a deliberate playful imitation or a segmentation/mapping irregularity. No material Mutsuki or Haruka claim depends on resolving it.
4. The day-labor mercenaries in scene 2 are role-labeled but not promoted to stable person identities. Their lines are usable as **labor-structure evidence**, not as individual character baselines.

The episode's major relational and institutional claims are independently supported by cleanly mapped lines.

### Local-information lock

Available prior analytical authority is limited to:

- the canonical two-unit Prologue and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md` through `E008_DEEP_READING.md`;
- the seven longitudinal ledgers through E008.

No E010 or later main-story unit, bond story, MomoTalk, event, character package, relationship bundle, adaptation, wiki, or franchise hindsight is used to settle Problem Solver 68's later loyalties, the hidden sponsor's identity or goal, Aru's mature ethics, or the ultimate meaning of the Abydos conflict.

---

# 1. Story placement and local chronology

E008 ended by arranging a deliberate dramatic irony. The Countermeasures Committee and Problem Solver 68 had eaten in the same local restaurant. Abydos treated the four newcomers as hungry students and helped them preserve dignity despite their poverty. Kayoko and Mutsuki recognized the Abydos uniforms; Aru apparently did not. Mutsuki chose not to tell Aru because she found the uncertainty entertaining.

E009 converts that irony into moral conflict almost immediately.

The unit's movement is:

> **hospitality remembered → target identity made explicit → Aru's conscience resists → corporate role is invoked to suppress hesitation → hired labor mobilizes → Abydos detects an expensive mercenary formation → reciprocal recognition at the battle line → gift-obligation and contract-obligation collide → violence begins → wage/time limits dissolve the hired formation → Problem Solver 68 retreats → Abydos moves from defense toward investigation**

This progression matters because E009 refuses an easy moral simplification in either direction.

Problem Solver 68 is not innocent through ignorance. Once Aru learns who Abydos is, she understands that she is about to attack people she has just called `いい人たち`. Mutsuki explicitly frames Aru as `心優しい`. The moral fact is therefore present inside the organization.

But neither does the episode depict the organization as a homogeneous bloc of remorseless mercenaries. Aru hesitates; Mutsuki compartmentalizes; Kayoko observes and keeps the operation moving; Haruka volunteers immediate violent action; the hired day laborers care about wages and hours rather than the grandiose identity of Problem Solver 68.

The political-economic structure from E007–E008 therefore gains a psychological layer. The contract chain does not merely distribute violence. It distributes **knowledge, incentives, emotional investment, role identities, and exit conditions**.

---

# 2. Narrative reconstruction

The episode begins as the two groups separate after the meal. Serika tells the visitors to be careful. Nonomi wishes them success at work. Aru says goodbye and, once away from the Abydos group, exhales and says:

> `ふう……いい人たちだったわね。`

Kayoko and Mutsuki fall silent. Kayoko asks whether Aru noticed the other girls' uniforms. Aru does not understand the question. Mutsuki answers directly: they were Abydos.

Aru's reaction is explosive. She had not recognized them. Haruka immediately translates the revelation into mission terms: if those students are the target, should she go `始末` them now? Mutsuki tells her there is no need because the scheduled attack will begin shortly.

Aru's reaction is the opposite. She says she cannot believe that those girls are Abydos and calls it a cruel trick of fate. Mutsuki reminds her that they have work to do; Kayoko reminds her that the hired personnel are waiting for an order. Aru then asks, almost to herself, whether she is really about to attack those girls.

Mutsuki laughs and identifies the contradiction:

> `心優しいアルちゃんに、この状況はちょっとキツいねー。`

She then invokes the group's claimed motto:

> `「情け無用」「お金さえもらえればなんでもやります」がうちのモットーでしょ？`

Aru agrees weakly. Kayoko internally observes that Aru is completely shaken.

Aru resolves the conflict not by re-evaluating the contract but by invoking office:

> `こ、このままじゃダメよ、アル！一企業の長として、このままじゃ！`

She orders the hired personnel gathered.

The subcontractors immediately expose the gap between Problem Solver 68's theatrical corporate language and the labor market beneath it. One complains that the group was late. Another says overtime is off the table because the hourly wage has already been negotiated down. Aru dismisses the complaint and orders the assault on Abydos.

Ayane detects a large force roughly fifteen kilometers south of the school. Shiroko first suspects the Helmet Gang, but Ayane says it is not them; the approaching formation is composed of mercenaries, probably day laborers. Hoshino remarks that mercenaries should be expensive. Ayane concludes that allowing further approach is dangerous and asks Sensei:

> `先生、出動命令を！`

Sensei's sole authored response is:

> `出動だー！`

The committee intercepts the formation. Nonomi recognizes the ramen-shop students. Aru can only groan. Serika immediately names the moral issue:

> `ラーメンも無料で特盛にしてあげたのに、この恩知らず！！`

Mutsuki does not deny the gift or deny gratitude. Instead she answers:

> `その件はありがと。それはそれ、これはこれ。こっちも仕事でさ。`

and then makes her principle explicit:

> `公私はハッキリ区別しないと。受けた仕事はきっちりこなす。`

The two sides are therefore not disputing what happened at the restaurant. They disagree about **what normative weight that hospitality should carry once a prior contractual obligation comes due**.

Shiroko realizes that their `仕事` is the `便利屋` business. Nonomi criticizes the occupation as inappropriate work for students. Aru responds defensively that it is not a mere `アルバイト` but a legitimate `ビジネス`, and insists on the title `社長`. The group's layered titles are recited, though one following source line contains an impossible speaker mapping and is quarantined.

Shiroko asks who is behind them, immediately assumes they will not answer, and prepares to force the issue. Aru responds that the answer is `企業秘密` and orders the attack.

The second canonical scene resolves the battle through labor structure rather than decisive battlefield victory. A school bell rings. A mercenary notes that it is the scheduled end time. Another says today's daily pay only covers work up to that point and tells everyone to go home. Other contractors discuss getting food on the way back.

Aru tries to stop them, but the paid formation dissolves.

Mutsuki recognizes that the fight has lasted unexpectedly long and asks whether they should run. Aru delivers a theatrical threat that Mutsuki immediately calls the line of a `三流悪役`. Aru angrily corrects `逃げる` into `退却` and orders withdrawal.

Abydos confirms the enemy's `退勤……いえ、退却`. Ayane does not yet understand why this strange organization is targeting them. Hoshino proposes starting with the identity of `社長のアルって子`. The group returns, and the next-title marker is:

> `次回;手がかりを探して`

---

# 3. Central thesis

The strongest E009 thesis is:

> **E009 transforms the proxy-contract architecture from an abstract political economy into a conflict among competing obligations. Problem Solver 68 knowingly proceeds against students whose kindness it has just accepted: Aru's conscience registers the contradiction but she subordinates it to her self-conception as `一企業の長`; Mutsuki explicitly compartmentalizes private gratitude from professional duty through `それはそれ、これはこれ` and `公私`; Haruka translates target identity directly into loyal violence; Kayoko keeps the operational machinery legible without supplying a moral resolution. Meanwhile, the subcontracted mercenaries obey a narrower wage contract and simply leave when paid time expires. The episode therefore shows that fragmented contracts distribute agency and responsibility rather than erasing them.**

A second thesis concerns the language of debt and obligation developed across E005–E009.

E005 made Serika's wages into school interest payments. E007 had Serika describe Sensei's rescue as a `借り` that she must repay. E008 contrasted predatory economic extraction with dignity-preserving hospitality. E009 now adds `恩`.

Serika's accusation `恩知らず` is not merely “you are mean after we fed you.” It invokes a relational accounting system in which a received kindness should alter later conduct. Mutsuki's reply is striking precisely because she **does acknowledge the kindness**. Her answer is not denial but compartmentalization:

> gratitude is true; the contract is also true; the two belong to different domains.

The episode therefore juxtaposes at least four obligation systems:

1. **financial debt** — Abydos's formal monetary liability;
2. **reciprocal personal debt** — Serika's `借り` to Sensei;
3. **social/moral favor** — Shibaseki/Abydos hospitality, framed by Serika as `恩`;
4. **commercial labor contract** — Problem Solver 68's paid mission and the subcontractors' time-bounded wage agreements.

The central question is no longer whether characters have obligations. Everyone does. The question is **which obligation gets priority when obligations conflict**.

A third thesis concerns legitimate authority. E008 and E009 form a useful paired test:

- in ordinary debt-policy deliberation, Sensei's choice is nonbinding and Ayane vetoes it;
- in an immediate armed threat, Ayane explicitly requests `出動命令` from Sensei.

Sensei's authority is therefore becoming **contextual, functional, and locally delegated**, not globally sovereign.

---

# 4. Scene-by-scene close reading

## 4.1 `いい人たちだった`: moral recognition precedes target recognition

Stable evidence: `scene:001:u:0004-0010`, raw `DataList[1574]–[1582]`, excluding quarantined `u:0003`.

Aru's first private evaluation after leaving the restaurant is:

> `ふう……いい人たちだったわね。`

This line is crucial because it prevents the later hesitation from being reduced to fear of a strong opponent.

Before she knows that the students are the target, Aru has already made a positive moral/social judgment. They were good people. The restaurant episode gave her direct evidence of generosity. E009 then reveals that this judgment is not shallow: when target identity becomes explicit, her emotional system treats the information as a problem.

The sequence is carefully ordered:

> **kindness recognized first → identity revealed second → contract becomes morally personalized third**.

If Aru had learned “those are Abydos” before saying `いい人たちだった`, her later response could be read primarily as tactical surprise. The actual order makes conscience much harder to dismiss.

## 4.2 Aru's shock is not ignorance of the mission; it is collision between mission and person

Stable evidence: `u:0011`, `u:0016`, `u:0019`, raw `DataList[1584]`, `[1590]`, `[1593]`.

Aru already knew the target was Abydos in the abstract. E008 had established that Problem Solver 68 was spending resources on an Abydos assault mission.

What she did **not** know was that “Abydos” referred to these particular students she had just met.

That distinction matters.

Her line:

> `本当に……？私、今から……あの子たちを……。`

is a transition from institutional abstraction to interpersonal concreteness. `あの子たち` is not a school name, contract target, or strategic object. It points back to the people in the restaurant.

E009 therefore demonstrates a recurring ethical problem of mediated coercion: distance makes targets abstract; contact restores personhood; role systems then have to decide what to do with that restored personhood.

## 4.3 `心優しいアルちゃん`: Mutsuki explicitly identifies the trait Aru is trying to suppress

Stable evidence: `u:0020`, raw `DataList[1594]`.

Mutsuki says:

> `心優しいアルちゃんに、この状況はちょっとキツいねー。`

This is unusually valuable because it is not merely an external analyst inferring kindness from Aru's hesitation. A close associate names it.

At this boundary, `心優しい` should still be read narrowly. It does not establish that Aru is universally benevolent or unwilling to use violence. She orders the assault moments later.

What it does establish is a contradiction inside her current character architecture:

- she wants to be the head of an organization that advertises ruthlessness;
- her actual affective response to personally encountered kindness is softer than that brand identity;
- she experiences the mismatch as a threat to her executive self-presentation.

The interesting trait is therefore not simply “kind.” It is **kindness in conflict with aspirational outlaw/corporate performance**.

## 4.4 `一企業の長として`: role identity becomes a technology for overriding hesitation

Stable evidence: `u:0024-0025`, raw `DataList[1598]`, `[1600]`.

Aru does not resolve her hesitation by concluding that attacking Abydos is morally right. She does not revisit the sponsor's reason, discover a necessity, or deny that Abydos treated her well.

Instead she tells herself:

> `こ、このままじゃダメよ、アル！一企業の長として、このままじゃ！`

This is self-command through office.

The phrase `一企業の長として` turns the problem from “what should I do to these people?” into “what must someone in my role do?” Role identity supplies distance from personal feeling.

This is not inherently corrupt—professional roles often require actors to set aside personal preference—but here the substantive act is a paid assault against people Aru herself regards as good. E009 therefore uses the corporate persona to expose a genuine ethical danger: **role-duty can become a mechanism for avoiding first-person moral judgment**.

Aru remains responsible because the source shows the hesitation, the alternative affect, and then the choice to proceed.

## 4.5 `情け無用` and organizational motto as performed hardness

Stable evidence: `u:0021-0022`, raw `DataList[1595]–[1596]`.

Mutsuki cites:

> `「情け無用」「お金さえもらえればなんでもやります」がうちのモットーでしょ？`

E008 had already shown that some Problem Solver 68 “company principles” are improvised in the moment. E009 therefore gives us a useful ambiguity: this motto matters behaviorally, but the text has not yet established it as a deep, stable institutional creed.

More importantly, Aru's weak `そ、そうだけど……` demonstrates that the slogan does not eliminate conscience.

The organization can **say** that money overrides mercy while its leader visibly struggles when a concrete case makes the slogan costly.

That makes Problem Solver 68's hardness partly theatrical—but not harmlessly so. The theatrical identity is strong enough to help produce actual violence.

## 4.6 Haruka: loyalty collapses moral distance in the opposite direction

Stable evidence: `u:0014-0015`, raw `DataList[1588]–[1589]`, and clean Haruka `u:0033` at `[1615]`.

Haruka reacts to the revelation by asking:

> `わ、私が始末してきましょうかっ！？`

This differs sharply from Aru.

Where Aru personalizes the target and hesitates, Haruka immediately translates target identity into a service opportunity. Her first concern is whether she can perform violence for the organization now.

Combined with E008's extreme self-abasement and deference, the current bounded model becomes:

> **low self-worth + strong upward loyalty + eagerness to make herself useful can make violent service feel like a route to value.**

That is still an inference, not a mature psychological diagnosis. The source does not yet explain why Haruka is like this. But the pattern is now materially stronger than a single poverty scene.

## 4.7 Kayoko: operational realism without explicit moral adjudication

Stable evidence: `u:0008`, `u:0013`, `u:0018`, `u:0023`, `u:0031`.

Kayoko tells Aru the uniforms mattered, confirms that Aru truly failed to notice, reminds her that the hired personnel are waiting for orders, internally recognizes that Aru is shaken, and later sighs as the operation proceeds.

E009 preserves the role emerging in E008: Kayoko makes constraints visible.

But it is important not to convert that realism into moral opposition without evidence. She does not tell Aru to cancel the contract. She does not endorse the assault in an ideological speech either.

Her present function is closer to **organizational reality principle**: she sees what is happening and keeps the decision environment legible.

This makes her silence ethically interesting but still OPEN.

## 4.8 Mutsuki: `それはそれ、これはこれ` is not ignorance but deliberate compartmentalization

Stable evidence: `u:0044-0045`, raw `DataList[1629]–[1630]`.

Serika's accusation gives Mutsuki every opportunity to deny the meal mattered. She does the opposite:

> `その件はありがと。`

Then:

> `それはそれ、これはこれ。こっちも仕事でさ。`

and:

> `公私はハッキリ区別しないと。受けた仕事はきっちりこなす。`

This is one of the clearest ethical propositions yet spoken by a student antagonist.

Mutsuki's position is internally coherent:

- private kindness deserves gratitude;
- professional obligation remains binding;
- the two should not contaminate one another;
- accepting a job creates a duty to complete it.

The problem is not inconsistency. The problem is the **substantive object of the job**.

Professionalism is being used to justify attacking benefactors who are also students defending their school. The episode therefore distinguishes procedural professionalism from moral legitimacy.

A person can be reliable about a wrongful or questionable task.

## 4.9 `恩知らず`: Serika proposes a rival moral accounting system

Stable evidence: `u:0043`, raw `DataList[1628]`.

Serika calls them:

> `この恩知らず！！`

`恩知らず` carries more than simple annoyance. It labels someone who fails to properly recognize a favor/kindness received.

This becomes especially rich after E007's `借り` language. Serika herself responded to Sensei's help by saying she would repay the `借り`. E009 shows the same reciprocity ethic applied outward: if someone receives generosity, that fact should change what they owe relationally.

Mutsuki's answer reveals the precise disagreement.

Serika's model:

> **favor received → relational obligation → later conduct should reflect the relationship**

Mutsuki's model:

> **favor received → gratitude acknowledged, but professional contract remains independently binding**

The episode does not present a formal philosophical debate, but its comedy is built around one.

## 4.10 The title's “ingratitude” is complicated by explicit gratitude

The title `恩知らずの血戦` is therefore deliberately sharper than “battle against rude people.”

Mutsuki literally says thank you. Aru has already called Abydos good people. Problem Solver 68 is not unaware of the kindness.

The “ingratitude” lies in **conduct that refuses to let recognized kindness modify professional behavior**.

That distinction matters because it turns the title into a question about whether gratitude is merely an emotion/verbal acknowledgment or whether genuine gratitude imposes action-guiding duties.

E009's answer is not abstractly declared, but Serika clearly treats the latter as true.

## 4.11 The subcontractors expose violence as wage labor

Stable evidence: `u:0026-0029`, raw `DataList[1606]–[1609]`; scene 2 `u:0002-0007`, raw `DataList[1647]–[1656]`.

The hired mercenaries are not written as fanatically loyal extensions of Aru's will.

Before deployment, one says:

> `残業はナシでね。時給も値切られてるし。`

This single line establishes several structural facts:

- their relation to Problem Solver 68 is wage-based;
- compensation is hourly enough for `時給` to matter;
- terms have been negotiated downward;
- overtime is explicitly outside the accepted bargain.

The second scene pays this off with almost bureaucratic precision. A bell rings. One mercenary says `定時だ`. Another says:

> `今日の日当だとここまでね。あとは自分たちで何とかして。`

and the formation simply leaves.

The comic mechanism is strong, but the institutional implication is real: **contracted violence remains labor governed by labor incentives**.

The hidden sponsor cannot simply will violence into existence. The sponsor pays a contractor; the contractor pays more workers; those workers retain their own economic boundaries. The farther one moves down the chain, the thinner the strategic identification becomes.

This materially strengthens and revises `BA-C012`.

## 4.12 The contract chain distributes responsibility instead of eliminating it

E007–E009 now expose at least three layers:

> **hidden sponsor → Problem Solver 68 → hired day-labor mercenaries**

Each layer appears to possess a different relationship to the operation:

- the hidden sponsor knows the larger strategic reason for pressuring Abydos, though that reason remains unrevealed;
- Problem Solver 68 knows it has accepted an Abydos assault job and expects payment, but the source has not shown that it understands the sponsor's full strategic purpose;
- the subcontracted mercenaries appear primarily concerned with the immediate paid task, wage rate, hours, and leaving when the paid term ends.

This produces **asymmetric information without zero agency**.

Aru cannot excuse the attack merely because she lacks the sponsor's motive: she knows enough to understand that she is directing an armed assault on a school and, by E009, on students she personally regards as kind.

The day laborers may know even less, but they still choose to participate within their contracted terms.

The sponsor's use of intermediaries therefore does not erase downstream responsibility. It **fragments** responsibility while also making the upstream actor harder to identify and challenge.

## 4.13 Ayane's `出動命令`: ordinary veto and emergency delegation coexist

Stable evidence: `u:0034-0040`, raw `DataList[1617]–[1625]`, plus `choice:001` at `[1623]`.

E008 gave unusually clear counterevidence to sovereign readings of Sensei: Ayane could reject all available Sensei proposals in a regular policy meeting.

E009 gives the complementary case.

Ayane detects the formation, classifies it as a mercenary force, judges further approach dangerous, and says:

> `先生、出動命令を！`

The sequence is important:

1. Ayane's local system detects the threat;
2. Ayane interprets it;
3. Ayane determines that intervention is required;
4. she calls on Sensei to issue the operational command.

Sensei's command role is therefore not evidence that Abydos lacks judgment. The student institution **activates** the adult's command function when the situation enters the domain where that function has proven useful.

This strengthens the current model of Sensei authority as **context-sensitive and functionally delegated**.

In ordinary governance, Sensei can be overruled. In battle, the committee can deliberately center Sensei's tactical command.

Those are not contradictory states.

## 4.14 `日雇いの傭兵`: Ayane reads the enemy economically, not only tactically

Ayane does not merely announce “many enemies.” She identifies them as:

> `……傭兵です！おそらく日雇いの傭兵！`

Hoshino immediately responds that mercenaries should be expensive.

The Countermeasures Committee is beginning to interpret violence through cost structure.

This continues the E007 supply-chain turn. The question is no longer only “who is attacking?” but also:

- who can afford this force?
- why are hired units appearing?
- what does the expenditure imply about the actor behind the visible attackers?

Abydos's economic weakness paradoxically makes its members highly sensitive to the economics of hostile force.

## 4.15 Recognition at the battle line destroys plausible social anonymity

Nonomi's:

> `あれ……ラーメン屋さんの……？`

and Serika's immediate accusation ensure that neither side can maintain the restaurant interaction as irrelevant anonymous contact.

E008 humanized the enemy before the battle. E009 makes both groups remember that humanization **during** the conflict.

Aru's `ぐ、ぐぐっ……` is especially useful because she has already had the private moral crisis. The public confrontation reactivates it.

This does not stop the attack. But it prevents the narrative from allowing violence to proceed behind total depersonalization.

## 4.16 Nonomi's criticism attacks the occupation, not only the attack

Stable evidence: `u:0047-0051`, raw `DataList[1633]–[1637]`.

Nonomi says:

> `学生なら、他にもっと健全なアルバイトがあるでしょう？それなのに便利屋だなんて！`

Her framing is revealing.

She does not first describe Aru's group as monsters or criminals. She treats them as students doing an unhealthy kind of work.

Aru reacts intensely to the word `アルバイト`:

> `アルバイトじゃないわ！れっきとしたビジネスなの！`

and then asserts:

> `私は社長！`

This exposes how central organizational recognition is to Aru's self-concept.

The insult is not just “your work is wrong.” It is “your company is not really a company.”

Aru's self-image therefore depends on **institutional seriousness** even when the institution itself is improvised, cash-poor, and ethically unstable.

## 4.17 Titles perform hierarchy, but do not guarantee institutional depth

Problem Solver 68's language of `社長`, `室長`, and `課長` gives the organization a corporate hierarchy.

But E008–E009 repeatedly undercut the solidity of that hierarchy:

- mottos can be invented in real time;
- Aru's target knowledge is incomplete;
- subcontractors can leave when their paid hours end;
- the organization's entire operation is financially fragile;
- close associates openly tease the president;
- the source's own following line about `社長` is attribution-corrupted and cannot be assigned, but its scene function clearly mocks the thinness of the corporate performance.

The current best model is not “fake company” versus “real company.” Problem Solver 68 **does** organize paid work, hire personnel, accept contracts, assign titles, and attempt missions.

Its institutional reality is real but **performative, adolescent, and unstable**.

## 4.18 `企業秘密`: confidentiality protects the upper layer of the proxy chain

Stable evidence: `u:0053-0056`, raw `DataList[1641]–[1644]`.

Shiroko asks:

> `誰の差し金？`

and immediately assumes the answer will not be volunteered.

Aru replies:

> `それはもちろん企業秘密よ？`

At minimum, this establishes that Problem Solver 68 treats the identity/source of the commission as protected business information.

It does **not** establish how much Aru knows about the client's ultimate purpose. The source still supports only a narrower conclusion:

> Problem Solver 68 has enough contractual knowledge to understand that a client relationship exists and enough organizational norm to refuse disclosure.

This confidentiality function is politically important. Intermediation does not only supply force. It creates **opacity** between target and sponsor.

## 4.19 The battle ends because the labor contract ends

Stable evidence: scene 2 `u:0001-0007`, raw `DataList[1646]–[1656]`.

The school bell is one of the episode's strongest comic-symbolic devices.

The battle does not end because:

- Aru has a moral revelation;
- Abydos decisively annihilates the attackers;
- the sponsor cancels the mission;
- Sensei forces surrender.

It ends because the workers' paid period ends.

The bell collapses three institutional rhythms into one sound:

- school time;
- work time;
- battle time.

The hired mercenaries hear it as the end of a shift. Their violence is neither sacred nor personal. It is labor, and labor stops when compensation stops.

This is an unusually clean illustration of **commodified violence without total militarization of identity**.

## 4.20 `退勤……いえ、退却`: even Ayane cannot keep labor and battle vocabularies separate

Ayane reports:

> `敵兵力の退勤……いえ、退却を確認。`

The correction is a joke, but analytically precise.

`退勤` means leaving work / clocking out. `退却` means retreat.

The scene has made both descriptions true.

The mercenaries are retreating **because they are clocking out**.

The slip therefore captures E009's institutional thesis in miniature: the battlefield is being structured by employment relations.

## 4.21 Aru's `逃げ……じゃなくて、退却`: self-image survives defeat through vocabulary

Stable evidence: scene 2 `u:0009-0013`, raw `DataList[1658]–[1662]`.

Mutsuki asks directly:

> `どうする？逃げる？`

Aru first performs a villainous threat:

> `こ、これで終わったと思わないことね！アビドス！！`

Mutsuki immediately calls it a `三流悪役のセリフ`.

Aru then says:

> `逃げ……じゃなくて、退却するわよ！`

This is the same character mechanism seen earlier in a smaller form.

Aru uses vocabulary to preserve role dignity:

- not part-time work, `ビジネス`;
- not just Aru, `社長`;
- not running away, `退却`.

Her identity is maintained through **reclassification**.

The comedy works because the audience can see the gap between material reality and prestigious terminology. But the need for that terminology is psychologically meaningful: Aru is actively constructing the person she wants to be.

## 4.22 Mutsuki enjoys puncturing the role while still serving the mission

Mutsuki's relation to Aru becomes more complex in E009.

She:

- forces target recognition;
- names Aru's kindness;
- invokes the ruthless company motto;
- pushes the operation forward;
- later offers the practical option of escape;
- mocks Aru's villain line;
- remains inside the group throughout.

She is not merely a subordinate and not simply an ethical critic.

Her current relational function is closer to **playful destabilizer who nonetheless helps the organization act**.

She punctures Aru's illusions without necessarily opposing the decisions those illusions support.

That combination is important for future relationship analysis.

## 4.23 The battle exposes Aru's authority as resource-dependent

Aru can order the mercenaries to attack, but she cannot make them work unpaid overtime.

When the subcontractors leave, she protests:

> `帰っちゃダメ！！`

They leave anyway.

This is a useful institutional limit.

Aru's title gives her authority inside Problem Solver 68, but authority over hired labor is contractual rather than personal. Once the bargain expires, the personnel no longer recognize her order as binding.

This mirrors, in a distorted way, the broader project interest in bounded authority:

> **titles do not create unlimited command; relationships and institutional terms determine the actual scope of obedience.**

## 4.24 Abydos wins enough to investigate, not enough to understand

After Problem Solver 68 retreats, Ayane says:

> `一体何が起きているのでしょうか……。`

This is a good epistemic boundary marker.

The Countermeasures Committee now knows:

- a strange paid organization is targeting them;
- Aru is its president;
- the force included expensive day-labor mercenaries;
- the group refuses to identify whoever commissioned the work.

It still does not know the hidden sponsor or larger purpose.

Hoshino's response is methodical:

> `まずは社長のアルって子の身元から洗ってみたら。何か出てくるよ、きっと。`

The arc therefore shifts again:

> **forensic material investigation (E007) → social/organizational encounter (E008–E009) → intelligence investigation of an identified intermediary (E010 boundary)**.

The students are not merely surviving attacks. They are building a causal model of the attack network.

---

# 5. Character-state analysis

## 5.1 Aru — conscience versus aspirational executive identity

E009 materially strengthens the E008 baseline.

### Trait
Aru is emotionally softer than her corporate/outlaw persona permits her to comfortably admit.

### State
She is shocked and distressed when the abstract target `アビドス` becomes the specific students she has just experienced as kind.

### Strategy
She manages dissonance through role invocation: `一企業の長として`.

### Value / desired self
She wants to be a serious, commanding company president whose organization completes accepted work and cannot be dismissed as a mere part-time operation.

### Contradiction
She recognizes kindness and feels reluctance, yet orders the assault anyway.

### Institutional position
Her power over internal members is socially real, but her power over subcontractors ends where the wage bargain ends.

### Development delta
E008 showed performative mastery under uncertainty. E009 shows that the performance is also used **against her own conscience**.

This is a more consequential function than simple bluffing.

## 5.2 Mutsuki — compartmentalized professionalism plus playful destabilization

E009 is the clearest current statement of Mutsuki's ethics.

She articulates:

> `それはそれ、これはこれ`

and:

> `公私はハッキリ区別しないと。受けた仕事はきっちりこなす。`

Her current profile therefore includes:

- strong situational perception;
- attraction to uncertainty and entertainment;
- willingness to let Aru walk into a socially painful revelation;
- explicit compartmentalization of personal gratitude and professional duty;
- commitment to completing accepted work;
- readiness to puncture Aru's self-image even while supporting the mission.

This should not yet be flattened into “amoral.” She acknowledges gratitude, recognizes Aru's kindness, and appears socially perceptive. The more precise current term is **ethically compartmentalizing**.

## 5.3 Kayoko — realism, constraint recognition, and morally noncommittal operational support

Kayoko continues to see the situation earlier and more clearly than Aru.

She notices the uniform issue, recognizes Aru's distress, reminds her that hired personnel await orders, and later watches the operation deteriorate.

Her state is not enthusiastic. But the source does not show her trying to stop the assault.

Current bounded formulation:

> **Kayoko functions as Problem Solver 68's reality principle without yet functioning as its moral veto.**

That distinction should remain open for later evidence.

## 5.4 Haruka — violent usefulness as immediate answer to role demand

Haruka's `始末してきましょうか` and later `ひとり残らず、ぶっ潰しちゃいますっ！` place her deference into an operational register.

E008 established extreme self-negation around poverty. E009 shows the other side of that low-entitlement posture: she is extremely eager to make herself useful to Aru and the group, including through violence.

The safest current inference is:

> **Haruka's self-worth appears unusually contingent on useful service to the organization, and violent service is not excluded from that route to usefulness.**

The developmental cause remains completely open.

## 5.5 Serika — reciprocity ethic becomes outward moral judgment

Serika's `恩知らず` extends her E007 `借り` ethic.

She does not treat hospitality as morally neutral once given. A received favor creates a relational fact.

This suggests a coherent value pattern:

- she wants to repay help she receives;
- she expects recognized kindness to constrain later betrayal/harm;
- economic hardship does not negate reciprocal obligation.

Her indignation is therefore not only personal offense. It expresses an ethical model.

## 5.6 Ayane — operator, threat classifier, and delegator of tactical command

Ayane's state advances in two directions.

First, she detects and classifies a new kind of force: not Helmet Gang, but likely day-labor mercenaries.

Second, she explicitly calls on Sensei for the sortie order.

This strengthens her role as the committee member who converts information into institutional action while preserving clear division of function.

## 5.7 Hoshino — economic inference and investigative tempo

Hoshino immediately recognizes that a mercenary force implies significant cost. After the battle, she does not chase blindly. She proposes beginning with Aru's identity and investigating step by step.

Her current strategic style continues to combine relaxed presentation with strong tempo control:

- identify what matters;
- avoid overreacting to incomplete information;
- pursue the next tractable clue.

## 5.8 Shiroko — direct causal interrogation

Shiroko rapidly moves from recognizing the nature of Problem Solver 68's job to asking `誰の差し金？`.

This is the most direct articulation yet of the committee's hidden-principal hypothesis in interpersonal confrontation.

She also immediately assumes voluntary disclosure is unlikely and prepares coercive interrogation through force.

The source therefore keeps her action-forward pragmatism intact, while opening a future ethical question about how readily she treats violence as an information-gathering instrument.

---

# 6. Relationship-state analysis

## 6.1 Abydos ↔ Problem Solver 68 — hospitality becomes adversarial knowledge, not erased relationship

E008 created a low-stakes social encounter before hostility. E009 does not erase it when the battle begins.

Both sides remember.

That creates a relationship state different from anonymous enemies:

> **mutual social recognition + opposed institutional roles + unresolved sponsor structure**.

This matters because future changes in the conflict can now be relationally meaningful. They know one another as students as well as opponents.

## 6.2 Aru ↔ Abydos — positive personal judgment and active institutional aggression coexist

Aru's current relation to Abydos is internally split:

- personal: `いい人たち`;
- institutional: contracted target;
- emotional: reluctant;
- behavioral: orders the attack.

This is not hypocrisy in the simple sense of secretly feeling nothing. The contradiction is visible and painful.

The stronger formulation is **role-mediated moral dissonance**.

## 6.3 Mutsuki ↔ Abydos — gratitude explicitly subordinated to work

Mutsuki's relation is unusually explicit:

- she acknowledges the food favor;
- refuses to let it alter mission performance;
- frames the separation as correct professionalism.

This gives a clean relational state:

> **personal goodwill/acknowledgment does not currently supersede contractual hostility.**

## 6.4 Aru ↔ Mutsuki — intimate perception without protective cushioning

Mutsuki knows Aru well enough to call her kind and to recognize the situation will be hard for her.

Yet she does not shield Aru from the contradiction. She pushes her toward the job and later mocks her retreat performance.

Their closeness therefore includes **accurate reading + teasing pressure + continued cooperation**.

## 6.5 Aru ↔ Kayoko — leader and reality-check subordinate

Kayoko understands Aru's state and the operational constraints but does not seize command from her.

She reminds rather than dictates.

This preserves Aru's leadership while showing that leadership depends on members who see the situation more clearly than she sometimes does.

## 6.6 Aru ↔ Haruka — upward devotion and permission-seeking violence

Haruka's first response to target recognition is to ask whether she should eliminate them.

Her aggression is explicitly permission-oriented.

This strengthens the asymmetry of the relationship: Aru's position is not merely a comic title to Haruka. It appears to organize Haruka's willingness to act.

## 6.7 Sensei ↔ Abydos committee — delegated tactical authority after nonbinding civil participation

The E008–E009 pairing is now one of the strongest relationship-state findings in the arc.

Sensei is:

- included socially and institutionally;
- trusted enough to be asked for judgment;
- not obeyed automatically in ordinary policy;
- explicitly requested to command in crisis.

The relationship is becoming a **functional partnership with domain-specific authority**.

---

# 7. Institutional-state analysis

## 7.1 Problem Solver 68 is a real organization, but a fragile one

E009 confirms several real institutional properties:

- accepted external work;
- confidentiality norm (`企業秘密`);
- named hierarchy;
- president issuing orders;
- subcontracting capacity;
- ability to mobilize a large force;
- expectation of payment.

It also exposes fragility:

- resource exhaustion;
- negotiated-down subcontractor wages;
- no ability to compel overtime;
- incomplete target knowledge;
- leader role-performance under stress;
- hired force dissolves when paid time expires.

The correct model is therefore **institutionally real but operationally precarious**.

## 7.2 Abydos's command system becomes clearer

E009 shows:

- Ayane as detection/operator and threat classifier;
- Sensei as requested sortie commander;
- students as frontline actors;
- Hoshino as post-action investigative strategist.

This is another strong counterexample to an adult-replacement model.

The institution distributes roles.

## 7.3 Proxy war becomes labor market

`BA-C012` now needs a stronger formulation.

The coercive architecture is not only a sequence of organizations. It is a **market relation at several layers**:

- sponsor purchases Problem Solver 68's service;
- Problem Solver 68 purchases additional combat labor;
- combat labor prices its time and refuses unpaid extension.

This changes the interpretive emphasis from “mastermind controls minions” to **principal–contractor–subcontractor coordination under incomplete information and bounded contracts**.

## 7.4 Confidentiality and intermediation create sponsor protection

Abydos can now see and fight the contractor. It still cannot see the principal.

`企業秘密` functions as a social/institutional barrier to tracing the chain upward.

Combined with E007's illegal weapons and E008's subcontracting, the hidden sponsor's power increasingly appears to include not just resources but **organizational distance**.

---

# 8. Sensei role and choice-space

E009 contains only one Sensei choice:

> `出動だー！`

Its importance comes from context rather than semantic richness.

Ayane asks for an `出動命令`. The choice fulfills the requested role.

This should be read against E008:

| Context | Student institution's treatment of Sensei |
|---|---|
| regular debt-policy meeting | Sensei may choose among proposals, but Ayane rejects unacceptable outcomes |
| approaching armed mercenary formation | Ayane explicitly requests Sensei issue the sortie order |

The emerging rule is:

> **Sensei's authority expands when the student institution identifies a domain where Sensei's specialized function is useful; it contracts where student institutional judgment remains sufficient.**

This is stronger and more precise than either “Sensei is in charge” or “Sensei is just an advisor.”

Choice-space remains nonbranching. The player voices the commanded transition into battle rather than deciding whether the committee will respond to the threat.

---

# 9. Japanese-language and voice analysis

## 9.1 Aru: `一企業の長として`

This phrase is central to Aru's self-regulation.

`～として` means “as / in the capacity of.” Aru invokes not desire but office. She tells herself how someone occupying the category `企業の長` must act.

The line is evidence that role identity is psychologically active, not ornamental.

## 9.2 Mutsuki: `それはそれ、これはこれ`

This idiom cleanly separates two matters that another person might see as linked.

In E009:

- `それ` = the ramen/hospitality and gratitude;
- `これ` = the current job/assault.

The phrase allows Mutsuki to acknowledge the former while denying that it governs the latter.

## 9.3 Mutsuki: `公私`

`公私` literally distinguishes public/official and private/personal spheres.

Her line:

> `公私はハッキリ区別しないと。`

gives the assault a professional-ethics vocabulary.

The irony is that the “public” side here is not public service but a privately paid attack contract. Mutsuki is applying a conventional professionalism distinction to morally dubious work.

## 9.4 Serika: `恩知らず`

`恩` refers to kindness/favor/benefit received with relational moral weight; `恩知らず` condemns one who fails to recognize that moral relation appropriately.

The accusation fits Serika's established reciprocity ethic.

It is especially revealing because Mutsuki does not deny receiving the favor. The disagreement is about whether recognition must affect action.

## 9.5 Aru: `企業秘密`

The phrase means company/business secret.

Aru's use continues her insistence that Problem Solver 68 be treated as a serious enterprise. It also performs a real intermediary function by refusing the target direct access to the client relation.

## 9.6 Labor register: `残業`, `時給`, `定時`, `日当`, `退勤`

These words form a coherent lexical field:

- `残業` — overtime;
- `時給` — hourly wage;
- `定時` — scheduled end time;
- `日当` — daily pay;
- `退勤` — leaving/clocking out from work.

Placing this vocabulary inside an armed battle makes the episode's political economy explicit through comedy.

## 9.7 Aru: `逃げ` versus `退却`

Aru begins to say `逃げ`—run away—then replaces it with the more dignified tactical term `退却`—retreat.

This is a compact example of her linguistic self-fashioning. Naming changes the social meaning of the same material movement.

## 9.8 Mutsuki: `三流悪役`

Calling Aru's threat a `三流悪役のセリフ` marks the group's own awareness of villain-performance conventions.

The scene therefore refuses to treat Aru's grandiose rhetoric as transparent character truth. Her own friend hears it as genre performance.

---

# 10. Motifs, symbols, and callbacks

## 10.1 Debt / obligation expands from money to morality

The arc's obligation vocabulary now includes:

- financial principal/interest;
- wages and labor;
- `借り`;
- `恩`;
- paid contracts;
- confidentiality;
- work-hour obligations.

E009 is the first unit where these forms directly compete inside one battle.

## 10.2 Hospitality before hostility becomes remembered hospitality during hostility

E008's meal was not disposable comic relief.

E009 explicitly carries it into the confrontation through Aru's `いい人たち`, Serika's `恩知らず`, and Mutsuki's acknowledgment of thanks.

The callback changes the moral texture of the fight.

## 10.3 The school bell

The bell normally structures student life.

Here it also structures paid combat labor.

It symbolically reminds the scene that even the people conducting this armed conflict remain embedded in ordinary schedules rather than inhabiting a totally separate military world.

## 10.4 Corporate vocabulary as armor

Aru repeatedly protects identity through institutional language:

- `ビジネス`;
- `社長`;
- `企業秘密`;
- `一企業の長`;
- `退却`.

The vocabulary functions almost like psychological armor against embarrassment, doubt, and defeat.

## 10.5 Expensive violence, poor contractors

E008 showed Problem Solver 68 struggling to afford ramen after spending on the mission. E009 shows the hired mercenaries complaining their wage was negotiated down.

This creates a recurring paradox:

> the operation is expensive at the aggregate level while many people executing it are individually cash-constrained.

The hidden sponsor's resource power is therefore not evenly distributed down the chain.

---

# 11. Violence, ethics, and power

## 11.1 Personal kindness does not automatically defeat institutional violence

E009's strongest ethical point is that humanization is not sufficient by itself.

Aru knows Abydos is kind. She attacks anyway.

Mutsuki is grateful. She attacks anyway.

The episode therefore resists an optimistic assumption that personal contact automatically dissolves structural conflict.

Relationships matter, but institutional incentives and role identities can remain stronger.

## 11.2 Professionalism is morally incomplete

Mutsuki's `受けた仕事はきっちりこなす` is a recognizable virtue in ordinary contexts: reliability.

E009 exposes why reliability cannot be a complete ethical principle.

One must still ask what work has been accepted.

A perfectly reliable contractor can be reliably harmful.

## 11.3 Role obligation does not erase first-person responsibility

Aru's internal conflict is evidence against moral disappearance into office.

She cannot plausibly say “the company did it” in a way that removes her agency, because the text shows her personally deciding to use the company role to overcome her reluctance.

This is a useful bounded ethical inference:

> **institutional role mediates responsibility; it does not annihilate it.**

## 11.4 Wage labor limits command power

The subcontractors demonstrate another side of institutional power.

Aru can purchase labor, but she cannot purchase unlimited obedience for a limited wage.

Their refusal of overtime is structurally legitimate within their agreement even though the work itself is violent.

This again separates **internal contractual validity** from **external moral legitimacy**.

## 11.5 Sensei's command remains relationally authorized

Ayane's request for the sortie order is important because it prevents tactical leadership from being read as spontaneous adult seizure of control.

The committee detects and frames the emergency; Sensei performs the requested command role.

This is delegated coordination, not replacement governance.

---

# 12. Competing readings and counterevidence

## Reading A: “Aru is secretly good and therefore not responsible for the attack.”

**Rejected / too strong.**

Evidence for kindness is real: `いい人たち`, visible hesitation, Mutsuki's `心優しい`. But Aru consciously overcomes the hesitation and orders the assault.

The more defensible reading is that **moral sympathy and culpable action coexist**.

## Reading B: “Problem Solver 68 are simply ruthless mercenaries.”

**Too flat.**

Mutsuki does articulate ruthless professional compartmentalization, but Aru visibly struggles, Kayoko is restrained rather than bloodthirsty, Haruka's violence is tied to extreme deference/usefulness, and the group is economically precarious.

They remain accountable attackers without being psychologically uniform.

## Reading C: “The ramen kindness changes nothing.”

**Contradicted.**

It changes Aru's emotional state and structures Serika/Mutsuki's ethical dispute. It simply does not stop the contract.

## Reading D: “Mutsuki is ungrateful.”

**Lexically and morally incomplete.**

The title/Serika call her side `恩知らず`, but Mutsuki explicitly says `ありがと`. The sharper issue is whether **gratitude that does not constrain action** counts as adequate recognition of `恩`.

## Reading E: “Aru is being coerced by the sponsor and has no agency.”

**Unsupported.**

At this boundary there is no evidence of coercion forcing Problem Solver 68 to accept or continue the contract. Aru is economically motivated and role-committed, but she issues the attack order herself.

## Reading F: “The hired mercenaries prove nobody takes the battle seriously.”

**Too strong.**

Their labor comedy is real, but Abydos judges the approaching force dangerous and a large battle lasts until the paid shift ends. The scene makes violence ordinary/commodified, not unreal.

## Reading G: “Sensei is now commander of Abydos.”

**Contradicted by E008–E009 pairing.**

Sensei is asked to issue a combat sortie order, but ordinary governance remains student-run and student-vetoable. The better model is contextual delegated command.

---

# 13. Cumulative claim transitions

No new claim ID is required. E009 most strongly revises `BA-C012` and sharpens the domain-specific authority model already housed in `BA-C002`–`BA-C004`, `BA-C007`, and `BA-C010`.

| Claim ID | Transition at E009 | Current effect |
|---|---|---|
| BA-C001 | **PRESERVE / STRENGTHEN lightly** | responsible adulthood is not the main focus, but Sensei responds to an explicitly student-identified emergency rather than preempting student judgment |
| BA-C002 | **STRENGTHEN** | legitimacy becomes more clearly domain-specific: Ayane vetoes Sensei in E008 ordinary policy but explicitly requests Sensei's sortie command in E009 combat |
| BA-C003 | **STRENGTHEN** | Schale remains additive to an Abydos system that detects, classifies, fights, and investigates on its own institutional terms |
| BA-C004 | **STRENGTHEN** | Sensei's differentiated capacity is again specifically command/coordination when Ayane asks for `出動命令`; no personal combat supremacy appears |
| BA-C005 | **PRESERVE REJECTED** | the adult does not identify the new enemy, uncover the sponsor, or independently author the response; student systems and judgment remain indispensable |
| BA-C006 | **PRESERVE REJECTED; counterevidence strengthened** | Abydos detects a large force, classifies its labor structure, resists it, and begins systematic investigation of the intermediary network |
| BA-C007 | **STRENGTHEN / contextualize** | Schale service now includes performing requested crisis command while leaving post-battle investigation with the student institution |
| BA-C008 | **STRENGTHEN** | the sole choice is a singleton enactment of a requested sortie order, not meaningful route branching |
| BA-C009 | **PRESERVE** | no material technical-system ontology delta |
| BA-C010 | **STRENGTHEN** | authority is again shown as scoped by institutional relationship: requested in battle, nonbinding in ordinary deliberation |
| BA-C011 | **PRESERVE / STRENGTHEN lightly** | responsible adult usefulness coexists with student operational competence; no adult supremacy is needed to explain successful defense |
| BA-C012 | **STRENGTHEN / REVISE SHARPLY** | proxy coercion is now a nested labor market with morally active intermediaries: hidden sponsor → Problem Solver 68 → day-labor mercenaries. Strategic knowledge is asymmetric, but Aru knowingly chooses to proceed after personalizing the target; subcontractors retain wage/hour exit conditions. Responsibility is distributed rather than erased by the contract chain |

### Revised current formulation of BA-C012

> **Abydos is being pressured through a layered political economy of coercion in which an unresolved sponsor supplies or finances force through intermediaries; Problem Solver 68 accepts and operationalizes the Abydos assault while subcontracting additional combat labor, and lower layers possess progressively narrower strategic knowledge and their own contractual incentives. Intermediation creates opacity and distributed responsibility, not automatic moral exculpation.**

---

# 14. Open questions after E009

1. Who commissioned Problem Solver 68, and what is the sponsor's actual objective toward Abydos?
2. How much does Aru personally know about the client beyond the existence of the job and protected business relationship?
3. Will Aru's `心優しい` hesitation materially alter future behavior, or will executive self-performance continue to override it?
4. Is Mutsuki's `公私` compartmentalization a stable ethical principle, a playful rationalization, or both?
5. Why did Kayoko initially remain silent after recognizing the Abydos uniforms in E008, and what are her own moral limits on accepted work?
6. How far does Haruka's extreme usefulness-seeking extend, and what relationship history produces it?
7. Can Abydos trace the sponsor through Aru/Problem Solver 68 despite `企業秘密`?
8. Does the expensive use of hired mercenaries connect directly to the illegal weapons supply route identified in E007, or are these separate operational channels under the same hidden principal?
9. What formal or informal rules govern mercenary/day-labor combat employment in Kivotos?
10. Will the hospitality relationship later change the status of Problem Solver 68 from enemy to something more ambivalent?

---

# 15. Evidence locator index

All locators refer to the pinned `ScenarioScriptMain1ExcelTable.json` unless otherwise stated.

## Scene 1 — target recognition and attack

- `u:0001-0005` — `DataList[1571]–[1577]`: restaurant farewell; Aru `いい人たちだった`; `u:0003` attribution quarantined.
- `u:0008-0013` — `[1580]–[1587]`: Kayoko asks about uniforms; Mutsuki identifies Abydos; Aru shock.
- `u:0014-0015` — `[1588]–[1589]`: Haruka offers immediate `始末`; Mutsuki defers violence to scheduled attack.
- `u:0016-0023` — `[1590]–[1597]`: Aru moral conflict; Mutsuki `心優しい`; `情け無用` / money motto; Kayoko notes Aru is shaken.
- `u:0024-0025` — `[1598]`, `[1600]`: Aru invokes `一企業の長として` and orders mobilization.
- `u:0026-0029` — `[1606]–[1609]`: subcontractor wage/overtime complaint; Aru orders Abydos assault.
- `u:0032-0033` — `[1613]`, `[1615]`: suspicious Mutsuki mapping followed by clean Haruka `ぶっ潰しちゃいます`; do not overattribute `u:0032`.
- `u:0034-0039` — `[1617]–[1622]`: Ayane detects large force, identifies likely day-labor mercenaries; Hoshino notes cost; Ayane requests sortie order.
- `choice:001` — `[1623]`: Sensei `出動だー！`.
- `u:0040-0043` — `[1625]–[1628]`: formation identified; Nonomi recognizes restaurant group; Serika `恩知らず`.
- `u:0044-0045` — `[1629]–[1630]`: Mutsuki `ありがと` / `それはそれ、これはこれ` / `公私` / job-completion principle.
- `u:0046-0051` — `[1631]–[1637]`: Shiroko identifies 便利屋 work; Nonomi criticizes occupation; Aru insists `ビジネス` / `社長`; titles recited.
- `u:0052` — `[1638]`: impossible Aru self-address; quarantined.
- `u:0053-0056` — `[1641]–[1644]`: Shiroko asks `誰の差し金`; Aru `企業秘密`; attack begins.

## Scene 2 — contract expiration and retreat

- `u:0001-0007` — `DataList[1646]–[1656]`: bell; `定時`; daily pay ends; mercenaries clock out and ignore Aru's protest.
- `u:0009-0013` — `[1658]–[1662]`: Mutsuki asks whether to flee; Aru villain threat; `三流悪役`; `逃げ` corrected to `退却`.
- `u:0014-0016` — `[1665]–[1667]`: Problem Solver 68 escapes; Ayane's `退勤……いえ、退却`.
- `u:0017-0019` — `[1668]–[1670]`: Abydos uncertainty; Hoshino proposes investigating Aru's identity; return order.
- `u:0020` — `[1672]`: `次回;手がかりを探して`.

---

# 16. Conclusion and next boundary

E009 is the point where the arc's economic and ethical structures become inseparable.

The visible battle is comic, but the underlying model is sophisticated:

> **kindness creates one obligation; contracts create another; offices create role expectations; wages create time-limited obedience; confidentiality protects principals; personal conscience survives inside institutions but does not automatically control them.**

Problem Solver 68 is now neither an anonymous enemy nor a simple victim of a mastermind. Its members are morally differentiated intermediaries operating with incomplete strategic information but real operational agency.

Aru is the clearest case. She knows Abydos treated her well, feels the wrongness strongly enough to hesitate, and still chooses to proceed because her desired identity as company president tells her that completing the job is what a leader does.

Mutsuki offers the cleanest rival ethic: gratitude and work belong to different spheres. Her `公私` distinction converts reliability into a reason to continue violence.

The subcontracted mercenaries then expose the material limit of that entire performance: they are not bound by Aru's identity or the sponsor's strategic objective. They are bound by the wage bargain, and when the bargain ends, so does their battle.

At the same time, Abydos's institutional model grows clearer. Ayane can reject Sensei in ordinary deliberation and request Sensei's command in crisis. Hoshino can treat the battle not as an isolated encounter but as another clue in a larger causal network. Student agency and adult assistance continue to coexist without collapsing into a simple hierarchy.

The next mandatory sequential unit is:

**`BLUE_ARCHIVE_MAIN_V001_C001_E010_DEEP_READING.md`**\
`BA:main:001:001:010`\
**第10話「手がかりを探して」**

The next reading should test whether Abydos can turn Aru/Problem Solver 68 into actionable intelligence about the hidden sponsor, whether the organization can maintain `企業秘密` under investigation, and whether E009's interpersonal moral conflict produces any downstream change in the contractor relationship.

No checkpoint or side-source backfill is warranted solely at E009.
