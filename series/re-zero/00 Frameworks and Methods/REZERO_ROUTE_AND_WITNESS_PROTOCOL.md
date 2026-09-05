---
series: RE_ZERO
artifact_type: witness_protocol
scope: ROUTE_EVENT_STATE_AND_CROSS_VERSION_EVIDENCE_CONTROL
generation: V0.2
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — route, event-state, and witness protocol

## 1. Responsibility

This protocol prevents analytical collapse among event-states and source families. It controls **where evidence is allowed to travel**.

It is deliberately stricter than a normal chronology guide because Re:Zero analysis can become circular if the reader blends knowledge from later volumes, superseded sequences, side stories, alternate routes, the web novel, and the anime into a single timeless character/world model.

## 2. Witness classes

Every admitted source-bearing object should receive one primary witness class:

- `MAIN_LN` — numbered published Japanese light novel in the governing main spine;
- `SUPPLEMENTAL_MAINLINE` — source-verified mainline side story, short-story collection, EX/supplemental volume, bonus story, or comparable material whose relation to the main route is established;
- `ALTERNATE_ROUTE` — IF or other source explicitly operating as an alternate/counterfactual route rather than an event in the governing main spine;
- `DEVELOPMENTAL_WN` — web-novel text treated as a distinct textual/version witness;
- `ANIME_ADAPTATION` — audiovisual adaptation evidence;
- `OTHER_ADMITTED` — another witness with a separately documented analytical role.

Do not assign a witness class from filename intuition alone. Source identity and relation must be verified in the inventory.

## 3. Source-horizon rule

A witness may be acquired without being analytically opened.

Every non-spine witness receives a horizon tuple before prospective reading:

- **`H_pub` — publication-safe horizon.** The greatest numbered main-LN volume whose official publication date is on or before the witness's first publication date. This prevents a prequel or side story published late in the franchise from leaking later-established information into an earlier prospective freeze merely because its events occur earlier.
- **`H_diegetic` — diegetic dependency horizon.** The latest main-volume state whose characters, relationships, institutions, terminology, world knowledge, or events the witness demonstrably presupposes. Determine this from source/publisher metadata or a controlled placement audit; do not read through an unopened witness just to force a placement.
- **`H_route` — route/divergence horizon.** For `ALTERNATE_ROUTE`, the latest main-volume state needed to establish the divergence premise or route conditions without importing later main-route knowledge.
- **`H_final` — earliest safe opening point.** The latest established dependency among `H_pub`, `H_diegetic`, and `H_route`.

If a potentially material dependency is unknown, `H_final` is `OPEN`, even when `H_pub` is known.

A safe horizon controls **when the witness may be opened**, not what it is allowed to prove. Witness-class transfer rules still apply after opening.

### 3.1 Conservative rules

- A story set chronologically in the past is not therefore safe to read early. Publication horizon still constrains it.
- A compilation inherits the publication horizon of the compilation unless each component's earlier publication identity and exact textual continuity are separately verified.
- A revised/reprinted story inherits the later witness's horizon unless exact equivalence to an earlier admitted text is established.
- A same-day supplement/main-volume release may use that main volume in `H_pub`; prospective practice still reads/freezes the numbered main volume first.
- A publisher blurb may establish bibliographic or broad placement metadata, but its narrative claims are not source findings about the primary text.
- If placement requires spoilers to resolve, defer the witness instead of sacrificing the prospective freeze.

### 3.2 Alternate-route / IF horizon

For an IF or other explicit counterfactual witness:

`H_final = max(H_pub, H_route, H_diegetic)` when all relevant components are known.

The divergence point can be much earlier than publication. The later publication horizon still dominates if the IF was written after later main volumes.

Opening an IF after `H_final` authorizes only route-bounded counterfactual analysis. It does not merge its events into main-route continuity.

### 3.3 Current worked bibliographic check

The 2026-09-04 source audit found no supplemental witness in the acquired Re:Zero Drive manifest. Official bibliographic metadata does, however, establish `Ｒｅ：ゼロから始める異世界生活　短編集１４` as a 2026-07-24 publication, after main LN V45 on 2026-06-25.

If that exact collection is later acquired, its initial `H_pub` is therefore `AFTER_V45_FREEZE`. `H_diegetic` remains unassigned until a controlled placement audit, so its current `H_final` is `OPEN`.

This is a test of the rule, not an exhaustive supplemental bibliography.

## 4. Event-state identity

When repeated or branching sequences matter, assign a local identifier sufficient to distinguish them inside the current reading. The identifier should encode only what the reader at that horizon can safely know.

A useful minimal record is:

| Field | Meaning |
|---|---|
| `witness` | admitted source witness |
| `volume_or_item` | stable source item identity |
| `arc` | source-verified arc identity if available |
| `event_state` | local repeated/branch state identifier |
| `focalizer` | viewpoint-bearing character or narration mode |
| `knowledge_delta` | material information gained/lost/revealed |
| `relationship_delta` | material trust/disclosure/dependence change |
| `outcome` | local consequence without assuming global durability |
| `carry_forward` | what evidence or experience demonstrably persists, if anything |

The schema is analytical metadata, not a claim that the fiction uses these labels.

## 5. Active-world fact versus observed-state fact

Use different propositions for different responsibilities:

- `OBSERVED_STATE_FACT`: happened in the depicted state/witness;
- `ACTIVE_STATE_FACT`: established in the currently active narrative state;
- `RETAINED_EXPERIENCE`: demonstrably carried by a character or narrator across states;
- `READER_KNOWLEDGE`: learned by the reader even when unavailable to characters;
- `COUNTERFACTUAL_ROUTE_FACT`: established only in an alternate-route witness.

Never convert one class into another implicitly.

## 6. Behavioral transfer across states

A repeated choice under comparable conditions can support a stronger stable-tendency inference. A choice made under unique knowledge, coercion, despair, trust, injury, social pressure, or route-specific history may remain state-bound.

Before transferring behavior, compare:

- information;
- goals;
- emotional/stress state;
- relationships;
- status and coercive constraints;
- available resources;
- immediate threats;
- prior experiences demonstrably retained;
- opportunity for reflection or rehearsal.

State the conditional if the conditions matter.

## 7. Relationship asymmetry

For each important dyad, distinguish:

- A's remembered relationship history;
- B's remembered relationship history;
- current mutual history;
- reader-observed prior-state interactions;
- secrets or information held by only one party;
- obligations that exist socially versus obligations felt privately.

This avoids describing intimacy, betrayal, trust, or repair as symmetrical when the evidence is not symmetrical.

## 8. Causal credit and rehearsal effects

A successful later outcome may depend on information or rehearsal acquired in prior failed states. When assigning causal credit, separate:

- direct contribution in the successful state;
- knowledge imported from earlier states;
- sacrifices or observations that enabled that knowledge;
- allies whose behavior was elicited differently because the focal character changed strategy;
- luck or changed external conditions.

Do not give a single character total causal credit merely because they integrate information across states.

## 9. Mainline supplemental material

A `SUPPLEMENTAL_MAINLINE` witness may update the main-route model only after:

1. source identity is verified;
2. its route relation is established;
3. diegetic/publication placement is sufficiently known for the intended use;
4. the prospective horizon permits reading it;
5. the analysis states which existing claims it preserves, strengthens, revises, downgrades, rejects, or leaves open.

A side story can be highly authoritative within its scope without being safe to read early.

## 10. Alternate-route / IF material

Alternate-route material is valuable primarily for **bounded counterfactual analysis**.

It can support claims such as:

- a behavior is possible for this character under the route's conditions;
- a pressure point or latent tendency becomes visible when circumstances diverge;
- a relationship or institution behaves differently when a specific premise changes.

It cannot by itself establish:

- that the main-route character remembers those events;
- that an alternate-route relationship exists in the main route;
- that a route-specific choice is a timeless personality essence;
- that route-specific world events occurred in the main route;
- that main-route moral responsibility includes acts committed only in an alternate witness.

Comparative counterfactual claims should name the divergence conditions whenever known.

## 11. Web-novel material

Treat `DEVELOPMENTAL_WN` as a version witness, not a secret source of unprinted light-novel facts.

Use it for questions such as:

- textual development;
- scenes or explanations added, removed, reordered, or rewritten;
- characterization or mechanics differences between versions;
- how adaptation from web publication to light novel changes emphasis.

Do not use web-novel wording to settle a light-novel wording dispute. Do not fill a missing light-novel volume with web-novel content while labeling the result a light-novel reading.

## 12. Anime adaptation

`ANIME_ADAPTATION` evidence is authoritative for the anime witness: performance, timing, blocking, editing, sound, music, visual framing, and the anime's own presented wording.

Cross-witness comparison should distinguish:

- faithful retention;
- compression;
- omission;
- expansion;
- reordering;
- changed focalization;
- changed ambiguity;
- audiovisual interpretation not present in prose.

Anime-only evidence cannot silently overwrite a light-novel claim.

## 13. Translation witnesses

Translations can accelerate navigation and provide a useful comparison surface, but Japanese remains the semantic anchor for admitted light-novel evidence.

When a translation materially affects interpretation:

1. quote or identify the relevant Japanese locus;
2. identify the translation witness;
3. explain the semantic difference rather than simply choosing a preferred wording;
4. preserve ambiguity when the Japanese remains ambiguous.

## 14. Cross-witness comparison matrix

| From | To main-LN model? | Default rule |
|---|---|---|
| `MAIN_LN` earlier volume | yes | prospective revision rules apply |
| `SUPPLEMENTAL_MAINLINE` | conditionally | only after verified scope and safe insertion |
| `ALTERNATE_ROUTE` | no direct merge | counterfactual/conditional inference only |
| `DEVELOPMENTAL_WN` | no direct merge | version-comparison evidence only |
| `ANIME_ADAPTATION` | no direct merge | adaptation-comparison evidence only |
| translation | no silent merge | convenience witness; Japanese adjudicates wording-sensitive claims |

## 15. Abstentions

When route relation, placement, continuity, or source identity is unclear, record the uncertainty. Do not solve it with wiki chronology, fandom labels, or remembered canon while presenting the result as source-derived.

A disciplined `OPEN` state is analytically superior to a falsely unified chronology.
