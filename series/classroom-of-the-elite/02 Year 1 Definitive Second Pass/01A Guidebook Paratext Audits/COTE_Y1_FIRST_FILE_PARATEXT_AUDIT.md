---
title: "Classroom of the Elite — Year 1 First File Paratext Audit"
subtitle: "The file and the person: institutional legibility, retrospective compression, and the ordinary life that exceeds measurement"
series_jp: "ようこそ実力至上主義の教室へ"
series_en: "Classroom of the Elite"
project: "Manga and anime discussions"
artifact_type: "guidebook_paratext_audit"
canonical_filename: "COTE_Y1_FIRST_FILE_PARATEXT_AUDIT.md"
year_arc: 1
source_code: "Y1FF"
analysis_pass: 2
method: "COTE_Y1_ANALYTICAL_METHOD_V2.md"
method_version: "2.0"
architecture: "COTE_Multi_Document_Synthesis_Architecture_v1.md"
architecture_version: "1.0"
source_language: "ja"
source_format: "epub_fixed_layout_mixed"
source_filename: "Classroom of the Elite - Year 1 Official Guidebook - First File [Japanese].epub"
official_title: "ようこそ実力至上主義の教室へ １年生編公式ガイドブック First File (MF文庫J)"
creators:
  - "衣笠彰梧"
  - "トモセ シュンサク"
publisher: "株式会社ＫＡＤＯＫＡＷＡ"
publication_date: "2024-11-25"
source_sha256: "b0b95aea1a832f6492c6e6b40faf19a277a3c4435fef3fe0859947e6fe8a45b1"
source_size_bytes: 121638502
source_status: "verified_primary"
spine_items: 253
raster_resource_count: 247
exclusive_bonus_fiction_spines:
  - 246
  - 247
exclusive_bonus_fiction_paragraphs: 205
exclusive_bonus_fiction_characters: 5963
exclusive_bonus_fiction_sha256: "9c8b344233c003fc3de6eb4abeb28c412627ee37b1bd45c365e2da23702e60c1"
locator_scheme: "first-file-dual-locator-v1"
documentary_authority: "fixed-layout image resource; OCR is retrieval aid only and non-authoritative"
fiction_authority: "XHTML Japanese text with deterministic paragraph locators"
evidence_entries: 82
fixed_layout_documentary_entries: 58
bonus_fiction_entries: 24
japanese_anchor_entries: 18
analytical_reading_position: "after Y1V11.5; final Year 1 source before year-boundary specialist synthesis"
spoiler_boundary: "through First File only; no Year 2 novel, Volume 0, Second List, Year 3, adaptation, wiki, or later-franchise evidence imported"
cumulative_scope: "Y1V01–Y1V11.5 plus Y1FF"
status: "canonical_recovered_from_locked_source_audit"
created_at: "2026-08-14"
updated_at: "2026-08-14"
provenance_note: "This artifact is reconstructed from the previously source-audited and formally locked Y1FF source map, 82-entry evidence ledger, 18-entry Japanese terminology index, and Year 1 evidence-lock audit. The 121.6 MB First File EPUB was not remounted in the current runtime because the Drive connector transfer path cannot hand off that binary size. Documentary claims therefore reproduce already-verified image-primary locators rather than pretending to be a new OCR-based reread. Bonus-fiction claims reproduce already-verified XHTML paragraph locators."
---

# 『ようこそ実力至上主義の教室へ』
## Year 1 Official Guidebook — *First File*
### Second-Pass Paratext Audit
### The file and the person: institutional legibility, retrospective compression, and the ordinary life that exceeds measurement

# 0. Scope, provenance, and why this is not an ordinary volume deep reading

*First File* is not Volume 12. It is also not an omniscient answer key to Year 1.

It is a mixed official artifact composed of several different evidentiary forms: calendars, school-system explanation, dated character ratings, retrospective profile prose, class summaries, a hypothetical Year-1 OAA reconstruction, visual archives, volume-by-volume activity summaries, special editorial columns, a quiz, prospective bridge material, and two pieces of bonus fiction. Those forms do not possess equal authority and should not be read as though they were spoken by one all-knowing narrator.

The audit therefore begins with a source-hierarchy rule:

> **The Japanese novels remain the governing literary evidence for what happened, how characters experienced it, and what uncertainty the narrative preserved. *First File* may corroborate, compress, measure, classify, or retrospectively frame Year 1. It may not silently replace the novels' more granular evidence.**

A second rule follows from the EPUB's physical construction. The documentary portion is overwhelmingly fixed-layout and image based. The authoritative documentary object is therefore the page image itself. OCR may help find text, but OCR is not promoted into primary-source wording. The two final bonus-fiction spines are ordinary text-bearing XHTML and can be cited by deterministic paragraph locator.

The present runtime cannot remount the 121.6 MB EPUB because of the connected-storage transfer limit. This document therefore does **not** claim a fresh page-by-page OCR reread. It is a recovery of the already completed source audit from the locked primary-source map, the 82 verified `Y1FF` evidence records, the 18 verified Japanese anchors, and the formal Year 1 evidence-lock audit. The earlier audit resolved all 58 documentary entries to actual spine/XHTML/image resources and all 24 bonus-fiction entries to valid paragraph locators. Nothing here upgrades an unverified OCR string into fact.

That provenance limitation affects workflow, not the interpretive boundary. The recovered evidence layer is already source-audited and internally frozen. The task here is to restore its argument in a human-readable canonical artifact while retaining the original evidentiary distinctions.

## 0.1 The four First File evidence layers

This audit uses four source layers.

### `FF-DATA`

Institutional or documentary records: calendars, class-point positions, school-system descriptions, Protection Point mechanics, and other directly presented factual apparatus.

These are strong evidence for **what the guidebook records**. They are not necessarily evidence that the institution's categories exhaust the person being measured.

### `FF-RATING`

Dated ability tables and the explicitly hypothetical Year-1 OAA reconstruction.

These are particularly important because their limitation is part of their meaning. A rating measures a person through selected axes, at a selected time, from a selected institutional perspective. Ayanokōji's files show dramatically that accurate recording of visible performance can coexist with profound ignorance of underlying capacity.

### `FF-EDITORIAL`

Official retrospective prose: character summaries, relationship descriptions, class-state judgments, activity reports, special columns, bridge material, and quiz framing.

This layer is valuable as **official retrospective framing**, not as an omniscient literary narrator. It can confirm that a reading is officially foregrounded, but its compression may remove ambiguity, causal complexity, or ethical texture that matters in the novels.

### `FF-FICTION`

The two exclusive final stories.

These are narrative fiction and receive the strongest literary weight inside *First File*. They disclose first-person interiority and relational experience that the rating files cannot represent. Their placement at the end of the guidebook is formally important: after hundreds of pages of filing, measuring, summarizing, and remembering Year 1, the book closes by returning to people living ordinary time that is not reducible to those files.

# 1. Executive thesis — the file is real information, but the file is not the person

*First File* is most analytically useful when read not as a warehouse of trivia but as a paratext about **legibility**.

Across Year 1, Advanced Nurturing High School repeatedly converts students into records:

- entrance scores;
- class points;
- private points;
- exam rankings;
- praise and criticism votes;
- Protection Points;
- class placement;
- institutional decisions;
- and eventually increasingly formalized ability metrics.

Ayanokōji, meanwhile, repeatedly authors the information other people are permitted to see. Horikita learns that static evaluation can miss developmental trajectory. Ryūen turns fear into coordination. Ichinose converts trust into political capacity. Sakayanagi centralizes extraordinary talent. Kōenji demonstrates that enormous possessed ability can remain politically unavailable. Kei's social competence lives badly inside conventional academic metrics. Hiyori's quiet inference is almost comically misrepresented if a single formal `judgment` grade is treated as total judgment.

*First File* gathers those problems into literal files.

Its documentary pages say, in effect:

> Here is the student as an institution can record the student.

Its editorial pages say:

> Here is Year 1 as an official retrospective can make Year 1 easy to remember.

Its bonus fiction then says:

> Here are experiences that matter precisely because they are difficult to convert into a score, summary, or strategic result.

Ayanokōji enjoys an irrelevant phone conversation. He realizes that reciprocal reluctance to end a call is something he does not know how to communicate. He wants tomorrow to come because he wants to see Kei. Ichinose privately names Ayanokōji a precious friend, reaches toward a category she cannot complete, suppresses the feeling because their classes are rivals, and then deliberately returns herself to the class struggle.

Those are not anti-institutional facts in the sense that the school is incapable of observing behavior. They are anti-reductionist facts. A file can record the consequence. It cannot automatically possess the experience's meaning.

The guidebook therefore adds a final term to Year 1's progression:

> **development versus control → reciprocal authorship → the file and the person**

The governing Year 1 question is no longer only whether a capable person may shape another person's development. It becomes:

> **What happens when an institution, strategist, leader, or retrospective archive possesses a usable model of another human being and mistakes that model for the human being as such?**

# 2. First File as an archive: memory is itself a form of authorship

The guidebook's first major function is archival. Calendars reconstruct the year's event sequence. Class-point movement becomes visible as a timeline. The School Guide explains the institutional ideology and point systems. Character pages align faces, ability axes, concise biography, relationship diagrams, and retrospective prose. Later Activity Report pages convert each volume into a chronological story guide. The quiz converts recollection into a scored exercise.

This is not neutral formatting.

Any archive selects:

- what receives a field;
- what receives a number;
- what receives a caption;
- what becomes a named event;
- what becomes a relationship line;
- what becomes background;
- and what disappears because the archive has no convenient slot for it.

That makes *First File* a useful meta-object for a series obsessed with records and hidden authorship. The novels repeatedly ask who controls the operative version of reality. Volume 2 distinguishes event truth from evidentiary power. Volume 9 shows reputation being authored through rumor. Volume 11 shows Tsukishiro's ability to capture the official record. *First File* is benevolent rather than antagonistic, but formally it performs the same basic operation: it turns a messy year into a retrievable model.

The danger is not that the model is false. Much of it is extremely useful.

The danger is the inference:

> **recorded = complete**.

The guidebook itself repeatedly gives us reasons to reject that inference.

# 3. Calendars, points, and the institution's dream of total chronology

The annual calendars are the cleanest documentary layer. They stabilize event order and class-point movement. The year-end checkpoint records the four class positions at **1131 / 550 / 508 / 347** for Sakayanagi's, Ichinose's, Ryūen's, and Horikita's classes respectively.

These records matter because the novels intentionally make institutional state difficult to hold in memory. Students pass through exams, reversals, temporary alliances, rule changes, and interpersonal crises. A timeline provides a longitudinal spine.

But point totals are outcomes, not causal explanations.

The same final number can conceal radically different political constitutions:

- a class can be high because a central strategist allocates strong specialists efficiently;
- a class can preserve every member yet fail to convert solidarity into enough points;
- a class can coordinate through fear and still suffer from weak distributed development;
- a class can contain explosive ability while failing to aggregate it.

The guidebook's own class summaries make this distinction explicit enough that reading the point table as a pure merit ranking would contradict the rest of the book.

This is an important refinement of `実力至上主義`.

A class-point total is **an institutional result**. It is not a metaphysical quantity of human worth.

# 4. Ability evaluation — when an accurate file becomes a misleading person

The dated `能力評価 / ability evaluation` pages are among *First File*'s most useful and most dangerous materials.

They are useful because they provide a standardized cross-character snapshot. They are dangerous because standardization creates a visual rhetoric of commensurability. Once every student has the same axes, it becomes tempting to believe every meaningful difference has been translated onto those axes.

Ayanokōji is the decisive counterexample.

His July 1 profile records:

- academics: **C**;
- judgment: **C-**;
- cooperation: **D**;
- physical: **C-**;
- intelligence: **C-**.

The same page's editorial prose also recognizes that his mediocre academic evaluation follows from deliberately scoring fifty in every entrance-exam subject.

This means the guidebook does something conceptually sophisticated whether or not it intends the sophistication as theory:

> **It places the measurement and the reason the measurement is misleading on the same page.**

The institutional file can therefore be factually accurate about demonstrated output while radically incomplete about latent capacity.

Ayanokōji is not evidence that measurement is meaningless. He is evidence that measurement has an object more specific than readers often assume.

It measures something like:

> **capacity as made visible under a particular observation regime.**

This was already one of Year 1's recurring insights. *First File* turns it into graphic form.

## 4.1 Cooperation is not morality

The axis `協調性 / cooperation` creates similar problems.

Kushida can rate very highly in cooperation while concealing behavior that severely threatens the class. Kōenji can rate catastrophically low in cooperation while possessing enormous academic and physical capacity. Kei's low formal profile cannot explain her ability to govern social atmosphere. Ichinose's high cooperation is politically meaningful but does not guarantee strategic victory.

So cooperation cannot simply mean:

- goodness;
- trustworthiness;
- loyalty;
- moral concern;
- or total collective usefulness.

It records a narrower form of institutionally or socially visible coordination.

The metric can be useful precisely because the analysis refuses to ask it to answer questions it was not built to answer.

# 5. The July profiles as frozen visibility states

The compact profiles become especially illuminating when read as **frozen states of visible Year 1 identity** rather than timeless character sheets.

## 5.1 Horikita Suzune

Horikita's profile records:

- academics A;
- judgment B-;
- cooperation E;
- physical B+;
- intelligence A-.

The editorial prose treats her academic and athletic capacity as compatible with A-class quality while locating her original D placement in an inability to take other people adequately into account. It also retrospectively recognizes her growing understanding of the difference between solitude and being truly solitary.

This supports, rather than replaces, the Year 1 developmental reading.

Her problem was never simple lack of ability. It was the failure to convert exceptional individual capacity into relationally usable leadership. By V11.5, she can integrate formative influences without imitating them, end an alliance, demand an auditable comparison with Ayanokōji, and accept jurisdiction over a Kushida problem whose efficient answer Ayanokōji would still make differently.

The E cooperation rating is therefore historically meaningful. It is also obsolete as a total description by the year endpoint.

That obsolescence is development.

## 5.2 Kushida Kikyō

Kushida's profile records B academics, C+ judgment, A cooperation, B physical ability, and B- intelligence. The accompanying prose separates that extraordinary social cooperativeness from the middle-school conduct that contributed to D placement.

This is exactly why a single metric cannot morally classify her.

Kushida's ability to create trust, remember people, circulate socially, and connect otherwise separated classmates is real. So are her secrecy, vindictiveness, and capacity to weaponize intimacy.

The Year 1 problem is not that her cooperation score is fake. It is that **social capacity and prosocial intention are not identical variables**.

## 5.3 Sakura Airi

Sakura's profile records modest conventional metrics and low social visibility, while the editorial framing links the Shizuku identity to self-change and her later movement toward a peer group she desires.

That is consistent with the second-pass correction established in Volume 2: the performed identity should not be reduced to a false mask covering a single true self. It is an authored interface through which capacities unavailable in one context can become expressible in another.

The file can record low visible cooperation. It cannot by itself explain why visibility changes when the social environment becomes safer.

## 5.4 Karuizawa Kei

Kei's July profile is strikingly weak on formal axes: D- academics, C- judgment, E+ cooperation, D physical, D- intelligence. Yet the guidebook's prose identifies her public personality and boyfriend strategy as adaptations to earlier trauma.

The apparent contradiction is productive.

A metric focused on academic and institutionally legible performance misses much of the capacity that made Kei strategically important in Volume 4:

- reading social atmosphere;
- commanding status inside the girls' hierarchy;
- maintaining a performed identity under pressure;
- information circulation;
- coalition behavior;
- and survival inside social threat.

Those capacities are not necessarily admirable. They are still abilities.

Kei therefore remains one of Year 1's strongest demonstrations that `実力` is ecological and relational. The environment decides which capacity becomes valuable.

## 5.5 Hirata Yōsuke

Hirata's profile is conventionally strong and the editorial layer calls him highly trusted and difficult to replace. Here the file and narrative largely agree.

But Volume 10 and Volume 11 complicate even this apparently easy case. A socially indispensable leader can become unavailable when his moral identity collapses under an expulsion system. His high cooperation is not a mechanical resource the class can always activate.

The distinction is:

> **possessed capacity ≠ available capacity under every psychological condition.**

## 5.6 Kōenji Rokusuke

Kōenji's compact profile—A academics, C judgment, E- cooperation, A physical ability, C intelligence—is almost a diagram of Year 1's anti-scalar merit argument.

He can possess enormous capacity and remain politically unusable because he rejects the collective's claim to that capacity.

This is not merely a defect in Kōenji. It is a constitutional question for the class:

> By what authority does a group claim the labor of a member who does not recognize its purposes as his own?

His file captures the tension unusually well because the high and low axes coexist without yielding a simple answer to whether he is “good.”

## 5.7 Sudō Ken

Sudō's profile—E academics, D+ judgment, D cooperation, A physical, E intelligence—preserves the early institutional visibility that made him look disposable to Horikita.

But Year 1 repeatedly demonstrates why that snapshot is inadequate as a developmental verdict. His athletic ability becomes class value. He accepts coaching. He learns collective consequence. Horikita's recognition becomes a reason to redirect effort. By the end of the year, his trajectory matters more than the original static category.

The file is historically useful because it shows what development had to overcome.

# 6. Ayanokōji's file — authored visibility as a life strategy

Ayanokōji's pages deserve separate treatment because the relation between person and file is not merely accidental in his case.

He **authors the file**.

The entrance-exam fifties are the obvious example. Across Year 1 he also controls swim time, physical visibility, causal attribution, public credit, strategic participation, and the amount of information particular observers receive about his ability. His file is therefore partly an institutional measurement and partly a product of his environmental authorship.

This changes the interpretation of institutional ignorance.

The school is not simply incompetent because it fails to know him. It is operating against a subject who understands observation and actively shapes the observable surface.

That makes *First File* an unusually fitting paratext for Ayanokōji. A dossier about him necessarily becomes a dossier about the limits of dossiers.

## 6.1 The “merciless for final victory” shorthand

The profile retrospectively describes him as merciless when final victory is at stake. This is supported by real Year 1 evidence, especially his explicitly marked strategic logic around using people as tools and ensuring that he wins in the end.

But the editorial label should not overwrite contrary evidence:

- he often prefers lower-coercion methods when he believes they will work;
- he can protect privacy;
- he can preserve refusal;
- he can intervene because he wants friends to remain;
- he experiences ordinary pleasure without strategic function;
- and he increasingly chooses developmental projects for reasons that cannot be reduced to a single victory condition.

The correct status is therefore **official compression of a real tendency**, not complete personality definition.

## 6.2 White Room framing

The guidebook officially frames Atsuomi as the operator of the White Room and Ayanokōji as the surviving fourth-generation highest masterpiece.

At the Year 1 boundary this counts as meaningful retrospective corroboration of the broad structure. It does not license importing later granular White Room history backward into Year 1.

The source-tier distinction remains:

1. what Year 1 novels directly establish;
2. what adversarial speakers such as Tsukishiro claim;
3. what *First File* officially frames;
4. what later primary fiction may eventually establish.

The guidebook strengthens the broad father/artificial-development/fourth-generation/masterpiece structure. It does not make every hostile or prospective detail automatically true.

# 7. Ryūen and Hiyori — the same file can reveal dictatorship and measurement failure

## 7.1 Ryūen Kakeru

Ryūen's July rating gives him D academics, A judgment, E- cooperation, B physical ability, and B intelligence. His profile combines overwhelming leadership with a form of class-directed obligation behind his violence. The background page foregrounds childhood violence, absence of fear, transactional cooperation, and outcome-oriented methods. The relationship page emphasizes utility-based cross-class contacts and his post-defeat plan to challenge other leaders.

The year-end class summary is more analytically valuable than any single number:

> Ryūen's class can coordinate powerfully under dictatorship, but the structure is overdependent on Ryūen and underdevelops individual autonomy.

This strongly supports the polity ledger's diagnosis.

It also preserves an important moral distinction. Increased voluntary loyalty after Ryūen's defeat can make his rule **more legitimate sociologically** without proving moral reform. Followers can choose a violent leader because they judge him effective, protective, exciting, or preferable to alternatives. Voluntary support changes the authority structure; it does not retroactively cleanse coercion.

## 7.2 Shiina Hiyori

Hiyori's page is one of the best internal demonstrations that a rating category should not be read too literally.

Her compact rating gives:

- academics A-;
- judgment E;
- cooperation D;
- physical E;
- intelligence A-.

Yet the same page's prose describes perceptive inference, quick thinking, and willingness to make harsh class-protective judgments.

This is not a reason to discard the `judgment E` data. It is a reason to ask **what that rating operationalizes**.

If “judgment” were total practical intelligence, the page would contradict itself. The better interpretation is that the metric captures a narrower standardized dimension that can diverge from:

- situational inference;
- literary/social perception;
- moral resolve;
- strategic restraint;
- or context-specific decision quality.

*First File* thus contains its own warning against naïve psychometrics.

# 8. Ichinose Honami — solidarity as capacity, not naïveté

Ichinose's profile is conventionally impressive: B+ academics, B judgment, A- cooperation, C physical, A intelligence. The editorial material highlights pooled private-point management as contingency infrastructure and identifies excessive consideration for others as a possible liability.

The class summary is more precise:

- high cohesion;
- pooled resources;
- no expulsions;
- but insufficient conversion of those advantages into competitive results.

This matters because “Ichinose is too nice” is analytically weak.

Her class has built something real and difficult:

- trust sufficient for collective saving;
- a reputation that facilitates cooperation;
- strong internal protection;
- and a constitution capable of carrying all members through the first year.

The failure is not absence of political capacity. It is **insufficient adversarial architecture and insufficient conversion of solidarity into upside**.

That distinction preserves the value of trust while allowing strong criticism of strategy.

The bonus fiction later makes the same point psychologically. Ichinose can trust her classmates and still withhold some uncertainty because she does not want to burden them. She can blame herself without that self-blame becoming omniscient causal truth. She can be emotionally affected by Ayanokōji and still consciously return priority to the class struggle.

Her softness and agency are not mutually exclusive.

# 9. Sakayanagi Arisu — elite allocation and succession risk

Sakayanagi's July rating gives A academics, A judgment, C+ cooperation, E- physical ability, and A intelligence. The prose explicitly treats physical disability as a competitive handicap while recognizing her leadership.

The class summary is the more important political artifact. It describes a class with:

- deep talent;
- effective role allocation;
- centralized strategic intelligence;
- and incomplete unity because strategy remains heavily monopolized.

That is almost a constitutional diagnosis.

Sakayanagi's system is highly efficient when the sovereign is present. The cost is that other members have less incentive or opportunity to develop independent strategic authorship.

At the Year 1 boundary, this remains a **risk**, not a later-outcome claim. The audit must not use subsequent events to prove the prediction. What *First File* supports is narrower:

> The class's strength is real, and its centralization is real.

That is enough to identify succession as an open structural question.

# 10. The four class summaries — four theories of political organization

Read together, the class pages are among the strongest parts of *First File* because they corroborate the second pass's decision to treat the four classes as **political constitutions**, not merely teams with different power levels.

## 10.1 Horikita polity — developmental pluralism under an aggregation problem

The class contains distinctive students with explosive potential but inadequate cohesion. Leadership must aggregate individualists.

This is the Year 1 Horikita problem in compact form.

Her mature role is increasingly not “be the strongest person” but:

- identify heterogeneous capacities;
- persuade people to participate;
- allocate roles;
- tolerate disagreement;
- and create conditions under which abilities the leader does not possess become collectively usable.

## 10.2 Ryūen polity — coercive coordination with weak distributed development

Ryūen solves coordination through centralized force and fear. That creates decisive action but makes too much of the class dependent on one strategic center.

The class's political question is whether loyalty can become more voluntary and whether followers can become authors rather than only instruments.

## 10.3 Ichinose polity — solidarity with low strategic conversion

Ichinose's class protects membership and builds trust infrastructure exceptionally well. Its weakness is not cohesion but insufficient conversion of cohesion into competitive gain.

The open question is whether adversarial competence can be added **without destroying the norms that make the class worth preserving**.

## 10.4 Sakayanagi polity — aristocratic optimization with centralized authorship

Sakayanagi's class has the deepest conventional talent pool and a leader capable of unusually precise allocation. Its vulnerability is concentration of strategic authorship.

The question is not whether centralized excellence works. It clearly does.

The question is what the polity can become if leadership must be reproduced rather than merely obeyed.

## 10.5 Why these are not four personality stereotypes

The value of the class summaries is structural. They discourage reducing the leaders to:

- Horikita = cold;
- Ryūen = violent;
- Ichinose = nice;
- Sakayanagi = genius.

The relevant differences are institutional:

- how information moves;
- who may decide;
- how members are developed;
- how dissent is handled;
- whether trust is horizontal or vertical;
- whether ability is generated or merely allocated;
- and how much a class can survive the temporary unavailability of its leader.

# 11. “If OAA had existed” — hypothetical measurement and the rhetoric of false precision

The OAA reconstruction is one of the most important paratextual objects in the guidebook because the heading itself marks the exercise as counterfactual: `もしもOAAがあったら`—**if OAA had existed**.

The ratings reconstruct what the later OAA framework might have displayed around the start of the first-year second term. They are therefore not hidden true stats finally revealed by an omniscient authorial database. They are a retrospective simulation of institutional legibility.

Selected figures are:

| Character | Academics | Physical | Adaptive/quick thinking | Social contribution | Overall |
|---|---:|---:|---:|---:|---:|
| Ayanokōji | 50 | 45 | 31 | 27 | 40 |
| Horikita | 89 | 79 | 57 | 34 | 69 |
| Kei | 33 | 44 | 46 | 22 | 38 |
| Ryūen | 42 | 69 | 76 | 1 | 54 |
| Hiyori | 82 | 29 | 23 | 44 | 45 |
| Ichinose | 81 | 53 | 84 | 84 | 74 |
| Sakayanagi | 93 | 24 | 71 | 55 | 62 |

These numbers are valuable because they show what the chosen system would reward and punish.

They should be read as **measurement outputs**, not as metaphysical truth.

## 11.1 Ayanokōji's 40 is not an error

It is tempting to laugh at Ayanokōji's overall 40 as proof that OAA is useless.

That misses the point.

If he has deliberately produced mediocre visible outputs, then a system built from visible outputs should rate him as mediocre. The number accurately represents **the institutional subject he has authored for observation**.

The deeper question is not:

> Why is the number wrong?

It is:

> **What kind of truth is the number true about?**

For Ayanokōji, it is true about demonstrated visibility, not total capacity.

## 11.2 Ryūen's social contribution of 1

A social-contribution score of 1 alongside high adaptive ability is similarly illuminating. Ryūen can generate collective results through methods the institution's prosocial metric regards as nearly maximally deficient.

Effectiveness and socially approved contribution are distinct dimensions.

## 11.3 Ichinose's 84/84

Ichinose's very high adaptability and social contribution fit the class's extraordinary cohesion. Yet her class can still lose competitive ground.

Again:

> high individual or social metrics do not mechanically generate institutional victory.

## 11.4 Sakayanagi and disability

Sakayanagi's low physical score visibly depresses the overall aggregate despite elite academic and strategic values. This is a useful warning about composite scores. An aggregate can accurately incorporate a real competitive limitation while still creating a misleading impression if readers interpret the aggregate as total human capability.

## 11.5 Hiyori as internal counterexample

Hiyori's low adaptive score is especially difficult to reconcile with the guidebook's own prose if adaptability is treated as total quick-wittedness. The contradiction forces a narrower reading of the metric.

The metric does not fail because it has boundaries.

It fails only when its user forgets those boundaries.

# 12. Editorial compression — useful maps that erase the road

The Activity Report turns each volume into a chronological sequence with explanatory prose. This is excellent for retrieval. It is also an example of **retrospective causal smoothing**.

A novel allows uncertainty to persist across hundreds of pages. It can withhold motive, distribute causation, stage mistaken interpretation, and let a character act without knowing what another character knows. A one-page activity summary must choose what to foreground.

That means the summary often converts:

- ambiguous development into named development;
- distributed causation into a primary actor;
- unresolved relationship texture into a relationship label;
- and temporally experienced mystery into retrospective clarity.

The correct use is therefore:

> **navigation and framing, followed by return to the novel for difficult claims.**

The incorrect use is:

> **guidebook sentence overrides novel evidence because it is shorter and official.**

## 12.1 Horikita's V11.5 framing

The V11.5 activity summary explicitly foregrounds Horikita's pursuit of growth, desire to verify Ayanokōji's ability, and movement toward an independent path.

This strongly supports the second-pass endpoint.

But “independent” should still mean **increasing self-authorship through integration**, not purification of Manabu's or Ayanokōji's influence. The novel itself gives the more precise model.

## 12.2 Ayanokōji–Kei framing

The V11.5 summary frames Ayanokōji as entering romance with Kei to learn love. The special `人心掌握術` column further compresses their history into a language of psychological capture and management.

Both descriptions identify something real.

Neither is sufficient by itself.

The novels preserve at least four simultaneous facts:

1. the relationship originates inside nonconsensually authored danger and protection;
2. Ayanokōji repeatedly conceptualizes Kei developmentally and instrumentally;
3. Kei exercises meaningful choice inside and after that structure;
4. by the end of Year 1, ordinary reciprocal desire exists that cannot be reduced to pure strategic function.

The bonus fiction is crucial because it supplies the fourth point in unusually direct form.

# 13. `人心掌握術` — mastery language and the ethics of shorthand

The phrase `人心掌握術` can be rendered approximately as a technique/art of grasping, winning, or controlling people's hearts.

As a guidebook header, it is effective. It tells the reader that Ayanokōji possesses exceptional capacity to understand and move people.

As ethical analysis, it is too compressed.

The phrase can collapse together very different operations:

- noticing another person's needs;
- building trust;
- withholding information;
- creating dependency;
- coercing behavior;
- giving someone space to decide;
- engineering a crisis;
- offering protection;
- teaching;
- and developing affection.

Year 1's ethical project depends on **not** collapsing those operations.

That is why this audit treats `人心掌握術` as a useful official retrospective category and simultaneously as evidence of how paratext can simplify morally heterogeneous behavior into a single competence.

The phrase is itself an example of the file/person problem.

# 14. Protection Point, points, and quantified rights to remain

The guidebook restates the Protection Point as a nontransferable one-use resource capable of canceling an expulsion.

This matters beyond mechanics.

Year 1 repeatedly monetizes or quantifies continuation:

- private points can purchase examination intervention;
- enormous private-point wealth can buy class transfer;
- class points determine collective hierarchy;
- praise votes can generate a Protection Point;
- and the Protection Point can preserve a person whom the institution would otherwise remove.

The school therefore does not merely measure ability. It builds a political economy in which **the right to continue developing can become contingent upon scarce institutional resources**.

*First File*'s system summaries make those mechanics easy to see in one place. They should feed later `Y1_06` and `Y1_08` analysis, but the full ethical argument belongs there rather than in this source-local audit.

# 15. White Room bridge material — prospective framing is not retrospective omniscience

The Year-2 bridge reiterates White Room generation structure and identifies a White Room student as an approaching threat.

Inside the Year 1 boundary this is **prospective First File framing**.

The audit must not use Year 2 novels to confirm or elaborate it.

This source-boundary rule is especially important because *First File* was published after readers could in reality know later material. The analytical project deliberately asks a different question:

> What can the Year 1 corpus plus its official retrospective guidebook responsibly establish without importing the later narrative?

The answer is:

- broad White Room structure is strengthened;
- a prospective threat is officially framed;
- the finer content of Tsukishiro's testimony remains source-tiered;
- later identity, motive, institutional history, and outcome remain outside this document.

# 16. Visual archive — private bodies inside an institutional file

The casual-clothes archive re-presents selected off-duty illustrations as a curated visual collection. One page foregrounds characters including Ichinose, Ryūen, Sakayanagi, Kei, and Hiyori.

This is easy to dismiss as fan-service compilation, but formally it matters.

The guidebook repeatedly presents students as:

- files;
- ratings;
- diagrams;
- leaders;
- class resources;
- and historical actors.

The casual-clothes section interrupts that institutional grammar with private embodiment.

Clothes chosen outside school uniform make individuality visually available through:

- taste;
- comfort;
- self-presentation;
- gendered styling;
- social context;
- and ordinary leisure.

The archive therefore participates in the same dialectic as the bonus fiction:

> **The school can standardize the uniform and the metric; the paratext also preserves the student outside the standardized role.**

This should not be overstated into a grand authorial manifesto. But it is a meaningful formal contrast inside a guidebook whose title is literally *First File*.

# 17. Bonus fiction I — Ayanokōji and Kei after the confession

The first bonus story is the strongest reason *First File* cannot be treated merely as reference material.

It returns to Ayanokōji after V11.5 and gives him a problem with almost no strategic importance:

> how to talk to his girlfriend on the phone like an ordinary teenager.

That smallness is the point.

## 17.1 `学生らしい生活`

Ayanokōji says he spends his days at the school in order to live a `学生らしい生活`—a student-like life. He describes ordinary study and exercise as the kind of daily life through which he can feel `一番充実感を味わえる`—the greatest sense of fulfillment.

This significantly strengthens the V11.5 claim that ordinary life is not merely camouflage or passive refuge.

He is not saying:

> ordinary life is useful because it helps me hide.

He is saying, at this local boundary:

> ordinary life itself is fulfilling.

That is self-authored value.

## 17.2 Romance as chosen non-optimization

The story states that Ayanokōji deliberately avoids overanalyzing some of his emerging romantic behavior and chooses to `恋愛という世界に身を任せる`—entrust himself to the world of romance.

For this protagonist, not optimizing is an action.

Year 1 repeatedly shows him reducing uncertainty by controlling information, timing, environment, and alternatives. Here he accepts uncertainty because the uncertainty is part of the experience he wants to learn.

This is not proof that he has abandoned control as a general method.

It is evidence that **he can locally choose not to exercise all available control**.

That distinction is ethically important.

## 17.3 `使う者と使われる者`

The story explicitly looks back on Ayanokōji and Kei as `使う者と使われる者`—the one who uses and the one who is used—before contrasting that older structure with their present reciprocal contact.

This is unusually strong retrospective textual evidence because it does not require the analyst to invent the instrumental origin.

But the contrast is not:

> use was fake, love is now pure.

The better reading is developmental:

> a relationship with a coercive/instrumental origin has acquired forms of reciprocity that the origin did not guarantee.

The origin remains morally relevant. The later reciprocity is also real.

## 17.4 Strategically irrelevant conversation becomes intrinsically interesting

Ayanokōji finds a conversation interesting even though it yields no strategically relevant information.

This is small but conceptually major.

Much of his Year 1 social intelligence is extractive or diagnostic. Conversation produces:

- information;
- leverage;
- psychological models;
- coalition access;
- or predictions.

The bonus story gives him conversation as **shared time whose value lies in being shared**.

That is ordinary-life counter-curriculum in its purest form.

## 17.5 He is bad at this

The story refuses wish fulfillment in which genius automatically becomes a perfect boyfriend.

Ayanokōji ends the first call too cleanly. Kei had expected reciprocal reluctance to separate. He has to learn that `名残惜しい`—being sorry to part—is not merely an internal state but something communicated through timing, hesitation, and conversational convention.

This is a beautiful inversion of his ordinary competence.

He can model complicated strategic environments.

He cannot intuit a mundane social ritual that many adolescents learn without formal analysis.

The White Room's deprivation becomes visible not through a dramatic flashback but through a failed phone call.

## 17.6 `オレは早く恵に会いたい`

The strongest line is simple: `オレは早く恵に会いたい`—he wants to see Kei soon.

This should neither be minimized nor inflated.

It is strong evidence of **present-tense personal desire**.

It strongly weakens an instrument-only interpretation in which Kei matters only because she is useful for Ayanokōji's education.

It does **not** prove:

- permanent love;
- lifelong singularity;
- future fidelity;
- ethical equality;
- or completed `掛け替えのない存在` status.

Present desire is real. Permanent irreplaceability remains unresolved.

## 17.7 Kei still makes relational decisions

Kei decides that the relationship will remain secret a little longer.

That matters because it prevents the romance from being described as an entirely unilateral curriculum authored by Ayanokōji. Information asymmetry remains substantial, but Kei is still a participant who can decide the public status of the relationship.

The year-end question is therefore not whether she has zero agency.

It is how much **reciprocal agency** can grow inside a relationship whose origin and information structure were profoundly unequal.

## 17.8 Peace and rapids

Ayanokōji still wants peaceful days, but he now recognizes unpredictable rapids as part of what makes school life interesting.

This completes a progression that began much earlier. Ordinary life no longer means perfect absence of disruption.

A life can remain ordinary while containing:

- difficult relationships;
- competition;
- mistakes;
- embarrassment;
- uncertainty;
- and events he did not fully design.

That is a richer freedom than simple escape from the White Room.

# 18. Bonus fiction II — Ichinose and the feeling she cannot classify

The second bonus story provides an important counterpoint to the first.

Ayanokōji's story concerns a newly named romance and his inability to perform its ordinary conventions smoothly.

Ichinose's story concerns a relationship she **cannot yet name** and her decision to subordinate that uncertainty to class responsibility.

## 18.1 Solitude as political reflection, not collapse

Ichinose reports spending much of spring break alone thinking through Year 2 and her class's future before returning to ordinary peer time.

This is not simple social withdrawal.

It is reflective processing.

The scene matters because Ichinose is often flattened into a person who only functions through collective warmth. The story gives her a private deliberative self capable of stepping away from the group without rejecting it.

## 18.2 Trust and concealment coexist

She genuinely trusts her classmates while hiding some uncertainty because she does not want to burden them.

That distinction matters.

Concealment does not automatically prove distrust.

It can also arise from:

- protective intent;
- leadership burden;
- embarrassment;
- unresolved self-knowledge;
- or fear of destabilizing others.

Whether such concealment is healthy is a separate question.

## 18.3 Self-blame is character evidence, not omniscient causation

Ichinose blames herself for the year-end defeat.

The audit preserves this as **interiority**, not a definitive causal verdict.

A leader's willingness to assume responsibility tells us something important about the leader. It does not automatically tell us that every failure was actually hers.

This distinction should carry into later leadership analysis.

## 18.4 `大切な友達` and the unfinished next category

Ichinose can call Ayanokōji `大切な友達`—a precious or important friend—and then reaches toward `とても、私にとって重要な……`—“very important to me…”—without completing the category.

The ellipsis is evidence.

The text does not need to name the feeling in order to show that the existing category is under strain.

This is an excellent example of why paratext ratings cannot substitute for narrative interiority. No relationship diagram or social-contribution score can adequately represent a person trying and failing to name a new relation.

## 18.5 Rival classes structure private feeling

Ichinose explicitly thinks of their classes as `競い合うライバルのクラス`—rival classes that compete with one another.

Her inability or unwillingness to indulge the feeling is therefore not only romantic hesitation. It is political.

Institutional structure enters intimacy.

If they were in the same class, she imagines the dilemma might disappear. The class system is thus not a background container around relationships. It helps constitute what relationships are permitted to mean.

## 18.6 Ayanokōji as restoration of will

Remembering Ayanokōji's earlier support produces intense warmth and is linked to recovering from `戦意喪失`—loss of will to fight.

This gives the relationship developmental significance without reducing Ichinose to dependency.

He helped restore a horizon.

She then chooses to return priority to her own class and `新しい戦いが始まる`—a new battle begins.

The final movement belongs to her.

# 19. The bonus stories as formal rebuttal to total legibility

The placement of the bonus fiction is analytically elegant.

Hundreds of pages establish:

- who is rated highly;
- who is rated poorly;
- how classes rank;
- what events occurred;
- how relationships can be summarized;
- what institutional categories describe students;
- and how the year can be remembered.

Then the guidebook closes with:

- a boy learning that enjoyable conversation can be useless;
- a girlfriend wanting him to hesitate before hanging up;
- desire for tomorrow because another person will be there;
- a girl sitting alone with a political and emotional problem she cannot name;
- trust that coexists with concealment;
- and feelings constrained by the arbitrary institutional fact of class membership.

The formal implication is not that measurement is evil.

It is:

> **The most humanly significant facts may be precisely those that do not become more true when converted into a metric.**

# 20. Retrospective correction matrix

The following matrix records what *First File* does to the mature Year 1 second-pass claims. These are not all new facts. Some are confirmations of conclusions already reached independently from the novels.

| Prior Year 1 claim | First File effect | Audit judgment |
|---|---|---|
| Ayanokōji's ordinary-life desire is mainly passive refuge from the White Room | Bonus fiction names student-like life as personally fulfilling and depicts desire for school to resume | **STRENGTHENED** |
| Ayanokōji remains capable of choosing non-optimization locally | He consciously lets himself enter romance without fully analyzing/controling every response | **STRENGTHENED** |
| Kei is only an instrument/protected collaborator at the Year 1 endpoint | Bonus fiction explicitly contrasts old user/used relation with reciprocal contact and gives direct desire to see her | **WEAKENED / CORRECTED** |
| Kei has already become permanently irreplaceable | Present desire is strong, but no evidence establishes permanent singularity | **UNRESOLVED** |
| Ayanokōji's humanization entails ethical reform | Ordinary fulfillment and reciprocity coexist with continuing developmental/informational sovereignty | **WEAKENED** |
| Horikita's independence means becoming free of Manabu/Ayanokōji influence | Official V11.5 framing supports independent path, while novel evidence shows integration of formative influence | **STRENGTHENED AS INTEGRATION; PURIFICATION REJECTED** |
| Static ratings reveal total ability | Ayanokōji and Hiyori demonstrate the limits of visible-output measurement; OAA exercise is explicitly hypothetical | **CORRECTED** |
| `協調性` can be read as goodness or loyalty | Kushida, Kōenji, Kei, and class-polity evidence separate cooperation from moral worth | **CORRECTED** |
| Ryūen's post-defeat follower loyalty proves moral reform | Guidebook supports leadership, obligation, and continued outcome-oriented violence, not moral conversion | **UNRESOLVED / WEAKENED** |
| Ichinose's central defect is naïve kindness | Class summary identifies strong cohesion/resource pooling/no expulsions but insufficient result conversion | **CORRECTED** |
| Hiyori's formal `judgment E` means poor practical judgment in general | The same profile describes strong inference and hard class-protective decisions | **CORRECTED** |
| Sakayanagi's polity is simply “the strongest class” | Guidebook highlights talent/allocation while also identifying strategy monopolization and incomplete unity | **RETROSPECTIVE RECONTEXTUALIZATION** |
| Horikita's class weakness is simply low ability | Guidebook describes explosive individual potential with aggregation/cohesion deficit | **STRENGTHENED** |
| White Room details in Tsukishiro's V11.5 testimony can all be treated as settled | Guidebook corroborates broad structure but does not erase testimony/source-tier distinctions | **PARTLY CONFIRMED; FINER CLAIMS UNRESOLVED** |
| Year 1 is a simple protagonist-humanization arc | Guidebook places institutional files against private experience and preserves Ayanokōji's authorship problem | **CORRECTED** |

# 21. What First File adds to the theory of `実力`

The guidebook permits a more precise Year 1 formulation of `実力`.

A person's ability cannot be reduced to a single hidden essence. Across the Year 1 corpus it depends on at least six stages:

1. **possession** — what capacities the person has;
2. **development** — what capacities can grow;
3. **expression** — what the environment permits the person to show;
4. **legibility** — what another actor or institution can recognize;
5. **coordination** — whether the capacity can become socially usable with others;
6. **recording** — whether the official outcome preserves what was actually expressed.

*First File* adds special force to stage four.

Its ratings are legibility machines.

They do not merely discover ability. They create an institutional object called “ability” by choosing dimensions and recording output.

That does not make them arbitrary.

A ruler measures real length while ignoring color. A scale measures real mass while ignoring intention. An OAA-like system can measure real outputs while ignoring hidden capacity, unwillingness to cooperate, trauma, future trajectory, private motivation, or deliberate deception.

The mature Year 1 proposition can therefore be stated:

> **`実力` is not merely what a person can do. It is what can be developed, expressed, recognized, coordinated, and preserved as a truthful result—while every measurement remains a model rather than the person in full.**

# 22. The file/person distinction and Ayanokōji's ethics

The paratext also clarifies why Ayanokōji's extraordinary psychological insight does not automatically justify his interventions.

Ayanokōji is himself a victim of reduction.

The White Room treats him as:

- outcome;
- masterpiece;
- proof of curriculum;
- asset;
- successor;
- and product of developmental design.

He rebels in part by insisting, however incompletely, on ordinary goals that the system did not assign.

Yet his own strategic method often constructs files of other people:

- needs;
- weaknesses;
- likely reactions;
- leverage points;
- developmental bottlenecks;
- useful roles;
- and future trajectories.

His models are often extraordinarily accurate.

The moral problem is not that he misunderstands everyone.

It is that **understanding can become a claim of jurisdiction**.

*First File* makes this contradiction formally visible because Ayanokōji's own official file is so obviously inadequate to him. The boy who exceeds his file is also the boy most tempted to treat other people's psychological files as actionable maps.

That produces the strongest version of the Year 1 ethical question:

> **Can Ayanokōji recognize that another person's model can be accurate enough to help while still being incomplete enough to forbid ownership?**

This is reciprocal authorship at the epistemic level.

# 23. The file/person distinction and Horikita's leadership

Horikita's development points toward a more accountable alternative.

Her early error is not lack of judgment. It is overconfidence in a narrow evaluative model:

- low score = low value;
- difficult student = disposable;
- current weakness = future weakness;
- leader knows what others should become.

Across Year 1 she learns to revise that model through contact with actual people.

By the end of the year, stronger leadership means:

- gathering information;
- accepting correction;
- distinguishing potential from current output;
- working with capacities she does not possess;
- allowing others to challenge her;
- and remaining publicly accountable for decisions.

The guidebook's July cooperation E becomes almost an archival photograph of the problem she spent the year learning to overcome.

Her mature value is therefore not that she finally possesses a perfect file on the class.

It is that she becomes **more correctable when the file is wrong**.

# 24. The file/person distinction and the class constitutions

The four classes can now be compared through their relationship to human legibility.

### Horikita

Needs increasingly accurate local knowledge of heterogeneous people so ability can be developed and coordinated. Risk: hidden Ayanokōji authorship can make the public constitution depend on information she does not possess.

### Ryūen

Builds highly actionable models of fear, desire, weakness, and incentives. Risk: treating accurate psychological models as authorization for coercion.

### Ichinose

Builds political order through trust and social transparency. Risk: norms optimized for reciprocal good faith can be exploited by actors who do not reciprocate.

### Sakayanagi

Builds a sophisticated centralized map of talent and assigns people to roles. Risk: the better the sovereign's model, the less the polity may need to develop independent model-builders.

The Year 1 political problem is thus not simply which leader is smartest.

It is:

> **What institutional arrangement best uses knowledge about people without converting knowledge into possession?**

# 25. Japanese anchor index — First File

These eighteen short anchors are the locked exact-language retrieval layer for `Y1FF`. Fixed-layout documentary anchors inherit image-primary authority; fiction anchors inherit XHTML paragraph authority.

| Japanese | Working translation | Locator | Analytical use |
|---|---|---|---|
| `能力評価` | ability evaluation | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | Dated standardized measurement; Ayanokōji shows visible performance can be deliberately authored. |
| `協調性` | cooperation | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | Metric axis that must not be conflated with morality or loyalty. |
| `もしもOAAがあったら` | if OAA had existed | `Y1FF|spine:84|text/part0083.html|image:00082.jpeg` | Explicitly counterfactual retrospective measurement. |
| `機転思考力` | adaptive / quick-thinking ability | `Y1FF|spine:84|text/part0083.html|image:00082.jpeg` | Chosen legibility dimension, not exhaustive practical judgment. |
| `社会貢献性` | social contribution | `Y1FF|spine:84|text/part0083.html|image:00082.jpeg` | Quantifies socially visible contribution. |
| `人心掌握術` | technique/art of winning or controlling hearts | `Y1FF|spine:240|text/part0239.html|image:00238.jpeg` | Official shorthand for Ayanokōji's people-management; ethically compressed. |
| `プロテクトポイント` | Protection Point | `Y1FF|spine:241|text/part0240.html|image:00239.jpeg` | One-use, nontransferable institutional protection from expulsion. |
| `学生らしい生活` | student-like life | `Y1FF|spine:246|text/part0245.html|p:0009` | Ayanokōji names ordinary student life as the purpose of his days at ANHS. |
| `一番充実感を味わえる` | gives the greatest sense of fulfillment | `Y1FF|spine:246|text/part0245.html|p:0010` | Ordinary study/exercise carries intrinsic fulfillment. |
| `恋愛という世界に身を任せる` | entrust myself to the world of romance | `Y1FF|spine:246|text/part0245.html|p:0046` | Chosen local non-optimization and experiential learning. |
| `使う者と使われる者` | the one who uses and the one who is used | `Y1FF|spine:246|text/part0245.html|p:0057` | Names the earlier instrumental Ayanokōji–Kei structure. |
| `名残惜しい` | reluctant to part | `Y1FF|spine:246|text/part0245.html|p:0151` | Mundane reciprocity Ayanokōji must learn to communicate. |
| `オレは早く恵に会いたい` | I want to see Kei soon | `Y1FF|spine:246|text/part0245.html|p:0157` | Direct present-tense desire; irreplaceability still unresolved. |
| `大切な友達` | precious / important friend | `Y1FF|spine:247|text/part0246.html|p:0013` | Ichinose's available relational category for Ayanokōji. |
| `とても、私にとって重要な……` | very important to me... | `Y1FF|spine:247|text/part0246.html|p:0013` | Unfinished phrase makes failed categorization evidentiary. |
| `競い合うライバルのクラス` | classes that compete as rivals | `Y1FF|spine:247|text/part0246.html|p:0014` | Class structure constrains private relationship meaning. |
| `戦意喪失` | loss of will to fight | `Y1FF|spine:247|text/part0246.html|p:0013` | Ayanokōji's support is connected to recovery of competitive agency. |
| `新しい戦いが始まる` | a new battle begins | `Y1FF|spine:247|text/part0246.html|p:0029` | Ichinose returns priority to class struggle at the Year 2 threshold. |

# 26. Full First File evidence ledger

The following 82 records reproduce the locked source-audited `Y1FF` evidence layer. Documentary rows are image-primary. Fiction rows are paragraph-primary.

| Evidence ID | Locator | Layer | Type | Claim / event | Confidence |
|---|---|---|---|---|---|
| `Y1FF-E001` | `Y1FF|spine:3|text/part0002.html|image:00003.jpeg` | `FF-DATA` | `IR` | First-half annual calendar records the school-year event sequence and class-point movement through the sports festival. | `H` |
| `Y1FF-E002` | `Y1FF|spine:4|text/part0003.html|image:00004.jpeg` | `FF-DATA` | `IR` | Second-half annual calendar records Paper Shuffle through spring break and Year 1 closing class-point positions. | `H` |
| `Y1FF-E003` | `Y1FF|spine:10|text/part0009.html|image:00008.jpeg` | `FF-DATA` | `IR` | School Guide states the institutional ideal of cultivating excellent personnel and outlines the class/private point system. | `H` |
| `Y1FF-E004` | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | `FF-RATING` | `IR` | Ayanokōji 7/1 rating: academics C, judgment C-, cooperation D, physical C-, intelligence C-. | `H` |
| `Y1FF-E005` | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | `FF-EDITORIAL` | `RC` | Ayanokōji rating prose explicitly attributes his mediocre academic evaluation to deliberately scoring 50 in every entrance-exam subject. | `H` |
| `Y1FF-E006` | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | `FF-EDITORIAL` | `RR` | Ayanokōji survey labels low communication ability but also notes the emergence of a comfortable peer group. | `H` |
| `Y1FF-E007` | `Y1FF|spine:13|text/part0012.html|image:00011.jpeg` | `FF-EDITORIAL` | `VJ` | Ayanokōji survey retrospectively labels him merciless when final victory is at stake. | `M` |
| `Y1FF-E008` | `Y1FF|spine:14|text/part0013.html|image:00012.jpeg` | `FF-DATA` | `RR` | Ayanokōji background page officially frames his father as White Room operator and Ayanokōji as the surviving fourth-generation highest masterpiece. | `M` |
| `Y1FF-E009` | `Y1FF|spine:14|text/part0013.html|image:00012.jpeg` | `FF-EDITORIAL` | `RR` | Ayanokōji background page summarizes his Year 1 hidden-X activity and protection from expulsion. | `H` |
| `Y1FF-E010` | `Y1FF|spine:15|text/part0014.html|image:00013.jpeg` | `FF-EDITORIAL` | `RR` | Ayanokōji relationship page identifies post-island social expansion into the Ayanokōji group and other peer ties. | `H` |
| `Y1FF-E011` | `Y1FF|spine:15|text/part0014.html|image:00013.jpeg` | `FF-EDITORIAL` | `RR` | Ayanokōji relationship page frames his Kei relationship as a romance entered to learn an absent domain. | `H` |
| `Y1FF-E012` | `Y1FF|spine:17|text/part0016.html|image:00015.jpeg` | `FF-RATING` | `IR` | Horikita 7/1 rating: academics A, judgment B-, cooperation E, physical B+, intelligence A-. | `H` |
| `Y1FF-E013` | `Y1FF|spine:17|text/part0016.html|image:00015.jpeg` | `FF-EDITORIAL` | `RR` | Horikita rating prose treats her academic and athletic capacity as A-class level while locating her D-class placement in inability to consider others. | `H` |
| `Y1FF-E014` | `Y1FF|spine:17|text/part0016.html|image:00015.jpeg` | `FF-EDITORIAL` | `RR` | Horikita survey states she gradually understands the difference between solitude and being truly solitary. | `H` |
| `Y1FF-E015` | `Y1FF|spine:21|text/part0020.html|image:00019.jpeg` | `FF-RATING` | `IR` | Kushida 7/1 rating: academics B, judgment C+, cooperation A, physical B, intelligence B-. | `H` |
| `Y1FF-E016` | `Y1FF|spine:21|text/part0020.html|image:00019.jpeg` | `FF-EDITORIAL` | `RR` | Kushida prose separates high social cooperation from the middle-school conduct that contributed to D placement. | `H` |
| `Y1FF-E017` | `Y1FF|spine:23|text/part0022.html|image:00021.jpeg` | `FF-RATING` | `IR` | Sakura 7/1 rating records modest academic capacity and low judgment/cooperation/physical visibility. | `H` |
| `Y1FF-E018` | `Y1FF|spine:23|text/part0022.html|image:00021.jpeg` | `FF-EDITORIAL` | `RR` | Sakura framing links Shizuku identity to self-change and later social movement toward the desired peer group. | `H` |
| `Y1FF-E019` | `Y1FF|spine:25|text/part0024.html|image:00023.jpeg` | `FF-RATING` | `IR` | Kei 7/1 rating: academics D-, judgment C-, cooperation E+, physical D, intelligence D-. | `H` |
| `Y1FF-E020` | `Y1FF|spine:25|text/part0024.html|image:00023.jpeg` | `FF-EDITORIAL` | `RR` | Kei page identifies her public personality and boyfriend strategy as survival adaptations to earlier trauma. | `H` |
| `Y1FF-E021` | `Y1FF|spine:29|text/part0028.html|image:00027.jpeg` | `FF-RATING` | `IR` | Hirata 7/1 rating: academics B, judgment B+, cooperation A-, physical B, intelligence B. | `H` |
| `Y1FF-E022` | `Y1FF|spine:29|text/part0028.html|image:00027.jpeg` | `FF-EDITORIAL` | `RR` | Hirata is officially framed as highly trusted and functionally difficult for the class to replace. | `H` |
| `Y1FF-E023` | `Y1FF|spine:30|text/part0029.html|image:00028.jpeg` | `FF-RATING` | `IR` | Kōenji compact profile: academics A, judgment C, cooperation E-, physical A, intelligence C. | `H` |
| `Y1FF-E024` | `Y1FF|spine:31|text/part0030.html|image:00029.jpeg` | `FF-RATING` | `IR` | Sudō compact profile: academics E, judgment D+, cooperation D, physical A, intelligence E. | `H` |
| `Y1FF-E025` | `Y1FF|spine:42|text/part0041.html|image:00040.jpeg` | `FF-EDITORIAL` | `RR` | Horikita-class year-end summary says distinctive students have explosive potential but cohesion remains insufficient and leadership must aggregate individualists. | `H` |
| `Y1FF-E026` | `Y1FF|spine:45|text/part0044.html|image:00043.jpeg` | `FF-RATING` | `IR` | Ryūen 7/1 rating: academics D, judgment A, cooperation E-, physical B, intelligence B. | `H` |
| `Y1FF-E027` | `Y1FF|spine:45|text/part0044.html|image:00043.jpeg` | `FF-EDITORIAL` | `RR` | Ryūen profile simultaneously frames overwhelming leadership and a form of class-directed obligation behind violence. | `H` |
| `Y1FF-E028` | `Y1FF|spine:46|text/part0045.html|image:00044.jpeg` | `FF-EDITORIAL` | `RR` | Ryūen background page traces childhood violence, absence of fear, island cooperation-for-payment and preference for outcome-oriented methods. | `H` |
| `Y1FF-E029` | `Y1FF|spine:47|text/part0046.html|image:00045.jpeg` | `FF-EDITORIAL` | `RR` | Ryūen relationship page emphasizes utility-based cross-class contacts and his post-defeat plan to overturn Sakayanagi and Ichinose. | `H` |
| `Y1FF-E030` | `Y1FF|spine:51|text/part0050.html|image:00049.jpeg` | `FF-RATING` | `IR` | Hiyori 7/1 rating: academics A-, judgment E, cooperation D, physical E, intelligence A-. | `H` |
| `Y1FF-E031` | `Y1FF|spine:51|text/part0050.html|image:00049.jpeg` | `FF-EDITORIAL` | `RC` | The same Hiyori page describes perceptive inference and quick thinking despite formal judgment E. | `H` |
| `Y1FF-E032` | `Y1FF|spine:51|text/part0050.html|image:00049.jpeg` | `FF-EDITORIAL` | `RR` | Hiyori is framed as capable of harsh class-protective judgment despite a quiet temperament. | `H` |
| `Y1FF-E033` | `Y1FF|spine:60|text/part0059.html|image:00058.jpeg` | `FF-EDITORIAL` | `RR` | Ryūen-class year-end summary calls the class coordinated under dictatorship but overdependent on Ryūen and weak in individual development. | `H` |
| `Y1FF-E034` | `Y1FF|spine:63|text/part0062.html|image:00061.jpeg` | `FF-RATING` | `IR` | Ichinose 7/1 rating: academics B+, judgment B, cooperation A-, physical C, intelligence A. | `H` |
| `Y1FF-E035` | `Y1FF|spine:63|text/part0062.html|image:00061.jpeg` | `FF-EDITORIAL` | `RR` | Ichinose profile highlights collective private-point management as a contingency resource. | `H` |
| `Y1FF-E036` | `Y1FF|spine:63|text/part0062.html|image:00061.jpeg` | `FF-EDITORIAL` | `RR` | Ichinose profile identifies excessive consideration for others as a possible liability rather than lack of intelligence. | `H` |
| `Y1FF-E037` | `Y1FF|spine:70|text/part0069.html|image:00068.jpeg` | `FF-EDITORIAL` | `RR` | Ichinose-class year-end summary records strong cohesion, collective savings, no expulsions, and insufficient result conversion. | `H` |
| `Y1FF-E038` | `Y1FF|spine:73|text/part0072.html|image:00071.jpeg` | `FF-RATING` | `IR` | Sakayanagi 7/1 rating: academics A, judgment A, cooperation C+, physical E-, intelligence A. | `H` |
| `Y1FF-E039` | `Y1FF|spine:73|text/part0072.html|image:00071.jpeg` | `FF-EDITORIAL` | `RR` | Sakayanagi rating prose treats physical disability as a competitive handicap while recognizing her as class leader. | `H` |
| `Y1FF-E040` | `Y1FF|spine:83|text/part0082.html|image:00081.jpeg` | `FF-EDITORIAL` | `RR` | Sakayanagi-class summary emphasizes deep talent and correct role allocation while warning that strategy is monopolized and the class is not fully unified. | `H` |
| `Y1FF-E041` | `Y1FF|spine:84|text/part0083.html|image:00082.jpeg` | `FF-RATING` | `IR` | Hypothetical Year-1 OAA page explicitly states that the ratings reconstruct what Year-2 OAA would have shown at the start of the first-year second term. | `H` |
| `Y1FF-E042` | `Y1FF|spine:84|text/part0083.html|image:00082.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Ayanokōji at 50 academics, 45 physical, 31 adaptability, 27 social contribution, 40 overall. | `H` |
| `Y1FF-E043` | `Y1FF|spine:85|text/part0084.html|image:00083.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Horikita at 89 academics, 79 physical, 57 adaptability, 34 social contribution, 69 overall. | `H` |
| `Y1FF-E044` | `Y1FF|spine:85|text/part0084.html|image:00083.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Kei at 33 academics, 44 physical, 46 adaptability, 22 social contribution, 38 overall. | `H` |
| `Y1FF-E045` | `Y1FF|spine:85|text/part0084.html|image:00083.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Ryūen at 42 academics, 69 physical, 76 adaptability, 1 social contribution, 54 overall. | `H` |
| `Y1FF-E046` | `Y1FF|spine:86|text/part0085.html|image:00084.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Hiyori at 82 academics, 29 physical, 23 adaptability, 44 social contribution, 45 overall. | `H` |
| `Y1FF-E047` | `Y1FF|spine:86|text/part0085.html|image:00084.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Ichinose at 81 academics, 53 physical, 84 adaptability, 84 social contribution, 74 overall. | `H` |
| `Y1FF-E048` | `Y1FF|spine:86|text/part0085.html|image:00084.jpeg` | `FF-RATING` | `IR` | Hypothetical OAA measures Sakayanagi at 93 academics, 24 physical, 71 adaptability, 55 social contribution, 62 overall. | `H` |
| `Y1FF-E049` | `Y1FF|spine:105|text/part0104.html|image:00103.jpeg` | `FF-EDITORIAL` | `VF` | Casual-clothes archive deliberately re-presents selected private/off-duty illustrations as a visual character collection. | `H` |
| `Y1FF-E050` | `Y1FF|spine:106|text/part0105.html|image:00104.jpeg` | `FF-EDITORIAL` | `VF` | Second casual-clothes page foregrounds Ichinose, Ryūen, Sakayanagi, Kei and Shiina in private/off-duty presentation. | `H` |
| `Y1FF-E051` | `Y1FF|spine:108|text/part0107.html|image:00106.jpeg` | `FF-EDITORIAL` | `RR` | Activity Report opens by converting Volume 1 into chronological Story Guidance with event summary and retrospective explanatory prose. | `H` |
| `Y1FF-E052` | `Y1FF|spine:236|text/part0235.html|image:00234.jpeg` | `FF-EDITORIAL` | `RR` | V11.5 activity summary explicitly frames Horikita as pursuing growth, seeking Ayanokōji ability verification, and moving toward an independent path. | `H` |
| `Y1FF-E053` | `Y1FF|spine:237|text/part0236.html|image:00235.jpeg` | `FF-EDITORIAL` | `RR` | V11.5 activity summary frames Ayanokōji as identifying Matsushita ability, handling White Room danger, and entering a romance with Kei to learn love. | `H` |
| `Y1FF-E054` | `Y1FF|spine:240|text/part0239.html|image:00238.jpeg` | `FF-EDITORIAL` | `RR` | Special column 人心掌握術 compresses Ayanokōji–Kei development into a language of psychological capture and future romantic learning. | `H` |
| `Y1FF-E055` | `Y1FF|spine:241|text/part0240.html|image:00239.jpeg` | `FF-EDITORIAL` | `RR` | Year-2 bridge column reiterates White Room generation structure and identifies a White Room student as a coming threat. | `H` |
| `Y1FF-E056` | `Y1FF|spine:241|text/part0240.html|image:00239.jpeg` | `FF-DATA` | `IR` | Year-2 bridge column explains the Protection Point as a nontransferable one-time expulsion-canceling institutional resource. | `H` |
| `Y1FF-E057` | `Y1FF|spine:242|text/part0241.html|image:00240.jpeg` | `FF-EDITORIAL` | `RR` | Guidebook quiz converts Year 1 narrative recall into a scored memory exercise, making retrospective canon mastery itself part of the paratext. | `H` |
| `Y1FF-E058` | `Y1FF|spine:239|text/part0238.html|image:00237.jpeg` | `FF-DATA` | `IR` | Year-end checkpoint records A 1131, B 550, Ryūen class 508, Horikita class 347. | `H` |
| `Y1FF-E059` | `Y1FF|spine:246|text/part0245.html|p:0006` | `FF-FICTION` | `CI` | Ayanokōji says he is basically looking forward to returning to school. | `H` |
| `Y1FF-E060` | `Y1FF|spine:246|text/part0245.html|p:0009` | `FF-FICTION` | `CI` | Ayanokōji states he spends his days at the school in order to live a student-like life. | `H` |
| `Y1FF-E061` | `Y1FF|spine:246|text/part0245.html|p:0010` | `FF-FICTION` | `CI` | Ordinary studying and exercise are described by Ayanokōji as the daily life that gives him the greatest sense of fulfillment. | `H` |
| `Y1FF-E062` | `Y1FF|spine:246|text/part0245.html|p:0015-0017` | `FF-FICTION` | `TF` | Ayanokōji now explicitly places Kei beyond friendship in the category of girlfriend. | `H` |
| `Y1FF-E063` | `Y1FF|spine:246|text/part0245.html|p:0041-0046` | `FF-FICTION` | `CI` | He deliberately avoids deeply analyzing or controlling his emerging romantic behavior and chooses to let himself enter the world of romance. | `H` |
| `Y1FF-E064` | `Y1FF|spine:246|text/part0245.html|p:0051-0053` | `FF-FICTION` | `CI` | He admits he wanted to wait for contact from Kei rather than initiate it himself. | `H` |
| `Y1FF-E065` | `Y1FF|spine:246|text/part0245.html|p:0056-0061` | `FF-FICTION` | `CI` | He contrasts the former user/used relation with the new world opened by ordinary reciprocal contact. | `H` |
| `Y1FF-E066` | `Y1FF|spine:246|text/part0245.html|p:0065-0067` | `FF-FICTION` | `CI` | Conversation with no strategic or informational relevance becomes intrinsically interesting to him. | `H` |
| `Y1FF-E067` | `Y1FF|spine:246|text/part0245.html|p:0068-0081` | `FF-FICTION` | `CI` | Ayanokōji recognizes ordinary conversational weakness and treats reciprocal topic-making as something new he should attempt. | `H` |
| `Y1FF-E068` | `Y1FF|spine:246|text/part0245.html|p:0082-0120` | `FF-FICTION` | `TF` | The first call ends badly because Ayanokōji immediately disconnects when Kei expected reciprocal reluctance to separate. | `H` |
| `Y1FF-E069` | `Y1FF|spine:246|text/part0245.html|p:0111` | `FF-FICTION` | `CI` | Ayanokōji says this is the first time he has talked with someone this enjoyably. | `H` |
| `Y1FF-E070` | `Y1FF|spine:246|text/part0245.html|p:0139-0145` | `FF-FICTION` | `CI` | He calls the difficult phone-ending problem a trial attached to his own decision to seek a romantic relationship. | `H` |
| `Y1FF-E071` | `Y1FF|spine:246|text/part0245.html|p:0147-0160` | `FF-FICTION` | `CI` | Ayanokōji explains that he wants tomorrow to arrive because he wants to see Kei. | `H` |
| `Y1FF-E072` | `Y1FF|spine:246|text/part0245.html|p:0163-0169` | `FF-FICTION` | `TF` | Kei is the person who decides that their relationship will remain secret for a little longer. | `H` |
| `Y1FF-E073` | `Y1FF|spine:246|text/part0245.html|p:0170-0176` | `FF-FICTION` | `CI` | Ayanokōji still wants peaceful days but now also calls unpredictable rapids part of what makes school life interesting. | `H` |
| `Y1FF-E074` | `Y1FF|spine:247|text/part0246.html|p:0002-0005` | `FF-FICTION` | `CI` | Ichinose reports spending much of spring break alone thinking through Year 2 and her class future before re-entering ordinary peer time. | `H` |
| `Y1FF-E075` | `Y1FF|spine:247|text/part0246.html|p:0006-0011` | `FF-FICTION` | `CI` | Ichinose genuinely trusts her classmates while also hiding some uncertainty because she does not want to burden them. | `H` |
| `Y1FF-E076` | `Y1FF|spine:247|text/part0246.html|p:0010` | `FF-FICTION` | `CI` | Ichinose attributes the year-end defeat to herself; this is her self-blame rather than omniscient causal adjudication. | `H` |
| `Y1FF-E077` | `Y1FF|spine:247|text/part0246.html|p:0013` | `FF-FICTION` | `CI` | Remembering Ayanokōji support still makes Ichinose feel intense warmth and restores her willingness to continue fighting rival classes. | `H` |
| `Y1FF-E078` | `Y1FF|spine:247|text/part0246.html|p:0013` | `FF-FICTION` | `UA` | Ichinose calls Ayanokōji a precious friend and very important person but cannot produce the next relational category. | `H` |
| `Y1FF-E079` | `Y1FF|spine:247|text/part0246.html|p:0014-0017` | `FF-FICTION` | `CI` | She treats cross-class rivalry as a reason not to indulge or name those feelings and imagines the dilemma disappearing if they shared a class. | `H` |
| `Y1FF-E080` | `Y1FF|spine:247|text/part0246.html|p:0018-0019` | `FF-FICTION` | `CI` | Ichinose describes the feeling as difficult to suppress and physically shakes it away. | `H` |
| `Y1FF-E081` | `Y1FF|spine:247|text/part0246.html|p:0020-0024` | `FF-FICTION` | `CI` | Her guard tends to loosen around close friends. | `H` |
| `Y1FF-E082` | `Y1FF|spine:247|text/part0246.html|p:0025-0029` | `FF-FICTION` | `CI` | She consciously returns priority to the class battle and approaches Year 2 without the security of a comfortable upper-class margin. | `H` |

# 27. Evidence-type glossary and interpretation limits

The compact evidence labels are retrieval aids, not substitutes for judgment.

- `IR` — institutional record/rule or institutionalized rating output;
- `RC` — record correction/contradiction internal to the documentary layer;
- `RR` — retrospective or revision framing;
- `VJ` — value judgment supplied by the paratext rather than neutral measurement;
- `CI` — character interiority in bonus fiction;
- `TF` — direct textual fact in bonus fiction;
- `UA` — unresolved ambiguity that should remain unresolved;
- `VF` — visual fact or visual-curatorial fact.

The confidence grade refers to confidence that the source supports the stated record—not confidence that every possible interpretation of the record is settled.

The most important example is `Y1FF-E008`. Confidence is medium not because the page is unverified; the page locator is verified. The qualification concerns **epistemic status**. The guidebook officially frames the White Room structure, but Year 1 analysis still distinguishes official retrospective framing from later primary-fiction verification of finer history.

# 28. Interpretive limits preserved at the First File boundary

The following questions remain open and must not be solved by later-year memory inside this artifact.

## 28.1 Kei and irreplaceability

The bonus story makes an instrument-only endpoint untenable. Ayanokōji enjoys purposeless conversation, attempts reciprocal behavior, and wants to see Kei.

It still does not prove that Kei has become permanently singular or that the relationship has become ethically symmetrical.

**Status: unresolved.**

## 28.2 Ayanokōji and ethical reform

Ordinary-life desire is real. Local non-optimization is real. Reciprocal learning is real.

His continuing willingness to author other people's environments and futures is also real.

**Status: development without completed ethical transformation.**

## 28.3 Horikita and independence

Her independent path is officially foregrounded. The novels show that independence consists of integrating and revising inherited influence, not becoming untouched by it.

**Status: strengthened as self-authored integration.**

## 28.4 Ryūen and legitimacy

His rule can become more voluntarily sustained without becoming morally benign.

**Status: sociological legitimation remains distinct from moral reform.**

## 28.5 Ichinose and trust

The evidence does not require the conclusion that trust itself is her defect.

**Status: solidarity remains real capacity; adversarial architecture remains the problem.**

## 28.6 White Room detail

Broad framing is strengthened. Fine-grained claims remain source-tiered.

**Status: partial retrospective corroboration, not total closure.**

## 28.7 Ratings and total human value

The guidebook never warrants reading its axes as complete personhood.

**Status: explicitly rejected as an analytical move.**

# 29. Year 1 architectural delta

Before *First File*, the mature V11.5 endpoint can be formulated as **reciprocal authorship**.

Ayanokōji has begun choosing goals that are not White Room assignments. Horikita increasingly authors her own leadership. Kei can answer rather than merely be assigned. Ichinose can retain her own class purpose despite Ayanokōji's influence. Manabu's legacy challenge asks Ayanokōji what he will leave behind rather than what role he will fulfill.

*First File* adds an epistemic layer:

> **Reciprocity requires not only letting another person choose, but accepting that one's model of that person is incomplete.**

This is why the guidebook belongs at the Year 1 boundary rather than in a miscellaneous appendix.

Its ratings, archives, and summaries turn the entire first year into a test case for the series' title concept. The files contain real information. Some are extraordinarily useful. Yet Ayanokōji can manufacture the file that measures him. Hiyori can exceed a judgment grade. Kei's social survival capacity can disappear inside weak conventional ratings. Horikita's cooperation E can become obsolete through development. Ichinose's high social metrics cannot automatically solve adversarial politics. Kōenji's high capacities cannot be requisitioned by the group simply because they exist.

The final Year 1 progression should therefore be revised to:

> **authored visibility → authored legibility → authored environment → authored dependency → counter-curriculum → controlled exposure → distributed integration under hidden contingency → sovereignty over futurity → negotiated indispensability → institutional authorship → authored reputation → manufactured disposability → developmental authorship under procedural capture → reciprocal authorship → the file and the person**

The last term does not replace the earlier ones.

It tells us what they had been approaching all along.

# 30. Handoff to the formal Year 1 evidence lock

This audit completes the final source-local reading required before the Year 1 evidence freeze.

The formal reconciliation should verify:

1. all 82 `Y1FF` evidence IDs remain sequential and unique;
2. the 58 fixed-layout records resolve to existing image resources;
3. the 24 fiction records resolve to their XHTML paragraph ranges;
4. the 18 Japanese anchors remain consistent with the mixed image/text authority boundary;
5. V11 and V11.5 evidence remains unchanged at their earlier spoiler boundaries;
6. no Year 2, Volume 0, *Second List*, Year 3, or adaptation evidence leaks backward;
7. specialist ledgers inherit the corrected `the file and the person` endpoint without silently rewriting prior volume artifacts.

Only after that lock should the provisional `COTE_Y1_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` be revised and frozen.

# 31. Final synthesis

*First File* is valuable because it is both an archive and an inadvertent critique of archival completeness.

It demonstrates that official files can be:

- accurate;
- useful;
- carefully categorized;
- retrospectively clarifying;
- and still radically incomplete as models of persons.

Ayanokōji's weak ratings are not meaningless numbers. They are accurate records of the performance he allowed the institution to see.

Horikita's low cooperation is not a lie. It is a photograph of a developmental state she can outgrow.

Kei's poor formal profile does not make her socially incapable. It reveals that the metric is not built to capture the kind of social survival competence that made her important.

Hiyori's page does not prove that ratings are fraudulent. It proves that a single label can be narrower than the capacities surrounding it.

Ichinose's high social metrics do not guarantee victory. They show that solidarity is real capacity whose political conversion remains a separate problem.

And the bonus fiction closes the argument at the level most resistant to quantification.

Ayanokōji wants school to return.

He enjoys a conversation that produces nothing useful.

He fails to hang up correctly because another person's expectation is not a tactical protocol.

He wants to see Kei.

Ichinose has a feeling she cannot fit into the available category of friendship.

She refuses to let the feeling erase her class responsibility.

These are not grand victories.

They are evidence that a human life contains values whose significance depends upon being lived rather than scored.

The Year 1 corpus can therefore close its source-reading phase on a proposition more precise than either “meritocracy is false” or “people cannot be measured”:

> **Measurement is real. Classification is useful. Knowledge about people can be extraordinarily powerful. The ethical and epistemic danger begins when a partial model becomes a claim to total definition.**

That applies to the school.

It applies to the guidebook.

It applies to Ayanokōji.

And it applies to the reader.

A file can help us find the person.

It cannot be allowed to become the person.
