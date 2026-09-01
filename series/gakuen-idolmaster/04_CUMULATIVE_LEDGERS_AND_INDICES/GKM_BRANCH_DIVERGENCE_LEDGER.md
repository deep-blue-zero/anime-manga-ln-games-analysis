---
title: "Gakuen Idolmaster V2 - Branch Divergence Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.0"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-08-15 - Phase 3 Shiun Sumika textual core pass"
status: "active; cumulative through Phase 3 Shiun Sumika textual core pass"
---

# BRANCH DIVERGENCE LEDGER

## Schema

| field | meaning |
| --- | --- |
| branch_id | stable branch-family identifier |
| track_scope | route in which the branch occurs |
| source_family | files composing the branch |
| variants | mutually exclusive states |
| invariant_candidate | what may be compared across states |
| biography_safe | YES / CONDITIONAL / INVARIANT-ONLY / NO |
| confidence | high / moderate / tentative |
| notes | unresolved mapping or cautions |

## Phase 1 entries

| branch_id | track | source family | variants | invariant candidate | biography safe | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BR-S1-OPEN | P1[IDOL] | `opening-normal-*`, `opening-true-*` | conditional route-start fragments | initial work posture, Producer address, self-presentation | INVARIANT-ONLY | high | do not concatenate all openings |
| BR-S1-STEP1 | P1[IDOL] | `after-step-1-normal-01..03` | selected development scenes | response to training, weakness, care, work | INVARIANT-ONLY | high | exact gameplay selector not reconstructed |
| BR-S1-MID | P1[IDOL] | `after-audition-mid-failure` + normal 01..04 | failure; four explicit success grades | defeat response, standard of success, self-evaluation | CONDITIONAL / INVARIANT-ONLY | high | Saki sources directly distinguish highest through barely passing |
| BR-S1-STEP2 | P1[IDOL] | `after-step-2-normal-01..03` | selected development scenes | later training adaptation | INVARIANT-ONLY | high | not a three-scene required sequence |
| BR-S1-FINAL | P1[IDOL] | `after-audition-final-failure` + normal 01..04 | failure; four success grades | final-pressure response, Producer relationship | CONDITIONAL / INVARIANT-ONLY | high | mutually exclusive results |
| BR-S1-END | P1[IDOL] | `ending-normal-01..05`, `ending-true-01` | five normal endpoints; one true-labeled endpoint | end-state desire and relationship | NO for event merge; INVARIANT-ONLY for traits | high | exact mapping from result grade to ending number remains local |
| BR-S2-A | P2[IDOL] | `after-audition-a-normal-02/03` | two successful presentations | early N.I.A. self-assessment | CONDITIONAL | high | exact grade/condition semantics not universalized |
| BR-S2-B | P2[IDOL] | `after-audition-b-normal-02/03` | two successful presentations | response to rising public pressure | CONDITIONAL | high | exact grade/condition semantics not universalized |
| BR-S2-MIDFAIL | P2[IDOL] | `after-audition-mid-failure-01` | qualification/ranking failure | recovery behavior | CONDITIONAL | high | unsuccessful branch cannot precede FINALE in same run |
| BR-S2-FINAL | P2[IDOL] | character final failure/normal + `presult_002` failure/normal/true | failed objective; success; FINALE first | response to audience/fan-based judgment | CONDITIONAL / INVARIANT-ONLY | high | branch labels distributed across pstory and presult |
| BR-S3-WORLD | P3 | common vs Saki vs REVERSI exposition | Sena-current; Ume-current/Sena-former; REVERSI special | stable H.I.F. reform rules | NO for champion merge; YES for shared rules | high | world-state branch exists before competition result |
| BR-S3-SELECTION | P3[TRACK] | common Selection fragments + character success/failure + presult | failure; qualification | response to harsher Selection | CONDITIONAL | high | three-exam rule invariant; exact fragment assembly partly technical |
| BR-S3-FINAL | P3[TRACK] | final exposition + character final + presult | non-victory/failure; normal completion; Prima Stella true-labeled | pressure response, song choice, Producer partnership | CONDITIONAL / INVARIANT-ONLY | high | prescribed/free rounds invariant |
| BR-U1-PTRACK | U1 vs individual P tracks | entire unit story versus one-idol Produce routes | ensemble Producer assignment; individual assignment | Producer pedagogy repeated across structures | NO for biography merge; INVARIANT-ONLY for repeated traits | high | U1 is track-level branch, not an optional result |
| BR-CHAMPION-HISTORY | U1 / P3-C / P3-SAKI | U1 ending and P3 starts | Saki summer champion; Sena current; Ume current | institution's seasonal title logic only | NO | high | missing transitions must not be invented |
| BR-PRODUCER-13 | P1/P2 across 13 idols | all character routes | thirteen parallel selected-idol biographies | repeated Producer methods | NO for event merge; INVARIANT-ONLY for method | high | one Producer is not presumed to complete all routes sequentially |

## Filename-semantics rule

A trailing numeric suffix is classified only after source inspection. It may encode:

- result grade;
- technical part position;
- dialogue-pool index;
- stage number;
- runtime composition fragment.

The ledger must not infer one universal meaning from filename shape.

## Phase 3 — Saki-specific branch entries

| branch_id | track | source family | variants | invariant candidate | biography safe | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BR-SAKI-P1-RESULT | P1-SAKI | Saki mid/final result files and endings | failure; four graded successes; normal endpoints; true-labeled endpoint | standards of excellence, affective discharge, demand for analysis, resistance to “completion” praise | CONDITIONAL / INVARIANT-ONLY | high | ordinary failure cycle is comparable; no one biography contains every result |
| BR-SAKI-P1-SCENEPOOL | P1-SAKI | `opening-*`, `after-step-*` | alternate/conditional developmental scenes | body-history, plateau anxiety, Producer reliance, care practice | INVARIANT-ONLY | high | do not narrate every pool member sequentially |
| BR-SAKI-SUMMER-CHAMPION | D-SAKI vs U1 | `adv_dear_hski_021–023` vs `adv_unit_01-04_20..25` | Ume wins summer Prima Stella; Saki wins summer Prima Stella | summer H.I.F. as title/succession pressure | NO for result merge | high | personal outcomes are mutually exclusive even though institutional old-rules summer H.I.F. may be compared |
| BR-SAKI-P3-WORLD | P3-SAKI vs P3-C | Saki world explanation and common Series 3 | Ume incumbent/Sena former; Sena incumbent | winter H.I.F. reform, Selection, prescribed/free rounds | NO for champion merge; YES for shared rules | high | Saki's route must not inherit Sena-current fact from common track |
| BR-SAKI-P3-RESULT | P3-SAKI | Saki selection/final fragments, result wrappers, Dear Idol 036–037 | selection failure/success; final non-victory/normal; true-labeled Prima Stella; D-SAKI narrative victory | response to title pressure and Producer–idol accumulated production | CONDITIONAL | high | Dear Idol supplies the richest personal victory narrative; system files remain branch wrappers |
| BR-SAKI-COMMUNICATION | C-SAKI | communication episodes 000–019 | internally ordered multipart episodes; globally floating song/relationship states | linguistic voice, song self-interpretation, leisure, care, partnership | CONDITIONAL / C2-C4 | moderate-high | do not impose numeric episode order as exact chronology without internal anchors |
| BR-SAKI-PEVENT | PE-SAKI | 83 Produce Events | run-conditioned school/activity/job/advice scenes | repeated habits, competence, care, revision behavior | INVARIANT-ONLY | high on C3 status | later event/support pass decides which ordinary patterns survive broader evidence |
| BR-SAKI-SONG-SELF | D/C-SAKI | `Fighting My Way`, `Campus mode!!`, `がむしゃらに行こう！`, `Wildest Flower`, `GO MY WAY!!`, H.I.F. songs | distinct self-models and narrative placements | controlled disclosure, appropriation, propulsion from deficiency | INVARIANT-ONLY until AV | moderate | textual dramaturgy is established; sonic continuity remains pending |

## Phase 3 — Kotone branch notes

| branch/state | source family | divergence rule | analytical consequence |
| --- | --- | --- | --- |
| `P1[KOTONE]` result ladder | Series 1 pstory | failure/normal/strong result states are alternatives | use to infer standards and response patterns, not cumulative biography |
| `P2[KOTONE]` result ladder | Series 2/N.I.A. pstory | result states are alternatives; Series 2 presupposes successful P1 macro-progress, not one exact grade | failure language may reveal fear without becoming canonical result |
| no Kotone `P3` pstory in Source Lock | pstory inventory | snapshot absence | do not fabricate Series-3 gameplay chronology; later H.I.F. evidence comes through Dear/modular sources |
| `D-KOTONE` H.I.F. | Dear 21–27 | coherent late longitudinal state | can be analyzed as Dear-route development without claiming missing P3 mechanics |
| `U1` Re;IRIS | Unit Story | separate coherent unit track | use for capacity/comparison, not as automatically shared P-route past |
| `cidol 011` Re;IRIS dream/alternate state | Idol Communication | explicitly comparative/dreamlike state | reveals preference/possibility, not literal P-route biography |


## Phase 3 — Mao branch notes

| branch ID | track | source family | divergent states | invariant character evidence allowed | merge rule | confidence | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `BR-MAO-P1-RESULT` | `P1[MAO]` | 31 Series-1 objects | intermediate/final failure; graded normal successes; true-labeled ending | reactions to evaluation, cute/cool anxiety, stage appetite, failure persistence | **NO additive result biography** | high | weak/strong/true outcomes map possibility-space |
| `BR-MAO-P1-END05` | `P1[MAO]` | `ending-normal-05` | low-performance branch includes practice avoidance / desire to give up | reveals that self-acceptance does not make motivation frictionless | branch-specific only | high | counterevidence to seamless growth story |
| `BR-MAO-P2-RESULT` | `P2[MAO]` | 11 Series-2 objects | N.I.A. failure/success paths | protector behavior, fan/rival orientation, competitive grief | **NO result merge** | high | subordinate trap/help scenes are route possibilities, not fixed sequence |
| `BR-MAO-P3-SELECTION` | `P3-C[MAO]` | `selection-failure-01` vs `selection-normal-02` | fail qualification / survive with weakest hand | late “ugly struggle can still be cool” and strategic self-use | conditional | high | shared P3 rules come from common exposition |
| `BR-MAO-P3-FINAL` | `P3-C[MAO]` | `final-failure-01` vs `final-normal-02` plus Dear late route | final failure / nonfailure gameplay states; Dear has its own Prima Stella culmination | persistence and title pressure can cross-inform only when scope named | **DO NOT force one exact gameplay result into Dear** | high | Dear 036 is D-MAO authority for its victory state |
| `BR-MAO-D-U1` | `D-MAO` vs `U1` | Dear route vs Unit Story 01 | solo longitudinal producer relation vs ensemble dorm/unit context | stable senior-care traits may be compared | no biography merge | high | U1 Mao remains a supporting senior, not the Dear protagonist |
| `BR-MAO-COMMU` | `C-MAO` | rank-3 communications | modular song/life scenes with floating placement | relational self, succession, acting craft, preferences | invariant-only unless internally dated | high | do not construct one exact order from numeric episode labels |

## Phase 3 - Lilja branch/route notes

| branch object | classification | rule |
| --- | --- | --- |
| `P1[LILJA]` | C1 within P1 | coherent first Produce progression; do not merge result grades into one exact biography |
| `P2[LILJA]` | C1/C3 | N.I.A. success/failure fragments show confidence and failure semantics; exact results are branch-scoped |
| `P3-C[LILJA]` | C3 fragments | only four Lilja pstory fragments exist in Source Lock: selection failure/normal and final failure/normal |
| `D-LILJA` | C1 longitudinal Dear track | coherent 001-037 arc; Dear 036 REVERSI victory/Lilja Prima Stella authoritative only here |
| `M-LILJA` | C4/modular | idol communications/events supply song, culture, family, ordinary life, and performance hypotheses; chronology must be source-adjudicated |
| REVERSI public-history material | D-LILJA / modular | relationship publicity is usable evidence for dyad/production but not a license to merge Sumika's future V2 route wholesale |
## China branch topology delta

| track/state | evidence | status | do-not-merge rule |
| --- | --- | --- | --- |
| `P1[CHINA]` | 31 Series-1 pstory objects / 813 messages | coherent route family | result branches remain conditional; P1 true ending is not every P1 outcome |
| `P2[CHINA]` | 11 Series-2/N.I.A. pstory objects / 149 messages | coherent result-state family | supports macro progression but does not dictate exact D-CHINA scene history |
| `P3-C[CHINA]` | 4 Series-3 fragments / 33 messages | **conditional fragments only** | never reconstruct a complete China Series-3 Produce biography from these files |
| `D-CHINA` | Dear 001–037 | strong longitudinal character track | Dear 036 Prima Stella victory is authoritative **inside D-CHINA only** |
| `M-CHINA` | cidol/events/live/growth/startup | modular | use for character invariants and compatible texture, not forced chronology |

China's four P3-C fragments are `selection-failure-01`, `selection-normal-02`, `final-failure-01`, and `final-normal-02`. Their coexistence with D-CHINA victory is possibility-space evidence, not contradiction requiring collapse.
## Shinosawa Hiro branch control

| branch / track | source | divergence | rule |
| --- | --- | --- | --- |
| `P1[HIRO]` | Series 1 Produce Story | normal/failure result states around early hobbyist growth | use for P1 trait/result evidence only; do not force one audition grade universally |
| `P2[HIRO]` | Series 2 Produce Story | N.I.A. success/failure texture; low-ability pleasure begins changing | branch-scoped evidence for desire-to-improve transition |
| `P3-C[HIRO]` | Series 3 four fragments | selection failure, selection normal, final failure, final normal | **conditional result fragments only**; no complete P3 route exists in Source Lock 1.0 |
| `D-HIRO` | Dear 021-037 | winter H.I.F. path culminating in Dear 036 Prima Stella | distinct longitudinal authority; victory does not overwrite P3-C failure branches |
| `M-HIRO` | Produce Events / idol commus / live / startup | modular ordinary-life, song/image, work and social evidence | use as compatible trait/relationship evidence only when continuity does not require a specific result state |

P3 failure fragments are analytically valuable because they prove that separation/ending has become genuinely frightening. They must not be read as having occurred in the same result state as D-HIRO's Prima Stella victory.

## Phase 3 — Rinami branch divergence

- **P1[RINAMI]**: coherent Series-1 route; late-blooming third-year, produced-natural onee-san strategy, technical recovery, public validation.
- **P2[RINAMI]**: coherent Series-2/N.I.A. result progression; competition becomes desirable without erasing care.
- **P3-C[RINAMI]**: Source Lock 1.0 contains only four conditional result fragments: `selection-failure-01`, `selection-normal-02`, `final-failure-01`, `final-normal-02`. Treat as result-state evidence only.
- **D-RINAMI**: Dear 001–037 longitudinal route; includes summer-H.I.F. loss/homecoming, H.O.F., and Dear 036 Prima Stella. **Do not merge Dear 036 into P3-C result states.**
- **M-RINAMI**: Produce Events, CIDOL/song commus, live/growth/startup provide modular evidence; assign to longitudinal chronology only when explicit.
- Explicit Dear 037 confession/vow is D-RINAMI authority. Do not silently project that exact outcome into every modular or conditional state.

## Phase 3 — Sumika branch divergence

- **P1[SUMIKA]**: coherent Series-1 route; strategic noninvestment gradually gives way to owned frustration, renewed training and top-idol intent.
- **P2[SUMIKA]**: coherent Series-2/N.I.A. result progression; public success and seriousness are established without guaranteeing one exact result grade globally.
- **P3-C[SUMIKA]**: Source Lock 1.0 contains only four conditional result fragments: `selection-failure-01`, `selection-normal-02`, `final-failure-01`, `final-normal-02`. Treat as result-state evidence only.
- **D-SUMIKA**: Dear 001–037 longitudinal route; summer selection loss, body reconstruction, REVERSI, public trauma disclosure and Dear 036 Prima Stella. **Do not merge Dear 036 into P3-C failure states.**
- **M-SUMIKA**: Produce Events, CIDOL/song commus, live/growth/startup supply modular trait, song, relationship and work evidence; assign chronologically only when internally anchored.
- P3 selection-failure explicitly allows the REVERSI unit/promise to end in that result state; P3 final-failure instead has Sumika and Lilja make a new next-year rivalry promise. These outcomes must not be sequenced as one history.


## Phase 3 — Ume branch divergence

- **P1[UME]**: coherent Series-1 Produce route; supplementary-admit beginning, slow-start development, Saki-centered competitive orientation and early fan-facing correction.
- **P2[UME]**: coherent Series-2/N.I.A. result progression; winning/losing etiquette and broader public competition deepen Ume's rivalry ethics.
- **P3-C[UME]**: Source Lock 1.0 contains only four conditional result fragments (`selection-failure-01`, `selection-normal-02`, `final-failure-01`, `final-normal-02`). Treat as result-state evidence only; **do not fabricate a complete Series-3 route**.
- **D-UME**: Dear 001–037 longitudinal trajectory; includes equality/fear, victory over Saki, post-pursuit individuation, H.I.F. development and Dear 036 Prima Stella. Do not merge D-UME victory into P3-C.
- **M-UME**: Produce Events, CIDOL/song commus, live/growth/startup provide modular relationship, body, song, fan and family evidence; place longitudinally only when internally anchored.
- Dear 036–037's `world's strongest idol` formulation is D-UME authority, not a universal endpoint automatically inherited by every result branch.

## Phase 3 — Misuzu branch divergence

- **P1[MISUZU]**: coherent Series-1 Produce route; post-SyngUp! state, self-paced developmental contract, selective effort and early solo formation.
- **P2[MISUZU]**: coherent Series-2/N.I.A. progression; jealousy, public competition and social/rival pressure become more explicit.
- **P3-C[MISUZU]**: Source Lock 1.0 contains only four conditional result fragments. Treat them as result-state evidence only; **do not fabricate a complete Series-3 biography**.
- **D-MISUZU**: Dear 001–037 longitudinal trajectory; includes Temari/Rinha reconfiguration, H.I.F. defeat, wrong-path overtraining, Producer mutuality and Dear 036–037 Prima Stella/night-sky summit. D-MISUZU outcomes do not automatically overwrite P3-C.
- **M-MISUZU**: Produce Events, six CIDOL/song-commu clusters, live/growth/startup provide modular work, care, song, fan and unit evidence; place longitudinally only when internally anchored.
- The temporary-unit/Begrazia material does not imply permanent SyngUp! restoration; unit membership is modular and can coexist with solo identity.

## Juo Sena branch and state controls - Phase 3

| track | source count | permitted use | prohibition |
| --- | ---: | --- | --- |
| `P1[SENA]` | 31 Produce Story objects | early ceiling, perfect-image management, failure/normal/true-labeled response space | do not assemble mutually exclusive outcomes into one biography |
| `P2[SENA]` | 11 N.I.A. objects | external legitimacy, strategy, recognition, stat-defying performance, changed loss response | do not treat one result branch as universal ranking fact |
| `D-SENA` | Dear 001-027 | strongest longitudinal developmental spine from retirement plan to generative supremacy | do not overwrite P1/P2 branch states mechanically |
| `M-SENA` | CIDOL, Produce Events, live, growth, startup | modular character, work, song, relationship, and institutional evidence | exact chronology remains source-specific |
| `P3[SENA]` | 0 | none | do not invent or infer a Series-3 Produce Story route from other characters' routes |

**True-labeled caution:** `ending-true-01` supports a true-labeled P1 state, including intensified possession/history language. It does not authorize treating all P1 results, Dear, and later modular stories as one literal uninterrupted sequence.

**Cross-track invariant:** Sena's competence, command, measurement habit, possessive recognition, fear of stagnation, and hunger for meaningful opposition recur across state families. The meaning of retirement, loss, and ownership changes substantially by track and development stage.

## Tsubame branch controls — 2026-08-16

- `P1[TSUBAME]` = 31 Series-1 Produce Story objects.
- `P2[TSUBAME]` = 11 Series-2/N.I.A. Produce Story objects.
- `D-TSUBAME` = Dear 000–027 longitudinal route.
- `M-TSUBAME` = modular song/idol communications.
- **No Series-3 Produce Story is present in Source Lock 1.0. Do not create or cite `P3-C[TSUBAME]` from absence.**
- Dear's summer/winter H.I.F. state must not be projected automatically into P1/P2 chronology where the source does not establish equivalence.
- `クライアイ` can inform thematic/voice analysis across the character model but remains modular unless a stronger placement is established.

