---
title: "GKM Source-to-Analysis Audit — Adversarial Review and Reconciliation Record"
series: GKM
artifact_type: audit
scope: SOURCE_LOCK_1_2_SOURCE_TO_ANALYSIS_AUDIT
generation: V2
status: active_provisional
audit_nature: "non-authoritative retrospective audit; does not itself revise any canonical conclusion (corrections are applied separately through the claim-revision route and recorded in GKM_SOURCE_TO_ANALYSIS_AUDIT_DISPOSITIONS_20261115.md)"
audit_id: GKM-SAA-20261115
source_boundary: "GAKUMAS V2 Source Lock 1.2 — DreamGallery/Campus-adv-txts @ f8ff5ef7b243f2f7e3b2723def31072874539ca9, revision 88; 4,052 raw objects / 103,355 extracted messages; manifest.csv SHA-256 10ad24271fbf7d322284a8364af09ba3551635ea4e793f2046dbdb491ce2c423"
source_lock: GAKUMAS V2 Source Lock 1.2
source_commit: f8ff5ef7b243f2f7e3b2723def31072874539ca9
source_revision: 88
audit_baseline_commit: "176d472a2df2b325f0c54e1c589f7f5e8a89ada9"
created: "2026-11-15"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# F. Adversarial review and reconciliation record

Audit: GKM source-to-analysis audit, 2026-11-15. This record keeps the significant disagreements between specialists, reviewers and the
principal integrator, and how each was decided. Row-level detail is in `F_review_table.md` (all 85 reviews), `03_adversarial_review/R*/reviews.jsonl`
(blind readings, eight-point verification, strongest defenses and reasoning) and `03_adversarial_review/integrator_adjustments.tsv`.

## 1. Review design

- **Who.** Eight reviewers (R01–R08) ran in fresh contexts. None had read or compared sources in Stages A or B.
- **What.** 85 of 292 candidates were reviewed: all 9 proposed P1s, a deterministic ~30% sample of P2s (40) chosen corrective dispositions and low confidence first, and all 36
  P3s with a corrective disposition (misreading, attribution, continuity) or an owner-adjudication flag.
- **How.** The locators were opened first, and the blind reading of A1 was written before the claim was opened. Each finding then got the eight-point check (exists, anchor accurate, speaker
  correct, continuity respected, context considered, counterevidence examined, not already covered, proportionate) and, for every P1, a strongest
  defense of the existing analysis.

## 2. Outcome

| Verdict | n |
| --- | ---: |
| SUSTAIN | 47 |
| QUALIFY | 38 |
| REJECT | 0 |
| OPEN | 0 |

| Severity transition (reviewed) | n |
| --- | ---: |
| P1 → P1 | 4 |
| P1 → P2 | 5 |
| P2 → P2 | 26 |
| P2 → P3 | 14 |
| P3 → P3 | 36 |

Eight-point verification results:

| Check | yes | partly | no / n/a |
| --- | ---: | ---: | ---: |
| exists | 83 | — | n/a 2 |
| anchor accurate | 84 | 1 | — |
| speaker correct | 76 | 8 | n/a 1 |
| continuity respected | 61 | 23 | n/a 1 |
| context considered | 74 | 11 | — |
| counterevidence examined | 83 | 2 | — |
| not already covered | 35 | 47 | no 3 |
| proportionate | 54 | 23 | no 8 |

**Interpretation.** The reviewers found the source work reliable. Anchors were verbatim, speaker attribution (including `isInner`, voice and actor
checks) was correct in all but a handful of partial cases, and no finding faulted a Source Lock 1.0 reading for lacking later evidence. Disagreement concentrated on
**proportion and existing coverage**. In 50 of 85 reviews the reviewer found that the canonical corpus already made at least part of the point, usually in a section or
document other than the one the specialist named. In 31 reviews the proposal was judged only partly proportionate or disproportionate. That is why 19 of the 49
reviewed P1/P2 findings were downgraded, and why no reviewed finding was raised.

**Implication for unreviewed findings.** 207 findings (83 P2, 124 P3) rest on one specialist. Applying the reviewed downgrade rate, roughly a third
of unreviewed P2s would probably settle at P3 on review. None would be expected to vanish entirely: no reviewed finding was rejected. Their status is `ACCEPTED_SPECIALIST_ONLY`.

## 3. Sustained objections against specialists (selected)

| Finding | Objection | Result |
| --- | --- | --- |
| CMP03-C001 Kotone father arc (P1) | Interpretive frames already exist: core §3.2.14, §9.2/KOTO-C06, §11.2, and Sena core §24. "Opposite function" overstates the misreading | P2 |
| CMP05-C001 Lilja romance thread (P1) | Core §12.2 already reads Dear 037 as romance-adjacent, with the answer deferred and enclosure kept OPEN. The real gap is the communications evidence. Drop the Sweden-trip and Christmas items as romance signals | P2; branch-label fix P3 |
| CMP12-C001 Sena cross-route defeats (P1) | The SL1.1 Sena refresh already tests OPEN-SENA-12. The owning cores already read each defeat scene (Saki §3.2.10 and others). The gap is integration into Sena's home, not absence from the corpus | P2 |
| CMP13-C001 Tsubame / Sena first retirement (P1) | The D003 omission holds. The developmental contrast is present in substance (§20, §22, RS-II §5.3). MISINTERPRETED does not hold | P2 OMITTED |
| CMP18-C002 Juo father / 100 Pro (P1) | Spine §14, NPC ledger L516 and Sena core §33 carry parts. The defect is the split entity rows and the missing N.I.A.-planner attribution | P2 |
| CMP17-C002 Saki concealment "track-dependent" | D-SAKI 023 asks the same "did I keep up the front" question as U1. The track-dependence thesis fails | P3 |
| CMP09-C001 Sumika exit-offer test | Recurrent, not branch-invariant | P2, scope narrowed |
| CMP04-C001 Mao promise (P1) | "Enforces whenever" is false across branches (P1 mid-failure ch2). The promise's content drifts | P1 kept, qualified |
| CMP16-C002 Misuzu's estranged friend = Rinha | The identification holds only by inference. S03b §9 already routes it, and XW-030 is the stronger anchor | P3; dissent from HSCA-119 preserved |
| CMP14-C002 / C003 Kanae | The Kanae reading already sets voiced freedom against approval structures. "Independent" overstates only in two ledger shorthands | P3 |
| CMP07-C003 Hiro 神格 | The disposition is an attribution error, not a misreading. Fans and the Producer coin 神格 before Sena does | P2 ATTRIBUTION_ERROR |
| CMP18-C007 N.I.A. exclusions | These are conventions (暗黙の了解), not rules. P2-SENA is a counterexample | P2, reworded |
| CMP16-C008 Kuramoto household | Re-anchor on SL1.0 `adv_cidol-kcna-3-009_02`. Do not carry an SL1.0 fault with SL1.1 evidence | P3 UNDERWEIGHTED |

## 4. Objections rejected (specialist upheld against a challenge)

The reviewers raised no challenge that the integrator overturned. The integrator did, however, uphold the following against defenses the reviewers themselves raised:

- **CMP07-C001 Hiro origin line (P1).** Strongest defense: the core already uses owl (§12, HIRO-C15/C16), and HIRO-C14 already credits
  「かわいくなりたかった」. Rejected. The core never records owl's live as Hiro's stated trigger (dear_024 L203 「それが、きっかけ。」), the friend's letter
  (dear_035 nameless `isInner` lines L189–L212) or the closure in Dear 036 L660. The route's final arc is built on that origin. Principal A1 check confirmed it.
- **CMP08-C001 Rinami romance mechanics (P1).** Strongest defense: core line 286 already says Rinami fuses confession and production. Rejected at the P1 level. The
  Producer's recurring professional reframing of her bids (five C1 Dear scenes) and his hidden single-option 「――はい」 (dear_037 L453) are unmodelled. R06 kept P1 and
  the integrator concurs, adopting R06's "supplement, don't replace" qualification.

## 5. Unresolved or preserved disagreements

| Item | Positions | Integrator disposition |
| --- | --- | --- |
| CMP11-C001 Misuzu reciprocal-jealousy origin | Specialist (after reading HSCA): borderline P2, because HSCA-121 shows Misuzu cried before Temari in Dear 009. R01: P1 with narrowed scope | **P1 adopted, qualified, dissent preserved**. Owner adjudication |
| CMP03-C001 Kotone | Specialist: P1; HSCA-023 had P2; R03: P2 | P2. The specialist's P1 view is recorded |
| CMP16-C002 Rinha identification | CMP16 and R08: holds by inference; HSCA-119 disputes the transfer timing | P3, inference label required. Owner adjudication |
| CMP12-C013 Sena's voice actress | Ledgers disagree ("Harusaki Non" vs "Hina Yomiya"). A1 cannot settle it | Open. Resolve from an official credit (A4); do not substitute one ledger's name for another |
| CMP10-C015 Sena as Ume's producer | Specialist's post-freeze erratum: P3 fits | P3 (integrator adjustment) |
| CMP15-C001 Saki's idol origin | Specialist's post-freeze erratum: the Saki core already has Sena as origin (HSCA-146); only the E005 locator is missing | Narrowed to the remaining examples |
| Unverified side-claims (R03) | CMP03-C001's E001/D-SENA 016 addition; CMP03-C008's P2 a-01 link; CMP13-C012's school_003 L24 | Do not adopt these elements without an A1 check |

## 6. Specialist self-corrections after reading HSCA

Five comparators reported, after their freeze, that the HSCA register showed errors in their own frozen dispositions. These include false `COVERED` rows: CMP10 (HSCA-060/064), CMP03 (HSCA-026),
CMP11 (HSCA-032/097) and CMP01 (B10-0001/0007). The frozen files were not edited. The HSCA findings involved are recorded in the comparators'
`hsca_reconciliation.jsonl` as `NOT_REDISCOVERED`, with the comparator's A1 judgment that they still hold. They appear in Proposed Change Plan Batch 6.

## 7. Process objections recorded against the audit itself

- The principal's HSCA-register copy in the shared scratchpad during Stage A (Limitations §3).
- Incidental HSCA exposure for CMP01, CMP04 and CMP12 before the files were sealed. Affected candidates carry `hsca_exposure: true`.
- A02/B02 Temari agreement is not independent.
- Reviewers share a model family with specialists. Independence here means separate contexts, blind-first reading and separate source access, not model diversity.
