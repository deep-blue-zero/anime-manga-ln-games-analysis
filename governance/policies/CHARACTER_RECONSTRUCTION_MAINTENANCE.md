# Character reconstruction maintenance

This is the canonical operating policy for the scheduled character reconstruction evaluator. The assessment ontology, schema binding, canonicalization, hashing, and validation boundary are owned by `../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md`; this policy owns how the evaluator applies them. It grants no authority beyond what is stated here.

## Ownership and execution

The owner-authorized reconstruction evaluator is the sole routine writer of:

- the capability registry partitions `characters/reconstruction_capabilities/<namespace>/<subject>.jsonl`, the canonical production capability registry ([Registry storage](#registry-storage) specifies the layout); and
- `characters/CHARACTER_RECONSTRUCTION_INDEX.md` with the namespace pages `characters/reconstruction_index/<namespace>.md`, its deterministic generated view, produced only by `tools/generate_reconstruction_index.py`.

The evaluator decides what an exact, commit-bound evidence set can responsibly support for one discovery analysis subject. It does not decide whether substantial analysis exists, define entity or subject identities, curate evidence references or coverage, or revise analytical prose. Those remain with the character curation agent under `CHARACTER_DISCOVERY_MAINTENANCE.md` and with the owning `series/` or `studies/` projects. Neither global registry is a substitute for a monograph, reconstruction model, or behavioral ledger in its canonical analytical home.

The output boundary applies to the evaluator's authored delta. It grants no authority to modify the discovery registry partitions under `characters/registry/`, `CHARACTER_ANALYSIS_INDEX.md` or its pages under `characters/index/`, analytical prose, evidence or authority metadata, schemas, tools, workflows, other registries, governance records, or Drive files. The repository validator enforces the boundary mechanically: a delta that changes any reconstruction output may change no other path unless the same reviewed change also amends `governance/repository-controls/reconstruction-capability-policy.json`, which only an owner-reviewed governance change may do.

The evaluator follows the shared rules for scheduled agents in `../../AGENTS.md`.

## Registry storage

The registry is one logical registry stored as one JSONL partition per analysis subject, with a generated view to match:

```text
characters/reconstruction_capabilities/<namespace>/<subject>.jsonl   every assessment of one subject
characters/CHARACTER_RECONSTRUCTION_INDEX.md                         generated root index, one table row per assessment
characters/reconstruction_index/<namespace>.md                       generated namespace page: full recorded claims, limits and evidence
```

- A record's partition is fixed by its `analysis_subject_id`: `<namespace>` is the part before `:` and `<subject>` the part after it. Every assessment of a subject, current and historical, is in that one file, so a file grows only with the subject's own reassessment history and never with how many subjects a franchise registers.
- Within a partition, records are in strictly ascending ASCII `assessment_id` order, one record per line, with no blank lines and a final LF. `assessment_id` is unique over the whole registry, and tools read the whole registry as one logical registry in ASCII `assessment_id` order, the order the retired single file kept. A partition left with no records is deleted.
- A current snapshot has at least one partition. An absent registry is a missing input, never an empty registry; only a read of a commit from before the registry existed treats absence as no records.
- `python tools/reconstruction_registry.py normalize` moves worktree records into their partitions in canonical order without changing a byte of any record, then lists every registry path whose worktree differs from the Git index. That list, not the set of files it rewrote, is what to stage: a lifecycle transition made in place or a new partition written already sorted needs no rewriting but still needs staging. `replay --base <commit> --head <commit>` applies the records changed between two commits, in either layout, to the worktree partitions; the procedure below uses it to carry assessments across the migration. `export --snapshot index`, or `--snapshot commit --commit <sha>`, prints the whole logical registry as one JSONL stream for a consumer or a comparison. The export is a view and is never committed.
- `python tools/generate_reconstruction_index.py --snapshot index` writes the root index and the namespace pages, removes a page whose namespace no longer has records, and lists every generated output to stage. Tools read the registry only through `read_reconstruction_registry` in `tools/character_index_core.py`.

The single file `characters/reconstruction_capabilities.jsonl` was retired on 2026-11-06 when it neared the 1 MiB review threshold; the migration moved every record byte for byte. Current snapshots reject that file. Commits from before the migration are still read in the old layout, so `reconstruction_status.py` verifies them and the validator compares a change with pre-migration published history. The publication gate records the layout in `registry_layout` (`SUBJECT_PARTITIONS_V1`), which validation requires to match the tooling. If one partition or one generated page ever approaches 1 MiB, splitting it further needs a reviewed tooling change that amends `registry_layout`, the route by which a change may touch the outputs beside other paths; never raise the threshold or add a named size exception for a living registry file.

### Carrying a pre-migration branch across

A branch whose unmerged assessments predate the 2026-11-06 partition migration changes the retired single file, so merging `main` would conflict on reconstruction outputs, and the merge gate rejects any merge that conflicts on them. Carry those assessments across without a conflicted merge:

1. Note the branch head `H` and the merge base `B` of `H` and `origin/main`.
2. In a commit touching only reconstruction outputs, restore them to the merge base: `git checkout B -- characters/reconstruction_capabilities.jsonl characters/CHARACTER_RECONSTRUCTION_INDEX.md`.
3. Merge `origin/main`; it now applies cleanly and brings the partitions and namespace pages.
4. Run `python tools/reconstruction_registry.py replay --base B --head H`. It applies exactly the records the branch added or transitioned, and stops before writing if `main` also changed one of those records; reconcile such a record by hand. Stage each `registry path to stage` it reports, run `python tools/generate_reconstruction_index.py --snapshot index`, stage each `generated output to stage` it reports, and commit the reconstruction outputs as an ordinary publication commit.
5. Re-derive currentness for the carried records and run the commit gate as before any push.

A candidate withdrawn only because the single file was full is prepared again through the ordinary procedure.

## Publication phases

`governance/repository-controls/reconstruction-capability-policy.json` is the machine-readable publication gate; it also records the registry's storage layout ([Registry storage](#registry-storage)).

- `CALIBRATION` is the initial phase. The registry may hold only `CANDIDATE` records and their `STALE` or `SUPERSEDED` history. `REVIEWED` is rejected by validation. The merge gate leaves every reconstruction PR for the owner, who reviews and merges each publication.
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

`--assessment <id>` restricts the report. `--require-current-reviewed` exits 0 only when the selection is nonempty and every selected assessment is `CURRENT_REVIEWED`, and records `current_reviewed_certified` in its output; an empty selection, including an empty registry, exits 1 and never certifies readiness. Unknown IDs and historical-validity failures exit 2. A recorded `REVIEWED` label alone is never present-day readiness.

## Inputs and Git-derived work discovery

Before each run, read the live repository instructions, integration checklist, this policy, the specification and schema, `characters/README.md`, and the discovery maintenance policy. Verify repository identity and approved commit identities.

Capture the full current `main` SHA. Derive all work from integrated Git state at that SHA:

```bash
python tools/reconstruction_status.py work-queue --snapshot commit --commit <full-main-sha> --since <last-verified-checkpoint-sha> [--deferred <subject-id> ...] [--hint <subject-id> ...]
```

The queue is keyed by exact `analysis_subject_id`; each subject appears once with all applicable reasons merged. Its tiers are the required priority, apart from the backfill slot reserved under [Initial population and backfill](#initial-population-and-backfill):

1. `EFFECTIVELY_STALE_ASSESSMENT`: a current-claim record no longer applies; historical validity failures stop the run before any queue is produced.
2. `REASSESSMENT_NEEDED`: an included subject whose assessments are all historical.
3. `NEWLY_ELIGIBLE`: an `INCLUDED` subject enrolled since the checkpoint.
4. `BACKFILL_UNASSESSED`: any other eligible subject without an assessment.
5. `DEFERRED_EVIDENCE_CHANGED`: a subject the evaluator deferred whose discovery scope, coverage, curation, or reviewed-evidence membership has since changed, or whose reviewed evidence bytes or authority classification changed without a discovery edit. `--deferred` requires `--since`; only the deferred subjects' reviewed evidence paths are compared, at the cost of one checkpoint snapshot.
6. `ANALYSIS_FRONTIER_ADVANCED`: a subject whose claims all still apply, but where current-authority analysis under the roots of its reviewed evidence (`series/<slug>` or `studies/<slug>`) has gained at least `--frontier-min-mentions` (default 10) matches of the subject's registered names in a single file since a claim's `basis_commit`. Names match by the preferred name, unambiguous aliases and their distinctive parts. The item's `frontier` lists each claim's base and every such path with its mention growth. For a deferred subject, growth is measured from the checkpoint when it is later than the basis.

Currentness reasons cover subject absence, scope, curation and coverage changes, reviewed-evidence membership, evidence location and anchors, referenced bytes, and authority or supersession state. A change to an unrelated file never makes a claim stale. Analysis that grows around a subject outside its evidence creates only tier-6 work. Discovery records are the only source of eligibility; prominence, appearance frequency, or the existence of a monograph is never treated as readiness, and mention growth is a recall heuristic for finding work, never evidence.

The frontier tier exists because works in current publication outgrow their assessments: a new volume reading or ledger entry rarely edits the evidence a claim cites, so currentness alone leaves a claim bounded at an earlier horizon. For each frontier item, read the listed paths against the claim's `temporal_boundary` and `source_boundary`:

- if the analysis extends the subject and is not on its discovery row, record a discovery lead naming the subject, the paths and the main SHA. Enrollment changes the row's reviewed evidence or coverage, which makes the claim effectively stale and returns the subject at tier 1;
- if the row already carries the extending evidence, prepare a superseding candidate at a newer basis under the usual batch limits;
- otherwise, or while a lead is outstanding, defer the subject with its reason and basis SHA, so it returns only after further growth.

A frontier item never justifies marking a record `STALE`, citing unenrolled evidence, or editing discovery.

The evaluator never depends on the discovery agent's private memory, checkpoint, or undocumented communication. Advisory hints only annotate queued subjects; a missing hint never hides work and a duplicate hint never duplicates it.

## Standing selection authorization

The owner grants presumptive approval for all future additions to the evaluator's assessment workload from eligible `INCLUDED` discovery subjects, including additions to the calibration cohort and later backfill batches. The evaluator may select these subjects, prepare `CANDIDATE` assessments, and submit them for review without separate owner approval of each subject or batch. Selection follows the queue priorities, evidence requirements, bounded batch sizes, and path limits in this policy; it never authorizes enrollment in discovery or assessment of an ineligible subject.

This standing approval is for selection and candidate preparation only. It does not accept assessment claims, establish human review, accept calibration, promote a record to `REVIEWED`, change the publication phase, or grant additional publication or merge authority. The existing validation, human-review, publication, and integration requirements continue to apply.

## Initial population and backfill

There is no deadline for assessing every registered subject, but backfill must advance. New enrollments and extended rows refill the higher tiers on almost every run, so waiting for them to empty would never reach tier 4. While the queue has tier-4 subjects, one slot of each run's candidate capacity is reserved for them. The other slots follow tier order, and mechanical reconciliations are never limited.

- A run whose capacity is a single candidate alternates. It uses the reserved slot when the previous run's candidates included no backfill subject, and follows tier order otherwise.
- Choose backfill subjects whose curated evidence is complete and stable: prefer dedicated reviewed models or monographs in projects that are not currently adding analysis of that subject, so the candidate stays current until owner review. Prefer one shared basis commit per batch so validation and review cost stay proportional.
- Deferring a backfill subject does not use the slot; take the next suitable one. Leave the slot unused only when no examined tier-4 subject has sufficient evidence.
- During `CALIBRATION`, a backfill subject is a cohort addition under the standing selection authorization.

A subject may be deferred for insufficient evidence, unresolved authority, ambiguous identity, or reviewer unavailability; deferral is recorded in the checkpoint and the PR description, never as a registry record.

Do not equate discovery inclusion with a capability, and do not assess a subject merely to increase coverage.

## Preparing a candidate assessment

1. Choose a basis commit that is a reviewed commit on `main`. Validation rejects a basis that is not an ancestor of the integrated history.
2. Read the subject's discovery row and every reviewed evidence item intended for use at that commit, together with the governing project method, source boundary, and current-state entrypoint. Reference only `REVIEWED` evidence curated directly on that exact subject; composites never borrow leaf evidence.
3. Record one claim per controlled dimension and scenario. Grade only what the cited evidence supports; use `NOT_ASSESSED` rather than inference from silence. Distinguish `EVIDENCE_BACKED` limits from `EVIDENCE_GAP` limits, and bound every assessed `CROSS_SCENARIO` claim.
4. Set `source_boundary` and `temporal_boundary` from the evidence, never broader than the subject. Name the method as this policy and the specification with an exact method version.
5. Compute the exact claim union and `CHARACTER_EVIDENCE_SET_V1` digest with the repository implementation; never hand-compute or approximate it.
6. Write the record to its subject's partition, or run `python tools/reconstruction_registry.py normalize` to place it, and stage each registry path the tool reports. Run `python tools/generate_reconstruction_index.py --snapshot index`, stage each generated output it reports, and run `python tools/prepare_commit.py --base origin/main --check`, which also applies the repository audit's 1 MiB review threshold to the staged files. Confirm `reconstruction_status.py currentness` reports the new record as current against the staged index or the reconciled head.

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

Independent review is semantic: the reviewer re-derives judgments from the evidence and records agreements, disagreements, and corrections. Systematic overgrading or undergrading, unsupported scenario readiness, or limits stated as gaps when evidence affirmatively shows them blocks acceptance until the method is corrected and the affected pilots are re-run.

The readiness gate for `ROUTINE` is an owner-accepted calibration record under `governance/reports/` stating the pilot set, the reviewed outcomes, each distinction exercised, the fixed method version, and remaining known weaknesses. The owner then sets the phase and record in the policy file through a governance change. Pilot candidates may be published during calibration only as `CANDIDATE` records through owner-merged PRs.

### Owner calibration rulings

These rulings record how the owner reads the specification's tier definitions after reviewing the first My Hero Academia and Tomozaki cohort (PR #540). They bind the evaluator's grading and add no tier criterion beyond the specification. The first cohort showed systematic undergrading: the evaluator identified operational models and supported conditional predictions, then rejected B because those predictions had limits.

**B and C.**

- B is a strong inferential model with explicit bounded uncertainty. The evidence explains why the character's response changes when the relationship, stakes, knowledge or chronology change, and the record states where that explanation stops. Partial probe results, medium-confidence reconstructions and unsupported domains narrow a B's scope and confidence; on their own they do not make the record C.
- C is specialist-supported interpretation, possibly with narrow extrapolation, where the evidence does not establish that discriminating account. C is compatible with `CONDITIONAL` scenario readiness: it excludes unconstrained simulation, not bounded extrapolation.
- Judge the tier within the record's declared scope. Missing support outside that scope restricts use; it does not lower the tier. Count each uncertainty once: if it narrows a scenario's conditions, it is not also a reason to deny the tier that accommodates the narrowing.
- Distinguish productive uncertainty from insufficiency. Not knowing the exact wording, topic or affect is productive uncertainty. Being unable to tell which of the competing motives decides a choice is insufficiency.
- These are not tier criteria: `DIALOGUE` readiness, blind or held-out validation, ordinary-life coverage, and the number of B dimensions or `CONDITIONAL` scenarios. Their absence limits confidence or permitted use and is recorded as a limit. A partial or retrospective probe is evidence: state what it shows about the model.
- A model derived from a monograph is one line of evidence, not independent corroboration. Derivation from analytical evidence is expected and is not a deficiency.
- A generated response is noncanonical by nature. For `DIALOGUE` and voice, ask whether the evidence constrains the output enough for the declared use. "Illustrative, never quotation" bounds the use of output; it is not a finding that output is unsupported. A project's caveat that some strings are retrieval aids applies only to the strings it names.
- A useful model predicts the character's mistakes and overreach, not only prudent or ethical conduct.
- For each overall tier, the calibration note explains both why the next tier up would overclaim and why the next tier down would understate what the evidence shows. Earlier candidates are not precedent; these rulings are.

**Safeguards that stay.**

- A temporal boundary limits which evidence may be used, as in a validation freeze. It never limits what the character knows: memories revealed late in the source belong to the character at every earlier state they predate.
- Chronology conditions split a volume at a located state change inside it. One whole-volume label never covers two capability states.
- Scenario conditions cover the relationships the evidence samples. A transfer to a comparable relationship is a separate, lower-confidence condition with its own justification.
- An exceptional or terminal transformation is not generalized into a transferable policy, and behavior is attributed to whoever is in control in that state.

**Anchors.** These explain the reasoning; they set no quota or threshold.

- *Bakugo and Midoriya, bounded B.* Each model specifies what changes the response. For Bakugo that is competence, trust, perceived pity, task meaning and danger (BK04a–c, BK09). For Midoriya it is the difference between emergency initiative, sustained overtraining and restraint that preserves a later rescue (MI01a–c, MI11). Exact emotional expression, private life and adult outcomes stay outside scope, and that does not lower the tier.
- *Toga, C.* The model makes narrow predictions about attraction, perceived rejection, bereavement and resources. It cannot yet say which priority wins when recognition changes the relationship (TG-V01), and her terminal correction does not transfer.
- *Shigaraki, a scope case.* Autonomous Tomura has a B-like submodel, but a whole-scope record that also admits override and fused states does not establish it. The tier follows the declared scope.

**Directed supersessions.** The owner does not accept the twelve PR #540 candidates as they stand and directs a superseding candidate for each. The expected outcome is the owner's reading of the evidence, not a grade to copy. The evaluator re-derives every claim at a current basis; where the evidence does not support the expected outcome, it publishes the tier the evidence supports and explains the difference in the calibration note.

| Subject | Expected outcome | Corrections |
| --- | --- | --- |
| `my-hero-academia:bakugo-katsuki@manga` | B | — |
| `my-hero-academia:midoriya-izuku@manga` | B | — |
| `my-hero-academia:todoroki-shoto@manga` | Bounded B | Domestic routine, humor and exact affect stay limited. |
| `my-hero-academia:endeavor@manga` | Bounded B | Covers the professional and accountability mechanisms (EN03–07), not every unprecedented family crisis; EN-V01's partial relational result stays a limit. |
| `my-hero-academia:all-might@manga` | B | His youth and Nana's teaching are his knowledge throughout. Split V11 and V40 at the located state changes. Mundane-social conditions cover the sampled Midoriya and Inko interactions, with any transfer to a comparable student as a separate, lower-confidence condition. `NEGATIVE_EVIDENCE` B. The V39 correction about his intent stays local. |
| `my-hero-academia:shigaraki-tomura@manga` | C | Restrict cross-scenario conditions to autonomous-Tomura states. Narrow ethical readiness to located positions. Professional readiness drops V38–V41 Tomura unless evidence after augmentation supports it. |
| `my-hero-academia:himiko-toga@manga` | C | Correct the dialogue rationale under these rulings. |
| `my-hero-academia:todoroki-toya@manga` | C | Correct the dialogue rationale under these rulings. |
| `tomozaki:kikuchi-fuka@light-novel` | B | Keep the monograph's restriction on freeform Japanese. |
| `tomozaki:tomozaki@light-novel` | B | Durability under another unique-usefulness crisis is untested and limits that domain. |
| `tomozaki:hinami@light-novel` | Bounded B | Hidden priorities and novel crisis responses stay outside scope. |
| `tomozaki:mimimi@light-novel` | Bounded B | Exact refusal or contact outcomes and severe new comparison crises stay uncertain. |

- Successors take precedence over every other substantive candidate, including the reserved backfill slot, and count against the per-run candidate limit.
- Prepare a successor once its predecessor is published on `main`, with reciprocal supersession links. A predecessor still unpublished in the evaluator's open PR is withdrawn from that PR in a new commit and replaced by its successor.
- These rulings reopen no other published candidate. Before calibration acceptance, the owner decides which other pilots count as affected.

## Discovery and reconstruction referrals

Work discovery is Git-derived. Either agent may note leads for the other in its PR description: discovery may name subjects whose analysis changed materially, which the evaluator may pass as `--hint` values; the evaluator may name substantial analysis that is not enrolled. Leads are prioritization hints only. A hint cannot add a subject the queue does not already contain, and the evaluator never invents or adds a discovery identity.

## Branch, publication, and integration

1. Use the reusable `character-reconstruction` branch with at most one open PR to `main`. Merge current `main` into it without force.
2. The complete branch delta may contain only the reconstruction outputs: the registry partitions, the root index and its namespace pages. The merge gate accepts them from no other branch.
3. A PR whose only registry changes are `STALE` reconciliations that `reconstruction_status.py currentness` reports at the reconciled head, with `stale_reason` citing the derived reasons, is **mechanical maintenance**. Any other change, including a new candidate, a supersession or a promotion, is **substantive**. While substantive work is open, add mechanical reconciliations to that PR rather than opening a second one; the whole PR is then substantive.
4. Push and open or update the PR. The repository audit reports `Repository integration audit` directly on the exact audited SHA; this branch never waits on housekeeping.
5. During `CALIBRATION` the merge gate leaves every PR for the owner. During `ROUTINE` the CI agent may merge mechanical-maintenance PRs under `NIGHTLY_ANALYTICAL_INTEGRATION.md`, and holds substantive ones for the owner's review. Only the owner merges a promotion. Passing checks never establish semantic correctness.

## Checkpoints, conflicts and failures

In addition to the shared rules, record in the checkpoint and PR description the reviewed `main` SHA, the queue derived at it, subjects assessed, how the backfill slot was used (the subject assessed, or the subjects examined and why none qualified), deferred subjects with reasons and basis SHAs, mechanical reconciliations, and outstanding leads. Advance completed coverage only to work verified on `main`; without a trustworthy checkpoint, establish a documented baseline from the integrated registry and recompute the full queue.

The discovery registry, analytical evidence and `main` may advance at any time. Before every push, re-derive currentness for the PR's added or transitioned records and revalidate. Resolve conflicts only within the two outputs by re-deriving them from the reconciled registry and the generator. A conflict that needs discovery or analytical changes is reported, not repaired.

A historical-validity failure on `main` is a repository defect: report it with the exact validator output and repair it forward through an authorized change.
