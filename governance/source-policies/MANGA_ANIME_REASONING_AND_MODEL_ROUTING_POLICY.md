---
title: Manga / Anime Reasoning and Model Routing Policy
artifact_id: MANGA_ANIME_REASONING_MODEL_ROUTING_POLICY
artifact_type: reasoning_model_routing_policy
version: 1.0
status: CANONICAL
scope: corpus-wide analytical artifact generation
created: 2026-08-27
maintainer: ChatGPT + user
do_not_use_as_literary_evidence: true
current_provider: OpenAI
current_model_family: GPT-5.6
current_chatgpt_mapping_verified: 2026-08-27
current_pricing_verified: 2026-08-27
supersedes: null
superseded_by: null
---

# Manga / Anime Reasoning and Model Routing Policy

## Governing principle

> **Route analytical work by the kind of reasoning it requires, not by document length, prestige, or habit; keep the durable reasoning class stable while treating literal model names, reasoning controls, availability, and prices as a replaceable provider snapshot.**

This policy governs model/reasoning selection for future analytical artifacts in the Manga / Anime project. It is corpus-wide infrastructure, not literary evidence. It exists so that a new chat, a new series, or a new OpenAI model release does not require reasoning-budget decisions to be reconstructed from memory.

The policy has two deliberately separate layers:

1. **Stable project reasoning classes** describe the intellectual workload in model-agnostic terms.
2. **Current provider mappings** translate those classes into the reasoning/model controls currently available in ChatGPT or another execution surface.

The stable class is the durable recommendation. The literal model name is a time-bounded implementation choice.

---

# 1. Scope and precedence

This policy applies to future artifacts generated for the Manga / Anime analytical corpus, including:

- sequential deep readings;
- checkpoints;
- longitudinal ledgers;
- claim-revision ledgers;
- evidence matrices and locator indexes;
- character monographs;
- relationship studies;
- specialist syntheses;
- full-series syntheses;
- character reconstruction models;
- prospective-model adjudication and experiment reports;
- validation, consistency, contradiction, and release audits;
- corpus maps, manifests, checksum maintenance, and other analytical administration.

It does **not** determine literary authority, source authority, or truth. A document produced at a higher reasoning tier is not automatically more authoritative than a lower-tier document. Authority continues to be determined by the series architecture, source boundary, evidence provenance, revision state, and `ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`.

## Precedence

When selecting a reasoning configuration for a specific operation, use:

1. **explicit user instruction for the current operation**;
2. **current canonical/frozen series architecture or method**, when it assigns a reasoning class or tier to that artifact;
3. **this corpus-wide policy**;
4. **the platform/model default**, only when no stronger routing rule exists.

A series architecture may override the global default because some projects have unusually high contradiction density, visual/audio requirements, branching state, source ambiguity, or reconstruction complexity. Such overrides should state why.

A new chat does not reset these routing rules.

---

# 2. Stable reasoning classes

Every future substantive project artifact should, when practical, be assigned one of the following stable classes.

| Stable class | Intended workload | Current ChatGPT mapping |
|---|---|---|
| `ROUTINE_FAST` | deterministic, clerical, low-ambiguity administration | GPT-5.6 Sol Instant |
| `BOUNDED_STANDARD` | bounded extraction, normalization, indexing, or structured synthesis with limited interpretive ambiguity | GPT-5.6 Sol Medium |
| `SUBSTANTIVE_ANALYSIS` | serious analytical work with a well-defined scope and manageable interaction count | GPT-5.6 Sol High |
| `DEEP_SYNTHESIS` | high-dimensional interpretation, cross-source integration, contradiction handling, retrospective synthesis, or difficult character/thematic reconstruction | GPT-5.6 Sol Extra High |
| `PREMIUM_QUALITY_FIRST` | exceptionally difficult, propagation-sensitive, quality-first work where additional model work has a plausible material reliability advantage | GPT-5.6 Sol Pro |

These names are intentionally provider-independent. A future GPT-6, GPT-7, or non-OpenAI execution surface should be mapped onto these classes without rewriting every historical series architecture.

---

# 3. What each class means

## 3.1 `ROUTINE_FAST`

Use when the operation is overwhelmingly deterministic and the cost of deeper interpretive reasoning is negligible.

Typical examples:

- checksum regeneration;
- simple manifest insertion once all fields are already known;
- renaming/routing metadata operations whose target is unambiguous;
- mechanical format normalization;
- confirming exact counts already produced by a verified extraction step;
- copying an already-approved value into a corpus map.

Do **not** use merely because the requested output is short. A one-paragraph claim adjudication can require deeper reasoning than a ten-page manifest.

Escalate above `ROUTINE_FAST` when the operation requires deciding among competing interpretations, reconciling inconsistent sources, or inferring a new analytical state.

## 3.2 `BOUNDED_STANDARD`

Use for work that requires genuine reasoning but is narrow, highly structured, and easy to verify.

Typical examples:

- source inventory reconciliation;
- locator index construction after source boundaries are stable;
- schema-driven evidence extraction;
- low-ambiguity crosswalk construction;
- bounded metadata/source audits;
- structured ledgers where the interpretation has already been established elsewhere and the task is primarily routing or normalization.

The class is appropriate when errors are generally local and readily auditable rather than interpretively contagious.

## 3.3 `SUBSTANTIVE_ANALYSIS`

Use for normal high-quality analytical work in the corpus.

Typical examples:

- sequential volume/episode deep readings with a mature method;
- bounded character or relationship analyses;
- thematic ledger updates with established categories;
- evidence-based specialist sections whose governing question is narrow and whose major concepts are already stabilized;
- readiness assessments where state criteria are explicit;
- source-grounded synthesis across a modest number of artifacts.

This is not a “cheap” or low-quality class. It is the default for intellectually serious work that is well constrained enough that larger reasoning budgets are unlikely to change the governing conclusion materially.

## 3.4 `DEEP_SYNTHESIS`

Use when the task contains enough interacting evidence, ambiguity, or retrospective dependence that extended reasoning is likely to improve consistency and calibration.

Typical triggers include:

- many volumes/episodes must be integrated simultaneously;
- later evidence substantially recontextualizes earlier readings;
- several plausible interpretations must be distinguished rather than collapsed;
- a character has strong state changes, masks, unreliable self-reports, role-conditioned behavior, or relationship-specific policies;
- the artifact must separate causal explanation from moral justification or responsibility;
- visual, linguistic, institutional, thematic, and character evidence interact;
- a contradiction could reflect chronology, source perspective, translation, unreliable narration, or genuine inconsistency;
- the task requires an adversarial counterreading rather than only a positive synthesis.

Most mature full-series specialist syntheses should begin here unless their scope is unusually bounded.

## 3.5 `PREMIUM_QUALITY_FIRST`

Use selectively. This class is not simply “more important” or “longer.” It is reserved for tasks where the additional model work of the premium/Pro mode has a plausible **meaningful marginal reliability advantage**.

Strong candidates have several of the following properties:

- **propagation sensitivity:** an error will become an input to many later artifacts;
- **integration breadth:** the task must reconcile a large fraction of the corpus rather than a local subset;
- **contradiction density:** multiple high-quality evidence routes support competing formulations;
- **epistemic fragility:** conclusions depend on maintaining distinctions among fact, inference, speculation, narrator knowledge, character knowledge, retrospective knowledge, and present-authority claims;
- **adversarial requirement:** the artifact must actively search for failure cases, disconfirming evidence, alternative explanations, or cross-document inconsistency;
- **non-local validation:** quality cannot be assessed by checking one source or one section in isolation;
- **high downstream cost of error:** the artifact defines architecture, claim routing, final integration, or model validity for many subsequent documents;
- **clear evaluation criteria:** there is a concrete way to judge whether the extra model work improved the result.

Typical examples:

- corpus-wide claim-revision ledgers that route all later specialist work;
- the most causally or psychologically difficult central-character monographs;
- ending/causality syntheses with many competing readings and retrospective dependencies;
- adversarial contradiction/counterreading matrices;
- final continuous full-series syntheses written after specialist convergence;
- cross-model consistency audits spanning multiple reconstruction models.

Do **not** use Pro merely because it exists. If Extra High reliably produces equivalent quality for that artifact class, downgrade future instances.

---

# 4. Decision factors

Reasoning selection should be based on the following factors rather than word count alone.

## 4.1 Error propagation

Ask: **If this artifact is wrong, how many later artifacts inherit the error?**

A local deep reading can often be corrected locally. A claim-revision ledger, synthesis architecture, or final cross-model audit can contaminate an entire downstream phase. Higher propagation warrants more reasoning.

## 4.2 Evidence breadth

Ask how many independent source regions, volumes, episodes, ledgers, or specialist analyses must remain simultaneously coherent.

Large input size alone is not enough for Pro; a 500-page deterministic locator build can remain bounded. What matters is how much of that material must be *interpreted together*.

## 4.3 Interpretive ambiguity

Escalate when several readings remain genuinely plausible and the artifact must distinguish them by evidence rather than choose the most narratively convenient one.

## 4.4 Temporal/state complexity

Character and institutional analysis becomes harder when claims must be indexed to developmental state. A statement true at one point in a series may be false later without either observation being erroneous.

## 4.5 Contradiction and source-perspective burden

Higher reasoning is warranted when apparent contradictions may arise from:

- later revision;
- unreliable narration;
- character ignorance;
- propaganda;
- translation;
- paratext;
- adaptation divergence;
- continuity branches;
- scene-performance evidence versus transcript content;
- or actual textual inconsistency.

## 4.6 Reversibility and auditability

Mechanical errors that are immediately visible and cheap to repair do not justify premium reasoning as readily as subtle synthesis errors that can survive many downstream reads.

## 4.7 Evaluation clarity

Pro is most defensible when the result can be evaluated against explicit criteria: contradiction count, evidence coverage, prediction adjudication, source traceability, cross-model consistency, or preservation of earlier claim boundaries.

---

# 5. Current OpenAI / ChatGPT mapping — verified 2026-08-27

This section is intentionally time-sensitive and may be revised in place without changing the stable reasoning classes above.

Current official OpenAI documentation describes the ChatGPT choices as:

- **Instant** — fast responses for everyday questions;
- **Medium** — standard reasoning with GPT-5.6 Sol;
- **High** — extended reasoning with GPT-5.6 Sol;
- **Extra High** — the highest reasoning effort available with GPT-5.6 Sol;
- **Pro** — GPT-5.6 Sol Pro for difficult tasks and longer-running workflows.

Current project mapping:

```yaml
provider: OpenAI
surface: ChatGPT
verified_date: 2026-08-27
stable_class_mapping:
  ROUTINE_FAST: "5.6 Sol Instant"
  BOUNDED_STANDARD: "5.6 Sol Medium"
  SUBSTANTIVE_ANALYSIS: "5.6 Sol High"
  DEEP_SYNTHESIS: "5.6 Sol Extra High"
  PREMIUM_QUALITY_FIRST: "5.6 Sol Pro"
```

For the currently documented Business/Enterprise/Edu credit-based ChatGPT rate card, Medium, High, and Extra High all use GPT-5.6 Sol and are charged at the same per-message rate, while Pro uses GPT-5.6 Sol Pro at five times that per-message credit rate. The project therefore should not economize among Medium/High/Extra High merely because one reasons longer when their applicable credit cost is equal. Pro requires a separate marginal-value justification.

Current official-source set used for this mapping:

- OpenAI Help Center — **GPT-5.6 in ChatGPT**: https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt
- OpenAI API — **Model guidance**: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI Help Center — **ChatGPT Rate Card**: https://help.openai.com/en/articles/11481834
- OpenAI Help Center — **ChatGPT Release Notes**: https://help.openai.com/en/articles/6825453-
- OpenAI Help Center — **Model Release Notes**: https://help.openai.com/en/articles/9624314-model-release-notes

These URLs are routing references, not frozen evidence. Their contents can change.

---

# 6. How this policy uses OpenAI's guidance

The current routing policy follows several principles stated in OpenAI's own documentation:

1. reasoning effort should be selected intentionally for the workload;
2. a medium/default level is a balanced starting point for general work;
3. higher reasoning should be used when it produces a measurable quality gain;
4. maximum reasoning should be reserved for the hardest quality-first workloads;
5. Pro mode is appropriate when marginal quality improvement materially affects a difficult task;
6. representative tasks should be compared rather than assuming the largest reasoning budget is always optimal.

The project adds its own domain-specific translation of those principles into artifact classes. OpenAI does not prescribe which anime/manga document belongs to which tier.

---

# 7. Pro cost/value rule

`PREMIUM_QUALITY_FIRST` requires an explicit reason because premium execution is materially more expensive.

For current ChatGPT credit-based pricing, the project assumes:

```yaml
current_credit_assumption:
  instant: "unlimited / not charged as a Sol reasoning message under the cited rate card"
  medium: 10
  high: 10
  extra_high: 10
  pro: 50
verified_date: 2026-08-27
```

This is a provider snapshot, not a permanent project constant.

A Pro recommendation should identify the expected marginal benefit in terms such as:

- reduced contradiction risk;
- stronger adversarial verification;
- better long-range integration;
- more reliable claim-state reconciliation;
- improved cross-model consistency;
- or prevention of propagation from a load-bearing upstream artifact.

A Pro recommendation should **not** be justified only by:

- document length;
- central-character popularity;
- prestige of the project;
- the desire to make an artifact “definitive”;
- or the fact that credits are available.

---

# 8. Pro downgrade and escalation rule

A tier assignment is a default, not a metaphysical property of the document.

## Downgrade

If representative Extra High work demonstrates equivalent analytical quality for a Pro-designated artifact class, later instances should be downgraded to `DEEP_SYNTHESIS` unless a new complication appears.

Evidence supporting downgrade can include:

- equivalent contradiction detection;
- equivalent evidence coverage;
- no material difference under adversarial review;
- stable claims across repeated runs;
- or a later model generation that makes the premium mode unnecessary.

## Escalation

Escalate from High or Extra High to Pro when preliminary work exposes:

- unresolved high-impact contradictions;
- repeated loss of temporal or epistemic state distinctions;
- failure to reconcile several strong evidence routes;
- unusually high dependency on cross-document consistency;
- or demonstrated quality gains from a Pro comparison pass.

When escalation occurs, the artifact or series architecture should record the reason.

---

# 9. Model-release and documentation-freshness rule

Literal model names and reasoning controls are volatile. The project must not treat a historical routing table as permanent product truth.

## Mandatory re-check triggers

Before establishing or materially revising reasoning recommendations, consult current **official OpenAI documentation and release announcements** when any of the following is true:

1. OpenAI releases a new flagship ChatGPT reasoning model or model family;
2. the ChatGPT model picker adds, removes, or renames a reasoning level;
3. Pro changes model family, behavior, availability, or pricing;
4. OpenAI adds a new reasoning control that could materially affect analytical work;
5. the current policy's provider mapping has not been verified recently and a new major analytical phase is about to begin;
6. observed output quality suggests that the old mapping is no longer optimal;
7. a series architecture is about to designate a large number of expensive premium operations.

## Recommended freshness cadence

Do **not** web-search OpenAI documentation before every deep reading. That creates noise without meaningful benefit.

Instead:

- re-check at **model/feature release boundaries**;
- re-check before a **new major project phase** if the mapping has not been verified within roughly 30 days;
- re-check before committing to a **large Pro tranche** if pricing or capability may have changed;
- otherwise reuse the latest verified canonical mapping.

## Source priority for model routing

Use official OpenAI sources in this order where applicable:

1. product/model-specific Help Center documentation;
2. OpenAI developer model guidance and reasoning documentation;
3. official ChatGPT/model release notes;
4. official rate card/pricing documentation;
5. official OpenAI announcements where the above have not yet incorporated a release.

Third-party benchmarks and community reports may inform later empirical evaluation but do not define the canonical product mapping.

---

# 10. Migration when a new model family appears

When a new model family becomes available:

1. **do not rewrite historical artifacts merely to replace old model names**;
2. verify current OpenAI documentation and release notes;
3. update only the **Current OpenAI / ChatGPT mapping** section of this policy unless stable class definitions themselves need revision;
4. preserve the prior mapping in the policy changelog;
5. update `MANGA_ANIME_DRIVE_INDEX.md` if the routing change is material;
6. use the new mapping for future artifacts;
7. do not change an immutable/frozen release merely because the execution model changed.

Series architectures should preferably store both a stable class and the literal model mapping that was current when the recommendation was made.

Example:

```yaml
recommended_reasoning_class: DEEP_SYNTHESIS
recommended_reasoning_at_design_time: "5.6 Sol Extra High"
reasoning_policy: MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md
```

If a future mapping resolves `DEEP_SYNTHESIS` to a different model/tier, the stable class remains valid without rewriting the architecture.

---

# 11. ChatGPT UI versus API / Work / Codex controls

Do not assume that similarly named controls on different OpenAI surfaces are identical.

As of the current verification date:

- ChatGPT exposes Instant, Medium, High, Extra High, and Pro as user-facing choices for eligible plans;
- the API exposes `reasoning.effort` values such as `medium`, `high`, `xhigh`, and `max`;
- API **Pro mode** and **reasoning effort** are independent controls.

Therefore:

> **Do not encode `Extra High = API xhigh`, `Pro = API max`, or any other one-to-one equivalence as a permanent project rule.**

If Codex, Work, the API, or another agent surface generates a corpus artifact, map the stable project class onto that surface using its current official documentation.

The artifact's stable reasoning class is more durable than the surface-specific control used to execute it.

---

# 12. Front-matter standard for future artifacts

New Markdown analytical artifacts should normally include routing metadata in addition to their existing authority metadata.

Recommended fields:

```yaml
recommended_reasoning_class: DEEP_SYNTHESIS
resolved_reasoning_option: "5.6 Sol Extra High"
reasoning_policy: MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md
reasoning_policy_version: "1.0"
model_guidance_verified_date: "2026-08-27"
```

For premium artifacts:

```yaml
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
resolved_reasoning_option: "5.6 Sol Pro"
pro_justification: "Propagation-sensitive cross-corpus claim reconciliation; errors would route multiple downstream specialist syntheses."
```

For a series-specific override:

```yaml
reasoning_override: true
reasoning_override_reason: "Series architecture requires adversarial multi-branch continuity reconciliation."
```

These fields are routing metadata, not evidence and not an authority ranking.

## Non-Markdown sidecars

TSV, JSON, checksum, and other sidecar files need not embed YAML. Their generating operation should inherit the reasoning class from the governing architecture, manifest, or associated Markdown artifact.

---

# 13. Recommended default by artifact role

These are corpus-wide defaults. Series architectures may override them.

| Artifact role | Default class | Notes |
|---|---|---|
| checksum / mechanical manifest regeneration | `ROUTINE_FAST` | escalate if content authority must be adjudicated |
| source inventory / lock audit | `BOUNDED_STANDARD` | High when source identity or edition status is ambiguous |
| locator index / crosswalk | `BOUNDED_STANDARD` | High when semantic routing requires interpretation |
| sequential deep reading | `SUBSTANTIVE_ANALYSIS` | Extra High for unusually dense/ambiguous installments |
| cumulative ledger update | `SUBSTANTIVE_ANALYSIS` | Extra High when reclassifying prior states |
| checkpoint synthesis | `DEEP_SYNTHESIS` | Pro only when it defines a highly propagation-sensitive freeze |
| claim-revision ledger | `DEEP_SYNTHESIS` | Pro for corpus-wide/load-bearing retrospective rerouting |
| character monograph | `DEEP_SYNTHESIS` | High if narrow; Pro only for unusually difficult central cases |
| relationship specialist | `DEEP_SYNTHESIS` | High if bounded and evidence is stable |
| thematic/institutional specialist | `DEEP_SYNTHESIS` | High when local; Pro only for load-bearing conflict resolution |
| continuous full-series synthesis | `PREMIUM_QUALITY_FIRST` | especially when written after many specialist documents |
| reconstruction model | `DEEP_SYNTHESIS` | may be High for domain-limited characters |
| prospective prediction/adjudication | `DEEP_SYNTHESIS` | Pro for final experiment-level integration if warranted |
| adversarial contradiction audit | `PREMIUM_QUALITY_FIRST` | strong Pro candidate because failure detection is the purpose |
| cross-model consistency audit | `PREMIUM_QUALITY_FIRST` | strong Pro candidate when many models interact |
| release/admin audit | `SUBSTANTIVE_ANALYSIS` | lower if purely mechanical |

---

# 14. Sequential-reading special rule

A mature sequential-reading method often benefits more from **consistency across installments** than from changing models every volume or episode.

For an active sequential run:

- preserve the established reasoning class while the method and source complexity remain stable;
- escalate a specific installment when it introduces unusually dense ambiguity, formal complexity, source defects, or major retrospective contradictions;
- do not silently downgrade a sequence merely to save credits when Medium/High/Extra High have the same applicable per-message cost;
- record a material tier change in the series current-state map when it changes the project method or validation comparability.

---

# 15. Full-series and reconstruction special rule

Full-series synthesis and character reconstruction are distinct responsibilities.

A literary monograph may deserve `DEEP_SYNTHESIS` or `PREMIUM_QUALITY_FIRST` because it integrates motive, development, symbolism, language, relationships, and thematic function.

A reconstruction model may require a different tier because its task is narrower: time-indexed behavior, speech, relationship-conditioning, ordinary-life repertoire, negative constraints, and prediction validity.

Do not assign Pro to both automatically. Choose based on each artifact's error topology.

Likewise, a high-tier reconstruction model never outranks the primary source, sequential reading, specialist synthesis, or evidence ledger from which it is derived.

---

# 16. When not to increase reasoning

Higher reasoning is not always better.

Do not escalate merely because:

- the agent has remaining context;
- the artifact is long;
- the series is prestigious or personally important;
- a previous unrelated project used Pro;
- the task feels difficult but has no clear evaluation criterion;
- the prompt is underspecified or contradictory.

First repair the task definition, source boundary, authority routing, or stopping condition. More reasoning applied to a malformed task can produce more elaborate error rather than better analysis.

---

# 17. Empirical calibration

When a new model family or reasoning feature appears, use representative project tasks to calibrate the mapping.

Good calibration probes include:

- one mature sequential deep reading with known quality criteria;
- one claim-revision sample with several genuine transitions;
- one difficult character-state reconstruction problem;
- one adversarial contradiction audit;
- one bounded evidence/index task.

Compare:

- factual/source accuracy;
- preservation of epistemic boundaries;
- contradiction detection;
- evidence traceability;
- unwanted overinterpretation;
- cross-document consistency;
- latency and credit cost.

Do not use prose elegance alone as the evaluation criterion.

---

# 18. Relationship to memory and chat context

This file, not conversational memory, is the canonical durable home for reasoning/model-routing policy.

Memory may help an agent remember that the policy exists, but it should not be relied upon for current tier names, pricing, or product semantics. Those facts are volatile and should be resolved through this policy's current mapping plus fresh official documentation when a re-check trigger fires.

The master routing index should point to this file so that future chats can recover it deterministically.

---

# 19. Existing artifacts and backfill

This policy is prospective by default.

Do not mass-edit frozen or mature historical artifacts solely to add routing metadata. Backfill reasoning metadata only when:

- a series is already undergoing a legitimate architecture revision;
- the routing information materially helps future execution;
- or the user explicitly requests a corpus-wide migration.

Existing series-specific reasoning recommendations remain valid where they are more specific, but future architecture updates should migrate toward stable reasoning classes plus a literal model-at-design-time field.

---

# 20. Maintenance requirements

Whenever this policy's current provider mapping changes materially:

1. consult current official OpenAI documentation and release notes;
2. revise this file **in place** rather than creating near-duplicate policy files;
3. increment the policy version;
4. update `current_chatgpt_mapping_verified` and, where applicable, `current_pricing_verified`;
5. preserve the stable reasoning-class definitions unless the analytical taxonomy itself needs revision;
6. add a changelog entry explaining the old and new mapping;
7. update `MANGA_ANIME_DRIVE_INDEX.md` when the change affects routing;
8. preserve old series artifacts and frozen releases unless another architecture rule requires migration.

---

# 21. Operational checklist before generating a new artifact

Before substantive generation:

1. resolve the canonical series root and current entrypoint;
2. read the governing series architecture/method;
3. determine whether that architecture assigns a stable reasoning class or literal tier;
4. if not, classify the operation using this policy;
5. check whether a model-release/documentation freshness trigger has fired;
6. if it has, consult current official OpenAI documentation before resolving the literal model option;
7. if Pro is proposed, state the marginal-quality justification;
8. write routing metadata into the artifact front matter when practical;
9. generate the artifact;
10. update corpus maps/manifests/indexes only when project state materially changes.

---

# 22. Current summary rule

As of 2026-08-27, for ChatGPT-based project work:

> **Instant for routine deterministic work; Medium for bounded structured reasoning; High for normal substantive analysis; Extra High for difficult multi-source synthesis; Pro only for difficult quality-first work where additional model work is plausibly worth a five-times-higher per-message credit cost.**

And for future models:

> **Preserve the stable workload class, re-check official OpenAI documentation and announcements at model/feature release boundaries, then update the current mapping rather than rewriting the intellectual architecture of the corpus.**

---

# Changelog

## v1.0 — 2026-08-27 — Corpus-wide reasoning/model routing policy established

- Established five stable project reasoning classes: `ROUTINE_FAST`, `BOUNDED_STANDARD`, `SUBSTANTIVE_ANALYSIS`, `DEEP_SYNTHESIS`, and `PREMIUM_QUALITY_FIRST`.
- Mapped the classes to the current ChatGPT GPT-5.6 Sol/Pro reasoning options after checking current official OpenAI documentation.
- Established explicit Pro value, downgrade, and escalation rules.
- Established model-release/documentation-freshness triggers and a provider-migration procedure.
- Distinguished ChatGPT UI tiers from API reasoning effort and Pro-mode controls.
- Established prospective front-matter guidance for future project artifacts.
- Designated this file, rather than memory, as the canonical durable home for corpus-wide reasoning/model routing.
