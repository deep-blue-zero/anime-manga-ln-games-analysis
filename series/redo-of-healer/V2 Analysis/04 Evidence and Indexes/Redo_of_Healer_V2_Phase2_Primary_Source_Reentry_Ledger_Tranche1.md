# Redo of Healer — V2 Phase 2
## Targeted Japanese Primary-Source Re-entry and Locator Ledger — Tranche 1
### Volumes 1–10: core longitudinal claims, corrections, and reusable evidence anchors

**Project:** 『回復術士のやり直し』 / *Redo of Healer*  
**Scope:** Japanese light novels Volumes 1–10  
**Governing protocol:** `Redo_of_Healer_V2_Synthesis_Expansion_Protocol.md`  
**Prior phase:** `Redo_of_Healer_V2_Phase1_V1_Audit.md`  
**Current phase:** Phase 2 — targeted primary-source re-entry  
**Tranche status:** Core evidence tranche. No V2 specialist document has yet been rewritten.

---

# I. Purpose

Phase 2 exists to prevent V2 from becoming a longer paraphrase of V1.

The V1 audit identified several mature interpretations that were plausible or persuasive but insufficiently demonstrated in the final 37.6k-word corpus. This tranche therefore returns directly to the Japanese EPUBs and constructs reproducible evidence paths for the highest-value claims before specialist expansion begins.

The operative chain is:

> **planned V2 claim → verified scene → volume/chapter/XHTML/paragraph locator → Japanese primary source**

The goal is not to maximize quotations. It is to establish enough reliable anchors that V2 can demonstrate its arguments without relying on memory, the prior chat, or the compressed V1 wording.

This tranche concentrates on the claims most likely to control Documents 02–07:

- Keyaru → Keyarga → integrated Keyaru;
- apples, food, home, and nourishment;
- first-timeline objectification;
- Freia/Flare and Ellen/Norn personhood;
- Setsuna, Kureha, Ragna, Lapis, and agency;
- Bullet as teacher and dark mirror;
- Branica, Jioral, Eve's order, Panakeia, and statecraft;
- healing, conceptual restoration, Hero/Demon King rules, divine beasts, and world reset;
- Volume 8 irreplaceability;
- Volume 9 post-revenge identity and monarchy;
- Volume 10 bodily compulsion, higher-rule architecture, Bullet's final override, and the second redo.

---

# II. Source identity and reproducibility

The original Japanese EPUBs remain the governing primary sources.

## Source SHA-256

| Volume | SHA-256 |
|---|---|
| 1 | `07a504a927a4355c2c5ccd50118cee8bb7a8b88c680190d1ae074ac7995f9199` |
| 2 | `1ede56845c10d83b264dc354fa50d3799e935842e38b68e5de8791ae46d68a7b` |
| 3 | `0a6088b699e9dad0bfa1083b1b3da95e4d91fc42c4e1eba2187f14e6d40d36b7` |
| 4 | `622ee687d210048bdcee8300c0ac0eff62e4623e6816865666f03936aa8d38d1` |
| 5 | `6a77044c4deb9bfcb7c9b82e19c9735f26d844455cdc6d580981dc147dd463d9` |
| 6 | `8a02424f617efab9288b530c30b21141358de6dfafe3a8d6b3441d8f27dc8856` |
| 7 | `e955902938682119296a4156b58c927d3fdc49d186e8b136a3fb440995ff0bc1` |
| 8 | `f16e4a0192309d4762e1213d7ff8dd67171a0f5f33a42a73acdf760cb85a2c17` |
| 9 | `ad927e61c1de36d9c200f6b06e66500a5210ba6dc87dea0f3d31eaa212ded81c` |
| 10 | `dfd97c3f79c2250e07130c006bac3770297fec1f3d7d82762fd2bdf989f9fa95` |

## Locator convention

The EPUBs are structurally clean.

Volumes 1–9 use narrative XHTML files under:

`item/xhtml/p-XXX.xhtml`

Volume 10 uses:

`OEBPS/Text/p-XXX.xhtml`

For the analytical ledger, the stable human-readable locator is written as:

> **V[volume] — [chapter title] — `p-XXX.xhtml` ¶[normalized paragraph number]**

The paragraph number is the ordinal position of the non-empty `<p>` element in that XHTML file after whitespace normalization. It is **not** a publisher page number. It is an internal analytical locator designed to be reproducible from the exact frozen EPUB identified above.

Volume 10 has an especially important source boundary:

- `p-001.xhtml` through `p-023.xhtml` belong to *Redo of Healer*;
- `p-024.xhtml` onward begins the unrelated promotional sample 『捨てられエルフさんは世界で一番強くて可愛い！』 and remains excluded.

---

# III. Evidence status

This tranche uses the V2 protocol's epistemic distinctions:

- **TF — Textual fact:** directly established by narration, dialogue, event, or explicit system rule.
- **SI — Strong inference:** supported by multiple independent textual signals but not stated as one formal rule.
- **SP — Speculation:** plausible but unresolved.
- **VJ — Value judgment:** ethical, political, or literary evaluation.

A major function of Phase 2 is to downgrade claims that V1 phrased too confidently and upgrade claims that turn out to have stronger Japanese support than expected.

---

# IV. Major Phase-2 corrections to the Phase-1 map

## Correction 1 — “conceptual healing” is explicitly textual

Phase 1 conservatively treated “conceptual healing” as potentially only our analytical label.

That caution is no longer necessary.

**V6 — 第十五話「回復術士は真の勇者になる」 — `p-016.xhtml` ¶13–16**

Keyaru explicitly defines healing as returning something to its **あるべき姿 / arubeki sugata** (“the state/form it ought to have”) and says:

> `勇者という概念を【回復】する`  
> “heal/restore the concept of the Hero”

The narration then explicitly calls this:

> `概念の【回復】`

Therefore:

- **TF:** `概念の【回復】` is an in-text category/formulation.
- “conceptual restoration” remains an English analytical gloss, but it is grounded directly in the Japanese text.
- Document 06 may treat conceptual healing/restoration as canonically articulated rather than merely inferred.

This materially strengthens the healing ladder.

---

## Correction 2 — the apple/nourishment thread is much earlier than the V1 compression suggested

The orchard is not a late Volume-10 motif retroactively imposed on the series.

It develops in stages.

### Volume 1 — livelihood

**V1 — 第一話「少年は夢を見る」 — `p-002.xhtml` ¶21–26, ¶40–42**

Keyaru is directly established as an apple farmer maintaining the orchard his dead parents left him.

This is initially practical identity and livelihood.

### Volume 4 — positive moral dream

**V4 — 第八話「回復術士はかつての夢を見る」 — `p-009.xhtml` ¶160–169**

Keyaru remembers his childhood intention:

- preserve his parents' orchard;
- make delicious apples and sweets;
- make people living in a harsh world happy through what he produces;
- support people even if he lacks the power to defeat monsters.

This is already far more than a food motif.

### Volume 4 — explicit Keyaru/Keyarga internal conflict

**V4 — 第二十話「回復術士は夢を見る」 — `p-021.xhtml` ¶3–24**

The earlier Keyaru condemns the present self:

> `僕は、おまえみたいになりたくなかった`

Keyarga answers that the old dream failed to include **his own happiness**, and that a powerless healer would simply be consumed again.

This is one of the earliest direct pieces of evidence for Keyarga as a functional answer to helplessness, years before Volume 9 supplies the explicit “armor” metaphor.

### Volume 9 — identity integration

**V9 — 第六話「回復術士は王になる」 — `p-007.xhtml` ¶46–65**

The novel finally names the structure:

> `ケヤルガは俺にとって鎧だった。`

Keyaru also explicitly remembers wanting to grow delicious apples and make everyone happy, but rejects a simple restoration to his old self.

### Volume 10 — biographical causality

**V10 — 第十三話「回復術士は愛人を救う」 — `p-014.xhtml` ¶99–110**

Volume 10 adds the causal sequence:

> orchard and apple-pie happiness  
> → parents killed by monsters  
> → wish to become a Hero so others would not suffer similarly  
> → objectification in Jioral  
> → revenge identity

The crucial question becomes:

> `俺がなりたかった俺は今の俺なのか？`

### Revised V2 conclusion

The correct chronology is therefore:

> **V1 livelihood → V4 positive nourishment telos and internal contradiction → V9 explicit armor/integration → V10 causal autobiography and self-questioning**

V2 should not describe the orchard as a Volume-10 invention. Volume 10 **crystallizes** an identity structure that the novels had already made explicit.

---

# V. Volume-by-volume primary-source re-entry

# Volume 1
## Foundational objectification, Freia, Setsuna, and the first redo

### 1. First-timeline Keyaru is explicitly reduced to a usable remnant

**Locator:** V1 — 第零話「ケヤルが目覚めた日」 — `p-014.xhtml` ¶2, ¶77–82, ¶280–295

### Verified findings

**TF:** Keyaru retrospectively calls the first timeline days in which his personality was taken and he was merely used.

**TF:** Jioral's drug regimen is not simply analgesia. It produces dependency and removes the behavioral obstacles that would make him resist use as a Healing Hero.

**TF:** Keyaru later describes Flare as having taken his ego/selfhood and reduced him to a tool immediately.

### V2 implications

Document 02 should distinguish at least five objectification vectors:

1. **Healing instrument** — value measured by healing output.
2. **Pain sink** — his subjective suffering matters only as an obstacle to utility.
3. **Drug-dependent resource** — chemistry is used to keep the resource available.
4. **Sexual object** — his body is treated as accessible material.
5. **State asset** — the Hero is institutionally processed as usable capacity.

The important claim is not simply “Keyaru was abused.” It is:

> **the first timeline teaches him that having a useful body without control over that body makes usefulness a route to enslavement.**

This is the foundation of his later equation of power with personhood insurance.

---

### 2. The first redo is explicitly revenge-authored

**Locator:** V1 — `p-014.xhtml` ¶317–320

Keyaru's first world reset is articulated as:

- redo the world;
- destroy the lives of those who destroyed his;
- construct specific revenge plans;
- experience joy at the prospect.

### Evidence status

- **TF:** revenge is the explicit motive of the first reset.
- **SI:** the first redo is “sole-authored” in the sense that Keyaru alone possesses the memory, the plan, and the operative historical agenda.
- **VJ:** calling this “historical authorship through domination” is analytical language.

This creates the baseline against which Volume 10's consultation must be measured.

---

### 3. Flare → Freia is memory erasure plus retained knowledge, not simple total replacement

**Locator:** V1 — 第十一話「回復術士はフレア王女を壊す」 — `p-012.xhtml` ¶204–215

### Verified findings

**TF:**

- Keyaru alters Flare's body.
- He erases autobiographical memory.
- He deliberately leaves knowledge/skills available.
- He expects “Flare” as the prior practical identity to disappear and a useful new self to emerge.

### V2 implications

Freia cannot be modeled as either:

> “exactly the same Flare with amnesia”

or:

> “a wholly unrelated person created ex nihilo.”

The textual structure is mixed:

- same body, though altered;
- retained knowledge and magical capacity;
- erased autobiographical memory;
- imposed new relational frame;
- later independently accumulated history.

Document 03 must therefore separate **physical continuity, cognitive/skill continuity, autobiographical continuity, relational continuity, and later accumulated agency**.

---

### 4. Setsuna's founding relationship is structurally coercive even when later choice becomes meaningful

**Locators:**
- V1 — 第十八話「回復術士は少女を慰める」 — `p-020.xhtml` ¶94–109, ¶153–190
- V1 — Epilogue「回復術士はセツナを手に入れる」 — `p-023.xhtml` ¶17–20, ¶94–105, ¶128–139

### Verified findings

The source supports both sides of the future V2 argument.

#### Coercive origin

**TF:**

- Setsuna has been enslaved.
- She is sick and weak.
- her community is under severe threat;
- Keyaru possesses overwhelming force;
- Keyaru removes the slave collar partly because he does not require it to control the practical relationship;
- she offers lifelong service in exchange for power/protection.

Therefore:

> **absence of memory rewriting does not equal free-origin consent.**

#### Meaningful later choice

**TF:**

- after the village is rescued, Setsuna tells her father she chooses to leave and grow stronger with Keyaru;
- she gives her true name after seeing that he fulfilled his promise;
- she later makes her own moral distinction about whom retaliation should fall upon.

This supports a deliberately mixed conclusion:

> **Setsuna's later loyalty is not fake merely because the founding conditions are coercive; the later loyalty also cannot retroactively cleanse those founding conditions.**

---

# Volume 2
## Kureha, justice, and Keyaru's self-aware moral theater

### 1. Kureha's justice is genuinely destabilized

**Locator:** V2 — 第七話「回復術士は剣聖を慰める」 — `p-008.xhtml` ¶31, ¶65

Kureha says she had believed fighting for the kingdom was justice, then discovers that the kingdom itself may be evil. She explicitly says she must rethink:

- what justice is;
- what her sword should serve.

### Evidence status

- **TF:** justice is a genuine Kureha concern.
- **SI:** Kureha operates as a moral counterweight because she continues to ask whom power ought to serve.
- **Caution:** this does not yet make her a developed constitutional theorist.

---

### 2. Keyaru explicitly knows Kureha's “justice” reading of him is false

**Locator:** V2 — 第十四話「回復術士は笑顔を引き吊らせる」 — `p-015.xhtml` ¶81–88

Keyaru internally says he possesses essentially no justice ethic and describes himself through appetite, anger, violence, and desire. Kureha nevertheless tells him she sympathizes with his justice.

This is a highly useful narration anchor.

### V2 implication

The difference between:

- **how allies morally narrate Keyaru**, and
- **how Keyaru privately narrates his own motives**

must remain visible.

Later growth should not be projected backward into Volume 2.

---

### 3. “Justice” becomes theater

**Locator:** V2 — 第十九話「回復術士は正義を執行する」 — `p-020.xhtml` ¶101–122

Keyaru publicly calls his retaliation “justice,” while the earlier private narration has already disclaimed a principled justice ethic.

### V2 implication

This is useful for Documents 02, 07, and 08:

> **Keyaru can deploy justice vocabulary rhetorically while remaining aware that his actual permission structure is retaliatory and personal.**

---

# Volume 3
## Branica, Norn, and the instability of the early moral map

### 1. Branica is a concrete counterexample, not merely lore

**Locator:** V3 — 第二話「回復術士は魔王と出会う」 — `p-003.xhtml` ¶51–63, ¶115–116

Keyaru sees:

- humans and demons living together;
- humans and demons drinking together;
- exchange relations that complicate the simple predator/prey model.

He concludes:

> `共存共栄、ブラニッカは頭のいいやり方をしている。`

### Evidence status

- **TF:** coexistence is materially real.
- **VJ:** Branica should not be romanticized as utopia.
- **SI:** it becomes a living counterexample to the premise that species conflict is politically inevitable.

This is one of the textual roots of the later human-demon peace project.

---

### 2. Early coexistence language is still partly instrumental

**Locator:** V3 — later Eve/Branica planning passages in the same volume

Keyaru can speak in favor of coexistence while also privately treating parts of that language as useful for placing Eve on the Demon King path.

### V2 implication

Document 05 should show development:

> **coexistence begins as something Keyaru can recognize as intelligent and useful before it becomes part of the world he actively wants to preserve.**

Do not back-project Volume 9 sincerity into Volume 3.

---

### 3. Norn's violence is systemic rather than merely temperamental

**Locators:**
- V2 — 第十五話「回復術士は妹姫を追憶する」 — `p-016.xhtml` ¶148–175
- V3 — 第十八話「回復術士はノルン姫の蛮行に心を痛める」 — `p-019.xhtml`
- V3 — `p-021.xhtml` ¶64–80

Norn's defining capacity is to make coercive action politically legible:

- efficiency over humanitarian restraint;
- production of public justification;
- reading/managing motives;
- converting a campaign into a story in which the state appears to be saving humans from demons.

### V2 implication

Norn should remain distinct from Blade and Bullet.

> **Norn's violence is administrative and narrative: she is dangerous because she can make destructive policy look like necessity, rescue, and state reason.**

---

### 4. Norn's private wound is already visible before Ellen

**Locator:** V3 — `p-022.xhtml` ¶53–70

When Keyaru reads Norn's memory, he discovers that:

- her military/political excellence is partly driven by desire to be seen by Flare;
- she lacks Flare's magical/body gifts;
- she develops the skills available to her through extreme effort;
- her hostility toward Flare is entangled with frustrated attachment.

### V2 implication

This material should be recovered into the Ellen/Norn dossier without excusing Norn's actions.

It is one of the clearest cases where:

> **psychological explanation and moral exculpation must remain separate.**

---

# Volume 4
## Nourishment, Keyarga's internal contradiction, Bullet as teacher, divine beasts

Volume 4 turns out to be much more important to the V2 identity thesis than the V1 compression made visible.

---

### 1. The nourishment telos becomes explicit

**Locator:** V4 — 第八話「回復術士はかつての夢を見る」 — `p-009.xhtml` ¶150–169

Keyaru cooks for the group and feels happiness specifically because they enjoy what he made.

This triggers memory of the childhood dream:

- preserve the family orchard;
- produce good food;
- make harsh life more bearable;
- “fight” through nourishment even without combat power.

### V2 implication

Food is not simply domestic filler.

It represents a positive form of efficacy:

> **make something → give it to another person → see the other person become happier → experience efficacy without domination.**

This is structurally opposite to revenge.

---

### 2. The old Keyaru already attacks the Keyarga solution

**Locator:** V4 — 第二十話「回復術士は夢を見る」 — `p-021.xhtml` ¶3–24

The dream stages an internal dialogue:

- old Keyaru: “I did not want to become you.”
- Keyarga: “What else could I have done?”
- old Keyaru: “I only wanted everyone to be happy.”
- Keyarga: “That ‘everyone’ did not include me.”

This is foundational.

### Evidence status

- **TF:** the novel explicitly dramatizes a conflict between prior and current self-conceptions.
- **SI:** Keyarga functions as an answer to self-erasing benevolence and helplessness.
- **Caution:** “trauma armor” remains our analytical synthesis until V9 supplies the literal armor metaphor.

---

### 3. Bullet is explicitly Keyaru's teacher

**Locator:** V4 — `p-021.xhtml` ¶35–62

The novel directly establishes:

- Bullet's intelligence background;
- survival philosophy;
- lie detection;
- enemy/ally classification;
- conditioning/psychological techniques;
- the fact that Bullet teaches Keyaru these methods;
- Keyaru's admission:

> `認めたくはないが、彼は俺の教師だ。`

This is not merely a thematic comparison invented by the synthesis.

### V2 implication

Document 04 should elevate Bullet's role from “worst abuser” to:

> **abuser-teacher whose techniques become part of the architecture Keyarga uses to survive and dominate.**

The relationship is therefore contaminating in a deeper sense: Keyaru defeats Bullet partly by becoming competent in skills Bullet helped transmit.

---

### 4. Bullet's care logic is already substitutional and preservational

**Locator:** V4 — 第二十一話「【砲】の勇者は恋をする」 — `p-022.xhtml`

Bullet's own chapters establish the grotesque logic by which he:

- selects;
- cultivates;
- idealizes;
- freezes/“preserves”;
- substitutes one person for another.

V2 should discuss this clinically, without reconstructing graphic material.

### Ethical relevance

Bullet's later “doll” logic is not a late metaphor imposed by Volume 8. His relation to persons is already organized around:

> **material → cultivation → ideal state → preservation/replacement**

That makes Volume 8's personhood debate structurally earned.

---

### 5. Caladrius links power to life expenditure

**Locator:** V4 — 第十三話 / 第十四話 — `p-013.xhtml`, `p-014.xhtml`; especially `p-014.xhtml` ¶90

Eve explains that full use of Caladrius consumes:

- stamina;
- mana;
- life itself.

### V2 implication

Divine-beast power should not be treated as free supernatural escalation.

The system repeatedly binds extraordinary power to:

- life;
- identity;
- role;
- restriction.

This becomes more important when Guren and Chronos later enter the time function.

---

# Volume 5
## Lapis, Hakuou, the Demon King system, Bullet's strategic theft

### 1. Lapis's body is political leverage

**Locator:** V5 — `p-009.xhtml` ¶110–145

Keyaru heals visible effects of Lapis's condition and recognizes that the illness was deliberately induced through poison disguised as medicine.

He then uses the ongoing treatment requirement as leverage over Carol.

### V2 implication

Lapis is important before Volume 10 because her body already sits at the intersection of:

- family love;
- political coercion;
- medical dependence;
- betrayal;
- strategic leverage.

This makes her later status as both beloved person and system-compelled attacker more than an isolated late twist.

---

### 2. Hakuou exposes the hidden depth of the Demon King office

**Locator:** V5 — `p-020.xhtml` ¶1–12

After defeating Hakuou, Keyaru reads his memory and realizes that:

- ordinary human knowledge of the Demon King is superficial;
- even demon-side knowledge is incomplete;
- the Demon King's power comes from a deeper source;
- the power used elsewhere is connected to the power-granting source behind the office.

### Evidence status

- **TF:** Hakuou had touched hidden information about the source behind Demon King power.
- **SI:** the Demon King office is not merely political kingship plus large statistics; it is embedded in a larger metaphysical architecture.

V2 should avoid teleological wording such as “the office was designed to corrupt” unless a source directly states design intent.

---

### 3. Black power is tied to altered temperament

**Locator:** V5–V6 transition; explicitly restated in V6 `p-016.xhtml` ¶5–10

The source directly says black power is the cause of Demon King madness/aggression.

This is stronger than a merely symbolic “corruption” reading.

### V2 implication

Document 06 should distinguish:

- political office;
- supernatural power source;
- destructive impulse;
- institutional succession.

---

### 4. Bullet wins the Philosopher's Stone through timing and indirect strategy

**Locator:** V5 — `p-020.xhtml` ¶18–87

Bullet:

- waits until Keyaru defeats Hakuou;
- occupies Keyaru with ranged pressure;
- targets Eve to force Keyaru's defensive response;
- has another unit extract the Philosopher's Stone;
- escapes after achieving the real objective.

### V2 implication

This is one of the earliest strong demonstrations that Bullet fights Keyaru on the level of:

> **objective structure rather than duel outcome.**

Keyaru can be stronger in direct confrontation and still lose the operation.

---

# Volume 6
## conceptual healing, true Heroism as metaphysical role, Jioral, reconstruction

### 1. Healing is explicitly “return to the state that ought to be”

**Locator:** V6 — 第十五話「回復術士は真の勇者になる」 — `p-016.xhtml` ¶13–16

This is the central metaphysical sentence of the existing corpus.

`【回復】というのはあるべき姿に戻す力`

### V2 question

Once this is true, every major use of healing asks:

> **Who or what determines the “ought-to-be” state?**

This links:

- body;
- Hero role;
- human form;
- memory;
- time;
- eventually world history.

---

### 2. Heroism is a recoverable concept/role

**Locator:** V6 — `p-016.xhtml` ¶13–41

Keyaru restores the **concept of the Hero** in himself to regain the Hero's original anti-black function.

### V2 implication

The Hero system cannot be reduced to “chosen powerful people.”

A Hero has:

- status;
- role;
- metaphysical function;
- a historically altered relationship to that function.

Document 06 should separately track:

> Hero as social title  
> Hero as power category  
> Hero as metaphysical role  
> Hero as ethical category

These do not always coincide.

---

### 3. Healing can restore Jioral's king toward an earlier human state

**Locator:** V6 — `p-016.xhtml` ¶52–61

Keyaru combines the restored Hero function with healing to return the black-transformed king toward human form.

### V2 implication

Healing has become explicit **regression to an earlier valid state**, which anticipates later personal and world temporal regression.

---

### 4. Prohm/Jioral provides an explicit explanation-without-excuse model

**Locator:** V6 — battle/reflection passages surrounding the king confrontation

Keyaru directly reflects that the king's treatment of his daughters may help explain what Flare and Norn became while refusing to treat that explanation as exculpation.

### V2 implication

This is unusually useful because the novel itself models the analytical distinction V2 needs:

> **causal production of cruelty ≠ removal of culpability**

---

### 5. New Jioral already depends on symbolic heroes

**Locators:**
- V6 — 第六話「回復術士は王を目指す」 — `p-007.xhtml` ¶165–172
- V6 — Epilogue「ジオラル王国再建」 — `p-017.xhtml` ¶19–20

The reconstruction project requires:

- administrative competence;
- a public symbol;
- Keyaru's “Healing Hero” image;
- Freia performing the public continuity of Flare.

### V2 implication

Panakeia does not invent political theater in Volume 9. It develops a technique already central to post-Prohm reconstruction.

---

# Volume 7
## invention, airpower, anti-conquest statecraft, and Bullet as strategic equal/superior

### 1. Keyaru genuinely enjoys creation

**Locator:** V7 — `p-013.xhtml` ¶70–105

The aircraft scene is important for more than technology.

Keyaru:

- calculates;
- designs;
- tests;
- iterates;
- names the machine `飛行機`;
- experiences wonder and practical excitement.

### V2 implication

The builder self is not only “cooking.”

It includes a broader positive competence:

> **making systems and objects that did not previously exist.**

This is a non-revenge source of pleasure and efficacy.

---

### 2. Aircraft changes the military and political problem

**Locator:** V7 — `p-016.xhtml` ¶46–115

Airpower provides:

- safe high-altitude casting;
- range extension;
- precision observation;
- mass destruction;
- strategic surprise.

### V2 caution

The fact that Keyaru enjoys invention does not make the uses of invention benign.

The aircraft immediately becomes an instrument of mass killing and deterrence.

This duality belongs in Documents 02, 05, and 07.

---

### 3. Keyaru explicitly rejects decapitation conquest because it produces endless balancing war

**Locator:** V7 — `p-017.xhtml` ¶66–81

Freia proposes ending the war by simply destroying the enemy ruler/capital.

Keyaru replies that this would make every state believe it might be next and force Jioral into war until it dominates all human states.

He therefore prefers:

- negotiation;
- conference;
- public signaling of peaceful intent;
- military superiority retained in the background.

### Evidence status

This is direct textual evidence that Keyaru's late political logic is already becoming:

> **deterrence + reassurance + controlled diplomacy**

rather than conquest for its own sake.

This is a crucial bridge to Volume 9.

---

### 4. Bullet understands the aircraft threat

**Locator:** V7 — `p-016.xhtml` ¶94–97

Keyaru explicitly says he expects Bullet to imagine an attack mode nobody else should have predicted.

### V2 implication

Keyaru's relationship to Bullet contains a paradox:

> he hates Bullet most and therefore grants Bullet some of his highest assessments of competence.

---

# Volume 8
## irreplaceability, Keyarga as mask, companion agency, Bullet's doll logic

### 1. Volume 8 directly rejects the replaceability of lived history

**Locator:** V8 — 第六話「回復術士は貢ぎものになる」 — `p-007.xhtml` ¶6–32

This is one of the most important passages in the entire series.

Keyaru reasons:

- reset Eve might have the same shape;
- reset Eve would not have the same lived growth;
- he cannot reproduce his present relation by simply “meeting again”;
- the same is true of Freia, Setsuna, Kureha, and Guren;
- he loves **these present histories**.

He concludes:

> `やり直しは利かないな`

### V2 implications

This gives strong textual support for:

> **personhood as accumulated lived history**

and creates the necessary contrast with Volume 10.

The second reset matters only because Volume 8 made reset morally costly.

---

### 2. Keyarga is already called an idealized mask before V9's armor metaphor

**Locator:** V8 — `p-007.xhtml` ¶30–32

Keyaru says:

> because he hated himself, he discarded Keyaru's appearance/name and put on the mask of his ideal self, Keyarga.

### Revised identity progression

V2 can now distinguish:

- **V4:** internal old-self versus Keyarga conflict;
- **V8:** Keyarga as `理想の自分` and `仮面`;
- **V9:** Keyarga explicitly as `鎧`;
- **V10:** practical test — revenge can be relinquished.

This is a much stronger developmental chain than the V1 compressed statement.

---

### 3. Keyaru directly tells Bullet that his companions are not dolls

**Locator:** V8 — 第十二話「回復術士はサインを送る」 — `p-013.xhtml` ¶15

Keyaru's claim is:

- his women think and act without him;
- they are strong;
- he does not want “doll play.”

This should be treated as both:

- evidence of how he increasingly conceptualizes the household;
- a claim requiring ethical stress-testing because several relationships began through extreme coercion.

---

### 4. The final Bullet argument turns reset into a personhood test

**Locator:** V8 — 第二十二話「回復術士は賭けにでる」 — `p-023.xhtml` ¶84–112

Keyaru tells Bullet:

> even if time is rewound, some things cannot be recovered.

His strongest formulation:

> people who have lost the time spent together are not simply interchangeable with same-shaped versions.

Bullet is accused of loving dolls rather than persons.

### V2 significance

This passage is central to:

- Document 03 personhood;
- Document 04 Bullet;
- Document 07 reset ethics;
- Document 10 prospective truth.

---

### 5. Ellen reconstructs Norn because she needs Norn's competence

**Locator:** V8 — 第二十話「軍師の憂鬱」 — `p-021.xhtml` ¶46–50

The text explicitly says Ellen does **not** reconstruct Norn for revenge.

The recovered/reconstructed strategic self lets her make moves Ellen otherwise could not.

### V2 implication

Volume 9's “I choose Ellen” is not simply an amnesiac personality refusing memory.

By Volume 8, Ellen is already deliberately incorporating useful aspects of Norn.

---

# Volume 9
## explicit integration, Ellen's self-choice, cooking, monarchy, religion, forgiveness, Eve's mercy

### 1. Keyarga is explicitly armor

**Locator:** V9 — 第六話「回復術士は王になる」 — `p-007.xhtml` ¶46–65

Canonical line:

> `ケヤルガは俺にとって鎧だった。`

Keyaru explains:

- the old Keyaru was too kind/weak for the revenge he thought necessary;
- he created an ideal merciless self;
- revenge is over;
- the armor is no longer necessary;
- he cannot and does not want to simply become his old self.

### V2 implication

“Trauma armor” is a strong **SI/VJ synthesis** directly grounded in a **TF armor metaphor**.

---

### 2. Ellen knows she was Norn and consciously refuses full restoration

**Locator:** V9 — 第二話「回復術士は妹の秘密を聞く」 — `p-003.xhtml` ¶70–94

This is the strongest personhood evidence for Ellen.

**TF:**

- she knows she was Norn;
- Norn's autobiographical memory did not simply return;
- she reconstructs Norn's strategic personality from traces because Norn is the better strategist;
- Keyaru offers full restoration;
- Ellen refuses;
- she says she prefers her current self;
- she fears a complete restoration would destroy Ellen.

### V2 caution

This does **not** erase origin coercion.

The future argument must remain:

> **later self-ratification is morally significant without making the original rewriting legitimate.**

---

### 3. Cooking becomes an explicit post-revenge positive identity

**Locator:** V9 — 第三話「回復術士は料理を作る」 — `p-004.xhtml` ¶32–44

Keyaru says:

> after peace, he realized he likes cooking.

He imagines:

- a small restaurant;
- not doing it for money;
- ordinary happy days with loved ones.

### V2 implication

The positive endpoint is not reducible to sexual possession or sovereign power.

There is a recurring constructive telos organized around:

> making → feeding → dwelling → ordinary happiness.

---

### 4. The monarchy debate is much more explicit than V1 could preserve

**Locator:** V9 — 第四話「回復術士は選択する」 — `p-005.xhtml` ¶1–57

Kureha argues for a republic because inherited elite status does not make persons morally or intellectually superior.

Ellen argues that:

- democracy/republicanism often produces mediocre governance;
- her own extreme competence makes monarchy preferable in the short term;
- monarchy contains a fatal long-run succession problem.

Keyaru chooses monarchy and explicitly privileges the near-term world he and Ellen can build over centuries he will not live to see.

### V2 implications

This is not merely “Keyaru likes dictatorship.”

The novel puts three distinguishable issues on the table:

1. competence;
2. procedural/general legitimacy;
3. succession/time horizon.

Document 05 should analyze each separately.

---

### 5. Religion is criticized and then appropriated as political technology

**Locators:**
- V9 — 第七話「回復術士は世界宗教に挑む」 — `p-008.xhtml` ¶64–98
- V9 — 第十話「回復術士は帰還する」 — `p-011.xhtml` ¶10–39

Keyaru rejects Faran's:

- human supremacy;
- false deity;
- status hierarchy.

He does **not** reject religion as such.

He explicitly treats religion as useful for:

- social cohesion;
- emotional stability;
- political control;
- public narrative.

He then considers building a religion around a real divine beast/miracle source.

### V2 implication

This is one of the strongest examples of the series' recurring contradiction:

> **Keyaru hates ideological fraud when it is used against him or his protected circle, yet willingly creates managed political fiction when he controls the purpose.**

---

### 6. Falbo produces a real coercion-sensitive culpability distinction

**Locator:** V9 — 第十四話「回復術士は許す」 — `p-015.xhtml` ¶40–115

Falbo admits betrayal but explains that his people were held hostage.

Keyaru initially says:

> crime remains crime.

He then tests whether Falbo truly prioritizes his people over himself.

When Falbo accepts his own death if the tribe will be saved, Keyaru:

- rescues the tribe;
- cancels Falbo's execution;
- warns that the pardon is conditional and exceptional.

### V2 significance

This is real development in Keyaru's culpability taxonomy.

He does **not** conclude:

> coerced betrayal is morally irrelevant.

But he does distinguish:

> malicious betrayal  
> from  
> betrayal committed under hostage coercion for communal survival.

This is much more nuanced than the earlier enemy/ally binary.

### Counterevidence in the same chapter

Immediately after pardoning Falbo, Keyaru's thoughts about the Red Dragons become objectifying and punitive again.

That makes the chapter especially useful:

> **moral-cognitive development occurs without eliminating the old retaliatory/possessive structure.**

---

### 7. Eve explicitly attempts to break retaliatory cycles

**Locator:** V9 — Epilogue「回復術士は悩む」 — `p-019.xhtml` ¶30–60

Keyaru learns that apparent anti-Eve rebellion may have been generated by persecution occurring despite Eve's order not to retaliate against the former regime.

He says:

- Eve is kinder than he is;
- she is trying to stop cycles of hatred;
- he will not allow others to trample that choice.

### V2 implication

Eve is not merely “nice.”

She represents a different sovereign theory:

> **strength may be shown by refusing retaliatory entitlement even when retaliation is emotionally intelligible.**

---

# Volume 10
## culmination: uncertainty, vulnerability, bodily compulsion, higher rules, and another redo

### 1. Ragna's `妾 / warawa` is explicitly performed leadership language

**Locators:**
- V10 — 第十話「回復術士は領主になる」 — `p-011.xhtml` ¶189–194
- V10 — 第十一話「回復術士は竜を抱く」 — `p-012.xhtml` ¶155–158

Ragna explicitly admits that her natural/private self-reference is `私 / watashi`, while `妾 / warawa` is maintained because it sounds more authoritative/chief-like.

### Evidence status

- **TF:** the register split is self-conscious role performance.
- **VJ:** “performed sovereignty” is an appropriate analytical label.

This belongs in Documents 03 and 08.

---

### 2. Ragna's relationship changes after a coercively structured political origin

**Early locator:** V10 — 第三話「回復術士は約束する」 — `p-004.xhtml`

Ragna initially accepts marriage in a context where:

- Keyaru possesses overwhelming coercive capacity;
- her people need security;
- she explicitly frames herself as a possible sacrifice for the tribe.

**Later locator:** V10 — 第十話「回復術士は領主になる」 — `p-011.xhtml` ¶150–198

Later she:

- discloses private fear;
- admits weakness she has never shown Hiseki;
- shifts from `妾` to `私`;
- says she wants intimacy for herself rather than as tribal payment.

### V2 conclusion

The relationship should be described as:

> **moving toward genuine reciprocal personal choice after a politically coercive founding structure**

not:

> “always consensual”

and not:

> “later affection is therefore fake.”

---

### 3. Keyaru admits fear and loneliness

**Locator:** V10 — `p-011.xhtml` ¶161–172

Keyaru says that:

- his decisions have killed thousands;
- moving forward frightens him;
- he feels obligated to hide regret and fear from people who follow him;
- he realizes aloud that he has been lonely;
- even his lovers have not known the truth of the redo.

### V2 implication

This is unusually direct evidence that late Keyaru's psychological opacity decreases.

It does not prove moral redemption.

It does show:

> **a narrowing gap between felt emotion and named emotion.**

---

### 4. Keyaru relinquishes the necessity of personally killing Bullet

**Locator:** V10 — 第八話「回復術士は招き入れる」 — `p-009.xhtml` ¶20–36

Keyaru says:

- old Keyarga would prioritize the revenge plan even over the world;
- present Keyaru prioritizes his happy life;
- he no longer needs to be the one who kills Bullet;
- his earlier public claim that he had “killed Keyarga” was initially aspiration, but his root has now actually changed.

### V2 significance

This is one of the strongest behavioral tests of the Volume 9 armor thesis.

---

### 5. Chronos confirms a higher rule architecture but does not identify literal “players”

**Locator:** V10 — 第七話「回復術士は開き直る」 — `p-008.xhtml` ¶80–122

Chronos says:

- divine beasts are pieces prepared to maintain the world;
- destructive/opposing pieces also exist;
- there is a game/board structure;
- pieces have permitted and forbidden forms of intervention;
- he incurs punishment for revealing forbidden information;
- Hero killing by a Hero violates a balancing rule;
- Keyaru should kill no more Heroes;
- the first “mistake” must be made not to have happened.

### Epistemic status

**TF:**

- higher rule architecture;
- world-maintaining “pieces”;
- opposing/destructive pieces;
- intervention restrictions;
- punishment for divine-beast rule violation;
- Chronos's Hero-killing warning.

**SI:**

- there are agents/interests not reducible to ordinary in-world political actors.

**SP:**

- literal human-like “players”;
- metafictional readers/authors;
- simulation operators;
- the exact ontology of the external level.

V2 must preserve this boundary rigorously.

---

### 6. Chronos's initial explanation is challenged by historical counterevidence

**Locator:** V10 — 第十四話「回復術士は追い詰められる」 — `p-015.xhtml` ¶131

Ellen finds many historical cases of Heroes killing Heroes without the same catastrophe.

Therefore:

- the simple rule “Hero kills Hero → world balance collapses” is inadequate;
- Keyaru's case is special for an unresolved reason.

This is one of the strongest reasons not to overstate the mechanics.

---

### 7. The seven-to-seven relationship remains hypothesis, not rule

**Locator:** V10 — 第二十話「回復術士は……」 — `p-021.xhtml` ¶46–54

The text establishes:

- Keyaru killed seven Heroes;
- seven anomalous Demon King candidates possess Hero marks;
- the counts match.

Keyaru says this may not be coincidence.

### Epistemic status

- **TF:** count correlation.
- **SI:** Keyaru's Hero kills are causally relevant.
- **SP:** exact replacement mechanism and why replacements appear specifically among Demon King candidates.

Do not convert Keyaru's provisional reasoning into narrator-confirmed law.

---

### 8. The orchard becomes a full autobiographical causal model

**Locator:** V10 — 第十三話「回復術士は愛人を救う」 — `p-014.xhtml` ¶95–140

Volume 10 supplies the most complete chain:

- family apple orchard;
- joy in others eating what he made;
- apple pies for village celebrations;
- parents killed by monsters;
- Hero dream born from grief;
- Jioral objectification;
- revenge;
- question of whether present self is wanted self;
- possibility of future orchard without abandoning current loved relationships.

Important line:

> `勇者になる前の俺の残骸。`

The retained apple-pie memory is described as a remnant of the pre-Hero self.

### V2 implication

The orchard is not an argument that Keyaru should revert to childhood.

It is a **positive telos that survives transformation**.

The late synthesis should emphasize integration:

> current competence + recovered capacity to nourish/build.

---

### 9. Ellen's `損切り / songiri` framing is self-sacrificial strategic clarity

**Locator:** V10 — 第十四話「回復術士は追い詰められる」 — `p-015.xhtml` ¶153–155

Ellen says:

- she does not want to lose their life together;
- she will struggle as hard as possible;
- but there is a point beyond which refusing reset becomes catastrophic failure to cut losses.

### V2 implication

This is not evidence Ellen values the present less.

It is evidence that her strategic identity persists even when **her own history** is one of the assets at risk.

---

### 10. Lapis proves action and agency can separate

**Locators:**
- V10 — 第十八話「回復術士は恋人に手を伸ばす」 — `p-019.xhtml` ¶125–142
- V10 — 第十九話「回復術士は敗走する」 — `p-020.xhtml` ¶19–31

Lapis:

- remembers Keyaru and Eve;
- says she loves and wants to protect them;
- asks to be killed rather than harm them;
- physically tries to restrain herself;
- is nevertheless compelled to attack;
- deliberately makes her attacks more avoidable when she can.

### Evidence status

This is the corpus's clearest **TF separation of moral agency and bodily behavior**.

V2 ethics should use it as the mature endpoint of a line already visible in coercion cases like Falbo:

> **what a body does is not sufficient evidence of what the person chooses.**

---

### 11. Ragna's compelled violence receives the same treatment

**Locator:** V10 — `p-020.xhtml` ¶40–48

Ragna can speak as wife/lover while simultaneously saying she “must” kill Hero and Demon King.

The novel treats this as the same compulsion structure as Lapis.

### V2 implication

Her attack cannot be used as evidence that later love was false.

---

### 12. Hiseki's death remains high-confidence but indirect

**Locator:** V10 — `p-020.xhtml` ¶40–44

Keyaru sees Ragna arrive after fighting Hiseki and concludes:

> `ヒセキは死んだのか。`

### Evidence status

- **SI / very high confidence:** Hiseki has been killed or defeated fatally.
- **Caution:** this is Keyaru's conclusion from circumstances; the source does not provide a separate corpse-verification scene before reset.

V2 should preserve the slight qualification.

---

### 13. Keyaru rejects “reset now” even after the system tries to force the choice

**Locator:** V10 — `p-020.xhtml` ¶51–80

Even after recognizing that he alone could escape and reset, Keyaru refuses to abandon:

- Eve;
- the companions;
- Lapis;
- Ragna.

He explicitly says his anger is **not** toward Lapis/Ragna/candidates but toward the world/rule structure imposing the situation.

### V2 significance

This is very strong evidence that the Volume 8 position persists into Volume 10.

The eventual reset is not:

> “Keyaru changed his mind because reset is convenient.”

It happens only after the current timeline becomes effectively unsalvageable.

---

### 14. Ellen's “outside the world” model is explicitly presented as hypothesis

**Locator:** V10 — `p-021.xhtml` ¶87–105

Ellen's message reasons:

- ordinary events have motive → preparation → action → result;
- the candidate crisis seems to contain only the result;
- perhaps the unseen causal work exists “outside” the world;
- perhaps Keyaru's Hero-killing allows that interference.

But both narrator and Keyaru explicitly mark the chain as hypothesis.

### Evidence status

- **TF:** Ellen makes the hypothesis.
- **TF:** Keyaru knows it is hypothetical.
- **SP/SI:** the exact external-causality model.

This is the correct V2 boundary.

---

### 15. Bullet's final act preserves his core autonomy pathology

**Locator:** V10 — Epilogue「回復術士のやり直し」 — `p-022.xhtml` ¶23–53

Bullet:

- threatens Eve;
- imposes a forced binary choice;
- makes “disable me” insufficient;
- requires Keyaru to kill him;
- deliberately triggers the forbidden Hero kill;
- says he did it out of love because Keyaru's chosen plan was “worst” and “destructive.”

Keyaru later interprets the outcome as having saved him.

### Ethical conclusion

This is the perfect case for separating:

> **beneficial consequence**

from

> **legitimate method.**

Bullet's method remains:

> **I know what you need better than you do; therefore I may override your authorship.**

That is not a late redemption reversal. It is continuity.

---

### 16. Ellen's death is reported/accepted, not corpse-verified

**Locator:** V10 — Epilogue — `p-022.xhtml` ¶1–22

The chapter begins:

> `エレンの死を聞いた。`

Bullet says he left her in a collapsing situation rather than personally killing her.

Keyaru:

- briefly considers survival;
- accepts Bullet's assessment;
- reasons Ellen would not have misread the battlefield;
- understands that she knowingly sent Bullet away because otherwise Keyaru would die.

### Correct V2 status

> **reported death / overwhelmingly implied death**

not:

> **directly corpse-verified death.**

---

### 17. The second redo is consultative/partially co-authored, not equal collective control

**Locator:** V10 — Epilogue — `p-022.xhtml` ¶78–113

Keyaru:

1. chooses to redo;
2. tells Freia, Setsuna, and Kureha the truth;
3. asks what they would want changed.

Their answers matter.

#### Setsuna
She asks that her people be saved **before** enslavement, even though enslavement is what led to meeting Keyaru.

#### Freia
She asks Keyaru to become Flare's friend because she dimly remembers Flare as lonely and suffering.

#### Kureha
She asks for a normal beginning: thank him properly, become friends, train together before Keyarga exists.

### Correct V2 formulation

This is not full equality of authorship.

Keyaru still:

- possesses the decisive information;
- makes the reset decision;
- has exceptional operational authority;
- depends on Guren's time function.

But he has ended **exclusive historical authorship**.

Better phrases:

- **partial collaborative authorship**
- **shared claims over historical revision**
- **consultative co-authorship**
- **the end of Keyaru's sole authorship**

---

### 18. Eve explicitly wants to save the Black Wings herself

**Locator:** V10 — Epilogue — `p-022.xhtml` ¶149–160

Eve imagines retaining memory and using the next timeline to save her own people before Keyaru must do it.

### V2 significance

The second redo is not merely:

> Keyaru promises to rescue everyone more efficiently.

Other people now formulate:

> **what they themselves want to do differently.**

That is a major ethical difference from the first redo.

---

### 19. Memory retention is probabilistic

**Locator:** V10 — Epilogue — `p-022.xhtml` ¶70–87, ¶179–186

Guren says:

- connected people may retain memory;
- probability is uncertain and below certainty;
- Guren herself will definitely not forget;
- timing matters, especially while Eve remains alive.

### Correct V2 status

Do not state:

> “the whole household carries memory into the new timeline.”

Only Guren's retention is treated as certain before the volume ends.

---

### 20. The exact reset landing point is not shown

**Locator:** V10 — Epilogue — `p-022.xhtml` ¶191–205

Keyaru conceptualizes:

> `回帰の【回復】`  
> target: `世界`

and the world rewinds.

The volume ends at:

> `さて、始めようか回復術士のやり直しを。`

No post-reset scene establishes the exact landing date.

### Correct V2 status

**SP:** any exact landing point.

---

# VI. Cross-volume evidence packets for the main V2 theses

# A. Keyarga as trauma architecture

The primary-source chain is now substantially stronger.

## Stage 1 — pre-Keyarga productive self
- V1 `p-002.xhtml`: apple farmer.
- V4 `p-009.xhtml`: explicit dream of making people happy through apples/sweets.

## Stage 2 — objectification
- V1 `p-014.xhtml`: personality stripped, drug dependency, tool status.

## Stage 3 — defensive inversion
- V4 `p-021.xhtml`: “what else could I have done?”; helpless benevolence excludes Keyaru's own survival/happiness.

## Stage 4 — idealized mask
- V8 `p-007.xhtml` ¶31: `理想の自分であるケヤルガの仮面`.

## Stage 5 — armor named
- V9 `p-007.xhtml` ¶46–65: `ケヤルガは俺にとって鎧だった`.

## Stage 6 — behavioral integration
- V10 `p-009.xhtml`: revenge no longer outranks current happiness.
- V10 `p-011.xhtml`: fear and loneliness become speakable.
- V10 `p-014.xhtml`: asks whether current self is wanted self but chooses integration rather than regression.
- V10 `p-022.xhtml`: reveals the redo and asks others what they want changed.

### V2 thesis status

> **Keyarga-as-trauma-armor is now strongly supported SI/VJ grounded in multiple TF stages.**

The argument should not be reduced to a diagnosis of multiple personality/dissociation.

---

# B. Personhood as accumulated history

## Freia
- V1: autobiographical memory erased, knowledge retained.
- later volumes: new accumulated history.
- V10: present Freia can think about pre-rewrite Flare as someone whose suffering mattered.

## Ellen
- V8: reconstructs Norn's competence.
- V9: knows she was Norn, refuses full restoration, chooses Ellen.

## Eve / reset
- V8: same-shaped reset Eve would not be the present person Keyaru loves.

## Lapis/Ragna
- V10: subjective continuity remains while motor/action output is hijacked.

### V2 thesis status

The series repeatedly rejects body-only identity.

A more precise model is:

> **personhood is distributed across body, memory, skill, accumulated relationships, choices, and lived history; none alone is sufficient in every case.**

---

# C. Moral development versus expanded possessive circle

Phase 2 strengthens **both** sides.

## Evidence for real development

- V8: refuses a strategically superior reset because present histories matter.
- V9: distinguishes hostage-coerced betrayal from ordinary betrayal.
- V9: recognizes Eve's anti-retaliatory mercy as morally significant.
- V10: relinquishes personal necessity of killing Bullet.
- V10: does not blame Ragna/Lapis for compelled actions.
- V10: refuses to abandon them even when reset is available.
- V10: asks companions what they want changed.

## Evidence against universal moral transformation

- V9 Falbo chapter immediately returns to punitive/objectifying fantasies about enemies.
- V10 `p-021.xhtml` ¶101: Keyaru still says he primarily cares about his own important people rather than everyone equally.
- Panakeia remains highly personalist.
- consent is not established as a universal limiting principle.

### V2 likely conclusion

> **Keyaru develops real recognition of agency, coercion, and irreplaceability without becoming a universalist moral subject. His protected circle becomes both larger and more internally person-sensitive. The “expanded possessive circle” counterreading remains partly true rather than being simply refuted.**

---

# D. Politics: household → deterrence → state

Primary-source chain:

- V3 Branica: coexistence is materially possible.
- V6 New Jioral: legitimacy requires public Hero/Flare symbols.
- V7 airpower: overwhelming force changes diplomacy.
- V7: Keyaru rejects total conquest because it creates endless balancing war.
- V9: monarchy debate openly acknowledges short-term competence versus long-run succession failure.
- V9: religion treated as social technology.
- V9: Eve pursues anti-retaliatory governance.
- V10: Red Dragon settlement expands incorporation.

### V2 stress test

Panakeia can plausibly be described as:

> **authoritarian peacebuilding organized around a widened protected household**

but V2 must ask:

> does institutional logic actually become impersonal, or is superior personal rule merely scaled upward?

The primary sources do not justify resolving that question by fiat.

---

# E. Healing progression

The source-supported ladder is now:

1. physical restoration;
2. pain/memory/experience access;
3. skill acquisition/copying through healing;
4. bodily alteration;
5. memory/identity alteration;
6. degradation / deliberately wrong restoration;
7. **explicit `概念の【回復】`**;
8. human-state regression;
9. personal temporal regression;
10. world-scale `回帰の【回復】`.

The repeated governing question becomes:

> **what counts as the state something ought to return to?**

This is not only an analytical metaphor. It arises from Keyaru's own definition of healing.

---

# F. Bullet: predator, teacher, and autonomy-negating “lover”

Primary-source chain:

- V4: former intelligence ace; survival/conditioning skills taught to Keyaru; Keyaru calls him teacher.
- V4: person-substitution/preservation logic already visible.
- V5: objective-oriented theft of Philosopher's Stone.
- V7: predicts/adapts to Keyaru's innovations.
- V8: wants reset and treats persons as reproducible dolls.
- V10: rejects Keyaru's choice, forces a Hero kill, calls override “love.”

### V2 thesis status

The strongest formulation survives source re-entry:

> **Bullet understands persons with extraordinary acuity while refusing their jurisdiction over themselves.**

He is therefore not merely “Keyaru but worse.”

He is a dark teacher whose pathology is **accurate understanding without recognition of autonomy**.

---

# VII. Claims downgraded or preserved as unresolved

## 1. Ellen's death
**Status:** very high-confidence reported/implied, not direct physical verification.

## 2. Hiseki's death
**Status:** very high-confidence inference from Ragna's return and Keyaru's conclusion, not independent corpse verification.

## 3. seven Hero kills → seven candidates
**Status:** strong correlation and likely causal relevance; exact mechanism unresolved.

## 4. literal external “players”
**Status:** unsupported as fact. Higher rule architecture is textual; ontology of external level unresolved.

## 5. exact second-reset date
**Status:** unknown.

## 6. household memory after reset
**Status:** uncertain/probabilistic except Guren.

## 7. full collaborative authorship
**Status:** overstatement. The stronger claim is the end of Keyaru's exclusive authorship and recognition of companions' claims over revision.

## 8. Panakeia as legitimate
**Status:** normative/political evaluation, not textual fact.

## 9. Freia as wholly new person
**Status:** philosophical conclusion requiring dimensional continuity analysis.

## 10. Ellen as wholly self-authored
**Status:** too strong. Later ratification is significant, but the subject performing ratification was produced through coercive reconstruction.

---

# VIII. Source-return priorities for the next Phase-2 tranche

This first tranche has verified the **core longitudinal claims**. Before Phase 3 specialist rewriting, a second source-reentry tranche should backfill narrower document-specific evidence in the following areas.

## Document 03 backfill
- exact transition at which Norn receives the name Ellen;
- additional Freia independent-choice scenes outside Keyaru's direct interpretation;
- Setsuna's later tribe/identity developments after Volume 1;
- Kureha's Sword Hero development;
- Guren's agency restrictions before Chronos;
- Ragna/Hiseki relational history;
- Lapis's post-Volume-5 political/relational trajectory.

## Document 04 backfill
- Blade's pattern as opportunistic appetite;
- Prohm as paternal/state instrumentalization;
- Hakuou's own subjective relation to black power;
- Hiseki's public/private split and political competence;
- Faran/Holy Emperor as sacred-order antagonist.

## Document 05 backfill
- precise New Jioral → Panakeia legal discontinuity language;
- world-conference liability logic in full;
- airpower proliferation/Casta;
- Eve's administrative/factional problems;
- Volume-10 low-tax/infrastructure settlement detail.

## Document 06 backfill
- exact Hero succession wording before Volume 10;
- Divine Armament mechanics;
- Guren's purification and replacement-role constraints;
- Demon King heart/Philosopher's Stone relation;
- black-knight system;
- personal temporal regression mechanics from the first redo.

## Document 08 backfill
- representative Japanese passages for Keyaru's cognitive prose rhythm;
- pronoun/register changes under disguise;
- a compact corpus of `俺`, possession vocabulary, classification language;
- `やり直し`, `鎧`, `仮面`, `あるべき姿`, `回帰`, `損切り`, `破壊衝動`.

These are **micro-backfills**, not reasons to reopen the V2 master theses.

---

# IX. Phase-2 provisional synthesis

Primary-source re-entry substantially strengthens the planned V2 while correcting several simplifications.

The most important changes are:

### 1. Keyarga's identity architecture is visible much earlier than Volume 9
Volume 4 already stages the old Keyaru accusing Keyarga of becoming a monster and Keyarga defending himself as the only way to include **his own** survival and happiness.

### 2. Nourishment is not a late sentimental add-on
It exists from Volume 1 as livelihood and by Volume 4 as an explicit alternative mode of “fighting” through making people happy.

### 3. Volume 8 is the philosophical hinge of the reset problem
It directly says present people cannot be reproduced by replaying history with same-shaped bodies.

### 4. Volume 9 provides explicit integration language
`仮面` in Volume 8 becomes `鎧` in Volume 9, and the post-revenge Keyaru chooses neither simple regression nor continued full-time Keyarga.

### 5. Volume 10 tests rather than merely announces integration
He can:
- give up personal revenge priority;
- name fear and loneliness;
- distinguish compelled action from agency;
- refuse to abandon people whose bodies are attacking him;
- disclose his hidden history;
- ask others what they want changed.

### 6. The moral-development counterreading survives
The text still gives abundant evidence of possessiveness, particularism, and punitive permission. V2 should therefore describe development as **real but incomplete** rather than redemption.

### 7. The world-system must remain epistemically layered
Chronos proves a higher rules layer. Ellen's “outside the world” model remains a hypothesis. The seven-to-seven pattern remains an inference. Literal player ontology remains unresolved.

### 8. The second redo is ethically different without becoming democratically equal
The critical transition is not that Keyaru relinquishes all control.

It is:

> **other people finally acquire acknowledged claims over what history should become.**

That is enough to transform the meaning of the redo without sentimentalizing it.

---

# X. Phase-2 tranche completion checklist

- [x] Freeze exact source identity through SHA-256.
- [x] Establish reproducible chapter/XHTML/paragraph locator convention.
- [x] Confirm Volume-10 unrelated-sample boundary.
- [x] Re-enter first-timeline objectification.
- [x] Re-enter Flare → Freia memory/knowledge mechanics.
- [x] Re-enter Setsuna's coercive origin and later independent choice.
- [x] Re-enter Kureha's justice problem.
- [x] Re-enter Branica as concrete coexistence evidence.
- [x] Re-enter Norn's institutional violence and private wound.
- [x] Re-enter Volume-4 nourishment and Keyaru/Keyarga dream conflict.
- [x] Re-enter Bullet's explicit teacher status.
- [x] Re-enter Lapis's poisoned-body political function.
- [x] Re-enter Hakuou/Demon King deeper-system evidence.
- [x] Confirm textual `概念の【回復】`.
- [x] Re-enter New Jioral symbolic-legitimacy mechanics.
- [x] Re-enter aircraft, bombing, deterrence, and anti-conquest reasoning.
- [x] Re-enter Volume-8 reset refusal and personhood argument.
- [x] Re-enter Ellen's deliberate Norn reconstruction.
- [x] Re-enter Volume-9 `鎧` passage.
- [x] Re-enter Ellen's explicit self-choice.
- [x] Re-enter cooking/restaurant positive telos.
- [x] Re-enter monarchy versus republic debate.
- [x] Re-enter religion-as-state-technology material.
- [x] Re-enter Falbo coercion-sensitive pardon.
- [x] Re-enter Eve anti-retaliation material.
- [x] Re-enter Ragna `妾 / 私` role split.
- [x] Re-enter Keyaru/Ragna vulnerability exchange.
- [x] Re-enter Keyaru's relinquishment of personal Bullet revenge.
- [x] Re-enter Chronos and rule-restriction evidence.
- [x] Re-enter Volume-10 orchard/identity passage.
- [x] Re-enter Ellen `損切り`.
- [x] Re-enter Lapis/Ragna agency-versus-action compulsion.
- [x] Re-enter seven-Hero/seven-candidate correlation.
- [x] Re-enter Ellen outside-causality hypothesis with correct uncertainty.
- [x] Re-enter Bullet's final autonomy override.
- [x] Re-enter Ellen death status.
- [x] Re-enter second-redo wishes.
- [x] Re-enter Eve's self-authored next-timeline wish.
- [x] Re-enter memory-retention uncertainty.
- [x] Re-enter final world-scale `回帰の【回復】`.
- [x] Record narrower micro-backfill queue for remaining Phase-2 work.
- [x] Do **not** begin Phase-3 specialist prose rewriting yet.

---

# XI. Handoff

The evidence now supports the main V2 expansion more strongly than V1 alone did.

The next work inside **Phase 2** is the narrower document-specific backfill listed in Section VIII. Once those anchors are collected, Phase 3 can begin in the prescribed specialist order:

1. `02_KEYARU_KEYARGA_CHARACTER_DEEP_DIVE.md`
2. `03_PERSONHOOD_HOUSEHOLD_AND_RELATIONSHIPS.md`
3. `04_BULLET_ANTAGONISTS_AND_DARK_MIRRORS.md`
4. `05_POLITICS_INSTITUTIONS_AND_STATECRAFT.md`
5. `06_HEALING_POWER_METAPHYSICS_AND_WORLD_SYSTEM.md`
6. `07_ETHICS_REVENGE_AUTONOMY_AND_LOVE.md`
7. `08_NARRATION_LANGUAGE_GENRE_AND_MOTIFS.md`

The governing rule remains:

> **Do not write V2 from the V1 conclusion. Write V2 from the Japanese evidence path that makes the conclusion survive.**
