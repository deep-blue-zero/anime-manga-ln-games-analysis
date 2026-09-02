---
title: "Classroom of the Elite — Evidence Reconciliation Audit for Y1V05–Y1V07.5"
artifact_type: "evidence_reconciliation_audit"
checkpoint_id: "Y1-CP02"
version: "1.0"
status: "PASS_AFTER_TERMINOLOGY_METADATA_REPAIR"
source_boundary: "Y1V05–Y1V07.5"
cumulative_boundary: "Y1V01–Y1V07.5"
spoiler_boundary: "through Y1V07.5 only"
tranche_evidence_entries: 377
cumulative_evidence_entries: 652
validated_text_locators: 346
validated_visual_locators: 31
terminology_passage_entries: 146
created_at: "2026-08-12"
updated_at: "2026-08-12"
---

# Evidence Reconciliation Audit
## `Y1V05–Y1V07.5`

# 1. Result

> **PASS_AFTER_TERMINOLOGY_METADATA_REPAIR**

The four canonical volume artifacts, checkpoint evidence snapshot, source maps, and Japanese-source identities reconcile without missing or duplicate evidence entries. The only required repair was a stale terminology-index YAML count: the table contained 146 validated rows while metadata said 157. The checkpoint snapshot now records the actual count.

# 2. Artifact reconciliation

| Volume | Expected evidence | Artifact evidence | Ledger evidence | Source hash | Result |
|---|---:|---:|---:|---|---|
| `Y1V05` | 77 | 77 | 77 | `083a6151a29c3efb6fdfe9de9a4e133975dd1d7aa6460e17510171db17b67abe` | PASS |
| `Y1V06` | 73 | 73 | 73 | `fed319353078c3790fbe0348550642599e7003258b257b79a4f8354ab9ea5c12` | PASS |
| `Y1V07` | 116 | 116 | 116 | `f36da0aafdef2e6f7789750754a65ff5bcf61c5479e48a1d07ca51b1a6eae097` | PASS |
| `Y1V07.5` | 111 | 111 | 111 | `809b78ada556e4c1885d3ea3f856e784bebf6ad762491a0cd4f741e0f20d925a` | PASS |
| **Total** | **377** | **377** | **377** | — | **PASS** |

- Tranche evidence IDs: **377**.
- Unique tranche IDs: **377**.
- Cumulative evidence through `Y1V07.5`: **652**.
- Missing IDs: **0**.
- Duplicate IDs: **0**.
- Unexpected IDs: **0**.

# 3. Locator validation

- Text locators validated: **346**.
- Visual locators validated: **31**.
- Total validated: **377/377**.
- Locator errors: **0**.

Validation confirms:

- each spine/paragraph range exists in the frozen extraction;
- each XHTML path matches the paragraph map;
- each image locator resolves to an EPUB resource;
- Volume 5's historical spine offset is applied explicitly;
- no source locator points into Volume 8 or later material.

# 4. Source identity

| Volume | EPUB SHA-256 | Normalized-text SHA-256 | Paragraphs | Japanese characters |
|---|---|---|---:|---:|
| `Y1V05` | `083a6151a29c3efb6fdfe9de9a4e133975dd1d7aa6460e17510171db17b67abe` | `a1af41937668e9a78541426dedabd4e5b1308d9acdc80e6860db8fbb9dbd6d3a` | 3,603 | 145,015 |
| `Y1V06` | `fed319353078c3790fbe0348550642599e7003258b257b79a4f8354ab9ea5c12` | `684c46f94745ab37881e3f62034e9b29307e5f2b4291376376e3eb18581078dc` | 3,620 | 150,989 |
| `Y1V07` | `f36da0aafdef2e6f7789750754a65ff5bcf61c5479e48a1d07ca51b1a6eae097` | `82247b695ae062dcb154d75330c4bf93a2a3c6f2b1fa69bdb26b23ef5e020d1a` | 4,031 | 133,528 |
| `Y1V07.5` | `809b78ada556e4c1885d3ea3f856e784bebf6ad762491a0cd4f741e0f20d925a` | `61246a54758030821a292588fbbc71a54e5d062dbfdaefb0fa69f9b6fc286e3d` | 3,820 | 124,881 |

All source identities match the canonical volume YAML and source map.

# 5. Terminology and language audit

The frozen checkpoint index contains **146** actual Japanese terminology/passage rows. Its prior metadata value of 157 was stale. The correction changes no quotation, locator, or interpretation.

The tranche's most important indexed formulations include:

- `相手を見ること`;
- `相手に主導権を与えること`;
- `自分自身が決めるもの`;
- `存在意義`;
- `仲間`;
- `熱量`;
- `戦略も、知略も関係ない`;
- `信頼`;
- `存在意義` in Kushida's approval economy;
- `切り捨てる`;
- `見捨てるわけにはいかない`;
- `所有物`;
- `俗世間`;
- `自由とは何か`;
- `恐怖`;
- `宿木`;
- `かけがえのない存在`;
- `必要不可欠な存在`;
- `ホワイトルームを出ても尚、やはりホワイトルームの中`.

# 6. Structural and spoiler QA

| Check | Result |
|---|---|
| Canonical filenames | PASS |
| UTF-8 decoding | PASS |
| YAML front matter | PASS |
| Evidence-ID contiguity | PASS |
| Source locator recovery | PASS |
| Japanese-source identity | PASS |
| Later-volume leakage | PASS |
| Unresolved placeholders | PASS |
| Chat-wrapper or file-citation markup inside archival prose | PASS |
| Copyrighted EPUB payloads in checkpoint package | PASS |
| ZIP CRC integrity | PASS |


# 7. Package integrity

- Package files: **29** including the internal checksum registry.
- ZIP CRC test: **PASS**.
- Source EPUB payloads: **excluded**.
- Volume 8 and later analysis: **excluded**.
- Final archive SHA-256: recorded in the external `.zip.sha256` sidecar.

# 8. Boundary discipline

The checkpoint deliberately leaves unresolved:

- Nagumo's mature institutional program;
- Sakayanagi's complete genius theory;
- the long-term result of Horikita's Kushida decision;
- whether Kei's negotiated partnership becomes autonomy or deeper dependency;
- whether Ryūen returns as a ruler, subordinate, or something else;
- the future durability of the Ayanokōji Group;
- and how the school will next formalize expulsion and rescue.

No Volume 8 answer is imported.

# 9. Final audit judgment

The `Y1V05–Y1V07.5` tranche is fit for historical reference, cumulative retrieval, and later Year 1 synthesis.
