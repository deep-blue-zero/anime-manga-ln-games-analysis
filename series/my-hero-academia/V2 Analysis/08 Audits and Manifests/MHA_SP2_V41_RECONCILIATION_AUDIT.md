---
series: MHA
corpus: MHA_SP2
artifact_type: reconciliation_audit
scope: V41_PROMOTION
generation: V2
status: canonical
source_boundary: Japanese manga V01-V41; V41 narrative p005-p195; V42 excluded
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# MHA SP2 — V41 reconciliation and promotion audit

## Identity and transport disposition

The maintained-document base is stable-branch merge `c999a3d82b618fa022ec97993211d99116aa28a3`, containing main `da94ba9b5f37e9bddffa98cde9834b394c18b937` without rebasing either published history. The merged tree equals that fetched main tree; ancestry, rather than analytical content, required reconciliation. All MHA V2 paths were inventoried after reconciliation.

The supplied `MHA_V41_V42_ANALYSIS_MATERIALS.zip` has SHA-256 `773ee1a5fe6983c5ce8c7e954d4c44b8fb6456db97f03f3f971024e7a4c73fe5`. All 78 entries in `SHA256SUMS.txt` verified, with all non-manifest bundle files covered. `BUNDLE_README.md` controls transport interpretation only. The V41 canonical-form draft is byte-identical to the existing Git sequential-home draft; that Git object is reused. All seventeen semantic proposal base blobs match the post-reconciliation maintained files. This permits bounded semantic incorporation but does not make the proposals authoritative. The prepared full-ledger candidate and split/rejoined variants are comparison/transport material only; no duplicate analytical object is imported.

## Verified maintained beforeimages

Each file below was read completely before editing. Changes preserve unrelated rows, record IDs, ordering, formatting and historical snapshots. Character/top-state rows, authority markers and operative routing receive targeted edits; V41 ledger sections are appended. The two existing draft artifacts receive bounded source corrections and promotion, not regeneration.

| Maintained path relative to V2 Analysis | Base Git blob | Disposition |
|---|---|---|
| `03 Longitudinal Ledgers/Character Group Ledgers/MHA_SP2_CLASS_1A_CHARACTER_STATE_LEDGER.md` | `a907eee74d1cba56601658f552199c96e9531870` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/Character Group Ledgers/MHA_SP2_UA_STUDENTS_STAFF_CHARACTER_STATE_LEDGER.md` | `82002992262eb20e95234ca691f4e8b61520d732` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/Character Group Ledgers/MHA_SP2_FAMILY_CIVILIAN_SOCIAL_ACTOR_LEDGER.md` | `3f6be034f0875fbdba9febfd3d3615eb81f4f8ef` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/Character Group Ledgers/MHA_SP2_VILLAIN_ANTAGONIST_CHARACTER_STATE_LEDGER.md` | `8d11f5c22848696a0dfa1494f45cc796f449b4fc` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_RELATIONSHIP_STATE_LEDGER.md` | `864014692be0c61801712a87bb795974f7a3ec48` | Bounded V41 cumulative synchronization |
| `04 Character Modeling and Reconstruction/MHA_SP2_CHARACTER_MODEL_READINESS_INDEX.md` | `754e9eb21d2d574ba0ef414d3c6796c4503d0c15` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_POWER_PHILOSOPHY_LEDGER.md` | `7ae7465c34e280f93ee06b533a6c06d0500dba1e` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_HERO_SOCIETY_LEDGER.md` | `90e9055ce1049d29094b05a23d11d041b02e2b6c` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_RECOGNITION_FAILED_RESCUE_LEDGER.md` | `bce7dba2a9099b108f4ba2cc15e4a98e67c8bdeb` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_VILLAIN_FORMATION_LEDGER.md` | `e41b849de23912fe78d717a47a6258df5f3becfc` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_JAPANESE_VOCABULARY_LEDGER.md` | `43df10bd2d4eeba1915cc56a2d62044afe924868` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_VISUAL_MOTIF_LEDGER.md` | `8bb0d810461929a6bdafdefeaa9c00763f621c13` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_CALLBACK_PAYOFF_LEDGER.md` | `d9843d4448b728dca13c9c49bff134232a985196` | Bounded V41 cumulative synchronization |
| `03 Longitudinal Ledgers/MHA_SP2_FIRST_PASS_CORRECTION_LEDGER.md` | `daf91ce8de3b76bed4eefb6954de675e79163bed` | Bounded V41 cumulative synchronization |
| `07 Evidence and Indexes/MHA_SP2_PRIMARY_SOURCE_LOCATOR.md` | `e4aa40bed7f0e97b5438903fdf472d54af7abebb` | Bounded V41 cumulative synchronization |
| `01 Source Lock and Inventory/MHA_SP2_SOURCE_INVENTORY.md` | `735e027e463016bc1a4e3554dd9503a937459201` | Bounded V41 cumulative synchronization |
| `00 Frameworks and Methods/CURRENT_STATE_AND_CORPUS_MAP.md` | `0a5882c322d96e29f7c31c7effaa1ef9bec5e11c` | Bounded V41 cumulative synchronization |
| `02 Sequential Readings/MHA_SP2_V41_DEEP_READING.md` | `21bfecd186801a54a01420162137f0bbd7cb7423` | Reuse Git draft; source corrections; canonical promotion |
| `08 Audits and Manifests/MHA_SP2_V41_UPDATE_MANIFEST.md` | `a089212d99d41ee70bc0af215552925019026704` | Update tranche completion state; canonical promotion |
| `03 Longitudinal Ledgers/Character Group Ledgers/MHA_SP2_PRO_HERO_CHARACTER_STATE_LEDGER.md` | `f4e9b9558ba62ba54706f7c8a9e0d68b6a83f7f1` | Fully screened; no V41 mutation |

The Pro Hero ledger already contains the relevant prior resignation/return framework. V41 Death Arms/unnamed-pro participation adds institutional evidence, routed to Hero Society, without enough distinct individual behavior to justify a new pro model or tier. Its last contribution boundary is therefore retained.

## Direct Japanese-page verification and corrections

The connected Drive source `1q6pj0t6mP59pOsywt8p58H3VWz2l52X_` was fetched read-only and independently hashed: 104,293,245 bytes; SHA-256 `236c8ee8546dcc4c2007a9ffedced6e3489f1d0a2f721cea0d89b5dc75220700`; 209 JPEG pages plus `ComicInfo.xml`. Logical page numbers follow archive order. This audit revisits decisive scenes; it does not claim a new blind reread of the whole volume.

| Probe | Direct pages | Result and downstream consequence |
|---|---|---|
| Personhood, moral anthropology and OFA relinquishment | p019, p033, p035, p049 | Personhood assertion and treasured relinquishment stand. At p033 Kudo interprets Midoriya; the page is not direct first-person testimony by Midoriya. |
| Shimura threshold and protection | p100-p123 | At p110 Nana blocks Kotaro while Midoriya reaches Tenko. Midoriya subsequently holds the child's hands through Decay. The packet assigned Nana's block to Midoriya at the wrong pages; that false action atom and its purported held-out pass are removed. |
| Shigaraki choice and League identity | p116-p123, p127 | The p116 choice sentence concerns destruction of home/family. It does not say he chose to join League hands. The later League montage and villains' hero obligation support a distinct relational claim. Source wording, locator and literal-versus-formal interpretation are corrected. |
| AFO design and possession | p131-p136 | Latent-factor removal, destruction-only copy and covert family manipulation are established. The packet's `自由意思を避けて導く` is unattested: p132 links experienced choice to willpower and describes redirecting free will. Specific acts are distinguished from AFO's total-authorship boast. |
| Kurogiri continuity | p149-p150 | Aizawa's mixed black/white model and current teaching duty are direct. His interpretation is operational evidence, not narrator-certified metaphysical identity. |
| Eri agency and adult disagreement | p157-p159 | Chosen contribution and future song stand; Aizawa warns of Quirk injury and Ectoplasm apologizes. Two-to-three-minute restorative utility does not prove the horn loss harmless or consensually approved by all adults beforehand. |
| Reciprocal need | p173-p175 | OFA factors lost/current embers stand. Aoyama delivers the reciprocal-need appeal and the page recalls the earlier offered hand. Aizawa supplies bandages and a civilian-donated shirt. Attribution is corrected across voice, character, relationship, locator and callback surfaces. |
| Tragedy, affect and plural strength | p166-p168, p187-p188, p195 | Yoichi color-loss, Sero's anti-tragedy answer and relational `弱き強さ` stand. The p195 punch does not establish its V42 outcome. |

Source corrections change the V41 draft section 7.3 and 13.3 headings to identify the correct agents; numbered section identities remain. No previously current V01-V40 deep reading is rewritten. New callback routing also locates the public refuge argument in V33 and explicit Shigaraki autonomy recovery/rejection in V38/V40 rather than the packet's V34/V37 shorthand.

## Cumulative closure and residual boundary

All seventeen required maintained surfaces are synchronized in this tranche. Sero advances to underlying tier `emerging`; qualifiers do not make him strong. No other V41 tier is inflated. The readiness audit carries forward gaps and reserves final snapshot reconciliation for the V42 evidence tranche.

V41 deep reading and manifest become canonical together with the ledgers; the current-state map advances to V01-V41 and points to V42. All final AFO/Tomura life/control outcomes, permanent OFA state, Kurogiri terminal identity, post-horn consequences and postwar settlement remain prospective at p195. The working packet remains noncurrent provenance, including its superseded errors; it must not be mined in preference to corrected canonical evidence.

## Repository verification responsibility

The full nineteen-file maintained diff and this new audit were reviewed, including all appended semantic contributions. Exact-path staging and the index-snapshot stable-branch preflight are the commit gate. No global housekeeping-owned routing output, `characters/registry.jsonl`, or `CHARACTER_ANALYSIS_INDEX.md` is part of this tranche. Remote exact-head CI and protected main integration are later publication obligations and are not asserted as completed here.
