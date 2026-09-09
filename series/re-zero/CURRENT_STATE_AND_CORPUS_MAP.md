---
series: RE_ZERO
artifact_type: corpus_map
scope: SERIES_BOOTSTRAP_AND_ANALYTICAL_ROUTING
generation: V0.6
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:ZERO -Starting Life in Another World- — current state and corpus map

This is the canonical first read for the Git-side Re:Zero analytical corpus.

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: EVOLVING
  governing_method: 00 Frameworks and Methods/REZERO_ANALYTICAL_METHOD.md
  synthesis_architecture: 00 Frameworks and Methods/REZERO_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - 04 Longitudinal Ledgers/REZERO_MASTER_LONGITUDINAL_LEDGER.md
  sequential_analysis_lock: OPEN
```

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: main_light_novel_volume
  authorized_start: V03
  terminal_boundary: V43
  committed_high_water_mark: V03
  next_candidate_operation: V04
  confirmation_between_units: false
  run_state: paused_by_user
  pause_boundary: after_verified_V03_publication
```

## Authority split

- **GitHub is the analytical authority** for methods, source-routing decisions, sequential readings, longitudinal ledgers, character analysis, adaptation analysis, specialist synthesis, and analytical audits promoted under `series/re-zero/`.
- **Primary-source media do not belong in this Git root.** Japanese light-novel files, audiovisual media, scans, extracted text, and other source-bearing objects remain in the governed evidence plane unless a policy explicitly admits a reference representation.
- **The current source lock admits the acquired Japanese main-light-novel spine V01-V43.** Exact file identity, integrity, Drive provenance, alternate-edition handling, the bounded post-manifest V41 hash override, and known current acquisition gaps are recorded in `01 Source Lock and Inventory/REZERO_SOURCE_LOCK_AND_INVENTORY.md`. The lock does not claim complete-to-date possession: published Japanese V44 and V45 are not present in the live governed folder.
- Local workspaces are working environments, not authority, until an artifact is promoted through the governed Git route.

## Current analytical state

**The acquired Japanese main-LN range V01-V43 is source-locked, and the prospective Japanese-primary Volume 01 through Volume 03 deep readings are frozen and canonical. The source-verified V02–V03 estate-story checkpoint is also frozen. Volume 04 and the separately previewed non-spine story remain analytically unopened. The sequential run is paused at the user's post-V03 boundary. No character monograph, standalone specialist synthesis, PACTRIH placement, adaptation judgment, or full-series synthesis is canonical here yet.**

The later project-initiation architecture gate is satisfied prospectively. `REZERO_SYNTHESIS_ARCHITECTURE.md` is the canonical `EVOLVING` synthesis architecture, and `REZERO_MASTER_LONGITUDINAL_LEDGER.md` is the required cumulative home promoted and backfilled from the unmodified V01/V02 freezes, then advanced through V03. `SEQUENTIAL_ANALYSIS_LOCK = OPEN`, but the user-requested execution pause controls: no V04 source-facing work begins until the user resumes the run.

The governed source audit admits one continuous Japanese main-volume sequence V01-V43. A live 2026-09-08 rescan found no V44/V45 or other new source, reproduced 44 of 45 manifest objects exactly, and re-audited the sole post-manifest replacement, Japanese V41, under its current exact hash. A 2026-09-04 official-publication freshness check establishes V44 and V45 as published but absent from that acquisition. This does not block the authorized V03-V43 run; it means the repository must not describe the source corpus as complete-to-date.

The architecture remains intentionally conservative because Re:Zero has multiple source families that can contaminate one another if treated as a single undifferentiated canon pool. Main light novels, mainline supplemental stories, alternate-route/IF material, web-novel material, and anime adaptation evidence must remain separately labeled witnesses until a specific analytical operation compares them. The current audited source folder admits no supplemental, IF/alternate-route, web-novel, or audiovisual witness.

The first three interpretive operations are complete. `REZERO_LN_V01_DEEP_READING.md` freezes four local event-states and 24 V01 claim IDs. `REZERO_LN_V02_DEEP_READING.md` carries those claims forward through explicit revision operations, freezes four mansion event-states (`V02-E1` through `V02-E4`), 30 stable V02 claim IDs, and the bounded V03 question set. `REZERO_LN_V03_DEEP_READING.md` adjudicates all 30 V02 claims and all 26 V03 questions, confirms a surviving fifth-day mansion state, freezes 35 V03 claim IDs and 24 bounded V04 questions, and preserves the exact consumed Japanese witness identity. `REZERO_ARC_ESTATE_STORY_CHECKPOINT.md` records the source-verified V02–V03 structural break without inventing a formal arc ID. V04 is the next candidate only after resumption.

## Governing method and retrieval route

Read in this order for new Re:Zero analytical work:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/REZERO_ANALYTICAL_METHOD.md`
3. `00 Frameworks and Methods/REZERO_SYNTHESIS_ARCHITECTURE.md`
4. `00 Frameworks and Methods/REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`
5. `01 Source Lock and Inventory/REZERO_SOURCE_LOCK_AND_INVENTORY.md`
6. `04 Longitudinal Ledgers/REZERO_MASTER_LONGITUDINAL_LEDGER.md`
7. the immediately prior frozen sequential reading's claim ledger and outbound question set;
8. only the additional character, supplemental, adaptation, promoted-ledger, or specialist artifact required for the task.

The intended primary semantic anchor is the **Japanese light novel**, within the exact admitted source range. Translations may be convenience witnesses; wording-sensitive claims return to Japanese. Anime, web-novel material, IF/alternate routes, side stories, bonus stories, game material, guidebooks, interviews, and other supplements do not silently overwrite main-light-novel findings.

## Why Re:Zero needs a route-aware method

The project must preserve more than ordinary chronology. Whenever the text presents repeated, reset, branching, failed, counterfactual, or otherwise non-identical event states, analysis must keep separate:

- what occurred in a particular event-state or iteration;
- what remains true in the currently active narrative state;
- what a focal character remembers or has learned across states;
- what other characters locally know in that state;
- what the reader has learned from states that characters may not share;
- which behaviors repeat under similar conditions and which depend on changed information;
- what later success owes to information, sacrifice, rehearsal, coercion, luck, or altered circumstances from earlier attempts.

A discarded or superseded event-state can remain highly probative character evidence without being treated as a durable event in the active world-state. Conversely, a later successful sequence does not erase the experiential or interpretive importance of earlier failures for any character whose state actually carries forward.

## Corpus architecture

| Layer | Analytical responsibility | Current state |
|---|---|---|
| `00 Frameworks and Methods` | Governing evidence, prospective-freeze, route-state, witness-separation, focalization, Japanese-language, safe-horizon, revision, longitudinal-routing, specialist, and completion rules | populated; analytical method V0.1; witness protocol V0.2; synthesis architecture V1.0 `EVOLVING` |
| `01 Source Lock and Inventory` | Exact admitted witness set, integrity/provenance, edition identity, publication ordering, and source-family classification | V01-V43 Japanese `MAIN_LN` admitted; V41 current hash point-audited after manifest drift; V44-V45 known acquisition gaps; V01-V03 consumed into frozen prospective analysis |
| `02 Sequential Readings` | Main-light-novel volume-by-volume prospective deep readings and source-verified arc checkpoints | V01-V03 deep readings and the V02–V03 estate-story checkpoint frozen/canonical; V04 remains unopened |
| `03 Supplemental and Alternate Witnesses` | Mainline side stories, collections, EX/supplemental material, IF/alternate routes, web-novel witnesses, and other non-spine material | routing contract populated; no witness admitted yet |
| `04 Longitudinal Ledgers` | Current claims/revisions, route/event-state, knowledge, relationship, character-state, institution, mechanics, ordinary-life, terminology, prospective questions, and readiness | master ledger V1.1 current through V03; schema contract retains later split thresholds; no dedicated ledger yet promoted |
| `05 Character Analysis` | Character reconstruction only after sufficient longitudinal evidence exists | routing contract populated; no monographs yet |
| `06 Adaptation Analysis` | Anime and later audiovisual comparison as separately labeled witnesses | routing contract populated; no adaptation findings yet |
| `07 Specialist Synthesis` | Dense questions with independent retrieval responsibility, instantiated only when earned | not instantiated |
| `08 Audits and Manifests` | Bootstrap and later analytical/source-integrity manifests | bootstrap manifest populated; detailed source audit remains Drive-authoritative |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of an unused directory is intentional. Re:Zero should grow by analytical responsibility, not by template symmetry.

## Architecture repair provenance and sequential lock

The Re:Zero Git-native root was created and V01/V02 were frozen before enforcement of the current initiation validator. After merging live `origin/main` into the stable branch, the role-gap audit found a complete analytical method and witness protocol but no separately recoverable synthesis/corpus architecture and no promoted cumulative current-state home despite repeated longitudinal responsibilities.

The repair therefore:

- preserves the historical bootstrap manifest and both frozen readings unchanged;
- creates `REZERO_SYNTHESIS_ARCHITECTURE.md` as the canonical `EVOLVING` architecture;
- promotes one proportional `REZERO_MASTER_LONGITUDINAL_LEDGER.md` rather than seven empty or competing ledgers;
- backfills only the state already established by V01/V02;
- marks the routing descriptor `project_initiation_gate: REQUIRED`;
- records the bounded audit in `08 Audits and Manifests/REZERO_ARCHITECTURE_REPAIR_MANIFEST.md`.

All initiation requirements are now initialized. The sequential lock is affirmatively **OPEN**. The repair preceded V03; V03 is now frozen, and the user-requested pause keeps V04 unopened.

## Reasoning-class routing

- architecture repair, final role-gap review, and full-series integration: `PREMIUM_QUALITY_FIRST`;
- ordinary Japanese-primary VNN deep reading and interpretive master-ledger update: `SUBSTANTIVE_ANALYSIS`;
- deterministic source identity, checksum, locator, and metadata maintenance: `BOUNDED_STANDARD` or `ROUTINE_FAST`;
- source-verified checkpoints, mature character work, and difficult relationship/specialist synthesis: normally `DEEP_SYNTHESIS`, with evidence-based escalation for unusually propagation-sensitive cases.

The stable class governs; literal provider/model names remain a mutable mapping in the corpus-wide reasoning policy.

## Main reading methodology

The numbered main light novels use a **prospective freeze**:

1. establish the exact source witness and current analytical horizon;
2. record material expectations, unresolved questions, and confidence before opening the next volume;
3. read only the newly admitted source increment;
4. identify what the new volume preserves, strengthens, revises, downgrades, rejects, or leaves open;
5. write a bounded deep reading rather than a chapter transcript;
6. freeze that state before advancing.

Where an official/source-verified arc structure exists, preserve both global volume identity and arc identity. Do not infer or hard-code arc boundaries from fandom memory when the locked corpus can establish them directly.

## Supplemental and alternate witnesses

Non-spine material is not inserted merely because it is available.

Before reading a supplement analytically, establish:

- exact witness identity and source family;
- publication order;
- diegetic or route relationship to the main light novel where knowable;
- the earliest safe analytical insertion point relative to the prospective main-volume horizon;
- whether the item is mainline supplemental evidence, alternate-route/counterfactual evidence, a developmental web-novel witness, an adaptation witness, or something else.

The witness protocol now separates publication horizon (`H_pub`), diegetic dependency (`H_diegetic`), and route/divergence dependency (`H_route`). The safe opening point `H_final` is the latest established dependency. If a material dependency is unresolved, `H_final` remains `OPEN` and the witness stays unread.

Alternate-route material may illuminate constraints, latent tendencies, or counterfactual possibilities, but it does not prove that the same choice would occur in the main route under materially different knowledge, relationships, or conditions.

## Initial analytical questions — not findings

The sequential pass should test rather than assume questions including:

- how repeated failure, partial success, and accumulated information change judgment, self-conception, planning, risk tolerance, and interpersonal behavior;
- which character tendencies remain stable across materially different event-states and which are products of local information or pressure;
- how asymmetric knowledge changes trust, consent, persuasion, deception, dependency, and apparent irrationality;
- how relationships develop when continuity may be experienced differently by the participants;
- how fear, grief, shame, hope, exhaustion, attachment, obligation, and trauma alter practical agency without being reduced to generic pathology labels;
- how institutions, factions, status, law, custom, patronage, violence, and material resources constrain nominal choices;
- which setting explanations are demonstrated, which are viewpoint-bound, which are institutional doctrine, and which remain unresolved;
- how abilities, rules, costs, exceptions, and hidden mechanisms should be reconstructed without converting character theory into world fact;
- how Japanese register, address terms, self-reference, politeness, insults, emotional formulae, and recurring lexical choices change interpretation;
- where ordinary routines, food, work, study, leisure, humor, gifts, comfort, etiquette, and low-stakes choices reveal durable character structure;
- which later conclusions genuinely revise earlier models and which merely add information unavailable at the earlier freeze.

## Current work order

1. Treat both frozen sequential readings as immutable historical prospective states. V01 remains the original prior; V02 owns the historical V01→V02 revision transaction and must not retroactively rewrite V01.
2. Preserve the completed V03 transaction as its own prospective state: it owns the V02→V03 revisions, 35 current claims, the V04 horizon, and the source-verified V02–V03 estate-story checkpoint.
3. Keep V04 and the previewed non-spine story unopened while the user pause is active. On resumption, load the frozen V03 horizon before opening only admitted Japanese witness `RZ-MAIN-LN-JA-V04`.
4. Continue prospectively through the admitted main-LN spine; create later checkpoints only after source evidence establishes the boundary and the final contributing volume is frozen.
5. Acquire and integrity-audit Japanese V44 and V45 before the sequential reading reaches that boundary; admission is not implied by their bibliographic existence.
6. Do not open supplemental or alternate-route material merely to construct a bibliography. When a witness is acquired, assign its source class and `H_pub`/`H_diegetic`/`H_route`/`H_final` state before reading it analytically.
7. Update the master longitudinal ledger in every volume transaction; promote a dedicated ledger only when one responsibility develops an independent retrieval/revision burden, then leave routing rather than a competing full copy in the master.
8. Create character monographs only after enough cross-state and longitudinal evidence exists to distinguish stable tendency, local state, recipient effect, role effect, and genuine revision.
9. Treat anime and other adaptations as distinct witnesses whose performance, direction, framing, omission, compression, and reordering can be analyzed without replacing the light-novel model.

## Bootstrap abstentions

- No synopsis, wiki, fandom consensus, adaptation memory, prior ChatGPT discussion, or model knowledge is promoted as a Re:Zero source finding by this scaffold.
- No later volume, supplement, alternate route, or adaptation is allowed to contaminate an earlier prospective freeze.
- No failed/discarded event-state is automatically treated as a durable active-world event; no active-world reset automatically erases its evidentiary value for character reconstruction.
- No character's explanation of mechanics, history, politics, religion, another person's motives, or hidden causality is treated as objective fact solely because it is explicit dialogue or narration.
- No IF/alternate-route evidence is silently blended into main-route personality claims.
- No web-novel wording is treated as the light novel's wording.
- No anime-only performance or staging is attributed to the light novel.
- No PACTRIH score or cross-series ethical placement is assigned before source-grounded evidence is sufficient.
- No character registry edit is implied by creating this analytical root; character discovery remains under the repository's separate curation authority.
