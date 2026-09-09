---
series: PJSK
artifact_type: live_service_integration_method
scope: FULL_SERIES
generation: V1
status: canonical
source_boundary: "Ongoing Project SEKAI live-service releases"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---


# Project SEKAI Live-Service Integration Method


## Purpose


Project SEKAI is an ongoing live-service work. The analytical corpus must absorb new releases without periodically restarting the project, erasing historical states, or silently allowing unreviewed material to alter current character models.


The governing rule is:
source corpus grows continuously; each event envelope is screened once at franchise scope; analytical authority advances through controlled scope-specific integration checkpoints.


## Three current boundaries


Always distinguish:


SOURCE_CURRENT
Newest material successfully ingested into the source/provenance corpus.


ANALYSIS_CURRENT
Newest material that has been read, interpreted, and integrated into canonical analytical infrastructure.


RECONSTRUCTION_CURRENT
Newest state considered safe as the default for present-day character simulation.


These boundaries may differ. Source-current material must not silently contaminate reconstruction-current authority.


## Intake lifecycle


New game content follows:
new release -> source pipeline ingest -> 08_CURRENT_RELEASE -> franchise-wide complete-envelope screen -> EVENT_RELEVANCE_AND_ROUTING_LEDGER -> scope-specific impact triage -> required analysis -> claim revision -> state/relationship/epistemic updates -> reconstruction delta -> promotion to integrated authority.


08_CURRENT_RELEASE is an analytical staging area, not a second source archive.


## Integration packet


A release or analytically coherent batch may receive an integration packet containing:
- release/event identifier;
- source locators;
- core event story;
- associated card stories;
- event-linked area conversations;
- relevant self/special/My SEKAI material;
- involved characters;
- relationship relevance;
- chronology/condition notes;
- preliminary analytical significance;
- existing claims potentially affected;
- required treatment level.


Do not duplicate full transcript bodies in the packet when source locators provide reliable retrieval.


## Franchise-wide relevance routing before impact triage


Every event complete-envelope pass is first treated as a reusable franchise-wide discovery operation. Before an active unit receives I0-I3 triage, update `PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md` with the event's complete envelope, materially represented units/characters/relationships, evidence domains, exact locators, and future review priority.


The routing ledger answers **what the release contains and where later analysis should look**. `PJSK_RELEASE_IMPACT_LEDGER.md` answers **what the release changes relative to an established analytical baseline**. Do not collapse these responsibilities.


For units or characters whose main-story/longitudinal foundation is not mature enough for before/after comparison, record relevance but set impact to `DEFERRED_PENDING_FOUNDATION`. Roster presence, marketing focus, or obvious event centrality is not enough to assign I0-I3 without a baseline.


A later unit project must build its event queue from the routing ledger rather than restart a blind sequential pass over every event. Routes marked NONE are skipped by default. PRIMARY, SECONDARY, and CROSS_UNIT routes are reopened only at the preserved evidence surfaces unless a concrete routing deficiency requires a larger recheck.


For complete-envelope readings created before this rule, preserve the source work under conservative backfill states. `ROUTED_FROM_EXISTING_COMPLETE_READING` means the envelope pass is reusable; partial non-active-unit extraction may still require targeted rereading. `PENDING_ONE_TIME_UNIVERSAL_SCREEN` means the event still needs one franchise-wide pass, not one pass per unit.


## Impact classes


I0 RECORD_ONLY
No meaningful analytical change. Keep source retrievable; no prose analysis required.


I1 CHARACTERIZATION_INCREMENT
Adds evidence for an established trait, preference, speech pattern, ordinary behavior, or relationship tendency. Usually update evidence indexes and possibly STRENGTHEN an existing claim.


I2 INTERPRETIVE_REFINEMENT
Changes how an established behavior, motive, relationship, or theme should be understood. Requires claim-revision review and targeted updates.


I3 STATE_CHANGING_RELEASE
Produces a durable psychological, relationship, epistemic, or unit-level transition. Requires full deep reading, ledger updates, reconstruction review, and possibly later synthesis-generation work.


Impact class is about analytical consequence, not marketing importance or event rarity.


## Release impact ledger


Maintain PJSK_RELEASE_IMPACT_LEDGER with fields conceptually equivalent to:
release
character/unit
impact class
state change
relationship change
epistemic change
claim revision
reconstruction update required
integration status


This ledger is the consequence-routing surface for deciding what a new release actually changes relative to a mature analytical baseline. Franchise-wide discovery and future-unit retrieval are owned by `PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md`.


## Historical state preservation


Character states are append-only historically.


If a character progresses M4 -> M5, M4 remains authoritative for scenarios set during its valid period. Never rewrite M4 to resemble the current character.


The same rule applies to relationship and epistemic states. Later disclosure must not erase earlier ignorance; later intimacy must not be projected backward.


## Reconstruction delta


Every I2 or I3 release affecting a reconstruction-ready character should produce a compact delta:


PRESERVED
Existing behavior/psychology still supported.


STRENGTHENED
Existing claim receives stronger or broader evidence.


REVISED
Prior formulation remains partly useful but must change.


DOWNGRADED
Prior confidence should be reduced.


REJECTED
Later evidence directly defeats the prior formulation.


NEW
New state, relationship mode, speech behavior, preference, coping strategy, or conditional tendency.


CURRENT STATE
The state identifier that should now be the default after integration.


This delta should update the canonical model rather than create an endless series of "updated" profiles.


## Selective model updates


A new event involving a character does not automatically justify rewriting the whole monograph or reconstruction model.


Ask which semantic responsibilities changed:
- psychology/self-concept;
- relationship with a specific person;
- knowledge state;
- ordinary behavior;
- stress response;
- speech/register;
- values or priorities;
- unit role.


Update only the canonical sections affected. If nothing material changes, index the evidence and mark the appropriate claim PRESERVE or STRENGTHEN.


## Relationship and epistemic independence


A character may undergo little internal change while one relationship changes substantially. Update RELATIONSHIP_STATE even when CHARACTER_STATE does not require a new state identifier.


Likewise, information acquisition can change plausible behavior immediately without changing personality. Update EPISTEMIC_STATE independently.


## Current simulation rule


Default current-character simulation uses the latest fully integrated reconstruction-current state, not merely the newest source material available.


If a scenario explicitly requires material newer than the analytical cutoff, perform a provisional current-release reading and label its conclusions provisional. Do not silently promote them to canonical reconstruction authority.


## Analytical lag visibility


PJSK_ANALYTICAL_CORPUS_MAP should expose at least:
- source-current boundary;
- fully integrated boundary;
- partially integrated material;
- pending material;
- reconstruction-current boundary for characters whose status differs materially.


This makes analytical lag explicit rather than forcing a future reader to infer it from file modification times.


## Update cadence


Use three cadences:


Immediate source ingestion
The source pipeline may remain continuously current.


Rapid triage
Record franchise-wide relevance routes, then classify baseline-mature scopes and identify affected analytical responsibilities.


Deferred integration
Perform deep analysis when the relevant unit/character work is advanced. There is no requirement to interrupt current N25 analysis because unrelated VBS material was just released.


## Synthesis generations


Do not continuously rewrite frozen major syntheses after every event.


Mutable ledgers and reconstruction models absorb incremental change. Create a new unit/full-series synthesis generation only at analytically meaningful milestones such as:
- completion of a major narrative arc;
- major unit status change;
- major character-state transition;
- anniversary or release boundary that corresponds to real narrative consolidation;
- accumulated changes making the previous synthesis materially obsolete.


Calendar passage alone is not sufficient reason for a new generation.


## Frozen versus mutable


Mutable by default:
- analytical corpus map;
- current-release manifests;
- event relevance and routing ledger;
- release impact ledger;
- character/relationship/epistemic ledgers;
- claim revision ledger;
- current reconstruction model;
- evidence index.


Frozen when explicitly released:
- major unit synthesis generations;
- full-series synthesis generations;
- archival locks and manifests.


Corrections to frozen releases normally become later generations rather than silent edits.


## Source-context safeguards


Do not flatten uncertain or conditioned chronology merely to make an incremental timeline look complete. Preserve undated, condition-ordered, special, alternate, and My SEKAI context classes where the source pipeline does so.


Virtual Singer material requires context-aware manifestation handling. New appearances should not automatically be generalized across every manifestation.


## Promotion checklist


Before a release leaves 08_CURRENT_RELEASE and becomes integrated:
1. Source locators and chronology/context are resolved as far as the corpus supports.
2. Franchise-wide relevance routing is complete; impact class is assigned for the active baseline-mature scope, while unfounded scopes are marked `DEFERRED_PENDING_FOUNDATION`.
3. Required deep reading or characterization extraction is complete.
4. Character-state effects are recorded.
5. Relationship effects are recorded.
6. Epistemic effects are recorded.
7. Claim revisions are routed.
8. Reconstruction deltas are applied where necessary.
9. Evidence indexes are updated.
10. Analytical cutoff metadata is advanced only for the scope actually integrated.


## Failure mode to avoid


The project should never need a giant "V2 because the old Project SEKAI analysis became stale" solely because the game kept releasing content. The preferred model is continuous integration of state and evidence with periodic frozen synthesis generations.


A reread generation is justified when the analytical method itself improves enough to warrant reinterpretation, not simply because new episodes exist.