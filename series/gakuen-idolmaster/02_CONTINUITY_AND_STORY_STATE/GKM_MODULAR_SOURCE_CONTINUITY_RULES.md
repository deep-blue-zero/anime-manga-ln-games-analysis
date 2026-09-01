---
title: "Gakuen Idolmaster V2 Modular Source Continuity Rules"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "source-family placement protocol"
version: "2.0"
phase: "1 - Continuity and Story-State Reconstruction"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 1 artifact"
---

# GKM MODULAR SOURCE CONTINUITY RULES

## 0. Purpose

This document governs continuity placement for source families outside the main Produce and Unit Story spines. Its function is to preserve characterization without inventing exact dates or forcing all material into one route.

---

# 1. Internal order versus global placement

Every source is evaluated on two axes:

1. **internal order** — do parts within this story clearly follow one another?;
2. **global placement** — where, if anywhere, does the completed story fit relative to P1, P2, P3, or U1?

A support story can be `C1 within its two parts` while remaining `C4 relative to the Produce macro-spine`.

---

# 2. Source-family inventory and defaults

| family | files | messages | internal-order rule | default global class |
| --- | ---: | ---: | --- | --- |
| Dear Idol | 462 | 31,438 | numbered sequence/parts are provisional internal order | C2 |
| Idol communications | 321 | 13,616 | parts within an episode are C1 | C2/C4 |
| Story events | 136 | 8,507 | `main-01 -> main-N` is C1 | C2 |
| Support cards | 498 | 9,777 | parts within one story are C1 | C4 |
| Produce events | 1,101 | 13,716 | selected/conditional run scenes | C3, sometimes C2 |
| Startup/seasonal | 31 | 215 | occasion/date explicit | C4 |
| Live scenes | 106 | 194 | performance/result wrapper | C3 |
| Unit Story | 66 | 4,525 | full internal order | C1 @ U1 |

Defaults are starting points, not permanent verdicts.

---

# 3. Dear Idol

## 3.1 Internal order

Dear Idol files are numbered by character, often through `dear_037` in this snapshot, with some split-part files. Numerical order is treated as a provisional within-family sequence.

## 3.2 Global placement

Default: `C2 @ character`.

Promote to `C1 relative to P-track` only when the text explicitly names:

- a prior competition;
- an established relationship milestone;
- a date/season;
- an institutional title;
- a direct predecessor scene.

Do not assume `dear_030` occurs after P3 merely because 30 is larger than 20.

## 3.3 Use

Dear Idol may be central to internal character development. Floating placement does not reduce evidentiary importance; it only limits chronological claims.

---

# 4. Idol communications

## 4.1 Technical organization

The archive sorts communications by character, rank, episode, and part. In Source Lock 1.0, the present files are rank-3 communications with uneven episode coverage by character.

## 4.2 Continuity rule

- parts `01 -> 02 -> 03` within an episode: `C1`;
- order among episode numbers: provisional, verified through content;
- rank/unlock status: not automatically a calendar date;
- global P-track placement: `C2` unless anchored;
- highly modular/casual communication: `C4` if no continuity dependence exists.

---

# 5. Story events

## 5.1 Internal order

Each numbered event's `main-01 -> main-N` sequence is `C1`.

## 5.2 Event-to-event order

Event number and release order are metadata, not sufficient proof of in-world chronology. Default global placement is `C2`.

## 5.3 Known early anchor

Event 001 begins with first-year classmates introducing themselves, Saki and Temari immediately clashing, and Sumika mediating class formation. It is therefore provisionally placed near the early first-year school state:

- `C1 within Event 001`;
- `C1/C2 relative to entrance-era school chronology`;
- not automatically identical to U1's exact sequence of meetings.

## 5.4 Promotion rule

Promote an event when it names:

- N.I.A., H.I.F., Selection, FINALE, or a reigning Prima Stella;
- a prior event's consequences;
- graduation/semester/season;
- a unit already formed;
- a relationship rupture or repair that can be located elsewhere.

---

# 6. Support-card stories

## 6.1 Default

Support stories are `C1 within story`, `C4 globally`.

This is not a “less canon” judgment. It recognizes that support stories are often designed to remain compatible with multiple route states.

## 6.2 Analytical value

They are especially strong for:

- ordinary social behavior;
- food, training, money, health, study, work, and domestic practice;
- forms of address and casual register;
- pair/group relationship grammar;
- side-character participation;
- behavior outside crisis scenes.

## 6.3 Promotion criteria

A support story may become C2 or C1 when it contains direct placement evidence. Otherwise preserve its relational content without inventing a date.

---

# 7. Produce events

Produce events are often selected by activity, parameter, week, or route condition.

Default:

- `C3 @ selected Produce run`;
- `C2` only when the scene is clearly a stable, compatible event rather than a mutually exclusive run selection.

Do not write a biography in which all 80+ Produce-event files for one idol occurred during one finite production cycle.

The correct use is often:

> a catalog of conditional behavior under different work/training contexts.

---

# 8. Seasonal/startup material

A birthday or seasonal line can have a fixed occasion while remaining flexible in route history.

Default:

- occasion: `C0` or `C1` as stated;
- integration with P/U track: `C4`.

Example formulation:

> In a birthday interaction, the character says X; the corpus does not establish whether this is before or after N.I.A.

---

# 9. Live and result scenes

Live-start/end files and `presult` wrappers are tied to performance outcomes.

Default: `C3`.

They may provide:

- exact result framing;
- who speaks after success/failure;
- whether an audience is present;
- eligibility for the performance;
- Producer response;
- Prima Stella/FINALE state.

They must be attached to the corresponding branch rather than treated as free-floating live history.

---

# 10. System and exception material

System categories are not automatically discarded.

Phase 0 already promoted:

- `adv_pstory_003_reversi_world-explanation-final.txt` to shared institutional spine;
- `adv_tower-001.txt` to Hatsuboshi Request System evidence;
- dialogue-bearing `presult` and Produce refresh files to route/transition evidence.

Promotion changes analytical indexing, not the immutable raw path.

---

# 11. Placement decision tree

For every modular story:

```text
1. Is it a mutually exclusive outcome or selected run scene?
   YES -> C3.

2. Does it have ordered parts?
   YES -> C1 within the story object.

3. Does it explicitly name a competition, date, season, title-holder,
   predecessor event, or established unit/relationship state?
   YES -> assign a track-scoped C0/C1/C2 placement.

4. Is it broadly compatible but not precisely locatable?
   YES -> C2.

5. Is it intentionally modular/flexible ordinary-life or seasonal material?
   YES -> C4.
```

Then record cross-track compatibility separately.

---

# 12. Release order rule

Release order may be used as:

- a discovery aid;
- evidence about publication history;
- a tiebreaker when the text already supports progression.

Release order may not alone establish:

- in-world date;
- one universal route;
- that later-released support material occurs after P3;
- that an event ID is chronologically after every lower ID.

---

# 13. Required ledger fields

Each source eventually receives:

- canonical source ID;
- source family;
- internal sequence position;
- track scope;
- C0-C4 class;
- explicit anchors;
- predecessor/successor if known;
- branch/result state;
- cross-track compatibility;
- confidence;
- notes and unresolved conflicts.

---

# 14. Verdict

The modular corpus will be preserved through **local precision**, not forced global chronology. This allows support, event, Dear Idol, and communication material to remain central to character analysis without converting flexible live-service storytelling into an invented master timeline.
