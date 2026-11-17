---
title: "Onna Tomodachi wa Tanomeba Igai to Yarasete Kureru — Synthesis Architecture"
artifact_id: ONNA_TOMODACHI_SYNTHESIS_ARCHITECTURE
artifact_type: synthesis_architecture
series: onna-tomodachi
version: "1.0"
status: canonical
authority_generation: ONNA_TOMODACHI-INITIAL
authority_scope: "Independent witness, disclosure, claim and character state for the original novel and the manga adaptation"
source_boundary: "NONE admitted; foundation metadata only"
created: 2026-11-15
last_updated: 2026-11-15
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Onna Tomodachi wa Tanomeba Igai to Yarasete Kureru — Synthesis Architecture

## Purpose and lane topology

[Current State and Corpus Map](CURRENT_STATE_AND_CORPUS_MAP.md) is the single entrypoint. This INITIAL design applies the [source register](ONNA_TOMODACHI_SOURCE_REGISTER.md) and [method](ONNA_TOMODACHI_ANALYTICAL_METHOD.md) to the original Japanese published prose and the Japanese manga adaptation. It asks how each work gives readers access to characters’ friendship, expectations and agency. Claims about novel focalization and original continuity take their authority from Japanese novel witnesses. Claims about the manga’s visibility, omissions or additions take authority from its own witness. Neither a coincident volume number nor familiarity with one lane establishes the content or interpretation of the other.

| Responsibility | Capture as read | Canonical or future home |
| --- | --- | --- |
| Novel relationships and knowledge | Attributed line or thought, focalizer, direct action, response, actual event and disclosure timing, rivals and evidence of change | Initialized [light-novel ledger](ONNA_TOMODACHI_LIGHT_NOVEL_LEDGER.md), supporting a prose reading of relational assumptions and reported intentions |
| Manga relationships and visibility | Panel sequence, who can see an exchange and interpret it, material address or gesture, the effect of visual timing, rival explanations | Initialized [manga ledger](ONNA_TOMODACHI_MANGA_LEDGER.md), supporting a manga-specific account of staged responses and reciprocity |
| Form and continuity within a work | Prose spine location, illustration class and placement, or image positions/reading order and page region, with self-report distinguished from evidence | Governing volume reading and the appropriate work ledger for load-bearing recurrence |
| Character qualification and revision | Ordinary behavior, boundaries, context-specific choices or communication, personal history, contrary cases, change/disclosure distinction | Appropriate lane ledger and lane-bounded subject, claims and acceptance |
| Comparison across works | Separately verified anchor in each lane and material convergence, change or unresolved mismatch | Deferred aligned study; evidence and claim homes stay within each lane |

Two initialized cumulative homes are necessary because language form, evidence unit, continuity and eligibility can differ. Each carries evidence, longitudinal state and claim history together. Alignment needs admitted evidence from both sides and has no day-one artifact. A future study only compares eligible, mapped material at explicit version boundaries, with claims about what an adaptation changes confined to demonstrated differences. Marginal local observations remain in their source-facing readings.

## Standing independent source readers

In either lane the principal and integrator opens the actual source, directly inspects the entire authorized unit, owns its single reading and reconciles the transaction. For an original light novel, assign an independently working source-aware specialist to Japanese viewpoint, speech and differences between narration’s interpretation and evidenced character decisions. For manga, assign independent specialist work to visual framing, layout, dialogue placement, reader access and directed reaction. For especially dense units add separate specialist coverage of individual behavior, ordinary-life details or the tension between accounts of an exchange. A distinct critical reviewer directly examines diagnostic evidence, preferably before the interpretation, and checks exact wording or visual attribution, chronology, choice and response, epistemic boundaries, counterexamples and omissions. No routine reduced category is designated.

Each context receives the assigned frontier and source access. Independent interpretations originate before the principal draft is shared. State actual spoiler exposure across lanes, supplements and later units. A compromised contribution loses prospective or independent credit within the affected bounds and keeps its provenance. The principal records respective assignments, inspected source, actual context separation, evidence and rivals, corrections, obligations and dispositions in `checkpoints/ONNA_TOMODACHI_LN_Vnn_CHECKPOINT.md` or `checkpoints/ONNA_TOMODACHI_MANGA_Vnn_CHECKPOINT.md`. Update only the corresponding cumulative home in the atomic transaction. Genuine independent access and the required original-witness medium are capability preconditions for acceptance and high-water advancement. Use [topology §4.1](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md#multi-agent-source-reading).

## Unit, synthesis and revision

Write the accepted artifacts only on admission under `readings/ONNA_TOMODACHI_LN_Vnn_DEEP_READING.md` or `readings/ONNA_TOMODACHI_MANGA_Vnn_DEEP_READING.md`. Each supplies coverage, preserved entering and exit freezes, a near-front human-facing synopsis finalized after prospective capture, a causal and formal account, competing evidence, ledger manifest and durable review. The reading owns source observations; ledgers route by stable lane-tagged IDs to paragraphs, pages and panels. A later conflict may arise from asymmetric awareness, reporting, sequencing, different witnesses or genuine divergence. Compare exact evidence, label each continuity, and retain uncertain rival explanations. Revise materially changed claims in the corresponding ledger using `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`. Preserve earlier knowledge boundaries and prospective evidence. Use a linked erratum or superseding analysis for changes to frozen judgment. Keep the current map, source register and ledger views mutable under [archive authority rules](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md).

Reconcile each lane’s accepted coverage, source horizons, continuity, current claims and independent acceptance before assessing synthesis readiness. A prospective specialist account of the novel’s focalization and pragmatic language can feed its own relationship analysis. The manga’s portrayal of agency can use an equivalent question with its own visual and dialogic diagnostics. Anticipate a two-lane comparison only after relevant independent syntheses exist and both scopes permit it, with a scene-aligned paired register when recurrence justifies it. Preserve omissions, reordering, understaging, uncertain parallels and evidence-dependent differences. Distinguish source-run completion, reconciled longitudinal state, readiness for character and specialist work, integrated synthesis readiness, independent semantic review and approved freeze or release. Apply the role-gap review and record incomplete responsibilities before any broader conclusion. Amend this design and entrypoint only when a demonstrated recurring evidence or retrieval requirement needs a new home.

Use each lane ledger for eligibility decisions no later than its specialist-synthesis readiness gate and revisit them after material changes. Consider any adequately evidenced person with convergent observations, meaningful contextual variation and limits or counterexamples, regardless of role. The stable subject record carries identity, work, temporal boundary, rationale and gaps, reassessment trigger and accepted portrait link. Use `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE` and `REASSESS_AFTER_REVISION`. Qualification creates an outstanding production obligation, reported until accepted. A different continuity can support a different portrait; author one self-contained portrait per qualifying subject and scope in `characters/<subject>-light-novel.md` or `characters/<subject>-manga.md`. Verify all coverage obligations under [initiation §5.5.1](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard). Mark untested dimensions unknown and keep sensitive relationship analysis bounded to what is supported. Record portrait-only self-containment and source fidelity separately, with the named-subject referential check. Track outstanding obligations in the readiness/release audit. Reconstruction and validation use separate authorization and responsibility.

Use BOUNDED_STANDARD for metadata, ROUTINE_FAST for deterministic checks, SUBSTANTIVE_ANALYSIS for authorized units, DEEP_SYNTHESIS for lane-bounded specialists and portraits and PREMIUM_QUALITY_FIRST for two-lane architecture, material interface conflicts and integrated comparison. Prefer direct local prose/page inspection and coordinated transactions, with fresh evidence-bounded contexts for substantial synthesis and designated repository integration. The [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) and [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) govern separate source and temporal packet boundaries, acceptance and reopened corrections.
