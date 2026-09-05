---
series: PJSK
artifact_type: synthesis_architecture
scope: FULL_SERIES
generation: V1
status: canonical
source_boundary: "Project SEKAI analytical layer"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---


# Project SEKAI Synthesis Architecture


## Purpose


This architecture defines how local readings become longitudinal understanding without duplicating analytical responsibility. The project should be able to answer both literary questions and reconstruction questions while preserving source provenance, temporal state, and authority.


The core rule is: story analysis owns shared causes; ledgers own transitions; character monographs own person-level interpretation; reconstruction models own conditional prediction; syntheses own cross-document integration.


## Analytical layers


### Layer 1 — Source and provenance
Owned by the existing source pipeline. Canonical stories, structured records, chronology metadata, character/relationship/unit projections, and stable locators live there. The interpretive layer should reference rather than duplicate this material. The analytical layer may maintain `PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md` as a franchise-wide discovery/routing index pointing back to those source objects; it must not duplicate transcript bodies.


### Layer 2 — Bounded deep readings
Main-story phases and major event readings explain what happens within a coherent narrative block. They are the canonical home for local causal interpretation.


### Layer 3 — Longitudinal ledgers
Mutable cumulative infrastructure records state transitions across bounded readings. Core ledgers are CHARACTER_STATE, RELATIONSHIP_STATE, EPISTEMIC_STATE, THEME_AND_MOTIF, RELEASE_IMPACT, and CLAIM_REVISION.


### Layer 4 — Character and relationship synthesis
Character monographs interpret identity, psychology, values, development, social masks, contradictions, and relationships. Relationship syntheses exist only for pairings/groups whose independent analytical importance warrants a dedicated artifact.


### Layer 5 — Reconstruction
Reconstruction models translate interpreted character evidence into conditional behavioral and speech predictions across temporal states, interlocutors, contexts, and stakes.


### Layer 6 — Unit and specialist synthesis
Unit syntheses integrate long spans of events and character development. Specialist documents own genuinely distinct topics such as family systems, creative labor, SEKAI ontology, musical identity, or other recurring analytical dimensions.


### Layer 7 — Full-series synthesis
Cross-unit and whole-series interpretation is produced only after sufficient lower-layer coverage. Full-series synthesis should not become a dumping ground for unresolved local analysis.


## Main-story architecture


Each human-unit main story receives:
1. four to six phase DEEP_READING artifacts;
2. state/relationship/epistemic ledger updates;
3. one MAIN_STORY_SYNTHESIS.


The synthesis should normally cover:
- initial configuration of the unit and each member;
- structural phases and causal progression;
- major conflicts and revelations;
- relationship topology and changes;
- psychological state transitions;
- self-concept and social-mask changes;
- epistemic asymmetries;
- thematic/structural mechanisms;
- ending equilibrium;
- unresolved tensions passed into events;
- character-specific implications that later monographs can reuse without retelling the story.


The synthesis is not a concatenation of phase summaries. It is a higher-level causal model of how the foundation works.


## Event architecture


Events first receive one franchise-wide complete-envelope relevance screen recorded in `PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md`. Material then enters 03_SEQUENTIAL_EVENT_READINGS according to the unit or MIXED scope that actually requires interpretation. Analysis depth is determined by significance rather than release equality, and later unit work consumes the preserved routing record rather than repeating source discovery.


A developmental or relationship-heavy event gets a full DEEP_READING. Characterization-heavy events may get shorter focused readings. Ordinary behavioral material can be indexed directly into evidence and reconstruction infrastructure when no distinct literary artifact is warranted.


Every event with material consequences should emit a structured delta:
- character state delta;
- relationship delta;
- epistemic delta;
- claim revision delta;
- reconstruction relevance;
- unresolved implications.


## Franchise-wide event relevance and routing layer


`PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md` is the canonical bridge between the source/provenance layer and unit-specific event interpretation. It belongs in `01_SOURCE_LOCK_AND_INVENTORY` because its responsibility is reusable discovery and retrieval routing rather than cumulative psychological state.


The expensive operation is the complete-envelope screen. Perform it once at franchise scope. Before source cleanup, preserve which units, characters, relationships, evidence domains, and exact locators are materially represented. This record may be created even when some unit foundations do not yet exist.


Unit relevance and longitudinal impact are different questions. A route may be PRIMARY, SECONDARY, CROSS_UNIT, INCIDENTAL, NONE, or UNRESOLVED before its baseline-relative impact can be known. I0-I3 is assigned only after the relevant unit/character baseline is mature enough to compare before and after. Until then use `DEFERRED_PENDING_FOUNDATION`.


When another unit later receives a main-story foundation, its event-analysis queue is generated from this routing ledger rather than by rereading the complete franchise event corpus. Existing `NONE` routes are skipped by default; PRIMARY/SECONDARY/CROSS_UNIT routes are interpreted from preserved locators. A complete-envelope reread is exceptional and requires a demonstrated routing deficiency; otherwise reopen only targeted evidence surfaces.


Legacy complete-envelope passes performed under an N25-focused workflow remain reusable. Their non-N25 extraction quality must be marked conservatively so later work can distinguish `ROUTED_FROM_EXISTING_COMPLETE_READING`, partial non-active-unit detail, and genuine `TARGETED_RECHECK_REQUIRED` cases without discarding prior source review.


## Longitudinal ledger responsibilities


### PJSK_CHARACTER_STATE_LEDGER
Tracks psychologically meaningful states over time. States are append-only historically. New states do not erase old ones.


### PJSK_RELATIONSHIP_STATE_LEDGER
Tracks pair/group relationship changes, including asymmetry. Record trust, intimacy, dependency, rivalry, resentment, admiration, vulnerability, authority, communication norms, and repair patterns where material.


### PJSK_EPISTEMIC_STATE_LEDGER
Tracks who knows, believes, suspects, misunderstands, or does not know what. This ledger prevents an otherwise accurate reconstruction from using future knowledge in an earlier state.


### PJSK_THEME_AND_MOTIF_LEDGER
Tracks recurring thematic and symbolic material across units/events without forcing every local reading to recreate the whole thematic history.


### PJSK_RELEASE_IMPACT_LEDGER
Tracks what each new live-service release materially changes and which canonical artifacts require update.


### PJSK_CLAIM_REVISION_LEDGER
Routes earlier analytical claims through PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, or OPEN transitions.


## Character package architecture


Create a character folder only when substantive analysis begins. A mature principal-human package normally contains:


PJSK_<CHARACTER>_CHARACTER_MONOGRAPH
Owns identity, background, self-concept, values, needs, fears, defenses, emotional architecture, agency, social masks, relationships, contradictions, and development.


PJSK_<CHARACTER>_RECONSTRUCTION_MODEL
Owns behavioral invariants, state-dependent variables, context modes, relationship-conditioned behavior, stakes/pressure response, speech/register, anti-patterns, and evidence-distance rules.


PJSK_<CHARACTER>_EVIDENCE_INDEX
Owns locators and categorized evidence. It should remain compact and retrieval-oriented rather than repeating interpretive prose.


STATE_HISTORY/
Optional separate state snapshots when temporal complexity makes them useful. State history preserves earlier simulation targets.


Do not automatically split speech, relationships, psychology, and behavior into separate monographs unless evidence volume or retrieval need justifies independent responsibility.


## Reconstruction interfaces


Every reconstruction model should be callable conceptually with:


state S + relationship R + knowledge K + context C + stakes H -> plausible goals -> choice -> behavior -> speech.


The model should distinguish:
- behavioral invariants;
- state-dependent variables;
- context modes;
- relationship conditioning;
- stakes and pressure;
- textual speech/register;
- behavioral constraints and anti-patterns;
- evidence distance D0-D4.


This interface is the bridge from literary analysis to scenario simulation.


## Unit syntheses


A unit longitudinal synthesis is warranted when accumulated event readings materially extend beyond the main-story foundation. It should integrate:
- durable character development;
- evolving unit identity;
- relationship topology;
- changing artistic/professional goals;
- major external pressures;
- recurring thematic structures;
- unresolved trajectories;
- current reconstruction-relevant states.


Do not rewrite the entire unit synthesis after every event. Mutable ledgers carry incremental change; major synthesis generations are produced at meaningful analytical milestones.


## Specialist syntheses


Create specialist artifacts only when a dimension:
- recurs across many readings;
- accumulates substantial evidence;
- supports later synthesis or reconstruction;
- requires independent retrieval.


Examples may include:
- family and parental systems;
- creative labor and artistic validation;
- performance and public identity;
- SEKAI as psychological/narrative space;
- online/offline identity;
- institutional school/idol/music-scene pressures;
- cross-unit social networks.


Specialist synthesis should not steal responsibility from character monographs or event deep readings.


## Full-series synthesis


Full-series synthesis should be generation-based and frozen when declared complete. It should integrate only claims already supported by lower layers, except where the synthesis explicitly opens a new cross-series hypothesis and marks it accordingly.


A full synthesis generation should identify:
- source and analysis cutoff;
- included unit/event coverage;
- current authority state;
- unresolved gaps;
- supersession relationship to earlier generations.


## Mutable versus frozen artifacts


Normally mutable:
- analytical corpus map;
- event relevance and routing ledger;
- current reconstruction models;
- evidence indexes;
- state/relationship/epistemic ledgers;
- release-impact ledger;
- claim-revision ledger;
- current-release manifests.


Normally frozen once declared a release:
- major unit synthesis generations;
- full-series synthesis generations;
- archival locks/manifests.


Corrections to frozen releases should normally become later generations rather than silent mutation.


## Authority and duplication control


Before creating an artifact, ask:
1. Is there already a canonical topical home for this insight?
2. Is this new document analytically distinct or merely more recent?
3. Will another artifact be forced to repeat the same interpretation?
4. Does the new artifact have a clear scope, authority state, and retrieval purpose?


Prefer updating the existing canonical home. Preserve materially distinct superseded work under 90_LEGACY_AND_SUPERSEDED. Delete only genuine redundancy.


## Completion standard


The architecture is working when a new reader can move from a question to the correct current artifact, then to supporting ledger state, then to exact source evidence, without needing to infer which of several similarly named files is authoritative.