---
title: "Watayuri — Bootstrap Receipt"
artifact_id: WATAYURI_BOOTSTRAP_RECEIPT
artifact_type: bootstrap_receipt
series: "Yuri Is My Job! / 私の百合はお仕事です！"
generation: WATAYURI_BOOTSTRAP_V1
version: "0.1"
status: active_provisional
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-28"
source_boundary: "Metadata-only bootstrap; no narrative manga inspection"
canonical_home: series/watayuri/07 Audits and Handoffs/WATAYURI_BOOTSTRAP_RECEIPT.md
---

# Bootstrap receipt — owner audit candidate

- Repository: `deep-blue-zero/anime-manga-ln-games-analysis`.
- Exact `origin/main` base: `5b5166b14d2056db13c7380ac653b91c289be34f`.
- Stable branch: `series/watayuri`, created from that base. The **commit containing this receipt** is the bootstrap content commit; obtain its exact immutable SHA with `git log -1 --format=%H -- series/watayuri/07\ Audits\ and\ Handoffs/WATAYURI_BOOTSTRAP_RECEIPT.md`. A Git commit cannot literally contain its own hash. The publication result and remote head must also be verified independently at audit time.
- Entrypoint: `series/watayuri/CURRENT_STATE_AND_CORPUS_MAP.md`.
- Method: `series/watayuri/00 Frameworks and Methods/WATAYURI_ANALYTICAL_METHOD.md`.
- Synthesis architecture: `series/watayuri/00 Frameworks and Methods/WATAYURI_SYNTHESIS_ARCHITECTURE.md`.
- Reconstruction specification and source map: the corresponding `WATAYURI_CHARACTER_RECONSTRUCTION_SPEC.md` and `WATAYURI_SOURCE_AND_SCOPE_MAP.md` in that same frameworks directory.
- Initiation/routing: `project_initiation_gate: REQUIRED`; `PRESENT_VERIFIED` entrypoint; `PRESENT_UNREVIEWED` materialization; `active_provisional` authored files. Architecture lifecycle `INITIAL`.
- `SEQUENTIAL_ANALYSIS_LOCK = CLOSED`; reason `AWAITING_OWNER_BOOTSTRAP_AUDIT`. No substantive sequential findings existed at bootstrap. **No manga narrative page, dialogue, scene or booklet contents were inspected.**

## Exact authored paths

1. `series/watayuri/CURRENT_STATE_AND_CORPUS_MAP.md`
2. `series/watayuri/.repository/series-registry.json`
3. `series/watayuri/00 Frameworks and Methods/WATAYURI_ANALYTICAL_METHOD.md`
4. `series/watayuri/00 Frameworks and Methods/WATAYURI_SYNTHESIS_ARCHITECTURE.md`
5. `series/watayuri/00 Frameworks and Methods/WATAYURI_CHARACTER_RECONSTRUCTION_SPEC.md`
6. `series/watayuri/00 Frameworks and Methods/WATAYURI_SOURCE_AND_SCOPE_MAP.md`
7. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_RELATIONSHIP_AND_ATTACHMENT_LEDGER.md`
8. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_PERSONA_ROLE_AND_PERFORMANCE_LEDGER.md`
9. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_INFORMATION_DISCLOSURE_AND_MISREADING_LEDGER.md`
10. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_AGENCY_BOUNDARY_RUPTURE_AND_REPAIR_LEDGER.md`
11. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_CHRONOLOGY_MEMORY_AND_RETROSPECTION_LEDGER.md`
12. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_JAPANESE_SPEECH_ADDRESS_AND_REGISTER_LEDGER.md`
13. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_VISUAL_FORM_STAGING_AND_GAZE_LEDGER.md`
14. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md`
15. `series/watayuri/03 Longitudinal Ledgers/WATAYURI_CAST_AND_RECONSTRUCTION_READINESS.md`
16. `series/watayuri/07 Audits and Handoffs/WATAYURI_BOOTSTRAP_RECEIPT.md`

Nine longitudinal/readiness instruments have explicit schemas but **zero evidence rows**. They were kept separate because pair state, performed role, information distribution, concrete agency, chronology, written speech, manga form, claim revision and artifact readiness each have a distinct cumulative question. No proposed ledger was merged or dropped. No character or specialist artifacts were created.

## Source-reconnaissance boundary

Drive folder ID `1bKsOEQiLKU41cgW1Ht2Pt4qFj0nCdWwi`, inside evidence root ID `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`, had 18 direct objects at listing: V01–V14 Japanese EPUBs, separate V10 special-edition booklet, and `drive_propagation_manifest.json` (`1nUNuMWZWoaB_8iu1SoKuulHVDa0UgGQX`), `calibre_import_manifest.json` (`12hxsdZEFQimyis6OakpHUh76fq4oDCnI`), `CALIBRE_IMPORT.md` (`1kgxmaclUTZmb7iMSuZ1Dxo9UPPV0MQTt`). The source map records each filename, ID, size and available **local-source** hash. Drive metadata confirmed names and sizes, not remote hashes. No raw EPUB or page image entered Git.

## Validation and publication

The initial staged author preflight identified missing `jsonschema`, two prohibited full Drive URLs, and this receipt link before the receipt existed. The URLs were replaced by IDs; the repository's hash-pinned validation requirements were installed in an isolated scratch target; this receipt was then created. The staged author preflight passed for the authored content and reported `AWAITING_SYNCHRONIZATION` for exactly `governance/MANGA_ANIME_CORPUS_INDEX.md`, `series/README.md` and `series/registry.json`, the three housekeeping-owned projections of this new root. The command was `python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/watayuri --repo .` with the isolated dependencies in `PYTHONPATH`; it is rerun on the final staged candidate. The staging allowlist is the 16 exact paths above, with `git diff --cached --check` and full diff review.

Only the named root and its local descriptor are authored here. Housekeeping owns `series/registry.json`, `series/README.md` and the corpus index synchronization. The character curation agent owns global character files. A passed author preflight and a published stable branch do **not** establish integration readiness or owner approval; no PR or `main` merge is part of this bootstrap.

## Questions for owner audit

Assess whether all nine day-one instruments earn independent retrieval homes, especially whether speech and staging need this level of separation; whether the proposed page/EPUB locator policy is practical once V01 is structurally verified; and when or whether the V10 booklet and embedded bonus material deserve separate admission. The source file hashes have not been remotely rechecked. A future published-volume boundary has not been independently verified. These are explicit unresolved decisions, not defects silently resolved by the bootstrap.

**Next permitted operation:** owner audit of the Watayuri bootstrap architecture. Do not begin V01 until the owner approves the foundation and explicitly authorizes opening the sequential-analysis lock. This receipt documents construction and checks; it does not substitute for the owner's audit.
