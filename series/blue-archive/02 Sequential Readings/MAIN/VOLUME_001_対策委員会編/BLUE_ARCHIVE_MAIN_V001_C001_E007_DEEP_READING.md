---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E007
generation: V1
status: active_provisional
source_boundary: Canonical Japanese main-story unit BA:main:001:001:007, 対策委員会編 第7話『新たなる脅威？』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-16
---

# BLUE ARCHIVE — MAIN V001 C001 E007 DEEP READING
## 対策委員会編 — 第7話「新たなる脅威？」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the ninth canonical main-story object in analytical order and the seventh object in `対策委員会編`:

- story ID: `BA:main:001:001:007`;
- analytical scope: `MAIN_V001_C001_E007`;
- source title: `第7話;新たなる脅威？`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第7話`;
- raw group ID: `11070`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- record count: **97**;
- promoted utterance count: **71**;
- normalized choice groups: **2**;
- canonical scene count: **3**;
- normalized person IDs at story level: Ayane, Hoshino, Nonomi, Serika;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_007.md`;
- complete source-side convenience rendering: `07話_新たなる脅威？.md`.

### Canonical scene structure

1. `BA:main:001:001:007:scene:001` — `対策委員会・教室`. Serika attempts to present herself as recovered but collapses; the committee credits Sensei's tracking role, then analyzes wreckage from the rescue battle and discovers that the Helmet Gang possessed a prohibited weapon type beyond what the students believe the gang could obtain independently. Primary text-bearing span: `ScenarioScriptMain1ExcelTable.json:DataList[1200]–[1221]`, with gaps for control records.
2. `BA:main:001:001:007:scene:002` — `高層オフィスビル`. An unidentified sponsor assesses the Helmet Gang's failure, states that a main battle tank had been supplied, adopts the logic `目には目を、生徒には生徒を`, and places a job with `便利屋68`. Text-bearing span: `DataList[1223]–[1232]`.
3. `BA:main:001:001:007:scene:003` — `カタカタヘルメット団のアジト`, followed without a new explicit place marker by Serika's post-rescue visit scene. Unknown/new combatants defeat the Helmet Gang, identify themselves collectively as `便利屋68`, and declare that they will take over the Abydos job; Sensei then visits Serika, who thanks Sensei while insisting on repaying the personal obligation. Text-bearing span: principally `DataList[1234]–[1294]`.

### Choice-space

Only two normalized Sensei choice groups occur, both singleton formulations:

1. `BA:main:001:001:007:scene:003:choice:001` — `お見舞いに来たよ。` — raw `DataList[1274]`.
2. `BA:main:001:001:007:scene:003:choice:002` — `それは良かった。` — raw `DataList[1278]`.

E007 therefore contains no branching or persona-polarized choice pair. At the Serika relationship beat, the authored Sensei response range is unusually narrow: **visit, concern, relief**.

### New-actor identity / source-layer caution

E007 exposes a significant difference between source layers.

The complete convenience rendering supplies labels including `カイザーPMC理事`, `ムツキ`, and `アル`. However, the promoted canonical utterance/scene layer keeps the high-rise sponsor and the new hideout combatants as `？？？` / `BA_SPEAKER_UNKNOWN`, and the story-level normalized `person_ids` list contains only the four Abydos students named above.

Accordingly, this reading distinguishes four levels of evidence:

1. **canonical textual fact:** an unidentified sponsor in a high-rise office says a main battle tank was sent and commissions `便利屋68`;
2. **canonical textual fact:** unknown combatants defeat the Helmet Gang and explicitly identify their organization as `便利屋68`;
3. **source-convenience metadata:** the convenience rendering attaches specific franchise labels to some otherwise unresolved speakers;
4. **not yet promoted:** fine-grained character-state or voice claims for those named new individuals.

The organizational identity `便利屋68` is secure because it is self-declared in the canonical scene text. The exact normalized identities of individual new speakers remain **SOURCE-LAYER UNRESOLVED at this boundary**.

### Local-information lock

Available prior analytical authority is limited to:

- the canonical two-unit Prologue and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md` through `E006_DEEP_READING.md`.

No E008 or later main-story unit, bond story, MomoTalk, event, character package, relationship bundle, adaptation, wiki, or franchise hindsight is used to decide the hidden sponsor's identity, `便利屋68`'s internal relationships, the exact commercial contract, or the ultimate purpose of the operation against Abydos.

---

# 1. Story placement and local chronology

E006 ended before the Countermeasures Committee had fully returned to ordinary conditions. Serika had been recovered from a moving transport, but the group remained in hostile territory and was preparing to break through an encirclement. E007 begins after that escape has succeeded.

The episode performs three linked transitions:

> **rescue aftermath → forensic discovery of a hidden supply structure → replacement of the failed local proxy by a paid specialist organization**

while, in parallel, it advances the most immediate interpersonal question from E004–E006:

> **Serika rejects automatic adult legitimacy → Sensei helps rescue her → Serika acknowledges the help without surrendering reciprocity or Abydos-centered judgment**

This is the first Abydos unit in which the story unmistakably opens a **reader-knowledge gap** between what the committee knows and what the audience is shown.

The committee knows:

- the Helmet Gang used a weapon type prohibited in Kivotos;
- the gang should not have been able to obtain that equipment independently;
- analyzing the circulation route may reveal an entity `裏にいる`;
- that hidden entity may explain why ordinary delinquents pursue Abydos so persistently.

The audience is then shown more:

- an unidentified sponsor considers the Helmet Gang expendable and inadequate;
- the sponsor explicitly says a `主力戦車` had been sent;
- the sponsor switches methods after failure;
- `便利屋68` is commissioned;
- `便利屋68` subsequently removes the Helmet Gang from the operation and declares the Abydos job its own.

Thus the title's question mark matters. `新たなる脅威？` does not simply mean “a completely new enemy has appeared.” The deeper threat is partly **old but newly visible**. The Helmet Gang's pressure had already been embedded in a larger supply and contracting structure. What changes is the committee's evidence and the reader's access to the architecture behind the violence.

---

# 2. Narrative reconstruction

Back in the Countermeasures Committee classroom, Ayane checks on Serika. Serika insists she is fine and tries to demonstrate that she is energetic, but immediately staggers and collapses. Nonomi moves to take her to the infirmary. Hoshino remarks that after taking a hit from a `Flak41` anti-aircraft gun, it would be stranger if Serika could simply walk around normally, and says she should be allowed to rest.

The group then looks back on how close the abduction came to disaster. Ayane says the situation could have become terrible without Sensei. Nonomi specifically credits Sensei with allowing them to keep tracking Serika's location. Hoshino preserves the established joke by concluding that Sensei was not *merely* a stalker.

Ayane then changes the subject to physical evidence recovered during the battle. The committee has examined scattered tank parts and concluded that the vehicle was an `違法機種` whose use is prohibited in Kivotos. More importantly, the Helmet Gang appears to possess weapons it could not have acquired by itself.

Nonomi proposes analyzing the part's `流通ルート`. If they can reconstruct the circulation/distribution path, they may be able to identify the `裏にいる存在`—the entity behind the gang. Ayane connects this to motive: discovering that backer may explain why otherwise ordinary delinquents have targeted Abydos so persistently. Hoshino agrees that they should investigate carefully.

The narrative then cuts away from the students to a high-rise office building.

An unidentified speaker contemptuously judges the Helmet Gang as inferior delinquents whose capabilities have reached their limit. The speaker says that even after a `主力戦車` was sent, the result was still failure. The speaker then changes strategy using the formula:

> `目には目を、生徒には生徒を`

and decides to hire specialists.

A phone call follows. The receiving party identifies itself as `便利屋68` and says it solves anything. The hidden sponsor asks the organization to take a job.

The scene then cuts to the Helmet Gang hideout. Unknown/new combatants violently overwhelm the gang. One reports that her side is finished; another reports the area secured to a `ボス`. The defeated Helmet Gang demands identification.

A leading speaker mocks the hideout, then jokingly tells the gang it will be “liberated from labor.” When the gang does not understand, the speaker clarifies: they are being fired. From that moment, `アビドスは私たちが引き受ける`—the Abydos matter will be taken over by the newcomers.

The organization then identifies itself:

> `私たちは、便利屋68。`

and defines its commercial principle:

> `金さえもらえれば、何でもする……。`

They are `なんでも屋`: a paid problem-solving/odd-jobs organization willing to do anything for money.

The story then returns to Serika's recovery. Sensei visits her. Serika initially insists she is fine and cannot remain inactive: Ayane and the others are worried, and she still needs to go to her part-time job. She tries to wave off the need for a visit.

Sensei's first authored line simply says that Sensei came to see how she was doing. The second says that it is good that she is all right.

After a pause, Serika stops Sensei. With difficulty, she says she realized she had never properly thanked Sensei. She gives an explicit `ありがとう……色々と……`.

She immediately protects her sense of reciprocity and Abydos-centered responsibility. Sensei should not think that this much alone means Sensei has fully contributed to Abydos. She calls the assistance a `借り` and promises:

> `この借りはいつか必ず返すんだから！`

The scene ends with a small but real change in interpersonal tone. Serika says:

> `じゃあ……また明日ね！`

then hesitates—`えっと、せ……`—before finishing:

> `……先生。`

The next-title marker is `次回;便利屋参上！`.

---

# 3. Central thesis

The strongest E007 thesis is:

> **E007 reveals that the apparent Helmet Gang conflict is an externally sponsored and economically mediated coercive system rather than a purely local delinquent feud: prohibited weapons, a hidden supplier who claims to have sent a main battle tank, and the replacement of failed gang proxies with paid `便利屋68` specialists expose a vertical structure of procurement, contracting, and deniable violence. In parallel, Serika's gratitude to Sensei becomes explicit but remains governed by reciprocity rather than submission: rescue creates a `借り` she intends to repay, and continued contact becomes imaginable without any textual declaration that she has surrendered her independent judgment.**

This unit therefore adds a new axis to the Abydos analysis.

Until E006, the major institutional asymmetry was largely:

> **Abydos local competence + severe resource scarcity ↔ Schale's exceptional outside capacity**.

E007 shows that Abydos's opponents also possess access to **outside capacity**—but through a very different moral structure.

The contrast is not “students versus adults” or “local versus external” in itself. It is between ways of using asymmetrical capacity:

- Sensei's exceptional resources/information are repeatedly directed toward enabling, rescue, or continued service without taking ownership of Abydos;
- the hidden sponsor supplies weapons to disposable proxies and, when they fail, purchases a new force to continue pressure against the school.

Power is therefore becoming less important as a category than **the relationship through which power is exercised**.

A second, equally important pattern appears in the language of money and repayment.

E005 showed Serika converting her time into wages to service Abydos's literal debt. E007 shows a hidden sponsor converting money/resources into outsourced violence. `便利屋68` defines itself through payment: `金さえもらえれば、何でもする`. Then Serika describes Sensei's rescue as a `借り` that she must `返す`.

Three economic registers now coexist:

1. **institutional debt** — Abydos owes an enormous financial liability;
2. **commercial contract** — a sponsor purchases coercive labor against Abydos;
3. **personal reciprocal obligation** — Serika refuses to let rescue become unilateral dependency and frames help as a favor/debt to be repaid.

This does not mean all three are morally equivalent. Their juxtaposition instead makes **how obligations are created and repaid** a growing thematic concern.

---

# 4. Scene-by-scene close reading

## 4.1 Serika's collapse: resilience is not invulnerability

Canonical scene: `BA:main:001:001:007:scene:001`.

Serika's first post-rescue behavior is consistent with the self-demand established in E005. Asked whether she is hurt, she says she is fine and begins to demonstrate it:

> `見てよ、ピンピンして……`

She then collapses.

This is more than a physical gag. E005 had shown Serika treating available time as something to be converted into useful labor; E006 showed her returning to tactical contribution immediately after rescue. E007 now shows the cost of that stance. Her will to continue functioning exceeds what her body can presently sustain.

Hoshino's response is useful because it establishes the severity without romanticizing the collapse. Serika took a hit from a `Flak41` anti-aircraft gun; Hoshino says walking around normally after that would itself be strange.

At this boundary, the safest conclusion is:

> **Blue Archive's student bodies may tolerate extraordinary violence, but the narrative still uses exhaustion, injury, collapse, and recovery as meaningful state changes.**

The episode therefore cautions against treating combat survivability as emotional or physiological invulnerability.

## 4.2 Care is already distributed before Sensei enters the interpersonal scene

Nonomi immediately says she will take Serika to the infirmary. Hoshino says she should rest. Ayane checks on her.

Sensei is praised for the rescue, but the students do not wait for Sensei to define post-rescue care. This continues the differentiated-capacity pattern from E006: Sensei was essential to one missing informational function, not the origin of every caring or competent action around Serika.

The social system surrounding Serika is already active.

## 4.3 `先生がいなかったら` is gratitude for a specific causal contribution

Ayane's `先生がいなかったら……` and Nonomi's explicit statement that Sensei's contribution prevented them from losing Serika's trail represent strong praise.

But the causal object remains specific: **tracking**.

This matters for the ongoing rejection of an omnipotent-savior reading. The committee does not say Sensei alone defeated the enemy, knew the area, discovered the abduction, cared about Serika, or physically performed every rescue function. E006 already distributed those functions across the group.

Hoshino's `ただのストーカーじゃなかった` joke keeps the E005 boundary violation in narrative memory even while recognizing the emergency value of Sensei's capacities. The text itself refuses a clean moral overwrite.

## 4.4 Physical debris becomes institutional evidence

Ayane's examination of the destroyed tank parts is a major genre and analytical transition.

The previous units asked:

- Can the students repel attackers?
- Who is threatening them?
- Can Serika be recovered?

E007 asks:

> **Where did the attackers' capabilities come from?**

Ayane identifies the equipment as a `違法機種`—an illegal/prohibited model. This does two things at once.

First, it establishes a wider regulatory order. “Illegal” has meaning only because some authority or norm distinguishes permitted from prohibited equipment. E007 does not yet define the governing statute, regulator, enforcement mechanism, or scope of the prohibition, so those remain OPEN.

Second, it makes material culture evidentiary. A broken tank part is not merely wreckage. Its model and distribution history can reveal institutional relationships.

That is a meaningful expansion of the project's evidence ontology inside the fiction itself: **objects carry provenance**.

## 4.5 `自分たちでは入手できない` converts capability disparity into a supply-chain hypothesis

Ayane says the Helmet Gang possesses weapons it could not obtain itself.

This is analytically stronger than “the gang is unusually well armed.” It separates **possession** from **procurement capacity**.

The committee therefore begins reasoning backward:

> prohibited equipment in gang hands → gang cannot independently procure it → some external path supplied it → trace the path → identify the backer.

Nonomi names the investigative method directly:

> `この部品の流通ルートを分析すれば`

The phrase `流通ルート` moves the conflict into logistics, commerce, and institutional networks. The committee is no longer merely reacting to attackers; it is beginning a counter-network investigation.

## 4.6 `裏にいる存在`: the committee knows there is a hidden layer without yet knowing its identity

Nonomi's `裏にいる存在` and Ayane's question about why mere delinquents are so persistent establish the students' epistemic position precisely.

They now have strong reason to believe there is someone or something behind the Helmet Gang. They do **not** yet know who.

This distinction matters because the following cutaway gives the audience evidence that the students lack. Future analysis must preserve that knowledge asymmetry rather than back-projecting the sponsor's shown dialogue into the committee's beliefs.

## 4.7 The high-rise cutaway confirms supply and command from above

Canonical scene: `BA:main:001:001:007:scene:002`.

The unidentified sponsor says:

> `主力戦車まで送り出したというのに`

This directly supports the committee's supply hypothesis from the reader's perspective. The tank was not random battlefield salvage. The hidden actor understands it as something **sent** into the operation.

The sponsor also calls the Helmet Gang `格下のチンピラごとき`, treating them with contempt as disposable lower-tier operators.

The threat architecture becomes vertical:

> **resource-holding sponsor → armed local proxy → Abydos target**.

E007 then shows that the middle layer is replaceable.

## 4.8 `目には目を、生徒には生徒を`: instrumental equivalence

The sponsor's adaptation formula is:

> `目には目を、生徒には生徒を……`

The first half invokes retaliatory symmetry: eye for eye. The second transforms that logic into tactical matching: student for student.

At this boundary, the safest interpretation is not that the sponsor gives a philosophical theory of justice. The phrase functions operationally. The previous proxy failed; a more appropriate category of opponent will be contracted.

What is striking is the sponsor's **instrumental view of persons**. “Students” appear as a class of asset to be countered with another class of asset.

That contrasts sharply with the previous episode's rescue, where Serika's singularity—her routines, relationships, fear, and safety—was the reason exceptional capabilities were mobilized.

The same story world can therefore contain large asymmetries of power under radically different relational logics:

- person as someone whose agency/safety matters;
- person as a tactical category to be matched.

## 4.9 `専門家に依頼`: coercion becomes contract

The sponsor does not personally escalate the attack. The sponsor decides to `依頼`—commission/request—a `専門家`.

That choice of mechanism matters.

Violence is outsourced.

The phone call makes this explicit when the receiving organization answers as `便利屋68`, advertising universal problem-solving. The exact contractual price, terms, legal status, and internal composition remain unknown. Yet the form is unmistakable: **a client purchases specialized action from an external service provider**.

This is the clearest evidence so far that the Abydos conflict is embedded in a political economy of coercion rather than being reducible to spontaneous gang hostility.

## 4.10 便利屋68 displaces rather than joins the failed proxy

Canonical scene: `BA:main:001:001:007:scene:003`.

The new organization attacks the Helmet Gang itself.

This is crucial. The sponsor is not simply strengthening one existing coalition. The failed intermediary is being replaced.

The new force jokingly calls this `労働から解放` and then clarifies:

> `要するにクビってこと。`

The employment metaphor is comic, but structurally accurate to the episode's logic. The Helmet Gang has failed at its assigned function, and another paid organization takes over.

The declaration:

> `現時刻をもって、アビドスは私たちが引き受けるわ。`

marks a transfer of operational responsibility.

The hidden sponsor's coercive project survives the failure of individual agents because agents are substitutable.

That is a much more serious threat than any single gang leader.

## 4.11 `金さえもらえれば、何でもする`: monetized agency

The organization's self-description is one of E007's most important thematic lines:

> `金さえもらえれば、何でもする……。`

The particle structure makes payment the sufficient condition: **so long as money is paid**, anything can be done.

This does not yet tell us whether the organization literally has no ethical limits; self-presentation may exaggerate. But it clearly establishes a commercial identity in which money legitimates—or at least activates—action.

Placed after E004–E005, the contrast is striking.

Serika works because Abydos is drowning in debt. Her labor is a sacrifice directed toward preserving a community.

The sponsor uses economic capacity to purchase action against that community.

Money is not morally coded in one direction. It is an amplifier of different value systems.

## 4.12 Sensei's post-emergency role contracts back down to a visit

After the high-stakes use of federal information access in E006, Sensei's E007 interaction with Serika is deliberately ordinary.

The first choice is simply:

> `お見舞いに来たよ。`

No command, surveillance tool, strategic plan, or authority claim appears.

This is important for `BA-C010`. Exceptional emergency authority does not automatically expand into post-emergency control. Once Serika is safe, Sensei's role becomes **presence and concern**.

There is also no authored option to scold Serika for working, order her to rest, claim credit for the rescue, or demand gratitude.

That does not prove Sensei would never behave paternalistically elsewhere. It does show that this particular scene chooses a low-control register after the emergency.

## 4.13 Serika still experiences rest as morally difficult

Serika says she cannot stay inactive forever, the others are worried, and she needs to return to work.

This continues the E005–E007 trajectory:

> work despite free day → fight despite danger → contribute immediately after rescue → claim to be fine → collapse → plan return to work.

Her responsibility ethic is admirable but beginning to look potentially self-erasing.

The text has not yet framed this as a diagnosed flaw, and Sensei does not challenge it in E007. Therefore the claim should remain provisional:

> **Serika appears to experience inactivity as difficult to justify while Abydos still needs labor.**

Whether this develops into a broader self-worth problem remains OPEN.

## 4.14 `ありがとう……色々と……`: gratitude becomes explicit

E007 is the first clean post-rescue moment where Serika voluntarily initiates thanks.

She says she realized she had not properly thanked Sensei and offers:

> `あ、ありがとう……色々と……。`

The important fact is not that she becomes suddenly warm. She struggles to say it.

The gratitude therefore has evidentiary weight precisely because it costs her something socially. She chooses to articulate a debt she had previously resisted allowing the adult relationship to create.

This is a genuine relationship transition.

It is **not yet full trust**.

## 4.15 `この借りはいつか必ず返す`: help becomes reciprocal obligation, not dependency

Serika immediately follows gratitude with resistance to unilateral indebtedness:

> `この借りはいつか必ず返すんだから！`

`借り` here is not the school's formal `借金`. It is a personal debt/favor/obligation.

But the semantic echo is too structurally apt to ignore.

Abydos is already organized around repayment language. Serika has internalized repayment so deeply that even rescue is translated into something that must eventually be returned.

Her relationship model is:

> **you helped me → therefore I owe you → therefore the relationship must become reciprocal rather than leaving me as a passive beneficiary.**

This helps explain why adult assistance can feel threatening to her autonomy even when she is grateful. Dependence is morally uncomfortable unless converted into exchange.

The line thus deepens rather than cancels her E004–E005 resistance.

## 4.16 `この程度でアビドスの役に立てたなんて思わないで`: Serika keeps the evaluative standard local

Serika also warns Sensei not to imagine that this single rescue means Sensei has fully proven usefulness to Abydos.

This is significant because gratitude does not transfer evaluative authority.

Serika retains the right to judge what counts as service to the school. Her metric remains **Abydos's needs**, not Sensei's self-image.

This is exactly the kind of relationship that avoids the simplistic poles of rejection or submission:

- she can admit a specific good;
- she can owe a specific favor;
- she can anticipate future contact;
- she can still withhold broader endorsement.

## 4.17 `また明日ね`: continuity becomes voluntary

The line:

> `じゃあ……また明日ね！`

is small but important.

In E005, Serika repeatedly told Sensei to go away. E007 ends with her voluntarily presupposing another encounter tomorrow.

This is not a confession of trust. It is stronger evidence of **accepted continuity**.

Sensei is becoming someone Serika expects to remain in the committee's social horizon.

## 4.18 The hesitant `先生` is tonal softening, not a first lexical address

Serika ends:

> `えっと、せ……`
>
> `……先生。`

It would be analytically careless to say this is the first time she has ever called Sensei `先生`; she has used the term earlier.

What changes is pragmatic context and delivery. Here the address follows gratitude and `また明日`, with hesitation foregrounded by the script.

The evidence supports:

> **a softened, self-conscious use of an already established address term**.

It does not by itself support “Serika is now fully dere,” “Serika has accepted Sensei unconditionally,” or “her earlier distrust was fake.”

---

# 5. Character-state analysis

## 5.1 Serika — from defended independence to reciprocal recognition

E007 materially changes Serika's state without overturning it.

### Trait/state now supported

- **High responsibility drive:** she tries to resume ordinary obligations despite significant injury.
- **Vulnerability denial/minimization:** she says she is `ピンピン` immediately before collapsing.
- **Gratitude capacity:** she voluntarily initiates thanks once she has had time to recover.
- **Reciprocity norm:** assistance becomes a `借り` she must repay.
- **Abydos-centered judgment:** one rescue does not automatically satisfy her standard for “helping Abydos.”
- **Relational softening:** she anticipates seeing Sensei tomorrow and ends in a gentler address register.
- **No explicit full recognition yet:** E005's `まだ先生のこと認めてない` has not been directly reversed.

The best current Serika formulation is therefore:

> **She is no longer merely resisting Sensei's presence; she is beginning to negotiate a relationship in which help can be acknowledged without surrendering autonomy.**

## 5.2 Ayane — operator becomes forensic institutional analyst

Ayane's role continues broadening beyond battlefield operator.

She:

- checks Serika's physical state;
- evaluates recovered material evidence;
- identifies a prohibited weapon model;
- distinguishes gang possession from gang procurement ability;
- links the weapons question to the persistence of attacks.

Her competence increasingly spans operations, records, institutional facts, and causal investigation.

This is strong counterevidence to any model of the committee as merely brave but administratively naïve students.

## 5.3 Nonomi — affective warmth and analytical reasoning coexist

Nonomi's E007 contribution is easy to underweight because her surface register remains bright.

But she proposes the decisive investigative step: analyze the component's `流通ルート` to find the entity behind the Helmet Gang.

The scene therefore reinforces a pattern already visible in her crisis behavior: her high-affect social presentation is compatible with concrete reasoning and decisive action.

## 5.4 Hoshino — humor, rest judgment, and strategic patience

Hoshino performs three functions:

1. correctly normalizes Serika's need for rest after extreme injury;
2. preserves the stalker joke, keeping prior social friction narratively alive;
3. accepts the supply-chain investigation with `じっくり調べてみよっかー`.

The last point is important. E003 showed Hoshino willing to seize an immediate tactical opportunity. E007 shows she can also accept slower investigation when the problem is structural.

Her strategic baseline is therefore not simply aggression or laziness. It includes tempo selection.

## 5.5 Sensei — emergency actor returns to ordinary care

E007 adds little new raw capacity to Sensei's profile. That is precisely why it matters.

After the extraordinary central-network use in E006, Sensei's next Serika interaction is reduced to:

- visiting;
- asking/indicating concern;
- expressing relief.

There is no appropriation of her recovery or of the committee's investigation.

This strengthens the idea that exceptional power is **situationally activated**, not the total content of Sensei's relationship to students.

## 5.6 Unknown sponsor — first secure structural baseline

A new entity-level state can now be opened without assigning a normalized personal identity.

The hidden sponsor:

- is situated in a high-rise office context;
- has enough resource control to say a main battle tank was sent;
- judges the Helmet Gang as an inferior/failed proxy;
- adapts strategy after failure;
- treats students instrumentally as a tactical category;
- commissions `便利屋68` as a specialist replacement.

Exact name, institution, motive, age, legal status, and relationship to Abydos's debt remain OPEN at the promoted canonical layer.

## 5.7 便利屋68 — organizational baseline only

At E007's local boundary, `便利屋68` can be characterized securely as an organization that:

- accepts commissioned work;
- advertises broad problem-solving capability;
- defeats the Helmet Gang;
- replaces the gang in the Abydos operation;
- self-describes through payment-contingent action.

Individual member monographs should **not** be opened from E007 because the promoted canonical person mappings for the scene remain unresolved. E008 may repair that boundary.

---

# 6. Relationship-state analysis

## 6.1 Sensei ↔ Serika — rejection becomes negotiated reciprocity

The relationship has now moved through a clear sequence:

> **outsider rejection → unwanted pursuit → emergency rescue → explicit gratitude → declared personal debt → anticipated future contact**

The correct transition is not “Serika now trusts Sensei.”

It is:

> **Serika now recognizes specific positive obligations created by Sensei's conduct and permits the relationship to continue, while maintaining her right to judge Sensei's broader value to Abydos.**

That is a much more interesting and more textually defensible state.

## 6.2 Serika ↔ Countermeasures Committee — care is now bidirectional and embodied

E006 revealed Serika's terror at being misread as a deserter or betrayer. E007 begins with the other members physically caring for her and worrying about her condition.

Her statement that Ayane and everyone else are worried shows that she registers this care as an obligation to return, not merely something to receive.

The ensemble remains reciprocal, but Serika may be translating others' concern too quickly into pressure to become useful again. That possibility should be tracked.

## 6.3 Helmet Gang ↔ hidden sponsor — proxy relationship now strongly supported

From the committee's perspective this remains an inference. From the reader's cutaway, the relation is substantially clearer.

The sponsor says a main battle tank was sent and evaluates the gang's performance. This supports a model of the gang as an externally supplied proxy or operational intermediary.

The exact contract—payment, coercion, command hierarchy, or informal sponsorship—is not stated and should remain OPEN.

## 6.4 Hidden sponsor ↔ 便利屋68 — explicit commissioned relationship

The sponsor calls `便利屋68` and says work is being requested. The group later takes over the Abydos matter.

This is the first secure contractor relationship in the Abydos arc.

Again, exact terms remain unknown, but the functional relationship is no longer speculative:

> **client/sponsor → commissioned specialist organization**.

## 6.5 便利屋68 ↔ Helmet Gang — competitive replacement

The new organization does not coordinate with the gang. It violently removes them from the operation and uses employment language to describe the transfer.

This means the opposition to Abydos is not a stable interpersonal coalition. It is a layered system in which agents can compete and be replaced while the higher-level objective persists.

---

# 7. Institutional-state analysis

## 7.1 Abydos's threat model changes from actor-centric to network-centric

Before E007, the Helmet Gang could still be modeled as the primary hostile institution confronting Abydos.

After E007, that is inadequate.

The minimum current threat architecture is:

> **hidden resource-holder/sponsor → weapons/logistics pipeline → disposable or replaceable coercive agents → pressure on Abydos**

The Helmet Gang is one node, not the whole system.

## 7.2 Kivotos has a meaningful prohibited-weapons category

Ayane's `キヴォトスでは使用が禁止されている違法機種` is the first explicit evidence in this arc of a weapons-regulatory distinction.

We do not yet know:

- who enacts the prohibition;
- whether possession, use, sale, or all three are banned;
- what enforcement body exists;
- how widespread black-market access is;
- whether exceptions exist.

But the prohibition itself is TEXTUAL FACT.

This opens a future institutional research line around law, arms circulation, and enforcement capacity.

## 7.3 Material provenance becomes a route to political provenance

The committee's reasoning treats supply chains as political evidence.

The logic is:

> **identify object → identify prohibition → identify procurement mismatch → reconstruct circulation → infer backer**.

This is institutionally sophisticated and should be preserved as an Abydos capability, not attributed to Sensei.

## 7.4 便利屋68 introduces commercialized coercive service

At this point `便利屋68` should enter the institution ledger as a **paid general-service organization functioning here as a coercive contractor**.

Do not yet collapse it into a generic “criminal gang.” Its own self-description centers service-for-payment, and its behavior toward the Helmet Gang is organizationally distinct from simple territorial delinquency.

## 7.5 The hidden sponsor's exact institutional home remains unresolved

The convenience rendering labels the sponsor `カイザーPMC理事`, but the promoted canonical layer retains `？？？` and no normalized person ID.

Therefore the current institutional ledger should use a neutral label such as **UNKNOWN ABYDOS SPONSOR** and record the convenience label as a source-resolution note rather than current-authority identity.

This is a provenance discipline issue, not skepticism that the convenience label may ultimately be correct.

---

# 8. Sensei role, authority, and ethics

E007 is valuable precisely because it occurs **after** a justified emergency exception.

If the narrative intended emergency rescue to establish unlimited adult entitlement, this would be the place to show Sensei taking over Serika's recovery or the committee's investigation.

It does not.

Sensei is absent from the supply-chain analysis in canonical scene 1 (`sensei_present: false` in the promoted chunk). Ayane and Nonomi generate the investigative path.

When Sensei later appears, the interaction is private/low-stakes and caring. The choice interface offers only:

- `お見舞いに来たよ。`
- `それは良かった。`

This supports a bounded model:

> **exceptional intervention during coercive emergency → reversion to ordinary relational presence once immediate coercion ends**.

Two cautions remain.

First, E005's boundary violation is not erased. Hoshino's stalker joke actively preserves it in continuity.

Second, Sensei does not challenge Serika's desire to return quickly to work despite her collapse. This can be read as respecting her agency, but it may also be under-protective. E007 does not adjudicate that tension.

The best current ethics formulation remains:

> **Sensei is neither sovereign rescuer nor perfectly consent-sensitive saint; the emerging norm is situational discretion whose legitimacy depends on purpose, proportionality, reversibility, and continued student agency.**

---

# 9. Japanese-language and voice analysis

## 9.1 `違法機種`

`違法` is stronger than “unusual” or “restricted-looking.” Ayane is explicitly classifying the recovered model through a legal/normative category.

This is institutional language, not combat slang.

## 9.2 `流通ルート`

`流通` concerns circulation/distribution. `ルート` specifies path/channel.

Nonomi's phrase frames weapons not as isolated objects but as things moving through a network. It is an economically and logistically inflected way of thinking about violence.

## 9.3 `裏にいる存在`

Literally, the “existence/entity behind” the gang.

The expression deliberately leaves identity open while strongly asserting hidden agency. It is well suited to the committee's epistemic position: enough evidence for a backer hypothesis, insufficient evidence for a name.

## 9.4 `格下のチンピラごとき`

The hidden sponsor's language is contemptuous twice over.

- `格下` marks inferior rank/status.
- `ごとき` dismissively minimizes the referent.

The gang is not treated as a respected partner. This linguistic register supports the interpretation of replaceable proxy status.

## 9.5 `目には目を、生徒には生徒を`

The line adapts a familiar symmetry formula into tactical categorization.

Its function here is not legal-philosophical proportionality. It is operational matching: the sponsor decides that the target category “students” should be countered with “students.”

This instrumental grammar should be tracked if later sponsor dialogue repeats it.

## 9.6 `専門家に依頼`

`依頼` is commission/request rather than command in the narrow military sense. Combined with `専門家`, it gives the escalation a service-market form.

## 9.7 `労働から解放` / `クビ`

The new organization's employment jokes recode violent displacement as labor-market turnover.

`解放` sounds grandiose/beneficent; `クビ` brutally clarifies the practical meaning: firing.

The contrast creates comedy while reinforcing the contractor logic.

## 9.8 `金さえもらえれば`

The `さえ～れば` construction makes receipt of money the sufficient threshold condition in the organization's self-description.

A cautious paraphrase is:

> **if we get paid, that is enough for us to act**.

Whether this is literal ethical nihilism or stylized branding remains to be tested.

## 9.9 `借り` / `返す`

Serika's `借り` is personal obligation, not the formal institutional `借金` of E004.

But `返す` belongs to the same repayment semantic field. Her social ethics and Abydos's financial crisis now rhyme linguistically:

- school owes money;
- Serika works to repay interest;
- Sensei helps Serika;
- Serika insists the favor must be repaid.

This supports a motif of **reciprocity/debt as a language for relationships**, without collapsing personal gratitude into financial liability.

## 9.10 `また明日ね`

This is an ordinary future-oriented leave-taking, and that ordinariness is the point.

After repeated earlier rejection, Serika voluntarily assumes the relationship continues tomorrow.

## 9.11 Hesitant `先生`

The address term is not new. The hesitation is.

Voice analysis should therefore code the change as **pragmatic softening/self-consciousness**, not lexical adoption.

---

# 10. Motifs, symbols, and callback structure

## 10.1 Debt and repayment move from institution to relationship

The debt motif now has three layers:

- `借金`: school-level financial obligation;
- wage labor/interest: personal time converted into institutional repayment;
- `借り`: interpersonal obligation created by care/rescue.

Serika is the point where these layers meet.

## 10.2 Money as morally neutral amplifier

Money preserves Abydos through Serika's labor and can also fund violence against it through contracted specialists.

The text is not saying “money is evil.” It is showing that economic capacity can be attached to very different ends.

## 10.3 Proxy replacement

E007 introduces a motif of **replaceable intermediaries**.

The Helmet Gang's defeat does not end the pressure because the objective exists above them. This changes how future victories must be evaluated: destroying a proxy may not remove the system producing proxies.

## 10.4 Wreckage as truth-bearing residue

Destroyed weapons leave parts. Parts carry model identity. Model identity carries legal and distribution information. Distribution information can reveal hidden actors.

Violence therefore produces evidence against its own hidden architecture.

## 10.5 Recovery and the refusal to remain still

Serika's collapse and subsequent desire to return to work continue the motif of responsibility exceeding bodily limits.

This should remain a Serika-specific line until later evidence establishes a broader series pattern.

## 10.6 Comedy as continuity rather than erasure

The “stalker” joke survives the rescue. The employment jokes accompany violent organizational replacement. Serika's gratitude is wrapped in defensive anger.

Comedy repeatedly sits *beside* serious state changes without canceling them.

---

# 11. Violence, ethics, power, and political economy

E007 materially expands the ethics-of-violence analysis because the main new information concerns **who enables violence** rather than only who pulls the trigger.

The Helmet Gang's previous attacks now have at least three layers of responsibility to investigate:

1. direct actors who commit assault/kidnapping;
2. suppliers or sponsors who provide capabilities the direct actors cannot obtain themselves;
3. commissioners who choose to continue the project by hiring replacement specialists.

This is a classic responsibility-distribution problem even before exact legal categories are known.

The hidden sponsor attempts to gain the benefits of coercion through intermediaries. Whether this arrangement is intended to provide deniability is not stated; therefore “plausible deniability” should remain a hypothesis, not fact. But the use of replaceable agents clearly distances resource-holder from frontline violence.

`便利屋68` adds a second problem: **contract does not neutralize agency**. The organization acts for money, but paid action remains action. If later material shows knowledge, coercion, deception, or limits on the contract, moral responsibility can be refined. E007 alone supports only the baseline that payment motivates accepted work.

The most important ethical contrast is with Sensei.

Both Sensei and the hidden sponsor possess capacities that Abydos itself lacks. Yet E006–E007 show opposite uses:

- Sensei accepts risk to retrieve information needed to restore a coerced student's agency;
- the sponsor distributes weapons and hires agents to continue coercive pressure after the first proxy fails.

Thus **capacity is not legitimacy**.

Legitimacy must be argued from purpose, relation to persons, proportionality, accountability, and what happens to the agency of those affected.

This is one of the strongest extensions yet of the Prologue's authority thesis.

---

# 12. Threat architecture: what is actually “new”?

The episode title should be answered with a qualified formulation.

### Not entirely new

The hidden sponsor appears to have been structurally relevant before E007, because the sponsor says a main battle tank had already been sent. The Helmet Gang's abnormal equipment therefore belonged to a preexisting support relationship.

### Newly discovered by the committee

The students now possess material evidence that their opponent's capability exceeds independent gang procurement and can begin tracing the supply route.

### Newly shown to the audience

The audience sees the sponsor's existence, dissatisfaction, and contracting decision.

### Newly deployed on the surface

`便利屋68` becomes the replacement operational actor.

Therefore the episode's “new threat” is best modeled as:

> **a new visible agent exposing an older hidden system**.

This matters for future reading. E008 should not be approached as if `便利屋68` spontaneously decided to attack Abydos for purely personal reasons. At the E007 boundary, the organization has entered through a commission from an unseen sponsor.

---

# 13. Competing readings and counterevidence

## Reading A: “The Helmet Gang was the real enemy, and 便利屋68 is just the next enemy.”

**Against:** E007 explicitly establishes prohibited arms outside the gang's procurement capacity, an unseen supplier claiming to have sent a main battle tank, and a sponsor who hires the replacement force.

**Verdict:** insufficient. The gang is an operational layer, not the complete threat structure.

## Reading B: “The new sponsor identity is now fully established as カイザーPMC理事.”

**For:** the convenience rendering supplies that label.

**Against:** the promoted canonical scene/utterance layer still stores the speaker as `？？？` with no normalized person ID.

**Verdict:** **SOURCE-LAYER UNRESOLVED**. Preserve the convenience label as a candidate/metadata fact; do not use it yet as the basis for detailed person-specific synthesis.

## Reading C: “Serika has now completely accepted Sensei.”

**For:** she voluntarily thanks Sensei, says `また明日ね`, and ends with a softened `先生`.

**Against:** she explicitly frames the help as a debt to repay, warns Sensei not to overclaim usefulness to Abydos, and never says that the earlier `認めてない` judgment has been reversed.

**Verdict:** **REVISE DOWNWARD**. Relationship softening and specific gratitude are established; full acceptance remains OPEN.

## Reading D: “Serika's independence was merely tsundere theater.”

**Against:** E005 showed real wage labor and interest repayment; E006 showed deep committee-identification; E007 shows continued work pressure and a reciprocity ethic.

**Verdict:** REJECT. Tsundere-coded expression may be part of presentation, but the underlying autonomy ethic is substantively grounded.

## Reading E: “Sensei's rescue proves adults are what Abydos really needs.”

**Against:** E007's crucial supply-chain discovery is generated by Ayane/Nonomi without Sensei present; the hidden opponent itself also appears to possess superior external resources. External capacity is not inherently benevolent.

**Verdict:** REJECT as simplification. The story is testing *uses and relationships of power*, not merely celebrating adult capacity.

## Reading F: “Paid contractors are automatically less responsible because they are only doing a job.”

**Against:** E007 gives no such moral exemption. The organization self-identifies its willingness to act for payment and violently displaces the prior proxy.

**Verdict:** unsupported. Contract explains mechanism/motivation, not exculpation.

## Reading G: “Sensei should have ordered Serika to stop working after her injury.”

**Possible argument:** her collapse and immediate return-to-work impulse suggest risk of self-neglect.

**Counterargument:** E007 gives no medical assessment beyond rest and no evidence that Sensei possesses or should exercise unilateral authority over her schedule.

**Verdict:** OPEN ethical tension. The scene supports bounded concern; it does not adjudicate the ideal degree of protective paternalism.

---

# 14. Cumulative ledger deltas

## Character delta

- **Serika:** add post-rescue physical consequence, explicit gratitude, reciprocity/debt framing, continued work-pressure, and voluntary continuity with Sensei; do not mark full `認める` resolution.
- **Ayane:** add forensic/procurement analysis and prohibited-weapons identification.
- **Nonomi:** add supply-route/backer inference.
- **Hoshino:** add rest judgment and deliberate slow-investigation tempo.
- **Sensei:** add post-emergency low-control visit/concern; no new exceptional capacity.
- **UNKNOWN ABYDOS SPONSOR:** open structural entity with resource supply, proxy evaluation, and contracting role; normalized identity unresolved.
- **便利屋68:** organizational baseline only; individual member mapping deferred.

## Relationship delta

- **Sensei ↔ Serika:** transition from unresolved post-rescue status to explicit gratitude + reciprocal obligation + accepted continuity; full trust remains open.
- **Helmet Gang ↔ hidden sponsor:** strong reader-level evidence of externally supplied proxy relationship.
- **hidden sponsor ↔ 便利屋68:** explicit commission relationship.
- **便利屋68 ↔ Helmet Gang:** competitive/violent replacement.

## Institutional delta

- add Kivotos prohibited-weapons category;
- add arms/procurement circulation as an investigative dimension;
- add UNKNOWN ABYDOS SPONSOR as distinct threat node;
- add `便利屋68` as commissioned paid service/coercive organization;
- revise Helmet Gang from standalone local threat to externally supplied/replaceable intermediary.

## Sensei ethics delta

- strengthen post-emergency boundedness: exceptional rescue authority recedes into ordinary care;
- preserve E005 consent counterevidence;
- do not infer post-rescue entitlement from Serika's gratitude.

## Language delta

Add high-priority terms:

- `違法機種`;
- `流通ルート`;
- `裏にいる存在`;
- `格下のチンピラごとき`;
- `主力戦車`;
- `目には目を、生徒には生徒を`;
- `専門家に依頼`;
- `労働から解放`;
- `クビ`;
- `金さえもらえれば、何でもする`;
- `借り` / `返す`;
- `また明日ね`.

## Motif delta

Add/strengthen:

- outsourced/proxy violence;
- money as morally nonuniform capacity amplifier;
- repayment as both institutional and relational language;
- wreckage/provenance revealing hidden power;
- visible threat versus structural sponsor;
- injury and over-responsibility;
- replaceable intermediaries.

---

# 15. Claim-revision ledger delta

| Claim ID | E007 transition | Current effect |
|---|---|---|
| BA-C001 | **STRENGTHEN lightly** | responsible adulthood includes post-emergency ordinary care without claiming the committee's investigation or Serika's recovery as adult property |
| BA-C002 | **STRENGTHEN / partial Serika resolution** | Serika now offers explicit gratitude and accepts future contact, but full `認める`/trust remains OPEN and reciprocity remains central |
| BA-C003 | **STRENGTHEN** | the committee independently detects and investigates the deeper threat while Schale remains a supporting relation rather than replacement analytic authority |
| BA-C004 | **PRESERVE** | no new Sensei capability; E007 instead shows that outside resource asymmetry can also empower hostile sponsors |
| BA-C005 | **PRESERVE REJECTED; counterevidence strengthened** | Ayane/Nonomi identify the supply-chain problem without Sensei present; adult/external capacity is not uniquely competent or inherently benevolent |
| BA-C006 | **PRESERVE REJECTED; counterevidence strengthened** | student institutional analysis identifies illegal equipment, procurement mismatch, and a route to the hidden backer |
| BA-C007 | **STRENGTHEN / maintain complication** | justified emergency intervention is followed by low-control ordinary care; E005 boundary counterevidence remains valid and is not retroactively erased |
| BA-C008 | **STRENGTHEN** | the two singleton choices narrowly author care and relief rather than branching, joking, or dominance |
| BA-C009 | **PRESERVE** | no material new technical-system ontology; physical provenance rather than digital system is the main evidentiary tool |
| BA-C010 | **STRENGTHEN** | exceptional emergency power demonstrably recedes after rescue; Sensei does not convert successful intervention into governance over Serika or the committee |
| BA-C011 | **STRENGTHEN** | Serika's gratitude recognizes specific adult usefulness without collapsing student evaluative agency or establishing supremacy |
| **BA-C012** | **OPEN — NEW** | **Abydos's violent pressure is organized through economically mediated proxy/contract structures: an external sponsor supplies otherwise inaccessible military capability and replaces a failed local intermediary with a paid specialist organization. Exact sponsor identity, motive, and contract structure remain unresolved.** |

`BA-C012` is opened because E007 establishes a genuinely distinct analytical responsibility not reducible to the adult-legitimacy claims: the **political economy and proxy architecture of coercion against Abydos**.

---

# 16. Open questions after E007

1. Who is the hidden sponsor at the **promoted canonical** identity layer?
2. Why is Abydos being targeted persistently?
3. What is the relationship, if any, between the hidden sponsor and Abydos's debt/creditor structure?
4. What exactly makes the recovered model `違法`, and who regulates such weapons?
5. Through what `流通ルート` did the Helmet Gang receive prohibited equipment?
6. Was the Helmet Gang paid, commanded, supplied opportunistically, or connected through some other arrangement?
7. What are the exact terms of the `便利屋68` commission?
8. Does `便利屋68` understand the full context of Abydos, or only the client's job request?
9. Is `金さえもらえれば、何でもする` literal organizational doctrine, branding, bravado, or some combination?
10. Will E008 resolve the individual speaker identities that E007's promoted canonical layer leaves unknown?
11. Does Serika ever explicitly revise `まだ先生のこと認めてない`?
12. Does her `借り` framing evolve into trust, friendship, mentorship, rivalry, or continued transactional reciprocity?
13. Will anyone challenge Serika's tendency to return to labor before fully recovering?
14. Can the committee trace the supply chain before the new contractor acts?
15. Does the new opponent change the conflict's scale, ethics, or merely its competence?

---

# 17. Evidence locator index

| Analytical point | Stable source locator |
|---|---|
| Serika insists she is fine, then collapses | `BA:main:001:001:007:scene:001:u:0004` onward; `DataList[1203]` onward |
| post-rescue praise for Sensei | `scene:001`, principally `DataList[1212]–[1214]` |
| illegal/prohibited weapon classification | `scene:001:u:0014`, `DataList[1217]` |
| gang cannot independently obtain weapons | `scene:001:u:0015`, `DataList[1218]` |
| `流通ルート` / hidden-backer inference | `scene:001:u:0016`, `DataList[1219]` |
| motive question / persistent targeting | `scene:001:u:0017`, `DataList[1220]` |
| hidden sponsor condemns failed proxy | `scene:002:u:0003`, `DataList[1225]` |
| `主力戦車` already supplied | `scene:002:u:0003`, `DataList[1225]` |
| `目には目を、生徒には生徒を` / specialist commission | `scene:002:u:0004`, `DataList[1226]` |
| `便利屋68` answers phone | `scene:002:u:0007`, `DataList[1230]` |
| `労働から解放` employment metaphor | `scene:003:u:0015`, `DataList[1254]` |
| takeover of Abydos operation | `scene:003:u:0017`, `DataList[1256]` |
| `金さえもらえれば、何でもする` | `scene:003:u:0024`, `DataList[1266]` |
| Sensei visit choice | `scene:003:choice:001`, `DataList[1274]` |
| Sensei relief choice | `scene:003:choice:002`, `DataList[1278]` |
| Serika initiates thanks | `scene:003:u:0035-0036`, `DataList[1282]–[1283]` |
| `この借りはいつか必ず返す` | `scene:003:u:0037`, `DataList[1284]` |
| `また明日ね` | `scene:003:u:0041`, `DataList[1288]` |
| hesitant final `先生` | `scene:003:u:0043`, `DataList[1290]` |
| next-title marker | `scene:003`, `DataList[1294]` |

---

# 18. Source-integrity and provenance audit note

E007 does **not** repeat the same kind of impossible self-address corruption seen in E006 for its core Abydos material. Ayane, Nonomi, Hoshino, and Serika's normalized mappings in scene 1 are internally coherent, and the Serika visit material in scene 3 is clean.

The main integrity issue is different: **identity resolution across source layers**.

The convenience Markdown includes explicit names for several new actors, while the promoted canonical utterance layer stores the corresponding speakers as unresolved `？？？` and the story-level `person_ids` omits those individuals. Because the project method privileges reversible promoted canonical evidence, individual-specific analysis for those new speakers is deferred.

This does not prevent analysis of:

- the existence of a hidden sponsor;
- that sponsor's explicit statements about supplied armor and hiring specialists;
- the existence and self-declared commercial identity of `便利屋68`;
- the organization's replacement of the Helmet Gang.

No separate `SOURCE_AUDIT` artifact is created at E007 because the discrepancy is currently containable inside the established source-integrity infrastructure and this deep reading. If E008 fails to normalize the newly introduced actors despite explicit main-story identification, a dedicated attribution/cross-layer audit will become more strongly warranted.

---

# 19. Conclusion and next boundary

E007 is a structural hinge.

The Abydos story has moved from:

> **five students trying to keep a dying school alive while fighting local attackers**

into:

> **five students discovering that the local attackers are nodes in a larger economic and logistical system capable of supplying prohibited armor and replacing failed proxies with paid specialists**.

At the same time, the Serika/Sensei relationship moves without collapsing its tension. Serika can now say thank you. She can imagine tomorrow with Sensei still present. She can soften the way she says `先生`. But she also converts the rescue into a `借り` she must repay and refuses to let one dramatic intervention settle the question of what it means to help Abydos.

That combination is analytically important.

The story is not resolving autonomy against dependence by choosing one side. It is building a world in which durable community requires receiving help **without losing the capacity to answer, reciprocate, evaluate, and act**.

E007 also reveals the darker mirror of that principle. Capacity can be exchanged through relationships of care—or purchased through relationships of instrumental contract. The same broad resources that can rescue a student can, under different institutions and motives, supply tanks and hire proxies.

The next mandatory sequential unit is:

- `BA:main:001:001:008`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E008_DEEP_READING.md`;
- 第8話「便利屋参上！」;
- source metadata: **274 records, 224 utterances, 2 normalized choice groups, 1 canonical scene**.

E008 should test:

1. whether the promoted person mappings now resolve `便利屋68`'s members;
2. whether the organization understands the sponsor's larger objective or only a paid task;
3. how commercial self-presentation translates into actual behavior;
4. whether the Countermeasures Committee recognizes the proxy replacement;
5. whether Serika's new gratitude changes her conduct toward Sensei in group interaction;
6. whether `BA-C012` should be strengthened, narrowed, or revised after direct contact with the new contractor.

No checkpoint or side-source backfill is warranted at the E007 boundary.
