---
title: "Tokyo 7th Sisters — Evidence Substrate And Locator Protocol"
artifact_id: T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL
artifact_type: evidence_locator_protocol
series: Tokyo 7th Sisters
generation: V1
version: "1.121"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "c20260909-r484; preserved offline Japanese game; analysis integrated through T7S_B0217; complete source-lock JSON and two logical coverage roles maintained through checked manifest-bound physical components"
architecture_lifecycle: EVOLVING
created: 2026-09-09
last_updated: 2026-10-30
---

# Tokyo 7th Sisters evidence substrate and locator protocol

Current route: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Governing pair: [T7S_ANALYTICAL_METHOD.md](T7S_ANALYTICAL_METHOD.md) and [T7S_SYNTHESIS_ARCHITECTURE.md](T7S_SYNTHESIS_ARCHITECTURE.md). Source recovery: [T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md](T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md).

Section letters retained from the approved design are cross-document references: E/P = [source and locator protocol](T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md); F = [topology](../01%20Sources%20and%20Chronology/T7S_TOPOLOGY_AND_CHRONOLOGY.md); G/H/I/N/O = [reading method](T7S_ANALYTICAL_METHOD.md); J/K/M/R/S/U/X/Y/Z = [synthesis architecture](T7S_SYNTHESIS_ARCHITECTURE.md); L = [reconstruction protocol](T7S_CHARACTER_RECONSTRUCTION_PROTOCOL.md) (monograph promotion is owned by the synthesis architecture); V/T = [bootstrap and gate record](../09%20Audits%20and%20Manifests/T7S_BOOTSTRAP_AND_GATE_RECORD.md). B01–B13 identify the architecture’s bootstrap inventory, not source IDs.

## E. Source/witness authority model

**Decision:** admit sources by witness, edition, scope, and capability. Source class alone does not settle continuity or make every statement by a character true.

| Class | Initial/admission state | Supports | Boundary |
| --- | --- | --- | --- |
| `GAME_STORY` | Preserved Main/Sub/Event and narrative additional scripts | Events, causal structure, development, dialogue, relationships | A dream, performance, recollection, or unreliable statement retains that mode |
| `GAME_SUPPLEMENTAL` | Native card/character/home/stage messages with conditions and identities retained | Ordinary behavior, speech, tastes, relational address, persona | A repeatable UI utterance is not automatically a dated unique event or historical relationship milestone |
| `GAME_PRESENTATION` | Sprites, backgrounds, CGs, cards, UI, movies, native commands | Presentation, iconography, staging, branding | Resource availability and native references do not prove exact playback |
| `LYRICS_GAME_MASTER` | The 215 nonempty master entries, individually identified | Wording as stored in the game; song/persona analysis | Not presumed complete studio lyrics, sung alignment, or autobiographical character testimony |
| `SONG_RECORDING` / `MUSIC_VIDEO` | Admit exact game/studio/MV edition when relevant | Performed music, arrangement, audiovisual form | Keep mixes, edits, artists, performances, and narrative speakers separate |
| `ANIME_ADAPTATION` | Future admission of the film/edition and its evidence derivatives | That adaptation's story and performance | No automatic overwrite of game events or game character knowledge |
| `LIVE_PERFORMANCE` | Future exact performance/date/recording | Performer embodiment, staging, public presentation | Actor behavior is not direct evidence of fictional private behavior |
| `OFFICIAL_PARATEXT` | Scoped announcements, profiles, commentary | Release anchors, official framing, production claims | Intention and publicity do not overrule what the story presents |
| `SECONDARY_REFERENCE` | Clearly attributed, bounded use | Chronology leads and external reference facts | Confirm load-bearing chronology where possible; fan orders stay recommendations |

Within a witness, retained native source bytes and verified transformations ground claims. Normalized JSON, transcripts, SQLite, the browser, and generated packets are retrieval projections. Corrections route back to native evidence; a convenient derivative cannot overrule it. Runtime capture governs runtime observations within its recorded build, branch, and settings. Conflicting witnesses remain separate records with an explicit comparison, rather than a blended “canon.”

Every witness record needs `witness_id`, class, continuity assignment or `UNKNOWN`, edition/build, acquisition/verification references, immutable source hashes, capabilities, limitations, admission scope, and analysis horizon. Store portable bindings in `T7S_SOURCE_LOCK.json`; local path resolution stays outside Git. Source admission allows retrieval, not unrestricted future-content consumption.

| Analytical responsibility | Strongest initial evidence route |
| --- | --- |
| Literary structure and detailed plot | Complete bounded game-story documents, page/command context, and relevant explicit presentation |
| Development | Ordered or partially ordered story transitions, tested against Sub/Event and supplemental counterexamples |
| Ordinary-life characterization | Sub/Event scenes and conditional card/character messages, preserving recipient/context |
| Relationships | Actual interactions and information asymmetry; isolated references are weaker than exchanges |
| Japanese speech | Native Japanese dialogue/messages with literal labels and surrounding turns |
| Performed voice | Correctly resolved and listened-to voice asset; runtime capture when delivery depends on scene timing/mix |
| Visual identity | Canonical image plus native role/occurrence; separate narrative presentation from card/promotional representation |

## P. Evidence locator/query model

### Portable syntax

Use `t7s://<immutable-corpus-alias>/v1/<object-route>`. Initial alias: **`c20260909-r484`**, bound by `T7S_SOURCE_LOCK.json` to the full collection-manifest digest, database/source-artifact digests, and schema version. Once published, an alias cannot be retargeted; a changed corpus receives a new alias with an explicit crosswalk.

This is a **versioned citation convention**, not an installed operating-system URI handler. Day-one recoverability uses the documented read-only queries and verified bounded query adapter. A general production resolver is not claimed. Bootstrap checks and their limits are recorded in [T7S_BOOTSTRAP_AND_GATE_RECORD.md](../09%20Audits%20and%20Manifests/T7S_BOOTSTRAP_AND_GATE_RECORD.md).

| Object | Route and required checks |
| --- | --- |
| Episode | `/episode/<episode_id>` → one `episodes` row → script and full hierarchy; episode alone is too broad for a precise dialogue claim |
| Script/document/source field | `/script/<script_id>?doc=<document_ref>#<JSON-pointer>`; `doc` mandatory, including `primary`; optional `line` and `log` are cross-checks |
| Page / line | Source pointer plus document; line uses `lines.line_index`, page/log uses `pages.log_order_index`; retain native `page_index` too |
| Master record/hierarchy | `/master/<table>?row=<zero-based-row>&<native-key-fields>#/<field>`; pointer relative to selected row; qualify scenario layer with category and layer ID |
| Supplemental text | `/supplemental/<namespace>/<full-canonical-id>`; preserve the complete stored ID even when it repeats the namespace |
| Media occurrence | `/record/<encoded-origin-artifact>/<zero-based-source-row>`; source lock binds the origin ledger's SHA-256; verify owner, pointer, logical/native reference and status |
| Canonical media | `/asset/<encoded-asset-id>?kind=<kind>`; resolve exact `(kind, asset_id)` and verify decoded bytes |
| Native resource | `/resource/<encoded-resource-id>?kind=<kind>` resolves the exact `media_resources` key; pair it with the occurrence route and retain candidate/native bank-wave links |
| Voice cue | Cite the media occurrence plus its native cue name/ID and cue-sheet identity where present; these are checked against the origin record, not presumed to be globally unique resource keys |
| Browser target | Derived convenience link to the local image browser's `#asset=<image-sha>` or episode-owner view; canonical citation remains source/asset identity |

Percent-encode path segments and query values as UTF-8; decode once. Apply JSON Pointer `~0`/`~1` escaping before URI encoding. All exported row/page/line/log indexes here are **zero-based**. JSONL physical line number is row index + 1. Never silently substitute a near-matching ID, document, hash, or source edition.

**Verified example routes:**

```text
t7s://c20260909-r484/v1/episode/201000001
t7s://c20260909-r484/v1/script/memory_0001.json__156050967bac492b?doc=primary&line=0&log=1#/Pages/1/TextArea/Dialogue
t7s://c20260909-r484/v1/script/ep6_101001_01.json__6a27ccf6a33d8ee9?doc=inline_movie_transcripts%2F0&line=0&log=2#/Pages/0/TextArea/Dialogue
t7s://c20260909-r484/v1/supplemental/card_message/card_message%3A1001%3A1
t7s://c20260909-r484/v1/master/m_scenario_layer?row=0&category=0&layer_id=100020#/title
t7s://c20260909-r484/v1/master/m_live_music_meta?row=1&music_id=1#/lyric
t7s://c20260909-r484/v1/record/media%3Avisual_relations.jsonl/0
t7s://c20260909-r484/v1/asset/image%3Asha256%3A31b63d12811facf787b9292fd1787ab066f6a28322772586cc0ead59135c0c4a?kind=visual
```

The first dialogue example preserves native display label `御園尾マナ` and voice reference `vo_memory_001_001`; the inspected identity-resolution status is `unresolved`. Display text must not be silently upgraded into a resolved character ID. The inline example selects the parent occurrence's child document; the child source is `vo_ep6_01_m01.json__a8270f514b91dd75`, reached through `/Pages/1/InlineMovie/VideoVoiceFileName` in its parent.

### Actual schema constraints

| SQLite/source fact | Resolver rule |
| --- | --- |
| `episodes` PK = episode ID; `scenarios` PK = script ID | Never infer ownership from name prefix alone; additional scripts need no invented episode |
| `pages` PK = `(script_id, log_order_index)` | A native page number is not globally unique |
| `lines` PK = `(script_id, line_index)` | Cross-check document and native pointer; indexes are projection-version-bound |
| Inline documents restart native page numbering | `adv_system_001...` has page 0 in both primary and inline documents; page-only resolution must fail as ambiguous |
| Structured JSON has `raw_script` and `inline_movie_transcripts[N].raw_script` | Resolve the document before applying its relative `/Pages/...` pointer; verify the child's own provenance/hash |
| `supplemental_text` PK = `(namespace, canonical_id)` | Retain deleted/inactive flags, conditions, origin artifact and source row |
| `media_relations.relation_row` is a database import ordinal | Stable citation uses origin artifact + source row + pinned ledger hash; database ordinal is only a lookup convenience |
| Many visual relations have `document_ref = NULL` | Keep `UNBOUND_DOCUMENT` until exact owner/pointer evidence uniquely binds the document; never coalesce NULL to primary |
| `media_relation_assets` links relation rows to `(kind, asset_id)` | Preserve zero/one/many candidates and resolution confidence; byte identity does not prove scene execution |
| Source artifacts include hashes and scoped paths | Verify the appropriate corpus/media/root scope; local resolver rejects paths escaping the configured evidence root |

Canonical ID spellings are retained: images use `image:sha256:<digest>`, WAVs `wav:<digest>`, and movies `movie:<source-digest>`. Do not assume all IDs mean decoded-byte SHA-256; consult `decoded_sha256` for the actual byte check. Script occurrences also remain distinct when decoded bytes match: 1,578 script records have 1,557 distinct decoded hashes, with four repeated-hash groups covering 25 records.

### Query contract

Open SQLite with `mode=ro&immutable=1`, `query_only=ON`, and `temp_store=MEMORY`. Example dialogue recovery, using parameters rather than interpolated text:

```sql
SELECT l.*, s.source_chain_json, s.decoded_sha256,
       s.normalized_sha256, p.native_page_json,
       p.effective_state_json, p.transitions_json, p.semantics_status_json
FROM lines AS l
JOIN scenarios AS s ON s.script_id = l.script_id
JOIN pages AS p
  ON p.script_id = l.script_id AND p.log_order_index = l.log_order_index
WHERE l.script_id = :script_id
  AND l.document_ref = :document_ref
  AND l.source_json_pointer = :source_pointer;
```

Require the intended unique match, verify optional line/log checks, resolve the correct native document, and compare the field value and hashes. Page/command claims without dialogue resolve through `pages` directly. For media, select the cited `origin_artifact` and `source_row_index`, then join `media_relation_assets` and `media_assets`; strict document matching governs automatic page attachment. Unbound media remains a candidate requiring adjudication.

Each analytical claim cites a source locator plus a concise evidence assertion; machine evidence rows retain the source digest, native display label, cue/resource identity, and any inference about identity or AV association separately. Claim → analytical artifact → ledger/state → locator → native source → linked media must be recoverable without a guessed filename.

**Design validation:** 25 read-only feasibility probes passed, including Main/Sub/Event and proposed first-reading text pointers, inline child provenance, five supplemental namespaces, category-qualified hierarchy, origin-ledger row recovery, linked image bytes, and lyric-master lookup. Negative probes expose ambiguous page/layer IDs, nonexistent documents, unbound visual documents, and a wrong image digest. These test real source structure and the proposed convention's required distinctions; they are not a claim that a complete resolver or every corpus locator has been tested. [Bootstrap probe receipt and limits](../09%20Audits%20and%20Manifests/T7S_BOOTSTRAP_AND_GATE_RECORD.md)

## Evidence-plane and analysis-plane boundary

Retained captures, native/decrypted/normalized scripts, masters and complete lyrics, SQLite, full transcripts, images/audio/video, source-artifact manifests, temporary packets and local resolver configuration remain external evidence. Git contains original analytical prose, bounded factual paraphrase, source digests/locators, typed state, claims/rivals, methods and authored admission/coverage decisions. No local absolute path is part of a public citation.

Configure external corpus, media and archive roots in local tooling. Resolve paths only inside their configured root; reject path traversal, absolute substitutions, wrong scope and hash drift. The source lock binds the collection alias, database, catalog, selected masters and the full external source-artifact manifest. The latter is a retrieval projection of the database's `source_artifacts` table, not a competing source authority. It can be regenerated with the recipe in the lock. Every actual cited source/media object is checked against its bound digest at use.

Packets record lock digest, exact membership and ranges, query/parameters, adapter version/hash, horizon and state filters, ordering basis, exclusions, unresolved joins and output hash. Include complete relevant native page context, no-dialogue pages, inline child documents, choices and absent/empty distinctions. A packet is disposable if identical evidence can be regenerated; its used recipe/membership/provenance remains recoverable. Metadata discovery and machine equality tests do not mark a story consumed.

### Exact membership and initial coverage

The canonical coverage ledger is one authored logical consumption/routing ledger represented by the [manifest](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING_MANIFEST.json), the [current-or-consumed shard](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING.jsonl), and the [routed-or-unconsumed shard](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING_ROUTED.jsonl). Across the disjoint union it has one record per exact script and catalog episode membership plus twelve supplemental tranche records (ten active leaves and two inactive split parents): 870 current-or-consumed records and 720 routed-or-unconsumed records after B0217, 1,590 data records total. It contains IDs and decisions; no copied source text or bulk metadata.

At B0191 the current-or-consumed role has four physical components: its original address, CURRENT_002, CURRENT_003 and [CURRENT_004](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING_CURRENT_004.jsonl). The routed role retains two components. That six-component boundary is historical; current retrieval is the seven-component route recorded here. This bounded physical growth preserves the complete 1,590-record logical union, role defaults and decision history; frozen transition receipts retain their historical five-component boundary.

At B0217 the current-or-consumed role gains [CURRENT_005](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING_CURRENT_005.jsonl). Read all seven ordered components through the current manifest: five current-or-consumed and two routed-or-unconsumed components; the original role address alone is incomplete. This bounded repartition preserves every logical identity, default and history outside the exact seven-case B0217 transition. Frozen B0191 six-component and B0177 five-component receipts remain historical and unchanged. All physical and actual quoted-native limits remain unchanged.

Each shard's META record declares its own field defaults. Expand every record with only its shard-local explicit defaults before interpretation; unknown record types or fields are validation failures. Record identity is `(record_type, script_id)` for `SCENARIO` and `(record_type, tranche_id)` for `SUPPLEMENTAL_TRANCHE`. When a routed record is consumed, move it atomically to the current-or-consumed shard while preserving its complete effective state, `decision_history`, and current decision fields. The manifest binds shard bytes, file hashes, membership hashes, record counts, partition rule, and the pre/post effective-state hash proving the split was lossless. A set of IDs alone is not evidence of reading.

Use `SELECT script_id FROM scenarios ORDER BY script_id COLLATE BINARY` to recover all 1,578 scripts. Join `episodes` on script ID to recover all 1,350 catalog memberships and their qualified hierarchy. Additional scripts are the exact anti-join, not a filename guess. Supplemental membership recipes use namespace-qualified full IDs in BINARY order, UTF-8 without BOM and one LF per ID including the last. The source lock pins each membership digest, so an auditor can recover every still-unread record without a complete copied source registry in Git.

To split a supplemental tranche, retain its original scope/decision history, name child memberships with exact predicates and digests, and prove their union equals the parent with empty intersection. Count active leaf tranches only. Partial script consumption uses explicit document/page ranges and remaining holes; completion requires every required native page, inline document and choice branch accounted for. Shared semantic screening may feed multiple subjects, but each subject's integration decision is tracked separately.

### Bounded first-operation query equivalent

Resolve episode `201000001` to `scout_000_00_01.json__8df3fd723276f650` through the locked catalog. Read the complete structured source, select every page ordered by `log_order_index` and every line ordered by `line_index`, and compare each document-qualified native pointer with the selected document. The bootstrap adapter verified 195 pages and 190 text pointers and copied that one full structured source to an external packet with an exact receipt. No later script is included. That is a reproducible query-equivalent retrieval route; it does not claim a universal resolver or a semantic reading.

For future script packets, repeat those checks for each explicitly admitted member and each inline child with its own provenance; fail on unbound documents or mismatches. For an ordinary query, pass IDs as parameters, verify the intended cardinality, compare native bytes/value and reject ambiguity. Never silently substitute search results outside the admitted horizon. Source access is required to verify the external evidence; the public repository does not redistribute it.

## Revision history

- 2026-09-09 — V1 / 1.0: establish the source/witness authority model, portable locator grammar, exact membership rules, and bounded first-operation query equivalent.
- 2026-09-24 — V1 / 1.1: bind the coverage ledger as a manifest-governed, two-shard logical artifact after T7S_B0080–T7S_B0099; preserve all 1,590 effective records through a lossless partition and define atomic record migration for later consumption.

- 2026-09-25 — V1 / 1.2: migrate both B0100 records with shard-local default expansion and complete history preservation; bind current effective state separately from the immutable original sharding proof.

- 2026-09-25: migrate 2 complete T7S_B0101 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 2 complete T7S_B0102 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 2 complete T7S_B0103 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 2 complete T7S_B0104 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 2 complete T7S_B0105 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 3 complete T7S_B0106 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-25: migrate 3 complete T7S_B0107 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0108 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0109 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0110 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0111 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0112 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0113 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0114 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0115 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0116 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0117 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0118 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0119 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0120 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0121 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0122 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0123 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0124 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0125 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0126 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0127 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0128 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0129 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0130 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0131 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0132 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0133 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0134 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0135 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0136 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0137 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0138 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0139 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0140 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0141 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0142 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0143 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0144 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0145 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0146 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0147 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0148 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0149 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0150 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0151 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0152 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0153 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0154 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0155 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0156 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0157 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0158 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-09-26: migrate 3 complete T7S_B0159 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0160 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0161 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0162 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0163 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0164 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0165 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0166 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0167 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-11: migrate 3 complete T7S_B0168 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-12: migrate 3 complete T7S_B0169 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-12: migrate 3 complete T7S_B0170 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-12: migrate 3 complete T7S_B0171 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-12: migrate 3 complete T7S_B0172 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-13: migrate 3 complete T7S_B0173 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-13: migrate 3 complete T7S_B0174 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-13: migrate 3 complete T7S_B0175 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

## Analytical entity-storage retrieval

The [entity owner](../03%20Longitudinal%20Ledgers/T7S_ENTITY_STATE_LEDGER.md), [manifest](../03%20Longitudinal%20Ledgers/T7S_ENTITY_STATE_LEDGER_MANIFEST.json) and [storage record](../09%20Audits%20and%20Manifests/T7S_ENTITY_STATE_STORAGE_TRANSITION_V1.md) represent one authored logical entity ledger. Bind current source-lock `physical_storage.entity_state_ledger` path/hash, then verify manifest/owner/all component full-file and payload lengths/hashes, direct series-relative paths, ordering and whole logical-view hash before reading or deriving entering state. Read the owner prefix before its unique route marker plus every ordered payload; the wrapper alone is incomplete evidence. Payload offsets exclude component metadata rather than changing transferred prose. Source locators and relative references retain their bytes and directory.

Admission freezes retain physical source-lock and entity owner/manifest/component fingerprints plus the exact logical-view fingerprint. Native-page checks and edition bindings remain independent. An administrative version change consumes no episode and retargets no old path. Missing parts, stale hashes, duplicate owners, unsupported representation or failed reconstruction stop use. At that entity cutover, coverage retained its then two-shard representation; that historical change granted no general file-size or source-schema exception. The current control representation is defined below.

- 2026-10-13 —1.78: add checked retrieval for B0175 entity storage; retain native authority, locator histories and modality/release gates.

- 2026-10-13: migrate 3 complete T7S_B0176 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-13: migrate 3 complete T7S_B0177 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

## Analytical control-storage retrieval

Bind the [physical SourceLock owner](../01%20Sources%20and%20Chronology/T7S_SOURCE_LOCK.json), its exact [manifest](../01%20Sources%20and%20Chronology/T7S_SOURCE_LOCK_MANIFEST.json) and every ordered source-lock component before reading any source-control field. Verify each full-file and payload length/hash, unique identity, contiguous logical byte interval, exact framing, direct series-relative path and final logical JSON length/hash. Check owner/manifest/logical version, witness, corpus alias and high-water agreement; use the separately reviewed reader projection. The original owner address remains the single current entrypoint; its wrapper is not the complete logical SourceLock. Binding its own manifest through the physical owner avoids a logical self-hash cycle.

For [coverage](../01%20Sources%20and%20Chronology/T7S_COVERAGE_AND_ROUTING_MANIFEST.json), read all five declared JSONL components. Expand each row only with its own role's bound original META defaults; verify per-component counts/hashes and exact reassembly of both logical role views. Require the disjoint union of all1590 identities and the canonical effective-state digest. A null admitted horizon is a retained value, not a reason to exclude an active supplemental leaf. Separate source identity, narrative reconstruction, analytical integration and AV state fields keep their original meanings.

Fresh prospective records capture the physical source-lock owner/manifest/components, the complete logical SourceLock fingerprint, all physical coverage shards and both whole logical role fingerprints/effective-state digest, together with the unchanged entity representation. Old freezes, receipts and path literals are historical and unmodified. Native equality, actually read Japanese/static evidence and performed audio/runtime observations remain separate. Source-lock12.83 is metadata storage only with B0177 unchanged.

Missing/indirect/foreign parts, stale hashes, unknown schemas, owner/version/horizon mismatches, wrong inherited defaults and duplicate/missing effective records stop use. Monolithic consumers must be adapted through reviewed fresh code/hash bindings before another source extraction or closeout. Every physical file and actual quoted native argument retains its existing limit. The [control-storage record](../09%20Audits%20and%20Manifests/T7S_CONTROL_STORAGE_TRANSITION_V1.md) owns the administrative mapping; it admits no new primary source or2053 semantics.

- 2026-10-14 —1.81: add full checked SourceLock/coverage retrieval after B0177; preserve all historical native/source boundaries and modality/release requirements.

- 2026-10-14: migrate 3 complete T7S_B0178 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-14: migrate 3 complete T7S_B0179 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-14: migrate 3 complete T7S_B0180 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-14: migrate 3 complete T7S_B0181 records through explicit shard-local defaults; retain the original lossless-sharding proof and bind the new current state separately.

- 2026-10-14: move exactly seven Sisara Intimacy records with their full explicit routed defaults and retained histories; all1583 other effective records remain exact.

- 2026-10-14: move exactly9 fullT7S_B0183records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-14: move exactly9 fullT7S_B0184records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-14: move exactly9 fullT7S_B0185records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-14: move exactly8 fullT7S_B0186records with explicit defaults/history; all1582other effective records retain bytes/values.

- 2026-10-14: move exactly9 fullT7S_B0187records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-14: move exactly9 fullT7S_B0188records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-28: move exactly7 fullT7S_B0189records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-28: move exactly8 fullT7S_B0190records with explicit defaults/history; all1582other effective records retain bytes/values.

- 2026-10-28: move exactly9 fullT7S_B0191records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-29: move exactly5 fullT7S_B0192records with explicit defaults/history; all1585other effective records retain bytes/values.

- 2026-10-29: move exactly5 fullT7S_B0193records with explicit defaults/history; all1585other effective records retain bytes/values.

- 2026-10-29: move exactly6 fullT7S_B0194records with explicit defaults/history; all1584other effective records retain bytes/values.

- 2026-10-29: move exactly6 fullT7S_B0195records with explicit defaults/history; all1584other effective records retain bytes/values.

- 2026-10-29: move exactly5 fullT7S_B0196records with explicit defaults/history; all1585other effective records retain bytes/values.

- 2026-10-29: move exactly6 fullT7S_B0197records with explicit defaults/history; all1584other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0198records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-29: move exactly8 fullT7S_B0199records with explicit defaults/history; all1582other effective records retain bytes/values.

- 2026-10-29: move exactly8 fullT7S_B0200records with explicit defaults/history; all1582other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0201records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0202records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-29: move exactly9 fullT7S_B0203records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0204records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0205records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-29: move exactly7 fullT7S_B0206records with explicit defaults/history; all1583other effective records retain bytes/values.

At T7S_B0206 the current SourceLock manifest declares five ordered logical components001–005. Read every component through the physical owner and current manifest; no individual part is a complete SourceLock. The earlier four-component snapshots remain frozen. This bounded growth changes storage only, preserves complete earlier logical/serialized history and admits no additional primary evidence or2053 semantics.

- 2026-10-29: move exactly7 fullT7S_B0207records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0208records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly9 fullT7S_B0209records with explicit defaults/history; all1581other effective records retain bytes/values.

At B0210 the current entity manifest declares four ordered components001–004. All three older complete component files/payloads/specifications remain byte-identical; new004 holds only the separately reviewed B0210 entity addition. Read all four ordered payloads through the exact manifest. Original three-component prospective freezes and storage-transition receipts remain historical; physical caps, source admission, local horizons and maturity gates are unchanged.

- 2026-10-30: move exactly9 fullT7S_B0210records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-30: move exactly9 fullT7S_B0211records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-30: move exactly9 fullT7S_B0212records with explicit defaults/history; all1581other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0213records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0214records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0215records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0216records with explicit defaults/history; all1583other effective records retain bytes/values.

- 2026-10-30: move exactly7 fullT7S_B0217records with explicit defaults/history; all1583other effective records retain bytes/values.
