---
title: "Gakuen Idolmaster V2 Continuity and Story-State Map"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "reader-oriented continuity reconstruction"
version: "2.1"
phase: "1 - Continuity and Story-State Reconstruction"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 1 artifact; institutional-level clarification 2026-08-15"
---

# GKM CONTINUITY AND STORY-STATE MAP

## 0. Phase 1 finding

The V2 corpus does **not** describe one universally mergeable timeline. It contains:

1. a clearly ordered **Produce macro-spine**—Series 1 (`初`) → Series 2 (`N.I.A.`) → Series 3 (reformed winter `H.I.F.`);
2. thirteen parallel character-specific Produce routes in Series 1 and Series 2;
3. multiple, mutually exclusive Series 3 world states;
4. a separately coherent Unit Story track running from the entrance ceremony to an old-rules summer H.I.F.;
5. modular Dear Idol, communication, event, support-card, seasonal, live, and Produce-event material whose exact cross-track placement varies in confidence.

The governing conclusion is:

> **Gakumas has a shared institutional history, but not one additive biography for the Producer, every idol, every audition result, and every reigning Prima Stella.**

Future analysis must therefore name both the **story state** and the **continuity track** whenever a claim depends on route history.

---

## 1. Scope and notation

### 1.1 Source basis

This map is grounded in Source Lock 1.0:

- upstream commit `00d150a069a3ffa723a1ff264752ba242024caad`;
- revision `32`;
- 3,777 raw ADV scripts;
- 93,924 extracted message lines.

The main continuity evidence comes from:

- `transcripts_raw/01_produce_main_story/`;
- `transcripts_raw/09_produce_system_and_growth/`;
- `transcripts_raw/12_unit_story/`;
- the corresponding dialogue-only and analysis-bundle views;
- Phase 0's adjudicated shared/system exceptions.

### 1.2 Track notation

| track | meaning |
| --- | --- |
| `P1[IDOL]` | Series 1 Produce route for one selected idol; goal is the regular performance `初` |
| `P2[IDOL]` | Series 2 Produce route for that idol; N.I.A. competition |
| `P3-C[IDOL]` | Series 3 common winter-H.I.F. world state, with Sena as reigning champion/top idol |
| `P3-SAKI` | Saki-specific Series 3 world state, with Ume as reigning Prima Stella and Sena as former champion |
| `P3-REVERSI` | REVERSI-specific Series 3 H.I.F. final-exposition branch |
| `U1` | Unit Story 01: entrance ceremony → Re;IRIS/Begrazia → old-rules summer H.I.F. |
| `M-*` | modular source whose placement is evaluated independently: Dear Idol, event, support, communication, etc. |

`[IDOL]` is essential. The thirteen Produce routes are parallel alternatives. They are not evidence that one Producer simultaneously completed thirteen separate one-idol biographies.

---

# 2. Corpus topology

## 2.1 Produce Story coverage

| Produce series | files | message lines | character coverage | shared/special coverage |
| --- | ---: | ---: | --- | --- |
| Series 1 | 406 | 9,081 | all 13 idols, 31 files each | 3 common files |
| Series 2 | 147 | 2,078 | all 13 idols, 11 files each | 4 common files |
| Series 3 | 55 | 467 | 10 idols with individual result fragments; Saki has 2 additional world-explanation files | 12 common files + 1 REVERSI file |

Series 3 has no individual `pstory_003` owner folder for Kotone, Sena, or Tsubame in Source Lock 1.0. This is a **snapshot-coverage fact**, not proof that those characters have no relevance to H.I.F. or no later story.

## 2.2 Unit Story coverage

`unit_01` contains 66 scripts / 4,525 messages:

| episode | scripts | messages | principal span |
| --- | ---: | ---: | --- |
| Episode 1 | 14 | 979 | entrance ceremony and formation of the Saki/Temari/Kotone unit |
| Episode 2 | 15 | 1,024 | H.I.F. plan, April/May Selection, roles, cohabitation, ordinary unit formation |
| Episode 3 | 12 | 885 | Worst Three, Begrazia, Re;IRIS naming, first live, challenge for the next Selection |
| Episode 4 | 25 | 1,637 | Re;IRIS–Begrazia Selection, defeat/recovery, summer H.I.F., Re;IRIS victory, Saki as summer Prima Stella |

---

# 3. Produce macro-spine

## 3.1 Series 1 — the regular performance `初`

### Fixed institutional premise

Source:

`adv_pstory_001_cmmn_world-explanation.txt`

Raw path:

`transcripts_raw/01_produce_main_story/series_001/cmmn=Common_-_shared/world-explanation.txt`

Asari explains that the target is Hatsuboshi's recurring performance `初`. Passing the intermediate and final exams permits participation, while main-stage performance requires stricter conditions and the final result is especially important.

Continuity status:

- institutional rule: `C0 @ P1`;
- progression from preparation to intermediate exam to final exam: `C1 @ P1`;
- actual exam outcome: `C3`.

### Provisional route order

```text
P1 world explanation
  -> route-start dialogue pool
  -> first development interval / one conditional scene pool
  -> pre-intermediate-exam scene
  -> intermediate result
       |- failure endpoint / failed run state
       `- one of four successful result grades
            -> second development interval / one conditional scene pool
            -> pre-final-exam scene
            -> final result
                 |- failure state
                 `- one of four successful result grades
                      -> result-conditioned ending pool
                           |- normal-labeled endpoints
                           `- true-labeled endpoint
```

This diagram is an event-state model, not a claim that every file in a 31-file bundle plays sequentially.

### Why the bundle is not a 31-scene chronology

For each idol, Series 1 contains:

- 5 `opening-normal-*` files;
- 2 `opening-true-*` files;
- 3 `after-step-1-normal-*` files;
- 3 `after-step-2-normal-*` files;
- intermediate failure plus 4 normal result files;
- final failure plus 4 normal result files;
- 5 normal endings plus 1 true-labeled ending.

Several of these are conditional pools or mutually exclusive result grades. Saki's final normal-result files explicitly range from `最高の結果` to `ギリギリの結果`; they cannot all describe the same run.

### True-labeled status

`true` is retained as a source label. It does not establish that every other outcome is non-canonical. The safe formulation is:

> **Series 1 true-labeled achievement branch.**

### Series 1 endpoint rule

A later character monograph may use all outcomes to reconstruct a character's possibility-space, but a biographical summary must select or explicitly bracket the branch.

---

## 3.2 Series 2 — N.I.A.

### Direct precedence from Series 1

Source:

`adv_pstory_002_cmmn_world-explanation.txt`

Raw path:

`transcripts_raw/01_produce_main_story/series_002/cmmn=Common_-_shared/world-explanation.txt`

The Producer states:

> `定期公演で結果を出したいま、彼女には次の目標が必要ですから。`

This directly places N.I.A. after a **successful Series 1 regular-performance state**. It does not identify one exact Series 1 rank or require the true-labeled maximum result.

Continuity status:

- `P1-success -> P2`: `C1`, high confidence;
- exact predecessor grade: unresolved and branch-dependent.

### N.I.A. fixed rules

The shared exposition establishes:

- `N.I.A.` = `NEXT IDOL AUDITION`;
- a joint competition among multiple idol-training schools;
- multiple auditions during the competition period;
- non-Hatsuboshi students as rivals;
- fan-vote totals as qualification requirements for some auditions;
- N.I.A. ranking determined by fan votes;
- only the top three may enter the public FINALE audition;
- audience voting as part of judging;
- the Producer's responsibility for increasing the idol's N.I.A. popularity before the audition;
- N.I.A. as an idol/Producer `タッグマッチ`;
- the large goal: win the FINALE and perform the victory live.

These are `C0 @ P2` rules.

### Provisional route order

```text
successful P1 state
  -> N.I.A. world explanation
  -> character opening
  -> audition stage A
       -> one of two successful result presentations
  -> audition stage B
       -> one of two successful result presentations
  -> ranking / qualification threshold
       |- mid-route failure state
       `- final-audition access
            -> final result
                 |- failure
                 |- normal success
                 `- true-labeled system result: FINALE first place
            -> result-conditioned ending/live wrapper
```

The corpus exposes the competition architecture more clearly than the exact runtime threshold logic. The exact mapping among audience vote, ranking, each intermediate result file, and the terminal endpoint remains a character-pass verification task.

### Series 2 branch labels are distributed across source families

The highest Series 2 state is not expressed uniformly in character `pstory` filenames. Shared `presult` contains:

`adv_presult_002_final-true-01.txt`

whose Producer line explicitly says the idol took first place at the FINALE. Therefore a character-only file list is insufficient for reconstructing the complete branch system.

---

## 3.3 Series 3 — reformed winter H.I.F.

### Fixed institutional reform

The common world-explanation states that H.I.F. will be renewed in winter after heightened external attention, with:

- stricter participant selection;
- no separate solo and unit divisions;
- three Selection exams;
- a higher cutoff;
- a prescribed-song round and a free-song round in the main tournament;
- aggregated judging across both rounds;
- the overall winner becoming `プリマステラ / 一番星`;
- evaluation not only of idol ability but of the Producer's accumulated production.

Institutional reform status:

- `C0 @ P3`, high confidence;
- Sequence `Selection -> H.I.F. main tournament`: `C1 @ P3`;
- selection and final outcomes: `C3`.

### Series 3 is not one world state

The common route says Sena is the reigning top idol/Prima Stella. The Saki-specific route instead says:

- Ume is the new Prima Stella;
- Sena is a former champion, still called a top idol;
- the Selection chooses challengers to Ume.

These states are mutually exclusive at the same competition moment.

| Series 3 track | reigning champion/world-state fact | status |
| --- | --- | --- |
| `P3-C` | Sena is current Prima Stella/top idol | `C0 within P3-C`; not universal |
| `P3-SAKI` | Ume is current Prima Stella; Sena is former champion | `C0 within P3-SAKI`; mutually exclusive with P3-C |
| `P3-REVERSI` | special unit-aware H.I.F. exposition; current champion not named in that special file | branch-specific; inherit no champion fact without another source |

This is the strongest direct proof in Phase 1 that Gakumas requires **track-scoped continuity**.

### Series 3 route order

```text
route-scoped reigning-champion state
  -> winter H.I.F. reform exposition
  -> Selection exam 1
  -> Selection exam 2
  -> Selection exam 3
       |- selection failure
       `- selection success
            -> H.I.F. main-tournament exposition
            -> prescribed song: ガラクタロード
            -> free song selected/refined for the idol
            -> aggregate judgment
                 |- final failure
                 |- non-winning/normal completion state
                 `- true-labeled Prima Stella state
```

The source fragments are composed across common and character-owned files. Numeric suffixes such as `normal-01`, `normal-02`, and `normal-03` are sometimes technical sequence positions rather than result grades. For example, `selection-01-normal-01` contains Asari's pre-exam encouragement, the character-owned `selection-normal-02` supplies character material, and `selection-01-normal-03` is staging-only. Filename interpretation must therefore be **family-specific**.

### Participant coverage under Source Lock 1.0

Individual Series 3 result fragments exist for:

- Mao;
- Misuzu;
- Rinami;
- Saki;
- Ume;
- China;
- Lilja;
- Hiro;
- Sumika;
- Temari.

Kotone, Sena, and Tsubame lack individual `pstory_003` folders in this frozen snapshot. Their absence is recorded as corpus incompleteness, not converted into an in-world exclusion.

---

## 3.4 Strength of the Produce ordering

| relation | status | evidence strength |
| --- | --- | --- |
| `P1[IDOL] -> P2[IDOL]` | established | direct Series 2 statement that the idol has obtained results at the regular performance and needs a next goal |
| `P2[IDOL] -> P3[IDOL]` | provisional intended macro-order | source-series numbering, escalating institutional scope, and winter H.I.F. culmination support it; no shared line explicitly says “after N.I.A.” |
| one idol's P-route -> another idol's P-route | not additive | parallel Producer assignments; combine only shared institutional facts or independently repeated traits |
| one result branch -> all other result branches | prohibited | mutually exclusive performance outcomes |

The intended macro-spine is therefore retained as:

> **Series 1 → N.I.A. → reformed winter H.I.F.**

but with the bridge into Series 3 explicitly route-scoped.

---

# 4. Unit Story placement

## 4.1 Internal chronology

`U1` begins on the entrance-ceremony day and proceeds in a continuous ensemble narrative:

```text
entrance ceremony
  -> Producer meets Ume and Saki
  -> Producer gathers Saki, Temari, and Kotone
  -> unit agreement
  -> April-end H.I.F. Selection
  -> cohabitation, roles, leader/center work
  -> Ume/China/Hiro and Begrazia formation
  -> Re;IRIS naming and first live
  -> next-month Selection: Re;IRIS vs Begrazia
  -> Re;IRIS defeat and recovery
  -> preparation for the summer H.I.F.
  -> Re;IRIS wins the unit division
  -> Saki is named the summer Prima Stella
```

This is `C1 @ U1` throughout, except for any embedded hypotheticals or memories that require their own labels.

## 4.2 Direct calendar anchors

The Unit Story explicitly provides:

- entrance-ceremony start;
- Selection at the end of April and end of May;
- H.I.F. as a summer event;
- Saki describing herself as still only roughly half a year into enrollment;
- Sena's approaching graduation;
- Saki named `夏のプリマステラ`.

## 4.3 Old-rules H.I.F.

The Unit Story H.I.F. has separate unit and solo structures:

- Re;IRIS wins the unit division;
- afterward, one Re;IRIS member and the solo winner are considered for the final Prima Stella live;
- Saki becomes summer Prima Stella.

Series 3 explicitly abolishes the solo/unit division. Therefore:

> **At the institutional-rule level, U1's old-rules summer H.I.F. precedes the reformed winter H.I.F. of Series 3.**

This is a strong chronology link between institutional states.

## 4.4 Why U1 is still a separate continuity track

U1 cannot simply be pasted into every Produce biography because:

1. the Producer simultaneously produces Saki, Temari, and Kotone, while individual Produce routes center one selected idol;
2. Re;IRIS and Begrazia formation determine relationship history unavailable as a universal premise in every solo route;
3. U1 ends with Saki as summer Prima Stella;
4. Series 3 branches instead begin with either Sena or Ume as the reigning champion;
5. Source Lock 1.0 contains no universal transition that reconciles all champion successions and Producer assignments.

The safe model is:

- `U1` is internally fixed and narratively substantive;
- it shares institutional history and many character premises with the broader corpus;
- its route-exclusive events remain `U1` biography unless another source explicitly imports them.

---

# 5. C0-C4 continuity model, revised for track scope

## 5.1 C0 — fixed anchor **within a named scope**

Use for explicit institutional rules, fixed premises, or world-state facts.

Examples:

- N.I.A. top-three qualification for FINALE: `C0 @ P2`;
- reformed winter H.I.F. uses prescribed/free rounds: `C0 @ P3`;
- Ume is reigning champion: `C0 @ P3-SAKI`, not global;
- Sena is reigning champion: `C0 @ P3-C`, not global.

**C0 does not mean universal across mutually exclusive routes.**

## 5.2 C1 — strong longitudinal state

Use when a source explicitly succeeds or precedes another state.

Examples:

- Series 2 follows a successful regular performance;
- Unit Story part order;
- Selection success precedes H.I.F. final;
- parts within one event or support story.

## 5.3 C2 — compatible floating state

Use when a source can coexist with a track but exact placement is not established.

Examples:

- a Dear Idol episode with clear developed rapport but no named competition/date;
- an event compatible with first-year school life but not tied to a specific Produce stage.

## 5.4 C3 — branch or conditional state

Use for mutually exclusive outcomes, selected scenes, route-specific world states, or system-conditioned variants.

Examples:

- failure versus successful audition outcomes;
- multiple result grades;
- true-labeled versus normal endpoints;
- `P3-C` versus `P3-SAKI` champion state;
- Produce-event scenes selected by run conditions.

## 5.5 C4 — flexible side continuity

Use when characterization is valuable but literal chronological integration should remain cautious.

Examples:

- most support-card stories before individual audit;
- seasonal/startup scenes;
- modular comedy or everyday-life material whose route compatibility is deliberately broad.

## 5.6 Dual labeling

A source may carry two useful labels at different levels:

- `C1 within event_014`, but `C2 relative to P2`;
- `C0 institutional rule within P3-SAKI`, but `C3 when compared with P3-C`;
- `C1 within U1`, but `track-exclusive` relative to individual Produce biography.

The ledger therefore records both **continuity class** and **track scope**.

---

# 6. Modular source placement

| source family | internal ordering | default cross-track class | rule |
| --- | --- | --- | --- |
| Tutorial | ordered parts | C0-C1 | shared entry/world premise unless contradicted by route setup |
| Produce main story | strong within selected route | C0/C1/C3 | principal P-track evidence; branch label mandatory |
| Produce events | conditional pools | C3, sometimes C2 | do not assume every scene occurs in one run |
| Dear Idol | numeric/part order within its own sequence | C2 by default | promote to C1 only through explicit predecessor/date/state references |
| Idol communications | parts within an episode are C1 | C2/C4 across episodes | rank/unlock metadata is not automatically calendar chronology |
| Story events | parts within an event are C1 | C2 by default | event ID/release order does not by itself establish in-world order |
| Support-card stories | parts within a story are C1 | C4 by default | strong relational evidence; exact placement requires anchors |
| Unit Story | complete internal sequence | C1 @ U1 | separate ensemble continuity track |
| Startup/seasonal | date or occasion anchored | C4 | calendar occasion can be explicit while route integration remains flexible |
| Live/result scenes | result-conditioned | C3 | performance wrapper belongs to a route outcome |
| Produce system/growth | system-conditioned | C3/SYSTEM | promote institutional lines to C0/C1 as Phase 0 did |
| Tower/request-system | institutional introduction | C0/C2 | fixed system, floating exact date |

Known promotion:

- Event 001 opens with first-year class introductions and therefore receives a provisional early-school `C1/C2` placement rather than an undifferentiated C4 label.

No other numbered event is assigned an exact date during Phase 1 without direct evidence.

---

# 7. False-biography prohibitions

The following constructions are prohibited unless later source evidence supplies a bridge:

1. **All thirteen solo Producer relationships happened to one Producer in sequence.**
2. **Every failure, normal, and true-labeled result happened to one idol.**
3. **Sena and Ume were simultaneously the reigning Prima Stella in the same Series 3 track.**
4. **Unit Story's Re;IRIS formation is automatically part of every solo Produce route.**
5. **Saki's Unit Story summer championship automatically precedes Saki's Series 3 Ume-champion world state.**
6. **Numerical suffixes have one universal meaning across filename families.**
7. **Support-card or seasonal material has an exact date because it was released later.**

Permitted formulations include:

- “Across alternate outcome states, Saki consistently…”
- “In the U1 ensemble continuity…”
- “In Saki's Series 3 branch, Ume is the reigning Prima Stella…”
- “The common Series 3 route instead places Sena in that role…”
- “This support story is compatible with a later-developed relationship state, but its exact placement remains floating.”

---

# 8. Open continuity questions carried forward

These do not block Phase 2 or Phase 3, but must remain explicit:

1. The exact runtime mapping from Series 1 final-result grades to the five normal endings is not proven globally.
2. Series 2's hidden thresholds linking audition A/B, fan ranking, FINALE access, and endpoint files require character-by-character verification.
3. Series 3 fragment assembly across common `normal-01/03`, character `normal-02`, and result wrappers is only partially reconstructed.
4. The exact narrative bridge from N.I.A. to each Series 3 champion state is not present in shared exposition.
5. Unit Story's summer champion succession cannot be merged into the common or Saki-specific Series 3 branches without an explicit intermediate source.
6. Dear Idol, communications, events, and support stories require local anchors during their dedicated passes; Phase 1 establishes defaults, not invented dates.
7. Source Lock 1.0's absent Series 3 individual folders for Kotone, Sena, and Tsubame may reflect incomplete live-service coverage.

---

# 9. Phase 1 continuity verdict

The project may now use the following stable shorthand:

```text
PRODUCE MACRO-SPINE:
P1[IDOL] --successful state--> P2[IDOL] --provisional intended continuation--> P3[TRACK]

SERIES 3 TRACKS:
P3-C      = Sena-current world state
P3-SAKI   = Ume-current world state
P3-REV    = REVERSI-special H.I.F. exposition

ENSEMBLE TRACK:
U1 = entrance ceremony -> April/May Selection -> old-rules summer H.I.F. -> Saki summer Prima Stella

MODULAR SOURCES:
placed locally by C0-C4 + track scope; never forced into one master biography.
```

This model is sufficiently stable for the shared/institutional deep reading and later character-core passes. Every later document must preserve track scope whenever a claim depends on route history.


## 11. Educational-level clarification from S1 + paratext

This clarification does **not** change the route topology above. It corrects the social/institutional placement of the player Producer.

### S1 bounded fact

Independent narrative sources identify GakumasP as `プロデューサー科` first year (`プロデューサー科１年`; `プロデューサー科の1年`; `プロデューサー科1年1組`). Idol-side material separately distinguishes `中等部` and `高等部`, while Temari calls the Producer instructional environment `大学`.

Therefore all tracks should inherit the following institution-level premise unless a future source explicitly creates a contrary track:

> **GakumasP and the idols belong to the wider Hatsuboshi educational system but are not ordinary same-level high-school classmates.**

This is an institutional identity rule, not a chronology bridge. It does not merge P1/P2/P3, Dear, U1, or modular sources.

### External taxonomy

Official paratext confirms the formal `プロデューサー科` label. Credited creator commentary specifies the protagonist's placement as the Producer Course of `初星学園専門大学` and explains that this was selected to create physical proximity without collapsing the Producer's professional/psychological distance. Those claims remain source-labeled S2/S3 in the external register and must not be used to erase S1 ambiguity elsewhere.
