---
series: AOT
artifact_type: synthesis_architecture
scope: V01-V34
generation: V2
status: canonical
version: '1.2'
last_amended: '2026-08-27'
architecture_lifecycle: STABILIZED
reasoning_class_policy: MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md v1.0
reasoning_budget_policy: Section VI stable reasoning-class registry plus current provider mapping
execution_scope_policy: MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md v1.0
date: '2026-08-27'
source_boundary: Complete Japanese manga tankobon Volumes 1-34; sequential V2 deep-reading phase complete
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
parent_method: AOT_ANALYTICAL_METHOD_V2.md
project_policy: AOT_PROJECT_DECISIONS_AND_CHECKPOINT_POLICY.md
character_modeling_architecture: AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md
validation_method: AOT_CHARACTER_RECONSTRUCTION_AND_VALIDATION_METHOD_V1.md
current_entrypoint: CURRENT_STATE_AND_CORPUS_MAP.md
next_operation: AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md
---

# 『進撃の巨人』 / *Attack on Titan*
## Full-Series Synthesis Architecture and Post-V34 Document Roadmap v1.2
### Specialist homes, evidence routing, production order, character reconstruction boundary, and final integration plan

## 0. Purpose

The V2 sequential manga reading is complete through Volume 34. The project therefore changes analytical mode.

Volumes 1-34 were read as publication-bounded objects so that later revelations could not silently overwrite earlier uncertainty. The next phase is allowed to be retrospective, but it must not destroy the historical record created by that discipline. The purpose of this architecture is to define **where the mature full-series analysis belongs, in what order it should be produced, which documents own which questions, how claims route back to evidence, and when character reconstruction becomes authoritative**.

The earlier project policy correctly required a full-series phase containing multi-document thematic synthesis, character and relationship studies, political and institutional analysis, Titan ontology, freedom/personhood/inheritance, Japanese-language and visual-form analysis, evidence and locator infrastructure, full-series character reconstruction, validation, and final archival administration. That policy deliberately did not specify the mature internal document map. Now that all thirty-four volumes have been read, the corpus contains enough evidence to formalize that map without designing it around incomplete knowledge.

This architecture therefore does **not** replace:

- `AOT_ANALYTICAL_METHOD_V2.md` as the governing reading/provenance method;
- `AOT_PROJECT_DECISIONS_AND_CHECKPOINT_POLICY.md` as the governing phase policy;
- the canonical V01-V34 deep readings as volume-local evidence authorities;
- the V19 and V27 checkpoints as boundary-specific historical authorities;
- the character-modeling architecture, schema, or validation method.

It supplies the missing layer between those methods and the final synthesis corpus.

The governing architectural principle is:

> **Separate documents by governing question, not by whichever topic happens to be adjacent in the final plot.**

The second principle is:

> **Every major question receives one primary analytical home. Other documents may invoke the conclusion briefly, but should cross-reference rather than reproduce the same deep dive.**

The third principle is:

> **Evidence is stabilized before interpretive compression. Specialist synthesis is written before the continuous full-series synthesis. Character reconstruction is written after the literary/full-series synthesis, not instead of it.**

The fourth principle is specific to *Attack on Titan*:

> **Retrospective knowledge may revise a claim, but it must not erase what the text supported at an earlier publication boundary.**

This is the post-V34 bridge from sequential reading to mature synthesis.

## 0.1 Corpus-wide governance alignment and lifecycle

This architecture remains **`canonical`** as an authority state and is now explicitly **`STABILIZED`** as an architecture lifecycle state. These are different dimensions: `canonical` answers which architecture governs current work; `STABILIZED` records that the complete V01-V34 sequential source has been read and the mature synthesis responsibilities are substantially known, while still permitting explicit amendment before release freeze.

The following corpus-wide governance documents apply without displacing AOT-specific method or structure:

- `ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md` governs authority, supersession, legacy retention, and canonical retrieval surfaces;
- `MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` supplies the corpus-wide Minimum Semantic Contract and lifecycle terminology. AOT is a mature grandfathered project, so this policy is used as a gap audit rather than as a mandate to redesign the established tree;
- `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` governs durable reasoning classes. Section VI retains AOT-specific per-artifact recommendations but expresses the durable architectural choice as a stable class, with literal GPT-5.6 names treated as the current provider mapping;
- `MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md` governs authorization, atomic closeout, recovery, and concurrency for future sequential operations. AOT's main manga sequential contract is already closed at V34; there is no V35 operation. The policy does not alter the post-V34 synthesis order.

`MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md` is **not an active AOT requirement** for this manga-only source topology. It remains a corpus-wide audiovisual boundary document and must not be used to import episode-bundle, audio, or continuous-video obligations into the Japanese manga analysis.

### Source and sequential contract

The source topology remains one linear Japanese tankōbon manga continuity, Volumes 1-34, with tankōbon apparatus classified under `AOT_ANALYTICAL_METHOD_V2.md`. Adaptations, interviews, guidebooks, external criticism, and other source layers remain excluded unless an explicitly separated later phase activates them. Exact Japanese wording, panel composition, page sequence, spatial relation, body language, or visual grammar escalates to the original Japanese manga page.

The canonical sequential phase is complete. Its historical transaction contract remains: one volume-local deep reading plus required cumulative/modeling/provenance updates under the method and project policy. Those completed artifacts are not retroactively redesigned to satisfy newer corpus-wide terminology. Publication-boundary truth remains preserved.

### Architecture amendment rule

A new ledger, specialist home, evidence layer, or validation responsibility may be added only when recurring evidence demonstrates a distinct analytical function not adequately served by an existing canonical home. Material amendments must be reviewed explicitly because downstream specialist work may depend on them. Cosmetic normalization is not sufficient reason to rename, renumber, relocate, or duplicate established AOT artifacts.

Before creating a new analytical artifact, search for an existing canonical topical home. Prefer updating that home when the semantic responsibility is already represented.

### Mutable and frozen state

The following remain mutable while the project is active: `CURRENT_STATE_AND_CORPUS_MAP.md`, cumulative ledgers where their method permits continued updates, the synthesis evidence/index infrastructure, corpus manifest/checksum infrastructure, and this architecture while it remains `STABILIZED` rather than release-frozen.

The V19 checkpoint, V27 checkpoint as its own historical boundary, frozen V01-V19 prospective prediction register, and completed volume-local deep readings retain their boundary-specific authority and must not be silently rewritten to simulate retrospective omniscience. If the architecture is later frozen as part of a release, material structural changes should normally become a later architecture version rather than silently mutating the frozen release.

### Canonical retrieval route

For future recovery, use:

> `MANGA_ANIME_DRIVE_INDEX.md` -> `CURRENT_STATE_AND_CORPUS_MAP.md` -> AOT governing method/architecture -> narrowest canonical topical home -> evidence/revision/locator infrastructure -> original Japanese manga page when exact verification is load-bearing.

This route preserves the existing AOT architecture while making its authority, lifecycle, evidence escalation, and future amendment behavior explicit.

---

# I. Architectural precedents and AOT-specific departures

This design borrows methods from several mature project corpora without importing any of their interpretations as evidence about *Attack on Titan*.

## 1. LOGH precedent: primary homes and different reader/drafting orders

The *Legend of the Galactic Heroes* corpus demonstrates the value of assigning one primary analytical home to each large question and separating reader order from production order. AOT should borrow that discipline because political institutions, military operations, personal relationships, ethics, historiography, and protagonist psychology repeatedly intersect without becoming the same question.

## 2. 86 precedent: layered corpus plus continuous synthesis written last

The *86* V2 architecture is the closest overall structural precedent. It separates frameworks, chronological evidence, longitudinal ledgers, specialist synthesis, retrieval infrastructure, release administration, and an additive reconstruction layer. Its continuous full-series synthesis is written only after specialist documents have stabilized. AOT should use the same basic logic.

## 3. MHA V2 precedent: character-state and reconstruction separation

The MHA V2 architecture is particularly useful for keeping literary synthesis separate from reconstruction. A literary monograph about Eren, Mikasa, Armin, Reiner, or Historia is not the same artifact as a state-conditioned behavior/speech reconstruction model. AOT already has an even stronger prospective validation history and should preserve that distinction.

## 4. Youjo Senki precedent: military, institutional, ethical, and historiographic separation

The *Youjo Senki* corpus shows why tactical success, strategic effect, political purpose, institutional legitimacy, moral justification, individual authorship, and historical narration must be evaluated separately. AOT requires the same firewall, especially around the Rumbling, deterrence, coups, child soldiers, Titan inheritance, and coalition warfare.

## 5. AOT-specific requirements

AOT must add or emphasize several layers that the precedents do not provide in the same form:

- publication-boundary retrospective revision from V19 and V27 checkpoints;
- a frozen V01-V19 prospective character register with V20-V34 adjudication;
- manga-specific page, panel, spread, body, scale, spatial, and visual-motif analysis;
- Titan/Paths/body/memory ontology as both literal mechanism and personhood problem;
- contested historical testimony and source criticism;
- the separation of causal explanation, understanding, responsibility, justification, and absolution;
- final-volume causality and recurrence questions that require especially careful epistemic labeling.

AOT should therefore be structurally comparable to mature corpora without being forced into their exact folder trees.

---

# II. Authority stack after V34

The post-V34 corpus uses the following precedence.

1. **Original Japanese manga page** — final authority for exact wording, panel composition, page order, visual form, and disputed source claims.
2. **Canonical V2 volume deep reading** — volume-local interpretive and evidence-routing authority.
3. **Longitudinal ledgers and frozen prospective/adjudication infrastructure** — cumulative state and model-support evidence.
4. **Historical checkpoints** — authoritative for what could responsibly be synthesized at their own boundaries; they remain immutable historical authorities.
5. **Full-series claim-revision ledger and specialist syntheses** — current retrospective full-series analytical authorities for their designated questions.
6. **`AOT_FULL_SERIES_SYNTHESIS_V01-V34.md`** — integrated reader-facing full-series authority, written after specialist convergence.
7. **Full-series character reconstruction models** — derived behavioral/speech models, narrower in purpose than literary synthesis.
8. **Validation and cross-model consistency audits** — audits of derived model quality and scope.
9. **Generated hypothetical scenarios** — never evidence and never permitted to feed back upward into the corpus.

Two consequences follow.

First, the eventual full-series synthesis may supersede the V27 checkpoint as **current full-series interpretation**, but it does not make the V27 checkpoint wrong for its V01-V27 boundary. The checkpoint remains historical evidence of what the corpus supported before V28-V34.

Second, a reconstruction model may summarize a specialist character monograph, but it may not become the source from which the monograph is later rewritten. The evidence flow is one-way.

---

# III. Post-V34 directory architecture

The canonical analytical root remains unchanged. Do not create a parallel AOT root for the synthesis phase.

The mature structure should be:

```text
Attack on Titan/
├── CURRENT_STATE_AND_CORPUS_MAP.md
│
├── 00 Frameworks and Methods/
│   ├── AOT_ANALYTICAL_METHOD_V2.md
│   ├── AOT_PROJECT_DECISIONS_AND_CHECKPOINT_POLICY.md
│   ├── AOT_FULL_SERIES_SYNTHESIS_ARCHITECTURE_V1.md
│   ├── AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md
│   ├── AOT_CHARACTER_RECONSTRUCTION_AND_VALIDATION_METHOD_V1.md
│   └── AOT_CHARACTER_MODEL_SCHEMA_V1.md
│
├── 01 Source Lock and Inventory/
│   └── AOT_SOURCE_INVENTORY_V01-V34.md
│
├── 02 Sequential Readings/
│   └── AOT_V01_DEEP_READING.md ... AOT_V34_DEEP_READING.md
│
├── 03 Checkpoints and Longitudinal Ledgers/
│   ├── AOT_CHECKPOINT_50P_V01-V19_SYNTHESIS.md
│   ├── AOT_CHECKPOINT_75P_V01-V27_SYNTHESIS.md
│   ├── AOT_CHARACTER_MODEL_PROSPECTIVE_PREDICTION_REGISTER_V01-V19.md
│   ├── AOT_CHARACTER_MODEL_PROSPECTIVE_ADJUDICATION_LEDGER.md
│   ├── AOT_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md
│   ├── AOT_RELATIONSHIP_CONDITIONED_BEHAVIOR_LEDGER.md
│   ├── AOT_EVERYDAY_LIFE_PREFERENCES_AND_LOW_STAKES_BEHAVIOR_LEDGER.md
│   ├── AOT_JAPANESE_VOICE_AND_VOCABULARY_LEDGER.md
│   └── AOT_CHARACTER_MODEL_READINESS_AND_COVERAGE_LEDGER.md
│
├── 04 Specialist Synthesis/
│   └── [Documents 01-20 below, created as work begins]
│
├── 05 Full-Series Synthesis/
│   └── AOT_FULL_SERIES_SYNTHESIS_V01-V34.md
│
├── 06 Evidence and Indexes/
│   ├── AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md
│   ├── AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md
│   ├── AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv
│   ├── AOT_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md
│   ├── AOT_SYNTHESIS_CROSSWALK.md
│   ├── AOT_CLAIM_INDEX.json                         [optional]
│   └── AOT_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md [only if an English comparison corpus is supplied]
│
├── 07 Character Reconstruction and Validation/
│   ├── AOT_CHARACTER_MODEL_PROSPECTIVE_EXPERIMENT_REPORT.md
│   ├── AOT_CHAR_<NAME>_RECONSTRUCTION_MODEL.md
│   ├── AOT_CHARACTER_MODEL_VALIDATION_AUDIT.md
│   └── AOT_CROSS_MODEL_CONSISTENCY_AUDIT.md
│
├── 08 Audits and Manifests/
│   ├── AOT_MIGRATION_NOTES.md
│   ├── AOT_CORPUS_MANIFEST.md
│   ├── AOT_ARTIFACT_SHA256SUMS.txt
│   └── AOT_SYNTHESIS_PHASE_DELIVERY_AUDIT.md [at release]
│
└── 90 Legacy and Superseded/
    └── Conversation Archives/ [only when needed]
```

The folders `04`, `05`, `06`, `07`, and `90` should be instantiated only when they acquire substantive contents. Empty directories should not be created merely to make the tree look complete.

The sequential readings are now a completed evidence layer. They should not be retroactively rewritten to make early interpretation look omniscient. Corrections belong in revision infrastructure and later synthesis.

---

# IV. Specialist synthesis document map

The specialist layer is reader-facing analytical prose. Each document should have a single governing question and an explicit anti-duplication boundary.

The recommended reader order is numbered because the order is analytically meaningful. The filenames retain the stable `AOT_` identifier.

## `AOT_01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`
### From walls and extermination to plural sovereignty, causal authorship, and non-transferable responsibility

**Governing question:**

> How does the manga repeatedly replace its central problem, and what does the complete V01-V34 sequence become when later revelations are allowed to recontextualize—but not erase—the earlier publication experience?

**Primary responsibilities:**

- volume and arc progression;
- changes in genre mode;
- epistemic-world expansion;
- structural hinge volumes;
- transformation of the human/Titan problem;
- transformation of freedom from spatial horizon to political/ethical authorship;
- relation among V19, V27, and final-series theses;
- ending as structural culmination rather than a detached controversy;
- one mature master thesis plus serious competing formulations.

**Do not duplicate:** full Eren motive analysis, detailed political theory, detailed Titan mechanics, detailed visual-form analysis.

This should be the first substantial specialist essay drafted after evidence stabilization.

## `AOT_02_EREN_JAEGER_FREEDOM_DESIRE_CAUSALITY_AND_RESPONSIBILITY.md`

**Governing question:**

> What remains continuous in Eren across radically changing knowledge states, and how should desire, future memory, coercion, care, violence, self-authorship, and responsibility be related without reducing his terminal behavior to one motive?

**Primary responsibilities:**

- pre-Carla freedom desire;
- exterminatory language and its changing objects;
- outside-world imagination;
- Titan identity and bodily authorship;
- Historia nondisclosure and protection;
- Reiner recognition;
- post-timeskip self-conception;
- future-memory constraint;
- relationship to Armin, Mikasa, Zeke, Reiner, Historia, and the 104th;
- Rumbling motive as multi-causal;
- self-coercion and `進み続ける`;
- final self-accounting;
- responsibility without simplistic metaphysical voluntarism.

**Secondary homes:** final causality mechanics -> Document 19; general freedom philosophy -> Document 14; relationship-wide comparison -> Document 16.

## `AOT_03_MIKASA_ACKERMAN_LOVE_AGENCY_HOME_AND_MEMORY.md`

**Governing question:**

> How does Mikasa's attachment to Eren function as love, home, memory, obligation, autonomy problem, and eventually a basis for opposition without requiring emotional renunciation?

**Primary responsibilities:**

- childhood rescue and attachment formation;
- Ackerman claims and their evidentiary status;
- family/home language;
- combat protectiveness versus broader agency;
- scarf as object and relational sign;
- speech and silence;
- moral disagreement with Eren;
- V29-V34 separation between attachment and obedience;
- cabin sequence;
- killing Eren while retaining love;
- grief and postwar continuity.

**Anti-caricature requirement:** do not reduce Mikasa to "Eren obsession" or treat final opposition as proof that earlier attachment was false.

## `AOT_04_ARMIN_ARLERT_KNOWLEDGE_IMAGINATION_DIALOGUE_AND_RESPONSIBILITY.md`

**Governing question:**

> How does Armin turn imagination and incomplete knowledge into action, and what happens when a character associated with dialogue and possibility inherits command, mass violence, and postwar political responsibility?

**Primary responsibilities:**

- outside-world book and positive freedom horizon;
- inferential style;
- fear, self-doubt, and action;
- dialogue as method rather than pacifist identity;
- serum survival and inherited burden;
- Colossal Titan responsibility;
- modeling Eren under uncertainty;
- command after Hange;
- ordinary-life ontology in V34;
- narrative testimony and diplomacy;
- ethical limits of understanding.

## `AOT_05_REINER_BRAUN_ROLE_IDENTITY_GUILT_RECOGNITION_AND_SURVIVAL.md`

**Governing question:**

> How does Reiner's life expose the difference between imposed roles, sincerely inhabited roles, retrospective guilt, and continuing responsibility?

**Primary responsibilities:**

- childhood ideology and family motive;
- Marcel manipulation and survivor debt;
- Warrior/soldier role organization;
- 104th attachment as psychologically real;
- mission continuation and hero desire;
- guilt and suicide attempt;
- candidate children as relational tether;
- Eren/Reiner recognition;
- later alliance conduct;
- survival without clean redemption.

## `AOT_06_ZEKE_JAEGER_FAMILY_SALVATION_ANTINATALISM_AND_INSTRUMENTAL_REASON.md`

**Governing question:**

> How does Zeke convert childhood injury, Ksaver attachment, biological reasoning, and a salvation model into a coercive political project, and what exactly changes in the final Paths conversation?

**Primary responsibilities:**

- Grisha/Dina childhood pressure;
- betrayal and survival;
- Ksaver relationship;
- euthanasia reasoning;
- trust in Eren;
- command and strategic deception;
- instrumental treatment of bodies and reproduction;
- ordinary-life deficit and baseball/catch memory;
- Armin's intervention;
- voluntary exposure to Levi;
- revision rather than total repudiation of his earlier worldview.

## `AOT_07_HISTORIA_YMIR_IDENTITY_SOVEREIGNTY_AND_CHOSEN_OBLIGATION.md`

**Governing question:**

> What does the manga do with imposed names, inherited roles, royal bodies, chosen obligations, care, sovereignty, and reproductive instrumentalization through Historia and Ymir?

**Primary responsibilities:**

- Krista/Historia distinction;
- Ymir's imposed and chosen identities;
- mutual recognition;
- Uprising authorship;
- queenly office;
- orphan/farm institutional practice;
- royal-blood strategic burden;
- pregnancy and evidentiary limits;
- distinction between accepting responsibility and legitimating coercion;
- Ymir Fritz as separate historical/ontological figure only where comparison clarifies rather than conflates.

## `AOT_08_LEVI_ERWIN_HANGE_COMMAND_SACRIFICE_AND_SUCCESSION.md`

**Governing question:**

> How does Survey Corps command evolve when leaders must act under radical uncertainty, spend lives, preserve subordinates as persons, and hand responsibility to successors?

**Primary responsibilities:**

- Erwin's dream, secrecy, strategic ruthlessness, and legitimacy;
- Levi's uncertainty ethic and relationship-conditioned judgment;
- serum decision;
- Hange's knowledge practice and command burden;
- civil-military responsibility;
- sacrifice without reimbursement;
- leadership succession to Armin;
- Levi's V34 relation to the dead.

This is not a substitute for later individual reconstruction models for Levi, Erwin, or Hange.

## `AOT_09_104TH_WARRIORS_AND_GENERATIONAL_ENSEMBLE_BELONGING_BETRAYAL_AND_REPAIR.md`

**Governing question:**

> How does the series turn cohorts trained to divide humanity into enemies into networks of friendship, rivalry, betrayal, inherited hatred, and partial repair?

**Primary responsibilities:**

- 104th social world;
- Jean, Connie, Sasha, Annie, Bertolt, Marco and others as independent agents;
- Warrior peer relations;
- Gabi/Falco and candidate generation;
- Kaya/Gabi and recursive grievance;
- alliance formation;
- reunion without moral erasure;
- humor, food, teasing, domestic fragments, and ordinary group life;
- generational change in enemy recognition.

## `AOT_10_STATES_EMPIRE_NATIONALISM_LEGITIMACY_AND_POLITICAL_VIOLENCE.md`

**Governing question:**

> What makes political authority comparatively legitimate in a world where every major state or faction uses secrecy, coercion, historical narrative, sacrifice, and emergency power?

**Primary responsibilities:**

- Walls monarchy and memory regime;
- Uprising and comparative legitimacy;
- military government;
- Marleyan imperial structure;
- Tybur political theater;
- internment regime;
- Paradis after the sea;
- Volunteers;
- Yeagerists;
- coups, detention, assassination, emergency authority;
- alliance diplomacy;
- post-Rumbling Paradis militarization;
- legitimacy versus mere control.

**Required distinction:** tactical/strategic necessity cannot by itself settle political legitimacy or ethical justification.

## `AOT_11_WAR_STRATEGY_LOGISTICS_TECHNOLOGY_AND_DETERRENCE.md`

**Governing question:**

> How do military means, logistical constraints, technology, intelligence, deterrence, and organizational learning shape what actors can plausibly choose without determining what they ought to choose?

**Primary responsibilities:**

- Survey Corps operational adaptation;
- ODM technology and spatial doctrine;
- Titans as weapons and strategic infrastructure;
- Shiganshina operations;
- Marleyan combined-arms doctrine;
- anti-Titan technological change;
- Liberio raid;
- Paradis modernization;
- Rumbling as deterrent proposal versus exterminatory execution;
- alliance logistics and command;
- civilian distinction;
- tactical, operational, strategic, political, and ethical outcome separation.

**Do not place here:** the complete moral judgment of the Rumbling; that requires Documents 10, 14, 16, and 19 as well.

## `AOT_12_RACE_MEMORY_HISTORY_PROPAGANDA_AND_ENEMY_CONSTRUCTION.md`

**Governing question:**

> How do states, families, movements, and individuals convert incomplete history into identities of victim, devil, hero, traitor, and enemy—and what epistemic practices allow those categories to be revised?

**Primary responsibilities:**

- controlled history inside the Walls;
- Grisha's archive;
- Marleyan official history;
- Restorationist counter-history;
- Kruger's source skepticism;
- inherited memories as evidence and distortion;
- propaganda and child formation;
- `悪魔` / `人` category revision;
- Willy's staged public narrative;
- nationalism and collective responsibility;
- testimony, archives, photographs, memories, and interested sources;
- postwar storytelling and diplomacy.

The document must preserve a strict distinction among **textual fact, character belief, state narrative, interested testimony, strong inference, and unresolved historical claim**.

## `AOT_13_TITANS_PATHS_BODY_MEMORY_INHERITANCE_AND_PERSONHOOD_ONTOLOGY.md`

**Governing question:**

> What does the manga actually establish about Titans, Subjects of Ymir, Paths, memory, bodily transformation, inheritance, and the relation between mechanism and personhood?

**Primary responsibilities:**

- human/Titan category collapse;
- shifter and mindless-Titan continuity;
- Founder and royal-blood conditions;
- memory transmission;
- bodily succession;
- Paths evidence by publication stage;
- Ymir Fritz;
- inherited Titan forms;
- body reconstruction;
- Titan curse ending;
- literal mechanics versus symbolic interpretation;
- epistemic uncertainty where mechanism remains underdetermined.

**Methodological rule:** do not deny symbolic force because a mechanism is literal, and do not infer mechanics from symbolism.

## `AOT_14_FREEDOM_AUTONOMY_PERSONHOOD_INHERITANCE_AND_RESPONSIBILITY.md`

**Governing question:**

> What does "freedom" become across the complete manga once multiple persons and institutions claim self-authorship at the same time?

**Primary responsibilities:**

- spatial freedom and the outside world;
- negative and positive freedom;
- authorship under inherited constraints;
- consent and bodily instrumentalization;
- selected attachment versus imposed purpose;
- protection and sovereignty;
- recognition and personhood;
- future knowledge and responsibility;
- freedom versus unlimited permission;
- love without obedience;
- understanding without exoneration;
- non-transferable responsibility.

This is the primary philosophical home. Character documents should cite it rather than independently rebuilding the complete theory of freedom.

## `AOT_15_CHILDHOOD_HOME_FAMILY_ORDINARY_LIFE_AND_THE_FUTURE.md`

**Governing question:**

> What kinds of life does the manga imply are worth protecting once military glory, inherited mission, reproductive duty, and historical destiny are stripped of their claim to be sufficient purposes?

**Primary responsibilities:**

- childhood as target of inherited projects;
- parents and children;
- Grisha, Carla, Braun family, candidate families, Ackerman family, Reiss family;
- "children in the forest";
- home and return;
- food, markets, farms, training, teasing, reading, games, ordinary work;
- Sasha and appetite;
- Falco/Gabi future imagination;
- Armin/Zeke ordinary moments;
- postwar family and memory;
- birth and unconditional worth;
- ordinary life as anti-instrumental value.

This document is also the literary counterpart to the reconstruction layer's everyday-life bias correction.

## `AOT_16_RELATIONSHIPS_LOVE_LOYALTY_RECOGNITION_BETRAYAL_AND_NONPOSSESSION.md`

**Governing question:**

> How do intimate and social relationships alter action without granting ownership over another person's choices?

**Primary responsibilities:**

- Eren/Mikasa/Armin triad;
- Historia/Ymir;
- Reiner/104th;
- Levi/Erwin;
- Zeke/Ksaver and Zeke/Eren;
- Gabi/Falco;
- Annie/father;
- Jean/Marco and survivor memory;
- trust under uncertainty;
- betrayal without dehumanization;
- recognition without reconciliation;
- protection versus jurisdiction;
- attachment without possession;
- grief and continuing bonds.

Character monographs own individual development. This document owns the **cross-series theory of relationship-conditioned agency**.

## `AOT_17_JAPANESE_LANGUAGE_NAMES_REGISTER_KEY_TERMS_AND_TRANSLATION_SENSITIVITIES.md`

**Governing question:**

> Which Japanese lexical, grammatical, naming, address, and register patterns carry analytical distinctions that are weakened by summary or translation?

**Primary responsibilities:**

- `自由`;
- `駆逐`;
- `戦え`;
- `進み続ける`;
- `生まれてきた`;
- `特別` / ordinary-worth language;
- `悪魔` / `人`;
- `家族`, home/return vocabulary;
- `信頼` and related trust language;
- pronouns and address terms;
- role/title language;
- command register;
- relationship-conditioned speech shifts;
- naming/renaming and identity;
- translation-sensitive ambiguity.

This document concerns written manga language. Anime vocal performance remains outside scope unless activated as a later adaptation layer.

## `AOT_18_MANGA_FORM_VISUAL_GRAMMAR_SPACE_BODY_AND_MOTIFS.md`

**Governing question:**

> How does the manga make its arguments through page construction, spatial scale, bodily representation, visual rhyme, recurring objects, and the changing geometry of confinement and freedom?

**Primary responsibilities:**

- walls, gates, horizons, forests, basements, seas, cities, internment zones, battlefields;
- verticality and scale;
- Titan/human body relation;
- napes, mouths, eyes, hands, fragments, corpses;
- page turns and reveal mechanics;
- double spreads;
- crowd geometry;
- memory-image recurrence;
- scarf, key, photograph, book, baseball, leaf, tree and other load-bearing objects;
- opening/final tree relation;
- visual reversals between early and late war imagery.

**Evidence requirement:** this document cannot be responsibly produced only from prose deep readings. Load-bearing claims must trigger selective CBZ restoration and direct page/spread verification.

## `AOT_19_ENDING_CAUSALITY_MEMORY_HISTORICAL_RECURRENCE_AND_POSTWAR_TIME.md`

**Governing question:**

> What does the final movement establish about future memory, causal constraint, Eren's agency, Ymir's release, the end of Titan power, political aftermath, and historical recurrence—and which popular total explanations exceed the manga's evidence?

**Primary responsibilities:**

- Attack Titan/future-memory evidence chain;
- causal loop claims and limits;
- Eren's terminal self-accounting;
- Ymir/Mikasa relation and evidentiary caution;
- Titan-power termination;
- peace delegation;
- Paradis militarization;
- Mikasa's postwar life and memory;
- tankobon-added future epilogue;
- destruction and regrowth;
- final tree;
- recurrence possibility versus deterministic repetition;
- counterreadings of the ending.

This document should be written late, after Documents 02, 03, 04, 06, 12, 13, and 14 have stabilized, so it does not use the ending as a shortcut that flattens the whole series.

## `AOT_20_REFERENCE_MATRICES_COUNTERREADINGS_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`

**Governing question:**

> Which conclusions survive cross-document comparison, where do serious alternative readings remain viable, and what should future comparative or adaptation work retrieve first?

**Primary responsibilities:**

- character/value matrices;
- institution/legitimacy comparison;
- violence/responsibility comparison;
- freedom formulations by phase;
- source-type and epistemic-confidence matrix;
- preserved counterreadings;
- unresolved contradictions;
- genuinely open questions;
- adaptation-comparison hooks without importing adaptation evidence;
- concise cross-project comparison hooks for later corpus-wide work.

This is a reference and adversarial-audit document, not another master essay.

---

# V. Evidence and revision infrastructure

The specialist layer must not be drafted directly from memory of thirty-four essays. The evidence layer is the first production responsibility after this architecture is locked.

## 1. `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md` — **next canonical operation**

This is the first post-architecture artifact.

It should route:

- the major V19 checkpoint claims;
- the major V27 checkpoint claims;
- V28-V34 post-checkpoint deltas;
- any earlier high-value volume hypotheses that remained open into later volumes;
- important character-model claims whose final status matters to literary synthesis.

For each claim, record:

- stable claim ID;
- earlier formulation;
- boundary at which it was authoritative;
- final V01-V34 formulation;
- transition state: `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`;
- primary specialist home;
- supporting volumes/evidence IDs;
- contradicting or complicating evidence;
- confidence;
- primary-source verification requirement.

A revision does not retroactively mark the older checkpoint as defective. It records what later evidence changed.

This ledger is the main firewall against two opposite failures:

1. treating the V27 checkpoint as if the ending did not happen; and
2. treating the ending as if every earlier uncertainty had always been obvious.

## 2. `AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md`

This matrix maps each volume to the specialist homes it materially supports.

Recommended columns:

- volume;
- major evidence IDs;
- architecture/progression;
- character monographs affected;
- political/institutional;
- military;
- history/propaganda;
- ontology;
- freedom/personhood;
- childhood/ordinary life;
- relationships;
- Japanese language;
- visual form;
- ending/causality;
- source reinspection priority.

The purpose is retrieval and coverage auditing, not plot summary.

## 3. `AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv`

This should contain the load-bearing page-level locators needed by the final synthesis corpus.

Recommended fields:

- locator ID;
- volume;
- chapter;
- internal CBZ image filename;
- sequential page index;
- printed page if verified;
- short Japanese anchor;
- panel/spread description;
- evidence type;
- linked claim IDs;
- linked specialist document;
- verification status.

Do not attempt to index every panel in the manga. Prioritize claims whose wording, facial expression, page turn, visual rhyme, or spatial construction materially affects interpretation.

## 4. `AOT_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md`

This grows during specialist drafting and consolidates exact short passages, lexical clusters, address terms, and translation-sensitive anchors.

It is a retrieval layer, not permission to reproduce long copyrighted passages.

## 5. `AOT_SYNTHESIS_CROSSWALK.md`

Created after the specialist layer is substantially complete.

For each major final-series claim, route:

> final synthesis section -> primary specialist home -> claim-revision entry -> deep-reading/evidence ID -> primary-source locator when required.

This is the main traceability surface for future comparative work.

## 6. Optional `AOT_CLAIM_INDEX.json`

Useful if the corpus becomes large enough that machine retrieval benefits from structured fields:

- claim ID;
- formulation;
- status;
- primary home;
- evidence volumes;
- locators;
- confidence;
- revision history.

Do not create it merely because another series has one.

## 7. Translation audit remains conditional

`AOT_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` should be created only if an English comparison corpus is supplied or a specific translation question becomes analytically important. The Japanese manga remains governing authority either way.

---

# VI. Drafting order versus reader order

The reader-facing specialist package is numbered 01-20, but production should follow evidence dependency rather than filename order.

## Reasoning-class policy for post-V34 production

The durable recommendation for each artifact is a **stable reasoning class** defined by `MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`. Literal provider/model names are a time-bounded mapping and may change without changing the architectural class.

Current mapping verified by the corpus-wide policy on 2026-08-27:

| Stable class | Current provider mapping | Architectural use |
|---|---|---|
| `ROUTINE_FAST` | `5.6 Sol Instant` | Deterministic or clerical operations where added interpretive work has negligible value. |
| `BOUNDED_STANDARD` | `5.6 Sol Medium` | Bounded, structured, readily auditable extraction/routing/administration. |
| `SUBSTANTIVE_ANALYSIS` | `5.6 Sol High` | Serious but well-bounded analysis with manageable interaction and ambiguity. |
| `DEEP_SYNTHESIS` | `5.6 Sol Extra High` | High-dimensional integration, retrospective dependence, state complexity, or contradiction handling. |
| `PREMIUM_QUALITY_FIRST` | `5.6 Sol Pro` | Select propagation-sensitive work where additional model work has a plausible material reliability advantage. |

A document's class governs its **substantive final drafting/adjudication pass**. Retrieval, checksum calculation, mechanical extraction, locator harvesting, or other bounded support work should use the class appropriate to that support operation rather than automatically inheriting a premium class from the final document.

For Markdown artifacts created under this roadmap, front matter should normally record both layers, for example:

```yaml
recommended_reasoning_class: DEEP_SYNTHESIS
current_provider_mapping: "5.6 Sol Extra High"
reasoning_policy_source: "MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md v1.0"
series_routing_source: "AOT_FULL_SERIES_SYNTHESIS_ARCHITECTURE_V1.md v1.2"
```

TSV, JSON, checksum, and other machine-oriented artifacts may rely on this architecture as the authoritative routing registry rather than embedding prose metadata.

### Fixed-document reasoning table

| Phase | Artifact | Stable reasoning class | Current provider mapping | Why this class is appropriate |
|---|---|---|---|---|
| 1 | `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Global V19/V27-to-V34 re-adjudication; errors propagate into every specialist home. |
| 1 | `AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Broad evidence routing and coverage audit, but bounded once claim states are stabilized. |
| 1 | `AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv` | **`BOUNDED_STANDARD`** | **`5.6 Sol Medium`** | Primarily verification and structured locator work; interpretation should remain minimal. |
| 1+ | `AOT_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Requires linguistic discrimination and evidence selection, but not whole-corpus thesis integration on every entry. |
| 1+ optional | `AOT_CLAIM_INDEX.json` | **`BOUNDED_STANDARD`** | **`5.6 Sol Medium`** | Structured serialization of already-adjudicated claims; no independent thesis generation. |
| Conditional | `AOT_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Translation-sensitive semantic/pragmatic distinctions can alter interpretation and require careful Japanese-primary comparison. |
| 2 | `AOT_01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Whole-series structural synthesis, but supported by the completed revision ledger and evidence matrix. |
| 3 | `AOT_02_EREN_JAEGER_FREEDOM_DESIRE_CAUSALITY_AND_RESPONSIBILITY.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Highest-density motive, temporal-causality, responsibility, relationship, and endpoint integration problem in the corpus. |
| 3 | `AOT_03_MIKASA_ACKERMAN_LOVE_AGENCY_HOME_AND_MEMORY.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Longitudinal relationship/agency analysis with major final-volume recontextualization and anti-caricature requirements. |
| 3 | `AOT_04_ARMIN_ARLERT_KNOWLEDGE_IMAGINATION_DIALOGUE_AND_RESPONSIBILITY.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Requires reconciling epistemic style, command, dialogue, violence, testimony, and responsibility across changing roles. |
| 3 | `AOT_05_REINER_BRAUN_ROLE_IDENTITY_GUILT_RECOGNITION_AND_SURVIVAL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Multiple sincerely inhabited roles, guilt states, enemy recognition, and survival/redemption distinctions require state-sensitive synthesis. |
| 3 | `AOT_06_ZEKE_JAEGER_FAMILY_SALVATION_ANTINATALISM_AND_INSTRUMENTAL_REASON.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Dense ideological, familial, biological, strategic, and terminal-revision reasoning. |
| 3 | `AOT_07_HISTORIA_YMIR_IDENTITY_SOVEREIGNTY_AND_CHOSEN_OBLIGATION.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Identity, bodily sovereignty, chosen obligation, inheritance, and reproductive instrumentalization cross several arcs. |
| 3 | `AOT_08_LEVI_ERWIN_HANGE_COMMAND_SACRIFICE_AND_SUCCESSION.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Multi-character command ethics and succession require separating relationship-conditioned judgment from doctrine. |
| 3 | `AOT_09_104TH_WARRIORS_AND_GENERATIONAL_ENSEMBLE_BELONGING_BETRAYAL_AND_REPAIR.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Large ensemble with asymmetric relationships, faction migration, betrayal, repair, and distributed agency. |
| 4 | `AOT_10_STATES_EMPIRE_NATIONALISM_LEGITIMACY_AND_POLITICAL_VIOLENCE.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Comparative institutional and legitimacy analysis across multiple regimes/factions; deep but topically bounded. |
| 4 | `AOT_11_WAR_STRATEGY_LOGISTICS_TECHNOLOGY_AND_DETERRENCE.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Must keep tactical, operational, strategic, political, and ethical success separate across many campaigns. |
| 4 | `AOT_12_RACE_MEMORY_HISTORY_PROPAGANDA_AND_ENEMY_CONSTRUCTION.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Requires source criticism, ideology analysis, historical testimony, propaganda, and dehumanization without collapsing actor positions. |
| 4 | `AOT_13_TITANS_PATHS_BODY_MEMORY_INHERITANCE_AND_PERSONHOOD_ONTOLOGY.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Mechanistic and philosophical claims are deeply intertwined; exact uncertainty boundaries matter. |
| 4 | `AOT_14_FREEDOM_AUTONOMY_PERSONHOOD_INHERITANCE_AND_RESPONSIBILITY.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Central philosophical synthesis across the whole series, but should consume already-stabilized institutional/ontological findings. |
| 5 | `AOT_15_CHILDHOOD_HOME_FAMILY_ORDINARY_LIFE_AND_THE_FUTURE.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Rich longitudinal synthesis with lower causal/mechanistic ambiguity than the central political/ontological documents. |
| 5 | `AOT_16_RELATIONSHIPS_LOVE_LOYALTY_RECOGNITION_BETRAYAL_AND_NONPOSSESSION.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Directed relationship states and recognition/nonpossession distinctions require broad cross-character integration. |
| 5 | `AOT_17_JAPANESE_LANGUAGE_NAMES_REGISTER_KEY_TERMS_AND_TRANSLATION_SENSITIVITIES.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Japanese-primary semantic, register, address, naming, and translation-sensitive synthesis across 34 volumes. |
| 5 | `AOT_18_MANGA_FORM_VISUAL_GRAMMAR_SPACE_BODY_AND_MOTIFS.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Cross-volume visual/formal argument requires precise page evidence and restraint against thematic over-reading. |
| 5 | `AOT_19_ENDING_CAUSALITY_MEMORY_HISTORICAL_RECURRENCE_AND_POSTWAR_TIME.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Final-volume causal architecture, future memory, responsibility, epilogue recurrence, and competing interpretations are unusually entangled and contested. |
| 6 | `AOT_20_REFERENCE_MATRICES_COUNTERREADINGS_CONTRADICTIONS_AND_OPEN_QUESTIONS.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Deliberately adversarial cross-document convergence; must find contradictions rather than merely summarize prior work. |
| 6 | `AOT_SYNTHESIS_CROSSWALK.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | High-coverage traceability work after specialist conclusions stabilize; mainly routing rather than new interpretation. |
| 7 | `AOT_FULL_SERIES_SYNTHESIS_V01-V34.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Highest-level integration of the complete specialist corpus into one non-duplicative, internally consistent full-series argument. |
| 8 | `AOT_CHARACTER_MODEL_PROSPECTIVE_EXPERIMENT_REPORT.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Requires careful interpretation of the frozen V01-V19 construction set and V20-V34 adjudication without overstating predictive warrant. |
| 8 | `AOT_CHAR_EREN_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Highly state-dependent model, but narrower and more evidence-constrained than the Pro literary monograph. |
| 8 | `AOT_CHAR_MIKASA_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Relationship-conditioned behavior, sparse ordinary-life evidence, and major terminal state change require caution. |
| 8 | `AOT_CHAR_ARMIN_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Broad epistemic/command/social repertoire with materially different low- and high-stakes modes. |
| 8 | `AOT_CHAR_REINER_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Strong temporal/role-state variation and guilt-conditioned behavior make timeless personality compression especially dangerous. |
| 8 | `AOT_CHAR_JEAN_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Good longitudinal behavioral coverage with comparatively tractable state partitioning. |
| 8 | `AOT_CHAR_HISTORIA_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Identity/role changes and sparse later ordinary-life evidence require careful uncertainty handling. |
| 8 | `AOT_CHAR_LEVI_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Strong command/relationship evidence but substantial injury/state and crisis-sampling effects. |
| 8 | `AOT_CHAR_ERWIN_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Extensive command evidence with a relatively bounded historical state range and clear domain limits. |
| 8 | `AOT_CHAR_HANGE_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Strong recurring voice/behavior evidence and command transition, with manageable state complexity. |
| 8 | `AOT_CHAR_ANNIE_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Good diagnostic relationship/mission evidence but narrower ordinary-life coverage; explicit uncertainty can carry the gap. |
| 8 | `AOT_CHAR_ZEKE_RECONSTRUCTION_MODEL.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Ideological, familial, strategic, deceptive, and terminally revised states require careful partitioning. |
| 8 | `AOT_CHAR_GABI_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Strong developmental trajectory and relationship evidence; state changes are substantial but well observed. |
| 8 | `AOT_CHAR_FALCO_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Consistent behavioral and relational repertoire with fewer contradictory state regimes than Tier-A cases. |
| 8 | Any additional readiness-promoted `AOT_CHAR_<STABLE_NAME>_RECONSTRUCTION_MODEL.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Default for later models; escalate to Extra High when state/voice/relationship complexity materially exceeds the standard case. Pro requires explicit new justification. |
| 8 | `AOT_CHARACTER_MODEL_VALIDATION_AUDIT.md` | **`DEEP_SYNTHESIS`** | **`5.6 Sol Extra High`** | Adversarial per-model validation across multiple domains and scenario distances. |
| 8 | `AOT_CROSS_MODEL_CONSISTENCY_AUDIT.md` | **`PREMIUM_QUALITY_FIRST`** | **`5.6 Sol Pro`** | Suite-level audit must reconcile directed relationships, knowledge states, timeline boundaries, and distinct voices across all generated models. |
| 9 | `AOT_SYNTHESIS_PHASE_DELIVERY_AUDIT.md` | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Release gate requires careful authority, completeness, provenance, and routing checks, though not new literary interpretation. |
| 9 | `00_README_AND_CORPUS_MAP.md` when the corpus is frozen | **`SUBSTANTIVE_ANALYSIS`** | **`5.6 Sol High`** | Final entrypoint must compress the mature authority map accurately without creating new claims. |
| 9 maintenance | `AOT_CORPUS_MANIFEST.md` update | **`BOUNDED_STANDARD`** | **`5.6 Sol Medium`** | Mostly deterministic inventory/authority maintenance with modest judgment. |
| 9 maintenance | `AOT_ARTIFACT_SHA256SUMS.txt` regeneration | **`ROUTINE_FAST`** | **`5.6 Sol Instant`** | Pure checksum/integrity operation; additional reasoning provides no meaningful benefit. |
| Ongoing maintenance | `CURRENT_STATE_AND_CORPUS_MAP.md` update | **`BOUNDED_STANDARD`** | **`5.6 Sol Medium`** | Routing/state maintenance; judgment is bounded by already-canonical artifacts. |
| Ongoing maintenance | `MANGA_ANIME_DRIVE_INDEX.md` update | **`BOUNDED_STANDARD`** | **`5.6 Sol Medium`** | Cross-project routing update; accuracy and concurrency control matter more than deep interpretation. |

### Premium allocation rule

The current fixed roadmap contains **six default `PREMIUM_QUALITY_FIRST` artifacts**:

1. `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md`;
2. `AOT_02_EREN_JAEGER_FREEDOM_DESIRE_CAUSALITY_AND_RESPONSIBILITY.md`;
3. `AOT_19_ENDING_CAUSALITY_MEMORY_HISTORICAL_RECURRENCE_AND_POSTWAR_TIME.md`;
4. `AOT_20_REFERENCE_MATRICES_COUNTERREADINGS_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`;
5. `AOT_FULL_SERIES_SYNTHESIS_V01-V34.md`;
6. `AOT_CROSS_MODEL_CONSISTENCY_AUDIT.md`.

These assignments are preserved because each operation has unusually high propagation sensitivity, integration breadth, contradiction density, adversarial burden, or suite-level consistency risk. The current provider mapping is `5.6 Sol Pro`, but that literal mapping is not permanent architecture.

Do **not** add premium execution merely because a subject is important, controversial, long, or prominent. Escalation beyond these six defaults requires a concrete expected reliability gain. Conversely, if representative `DEEP_SYNTHESIS` work demonstrates equivalent contradiction detection, evidence coverage, state preservation, and cross-document consistency, apply the corpus-wide downgrade rule rather than treating premium status as intrinsic to the filename.

## Phase 0 — Architecture lock and administrative registration

**Output:** `AOT_FULL_SERIES_SYNTHESIS_ARCHITECTURE_V1.md`

Tasks:

- register the architecture in the current-state map;
- register it in the corpus manifest/checksum registry;
- update the master Drive index;
- correct stale V33-current wording in the current-state map;
- identify `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md` as the next operation.

No specialist essay should begin before Phase 0 is complete.

## Phase 1 — Retrospective evidence stabilization

Production order:

1. `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md`;
2. `AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md`;
3. seed `AOT_PRIMARY_SOURCE_LOCATOR_INDEX_V01-V34.tsv` from existing verified locators;
4. seed `AOT_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md` from existing language ledger and load-bearing deep-reading anchors.

Phase gate:

- every major V19 and V27 claim has a final transition state or explicitly remains `OPEN`;
- V28-V34 evidence is routed rather than merely appended;
- no major specialist question lacks a retrieval path.

## Phase 2 — Macroarchitecture

Draft:

- `AOT_01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`.

This establishes the mature structural map and provisional final-series master thesis. It may still be revised after specialist work, but it should not attempt to answer all specialist questions itself.

## Phase 3 — Core character monographs

Recommended order:

1. Eren;
2. Mikasa;
3. Armin;
4. Reiner;
5. Zeke;
6. Historia/Ymir;
7. Levi/Erwin/Hange command-succession study;
8. 104th/Warrior/generational ensemble.

Why this order:

- Eren, Mikasa, and Armin define the central relational and philosophical triangle;
- Reiner and Zeke expose the strongest enemy/kinship/motive counterstructures;
- Historia/Ymir clarifies authorship, inheritance, and bodily sovereignty;
- command and ensemble documents then distribute agency beyond protagonist-centered readings.

Phase gate:

- each character thesis is time-indexed where necessary;
- later knowledge does not erase earlier real states;
- responsibility is distinguished from causal explanation;
- literary monographs do not claim to be simulation models.

## Phase 4 — Political, military, historical, ontological, and philosophical specialists

Recommended order:

1. States/empire/nationalism/legitimacy;
2. War/strategy/logistics/technology/deterrence;
3. Race/memory/history/propaganda/enemy construction;
4. Titans/Paths/body/memory/inheritance/personhood ontology;
5. Freedom/autonomy/personhood/inheritance/responsibility.

The philosophy document comes after the institutional and ontological specialists so that it does not float free of the actual mechanisms and political arrangements characters confront.

## Phase 5 — Social, linguistic, visual, and ending specialists

Recommended order:

1. Childhood/home/family/ordinary life/future;
2. Relationships/love/loyalty/recognition/nonpossession;
3. Japanese language/names/register/key terms;
4. Manga form/visual grammar;
5. Ending/causality/memory/recurrence/postwar time.

The ending specialist is deliberately late. It should synthesize already-stabilized claims rather than dictate them retrospectively.

## Phase 6 — Adversarial convergence and reference layer

Create:

- `AOT_20_REFERENCE_MATRICES_COUNTERREADINGS_CONTRADICTIONS_AND_OPEN_QUESTIONS.md`;
- `AOT_SYNTHESIS_CROSSWALK.md`.

Run a cross-document audit for:

- duplicate primary homes;
- incompatible definitions of freedom, responsibility, personhood, recognition, or legitimacy;
- accidental treatment of character belief as fact;
- inconsistent Eren motive claims;
- inconsistent Paths/future-memory mechanics;
- relationship-state contradictions;
- visual claims lacking source verification;
- post-hoc certainty leaking into early-volume description;
- language claims unsupported by Japanese evidence.

Where two readings remain genuinely defensible, preserve the disagreement rather than forcing false convergence.

## Phase 7 — Continuous full-series synthesis

Only after Phases 1-6 stabilize should the project write:

`AOT_FULL_SERIES_SYNTHESIS_V01-V34.md`

This is the integrated final literary synthesis required by the original analytical method.

It should **not** be a concatenation of specialist summaries. Its function is to answer:

> What does *Attack on Titan* ultimately become as a complete work, and how do its character, political, ontological, formal, and ethical systems constrain one another?

Recommended scale: approximately **25,000-40,000 words**, expandable only when integration genuinely requires it. The specialist corpus may be much larger. The continuous synthesis should earn compression by relying on specialist homes.

Recommended high-level structure:

1. mature series thesis and strongest counter-thesis;
2. narrative transformation across V01-V34;
3. character integration centered on Eren/Mikasa/Armin but not restricted to them;
4. politics, institutions, war, and historical testimony;
5. Titan/Paths ontology and bodily inheritance;
6. freedom, personhood, love, recognition, and responsibility;
7. ordinary life, childhood, home, and future;
8. manga form and Japanese-language findings that materially change interpretation;
9. ending, causal responsibility, and recurrence;
10. what the manga resolves, what it deliberately leaves unresolved, and what later adaptation/comparative work must not assume.

A concise executive README may eventually summarize this corpus, but it should be written after the conclusions stabilize.

## Phase 8 — Full-series character reconstruction and validation

The character-modeling architecture already requires full-series reconstruction to follow V34 **and full-series synthesis**. This architecture preserves that gate.

First create:

`AOT_CHARACTER_MODEL_PROSPECTIVE_EXPERIMENT_REPORT.md`

It should summarize, without modifying the frozen records:

- construction boundary V01-V19;
- adjudication boundary V20-V34;
- final eligible-event tally;
- domains in which predictions were strong;
- domains that remained weak or sparsely sampled;
- important PARTIAL/CONFOUNDED lessons;
- what the experiment does and does not warrant about novel-situation simulation.

Then generate reconstruction models only for characters whose readiness ledger warrants them.

Use the existing naming convention:

`AOT_CHAR_<STABLE_NAME>_RECONSTRUCTION_MODEL.md`

Likely high-priority candidates include Eren, Mikasa, Armin, Reiner, Jean, Historia, Levi, Erwin, and Hange, with Annie, Zeke, Gabi, Falco, and others promoted only according to final domain-specific readiness. The roster is **not** a completion checklist.

Every model must preserve:

- time-indexed states;
- knowledge state;
- role state;
- relationship-conditioned behavior;
- low-stakes control samples;
- Japanese written-voice evidence;
- negative constraints;
- scenario-distance limits;
- explicit `NO_EVIDENCE` where appropriate.

After individual models:

1. run `AOT_CHARACTER_MODEL_VALIDATION_AUDIT.md`;
2. run `AOT_CROSS_MODEL_CONSISTENCY_AUDIT.md`.

The cross-model audit must test:

- directed relationship consistency;
- timeline leakage;
- convergence of distinct voices into generic prose;
- contradictory knowledge states;
- crisis-state overfitting;
- inappropriate transfer into unsupported ordinary/modern scenarios;
- whether one character's model assumes another character behaves differently from that character's own model.

Generated scenario outputs remain outside the evidence corpus.

## Phase 9 — Release administration and freeze

Once the specialist corpus, continuous synthesis, evidence indexes, and intended reconstruction suite are complete:

- update `AOT_CORPUS_MANIFEST.md`;
- regenerate `AOT_ARTIFACT_SHA256SUMS.txt`;
- create `AOT_SYNTHESIS_PHASE_DELIVERY_AUDIT.md`;
- audit every authority/supersession field;
- ensure frozen historical checkpoints and prospective register remain unchanged;
- confirm all current claims route to a canonical home;
- archive redundant chat transcripts only after structured artifacts preserve their unique content;
- create `00_README_AND_CORPUS_MAP.md` if the corpus is explicitly frozen as a completed release.

Until that release freeze, `CURRENT_STATE_AND_CORPUS_MAP.md` remains the one canonical first-read entrypoint.

---

# VII. Primary-home and anti-duplication rules

The following routing rules are mandatory.

| Question | Primary home |
|---|---|
| What does the series become over time? | AOT_01 series architecture/progression |
| What is Eren's complete character/motive architecture? | AOT_02 Eren |
| How does Mikasa combine love and agency? | AOT_03 Mikasa |
| How does Armin combine knowledge, dialogue, command, and violence? | AOT_04 Armin |
| What is Reiner's role/identity/guilt structure? | AOT_05 Reiner |
| What is Zeke's salvation/antinatalism architecture? | AOT_06 Zeke |
| How do Historia/Ymir illuminate identity and bodily sovereignty? | AOT_07 Historia/Ymir |
| How does Survey Corps command handle uncertainty/sacrifice/succession? | AOT_08 Levi/Erwin/Hange |
| How do cohorts and generations transform belonging/enmity? | AOT_09 ensemble |
| What makes institutions legitimate or illegitimate? | AOT_10 politics/institutions |
| What are the military means and strategic constraints? | AOT_11 war/strategy/logistics |
| How are enemy identities and historical narratives produced? | AOT_12 history/propaganda |
| What does the manga establish about Titans/Paths/body/memory? | AOT_13 ontology |
| What is the mature philosophical theory of freedom/personhood/responsibility? | AOT_14 philosophy |
| What ordinary life/future is being protected? | AOT_15 childhood/home/ordinary life |
| How do relationships alter agency without becoming possession? | AOT_16 relationships |
| Which Japanese-language distinctions matter? | AOT_17 language |
| How does manga form carry meaning? | AOT_18 visual/form |
| What exactly does the ending establish? | AOT_19 ending/causality |
| What disagreements/open questions remain? | AOT_20 matrices/counterreadings |
| How did checkpoint claims change? | full-series claim-revision ledger |
| Where is the primary evidence? | locator index / deep reading / CBZ |
| What would a character plausibly do in a novel situation? | reconstruction model, after synthesis |

A subject may appear in several documents because AOT is structurally interconnected. Duplication becomes a problem when two files attempt to be the definitive home for the same question.

Use short cross-references such as:

> Eren's complete motive architecture is developed in AOT_02; the present document uses only the portion necessary to evaluate political responsibility.

That is preferable to reproducing the full argument.

---

# VIII. Claim and evidence standards for the retrospective phase

## 1. Epistemic labels

Specialist documents should distinguish at least:

- **TEXTUAL FACT** — directly established by the manga;
- **CHARACTER BELIEF** — what a character believes or claims;
- **IN-WORLD HISTORICAL CLAIM** — testimony/archive/state narrative whose truth may be partial or interested;
- **STRONG INFERENCE** — best explanation of convergent evidence;
- **INTERPRETIVE THESIS** — literary/philosophical reading;
- **SPECULATION** — plausible but underdetermined;
- **VALUE JUDGMENT** — normative evaluation.

These categories are especially important for ancient Eldian history, Paths mechanics, Eren's causal knowledge, Ymir's motives, and the final tree.

## 2. Retrospective transition vocabulary

Use only:

`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`.

Do not rewrite older claims in place merely because the final series supports a new formulation.

## 3. Explanation is not absolution

Every specialist dealing with violence must keep separate:

- cause;
- motive;
- constraint;
- psychological intelligibility;
- tactical necessity;
- strategic necessity;
- political legitimacy;
- ethical justification;
- responsibility;
- exoneration/absolution.

AOT repeatedly permits deep understanding without requiring moral acquittal.

## 4. Recognition is not reconciliation

Humanization or recognition of an enemy does not automatically imply:

- trust;
- forgiveness;
- political agreement;
- de-escalation;
- refusal to use force.

This is a recurring result from Reiner/Eren, Gabi/Kaya, alliance formation, and final-volume conduct.

## 5. Mechanism and symbolism remain separate but compatible

A literal Titan/Paths mechanism can carry symbolic force. Symbolic interpretation cannot establish a literal mechanic the text leaves open.

## 6. Visual claims require visual evidence

A deep reading may alert the synthesis to a visual pattern. If the final specialist claim depends on exact panel composition, gaze, body posture, page turn, spread geometry, or visual rhyme, re-open the relevant Japanese CBZ and verify it.

---

# IX. Specialist completion criteria

A specialist document is not complete merely because it is long.

Before promotion to `canonical`, it should satisfy:

1. one explicit governing question;
2. one mature thesis and at least one serious counterreading;
3. full V01-V34 temporal coverage where relevant;
4. checkpoint/revision routing where earlier claims materially changed;
5. separation of fact, belief, inference, interpretation, and value judgment;
6. evidence references to canonical deep readings and locators;
7. direct Japanese or visual verification for load-bearing language/form claims;
8. no hidden reliance on anime adaptation or external criticism;
9. an anti-duplication statement identifying neighboring specialist homes;
10. a final section stating what remains unresolved.

Character monographs additionally require:

- developmental state separation;
- relationship-conditioned differences;
- negative evidence against caricature;
- ordinary-life evidence where available;
- no conversion of literary analysis into deterministic simulation claims.

---

# X. What should not be done

The post-V34 phase should explicitly avoid the following shortcuts.

## 1. Do not write the giant continuous synthesis first

Doing so would force character, politics, ontology, form, and ethics into one document before their contradictions are reconciled. The continuous synthesis is an integration artifact, not a discovery scratchpad.

## 2. Do not create a "100% checkpoint" that merely appends V28-V34

The final phase is retrospective and should re-adjudicate the entire series. The claim-revision ledger performs the controlled bridge from checkpoint thinking to full-series authority.

## 3. Do not silently mutate V19 or V27 checkpoints

They preserve historically valid knowledge boundaries.

## 4. Do not use final-volume knowledge to rewrite volume-local deep readings

If an early reading needs correction, record the transition in the revision ledger or later synthesis.

## 5. Do not turn every major character into a literary monograph or reconstruction model

Create an artifact when it has a distinct analytical responsibility and sufficient evidence, not to complete a roster.

## 6. Do not make character reconstruction the master interpretive layer

Models are derived tools for conditional behavioral inference. They are not the place to decide the series' political or philosophical meaning.

## 7. Do not treat the final epilogue as proof of a single deterministic philosophy of history

Recurrence, possibility, structural persistence, and deterministic repetition must remain separately argued claims.

## 8. Do not let "Rumbling debate" swallow the rest of the manga

The final violence is central, but AOT's mature analysis also depends on childhood, ordinary life, institutions, relationships, source criticism, bodily inheritance, visual form, and the long development of freedom before the Rumbling becomes possible.

---

# XI. Immediate roadmap from the current corpus state

The sequential phase is already complete and administratively integrated through V34. Therefore the next operations are:

1. **Lock and register this architecture** as the post-V34 synthesis roadmap.
2. **Create `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md`.** This is the immediate next analytical operation.
3. Build `AOT_V01-V34_SYNTHESIS_EVIDENCE_MATRIX.md` and seed the primary-source locator index.
4. Draft `AOT_01_SERIES_ARCHITECTURE_VOLUME_PROGRESSION_AND_MASTER_THESIS.md`.
5. Produce core character monographs in the order defined above.
6. Produce political, military, historical, ontological, philosophical, social, linguistic, visual, and ending specialists.
7. Run the counterreading/contradiction/reference phase and create the synthesis crosswalk.
8. Write `AOT_FULL_SERIES_SYNTHESIS_V01-V34.md` last among literary synthesis artifacts.
9. Produce the prospective-experiment report, full-series reconstruction models where readiness warrants, and validation/cross-model audits.
10. Perform release administration and freeze only after the intended synthesis/reconstruction corpus is complete.

The immediate handoff is therefore unambiguous:

> **NEXT: `AOT_FULL_SERIES_CLAIM_REVISION_LEDGER.md` — route V19 and V27 checkpoint claims through the complete V28-V34 evidence boundary using PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN, assign each surviving claim a primary specialist home, and identify the exact evidence/primary-source verification needed before specialist drafting begins. Recommended reasoning class: `PREMIUM_QUALITY_FIRST`; current provider mapping: `5.6 Sol Pro`.**

---

## v1.2 governance-alignment amendment — 2026-08-27

This amendment closed the post-sequential architecture review required by newer corpus-wide governance. It added the `STABILIZED` architecture lifecycle state, normalized literal GPT-5.6 recommendations to durable reasoning classes while preserving AOT-specific per-document routing, recorded the newer sequential-execution policy as an operational boundary, made amendment/mutable/frozen/retrieval behavior explicit, and confirmed that the anime episode-bundle specification does not apply to the manga-only source topology.

No specialist home, directory number, source boundary, checkpoint/prospective authority state, production dependency, or immediate analytical next step was changed.

---

# XII. Success condition

This architecture succeeds if the finished AOT corpus can answer all of the following without collapsing them into one undifferentiated essay:

- What does the complete narrative become over time?
- What is the strongest evidence-grounded account of Eren, Mikasa, Armin, Reiner, Zeke, Historia/Ymir, and the command/ensemble structures?
- How do states, militaries, racial orders, propaganda systems, and emergency regimes acquire or lose legitimacy?
- What does the manga actually establish about Titan and Paths ontology?
- How do freedom, personhood, attachment, inheritance, recognition, and responsibility change across the series?
- What kinds of ordinary life and future are being protected from instrumentalization?
- Which Japanese-language and manga-form features materially alter interpretation?
- Which ending claims are facts, strong inferences, interpretations, or unresolved possibilities?
- How did the project's own earlier claims change as evidence accumulated?
- Can every load-bearing synthesis claim be routed back to a canonical deep reading and, when necessary, the original Japanese page?
- Can a later character reconstruction state its confidence and limits without pretending synthetic behavior is canon?

The final corpus should make the path from evidence to interpretation visible rather than burying it inside one "definitive" document.

That is the governing post-V34 architecture.
