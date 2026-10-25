---
title: "Cornered Mouse — Analytical Method"
artifact_id: CORNERED_MOUSE_ANALYTICAL_METHOD
artifact_type: analytical_method
series: "The Cornered Mouse Dreams of Cheese / 窮鼠はチーズの夢を見る"
series_id: cornered-mouse
generation: CORNERED_MOUSE_BOOTSTRAP_V1
version: "0.2"
status: active_provisional
scope: "Prospective Japanese manga inspection, evidence discipline and atomic closeout"
source_boundary: "Japanese manga continuity; AIO2020 structurally checked; no narrative admission or reading"
canonical_home: series/cornered-mouse/00 Frameworks and Methods/CORNERED_MOUSE_ANALYTICAL_METHOD.md
created: "2026-10-24"
review_status: OWNER_BOOTSTRAP_ARCHITECTURE_APPROVED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Analytical method

This method governs **what to inspect and how to reason**. The [source map](CORNERED_MOUSE_SOURCE_AND_SCOPE_MAP.md) owns witnesses and ordering; the [architecture](CORNERED_MOUSE_SYNTHESIS_ARCHITECTURE.md) owns cumulative destinations and synthesis gates. It is provisional, with no narrative findings. Higher-level [initiation](../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [continuation](../../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) and [handoff](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) contracts govern.

The planned manga inspection lane is `STILL_IMAGE`, with `TEXT` only for source-checked lettering/transcripts and translation comparison under the [inspection-lane policy](../../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md). Japanese remains the primary language. The bootstrap capability probe covered only contents/colophon images; a future authorized reading must verify narrative image legibility. No audio or continuous-AV lane is admitted. This names the existing page-based evidence route without adding an inspection stage or evidence obligation.

## Unit, access and locators

Use the source map's separately titled chapter/component candidates, in verified collection order, as atomic transactions. This preserves interlude disclosure and supports reconciliation across edited collections. Do not treat two bibliographic books or one omnibus as two or one complete reading transactions. If inspection reveals a titled component needs subdivision, define stable subunits and freeze points before consuming it; amend the source map/architecture with the reason, without retroactively inventing checkpoints.

Before narrative access, recover owner authorization, approved witness, source hash, component range, predecessor freeze and current lock. Admit only the authorized range. A structural probe may locate boundaries; it cannot be used to read later scenes. Stop on corrupt/missing/ambiguous pages or inadequate legibility, record the exact gap, and do not advance completion. View every page in the unit at usable resolution; contact sheets orient inspection but cannot certify unreadable dialogue or omitted panels. Record actual page coverage and unresolved visual/textual gaps.

Use a source reference in this exact grammar:

`CM-JP-AIO2020::spNNNN::xhtml=<member>::image=<member>::panel=Pnn::balloon=Bnn`

`spNNNN` is the 1-based OPF spine position, padded to four digits and including covers/paratext; `xhtml` and `image` are exact case-sensitive archive paths. Bind the whole-source SHA-256 through the source map and an image digest through the unit's coverage receipt. Panel/balloon selectors are optional until relevant. Number panels and balloons in the page's verified reading order; document ambiguous order with a bounded region or `(left, top, right, bottom)` coordinates on the original-size image. `P00` denotes whole-page composition, not an invented panel. A spread cites both images and the verified viewing order. Printed page numbers are additional labels only after image verification. A valid existing example is the **contents** reference `CM-JP-AIO2020::sp0010::xhtml=item/xhtml/p-0008.xhtml::image=item/image/i-0008.jpg::panel=P00`; it is not a narrative observation.

Within a reading, assign stable observation IDs `CM-U01-O001`, scene IDs `CM-U01-SC01` and evidence anchors such as `#cm-u01-o001`; reserve comparable unit-prefixed IDs for later units. A cumulative row refers to `reading path#anchor` plus its source locator. Observations are never renumbered after publication. Character (`CM-CH-...`), relationship (`CM-REL-...`), information (`CM-INF-...`), decision (`CM-DEC-...`), claim (`CM-CL-...`) and forecast (`CM-PR-...`) IDs are allocated only when admitted evidence warrants records. They are local IDs, not global character enrollment.

## Five knowledge planes

Keep reader-visible evidence, each character's knowledge/beliefs, the analyst's contemporary inference, later established disclosure and mature retrospective interpretation separately labeled. Record event-time and disclosure-time independently; uncertainty in either stays explicit. Character testimony proves an utterance, not its truth, sincerity or narrator endorsement. A recollection is not automatically an independently shown event.

Freeze an entering state from the predecessor before opening the unit. At the first unit there are no admitted narrative claims. Declare unavoidable external exposure, including this bibliographic scouting; do not present synopsis-based expectations or source-aware hindsight as blind predictions. Record a genuine forecast with its timestamp/committed boundary, target and falsifier **before** inspecting the outcome. Freeze within a long unit before a later page if making a page-bounded forecast; otherwise forecasts are only prospective beyond the unit. Retrospectively reconstructed expectations receive that label and no predictive credit.

Later explanations may revise current interpretation through claims history; they never rewrite what an earlier freeze knew. Later-authored manga set earlier has separate publication, event-time and analytical disclosure fields. Keep supplemental images and commentary outside the mainline inspection batch. Preserve original closing material in its verified collection sequence; an authorial chronological note does not move it into a different prospective position.

## Observation and interpretation

Inspect plot/scene action, speaker and addressee, narrative perspective, interior monologue, page/panel composition, gaze, gesture, facial expression, framing, distance, silence, juxtaposition, transitions and revelation timing as distinct channels. Note what is shown, withheld or inferred. Expression and gesture may support several motives; a compelling facial reading is not direct access to a unique interior state. Distinguish written thought, spoken speech, depicted action and analyst interpretation. Record attribution uncertainty rather than filling it from expectation.

Use explicit claim kinds: `OBSERVATION`, `TESTIMONY_OR_RECOLLECTION`, `SUPPORTED_INTERPRETATION`, `COMPETING_INTERPRETATION`, `SPECULATIVE_HYPOTHESIS`, `UNRESOLVED_QUESTION`, `VALUE_JUDGMENT`. Consequential interpretations carry source locators, temporal scope, confidence with reasons, material counterevidence, a credible alternative when available and a disconfirmation condition. Criticism and sympathetic explanation meet the same standard. Do not diagnose psychiatric conditions from dramatic conduct, substitute generic BL conventions for evidence, or turn moral vocabulary into a causal explanation.

Japanese is the language basis for consequential wording. Preserve only short necessary Japanese snippets with exact locators and a clearly labeled gloss; compare an identified official English witness separately. OCR must be checked against legible source images before a precise quotation or linguistic claim. Record uncertain reading, omitted subject, ambiguous reference and register alternatives. Manga supports written vocabulary, self-reference, address and conversational behavior; it provides no acoustic timbre, breath or actor performance. Do not import those from drama CDs or film.

## Open analytical lenses

| Lens | Required distinctions and questions; no predetermined answer |
|---|---|
| Desire, attachment and dependency | Attraction, affection, familiarity, habit, obsession, insecurity and fear of loss are distinct candidates. Compare professed and demonstrated attachment, desire and willingness to sustain a relationship. Persistent desire does not prove compatibility. |
| Agency, consent and coercion | Track each request/refusal, boundary, conditional agreement, pressure, information leverage and practical exit option. Sexual consent, affection and later acceptance are distinct and time-specific. Test desire, fear, habit, opportunism and unresolved motives as explanations for compliance. Later love cannot retroactively establish earlier consent; evidenced change still deserves recognition. |
| Sexuality and self-conception | Separate stated identity, conduct, desire, self-description, social expectation, uncertainty and possible change. One encounter/relationship cannot establish a definitive orientation. No orientation or uncertainty is inherently more authentic. |
| Commitment, betrayal and responsibility | Record emotional/sexual exclusivity, formal status, promises and unspoken assumptions separately. Distinguish deception, omission, avoidance and failure to decide; identify people affected and foreseeable consequences. Emotional meaning and ethical conduct are independently assessed. |
| Asymmetry | Compare information, initiative, bargaining power, investment, uncertainty tolerance and vulnerability directionally over time. Initiative alone does not prove control. |
| Other characters' agency | Preserve each person's name when known, expressed preferences, knowledge, commitments, choices and consequences. Women and secondary characters have independent responsibilities in the evidence; limited interior access is a limitation, not permission to invent motives or reduce them to obstacles. |

When evidence conflicts, test chronology/disclosure, character ignorance or deception, focalization, translation/edition revision, paratext, continuity and genuine inconsistency. Route unresolved conflict to a claim row and affected state home. Do not force harmonization or a static ethical verdict.

## Atomic reading and closeout

1. Verify authorization and exact source identity/range; create `01 Sequential Readings/CORNERED_MOUSE_U01_DEEP_READING.md` only for an actually authorized unit, using `artifact_type: deep_reading` and truthful authority metadata. Supplements use `02 Supplemental Readings/` only when separately admitted. These are future paths, not empty bootstrap artifacts.
2. Record coverage, Japanese witness, hashes and locator convention; predecessor freeze; entering reader/character/analyst state and contamination limitations.
3. Inspect the complete unit. Preserve scene/plot observations, formal evidence, speaker certainty, information changes, directional relationship/decision changes and consequential competing explanations. Unit knowledge limits apply even when all pages share one EPUB.
4. Adjudicate prior genuine forecasts against their original target; record support, failure, mixed result, non-discriminating outcome or unobserved outcome without changing the old forecast. Distinguish explanation after the event from prediction.
5. Advance the four cumulative homes only where material evidence warrants changes. Record explicit no-change dispositions for unaffected ledgers. Route each substantive claim/revision and its downstream impact; keep original observations recoverable.
6. Record a closing checkpoint: inspected range and gaps; prospective exit freeze; current hypotheses/counterevidence; affected ledger IDs; readiness gaps; next candidate and permission. Freeze the reading before any subsequent narrative access, then validate and commit the complete transaction before continuous execution advances.

Update source coverage and the current entrypoint only to verified committed completion. A drafted reading, retrieved EPUB or ledger row alone is not a closed unit. A continuous run requires a recoverable terminal boundary; an informational next candidate grants no continuation. Resume interruptions by comparing live repository state and remote heads before writes; never duplicate or regress an accepted high-water mark.

Frozen readings and forecasts retain their historical bytes. Corrections use attributable errata/current claim revisions or authorized successors under the archive policy. Method amendments record version/reason and affected future operations; backfill occurs only for a material evidence gap, never as invented prospective history.
