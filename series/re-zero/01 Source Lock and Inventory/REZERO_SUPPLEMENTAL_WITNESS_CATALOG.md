---
series: RE_ZERO
artifact_type: supplemental_witness_catalog
scope: NON_SPINE_BIBLIOGRAPHIC_AWARENESS_AND_HORIZON_ROUTING
generation: V0.1
status: canonical
release_state: mutable_active
analytical_opening_state: CLOSED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — supplemental witness catalog

## 0. Responsibility and non-authority

This is the canonical bibliographic-awareness and horizon-routing surface for Re:Zero material outside the numbered Japanese main-light-novel spine. It prevents “not yet acquired” from being confused with “does not exist” while preserving the prospective reading boundary.

Cataloging is not source admission, analytical opening, or canon transfer:

`CATALOGED ≠ ACQUIRED ≠ ADMITTED ≠ SAFE_TO_OPEN ≠ CONSUMED`

The source lock remains the authority for exact acquired-object identity, hashes, provenance, and admission. `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` remains the authority for witness class and horizon logic. Analytical readings of admitted non-spine material belong in `03 Supplemental and Alternate Witnesses/`.

No narrative content was opened to create this catalog. Titles, dates, and existence claims may be recorded only from governed source metadata, official bibliographic evidence, or paratext already lawfully opened inside an admitted source.

## 1. Catalog state vocabulary

| State | Meaning |
|---|---|
| `FAMILY_AWARENESS_ONLY` | a witness family is known as a routing category; no item-level existence claim is made |
| `KNOWN_UNACQUIRED` | item-level bibliographic existence is established, but no governed source object is present |
| `ACQUIRED_UNAUDITED` | an object is present but identity/integrity is not yet sufficient for admission |
| `AUDITED_NOT_CLASSIFIED` | exact object identity is established, but witness role or horizon is unresolved |
| `CLASSIFIED_HORIZON_OPEN` | role is classified, but one or more material horizon dependencies remain unresolved |
| `ADMITTED_NOT_SAFE` | source lock admits the object, but `H_final` has not been reached |
| `SAFE_TO_OPEN` | admission and all material horizons permit the bounded analytical operation |
| `CONSUMED` | an authorized analysis has opened the witness and records its resulting artifact |
| `EXCLUDED_OR_DUPLICATE` | the object is not an independent usable witness; the reason must be recorded |

Only the source lock may establish `ADMITTED_NOT_SAFE` or `SAFE_TO_OPEN`. Only a completed analytical transaction may establish `CONSUMED`.

## 2. Required item fields

Every item-level row records, when knowable without narrative opening:

- stable catalog ID;
- exact displayed title and script;
- witness family and provisional source role;
- edition/container relationship;
- official publication date or bounded ordering evidence;
- acquisition and integrity state;
- `H_pub`, `H_diegetic`, `H_route`, and conservative `H_final`;
- provenance route;
- duplicate/alternate-edition relationship;
- analytical disposition and next safe action;
- unresolved identity or dependency questions.

An unresolved material dependency forces `H_final: OPEN`. Unknowns are not filled from fandom memory, synopsis sites, adaptation recall, or model memory.

## 3. Current item-level catalog

| catalog ID / title | family and publication relationship | acquisition / integrity | provisional role and classification | horizons | analytical opening | provenance and next action |
|---|---|---|---|---|---|---|
| `RZ-SUP-SSC-014-JA`<br>`Ｒｅ：ゼロから始める異世界生活　短編集１４` | short-story collection, collection volume 14; component/container relationships unaudited; official Japanese publication date `2026-07-24` | `KNOWN_UNACQUIRED` / `NOT_APPLICABLE_UNTIL_ACQUIRED` | `SUPPLEMENTAL_MAINLINE_PENDING_ITEM_CLASSIFICATION` | `H_pub: AFTER_V45_FREEZE`<br>`H_diegetic: OPEN`<br>`H_route: N/A`<br>`H_final: OPEN` | `CLOSED` | Existence/date already established in the governed source lock from the official `https://www.re-zero.com/books/` catalog. Do not acquire, admit, or open under this catalog entry alone; item-level contents and dependencies require a later bounded audit. |

The catalog intentionally makes no content claim about Short Story Collection 14.

## 4. Unresolved paratext lead

| lead ID | evidence already available | unresolved fields | disposition |
|---|---|---|---|
| `RZ-LEAD-V03-PREVIEWED-SERIAL-STORY` | V03 paratext announces a separately published serial story positioned as following the estate story | exact title, edition/container, source object, publication order, witness class, diegetic placement, route dependency, and safe horizon | `UNRESOLVED_LEAD_ONLY`; remain unopened and do not collapse it into the Short Story Collection 14 entry or any remembered title |

A lead is not an item-level catalog claim beyond the bounded paratext evidence stated here.

## 5. Witness-family awareness register

| Family | Current catalog posture | Required classification before opening |
|---|---|---|
| EX and other named supplemental volumes | `FAMILY_AWARENESS_ONLY` | exact edition, relationship to main LN, publication and diegetic horizons |
| short-story collections | one item cataloged; family otherwise `FAMILY_AWARENESS_ONLY` | item/component identity, original publication, container duplication, horizon per component where needed |
| shop, special-edition, event, and campaign bonuses | `FAMILY_AWARENESS_ONLY` | exact text identity, distribution provenance, duplication/reprint chain, safe horizon |
| serialized or separately published mainline side stories | one unresolved V03 paratext lead; otherwise `FAMILY_AWARENESS_ONLY` | title, source object, serialization/container relation, diegetic and publication dependency |
| IF / alternate-route prose | `FAMILY_AWARENESS_ONLY` | divergence condition, route identity, `H_route`, and transfer prohibition |
| developmental web novel | `FAMILY_AWARENESS_ONLY` | version identity, chapter boundary, LN relation, and wording-separation rule |
| guidebooks, interviews, author notes, and other paratext | `FAMILY_AWARENESS_ONLY` | speaker, publication context, authority type, and whether the evidence is bibliographic, authorial, or diegetic |
| games and other interactive works | `FAMILY_AWARENESS_ONLY` | route/ending identity, authorship/official status, mechanics of player choice, and cross-witness role |
| anime and other audiovisual adaptations | `FAMILY_AWARENESS_ONLY` | exact season/episode/release, adaptation role, audiovisual evidence route, and prose non-substitution |

This register is corpus awareness, not an assertion that every possible family contains relevant or obtainable material.

## 6. Duplicate and container discipline

A story may appear in a periodical, shop bonus, web release, collection, revised collection, or translated edition. Do not count containers as independent narrative evidence without checking identity and revision.

Where a component-level audit becomes necessary, assign stable component IDs and record:

- first verified publication;
- every acquired container;
- exact or materially revised duplication status;
- the controlling Japanese witness for wording;
- per-component horizon when a collection mixes placements;
- the one analytical reading that later containers route to.

## 7. Promotion and maintenance rule

Update this catalog when official bibliographic evidence or a governed acquisition establishes a new item, identity correction, container relationship, or horizon fact. Do not browse or open narrative material merely to make the catalog look complete.

An item moves toward analysis only through this chain:

1. item-level existence and identity become sufficiently specific;
2. a governed source object is acquired;
3. source lock verifies identity, integrity, edition, and provenance;
4. witness protocol assigns role and all material horizons;
5. the requested analytical operation reaches `H_final`;
6. a bounded witness-specific reading is created in `03 Supplemental and Alternate Witnesses/`;
7. any cross-witness transfer is explicitly argued and labeled.

Until those gates are satisfied, the safe action is catalog maintenance and abstention.
