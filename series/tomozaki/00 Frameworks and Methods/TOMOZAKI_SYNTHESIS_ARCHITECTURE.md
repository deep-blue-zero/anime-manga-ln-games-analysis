---
series: TOMOZAKI
artifact_type: synthesis_corpus_architecture
scope: JP_LIGHT_NOVEL_V01-V11_PLUS_ROUTED_V06_5_AND_V08_5
source_boundary: "Audited Japanese light-novel EPUB corpus: numbered main Volumes 01-11 plus side-story Volumes 06.5 and 08.5; source audit dated 2026-08-29"
analytical_generation: V2_REMEDIATION
architecture_version: "1.1"
architecture_lifecycle: EVOLVING
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
canonical_entrypoint: "../CURRENT_STATE_AND_CORPUS_MAP.md"
governing_method: "TOMOZAKI_ANALYTICAL_METHOD.md"
historical_initialization_state: ARCHITECTURE_GATE_VIOLATED_BEFORE_V01
sequential_completion_gate: PASS_AT_V11_BOUNDARY
longitudinal_reconciliation_gate: OPEN_BACKFILL_IN_PROGRESS
specialist_synthesis_gate: CLOSED
full_series_synthesis_gate: CLOSED
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
resolved_reasoning_option: "Codex gpt-6-astra with max reasoning for the owner-directed remediation operation"
reasoning_policy: "../../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md"
reasoning_policy_version: "1.0"
model_guidance_verified_date: "2026-09-13"
---

# Bottom-Tier Character Tomozaki — synthesis and corpus architecture

## 1. Governing responsibility

This document is the canonical synthesis architecture for the Japanese-light-novel analysis of *Bottom-Tier Character Tomozaki* (`弱キャラ友崎くん`). It governs what the source-facing readings accumulate into, which artifact owns each recurrent responsibility, how claims remain traceable and revisable, what dependencies must converge before whole-series integration, and when the corpus may truthfully call a phase complete.

Its responsibility is distinct from the companion analytical method:

- `TOMOZAKI_ANALYTICAL_METHOD.md` governs how a source is read, how evidence is classified, and how a bounded interpretation is judged.
- this architecture governs where accumulated knowledge goes, which artifacts may become mature authority, and in what order those artifacts are built and validated;
- `../CURRENT_STATE_AND_CORPUS_MAP.md` is the mutable entrypoint and current-state router. It does not substitute for either the method or this architecture.

The current architecture lifecycle is `EVOLVING`. Sequential reading has already reached the V11 boundary, but the cumulative and specialist layers are undergoing owner-directed remediation. `EVOLVING` is not a downgrade of the completed readings. It is the truthful state of a newly established architecture whose required downstream responsibilities are not yet reconciled.

### 1.1 Authority and governing policy

This architecture is canonical within `series/tomozaki/` and is subordinate to live repository governance, especially:

- `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`;
- `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`;
- `governance/policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`;
- `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`;
- `governance/policies/BRANCH_LIFECYCLE.md`;
- the live authority state and scope files.

Higher-level policy controls if a conflict arises. The primary Japanese witnesses remain evidence authority; no architectural declaration can make a downstream interpretation override the novels.

### 1.2 Historical architecture debt

Tomozaki began substantive sequential reading without a synthesis architecture satisfying the repository's Minimum Semantic Contract. The initial project had a strong method, source lock, folder scaffold, and current-state router, but it did not establish the required cumulative responsibilities, specialist domains, evidence route, revision protocol, dependency graph, completion gates, reasoning classes, or responsibility matrix. The first narrow longitudinal ledger was added only after V02.

The former self-reference in the corpus map that named the map itself as `synthesis_architecture` did not cure that absence: the map also correctly described itself as only a router. The later V11 validation audit verified impressive source coverage, but it did not audit all architecture-contract responsibilities and therefore could not validly close them.

This file repairs that governance debt prospectively and retrospectively without pretending it existed at project birth. It does not rewrite history, recast the volume readings as defective, or manufacture cumulative observations that were never recorded.

### 1.3 Preservation rule

All V01–V11 deep readings and the V06.5/V08.5 supplemental readings remain canonical historical source-facing states. Their pre-volume registers, predictions, falsifiers, claim adjudications, abstentions, and post-volume freezes must remain unchanged during this remediation. Later synthesis may revise the current interpretation of an earlier claim, but it may not alter what was known or predicted at the earlier boundary.

The existing effort/competition/goal-ownership ledger is retained as a canonical longitudinal evidence spine. Its narrowness is a strength, not a defect. New ledgers must complement rather than paraphrase or replace it.

## 2. Source topology and continuity

### 2.1 Admitted primary corpus

The current literary continuity is the audited Japanese EPUB set recorded in `../01 Source Lock and Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`:

- main numbered Volumes 01–11, in publication order;
- Volume 06.5 as a publication-order supplement after V06 with story-local diegetic placement;
- Volume 08.5 as a publication-order supplement after V08 with mixed internal chronology;
- the acquired V07 Special Edition witness, whose main novel is literary evidence and whose `FLY mini ART WORKS` block is edition-specific visual paratext;
- explicitly routed bonus or appended material only at the authority and chronology assigned by the source lock and its deep reading.

The default numbered developmental chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

V06.5 and V08.5 do not become simple steps in that chain. Each observation from them carries its own story-local time, narrator/observer access, and continuity classification. Parallel, adapted, promotional, and non-narrative material remains segregated where the corresponding reading says it is segregated.

### 2.2 Excluded or separately admissible sources

The present architecture does not admit:

- V12 or later prose;
- anime or manga adaptations;
- official or fan translations as semantic authority;
- interviews, promotional copy, reception, wikis, or fandom consensus;
- retailer bonuses not present and routed in the audited witnesses;
- remembered canon or model knowledge.

A later source enters only through a source-lock amendment. Adaptations or translations require a declared comparative responsibility and cannot silently alter the light-novel continuity.

### 2.3 Source-layer conflicts

An apparent conflict must first be classified rather than harmonized. Available classes are:

- `DEVELOPMENTAL_CHANGE` — the character or relationship changed;
- `FOCALIZATION_LIMIT` — an observer's model differs from another perspective or later access;
- `SELF_THEORY_GAP` — what a character says about themself differs from demonstrated conduct;
- `KNOWLEDGE_STATE_DIFFERENCE` — reader and actor, or two actors, possess different information;
- `STRATEGIC_OR_AFFECTIVE_SPEECH` — deception, concealment, embarrassment, persuasion, anger, or role performance changes the statement's force;
- `RETROSPECTIVE_REFRAMING` — later memory or explanation changes interpretation without rewriting the earlier event;
- `SUPPLEMENT_PLACEMENT` — a side story supplies evidence from a different diegetic point;
- `SOURCE_LAYER_DIVERGENCE` — edition, adaptation, translation, paratext, or other witness differs;
- `GENUINE_TEXTUAL_TENSION` — the admitted source does not currently permit reconciliation;
- `UNRESOLVED` — the available evidence cannot yet choose among classes.

Material conflicts require a claim-state entry or an explicit `OPEN` result. Mature synthesis may not erase them with a totalizing motive theory.

## 3. Authority ladder and artifact roles

For literary claims, use this precedence unless a narrower policy controls:

1. admitted Japanese primary source, bounded by the source lock;
2. source lock and canonical source-facing deep reading for the relevant volume/state;
3. reconciled cumulative ledger or claim/evidence index;
4. validated literary character, relationship, or specialist synthesis;
5. validated full-series synthesis for cross-domain integration;
6. provisional or pre-remediation monograph/synthesis candidates;
7. future derived-use reconstruction models;
8. conversation history, summaries, memory, or informal notes.

Higher placement does not make an inference direct evidence. A deep reading preserves the source-facing state; a later ledger can become current authority for the claim's cross-volume revision history without becoming a replacement for the source passage.

The current seven character monographs and current full-series synthesis are valuable first-pass candidates. Until their architecture-defined inputs converge and they pass role-specific review, they do not carry mature literary authority merely because their front matter or filenames once called them canonical.

## 4. Sequential-reading contract

### 4.1 Preserved completed sequence

The V01–V11 numbered readings and V06.5/V08.5 supplemental readings satisfy the source-facing component of the sequential gate. They collectively preserve:

- exact witness identity and package observations;
- a pre-source claim/question/prediction horizon;
- incremental narrative and image-layer evidence;
- state vectors and relationship developments;
- Japanese wording or wording-sensitive observations where captured;
- competing readings, counterevidence, falsifiers, and abstentions;
- explicit adjudication of inherited claims;
- a bounded post-source freeze.

Their prose is not to be regenerated for architectural conformity. Retrospective backfill cites them as evidence and leaves their prospective horizons intact.

### 4.2 Architectural outputs for a future source unit

If a later numbered or supplemental source is admitted, a completed source-unit operation must produce or explicitly adjudicate all applicable outputs:

1. source-lock and inventory advancement;
2. a pre-source freeze copied from the preceding numbered boundary before prose access;
3. the canonical deep or supplemental reading;
4. claim dispositions using `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`;
5. evidence locators sufficient for any new load-bearing claim;
6. updates to every affected mandatory cumulative ledger;
7. readiness and promotion decisions for characters, relationships, or specialist domains;
8. corpus-map and architecture-review updates where state changed.

A standalone deep-reading document is source-facing complete when frozen, but the source-unit tranche is not architecturally complete until applicable cumulative state advances or the operation records a reasoned `NO CHANGE`.

## 5. State model: preventing terminal flattening

Every cumulative and mature synthesis claim must be representable as a state tuple:

`〈source position, diegetic position, continuity layer, observer/focalizer, actor knowledge, reader knowledge, evidence class, revision state〉`

At minimum, documents must distinguish:

- true or supportable at VNN from the current V11 interpretation;
- stable tendency from developmental state, situational role, recipient-conditioned behavior, crisis behavior, and deliberate performance;
- competence, confidence, status, self-concept, agency, and value ownership;
- a character's stated belief from inferred motive and from demonstrated result;
- another person's interpretation of a character from direct access to that character's interiority;
- present action from later causal or autobiographical explanation;
- pre-reveal from post-reveal reader knowledge;
- mainline progression from a supplement's story-local retrospective evidence;
- living action from posthumous testimony or another person's use of a deceased character's history;
- explanation of formation from authority to define meaning or prescribe remedy.

Terminal V11 state is a boundary state, not the character's timeless essence and not the series ending.

## 6. Longitudinal infrastructure

### 6.1 Current mandatory cumulative homes

The completed readings demonstrate independent retrieval burdens for the following layers.

| Cumulative responsibility | Canonical artifact | Current state | Why it is independent |
|---|---|---|---|
| Effort, competition, rank, goal origin/ownership, stopping rules, comparative self-worth, capacity governance | `../03 Longitudinal Ledgers/TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md` | current through V11 | Already mature and deliberately narrow; its claim history should not be diluted into general character summary. |
| Developmental character state | `../03 Longitudinal Ledgers/TOMOZAKI_CHARACTER_STATE_LEDGER.md` | canonical mutable backfill through V11 | At least seven evidence-rich figures change across many volumes and contexts; terminal monographs cannot preserve all earlier state transitions. |
| Directional relationship and network state | `../03 Longitudinal Ledgers/TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md` | canonical mutable backfill through V11 | Trust, disclosure, leverage, consent, repair, third-party effects, and option structures have dyadic histories not owned by either individual. |
| Major-claim revision and evidence routing | `../03 Longitudinal Ledgers/TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md` | canonical mutable L1 crosswalk through V11; twelve L2/L3 queues open | The 319 claim IDs and 140 question IDs now have an auditable promoted/local partition, while load-bearing lineages have current dispositions and deterministic reading routes. |
| Social atmosphere, group systems, status enforcement, punishment, and repair | `../03 Longitudinal Ledgers/TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md` | canonical mutable backfill through V11 | `空気`, conformity, reputation, informal sanctions, facilitation, and group option structures recur independently across school, election, bullying, festival, and later peer intervention. |
| Japanese voice, register, address, and load-bearing conceptual terms | `../03 Longitudinal Ledgers/TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md` | required but source-escalation-dependent | The readings preserve many key lexemes, but mature character-specific register and translation-sensitive claims need selective return to exact Japanese passages rather than invention from summaries. |

Character state, relationship state, claim/evidence lineage at L1, and social/group-system state form the first completed remediation backfill. The existing readings preserved enough evidence to establish those layers without reopening the EPUBs. Japanese voice/register and the twelve high-risk L2/L3 locator queues remain the targeted source-escalation boundary.

### 6.2 Responsibilities that remain local or distributed

Not every recurring observation earns a new ledger.

- Package structure, image segregation, and witness identity remain in the source lock and individual readings unless a later comparative-source project creates a new need.
- Prospective predictions and falsifiers remain in the frozen readings; the claim index crosswalks material revisions but does not duplicate every historical paragraph.
- Ordinary-life preferences and habits are captured in character-state rows and later monographs. A separate ordinary-life ledger is deferred unless reconstruction work reveals repeated retrieval failure.
- Professional viability, effort, rank, and future planning remain in the existing effort/goal ledger unless a distinct institutional/work responsibility emerges.
- Ethical judgments about disclosure and intervention route through relationship state, the claim index, and a later specialist synthesis rather than a free-standing ethics ledger at this stage.

### 6.3 Ledger standards

A mature ledger must:

- state one bounded responsibility;
- keep volume or story-local chronology visible;
- distinguish direct evidence, corroborated inference, hypothesis, value judgment, and open state;
- route material entries to source-facing readings and, where necessary, exact primary locators;
- preserve contradiction and counterevidence;
- identify affected downstream artifacts;
- use explicit revision dispositions;
- record `NO CHANGE` only when that result itself matters;
- avoid turning a matrix into decontextualized personality scores.

## 7. Literary character responsibility

### 7.1 Promotion threshold

A character earns an independent literary monograph when the admitted corpus supports several of the following and the responsibility cannot be carried reliably by an ensemble or specialist document:

- meaningful state across multiple source units or developmental bands;
- behavior under more than one role, stress level, or recipient relationship;
- a consequential gap between self-description and demonstrated behavior;
- motive, value, or goal revision;
- contradictions or rival readings requiring independent adjudication;
- distinctive voice/register or ordinary-life evidence with interpretive force;
- independent effect on multiple relationships or specialist problems;
- enough traceable evidence to state limits and counterevidence rather than extrapolate.

Prominence alone is insufficient. Conversely, socially ordinary expression or limited focalization is not evidence of analytical thinness.

### 7.2 Required mature monographs

The current evidence makes mature independent studies mandatory for:

- Tomozaki Fumiya;
- Hinami Aoi;
- Kikuchi Fuka;
- Nanami Minami / Mimimi.

The existing Tomozaki and Hinami files are severe backfill priorities because they carry the series' central competing methods and the largest propagation risk. Kikuchi and Mimimi are also material backfills, not romance-subplot summaries.

Tama, Mizusawa, and Yuzu have earned independent current files, but the role-gap audit must determine whether each becomes a full mature monograph or a clearly bounded character dossier. Reclassification is not demotion: it is an honest statement of evidence breadth and document responsibility.

Nakamura, Konno, Haruka, Rena, and other supporting figures remain evidence-sufficiency decisions. They may earn bounded dossiers, ensemble treatment, or sections in relationship/social-system specialists. No file is mandatory merely because the character is close to the protagonist.

### 7.3 Monograph semantic contract

A mature major-character study should include, where evidence supports it:

- governing literary function and a falsifiable central account;
- chronological developmental bands rather than terminal traits;
- stable tendencies versus state, role, performance, and recipient effects;
- evidence hierarchy appropriate to narrator access;
- self-theory versus demonstrated behavior;
- motive and goal hierarchy, including ownership and stopping conditions;
- attentional biases, competence, blind spots, and decision habits;
- confidence/status/self-concept/agency/value distinctions;
- strengths that also generate failures;
- stress, defeat, repair, and failure behavior;
- relationship-conditioned variation;
- ordinary-life evidence where relevant;
- Japanese voice/register and wording only where traceable;
- rival readings, counterevidence, and explicit dispositions;
- ethical and agency questions when justified;
- a V11 current-boundary state with unresolved questions and abstentions;
- claim and locator routing;
- handoff constraints for relationships and final synthesis.

Length is not a gate. Responsibility coverage, developmental precision, adversarial survival, and evidence retrieval are.

## 8. Relationship and ensemble responsibility

Relationships have state that neither participant's monograph can own alone. The ledger records that state; dedicated relationship syntheses explain emergent logic.

The following relationship specialists are mandatory before full-series integration:

- Tomozaki ↔ Hinami: coaching, mutual proof, rivalry, disclosure, knowledge claims, consent, intervention, defeat, and competing theories of life;
- Tomozaki ↔ Kikuchi: observation, authorship, selection, allocation, disclosure, jealousy, touch, privacy, repair, and relationship governance;
- Tomozaki ↔ Mimimi: recognition, care, confession, refusal, routine loss, continuing support, stopping rules, and third-party ethical limits.

The role-gap audit and relationship ledger must test independent specialists or ensemble ownership for:

- Hinami ↔ Tama;
- Hinami ↔ Mizusawa;
- Mimimi ↔ Tama;
- Tomozaki ↔ Mizusawa;
- Tomozaki ↔ Rena;
- the core peer group as a distributed care/intervention system;
- class atmosphere and punishment networks.

A relationship earns a specialist when changes in one direction alter the other person's option structure, when third parties materially change the dyad, or when its longitudinal problem cannot be reconstructed from the two character files without repeated cross-volume work.

A mature relationship synthesis must distinguish A→B from B→A and track desired relation, standing, knowledge, disclosure, trust, leverage, care, dependency, ordinary presence, boundaries/refusal, conflict/repair, third-party effects, consent, and authority. Narrative centrality does not prove romance or reciprocity.

## 9. Specialist-synthesis program

### 9.1 Mandatory literary specialists

The completed source boundary makes the following problem domains mandatory inputs to final integration. Their eventual filenames and grouping may change if the responsibility remains explicit.

1. **Game models, learned form, authenticity, and self-authorship.** What technique can teach; when practiced form becomes owned competence; what optimization sees and misses; how desire and refusal enter the model.
2. **Effort, mastery, rank, goal ownership, and future viability.** The existing ledger is the evidence spine; the specialist explains the series' competing effort regimes without equating exertion, victory, value, and ownership.
3. **Social atmosphere, group systems, reputation, punishment, and repair.** How `空気` becomes causal; how groups distribute risk and sanctions; how facilitation, status, and ordinary presence change possible action.
4. **Control, causality, result, reason, and retrospective meaning.** Hinami's calculability and proof system; Nagisa's causally unresolved death; the family meaning framework; the limit from formation explanation to total essence or remedy.
5. **Romance, care, disclosure, boundaries, and the ethics of intervention.** Relationship governance, privacy, standing, cost, consent, and the distinction between understanding a mechanism and owning a person's end.
6. **Authorship, fiction, observation, and personhood.** Kikuchi's worlds and people, self-inclusion, observational exposure, fictionalization, possible publication, and the ethics of using another person's pain.
7. **Japanese conceptual language, voice, and register.** Load-bearing terms such as game/rank/result/reason/meaning/strength, character-specific ways of owning propositions, address shifts, and the interpretive cost of translation.

These are Tomozaki-specific responsibilities, not imported Oregairu titles. Consolidation is allowed only if no responsibility becomes an underdeveloped subsection of another document.

### 9.2 Anticipated but not yet mandatory specialists

- professional play, schooling, work, and adulthood as an institutional pathway;
- gendered performance, attraction, and sexual boundary systems;
- ordinary life, food, games, clothing, and shared activity as relational evidence;
- adaptation divergence, if an adaptation corpus is later admitted.

An anticipated domain becomes mandatory only when the architecture amendment rule is met.

### 9.3 Specialist home

New character-external and relationship specialists should live under `../06 Specialist Synthesis/`, created when the first such artifact is authored. The existing `../05 Full-Series Synthesis/` identity is retained; numeric folder order does not override the dependency graph.

## 10. Evidence and locator routing

### 10.1 Retrieval chain

The intended production route is:

`locked Japanese source → source-facing volume reading → cumulative ledger/index → literary character/relationship/specialist synthesis → full-series synthesis`

Validation runs backward:

`full-series claim → contributing specialist claim → ledger or claim-index entry → volume-reading section → exact Japanese source locator where required`

A mature claim passes traceability only if a future reader can follow this chain without relying on the originating conversation.

### 10.2 Locator levels

Use the least duplicative locator that still permits deterministic retrieval:

- **L1 — artifact locator:** exact deep-reading or supplemental-reading path and section/table/claim number;
- **L2 — source-unit locator:** volume plus chapter, named story, scene boundary, or EPUB spine/XHTML item;
- **L3 — exact textual locator:** source item plus a short diagnostic Japanese phrase or unambiguous local marker;
- **L4 — package/visual locator:** archive item, image asset, or paratext block where visual/package evidence matters.

Retrospective character and relationship backfill may begin with L1 when the deep reading adequately preserves the evidence. L2/L3 is required before freezing a claim whose force depends on exact wording, speech register, translation, causal sequence, disputed attribution, or a high-propagation interpretation not fully preserved in the reading. Do not invent page numbers or quotations.

The claim/evidence index owns the current crosswalk and revision state. It should not reproduce long copyrighted passages; diagnostic Japanese is short and purpose-limited.

### 10.3 Wording and voice

Japanese wording notes live initially in the source-facing reading and later in the voice/register/key-terms ledger. Character monographs and specialists cite that ledger or the exact source locator. A remembered translation, English fandom term, or paraphrase cannot support a claim about register.

## 11. Claim revision and supersession

### 11.1 Revision vocabulary

Use these dispositions for material claims:

- `PRESERVE` — later evidence leaves the claim materially intact;
- `STRENGTHEN` — later evidence increases support or scope within stated limits;
- `REVISE` — the claim survives only in changed form;
- `DOWNGRADE` — possible but less supported, narrower, or more viewpoint-bound;
- `REJECT` — contradicted or no longer responsibly supportable;
- `OPEN` — evidence remains insufficient or competing accounts survive.

Each disposition must state the prior claim, changed evidence, current formulation, and downstream artifacts affected. `REVISE` must not conceal which part was abandoned.

### 11.2 Historical discoverability

Earlier numbered claims remain in their frozen readings. The new claim/revision index crosswalks only materially reusable or disputed claims into corpus-wide identifiers; it does not renumber or overwrite the original local registers. Current literary specialists cite the crosswalk where available and explicitly flag any claim they newly promote.

Artifact supersession is separate from claim revision. A successor names what it supersedes and the corpus map routes current authority. Immutable historical audits or frozen readings remain unchanged even when a later artifact demonstrates that their closure conclusion no longer governs.

### 11.3 Current pre-remediation artifacts

The existing V11 full-series synthesis is a provisional integration candidate produced before the mandatory cumulative and specialist dependencies existed. The former V11 validation audit remains a frozen record of what that tranche checked, but a new architecture/role-gap audit becomes current for architecture-readiness questions. The old audit's source-coverage results remain useful; its claim that architecture gaps were closed does not govern the remediation generation.

## 12. Dependency graph and execution order

The governing dependency chain is:

```text
source lock + analytical method + preserved V01–V11 readings
                         │
                         ▼
canonical architecture + architecture/role-gap audit
                         │
                         ▼
character-state + relationship-state backfill
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
claim/evidence index       social-system + voice ledgers
             └───────────┬───────────┘
                         ▼
major literary character monographs
                         ▼
relationship syntheses + thematic specialists
                         ▼
adversarial claim/locator audit + cross-specialist convergence
                         ▼
revised full-series synthesis
                         ▼
literary validation/release audit
                         ▼
optional derived reconstruction models and their own validation
```

Practical remediation order:

1. preserve and inventory the completed sequential evidence;
2. establish this architecture and a full role-gap audit;
3. backfill character-state and relationship-state chronology;
4. build the claim/evidence index and social-system ledger;
5. perform targeted Japanese source escalation and build the voice/register layer;
6. deepen Tomozaki and Hinami first, then Kikuchi and Mimimi;
7. deepen or honestly reclassify Tama, Mizusawa, and Yuzu; promote other figures only when earned;
8. write the three mandatory relationship syntheses and any earned ensemble synthesis;
9. write the mandatory thematic specialists;
10. adversarially reconcile claims, locators, and contradictions across specialists;
11. revise the full-series synthesis last;
12. validate and release the literary corpus;
13. only then create evidence-sufficient reconstruction models.

The current full-series synthesis gate is closed. Existing prose may be read as a hypothesis inventory, but it must not dictate ledger outcomes or be cosmetically expanded before its dependencies converge.

## 13. Completion gates

| Gate | Pass condition | Current state |
|---|---|---|
| Sequential-source completion | Every admitted witness has correct source routing, source-facing analysis, adjudication, and bounded freeze. | **PASS at V11 plus routed V06.5/V08.5** |
| Architecture establishment | Canonical architecture satisfies all Minimum Semantic Contract responsibilities and a role-gap audit tests the actual corpus. | **PASS at design/audit level; lifecycle remains EVOLVING** |
| Longitudinal reconciliation | Every mandatory cumulative home is backfilled through V11; overlaps and contradictions are reconciled; material claims have usable evidence routes. | **OPEN** |
| Specialist readiness | Required ledger inputs are stable enough to support literary drafting; promotion scopes are explicit; unresolved states are preserved. | **CLOSED** |
| Specialist completion | Required major characters, relationships, and thematic problems pass their semantic contracts and adversarial checks. | **NOT STARTED as mature layer; current monographs are candidates** |
| Cross-specialist convergence | Shared terms, time states, claims, and relationship facts agree or record explicit unresolved conflicts. | **CLOSED** |
| Full-series synthesis readiness | Longitudinal and specialist gates pass; a convergence audit authorizes integrated drafting. | **CLOSED** |
| Full-series synthesis completion | One integrated argument answers the series-wide problem without becoming synopsis or erasing open publication-boundary questions. | **CURRENT FILE IS PRE-REMEDIATION CANDIDATE, NOT GATE PASS** |
| Validation/audit completion | Backward traceability, source boundary, contradictions, uncertainty, architecture roles, repository checks, and release state all pass. | **OPEN; prior audit retained as historical checkpoint** |
| Frozen/release state | Exact reviewed artifacts are versioned, validated, and intentionally release-locked under repository governance. | **NOT REACHED** |

Passing a later gate never retroactively changes a frozen earlier reading. V11 source-boundary completion is not series-ending closure.

## 14. Reasoning-class routing

Stable workload classes govern durable routing; literal provider/model names are time-bounded execution metadata.

| Operation | Default stable class | Escalation condition |
|---|---|---|
| Source inventory, checksums, mechanical manifests | `ROUTINE_FAST` or `BOUNDED_STANDARD` | edition identity or semantic source routing is ambiguous |
| Sequential deep reading | `SUBSTANTIVE_ANALYSIS` | unusually dense causal, linguistic, or contradiction burden → `DEEP_SYNTHESIS` |
| Character/relationship/social ledger backfill | `DEEP_SYNTHESIS` | corpus-wide claim rerouting or unusually high propagation risk → `PREMIUM_QUALITY_FIRST` |
| Locator construction | `BOUNDED_STANDARD` | wording/attribution adjudication → `SUBSTANTIVE_ANALYSIS` or higher |
| Claim-revision index | `DEEP_SYNTHESIS` | load-bearing whole-corpus reclassification → `PREMIUM_QUALITY_FIRST` |
| Major literary monograph | `DEEP_SYNTHESIS` | Tomozaki/Hinami or comparable central contradiction density → `PREMIUM_QUALITY_FIRST` |
| Relationship or thematic specialist | `DEEP_SYNTHESIS` | architecture-defining conflict resolution → `PREMIUM_QUALITY_FIRST` |
| Synthesis architecture, adversarial role-gap audit, cross-specialist convergence | `PREMIUM_QUALITY_FIRST` | already quality-first by responsibility |
| Full-series synthesis | `PREMIUM_QUALITY_FIRST` | default because errors propagate across the corpus |
| Reconstruction model | `DEEP_SYNTHESIS` | cross-model consistency audit → `PREMIUM_QUALITY_FIRST` |
| Pure release administration | `ROUTINE_FAST` or `SUBSTANTIVE_ANALYSIS` | adversarial semantic release audit → `PREMIUM_QUALITY_FIRST` |

The owner directed Max reasoning for this remediation's synthesis documents and character monographs. That current execution control takes precedence for this operation. It is recorded without claiming that a Codex reasoning control is identical to ChatGPT Pro or to any durable class. A new model family was available at design time, so official [OpenAI GPT-6 Astra model guidance](https://developers.openai.com/api/docs/models/gpt-6-astra) was rechecked on 2026-09-13; the stable classes survive future provider changes.

## 15. Mutable, frozen, and superseded behavior

### 15.1 Immutable historical states

- V01–V11 deep readings and the V06.5/V08.5 supplemental readings are prospectively frozen.
- A frozen audit or explicit release artifact remains unchanged; a successor corrects its authority claim.
- Historical claims, failed predictions, and uncertainty remain discoverable.

### 15.2 Mutable current authority

- this architecture remains mutable while `EVOLVING`;
- the corpus map is updated in place as current routing changes;
- cumulative ledgers and the claim/evidence index are maintained through targeted edits;
- literary monographs and specialists are mutable until an explicit validated release;
- the source lock changes only through a documented source-admission operation.

Material document-wide revision is permissible during this owner-directed remediation only with identity/provenance preserved and the full diff reviewed. Authored ledgers must not be regenerated from summaries.

### 15.3 Supersession

A successor artifact must identify the prior artifact and the responsibility superseded. Superseded work is retained as historical evidence unless repository policy provides a governed archive move. The corpus map, not timestamp guessing, tells future readers what is current.

## 16. Reconstruction and simulation models

Tomozaki is frequently used for counterfactual social scenarios, so a derived reconstruction layer is likely valuable after literary stabilization. It must live under `../07 Character Reconstruction Models/` and use at least:

- `artifact_type: character_reconstruction_model`;
- `authority_class: derived_use_model`;
- `do_not_use_as_primary_literary_authority: true`;
- explicit literary, ledger, locator, and audit dependencies;
- an era/state selector before behavioral inference;
- attentional priorities, motive hierarchy, decision heuristics, stress behavior, relationship-conditioned variation, voice/register controls, ordinary habits, failure modes, anti-caricature rules, domain confidence, and out-of-distribution warnings.

Model generation order is `select state → select relationship/standing → establish knowledge and stakes → infer attention → infer motives and constraints → generate behavior/register → test negative constraints`. Unknowns remain unknown. A reconstruction model cannot supply circular evidence back to the literary corpus.

Primary-source escalation for a model is targeted: compile from mature literary authority, identify a thin or contradictory field, reopen only the needed source scene, and record why the escalation occurred and what changed.

No reconstruction model is authorized as part of the first remediation tranche.

## 17. Architecture amendment rule

A new ledger, specialist, or analytical layer may be added when the dimension:

- recurs across multiple source units;
- accumulates evidence independently;
- affects later synthesis;
- cannot be represented adequately in a current canonical home; or
- requires independent retrieval for future literary or reconstruction work.

Removal or consolidation is allowed when the proposed responsibility is non-independent, duplicative, or unsupported. Material amendments must update this document's version/history and the corpus map. A discovered gap triggers retrospective backfill only when existing readings or targeted source access can repair a material retrieval failure; it does not license cosmetic rereading.

Promotion from `EVOLVING` to `STABILIZED` requires:

1. the role-gap audit to enumerate the mature responsibilities;
2. all mandatory longitudinal homes to exist with stable schemas;
3. character and relationship promotion decisions to be explicit;
4. specialist domains and dependency order to be substantially known;
5. no material observation class to lack a destination.

`FROZEN` requires an intentional release and does not follow automatically from stabilization.

## 18. Responsibility matrix

| Analytical dimension | Sequential capture | Canonical cumulative home | Mature destination | Remediation state |
|---|---|---|---|---|
| Witness identity, package, chronology | yes | source lock + source-facing reading | audit/provenance | satisfied |
| Prospective questions, predictions, falsifiers | yes | frozen source-facing reading; material crosswalk in claim index | relevant specialist | satisfied locally; crosswalk pending |
| Character developmental state | yes | character-state ledger | monograph + relationships + final synthesis | backfilled through V11; reconciliation current |
| Directional relationship/network state | yes | relationship-state ledger | relationship/ensemble specialists | backfilled through V11; reconciliation current |
| Effort, competition, rank, goal ownership | yes | existing effort/competition ledger | effort specialist + character studies | current through V11 |
| Major claims and revision history | yes | claim-revision/evidence index | all mature synthesis | L1 crosswalk backfilled through V11 |
| Source locators | uneven but substantial | claim-revision/evidence index; source readings | audit + mature synthesis | L1 current; twelve targeted L2/L3 queues open |
| Social atmosphere, reputation, punishment, repair | yes across several volumes | social-atmosphere/group-systems ledger | social-system specialist | backfilled through V11; specialist pending |
| Technique, learned form, authenticity, authorship | yes | character/relationship ledgers + claim index | game/form/self-authorship specialist | distributed; specialist pending |
| Causality, result, reason, meaning | yes, especially V08.5–V11 | claim index + character/relationship ledgers | control/causality/meaning specialist | distributed; specialist pending |
| Romance, privacy, disclosure, consent, intervention | yes | relationship ledger + claim index | three relationship specialists + ethics specialist | backfill pending |
| Fiction, observation, personhood, publication | yes | character ledger + claim index | Kikuchi monograph + authorship specialist | distributed; specialist pending |
| Japanese key terms | intermittent | voice/register/key-terms ledger | all language-sensitive specialists | partial; source escalation required |
| Character-specific voice, address, register | intermittent | voice/register/key-terms ledger | monographs + later reconstruction models | too thin; targeted source checks required |
| Ordinary-life preferences and habits | local as relevant | character/relationship ledgers | monographs; later models | no separate ledger yet |
| Professional play, school, work, future | yes | effort/goal ledger | Tomozaki monograph; possible future-path specialist | substantially routed |
| Visual/paratext evidence | diagnostic only | source reading/source lock | local specialist claim if needed | intentionally local/distributed |
| Reconstruction readiness | not a source-reading obligation | future reconstruction readiness entries/audit | derived-use models | deferred until literary convergence |

Every new recurring observation must route to a cumulative home, a named direct synthesis responsibility, or an explicit local-only status.

## 19. Canonical entrypoint and retrieval route

Start with `../CURRENT_STATE_AND_CORPUS_MAP.md`. Before changing project state, read in order:

1. this architecture;
2. `TOMOZAKI_ANALYTICAL_METHOD.md`;
3. the source lock;
4. the current architecture/role-gap audit;
5. the ledger(s), monograph(s), specialist(s), and source-facing reading(s) governing the requested responsibility;
6. live repository governance and working-tree state before any mutation or integration step.

The corpus map must always expose the exact completed source boundary, architecture lifecycle, current ledgers, mature versus provisional character/specialist status, open synthesis gate, and next required operation.

## 20. Revision history

### v1.1 — 2026-09-13 — first cumulative backfill instantiated

- Accepted canonical mutable V11 backfills for character state, directional relationship state, claim/evidence lineage, and social-atmosphere/group systems.
- Recorded the claim index's complete 319-claim/140-question universe, promoted/local partition, and twelve targeted L2/L3 escalation queues.
- Kept longitudinal reconciliation open because Japanese voice/register, targeted source escalation, and cross-ledger convergence remain unfinished.
- Kept specialist and full-series gates closed.

### v1.0 — 2026-09-13 — remediation architecture established

- Recorded that the project historically lacked the required synthesis architecture before V01.
- Preserved every numbered and supplemental source-facing freeze as canonical historical evidence.
- Separated method, architecture, and entrypoint responsibilities.
- Defined source topology, state model, contradiction classes, authority ladder, evidence levels, claim revision, dependencies, completion gates, reasoning routing, and mutable/frozen behavior.
- Promoted character-state, relationship-state, claim/evidence, social-atmosphere/group-systems, and Japanese voice/register cumulative responsibilities based on the completed corpus.
- Defined major character, relationship, and thematic specialist responsibilities.
- Closed the specialist and full-series synthesis gates until cumulative backfill and cross-specialist convergence are complete.
- Deferred reconstruction models until literary authority is mature.
