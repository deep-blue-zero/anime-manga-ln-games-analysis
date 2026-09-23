---
title: "Tokyo 7th Sisters — Opening Prerequisite Audit"
artifact_id: T7S_OPENING_PREREQUISITE_AUDIT
artifact_type: bounded_prerequisite_audit
series: Tokyo 7th Sisters
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "c20260909-r484 metadata and preserved client routing; official release paratext for entry-point routing only; no sequential analysis consumed"
architecture_lifecycle: INITIAL
created: 2026-09-09
last_updated: 2026-09-09
---

# Bounded opening-prerequisite audit

Current authority and live lock: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Gate history: [T7S_BOOTSTRAP_AND_GATE_RECORD.md](T7S_BOOTSTRAP_AND_GATE_RECORD.md). Dependency and schedule home: [T7S_TOPOLOGY_AND_CHRONOLOGY.md](../01%20Sources%20and%20Chronology/T7S_TOPOLOGY_AND_CHRONOLOGY.md).

## Decision OPA-0001

**Retain EPISODE 1.0 / アバンタイトル / 始まりの日 (第0話), episode `201000001`, as the first analytical reading candidate. The bounded prerequisite review supports reopening the readiness gate.** The preserved recommendation sequence places this introduction first, EP0.0 at positions 155–160, and EP0.7 at 163–165. The preserved client explicitly sorts that sequence in ascending order and supplies it to its recommendation service. This is positive evidence for the selected entry point, beyond episode numbering or an absence of prerequisite fields.

Within this scope, the proposed opening does not knowingly skip a documented EP0.0 or EP0.7 prerequisite. This is an evidence-bounded scheduling decision, **not a finding that the introduction has no allusions, assumes no onboarding knowledge, or is narratively independent of every other source**. No `REQUIRES_KNOWLEDGE_OF` edge, fictional chronology, character knowledge or literary interpretation is inferred from these ranks. EP0.0 and EP0.7 remain unconsumed; their eventual exact admission boundaries require their own prospective review. The ranks do not authorize an automatic 235-episode reading schedule.

## Scope and stopping rule

The owner authorized temporary closure and one prerequisite audit before reopening. GATE-0003 was published in commit `4acccc4` before the decision was made. The earlier source-recovery gate was insufficient to establish intended opening prerequisites; its history remains intact.

The question is whether EP0.0 or EP0.7 should precede the proposed EP1.0 introduction on documented presentation, recommendation, publication or access grounds. Permitted inspection covered native identifiers, parent links, titles, ordering and availability fields, tutorial flow/file metadata, a small client recommendation-code slice, and official publication paratext. The stopping condition is a supported entry-point decision with material uncertainties stated; it is not complete franchise chronology or a full historical unlock reconstruction.

No scenario dialogue, structured story pages, transcript prose, tutorial dialogue, audiovisual playback or character dossiers were read for this audit. Initial web searches incidentally exposed plot-bearing search snippets, official chapter synopsis snippets and out-of-scope card material; the release page also exposed track titles. These were quarantined from the decision and must remain in exposure history. No pristine first encounter is claimed. Source files and existing story-consumption counters remain unchanged.

## Native evidence and exact scope

Witness alias: `c20260909-r484`, `T7S_GAME_OFFLINE_JA_R484`. All row positions below are **zero-based JSON array indices**, not episode ordinals or fictional chronology. Main nodes use native category `0`; qualify layer IDs by category and witness. The source lock and locator protocol remain the external recovery route.

| Scope | Native scenario IDs | `m_scenario` row indices | `m_scenario_recommend` row indices | Recommendation `series` / `order` |
| --- | --- | --- | --- | --- |
| EP1.0 introduction | `201000001` | 6 | 6 | `100020` / **1** |
| EP0.0 | `101000101`, `101000201`, `101000301`, `101000401`, `101000501`, `101000601` | 0–5, in listed order | 0–5, in listed order | `100020` / **155–160**, respectively |
| EP0.7 | `811100101`, `811100102`, `811100103` | 1188–1190, in listed order | 202–204, in listed order | `100020` / **163–165**, respectively |

The introduction resolves to `scout_000_00_01.json.enc`, qualified hierarchy `100020 / 200030 / 300010`; the analytical script ID remains `scout_000_00_01.json__8df3fd723276f650`. EP0.0 belongs to family `200010`, and EP0.7 to `200020`, both under `100020`. The six EP0.0 records occur before the introduction in the physical master array while their recommendation positions occur much later. This directly demonstrates why array order and recommendation order must remain separate axes.

Integrity checks found 235 recommendation rows for series `100020`, unique orders covering 1–235 without holes or nonpositive values. `201000001` is the unique minimum; `201000101` follows at order 2. All 348 recommendation records, across both stored series values, join uniquely to `m_scenario`. The full other-series schedule was not interpreted.

The scoped `m_scenario_contents` records all have `campaign_id=0` and `start_time=0`: rows 0–6 for EP0.0/the introduction, and 1100–1102 for EP0.7. These offline values do not establish original release dates or historical unlock conditions. `m_scenario` has no explicit prerequisite field. Scoped reward rows describe rewards, not dependencies. Neither observation proves absence of gating elsewhere.

The 26 `m_tutorial_scenario` rows map IDs to tutorial filenames; none directly names these ten scenario files. The 11 `m_tutorial_flow` rows describe onboarding stages, including opening movie and episode-top transitions. They do not supply a join from tutorial completion to an EP0.0/EP0.7 requirement for this introduction. **Exact historical onboarding requirements remain unresolved.** Filename separation and the offline archive cannot certify the experience of a new account in every earlier client.

## Client routing corroboration

Static inspection of the preserved ARM64 client corroborates the meaning and direction of the recommendation field:

- `ScenarioRecommendMaster.GetSeriesScenarioList(int series)`, RVA `0x3C138B8`: filters records by the series value, calls `System.Linq.Enumerable.OrderBy<ScenarioRecommendMaster, int>` at `0x3C13A58`, then materializes the list.
- Its predicate at `0x3C13B50` compares the record's `Series` field at offset `0x14` with the requested series. Its ordering selector at `0x3C13B38` reads `Order` at offset `0x18`. These offsets agree with the recovered managed field definitions.
- `t7s.RecommendScenarioService.GetRecommendScenario(int series)`, RVA `0x40F61E0`, calls the ordered-list method at `0x40F6298`; its ID selector at `0x40F6634` reads `ScenarioId` at offset `0x10`, and the service retrieves corresponding scenario models.

This establishes a client recommendation route using ascending native ranks. It does not certify a particular current screen, every progress-dependent branch, a fresh-account playback trace, or a historical server-enforced unlock graph. No emulator reset or playback was needed for this decision.

## Publication cross-check

The official news post dated **2020-02-17** identifies EPISODE 0.7 as an **October 2019** release and presents it as the Seven Sisters final chapter. This corroborates treating its low episode number as insufficient evidence of an intended initial introduction. The source supplies a month, not a complete original release sequence. [Official soundtrack announcement](https://t7s.jp/news/2020/02/1657/)

EP0.0's original release date and the introduction's earliest release/revision history were not established by this bounded audit. The inherited secondary 2031/2043 setting claims were not reclassified or used to choose the opening. No fan reading order, synopsis interpretation or creator-interview story discussion is a decision premise. Official paratext is admitted here for routing only; it does not expand the literary witness or entering character-knowledge horizon.

## Counterchecks and remaining uncertainty

| Alternative or failure mode | Finding and consequence |
| --- | --- |
| Read 0.0 / 0.7 first because their numbers are smaller or their settings earlier | Unsupported as a prerequisite rule; directly conflicts with the preserved recommendation ranks. Keep numbering, diegetic time and schedule separate. |
| EP0.0 must precede the introduction because its rows appear first | Falsified as a recommendation-order inference: rows 0–5 have ranks 155–160, while row 6 has rank 1. |
| The recommendation table's name is an analyst guess, or order might descend | Addressed by the client method, field selectors and ascending `OrderBy` call. |
| The offline build proves all historical content was freely accessible | Rejected. Zero availability fields and a preserved menu do not reconstruct historical server or tutorial requirements. |
| An intended opening must require no prior knowledge of any kind | Not established. Recommendation evidence supports this candidate among the audited episode groups; onboarding, allusions and specific knowledge dependencies remain subject to bounded source evidence. |
| A later discovery can be silently imported into the first reading | Prohibited. If a load-bearing reconstruction needs unadmitted prior material, pause that dependent work, record the missing prerequisite and revise the boundary prospectively. Preserve earlier findings and exposure records. |

The unresolved historical onboarding and release questions do not identify a competing EP0.0/EP0.7 prerequisite and do not negate the positive recommendation evidence. They remain explicit limits, not silently resolved negative findings. Reopen this decision if an admitted source establishes a conflicting mandatory prerequisite, a relevant witness revision changes the routing, or the proposed first packet changes.

## Evidence binding and reproduction

Native master digests below bind the exact external JSON bytes inspected. Recover them through the locked collection's master namespace; filter by the scenario IDs and category-qualified ancestry above, join by `scenario_id`, then sort recommendation rows for `series=100020` by integer `order`. Recheck uniqueness, range and referential integrity before reusing the result. Do not query narrative text to reproduce this audit.

| Input | SHA-256 |
| --- | --- |
| `m_scenario.json` | `0409286e46697e8bfe474ec607b01c7065107ae1f0e4e161c4b316a49b129c65` |
| `m_scenario_layer.json` | `5fac27e3e6bea2381b29eaf95a72e5c5f1c78af502554b1b0cb62106dcefafdc` |
| `m_scenario_recommend.json` | `d4d90261fa085363ab0ac2bd190305f9d82d7f58952c70823134b3725e12cddb` |
| `m_scenario_contents.json` | `f16c534ceeef8581a9e0d95eb969ce06be0fce5783570c72e8aa67e1f81ae926` |
| `m_scenario_reward.json` | `163b6909832500f421afefc3bba0b35f4b6f16727998367451d4a0c974d35ab9` |
| `m_tutorial_scenario.json` | `56103bb6bb395920571dbc1d65f5671adac8088f5a007689659318c90434ca56` |
| `m_tutorial_flow.json` | `47eaa3bec2e3eed475181c0c7790ea4f524894a2a65a395a54ba4f35e8e8f170` |
| Preserved ARM64 `libil2cpp.so` | `d7cb61c1be25350dda842be1f34fda4d0acf4625a45a10abd0b4c73ac37291f3` |
| Recovered managed-definition `dump.cs` | `de7e34cad700c34624dc19de08ed50ac007e7c4fee1c65ba633f3fc16abfd47c` |
| Recovered method/metadata mapping `script.json` | `0795f1e56340edf1db6759a8832b91e90be468a223f01e0c6258de1dca69a86b` |
| Official release page capture | `dd3cd51dc40b90f24ba05875f16287b510d3906de792a7063c4ca50741878395` |

The official page was retrieved at `2026-09-10T00:54:24Z` (2026-09-09 in the project owner's timezone). Native scoped-row receipt SHA-256: `503c6354527e3f638691213216d3ded753eee03ebbc4d61510694af262421980`; recommendation-integrity receipt: `d8962f80fdecc2b91dbce9288525d54d248ad798dbe9d48494876cf2930dc10b`. These receipts, capture and bounded disassembly remain external; Git carries this concise decision and recovery coordinates, not source dumps. Client routing evidence is an auxiliary technical witness, not literary evidence.

## Gate consequence and analytical state

OPA-0001 supplies the missing opening-prerequisite decision for GATE-0004. The live lock remains owned by the entrypoint; the gate record must explicitly record the subsequent CLOSED → OPEN transition. The selected packet remains exactly 195 pages / 190 text records from episode `201000001`, with its prior recovery receipt unchanged. All Main/Sub/Event/additional/supplemental semantic consumption remains zero; every line frontier remains `NOT_STARTED`. No character, causal or claim-ledger entry is created by this audit.

Reopening records readiness only. This operation ends after the audited decision and verified branch publication. It does not start story analysis or grant continuous execution.

## Revision history

- 2026-09-09 — V1 / 1.0: OPA-0001 completed under temporary closure; retain the EP1.0 introduction on native recommendation evidence and bounded client corroboration, with historical and narrative limits stated.
