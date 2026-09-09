---
series: PJSK
artifact_type: analytical_method
scope: FULL_SERIES
generation: V1
status: canonical
source_boundary: "Project SEKAI Japanese corpus pipeline"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---


# Project SEKAI Analytical Method


## Objective


The analytical program has two equally important goals: understand the story as a longitudinal narrative, and reconstruct major characters well enough to predict plausible thought, behavior, and speech across low-, medium-, high-, and unfamiliar-stakes scenarios. Story analysis and reconstruction must share evidence without collapsing into one artifact.


The primary analytical sequence is:
source evidence -> complete-envelope franchise screen -> event relevance/routing -> bounded deep reading / active-scope integration -> state transition -> longitudinal ledger -> synthesis -> character monograph -> reconstruction model -> audit.


## Evidence authority


The source pipeline is authoritative for transcript text, metadata, story identity, chronology metadata, and provenance. Generated character, relationship, unit, and contextual bundles are retrieval projections, not independent narrative authorities. Exact quotations and disputed readings should route back to canonical story records.


Fan transcript mirrors are research primary-text proxies rather than official-publication authority. Important verbatim claims should be verifiable against the game or independently rendered assets when publication-grade certainty matters.


## Unit of analysis


Do not default to chapter-by-chapter essays. Human-unit main stories should be read exhaustively but interpreted in coherent causal phases, normally four to six phases across a 21-episode foundation. Events are analyzed as whole event narratives unless a genuinely distinct internal sub-arc warrants separate treatment.


A phase boundary is justified by one or more of:
- durable psychological transition;
- relationship-state transition;
- epistemic revelation;
- causal turning point;
- thematic/structural shift;
- new equilibrium after crisis.


Do not split a continuous crisis merely to equalize block size.


## Seven analytical lenses


Every substantial story deep reading should address seven lenses.


1. Narrative and causal structure
What happens? What causes what? Which events are necessary rather than merely adjacent? What is setup, escalation, reversal, climax, and consequence?


2. Psychological state
For each central character, identify active goals, fears, beliefs, self-concept, suppressed or unrecognized needs, coping strategies, and emotional baseline. Distinguish internal state from outward presentation.


3. Relationship state
Track trust, intimacy, dependence, rivalry, resentment, admiration, authority, vulnerability, and communication patterns. Relationship states may be asymmetric.


4. Epistemic state
Track what each character knows, believes, suspects, misunderstands, and does not know. Knowledge changes must be separated from personality changes.


5. Behavior and speech
Record observable decisions, initiative, avoidance, conflict responses, repair behavior, practical habits, and speech/register evidence. Treat speech as behavior conditioned by state and interlocutor, not as a bag of catchphrases.


6. Theme and structure
Identify recurring ideas, motifs, symbolic spaces, music/creative practice, family/social institutions, identity structures, and narrative contrasts. Do not force every scene into a thematic thesis.


7. Continuity and revision
Compare the current reading with existing claims. Use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, or OPEN where later evidence materially changes an interpretation.


## Phase-reading template


Each main-story phase or major event deep reading should normally contain:
- scope and source boundary;
- concise narrative map;
- causal analysis;
- character-by-character state analysis;
- relationship changes;
- epistemic changes;
- key behavioral and speech evidence;
- thematic/structural interpretation;
- contradictions or alternative readings;
- state handoff at the end of the block;
- for events, franchise-wide relevance/routing outcome and deferred-unit flags;
- claims to update in longitudinal ledgers;
- unresolved questions for later material.


The state handoff is mandatory for developmental material. It should make clear what is true at the end of the block that was not true at the beginning.


## Main-story foundation method


For each human unit:
1. Inspect all 21 episodes and propose provisional phase boundaries.
2. Read every episode in order before finalizing the boundary that contains it.
3. Produce phase deep readings with episode-level locators retained inside the block.
4. Update initial character, relationship, and epistemic states after each phase.
5. Produce a MAIN_STORY_SYNTHESIS only after all phase readings are complete.
6. Mark the ending state as the foundation from which later events depart.


The main-story synthesis should establish a shared historical substrate for all four unit members so later character monographs do not independently retell the same narrative.


## One-pass franchise event screening and deferred unit routing


The expensive complete-envelope event pass is a franchise-level discovery operation, not a unit-specific operation. A source envelope should normally be inspected once, with reusable routing captured before temporary source payloads are cleaned up.


For every event envelope, record in `PJSK_EVENT_RELEVANCE_AND_ROUTING_LEDGER.md`:
- exact envelope boundary and completion status;
- materially represented units, characters, and relationship pairs/groups;
- relevance as PRIMARY, SECONDARY, CROSS_UNIT, INCIDENTAL, NONE, or UNRESOLVED;
- evidence domains and exact evidence-bearing locators;
- participant-side, retrospective, audience-only, inferred, or context-conditioned status where material;
- future review priority;
- routing/backfill quality and any targeted-recheck requirement.


Discovery authority and longitudinal-impact authority must remain separate. I0-I3 is assigned only where a sufficiently mature unit/character baseline exists. For an unfounded unit, preserve the route as `DEFERRED_PENDING_FOUNDATION` rather than guessing impact from roster presence or event prominence.


After a new unit main-story foundation is completed, generate that unit's event queue from the routing ledger. Do not restart at EVENT_0001 and blindly reread the full event corpus. Interpret PRIMARY/SECONDARY/CROSS_UNIT routes from their preserved locators, skip NONE by default, and reopen a complete envelope only when a concrete routing deficiency is demonstrated. Otherwise use targeted locator-level rereads.


A complete source pass does not imply that every unit has already received full longitudinal interpretation. It means later unit work begins from preserved franchise-wide discovery rather than repeating discovery. Earlier unit-focused complete-envelope readings may be reused under conservative backfill states, with partial non-active-unit extraction explicitly marked instead of overstated.


## Event significance tiers


Tier A / developmental
Produces durable character-state change. Requires full deep reading and ledger updates.


Tier B / relationship
Substantially changes or exposes an important relationship. Usually requires full deep reading and relationship/epistemic updates.


Tier C / characterization
Deepens established psychology without a major transition. Moderate analysis is appropriate.


Tier D / behavioral and ordinary-life
Provides valuable evidence about everyday habits, humor, preferences, initiative, irritation, practical behavior, and conversational style. Extract and index aggressively; do not inflate every scene into a literary essay.


Tier E / special or alternate context
Keep analytically separated unless continuity is established. Do not silently treat alternate, special, April Fool, or My SEKAI context as ordinary continuity.


## Source-type functions


Main story: foundational psychology, relationships, unit formation, initial state transitions.
Major events: longitudinal development and durable change.
Character-focus events: deep character psychology and self-concept.
Card stories: fine-grained characterization, private behavior, relationships, practical habits.
Area dialogue: ordinary-life baseline, casual interaction, conversational rhythm, cross-unit behavior.
Self material: presentation and self-description.
Special material: context-specific evidence requiring continuity checks.
My SEKAI: useful but separate context class unless justified otherwise.
Audio: vocal-performance evidence where aligned; it does not replace textual authority.


## Longitudinal state method


Character state, relationship state, and epistemic state must be maintained separately. A character can remain psychologically stable while learning new information or changing one relationship substantially.


Character-state records should include:
- temporal/source boundary;
- self-concept;
- goals;
- fears;
- emotional baseline;
- social masks;
- dependencies;
- coping strategies;
- agency level;
- stress vulnerabilities;
- speech/register changes;
- key evidence.


Historical states are preserved. Later growth does not overwrite earlier authority for scenarios set in earlier periods.


## Low-stakes requirement


Every serious character reconstruction must include ordinary-life evidence. High-stakes climax scenes reveal value priority under pressure but are insufficient to reconstruct daily personality. Low-stakes evidence should answer questions such as:
- who initiates conversation;
- how the character jokes or responds to teasing;
- what interests or bores them;
- how they respond to inconvenience;
- whether they give practical help;
- how they shop, study, practice, plan, eat, or spend downtime;
- how much silence they tolerate;
- how direct they are when nothing dramatic is forcing disclosure.


## High-stakes requirement


High-stakes evidence should identify value ordering under conflict: loyalty versus self-preservation, honesty versus relationship preservation, autonomy versus obligation, success versus protection, public image versus private need, and similar tradeoffs. Reconstruction should model which priorities survive pressure rather than merely label a character brave, kind, selfish, or anxious.


## Contradictions and uncertainty


Do not force characters into perfect consistency. Distinguish:
- durable trait;
- context-specific behavior;
- temporary state;
- development over time;
- self-misunderstanding;
- deliberate mask;
- genuine contradiction;
- uncertain interpretation.


When evidence is inadequate, mark OPEN rather than filling the gap from genre convention or fan expectation.


## Output discipline


Prefer one canonical topical home per semantic responsibility. Update an existing ledger, monograph, reconstruction model, or synthesis when the new insight belongs there. Create a new artifact only when it has a distinct analytical function.


The purpose of the architecture is not maximal document count. It is to preserve causal history, current authority, and retrievability while allowing detailed character reconstruction without repeatedly re-reading the whole corpus.