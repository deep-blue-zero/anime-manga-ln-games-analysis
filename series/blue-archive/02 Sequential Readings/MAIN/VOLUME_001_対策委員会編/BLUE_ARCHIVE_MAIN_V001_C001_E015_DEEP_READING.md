---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E015
generation: V1
status: active_provisional
source_boundary: "Canonical Japanese main-story unit BA:main:001:001:015, 対策委員会編 第15話『行こう、夕日に向かって！』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-18
---

# BLUE ARCHIVE — MAIN V001 C001 E015 DEEP READING
## 対策委員会編 — 第15話「行こう、夕日に向かって！」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the seventeenth canonical main-story object in analytical order and the fifteenth object in `対策委員会編`:

- story ID: `BA:main:001:001:015`;
- analytical scope: `MAIN_V001_C001_E015`;
- source title: `第15話;行こう、夕日に向かって！`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第15話`;
- raw group ID: `11150`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- record count: **166**;
- promoted utterance count: **133**;
- normalized choice groups: **0**;
- canonical scene count: **1**;
- promoted person IDs: Aru, Ayane, Haruka, Hifumi (`BA_PERSON_HIHUMI` in the pinned corpus identifier), Hoshino, Kayoko, Mutsuki, Nonomi, Serika, and Shiroko;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_015.md`;
- complete source-side convenience rendering: `15話_行こう、夕日に向かって！.md`.

### Canonical scene structure

The promoted corpus encodes E015 as one canonical scene:

1. `BA:main:001:001:015:scene:001`
   - opening place marker: `市街地`;
   - principal text-bearing span: `ScenarioScriptMain1ExcelTable.json:DataList[2296]–[2459]`, with gaps for control/narration records;
   - contains the post-raid escape, discovery of the cash, the committee's argument over whether to keep it, Hoshino's refusal, Aru's admiration for the masked group, the accidental transfer of the cash bag to Problem Solver 68, and the final reveal to Aru that the `覆面水着団` was Abydos.

The source includes an embedded location transition to `便利屋オフィス` near the end, but the promoted scene layer preserves the entire unit as one canonical scene. This reading follows the promoted structure rather than inventing a second scene.

### Choice-space and Sensei presence

E015 contains **no normalized Sensei choice groups**, and the canonical scene chunk marks `sensei_present: false`.

This is analytically important for the ethics of the post-raid decision.

E013 gave Sensei a requested launch line, `銀行を襲うよ！`. E014 executed the raid without textual Sensei presence. E015 then stages the committee's most explicit moral argument so far—whether to convert the raid into material expropriation—again without Sensei.

Therefore:

- Sensei's E013 endorsement remains part of the causal and ethical background;
- E015's refusal to keep the cash is **not** an adult correction imposed on students;
- the committee generates, debates, and enforces its own limiting principle;
- Hoshino acts as chair, but Nonomi, Ayane, Serika, Shiroko, and Hifumi expose different moral intuitions around the same problem.

This sharply strengthens the rejection of any reading in which students require an adult to supply all moral judgment or institutional self-restraint.

### Source-integrity cautions

E015 is comparatively clean at the promoted person layer.

A few cautions remain:

1. The source-side convenience Markdown suppresses speaker labels on several lines that the promoted utterance layer identifies cleanly:
   - `できるだけ早く離れないと……` → Hifumi (`u:0004`);
   - `やった！大成功！` → Serika (`u:0014`);
   - `う、うん……バッグの中に。` → Shiroko (`u:0017`);
   - `ちょ、ちょっと待ってください！` → Ayane (`u:0025`);
   - `私はアビドスさんの事情をよく知りませんが……` → Hifumi (`u:0053`);
   - `あはは……良いことしたって思いましょう。` → Hifumi (`u:0120`).

   The promoted person mapping is used here because the stable utterance records provide unambiguous person IDs.

2. Hoshino estimates the cash as `軽く1億はある`. This is an in-scene estimate—roughly ¥100 million or more—not an audited amount. Do not transform it into a precise financial figure.

3. Serika says the cash is money Abydos earned and that it flowed into the shadow bank. This is **her assertion at the current information boundary**, not narrator-certified proof. The seized `集金記録` are confirmed to be in Shiroko's bag, but E015 never reads them.

4. Nonomi calls the money `犯罪者の資金`. Again, this expresses her current judgment; it does not independently prove ownership, provenance, or downstream use of the specific banknotes.

5. The cash bag was originally placed in Shiroko's possession through the bank employee's E014 misunderstanding. E015 explicitly states that Shiroko did not intentionally take the money. The later accidental abandonment of the bag creates a transfer to Problem Solver 68, but E015 does not yet establish what Problem Solver 68 ultimately does with it.

6. Haruka's `もう食事抜かなくてもいいんですか？` is clean textual evidence that Problem Solver 68's financial distress has included skipped meals. It should not be inflated into a quantified chronic-malnutrition claim.

No major E015 finding requires repairing a corrupted speaker attribution.

### Local-information lock

Available prior analytical authority is limited to:

- the canonical two-unit Prologue and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md` through `E014_DEEP_READING.md`;
- the seven longitudinal ledgers through E014.

No E016 or later main-story unit, Kaiser institutional package, Black Market side source, Problem Solver 68 event/group/bond material, Hifumi bond/MomoTalk material, adaptation, wiki, or franchise hindsight is used to determine:

- the actual contents of the seized `集金記録`;
- whether those records prove Abydos's interest payments entered criminal circulation;
- whether Kaiser Loan owns, controls, or merely transacts with the shadow bank;
- whether Kaiser Loan and Kaiser PMC share command, ownership, or anti-Abydos purpose;
- whether the abandoned cash is ultimately kept, returned, spent, or seized by Problem Solver 68;
- whether the cash changes Problem Solver 68's relationship with its client;
- whether Aru's discovery that the masked group was Abydos changes her later conduct;
- whether `覆面水着団` becomes a durable public identity;
- whether Hoshino's ethical rule survives later, more severe desperation.

---

# 1. Story placement and local chronology

E014 ended with a precise unresolved distinction:

> **Abydos acquired the targeted collection records, but acquisition was not yet interpretation.**

The committee had also exited the shadow bank under Market Guard pursuit. It had used planned armed coercion, disabled the external alarm/reporting system, and obtained the object Shiroko called the `集金記録`. The operation was therefore materially successful, ethically compromised, and epistemically incomplete.

E015 begins immediately in flight.

The students are still masked. They expect road closures. Ayane tracks their escape remotely. The first explicit objective check is not money:

> `シロコちゃん、集金記録の書類はちゃんと持ってるよね？`

Shiroko confirms:

> `う、うん……バッグの中に。`

Only then do they discover that the bag also contains a large quantity of cash.

The episode's movement is:

> **escape from the raid → confirm the documentary objective → discover roughly ¥100 million accidentally included in the bag → debate whether material desperation justifies keeping it → Hoshino refuses on habituation and institutional-identity grounds → the committee retains only the documents → Aru approaches and idealizes the masked raiders as authentic outlaws → Abydos improvises an increasingly absurd `覆面水着団` mythology → the abandoned cash bag is accidentally left behind → Problem Solver 68 finds it → Haruka reveals the depth of their food insecurity → Aru later learns that her admired outlaw group was Abydos.**

This means E015 does **not** perform the expected next investigative step.

It does not read the documents.

Instead, the narrative pauses the Kaiser investigation to ask a more basic question:

> **What kind of institution does Abydos want to remain while trying to survive?**

That question is not abstract. It is tested with enough money to relieve an enormous portion of the committee's immediate pressure.

---

# 2. Narrative reconstruction

The masked group is fleeing the Black Market.

Serika complains that the mask makes breathing difficult and wants to remove it. Hoshino tells everyone to keep moving because pursuers will arrive quickly. Hifumi predicts that roads will soon be sealed. Nonomi says preparations are complete. Shiroko leads them toward the planned route.

Even in retreat, the mask gag continues. Serika asks why Shiroko still has hers on. Hoshino jokes that Shiroko may have found her calling and incorporated the mask into her soul. Serika concludes that Shiroko was fortunate to end up at Abydos, because at another school she might have caused something even more extraordinary.

The comedy is also character diagnosis.

The raid was not merely something Shiroko endured. She appears unusually at home in the operational identity.

Ayane reports that they have broken through the blockade point and are safe for the moment. Serika celebrates. Ayane exhales at the reality of what they have done:

> `本当にブラックマーケットの闇銀行を襲っちゃうなんて……ふう……。`

Hoshino immediately checks the mission objective.

Shiroko still has the `集金記録`.

The bag opens.

It contains bundles of cash.

Serika initially assumes Shiroko stole it. Shiroko rejects that accusation: the documents are there, but the bank employee put the money in the bag through the misunderstanding established in E014.

Hoshino estimates that the bag contains at least roughly ¥100 million.

This creates a temptation that is proportionate to Abydos's desperation.

Serika's first response is ecstatic practicality: take it and use it.

Ayane stops her.

If they use the money, Ayane says, then they will really have committed a crime.

Serika rejects the relevance of that distinction. Her reasoning combines restitution and consequentialism:

- Abydos earned the money through labor;
- the money was then sent into the shadow bank;
- if left there, it might become weapons or military equipment for criminals;
- therefore taking money from bad people seems morally permissible;
- and the money can reduce the school's debt.

At the current evidence boundary, the first premise is stronger psychologically than evidentially. Serika knows Abydos paid Kaiser Loan in cash and saw the same collection apparatus enter the shadow bank, but the seized records have not yet been read. She treats the suspected cash-flow connection as settled.

Nonomi sides with Serika.

She calls the money criminal funds and argues that Abydos can put it to better use.

Hoshino does not immediately pronounce judgment.

She asks Shiroko what she thinks.

Shiroko answers in a revealingly indirect way:

> `……自分の意見を述べるまでもない、ホシノ先輩が反対するだろうから。`

She says there is little need to state her own view because Hoshino will oppose the idea.

The line does two things at once.

It establishes that Shiroko knows Hoshino's normative boundary well enough to predict it, but it does **not** tell us whether Shiroko independently shares the boundary. Her later obedience is clear; her private normative agreement remains less certain.

Hoshino confirms the prediction.

> `私たちに必要なのは書類だけ。お金じゃない。`

The committee needs the documents, not the money.

Hoshino's next argument is the ethical center of E015.

She does not deny that the bank is bad.

She does not claim that lawfulness always overrides necessity.

She does not even spend most of the argument discussing who legally owns the banknotes.

Instead she asks what happens **next time**.

Even if they grant that this particular money belongs to bad actors, what do they do after they become accustomed to solving problems this way?

> `こんな方法に慣れちゃうと……`
>
> `ゆくゆくは、きっと平気で同じことをするようになるよ。`

Then, in a future crisis, they will tell themselves:

> `仕方ないよね`

—and reach for something they know they should not do.

Hoshino frames the danger as habituation.

Exceptional wrongdoing can become normal decision procedure.

The concern is also explicitly pedagogical:

> `このおじさんとしては、カワイイ後輩がそうなっちゃうのはイヤだなー。`

The joking `おじさん` persona masks a chairperson's protective responsibility toward younger students.

Then Hoshino gives the decisive proposition:

> `そうやって学校を守ったって、何の意味があるのさ。`

Survival is not self-justifying.

If the means used to preserve Abydos corrupt the kind of institution the committee is trying to preserve, mere continued existence loses its meaning.

Hoshino links this to an earlier unresolved financial option.

If they were willing to preserve the school by any available means, they could simply have used Nonomi's shining gold card.

Nonomi confirms that she had proposed exactly that and Hoshino refused.

Nonomi then articulates the principle more explicitly than Hoshino does:

> `いくら頑張ったって、きちんとした方法で返済をしない限り、アビドスはアビドスじゃなくなってしまう……。`

Unless the debt is repaid through a proper method, Abydos will cease to be Abydos.

Hoshino agrees.

The issue is therefore not asceticism for its own sake.

The committee's chosen method of survival is constitutive of institutional identity.

Hoshino orders that the cash be left behind and only the necessary documents retained:

> `これは委員長としての命令だよー。`

Serika protests bitterly.

Shiroko obeys because it is the chairperson's order.

Hifumi, speaking as an outsider who admits she does not know Abydos's circumstances well, adds a prudential argument: carrying the money could bring further trouble. It is a `災いの種`.

Nonomi accepts the decision and volunteers to dispose of the bag.

Before that can be resolved neatly, Ayane detects someone approaching.

It is Aru.

The masked students immediately switch back into threat assessment. Shiroko asks whether they should repel her. Hoshino refuses immediate violence because Aru is not showing hostile intent:

> `戦う気がないって相手を叩くのもねえ`

This is a small but important limiting principle after E014. The committee's willingness to use force is not generalized into permission to attack any inconvenient observer.

Aru approaches not as an enemy but as an admirer.

She watched the bank raid.

To her, the five-minute operation was a revelation of authentic outlawhood. It demonstrated the kind of fearless conduct she wishes she could perform.

Aru restates her aspiration:

> `法律や規律に縛られない、本当の意味での自由な魂！`

She wants to become an outlaw with a truly free soul, not bound by law or rules.

She asks for the group's name so she can remember their achievement.

Abydos could simply correct her misunderstanding.

Instead Nonomi embraces the role.

They are the `覆面水着団`.

Aru is delighted.

Hoshino adds that their proper uniform is actually a school swimsuit plus mask. Nonomi invents an idol-by-day, righteous-phantom-thief-by-night backstory and reintroduces herself as `クリスティーナだお♧`. Hoshino supplies an absurd motto:

> `目には目を、歯には歯を。無慈悲に、孤高に、我が道の如く魔境を行く。`

Aru treats every additional layer of nonsense as proof of authenticity.

Kayoko watches in disbelief.

Mutsuki compares Aru's expression to a child brought to a tokusatsu event.

Nonomi eventually signals that they should escape before the performance becomes harder to sustain.

Hoshino shouts the episode title:

> `行こう！夕日に向かって！`

Hifumi deadpans:

> `夕日、まだですけど……。`

The joke encapsulates the entire identity-performance theme.

Aru wants authentic outlawhood.

Abydos is knowingly performing a fake myth of outlawhood.

Yet the actual raid that generated the myth was real.

After the masked group leaves, Aru vows to engrave Hoshino's invented motto onto her soul.

Mutsuki knows the truth and decides not to tell Aru immediately because watching the misunderstanding is amusing.

Haruka then notices the abandoned bag.

Aru briefly imagines that the `覆面水着団` left it for her. Kayoko immediately rejects the fantasy as unlikely. They open the bag and discover the cash.

The scene cuts back to Abydos realizing Nonomi left it behind.

Hoshino is unconcerned: they were going to dispose of it anyway.

Shiroko imagines that somebody will pick it up.

Nonomi hopes it will go to someone who needs money.

Hifumi reframes the mistake as accidental charity: perhaps a hungry person can eat because of it.

Serika alone remains agonized by the wasted opportunity and calls the others excessively kind.

The story then returns to Problem Solver 68.

Their shock at the cash is followed by one of the episode's least comic and most materially important lines.

Haruka asks:

> `……もしかしてこれで、もう食事抜かなくてもいいんですか？`

Problem Solver 68's financial precarity has reached the level of skipped meals.

The money that Abydos refuses because it would corrupt the meaning of its survival falls, by accident, into the hands of another financially desperate student organization.

The episode does not show what Problem Solver 68 does with it.

Finally, at the Problem Solver office, Aru learns that the `覆面水着団` was Abydos.

Her response is a full comic collapse:

> `覆面水着団がアビドスだったですってええ！！？？`

Mutsuki laughs.

Kayoko sighs.

The source notes that they eventually told her.

E015 ends with the next-episode marker:

> `次回;明かされる真実`

The documents still have not been read.

---

# 3. Central thesis

E015's central thesis is:

> **Abydos defines survival as a normative project rather than bare institutional persistence. The committee is willing to use extraordinary and even coercive means to obtain evidence from a criminalized parallel institution, but Hoshino refuses to convert that operation into opportunistic enrichment. Her reason is not simple legalism: repeated expedient wrongdoing would habituate the students to violating their own limits whenever a crisis made it feel necessary. Nonomi makes the institutional consequence explicit—if Abydos repays its debt by means incompatible with the kind of school it is trying to preserve, then “Abydos” survives only nominally.**

This is the clearest statement so far that **means can constitute identity**.

A second thesis concerns distributed student ethics:

> **E015 shows that the students themselves, without Sensei present, possess conflicting but serious moral frameworks and can generate institutional self-restraint. Ayane draws a procedural line around expropriation; Serika argues from restitution and desperation; Nonomi initially argues consequentially but recognizes Hoshino's identity principle; Hifumi warns about downstream risk; Shiroko anticipates and obeys committee authority; Hoshino converts the dispute into a rule about what sort of people and institution they are becoming.**

The third thesis concerns the distinction between **lawlessness and self-governance**:

> **The Countermeasures Committee is not simply becoming “lawless.” It has shown willingness to violate external legal norms while simultaneously maintaining internal restraints concerning purpose, target, possession, and escalation. Those internal restraints are ethically contestable and do not retroactively justify the bank raid, but they are real.**

The fourth thesis concerns Aru:

> **Aru's ideal of freedom from law and rules is now juxtaposed directly with Abydos's self-imposed limits. She admires the masked group precisely because she sees only the visible audacity of the raid, not the internal debate that follows it. The irony is that the “true outlaws” she idealizes are, at the moment she praises them, choosing not to behave as unbounded outlaws.**

The fifth thesis concerns the Kaiser investigation:

> **E015 deliberately withholds epistemic payoff. Possession of the `集金記録` is reconfirmed, but the records are not opened. Serika and Nonomi speak as if the shadow-bank cash's criminal provenance is established; the analysis must not follow them across that evidentiary gap. BA-C013 remains unresolved.**

---

# 4. Scene-by-scene close reading

## 4.1 Escape discipline: the raid continues after the bank doors

E015 opens by refusing to treat escape as an afterthought.

Hoshino expects pursuit.

Hifumi expects road closures.

Nonomi claims preparations are complete.

Ayane tracks the route and confirms when the blockade point has been passed.

This preserves E014's picture of the raid as planned operation rather than impulsive chaos.

The students' competence therefore extends across:

> entry → alarm isolation → objective acquisition → withdrawal → route management → blockade escape.

The comedy of masks sits on top of genuine tactical sequencing.

## 4.2 Shiroko's mask: transgression as surprisingly comfortable identity

Serika asks why Shiroko still wears the mask after escape.

Hoshino jokes that it may have become part of Shiroko's soul.

Serika's response matters:

> `シロコ先輩はアビドスに来て正解だわ……`
>
> `他の学校だったら、ものすごい事をやらかしてたかも……。`

The joke retrospectively characterizes Abydos as both social home and containment structure.

Shiroko's extreme operational imagination exists inside a group whose other members can redirect, limit, or contextualize it.

E015 later demonstrates exactly that structure when Hoshino rejects the money and rejects attacking non-hostile Aru.

Thus “Abydos was the right school for Shiroko” can be read not only as belonging but as **institutional channeling of disposition**.

## 4.3 Objective-first accounting: the records are checked before the cash is discovered

Hoshino's first material question after escape is:

> `集金記録の書類はちゃんと持ってるよね？`

This matters because E014 left open whether the raid's stated evidentiary purpose would remain operationally dominant after success.

E015 confirms that it does.

The group checks the documents first.

The cash is accidental surplus.

That distinction does not make the raid lawful or harmless, but it materially weakens a reading in which the evidence rationale was merely pretext for robbery.

## 4.4 The ¥100 million temptation is narratively calibrated to Abydos's desperation

Hoshino estimates:

> `軽く1億はあるね`

This is not petty cash.

At E010's exact monthly interest collection of ¥7,883,250, even roughly ¥100 million represents more than twelve such monthly-interest payments.

The episode therefore creates a genuine temptation rather than a symbolic one.

Serika's response is understandable because the amount is large enough to matter materially.

The scene asks what a moral rule is worth when breaking it would actually help.

## 4.5 Ayane draws a line inside an already extralegal operation

Ayane says:

> `そんなことしたら……本当に犯罪だよ、セリカちゃん！！`

The word `本当に` is striking after the committee has literally just robbed a shadow bank at gunpoint.

It should not be flattened into logical inconsistency.

Ayane's line reveals a distinction in her own moral categorization:

- the bank operation was reluctantly accepted as a means to acquire inaccessible evidence against suspected predatory/criminal finance;
- taking the bank's money for Abydos's benefit would transform the operation into straightforward self-enrichment.

Whether that distinction would satisfy an external legal system is separate.

Within Ayane's reasoning, **purpose changes the moral category**.

## 4.6 Serika's restitution argument exceeds the evidence currently available

Serika says:

> `このお金はそもそも、私たちが汗水流して稼いだお金なんだよ！`
>
> `それがあの闇銀行に流れてったんだよ！`

Emotionally, the line follows years of labor under crushing interest payments.

Epistemically, it overstates the case.

At this boundary, Abydos knows:

- it paid Kaiser Loan in cash;
- the same Kaiser Loan collection apparatus entered the shadow bank;
- cash was delivered there;
- collection records exist and are now in Shiroko's possession.

It does **not** yet know:

- that the banknotes in Shiroko's bag include Abydos's payment;
- that all or most Kaiser Loan collections are criminal proceeds;
- that Abydos's payments financed weapons;
- that the shadow bank is owned by Kaiser;
- that Kaiser Loan and Kaiser PMC are one anti-Abydos structure.

Serika's argument is therefore a **RELATIONAL/ETHICAL INFERENCE built on an OPEN financial-provenance hypothesis**, not a TEXTUAL FACT about the money.

## 4.7 `悪人のお金を盗んで、何が悪いの！？`: retributive moral compression

Serika then asks:

> `悪人のお金を盗んで、何が悪いの！？`

This continues the E013 pattern:

> `私らは悪くないし！悪いのはあっち！`

Under pressure, Serika compresses complex institutional ethics into a moral binary.

The bank is bad.

Abydos has been harmed.

Therefore taking from the bank feels reparative rather than predatory.

That reasoning is psychologically coherent without becoming narrator-endorsed ethical truth.

## 4.8 Nonomi initially takes the consequentialist side

Nonomi says:

> `犯罪者の資金ですし、私たちが正しい使い方をした方がいいと思います。`

Her reasoning is initially outcome-oriented.

If the money belongs to criminals, and Abydos can use it correctly, then transferring control appears beneficial.

This is important because Nonomi later becomes the character who most clearly verbalizes Hoshino's anti-corruption principle.

Her arc inside the conversation is therefore not “Nonomi already agrees.”

It is:

> consequentialist temptation → recognition of Hoshino's deeper rule → acceptance.

## 4.9 Shiroko knows Hoshino's answer before Hoshino gives it

Shiroko says:

> `自分の意見を述べるまでもない、ホシノ先輩が反対するだろうから。`

This is high-value relationship evidence.

Shiroko understands Hoshino's normative tendencies well enough to forecast the decision.

The line should not be overread into full agreement.

But it establishes that Hoshino's refusal is not experienced as an arbitrary surprise by the member whose transgressive imagination has been most consistently foregrounded.

Hoshino's rule is legible within the group.

## 4.10 `私たちに必要なのは書類だけ。お金じゃない。`: purpose limitation

Hoshino's first principle is objective limitation.

> `私たちに必要なのは書類だけ。お金じゃない。`

The raid was authorized internally for a specific purpose.

The appearance of additional opportunity does not automatically expand that mandate.

This is a meaningful form of self-restraint after E014's coercion.

It resembles a **purpose limitation** norm:

> use extraordinary means for the claimed extraordinary objective; do not silently convert access into general permission.

## 4.11 Hoshino's real argument is habituation, not legality

The core sequence is:

> `今回のは悪人の犯罪資金だからいいとして、次はどうする？その次は？`
>
> `こんな方法に慣れちゃうと……`
>
> `ゆくゆくは、きっと平気で同じことをするようになるよ。`

Hoshino concedes the strongest version of Serika's case for argument.

Suppose this particular money really is criminal money.

Even then, what does repeating the method do to the committee?

This is a virtue-ethical and institutional argument.

Actions form habits.

Habits form decision rules.

Decision rules form people and organizations.

## 4.12 `仕方ないよね`: emergency language as future self-authorization

Hoshino predicts that the next crisis will produce:

> `仕方ないよね`

The phrase matters because it names a mechanism of moral erosion.

The danger is not that the students will suddenly become malicious.

The danger is that they will continue to experience themselves as good while expanding the category of “necessary exception.”

This is a sophisticated concern about **self-exculpating necessity**.

The committee could normalize transgression without ever deciding to become evil.

## 4.13 Hoshino's `カワイイ後輩`: governance as moral guardianship

Hoshino says:

> `カワイイ後輩がそうなっちゃうのはイヤだなー`

Her chairperson role is not limited to strategy or debt management.

She treats leadership as responsibility for what kind of people her juniors become.

The `おじさん` register makes the statement playful, but the content is serious.

This is one of the strongest pieces of evidence so far for Hoshino's protective seniority as a governing function.

## 4.14 `そうやって学校を守ったって、何の意味があるのさ`: survival can defeat itself

This is the episode's most important line.

> `そうやって学校を守ったって、何の意味があるのさ。`

Abydos's goal is not merely to keep a legal entity operating.

The school matters because it embodies relationships, commitments, memory, and a chosen way of acting.

If the method of preservation destroys those things, “saving the school” becomes semantically hollow.

This is **institutional telos** rather than simple debt repayment.

## 4.15 The gold card callback proves the rule predates the robbery

Hoshino says that if they were willing to use such methods, they could have relied on Nonomi's gold card from the beginning.

Nonomi confirms she proposed it.

This is crucial because it prevents E015's ethics from looking improvised after the fact.

Hoshino had already rejected a far less coercive shortcut.

The principle is therefore broader than “do not steal.”

It is about preserving Abydos through a form of collective effort that remains recognizably its own.

## 4.16 `アビドスはアビドスじゃなくなってしまう`: identity through procedure

Nonomi articulates the institutional thesis explicitly:

> `きちんとした方法で返済をしない限り、アビドスはアビドスじゃなくなってしまう`

Abydos is not defined only by:

- buildings;
- legal registration;
- debt balance;
- remaining students;
- continued institutional existence.

It is also defined by **how** those students keep faith with it.

This warrants a new longitudinal claim because it is semantically distinct from prior claims about adult authority, Schale, or extra-federal institutions.

## 4.17 `委員長としての命令`: ethics becomes institutional decision

Hoshino does not leave the debate at persuasion.

She says:

> `これは委員長としての命令だよー。`

The cash will be left.

Only the documents will be taken.

This is an exercise of actual committee authority.

The decision becomes institutional rather than merely personal.

Shiroko's response:

> `委員長としての命令なら`

shows the hierarchy functioning even where private opinions are not fully verbalized.

## 4.18 Hifumi's `災いの種`: outsider prudence rather than moral absolutism

Hifumi does not claim authority over Abydos's internal values.

She begins:

> `私はアビドスさんの事情をよく知りませんが……`

This epistemic modesty is characteristic.

Her argument is prudential:

> the cash may draw them into further trouble.

She calls it:

> `災いの種`

The phrasing frames money not as salvation but as a seed of future disaster.

It independently converges with Hoshino's concern about downstream consequences.

## 4.19 Hoshino refuses unnecessary violence against Aru

When Aru approaches, Shiroko asks:

> `撃退する？`

Hoshino answers:

> `戦う気がないって相手を叩くのもねえ`

This is important counterevidence against interpreting E014 as evidence that Hoshino has embraced generalized coercion.

She authorized violence against a specific target in a specific operation.

She rejects attacking a non-hostile person merely because that person appears during escape.

The distinction does not retroactively settle the proportionality of the bank raid, but it establishes **target discrimination** as a real internal norm.

## 4.20 Aru sees only the visible half of Abydos's ethics

Aru saw:

- a five-minute bank takeover;
- successful withdrawal;
- audacity against the Black Market;
- apparent freedom from rules.

She did **not** see:

- the debate over the cash;
- Hoshino's refusal;
- the distinction between records and money;
- the concern about habituation;
- the committee's self-imposed boundary.

Therefore her praise is dramatically ironic.

She calls them authentic outlaws at exactly the point when they are proving that they do not understand themselves as unbounded outlaws.

## 4.21 `法律や規律に縛られない、本当の意味での自由な魂`: Aru's freedom ideal sharpens

Aru defines authentic outlawhood as:

> `法律や規律に縛られない、本当の意味での自由な魂！`

This deepens E014's:

> `何事にも恐れず`
>
> `何事にも縛られない`

Aru's ideal is not primarily cruelty.

It is freedom from constraint.

That makes the contrast with Hoshino sharper.

Hoshino accepts external transgression but insists on internal constraint.

Aru dreams of a self that is constrained by nothing.

Yet Aru's actual behavior repeatedly reveals conscience, fear, obligation, and economic dependence.

## 4.22 The `覆面水着団` mythology becomes collaborative improvisation

Nonomi names the group.

Hoshino invents a uniform rule.

Nonomi invents an idol/phantom-thief double life.

Hoshino invents a motto.

Aru treats every fabricated detail as authenticity.

This is not trivial filler.

It shows how **identity can be socially manufactured through performance**.

The false identity gains power because an observer wants it to be true.

## 4.23 `正義の怪盗`: the joke accidentally approximates Abydos's self-understanding

Nonomi claims they are righteous phantom thieves who defeat bad people.

The story treats the line as improvised nonsense.

But it also approximates the committee's self-justification:

- target bad institutions;
- seize only what the mission requires;
- reject enrichment;
- regard the action as serving a defensive or corrective end.

The fiction is ridiculous, but it is not entirely unrelated to how Abydos narrates its own conduct.

## 4.24 `夕日、まだですけど`: theatrical timing versus reality

Hoshino shouts:

> `行こう！夕日に向かって！`

Hifumi replies:

> `夕日、まだですけど……。`

The line punctures heroic staging.

Abydos is performing the exit that fits the myth rather than the actual time of day.

This reproduces the episode's larger structure:

> heroic/outlaw image ↔ ordinary material reality.

Aru wants the image.

Hifumi keeps noticing the reality.

## 4.25 Mutsuki controls information for amusement

Mutsuki knows Aru is admiring Abydos.

She thinks:

> `事実を伝えるべきなんだろうけど……いつ言おうか？`
>
> `面白いからしばらく放置で`

This extends her established social-perceptive/playful role.

She does not merely detect Aru's performance.

She actively manages information to prolong the comedy.

The eventual disclosure is delayed, not absent.

## 4.26 The cash transfer is accidental, not philanthropic intent

Nonomi leaves the bag behind.

Abydos later discovers the mistake.

Hoshino says it is fine because they meant to discard the money anyway.

Shiroko hopes somebody will find it.

Nonomi hopes someone in need will benefit.

Hifumi reframes it as feeding a hungry person.

This is charitable reinterpretation after the fact, not an intentional donation plan.

The distinction matters because the recipient is Problem Solver 68.

Abydos did not knowingly choose to finance them.

## 4.27 Haruka's skipped meals convert PS68 poverty from comic bookkeeping into bodily deprivation

Haruka asks:

> `もう食事抜かなくてもいいんですか？`

This is a major material delta.

E012–E014 established:

- exhausted operating funds;
- difficulty financing mercenaries;
- office rent pressure;
- failed bank credit;
- unstable business income.

E015 adds direct bodily consequence.

At least some member(s) of Problem Solver 68 have been skipping meals because of the group's financial condition.

The line deepens the stakes beneath Aru's theatrical company identity.

## 4.28 The episode's final joke destroys Aru's clean distinction between ideal and rival

Aru eventually learns:

> `覆面水着団がアビドスだった`

The people she regarded as authentic outlaws were the same students she has fought, eaten with, and been hired to oppose.

At the local boundary, the episode gives us shock but not yet integration.

We do not know whether Aru:

- revises her evaluation of Abydos;
- revises her idea of outlawhood;
- becomes embarrassed;
- becomes more hostile;
- admires them more;
- changes how she treats her current contract.

E016 must test the consequence.

---

# 5. Character-state analysis

## 5.1 Hoshino — institutional survival has a moral content

### TEXTUAL FACT

Hoshino:

- prioritizes the seized `集金記録`;
- refuses to keep the roughly ¥100 million;
- frames repeated use of such methods as habituation;
- predicts future self-justification through `仕方ないよね`;
- says preserving the school that way would be meaningless;
- links the rule to her earlier refusal to rely on Nonomi's gold card;
- issues the decision as `委員長`;
- refuses to attack non-hostile Aru.

### CHARACTER INFERENCE

E015 is one of the strongest Hoshino episodes so far.

Her leadership combines:

- strategic pragmatism;
- willingness to authorize coercive action;
- internal limiting principles;
- concern about character formation;
- protection of juniors;
- institutional identity;
- target discrimination.

The important point is that she is **not a procedural legalist**.

She has just led an armed bank raid.

Her ethics are closer to:

> exceptional action may be necessary, but necessity must remain purpose-limited, and repeated exceptions can corrupt both people and institution.

That makes her more morally complex than either “laid-back delinquent leader” or “secretly the responsible one.”

### OPEN

- Why Hoshino places such value on preserving Abydos's identity remains only partly explained.
- Whether this anti-habituation rule survives a more severe existential crisis is unknown.
- Whether she sees the bank raid itself as morally regrettable, justified, or merely necessary remains underdefined.

## 5.2 Shiroko — action reflex constrained by trusted hierarchy

### TEXTUAL FACT

Shiroko:

- retains the mask;
- confirms the records are secure;
- denies intentionally stealing cash;
- does not state her own cash position because she predicts Hoshino will oppose keeping it;
- obeys the chairperson's order;
- suggests repelling Aru before Hoshino notes Aru is non-hostile;
- accepts the accidental loss of the money.

### CHARACTER INFERENCE

Shiroko remains the committee member most naturally oriented toward direct operational action.

But E015 shows an important counterweight:

> she operates inside a relationship of trust and hierarchy.

Hoshino's decision is predictable to her.

The chair's order is sufficient to terminate the money question.

This supports the earlier suggestion that Abydos does not suppress Shiroko's transgressive imagination; it **channels** it.

### OPEN

Her private view on keeping the cash is not expressed.

Do not infer agreement merely from obedience.

## 5.3 Serika — desperation, restitution, and moral overclaiming

### TEXTUAL FACT

Serika:

- wants to use the cash to reduce Abydos's debt;
- describes it as money Abydos earned through labor;
- says it flowed to the shadow bank;
- argues it might otherwise become criminal weapons;
- asks what is wrong with stealing from bad people;
- bitterly protests Hoshino's refusal;
- ultimately remains with the group's decision.

### CHARACTER INFERENCE

Serika's position is materially grounded in lived deprivation.

Her labor, financial vigilance, and years of debt pressure make the idea of leaving ¥100 million almost intolerable.

Her weakness under pressure is **moral compression**:

> harmed self + bad opponent + useful resource → reparative entitlement.

This is not greed in a simple sense.

The desired use is institutional debt repayment, not luxury.

But E015 again shows that her certainty can outrun the evidence.

## 5.4 Ayane — evidence discipline becomes property/means discipline

### TEXTUAL FACT

Ayane:

- coordinates escape;
- confirms blockade passage;
- reacts to the reality of the raid;
- immediately objects to using the money;
- calls doing so `本当に犯罪`;
- identifies Aru as the approaching non-hostile person.

### CHARACTER INFERENCE

E013 established Ayane as the strongest evidence-threshold voice.

E015 extends that procedural disposition into moral categorization.

She tolerates the evidence raid reluctantly but distinguishes it from taking money for self-benefit.

Her reasoning is not fully theorized, but her stable function is clear:

> Ayane creates stopping points against escalation.

## 5.5 Nonomi — consequentialist temptation yields to institutional loyalty

### TEXTUAL FACT

Nonomi:

- initially agrees with Serika;
- calls the cash criminal funds;
- argues Abydos can use it correctly;
- confirms she previously proposed using her own gold card;
- explains Hoshino's refusal in terms of Abydos ceasing to be Abydos;
- accepts the decision;
- invents most of the `覆面水着団` mythology;
- accidentally leaves the cash behind;
- hopes someone in need receives it.

### CHARACTER INFERENCE

Nonomi is generous in more than one moral register.

She is willing to use personal wealth.

She is willing to redirect criminal wealth.

She is willing to reframe accidental loss as benefit to an unknown needy person.

But she also recognizes that Hoshino's principle is not simple pride.

The school's mode of survival matters.

This gives Nonomi greater ethical flexibility than a one-note “kind rich girl” model.

## 5.6 Hifumi — outsider moderation, epistemic modesty, and reality checks

### TEXTUAL FACT

Hifumi:

- predicts roadblocks;
- says she does not know Abydos's circumstances well;
- warns the cash could be a `災いの種`;
- asks whether Aru is an acquaintance;
- corrects Hoshino that there is no sunset yet;
- reframes the lost money as potentially feeding a hungry person.

### CHARACTER INFERENCE

Hifumi remains useful because she is not fully absorbed into Abydos's internal moral logic.

Her repeated mode is:

> acknowledge limits of knowledge → identify practical risk → reduce harm → puncture theatrical excess.

Her “sunset” correction is comic, but structurally continuous with her broader role.

## 5.7 Aru — freedom ideal meets the people she already knows

### TEXTUAL FACT

Aru:

- praises the five-minute bank raid;
- calls the masked group unusually outlaw-like;
- says she wants a free soul unbound by law and rules;
- asks for the group's name;
- treats increasingly absurd invented lore as cool;
- internalizes Hoshino's fake motto;
- later discovers the group was Abydos and reacts with extreme shock.

### CHARACTER INFERENCE

E015 deepens Aru's aspirational identity rather than merely repeating it.

Her ideal of outlawhood is fundamentally about **freedom from constraint**.

The dramatic irony is that she admires Abydos without seeing their self-restraint.

She mistakes purpose-limited transgression for unbounded freedom.

At the end, that fantasy collides with personal recognition.

The “true outlaws” are not remote icons. They are people she knows.

### OPEN

The effect of that revelation belongs to E016 or later.

## 5.8 Mutsuki — information asymmetry as play

Mutsuki recognizes the comedy and deliberately prolongs it.

Her:

> `面白いからしばらく放置で`

is consistent with her established tendency to understand Aru's self-performance and manipulate the social situation for amusement.

This is not evidence that she is indifferent to all consequences; the stakes here are embarrassment, not mortal danger.

## 5.9 Kayoko — reality remains her default register

Kayoko's most characteristic E015 moment is:

> `いや、それはないわ……ただの忘れ物じゃない？`

when Aru imagines the bag was left as a gift.

She refuses romanticized interpretation when ordinary explanation suffices.

This extends the reality-check function established in E014.

## 5.10 Haruka — loyalty now sits beside explicit material deprivation

Haruka contributes relatively little to the masked-group comedy, but her final line is major:

> `もう食事抜かなくてもいいんですか？`

Her self-effacing loyalty and readiness to work/attack now sit inside a more concrete deprivation context.

This may help explain why PS68's precarious company structure matters to its members beyond Aru's vanity.

Do not infer the causal origin of Haruka's personality from poverty alone.

## 5.11 Sensei — absence makes student ethics analytically visible

Sensei has:

- no presence;
- no choices;
- no dialogue.

This matters.

E015 gives the strongest explicit moral-limit argument of the Abydos arc so far without adult intervention.

Sensei's E013 endorsement remains relevant to the existence of the raid.

But the post-raid restraint is student-authored.

That strengthens the distinction between:

> adult responsibility as a major Blue Archive axis\
> **and**\
> adult monopoly on ethical agency, which the text continues to reject.

---

# 6. Relationship-state analysis

## 6.1 Hoshino ↔ Shiroko — predictable authority and trusted constraint

Shiroko predicts Hoshino's answer before she gives it.

That is stronger than generic obedience.

It implies accumulated knowledge of Hoshino's values.

Hoshino, in turn, asks Shiroko for an opinion before issuing the decision.

The relationship combines:

- recognition of Shiroko's agency;
- awareness of her action-oriented disposition;
- trusted chair authority;
- willingness to impose a boundary.

## 6.2 Hoshino ↔ Serika — moral disagreement inside legitimate hierarchy

Serika strongly disagrees with Hoshino.

She does not quietly assent.

Yet the argument remains internal to a functioning committee.

Hoshino's `委員長としての命令` resolves action without erasing disagreement.

This is significant student-governance evidence: authority is effective even without unanimous belief.

## 6.3 Hoshino ↔ Nonomi — prior disagreement, present mutual understanding

Nonomi reveals that she had offered a gold-card solution and Hoshino refused.

She now explains Hoshino's position sympathetically.

Their relationship therefore includes a meaningful policy disagreement:

> Nonomi is willing to mobilize private wealth; Hoshino believes doing so would undermine the mode of collective preservation.

Nonomi's understanding prevents the disagreement from becoming alienation.

## 6.4 Ayane ↔ Serika — procedural check against desperation

Ayane directly stops Serika's move toward using the money.

This extends the committee's internal balancing system.

Serika supplies urgency.

Ayane supplies procedural/evidentiary brakes.

Neither role is reducible to personality alone; together they form part of institutional governance.

## 6.5 Aru ↔ Abydos — enemy, model, and known acquaintance collapse together

Before the reveal, Aru relates to masked Abydos as aspirational icon.

After the reveal, that icon becomes the same Abydos she already knows.

This creates a potentially important relationship transition:

> adversarial familiarity → anonymous admiration → recognition that the admired anonymous object was the familiar rival.

The emotional consequence remains OPEN.

## 6.6 Mutsuki ↔ Aru — affectionate manipulation through delayed truth

Mutsuki knows what Aru does not.

She withholds the truth because the misunderstanding is funny.

The eventual source note says they tell Aru.

This suggests playful asymmetry rather than permanent deception.

## 6.7 Problem Solver 68 ↔ Abydos — accidental material transfer

The two organizations now have a bizarre new material link.

Abydos intentionally refuses the cash.

Problem Solver 68 accidentally receives it.

The source does not yet establish retention or spending.

Nevertheless the contrast is narratively sharp:

- Abydos refuses money to preserve institutional identity;
- PS68 is poor enough that Haruka immediately thinks about no longer skipping meals.

The same money means different things inside different institutional economies.

## 6.8 Hifumi ↔ Abydos — outsider witness to internal ethics

Hifumi sees the committee refuse the cash.

Because she explicitly admits limited knowledge of their circumstances, her role here is not to validate the full Abydos ethic.

Instead she adds an outsider's risk assessment.

Her continuing presence means she witnesses not only Abydos's violence but also its internal restraints.

---

# 7. Institutional-state analysis

## 7.1 Abydos Countermeasures Committee — extralegal capacity with internal limiting rules

E014 established that the committee can perform a planned armed evidence raid.

E015 adds that it also possesses internal normative constraints.

Current observed rules include:

1. mission objective matters;
2. evidence acquisition does not automatically authorize enrichment;
3. non-hostile persons are not automatic targets;
4. committee chair authority can terminate opportunistic escalation;
5. preservation of Abydos must remain compatible with an idea of what Abydos is;
6. emergency exception should not become normalized routine.

This does not prove the committee's ethics are externally legitimate.

It proves they are **not normless**.

## 7.2 Abydos as identity-bearing institution

Nonomi's line:

> `アビドスはアビドスじゃなくなってしまう`

requires an institutional model beyond debt.

Abydos has:

- history;
- members;
- relationships;
- obligations;
- procedures;
- a concept of proper repayment;
- an idea of continuity that can be violated even while the institution physically survives.

This is the first sufficiently explicit evidence to open a distinct claim about **normative institutional identity**.

## 7.3 Problem Solver 68 — financial precarity reaches food insecurity

Prior units established:

- near-exhausted operating funds;
- inability to finance desired force;
- office-rent burden;
- rejected credit;
- irregular receivables.

E015 adds:

> `もう食事抜かなくてもいいんですか？`

Problem Solver 68's financial problem is now bodily, not merely balance-sheet.

This significantly deepens the meaning of Aru's office and corporate-performance choices.

Maintaining appearance has costs borne by members.

## 7.4 Shadow bank — cash leaves the bank without intended ownership transfer

The shadow bank's employee mistakenly placed the cash in Shiroko's bag under duress in E014.

E015 confirms:

- the cash physically leaves the bank;
- it is approximately ¥100 million or more by Hoshino's rough estimate;
- Abydos did not seek it as mission objective;
- the committee intentionally refuses to appropriate it;
- the cash is accidentally left where PS68 finds it.

Do not describe this as a normal bank withdrawal, proven restitution, or deliberate Abydos donation.

## 7.5 Market Guard — pursuit/blockade capacity remains active

The opening assumes immediate pursuit and road closure.

Ayane confirms the group has crossed the blockade point.

This mildly strengthens the prior picture of Market Guard as a network-capable security apparatus rather than guards limited to one doorway.

No new evidence establishes exact legal status.

## 7.6 Kaiser Loan / Kaiser Corporation — no evidentiary advance

E015 contributes **no new Kaiser fact**.

The records remain unread.

Therefore:

- Kaiser Loan → shadow-bank operational cash interface remains established from E013;
- Abydos-specific cash → crime remains unproved;
- Kaiser Corporation → shadow-bank ownership remains unproved;
- Kaiser Loan ↔ Kaiser PMC common hierarchy remains unproved;
- Kaiser PMC → discontinued tank remains unproved.

The episode's characters sometimes speak more confidently than the evidence warrants.

The analysis must not follow them.

---

# 8. Sensei role, authority, and choice-space

E015 contains no Sensei presence.

### BA-C001 — responsible adulthood as central normative axis

**REVISE / REFINE lightly.**

E015 does not weaken the importance of responsible adulthood, but it makes clear that normative responsibility is not monopolized by adults.

Hoshino performs an explicit moral-educative leadership role toward younger students.

The broader series model should therefore distinguish:

> adulthood as a central normative problem\
> from\
> students as morally passive recipients.

### BA-C002 — Sensei legitimacy enacted rather than merely delegated

**PRESERVE.**

No new direct evidence.

### BA-C003 — Schale as corrective rather than replacement sovereign

**STRENGTHEN indirectly.**

The student institution independently governs itself after the operation.

Schale does not need to replace its internal decision-making.

### BA-C005 — conventional omnipotent player-avatar

**PRESERVE REJECTED.**

A major ethical decision occurs entirely without Sensei.

### BA-C006 — student governance inherently incapable and requires adult replacement

**STRENGTHEN REJECTION SHARPLY.**

E015 is direct counterevidence.

Students:

- debate competing ethical positions;
- recognize evidentiary/purpose distinctions;
- apply hierarchy;
- constrain violence;
- sacrifice material advantage for institutional principles.

### BA-C007 — Schale legitimacy through chosen service/restraint

**PRESERVE / COMPLICATE.**

Sensei endorsed the operation but does not supply the operation's later limiting principle.

Schale's ethical significance cannot be defined as “the adult always supplies restraint.”

### BA-C008 — choice as ethical/persona agency

**PRESERVE.**

No choice groups.

### BA-C010 — legitimate authority as custodial/nonpossessive

**STRENGTHEN by student analogue.**

Hoshino refuses to convert temporary physical control over resources into entitlement to possess them.

This is not a Sensei act, but it strengthens the larger motif of **access ≠ ownership**.

### BA-C011 — responsible adulthood distinct from supremacy/infallibility

**STRENGTHEN / REFINE.**

Students can exercise meaningful ethical judgment independently.

Responsible adulthood remains important precisely because it coexists with student agency rather than replacing it.

---

# 9. Japanese language, voice, and address

## 9.1 Hoshino's moral language stays colloquial while carrying abstract content

Hoshino never abandons her casual register.

Even the core argument contains:

- `うへ～`;
- `おじさん`;
- `カワイイ後輩`;
- `～だよー`.

The register does not become formal when the thought becomes serious.

This is important for voice reconstruction.

Hoshino's mature ethical content is often delivered through deliberately unserious surface language.

## 9.2 `こんな方法に慣れちゃうと`

`慣れる` frames moral decline as acclimatization.

The concern is not a single catastrophic fall.

It is gradual normalization.

The colloquial contraction `慣れちゃう` makes the warning conversational rather than sermon-like.

## 9.3 `仕方ないよね`

Hoshino places this phrase inside quotation marks as a future rationalization.

`仕方ない` is ordinary necessity language: “it can't be helped.”

Here it becomes morally dangerous because it can authorize repeated exceptions.

The phrasing is powerful precisely because it is mundane.

## 9.4 `そうやって学校を守ったって、何の意味があるのさ`

The rhetorical `何の意味があるのさ` moves the argument from rule compliance to telos.

What is the **meaning** of preservation?

The particle/register remains Hoshino-like rather than institutional.

## 9.5 `きちんとした方法`

Nonomi uses the ordinary phrase `きちんとした方法` rather than a legalistic term such as `合法`.

That supports the reading that the issue is proper method, not merely external legality.

“Proper” is internal and normative.

## 9.6 `アビドスはアビドスじゃなくなってしまう`

The repeated proper noun creates an identity proposition:

> Abydos can continue to exist and yet cease to be Abydos.

`～てしまう` adds an undesirable completed transition.

This is one of the strongest institutional-identity formulations in the arc.

## 9.7 `委員長としての命令`

Hoshino explicitly marks the role basis of authority.

She is not saying merely:

> I personally don't want this.

She invokes office:

> as chairperson, this is an order.

This supports both character and institutional analysis.

## 9.8 Aru's `法律や規律に縛られない`

Aru pairs:

- `法律` — law;
- `規律` — rules/discipline/order;
- `縛られない` — not bound;
- `自由な魂` — free soul.

Her outlaw fantasy is lexically a fantasy of **unbinding**.

That is more precise than generic criminality.

## 9.9 Hifumi's epistemic disclaimer

> `私はアビドスさんの事情をよく知りませんが……`

Hifumi again marks the limit of her authority before offering judgment.

This is stable evidence for her cautious interpersonal epistemics.

## 9.10 Haruka's food-security line

> `もう食事抜かなくてもいいんですか？`

The ordinary `もう～なくてもいい` construction makes the deprivation especially stark.

She does not dramatize hunger.

She asks whether the condition can now stop.

---

# 10. Motifs, symbols, and callbacks

## 10.1 Documents versus cash

E014 established:

> treasure offered → records requested.

E015 makes the distinction explicit again:

> `私たちに必要なのは書類だけ。お金じゃない。`

Paper represents truth/proof.

Cash represents temptation, power, relief, and contamination.

The story privileges the harder-to-use evidentiary object over the immediately useful material object.

## 10.2 Access versus ownership

The committee physically controls the money.

Hoshino denies that control creates entitlement.

This echoes the Prologue's larger custody motif:

> capacity to possess or control does not necessarily justify possession.

## 10.3 Debt versus identity

Abydos's debt is numerically devastating.

E015 insists that debt elimination is not the sole objective function.

How the debt is repaid is part of what the school is.

## 10.4 Habituation

E015 introduces a major motif:

> exceptional act → repeated act → normalized act → changed person/institution.

This should be tracked beyond the arc.

## 10.5 Masks and moral visibility

Aru sees masked Abydos as pure outlaw freedom.

The mask hides not only identity but internal ethical structure.

Observers see conduct.

They do not see deliberation.

## 10.6 False mythology and true behavior

The `覆面水着団` backstory is invented.

The raid is real.

The self-restraint is real.

Aru believes the invented part because the real action makes it plausible.

## 10.7 The gold card

The gold card returns as a rejected shortcut.

It represents the possibility of solving structural hardship through private wealth.

Hoshino's refusal indicates that institutional self-rescue matters to her independently of legal purity.

## 10.8 Accidental redistribution

The cash rejected by Abydos falls to another poor organization.

This creates darkly comic distributive irony.

Abydos's moral refusal does not return the money to its prior institution.

It reroutes it unpredictably.

## 10.9 Hunger

The final cash scene converts financial abstraction into bodily need.

For PS68, money means food.

That fact complicates any easy moral judgment of what they may do next.

## 10.10 Sunset before sunset

`行こう！夕日に向かって！` followed by `夕日、まだですけど……` turns heroic imagery into conscious performance.

The story repeatedly asks how narratives about oneself relate to actual conduct.

---

# 11. Violence, ethics, power, and responsibility

## 11.1 E015 does not absolve E014

Leaving the money does not erase:

- armed coercion;
- security neutralization;
- threats;
- Hifumi's compromised consent;
- unlawful/extralegal evidence seizure.

The refusal matters as evidence of internal limits, not as retroactive purification.

## 11.2 Purpose limitation is real

The committee distinguishes:

> evidence needed for investigation\
> from\
> money useful for debt relief.

Hoshino insists that access gained for one purpose should not silently authorize another.

## 11.3 Hoshino is not a simple deontologist

Her argument includes:

- consequences for future behavior;
- virtue/habit formation;
- care for juniors;
- institutional identity;
- role authority.

It is not reducible to “stealing is always wrong.”

## 11.4 Serika's position is not simple greed

Serika wants the money for the school.

Her reasoning is restitutional and defensive.

The ethical weakness lies in overclaiming provenance and treating opponent badness as sufficient permission.

## 11.5 Non-hostility matters to Hoshino

Hoshino refuses to attack Aru when Aru shows no hostile intent.

This establishes a discriminatory principle after the bank raid.

Again, it does not settle the bank raid's own proportionality.

## 11.6 Institutional ethics can be stricter than legal compliance and looser than legality

Abydos's rule is paradoxical from an external legal perspective:

- armed evidence raid: permitted internally;
- keeping accidentally acquired criminal-bank cash: prohibited internally.

The group's moral map does not track law one-to-one.

It tracks purpose, identity, necessity, and corruption risk.

## 11.7 The hardest ethical line is about what repeated exceptions do to the self

`仕方ないよね` is the key.

Hoshino fears a future in which necessity becomes a reusable moral solvent.

That concern is highly generalizable and should be tested against later crises.

---

# 12. Competing readings and counterevidence

## Reading A — “E015 proves the cash belonged to Abydos.”

**REJECT.**

Serika asserts that the money is what Abydos earned and sent into the shadow bank.

The records are still unread.

The specific provenance of the cash remains unproved.

## Reading B — “Hoshino has become a legalist.”

**REJECT.**

She has just led an armed shadow-bank raid.

Her argument concerns objective limitation, habituation, juniors' character, and institutional meaning—not categorical obedience to law.

## Reading C — “Because Abydos leaves the money, the raid is morally justified.”

**REJECT.**

Refusal of enrichment is morally relevant but does not erase coercive means or Hifumi's consent problem.

## Reading D — “Serika is greedy.”

**DOWNGRADE strongly.**

Serika wants to use the money for school debt and sees it as restitution from a harmful financial system.

Her reasoning is ethically compressed, but the source does not frame her desire as private enrichment.

## Reading E — “Nonomi always shared Hoshino's position.”

**REJECT.**

Nonomi initially agrees with Serika.

She later articulates Hoshino's principle and accepts it.

## Reading F — “Shiroko agrees with Hoshino.”

**OPEN.**

Shiroko predicts Hoshino's opposition and obeys the chairperson's order.

She does not clearly state her own position.

## Reading G — “Abydos is now a normless criminal group.”

**REJECT.**

E015 demonstrates internal restraints regarding objective, property, target discrimination, hierarchy, and institutional identity.

This does not make external illegality disappear.

## Reading H — “Abydos is morally pure because it has internal rules.”

**REJECT.**

Internal norms can be meaningful without being sufficient.

The prior raid remains ethically contestable.

## Reading I — “Aru admires Abydos because she understands their ethics.”

**REJECT.**

Aru sees their audacity and mistakes it for unbounded freedom.

She does not witness the cash debate.

## Reading J — “Aru's outlaw ideal is fundamentally about harming people.”

**DOWNGRADE.**

Her explicit vocabulary centers freedom from law, rules, fear, and constraint.

Harm can result from that ideal, but cruelty is not the core self-description.

## Reading K — “The abandoned money is an intentional gift to Problem Solver 68.”

**REJECT.**

Nonomi forgets the bag.

Abydos does not know PS68 will receive it.

## Reading L — “Haruka's line proves all four PS68 members are chronically starving.”

**REJECT / OVERCLAIM.**

It establishes skipped meals within their financial hardship.

It does not quantify frequency or individual nutritional status.

## Reading M — “The Kaiser investigation advances because the records are now available.”

**PRESERVE ONLY AS POTENTIAL.**

Physical access advances.

Evidentiary content does not.

E015 does not read the records.

---

# 13. Cumulative ledger deltas

## 13.1 Character ledger

- **Hoshino:** major strengthening—chairperson as moral governor; habituation analysis; junior-protection ethic; institutional-identity principle; target discrimination.
- **Shiroko:** mask comfort/action identity; predicts Hoshino's boundary; obeys chair authority; personal cash view remains open.
- **Serika:** restitution/consequentialist argument under deprivation; evidentiary overclaim; continued acceptance of committee authority.
- **Ayane:** procedural conscience now includes clear line against self-enrichment.
- **Nonomi:** initially supports use of cash, then articulates/accepts Hoshino's institutional-identity principle; gold-card offer confirmed.
- **Hifumi:** outsider epistemic modesty, risk framing, reality-check function continue.
- **Aru:** freedom/unbinding ideal sharpened; anonymous admiration collides with recognition of Abydos.
- **Mutsuki:** information withholding for amusement becomes explicit.
- **Kayoko:** ordinary-explanation reality check continues.
- **Haruka:** skipped meals establish bodily depth of PS68 poverty.
- **Sensei:** no presence; student ethical self-governance strengthened.

## 13.2 Relationship ledger

- Hoshino ↔ Shiroko: values predictable enough for Shiroko to forecast chair's ruling.
- Hoshino ↔ Serika: strong disagreement resolved through legitimate committee authority.
- Hoshino ↔ Nonomi: prior gold-card disagreement contextualized; mutual understanding evident.
- Ayane ↔ Serika: procedural check against scarcity-driven escalation.
- Aru ↔ Abydos: anonymous admiration → identity revelation.
- Mutsuki ↔ Aru: playful control of truth timing.
- PS68 ↔ Abydos: accidental cash transfer creates material entanglement.
- Hifumi ↔ Abydos: witnesses both transgression and self-restraint.

## 13.3 Institution ledger

- Abydos: internal limiting norms now explicit.
- Abydos identity: proper method becomes constitutive of institutional continuity.
- PS68: food insecurity now textually established.
- Shadow bank: cash loss confirmed through employee misunderstanding; ultimate recipient unresolved.
- Market Guard: blockade/pursuit capacity reinforced.
- Kaiser: no new institutional proof.

## 13.4 Sensei ethics ledger

- no E015 presence/choices;
- post-raid restraint is student-authored;
- adult responsibility must remain distinct from adult monopoly on moral judgment;
- E013 launch endorsement remains antecedent responsibility.

## 13.5 Japanese voice/address ledger

Add:

- Hoshino: `こんな方法に慣れちゃうと`, `仕方ないよね`, `何の意味があるのさ`, `カワイイ後輩`, `委員長としての命令`.
- Nonomi: `きちんとした方法`, `アビドスはアビドスじゃなくなってしまう`.
- Serika: `汗水流して稼いだ`, `悪人のお金を盗んで、何が悪いの！？`.
- Hifumi: `事情をよく知りませんが`, `災いの種`.
- Aru: `法律や規律に縛られない`, `本当の意味での自由な魂`.
- Haruka: `もう食事抜かなくてもいいんですか？`.
- group-performance vocabulary: `覆面水着団`, `正義の怪盗`, `我が道の如く魔境を行く`, `夕日に向かって`.

## 13.6 Motif/theme ledger

Add:

- survival versus identity;
- means as constitutive of ends;
- habituation and emergency rationalization;
- documents versus cash;
- access versus ownership;
- self-imposed rules inside extralegal action;
- masks hiding internal moral structure;
- accidental redistribution;
- hunger as material consequence of institutional precarity;
- heroic timing/performance versus reality.

## 13.7 Claim revision ledger

- BA-C001: **REVISE / REFINE lightly**.
- BA-C002: **PRESERVE**.
- BA-C003: **STRENGTHEN indirectly**.
- BA-C004: **PRESERVE**.
- BA-C005: **PRESERVE REJECTED**.
- BA-C006: **STRENGTHEN REJECTION SHARPLY**.
- BA-C007: **PRESERVE / COMPLICATE**.
- BA-C008: **PRESERVE**.
- BA-C009: **PRESERVE**.
- BA-C010: **STRENGTHEN by analogue**.
- BA-C011: **STRENGTHEN / REFINE**.
- BA-C012: **PRESERVE**.
- BA-C013: **PRESERVE / HOLD UNRESOLVED**.
- BA-C014: **STRENGTHEN lightly**.
- **BA-C015: OPEN** — Abydos institutional identity is constituted partly by the means through which it survives; mere persistence can become self-defeating if emergency expedients normalize practices incompatible with the institution the students believe they are preserving.

---

# 14. Claim transitions at E015

## BA-C001 — responsible adulthood as central normative axis

**REVISE / REFINE lightly.**

E015 shows student leadership performing explicit moral formation without Sensei. Responsible adulthood remains central, but ethical agency is distributed.

## BA-C002 — Sensei legitimacy enacted rather than merely delegated

**PRESERVE.**

No direct E015 evidence.

## BA-C003 — Schale as cross-institutional corrective rather than replacement sovereign

**STRENGTHEN indirectly.**

Abydos retains independent governance and moral decision-making.

## BA-C004 — coordination + privileged access + vulnerability

**PRESERVE.**

No Sensei capability evidence.

## BA-C005 — conventional omnipotent player-avatar

**PRESERVE REJECTED.**

A consequential institutional decision occurs without Sensei.

## BA-C006 — student governance inherently incapable and requires adult replacement

**STRENGTHEN REJECTION SHARPLY.**

The committee debates, limits, commands, and self-regulates.

## BA-C007 — Schale legitimacy through chosen service/restraint

**PRESERVE / COMPLICATE.**

Adult endorsement does not equal adult monopoly on restraint.

## BA-C008 — choice as ethical/persona agency more than route branching

**PRESERVE.**

No E015 choice groups.

## BA-C009 — systems humanized relationally

**PRESERVE.**

No material new system ontology.

## BA-C010 — legitimate authority custodial/transferable/nonpossessive

**STRENGTHEN by analogue.**

Hoshino explicitly refuses to convert physical control over the cash into entitlement.

## BA-C011 — responsible adulthood distinct from supremacy/infallibility

**STRENGTHEN / REFINE.**

Student moral competence remains robust without Sensei.

## BA-C012 — political economy/proxy architecture of coercion

**PRESERVE.**

No new Kaiser PMC, client, tank, or sponsor evidence.

## BA-C013 — Abydos debt / Kaiser Loan / shadow-finance interface

**PRESERVE / HOLD UNRESOLVED.**

The `集金記録` are secure but unread.

Serika's claim that the cash is Abydos's own money must not be promoted to fact.

### Current canonical provisional formulation after E015

> **Abydos's debt is an active high-interest creditor relationship administered by Kaiser Loan, a business operated by Kaiser Corporation. The same Kaiser Loan collection apparatus used for Abydos's interest payment was directly observed delivering monthly cash collections to a Black Market shadow bank under Market Guard protection. E014–E015 establish that Abydos successfully seized collection records that may test the provenance relationship, but E015 does not disclose their contents. It therefore remains unproved that the specific cash in the shadow bank included Abydos's payment, that Abydos's money financed crime, that Kaiser owns the shadow bank, or that Kaiser Loan and Kaiser PMC form one coordinated anti-Abydos hierarchy.**

## BA-C014 — parallel extra-federal institutional ecologies

**STRENGTHEN lightly.**

Market Guard's pursuit/blockade response reinforces network-level enforcement capacity.

No exact legal-status resolution occurs.

## BA-C015 — survival, means, and institutional identity

**OPEN — NEW.**

### Provisional formulation

> **Abydos defines institutional survival normatively rather than as bare persistence. E015 explicitly argues that repeated reliance on expedient wrongdoing would habituate the students to expanding “necessary” exceptions, and Nonomi states that unless repayment occurs through a `きちんとした方法`, Abydos would cease to be Abydos. The claim is therefore that methods of survival can constitute institutional identity: preserving the organization through practices that erode its governing values may defeat the meaning of preservation itself.**

### Evidence

- Hoshino: `私たちに必要なのは書類だけ。お金じゃない。`
- Hoshino: `こんな方法に慣れちゃうと……`
- Hoshino: future `仕方ないよね` rationalization.
- Hoshino: `そうやって学校を守ったって、何の意味があるのさ。`
- Nonomi: `きちんとした方法で返済をしない限り、アビドスはアビドスじゃなくなってしまう……。`
- Hoshino: `これは委員長としての命令だよー。`

### Forward test

Test whether later crises:

- preserve this anti-habituation rule;
- force Hoshino or others to revise it;
- reveal that “proper repayment” is linked to memory, autonomy, solidarity, or another deeper value;
- expose contradictions between this internal self-image and how Abydos treats outsiders.

---

# 15. Open questions after E015

1. What exactly is written in the seized `集金記録`?
2. Do the records identify Kaiser Loan collections individually?
3. Can Abydos trace its own payment into the shadow bank?
4. Do the records establish criminal use, ownership, or merely transaction flow?
5. Is Kaiser Corporation linked beyond the already known Kaiser Loan operation?
6. Is Kaiser PMC linked to Kaiser Loan by more than shared naming?
7. Does the evidence connect to the discontinued tank?
8. What happens to the roughly ¥100 million found by Problem Solver 68?
9. Does PS68 keep or use it?
10. Does Haruka's skipped-meal line indicate broader ongoing deprivation?
11. How does Aru process learning that Abydos was the `覆面水着団`?
12. Does Aru revise her concept of “true outlaw” after identifying the group?
13. Does Hoshino's anti-habituation principle survive the next existential pressure?
14. Does Serika later revise the belief that shadow-bank cash can be treated as Abydos's own money?
15. Does Nonomi's gold-card solution return?
16. Is `覆面水着団` remembered outside this local comic sequence?
17. Does Hifumi remain implicated or reputationally exposed after leaving the Black Market?
18. Does Market Guard retaliation continue?
19. Does Sensei re-enter before the evidence is interpreted?
20. Does E016's title `明かされる真実` refer to the collection records, another investigation strand, or both?

---

# 16. Evidence locator table

| Analytical use | Stable locator | Raw locator |
|---|---|---|
| escape urgency / pursuit | `u:0002-0005` | DataList[2301]–[2304] |
| Shiroko mask / Abydos as fitting home | `u:0007-0010` | [2306]–[2311] |
| blockade cleared | `u:0013-0015` | [2318]–[2320] |
| records confirmed in bag | `u:0016-0017` | [2321]–[2322] |
| accidental cash discovery | `u:0019-0022` | [2325]–[2328] |
| Ayane objects to use | `u:0025-0027` | [2332]–[2334] |
| Serika restitution/criminal-money argument | `u:0028-0029` | [2335]–[2336] |
| Nonomi initially agrees | `u:0031-0032` | [2338]–[2339] |
| Shiroko predicts Hoshino | `u:0033-0036` | [2340]–[2343] |
| records not money | `u:0037` | [2344] |
| habituation argument begins | `u:0038-0040` | [2345]–[2347] |
| `仕方ないよね` future rationalization | `u:0042` | [2349] |
| juniors / meaning of saving school | `u:0043-0044` | [2350]–[2351] |
| gold-card callback | `u:0046-0047` | [2353]–[2354] |
| `アビドスはアビドスじゃなくなる` | `u:0048-0049` | [2355]–[2356] |
| chairperson order / documents only | `u:0050-0052` | [2357]–[2361] |
| Hifumi `災いの種` | `u:0053-0054` | [2362]–[2363] |
| Aru approaches non-hostile | `u:0057-0064` | [2366]–[2377] |
| Shiroko suggests repel / Hoshino rejects non-hostile attack | `u:0065-0069` | [2378]–[2382] |
| Aru praises five-minute raid | `u:0070-0074` | [2383]–[2387] |
| Aru asks group name | `u:0076-0078` | [2389]–[2391] |
| `覆面水着団` name | `u:0080-0084` | [2393]–[2397] |
| invented costume lore | `u:0086-0087` | [2399]–[2400] |
| righteous phantom-thief lore / Christina | `u:0088-0090` | [2401]–[2403] |
| invented motto | `u:0091-0092` | [2404]–[2405] |
| Kayoko/Mutsuki reaction | `u:0093-0094` | [2407]–[2408] |
| episode-title exit / no sunset | `u:0095-0099` | [2411]–[2415] |
| Aru internalizes motto | `u:0100-0101` | [2416]–[2417] |
| Mutsuki delays truth for amusement | `u:0102-0105` | [2420]–[2423] |
| PS68 finds bag | `u:0106-0114` | [2426]–[2434] |
| Abydos realizes cash left behind | `u:0115-0121` | [2436]–[2442] |
| PS68 cash shock | `u:0122-0124` | [2444]–[2446] |
| Haruka skipped meals | `u:0125-0126` | [2449]–[2450] |
| Aru learns masked group was Abydos | `u:0127-0132` | [2452]–[2457] |
| next episode marker | `u:0133` | [2459] |

---

# 17. Cumulative delta summary

E015 materially changes the project in five ways.

### 1. It opens a new institutional-ethics claim

**BA-C015** is warranted.

Abydos's identity is partly constituted by the means through which it survives.

### 2. It strengthens student-governance competence

The strongest moral limit in the raid sequence is imposed by students without Sensei present.

### 3. It restrains the interpretation of the Kaiser investigation

The records are possessed but unread.

No new Kaiser provenance fact is established.

### 4. It deepens Hoshino and Problem Solver 68 simultaneously

Hoshino becomes the clearest internal theorist of moral habituation and institutional identity.

PS68's poverty becomes bodily through Haruka's reference to skipped meals.

### 5. It turns Aru's outlaw aspiration into dramatic irony

Aru praises masked Abydos for freedom from constraint while the audience has just watched Abydos impose constraints on itself.

Her ideal and their actual conduct are not the same thing.

---

# 18. Conclusion and next source boundary

E015 is a deceptively important episode.

Its plot appears to be post-robbery comedy.

Its real function is to answer a question E014 made unavoidable:

> **Once you permit yourself one extraordinary transgression, what stops the exception from expanding?**

Hoshino's answer is not external law.

It is identity.

The committee needs the records, not the money.

If they begin solving every desperate problem by telling themselves `仕方ないよね`, they will become people for whom the exceptional act is ordinary.

If preserving Abydos requires that transformation, then the preservation has lost its meaning.

Nonomi gives the proposition its cleanest institutional form:

> `きちんとした方法で返済をしない限り、アビドスはアビドスじゃなくなってしまう`

That statement establishes a new analytical responsibility for the project.

Abydos is not only a financially distressed school.

It is an institution trying to decide which compromises still count as survival and which would amount to self-erasure.

At the same time, the story refuses moral tidiness.

The students still raided a bank.

Hifumi was still dragged beyond her original consent.

Serika still treats suspicion as proof.

The money they virtuously refuse does not magically return to a neutral owner—it falls into the hands of another desperate organization.

Haruka's first thought is whether they can finally stop skipping meals.

And Aru, who imagines authentic outlawhood as freedom from all constraint, has spent the episode admiring people whose most consequential post-raid act is precisely to constrain themselves.

The Kaiser investigation remains paused at the edge of proof.

The collection records are still in Shiroko's possession.

Their contents remain unread.

The next sequential unit is therefore:

**`BLUE_ARCHIVE_MAIN_V001_C001_E016_DEEP_READING.md`**\
`BA:main:001:001:016`\
**第16話「明かされる真実」**

The E016 reading must preserve all E015 distinctions and specifically test:

1. what the `集金記録` actually contains;
2. whether Abydos-specific payments can now be traced;
3. whether Kaiser Loan, Kaiser Corporation, the shadow bank, Kaiser PMC, or the discontinued weapon become explicitly connected;
4. whether BA-C013 can finally be strengthened from operational interface to specific provenance;
5. whether BA-C015's institutional-identity principle is immediately tested or merely left standing;
6. whether the accidental PS68 cash transfer has consequences;
7. whether Aru's discovery changes her contract, self-image, or relationship to Abydos;
8. whether Sensei re-enters the investigation;
9. whether any audience-only E012 knowledge crosses into Abydos's epistemic horizon;
10. whether a checkpoint becomes warranted after the new truth is disclosed.

**Recommended reasoning:** GPT-5.6 Sol — **High**.
