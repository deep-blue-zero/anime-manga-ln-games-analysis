---
title: "Gakuen Idolmaster V2 Source-to-Analysis Audit — Executive Report (2026-11-15)"
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

# A. Executive audit report

**Question.** How much of Gakuen Idolmaster's original Japanese narrative evidence does the existing analytical corpus represent accurately? What material
is missing or misread? Which targeted changes would improve it?

**Short answer.** The corpus is reliable and unusually disciplined. Across 9,788 comparisons of independently found evidence against the canonical homes,
**84% were already covered interpretively**. No major established conclusion is contradicted by the source (**P0: 0**). After independent review,
**four** findings remain at P1. All four are omissions or under-modelled relational mechanics; none is a reversal. The 113 P2 findings are mostly
**propagation failures**: correct evidence that never reached the right analytical home. They are rarely misreadings. The most valuable improvements are, in order:
- carrying cross-track evidence into each subject's home;
- modelling the Producer's side of each relationship, branch by branch;
- integrating the late-Dear "origin and closure" threads;
- a small set of cheap factual corrections (one systematic misgendering, one split entity, several speaker or referent slips).

## 1. Baselines

| Item | Value |
| --- | --- |
| Analytical baseline | PR #600 head `176d472a2df2b325f0c54e1c589f7f5e8a89ada9`, `series/gakuen-idolmaster/`: 511 files, inventoried with blob IDs. PR #600 is **open**; it is audited as a proposal, not as merged authority |
| Governance baseline | `main` `f31e07250156a33c5290b335c397a5abf8297a67`. Since the PR #600 merge base, `main` has not changed Gakumas files or governance |
| Multi-agent instruction | PR #599 §4.1 at `85fc1fd7`, **open**. Used as the owner's instruction for this audit only |
| Source | A1 archive at the local Source Lock 1.2 A1 archive (owner workstation). This is **not** in the local Gakuen Idolmaster workspace (owner workstation), which holds the repository checkout and AV media. Manifest hashes and the A1/A2 inventory fingerprints match the Source Lock 1.2 receipt exactly: 4,052 objects / 103,355 extracted messages (103,374 raw `[message` commands) |
| Lock lineage | Each object is tagged with the lock where it first appears: SL1.0 (revision 32) 3,777 · SL1.1 (revision 86) 172 · SL1.2 (revision 88) 103. No later evidence was admitted |

Details: `checkpoints/CHECKPOINT_1_BASELINE_LOCKED.md`.

## 2. How the audit was done

- **Stage A, blind source reading.** 37 independent subagent readers each read one bounded partition. Before reading, none had seen the canonical analysis, the prior HSCA
  audit or any PR discussion. Together the partitions covered **all 4,052 A1 objects**:
  - 3,671 dialogue objects read in full through an A1-derived view carrying A1 line numbers, choice and branch spans, inner-speech flags, ruby and speaker-portrait codes;
  - 381 no-message objects inspected in raw A1 and classified.

  The readers produced 4,090 observations, each marked as verified against raw A1 by the reader's own script and spot checks, plus 498 negative controls.
  Everything was frozen by SHA-256.
- **Stage B, canonical comparison.** 18 comparators (14 subjects plus events, support stories, Unit Story 01 and relationship systems, and institutions, Producer and Rinha) read the
  canonical homes in full. They dispositioned every relevant observation, including cross-track evidence from all other readers, and froze 292 candidate findings
  **before** opening the HSCA register.
- **Stage C, adversarial review.** 8 fresh reviewers examined 85 findings: all P1s, a ~30% P2 sample and every corrective or owner-flagged P3. Each
  wrote a blind A1 reading before opening the claim, and gave every P1 a strongest-defense section.
- **Integration.** The principal adjudicated the reviewed findings, personally re-checked the A1 anchors of the surviving P1s, and recorded every dissent.

## 3. Coverage actually achieved

| | Objects |
| --- | ---: |
| Admitted A1 objects | 4,052 |
| Read in full (dialogue) | 3,671 |
| No-message objects inspected in A1 | 381: voice-only 284, staging-relevant 94 (87 in the system partition plus 7 Produce Series 003 staging stubs in the common-route partition), technical 2, opaque `musics.txt` 1 |
| Partial / not read / inaccessible | 0 / 0 / 0 |
| Objects carrying ≥1 independent observation | 2,600 |
| Objects linked to a Stage B finding | 678 |

Per-object ledger: `C_SOURCE_COVERAGE_LEDGER.tsv` (one row per object: lock, archive path, SHA-256, reader, status, function, participants,
observation IDs, finding IDs).

## 4. Overall reliability of the existing analysis

| Disposition of 9,788 observation comparisons | n | % |
| --- | ---: | ---: |
| COVERED | 8,195 | 83.7 |
| SOURCE_SCOPE_LIMITED (outside a document's declared boundary) | 385 | 3.9 |
| OMITTED | 366 | 3.7 |
| UNDERWEIGHTED | 337 | 3.4 |
| CROSS_REFERENCE_GAP | 331 | 3.4 |
| OPEN / TRACEABILITY_GAP / ALREADY_CORRECTED | 43 / 34 / 29 | 1.1 |
| MISINTERPRETED / ATTRIBUTION_ERROR / CONTINUITY_ERROR | 22 / 17 / 14 | 0.5 |
| AV_DEPENDENT | 15 | 0.2 |

> **Correction (2026-11-15).** An earlier version of this report gave the comparison total as 10,788 and computed the percentages against it. The category counts were right, but the total was an addition error carried over from Checkpoint 3. The frozen Stage B disposition files hold 9,788 rows, which is the denominator used above. The no-message line in §3 also omitted the 7 Produce Series 003 staging stubs classified in the common-route partition, so its classes now add to 381. A read-only external review found both errors. A later review (PR #617) found that five findings naming their objects in shorthand (CMP01-C011, CMP01-C012, CMP06-C006, CMP07-C016, CMP10-C016) had no link in the coverage ledger. They are now linked through the objects of the Stage A observations they cite, which raises the count of objects linked to a finding from 628 to 678. Three findings cite no A1 object because they concern consistency inside the canon (CMP12-C012, CMP12-C013, CMP14-C011), so they stay unlinked. No finding, severity or recommendation changes.

Errors of reading (misinterpretation, attribution, continuity) make up **half a percent** of comparisons. The corpus's weaknesses are mostly **absences
and routing**, not misreadings.

**Final findings register (292):** P0 **0** · P1 **4** · P2 **113** · P3 **175**.

Independent review sustained 47 of 85 sampled findings, qualified 38 and rejected none. It lowered 5 of 9 proposed P1s to P2 and 14 of 40 sampled
P2s to P3, and raised none. Reviewers found the specialists' **source work** reliable: anchors verbatim, speakers correct, lock boundaries respected.
They found the **severity and "omitted everywhere"** claims frequently overstated, because the canon often made part of the point elsewhere. Unreviewed P2s
(`ACCEPTED_SPECIALIST_ONLY`) should be read with that ~35% downgrade tendency in mind.

## 5. Strongest surviving character-level conclusions

Blind readers who never saw the canon repeatedly reconstructed its central theses, which is strong independent corroboration. Examples:

- **Saki.** 無敵 → 不屈 and the layered model of recovery (action, identity, affective, relational). Confirmed across Dear, Produce, Unit Story and support stories.
- **Temari.** "Authored combustion": coolness as an authored truth rather than a fake persona.
- **Kotone.** 普通 as the class climax, money as both scarcity and pleasure, successor reframed as rival, and her audience ethic. All verified against A1 and extended correctly by SL1.1.
- **Mao.** The rejection of "tomboy learns femininity" and "the prince was fake". The Dear 004 anti-substitution reading. Gender-identity restraint.
- **Lilja.** A talent taxonomy that refuses the romance of grit, and REVERSI as a differentiated partnership.
- **China.** Stewardship rather than renunciation, nondelegable accountability, and socially ratified self-credit.
- **Hiro.** The boredom of competence, and the additive model in which hobby and dream coexist.
- **Rinami.** Reciprocal care becoming self-authored desire.
- **Sumika.** "Self-authored expectation". The mask as a chosen lie meant to become true. The injury model.
- **Ume.** Differentiation without severance; the rejection of "fearless Ume"; burnout revised.
- **Misuzu.** マイペース as a system; the depression correction; care that is both gift and attachment technology.
- **Sena.** Retirement as displaced desire. Her vision accurate but ontologically incomplete. "Generative supremacy" under ethical reservation.
- **Tsubame.** No.2 as rank, refuge and excuse; the Dear 024 individuation; strictness as sharpening care.
- **Kanae (SL1.2).** An accurate Dear spine with exemplary Produce-state discipline. No P0/P1.
- **Shared spine, continuity and branch topology.** Exemplary claim discipline. Event numbers are correctly not treated as a calendar. True-labeled states are kept scoped.

## 6. Significant omissions and inaccuracies

### P1: four substantial deficiencies (all omissions or under-modelling; none reverses a thesis)

1. **GKM-SAA-001 Mao: the promise as relational contract, and the Dear 022–026 crisis** (CMP04-C001; reviewed QUALIFY, P1). The Producer presents
   his own replacement as 「申し分のない」, defers with 「決めるのは、麻央さんです」 (dear_024 L19), and later admits fault (dear_026 L74–75). Mao invokes
   「約束したじゃないですか」 (dear_022 L374–377), and Asari reframes the situation. None of this is in any canonical home. The P1 claims are branch-bounded, and the promise's content drifts across the route.
2. **Hiro: the origin line** (CMP07-C001; reviewed SUSTAIN, P1). owl's live is Hiro's stated trigger (「それが、きっかけ。」 dear_024 L203). The
   final three Dear chapters close that loop: 初心 in Dear 034; the friend's inner-speech letter in Dear 035 L189–212, which A2 omitted; and 「わたしが憧れたアイドルは、あなたに敗れ…」 in Dear 036 L660.
   The core uses owl only as a theorist of constructed personas.
3. **Rinami: the Producer's side of the romance** (CMP08-C001; reviewed QUALIFY, P1). Across five C1 Dear scenes he reframes her bids for intimacy as professional.
   His romantic answer is a hidden single-option 「――はい」 (dear_037 L453). Read this way, the fusion of romance and production is co-produced in idiom and authored by Rinami in voice.
   "Genuine mutual love" should be scoped.
4. **Misuzu: reciprocal jealousy at the origin** (CMP11-C001; reviewed QUALIFY, P1; **dissent preserved**). Temari's 「美鈴を取られたみたいに」
   (dear_032 L286) mirrors Misuzu's 「心が、奪われてしまった」 (dear_010 L275). Misuzu also asks whether she ranks above Kei and Rinha (dear_034 L594), and tells Temari herself where her idolhood began (dear_036).
   The specialist regards this as borderline P2. Owner adjudication required.

Downgraded from proposed P1 to P2, with the reasons recorded in F §3: Kotone's father arc; the Lilja romance-coded thread; Sena's defeat states in other routes;
Sena's first retirement plan in Tsubame's route; and the Juo father / 100 Pro president identity with the N.I.A. planners.

### Inaccuracies worth fixing first (cheap, high value)

- **Mao misgendered.** Five support readings and two ledger rows use "he/his" for Mao: CMP04-C012 and CMP16-C001, both sustained (P2).
- **Split entity.** "Sena's father", 十王龍正 / Ryuusei Juo and President Juo appear as unlinked NPC rows, although cidol-jsna-3-002_02 L192 (SL1.0)
  identifies the father as 十王社長. The headmaster's statement about the N.I.A. planners is unrecorded (CMP18-C002; P2).
- **Initiative misattributed.**
  - Temari's given-name address and ramen are both initiated by the Producer, not Temari (CMP02-C001; sustained).
  - In Hiro §21, Hiro voices the relationship stake and the Producer accepts it tacitly (CMP07-C002; sustained).
  - 神格 is coined by fans and the Producer before Sena uses it (CMP07-C003; sustained as ATTRIBUTION_ERROR).
- **Mis-scoped evidence.** Mao's Dear 027 waiting-room cry is cited as her "private breakdown after public framing" in five homes (CMP04-C002; sustained).
- **Branch-invariance overstated.** Examples: the Sumika exit-offer test, Sumika's face-saving across endings, the Producer's leisure answer, and a Lilja Dear 037 line attributed across branches.

## 7. Recurring analytical weaknesses

1. **Cross-track propagation.** This is the historical audit's weakness, and it persists in the newer corpus. Evidence developed in another character's route,
   in events or support stories, or in Unit Story 01, often does not reach the subject's own home. Examples:
   - Sena's defeat states in eight other routes;
   - Sena as China's and Ume's producer;
   - Kanae's earlier appearances in China's and Hiro's routes (CMP14-C001/C009);
   - Ume's Unit Story relationships, which have no character home;
   - Revision 86 support routing executed for only 5 of 15 families (CMP16-C004).

   The owning character's reading is usually correct. The **counterpart's** home is what is missing.
2. **The Producer is under-modelled as an agent.** Several of the strongest findings concern initiative, acquiescence or reframing by the Producer that
   the canon attributes to the idol or leaves out: Mao, Rinami, Temari, Lilja, Sumika's engineered live and pre-arranged unit, and two-way influence in Ume's Dear 023.
   Branch differences in his behavior are also often flattened. The cores model each idol carefully and model him as a constant.
3. **Late-chain closure is under-integrated.** Several Dear chains end by returning to an origin: Hiro and owl (Dear 034–036); Kotone's father found at the N.I.A. final;
   Misuzu's origin told to Temari (Dear 036); Mao's promise invoked and renegotiated (Dear 022–027). These endings are often outside the core's main argument. The cores were
   strongest on Dear 001–027 and weakest on the 028–037 closures.
4. **Family and ordinary life are thinner than the thesis.** Examples: Sena's distance from her family and her father's verdict that she "won't make it as a pro"; Sumika's family strain and repair;
   China's early-childhood loneliness; small habits and preferences.
5. **Linguistic specificity.** The register sections are often generic. Examples: Sena's stable formulas and her ruby system (一番星《プリマステラ》 and others), and Lilja's speech level shifting with
   her addressee. The Japanese-register ledger has strong rows, but the cores rarely use them.
6. **Branch-scope creep.** Some claims are stated as invariant when they are recurrent, or come from one choice of three.

## 8. Areas stronger than expected

- **Thesis quality.** No core is a single-thesis caricature. Most explicitly refuse the easy binary (fake/real, weak/strong, care/selfish), and the
  blind readers independently reached the same syntheses.
- **Branch and lock discipline.** Failure, normal and true-labeled states are kept apart. SL1.0, SL1.1 and SL1.2 evidence is cleanly separated. The Kanae reading's Produce-state discipline
  is exemplary: it treats a response option as unable to explain how a result was earned.
- **Falsifiability.** The evidence matrices give each claim a narrowing condition, so this audit could test them.
- **Prior corrections.** The HSCA-006 attribution fix (E001: the line credited to Lilja is Sumika's, voice `ssmk-018`) is correct and complete. The U1 nightmare correction
  (Saki core §3.6.1) is a model of epistemic care.
- **The newest analysis (Kanae, PR #600).** No P0/P1. Twelve spans re-checked against A1 had no factual error. The gaps are cross-track (earlier
  appearances) plus two AV-documentation inconsistencies.

## 9. Relation to the historical audit (HSCA, Source Lock 1.0)

All 180 HSCA findings were reconciled **after** each comparator had frozen its own independent findings:

| | n |
| --- | ---: |
| HSCA findings independently rediscovered, extended, narrowed or contradicted by this audit | **127** (P2 73, P3 50, P1 3, evidence-only 1) |
| Recorded as corrected in the baseline | 8: the seven 2026-11-12 dispositions (HSCA-001–006, 046), plus HSCA-059, judged partly addressed through the HSCA-002 correction (CMP01) |
| Not rediscovered by this audit | 49 (P2 20, P3 29). Every one checked in A1 still holds |
| New findings with no HSCA counterpart | 158 candidate rows |

The two audits corroborate each other strongly. 71% of the earlier findings were found again by blind readers and comparators who had not seen them.
**Three of the seven 2026-11-12 corrections are incomplete.** HSCA-001's Rinha-crosswalk routing was never done (CMP17). HSCA-005's legacy ledger
and pass report still say "Lilja rejects" (CMP05, CMP09). HSCA-004 still lacks its Saki-side cross-reference (CMP01). The other four (002, 003, 006, 046)
were judged adequate. The audit did not copy HSCA severities. Where they differ, both are recorded: for example, CMP04-C001
extends HSCA-011 at a higher severity, and CMP18-C002 rates HSCA-150 higher.

## 10. Prioritized recommendations

1. **Batch 0, factual corrections.** Fix the Mao pronoun error everywhere, merge the Juo father entity, and fix the sustained attribution, locator and branch-label errors. Low
   risk, no owner judgment needed for most.
2. **Batch 1, the four P1 integrations** (Mao promise, Hiro origin, Rinami romance mechanics, Misuzu reciprocal origin), as bounded subsections, with
   the reviewers' qualifications applied. Owner adjudication for the Misuzu severity and the Rinami "mutual love" scope.
3. **Batch 2, cross-track counter-tracks** in each subject's home, especially Sena (defeat states), Kanae (earlier appearances), Ume (Unit Story) and the
   support-routing backlog. This addresses the main recurring weakness.
4. **A Producer model.** A cross-core section or ledger that records his behavior branch by branch (initiative, reframing, acquiescence, admission), so the cores
   stop treating him as a constant.
5. **Batch 6, close the historical loop.** Act on the 49 HSCA findings that are still open and not rediscovered (20 at P2), and finish the partial corrections to HSCA-001,
   HSCA-004 and HSCA-005.
6. **Before Phase 7 monographs,** treat the late-chain closures, family material and linguistic signatures as required inputs. They are the main readiness gaps
   in Deliverable D.

The full ordered plan, with target sections, evidence, transitions, dependencies and adjudication flags, is in `E_PROPOSED_CHANGE_PLAN.md`.

## 11. Audiovisual boundary

This is a transcript-to-analysis audit. **Direct listening: 0 seconds. Continuous-motion review: 0 seconds.** 63 findings carry an AV-dependency note
(AV-C script metadata or AV-D inference), and 15 observation comparisons were dispositioned `AV_DEPENDENT`. These are routed to the existing Carbon queue in
Plan Batch 5. The Carbon review was not performed and the Kaya Rinha AV gate was not touched.

The PR #600 AV handoff has documentation inconsistencies, recorded separately from literary findings:
- the Carbon handoff ID and version were not updated after the Kanae supplement (CMP14-C011);
- the scope of packet and adjudication rows does not match (CMP14-C012).

The PR #600 review comment on "P2 versioning" itself could not be read: the GitHub connector failed and agents had no web access.

## 12. Limitations (summary; full statement in `G_LIMITATIONS_AND_COMPLETION_STATEMENT.md`)

- 207 of 292 findings rest on one specialist.
- Stage A readers used an A1-derived view, and decisive staging was checked only where readers chose to open raw A1.
- Condition-branch dispatch is unrecoverable from A1.
- The shared-scratchpad events reduced independence in two bounded cases (A02←B02 on Temari; A12 on Temari).
- The principal's HSCA-register copy sat in the shared scratchpad during part of Stage A. No reader reports opening it.
- All agents share one model family.
- No repository file was modified, and nothing was committed, pushed or opened as a PR.

## 13. Publication recommendation and follow-up PRs

- **Publishing the accepted report.** After owner acceptance, publish a sanitized package beside the earlier audit, as
  `series/gakuen-idolmaster/01_CORPUS_AUDIT_AND_SOURCE_LOCK/SOURCE_TO_ANALYSIS_AUDIT_20261115/`. Mark it as a non-authoritative retrospective audit with the same front-matter
  conventions as the HSCA package. Include:
  - this report;
  - the findings register (TSV);
  - the index;
  - the change plan;
  - the review record;
  - the limitations statement;
  - the coverage ledger, which contains hashes and locators only, no source text beyond short anchors.

  Add a dated first-read note to `CURRENT_STATE_AND_CORPUS_MAP.md` stating that the audit revises no canonical reading. Raw A1 views, partition files and agent scratch
  material stay local. Route the publication through the author preflight and `CHANGE_INTEGRATION_CHECKLIST.md` on `series/gakuen-idolmaster`, after PR #600 is
  merged or reconciled, so the audit's baseline matches `main`.
- **Follow-up correction PRs** (separately authorized; each through the checklist, with targeted edits and claim-revision rows):
  1. Batch 0 factual and attribution corrections.
  2. Batch 1 P1 integrations.
  3. Batch 2 cross-track counter-tracks, grouped by core.
  4. A Producer-model ledger or section.
  5. Batch 6 historical-audit closure.

  Batches 3–4 (P2 additions, P3 traceability) can travel with the PR that touches the same file.
