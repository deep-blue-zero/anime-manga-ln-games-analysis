---
title: "Gakuen Idolmaster V2 - Continuity and Story-State Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.2"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-08-15 - Phase 3 Shiun Sumika textual core pass"
status: "active; cumulative through Phase 3 Shiun Sumika textual core pass"
---

# CONTINUITY AND STORY-STATE LEDGER

## Governing fields

| field | meaning |
| --- | --- |
| continuity_id | stable ledger ID |
| scope | named route/institution/story object |
| bounded claim | what the source supports |
| source family | primary locator/pattern |
| class | C0-C4 or O (open snapshot gap) |
| assertion type | institution, event, world state, conditional response, or snapshot gap |
| confidence | evidentiary confidence |
| restraint | what must not be inferred |

## Phase 1 entries

| id | scope | bounded claim | source | class | assertion type | confidence | restraint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CONT-001` | `G-INST/P1` | Series 1 target is recurring performance 初; intermediate and final exams gate participation | `adv_pstory_001_cmmn_world-explanation.txt` | `C0` | `INSTITUTION_RULE` | high | result itself C3 |
| `CONT-002` | `P1-[IDOL]` | route-start/training/exam/end family is a conditional graph, not 31 consecutive scenes | `adv_pstory_001_[code]_*` | `C1/C3` | `RELEASE_ORDER_ONLY + CONDITIONAL_RESPONSE` | high | numeric suffix semantics family-local |
| `CONT-003` | `D-[IDOL]` | Dear 001-010 forms the initial character/Producer route | `adv_dear_[code]_001..010.txt` | `C1` | `EVENT_OCCURRED` | high | 010-01 inserted after 010 where present |
| `CONT-004` | `P1->P2` | N.I.A. follows a successful regular-performance state | `adv_pstory_002_cmmn_world-explanation.txt` | `C1` | `EVENT_OCCURRED` | high | exact P1 grade unresolved |
| `CONT-005` | `G-INST/P2` | N.I.A. uses fan-vote ranking; top three enter FINALE | `adv_pstory_002_cmmn_world-explanation.txt` | `C0` | `INSTITUTION_RULE` | high | Producer popularity work explicit |
| `CONT-006` | `D-[IDOL]` | Dear 011-020 is the route-resolved N.I.A. cycle | `adv_dear_[code]_011..020.txt` | `C1` | `EVENT_OCCURRED` | high | special structure for Tsubame/Sena |
| `CONT-007` | `P2-[IDOL]` | N.I.A. pstory/presult failure, normal, true-labeled outcomes are mutually exclusive | `adv_pstory_002_[code]_* + adv_presult_002_*` | `C3` | `CONDITIONAL_RESPONSE` | high | Dear successful route does not erase alternatives |
| `CONT-008` | `D-[IDOL]` | Dear 021-027 is post-N.I.A./summer-H.I.F. transition | `adv_dear_[code]_021..027.txt` | `C1` | `EVENT_OCCURRED` | high | content varies by route |
| `CONT-009` | `D-SAKI` | Ume is summer Prima Stella | `adv_dear_hski_022.txt` | `C0` | `EVENT_OCCURRED` | high | track-scoped incumbent |
| `CONT-010` | `U1` | Saki is summer Prima Stella after Re;IRIS unit victory | `adv_unit_01-04_20.txt; adv_unit_01-04_25.txt` | `C0/C1` | `EVENT_OCCURRED` | high | incompatible with D-SAKI champion state |
| `CONT-011` | `D-SENA` | Sena wins summer H.I.F. three-peat | `adv_dear_jsna_027.txt` | `C0/C1` | `EVENT_OCCURRED` | high | route-scoped |
| `CONT-012` | `G-INST/P3` | winter H.I.F. reforms solo/unit divisions, Selection, prescribed/free rounds | `adv_pstory_003_cmmn_world-explanation-selection.txt; ...final.txt` | `C0` | `INSTITUTION_RULE` | high | later than old-rules summer regime |
| `CONT-013` | `D-[10 resolved routes]` | Dear 028-037 is winter-H.I.F. route; 036 ceremony, 037 aftermath | `adv_dear_[code]_028..037.txt` | `C1` | `EVENT_OCCURRED` | high | not present for Kotone/Tsubame/Sena |
| `CONT-014` | `P3-C` | Sena is incumbent Prima Stella/top idol | `adv_pstory_003_cmmn_world-explanation-selection.txt` | `C0` | `INSTITUTION_RULE/WORLD_STATE` | high | not global |
| `CONT-015` | `P3-SAKI` | Ume is incumbent; Sena former champion | `adv_pstory_003_hski_world-explanation-selection.txt` | `C0` | `WORLD_STATE` | high | mutually exclusive with P3-C |
| `CONT-016` | `P3-REV-LILJA` | REVERSI wins; Lilja receives singular Prima Stella title | `adv_dear_kllj_036.txt` | `C1/C3` | `EVENT_OCCURRED` | high | exclusive with Sumika endpoint |
| `CONT-017` | `P3-REV-SUMIKA` | REVERSI wins; Sumika receives singular Prima Stella title | `adv_dear_ssmk_036.txt` | `C1/C3` | `EVENT_OCCURRED` | high | exclusive with Lilja endpoint |
| `CONT-018` | `D-KOTONE` | winter outcome absent after Dear 027 | `adv_dear_fktn_027.txt` | `O` | `SNAPSHOT_GAP` | high | do not infer |
| `CONT-019` | `D-TSUBAME` | winter rematch fixed, result absent | `adv_dear_atbm_027.txt` | `C1/O` | `SNAPSHOT_GAP` | high | do not infer |
| `CONT-020` | `D-SENA` | summer three-peat fixed, own winter result absent | `adv_dear_jsna_027.txt` | `C1/O` | `SNAPSHOT_GAP` | high | do not infer |
| `CONT-021` | `U1` | entrance -> April/May Selection -> summer H.I.F. is internally ordered | `adv_unit_01-01_01.txt ... adv_unit_01-04_25.txt` | `C1` | `EVENT_OCCURRED` | high | parallel ensemble track |
| `CONT-022` | `E-001` | first-year class introductions place Event 001 early | `adv_event_001_main-01.txt` | `C1/C2` | `EVENT_OCCURRED` | high/moderate | not identical to U1 meeting order |
| `CONT-023` | `SUPPORT-[ID]` | parts ordered within story; cross-track placement flexible | `adv_csprt_*` | `C1 internal/C4 external` | `CONDITIONAL_RESPONSE` | high | promote by direct anchor |
| `CONT-024` | `CIDOL-[ID]` | parts ordered within episode; episode/rank is not a calendar | `adv_cidol_*` | `C1 internal/C2-C4 external` | `CONDITIONAL_RESPONSE` | high | local audit required |
| `CONT-025` | `P-EVENT-[IDOL]` | Produce events are selected run states | `adv_pevent_*` | `C3` | `CONDITIONAL_RESPONSE` | high | no additive biography |


## Scope rule

`C0` and `C1` are never interpreted globally without the scope column. A route-fixed champion can still be C3 relative to another route.


## Phase 2 entries — institutional and shared-source placement

| id | scope | bounded claim | source | class | assertion type | confidence | restraint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CONT-027` | `G-INST` | the protagonist Producer is both a student and a credentialed P-course Producer | `adv_tutorial_first_cmmn-01.txt` | `C0` | `INSTITUTION_RULE` | high | does not prove every producer-like character has identical authority |
| `CONT-028` | `U1` | the P-course student receives a classroom as an activity base | `adv_unit_01-01_03.txt` | `C0/C1` | `INSTITUTION_RULE` | high | do not export the exact room assignment to every Produce route without evidence |
| `CONT-029` | `E-001` | first-year class is understood as agency-like and expected to cooperate in interclass activity | `adv_event_001_main-01/02.txt` | `C1 internal/C2 global` | `EVENT_OCCURRED + SCHOOL_CULTURE` | high/moderate | event's exact relation to U1 meeting order remains separate |
| `CONT-030` | `U1` | center and leader are distinct, with center changing by song and Kotone chosen for coordination/trust | `adv_unit_01-03_01.txt` | `C1` | `EVENT_OCCURRED` | high | U1-specific unit governance model |
| `CONT-031` | `U1/old H.I.F.` | Selection results enter résumés and are disclosed inside and outside school | `adv_unit_01-03_03.txt` | `C0/C1` | `INSTITUTION_RULE` | high | later regimes may alter implementation; no universal privacy policy inferred |
| `CONT-032` | `floating institutional` | paid industry work is allocated through the Hatsuboshi Request System and internal auditions | `adv_tower-001.txt` | `C0 system/C2 date` | `INSTITUTION_RULE` | high | exact calendar, contract terms, and labor protections unresolved |
| `CONT-033` | `E-005` | Sena receives exceptional permission to operate a student-council pseudo-agency with reduced Producer authority | `adv_event_005_main-01.txt` | `C1 internal/C2 global` | `EVENT_OCCURRED + INSTITUTION_RULE` | high | exception must not be generalized to ordinary Idol-course students |
| `CONT-034` | `P3 shared Produce Events` | lesson choices expose alternative Producer curricula and evaluative standards | `adv_pevent_003_cmmn_school_*` | `C3 collectively` | `CONDITIONAL_RESPONSE` | high | branches establish the curriculum's possibility-space, not one sequential school day |
| `CONT-035` | `E-003` | a live is reoriented from abstract result-seeking toward concrete audience enjoyment | `adv_event_003_main-04.txt` | `C1 internal/C2 global` | `EVENT_OCCURRED` | high/moderate | full event interpretation remains Phase 4 |
| `CONT-036` | `U1` | H.I.F. is addressed to fans and to the people whose labor makes the festival possible | `adv_unit_01-04_16.txt` | `C1` | `EVENT_OCCURRED` | high | character speech is evidence of public ethic, not necessarily formal policy |
| `CONT-037` | `floating event system` | Idol Strengthening Month compares Producer–idol development | `adv_event_highscore_introduction-01.txt` | `C0 system/C2 date` | `INSTITUTION_RULE` | high | exact relation to P1/P2/P3 calendar unresolved |
| `CONT-038` | `P3` | 100 Pro is heavily involved in winter H.I.F. | `adv_pevent_003_cmmn_school_3-006.txt` | `C0/C1` | `INSTITUTION_RULE` | high | exact sponsorship, judging, recruitment, or control must not be invented |
| `CONT-039` | `U1` | material pressure from tuition and paid work affects available developmental time | `adv_unit_01-02_05.txt` | `C1` | `EVENT_OCCURRED` | high | character-specific; not a universal student condition |
| `CONT-040` | `U1/old H.I.F.` | cooperation continues into a final structure that turns unit members into rivals for one title | `adv_unit_01-04_18/24.txt` | `C1` | `INSTITUTION_RULE + EVENT_OCCURRED` | high | old-regime structure; do not collapse with reformed winter rules |
| `CONT-041` | `P3 common lessons` | Asari's pedagogical relationship to the Producer persists through advanced H.I.F. preparation | `adv_pevent_003_cmmn_school_3-005-02.txt` | `C2/C3` | `CONDITIONAL_RESPONSE` | moderate/high | exact lesson branch is optional, but institutional teacher role is strongly supported |

## Phase 2 continuity rule

Institutional facts may recur across tracks without making their personal biographies additive. A school rule can be `C0` while the event that reveals it remains `C2`, `C3`, or `C4` relative to another route. Later character documents must cite the institution entry and the character-track entry separately when both matter.

## Phase 3 — Saki continuity-track additions

| entry ID | source / family | track scope | default class | placement finding | conflict rule |
| --- | --- | --- | --- | --- | --- |
| CONT-SAKI-001 | P1 Saki Produce Story | `P1-SAKI` | C1 spine + C3 results/pools | selection, training, exams, result-conditioned endings | only branch invariants may be exported across result states |
| CONT-SAKI-002 | P2 Saki Produce Story | `P2-SAKI` | C1 spine + C3 results | follows a successful P1 state; N.I.A. public/fan campaign | exact predecessor P1 grade unresolved |
| CONT-SAKI-003 | Dear Idol Saki 001–020 | `D-SAKI` | C1 internal | early selection/plateau → direct Ume contest → N.I.A./external rivalry | alignment with every P1/P2 result grade is not asserted |
| CONT-SAKI-004 | Dear Idol Saki 021–023 | `D-SAKI-SUMMER` | C1 | old-rules summer H.I.F.; Ume wins Prima Stella; Saki's identity breaks | mutually exclusive with U1 Saki-champion summer result |
| CONT-SAKI-005 | Dear Idol Saki 024–035 | `D-SAKI-POSTLOSS` | C1 | Project Stardust, relational reconstruction, Wildest Flower, winter preparation | exact alignment with all modular communications remains local |
| CONT-SAKI-006 | Dear Idol Saki 036–037 | `D-SAKI-WINTER` | C1 | reformed winter H.I.F.; Saki defeats incumbent Ume and becomes Prima Stella | track-specific title history; do not import P3-C Sena-incumbent state |
| CONT-SAKI-007 | Unit Story Saki | `U1` | C1 internal | entrance → Re;IRIS/Begrazia → old-rules summer H.I.F. → Saki Prima Stella | parallel ensemble biography, not an optional D-SAKI result |
| CONT-SAKI-008 | Saki communications | `C-SAKI` | C1 within multipart episode; C2/C4 globally | songs, hobbies, care, equality/exclusivity, post-loss reflections | numeric episode order alone does not establish exact global date |
| CONT-SAKI-009 | Saki Produce Events | `PE-SAKI` | C3 | conditional school/activity/job/advice ecology | traits require repetition; events are not additive biography |
| CONT-SAKI-010 | Saki live/result wrappers | `LIVE/PRESULT-SAKI` | C3 | compact public utterances tied to outcome state | no result wrapper is universal biography |

## Phase 3 — Kotone continuity update

- Kotone Source Lock pstory inventory: **31 Series-1 + 11 Series-2/N.I.A. objects; no dedicated Series-3 pstory folder**.
- Dear Idol provides a later H.I.F.-era longitudinal state through Dear 21–27; this must not be backfilled with nonexistent pstory mechanics.
- `cidol` episode numbers are identifiers, not proof of one strict global chronology unless dialogue supplies internal placement.
- `雨上がりのアイリス` communication contains an alternate/dream Re;IRIS comparison; preserve it as comparative evidence.
- `U1` remains a separate coherent old-rules summer-H.I.F. track and is not automatically merged into `D-KOTONE`.


## Phase 3 — Mao story-state updates

| state ID | track | bounded state | principal evidence | continuity status | analytical use |
| --- | --- | --- | --- | --- | --- |
| `STATE-MAO-D-EARLY` | `D-MAO` | scouting through integration of cute/cool | Dear 001–010 | C1 within D-MAO | child-actor history, puberty/category rupture, first reconstruction |
| `STATE-MAO-D-NIA` | `D-MAO` | N.I.A./Shion/Gekka/Little Prince phase | Dear 011–020 | C1 within D-MAO | reclaimed prince, rival horizontalization, technical reality check |
| `STATE-MAO-D-PRO` | `D-MAO` | 100Pro offer and producer-choice conflict | Dear 021–026 | C1 within D-MAO | professionalization/coauthorship/credential boundary |
| `STATE-MAO-D-SUMMERLOSS` | `D-MAO` | awakened Sena wins summer H.I.F.; Mao privately grieves | Dear 027 | C0/C1 within D-MAO | failure hinge; do not universalize champion history |
| `STATE-MAO-D-WINTER` | `D-MAO` | winter training → Mao Prima Stella → joint 100Pro future | Dear 028–037 | C1 within D-MAO | late reclaimed aspiration and `0番` endpoint |
| `STATE-MAO-P1` | `P1[MAO]` | regular-performance route | 31 Series-1 objects | result branches C3 | early cute/cool and failure possibility-space |
| `STATE-MAO-P2` | `P2[MAO]` | N.I.A. route | 11 Series-2 objects | result branches C3 | public competition/fan/rival possibility-space |
| `STATE-MAO-P3C` | `P3-C[MAO]` | reformed winter H.I.F. gameplay fragments | 4 Mao-owned objects + common P3 exposition | world rules C0; results C3 | ugly persistence/weakest-hand/final-failure comparisons |
| `STATE-MAO-C` | `C-MAO` | modular communications | 24 cidol objects | C2/C4 unless internally linked | songs, dorm memory, succession, Osaka, Rinami duet |
| `STATE-MAO-U1` | `U1` | dorm-leader/supporting senior role | selected Unit Story 01 scenes | C1 within U1 | ensemble care; never pasted into D-MAO chronology |

## Phase 3 Lilja continuity checkpoint

- Lilja Source Lock coverage: 210 objects / 5,791 messages.
- Produce Story: 31 Series-1 objects, 11 Series-2 objects, four Series-3 result fragments.
- The four Series-3 fragments are `selection-failure-01`, `selection-normal-02`, `final-failure-01`, `final-normal-02`; they do not form a complete P3 route.
- Dear 021-037 forms the strongest longitudinal winter-H.I.F./REVERSI state available for Lilja, but remains `D-LILJA` rather than universal P3 truth.
- Dear 036: REVERSI wins and Lilja is Prima Stella in `D-LILJA`.
- P3 final-failure: Sena wins and REVERSI recommits for next year in that branch.
- Never overwrite one result with the other.
- Modular cidol fantasy/role-play (especially episode 012 robot-war scenario) is symbolic/character evidence, not a literal world-state event.
## China continuity update

- `P1[CHINA]`: 31 Produce Story objects / 813 messages.
- `P2[CHINA]`: 11 Produce Story objects / 149 messages.
- `P3-C[CHINA]`: four conditional result fragments / 33 messages only; incomplete as a full route.
- `D-CHINA`: Dear 001–037, including student-council election and winter-H.I.F. progression.
- `M-CHINA`: Produce Events, Idol Communications, live/growth/startup; modular unless a stronger locator anchors placement.
- Dear 036 Prima Stella and Dear 037 aftermath remain **D-CHINA** result state.
- Student-council victory in Dear 027 belongs to D-CHINA and must not be silently imported into unrelated branches.
- The current character thesis is intended to capture cross-track invariants—accurate weakness, support ethics, relational legitimacy—while result claims remain track-scoped.
## Hiro continuity checkpoint — Phase 3

- Source-owned total: **207 objects / 5,653 messages**.
- P1: **31 / 785**; P2: **11 / 149**; P3-C: **4 / 45 conditional fragments**.
- `D-HIRO` Dear 021–037 is the principal winter-H.I.F. longitudinal track.
- `D-HIRO` Dear 036 = Hiro Prima Stella; track-scoped.
- P3-C `selection-failure-01` and `final-failure-01` remain incompatible alternative result states and establish fear of termination/separation.
- Modular song/image communications (`C-HIRO`) can support longitudinal hypotheses but do not by themselves prove exact placement inside every result route.
- Current safe developmental spine: effortless competence/boredom -> chosen unsuitability/hobby -> first jealousy/liking idolhood -> fan/rival responsibility -> shared dream -> goddess/cute coauthorship -> crisis wager/fear of loss -> accumulated relational power -> D-HIRO peak miracle -> self-owned top-idol dream.

## Phase 3 — Rinami continuity/state delta

| track | scope in Source Lock 1.0 | safe use | unsafe merge |
| --- | --- | --- | --- |
| P1[RINAMI] | 31 Produce Story objects / 670 messages | Series-1 development, late-blooming recovery, first performance logic | do not treat all Dear romance/Prima Stella as already resolved |
| P2[RINAMI] | 11 Produce Story objects / 167 messages | N.I.A. competition/result-state development | do not use as proof of D-RINAMI summer/winter sequence |
| P3-C[RINAMI] | 4 conditional fragments / 40 messages | selection/final conditional reactions only | **not a complete Series-3 route**; do not fabricate missing connective episodes |
| D-RINAMI | 38 objects / 2,805 messages | longitudinal character authority including Dear 036 Prima Stella | D-RINAMI victory does not overwrite P3-C normal/failure states |
| M-RINAMI | 83 Produce Events + 30 CIDOL + minor families | trait, ordinary-life, work, song/image, relationship tests | not automatically chronological in every route |

Continuity-sensitive hinge: Dear 023–027 summer loss/homecoming and Dear 036 victory belong to D-RINAMI's own result history. Preserve that state identity in later ensemble/monograph synthesis.

## Sumika story-state additions — Phase 3

| state ID | track | source family | bounded authority | continuity warning |
| --- | --- | --- | --- | --- |
| `STATE-SUMIKA-P1` | `P1[SUMIKA]` | Series 1 Produce Story | avoidance -> renewed commitment -> top-idol intent | branch grades/result texture remain local |
| `STATE-SUMIKA-P2` | `P2[SUMIKA]` | Series 2 Produce Story | N.I.A. competitive seriousness and public growth | do not use to force D-SUMIKA exact outcomes |
| `STATE-SUMIKA-P3C` | `P3-C[SUMIKA]` | four Series 3 files | selection/final conditional outcomes only | **not a complete Series-3 biography** |
| `STATE-SUMIKA-D` | `D-SUMIKA` | Dear 001–037 + 010-01 | longitudinal injury/expectation -> N.I.A. -> STEP3 -> REVERSI/HIF | Dear 036 Prima Stella belongs here only |
| `STATE-SUMIKA-M` | `M-SUMIKA` | 83 pevent + 24 cidol + live/growth/startup | ordinary sociability, song authorship, work, REVERSI texture | compatible trait evidence unless result-state dependency appears |

Sumika's D-track and Lilja's D-track may be compared for REVERSI, but agreement on shared scenes does not erase character-specific internal framing.


## Ume story-state additions — Phase 3

| state ID | track | source family | bounded authority | continuity warning |
| --- | --- | --- | --- | --- |
| `STATE-UME-P1` | `P1[UME]` | Series 1 Produce Story | supplementary admission -> slow-start growth -> Saki-centered idol challenge | local result branches remain local |
| `STATE-UME-P2` | `P2[UME]` | Series 2 Produce Story | N.I.A. competition, public/fan stakes, victory/defeat etiquette | do not force D-UME exact outcomes |
| `STATE-UME-P3C` | `P3-C[UME]` | four Series 3 files | selection/final conditional reactions only | **not a complete Series-3 biography** |
| `STATE-UME-D` | `D-UME` | Dear 001–037 | pursuit -> equality/fear -> Saki victory -> post-pursuit self-authorship -> HIF/Prima Stella | D-UME result history remains character-track-specific |
| `STATE-UME-M` | `M-UME` | 83 pevent + 24 CIDOL + minor families | family/body, Worst Three, song, work, fans, ordinary life | compatible trait evidence unless result dependency appears |

The strongest longitudinal hinge is Dear 019–020: beating Saki does not complete Ume's biography; it ends the **pursuit-only** form of the biography and opens self-authored idol vocation.

## Misuzu story-state additions — Phase 3

| state ID | track | source family | bounded authority | continuity warning |
| --- | --- | --- | --- | --- |
| `STATE-MISUZU-P1` | `P1[MISUZU]` | Series 1 Produce Story | post-SyngUp! depression -> self-paced development -> solo ambition | do not back-project late confidence into opening state |
| `STATE-MISUZU-P2` | `P2[MISUZU]` | Series 2 Produce Story | N.I.A. jealousy/competition and public pressure | do not force D-MISUZU exact outcomes |
| `STATE-MISUZU-P3C` | `P3-C[MISUZU]` | four Series 3 files | selection/final conditional reactions only | **not a complete Series-3 biography** |
| `STATE-MISUZU-D` | `D-MISUZU` | Dear 001–037 | pace contract -> Temari/Rinha revision -> H.I.F. defeat -> promise crisis -> Prima Stella/night sky | Dear 036–037 authority remains D-MISUZU-specific |
| `STATE-MISUZU-M` | `M-MISUZU` | 83 pevent + 18 CIDOL + live/growth/startup | daily work, care, songs, temporary units, fan rhetoric | compatible trait evidence unless result-state dependency appears |

The decisive late continuity correction is that Prima Stella does **not** complete Misuzu's sky. Dear 037 explicitly enlarges it through unseen stars and a future expected to exceed the present summit.

## Juo Sena continuity map - Phase 3

| state | placement | key transition |
| --- | --- | --- |
| `P1[SENA]` | initial Produce framework | crowned senior encounters plateau, Producer, branch-conditioned failure/success, and perfect-image pressure |
| `P2[SENA]` | N.I.A. framework after initial relation | external field and public ranking expose recognition limits and allow loss without automatic retirement |
| `D-SENA 001-010` | longitudinal Dear movement | retirement/Producer plan -> stat critique -> failed scouting -> humanization -> external rivalry -> Producer apprenticeship |
| `D-SENA 011-020` | longitudinal expansion | world rival -> produces differentiated idols -> successor becomes rival -> support enters ability ontology |
| `D-SENA 021-027` | H.I.F./Prima Stella summit | institutional reform -> custom songs/field construction -> fear -> summer victory -> reopened world ambition |
| `M-SENA` | modular compatible/side states | ordinary work, student-council office, song communications, family/peer texture, live and growth states |

**Continuity finding:** Sena's retirement statement is an early-state solution to plateau and solitude, not a fixed endpoint. Later claims that she will remain an idol and Producer belong to a developed D-SENA state.

**Absence control:** Source Lock 1.0 contains no Sena Series-3 Produce Story family. H.I.F/STEP3 meaning enters through D-SENA, CIDOL, shared/unit, and other modular evidence, not through an inferred P3 Sena route.

## Tsubame continuity delta — 2026-08-16

Tsubame's most stable longitudinal sequence within `D-TSUBAME` is: No.2/Sena-only hierarchy → Misuzu defeat and avoidance recognition → first Sena victory / rival recognition → childhood liberation origin → N.I.A. externalization through Tsukika/Shion → hero ideal → Sena retirement crisis → explicit independent idol identity → Sena re-choice → star-quality problem → summer H.I.F. defeat → winter wager.

The source lock contains no Tsubame Series-3 Produce Story; Phase 3 therefore carries no synthetic cross-branch P3 biography. Dear 024–027 is a valid Dear-route late state, not universal proof that every branch has reached the same configuration.


<!-- PHASE4_EVENTS_001_005_2026-08-23 -->
## Phase 4 — Numbered Events 001–005 continuity promotion

**Authority:** `GKM_EVENTS_001_005_DEEP_READING.md` — Drive `1jb1bUXahrykBDIrdw3VJGdCHSZEGoIe0`.

| source/state | continuity | confidence | promoted finding |
|---|---|---|---|
| `adv_event_highscore_introduction-01/02` | C4 / SYSTEM | high | modular school-wide `アイドル強化月間` framing; no numbered-event dependence established |
| Event 001 | early first-year C1/C2 | very high | begins with Class 1-1 first introductions and proceeds directly into first bonding intervention |
| Event 002 opening | early first-year C1/C2 | very high | Class 1-2 first introductions; approximately parallel to Event 001 opening |
| Event 002 latter half | after Event 001 bonding | very high | Misuzu observes 1-1's change and 1-2 explicitly adopts the class-party model |
| Event 003 | summer modular state | high season / moderate cross-track | Mao/Rinami third-year final summer; Sumika first-year summer; branch-track placement not forced |
| Event 004 | after Event 001; summer festival | very high relative / moderate exact date | explicitly references prior Class 1-1 bonding; Lilja's first Japanese festival |
| Event 005 | early first year, pre-summer H.I.F. | high | freshman council recruitment after observable growth since entrance ceremony |

**Governing correction:** numbered event ID is not a reliable diegetic date. Preserve event-local chronology and explicit cross-event dependencies rather than treating `001 → 005` as a literal calendar sequence.

<!-- PHASE4_EVENTS_006_012_2026-08-23 -->
## Phase 4 — Events 006–012 continuity additions

**Authority:** `GKM_EVENTS_006_012_DEEP_READING.md` — Drive `12qIoWXbSo45TffFLiTA1WvKgB9wpRLJo`.

| relation / source | classification | confidence | finding |
|---|---|---|---|
| Event 005 → Event 006 | bounded `C1/C2` relative link | very high | E006 presupposes the student-council freshman membership state established in E005 |
| Event 007 → Event 011 | bounded `C1/C2` memory link | very high | E011 explicitly recalls the Halloween work from E007 |
| Event 009 | seasonal modular state | very high for season | Christmas work |
| Event 010 | seasonal modular state | very high for season | Valentine's Day |
| Event 011 | seasonal modular state | very high for season | Hinamatsuri / early-March context |
| E009 → E010 → E011 | local seasonal ordering | high | winter/Christmas → Valentine's → Hinamatsuri; do not force this sequence into every Produce-route biography |
| Event 012 present | modular mini-live state | high | Saki/Lilja/Sumika temporary regional mini-live framing |
| Event 012 internal history | early-first-year reconstructed state | high within E012 | flashback layer reconstructs Lilja's inefficient overtraining, Sumika's withdrawal/concealment, and Saki's peer intervention; keep flashback and present state distinct |

**Control rule:** numbered-event order remains non-identical to diegetic chronology. Use direct memories, seasonal anchors, and event-internal flashback labels; do not infer a universal additive timeline from `006`–`012`.

<!-- PHASE4_EVENTS_013_020_2026-08-23 -->
## Phase 4 — Events 013–020 continuity additions

**Authority:** `GKM_EVENTS_013_020_DEEP_READING.md` — Drive `1pyVYENC8kCbXvQtYU60pVdYad8yxCobF`.

Event numbering again cannot be used as a calendar. This tranche contains several strong local anchors, but they point in different temporal directions.

| event | story-state estimate | confidence | basis |
| --- | --- | --- | --- |
| Event 013 | third-year school-trip state, before a coming H.I.F.; after Sena has begun producing first-year student-council members | high locally; moderate globally | Kyoto school trip; Sena discusses current first-year production project; final challenge is framed toward the next H.I.F. |
| Event 014 | first-year Class 1-2 after its friendship structure has stabilized; exact season unresolved | high relationally; low-moderate calendar | Hiro, Ume, China, Misuzu act as established class friends; Class 1-1 rivalry is also established |
| Event 015 | third-year escort-program state with first-year China and Lilja; autumn-coded by red maple scenery; exact relation to route tracks unresolved | high for program structure; moderate for season | Rinami explicitly acts as third-year guide; Hiroshima live; red maple avenue after the performance |
| Event 016 | first-year weekend after Ume has joined the student council and developed an independent friend group | very high relative to E005/E006; low-moderate exact date | Saki comments on Ume's current student-council work and friends; outing is organized partly to give both sisters independent social time |
| Event 017 | third-year state shortly before the **summer H.I.F.** | very high locally | Tsubame explicitly says summer H.I.F. is approaching; senior quartet schedules a recruitment/publicity shoot |
| Event 018 | escort-program state; Sumika is still managing dance-related fear after injury | high locally; moderate global placement | Mao is third-year lead; Sumika and Hiro are first-year participants; Sumika describes ongoing graded return to dance |
| Event 019 | escort-program emergency replacement state; likely after prior regional program installments, but exact order beyond program continuity remains bounded | high for program identity; moderate-high for relation to E015/E018 | student council describes Nagoya as the next upcoming escort-program performance; Saki is recruited as exceptional first-year substitute leader |
| Event 020 | first-year Lilja–Sumika shared-life state, less than one year into their present cohabitation/routine | high locally | they explicitly say it has not yet been a year; both are active Hatsuboshi idols and discuss current work, SNS, and magazine questionnaires |

### Embedded C1 history inside modular events

Several events contain memories that are stronger than the event's own modular placement.

- **Event 013** reconstructs the third-year class's first day: Rinami, Mao, Tsubame, and Sena already display the relational grammar that survives into third year. It also reconstructs Sena's earlier Prima Stella victory and Mao's failure to answer Sena's request to be pursued.
- **Event 016** reconstructs Rinha teaching a younger Temari to bat. The wording Temari later repeats is not merely similar in theme; it is a direct behavioral inheritance.
- **Event 020** contains stable Sweden-history material for Lilja and Sumika: frequent visits to Lilja's home, shared Japanese-language isolation, ballet-centered loneliness, anime/game exchange, and mutual world-expansion.

These memories should be promoted as historical evidence without converting the containing event into a universal route chronology.

### Event-number warning strengthened

Event 017 is explicitly pre-summer-H.I.F., while Event 015 is autumn-coded. Therefore `015 → 016 → 017` cannot be read as an uncomplicated diegetic sequence. The safe practice remains:

> **event-local chronology + explicit cross-event links + seasonal anchors, never event number as biography.**

---

<!-- PHASE4_EVENTS_021_PLUS_2026-08-23 -->
## Phase 4 — Events 021+ continuity additions and numbered-event closure

**Authority:** `GKM_EVENTS_021_PLUS_DEEP_READING.md` — Drive `1kYHscRZA5RSTT6l5TGyaAUMLmeu9uQ6T`.

| event | bounded story-state | status | evidence |
| --- | --- | --- | --- |
| E021 | senior council state ~one year after Sena's first Prima Stella | **high** | Tsubame explicitly finds the old victory photo and says one year has passed |
| E022 | third-year pre-summer-H.I.F.; Kotone first year; Sena current high-status idol | **high local** | Mao calls summer H.I.F. the third-years' last chance; Sena sends notes/live ticket |
| E023 | February, after Temari/Misuzu reconciliation and one year after birthday missed during SyngUp! dissolution | **very high** | explicit month and prior-year account |
| E024 | approximately one year into Sena's student-council producer project; February Shibuya Sound Fest; graduation approaching | **very high local** | explicit year of training / February festival / graduation framing |
| E025 | late senior year, pre-graduation succession state | **very high local** | China explicitly next student-council president; juniors target readiness by spring |
| E026 | modular external-cover professional state | **high professional / low-moderate calendar** | event operator requests trio; headmaster/Sena recommend; no exact season |
| E027–E028 | **absent from Source Lock 1.0** | **coverage fact** | no scripts in dedicated `event_021-plus.dialogue.txt` bundle |
| E029 | internally ordered Asari teacher→produced-idol branch; global mergeability unresolved | **high internal / branch-gated global** | agreement → auditions → live → continuation; premise reverses baseline teacher/student roles without external bridge |

### Phase-4 event corpus closure

Dedicated event source boundary is now completely read under Source Lock 1.0: **136 scripts / 8,507 messages**. Event numbers remain non-calendar identifiers; 027–028 must not be reconstructed from absence. Any later acquisition requires a source-lock delta and a Phase-4 addendum/revision.


<!-- PHASE5_SUPPORT_SERIES_01_2026-08-23 -->
## Phase 5 — Support Series 1 continuity layer

**Authority:** `GKM_SUPPORT_SERIES_01_DEEP_READING.md` — Drive `1bIaJl--tZuINAqz_mhNfufWMLjnEibwz`.

### Governing support-story rule

Support Series 1 consists of 13 support-story IDs / 26 scripts / 470 messages. Story number is **not** diegetic chronology, and two parts grouped under one support story frequently share a focal character without forming one continuous scene. Default classification remains modular `M-*`; promote only explicit historical anchors.

| source | continuity assessment | status / reason |
| --- | --- | --- |
| S0001-P01 | late middle-school Temari immediately before high-school progression | **C1 historical anchor** — trainer explicitly frames middle school ending and coming external-entry competition |
| S0001-P02 | early high-school vocal class after Saki's external admission | **C1-compatible early anchor** — Saki identified as high-school entrant; exact day unresolved |
| S0003-P02 | dorm-life state with Mao as dorm leader and Kotone working late | C2 modular; formal late-return permission system is institutional fact independent of exact date |
| S0008/S0009 | established Worst Three / first-year friendship-training state | C1/C2-compatible relational state; do not force exact relation to numbered-event sequence |
| S0010-P01 | post-SyngUp rupture state in which Misuzu no longer hands Temari care items directly | **C1 relational-history evidence**; exact relation to later reconciliation remains bounded |
| S0011-P02 | pre/new-school-year council recruitment state after older council members graduate and incoming first-years are being reviewed | C1-compatible institutional succession anchor; exact relation to every Produce route unresolved |
| S0012-P01 | early first-year Saki already enrolled and receiving a senior lesson event | C1-compatible senpai/kouhai anchor |

**Cross-track prohibition:** none of these modular support objects selects a single Produce-result branch. Use historical content where explicit, not the enclosing support ID as universal biography.

<!-- PHASE5_SUPPORT_SERIES_02_PART_001_025_2026-08-23 -->
## Phase 5 — Support Series 2 Part 001–025 continuity additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_001_025_DEEP_READING.md` — Drive `1j7SzxEJ0KnP4GNYlvxEqNsJE3rSXFlPM`.

- Bundle filename `part_001-025` contains **story_0000–story_0025 inclusive**: 26 stories / 52 scripts / 961 messages. Coverage accounting must use the actual source boundary.
- Support-story numbering remains non-chronological; paired parts are not presumed adjacent.
- `story_0001`: direct post-SyngUp retrospective evidence from both Temari and Misuzu. Historical incompatibility = Temari's high training drive versus Misuzu repeatedly stopping her; both preserve positive attachment.
- `story_0007/part_02`: **C1 entrance-day memory** — Hiro is physically depleted; China introduces herself and helps her reach the shared classroom.
- `story_0011`: Sena is actively recruiting Kotone and Kotone has not consented. Strongly compatible with the early student-council pseudo-agency recruitment period; exact relation to Event 005 remains OPEN absent a direct bridge.
- `story_0013`: **C1 local anchor — third-year spring**, with Mao/Rinami stating one school year remains until graduation.
- `story_0014`: current Producer Course state includes older students and active working producers; exact protagonist friendship answer is not preserved in A2 and remains unasserted.
- `story_0023`: embedded festival memory directly establishes Mao repairing Lilja's sandal strap, treating her injured foot, and carrying/escorting her to safety.
- `story_0022`: its two parts must not be read automatically as a promise/broken-promise sequence; Misuzu's private-lesson request and later absence may be different modular occasions.

**Current Phase-5 boundary:** Support Series 1 + Series 2 `story_0000–0025` complete. Next locked tranche: `support_series_2_part_026-050.dialogue.txt`.

<!-- PHASE5_SUPPORT_SERIES_02_PART_026_050_2026-08-23 -->
## Phase 5 — Support Series 2 Part 026–050 continuity additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_026_050_DEEP_READING.md` — Drive `1N8cUGstn4VM0sTfLJ_IQVhKfxKDIyL-j`.

Support IDs remain modular and are **not** a global chronology. Local anchors:

- `story_0028` — autumn / pampas grass; part 2 contains direct Hanami household-history evidence: busy parents were often away, Saki progressively took on routine cooking for Ume.
- `story_0034` — autumn foliage; direct childhood memory of Saki/Ume playing near their grandmother's rice fields, getting muddy, eating unknown berries, and competing at dragonfly catching.
- `story_0035` — Christmas-party preparation.
- `story_0037` — winter / year-end and New Year social planning.
- `story_0041` + `story_0042` — Valentine's period / February.
- `story_0044` — approaching spring.
- `story_0049` — current student-council leadership explicitly trains Ume and China for work they will carry “next year.”

Embedded biography may be stronger than the containing support object's modular placement. No support-story number is promoted into a universal date sequence.

<!-- PHASE5_SUPPORT_SERIES_02_PART_051_074_2026-08-24 -->
## Phase 5 — Support Series 2 Part 051–074 continuity additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_051_074_DEEP_READING.md` — Drive `1ltF2IUHs9HJZdHB8zTW2XsIbqmRyTPhP`.

### Bundle-boundary control

The architecture/routing label `051–074` is **not** a contiguous story-ID boundary. Inspected IDs are `0051,0052,0053,0054,0056,0058–0077,0079`; `0055`, `0057`, `0078` are absent from this bundle while `0075–0077` and `0079` are included. Coverage authority follows the 52 scripts / 1,037 messages actually present.

### Stronger local / historical anchors

| story | classification | anchor |
| --- | --- | --- |
| `0058` | C2 seasonal | explicit summer heat and younger siblings on school vacation |
| `0062` | C2 seasonal | Halloween costume/dorm context |
| `0069` | C1-compatible late-third-year institutional | Sena/Tsubame/Rinami actively handing council work to China/next generation; remaining-time language |
| `0075 part_02` | **C1 historical anchor** | explicit first-year Mao/Rinami scene; Sena/Tsubame already serve as high-performing comparison; Mao height-based self-theory active |
| `0077 part_02` | **C1 historical memory** | Sena recalls planting watermelon seed in Tsubame's home garden; Ume recalls childhood seed-spitting contests with Saki |
| `0079` | C2/C4 modular mature-state | Sena live; Tsubame rivalry/fandom and Kotone mentorship are established, but exact global date remains open |

### Continuity implications

- `0075` materially predates Mao's mature refractive-role solution and therefore cannot be treated as a retroactive late-state friendship scene.
- `0077` proves Sena/Tsubame childhood domestic access but not frequency, exclusivity, or complete childhood chronology.
- Seasonal support scenes remain modular; do not chain Halloween → Valentine → summer identifiers into a single mandatory support-card calendar without bridging evidence.

**Cumulative Phase-5 support boundary:** 180/498 scripts / 3,463/9,777 messages.

<!-- PHASE5_SUPPORT_SERIES_03_PART_001_025_2026-08-24 -->
## Phase 5 — Support Series 3 Part 001–025 continuity / story-state controls

**Source boundary:** `support_series_3_part_001-025.dialogue.txt` = **78 scripts / 1,534 messages**, actual `story_0000`–`story_0025`, three parts each. Bundle filename is routing, not literal story minimum.

### Strong local / historical anchors

- `story_0001`: post-SyngUp estrangement before full Temari/Misuzu repair; each already has new class relationships.
- `story_0003`: Ume recalls Saki's makeup instruction around the decision to enter Hatsuboshi; current scene is after enrollment.
- `story_0005`: Mao/Rinami first encounter occurs two years before their current third-year scene; same-year entry is explicit.
- `story_0006`: China/Rinami first encounter during new student-council photography; present material also frames China as next-president candidate.
- `story_0007`: Lilja is an early first-year/new-dorm entrant and does not yet have a producer in the overtraining scene.
- `story_0011`: active estrangement-era Misuzu/Temari state plus early Sena scouting of Ume/Misuzu.
- `story_0015`: explicit first meeting of Sena's current council: Sena president, Tsubame vice president, Rinami secretary, Misuzu accounting-audit (`会計監査`), plus first-year Ume/China; Sena states this year's council is a pseudo-agency.
- `story_0017`: Sumika/Lilja move-in / early cohabitation and shared pre-/early-enrollment history.
- `story_0024`: Kotone work burden is materially affecting school performance; hardship-student relief is named as an available institutional route.

### Dream / nonliteral control

- `story_0004` parts 1–2 are dreams using remembered sibling rivalry grammar; do not treat the dream contests as literal events.
- `story_0021/part_03` explicitly self-identifies as dream by uniform inconsistency; the middle-school-third-year dialogue is evidence of Misuzu's remembered/desiring relational grammar, not a literal present event.

### Relationship-state control

`story_0021/part_02` one-night thunder truce does **not** by itself close the Temari/Misuzu estrangement. It temporarily restores caregiving access while preserving the larger “we are still fighting tomorrow” state.

<!-- PHASE5_SUPPORT_SERIES_03_PART_026_050_2026-08-24 -->
## Phase 5 — Support Series 3 Part 026–050 continuity anchors

- `story_0027`: summer-vacation multiday stay at China's family property; Ume/China/Hiro already identify one another as friends and create a private-life category distinct from school or sports camp.
- `story_0028`: active Temari/Misuzu estrangement with explicitly bounded temporary ceasefire; do not collapse into full reconciliation.
- `story_0030`: China is already in student council; Rinami transmits a festival viewing place learned from a graduated senior.
- `story_0033`: **post-reconciliation** Temari/Misuzu share a two-person room; Misuzu explicitly says old SyngUp/wings structure will not return. Retrospective first-live fight is historical evidence.
- `story_0035`: Ume has established class friendships; ordinary Saki/Ume study/rest routine follows enrollment.
- `story_0038`: newcomer-welcome period; Sena already functions as Prima Stella/president and scans new entrants for development.
- `story_0041`: winter illumination after council work.
- `story_0042`: one-year-prior entrance-exam preparation plus earlier shared Hatsuboshi live memory for Sumika/Lilja.
- `story_0044`–`0046`: multiyear `Campus mode!!` practice history; Mao/Rinami are near graduation and explicitly preparing to hand the song onward.
- `story_0047`–`0048`: Valentine's-period relational evidence.
- `story_0050`: mature Ume/China/Hiro friendship state in which increased idol work is already reducing unstructured time together.

### Continuity control

`story_0033` is a repaired-state authority for Temari/Misuzu but does **not** mean every earlier support story should be reordered into one linear path. Use explicit relationship-state language to route the scene, not numeric story order.

<!-- PHASE5_SUPPORT_SERIES_03_PART_051_075_2026-08-24 -->
## Phase 5 — Support Series 3 Part 051–075 continuity anchors — 2026-08-24

- `story_0051`: Mao/Rinami are explicitly new first-year classmates; Sena is already exceptional; Mao projects to the next cherry-blossom season.
- `story_0052`: retrospective to Saki/Ume Hatsuboshi decision and Saki's unnamed idol inspiration; present Ume is in a more individuated vocation state.
- `story_0053`: explicit **final high-school school trip** for the third-year cohort.
- `story_0055`: entrance-day Lilja/Sumika memory plus later injury-nightmare aftermath; dream exaggeration is remembered-trauma evidence, not literal injury description.
- `story_0058`: active Temari/Misuzu estrangement; remembered ramen outings explicitly include Rinha as third participant.
- `story_0060`: Mashiro Yu is ordinary-course second year / broadcast-club president.
- `story_0064`: Rinami retrospectively identifies first-year removal from `Love☆しすたぁず` and subsequent stage fear.
- `story_0065`: active Temari/Misuzu estrangement while Kotone already runs a paid Temari lunch service.
- `story_0068`: Kotone's younger sister has attended Kotone lives and visits Hatsuboshi to observe daily school life.
- `story_0069`: student-council festival patrol + customary fireworks-viewing place.
- `story_0070`: Kotone's work/school accommodations are already active and academic retest risk is current.
- `story_0071`: third-year leisure with established Sena public fame and Tsubame No.2 status.
- `story_0075`: China treats cross-class friendship as settled ordinary Hatsuboshi life.

### Continuity control

The source confirms modular relationship states but does not license sorting all `0051`–`0075` stories into one numeric chronology. Use explicit states (first-year memory, estrangement, third-year trip, current work/school condition) as anchors. The identity of Saki's unnamed original idol inspiration and Temari's unnamed `昔、仲間` teaching source remain OPEN at these locators.


<!-- PHASE5_SUPPORT_SERIES_03_PART_076_102_2026-08-24 -->
## Phase 5 closure - final support routing boundary

Final canonical support reading: `GKM_SUPPORT_SERIES_03_PART_076_102_DEEP_READING.md` - Drive `1B43voVD6wXug902H9K49VFFDtCFLYnws`.

- Architecture routing label: `SUPPORT_SERIES_03_PART_076_102`.
- Actual source story IDs: `story_0076`-`story_0098`, `story_0100`-`story_0105`, and `story_0108`.
- `story_0099`, `story_0106`, and `story_0107` are absent from the bundle; they are **not analysis gaps** because the audited final tranche is exactly **90 scripts / 1,797 messages** and reconciles the Source Lock support inventory to **498 scripts / 9,777 messages**.
- Every included story has exactly three parts.

### Strong or useful state anchors

- `story_0076`, `0096` - post-reconciliation Temari/Misuzu states;
- `story_0079` - pre-graduation student-council succession expectation;
- `story_0086` - final-year high-school leisure/finitude context for Sena/Tsubame;
- `story_0091` - explicit post-graduation/alumni continuity planning;
- `story_0093` - pre-admission Sumika/Lilja entrance-exam history;
- `story_0097` - H.I.F. return and planned SyngUp dissolution-live context;
- `story_0098` - third-years' final high-school sports festival;
- `story_0104` - H.I.F. context with Sena seeking a fourth consecutive First Star title.

**Phase 5 is COMPLETE under GAKUMAS V2 Source Lock 1.0.** Support-story numbering remains a routing/identity system and is not promoted into one linear chronology.
