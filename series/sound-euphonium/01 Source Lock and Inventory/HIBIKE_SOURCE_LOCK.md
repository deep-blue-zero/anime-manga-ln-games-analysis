---
series: HIBIKE
artifact_type: source_lock
scope: V2_PHASE1_INITIAL_LOCK
generation: V2
status: canonical
source_boundary: 'Immutable initial Phase-1 lock: Japanese EPUB sources HIBIKE-V01 through HIBIKE-V14 by filename and SHA-256; supplemental/adaptation evidence governed by explicit classifications below'
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Sound! Euphonium V2 — Source Lock

## 1. Lock declaration

**Phase 0 is complete.**

Effective 2026-08-19, the V2 project locks the fourteen verified Japanese EPUB sources identified below as the governing primary-text corpus for Phase 1 sequential reading.

This lock is **immutable as a historical source boundary**. New supplemental material, corrected editions, or future publications must not be silently inserted. They require a new superseding source-lock artifact and a corresponding update to `CURRENT_STATE_AND_CORPUS_MAP.md`.

The lock is based on:

- publisher-verified bibliography;
- complete acquisition of the current fourteen-book prose set;
- structural/readability audit of all fourteen EPUBs;
- SHA-256 identity;
- explicit separation of OCR legacy, prose supplements, and adaptation paratext.

---

## 2. Locked governing core

| Source ID | Locked filename | SHA-256 |
|---|---|---|
| HIBIKE-V01 | `Sound! Euphonium - Novel 01 - Kitauji High School Concert Band Welcome [Japanese].epub` | `8b03b3aad0555b22cbb0ebe2f19b1adf9f3919b60487395dae0ab7958488e288` |
| HIBIKE-V02 | `Sound! Euphonium - Novel 02 - Kitauji High School Concert Band The Hottest Summer [Japanese].epub` | `fda7b77e5028f8e50d55cbffe883b3b63b57cf35d0abc1618e620b40c504cf12` |
| HIBIKE-V03 | `Sound! Euphonium - Novel 03 - Kitauji High School Concert Band The Greatest Crisis [Japanese].epub` | `81a7ebcb03bda07cdb6b43efd1e1c50301d866cb883cee421a65086cea95b013` |
| HIBIKE-V04 | `Sound! Euphonium - Novel 04 - Kitauji High School Concert Band Secret Story [Japanese].epub` | `999645e5f9f4405dc9d2e1d5a2938c9ffcb8f377f42e6c2a4a8265e302fa25b5` |
| HIBIKE-V05 | `Sound! Euphonium - Novel 05 - Rikka High School Marching Band Welcome Part 1 [Japanese].epub` | `99623910c375268a3443920ca464c51cbf2fb3f86094948cc22d4f607bf6a780` |
| HIBIKE-V06 | `Sound! Euphonium - Novel 06 - Rikka High School Marching Band Welcome Part 2 [Japanese].epub` | `e14b74c7829ed30ae2447587b5a1bbded5621d1faf571f3201fb639d673e16b2` |
| HIBIKE-V07 | `Sound! Euphonium - Novel 07 - Kitauji High School Concert Band Diary [Japanese].epub` | `18e15066adabd7875d85509a570ef70790862da2a4313c88861310dea749f077` |
| HIBIKE-V08 | `Sound! Euphonium - Novel 08 - Kitauji High School Concert Band Turbulent Second Movement Part 1 [Japanese].epub` | `478652db40270358fa36bede8a835076abe22a86177c251851623850dfc4b8cb` |
| HIBIKE-V09 | `Sound! Euphonium - Novel 09 - Kitauji High School Concert Band Turbulent Second Movement Part 2 [Japanese].epub` | `3a5249c76be8618cf386fab5a9b3ab307ab424be09d7517665c77305fdbd1fb2` |
| HIBIKE-V10 | `Sound! Euphonium - Novel 10 - Kitauji High School Concert Band True Story [Japanese].epub` | `04ae787ac0b852b5b83cf2077d602a242b31dd9c39b4e0fc71fb5467e3c477c1` |
| HIBIKE-V11 | `Sound! Euphonium - Novel 11 - Kitauji High School Concert Band Decisive Final Movement Part 1 [Japanese].epub` | `56cc0592af7aff896dbffbb4f23444ee4e497e783a94f1338630bf6c82c0da45` |
| HIBIKE-V12 | `Sound! Euphonium - Novel 12 - Kitauji High School Concert Band Decisive Final Movement Part 2 [Japanese].epub` | `5e98951d0a5e7829d6cc99f37acedb3926a04664d032a17b231dee8242bbf46b` |
| HIBIKE-V13 | `Sound! Euphonium - Novel 13 - Watching You Take Flight [Japanese].epub` | `0728962b4793b2b59911cb332a0db174d47237a6e95011ffa408e2a91a1b733e` |
| HIBIKE-V14 | `Sound! Euphonium - Novel 14 - Kitauji High School Concert Band Everyone's Story [Japanese].epub` | `b80455a6106a0a3fd54ff59826363d6a7f698efc710c1521e838501dbdfe24e9` |

Canonical file route:
`Primary Sources/Sound Euphonium/Epub + PDF/`

`rename_manifest.json` is provenance/inventory support. Where its inherited filename metadata conflicts with publisher-verified bibliographic data, `HIBIKE_SOURCE_INVENTORY.md` governs the bibliographic correction while the original filename remains preserved as provenance.

---

## 3. Governing-evidence rules

### 3.1 Narrative and linguistic authority

For exact claims about Takeda's prose, the locked Japanese text governs:

- dialogue wording;
- narration;
- particles and sentence endings;
- forms of address;
- honorifics/register;
- Kansai/regional features;
- punctuation and ellipsis;
- ruby/readings;
- speaker attribution;
- chronology and scene content;
- prose focalization.

### 3.2 EPUB package provenance

Some locked files are retail-ebook-derived or converted packages rather than provably untouched publisher-native EPUB archives. This does not invalidate their text for the present analytical purpose, because they have passed structural/readability audit and are matched to publisher-verified editions.

However:

- package-generated romanizations are non-authoritative;
- incidental OPF metadata is subordinate to Japanese title text and publisher bibliography;
- layout/CSS conversion artifacts should not be interpreted as literary form;
- if an exact edition discrepancy is later demonstrated, a versioned source-lock revision is required.

### 3.3 Hybrid/paratext sections

Where a locked book contains guide, interview, commentary, or editorial matter, those sections retain their own evidence class. Locking the whole EPUB does **not** promote every paratextual statement to narrative fact.

---

## 4. OCR legacy lock

The ten V1 OCR analysis packs are retained under:
`Primary Sources/Sound Euphonium/OCR/`

Status: **historical_legacy**.

They are permitted for:

- provenance;
- V1 reconstruction;
- comparison against OCR errors;
- visual-page recovery when useful.

They are **not current authority for exact wording** where a locked EPUB exists.

V1↔V2 mapping is governed by:
`HIBIKE_V1_OCR_TO_V2_TEXT_CROSSWALK.md`.

---

## 5. Supplemental prose status at initial lock

### Deferred, not admitted to the initial governing core

**2023 Ensemble Contest theatrical Takeda short stories**

- `休日、愛らしい友人と`
- `贈り物に愛を込めて`
- `偶発的再会と他愛ない会話について`

Status: `official_author_written_adaptation_adjacent_supplemental_prose / deferred`.

**2026 Final Chapter Part I theatrical Takeda short stories**

- `君は可愛い、君が可愛い`
- `予算は五千円までです。`
- `シャボン玉の行方は知らない。`

Status: `official_author_written_adaptation_adjacent_supplemental_prose / deferred`.

**2021 5th Anniversary Disc booklet Takeda story**

Status: `official_author_written_adaptation_paratext_supplement_candidate / open` pending title/text acquisition and duplication audit.

**Future 『北宇治高校の吹奏楽部日誌2』**

Status on lock date: `future_canonical_prose_supplement_candidate / unreleased`, scheduled 2026-09-10.

None of these absences blocks HIBIKE-V01.

### Already satisfied

`記憶のイルミネーション` is contained in the locked HIBIKE-V13 paperback-edition EPUB and therefore requires no separate prose acquisition.

See `HIBIKE_SUPPLEMENTAL_SOURCE_AUDIT.md` for details.

---

## 6. Adaptation/paratext admission

### Acquired KyoAni Official Illustration Works

File:
`Sound! Euphonium - Reference - Official Illustration Works [Japanese].pdf`

SHA-256:
`5ab8c96ff4508031dca507a744bf4f6a9b1b4ba4add0508ae3cf8ade82e4616b`

Status: **admitted adaptation/visual paratext, excluded from governing novel-text authority**.

It may support a separately labeled adaptation/design inference. It may not override or silently supplement novel-canonical speech, thought, or continuity.

### Not admitted by default

- manga adaptations;
- anime scripts/scenario books;
- audio dramas;
- animation setting/design books;
- promotional art and merchandise imagery.

These require explicit later admission to an adaptation-comparison layer if used.

---

## 7. Stable locator lock

Phase-1 primary evidence uses:

`HIBIKE-VXX / SNN / P#### / <short exact Japanese cue>`

The generated locator map for each volume must preserve the original OPF spine ordinal and XHTML path. Paragraph numbering is deterministic within the locked file hash. If a source file changes, its locators are no longer assumed stable and the source lock must be revised.

---

## 8. Revision policy

This document freezes the **initial Phase-1 source boundary**.

Future changes require a new source-lock artifact rather than silent mutation, for example:

`HIBIKE_SOURCE_LOCK_V2_1.md`

A superseding lock must specify:

- newly admitted/replaced source;
- reason for transition;
- old/new hashes where relevant;
- locator consequences;
- evidence-class consequences;
- whether prior analytical claims require audit.

The current lock then becomes historical authority for the work produced under it.

---

## 9. Phase-1 authorization

The following Phase-0 gates are satisfied:

- [x] current fourteen-book bibliography established;
- [x] HIBIKE-V01–V14 acquired;
- [x] EPUB integrity/readability audit passed;
- [x] source hashes recorded;
- [x] V1 OCR provenance preserved;
- [x] V1↔V2 structural crosswalk established;
- [x] supplemental-source boundary audited;
- [x] adaptation/paratext boundary established;
- [x] stable locator grammar established;
- [x] source lock issued.

**AUTHORIZED NEXT STEP:** `HIBIKE_V01_DEEP_READING.md` under `02 Sequential Readings/`, using the V2 analytical and character-modeling methods. Recommended reasoning effort: **Extra High**.
