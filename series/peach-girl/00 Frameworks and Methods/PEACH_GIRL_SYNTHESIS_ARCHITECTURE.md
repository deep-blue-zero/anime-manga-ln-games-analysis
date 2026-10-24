---
title: "Peach Girl — Synthesis and Corpus Architecture"
artifact_id: PEACH_GIRL_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.5"
status: active_provisional
scope: "Cumulative responsibilities, specialist dependencies, reconstruction and completion gates"
source_boundary: "Verified original Japanese manga V01–V18 already admitted; independent second-pass audit pending; no new narrative admission"
canonical_home: series/peach-girl/00 Frameworks and Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md
created: "2026-10-16"
architecture_lifecycle: EVOLVING
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Synthesis and corpus architecture

This architecture proposes how future sequential evidence becomes mature literary and behavioral work. It depends on the [method](PEACH_GIRL_ANALYTICAL_METHOD.md), the [source map](PEACH_GIRL_SOURCE_AND_SCOPE_MAP.md) and the live governance linked by the sole [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). It is an INITIAL, current-eligible provisional foundation awaiting owner audit. No previous Peach Girl architecture is superseded. File creation does not establish analytical completion or permission to read.

## Source model and canonical homes

The target is the original manga by 上田美和. The proposed sequential witnesses are Japanese 新装版 V01–V18, not every franchise object sharing the title. Original collected volumes, later editions and magazine serialization remain distinguishable witnesses. No page-for-page equivalence is assumed. Packaged bonus fiction, advertisements, illustrations, covers and editorial matter receive component classifications and separate admission decisions. Bibliographic publisher records identify editions and publication structure; their promotional descriptions are not literary evidence.

裏ピーチガール and ピーチガールNEXT are separately published related manga, outside the original-mainline boundary. Their relationship to this continuity would require separate authentication and admission; they must not become a parallel Peach Girl canonical root or silently enter earlier freezes. Anime, live action, novelization, localization, interviews, promotion and reception are separate lanes. None is admitted now. Unknown extras remain unknown rather than presumed absent.

Git holds methods, interpretations, compact witness references and governance. Drive holds canonical primary and deterministic derived evidence, including complete locator maps and any review images. Temporary downloaded sources and processing artifacts are working material. Nothing about local accessibility moves raw evidence into public Git authority.

`00 Frameworks and Methods/` holds the governing pair and source map. `03 Longitudinal Ledgers/` holds the four instruments below. `07 Audits and Handoffs/` holds the bootstrap receipt and later justified audits/checkpoints. Future readings use `02 Sequential Readings/`; evidence-ready character/relationship arguments may use `04 Character and Relationship Analysis/`; specialists and an integrated argument may use `05 Synthesis/`. These future paths are conventions, not present files or promised artifact counts. Do not create empty subject folders, monographs, models or synthesis documents.

## Accumulation and responsibility matrix

The route is sequential evidence → cumulative state → specialist synthesis → evidence-tested character reconstruction → full-series convergence → validation/release. The reconstruction stage is separately assessed and can remain blocked while a clearly scoped literary synthesis proceeds. It cannot be reported complete by finishing the literary pass.

| Recurring question | Sequential contribution and canonical cumulative home | Eventual use | Day-one decision |
| --- | --- | --- | --- |
| Who is the evidenced subject; how do goals, choices, self-presentation and capabilities change; what can be modeled? | Original observations in the reading; [character development/readiness](../03%20Longitudinal%20Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md) owns identity, developmental events, actor-level agency and readiness assessments | Character monograph and time-bounded behavioral model | Required, zero rows |
| What does A feel toward B, what do they call the relation, and what have they actually committed to? | [Directional relationships/commitments](../03%20Longitudinal%20Ledgers/PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER.md) owns pair-state transitions, offers/answers and relational boundary/repair consequences | Dyadic or ensemble relationship argument | Required, zero rows |
| Who knows, believes or circulates what; how does an audience's account affect social standing? | [Information/reputation](../03%20Longitudinal%20Ledgers/PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER.md) owns proposition, belief, transmission and audience-reputation states | Information asymmetry, misunderstanding and social reputation specialist | Required, zero rows |
| Which interpretations survive later evidence and why? | [Claims/revisions](../03%20Longitudinal%20Ledgers/PEACH_GIRL_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md) owns material propositions, alternatives, forecast terms and revision dependencies | Every consequential synthesis/model claim | Required, zero rows |
| How does panel form guide a reader's access to motive or events? | Exact text/form observations and Japanese uncertainty notes stay in the source reading; stable observation IDs permit independent retrieval | Manga-form specialist when recurring evidence justifies it | No independent visual or speech ledger yet |
| When did events occur and when were they disclosed? | Every observation/state has represented-time and learned-after fields; readings own event context | Chronology/causality account; possible later chronology instrument | No independent chronology ledger yet |
| What conduct, choices or consequences remain local? | Reading owns the specific encounter and alternatives; link material actor, pair and information consequences to their respective homes | Specialist argument if recurrence warrants it | Local-only when no cumulative consequence |

These are architectural questions chosen for the requested longitudinal/relationship/reconstruction goals across an 18-volume candidate corpus. They are not findings that any named character displays manipulation, dependency or a particular attachment. Four homes minimize duplicated state without committing to the larger ledger sets of other projects.

The reading owns each `PG-EV-…` observation, short quotation, translation uncertainty and context. A domain row owns a state change and points to observation IDs and material claim versions. The claims ledger owns why a proposition is accepted or revised; it does not duplicate the domain history. A specialist makes an argument from these records. A source hash or edition identity lives only in the source map, referenced elsewhere by source key. Cross-link IDs instead of reproducing whole scenes or maintaining two canonical current views.

## Sequential contribution and state preservation

Each authorized VNN contributes complete admitted-page coverage, entering/exit states, analytical reasoning and counterreadings, new observations, material ledger updates, inherited claim/prediction adjudication, source-stage advancement, readiness effects where warranted and an atomic validated commit. The method owns the detailed closure contract. No unit closes from a prose draft alone. The source map separates mainline completion from supplemental inspection; a supplement cannot advance the numbered-volume high-water mark.

Stable local IDs use `PG-CHAR`, `PG-CS`, `PG-RD`, `PG-RL`, `PG-CM`, `PG-IP`, `PG-KN`, `PG-TX`, `PG-RP`, `PG-CL`, `PG-PR`, `PG-RV`; observations use `PG-EV-VNN-####` and unit freezes `PG-FR-VNN`. Ledger allocation order is not story chronology. Global character identifiers remain unassigned until the authorized curation workflow acts. Each instrument defines required fields and row triggers; no cast, findings or predictions are prefilled.

Separate story time, publication/edition time, disclosure order, character belief and analyst claim state. A later account of an earlier event may be `REVEALED_NOT_NEW`, not a developmental transition. Preserve directional knowledge and public/private relationship understandings. An uncertain time interval stays uncertain. Temporal change does not itself create a new continuity or global character subject.

Frozen unit snapshots retain active claim/domain versions and a compact entering-state reconstruction. Mutable ledgers retain event history plus a current view. Later evidence changes current views through explicit revisions, never by silently editing prior prospective states. Major claims use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`, with old/new basis and downstream obligations. Failed forecasts remain recoverable. Whole-artifact supersession follows the repository's reciprocal authority graph rather than deleting old thinking.

## Contradictions and source escalation

Do not silently harmonize a disagreement. Test reading/translation error, narrator or focalizer scope, ignorance, deceptive intent, rumor, temporal change, remembered/imagined events, edition revision, separate continuity, paratextual framing and genuine inconsistency. Deliberate deception is a supported interpretation only when knowledge and intent are evidenced. Preserve more than one explanation if the source does not discriminate them.

A material conflict creates or revises a `PG-CL` claim and linked domain state. A source problem remains a source-map gap with affected locators. A dispute involving multiple claims, unstable edition identity or high propagation risk warrants a bounded audit in the existing audit home. No source escalation admits later narrative material without authorization. An unresolved load-bearing contradiction blocks the affected promotion or forces an explicit scoped provisional result.

## Specialist and character responsibilities

Anticipated specialist questions include romantic development and changing commitments; friendship/rivalry and nonromantic affiliation; information asymmetry and interpersonal manipulation where evidenced; reputation and peer audiences; agency, constraints, boundaries and interpersonal consequences; and manga form's effect on a reader's access to motives. An eventual ending/causality argument follows verified mainline completion. These are anticipated responsibilities, not mandatory day-one documents or conclusions.

A responsibility earns a separate specialist when evidence spans independent situations/units, poses a distinct explanatory question, needs sustained reconciliation, and would be poorly served by a section of another artifact. Relationship work must distinguish both directions and knowledge boundaries; asymmetry or thin access narrows its claims. A major character monograph warrants its own home when developmental phases, motive/self-report, ordinary and pressured behavior, relationships, written interaction, counterevidence and thematic function require integration. Lesser subjects can remain within scoped ensemble work. Do not force identical monograph depth across uneven evidence.

Dependencies matter: information-state reconciliation precedes strong claims about knowing deception; developmental and directional-state reconciliation precedes romantic/agency mechanisms; source-checked formal observations qualify each account of what the reader could infer; those arguments converge before an ending or full-series account. A form specialist may challenge a psychological reading rather than merely illustrate it. No fixed specialist roster can substitute for the post-sequential role-gap audit.

## Character reconstruction contract

This section is the canonical reconstruction specification at bootstrap. A separate specification file would duplicate a manageable contract, so none is created. A future model is an operational behavioral artifact, distinct from a literary monograph, cast entry or rich description. All subjects are presently unassessed; none is model-ready.

Every proposed model must bind a verified local subject/continuity, exact source and Git evidence snapshot, temporal state/cutoff, claim versions, intended scenario domain, limitations and assessment history. It must represent:

- Knowledge and belief accessible to the character at that time, including error and ignorance; reader-only information is excluded.
- Stable tendencies versus demonstrated development, with context-diverse support and counterexamples. Changed behavior is not normalized into one timeless personality.
- Motivations, conflicting desires, priorities, constraints, decision rules and evidenced characteristic misjudgments/failure conditions.
- Behavior with peers, intimates and strangers where inspected; romantic and nonromantic tendencies remain distinct and evidence-bounded.
- Written speech/address/register, conversational initiative, disclosure, refusal and repair patterns; acoustic voice is unavailable from unvoiced manga.
- Rule-level evidence strength, alternatives, unsupported contexts, negative constraints, triggers for abstention and bounded extrapolation.

Readiness is assessed separately for character evidence organization, literary monograph, operational model and scenario portability. A locally `DOMAIN_READY` assessment names a narrow domain and does not assign a global capability grade. Repeated scenes from one encounter are not independent contexts. Thin stranger/ordinary behavior or uncertain speaker identity blocks the corresponding model domain rather than inviting genre-based completion.

Before a model is accepted, retain a frozen rule set and perform a separately authorized validation using identifiable source-grounded cases with disclosure boundaries, predictions made before outcome access, alternatives and failure records. Distinguish observed fit, genuine held-out performance and untested extrapolation. If no valid held-out source exists, report that limitation; do not invent accuracy or call a retrospective fit prospective. New rules after failure receive new versions and untested status. Hypothetical or crossover scenarios are labeled noncanonical, preserve the selected state/knowledge, and do not become evidence about the original manga.

Validation authorizes only its declared domains. Global discovery and reconstruction capability records remain under their separate owner-reviewed workflows. This bootstrap authorizes no model construction, simulation, validation experiment or comparative adjudication.

## Completion gates and integration order

| Gate | Evidence needed to close | What closure does not establish |
| --- | --- | --- |
| G1 Sequential source completion | Every admitted original-mainline unit closed in order; exact witnesses, components, coverage, gaps and all 18 prospective freezes reconciled against verified publication/edition boundary | Ledger reconciliation, specialist maturity or franchise completion |
| G2 Longitudinal reconciliation | Four instrument histories/current views and claim versions agree with readings; unresolved forecasts/contradictions classified; source/locator audit and architecture/role-gap review completed | Relationship conclusions or model readiness |
| G3 Relationship and specialist synthesis | Justified character/dyadic/ensemble and specialist responsibilities make evidence-grounded arguments, preserve counterreadings, and reconcile their load-bearing dependencies | Behavioral portability or full-series integration |
| G4 Character-model readiness | Each proposed model/domain separately assessed under the reconstruction contract; mandatory evidence/validation debts closed or explicitly blocked with no completion claim | Universal simulation capability; a monograph alone cannot close this gate |
| G5 Full-series synthesis | G1–G3 closed; G4 dispositions recoverable; cross-specialist contradictions reconciled; a single integrated original-manga argument explains development, form and ending within declared exclusions | Final release or owner acceptance |
| G6 Validation and release | Consequential claims/quotations/locators checked, counterreading and coverage audit done, source/freezes verified, repository checks and final exact-head integration audit passed, owner release decision recorded | Admission of sequels, adaptations or new sources |

Gate decisions record scope, artifacts/versions, reviewer/date, evidence inspected, omissions, unresolved mandatory/optional work and next owner. A bounded provisional specialist can follow a closed tranche without claiming G1 or G3 for the full series. All gates are NOT_STARTED at bootstrap. A project can release a truthful literary scope with models explicitly unready; it cannot label the full intended modeling program complete. A future completed run records `run_state: completed` with no next candidate; optional project-local run seals and the required eventual terminal-closure route follow initiation Section 3.8. The present CLOSED bootstrap is not a completed run and needs no closure record. Admission closure does not prohibit authorized retrospective correction of already admitted interpretations; it never permits editing frozen source-reading bytes.

Before specialist dispatch, stabilize the relevant locators/claims and provide an exact frozen input snapshot. Before full-series synthesis, repeat the architecture/role-gap audit and converge specialist arguments; do not concatenate abstracts. Final validation may require bounded source reinspection and dependent revisions. An unsupported central premise reopens affected outputs while preserving unaffected prose and historical freezes.

## Execution, reproducibility and amendment

Source inventory/locator reconciliation uses `BOUNDED_STANDARD`; serious sequential reading and interpretive state updates use `SUBSTANTIVE_ANALYSIS`; architecture, checkpoints, monographs, specialists and reconstruction use `DEEP_SYNTHESIS`. Full-series convergence uses `PREMIUM_QUALITY_FIRST` because a load-bearing error can propagate across many mature claims; assess success by evidence traceability, temporal consistency and counterreading coverage. Deterministic checks may use tools. These classes inherit live reasoning policy and do not encode a provider preference.

One designated source-capable sequential operator owns each reading and synchronized mutable ledgers; one integration operator owns Git publication. A fresh adequately grounded synthesis session is the preferred later owner for substantial retrospective arguments under the long-series protocol. Actual environment/capability is verified for each stage; this hosted bootstrap verified Git/text authoring, Drive metadata and V01 transport/packaging, not narrative image inspection. No subagents or parallel analytical runs are commissioned here.

For substantial handoff, transfer the full files plus exact Git/base/tree, method/architecture versions, source set/checksums, locator-map versions, component boundary, inspected/completed coverage, last freeze, claim/domain versions, unresolved debts, output identities and acceptance criteria. Record actual producer/receiver, surface/runtime, observed configuration or unknown values, time and inspection route. The receiver verifies bytes and compares handed-off base, returned candidate and live target before integration. A summary is navigation, not a substitute for the analytical corpus.

An approved bootstrap baseline can later be frozen by exact commit and source/locator set for independent executions with reconstructible entering states. Output candidates must retain their lineage and remain isolated until separately authorized acceptance. No extra canonical roots, experiment assignments, comparative criteria or anticipated comparative findings are created. Reproducibility does not require identical interpretations; it requires recoverable sources, methods and state transitions.

Review architecture after the first meaningful closed tranche, recurring unrepresented evidence, new source types, major retrospection, sequential completion, specialist dispatch and release. Add a ledger only for recurring independent evidence/retrieval that existing homes cannot adequately hold; merge redundant responsibilities only with preserved IDs/history. Visual form, speech, standalone agency and chronology remain candidates. Backfill only a material gap not repairable from existing readings and retained evidence. Record material amendment, rationale, affected dependencies and version in this document and the entrypoint. Lifecycle may become EVOLVING, then STABILIZED, then an explicitly FROZEN release; none occurs merely with elapsed time.

Mutable homes are the entrypoint, source-admission map, method/architecture and cumulative ledgers, maintained by targeted edits. Prospective freezes, accepted checkpoints and release manifests preserve their exact historical state. Later errata or successor versions remain discoverable. Start retrieval at the entrypoint, then source map and governing pair, then relevant ledger/last freeze, reading and primary witness. Do not reconstruct permission or authority from an old chat.

Revision history: 0.1 — INITIAL owner-audit candidate, 2026-10-16 UTC; four justified instruments and reconstruction contract specified; no findings. Review status updated 2026-10-16 UTC after owner execution authorization; content unchanged. The run's single-operator CLOUD_ONLY arrangement is recorded in the initiation record.


## Amendment0.2 — post-sequential responsibility audit,2026-10-20

The original INITIAL specification above is historical bootstrap language. Current lifecycle EVOLVING follows the actual [G1/G2 review](../07%20Audits%20and%20Handoffs/PEACH_GIRL_G1_G2_LONGITUDINAL_RECONCILIATION.md), not elapsed time. G1 closes for inherited audited V01–V04 plus new full V05–V18; G2 closes for four histories/current projections. G3–G6 remain pending here.

Evidence warrants separate Momo/Kairi/Tōji/Sae monographs, a scoped Misao/Ryo/supporting-cast study, directional dyadic/ensemble work, and distinct information/reputation, agency/repair and manga/Japanese-form specialists. No new ledger: existing event/knowledge/readings already cover chronology, agency, speech and form. Uneven evidence limits supporting subjects rather than forcing identical coverage.

The present owner recovery brief expressly authorizes G4 assessment and actual testing. It supersedes the bootstrap's no-construction authorization statement for this new run; all evidentiary constraints remain. No genuinely held-out original source remains after full exposure. Freeze any rule set before testing; disclose retrospective design, alternatives, failure and abstention. Operational portability cannot be declared validated from retrospective fit. G4 may remain BLOCKED_NO_HELD_OUT_VALIDATION while a truthful literary scope proceeds.

One source-capable operator continues; no independent blind reviewers or agents are commissioned. Mature synthesis begins only after this audit commit. Full-series convergence follows G3/G4 dispositions; repeat role-gap audit at G6. No adaptation/sequel/source promotion/global registry write is admitted.


## Amendment0.3 — converged literary scope and model debt,2026-10-20

The [G5 decision](../07%20Audits%20and%20Handoffs/PEACH_GIRL_G5_CONVERGENCE_AND_ROLE_GAP_DECISION.md) repeats the role-gap review after9 G3 studies and actual G4 testing. No new ledger/specialist is mandatory for the original literary scope. [Full-series synthesis](../05%20Synthesis/PEACH_GIRL_FULL_ORIGINAL_SERIES_SYNTHESIS.md) integrates causal, social, romantic, reputational, structural and visualarguments while keeping competingendingreadings.

G1/G2 CLOSED/compositeprovenance;G3 CLOSED_scopedliterary;G4 assessment/testsperformed but operationalacceptanceBLOCKED_NO_HELD_OUT_VALIDATION/no fullmodelprogramcompletion;G5 CLOSED_scopedliterary;G6 localchecks/packagepending/externalintegrationandownerreleaseunperformed. Lifecycle remains EVOLVING untilfinalvalidation; no automaticreleaseFROZEN or acceptance.


## Amendment0.4 — verified local literary architecture,2026-10-20

The [G6 local audit](../07%20Audits%20and%20Handoffs/PEACH_GIRL_G6_LOCAL_VERIFICATION_AND_LIMITS.md) records actualsource/corpus/dependency/freeze checks and repeatedrole-gapreview. Lifecycle STABILIZED applies to this completedoriginal-mangaliteraryorganization:18readings/4ledgers/9G3studies/G4assessment/G5convergence. No furthermandatoryledger/specialist isidentified. This is not releaseFROZEN or owneracceptance.

G4operationalacceptance remainsBLOCKED_NO_HELD_OUT_VALIDATION; modelprogramincomplete. G6localpackageproof is generatedafterfinalcommit; fullG6externalintegration/remoteaudit/evidencepromotion/ownerrelease remainUNPERFORMED. Historicalbootstrap and amendmentgate statements above retain their dates; currentdispositions arethisamendment/entrypoint/G6audit. No new narrativeadmission or historicalfreezeedit.

## Amendment 0.5 — independent second-pass responsibilities, 2026-10-23

The owner-authorized independent second pass applies method 0.3 to already admitted V01–V18. Historical bootstrap and amendments 0.2–0.4 retain their actual judgments and dates. The architecture is now EVOLVING for this explicit reassessment; this does not assert an analytical defect before source review or erase the earlier STABILIZED literary organization. The [second-pass audit](../07%20Audits%20and%20Handoffs/PEACH_GIRL_SECOND_PASS_AUDIT_20261023.md) records new evidence and decisions. Source admission remains complete with no new candidate; no historical sequential reading or prospective freeze is rewritten.

### Evidence ownership and downstream sequence

The method's all-volume Pass A completion receipt precedes systematic Pass B comparison. Finalized source-first notes and their recoverable private locations stay outside public Git; sanitized per-volume coverage, note hashes, exposure and capability limitations belong in the second-pass audit. Source identities/checksums remain owned by the source map and its verification receipts; the audit identifies the exact snapshot checked. Private notes are preliminary independent work, not competing canonical volume readings.

The audit owns attributable findings, material new `PG-SA2-VNN-####` observations, errata and the navigable reading-to-correction route. Existing `PG-EV` observations remain in their original readings. Each supplemental observation links to the original frozen reading/exit and exact witness/locator through the audit route, without changing original bytes. The four existing ledgers continue to own domain histories/current states and claim revisions. Monographs, relationship studies and specialists continue to own their established arguments; the audit routes corrective obligations to them and does not duplicate their canonical conclusions.

The second-pass dependency order is: finalized all-volume source-first receipts → volume comparison/findings → affected longitudinal and claim revisions → character/relationship and specialist deepening → second-pass G3 decision → reconstruction assessment with explicit limits → cross-specialist convergence → second-pass G5 decision → G6 verification/publication. Dependencies may require returning a changed central premise to its affected current homes before acceptance. Repeat the responsibility assessment at G5. Do not interpret this ordering as permission to postpone a material downstream correction beyond publication.

### Source-to-synthesis depth and coverage matrix

Maintain this review as a section of the existing second-pass audit, not a fifth longitudinal ledger. Assess each major character, directional relationship or ensemble responsibility, specialist responsibility and integrated synthesis responsibility against the actual reviewed content. A compact row may group related evidence only when its locators, developmental distinctions and disposition remain recoverable.

| Required field | Review responsibility |
| --- | --- |
| Subject/question and canonical home/version | Name the existing artifact and section that owns the question; mark a missing home explicitly rather than infer adequacy from an inventory |
| Consequential evidence and state route | Link original `PG-EV` or new `PG-SA2` observations, source locators, material ledger/claim versions and relevant temporal phases |
| Analytical work required and inspected | Identify mechanism, development, directionality, knowledge, counterreading or formal distinction that the home must explain; identify the actual sections reviewed |
| Integration disposition | Assign `INTEGRATED`, `INTENTIONALLY_OMITTED_WITH_JUSTIFICATION`, `LOST_THROUGH_COMPRESSION`, `MISINTERPRETED_OR_MISATTRIBUTED` or `UNCERTAIN_NOT_PROMOTED`, with reasons and contrary evidence |
| Remedy and dependencies | Record expansion/correction in the current home, a justified separate responsibility only if needed, downstream affected artifacts, owner and completion evidence |
| Remaining limits | Distinguish mandatory debt blocking the declared scope from optional enrichment and unsupported domains |

Record source inspection, material observation coverage, explanatory depth, longitudinal character development, relationship reconstruction, specialist integration, behavioral reconstruction and validated portability as separate axes. Trace consequential evidence across phases and ordinary as well as crisis contexts; do not demand that every local scene be repeated in synthesis. An intentional omission needs an analytical reason, and an uncertain claim needs an explicit non-promotion disposition. Word count, document existence, a green repository check or agreement between agents does not establish semantic adequacy.

### Separate role-gap decisions at G3 and G5

For each reviewed responsibility, answer both questions independently:

1. **Missing responsibility:** Does a consequential recurring question lack a canonical home? Identify the distinct question, distributed evidence, dependency and why an existing artifact cannot adequately own it before creating a new home.
2. **Underdeveloped responsibility:** Does an existing home's actual explanation fail to preserve material evidence, developmental stages, decision mechanisms, directional differences, form or counterevidence? Expand or correct that home when its scope already encompasses the problem; insufficient depth alone does not justify another file.

Also record unnecessary duplication and evidence stranded in readings or ledgers. A monograph or specialist's presence answers neither question. Preserve earlier G3/G5 decisions as dated historical evaluations, then issue an attributable linked successor/reassessment for the second pass with the exact reviewed corpus and unresolved obligations. Do not silently reuse a former closure as proof of current adequacy or declare a gap repaired before the relevant content is reviewed. The entrypoint must distinguish prior scoped closures from pending second-pass decisions.

### Reconstruction maturity and canonical responsibilities

| Artifact/maturity | Responsibility and limit |
| --- | --- |
| Literary character monograph | Explains evidenced development, motives, relationships, written language, form and thematic function; does not itself establish a behavioral simulation |
| Source-grounded time-indexed reconstruction dossier | Organizes a character's evidenced states and context-sensitive behavioral mechanisms across meaningful cutoffs; may be substantially developed while validation is unavailable |
| Executable categorical prototype | Implements a bounded frozen rule set and declared case domain; a handful of categories does not constitute comprehensive reconstruction or establish portability |
| Validated operational model | Meets independent acceptance requirements for explicitly tested domains and temporal states, with genuine held-out evidence, failures, calibration or portability claims supported to the extent asserted |

A dossier should make identity/continuity, source/evidence snapshot, temporal phases, knowledge and beliefs, competing goals, stable/contextual tendencies, decision mechanisms and errors, emotional/interpersonal responses, romantic/nonromantic behavior, social presentation and written speech, counterevidence, failure conditions, unsupported contexts, abstention reasons and scenario limits recoverable. Preserve contradictions and changing states rather than building one timeless personality. A character at a selected cutoff cannot use future facts known only to the auditor.

Deepen the established character home where it can hold that responsibility clearly. A separate dossier requires a distinct source-grounded reconstruction responsibility and an entrypoint route; do not create it merely to increase artifact counts. Assess supporting subjects within their actual evidence limits, naming missing domains rather than forcing equal readiness. No new reconstruction specification or ledger is required by this amendment; the governing contract stays here.

Retrospective rule testing can expose contradictions and overgeneralization, with frozen versions, failures and post-test revisions preserved, but full-outcome exposure prevents it from becoming held-out predictive validation. Existing G4 operational acceptance remains `BLOCKED_NO_HELD_OUT_VALIDATION` unless valid new independent evidence satisfies the existing acceptance contract. Dossier development, successful retrospective fit or a completed literary pass cannot remove that blocker. Do not claim calibrated reliability, conversational portability or acoustic voice from unvoiced manga, and do not write global reconstruction-capability records.

### Second-pass completion boundary

The new audit must report actual all-volume inspection and comparison coverage, significant agreements/corrections/omissions/compression, propagation state, source-to-synthesis dispositions, exposure limitations and remaining evidence/capability debts. G3/G5 semantic closure requires reviewed arguments and evidence of discharged responsibilities. G4 retains scoped readiness and the operational blocker. G6 separately requires historical-byte/source integrity, reconciled consequential claims, resolved mandatory debt, repository validation and the exact final-head remote audit under live publication controls. Prior gate decisions and a prior successful audit do not certify the revised head.

The existing entrypoint remains the sole current retrieval surface and must identify governing versions, audit route, pending duties and actual publication state. Draft-to-Ready is conditional on completing the owner's mandatory audit and validation; preserve any independent owner hold and leave integration to its designated process. No new ledger, duplicate canonical synthesis, franchise source, frozen-byte change, global governance or registry change is authorized by this amendment.

Revision history addendum: 0.5 — prospective independent second-pass responsibilities and EVOLVING reassessment, 2026-10-23 owner date; source-to-synthesis dispositions, separate G3/G5 gap questions and reconstruction maturity distinguished. Earlier closures remain historical; no new semantic closure, model acceptance or publication completion is claimed.
