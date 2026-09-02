---
title: "Classroom of the Elite — Final Year 1 Reconciliation and Evidence Lock"
series: "Classroom of the Elite"
artifact_type: "final_reconciliation_evidence_lock"
checkpoint_id: "Y1-FINAL-LOCK"
sequence_alias: "Y1-CP04"
status: "canonical_checkpoint_passed"
source_boundary: "Y1V01–Y1V11.5 + Y1FF"
spoiler_boundary: "through First File only"
method: "COTE_Y1_ANALYTICAL_METHOD_V2.md"
architecture: "COTE_Multi_Document_Synthesis_Architecture_v1.md"
created_at: "2026-08-14"
updated_at: "2026-08-14"
---
# Final Year 1 Reconciliation / Evidence Lock
## `Y1-FINAL-LOCK`

# 0. Result

**PASS.**

The Year 1 source-reading layer is complete and the evidence boundary is now frozen through `Y1FF` / *First File*.

The lock contains:

- fourteen canonical Japanese numbered/decimal novel deep readings, `Y1V01–Y1V11.5`;
- one canonical *First File* mixed-paratext audit;
- **1,419 unique evidence records**;
- **283 exact-language Japanese terminology/passages**;
- final end-of-Year-1 character, relationship, institution/exam, class-polity, and longitudinal-claim snapshots;
- a reconciled source map through `Y1FF`;
- and an explicit source-authority boundary preventing later-year evidence from silently rewriting Year 1.

This lock does **not** freeze the specialist synthesis corpus. Its purpose is narrower and logically prior: it establishes the evidentiary state from which `COTE_Y1_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` and later Year 1 specialist documents may now be written without uncertainty about source ingestion or rolling-ledger state.

# 1. Why a final reconciliation was necessary

Checkpoint 03 froze the sequential corpus through Volume 10. Volume 11 was then added as a post-checkpoint rolling analysis, leaving the live ledgers at a V11 boundary. V11.5 and *First File* changed enough of the year-end architecture that simply appending their findings would have been methodologically inadequate.

Three different operations had to be distinguished.

First, **source validation**: do the new evidence locators actually resolve against the Japanese sources under the established locator grammar?

Second, **claim reconciliation**: do V11.5 and *First File* confirm, strengthen, weaken, correct, or leave unresolved the claims inherited from V1–V11?

Third, **boundary freezing**: what can responsibly be called the canonical Year 1 state without importing Year 2, Volume 0, *Second List*, or later knowledge?

The final lock performs all three.

# 2. Evidence arithmetic and locator integrity

The cumulative evidence arithmetic is exact:

| Boundary | New evidence | Cumulative evidence |
|---|---:|---:|
| CP03 through Y1V10 | 1,037 | 1,037 |
| Y1V11 | 149 | 1,186 |
| Y1V11.5 | 151 | 1,337 |
| Y1FF / *First File* | 82 | **1,419** |

The final ledger contains **1,419 unique IDs with no gaps or duplicate IDs inside the appended V11.5/First File ranges**.

## V11 revalidation

The final lock independently rechecked all 149 V11 evidence locators against the Japanese EPUB:

- **140 text locators**;
- **9 visual locators**;
- **149/149 valid**;
- **0 locator repairs required**.

The EPUB byte fingerprint remains:

`a067284074b9209c4712b41d05ce01da17c971bc6d7993afb07cd548524a0a9f`

The immutable V11 artifact's normalized-text fingerprint remains:

`bccbf87237aae9e75882de75209c4251ee971888a4e44f578993bf3f26326c4d`

## V11.5 validation

The final lock independently checked all 151 V11.5 evidence locators against the Japanese EPUB:

- **141 text locators**;
- **10 visual locators**;
- **151/151 valid**;
- **0 locator repairs required**.

The EPUB byte fingerprint is:

`c5078e3770b0a74b161070920d65a91c681d8d54905477d15434bb05f5848fde`

The immutable V11.5 normalized-text fingerprint is:

`03aa6792ac46c1d512bedc4a57f039a4028cb8cd1b11ea4a2e03c17a8dbf9cbc`

The only validation subtlety was structural rather than substantive: image-bearing `<p>` nodes count in the canonical paragraph address space even when they contain no text, while pure `<br>` spacer paragraphs do not. Once that established normalizer was applied, the apparent V11.5 edge cases resolved without changing a single canonical locator.

## First File validation tier

*First File* requires a different statement because its physical source is different. The guidebook is a 121.6 MB mixed fixed-layout EPUB whose documentary pages are overwhelmingly raster/image based. The final-lock runtime could not remount that binary through the connected-storage handoff path.

The lock therefore **does not pretend to have performed a fresh OCR reread**.

Instead it inherits the previously completed source audit:

- 82/82 locked `Y1FF` evidence records;
- 58 fixed-layout documentary records whose authoritative object is the page image;
- 24 XHTML bonus-fiction records with deterministic paragraph locators;
- 18 exact-language Japanese anchors;
- source SHA-256 `b0b95aea1a832f6492c6e6b40faf19a277a3c4435fef3fe0859947e6fe8a45b1`.

This is an inherited validated state, not a degraded inference. The provenance difference is explicitly recorded so that future work can distinguish **fresh final-lock revalidation** from **previously source-audited inherited validation**.

# 3. Source-authority reconciliation

The most important methodological decision is that V11.5 and *First File* are not allowed to answer the same questions in the same way.

## Japanese novel text

The Japanese novels remain the strongest Year 1 literary evidence for:

- event sequence;
- character interiority;
- dialogue and voice;
- causal ambiguity;
- narrative withholding;
- ethical contradiction;
- and development experienced over time.

## First File data and ratings

`FF-DATA` and `FF-RATING` are strong evidence for what the official guidebook records or retrospectively models. They do not become omniscient descriptions of total persons.

Ayanokōji's weak July ratings are the decisive example. They can be accurate as a record of the output he permitted while being profoundly incomplete about latent capacity. The correct inference is therefore not “measurement is false.” It is that **the object of measurement is narrower than the person**.

## First File editorial prose

`FF-EDITORIAL` is official retrospective framing. It may corroborate a reading, make an institutional interpretation visible, or compress a year-long development into a usable label. It may also remove uncertainty and causal texture that the novels deliberately preserve. It cannot silently supersede stronger scene-level evidence.

## First File fiction

`FF-FICTION` receives the strongest literary weight inside the guidebook because it supplies narrative experience and first-person interiority. Its Ayanokōji and Ichinose stories are therefore allowed to revise relationship and ordinary-life claims in ways that a rating table alone could not.

The final lock's governing source rule is:

> **Authority is question-relative. A source may be strong evidence for what was recorded without being strong evidence for what the person wholly is.**

# 4. Ayanokōji reconciliation — freedom separates into three questions

The through-V11 ledger was correct to identify a deep contradiction: Ayanokōji's liberation was becoming self-authored at the same moment he consciously chose Horikita's development as a personal project. V11.5 does not remove that contradiction. It makes it structurally clearer.

## 4.1 Ordinary life as positive self-authorship

V11.5 contains the strongest explicit statement in Year 1 that ordinary school life is not merely refuge by negation. Ayanokōji calls it the first goal he has set for himself. *First File* then shows the positive content of that goal:

- ordinary study and exercise can feel fulfilling;
- a phone conversation can be interesting even when it produces no strategic value;
- social leave-taking can matter because another person is reluctant to part;
- and he can simply want to see Kei.

The final lock therefore marks the ordinary-life thread **STRENGTHENED** and rejects the stronger hypothesis that adolescent desire is only performance or camouflage.

## 4.2 Developmental authorship as a self-chosen purpose

Manabu's legacy challenge activates a second form of self-authorship. Ayanokōji imagines developing students across the four classes and then observing or producing competition among developed people. He is excited by the idea and disturbed by his own excitement.

This is not a return to White Room obedience. Nobody assigns the project to him. It is precisely because it is freely wanted that the ethical problem becomes harder.

The final lock therefore refuses the equation:

`self-chosen = ethically legitimate`.

## 4.3 Reciprocal authorship as the unresolved constraint

Year 1 supplies several countermodels to unilateral development:

- Horikita is given the Kushida problem even though Ayanokōji would solve it differently;
- Keisei articulates support plus dissent;
- Manabu refuses to give Suzune a self she must copy;
- Hiyori can correct Ryūen;
- Ichinose can accept help without becoming an ally;
- Kei has to answer the confession herself.

The resulting question is not whether Ayanokōji can make people grow. He demonstrably can.

It is whether he can allow growth to produce **ends he did not choose and persons his model did not predict**.

*First File* makes the epistemic side of this problem explicit: a file or model can be useful and still incomplete. Superior psychological prediction is not proof of total person-knowledge.

# 5. Horikita reconciliation — from independence to integrated self-authorship

The V11 ledger described Horikita as independently capable while Ayanokōji made her development his private project. V11.5 supplies the correction needed to make “independence” precise.

The mirror prologue rejects the notion that liberation means stripping away every trace of Manabu. Horikita calls the imitative self a `偽者`, but immediately acknowledges the years lived in that form as `紛れもない私`. This is not a contradiction in the text. It is the point.

She can reject the purpose that organized an earlier self without declaring the self historically unreal.

The final lock therefore replaces a purification model with an **integration model**:

> influence becomes material for self-authorship rather than evidence against self-authorship.

This also changes how leadership should be read. Horikita's mature value is increasingly not possession of the best static model of every classmate. It is her capacity to:

- gather better information;
- delegate to domain experts;
- revise her judgment;
- allow others to contradict her;
- publicly own consequential decisions;
- and work with a class whose ability portfolio changes over time.

*First File*'s July cooperation E is therefore retained as a meaningful historical observation and rejected as a timeless identity. The metric becomes evidence of development precisely because the person can outgrow the state it records.

# 6. Kei reconciliation — reciprocal romance inside a hidden curriculum

The final lock treats Ayanokōji–Kei as one of the places where binary interpretations are least adequate.

The romance is **not merely simulated**. V11.5 contains an explicit confession from Ayanokōji and an explicit affirmative answer from Kei. The relationship is not created by assigning her a role without response. *First File* further adds direct present-tense desire and enjoyment of interaction that produces no strategic return.

At the same time, Year 1 does **not** prove completed conventional love or stable irreplaceability. The interior narration retains:

- `教科書`;
- learning-language;
- a dependency-cure purpose;
- a future-oriented hope that Kei will become `掛け替えのない存在`;
- and the closing `祈ろう`, which is aspiration rather than accomplished self-certainty.

The final lock therefore records:

> **explicit reciprocal romance + continuing developmental asymmetry + unresolved irreplaceability.**

This formulation supersedes both “Kei is only a tool” and “the confession completes Ayanokōji's humanization.”

# 7. Ichinose reconciliation — future horizon without surrender of class agency

V11.5 and *First File* together force a similarly nonbinary reading of Ichinose.

Ayanokōji gives her a one-year meeting horizon and occupies a position she can call trustworthy despite class rivalry. That is real future-oriented care. Yet his interior `介錯` language means he still conceptualizes himself as a possible terminal judge if her trajectory collapses.

The *First File* bonus story adds Ichinose's side. Ayanokōji is a `大切な友達`, then something she cannot finish naming. The feeling restores warmth and fighting will. But she also explicitly remembers that their classes are rivals and returns herself to `新しい戦いが始まる`.

The final lock therefore rejects the interpretation that romance or attachment simply absorbs Ichinose's political identity. Her class agency remains active.

Her polity problem is correspondingly refined: solidarity is real capacity, while adversarial resilience and conversion of social capacity into results remain underdeveloped.

# 8. Ryūen, Sakayanagi, and the alternative polities

## Ryūen

The through-V11 distinction between legitimacy and ethics is retained. Followers increasingly choose him after fear ceases to be the sole basis of obedience. This increases sociological legitimacy. It does not prove moral reform. `勝つための悪逆` and willingness to use coercive or harmful tactics remain local evidence.

*First File* adds the structural diagnosis: the class is highly coordinated but overdependent on Ryūen and weak in distributed individual development.

## Sakayanagi

The final lock rejects a simple “strongest polity” reading. Her order possesses deep talent and sophisticated role allocation, but strategic knowledge is centralized. Personal rivalry can therefore impose costs on classmates who do not author the sovereign's private priorities. High informational competence creates both strength and fiduciary risk.

## Four-class comparison

The year-end point table is retained as institutional outcome data, not total merit:

- Sakayanagi polity: 1131;
- Ichinose polity: 550;
- Ryūen polity: 508;
- Horikita polity: 347.

The numerical order does not erase the constitutional differences that produced it.

# 9. `実力` reconciliation — from ability to the file/person distinction

The final Year 1 `実力` model is not a rejection of measurement. It is a decomposition of what measurement can mean.

By the boundary, the series has forced at least six stages apart:

1. **possession** — capacity a person actually has;
2. **development** — capacity that can change under environment and effort;
3. **expression** — what the person chooses or manages to display;
4. **legibility** — what an observer or metric can recognize from that display;
5. **coordination** — what a group can make usable with other capacities;
6. **recording** — what the institution officially preserves as the result.

Kōenji shows possession without reliable collective coordination. Horikita shows development and increasingly generative coordination. Ayanokōji shows deliberate suppression of expression and therefore distorted legibility. Tsukishiro shows that honest expression and recognition can still fail at the record layer. *First File* shows that a standardized file can be perfectly usable within its bounded purpose and still fail as a total theory of a person.

The locked formulation is:

> **`実力` is not merely what a person can do. It is what can be developed, expressed, recognized, coordinated, and preserved as a truthful result—while every measurement remains a model rather than the person in full.**

# 10. Institution reconciliation — ANHS is not one actor

The earlier institutional ledger correctly identified administrative procedural sovereignty. V11.5 adds a needed correction: ANHS cannot be treated as a monolithic will.

Ayanokōji seeks help through Chairman Sakayanagi, Mashima, and Chabashira precisely because one part of the institution may serve as a check on another. Tsukishiro's presence is described as contamination of a field that should otherwise be decided by student ability. Whether that ideal was ever fully realized is a separate question; the important point is that institutional integrity has internal advocates.

This creates a more constitutional reading of the school:

- exams author environments;
- teachers and councils mediate implementation;
- administrators may capture procedures;
- and other adults may attempt oversight.

The final institution question is therefore not merely “is ANHS good or bad?” It is:

> **Which institutional arrangements make consequential judgments contestable, correctable, and honestly recorded?**

# 11. White Room epistemic lock

The final Year 1 boundary contains more White Room material than the early volumes, but it still does not justify importing later retrospective certainty.

Directly established Year 1 material includes:

- Atsuomi's ownership claim;
- Ayanokōji's resistance to it;
- Sakayanagi's childhood encounter with the project;
- broad manufactured-genius/elimination framing;
- Ayanokōji's current expectation of future return;
- and Tsukishiro's detailed testimony.

The final item remains testimony where the volume itself leaves verification open. *First File* can strengthen broad official framing without turning every fine-grained Tsukishiro statement into omniscient fact.

The evidence lock therefore preserves epistemic tiers rather than synthesizing all White Room claims into one settled chronology.

# 12. First File as retrospective archive — what it can and cannot revise

*First File* is unusually valuable precisely because it demonstrates the danger of reading paratext without a source hierarchy.

The same artifact contains:

- factual calendars and system records;
- dated ratings;
- an explicitly hypothetical OAA reconstruction;
- editorial character summaries;
- retrospective class-state judgments;
- visual archives;
- and new fiction.

A single “official” label cannot make those evidentiary forms identical.

The final lock therefore treats guidebook authority functionally:

- use calendars for chronology;
- use ratings for what the rating records;
- use editorial summaries for official retrospective framing;
- use hypothetical OAA for measurement theory, not back-projected institutional fact;
- use bonus fiction as narrative literary evidence.

This is also why the guidebook's final formal movement matters. After hundreds of pages of filing and classifying Year 1, it closes with experiences that exceed the file: an unnecessary conversation, a wish to see someone, difficulty ending a call, an unnamed feeling, a deliberate return to competitive responsibility.

The guidebook is therefore not anti-measurement. It is anti-reductionist when read as a whole.

# 13. Locked class-polity states

The four stable polities close Year 1 with distinct constitutional problems.

### `POLITY-HORIKITA`

Dynamic developmental pluralism. Its strength is growing capacity to aggregate heterogeneous people and revise leadership knowledge. Its vulnerabilities are incomplete cohesion, difficult autonomous actors, and hidden dependence on Ayanokōji's off-record sovereignty.

### `POLITY-RYUEN`

Centralized coercive coordination with increasing voluntary loyalty. Its strength is adversarial adaptability; its vulnerabilities are ethical coercion, leader dependence, and limited distributed development.

### `POLITY-ICHINOSE`

Trust-centered solidarity and collective capital. Its strength is voluntary cohesion; its vulnerabilities are adversarial security and result conversion.

### `POLITY-SAKAYANAGI-ORIGIN`

Aristocratic optimization through sophisticated centralized talent mapping. Its strength is allocation; its vulnerabilities are incomplete unity, succession dependence, and the political cost of sovereign private priorities.

Above all four remains administrative procedural sovereignty.

# 14. Final correction matrix

| Earlier/provisional proposition | Final Year 1 status | Locked formulation |
|---|---|---|
| Ayanokōji's ordinary self is only camouflage | REJECTED | ordinary life is a genuine self-chosen and intrinsically valued project alongside strategic concealment |
| Self-authorship equals ethical humanization | REJECTED | self-chosen purposes can remain coercive toward others; reciprocal authorship is a separate test |
| Horikita's liberation means becoming uninfluenced | REJECTED | self-authorship integrates formative influence rather than erasing it |
| Haircut = return to true self | REJECTED | V11.5 explicitly preserves the lived imitative years as `紛れもない私` |
| Kei is only a tool/textbook | REJECTED AS TOTAL EXPLANATION | explicit mutual romance and present desire coexist with hidden curriculum and dependency history |
| Kei is already permanently irreplaceable | UNRESOLVED | `掛け替えのない存在` is a hoped-for future condition |
| Ichinose's weakness is simply excessive kindness | CORRECTED | solidarity is real capacity; adversarial security and result conversion are distinct deficits |
| Ryūen's voluntary followers prove ethical reform | REJECTED | legitimacy increases while coercive ethics persist |
| Static ratings reveal total ability | REJECTED | ratings can accurately capture bounded visible output while missing latent, concealed, contextual, or developmental capacity |
| Cooperation score = moral goodness/loyalty | REJECTED | `協調性` is a bounded legibility dimension |
| OAA existed as Year 1 measurement infrastructure | REJECTED | *First File* labels its Year 1 reconstruction counterfactual: `もしもOAAがあったら` |
| All Tsukishiro White Room claims are settled fact | REJECTED | testimony remains tiered where independent Year 1 corroboration is absent |
| Class points directly rank total class merit | REJECTED | points are institutional outcomes produced by different constitutions and environments |
| Good development means the developer's plan succeeds | REJECTED | reciprocal authorship requires room for another person's purposes and unpredicted identity |

# 15. Development versus revelation — final Year 1 guardrail

The final lock preserves a distinction that the later series must not erase.

Some changes are **development**:

- Sudō's emotional regulation and contribution;
- Horikita's increasing relational/leadership competence;
- Hirata's movement after crisis;
- class constitutions responding to defeat;
- Ayanokōji gaining ordinary-life experience.

Other changes are primarily **revelation or improved legibility**:

- the reader learning more of Ayanokōji's concealed capacity;
- Matsushita revealing deliberate underperformance;
- Sakayanagi receiving evidence that changes her classification of Ayanokōji;
- guidebook files making earlier visible states easier to compare.

Many cases combine both. The specialist corpus must continue marking which operation is occurring rather than treating every later surprise as proof that the earlier person was fake.

# 16. No-later-year contamination audit

The final lock searches the new evidence layer and final snapshots for later-source evidence IDs. None are admitted.

The following remain outside the Year 1 evidentiary boundary:

- Year 2 numbered/decimal novels;
- Volume 0;
- *Second List*;
- Year 3;
- anime and manga adaptations;
- wikis and secondary summaries;
- later-franchise retrospective answers.

References to those materials may occur only as explicit exclusions or future-work labels, never as premises that settle Year 1 interpretation.

# 17. Final Year 1 progression

The reconciled source-reading progression is now locked as:

> **authored visibility → authored legibility → authored environment → authored dependency → counter-curriculum → controlled exposure → distributed integration under hidden contingency → sovereignty over futurity → negotiated indispensability → institutional authorship → authored reputation → manufactured disposability → developmental authorship under procedural capture → reciprocal authorship → the file and the person**

This sequence should not be mistaken for fifteen isolated themes. It describes the increasing scale of the same governing problem: **who gets to define what another person is, what capacities count, what development is for, and what happens when the model becomes authoritative enough to control the person's future?**

# 18. Locked Year 1 thesis for downstream synthesis

The final evidence lock does not force the specialist documents to reproduce one thesis verbatim, but it constrains what a responsible Year 1 synthesis must be able to explain.

The strongest boundary formulation is:

> **Year 1 examines developmental authorship: the power to make other people's capacities visible, usable, challenged, preserved, or transformed—and the recurring danger that the person or institution capable of cultivating another human being will mistake understanding for jurisdiction. By the end of the year, the problem becomes reciprocal and epistemic: self-authorship is insufficient unless other people retain authorship over themselves, and no rating, strategy, institutional record, or psychological model is entitled to become the whole person.**

That formulation preserves both sides of the series' attraction to competence. The books do not deny that people differ, that measurement can reveal real information, that leaders can make groups more capable, or that Ayanokōji often understands developmental mechanisms better than the people around him.

The critique enters at the transition from:

`I understand something true about you`

to:

`therefore I am entitled to decide what you should become`.

# 19. Artifacts superseded and artifacts preserved

The final lock creates `THROUGH_Y1` snapshots for current Year 1 reference. It does **not** overwrite the older through-V11 snapshots.

Preserved historical boundary:

- `COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1V11.md`
- `COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y1V11.md`
- `COTE_RELATIONSHIP_LEDGER_THROUGH_Y1V11.md`
- `COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y1V11.md`
- `COTE_CLASS_POLITY_LEDGER_THROUGH_Y1V11.md`
- `COTE_LONGITUDINAL_CLAIM_LEDGER_THROUGH_Y1V11.md`

Superseding current-state Year 1 snapshots:

- `COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1.md`
- `COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y1.md`
- `COTE_RELATIONSHIP_LEDGER_THROUGH_Y1.md`
- `COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y1.md`
- `COTE_CLASS_POLITY_LEDGER_THROUGH_Y1.md`
- `COTE_LONGITUDINAL_CLAIM_LEDGER_THROUGH_Y1.md`

Mutable retrieval/admin artifacts are updated to the final boundary:

- `COTE_Y1_12_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md`
- `COTE_Y1_13_JAPANESE_TERMINOLOGY_AND_PASSAGE_INDEX.md`
- `COTE_Y1_LONGITUDINAL_THREAD_REGISTRY.md`
- `COTE_Y1_SOURCE_MAP.json`
- `COTE_Y1_PROJECT_STATUS.md`

# 20. Gate decision

All three gates required before freezing `COTE_Y1_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` are now satisfied:

1. `COTE_Y1_V11_5_DEEP_READING.md` — complete;
2. `COTE_Y1_FIRST_FILE_PARATEXT_AUDIT.md` — complete;
3. final Year 1 reconciliation/evidence lock — **complete and passed**.

The next architecture-defined phase is therefore:

> **Revise and freeze `COTE_Y1_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` as the canonical Year 1 snapshot.**

Only after that freeze should the specialist corpus proceed to:

`COTE_Y1_02_AYANOKOJI_CHARACTER_PSYCHOLOGY_ETHICS_AND_VOICE.md`.
