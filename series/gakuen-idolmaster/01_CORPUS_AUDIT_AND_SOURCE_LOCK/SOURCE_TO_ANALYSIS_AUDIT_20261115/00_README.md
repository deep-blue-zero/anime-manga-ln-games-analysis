---
title: "GKM Source-to-Analysis Audit 2026-11-15 — Package Map"
series: GKM
artifact_type: audit
scope: SOURCE_LOCK_1_2_SOURCE_TO_ANALYSIS_AUDIT
generation: V2
status: active_provisional
audit_nature: "non-authoritative retrospective audit; does not itself revise any canonical conclusion"
audit_id: GKM-SAA-20261115
source_lock: GAKUMAS V2 Source Lock 1.2
source_commit: f8ff5ef7b243f2f7e3b2723def31072874539ca9
source_revision: 88
audit_baseline_commit: "176d472a2df2b325f0c54e1c589f7f5e8a89ada9"
created: "2026-11-15"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# GKM source-to-analysis audit (2026-11-15): package map

This is a retrospective, multi-agent audit of the Gakuen Idolmaster V2 analytical corpus. It audited the PR #600 head `176d472a` against the
original Japanese A1 scripts at **GAKUMAS V2 Source Lock 1.2**. It is **non-authoritative**: every canonical reading stays the current authority. The
corrections the owner authorized are applied separately through the ordinary claim-revision route. They are recorded, finding by finding, in
[the dispositions crosswalk](../GKM_SOURCE_TO_ANALYSIS_AUDIT_DISPOSITIONS_20261115.md) and in the claim-revision ledger.

| File | Content |
| --- | --- |
| [Executive report](GKM_SAA_A_EXECUTIVE_AUDIT_REPORT.md) | Baselines, coverage, reliability, strongest conclusions, omissions and inaccuracies, recurring weaknesses, HSCA reconciliation, recommendations |
| [Findings register](GKM_SAA_B_FINDINGS_REGISTER.tsv) | 292 findings (`GKM-SAA-001`–`292`), with every field: A1 object and lines, Japanese anchor, continuity and epistemic status, existing claim, disposition, proposed change, counterevidence, severity, confidence, reviewer decision, integrator disposition, HSCA relation, destination |
| [Findings index](GKM_SAA_B_FINDINGS_INDEX.md) | One line per finding, grouped by final severity and subject |
| [Source coverage ledger](GKM_SAA_C_SOURCE_COVERAGE_LEDGER.tsv) | One row per admitted A1 object (4,052): lock, name, category, SHA-256, reader, reading status, narrative function, observation count, finding IDs. A compact projection of the full local ledger |
| [Character assessments](GKM_SAA_D_CHARACTER_ASSESSMENTS.md) | Assessments for the 14 playable subjects and the distributed subjects |
| [Proposed change plan](GKM_SAA_E_PROPOSED_CHANGE_PLAN.md) | The ordered correction batches the owner authorized for execution |
| [Adversarial review record](GKM_SAA_F_ADVERSARIAL_REVIEW_RECORD.md) and [review table](GKM_SAA_F_REVIEW_TABLE.md) | 85 independent reviews (47 sustained, 38 qualified, 0 rejected) and preserved dissent |
| [Limitations and completion](GKM_SAA_G_LIMITATIONS_AND_COMPLETION.md) | What is and is not complete, independence and contamination disclosures |

In both TSV files an empty final cell is written as `—`, so that no line ends in whitespace. In the coverage ledger, five findings that name their objects in shorthand are linked through the objects of the Stage A observations they cite. Three findings concern consistency inside the canon and cite no A1 object, so they are not linked. The executive report's correction note gives the details.

**Headline.** P0 0 · P1 4 · P2 113 · P3 175. 84% of 9,788 evidence comparisons were already covered by the canonical prose. 127 of the 180 Source Lock 1.0
historical-audit findings (HSCA) were independently rediscovered.

**What stays local.** The A1-derived reading views, partition files, 37 frozen blind readings, 18 comparisons, 8 review packets, agent receipts and checkpoints
remain on the owner's workstation, as raw-source derivatives and process evidence. Each finding's chain can be followed by ID:
`original_name` → Stage A `obs_id` → Stage B `cand_id` → Stage C review → `GKM-SAA-nnn`. Local absolute paths have been removed from these copies.

Audiovisual boundary: no listening or continuous-motion review was performed. AV-dependent questions are routed to the existing Carbon packet for
Gemini Carbon 4.
