---
corpus: NANA_JP_DEEP_READING
work: "NANA"
work_ja: "NANA"
author: "矢沢あい"
document: analytical_method
version: "2.0"
date: "2026-08-11"
primary_language: ja
source_type: manga
source_format: image_epub
primary_scope: "Japanese tankōbon Volumes 1-21; post-Volume-21 chapters when supplied; paratext later"
analysis_mode: sequential_first_pass
spoiler_policy: strict_publication_order
canonical_volume_filename: "NANA_VXX_DEEP_READING.md"
artifact_prefix: "NANA_"
---

# NANA — Analytical Method and Reading Protocol v2
## Japanese-original sequential close reading with provenance, source tracking, and synthesis traceability

## 1. Purpose

This document supersedes the first *NANA* analytical charter while preserving its interpretive commitments.

The project remains a sequential, Japanese-original close reading of Ai Yazawa's 『NANA』. The primary objective is still to understand the manga as a sequence of lived relationships whose meanings change over time, rather than beginning from a predetermined thesis and collecting confirming examples.

Version 2 adds an archival and evidentiary architecture designed to make every major conclusion retrievable later.

The governing interpretive principle remains:

> **Read *NANA* first as a sequence of lived relationships, not as a collection of themes waiting to be identified.**

The governing provenance principle is now:

> **Every load-bearing analytical claim should be traceable from synthesis → canonical analytical artifact → evidence entry → primary-source locator → original Japanese page.**

This method is therefore designed to produce two things simultaneously:

1. a self-contained literary analysis of every volume; and
2. a durable evidence system from which later multi-document synthesis can be written without reconstructing the source trail from memory.

---

# 2. What v2 changes

Version 2 adds the following requirements to the existing method:

- canonical per-volume Markdown artifacts;
- standardized YAML metadata for Library retrieval;
- source-file identifiers, page counts, and checksums where available;
- a source/structure audit at the beginning of every volume;
- an Evidence Classification Ledger;
- a Primary-Source Locator Ledger;
- explicit hypothesis stress-testing and counterevidence;
- a formal prospective-versus-retrospective reading split;
- standardized cumulative-ledger updates;
- stable evidence IDs;
- corpus-wide naming conventions;
- a Library search/retrieval strategy;
- raw-source cold-storage and selective reintroduction rules;
- and a final synthesis traceability chain.

The key adaptation from the *My Hero Academia* second-pass architecture is archival rather than epistemic.

*MHA* second pass can use full-series hindsight by design. The *NANA* project currently **must not**. *NANA* remains a spoiler-bounded first-pass reading through each volume in publication order. Later reinterpretation is allowed only in explicitly labeled retrospective correction fields after the later evidence has actually been analyzed.

---

# 3. Source hierarchy

## Tier 1 — Original Japanese manga page

The governing source is the original Japanese page as published in the supplied tankōbon image EPUB.

Interpretation must privilege the complete page:

- dialogue;
- narration;
- thought text;
- handwritten text;
- sound effects when meaningful;
- speech-balloon shape;
- panel composition;
- faces;
- gaze;
- gesture;
- clothing;
- props;
- page turns;
- silence;
- negative space;
- and sequential juxtaposition.

Extracted or machine-readable text may support searching, but it is not the governing source when the page itself is available.

> **OCR is a retrieval aid, not quotation-grade evidence.**

## Tier 2 — Collected-volume apparatus

Covers, chapter art, author notes, 「淳子の部屋」, bonus pages, advertisements with contextual value, and other included material should be inspected and classified.

They may provide:

- editorial framing;
- visual emphasis;
- tonal counterpoint;
- self-parody;
- publication context;
- or character marketing.

They do not automatically possess equal canonical weight with mainline narrative pages.

## Tier 3 — Official paratext

*NANA 7.8* and later official books should be read after the relevant main narrative unless a narrow factual question requires earlier consultation.

Separate:

- documentary information;
- editorial characterization;
- Yazawa commentary;
- cultural reference material;
- publication-era metatext.

The rule remains:

> **What the manga demonstrates outranks what supplementary material summarizes.**

## Tier 4 — Adaptations

The anime receives a later independent adaptation pass.

Anime dialogue, voice acting, music, pacing, and staging are evidence for the anime's interpretation of *NANA*, not retroactive evidence for what the manga itself establishes.

## Tier 5 — External criticism and reception

Academic, feminist, queer, fashion, music, Japanese popular criticism, reviews, and fandom interpretation should be brought in after substantial independent close reading.

Use criticism as a challenge set rather than an interpretive authority.

---

# 4. Canonical corpus naming

Every durable artifact must use a stable filename.

## Per-volume analyses

```text
NANA_V01_DEEP_READING.md
NANA_V02_DEEP_READING.md
...
NANA_V21_DEEP_READING.md
```

## Post-Volume-21 continuation

Once Chapters 81–84 are supplied in Japanese, use either one chapter-range artifact or individual chapter artifacts depending on source packaging:

```text
NANA_CH081_084_CONTINUATION_DEEP_READING.md
```

or

```text
NANA_CH081_DEEP_READING.md
...
NANA_CH084_DEEP_READING.md
```

Do not call this material "bonus" or "supplemental." It is continuation of the primary narrative.

## Method and global ledgers

Recommended names:

```text
NANA_ANALYTICAL_METHOD_V2.md
NANA_MASTER_SOURCE_INVENTORY.md
NANA_EVIDENCE_INDEX.md
NANA_PRIMARY_SOURCE_LOCATOR_INDEX.md
NANA_CHARACTER_STATE_LEDGER.md
NANA_RELATIONSHIP_STATE_LEDGER.md
NANA_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md
NANA_HOME_AND_MATERIAL_LIFE_LEDGER.md
NANA_NARRATION_AND_TEMPORAL_LEDGER.md
NANA_MOTIF_AND_LEXICAL_INDEX.md
NANA_OPEN_QUESTIONS_AND_HYPOTHESES.md
NANA_RETROSPECTIVE_CORRECTION_LOG.md
```

These do not all need to be separately emitted after every volume. The canonical per-volume document contains the entries required to reconstruct them later.

---

# 5. Standard YAML metadata

Every canonical volume analysis begins with YAML front matter.

Minimum schema:

```yaml
---
corpus: NANA_JP_DEEP_READING
work: NANA
author: 矢沢あい
volume: 01
chapters: "..."
chapter_titles:
  - "..."
analysis_pass: 1
primary_language: ja
source_type: manga
source_format: image_epub
source_edition: japanese_tankobon
source_file: "Nana - Volume 01 [Japanese].epub"
source_sha256: "..."
source_spine_pages: 191
primary_source_verified: true
spoiler_scope: "through Volume 01 only"
method: "NANA_ANALYTICAL_METHOD_V2"
provenance_status: full
major_characters:
  - ...
major_relationships:
  - ...
major_topics:
  - ...
major_visual_motifs:
  - ...
major_lexical_targets:
  - ...
cumulative_status:
  - strengthened
  - complicated
  - revised
---
```

Use metadata to improve Library search, not to replace prose.

Do not invent chapter titles, page counts, hashes, or locators. If a field has not been verified, use:

```yaml
field_name: null
```

or omit it.

---

# 6. Source and structure audit

Before literary analysis, establish the source object.

Record:

- exact source filename;
- format;
- page/spine count;
- checksum when available from the integrity manifest;
- chapter list and titles;
- chapter-opening locations;
- included bonus material;
- duplicated or blank structural pages;
- packaging anomalies;
- metadata-language anomalies;
- and whether the source is suitable for Japanese linguistic analysis.

For the existing corpus, the package metadata's `zh-CN` language declaration does not override the visibly Japanese manga pages.

The page image is the language authority.

---

# 7. Sequential spoiler discipline

The first-pass analysis of Volume N may use only:

- Volumes 1 through N already analyzed;
- earlier canon material already encountered in publication order;
- the current volume's included paratext, appropriately classified.

It must not use later manga developments to settle:

- motive;
- relationship status;
- paternity;
- future residence;
- death;
- disappearance;
- marriage;
- sexuality;
- career outcome;
- or the meaning of future-narration fragments.

The analysis may say:

> "This may be foreshadowing."

It may not say:

> "This proves the later event"

until the later event has actually been analyzed.

---

# 8. Prospective and retrospective modes

The v2 method makes the two modes explicit.

## Prospective reading

This is the default per-volume mode.

Ask:

> What can a careful reader know here, now?

Prospective reading controls the main body of every volume artifact.

## Retrospective correction

When later analyzed material changes an earlier conclusion, record the change in the later volume's cumulative-delta section and eventually in:

```text
NANA_RETROSPECTIVE_CORRECTION_LOG.md
```

Use labels such as:

- strengthened;
- refined;
- weakened;
- overturned;
- reclassified;
- still unresolved.

Do not silently rewrite the historical analysis.

The purpose is to preserve what the earlier evidence genuinely supported at the time.

---

# 9. Multi-pass workflow for every volume

## Pass 0 — Integrity and structure

1. Confirm the EPUB opens.
2. Confirm the reading spine.
3. Map chapter starts and extras.
4. Record page count, source hash, and anomalies.
5. Establish the spoiler boundary.

## Pass 1 — Spoiler-bounded linear read

Read in spine order.

Capture:

- event sequence;
- time and place;
- entrances and exits;
- living arrangements;
- work developments;
- confessions;
- lies;
- promises;
- refusals;
- sexual encounters;
- money transfers;
- objects exchanged;
- relationship changes;
- future-narration passages;
- and unanswered questions.

Do not solve ambiguity prematurely.

## Pass 2 — Causal and formal reconstruction

Build:

- chapter map;
- concise causal synopsis;
- opening/closing comparison;
- information-distribution map;
- major page-turn effects;
- visual architecture;
- domestic-space changes;
- and chronology.

## Pass 3 — Character, relationship, and voice reading

Update:

- Nana Osaki state;
- Komatsu Nana/Hachi state;
- supporting character states;
- relationship-state dossiers;
- Japanese voice profiles;
- address and nickname changes;
- and narrator/focalization distinctions.

## Pass 4 — Material, social, ethical, and thematic reading

Analyze:

- money;
- work;
- housing;
- gender;
- marriage;
- sexuality;
- consent;
- coercion;
- artistic vocation;
- celebrity;
- fashion;
- family;
- and social expectations.

Separate:

- causal effectiveness;
- emotional effect;
- ethical legitimacy;
- psychological plausibility;
- and thematic force.

## Pass 5 — Adversarial rereading

Challenge the preferred thesis.

At minimum ask:

1. What evidence does the current interpretation fail to explain?
2. Am I turning a recurring object into a symbol too early?
3. Am I treating Hachi's retrospective narration as omniscient?
4. Am I mistaking Nana's self-presentation for stable self-knowledge?
5. Am I using modern ethical vocabulary in a way that erases the period setting?
6. Am I using social context to excuse conduct rather than explain it?
7. Am I treating attraction, dependency, possession, protection, and love as synonyms?
8. Am I treating visual romanticization as moral approval?
9. Am I forcing Nana/Hachi into either "only friendship" or "secret canonical romance"?
10. Am I allowing later information to leak backward?
11. Is a character's material constraint being erased by an abstract moral judgment?
12. Which competing interpretation deserves to remain live?

## Pass 6 — Provenance audit

For every load-bearing claim:

1. assign or verify an evidence ID;
2. identify the relevant chapter;
3. record the EPUB spine-page locator;
4. record printed page number when visible and stable;
5. add a short Japanese anchor where useful;
6. classify the evidence;
7. link the claim to character/relationship/motif tags.

No invented locator is better than a false locator.

## Pass 7 — Cumulative delta

State exactly what the volume changes.

Record:

- new facts;
- revised character states;
- relationship changes;
- motifs strengthened or weakened;
- lexical patterns;
- earlier hypotheses revised;
- unresolved questions;
- and evidence reserved for future synthesis.

---

# 10. Character-state method

For every materially affected character, ask:

- What do they want?
- What do they believe is happening?
- What are they afraid of?
- What are they refusing to admit?
- What do they know?
- What do they not know?
- What changed?
- What remains unresolved?
- What does the visual presentation reveal that their speech does not?
- What does their language reveal that plot summary would miss?

The cumulative dossier should eventually track:

- identity/social position;
- desire;
- fear;
- known history;
- current relationships;
- voice markers;
- material conditions;
- sexual/romantic history;
- relationship to home;
- relationship to work/art;
- self-image;
- others' perceptions;
- defensive strategies;
- ethical tendencies;
- recurring visual motifs;
- and unresolved questions.

Historical states must be preserved.

Late-series characterization must not erase early-state uncertainty.

---

# 11. Relationship-state method

Relationship categories are descriptive tools, not permanent labels.

For each major dyad, track both sides separately.

Core dossiers include:

- Nana / Hachi;
- Nana / Ren;
- Hachi / Shoji;
- Hachi / Nobu;
- Hachi / Takumi;
- Nana / Yasu;
- Shin / Reira;
- Ren / Reira;
- Nana / BLAST;
- Hachi / the 707 network.

Track, where applicable:

> attraction → intimacy → expectation → obligation → dependence → jealousy → possession → rupture → repair → transformation

Also record:

- what each person calls the relationship;
- what each believes it promises;
- what the other provides;
- what is freely chosen;
- what is materially constrained;
- what leaving would cost;
- and what remains unspoken.

---

# 12. Japanese voice and address ledger

Each major character should acquire a cumulative voice profile.

Track only linguistically meaningful features:

- first-person forms;
- second-person forms;
- names/nicknames;
- honorifics;
- omission of honorifics;
- formality;
- feminine/masculine fictional register;
- sentence endings;
- contractions;
- slang;
- imperatives;
- requests;
- pseudo-requests;
- apologies;
- hedging;
- evasions;
- register shifts;
- and relationship-specific speech.

Special targets:

## Hachi

Distinguish present-event Hachi from retrospective narrator Hachi.

## Nana Osaki

Track when roughness functions as identity, humor, intimacy, armor, jealousy, or collapse.

## Takumi

Track conversational power:

- interruption;
- assumed answers;
- command forms;
- decision announcements;
- practical planning;
- reassurance;
- sexual language;
- infantilization;
- and the conversion of preference into apparent inevitability.

## Ren / Nobu / Yasu / Shin

Do not collapse them into generic masculine speech.

Use language to compare models of:

- authority;
- vulnerability;
- intimacy;
- protectiveness;
- dependence;
- and emotional disclosure.

---

# 13. Narration and temporal ledger

Every retrospective passage should record:

1. speaker;
2. apparent narrating time;
3. addressee;
4. tense/aspect;
5. temporal deixis;
6. emotional register;
7. knowledge implied;
8. knowledge actually confirmed;
9. images attached to the narration;
10. repeated wording;
11. evidentiary status.

Track language such as:

- あの時;
- あの日;
- 今;
- もう;
- ずっと;
- いつか;
- きっと;
- もし;
- 忘れる;
- 覚えている;
- 戻る;
- 会う.

The long-term goal is not merely to claim that *NANA* is nostalgic, but to show exactly how the manga formally causes the present to feel already lost.

---

# 14. Visual and manga-form method

Analyze at four scales.

## Panel

- gaze;
- face;
- posture;
- hands;
- touch;
- distance;
- clothing;
- props;
- foreground/background relation.

## Page

- panel density;
- whitespace;
- page hierarchy;
- silent panels;
- visual interruption;
- page-turn reveal;
- repetition.

## Scene

Track the function of:

- 707;
- bedrooms;
- bars;
- hotels;
- rehearsal rooms;
- restaurants;
- cars;
- train stations;
- workplaces;
- family houses;
- concert venues;
- backstage spaces.

## Series

Track recurring objects without declaring symbolism prematurely:

- keys;
- doors;
- windows;
- beds;
- tables;
- food;
- cigarettes;
- phones;
- photographs;
- flowers;
- jewelry;
- clothing;
- instruments;
- luggage;
- gifts.

Use:

> recurrence → contextual comparison → functional pattern → interpretation

---

# 15. Home and material-life ledger

For every major domestic space, record:

- ownership/lease;
- rent;
- who pays;
- who has keys;
- who enters without asking;
- who cooks;
- who cleans;
- who waits;
- who sleeps there;
- whose belongings accumulate;
- who makes decisions;
- who calls it home;
- who leaves;
- whether return remains possible.

For material life, track:

- wages;
- employment;
- unemployment;
- gifts;
- transportation;
- food;
- clothing;
- professional costs;
- music contracts;
- management;
- housing;
- marriage;
- pregnancy;
- childcare;
- career interruption;
- celebrity wealth;
- and dependence.

Never reduce an adult decision to:

> "Who does she love more?"

Also ask:

> What choices are materially possible?

---

# 16. Sexuality, consent, coercion, and power

Analyze significant sexual encounters individually.

Distinguish:

- desire;
- initiation;
- explicit consent;
- acquiescence;
- reluctance;
- pressure;
- intoxication;
- age;
- financial exchange;
- professional power;
- dependency;
- verbal refusal;
- bodily resistance;
- coercion;
- assault.

Later love, marriage, dependence, affection, or defense does not retroactively establish consent to an earlier act.

Abuse does not require pretending every affectionate experience inside the relationship was psychologically false.

For coercive control, track:

- information;
- isolation;
- money;
- housing;
- reproduction;
- sexual access;
- jealousy;
- professional leverage;
- social legitimacy;
- reassurance;
- threats;
- and decision-making.

For age/power-asymmetric relationships, separate:

> textual depiction / character interpretation / visual romanticization / narrative consequence / ethical judgment

---

# 17. Gender, social scripts, and period context

The relevant social world is turn-of-the-century Japan.

Introduce historical context only when it changes interpretation.

Potential domains:

- women's work;
- marriage;
- pregnancy;
- reproductive expectation;
- young-adult housing;
- Tokyo migration;
- mobile-phone culture;
- nightlife;
- music-industry structures;
- fashion subcultures;
- celebrity journalism;
- youth labor;
- gendered adulthood.

Context explains.

It does not excuse.

It also does not replace the manga.

---

# 18. Queer and relational ambiguity

Do not begin from either:

> "Nana and Hachi are only friends"

or:

> "Nana and Hachi are secretly a canon couple."

Track:

- narrative centrality;
- intimacy;
- jealousy;
- touch;
- domesticity;
- address;
- separation anxiety;
- possessiveness;
- retrospective narration;
- visual pairing;
- comparison with canonical romances.

The strongest final conclusion may be structural:

> **Does Nana/Hachi occupy the narrative and emotional position normally reserved for a central romance, regardless of categorical label?**

Let the evidence decide.

---

# 19. Music, celebrity, and fashion

## Music/industry

Track:

- artistic motive;
- composition;
- band hierarchy;
- professional management;
- contracts;
- media image;
- touring;
- fan relation;
- privacy;
- press;
- commercial compromise.

Separate:

> music as personal expression

from

> music as industry.

## Fashion

Treat clothing as character authorship.

Track:

- silhouette;
- repeated pieces;
- changes;
- public/private clothing;
- subcultural meaning;
- gender presentation;
- aspiration;
- wealth;
- gifts/borrowing;
- jewelry;
- Vivienne Westwood;
- punk lineage.

Ask:

> **What does the character's body become when dressed this way, in this scene, for this observer?**

---

# 20. Evidence Classification Ledger

Every canonical volume artifact ends with a compact evidence ledger.

Use stable IDs:

```text
NANA_V01_E001
NANA_V01_E002
...
```

Recommended fields:

| ID | Location | Japanese anchor | Evidence/function | Class | Epistemic status | Tags |
|---|---|---|---|---|---|---|

## Evidence classes

- **TF — Textual fact:** directly shown or unambiguously stated.
- **SI — Strong inference:** multiple independent signals make alternatives unlikely.
- **TI — Thematic interpretation:** analytical synthesis built from textual evidence.
- **CB — Character belief:** what a character believes; not automatically narrative fact.
- **UA — Unresolved ambiguity:** intentionally or evidentially unsettled.
- **FP — Prospective/foreshadowing signal:** suggests a later development without establishing it.
- **RC — Retrospective correction:** later analyzed evidence changes an earlier entry.
- **VJ — Value judgment:** normative or critical evaluation by the analysis.

## Epistemic status

Preserve the project's existing A–E confidence system:

- **A — directly established**
- **B — strongly established**
- **C — strongly implied**
- **D — plausible inference**
- **E — speculation/theory**

Character belief remains separately marked as `CB`.

This two-axis system prevents "directly quoted character belief" from being confused with "objective fact."

---

# 21. Primary-Source Locator Ledger

Every load-bearing evidence entry should have a retrievable primary locator.

For image EPUBs use:

1. volume;
2. chapter;
3. EPUB spine-page index;
4. printed page number when visible and verified;
5. source filename;
6. short Japanese anchor;
7. optional surrounding-page range.

Recommended row:

| Evidence ID | Chapter | EPUB spine page | Printed page | Source file | Japanese anchor | Verification note |
|---|---|---:|---:|---|---|---|

Example format only:

```text
NANA_V03_E017 | Ch. 5 | spine p. [verified] | [printed if visible] |
Nana - Volume 03 [Japanese].epub |
「かなり恋に近い」 |
Future Hachi retrospectively classifies her admiration for Nana.
```

Do not guess the page number from memory.

If not re-opened and verified, use:

```text
locator_status: pending_backfill
```

A missing locator is a known gap.

A false locator corrupts the corpus.

---

# 22. Hypothesis stress-testing

Every volume must preserve at least one credible counterreading where the text supports it.

For major hypotheses record:

- preferred interpretation;
- evidence supporting it;
- evidence against it;
- alternative explanation;
- what future evidence would discriminate among them.

Examples:

> Is Hachi's behavior dependence, domestic vocation, fear of abandonment, or some combination?

> Is Nana's independence self-authorship, armor, or both?

> Is a scene romantically coded, sexually coded, friendship-coded, or deliberately multivalent?

> Is Takumi's competence care, control, or both depending on context?

The method should resist theories that become unfalsifiable.

---

# 23. Required per-volume artifact structure

The default canonical artifact uses 21 functions.

Headings may merge where a volume's form requires it, but the functions must remain.

```markdown
---
[YAML metadata]
---

# 『NANA』Volume N Deep Reading
## [Interpretive subtitle]

## 1. Central thesis and volume role
## 2. Source integrity, edition, and chapter map
## 3. Narrative architecture and causal close read
## 4. Nana Osaki — character-state update
## 5. Komatsu Nana / Hachi — character-state update
## 6. Other materially affected characters
## 7. Relationship-state changes
## 8. Japanese voice, address, and translation-sensitive language
## 9. Narration, time, memory, and information distribution
## 10. Visual/formal analysis
## 11. Home and domestic-space ledger
## 12. Material and economic adulthood
## 13. Music, celebrity, industry, and fashion
## 14. Gender, sexuality, and social scripts
## 15. Ethics, consent, coercion, care, and power
## 16. Motif and lexical tracking
## 17. Counterreadings, limitations, and hypothesis stress-test
## 18. Evidence Classification Ledger
## 19. Primary-Source Locator Ledger
## 20. Cumulative delta and retrospective-correction status
## 21. Volume thesis and questions carried forward
```

Do not pad simple volumes with empty prose merely to satisfy headings.

A merged section should note which required functions it covers.

---

# 24. Cumulative ledgers

Across the project maintain these analytical streams:

1. master chronology;
2. Nana Osaki character-state ledger;
3. Hachi character-state ledger;
4. supporting-character trajectory ledger;
5. relationship-state matrix;
6. Japanese voice/address matrix;
7. narration/temporal ledger;
8. home/domestic-space ledger;
9. money/work/material-life ledger;
10. sexuality/consent/coercive-control ledger;
11. music/industry/celebrity ledger;
12. fashion/object ledger;
13. motif/lexical index;
14. evidence ledger;
15. source locator ledger;
16. open-question/competing-hypothesis register;
17. retrospective correction log.

The per-volume artifacts are the durable source from which these can later be compiled.

---

# 25. Library retrieval strategy

The artifacts should be easy to find without remembering exact titles.

Every volume document should include:

- exact canonical filename;
- volume number;
- chapter range;
- major character names in English and Japanese when practical;
- major relationship names;
- key Japanese lexical anchors;
- important motifs;
- source filename;
- evidence IDs.

Good search targets should therefore work:

```text
NANA V03 恋に近い Hachi Nana
NANA V02 707 privacy locks
NANA V01 東京 Ren departure
NANA Takumi command imperatives
NANA 707 home table chairs
```

The metadata exists to make later synthesis and targeted retrieval cheap.

---

# 26. Raw-source cold storage and selective reintroduction

Once a volume has:

- a complete canonical deep-reading artifact;
- verified source metadata;
- a locator ledger;
- and sufficient short Japanese anchors,

the raw EPUB does not need to remain constantly loaded for every later synthesis task.

However, the raw source remains the final authority.

When a synthesis claim is contested, quotation-sensitive, visually dependent, or unusually important:

1. retrieve the canonical analytical artifact;
2. identify evidence IDs;
3. follow the locator;
4. selectively reintroduce the original volume;
5. verify the page;
6. then write the final claim.

This allows a large corpus to remain auditable without requiring all raw manga files to be simultaneously active.

---

# 27. Periodic synthesis

Do not wait until the end for all synthesis.

Use natural narrative transitions rather than rigid volume-count checkpoints.

A checkpoint should summarize:

- current character architecture;
- current relationship map;
- current home/material structure;
- Japanese voice findings;
- temporal/narrative structure;
- motifs;
- strongest current hypotheses;
- counterevidence;
- and unresolved questions.

Checkpoint conclusions remain provisional.

They should cite volume artifact filenames and evidence IDs rather than attempting to replace them.

---

# 28. Supplemental-material phase

After the extant main narrative is analyzed, read official supplements in layers.

For *NANA 7.8* distinguish:

- documentary facts;
- editorial characterization;
- Yazawa commentary;
- cultural material;
- metatext.

Authorial statements are evidence about intention and self-understanding, not a veto over textual interpretation.

Where useful, separate:

> **The manga establishes...**

> **Yazawa states...**

> **A reasonable interpretation is...**

---

# 29. Hiatus and incomplete narrative

The final extant-text synthesis should be titled approximately:

```text
NANA: Full-Series Synthesis Through Chapter 84
```

not "complete-series analysis" unless the narrative is actually completed.

Distinguish:

> trajectory

from

> destination.

The absence of a published ending does not prevent interpretation of what the extant text has already done.

It does prevent unresolved trajectories from being promoted to final outcomes.

---

# 30. Final synthesis traceability

The eventual multi-document synthesis should use a three-layer evidence architecture.

## Layer 1 — Reader-facing synthesis claim

Example:

> 707 becomes a model of home founded through shared routine and bounded access rather than simple ownership.

## Layer 2 — Canonical analytical artifact

Example:

```text
NANA_V02_DEEP_READING.md
NANA_V03_DEEP_READING.md
```

## Layer 3 — Primary evidence

Example:

```text
NANA_V02_E0XX
→ Chapter X
→ EPUB spine page Y
→ original Japanese page
```

For every load-bearing thesis, preserve at least one such chain.

For disputed or translation-sensitive claims, preserve multiple independent chains.

The final corpus should make it possible to move:

> **synthesis → analysis → evidence ID → locator → manga page**

without reconstructing the path from memory.

---

# 31. Quality-control checklist

Before finalizing a volume artifact verify:

- [ ] complete Japanese source read in spine order;
- [ ] chapter map verified;
- [ ] illustrations and bonus pages inspected;
- [ ] source filename/page count/hash recorded when available;
- [ ] spoiler boundary explicit and intact;
- [ ] present-event and retrospective narration distinguished;
- [ ] fact, character belief, inference, and interpretation separated;
- [ ] plot explained causally rather than merely summarized;
- [ ] major character-state changes recorded;
- [ ] relationship states tracked dynamically;
- [ ] Japanese-language observations have interpretive payoff;
- [ ] important visual claims are grounded in inspected pages;
- [ ] material constraints remain visible;
- [ ] sexual/ethical scenes are analyzed individually;
- [ ] period context explains rather than excuses;
- [ ] queer ambiguity is neither denied nor prematurely resolved;
- [ ] at least one serious counterreading is tested;
- [ ] evidence IDs are stable;
- [ ] load-bearing claims have source locators;
- [ ] no locator is guessed;
- [ ] cumulative delta is explicit;
- [ ] open questions are carried forward;
- [ ] the artifact is emitted as canonical Markdown.

---

# 32. Migration rule for Volumes 1–3

Volumes 1–3 were analyzed before v2's full provenance architecture.

Their existing prose should be preserved as historical analytical artifacts rather than silently rewritten.

Migration procedure:

1. emit each existing analysis as a canonical Markdown file;
2. add YAML front matter;
3. add source filename, page count, and checksum from the integrity manifest;
4. mark the artifact as a migrated legacy analysis;
5. do **not** fabricate evidence IDs or page locators from memory;
6. add a provenance note stating whether locator backfill is complete or pending;
7. if exact traceability is later needed, reopen the original EPUB and backfill the locator ledger deliberately.

Recommended metadata:

```yaml
provenance_status: migrated_legacy_analysis
locator_status: pending_backfill
```

Beginning with Volume 4, full v2 provenance should be native rather than retrofitted.

---

# 33. Final methodological principle

The original method ended with the standard:

> **Describe the characters closely enough that contradiction stops looking like inconsistency and begins looking like personhood.**

Version 2 retains that standard and adds another:

> **Record the evidence carefully enough that a later synthesis can recover not only what we concluded, but exactly why we were entitled to conclude it.**

The two standards belong together.

*NANA* requires interpretive subtlety because its people are contradictory.

A durable *NANA* corpus also requires evidentiary discipline because those contradictions are easy to flatten once the reading spans thousands of pages.

The project succeeds only if it preserves both the people and the path back to the pages that made those people legible.
