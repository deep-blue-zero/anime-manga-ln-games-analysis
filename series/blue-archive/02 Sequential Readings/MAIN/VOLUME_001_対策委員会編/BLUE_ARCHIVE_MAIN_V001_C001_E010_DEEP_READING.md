---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E010
generation: V1
status: active_provisional
source_boundary: "Canonical Japanese main-story unit BA:main:001:001:010, 対策委員会編 第10話『手がかりを探して』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-16
---

# BLUE ARCHIVE — MAIN V001 C001 E010 DEEP READING
## 対策委員会編 — 第10話「手がかりを探して」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the twelfth canonical main-story object in analytical order and the tenth object in `対策委員会編`:

- story ID: `BA:main:001:001:010`;
- analytical scope: `MAIN_V001_C001_E010`;
- source title: `第10話;手がかりを探して`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第10話`;
- raw group ID: `11100`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- record count: **103**;
- promoted utterance count: **81**;
- normalized choice groups: **1**;
- canonical scene count: **1**;
- normalized person IDs: Ayane, Hoshino, Mutsuki, Nonomi, Serika, Shiroko;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_010.md`;
- complete source-side convenience rendering: `10話_手がかりを探して.md`.

### Canonical scene structure

The promoted source treats the entire episode as one canonical scene:

- `BA:main:001:001:010:scene:001`;
- initial explicit place marker: `アビドス・住宅街`;
- the episode subsequently moves through the interest-payment sequence and into a committee briefing without being split into additional canonical scene objects;
- principal text-bearing span: `ScenarioScriptMain1ExcelTable.json:DataList[1675]–[1775]`, with gaps for control and choice records.

This matters methodologically. “One canonical scene” here is a source-normalization object, not proof of uninterrupted physical location or continuous clock time. Internal narrative transitions must still be read from dialogue and action.

### Choice-space

There is one normalized Sensei choice group:

- `BA:main:001:001:010:scene:001:choice:001` — `ケンカしないで仲良くしてくれると嬉しいな。` — raw `DataList[1702]`.

It is a singleton choice. It expresses a de-escalatory preference but creates no visible route branch. Mutsuki immediately rejects the desired outcome as presently impossible because the assault remains contracted work and Aru is highly motivated to complete it.

### Source-integrity cautions

E010 is analytically strong, but the promoted and convenience layers diverge in several places.

1. **Promoted person metadata does not include Aru.** The convenience rendering labels some committee-briefing lines `アル` and `ムツキ`, but the promoted utterance layer assigns the relevant exposition to established Abydos speaker IDs, principally Ayane. Those convenience labels must therefore not be used to claim Aru or Mutsuki is physically present at the committee briefing.
2. `u:0009` / raw `DataList[1687]` (`な、ななっ！？`) is mapped to the same speaker ID as Mutsuki despite functioning like an interruption/reaction at Mutsuki's entrance. Attribution is unstable and excluded from voice inference.
3. `u:0012` / `DataList[1692]` (`な、何してるんですか！離れてください！`) is likewise mapped to Mutsuki even though Mutsuki has just initiated the physical contact and then answers `おっと、引っ張らないでよー`. The sequence is internally inconsistent if read as one speaker. The line is quarantined rather than silently reassigned.
4. In the convenience rendering, `部活のリーダーの名前はアルさん` / `自らを「社長」と称しているようです` are visually labeled as Aru speech and the following membership explanation as Mutsuki speech. The promoted speaker mapping and story-level person list instead place these inside the committee's research briefing. Current analysis follows the promoted layer.

The major E010 institutional claims do not depend on repairing these anomalies.

### Local-information lock

Available prior analytical authority is limited to:

- the canonical two-unit Prologue and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md` through `E009_DEEP_READING.md`;
- the seven longitudinal ledgers through E009.

No E011 or later main-story unit, Black Market sequence, bond story, MomoTalk, event, character package, relationship bundle, adaptation, wiki, or franchise hindsight is used to identify the hidden sponsor, connect Kaiser Loan to the sponsor, adjudicate the legality of Problem Solver 68, or determine what the Black Market investigation will uncover.

---

# 1. Story placement and local chronology

E009 ended with the failed mercenary assault and Hoshino's decision to begin tracing the attackers through Aru. E010 converts that intention into institutional inquiry while simultaneously returning to the ordinary economic burden that makes Abydos vulnerable in the first place.

Its movement is:

> **morning administrative labor → Mutsuki demonstrates that personal friendliness can coexist with active contractual hostility → monthly interest payment makes the debt relation concrete → committee research identifies Problem Solver 68 as a Gehenna club → weapons forensics identifies the Black Market as the working procurement route → the committee cautiously proposes testing whether the two investigative tracks intersect**

The unit is therefore a pivot from **defense** to **investigation**, but not from uncertainty to omniscience.

The committee does not discover a mastermind. It discovers a route.

It begins with two partially independent questions:

1. **Who are the students who attacked us last night?**
2. **How did the Helmet Gang obtain a discontinued strategic weapon?**

Ayane explicitly presents them as `2つの事案`—two matters. Only after laying out the evidence for each does she say:

> `ふたつの出来事の関連性を探すのも、ひとつの方法かもしれません。`

The wording matters. `かもしれません` preserves uncertainty, and `ひとつの方法` frames linkage as an investigative avenue rather than established fact.

This is a strong methodological feature inside the narrative itself. The characters do not retroactively collapse every hostile actor into one conspiracy merely because the audience suspects a larger structure. They move from separate evidence streams toward a testable common locus.

---

# 2. Narrative reconstruction

Early in the morning, Sensei encounters Ayane in the Abydos residential area. Ayane explains that this is the day the school's interest payment is due. She has come early because repayment requires preparation and because the committee's future plan must be reviewed. Before they separate, she also says she has found information on the previous night's attackers and asks Sensei to review it later at school. Her preliminary finding is explicit: they were students from Gehenna Academy.

Mutsuki abruptly appears and greets Sensei with intense casual familiarity. The source describes her pressing/rubbing close enough that Sensei's weight/breathing becomes part of the joke. The promoted speaker layer then contains an attribution anomaly around the protest demanding that she let go, so the exact speaker of that objection is quarantined.

What follows is clean. Mutsuki recognizes Ayane as the glasses-wearing Abydos student from the ramen shop and the subsequent assault. Ayane objects to the overfamiliarity and insists on her name.

Mutsuki's answer extends the ethical compartmentalization established in E009:

> `だって私たち、別にメガネっ娘ちゃんたちのことが嫌いなわけじゃないし。`

and:

> `ただ、部活で請け負ってる仕事だからさ。仕事以外の時は仲良くしたっていいじゃん？`

The hostility is therefore not narrated by Mutsuki as hatred. In her model, the attack belongs to the domain of contracted club work; ordinary social relations can continue outside that role.

Ayane recognizes exactly what Mutsuki is doing and protests that she is attempting, after the fact, to divide public/professional and private conduct: `今さら公私を区別しようということですか！？`

Mutsuki then brings Sensei into the dispute through a striking nonpossessive claim:

> `「シャーレ」の先生は、あんたたちだけのモンじゃないでしょ？`

Sensei is not something that belongs only to Abydos.

The sole choice expresses a wish that they stop fighting and get along. Mutsuki says that is impossible for now because the attack is still work and Aru's motivation is high; if Mutsuki performs carelessly, Aru will be angry. Yet she also invites Sensei to visit Problem Solver 68 someday and says Aru and the others would be happy.

Ayane rejects the implied future friendliness and angrily says that next time she sees Mutsuki she will shoot her on the spot. The scene is comic in register, especially because Mutsuki responds with an airy `はいはーい`, but the anger also has an obvious concrete basis: Mutsuki's organization attacked the school the previous day and is now acting socially casual about it.

The narrative then makes the debt relation concrete.

A bank/loan employee states that after applying the variable interest and related terms, the current interest payment is:

> `788万3250円`

—**¥7,883,250**.

The payment is made entirely in cash. The employee thanks the students for doing business with `カイザーローン` and says they will see them again next month.

After the cash transport vehicle leaves, Hoshino says they somehow survived another month. Shiroko asks how long remains until repayment. Ayane answers that it is a **309-year repayment**, but Serika stops the calculation, saying the exact number will only increase her stress and that they cannot finish repaying within their lifetimes anyway.

Nonomi notices another institutional peculiarity: why does Kaiser Loan accept only cash, to the point that a cash-transport vehicle must be arranged? The episode does not answer her question.

Shiroko looks at the departing vehicle. Serika immediately tells her not to attack it. Shiroko says she understands. Serika adds that she must not even make a plan. Shiroko's quieter `うん……` preserves the E008 bank-robbery callback and demonstrates that the group now anticipates her operational imagination before she verbalizes it.

Hoshino redirects attention from the debt toward the immediate security problem and brings everyone back to the classroom.

Ayane formally opens the briefing by saying there are two matters to discuss.

The first is Problem Solver 68. The committee's research identifies it as a Gehenna student club. It has a reputation there for dangerous behavior and poor conduct. Ayane describes the `便利屋` model as a service provider that handles whatever it is asked to do. The leader is Aru, who calls herself `社長`; beneath her are three members using the titles `室長`, `課長`, and `平社員`.

Hoshino is amused by the corporate form. Nonomi reacts positively to the idea of a student president/CEO, but Ayane stresses that the title is self-appointed. The club appears to be hiding somewhere inside the Abydos area.

Shiroko asks whether Gehenna permits students to establish companies. Ayane answers cautiously: she does not think so and supposes they started one on their own. This is not a verified legal ruling and must remain reported inference at this boundary.

Nonomi says the four had not looked like bad students to her. Ayane answers that, according to what she found, they have committed many acts of delinquency and are treated as problem students in Gehenna. Her emotional hostility is visible enough that Serika later asks whether something happened that morning.

Hoshino suggests that next time they capture the group and interrogate them. Ayane agrees eagerly if the opportunity arises.

Ayane then turns to the second matter: the hidden force behind the Helmet Gang attack on Serika.

Analysis of the strategic-weapon fragments recovered from the previous fighting has produced a new forensic result. The model number is no longer traded and production has been discontinued. The students therefore ask the obvious procurement question: how could the Helmet Gang have obtained it?

Ayane gives the committee's current answer:

> `生産が中止された型番を手に入れる方法は……キヴォトスでは「ブラックマーケット」しかありません。`

The Black Market is presented as dangerous. Ayane explains that students who have left ordinary school participation for various reasons—`中退、休学、退学`—form groups there, and that many unapproved clubs operate without Federal Student Council authorization.

Shiroko asks whether that means groups like Problem Solver 68. Ayane says yes and adds that Problem Solver 68 has reportedly caused incidents in the Black Market several times.

Nonomi identifies the overlap as potentially important.

Ayane remains cautious:

> `ふたつの出来事の関連性を探すのも、ひとつの方法かもしれません。`

Hoshino accepts the investigative direction and proposes looking into the Black Market because they may find an unexpected clue.

The next-title marker is:

> `次回;ブラックマーケットへ（１）`

---

# 3. Central thesis

The strongest E010 thesis is:

> **E010 converts the Abydos conflict from a sequence of attacks into an evidence-driven investigation while simultaneously revealing that the school's debt is an active institutional relationship rather than inert backstory. Ayane keeps the contractor problem and the weapons-procurement problem analytically separate, then proposes the Black Market as a testable point of intersection rather than assuming a single conspiracy. In parallel, Kaiser Loan's exact variable-interest collection, cash-only repayment, and 309-year horizon make ordinary student labor visibly incapable of resolving the debt on normal timescales. The episode therefore links two forms of structural opacity—hidden coercive sponsorship and opaque long-duration credit—without yet proving that they belong to the same actor.**

A second thesis concerns Mutsuki and the ethics of `公私`.

E009 established her principle under direct combat:

> gratitude for hospitality can be real while professional hostility remains active.

E010 proves that this was not a battlefield excuse improvised once. Mutsuki applies the same model in ordinary morning life. She says she does not dislike the Abydos students, treats the attack as `部活で請け負ってる仕事`, and sees no contradiction in being friendly outside work.

This turns `公私` from a line into a **stable provisional worldview**.

A third thesis concerns Sensei's institutional position.

Mutsuki's `シャーレの先生は、あんたたちだけのモンじゃない` echoes a conclusion already reached from the Prologue architecture: Schale is cross-institutional. Sensei can work closely with Abydos without becoming Abydos property, exclusive advocate, or substitute sovereign.

Sensei's own response is de-escalatory, but it does not compel peace. Mutsuki refuses because her student organization remains committed to its job. The adult can articulate a norm without automatically overriding student agency.

---

# 4. Scene-by-scene close reading

Because E010 is one promoted canonical scene with multiple internal movements, the following sections follow narrative functions rather than canonical scene splits.

## 4.1 Ayane's morning: administration before adventure

Stable evidence: `u:0002-0007`, raw `DataList[1678]–[1683]`.

The episode opens not with the prior battle, the mysterious sponsor, or weapons, but with Ayane preparing a financial payment before ordinary school activity.

Her phrasing is procedural:

- `今日は利息を返済する日`;
- `色々と準備`;
- `返済の準備`;
- `今後の計画も見直さないと`.

This strengthens the image of Ayane as the committee's administrative center. The debt consumes not only money but **planning time, attention, and routine institutional labor**.

The school crisis is therefore lived through recurring administration. Insolvency is not a single dramatic revelation from E004. It has calendar dates, preparation work, transport, accounting, and the need to repeatedly revise plans.

Ayane also reports that she has already found information on the attackers before the formal briefing. The contrast with Sensei is important. Sensei does not arrive carrying a solved dossier. The student institution performs the research and asks the adult to review it later.

This is additional counterevidence to both the omnipotent-avatar model and the student-incapacity model.

## 4.2 E010 resolves Gehenna affiliation without requiring hindsight

Ayane says directly:

> `ゲヘナ学園の生徒だったのですが、`

The later briefing confirms that the people who attacked Abydos belong to the Gehenna-associated `便利屋68` club.

This resolves an uncertainty intentionally preserved in E008. There, Shiroko had only asked whether their uniforms were Gehenna uniforms and the promoted story lacked a normalized school ID. It would have been premature to convert visual recognition into settled affiliation.

E010 now supplies the missing in-story research result.

**Revision transition:**

> Gehenna-indicative uniform recognition → **STRENGTHEN to explicit reported affiliation**.

The project should preserve this sequence because it demonstrates why local-information locks matter. A conclusion can be correct in hindsight and still be analytically premature when first encountered.

## 4.3 Mutsuki's friendliness is compatible with hostility because she partitions roles

Clean core evidence: `u:0014-0024`, excluding quarantined anomaly lines.

Mutsuki does not attempt to pretend the prior attack did not happen. Ayane explicitly references both the ramen-shop meeting and the school assault.

Mutsuki's answer is not apology. It is a theory of relation:

> `別にメガネっ娘ちゃんたちのことが嫌いなわけじゃないし。`

The attack does not, in her account, express personal hatred.

Then:

> `部活で請け負ってる仕事だからさ。仕事以外の時は仲良くしたっていいじゃん？`

This is the peacetime equivalent of E009's `それはそれ、これはこれ` and `公私`.

The pattern is now longitudinally secure enough for a bounded formulation:

> **Mutsuki treats institutional/contractual roles and personal affect as separable domains.**

That is not the same as saying she is morally neutral, emotionally shallow, or incapable of loyalty. The evidence only establishes a willingness to preserve ordinary friendliness across a role boundary that also permits organized violence.

## 4.4 Ayane rejects Mutsuki's partition because harm remains relationally salient

Ayane responds:

> `今さら公私を区別しようということですか！？`

The phrase `今さら` is important. Ayane's objection is not that public/private distinction is conceptually impossible. It is that Mutsuki is invoking it **after participating in an attack**.

Where Mutsuki treats role separation as sufficient to protect social friendliness, Ayane treats past harm as something that legitimately contaminates the supposedly private relation.

This extends the E009 conflict between Serika's `恩` and Mutsuki's `公私`:

- Serika: kindness should constrain later hostile action;
- Ayane: hostile action should constrain later friendly intimacy;
- Mutsuki: both directions can remain partitioned.

The arc is therefore exploring the permeability of roles from both sides.

## 4.5 `シャーレの先生は、あんたたちだけのモンじゃない`: nonpossessive adult authority

Mutsuki's strongest institutional line is:

> `「シャーレ」の先生は、あんたたちだけのモンじゃないでしょ？`

The colloquial `モン`—“thing/property”—makes the possessive framing unusually explicit.

This line should **not** be romanticized into jealousy triangulation. The immediate issue is institutional/social access to Sensei. Mutsuki argues that Sensei's connection to Abydos is not exclusive because Sensei is Schale's teacher.

This aligns with prior evidence:

- Schale was created as a cross-jurisdictional institution;
- multiple schools invited future contact in the Prologue;
- Sensei assists Abydos without becoming its owner/governor;
- E008–E009 showed authority activated differently by context.

E010 adds a student-side articulation of the same structure:

> **closeness to one school does not convert a cross-school adult into that school's possession.**

## 4.6 Sensei's de-escalatory preference is morally legible but causally bounded

Choice 001:

> `ケンカしないで仲良くしてくれると嬉しいな。`

This is one of the clearest low-coercion Sensei formulations in the Abydos arc. Sensei does not threaten, command reconciliation, invoke federal authority, or demand that Mutsuki cancel the contract.

The wording is a preference: `嬉しいな`.

Mutsuki's response establishes the limit:

> `それはムリかなー。こっちも仕事だからね。`

She further says Aru is highly motivated and would become angry if she performs the job carelessly.

Thus:

> **Sensei can voice a cross-group norm without possessing the power—or choosing to use power—to make students obey it.**

This strengthens the existing model of ethical/persona choice over route sovereignty.

## 4.7 Mutsuki's invitation complicates enemy categories without dissolving them

Mutsuki invites Sensei to visit Problem Solver 68:

> `いつかうちの便利屋に遊びにおいでよ、先生。`

and says Aru and the others would be happy.

This should not be treated as proof that Problem Solver 68 has abandoned hostility, nor as proof of manipulation. The line is compatible with the worldview she has just explained: outside contracted work, personal sociality can be genuine.

The significant point is that Blue Archive's opponent categories are becoming **institutional rather than totalizing**.

A person can be:

- an enemy in one operational context;
- friendly in another social context;
- bound to an organization whose objectives remain opposed to yours.

That complexity is already present before any later reconciliation material is consulted.

## 4.8 Ayane's threat is emotionally meaningful but should not be literalized

Ayane says:

> `今度会ったらその場で撃ちます！`

Given the comic rhythm and Mutsuki's dismissive `はいはーい`, the safest reading is **heightened anger expressed through Kivotos's normalized armed idiom**, not a verified intent to murder Mutsuki on sight.

At the same time, reducing it to empty comedy would also be wrong. Ayane is genuinely furious because Mutsuki participated in an attack and immediately behaves as though ordinary friendliness can resume.

The important character contrast appears later: when Ayane runs the formal briefing, her anger does not cause her to collapse the evidence into certainty. She still presents separate cases and a tentative linkage hypothesis.

So E010 gives Ayane a useful combination:

> **high personal affect + disciplined institutional reasoning.**

## 4.9 The exact monthly interest: ¥7,883,250

Stable evidence: `u:0029`, raw `DataList[1712]`.

E008 gave the rounded student statement `利息だけで788万円`.

E010 provides the creditor-side exact amount after applying `変動金利等を諸々`:

> **¥7,883,250**.

This does three things.

First, it verifies that Serika's E008 number was not hyperbole.

Second, it introduces **variable interest** as part of the current loan mechanics.

Third, it shows that the debt is administered through a recurring external institution with formal collection rather than merely existing as a number in the students' internal accounts.

The episode still does not provide enough data to reconstruct the complete amortization formula, rate-reset mechanism, contractual history, or principal reduction. Any financial model beyond the stated figures should remain provisional.

## 4.10 Kaiser Loan enters as a current institution, not yet as a proven villain

The employee says:

> `カイザーローンとお取引いただき、毎度ありがとうございます。来月もよろしくお願いいたします。`

This is the first sequential unit in the current analysis to name the active creditor institution directly.

The tone is formally commercial. The students are recurring customers/debtors, and the payment repeats monthly.

There is an obvious temptation to connect the name `カイザー` to E007's convenience-layer label for the unresolved high-rise sponsor. That inference is **not currently authorized**.

Why not?

- E007's promoted canonical layer deliberately kept the sponsor unidentified.
- The convenience rendering supplied a candidate label that was explicitly quarantined from current authority.
- E010 canonically names `カイザーローン`, but it does not state that the creditor and the hidden sponsor are the same organization or related entities.

Therefore the correct state is:

> **Kaiser Loan is now a canonical creditor institution. Any relationship between Kaiser Loan and the E007 sponsor is OPEN.**

This distinction is important enough to preserve in the claim ledger.

## 4.11 Cash-only repayment is an anomaly noticed inside the text, not yet an explanation

Nonomi asks:

> `カイザーローンはなぜ現金でしか受け付けないのでしょうね？`

and notes that a cash transport vehicle must be arranged.

The narrative itself therefore marks the payment method as unusual enough to attract student curiosity.

But E010 gives no answer.

It would be premature to conclude:

- money laundering;
- corruption;
- evasion of financial oversight;
- intentional predation;
- connection to the Black Market;
- connection to the sponsor.

Current authority supports only:

> **Kaiser Loan requires cash payment; this requirement is unusual enough that Nonomi questions it; its purpose remains unknown.**

The distinction between anomaly and explanation is exactly the same discipline the committee later applies to its two investigative cases.

## 4.12 The 309-year horizon converts “large debt” into intergenerational impossibility

Shiroko asks how long remains until repayment. Ayane begins:

> `309年返済なので……`

Serika stops her and says:

> `どうせ死ぬまで完済できないんだし！`

The point is not only numerical magnitude. A 309-year repayment frame exceeds any individual's ordinary lifespan many times over.

This alters the existential character of the debt.

A conventional student effort ethic assumes that sufficiently hard work can eventually discharge an obligation. Abydos's current financing structure breaks that intuitive relationship between effort and completion.

The students can:

- work part-time;
- capture wanted criminals;
- solve complaints;
- volunteer;
- economize;
- skip meals;
- make the monthly payment;

and still face a horizon no living member can personally complete.

This is why Serika's desperation in E008 cannot be explained simply as impatience. The ordinary moral promise “work hard and repay what you owe” has been stretched beyond a human timescale.

## 4.13 `死ぬまで完済できない`: debt pressures identity, not only budget

Serika's phrasing is emotionally blunt. The debt is measured against life expectancy.

This links back to her E005 self-concept:

> **I am someone who stays and contributes.**

The difficulty is that no amount of staying within one lifetime appears sufficient to see the debt extinguished.

This creates a durable tension in Serika's ethics:

- she strongly believes in work, repayment, and not abandoning Abydos;
- the institutional terms make complete repayment impossible on her personal horizon.

The story has not yet resolved that contradiction. It should remain a major longitudinal Serika and institutional thread.

## 4.14 Shiroko and the cash truck: recurring criminal imagination as known social pattern

Nonomi's question about the cash truck is followed by Shiroko's silence.

Serika immediately says:

> `シロコ先輩、あの車は襲っちゃダメだよ。`

When Shiroko agrees, Serika adds:

> `計画もしちゃダメ！`

This is a callback to E008's fully prepared bank-robbery proposal, but it also tells us something relationally important.

The group now knows Shiroko's problem-solving style well enough to **intercept the planning stage before speech**.

Shiroko's `うん……` is comic, but it also preserves continuity: her operational imagination has not disappeared merely because the prior proposal was vetoed.

The committee's governance therefore includes informal mutual regulation based on knowledge of each member's tendencies.

## 4.15 `2つの事案`: Ayane preserves analytical separation

Stable evidence: `u:0049-0050`.

Ayane's briefing begins:

> `まずは、2つの事案についてお話ししたいと思います。`

This phrase is one of the episode's most important structural lines.

The story already knows, at the audience level, that an unresolved sponsor hired Problem Solver 68 after the Helmet Gang failed. A less disciplined reading could therefore treat all hostile evidence as one confirmed network.

Ayane does not have that audience knowledge.

She presents:

1. the previous night's Problem Solver 68 assault;
2. the Helmet Gang's hidden backer / discontinued weapon.

Only later does she propose searching for linkage.

This is good in-world epistemology and should guide the external analysis too.

## 4.16 Problem Solver 68 becomes an investigated institution

Ayane's research produces several levels of evidence.

### Strong current facts

- the attackers are students associated with Gehenna;
- their club is called `便利屋68`;
- the club performs requested jobs as a service activity;
- Aru is its leader and uses the title `社長`;
- three other members use corporate-style titles;
- the group is currently somewhere in the Abydos area.

### Reported reputation

Ayane says they are known in Gehenna as dangerous and badly behaved and have committed substantial delinquency.

This is **reported institutional reputation**, not a substitute for direct character reading. E008–E009 already independently demonstrate serious misconduct—the group accepted and carried out an armed assault—so the reputation is not unsupported, but later analysis should still distinguish reputation from observed action.

### Ayane's inference about business legality

When Shiroko asks whether Gehenna allows student startups, Ayane says:

> `それはないと思いますが……勝手に起業したのではないでしょうか。`

The hedges `と思います` and `ではないでしょうか` matter.

Current authority does **not** support a definitive general rule “Gehenna legally prohibits student businesses.” It supports that Ayane does not think this operation is formally authorized and suspects self-organization outside normal rules.

## 4.17 Nonomi preserves the distinction between observed person and reported reputation

Nonomi responds:

> `悪い子たちには見えませんでしたが……。`

This is a small but important epistemic counterweight.

She is not denying the assault. She personally experienced both the shared meal and the later conflict. Her point is that the individuals did not present in ordinary interaction as reducible to “bad kids.”

This maintains a central E008–E009 distinction:

> **humanization does not erase wrongdoing, and wrongdoing does not exhaust personhood.**

Ayane's report and Nonomi's perception can both be true at once.

## 4.18 Ayane's grudge does not invalidate her investigation—but it becomes relevant evidence about the investigator

Ayane advocates heightened caution and is unusually eager about the prospect of capturing/interrogating Problem Solver 68.

Serika notices:

> `並々ならぬ恨みを感じるんだけど……。`

Ayane denies that anything happened.

The comedy clearly refers back to the morning Mutsuki encounter.

Analytically, the useful point is not “Ayane is biased, therefore her research is false.” That would be an overcorrection.

Instead:

- Ayane has a personal emotional reaction;
- her research briefing contains sourced/report-style information;
- she nevertheless preserves two-case separation and tentative linkage language.

Thus E010 supplies evidence that **institutional reasoning can remain disciplined even when the researcher is personally irritated**.

## 4.19 The obsolete model number turns the arms question into provenance analysis

Ayane's forensic result:

> `現在は取引されていない型番`

The weapon model is no longer traded.

Hoshino asks whether that means production has ended. Serika asks the procurement question: how was it obtained?

The analytical frame has therefore shifted from:

> “the enemy had a powerful weapon”

to:

> **“what supply chain can still deliver an obsolete/discontinued weapon?”**

This is a more mature institutional question because capability is treated as evidence of logistics.

E007 had already suggested tracing `流通ルート`. E010 now narrows the route.

## 4.20 The Black Market is introduced as an institutional shadow ecology

Ayane says the only current Kivotos route she knows for obtaining such a discontinued model is the `ブラックマーケット`.

She then describes the population and organizational ecology:

- students who have left standard school participation through `中退`, `休学`, or `退学`;
- groups formed among such students;
- many `非認可の部活` operating without Federal Student Council permission.

The Black Market should therefore not yet be flattened into “a criminal shopping district.”

At this boundary it appears to be a **parallel student social/institutional space outside ordinary recognized school structures**.

Its defining features include:

- disrupted or severed school affiliation;
- alternative group formation;
- unapproved organizational life;
- illicit or unavailable goods circulation;
- enough danger that Nonomi immediately reacts to the location as risky.

Whether it has governance, territorial rules, internal authorities, or stable markets beyond this remains OPEN until the next unit.

## 4.21 School exit matters because Kivotos normally organizes personhood institutionally

Across the first ten Abydos episodes, school affiliation has been repeatedly important:

- Abydos's survival is bound to maintaining a school despite depopulation;
- student count affects money and political voice;
- Problem Solver 68 is investigated through Gehenna affiliation;
- Schale crosses academy boundaries;
- clubs carry operational roles.

The Black Market description introduces students whose relation to school has broken down or become suspended.

That makes `中退・休学・退学` more than demographic color. It suggests that Kivotos contains students who exist **outside or at the edge of the academy-centered institutional order**.

The text does not yet tell us what that means for rights, policing, welfare, or identity. Those are forward questions, not current conclusions.

## 4.22 Problem Solver 68 becomes a bridge clue, not proof of common authorship

Shiroko asks:

> `便利屋68みたいに？`

Ayane says Problem Solver 68 has reportedly caused incidents in the Black Market.

Nonomi sees this as an important point.

The inference chain is now:

- discontinued weapon → Black Market likely procurement route;
- Problem Solver 68 → reported Black Market activity;
- therefore Black Market could contain evidence relevant to both hostile incidents.

But the episode carefully stops short of:

> “Problem Solver 68 supplied the Helmet Gang.”

or:

> “Problem Solver 68 and the Helmet Gang have the same employer.”

or:

> “the Black Market is controlled by the hidden sponsor.”

The operative language is `関連性を探す`—**look for a relationship**.

That distinction should remain explicit in all downstream synthesis.

## 4.23 Hoshino turns uncertainty into an investigable next action

Hoshino's close is:

> `ブラックマーケットを調べてみよう。`

followed by:

> `意外な手がかりがあるかもしれないしね。`

This is a good example of her strategic style.

She does not demand certainty before acting, but neither does she convert a hypothesis into fact. The Black Market is worth investigating precisely because it may produce an unexpected clue.

The shift is:

> **uncertainty → bounded exploratory action**.

That is an important form of competence distinct from tactical command.

---

# 5. Character-state analysis

## 5.1 Ayane — administrator, investigator, and emotionally invested participant

E010 is one of Ayane's strongest units so far.

### Trait / strategy

She demonstrates high administrative conscientiousness:

- early arrival;
- repayment preparation;
- future-plan revision;
- attacker research;
- meeting structure;
- forensic synthesis.

### State

She is also personally angry at Mutsuki.

The text does not make her a detached bureaucrat. Her institutional competence coexists with irritation, embarrassment, and a willingness to threaten violence in comic register.

### Value

Ayane values boundaries and accountability. Mutsuki's attempt to act friendly after attacking the school feels illegitimate to her.

### Development

Her role has expanded:

> operator/secretary → crisis coordinator → forensic analyst → case organizer/investigative lead.

E010 strengthens her as one of the principal epistemic engines of the Abydos arc.

## 5.2 Mutsuki — `公私` becomes a stable relational doctrine

E009 gave Mutsuki a wartime expression of compartmentalization. E010 demonstrates continuity outside combat.

She can:

- attack Abydos as work;
- not hate the Abydos students;
- greet them casually later;
- seek friendly relations outside work;
- invite Sensei to visit her organization;
- still refuse Sensei's requested reconciliation because the contract remains active.

This is coherent, not random.

Bounded formulation:

> **Mutsuki treats roles as context-dependent and resists allowing one hostile institutional role to totalize all personal relations.**

Whether the story ultimately endorses that ethic is OPEN. Ayane and Serika provide direct counterarguments.

## 5.3 Sensei — cross-institutional, de-escalatory, and epistemically dependent

Sensei's only authored choice is conciliatory.

But the larger structural evidence is even more important:

- Ayane finds the attacker information;
- the committee conducts the weapons analysis;
- the students identify the Black Market;
- Hoshino chooses the investigative next step.

Sensei is present and consulted, but not omniscient.

Mutsuki's possessive-language challenge further clarifies that Sensei's intimacy with Abydos does not make Schale an Abydos-owned resource.

## 5.4 Nonomi — curiosity about systems and resistance to moral flattening

Nonomi asks why Kaiser Loan requires cash only. This is a small but valuable institutional observation: she notices process anomalies rather than only the painful amount.

Later, she resists collapsing Problem Solver 68 into its reputation:

> `悪い子たちには見えませんでしたが……。`

Her recurring care orientation is therefore joined by an epistemic tendency to keep ordinary personhood visible even after conflict.

## 5.5 Shiroko — operational imagination and concise institutional questioning

E010 gives Shiroko two different modes.

The comic mode is the cash truck: her silence is enough for Serika to infer a robbery plan.

The investigative mode is equally concise:

- does Gehenna permit startups?
- does “unapproved club” mean something like Problem Solver 68?

She repeatedly asks questions that test **organizational category and operational possibility**.

## 5.6 Serika — repayment ethics under an impossible horizon

Serika's existing ethic emphasizes contribution, staying, and repayment.

E010 confronts that ethic with a 309-year structure.

Her refusal to hear the exact completion number is not rejection of repayment responsibility. She has repeatedly worked toward it. It is recognition that the current schedule exceeds her life.

Her role as social regulator of Shiroko also continues: she stops not only the robbery but the plan.

## 5.7 Hoshino — separates urgent threat from permanent burden

After the payment, Hoshino says the immediate problem should be addressed first and returns the group to the classroom.

This is strategically sensible prioritization:

- the debt is catastrophic but chronic;
- the contractor/sponsor threat is acute and actionable.

She later selects investigation of the Black Market as the next bounded move.

---

# 6. Relationship-state analysis

## 6.1 Mutsuki ↔ Ayane

Current state:

> **active institutional hostility + attempted unilateral social casualness + boundary rejection**.

Mutsuki addresses Ayane through a teasing visual label before eventually using `アヤネちゃん`. Ayane insists on her proper name and refuses Mutsuki's attempt to normalize friendliness.

The relationship is not simple mutual hatred. Mutsuki explicitly denies dislike. The asymmetry is that Ayane does not accept Mutsuki's framework for separating work from ordinary relation.

## 6.2 Mutsuki ↔ Sensei

E010 establishes direct social ease and invitation.

Mutsuki treats Sensei as someone she can greet physically/casually, recruit into a conversational alliance against Ayane's exclusivity, and invite to Problem Solver 68.

No romance claim is warranted.

The strongest current formulation is:

> **Mutsuki recognizes Sensei as a cross-group social figure whose accessibility should not be monopolized by Abydos.**

## 6.3 Sensei ↔ Abydos

Mutsuki's line functions as outside commentary on an increasingly close relationship.

Sensei is embedded enough that another student can jokingly accuse Abydos of treating Sensei as “theirs,” but the actual institutional record remains nonpossessive:

- Sensei has no exclusive Abydos office;
- Schale remains cross-school;
- student governance remains intact;
- Sensei's preferences can be refused.

## 6.4 Abydos ↔ Problem Solver 68

E009 gave direct armed hostility.

E010 adds investigation and ordinary post-conflict contact.

The relationship now includes:

- hospitality memory;
- contract violence;
- differing theories of `公私`;
- personal curiosity/friendliness;
- institutional intelligence gathering;
- plans for capture/interrogation if possible.

This is an unusually dense relationship for actors who have known one another only briefly.

## 6.5 Abydos ↔ Kaiser Loan

This relationship now deserves explicit longitudinal tracking.

Current known features:

- creditor/debtor relation;
- recurring monthly interest collection;
- variable interest/related terms;
- cash-only payment;
- cash transport;
- 309-year repayment horizon;
- students experience payment as survival from month to month.

Unknown:

- original loan terms beyond the E004 disaster-history account;
- present principal movement;
- refinancing history details;
- reason for cash-only payment;
- legal/regulatory status;
- relationship, if any, to the hidden sponsor.

---

# 7. Institutional-state analysis

## 7.1 Abydos is now clearly an investigative institution as well as a defense institution

The Countermeasures Committee has accumulated:

- routine administration;
- accounting specialization;
- defensive command structures;
- forensic recovery of weapon fragments;
- attacker identification;
- reputation research;
- hypothesis formation;
- prioritization of next investigative location.

This strongly continues to reject the idea that student governance is inherently incapable.

## 7.2 Problem Solver 68 is explicitly a Gehenna student club

E010 resolves school affiliation at the story level through Ayane's research.

The organization continues to mimic corporate form:

- `社長`;
- `室長`;
- `課長`;
- `平社員`.

But Ayane repeatedly calls it a `部活`.

The tension is important:

> **student club form + business rhetoric + paid service activity + possible nonauthorization**.

Do not resolve that tension into “real corporation” or “mere pretend club” yet.

## 7.3 Kaiser Loan becomes a named current institution

E004 gave the debt's disaster history. E010 names the current creditor/collector.

This creates a distinct analytical responsibility because the debt now has an organizational counterparty and recurring procedures.

Provisional institutional formulation:

> **Abydos's debt is maintained through an ongoing creditor relation whose terms produce recurring interest obligations on a timescale vastly exceeding the students' lives.**

Whether the arrangement is exploitative by design, legally irregular, or connected to hostile actors remains OPEN.

## 7.4 The Black Market is a liminal institutional zone

At introduction, the Black Market concentrates:

- unavailable/discontinued goods;
- students outside standard school participation;
- collective formation among those students;
- non-GSC-approved clubs;
- prior Problem Solver 68 incidents.

It is therefore likely to matter not merely as “where criminals shop,” but as a counter-space to Kivotos's academy-centered governance.

That hypothesis should be tested in E011 rather than treated as complete now.

---

# 8. Sensei role and choice-space

E010's sole choice is ethically simple but structurally useful.

Sensei says that peaceful friendship would make Sensei happy.

Three observations follow.

### 8.1 The choice is relational, not sovereign

Sensei expresses preference rather than order.

### 8.2 The preference fails to determine behavior

Mutsuki says reconciliation is impossible while work obligations remain active.

### 8.3 Schale remains cross-institutional

Mutsuki explicitly denies that Abydos owns exclusive access to Sensei.

Together these strengthen the existing model:

> **Sensei can be morally influential and relationally central without being causally omnipotent or institutionally possessed.**

---

# 9. Japanese-language analysis

## 9.1 `公私`

E009 introduced Mutsuki's explicit `公私` distinction in battle.

E010 has Ayane throw the same concept back at her:

> `今さら公私を区別しようということですか！？`

The repetition turns the term into an active ethical keyword shared across opposing interpretations.

## 9.2 `請け負ってる仕事`

Mutsuki says Problem Solver 68's attack is work the club has `請け負ってる`—accepted/undertaken on commission.

The verb reinforces the contractor model from BA-C012 without telling us the full contract terms.

## 9.3 `モン`

`あんたたちだけのモンじゃない` uses colloquial “thing/property” language.

It sharpens the nonpossessive framing of Sensei more than a neutral “Sensei works for other schools too” would.

## 9.4 `変動金利`

The banker's `変動金利等を諸々適用し` formally introduces variable-rate mechanics.

The loan burden is therefore not described as a perfectly static historical contract.

## 9.5 `309年返済`

This compact phrase is one of the arc's strongest scale markers. It converts abstract debt magnitude into human timescale.

## 9.6 `2つの事案`

`事案` is administrative/investigative vocabulary. Ayane frames the attacks as cases to organize rather than simply enemies to hate.

## 9.7 `関連性を探す`

The verb `探す` is epistemically crucial. They are **searching for** a connection, not reporting one.

## 9.8 `非認可の部活`

This phrase introduces a category of student organization existing outside Federal Student Council approval.

It should be tracked separately from merely “criminal gang,” because the language retains the club/institutional form while marking authorization failure.

---

# 10. Motifs, symbols, and longitudinal callbacks

## 10.1 Debt as calendar

E004: debt history.\
E005: wages applied to interest.\
E008: ¥7.88m monthly interest.\
E010: exact ¥7,883,250 collection day.

Debt has progressed from backstory → labor → arithmetic → recurring ritual.

## 10.2 Debt as lifespan

The `309年返済` / `死ぬまで完済できない` pair moves debt from economics into mortality.

## 10.3 Vehicles as economic objects

Earlier vehicles carried combatants, kidnappers, and rescue targets. E010's cash transport vehicle is a financial-logistics object—and immediately activates Shiroko's criminal-planning motif.

## 10.4 Roles that do not totalize persons

E008: opponents share ramen.\
E009: kindness collides with contract.\
E010: Mutsuki explicitly claims friendship can exist outside work.

The motif is now stable enough to track longitudinally.

## 10.5 Evidence fragments

The broken strategic weapon is not discarded after battle. Its fragment becomes an investigative artifact whose model number reveals a supply-route clue.

Violence leaves material evidence.

## 10.6 The edge of school society

The Black Market introduces students outside ordinary academy participation. This mirrors Abydos's fear of disappearance from institutional existence from another direction: one school struggles not to vanish; elsewhere students already inhabit spaces beyond ordinary school structures.

That comparison is promising but remains provisional until the Black Market is actually visited.

---

# 11. Violence, ethics, and power

## 11.1 Violence is increasingly mediated by institutions

The arc no longer depicts violence as simply “students with guns.”

It now includes:

- sponsor procurement;
- contractors;
- subcontracted mercenaries;
- weapon markets;
- investigative forensics;
- unapproved clubs;
- possible interrogation.

Violence has a political economy and an organizational infrastructure.

## 11.2 Mutsuki's `公私` model does not erase responsibility

Her claim that hostility is only work explains her affect; it does not show that the contract morally compels her or makes the harm neutral.

E009 already showed that intermediaries retain agency. E010 strengthens this because Mutsuki can imagine refusing social hatred while continuing operational violence.

## 11.3 Ayane/Hoshino's interrogation proposal opens a new ethical question

Hoshino suggests capturing and interrogating Problem Solver 68; Ayane agrees.

The exact methods are unstated. Do not translate `取り調べ` into torture or unlawful coercion without evidence.

But it does mean the committee is willing to move beyond defense toward coercive information gathering if it captures an attacker.

This should be tracked.

## 11.4 Credit power and coercive power are adjacent but not yet connected

The episode places Kaiser Loan and the sponsor investigation in the same unit, but narrative adjacency is not proof of common control.

The disciplined reading is:

- credit structurally burdens Abydos;
- coercive actors structurally attack Abydos;
- E010 does not prove they have the same principal.

---

# 12. Competing readings and counterevidence

## Reading A: “E010 proves Kaiser Loan is behind the attacks.”

**REJECT at this boundary.**

Kaiser Loan is canonically named as creditor. The E007 sponsor remains unidentified in the promoted layer. No E010 line connects the two.

## Reading B: “The Black Market proves Problem Solver 68 supplied the Helmet Gang.”

**REJECT.**

The episode says Problem Solver 68 has reportedly caused trouble there and the discontinued weapon likely came from there. Ayane explicitly proposes searching for a relationship; she does not state one.

## Reading C: “Mutsuki is only pretending to be friendly.”

**UNSUPPORTED.**

Her friendliness is perfectly consistent with her stated compartmentalization ethic. Manipulation is possible in principle but not established here.

## Reading D: “Mutsuki's friendliness means the conflict is not serious.”

**REJECT.**

She explicitly says the work continues and that Aru will object if she performs carelessly.

## Reading E: “Ayane is jealous of Mutsuki romantically.”

**REJECT as current-authority inference.**

Ayane has obvious nonromantic reasons for anger: Mutsuki attacked her school and immediately becomes physically/socially familiar with Sensei. No romance marker is required.

## Reading F: “309 years means the debt literally cannot ever be repaid.”

**TOO STRONG.**

The stated schedule is 309 years and Serika believes they will not finish within their lives. Future refinancing, principal changes, windfalls, or institutional changes are unknown.

## Reading G: “Cash-only repayment proves criminal finance.”

**REJECT.**

The text marks cash-only collection as unusual but supplies no explanation.

## Reading H: “Ayane's anger invalidates her intelligence report.”

**REJECT.**

Her emotional involvement is real, but she still distinguishes evidence levels, separates two cases, uses hedged language where appropriate, and proposes testing rather than assuming linkage.

## Reading I: “Black Market students are all criminals.”

**REJECT.**

Ayane describes students gathered there after `中退・休学・退学` and notes unapproved clubs. Those status categories do not by themselves establish criminality for every person.

---

# 13. Cumulative ledger deltas

## Character ledger

### AYANE — STRENGTHEN
Administrator/investigator role expands sharply. E010 adds debt-day preparation, attacker research, formal two-case briefing, forensic weapons analysis, and disciplined linkage hypothesis despite personal irritation toward Mutsuki.

### MUTSUKI — STRENGTHEN
`公私` compartmentalization becomes longitudinally stable outside battle. She explicitly says she does not dislike Abydos, treats hostility as commissioned club work, and maintains social friendliness outside the job.

### SENSEI — STRENGTHEN
Cross-institutional/nonpossessive role is explicitly articulated by Mutsuki. Sole choice is de-escalatory but nonbinding; students retain agency and investigative authorship.

### NONOMI — STRENGTHEN lightly
Notices the unexplained cash-only creditor practice and resists reducing Problem Solver 68's members to a bad-student reputation.

### SHIROKO — STRENGTHEN
Cash-truck callback preserves operational criminal imagination; institutional questioning targets startup authorization and organizational category.

### SERIKA — STRENGTHEN
Repayment ethic confronts a 309-year horizon; she refuses exact completion arithmetic while continuing to police practical financial/criminal boundaries inside the group.

### HOSHINO — STRENGTHEN
Prioritizes acute threat over chronic debt and converts uncertain Black Market overlap into a bounded investigative next step.

## Relationship ledger

- **Mutsuki ↔ Ayane:** active hostility + attempted social casualness + rejected `公私` partition.
- **Mutsuki ↔ Sensei:** direct casual access/invitation; Sensei framed as nonexclusive cross-school adult.
- **Abydos ↔ Problem Solver 68:** shifts from battle to mutual investigation/continued role conflict.
- **Abydos ↔ Kaiser Loan:** newly explicit creditor/debtor relation with monthly variable interest, cash-only payment, and 309-year schedule.

## Institution ledger

- Problem Solver 68: explicit Gehenna student-club affiliation now established; business/legal authorization remains partly inferred.
- Kaiser Loan: new named creditor institution.
- Black Market: new liminal institutional/economic zone connecting discontinued-goods circulation with unapproved student organizations.
- Abydos Countermeasures Committee: investigative capacity strengthened.

## Sensei ledger

Add E010 choice 001 as **de-escalatory preference / nonbinding relational agency**.

## Japanese-language ledger

Add:

- `公私` callback;
- `請け負ってる仕事`;
- `あんたたちだけのモンじゃない`;
- `変動金利`;
- `309年返済`;
- `2つの事案`;
- `非認可の部活`;
- `関連性を探す`.

## Motif ledger

Add:

- debt as recurring calendar/ritual;
- debt measured against human lifespan;
- cross-context friendliness under persistent role conflict;
- physical evidence becoming supply-chain evidence;
- Black Market as edge-of-school institutional space;
- anomaly without explanation: cash-only repayment.

---

# 14. Claim-revision transitions

## BA-C001 — STRENGTHEN lightly
Responsible adulthood remains service-oriented and nonexclusive. Sensei expresses a peace preference without claiming authority to force reconciliation.

## BA-C002 — STRENGTHEN
Sensei is increasingly socially legitimate across student groups, not just Abydos. Mutsuki directly treats Sensei as available beyond one school's claim.

## BA-C003 — STRENGTHEN strongly
Schale's cross-institutional character receives explicit student-side articulation: `シャーレの先生` is not Abydos property. Meanwhile Abydos itself conducts the investigation.

## BA-C004 — PRESERVE
No major new exceptional capability. E010 is stronger evidence about social/institutional role than technical power.

## BA-C005 — PRESERVE REJECTED; counterevidence strengthened
Sensei does not identify Problem Solver 68, solve the debt, analyze the weapon fragments, or locate the Black Market clue. Student investigation remains indispensable.

## BA-C006 — PRESERVE REJECTED; counterevidence strengthened
Abydos performs administration, debt servicing, attacker research, forensic analysis, hypothesis separation, and investigative planning.

## BA-C007 — STRENGTHEN
Sensei's service role remains low-possession and nonexclusive. The student institution owns its cases and next investigative move.

## BA-C008 — STRENGTHEN
The sole singleton choice expresses a conciliatory persona/ethical preference; Mutsuki refuses the desired outcome, confirming that choice does not imply route sovereignty.

## BA-C009 — PRESERVE
No major technical-system relational ontology delta.

## BA-C010 — STRENGTHEN strongly
The line `あんたたちだけのモンじゃない` makes nonpossessive authority explicit: closeness to Abydos does not become ownership of Sensei.

## BA-C011 — STRENGTHEN lightly
Sensei's preferred reconciliation fails; adult ethical preference is not infallible command. Student institutions continue to make autonomous decisions.

## BA-C012 — STRENGTHEN / REFINE
E010 moves the proxy architecture into investigation. Problem Solver 68 is now explicitly identified as a Gehenna club with reported Black Market activity, while the Helmet Gang's discontinued weapon independently points toward the Black Market. **The Black Market becomes a candidate intersection, not yet proof of common authorship.**

## BA-C013 — OPEN / NEW

> **Abydos's debt is an active institutional creditor relationship, not merely historical background: Kaiser Loan collects recurring variable-interest payments in cash under a stated 309-year repayment horizon that normal student earnings cannot presently overcome. The reason for cash-only collection, the full loan mechanics, and any relationship between Kaiser Loan and the hidden sponsor remain unresolved.**

This receives a new claim ID because it has a distinct semantic responsibility from BA-C012. BA-C012 concerns the political economy of coercion and proxy violence; BA-C013 concerns the institutional governance of debt/credit. E010 places them adjacent but does not authorize collapsing them into one system.

---

# 15. Open questions entering E011

1. What is the Black Market as an actual social and physical space beyond Ayane's briefing?
2. What forms of governance, policing, commerce, or territorial authority operate there?
3. Can the committee independently verify that the discontinued weapon passed through the Black Market?
4. Does Problem Solver 68's reported Black Market history produce a meaningful lead or merely shared geography?
5. Does the investigation reveal a principal above Problem Solver 68, or only additional intermediaries?
6. How does Sensei function in a high-risk investigative environment compared with prior combat-command scenes?
7. Do students outside standard academy status retain recognizable club/institutional identities?
8. Does the cash-only Kaiser Loan anomaly recur or remain unresolved background?
9. Is any link between Kaiser Loan and the hostile sponsor established by primary text? **Do not infer one from the shared `カイザー` label alone.**
10. Will the committee maintain the evidentiary discipline of `関連性を探す`, or will new evidence justify stronger causal claims?

---

# 16. Evidence locator index

All locators are within `BA:main:001:001:010:scene:001` unless stated otherwise.

| Topic | Locator | Raw source | Evidence |
|---|---|---|---|
| repayment-day administrative labor | `u:0004-0005` | `DataList[1680-1681]` | Ayane prepares interest payment and future-plan review |
| attacker research | `u:0006-0007` | `DataList[1682-1683]` | Ayane found information; attackers identified as Gehenna students |
| Mutsuki entrance | `u:0008` | `DataList[1685]` | direct casual greeting to Sensei |
| attribution anomaly | `u:0009`, `u:0012` | `DataList[1687]`, `[1692]` | lines mapped inconsistently to Mutsuki speaker ID; quarantined |
| no personal dislike | `u:0018` | `DataList[1698]` | Mutsuki denies hatred of Abydos students |
| commissioned club work / outside-work friendship | `u:0019` | `DataList[1699]` | Mutsuki's role-partition model |
| Ayane `公私` challenge | `u:0020` | `DataList[1700]` | rejects after-the-fact compartmentalization |
| Sensei not Abydos property | `u:0021` | `DataList[1701]` | `シャーレ` / `あんたたちだけのモンじゃない` |
| de-escalatory Sensei choice | `choice:001` | `DataList[1702]` | `ケンカしないで仲良くしてくれると嬉しいな。` |
| work prevents reconciliation | `u:0022` | `DataList[1703]` | Mutsuki cites contract and Aru motivation |
| invitation to Problem Solver 68 | `u:0023` | `DataList[1704]` | future social invitation to Sensei |
| exact interest | `u:0029` | `DataList[1712]` | `788万3250円` after variable interest etc. |
| cash-only completed payment | `u:0030` | `DataList[1713]` | all paid in cash |
| Kaiser Loan named | `u:0031` | `DataList[1714]` | creditor institution + monthly recurrence |
| 309-year schedule | `u:0037` | `DataList[1722]` | Ayane states repayment period |
| lifetime impossibility as perceived by Serika | `u:0038-0039` | `DataList[1723-1724]` | stress + `死ぬまで完済できない` |
| cash-only anomaly | `u:0041` | `DataList[1726]` | Nonomi questions cash-only collection / transport |
| Shiroko cash-truck callback | `u:0043-0046` | `DataList[1729-1732]` | Serika prohibits robbery and even planning |
| two-case framing | `u:0049-0050` | `DataList[1736-1737]` | Ayane explicitly structures `2つの事案` |
| Problem Solver 68 identification | `u:0051-0056` | `DataList[1739-1747]` | club/service model/Aru titles; follow promoted speaker mapping |
| business authorization uncertainty | `u:0060-0061` | `DataList[1753-1754]` | Shiroko question; Ayane hedged inference |
| reported delinquent reputation | `u:0062-0064` | `DataList[1755-1757]` | Nonomi counter-perception + Ayane report |
| possible capture/interrogation | `u:0065-0066` | `DataList[1758-1759]` | Hoshino/Ayane |
| Ayane grudge recognized | `u:0067-0068` | `DataList[1760-1761]` | Serika notices emotional intensity |
| discontinued weapon model | `u:0069-0072` | `DataList[1762-1765]` | forensic provenance → Black Market route |
| Black Market danger | `u:0073` | `DataList[1766]` | Nonomi reaction |
| Black Market population/institutions | `u:0074` | `DataList[1767]` | school-exit students + unapproved clubs |
| Problem Solver 68 Black Market history | `u:0075-0076` | `DataList[1768-1769]` | reported incidents |
| tentative linkage | `u:0077-0078` | `DataList[1770-1771]` | potential importance + `関連性を探す` |
| investigative decision | `u:0079-0080` | `DataList[1772-1773]` | Hoshino chooses Black Market investigation |
| next boundary | `u:0081` | `DataList[1775]` | `次回;ブラックマーケットへ（１）` |

---

# Conclusion

E010 is a transition episode in the strongest sense: it changes **how the characters know**.

The Abydos conflict has moved from visible violence to institutional provenance. The students ask who the attackers are, how weapons moved, what kinds of organizations exist outside normal school authorization, and where evidence streams might intersect. Crucially, they do not yet know the answer.

At the same time, the episode makes the debt system more concrete than ever. The school is not merely “in debt.” It has a named creditor, an exact monthly variable-interest collection, a cash-only procedure, a transport apparatus, and a 309-year repayment horizon. This deserves its own longitudinal claim because it is an enduring institutional relationship with a logic distinct from the proxy-violence chain.

The most important interpretive discipline after E010 is therefore **non-collapse**:

- do not collapse Kaiser Loan into the hidden sponsor;
- do not collapse Problem Solver 68 into the Helmet Gang's supplier;
- do not collapse Black Market co-location into common authorship;
- do not collapse Mutsuki's friendliness into peace;
- do not collapse Ayane's anger into bad investigation;
- do not collapse Sensei's relational centrality into exclusive possession or omniscience.

The episode itself models that restraint. Ayane has two cases, identifies a possible intersection, and goes looking for evidence.

The next sequential boundary is `BA:main:001:001:011`, 第11話「ブラックマーケットへ（１）」.
