---
title: "IDOLY PRIDE V2 Analytical Method"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_ANALYTICAL_METHOD"
version: "2.0"
status: "governing framework"
artifact_role: "methodology"
source_cutoff: "to be frozen during Phase 0"
preferred_text_interface: "analysis_bundles"
provenance_interface: "idoly-ingest"
---


# IDOLY PRIDE V2 Analytical Method


## 1. Purpose


This document governs the second-pass, source-grounded analysis of *IDOLY PRIDE* across the game corpus, anime, audiovisual performance material, official visual material, and prior analytical work.


The V2 project is not a cleanup of old prose. It is a reconstruction of the analytical model from the underlying evidence, with the prior corpus treated as a historical hypothesis set rather than an authority. The central objective is to produce a durable body of analysis that can survive context loss, retrieval delay, future source additions, and disagreement among earlier interpretations.


The governing principle is:


> Read broadly first, classify evidence second, synthesize third.


The V2 pass must resist two opposite failures:


1. **Excessive fragmentation:** analyzing isolated events, cards, or conversations without reconstructing longitudinal character and unit development.
2. **Premature synthesis:** deciding what a character, relationship, or theme "means" before auditing the distributed corpus that could complicate or overturn that interpretation.


The project therefore places longitudinal ledgers between source reading and synthesis prose. Those ledgers are the epistemic center of V2.


---


# 2. Corpus model


## 2.1 Source and interface distinction


The project must distinguish the underlying evidence from the interfaces used to read it.


### A. Game-extracted source corpus


The INFO PRIDE-derived corpus is overwhelmingly material extracted directly from the game and normalized into a local archival tree. For the purposes of V2, the Japanese game dialogue should be treated as game-source textual evidence, subject to the exceptions noted below.


### B. `analysis_bundles/` — preferred analytical reading interface


`analysis_bundles` is the default interface for most V2 reading. It reorganizes the extracted game material into forms optimized for literary and character analysis while preserving granular source paths.


Use it for:


- complete character reading;
- chronological character reconstruction;
- category-specific slices;
- main-story and unit-origin context;
- event, card, bond, and message reading;
- relationship reconnaissance;
- character speech and register analysis;
- discovering repeated motifs or contradictions across many sources.


The presence of a passage in an analytical bundle does not make the bundle itself the original narrative unit. When exact context matters, descend to the provenance layer.


### C. `idoly-ingest/` — provenance and granular retrieval interface


`idoly-ingest` is the lower-level source-preserving interface. It consolidates raw extracted story fragments into bounded bundles while maintaining source story IDs, source paths, speaker metadata, and other provenance information.


Use it for:


- exact scene reconstruction;
- identifying the full event/card/story sequence surrounding a passage;
- verifying context discovered in a character omnibus;
- resolving apparent contradictions caused by bundle reordering;
- building stable source locators;
- checking whether a claim depends on one scene or recurs across multiple independent scenes.


### D. `idoly-ingest-selected-events-core-important/` — historical triage aid


This directory may remain useful as a fast orientation layer, especially for previously identified high-value events. It must not govern V2 source priority.


Its labels reflect an earlier analytical judgment. V2 must be able to promote overlooked sources, demote previously emphasized sources, and identify events whose importance was misunderstood.


Therefore:


> The V2 Corpus Coverage and Priority Ledger supersedes the curated event subset as the authoritative priority map.


### E. Underlying archival extraction


The raw archival corpus remains the terminal textual provenance layer. V2 should not duplicate this source tree inside the analysis-artifact tree. The analysis corpus should record enough source identity to route back to it.


---


# 3. Evidence classes and authority


V2 must separate evidence by what it can actually establish.


## Tier A — governing narrative evidence


- main game story;
- unit-origin stories;
- anime narrative dialogue and audiovisual presentation.


These sources establish the broadest narrative architecture, core histories, foundational relationships, and major turning points.


## Tier B — major character-development evidence


- substantial event stories;
- card stories;
- bond stories;
- major unit or cross-unit side stories.


These often contain characterization as important as the main story, but their function must be evaluated rather than assumed.


## Tier C — social and linguistic evidence


- messages;
- group chats;
- ordinary-life scenes;
- short communications.


These are especially valuable for:


- speech register;
- relational grammar;
- spontaneous care;
- teasing and conflict style;
- who manages group chaos;
- who initiates contact;
- who hides vulnerability;
- how units behave when no major plot crisis is occurring.


They should not automatically be treated as lower-value characterization merely because their narrative stakes are small.


## Tier D — audiovisual and formal evidence


- anime audio;
- anime frames and staging;
- complete song audio;
- lyrics;
- 3DMVs;
- live/performance sequences;
- card illustrations;
- key visuals;
- photographs and other official visual material;
- official 4koma when used as supplementary characterization or paratext.


These sources can establish things transcripts cannot:


- vocal affect;
- hesitation;
- breath and emotional suppression;
- choreography;
- blocking;
- editing;
- gaze;
- spatial relation;
- costume language;
- lighting;
- musical structure;
- arrangement;
- audience positioning;
- visual rhyme.


## Tier E — derived or approximate evidence


The main special case is telephone ASR. Telephone audio is source evidence; machine-generated transcripts are provisional representations of that audio.


Use ASR to discover and roughly understand a call. Do not use unreviewed ASR for quotation-sensitive or subtle linguistic claims without listening to the audio.


Mark such evidence:


`TELEPHONE_ASR_UNVERIFIED`


After listening and correcting wording where necessary:


`TELEPHONE_AUDIO_VERIFIED`


## Tier F — historical analysis


- prior chat analyses;
- prior unit deep dives;
- previous synthesis documents;
- V1 conclusions and comparative writeups.


These are not evidence for what the work says. They are evidence for what the project previously believed.


Use them to:


- recover hypotheses;
- recover overlooked source references;
- identify claims requiring retesting;
- compare V1 and V2 conclusions;
- preserve useful formulations after source revalidation.


They never override Tiers A-E.


---


# 4. Source-priority classifications


Each meaningful source encountered during V2 should receive one or more analytical-priority labels in the Corpus Coverage and Priority Ledger.


## `FOUNDATIONAL`


The source changes or establishes the basic model of a character, unit, relationship, institution, or series-level idea. Removing it would materially distort the synthesis.


## `CORE`


The source is necessary for a mature account but does not by itself redefine the model.


## `IMPORTANT`


The source significantly deepens, qualifies, or tests a major conclusion.


## `TEXTURE`


The source provides social rhythm, voice, comic behavior, ordinary-life evidence, or relational detail without substantially changing the major arc.


## `REDUNDANT`


The source repeats characterization already established more strongly elsewhere. Redundant does not mean worthless; repetition can demonstrate stability. The label means it need not receive extended prose treatment.


## `CONFLICTING`


The source appears to contradict, destabilize, or complicate another source or an existing V2 claim. It must be resolved or explicitly preserved as ambiguity before final synthesis.


## `FORMAL_DEPENDENT`


The transcript alone is insufficient because the interpretation materially depends on audio, visual staging, performance, music, or another formal element.


A source may hold multiple labels, for example `CORE + FORMAL_DEPENDENT`.


Priority is an analytical judgment, not a claim of canonical status.


---


# 5. Epistemic classification of claims


Every major V2 conclusion should be understood as belonging to one of the following classes.


## `TEXTUAL_FACT`


Directly established by the relevant narrative text.


Examples include stated history, explicit motives, declared goals, or directly observable actions.


## `FORMAL_FACT`


Directly observable in audiovisual or visual evidence: a camera composition, performance order, lyric, costume, vocal pause, blocking decision, musical transition, or similar formal property.


## `STRONG_INFERENCE`


Not explicitly stated, but supported by convergent evidence with little plausible competing explanation.


## `INTERPRETATION`


A defensible explanatory model that organizes evidence but is not uniquely compelled by it.


## `OPEN_HYPOTHESIS`


A plausible idea worth preserving for later testing, but insufficiently stabilized for canonical synthesis.


## `UNRESOLVED_CONFLICT`


Evidence remains genuinely inconsistent, chronologically ambiguous, or insufficient to support a responsible resolution.


The project must not hide interpretive status merely because a formulation is rhetorically elegant.


---


# 6. Chronology policy


*IDOLY PRIDE* is a live-service transmedia work whose publication order, inferred in-universe chronology, and character-development chronology may not fully coincide.


V2 must track at least three timelines:


1. **Release/publication order** — when content entered the franchise.
2. **Narrative/in-universe order** — when events appear to occur within the story world.
3. **Character-development order** — the sequence in which evidence meaningfully changes the reader's model of a character.


The corpus's generated chronological keys are archival ordering aids. They are not automatic claims about exact in-universe chronology.


When chronology is uncertain:


- preserve the uncertainty;
- identify the basis for the proposed placement;
- do not manufacture exact dates;
- avoid using uncertain chronology to prove psychological causation.


Later material may clarify earlier ambiguity, but V2 should preserve what was knowable at the earlier narrative boundary when that distinction matters.


---


# 7. Phase structure


## Phase 0 — Corpus audit and source lock


Before interpretive drafting:


- inventory the accessible game-extracted corpus;
- record the `analysis_bundles` and `idoly-ingest` snapshots used;
- inventory anime bundles and other audiovisual materials;
- inventory 4koma and visual assets;
- record known missing assets;
- record telephone audio/transcript status;
- establish the V2 source cutoff;
- freeze naming conventions and character-code mappings;
- record the standing Makino continuity assumption used by this project;
- create a source manifest and source-class policy.


The source lock does not imply that the live-service franchise has ended. It means V2.0 analyzes a defined snapshot. Later material should produce an explicit update release rather than silently changing the corpus.


## Phase 1 — Corpus Coverage and Priority Ledger


Audit the distributed game corpus broadly enough that source priority is determined by V2 rather than inherited from V1.


For each source, record where practical:


- stable source ID;
- source type;
- title;
- release/order information;
- characters;
- units;
- major relationship axes;
- themes or institutions implicated;
- narrative function;
- V2 priority;
- priority rationale;
- V1 relevance;
- whether it is new to V2;
- whether it complicates a prior claim;
- whether audiovisual review is required;
- source path / bundle locator.


The purpose is not to summarize every source in detail. It is to know what exists and why it matters.


## Phase 2 — Longitudinal ledgers


Construct evidence-bearing working ledgers before final character or unit prose.


Required ledger families:


- character longitudinal ledgers;
- unit-development ledgers;
- relationship ledgers;
- theme/motif ledgers;
- institution/labor ledgers;
- Mana/inheritance ledger;
- manager/production ledger;
- performance and audiovisual ledger as material becomes available.


## Phase 3 — Unit and character syntheses


Write the mature unit/character documents only after the relevant ledgers have stabilized.


The unit documents are a normalization layer between raw evidence and series-level thematic synthesis. They should establish the most complete model of each unit and its members without forcing all cross-unit or series-wide themes into the same document.


## Phase 4 — Relationship and thematic syntheses


Only after character/unit models stabilize, synthesize cross-cutting structures such as:


- intimacy, dependence, rivalry, and care;
- grief, death, memory, and inheritance;
- idolhood and audience recognition;
- professional labor and industry;
- production, autonomy, and managerial ethics;
- ordinary-life social texture.


This prevents thematic claims from turning characters into examples of a thesis selected in advance.


## Phase 5 — Audiovisual, music, and performance audit


Perform dedicated formal analysis rather than treating audiovisual material as illustrations for conclusions already reached from transcripts.


This phase includes:


- full-series anime formal audit;
- targeted song and 3DMV analysis;
- major live/performance sequence review;
- voice/register listening where useful;
- telephone audio verification for high-value calls;
- visual design/card-art/4koma audit.


Formal findings may revise earlier textual syntheses.


## Phase 6 — Series architecture and chronology synthesis


After unit, relationship, thematic, and formal layers stabilize, write the series-architecture document.


This phase should answer:


- how the project changes across anime and game eras;
- how Mana's absence structures later narrative possibility;
- how Hoshimi, rivals, external units, and global/commercial arcs change the scale of the work;
- how publication chronology and developmental chronology interact;
- which early premises are preserved, revised, or outgrown.


Series architecture is intentionally late. Writing it too early encourages the rest of the project to conform to a premature master thesis.


## Phase 7 — Evidence locator and claim-routing audit


Create the traceability system that allows important synthesis claims to route backward.


Preferred chain:


> full-series claim -> specialist synthesis -> longitudinal ledger -> analysis bundle -> granular ingest/source story -> original extracted game asset or audiovisual evidence


Not every sentence requires a unique ledger entry, but every major or contestable claim should have a recoverable evidentiary path.


## Phase 8 — Continuous full-series synthesis


Write the final literary synthesis as a sustained argument about the work, not as a document-by-document recap.


It should be readable independently while remaining traceable to specialist documents.


## Phase 9 — Final audit and immutable release


Before freezing V2.0:


- duplication audit;
- source coverage audit;
- unresolved-conflict audit;
- citation/locator audit;
- terminology consistency audit;
- character-name/code audit;
- chronology caveat audit;
- missing-source disclosure;
- file manifest;
- checksums when packaging;
- immutable release copy.


Future corrections should become V2.1 or a later version rather than silently mutating V2.0.


---


# 8. Character longitudinal ledger schema


Each major character should be reconstructed using the same conceptual dimensions while allowing character-specific additions.


Recommended fields:


## Identity and initial state


- role at first meaningful appearance;
- unit/institutional position;
- public image;
- self-image;
- known history at that boundary.


## Core motivational architecture


- core desire;
- core fear or wound;
- immediate goal;
- long-term aspiration;
- what the character believes success would prove.


## Defensive structure


- default coping strategy;
- avoidance pattern;
- control strategy;
- pride/shame dynamic;
- how the character reacts to failure, pity, dependence, or uncertainty.


## Public and private personae


- professional persona;
- private persona;
- difference between stage, work, domestic, friend, rival, and manager-facing selves;
- conditions under which the persona collapses or softens.


## Idol philosophy


- what an idol is for;
- what audiences mean;
- what winning means;
- what failure means;
- attitude toward talent, training, image, fame, professionalism, artistry, money, or service.


## Relational architecture


- unit role;
- closest attachments;
- rivals;
- seniors/juniors;
- manager relationship;
- dependency patterns;
- care style;
- conflict style;
- boundaries;
- jealousy or possessiveness where supported;
- forms of intimacy the character can and cannot verbalize.


## Voice and language


- pronouns and self-reference;
- address terms;
- politeness level;
- sentence-final patterns;
- recurring lexical fields;
- teasing style;
- apology style;
- command/request style;
- text-message voice versus spoken voice;
- register changes by relationship.


## Formal and bodily identity


- vocal performance traits;
- costume/stage identity;
- recurring visual motifs;
- body, illness, fatigue, athleticism, food, touch, or other embodied motifs where relevant.


## Turning points


For each turning point record:


- prior state;
- trigger;
- immediate response;
- behavioral change;
- later confirmation or reversal;
- key sources.


## Contradictory evidence


Record evidence that resists the current model rather than smoothing it away.


## Mature state


Describe what has genuinely changed, what remains stable, and what only appears resolved.


## Open questions


Preserve uncertainties for later source additions or comparative work.


---


# 9. Relationship ledger schema


Relationships should not be reconstructed only by merging two individual character profiles.


For each major relationship track:


- first meaningful configuration;
- asymmetries of status, knowledge, age, talent, fame, or institutional power;
- forms of address;
- who initiates contact;
- who pursues and who withdraws;
- conflict grammar;
- repair grammar;
- care behaviors;
- dependence and independence;
- rivalry and admiration;
- jealousy/possessiveness where evidenced;
- touch, gifts, food, work, teasing, silence, and other recurring relational media;
- public versus private relationship;
- major turning points;
- relationship-specific speech changes;
- evidence against an overly simple interpretation;
- mature relationship state;
- unresolved ambiguity.


For romantic or yuri-coded interpretations, distinguish:


1. explicit textual romance;
2. romantic coding;
3. exceptional intimacy compatible with multiple readings;
4. fandom-driven speculation unsupported by the source.


Do not collapse these categories.


---


# 10. Unit ledger schema


Each major unit should be treated as a collective character with internal structure.


Track:


- founding conditions;
- explicit and implicit unit purpose;
- center/leadership model;
- division of emotional and professional labor;
- member-specific functions;
- internal conflicts;
- shared vocabulary and rituals;
- competitive philosophy;
- audience philosophy;
- sound/performance identity;
- visual identity;
- relationship to Mana's legacy;
- relationship to Hoshimi or industry institutions;
- external rivals;
- key defeats and victories;
- changes in cohesion;
- ordinary-life unit culture;
- mature collective identity.


Do not assume a unit's promotional concept is identical to its narrative identity.


---


# 11. Theme and institution ledger schema


Themes should be built bottom-up from recurring evidence.


A thematic ledger entry should contain:


- concept or motif;
- source;
- character/unit;
- local narrative function;
- recurrence status;
- counterexample;
- whether the pattern is textual, formal, or interpretive;
- relationship to existing V2 thesis;
- confidence.


Institutional ledgers should track:


- agency management;
- labor expectations;
- training;
- money and material survival;
- branding;
- fan relations;
- career longevity;
- contracts/business decisions when depicted;
- competition systems;
- domestic and overseas work;
- professional adulthood;
- public image;
- how institutional pressure interacts with individual agency.


---


# 12. Japanese-language method


Japanese dialogue is not merely a container for plot information. It is characterization.


V2 should systematically attend to:


- personal pronouns and their absence;
- self-reference by name;
- surname/given-name/nickname choice;
- honorifics;
- politeness level;
- gendered or stylized sentence endings;
- ojou-sama language;
- roughness or softness;
- dialect or marked vocabulary;
- professional versus private speech;
- abruptness, hedging, ellipsis, repetition, and unfinished syntax;
- message punctuation and emoji/stamp behavior where relevant;
- changes in how one character speaks to another over time.


Lexical observations should be tied to function. A sentence ending is analytically useful because of what it does in the character's relational grammar, not merely because it is identifiable.


When quoting Japanese:


- preserve wording accurately;
- provide translation when the Japanese is important to the argument;
- distinguish literal semantic content from pragmatic effect;
- verify telephone wording against audio before relying on fine linguistic nuance.


---


# 13. Audiovisual and performance method


Transcripts cannot establish audiovisual form.


For anime and performance material, analyze at least the following channels independently before integrating them:


## Dialogue/audio


- timing;
- pause;
- emphasis;
- breath;
- laughter;
- crying;
- vocal strain;
- emotional suppression;
- relationship-specific tone;
- performance delivery.


## Image and mise-en-scene


- framing;
- camera distance;
- gaze;
- isolation/pairing;
- blocking;
- foreground/background hierarchy;
- recurring spatial arrangements;
- visual rhyme;
- costume;
- lighting;
- stage/audience relation.


## Editing


- cuts and transitions;
- temporal compression;
- montage;
- image/song synchronization;
- reaction-shot structure;
- withheld visual information.


## Music


- melodic profile;
- harmonic tension and release;
- instrumentation;
- rhythm and tempo;
- arrangement density;
- vocal distribution;
- lyrical perspective;
- relationship between song structure and dramatic structure.


Contact sheets are reconnaissance tools, not sufficient final evidence for fine visual claims. When a contact sheet identifies an important shot, inspect the individual frame or sequence.


---


# 14. Treatment of ordinary-life material


V2 must not equate low plot stakes with low analytical value.


Messages, chats, light cards, food scenes, jokes, shopping, dorm behavior, and casual interactions can reveal:


- default social hierarchy;
- who mediates conflict;
- who remembers practical needs;
- who initiates affection indirectly;
- how embarrassment works;
- which relationships survive outside crisis;
- whether a unit has become genuinely comfortable;
- how professional personae relax in private.


However, ordinary-life evidence should not be inflated into dramatic turning points when it merely confirms a stable pattern.


---


# 15. Adversarial reading and contradiction protocol


Before any major V2 thesis becomes canonical, ask:


1. What evidence argues against it?
2. Is the pattern longitudinal or event-specific?
3. Is a recurring joke being mistaken for deep psychology?
4. Is later characterization being projected backward?
5. Is a single writer/event tonally anomalous?
6. Does another source class materially complicate the claim?
7. Does the audiovisual presentation alter what the transcript seems to imply?
8. Is absence of evidence being treated as evidence of absence?
9. Is promotional framing being confused with narrative framing?
10. Is V1 familiarity causing selective attention?


If conflicting evidence cannot responsibly be reconciled, preserve the conflict.


A mature synthesis is allowed to say that a character is inconsistent, that chronology is unclear, or that two interpretive models remain viable.


---


# 16. V1 revision protocol


Prior analysis is valuable precisely because it can be tested.


For each important inherited V1 claim, V2 should eventually classify it as one of:


- `CONFIRMED` — substantially survives source re-audit;
- `STRENGTHENED` — correct but now supported more broadly or precisely;
- `REFINED` — core insight survives but wording or causal model changes;
- `NARROWED` — claim was too broad;
- `WEAKENED` — some evidence remains but confidence drops;
- `OVERTURNED` — contradicted by stronger evidence;
- `UNRESOLVED` — cannot yet be responsibly adjudicated;
- `NEW_V2` — important conclusion not materially present in V1.


The revision ledger should preserve particularly useful V1 formulations when they survive, but never protect them from correction.


---


# 17. Source locators and claim routing


Every source-facing ledger entry should use stable identifiers wherever possible.


Recommended game locator fields:


- analysis-bundle file;
- bundle or scene heading;
- source story ID;
- granular source path;
- relevant character code(s);
- event/card/message identifier;
- asset identifier when formal evidence is implicated.


Recommended audiovisual locator fields:


- medium;
- episode/song/3DMV/performance identifier;
- timestamp or scene index;
- frame/contact-sheet locator where available;
- subtitle/audio file identity;
- verification status.


The desired provenance chain is:


> synthesis claim -> specialist document -> ledger entry -> source bundle -> granular source ID/path -> original game-extracted or audiovisual evidence


The chain should be recoverable without requiring the original chat transcript.


---


# 18. Duplication policy


V2 is multi-document by design, but it should not become multi-document repetition.


Use the following ownership rules:


- **Unit/character documents** own longitudinal character models and internal unit structure.
- **Relationship document** owns cross-unit relational forms and relationship comparisons.
- **Grief/memory document** owns series-wide death, memorialization, survival, and inheritance arguments.
- **Labor/industry document** owns institutional and professional structures.
- **Idolhood/audience document** owns competing definitions of idolhood, fandom, recognition, and performance purpose.
- **Manager/production document** owns Makino's professional/ethical role and the problem of guidance versus autonomy.
- **Voice/register document** owns systematic linguistic comparison.
- **Formal document(s)** own audiovisual and visual arguments.
- **Series architecture document** owns chronology and structural progression.
- **Full-series synthesis** integrates conclusions but should point conceptually back to specialist ownership rather than re-proving every claim.


A short recap is acceptable when needed for readability. Rewriting the same full argument in multiple documents is not.


---


# 19. Quality gates for major synthesis documents


A major document should not be considered stable until it passes the following gates.


## Source breadth gate


The relevant main story, origin material, major events, cards/bonds, and ordinary-life evidence have been sampled or audited sufficiently to avoid obvious selection bias.


## Longitudinal gate


The document distinguishes early, transitional, and mature states rather than flattening the character/unit across time.


## Counterevidence gate


Major claims have been tested against contradictory or inconvenient evidence.


## Source-class gate


Textual claims and formal claims are not conflated.


## Language gate


Important Japanese-language claims are based on actual wording, with ASR caveats where necessary.


## Duplication gate


The document owns a clear analytical function and does not substantially duplicate neighboring documents.


## Traceability gate


Its most important claims can route backward to ledger/source evidence.


## Uncertainty gate


Ambiguity is disclosed rather than silently resolved.


---


# 20. Full-series interpretive posture


V2 should remain open to the possibility that the prior project's strongest broad thesis survives, but it must not assume it.


Particularly important hypotheses to test include:


- Mana as an originating absence whose death creates the later idol ecosystem;
- the difference between inheriting Mana and imitating her;
- Makino's movement from grief-bound witness to producer of new possibilities;
- Sunny Peace and Tsuki no Tempest as divergent answers to what follows Mana;
- LizNoir as adult/professional counterpoint;
- IIIX as a later expansion of idolhood into damaged adulthood, global ambition, hostile intimacy, and self-authorship;
- rivalry as a form of recognition rather than mere antagonism;
- performance as proof, memory transmission, self-authorship, or social connection depending on the character;
- the work's increasing concern with labor, money, career, image, and institutional survival.


These are V2 research questions until the audit confirms them.


---


# 21. Completion standard


The V2 analytical method succeeds when the project no longer depends on conversational memory to answer basic questions such as:


- Why do we believe this about a character?
- Which source changed the interpretation?
- Is the claim textual or interpretive?
- What evidence argues against it?
- Where in the extracted corpus can the source be found?
- Did the conclusion exist in V1 or emerge in V2?
- Does the claim require audiovisual verification?
- What source cutoff does the conclusion assume?


The final corpus should make those questions answerable through artifacts.


The methodological ideal is:


> broad corpus awareness -> explicit source priority -> longitudinal evidence -> adversarial interpretation -> specialist synthesis -> claim routing -> continuous full-series argument -> immutable release.


That sequence, rather than any single thematic thesis, is the governing logic of the IDOLY PRIDE V2 project.