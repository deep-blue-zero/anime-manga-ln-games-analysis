---
title: "NTR — Analytical Method"
artifact_id: NTR_ANALYTICAL_METHOD
artifact_type: analytical_method
series: "NTR: Netsuzou Trap / 捏造トラップ-NTR-"
generation: NTR_BOOTSTRAP_V1
status: active_provisional
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-28"
source_boundary: "Prospective Japanese manga V01–V06 method; no narrative material inspected"
canonical_home: series/ntr-netsuzou-trap/00 Frameworks and Methods/NTR_ANALYTICAL_METHOD.md
recommended_reasoning_class: SUBSTANTIVE_ANALYSIS
---

# NTR — analytical method

This provisional method defines *how* a future Japanese manga volume is read. The [architecture](NTR_SYNTHESIS_ARCHITECTURE.md) defines where its findings go; the [source map](NTR_SOURCE_AND_SCOPE_MAP.md) defines the witnesses. `SEQUENTIAL_ANALYSIS_LOCK = CLOSED` in the [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) until the owner audits and explicitly unlocks it. No examples below assert events in the manga.

## Source and prospective boundary

Use the exact Japanese VNN Drive EPUB identified by source key; compare metadata, identity, and available integrity checks before admission. Record the limits of any missing remote checksum. Establish chapter, spine/image/page, panel/balloon, cover/insert/extra boundaries from the admitted witness before citing narrative details. Do not ingest the primary images into Git. An optional deterministic locator sidecar belongs in Drive and is referenced by hash/ID from Git.

Read V01 → V02 → V03 → V04 → V05 → V06. At each volume opening, freeze what was knowable from already closed volumes, including working hypotheses and predictions; do not import later reveals, creator remarks, adaptations, or user/analyst fandom knowledge. At close, freeze the new state and record claims as `OBSERVED`, `INFERRED`, `OPEN`, or `SPECULATIVE`, with source locators, counterevidence, and confidence. Later material changes a current claim by a dated revision link; it never rewrites what the earlier reader could have known.

## Scene and evidence capture

For each consequential scene or chapter, record the depicted action and dialogue in concise paraphrase, Japanese wording only when a specific lexical/register point depends on it, exact locator, actor/speaker, audience, temporal order, information distribution, and the visual basis of an inference. Distinguish source observation, character report, character belief, narrator framing, and analyst judgment. A character's claim about another's motives is evidence of the *claim* before it is evidence of the motives. Preserve plausible counterreadings; mark omissions or uncertain image order rather than guessing. Use only minimal source quotation needed for analysis.

### Desire, agency, and permission

Code independently: attraction, physiological arousal if depicted, romantic attachment, sexual desire, consent, acquiescence, initiation, reciprocation, refusal, hesitation, resistance, withdrawal, non-response/freeze where evidenced, boundary crossing, manipulation, coercion, threat/leverage, later pursuit, retrospective interpretation, and later relationship choice. A single scene may support several different variables without making them equivalent.

**Later desire or love does not establish earlier consent. Physiological response does not establish consent.** Evaluate permission at the time of the action using what was communicated, the available alternatives, boundaries, pressure, power, deception, and response. Later testimony may clarify an earlier subjective state, but preserve the earlier ethical assessment and its evidentiary basis as a distinct question. Do not homogenize every uncomfortable interaction, or balance distinct conduct into a generic judgment about a whole pair. Keep affective truth, intention, harm, responsibility, and ethical permission separate.

For infidelity, establish the represented public label, private mutual understanding, explicit or narratively supported exclusivity expectations, outside intimacy, concealment and disclosure, and who was owed what information. Do not invent a formal monogamy contract; do not ignore a shared expectation merely because it was informal. Distinguish descriptive relationship states from ethical evaluation.

### Information, action, form, and language

Maintain directional A→B and B→A relationship observations independently. Record who knows, suspects, falsely believes, hides, discloses, or believes another knows a consequential proposition; track higher-order beliefs only when action depends on them. Before treating inaction as a decision, identify actual options and constraints. Time-index any recurring pursuit/withdrawal cycle and compare the changed entering state.

Treat manga as visual narrative. Capture diagnostic gaze, orientation, distance, initiation/response to touch, reaction shots, withheld faces, panel isolation, page-turn reveals, public/private staging, and repeated compositions. Distinguish **depicted fact**, **formal mechanism**, and **psychological inference**. Test whether recurrence and escalation form a coherent melodramatic grammar rather than presuming that apparent coincidence is either an error or a design. For intimate scenes, retain only analytically necessary description; no reproduced images or gratuitous detail.

Japanese lettering supports written speech, address, honorific, politeness, lexical, and sentence-ending comparisons. Track features that recur, change with conditions, differentiate subjects, or affect reconstruction, with exact locators and cautious translation notes. Manga lettering cannot establish acoustic timbre, pitch, breath, or voice-actor delivery; anime speech is separate adaptation evidence.

## Completed VNN transaction

One authorized operation closes **one** volume unless the owner explicitly authorizes a bounded continuous run. Complete all of the following before advancing the high-water mark:

1. Verify and admit only the exact VNN witness; fix its locator convention and entering prospective state.
2. Inspect the complete admitted volume, including identifying and separately routing any paratext or extras; create `NTR_VNN_DEEP_READING.md` in a sequential-reading home only once evidence exists. For V02+, include a concise synopsis and developments **from the previous volume** as understood at the entering boundary; distinguish a later retrospective correction.
3. Record chronology and state changes, evidence, counterreadings, unresolved gaps, ethical distinctions, visual/language observations, and a prospective endpoint. Update only materially affected longitudinal homes; zero new rows in a ledger is permissible when justified.
4. Add/revise claims and adjudicate earlier predictions with `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`. Check subject/model readiness without fabricating a cast or grade.
5. Update the source state, entrypoint, and frozen volume boundary; validate and commit the complete transaction. Name the next candidate operation as routing only. Do not silently start the next volume.

If an extraction, locator, or completeness problem blocks reliable reading, retain an explicit partial state rather than marking `INSPECTED` or `CLOSED`. If a later source materially revises an earlier reading, add a retrospective revision or audit linked to the frozen artifact; preserve the historical prospective record. The source map's supplement quarantine remains in force through V06 mainline freeze.
