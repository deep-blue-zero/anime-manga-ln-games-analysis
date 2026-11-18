---
series: WUWA
artifact_type: authority_transition_record
analytical_responsibility: "Attribute owner acceptance of existing Chapter II AV-reconciled character analyses as current authority without changing the historical AV audit or restricted evidence"
scope: WUWA_CH2_AV_CHARACTER_PACKET_ADOPTION_2026_11_18
source_boundary: "Existing pinned Wuthering Waves 3.6.0 semantic corpus and 2026-11-15 integrated Chapter II AV audit WUWA_RINASCITA_CH2_SHARED_AV_V01"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Wuthering Waves — adoption of AV-reconciled character packets (2026-11-18)

## Decision and attribution

The repository owner requested on 2026-11-18 that character entries reflect the Chapter II audiovisual work already performed and no longer misdescribe the validated character analyses as unaccepted drafts. This scoped adoption recognizes the eight previously published, AV-reconciled source-bounded reconstruction packets below as current `active_provisional` authority. The historical [Chapter II shared AV audit](WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_AUDIT.md) and its hash-bound [manifest](WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_MANIFEST.json) continue to describe the initial reconciliation **at the time it occurred**; their original `draft_noncurrent` status statements are not retrospectively falsified.

The transition changes **analytical authority/currentness**, not the pinned primary source, media authorization, semantic interpretations, or the completion state of unreviewed AV targets. It introduces per-character canonical current-state routers, changes the current-authority quartet for the owner-adopted analytical packet files, compiled model metadata and packet validators, and synchronizes the title-wide character index, claim index, README and current corpus map. Existing `PRE_AV` filenames and earlier generation identifiers remain provenance of their original construction, not present-status signals. The [character reconstruction protocol](../00%20Frameworks%20and%20Methods/WUWA_CHARACTER_RECONSTRUCTION_PROTOCOL.md) expressly allows current text/machine-audio authority with incomplete optional AV review.

## Adopted packets and observed AV bounds

| Character | Chapter II resolved scene targets | Directly listened solo lines (four dubs each) | Current status | Remaining scope |
|---|---:|---:|---|---|
| [Augusta](../04%20Character%20Analysis/Augusta/WUWA_AUGUSTA_CURRENT_STATE.md) | 19/32 | 8/605 (32 renders) | `active_provisional` | 13 crosswalk targets not resolved in this recording; 597 solo lines not heard in the calibrated cohort |
| [Brant](../04%20Character%20Analysis/Brant/WUWA_BRANT_CURRENT_STATE.md) | 5/38 | 6/606 (24 renders) | `active_provisional` | 33 crosswalk targets not resolved in this recording; 600 solo lines not heard in the calibrated cohort |
| [Cantarella](../04%20Character%20Analysis/Cantarella/WUWA_CANTARELLA_CURRENT_STATE.md) | 4/36 | 6/845 (24 renders) | `active_provisional` | 32 crosswalk targets not resolved in this recording; 839 solo lines not heard in the calibrated cohort |
| [Iuno](../04%20Character%20Analysis/Iuno/WUWA_IUNO_CURRENT_STATE.md) | 21/39 | 8/540 (32 renders) | `active_provisional` | 18 crosswalk targets not resolved in this recording; 532 solo lines not heard in the calibrated cohort |
| [Phoebe](../04%20Character%20Analysis/Phoebe/WUWA_PHOEBE_CURRENT_STATE.md) | 7/24 | 6/476 (24 renders) | `active_provisional` | 17 crosswalk targets not resolved in this recording; 470 solo lines not heard in the calibrated cohort |
| [Qiuyuan](../04%20Character%20Analysis/Qiuyuan/WUWA_QIUYUAN_CURRENT_STATE.md) | 5/27 | 5/255 (20 renders) | `active_provisional` | 22 crosswalk targets not resolved in this recording; 250 solo lines not heard in the calibrated cohort |
| [Shorekeeper](../04%20Character%20Analysis/Shorekeeper/WUWA_SHOREKEEPER_CURRENT_STATE.md) | 2/14 | 4/543 (16 renders) | `active_provisional` | 12 crosswalk targets not resolved in this recording; 539 solo lines not heard in the calibrated cohort |
| [Zani](../04%20Character%20Analysis/Zani/WUWA_ZANI_CURRENT_STATE.md) | 2/12 | 5/912 (20 renders) | `active_provisional` | 10 crosswalk targets not resolved in this recording; 907 solo lines not heard in the calibrated cohort |

## Explicit non-adoptions and limits

- **Changli, Jinhsi, Luuk Herssen and Yinlin** retain `draft_noncurrent` / `do_not_use_as_current_authority: true`. Scope-boundary notes on three of these are not direct Chapter II character analyses; Luuk Herssen's crosswalk was outside the recording scope.
- **Aemeath, Cartethyia, Chisa, Denia, Lynae and Sigrika** retain their existing current `active_provisional` authority and modality-specific unfinished work; Cartethyia's original current packet already contains Chapter II AV reconciliation.
- The 29h23m English-dubbed game recording is a **Chapter II main-story witness**, not the full game. Voice review used a **stratified 107-moment, 428-render, four-dub cohort**, not full-corpus listening. The six other characters' unresolved audiovisual work and all independently unreviewed scenes remain OPEN.
- Raw footage, client voice streams, audio waveform arrays and evidence capsules remain outside Git, in the restricted Drive/local evidence plane. The authority transition is not a new extraction, direct source inspection, or proof of reconstructed-character simulation fidelity.
- Source-freeze metadata conflicts, unobserved optional choices, event-image identities, speaker/asset anomalies and dub-specific uncertainties remain individually recorded; changing packet currentness does not resolve them.
- The global character discovery registry and its generated index are owned by the separate character-discovery curator. Any addition or expanded coverage for these adopted packets is a later evidence-qualification decision, not an unauthorized same-change registry modification on this series branch. No reconstruction-capability grades are created.

## Validation and historical preservation

Retain the Chapter II AV reconciliation audit/manifest, earlier import/adoption manifests, and frozen source releases byte-for-byte. Each changed analytical file must carry the current quartet (`status: active_provisional`, `release_state: owner_adopted_current_provisional`, `do_not_use_as_current_authority: false`, and unchanged genuine supersession fields), or an equivalent model authority field. Packet structure validators are adjusted for these correct state expectations; evidence/source constraints are unchanged. Publication requires the usual author preflight and the exact-head repository integration audit; this record does not itself assert those checks have passed.
