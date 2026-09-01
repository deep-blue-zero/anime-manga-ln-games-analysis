---
series: KONOSUBA
artifact_type: source_lock
scope: FULL_MAIN_SERIES
generation: V1
status: canonical
source_boundary: Japanese main-series light novels V01-V17 complete in the current corpus; V07 acquired and audited 2026-08-27
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA - Source Lock

## 1. Purpose

This document defines which sources may update the canonical sequential analysis and character models during the main-series reading project.

## 2. Primary derivation authority

The canonical derivation corpus is the **Japanese main-series light novels in volume order**.

Current primary-source root:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-0f70fc4c9766e347`

Main-series subfolder:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-2d38c00a5f2fb83a`

The retained EPUBs are governed by the source audits under `Source Audit and Manifests` and the current `audit_manifest.json`.

## 3. Current sequence state

Present:

`V01-V17`

Missing:

`none`

The former V07 continuity gate is **RESOLVED**. V07 was added to the canonical `Main Series` folder, matched the updated manifest SHA-256 exactly, passed ZIP/EPUB integrity checks, and passed a dedicated Japanese-language audit on 2026-08-27.

Canonical sequential analysis may therefore proceed V07 -> V08 -> V09 under the already-frozen Model Generation 0.2 prospective predictions. Later source availability does not license out-of-order analytical updates.

## 4. Withheld sources

The following sources are **not** part of initial model derivation:

- `Yorimichi`;
- `Consulting the Masked Devil`;
- Dust V06;
- Dust V07.

They are reserved for later out-of-sample validation after the main-series models are frozen, subject to chronology/canonicity/viewpoint audit.

This is a methodological holdout, not a judgment that the material is unimportant.

## 5. Non-authoritative external material during sequential reading

The following must not silently update canonical model state:

- anime adaptation scenes;
- manga adaptation material;
- fan wiki summaries;
- fandom reputation/memes;
- unofficial character descriptions;
- later-volume information read out of sequence;
- model memory of plot events not re-grounded in the current primary source.

Such material may be discussed separately, but source provenance must be explicit and it cannot override Japanese-primary findings without a documented methodological decision.

## 6. Translation policy

If an official or unofficial translation is later added, it may support navigation or comparative translation analysis. Claims about Japanese wording, register, pronouns, honorifics, sentence-final stance, wordplay, or pragmatic effect must return to the Japanese source.

## 7. Source update procedure

For any later replacement/addition:

1. verify file integrity;
2. verify language;
3. record hash and filename;
4. update the primary-source manifest;
5. update `KONOSUBA_SOURCE_INVENTORY.md`;
6. update this source lock if authority/boundary changes;
7. update `CURRENT_STATE_AND_CORPUS_MAP.md`;
8. update the master `MANGA_ANIME_DRIVE_INDEX.md` if routing materially changes.

## 8. Governing rule

No adaptation, summary, memory, or later source is allowed to erase the distinction between **what the Japanese main novel actually establishes at this point in sequence** and what is known elsewhere.
