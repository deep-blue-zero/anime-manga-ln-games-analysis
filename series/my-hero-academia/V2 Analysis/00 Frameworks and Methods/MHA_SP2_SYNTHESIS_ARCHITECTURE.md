---
series: MHA
artifact_type: synthesis_architecture
scope: FULL_SERIES_V01-V42_WITH_BOUNDED_SUPPLEMENTAL_RECONCILIATION
generation: V2
status: canonical
source_boundary: Japanese main manga Volumes 1-42 complete and preserved; bounded UA, UAN and UAG reconciliation governed by section 16; current completion is recorded in the corpus map
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# My Hero Academia V2 — Series Architecture, Roadmap, and Character-Modeling Structure

## 1. Purpose

This document is the governing architecture for the Japanese-primary second-pass reread of 『僕のヒーローアカデミア』. It converts the existing volume-level analytical method into a cumulative series system capable of supporting both literary synthesis and evidence-grounded character reconstruction.

The architecture is designed around two simultaneous goals:

1. produce a definitive volume-by-volume reread and full-series synthesis; and
2. preserve enough longitudinal character evidence to reconstruct plausible speech, judgment, relationships, and behavior in novel situations without confusing simulation with canon.

The architecture does **not** treat character simulation as a replacement for literary analysis. Modeling is a downstream use of the same primary-source evidence.

## 2. Canonical roots

### Analytical root

Current governed Git home: `series/my-hero-academia/V2 Analysis/`, under the repository authority boundary. The original Google Drive `My Hero Academia` analytical-artifact root is provenance; current routing is the V2 corpus map.

### Primary-source root

Google Drive: `My Hero Academia` primary sources.

Current visible subfolders:

- `Main volumes`
- `Supplemental material`

The Japanese main-volume source sequence V01–V42 is complete and byte-locked. The source inventory remains `active_provisional` only for supplemental scope; this does not reopen the main-volume sequence.

## 3. Authority precedence

Within MHA, use the following order:

1. this V2 architecture and the current V2 corpus map;
2. the amended V2 analytical method;
3. canonical V2 sequential volume readings and cumulative ledgers;
4. canonical V2 specialist and full-series syntheses, now complete and routed below;
5. primary Japanese manga for direct verification;
6. V1 analysis only as `historical_legacy` and revision-comparison material.

V1 findings do not remain authoritative merely because they are earlier or more complete. They must survive V2 re-adjudication.

## 4. V2 Drive structure

```text
V2 Analysis/
├── 00 Frameworks and Methods/
│   ├── CURRENT_STATE_AND_CORPUS_MAP.md
│   ├── MHA_SP2_ANALYTICAL_METHOD_V2_1.md
│   ├── MHA_SP2_SYNTHESIS_ARCHITECTURE.md
│   └── MHA_SP2_CHARACTER_MODELING_SCHEMA.md
│
├── 01 Source Lock and Inventory/
│   └── MHA_SP2_SOURCE_INVENTORY.md
│
├── 02 Sequential Readings/
│   ├── MHA_SP2_V01_DEEP_READING.md
│   ├── MHA_SP2_V02_DEEP_READING.md
│   └── ... through V42
│
├── 03 Longitudinal Ledgers/
│   ├── Character Group Ledgers/
│   │   ├── MHA_SP2_CLASS_1A_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_UA_STUDENTS_STAFF_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_PRO_HERO_CHARACTER_STATE_LEDGER.md
│   │   ├── MHA_SP2_VILLAIN_ANTAGONIST_CHARACTER_STATE_LEDGER.md
│   │   └── MHA_SP2_FAMILY_CIVILIAN_SOCIAL_ACTOR_LEDGER.md
│   ├── MHA_SP2_RELATIONSHIP_STATE_LEDGER.md
│   ├── MHA_SP2_POWER_PHILOSOPHY_LEDGER.md
│   ├── MHA_SP2_HERO_SOCIETY_LEDGER.md
│   ├── MHA_SP2_RECOGNITION_FAILED_RESCUE_LEDGER.md
│   ├── MHA_SP2_VILLAIN_FORMATION_LEDGER.md
│   ├── MHA_SP2_JAPANESE_VOCABULARY_LEDGER.md
│   ├── MHA_SP2_VISUAL_MOTIF_LEDGER.md
│   ├── MHA_SP2_CALLBACK_PAYOFF_LEDGER.md
│   └── MHA_SP2_FIRST_PASS_CORRECTION_LEDGER.md
│
├── 04 Character Modeling and Reconstruction/
│   ├── MHA_SP2_CHARACTER_MODEL_READINESS_INDEX.md
│   ├── MHA_SP2_CHARACTER_RECONSTRUCTION_CORPUS_INDEX.md
│   ├── MHA_SP2_AGGREGATE_RECONSTRUCTION_VALIDATION.md
│   └── 30 canonical character reconstruction dossiers
│
├── 05 Specialist Synthesis/
│   └── MHA_SP2_SPECIALIST_SYNTHESIS_INDEX.md, eight comparative specialists and eight individual literary studies
│
├── 06 Full-Series Synthesis/
│   └── MHA_SP2_FULL_SERIES_SYNTHESIS.md and three distinct supporting adjudications
│
├── 07 Evidence and Indexes/
│   └── MHA_SP2_PRIMARY_SOURCE_LOCATOR.md and future crosswalks
│
└── 08 Audits and Manifests/
    └── source locks, corpus audits, manifests, checksums, handoffs
```

No empty categories should be created merely for symmetry. The folders above exist because each already has a planned analytical responsibility.

## 5. Why group-specific character ledgers are necessary

The existing method has a generic character trajectory ledger. That is adequate for thematic synthesis but insufficient for modeling a cast as large as MHA because it encourages only the most salient characters to be updated.

The group ledgers solve three problems:

- **coverage:** minor and secondary characters remain visible even when not central to the current volume;
- **retrieval:** a later model-building pass can retrieve all relevant characters from a social/institutional cohort without searching forty-two volume essays;
- **state continuity:** small behavioral or relational changes can accumulate without needing a standalone monograph.

The ledgers are organized by durable social role rather than moral importance.

### Class 1-A

All Class 1-A students. This is the densest and most frequently recurring cohort and warrants its own ledger.

### Other U.A. students and staff

Class 1-B, Big Three, General Studies, Support Course, teachers, administration, and other U.A.-embedded actors.

### Professional heroes and hero-system actors

Pro heroes, sidekicks, agency personnel, HPSC-linked actors, police when functioning within the hero system, and other adult professional hero infrastructure.

### Villains and antagonists

League of Villains, Meta Liberation Army, organized villain actors, vigilante/criminal antagonists, and other recurring hostile figures. This ledger records behavior without assuming villainy explains the whole person.

### Family, civilians, and other social actors

Parents, siblings, civilians, media figures, doctors, ordinary bystanders, and other non-hero/non-villain actors whose behavior materially shapes characters or the social system.

Characters may migrate in social role over time, but their canonical entry should remain in the ledger that best preserves longitudinal identity. Cross-links should record role changes rather than duplicating the full model.

## 6. Character-state record

Every materially updated character entry should preserve the following fields when evidence exists:

### Identity and role
- current public/social role;
- institutional memberships;
- hero/villain/student status;
- known aliases and naming preferences.

### Psychological state
- dominant desires;
- active fears;
- self-conception;
- shame/pride vulnerabilities;
- unresolved contradictions;
- current sources of confidence and insecurity.

### Values and power philosophy
- what power means to the character;
- what power permits;
- what power obligates;
- moral priorities;
- legitimacy beliefs;
- personhood/autonomy assumptions where textually supported.

### Perception and cognition
- what the character habitually notices;
- blind spots;
- analytical style;
- attribution habits;
- epistemic limits;
- common misreadings of other people.

### Decision behavior
- default decision heuristics;
- risk tolerance;
- action threshold;
- response to uncertainty;
- response to authority;
- response to helplessness;
- response to insult, fear, shame, praise, defeat, and responsibility.

### Social and relational behavior
- baseline sociability;
- hierarchy sensitivity;
- dominance/submission patterns;
- care/help behavior;
- conflict style;
- reconciliation style;
- relationship-specific exceptions.

### Stress and escalation
- low-stakes baseline;
- competitive stress;
- acute danger;
- injury/exhaustion;
- shame/humiliation;
- moral crisis;
- grief/loss;
- group-pressure behavior.

### Japanese voice and speech behavior
- pronouns;
- address terms;
- sentence endings;
- formality;
- contractions/slang;
- recurring phrases;
- insults/praise patterns;
- hesitation and silence;
- emotional register changes;
- relationship-specific speech differences.

### Embodiment and action
- habitual posture/gesture where textually meaningful;
- relationship to injury and bodily cost;
- quirk-specific bodily habits;
- fighting or rescue style;
- noncombat habits relevant to personality.

### Behavioral evidence
For every material modeling claim preserve:
- observed context;
- behavior or wording;
- source locator;
- evidence class;
- whether repeated or one-off;
- current confidence.

### Predictive note
Only after the above, optionally record:
- likely response in analogous situations;
- conditions that would change the prediction;
- confidence level;
- evidence used.

Predictive notes are never canon and must not be fed back into the observational fields as evidence.

## 7. Relationship state ledger

Character models cannot be reconstructed independently of relationships. The relationship ledger records directed pairs or small-group relations where behavior changes significantly by partner.

For each relation track:

- current relational definition;
- trust;
- affection;
- rivalry;
- fear;
- dependency;
- authority;
- resentment;
- idealization;
- protectiveness;
- communication style;
- recurring conflict;
- repair behavior;
- speech/register differences;
- major state transitions;
- asymmetries in how each person understands the relationship.

Examples from Volume 1 already requiring longitudinal tracking include:

- Midoriya → Bakugo;
- Bakugo → Midoriya;
- Midoriya ↔ All Might;
- Midoriya ↔ Uraraka;
- Midoriya ↔ Iida;
- Midoriya ↔ Inko;
- Midoriya ↔ Aizawa.

## 8. Model-readiness states

A character's reconstruction readiness must be explicit.

### `insufficient`
Too little direct evidence or too narrow a context range.

### `emerging`
Several consistent traits are visible, but behavior remains underdetermined outside observed contexts.

### `moderate`
Repeated evidence exists across multiple contexts and relationships; cautious novel-situation reconstruction is possible.

### `strong`
Extensive longitudinal behavior, speech, stress, and relationship evidence supports high-confidence reconstruction across ordinary and high-stakes contexts.

### `specialist_ready`
Strong model plus sufficiently rich language/relationship evidence for a standalone character dossier and formal scenario-validation tests.

Readiness is evidence coverage, not character importance.

## 9. Volume workflow amendment

After every future volume reading:

1. write the canonical volume deep reading;
2. update every group ledger for characters whose state materially changed;
3. add newly observed behavioral evidence even if the character did not undergo thematic development;
4. update relationship states;
5. update model-readiness ratings only when evidence breadth materially changes;
6. update thematic ledgers;
7. update source locators;
8. record first-pass claim transitions;
9. update `CURRENT_STATE_AND_CORPUS_MAP.md` only when project state materially changes.

A character appearing without new usable evidence does not require a synthetic update.

## 10. Phased roadmap

### Phase 0 — Framework and source lock
- establish V2 architecture;
- amend analytical method;
- establish modeling schema;
- create source inventory;
- initialize ledgers;
- seed Volume 1 evidence.

### Phase 1 — Sequential reread, Volumes 1–42
- one Japanese volume per pass;
- canonical deep-reading artifact per volume;
- cumulative character/model and thematic ledgers updated continuously.

### Phase 2 — Mid-series modeling checkpoints
At major structural boundaries, audit whether character models have enough context diversity. Suggested checkpoints:
- post-Sports Festival;
- post-Kamino;
- post-Overhaul;
- post-My Villain Academia;
- post-Paranormal Liberation War;
- post-Dark Deku;
- post-Final War / Volume 42.

These checkpoints should identify what kinds of situations remain missing for each important character rather than merely summarizing them.

### Phase 3 — Character reconstruction dossiers
After enough evidence accumulates, produce specialist dossiers for characters that reach `specialist_ready`. The user-authorized completion scope also includes every `strong` character. This extension yields 30 dossiers (13 specialist_ready, 17 strong) without changing the five readiness definitions or treating dossier existence as promotion.

The original anticipated candidates included Midoriya, Bakugo, All Might, Todoroki, Endeavor, Shigaraki/Tenko, AFO, Ochako, Toga, Iida, Aizawa, Hawks, Twice, Spinner, Dabi, and others as evidence warrants.

### Phase 4 — Validation probes
Test reconstruction quality using held-out canonical scenes or deliberately withheld later-volume material:

- predict likely behavior from the model using only evidence available before the held-out scene;
- compare prediction to canonical behavior;
- classify mismatch as missing state, wrong inference, context sensitivity, or genuine surprise;
- revise the model rather than rationalizing the miss.

This is the preferred method for testing simulation rigor. The completed thirty-probe corpus uses retrospective chronological evidence holdouts: the analyst knew later manga, frozen inputs are selected earlier evidence, and supplied later initial conditions are not predictions. The aggregate report retains partials, misses and the contaminated original Hawks exercise; it does not report blind accuracy. The five V41→V42 checkpoint comparisons remain directional comparisons/open-question resolutions.

### Phase 5 — Specialist synthesis
Draft subject-specific documents from the mature ledgers and sequential readings.

### Phase 6 — Full-series synthesis
After Volume 42, produce the definitive multi-document synthesis with direct primary-source re-verification of load-bearing claims.

## 11. Separation of responsibilities

### Sequential volume readings answer
What does this volume do, and what evidence does it add?

### Group character ledgers answer
What do we currently know about each character as a changing person?

### Relationship ledger answers
How does behavior change by social partner and relational state?

### Thematic ledgers answer
How do recurring philosophical, social, visual, and linguistic structures evolve?

### Modeling dossiers answer
Given the accumulated evidence, what behavior/speech can be reconstructed, with what confidence and limits?

### Specialist syntheses answer
What is the strongest mature interpretation of a subject across the complete corpus?

### Individual literary studies answer
How does one person's whole trajectory develop its governing literary question across changing relationships, social roles, embodiment, narrative disclosure and ordinary ends? These studies synthesize evidence across comparative responsibilities without becoming operational reconstruction models or changing the fourteen-ledger partition.

These responsibilities should not be collapsed into near-duplicate documents.

## 12. Governing rule for simulation

The project should model **conditional behavioral tendencies**, not deterministic personalities.

A valid reconstruction states:

> Given this character state, relationship, knowledge, stakes, and social context, the best-supported response is X, with Y plausible alternatives and Z confidence.

An invalid reconstruction states:

> This character is the kind of person who always does X.

MHA repeatedly depicts growth, role conflict, hidden information, situational stress, and relationship-specific exceptions. A rigorous model must preserve that conditionality.

## 13. End-state deliverable

At the completion of Volume 42, the MHA V2 corpus should be able to support both:

- a source-grounded definitive literary/thematic synthesis; and
- evidence-auditable character reconstruction in novel scenarios.

The two outputs should share evidence infrastructure but remain epistemically distinct.


## 14. Completed corpus and current routing

The authorized V01–V42 main-manga analytical program is complete. V41/V42 readings and the final checkpoint are canonical. No next sequential main volume or unfinished specialist/full-series document remains. Publication/integration receipts are separate from this analytical completion statement.

- [Current-state and corpus map](CURRENT_STATE_AND_CORPUS_MAP.md) — canonical current routing and historical-boundary controls.
- [Reconstruction corpus](../04%20Character%20Modeling%20and%20Reconstruction/MHA_SP2_CHARACTER_RECONSTRUCTION_CORPUS_INDEX.md) and [aggregate validation](../04%20Character%20Modeling%20and%20Reconstruction/MHA_SP2_AGGREGATE_RECONSTRUCTION_VALIDATION.md) — thirty dossiers and all formal comparisons; the readiness index alone owns tiers.
- [Specialist disposition and corpus](../05%20Specialist%20Synthesis/MHA_SP2_SPECIALIST_SYNTHESIS_INDEX.md) — all fourteen maintained ledgers assigned before drafting to eight material specialist responsibilities.
- [Definitive full-series entrypoint](../06%20Full-Series%20Synthesis/MHA_SP2_FULL_SERIES_SYNTHESIS.md) — integrated argument and three supporting documents with distinct paired, social-future and form/revision/residual responsibilities.
- [Publication/source audit](../08%20Audits%20and%20Manifests/MHA_SP2_PUBLICATION_AND_SOURCE_REVERIFICATION_AUDIT.md) — source hashes, mapping, inspected ranges, correction propagation and frozen publication equivalence.

At the completed manga-only boundary, supplemental inventory remained provisional and excluded; the later named-book continuation is governed by section 16. Unshown futures, exact medical endpoints, vestige metaphysics, complete equipment limits and reform durability are residuals defined in the full-series corpus, not missing main-volume readings. Future reconstruction must retain dated state, relationships, knowledge and uncertainty rather than import final outcomes into an earlier freeze.


## 15. Post-completion maturation and literary-character ownership

The completed V01–V42 baseline remains complete. The subsequent maturity review identified underdeveloped longitudinal arguments and eight distinct individual literary questions; the user authorized their implementation. This is maturation inside the existing V2 generation, not a new sequential reread or supplemental expansion. **MATURATION_STATE = COMPLETE** for the local analytical work. The implementation record verifies the finished arguments, routes, evidence and preservation requirements, while recording publication separately.

The eight comparative specialists retain their identities and the primary fourteen-ledger partition in the specialist index. Seven received substantive expansion; S8's fifteen claim adjudications and existing V1 qualifications are preserved. The following individual homes belong beside them in `05 Specialist Synthesis/`. They reuse the readings and ledgers but own complete character interpretations, not another set of comparative specialists or reconstruction dossiers.

| Literary home / current artifact | Primary governing question | Comparative owners and full-series dependency |
|---|---|---|
| L1 — [MHA_SP2_MIDORIYA_IZUKU_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_MIDORIYA_IZUKU_CHARACTER_MONOGRAPH.md) | How can a person formed through rescue and entrusted power author his methods and ends while including himself among those who may receive care? | S1/S2/S3 retain comparative development, rescue and inheritance; F1/F2/F3 consume the individual argument. |
| L2 — [MHA_SP2_BAKUGO_KATSUKI_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_BAKUGO_KATSUKI_CHARACTER_MONOGRAPH.md) | How do admiration and proof of worth develop from domination into accountable cooperation and enabling care without erasing earlier harm or persistent voice? | S1 retains directed rivalry; F1/F3 consume the trajectory across peers, mentors, public performance and injury. |
| L3 — [MHA_SP2_SHIGARAKI_TOMURA_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_SHIGARAKI_TOMURA_CHARACTER_MONOGRAPH.md) | How does the work construct destructive leadership and situated agency while progressively revealing engineered history, possession and contested identity? | S3/S5 retain power and comparative formation; F2/F4 consume the distinction between explanation, chosen harm and limited terminal recognition. |
| L4 — [MHA_SP2_ALL_MIGHT_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_ALL_MIGHT_CHARACTER_MONOGRAPH.md) | How does a real public ideal become a teachable, dependent person and continuing mentor without becoming either an obsolete function or an innocent abstraction? | S3/S4 retain inheritance and institutions; F2/F3 consume the changing relation among purpose, pedagogy, risk and ordinary presence. |
| L5 — [MHA_SP2_ENDEAVOR_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_ENDEAVOR_CHARACTER_MONOGRAPH.md) | How do expertise, public legitimacy, parental ownership, guilt and responsive responsibility change at different rates? | S4/S6 retain institutional and family comparison; F2/F3 consume the refusal of moral offsetting between roles. |
| L6 — [MHA_SP2_TODOROKI_SHOTO_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_TODOROKI_SHOTO_CHARACTER_MONOGRAPH.md) | How does negative self-definition become selective inheritance, social learning and positive ordinary ends without requiring filial absolution? | S1/S3/S6 retain comparative implications; F2/F3 consume the trajectory beyond the father's project. |
| L7 — [MHA_SP2_URARAKA_OCHAKO_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_URARAKA_OCHAKO_CHARACTER_MONOGRAPH.md) | How do material care, independent ambition, attention to rescuers, desire and survivor responsibility become a chosen life? | S1/S2/S6 retain comparative care; F2/F3 consume independent history beyond either romantic support or a terminal pair. |
| L8 — [MHA_SP2_HIMIKO_TOGA_CHARACTER_MONOGRAPH.md](../05%20Specialist%20Synthesis/MHA_SP2_HIMIKO_TOGA_CHARACTER_MONOGRAPH.md) | How do imposed normality, authored desire, violence and particular belonging change across several interlocutors into a chosen gift without general absolution? | S5 retains comparative formation and F2 intervention/gift adjudication; F2/F4 consume the whole trajectory and its final limits. |

An individual home must develop its governing question across early, middle and late evidence, distinguish narrated history from the order of disclosure, and adjudicate a serious rival reading. Its scope is not earned by a file count, readiness tier or protagonist status. If a full argument can be owned by a navigable existing primary section without displacing that owner's comparative purpose, the separate file becomes redundant and should not be expanded merely to defend its existence.

Toya's failed capture, family-produced worth and staged revenge remain in S5/S6; AFO's pedagogy, selective strategic understanding and ownership claims remain in S3/S5/F2. These are nonduplication decisions, not claims of thin characterization. No parallel Todoroki-family, rival-dyad, ensemble, adversarial or residual file is established. S7 retains a joint language/form responsibility because speaker, visual mediation and sequence jointly change the same arguments. F2/F3/F4 retain counterreadings and R01–R13.

Literary interpretation is not a behavioral freeze. The four targeted model changes add discriminative support for Midoriya, Bakugo, All Might and Aizawa without rewriting existing atoms, formal probes, frozen inputs, contamination notices or readiness. The other twenty-six dossiers and S8 remain unchanged. A useful new example need not become a new probe: V19 All Might applies learner-led teaching already explicit in V12, and Bakugo has earlier noncombat cooperation. No validation quota follows from greater literary depth.

The [maturation implementation record](../08%20Audits%20and%20Manifests/MHA_SP2_MATURATION_IMPLEMENTATION_RECORD.md) owns completion evidence for this bounded change. The specialist index routes completed individual homes; the corpus map distinguishes the completed baseline from this additional implementation. Evidence status, primary locators, source exclusions and the literary/reconstruction separation remain governed by the existing method and schema.


## 16. Bounded official-supplement reconciliation — 2026-09-10

This is continuation of the existing mature V2 analytical root, not a material restart or a new generation. The existing method, longitudinal corpus and synthesis roles remain adequate; the missing responsibilities are independent supplemental source accounting and cross-source claim adjudication. Section 18 of the [method](MHA_SP2_ANALYTICAL_METHOD_V2_1.md#18-official-supplemental-material-reconciliation-amendment--2026-09-10) supplies the reading contract. The [current map](CURRENT_STATE_AND_CORPUS_MAP.md#current-supplemental-reconciliation) controls actual progress rather than the historical queues below it.

| Responsibility | Canonical home | Required result and dependency |
|---|---|---|
| Exact source objects, edition distinctions and image retrieval | `01 Source Lock and Inventory/MHA_SP2_OFFICIAL_SUPPLEMENTAL_SOURCE_LOCK.md` and `MHA_SP2_SUPPLEMENTAL_SPINE_MAP.tsv` | All three original EPUBs locked; deterministic original spine/member/hash mapping; repaired EPUBs identified as reading derivatives, not additional witnesses. |
| Complete independent book review | `01A Supplemental Source Audits/MHA_SP2_ULTRA_ARCHIVE_PARATEXT_AUDIT.md`, `MHA_SP2_ULTRA_ANALYSIS_PARATEXT_AUDIT.md`, `MHA_SP2_ULTRA_AGE_PARATEXT_AUDIT.md` | One argument-bearing audit per book, with its own topology, attribution, time, evidence, contradictions and coverage file named `MHA_SP2_<CODE>_PAGE_COVERAGE.csv`. These are separate source responsibilities, not literary monographs. |
| Selective cross-book evidence and claim revision | `07 Evidence and Indexes/MHA_SP2_SUPPLEMENTAL_EVIDENCE_RECONCILIATION_LEDGER.md` | Stable records connect exact source locators to manga/book comparators, authority/dependence, time, effect and canonical destinations. No quota or transcription of every profile fact. |
| Every subject's current applicability | Existing readiness index; reconciliation impact audit and its character review matrix | Preserve the baseline 86 current rows and identify historical distributed candidates, aliases and true new discoveries. Record unchanged as well as changed outcomes; no automatic tier increase or dossier creation. |
| Current conditional reconstruction | Existing 30 dossiers and corpus index | Targeted, source-labeled additions/revisions after full-file review; preserve historical model and validation blocks. The existing schema owns tier gates. |
| Comparative, individual and full-series interpretation | Existing eight specialists, eight literary monographs and F1–F4 | Evidence-driven revision after source stabilization. Separate added characterization from manga execution; preserve or explicitly re-adjudicate counterreadings. |
| Completion, validation limits and preservation | `08 Audits and Manifests/MHA_SP2_SUPPLEMENTAL_RECONCILIATION_IMPACT_AUDIT.md` | Report real coverage and dependent/unique evidence, all character/home dispositions, changed and unchanged conclusions, exact historical preservation and remaining uncertainties. Publication is separately verified. |

The `01A` location is justified because three image-based reference books each need independent page-complete source audits alongside the existing source-lock and sequential-reading areas. It does not alter the 42 volume readings or create another analytical root. The COTE guidebook audit is a methodological precedent for source-specific treatment, not a folder/schema template or permission to substitute an inherited audit for fresh MHA page inspection.

**Dependency and transaction order:** admit and lock sources/method → review UA and close its coverage/audit/ledger checkpoint → review UAN and close its checkpoint → review UAG and close its checkpoint → reconcile cross-book claims → review all characters and update current models/readiness → converge specialists/monographs → integrate F1–F4 → validate and close the pass. Disjoint page ranges inside the active book may be reviewed by parallel agents, with one integrated coverage record; no later book is substantively opened before the preceding book's checkpoint is verified and committed. Publication can wait until a coherent reviewed state. A bootstrap commit certifies infrastructure only, never completed evidence review.

Source auditing inherits `SUBSTANTIVE_ANALYSIS`; cross-source adjudication, reconstruction and literary integration inherit `DEEP_SYNTHESIS`. Mechanical identity/coverage checks are `BOUNDED_STANDARD` or `ROUTINE_FAST`. These are workload classes under the corpus policy, not claims about provider pricing or evidence authority; the current execution uses the user's selected agent configuration without silently changing historical model recommendations.

The new ledger and current impact audit are mutable during this pass. Closed book checkpoints are preserved through Git history; later cross-book findings append a dated adjudication instead of pretending it was known at the earlier checkpoint. All original volume readings, historical freezes, source locks, checkpoints, formal probes and first-pass history remain protected. The fourteen manga-derived longitudinal ledgers remain preserved; new supplemental evidence has its own cumulative ledger so its origin is not lost.

No new specialist or character monograph is predetermined. A new home would need a material independent responsibility that existing owners cannot carry. The final current entrypoint must name the exact completed boundary **V01–V42 + UA + UAN + UAG**, distinguish it from the complete manga-only historical boundary, and retain the separate unresolved question of volume-embedded paratext. No automatic main-branch integration is authorized by this architecture.
