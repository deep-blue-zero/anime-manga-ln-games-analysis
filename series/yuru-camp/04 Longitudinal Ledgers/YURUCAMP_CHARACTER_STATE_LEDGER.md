---
title: Yuru Camp Character State Ledger
artifact_id: YURUCAMP_CHARACTER_STATE_LEDGER
artifact_type: ledger
series: YURUCAMP
status: active_provisional
source_boundary: Japanese main manga V01-V16 only
operation: V01–V15_RETROSPECTIVE_LEDGER_BACKFILL
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
updated: '2026-10-23'
continuation_operation: V16_SEQUENTIAL_ANALYSIS
---

# Yuru Camp Character State Ledger

V01–V15 records were consolidated retrospectively under [architecture §6.0](../00%20Frameworks/YURUCAMP_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V1.md). V16 records extend the same ledger from the separately recorded complete Japanese-primary prospective reading; this ledger is not a character model. The [reconstruction specification](../00%20Frameworks/YURUCAMP_CHARACTER_RECONSTRUCTION_SPEC.md) governs any later modeling. The [current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md) remains the sole first-read route. The V16 main narrative, earlier-spring special and bonus comedy retain their distinct temporal and narrative modes.

Each E-record in the [locator/revision ledger](YURUCAMP_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md) supplies the exact source object, volume/chapter/raw image locator, canonical reading/checkpoint, observation scope, alternatives, and verification status. Raw numbers in V01–V15 rows are archive image names, **not printed pages**. V16 uses EPUB reading-spine ordinals and exact image members through the current source manifest; these are not old CBZ raw positions or printed pagination. A row's support boundary is the earliest boundary established by its cited evidence, not necessarily the character's first-ever occurrence. V01–V15 rows were consolidated on 2026-10-17; V16 rows were added on 2026-10-23 from the complete primary-source reading. Later audit knowledge is never attributed to an earlier reader.

`PRIMARY_VERIFIED` certifies only the stated underlying observations, not a universal behavioral rule, readiness grade, or independent held-out validation. `ANALYSIS_EXTRACTED` means the canonical analysis was checked but its source observation was not independently reinspected for that record. A mixed row remains `ANALYSIS_EXTRACTED`; verified components remain individually retrievable. DE = direct observation; RP = recurrent pattern; IN = inference; TH = theme; CA = counterevidence. Confidence concerns the stated bounded proposition, and is separate from verification.

## Temporally indexed state records

| ID | Subject | Support boundary | Observed state / bounded inference | Confidence, counterevidence and exclusions | Evidence | Verification |
| --- | --- | --- | --- | --- | --- | --- |
| CS01 | YC-RIN | V01 | Solitude/group reluctance coexists with practical help and repair of awkward contact. | DE/CA; high for scenes; do not reconstruct a hostile recluse or automatic joiner. | E01-01, E01-02 | PRIMARY_VERIFIED |
| CS02 | YC-NADESHIKO | V01 | Camping novice with food initiative; offers a way to join without requiring Rin to change preference. | DE/IN; moderate for tendency; novice does not mean generally helpless. | E01-02, E01-03 | PRIMARY_VERIFIED |
| CS03 | YC-ENA | V02 | Can mediate gently while leaving Rin to act; already knows Rin well enough to prompt the gift. | DE; high; no global authority to speak for Rin. | E02-02 | PRIMARY_VERIFIED |
| CS04 | YC-RIN | V02 | Initiates a shared food-camping plan herself. | DE/CA; high; change is available initiative, not loss of solitude. | E02-02 | PRIMARY_VERIFIED |
| CS05 | YC-CHIAKI | V03 | Organizer under material limits; can supply useful route information despite not being the solo traveler. | DE/RP; moderate; distinguish remembered family knowledge from field mastery. | E03-01, E03-03 | ANALYSIS_EXTRACTED |
| CS06 | YC-AOI | V03 | Thin early baseline; group participation and conversational calibration are supportable. | RP/IN; moderate/limited; no cycling expertise or independent arc can be imported. | E03-03 | ANALYSIS_EXTRACTED |
| CS07 | YC-RIN | V03 | Fallible traveler who refuses, then considers a group invitation after Ena’s reframing. | DE; high; at this boundary she has not yet enacted Christmas attendance. | E03-01, E03-02 | PRIMARY_VERIFIED |
| CS08 | YC-AOI | V04 | Cooking/practical contribution becomes more legible in the Christmas configuration. | DE/RP; moderate; domain-specific evidence. | E04-01 | ANALYSIS_EXTRACTED |
| CS09 | YC-RIN / YC-NADESHIKO | V04 | Comfortable ordinary thanks, teasing, shared quiet and future plans; Rin also prompts Nadeshiko’s morning task. | DE/IN; high observations, moderate familiarity interpretation; no romance inference. | E04-02 | PRIMARY_VERIFIED |
| CS10 | YC-RIN | V05 | Can name the loneliness of solo camping as part of its pleasure after enjoying group camping. | DE/CA; high; does not choose a single permanently superior mode. | E05-02 | PRIMARY_VERIFIED |
| CS11 | YC-AYANO | V05 | Nadeshiko’s established friend; expresses curiosity and a future moped visit. | DE; moderate; no completed camping competence at this boundary. | E05-02, E05-03 | ANALYSIS_EXTRACTED |
| CS12 | YC-CHIAKI / YC-AOI / YC-ENA | V06 | Underprepared for Yamanaka cold; recognize failure and accept rescue. | DE/CA; high; collective correction cannot be credited wholly to one student. | E06-01, E06-02 | PRIMARY_VERIFIED |
| CS13 | YC-NADESHIKO | V06 | Solo camping becomes an expressed prospective interest. | DE; high; not yet a completed solo trip. | E06-01 | PRIMARY_VERIFIED |
| CS14 | YC-NADESHIKO | V07 | Completes a socially porous first solo trip; mixed cooking outcome; wants solo/group alternation. | DE/CA; high; do not equate solo practice with social withdrawal. | E07-01, E07-02 | PRIMARY_VERIFIED |
| CS15 | YC-RIN / YC-SAKURA | V07 | Care includes checking without taking over; concealment is a real counterexample to perfectly transparent autonomy. | DE→IN; moderate; do not turn care into either pure control or pure consent. | E07-02 | PRIMARY_VERIFIED |
| CS16 | YC-RIN | V08 | Riding itself matters, supported by distinct family contributions. | RP/IN; moderate; support is not evidence that family chooses her goals. | E08-01 | ANALYSIS_EXTRACTED |
| CS17 | YC-AKARI | V08 | Aoi’s younger sister joins travel; not Nadeshiko’s sister (ER-002). | DE; high sibling attribution; no reconstruction readiness. | E08-02 | PRIMARY_VERIFIED |
| CS18 | YC-ENA | V09 | Future driving aspiration is visible. | DE; moderate; cannot grant a license, car or driving skill before acquisition. | E09-01 | ANALYSIS_EXTRACTED |
| CS19 | YC-RIN | V09 | Return-state includes companionship memories, solitude, fatigue and relief near home; recognizes reciprocal worry. | DE/CA; high; mood has several explicit causes. | E09-02, E09-03 | PRIMARY_VERIFIED |
| CS20 | YC-TOBA | V10 | Specific fuel-stove knowledge and limiting instructions are available. | DE; high; alcohol comedy elsewhere does not erase or universalize this competence. | E10-02 | PRIMARY_VERIFIED |
| CS21 | YC-CHIAKI | V10 | Experimentation and organization remain compatible with error and complacency. | DE/CA; moderate; distinguish a safe food failure from severe exposure risk. | E10-03, E10-04 | ANALYSIS_EXTRACTED |
| CS22 | YC-AYANO | V11 | Motor travel/social competence coexists with novice camping; selects used compact gear and erects her own tent. | DE/CA; mixed-source moderate; motorcycle experience is not camping mastery. | E11-01, E11-02 | ANALYSIS_EXTRACTED |
| CS23 | YC-NADESHIKO | V11 | Can travel a separate module and actively learn culinary presentation while sustaining shared plans. | DE/RP; moderate; independence is contextual, not severed connection. | E11-02, E11-03 | ANALYSIS_EXTRACTED |
| CS24 | YC-CHIAKI / YC-AOI / YC-ENA | V12 | Independent outing and narrated recall consolidate a configuration without Rin/Nadeshiko present. | DE/RP; moderate; comic retelling is not a literal recording. | E12-02 | ANALYSIS_EXTRACTED |
| CS25 | YC-NADESHIKO / YC-AOI / YC-CHIAKI | V12 | Imagined juniors/material continuity coexist with doubt about recruitment and comic overreach. | DE/CA; high; no actual successor or promotion is established. | E12-03 | PRIMARY_VERIFIED |
| CS26 | YC-ENA / YC-RIN | V12 | Invented origin stories show playful coordination; they do not reveal true biographies. | DE/CA; high; abstain on the actual full origin beyond explicit non-retracted information. | E12-04 | PRIMARY_VERIFIED |
| CS27 | YC-CHIAKI | V13 | First solo camping adds experience to an organizer previously modeled mainly in groups. | DE; moderate; one attempt does not make solo her dominant preference. | E13-03 | ANALYSIS_EXTRACTED |
| CS28 | YC-EMA | V13 | Art/contact evidence introduces a distinct peripheral subject. | DE; moderate; quietness is not diagnosis, membership or future motive. | E13-03 | ANALYSIS_EXTRACTED |
| CS29 | YC-AOI | V13 | Actual novice road cyclist with enthusiasm, fear, extension of route, puncture and family recovery. | DE/CA; high; canonical V13 V1.2 governs; do not misassign this to Nadeshiko. | E13-04 | PRIMARY_VERIFIED |
| CS30 | YC-CHIAKI | V13 | Offers useful material improvisation and shares quiet with Aoi. | DE; high; brake-holding aid is not repair expertise. | E13-04 | PRIMARY_VERIFIED |
| CS31 | YC-AOI | V14 | Learns specific puncture work, recognizes compatibility limits internally and arranges teacher pickup for a junior. | DE/CA; high; newly available capacity, bounded uncertainty. | E14-01 | PRIMARY_VERIFIED |
| CS32 | YC-MEI | V14 | Joins by choice, brings cycling interest and participates in a demanding proposed trip. | DE; high; novice needs and future execution remain distinct. | E14-03, E14-04 | PRIMARY_VERIFIED |
| CS33 | YC-EMA | V14 | Library/work/food knowledge provides another route into the social network. | DE; moderate; work knowledge does not prove camping experience. | E14-02, E14-05 | ANALYSIS_EXTRACTED |
| CS34 | YC-AOI / YC-MEI | V15 | Near-peer riding and open retreat options; Aoi explicitly remains a recent beginner. | DE/CA; high; REVISE expert-mentor shorthand to competent beginner/co-learner. | E15-01, E15-02 | PRIMARY_VERIFIED |
| CS35 | YC-CHIAKI | V15 | Promotion application is being written. | DE; high; formal approval remains unestablished. | E15-04 | PRIMARY_VERIFIED |
| CS36 | YC-RIN | V15 | Can answer Ema conditionally about camping; this newly attributed evidence belongs to Rin (ER-001). | DE; high observation, moderate tendency; no promise Ema will enjoy it. | E15-05 | PRIMARY_VERIFIED |
| CS37 | YC-ENA | V15 | Supplies the dog/home invitation; does not give the camping advice in this scene. | DE/CA; high; remove that specific support from Ena’s model, preserve earlier independent evidence. | E15-05 | PRIMARY_VERIFIED |
| CS38 | YC-EMA | V15 | Curious about camping, engaged in illustration/dog conversation, still not shown as club member or camper. | DE/CA; high for scene; abstain about eventual joining or motivation. | E15-05 | PRIMARY_VERIFIED |
| CS39 | YC-NADESHIKO | V15 | Schedule frustration leads to a solo-camping idea. | DE; high; ordinary preference flexibility, not an executed next-volume event. | E15-06 | PRIMARY_VERIFIED |
| CS40 | YC-RIN | V16 main narrative | Requests a practical shorter haircut despite familiar teasing; unexpected bookshop closure changes her work plans, and she actively asks to join Ayano's proposed touring. | DE; high for acts, moderate for broader initiative pattern; plans and recalled travel photographs are not completed Golden Week travel or abandonment of solitude. | E16-01, E16-02 | PRIMARY_VERIFIED |
| CS41 | YC-NADESHIKO | V16 main narrative | Elaborate Gunma itinerary and specific Abt interest coexist with unworkable planned connections and an overlooked museum camping event; she accepts revision/help and distinguishes liking trains from broad technical expertise. | DE/CA; high; enthusiasm and domain-specific knowledge do not establish complete route planning. A future museum camp is a wish, not an accomplished overnight. | E16-03, E16-06, E16-09, E16-10 | PRIMARY_VERIFIED |
| CS42 | YC-ENA | V16 main narrative | Chooses to join Nadeshiko's trip, contributes planning alternatives and playful attention, but sleeps through much early travel and relies on Ema's navigation and recorded scenery. | DE/CA; high for episode; temporary early-morning difficulty is not global incapacity, and a hurried proposed itinerary is not an endorsed final plan. | E16-03, E16-04, E16-06, E16-07 | PRIMARY_VERIFIED |
| CS43 | YC-EMA | V16 main narrative | Scenic interest and an accepted invitation become actual shared rail/walking/museum travel. She seeks borrowed light equipment, relays Ibigawa's cold warning and proposes bungalow accommodation that both seniors accept. | DE/IN; high acts, moderate agency interpretation; no prior family camping experience is reported, and the volume ends this thread before campsite arrival or overnight. Club membership remains unestablished. | E16-01, E16-04, E16-05, E16-06 | PRIMARY_VERIFIED |
| CS44 | YC-EMA | V16 main narrative | Finds the completed downhill walk pleasant and an unfamiliar railway domain stimulating; her tablet drawings make Nadeshiko's visual associations shareable, and she participates in photographs and humor. | DE/IN; high observations, moderate repertoire inference; pleasure in these activities is not established camping enjoyment, train expertise or total identity conversion. Private thoughts are not statements received by the seniors. | E16-07, E16-08, E16-09 | PRIMARY_VERIFIED |
| CS45 | YC-AYANO | V16 main narrative | Shares photographs of earlier camping, proposes a May meeting and describes a northward multi-day riding/camping route; receives Rin's direct wish to ride together. | DE; high for exchanged reports and plans; the proposed route has not been completed or independently certified safe by this exchange. | E16-02 | PRIMARY_VERIFIED |
| CS46 | YC-RIN | V16 special; earlier spring | Accepts Nadeshiko's shared-camp invitation, enjoys solitary lakeside wandering before her arrival, contributes ice cream to their dessert, and explicitly imagines a quiet solo-use campsite. | DE/CA; high; earlier-season material, not a post-Golden-Week state transition. Companionship and positive solitude coexist; hypothetical campsite features and conditional next-year interest are not completed projects. | E16-11, E16-13, E16-14 | PRIMARY_VERIFIED |
| CS47 | YC-NADESHIKO | V16 special; earlier spring | A missed bicycle turn causes extra mountain travel, which she later recognizes as needing more map checks; her stamina and actual dessert preparation coexist with that navigation error. | DE/CA; high; the earlier spring trip is distinct from Gunma. A scenic discovery does not vindicate the missed turn, and one error does not erase cooking or travel capacities. | E16-12, E16-13 | PRIMARY_VERIFIED |
| CS48 | YC-CHIAKI | V16 bonus; chronology not fixed | Hammock experimentation and joking discussion of finding a more distinctive hobby keep initiative, DIY interests and material constraints visible outside the main trip. | DE/CA; high for depicted comedy; the fantasy portal, imagined handlift trip and possible new hobbies are not actual travel, licenses, dog adoption or professional construction competence. Formal club promotion is not established. | E16-15 | PRIMARY_VERIFIED |

## Model-use limits

These records are retrieval foundations, not complete psychologies. No subject has a readiness grade. Self-knowledge, information learned off panel, broad political/moral commitments, romantic orientation, and behavior outside observed domains remain insufficiently evidenced. Supporting subjects have their own identities (YC-SAKURA, YC-AYANO, YC-TOBA, YC-AKARI); do not pool them into a generic caregiver. See the locator ledger’s five checkpoint freezes before choosing a model boundary.
