---
series: IMOSAE
artifact_type: analytical_method
scope: V01-V14_main_series_plus_labeled_supplements
generation: V1
status: canonical
source_boundary: Japanese light novel main series Volumes 01-14; supplemental sources admitted only through explicit tiering
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-08-18'
paired_with: IMOSAE_SYNTHESIS_ARCHITECTURE_V1.md
---

# 妹さえいればいい。 / A Sister's All You Need
## Analytical Method V1

## 0. Purpose

This document governs the sequential and retrospective analysis of the complete fourteen-volume Japanese main series of **『妹さえいればいい。』** by 平坂読.

The project is not a plot-summary exercise and should not be reduced to the title's provocation, romantic pairings, or a catalogue of light-novel-industry jokes. The series should be read simultaneously as:

- an ensemble adult coming-of-age narrative;
- a novel about authorship, talent, work, career instability, and the production of entertainment;
- a relationship drama involving friendship, family, romance, sexuality, jealousy, dependency, care, and professional intimacy;
- a metatext about light novels, manga, anime, games, awards, adaptation, editors, readers, and creators;
- a comedy whose vulgarity can both expose and conceal serious emotional or ethical problems;
- a Japanese prose work whose narration, dialogue, register, ruby, typography, and paratext are part of the evidence;
- an illustrated publication in which Kantoku's images, covers, and page placement form a meaningful paratextual layer.

The governing principle is:

> **Read each volume first as the reader could have understood it at that point in publication, then preserve later reinterpretation as an explicit delta rather than silently rewriting the earlier reading.**

A second principle is:

> **Professional success, artistic worth, personal happiness, moral legitimacy, and relational success are separate variables unless the text itself joins them.**

A third principle is:

> **Comedy is evidence of framing, not an automatic ethical verdict. A joke can normalize, criticize, evade, intensify, or merely exploit a situation; determine which through context rather than assumption.**

A fourth principle is:

> **The Japanese text governs linguistic claims. Translation may be used for explanation, but character voice, register, wordplay, naming, and repeated terminology must be checked against the original.**

---

# I. Corpus boundary and authority hierarchy

## 1. Tier 1A — Main-series Japanese prose

The governing narrative corpus is the numbered Japanese light-novel series:

- `V01` through `V14`.

The numbered novels are the highest authority for:

- narrative events;
- character states;
- relationship development;
- chronology;
- internal works of fiction;
- professional/career developments;
- narrator framing;
- Japanese wording and voice.

Volume 14 is the endpoint of the numbered main series.

## 2. Tier 1B — Main-volume illustrations and internal paratext

Treat as primary **paratextual** evidence rather than identical to prose narration:

- cover illustrations;
- color inserts;
- monochrome illustrations;
- chapter/title-page graphics;
- included bonus illustrations;
- typography and emphasis;
- afterwords;
- colophons.

Important distinction:

> **An illustration can establish editorial/visual emphasis and a licensed depiction of a scene; it does not automatically override a contradiction in the prose.**

Author afterwords establish authorial commentary and production context, not diegetic fact unless the fiction separately supports it.

## 3. Tier 2 — Author-written or officially supervised supplemental narrative

Potential examples include:

- special-edition drama CDs with scripts by 平坂読;
- Blu-ray audio dramas with author-written scenarios;
- other verified official short narrative material.

These may refine voice, relationship rhythm, comedy, and alternative situations, but they must receive a `SUPP-*` locator namespace and must not silently overwrite the main-series chronology.

## 4. Tier 3 — Authorized adaptations and spin-offs

Examples include:

- the television anime;
- `妹さえいればいい。@comic`;
- `妹さえいればいい。外伝 妹にさえなればいい!`;
- mini-anime and other authorized adaptation material.

Use these for:

- adaptation choices;
- visual reinterpretation;
- compression/omission;
- alternate emphasis;
- production history;
- potentially valuable supplementary characterization when clearly labeled.

Do **not** use an adaptation-only event as evidence that the event occurred in the novel continuity.

## 5. Tier 4 — Reception, marketing, interviews, and contextual material

Examples:

- creator interviews;
- promotional copy;
- sales/award information;
- event commentary;
- contemporary reviews or reception data.

These belong in contextual or reception analysis, not as substitutes for textual interpretation.

---

# II. Phase 0 — Source lock, normalization, and provenance

No volume deep reading should begin until Phase 0 has produced a frozen, auditable reading layer.

## Phase 0.1 — Immutable source freeze

For each of the fourteen EPUBs:

1. Record exact filename.
2. Record byte size.
3. Record SHA-256.
4. Run ZIP CRC validation.
5. Record OPF path and EPUB version/package type.
6. Record whether navigation is EPUB 2 NCX or EPUB 3 nav.
7. Mark the original EPUB as immutable.

The project must never rewrite the source EPUBs merely to make extraction convenient.

Output homes:

- `IMOSAE_SOURCE_INVENTORY.md`
- `IMOSAE_SOURCE_LOCK.md`
- machine-readable checksum/manifest files.

## Phase 0.2 — Colophon-first bibliographic authority

Embedded EPUB metadata is retrieval metadata, not final bibliographic authority.

For every volume, recover from the colophon where available:

- Japanese title;
- volume number;
- author;
- illustrator;
- imprint/publisher;
- base-edition publication/printing date;
- ebook date if separately stated;
- ISBN;
- edition notes.

When package metadata conflicts with the colophon, preserve both but mark the colophon as bibliographically authoritative for this project.

## Phase 0.3 — Package and content inventory

Inventory:

- spine order;
- chapter/navigation labels;
- XHTML members;
- image members;
- stylesheets;
- fonts if referenced, without redistributing them;
- afterword and colophon members;
- promotional or retailer-bonus members;
- embedded special-edition material if present.

Each spine member receives a content class before analysis.

Recommended classes:

- `MAIN_NARRATIVE`
- `BONUS_FICTION`
- `AUTHOR_AFTERWORD`
- `ILLUSTRATION`
- `TITLE_FRONTMATTER`
- `COLOPHON`
- `PROMOTIONAL`
- `RETAILER_EBOOK_BONUS`
- `OTHER_PARATEXT`

## Phase 0.4 — Loss-aware Japanese extraction

Generate an analytical reading layer that preserves source order and paragraph boundaries.

### Ruby

Do not flatten ruby into duplicated text such as `瞳ひとみ`.

Store:

- base text in the canonical reading stream;
- reading in a structured sidecar/annotation field.

Conceptual representation:

```text
base: 瞳
reading: ひとみ
```

Ruby itself can be analytically meaningful when it supplies:

- non-obvious readings;
- wordplay;
- name readings;
- foreign/technical readings;
- semantic double-coding.

## Phase 0.5 — Gaiji resolution and special-symbol register

The present EPUB set contains inline gaiji/special-symbol images. A naïve HTML-to-text conversion can silently delete them.

Procedure:

1. Hash every distinct gaiji image.
2. Assign stable IDs, e.g. `IMOSAE-G001`.
3. Capture surrounding Japanese context and any ruby/alt metadata.
4. Resolve the character/symbol where confidence is high.
5. Preserve an explicit token where resolution is uncertain:

```text
⟦GAIJI:IMOSAE-G017⟧
```

6. Record confidence and evidence in `IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md`.
7. Never substitute a guessed glyph silently.

## Phase 0.6 — Typography and emphasis preservation

Preserve machine-readable markers for:

- sesame-dot emphasis;
- bold/strong text;
- enlarged/reduced type;
- tate-chū-yoko/upright treatment;
- centered text;
- unusual spacing;
- image-only textual elements.

The analytical prose view can be simplified for reading, but the locator/evidence layer must retain enough information to recover the original formal treatment.

## Phase 0.7 — Stable paragraph-level locators

Generate locators that survive ordinary re-extraction and can route back to the original EPUB member.

Recommended grammar:

```text
V06|chapter:那由多の景色|spine:NN|xhtml:OEBPS/Text/XXXX.xhtml|p:0042
```

Where useful, add:

- a short normalized-text fingerprint;
- illustration anchor;
- ruby/gaiji annotation IDs.

Do not use ebook page numbers as the sole locator. They can change by renderer, font size, or edition.

## Phase 0.8 — Illustration and paratext inventory

For every meaningful visual asset record:

- volume;
- member filename;
- dimensions;
- page/spine relation;
- whether color or monochrome;
- preceding/following prose anchor;
- depicted characters if unambiguous;
- scene represented;
- whether it is narrative illustration, cover, ad, bonus, or unrelated promotional image.

Create a visual locator such as:

```text
V09|ILL:012|member:OEBPS/Images/...
```

Do not treat illustrations as detachable gallery images. Placement relative to prose is part of the evidence.

## Phase 0.9 — Extraction validation

Before freezing Phase 0:

- sample beginning/middle/end of every volume;
- sample ruby-heavy passages;
- sample gaiji-heavy passages;
- sample emphasized typography;
- sample dialogue exchanges;
- sample chapter boundaries;
- verify illustration anchors;
- compare normalized extraction to original XHTML.

Required outcome:

> No silent text loss in sampled passages; every unresolved loss is explicitly marked.

## Phase 0.10 — Phase-0 source-lock audit

Freeze:

- hashes;
- colophon inventory;
- normalized text version;
- gaiji register;
- locator grammar;
- content classes;
- illustration index version.

Later corrections create a new normalized-text version and a documented delta. Do not silently mutate the frozen reading layer.

---

# III. Evidence-state labels

Use evidence labels where the distinction matters.

## TF — Textual fact

Directly narrated or spoken content in the main novels.

## LF — Linguistic fact

Directly observable Japanese-language feature:

- register;
- pronoun;
- address term;
- sentence ending;
- lexical recurrence;
- ruby;
- explicit wordplay.

## PF — Paratextual fact

Direct fact from an illustration, afterword, cover, colophon, or publication paratext.

## SF — Supplemental-source fact

Directly present in a labeled official supplement or adaptation, but not automatically mainline fact.

## FR — Formal recurrence

Demonstrable recurrence/transformation of:

- phrase;
- chapter form;
- game;
- fictional work;
- joke structure;
- image;
- object;
- narrative situation;
- publication device.

## SI — Strong inference

Interpretation supported by several mutually reinforcing pieces of evidence.

## IT — Interpretive thesis

Higher-order explanation that organizes a substantial evidence set.

## SP — Speculation

Plausible but underdetermined interpretation.

---

# IV. Mandatory interpretive distinctions

Do not collapse the following:

- narrator description ≠ objective authorial truth;
- character belief ≠ series endorsement;
- comic framing ≠ moral approval;
- embarrassment ≠ lack of desire;
- desire ≠ entitlement;
- sexual frankness ≠ consent;
- intimacy ≠ romance;
- romance ≠ a healthy relationship;
- professional success ≠ artistic worth;
- artistic talent ≠ moral superiority;
- commercial compromise ≠ artistic betrayal by definition;
- failure ≠ lack of talent;
- effort ≠ entitlement to success;
- editor judgment ≠ neutral truth;
- creator self-image ≠ actual capability;
- fictional-work content ≠ simple autobiography;
- game metaphor ≠ literal theory of human relations;
- an illustration's emphasis ≠ complete narrative meaning;
- an afterword statement ≠ diegetic canon;
- adaptation choice ≠ novel continuity.

---

# V. Sequential evidence boundary

The first pass is prospective.

For `IMOSAE_V07_DEEP_READING.md`, semantic evidence may use:

- Volumes 1–7;
- previously admitted supplements whose chronological/authority status has been explicitly defined.

It may not use Volumes 8–14 to make Volume 7 appear less ambiguous than it originally was.

After later volumes add pressure, record:

> Earlier reading → later evidence → current disposition.

Use the claim-transition vocabulary:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

The early volume artifact remains historically faithful to its boundary.

---

# VI. Novel-by-novel close-reading workflow

Every numbered volume receives the following workflow. Not every pass must occupy equal space; the method is comprehensive, not mechanically symmetrical.

## Pass 0 — Volume source lock

Record:

- source EPUB filename;
- SHA-256;
- normalized-text version;
- colophon record;
- chapter list;
- substantive member count;
- illustration count;
- unresolved gaiji relevant to the volume;
- semantic evidence boundary.

## Pass 1 — Naïve structural reading

Before generating a thematic thesis, reconstruct the volume in sequence:

- opening condition;
- chapter progression;
- changes in viewpoint or focalization;
- major reversals;
- climactic scenes;
- ending state;
- unresolved residue.

Do not force every comic chapter into a unified symbolic thesis if the volume is deliberately episodic.

## Pass 2 — Narration and focalization

Track:

- focal character(s);
- narrator distance;
- free-indirect or interior passages;
- withheld knowledge;
- shifts in comic versus serious register;
- authorial-seeming generalizations that may actually belong to a focal character;
- how prose rhythm changes around embarrassment, sex, professional crisis, grief, or artistic work.

Required question:

> **Who gets to define what this scene means, and how trustworthy is that position?**

## Pass 3 — Character-state analysis

For every materially affected principal character track:

- stated desire;
- enacted desire;
- fear/wound;
- self-conception;
- professional identity;
- private identity;
- defensive strategy;
- source of pride;
- source of shame;
- capacity gained/lost;
- contradiction exposed;
- what they cannot yet say plainly.

Avoid diagnosing pathology unless the text itself supplies a clinical frame.

## Pass 4 — Relationship ecology

Track relationships as dynamic systems rather than ship slots.

For each important bond ask:

- What does each person want from the other?
- What can they say directly?
- What requires jokes, work, games, sex, alcohol, rivalry, or fiction as mediation?
- Who has interpretive power?
- Who can refuse whom?
- Who carries emotional or practical labor?
- Is care reciprocal, asymmetrical, avoidant, possessive, transactional, or changing?
- What repairs conflict?
- What remains unresolved after reconciliation?

Include friendships, professional partnerships, family ties, rivalry, mentorship, and romance.

## Pass 5 — Creative labor and industry

This is mandatory for every volume in which it appears.

Track:

- writing process;
- deadlines;
- editorial intervention;
- awards;
- contracts;
- royalties/money;
- adaptation;
- illustrator/manga/anime collaboration;
- publicity;
- sales/reception;
- professional jealousy;
- networking;
- career precarity;
- burnout;
- comparison among creators;
- the social consequences of success and failure.

Required distinctions:

> career result / artistic judgment / self-worth / peer recognition / reader response

should be kept separate unless the characters or narration explicitly collapse them.

## Pass 6 — Talent, effort, ambition, and failure

Track how the volume distributes:

- talent;
- technique;
- experience;
- luck;
- market fit;
- persistence;
- discipline;
- originality;
- insecurity;
- envy.

Ask:

> **What does the volume believe can be earned, and what remains contingent?**

Do not romanticize either prodigy mythology or effort mythology.

## Pass 7 — Family, siblinghood, and identity

Track:

- literal sibling relations;
- imagined/fictional sibling roles;
- family disclosure;
- chosen versus inherited bonds;
- gendered expectations;
- the meaning of “sister” within the protagonist's artistic fixation;
- whether sibling language is comic fetish, emotional displacement, aesthetic program, family wound, or some combination.

The title's premise should be investigated longitudinally, not treated as the answer in advance.

## Pass 8 — Sexuality, erotic comedy, and boundaries

Analyze rather than sanitize the text's sexual material.

Track:

- mutual desire;
- unilateral desire;
- consent/refusal;
- embarrassment;
- voyeurism;
- objectification;
- sex as intimacy;
- sex as comedy;
- sexual competition;
- eroticization by narration versus by illustration;
- when vulgarity creates honesty;
- when vulgarity obscures harm;
- when a scene is deliberately ethically uncomfortable.

Do not infer that adult sexual content is thematically mature merely because it is explicit.

## Pass 9 — Games, TRPGs, food, alcohol, travel, and social ritual

These recurring activities should not be dismissed as downtime.

Ask what each social form enables:

- disclosure;
- competition;
- collaboration;
- role experimentation;
- lowered inhibition;
- conflict;
- professional networking;
- temporary escape from work;
- community formation.

Track repeated games and rituals as longitudinal formal devices.

## Pass 10 — Fiction within fiction and intertext

Inventory and interpret:

- characters' novels;
- manga/anime adaptations;
- fictional titles;
- excerpts or synopses;
- references to real genres/works/industry conventions;
- parody;
- creator analogies;
- metafictional chapter structures.

For an internal fictional work, ask separately:

1. What is the work about inside the story?
2. What does producing it reveal about its creator?
3. How do other characters read it?
4. What professional consequences does it have?
5. Is the novel inviting an analogy to the main narrative, or merely tempting us to make one?

## Pass 11 — Japanese voice, naming, and style

For recurring characters track:

- first-person pronouns;
- second-person forms;
- surnames/given names/nicknames;
- honorifics;
- politeness levels;
- sentence endings;
- contractions;
- rough/feminine/formal/otaku/professional registers;
- swearing/vulgarity;
- editor/creator jargon;
- relationship-dependent shifts;
- recurring lexical tics.

Character voice should become reconstructable from accumulated evidence, but this is **textual voice**, not acoustic performance.

## Pass 12 — Illustration and publication-form analysis

For each meaningful illustration ask:

- Why this scene?
- Why this moment within the scene?
- Whose body/face receives emphasis?
- Is the visual register comic, erotic, domestic, professional, romantic, or dramatic?
- Does the illustration intensify or simplify an ambiguity in the prose?
- What does cover progression imply about marketing focus or ensemble hierarchy?

Do not infer an entire relationship from one promotional image.

## Pass 13 — Counterevidence and alternative readings

Every deep reading must include at least one non-trivial stress test.

Questions:

- What evidence resists the governing thesis?
- Is a serious interpretation being generated from what may simply be a gag?
- Is a gag being used to avoid acknowledging a serious consequence?
- Are we projecting later development backward?
- Are we mistaking authorial familiarity with the LN industry for documentary realism?
- Does another character provide a credible counter-reading?

## Pass 14 — Cumulative delta

At the end of the volume update only the ledgers materially affected.

Record:

- new evidence IDs;
- character deltas;
- relationship deltas;
- professional/industry deltas;
- family/sibling deltas;
- voice/terminology deltas;
- formal recurrences;
- open questions;
- predictions/hypotheses still live;
- pressure on previous claims.

---

# VII. Standard volume artifact

Recommended filename:

`IMOSAE_V01_DEEP_READING.md`

Required structure:

1. YAML authority/provenance block.
2. Executive thesis.
3. Source lock and evidence boundary.
4. Chapter/structural map.
5. Narrative/focalization analysis.
6. Character-state changes.
7. Relationship ecology.
8. Creative labor and industry.
9. Talent/effort/success/failure.
10. Family/sibling identity where active.
11. Sexuality/comedy/boundaries where active.
12. Games/social ritual where active.
13. Fiction-within-fiction/intertext.
14. Japanese voice and terminology.
15. Illustration/paratext analysis.
16. Counterevidence/competing interpretations.
17. Cumulative delta.
18. Open questions.
19. Primary-source locator table.

Recommended front matter:

```yaml
---
series: IMOSAE
artifact_type: deep_reading
scope: V01
generation: V1
status: canonical
source_boundary: "Japanese light novel Volume 01"
semantic_evidence_boundary: "V01 only"
future_semantic_evidence_used: false
source_sha256: "..."
normalized_text_version: "..."
analysis_method: IMOSAE_ANALYTICAL_METHOD_V1.md
architecture_protocol: IMOSAE_SYNTHESIS_ARCHITECTURE_V1.md
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---
```

---

# VIII. Checkpoint protocol

Use five checkpoints rather than one after every volume. The series is fourteen volumes: three-volume tranches preserve developmental state without overwhelming the corpus with repetitive snapshots.

## `IMOSAE_V01-V03_CHECKPOINT.md`

Freeze:

- initial ensemble structure;
- initial theory of authorship and talent;
- early sibling/family/title problem;
- relationship baselines;
- initial industry model;
- strongest open questions.

## `IMOSAE_V04-V06_CHECKPOINT.md`

Focus on changes in:

- professionalization;
- adaptation/media-mix pressures;
- creator comparison;
- relationships moving beyond introductory roles;
- how group social rituals mediate work.

## `IMOSAE_V07-V09_CHECKPOINT.md`

Focus on:

- mature friendship/romantic/professional ecology;
- career divergence;
- jealousy and comparison;
- changing definitions of success;
- expansion of younger/newer creator perspectives.

## `IMOSAE_V10-V12_CHECKPOINT.md`

Focus on:

- identity disclosure/reclassification;
- family and siblinghood;
- creative crisis;
- adult futures;
- relationship restructuring;
- whether early professional/self-worth theses survive.

## `IMOSAE_V13-V14_END_STATE_CHECKPOINT.md`

Freeze the completed-mainline end state before any supplemental retrospective work.

Record:

- final character states;
- final relationship states;
- professional/career outcomes;
- unresolved tensions;
- title-theme resolution/non-resolution;
- what the ending treats as continuity versus closure.

Checkpoint labels above identify retrieval concerns, not conclusions to be assumed.

---

# IX. Longitudinal ledgers

Maintain in parallel with sequential reading.

## 1. Character and relationship state ledger

Track the principal ensemble and meaningful secondary figures across volumes.

## 2. Creative labor, career, and industry ledger

Track:

- projects;
- publications;
- adaptation;
- sales/status;
- awards;
- deadlines;
- editors;
- career transitions;
- professional crises.

## 3. Family, identity, and siblinghood ledger

Track literal and symbolic uses of family/sibling roles.

## 4. Japanese voice, style, and terminology ledger

Track both character idiolect and industry/creative terminology.

## 5. Fiction-within-fiction, games, and intertext ledger

Track recurring fictional works, games, metaphors, and formal callbacks.

## 6. Visual paratext and illustration ledger

Track cover/illustration progression and transformed visual motifs.

## 7. Claim revision ledger

Use:

`PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`.

Every mature thesis should be routable back to the volume evidence that formed it and later evidence that changed it.

---

# X. Core hypotheses to test, not assume

These are starting questions, not conclusions.

## H1 — Making art is represented as a form of adult life rather than merely a route to self-expression.

Test money, deadlines, social labor, professional compromise, failure, and long-term sustainability.

## H2 — Talent is real in the series, but talent is an unstable basis for self-worth and relationship hierarchy.

Test prodigy figures, jealousy, effort, career results, and how characters respond to unequal ability.

## H3 — The light-novel industry is represented neither as pure exploitation nor as a romantic creative community.

Test editors, publishers, adaptations, creators, sales, networking, and institutional constraints.

## H4 — Games, alcohol, food, travel, and group ritual are social technologies through which characters say things ordinary conversation makes difficult.

Test whether these devices consistently alter disclosure, hierarchy, or conflict.

## H5 — The protagonist's “sister” fixation changes meaning across the series.

Test whether it functions as fetish, aesthetic doctrine, displacement, family problem, creative engine, comic mask, or some shifting combination.

## H6 — Fiction within fiction acts as an indirect language for desire and professional anxiety.

Test each internal work rather than assuming simple one-to-one autobiography.

## H7 — Vulgar comedy often provides access to serious material, but sometimes also protects characters or the text from confronting harm.

Search deliberately for both outcomes.

## H8 — Adult romantic development cannot be understood separately from friendship, career, family, and creative identity.

Test whether relationships flourish or fail when isolated from those systems.

## H9 — The series is structurally ensemble-driven even when one character supplies the principal focal point.

Test whose actions actually change the state of the social/professional system.

---

# XI. Supplemental-material integration protocol

Supplementary materials should not contaminate the prospective fourteen-volume baseline.

Preferred order:

1. Finish and freeze `V13-V14_END_STATE_CHECKPOINT`.
2. Audit each supplement's authorship, continuity status, date, and format.
3. Assign an authority tier and `SUPP-*` source ID.
4. Perform source-facing readings of high-value supplements.
5. Record whether each supplement:
   - preserves;
   - strengthens;
   - revises;
   - complicates;
   - or merely illustrates a mainline claim.
6. Keep adaptation-only or counterfactual material in explicitly separate lanes.
7. Only then draft specialist and full-series synthesis.

Exception:

A supplement can be consulted earlier for **bibliography/provenance only** without importing its semantic character information into the sequential pass.

---

# XII. Retrospective synthesis operations

After V14 and the selected supplemental pass:

## 1. Consolidation

Move distributed observations into their canonical topical homes.

## 2. Stress testing

Search intentionally for passages that weaken the most attractive mature theses.

## 3. Longitudinal reconstruction

For major claims use:

> Initial formation → pressure → transformation/persistence/regression → end state.

## 4. Voice reconstruction

For major characters, synthesize:

- baseline syntax/register;
- relationship-dependent speech;
- professional versus private voice;
- comedy/vulgarity style;
- conflict speech;
- vulnerability speech;
- lexical signatures.

Do not claim acoustic properties from prose alone.

## 5. Formal synthesis

Track how:

- chapter forms;
- internal fiction;
- games;
- recurring jokes;
- illustrations;
- title motifs;
- publication paratext

change meaning across the series.

## 6. Ending analysis

Treat separately:

- professional ending;
- relationship ending;
- family ending;
- artistic ending;
- social-group continuity;
- unresolved futures.

Closure in one dimension does not imply closure in all others.

---

# XIII. Final safeguards

- Prefer the Japanese primary text over remembered anime scenes.
- Do not use fandom consensus as evidence.
- Do not flatten adult sexuality into either prudish condemnation or automatic liberation.
- Do not mistake the author's industry experience for neutral documentary truth.
- Do not romanticize creative suffering.
- Do not convert commercial success into proof of artistic superiority.
- Do not turn every fictional work into a coded confession.
- Do not reduce female characters to romantic routes around the male protagonist.
- Do not reduce male friendship to comic filler.
- Do not overread illustrations detached from their publication context.
- Preserve ambiguity when the text preserves it.
- Identify fact, inference, interpretation, and speculation explicitly when stakes are high.

---

# XIV. Target analytical capability

At completion the corpus should support, with traceable evidence:

- volume-by-volume literary reconstruction;
- precise character and relationship development;
- textual modeling of major character voices;
- analysis of creative labor and the light-novel/media industry;
- analysis of talent, ambition, failure, envy, and self-worth;
- analysis of family and siblinghood;
- analysis of sexuality, comedy, intimacy, and boundaries;
- analysis of games and social ritual;
- analysis of fiction within fiction and metatext;
- illustration/paratext analysis;
- full-series ending interpretation;
- comparison with other creator-industry and ensemble works.

The target is not maximal interpretation.

The target is **maximal explanatory power under auditable textual constraints**.
