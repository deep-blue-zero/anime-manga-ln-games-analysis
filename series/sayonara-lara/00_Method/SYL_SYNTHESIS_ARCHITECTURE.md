---
title: "Sayonara Lara: Synthesis and Corpus Architecture"
artifact_id: "SYL_SYNTHESIS_ARCHITECTURE"
artifact_type: synthesis_architecture
version: "1.1-adopted"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
prepared_on: "2026-09-20 America/New_York"
drafted_against_commit: "f9dda552a5735f454e3bb99b4af6c920235a618d"
source_boundary: "Corpus architecture for Japanese-language TV anime Episodes 01-12; adopted before sequential episode inspection"
canonical_home: "series/sayonara-lara/00_Method/SYL_SYNTHESIS_ARCHITECTURE.md"
generation: V1_JP_AUDITED
adopted_on: "2026-09-20 America/New_York"
---

# Sayonara Lara: synthesis and corpus architecture

## 1. Identity and design

Proposed root: `series/sayonara-lara/`.

Proposed continuing branch: `series/sayonara-lara`, following live branch policy rather than creating a parallel bare `sayonara-lara` branch [G03]. Codex must first check current registries, roots, aliases, and branches; preserve a discovered canonical home rather than duplicating it.

One current entrypoint: `CURRENT_STATE_AND_CORPUS_MAP.md`. It remains the entrypoint after release; a frozen phase does not justify another 'final README'. Methods govern procedure; ledgers retain cumulative evidence and revision; specialist documents make independent arguments; the full-series synthesis reconciles them. A retrieval guide routes to those homes without becoming another full interpretation.

Proposed generation: `V1_JP_AUDITED`, subject to existing-root reconciliation. The earlier conversation is a separate legacy analytical state, not an already verified V1 corpus. Architecture lifecycle starts `INITIAL`, then becomes `EVOLVING`, `STABILIZED`, and eventually `FROZEN` only through explicit decisions.

This design is deliberately bespoke to a twelve-episode fantasy/domestic drama. It does not copy a large live-service or manga tree merely to reproduce its number of files.

## 2. Three planes and one responsibility per artifact

**Evidence plane:** authorized Drive/source objects, original media, Japanese/English subtitle witnesses, frames, clips, extraction metadata, full joins, ASR outputs, annotations, measurements, source snapshots.

**Working plane:** local caches, temporary models, analysis runs, transport archives, candidate drafts, tools not separately authorized for repository publication.

**Analytical plane:** adopted Git methods, readings, interpretive ledgers, monographs, studies, bounded source pointers, and acceptance records.

A processed derivative is not automatically interpretation. A measured pitch table remains evidence; an argument about Mari's performed reserve belongs in Git. Do not commit episode ZIPs, full subtitle corpora, audio, images, model weights, private paths, signed URLs, or unreviewed extraction executables.

## 3. Intended tree and creation timing

`I` means justified bootstrap infrastructure; `E` means created when that episode/checkpoint is actually analyzed; `S` means created when substantive synthesis is supported; `C` means conditional on demonstrated need. Planned destinations are not fake live links or empty completed documents.

```text
series/sayonara-lara/
  CURRENT_STATE_AND_CORPUS_MAP.md                          [I]
  .repository/
    series-registry.json                                  [I]
  00_Method/
    SYL_ANALYTICAL_METHOD.md                               [I]
    SYL_SYNTHESIS_ARCHITECTURE.md                          [I]
    SYL_AUDIO_AND_AV_PROTOCOL.md                           [I]
    SYL_METHOD_SOURCES_AND_DESIGN_NOTES.md                  [I]
  01_Source_Control/
    SYL_SOURCE_REGISTER.md                                [I]
    SYL_EXECUTION_AND_INSPECTION_RECORD.md                 [I]
    SYL_EXTERNAL_SOURCE_REGISTER.md                       [I]
  02_Episode_Readings/
    SYL_EP01_DEEP_READING.md ... SYL_EP12_DEEP_READING.md   [E]
    SYL_E04_CHECKPOINT.md                                  [E]
    SYL_E08_CHECKPOINT.md                                  [E]
    SYL_E12_SEQUENTIAL_CLOSEOUT.md                         [E]
  03_Ledgers/
    SYL_CLAIMS_AND_REVISIONS.md                            [I]
    SYL_CHARACTER_STATE_AND_READINESS.md                   [I]
    SYL_RELATIONSHIP_TRAJECTORIES.md                       [I]
    SYL_WORLD_RULES_AND_CAUSALITY.md                       [I]
    SYL_MOTIFS_COMEDY_AND_FORM.md                          [I]
    SYL_LANGUAGE_AND_PERFORMANCE.md                       [I]
  04_Characters/
    SYL_LARA_MONOGRAPH.md                                 [S]
    SYL_MARI_MONOGRAPH.md                                 [S]
    SYL_GRACE_MONOGRAPH.md                                [S]
    SYL_ROWAN_MONOGRAPH.md                                [S]
    SYL_LISA_MONOGRAPH.md                                 [C]
    SYL_SUPPORTING_ENSEMBLE.md                            [S]
    SYL_LARA_BEHAVIOR_MODEL.md                            [C]
    SYL_MARI_BEHAVIOR_MODEL.md                            [C]
  05_Relationships/
    SYL_LARA_MARI_RELATIONSHIP.md                         [S]
  06_Specialist_Studies/
    SYL_ALIENATION_EMBODIMENT_AND_SELF_AUTHORSHIP.md        [S]
    SYL_LOVE_FAIRYTALE_AND_RELATIONSHIP_CLASSIFICATION.md   [S]
    SYL_COMEDY_VOICE_AND_AUDIOVISUAL_FORM.md               [S]
    SYL_FAMILY_LAW_LIGHT_AND_CAUSALITY.md                  [S]
    SYL_ENDING_AND_DRAMATIC_CLOSURE.md                    [S]
    SYL_CREATOR_CONTEXT_AND_RECEPTION.md                  [S]
  07_Series_Synthesis/
    SYL_FULL_SERIES_SYNTHESIS.md                          [S]
    SYL_COMPARATIVE_ANALYSIS_GUIDE.md                      [S]
  08_Validation/
    SYL_BLOCKERS_AND_EVIDENCE_DEBTS.md                     [I]
    SYL_INITIALIZATION_AND_ACCEPTANCE.md                  [I]
    SYL_FINAL_CLAIM_AND_COVERAGE_AUDIT.md                  [S]
    SYL_RECONSTRUCTION_VALIDATION.md                      [C]
  90_Legacy_and_Superseded/
    SYL_LEGACY_AND_HYPOTHESIS_REGISTER.md                  [I]
```

Do not create all future directories/files just to realize this diagram. Bootstrap documents are justified because their responsibilities begin before Episode 1: source integrity, capability uncertainty, cumulative state, and known legacy-contamination risks.

Grace's dedicated monograph is a planned major responsibility, not an already established level of coverage. If the verified source does not sustain it, move that responsibility into the ensemble study through an explicit architecture amendment, not a hollow monograph. Apply the same discipline to every anticipated destination.

## 4. Responsibility matrix

| Dimension | Sequential capture | Cumulative owner | Mature destination |
|---|---|---|---|
| Narrative event and presentation | Scene map and close reading | Episode artifact; world ledger for recurring causal claims | Full series; ending |
| Character states, choices, knowledge | Each consequential change | Character state/readiness | Character monographs |
| Directional relationship change | Baseline, event, response, revised expectations | Relationship trajectories | Lara/Mari relationship; relevant monograph |
| Claim history and counterevidence | New/revised major claims | Claims/revisions | All syntheses cite this spine |
| Light, transformation, family law | Shown rule versus claimed rule | World rules/causality | Family/law specialist; ending |
| Alienation and embodied belonging | Mechanism, cost, changed capability | Character/relationship rows plus linked claim IDs | Alienation specialist |
| Recurring objects, composition, comedy | Specific formal device and consequences | Motifs/comedy/form | Comedy/AV specialist |
| Japanese wording and performed speech | Cue, register, actual inspection route | Language/performance | Monographs; love and AV specialists |
| Intent and audience interpretation | Kept outside episode proof | External source register | Creator/reception specialist |
| Missing verification | Scope and affected claims | Blockers/evidence debts | Closure audit |
| Source identity and retrieval | Intake and version changes | Source register | Every evidence route |

Episode readings retain the local argument. Ledgers store compact cumulative changes, not copies of whole readings. Monographs supply integrated causal models, not stitched ledger rows. The same quotation may be referenced from multiple places, but its full linguistic adjudication has one home.

## 5. Canonical document contracts

### Current-state/corpus map

Owns routing and current operational truth: adopted generation, evidence boundary, method/architecture/protocol paths, gate state, authorized range, committed transaction high-water mark, actual channel coverage, live blockers, specialist readiness, current artifact list, next operation, and publication status. It does not duplicate all project arguments.

### Method sources and design notes

Owns the bibliography, dated governance snapshot, external tooling references, and the distinction between repository requirements and series-specific design choices. It is not another analytical method or current entrypoint. Interview lead records migrate to the external source register with their status preserved.

### Source register

Owns sanitized identity and availability of evidence. Distinguish user-reported inventory from actual locked files. Store source IDs, hashes/revisions when obtained, version/language, actual retrieval route, timing basis, and major transformation notes. Detailed machine joins remain outside Git.

### Execution/inspection record

Owns observed environment capabilities, tool/model versions and run IDs, direct versus delegated inspection, interval coverage, failures, and sampling limits. Other files reference this record rather than reasserting blanket 'audio analyzed'.

### Claims/revisions

Owns the current formulation and historical transition of each major proposition. Claim IDs survive changes. Each row identifies its topical analytical owner; this ledger adjudicates revision without becoming an extra thematic monograph.

### Character state/readiness

Owns local cast identity, verified names/aliases, source-state boundaries, evidence distribution, contradictions, and readiness by responsibility. A character can be ready for literary analysis but not voice emulation or behavioral prediction. The global registry is not edited by the series analyst [G12].

### Relationship trajectories

Owns directional relationship events and differences in knowledge/expectation. Record who feels, requests, refuses, gives, receives, or interprets what. A shared scene does not imply symmetrical feeling.

### World rules/causality

Owns rule assertions and their corroboration or failure. Distinguish actual demonstrated mechanism, authority's explanation, hypothetical rule, allegorical interpretation, and inconsistency. Do not let metaphor repair an unexplained physical event.

### Motifs/comedy/form and language/performance

The first owns formal patterns and comic mechanisms. The second owns exact-language disputes and sound-specific observations. A joke that depends on both links the two records instead of duplicating full evidence. Music, silence, and sound-image relations enter the performance ledger; their broader dramatic role is synthesized in the AV specialist.

### Legacy/hypothesis register

Owns the relationship to prior chat analysis and the seed questions in Document 05. It is not current episode authority. Preserve recoverable prior formulations, contrary user/assistant positions, and evidence defects. Do not 'repair' history by making the assistant's latest opinion look like the only earlier position.

## 6. Character and relationship synthesis contracts

### Lara monograph

Must explain curiosity apart from prince-seeking; embodiment; self-worth and guilt; the difference between sacrifice and choice; competence acquisition; familial versus personal ends; rejection and recognition; humor and performed sincerity; relationship-specific behavior; developmental states; and the ending's effect on her agency. Include the strongest case against the governing interpretation.

### Mari monograph

Must recover her independent life: boxing, family, inherited values, everyday preferences, peer conflict, practical generosity, reserve, irritability, and attachments other than Lara. Test grief and narrowing rather than diagnosing them by assumption. Explain when she chooses care, when she resists, and what changes for her rather than treating her as Lara's therapeutic instrument.

### Grace, Rowan, and Lisa

Grace requires an account of motive, information control, coercion, adaptation, comedy, sacrifice, reliability, and discrepancies between professed liberation and engineered choice. Lisa requires a distinct account of sisterly attachment, collective duty, inherited hostility, agency, and knowledge where verified coverage supports it. Do not flatten either into a plot-device villain or use sympathetic history to erase coercion.

Rowan has a planned dedicated monograph because the owner identifies the king as a major ideological axis. It must test his theory of royal duty, personhood, family, sacrifice, inherited antagonism, and legitimate rule against what he chooses and permits. The monograph must distinguish institutional position from private attachment, explanation from excuse, and ideological consistency from opportunistic control. If the verified source does not sustain independent explanatory value, record an architecture amendment and return the responsibility to the supporting ensemble rather than publishing a hollow file.

### Supporting ensemble

Owns substantial bounded studies of Keiko, the original prince, Luca, Himeka, Ouji, Yoshiya, Kota, household figures, boxing peers, and later relevant characters, subject to exact name/identity verification. Characters listed here are candidate subjects, not a certified cast list. Rowan routes to his planned dedicated monograph while retaining ensemble links where his conduct affects other figures. Keep original prince and Luca distinct until the source establishes their relationship.

### Lara/Mari relationship

Owns the dyad's complete trajectory and directional state. Must explain rescue, boundaries, dependence, reciprocity, naming, shared activity, conflict, changing agency, love-language, and separation/continuation. Distinguish dyadic evidence from the genre label 'yuri'. It may conclude romance, friendship, asymmetric attachment, unresolved categorization, or a changing configuration if the evidence supports that outcome.

### Readiness and behavior models

A substantive E04 or E08 provisional monograph is permitted after the corresponding audit; do not wait until Episode 12 for every useful character synthesis. Update its established home as scope grows. Require cross-situation behavior, motive evidence, counterexamples, state boundaries, and unresolved channels. Word count and scene count alone are not readiness.

Only Lara and Mari have anticipated dedicated behavior models, conditional on demonstrated evidence. Define response policies and limits rather than generating dialogue as validation. A prospective test is valid only if the behavior was not already known; otherwise call it a retrospective consistency test. Reconstruction never substitutes for literary interpretation.

## 7. Specialist responsibilities

| Specialist | Independent analytical question | Required inputs |
|---|---|---|
| Alienation, embodiment, self-authorship | What forms of estrangement occur, and what actually changes them? Does reciprocal reintegration explain the whole series? | Character/relationship state, motifs, relevant rules |
| Love, fairy tale, relationship classification | What concepts of love are distinguished, revised, or conflated? What does 'yuri' classify here, and what is actually romantic? | JP language audit, dyad study, internal romantic comparators, verified fairy-tale witness if used |
| Comedy, voice, audiovisual form | How do performance, local realism, fantasy, timing, framing, and role reversals build character and meaning? | Coverage-qualified formal and performance evidence |
| Family, law, light, causality | What is required by the world's mechanisms, asserted by authorities, chosen by persons, and imposed by family? | Rule ledger, agency claims, Grace/Lisa/Rowan evidence |
| Ending and dramatic closure | How well do causal resolution, self-authorship, Mari's position, and relationship communication converge? | Four preceding analytical domains and final episodes |
| Creator context and reception | Where do stated aims, textual realization, marketing, translation, and sampled expectations converge or conflict? | Verified external records plus established source analysis |

The creator/reception study is required because the owner explicitly raised this controversy. It is not a prerequisite for deciding what an episode shows. A narrow sample can support a narrow reception study; a JP-versus-EN cultural generalization requires adequate comparable sampling and cannot be inferred from Reddit alone.

If a new recurring domain cannot be handled in these homes, amend architecture with responsibility, evidence need, target, dependency, and material backfill. Do not split every attractive motif into its own essay.

## 8. Dependency graph

```text
source lock + capability verification + adopted foundation
    -> sequential episode transactions + synchronized ledgers
    -> E04/E08 evidence checkpoints and bounded provisional character work
    -> E12 sequential closeout + role-gap/coverage audit
    -> character monographs (including Rowan if readiness is sustained) + relationship synthesis + rule/language stabilization
    -> alienation / love / comedy-AV / family-causality specialists
    -> ending specialist
    -> creator/reception comparison against established textual results
    -> full-series convergence
    -> comparative guide and any separately validated behavior models
    -> final semantic + coverage + repository audit
    -> owner-controlled promotion/integration/release
```

This is not a license for circular proof. A monograph citing a specialist that cites the same monograph is not independent support. Resolve load-bearing conclusions to episode evidence and the claim spine. Independently owned specialists can be drafted in parallel against one snapshot; ledger mutation has one integrator.

## 9. Completion and phase gates

| Gate | Exit condition |
|---|---|
| G0: bootstrap accepted | Root resolved; current-eligible method/architecture; justified infrastructure; actual capability/source plan; explicit OPEN only after verification |
| G1: episode transaction | Present-phase requirements met, narrative reading and cumulative updates committed, deferred obligations explicitly assigned |
| G2: E04/E08 checkpoint | Contradictions and uncertainty reviewed; hypotheses tested; readiness updated; no hidden source/channel gaps |
| G3: sequential closeout | E01-E12 transactions closed; canonical boundary exact; remaining AV debts separately visible |
| G4: specialist readiness | Necessary evidence for each specialist available and inspected, or its provisional scope explicitly bounded |
| G5: full-series readiness | Required specialist responsibilities covered; major source/AV/causal disputes resolved or honestly adjudicated as unresolved |
| G6: semantic acceptance | Arguments reconcile rather than concatenate; contrary evidence retained; revised claims propagated |
| G7: repository/publication | Applicable preflight, housekeeping, exact-head audit, and integration requirements satisfied |
| G8: frozen release | Explicit approved freeze with exact source/artifact versions and reproducible routes |

Unresolved interpretive ambiguity can be a valid conclusion. Uninspected evidence needed to determine a claim cannot be disguised as artistic ambiguity.

## 10. Phase ownership and continuation

Prefer a bounded hybrid arrangement: this Chat supplies the foundation proposal; local Codex/Work verifies, adopts, and performs ordered episode readings; a fresh high-capability synthesis session can author major monographs and integration from a frozen snapshot; the local integrator completes source/AV gaps and publication. A twelve-episode project need not invoke every long-series phase if the simpler route is adequate [G09-G11].

Use `BOUNDED_STANDARD` for source indexing, `SUBSTANTIVE_ANALYSIS` for normal episodes, `DEEP_SYNTHESIS` for major monographs/specialists, and `PREMIUM_QUALITY_FIRST` only when difficult or propagation-sensitive adjudication justifies it. Resolve actual model access at execution time; brand names do not certify capabilities.

The handoff prompt defines a conditional bounded run through Episode 12 after bootstrap, source delivery, and gate satisfaction. If the sources are not present, complete initialization as far as warranted and stop with a precise next operation. Do not create a watch, schedule, or silently acquire episodes.

## 11. Mutation, preservation, and global ownership

Adopt the live machine authority quartet [G12]. Methods/architecture can become `canonical` after accepted bootstrap even while narrative coverage remains zero. Provisional actual analyses can be `active_provisional`; empty scaffolds and unsupported candidates remain `draft_noncurrent`. Governance documents carry `do_not_use_as_literary_evidence: true`.

Freeze episode/checkpoint knowledge states. Update cumulative documents by targeted patches, preserving IDs and unaffected content. Adopt retrospective changes in topical homes with claim transitions. Preserve nonidentical prior analysis in the legacy layer; do not import the entire conversation as a preferred current source.

The series author supplies its `.repository/series-registry.json`. Housekeeping owns the five routing outputs. Character curation owns `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`; local readiness is not global enrollment. No source/media material enters Git under an analytical-docs authorization.

## 12. Comparative retrieval and final acceptance

The final comparative guide should be a short router with bounded thesis capsules, stable monograph/study links, state-specific warnings, supported comparison axes, and important unresolved claims. It must not become a second full-series synthesis or a matrix of speculative crossovers.

For a later comparative request, route: entrypoint -> relevant monograph/dyad/specialist -> claim history -> episode scene -> source witness when needed. Use the other series' own current entrypoints; do not substitute general fandom memory.

Final acceptance requires a coherent argument about the series, credible independent accounts of Lara and Mari, a defensible relationship classification, a causal audit of the ending, and source-qualified treatment of performance/comedy. An aesthetically tidy tree or green repository audit alone satisfies none of these literary requirements.

## Source key

Governance [Gxx], tooling [Txx], and creator-context [Pxx] identifiers resolve in the [method sources and design notes](SYL_METHOD_SOURCES_AND_DESIGN_NOTES.md).
