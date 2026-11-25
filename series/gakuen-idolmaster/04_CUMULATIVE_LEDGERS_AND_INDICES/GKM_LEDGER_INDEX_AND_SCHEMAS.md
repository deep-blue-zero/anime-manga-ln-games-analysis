---
title: "Gakuen Idolmaster V2 Ledger Index and Schemas"
project: "Gakuen Idolmaster"
document_type: "ledger index"
version: "2.1"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
last_updated: "2026-11-25 — Carbon residual evidence register; 2026-11-15 — source-to-analysis audit conventions and pronoun style note"
---

# GKM LEDGER INDEX AND SCHEMAS

Phase 0 initializes the following cumulative ledgers. Each is a living analytical apparatus file; final reader-facing synthesis should cite through them when practical rather than treating them as prose chapters.

| file | purpose |
| --- | --- |
| GKM_SOURCE_IDENTITY_AND_DEDUP_LEDGER.md | Source Identity and Dedup Ledger |
| GKM_CONTINUITY_AND_STORY_STATE_LEDGER.md | Continuity and Story-State Ledger |
| GKM_BRANCH_DIVERGENCE_LEDGER.md | Branch Divergence Ledger |
| GKM_CHARACTER_STATE_LEDGER.md | Character State Ledger |
| GKM_RELATIONSHIP_STATE_LEDGER.md | Relationship State Ledger |
| GKM_INSTITUTION_AND_IDOL_SYSTEM_LEDGER.md | Institution and Idol-System Ledger |
| GKM_THEME_AND_MOTIF_LEDGER.md | Theme and Motif Ledger |
| GKM_JAPANESE_VOICE_AND_REGISTER_LEDGER.md | Japanese Voice and Register Ledger |
| GKM_NPC_AND_SIDE_CHARACTER_LEDGER.md | NPC and Side-Character Ledger |
| GKM_SUPPORT_AND_EVENT_PARTICIPANT_INDEX.md | Support and Event Participant Index |
| GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md | Primary Source Locator Ledger |
| GKM_LEGACY_CLAIM_REVISION_LEDGER.md | Legacy Claim Revision Ledger |
| GKM_VOICE_PERFORMANCE_STATE_LEDGER.md | Voice Performance State Ledger |
| GKM_SONG_AND_MUSICAL_IDENTITY_LEDGER.md | Song and Musical Identity Ledger |
| GKM_AUDIOVISUAL_VERIFICATION_QUEUE.md | Audiovisual Verification Queue |
| GKM_AUDIOVISUAL_SOURCE_CROSSWALK.md | Audiovisual Source Crosswalk |
| [GKM_CARBON_RESIDUAL_EVIDENCE_REGISTER.md](GKM_CARBON_RESIDUAL_EVIDENCE_REGISTER.md) | Unavailable recording editions and claim-level limitations after the local playback assignment |

All ledgers begin under Source Lock 1.0. A later source-lock upgrade must record which entries were derived from which source version.


## Source Lock 1.1 — transcript refresh, 2026-11-12

The dated 1.1 rows keep the original ledger schemas and source identities. Resolve each GKM-R86 group to a reading and exact A1 source in the [locator ledger](GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-lock-11--transcript-refresh-2026-11-12).

## Source Lock 1.2 — transcript refresh, 2026-11-15

[Source Lock 1.2](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_REFRESH_20261115.md) adds six retrieval groups, GKM-R88-01 to GKM-R88-06. Start with their [A1 locator table](GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-lock-12--transcript-refresh-2026-11-15) and [Kanae’s reading](../03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/14_HIWATARI_KANAE/GKM_HIWATARI_KANAE_SOURCE_LOCK_12_READING.md). The dated 1.2 entries retain the existing schemas.

## Source-to-analysis audit corrections — 2026-11-15

The [dispositions crosswalk](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_SOURCE_TO_ANALYSIS_AUDIT_DISPOSITIONS_20261115.md) maps every `GKM-SAA-nnn` finding to its homes. Each cumulative ledger records the corrections in a dated section named "Source-to-analysis audit corrections — 2026-11-15" (the claim-revision ledger: "[Source-to-analysis audit claim revisions — 2026-11-15](GKM_LEGACY_CLAIM_REVISION_LEDGER.md#source-to-analysis-audit-claim-revisions--2026-11-15)"). Those sections keep each ledger's existing schema. New locators use `LOC-SAA-nnnX`, where `nnn` is the audit number, and are listed in the [locator ledger](GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-to-analysis-audit-corrections--2026-11-15). The participant index now fills its `mentioned_characters` field for support rows where an absent figure carries the scene, marking each figure named or unnamed. The source-identity ledger holds a source-anomaly table.

**Style note — pronouns follow the character, not the persona (GKM-SAA-031, with GKM-SAA-013).** Mao's `ボク` and prince register are not grounds for masculine English pronouns. Every ledger and reading refers to Mao as she/her (see MAO-C14; `adv_dear_amao_003.txt` L81; `adv_cidol-amao-3-015_02.txt` L147). The same rule applies to any persona, role or first-person form: describe the persona as a persona and keep the character's own pronouns.
