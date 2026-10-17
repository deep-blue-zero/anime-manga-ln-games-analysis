---
title: "Shuukura V2 — Analytical Method"
artifact_id: SHUUKURA_ANALYTICAL_METHOD
artifact_type: analytical_method
series: "Shuukura / 週に一度クラスメイトを買う話"
series_id: shuukura
generation: SHUUKURA_V2
version: "0.1"
status: active_provisional
scope: "Prospective Japanese reading, evidence admission and interpretive revision"
source_boundary: "Bootstrap metadata and architecture only; zero V2 narrative units admitted or read"
canonical_home: series/shuukura/00 Frameworks and Methods/SHUUKURA_ANALYTICAL_METHOD.md
created: "2026-10-17"
planning_date: "2026-10-16"
review_status: OWNER_BOOTSTRAP_REVIEW_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Analytical method

## Authority, purpose and independence

This INITIAL V2 method is an owner-reviewable proposal at the continuing Shuukura root. It governs how evidence will be read, while the [synthesis architecture](SHUUKURA_SYNTHESIS_ARCHITECTURE.md) governs its cumulative destinations. The [current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) owns operational authorization. Current-eligible provisional metadata describes the proposed governing documents; it does not mean the owner has accepted the foundation or admitted narrative evidence. The sequential lock remains CLOSED.

Read the Japanese published novels as relationship-centered literary fiction. Investigate how specific people perceive, desire, act, speak, misjudge and change. Moral evaluation, genre expectations, diagnostic labels and a presumed destination for the central relationship cannot replace that investigation. Neither novelty relative to V1 nor agreement with V1 is a criterion of improvement.

V1 is historical intellectual provenance, not primary evidence and not an expected-answer key. Bootstrap inspected its paths, administrative metadata, README, manifest and export-warning lines, not its substantive conclusions. Later independent sequential sessions must not load V1 readings, claim extracts or the transcript. Incidental publisher blurbs, web metadata and navigation headings seen during reconnaissance are an exposure limitation: they are not V2 findings. Begin the first reading in a fresh context supplied with this architecture and a spoiler-minimized admission packet, not the reconnaissance session's conversation. Record any actual prior familiarity; do not promise psychological blankness.

## Source precedence and admission

The [source inventory](SHUUKURA_SOURCE_INVENTORY.md) distinguishes publication, acquisition, verified bytes, structural inspection, narrative inspection and analytical admission. Only admitted Japanese source evidence can support V2 literary findings. The preferred lane is the acquired Japanese LN witness at its recorded hash, after edition and locator checks. Kakuyomu, Narō, supplemental prose, images, performance and adaptations retain separate witness IDs. No difference alone establishes another continuity; no matching title establishes textual identity.

The LN is authoritative for a claim explicitly about the LN; the web witness is authoritative for its own wording. Cross-witness conclusions cite both. An edition change produces a new witness revision and a comparison record, never a silent replacement. English or other translations may assist a separately declared translation question but cannot resolve Japanese ambiguity by themselves. Search snippets, V1 summaries and promotional descriptions cannot fill a missing passage.

Before a unit is admitted, verify its identity, source hash, allowed scope, opening/closing native locators and completeness. A decoding success is not a reading. A material missing page, unresolved edition identity or mandatory unavailable modality stops the affected unit. Preserve available independent work and record the precise missing requirement. Do not evade access restrictions or reconstruct unavailable narrative text from other analysis.

## Atomic units and prospective freezes

One LN volume is the normal atomic transaction, including its narrative interludes and internal extras in the verified spine order. Distinguish cover/front matter/illustrations, main chapters, interludes, afterword and bonus fiction as components; paratext is not narrated story fact. Within each volume read chapters, paragraphs and perspective changes in source order. Keep the first-encounter notes before writing the endpoint interpretation. A web atomic unit is one identified episode, unless the authorized run explicitly defines a bounded, ordered chapter group. A supplemental unit is one complete named story; multipart originals remain ordered under that story's ID.

Freeze an entering state **before** narrative exposure: source witness/hash; completed unit boundary; actor identities established so far; relevant character and directional relationship states; known/believed/suspected propositions; unresolved language; live claims and competing hypotheses; registered predictions; excluded later material; observed executor/capabilities. Name the prior endpoint and its Git state in the unit record. V01 enters with no source-derived V2 character facts.

For every scene retain three clocks: (1) source presentation order; (2) depicted event time or explicit uncertainty; (3) disclosure/analyst-admission time. A remembered event may precede the current scene while its evidentiary disclosure occurs later. Never backdate that disclosure into an earlier legitimate reading.

Within-unit retrospective summaries may use the completed unit's knowledge if clearly labeled. They must not overwrite first-encounter notes or ascribe endpoint knowledge to an earlier narrator or character. The endpoint freeze records what changed, what remains uncertain, and which future propositions would discriminate between alternatives. Later evidence revises mutable claims and cumulative state with dated revisions; it does not rewrite frozen prospective records.

## Alternating narration and epistemic asymmetry

Identify narrator and focalizer separately at each perspective boundary. Do not infer them mechanically from alternating chapter positions. Use source indicators, not an assumed A/B pattern; if identity remains uncertain, say so and retain candidate identities. The principal intended subjects are 宮城志緒理 (Miyagi Shiori) and 仙台葉月 (Sendai Hazuki), but their names in this specification are project identity labels, not assertions about what either person knows at the first scene.

For each consequential proposition distinguish:

| Question | Required distinction |
| --- | --- |
| What is presented? | Externally narrated action/dialogue, private experience, remembered event, fantasy, counterfactual or quoted report |
| Who has access? | Narrator/focalizer, speaking subject, addressee, bystander and analyst each receive their own epistemic status |
| What is its force? | Direct observation, explicit self-report, inference, suspicion, desire, self-explanation or unknown |
| What could be wrong? | Limited access, mistaken inference, memory uncertainty, rhetorical emphasis, concealment, self-deception or genuine inconsistency |
| What changes later? | Newly disclosed evidence, revised belief, corrected attribution or a competing interpretation; retain original boundary |

Private narration is strong evidence that a thought is represented, not automatic proof that its causal explanation is accurate. Spoken denial does not by itself prove hidden desire. Inconsistency between narration and action can arise from context, conflict, changed intention or interpretation error; do not default to dishonesty. A narrator's belief about the other person belongs in the [disclosure ledger](../04%20Longitudinal%20Ledgers/SHUUKURA_DISCLOSURE_AND_NARRATION_LEDGER.md), not in the other person's known-fact state.

Build paired-account comparisons only after both passages are admitted. Compare shared event anchors, what each account actually covers, omissions, temporal placement and access. Absence of an account is not a contradiction. Reader inference beyond either self-understanding remains an inference with alternatives and a specified evidence boundary. A later disclosure may support a retrospective explanation without proving the earlier character consciously possessed it.

## Evidence objects and exact locators

Use the inventory's stable unit IDs: `LN-JP-V01`, `BW-JP-V03`, `KSS-01`, and future `KAK-JP-E0001` / `NAR-JP-E0001` bound to immutable web episode IDs. The witness/edition revision is a separate required field. A local observation is `<unit>-O001`; a prediction is `PRED-<unit>-001`; a material interpretive claim is `CLM-<unit>-001.v1`, with `.v2` and later versions preserved. The claims ledger uses these same identifiers. Allocate identifiers once, never recycle or renumber them after deletion or correction. IDs identify provenance, not confidence.

An observation record contains source ID/revision/hash; native component and chapter; scene ID; exact start/end locator; source and event ordering; observer/narrator; evidence kind; bounded description; language note where consequential; inspection channel/method; and any uncertainty. A source-local paragraph locator is valid only against a named deterministic extraction with its hash, parser version and paragraph-to-native mapping retained in Drive. For EPUB, retain member path, native fragment if present, and verified paragraph/span anchors. Do not pretend that an electronic display page equals a print page. For PDF use actual PDF page ordinal, crop/region when needed, and original-to-derivative mapping. For web use work ID, immutable episode ID, retrieval revision/time and span anchor. A TOC-derived ordinal alone is not an exact narrative locator.

The sequential reading owns the observation and any short necessary Japanese quotation. Ledgers reference it rather than copying the same passage into four places. Preserve ruby/base text and punctuation where meaning depends on them. Full extracted text, screenshots, audio and deterministic locator files remain in the evidence plane, not the public Git corpus. A mature claim must be retrievable from claim revision to observation to the hashed primary witness without relying on a chat citation.

## Japanese language and narration

Record original Japanese for consequential address forms, naming changes, pronoun omission, register, imperatives, indirect requests, refusals, hedges, modal force, particles and ambiguous attachments. Identify speaker, addressee and possible omitted subject before translating. Keep literal syntax, plausible readings and chosen contextual interpretation separate. Preserve an unresolved antecedent rather than silently assigning it to Miyagi or Sendai.

Distinguish what a character explicitly says from conversational implication and from the analyst's explanation. Track whether an imperative is framed as a request, rule or performance, who recognizes it as such, and how the addressee responds. Neither polite form nor blunt form determines affection, coercion or consent without context. A naming change requires an actual before/after locator and interlocutor context; do not infer a permanent speech rule from one utterance.

Translation notes include the source span, alternatives, grounds and confidence. Consult primary linguistic/reference sources when a consequential usage cannot be resolved from the text, keeping reference support distinct from narrative evidence. Do not invent certainty through an idiomatic English paraphrase. Distinguish narrator prose, interior monologue, quoted dialogue and dramatized spoken performance. A prose style model cannot claim verified vocal delivery.

## Behavior, relationship and agency questions

For an event, identify who initiates, what is requested, the perceived options, response, constraints, agreement or refusal, subsequent action, consequence and repair. Separate stated rules from mutually understood rules and from actual enforcement. Payment is an observable condition when sourced; it does not automatically establish either free choice or coercion. Consent is action- and time-specific; compliance, silence, a previous agreement or presumed affection cannot settle its scope. Conversely, analytical vocabulary must not prejudge harm or erase context.

Track each direction independently: Miyagi's expectations of Sendai and Sendai's expectations of Miyagi can diverge. Record desire, fear, conflicting priorities, self-presentation, self-justification, dependence, autonomy, exclusivity, jealousy, concealment, accommodation and emotional regulation only where evidence warrants. Context includes public/private setting, social and domestic circumstances, third parties, available information and alternatives. These are investigatory dimensions, not initial findings or diagnoses.

Ask whether a behavior recurs, under which conditions it changes, and what would falsify the proposed pattern. Distinguish intention from outcome and explanation from justification. Include supportive, mundane and countervailing scenes rather than selecting only dramatic incidents. Development may be uneven or reversible; a changed response does not alone prove a stable trait change. Normative evaluation must state the evaluative criterion, keep its evidentiary premises visible, and remain distinguishable from descriptive and literary claims.

## Claims, challenge and revision

Label statements as `SOURCE_FACT` (bounded presentation), `OBSERVATION`, `INTERPRETATION`, `HYPOTHESIS`, `UNCERTAINTY` or `NORMATIVE_EVALUATION`. A source fact about narration need not be an objective fact inside the story. Confidence is reasoned and scoped, not a numerical substitute for evidence.

A material claim records supporting observations, its strongest counterevidence, viable alternatives, boundary and downstream dependencies. Separate repeated textual support from repetition of the same event by two narrators. Predictions are frozen before the test passage, specifying observable outcomes, alternatives and disconfirmation conditions. If the analyst already knows the outcome, classify the exercise as retrospective fitting, never held-out prediction.

Revision uses `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN` in the [claims ledger](../04%20Longitudinal%20Ledgers/SHUUKURA_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md). Preserve the old formulation, evidence scope and reason for change. Propagate only to affected current homes. Correct frozen errors through attributable errata and current revisions under live policy; never silently alter historical bytes. A disagreement with another analyst is a reason to inspect evidence, not proof of error.

## Unit acceptance and capability boundaries

A completed reading must cover every admitted narrative component, identify skipped/unavailable components, preserve the entering/endpoint freezes, provide recoverable observations, reconcile all four ledgers and coverage state, adjudicate due predictions, and identify the next permitted operation without authorizing it. Review exact locators, consequential Japanese, alternatives, temporal attribution and all material relationship transitions. Perform the handoff contract's bounded name-and-reference review across the introduction, middle, endpoint and major relationships; use actual established names where the boundary allows.

Illustrations require direct image inspection if used for a visual claim. Text extraction does not inspect image content. Voice dramas require a separately admitted script/audio witness; a transcript supports lexical claims, while prosody requires actual audio inspection. Continuous AV is not required for an LN-only interpretation merely because promotional videos exist. No capability is certified by the ability to download or decode a file. Record only channels actually inspected.

Amend the method when recurring source behavior exposes a real gap. State the evidence, affected responsibilities and targeted backfill, preserving existing freezes and IDs. The architecture owns amendment and synthesis gates. This bootstrap performs no narrative reading and certifies no finished model.
