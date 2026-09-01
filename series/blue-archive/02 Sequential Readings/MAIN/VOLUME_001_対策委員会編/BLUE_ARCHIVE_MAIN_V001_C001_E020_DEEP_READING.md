---
series: BLUE_ARCHIVE
artifact_type: deep_reading
scope: MAIN_V001_C001_E020
generation: V1
status: active_provisional
source_boundary: Canonical Japanese main-story unit BA:main:001:001:020, 対策委員会編 第20話『風紀委員会、参戦！』, electricgoat/ba-data@jp cbe3fd623c2aab9e781ba0ce0483bc77c68bff86
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-18
updated: 2026-08-18
---

# BLUE ARCHIVE — MAIN V001 C001 E020 DEEP READING
## 対策委員会編 — 第20話「風紀委員会、参戦！」

## 0. Source boundary, provenance, and integrity constraints

This reading is limited to the twenty-second canonical main-story object in analytical order and the twentieth/final object in `対策委員会編` Chapter 1:

- story ID: `BA:main:001:001:020`;
- analytical scope: `MAIN_V001_C001_E020`;
- source title: `第20話;風紀委員会、参戦！`;
- source arc/chapter: `第1篇_対策委員会編 / 第1章 / 第20話`;
- raw group ID: `11200`;
- source class: `main`;
- source repository: `electricgoat/ba-data`;
- branch: `jp`;
- commit: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`;
- source table: `Excel/ScenarioScriptMain1ExcelTable.json`;
- source SHA-256 at the current V001 boundary: `3e788789e047e0efb5e5d15c8d4f517510ac430fd554dc41cbb7826a3c4af877`;
- parser version: `0.1.0`;
- promoted scene-record count: **85**;
- normalized Sensei choice groups: **2**;
- canonical scene count: **2**;
- promoted named persons materially represented: Kayoko, Mutsuki, Iori, Chinatsu, Serika, Ayane, Shiroko, Nonomi, Ako, Haruka, and Sensei through choice-space/presence;
- additional role speakers: grenadier / Prefect Team member;
- canonical source path: `02_CANONICAL_STORIES/MAIN/VOLUME_001/CHAPTER_001/EPISODE_020.md`;
- source-side convenience rendering: `20話_風紀委員会、参戦！.md`;
- stable complete-scene projections:
  - `BA:main:001:001:020:scene:001`;
  - `BA:main:001:001:020:scene:002`.

### Canonical scene structure

1. `BA:main:001:001:020:scene:001`
   - location: `破壊されたアビドス市街地`;
   - stable records `u:0001`–`u:0059` plus `choice:001`;
   - contains the Prefect Team's opening bombardment/pursuit of Problem Solver 68, Iori and Chinatsu's disagreement over whether Abydos must first be informed, Abydos's sovereignty debate while Hoshino remains unreachable, Sensei's deliberative prompt, Ayane's explicit no-permission/no-jurisdiction objection, Chinatsu's recognition of Sensei, and the outbreak of direct Abydos–Prefect Team combat.

2. `BA:main:001:001:020:scene:002`
   - location not explicitly stated;
   - stable records `u:0001`–`u:0026` plus `choice:001`;
   - contains the Prefect Team's defeat, Sensei's reunion with Chinatsu, Chinatsu's retrospective acknowledgment that Sensei's presence should have triggered withdrawal, Ayane's formal demand for affiliation, Ako's remote administrative introduction and implicit disciplining of Iori, and Haruka's final opportunistic escalation as everyone gathers.

### Source-integrity warning 1 — convenience rendering is incomplete

The source-side convenience file `20話_風紀委員会、参戦！.md` stops after the first scene at the moment combat begins.

The promoted canonical retrieval layer, however, contains a complete second scene with stable IDs through `scene:002:u:0026`.

Therefore:

> **The convenience Markdown is not a complete literary object for E020. The two-scene promoted canonical projection is governing evidence.**

This is an important pipeline/source-audit issue and should not be mistaken for a narrative ellipsis.

### Source-integrity warning 2 — speaker-mapping anomalies remain quarantined

The promoted layer attributes the following to Chinatsu:

- `はあ、面倒だな、たかが4人で。こっちは一個中隊級の兵力なのに。` (`scene:001:u:0045`);
- `ちっ、仕方ない。行くぞ！` (`scene:001:u:0058`).

Both lines are linguistically and situationally discordant with Chinatsu's surrounding procedural register and closer to Iori's more aggressive voice. The stable promoted layer nevertheless labels them Chinatsu.

A further anomaly occurs at `scene:002:u:0010`, which is promoted as Iori saying:

> `それは私から答えさせていただきます。`

Immediately afterward, Ayane reacts to a communication, Iori says `アコちゃん……？`, Chinatsu says `アコ行政官……？`, and Ako introduces herself remotely. Narrative sequence strongly suggests `u:0010` may belong to the incoming remote speaker rather than Iori, but this reading will **not silently rewrite the promoted attribution**.

No major institutional or thematic claim depends on resolving these anomalous lines.

### Choice-space and Sensei presence

E020 contains two normalized Sensei choice groups:

1. `scene:001:choice:001`
   - `じゃあ便利屋をこのまま風紀委員会に引き渡しちゃう？`
2. `scene:002:choice:001`
   - `久しぶり、チナツ。`

The first is especially important because it functions as a **deliberative prompt rather than a sovereign command**. Sensei raises the apparent low-conflict option—hand PS68 over—after Nonomi asks what Abydos should do. Shiroko rejects it as leaving no acceptable alternative; Ayane then supplies the jurisdictional reasoning for resistance.

The second reactivates the Prologue relationship with Chinatsu and confirms that the two recognize one another.

### Local-information lock

Available prior analytical authority is limited to:

- canonical Prologue E001–E002 and `BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md`;
- `BLUE_ARCHIVE_MAIN_V001_C001_E001_DEEP_READING.md` through `E019_DEEP_READING.md`;
- the seven longitudinal ledgers through E019.

**Chapter 2 is out of scope.**

No `MAIN_V001_C002` material, later main-story explanation, Prefect Team side material, event/bond story, adaptation, wiki, or franchise hindsight is used to determine:

- the full content of Ako's explanation;
- who precisely ordered the Prefect Team's deployment and under what detailed instructions;
- whether Iori exceeded an explicit prior order;
- the full reason Ako is involved;
- whether Haruka attacks and whom she targets next;
- whether Hoshino's abnormal unreachability is caused by Black Suit;
- what Black Suit offered Hoshino;
- or the longer-term settlement of Abydos–Gehenna jurisdiction.

E020 ends Chapter 1 but does **not** resolve all of these threads. The next analytical action is therefore the mandatory **Chapter 1 checkpoint**, not Chapter 2 reading.

---

# 1. Story placement and local chronology

E019 ended with a company-scale Gehenna Prefect Team force shelling Problem Solver 68 from approximately three kilometers away.

E020 makes the political significance explicit.

The narrative sequence is:

> **Kayoko recognizes the incoming Prefect Team → the Prefect Team suppresses PS68 with indirect fire → Iori treats interference by Abydos as obstruction of Gehenna public duty → Chinatsu argues explanation should precede coercion → Abydos realizes it was inside the artillery envelope → Nonomi identifies the risk of inter-academy political conflict → Hoshino remains abnormally unreachable → Sensei raises surrender/hand-over as an option → Shiroko rejects it → Ayane articulates territorial autonomy and consent → Abydos moves to stop the Prefect Team → Chinatsu recognizes Sensei and urgently tries to halt the battle → fire nevertheless opens → the Prefect Team is defeated → Chinatsu concedes that Sensei's presence should have changed their tactical judgment → Ayane demands formal institutional identification → Ako appears remotely as a Gehenna administrator and offers an explanation → Ako implicitly disciplines Iori → Haruka notices everyone is gathered and begins another escalation.**

This closes Chapter 1 not by resolving the conspiracy plot, but by crystallizing the arc's political vocabulary.

Earlier units had repeatedly asked whether authority is legitimate merely because it is:

- adult;
- official;
- financially powerful;
- helpful;
- contractual;
- or formally institutional.

E020's answer is increasingly consistent:

> **No. Status and purpose matter, but legitimacy also depends on jurisdiction, procedure, consent, accountability, and the practical agency of those over whom power is exercised.**

---

# 2. Narrative reconstruction

## Scene 1 — Public duty enters someone else's territory

Kayoko is the first person to understand the new threat.

She warns Aru, Mutsuki, and Haruka to hide because:

> `うちの風紀の連中だよ！`

The possessive `うちの` confirms a meaningful shared Gehenna institutional frame even though PS68 operates as an independent and unruly club. Kayoko is not encountering an unknown army. She recognizes the academy coercive apparatus chasing them.

The Prefect Team opens with heavy force.

A grenadier reports the target suppressed; Iori immediately orders infantry through the second platoon to advance.

Chinatsu then asks the question that creates the episode's first normative split:

What should they do about the students on the other side?

Iori identifies them vaguely as Abydos and gives an uncompromising answer:

> `公務の執行を妨害する輩は全員敵だ。`

The sentence matters less as evidence that the Prefect Team has lawful jurisdiction than as evidence of **Iori's own theory of authority**.

For Iori, official purpose plus operational obstruction is sufficient to convert outsiders into enemies.

Chinatsu immediately proposes a different order of operations:

> `しかしこちらの事情を説明するのが先かと……。`

Explanation should come first.

Iori asks whether explanation is even necessary and says that if outsiders interfere, the Prefect Team will beat them down without question.

This creates a sharp internal contrast:

- **Iori:** official mission → resistance = enemy → force;
- **Chinatsu:** official mission → explain circumstances → seek noninterference before force.

The institution is therefore not ideologically homogeneous.

### Abydos receives the intervention as a jurisdictional crisis

Serika initially interprets the Prefect Team as arriving to arrest PS68.

Ayane refuses to claim more than the evidence supports:

> `まだわかりません……しかし私たちに友好的とは判断しかねます。`

Shiroko adds the decisive operational fact: Abydos was inside the bombardment area even if the shells were not obviously aimed directly at them.

Nonomi then distinguishes the Prefect Team from the kinds of armed organizations the story has previously normalized.

The Prefect Team is not merely:

- another academy's recognized armed club;
- or a private-ish club such as PS68.

Its institutional character makes the encounter politically dangerous:

> `一歩間違えれば、政治的な紛争の火種になるかもしれません……。`

This is a sophisticated point.

The same bullet or shell can have different political meaning depending on **who fires it under what authority**.

Violence by an outlaw club can remain a local criminal/contractual dispute. Violence by the coercive arm of a major academy inside another academy's district can become inter-polity conflict.

### Hoshino's absence becomes materially consequential

Nonomi asks whether Hoshino can be reached.

Ayane says no and notes:

> `普段なら、ここまで連絡取れないことはないはずなのに……。`

This establishes **abnormal unavailability**, not its cause.

The audience knows E017 ended with Hoshino being approached by Black Suit, so a causal connection is plausible. But E020 never states that Black Suit is why Hoshino cannot be reached.

The correct evidentiary state is:

> **temporal adjacency + abnormal absence = strong question, not proof.**

More importantly, Hoshino's absence tests whether the committee can make a sovereignty decision without its chair.

It can.

### Sensei's choice prompts deliberation rather than deciding it

Nonomi asks what they should do.

Sensei raises:

> `じゃあ便利屋をこのまま風紀委員会に引き渡しちゃう？`

Read literally, this can sound like a proposal to avoid conflict by surrendering PS68.

But structurally it functions as an elicitation of the committee's own reasoning.

Nonomi is reluctant but cannot justify fighting Gehenna. Serika asks what alternative exists. Shiroko supplies one:

> `他に選択肢はない、風紀委員会を阻止する。`

Ayane pauses, then agrees.

The actual normative argument comes from **Ayane**, not Sensei.

She concedes the morally inconvenient premise:

> `きっと、便利屋の皆さんが問題を起こしたのは事実です……。`

PS68 wrongdoing is not denied.

Then she separates wrongdoing from jurisdiction:

> `しかし、だからといって、他の学園の風紀委員会が私たちの許可もなく、こんな暴挙を敢行してもいいという意味ではありません。`

This is one of the clearest political statements in Chapter 1.

The structure is:

1. **Wrongdoing occurred.**
2. **Punishment may be justified.**
3. **That does not mean any institution may punish anywhere.**
4. **Abydos's permission matters because the action occurs inside Abydos's autonomous district.**

Serika translates the point into the language of school rights:

> `これは私たちの学校の権利を無視するような真似よ！`

and insists:

> `便利屋を罰するのは私たち！`

Her wording mixes sovereignty with personal grievance—PS68 destroyed Shiba Seki—but the underlying institutional claim is the same.

Abydos is not defending PS68's innocence.

It is defending **its own right to determine PS68's disposition inside its jurisdiction**.

### `公務` is not self-legitimating

This directly answers Iori's earlier framing.

Iori uses `公務`—public duty—as if the official character of Gehenna's mission settles the matter.

Ayane's reasoning says the opposite:

> public purpose does not erase territorial jurisdiction.

This closely parallels E016.

There, Hifumi reformulated Hoshino's fear as harmful action occurring under the **`名目`** of support.

Here, coercive action occurs under the **`公務`** of a formal disciplinary body.

The repeated principle is:

> **The normative label attached to power does not by itself legitimate its exercise.**

Support can dominate.

Public duty can trespass.

Authority must still answer questions of consent, competence, jurisdiction, and accountability.

### Chinatsu recognizes the danger too late

The Prefect Team sees Abydos preparing to fight.

A line promoted as Chinatsu dismisses four opponents against company-scale force, though the attribution is linguistically suspect and remains quarantined.

Iori then says the Prefect Team cannot decline a fight that has been offered and orders battle readiness.

Chinatsu notices what the Prefect Team initially classifies as a civilian on the Abydos side.

Recognition follows:

> `……あ、あの方は……まさかシャーレの[USERNAME]先生！？`

Iori does not know what Schale is.

Chinatsu immediately says:

> `……この戦闘、行ってはいけません！`

This demonstrates uneven institutional knowledge **inside the same coercive organization**.

Chinatsu's Prologue encounter with Sensei gives her information Iori lacks.

Before she can stop events, a Prefect Team member reports Abydos approaching and opens fire.

The battle begins.

The scene therefore ends with a failure of institutional control at multiple levels:

- no consultation with Abydos before entry;
- no shared understanding of Schale inside the Prefect Team;
- a procedural objection from Chinatsu unable to stop momentum;
- and armed personnel initiating fire before the internal warning fully propagates.

## Scene 2 — Defeat, recognition, and supervisory correction

The second scene opens with Iori shocked:

> `な、なに？！私たちが負けただと？！`

The episode does not provide a detailed tactical reconstruction of the engagement.

What it does provide is Chinatsu's interpretation.

Sensei greets her:

> `久しぶり、チナツ。`

Chinatsu replies that meeting again in this form is unfortunate and says:

> `先生がそこにいらっしゃることを知った瞬間、勝ち目はないと判断して後退するべきでした……私たちの失策です。`

This is the strongest explicit statement so far about Sensei's tactical reputation from someone who has already fought under/alongside Sensei in the Prologue crisis.

It does **not** establish personal combat supremacy.

It establishes that Chinatsu treats Sensei's presence as a decisive operational variable capable of making a company-scale force's engagement unwinnable.

That materially strengthens the existing model:

> **Sensei = vulnerable noncombatant/adult + exceptional command/coordination multiplier + privileged institutional actor.**

Those traits coexist rather than cancel one another.

### Ayane immediately converts battlefield victory into institutional procedure

After the Prefect Team loses, Ayane does not merely gloat or demand surrender.

She identifies herself formally:

> `アビドス対策委員会の奥空アヤネです。所属をお願いします。`

This is a revealing move.

Her concern throughout the episode has been political status and jurisdiction. Once Abydos has physically stopped the intervention, she immediately seeks to regularize the encounter through institutional identification.

That is a strong character/institutional signal:

> Ayane uses force to defend jurisdiction, then returns to procedure.

This separates territorial self-defense from generalized anti-institutionalism.

### Ako enters as administrative authority

A communication interrupts.

The promoted layer contains a probable attribution anomaly immediately before Ako's voice becomes explicit, but the unambiguous portion begins when Ako identifies herself:

> `こんにちは、アビドスの皆様。私はゲヘナ学園所属の行政官、アコと申します。`

She then asks permission to explain the situation:

> `今の状況について少し説明させていただきたいと思いますが、よろしいでしょうか？`

This is structurally the opposite of Iori's earlier:

> `説明？必要か、それ？`

Ako's first act is not another attack.

It is **self-identification + request to explain**.

That does not retroactively legitimate the Prefect Team's earlier incursion. But it changes the institutional mode from unilateral coercion toward accountable communication.

Iori becomes visibly uncomfortable.

Ako then tells her where to find the reflection-letter template:

> `イオリ。反省文のテンプレートは私の机の、左の引き出しにあります。ご存じですよね？`

At the E020 boundary, the safest inference is:

> **Ako regards Iori's conduct as sufficiently problematic to warrant internal disciplinary correction.**

E020 does not yet tell us exactly which instruction was violated or whether responsibility lies only with Iori.

### Haruka closes the chapter by refusing closure

While everyone is gathered for institutional explanation, Haruka notices the concentration of people.

Her posture changes.

She says:

> `ああ、みんな集まってます。`
>
> `……チャンスですね。`

Then repeats:

> `許さない……`

again and again.

The precise target and next action remain unstated at the Chapter 1 boundary.

This is thematically fitting.

The episode has just tried to move from coercion into explanation, but Haruka's unresolved grievance/loyalty logic threatens to re-open violence before deliberation can stabilize the scene.

Chapter 1 therefore closes with **institutional procedure newly possible but not yet secure**.

---

# 3. Central theses

## Thesis 1 — Legitimate coercion requires more than an official target and official status

E020's strongest political statement is Ayane's distinction between:

- the truth that PS68 caused trouble;
- and the separate question of whether Gehenna has authority to conduct armed enforcement inside Abydos territory without permission.

This yields a provisional institutional principle:

> **Wrongdoing does not erase jurisdiction.**

An actor can be genuinely culpable and still be subject to an illegitimate arrest/intervention process.

That is an unusually important distinction for the series' political ethics because it prevents outcome-based reasoning from swallowing procedure.

## Thesis 2 — E016's asymmetric-power warning is confirmed, but not fatalistically

Hoshino warned that near-defunct Abydos might lack the power to control actions by giant academies such as Trinity or Gehenna.

E020 presents almost exactly that scenario:

- major academy;
- official armed body;
- company-scale force;
- tactical action inside Abydos territory;
- no prior Abydos permission;
- assumption that resistance can simply be crushed.

So `BA-C016` strengthens sharply.

However, one important correction is necessary.

Hoshino's warning was about **practical inability to control** the stronger institution. E020 shows Abydos successfully resisting once Sensei is present.

Therefore:

> **Power asymmetry creates the domination risk; it does not make domination inevitable.**

Schale's role becomes especially revealing. Sensei does not replace Abydos's judgment. Instead, Sensei's presence helps restore enough practical capacity for Abydos to enforce the decision it makes for itself.

This is perhaps the clearest interaction yet between `BA-C003`, `BA-C007`, `BA-C010`, and `BA-C016`.

## Thesis 3 — Schale can increase local autonomy without becoming the local sovereign

Sensei's first choice asks whether PS68 should simply be handed over.

The committee refuses that route and constructs its own jurisdictional argument.

Sensei then becomes a decisive force multiplier in the engagement, according to Chinatsu.

The sequence is therefore:

> **Sensei opens deliberation → students decide → student institution articulates legal/political basis → Sensei-enabled capacity makes that decision enforceable.**

That is very different from:

> adult decides → students obey.

E020 therefore gives the strongest Chapter 1 evidence so far for Schale as an **autonomy-enabling external institution** rather than a replacement sovereign.

---

# 4. Scene-by-scene close reading

## 4.1 `うちの風紀` — Kayoko's institutional familiarity

Kayoko's `うちの風紀の連中` is compact but important.

PS68's outlaw performance does not place it outside all institutional identity. Kayoko still speaks of the Prefect Team as belonging to the same `うち` frame.

This strengthens the reading of PS68 as a deviant/internal Gehenna organization rather than a wholly extra-academic criminal polity.

## 4.2 `公務の執行` — Iori's officialist vocabulary

Iori frames the mission as execution of `公務`.

The term does real ideological work.

It converts:

- academy disciplinary pursuit;

into:

- presumptively legitimate public action.

Her next move makes the danger visible:

> obstruct official action → become enemy.

E020 does not accept that syllogism uncritically.

## 4.3 `説明` — Chinatsu's procedural counterweight

Chinatsu repeatedly embodies a more procedural institutional instinct.

Her proposal that explanation should come first establishes a meaningful internal check:

> coercive capacity does not eliminate the need to communicate with affected outsiders.

This makes her later recognition of Sensei consistent with a broader risk/procedure orientation rather than mere personal deference.

## 4.4 Nonomi understands institutional violence as political violence

Nonomi's distinction between the Prefect Team and ordinary armed clubs is conceptually sophisticated.

She understands that the identity of the shooter changes the meaning of the shot.

This expands her model beyond optimism/caretaking into institutional awareness.

## 4.5 Hoshino's silence is now an institutional absence

Earlier Hoshino delegated routinely.

E020 is different because the committee actively seeks him during a jurisdictional crisis and cannot reach him.

His absence is therefore not just physical.

It creates a test of succession/distributed authority.

Ayane, Shiroko, Nonomi, and Serika pass that test.

## 4.6 Shiroko supplies the decision; Ayane supplies the constitutional argument

Shiroko says the Prefect Team must be stopped.

Ayane then explains why.

This is a useful differentiation of group cognition:

- **Shiroko:** decision under operational constraint;
- **Ayane:** institutional/legal articulation;
- **Nonomi:** political-risk recognition;
- **Serika:** rights/grievance translation.

The committee functions as a distributed reasoning system.

## 4.7 Serika's `私たちの獲物` becomes jurisdictional ownership

Serika initially says PS68 is `私たちの獲物`.

That phrasing is comic and possessive.

But after Ayane's explanation it becomes something more principled:

> `便利屋を罰するのは私たち！`

The same emotional energy is redirected into a political claim: punishment must proceed through the institution whose territory/community was harmed.

Her reasoning is less abstract than Ayane's, but it is not wholly different.

## 4.8 `許可もなく` is the key phrase

Ayane's strongest term is not merely `暴挙`.

It is:

> `私たちの許可もなく`

Without our permission.

That phrase makes consent/jurisdiction explicit and directly operationalizes E016's recipient-control concern.

## 4.9 Chinatsu sees Sensei first as civilian, then as strategic variable

The sequence is revealing.

Chinatsu first says a civilian is visible on the Abydos side.

Then she recognizes Sensei.

Then she says the battle must not happen.

After defeat, she adds that Sensei's presence should have been enough to conclude they could not win.

Sensei therefore occupies a dual status:

- physically vulnerable non-student/noncombatant adult;
- strategically decisive coordination actor.

This duality has been present since the Prologue and is now explicitly recognized by another institution.

## 4.10 Iori does not know Schale

Iori's `シャーレ？なんだそれ？` is important institutional evidence.

Schale's legitimacy/reputation is not uniformly distributed across Kivotos.

Chinatsu has direct experience.

Iori lacks even baseline recognition.

Thus “institutional knowledge” cannot be treated as academy-wide omniscience.

## 4.11 Ayane returns to procedure immediately after victory

`所属をお願いします` is not decorative formality.

It demonstrates what Abydos was fighting for.

The goal was not destruction of the Prefect Team.

The goal was to stop unilateral action and force the encounter back into an accountable institutional channel.

## 4.12 Ako's entrance partially repairs process, not substance

Ako does three things quickly:

1. identifies herself and institution;
2. asks permission to explain;
3. signals internal discipline toward Iori.

This is procedural repair.

But because E020 ends before the explanation, it would be premature to conclude that Gehenna's substantive justification is adequate.

## 4.13 Haruka remains the danger of unprocessed internal affect

Haruka's repeated `許さない` mirrors Serika's E019 title language in form but not yet in clear target/reason.

The repetition is obsessive rather than deliberative.

Institutional actors are finally trying to talk; Haruka sees a tactical opportunity.

That contrast keeps the autonomy/communication problem alive inside PS68.

---

# 5. Character-state analysis

## Ayane

E020 is Ayane's strongest political/institutional episode so far.

### Trait
Procedural, evidentiary, institution-conscious.

### State
Operating under leader absence in a high-risk inter-academy confrontation.

### Strategy
- refuse unsupported assumptions about Prefect intent;
- distinguish culpability from jurisdiction;
- insist on permission/autonomy;
- after victory, demand formal affiliation.

### Value
Abydos's institutional right to govern events inside its own district.

### Desire
Prevent a stronger academy from converting superior force into de facto authority.

### Fear
Political conflict and erosion of Abydos autonomy.

### Self-concept
Not merely operator/secretary, but authorized representative of the `アビドス対策委員会`.

### Contradiction
She is willing to use force to defend procedural order.

### Development
Administrative competence has become constitutional reasoning.

## Shiroko

Shiroko again supplies decision under uncertainty.

She does not spend long debating the Prefect Team's institutional legitimacy. Once the available options are clarified, she says:

> `風紀委員会を阻止する。`

Her operational decisiveness is then stabilized by Ayane's political reasoning rather than replacing it.

This is important because Shiroko's action-orientation can look normatively thin when isolated. In the committee, it becomes one component of a distributed decision process.

## Nonomi

Nonomi's E020 contribution is institutional rather than merely emotional.

She recognizes that the Prefect Team's formal status raises the stakes from local combat to possible political conflict.

She also seeks Hoshino before escalation, showing that her caution includes respect for existing leadership channels.

Her uncertainty—`私たちはどうすれば`—should not be read as incapacity. It is appropriate caution before crossing into inter-academy armed conflict.

## Serika

Serika fuses personal and political grievance.

She wants PS68 punished for Shiba Seki, but she rejects Gehenna doing the punishing.

Her language of `私たちの学校の権利` is less formal than Ayane's `許可`/`政治的紛争`, but it gives emotional force to the same sovereignty claim.

## Hoshino

Hoshino is absent but materially important.

The text now establishes that his unreachability is unusual.

Given the E017 Black Suit encounter, a causal relation is an important open hypothesis, but it remains unproved.

His absence also demonstrates that the committee can act politically without him.

## Kayoko

Kayoko's immediate recognition of `うちの風紀` confirms high institutional familiarity.

She understands the danger before Abydos does and attempts withdrawal/concealment.

No E020 line explains the full basis of her knowledge or personal history with the Prefect Team; later material must not be backfilled here.

## Chinatsu

Chinatsu emerges as the Prefect Team's procedural brake.

Directly supported features:

- proposes explanation before coercion;
- notices/flags the civilian on the opposing side;
- recognizes Sensei/Schale;
- urgently argues the battle should not proceed;
- after defeat, accepts operational error and says Sensei's presence should have triggered withdrawal.

Two promoted lines clash sharply with this register and remain attribution-anomaly quarantines.

## Iori

Iori's current model becomes clearer:

- mission-first;
- aggressive;
- officialist;
- quick to collapse obstruction into enemy status;
- limited awareness of Schale;
- willing to escalate against outsiders;
- then visibly subordinate/embarrassed when Ako enters.

E020 does not yet establish the exact scope of her orders, so “rogue officer” would be premature.

## Ako

Ako enters only at the end but with immediate institutional weight.

Her formal self-identification as `ゲヘナ学園所属の行政官` and her ability to reprimand Iori suggest supervisory authority.

Her first mode is communicative rather than kinetic:

> ask permission to explain.

That makes her a useful contrast with Iori, but E020 alone is insufficient for a mature Ako model.

## Haruka

Haruka ends the chapter still operating through affective/loyalty-driven escalation.

She sees everyone gathered, interprets it as a `チャンス`, and repeats `許さない` obsessively.

The target and intended act remain open.

This preserves the E018–E019 pattern: Haruka's loyalty and grievance can bypass deliberative confirmation.

## Sensei

E020 strongly develops Sensei without making Sensei the source of Abydos's political reasoning.

- raises a question rather than issuing the sovereignty decision;
- remains present as a civilian/non-student adult;
- is recognized by Chinatsu from the Prologue;
- is treated by Chinatsu as a decisive strategic variable;
- participates in a victory that restores Abydos's ability to control its own territory.

The result is **autonomy amplification**, not replacement sovereignty.

---

# 6. Relationship-state analysis

## Sensei ↔ Chinatsu

The Prologue relationship reactivates explicitly.

Sensei says `久しぶり`.

Chinatsu responds with recognition and regret about the circumstances.

More importantly, she has developed a strong operational expectation about Sensei:

> if Sensei is present, the probability of victory changes dramatically.

This is experiential legitimacy/reputation, not abstract federal title alone.

## Sensei ↔ Abydos committee

E020 is one of the strongest demonstrations yet that trust does not require adult command monopoly.

The committee is willing to make a politically dangerous decision while Sensei is present, and Sensei does not overwrite it.

## Abydos ↔ PS68

The relationship remains antagonistic because of Shiba Seki, but E020 produces a limited convergence of interests.

Abydos refuses to hand PS68 to Gehenna because:

- local jurisdiction matters;
- Abydos still wants its own reckoning;
- and PS68 remains connected to unresolved sponsor questions.

This is not forgiveness or alliance.

It is **jurisdictionally mediated protection from third-party seizure**.

## Abydos ↔ Gehenna Prefect Team

The relationship begins as unilateral armed intrusion and shifts, after defeat, toward formal dialogue.

That shift is still provisional at the episode boundary.

## Iori ↔ Chinatsu

The pair displays internal institutional differentiation.

Iori privileges mission execution and force.

Chinatsu repeatedly introduces procedure, explanation, recognition, and caution.

## Iori ↔ Ako

Ako's appearance immediately changes Iori's affect.

The reflection-letter remark indicates accountability inside the Prefect Team rather than perfectly unified command.

The exact command fault remains open.

---

# 7. School / club / institution state

## Abydos / Countermeasures Committee

E020 upgrades Abydos from a survival organization into an actor explicitly articulating **territorial-political autonomy**.

Current institutional capacities now include:

- debt management;
- security operations;
- evidence acquisition;
- political-economic inference;
- community protection;
- inter-academy threat recognition;
- jurisdictional reasoning;
- and enforcement of local autonomy.

This sharply strengthens the rejection of “student governance = inherently incapable.”

## Gehenna Prefect Team

E020 establishes the Prefect Team as:

- a formally recognized coercive institution;
- capable of company-scale deployment;
- equipped with indirect fire;
- empowered to pursue Gehenna rule violators;
- internally differentiated in procedural judgment;
- and subject to administrative supervision/accountability.

But its extraterritorial jurisdiction is **not established**.

Indeed, Abydos explicitly contests it.

## Problem Solver 68

PS68 remains a Gehenna-connected but institutionally deviant organization.

Kayoko's `うちの風紀` confirms shared academy frame; Prefect Team pursuit confirms PS68 is subject to Gehenna disciplinary attention.

E020 still does not resolve PS68's sponsor/client architecture.

## Schale

Schale's functional role becomes clearer:

> **external capacity that can prevent a stronger institution from simply converting force superiority into authority over a weaker local institution.**

This is a strong autonomy-enabling model.

---

# 8. Sensei role and choice-space

## Choice 1 — `じゃあ便利屋をこのまま風紀委員会に引き渡しちゃう？`

This choice should not be overread as Sensei's settled preference.

Its narrative function is interrogative.

It makes the committee articulate why the apparently easiest solution is unacceptable.

The response belongs to the students.

This is significant for `BA-C008`: choice-space again shapes ethical/persona participation without creating a divergent route.

## Choice 2 — `久しぶり、チナツ。`

This choice reactivates memory/relationship rather than strategy.

It places Sensei inside a persistent social network across institutions.

## Ethical role

E020's Sensei ethics can be summarized as:

> **lend capacity without appropriating jurisdiction.**

Sensei's presence materially alters the balance of power, but Abydos supplies the political judgment and local claim of right.

---

# 9. Japanese-language and voice analysis

## Ayane

Key lexical field:

- `友好的とは判断しかねます`
- `政治的紛争`
- `戦術的行動`
- `許可もなく`
- `暴挙`
- `所属をお願いします`

This is strongly institutional/administrative Japanese.

Ayane does not merely say “they're bad” or “fight them.” She names categories of action, jurisdiction, and political consequence.

## Iori

Key language:

- `公務の執行`
- `全員敵`
- `問答無用`
- `まとめて叩きのめす`
- `売られた喧嘩`

Her register compresses legal/official status and aggressive colloquial violence.

That combination is character-defining: formal mission vocabulary does not soften her combativeness.

## Chinatsu

Clean surrounding lines use:

- `事情を説明するのが先かと`
- `確認中ですので、お待ちください`
- `この戦闘、行ってはいけません`
- `失策です`

This is cautious, procedural, and evaluative.

The two anomalously promoted rough lines should not be used to overwrite that pattern.

## Nonomi

Nonomi uses formal institutional distinction surprisingly naturally:

- `公認武力集団`
- `性質が異なります`
- `政治的な紛争の火種`

Her soft social persona therefore coexists with sophisticated political vocabulary.

## Serika

Serika translates abstract sovereignty into emotional ownership:

- `私たちの獲物`
- `私たちの学校の権利`
- `罰するのは私たち`

She makes the constitutional claim socially immediate.

## Ako

Ako's entry is formally polished:

- `ゲヘナ学園所属の行政官`
- `説明させていただきたい`
- `よろしいでしょうか`

Her politeness contrasts sharply with the violence that preceded her communication.

## Haruka

Haruka's closing repetition:

> `許さない……許さない……`

abandons explanatory syntax almost completely.

Language collapses into obsessive affect.

---

# 10. Motifs, symbols, and structural callbacks

## 10.1 Labels versus legitimacy

E016: `サポートするという名目`

E020: `公務の執行`

Both involve normatively positive/official labels attached to power.

Both are subjected to the same test:

> What control does the affected party retain?

## 10.2 Permission / refusal / control

E016–E020 form a coherent chain:

- weak Abydos may not be able to control powerful helpers;
- Aru protects PS68's ability to refuse clients;
- Black Suit threatens Hoshino with an unrefusable proposal;
- Haruka bypasses confirmation inside PS68;
- E020 makes `許可もなく` the explicit territorial form of the same problem.

The autonomy motif is now one of the strongest longitudinal structures in Chapter 1.

## 10.3 Hospitality space → battlefield → diplomatic table

Shiba Seki began as ordinary hospitality.

Its destruction produced polarized combat.

The combat attracted formal coercive power.

After defeat, Ayane and Ako attempt to transform the battlefield into an institutional conversation.

The arc repeatedly converts spaces between:

> ordinary life ↔ violence ↔ procedure.

## 10.4 Hoshino absent / distributed committee present

The committee's ability to articulate and defend sovereignty while its chair is unreachable is a structural callback to the earlier distribution of labor that E017 highlighted.

---

# 11. Violence, ethics, law, and power

E020 presents four different theories of legitimate force.

## Iori — mission-authorized coercion

Official duty grants broad authority; obstruction legitimates force.

## Chinatsu — proceduralized coercion

Official mission may justify enforcement, but explanation, identification, situational awareness, and civilian risk matter first.

## Abydos — territorial/jurisdictional coercion

PS68 wrongdoing can justify punishment, but the local institution retains authority over what happens inside its territory.

## Sensei/Schale — enabling force without jurisdictional seizure

Sensei helps make Abydos's decision enforceable but does not claim Abydos's right for Schale.

The episode does not fully adjudicate all four theories, but the narrative gives strong weight to the latter three over Iori's initial `問答無用` model.

### Political-legal principle

A useful formulation is:

> **Substantive guilt and procedural legitimacy are separable.**

PS68 can have committed a wrong.

Gehenna can have a legitimate disciplinary interest in PS68.

Abydos can still be justified in rejecting an armed extraterritorial operation conducted without notice or consent.

This is the episode's most rigorous institutional insight.

---

# 12. Competing readings and counterevidence

## Reading A — Abydos is simply being possessive because it wants revenge on PS68

Evidence:

- Serika says `便利屋は私たちの獲物`;
- Serika insists Abydos should punish them for Shiba Seki.

Counterevidence:

- Nonomi independently raises political-conflict risk before the fight;
- Ayane explicitly concedes PS68 wrongdoing and then separately argues jurisdiction/permission;
- Ayane later seeks formal affiliation after victory.

**Assessment:** revenge is present, especially in Serika, but cannot explain the committee's full reasoning.

## Reading B — The Prefect Team is obviously legitimate because it is pursuing Gehenna delinquents

Evidence:

- PS68 is Gehenna-connected;
- Iori calls the operation `公務`;
- the Prefect Team is a formal disciplinary body.

Counterevidence:

- Chinatsu says explanation should come first;
- Abydos was inside the bombardment envelope;
- no Abydos permission was obtained;
- Ako's arrival immediately shifts toward explanation and signals disciplinary concern toward Iori.

**Assessment:** Gehenna has a plausible disciplinary interest, but E020 does not establish unrestricted extraterritorial jurisdiction. Official status is insufficient by itself.

## Reading C — Sensei simply decides to fight Gehenna and students follow

Counterevidence:

- Sensei's first choice suggests the opposite possibility: hand PS68 over;
- Shiroko rejects that route;
- Ayane supplies the political basis;
- the students choose resistance before Sensei issues any directive in text.

**Assessment:** contradicted by scene structure.

## Reading D — Hoshino is definitely absent because Black Suit detained him

Evidence:

- E017 ends with Black Suit confronting Hoshino;
- E020 says Hoshino is abnormally unreachable.

Counterevidence:

- no explicit causal statement;
- E020 never mentions Black Suit.

**Assessment:** strong open hypothesis, not established fact.

## Reading E — E020 proves Sensei is personally invincible

Counterevidence:

- Chinatsu's statement concerns the tactical consequence of Sensei's presence;
- prior evidence consistently shows Sensei physically vulnerable and dependent on student combatants;
- no personal combat feat is shown here.

**Assessment:** reject. E020 strengthens command/coordination reputation, not personal-force supremacy.

---

# 13. Cumulative ledger deltas

## Character ledger

- **Ayane:** major strengthening — jurisdictional/constitutional reasoning, formal representation, post-combat proceduralization.
- **Shiroko:** operational decisiveness remains strong; supplies decision under uncertainty.
- **Nonomi:** institutional-political literacy strengthens; recognizes formal armed-body escalation risk.
- **Serika:** personal grievance and local-rights defense become fused.
- **Hoshino:** abnormal unreachability becomes explicit; cause remains OPEN.
- **Kayoko:** Gehenna/Prefect familiarity strengthens.
- **Chinatsu:** procedural/risk-mitigation role and Sensei recognition strengthen; two speaker anomalies quarantined.
- **Iori:** officialist/aggressive enforcement style established; Schale ignorance explicit.
- **Ako:** initial administrative/supervisory baseline established.
- **Haruka:** unresolved affective escalation continues.
- **Sensei:** strategic force-multiplier reputation strengthens without personal combat dominance.

## Relationship ledger

- Sensei ↔ Chinatsu reactivated from Prologue.
- Abydos ↔ PS68 becomes third-party-protection-without-forgiveness.
- Abydos ↔ Prefect Team enters armed sovereignty conflict, then provisional dialogue.
- Iori ↔ Ako shows internal accountability hierarchy.
- Sensei ↔ Abydos strengthens as autonomy-enabling support.

## Institution ledger

- Abydos explicitly asserts territorial autonomy.
- Prefect Team established as company-scale formal coercive apparatus with internal procedural disagreement.
- Schale functions as balancing capacity rather than replacement jurisdiction.
- `公務` is not accepted as self-authenticating extraterritorial authority.

## Sensei ledger

- two choices;
- first is deliberative/inquisitive, not dictatorial;
- second is relational memory;
- Chinatsu treats Sensei's presence as decisive tactical multiplier;
- Sensei remains civilian/vulnerable in classification.

## Voice ledger

- Ayane's institutional lexicon expands sharply.
- Iori's `公務` + `問答無用` mixture establishes officialist/aggressive voice.
- Chinatsu's clean lines are procedural; two rough-line attributions quarantined.
- Ako enters with polished administrative honorific register.
- Haruka's language collapses into obsessive repetition.

## Motif/theme ledger

- labels vs legitimacy (`名目` / `公務`);
- permission/refusal/control;
- local sovereignty;
- differentiated meaning of violence by institutional actor;
- procedure after force;
- distributed governance under leader absence.

---

# 14. Claim revision and chapter-closing adjudication

No new claim ID is opened at E020.

The episode is best treated as a major test of existing claims, especially `BA-C003`, `BA-C004`, `BA-C006`, `BA-C007`, `BA-C010`, `BA-C011`, and `BA-C016`.

| Claim ID | E020 transition | Effect |
|---|---|---|
| BA-C001 | **STRENGTHEN / REFINE** | responsible adulthood helps preserve student self-government rather than replacing it |
| BA-C002 | **STRENGTHEN** | Chinatsu's prior experience with Sensei produces concrete cross-school operational trust/reputation |
| BA-C003 | **STRENGTHEN SHARPLY** | Schale enables Abydos to defend its jurisdiction while Abydos itself decides the policy |
| BA-C004 | **STRENGTHEN SHARPLY / REFINE** | Chinatsu treats Sensei as a decisive command/coordination variable; no personal-force dominance established |
| BA-C005 | **PRESERVE REJECTED** | Sensei's importance is relational/command-based, not omnipotence |
| BA-C006 | **STRENGTHEN REJECTION SHARPLY** | students independently articulate sovereignty, jurisdiction, political risk, and procedure under leader absence |
| BA-C007 | **STRENGTHEN** | service/restraint becomes autonomy amplification: Sensei adds capacity without seizing the local decision |
| BA-C008 | **STRENGTHEN** | choice-space elicits ethical/institutional reasoning rather than branching plot |
| BA-C009 | **PRESERVE** | no major technical-system ontology delta |
| BA-C010 | **STRENGTHEN SHARPLY** | legitimate authority is nonpossessive; Schale's power helps Abydos retain control rather than transferring control to Schale |
| BA-C011 | **STRENGTHEN SHARPLY** | adult usefulness and student political competence coexist directly |
| BA-C012 | **PRESERVE** | no Kaiser/Black Suit network evidence |
| BA-C013 | **PRESERVE** | no finance/proxy evidence |
| BA-C014 | **PRESERVE** | no Black Market function delta |
| BA-C015 | **PRESERVE / CONNECT** | institutional identity now includes control over the legitimate means by which local justice/governance is exercised |
| BA-C016 | **STRENGTHEN SHARPLY / CONFIRM FIRST DIRECT TEST** | stronger-academy tactical action without permission demonstrates the domination/jurisdiction risk; Abydos's agency is restored through resistance, not assumed absent |
| BA-C017 | **PRESERVE / CONNECT** | territorial `許可` is the institutional form of retained refusal/control; Haruka's closing behavior still shows weak internal deliberative control |
| BA-C018 | **PRESERVE / CONSEQUENCE CONTINUES** | Shiba Seki's destruction remains the grievance that shapes Abydos's refusal to surrender PS68 |

### BA-C003 revised provisional formulation after E020

> **Schale functions as a cross-institutional corrective and autonomy amplifier rather than a replacement sovereign. In E020 Sensei is present during an asymmetric intervention by Gehenna, but Abydos's students independently determine that the Prefect Team must be stopped and articulate the jurisdictional basis themselves. Sensei's extraordinary operational value then helps make their chosen policy enforceable. Schale therefore adds practical capacity without appropriating Abydos's decision-right.**

### BA-C004 revised provisional formulation after E020

> **Sensei's demonstrated exceptional capability is principally command/coordination and institutional leverage rather than personal combat force. Chinatsu explicitly says that once she knew Sensei was present she should have judged the engagement unwinnable and withdrawn, materially strengthening Sensei's reputation as a force multiplier. This coexists with his classification as a civilian/non-student adult and with longstanding physical vulnerability.**

### BA-C016 revised provisional formulation after E020

> **Under severe power asymmetry, legitimate intervention cannot be inferred from benevolent intent, official purpose, or the target's genuine wrongdoing. E020 gives the first direct territorial test: Gehenna's Prefect Team pursues its own problem students into Abydos territory and begins tactical operations without Abydos permission. Ayane explicitly concedes PS68 wrongdoing while rejecting Gehenna's unilateral action on jurisdictional grounds. The key legitimacy variable is therefore whether the affected institution retains meaningful agency to authorize, shape, constrain, refuse, or terminate the intervention. E020 also shows that asymmetry creates domination risk rather than inevitable domination: Schale's support allows Abydos to enforce its own refusal without transferring sovereignty to Schale.**

### E020 epistemic firewall

- **Abydos knows:** Prefect Team is Gehenna's formal armed disciplinary body; it entered with company-scale force; it acted tactically inside Abydos territory without prior permission; Chinatsu recognizes Sensei; Ako identifies herself as a Gehenna administrator and offers explanation.
- **Abydos does not yet know:** full deployment rationale/order chain; exact Ako plan; whether Iori exceeded precise orders; any causal relation between Hoshino's absence and Black Suit.
- **Prefect Team field element knows unevenly:** Chinatsu knows Sensei/Schale; Iori initially does not.
- **Sensei/project knows:** Hoshino's unavailability follows E017's Black Suit meeting in narrative chronology, but causation remains OPEN.
- **PS68 internal responsibility remains differentiated:** Haruka caused Shiba Seki's destruction; Aru later ratified it; Abydos still lacks that complete internal history.
- **Convenience-source caution:** source-side `20話_...md` omits canonical scene 2; use stable promoted two-scene projection.

---

# 15. Evidence locators

## Prefect Team purpose / Iori theory of authority

- `scene:001:u:0011` — infantry advance order;
- `scene:001:u:0012-0019` — Chinatsu/Iori dispute over Abydos and explanation;
- `scene:001:u:0014` — `公務の執行を妨害する輩は全員敵`;
- `scene:001:u:0018` — outsiders who interfere will be beaten down.

## Abydos political reasoning

- `scene:001:u:0021` — Ayane: not enough evidence to know purpose, but not friendly;
- `scene:001:u:0022` — Shiroko: Abydos was inside bombardment range;
- `scene:001:u:0025-0026` — Nonomi: formal armed body / political-conflict risk;
- `scene:001:u:0027-0029` — Hoshino unusually unreachable;
- `scene:001:choice:001` — Sensei raises hand-over option;
- `scene:001:u:0034` — Shiroko chooses to stop Prefect Team;
- `scene:001:u:0037-0042` — Ayane/Serika sovereignty and permission argument.

## Sensei / Chinatsu / battle

- `scene:001:u:0049-0055` — Chinatsu detects civilian, recognizes Sensei/Schale, tries to halt battle;
- `scene:001:u:0056-0059` — fire begins before halt;
- `scene:002:u:0001` — Iori confirms Prefect Team defeat;
- `scene:002:choice:001` — Sensei greets Chinatsu;
- `scene:002:u:0006-0007` — Chinatsu says Sensei's presence should have triggered withdrawal.

## Ayane procedural follow-through / Ako entrance

- `scene:002:u:0008` — Ayane formally identifies herself and requests affiliation;
- `scene:002:u:0011-0015` — communication/Ako identification;
- `scene:002:u:0014-0015` — Ako self-identifies and requests permission to explain;
- `scene:002:u:0016-0018` — Iori discomfort / reflection-letter reprimand.

## Haruka cliffhanger

- `scene:002:u:0019-0026` — gathers herself, notices everyone assembled, calls it a chance, repeats `許さない`.

---

# 16. Conclusion and next boundary

E020 closes Chapter 1 by making its political ethics explicit.

The episode's most important proposition is not “Abydos beats Gehenna.”

It is:

> **An institution does not gain legitimate authority over another institution merely because its target is guilty, its purpose is official, or its force is overwhelming.**

Ayane's reasoning is unusually clean:

- PS68 probably did wrong;
- Gehenna may legitimately care about its own delinquent students;
- but unilateral armed action inside Abydos territory without Abydos permission remains unacceptable.

This is the concrete territorial realization of the autonomy problem developed across E015–E019.

At the same time, Sensei's role becomes more precise.

Sensei is powerful enough that Chinatsu believes the Prefect Team should have withdrawn on recognition alone. Yet Sensei does not become the source of Abydos sovereignty. The committee chooses, reasons, and formally represents itself. Sensei supplies the capacity that prevents a larger institution from making local consent irrelevant.

That is the strongest Chapter 1 evidence yet for:

> **Schale as an institution that can increase another institution's practical autonomy without possessing it.**

Several questions remain deliberately unresolved at the chapter boundary:

- Hoshino's abnormal absence and Black Suit;
- Ako's full explanation and command structure;
- the eventual jurisdictional settlement;
- Haruka's closing action;
- PS68 responsibility and long-term reconciliation;
- Kaiser/Black Suit ultimate architecture.

Because `MAIN_V001_C001` is now complete, the next mandatory analytical artifact is **not Chapter 2 E001**.

It is:

> **`BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md`**

The checkpoint should use **GPT-5.6 Sol Extra High** if available and should adversarially reconcile E001–E020, especially:

1. responsible adulthood versus student political competence;
2. Schale as corrective/autonomy amplifier rather than replacement sovereign;
3. debt/Kaiser/proxy evidence architecture and remaining firewalls;
4. Hoshino's ethical/political development and hidden Black Suit exposure;
5. PS68's performed outlaw identity, contract ethics, command failures, and emerging relational ties;
6. autonomy/refusal/permission as a cross-cutting Chapter 1 structure;
7. Shiba Seki as relational infrastructure;
8. formal coercion, jurisdiction, and inter-academy sovereignty;
9. Sensei's tactical reputation versus physical/non-omniscient limitations;
10. every `BA-C001`–`BA-C018` claim transition, including whether any should be strengthened, narrowed, merged, downgraded, or left open before Chapter 2.
