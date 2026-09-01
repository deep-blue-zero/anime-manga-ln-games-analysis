---
project: DJFW
artifact_type: corpus_map
scope: ongoing_comparative_corpus
generation: V1
status: active_provisional
source_boundary: "Cross-franchise doujinshi, hentai manga, all-ages fanworks, fanbooks, and related fan-created works analyzed at a high level for character voice, transformation pressure, subjecthood, canon relation, and cultural taxonomy."
analysis_root_id: 1j-SJWChEvVtkU9bRqszoocYzXVZxPkjB
source_root_id: 1sr196MHP1yqxMOHQoLZSjnLmAnGc46DL
control_sheet_id: 1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# DJFW_CURRENT_STATE_AND_CORPUS_MAP.md

## Project identity

**DJFW** is the canonical comparative corpus for doujinshi, hentai manga, all-ages fanworks, fanbooks, and adjacent derivative fanworks in the Manga / Anime archive.

This is not a series-specific architecture. It is a cross-franchise comparative project governed by method, source intake, character-baseline readiness, and case-by-case transformation analysis.

## Canonical roots

- Analytical root: `DOUJINSHI_FANWORK_COMPARATIVE_TAXONOMY` / Drive ID `1j-SJWChEvVtkU9bRqszoocYzXVZxPkjB`.
- Primary-source root: `DOUJINSHI_FANWORK_COMPARATIVE_TAXONOMY_SOURCES` / Drive ID `1sr196MHP1yqxMOHQoLZSjnLmAnGc46DL`.
- Operational control sheet: `DJFW_PROJECT_CONTROL_SHEET` / Drive ID `1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg`.

## Current authority

Read this file first. Then use:

1. `DJFW_PROJECT_ARCHITECTURE.md`
2. `00 Frameworks and Methods/DJFW_COMPARATIVE_METHODOLOGY.md`
3. `00 Frameworks and Methods/DJFW_READING_PROTOCOL.md`
4. `00 Frameworks and Methods/DJFW_CHARACTER_VOICE_AND_TRANSFORMATION_TAXONOMY.md`
5. `DJFW_PROJECT_CONTROL_SHEET` for sortable registry / ledger state.

## Current workflow

New works should enter through this sequence:

`register case -> add primary source -> source QA/extraction -> baseline resolution -> case-reading tree -> analysis -> Sheets ledgers -> current-state/taxonomy update -> closeout manifest`.

The case ID is assigned before source filing so that raw source folders, extracted reading copies, analysis documents, and ledgers do not drift.

## Current source state

Live primary-source packages are now present in the canonical DJFW source root for `DJFW_CASE_0001` and `DJFW_CASE_0002` through `DJFW_CASE_0010`. The 0002-0010 tranche is SHA-256 locked in `DJFW_CASE_0002-0010_CONTINUOUS_SEQUENTIAL_RUN_MANIFEST.md`; case 0008 is an exact duplicate source resupply and remains one case. Older handoff-only backlog entries outside these live cases remain metadata-only / reupload-needed unless their sources or prior evidence artifacts are recovered.

## Current analytical state

The governing taxonomy is inherited from the doujinshi/fanwork handoff, but this V1 architecture separates:

- method and protocol;
- primary-source inventory;
- case readings;
- character/pairing baseline readiness;
- Sheets-based comparative ledgers;
- synthesis and taxonomy state.

## Baseline policy

DJFW does not duplicate canonical series baselines. It points to existing series roots and creates short baseline briefs only when useful for fanwork comparison. Canon authority remains in the original series project.

## Safety and description policy

Analysis remains high-level and non-graphic. For R18 works and works involving adolescent/school-age fictional characters, analysis focuses on structure, tone, voice, transformation pressure, subjecthood, canon relation, and audience logic rather than explicit detail.

## Next recommended operations

1. Seed prior handoff works into the `Cases` tab as metadata-only / needs-reupload entries.
2. Create the first live case folder when a new work is uploaded.
3. Resolve the relevant character/pairing baseline before making strong fidelity claims.
4. Update `DJFW_TAXONOMY_STATE.md` only when a case materially changes the comparative model.

## Known limitations

This V1 corpus map preserves the project architecture and governing workflow. It does not preserve page-level evidence from prior uploaded works. Prior detailed source claims must be recovered from original files, existing artifacts, or re-uploaded source packages.

## Live case state update — 2026-08-28

`DJFW_CASE_0001` is registered as the first live case: `純潔の才能` / `Junketsu no Sainou` / working alias `Gift of Purity` (`Lycoris Recoil`, Bad Mushrooms / Chicke III / 4why).

Current state:

- Raw CBZ package uploaded to the DJFW source root.
- Extraction complete locally: 81 image/page entries from 83 ZIP entries.
- Extraction manifest uploaded.
- Page-order manifest uploaded.
- Safe blurred page-order contact sheet uploaded.
- Full OCR/transcription not performed.
- Lycoris baseline authority resolved through the current V2 corpus map and relevant voice/relationship synthesis artifacts.
- First-pass non-graphic case reading written.
- First-pass baseline comparison written.
- Control sheet updated: Cases, Sources, Extractions, crosswalks, Voice Fidelity, Subjecthood, Transformation Pressure, Canon Relation, Audience Orientation, and Value Assessment ledgers.

Corrected classification:

> institutional-training comedy / DA-service-skill parody / R18 yuri intensification / Chisato-Takina relationship-grammar preservation under genre pressure.

The prior handoff-derived works in the control sheet remain backlog metadata entries rather than live case IDs until their source packages or prior evidence artifacts are recovered.


## Live case state update — 2026-08-28 second pass

`DJFW_CASE_0001` now has a second-pass afterward/bonus-chemistry update.

Completed:
- Inspected p061-p080 for non-graphic bonus and afterword evidence.
- Uploaded `DJFW_CASE_0001_BONUS_AFTERWORD_LOCATOR_NOTES.md` / Drive ID `165jZQSS0tV4tPemRjEYBx4SL7dmkLrQf`.
- Added `## 15. Second pass: afterward and bonus chemistry` to the case reading.
- Added `## 11. Second-pass bonus/afterword comparison` to the baseline comparison.
- Updated Cases, Extractions, Voice Fidelity, Value Assessment, and Revision Ledger tabs.

Second-pass claim state:
> STRENGTHEN — bonus/afterword material materially supports the Chisato/Takina gap/exchange reading. The afterword confirms relationship gap/exchange as a stated creative method, while the bonus material confirms Chisato-forward / Takina-brake chemistry.

Scope limit: boundary-testing bonus material remains categorical only and should not be expanded into graphic description. Full OCR/transcription remains optional and is only needed for Japanese register-level claims.
.

## Method update — Diegetic Self-Audit Test

Created `DJFW_DIEGETIC_SELF_AUDIT_TEST.md` under `00 Frameworks and Methods` / Drive ID `1VRRHWE6EccxfDtafGmJvwq1tIYsxhECf2msKtid-ZtA`.

Purpose: reusable post-case framework for Re:Creators-style character self-recognition and delta analysis. Use after a case reading and baseline comparison to ask what canon characters would recognize, reject, concede, or identify as fanwork distortion.

Status: active_provisional until tested across multiple DJFW cases. It inherits the DJFW safety policy: for R18 or boundary-testing works, analysis remains high-level and non-graphic.



## Case sync update — 2026-08-28 Hiro/Gakumas cluster

The analytical root contains individual case-reading histories for `DJFW_CASE_0006` through `DJFW_CASE_0010`. Their earlier active-provisional V1 readings are now superseded provenance; the 2026-08-28 continuous-sequential V2 readings are current authority.

- `DJFW_CASE_0006` — `Ichijou 10-man Yen`: Hiro frailty-collapse / bodily-risk negative-control case. Voice fidelity low-to-medium-low; subjecthood reduced; Producer accountability weakened.
- `DJFW_CASE_0007` — `Shirayoi no Yado`: current positive Hiro fanwork benchmark. Occult/folklore AU converts Hiro-specific mismatch, calm, difficulty-seeking, and Producer entanglement into story grammar. Structural fidelity medium-high; behavioral grammar high.
- `DJFW_CASE_0008` — `Gakuen Ikisugi Master 4`: multi-character anthology. Hiro segment shows thin micro-fidelity through evaluative deadpan but reduced subjecthood. Later reupload confirmed duplicate; no second case created.
- `DJFW_CASE_0009` — `GakuMas Icha Love Ero Goudou / Dosukebe mode!!`: multi-artist Gakumas anthology. The mameojitan Hiro segment is now manually mapped and the prior OPEN state is retired; safe setup/closing evidence supports medium-high/high short-form Hiro fidelity, especially in frailty, shared aspiration, teasing, reciprocal constraint, and accountable difficulty.
- `DJFW_CASE_0010` — Typehatena negative-control case: character specificity is structurally subordinate to recurring artist-machine grammar. Closing-page Hiro depiction is registered, but does not make the work a Hiro-character artifact; it demonstrates visual presence without character authorship. Analysis remains categorical-only.

Current Hiro comparison is metric-dependent: `0007` is the strongest long-form transformative AU, while `0009` is the strongest short-form relational/voice compression; `0008` remains thin motif-first micro-fidelity, `0006` is a frailty-collapse negative control, and `0010` is a visual-presence-without-authorship negative control rather than a preservation candidate.

The Diegetic Self-Audit Test has now been applied informally to this cluster. Hiro's modeled self-audit emphasizes dry analytical correction: distinguishing works that understand her chosen difficulty and authored mismatch from works that merely use frailty, body, label, or visual design. This application is interpretive/provisional and should not replace the source-backed case readings.


## Continuous-sequential tranche closeout — 2026-08-28 — DJFW_CASE_0002-0010

The user authorized `continuous_sequential` processing through the nine supplied Idolmaster / Gakuen Idolmaster fanworks. The tranche is transactionally closed at `DJFW_CASE_0010`. All nine raw CBZs are now in the canonical primary-source tree with SHA-256/page locks, and `DJFW_CASE_0002-0010_CONTINUOUS_SEQUENTIAL_RUN_MANIFEST.md` / Drive ID `1B0YLxaV_V7ZXFsRBohXyaFbKFMPCG8Wn` is the run-level closeout authority. Cases 0002-0005 have new canonical V1 continuous-sequential readings; cases 0006-0010 have canonical V2 continuous-sequential readings superseding the prior first-pass artifacts. The old V1 files for 0006-0010 have been explicitly marked `superseded` and `do_not_use_as_current_authority: true` rather than silently overwritten as current analysis.

The Gakuen Idolmaster cluster intake reports have been routed to `08 Audits and Manifests` as provenance: `DJFW_GAKUMAS_HIRO_CLUSTER_001_FIRST_PASS_ANALYSIS.md` (`1jpJ7Jn6HWVtW4LnNP_Frr9kVuOngGCr0`) and `DJFW_GAKUMAS_HIRO_CLUSTER_002_FIRST_PASS_ANALYSIS.md` (`1uwwQTc1-vdflk5agWjzv3QiRAsXR1C4l`), together with their OCR-status sidecars. Their analytical front matter now marks them `historical_legacy`; individual continuous-sequential readings are preferred.

The telomereNA Minami quartet now has four source-locked case readings under the audited mobile-game Minami baseline. The strongest corpus-level result is that Gustav repeatedly exhibits explicit character-collapse awareness in afterwords. `Mizugi no Shita no Yuuwaku` remains the most costume/body-premise-driven but uses an official Minami trait as a bridge and acknowledges the risk of sexual-appeal-priority collapse. `Maid Shujuu Lovers` explicitly states that stronger personality transformation would require diegetic time because ordinary Minami would not simply become a different person. `Yoru made Matenai complete` is best understood as accretive relationship continuity rather than tightly preplanned long-form plot. `Otona no Sei ni Shite` is the strongest quartet case for private adulthood/self-authorization, while the canonical Minami audit prevents misreading that as the late creation of first-person desire.

The Hiro tranche also materially advanced. `Shirayoi no Yado` remains the strongest long-form transformative Hiro AU because frailty, calm, impossible-experience attraction, charisma, and Producer attachment are translated into occult story grammar. `Dosukebe mode!!` received the largest revision: the table of contents and safe segment mapping identify the mameojitan Hiro contribution, and its setup/closing dialogue strongly preserve the mature relation among weak body, shared dream, reciprocal constraint, teasing, and pleasure in accountable difficulty. Its prior OPEN fidelity state is therefore retired. `Gakuen Ikisugi Master 4` is corrected from one Hiro segment to two adjacent independently authored micro-segments. `Ichijou 10-man Yen` remains a useful frailty-collapse control. The Typehatena case remains categorical-only: Hiro's closing-page visual presence is registered, but voice, decisions, relationship grammar, and subjecthood remain unnecessary to the creator-machine mechanism.

The control sheet has been advanced across Cases, Sources, Extractions, source/baseline crosswalks, Voice Fidelity, Subjecthood, Transformation Pressure, Canon Relation, Audience Orientation, Value Assessment, Collapse Risk, and Revision Ledger state. Current analytical retrieval should start with this corpus map, then the control sheet/run manifest, then the individual continuous-sequential reading for the case. Cluster reports and superseded V1 readings are provenance only.
