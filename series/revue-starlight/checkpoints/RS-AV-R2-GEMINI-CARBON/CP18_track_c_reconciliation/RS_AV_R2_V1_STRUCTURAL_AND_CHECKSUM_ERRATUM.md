---
title: "RS-AV-R2-GEMINI-CARBON — Separate Structural, Hygiene, & Checksum Erratum (Published V1 Corpus + Post-Freeze R2 Audit Errata)"
generation: "RS-AV-R2-GEMINI-CARBON"
artifact_type: "erratum"
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
model: "Gemini 4 Carbon (High reasoning)"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
existing_corpus_exposure: true
pinned_published_baseline_commit: "0bae19f328c3fdef82047e5753568fbb8478daed"
pinned_r2_freeze_commit: "224c52786b9b5a1d5edd6ce203bfb0714305627e"
pinned_r2_comparative_audit_commit: "724f8fb0fd79705fa3f1c558851d29b12dd2de1a"
document_role: "structural_and_checksum_erratum"
---

# Separate Erratum: `V1` Structural & Checksum Audit Findings (Plus Non-Retroactive `RS-AV-R2` Errata)

Per `governance/AGENT_ROUTING.md` (`§4.2` Duty of Correction and `§8.2` `#84-frozen-release-administrative-maintenance`), non-interpretive **structural, heading, concatenation, and checksum-audit findings** are separated here from the substantive literary and audiovisual reconciliation in `RS_AV_R2_V2_CLAIM_BY_CLAIM_RECONCILIATION_LEDGER.md`.

In addition, to uphold strict epistemic symmetry while preserving `CP16` (`224c52786b9b5a1d5edd6ce203bfb0714305627e`) and `CP17A` (`724f8fb0fd79705fa3f1c558851d29b12dd2de1a`) **byte-for-byte**, Part II records every post-freeze erratum identified in `RS-AV-R2-GEMINI-CARBON`'s own untouched earlier commits.

---

## Part I — Published `V1` (`2026-08-10`, `0bae19f3`) Structural & `CHECKSUM_AUDIT.md` Errata

### 1.1 Cryptographic Hash Integrity vs. Content-Hygiene Attestation Split

Programmatic byte verification across all `26` tracked files in `series/revue-starlight/` establishes a sharp distinction between **cryptographic digest accuracy** and **structural hygiene accuracy**:

1. **`FILE_CHECKSUMS.sha256` & `CORPUS_MANIFEST.md` SHA-256 Digests — `PASS` (`PRESERVE` Cryptographic Record)**:
   - Every SHA-256 digest, byte count (`887,449` numbered-synthesis bytes; `1,035,627` payload bytes), and file count (`25` hashed files in `FILE_CHECKSUMS.sha256`; `21` payload files in `CORPUS_MANIFEST.md` `L30–50`) matches the exact committed bytes on `origin/main` (`0bae19f328c3fdef82047e5753568fbb8478daed`) with **zero hash mismatches**.
2. **`07 Audits and Manifests/CHECKSUM_AUDIT.md` Hygiene Claims (`L13`, `L28`, `L39`) — `FAIL` (`REJECT` Hygiene Attestation)**:
   - `CHECKSUM_AUDIT.md` `L28` certifies: `- Repeated exact level-one heading scan: PASS`.
   - `CHECKSUM_AUDIT.md` `L39` certifies: `Document 10 was checked for an accidental concatenated second draft. The duplicate tail was removed before this definitive build...` (implying the definitive `00–15` build is free of concatenated second drafts).
   - Direct line-by-line inspection **falsifies both attestations across four numbered `V1` documents** (`04`, `05`, `06`, and `15`), proving that `V1`'s pre-release scan checked only *identical full-string `#` lines* (missing Roman-numeral and Appendix-letter collisions with slightly varied subtitles) and checked `Document 10` without catching `Document 04` and `Document 05`.

---

### 1.2 Exact Line-Anchored Structural Defects in `V1` & Canonical `V2` Repair Actions

| Affected `V1` File | Exact Defect & Line Locators | `CHECKSUM_AUDIT.md` Conflict | Canonical `V2` / §8.2 Repair Action |
| :--- | :--- | :--- | :--- |
| **`05 Full-Series Synthesis/04_MAYA_CLAUDINE_RIVALRY_PERFECTION_AND_EXPOSURE.md`** (`61,049` bytes, `1,643` lines, `SHA-256: a972d869...`) | **Unremoved `697`-line concatenated second draft (`42.4%` of file)**: Draft 1 progresses monotonically from `# I. Executive thesis` (`L21`) through `# XIV. Maya's 空っぽの器` (`L320`) … `# XXIII. あなたは美しい` (`L524`) … `# XXXVI. Comparative export matrix` (`L862`) to **`# XXXVII. Final synthesis` (`L915–L945`)**. Immediately at **`L947`**, the file resets Roman numerals backward (`37 → 14`) into a second complete back-half draft: `# XIV. Audience and reciprocal exposure` (`L947`), `# XV. あなたは美しい` (`L1057`), `# XVI. Wager, tomorrow, and the repaired meaning of eternity` (`L1100`), `# XVII. Music, choreography, and visual form` (`L1195`), `# XVIII. Romantic and erotic coding` (`L1272`, duplicating `# XXXII` at `L752`), `# XIX. Relationship ethics` (`L1342`, duplicating `# XXXIII` at `L786`), `# XX. TV resolution → film pressure → revised understanding` (`L1395`, duplicating `# XXXIV` at `L814`), `# XXI. Contradiction audit` (`L1408`, duplicating `# XXXV` at `L826`), `# XXII. Comparative export matrix` (`L1470`, duplicating `# XXXVI` at `L862`), and a second **`# XXIII. Final synthesis` (`L1524–L1643`)**. | Directly falsifies `CHECKSUM_AUDIT.md` `L13` & `L39` (unremoved concatenated second draft; `10` collided `# XIV`–`# XXIII` Roman numerals; `2` competing `Final synthesis` conclusions). | Merge unique nuances from `L947–L1643` (notably `L1323–1335` on preserving rivalry rather than translating it away into conventional couplehood) into the single canonical structure (`# I`–`# XXXVII`), eliminate the `697`-line duplicate tail, and add `REC-12` (`TV10` Maya clasp cut `18:36.75` vs. Claudine manual cloak tear `19:11` + `"Ma Claudine"` `20:24`). |
| **`05 Full-Series Synthesis/05_MAHIRU_FUTABA_KAORUKO_CARE_DEPENDENCE_AND_DIFFERENT_ROADS.md`** (`56,367` bytes, `1,862` lines, `SHA-256: 9199a479...`) | **Concatenated duplicate Appendix block (`122` lines) + non-monotonic `D → H` jump**: After `# Appendix A` (`L1463`), `# Appendix B` (`L1513`), `# Appendix C — Six-outcome audit: Mahiru / Hikari` (`L1549`), `# Appendix D — Six-outcome audit: Futaba / Kaoruko` (`L1577`), `# Appendix E` (`L1605`), `# Appendix F` (`L1628`), and `# Appendix G — Care as embodied labor` (`L1659–L1689`), line **`L1690`** resets backward (`G → A`) to append a **second** `# Appendix A — Six-outcome audit of the Mahiru / Hikari Revue` (`L1690`, duplicating `L1549`), a **second** `# Appendix B — Six-outcome audit of the Futaba / Kaoruko film Revue` (`L1718`, duplicating `L1577`), a **second** `# Appendix C` (`L1746`), and a **second** `# Appendix D` (`L1794`), then skips `E, F, G` to `# Appendix H — Professionalization changes the meaning of care` (`L1812–L1862`). | Falsifies `CHECKSUM_AUDIT.md` `L13`, `L28`, & `L39` (`4` collided `# Appendix A`–`D` headings and duplicate six-outcome audit tables). | Deduplicate the `L1549–L1604` and `L1690–L1745` six-outcome tables, retain the non-duplicate content of `L1746–L1811` (`Care without jurisdiction` & `Unresolved tensions`) and `L1812–L1862` (`Professionalization`), and re-letter monotonically `# Appendix A` through `# Appendix J`. |
| **`05 Full-Series Synthesis/06_SEISHO_99TH_CLASS_ENSEMBLE_AND_CHARACTER_ECOLOGY.md`** (`45,922` bytes, `1,637` lines, `SHA-256: eef83055...`) | **Six-letter Appendix numbering gap (`F`–`K` missing)**: Progresses `# Appendix A` (`L1244`) through `# Appendix E — Limits of the ensemble ideal` (`L1519–L1609`), then jumps directly to **`# Appendix L — Why the 99th class is more than friendship` (`L1610–L1637`)**, omitting `Appendix F` through `Appendix K` (evidence of an excised interim block whose trailing heading letter was never renumbered). *(Also uses `# 1. Aijō Karen`–`# 9. Saijō Claudine` as H1 headings inside `# XVIII` at `L758–L982`.)* | Structural numbering defect missed by `CHECKSUM_AUDIT.md` `L13–22`. | Re-letter `# Appendix L` (`L1610`) to `# Appendix F` and demote `# 1.`–`# 9.` (`L758–L982`) to `## 1.`–`## 9.` under `# XVIII`. |
| **`06 Evidence and Indexes/15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md`** (`55,170` bytes, `577` lines, `SHA-256: 85ead2c5...`) | **Duplicate `# XIII` Roman numeral + overlapping re-indexed sections**: `# XIII. Index-use principle` (`L400`) is followed `17` lines later by a **second `# XIII`** (`# XIII. Formal self-introductions and identity declarations`, `L417`), after which `# XV. Address forms and relational voice markers` (`L449`) and `# XVI. Motif lexicon` (`L469`) partially duplicate `# X. Address forms and role/self markers` (`L342`) and `# XI. Motif vocabulary` (`L361`). | Collided top-level Roman numeral `# XIII` missed by `CHECKSUM_AUDIT.md` `L28`. | Renumber `# I`–`# XVII` strictly monotonically, merge `# X`/`# XV` and `# XI`/`# XVI` into unified non-overlapping index tables, and append `REC-22`'s verified `.ass`-vs.-audio correction table. |

### 1.3 Upgraded Programmatic Gate Required for `V2` `CHECKSUM_AUDIT.md`

Before `V2`'s `07 Audits and Manifests/CHECKSUM_AUDIT.md` may certify `PASS`, the build script must enforce **prefix-normalized H1 uniqueness** (checking Roman-numeral sequences `# I, # II, ...` and `# Appendix A, B, ...` for strict monotonicity without resets or gaps, not merely exact full-line string equality) alongside `python tools/validate_repository.py` and SHA-256 verification.

---

## Part II — Transparent Post-Freeze Errata on `RS-AV-R2-GEMINI-CARBON` (`CP16` & `CP17A` Preserved Byte-for-Byte)

Because `CP16_IMMUTABLE_FREEZE` (`224c52786b9b5a1d5edd6ce203bfb0714305627e`) and `CP17A` (`724f8fb0fd79705fa3f1c558851d29b12dd2de1a`) are frozen historical commits and are **never retroactively edited**, the following three self-audit errata are formally logged here and corrected in all proposed `V2` deliverables:

| Frozen `R2` Commit & File | Exact Line(s) | Erratum Description | Primary-Source Ground Truth & `V2` Resolution |
| :--- | :--- | :--- | :--- |
| **`CP16` (`224c5278...`)** — `01_tv_episodes/RS_AV_R2_TV01_DEEP_READING.md` | `L15` (`primary_video_sha256` YAML field) | Recorded an early transcription string (`f4dc5d4b...`) in `TV01`'s YAML header (already disclosed in `07_freeze/RS_AV_R2_IMMUTABLE_FREEZE_MANIFEST.json` `L24`, `L35` and `CP17A` `RS_AV_R2_POST_EXPOSURE_SELF_AUDIT.md` `L71`). | Verified SHA-256 of `Shoujo Kageki Revue Starlight - S01E01.mkv` is `a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250`. Corrected in `V2` `01 Source Lock and Inventory/SOURCE_INVENTORY.md` and `02 Television Series Readings/TV01_BUTAI_SHOUJO_DEEP_READING.md`. |
| **`CP17A` (`724f8fb0...`)** — `08_comparative_audit/RS_AV_R2_SYMMETRIC_COMPARATIVE_CLAIM_AUDIT.md` | `L52`, `L94`, `L197` | Compressed `CP16`'s accurate `TV05` `16:48–16:53` reading (`RS_AV_R2_TV05_DEEP_READING.md` `L58`, `L140`) into the imprecise shorthand *"cross-bout hit"* / *"Claudine's stray blow striking Hikari across bouts."* | Rechecked on `S01E05.mkv` (`16:38–16:56`): Claudine and Hikari are opponents **in their own rooftop bout (`Claudine vs. Hikari`)**; **only the distraction** (`Karen vs. Mahiru` below causing Hikari to look down and call `華恋！` at `16:45`) is cross-bout, while Claudine's strike (`レヴューの最中に よそみなんてね`, `16:49–16:52`) is strictly within their own bout (`REC-07`). |
| **`CP17A` (`724f8fb0...`)** — `08_comparative_audit/RS_AV_R2_SYMMETRIC_COMPARATIVE_CLAIM_AUDIT.md` & `RS_AV_R2_INTEGRATOR_HANDOFF_AND_PUBLICATION_PROPOSAL.md` | `Claim Audit` `L84`, `L168`, `L178`; `Integrator Handoff` `L80` | Misread broadcast SDH angle brackets `<大切な人達を\N幸せにしたいと思えば> <何度でも キラめける>` (`s01e05.analysis.ass` `21:57.06–22:03.40`, `[L352–L353]`) as song lyrics and wrongly faulted `V1` (`Doc 05` `L285`, `Doc 15` `L128`) for not labeling those words as `Fly Me to the Star`. | Rechecked on `S01E05.mkv` (`21:55–23:55`): `21:57.06–22:03.40` is **spoken (non-sung) inner narration (`心の声`)** (`口パクなし` closed-mouth smile over instrumental `劇伴`), whereas the credited `Fly Me to the Star` (#5 Mahiru solo) sequence begins at **`22:30.891` / `22:31.0`** (`22:31.26` bossa-pop intro; `22:38.5` sung vocal `♪ 私 ずっと あなたを 見てた`; `23:32.5` credit). `CP17A`'s criticism of `V1` on `21:57–22:03` is **retracted (`REJECT`)**; `V1`'s quote citation is **`PRESERVE`d** (`REC-08`), while `R2`'s `Fly Me to the Star` ED state-machine discovery stands on `22:31–24:00` (`REC-17`). |
