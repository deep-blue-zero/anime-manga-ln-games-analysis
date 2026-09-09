---
series: RE_ZERO
artifact_type: synthesis_architecture
scope: JAPANESE_LIGHT_NOVEL_PROSPECTIVE_LONGITUDINAL_AND_SYNTHESIS_ARCHITECTURE
generation: V1.1
status: canonical
release_state: mutable_active
architecture_lifecycle: EVOLVING
source_boundary: "Japanese main light novel V01-V43 admitted; prospective analysis frozen through V03; V44-V45 known acquisition gaps; non-spine witnesses excluded until separately admitted"
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
reasoning_policy: MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md
pro_justification: "Propagation-sensitive architecture repair: this routing governs every later Re:Zero volume transaction and synthesis layer."
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — synthesis and corpus architecture

## 0. Authority and repair boundary

This document is the canonical synthesis/corpus architecture for the existing Re:Zero analytical project under `series/re-zero/`. It governs where source-facing observations accumulate, how claims and state remain recoverable across volume freezes, when specialist work earns an independent home, and what must converge before later synthesis.

It does not replace the source-facing rules in `REZERO_ANALYTICAL_METHOD.md` or the transfer restrictions in `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`. The paired foundation is:

- the analytical method defines **what to notice and how to judge evidence**;
- this architecture defines **where the resulting state goes and what it must eventually support**.

For character work, `REZERO_CHARACTER_RECONSTRUCTION_PROTOCOL.md` supplies the detailed reconstruction and fidelity responsibilities under this architecture. For non-spine corpus awareness, `01 Source Lock and Inventory/REZERO_SUPPLEMENTAL_WITNESS_CATALOG.md` records known candidates without admitting or opening them.

The project began before the later corpus-wide project-initiation architecture gate was enforced. V01 and V02 are already frozen prospective readings. This architecture is therefore `EVOLVING`, not `INITIAL`: it repairs a missing governing role around adequate preexisting work. It neither supersedes nor retrospectively rewrites the frozen readings. Its initial longitudinal state is an explicitly labeled backfill from those readings.

Higher-level dependencies are:

- `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`;
- `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md`;
- `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md`;
- `governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`;
- the repository authority, integration, branch-lifecycle, and housekeeping controls named by root `AGENTS.md`.

This architecture is governance and routing, not literary evidence. If it conflicts with later repository governance, the current repository policy governs. If a source claim conflicts with this architecture's anticipation, the source may justify an architectural amendment; the architecture may not dictate the literary conclusion.

## 1. Purpose and governed scope

The active analytical generation is a Japanese-primary, prospective, volume-by-volume reading of the numbered published light novel. The currently admitted main-spine boundary is V01-V43. V44 and V45 are published acquisition gaps and are not part of the authorized V03-V43 continuous run.

This architecture has five purposes:

1. preserve the reader's exact evidentiary horizon after each numbered volume;
2. keep active-world, superseded-state, retained-experience, reader-knowledge, and alternate-witness propositions distinct;
3. maintain one current cumulative state without mutating frozen prospective history;
4. route mature evidence into character, relationship, institutional, mechanics, linguistic, adaptation, or other specialist work only when earned;
5. make checkpoint, completion, and recovery decisions deterministic from repository state.

The numbered Japanese light novel is the only witness class authorized for the current sequential transaction stream. Supplemental mainline prose, IF/alternate routes, developmental web-novel text, translations, anime, games, interviews, and other paratext remain separate witness classes. Their acquisition does not authorize opening or cross-source transfer.

## 2. Source model and witness topology

### 2.1 Governing spine

`MAIN_LN` Japanese numbered volumes advance the primary prospective high-water mark. Every volume keeps its global `VNN` identity. Source-verified macrostructure may be added as metadata or a checkpoint label; fandom arc numbering must not be used to manufacture a boundary.

The source lock owns admission, exact identity, edition, provenance anchor, integrity evidence, and safe opening order. A changed file hash, replacement edition, missing object, or ambiguous identity pauses only the affected source unit until a bounded audit resolves it; an earlier verified volume freeze remains valid.

### 2.2 Non-spine witnesses

Non-spine material is routed by `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`:

- `SUPPLEMENTAL_MAINLINE` may update the main-route model only within verified scope after `H_final` permits opening;
- `ALTERNATE_ROUTE` supports route-local facts and bounded counterfactual comparison, never silent main-route biography;
- `DEVELOPMENTAL_WN` supports version-development comparison, never substitute light-novel wording;
- `ANIME_ADAPTATION` supports the anime's audiovisual and adaptation choices, never source-prose claims;
- translations remain navigation/comparison witnesses, with Japanese controlling wording-sensitive main-LN claims;
- `OTHER_ADMITTED` requires a declared role before use.

For every non-spine witness, `H_pub`, `H_diegetic`, `H_route` where applicable, and conservative `H_final` must be recoverable before analytical opening. An unresolved material dependency keeps `H_final: OPEN`.

### 2.3 Paratext

Afterwords, colophons, publisher metadata, and other paratext inside or attached to an admitted volume may establish bibliographic identity or authorial framing. They must be labeled as paratext and do not become narrator-certified diegetic fact.

## 3. Canonical corpus roles and retrieval route

The canonical entrypoint is `series/re-zero/CURRENT_STATE_AND_CORPUS_MAP.md`. A future analyst reads in this order:

1. the current corpus map;
2. `REZERO_ANALYTICAL_METHOD.md`;
3. this synthesis architecture;
4. `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` when event-state or cross-witness routing matters;
5. `REZERO_CHARACTER_RECONSTRUCTION_PROTOCOL.md` for character promotion, reconstruction, or fidelity work;
6. `REZERO_SUPPLEMENTAL_WITNESS_CATALOG.md` when non-spine discovery or acquisition is in scope;
7. `REZERO_SOURCE_LOCK_AND_INVENTORY.md` for the next exact admitted source;
8. `REZERO_MASTER_LONGITUDINAL_LEDGER.md`;
9. the immediately prior frozen volume's claim ledger and outbound question horizon;
10. only the additional specialist or witness-specific artifact required for the operation.

The retrieval chain for a mature claim is:

`corpus map -> master ledger current row -> claim ancestry / relevant frozen VNN reading -> exact internal EPUB locus -> admitted hashed witness`.

The master ledger is the cumulative canonical home. Frozen VNN readings are the authority for what the reader knew at each historical volume boundary and for the exact source-facing argument recorded there. Neither role displaces the other.

## 4. Atomic numbered-volume completion contract

A numbered volume is the atomic sequential operation. A draft deep reading alone does not advance the high-water mark.

### 4.1 Entering state

Before opening `VNN`:

1. fetch and resolve the live stable branch and current corpus map;
2. confirm the last **verified committed** volume and that no partial next transaction is being mistaken for a freeze;
3. read the governing method, architecture, master ledger, and any promoted specialist ledger relevant to `VNN`;
4. read the prior frozen claim ledger and outbound questions;
5. record a bounded `VNN` pre-reading horizon without later-volume answers;
6. resolve the exact admitted source ID, file identity, hash, language, and integrity state;
7. keep `VNN+1` and every later narrative witness unopened.

### 4.2 Source-facing outputs

The VNN deep reading must meet the method's quality floor and, where evidenced, preserve:

- scene/chapter structure and focalization;
- event-state identity and active/superseded durability;
- reader, Subaru, and other-character knowledge states;
- retained and non-retained information;
- character, relationship, role, information, and stress-conditioned change;
- institutions, factions, status, law/custom, patronage, coercion, resources, and practical agency;
- mechanics propositions with speaker/source confidence, observed regularities, costs, and exceptions;
- ordinary-life baselines where diagnostic;
- Japanese wording, register, address, and locator evidence where semantically material;
- counterevidence, rival readings, and falsifiers;
- explicit predecessor-claim adjudication and stable new claim IDs.

### 4.3 Closeout gate

Before `VNN+1` may be opened, all applicable responsibilities must be complete in one atomic transaction:

1. create and freeze `REZERO_LN_VNN_DEEP_READING.md` with `artifact_type: sequential_deep_reading`;
2. adjudicate materially affected prior claims as `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`;
3. assign new IDs under the `RZ-VNN-CNNN` grammar;
4. update the master ledger's claim state, event-state, knowledge, relationship, character, institution, mechanics, ordinary-life, terminology, and readiness responsibilities;
5. update any separately promoted ledger without duplicating canonical ownership;
6. freeze the bounded VNN+1 question/prediction horizon;
7. update the corpus map and source-consumption state;
8. run the repository-prescribed staged-index author preflight;
9. commit exactly the complete volume path set under approved identity;
10. verify the committed tree, normal remote publication, exact remote readback, housekeeping state, and exact-SHA audit state required by current policy.

Only the last verified committed transaction advances `committed_high_water_mark`. Continuous authorization changes cadence, not this closeout standard.

## 5. Longitudinal infrastructure

### 5.1 Promoted day-one cumulative home

`04 Longitudinal Ledgers/REZERO_MASTER_LONGITUDINAL_LEDGER.md` is required infrastructure from the architecture-repair boundary onward. Its creation after V02 is an explicit repair/backfill event; it is not represented as having governed V01 or V02 prospectively.

The master ledger initially owns:

- current claim state and revision ancestry;
- route/event-state history and durability class;
- knowledge provenance and information asymmetry;
- relationship state and remembered-history asymmetry;
- character developmental, role, information, recipient, and stress state;
- institutions, factions, status, resources, power, and practical agency;
- mechanics/world-model propositions and confidence;
- analytically diagnostic ordinary life and preferences;
- Japanese terminology/register observations when longitudinally diagnostic;
- prospective questions and predictions;
- readiness flags for character, relationship, checkpoint, and specialist promotion.

The ledger records current state compactly and routes to exact evidence rather than duplicating every argument from a deep reading. A material revision preserves ancestry; current wording may change while the prior frozen claim remains discoverable.

### 5.2 Specialist-ledger promotion

The master ledger is not a permanent ban on specialization. A dimension earns a dedicated ledger only when it has an independent retrieval/revision burden that the master can no longer represent safely—for example, many interacting event states, a dense knowledge-holder network, or a mechanics model with numerous exceptions.

When splitting a responsibility:

1. name the new canonical home and its exact scope;
2. backfill only the current state and material history necessary for independent use;
3. leave a routing row in the master ledger;
4. update this architecture and the corpus map in the same bounded architectural transaction;
5. stop maintaining full duplicate current-state tables in both files.

No ledger is created for symmetry. A dimension may remain local to one VNN reading when it does not recur or affect downstream work.

`04 Longitudinal Ledgers/REZERO_LEDGER_PROMOTION_AND_SCHEMAS.md` registers the exact candidate filenames and their dimension-specific thresholds. The post-V03 review in Section 14 records the current disposition of every candidate; none is promoted at this boundary.

## 6. Evidence and locator routing

The exact hashed EPUB remains outside Git. Git stores provenance-safe source IDs, hashes, compact wording evidence, and internal locators.

- Every frozen main-volume reading owns its detailed source locus convention and source-facing evidence trail.
- The master ledger cites volume sections and/or exact internal XHTML loci for current load-bearing rows.
- Short Japanese quotation is retained only when wording itself matters; large copyrighted passages are prohibited.
- A dedicated evidence/index layer is deferred until cross-volume retrieval becomes materially unreliable. Its reserved but uninstantiated directory is `09 Evidence and Indexes/`.
- Candidate `09 Evidence and Indexes/REZERO_CLAIM_EVIDENCE_INDEX.md` is promoted only when claim-to-locus routing repeatedly spans enough frozen volumes or specialists that the master-ledger and VNN routes become error-prone. It maps claims and revisions to evidence; it does not restate conclusions.
- Candidate `09 Evidence and Indexes/REZERO_LOCATOR_INDEX.md` is promoted only when repeated use of heterogeneous internal EPUB, audiovisual, or supplemental locators makes witness-local conventions insufficient. It maps a stable analytical locator to volume, source ID, internal locus, and relevant tags; it does not become a source lock.
- Candidate `09 Evidence and Indexes/REZERO_CHARACTER_EVIDENCE_MATRIX.md` is promoted only when enough characters approach mature reconstruction that comparing ordinary-life, adverse, failure, relationship, recipient, knowledge, event-state, voice, role, competence, counterevidence, and endpoint coverage materially improves readiness review. It exposes gaps; it does not promote readiness.
- Candidate `09 Evidence and Indexes/REZERO_WITNESS_DEPENDENCY_INDEX.md` is promoted only when many admitted non-spine items have interacting publication, diegetic, route, container, or duplication dependencies that the supplemental catalog can no longer retrieve safely. It does not admit witnesses or decide transfer.
- Source inventory and integrity metadata remain in the source lock and governed external audit records; analytical files do not duplicate raw acquisition evidence.
- Adaptation timestamps, frames, performance, and audio observations remain in the adaptation layer when that witness class is admitted.

Every mature specialist claim must be traceable to a current ledger row or frozen reading and from there to an admitted source locus. “Known from the series” and model memory are not evidence routes.

## 7. Temporal, developmental, epistemic, and event-state model

Every cumulative proposition is indexed as needed by:

- source horizon (`VNN` or bounded witness horizon);
- event-state/route;
- durability class (`OBSERVED_STATE_FACT`, `ACTIVE_STATE_FACT`, `RETAINED_EXPERIENCE`, `READER_KNOWLEDGE`, or `COUNTERFACTUAL_ROUTE_FACT`);
- holder and source of knowledge;
- evidence class (`DIRECT`, `CORROBORATED INFERENCE`, `INTERPRETIVE HYPOTHESIS`, or `OPEN`);
- character conditioning: development, information, relationship/recipient, role/status, and stress/situation.

A superseded-state event can remain evidence of what a character did under those conditions without becoming active-world history. A remembered relationship can be ethically or psychologically consequential for Subaru without being mutual history. A later explanation can revise the current mechanics model without making an earlier speaker retrospectively knowledgeable.

Behavior transfers across states only after comparing information, goals, stress, recipient, status, coercion, resources, retained experience, and opportunity. Conditional evidence stays conditional.

## 8. Claim revision, current authority, and supersession

Frozen volume claim IDs never disappear. Later volumes adjudicate them with the six-state transition vocabulary.

The master ledger keeps, for every material current claim:

- stable current claim ID;
- current formulation and evidence class;
- predecessor ID(s) or `NEW`;
- latest transition operation;
- current source horizon;
- canonical evidence route;
- counterevidence or unresolved condition.

`REVISE`, `DOWNGRADE`, and `REJECT` never authorize editing the predecessor freeze. They change the cumulative current state while retaining the old formulation and transition route. `OPEN` is a valid durable state, not a failure to decide.

If a mutable architecture, ledger, or synthesis is replaced, the successor and prior artifact must state their supersession relationship under the archive policy. Frozen readings and frozen checkpoints are historical authority for their bounded horizons and are not silently made noncurrent merely because later synthesis exists.

## 9. Cross-source conflict and contradiction routing

Apparent contradiction is classified before harmonization. Candidate causes include:

- different event states or routes;
- different character knowledge, deception, ignorance, doctrine, or propaganda;
- changed focalization or unreliable/self-interested account;
- later textual correction or expanded evidence;
- translation or wording variation;
- edition/revision difference;
- supplemental retrospection;
- web-novel/light-novel version divergence;
- adaptation compression, reordering, performance, or original material;
- genuine unresolved inconsistency.

The responsible VNN reading or specialist artifact records the competing propositions, scopes, and evidence. Material impact triggers a claim transition; unresolved causation remains `OPEN`. A witness may be authoritative for its own wording/performance while ineligible to alter the main-LN model directly.

Prospective contamination is itself an audit issue. If later knowledge is accidentally encountered, the affected proposition is quarantined and excluded from the earlier freeze unless independently supported within the permitted horizon.

## 10. Character and relationship synthesis responsibility

The project expects later character monographs and may earn relationship/ensemble syntheses, but neither is created from importance or popularity alone. `REZERO_CHARACTER_RECONSTRUCTION_PROTOCOL.md` is the controlling detailed contract; this section owns architectural routing and promotion only.

A character earns an independent canonical home when the accumulated source can distinguish most of:

- stable tendencies from bounded phases;
- information, recipient/relationship, role/status, and stress effects;
- self-conception from observed social effect;
- ordinary-life baseline from crisis behavior;
- relationship and disclosure policies;
- route/event-state consistency and divergence;
- Japanese voice/register where material;
- contradictions, counterevidence, negative controls, and operational abstentions.

A relationship earns an independent synthesis when its remembered histories, disclosures, power, obligations, ruptures, repairs, or non-mutual continuity create recurring analytical work not safely owned by the relevant character monographs and master-ledger row.

Readiness values are `NOT_READY`, `ACCUMULATING`, `CHECKPOINT_READY`, and `MONOGRAPH_READY` or `SPECIALIST_READY`. Advancement requires cited evidence and may be downgraded if later source shows the apparent pattern was state-bound. The first `MONOGRAPH_READY` promotion must pass the separate fidelity audit defined by the character reconstruction protocol before reusable-model status. Local monographs do not authorize edits to `characters/registry.jsonl` or `CHARACTER_ANALYSIS_INDEX.md`.

## 11. Specialist synthesis responsibilities

At V02 no standalone specialist is mandatory. The following responsibilities are **anticipated candidates**, to be promoted only when recurrence and independent synthesis burden are demonstrated:

- memory, identity, continuity, and asymmetric experience;
- relationship continuity under non-mutual memory;
- restoration, agency, responsibility, sacrifice, and constrained disclosure;
- mechanics/metaphysics/world-model reconstruction;
- institutions, political legitimacy, royal-selection status, patronage, law, and coercion;
- trauma/stress/risk and practical agency without unsupported diagnosis;
- Japanese prose voice, address, titles, naming, register, and translation-sensitive meaning;
- genre literacy and narrative self-modeling;
- ordinary life, labor, comfort, routine, and domesticity as character reconstruction evidence;
- adaptation divergence, performance, music, sound, and visual grammar after audiovisual witnesses are admitted.

A candidate becomes mandatory for full-series readiness only when an architecture review records that final integration cannot responsibly answer its recurring claims from ledgers and character work alone. A later review may merge or retire a candidate that the source does not earn.

## 12. Dependency graph and integration order

```text
current governance + admitted source lock
        |
        v
analytical method + synthesis architecture
        |
        v
frozen VNN prospective reading
        |
        v
master longitudinal current state
        |
        +--> promoted specialist ledgers when independently necessary
        |
        +--> character / relationship readiness and monographs
        |
        +--> claim, evidence, terminology, and locator stabilization
        |
        v
source-verified checkpoints + required specialist syntheses
        |
        v
cross-specialist contradiction and dependency reconciliation
        |
        v
full-series synthesis readiness review
        |
        v
10 Full-Series Synthesis/REZERO_FULL_SERIES_SYNTHESIS.md
        |
        v
validation / release audit -> freeze
```

Claim/evidence stabilization precedes any synthesis that depends on the disputed claims. Character monographs may begin when their own threshold is met, but a final character model waits for the relevant sequential and relationship state. Adaptation work cannot become an input to main-LN literary conclusions without an explicit cross-witness comparison stage.

`07 Specialist Synthesis/` remains the canonical home for earned domain, relationship, and cross-witness specialists. The separately named future canonical full-series home is `10 Full-Series Synthesis/REZERO_FULL_SERIES_SYNTHESIS.md`. Neither the directory nor file is instantiated until a readiness review establishes a complete-series source boundary or an expressly named bounded corpus and confirms that required specialists have converged. Exhaustion of the currently admitted V43 range does not equal published-series completion.

## 13. Responsibility matrix

| Analytical dimension | Sequential observation | Cumulative canonical home | Mature/final destination | State through V03 |
|---|---|---|---|---|
| Claims and revisions | material claims, counterevidence, six-state adjudication | master ledger claim tables | relevant specialists and full-series synthesis | master current through V03; claim-evidence index deferred |
| Route/event-state | local state, trigger, outcome, durability, carry-forward | master ledger event-state tables | memory/continuity or mechanics specialist if earned | master sufficient through V03 |
| Knowledge/asymmetry | holder, source, confidence, nonholder, consequence | master ledger knowledge table | relationship, agency, and continuity syntheses | master sufficient through V03 |
| Relationships | each party's remembered history, trust, disclosure, dependency, power | master ledger relationship table | character monographs; dyadic/ensemble synthesis if earned | master sufficient through V03 |
| Character state/stress | goals, self-model, conditions, behavior, recovery, counterexample | master ledger character/readiness tables | protocol-governed character monographs/models | accumulating; no monograph ready through V03 |
| Institutions/factions/power | rule/doctrine, actor behavior, capacity, resources, status, coercion | master ledger institution table | institutional/political specialist if earned | dedicated home deferred with trigger |
| Mechanics/world model | speaker theory, observation, cost, exception, corroboration | master ledger mechanics table | mechanics/metaphysics specialist if earned | master sufficient through V03 |
| Ordinary life/preferences | only model-diagnostic routines, tastes, labor, comfort, low-stakes conduct | master ledger ordinary-life table | character/relationship or ordinary-life specialist if earned | dedicated home deferred with trigger |
| Japanese wording/register | wording-sensitive terms, address, titles, pragmatic shifts, exact locus | master ledger terminology table plus VNN evidence loci | language/register specialist; character and translation analysis | dedicated home deferred with trigger |
| Prospective questions | bounded falsifiers/predictions before next volume | master ledger open-question register and prior VNN freeze | next VNN adjudication; checkpoints | V04 horizon frozen |
| Source identity/locators | source ID, hash, locus convention | source lock plus VNN reading; ledger routes only | evidence/index layer if retrieval burden earns it | not currently warranted |
| Character/relationship/specialist readiness | cited accumulation and threshold judgment | master ledger readiness tables | promoted canonical artifacts | initialized; nothing ready through V03 |
| Supplemental/IF/WN | catalog awareness only; no opening until admission and safe horizon | supplemental catalog + source lock + witness protocol; later witness-specific reading | bounded cross-witness specialist | catalog initialized; no witness admitted |
| Anime/adaptation | no observation until source admission | adaptation source lock/readings when created | adaptation specialists and bounded comparison | `NO_WITNESS_ADMITTED` |

An observation omitted from cumulative state is intentionally local only when the VNN reading explains that it neither recurs nor affects later claims. Material evidence may not be left without a retrieval destination.

## 14. Architecture extension and review rule

This architecture is expected to evolve. Review it:

- after V03-V05 if those volumes expose recurring dimensions not safely represented here;
- at every source-verified major-arc boundary;
- when a new witness class is admitted;
- when a master-ledger section becomes costly or ambiguous to retrieve or revise;
- before major character or relationship syntheses;
- after V43 sequential exhaustion;
- before specialist convergence and before full-series synthesis.

A material amendment records: trigger, affected responsibility, old and new canonical homes, required backfill, dependency consequences, reasoning-class change if any, corpus-map update, and validation result. Backfill is limited to material evidence needed to repair the responsibility; it does not authorize cosmetic re-reading or alteration of frozen artifacts.

### Post-V03 candidate review

The V03 closeout supplied enough evidence to test architectural pressure but not enough independent retrieval burden to justify a split. These dispositions govern until a later review changes them:

| Candidate responsibility | Disposition through V03 | Concrete later trigger |
|---|---|---|
| event-state / route | `RETAIN IN MASTER` | promote if interacting loops/routes require an independently maintained chronology or carry-forward matrix |
| knowledge / information asymmetry | `RETAIN IN MASTER` | promote if proposition-holder-nonholder networks and disclosure revisions become unsafe to retrieve as one compact table |
| relationship continuity | `RETAIN IN MASTER` | promote if multiple dyads require maintained asymmetric histories, rupture/repair chains, or cross-dyad comparison |
| mechanics / metaphysics | `RETAIN IN MASTER` | promote if competing explanations, costs, exceptions, and revision ancestry become independently dense |
| institution / faction / power | `DEFER WITH TRIGGER` | promote when royal-selection actors, rules, resources, patronage, enforcement, and faction divergence need their own maintained model |
| ordinary life / preferences | `DEFER WITH TRIGGER` | promote when cross-character low-stakes evidence becomes too recurrent for character monographs and the master table |
| Japanese voice / register / terminology | `DEFER WITH TRIGGER` | promote when recurring speaker- and recipient-conditioned wording shifts exceed witness-local evidence plus the master terminology table |
| character reconstruction readiness | `RETAIN IN MASTER` | promote a readiness ledger only when many candidates require cross-horizon audit scheduling that cannot be maintained compactly; monographs still follow the character protocol |
| locator / evidence index | `NOT CURRENTLY WARRANTED` | promote only after repeated cross-volume or cross-witness retrieval failures demonstrate a separate navigation burden |

No dedicated ledger, evidence index, character monograph, or specialist synthesis is created by this review.

## 15. Completion gates

The project distinguishes:

1. **atomic volume completion** — one VNN reading and all cumulative state are frozen, committed, and verified;
2. **authorized sequential-run completion** — V03-V43 are individually complete or the run ends at a genuine blocker;
3. **admitted-source exhaustion** — every currently admitted numbered main-LN witness is processed;
4. **longitudinal reconciliation** — master and promoted ledgers have no unprocessed material transitions through that boundary;
5. **specialist readiness** — architecture review identifies and completes every specialist responsibility required by the reached source;
6. **full-series synthesis readiness** — source boundary, claim/evidence state, character/relationship work, specialists, and contradictions have converged sufficiently for the explicitly named synthesis scope;
7. **validation/release completion** — the exact final tree and remote audit pass and a release/freeze is deliberately declared.

V43 can satisfy the authorized run without satisfying published-series completion because V44/V45 remain outside the acquired/admitted boundary. No final full-series synthesis begins merely because the current source inventory is exhausted.

## 16. Stable reasoning-class assignments

| Operation | Stable class | Escalation rule |
|---|---|---|
| architecture repair, extension, and architecture role-gap audit | `PREMIUM_QUALITY_FIRST` | default because errors propagate through the full project |
| ordinary Japanese-primary VNN deep reading | `SUBSTANTIVE_ANALYSIS` | escalate for unusual contradiction, source defect, or state complexity |
| interpretive master-ledger update | `SUBSTANTIVE_ANALYSIS` | escalate to `DEEP_SYNTHESIS` for broad retrospective rerouting |
| checksum, locator, inventory, and deterministic metadata work | `ROUTINE_FAST` or `BOUNDED_STANDARD` | escalate when edition/source identity is interpretively ambiguous |
| source-verified arc/checkpoint synthesis | `DEEP_SYNTHESIS` | premium only for propagation-sensitive contested freezes |
| mature major-character monograph | `DEEP_SYNTHESIS` | premium for central cases with high contradiction/state density |
| difficult relationship or specialist synthesis | `DEEP_SYNTHESIS` | premium only with explicit marginal-reliability justification |
| final claim reconciliation, architecture/role-gap audit, full-series synthesis | `PREMIUM_QUALITY_FIRST` | default quality-first boundary |

Literal provider/model names remain a time-bounded mapping owned by the corpus-wide reasoning policy and are not durable architectural ontology.

## 17. Mutable, frozen, and generated behavior

Mutable current-state artifacts:

- `CURRENT_STATE_AND_CORPUS_MAP.md`;
- this `EVOLVING` architecture until explicitly stabilized/frozen;
- `REZERO_CHARACTER_RECONSTRUCTION_PROTOCOL.md`, ledger-schema contracts, and directory routers;
- `REZERO_SOURCE_LOCK_AND_INVENTORY.md`;
- `REZERO_SUPPLEMENTAL_WITNESS_CATALOG.md`;
- `REZERO_MASTER_LONGITUDINAL_LEDGER.md` and later promoted current ledgers;
- readiness tables and non-frozen specialist drafts.

Frozen artifacts:

- each completed `REZERO_LN_VNN_DEEP_READING.md`;
- source-verified checkpoint freezes once declared;
- the historical bootstrap manifest;
- bounded repair/update manifests with `release_state: frozen_record`.

Generated global routing outputs are owned only by repository housekeeping. Character registry/index outputs are owned only by character curation. Neither may be manually edited during ordinary Re:Zero work. Primary-source files, extracted copyrighted text, private acquisition evidence, and unreviewed binaries remain outside Git.

Mutable documents use targeted verified edits and preserve material history. Frozen documents change only through an explicit correction/supersession transaction authorized by stronger governance; a later interpretation normally updates the current ledger instead.

## 18. Recovery and next-operation determination

After interruption or ambiguous publication:

1. fetch live `origin/main` and `origin/series/re-zero`;
2. read the current corpus map and master ledger;
3. inspect recent commits and remote status;
4. locate the last exact volume whose complete transaction is committed and verified;
5. inspect whether the next reading or mutable ledger was partially written;
6. resolve branch, source, or prospective-contamination ambiguity before new source reading;
7. resume at the first unclosed volume within the authorized terminal boundary.

Conversational memory never advances state. A drafted file, local commit, push success message, earlier green audit, or housekeeping-pending source commit is not the same as a verified completed transaction.

## 19. Initial repair decision

The V01 and V02 freezes already repeat claim revision, event-state, knowledge, relationship, character, institution, mechanics, ordinary-life, and terminology responsibilities. Reconstructing them for every later volume would be costly and error-prone. They therefore cross the promotion threshold for one proportional master ledger at this repair boundary.

No evidence at V02 yet requires seven independent ledgers, a character monograph, a relationship specialist, or a thematic/metaphysical final synthesis. Those remain readiness decisions governed by recurrence, contradiction density, and independent retrieval responsibility.

## 20. Post-V03 architecture-extension decision

At the first safe boundary after V03 publication, the architecture gained two responsibilities that were under-specified but now safely definable without reading V04: a dedicated character-reconstruction protocol and a non-spine bibliographic-awareness catalog. The existing master ledger remains proportional, so all specialist-ledger candidates were reviewed and deliberately left unpromoted.

The amendment also reserves exact future homes for evidence/index artifacts and the full-series synthesis without instantiating empty directories or files. Frozen V01, V02, and V03 readings remain unchanged; the analytical horizon and sequential high-water mark remain V03.
