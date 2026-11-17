---
title: "GKM Source-to-Analysis Audit — Limitations and Completion Statement"
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

# G. Limitations and completion statement

Audit: GKM source-to-analysis audit, 2026-11-15 (`source-to-analysis-audit-20261115`).
Baseline: PR #600 head `176d472a` (open, unmerged) for `series/gakuen-idolmaster/`; governance from `main` `f31e0725`; A1 Source Lock 1.2
(revision 88, `f8ff5ef7`). PR #599 §4.1 was applied as an owner instruction for this audit, not as integrated governance.

## 1. What is complete

- **Source coverage.** All 4,052 admitted A1 objects have a coverage row. 3,671 dialogue-bearing objects were read in full by blind Stage A
  readers through an A1-derived view carrying A1 line locators. All 381 no-message objects were inspected and classified from raw A1. No object is
  `PARTIAL`, `NOT_READ` or inaccessible. (Deliverable C.)
- **Blind reading.** 37 independent readers produced 4,090 observations and 498 negative controls. Every observation is marked as verified
  against raw A1 by its reader's script and spot checks. The files were frozen by SHA-256 before any comparison began.
- **Canonical comparison.** 18 comparators dispositioned 9,788 observation rows against the canonical homes. They proposed 292 candidates and froze them before
  the HSCA reconciliation.
- **Adversarial review.** Independent reviewers examined 85 selected findings (all P1s, a P2 sample, and corrective or owner-flagged P3s). They read A1 first,
  before opening each claim.

## 2. What is not complete or not verified

1. **Most candidates were not independently reviewed.** The review covers every P1, about 30% of P2s and the disputed P3s.
   Unreviewed P2 and P3 findings are marked `ACCEPTED_SPECIALIST_ONLY` in the register. Their reliability can be estimated only from the
   sustain rate in the reviewed sample (Deliverable F); they have not been individually verified.
2. **The reading view is a derivative.** Stage A readers read an A1-derived view, not the raw command stream. The view keeps every message,
   narration, choice, branch, inner-speech flag, ruby and speaker-portrait code, but drops camera, motion and facial commands. Readers were told to open
   raw A1 for decisive staging, and their verification checked anchors against raw lines. Staging-dependent readings may still be under-sampled.
3. **Voice attribution in views is heuristic.** `{voice~code}` tags match by clip timing and appear only for non-cast speaker names. Cast-name
   attribution relies on `name=`. Two attribution findings (E1-0006, and the `name=佑芽` line in `adv_live_hmsz_001_start-03-01`) were confirmed from raw
   voice and actor commands. Other attribution errors of the same kind may remain undetected.
4. **Condition branches and result dispatch.** A1 carries no condition expressions or grade labels for several Produce endings and live
   variants, so readers inferred orderings and dispatch. Branch-dependent claims are labelled, but exact eligibility remains open (as the Kanae receipt also says).
5. **Large extracts were filtered.** CMP17 and CMP18 filtered the 2,835-row relationship extract and the 2,157-row
   institution/family/Producer extract to their canonical claims. CMP18 judged 768 rows from their summaries. Cross-track rows outside those filters were
   dispositioned only by the per-character comparators.
6. **Specialist self-corrections after the freeze.** Five comparators reported errors in their own frozen dispositions after reading
   HSCA material (Checkpoint 3 §4). These are recorded as integrator adjustments. The frozen bytes were not edited, so `dispositions.jsonl` contains
   a few known false `COVERED` rows.
7. **PR discussion not read.** The GitHub MCP connector failed to connect and agents had no web access. The PR #600 "unresolved P2
   versioning comment" on the AV handoff was therefore **not read**. CMP14 independently found and recorded AV-documentation inconsistencies in the Carbon
   packet and adjudication files (CMP14-C011, C012). Whether these match the PR comment is unverified.
8. **No audiovisual inspection.** Direct listening: 0 seconds. Continuous-motion review: 0 seconds. AV-dependent questions are routed to the
   existing Carbon queue. The Carbon review was not performed and the Kaya Rinha AV gate was not touched.
9. **Model identity and effort.** Every agent ran as a native Claude Code subagent of the same model family as the principal (Claude Opus 5.5).
   Reasoning effort, token use and sampling settings were not observed and are not reported. Model diversity was not used.

## 3. Independence and contamination disclosures

- **Shared scratchpad (Stage A).** Native subagents shared the session scratchpad. Before the principal's hygiene rule, many readers wrote
  helper files there. Two events carried analytical content. The harness showed A02 some of B02's Temari scratch notes, so A02/B02 agreement on Temari is not
  independent. A12 saw six Temari negative controls from another reader. Other events exposed only filenames or generic code.
- **Principal process error.** The principal extracted a copy of the HSCA findings register into the shared scratchpad for indexing. It stayed there
  from 13:55 until it was noticed and removed after reader B01 completed. Two readers saw the filename in a listing. **No reader reports opening it.** The audit
  cannot exclude unreported access, but no Stage A record cites HSCA material.
- **HSCA exposure in Stage B.** The HSCA files initially sat inside the canonical snapshot. Unscoped greps by CMP01, CMP04 and CMP12 surfaced
  truncated HSCA lines before the files were sealed. Affected candidates carry `hsca_exposure: true` and receive no independent-rediscovery credit. The canonical baseline
  also contains HSCA-labelled corrections (HSCA-001–006, 046), which every comparator necessarily read.
- **Model priors.** Background knowledge of the game from model training cannot be excluded. Readers flagged where it might have shaped a reading.
- **Agreement is not corroboration by default.** All agents share one model family. The register therefore separates reader agreement from source
  verification and gives weight only to A1-verified anchors.

## 4. Runtime events

- The runtime caps concurrent subagents at 20, so Stage A ran in waves and Stage B comparators started in two phases.
- An API five-hour usage limit interrupted 13 Stage B comparators. On the owner's instruction they were resumed from saved state, not restarted.
  Ten had already frozen their comparison and resumed only the HSCA step. Freeze hashes were verified after resumption: 18/18 match.
- The partition sizes quoted in some Stage A prompts (support quarters) came from a pre-rebuild count. The readers used the authoritative
  object lists, and the totals reconcile (547 support objects; 4,052 overall).

## 5. Completion statement

The audit is complete as a **source-to-analysis coverage and comparison audit at Source Lock 1.2**: every admitted object is accounted for and
every Stage A observation has at least one canonical disposition. Every P1, plus an adversarial sample, has been independently reviewed against A1. It is **not**
a certification that all 292 candidates are correct (most P2/P3s rest on one specialist), not an audiovisual audit, and not a replacement for
owner adjudication of the findings flagged for it.

No repository file was modified. Nothing was committed, pushed or opened as a PR. Local Git refs `refs/audit/pr599` and `refs/audit/pr600` were created
only to pin the inspected heads.

## 6. Integration corrections made by the principal

- An integrator note recording R04's correction was first misfiled under CMP04-C005 (Mao) instead of CMP09-C005 (Sumika). Drafters D1, D2 and E each flagged it independently.
  It was moved, and the register was rebuilt.
- The first register build missed HSCA relations wherever a reconciliation row listed several candidate IDs in one field (for example GKM-SAA-078 and 227). The aggregator was
  fixed to parse every `CMPnn-Cnnn` ID, and the register was rebuilt. Audit IDs are unchanged, because no severity moved.
- Checkpoint 3's HSCA ID count (187) counted malformed strings. The normalized figures (all 180 addressed; 127 rediscovered or extended; 8 corrected; 49 not rediscovered) are
  recorded in an erratum appended to Checkpoint 3.
- Deliverables D and E were drafted by integration subagents from the frozen records under `briefs/STAGE_D_DRAFTING_BRIEF.md` and the plan prompt. The principal
  checked them for consistency with the register. They add no findings.
