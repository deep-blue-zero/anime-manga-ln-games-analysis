---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_CMR_PORT_AUDIT
artifact_type: analytical_port_and_authority_audit
scope: "CMR intake freeze; Japanese LN V01-V14"
generation: V2_CMR
version: "1.0"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md"
snapshot_date: 2026-10-11
repository_base_commit: "238fed779661f6a5a49d6a70034a6183d17ca175"
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Youjo Senki CMR Drive inventory and controlled analytical port audit

The intake inventory is closed for **20 files, five direct subfolders, and 32 retained file revisions** beneath the CMR Drive root (verified folder ID `1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4`). Nineteen current small-file originals were obtained through authenticated, explicitly bounded raw-file compatibility and verified by exact SHA-256 and byte length. The 52,894,654-byte locator corpus was regenerated deterministically from the fourteen hash-matching source EPUBs; its current Drive body was not materialized. This distinction is preserved in the machine manifest.

This is a **branch proposal**. No commit, push, main integration, or Drive pointer mutation is established by this audit. Effective methodological promotion awaits verified main integration and the separately verified former-Drive pointer update. The original method is retained as the revision-bound source; the proposed Git method is visibly labeled `active_provisional`. The historical first CMR1 audit is separately labeled `historical_legacy` and vetoed as current authority.

For public repository navigation, source identities are exposed as verified Drive IDs rather than new external Drive URLs. Lookup uses each record's `drive_id`; original names, parents and source coordinates are retained.

The machine-checkable [disposition manifest](YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) contains one record for each of the 25 inventoried files/folders. Every record binds original identity, role, size/hash basis, source status, dependency routes, exactly one disposition, and Git treatment. File records embed all 32 observed retained revision IDs, sizes, timestamps, MIME types and inspection states. The freeze describes the objects **at intake**; a later evidence append or pointer update must preserve this snapshot rather than overwrite its provenance.

## Inventory and original byte integrity

The current source filenames and original object IDs remain recoverable. Hashes in this table are exact original-byte hashes for all files except the locator, whose hash is confirmed by the recorded manifest and identical deterministic reconstruction.

| Original file | Drive ID | Original bytes | SHA-256 at intake | Disposition |
|---|---|---:|---|---|
| `YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md` | `16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh` | 43,630 | `405d89789d730ec3ccdff1de020d318dc39c9910b36577d2b3e1f63a52737361` | canonical Git analytical derivative or controlled migration |
| `README.md` | `1d6vk6xFzkML17mwbUmBrWyxNxftptkv4` | 7,294 | `cbb374eb7d6a55602300004bd3dda3a13bc3b773c7db46ee0dfef152aeb38059` | historical/superseded |
| `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_MANIFEST.md` | `1JxHeRuCRltCmQsyIs2nQruzewx1U8Bmd` | 14,888 | `43c1cf9bb04e2883e473a85d2db306b1242741569263778974db1b6229d5b02b` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_SCRIPT.py` | `1whdImFw-vUblagWfpiqEmY58hT1vd3LZ` | 98,103 | `23078662fed83e7aa8ba7c5e59fe9e0946a58ab75abab61a7de0a326e5e6909f` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2_DIAGNOSTIC_EVIDENCE_INDEX.tsv` | `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH` | 1,043,995 | `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2_ADJUDICATION_LEDGER.tsv` | `1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g` | 648,524 | `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_MANIFEST.md` | `1v3oLyOSuwD9WgZX_TvAPekRo20g4m_Rh` | 9,142 | `2edb901c91698f8bc460909193fc87175dff766181dddc2cf67bf7735121828b` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_SCRIPT.py` | `1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5` | 17,909 | `95e52f0e50f42c16eec4bb421245d7f150959478451559e6e47614052c87a074` | Drive-primary evidence/reference |
| `YOUJO_SENKI_TANYA_CMR2_CANDIDATE_SCENE_POOL.tsv` | `1LRcSX-k739E4O4xQ2ImZnawzx6IylARo` | 2,290,984 | `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_AUDIT.md` | `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51` | 26,319 | `30ace4c0f4a0b03aa003aea8e7377cb1595450bed326451908a59bf13c5c3417` | canonical Git analytical derivative or controlled migration |
| `YOUJO_SENKI_CMR1_READINESS_AUDIT_SCRIPT.py` | `1keRBa1MAecQmFefKgmnUMroSeOarf1B1` | 11,609 | `7a563001eef1e24259cb1637077665c5f47cd4690c5e8d9e2d417daeb0a13836` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_METRICS.tsv` | `13pEqvLZiv8Pc0SjvbsWSYpk_G4VMKZ0b` | 5,034 | `e5299ffeb29f542c7015003a3f0f8bb8f957793620eaa2d37957ea3a0eeeb6fb` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CHARACTER_ALIAS_MAP.tsv` | `1C95SxSuba7Fr9diTMyc1N8q58TbzxsLs` | 25,311 | `567426240c2072a21e6abea40775fd2428a6aec433f85417da2c8de08a8161a9` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md` | `1zWogK3vzZ0Tj1_92r3NaESIj1NzV1Biv` | 9,049 | `67120306369bb343f691f0007d5fbc968eb7de4a083a391f7adeb5914606eaad` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_SCRIPT.py` | `1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu` | 14,916 | `e21635d9f19d5925e2ad3f40aaaf2ac8cfff4d0f1dee8082c49415be09f04adc` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CMR_SOURCE_MEMBER_INDEX.tsv` | `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR` | 203,927 | `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220` | Drive-primary evidence/reference |
| `YOUJO_SENKI_CMR_SOURCE_LOCATOR_INDEX.tsv` | `140ow12czVj4J8Q_JR44MSWI98LUxj3uk` | 52,894,654 | `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe` | Drive-primary evidence/reference |
| `README.md` | `1VJj8j-KwC2ODJT7mkJcX1zvExrY4Cvl2` | 1,401 | `b937176e3c85e5b86a88b40e3343b9c66846bbb8d05be5c866464f0eca13e416` | working-only |
| `README.md` | `1B9k4mqImDwLNhZz4jrbXi85h5fSsN7dP` | 1,160 | `4149b405131c6752d343badea04ec7f83d1c231e9d328e2292009740fc665bf0` | working-only |
| `README.md` | `1Z7UPnnWeFoO2tpXxv1NfvWtcMkPwt63V` | 1,224 | `43a09f35d735cd04edff32e127cc843e0b3d6626ade794687c1c29f6a06263b1` | working-only |

The alias map has 44 logical data rows, the readiness metrics 20, and the member index 608. Small size is insufficient grounds for analytical import: the member/alias/metrics/candidate/diagnostic layers remain primary-source-derived evidence/reference objects. In particular, the 1,043,995-byte diagnostic export remains in Drive even though it lies just below 1 MiB. Its evidence and short-source-text aggregate are distinct from the newly authored paraphrased interpretive index required in Git.

The audited extraction, readiness, candidate, and adjudication scripts also remain Drive source/reference implementations. The local execution copies only implement declared runtime path substitutions. Their existence in a build cache creates no analytical authority or publication eligibility.

| Original folder | Drive ID | Direct files | Treatment |
|---|---|---:|---|
| 00 Frameworks and Methods | `1Ul_BbZkw9UkSOrDik3hmWVfcK84WWGvW` | 1 | Drive reference folder |
| 01 Evidence and Locators | `1aDiFqWjWHZ53xX-lBvjMLfA6eN89Z7SZ` | 16 | Drive reference folder |
| 02 Character Models | `1AMNfngVWTSm_4O0XadlJjHWjR8hMw21X` | 1 | Drive reference folder |
| 03 Relationship Registers | `1TomsYaw1BmQMRp-JuMils2PeHzl375uo` | 1 | Drive reference folder |
| 04 QA and Simulation | `1dPqF3RjqawccCi8LA59QVMXsp2KDvH63` | 1 | Drive reference folder |

No README exists directly in the CMR root or the Methods folder. Evidence has its v2.3 README; Models, Relationships, and QA each have one scaffold README and no finished artifact at intake. Folder fetch returned the complete direct contents of each folder (all below the 100-child boundary). Search alone omitted TSV and Python MIME classes, so its Markdown-only result was not treated as a full inventory.

## Live-state reconciliation and preservation

The observed current Drive state matches the supplied V12 starting snapshot and the existing Git series entrypoint:

| Layer | Verified intake state |
|---|---|
| Governing method | v1.1; complete original body obtained |
| CMR0 | 14/14 locked Japanese EPUB hashes; 608 members, 222 text-bearing members, 63,812 locators; zero member extraction errors |
| CMR1 | First audit of 20 subjects; qualitative classifications and ceilings preserved in the historical baseline |
| CMR2A | 1,200 candidate centers across V01–V14 |
| CMR2B ledger | 1,045 V01–V12 candidates; 607 `RETAIN`, 383 `MERGE`, 55 `REJECT` |
| CMR2B diagnostic evidence | 676 V01–V12 provisional states; 619 `HIGH`, 57 `MODERATE` |
| Remaining candidates at intake | 92 V13 plus 63 V14 = 155 |
| Mature models, directional matrix, QA | Not present in Drive at intake; their absence is preserved as pending work |

Logical TSV parsing found zero ragged rows and zero duplicate candidate/ledger/diagnostic identifiers. Every frozen ledger candidate resolves to the 1,200-row source pool, every ledger diagnostic reference resolves to the 676-row diagnostic index, and every diagnostic source-candidate reference resolves to the candidate pool. This checks identity/referential integrity; it does not turn heuristic tags into speaker/focalizer or behavioral judgments.

The locked current V12 ledger hash is `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0`; the current V12 diagnostic hash is `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68`. Existing row values, dispositions and diagnostic IDs must survive the V13–V14 append. Cross-volume consolidation adds a many-to-one route without erasing the original evidence history.

The original locator rebuild reproduces `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`, and the member rebuild reproduces `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220`. Candidate retrieval reproduces `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a`, independently matching the recovered original candidate bytes. Exact Japanese wording and markup still require the source XHTML where load-bearing; whitespace-normalized extracted text is a routing layer.

## Revision coverage and unavailable historical bytes

Two method revisions are exposed: the original 34,642-byte revision and current 43,630-byte v1.1. The current method bytes were recovered. Reading the previous revision's media returned **403 FORBIDDEN**; that previous body's hash and content comparison remain unverified.

The ledger exposes twelve cumulative revisions, ending with the 648,524-byte V12 revision. Its current exact bytes were recovered. The connector's readable revision-media operation does not support `text/tab-separated-values` or `text/x-python`; older ledger/script byte comparisons were not asserted. The remaining 18 files each expose a single retained revision. A single retained revision does not prove that earlier working versions never existed.

All 32 exact revision IDs and sizes are frozen in the disposition JSONL. Historical entries carry `content_sha256: null` and `historical bytes not obtained` instead of invented integrity. Current originals have their exact verified hashes; the locator current revision retains its non-download inspection distinction.

Initial streamed materialization failed on the executor's authenticated-download DNS route. This was a transport failure, not a denial of current Drive-file ownership. The task's orchestrating caller explicitly opted into bounded compatibility for the known small files, with a separate named bound for the 2,290,984-byte candidate pool. No giant-locator inline download, source-byte relocation into Git, or Drive mutation followed from that exception.

## Controlled transformations and authority mapping

| Source analytical responsibility | Proposed Git artifact | Transformation and authority state |
|---|---|---|
| v1.1 CMR method, Drive `16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh` | [Git method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md) | Metadata normalization/routing and an explicit port notice; full substantive body preserved; `active_provisional` branch proposal |
| First CMR1 audit, Drive `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51` | [Historical readiness baseline](YOUJO_SENKI_CMR1_READINESS_BASELINE.md) | Metadata/provenance and a baseline notice; all 20 classifications, individual ceilings and source locators preserved; `historical_legacy`, veto=true |
| Original evidence, scripts and folder inventory | [Disposition JSONL](YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) and this audit | Newly authored interpretive provenance/pointers; no raw evidence files imported |

The method changes exactly: `supersedes: null` and `superseded_by: null` to arrays; Drive `canonical_home` to the named Git home; parent-analysis metadata to the established Git V2 home; addition of source revision/hash, pending-promotion and unperformed-pointer fields; and a prefatory routing table that labels the original Section XV hierarchy historical. The original body's SHA-256 remains **`c943b0ce3867c4952cefb8209766e15a47f482133ad2d68420af17b31e3c45f3`**. The transformed file is **46,185 bytes**, SHA-256 **`b4c9a7acc067d891c01f645ce7919f562c97fc00492cec16523df39d2cf1d3a2`**.

The readiness baseline changes exactly: null supersession fields to arrays; `active_provisional` to `historical_legacy`; veto=false to veto=true; artifact type/home/identity to a baseline provenance responsibility; addition of source revision/hash and original-status fields; and a baseline notice. The original body's SHA-256 remains **`ed9dd9a46a94eddead7f85c154e5b2027490916e4197a5d24728b22b2bf48542`**. The transformed file is **28,832 bytes**, SHA-256 **`1376c6a798ea8fad7117adeaf64a8322a6bb495cf7a6fb1c29758c5834343859`**. No substantive body line, original classification, individual inference ceiling or exact locator is removed or revised.

Current Git responsibilities are intended under `CMR/Methods`, `CMR/Evidence`, `CMR/Models`, `CMR/Relationships`, `CMR/QA`, and `CMR/Provenance`, while source-derived bulk remains in Drive. These allocations do not authorize empty scaffolds or a parallel V3 literary corpus. The mature V2 corpus remains intact. The current first-read route is [the series entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md); the planned subordinate `CMR/README.md` is the integration owner's responsibility.

The planned former-Drive metadata pointer for the method must identify the accepted Git method and explicitly state the source-copy/provenance role after verified main integration. The first CMR1 source audit must route current readiness to the accepted current coverage home while retaining the first-audit freeze as historical provenance. Neither pointer update is claimed complete here. No global migration crosswalk, authority scope, owner registry or housekeeping-owned index is changed by this project-local port.

## Eligibility and remaining acceptance

Each analytical port artifact is UTF-8/LF and below 1 MiB. No large-text exception is requested. The 52.9 MB extracted locator and all original evidence exports remain in their Drive evidence home; Git LFS does not change that disposition. The public artifacts contain source IDs, safe source filenames, hashes, analytical arguments and metadata routes, with no local machine path, credentials, signed download URL, inline base64, EPUB payload or bulk Japanese source text.

The preserved method retains the mandatory five-channel separation and six-step speech transformation. Source anchors and inference ceilings still control future models; generated examples remain outside the evidence corpus. This port preserves methods and first-audit provenance. Tanya's source closure, current subject re-audit, diagnostic consolidation, completed models, relationship reconstruction, independent QA, final entrypoint, publication and exact-head integration remain their distinct acceptance responsibilities.
