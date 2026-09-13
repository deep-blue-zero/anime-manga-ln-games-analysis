---
series: TOMOZAKI
artifact_type: architecture_and_synthesis_role_gap_audit
scope: JP_LIGHT_NOVEL_V01-V11_PLUS_V06_5_AND_V08_5
source_boundary: "Audited Japanese light-novel EPUB corpus: numbered main Volumes 01-11 plus side-story Volumes 06.5 and 08.5; source audit dated 2026-08-29"
analytical_boundary: V11_PLUS_ROUTED_SUPPLEMENTS
analytical_generation: V2_REMEDIATION
audit_version: "1.0"
audit_date: "2026-09-13"
audit_cutoff_utc: "2026-09-13T04:37:30Z"
post_cutoff_remediation_recheck_utc: "2026-09-13T04:49:39Z"
status: canonical
release_state: immutable_checkpoint
supersedes:
  - "series/tomozaki/08 Audits and Manifests/TOMOZAKI_FULL_SERIES_SYNTHESIS_VALIDATION_AUDIT.md"
supersession_scope: "Architecture readiness, responsibility coverage, synthesis readiness, and the claim that no additional current-boundary document is required. The former audit's source-coverage, sequential-coverage, epistemic-safety, and historical repository-check results remain preserved."
superseded_by: []
do_not_use_as_current_authority: false
canonical_entrypoint: "../CURRENT_STATE_AND_CORPUS_MAP.md"
governing_architecture: "../00 Frameworks and Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md"
governing_method: "../00 Frameworks and Methods/TOMOZAKI_ANALYTICAL_METHOD.md"
governing_policy: "../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md"
reasoning_policy: "../../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md"
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
execution_surface: CODEX_DESKTOP
execution_model: gpt-6-astra
execution_reasoning: max
cross_surface_equivalence_claimed: false
historical_initialization_result: ARCHITECTURE_GATE_VIOLATED_BEFORE_V01
architecture_contract_result: SATISFIED_AT_V1_0_DESIGN_LEVEL
sequential_corpus_result: SATISFIED_PRESERVE
longitudinal_result: PARTIALLY_SATISFIED_FOUR_BACKFILLS_AUTHORED_VOICE_AND_RECONCILIATION_REQUIRED
character_layer_result: TOO_THIN_TO_CARRY_DECLARED_MATURE_ROLES
character_state_backfill_result: MISSING_AT_BASELINE_AUTHORED_AND_INDEX_VALIDATED_POST_CUTOFF_RECONCILIATION_REQUIRED
relationship_layer_result: MISSING_AT_BASELINE_AUTHORED_AND_INDEX_VALIDATED_POST_CUTOFF_RECONCILIATION_REQUIRED
claim_evidence_backfill_result: MISSING_AT_BASELINE_AUTHORED_AND_INDEX_VALIDATED_POST_CUTOFF_SOURCE_ESCALATION_REQUIRED
social_systems_backfill_result: MISSING_AT_BASELINE_AUTHORED_AND_INDEX_VALIDATED_POST_CUTOFF_RECONCILIATION_REQUIRED
specialist_layer_result: MISSING
full_series_synthesis_result: ACTIVE_PROVISIONAL_PRE_REMEDIATION_CANDIDATE
full_series_synthesis_gate: CLOSED
audit_outcome: REMEDIATION_REQUIRED
authoring_checks: PASS_YAML_LINK_ID_AND_INDEX_VALIDATION
repository_preflight: PASS_PHASE_CURRENT_SNAPSHOT_INDEX_PATHS_3286
---

# Bottom-Tier Character Tomozaki — architecture and synthesis role-gap audit

## 1. Governing decision

The Tomozaki literary corpus has completed its admitted V01–V11 sequential reading, including separately routed V06.5 and V08.5 material. It has not completed longitudinal reconciliation, specialist synthesis, cross-specialist convergence, mature full-series synthesis, or release validation.

The new synthesis architecture is substantively adequate. At the design level, it answers every responsibility in sections 5.1–5.16 and section 6 of the repository Minimum Semantic Contract. That pass does not retroactively cure the historical initiation violation and does not make the downstream corpus complete. It instead supplies the missing authority needed to remediate the corpus without rewriting the preserved source-facing readings.

The current disposition is therefore:

| Layer | Decision | Gate effect |
|---|---|---|
| Method and source lock | SATISFIED | no remediation reread required |
| Sequential V01–V11 plus V06.5/V08.5 analysis | SATISFIED; PRESERVE | sequential-source gate remains passed |
| Governing synthesis architecture | SATISFIED AT DESIGN LEVEL | architecture may govern remediation once reconciled into the release state |
| Longitudinal infrastructure | PARTIALLY SATISFIED | longitudinal-reconciliation gate remains open |
| Character monographs | TOO THIN for their intended mature roles | character/specialist gate remains closed |
| Relationship synthesis | MISSING at the audited baseline | specialist gate remains closed |
| Thematic specialist synthesis | MISSING | specialist gate remains closed |
| Existing full-series synthesis | useful ACTIVE_PROVISIONAL candidate, not mature authority | full-series gate remains closed |
| Former validation audit | preserved historical checkpoint; architecture-closure conclusion superseded | cannot open any current gate |
| Current role-gap audit | canonical architecture-readiness authority | defines the remediation sequence |

This result is a correction of role and maturity, not a rejection of the sequential analysis. The readings contain enough recurring evidence to justify and substantially backfill several cumulative layers. Their prospective state, claims, mistakes, questions, falsifiers, and abstentions are evidence and must not be rewritten into hindsight.

## 2. Audit method and classification vocabulary

### 2.1 Materials inspected

The audit inspected:

- the repository policy at governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md;
- the current entrypoint at series/tomozaki/CURRENT_STATE_AND_CORPUS_MAP.md;
- the analytical method and the new synthesis architecture under series/tomozaki/00 Frameworks and Methods/;
- the source lock and inventory;
- the sequential-reading README and every V01–V11 deep reading;
- both supplemental readings, V06.5 and V08.5;
- the effort/competition/goal-ownership ledger;
- the longitudinal-ledger README and first-remediation worktree state;
- all seven character-study candidates and their README;
- the current full-series synthesis candidate;
- the former V11 synthesis validation audit;
- relevant Git history, branch refs, staged state, unstaged tracked state, and untracked state.

The audit distinguishes two questions that must not be collapsed:

1. Does TOMOZAKI_SYNTHESIS_ARCHITECTURE.md itself satisfy the architecture contract?
2. Has the live corpus already executed every responsibility that architecture assigns?

The answer to the first is yes. The answer to the second is no.

### 2.2 Classification terms

| Classification | Meaning in this audit |
|---|---|
| SATISFIED | The responsibility has a correctly routed, sufficiently mature current owner for the audited boundary. |
| PARTIALLY SATISFIED | Material evidence or structure exists, but coverage, reconciliation, authority, or release state is incomplete. |
| MISSING | The required responsibility has no accepted canonical implementation at the audit cutoff. |
| MISROUTED | Material exists, but its current location, authority claim, dependency position, or gate claim is wrong. |
| TOO THIN | A declared artifact exists, but it cannot yet carry the breadth, depth, adversarial testing, or retrieval duty of its intended role. |
| NOT APPLICABLE | The source boundary does not justify a dedicated responsibility, and the architecture explicitly routes or defers it rather than forgetting it. |

An in-progress file is not promoted to SATISFIED merely because a path exists. It must first pass schema, boundary, contradiction, evidence-route, and current-state reconciliation checks.

### 2.3 Evidence-anchor convention

Line anchors in this audit refer to the working-tree versions inspected at the cutoff. Mutable artifacts can move; the named section remains the durable retrieval route. Commit-qualified historical anchors are immutable.

## 3. Exact repository and worktree checkpoint

### 3.1 Refs and divergence

The Git checkpoint re-read at 2026-09-13T04:37:30Z was:

| Field | Exact value |
|---|---|
| branch | series/tomozaki |
| HEAD | 4c6509cd2fbc86e41f9e0f47815ea019e413bc32 |
| origin/series/tomozaki | 4c6509cd2fbc86e41f9e0f47815ea019e413bc32 |
| origin/main | 6c663553bc6bc1d016ef08ea0ac557050a3f64f4 |
| HEAD relative to origin/main | 9 commits ahead, 39 commits behind |

HEAD and origin/series/tomozaki were identical. This fact does not mean the analytical tranche was published: most of the V03–V11 and synthesis corpus existed only in the index or worktree.

### 3.2 Index

The staged snapshot contained 26 changed paths, 11,075 insertions, and 106 deletions:

- one staged method edit;
- one staged sequential-reading README edit;
- eleven staged sequential additions from V03 through V11, including V06.5 and V08.5;
- a staged longitudinal README edit;
- a large staged effort-ledger update;
- seven staged character-monograph additions;
- one staged character README edit;
- one staged full-series synthesis addition;
- one staged former validation-audit addition;
- one staged current-map edit.

V01 and V02 were already tracked before this index tranche. The new synthesis architecture was not in the index at the cutoff.

### 3.3 Unstaged tracked state

The worktree also contained 11 unstaged tracked modifications, totaling 153 insertions and 61 deletions:

1. series/tomozaki/03 Longitudinal Ledgers/README.md;
2. all seven character monograph paths;
3. series/tomozaki/04 Character Analysis/README.md;
4. series/tomozaki/05 Full-Series Synthesis/TOMOZAKI_FULL_SERIES_SYNTHESIS.md;
5. series/tomozaki/CURRENT_STATE_AND_CORPUS_MAP.md.

The resulting status classes included MM for the longitudinal README, character README, and current map, and AM for the seven monographs and full-series synthesis. This matters: the staged validation result recorded by the former audit applies to its earlier index snapshot, not automatically to these later unstaged revisions.

### 3.4 Untracked state

The audit cutoff showed:

- an untracked .scratch/ subtree containing extraction, image-contact-sheet, EPUB-work, plain-text, and validation-support material;
- untracked series/tomozaki/00 Frameworks and Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md;
- untracked series/tomozaki/03 Longitudinal Ledgers/TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md, still being authored at the cutoff;
- no role-gap audit file before this artifact was created.

The .scratch/ subtree was not modified or enrolled by the baseline audit. During post-cutoff validation, an ignored `.scratch/validation-python-deps/` environment was added from the repository's exact hash-locked validation requirements because the bundled runtime did not contain `jsonschema`. It was not staged. Scratch material is neither current literary authority nor a substitute for source-lock and locator routing.

### 3.5 Concurrency boundary

This is an immutable role-gap checkpoint taken during an authorized remediation operation. The current map had already been amended in the worktree to anticipate the architecture, the role-gap audit, and two first-backfill ledgers. At the cutoff, those anticipated routes did not all have accepted completed artifacts. This audit therefore reports both the pre-remediation gap and the observed in-progress correction. Later files do not falsify the baseline finding; they satisfy work ordered by it.

At a post-cutoff recheck at 2026-09-13T04:49:39Z, both first-backfill files had completed their authoring passes:

- TOMOZAKI_CHARACTER_STATE_LEDGER.md: canonical mutable ledger, 706 lines, approximately 12,046 words, SHA-256 1372424E6B18849B1A952CCA915A67C08447201324DDB40730E3A32CA958353D after governing-architecture metadata normalization; YAML, 18 local artifact links, 30 unique claim IDs, required character enrollment, source-boundary exclusions, and supplement chronology passed file-local checks;
- TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md: canonical mutable ledger, 865 content lines, 15,258 words, SHA-256 EA6EAA03A09C66480A8584B08CC2052FA09ED979C2EAD9E038ED9D5621B92803; YAML, 13 reading basenames, 98 cited reading-section anchors, Markdown tables, whitespace, placeholder, and publication-hazard checks passed file-local validation.

Both remained untracked. Their completion remediates the baseline absence of dedicated character-state and relationship-state homes at the file-authoring level. It does not by itself pass longitudinal reconciliation: the two ledgers must be checked against each other, the effort ledger, the map, the eventual claim index, and the intended index or commit snapshot.

## 4. Historical architecture-gate violation

### 4.1 Policy preceded project initiation

The governing initiation policy entered the repository in commit:

- 9957068cc942bdfbfb4f3fbd39c0c6aca13ed2ea;
- timestamp 2026-09-01T17:40:00+00:00;
- the path governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md was added in that commit.

The Tomozaki bootstrap followed in:

- 9d70733c5a12e40217dd72c5875aaec66627784f;
- timestamp 2026-09-04T21:43:13-04:00;
- subject “Initialize Tomozaki analytical architecture.”

The first substantive reading followed in:

- c286a94890bdd8cd5c820b3276da0d138b038616;
- timestamp 2026-09-04T22:03:31-04:00;
- subject “Add Tomozaki Volume 1 deep reading.”

Tomozaki was therefore initiated after the policy existed. It is not an older mature corpus protected from the initialization requirement by grandfathering.

### 4.2 What the policy required

The current policy records the paired-foundation rule before substantive reading at lines 23–24 and identifies day-one longitudinal initialization at lines 177–193. Its Minimum Semantic Contract begins at lines 261–264. Its required transition after sequential completion is explicit at lines 631–641:

sequential completion → completion audit → architecture/role-gap audit → evidence/claim stabilization → specialist synthesis → cross-specialist convergence → full-series synthesis → validation/release audit.

The grandfathering section at lines 645–666 protects existing mature work, but specifically says a project with a method and no synthesis architecture should create the missing architecture before synthesis. That rule cannot make a post-policy project retrospectively compliant at initiation.

### 4.3 What the bootstrap actually contained

At commit 9d70733:

- CURRENT_STATE_AND_CORPUS_MAP.md:13–20 defined the entrypoint questions;
- lines 67–126 enumerated folder purposes, not a synthesis architecture;
- lines 94–101 named the future ledger home and stated that no substantive ledger existed;
- lines 103–110 named character analysis and stated that no monograph existed;
- lines 112–126 listed audit and repository paths while directories 05, 06, 07, and 90 were absent;
- lines 155–162 deferred longitudinal promotion, monographs, specialists, and whole-series synthesis until later.

That scaffold was useful, but it did not define cumulative owners, character/relationship promotion criteria, specialist domains, evidence routes, claim revision, contradiction classes, dependency order, completion gates, reasoning classes, mutable/frozen behavior, or a responsibility matrix. Deferring the decisions was the exact architecture debt the policy was written to prevent.

### 4.4 Historical finding

The historical initialization classification is ARCHITECTURE_GATE_VIOLATED_BEFORE_V01.

The corrective action is not to rewrite V01 or pretend the gate passed. The corrective action is:

- preserve the completed prospective corpus;
- install a truthful evolving architecture;
- audit the role gaps created by the missing architecture;
- backfill only justified cumulative responsibilities;
- reopen primary sources only where the preserved readings cannot support a required evidence level;
- re-run synthesis in the correct dependency order.

## 5. Minimum Semantic Contract audit of the new architecture

### 5.1 Overall design-level result

TOMOZAKI_SYNTHESIS_ARCHITECTURE.md passes the full section 5 contract at version 1.0. The architecture is appropriately EVOLVING rather than falsely STABILIZED, because its mandatory cumulative and specialist layers are not yet implemented and may reveal amendments.

| Contract responsibility | Design result | Architecture evidence | Audit reasoning |
|---|---|---|---|
| 5.1 Purpose, scope, and authority | SATISFIED | frontmatter lines 1–25; §§1.0–1.3 at 30–67 | Names source boundary, V2 remediation generation, authority ladder, governing policy/method/source lock, historical debt, and preservation. It correctly states that no earlier synthesis architecture is superseded. |
| 5.2 Source model | SATISFIED | §§2.1–2.3 at 69–115 | Routes V01–V11, V06.5, V08.5, alternate-edition and paratext layers, exclusions, future sources, and conflict classes. It does not admit adaptations or translations by implication. |
| 5.3 Sequential-reading contract | SATISFIED | §§4.1–4.2 at 134–164 | Defines preserved outputs and the prospective output contract for a future source unit, including claims, locators, ledger updates, readiness, source-lock changes, and map update. |
| 5.4 Longitudinal infrastructure | SATISFIED | §§6.1–6.3 at 187–226 | Names five mandatory cumulative homes, retains the narrow effort ledger, distinguishes distributed/local responsibilities, and defines ledger standards. |
| 5.5 Character and relationship responsibility | SATISFIED | §§7–8 at 228–307 | Establishes promotion tests, four mandatory mature monographs, three reassessment cases, supporting-character routing, three mandatory dyadic syntheses, further tests, and a mature semantic contract. |
| 5.6 Specialist synthesis | SATISFIED | §§9.1–9.3 at 309–336 | Names seven mandatory literary specialist domains, four anticipated domains, a promotion condition, and the specialist home. |
| 5.7 Evidence and locator routing | SATISFIED | §§10.1–10.3 at 338–367 | Defines forward and backward retrieval chains, L1–L4 levels, escalation triggers, the claim-index owner, and Japanese wording/voice routing. |
| 5.8 Claim revision and supersession | SATISFIED | §§11.1–11.3 at 369–392 | Uses PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN, requires changed-evidence and downstream-impact records, retains historical claims, and separates claim revision from artifact supersession. |
| 5.9 Temporal, developmental, epistemic, continuity state | SATISFIED | §5 at 166–185; §§2.1–2.3 | Defines a state tuple that separates source boundary, continuity, time, knowledge holder, evidence mode, confidence, and current disposition. |
| 5.10 Cross-source and contradiction handling | SATISFIED | §2.3 at 100–115 | Distinguishes developmental change, knowledge change, unreliable or bounded viewpoint, deception, retrospection, wording/translation variance, continuity divergence, paratext conflict, and unresolved inconsistency. |
| 5.11 Dependency graph and integration order | SATISFIED | §§12.1–12.2 at 394–441 | Requires architecture/audit before backfill, claim/evidence stabilization before mature specialists, convergence before full synthesis, validation after it, and reconstruction models only later. |
| 5.12 Extension and amendment | SATISFIED | §17 at 519–539 | Provides recurrence, independent accumulation, downstream effect, representation, retrieval, and source-reopen tests; records material changes in architecture history and map. |
| 5.13 Completion gates | SATISFIED | §13 at 443–458 | Separates source, longitudinal, character, specialist, convergence, full-series, validation, and release states and gives honest current results. |
| 5.14 Reasoning classes | SATISFIED | §14 at 460–478 | Assigns stable workload classes, escalation conditions, PREMIUM_QUALITY_FIRST for high-propagation work, and records owner-directed Max execution without claiming product-surface equivalence. |
| 5.15 Mutable, frozen, superseded behavior | SATISFIED | §15 at 480–500 | Protects prospective readings and frozen audits, allows current maps/ledgers/architectures to evolve, and requires scoped supersession with retained history. |
| 5.16 Entrypoint and retrieval route | SATISFIED | §19 at 566–577 | Names CURRENT_STATE_AND_CORPUS_MAP.md as first read, gives a complete route, and requires the map to expose source boundary, lifecycle, maturity, gate, and next action. |

### 5.2 Required responsibility-matrix result

The architecture also satisfies policy section 6. Its matrix at lines 541–564 maps sequential capture, cumulative owner, final destination, and initialization state across character state, relationship state, claims, evidence, social systems, technique/authenticity, causality/meaning, intimacy/consent, authorship, Japanese terms/register, ordinary life, professional pathways, and visual/paratext evidence.

The matrix is proportional to this literary source. It does not import anime-only audio obligations, game-route bookkeeping, or a visual ledger without evidence of independent retrieval need.

### 5.3 Design caveats that do not defeat the pass

- Version 1.0 is untracked at the audit cutoff. Content satisfaction is not release reconciliation.
- The architecture names required artifacts that do not yet exist or were still in active authoring.
- Its responsibility matrix reports current gaps truthfully. A matrix may satisfy the mapping contract while reporting MISSING implementation.
- The lifecycle must remain EVOLVING until schemas, promotion decisions, and cross-specialist terminology survive implementation.
- The architecture should be amended if backfill proves a proposed home duplicative or reveals a recurring independent dimension, but that possibility is part of compliance, not evidence of failure.

## 6. Actual corpus implementation against sections 5.1–5.16

This matrix rates the corpus as implemented at the cutoff, not merely the new architecture's prose.

| Responsibility | Corpus classification | Current evidence | Required correction |
|---|---|---|---|
| 5.1 Purpose, scope, authority | PARTIALLY SATISFIED | The worktree map now routes to the architecture and labels remediation at CURRENT_STATE_AND_CORPUS_MAP.md:13–31, while the architecture supplies the missing authority. Both remain unreconciled with the staged/released state. | Review, stage, and validate the authority set together. |
| 5.2 Source model | SATISFIED | Source lock lines 36–70 inventories all 13 EPUB witnesses; lines 74–97 route side/special material; lines 112–150 govern wording, exclusions, and revision. | Preserve; amend only if a new source is admitted. |
| 5.3 Sequential-reading contract | PARTIALLY SATISFIED | Thirteen source-facing readings are strong, but they were completed before required cumulative outputs had canonical owners. | Preserve readings; recover cumulative outputs through backfill. |
| 5.4 Longitudinal infrastructure | PARTIALLY SATISFIED | Effort ledger is mature. Character and relationship backfills were the active first tranche. Claim/evidence, social-systems, and voice/register homes were absent. | Complete and reconcile all five mandatory homes. |
| 5.5 Character and relationship synthesis | TOO THIN | Seven character candidates exist, but none yet meets the full mature-monograph semantic contract; no accepted relationship specialist exists. | Deepen four mandatory monographs; deepen or reclassify three bounded cases; then write earned dyadic/ensemble syntheses. |
| 5.6 Specialist synthesis | MISSING | No series/tomozaki/06 Specialist Synthesis/ implementation exists. | Write the seven mandatory problem-domain specialists after cumulative stabilization. |
| 5.7 Evidence and locator routing | PARTIALLY SATISFIED | Readings contain section, claim, question, image, and source routes; monographs and synthesis mostly point to whole files rather than claim-level evidence; no corpus-wide locator index exists. | Build the claim/revision/evidence index and escalate L2/L3 claims selectively. |
| 5.8 Claim revision and supersession | PARTIALLY SATISFIED | Readings use extensive local claim adjudication; the audit inventory found 319 distinct C-class and 140 Q-class identifiers under its token scan. No canonical corpus-wide current-disposition crosswalk exists. | Build the claim index; keep original IDs and frozen statements discoverable. |
| 5.9 Temporal/developmental/epistemic state | SATISFIED | Prospective freezes, state vectors, explicit reader/actor knowledge bounds, routed supplements, and the new state tuple prevent terminal flattening. | Preserve this discipline in cumulative and specialist work. |
| 5.10 Contradiction handling | PARTIALLY SATISFIED | Individual readings and candidates preserve counterevidence and abstentions; architecture defines conflict classes. Corpus-wide contradictions have not undergone adversarial reconciliation. | Record material conflicts in the claim index and convergence audit. |
| 5.11 Dependency graph/integration order | MISROUTED | A full-series synthesis and validation audit were written before the missing cumulative and specialist layers. New architecture and map now correct the order, but the pre-remediation files remain. | Preserve them as provisional/history; do not deepen final synthesis until convergence. |
| 5.12 Extension/amendment | SATISFIED | Architecture §17 and map work order permit justified backfill without indiscriminate restructuring. | Use formal amendments if implementation changes responsibility. |
| 5.13 Completion gates | PARTIALLY SATISFIED | The architecture and updated map now close the correct gates. The former immutable audit retains its historical closure claim; the provisional synthesis has since retracted its own former no-additional-ledger conclusion. The release authority set is not yet reconciled. | Route scoped audit supersession through this artifact and the map; validate the final authority set. |
| 5.14 Reasoning classes | SATISFIED | Architecture §14 assigns classes and captures current owner-directed Max execution. | Continue PREMIUM_QUALITY_FIRST for high-propagation synthesis and monographs. |
| 5.15 Mutable/frozen behavior | PARTIALLY SATISFIED | New architecture protects historical readings and old audit. V01–V07 and both supplements still declare mutable_active while the README and architecture call them frozen. | Preserve prose; later normalize only metadata through an explicit governed migration if needed. |
| 5.16 Entrypoint/retrieval | PARTIALLY SATISFIED | The worktree map is now a good remediation router at lines 34–45, 75–110, 190–288, and 321–385, but it anticipates files not accepted at cutoff and is unstaged over a different index version. | Reconcile actual file existence, maturity, and gate labels before release validation. |

## 7. Required responsibility matrix: project implementation

| Analytical responsibility | Sequential evidence | Canonical cumulative destination | Audit classification at cutoff | Final destination and decision |
|---|---|---|---|---|
| Character developmental state | Strong across V01–V11; explicit state sections recur | TOMOZAKI_CHARACTER_STATE_LEDGER.md | MISSING at baseline/cutoff; AUTHORED post-cutoff with file-local checks passed; corpus reconciliation pending | Mature monographs, relationship specialists, thematic specialists, final synthesis |
| Directional relationships and network state | Strong; V01 has an explicit relationship-state ledger and later volumes preserve vectors, boundaries, repair, third parties, and consent | TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md | PARTIALLY SATISFIED at cutoff; AUTHORED post-cutoff with file-local checks passed; corpus reconciliation pending | Three mandatory dyadic syntheses plus earned ensemble treatments |
| Effort, competition, rank, goal ownership, stopping rules, viability | Very strong and repeatedly revised | TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md | SATISFIED through V11 | Effort specialist and final synthesis |
| Major claims and revision history | Strong local registers; hundreds of claim/question IDs | TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md | PARTIALLY SATISFIED locally; MISSING cumulatively | Every mature synthesis and later release audit |
| Evidence locators | Substantial L1 routes; uneven exact locators | Claim/revision/evidence index plus source readings | PARTIALLY SATISFIED | Deterministic backward traceability; targeted L2/L3 for load-bearing claims |
| Social atmosphere, reputation, sanctions, facilitation, repair | Recurs from early group entry through the V05 class conflict and later intervention network | TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md | MISSING as cumulative owner | Social-atmosphere/group-systems specialist |
| Institutional state | School, class, student council, work, publishing, game competition, and professional pathways recur but vary in centrality | Social-systems ledger plus effort ledger; anticipated professional-pathway specialist if promoted | PARTIALLY SATISFIED in distributed evidence | Social specialist; professional specialist only if amendment test passes |
| Japanese key terms | Intermittently retained in readings and synthesis | TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md | PARTIALLY SATISFIED locally; MISSING cumulatively | Language specialist and all wording-sensitive mature claims |
| Character-specific voice, address, and register | Too uneven in the English analytical summaries | Same voice/register ledger | MISSING for mature cross-character use | Monographs, relationship specialists, language specialist, optional later reconstruction |
| Ordinary-life habits and preferences | Locally present and interpretively useful | Character and relationship ledgers; monographs | PARTIALLY SATISFIED; dedicated ledger NOT APPLICABLE now | Keep distributed unless retrieval burden later meets amendment threshold |
| Romance, care, privacy, disclosure, boundaries, consent, intervention | Strong recurring relationship evidence | Relationship ledger plus claim index | MISSING as reconciled cumulative state | Three dyadic specialists and ethics/intervention specialist |
| Fiction, observation, authorship, publication, personhood | Strong especially around Kikuchi and V11 | Character ledger plus claim index | PARTIALLY SATISFIED locally | Kikuchi monograph and authorship specialist |
| Technique, learned form, authenticity, self-authorship | Strong from V01 onward | Character/relationship ledgers and claim index | PARTIALLY SATISFIED, distributed | Mandatory game/form/self-authorship specialist |
| Control, causality, result, reason, retrospective meaning | Strong and high-risk at V08.5–V11 | Claim index plus character/relationship ledgers | PARTIALLY SATISFIED, distributed | Mandatory causality/meaning specialist |
| Visual/paratext evidence | Diagnostically inspected and segregated in source readings | Source lock and local reading sections | SATISFIED as local/distributed | Dedicated visual ledger NOT APPLICABLE absent new recurrence |
| Music/audio/performance | Not part of the admitted light-novel-only boundary | None | NOT APPLICABLE | Reassess only if an adaptation corpus is admitted |
| Route/branch state | Literary corpus is one main continuity with chronology-controlled supplements, not a branching game corpus | Source model and local supplement routing | NOT APPLICABLE as separate ledger | Reassess only if a branched source is admitted |
| World mechanics | No independent speculative-world system requires its own ledger | Distributed social/institutional routing | NOT APPLICABLE as separate ledger | Social and institutional owners suffice |
| Character reconstruction readiness | Literary authority has not converged | Future series/tomozaki/07 Character Reconstruction Models/ | DEFERRED; currently NOT APPLICABLE | Optional derived layer after literary release validation |

## 8. Artifact-by-artifact maturity audit

### 8.1 Entrypoint, method, architecture, and source lock

| Artifact | Classification | Evidence and disposition |
|---|---|---|
| CURRENT_STATE_AND_CORPUS_MAP.md | PARTIALLY SATISFIED RELEASE STATE; SATISFIED ROUTING DESIGN | The current worktree correctly labels historical violation, active remediation, EVOLVING architecture, open longitudinal gate, closed specialist and full-series gates at lines 13–31. Lines 75–110 distinguish source completion from synthesis incompletion; lines 225–288 map current and future homes; lines 321–385 give the correct work order and no-reread rule. It is unstaged over a staged predecessor and anticipates in-progress files, so release reconciliation remains open. |
| TOMOZAKI_ANALYTICAL_METHOD.md | SATISFIED | Prospective freezing at 45–60, focalization at 62–75, state-before-trait at 96–109, directional relationships at 158–176, peer ecology at 178–196, ordinary life at 198–204, Japanese wording/register at 206–221, revision vocabulary at 237–248, minimum volume outputs at 250–268, and promotion thresholds at 270–281 remain fit for the source. |
| TOMOZAKI_SYNTHESIS_ARCHITECTURE.md | SATISFIED AT DESIGN LEVEL | It passes all contract responsibilities in §5 above, truthfully records debt, preserves readings, and closes the correct gates. It remained untracked at the cutoff and must stay EVOLVING. |
| TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md | SATISFIED | Lines 36–70 establish witness identity and integrity; lines 74–97 route special/side material; lines 112–123 govern witness and wording claims; lines 125–150 govern exclusions and future change. No source-model remediation requires reopening the EPUBs. |

### 8.2 Sequential-reading README and corpus

The sequential corpus comprises thirteen reading artifacts and approximately 102,000 words. Their breadth, explicit uncertainty, and cumulative signals are sufficient to preserve the source-facing pass. They are not substitutes for cumulative synthesis.

| Artifact | Approximate words | Maturity | Evidence and caveat |
|---|---:|---|---|
| 02 Sequential Readings/README.md | 879 | PARTIALLY SATISFIED | Correctly describes the readings as closed/frozen and governs continuity. Some artifact frontmatter does not match that freeze claim. |
| TOMOZAKI_V01_DEEP_READING.md | 6,845 | SATISFIED CONTENT; METADATA PARTIAL | Establishes baseline character state near line 524 and an explicit relationship-state ledger near line 432. release_state remains mutable_active despite retrospective freeze. |
| TOMOZAKI_V02_DEEP_READING.md | 6,680 | SATISFIED CONTENT; METADATA PARTIAL | Deepens Mimimi/Hinami comparison, institutions, and forecast discipline. release_state remains mutable_active. |
| TOMOZAKI_V03_DEEP_READING.md | 7,639 | SATISFIED CONTENT; METADATA PARTIAL | State-vector material recurs near line 432; goal ownership and relationship choice are explicitly adjudicated. Staged addition; mutable_active. |
| TOMOZAKI_V04_DEEP_READING.md | 7,922 | SATISFIED CONTENT; METADATA PARTIAL | State reconstruction recurs near line 425; group atmosphere and negotiated effort create cumulative responsibilities. Staged addition; mutable_active. |
| TOMOZAKI_V05_DEEP_READING.md | 9,117 | SATISFIED CONTENT; METADATA PARTIAL | State material near line 592 and social-atmosphere retrieval at lines 836–848 explicitly foreshadow a later two-direction atmosphere artifact. Staged addition; mutable_active. |
| TOMOZAKI_V06_DEEP_READING.md | 8,364 | SATISFIED CONTENT; METADATA PARTIAL | Character state near line 417, relationship vectors near line 405, and ledger-promotion reasoning at lines 680–692 demonstrate independent dyadic retrieval need. Staged addition; mutable_active. |
| TOMOZAKI_V06_5_SUPPLEMENTAL_READING.md | 4,904 | SATISFIED CONTENT; METADATA PARTIAL | Correctly keeps retrospective and post-V06 units story-local. Staged addition; mutable_active. |
| TOMOZAKI_V07_DEEP_READING.md | 9,695 | SATISFIED CONTENT; METADATA PARTIAL | Character state near line 422 and relationship vectors near line 409; Special Edition paratext remains segregated. Staged addition; mutable_active. |
| TOMOZAKI_V08_DEEP_READING.md | 7,364 | SATISFIED | Character state near line 307 and explicit relationship maintenance. Its earlier decision at lines 545–558 to route relationship maintenance into the effort ledger is now superseded at the architecture level, not rewritten in the reading. release_state frozen. |
| TOMOZAKI_V08_5_SUPPLEMENTAL_READING.md | 5,656 | SATISFIED CONTENT; METADATA PARTIAL | Mixed chronology and adapted/parallel material remain segregated; no actor-knowledge laundering. Staged addition; mutable_active. |
| TOMOZAKI_V09_DEEP_READING.md | 8,703 | SATISFIED | Character state near line 325 and strong relationship repair evidence. Its lines 613–626 decline a relationship ledger at that boundary; recurring later evidence now justifies architectural promotion without changing the frozen decision. |
| TOMOZAKI_V10_DEEP_READING.md | 8,407 | SATISFIED | Character state near line 278, bounded Nagisa causality, and explicit consent/knowledge limits. Lines 527–540 similarly preserve the then-current no-ledger decision. |
| TOMOZAKI_V11_DEEP_READING.md | 11,078 | SATISFIED | Character state near line 381; forty current-boundary claims, twelve controlling questions, family-formation evidence, crisis, game result, and proposed intervention remain explicitly bounded. release_state immutable_freeze. |

The release-state mismatch is real but lower priority than semantic backfill. The correct immediate action is not to edit thirteen historical readings. If metadata normalization is later desired, it should be a narrow governed migration that changes no substantive prose and records why the earlier mutable labels no longer govern.

### 8.3 Longitudinal artifacts

| Artifact | Classification | Evidence and disposition |
|---|---|---|
| TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md | SATISFIED | Approximately 22,000 words and current through V11. Lines 15–33 define a precise responsibility; line 31 explicitly refuses general character-state, relationship, moral-score, psychiatric, or every-training-scene ownership. It is a mature narrow spine and must not be diluted into a generic summary. |
| TOMOZAKI_CHARACTER_STATE_LEDGER.md | MISSING AT CUTOFF; AUTHORED POST-CUTOFF; RECONCILIATION PENDING | The completed 702-line file provides chronology/evidence-plane control, three clocks, epistemic classes, state dimensions, revision rules, developmental bands, seven principal and bounded supporting-character states, a 30-claim register, open questions/abstentions, and downstream handoffs. File-local checks pass; it remains untracked and must undergo cross-ledger/corpus reconciliation. |
| TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md | IN PROGRESS AT CUTOFF; AUTHORED POST-CUTOFF; RECONCILIATION PENDING | The completed 865-line file covers mainline and story-local chronology, directional central and secondary dyads, network state, authority/consent, revisions, explicit negatives, source-section routes, and specialist promotions. File-local checks pass; it remains untracked and requires cross-ledger/corpus reconciliation. |
| TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md | MISSING | Required to crosswalk reusable/disputed local claim IDs, current dispositions, affected downstream artifacts, and locator levels without renumbering historical registers. |
| TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md | MISSING | Repeated atmosphere, reputation, punishment, facilitation, sanctions, re-entry, and repair create independent retrieval responsibility. |
| TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md | MISSING | Required for character-specific voice, address, proposition ownership, and load-bearing terms. This is the one cumulative layer that cannot mature from English analytical summaries alone. |

### 8.4 Character-analysis README

The working-tree README correctly reclassifies the seven files as active_provisional candidates and points mature responsibility back to the architecture. That is a sound authority correction. It is still MM against the index and must be reconciled with final file frontmatter and the current map before release.

### 8.5 Character monographs

Length is not the governing test. The word and section counts below are diagnostics of compression; the classification rests on missing semantic responsibilities.

| Candidate | Approximate words | Classification | Concrete maturity gap |
|---|---:|---|---|
| Tomozaki Fumiya | 2,950 | TOO THIN — SEVERE PRIORITY | A useful thesis, one-row-per-volume chronology, state vector, relationship sketches, rival readings, and endpoint exist. The evidence route at lines 237–243 points broadly to whole reading sets and the old synthesis rather than claim-level current evidence. Stress/repair, attentional and decision habits, recipient-conditioned changes, Japanese voice, contradiction dispositions, and dyadic handoffs need much greater resolution. |
| Hinami Aoi | 2,789 | TOO THIN — SEVERE PRIORITY | Strong caution around focalization, family causality, NO NAME, and diagnosis, but the central competing-method burden exceeds the current compression. The evidence route begins near line 226 and remains broad. Voice/register, chronological bands, relationship-conditioned state, knowledge/standing, causal alternatives, and falsifiable rival models need deep adjudication. |
| Kikuchi Fuka | 2,449 | TOO THIN — HIGH PRIORITY | Correctly distinguishes observation from authority and fiction from testimony, but chronology, publication risk, self-inclusion, relationship governance, jealousy/allocation/privacy, Japanese literary voice, and claim locators remain compressed. Evidence routing begins near line 221. |
| Nanami Minami / Mimimi | 2,223 | TOO THIN — HIGH PRIORITY | Correctly centers comparative self-worth, performed energy, relational firstness, love, and non-entitlement. It needs deeper ordinary-life/process evidence, recipient-conditioned voice, stopping-rule chronology, institutional labor, counterreadings, and locator routing. Evidence routing begins near line 198. |
| Natsubayashi Hanabi / Tama | 1,917 | TOO THIN FOR MATURE MONOGRAPH; DOSSIER DECISION OPEN | The V05 learning case and stable-principle argument are useful. Later-volume evidence is sparse, voice is not reconstructed, and the file may not sustain independent full-monograph maintenance across all mature-contract dimensions. Evidence routing begins near line 189. Deepen if evidence breadth warrants; otherwise reclassify honestly as a bounded dossier. |
| Mizusawa Takahiro | 2,017 | TOO THIN FOR MATURE MONOGRAPH; DOSSIER DECISION OPEN | The fluency-without-destination and hero-fantasy risks are sound. His pursuit chronology, self-model, professional experiments, stress/failure, voice, and relationship-specific authority need more evidence than the current broad route near line 179 supplies. Deepen or bound. |
| Izumi Yuzu | 1,980 | TOO THIN FOR MATURE MONOGRAPH; DOSSIER DECISION OPEN | Maintenance as competence and owned accommodation are important. The file needs more direct evidence of cost, absorber limits, desire, stopping rules, private state, ordinary-life patterns, and register. Broad evidence routing begins near line 189. Deepen or bound. |

All seven should be preserved. None should be deleted, silently retitled as mature, or treated as failed work. Their current best role is retrieval aid, hypothesis inventory, and structured seed for post-ledger monograph work.

Supporting characters should not receive automatic monographs. Current routing should be:

- Haruka, Nagisa, and Yoko into Hinami's formation analysis, the causality/meaning specialist, and appropriate state/relationship ledgers;
- Erika, Konno, Akiyama, and class actors into social atmosphere, punishment, repair, and accountability analysis;
- Nakamura into peer-network, Yuzu, Mimimi, and relationship-state analysis;
- Rena into consent, boundary, touch, standing, and intervention analysis;
- Jack, Endo, professional players, school and publishing actors into effort/institutional routes.

After those responsibilities converge, evidence may justify a bounded dossier or ensemble section. Proximity to the protagonist is not sufficient.

### 8.6 Full-series synthesis candidate

TOMOZAKI_FULL_SERIES_SYNTHESIS.md is approximately 7,594 words and contains a useful integrated thesis, developmental outline, major-character sketches, central dyadic arguments, theme sections, a relationship matrix, current claims, rival readings, and endpoint abstentions. It is valuable.

It is nevertheless TOO THIN and historically MISROUTED as mature full-series synthesis because:

- it was drafted before the mandatory cumulative and specialist responsibilities existed;
- its evidence routing relies chiefly on broad reading and ledger links, not a deterministic claim-to-source crosswalk;
- major character, relationship, atmosphere, form, causality, ethics, authorship, and language responsibilities are compressed into sections that should receive independent adversarial treatment;
- it cannot test convergence among specialists that did not yet exist;
- it uses the narrow effort ledger beyond the point at which relationship and general character state require separate owners;
- its substantive integrated arguments were composed before the five cumulative homes and specialist program existed, so they cannot demonstrate convergence retroactively;
- its frontmatter, authority notice, and revised §20 at lines 559–571 now correctly call it active_provisional, retract the former no-additional-ledger conclusion, and keep the final-synthesis gate closed.

Disposition:

1. preserve the file as the V11 pre-remediation integration candidate;
2. use it as a hypothesis and cross-domain gap inventory;
3. do not patch it piecemeal while prerequisites are moving;
4. write or substantially revise the mature full-series synthesis only after cumulative stabilization, monographs, relationship specialists, thematic specialists, and convergence audit;
5. make the eventual successor explicitly supersede this candidate's whole-series-authority role while preserving its historical reasoning.

### 8.7 Former validation audit

TOMOZAKI_FULL_SERIES_SYNTHESIS_VALIDATION_AUDIT.md is an immutable V1.0 checkpoint. It remains reliable evidence that its then-indexed tranche passed the checks it actually ran:

- source and sequential coverage;
- bounded epistemic claims;
- its then-current repository checks, including git diff --cached --check and author preflight;
- no commit/push/merge action by that operation.

Its architecture and maturity conclusions do not govern V2 remediation:

- lines 42–55 marked seven monographs and the whole synthesis PASS and rejected a second ledger;
- lines 63–76 marked broad-domain traceability PASS without the claim/evidence route now required;
- lines 112–118 concluded architecture gaps were closed and no additional current-boundary document was required.

Those conclusions are superseded by this audit for architecture readiness, role coverage, and synthesis completion only. The old file's substantive findings remain unchanged. Because it was a staged, unpublished addition, its authority metadata and a narrow notice were corrected before publication to provide the reciprocal successor edge required by repository validation. It should be read as evidence of what the pre-remediation tranche checked, not as a current instruction to skip remediation.

## 9. Cumulative layers justified by recurring V01–V11 evidence

### 9.1 Character-state ledger — mandatory

The corpus repeatedly separates competence, confidence, status, self-concept, agency, values, role, stress state, recipient, and focalization. State sections recur in V01 near line 524, V03 near 432, V04 near 425, V05 near 592, V06 near 417, V07 near 422, V08 near 307, V09 near 325, V10 near 278, and V11 near 381.

This is not a ledger copied from another series. It solves a real retrieval problem:

- Tomozaki's skills and social embedding persist through V11 crisis even as a governing identity claim collapses;
- Hinami's public role, NO NAME play, family state, coaching relation, and withdrawal cannot be collapsed into one trait;
- Mimimi's ambition, romantic restraint, routine loss, and public availability move on different clocks;
- Kikuchi's selective habitat, authorship, relationship standing, and collaboration must be time-indexed;
- supporting characters change in role, knowledge, and option structure even when their core tendency is stable.

Backfill can begin at L1 from preserved readings. No full EPUB reread is required.

### 9.2 Relationship-state ledger — mandatory

Relationships accumulate facts neither participant owns alone:

- A→B and B→A desired relation;
- standing and knowledge;
- disclosure and privacy;
- trust, leverage, care, and dependency;
- boundaries, refusal, consent, and authority;
- ordinary presence and routine;
- conflict and repair;
- third-party effects;
- changes to each person's available options.

V01 already contains an explicit relationship-state ledger near line 432. V06 and V07 preserve relationship vectors near lines 405 and 409. V06:680–692 notes that a relationship ledger becomes justified if retrieval grows difficult. V08–V10 locally declined promotion or routed maintenance elsewhere, but V11 supplies enough additional disclosure, consent, intervention, crisis, and third-party evidence to cross the recurrence and independent-retrieval threshold.

The earlier no-ledger decisions remain historically valid at their boundaries. The new architecture does not rewrite them; it makes a later promotion decision under more evidence.

### 9.3 Claim-revision and evidence index — mandatory

Local claim registers are a strength. Their volume-local structure becomes a corpus-wide weakness when a mature synthesis must answer:

- which earlier claims remain current;
- which were revised, downgraded, rejected, or left open;
- where the decisive later evidence entered;
- what source locator level supports the current formulation;
- which character, relationship, or specialist artifacts inherit the claim;
- whether a claim depends on wording, attribution, sequence, or contested causality.

The index should not copy all prose or renumber all local IDs. It should select material reusable, disputed, high-propagation, or wording-sensitive claims and point backward deterministically.

### 9.4 Social-atmosphere and group-systems ledger — mandatory

The recurring evidence is not merely “theme.” It has independently changing state:

- what a class or peer group rewards, fears, sanctions, or treats as speakable;
- how reputation constrains possible action;
- how visible status and private alignment differ;
- how punishment distributes through bystanders;
- how facilitators such as Yuzu and Mimimi absorb maintenance cost;
- how repair and re-entry occur;
- how student-council, school-event, work, game, and publishing institutions change standing.

V01's group entry, V02's election, V04–V05 class conflict, later relationship crises, V11 absence and collective intervention all require retrieval across character files. V05:836–848 explicitly anticipates a two-direction atmosphere artifact. A cumulative owner is justified.

### 9.5 Japanese voice, register, and key terms — mandatory but source-dependent

The series' major arguments depend on Japanese lexical and pragmatic distinctions around game, rank, result, reason, meaning, strength, effort, character, air/atmosphere, self-authorship, and forms of proposition ownership. Character-specific address, assertion, hedging, humor, directness, role performance, and register shifts matter to Tomozaki, Hinami, Kikuchi, Mimimi, Tama, Mizusawa, and Yuzu.

The current monographs contain virtually no recoverable character-specific Japanese voice evidence, and their generic source links cannot support mature register claims. The new layer should begin with terms already preserved in readings, then reopen only diagnostic passages needed for L2/L3 support. It must not manufacture Japanese from translations or remembered wording.

### 9.6 Responsibilities that should remain distributed

- Ordinary-life evidence stays in character and relationship state, monographs, and relevant specialists unless retrieval later proves a dedicated ledger necessary.
- Professional play, work, schooling, publishing, and adulthood currently route through the effort ledger, social systems, character state, and an anticipated specialist. A separate professional-pathway ledger is not yet justified.
- Visual and paratext evidence remains local to source lock/readings because it is diagnostic and edition-specific, not a recurring independent analytical state.
- Predictions and falsifiers remain in frozen readings; the claim index crosswalks material current dispositions without replacing the prospective record.
- Ethical judgments route through relationship state, claim evidence, and the later intervention specialist rather than a free-floating moral score ledger.
- Audio, performance, adaptation divergence, game branches, and route state are not current literary obligations.

## 10. Primary-source reopening decisions

### 10.1 No broad reread

No full V01–V11 reread is justified for:

- synthesis architecture;
- this role-gap audit;
- core character-state chronology;
- core relationship-state chronology;
- effort/goal-ownership maintenance;
- first-pass social/group-system chronology;
- claim-ID inventory and current-disposition crosswalk;
- promotion decisions based on recurrence;
- preservation or provisional reclassification of existing monographs and synthesis.

The source-facing readings are sufficiently rich for those first-pass backfills. Reopening all EPUB prose would add cost, risk hindsight contamination, and violate proportionality without a demonstrated material gap.

### 10.2 Targeted reopen required

Read-only return to the authorized Japanese EPUBs is required when a load-bearing claim depends on:

- exact Japanese wording or a character's register;
- address form, pronoun, politeness, sentence ending, quotation framing, or proposition ownership;
- translation-sensitive distinctions;
- disputed speaker or focalizer attribution;
- precise causal or temporal order not retained in the reading;
- an exact phrase needed to distinguish rival interpretations;
- a high-propagation claim for which L1 summary is too lossy;
- a contradiction that cannot be classified from existing artifacts.

The owner-designated external Tomozaki novel source directory is read-only evidence. All analytical output remains inside this registered Tomozaki repository workspace, and no source file is copied into Git.

### 10.3 Locator policy

- L1, an exact reading path plus section, table, or local claim ID, is sufficient for ordinary retrospective backfill when the preserved reading contains the evidence.
- L2, a source unit plus structural location, is required when sequence or attribution matters.
- L3, a short diagnostic Japanese phrase or unambiguous marker, is required for wording, register, translation, or disputed interpretive force.
- L4, a bounded visual or paratext asset route, applies only to diagnostic illustration/edition claims.

No invented page numbers, reconstructed quotations, long copyrighted passages, or unsupported Japanese should enter the ledgers.

## 11. Character and relationship dispositions

### 11.1 Mandatory mature monographs

The evidence makes four mature literary monographs mandatory:

1. Tomozaki Fumiya;
2. Hinami Aoi;
3. Kikuchi Fuka;
4. Nanami Minami / Mimimi.

Tomozaki and Hinami are first because errors in their methods, relationship, causality, and current state propagate into nearly every specialist. Kikuchi and Mimimi follow because they are not reducible to “romance options”: they independently carry authorship, observation, selection, allocation, comparison, performed brightness, relational firstness, restraint, and stopping-rule problems.

Each mature rewrite must satisfy the architecture semantic contract at lines 260–283: developmental bands; stable versus state/role/recipient effects; evidence hierarchy; self-theory versus behavior; motive and goal hierarchy; attention and decision habits; competence/confidence/status/self-concept/agency/value distinctions; strength/failure duality; stress/defeat/repair; relationship-conditioned variation; ordinary life; traceable voice/register; rival readings and dispositions; current V11 state; claims/locators; and handoff constraints.

### 11.2 Bounded dossier decisions

Tama, Mizusawa, and Yuzu have earned independent current files. The audit does not find enough implemented depth to certify them as mature full monographs. Later evidence review must choose one of two honest outcomes:

- deepen to the same mature contract because the corpus supports independent multi-domain maintenance; or
- relabel as bounded character dossier with a narrower responsibility, explicit exclusions, and clean handoff to relationship/social/thematic specialists.

Reclassification is not demotion. A precise dossier is stronger than an overclaimed monograph.

### 11.3 Mandatory relationship specialists

Three independent relationship syntheses are mandatory after the relationship ledger and character monographs stabilize:

- Tomozaki ↔ Hinami;
- Tomozaki ↔ Kikuchi;
- Tomozaki ↔ Mimimi.

They must remain directional. Affection, centrality, sacrifice, insight, or dramatic weight cannot establish reciprocity, romantic classification, consent, standing, or authority.

The relationship ledger must also test whether independent or ensemble treatment is earned for:

- Hinami ↔ Tama;
- Hinami ↔ Mizusawa;
- Mimimi ↔ Tama;
- Tomozaki ↔ Mizusawa;
- Tomozaki ↔ Rena;
- the core peer group as a distributed intervention/care system;
- class atmosphere and punishment networks.

## 12. Specialist-synthesis disposition

The completed source boundary justifies seven mandatory problem-domain specialists before final integration:

1. game models, learned form, authenticity, and self-authorship;
2. effort, mastery, rank, goal ownership, and future viability;
3. social atmosphere, group systems, reputation, punishment, and repair;
4. control, causality, result, reason, and retrospective meaning;
5. romance, care, disclosure, boundaries, and intervention ethics;
6. authorship, fiction, observation, and personhood;
7. Japanese conceptual language, voice, and register.

These are not arbitrary imported titles. Each recurs across multiple volumes, accumulates evidence independently, affects other syntheses, and cannot responsibly remain one short section inside the full-series file.

The following remain anticipated, not mandatory:

- professional play, schooling, work, and adulthood as an institutional pathway;
- gendered performance, attraction, and sexual-boundary systems;
- ordinary life, food, games, clothing, and shared activity as relational evidence;
- adaptation divergence if a new corpus is admitted.

Consolidation among mandatory specialists is permitted only if every responsibility remains explicit, independently retrievable, adequately developed, and adversarially tested. The correct home is series/tomozaki/06 Specialist Synthesis/, instantiated when the first specialist is ready.

## 13. Dependency and gate correction

### 13.1 Historical misordering

The pre-remediation execution order was:

sequential completion → narrow effort ledger → seven compressed character candidates → full-series synthesis candidate → validation audit.

That sequence skipped the architecture/role-gap audit, general character and relationship state, corpus-wide claims/locators, social systems, voice/register, relationship specialists, thematic specialists, and cross-specialist convergence. The former validation audit then certified the output under the incomplete role map.

### 13.2 Corrected order

The governing order is:

- source lock + method;
- preserved source-facing readings;
- synthesis architecture + role-gap audit;
- character-state + relationship-state backfill;
- claim/evidence index + social-systems ledger;
- targeted Japanese escalation + voice/register ledger;
- mature character monographs;
- relationship syntheses + thematic specialists;
- adversarial claims/locators audit + cross-specialist convergence;
- mature full-series synthesis;
- literary validation/release audit;
- optional reconstruction models.

### 13.3 Current gate table

| Gate | Current decision | Reopening condition |
|---|---|---|
| Source integrity and inventory | PASS | reopen only for newly admitted or changed witness |
| Sequential-source completion | PASS at V11 plus routed V06.5/V08.5 | new source admitted |
| Architecture contract | PASS at v1.0 design level | material amendment or implementation contradiction |
| Longitudinal reconciliation | OPEN | all mandatory cumulative homes reconciled through V11 with usable routes |
| Character maturity | CLOSED | required monographs pass semantic and adversarial review |
| Relationship/specialist synthesis | CLOSED | mandatory dyadic and thematic responsibilities pass |
| Cross-specialist convergence | CLOSED | shared states, terms, claims, and contradictions agree or record OPEN |
| Full-series synthesis readiness | CLOSED | all preceding literary gates pass |
| Validation/release | OPEN, not runnable as final | final index/worktree/authority set and literary traceability pass |
| Reconstruction models | DEFERRED | mature literary corpus releases first |

V11 source completion is not series-ending closure. A later volume can reopen the source boundary without invalidating this remediation sequence or changing what was known at earlier freezes.

## 14. Remediation work order

### 14.1 First tranche

The first remediation tranche is:

1. establish TOMOZAKI_SYNTHESIS_ARCHITECTURE.md as canonical EVOLVING authority;
2. establish this role-gap audit as current architecture-readiness authority;
3. make CURRENT_STATE_AND_CORPUS_MAP.md and the relevant READMEs route the historical violation, provisional artifacts, open gates, and exact next action;
4. preserve the former immutable audit while marking its architecture-closure conclusion superseded by scope;
5. finish and reconcile TOMOZAKI_CHARACTER_STATE_LEDGER.md;
6. finish and reconcile TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md;
7. validate that both ledgers cover V01–V11 and routed V06.5/V08.5 without changing historical readings;
8. reconcile worktree, index, path existence, frontmatter authority, and map status before calling the tranche complete.

Character and relationship state come first because the existing readings already preserve their core chronology and because later claims, monographs, and specialists depend on them.

Post-cutoff status: items 1, 2, 5, and 6 have authoring-complete files; the map/README authority correction is present in the working tree; items 3, 4, 7, and 8 still require final reconciliation and exact-snapshot validation. The longitudinal gate therefore remains OPEN.

### 14.2 Second tranche

1. build TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md;
2. build TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md;
3. inventory material claim conflicts and missing locator levels;
4. perform only the targeted source checks those inventories require;
5. build TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md.

### 14.3 Third tranche

1. rewrite/deepen Tomozaki and Hinami under PREMIUM_QUALITY_FIRST;
2. rewrite/deepen Kikuchi and Mimimi under PREMIUM_QUALITY_FIRST;
3. decide mature monograph versus bounded dossier for Tama, Mizusawa, and Yuzu;
4. test supporting-character and ensemble promotion without automatic enrollment.

### 14.4 Fourth tranche

1. write the three mandatory relationship syntheses;
2. resolve which tested dyads or ensembles earn independent treatment;
3. write the seven mandatory thematic specialists;
4. promote any anticipated domain only through the architecture amendment rule.

### 14.5 Fifth tranche

1. run adversarial claim and locator review;
2. reconcile terminology, developmental states, actor knowledge, relationship standing, causality, confidence, and open contradictions across specialists;
3. substantially rewrite the full-series synthesis last;
4. issue a new literary validation/release audit against the final snapshot;
5. consider reconstruction models only after literary release.

## 15. Preserved files and explicit non-actions

The following are preserved:

- TOMOZAKI_ANALYTICAL_METHOD.md;
- TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md;
- the sequential-reading README;
- all eleven numbered-volume readings;
- both supplemental readings;
- TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md;
- all seven pre-remediation character candidates;
- TOMOZAKI_FULL_SERIES_SYNTHESIS.md as a provisional candidate;
- TOMOZAKI_FULL_SERIES_SYNTHESIS_VALIDATION_AUDIT.md as an immutable historical checkpoint;
- the bootstrap manifest and repository routing inputs.

This audit does not authorize:

- rewriting earlier predictions, questions, falsifiers, claim states, or abstentions;
- altering the old immutable audit's substantive historical findings; only reciprocal supersession metadata and a preservation notice may be corrected before first publication when repository authority validation requires them;
- deleting or silently replacing provisional monographs or synthesis;
- broad primary-source rereading without a documented gap;
- admitting V12+, adaptations, translations, interviews, reception, or unaudited bonuses;
- inferring Japanese register from English paraphrase;
- treating V08.5 reader knowledge as numbered-volume actor knowledge;
- upgrading provisional files merely by changing frontmatter;
- creating a monograph for every named character;
- creating ledgers for anime audio, visual grammar, game routes, or other inapplicable dimensions;
- beginning final-synthesis revision before convergence;
- generating reconstruction models as circular evidence for literary claims.

## 16. Validation and reconciliation blockers

### 16.1 Authority blockers and resolution

- The architecture was untracked at the cutoff, and this audit did not exist before the current operation.
- The map already routed to the architecture, role-gap audit, and first-backfill paths, but an unstaged router could not establish a reconciled release by itself.
- Before first publication, the former audit received only reciprocal `superseded` metadata and a preservation notice. The new audit's repository-root `supersedes` path, the former audit's reciprocal `superseded_by` path, the map, and the architecture now pass the authority-graph checks on the exact intended index.
- This resolves the repository-authority blocker for the staged remediation snapshot. It does not open the literary-maturity or integration gates.

### 16.2 Index/worktree blockers and resolution

- At cutoff, the index contained 26 paths from an earlier tranche, 11 of those or related paths had later unstaged edits, and the architecture plus first-backfill files were untracked.
- Any validation result that preceded reconciliation applied only to that earlier snapshot.
- All intended Tomozaki remediation paths were subsequently staged together, including the four authored cumulative backfills and reciprocal audit metadata.
- The exact staged index then passed `python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/tomozaki --repo .` with `PASS: phase=current snapshot=INDEX paths=3286`.
- The current branch is 39 commits behind origin/main; integration readiness cannot be inferred from local authoring success.

### 16.3 Semantic blockers

- General character state was not an accepted cumulative layer at cutoff; its post-cutoff file now passes file-local and exact-index checks but still requires cross-ledger and specialist reconciliation.
- Relationship state was still in active backfill at cutoff; its post-cutoff file now passes file-local and exact-index checks but still requires cross-ledger and specialist reconciliation.
- Claim/revision/evidence and social-systems owners were missing at cutoff; both now have authored, exact-index-validated backfills. Twelve targeted L2/L3 source-escalation queues remain open in the claim index.
- The Japanese voice/register owner remains missing.
- Seven character files remained provisional and too thin.
- No mature relationship or thematic specialist existed.
- The full-series candidate has retracted its former no-additional-ledger conclusion, but no mature successor can exist until the missing dependencies converge.
- No cross-specialist contradiction or terminology convergence was possible.

### 16.4 Evidence blockers

- Broad path links in monographs and synthesis do not provide deterministic claim-to-source retrieval.
- Many claims can begin at L1, but high-propagation causal, wording, register, consent, attribution, and chronology claims require selective L2/L3 work.
- Character-specific Japanese voice is too thin to certify.
- Locator and quotation checks must avoid invented page numbers and long copied passages.

### 16.5 State and metadata blockers

- V01–V07 plus V06.5 and V08.5 call themselves mutable_active although the corpus map, README, and architecture treat their prospective states as frozen.
- The full-series synthesis frontmatter and revised §20 now agree that it is active_provisional and that additional cumulative and specialist layers are required; its substantive integration remains pre-remediation evidence rather than a gate pass.
- Line anchors in mutable files will drift during remediation; final indexes should route by path, section/ID, and source locator rather than line number alone.

### 16.6 Final release checks required

The attempted repository command `python tools/validate_repository.py --phase current --snapshot worktree --routing-preflight series/tomozaki --repo .` returned: “FAIL: routing preflight requires a current Git index or exact commit with full schema validation.” That result was an expected snapshot-selection blocker, not a semantic pass.

The intended Tomozaki paths were then reconciled in the Git index. The bundled Python runtime lacked `jsonschema`, so the repository's exact hash-locked validation dependencies were installed into ignored `.scratch/validation-python-deps/` and supplied through `PYTHONPATH`; this did not modify the governed corpus or staging set. After removing a local-path publication hazard and repairing reciprocal, repository-root supersession routing, the exact command `python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/tomozaki --repo .` returned `PASS: phase=current snapshot=INDEX paths=3286`. No commit, push, merge, or rebase was performed.

Before literary release:

1. confirm source boundary and witness identities;
2. confirm every required path exists and every map route matches actual maturity;
3. validate YAML/frontmatter and authority/supersession fields;
4. validate links and path casing;
5. run whitespace and repository author checks on the intended final snapshot;
6. audit backward traceability from representative mature claims;
7. audit claim dispositions and unresolved contradictions;
8. audit temporal, focalization, actor-knowledge, side-story, and continuity boundaries;
9. audit Japanese wording/register claims against exact source;
10. audit monograph, relationship, and specialist semantic contracts;
11. audit cross-specialist terminology and state convergence;
12. confirm final synthesis contains no dependency-skipping or source-ending overclaim;
13. record the exact validated commit/index/worktree snapshot;
14. issue a successor validation/release audit.

## 17. Reasoning and execution record

The stable reasoning class for this role-gap audit and high-propagation downstream synthesis is PREMIUM_QUALITY_FIRST. The owner directed Max reasoning for synthesis documents and character monographs in this remediation operation. This artifact was produced in Codex Desktop using gpt-6-astra with Max reasoning as current execution metadata.

That statement is operational provenance only. It does not claim that:

- Codex Max is identical to a ChatGPT Pro product setting;
- one product surface's labels guarantee another surface's behavior;
- a provider/model label is a permanent architecture class;
- stronger reasoning substitutes for source evidence, locators, or validation.

Stable role classes remain in the architecture; provider mappings may change and must be rechecked under the reasoning policy.

## 18. Final disposition

### 18.1 What is complete

- The admitted V01–V11 plus V06.5/V08.5 source boundary is locked and sequentially analyzed.
- The analytical method remains fit.
- The effort/competition/goal-ownership ledger is mature through V11.
- The new synthesis architecture fully covers the Minimum Semantic Contract at design level.
- Character-state, relationship-state, claim/revision/evidence, and social-atmosphere/group-systems backfills are authored and pass the exact staged-index repository check.
- The role gaps and their dependency order are now explicit.

### 18.2 What remains

- reconcile the four authored cumulative backfills across state, claims, terminology, and targeted L2/L3 source escalations;
- build the Japanese voice/register/key-terms layer;
- mature four mandatory character monographs;
- deepen or bound three additional character studies;
- write three mandatory relationship syntheses and adjudicate tested ensemble/dyad candidates;
- write seven mandatory thematic specialists;
- reconcile claims, locators, contradictions, terminology, and state across specialists;
- rewrite the full-series synthesis last;
- run a new validation/release audit.

### 18.3 Gate statement

The correct current statement is:

- SEQUENTIAL SOURCE COMPLETION: PASS.
- ARCHITECTURE DESIGN: PASS, EVOLVING.
- LONGITUDINAL RECONCILIATION: OPEN.
- CHARACTER MATURITY: CLOSED.
- RELATIONSHIP AND SPECIALIST SYNTHESIS: CLOSED.
- CROSS-SPECIALIST CONVERGENCE: CLOSED.
- FULL-SERIES SYNTHESIS: ACTIVE_PROVISIONAL CANDIDATE ONLY; GATE CLOSED.
- VALIDATION/RELEASE: OPEN.

No mature full-series closure may be claimed until those states change through evidence-backed work.

## 19. Revision history

### v1.0 — 2026-09-13 — canonical role-gap checkpoint

- Recorded the post-policy historical architecture-gate violation with commit and line anchors.
- Audited TOMOZAKI_SYNTHESIS_ARCHITECTURE.md against every Minimum Semantic Contract responsibility and found design-level compliance.
- Separated architecture compliance from actual downstream implementation.
- Audited the entrypoint, method, source lock, every sequential reading, the effort ledger, all seven character candidates, the full-series synthesis candidate, the former audit, and Git state.
- Promoted the justified character-state, relationship-state, claim/evidence, social-systems, and Japanese voice/register cumulative responsibilities.
- Defined source-reopen boundaries, character and specialist dispositions, corrected dependencies, first and later remediation tranches, preservation rules, and validation blockers.
- Superseded only the former audit's architecture-readiness and synthesis-completion conclusions.
