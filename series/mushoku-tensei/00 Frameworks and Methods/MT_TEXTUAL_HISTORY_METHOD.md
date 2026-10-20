---
title: "Mushoku Tensei - Textual History Method"
artifact_id: "MT_TEXTUAL_HISTORY_METHOD"
artifact_type: "textual_history_method"
series: "Mushoku Tensei"
generation: "V1"
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_TEXTUAL_HISTORY_METHOD.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Textual history and adaptation comparison

## 1. The research object

Study how meaning changes across identifiable witnesses: hosted WN versions, authenticated historical WN states, commercial Japanese LN editions, separately published supplements, translations, and adaptations. This is textual-history research, not permission to combine all versions into a single maximal canon.

The central distinctions are **observed textual difference**, **effect on characterization or reader position**, **probable revision mechanism**, and **attributed historical intent**. The first can sometimes be directly established while the latter three remain progressively more uncertain.

This lane is separate from the primary LN prospective reading. It opens only with an approved scope and an eligible comparison boundary. [MT_SOURCE_AND_SCOPE_MAP.md](MT_SOURCE_AND_SCOPE_MAP.md) owns admission rules.

## 2. Do not call a mutable page the original publication

A current WN page is a dated witness to what is displayed now. Its work publication date does not prove that every displayed phrase was present on that date. Record retrieval date, visible update information, and any independently authenticated earlier captures.

An author's later recollection is evidence of that recollection, not automatically a contemporaneous production record. A deleted story reproduced by fans may be useful as a lead but needs provenance, completeness, and version authentication. Never silently substitute a fan translation or reconstruction for unavailable Japanese original text.

The preceding conversation included specific claims about early wording, later author statements, and platform moderation. Keep these in the transport quarantine until their exact witnesses are verified. A plausible claim repeated across summaries does not become independent corroboration.

## 3. Comparison modes

Declare one of the following before inspection:

| Mode | What it can establish |
|---|---|
| `TARGETED_DIAGNOSTIC` | A precise change at identified passages; not a series-wide pattern. |
| `STRATIFIED_SAMPLE` | Patterns within a declared selection spanning kinds of scenes/changes; disclose selection limits. |
| `COMPLETE_ALIGNED_RANGE` | The inspected correspondence across a bounded range, with unmatched material accounted for. |
| `REVISION_HISTORY_CASE` | A documented sequence of drafts, edits, removals, or reintroductions. |
| `ADAPTATION_CASE` | Medium-specific treatment of an identified narrative sequence. |

Do not describe a search for controversial phrases as an exhaustive WN/LN comparison. To test systematic mitigation, sample or inspect mundane, sympathetic, violent, comic, and nonsexual material too; record counter-directional changes and unchanged diagnostic material.

## 4. Alignment and unmatched material

Establish correspondence through events, headings, scene structure, and prose rather than assuming equivalent volume numbers. WN-to-LN mappings may be many-to-one, one-to-many, moved, rewritten, added, or unmatched.

Retain original order and locators. Deterministic scripts can nominate matches, but semantic equivalence and interpretive effect require actual inspection. Keep alignments, normalized text, and hashes in Drive; store interpretive variant records in Git.

For each unit, record whether the earlier and later witnesses are fully inspected, partly inspected, or unavailable. If a scene is absent from the mapped range, check plausible relocation before calling it deleted. Failure to locate something is not yet proof that it never appeared.

## 5. Variant record

```yaml
variant_id: null
comparison_mode: TARGETED_DIAGNOSTIC
witness_a: null
witness_b: null
locator_a: null
locator_b: null
historical_order_and_basis: null
alignment_status: null
observed_difference_non_graphic: null
operation: null
possible_effects: []
competing_explanations: []
intention_evidence: []
unchanged_or_counterdirectional_context: []
claim_refs: []
inspection_limits: null
```

Useful operations include addition, omission, substitution, relocation, expansion, compression, perspective change, and revision of motivation or consequences. An operation is not its explanation. 'Omission' is observable; 'publisher censorship' normally is not established by omission alone.

Separate byte/packaging differences from textual differences. Separate altered wording from the analyst's translation choice. Preserve the source's ambiguity where neither witness resolves it.

## 6. Interpreting revision effects

Ask what changes in agency, sympathy, responsibility, explicitness, access to affected people, comic/erotic register, motivation, consequence, and thematic structure. A short deletion can be highly consequential; a long addition can be mostly logistical. Word count is not an effect-size measure.

Possible explanations include readability, characterization, continuity repair, revised pacing, changes in target audience, editorial advice, platform rules, commercial accessibility, author self-revision, and altered artistic priorities. Do not choose whichever explanation matches the desired verdict.

'Attenuation' can be an effect claim even when the decision-maker is unknown. 'Commercial palatability' is a causal hypothesis. 'The editor required removal' is a historical attribution requiring specific evidence. An effect can be plausible without a secure motive.

## 7. Authorial-intent ladder

Use progressively stronger formulations only when justified:

1. The text creates a particular effect in a supported reading.
2. A pattern makes that effect look deliberate rather than incidental.
3. A dated creator statement describes a compatible intention.
4. Contemporary evidence specifically connects that intention to the relevant revision.
5. Independent production evidence identifies the responsible decision and mechanism.

These are evidence distinctions, not mandatory steps for every literary inference. Authorial intent can be reasonably inferred without a confession, but the confidence and alternatives must remain visible. Later commentary cannot guarantee that the effect succeeded, that readers shared it, or that the intention was unchanged across years.

For commentary preserve exact source, author, date, original wording where necessary, translator, context, and whether the statement concerns the WN, LN, supplement, adaptation, or a different topic. Search snippets and unattributed paraphrases are not enough for a load-bearing quote.

## 8. Editorial and platform history

Separate audience criticism, voluntary revision, publisher intervention, and platform enforcement. They may overlap in time without proving a causal chain.

For a removal case, document the original work/version if available; author's contemporaneous response; actual notice if public; policy text in force at the time; the author's account of removal; and any verified subsequent rewrite. If the platform did not disclose the offending passage or rule, preserve that uncertainty. Do not infer a precise violation solely from subject matter or present-day rules.

A country's legal/cultural landscape and a private platform's all-ages rules are different questions. Do not treat 'Japanese tolerance' as a single explanatory fact. Legal conclusions require their own current qualified sources and are not supplied by this literary method.

## 9. Adaptations and translations

A later adaptation study needs a named source release, correspondence map, and the relevant perceptual channels. A subtitle can support wording; a screenshot cannot establish timing; extracted audio cannot establish bodily staging; opening a video file does not prove it was perceptually inspected.

For anime, follow the live episode-bundle and continuous-video-escalation policies. Use targeted continuous intervals when timing, motion, or performance is decisive; do not mandate video for a prose-only claim. Manga comparison needs legible page inspection, not dialogue extraction alone.

Assess focalization loss/addition, voice, pacing, framing, comedy, visual/sonic emphasis, and the representation of others' responses. A change in medium is not automatically softening or worsening. Both hypotheses require scene-specific support and scope-matched counterexamples.

A localization study distinguishes translator wording, edition revision, publisher changes, and source ambiguity. Do not attribute a difference to censorship or mistranslation before comparing the actual editions.

## 10. Completion and synthesis

A variant case closes when both sides are sufficiently verified for the claim, correspondence and limits are stated, the operation is separated from its interpretation, and the claim ledger is updated. Missing historical witnesses may leave causal history unresolved while permitting a bounded current-version comparison.

A systematic revision thesis needs a declared corpus/selection, meaningful counterexample search, attention to unchanged material, and a bounded conclusion. No tally alone proves commercial strategy or ethical rehabilitation.

Textual-history synthesis must preserve the main-LN reading as its own product. Report what changes when readers include the WN or later supplements, rather than retroactively inserting those materials into every earlier volume freeze.
