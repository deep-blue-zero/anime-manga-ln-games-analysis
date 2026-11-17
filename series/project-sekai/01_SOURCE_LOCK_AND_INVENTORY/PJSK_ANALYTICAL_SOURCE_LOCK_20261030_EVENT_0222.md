---
series: PJSK
artifact_id: PJSK_ANALYTICAL_SOURCE_LOCK_20261030_EVENT_0222
artifact_type: source_lock
scope: SOURCE_REFRESH_CATCHUP_EVENT_0214_0222_AND_GENERATION_DELTAS
generation: SOURCE_20261030T035133Z
status: canonical
source_boundary: "PJSK_SOURCE_20261030T035133Z_EVENT_0222; collected Japanese canonical text"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Project SEKAI — source lock for the collected EVENT_0222 boundary

## Authority and authorization

The owner authorized catching up to the latest locally collected source material on 2026-11-06. This run adopts the verified source-pipeline generation below for new analysis. It continues the established architecture and the committed EVENT_0213 analytical state; it does not restart the project or rewrite the completed EVENT_0171–0213 campaign.

`SOURCE_COMPLETION_CUTOFF = PJSK_SOURCE_20261030T035133Z_EVENT_0222`.

The [earlier lock](PJSK_ANALYTICAL_SOURCE_LOCK.md), its frozen readings and the [EVENT_0213 handoff](../09_EVIDENCE_AUDITS_AND_MANIFESTS/PJSK_EVENT_0213_SYNTHESIS_RECONSTRUCTION_HANDOFF.md) retain their exact historical scope and bytes. This successor lock governs the new catch-up only. The [intake](../08_CURRENT_RELEASE/PJSK_0214_0222_REFRESH_INTAKE.md) and [corpus map](../PJSK_ANALYTICAL_CORPUS_MAP.md#current-state) distinguish source admission, completed analysis and reconstruction readiness.

## Pinned generation

| Field | Verified value |
|---|---|
| Pipeline run | `20261030T035133Z` |
| Certification | `2026-10-30T03:51:33.866700Z` |
| Pipeline / parser | `0.2.9` / `0.1.0` |
| Pipeline code commit | `3caa5135c3e342ba7050bfedbed4be4ad60269aa` |
| Preferred Japanese transcript | `ci-ke/ProjectSekai-story` at `aa9a7f878c0030bd9307fe085282f1fa6c154b40` |
| Separate secondary identifier witness | `StarMoe-org/Moe-story` at `761e9021c8bd5eb002aa30679f5f89e524153811` |
| Master data | `Sekai-World/sekai-master-db-diff` at `0735c4066d82c6ead011d6b1c128abbef4419eae` |
| Stories / scenes / ordered records | 15,962 / 21,635 / 452,818 |
| Classes | 125 main; 1,816 event; 2,806 card; 2,880 area; 52 self; 69 special; 8,214 My SEKAI |
| Event inventory | 220 story-bearing events through EVENT_0222; 0166 and 0186 absent |
| Last event | EVENT_0222 — MORE MORE JUMP！ Memories; 20 core episodes |
| Last event's initial-availability bucket | `RB_20261026T060000Z` |
| Temporal partitions | 6,113 dated; 743 condition-ordered; 9,106 undated |

The current local generated `corpus/` and matching retained `01_RAW_UPSTREAM` snapshots supply the evidence. Local absolute paths remain in the private operational receipt. Canonical story records outrank generated character, unit, relationship and LLM retrieval bundles. The secondary source verifies identifiers at its documented granularity; it is not an independent certification of Japanese wording.

## Verification and comparison

All **15,962 canonical story files** match the current build checksum inventory. The twelve governing metadata/audit files listed in the [delta manifest](../09_EVIDENCE_AUDITS_AND_MANIFESTS/PJSK_SOURCE_REFRESH_20261030_DELTA_MANIFEST.json) also match their build checksums. For the **748 distinct affected or reused source surfaces**, raw normalized segment hashes, canonical hashes, structured text digests, ordered record locators and source identities were verified. Integrity verification does not claim that newly admitted narrative text has already been read.

Compared directly with the frozen v0.2.7 analytical source generation, this generation adds **670 logical stories** and removes none: 89 event, 76 card, 74 area, 429 My SEKAI and 2 special stories. This is a larger comparison interval than the retrieval agent's last 499-story refresh. Nine complete event envelopes contain 273 memberships across 263 distinct stories; 42 of those stories were already read in the preceding campaign. Another 449 added stories lie outside these event envelopes.

Thirty-six existing stories have changed raw-segment hashes. Thirty-five retain identical normalized text, speaker identities, ordered locators and preceding stage context. The sole normalized text change is the orthographic `例え` → `たとえ` at `PJSK:event:0097:07:006:0049`; its surrounding exchange, attribution and meaning remain unchanged. Existing interpretation is **PRESERVE**. Historical quotations remain pinned to their original lock; future exact quotation uses the selected source version. No old reading is edited.

Forty-two existing card-story rows gain an EVENT_0218 association. Their earlier associations and release times remain intact; all 42 have verified prior-read receipts and unchanged text/locator/speaker context. Later envelope membership is not a new publication date, a repeated experience or a reason to reread unchanged material blindly.

## Admission and exclusions

The authorized catch-up covers complete EVENT_0214–0222 envelopes, all 449 additional source-generation additions, and the recorded older-source revisions. Event transactions remain sequential and atomic; non-event additions receive separate, context-aware treatment. The run stops at this exact collected generation. Further upstream changes require another declared source boundary.

The source completeness diagnostic remains **review**, despite passing raw preservation and event/card/main coverage checks. Opening/tutorial special parent `2` and `op_02area` are absent. My SEKAI's semantic master crosswalk remains unverified. The 495 raw `virtual_live` files are outside this canonical adapter and this catch-up; they are not silently admitted as canonical stories. No source acquisition or pipeline modification is part of this analytical operation.

Release timestamps, archive publication, unlock conditions and depicted chronology remain distinct. My SEKAI, alternate, special, recollected and performed-fiction contexts are not flattened into ordinary continuity. Singer manifestations keep their local histories and knowledge recipients.

The separately retained asset list is historical (`1.9.0.30`, iOS, source commit `475d81169f2a00f07195d766eb936b8168a5c72c`), not current-game asset authority. Existing audio certification covers 543 retained alignments; no new audio was fetched in the refresh and no independent AV inspection is claimed by this catch-up. Reconstruction packages remain R3 through EVENT_0140 until a separately scoped package revision is completed.
