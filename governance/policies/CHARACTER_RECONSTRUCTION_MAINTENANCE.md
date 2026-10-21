# Character reconstruction maintenance

This is the canonical operating policy for the scheduled character reconstruction evaluator. The assessment ontology, schema binding, canonicalization, hashing, and validation boundary are owned by `../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md`; this policy owns how the evaluator applies them. It grants no authority beyond what is stated here.

## Ownership and execution

The owner-authorized reconstruction evaluator is the sole routine writer of:

- `characters/reconstruction_capabilities.jsonl`, the canonical production capability registry; and
- `characters/CHARACTER_RECONSTRUCTION_INDEX.md`, its deterministic generated view, produced only by `tools/generate_reconstruction_index.py`.

The evaluator decides what an exact, commit-bound evidence set can responsibly support for one discovery analysis subject. It does not decide whether substantial analysis exists, define entity or subject identities, curate evidence references or coverage, or revise analytical prose. Those remain with the character curation agent under `CHARACTER_DISCOVERY_MAINTENANCE.md` and with the owning `series/` or `studies/` projects. Neither global registry is a substitute for a monograph, reconstruction model, or behavioral ledger in its canonical analytical home.

The two-file boundary applies to the evaluator's authored delta. It grants no authority to modify `characters/registry.jsonl`, `CHARACTER_ANALYSIS_INDEX.md`, analytical prose, evidence or authority metadata, schemas, tools, workflows, other registries, governance records, or Drive files. The repository validator enforces the boundary mechanically: a delta that changes either production output may change no other path unless the same reviewed change also amends `governance/repository-controls/reconstruction-capability-policy.json`, which only an owner-reviewed governance change may do.

The recurring task runs in a cloud environment with Git, Python, the hash-locked validation dependencies, and authenticated GitHub access. Its schedule and credentials are configured externally by the owner. This policy does not install, schedule, or activate a task.

## Publication phases

`governance/repository-controls/reconstruction-capability-policy.json` is the machine-readable publication gate.

- `CALIBRATION` is the initial phase. The registry may hold only `CANDIDATE` records and their `STALE` or `SUPERSEDED` history. `REVIEWED` is rejected by validation. No evaluator PR is automatically integrated; the owner reviews and merges every publication.
- `ROUTINE` begins only through an owner-reviewed governance change that records calibration acceptance under `governance/reports/` and names that record in `calibration_acceptance_record`. The evaluator cannot make this change.

Production never admits `UNASSESSED` placeholder records. Eligible-but-unassessed state is derived from the discovery registry and the absence of a capability record; manufacturing records to populate the registry is prohibited.

## Assessment lifecycle

The schema vocabulary is unchanged: `UNASSESSED`, `CANDIDATE`, `REVIEWED`, `STALE`, `SUPERSEDED`.

- `CANDIDATE` is a complete, validated, visibly provisional assessment. It carries the provisional overall tier and claims a reviewer will be asked to accept unchanged.
- `REVIEWED` records that the human review below accepted exactly that candidate content. An agent never certifies its own assessment as human-reviewed.
- `STALE` records that the evaluator has reconciled an assessment that no longer applies; it keeps its historical basis, claims, and digest and states the reason.
- `SUPERSEDED` links a predecessor to a successor that replaces it.

A record first enters the registry as `CANDIDATE`, and only for an `INCLUDED` discovery subject; historical statuses arise only from validated transitions. A published record is never deleted and its claim payload never changes. Only `assessment_status`, `stale_reason`, and `superseded_by_assessment_id` may change, and only along `CANDIDATE -> REVIEWED | STALE | SUPERSEDED`, `REVIEWED -> STALE | SUPERSEDED`, and `STALE -> SUPERSEDED`. Any change to scope, evidence, grades, limits, method, or tier is a new assessment ID whose `supersedes_assessment_id` names its predecessor. Registry lines are ordered by ASCII `assessment_id`.

Overall A-E tiers are evidence-grounded human judgments of the whole evidence set. They are never computed from, averaged over, or capped by dimension grades, and no tier is assigned to make a record schema-valid.

## Historical validity and effective currentness

Two different questions are answered separately:

- **Historical validity** asks whether a record correctly binds its evidence, scope, and authority at its own `basis_commit`. It is checked on every validation and is always blocking. It never changes after publication, so valid history remains reproducible.
- **Effective currentness** asks whether a `CANDIDATE` or `REVIEWED` record still applies to a later integrated snapshot. It is derived, never stored, and reported as `CURRENT_REVIEWED`, `CURRENT_PROVISIONAL`, or `EFFECTIVELY_STALE` with explicit reasons.

Validation blocks an effectively stale record only when the change being validated adds it or changes its lifecycle fields. An untouched record made stale by later series, study, or discovery integration produces a validator notice and is reconciled by the evaluator's next run; ordinary analytical and discovery publication never waits for this policy. The generated index records publication state only and states that it certifies no present readiness.

Consumers verify present applicability with:

```bash
python tools/reconstruction_status.py currentness --snapshot commit --commit <full-main-sha>
```

`--assessment <id>` restricts the report and `--require-current-reviewed` exits nonzero unless each selected assessment is `CURRENT_REVIEWED`. A recorded `REVIEWED` label alone is never present-day readiness.

## Inputs and Git-derived work discovery

Before each run, read the live repository instructions, authority records, integration checklist, this policy, the specification and schema, `characters/README.md`, and the discovery maintenance policy. Verify repository identity and approved commit identities.

Capture the full current `main` SHA. Derive all work from integrated Git state at that SHA:

```bash
python tools/reconstruction_status.py work-queue --snapshot commit --commit <full-main-sha> --since <last-verified-checkpoint-sha> [--deferred <subject-id> ...] [--hint <subject-id> ...]
```

The queue is keyed by exact `analysis_subject_id`; each subject appears once with all applicable reasons merged. Its tiers are the required priority:

1. `EFFECTIVELY_STALE_ASSESSMENT`: a current-claim record no longer applies; historical validity failures stop the run before any queue is produced.
2. `REASSESSMENT_NEEDED`: an included subject whose assessments are all historical.
3. `NEWLY_ELIGIBLE`: an `INCLUDED` subject enrolled since the checkpoint.
4. `BACKFILL_UNASSESSED`: any other eligible subject without an assessment.
5. `DEFERRED_EVIDENCE_CHANGED`: a subject the evaluator deferred whose discovery scope, coverage, curation, or reviewed-evidence membership has since changed.

Currentness reasons cover subject absence, scope, curation and coverage changes, reviewed-evidence membership, evidence location and anchors, referenced bytes, and authority or supersession state. A change to an unrelated file never creates work. Discovery records are the only source of eligibility; prominence, appearance frequency, or the existence of a monograph is never treated as readiness.

The evaluator never depends on the discovery agent's private memory, checkpoint, or undocumented communication. Advisory hints only annotate queued subjects; a missing hint never hides work and a duplicate hint never duplicates it.

## Standing selection authorization

The owner grants presumptive approval for all future additions to the evaluator's assessment workload from eligible `INCLUDED` discovery subjects, including additions to the calibration cohort and later backfill batches. The evaluator may select these subjects, prepare `CANDIDATE` assessments, and submit them for review without separate owner approval of each subject or batch. Selection follows the queue priorities, evidence requirements, bounded batch sizes, and path limits in this policy; it never authorizes enrollment in discovery or assessment of an ineligible subject.

This standing approval is for selection and candidate preparation only. It does not accept assessment claims, establish human review, accept calibration, promote a record to `REVIEWED`, change the publication phase, or grant additional publication or merge authority. The existing validation, human-review, publication, and integration requirements continue to apply.

## Initial population and backfill

There is no deadline for assessing every registered subject. Backfill proceeds in bounded batches selected from the queue after higher tiers are empty, preferring one shared basis commit per batch so validation and review cost stay proportional. A subject may be deferred for insufficient evidence, unresolved authority, ambiguous identity, or reviewer unavailability; deferral is recorded in the checkpoint and the PR description, never as a registry record.

Do not equate discovery inclusion with a capability, and do not assess a subject merely to increase coverage.

## Preparing a candidate assessment

1. Choose a basis commit that is a reviewed commit on `main`. Validation rejects a basis that is not an ancestor of the integrated history.
2. Read the subject's discovery row and every reviewed evidence item intended for use at that commit, together with the governing project method, source boundary, and current-state entrypoint. Reference only `REVIEWED` evidence curated directly on that exact subject; composites never borrow leaf evidence.
3. Record one claim per controlled dimension and scenario. Grade only what the cited evidence supports; use `NOT_ASSESSED` rather than inference from silence. Distinguish `EVIDENCE_BACKED` limits from `EVIDENCE_GAP` limits, and bound every assessed `CROSS_SCENARIO` claim.
4. Set `source_boundary` and `temporal_boundary` from the evidence, never broader than the subject. Name the method as this policy and the specification with an exact method version.
5. Compute the exact claim union and `CHARACTER_EVIDENCE_SET_V1` digest with the repository implementation; never hand-compute or approximate it.
6. Stage the registry, run `python tools/generate_reconstruction_index.py --snapshot index`, stage the index, and run `python tools/prepare_commit.py --base origin/main --check`. Confirm `reconstruction_status.py currentness` reports the new record as current against the staged index or the reconciled head.

Structural validation cannot establish that a grade is correct. A candidate is a proposal for review, not a finding.

## Human review and promotion

Promotion from `CANDIDATE` to `REVIEWED` requires a human reviewer, the owner or a human the owner designates, who:

- reads the candidate's cited evidence at its basis commit rather than the evaluator's summary alone;
- tests each assessed dimension, scenario state, limit, and the overall tier against that evidence;
- records the decision in the promotion PR, naming each accepted `assessment_id`, its basis commit, and its evidence-set digest; and
- rejects, rather than edits, a candidate whose claims need change. A revised assessment is a new candidate superseding the old one.

The evaluator may prepare a promotion commit only to transcribe such a recorded decision; it never decides one. Only the owner merges a promotion. Promotion validates only if the record is effectively current at the reconciled head; if evidence changed after review, reassess.

## Calibration protocol

Calibration precedes `ROUTINE` publication. Under the standing selection authorization, the evaluator selects a deliberately diverse pilot of eligible existing subjects, for example:

- mature bounded reconstruction models with explicit validation or evaluation artifacts;
- subjects with substantial literary analysis but no strong operational model;
- distributed-substantial subjects whose evidence lives in shared readings;
- temporal-state, adaptation, player-archetype, and composite subjects; and
- a subject with active-provisional evidence.

The owner approved the following initial pilot cohort on 2026-10-20. This records selection approval, not completed assessments or accepted capability claims.

| Analysis subject | Calibration purpose |
| --- | --- |
| `shokugeki-no-soma:ikumi-mito@manga` | Bounded operational reconstruction and recipient-conditioned behavior. |
| `86-eighty-six:shinei-nouzen@original-light-novels` | Longitudinal psychological states, source-supported voice, and temporal limits. |
| `blue-archive:aru@game` | Distributed substantial evidence within a narrow chapter boundary. |
| `mass-effect:commander-shepard@paragon-player-archetype` | Player-archetype interpretation versus behavioral and dialogue sufficiency. |
| `the-idolmaster:yonai-p@u149-anime` | Adaptation-specific professional and relationship-conditioned behavior. |
| `shuukura:mio-komatsu@original-light-novel` | Narrow active-provisional evidence, knowledge boundaries, and ambiguity. |

Verify each subject's eligibility and evidence against current `main` before assessment. The initial cohort does not exercise separately registered temporal-state or composite identities; those categories remain untested until eligible subjects and adequate evidence exist. Do not invent identities to complete a calibration category. Future cohort additions follow the standing selection authorization and the same calibration requirements.

For each pilot subject, the evaluator prepares a candidate and a calibration note in the PR description giving, per assessed claim, the evidence locators relied on, the strongest counterevidence, and why a higher and a lower grade were rejected. The calibration set must collectively test whether the evaluator distinguishes:

- literary interpretation from behavioral prediction;
- substantial evidence from model sufficiency;
- broad reconstruction readiness from domain-bounded readiness;
- source-supported voice from merely fluent generated dialogue;
- historical psychological states from later character development;
- evidentiary contradiction from ordinary ambiguity; and
- speculative counterfactuals from supported extrapolations.

Independent review is semantic: the reviewer re-derives judgments from the evidence and records agreements, disagreements, and corrections. Systematic overgrading, unsupported scenario readiness, or limits stated as gaps when evidence affirmatively shows them blocks acceptance until the method is corrected and the affected pilots are re-run.

The readiness gate for `ROUTINE` is an owner-accepted calibration record under `governance/reports/` stating the pilot set, the reviewed outcomes, each distinction exercised, the fixed method version, and remaining known weaknesses. The owner then sets the phase and record in the policy file through a governance change. Pilot candidates may be published during calibration only as `CANDIDATE` records through owner-merged PRs.

## Discovery and reconstruction referrals

Work discovery is Git-derived. Referrals are prioritization hints only and never authority to publish, promote, or enroll anything.

- **From discovery.** An existing discovery PR description may contain a section titled `Reconstruction referrals (advisory, nonauthoritative)` naming the exact subject, the reviewed evidence references, the relevant basis commit, the material analytical change, apparent limits or gaps, and why a review may help. The evaluator may read such sections in PRs merged since its checkpoint and pass the subjects as `--hint` values. A referral cannot add a subject the queue does not already contain.
- **To discovery.** If the evaluator finds substantial character analysis that is not enrolled, it records the path, apparent subject, and reason under `Discovery candidates (advisory, nonauthoritative)` in its current PR description, or in its task report when it has no PR, and keeps it in its checkpoint until a later discovery PR or registry state resolves it. It never invents or adds a discovery identity, and never opens a PR solely to transmit referrals.

## Branch, publication, and integration

1. Use the exact reusable `character-reconstruction` branch and at most one open PR to `main`. Reconcile current `main` by an ordinary merge without force-pushing or rewriting published history. After a squash merge, merge current `main` into the branch before further work; recreate the branch from `main` only after a verified deletion.
2. The complete branch delta may contain only the two production outputs.
3. A PR whose only registry changes are `STALE` reconciliations that `reconstruction_status.py currentness` reports at the reconciled head, with `stale_reason` citing the derived reasons, is **mechanical maintenance**. Any other change, including a new candidate, a supersession, or a promotion, is **substantive**. While substantive work is open, append mechanical reconciliations to that PR rather than opening a second one; the whole PR is then substantive.
4. Publish normally under approved identities. The Repository audit runs on pushes to `character-reconstruction` and reports `Repository integration audit` directly on the exact audited SHA; this branch never enters the series/study pending-housekeeping state. If a token-originated push does not start a run, use the existing exact-commit or manual dispatch and verify the audited SHA.
5. Merging requires a successful `Repository integration audit` for the exact current head, both heads rechecked, and an enabled merge method compatible with live protection. Substantive PRs and every PR during `CALIBRATION` are merged only by the owner after review. During `ROUTINE`, the owner authorizes the evaluator to merge mechanical-maintenance PRs itself under the same checks. Passing checks never establish semantic correctness and confer no other merge authority.
6. Verify the integrated patch and the Repository audit for the exact integration commit on `main`. Report a post-merge failure as integrated but unverified; never revert or rewrite `main` automatically.

## Checkpoints and coverage accounting

Keep durable checkpoints in cloud task storage and in the relevant PR description, never in a disposable checkout. Record the reviewed `main` SHA, the queue derived at it, subjects assessed, deferred subjects with reasons and basis SHAs, mechanical reconciliations, open PR number and head, integration SHA, post-merge audit result, and outstanding referrals in both directions.

Track review, publication, integration, and post-merge verification separately. Advance the completed-coverage checkpoint only to work verified on `main`. An interrupted or failed run leaves the previous checkpoint in force and preserves unfinished work on the branch or in the checkpoint; it never silently discards it. Without a trustworthy checkpoint, establish a documented baseline from the integrated registry and audit records and recompute the full queue.

## Concurrency and conflicts

Serialize evaluator runs. Inspect unexpected branch content before any write and preserve it. The discovery registry, analytical evidence, and `main` may advance at any time; before every push and merge, recheck heads, re-derive currentness for the PR's added or transitioned records, and revalidate. Resolve conflicts only within the two outputs by re-deriving them from the reconciled registry and the generator, never by whole-file `ours` or `theirs` selection. A conflict that requires discovery or analytical changes is reported, not repaired.

## Failure reporting and recovery

Successful no-change runs remain quiet; do not create empty commits or PRs. Report verified integrations, substantive unresolved findings, historical-validity failures, access or validation failures, blocked integration, post-merge failure, incomplete review, and outstanding referrals. A historical-validity failure on `main` is a repository defect: report it with the exact validator output and repair it forward through an authorized change. Never disable or weaken a check to complete a run.

## Activation and scheduling

Merging the activation change makes this policy and the empty production registry effective but publishes no assessment. The owner separately configures the scheduled task, its credentials, and the cloud checkpoint store, and later accepts calibration. Pilot and subsequent subject selection follow the standing selection authorization above. Until calibration is accepted through the required governance change, the evaluator may prepare calibration candidates and publish them only through owner-reviewed, owner-merged PRs.
