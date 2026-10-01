---
series: BLUE_ARCHIVE
artifact_type: contextualization_audit
scope: Phase 2 arc contextualization across all 12 main-story groupings at the pinned Japanese snapshot
version: "1.2"
status: canonical
source_boundary: "electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; generation BA_REFRESH_20260928T032248159554Z; 480 admitted main readings; 69 supplemental objects admitted with limits; Phase 2 in progress and completion unproven"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Blue Archive Phase 2 contextualization audit

## 0. Responsibility and present result

**Phase 2 is NOT COMPLETE.** This audit owns the full acceptance matrix and records what would prove completion of the user-authorized **Start and complete Phase 2 — Arc contextualization** goal. It is an operational audit, not supplemental literary evidence or a character monograph. At the inspected input snapshot the current map and three contextualization controls report zero accepted supplemental admissions. Concurrent reading candidates are not counted as accepted until the integrator verifies their content, source routes, scope and affected shared state.

The [synthesis architecture](../00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md#phase-2--arc-contextualization) v1.4 defines five Phase 2 obligations after every major main arc: identify core related group stories; classify events by importance; read relevant bond/MomoTalk for major characters; inspect character-data written voice; update ledgers. The [method](../00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md) v1.3 gives the source-class, person/variant, ordinary-life, choice, language, counterevidence and locator contracts. Its numbered phase labels differ; this goal follows the synthesis architecture Phase 2 contextualization label and the method remains the interpretive contract.

This scope preserves **all 12 main-story groupings, 26 checkpoints and 480 main units**. It requires complete content review of **all 65 group objects and all 61 event-content packages / 1,010 canonical event objects**. All events remain visible regardless of school, stakes, comedy, seasonality or weak connection to the main plot. A conservative principal baseline of **111 subject retrieval families / 113 preserved raw person keys** requires **968 bond, 968 MomoTalk and 393 character-data objects**. These are **3,404 unique mandatory source objects**, not completed readings. The distinct Kei identity inquiry adds 19 available objects; positive mini-source leads add 29 objects for relevance review. Counts do not replace semantic acceptance.

The 111-family baseline is selected from already analyzed subjects and the named institutions, ensembles, working roles and ordinary-life questions in current checkpoint/ledger authority. It deliberately includes members whose value is ordinary pleasure, work, play, humor or a differing peer/private perspective. It is not derived from the 21 partial-model rows, machine co-occurrence rank or main appearance frequency. The roster and its individual reasons appear below. Source-facing reading may reveal another major subject or a required contextual source; add that obligation instead of freezing the roster to conceal it. No existing principal or quiet source is optional merely because a narrow pilot could succeed without it.

## 1. Input snapshot and source boundary

- Repository base: `3990c62cb5842a3783d38f3b55a7d28c7ab090b4` on `series/blue-archive`.
- Japanese raw witness: `a038020f1f5ac02dcfe76962426d38f86414cdd8`; generation `BA_REFRESH_20260928T032248159554Z`; game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`.
- Source inventory: `03_STRUCTURED_DATA/stories.jsonl`; SHA256 `c06e512173300972415110eeeea9538c3db86b27dc5ca2875be85904043b9a03`.
- Canonical inventory: 4,864 objects in nine source classes; all selected source paths were checked to exist. This checks transport/routes, not dialogue inspection.
- Existing main readings retain their original V1 or refreshed witness and local information boundaries. Contextual retrospective amendments update their owning ledgers and claims rather than silently rewriting historical readings.
- No new source generation, localization, adaptation, audiovisual witness, model, monograph or prediction register is admitted by this audit. Written language is the assigned voice channel.

| Governing input | Inspected SHA256 |
|---|---|
| [BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md](../00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md) | `18ebadc9d8ab0460930ef4e75cb02c749c8c15c9f2c402fa7b984e0a3caad976` |
| [BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md](../00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md) | `077819beeb10a6f2e39f5b484ae319652e6383ad645b8ac2bcfaa29f39e3901c` |
| [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md) | `ae17ea2a6e9b5dcaee358d910774c8c119dfa1a4b17e1a70b8eea5432fe3c2ed` |
| [BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) | `85528edb071ce3c575a32ab1b39903ccfd284f04cefc41196e2ea243ac86b46a` |
| [BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md) | `95635e734d11124af952d4077878807089e162579c4b0bfa54c618e480ca4e95` |
| [BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md) | `1f6535c396c7f419300ad9f2da2c2de4d5bedfa9f77abead2ff01bc902a470aa` |
| [BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) | `e4ea078588a123c21d10d2e9e8e7e173468ea1a4bf81db26027566e49b221f2f` |


The operational metadata dispatch is retained outside analytical Git in the title-local `_phase2_work/phase2_scope_metadata.json` with SHA256 `33aef4d9d88a528499f4aa5a21f536fe6e40694305670bcaa79e39f61a0df80d`. It contains every required story ID, canonical path route, raw witness metadata, per-principal MomoTalk/bond join and arc assignment. Its accompanying `phase2_required_source_metadata.jsonl` contains metadata for the 3,404 required objects. Neither file is a second analytical authority or a claim that story dialogue was read. Recovery does not require trusting that working copy: use the locked generation and the exact roster/source-selection rule below.

**Exact private-source selection rule:** union records whose explicit `person_id` or `person_ids` contains a raw key listed in §4; retain only `bond`, `momotalk` and `character_data` for the required private/baseline pool. Confirm every selected MomoTalk thread through `00_MANIFESTS/MOMOTALK_BOND_CROSSWALK.csv` and its exact bond ID. Empty `person_ids` does not mean no source: Yuzu and Eimi bond records have explicit `person_id` and positive crosswalk links. Every one of the 1,189 crosswalk rows points to an existing canonical bond object. Use each record’s `canonical_path` directly relative to the generation; it already begins with `02_CANONICAL_STORIES/`.

## 2. Completion requirements

| ID | Requirement | Evidence that passes | Current state |
|---|---|---|---|
| P2-R01 | Related group and ordinary institution coverage | All 65 complete group objects read in coherent sequences, per-sequence source/admission/chronology record, and evidence-grounded relevance for all 12 arc rows. | IN_PROGRESS; see §9 |
| P2-R02 | Fair event importance classification | All 61 packages / 1,010 objects receive complete content review and grounded priority, evidence-function and workflow decisions. Preserve every episode ID and all repeat contexts. No unread metadata verdict or quiet-material deferral. | IN_PROGRESS; see §9 |
| P2-R03 | Major-character bond and MomoTalk | All required 968 bond and 968 MomoTalk objects read for the 111 families with linked preface/scene, message boundaries, alternatives, variant/source context and public/peer/private comparison. New major subjects identified by reading add required routes. | IN_PROGRESS; see §9 |
| P2-R04 | Written linguistic baseline | All required 393 character-data objects inspected as contextual written language, compared with story/texting language and variant conditions. The 27 unresolved data routes receive identity review where relevant; performed voice remains unverified. | IN_PROGRESS; see §9 |
| P2-R05 | Ledger and coverage integration | Each accepted coherent reading transaction closes applicable deltas to character, relationship, institution, Sensei, voice, motif and claim ledgers; coverage, source gaps and admission controls agree. Negative/no-material deltas are truthful, not fabricated rows. | IN_PROGRESS; see §9 |
| P2-R06 | Every main arc contextualized | All 12 rows in §3 pass the five architecture obligations. Cross-arc reused readings are explicit and claim-specific. Main-only/identity-special people receive real retrieval review and named limits, not an invented private persona. | IN_PROGRESS; see §9 |
| P2-R07 | Provenance, chronology and attribution | All consequential claims recover exact source IDs, scene/utterance/choice/message locators and raw witnesses; documentary dates remain separate from narrative anchors. Unordered repertoire does not become a state edge. | IN_PROGRESS; see §9 |
| P2-R08 | Contrary evidence and ordinary breadth | Readings preserve pleasures, humor, play, minor disputes, work and uneventful relations with competing interpretations; no crisis-only essence, universal Sensei route or one-scene coverage ceiling. | IN_PROGRESS; see §9 |
| P2-R09 | Semantic acceptance and publication | Integrator reads delivered analyses, tests consequential quotations/locators and cross-document effects, resolves material contradictions, updates current state and verifies required source/housekeeping/final exact-commit repository gates. A green validator is not literary completeness. | IN_PROGRESS; see §9 |

Readiness or model promotion is a separate gate. Phase 2 completion does not require manufacturing a monograph/model, resolving unprinted legal/medical outcomes, authenticating every historical record, constructing a total timeline or inspecting performed voice. It does require honest claim limits for those debts and complete assigned textual contextualization. A required unread source cannot be relabeled optional to declare completion.

## 3. Full main-arc acceptance matrix

Every row inherits P2-R01–P2-R09. The main counts below describe already completed Phase 1, not Phase 2 progress. Related groups/events can serve several rows after source-facing relevance is established. Documentary participant metadata only schedules inquiry; it does not establish literary content or chronology. The operational dispatch distinguishes checkpoint-named subjects, metadata participant leads and cross-school/institution contextual leads. Family assignments do not assert that every member appeared in every main arc. In particular, only Wakamo carries the Hyakkiyako family’s Prologue inquiry; its other members remain Hyakka/community-context inquiries.

| Arc scope / main units | Governing checkpoint authority | Principal people and protected contexts | Contextual question and claim limit | Phase 2 |
|---|---|---|---|---|
| `MAIN_V000` / 2 | [MAIN_V000_C001](../02%20Sequential%20Readings/MAIN/PROLOGUE/BLUE_ARCHIVE_MAIN_V000_C001_CHECKPOINT.md) | Sensei, Rin, Arona, Wakamo, Yuuka, Hasumi, Chinatsu, Suzumi | Delegated authority, trust/access, adult restraint, private-versus-public asymmetry; ordinary and dyadic counterpart sources must not certify system provenance. | NOT COMPLETE |
| `MAIN_V001` / 83 | [MAIN_V001_C001](../02%20Sequential%20Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md), [MAIN_V001_C002](../02%20Sequential%20Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C002_CHECKPOINT.md), [MAIN_V001_C003](../02%20Sequential%20Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C003_CHECKPOINT.md) | Ayane, Shiroko, Nonomi, Serika, Hoshino, Yume, Hifumi, Aru, Mutsuki, Kayoko, Haruka, Hina, Hikari, Nozomi, Asagiri Suou, Underground Dweller | Collective survival, debt/work, inherited loss and governance; retain ordinary service, play and peer control alongside state-separated Hoshino/Yume and family/corporate conflict. | NOT COMPLETE |
| `MAIN_V002` / 45 | [MAIN_V002_C001](../02%20Sequential%20Readings/MAIN/VOLUME_002_時計じかけの花のパヴァーヌ/BLUE_ARCHIVE_MAIN_V002_C001_CHECKPOINT.md), [MAIN_V002_C002](../02%20Sequential%20Readings/MAIN/VOLUME_002_時計じかけの花のパヴァーヌ/BLUE_ARCHIVE_MAIN_V002_C002_CHECKPOINT.md) | Momoi, Midori, Alice / `AL-1S` (provisional), Yuzu, Key, Yuuka, Noa, Rio, Toki, Nel, Akane, Asuna, Karin, Himari, Eimi, Chihiro, Hare, Maki, Kotama, Utaha, Hibiki, Kotori, Sumire | Making/play and chosen membership, public/private council and service work, frightened protection and technology; separate Alice/Key, variant contexts, forecasts and enacted governance. | NOT COMPLETE |
| `MAIN_V003` / 89 | [MAIN_V003_C001](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C001_CHECKPOINT.md), [MAIN_V003_C002](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C002_CHECKPOINT.md), [MAIN_V003_C003](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C003_CHECKPOINT.md), [MAIN_V003_C004](../02%20Sequential%20Readings/MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C004_CHECKPOINT.md) | Hifumi, Azusa, Hanako, Koharu, Mika, Seia, Nagisa, Saori, Misaki, Hiyori, Atsuko, Hasumi, Tsurugi, Mashiro, Sakurako, Marie, Hinata, Mine, Hanae, Serina, Ui, Hina, Sensei, Beatrice, Maestro, Golconda / Francis | Study and friendship, suspicion and repair, differentiated rescue institutions, private fear/pleasure and accountability; no event/bond scene can substitute for missing legal or medical outcomes. | NOT COMPLETE |
| `MAIN_V004` / 44 | [MAIN_V004_C001](../02%20Sequential%20Readings/MAIN/VOLUME_004_カルバノの兎編/BLUE_ARCHIVE_MAIN_V004_C001_CHECKPOINT.md), [MAIN_V004_C002](../02%20Sequential%20Readings/MAIN/VOLUME_004_カルバノの兎編/BLUE_ARCHIVE_MAIN_V004_C002_CHECKPOINT.md) | Miyako, Saki, Moe, Miyu, Yukino, Niko, Otogi, Kurumi, Kanna, Kirino, Fubuki, Kaya, Rin, Sensei, Decartes | Material camp life, senior/subordinate relations, chosen duty and refusal, civilian safety, law enforcement and daily work; preserve individual FOX/RABBIT private voices and incomplete school/legal restoration. | NOT COMPLETE |
| `MAIN_V005` / 54 | [MAIN_V005_C001](../02%20Sequential%20Readings/MAIN/VOLUME_005_百花繚乱編/BLUE_ARCHIVE_MAIN_V005_C001_CHECKPOINT.md), [MAIN_V005_C002](../02%20Sequential%20Readings/MAIN/VOLUME_005_百花繚乱編/BLUE_ARCHIVE_MAIN_V005_C002_CHECKPOINT.md) | Yukari, Nagusa, Kikyou, Renge, Ayame, Niya, Kaho, Chise, Shizuko, Fina, Umika, Kaede, Mimori, Tsubaki, Michiru, Izuna, Tsukuyo, Shuro, Kokuriko, Azami, Kuzunoha, Kai / “Riku” (doctor; alias unresolved) | Role performance, house/club belonging, friendship through change, festival/community pleasure, authored fear and records; distinguish historical witness, shadow and current encounter identities. | NOT COMPLETE |
| `MAIN_V006` / 33 | [MAIN_V006_C001](../02%20Sequential%20Readings/MAIN/VOLUME_006/BLUE_ARCHIVE_MAIN_V006_C001_CHECKPOINT.md), [MAIN_V006_C002](../02%20Sequential%20Readings/MAIN/VOLUME_006/BLUE_ARCHIVE_MAIN_V006_C002_CHECKPOINT.md), [MAIN_V006_C003](../02%20Sequential%20Readings/MAIN/VOLUME_006/BLUE_ARCHIVE_MAIN_V006_C003_CHECKPOINT.md) | Saori, Misaki, Hiyori, Atsuko, Subaru, Maia, Nagisa, Mine, Serina, Hanae, Ui, Shimiko, Suzumi, Reisa, Sensei | Outside livelihood, music, study and provisional school-making; ordinary/private sources broaden personhood without closing resident harm, consent, parole, medical or archive debts. | NOT COMPLETE |
| `MAIN_V100` / 64 | [MAIN_V100_C001](../02%20Sequential%20Readings/MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C001_CHECKPOINT.md), [MAIN_V100_C002](../02%20Sequential%20Readings/MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C002_CHECKPOINT.md), [MAIN_V100_C003](../02%20Sequential%20Readings/MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C003_CHECKPOINT.md), [MAIN_V100_C004](../02%20Sequential%20Readings/MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C004_CHECKPOINT.md) | Sensei, Arona, Plana / A.R.O.N.A. (other-time-axis OS), Shiroko, Shiroko (other time axis, provisional), Prenapates (named, provisional), Rin, Kaya, Seia, Hanako, Ayane, Yuuka, Rio, Toki, Himari, Alice / `AL-1S` (provisional), Key, Maestro, Francis | Cross-school cooperation and ordinary aftermath, differentiated competence, counterpart identity and loss; reuse all ensemble contextual readings and retain technical/medical/civic claims at their actual witness limits. | NOT COMPLETE |
| `MAIN_S2_V000` / 4 | [MAIN_S2_V000_C001](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_000/BLUE_ARCHIVE_MAIN_S2_V000_C001_CHECKPOINT.md) | Decalcomania, Rin, Aoi, Ayumu, Momoka, Sensei, Arona, Plana / A.R.O.N.A. (other-time-axis OS), Rei (diving team, provisional) | Finite institutional work and waking care; separate photos/dream/shard and diver Rei from registry baseball Rei without positive identity evidence. | NOT COMPLETE |
| `MAIN_S2_V001` / 10 | [MAIN_S2_V001_C001](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_001/BLUE_ARCHIVE_MAIN_S2_V001_C001_CHECKPOINT.md) | Rin, Kaya, Aoi, Ayumu, Momoka, Heine, Sumomo, Mai, Sensei, Arona, Plana / A.R.O.N.A. (other-time-axis OS), Council-president claimant (identity-disputed role actor), Orwell (Decalcomania screen/shadow; identity provisional), Decalcomania | Rest, friendship and duty; individual memory versus public recognition; direct NPC routes remain unverified and event/council effectiveness cannot authenticate claimant identity. | NOT COMPLETE |
| `MAIN_S2_V002` / 38 | [MAIN_S2_V002_C001](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_002/BLUE_ARCHIVE_MAIN_S2_V002_C001_CHECKPOINT.md), [MAIN_S2_V002_C002](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_002/BLUE_ARCHIVE_MAIN_S2_V002_C002_CHECKPOINT.md) | Hina, Ako, Iori, Chinatsu, Makoto, Iroha, Ibuki, Satsuki, Chiaki, Karen (Gehenna Restoration Committee), Shoko (Gehenna Restoration Committee), Mayumi (Gehenna Restoration Committee), Fuuka, Juri, Haruna, Akari, Junko, Izumi, Kasumi, Meg, Sena, Erika, Kirara, Sensei | Freedom/discipline, office and coercion, distinct food/work/play and peer life, medical care and accountable aftermath; ordinary baseline is required without excusing war/custody conduct or certifying restitution. | NOT COMPLETE |
| `MAIN_S2_V003` / 14 | [MAIN_S2_V003_C001](../02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_003/BLUE_ARCHIVE_MAIN_S2_V003_C001_CHECKPOINT.md) | Umiji Minato, Tomoshita Ami, Komori Sumika, Sengoku Mitsuki, Funamori Sanae, Sammy (shipboard cat), Sensei, Arona, Plana / A.R.O.N.A. (other-time-axis OS), Council-president claimant (identity-disputed role actor) | Hospitality/work, shipboard care and taboo, independent desires and grief; inspect Odysseia event 861 as an institution/context lead without inventing Minato/Ami/Sanae bonds or merging unrelated divers. | NOT COMPLETE |


All 12 rows require explicit answers to: which group contexts are core and why; which events support/disturb the account and what their ordinary value is; which principal private sequences were read or have no verified route; how written language varies by audience/variant/state; and which ledgers/claims changed. A cross-school main crisis is contextualized through the relevant ensemble readings and ordinary afterstates; it is not satisfied by repeating its existing checkpoint.

## 4. Principal private-source baseline

The per-family rationale is a coverage decision. Each subject’s prior main-state description is retrievable from the [coverage index §3](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md#3-source-availability-versus-analyzed-coverage); the arc checkpoint links in §3 retain the reasons, counterevidence and temporal limits behind it. The final column adds the individual inquiry that earns complete private coverage. Counts are available canonical objects and currently not accepted completion evidence. Raw key suffixes below mean `BA_PERSON_<suffix>`.

| Subject family | Raw key suffixes retained | Main-arc inquiry routes | Bond | MomoTalk | Character data | Individual inclusion reason |
|---|---|---|---:|---:|---:|---|
| Ayane | `AYANE` | `MAIN_V001`, `MAIN_V100` | 7 | 7 | 3 | Administrative and elected leadership states require peer routine and private desires beyond task competence. |
| Shiroko | `SHIROKO` | `MAIN_V001`, `MAIN_V100` | 17 | 17 | 4 | Local and counterpart identities, solitary tactics and shared home require variant-bounded reading rather than person-general merging. |
| Nonomi | `NONOMI` | `MAIN_V001`, `MAIN_V100` | 9 | 9 | 3 | Collective care and Nephthys family conflict require desires beyond money/resource function. |
| Serika | `SERIKA` | `MAIN_V001`, `MAIN_V100` | 13 | 13 | 5 | COMPLETE available31 private/written objects accepted with limits in cycle002; independent pleasures, visitor service, literal boundaries and variant/chronology limits retained. Event and whole-arc duties remain open. |
| Hoshino | `HOSHINO` | `MAIN_V001`, `MAIN_V100` | 13 | 13 | 8 | Yume-linked grief, self-removal and later office acceptance require quiet desires and state-specific contrast. |
| Aru | `ARU` | `MAIN_V001`, `MAIN_V100` | 12 | 12 | 5 | Named Kohshinjo68 / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E002; rallies PS68 amid changing sky for Sensei/Kayoko. |
| Mutsuki | `MUTSUKI` | `MAIN_V001`, `MAIN_V100` | 11 | 11 | 5 | Named Kohshinjo68 / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E009; teases Aru's concern for Kayoko. |
| Kayoko | `KAYOKO` | `MAIN_V001`, `MAIN_V100` | 12 | 12 | 5 | Named Kohshinjo68 / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E004; confirms ship/Ark link severance. |
| Haruka | `HARUKA` | `MAIN_V001`, `MAIN_V100` | 12 | 12 | 5 | Named Kohshinjo68 / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E009; appears with PS68 in farewell under tag drift. |
| Hikari | `CH0242` | `MAIN_V001`, `MAIN_V100` | 5 | 5 | 2 | Named Highlander railway participant must retain differentiated ordinary/private conduct. |
| Nozomi | `CH0243` | `MAIN_V001`, `MAIN_V100` | 5 | 5 | 2 | Named Highlander railway participant must retain differentiated ordinary/private conduct. |
| Momoi | `MOMOI` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 3 | Maker and belonging advocate whose shortcuts/care require ordinary play comparison. |
| Midori | `MIDORI` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 3 | Evidence-sensitive sibling care and risk participation require an independent private/ordinary account. |
| Alice / `AL-1S` (provisional) | `ARIS` | `MAIN_V002`, `MAIN_V100` | 15 | 15 | 7 | Chosen personhood, game-language learning and hero performance require play and private desire beyond weapon crises. |
| Yuzu | `YUZU`, `CH0336` | `MAIN_V002`, `MAIN_V100` | 14 | 14 | 7 | Creative exposure and rescue under fear require ordinary fear, work and pleasure controls. |
| Yuuka | `YUUKA` | `MAIN_V002`, `MAIN_V100` | 14 | 14 | 5 | Voluntary membership inquiry, enforcement and revisable exceptions require council/private contrast. |
| Noa | `CH0095` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 4 | Council mediation, observation and emergency dispatch must be compared with routine/private relations. |
| Rio | `CH0158` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 4 | Secrecy, forecasts and coerced protection require ordinary/private counterevidence without exonerating office harm. |
| Koyuki | `CH0198` | `MAIN_V002`, `MAIN_V100` | 10 | 10 | 3 | Seminar member with named main-state capture/afterstate must retain her own private/ordinary range. |
| Akane | `AKANE` | `MAIN_V002`, `MAIN_V100` | 14 | 14 | 4 | Named CleanNClearing / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E006; reports transient Sanctum vanished and maintains vigilance. |
| Karin | `KARIN` | `MAIN_V002`, `MAIN_V100` | 14 | 14 | 5 | Named CleanNClearing / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E005; arrives with C&C to aid Toki. |
| Asuna | `ASUNA` | `MAIN_V002`, `MAIN_V100` | 13 | 13 | 5 | Named CleanNClearing / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E006; reports Toki escort complete. |
| Nel | `NERU` | `MAIN_V002`, `MAIN_V100` | 12 | 12 | 5 | Named CleanNClearing / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E005; arrives with C&C and rebukes Toki farewell. |
| Toki | `CH0187` | `MAIN_V002`, `MAIN_V100` | 12 | 12 | 8 | Obedience, displaced employment and C&C tolerance require her own preference, peer role and ordinary afterstate. |
| Hare | `HARE` | `MAIN_V002`, `MAIN_V100` | 9 | 9 | 3 | Named Veritas / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E016; readies self-destruct and sees premature activation. |
| Maki | `MAKI` | `MAIN_V002`, `MAIN_V100` | 9 | 9 | 3 | Named Veritas / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E016; fears debris and questions premature activation. |
| Kotama | `KOTAMA` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 3 | Named Veritas / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E016; simulation forecasts Ark destruction, then traces hack. |
| Chihiro | `CH0160` | `MAIN_V002`, `MAIN_V100` | 4 | 4 | 1 | Security/technical competence and coalition action require work/routine and private limits. |
| Utaha | `UTAHA` | `MAIN_V002`, `MAIN_V100` | 10 | 10 | 3 | Named Engineer / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E002; Engineering helps locate lower corridor signal. |
| Hibiki | `HIBIKI` | `MAIN_V002`, `MAIN_V100` | 11 | 11 | 3 | Named Engineer / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E002; Engineering identifies signal point. |
| Kotori | `KOTORI` | `MAIN_V002`, `MAIN_V100` | 9 | 9 | 3 | Named Engineer / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E010; assigned ground Engineering support. |
| Himari | `CH0159` | `MAIN_V002`, `MAIN_V100` | 8 | 8 | 4 | Dissent and technical coalition work require SPTF work, ordinary sociability and variant conditions. |
| Eimi | `EIMI`, `CH0337` | `MAIN_V002`, `MAIN_V100` | 14 | 14 | 6 | Named SPTF partner must not be reduced to a device or Himari support role; recover own private and contextual voice routes. |
| Sumire | `SUMIRE` | `MAIN_V002`, `MAIN_V100` | 9 | 9 | 3 | Named TrainingClub / Millennium role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E016; reports ready for Millennium defense. |
| Hifumi | `HIHUMI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 11 | 11 | 3 | Teaching and student agency plus fan pleasure require private/ordinary life alongside crisis leadership. |
| Azusa | `AZUSA` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 3 | Learned security/violence, present effort and peer delight require pleasures and trust outside crisis. |
| Hanako | `HANAKO` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 3 | Coercion-sensitive intelligence and humor require private and ordinary audience distinctions. |
| Koharu | `KOHARU` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 7 | 7 | 3 | Institutional exclusion, shame, care and peer humor require private/ordinary contrast. |
| Mika | `CH0069` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 10 | 10 | 3 | Anti-peace conduct, rescue and accountability require ordinary pleasure and relationship-specific self-presentation. |
| Seia | `CH0070` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Prognostic speech, lost foresight and Tea Party repair require ordinary/private voice without confirming supernatural claims. |
| Nagisa | `NAGISA` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 3 | Security coercion, aid, apology and school memory require ordinary council/peer/private contrast. |
| Hasumi | `HASUMI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 14 | 14 | 5 | Named Justice / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E014; reaches Koharu and thanks Mika for concrete rescue amid hostility. |
| Tsurugi | `TSURUGI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 7 | 7 | 3 | Named Justice / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E009; takes front defense in Chesed operation. |
| Mashiro | `MASHIRO` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 11 | 11 | 3 | Named Justice / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E014; confirms trapped civilians/Koharu near chapel and goes to help. |
| Sakurako | `SAKURAKO` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 9 | 9 | 3 | Named SisterHood / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E015; claims historical ceremonial attire and vows to break hatred. |
| Marie | `MARI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 12 | 12 | 5 | Named SisterHood / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E015; reacts to attire and remains uncertain at launch. |
| Hinata | `HINATA` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Named SisterHood / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E004; reports Sisterhood catacomb standby. |
| Mine | `CH0152` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 3 | Force/care and finite medical responsibility require baseline work/ordinary/private contrast without inventing clinical repair. |
| Hanae | `HANAE` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 9 | 9 | 3 | Named KnightsHospitaller / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V006 C003 E007; holds Arius patients until Mine approves discharge. |
| Serina | `SERINA` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 7 | 7 | 3 | Named KnightsHospitaller / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V006 C003 E007; checks Subaru and asks about Arius distrust. |
| Ui | `CH0169` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 7 | 7 | 4 | Named BookClub / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E013; laments opening her library to evacuees. |
| Shimiko | `SHIMIKO` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 5 | 5 | 1 | Named BookClub / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E013; opens old library as estimated safer shelter. |
| Suzumi | `SUZUMI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 9 | 9 | 3 | Named TrinityVigilance / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E013; joins Trinity response when new enemies appear. |
| Reisa | `CH0167` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Named TrinityVigilance / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E013; joins Vigilante help amid Trinity attack. |
| Ichika | `CH0071` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Named Justice / Trinity role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C001 E004; tries to prevent protest firing and fight. |
| Airi | `AIRI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 7 | 7 | 4 | Protected peer leisure and personal preferences: group/event ordinary-life inquiry is required even without main-plot state change. |
| Kazusa | `KAZUSA` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Protected peer leisure, self-presentation and personal preferences beyond emergency or plot utility. |
| Yoshimi | `YOSHIMI` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 3 | Protected everyday group interaction, teasing and pleasures beyond institutional/crisis scenes. |
| Natsu | `CH0155` | `MAIN_V003`, `MAIN_V006`, `MAIN_V100` | 8 | 8 | 4 | Protected ordinary peer grammar and tastes; participant metadata prompts full sources, never a low-value rank. |
| Saori | `SAORI` | `MAIN_V003`, `MAIN_V006` | 10 | 10 | 5 | Crisis leadership, outside work, self-worth and teaching require private and peer differentiation. |
| Misaki | `MISAKI` | `MAIN_V003`, `MAIN_V006` | 7 | 7 | 3 | Distinct vulnerability, study and Squad role require her own ordinary/private account. |
| Hiyori | `HIYORI` | `MAIN_V003`, `MAIN_V006` | 6 | 6 | 3 | Deprivation, outside-life teaching and peer dependence require pleasures and private grammar. |
| Atsuko | `ATSUKO` | `MAIN_V003`, `MAIN_V006` | 7 | 7 | 3 | Restricted speech, Squad care and provisional presidency require private desire, ordinary voice and state distinctions. |
| Subaru | `CH0309` | `MAIN_V003`, `MAIN_V006` | 5 | 5 | 1 | Central Arius shelter/music/exclusion/repair actor; own private sources and written register are necessary. |
| Miyako | `MIYAKO` | `MAIN_V004`, `MAIN_V100` | 10 | 10 | 3 | Captaincy, public duty and civilian-safety refusal require routine/peer/private comparison. |
| Saki | `CH0144` | `MAIN_V004`, `MAIN_V100` | 9 | 9 | 3 | RABBIT member with distinct work/discipline perspective requires a complete independent private/ordinary range. |
| Moe | `MOE` | `MAIN_V004`, `MAIN_V100` | 9 | 9 | 6 | Technical/demolition member requires pleasure and choice outside crisis utility. |
| Miyu | `CH0145` | `MAIN_V004`, `MAIN_V100` | 9 | 9 | 3 | RABBIT vulnerability and material life require independent ordinary/private characterization. |
| Niko | `CH0172` | `MAIN_V004`, `MAIN_V100` | 5 | 5 | 2 | FOX senior must retain own directed relations and private voice rather than collective culpability inference. |
| Kurumi | `CH0173` | `MAIN_V004`, `MAIN_V100` | 5 | 5 | 2 | FOX senior must retain own directed relations and private voice rather than collective culpability inference. |
| Otogi | `CH0174` | `MAIN_V004`, `MAIN_V100` | 5 | 5 | 2 | FOX senior must retain own directed relations and private voice rather than collective culpability inference. |
| Kanna | `CH0170` | `MAIN_V004`, `MAIN_V100` | 7 | 7 | 3 | Named PublicPeaceBureau / Valkyrie role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E004; reports D.U. evacuation complete but staff and food short. |
| Kirino | `KIRINO` | `MAIN_V004`, `MAIN_V100` | 7 | 7 | 3 | Named anzenkyoku / Valkyrie role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C001 E013; joins Schale operation and supports Miyako’s plan. |
| Fubuki | `CH0141` | `MAIN_V004`, `MAIN_V100` | 7 | 7 | 4 | Named anzenkyoku / Valkyrie role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C001 E013; warns of Kaiser defenses and joins Schale operation. |
| Yukari | `CH0161` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Chosen Hyakka belonging and household duty require ordinary/private contexts alongside forced inner exposure. |
| Nagusa | `CH0222` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Ayame-linked shame, role performance and relational challenge require ordinary/private controls without inventing stable repair. |
| Kikyou | `CH0225` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Strategist role, resentment, inquiry and witness consent require independent routine/private contexts. |
| Renge | `CH0224` | `MAIN_V005`, `MAIN_V100` | 9 | 9 | 3 | Succession resentment, apology intent and collective action require independent routine/private contexts. |
| Niya | `CH0109` | `MAIN_V005`, `MAIN_V100` | 5 | 5 | 1 | Named Onmyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C004 E010; reports ninja return and sends self-attributed Kuzunoha letter. |
| Kaho | `CH0107` | `MAIN_V005`, `MAIN_V100` | 5 | 5 | 1 | Named Onmyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; launches Hyakki district defense with mixed force. |
| Chise | `CHISE` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Named Onmyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; joins Hyakki district-defense departure. |
| Michiru | `CH0113` | `MAIN_V005`, `MAIN_V100` | 9 | 9 | 4 | Named NinpoKenkyubu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E001; challenges Nagusa's disguise and considers reading scroll. |
| Izuna | `IZUNA` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 4 | Named NinpoKenkyubu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E001; states Ayame search to Nagusa and credits sky to Sensei. |
| Tsukuyo | `CH0114` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 4 | Named NinpoKenkyubu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C003 E001; cites Schale request and comforts distressed Nagusa. |
| Shizuko | `SHIZUKO` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 4 | Named MatsuriOffice / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; reports festival shelter readiness and supplies pledge. |
| Fina | `PINA` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Named MatsuriOffice / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; joins Hyakki defense with situated chivalry slogan. |
| Umika | `CH0110` | `MAIN_V005`, `MAIN_V100` | 5 | 5 | 2 | Named MatsuriOffice / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; supports festival-committee shelter work. |
| Kaede | `KAEDE` | `MAIN_V005`, `MAIN_V100` | 5 | 5 | 2 | Named Shugyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V005 C001 E008; speaks about festival and reports safe after clash. |
| Mimori | `MIMORI` | `MAIN_V005`, `MAIN_V100` | 8 | 8 | 3 | Named Shugyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V005 C001 E021; Shugyoubu defense and broadcast observation. |
| Tsubaki | `TSUBAKI` | `MAIN_V005`, `MAIN_V100` | 7 | 7 | 3 | Named Shugyobu / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E010; joins Hyakki district-defense departure. |
| Wakamo | `WAKAMO` | `MAIN_V005`, `MAIN_V100`, `MAIN_V000` | 9 | 9 | 3 | Named EmptyClub / Hyakkiyako role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through V100 C002 E020; appears at Schale attack and pledges Sensei protection. |
| Hina | `HINA` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 13 | 13 | 6 | Office protection, coercion and later apology require ordinary contrast without certifying restitution. |
| Ako | `AKO` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 6 | 6 | 4 | Prefect work and directed Hina/council relations require routine/private self-presentation. |
| Iori | `IORI` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 10 | 10 | 3 | Enforcement, institutional boundary and refusal require ordinary work and private controls. |
| Chinatsu | `CHINATSU` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 9 | 9 | 3 | Medical/disciplinary roles and coalition action require routine/private linguistic contrast. |
| Makoto | `CH0079` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 8 | 8 | 4 | Office domination, coercion, isolation and recovery require ordinary/peer/private contexts without repaired-harm assumption. |
| Iroha | `CH0156` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 9 | 9 | 4 | Quitting/conditional return, Ibuki care and faction duties require routine/private preference. |
| Ibuki | `CH0077` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 8 | 8 | 4 | Care and loyalty in Pandemonium require an independent ordinary/private account. |
| Satsuki | `CH0080` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 10 | 10 | 4 | Technical testimony and coalition hypotheses require ordinary/private preference rather than occult-expert reduction. |
| Chiaki | `CH0238` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 8 | 8 | 4 | Questions exposing unity ideology and media/logistics work require ordinary/private register and motives. |
| Fuuka | `FUUKA` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 8 | 8 | 3 | Food-service labor, coercion, resistance and boundaries require independent pleasure and private desire. |
| Juri | `JURI` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 7 | 7 | 3 | Food-service contribution and work failures require ordinary/private self-presentation. |
| Haruna | `HARUNA` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 11 | 11 | 5 | Gourmet pleasure, destructive judgments and coercive aftermath require ordinary/private comparison. |
| Akari | `AKARI` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 7 | 7 | 3 | Gourmet humor and coercive aftermath require independent ordinary pleasures/private account. |
| Junko | `ZUNKO` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 9 | 9 | 3 | Gourmet frustrations and food pleasure require independent ordinary/private contexts. |
| Izumi | `IZUMI` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 11 | 11 | 5 | Tastes and boundaries after coercion require ordinary/private context, not uniform Gourmet persona. |
| Kasumi | `CH0089` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 9 | 9 | 4 | Hot-spring ideology/control recognition and group work require ordinary/private comparison. |
| Meg | `CH0088` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 4 | 4 | 1 | Hot-spring labor and school-service wishes require independent ordinary/private preference. |
| Sena | `CH0081` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 7 | 7 | 4 | Named Emergentology / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through S2 V002 C002 E020; rejects war-as-medicine rhetoric and proposes joint inspection. |
| Erika | `CH0076` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 5 | 5 | 2 | Named ShinySparkleSociety / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through S2 V002 C002 E018; appears with technical coalition after broadcast starts. |
| Kirara | `KIRARA` | `MAIN_S2_V002`, `MAIN_V001`, `MAIN_V003`, `MAIN_V100` | 5 | 5 | 2 | Named ShinySparkleSociety / Gehenna role requiring an independent ordinary/private account. Current admitted-main coverage basis: Analyzed through S2 V002 C002 E018; appears after counterbroadcast and sees recovery. |


| Reading family | Retrieval families | Raw person keys | Bond | MomoTalk | Data |
|---|---:|---:|---:|---:|---:|
| `ABYDOS_PS68` | 11 | 11 | 116 | 116 | 47 |
| `MILLENNIUM` | 23 | 25 | 241 | 241 | 95 |
| `TRINITY` | 25 | 25 | 213 | 213 | 85 |
| `ARIUS` | 5 | 5 | 35 | 35 | 15 |
| `RABBIT_VALKYRIE_FOX` | 10 | 10 | 73 | 73 | 31 |
| `HYAKKIYAKO` | 17 | 17 | 126 | 126 | 49 |
| `GEHENNA` | 20 | 20 | 164 | 164 | 71 |
| **Total** | **111** | **113** | **968** | **968** | **393** |

**Yuzu/Eimi identity routing:** `BA_PERSON_YUZU` and `BA_PERSON_CH0336` preserve distinct raw registry/variant rows (10018/26009 versus 20055); `BA_PERSON_EIMI` and `BA_PERSON_CH0337` likewise preserve 10001/20032 versus 10136. Japanese spacing differs while personal name, school and club agree. These are retrieval families, not permission to transfer every variant context or temporal state. Positive examples are `BA:momotalk:10018:thread:100180010` → `BA:bond:10018:002` → `02_CANONICAL_STORIES/BOND/YUZU/VARIANT_10018_EPISODE_002.md` and `BA:momotalk:10001:thread:100010010` → `BA:bond:10001:002` → `02_CANONICAL_STORIES/BOND/EIMI/VARIANT_10001_EPISODE_002.md`. No source is called absent solely because the record’s participant array is empty.

**Kei identity inquiry:** `BA_PERSON_CH0335` has 6 bond, 6 MomoTalk and 6 data objects; `BA_PERSON_CHAR_101350001` has one data object. Review these 19 objects as distinct source identities and compare with main Key/`Kei.sav` evidence. Positive modern registry names/variants provide a retrieval route, not a backward identity or survival proof. They add no automatic reconstruction readiness.

## 5. Complete group and event review routes

All group sequences below are required. The sequence key is metadata navigation (raw group ID divided by 100), not a guessed institutional name or permission to fuse separate literary stories. Read each listed complete object; interpret sequence boundaries from its actual source.

| Group source sequence key | Exact required story IDs | Current full content review |
|---|---|---|
| 11 | `BA:group:1101`, `BA:group:1102`, `BA:group:1103`, `BA:group:1104` | ACCEPTED_WITH_LIMITS cycle002 |
| 12 | `BA:group:1201`, `BA:group:1202`, `BA:group:1203` | PENDING |
| 13 | `BA:group:1301`, `BA:group:1302`, `BA:group:1303` | PENDING |
| 14 | `BA:group:1401`, `BA:group:1402`, `BA:group:1403` | PENDING |
| 15 | `BA:group:1501`, `BA:group:1502`, `BA:group:1503` | PENDING |
| 16 | `BA:group:1601`, `BA:group:1602` | PENDING |
| 17 | `BA:group:1701`, `BA:group:1702`, `BA:group:1703` | PENDING |
| 18 | `BA:group:1801`, `BA:group:1802` | PENDING |
| 19 | `BA:group:1901`, `BA:group:1902` | PENDING |
| 20 | `BA:group:2001`, `BA:group:2002` | PENDING |
| 21 | `BA:group:2101`, `BA:group:2102` | PENDING |
| 22 | `BA:group:2201` | PENDING |
| 23 | `BA:group:2301`, `BA:group:2302` | PENDING |
| 24 | `BA:group:2401`, `BA:group:2402`, `BA:group:2403`, `BA:group:2404` | PENDING |
| 25 | `BA:group:2501`, `BA:group:2502` | PENDING |
| 26 | `BA:group:2601`, `BA:group:2602` | PENDING |
| 27 | `BA:group:2701`, `BA:group:2702` | PENDING |
| 28 | `BA:group:2801`, `BA:group:2802` | PENDING |
| 29 | `BA:group:2901`, `BA:group:2902` | PENDING |
| 30 | `BA:group:3001`, `BA:group:3002`, `BA:group:3003` | PENDING |
| 31 | `BA:group:3101`, `BA:group:3102`, `BA:group:3103` | PENDING |
| 32 | `BA:group:3201`, `BA:group:3202` | PENDING |
| 33 | `BA:group:3301`, `BA:group:3302`, `BA:group:3303` | PENDING |
| 34 | `BA:group:3401`, `BA:group:3402`, `BA:group:3403` | PENDING |
| 35 | `BA:group:3501`, `BA:group:3502` | PENDING |
| 36 | `BA:group:3601`, `BA:group:3602`, `BA:group:3603` | PENDING |


All 61 event packages are required for complete content review. Each includes every canonical story ID named under that `event_content_id` in `stories.jsonl` and the [event index](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md#3-complete-event-object-inventory). The nine `EVENT_80000` stories and sixteen `EVENT_80001` stories are separate person contexts and may require separate readings; no synthetic anthology plot is invented. The 28 objects with two event contexts are each read once while both contexts remain in provenance.

| Event package | Required canonical objects | Complete review |
|---|---:|---|
| `EVENT_801` | 13 | PENDING |
| `EVENT_802` | 11 | PENDING |
| `EVENT_803` | 21 | PENDING |
| `EVENT_804` | 13 | PENDING |
| `EVENT_805` | 9 | PENDING |
| `EVENT_806` | 11 | PENDING |
| `EVENT_807` | 1 | PENDING |
| `EVENT_808` | 12 | PENDING |
| `EVENT_809` | 20 | PENDING |
| `EVENT_810` | 102 | PENDING |
| `EVENT_811` | 12 | PENDING |
| `EVENT_812` | 15 | PENDING |
| `EVENT_813` | 19 | PENDING |
| `EVENT_814` | 16 | PENDING |
| `EVENT_815` | 13 | PENDING |
| `EVENT_816` | 17 | PENDING |
| `EVENT_817` | 11 | PENDING |
| `EVENT_818` | 19 | PENDING |
| `EVENT_819` | 11 | PENDING |
| `EVENT_820` | 15 | PENDING |
| `EVENT_821` | 16 | PENDING |
| `EVENT_822` | 9 | PENDING |
| `EVENT_823` | 6 | PENDING |
| `EVENT_824` | 1 | PENDING |
| `EVENT_825` | 16 | PENDING |
| `EVENT_826` | 13 | PENDING |
| `EVENT_827` | 14 | PENDING |
| `EVENT_828` | 15 | PENDING |
| `EVENT_829` | 15 | PENDING |
| `EVENT_830` | 12 | PENDING |
| `EVENT_831` | 12 | PENDING |
| `EVENT_832` | 10 | PENDING |
| `EVENT_833` | 10 | PENDING |
| `EVENT_834` | 38 | PENDING |
| `EVENT_835` | 16 | PENDING |
| `EVENT_836` | 47 | PENDING |
| `EVENT_837` | 19 | PENDING |
| `EVENT_838` | 21 | PENDING |
| `EVENT_839` | 15 | PENDING |
| `EVENT_840` | 17 | PENDING |
| `EVENT_841` | 19 | PENDING |
| `EVENT_842` | 15 | PENDING |
| `EVENT_843` | 9 | PENDING |
| `EVENT_844` | 10 | PENDING |
| `EVENT_845` | 12 | PENDING |
| `EVENT_846` | 13 | PENDING |
| `EVENT_847` | 15 | PENDING |
| `EVENT_848` | 30 | PENDING |
| `EVENT_849` | 14 | PENDING |
| `EVENT_850` | 12 | PENDING |
| `EVENT_851` | 17 | PENDING |
| `EVENT_852` | 10 | PENDING |
| `EVENT_853` | 13 | PENDING |
| `EVENT_854` | 29 | PENDING |
| `EVENT_856` | 15 | PENDING |
| `EVENT_859` | 14 | PENDING |
| `EVENT_860` | 27 | PENDING |
| `EVENT_861` | 13 | PENDING |
| `EVENT_862` | 15 | PENDING |
| `EVENT_80000` | 9 | PENDING |
| `EVENT_80001` | 16 | PENDING |


Priority follows complete reading and uses `CORE`, `HIGH`, `SUPPORTING` or `UNASSESSED` separately from function and workflow. A quiet story can be core. Assess literary characterization, social context, recurrence/difference, ordinary repertoire, contrary evidence and continuity consequences. Record intrinsic ordinary value even when no durable state changes. A disposition that declines a specific claim does not discard the source. The independent stable-ID rotation begins with `EVENT_80000` and continues across unassessed packages alongside inquiry-led work. All-package review closes the rotation fairly.

## 6. Other source classes and explicit debts

**Mini:** 29 of the 46 mini objects are positive metadata leads for the baseline principals. Their exact IDs appear below. Review coherent complete sources; admit relevant ordinary material and retain reasons when an object is outside a particular claim. Remaining minis stay visible. Inspecting all 46 is permitted if their review reveals relevant schools/people; do not reject the other 17 for low stakes or lack of current main-plot overlap.

`BA:mini:70000010`, `BA:mini:70000020`, `BA:mini:70001020`, `BA:mini:70001030`, `BA:mini:70002010`, `BA:mini:70002020`, `BA:mini:70003020`, `BA:mini:70004010`, `BA:mini:70004020`, `BA:mini:70004030`, `BA:mini:70005010`, `BA:mini:70005020`, `BA:mini:70005030`, `BA:mini:70006010`, `BA:mini:70006020`, `BA:mini:70007010`, `BA:mini:70007020`, `BA:mini:70008020`, `BA:mini:70008030`, `BA:mini:70012010`, `BA:mini:70012020`, `BA:mini:70013010`, `BA:mini:70013020`, `BA:mini:70013030`, `BA:mini:70013040`, `BA:mini:70013050`, `BA:mini:70015010`, `BA:mini:70015020`, `BA:mini:70015030`.

**Special-operation/unclassified:** 96 and 334 objects respectively remain source-class/continuity inquiries. Metadata routes for relevant principal IDs are in the dispatch. Resolve any required identity, mode or missing contextual claim through exact full-source review. They cannot silently fill a main gap or supply default behavior. An identity/mode limitation may remain explicit where the assigned textual claim does not need it; a required outstanding source blocks that claim and corresponding completion requirement.

**Unresolved character data:** 27 objects lack a verified person route. Six profile routes are `BA:character_data:19002:profile_and_dialog`–`:19006:profile_and_dialog` and `BA:character_data:29003:profile_and_dialog`; six contextual-only routes are `BA:character_data:9009000:contextual_only`–`9009005:contextual_only`; fifteen event-costume records have zero or unresolved character IDs. The full exact metadata is retained in the dispatch and the locked inventory. Do not assign those records to a named NPC by expectation.

The following major/context-special subjects remain required in their arc assessments even though no direct canonical person/private-data route was verified from the registry/variant/source metadata. This is a routing result, not a claim that the entire franchise contains no such scene. Inspect complete group/event content and unresolved source identity where relevant; retain actual main evidence and audience limits without inventing a private persona.

| Main-only or identity-special subject | Required arc assessment | Current direct private route |
|---|---|---|
| Aoi | `MAIN_S2_V000`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Arona | `MAIN_V000`, `MAIN_V100`, `MAIN_S2_V000`, `MAIN_S2_V001`, `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Asagiri Suou | `MAIN_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Ayame | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Ayumu | `MAIN_S2_V000`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Azami | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Beatrice | `MAIN_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Council-president claimant (identity-disputed role actor) | `MAIN_S2_V001`, `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Decalcomania | `MAIN_S2_V000`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Decartes | `MAIN_V004` | NOT VERIFIED; preserve stated identity/source limit |
| Francis | `MAIN_V100` | NOT VERIFIED; preserve stated identity/source limit |
| Funamori Sanae | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Golconda / Francis | `MAIN_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Heine | `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Kai / “Riku” (doctor; alias unresolved) | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Karen (Gehenna Restoration Committee) | `MAIN_S2_V002` | NOT VERIFIED; preserve stated identity/source limit |
| Kaya | `MAIN_V004`, `MAIN_V100`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Key | `MAIN_V002`, `MAIN_V100` | NOT VERIFIED; preserve stated identity/source limit |
| Kokuriko | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Komori Sumika | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Kuzunoha | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Maestro | `MAIN_V003`, `MAIN_V100` | NOT VERIFIED; preserve stated identity/source limit |
| Mai | `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Maia | `MAIN_V006` | NOT VERIFIED; preserve stated identity/source limit |
| Mayumi (Gehenna Restoration Committee) | `MAIN_S2_V002` | NOT VERIFIED; preserve stated identity/source limit |
| Momoka | `MAIN_S2_V000`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Orwell (Decalcomania screen/shadow; identity provisional) | `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Plana / A.R.O.N.A. (other-time-axis OS) | `MAIN_V100`, `MAIN_S2_V000`, `MAIN_S2_V001`, `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Prenapates (named, provisional) | `MAIN_V100` | NOT VERIFIED; preserve stated identity/source limit |
| Rei (diving team, provisional) | `MAIN_S2_V000` | NOT VERIFIED; preserve stated identity/source limit |
| Rin | `MAIN_V000`, `MAIN_V004`, `MAIN_V100`, `MAIN_S2_V000`, `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Sammy (shipboard cat) | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Sengoku Mitsuki | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Sensei | `MAIN_V000`, `MAIN_V003`, `MAIN_V004`, `MAIN_V006`, `MAIN_V100`, `MAIN_S2_V000`, `MAIN_S2_V001`, `MAIN_S2_V002`, `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Shiroko (other time axis, provisional) | `MAIN_V100` | NOT VERIFIED; preserve stated identity/source limit |
| Shoko (Gehenna Restoration Committee) | `MAIN_S2_V002` | NOT VERIFIED; preserve stated identity/source limit |
| Shuro | `MAIN_V005` | NOT VERIFIED; preserve stated identity/source limit |
| Sumomo | `MAIN_S2_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Tomoshita Ami | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Umiji Minato | `MAIN_S2_V003` | NOT VERIFIED; preserve stated identity/source limit |
| Underground Dweller | `MAIN_V001` | NOT VERIFIED; preserve stated identity/source limit |
| Yukino | `MAIN_V004` | NOT VERIFIED; preserve stated identity/source limit |
| Yume | `MAIN_V001` | NOT VERIFIED; preserve stated identity/source limit |


S2 V003’s 14 main metadata objects have empty `person_ids` arrays. Their checkpoint supplies the named Minato/Ami/Sumika/Mitsuki/Sanae/Sammy roster; participant-array emptiness cannot erase them. `EVENT_861` offers an Odysseia institution/ordinary-context investigation lead with registry people Kokoro and Kotone; their available private sources are a further positive route if actual relevance is established. They are not aliases for the main NPCs. Likewise the S2 dive-team Rei is not registry baseball Rei merely because the name matches.

Retain the [gap-impact register](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) IDs: G01 ordinary/private breadth; G02 Yuuka; G03 Serika; G04 Hina; G05 Arius/PS68; G06 cross-school ordinary life; G07 chronology; G08 event names/repeat contexts; G09 attribution; G10 performance; G11 Hoshino/Yume; G12 counterparts/system/variants; G13 office/contract/safety/technical outcomes; G14 mode continuity. Contextual sources can broaden repertoire without closing a different legal, clinical, technical or historical claim.

## 7. Reading ownership and transaction closure

Local Codex owns source-facing reading, with bounded delegated contributions authorized by the user. One integrator owns shared ledgers, coverage, controls, this mutable audit and the current entrypoint. Parallel contributors have distinct reading paths against the same pinned source and return complete analysis plus exact inspected IDs, source/admission scope, chronology, source-label limits, positive/contrary evidence and proposed ledger deltas. No contributor concurrently rewrites shared state.

Workload routing: metadata enumeration is `BOUNDED_STANDARD`; interpretive reading is `SUBSTANTIVE_ANALYSIS` with escalation for dense/ambiguous objects; all-arc reconciliation and semantic acceptance are `DEEP_SYNTHESIS`. The local text route is adequate for this stage and source transport was verified. No perceived audio/video or unobserved model/effort setting is claimed. Substantial Phase 3 synthesis retains its distinct preferred route and readiness gate.

Close each coherent source transaction before proceeding as current authority: complete source-facing reading, exact inspection/admission decision, applicable ledger/claim/coverage deltas, tested locators, and truthful progress/high-water state. Reuse topical homes and preserve old checkpoint DEFER decisions as historical. Prospective forecasts are not required by this goal; post-exposure comparison is retrospective unless a real prior freeze exists.

## 8. Input-snapshot progress and final completion audit

| Responsibility | Required | Accepted at this input snapshot | State |
|---|---:|---:|---|
| Main arc acceptance rows | 12 | 0 | NOT COMPLETE |
| Complete group stories | 65 | 0 | PENDING |
| Complete event packages / objects | 61 / 1,010 | 0 / 0 | PENDING |
| Principal bond objects | 968 | 0 | PENDING |
| Principal MomoTalk objects | 968 | 0 | PENDING |
| Principal character-data objects | 393 | 0 | PENDING |
| Distinct Kei identity inquiry | 19 | 0 | PENDING REVIEW |
| Relevant mini leads | 29 | 0 | PENDING RELEVANCE / FULL READING |
| All 7 ledger/control synchronization | 7 plus affected indexes/controls | 0 contextual tranches accepted | PENDING |
| Semantic, locator and exact-publication closeout | Required | Not performed for final Phase 2 state | PENDING |

Before changing this audit to COMPLETE, inspect actual current files and source routes against every P2 requirement and every arc row. Match the verification scope to the claim: valid paths do not prove complete reading; a few ordinary scenes do not prove the whole major roster; source counts do not prove sequence coherence; a model gate does not prove literary contextualization; a validator does not prove source-grounded priority. Record completed coverage, unresolved claim limits, consequential revisions and authoritative evidence of every gate. Any required uninspected object, missing accepted reading, unsynchronized ledger/control or unverified completion requirement keeps the goal active.

## 9. Historical accepted progress — cycle001, 2026-10-01

[Cycle 001](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md) accepts exactly 34 objects with limits after contributor and integrator review. The [supplemental object crosswalk](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv) carries exact 3452 IDs, canonical hashes, full-reading routes, admission decisions, priority/function reasons and separate chronology/attribution limits. All 3452 canonical files matched the pinned checksum manifest at initial route verification; only 34 have accepted literary inspection. Input hashes in §1 and zero-progress §8 remain the initial scope snapshot, not current completion.

| Responsibility | Required | Current accepted | State |
|---|---:|---:|---|
| Main-arc acceptance rows |12|0|NOT COMPLETE; packet reuse begins, full principal/private obligations remain |
| Complete group objects |65|8|57 remain; GROUP2101–2102/1201–1203/1501–1503 accepted |
| Event packages/objects |61/1010|2/26|59/984 remain; EVENT816 and EVENT80000 complete |
| Principal bond |968|0|Full Serika lane drafting; no draft counts as admission |
| Principal MomoTalk |968|0|Linked messages/pre-and-post scenes await acceptance |
| Principal character data |393|0|Written baseline candidates await acceptance |
| Kei identity inquiry |19|0|PENDING REVIEW |
| Relevant mini leads |29|0|PENDING RELEVANCE/FULL READING |
| Mandatory objects |3404|34|3370 remain |
| All tracked objects |3452|34|3418 remain AVAILABLE_NOT_REVIEWED |
| Seven-ledger/control integration |All accepted tranches|1 cycle|All 7 updated with exact scoped deltas/negative effects |
| Cycle publication |Required|PASS exact1d1fff8|Source36903659170, housekeeping36904406457, final36904450683 succeeded; exact status success |

Combined [main coverage](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) and [contextual coverage](../06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CONTEXTUAL_CHARACTER_COVERAGE_INDEX.md) have 23 partial/345 unmodeled/368 subjects, all standalone models NONE. The original main tables/history remain their dated snapshot; the companion overrides 30 existing rows and adds 16. The object CSV retains all 3,452 IDs and exact canonical hashes; global provenance and recoverable metadata remain in §1 and the pinned source-class crosswalk rather than repeated CSV columns. New Reijo and 15 generic role buckets have positive source-facing routes without identity merging; Reijo private metadata remains a contextual lead and can add principal obligations if actual later relevance earns them. The scope is not frozen to conceal a newly major subject. Nothing closes Hina redress, Yume record provenance, performed voice or missing legal/medical/technical outcomes.

**Phase 2 remains IN_PROGRESS.** All P2-R01–R09 and all 12 arc rows must pass before completion. The next independent rotation is EVENT80001 all 16; the inquiry lane is EVENT814 all 16; the complete private lane is Serika31; the group lane continues with GROUP1101–1104. Those candidates receive their own future semantic/ledger/coverage/publication acceptance. No quiet-source exclusion, empty model infrastructure or replacement of historical main readings is authorized by this progress record.

## 10. Current accepted progress — cycle002, 2026-10-01

[Cycle002](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_002_CHECKPOINT.md) adds35 complete objects after contributor/integrator review; current69 accepted. §9 and §8 retain prior dated counts; this section and the exact object crosswalk own the current census.

| Responsibility | Required | Accepted | Remaining / state |
|---|---|---|---|
| Main-arc rows | 12 | 0 | NOT COMPLETE; all five duties required per arc |
| Group | 65 | 12 | 53 |
| Event packages / objects | 61 /1010 | 2 /26 | 59 /984 |
| Principal bond | 968 | 13 | 955 |
| Principal MomoTalk | 968 | 13 | 955 |
| Principal character_data | 393 | 5 | 388 |
| Kei identity | 19 | 0 | 19 |
| Mini leads | 29 | 0 | 29 |
| Mandatory objects | 3404 | 69 | 3335 |
| All tracked objects | 3452 | 69 | 3383 |
| Seven-ledger integration | Every accepted cycle | 2 cycles | All seven closed with claim-specific limits |
| Cycle001 publication | Exact final audit | PASS1d1fff8 | 36904450683 success |
| Cycle002 publication | Author/source/housekeeping/final exact head | PENDING | Separate publication gate; acceptance does not assert push completion |

Current coverage23 partial/354 unmodeled/377 subjects, all standalone NONE:38 existing overrides plus25 new subjects,314 other main rows inherited. Serika private/written coverage is complete at this generation; that does not complete its events, all principal families or an arc. WholePhase2 remains IN_PROGRESS:all9 requirements and12 arc rows remain incomplete. Concurrent Yuuka/Ayane/Hoshino, group and event candidates are not yet admitted. No quiet-source removal or scope reduction.
