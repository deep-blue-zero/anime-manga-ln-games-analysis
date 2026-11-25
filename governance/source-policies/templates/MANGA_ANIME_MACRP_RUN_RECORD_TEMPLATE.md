---
title: Manga / Anime MACRP Adoption and Run Record Template
artifact_id: MANGA_ANIME_MACRP_RUN_RECORD_TEMPLATE
artifact_type: macrp_run_record_template
version: "1.0"
status: canonical
scope: reusable operational template for one Multi-Agent Character Reconstruction Pass run; not a populated run record
created: 2026-11-24
last_updated: 2026-11-24
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/templates/MANGA_ANIME_MACRP_RUN_RECORD_TEMPLATE.md
supersedes: null
superseded_by: null
---

# MACRP Adoption and Run Record Template

Use with the [MACRP protocol](../MANGA_ANIME_MULTI_AGENT_CHARACTER_RECONSTRUCTION_PASS_PROTOCOL.md) and its [execution runbook](MANGA_ANIME_MACRP_EXECUTION_RUNBOOK.md). Copy the body below the line into one run record inside the project root, at the path the project names (Protocol Section 13.2), and give the run its own ID. Do not reuse this template's artifact ID. A stage that moves between environments also uses the [stage handoff template](MANGA_ANIME_ANALYTICAL_STAGE_HANDOFF_TEMPLATE.md).

Replace placeholders with observed state. Keep `null` or an explicit unknown where information is unavailable, and explain any resulting blocker. Empty checkboxes and examples are not evidence of completed work. These fields are documentation, not an enforced schema; an equivalent established project format is acceptable when the same information stays recoverable. Where a responsibility already has a project home, link to it instead of copying it here. Keep sealed probes and material withheld from blind participants out of this record until they are released.

---

```yaml
# Run record front matter: replace the template's own front matter with this block.
# A run record is operational provenance, never character evidence (Protocol Section 13.2).
title: "<Project> MACRP run <run ID>"
artifact_id: "<run ID>"
artifact_type: macrp_run_record
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
macrp_protocol_version: "1.0"
```

# <Project> MACRP run <run ID>

## 1. Start here

**Current stage and state:** <stage> / <PLANNED | IN_PROGRESS | READY_FOR_HANDOFF | ACCEPTED | BLOCKED | INTEGRATED>

**Next authorized action:** <What may be done now, distinct from possible later work.>

**Open blockers and holds:** <None, or each blocker or owner hold with its next owner.>

```yaml
# Use only these keys for R and T runs. Never write sequential_execution or
# project_initialization fields for them (Protocol Section 12.2).
macrp_run:
  run_id: null
  modes: {}                       # subject -> MACRP-R | MACRP-T | MACRP-F
  pass_state: blocked             # blocked while configure-only; then active | completed | blocked | interrupted_pending_recovery
  next_stage: null
  project_root: null              # series/<slug> or studies/<slug>
  canonical_entrypoint: null      # exact registered path
  run_record_path: null           # this file's repository path
  held_artifacts: []              # paths this run holds as mutable owner, once execution is authorized
  governing_method: null          # path and version
  governing_architecture: null    # path and version
  reconstruction_method: null     # project method, or the generic method if adopted
  baseline_commit: null           # full SHA on main
  publication_branch: null        # series/<slug> or studies/<slug>
  pull_request: null              # number, once open
  last_audited_head: null         # full SHA with a successful exact-head audit
  last_verified_checkpoint: null  # stage and commit
```

## 2. Authorization and scope

| Item | Value |
|---|---|
| Owner instruction (recoverable wording or reference) | |
| Configure only, or execute | |
| Mode per subject, and the reason | |
| Target subjects (discovery `analysis_subject_id` or project identity) | |
| States in scope (`Character@Unit` boundaries) | |
| Source and continuity boundary (exact locked inventory for live service) | |
| Diagnostic units or selection rule (MACRP-T), and the reread test result | |
| MACRP-F gate route: routing descriptor, method, entrypoint route, lock, run declaration, retrospective-material rule | |
| Workstreams in scope | |
| Write paths inside the project root | |
| Artifacts held by this run as mutable owner (also listed in the entrypoint) | |
| Run-specific acceptance criteria | |
| Stop conditions | |

**Scope changes:** <Each narrowing with its reason; each broadening with the new instruction that authorized it.>

## 3. Baseline and eligibility

**Baseline:** `baseline_commit` <full SHA>; frozen on <date>. Drift check at execution start: <none | refrozen at <SHA> because ...>.

**Baseline artifacts at `baseline_commit`:**

| Subject | Artifact | Path | Role, authority state, and frozen-release, byte-lock or recorded-hash state |
|---|---|---|---|
| | monograph / model / state / relationship / voice / ordinary-life / validation | | |

**Eligibility outcome:** <ELIGIBLE | ELIGIBLE_WITH_LIMITS | NOT_ELIGIBLE>, with reasons against Protocol Section 2.2.

**Baseline assessment:** maturity; source availability and route; qualification record state; validation history with exposure, by rule and model version; continuity and chronology constraints; execution capability.

**Current-state consistency findings:** <Each disagreement among the entrypoint, routers, model headers, ledger coverage and registry notes, and how this run resolves or bounds it.>

**Limitation diagnosis:**

| Deficiency | Subject and workstream | Evidence | Principal limitation (Protocol Section 2.4) | Work it calls for |
|---|---|---|---|---|

## 4. Source inventory and inspection lanes

| Source or tranche | Admitted? | Requirement | Inspection state | Lane | Route and limits (zero where none) |
|---|---|---|---|---|---|
| | yes | REQUIRED / OPTIONAL / OUT_OF_SCOPE | PENDING / PARTIAL / COMPLETE_FOR_DECLARED_SCOPE / UNAVAILABLE / NOT_APPLICABLE | TEXT / STILL_IMAGE / BUNDLE_MEDIATED / CONTINUOUS_AV | |

**Diagnostic selection (MACRP-T):** the rule, the units chosen and rejected with reasons, the adverse units included, and what the selection cannot show.

**Uncited-source search:** the source drawn independently of baseline citations, who searched it, and its scope.

```yaml
# Topology Section 5 profile fields, plus the pass's independent-context check.
execution_profile:
  product_surface: null
  tool_runtime_location: null
  observation_date: null
  capability_scope: null
  source_transport: null
  filesystem_read: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  filesystem_write: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  image_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  audio_content_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  continuous_av_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  git_write: "NOT_ASSIGNED | VERIFIED | UNVERIFIED | UNAVAILABLE"
  inspection_method: null
  inspection_lanes: []
  independent_contexts: "VERIFIED | UNVERIFIED | UNAVAILABLE"
```

## 5. Configuration, roster and workstream ownership

**Configuration:** <Dense | Standard | Bounded>, with the reason and any reduced-configuration justification.

**Planned roster:**

| Role | Context type and runtime | Split (workstream, subject or tranche) | Independence notes |
|---|---|---|---|
| Principal | | | |
| Specialist | | | |
| Reviewer A | | | |
| Reviewer B (owns workstream 12) | | | |
| Probe designer | | | Never a reviser |
| Probe respondents | | | |
| Probe judges | | | |

| Workstream | Owner role | Applicable? Reason if not |
|---|---|---|
| 1 Psychology | | |
| 2 Cognition | | |
| 3 Interiority | | |
| 4 Behavioral microanalysis | | |
| 5 Ordinary life | | |
| 6 Linguistic behavior | | |
| 7 Humor and play | | |
| 8 Relationship conditioning | | |
| 9 Ethics and conflict | | |
| 10 Competence and agency | | |
| 11 Longitudinal development | | |
| 12 Adversarial evidence | Reviewer B, with every specialist reporting adverse evidence | |

## 6. Assignment packets and participation receipts

**Assignment packets:** for each participant with controlled exposure, the packet's contents (source routes, metadata, method constraints, workstreams, conventions) and what it withheld.

One receipt per participant. Record observed facts only.

| Participant (role, not provider) | Context separation | Material actually inspected | Saw baseline, draft or probe material? | Auto-loaded instructions | Latent knowledge (recognized the work?) | Frozen findings (path and commit) | Observed model or settings |
|---|---|---|---|---|---|---|---|

**Exposure incidents:** <Any contamination, what it touched, and the credit removed.>

## 7. Observations, occurrences and frozen findings

Link to the project ledger rows, targeted records or unit records that hold observations (Protocol Section 7.1), and to each participant's frozen finding record with its commit. Do not copy source text beyond brief anchors.

**Occurrence register:**

| Canonical occurrence ID | Locator | Specialist-local IDs mapped | Baseline citations mapped | Re-presentations |
|---|---|---|---|---|

## 8. Reconciliation register

| Finding ID | Occurrence IDs | Baseline claim or locator | Source inspected by the finder? | Disposition (Protocol Section 8.1) | Claim transition | Resolution and evidence | Affected homes |
|---|---|---|---|---|---|---|---|

**Unresolved conflicts and rival readings retained:** <List.>

## 9. Planned and delivered outputs

| Output | Subject and state | Canonical home or successor path | Draft path (tranche 3) | New, revised or successor | Authority at acceptance | Acceptance reviews |
|---|---|---|---|---|---|---|
| | | | | | | self-containment / fidelity / name-and-reference / rule audit |

## 10. Test strategy and results

**Strategy:** the battery per subject (Protocol Section 10.2), the control arms, any stratified sample for a large cast, and each omission with its reason.

**Probe set:** designer <role>; custodian <who holds the sealed set>; sealed digest <SHA-256> recorded at <commit> before revision; full set committed at <commit> after the revised artifacts were frozen; digest check <passed | failed>; probe exposure <SEALED_FROM_REVISERS | REVISERS_EXPOSED, with reason>.

| Probe ID | Test (A-G) | Subject and state | Varied variable or conditions | Untargeted? | Outcome exposure | Latent knowledge | Probe exposure | Condition (baseline / revised / control / monograph-only) | Respondent | Judge | Result | Calibration | Limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Generated responses are noncanonical and never evidence.

## 11. Baseline comparison

| Dimension of change (Protocol Section 11) | Baseline state | Revised state | Evidence and probes (rule IDs and model versions) |
|---|---|---|---|

**Overconfidence found in the baseline:** <List.>

**What did not improve, and why:** <List.>

## 12. Acceptance

| Criterion (Protocol Section 12.1) | Met? | Evidence or blocker |
|---|---|---|
| 1 Authorized and bounded | | |
| 2 Coverage appropriate to scope | | |
| 3 Genuine independent participation | | |
| 4 Traceable source-grounded findings | | |
| 5 Reconciliation against authority | | |
| 6 Integrated, differentiated models | | |
| 7 Chronology, knowledge and control states | | |
| 8 Negative constraints and abstention | | |
| 9 Independent fidelity review | | |
| 10 Proportionate testing with exposure recorded | | |
| 11 Baseline comparison | | |
| 12 Persistent uncertainty documented | | |
| 13 Authority treatment and publication | | |
| 14 Resumable state if incomplete | | |
| 15 Leads | | |
| Run-specific criteria | | |

**Name-and-reference check (handoff Section 15.6):** sampled scope and material findings.

## 13. Completion, remaining gaps and leads

**Completion statement:** <What the run did and did not establish, within its declared scope.>

**Remaining items:** <Each as an evidence-backed limitation, an evidence gap the admitted source cannot close, or deferred work, with its next owner.>

**Discovery leads:** <Paths, stable anchors, dimensions and coverage boundary per subject; unenrolled substantial analysis found.>

**Evaluation leads:** <Per subject: what changed per workstream and evaluator dimension, tests and their exposure facts, new evidence-backed limits and remaining gaps. No tier or grade.>

## 14. Checkpoints and resumption

| Stage | Stage state | Commit | Audit (head and result) | Verified by | Next authorized action |
|---|---|---|---|---|---|
| 1 Configuration and baseline | | | | | |
| 2 Independent findings frozen (or MACRP-F unit transactions) | | | | | |
| 3 Drafts of reconciled and revised artifacts | | | | | |
| 4 Acceptance and completion | | | | | |
