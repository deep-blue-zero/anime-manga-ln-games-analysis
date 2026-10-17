---
title: Yuru Camp Primary Source Locator and Claim Revision Ledger
artifact_id: YURUCAMP_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
series: YURUCAMP
status: active_provisional
source_boundary: Japanese main manga V01-V15 only
operation: V01–V15_RETROSPECTIVE_LEDGER_BACKFILL
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
---

# Yuru Camp Primary Source Locator and Claim Revision Ledger

Retrospective evidence consolidation under [architecture §6.0](../00%20Frameworks/YURUCAMP_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V1.md), not a new prospective reading or a character model. The [reconstruction specification](../00%20Frameworks/YURUCAMP_CHARACTER_RECONSTRUCTION_SPEC.md) governs any later modeling. The [current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md) remains the sole first-read route. No V16 evidence is used.

Each E-record in the [locator/revision ledger](YURUCAMP_PRIMARY_SOURCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md) supplies the exact source object, volume/chapter/raw image locator, canonical reading/checkpoint, observation scope, alternatives, and verification status. Raw numbers are archive image names, **not printed pages**. A row's support boundary is the earliest boundary established by its cited evidence, not necessarily the character's first-ever occurrence. All rows were consolidated on 2026-10-17; later audit knowledge is never attributed to an earlier reader.

`PRIMARY_VERIFIED` certifies only the stated underlying observations, not a universal behavioral rule, readiness grade, or independent held-out validation. `ANALYSIS_EXTRACTED` means the canonical analysis was checked but its source observation was not independently reinspected for that record. A mixed row remains `ANALYSIS_EXTRACTED`; verified components remain individually retrievable. DE = direct observation; RP = recurrent pattern; IN = inference; TH = theme; CA = counterevidence. Confidence concerns the stated bounded proposition, and is separate from verification.

## Provenance contract and scope

Evidence universe: fifteen accepted Japanese-manga readings and five completed three-volume checkpoints at base `cfddecb9b5b05ce7b5b25060673ed2e77639da6c`. V13 is the corrected V1.2. The [preservation manifest](../09%20Audits%20and%20Reviews/YURUCAMP_FROZEN_ARTIFACT_PRESERVATION.json) fixes the exact historical bytes; the [repair audit](../09%20Audits%20and%20Reviews/YURUCAMP_CONTINUATION_REPAIR_AUDIT.md) records errata.

Candidate extraction used each reading’s scene/locator, character, relationship, competence, voice, claim-delta and carry-forward sections, followed by its checkpoint’s corresponding freezes and transitions. Every observation below names its earliest cited volume and the checkpoint that tests that tranche. The chapter/image locator is the primary scene-level join; the canonical document pair is the secondary analytical join. Broad extracted ranges deliberately advertise that the underlying observation has not been newly isolated and verified. No hindsight-generated quotation is admitted.

All V01–V15 archive SHA-256 values below were independently recomputed from the live Drive objects and match Phase 0. Image names have four digits and `.jpg`; use the exact archive member with that basename. A raw image is not automatically a printed page, a story page, or one side of a spread. Source decoding success is distinct from literary verification.

## Source identity and canonical analysis routes

| Volume | Drive object ID | Verified archive SHA-256 |
| --- | --- | --- |
| V01 | 1RH-UyG9AQPv_qJXAU6S7TUfO45SJD08j | decc38731d708147c1bc04916876ef0aa94e862859d5e5e43991260677efb11c |
| V02 | 14S_RhAL3MVzfKC5E-ixS5WnGTcEgI_e4 | c49747fea5326cc9e18f5b682f0989e1858a1f0efbf56817af4ccb1e505d8fe9 |
| V03 | 1MjTeALcesLykNlFX4x_a_tcAwbwFIYNV | 246c28ce24844cbefa37e2e3ced82494703a262f89a6e707d366c9d0026d2967 |
| V04 | 12KI6uaPFmFveYK4nQcYZ4WJWyGsMIrpE | f2c1a70d276d2243828dc7b5d8401f16471a578e507f32259d9e2de0c03dca3c |
| V05 | 12SENoLFSwXVQ_bXu5kvPK7BcX5HHHUlY | b63502cfa371059182e387b0b8886866b0eac9951f08010405a1ce4432c99e59 |
| V06 | 1BY-q6dl8NCKcchfcWu1hA5sLXr-24Fp5 | ecbf52418229e3ea710c3fc4a12c8ea3506879414c0f77e12cc0939f345892c2 |
| V07 | 1BklEAicC0YiiIHDgxU3eQVhL3RMIKnCZ | 81ebb21630205536d3db86ae4f67aa739dd8835f9ead59bc182ba4b78f1ea6c6 |
| V08 | 15btenYpQpad_B88EzR_Nk_zOSvsP9L4- | 7be122c49a2d95ccb3255139ad8fdd1d57dd0d1e9d5caaee4991a157bcf03d38 |
| V09 | 1oA_PCOi0QduPCkjy8w15KPgj1PDlimfG | e9017f5626fc64725d090f885fdd6f2cd26031b3bdccaae4b936d611c4d4fc3c |
| V10 | 1_BgrndXjlhQOHGnZtBs_XC5cYt2Ybouh | b9d2d5e2a04240808dc6dd3c4e9245b3cdbaefe3aad5172eca02d173fef95c19 |
| V11 | 14lOx-vMWZhiBfTw1b01av2zDcmNj5H3s | 729c013dd93006b0400618245fc0ce2c5e19c8eeaaa7b6661d5460d887912187 |
| V12 | 16hiGhy-yTlWzHYI0ENGFhXOmphexmuui | e9f6c074dd6309314dfe1d315e1371983ca82bec78337017c0bf29491481cf61 |
| V13 | 1nKg7jQgphHLmVA_PyIAHqYL4UKqQiuYz | 0cc621edc83ccf18ec6b0efa4bfbc2754de4613e6a4c0a6b2e6a2969b6a2e941 |
| V14 | 1u4mZ1SXozZfCFmMMQo3C1iYG9WtHgECJ | 935b42462214b1b599e1aa77a9b239f93a30dd5ae422c8db6f88e246bb4e1ce7 |
| V15 | 1KFvd5mfGEI9_MVfu-_KTwQJLZ00unJy2 | ca425887506860398242d09cc9eb21ddde3dec60fa9dd4db55bdc40dee9860cd |

| Volume | Canonical reading | Adversarial checkpoint |
| --- | --- | --- |
| V01 | [V01 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V01_DEEP_READING.md) | [CP03](../03%20Volume%20Deep%20Readings/YURUCAMP_V01-V03_CHECKPOINT.md) |
| V02 | [V02 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V02_DEEP_READING.md) | [CP03](../03%20Volume%20Deep%20Readings/YURUCAMP_V01-V03_CHECKPOINT.md) |
| V03 | [V03 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V03_DEEP_READING.md) | [CP03](../03%20Volume%20Deep%20Readings/YURUCAMP_V01-V03_CHECKPOINT.md) |
| V04 | [V04 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V04_DEEP_READING.md) | [CP06](../03%20Volume%20Deep%20Readings/YURUCAMP_V04-V06_CHECKPOINT.md) |
| V05 | [V05 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V05_DEEP_READING.md) | [CP06](../03%20Volume%20Deep%20Readings/YURUCAMP_V04-V06_CHECKPOINT.md) |
| V06 | [V06 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V06_DEEP_READING.md) | [CP06](../03%20Volume%20Deep%20Readings/YURUCAMP_V04-V06_CHECKPOINT.md) |
| V07 | [V07 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V07_DEEP_READING.md) | [CP09](../03%20Volume%20Deep%20Readings/YURUCAMP_V07-V09_CHECKPOINT.md) |
| V08 | [V08 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V08_DEEP_READING.md) | [CP09](../03%20Volume%20Deep%20Readings/YURUCAMP_V07-V09_CHECKPOINT.md) |
| V09 | [V09 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V09_DEEP_READING.md) | [CP09](../03%20Volume%20Deep%20Readings/YURUCAMP_V07-V09_CHECKPOINT.md) |
| V10 | [V10 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V10_DEEP_READING.md) | [CP12](../03%20Volume%20Deep%20Readings/YURUCAMP_V10-V12_CHECKPOINT.md) |
| V11 | [V11 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V11_DEEP_READING.md) | [CP12](../03%20Volume%20Deep%20Readings/YURUCAMP_V10-V12_CHECKPOINT.md) |
| V12 | [V12 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V12_DEEP_READING.md) | [CP12](../03%20Volume%20Deep%20Readings/YURUCAMP_V10-V12_CHECKPOINT.md) |
| V13 | [V13 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V13_DEEP_READING.md) | [CP15](../03%20Volume%20Deep%20Readings/YURUCAMP_V13-V15_CHECKPOINT.md) |
| V14 | [V14 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V14_DEEP_READING.md) | [CP15](../03%20Volume%20Deep%20Readings/YURUCAMP_V13-V15_CHECKPOINT.md) |
| V15 | [V15 reading](../03%20Volume%20Deep%20Readings/YURUCAMP_V15_DEEP_READING.md) | [CP15](../03%20Volume%20Deep%20Readings/YURUCAMP_V13-V15_CHECKPOINT.md) |

## Direct inspection log

Inspection date: 2026-10-17. Japanese images were visually read, not OCR-only. The complete chapter was reviewed where attribution or narrative-mode context required it (V07 Ch.39, V13 Ch.75, V15 Ch.87). Other selected contiguous scenes include their surrounding exchanges; scope does not silently expand to the full volume. V16–V18 are excluded from this literary inspection log.

| Volume | Raw images actually inspected |
| --- | --- |
| V01 | 0021–0024; 0081–0108 |
| V02 | 0072–0079 |
| V03 | 0144–0151 |
| V04 | 0136–0143 |
| V05 | 0137–0144 |
| V06 | 0130–0154 |
| V07 | 0103–0138 (complete Ch.39 within this span) |
| V08 | 0003–0014; 0057–0082 (complete Ch.43) |
| V09 | 0145–0154 |
| V10 | 0023–0028 |
| V11 | 0075–0080 |
| V12 | 0151–0154; 0165–0168 |
| V13 | 0135–0160 (complete Ch.75) |
| V14 | 0075–0078; 0127–0134; 0138–0141 |
| V15 | 0012–0015; 0026–0029; 0137–0162 (complete Ch.87) |

## Unique observation register

| Stable ID | Volume / chapter / raw-image locator | Canonical reading and checkpoint | Bounded observation / extracted proposition | Class, confidence and alternatives | Verification |
| --- | --- | --- | --- | --- | --- |
| E01-01 | V01 / Ch.1 / 0021–0024.jpg | V01 reading; CP03 | Rin offers food to the stranded Nadeshiko; practical care precedes established friendship. | DE; high for offer; kindness here does not establish universal hospitality. | PRIMARY_VERIFIED |
| E01-02 | V01 / Ch.3–4 / 0081–0108.jpg | V01 reading; CP03 | Rin dislikes the prospect of group camping; the later apology exchange and Nadeshiko’s optional invitation preserve that preference while enabling contact. | DE/CA; high for exchange, moderate for a general boundary rule; neither refusal nor apology proves aversion to people. | PRIMARY_VERIFIED |
| E01-03 | V01 / Ch.4 / 0093–0108.jpg | V01 reading; CP03 | Nadeshiko brings food and cooks with Rin; companionship and practical contribution coexist with novice camping status. | DE; food competence is not equipment or risk mastery. | PRIMARY_VERIFIED |
| E02-01 | V02 / Ch.8 / 0044–0051.jpg | V02 reading; CP03 | Separated night-view messages connect Rin’s solo trip and the club’s outing. | DE→IN; shared attention does not abolish separate itineraries. | ANALYSIS_EXTRACTED |
| E02-02 | V02 / Ch.9 / 0072–0079.jpg | V02 reading; CP03 | Ena prompts Rin to give the souvenir herself; Rin then initiates a meat-grilling plan and Nadeshiko volunteers site finding. | DE; high; Ena’s mediation and Rin’s own initiative are distinguishable. | PRIMARY_VERIFIED |
| E02-03 | V02 / Ch.11 / 0123–0126.jpg | V02 reading; CP03 | Charcoal lighting requires outside assistance; material choice defeats presumed competence. | DE/CA; no global expert grade for Rin. | ANALYSIS_EXTRACTED |
| E03-01 | V03 / Ch.18 / 0144–0147.jpg | V03 reading; CP03 | Rin privately criticizes her travel execution; Chiaki supplies route knowledge from family experience. Rin declines the group invitation. | DE; competence is distributed and refusal remains permissible. | PRIMARY_VERIFIED |
| E03-02 | V03 / Ch.18 / 0148–0151.jpg | V03 reading; CP03 | Ena frames solo and group camping as different kinds of enjoyment; Rin changes from refusal to considering it. | DE; high; consideration is not attendance or conversion. | PRIMARY_VERIFIED |
| E03-03 | V03 / Ch.14–18 / 0005–0154.jpg | V03 reading; CP03 | The V03 checkpoint preserves Nadeshiko’s social/food confidence, Chiaki’s initiative under budget constraints, and a comparatively thin Aoi baseline. | RP/IN; chapter-wide extraction locator, not a claim that every page was reverified. | ANALYSIS_EXTRACTED |
| E04-01 | V04 / Ch.19–22 / 0016–0021; 0095–0122.jpg | V04 reading; CP06 | Christmas participation occurs; Aoi’s cooking and shared errands make group pleasure practical. | DE/RP; V03’s merely prospective group invitation cannot be upgraded retrospectively. | ANALYSIS_EXTRACTED |
| E04-02 | V04 / Ch.23 / 0136–0143.jpg | V04 reading; CP06 | Rin and Nadeshiko share quiet conversation, teasing and thanks for errands; Rin assents to future camping. Rin wakes Nadeshiko for her planned breakfast. | DE; high; proximity/quiet does not specify romantic meaning. | PRIMARY_VERIFIED |
| E05-01 | V05 / Ch.24; 27 / 0005–0016; 0087–0088.jpg | V05 reading; CP06 | Paid work and family transport constrain or enable trips; icy roads require recovery support. | DE; independence is materially supported, not resource-free. | ANALYSIS_EXTRACTED |
| E05-02 | V05 / Ch.28 / 0137–0144.jpg | V05 reading; CP06 | Rin describes a positive solitary experience including loneliness; Ayano expresses interest in visiting by moped after hearing the pair. | DE/CA; high; Ayano’s expressed plan is not completed camping experience. | PRIMARY_VERIFIED |
| E05-03 | V05 / Ch.28 / 0117–0125.jpg | V05 reading; CP06 | Money, meals and Nadeshiko’s pre-existing friendship with Ayano complicate a simple isolated-camper dyad. | DE/IN; friendship predates Rin’s access to it. | ANALYSIS_EXTRACTED |
| E06-01 | V06 / Ch.33 / 0130–0133.jpg | V06 reading; CP06 | Nadeshiko considers solo camping; Aoi recognizes that altitude and earlier mild-weather experience undermined the trio’s preparation. | DE/CA; intention and recognition are not yet successful independent practice. | PRIMARY_VERIFIED |
| E06-02 | V06 / Ch.34 / 0135–0154.jpg | V06 reading; CP06 | Cold-weather failure requires nearby campers’ shelter and Toba’s intervention; Rin contacts Toba remotely; Toba specifies preparation and consultation. | DE/CA; high; rescued outcome is not safe original planning, and adult reliability remains domain-limited. | PRIMARY_VERIFIED |
| E07-01 | V07 / Ch.39 / 0109–0120.jpg | V07 reading; CP09 | Nadeshiko’s solo trip includes cooking with children, a burned item and successful social contact. | DE/CA; high; solo does not mean no interaction and one failure does not erase food ability. | PRIMARY_VERIFIED |
| E07-02 | V07 / Ch.38–40 / 0103–0138.jpg | V07 reading; CP09 | Rin and Sakura independently check on Nadeshiko; concealment prevents takeover but complicates consent-transparent care. Nadeshiko later wants solo/group alternation. | DE→IN; high for actions and expressed preference, moderate for the care model. | PRIMARY_VERIFIED |
| E08-01 | V08 / Ch.41–42 / 0005–0056.jpg | V08 reading; CP09 | Rin’s riding goal is enabled by several family members’ equipment and experience. | DE/RP; source sections distinguish father, mother and grandfather; avoid a composite family expert. | ANALYSIS_EXTRACTED |
| E08-02 | V08 / Ch.41; 43 / 0007–0010; 0057–0060.jpg | V08 reading; CP09 | Aoi asks Toba to include her younger sister, explicitly identified as Akari, and discusses bedding; departure later includes her. Raw0058’s separate entrustment is Sakura → Nadeshiko, not evidence for Akari. | DE; high for sibling attribution; corrects CP09 §18.8’s Kagamihara heading (ER-002); verification-reference correction recorded in audit. | PRIMARY_VERIFIED |
| E08-03 | V08 / Ch.45–46 / 0109–0160.jpg | V08 reading; CP09 | Izu permissions/site planning and reuse of the Iida connection show adult and group plans can need revision. | DE/CA; extracted scene range; no claim that all local rules are mastered. | ANALYSIS_EXTRACTED |
| E09-01 | V09 / Ch.47 / 0024–0025.jpg | V09 reading; CP09 | Ena imagines a driving license at eighteen; Rin acknowledges change while retaining liking for solo camping. | DE; future licensing is not current capacity. | ANALYSIS_EXTRACTED |
| E09-02 | V09 / Ch.52 / 0145–0148.jpg | V09 reading; CP09 | Rin’s return combines remembered companionship, a little loneliness, pleasant fatigue and security near home. | DE/CA; high for explicitly layered affect; reject a single-cause sadness diagnosis. | PRIMARY_VERIFIED |
| E09-03 | V09 / Ch.52 / 0149–0154.jpg | V09 reading; CP09 | Nadeshiko worries about unanswered messages and arrives with Sakura; Rin recognizes reciprocal worry and offers future travel as ordinary continuation. | DE/IN; high for acts; concern is not evidence of exclusive romantic obligation. | PRIMARY_VERIFIED |
| E10-01 | V10 / Ch.53 / 0017–0019.jpg | V10 reading; CP12 | Rin and Ayano begin direct trip coordination rather than requiring Nadeshiko to mediate every contact. | DE; relationship-specific change, not equal intimacy in all pairings. | ANALYSIS_EXTRACTED |
| E10-02 | V10 / Ch.53 / 0023–0028.jpg | V10 reading; CP12 | Toba demonstrates and limits use of improvised alcohol stoves; students learn about low-visibility flame and handling risks. | DE/CA; high as fictional instruction; this ledger is not a real-world safety manual. | PRIMARY_VERIFIED |
| E10-03 | V10 / Ch.55 / 0067–0069.jpg | V10 reading; CP12 | The sausage experiment fails in a recoverable domain. | DE/CA; food failure cannot be equated to exposure or fuel danger. | ANALYSIS_EXTRACTED |
| E10-04 | V10 / Ch.56 / 0083–0092.jpg | V10 reading; CP12 | The Oigawa plan distributes routes and meeting points; experience can still produce complacency. | DE/IN; prospective arrangement at V10, not yet successful execution. | ANALYSIS_EXTRACTED |
| E11-01 | V11 / Ch.59–60 / 0047–0051; 0063.jpg | V11 reading; CP12 | Rin/Ayano’s direct companionship includes retreat from danger and material assistance. | DE; retreat counts as judgment rather than proof of inadequacy. | ANALYSIS_EXTRACTED |
| E11-02 | V11 / Ch.60 / 0075–0080.jpg | V11 reading; CP12 | Nadeshiko notes culinary playfulness; Ayano explains used compact equipment, learns tent setup and erects it herself. Rin’s assistance is bounded. | DE; high; ownership/cost choice, novice setup and autonomy must remain distinct. | PRIMARY_VERIFIED |
| E11-03 | V11 / Ch.61–63 / 0083–0099; 0116–0119; 0145–0156.jpg | V11 reading; CP12 | Separate travel modules converge in food/story sharing, stranger contact and continuing check-ins. | RP/IN; evidence of compatible configurations, not equal preferences for every participant. | ANALYSIS_EXTRACTED |
| E12-01 | V12 / Ch.64 / 0013–0026.jpg | V12 reading; CP12 | Acquired wood needs splitting and months of drying; material benefit has labor and time costs. | DE; stored wood is not yet transmitted inheritance. | ANALYSIS_EXTRACTED |
| E12-02 | V12 / Ch.65–69 / 0031–0056; 0122–0124; 0147.jpg | V12 reading; CP12 | Chiaki/Aoi/Ena’s outing is retold to absent Nadeshiko; revised sausage technique succeeds. | DE/RP; retelling is mediated and exaggerated passages need mode checks. | ANALYSIS_EXTRACTED |
| E12-03 | V12 / Ch.69 / 0151–0154.jpg | V12 reading; CP12 | Nadeshiko imagines future juniors using prepared wood; Aoi questions whether juniors will join; Chiaki imagines coercive labor as a joke. | DE/CA; high; desire, reservation and fantasy are not completed succession. | PRIMARY_VERIFIED |
| E12-04 | V12 / Ch.bonus 101 / 0165–0166.jpg | V12 reading; CP12 | Ena and Rin retract invented friendship-origin stories. | DE/CA; high; narrated false history must not become a biographical fact. | PRIMARY_VERIFIED |
| E13-01 | V13 / Ch.70 / 0014–0020.jpg | V13 reading; CP15 | Cleanup includes Rin transmitting practical knowledge; no single expert owns all learning. | DE/RP; bounded teaching episode. | ANALYSIS_EXTRACTED |
| E13-02 | V13 / Ch.71 / 0044–0055.jpg | V13 reading; CP15 | Rin’s independent travel includes an imagined Nadeshiko bicycle possibility, distinct from the later actual Aoi bicycle sequence. | DE/CA; preserve imagined versus enacted mode; source-generation correction is V1.2. | ANALYSIS_EXTRACTED |
| E13-03 | V13 / Ch.73–74 / 0093–0105; 0109–0123.jpg | V13 reading; CP15 | Ema’s art/contact route and Chiaki’s first solo camping thicken different peripheral and club states. | DE; neither Ema membership nor a universal Chiaki solitude preference follows. | ANALYSIS_EXTRACTED |
| E13-04 | V13 / Ch.75 / 0135–0160.jpg | V13 reading; CP15 | Aoi receives her grandmother’s road bike, practices, extends her ride, punctures and needs pickup. Chiaki improvises a brake-holding aid. A father-expertise story is revealed as an April Fool joke. | DE/CA; high; the actual cyclist is Aoi. Brake stabilization is not puncture repair; father is not established as an expert road cyclist. | PRIMARY_VERIFIED |
| E14-01 | V14 / Ch.78 / 0075–0078.jpg | V14 reading; CP15 | Aoi privately questions tube/valve compatibility, refrains from an uncertain repair and arranges teacher truck pickup for Mei; she reports prior puncture instruction from her father. | DE/CA; high; specific instruction does not license expert family pedigree or universal repair ability. | PRIMARY_VERIFIED |
| E14-02 | V14 / Ch.79 / 0086–0087; 0102–0104.jpg | V14 reading; CP15 | Mei’s bicycle/rental needs and Ema’s food/library/work contacts are distinct entry paths. | DE; Ema’s practical knowledge need not originate in camping. | ANALYSIS_EXTRACTED |
| E14-03 | V14 / Ch.80 / 0127–0134.jpg | V14 reading; CP15 | Mei introduces herself and joins; membership count permits a promotion application. Ema is identified separately through Caribou; Aoi’s cycling-club takeover is comic fantasy. | DE/CA; high; threshold is not completed administrative approval. | PRIMARY_VERIFIED |
| E14-04 | V14 / Ch.81 / 0138–0141.jpg | V14 reading; CP15 | Aoi/Mei’s proposed cycling leg uses Chiaki/Toba car support and a planned father pickup; destination availability lengthens the route. | DE; high for planning; later execution not assumed at V14. | PRIMARY_VERIFIED |
| E14-05 | V14 / Ch.81 / 0149; 0157–0158.jpg | V14 reading; CP15 | Costs and portable food knowledge matter to the developing plan; Ema contributes without demonstrated camping participation. | DE; source knowledge and club membership must stay separate. | ANALYSIS_EXTRACTED |
| E15-01 | V15 / Ch.82 / 0012–0015.jpg | V15 reading; CP15 | Mei is relieved by Aoi’s near-peer pace after a sports-club experience; Aoi identifies herself as a recent road-bike beginner and jokes about no handicap. | DE/CA; high; seniority and helpfulness do not make her an expert mentor. | PRIMARY_VERIFIED |
| E15-02 | V15 / Ch.82 / 0026–0029.jpg | V15 reading; CP15 | Food, water and route pacing support the ride; Toba explicitly permits abandonment/pickup, reducing pressure on both riders. | DE/IN; high for offer, moderate for general non-coercion rule; no guarantee every future ride is recoverable. | PRIMARY_VERIFIED |
| E15-03 | V15 / Ch.83–86 / 0031–0136.jpg | V15 reading; CP15 | The trip works through ordinary constraints, split support and recovery rather than invulnerable execution. Mei evaluates the experience positively. | RP/IN; broad extracted arc; selected primary checks do not verify every stage. | ANALYSIS_EXTRACTED |
| E15-04 | V15 / Ch.87 / 0137.jpg | V15 reading; CP15 | Chiaki is currently writing the promotion application. | DE/CA; high; administrative completion remains OPEN through this image. | PRIMARY_VERIFIED |
| E15-05 | V15 / Ch.87 / 0141–0162.jpg | V15 reading; CP15 | Ema/Rin exchange illustration/dog information; Ena invites them home for Chikuwa. Ema later asks Rin about camping; Rin gives a conditional answer and optional trial suggestion. | DE/CA; high; ER-001 changes speaker attribution, not the conditional proposition. Ema is not shown camping or joining. | PRIMARY_VERIFIED |
| E15-06 | V15 / Ch.87 / 0153–0154.jpg | V15 reading; CP15 | Nadeshiko reacts to friends’ Golden Week work schedules and considers solo camping. | DE; high for aspiration; no executed next trip is admitted. | PRIMARY_VERIFIED |

## Checkpoint-preserving reconstruction of prospective truth

These are retrospective summaries of what the existing checkpoint sequence supported, not newly authored historical checkpoint replacements. Corrections discovered now are explicitly overlaid; the original mistaken formulations remain recoverable in the frozen files and CR records.

| Frozen boundary | Historical authority / evidence | Supportable state at that boundary | Do not backcast |
| --- | --- | --- | --- |
| V03 | CP03 character/relationship freezes; E01–E03 | Rin chooses solitude, helps and initiates selectively; fallible travel; group attendance still only under consideration. Nadeshiko is a camping novice with food/social capacity. Chiaki organizes and helps; Aoi remains comparatively thin; Ena reframes without forcing. | Christmas attendance; accomplished solo Nadeshiko; cycling Aoi; later juniors; any romance conclusion. |
| V06 | CP06 freezes; E04–E06 | Christmas group enjoyment coexists with solo pleasure/loneliness. Work/money/family recovery matter. Yamanaka exposes collective planning failure and distributed rescue. Nadeshiko now intends solo camping. | Completed Nadeshiko solo trip; a generalized expert trio; automatic consent-transparent care. |
| V09 | CP09 §§18–19; E07–E09 | Nadeshiko has tried a socially porous solo trip and wants alternation. Covert checks complicate care. Family-supported riding, modular Izu travel and compound return affect thicken Rin; Ena’s license remains aspirational. Akari is Aoi’s sister (ER-002 overlay). | Proven universal modularity, romance, future driving skill, or independent road-cycling Aoi. |
| V12 | CP12 character/relationship and claim freezes; E10–E12 | Direct Rin/Ayano friendship; separate routes can reconverge. Errors, revised recipes and independent club retelling thicken ordinary practice. Future juniors/wood continuity are imagined; false origin stories remain false. | Actual successors; accomplished promotion; Ema/Mei participation; cycling-expert Aoi. |
| V15 | CP15 §§29–33 plus ER-001; E13–E15 | Aoi is an actual competent cycling beginner/co-learner; Mei has joined and camped; Ema contributes through art/work/contact without established membership or camping. Chiaki is writing a promotion application. Conditional advice to Ema is Rin’s, with Ena supplying dog/home contact. | Formal promotion completed; Ema converted/recruited; expert Aoi; one-way senior teaching; V16 events; full-series thematic closure. |

## Claim transitions and errata

Stable older aliases (`YC-SOL-01`, `YC-AUT-01`, etc.) are retained where available. New CR IDs identify retrospective joins, not a renumbering of the old readings. A theme-level transition extracted from a checkpoint is not primary-verified merely because some examples were inspected.

| Revision / claim ID | Older formulation and original boundary | Transition | Current bounded disposition through V15 | Evidence | Class / verification limits |
| --- | --- | --- | --- | --- | --- |
| CR01 / YC-SOL-01 | V01–V03: solitude positive, group invitation considered | PRESERVE | V04–V09: group enjoyment and return loneliness coexist with chosen solitude; no cure narrative. | E03-02 E04-02 E05-02 E09-02 | DE→RP; high scene support, moderate generalization. |
| CR02 / YC-AUT-01 | Early: low-pressure invitations suggest supported autonomy | REVISE | V07 covert monitoring adds a consent-transparency cost; V15 recoverable support strengthens a bounded, imperfect autonomy model. | E01-02 E07-02 E15-02 | IN/CA; do not erase counterexample. |
| CR03 / YC-MOD-01 | V09: Izu supplies a local modular arrangement | STRENGTHEN | V10 plan / V11 execution / V12 independent outing / V14–V15 split support broaden recurrent practice; not universal preference. | E10-04 E11-03 E12-02 E14-04 E15-03 | RP/IN; mixed verification, ANALYSIS_EXTRACTED as a whole. |
| CR04 / YC-COMP-01 | Early: experienced Rin / novice Nadeshiko shorthand | REVISE | By V15 knowledge moves through food, travel, equipment, family, adults, juniors and nonparticipants; domain-specific competence replaces a single ladder. | E02-03 E03-01 E07-01 E11-02 E14-01 E14-05 | RP/CA; moderate; no total expertise scores. |
| CR05 / AOI_BICYCLE_EXPERT | V14 provisional senior helper / mentor shorthand | REJECT | V15 explicitly identifies recent beginner status; use competent beginner and co-learner, preserving specific V14 helpfulness. | E13-04 E14-01 E15-01 | DE/CA; primary-verified; V03 Aoi state unaffected. |
| CR06 / V13_RIDER_ATTRIBUTION | V13 pre-correction formulation blurred imagined Nadeshiko cycling with actual Ch.75 rider | REVISE | Accepted V13 V1.2 assigns the actual inherited-bike/practice/puncture sequence to Aoi. This repair independently verifies Ch.75, not a new generation. | E13-02 E13-04 | DE/CA; actual sequence primary-verified, imagined-scene extraction retained. |
| CR07 / CLUB_SUCCESSION | V12 future juniors and wood suggest possible institutional time | DOWNGRADE | V13–V15 favor adaptive inter-cohort continuity over completed inheritance: a new member joins, but no succession or completed promotion follows automatically. | E12-01 E12-03 E14-03 E15-04 | TH/CA; mixed verification; imagination retained at V12. |
| CR08 / CLUB_FORMAL_PROMOTION | V14 membership threshold met | OPEN | V15 raw0137 depicts application-writing; no accepted record establishes completed administrative approval. | E14-03 E15-04 | DE/CA; primary-verified; later resolution requires later authorized evidence. |
| CR09 / ER-001 / EMA_CAMPING_ADVICE | Frozen V15 and CP15: Ena gives Ema the conditional camping answer | REVISE | Rin gives that answer. Preserve the conditional proposition; reassign the voice, relationship and character delta. Ena’s distinct invitation remains hers. | E15-05 | DE/CA; PRIMARY_VERIFIED; full Ch.87; audit lists affected sections. |
| CR10 / ER-002 / AKARI_IDENTITY | CP09 §18.8 heading: Kagamihara Akari / 各務原あかり | REVISE | Index as Inuyama Akari, Aoi’s younger sister. The short body’s younger-sibling travel description survives; do not attach it to Nadeshiko’s family. | E08-02 | DE/CA; PRIMARY_VERIFIED sibling identity; Aoi’s explicit sister reference and Toba’s Akari name in Ch.41 planning resolve the family. |
| CR11 / EMA_MEMBERSHIP | V13 art link, V14 work/library link, V15 curiosity | OPEN | No camping participation or club membership established through V15; contribution is not recruitment outcome. | E13-03 E14-02 E14-05 E15-05 | DE/CA; mixed; absence conclusion bounded to accepted evidence, not future impossibility. |
| CR12 / YC-ROM-01 | V03: romance unsupported | PRESERVE | V06/V09/V12/V15 friendship evidence becomes richer; no authorized romantic conclusion follows from closeness, care, silence or routine futurity. | E04-02 E07-02 E09-03 E11-03 E15-05 | IN/CA; absence of sufficient evidence, not exclusion of every reading or future possibility. |
| CR13 / YC-RISK-01 | V06 cold failure reveals consequential risk | PRESERVE | V10 food experimentation and fuel instruction occupy different risk domains; V15 pickup is a specific recovery provision. | E06-02 E10-02 E10-03 E15-02 | CA/IN; preserve distinctions, do not turn “low shame” into consequence-free action. |
| CR14 / YC-ORD-01; YC-FLOUR-01 | Early ordinary pleasure candidate versus stronger philosophy | STRENGTHEN / OPEN | By CP15 ordinary-life sufficiency is strong; philosophical flourishing remains withheld. Experiential richness is not proof of a total doctrine. | E04-02 E05-02 E09-02 E12-02 E15-03 | TH; extraction from checkpoint sequence, not independently primary-verified theme. |
| CR15 / FAMILY_EXPERTISE | V13 Aoi reports father road-cycling experience via grandmother | REJECT | Ch.75 retracts it as April Fool teasing. V14 specific puncture instruction is admissible without resurrecting an expert-road-cyclist pedigree. | E13-04 E14-01 | DE/CA; PRIMARY_VERIFIED; distinguish source joke from analyst error. |
| CR16 / RIN_ENA_ORIGIN | V12 bonus supplies realistic-sounding childhood origin stories | REJECT | Explicit retractions prevent the fabricated details entering either biography. | E12-04 | DE/CA; PRIMARY_VERIFIED; narrative plausibility is not truth. |

## Remaining five architectural ledger responsibilities

No empty standalone files are created. The exact embedded homes below remain recoverable through the canonical reading/checkpoint routes above. Their deferred consolidation does not block V16 continuation; a later synthesis must satisfy the stated dependency.

| Responsibility | Current status | Existing home and bridge | Consolidation dependency |
| --- | --- | --- | --- |
| Place / Geography / Season / Travel | Embedded; standalone deferred | V01 §9; V15 §23.4; CP15 §§18–19,37.9; geography amendment governs evidence layers. | Need arises when place/season/mobility must be retrieved across many scenes for a dedicated argument; first align raw/printed locators and separate narrative causality from real-world identification. |
| Food / Hospitality / Routine | Embedded; core overlap linked | V01 §8; V15 §§11,23.5; CP15 §20; CM01/02/06/17/20/22/29 and directed RS rows supply behavior-critical cases. | Consolidate for a dedicated food/routine synthesis requiring comparison beyond competence or care; do not duplicate these rows without an additional retrieval responsibility. |
| Visual Rhythm and Form | Embedded; standalone deferred | V01 §11; V15 §15; CP15 §27; source register identifies checked quiet/fantasy scenes. | A formal claim requires spread/sequence reinspection at sufficient resolution. Contact-sheet checks of selected scenes do not verify every visual interpretation. |
| Non-Escalation and Social Regulation | Embedded with contradiction bridge | V01 §13; V15 §16; CP15 §22; CR02/13 and RS13/28 retain covert-care and consequential-risk counterexamples. | Consolidate when testing regulation across independent configurations; first distinguish tone, narrated repair, consent, actual outcomes and merely inferred ethics. |
| Candidate Themes and Counterevidence | Embedded plus this revision register | V01 §§14–15; V15 §§20–21; CP15 §§32–33; CR01–16 preserve consequential transitions. | Dedicated theme synthesis must reconcile the full checkpoint history and remaining sequential evidence; this register does not replace all local claim histories. |

## Coverage, counts and unresolved work

The unique observation register contains **50 records: 28 PRIMARY_VERIFIED and 22 ANALYSIS_EXTRACTED**, with zero unresolved CONFLICT_REQUIRES_REVIEW observations and zero placeholders counted as observations. It covers every V01–V15 volume, with at least one bounded primary check per volume. The five ledgers contain 39 character rows, 31 relationship rows, 25 verified voice-sample rows, 33 competence rows, and 16 revision rows. These are overlapping views; **do not add their verification counts to the 50 unique observations**. A voice row can include two micro-excerpts from the same episode; this does not create independent evidence.

Resolved conflicts: ER-001 (V15 Rin/Ena attribution), ER-002 (Akari surname/family), and independent reconfirmation of already accepted V13 V1.2. Open analytical questions are retained rather than mislabeled unresolved source conflicts: formal club promotion, Ema’s later participation, actual succession, stronger flourishing theory, and future relationship changes.

The 22 extracted observations need targeted image reinspection before serving as high-consequence reconstruction rules or exact voice claims. Verification gaps include broad family-support attributions (E08-01), detailed Izu rules (E08-03), full V15 trip execution (E15-03), and several recipe/retelling histories. They are useful canonical-analysis retrieval records now, not primary-certified models. Voice coverage is deliberately insufficient for a validated simulation of any subject. The held-out set is currently **none**: readings and selected images are all in-sample to this repair. Future independent tests must declare their split and avoid using later knowledge to score an earlier state.

No source imagery, archives, page extractions, or full dialogue is committed. No V16 reading, V16–V18 checkpoint, final character simulation, capability grade, or completed-series synthesis is produced.
