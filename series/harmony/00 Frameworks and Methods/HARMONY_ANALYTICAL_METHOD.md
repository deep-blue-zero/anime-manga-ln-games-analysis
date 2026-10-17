---
title: Harmony / ハーモニー — Prospective prose-reading method
artifact_id: HARMONY_METHOD
artifact_type: analytical_method
series: Harmony / ハーモニー
series_id: harmony
generation: HARMONY_BOOTSTRAP_V1
version: '0.18'
status: active_provisional
scope: Prospective prose-reading method
source_boundary: HAR-JP-EPUB-001 d583f6dc36612eb1aec9b18c4ae5a61460388591ee00f38abc2bbd69071fbbae; HAR-U017 complete Part IV numbered02 at spine31 text/part0012_split_002.html; exclusive before spine32 text/part0012_split_003.html; later narrative body unopened
canonical_home: series/harmony/00 Frameworks and Methods/HARMONY_ANALYTICAL_METHOD.md
created: '2026-10-16'
review_status: SCOPED_FOUNDATION_ACCEPTED_2026_10_16
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Harmony / ハーモニー — analytical method

This reviewed method governs source-bounded Japanese-prose operations under the exact owner-authorized run recorded in the entrypoint. It makes no plot, character or thematic claim. Read [the entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md), the [witness map](../00%20Frameworks%20and%20Methods/HARMONY_SOURCE_AND_SCOPE_MAP.md) and paired [architecture](../00%20Frameworks%20and%20Methods/HARMONY_SYNTHESIS_ARCHITECTURE.md) first. The current lock, exact authorized run and admitted frontier are read from that entrypoint; bootstrap was CLOSED with zero narrative findings.

## 1. Witness admission and source handling

Verify the precise candidate, archive hash, Japanese language/edition lineage, resource integrity and usable representation. Preserve the original bytes. Record what was actually retrieved, mechanically processed, rendered and semantically inspected as separate facts. Pin renderer/extractor versions and transformations when they are used. No source payload, wholesale transcript or substantial quotation goes into public Git; compact keys and locators route back to Drive.

Keep Japanese wording as the intended authority once verified. Never translate an ambiguous expression into a stronger factual claim. Any English wording is explicitly the analyst's translation or an identified translation witness; retain the Japanese term and diagnostic short excerpt where necessary, alternatives, and uncertainty. A translation may expose a question but cannot silently override the Japanese witness. Preserve ruby, punctuation, quotation level, orthography and typographic emphasis; flag ambiguous glyphs instead of guessing.

## 2. Locator grammar for the actual EPUB candidate

The candidate has `content.opf`, an ordered spine, named XHTML members and some element IDs. The durable locator is:

`HAR-JP-EPUB-001@sha256:<full digest>::spine:<one-based occurrence>::member:<exact archive path>::node:<XML element path>::chars:<start>-<end>`

`spine` counts all OPF occurrences, including cover/ancillary items; it is not a printed page. `member` is archive-root-relative, case-sensitive and percent-decoded only as the package requires. `node` is a one-based, namespace-aware element path with its namespace map preserved; an existing unique element ID may supplement it. An absent ID is never fabricated. `chars` is a zero-based, half-open Unicode-codepoint range over that node's decoded text/tail nodes in document order, with no Unicode/whitespace normalization; ruby readings remain separate from base text in the presentation, while the raw node path resolves the original. Record a hash of the exact selected source text as a disambiguator, without publishing extensive text.

Locator implementation `HAR-LOC-1` is fixed before the first evidence allocation. Paths use `/h:html[1]/h:body[1]/h:div[1]/h:p[1]` syntax, with `h = http://www.w3.org/1999/xhtml`; each one-based index counts siblings of the same expanded QName. A namespace map accompanies any additional prefix. Resolve XML without recovery, external entities, or network retrieval. XML entity decoding and XML-mandated line-ending decoding occur at parse time; no subsequent text or Unicode normalization occurs. The character stream is the selected element’s XML string-value: its own text, descendant text and descendant tails in document order, excluding the selected element’s own tail. Raw offsets therefore include `rt`/`rp` text where present; a separate presentation record retains ruby base/reading associations. `br` is an element event, not an invented character in this raw stream. Selected-span digests are SHA-256 over its exact UTF-8 encoding. These choices clarify the existing grammar without changing any previously allocated locator: none existed before this pilot.

For typography or markup claims, also cite the original member and a faithful render location; text offsets alone do not preserve layout. Member byte offsets or a verified CFI can supplement this grammar only after explicit round-trip verification. If parser output changes, preserve the old mapping and issue a new derivative/locator version. Never assign print pages from renderer screens, Kindle-style locations, file counts or catalog page totals. A later print/PDF witness gets its own edition key and independently verified page map.

An evidence record must resolve from artifact claim -> evidence ID -> source key and digest -> exact member/node/span. Test at least one opening locator and every quotation or load-bearing ambiguous locator by retrieval before accepting it. If a locator is broken, the affected claim remains unsupported until repaired through attribution-preserving revision.

## 3. Natural units and prospective frontiers

Use the source map's observed parts/subsections as segmentation candidates. Verify real heading boundaries, intervening framing and complete ordered content before fixing the transaction. Prefer a numbered subsection when it has a coherent boundary; use a bounded chapter/section group only with a literary reason and explicit authorization. An EPUB file split or token budget is never a literary unit. Internal processing chunks do not advance the high-water mark and may not hide omitted text.

For the first transaction, include the opening narrative framing rather than starting mechanically at the first TOC item. Subsequent units begin immediately after the last closed boundary. Keep a coverage list of every admitted member/span, including gaps, discontinuities and whether opening/epilogue material belongs to the unit. Do not inspect later narrative to settle an earlier interpretation. Structural navigation is inventory; its labels must not be mined as evidence for an earlier scene.

At entry and exit, distinguish (a) narrator assertion, (b) focal character knowledge at the scene time, (c) another character's report and access, (d) what the reader can establish through the unit, and (e) the analyst's inference. Narrated time and disclosure order are separate coordinates. Memory, reported speech, quotation-within-quotation and retrospective narration retain their source and reliability limits. Later revelation may revise the current account without entering an earlier frozen reading.

## 4. Evidence, inference and tests

Assign stable unit IDs `HAR-U001` onward only when a real unit is admitted; these are analytical ordinals, not invented chapter numbers. Within a unit, assign `HAR-U001-E001` onward to observations in its evidence table. Subject IDs use `HAR-C001`; directional relations use `HAR-R001`; knowledge/institution records use `HAR-K001`; claims use `HAR-CL001`, predictions `HAR-PR001`, revisions `HAR-RV001`. These are grammars only: **no such records exist at bootstrap**. IDs are never reassigned after a freeze.

Each material claim identifies its evidence IDs, witness/locator, scene and disclosure boundary, speaker/thinker/recipient, certainty and type: `OBSERVATION_OR_QUOTATION`, `SUPPORTED_INFERENCE`, `COMPETING_INTERPRETATION`, `SPECULATION`, or `VALUE_JUDGMENT`. Record what a passage actually says before arguing what it implies. Narrative assertion, corroborated fictional mechanism and real-world scientific validity remain separate.

For psychologically, politically, linguistically or morally consequential claims, record the strongest plausible competing explanation, counterevidence, evidence that would discriminate, and what remains unknowable. Do not manufacture false balance when an alternative lacks textual support. Predictions are timestamped to the admitted boundary before the outcome is opened; retrospective fit is labeled as such. Separate character belief, narrator stance, institutional doctrine and a defensible account of the novel's argument.

## 5. What each unit preserves

Capture changes in goals, constraints, perception, attention, self-presentation, private-belief access, decision policies, affect, coping, bodily conditions and speech/register where supported. Track directional influence, trust, dependence, obligation, consent and commitments without assuming reciprocity. Separate an actor's claim about an institution from a demonstrated rule, practical enforcement and actual organizational capacity.

Consider agency, personhood, coercion/consent, surveillance, moral responsibility, collective welfare, violence and biotechnology when the text warrants them. Explanation does not itself justify an act; agency does not erase constraints; an evaluative judgment requires its premises. Do not impose a predetermined thesis, a single moral label or a default PACTRIH score. Philosophical overlays require separate authorization and remain subordinate to source evidence.

### Novel-specific form controls: Harmony

Hayakawa explicitly identifies HTML-like notation as intentional textual form. Preserve tags, tag-like strings, angle-bracket variants, case, punctuation, nesting, indentation, ruby, typography, framing changes and interface-like constructions. Do not strip markup, apply Unicode normalization, repair syntax, standardize quotation marks or silently flatten the source. Distinguish **visible literary notation** from XHTML used to encode it; escape literal notation in Markdown so a renderer cannot hide it.

At admission, keep the original EPUB unchanged; compare a faithful render, underlying source markup and a bounded extraction for the authorized opening. Record render/extraction tool and version, hash, transformations and lost or uncertain features. Preserve ruby bases/readings separately, gaiji/image substitutions and CSS-dependent reading order. A reading may use an extraction only after its relevant features round-trip to the original; generic HTML-to-text output is inadequate for form-dependent claims. If fidelity is lost or cannot be established, block those claims and require a faithful witness or representation. A matched delimiter count is a diagnostic only, never proof of complete form preservation.

During each unit, locate the precise frame/notation change; distinguish its displayed form from hypotheses about speaker, interface, machine status, affect or reliability. Do not assign the markup a meaning before reading it. Unusual form that crosses a navigation boundary must be preserved in the entering/exiting state without reading ahead.

## 6. Atomic closeout and editorial check

For each authorized unit, finish the following transaction before advancing:

1. Verify owner scope, exact live branch/base, source key/hash and entry frontier. Load only applicable prior state; record actual observed execution capability/configuration without inventing model settings.
2. Inspect **all admitted text and meaningful form**, in order; retain a coverage disposition for every span and every classified ancillary item. A summary or selected quotation cannot stand in for coverage.
3. Produce the unit's deep reading with evidence table, alternatives, focalization/disclosure analysis and entering/exiting snapshots. Keep compact source-language support for wording-dependent claims.
4. Update each of the three owning ledgers, or record an explicit no-change disposition for that unit. Claims hold interpretation/revision history; the other ledgers link to claim IDs rather than duplicating competing arguments.
5. Freeze predictions and the exit state; reconcile coverage, unit count, next candidate, source-map admission boundary and any readiness change. Do not invent an operational character model from isolated evidence.
6. Check names and reference clarity in the opening, substantial middle, exit and every material relationship: who acts, speaks, thinks, observes, receives and is affected? Use verified names within the permitted frontier, preserve intentional concealment/aliases, and classify any role label under handoff Section 15. Record and repair real attribution defects.
7. Review exact changed paths, stage exact files, run required validation, commit the closed transaction and verify persistence/publication under the checklist. Freeze the reading bytes at acceptance; failed validation or ambiguous publication leaves the transaction incomplete. Never advance based only on drafted prose.

A separately authorized single operation stops after closeout. An authorized continuous run proceeds only to its named terminal boundary after each closed transaction. A CLOSED lock, unknown witness, missing required form, unresolved scope or contradictory run state blocks admission. The historical bootstrap was neither mode and admitted zero units. The historical G0 checkpoint authorized only HAR-U001 in single_operation mode. The later owner-authorized continuous run is recorded separately in the current entrypoint and continuation record; no frozen pilot state is widened.

## 7. Revision and preservation

Later evidence is reconciled in the claims ledger through `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`, retaining earlier wording and its boundary. Apply corrections to current topical homes; use an attributable erratum for a frozen reading. Do not edit a prospective freeze to make it retrospectively correct. A source/edition change creates a new witness and explicit dependent-claim review, not a silent replacement. Follow the global archive and handoff policies through the architecture.

## 8. Pre-continuation calibration — 2026-10-16

Advisory reviewer guidance is a prompt to verify the original Japanese, not a source or new governance. State deliberate formal patterns and strongly supported inferences affirmatively, with confidence attached to the precise proposition. Uncertainty about a literary form’s referent or fictional implementation must not erase certainty about the displayed form. Keep only material, textually supported counterreadings; compatible rhetorical functions need not compete with one another. Japanese wording, particles, omitted subjects, register, repetition and meaningful layout remain load-bearing. Narrative claims, strong inference, speculation and value judgment stay distinct. No forecast is required where the text offers no discriminating prospective test.

HAR-U001 remains byte-frozen. Current claim strengthenings use HAR-RV001–HAR-RV004 with complete earlier formulations preserved, including explicit current-version selectors for later source-bound changes; no retrospective source enters that pilot. Each continuation unit freezes its entering frontier before new words, including any explicitly dated source-bounded current-claim revisions. Recurring verification/runtime details live in source/continuation records so literary prose can concentrate on the unit’s warranted argument.
