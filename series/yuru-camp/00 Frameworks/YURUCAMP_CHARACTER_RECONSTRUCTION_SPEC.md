---
title: Yuru Camp Character Reconstruction Specification
artifact_id: YURUCAMP_CHARACTER_RECONSTRUCTION_SPEC
artifact_type: character_reconstruction_specification
series: YURUCAMP
generation: V1
status: canonical
source_boundary: V15 specification baseline at adoption; current admitted evidence follows CURRENT_STATE_AND_CORPUS_MAP.md
specification_baseline: Japanese manga through Volume 15 on 2026-10-17
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
updated: '2026-10-23'
---

# Yuru Camp Character Reconstruction Specification

## 1. Responsibility and authority

This is the series-local contract for **eventual evidence-supported behavioral reconstruction and validation**. It specifies the inputs, state model, abstention rules, and tests required before any reconstruction can be claimed. It does not duplicate literary monographs, generate simulations, or declare any character ready.

It implements the [global reconstruction capability specification](../../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md) within the [existing analytical method](YURUCAMP_ANALYTICAL_METHOD_V1.md) and [architecture §6.0](YURUCAMP_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V1.md). The [current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md) owns the current source/authority route. At this specification’s adoption on 2026-10-17, the accepted literary boundary was V15 and the governing adversarial freeze was V13–V15. Those are historical baseline fields, not a ceiling on subsequently admitted evidence. For the current committed boundary, governing checkpoint and admitted ledger extensions, follow the current-state map; apply this procedure to that explicitly bounded evidence set. The reconstruction specification being canonical means its **procedure** governs; it is not an authoritative readiness assessment.

No change to `characters/reconstruction_capabilities.jsonl`, the global character registry, or any character capability/discovery index is authorized here. Global grades, enrollment, and curation require the repository's separate controls. Discovery coverage and literary-analysis quality do not establish reconstruction capability.

## 2. Yuru Camp-specific object of modeling

Development often appears as a small change in what is ordinary: who sends a message, who initiates an invitation, which preference is remembered, who accepts help, or who feels free to decline. Model those changes without inventing a dramatic transformation or an unspoken total motivation.

The model must preserve:

- chosen solitude and sociability as different positive preferences; neither is a universal cure for the other;
- initiative, accommodation, refusal, teasing, silence, and boundaries as character- and relationship-dependent;
- practical competence by domain, conditions, equipment, money, transport, and available support;
- low-amplitude friendship across dyads, clubs, families, weak ties, remote communication, and asynchronous groups;
- Japanese conversational form, address, register, dialect, and silence as contextual evidence rather than decorative catchphrases;
- uncertainty, mistakes, corrections, and counterexamples, including care that is not fully consent-transparent;
- what a character has actually experienced or learned by a named scene, distinct from what the reader or later analyst knows.

Neither intimacy nor visual closeness establishes romance by itself. Neither seniority nor competent help establishes expert mastery. A plausible quiet reaction is not evidence that the character silently holds a particular belief.

## 3. Subjects and admissible scope

Stable local subject IDs below are keys for evidence retrieval, not global registry IDs or readiness grades. Preserve Japanese identity and continuity; resolve aliases against source evidence before linking records. Later character names may be used as retrospective indexing aids only when clearly marked unavailable at an earlier narrative boundary. The table records the V15 adoption baseline: statements such as Ema’s then-unestablished camping experience remain temporally indexed to V15. Later accepted observations belong to their own source-boundary records and must not be backcast into this baseline.

| Local subject | Identity | Initial modeling responsibilities | Reconstruction disposition at V15 adoption |
|---|---|---|---|
| YC-RIN | Shima Rin / 志摩リン | solitude, travel, initiative/refusal, remote care, domain-limited experience | Unassessed; no simulation authorized |
| YC-NADESHIKO | Kagamihara Nadeshiko / 各務原なでしこ | novice-to-practiced camping, food, sociability, chosen solo/group alternation | Unassessed |
| YC-AOI | Inuyama Aoi / 犬山あおい | teasing/dialect, cooking, calibration, later cycling beginner/co-learning | Unassessed; V13 cycling cannot enter V03 state |
| YC-CHIAKI | Ōgaki Chiaki / 大垣千明 | organization, experiments, errors/revision, recruitment, solo experience | Unassessed; eligibility is not completed formal promotion |
| YC-ENA | Saitō Ena / 斉藤恵那 | low-pressure connection, optional participation, Chikuwa-related care, advice | Unassessed |
| YC-MEI | Nakatsugawa Mei / 中津川メイ | newcomer agency, cycling interest, junior register, cost/effort learning | Unassessed; sparse earlier state and narrow domain |
| YC-EMA | Mizunami Ema / 瑞浪絵真 | illustration, quiet-space preference, work-derived knowledge, optional camping curiosity | Unassessed; no camping experience or club membership established by V15 |
| YC-SUPPORTING | Individually keyed when needed | Sakura, Ayano, Toba, Akari, family members, and other sufficiently evidenced subjects | No automatic readiness; separate identity, domain, and evidence assessment required |

The supporting row is not a composite character. Never transfer evidence among names merely because they serve a similar narrative role. A named-subject audit must separately account for each subject that a later artifact claims to reconstruct.

## 4. Required per-subject model record

Every eventual model must contain the following fields and supporting evidence. Absence must be explicit, not filled with genre expectations.

| Field | Required content and control |
|---|---|
| Identity and continuity | Local/global identity mapping where authorized; Japanese manga continuity; exact edition/object hash; no anime/anthology behavior silently imported |
| Boundary | Volume, chapter, image/scene endpoint, checkpoint; model creation date and exact repository basis commit kept separate |
| Temporally indexed state | Prior baseline, new observation, first-support boundary, state valid-from/through, unresolved later changes |
| Available knowledge | What the subject personally knows, was told, inferred, or has not learned; reader knowledge separated; uncertainty if information transfer is unseen |
| Stable preference / capacity | Repeated preference distinguished from new ability, temporary mood, compliance, practical constraint, and one successful attempt |
| Behavioral tendency | Bounded proposed rule, situations it covers, observations from independent episodes, failures and alternatives; no deterministic personality formula |
| Context and relationships | Directed actor→recipient, co-present/remote group, invitation history, familiarity, role and power differences; reverse direction assessed separately |
| Voice and register | Verified Japanese excerpts, self-reference/address, endings, politeness, dialect, comic mode, silent response; recipient and situation attached |
| Competence | Specific task, environment, resources, preparation, help used, errors, recovery, stated uncertainty; limits on transfer to another technical domain |
| Negative constraints | Evidence-backed exclusions and separate evidence gaps; unsupported motives, future knowledge, habitual speech, romantic assumptions, or mastery claims |
| Confidence and counterevidence | Observation confidence separated from generalization confidence and verification status; material counterexamples and competing explanations |
| Temporal divergence | Earlier/later state contrast with a source bridge; explicitly identify what would be anachronistic if backcast |
| Provenance and validation | Ledger record IDs, reading/checkpoint sections, primary locators, verified scope, basis commit/evidence hashes, test split and results |
| Abstention | Domains, contexts, voice features, or information state insufficiently evidenced; permitted output is “insufficient evidence,” a range, or no reconstruction |

Use the shared evidence classes: DE direct observation; RP recurrent pattern; IN inference; TH candidate theme; CA counterevidence. No conversion from DE to motive is automatic. A row may combine classes only if the observation and interpretation are visibly separated.

## 5. Evidence admission and temporal safeguards

The five core ledgers under `../04 Longitudinal Ledgers/` provide candidates and provenance. Their common locator/revision register owns source status:

- `ANALYSIS_EXTRACTED`: accurately taken from a canonical reading/checkpoint; not independently source-reverified in the repair.
- `PRIMARY_VERIFIED`: the bounded observation and quoted wording were checked in the specified original image/context. It does not certify a whole behavioral rule.
- `CONFLICT_REQUIRES_REVIEW`: attribution, identity, wording, or conclusion conflicts remain unresolved. Do not use as decisive model evidence.
- `UNVERIFIED`: insufficiently validated candidate, including a missing locator. Do not make it a hard behavioral constraint.

Before model construction, freeze the allowed evidence set at the requested endpoint. Use the V03/V06/V09/V12/V15 checkpoint-state matrix to prevent later discoveries leaking backwards. For a within-volume endpoint, the volume-end freeze is too broad: verify the exact scene order and information available before the endpoint.

Examples of forbidden leakage are treating Aoi's V15 cycling co-learning as V03 expertise; giving Ema camping experience because she later asks about trying it; treating the V12 imagined junior/firewood future as an already realized transfer; or letting Rin know about a trip or conversation she has not received. A chronological ledger row is not proof that every character knows its content.

A later revelation can revise the analyst's account without revising an earlier character's knowledge. Record both the original formulation and the later transition. Correct frozen readings through attributable errata/revision records rather than editing the old prospective state.

## 6. Voice, silence, and Japanese language constraints

Use image-verified, short excerpts for exact Japanese. A transcription from an analysis or OCR is a search candidate only. Verify the speaker, addressee, balloon/tail, adjoining panel, and whether the passage is live speech, thought, text message, reported speech, fantasy, or a joke. Review a full scene when isolated wording is ambiguous.

Aoi's dialect requires attested forms and contextual distributions, not exaggerated generic Kansai speech. Mei's junior register is evidence of relationship/style, not proof of dependence or incompetence. Rin's concise messages must not erase her more expansive speech or internal responses. Nadeshiko's enthusiasm must not become unvarying exclamation; Rin's conditional advice to Ema must not become universal indifference; Chiaki's comic intensity must not erase planning or revision.

Self-reference, address, sentence-final forms, and silence each require independent coverage. If self-reference is not adequately sampled, report that gap. Do not infer a global rule from one joke or one recipient. Silence may mark attention, timing, shared ease, uncertainty, or a panel transition; internal thought is unknown unless depicted. English paraphrase cannot validate Japanese voice.

## 7. Readiness procedure

Readiness is scoped to **subject × time × domain × situation × output mode**. The specification assigns no A–E grades or numerical score. A later local assessment must report each relevant global capability dimension, including `PSYCHOLOGICAL_MODEL`, `LONGITUDINAL_STATE`, `VOICE_REGISTER`, `MUNDANE_BEHAVIOR`, `RELATIONSHIP_CONDITIONING`, `INTERIORITY`, `CONFLICT_BEHAVIOR`, `ETHICAL_DELIBERATION`, `HUMOR_PLAY`, `SOURCE_COMPLETENESS`, `NEGATIVE_EVIDENCE`, and `TEMPORAL_SPECIFICITY`. Sparse conflict/ethical evidence cannot be manufactured because a checklist contains the dimension.

1. **Coverage audit:** enumerate independent scenes/episodes, domains, recipients, routine and strained situations, temporal slices, and contrary instances. Several panels from one episode are one evidence cluster; repeated quotation by multiple analyses is not independent evidence. No fixed row count alone establishes readiness.
2. **Identity and information audit:** verify attribution, source object, chapter ordering, name/address context, and character-specific available knowledge.
3. **Rule audit:** label direct observation versus extrapolation; retain alternatives and actual counterexamples. Check whether a “stable” rule is really a recent capacity or material constraint.
4. **Voice audit:** inspect original images across recipients and modes. Record insufficient dialect/register/self-reference coverage separately from behavioral coverage.
5. **Validation design:** reserve genuinely independent evidence before fitting a model where possible. Document exactly what the model builder has already seen. Existing V01–V15 analyses and scenes already used in this backfill cannot honestly be relabeled unseen held-out tests.
6. **Decision:** mark a proposed domain as supported for bounded testing, provisional with named limitations, or insufficient evidence. Even a passed local test does not authorize a global capability grade or unrestricted simulation.

All seven named subjects currently have **no reconstruction readiness determination** under this contract. Ledger consolidation improves inspectability; it is not the missing validation itself.

## 8. Validation protocol for later authorized work

| Test | Procedure | Failure or limit to report |
|---|---|---|
| In-sample reconstruction | Hide the continuation of an already admitted scene; compare the model's conditional account with the observed action/voice and alternatives | Diagnostic fit only; never claim independence |
| Independent validation | Before fitting, withhold genuinely unseen scenes/episodes or obtain a separately authorized blinded assessment with access provenance; compare against source outcomes | If builder/validator has seen the outcome, disclose contamination; future volumes are not admitted merely for testing |
| Counterexample challenge | Retrieve refusals, mistakes, irritation, inconsistent participation, failed plans, and correction scenes rather than only confirming examples | Revise or narrow the rule when the exception is substantive; avoid ad hoc excuses |
| Contradiction / attribution | Trace conflicting ledger rows to original scene and edition; distinguish fantasized, reported, and enacted events | Unresolved conflict requires abstention in affected domain |
| Temporal leakage | Audit every claimed fact and capacity against the endpoint and that subject's knowledge; compare earlier and later state records | Any later-only information invalidates the affected result |
| Relationship conditioning | Test whether changing recipient/group changes supported expectations; preserve directionality and role asymmetry | A generic “friendly” response across every dyad is inadequate |
| Domain transfer | Separate camping, cooking, navigation, weather, bicycle repair, riding, finance, art, and institutional knowledge | School seniority and one successful task cannot validate another domain |
| Novel situation | Mark all extrapolation, list nearest canonical analogues and important disanalogies, permit multiple plausible responses | Plausibility is not canon; no unsupported precise interiority or certain future behavior |
| Japanese realization | Compare register, address and forms against independently checked examples; evaluate content and Japanese naturalness separately | Catchphrase mimicry alone fails; unknown register/recipient combinations remain limited |

Record prompt/context, model basis, withheld evidence declaration, expected allowable range, observed comparison, evaluator access, contradictions, revisions, and final limits. Do not select only flattering successes. A failed test can narrow a model rather than demand an invented explanation. No novel scenario or character simulation is generated as part of this repair.

## 9. Failure modes and stopping rules

Stop or abstain when identity is uncertain, a source is inaccessible, a quotation is not image-verified, context is insufficient, narrative/reporting layers are confused, an earlier state cannot be reconstructed, or the claimed task exceeds supported competence. Material counterevidence cannot be hidden by averaging confidence.

Especially guard against: solitude-as-deficit; compulsory group inclusion; generic kindness replacing directional familiarity; romance from proximity; Ema's curiosity becoming membership; Mei as a blank successor; Aoi as an expert cyclist; Rin as universally infallible; universal enthusiasm for camping; money/transport/weather disappearing from behavior; and hypothetical junior succession becoming completed administration.

The output of an insufficient-evidence assessment is a precise gap and remediation route: subject, boundary, behavior/voice domain, missing scene or verification, and whether a targeted reinspection or separately authorized future source is required. It is not a fabricated completion state.
