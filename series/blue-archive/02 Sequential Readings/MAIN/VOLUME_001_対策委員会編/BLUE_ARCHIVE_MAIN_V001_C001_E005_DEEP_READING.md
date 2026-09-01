---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E005
generation: V1
status: active_provisional
source_boundary: Canonical Japanese main-story unit BA:main:001:001:005, 対策委員会編 第5話『セリカの平凡な一日』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-16
---

# BLUE ARCHIVE — MAIN V001 C001 E005 DEEP READING
## 対策委員会編 — 第5話「セリカの平凡な一日」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the seventh canonical main-story object in analytical order and the fifth object in `対策委員会編`:

- story ID: `BA:main:001:001:005`;
- analytical scope: `MAIN_V001_C001_E005`;
- source title: `第5話;セリカの平凡な一日`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第5話`;
- raw group ID: `11050`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- record count: **179**;
- promoted utterance count: **133**;
- normalized choice groups: **8**;
- canonical scene count: **1**;
- source person IDs represented in the recovered object: Serika, Nonomi, Ayane, Shiroko, Hoshino, plus raw non-student labels `マスター`, `ヘルメット団A`, and `ヘルメット団B`;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_005.md`;
- complete source-side convenience rendering: `05話_セリカの平凡な一日.md`.

The single canonical scene begins at location:

- `アビドス住宅街・45ブロック地区`;
- stable scene ID: `BA:main:001:001:005:scene:001`;
- raw text-bearing span: principally `ScenarioScriptMain1ExcelTable.json:DataList[900]–[1076]`, with gaps for control and branch records.

The promoted utterance layer independently returns exactly **133** objects for `BA:main:001:001:005`; the first text-bearing record is `DataList[900]` and the final next-title object is `DataList[1076]`.

### Choice-space

The source rendering exposes eight normalized choice groups in order:

1. `おはよう。`
2. `セリカちゃんは、これから学校？`
3. `追いかける。`
4. `追いかける。`
5. `どうも。`
6. `ノノミの隣に座る。 / シロコの隣に座る。`
7. `逃げる。`
8. `帰る。`

Several additional Sensei intentions are communicated indirectly because Serika echoes or answers an unprinted question—for example, she reacts to an implied suggestion that they go to school together and an implied question about her destination. These should not be promoted into formal choices absent a normalized choice object.

### E005 source-integrity note

E005 is materially cleaner for its central Serika material than E002–E004. The core opening, post-work monologue, and abduction sequence have internally coherent person mappings. The restaurant middle section contains many `character_narration` records associated with branch-selection groups; person IDs remain available and coherent, but those records should be understood as route-conditioned scene text rather than proof that every displayed line belongs to one single realized seating branch.

No E005 claim below requires silently repairing the E002–E004 speaker-label corruption. The earlier anomaly remains a corpus-level caution, but it should not be projected onto clean E005 Serika lines without evidence.

### Local-information lock

Available prior analytical authority is limited to:

- the canonical two-unit Prologue and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E002_DEEP_READING.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E003_DEEP_READING.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E004_DEEP_READING.md`.

No E006 or later main-story unit, bond story, MomoTalk, event, character package, relationship bundle, adaptation, wiki, or franchise hindsight is used to settle the abduction's motive, Serika's later response, or the identity of any possible supporting force.

---

# 1. Story placement and local chronology

E004 ended with an unresolved disagreement about adult involvement.

Hoshino and Shiroko argued that Sensei had earned enough trust to hear the committee's private burden. Serika agreed that Sensei had helped, but still called Sensei a `部外者`, invoked the absence of adult concern for Abydos, and rejected adults inserting themselves `今更`. Sensei then committed to remain with the committee rather than taking the offered exit.

E005 does not resolve this dispute through a speech. It moves into Serika's daily life.

That is analytically useful because it tests what her objection means **when she is not arguing in committee**.

The episode's movement is:

> **Serika rejects social familiarity with Sensei → Sensei follows despite her refusal → Serika reveals a hidden part-time job → the committee turns the workplace into a comic social encounter → Serika returns to solitary work/commute → her private monologue links wages directly to debt interest and school restoration → hostile actors identify her specifically as a committee member → Serika is overwhelmed and abducted alive**

The title `セリカの平凡な一日` is therefore ironic without being false.

The first two-thirds genuinely depict ordinary life: morning movement through the neighborhood, a part-time job, customer service, friends eating ramen, money anxiety, teasing, and getting off work. Yet “ordinary” life in present Abydos is already shaped by the institution's crisis. Serika works because the school owes money. She notices depopulation and declining security on the way home. Finally, her membership in the committee makes her a target for organized capture.

The episode thus translates the E004 macrostructure into a personal chain:

> **institutional debt → individual student labor → social privacy/self-reliance → movement through a declining district → personal exposure to conflict**

---

# 2. Narrative reconstruction

Sensei encounters Serika in Abydos's residential 45-block area in the morning. Sensei greets her. Serika immediately rejects the familiarity and says she still has not accepted Sensei: `私、まだ先生のこと認めてないから！`

She mocks Sensei for wandering around leisurely in the morning and says she herself is busy. When Sensei asks whether she is going to school, she objects to being called `セリカちゃん`, says what she does is none of Sensei's business, and calls Sensei an example of a `ダメな大人` for wandering around in the morning. She explains that it is a free-attendance day and refuses to say where she is going.

The interface then requires Sensei to `追いかける`.

Serika protests and explicitly calls the behavior `ストーカー`. To make Sensei stop, she finally reveals that she is going to a part-time job because she needs to earn even a little money. She again asks not to be followed.

The interface requires `追いかける` a second time.

Serika becomes angrier, calls Sensei a `ダメ大人`, tells Sensei to go away repeatedly, and runs off.

The scene then shifts to her workplace, Shibaseki Ramen. Her speech changes immediately into professional customer-service language. She welcomes customers, seats them, and handles an extra-noodle order. The committee then arrives as a group with Sensei. Serika is horrified.

Hoshino explains that Sensei is not responsible for locating the workplace: if Serika has a part-time job, this is the obvious place the group would guess. The shop master recognizes them as Abydos students and reminds Serika to focus on taking orders.

The restaurant sequence becomes ensemble comedy. Nonomi and Shiroko both invite Sensei to sit beside them; the choice interface permits either seat. Route-conditioned text has Serika policing how closely they crowd Sensei and insisting that everyone use the abundant empty seating rather than cluster pointlessly.

The group teases Serika about her uniform and learns that she started the job around a week earlier. Her friends had noticed that she sometimes disappeared but did not know why.

Serika then takes everyone's ramen order. Hoshino calls Shibaseki Ramen an `アビドス名物`—an Abydos specialty—and encourages Sensei to order freely.

Serika's attention immediately returns to money. She asks whether everyone can actually pay and whether they intend to make Nonomi treat them again. Nonomi says she could do so because her card still has room below its limit. Hoshino instead decides that Sensei will surely pay.

Sensei selects `逃げる`, but Hoshino catches Sensei. Hoshino then invokes the `大人のカード`, joking that this is its moment. Ayane notes that this does not seem like a place where such a card should be necessary. Hoshino reframes payment as a teacher's opportunity to fill the stomachs of cute students.

Nonomi quietly attempts to give Sensei something with which to pay, but the narration then states that Sensei settles the bill for everyone. The group thanks Sensei. Serika angrily ejects them for disrupting her work.

After the group leaves, Serika finally finishes her shift. Alone, she complains that everyone was noisy and that they were making too much of Sensei. She suspects Hoshino deliberately brought Sensei because of the previous day's disagreement and vows that she will not yield so easily.

Unseen Helmet Gang members have already identified her as a member of the Abydos Countermeasures Committee and plan to capture her in the next block.

Serika continues home through the declining district. She notices that more people have disappeared than before and that public security seems worse. Her private thought then states her own purpose with unusual clarity:

> `私たちが頑張らないと……そして学校を立て直さないと……。`

She immediately converts that goal into personal finance:

> `とりあえずバイト代が入ったら、利息の返済に充てて……。`

The institutional debt is therefore not abstract to her. Her wages are mentally earmarked for interest.

The Helmet Gang confronts her by full name. Serika recognizes them and, already in a bad mood, chooses immediate violent engagement, saying she will make sure they can never enter the area again. She is then struck from behind or from another direction and realizes they planned the encounter as an ambush.

Serika identifies the sound of heavy fire as possibly a `Flak41改` and realizes there is fire support from somewhere. The scale of the force is much greater than she expected. She loses consciousness.

The attackers explicitly order her captured and later state that there is no point if she is not kept alive: `生かさなければ意味がない`. They load her into a vehicle and head for a rendezvous point.

The next-title marker is `次回;救出作戦！`.

---

# 3. Central thesis

The strongest E005 thesis is:

> **Serika's resistance to Sensei is rooted not in lack of commitment but in an ethic of self-earned responsibility: her “ordinary” life already includes hidden wage labor whose proceeds she intends to devote to Abydos's interest payments. The episode simultaneously refuses to romanticize self-reliance. Sensei's comic pursuit crosses Serika's expressed social boundary, while Serika's own solitary assumption of institutional burden leaves her moving alone through a depopulating, insecure district where her committee membership makes her a target for abduction.**

This produces four major refinements.

First, E004's debt becomes **embodied labor**. The school owes ¥962.35 million, but E005 shows what that means at one human scale: a first-year student spends a free-attendance day working in a ramen shop and mentally allocates wages to monthly interest.

Second, Serika's anti-adult stance is revealed as inseparable from a positive moral identity:

> `私たちが頑張らないと`

Her emphasis is not simply “I dislike Sensei.” It is “**we have to be the ones who keep trying**.” Adult intervention threatens a self-conception built from having carried the school without reliable adult attention.

Third, E005 complicates any idealized Sensei ethics. Sensei is not uniformly consent-sensitive. The authored interface twice requires `追いかける` after Serika tells Sensei not to follow. The scene treats this as comic persistence, but Serika's repeated refusals and `ストーカー` language are textually real. Responsible adulthood in Blue Archive is therefore not being staged as moral saintliness.

Fourth, Serika's abduction exposes the danger in a purely self-reliant response to institutional collapse. The episode does **not** prove that “Serika was wrong to want independence” or that “she therefore needed an adult.” The ambush is a hostile group's intentional act. But structurally it does show that individual determination cannot by itself neutralize organized violence and deteriorating public security.

The resulting model is more demanding than either independence or rescue fantasy:

> **personal commitment matters, outside help can matter, and both still require negotiated trust, boundaries, and collective capacity.**

---

# 4. Scene-by-scene close reading

Because E005 is one canonical scene, the subsections below track internal movements within `BA:main:001:001:005:scene:001`.

## 4.1 `まだ先生のこと認めてない` — Serika's rejection is real but grammatically non-final

Stable evidence: `u:0004-0010`, raw `DataList[906]–[913]`.

Serika's most direct opening line is:

> `私、まだ先生のこと認めてないから！`

The important word is `まだ`.

It means **still / not yet**. The line is not equivalent to a permanent categorical statement such as “I will never accept you.” Serika asserts a current boundary while grammatically leaving future change possible.

That does not make her secretly accepting. The present-tense rejection is explicit.

The line also refines what `認める` means in this relationship. E004 already established that Serika can be grateful for help without treating Sensei as an insider. Here she refuses social familiarity immediately after a greeting. “Recognition/acceptance” therefore appears to include more than competence evaluation. It involves relational standing.

Sensei has proven useful. Serika has not yet decided that usefulness grants closeness.

## 4.2 Serika's criticism of “lazy adulthood” is projection grounded in real workload

Stable evidence: `u:0006-0014`, raw `DataList[908]–[917]`.

Serika sees Sensei walking around in the morning and says:

> `朝っぱらからこんなところをうろちょろしてたら、ダメな大人の見本みたいに思われるわよ？`

On a purely comic level, she is insulting Sensei.

E005 soon reveals why this specific insult fits her psychology. She is on her way to work on a day when school attendance is optional. She has already organized her time around earning money.

Her contrast is therefore:

> **adult apparently wandering without obligation ↔ student who experiences every available hour as potentially useful labor**.

Whether Sensei is actually idle is not established. Serika's perception is what matters. She measures moral worth through visible contribution because her own environment has trained her to treat nonproductive time as costly.

This makes `ダメな大人` more than generic tsundere abuse. It belongs to the adult-legitimacy vocabulary begun in E004.

## 4.3 The first ethical complication: Sensei follows after an explicit refusal

Stable evidence: choice groups 003–004; Serika `u:0017-0026`, raw `DataList[923]–[936]`.

Serika repeatedly communicates that she does not want Sensei to know where she is going:

- `そんなの教えるわけないでしょ？`
- `ついてこないで！`
- `あっち行ってよ！`

Sensei's authored option is nevertheless:

> `追いかける。`

and then, after she asks again to be left alone:

> `追いかける。`

Serika explicitly calls Sensei `ストーカー`.

The scene is written as comic persistence rather than threat. No later interaction in this unit frames Serika as afraid of Sensei. But analytical seriousness requires separating **tone** from **conduct**.

At the conduct level, Sensei disregards a clearly expressed social/privacy boundary.

This is important counterevidence against an overly polished version of `BA-C007` or `BA-C011`. Sensei's broader service to Abydos has been restraint-oriented, but the protagonist is not consistently boundary-perfect in personal interaction.

That distinction should remain:

> **macro-level nonappropriation does not guarantee micro-level consent sensitivity.**

The story's comedy may be designed partly to keep Sensei human and socially awkward. It should not erase what Serika actually says.

## 4.4 “I have to earn even a little” converts debt into time

Stable evidence: `u:0021-0023`, raw `DataList[927]–[929]`.

After being pressed, Serika finally reveals:

> `……バイトよ。`

and:

> `少しでも稼がなきゃ！`

E004 described a near-impossible institutional balance sheet. E005 converts it into **student time**.

Debt service is now paid not only in yen but in:

- optional school-day labor;
- concealed schedule changes;
- reduced leisure;
- emotional defensiveness around how time is used.

The phrase `少しでも` is crucial. Serika does not imagine that one part-time job will solve ¥962.35 million. Her labor is valuable because **any contribution is better than none**.

This is structurally tragic without requiring the text to label it tragic. The gap between personal wages and institutional debt is enormous, yet Serika's response is to work harder rather than disengage.

## 4.5 Workplace Serika proves that sharpness is not inability to regulate herself

Stable evidence: `u:0028-0033`, raw `DataList[940]–[945]`.

At Shibaseki Ramen, Serika immediately uses service language:

> `いらっしゃいませ！`

> `空いてるお席にご案内いたしますね！`

> `少々お待ちください！`

This is an important character correction.

Her sharpness around Sensei is not evidence that she simply lacks politeness, self-control, or social competence. She can code-switch into a professional customer-facing register when role expectations require it.

Her confrontational speech is therefore at least partly **relationally specific**.

This matters for character modeling. “Hot-tempered” may be accurate as a trait, but E005 shows that the expression of that trait is highly context-dependent.

## 4.6 The group does not confront Serika with a moral lecture; it invades her ordinary social space with familiarity

Stable evidence: `u:0034-0069`, raw `DataList[946]–[988]`.

The committee arrives as five customers including Sensei.

Serika suspects stalking again, but Hoshino says the group independently guessed the workplace. The friends then tease Serika about her uniform, crowd seats around Sensei, and ask when she started working.

This can be read as a **social intervention by normality**.

After E004's serious argument, they do not stage an immediate ideological rebuttal. They show up, eat ramen, embarrass Serika, and remain socially close.

But the source does not prove Hoshino's motive at this point. Serika later suspects Hoshino deliberately brought Sensei because of the previous day's disagreement. That is Serika's inference, not confirmed fact.

What is established is narrower:

- the group knows Serika well enough to identify the likely workplace;
- they had noticed she had been disappearing periodically;
- they did not know the reason;
- their response to discovery is teasing and inclusion rather than condemnation.

## 4.7 A hidden job indicates privacy inside a very small group

Stable evidence: `u:0064-0066`, raw `DataList[983]–[985]`.

Serika says she started the job about a week earlier. Nonomi realizes that this explains why Serika had sometimes disappeared.

A five-person institution is therefore not a transparent collective mind.

Even under extreme shared burden, members maintain private strategies and private labor.

This is useful counterevidence against flattening the Countermeasures Committee into perfect consensus. E004 already showed ideological disagreement about Sensei. E005 shows informational asymmetry about how members personally respond to debt.

## 4.8 Money consciousness is automatic for Serika even during a friendly meal

Stable evidence: `u:0074-0078`, raw `DataList[993]–[997]`.

Hoshino praises the ramen shop as an Abydos specialty. Serika's next concern is whether everyone can pay:

> `……ところで、みんなお金は大丈夫なの？`

She specifically asks whether they intend to rely on Nonomi again.

The line is revealing because nobody is discussing debt at that moment. Serika automatically audits the cost of a casual meal.

This suggests that scarcity has become a **cognitive habit**.

At the same time, Nonomi says her own card still has room below the limit. That prevents an important analytical mistake: Abydos's institutional insolvency should not be treated as proof that every member has identical personal liquidity.

The group has heterogeneous access to spending resources even while the school is financially collapsing.

## 4.9 `大人のカード` miniaturizes “adult power” into lunch

Stable evidence: `u:0079-0090`, raw `DataList[999]–[1015]`.

Sensei chooses:

> `逃げる。`

Hoshino catches Sensei, then invokes:

> `大人のカード`

The phrase sits in deliberate comic continuity with E003's `大人の力`.

E003 staged adult capacity at the scale of battle resources and command. E005 stages adult capacity at the scale of **paying for ramen**.

Hoshino even reframes the expense as a teacher's chance to feed hungry students.

This matters because the series is not allowing adult responsibility to remain purely heroic or military. Provisioning can be mundane.

The choice structure is also significant. `逃げる` is a designed intention whose result is immediate failure: Sensei is caught and the bill is paid anyway. This strengthens the current theory that Blue Archive choices often govern **persona and momentary action**, not route causality.

Nonomi's quiet attempt to supply payment adds another reciprocity wrinkle. The adult can buy the meal, but a student is prepared to support the adult's ability to do so. The scene again refuses a perfectly one-directional provider/dependent model.

## 4.10 Shibaseki Ramen is evidence that Abydos is declining, not socially dead

Stable evidence: `u:0028-0043`, `u:0074`, raw `DataList[940]–[957]`, `[993]`.

E001–E004 established abandoned districts, lost shops, depopulation, and ghost-town movement. E005 introduces a functioning local ramen shop that Hoshino calls an `アビドス名物`.

There is no contradiction.

Shiroko's earlier claim concerned an area where food stores were already gone, while she also said a more active area existed farther away. E005 now shows one surviving commercial/social node.

Abydos should therefore be modeled as **unevenly hollowed out**, not empty.

The surviving shop matters thematically. Institutional decline coexists with ordinary local culture worth preserving. “Reviving Abydos” is not a purely abstract defense of a school building; there are still businesses, routines, and places with communal identity.

## 4.11 Serika's anger after work is stubbornness, not hidden surrender

Stable evidence: `u:0096-0100`, raw `DataList[1024]–[1028]`.

After the group leaves, Serika complains that everyone was fussing over Sensei and suspects Hoshino intentionally brought Sensei because of the prior dispute.

She says:

> `私がそう簡単に折れると思ったら大間違いなんだから。`

This is important because the restaurant comedy does **not** secretly resolve E004's disagreement.

Serika remains resistant.

The episode therefore protects her dissent from being erased by ensemble warmth. She can enjoy group membership, work competently, be embarrassed by teasing, and still refuse to concede the adult-legitimacy argument.

## 4.12 Private monologue reveals the positive value beneath Serika's resistance

Stable evidence: `u:0105-0110`, raw `DataList[1039]–[1044]`.

Serika notices that the neighborhood has emptied further and that security has deteriorated.

Then:

> `このままじゃダメだ。私たちが頑張らないと……そして学校を立て直さないと……。`

This is the cleanest statement yet of her motivational core.

Her resistance to adult involvement is not a disguised desire to abandon the institution. The opposite is true. She is so strongly identified with the committee's collective responsibility that she experiences self-help as an ethical imperative.

The pronoun is `私たち`, not merely `私`.

Her independence is therefore collectivist in purpose even when individualistic in method.

## 4.13 Wages are explicitly earmarked for interest

Stable evidence: `u:0110`, raw `DataList[1044]`.

Serika continues:

> `とりあえずバイト代が入ったら、利息の返済に充てて……。`

This is one of the most important economic lines in the arc so far.

E004 said the committee can barely manage monthly interest. E005 proves that at least one member is attempting to feed personal labor income directly into that interest burden.

The scale mismatch is analytically central:

- the debt is hundreds of millions of yen;
- Serika is earning ordinary part-time wages;
- the wages are not even imagined as principal repayment first, but as interest service.

The debt trap therefore colonizes ordinary adolescent time without offering a plausible proportional path to resolution.

## 4.14 Committee membership becomes a personal targeting identifier

Stable evidence: `u:0101-0104`, raw `DataList[1033]–[1036]`.

Before Serika notices them, the attackers identify her as:

> `アビドス対策委員会のメンバー`

They are not selecting a random passerby.

The institution's political/security burden has become embodied in an individual member. Membership itself creates exposure.

This develops the “school as territory/community/asset” motif into a new level:

> **the student can become a hostage or instrument because she represents the institution.**

The precise purpose remains unknown at the E005 boundary.

## 4.15 Serika's immediate aggression mixes courage, habituation, and risk

Stable evidence: `u:0112-0118`, raw `DataList[1050]–[1056]`.

Serika recognizes the Helmet Gang and says her mood is already bad, then threatens to make them unable to enter the area again.

This confirms several things without requiring hindsight:

- she does not freeze upon encountering armed opponents;
- she is accustomed enough to armed conflict to answer with force immediately;
- her emotional state enters tactical behavior;
- she does not first seek withdrawal or reinforcement.

Calling this pure courage would be too flattering. Calling it pure recklessness would be too reductive.

At this boundary it is best understood as **confrontational self-reliance under conditions where armed conflict has become normalized**.

## 4.16 Defeat does not establish combat incompetence

Stable evidence: `u:0117-0128`, raw `DataList[1055]–[1067]`.

Serika realizes that enemies are positioned behind or around her and that the encounter was planned specifically around her.

She identifies a heavy weapon sound as possibly a modified `Flak41` and recognizes unexpected fire support.

That demonstrates tactical/combat literacy even as she is overwhelmed.

The source therefore supports:

> **Serika loses to a prepared capture operation with superior positioning/firepower.**

It does not support:

> **Serika is incapable of defending herself.**

The distinction matters because the arc has repeatedly separated local student competence from insufficient scale/resources.

## 4.17 `生かさなければ意味がない` changes the violence category

Stable evidence: `u:0129-0132`, raw `DataList[1069]–[1074]`.

After Serika collapses, Helmet Gang B asks whether to continue. Helmet Gang A says:

> `生かさなければ意味がない。`

The attackers then load her into a vehicle and head to a `ランデブーポイント`.

This is not simply battlefield victory.

The purpose requires Serika **alive**, implying that her continued personhood/body has instrumental value to the operation. At minimum, the violence has shifted from territorial harassment into organized abduction.

The text does not yet establish:

- whether ransom is intended;
- whether she will be used as leverage;
- whether another faction ordered the capture;
- who or what provides the apparent heavy fire support;
- what the rendezvous point connects to.

All remain OPEN.

---

# 5. Character-state updates

## 5.1 Serika

E005 is the first substantial Serika-centered unit and materially deepens her beyond “sharp skeptic of Sensei.”

### Trait

- quick-tempered and verbally combative;
- capable of professional restraint/code-switching at work;
- highly cost-conscious;
- action-oriented under danger;
- stubborn about relational boundaries.

### State

- still explicitly has not `認める` Sensei;
- embarrassed that the group discovers her part-time job;
- carrying part of Abydos's debt psychologically and materially;
- frustrated by friends' enthusiasm toward Sensei;
- abducted alive at episode end.

### Strategy

- personally earn money;
- conceal the job rather than turn it into a group discussion;
- allocate wages toward interest;
- respond to armed intrusion with direct force.

### Value

The clearest value is collective institutional responsibility:

> `私たちが頑張らないと`

She values Abydos enough to convert private time into repayment labor.

### Desire

- restore the school;
- contribute materially rather than merely hope;
- preserve agency over how she carries that burden.

### Fear / wound — bounded formulation

E004 established a history of perceived adult noninvolvement. E005 shows strong sensitivity to being patronized, followed, or treated as if her private life is automatically available to Sensei.

A mature “abandonment wound” diagnosis is still premature. The source supports **historically grounded distrust and boundary sensitivity**, not a clinical or totalizing explanation.

### Contradiction

Serika wants collective revival but pursues part of it privately. She demands that “we” work harder while concealing her own additional work from the other four.

That contradiction is productive rather than hypocritical. It suggests that shared responsibility and self-imposed burden coexist.

## 5.2 Sensei

E005 adds social imperfection to the existing vulnerability/fallibility model.

Sensei:

- greets Serika despite her hostility;
- asks about her destination;
- follows her twice despite explicit refusal;
- participates in the restaurant's group sociality;
- attempts to escape the imposed meal bill but is caught;
- ultimately pays for everyone;
- leaves when the outing ends.

This prevents a saintly reading. Sensei's relationship-building can be intrusive even while broader institutional conduct remains enabling.

## 5.3 Hoshino

Clean lines continue the established pattern of languid teasing plus practical social steering.

She:

- identifies the likely workplace;
- teases Serika rather than reopening E004 as a formal argument;
- orchestrates or at least strongly facilitates the group meal;
- catches Sensei attempting to flee the bill;
- frames feeding students as an adult/teacher opportunity.

Serika suspects Hoshino deliberately brought Sensei because of the prior conflict, but that motive is **Serika's inference**, not confirmed authorial fact at this boundary.

## 5.4 Shiroko

Shiroko remains socially direct and sparse. She invites Sensei to sit beside her in one branch, asks Serika how long she has been working, and later reports being full after Sensei pays.

No mature romantic reading is warranted from seating proximity.

## 5.5 Nonomi

Nonomi's personal card has remaining room below its limit, and she is willing to cover the meal. She later quietly attempts to support Sensei's payment.

This establishes **resource heterogeneity and generosity**, not a complete socioeconomic biography.

## 5.6 Ayane

Ayane's E005 role is lighter: she reacts awkwardly to Serika, participates in the meal, corrects Hoshino's odd money-making joke, and recognizes that Hoshino seemingly planned to put Sensei on the bill.

No major institutional-role change occurs.

---

# 6. Relationship-state updates

## 6.1 Sensei ↔ Serika

This relationship becomes more complex rather than simply warmer.

Current state:

> **demonstrated gratitude + explicit nonacceptance + boundary conflict + persistent social contact**

Serika says `まだ先生のこと認めてない`. That preserves E004's outsider state.

Sensei's repeated pursuit introduces actual counterevidence to a fully consent-sensitive adult model. Serika's `ストーカー` accusation is comic in tone but still names her perception of the behavior.

At the same time, the episode does not depict fear, estrangement, or total rupture. Sensei later appears with the group, pays for the meal, and Serika's post-work anger is directed at the group's fussing and Hoshino's suspected maneuver rather than a claim that Sensei harmed her severely.

The relationship remains **open and contested**.

## 6.2 Serika ↔ Countermeasures Committee

The group knows Serika's habits well enough to guess Shibaseki Ramen but did not know she had begun working there.

This is a useful intimacy/privacy balance:

- high familiarity;
- high teasing tolerance;
- incomplete knowledge of private burden strategies.

Nonomi's decision in E004 to go after Serika and the group's E005 appearance together form a cautious pattern of **not letting conflict become isolation**, though the exact motive for the visit remains unconfirmed.

## 6.3 Sensei ↔ Countermeasures Committee ensemble

The restaurant sequence shifts the relationship out of emergency operations and into low-stakes shared life.

Sensei is treated sufficiently as part of the social group to be seated with them, teased, and made to pay. This is not the same as formal committee membership, and Serika specifically continues to resist it.

The distinction matters:

> **ensemble social incorporation can advance faster than unanimous relational legitimacy.**

## 6.4 Serika ↔ Abydos as place

E005 gives Serika a relationship not merely to the school but to the district itself.

She notices residents disappearing and security worsening. She works at a local specialty restaurant she already frequented. Her school-revival motivation is therefore embedded in a lived community landscape, not only attachment to an institutional name.

---

# 7. Institutional state: debt becomes labor, and decline becomes uneven civic life

## 7.1 Student labor is part of the repayment ecology

E004 established monthly-interest pressure. E005 proves that a current student is attempting to generate wage income for that purpose.

This should be added to the Abydos debt model:

> inherited liability → current interest burden → student time/labor diverted into debt service

The exact amount of Serika's wages and whether they are formally transferred to school accounts are not stated. Her **intention** to use them for interest is explicit.

## 7.2 Institutional poverty is not identical to uniform individual poverty

Nonomi retains spending capacity on a personal card. Sensei can pay for the group.

This is important source discipline.

Abydos High is near insolvent. That does not imply every member has the same personal resource state.

Future economic analysis should distinguish:

- school balance sheet;
- committee-controlled funds;
- individual student income/assets/credit;
- Schale resources;
- local commercial economy.

## 7.3 Shibaseki Ramen is surviving local infrastructure

The shop is functioning, has a known master, employs Serika, and is described as an Abydos specialty.

Abydos's civic decline is therefore spatially uneven.

The district is becoming hollowed out, but ordinary commerce and local identity survive in pockets.

## 7.4 Public-security deterioration is now stated by a local resident/student perspective

Serika notes both lower population and worsening security on her route home.

This connects demographic contraction to everyday vulnerability without proving a complete causal model. It is reasonable to infer that fewer residents and weaker institutional capacity correlate with the environment in which armed groups can operate, but the source does not yet specify policing structures or exact causal mechanisms.

## 7.5 Committee membership carries personal security risk

The abductors select Serika because she is a committee member.

The committee is therefore not only a governance/revival organization; it also creates identifiable exposure for its members in local conflict.

---

# 8. Sensei role, choice-space, and ethics

## 8.1 E005 is the first strong counterexample to a purely consent-sensitive Sensei

The episode's third and fourth formal choices are both `追いかける`.

They occur after explicit Serika refusal.

That cannot be harmonized away simply because Sensei later acts generously.

The correct current formulation is:

> **Sensei's institutional ethics have so far been strongly nonappropriative, but Sensei's social persona can be nosy, persistent, and boundary-crossing in comedy.**

This is a refinement, not a collapse, of the adult-responsibility thesis.

## 8.2 Choice can author ethically imperfect persona

Earlier analysis emphasized that choices often enact ethical/persona agency without large causal branching.

E005 strengthens that claim from a new direction.

The player is not always choosing among equally admirable expressions of a fixed good protagonist. Sometimes the authored choice itself is socially questionable.

This matters for `BA-C008`:

> choice-space is a characterization device, not merely a morality menu.

## 8.3 Seating choice provides local social texture rather than plot divergence

The Nonomi/Shiroko seat choice changes branch-conditioned comic material around physical proximity but does not change the episode's institutional or dramatic outcome.

This is classic micro-persona/social choice-space.

It should not be inflated into route-level relational exclusivity.

## 8.4 `逃げる` demonstrates frustrated agency

Sensei can choose to flee the bill.

The narrative immediately blocks the attempt.

This creates a useful third category alongside branching and convergence:

- **branching choice** — changes later state;
- **convergent choice** — different formulation, same structural act;
- **frustrated choice** — intention is enacted briefly but another character/narrative force prevents the intended outcome.

E005 provides clean evidence for the third.

## 8.5 Paying for lunch is support without governance

Hoshino's adult-card joke turns adult resources into mundane care.

Sensei's ability to feed students does not create political authority. It nevertheless contributes to the relational texture of being a teacher/adult.

This is worth preserving because later analyses should not define adult responsibility only through crisis intervention.

---

# 9. Japanese-language observations

## 9.1 `まだ先生のこと認めてない`

`まだ` makes Serika's rejection temporally open while still emphatic in the present.

`認める` here appears broader than “admit competence.” It carries recognition/acceptance/standing.

## 9.2 `なれなれしくしないで`

Serika objects to overfamiliarity itself.

This is a direct relational-boundary phrase and should be tracked with E004's `部外者`.

## 9.3 `関係ない`

`私が何をしようと、別に先生とは関係ないでしょ？`

Serika asserts informational autonomy: what she does is not Sensei's concern.

## 9.4 `ダメな大人`

Serika uses the phrase while contrasting her own busyness with Sensei's apparent leisure and again when trying to make Sensei stop following her.

It extends the arc's adult vocabulary in a negative register: adult status can be judged and rejected, not merely admired.

## 9.5 `ストーカー`

The word is comedic but explicit. It names Sensei's persistence from Serika's perspective after she has declined to reveal her destination.

The tone should not erase the boundary content.

## 9.6 `少しでも稼がなきゃ`

The `少しでも` construction encodes incremental contribution under overwhelming scale.

Serika's economic ethic is not based on a realistic belief that one wage solves the debt; it is based on refusing zero contribution.

## 9.7 Customer-service register

Serika switches from abrasive informal speech to:

- `いらっしゃいませ`
- `ご案内いたします`
- `少々お待ちください`

The shift demonstrates situational register control.

## 9.8 `アビドス名物`

Hoshino's labeling of Shibaseki Ramen as a local specialty linguistically preserves Abydos as a culture/place with positive identity, not merely a disaster zone.

## 9.9 `大人のカード`

The phrase comicly extends `大人` from responsibility and battle-scale resources into ordinary purchasing/provisioning.

At this boundary, do not infer any metaphysical/card-system function not explained in the text.

## 9.10 `私たちが頑張らないと`

The line crystallizes Serika's collective self-conception.

She is personally laboring, but the imagined agent of recovery is `私たち`.

## 9.11 `利息の返済に充てて`

The verb `充てる` explicitly earmarks future wage income for interest payment.

It is stronger evidence than a generic claim that Serika “works because the school needs money.”

## 9.12 `生かさなければ意味がない`

The captor's line establishes that Serika must remain alive for the operation's purpose.

It transforms the violence from simple elimination into instrumental captivity while leaving the intended use open.

---

# 10. Motifs and thematic development

## 10.1 Institutional burden becomes embodied time

E004's debt architecture now reaches into an individual student's day.

Money problems become schedule problems.

## 10.2 Ordinary life under structural crisis

The title's “ordinary day” contains work, ramen, friends, money anxiety, depopulation, armed pursuit, and kidnapping.

The juxtaposition suggests that crisis has become woven into normalcy rather than replacing it completely.

## 10.3 Self-reliance versus isolation

Serika's self-reliance is morally serious because it comes from commitment.

But private work and solitary movement also reveal how individual burden-bearing can reduce collective knowledge of risk.

The episode does not state that dependence is preferable. It destabilizes **absolute self-sufficiency**.

## 10.4 Care through teasing and food

The committee's restaurant visit is noisy and embarrassing rather than solemnly therapeutic.

Shared food becomes a low-stakes medium of reintegration after ideological conflict.

## 10.5 Adult power miniaturized

E003: resources, equipment, command.

E004: listening and staying.

E005: paying for ramen—and sometimes being socially annoying.

The adult motif is becoming plural rather than heroic-monolithic.

## 10.6 Scarcity as cognition

Serika thinks about prices, payment, wages, and interest even when the scene is socially light.

Financial crisis has entered attention itself.

## 10.7 Uneven urban death

Abandoned blocks coexist with a beloved ramen shop.

Abydos is neither thriving nor empty; it is a partially living place undergoing contraction.

## 10.8 Membership as exposure

Being a member of the committee marks Serika for capture.

Institutional identity now has bodily stakes.

---

# 11. Violence, ethics, economics, and power

E005 is unusually effective because its economic and violent threads are causally adjacent without being identical.

Serika works because she wants to service interest. After work, she passes through a thinning neighborhood and reflects on worsening security. Then an armed group that knows her institutional identity executes a capture operation.

The correct analysis is not that debt directly causes the kidnapping. The source does not prove that.

The stronger formulation is:

> **Abydos's structural decline creates a world in which economic burden, demographic hollowing, security deterioration, and armed conflict coexist in the same student's ordinary routine.**

Serika's immediate choice to fight also deserves ethical nuance.

She faces people already planning to abduct her. Her violence is therefore not aggression against neutral strangers. Yet she does not know their plan when she first chooses confrontation, and she explicitly channels her bad mood into the threat.

This makes the encounter neither a clean pacifist problem nor a simple self-defense exemplar.

Her response reflects a setting in which armed force is ordinary enough that a student confronting a known hostile gang moves rapidly to combat.

The attackers then escalate from local gang harassment into organized capture using superior positioning and heavy support. Keeping her alive creates a coercive-power problem that the next unit must resolve without E005 hindsight.

---

# 12. Competing readings and counterevidence

## Reading A: “Serika is just a tsundere who secretly likes Sensei already.”

**Too strong.**

She explicitly says she has not yet accepted Sensei, asserts privacy boundaries, remains angry after the restaurant encounter, and vows not to yield easily.

Her embarrassment and social engagement do not erase explicit dissent.

## Reading B: “Serika is ungrateful to Sensei.”

**Rejected by E004–E005 together.**

E004 showed sincere gratitude for immediate help. Her dispute concerns legitimacy, intrusion, and relational standing—not denial that Sensei helped.

## Reading C: “Serika's part-time job proves she thinks she can personally repay the entire debt.”

**Rejected.**

Her phrasing is incremental: `少しでも`. She later earmarks wages for **interest**, not a fantasy of personally clearing the full principal.

## Reading D: “Sensei fully respects Serika's boundaries because Sensei is the responsible adult.”

**Contradicted at the micro-social level.**

The formal interface twice requires Sensei to follow after explicit refusal. The narrative plays this as comedy, but the conduct is intrusive.

## Reading E: “Because Sensei follows her, the whole adult-responsibility thesis collapses.”

**Also too strong.**

The project already distinguishes institutional conduct, social persona, and moral imperfection. Sensei can behave intrusively in a comic interpersonal scene while still refusing to seize Abydos's institution or debt.

The better conclusion is that adult responsibility is **non-saintly and unevenly enacted**.

## Reading F: “The restaurant proves Abydos is not really a ghost town.”

**Rejected.**

One functioning local business is compatible with severe uneven depopulation. Serika herself later remarks that the area has lost residents and become less safe.

## Reading G: “Serika is defeated because she is a weak fighter.”

**Unsupported.**

She is deliberately ambushed, notices enemies behind her, identifies heavy fire/support, and is targeted for live capture. The defeat primarily demonstrates prepared opposition and insufficient individual capacity against organized force.

## Reading H: “The kidnapping proves Serika was wrong to distrust adults.”

**Rejected as moral logic.**

Being victimized by hostile actors does not retroactively invalidate her consent boundary or her critique of adult neglect.

The structural lesson is about limits of solitary capacity, not moral punishment for independence.

## Reading I: “The kidnappers' patron/motive is now obvious.”

**OPEN.**

The text establishes targeted live capture and a rendezvous point. It does not identify the ultimate purpose or sponsor.

---

# 13. Claim revision at E005

No new claim ID is necessary. E005 materially sharpens existing claims.

| Claim ID | Transition at E005 | Current effect |
|---|---|---|
| BA-C001 | **STRENGTHEN / refine** | responsible adulthood now includes mundane provisioning but also socially imperfect behavior; responsibility is not saintliness |
| BA-C002 | **STRENGTHEN** | Serika still withholds `認める`; legitimacy remains member-specific and cannot be inferred from group incorporation |
| BA-C003 | **PRESERVE / STRENGTHEN lightly** | Schale appears in ordinary committee social life without replacing the committee's local work or institution |
| BA-C004 | **PRESERVE** | no new system-scale capability; adult resources shrink comically to meal payment while student competence remains independent |
| BA-C005 | **PRESERVE REJECTED** | Sensei can be socially awkward, fail to escape a bill, and remain outside Serika's trust; omnipotent-avatar model weakens further |
| BA-C006 | **PRESERVE REJECTED; counterevidence strengthened** | Serika independently works to service interest, tracks local decline, and displays combat literacy; institutional weakness is not generic student incapacity |
| BA-C007 | **REVISE / complicate** | Schale's macro-level service remains enabling, but Sensei's micro-social pursuit ignores explicit Serika refusal; legitimacy cannot be equated with perfect consent sensitivity |
| BA-C008 | **STRENGTHEN** | choices author social persona, route-conditioned proximity, persistence, and even frustrated action (`逃げる` fails), not merely plot branching |
| BA-C009 | **PRESERVE** | no material new technical-system ontology |
| BA-C010 | **PRESERVE / STRENGTHEN lightly** | Sensei provides ordinary resources without claiming ownership; Serika's own burden remains hers/committee's rather than transferred |
| BA-C011 | **STRENGTHEN / broaden** | non-infallibility now includes ethical/social imperfection, not only navigation/physical vulnerability; adult value coexists with being annoying or intrusive |

The most important revision is `BA-C007`: **enabling service and consent-sensitive relationship-building must be tracked separately**. A good institutional intervention does not automatically make every interpersonal behavior good.

---

# 14. Cumulative ledger deltas

## Character-state ledger

- **Serika:** add hidden part-time labor; wage-to-interest intention; professional code-switching; collective restoration ethic; explicit continued nonacceptance of Sensei; combat literacy; abducted alive after targeted ambush.
- **Sensei:** add persistent/nosy social behavior that crosses Serika's explicit boundary; mundane meal provisioning; choice-space includes frustrated escape.
- **Hoshino:** add social steering/teasing around Serika's workplace and adult-card meal framing.
- **Nonomi:** add personal card spending capacity and quiet willingness to subsidize payment; do not infer full wealth background.
- **Shiroko/Ayane:** minor social-state reinforcement only.

## Relationship-state ledger

- **Sensei ↔ Serika:** gratitude/nonacceptance becomes active boundary conflict under continued contact; no reconciliation yet.
- **Serika ↔ committee:** high familiarity coexists with concealed individual burden strategy.
- **Sensei ↔ committee ensemble:** expands from operational partnership into ordinary meal/social incorporation, without unanimous local legitimacy.

## Institution ledger

- debt burden now demonstrably reaches individual student wage labor;
- Shibaseki Ramen establishes surviving local commerce/community identity;
- personal resource heterogeneity must be separated from institutional insolvency;
- committee membership now creates personal targeting risk;
- local public-security deterioration is stated from Serika's perspective.

## Sensei ethics ledger

- add explicit counterexample to micro-level consent sensitivity: required pursuit after refusal;
- preserve distinction between institutional nonappropriation and interpersonal nosiness;
- add mundane provisioning/meal payment as low-stakes adult support;
- add `逃げる` as frustrated choice-space.

## Japanese voice/address ledger

Add/highlight:

- `まだ先生のこと認めてない`
- `なれなれしくしないで`
- `関係ない`
- `ダメな大人`
- `ストーカー`
- `少しでも稼がなきゃ`
- customer-service register
- `アビドス名物`
- `大人のカード`
- `私たちが頑張らないと`
- `利息の返済に充てて`
- `生かさなければ意味がない`

## Motif/theme ledger

Add:

- institutional debt → individual labor/time;
- ordinary life under chronic crisis;
- self-reliance versus isolation;
- surviving local culture/commercial nodes;
- adult power miniaturized into everyday provisioning;
- scarcity as cognitive habit;
- committee membership as personal exposure;
- social consent as separate axis from institutional service ethics.

## Claim ledger

Append E005 delta with `BA-C007` explicitly complicated/revised and `BA-C011` broadened from practical fallibility to ethical/social imperfection.

---

# 15. Open questions after E005

1. Why is Serika specifically being captured alive?
2. Is the capture operation solely a Helmet Gang initiative, or is another actor involved?
3. What is the source of the apparent heavy fire support Serika detects?
4. What is the rendezvous point and who is expected there?
5. How will the committee discover Serika is missing?
6. How will Sensei respond to an emergency involving the one member who most explicitly resisted adult involvement?
7. Will rescue respect Serika's agency after the immediate danger is removed?
8. Will E006 change Serika's evaluation of Sensei, and if so, through gratitude, trust, dependence, embarrassment, or something else?
9. How much money does Serika's job actually contribute relative to monthly interest?
10. Do other committee members have personal income or repayment strategies?
11. Why did Serika begin the job roughly a week earlier?
12. How many functioning businesses/inhabited zones remain in Abydos, and how uneven is depopulation?
13. Does worsening public security follow primarily from depopulation, institutional weakness, organized criminal expansion, or multiple factors?
14. Is Hoshino deliberately using ordinary group sociality to integrate Sensei and soften Serika's resistance, or is that only Serika's suspicion?
15. Will Sensei's repeated boundary-crossing social comedy remain a recurring persona feature, and how should it be weighed against broader responsible-adult ethics?
16. Does `大人のカード` have any significance beyond mundane/payment comedy that later primary text explicitly earns?

---

# 16. Evidence locator index

All stable locators below refer to `BA:main:001:001:005:scene:001` unless otherwise noted.

| Topic | Stable locator(s) | Raw source index / note |
|---|---|---|
| location / ordinary-day opening | `u:0001-0003` | `DataList[900-904]` |
| Serika has not accepted Sensei | `u:0004-0006` | `DataList[906-908]` |
| `ダメな大人` / busyness | `u:0009-0010` | `DataList[912-913]` |
| free-attendance day / privacy | `u:0011-0016` | `DataList[914-920]` |
| first required pursuit / `ストーカー` | `u:0017-0023` + choice 003 | `DataList[923-929]` |
| job reveal / `少しでも稼がなきゃ` | `u:0021-0023` | `DataList[927-929]` |
| second required pursuit / `ダメ大人` | `u:0024-0027` + choice 004 | `DataList[934-938]` |
| professional ramen-shop register | `u:0028-0033` | `DataList[940-945]` |
| group arrives / Hoshino explains location guess | `u:0034-0043` | `DataList[946-957]` |
| Nonomi/Shiroko seating branch | `u:0044-0058` + choice 006 | `DataList[959-975]`, selection-group conditioned |
| job begun about one week earlier | `u:0064-0066` | `DataList[983-985]` |
| ramen orders / Abydos specialty | `u:0069-0074` | `DataList[988-993]` |
| Serika cost-checks / Nonomi card | `u:0075-0078` | `DataList[994-997]` |
| failed `逃げる` / adult card | `u:0079-0083` + choice 007 | `DataList[999-1004]` |
| Nonomi private payment offer / Sensei pays | `u:0084-0090` | `DataList[1005-1015]` |
| Serika ejects group | `u:0091-0095` + choice 008 | `DataList[1016-1023]` |
| post-work refusal to “fold” | `u:0096-0100` | `DataList[1024-1028]` |
| abductors identify committee membership | `u:0101-0104` | `DataList[1033-1036]` |
| depopulation / security deterioration | `u:0105-0108` | `DataList[1039-1042]` |
| `私たちが頑張らないと` / school restoration | `u:0109` | `DataList[1043]` |
| wages earmarked for interest | `u:0110` | `DataList[1044]` |
| confrontation / targeted ambush recognition | `u:0111-0119` | `DataList[1049-1057]` |
| Flak41-modified sound / fire-support realization | `u:0120-0127` | `DataList[1058-1065]` |
| unconscious / live-capture order | `u:0128-0132` | `DataList[1067-1074]` |
| next title `救出作戦！` | `u:0133` | `DataList[1076]` |

---

# Closing assessment

E005 is deceptively important because it takes the Abydos arc's structural thesis and puts it inside one student's schedule.

Serika's skepticism toward Sensei is not exposed as empty defensiveness. Her ordinary life proves that she is **already paying for her beliefs**: she gives free time to wage labor, thinks automatically in terms of repayment, watches her neighborhood empty out, and insists that the students must restore their own school.

That makes her conflict with Sensei more serious, not less. She is protecting an identity built around responsibility under abandonment.

At the same time, the episode refuses to let self-reliance become invulnerability. Serika's private labor remains partly hidden from the group; her commute runs through a deteriorating security environment; and adversaries exploit her individual exposure by targeting her specifically as a committee member.

Nor does the episode make Sensei morally perfect. The twice-required `追いかける` choices disregard Serika's explicit wish to be left alone. This is analytically productive: **Blue Archive can present Sensei as a responsible adult at the institutional level while still writing a socially intrusive, comic, imperfect person.**

The unit's most useful compact formulation is therefore:

> **E005 turns Abydos's debt into student time and turns Serika's distrust into an ethic of self-earned contribution; then it exposes the limits of both adult idealization and solitary self-reliance.**

The next unit, `BA:main:001:001:006` / 第6話「救出作戦！」, should be read as a test of what rescue means after Serika has explicitly resisted deeper adult involvement: emergency intervention is clearly warranted by the abduction, but the analysis should distinguish **saving a student from coercive captivity** from claiming broader authority over her life, choices, or judgment afterward.
