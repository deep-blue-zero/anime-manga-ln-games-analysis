---
title: "Classroom of the Elite — Year 1 Checkpoint 01 Reconciliation"
subtitle: "Canonical reconciliation of the Y1V01–Y1V04.5 second-pass tranche"
series_jp: "ようこそ実力至上主義の教室へ"
series_en: "Classroom of the Elite"
project: "Manga and anime discussions"
artifact_type: "cross_volume_reconciliation_checkpoint"
checkpoint_id: "Y1-CP01"
version: "1.2"
status: "canonical_checkpoint_reconciled_and_audited"
source_boundary: "Y1V01–Y1V04.5"
spoiler_boundary: "through Y1V04.5 only"
analysis_pass: 2
method: "COTE_Y1_ANALYTICAL_METHOD_V2.md"
architecture: "COTE_Multi_Document_Synthesis_Architecture_v1.md"
canonical_volume_artifacts: 5
canonical_volume_words: 87991
canonical_volume_bytes: 627295
evidence_entries: 275
terminology_passage_entries_before_backfill: 64
normalized_paragraphs_reconciled: 18769
normalized_japanese_characters_reconciled: 758776
created_at: "2026-08-11"
updated_at: "2026-08-11"
next_source: "Y1V05"
longitudinal_threads:
  - "AYANOKOJI_FREEDOM"
  - "AYANOKOJI_AUTHORSHIP"
  - "AYANOKOJI_ORDINARY_LIFE"
  - "HORIKITA_INDEPENDENCE"
  - "HORIKITA_LEADERSHIP"
  - "KEI_DEPENDENCY_AUTONOMY"
  - "JITSURYOKU"
  - "ENVIRONMENTAL_AUTHORSHIP"
  - "RELATIONSHIP_RECIPROCITY"
  - "PROTECTION_OWNERSHIP"
  - "TRUTH_PROOF_RECORD"
  - "ORDINARY_LIFE_COUNTER_CURRICULUM"
validated_source_locators: 275
checkpoint_result: "PASS_AFTER_ADMINISTRATIVE_AND_PROVENANCE_REPAIRS"
---

# 『ようこそ実力至上主義の教室へ』
## Year 1 Checkpoint 01 Reconciliation
### Canonical reconciliation of `Y1V01–Y1V04.5`

# 0. Purpose and governing boundary

This checkpoint reconciles the first completed tranche of the Year 1 second pass:

- `Y1V01`;
- `Y1V02`;
- `Y1V03`;
- `Y1V04`;
- `Y1V04.5`.

It does **not** advance the spoiler boundary beyond Volume 4.5. It does not use Volume 5 or later Year 1 material to answer questions that remained open at this point, and it does not import Year 2, Volume 0, *Second List*, Year 3, adaptation material, or remembered future revelations.

The checkpoint has four functions:

1. verify that the five immutable volume artifacts and their 275 evidence entries remain internally consistent;
2. reconcile cumulative character, relationship, class-polity, institution, and terminology state;
3. identify cross-volume conclusions that are now sufficiently supported to carry forward into Volume 5;
4. externalize the current analytical state into files so later work does not depend upon live conversational memory.

This is an **interim canonical snapshot**, not a Year 1 synthesis. The later Year 1 ledgers and specialist documents will supersede it for current-state reference while preserving this checkpoint as the authoritative record of what had been established through `Y1V04.5`.

# 1. Corpus integrity reconciliation

## 1.1 Canonical volume layer

| Source | Canonical artifact | Words | Bytes | Evidence IDs | Source hash verified |
|---|---|---:|---:|---:|---|
| `Y1V01` | `volumes/COTE_Y1_V01_DEEP_READING.md` | 11,459 | 81,818 | 35 | yes |
| `Y1V02` | `volumes/COTE_Y1_V02_DEEP_READING.md` | 18,567 | 131,619 | 48 | yes |
| `Y1V03` | `volumes/COTE_Y1_V03_DEEP_READING.md` | 18,974 | 135,931 | 56 | yes |
| `Y1V04` | `volumes/COTE_Y1_V04_DEEP_READING.md` | 23,996 | 166,884 | 68 | yes |
| `Y1V04.5` | `volumes/COTE_Y1_V04_5_DEEP_READING.md` | 14,977 | 110,843 | 68 | yes |

The five artifacts total **87,973 analytical words** and **627,095 bytes**.

Each source EPUB hash recorded in the corresponding YAML front matter was rechecked against the available Japanese EPUB and matched. The five source maps jointly represent:

- 18,769 deterministic substantive paragraphs;
- 758,776 normalized Japanese characters;
- complete local source locators for the 275 evidence entries.

## 1.2 Evidence ledger integrity

The cumulative evidence ledger was compared against the evidence tables embedded in all five canonical volume artifacts.

Results:

- 275 cumulative evidence IDs;
- 275 unique IDs;
- no duplicate evidence IDs;
- no missing volume-local entries;
- no cumulative-ledger entries lacking a corresponding volume artifact;
- every volume sequence is contiguous from `E001` through its final entry;
- evidence counts reconcile exactly as `35 + 48 + 56 + 68 + 68 = 275`.

The Volume 1 cumulative-ledger locators originally used an older abbreviated format without the explicit `Y1V01|` source prefix. This checkpoint normalizes the **rolling ledger** to the current source-prefixed locator convention while leaving the immutable Volume 1 artifact unchanged. This is a formatting reconciliation, not a substantive revision.

## 1.2.1 Locator-index convention

The original frozen extractors used different historical spine-number bases: `Y1V01–Y1V04` use zero-based artifact locators, while `Y1V04.5` uses one-based artifact locators. Rewriting the earlier immutable artifacts would create unnecessary provenance churn. The source map records a per-source offset against its one-based `spine_index`. All 275 cumulative evidence locators—including one multi-spine range and thirteen visual-inventory locators—validate against the verified EPUB structure.

## 1.3 Alias and Volume 4.5 provenance reconciliation

The checkpoint discovered that an attempted compatibility-pointer repair had overwritten the canonical underscore-path Volume 4.5 artifact. The primary-source evidence layer was not lost: the verified Japanese EPUB, normalized extraction, complete 68-entry evidence table, exact-language index, revision audit, cumulative delta, and final synthesis remained available.

The canonical artifact was therefore reconstructed as an explicit version 1.1 source-grounded repair:

- canonical: `volumes/COTE_Y1_V04_5_DEEP_READING.md`;
- prior delivered v1.0 SHA-256: `639bc930c524be17bcb47eec067c1c61b0156de57523ad267270c81502a590eb`;
- repaired v1.1 SHA-256: `981d3022d7fdbd85748a5002ea34af938e12d997de742db1361ebab4aa3dd416`;
- evidence sequence preserved: `Y1V04.5-E001–E068`;
- source and normalized-text hashes unchanged;
- later-volume material excluded.

See [`../support/COTE_Y1_V04_5_RECOVERY_NOTE.md`](../04%20Source%20Maps%20and%20Support/COTE_Y1_V04_5_RECOVERY_NOTE.md) for the full provenance record.

This is not described as byte-for-byte recovery. The repaired artifact records its provenance and supersession state in YAML. The dot-form filename remains a small noncanonical pointer to the underscore artifact and is excluded from canonical counts and the clean checkpoint archive.

## 1.4 Administrative-state reconciliation

The prior corpus JSON index and checksum registry had not fully incorporated Volumes 2–4.5 or the current sizes of rolling ledgers. This checkpoint rebuilds:

- `COTE_Y1_CORPUS_INDEX.json`;
- `COTE_Y1_ARTIFACT_CHECKSUMS.sha256`;
- `COTE_Y1_CORPUS_MANIFEST.md`;
- `COTE_Y1_DELIVERY_AUDIT.md`;
- `support/COTE_Y1_PROJECT_STATUS.md`.

The rebuilt index treats all five volume artifacts, checkpoint ledgers, source/provenance files, and governing references as distinct artifact classes.

# 2. Cross-volume architecture through Volume 4.5

The first five works now form a coherent escalation in what Ayanokōji controls and what the school makes politically valuable.

| Stage | Volume | Governing problem | Ayanokōji’s characteristic form of authorship |
|---|---|---|---|
| 1 | `Y1V01` | Hidden evaluation and fragmented ability | authors his own mediocrity; controls timing and public credit |
| 2 | `Y1V02` | Truth under unequal credibility | authors the cue path through which proof becomes believable |
| 3 | `Y1V03` | Ecological ability and collective conversion | authors an examination environment and another person’s public legitimacy |
| 4 | `Y1V04` | Trust, trauma, and private political infrastructure | authors dependency by narrowing protection alternatives |
| 5 | `Y1V04.5` | Ordinary life outside explicit examination | reveals that he already possesses both coercive and low-coercion intervention models |

The cumulative movement is best described as:

> **authored visibility → authored legibility → authored environment → authored dependency → ethical plurality inside ordinary life**

Volume 4.5 prevents this sequence from becoming mechanically deterministic. Ayanokōji is not forced by incapacity to manipulate everyone. He can:

- let Ike discover his own competence;
- preserve Airi’s authority over her romantic answer;
- decline leverage over Katsuragi;
- shield Horikita’s dignity;
- destroy evidence that could have become future leverage;
- and stay with someone simply because she asks him not to leave.

The sharper cumulative ethical question is therefore no longer whether Ayanokōji can act less coercively. The text has already shown that he can.

It is:

> **What makes him choose scaffolding, concealment, command, coercion, or manufactured dependency in a particular relationship?**

# 3. Reconciled cumulative theses

## 3.1 `実力` is ecological, not merely possessed

The first tranche supports seven analytically separable forms of ability:

1. **possessed ability** — what a person can do;
2. **displayed ability** — what the person chooses or manages to show;
3. **measured ability** — what the school records;
4. **socially usable ability** — what others can reliably convert into collective action;
5. **developmental ability** — capacity to become more capable or usable over time;
6. **political ability** — capacity to create legitimacy, information networks, or compliance;
7. **moral ability** — capacity to exercise judgment under pressure without treating outcome as the only value.

Examples through Volume 4.5 include:

- Ayanokōji possesses far more than he displays and deliberately authors a mediocre measured profile.
- Ike’s camping experience becomes decisive only when the island environment makes it relevant.
- Sudō’s athletic capacity begins becoming institutionally and collectively usable through basketball discipline.
- Kei’s control of social atmosphere is politically valuable despite weak conventional academic framing.
- Kushida’s relational memory and social reach constitute real ability even while her motives remain unstable.
- Ibuki’s conversational capacity exists but becomes difficult to use under anticipated social judgment.
- Airi’s communication improves radically when the medium changes from face-to-face speech to text.
- Kōenji demonstrates the inverse problem: immense possessed ability may remain unavailable as class power.

The checkpoint therefore rejects any single-axis reading of `実力`.

## 3.2 Legibility is a political resource

Volume 1 shows that behavior becomes class consequence through rules students do not initially understand. Volume 2 shows that truth is ineffective unless it can become evidence with sufficient credibility. Volume 3 shows that a class can perform genuine cooperation while the public causal story of victory is false. Volume 4 shows that device identity, social masks, and trauma can be layered strategically. Volume 4.5 shows that privacy may require concealment from institutional surveillance.

The cumulative distinction is:

1. what happened;
2. what evidence exists;
3. who can make the evidence credible;
4. what others believe;
5. what the institution records;
6. what later readers may eventually learn.

Ayanokōji’s central early power is not merely solving problems. It is controlling the passage between these levels.

## 3.3 Class D’s defect is fragmented conversion

The class does not lack ability. Its abilities are:

- hidden;
- socially inaccessible;
- emotionally unregulated;
- distributed across incompatible personalities;
- or rejected as irrelevant by narrow evaluative frameworks.

The first tranche progressively makes this visible:

- Horikita must learn to teach rather than merely know.
- Sudō must protect physical talent from his own conduct.
- Ike’s practical knowledge requires a context in which it counts.
- Kushida converts private strategy into classwide participation.
- Hirata makes cooperation psychologically inhabitable.
- Kei governs a female social ecology that formal scores barely represent.
- Ayanokōji links these capacities while hiding his role.

The political question is whether the class can eventually internalize this integration rather than remaining dependent upon invisible correction.

## 3.4 Ordinary life is a counter-curriculum, not an escape from the institution

Volume 4.5 establishes that ordinary experience can develop capacities formal exams do not directly reward:

- accepting help;
- declining leverage;
- choosing friendship;
- tolerating purposeless time;
- forming sensory preferences;
- making a romantic refusal;
- and creating cross-class contact outside immediate competition.

Yet ordinary life remains institutionally shaped:

- campus isolation blocks family contact;
- points price leisure;
- surveillance affects privacy;
- student-council succession enters the pool outing;
- and class competition repeatedly reappears inside play.

The correct cumulative formulation is:

> **ordinary life is counter-curriculum inside enclosure, not life outside institutional power.**

## 3.5 Protection has already divided into distinct political forms

Through Volume 4.5, at least four protection models are visible.

### Hirata: bounded social protection

- publicly legible;
- nonsexual;
- not dependent upon private obedience;
- limited by his refusal to retaliate violently or privilege one person absolutely.

### Ayanokōji: effective private protection

- informationally asymmetric;
- capable of deterrence;
- frequently conditioned upon service;
- at its most severe, strengthened by danger he helped create.

### Ichinose: consensual collective protection

- rooted in voluntary disclosure and group trust;
- politically broad;
- not yet tested against the harshest compulsory sacrifice.

### Manabu: institutional protection through capacity

- formal office does not itself create power;
- authority depends upon the ability of the officeholder;
- his larger protective philosophy remains incompletely visible at this boundary.

The tranche therefore supports the distinction:

> **protection is not automatically ownership, but protection becomes ownership-like when safety depends upon obedience, concealed terms, or alternatives narrowed by the protector.**

# 4. Reconciled character state

Detailed checkpoint ledgers now exist for Ayanokōji, Horikita, the class core, rival leaders, and seniors/adults. The most important current-state conclusions are summarized here.

## Ayanokōji Kiyotaka

He is not an emotionless strategist with a fake ordinary layer. He is an unfinished person whose ordinary, relational, and strategic layers are all genuine and unequally developed.

By Volume 4.5 he has demonstrated:

- explicit loneliness and desire for friendship;
- attraction, embarrassment, sexual curiosity, and sensory pleasure;
- a sincere preference for school as separation from the outside world;
- a strong procedural sensitivity to how judgment becomes enforceable;
- exceptional capacity to model people and environments;
- willingness to engineer severe suffering when he predicts strategic benefit;
- and the ability to choose lower-coercion support when he considers it sufficient.

His description of himself as `生まれたばかり`, `まだ液状`, and `真っ白` is best read as unfinished ordinary autobiography, not absence of emotion.

## Horikita Suzune

She has moved from static academic merit toward developmental and relational judgment, but her leadership remains scaffolded.

She can now:

- redesign teaching around learners;
- research before judging;
- recognize progress;
- accept help in private;
- own a morally compromised bluff;
- identify that leisure may possess noninstrumental value;
- and use `仲間` for Ayanokōji.

She still:

- treats her own Class D placement as likely institutional error;
- interprets many social situations through competition;
- lacks broad relational infrastructure;
- and does not understand the full extent of Ayanokōji’s hidden authorship.

## Karuizawa Kei

Her `寄生虫` language is a trauma-authored self-model, not total character truth.

She already possesses:

- social command;
- rapid threat recognition;
- adaptive performance;
- and the ability to act covertly.

Her relationship with Ayanokōji is not yet a partnership. It is a **coerced protected collaboration** whose benefits are real and whose terms are radically asymmetric. Volume 4.5 shows the first signs that she can use the private relationship to discuss trauma and experience voluntary enjoyment, but her refusal capacity remains weak.

## Hirata Yōsuke

Hirata is the clearest early service leader. His ability lies in translating collective demands into forms people can inhabit without humiliation. His universal protection ethic produces real legitimacy but also a structural limit: he has difficulty granting one person exclusive priority or accepting conflict as unavoidable.

## Kushida Kikyō

Her social labor is real and politically valuable. Her private hostility does not erase the classwide effects of her memory, mediation, and credibility. The tension between the public and private selves remains unresolved rather than solved by simply calling one false.

## Sudō Ken

He is becoming the strongest early example of developmental ability. Athletic capacity is increasingly legible, and the possibility of converting it into class value is explicit. Emotional regulation and academic durability remain open.

## Sakura Airi

The Shizuku identity demonstrates authored visibility rather than a simple false-self/true-self split. She becomes more capable when relationships and media reduce the cost of expression. Her ability to reject Yamauchi while accepting Ayanokōji’s presence provides one of the tranche’s clearest low-coercion autonomy models.

## Ryūen Kakeru

His political system centralizes information, fear, and decision. His rejection of trust gives him speed and control but also makes his resource use and personal presence more predictable. His search for the hidden island author has begun.

## Ichinose Honami

She represents voluntary legitimacy, bounded openness, and a political willingness to help rivals when the rule system itself is at stake. She is strategically perceptive and capable of deception without treating coercion as her primary method.

# 5. Relationship-state reconciliation

The checkpoint relationship ledger distinguishes public form, private form, leverage, refusal capacity, dependence, and current reciprocity. The most consequential current relationships are:

## Ayanokōji–Horikita

- publicly: ordinary classmates with Horikita increasingly treated as visible leader;
- privately: low-pressure conversation, strategic dependence, and growing trust;
- asymmetry: Ayanokōji understands and authors more of the environment than Horikita knows;
- current status: functional alliance with emerging personal concern, not equal partnership.

## Ayanokōji–Kei

- publicly: nearly no meaningful relationship;
- privately: coerced protected collaboration;
- leverage: trauma knowledge, exposure risk, deterrent evidence, and promised safety;
- refusal capacity: weak;
- current status: high operational value and growing private disclosure, but reciprocity remains structurally incomplete.

## Ayanokōji–Airi

- public/private: quiet friendship formed through recognition and support;
- leverage: low;
- refusal capacity: comparatively strong;
- current status: one of the clearest examples that Ayanokōji can support autonomy without deciding the outcome.

## Kei–Hirata

- public: romantic relationship;
- private: protective social fiction;
- leverage: Hirata’s status protects Kei, but he does not demand private control;
- current status: ethically bounded but unable to provide the exclusive retaliation/protection Kei wants.

## Horikita–Sudō

- movement: contempt → domain recognition → conditional developmental respect;
- current status: asymmetrical but no longer static.

## Horikita–Kushida

- public cooperation and structural complementarity coexist with private hostility whose origin remains unresolved.

# 6. Institution and examination reconciliation

The institution/examination ledger now tracks the following systems:

1. **first-month class-point evaluation** — hidden behavioral criteria convert apparent freedom into collective economic judgment;
2. **midterm/point purchase** — academic survival, information markets, and private points become linked;
3. **Sudō adjudication** — event truth, evidence, credibility, and class reputation diverge;
4. **class-transfer price** — twenty million private points make mobility explicitly purchasable;
5. **deserted-island exam** — ecological ability, scarce resources, leader identity, and social legitimacy become measurable;
6. **zodiac exam** — trust, device identity, and betrayal are priced directly;
7. **school phones/location visibility** — infrastructure serves both care and surveillance;
8. **campus isolation** — family separation can function as deprivation for one student and refuge for another;
9. **student council** — formal office is separated from the actual ability of the officeholder.

The school increasingly appears not merely to measure students but to create markets and information asymmetries through which they become measurable.

# 7. Terminology and concept reconciliation

The exact-language passage index has been reconciled into thematic clusters.

## Ability and evaluation

- `平等`
- `実力`
- `実力至上主義`
- `不良品`
- `修理`
- `進歩`
- `成長`
- `シンキング`
- `場を支配する力`

## Freedom, authorship, and control

- `自由`
- `自由を守るために自由を捨てる`
- `手のひらで転がした`
- `道具`
- `目と耳`
- `命令だ`
- `本当の所有者`

## Relationship and dependence

- `友達`
- `仲間`
- `信頼`
- `寄生虫`
- `守る`
- `偽りの強者`
- `ありがとう`

## Truth, proof, and record

- `証拠能力`
- `証明力`
- `嘘を真実に変えた`
- `録画`

## Selfhood and ordinary life

- `偽りの仮面`
- `私じゃなくなって、私になる`
- `生まれたばかり`
- `まだ液状`
- `真っ白`
- `孤独なのだ`
- `今日は意外と楽しかったわ`

The terminology ledger records how these terms change cumulatively rather than assuming one translation or meaning remains stable across the series.

# 8. Evidence-state conclusions and unresolved tensions

## 8.1 Conclusions now strong enough to carry forward

1. Ayanokōji’s ordinary adolescent desires are textual fact, not merely external humanization.
2. His public mediocrity is deliberately authored.
3. Horikita’s early growth is genuine but materially scaffolded by Ayanokōji and others.
4. Class D’s central problem is conversion and integration of heterogeneous ability.
5. Kei possesses significant social and political ability beyond her self-description as parasite.
6. Hirata’s protection and Ayanokōji’s protection are structurally different, not merely more or less effective versions of the same act.
7. Trust, reputation, privacy, and device identity already function as political resources.
8. Ordinary-life scenes are necessary evidence for freedom, preference, and self-formation.
9. Successful protective outcomes do not erase coercion, complicity, or lack of consent.
10. Ayanokōji already possesses lower-coercion methods, making his selection among methods ethically significant.

## 8.2 Questions that remain locally open

The checkpoint preserves rather than answers:

- what environment produced Ayanokōji’s ability;
- the truth and extent of Chabashira’s paternal-expulsion claim;
- the complete basis of class assignment;
- why Hirata is in Class D;
- the origin and full danger of Kushida’s hostility toward Horikita;
- whether Horikita can become a leader without hidden correction;
- whether Kei’s collaboration can increase her independent refusal capacity;
- whether Ayanokōji’s ordinary attachments will constrain his tools logic;
- how Ryūen’s search for the hidden strategist will develop;
- what Nagumo’s rise will change in the student council;
- whether the school’s enclosure is primarily developmental, protective, exploitative, or some unstable combination.

## Audit disposition

> **PASS**

All evidence, locator, provenance, structural, and package checks required at this checkpoint have passed. The Volume 4.5 reconstruction remains explicitly qualified as source-grounded rather than byte-identical recovery.

# 9. Checkpoint outputs

This reconciliation produces or updates:

- `checkpoints/COTE_Y1_CHECKPOINT_01_RECONCILIATION_Y1V01_TO_Y1V04_5.md`;
- `ledgers/COTE_CHAR_LEDGER_AYANOKOJI_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_CHAR_LEDGER_HORIKITA_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_CHAR_LEDGER_CLASS_CORE_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_CHAR_LEDGER_RIVALS_LEADERS_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_CHAR_LEDGER_SENIORS_ADULTS_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_RELATIONSHIP_LEDGER_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_INSTITUTION_EXAM_LEDGER_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_THEME_TERMINOLOGY_LEDGER_THROUGH_Y1V04_5.md`;
- `ledgers/COTE_CLASS_POLITY_LEDGER.md`;
- `support/COTE_Y1_LONGITUDINAL_THREAD_REGISTRY.md`;
- `support/COTE_Y1_CHECKPOINT_01_RECONCILIATION.json`;
- refreshed corpus manifest, index, status, delivery audit, and checksums;
- a clean checkpoint ZIP excluding copyrighted EPUBs.

Package targets:

- `COTE_Y1_CHECKPOINT_01_V01_TO_V04_5_RECONCILED.zip`;
- `COTE_Y1_CHECKPOINT_01_V01_TO_V04_5_RECONCILED.zip.sha256`.

# 10. Handoff to Volume 5

The next volume should begin from the reconciled state rather than from an undifferentiated memory of Volumes 1–4.5.

The principal inherited analytical targets are:

1. whether public physical performance changes Ayanokōji’s legibility;
2. whether Horikita can translate private growth into visible class leadership;
3. whether Sudō’s athletic capacity becomes socially usable under public pressure;
4. how class solidarity behaves when physical competition, status, and humiliation become visible;
5. whether Ayanokōji’s intervention style changes when the decisive events occur publicly rather than in controlled private spaces;
6. how the school’s theory of `実力` changes when embodied performance becomes central.

The next canonical artifact is:

`volumes/COTE_Y1_V05_DEEP_READING.md`

# Related artifacts

- [Volume 1](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y1_V01_DEEP_READING.md)
- [Volume 2](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y1_V02_DEEP_READING.md)
- [Volume 3](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y1_V03_DEEP_READING.md)
- [Volume 4](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y1_V04_DEEP_READING.md)
- [Volume 4.5](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y1_V04_5_DEEP_READING.md)
- [Cumulative evidence ledger](../03%20Rolling%20Ledgers/COTE_Y1_12_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md)
- [Japanese terminology and passage index](../03%20Rolling%20Ledgers/COTE_Y1_13_JAPANESE_TERMINOLOGY_AND_PASSAGE_INDEX.md)
