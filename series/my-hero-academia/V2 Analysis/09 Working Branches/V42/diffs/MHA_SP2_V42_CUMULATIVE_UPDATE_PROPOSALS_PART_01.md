---
series: MHA
corpus: MHA_SP2
artifact_type: cumulative_update_proposals
scope: V42
generation: V2
method_generation: V2.1
status: PROVISIONAL
source_boundary: Japanese manga Volume 42, narrative V42:p005-p183
do_not_use_as_current_authority: true
apply_ready: false
dependency: V41 provisional tranche must be promoted/reconciled before exact V42 patches are generated
---

# MHA SP2 Volume 42 — Cumulative Update Proposals

## Responsibility

This document preserves the **semantic content** that Volume 42 should contribute to the cumulative MHA V2 corpus.

It is intentionally **not** an apply-ready Git patch.

Because Volume 41 remains provisional, the current canonical target blobs still represent a V40 high-water mark. Exact V42 patches generated against those blobs would be unsafe: promoting V41 would immediately invalidate their base state.

During a future authorized promotion, use this document as the semantic checklist, fetch the then-current target files, and integrate V42 after V41 in chronological order.

---

# 1. Class 1-A Character State Ledger

## Midoriya Izuku

Add terminal/adult state:

- Final Shigaraki relation is not a simple “successful rescue”: Midoriya defeats AFO's controlling trajectory, reaches Tomura, and preserves accountability, but explicitly says he could not save Tenko's **life**.
- Keeps the distinction between recognizing Tomura's personhood and forgiving his acts.
- OFA embers survive immediately, then extinguish; Midoriya remains psychologically/behaviorally continuous through a Quirkless adult interval.
- Adult vocation: U.A. teacher by choice, not merely incapacity.
- Support suit restores direct hero activity without displacing teaching.
- Adult decision policy remains possibility-oriented: notices/encourages younger people who reach out.
- Adult blind spot: universal concern can obscure particular personal wants.
- Bakugo explicitly identifies self-undervaluation as a perception problem.
- Midoriya finally names a relationship-specific desire for more contact with Ochako.

Suggested readiness: retain `specialist_ready`.

## Bakugo Katsuki

Add:

- emotional reaction to Midoriya's return toward Quirklessness shows childhood status logic reversed;
- central long-term support for Midoriya's hero suit;
- adult rivalry remains competitive but no longer requires Midoriya's degradation;
- recruitment/status language remains recognizably Bakugo;
- final Midoriya advice: he must value himself more highly to notice what he is missing;
- blunt speech style persists while prosocial/relational function changes.

Suggested readiness: retain `specialist_ready`.

## Uraraka Ochako

Add:

- postwar Toga grief is concealed behind social smiling;
- receives rather than only provides emotional support;
- adult Quirk-counseling work is both Toga-informed and self-chosen;
- internalized/apparitional Toga remains psychologically consequential;
- literal postmortem vestige mechanism is not established;
- adult relation with Midoriya moves from reciprocal care to explicitly mutual desire for more contact;
- self-directed desire becomes a final developmental task.

Suggested readiness: retain `specialist_ready`.

## Todoroki Shoto

Add:

- terminal conversation with Toya prioritizes ordinary personhood (favorite food) over forced ideological reconciliation;
- explicitly says Class A support allows him to become what he wants;
- adult identity is no longer primarily narrated through Endeavor;
- discovers that he likes eating;
- explicitly recognizes a self beyond `なりたい自分`;
- chooses craft/travel around personal preference;
- later Toya memorial reference integrates grief into ordinary adult life.

Suggested readiness: retain `specialist_ready`.

## Aoyama Yuga

Add:

- treats accountability as a long repair path from negative toward zero/equality rather than instant forgiveness;
- institutional departure/transition does not become permanent moral exclusion;
- prosocial self-authorship remains possible after coerced betrayal.

Suggested readiness: retain `strong`.

## Shinso Hitoshi

Add:

- formal hero-course inclusion closes the institutional transition from Quirk-based prejudice/structural mismatch toward trained role competence.

Suggested readiness: retain `strong` pending broader adult/private evidence.

## Shoji Mezo

Add:

- postwar anti-discrimination/professional continuity demonstrates that V37's normative position becomes durable adult action;
- re-evaluate whether new adult/professional breadth closes the V40 `moderate` -> `strong` gate.

Do not auto-promote without reviewing the exact canonical entry plus V41 effects.

## Class A cohort

Add cohort-level adulthood atoms:

- adult contact is intermittent because careers/schedules differ;
- group familiarity, teasing, ranking talk, and joint response persist;
- maturation does not mean personality convergence;
- the cohort remains a support network without requiring constant co-presence.

---

# 2. U.A. Students / Staff Character State Ledger

## Midoriya as staff-role cross-link

Keep Midoriya's canonical character home in Class 1-A if that is the established ledger convention, but cross-link his adult role:

- U.A. teacher;
- uses outreach/education to transmit hero experience;
- remains teacher after support-suit hero activity begins;
- teaching is explicitly self-chosen.

## Shinso

Cross-link formal hero-course transition if this ledger owns institutional role changes.

## U.A. as postwar institution

Record only behaviorally useful state:

- resumes education under postwar conditions rather than suspending young people indefinitely inside emergency identity;
- remains a site where trained professionals and former students can transmit experience.

Avoid turning the group ledger into a Hero Society synthesis.

---

# 3. Pro Hero Character State Ledger

V42 now supplies enough adult/professional endpoint material that this ledger should no longer be screened out as V41 did.

## All Might

Add:

- post-Symbol role becomes mentor/network facilitator rather than retired irrelevance;
- pluralizes `最高のヒーロー`;
- helps return Midoriya to frontline capacity through social/technical inheritance;
- does not claim ownership over what Midoriya will do with the suit.

Suggested readiness: retain `specialist_ready`.

## Endeavor

If Endeavor's canonical home is Pro Hero ledger, add:

- professional retirement/end-state is subordinated to family restitution;
- final duty language concerns lifetime compensation/apology rather than restoration of status.

If the ledger convention keeps his family-state details in the Pro Hero entry, cross-reference rather than duplicate full family analysis.

## Postwar professional field

Add compact system-facing atoms only where they attach to named professionals:

- hero work remains necessary but is changing as social conditions improve;
- adult heroes maintain rankings/status competition without rankings exhausting their social value;
- professional response now operates inside a wider preventive ecology.

Do not use a group character ledger to duplicate the Hero Society ledger.

---

# 4. Villain / Antagonist Character State Ledger

## Shigaraki Tomura / Shimura Tenko

Add final state:

- AFO control is defeated enough for Tomura to re-emerge distinctly;
- Tomura retains adult identity, Spinner concern, and League relational continuity;
- asks to be remembered as `死柄木弔`;
- dies before rehabilitation becomes possible;
- Midoriya does not forgive his acts;
- rescue result must distinguish life, heart, identity, possession, and accountability.

Suggested readiness: retain `specialist_ready`.

## All For One

Add:

- Midoriya directly rejects Demon Lord self-mythology;
- AFO's final Yoichi attachment is explicit, emotionally intense, and still permission/ownership structured;
- vulnerability does not produce reciprocity;
- final model should not call him affectless.

Suggested readiness: retain `strong`; ordinary reciprocal relationship breadth remains missing.

## Spinner

Add:

- surviving witness/prisoner role;
- `死柄木弔は俺のヒーローだった`;
- counterfactual self-questioning about whether he could have done more;
- chooses writing/history preservation;
- explicitly refuses erasure of the past while not being shown simply resuming violent action.

Suggested readiness: retain `strong`, very strongly strengthened.

## Toga

Do not add Chapter 431 apparition speech as independent new Toga behavior without an epistemic tag.

Safe update:

- Toga's pre-death acts remain causally active in Ochako's adult self-model.
- Ochako speculates about a possible OFA-like internal remainder; literal mechanism remains unresolved.

Toga remains `specialist_ready` from canonical V39 evidence; V42 mainly changes postmortem relational impact, not Toga's own observed behavior.

## Kurogiri / Shirakumo

Add:

- endpoint does not restore a pure pre-Nomu Shirakumo identity;
- terminal action remains Shigaraki-oriented and strengthens mixed-continuity interpretation.

Suggested readiness: retain `moderate`.

---

