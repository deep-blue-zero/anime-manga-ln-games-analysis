---
series: RE_ZERO
artifact_type: corpus_map
scope: SERIES_BOOTSTRAP_AND_ANALYTICAL_ROUTING
generation: V0.4
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:ZERO -Starting Life in Another World- — current state and corpus map

This is the canonical first read for the Git-side Re:Zero analytical corpus.

## Authority split

- **GitHub is the analytical authority** for methods, source-routing decisions, sequential readings, longitudinal ledgers, character analysis, adaptation analysis, specialist synthesis, and analytical audits promoted under `series/re-zero/`.
- **Primary-source media do not belong in this Git root.** Japanese light-novel files, audiovisual media, scans, extracted text, and other source-bearing objects remain in the governed evidence plane unless a policy explicitly admits a reference representation.
- **The current source lock admits the acquired Japanese main-light-novel spine V01-V43.** Exact file identity, integrity, Drive provenance, alternate-edition handling, and known current acquisition gaps are recorded in `01 Source Lock and Inventory/REZERO_SOURCE_LOCK_AND_INVENTORY.md`. The lock does not claim complete-to-date possession: published Japanese V44 and V45 are not present in the audited Drive manifest.
- Local workspaces are working environments, not authority, until an artifact is promoted through the governed Git route.

## Current analytical state

**The acquired Japanese main-LN range V01-V43 is source-locked, and the prospective Japanese-primary Volume 01 and Volume 02 deep readings are now frozen and canonical at `02 Sequential Readings/REZERO_LN_V01_DEEP_READING.md` and `02 Sequential Readings/REZERO_LN_V02_DEEP_READING.md`. Volume 03 has not been opened analytically. No character monograph, standalone specialist synthesis, PACTRIH placement, adaptation judgment, or full-series synthesis is canonical here yet.**

The governed Drive audit admits one continuous Japanese main-volume sequence V01-V43. A 2026-09-04 official-publication freshness check establishes V44 and V45 as published but absent from that audited acquisition. This does not block prospective work at the beginning of the series; it means the repository must not describe the source corpus as complete-to-date, and V44-V45 must be acquired and audited before the sequential reading reaches them.

The architecture remains intentionally conservative because Re:Zero has multiple source families that can contaminate one another if treated as a single undifferentiated canon pool. Main light novels, mainline supplemental stories, alternate-route/IF material, web-novel material, and anime adaptation evidence must remain separately labeled witnesses until a specific analytical operation compares them. The current audited source folder admits no supplemental, IF/alternate-route, web-novel, or audiovisual witness.

The first two interpretive operations are complete. `REZERO_LN_V01_DEEP_READING.md` freezes four local event-states and 24 V01 claim IDs. `REZERO_LN_V02_DEEP_READING.md` carries those claims forward through explicit revision operations, freezes four mansion event-states (`V02-E1` through `V02-E4`), 30 stable V02 claim IDs (`RZ-V02-C001` through `RZ-V02-C030`), and the bounded V03 question set. V02 ends after Subaru's deliberate death and an unidentified liminal scene; no subsequent restoration is assumed. The next permitted numbered operation is to record the V03 pre-reading horizon from the V02 freeze and then open only admitted Japanese witness `RZ-MAIN-LN-JA-V03`.

## Governing method

Read in this order for new Re:Zero analytical work:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/REZERO_ANALYTICAL_METHOD.md`
3. `00 Frameworks and Methods/REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`
4. `01 Source Lock and Inventory/REZERO_SOURCE_LOCK_AND_INVENTORY.md`
5. the relevant frozen sequential reading(s), once they exist;
6. only the longitudinal, character, supplemental, adaptation, or specialist artifact needed for the task.

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
| `00 Frameworks and Methods` | Governing evidence, prospective-freeze, route-state, witness-separation, focalization, Japanese-language, safe-horizon, and revision rules | populated; analytical method V0.1; witness protocol V0.2 |
| `01 Source Lock and Inventory` | Exact admitted witness set, integrity/provenance, edition identity, publication ordering, and source-family classification | V01-V43 Japanese `MAIN_LN` admitted; V44-V45 known acquisition gaps; V01-V02 consumed into frozen prospective analysis |
| `02 Sequential Readings` | Main-light-novel volume-by-volume prospective deep readings and source-verified arc checkpoints | V01 and V02 deep readings frozen/canonical; V03 is next and remains unopened |
| `03 Supplemental and Alternate Witnesses` | Mainline side stories, collections, EX/supplemental material, IF/alternate routes, web-novel witnesses, and other non-spine material | routing contract populated; no witness admitted yet |
| `04 Longitudinal Ledgers` | Recurring route/event-state, knowledge, relationship, character-state, institution, mechanics, and ordinary-life tracking once promotion thresholds are met | schema contract populated; no ledger promoted yet; V01-V02 state remains recoverable from the frozen volume files |
| `05 Character Analysis` | Character reconstruction only after sufficient longitudinal evidence exists | routing contract populated; no monographs yet |
| `06 Adaptation Analysis` | Anime and later audiovisual comparison as separately labeled witnesses | routing contract populated; no adaptation findings yet |
| `07 Specialist Synthesis` | Dense questions with independent retrieval responsibility, instantiated only when earned | not instantiated |
| `08 Audits and Manifests` | Bootstrap and later analytical/source-integrity manifests | bootstrap manifest populated; detailed source audit remains Drive-authoritative |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of an unused directory is intentional. Re:Zero should grow by analytical responsibility, not by template symmetry.

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

## Initial work order

1. Treat both frozen sequential readings as immutable historical prospective states. V01 remains the original prior; V02 owns the current V01→V02 revision state and must not retroactively rewrite V01.
2. Before opening Volume 03 analytically, instantiate its pre-reading horizon from V02 Sections 13, 14, and 16: carry the V01 revision table, preserve all 30 V02 claim IDs, and record the bounded unresolved questions without importing V03 answers.
3. Read only admitted Japanese witness `RZ-MAIN-LN-JA-V03`, produce `02 Sequential Readings/REZERO_LN_V03_DEEP_READING.md`, and freeze its explicit `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` operations against the V02 current state.
4. V02 author paratext describes V02 as `問題提起編`, V03 as `解決編`, and the unit as the `屋敷の物語`. After V03 is frozen, evaluate whether the source evidence has earned a structural checkpoint and whether recurring event-state/knowledge responsibilities now justify a separate ledger; do not invent an arc name merely from fandom convention.
5. Continue prospectively through the admitted main-LN spine; create later checkpoints only after source evidence establishes the boundary and the final contributing volume is frozen.
6. Acquire and integrity-audit Japanese V44 and V45 before the sequential reading reaches that boundary; admission is not implied by their bibliographic existence.
7. Do not open supplemental or alternate-route material merely to construct a bibliography. When a witness is acquired, assign its source class and `H_pub`/`H_diegetic`/`H_route`/`H_final` state before reading it analytically.
8. Promote longitudinal ledgers only when recurring responsibilities become costly or unreliable to reconstruct from frozen volume files.
9. Create character monographs only after enough cross-state and longitudinal evidence exists to distinguish stable tendency, local state, recipient effect, role effect, and genuine revision.
10. Treat anime and other adaptations as distinct witnesses whose performance, direction, framing, omission, compression, and reordering can be analyzed without replacing the light-novel model.

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
