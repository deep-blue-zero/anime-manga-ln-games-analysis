---
title: "〈物語〉シリーズ V2 V07 Deep Reading — 猫物語（黒）"
series: "〈物語〉シリーズ"
project: "Monogatari V2 second-pass deep reading"
artifact_id: "MONOGATARI_V2_V07_DEEP_READING"
version: "1.0"
date: "2026-08-14"
status: "Phase 1 canonical volume artifact"
volume_code: "V07"
japanese_title: "猫物語（黒）"
archive_position: "First Season archive spine V07"
source_file: "07 猫物語 黒.epub"
source_drive_id: "1lVr4ZUqUOxoDYyVmm2tmVZWWHz7eRN0K"
source_sha256: "216d79503299e41b5605444ed95b710d98c3151a89e9e4eca3f8563088d8a708"
source_language: "ja"
source_author: "西尾維新"
source_provenance_status: "Original Kodansha BOX first-print colophon preserved; later calibre wrapper present; no authenticated electronic-edition date located"
principal_story_unit: "第禁話 つばさファミリー"
narrators:
  - "阿良々木暦"
internal_story_range: "April 29-May 8, Golden Week, shortly after Kizumonogatari and before Bakemonogatari"
spoiler_policy: "Publication-local reading is separated from retrospective V2 interpretation; later-series knowledge is quarantined to retrospective sections."
method_version: "MONOGATARI_V2_ANALYTICAL_METHOD.md"
---

# 〈物語〉シリーズ V2 — Volume 07 Deep Reading
## 『猫物語（黒）』
### 第禁話「つばさファミリー」

> **Publication-local core:** 『猫物語（黒）』 is not a story in which Hanekawa's hidden evil self is exposed and exorcised. It is a story in which a girl who has made ethical correctness into a survival discipline encounters an oddity that can turn displaced stress into a usable body. The ordinary `障り猫` possession apparently ends after the first attack on her parents; according to Oshino's reconstruction, Hanekawa then refuses to let the cat go, pulls it back into herself, and creates a new hybrid—Black Hanekawa. The resulting violence is hers without being reducible to a single “true self.” Acute supernatural resolution can stop the violence, but the novel explicitly refuses to call that resolution of the underlying problem: `物語は完結するけれど、問題は解決しない`.
>
> **Retrospective V2 core:** V07 strongly confirms the V1 model of Hanekawa as over-adapted rather than merely “good,” but it also forces several corrections. Black Hanekawa is indeed an emergency stress-disposal system, yet “disposal” is not cure: it harms unrelated people, does not alter the family structure, can become self-reinforcing, and eventually threatens to erase Hanekawa. Araragi's idealization is not a neutral admiration but part of the problem; he repeatedly mistakes Hanekawa's ability to enact correctness for evidence that she cannot suffer. Most importantly, the volume's supposed “dark side” revelation does not establish that Black Hanekawa is more authentic than ordinary Hanekawa. V07 instead extends the rule already learned from Kanbaru, Kiss-shot, and Tsukihi: **a newly disclosed, darker, more transgressive layer can be real without becoming the whole truth of a person.**

---

# 1. Source audit

## 1.1 Governing supplied source

This reading is grounded in the supplied Japanese EPUB `07 猫物語 黒.epub`, fetched from the locked Google Drive corpus and materialized locally for close inspection.

- Drive ID: `1lVr4ZUqUOxoDYyVmm2tmVZWWHz7eRN0K`
- MIME: `application/epub+zip`
- Size: 326,463 bytes
- SHA-256: `216d79503299e41b5605444ed95b710d98c3151a89e9e4eca3f8563088d8a708`
- Internal title: `猫物語 黒`
- Creator: 西尾維新
- Language: ja
- Principal story unit: 第禁話「つばさファミリー」
- Numbered story sections: 001–013
- Included paratext: afterword and author/illustrator/first-print colophon

The end matter preserves a Kodansha BOX colophon stating:

- 『猫物語（黒）』
- first printing: **2010-07-28**
- author: 西尾維新
- publisher: 株式会社講談社
- illustrator: VOFAN

The afterword independently identifies this book as the **sixth book of the series**. This is historically important because the V2 Drive archive calls this file V07: the discrepancy is another demonstration that the Drive spine is an archival segmentation, not a publication-count identity. The original publication sequence counts 『化物語』 as two books, whereas the supplied Drive reconstruction distributes it across three archive files.

## 1.2 Digital-file provenance qualification

Unlike V06, this EPUB does not contain an authenticated-looking explicit electronic-edition date notice. The OPF includes:

- `dc:date` = `2015-09-24T14:00:00+00:00`
- calibre 7.23.0 contributor metadata
- calibre timestamp `2022-07-17T13:24:17.225789+00:00`
- MOBI-ASIN-like identifier `G6OU5AKCTYCLLQTBT3EW5VPNBNQMM6JY`

None of those fields is promoted to an official publication or digitization date. V07 therefore receives a split provenance classification:

- **high confidence** in the original 2010 Kodansha BOX first-print identity preserved in the colophon;
- **high analytical confidence** in the supplied Japanese narrative as the project's governing primary text;
- **moderate confidence** in the later digital packaging lineage;
- **no asserted official electronic-edition date** from the supplied file.

## 1.3 Extraction and locator layer

For close reading, the raw EPUB was expanded locally and converted into a paragraph-addressed audit text.

- derivative file: `monogatari_v07_source_text.txt`
- paragraph-addressed lines: 5,613
- visible text size: approximately 693 KB
- story locator format: `[part0002_split_XXX:YYYY]`

The derivative is a search and QA layer only. The EPUB remains governing evidence.

## 1.4 Source-specific evidentiary risks

V07 is unusually dangerous for overconfident interpretation because the book contains several competing explanations of “Hanekawa”:

1. **Araragi's admiration** repeatedly places her beyond ordinary humanity.
2. **Hanekawa's own statements** rationalize mistreatment and minimize need.
3. **Black Hanekawa's testimony** has shared access to Hanekawa's knowledge but explicitly lacks full access to how Hanekawa felt about every event.
4. **Oshino's reconstruction** combines specialist expertise, altered-state questioning, inference, and professional compromise.
5. **The standard sawarineko folktale** is itself a didactic model about “hidden sides,” not a guaranteed one-to-one description of this case.
6. **The afterword** reflects Nisio's authorial/parataxtual interest in unresolved problems but is not diegetic doctrine.

Accordingly, statements such as “Hanekawa feels nothing,” “Black Hanekawa is her true self,” “the cat simply possessed her,” or “the family caused everything” must be routed through speaker, confidence, and counterevidence.

---

# 2. Publication-local thesis

『猫物語（黒）』 is about a person whose survival strategy is so effective that other people misread the strategy as nature.

Hanekawa has learned to enact correctness with extraordinary consistency. She follows rules, performs fairness, studies, mediates, helps, and minimizes her own inconvenience to others. Araragi initially sees this as almost supernatural goodness. He says ordinary language is inadequate to describe her; language fit for gods or demons might be necessary. The compliment is also a warning. He is already narrating her outside the category of ordinary human weakness.

The Golden Week crisis begins not because Hanekawa suddenly becomes different but because the system sustaining that difference fails. The family structure in which she lives has no ordinary place for her. She says flatly that she has no family even though she has parents and a house. She has spent years trying to behave `娘らしく` toward adults who do not function as parents toward her. After her father hits her, she searches for a causal story in which her attempt to approach them disturbed a previously stable equilibrium. By the most disturbing point in the disclosure, she reaches the conclusion:

> `私は私だから──殴られても仕方がないんだ`

The sentence is not a metaphysical truth; it is a portrait of internalized blame. The problem is no longer simply “my father lost his temper.” Hanekawa has made her own personhood available as the explanation for why violence against her might be deserved.

The sawarineko gives that impossible arrangement a different output channel. Yet V07 refuses the simplest possession story. The ordinary possession apparently accomplishes its first proximate wish when the parents are drained. Hanekawa's own consciousness then returns. According to Oshino's post-crisis reconstruction, she could have let the oddity separate—but instead pulls it back, incorporates it, and thereby participates in the birth of a new entity, Black Hanekawa.

That makes the moral structure deliberately uncomfortable.

Hanekawa is harmed.

Hanekawa is not therefore without agency.

The cat is an external oddity.

The resulting Black Hanekawa is not therefore purely external.

The subsequent attacks on unrelated townspeople are understandable as stress discharge.

They are not therefore harmless or justified.

Araragi eventually defeats the acute supernatural configuration, but he knows while doing so that he is only resetting the board. The family remains. The violence remains in history. Hanekawa's mode of self-management remains. The novel's own formulation is more exact than any interpretive paraphrase:

> `物語は完結するけれど、問題は解決しない。`

V07's publication-local achievement is to make **non-resolution itself** the honest ending.

---

# 3. Retrospective V2 thesis

Through V07, the V2 corpus can now distinguish at least four different errors that previous readings might make about Hanekawa.

## Error 1: “Hanekawa is simply an angelic good girl.”

This is Araragi's initial pedestalization. Her goodness is real, but it is also disciplined, rule-governed, and partly defensive. Treating the performance as effortless nature prevents observers from noticing the cost.

## Error 2: “Therefore her goodness is fake.”

The source does not support that reversal. Hanekawa actually performs the ethical actions. She studies, helps, mediates, buries the cat, and tries not to impose on others. Construction does not make the behavior unreal. V05 has already taught us not to use origin/construction as a shortcut to worth.

## Error 3: “Black Hanekawa is the true Hanekawa.”

V07 repeatedly uses language such as `暗黒面`, `裏面`, and `猫をかぶる`, but the case mechanics undermine a simple “mask off = truth” reading. Black Hanekawa is a new hybrid produced by oddity mechanics, Hanekawa's retained knowledge, displaced stress, and Hanekawa's own decision/impulse to re-incorporate the cat. It is a real part of her causal and moral life without being an unmediated essence.

## Error 4: “If the oddity is removed, Hanekawa is cured.”

The book explicitly rejects this. The supernatural event can end while the life condition remains. Indeed, memory loss and ritualized explanation may make continuation possible by covering the wound rather than transforming it.

The stronger retrospective thesis is therefore:

> **Hanekawa's problem is not hidden evil but over-separation: ethical action from feeling, help-giving from help-receiving, household presence from belonging, stress from conscious ownership, and idealized public role from disallowed ordinary need. Black Hanekawa does not reveal the one true self; it materializes the cost of keeping those domains apart.**

『猫物語（白）』 will later be allowed to revise this model, but V07 already contains the architecture that makes such a revision possible.

---

# 4. Narrative architecture and arc map

The book can be divided into seven functional movements.

## A. Retrospective frame: the narrator warns against his own account

Before reconstructing Golden Week, Araragi says exhaustive narration cannot communicate the full truth. He calls the account a kind of reflection/apology and admits that now, near the beginning of the second semester, he sees things he failed to understand then.

This means the novel is not giving us an untouched April/May consciousness. It is a later Araragi staging an earlier Araragi while already carrying regret.

## B. Comic/sexual prelude: is attraction love?

The extremely long Tsukihi conversation about underwear, desire, and romantic recognition seems at first to be pure digression. Structurally it establishes Araragi's inability to name ordinary attraction. He wants a rational threshold at which affection becomes romance. Tsukihi keeps refusing the demand for an algorithm.

Araragi initially focuses on Hanekawa's chest and wonders whether sexual desire is proof of love. Tsukihi answers that sexual desire and love are not identical. The scene is comic, excessive, and ethically messy—but it establishes the conceptual problem that the ending will distort into sacrificial grandeur.

## C. Encounter and disclosure: Hanekawa's family/non-family

Araragi meets Hanekawa and learns that the category he takes for granted—family—does not function in her household. Her disclosure moves from technical family history to active parental violence. She repeatedly minimizes the burden of telling him and rationalizes the adults who hurt her.

This is the emotional cause layer.

## D. The cat: ordinary compassion becomes supernatural opportunity

Hanekawa buries a road-killed white cat. Araragi reads this as another proof of her extraordinary kindness. Later Black Hanekawa complicates that interpretation by claiming Hanekawa felt no pity: she performed what she considered ethically correct because being “ordinary” and “right” has become a rule system.

## E. Possession becomes creation

The sawarineko initially behaves as a possession oddity. After attacking the parents, however, the case changes. Hanekawa's retained consciousness and knowledge begin driving behavior. Stress is discharged through random attacks. Black Hanekawa identifies itself as a new species/persona formed from Hanekawa's stress. Oshino later reconstructs that Hanekawa re-incorporated the departing cat.

This is the crucial ontological pivot.

## F. Araragi's failed rescue and Shinobu's intervention

Araragi recognizes that he cannot beat Black Hanekawa. He spends days prostrating himself before the silent Shinobu, eventually receives Kokorowatari, and constructs a suicidal trap inside his own body. The trap can kill the oddity but cannot solve Hanekawa's life.

Shinobu then intervenes materially: her blood restores Araragi and her vampiric drain removes the cat/stress configuration from Hanekawa.

## G. Grey ending

Nobody is healed in the strong sense.

Hanekawa loses the Black Hanekawa memories.

Her parents lose memories of her attack.

The family system remains.

Araragi preserves the Golden Week memory and tells himself his feeling was “not love.”

Oshino calls the result a grey settlement rather than a clean black/white judgment.

The story ends by continuing.

---

# 5. Narrator and focalization audit

## 5.1 V07 is an explicitly retrospective Araragi text

The first paragraphs give the reader unusually strong permission to distrust completeness. Araragi says even a detailed account will fail to reproduce the truth of the nine days. He knows more at narration-time than event-time and repeatedly announces regret.

This is not generic unreliability. It is **self-conscious retrospective reconstruction**.

## 5.2 Idealization is a focalization error, not merely a romantic flourish

Araragi's early description of Hanekawa makes her almost nonhuman in excellence. Later he discovers that this reverence has made him stupid about her suffering. The key self-correction occurs when he realizes he had implicitly assumed Hanekawa could not suffer, regret, dislike, or be unhappy simply because she was Hanekawa.

His recurring thought—effectively, “Hanekawa will be fine because she is Hanekawa”—turns admiration into neglect.

This is one of V2's strongest examples of **benevolent misrecognition**.

## 5.3 Memory gaps are flagged directly

After being injured by Black Hanekawa, Araragi explicitly notes that his recollection around loss of consciousness combines hazy memory, inference, and what he later heard. The narrator labels the reconstruction rather than pretending cinematic omniscience.

## 5.4 The imagined Shinobu speech is not dialogue evidence

At the climax Araragi “hears” Shinobu speak in the archaic first-person voice he associates with Kiss-shot. The content is psychologically revealing—especially the imagined complaint that he cannot force her to live and then assume he may die freely—but the narrator explicitly says this was likely hallucination/imagination. It must be classified as:

- TF: Shinobu appears, gives/uses Kokorowatari, heals Araragi, drains Black Hanekawa.
- NR/IT: Araragi imagines what those actions mean.
- **Not TF:** Shinobu literally spoke those lines.

This matters because V1 sometimes treated the imagined sentence too quickly as direct Shinobu testimony.

## 5.5 Araragi's romance classification is also suspect

The book spends hundreds of lines asking what love is, then ends with Araragi claiming his love for Hanekawa is not `恋` because it has exceeded romance into a wish to die for her.

That conclusion should not be accepted merely because the narrator says it. It may instead show his inability to tolerate ordinary vulnerability. Sacrificial transcendence is easier for him to conceptualize than mutually chosen romance.

The final phrase—`初恋ではない何か`—keeps the category deliberately unstable.

---

# 6. Chronology

## 6.1 Event-time sequence

The principal Golden Week sequence runs across **April 29 through May 8**.

- **April 29, Saturday:** Golden Week begins. Araragi's long discussion with Tsukihi about love/desire precedes his encounter with Hanekawa.
- Hanekawa discloses family history and that her father struck her.
- Hanekawa and Araragi encounter/bury the dead white cat.
- **Late April 29 / early April 30:** the sawarineko manifestation escalates; Hanekawa's parents are drained; Araragi is badly injured.
- **May 1–2:** ordinary school days. Hanekawa is absent; cat rumors spread.
- **May 3:** Araragi encounters Black Hanekawa at school and learns the stress-discharge logic.
- **May 3–7:** Oshino repeatedly fights/loses to Black Hanekawa; Araragi spends much of the period prostrating himself before Shinobu.
- **May 7 after sunset:** Shinobu gives Araragi access to Kokorowatari; Araragi confronts Black Hanekawa; his trap wounds/separates the oddity; Shinobu intervenes and ends the acute episode.
- **May 8:** Araragi checks the cat grave, speaks with Oshino, then returns to school where Hanekawa has no conscious memory of the Golden Week crisis.

## 6.2 Placement relative to V04 and V01–V03

Internal chronology:

`傷物語 / Spring Break → 猫物語（黒） / Golden Week → 化物語 / May onward`

Publication/archive order is different. This makes V07 the first major test of whether retrospectively referenced Golden Week events in V03 survive direct narration.

## 6.3 Narration time versus event time

The opening indicates a narrator situated later, around the approach to the second semester. Therefore statements framed as “now I understand” must not be projected backward into April 29 event consciousness.

---

# 7. Causal plot reconstruction

A causally disciplined summary is important because “Hanekawa turns into a cat because of family stress” is too compressed.

1. Hanekawa lives for years in a household in which she has no secure relational place.
2. She responds by trying unusually hard to be a correct daughter and correct person.
3. Her father physically strikes her after she comments on his work.
4. She tells Araragi but immediately rationalizes the violence and describes her own disclosure as displaced frustration.
5. She encounters a road-killed white cat and buries it.
6. A sawarineko-type phenomenon attaches to her.
7. The initial manifestation attacks the nearest/most salient targets: her parents.
8. According to Oshino's later reconstruction, that first possession would have ended there because the proximate wish had been accomplished.
9. Hanekawa's consciousness returns—but she then strongly pulls the oddity back and incorporates it rather than letting the episode end.
10. This interaction creates a new hybrid, Black Hanekawa.
11. Black Hanekawa uses energy drain on unrelated people as a crude means of discharging accumulated stress.
12. Hanekawa's retained knowledge massively increases the oddity's effectiveness and allows it to anticipate Oshino.
13. The attacks reduce acute tension but do not alter the household generating it.
14. Araragi realizes that even successful stress discharge would be temporary unless the family environment changed.
15. Black Hanekawa escalates toward renewed violence against the parents.
16. Araragi obtains Kokorowatari through Shinobu and constructs an attack trap using his own body.
17. The trap injures/separates the oddity but also leaves Araragi dying.
18. Shinobu's vampiric power restores Araragi and drains the oddity/stress formation from Hanekawa.
19. Hanekawa's memories of the Black Hanekawa episode are unavailable to her afterward.
20. Her parents also lack the relevant attack memory.
21. The family environment remains unchanged.

The most important causal conclusion is therefore:

> **The supernatural case has a terminating mechanism; the life problem does not.**

---

# 8. Oddity dossier — sawarineko and Black Hanekawa

## 8.1 The standard sawarineko template

Oshino presents `障り猫` as a low-level, almost template-like folk oddity associated with the inverse of the beckoning cat. In the didactic version, a supposedly good person helps/buries a dead cat, later behaves badly, and observers blame possession—only for the story's punchline to imply that the person's “dark side” was always there.

The folktale therefore already contains a warning about moral essentialism:

> “good person” can be a partial description rather than a whole ontology.

## 8.2 Hanekawa breaks the template

The oddity should be weak. Oshino nevertheless loses repeatedly because Hanekawa's retained consciousness supplies:

- knowledge;
- tactical anticipation;
- behavioral control;
- selective restraint;
- a massive reservoir of unresolved stress.

Oshino says the weak cat has effectively been pulled upward toward top-tier threat status because the host is Hanekawa.

## 8.3 Possession becomes assimilation

The most important mechanical revelation arrives after the crisis. Oshino says ordinary possession had effectively ended after the parents were drained. Hanekawa's consciousness came back; then she pulled the departing cat back and incorporated it.

This is not the same as saying she sat down and rationally chose “I will become Black Hanekawa.” The reconstruction comes from Oshino's altered-state questioning and inference. But it does establish a strong degree of **host participation**.

V2 classification:

- TF/CD: Oshino reports post-crisis questioning and his reconstruction.
- SI: Hanekawa participated in sustaining/reforming the oddity rather than remaining a passive vessel.
- Not justified: “therefore every act of Black Hanekawa is identical to conscious Hanekawa's deliberate choice.”

## 8.4 Black Hanekawa as stress personification

Black Hanekawa calls itself:

> `ご主人のストレスが具現化して現れた人格という怪異`

The phrase is central but should not be treated as a complete scientific definition. It is a diegetic self-description from a hybrid entity whose intelligence is partly cat-like and whose knowledge is partly Hanekawa's.

It is nevertheless excellent evidence for function: the entity converts disallowed affect into behavior.

## 8.5 Stress disposal is not recovery

Black Hanekawa proposes attacking hundreds more people until enough stress has been discharged for the entity to disappear. Araragi sees the obvious flaw: the household remains, so the stress-generating condition remains.

Oshino later adds a stranger point: total elimination of tension may itself destabilize Hanekawa. His analogy resembles structural tension—remove everything that keeps a system taut and the system can collapse differently.

Thus V07's stress model is not therapeutic catharsis. “Venting everything” is not automatically healthy.

## 8.6 The cat's “no sympathy” claim

Black Hanekawa says Hanekawa did not pity the dead cat at all; she buried it because correct treatment of a dead animal had become a rule/equation. This is powerful evidence, but it needs speaker discipline.

The cat claims special competence here because ordinary sawarineko mechanics exploit pity and it says there was no such opening. It also shares Hanekawa's memories/knowledge. Yet it explicitly says it does not automatically know what Hanekawa felt about every remembered event.

The safest formulation is:

> **V07 strongly supports that Hanekawa's ethical action can operate independently of consciously felt pity; it does not prove that Hanekawa is globally emotionless.**

## 8.7 Oddity as explanatory mercy

Near the end, Oshino says something deliberately destabilizing: sometimes it is more bearable to say a yokai caused a crisis than to state without mediation that a girl crushed by family stress began acting violently. The supernatural remains literally real, but the **explanatory frame** can also function as responsibility displacement and mercy.

This strongly strengthens V1's “narrative bodies” thesis while preventing a reductive metaphor reading.

Oddities are real.

The stories told about oddities are also moral technologies.

---

# 9. Character pressure analysis

## 9.1 Hanekawa Tsubasa — goodness as adaptation

The most important Hanekawa sentence in V07 may not be spoken by Black Hanekawa at all. It is ordinary Hanekawa saying:

> `私はこんなに。娘らしくしているつもりなのに`

She is trying.

That verb-level fact matters. Daughterhood is not a secure status she possesses; it is a role she performs in hope that performance might produce relationship.

The same architecture appears in her moral identity. She does not simply “happen to be good.” She attempts to become an ordinary/right girl through repeated ethical compliance. The paradox is that she performs ordinary correctness so perfectly that she becomes abnormal.

### Core V07 formulation

> **Hanekawa is not good because she lacks darker feelings. She has made goodness into a discipline for surviving a life in which expressing inconvenient feeling threatens belonging she does not securely possess.**

## 9.2 Hanekawa and internalized culpability

Her explanation for being hit is structurally revealing. She reasons that perhaps she disturbed a stable household by trying to approach adults who had already settled into emotional distance. This converts victimization into systems maintenance: if the system had equilibrium before she asked for relationship, perhaps she is the disruptive variable.

The logic culminates in `私は私だから──殴られても仕方がない`.

V2 rejects that conclusion normatively. The source shows how she reaches it; it does not make it ethically valid.

## 9.3 Araragi — pedestalization as failed seeing

Araragi's admiration is enormous. He cannot initially conceptualize Hanekawa as someone who might:

- hate;
- regret;
- resent;
- be petty;
- need help;
- be unhappy.

That makes his admiration dangerous. A person treated as “too good to suffer” may receive less care than an obviously vulnerable person.

The house discovery is the point where idealization fails empirically. Hanekawa's house contains no room that belongs to her and almost no concentrated trace of her presence. Her possessions are distributed through functional/shared spaces like the belongings of a transient guest. Araragi's “Hanekawa will be okay because she is Hanekawa” becomes indefensible.

## 9.4 Araragi — romance converted into sacrifice

The Tsukihi conversation exposes his inability to name ordinary romantic feeling. The later confession then makes a peculiar move:

- he loves Hanekawa;
- it is not romance;
- it is “beyond” romance;
- because he wants to die for her.

This is not maturity. It is one of the clearest early examples of Araragi turning intimacy into self-erasure. He can conceptualize death for Hanekawa more easily than reciprocal ordinary desire.

## 9.5 Shinobu — agency through action before speech

Shinobu is still largely silent. That makes action disproportionately important.

She:

- remains near Araragi after injury, strengthening regeneration;
- accepts blood repeatedly;
- eventually supplies Kokorowatari;
- restores him with her blood;
- personally drains the Black Hanekawa formation.

Araragi initially interprets some of this through hunger/dependence. Oshino pushes back, implying Araragi is missing relational meaning.

Yet exact motive remains open. The strongest “you kept me alive, so you cannot die freely” formulation is Araragi's imagined voice, not verified speech.

## 9.6 Oshino — competent enough to know he cannot force a cure

Oshino loses repeatedly and does not turn those losses into omnipotent theatricality. He distinguishes:

- what a specialist can do;
- what a friend knows;
- what is actually the afflicted person's responsibility;
- when continued intervention becomes self-aggrandizing.

His limitations are part of his ethics.

---

# 10. Relationship-state audit

## 10.1 Araragi ↔ Hanekawa

**State entering V07:** newly formed friendship after Spring Break, with enormous debt/idealization from Araragi.

**V07 change:** intimacy increases through disclosure, but asymmetry worsens. Hanekawa tells him about family violence while simultaneously refusing him the right to redistribute that knowledge. Araragi learns more facts but repeatedly fails to understand what those facts mean.

He wants to help but cannot tolerate ordinary helplessness. His eventual choice of suicidal intervention is therefore relationally sincere and ethically distorted.

**State leaving V07:** Araragi carries a private memory and feeling Hanekawa does not consciously share. He promises normal treatment. The relationship is close but epistemically asymmetric.

## 10.2 Hanekawa ↔ her parents

The relationship is not adequately described by “bad family.” Hanekawa herself says they are not family, though they share a house and parental titles.

Material indicators:

- no room belonging to her;
- no consolidated trace of her life;
- emotional distance normalized as equilibrium;
- physical violence by father;
- mother observes without intervention;
- Hanekawa tries to perform daughterhood anyway.

The crisis does not repair this structure.

## 10.3 Araragi ↔ Shinobu

V07 advances their relation without pretending reconciliation is complete.

Araragi spends days in an indirect request/apology posture rather than issuing a command. Shinobu ultimately assists. Their interdependence is becoming practical and moral, but resentment and hierarchy remain.

This is an important bridge between V04's coercive bad ending and V05/V06's more explicit later `歩み寄り`.

## 10.4 Araragi ↔ Fire Sisters / family contrast

The Araragi household is intrusive, comic, boundary-poor, and sometimes ridiculous. It is not idealized as perfect. But Araragi has:

- people who notice his absence;
- sisters who invade his room;
- ordinary shared objects and routines;
- a place in the household that cannot be mistaken for temporary lodging.

His reaction after seeing Hanekawa's house—returning home and clinging to Tsukihi—shows that mundane family friction can itself be evidence of belonging.

## 10.5 Non-possession test

V07 produces mixed results.

Positive:

- Araragi recognizes Hanekawa has not asked him to intervene.
- He temporarily accepts Oshino's instruction not to make himself the resolver.
- He recognizes that defeating the oddity does not give him authorship over Hanekawa's life.

Negative:

- he enters her house without permission;
- he frames dying for her as a private wish that does not require her consent;
- he acts through a lethal plan she did not request;
- the post-crisis arrangement leaves her without knowledge of events central to her own body/history.

V07 therefore shows the early **conceptual discovery of non-possession without stable behavioral mastery**.

---

# 11. Rescue, care, and intervention audit

## 11.1 Oshino's strongest warning to Araragi so far

Oshino tells Araragi that responsibility does not mean every responsible person must personally resolve every problem. He explicitly says that sometimes a person can abandon responsibility and the situation may still be resolved by someone else.

This is a direct challenge to Araragi's rescue compulsion.

Even more precise is:

> `命懸けになることと、死んでもいいと思うことは違う`

Risking oneself for something and believing one's death is acceptable are not the same ethical posture.

This distinction should become a major longitudinal rescue criterion.

## 11.2 Hanekawa's refusal matters

Araragi eventually admits the simplest reason not to intervene: Hanekawa did not ask. Earlier she rejected being taken home and tightly controlled disclosure.

This is source-level evidence that **help without invitation is a problem the series recognizes early**.

## 11.3 But “she didn't say help” is also too simple

Near the end, Oshino adds a complication: not saying `助けて` does not necessarily mean no help was sought, just as not saying `好き` does not mean no love exists. Some words are too difficult to say lightly.

This prevents consent/request analysis from collapsing into formalism.

V2 should distinguish:

- explicit request;
- implicit distress signal;
- demonstrated refusal;
- inability to ask;
- unilateral intervention despite known refusal.

Those are not interchangeable.

## 11.4 Black Hanekawa as self-rescue system

Oshino says Hanekawa could not seek a hero outside herself, so she grew/created one inside herself. Black Hanekawa is therefore a grotesque answer to failed help-seeking:

> a rescuer that requires no vulnerable request because it is built from the same person.

But that “hero” hurts strangers, threatens family, erases memory, and risks absorbing Hanekawa entirely.

Self-reliance becomes self-fragmentation.

## 11.5 Araragi's Kokorowatari plan is knowingly inadequate

The cleanest intervention available is supernatural excision. Araragi understands while using it that:

- the family will remain;
- the stress structure will remain;
- the oddity alone will disappear;
- the situation will approximately reset to before Golden Week.

This is the clearest source confirmation so far that **ending the monster-of-the-week event is not equivalent to saving the person**.

## 11.6 Shinobu's intervention and reciprocal consequence

Shinobu's action prevents Araragi's chosen death. It also ends the Black Hanekawa formation through superior vampiric drain.

Retrospectively, this is the first strong post-Kizu case where Araragi's decision to preserve Kiss-shot's life produces reciprocal constraint on his own freedom to self-destruct. But motive must remain partly inferred because the explicit articulation appears in his hallucinated/imaginative reconstruction of her voice.

---

# 12. Specialist ethics and metaphysics

## 12.1 Oshino is not an omniscient exorcist

V07 makes his fallibility concrete. He can lose a hundred times. He can mislocate a grave. He can be surprised by Shinobu's weapon. His expertise is real without being omnipotent.

That distinction is important for the whole specialist system.

## 12.2 Specialist knowledge is modular

Oshino knows oddity classification and pursuit.

Araragi knows person-specific habits and spaces.

Shinobu knows vampiric/weapon capabilities unknown to Oshino.

Black Hanekawa knows Hanekawa's stored knowledge.

No single observer possesses the whole case.

This is a practical embodiment of the V2 anti-master-key rule.

## 12.3 Oshino's professional restraint

He tells Araragi to go home partly because Araragi has family who will worry. He refuses to turn the teenager's guilt into a job qualification. He also knows that simply killing/exorcising the hybrid would not solve what he considers the underlying human problem.

His repeated defeats therefore are not only evidence of insufficient power. They also reflect a restricted acceptable-solution set.

## 12.4 “Grey settlement” as specialist ethics

Oshino eventually accepts `白黒つけない、グレーの決着`.

That is not relativism. It acknowledges that:

- Hanekawa participated in creating the hybrid;
- she was also under severe structural pressure;
- the oddity was literally real;
- blaming only the oddity would be false;
- blaming only Hanekawa would be cruel and incomplete;
- the available intervention cannot repair the household.

The professional endpoint is not moral purity but an arrangement in which immediate catastrophe stops without pretending the past has become simple.

## 12.5 Explanatory models can be merciful fictions without being useless

Oshino's statement that it may be more bearable to call the crisis “Black Hanekawa” or “a yokai” than to describe it solely as a girl crushed by family stress is one of the series' most important early metaphysical comments.

It implies that supernatural naming can:

- assign causality;
- distribute responsibility;
- make intolerable facts narratable;
- create an intervention target;
- preserve enough distance for a person to continue.

But the cost is that the name may conceal human causes.

---

# 13. Japanese voice and address audit

## 13.1 Hanekawa's ordinary voice

Hanekawa's ordinary speech is calm, explanatory, and often self-minimizing. Severe content enters through conversationally soft packaging:

- `私には家族って、いないんだよね`
- `ただ、家族じゃないだけ`
- `私はこんなに。娘らしくしているつもりなのに`

The effect is important. She does not perform suffering through heightened melodrama. The emotional compression itself is characterization.

Her repeated reframing of disclosure as `八つ当たり`, `憂さ晴らし`, or `欲求不満の解消` demonstrates how rapidly she translates need into apology.

## 13.2 Black Hanekawa's voice

Black Hanekawa uses:

- first person `俺`;
- Hanekawa as `ご主人`;
- rough colloquial syntax;
- pervasive cat-speech `にゃ` transformations;
- blunt vulgarity and verbal aggression.

The register is radically unlike ordinary Hanekawa.

But V2 should not translate this as “the true Hanekawa finally speaks honestly.” The voice belongs to a hybrid character with explicit `キャラ設定`, feline constraints, and Hanekawa-derived knowledge.

Its speech can reveal things ordinary Hanekawa suppresses without becoming an unfiltered transcript of her consciousness.

## 13.3 Oshino's lightness under pressure

Oshino's familiar casualness persists even while discussing killing Hanekawa if the takeover becomes complete. Araragi explicitly notes that Oshino tends to say the most serious things lightly.

Register therefore functions as professional distance, not proof of moral indifference.

## 13.4 Silent Shinobu and projected voice

The imagined archaic `儂` speech belongs to Araragi's mental reconstruction of Kiss-shot's voice. Because he explicitly retracts it as likely hallucination, the Japanese voice ledger must preserve the distinction between:

- historical Kiss-shot voice known from V04;
- V07 silent Shinobu action;
- Araragi's projection of Kiss-shot-like speech onto that action.

---

# 14. Names, wordplay, ruby, and translation-sensitive analysis

## 14.1 「つばさファミリー」

The title is cruelly ironic. The story named “Tsubasa Family” centers on Hanekawa's insistence that the people in her house are not family and on the discovery that she has no room in that house.

The title therefore names an absence as though it were a possession.

## 14.2 障り猫 / 招き猫

Oshino explains the sawarineko partly through opposition to `招き猫`: one invites fortune; the other brings affliction/obstruction. English can convey the semantic contrast, but the compact wordplay is stronger in Japanese.

## 14.3 猫をかぶる

`猫をかぶる` means to put on a meek/innocent facade. V07 literalizes the idiom through supernatural cat imagery. This is one reason simplistic “dark side” reading feels tempting—but the story then complicates the idiom by turning the “cat” from mask into hybrid body and independent causal agent.

## 14.4 黒 / 白 / grey settlement

The book repeatedly organizes moral perception through black/white vocabulary:

- white cat;
- Black Hanekawa;
- `暗黒面`;
- pure/impure correctness;
- final `グレーの決着`.

Oshino's grey settlement is not merely a color joke. It becomes a refusal to let either “Hanekawa is innocent because oddity” or “Hanekawa is evil because violence” monopolize the account.

## 14.5 「何でもは知らない」 precursor logic

At the climax Araragi weaponizes a limit on knowledge: Hanekawa/Black Hanekawa does **not** know Kokorowatari exists. He begs her not to act as though she knows enough to make total judgments about herself.

The key logic is epistemic rather than simply catchphrase-based:

> lack of total knowledge blocks total self-condemnation.

## 14.6 可哀想 / 同情 / 哀れむ

V07 repeatedly distinguishes care from pity. Araragi interprets Hanekawa's refusal to pity him during Spring Break as treating him equally rather than looking down on him. This is morally meaningful, but V2 should preserve a caution: **all pity is not necessarily contempt**, and Hanekawa's inability to receive compassionate recognition may itself be part of her isolation.

---

# 15. Body, appetite, sexuality, gaze, and comedy

## 15.1 The opening sexuality debate is structurally relevant

The long underwear/romance conversation does several things simultaneously:

- parodies fanservice and incest comedy;
- establishes Tsukihi as an unexpectedly sharp analyst of romantic feeling;
- separates sexual appetite from romantic love;
- exposes Araragi's attempt to rationalize feeling through categories;
- primes the later question of what he actually wants from Hanekawa.

It is therefore not analytically disposable.

## 15.2 But structural relevance does not exculpate sexualization

Araragi repeatedly returns to Hanekawa's breasts, legs, underwear, and exposed body even in scenes of danger. The prose knows this is ridiculous and often mocks him for it.

Self-mockery does not erase objectification.

The V2 position remains:

> **Monogatari can use erotic gaze as characterization and comedy while simultaneously participating in the gaze it critiques.**

## 15.3 The body as evidence of unspoken violence

Hanekawa's bruised/swollen face forces family violence into material visibility. Araragi's residual vampire blood can erase much of that visible evidence. He does so partly because he knows she would resist direct assistance.

This produces an uneasy care question: healing the face helps her, but it also allows the household violence to become less socially legible.

## 15.4 Araragi turns his body into a weapon container

The climax radicalizes V04's body-as-payment pattern. Araragi literally uses his torso/spinal axis to conceal Kokorowatari so that Black Hanekawa will strike the weapon while tearing him apart.

His body becomes:

- bait;
- sheath;
- trap;
- expendable material.

This is perhaps the clearest early image of self-objectification in his rescue ethic.

## 15.5 Shinobu's blood reverses the economy

Araragi's blood has repeatedly sustained Shinobu. At the climax her blood restores him. Their bodily economy is becoming genuinely reciprocal even while the relationship remains unequal and wounded.

---

# 16. Family, home, and institutions

## 16.1 V06/V07 create a powerful family inversion

V06 gave us Tsukihi:

- nonhuman/supernatural origin;
- unquestionably treated by Araragi as sister/family.

V07 gives us Hanekawa:

- ordinary human biological history;
- people called father/mother;
- a house;
- but no experienced family belonging.

Together they provide strong cumulative evidence:

> **In Monogatari, family is not guaranteed by biological ontology, household co-residence, or naming. It is enacted through recognition, obligation, presence, conflict, and a durable place for the other person.**

## 16.2 The room is the strongest spatial evidence

`羽川家には、羽川翼の部屋がなかったのだ`.

The fact is more powerful than a symbolic paraphrase. She has lived there for years, yet there is no room around which her personhood coheres. Her belongings are distributed in functional/shared locations. Araragi compares the arrangement to hotel living and then realizes even “lodger” may overstate her embeddedness.

Home exists architecturally without functioning relationally.

## 16.3 The Araragi household is not ideal, but it has friction

Karen and Tsukihi are intrusive. The siblings bicker. Privacy is porous. Their comedy is sometimes aggressively boundary-insensitive.

But the household produces continuous evidence that Araragi exists **to other people**. The contrast with Hanekawa is not “good family versus evil family” so much as:

> messy belonging versus orderly non-belonging.

## 16.4 School fails to see the private crisis

Hanekawa's absence becomes an attendance fact and a rumor surface. The institution does not know what is happening at home. Her competence as class president likely makes her less legible as someone who might need intervention.

The private household wound therefore becomes visible publicly only after it has transformed into an impossible supernatural incident.

## 16.5 “Family as oddity” is an interpretation the text itself challenges

Araragi proposes that family itself may have been Hanekawa's long-term oddity. Oshino pushes back and warns him not to confuse a familiar schematic image with actual knowledge—his weather-map analogy says seeing the representation is not knowing the whole country.

This is an unusually useful anti-overinterpretation scene. The metaphor is suggestive; the novel refuses to certify it as total explanation.

---

# 17. Major thematic modules

## 17.1 Story versus problem

The governing line is:

> `物語は完結するけれど、問題は解決しない`

V07 distinguishes the needs of narrative closure from the conditions of human life. The reader can receive a climax; Hanekawa can still wake up in the same house.

## 17.2 Ordinary as impossible ideal

Hanekawa wants to be `普通の女の子`. Yet her definition of ordinary becomes relentlessly ethical: do the correct thing, follow the rule, make no trouble, be the daughter one should be.

The harder she tries to perform ordinary moral life, the less ordinary she appears.

## 17.3 Goodness without feeling

The cat-burial revelation asks whether ethically correct action requires the appropriate feeling.

V07 does not give an easy answer.

Hanekawa's action remains good in outcome and form.

But if moral action becomes an automatic law used to suppress affect, it can contribute to psychic fracture.

This anticipates the larger fake/real problem from V05–V06: constructed behavior can be real and valuable while still raising questions about ownership.

## 17.4 Responsibility without purity

Hanekawa is both victim and participant.

Her parents' violence is not justified by her later violence.

Her later violence is not justified by their abuse.

Black Hanekawa's supernatural status does not erase Hanekawa's causal participation.

Oshino's grey settlement is therefore an ethics of responsibility without requiring a pure victim/pure offender binary.

## 17.5 Rescue and the fantasy of the clean fix

Kokorowatari is almost the perfect symbol of the clean intervention: a blade that cuts only the oddity.

The book then tells us why even that is insufficient.

A perfectly targeted supernatural tool cannot cut away an abusive/non-family household.

## 17.6 Memory and survivable continuity

Hanekawa loses the Black Hanekawa memory. Her parents lose memory of being attacked. Araragi alone retains the full emotional burden.

Forgetting allows ordinary life to restart, but it also preserves the causes untouched.

V07 therefore treats forgetting neither as simple healing nor simple cowardice. It is a survival technology with costs.

---

# 18. Counterreadings and adversarial tests

## Counterreading A — “Black Hanekawa is simply Hanekawa's real personality.”

**Why tempting:** Oshino uses `裏側`, `暗黒面`, `猫をかぶる`; Black Hanekawa expresses violence and vulgarity ordinary Hanekawa suppresses.

**Why inadequate:** the entity is mechanically hybrid, obeys feline `キャラ設定`, possesses its own intelligence limits, shares knowledge without full affective access, and is explicitly described as a newly generated oddity. Hanekawa also consciously/semiconsciously participates in its creation without becoming identical to it.

**Verdict:** reject singular true-self reading.

## Counterreading B — “Hanekawa is not actually compassionate; she is an emotionless moral machine.”

**Why tempting:** Black Hanekawa says there was no pity when she buried the cat; Araragi calls her ethics a `戒律`.

**Why inadequate:** this is one scene and one speaker's mechanically privileged inference. It establishes separation between correct action and conscious pity, not global absence of emotion. The book itself shows shame, frustration, need, attachment, and distress.

**Verdict:** narrow to over-regulated affect rather than emotionlessness.

## Counterreading C — “The parents caused Black Hanekawa, therefore Hanekawa bears no responsibility.”

**Why tempting:** the household pressure is enormous and parental violence is a clear precipitating cause.

**Why inadequate:** Oshino's reconstruction says ordinary possession could have ended after the parents were attacked; Hanekawa then pulled the cat back and enabled subsequent indiscriminate harm.

**Verdict:** structural coercion and agency coexist.

## Counterreading D — “Araragi saves Hanekawa.”

**Why tempting:** he acquires the weapon, confronts the oddity, prevents renewed parental violence, and participates in ending the crisis.

**Why inadequate:** he explicitly knows the problem is not solved; Shinobu performs the decisive final intervention; Hanekawa returns to the same household; the ending calls the issue postponed.

**Verdict:** Araragi helps terminate an acute event, not cure Hanekawa.

## Counterreading E — “Oshino's self-saving doctrine means never help anyone.”

**Why tempting:** he repeatedly says people save themselves and tells Araragi to stop.

**Why inadequate:** Oshino himself spends days fighting, diagnoses the case, collects evidence, negotiates, and accepts collaborative intervention. His point concerns authorship and limits, not abstention.

**Verdict:** self-saving is locus-of-agency doctrine, not non-intervention absolutism.

## Counterreading F — “Family itself is the real monster.”

**Why tempting:** Araragi proposes nearly this formulation.

**Why inadequate:** Oshino immediately warns against half-understood abstraction. “Family” includes countless structures; the problem is this household's concrete relationships, violence, absence, and expectations.

**Verdict:** useful metaphor, not governing ontology.

---

# 19. V1 claim audit

| V1 proposition | V07 status | V2 revision |
|---|---|---|
| Black Hanekawa is an emergency stress-exhaust system rather than simply a “dark side” | **STRONGLY CONFIRMED + REFINED** | Stress-discharge function is explicit; however system is harmful, self-reinforcing, and not cure. |
| Hanekawa's goodness is over-adaptation/self-erasure | **STRONGLY CONFIRMED** | `娘らしく` effort, rule/equation ethics, apology for venting, and self-blame make adaptation source-visible. |
| 「つばさファミリー」 is about absence of family | **STRONGLY CONFIRMED** | Hanekawa explicitly says she has no family; house has no room belonging to her. |
| House has objects but not Hanekawa's trace/belonging | **DIRECTLY CONFIRMED** | Belongings are dispersed; no room; Araragi compares it to hotel/guest existence. |
| Araragi knows facts about Hanekawa but not their meaning because of idealization | **STRONGLY CONFIRMED** | He repeatedly realizes “Hanekawa because Hanekawa” was a substitute for seeing vulnerability. |
| Black Hanekawa is not “true Hanekawa” | **STRONGLY CONFIRMED + MECHANICALLY GROUNDED** | New hybrid oddity with feline settings + Hanekawa knowledge + host participation. |
| Kokorowatari represents fantasy of clean intervention | **EXPLICITLY CONFIRMED** | `物語は完結するけれど、問題は解決しない`; cutting oddity resets situation but not household. |
| Araragi turns his body into equipment | **EXTREMELY STRENGTHENED** | He literally makes his body the sheath/trap for Kokorowatari. |
| Shinobu refuses to let him die because he refused her death | **MOTIVE NARROWED / ACTION CONFIRMED** | Her intervention is TF; the explicit reciprocal-debt speech is Araragi's hallucinated/projected voice. |
| “I won't pity you” is equality/recognition | **SUPPORTED + COMPLICATED** | Anti-pity is framed as refusal to look down; but lack of compassionate recognition can also isolate Hanekawa. |
| Family/home is the hidden wound beneath the cat | **STRONGLY CONFIRMED, NOT TOTALIZED** | Household structure is core causal pressure; Oshino rejects “family itself = oddity” as too broad. |
| Ending is postponement rather than resolution | **DIRECTLY CONFIRMED** | The novel literally says the problem was postponed. |
| The story critiques clean moral binaries | **STRONGLY CONFIRMED** | final `グレーの決着`; victim/agent, good/dark, oddity/human responsibility all overlap. |

### Highest-value V1→V2 revision

V1's phrase “Black Hanekawa is Hanekawa's emergency exhaust system” should be retained but expanded:

> **Black Hanekawa is a partly self-authored emergency affect-disposal system created through the interaction of an external sawarineko and Hanekawa's over-regulated consciousness. It can discharge stress but cannot solve the conditions producing stress, and its operation externalizes costs onto other people while risking the disappearance of Hanekawa herself.**

That formulation preserves the insight without romanticizing the mechanism.

---

# 20. Retrospective later-material revision routes

This section records routes for later audit without allowing later material to overwrite V07's publication-local uncertainty.

## 20.1 『猫物語（白）』

Must test:

- whether Hanekawa herself accepts, revises, or rejects the “goodness as emotional emptiness” framing;
- whether Black Hanekawa becomes kin/part rather than disposable symptom;
- how jealousy/envy changes the externalization model;
- whether integration becomes possible without declaring one side authentic and the other false;
- how `ただいま` and home language revise V07's no-room/no-family architecture.

## 20.2 Later Shinobu material

Must test whether the reciprocal meaning Araragi imagines in V07 becomes something Shinobu later articulates independently. V07 cannot itself prove her motive through the hallucinated speech.

## 20.3 Later Araragi rescue practice

Must test whether he learns Oshino's distinction between:

- risking oneself;
- wanting to die;
- helping;
- assuming ownership of resolution.

## 20.4 Later family synthesis

V06/V07 already produce an important paired claim:

- Tsukihi: nonhuman origin, real family.
- Hanekawa: human origin, household without family.

Later family documents should test whether this relation-based definition survives marriage, adoption, cohabitation, adult household formation, and specialist-created persons.

---

# 21. Primary-source evidence locator

Canonical citation format:

`V07 — 『猫物語（黒）』 — つばさファミリー — section / local paragraph — scene anchor`

| # | Locator | Evidence / use |
|---:|---|---|
| 1 | V07 — opening — `[split_000:0003–0008]` | nine Golden Week days; narrator says full truth cannot be transmitted |
| 2 | V07 — opening — `[split_000:0029–0048]` | retrospective regret; current understanding differs from event-time understanding |
| 3 | V07 — 001 — `[split_000:0453–0819]` | Tsukihi/Araragi debate about how to identify love; reason versus felt preference |
| 4 | V07 — 001 — `[split_000:0890–0976]` | sexual attraction distinguished from romantic love |
| 5 | V07 — 002/003 — `[split_001:0532–0555]` | `私には家族って、いないんだよね`; household versus family distinction |
| 6 | V07 — family disclosure — `[split_001:0622–0643]` | no blood relation to current parents; `娘らしく` effort; Araragi catches idealization |
| 7 | V07 — disclosure — `[split_001:0653–0665]` | Hanekawa labels disclosure venting/displaced frustration and worries she burdened Araragi |
| 8 | V07 — disclosure — `[split_001:0723–0786]` | father hit her; mother watched; rationalization; `私は私だから──殴られても仕方がない` |
| 9 | V07 — aftermath — `[split_001:1056–1100]` | Araragi heals face; Hanekawa says parents may not notice; refuses ride/home intervention |
| 10 | V07 — cat burial — `[split_002:0151–0207]` | burial; Oshino says Hanekawa + sawarineko is unusually compatible |
| 11 | V07 — first Black Hanekawa encounter — `[split_002:0381–0499]` | hybrid violence; parents delivered; Araragi's arm torn off; stress language begins |
| 12 | V07 — narrator audit — `[split_002:0516–0552]` | memory gap around unconsciousness; later account mixes inference/hearsay/hazy recall |
| 13 | V07 — Shinobu proximity — `[split_002:0633–0718]` | her proximity strengthens Araragi healing; she remains with him; Oshino challenges his reduction to feeding |
| 14 | V07 — Oshino intervention limit — `[split_002:0735–0796]` | family worry; Araragi should go home; responsibility does not mean personally solving everything |
| 15 | V07 — Hanekawa refusal — `[split_002:0809–0817]` | Araragi acknowledges she did not ask him and rejected intervention |
| 16 | V07 — house — `[split_002:0835–0943]` | old `つばさ` nameplate; no room; belongings dispersed; no trace of durable belonging |
| 17 | V07 — house reflection — `[split_002:0953–0984]` | supernatural resolution will not reconcile family; Araragi also notes household may have been unhappy for all |
| 18 | V07 — Oshino defeats — `[split_002:1195–1279]` | ~20 losses at that point; weak sawarineko amplified by Hanekawa knowledge/consciousness |
| 19 | V07 — standard sawarineko tale — `[split_002:1282–1315]` | didactic hidden-side template; `猫をかぶる`; Hanekawa exceptional assimilation |
| 20 | V07 — controlled public harm — `[split_002:1335–1344]` | victims mostly not lethally injured; retained Hanekawa consciousness appears to restrain damage |
| 21 | V07 — Hanekawa influence on Araragi — `[split_002:1372–1382]` | Araragi says he feels rebuilt by Hanekawa but cannot know her mind by sitting in her seat |
| 22 | V07 — Black Hanekawa stress explanation — `[split_003:0084–0159]` | indiscriminate energy drain as `憂さ晴らし`; 15 years of household pressure; self-description as stress-personified new oddity |
| 23 | V07 — no-pity cat burial — `[split_003:0170–0212]` | cat says no sympathy; ethical routine/equation; ordinary-girl wish; Araragi calls it `戒律` |
| 24 | V07 — threatened renewed family violence — `[split_003:0234–0258]` | Araragi points out stress will return; cat proposes stronger retaliation against parents |
| 25 | V07 — Araragi feeling — `[split_003:0271–0297]` | loves Hanekawa, calls it not romance, defines feeling through wish to die for her |
| 26 | V07 — Oshino rescue warning — `[split_003:0334–0368]` | `命懸けになることと、死んでもいいと思うことは違う`; Araragi admits he acts from desire rather than duty |
| 27 | V07 — Kokorowatari climax — `[split_003:0835–0979]` | Araragi's body trap; oddity-only blade; knowledge limit; `物語は完結するけれど、問題は解決しない` |
| 28 | V07 — Shinobu intervention — `[split_003:1040–1105]` | imagined speech explicitly marked hallucination; TF actions: blood healing + vampiric drain; stress absorbed |
| 29 | V07 — immediate ending — `[split_003:1105–1116]` | Hanekawa answers “not okay”; narrator: problem postponed |
| 30 | V07 — post-crisis Black Hanekawa reconstruction — `[split_003:1187–1240]` | name Black Hanekawa; initial possession ends; Hanekawa pulls cat back; new hybrid born |
| 31 | V07 — grey explanation — `[split_003:1240–1285]` | stress not cured by venting; memory outsourcing; oddity explanation as merciful responsibility displacement; grey settlement |
| 32 | V07 — family-as-oddity challenge — `[split_003:1291–1321]` | Araragi proposes family as oddity; Oshino warns against schematic partial knowledge |
| 33 | V07 — implicit help / love — `[split_003:1353–1373]` | not saying `助けて` or `好き` does not prove absence; some words cannot be lightly spoken |
| 34 | V07 — final emotional classification — `[split_003:1381–1400]` | Araragi predicts future love elsewhere; preserves Golden Week feeling as `初恋ではない何か` |
| 35 | V07 — afterword — `part0003.html` | paratext: problems need not always be solved; unresolved problems can function as environment; book identified as sixth series volume |

---

# 22. Open questions carried forward

1. What precisely did Hanekawa consciously experience during the moment she re-incorporated the cat?
2. How much of Oshino's post-hypnotic reconstruction is direct testimony versus specialist inference?
3. Does “no pity” at the cat burial mean affective absence, emotional suppression, or simply action independent of pity?
4. Can Hanekawa develop a form of goodness that does not require disowning negative affect?
5. Is Black Hanekawa best modeled as part, sibling, tool, alter, oddity, or some combination—and does that category change later?
6. What is ethically lost when memory is outsourced to Black Hanekawa?
7. Does forgetting Golden Week protect Hanekawa or preserve the system injuring her—or both?
8. Would direct disclosure of the parents' abuse to another adult/institution have changed anything? The volume does not seriously explore this route.
9. How should V2 distinguish anti-pity equality from compassionate acknowledgment of vulnerability?
10. Does Araragi's “not romance because I want to die for her” formulation reveal devotion or inability to imagine mutual ordinary love?
11. To what degree does Shinobu's V07 intervention express chosen care versus self-preservation, debt, resentment, or appetite?
12. Does later Hanekawa ever reinterpret the household as family, non-family, or something else?
13. How does `猫物語（白）` change the relation between memory, affect, and self-authorship?
14. Will later specialist practice retain Oshino's willingness to accept grey/non-total resolutions?

---

# 23. Cumulative ledger updates required after V07

## L01 — chronology

Add Golden Week April 29–May 8 between Kizumonogatari and Bakemonogatari; distinguish event time from second-semester retrospective narration time.

## L02 — narrator/focalization

Add:

- explicit disclaimer that full truth cannot be transmitted;
- retrospective regret frame;
- idealization as focalization failure;
- memory-gap disclosure;
- imagined Shinobu speech must not be classified as literal dialogue;
- romance classification as potentially defensive narrator interpretation.

## L03 — oddity mechanics/residue

Add:

- standard sawarineko template;
- host amplification;
- possession → host re-incorporation → Black Hanekawa new-oddity transition;
- stress-personification function;
- selective energy-drain restraint;
- memory outsourcing;
- acute excision does not remove causal environment.

## L04 — character/self-story

Add:

- Hanekawa `普通の女の子` aspiration;
- daughter-role effort;
- internalized culpability for abuse;
- ethical `戒律` model with speaker caution;
- Black Hanekawa not privileged as singular true self;
- Araragi “Hanekawa because Hanekawa” pedestalization correction.

## L05 — relationship/address

Add:

- Hanekawa/Araragi disclosure + secrecy asymmetry;
- Araragi/Hanekawa love classification (`好き` but `恋` denied);
- Araragi/Shinobu indirect request/action reciprocity;
- family presence/non-presence comparison;
- non-possession mixed verdict.

## L06 — specialist ethics

Add:

- professional limits and repeated defeat;
- responsibility ≠ personal monopoly on resolution;
- `命懸け` ≠ `死んでもいい`;
- grey settlement;
- explanatory mercy/responsibility-displacement function of oddity naming;
- Oshino explicitly warns against family-as-total-metaphor.

## L07 — body/materiality

Add:

- parental violence on Hanekawa's face;
- healing removes visible evidence;
- cat/body transformation;
- house without room as spatial/material non-belonging;
- Araragi body-as-sheath/trap;
- reciprocal blood economy with Shinobu.

## L08 — Japanese language/index

Add:

- `つばさファミリー` irony;
- `障り猫 / 招き猫`;
- `猫をかぶる`;
- `普通の女の子`;
- `戒律`;
- `憂さ晴らし / 欲求不満`;
- Black Hanekawa `俺 / ご主人 / にゃ` register;
- `白黒つけない、グレーの決着`;
- `物語は完結するけれど、問題は解決しない`;
- `初恋ではない何か`.

## L09 — V1→V2 revision

Upgrade:

- Hanekawa over-adaptation: strongly confirmed;
- Black Hanekawa exhaust-system model: strongly confirmed but refined;
- clean exorcism/cure distinction: directly confirmed;
- Araragi pedestalization: strongly confirmed;
- house/no-belonging: directly confirmed;
- Shinobu motive: narrow direct-speech claims because key line is hallucinated;
- unresolved/postponed ending: directly confirmed.

---

# 24. Compact reusable formulations

### Hanekawa
> **Hanekawa's goodness is real, but it is not effortless innocence. V07 presents it as disciplined correctness developed in a household where being inconvenient threatens the little belonging she has.**

### Black Hanekawa
> **Black Hanekawa is not Hanekawa's “true dark self.” It is a hybrid oddity partly formed from an external sawarineko and partly self-authored through Hanekawa's need for a body that can perform disallowed affect.**

### Family
> **V06 and V07 together sever family from biology: Tsukihi is nonhuman by origin yet unquestionably family; Hanekawa is human and housed with parents yet experiences no family at all.**

### Araragi's idealization
> **Araragi does not fail to see Hanekawa because he thinks badly of her. He fails because he thinks impossibly well of her.**

### Rescue
> **V07's cleanest rescue lesson is that ending an oddity story and solving a person's life are different tasks.**

### Self-sacrifice
> **Araragi's early pathology is not simply courage. He converts intimacy into a desire to make his body the price of another person's survival.**

### Oshino
> **Oshino's expertise includes knowing when expertise cannot produce a clean cure. His “grey settlement” is a refusal to confuse classification with total understanding.**

### Oddity ontology
> **Black Hanekawa demonstrates that an oddity can be literally supernatural and simultaneously function as a narrative container for responsibility, memory, affect, and socially unspeakable human causation.**

### V07 full-volume thesis
> **『猫物語（黒）』 is the story of a girl who becomes so good at being unobtrusively correct that her unlivable feelings require another body—and of the people around her learning, too late, that removing that body does not remove the life that made it necessary.**
