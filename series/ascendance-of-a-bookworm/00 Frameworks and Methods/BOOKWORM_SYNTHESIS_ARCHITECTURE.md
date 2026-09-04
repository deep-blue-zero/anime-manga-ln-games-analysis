---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: synthesis_architecture
scope: JP_LIGHT_NOVEL_SEQUENTIAL_TO_FULL_SERIES_ANALYSIS
generation: V0.1
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
governing_method: BOOKWORM_ANALYTICAL_METHOD.md
source_boundary: "Japanese-language light-novel EPUB corpus: numbered main Volumes 01-33 plus acquired Royal Academy Stories: First Year side-story volume; source audit dated 2026-08-30"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm — synthesis and corpus architecture

## 1. Responsibility

This document governs **what corpus the sequential Japanese-light-novel readings are building** and how source-unit analysis must propagate into cumulative state, character work, specialist synthesis, evidence routing, and eventual full-series integration.

It is the paired architectural companion to `BOOKWORM_ANALYTICAL_METHOD.md`:

- the analytical method governs **what to notice and how to judge it**;
- the longitudinal layer governs **what must survive cumulatively**;
- this architecture governs **where preserved evidence and models must converge**.

This architecture is not literary evidence and establishes no substantive claim about any character, relationship, institution, theme, metaphysical system, or event merely by naming a future analytical responsibility.

## 2. Governing policy and authority

This architecture is subordinate to the live repository authority records and corpus-wide policies, especially:

- `governance/AUTHORITY_STATE.yaml`;
- `governance/AUTHORITY_SCOPE.json`;
- `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`;
- `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`;
- `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md`;
- `governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`.

The canonical first-read surface remains `../CURRENT_STATE_AND_CORPUS_MAP.md`.

The continuing integration branch `series/ascendance-of-a-bookworm` is a working publication surface. GitHub `main` remains current analytical authority until a reviewed branch state is integrated.

## 3. Source model

The current architecture is Japanese-light-novel primary and is bound to the audited 2026-08-30 inventory:

- numbered main sequence V01-V33;
- five Japanese part divisions preserved in source metadata;
- *Royal Academy Stories: First Year* present as acquired supplemental prose but not yet inserted into the numbered prospective chain.

Source identity, integrity, exclusions, and Drive provenance are governed by `../01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md`.

The following remain separate witnesses unless a later source-lock revision explicitly integrates them:

- anime and manga adaptations;
- translated editions;
- web-publication versions;
- fanbooks/reference works;
- other side stories or retailer bonuses;
- interviews, production material, reception, and fandom sources.

A later witness may test or revise an interpretation without silently changing what the earlier source boundary contained.

## 4. Sequential unit and atomic completion contract

The atomic sequential unit is **one numbered main light-novel volume** unless a separately authorized supplemental transaction is explicitly defined.

A VNN operation is architecturally complete only when all applicable responsibilities are closed:

1. exact source witness and part identity resolved;
2. entering prospective boundary recovered from the prior frozen state;
3. `BOOKWORM_VNN_DEEP_READING.md` completed;
4. material cumulative state propagated to `../03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`;
5. prior claims/predictions adjudicated where the new volume bears on them;
6. newly opened claims, uncertainties, and bounded next-volume expectations recorded;
7. evidence locators retained in the deep reading or promoted to the evidence/index layer when cross-volume retrieval warrants it;
8. `../CURRENT_STATE_AND_CORPUS_MAP.md` advanced to the new committed high-water mark;
9. the exiting state frozen before the next numbered volume is opened.

Writing standalone deep-reading prose without the required cumulative-state updates does not close the source-unit transaction.

Execution scope is separate from analytical architecture. Unless the user explicitly authorizes a bounded continuous run, one request advances one atomic source unit and stops after closeout.

## 5. Day-one longitudinal infrastructure

Before V01, the project initializes one canonical cumulative file:

`../03 Longitudinal Ledgers/BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`

It owns the pre-split cumulative state for the following recurring dimensions:

1. character identity, self-concept, role/status, bodily constraint, competence, and practical agency;
2. relationships, dependence, reciprocity, disclosure, obligation, patronage, conflict, and recipient-conditioned behavior;
3. institutions, class/status, law/custom, enforcement, coercive leverage, and practical freedom;
4. knowledge transfer, literacy, education, production, labor, commerce, diffusion, and unintended consequences;
5. world-model evidence concerning religion, magic/system mechanics, history, politics, economics, and institutional doctrine;
6. focalization, information asymmetry, character knowledge, reader knowledge, secrecy, and epistemic state;
7. ordinary-life evidence when it materially constrains or clarifies character and relationship models;
8. major claims, counterevidence, revision states, and prospective predictions/open questions.

This single-file initialization is intentional. A dimension receives a dedicated ledger only after recurring evidence makes independent retrieval or revision materially easier than maintaining it inside the master ledger.

## 6. Responsibility matrix

| Analytical dimension | Sequential capture | Initial cumulative home | Mature destination | Initialization state |
|---|---|---|---|---|
| Character identity/state/agency | when material | master longitudinal ledger | character monograph and/or integrated synthesis | initialized |
| Relationships/network state | when material | master longitudinal ledger | character, dyadic, ensemble, or specialist synthesis | initialized |
| Institutions/status/law/custom | when material | master longitudinal ledger | institutional/social specialist synthesis | initialized |
| Knowledge/production/education/economy | when material | master longitudinal ledger | knowledge/work/economic specialist synthesis | initialized |
| Religion/magic/world-model claims | when material | master longitudinal ledger | world-model/metaphysical specialist synthesis | initialized |
| Focalization/information state | yes when interpretation depends on it | master longitudinal ledger | character/world-model/final synthesis | initialized |
| Ordinary life/body/risk/competence | when diagnostic | master longitudinal ledger | character and social synthesis | initialized |
| Major claims and revisions | yes for material claims | master longitudinal ledger | specialist + full-series synthesis | initialized |
| Prospective predictions/open questions | every volume boundary | master longitudinal ledger | checkpoint adjudication + historical freeze | initialized |
| Exact source locators/terminology | deep-reading-local initially | deep reading + source lock; promote to `07 Evidence and Indexes` when needed | evidence/index layer | deferred until retrieval pressure exists |
| Character global discovery | not automatic | local character layer first | `characters/registry.jsonl` only after qualifying reviewed analysis exists | deferred |

## 7. Character and relationship synthesis

Dedicated character work is expected for subjects whose longitudinal evidence becomes substantial enough to support an independent reconstruction. Creation is evidence-triggered, not cast-list-triggered.

A character earns an independent canonical home when several of the following are true:

- the model spans multiple source states rather than one local appearance;
- stable tendencies must be separated from development, role effects, recipient effects, or situational effects;
- contradictions or self-report/reception gaps need independent adjudication;
- relationship policies, speech/register, ordinary life, identity transitions, or practical agency require sustained retrieval;
- the character is a major dependency for multiple specialist syntheses;
- a future reconstruction/simulation task would otherwise repeatedly reconstruct the same evidence.

Relationship work may remain inside character monographs or the master ledger until a dyad/network has independent analytical responsibility. A separate relationship synthesis should not be created merely because a relationship is important to the plot.

Global enrollment in `characters/registry.jsonl` remains a separate discovery decision requiring qualifying current evidence.

## 8. Part-boundary checkpoints

The Japanese main series supplies natural architecture-review boundaries:

- Part 1 closes at V03;
- Part 2 closes at V07;
- Part 3 closes at V12;
- Part 4 closes at V21;
- Part 5 closes at V33.

After the final volume of a part freezes, a part-boundary synthesis may be created in `../05 Specialist Synthesis/` if it improves retrieval. Suggested naming:

`BOOKWORM_PARTN_BOUNDARY_SYNTHESIS.md`

A part checkpoint should:

- summarize the current model reached at that boundary;
- adjudicate major predictions and open claims;
- identify architecture gaps or new recurring dimensions;
- record which planned specialist responsibilities have become warranted or should be dropped;
- preserve the underlying volume freezes rather than replacing them.

The first mandatory architecture review is after V03, or earlier if V01-V02 expose a recurring dimension that the master ledger cannot represent responsibly.

## 9. Specialist synthesis responsibilities

`../05 Specialist Synthesis/` is the canonical future home for bounded cross-volume syntheses that have independent retrieval responsibility.

Anticipated domains to test, not predetermined theses, include:

- institutions, status, class, law/custom, patronage, coercion, and practical autonomy;
- literacy, books, education, knowledge transfer, production, labor, commerce, and diffusion;
- religion, doctrine, magic/system mechanics, metaphysical evidence, and world-model revision;
- identity, names/titles/roles, focalization, information asymmetry, and social recognition;
- family, service, mentorship, friendship, patronage, intimacy, obligation, separation, and network change;
- bodily constraint, illness/risk, competence, resources, ordinary life, and the material conditions of agency;
- Japanese prose voice, speech register, titles/forms of address, terminology, and translation-sensitive interpretation;
- part-boundary structural synthesis when the five-part macrostructure itself requires independent treatment.

A candidate domain becomes a required specialist only after repeated evidence and downstream dependence justify it. Later reading may add, combine, narrow, or remove these responsibilities.

## 10. Evidence and locator architecture

Initial evidence routing is deliberately light:

- source-file identity and hash -> source lock / Drive audit manifest;
- passage-level analytical evidence -> the relevant sequential deep reading;
- cumulative claim state -> master longitudinal ledger;
- exact Japanese wording -> retained in bounded form with a locator in the artifact that makes the wording-sensitive claim.

`../07 Evidence and Indexes/` becomes the home for cross-volume retrieval structures when local locators stop being sufficient. Candidate artifacts include:

- `BOOKWORM_PRIMARY_SOURCE_LOCATOR_INDEX.tsv`;
- `BOOKWORM_JAPANESE_TERMINOLOGY_AND_ADDRESS_INDEX.md`;
- `BOOKWORM_ANALYTICAL_COVERAGE_MATRIX.md`;
- a dedicated claim/revision ledger if the master ledger becomes too dense.

Do not duplicate all source checksums or primary-source text in Git. The source audit manifest remains the canonical per-file integrity ledger in the governed evidence plane.

## 11. Claim revision and prospective history

The project uses the established transition vocabulary:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

Every material claim revision should preserve:

- the earlier formulation;
- the source boundary under which it was reasonable;
- the new evidence that tested it;
- the new formulation or uncertainty state;
- the current canonical home.

Later evidence changes the **current model**, not the historical fact that an earlier prospective state had less information.

## 12. Temporal, developmental, epistemic, and continuity state

The architecture must preserve at least these distinctions whenever they matter:

- true/known at VNN versus true/known in the current mature model;
- character knowledge versus reader knowledge;
- statement/belief versus independently corroborated setting fact;
- present behavior versus retrospective explanation;
- private identity/knowledge versus public status/recognition;
- nominal permission versus practical freedom;
- pre-transition versus post-transition name/title/role states;
- numbered-main continuity versus later supplemental/adaptation witnesses.

Do not collapse a long-running character or institution into one timeless final-state description.

## 13. Contradiction routing

Apparent contradictions should be classified before harmonization. Possible causes include:

- focalizer ignorance or bias;
- deception or strategic disclosure;
- status-dependent rules or exceptions;
- later recontextualization;
- terminology/translation variance;
- side-story retrospection;
- institutional doctrine differing from observed mechanism;
- genuine textual inconsistency.

Material unresolved contradictions remain `OPEN` and are routed to the master ledger or a later dedicated audit. Do not solve them by averaging incompatible accounts.

## 14. Dependency graph

The default dependency order is:

```text
Source lock + governing method + synthesis architecture
                    |
                    v
             VNN deep reading
                    |
                    v
          Master longitudinal ledger
                    |
          +---------+----------+
          |                    |
          v                    v
   part-boundary review   character/relationship
          |               promotion when earned
          +---------+----------+
                    |
                    v
          specialist syntheses
                    |
                    v
     architecture/role-gap audit
                    |
                    v
        cross-specialist convergence
                    |
                    v
        full-series synthesis
                    |
                    v
         validation/release audit
```

Evidence/index structures may be promoted in parallel whenever retrieval pressure warrants them.

## 15. Full-series synthesis gate

Sequential completion at V33 does **not** automatically authorize final synthesis.

`../06 Full-Series Synthesis/BOOKWORM_FULL_SERIES_SYNTHESIS.md` becomes eligible only after:

1. V01-V33 are all frozen under the prospective method;
2. the disposition and legitimate insertion boundary of *Royal Academy Stories: First Year* are explicitly resolved, whether integrated or intentionally excluded from a given synthesis scope;
3. the master ledger and any split ledgers are reconciled through the final covered source boundary;
4. a post-sequential architecture/role-gap audit confirms that material specialist responsibilities have been satisfied or explicitly waived with rationale;
5. material character/relationship dependencies required by specialist work are resolved;
6. claim/revision state and major contradictions are stabilized enough that the final synthesis can state uncertainty honestly;
7. required specialist syntheses have converged without unresolved routing conflicts;
8. evidence routes are sufficient to recover the basis of major mature claims.

The final synthesis becomes the preferred integrated interpretation for its declared boundary. It does not supersede frozen sequential readings as historical records of prospective knowledge.

## 16. Reasoning-class routing

Use stable corpus reasoning classes rather than hard-coding a provider model name.

| Operation | Default reasoning class |
|---|---|
| source-lock/locator administration | `BOUNDED_STANDARD` |
| ordinary VNN deep reading | `SUBSTANTIVE_ANALYSIS` |
| interpretive master-ledger update | `SUBSTANTIVE_ANALYSIS` |
| part-boundary checkpoint | `DEEP_SYNTHESIS` |
| mature character/relationship monograph | `DEEP_SYNTHESIS` |
| cross-volume specialist synthesis | `DEEP_SYNTHESIS` |
| architecture/role-gap audit | `DEEP_SYNTHESIS` |
| propagation-sensitive contradiction or claim-revision audit | `PREMIUM_QUALITY_FIRST` when the marginal reliability case is explicit |
| final full-series synthesis | `PREMIUM_QUALITY_FIRST` by default because of corpus-wide propagation sensitivity |

Explicit user instruction or a later architecture revision may override these defaults.

## 17. Architecture extension rule

This architecture is `INITIAL`, not frozen.

Add or split a ledger, evidence structure, character layer, or specialist responsibility when a dimension:

- recurs across multiple source units;
- accumulates evidence independently;
- materially affects later synthesis;
- cannot be represented cleanly in the current home;
- or repeatedly forces reconstruction from scattered deep readings.

Do not add infrastructure merely because another series has it. Do not backfill all earlier volumes unless the newly discovered dimension creates a material evidence gap that cannot be responsibly repaired from the frozen readings and retained source.

Material architecture changes must be recorded in the current corpus map.

## 18. Completion states

The project distinguishes:

1. **INITIALIZATION COMPLETE** — method, architecture, source lock, master ledger, and entrypoint are established; sequential lock may open.
2. **SEQUENTIAL IN PROGRESS** — V01-V33 advancing one frozen source unit at a time.
3. **SEQUENTIAL COMPLETE** — V33 frozen; this is not yet full-series readiness.
4. **LONGITUDINAL RECONCILIATION COMPLETE** — cumulative state and split ledgers reconciled through the final boundary.
5. **SPECIALIST READY / IN PROGRESS** — required specialist responsibilities established and executing.
6. **FULL-SERIES READY** — role-gap audit and convergence gates passed.
7. **VALIDATED / RELEASED** — integrated synthesis and required audits complete.
8. **FROZEN** — an explicitly release-locked generation; later structural change requires a successor rather than silent mutation.

## 19. Current initialization decision

At architecture generation V0.1:

- source reconnaissance: complete for the audited Japanese EPUB boundary;
- governing analytical method: present;
- synthesis architecture: present;
- required day-one longitudinal infrastructure: initialized as one master ledger;
- dedicated character/relationship homes: deferred until evidence earns them;
- dedicated cross-volume evidence indexes: deferred until retrieval pressure exists;
- sequential high-water mark: pre-V01;
- next sequential operation: Japanese-primary Volume 01 deep reading;
- first architecture review: after V03 or earlier on a material architecture trigger.
