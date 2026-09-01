---
series: AZUR_LANE
artifact_type: audit
scope: ST_LOUIS_10213_JP_AUDIO_RECONCILIATION
generation: V1
status: canonical
source_boundary: JP client AZL 9.3.386 / CV 1243; St. Louis group 10213; source bundles and extracted ship_skin_words voice records
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
semantic_authority: CN
performed_locale: JP
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — St. Louis JP Audio Reconciliation Audit

## 1. Verdict

**`ST_LOUIS_JP_AUDIO_SPOKEN_CORPUS_READY`**

The previous per-character coverage surface reported 69 mapped slots and three unresolved text records. The newer pipeline state correctly raised this to 71 mapped / 1 unresolved. Manual source adjudication closes the remaining ambiguity without inventing a missing spoken line:

- `102130:couple_encourage:0` → exact JP client resource `link1`;
- `102130:couple_encourage:1` → exact JP client resource `link2`;
- `102134:vote:0` contains the generic source placeholder `拉票描述`, has no character-voice resource, and is classified **NON_DIALOGUE_PLACEHOLDER**, not missing St. Louis dialogue.

Therefore the spoken candidate corpus contains **zero unresolved spoken text records**.

## 2. Final coverage

- textual/audio-reference candidate records: 77;
- mapped voiced dialogue: **71**;
- known unvoiced `drop_descrip` text: **5**;
- non-dialogue campaign placeholder: **1**;
- unresolved spoken records: **0**;
- archived unmatched auxiliary client assets after `link1/link2` repair: **5**;
- affinity: 8 / 8 voiced mappings;
- oath: 1 / 1;
- combat: 7 / 7;
- relationship-specific: 2 / 2.

`AUDIO_READY` in this audit means the **spoken St. Louis character-text corpus is source-complete for performed-voice analysis**. It does not assert that every auxiliary UI/gift client sound is semantically character dialogue.

## 3. Corrected mapping logic

The two relationship records previously used generated expected keys `couple_encourage1/2`, but the JP client uses `link1/link2`. The repaired aliases are deterministic because source order, battle-bundle location, record order, and client resource names agree.

The campaign record differs categorically. Its published source text is a generic description placeholder rather than St. Louis dialogue. Keeping it in an `AUDIO_NOT_FOUND` bucket would incorrectly imply a missing performance. It is preserved, not deleted, under `NON_DIALOGUE_PLACEHOLDER`.

## 4. Source decode and derivative QA

Original source bundles remain archival authority. For analysis, the mapped HCA streams were extracted from their embedded AFS2 banks and decrypted with the pinned Azur Lane HCA key already identified by the source-acquisition pipeline. The HCA cipher is type 56; decrypted audio was decoded to one PCM WAV per mapped utterance.

Derivative rules:

- PCM signed 16-bit little-endian WAV;
- 44.1 kHz;
- mono;
- whole mapped stream;
- no trimming;
- no normalization;
- no resampling;
- no denoising;
- no concatenation.

QA result:

- mapped derivatives: **71 / 71 PASS**;
- total duration: **13.07 minutes**;
- median utterance duration: **10.31 s**;
- source manifest SHA-256: `223e30d4adae316704469309bf4a89cb9e0cf332f6392ffb4b7a9df075501b21`;
- reconciled alignment SHA-256: `fe9691695e11bc583790fd11e5c9e266eb7412b34bd7e4d817a6b102ff6fff11`.

The first attempted decode without effective HCA decryption was rejected before interpretation and is not evidentiary. The canonical derivatives and measurement matrix were regenerated after successful frame-level decryption.

## 5. Final routing

```text
JP text record
→ reconciled client resource
→ original .b / ACB source bundle
→ embedded AFS2 stream / HCA
→ source-preserving PCM WAV derivative
→ fixed acoustic measurement matrix
→ three-pass performance interpretation
```

No semantic claim is inferred from a source gap that has not been explicitly dispositioned.
