---
corpus: AOT_JP_DEEP_READING
work: "進撃の巨人"
work_en: "Attack on Titan"
author: "諫山創"
document: analytical_method
version: "2.1"
date: "2026-08-23"
character_modeling_extension: "AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1"
primary_language: ja
source_type: manga
source_format: cbz_image_archive
primary_scope: "Japanese tankōbon Volumes 1-34; official paratext and adaptations only in later, explicitly separated phases"
analysis_mode: sequential_first_pass
spoiler_policy: strict_publication_order
canonical_volume_filename: "AOT_VXX_DEEP_READING.md"
artifact_prefix: "AOT_"
checkpoint_policy: "approximately 25%, 50%, 75%, then complete-series synthesis"
---

# 『進撃の巨人』
## Analytical Method and Reading Protocol v2.1
### Japanese-original sequential close reading with provenance, visual evidence, source tracking, and synthesis traceability

## 1. Purpose

This document establishes the governing method for the authoritative project deep reading of 諫山創's 『進撃の巨人』.

The project proceeds one Japanese tankōbon volume at a time, preserves the reader's knowledge state at each publication boundary, treats the original manga page as the governing evidence, and builds a durable analytical corpus suitable for later checkpoint and full-series synthesis.

The method has two equal objectives:

1. produce a substantial literary, character, visual, political, ethical, and philosophical reading of every volume; and
2. preserve enough provenance that a later synthesis claim can be traced through a canonical analytical artifact to a recoverable Japanese manga location; and
3. preserve enough state-conditioned, relationship-conditioned, low-stakes, and speech-pragmatic evidence that a later character-reconstruction layer can model plausible behavior without converting literary themes into personality stereotypes.

The governing interpretive principle is:

> **Read 『進撃の巨人』 as a sequence of changing epistemic, moral, spatial, bodily, and political problems—not as a solved mythology whose early ambiguities can be overwritten by later answers.**

The governing provenance principle is:

> **Every load-bearing series claim should be traceable from synthesis → canonical volume artifact → evidence entry → source locator → original Japanese manga page.**

The method adapts the most effective archival and evidentiary techniques developed in the NANA, AoButa, and My Hero Academia v2 protocols while remaining specific to the formal and thematic demands of *Attack on Titan*.

---

# 2. Scope and canonical endpoint

The canonical main manga contains **34 tankōbon volumes**. This project therefore uses:

```text
AOT_V01_DEEP_READING.md
...
AOT_V34_DEEP_READING.md
```

The analysis currently proceeds as a sequential first pass. A volume may be reread later, but its first canonical artifact must preserve what was textually available through that volume.

The project distinguishes:

- the original Japanese manga;
- tankōbon-only material and information pages;
- official authorial paratext;
- anime adaptations;
- guidebooks and databooks;
- external criticism, reception, and historical context.

The manga remains primary. Adaptation material may enrich a later comparative phase but may not silently fill manga ambiguities.

---

# 3. Source hierarchy

## Tier 1 — Original Japanese tankōbon page

The governing authority for:

- dialogue;
- narration;
- page order;
- panel composition;
- page turns;
- chapter architecture;
- character expression and posture;
- maps, diagrams, information pages, and visual motifs;
- Japanese lexical and grammatical nuance;
- what the reader knows at a given publication boundary.

When a line, facial expression, panel relation, or page turn matters, the original Japanese page governs.

## Tier 2 — Tankōbon apparatus

Includes:

- volume covers;
- inside covers;
- chapter title pages;
- tables of contents;
- fake previews, joke pages, and recurring paratext;
- military diagrams, maps, equipment notes, and appended information;
- author comments included in the volume.

These materials are evidence, but their function must be classified. A joke page is not automatically diegetic fact. A diagram can clarify military mechanics without functioning as omniscient narration.

## Tier 3 — Official authorial and editorial paratext

Includes interviews, official guidebooks, exhibition notes, and comparable material. These may clarify intention, process, names, or chronology, but they do not replace the manga's formal ambiguity.

Use formulations such as:

> **The manga establishes...**

> **Isayama later states...**

> **A plausible interpretation is...**

## Tier 4 — Anime and other adaptations

Adaptations may be analyzed later for:

- performance and voice;
- music;
- timing;
- color;
- animation staging;
- additions, omissions, or reordered material.

They may not be used to settle a manga-first volume before the adaptation comparison is explicitly activated.

## Tier 5 — External scholarship, criticism, reception, and historical context

Use only when the task explicitly calls for it. External context should explain possibilities, not overwrite the primary text.

---

# 4. Canonical corpus naming

## Per-volume artifacts

```text
AOT_V01_DEEP_READING.md
AOT_V02_DEEP_READING.md
...
AOT_V34_DEEP_READING.md
```

## Checkpoint syntheses

Recommended names:

```text
AOT_CHECKPOINT_25P_V01-V09_SYNTHESIS.md
AOT_CHECKPOINT_50P_V01-V18_OR_V19_SYNTHESIS.md
AOT_CHECKPOINT_75P_SYNTHESIS.md
AOT_FULL_SERIES_SYNTHESIS_V01-V34.md
```

The exact 50% and 75% stopping points may follow natural arc boundaries, but the filename must identify the covered volumes unambiguously.

## Global method and corpus files

```text
AOT_ANALYTICAL_METHOD_V2.md
AOT_CORPUS_MANIFEST.md
AOT_MIGRATION_NOTES.md
AOT_SOURCE_INVENTORY_V01-VXX.md
AOT_CUMULATIVE_LEDGER_V01-VXX.md
AOT_PROJECT_DECISIONS_AND_CHECKPOINT_POLICY.md
AOT_CORPUS_INDEX.json
SHA256SUMS.txt
```

## Stable evidence IDs

Use:

```text
AOT_V01_E001
AOT_V01_E002
...
AOT_V18_E087
```

Once published in a canonical artifact, an evidence ID must not be silently renumbered. If later material changes its classification, preserve the ID and record the correction.

---

# 5. Standard YAML metadata

Every canonical volume artifact begins with YAML front matter.

Minimum schema:

```yaml
---
corpus: AOT_JP_DEEP_READING
work: "進撃の巨人"
work_en: "Attack on Titan"
author: "諫山創"
volume: 01
chapters: "1-4"
chapter_titles:
  - "第1話 二千年後の君へ"
  - "第2話 その日"
  - "第3話 解散式の夜"
  - "第4話 初陣"
analysis_pass: 1
primary_language: ja
source_type: manga
source_format: cbz_image_archive
source_edition: japanese_tankobon_digital_sd
source_file: "Attack on Titan v01 (2010) (Digital SD) (KG Manga).cbz"
source_sha256: "..."
source_images: 194
content_pages: 193
source_integrity: verified
primary_source_verified: true
spoiler_scope: "through Volume 01 only"
method: "AOT_ANALYTICAL_METHOD_V2"
provenance_status: full
locator_status: chapter_complete_page_selective
retrospective_material_imported: false
major_characters:
  - "Eren Jaeger / エレン・イェーガー"
  - "Mikasa Ackerman / ミカサ・アッカーマン"
  - "Armin Arlert / アルミン・アルレルト"
major_relationships:
  - "Eren / Mikasa / Armin"
major_topics:
  - freedom
  - walls
  - home
  - dehumanization
major_visual_motifs:
  - birdcage
  - walls and scale
major_lexical_targets:
  - 自由
  - 駆逐
cumulative_status:
  - established
---
```

Metadata supports Library retrieval. It does not replace prose.

Never invent:

- chapter titles;
- checksums;
- page counts;
- source filenames;
- printed-page numbers;
- image locators;
- quotation wording.

If a field has not been verified, use `null`, omit it, or mark it `pending_backfill`.

---

# 6. Source and structure audit

Before literary analysis, establish the source object.

Record:

- exact filename;
- SHA-256;
- CBZ/ZIP integrity result;
- image count;
- cover count and sequential content-page count;
- internal filename pattern;
- image format and basic resolution consistency;
- chapter range and chapter titles;
- included special chapters;
- information pages, maps, joke previews, and bonus material;
- blank, duplicated, missing, corrupt, or out-of-order pages;
- whether the pages are visibly Japanese and fit for linguistic analysis;
- current spoiler boundary.

A valid archive is not automatically a complete literary source. Structural validity, language fitness, image legibility, and quotation-grade confidence should be recorded separately when necessary.

For manga CBZs, a useful stable locator hierarchy is:

1. volume;
2. chapter;
3. printed tankōbon page when visible and verified;
4. internal CBZ image filename;
5. sequential content-page index;
6. short Japanese anchor phrase;
7. panel or spread description.

---

# 7. Sequential spoiler discipline

A first-pass analysis of Volume N may use only:

- Volumes 1 through N already analyzed;
- earlier canon encountered in publication order;
- the current volume's included paratext, appropriately classified.

It must not use later manga information to settle:

- Titan identity;
- motive;
- allegiance;
- family relationship;
- world geography;
- political history;
- power mechanics;
- memory mechanisms;
- the meaning of a dream or title;
- a character's eventual moral or political destination.

A volume may say:

> **This is a foreshadowing signal.**

It may not say:

> **This proves the later revelation**

until that revelation has entered the analyzed corpus.

When later evidence changes an earlier interpretation, record both:

1. what the earlier volume supported at the time;
2. what the later volume subsequently establishes or recontextualizes.

This preserves narrative experience rather than replacing it with retrospective omniscience.

---

# 8. Prospective and retrospective modes

## Prospective reading

The canonical first-pass artifact asks:

- What can the reader conclude now?
- What categories still appear stable?
- What is suspicious but unresolved?
- What does a character believe?
- Which inference is strongest without later confirmation?

## Retrospective correction

Activated only after later volumes are analyzed. A retrospective correction must:

- cite the later volume;
- preserve the earlier interpretation as historically valid within its boundary;
- classify the change as strengthened, qualified, complicated, weakened, contradicted, or resolved;
- avoid pretending that later inevitability was visible from the beginning.

Use `RC — Retrospective correction` evidence entries and a cumulative correction log.

---

# 9. Multi-pass workflow for every volume

## Pass 0 — Integrity and structure

- verify archive integrity;
- count pages;
- map chapters;
- identify included paratext;
- record source metadata and hash;
- confirm spoiler scope.

## Pass 1 — Spoiler-bounded linear read

Read in page order without reorganizing the volume into later themes too early.

Record:

- causal sequence;
- what each character knows;
- what the reader knows;
- scene transitions;
- chapter openings and endings;
- page-turn revelations;
- questions actively raised by the text.

## Pass 2 — Narrative and spatial reconstruction

Build:

- causal synopsis;
- chapter architecture;
- chronology;
- location and movement map;
- military and logistical situation;
- information-distribution map;
- opening/closing relation.

## Pass 3 — Character, relationship, and voice reading

Update:

- Eren, Mikasa, and Armin;
- the 104th ensemble;
- Survey Corps and military professionals;
- infiltrator/warrior identities;
- family and inherited-history relations;
- speech-register and address-term changes;
- trust, recognition, and betrayal structures;
- low-stakes, ordinary, comic, or domestic behavior when the volume supplies it;
- speech pragmatics that may matter for reconstruction even when they carry little thematic weight;
- relationship- and role-conditioned changes in conduct;
- negative constraints: what the character conspicuously does not do, or what would overstate a crisis-state exception into a baseline.

## Pass 4 — Visual and manga-form audit

Inspect:

- page turns;
- double spreads;
- panel density;
- negative space;
- verticality and scale;
- body fragmentation;
- eyes, faces, mouths, hands, and napes;
- walls, gates, forests, cities, underground spaces, and battle geometry;
- diagrams, maps, and information pages;
- recurring visual rhyme.

## Pass 5 — Thematic, institutional, and ethical reading

Select the active modules:

- freedom and confinement;
- human/Titan ontology;
- personhood and recognition;
- home, return, and inheritance;
- knowledge and controlled history;
- military institutions and state legitimacy;
- choice, regret, and sacrifice;
- violence, dehumanization, accountability, and mercy;
- technology, logistics, architecture, and resource scarcity;
- childhood, trauma, family, and imposed purpose.

Keep separate:

- causal success;
- tactical success;
- operational success;
- strategic success;
- political legitimacy;
- ethical justification;
- psychological plausibility;
- thematic force.

## Pass 6 — Adversarial rereading

Challenge the preferred thesis.

Ask:

1. What evidence does it fail to explain?
2. Is a character belief being mistaken for objective fact?
3. Is an emotionally powerful scene being treated as a complete political or ethical argument?
4. Is a Titan mechanism being over-symbolized?
5. Is symbolism being denied because the mechanism is literal?
6. Is military necessity being allowed to erase consent or cost?
7. Is later knowledge leaking backward?
8. Is a protagonist-centered reading erasing supporting agency?
9. Is a humanizing explanation being mistaken for absolution?
10. Is dehumanizing wartime language being mistaken for settled ontology?
11. Which alternative reading deserves to remain live?
12. What evidence would discriminate between competing hypotheses?

## Pass 7 — Provenance audit

For every load-bearing claim:

- assign an evidence ID;
- classify its epistemic status;
- provide the strongest practical locator;
- include a short Japanese anchor when exact language matters;
- mark missing page-level backfill rather than guessing.

## Pass 8 — Cumulative delta

State exactly what the volume changes:

- new textual facts;
- revised character states;
- relationship-state changes;
- rules confirmed, contradicted, or left open;
- institutions newly legible;
- motifs introduced or transformed;
- earlier hypotheses strengthened or weakened;
- open questions carried forward;
- behavioral-state and decision-pattern deltas relevant to later reconstruction;
- voice/register and ordinary-life evidence newly available or newly contradicted.

---

# 10. Attack on Titan analytical lenses

## 10.1 Narrative architecture

For every volume ask:

- What problem does the volume inherit?
- What new problem replaces it?
- Does the volume complete an operation, begin an arc, reverse an apparent victory, or relocate the central conflict?
- How do chapter titles form an argument?
- What is the relationship between the first and last image or line?
- Which revelation reclassifies earlier material?

Avoid treating a volume as four plot summaries joined together.

## 10.2 Character-state method

Track characters dynamically rather than through fixed adjectives.

For each materially affected character record:

- starting state;
- pressure applied;
- choice made;
- action taken;
- information gained or lost;
- relation altered;
- bodily consequence;
- self-interpretation;
- discrepancy between self-interpretation and textual evidence;
- unresolved contradiction.

High-priority continuity targets include:

- Eren Jaeger;
- Mikasa Ackerman;
- Armin Arlert;
- Jean Kirstein;
- Historia Reiss;
- Ymir;
- Reiner Braun;
- Bertolt Hoover;
- Annie Leonhart;
- Levi;
- Erwin Smith;
- Hange Zoë;
- Connie Springer;
- Sasha Braus;
- the larger 104th and Survey Corps ensemble.

Do not make Eren the center of every volume. Some volumes are primarily about institutions, witnesses, secondary relationships, or opponents.

For reconstruction support, distinguish five different things that are often flattened into a single trait:

1. **stable disposition** — recurring across materially different states;
2. **developmental state** — true at a defined publication boundary but later revisable;
3. **situational delta** — a temporary shift under fear, injury, grief, exhaustion, rage, relief, or acute responsibility;
4. **relationship-conditioned response** — behavior available with one interlocutor or role relation but not necessarily generalizable;
5. **capability/role constraint** — what the character can or must do because of training, office, knowledge, body, or institutional position rather than personality.

When a scene is diagnostically useful for behavior, record the minimum causal tuple:

`state + knowledge + relationship/role + pressure + available alternatives -> response family -> consequence/self-interpretation`

Do not promote a single dramatic scene into a universal behavioral rule.

## 10.3 Relationship-state method

Track relations as changing structures, not labels.

Useful fields:

- public role;
- private attachment;
- trust basis;
- information asymmetry;
- dependency;
- coercion;
- care;
- rivalry;
- betrayal;
- shared objective;
- conflict of objectives;
- present state;
- likely fault line.

The Eren/Mikasa/Armin triad should be continuously tracked without reducing Mikasa and Armin to support functions.

For modeling purposes, relationship evidence is directional. `A -> B` may differ from `B -> A`, and both may change by public/private setting, rank, group presence, injury, secrecy, or crisis state. Record these differences rather than collapsing them into a single relationship adjective.

## 10.4 Freedom and confinement ledger

Track freedom at multiple scales:

- spatial movement;
- bodily autonomy;
- political autonomy;
- informational freedom;
- memory and historical knowledge;
- freedom from inherited role;
- freedom to bind oneself through chosen care;
- freedom as universal birthright;
- freedom as domination of obstacles;
- freedom as shared institution.

Track every major enclosure:

- Walls;
- gates;
- forests;
- cells;
- Titan bodies;
- crystal;
- underground chambers;
- military custody;
- bloodline;
- inherited memory;
- public role;
- ideological command.

## 10.5 Human/Titan ontology and transformation ledger

Keep distinct:

- observed behavior;
- biological inference;
- character theory;
- confirmed rule;
- exception;
- inherited memory;
- transformation trigger;
- body generation;
- regeneration;
- hardening;
- command/control effects;
- transfer hypotheses;
- unresolved mechanism.

Do not let a later explanation flatten the horror or ambiguity of earlier encounters.

## 10.6 Personhood, recognition, and dehumanization

Track:

- who is recognized by face, name, voice, memory, or relationship;
- who is reduced to monster, weapon, vessel, symbol, resource, bloodline, casualty, or statistic;
- whether recognition changes action;
- whether humanization is mistaken for exoneration;
- whether dehumanization becomes tactically useful;
- whether institutions grant or withdraw moral membership.

The series repeatedly distinguishes:

> **understanding a person**

from

> **forgiving the person's actions.**

Preserve that distinction.

## 10.7 Knowledge, memory, and information distribution

Maintain a knowledge-state map for:

- reader;
- Eren;
- Armin;
- Mikasa;
- Survey Corps leadership;
- Military Police;
- Wall religion;
- Reiss family;
- Warrior/infiltrator faction;
- civilians.

Track:

- notebooks;
- keys;
- basements;
- books;
- testimony;
- official narratives;
- censorship;
- memory alteration;
- inherited memory;
- reconnaissance;
- experimentation;
- destroyed evidence;
- strategic secrecy.

Ask who controls interpretation, not only who possesses information.

## 10.8 Institutions, politics, and legitimacy

Separate:

- formal legality;
- coercive capacity;
- informational authority;
- military competence;
- constitutional authority;
- public legitimacy;
- moral legitimacy;
- emergency necessity.

Track:

- Garrison;
- Survey Corps;
- Military Police;
- Central Interior Police;
- monarchy;
- Wall religion;
- merchant and press networks;
- civilian testimony;
- post-coup government;
- enemy command structures.

Never assume:

> the faction pursuing truth automatically deserves unrestricted power.

Never assume:

> institutional secrecy is automatically irrational.

Test claims against conduct and consequences.

## 10.9 Choice, trust, regret, and sacrifice

For every major decision record:

- available information;
- available alternatives;
- time pressure;
- coercive constraints;
- person making the choice;
- people bearing the cost;
- result;
- counterfactual uncertainty;
- retrospective self-interpretation.

Distinguish:

- informed self-sacrifice;
- coerced sacrifice;
- strategic exposure;
- self-erasure through martyrdom;
- chosen relational risk;
- institutional consumption;
- sacrifice remembered as irreplaceable;
- sacrifice retroactively used to justify a project.

Do not use outcome alone to prove a decision was rational or irrational.

## 10.10 Home, return, and inheritance

Track every form of home:

- lost geographic home;
- portable home;
- family relation;
- promised return;
- inherited mission;
- basement/archive;
- political bloodline;
- recovered territory;
- home as recognition across change;
- home as site of monstrosity or concealed history.

Track inheritance in both forms:

- inherited will, care, technique, memory, and responsibility;
- inherited crime, trauma, ideology, enemy, body, and consequence.

Never convert inherited consequence automatically into inherited guilt.

## 10.11 Body, architecture, technology, and logistics

Bodies in *Attack on Titan* function as:

- persons;
- weapons;
- prisons;
- shelters;
- archives;
- architecture;
- military resources;
- evidence;
- transferable vessels.

Track:

- maneuver gear;
- horses;
- gas and blades;
- artillery;
- hardening;
- Walls and gates;
- Titan napes;
- bodily exhaustion;
- supply and food;
- population density;
- evacuation;
- communication networks;
- automated defense.

The series repeatedly proves that courage without logistics does not produce victory.

## 10.12 Japanese language and character voice

Maintain two related but distinct linguistic layers.

**Interpretive language evidence** remains mandatory when wording changes literary, ethical, political, or character interpretation.

**Reconstruction language evidence** should also preserve recurring ordinary speech features even when they have little thematic payoff. These may include:

- habitual self-reference and pronouns;
- address and naming behavior by interlocutor;
- politeness and military-role accommodation;
- turn length and clause density;
- bluntness, hedging, mitigation, qualification, and self-correction;
- questions versus assertions;
- interruption, repetition, ellipsis, commands, and refusals;
- insult, teasing, reassurance, apology, praise, complaint, and disagreement strategies;
- rhetorical abstraction versus concrete practical language;
- register shifts under anger, fear, shame, grief, command, intimacy, exhaustion, or relief.

High-value interpretive targets include:

- pronouns and self-reference;
- address terms;
- military formality;
- shifts between 兵士 and 戦士;
- category words such as 人類, 人間, 巨人, 化け物, 敵;
- freedom vocabulary: 自由, 不自由, 奪う, 取り返す;
- extermination language: 駆逐, 駆除;
- choice and uncertainty: 選択, 結果, 悔い, 信じる;
- sacrifice: 心臓を捧げよ, 切り捨てる;
- home and return: 故郷, 帰る, ただいま, おかえり;
- identity and role: 兵士, 戦士, 王, 神, 器;
- power/mechanism terms: 座標, 始祖の巨人, 硬質化;
- ordinary worth: 特別, 普通, 生まれた.

Do not overread a single particle or sentence ending. Claims about voice require pattern and context. A reconstruction claim may be worth preserving even when it has low thematic payoff, but it should normally require recurrence, a clean relationship contrast, or a clearly bounded state delta.

The manga supports a **written-Japanese idiolect and discourse model**, not an anime vocal-performance model. Do not infer pitch, timbre, breath, timing, muttering, shouted delivery, or seiyuu-specific performance from manga punctuation or typography alone. If an anime-performance layer is later activated, keep it explicitly separate and cross-reference rather than silently merging it into manga authority.

## 10.13 Visual and formal analysis

Treat manga form as evidence, not illustration.

Analyze at four scales.

### Panel

- gaze;
- body angle;
- hands and mouths;
- line weight;
- background suppression;
- scale relation;
- action direction;
- facial continuity or distortion.

### Page

- reading flow;
- reveal timing;
- panel density;
- silence;
- negative space;
- repetition;
- visual interruption.

### Spread

- monumental scale;
- battlefield geography;
- public spectacle;
- relation between tiny human bodies and structures.

### Series

- repeated compositions;
- page-turn reversals;
- visual callbacks;
- role/body inversions;
- Wall imagery;
- tree/forest imagery;
- faces inside bodies;
- mouths as consumption, speech, rescue, and command;
- hands as agency, protection, injury, and transformation.

## 10.14 Callback, foreshadowing, and payoff ledger

Classify:

- setup;
- recurrence;
- reversal;
- payoff;
- recontextualization;
- false lead;
- unresolved thread;
- retrospective correction.

Do not assume every repeated image is deliberate foreshadowing. Test formal and causal support.

## 10.15 Behavioral reconstruction and ordinary-life capture

The literary analysis remains primary. This subsection prevents the project from discarding evidence needed for later character modeling merely because that evidence is mundane.

When present, capture:

- ordinary conversation when no major decision is being made;
- food, sleep, work, training, maintenance, recreation, humor, teasing, irritation, embarrassment, and boredom;
- how a character enters, exits, prolongs, or shuts down conversation;
- help-seeking, refusal, acceptance, repair, apology, and reassurance;
- reactions to being corrected, praised, ignored, mocked, ordered, protected, or depended upon;
- conduct when there is enough time to choose rather than only react;
- behavior in dyads versus groups;
- public-role versus private-role behavior;
- evidence that a famous trait is absent, muted, or overridden in a specific state.

For every reusable behavioral entry, prefer fields such as:

`character | scope | state | relationship/role | trigger/problem | available options | observed response | inhibited alternatives | result | self-interpretation | evidence IDs | confidence`

Absence of low-stakes evidence is a coverage gap, not permission to invent hobbies, preferences, conversational habits, or domestic behavior.

The dedicated downstream architecture is `AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md`. The per-character model schema and validation protocol are subordinate derived-use documents; they never override primary-source or canonical deep-reading authority.

---

# 11. Evidence Classification Ledger

Every canonical volume artifact contains a compact evidence ledger for load-bearing claims.

Use:

| Label | Meaning | Standard |
|---|---|---|
| **TF — Textual fact** | Directly stated or unambiguously shown | Recoverable from a source location |
| **VF — Visual fact** | Directly visible in panel/page composition | Description must match inspected page |
| **SI — Strong inference** | Best explanation of converging evidence | Alternatives considered and materially weaker |
| **TI — Thematic interpretation** | Literary, psychological, political, ethical, or formal synthesis | Supported but not uniquely entailed |
| **CB — Character belief** | Assertion or model held by a character | Never promoted to fact without support |
| **UA — Unresolved ambiguity** | Evidence incomplete or incompatible | Must remain open within current boundary |
| **FP — Foreshadowing/prospective signal** | Suggests a later development without establishing it | Cannot be converted into certainty early |
| **RC — Retrospective correction** | Later analyzed evidence changes an earlier reading | Used only after later source enters corpus |
| **VJ — Value judgment** | Explicit normative or critical evaluation by the analysis | Kept distinct from descriptive fact |

Optional confidence axis:

- **A — directly established**
- **B — strongly established**
- **C — strongly implied**
- **D — plausible**
- **E — speculative**

Recommended row:

| ID | Location | Japanese anchor / visual anchor | Evidence/function | Class | Confidence | Tags |
|---|---|---|---|---|---|---|

Keep quotations short. The purpose is retrieval, not reproduction.

---

# 12. Primary-Source Locator Ledger

Recommended row:

| Evidence ID | Volume | Chapter | Printed page | CBZ image | Sequential page | Japanese anchor / panel description | Verification note |
|---|---:|---|---:|---|---:|---|---|

Use the strongest practical locator.

### Exact lexical claim

- chapter;
- CBZ image when verified;
- short Japanese anchor.

### Scene-level relational claim

- chapter;
- scene description;
- one or more anchors.

### Visual claim

- CBZ image;
- page or spread description.

### Chapter-architecture claim

- chapter range;
- opening and closing scene.

Never guess an image filename or printed page from memory. Use:

```yaml
locator_status: pending_backfill
```

when needed.

A missing locator is an auditable gap. A fabricated locator corrupts the corpus.

---

# 13. Required per-volume artifact structure

The canonical artifact contains 21 functions. Headings may merge when that improves the argument, but the functions must remain.

```markdown
---
[YAML metadata]
---

# 『進撃の巨人』Volume N Deep Reading
## [Interpretive subtitle]

## 1. Central thesis and volume role
## 2. Source integrity, edition, chapter map, and spoiler boundary
## 3. Narrative architecture and causal close read
## 4. Character-state updates
## 5. Relationship, recognition, trust, and betrayal
## 6. Human/Titan ontology and power mechanics
## 7. Freedom, Walls, home, return, and spatial politics
## 8. Institutions, military systems, state power, and legitimacy
## 9. Choice, sacrifice, regret, accountability, and violence
## 10. Knowledge, memory, testimony, and information distribution
## 11. Japanese voice, address, and translation-sensitive language
## 12. Visual and formal analysis
## 13. Body, embodiment, architecture, technology, and logistics
## 14. Motif, callback, foreshadowing, and lexical tracking
## 15. Counterreadings, limitations, and hypothesis stress-test
## 16. Prospective reading at this publication boundary
## 17. What this volume changes in the series-so-far model
## 18. Evidence Classification Ledger
## 19. Primary-Source Locator Ledger
## 20. Cumulative-ledger updates and retrospective-correction status
## 21. Volume thesis and questions carried forward
```

Do not pad a volume with empty sections. A merged section should identify which functions it covers.

---

# 14. Required cumulative ledgers

Across the project maintain:

1. `AOT_MASTER_CHRONOLOGY_AND_LOCATION_LEDGER.md`
2. `AOT_KNOWLEDGE_STATE_AND_INFORMATION_LEDGER.md`
3. `AOT_HUMAN_TITAN_ONTOLOGY_LEDGER.md`
4. `AOT_FREEDOM_WALLS_CONFINEMENT_LEDGER.md`
5. `AOT_EREN_CHARACTER_POWER_AND_AGENCY_LEDGER.md`
6. `AOT_MIKASA_ARMIN_AND_TRIO_LEDGER.md`
7. `AOT_104TH_ENSEMBLE_LEDGER.md`
8. `AOT_WARRIOR_INFILTRATOR_IDENTITY_LEDGER.md`
9. `AOT_SURVEY_CORPS_MILITARY_AND_STATE_LEDGER.md`
10. `AOT_CHOICE_SACRIFICE_REGRET_LEDGER.md`
11. `AOT_RECOGNITION_PERSONHOOD_DEHUMANIZATION_LEDGER.md`
12. `AOT_HOME_RETURN_MEMORY_INHERITANCE_LEDGER.md`
13. `AOT_JAPANESE_VOICE_AND_VOCABULARY_LEDGER.md`
14. `AOT_VISUAL_MOTIF_AND_FORMAL_LEDGER.md`
15. `AOT_BODY_ARCHITECTURE_TECHNOLOGY_LOGISTICS_LEDGER.md`
16. `AOT_CALLBACK_FORESHADOWING_PAYOFF_LEDGER.md`
17. `AOT_OPEN_QUESTIONS_AND_HYPOTHESES.md`
18. `AOT_RETROSPECTIVE_CORRECTION_LOG.md`
19. `AOT_PRIMARY_SOURCE_LOCATOR_INDEX.md`
20. `AOT_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md`
21. `AOT_RELATIONSHIP_CONDITIONED_BEHAVIOR_LEDGER.md`
22. `AOT_EVERYDAY_LIFE_PREFERENCES_AND_LOW_STAKES_BEHAVIOR_LEDGER.md`
23. `AOT_CHARACTER_MODEL_READINESS_AND_COVERAGE_LEDGER.md`

The canonical per-volume artifacts are the durable evidence source. Global ledgers may be compiled from them rather than rewritten from scratch after every response.

Ledgers 20–23 and the existing `AOT_JAPANESE_VOICE_AND_VOCABULARY_LEDGER.md` form the minimum reconstruction-support layer. They are evidence-routing surfaces, not autonomous character canon. Their entries must remain subordinate to the volume artifacts and original Japanese pages.

---

# 15. Library retrieval strategy

Every artifact should include redundant, retrieval-friendly hooks:

- canonical filename;
- volume number;
- chapter range;
- Japanese and English character names;
- major institutions;
- major concepts;
- Japanese lexical anchors;
- important locations;
- source filename and hash;
- evidence IDs.

Useful search examples:

```text
AOT V04 原初的欲求 生まれたからだ freedom
AOT V07 選択と結果 Levi regret
AOT V09 Ragako おかえり Connie mother
AOT V10 兵士 戦士 Reiner Historia Ymir
AOT V12 誰か 見つけてくれ Coordinate
AOT V16 神 使命 いらなかった Historia Eren
AOT V18 特別 自由 Carla Keith Shadis
```

Use natural prose, not keyword stuffing.

---

# 16. Raw-source cold storage and selective reintroduction

Once a volume has:

- verified source metadata and checksum;
- a canonical deep-reading artifact;
- evidence classification;
- a sufficiently useful locator ledger;
- short Japanese anchors for major claims;

its raw CBZ need not remain active for every later synthesis task.

The original Japanese manga remains the final authority.

When a final synthesis claim is:

- contested;
- quotation-sensitive;
- visually dependent;
- mechanically important;
- politically or ethically load-bearing;

use the sequence:

1. retrieve the canonical artifact;
2. identify evidence IDs;
3. follow the locator;
4. selectively reintroduce the CBZ;
5. verify the Japanese page;
6. revise or write the synthesis claim.

---

# 17. Checkpoint synthesis protocol

Checkpoint syntheses occur approximately at:

- **25%:** Volumes 1–9;
- **50%:** around Volumes 18–19, following the user's chosen stopping point;
- **75%:** at a later natural threshold near three quarters of the 34-volume sequence;
- **100%:** after Volume 34.

A checkpoint should not replace volume artifacts. It should synthesize them.

Required functions:

- current narrative architecture;
- current character trajectories;
- current freedom/personhood model;
- current Titan ontology;
- institutions and political legitimacy;
- relationships and recognition;
- Japanese-language findings, including reconstruction-relevant voice/register deltas;
- behavioral and relationship-conditioned pattern changes;
- ordinary-life/low-stakes coverage and remaining blind spots;
- character-model readiness changes by character and time boundary;
- visual/formal development;
- strongest hypotheses;
- counterevidence;
- unresolved questions;
- evidence chains back to volume artifacts.

Checkpoint conclusions remain provisional.

---

# 18. Migration protocol for Volumes 1–18

Volumes 1–18 were originally analyzed in chat before this v2 artifact architecture became mandatory.

Their preservation must distinguish three possible states.

## Verbatim migration

Use only if the exact historical response is available as machine-readable text.

```yaml
provenance_status: migrated_legacy_analysis_verbatim
```

## Reconstructed migration

Use when the analysis is faithfully reconstructed from the historical response, current conversation record, and source reinspection, but is not a byte-for-byte export.

```yaml
provenance_status: migrated_legacy_analysis_reconstructed
```

## Fresh regeneration

Use when the Japanese CBZ is deliberately reopened and a new v2 reading is written.

```yaml
provenance_status: regenerated_from_primary_source
```

For the present V1–V18 migration:

- preserve each original spoiler boundary;
- do not import post-volume answers backward;
- audit each available CBZ's integrity, filename, hash, and image count;
- reconstruct prior analytical conclusions without claiming exact transcript identity;
- add stable evidence IDs;
- provide chapter-level locators and selective page-level locators where verified;
- mark remaining page-level backfill honestly;
- record material corrections rather than silently rewriting history.

The historical chat response remains historically important, but the new Markdown artifact becomes the canonical research record.

---

# 19. Quality-control checklist

Before finalizing a volume artifact verify:

- [ ] complete Japanese source audited and available;
- [ ] archive integrity verified;
- [ ] filename, image count, content-page count, and SHA-256 recorded;
- [ ] chapter map verified;
- [ ] spoiler boundary explicit and intact;
- [ ] later answers not imported backward;
- [ ] causal development explained rather than only summarized;
- [ ] character beliefs not promoted to fact;
- [ ] humanization not confused with absolution;
- [ ] military necessity not allowed to erase cost or consent;
- [ ] tactical, strategic, political, and moral judgments separated;
- [ ] Eren is not treated as the only meaningful subject;
- [ ] Mikasa and Armin retain independent agency and interiority;
- [ ] ensemble and institutions are tracked;
- [ ] Japanese-language observations with interpretive payoff are captured; low-thematic but reconstruction-relevant speech evidence is routed to the voice ledger when present;
- [ ] visual claims are grounded in inspected pages or clearly marked for backfill;
- [ ] body, architecture, technology, and logistics are not treated as decorative;
- [ ] at least one counterreading is tested;
- [ ] stable evidence IDs are assigned;
- [ ] locators are not guessed;
- [ ] cumulative delta is explicit;
- [ ] relationship-conditioned behavior is not generalized into a universal trait without support;
- [ ] crisis-state behavior is not treated as ordinary baseline;
- [ ] low-stakes/everyday evidence is harvested when present and absent evidence is marked as a coverage gap rather than invented;
- [ ] manga evidence is not used to infer anime vocal performance;
- [ ] open questions remain open;
- [ ] canonical Markdown artifact emitted;
- [ ] internal links and filenames resolve;
- [ ] no source CBZ is redistributed inside the analysis archive.

---

# 20. Prohibited shortcuts and recurring failure modes

Avoid:

- reducing the series to “humans are the real monsters”;
- reducing every Titan to a simple trauma metaphor;
- treating literal mechanics and symbolism as mutually exclusive;
- using the anime to settle manga ambiguity without an adaptation phase;
- treating Eren's perspective as the work's total perspective;
- treating military competence as moral legitimacy;
- treating political illegitimacy as automatic legitimation of the opposition;
- treating sacrifice as justified because a plan succeeds;
- treating sacrifice as pointless because a plan fails;
- equating empathy with forgiveness;
- denying accountability because a perpetrator was also a child or victim;
- denying personhood because accountability is required;
- treating every visual repetition as confirmed foreshadowing;
- overreading Japanese from one isolated line;
- flattening 兵士 and 戦士 without examining context;
- calling a migrated reconstruction a verbatim export;
- fabricating CBZ page locators;
- producing a long plot recap with thematic labels attached afterward;
- converting a thematic motif directly into a deterministic personality rule;
- treating a crisis-state utterance as the character's normal conversational register;
- using translated English phrasing as evidence of Japanese idiolect when the Japanese source is available;
- allowing synthetic or hypothetical outputs to become evidence for the model that generated them.

---

# 21. Final synthesis traceability

The eventual full-series synthesis uses three evidentiary layers. A downstream reconstruction layer may be added only after those layers are stable.

## Layer 1 — Reader-facing synthesis claim

Example:

> The manga turns freedom from Eren's first-person claim into a universal but politically unstable birthright.

## Layer 2 — Canonical volume artifacts

Example:

```text
AOT_V04_DEEP_READING.md
AOT_V16_DEEP_READING.md
AOT_V18_DEEP_READING.md
```

## Layer 3 — Primary evidence

Example:

```text
AOT_V04_E0XX
→ 第14話 原初的欲求
→ Japanese anchor: オレがこの世に生まれたからだ
→ original Japanese page
```

For every load-bearing thesis, preserve at least one chain.

For disputed, visual, or translation-sensitive claims, preserve multiple chains.

## Layer 4 — Derived character reconstruction and validation

Character-model claims are downstream products. They should route:

`reconstruction claim -> behavioral/relationship/voice/ordinary-life ledger -> canonical volume evidence -> primary source`

A reconstruction model should also carry an explicit validation state. Predictions or synthetic dialogue generated during QA never become evidence; failures must return the analyst to the source and revise the model claim. Prospective prediction records should be frozen before the source material that tests them is analyzed.

The final corpus should permit:

> **synthesis → analysis → evidence ID → locator → manga page**

without reconstructing the path from memory.

---

# 22. Governing methodological principle

The project succeeds only if it preserves two things at once:

1. the interpretive complexity of people whose actions are contradictory, historically constrained, and morally consequential; and
2. the evidentiary route back to the Japanese pages that made those conclusions possible.

The standing principle is:

> **Describe the characters and institutions closely enough that contradiction becomes legible without becoming exculpatory.**

The standing provenance principle is:

> **Record the evidence carefully enough that later synthesis can recover not only what we concluded, but why the text entitled us to conclude it.**

The standing reconstruction principle is:

> **Model characters as conditional repertoires across time, relationship, knowledge, role, and pressure—not as bundles of famous traits—and preserve the boundary where prediction becomes invention.**
