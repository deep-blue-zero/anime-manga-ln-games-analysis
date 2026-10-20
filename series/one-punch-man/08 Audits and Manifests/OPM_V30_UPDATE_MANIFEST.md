---
series: OPM
artifact_type: manifest
scope: V30 complete sequential analysis and local cumulative closeout
generation: V2
status: canonical
source_boundary: Japanese tankobon V01-V30; V31 next after readback PASS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
closeout_result: PASS
---

# One Punch Man — V30 Update Manifest

## Closeout result

**PASS — V30 local closeout is complete.** Source reading, audit, freeze, comparison, checkpoint and propagation passed final readback. V31 may begin. Repository authority remains unchanged until gated integration after V37 and the corpus-wide audit.

## Source and complete coverage

- Source: `One Punch Man - Volume 30 [Japanese].cbz`, 130,364,472 bytes; 208 entries / 207 JPEG images, all 1221 × 1920.
- SHA-256: `59135310fd0cd775a14a51f8885e8206f9348536b45cd6eb80cc3b8a3636cfd8`.
- [Source audit](../01%20Source%20Lock%20and%20Inventory/OPM_V30_SOURCE_AUDIT.md): CRC, full decode, order, manifest and duplicate checks PASS, plus complete semantic lock.
- [Reading](../02%20Sequential%20Readings/OPM_V30_DEEP_READING.md): every image directly inspected in order; source observations retained before stable synthesis.
- [Japanese/register audit](OPM_V30_JAPANESE_DIALOGUE_AND_REGISTER_AUDIT.md): PASS, with 64 original images reinspected for load-bearing wording and attribution after the stable reading.
- [Crosswalk](../01%20Source%20Lock%20and%20Inventory/OPM_TANKOBON_CHAPTER_AND_EXTRA_CROSSWALK.md): exact frozen map copied. Front 0001–0008; chapter-plus-art 0009–0038, 0039–0072, 0073–0102, 0103–0130, 0131–0168, 0169–0195; extra 0196–0201; end matter 0202–0207. Chapter spans distinguish attached art internally.

The colophon gives 2024 without month/day. The extra is undated within story time. Repeated Genos intervention/dismantling views are intercuts, not evidence of a hidden repair or an archive duplicate. Edition/cover reproductions are not further narrative chapters.

## Prospective evidence and retrospective controls

Sections 0–15 froze at `2026-09-13T00:31:21.783062+00:00` after stable synthesis and Japanese/register PASS. Prospective SHA-256: `c36330b90d9d6d12184266115e791fb7a76988baf673e2c0870b8f3b61179cde`. `_staging/verification/V30_prospective_freeze.json` records source/audit/full-file hashes at that boundary. Authority metadata and later sections can change without altering the frozen region.

The audit preserves speaker, tense and certainty: Bomb's interpretation of hero entry; Bang's self-critique, future retirement and invitation; Genos's former-self counterfactual and present strength question; inherited sword lore, locally narrated response and subsequent cost; King's private concern and public misattribution; magazine captions versus unobserved production. No unresolved Japanese correction remains.

The entire combined V29–V30 V1 reading was opened only after this freeze. Twenty claim transitions preserve useful reputation/body/teaching themes while correcting Golden Sperm's chapter placement, a supposed new Amai/acid encounter, broad hero–monster opposition, omitted Genos/Bomb/CE material and unproved cosmic certainty. Prior limited heading/summary-line exposure remains disclosed; it is not disguised as fresh blindness. V31 material is excluded. Bounded RR qualifies earlier Bang, Bomb, Genos, Darkshine, Atomic, rescue, CE, King and body-mechanism evidence without revising earlier frozen observations. No redraw finding is made.

## Cumulative propagation

Thirteen established state homes receive one V30 delta each: four character-state ledgers, directional relationships, readiness, heroism/institution, body/personhood, power/cosmic, technology/hidden actors, satire/public narrative, visual form and open questions. The checkpoint ledger is the fourteenth cumulative artifact. Inventory, crosswalk and the single entrypoint advance their current routing while preserving historical boundary entries.

Bang moves **moderate -> strong** through private/longitudinal/relationship and role-conflict breadth. Bomb moves **insufficient -> emerging** through family history, nonlethal conduct and witnessing. Nichirin and Banehige gain newly routed **emerging** profiles. All other tiers remain unchanged. Readiness does not measure combat output or moral endorsement, and no specialist-ready promotion occurs.

## Checkpoint A

V30: **0 CONFIRM / 0 PARTIAL / 0 CONTRADICT / 11 NON_DIAGNOSTIC**. Cumulative V07–V30: **34 CONFIRM / 3 PARTIAL / 0 CONTRADICT / 227 NON_DIAGNOSTIC**, **264 decisions across 24 volumes**. Entering totals 34 / 3 / 0 / 216 and every prior decision remain unchanged. No mismatch class activates.

Genos's ethical change does not supply a new civilian-threat trigger, respectful challenge to a stated Saitama claim or disconfirmation of Saitama's power. Saitama's recalled gaming and short silent extra do not constitute clean fresh tests of the six predictions. Test fit remains separate from substantive model evidence.

## Verification and continuation

Final receipt: `_staging/verification/V30_closeout_readback.json`. The precloseout snapshot, all-image review, freeze, V1 reopen, checkpoint and propagation receipts remain under staging. Readback verifies source/cache bytes, all-image map coverage, unchanged prospective text and Japanese judgments, exact bounded artifact scope, one delta per home, preserved historical bodies and registry, readiness transitions, all 264 decisions, links/metadata, immutable source inventory and read-only repository baseline.

Global-index disposition: **NO CHANGE**. Existing canonical home `series/one-punch-man/` and `CURRENT_STATE_AND_CORPUS_MAP.md` remain the only authority routes. No raw image/cache/pilot payload enters Git. Methods, V01–V29 readings/audits/manifests and legacy material remain unchanged.

**Next after readback PASS: V31 fresh source verification and sequential primary reading.** The technical Tonari pilot remains narratively isolated. Git stays closed until full V37 completion and the V28–V37 corpus-wide audit; reread current governance and `CHANGE_INTEGRATION_CHECKLIST.md` immediately before eventual integration.
