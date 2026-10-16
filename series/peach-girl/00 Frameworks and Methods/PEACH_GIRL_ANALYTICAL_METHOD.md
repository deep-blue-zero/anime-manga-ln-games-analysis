---
title: "Peach Girl — Prospective Manga Analytical Method"
artifact_id: PEACH_GIRL_ANALYTICAL_METHOD
artifact_type: analytical_method
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.1"
status: active_provisional
scope: "How admitted manga evidence is inspected, interpreted and prospectively frozen"
source_boundary: "Original Japanese manga; 新装版 V01–V18 candidate witnesses; no narrative admission at bootstrap"
canonical_home: series/peach-girl/00 Frameworks and Methods/PEACH_GIRL_ANALYTICAL_METHOD.md
created: "2026-10-16"
review_status: OWNER_BOOTSTRAP_AUDIT_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Analytical method

This is the proposed reading contract for Miwa Ueda's original manga. It governs evidence and judgment; the [architecture](PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md) allocates cumulative and final responsibilities. The [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) alone reports current permission and progress. This current-eligible provisional method contains no narrative findings, is not owner-approved, and does not open the sequential lock.

## Witness, admission and locator contract

Use the exact Japanese 新装版 witness identified in the [source map](PEACH_GIRL_SOURCE_AND_SCOPE_MAP.md). Inventory presence, successful transport, structural verification, narrative admission, actual inspection and transaction closure are separate states. Before reading a volume, retrieve intact bytes, match its recorded size and SHA-256, verify ZIP integrity, OPF identity, spine/resource ordering and image accessibility, and declare included components. A different checksum is a new or unresolved witness, never an unnoticed replacement. Record gaps without claiming a complete unit.

One admitted numbered volume is the default atomic unit. Chapter-sized work requires an explicitly approved amendment and complete verified chapter boundaries. Processing chunks do not change the unit, permit looking ahead, or advance the completed high-water mark. Within a volume, inspect in source order and retain chapter-level disclosure frontiers for consequential observations; do not use an end-of-volume revelation to explain what an earlier scene established at first encounter.

Use `PG-JP-NE-VNN-W01 / component / C<verified label or UNKNOWN> / iNNNN / panel / balloon`. `iNNNN` is the one-based occurrence in the admitted OPF spine, including covers and edition matter, not an operating-system sort or publisher page number. Record wrapper and image member paths in a versioned source-side locator map. If a wrapper references multiple images, use a subindex without silently renumbering later occurrences. Keep double-page images intact; any analysis crop adds a region coordinate against the original image and does not become a source page. Repeated resources retain occurrence identity. Reading direction and spread pairing follow the inspected edition, not an assumed Western ordering.

Publisher pagination is a separate `p<label>` field, established only when actually visible and mapped. Never calculate it by subtracting a presumed cover offset. Unnumbered, duplicate or missing printed pages remain explicit. Chapter identity and start/end indices require verification; navigation presence alone is insufficient. Panel IDs are analyst-assigned in a declared local reading sequence, with a brief region description when ambiguous. Balloon IDs identify speaker, recipient and reading order only to the certainty the page supports. No precise panel locator is invented at bootstrap.

The exact locator map, extraction parameters and source/derivative checksums belong in the Drive evidence plane. Public readings carry compact locators, evidence IDs and retrieval references. Preserve Japanese source spelling and furigana where inspected. Assign local character IDs only after admitted evidence, distinguish uncertain identity from a known unnamed person, and retain readable names in prose rather than replacing every reference with an ID. Apply handoff-contract Section 15: use established names as normal references, purposeful roles where analytically needed, and anonymity/aliases where the disclosure boundary requires them. Before semantic acceptance, promotion or integration, sample the introduction, substantial middle reasoning and exit/conclusion for referent/attribution clarity and record material findings; no mechanical name substitution can certify that check.

## Observation, assertion and interpretation

Every consequential observation has `PG-EV-VNN-####`, witness/component/locator, inspected context, disclosure frontier, represented story time with uncertainty, actual inspection route and limitations. A reading is the canonical home of that observation and its short wording/translation note; other documents cite it rather than copying a second authoritative transcript.

| Evidence class | What it establishes | What remains to be tested |
| --- | --- | --- |
| DEPICTED | An inspected action, layout, expression, gesture or visual/textual feature | Perspective, stylization, imagined/remembered status and interpretive meaning |
| CHARACTER_STATEMENT | A specific person's utterance, interior statement or recollection | Accuracy, sincerity, completeness, intention and persistence |
| NARRATOR_INFORMATION | Information attributed to an identified narrating layer | Narrator scope/reliability; distinction from a character thought or editorial caption |
| PARATEXT | Edition, publisher or creator material explicitly classified as such | Its authority for fictional events and independence from promotional framing |

Attach a separate claim label: `ESTABLISHED_SOURCE_FACT`, `STRONGLY_SUPPORTED_INTERPRETATION`, `PLAUSIBLE_COMPETING_INTERPRETATION`, `SPECULATIVE_HYPOTHESIS`, or `UNRESOLVED_QUESTION`. An established fact may be only that someone made a claim. Confidence (`HIGH`, `MODERATE`, `LOW`, `UNRESOLVED`) names evidential support, with a reason; it is not a diagnosis or numerical likelihood. Separate uncertainty about reading the marks, who speaks, event timing, translation, and motive.

For consequential interpretations, preserve supporting observations, the strongest available counterevidence, a credible competing reading, and what would discriminate them. If no counterevidence has been found, say that within the inspected boundary; do not invent an opposing scene. A statement that a character lied requires evidence of knowledge and intentional misrepresentation; false information alone may support error, rumor, partial knowledge or an unresolved cause.

Japanese is the primary wording witness. Translations are separately identified aids, never silent replacements. Preserve only short diagnostic quotations, with attribution, locator, literal/idiomatic alternatives and unresolved pronouns or register where relevant. OCR is a retrieval aid and must be checked visually before supporting a quotation. Illegible lettering remains illegible. No complete dialogue dump or unnecessary explicit image/dialogue reproduction belongs in Git.

## Prospective transaction

The current lock is CLOSED for `AWAITING_OWNER_BOOTSTRAP_AUDIT`. The following procedure applies only after separate owner approval and source-reading authorization:

1. Recover the exact approved Git base, method/architecture versions, authorized unit and previous frozen exit. For V01, the entering narrative state is empty. Record any prior knowledge or incidental exposure and its permitted use; unsupported memory never supplies evidence.
2. Verify and admit only the named source unit and components. Do not open later narrative pages, later analytical findings, summaries or quarantined supplements. A source-structure audit is not permission to inspect narrative images.
3. Inspect every admitted mainline page in order at legible resolution, including transitions across pages and chapters. Maintain coverage and unresolved-reading notes. Capture new observations before using them to test an explanatory account.
4. Test inherited interpretations and predictions against the new observations. Distinguish corroboration, absence of a test, contradiction and genuine revision. Record newly disclosed past events as later knowledge, not newly occurring actions.
5. Write the unit reading and update every materially affected cumulative instrument, including downstream claims and readiness when actually affected. Record a concise update/no-material-change disposition per instrument in the closeout; do not add dummy ledger events.
6. Freeze `PG-FR-VNN`: entering freeze/base, admitted witness hashes/components, inspected extent and exclusions, current claim and state versions, unresolved issues and actual prospective forecasts if warranted. Retain enough compact state to reconstruct the next entry without consulting mutable future ledger rows. VNN+1 cannot be opened before this transaction is closed and committed under live policy.

Each future `02 Sequential Readings/PEACH_GIRL_VNN_DEEP_READING.md` must contain: authorization/source receipt; entering state; component and page coverage; compact developments/context; source-grounded close reading of text and form; character/relationship/information/agency changes; counterreadings; inherited claim and forecast dispositions; ledger update manifest; prospective exit snapshot; limitations, completion decision and informational next candidate. Narrative summary is an orientation layer, not a substitute for analytical reasoning. No such reading is created during bootstrap.

Future execution defaults to `single_operation`. A separately authorized continuous run names a recoverable terminal boundary and closes each unit individually. Before admission, record the actual authorized run with the live policy's exact `sequential_execution` fields: `mode`, `unit_type`, `run_state`, `authorized_start`, `terminal_boundary`, `committed_high_water_mark`, `next_candidate_operation` and `confirmation_between_units`; the active candidate must agree with `project_initialization.next_permitted_operation` and an OPEN lock. An agent-written state is not owner permission. Interrupted or partly inspected units remain partial; the last committed high-water mark does not advance. Source gaps, illegibility, unauthorized scope, uncertain authority or required capability failure block the affected operation. Resume from verified state rather than conversational recollection.

## Character and relationship questions

Investigate romantic attraction and affection, friendship and affiliation, rivalry, jealousy, insecurity, attachment and dependency where evidenced. Keep directional feelings, declared labels, observed behavior, mutual understanding, public presentation and actual commitments distinct. Do not assume intimacy implies romance; do not recategorize explicitly supported romantic attraction as friendship or admiration without textual justification. A refusal, denial or reclassification is also evidence whose speaker, context and timing matter.

For a consequential choice, identify actor, options actually available, constraints, perceived knowledge, expressed intention, action, recipient response and observed consequence. Separate initiative, acquiescence, desire, permission and coercion; each has its own time and context. Neither affection nor a later reconciliation retroactively settles an earlier boundary. Equally, an analytical concern is not evidence that coercion occurred. Preserve alternatives and asymmetric evidence about the participants.

Compare declared intentions, inferred motives and observed conduct without assuming they must agree or that every discrepancy is deception. Track self-presentation, reputation and peer-group pressure through identifiable audiences and transmissions. Rumor truth, belief, circulation and social consequences are different questions. Social judgments are attributed to their source rather than adopted as the analyst's voice.

Sexual themes, if present, can have narrative, relational and formal significance. Describe the necessary event or framing at the level needed to analyze that significance, with locators, without unnecessary reproduction of explicit material. Neither the presence of a theme nor a reader's moral reaction predetermines its narrative function. Distinguish description, causal explanation, ethical evaluation and endorsement. An ethical argument states its criteria and addresses counterevidence. Avoid unsupported moral verdicts, clinical diagnoses or intentions inferred solely from genre conventions.

Developmental change needs a time-indexed basis. Repeated decisions across distinct situations may support a tendency; one expression or crisis does not establish a timeless trait. Include ordinary social contexts and failures as they become available, not only dramatic romantic scenes. A character can hold conflicting desires. Preserve limits imposed by focalization and access to interiority.

## Manga form and written interaction

Read panel sequence and pacing, page turns, scale, placement, gaze, expression, gesture, framing and viewpoint as evidence. Ask what is visible to the reader, to each character, and only through an attributed recollection or imagined image. Concealment, revelation, visual parallels and repeated motifs need locators and an account of their change in context. A visual repetition is not automatically a deliberate motif; alternatives may include convention or coincidence.

Test dialogue against depicted behavior and layout. Distinguish an inference that an expression suggests hesitation from an established refusal or specific motive. Track ambiguity when more than one panel order or speaker assignment is plausible. Do not infer motion between omitted moments as if it were directly shown. Written register, address forms, syntax, punctuation, lettering and interaction rhythm can support a written speech model. Unvoiced manga dialogue provides no acoustic timbre, pitch, vocal prosody or performed delivery.

## Revision, neutrality and maintenance

Later disclosures may revise the current interpretation through the claims ledger's `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` transitions. A new row records old/new formulations, both evidence routes, counterevidence, learned-after frontier and affected dependencies. Never backdate mature knowledge into an earlier freeze. Errata identify the actual earlier mistake in a separate attributable record; original frozen bytes remain unchanged. They are not retrospective story revisions disguised as corrections.

Version this method and record substantive changes in the entrypoint and architecture history. A frozen execution retains the version actually used. Capability, surface, dates, source routes and observed execution configuration are recorded for recovery; unknown metadata stays unknown. No system's identity supplies evidence or relaxes these standards. Independent capable executions receive the same prospective contract; this method contains no expected outcomes or comparative judgments.

Revision history: 0.1 — initial owner-audit candidate, 2026-10-16 UTC; zero narrative observations.
