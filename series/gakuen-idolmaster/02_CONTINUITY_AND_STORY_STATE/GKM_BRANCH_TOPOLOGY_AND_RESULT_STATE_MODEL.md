---
title: "Gakuen Idolmaster V2 Branch Topology and Result-State Model"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "branch topology specification"
version: "2.0"
phase: "1 - Continuity and Story-State Reconstruction"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 1 artifact"
---

# GKM BRANCH TOPOLOGY AND RESULT-STATE MODEL

## 0. Purpose

This document defines how the V2 project reads branching Produce material without converting alternate outcomes into a false linear biography.

The core distinction is:

> **A script can be authentic primary evidence without being sequentially compatible with every other authentic script.**

---

# 1. Filename semantics are local, not universal

A major Phase 1 correction is that technical suffixes must be interpreted by source family.

## 1.1 Result-grade example

In Saki's Series 1 final results:

- `after-audition-final-normal-01` says `最高の結果`;
- `...normal-02` says `素晴らしい結果`;
- `...normal-03` says `まずまずの結果`;
- `...normal-04` says `ギリギリの結果`.

Here `normal-01` through `normal-04` are mutually exclusive result grades.

## 1.2 Technical-sequence example

In Series 3 Selection:

- `selection-01-normal-01` contains shared Asari pre-exam dialogue;
- the character-owned `selection-normal-02` supplies character material;
- `selection-01-normal-03` can be staging-only.

Here the numeric suffix participates in runtime composition rather than denoting four ranks.

## 1.3 Governing rule

Never infer branch meaning from `normal`, `true`, `failure`, or a trailing number alone. Confirm through:

1. source content;
2. neighboring source families;
3. shared result/system wrappers;
4. repeated patterns across characters;
5. runtime/video evidence if composition remains unclear.

---

# 2. Branch vocabulary

| term | use |
| --- | --- |
| invariant | reproduced across mutually exclusive states |
| conditional | true only if a result, choice, or route condition is met |
| result grade | success tier distinguished by explicit evaluation language |
| terminal failure | run/state endpoint that blocks the current objective |
| true-labeled | source/game label; not a declaration of sole canon |
| world-state branch | route changes a shared fact such as the reigning champion |
| composition fragment | common/character/system file assembled into one runtime scene |
| track-exclusive biography | event is biographical only inside its named continuity track |

---

# 3. Series 1 topology

## 3.1 Uniform corpus template

All 13 idols have 31 Series 1 files. The family-level inventory is:

| family | per idol | corpus total |
| --- | ---: | ---: |
| opening normal | 5 | 65 |
| opening true-labeled | 2 | 26 |
| after step 1 | 3 | 39 |
| pre-intermediate exam | 1 | 13 |
| intermediate failure | 1 | 13 |
| intermediate normal grades | 4 | 52 |
| after step 2 | 3 | 39 |
| pre-final exam | 1 | 13 |
| final failure | 1 | 13 |
| final normal grades | 4 | 52 |
| normal endings | 5 | 65 |
| true-labeled ending | 1 | 13 |

Shared files add the world explanation and hard-state wrappers.

## 3.2 Structural graph

```text
START
  -> one opening-state fragment
  -> one step-1 character fragment
  -> MID EXAM
       |- FAIL-MID: terminal failed objective state
       `- PASS-MID: one of four explicit success grades
            -> one step-2 character fragment
            -> FINAL EXAM
                 |- FAIL-FINAL
                 `- PASS-FINAL: one of four explicit success grades
                      -> result-conditioned normal or true-labeled ending
```

## 3.3 Interpretation rules

- Opening files are a route-start pool, not five consecutive mornings in a mandatory biography.
- Step files are conditional character-development views; use them as possibility-space evidence unless runtime order is known.
- Intermediate and final result grades are mutually exclusive.
- Failure scenes are valid evidence for coping style but not events in the successful biography.
- Ending files cannot be merged into a composite ending.
- The mapping between each result tier and every ending number must be verified locally; the filename list alone is insufficient.

## 3.4 Branch-safe character claim

Safe:

> In both high-result and low-result states, Saki immediately evaluates the gap between her current performance and her desired standard.

Unsafe:

> Saki first barely passed, later achieved a middling result, then achieved the highest result in the same Series 1 run.

---

# 4. Series 2 / N.I.A. topology

## 4.1 Uniform corpus template

All 13 idols have 11 Series 2 files:

- one opening;
- one pre-audition-A scene;
- two audition-A success presentations;
- one pre-audition-B scene;
- two audition-B success presentations;
- one mid-route failure;
- one final failure;
- one final normal-success scene;
- one ending.

The common layer adds three audition-selection wrappers and the N.I.A. world explanation. Shared `presult` adds failure/normal/true-labeled final-evaluation states.

## 4.2 Structural graph

```text
P1 successful performance state
  -> N.I.A. introduction
  -> fan-building / popularity objective
  -> audition A
  -> audition B
  -> ranking and qualification pressure
       |- mid-route failure
       `- FINALE access
            -> final failure
            -> final normal success
            -> true-labeled FINALE-first result
```

The source establishes the existence and order of multiple auditions and FINALE qualification. It does not expose every hidden gameplay threshold in literary dialogue.

## 4.3 Result-state distribution

The branch system spans categories:

- character `pstory`: emotional response and character-specific result dialogue;
- common `pstory`: selection/pre-audition framing;
- `presult`: final evaluation and live eligibility;
- live/system sources: performance wrapper.

A character bundle is therefore not a complete branch map by itself.

## 4.4 Predecessor requirement

N.I.A. directly presupposes that the idol has already obtained results at the regular performance. The safe predecessor is:

> **a successful P1 state**

not necessarily:

> **the unique P1 true-labeled state**.

---

# 5. Series 3 / H.I.F. topology

## 5.1 Composite source structure

Source Lock 1.0 contains:

- common Selection wrappers for exams 1–3;
- common Selection success/result fragments;
- common H.I.F. final fragments;
- 10 idols with individual Selection/final success and failure material;
- Saki-specific Selection and final world explanations;
- a REVERSI-specific final world explanation.

This is a composition library, not 55 independent chronological episodes.

## 5.2 World-state branching precedes result branching

```text
WORLD STATE
  |- P3-C: reigning champion = Sena
  |- P3-SAKI: reigning champion = Ume; Sena = former champion
  `- P3-REVERSI: unit-aware special exposition; champion not fixed by special file alone

THEN
  -> Selection exams 1, 2, 3
       |- failure
       `- qualification
            -> H.I.F. main tournament
                 -> prescribed song
                 -> free song
                 -> aggregate result
                      |- failure/non-victory
                      `- Prima Stella true-labeled state
```

The world-state split is not merely an ending variation. It changes whom the idol is challenging before Selection begins.

## 5.3 Common institutional invariants

Across Series 3 branches, the following remain stable unless a later source contradicts them:

- winter H.I.F. reform;
- stricter Selection;
- three Selection exams;
- abolished solo/unit division;
- prescribed and free song rounds;
- aggregate ranking;
- winner becomes Prima Stella;
- Producer's accumulated work is judged through the idol's performance.

## 5.4 Champion-state exclusivity

The statements “Sena is current champion” and “Ume is current champion” are each direct evidence, but only within their route scopes. They must never be averaged into a vague claim that both are current.

## 5.5 Coverage limitation

No individual Series 3 pstory fragments exist for Kotone, Sena, or Tsubame in Source Lock 1.0. This must be represented as `NOT PRESENT IN LOCK`, not `DID NOT PARTICIPATE`.

---

# 6. Unit Story as track-level branch

`U1` is not merely another outcome file. It reorganizes the entire Producer assignment and social architecture:

- Producer assembles Saki, Temari, and Kotone;
- Re;IRIS and Begrazia become central units;
- April and May Selection structure the semester;
- the old-rules summer H.I.F. separates unit and solo competition;
- Re;IRIS wins the unit division;
- Saki becomes summer Prima Stella.

Thus `U1` is a **track-level branch**, internally C1 but externally non-additive with solo Produce biographies.

---

# 7. Branch-safe evidence use

## 7.1 Trait confidence ladder

A character claim becomes stronger when it appears in:

1. multiple mutually exclusive outcomes;
2. multiple source families;
3. both crisis and ordinary-life contexts;
4. both P-track and U-track without requiring identical biography;
5. text and directly inspected performance.

## 7.2 Required prose labels

Use one of:

- “in the failure branch…”
- “in the highest-result state…”
- “across result variants…”
- “within U1…”
- “in the common Series 3 track…”
- “in Saki's Ume-champion Series 3 track…”
- “this appears invariant across the compared branches…”

## 7.3 Biography-safety field

Every branch-ledger entry records:

- `YES`: safe to use as a track-scoped biographical fact;
- `CONDITIONAL`: safe only with branch label;
- `INVARIANT-ONLY`: individual event is exclusive, but repeated trait may be synthesized;
- `NO`: not safe to merge into a biography.

---

# 8. Remaining topology uncertainties

1. Exact Series 1 ending-to-result-tier mapping is not universalized yet.
2. Exact Series 2 runtime thresholds and whether all A/B success variants are grade or condition variants require direct play/video or fuller system reconstruction.
3. Series 3's common/character fragment assembly is understood at the event-state level, not every runtime transition.
4. The unseen prior event that makes Ume current champion in `P3-SAKI` is not supplied by the shared Produce corpus.
5. No source bridges U1's Saki summer championship to every winter-H.I.F. route.

These uncertainties are preserved rather than repaired by assumption.

---

# 9. Phase 1 branch verdict

The branch system is now stable enough for later analysis:

- Source files are primary evidence objects.
- Runtime-compatible sequences are track-scoped.
- Alternate results become possibility-space evidence.
- World-state branches are treated as mutually exclusive.
- `true` remains a label, not a universal canon verdict.
- Numeric suffixes receive family-specific interpretation.
