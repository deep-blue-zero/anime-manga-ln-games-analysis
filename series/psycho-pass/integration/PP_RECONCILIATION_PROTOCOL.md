---
title: "Psycho-Pass — Independent AV and franchise reconciliation"
artifact_id: PP_RECONCILIATION_PROTOCOL
artifact_type: project_reconciliation_protocol
series: psycho-pass
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "NONE; metadata-only foundation, no admitted narrative"
canonical_home: series/psycho-pass/integration/PP_RECONCILIATION_PROTOCOL.md
created: 2026-11-18
last_updated: 2026-11-18
---

# Independent AV and franchise reconciliation

This is the operational contract for the adopted `PP_AV_PRIMARY_CHARACTER_AND_FORM` method family and for local-to-franchise integration. It implements the [AV reconciliation protocol](../../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md), [topology §4.1](../../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md#multi-agent-source-reading), [bundle specification](../../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md) and [handoff contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md). It introduces no global exception. **No role has performed narrative analysis or verified a model capability during bootstrap.**

## First-start role and capability receipt

Before an authorized first unit, record the owner grant, run start/end, single-operation or explicitly bounded continuation mode, stop conditions, topology, role assignments and source/knowledge boundaries. The [continuation policy](../../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) controls run extent. A plan is not permission to continue through the franchise.

The principal inspects the complete required unit and owns draft synthesis. An independent source-language/argument specialist checks decisive Japanese wording, assertions, reasoning and institutional claims against the source. An independent AV/character specialist examines assigned performance/form evidence and meaningful behavioral alternatives. Assign at least one genuinely substantive independent specialist for every unit, selecting or combining those specialist responsibilities only when competence and coverage support it. The separate critical reviewer inspects decisive evidence and tests major claims, omitted scenes/persons, contrary cases and transition errors. The analytical integrator owns shared ledgers and acceptance; record if this is also the principal. No reduced source-reading configuration is preapproved for these extended episodes.

The owner prefers Gemini 4 Carbon High as principal continuous-AV analyst and independently operating OpenAI and/or Anthropic contexts for specialist/reviewer work. Resolve those roles to actually available capable runtimes. Record exact provider/model/surface, reasoning configuration where exposed, input support, image/video sampling information, direct-listening support, duration/context/transport constraints and successful source-access checks. Distinguish verified capability, provider documentation, owner preference and unverified expectation. Do not execute benchmarks or probes merely because this foundation names them.

Independent contexts receive the bounded sources and neutral assignment, not the principal's interpretation. Freeze their observations before claims exposure where feasible. Record actual prior exposure and `blind_order_achieved`; set false when the order or independence is compromised. Source-aware critical review still has value after exposure but cannot be reported as blind. If required roles or channels cannot be satisfied, pause acceptance at the last valid checkpoint rather than replacing independent source work with approval of prose.

## Evidence package and clocks

A complete episode bundle must satisfy all semantic responsibilities of the current specification: source identity and provenance, source-relative citation clock, visual evidence/index, dialogue/source-language route, linkage among evidence objects, audio access, coverage/quality assurance and retrievable artifact inventory. A source MKV plus unmatched subtitles is not a complete bundle. A partially prepared bundle is labelled partial with its missing responsibilities and blocked claims.

Bind every transported media/clip/derivative to the original witness hash, exact source interval, stream choice and transformation manifest. Record source-relative time and derivative-relative time separately, including offsets, cropping, resampling, encoding and audio handling. Keep originals, extracted frames/audio/subtitles and private manifests in authorized source/work environments. Public analytical Git contains safe metadata, derived analysis and necessary bounded quotations, without machine paths, account IDs or restricted media.

For New Edit source time, use `HH:MM:SS.mmm` relative to the recorded media origin, not player wall time or a TV subtitle clock. Calibrate with at least opening, middle and closing audiovisual anchors for full-episode inspection. For clips, verify endpoints and an interior anchor, preserving the source offset and adequate context. Record measured subtitle/audio alignment and residual error. Default ordinary navigation tolerance is ±0.5 seconds only when demonstrated by calibration; rapid action, turn timing, lip synchronization or sound-image order may demand frame/sample-level checks.

The available TV subtitle clocks exceed the candidate BD durations. Treat their timing as unaligned evidence, with possible cut/ad/edition differences. No assumed constant offset or original-broadcast pair mapping is permitted. BD-labelled ASS01/02 also require verification. Text synchronization, text accuracy and language identification are separate acceptance questions. E04 needs an adequate authorized Japanese evidence route before its required text claims can be complete; E11 spoken language requires actual verification because its track is untagged.

An ffprobe report establishes container metadata, not decoding completeness or model perception. A 23.976fps source does not prove that an inspecting model saw 23.976 frames per second. Record known sampling and unknown sampling explicitly. The files are approximately 1.7–2.6 GB; check actual runtime transport limits, not historical tool limits quoted in policy. Prepare the smallest faithful derivative appropriate to the evidence need, preserving relevant timing, visual detail and audio. If compression or sampling could remove the decisive feature, escalate source inspection and narrow the conclusion until adequate.

## AV-primary mirror workflow

1. Select the unit's actual AV responsibility under the [method](../framework/PP_ANALYTICAL_METHOD.md#governing-method-and-adopted-av-companion). Document why whole-episode continuity, targeted clips or `VIDEO_NOT_REQUIRED` matches it. Verify source/bundle identity and freeze entering hypotheses.
2. Issue a neutral observation packet with exact source IDs, bounded intervals, context, calibration task and uncertainties. It contains no preferred reading or desired adjudication. The principal's AV-first interpretation is a proposed analysis, not current authority merely because it is primary.
3. Freeze independent observations and source-language findings before supplying the claims packet where feasible. Preserve observation IDs, actual inspected scope and exposure record. If an analyst cannot directly listen/view, its output cannot be labelled a direct sound/motion observation.
4. Reinspect every load-bearing AV observation at its claimed source coordinates. Initial recalled timestamps are `REPORTED`. An observation becomes `ANCHORED` only when it is calibrated to a source interval and cue/frame, actually re-viewed or reheard, resolvable within the inspecting route's effective sampling and temporal precision, and supported by the corroboration required for that claim. Record inspector, anchors, resolution and confirmation evidence. Relocating a timestamp alone does not pass. Verify decisive quotations/terminology through the independent Japanese route. Listening-based transcription retains audio-observation or human-listening status and uncertainty until a distinct verified text witness supports TXT; hearing speech is not itself TXT verification. Bundle anchors and AV observations constrain each other.
5. The critical reviewer tests the principal and specialist interpretations against decisive source spans, best counterexamples and meaningful alternatives. Distinguish new findings from adjudications of earlier claims. State what source evidence actually discriminates between explanations.
6. For a material disagreement, return once for bounded clarification/reinspection, then obtain one independent verification pass where needed. If unresolved, retain `OPEN`, competing readings and the precise missing discriminator. Required unresolved facts or missing channels block the affected acceptance. Avoid indefinite review loops or automatic replacement on disagreement alone.
7. The integrator chooses `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN` for each material claim, with source-grounded reasons and dependencies. Confidence follows evidence and limitations. No model's status or majority agreement is a tie-breaker.

A later transcript/bundle challenge to an AV-primary interpretation is part of this mirror process. Exact wording can correct an AV paraphrase; direct motion/listening can correct an inference from a static or textual view. Neither channel automatically settles every question.

## Episode transaction and franchise proposals

A valid episode checkpoint contains the complete reading with beginning synopsis, source/coverage receipt, local observations and states, claim/disclosure changes, independent assignments and actual findings, reviewer objections/counterexamples, dispositions, pending evidence gaps and qualification/dependency review. Preserve substantive findings in the checkpoint or exact durable linked artifact; a line saying “specialist agreed” is inadequate.

The integrator atomically accepts that transaction before any high-water advance. An interrupted run preserves drafts as incomplete, recovers the last accepted boundary and does not infer completion from filenames. Required corrections are applied or acceptance remains pending. Optional unresolved interpretations state their bounded effect and trigger.

At a declared tranche/installment boundary, the local analyst submits `PP-DELTA-####` proposals identifying:
- new findings and changed character, directed relationship or institution/world state;
- revised/challenged interpretations and strongest counterevidence;
- chronology, continuity, edition or disclosure disagreements;
- evidence gaps, unresolved questions and proposed specialist/portrait obligations;
- exact affected master records, base versions, proposed before/after text and dependencies.

The integrator checks freshness and source lineage, accepts, qualifies, rejects or leaves open each proposal, and edits only affected authoritative records. Link the outcome to the applicable claim-transition vocabulary. A qualified acceptance narrows the conclusion explicitly. Stale bases require reconciliation before mutation. Record the master's actual reconciled boundary and pending deltas until materialization completes. Keep local observations and historical horizon conclusions in their original home.

## Freezes, handoff and completion

Accepted source-facing readings, pre-unit freezes and independent observation/review logs freeze at their declared checkpoint. Current ledgers, maps and designated living portraits change only through attributed, reviewable revisions. A correction to a frozen reading is a linked erratum or superseding artifact under the [archive policy](../../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md), preserving the original bytes and source horizon. Never silently rewrite a prospective record to resemble hindsight.

A fresh synthesis handoff includes the actual accepted reading/evidence/ledger bytes and hashes, immutable source identities and access routes, exact corpus/knowledge cutoff, base versions, entrypoint, active claims and significant contrary cases, independent findings/dispositions, required versus optional gaps, current portrait obligations and mutable ownership. Supply enough analytical substance to rebuild the argument, not only hyperlinks or a terse summary. The receiving agent acknowledges what it actually retrieved and inspected; missing evidence limits its authority.

Fresh synthesis returns provenance-bearing proposed changes and new work. The local integrator verifies source boundaries, significant claims, counterevidence and dependency propagation before accepting it. Completed prose does not itself establish required AV/text coverage, portrait fidelity, or reconstruction readiness. Final synthesis cannot be complete while required channels, material factual disputes or qualified portrait obligations remain unresolved. Optional enrichment may remain open with explicit consequences.

Named-subject handoff verification follows the handoff contract's §15: preserve stable identity, source-language names, purposeful roles and knowledge-bounded aliases; verify that material named people remain retrievable in the transferred synopsis, evidence and analysis. Inspect introduction, middle and latest/exit material where present, major relationships and any consequential minority/secondary contribution. Record what was checked and repair unexplained generic-label substitution or loss of a person's causal role before accepting the affected handoff.

At bootstrap all of these execution records are absent because no run is authorized. The sole next sequential operation remains `NONE_AWAITING_RUN_AUTHORIZATION`.
