---
series: AZUR_LANE
artifact_type: source_audit
scope: PRINZ_EUGEN_40303_DERIVED_EVIDENCE_PUBLICATION
generation: V1
status: canonical
scope_character: PRINZ_EUGEN_40303
semantic_authority: CN
source_boundary: "Comparison of canonical CHARACTER_MANIFEST.json declarations/hashes against the currently retrievable Google Drive Analysis and Primary Sources publication surfaces"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Azur Lane — Prinz Eugen Derived Evidence Publication Audit

## Verdict

**`PRINZ_EUGEN_DERIVED_PUBLICATION_PARTIAL`**

The pinned character build is structurally complete enough to declare the intended Prinz Eugen evidence package, but the current Drive publication is asymmetric.

### Published and directly retrievable now

Analysis root `02 Extracted Character Corpora/PRINZ_EUGEN_40303/` currently exposes:

- `CHARACTER_MANIFEST.json`
- `CHARACTER_SOURCE_MAP.md`
- `SOURCE_COVERAGE.json`
- `SOURCE_COVERAGE.md`
- `audio/` alignment/coverage infrastructure

Primary Sources `02 Japanese Voice Audio/Characters/PRINZ_EUGEN_40303/Listening Derivatives/` exposes:

- `PRINZ_EUGEN_JP_WAV_MANIFEST.jsonl`
- `PRINZ_EUGEN_JP_WAV_INDEX.md`
- `PRINZ_EUGEN_JP_AUDIO_ANALYSIS_PACK.md`
- literal `audio/wav` derivatives under `WAV/`
- an explicit `UNRESOLVED/` branch.

### Declared by the canonical manifest but not directly retrievable from Drive

The manifest hashes these outputs, proving they were generated in the pinned build:

| Declared artifact | SHA-256 |
|---|---|
| `human_readable/PRINZ_EUGEN_CN_CHARACTER_DIALOGUE_LEDGER.md` | `295f95690b91094c0c8075098b0700731820c47aa9c882f6677ab41c4bef669e` |
| `human_readable/PRINZ_EUGEN_CN_NARRATIVE_SCENE_CORPUS.md` | `2295376d044b301e64f62452f33596e9dd57b64d80a2641999ad750bdc93a928` |
| `human_readable/PRINZ_EUGEN_CN_NARRATIVE_SCENE_CORPUS_RAW.md` | `429dc2a618a3e385798efe82bc68e100bbb18ff5a0442d3eed5545dc3cdf5110` |
| `human_readable/PRINZ_EUGEN_CN_SCENE_INDEX.md` | `428ff37502af9926e92eaecb558f3850e2566887a0b44d735009b2738ad7c9c5` |
| `human_readable/PRINZ_EUGEN_CN_SOCIAL_RECONSTRUCTION.md` | `ad702e09b41b50485c19ee87aa571e9b9a8cbc51f12b0d91e531bbd09cb961fd` |
| `human_readable/PRINZ_EUGEN_RELATIONSHIP_EVIDENCE_INDEX.md` | `9b16b0a98707bf78f7d3a3b974c7a97eeee2671eb6283c237d9c01332de05c8d` |
| `human_readable/PRINZ_EUGEN_REGIONAL_CROSSWALK.md` | `3f0e8c5de9b1c06f446a83608a1468d0e0e4df83251267f7ba4a4e31c06fac7f` |
| `human_readable/PRINZ_EUGEN_ISLAND_EVIDENCE_CN.md` | `8d99ff3dcea7ca4f664a2ed38dd04757e2e6117d8df984ad91848f61b7d33b20` |
| `human_readable/PRINZ_EUGEN_ISLAND_EVIDENCE_JP.md` | `24e471503abd3dc74c8ada1bbcdce2b50edd0897d68a6e8ae3b34b92aa6e1194` |
| `human_readable/PRINZ_EUGEN_ISLAND_EVIDENCE_EN.md` | `3a76ef611098d4f60c4c022e028608937609d84cbb6edf5594e731e6a3af2100` |
| `human_readable/PRINZ_EUGEN_ISLAND_EVIDENCE_TW.md` | `7cd69ac907cbcb6122a144f46c21d8fdd816d9ef649e8b21f551adb7eb6c1eb4` |
| `human_readable/PRINZ_EUGEN_ISLAND_EVIDENCE_KR.md` | `6302535251dbf08074b0a2d736306b4a0177ccb713c02294be19ea65a4cb67ed` |

`PRINZ_EUGEN_JP_AUDIO_INDEX.md` is also declared in the build manifest and has a separately published Primary Sources equivalent, so the audio side is not part of this textual publication gap.

## Analytical consequence

The source summaries are sufficient to establish **readiness and routing**, but not sufficient to establish:

- personality architecture;
- stable motives;
- decision rules;
- defensive strategies;
- interpretation of teasing/provocation;
- emotional regulation;
- peer-specific relationship models;
- whether public affect differs from private affect;
- whether apparent detachment is sincere, defensive, strategic, playful, or context-dependent;
- any named-event developmental thesis.

Those are interpretive claims and require the actual source text in context.

## Prohibited workaround

Until the manifest-declared evidence is directly readable, do **not** fill the gap using:

- wiki summaries;
- fandom archetypes;
- remembered event plots;
- general knowledge of Prinz Eugen;
- translated quote collections;
- audio filenames alone;
- character-design inference.

The canonical corpus already defines the intended evidence. The correct action is to restore that evidence surface, not replace it.

## Closure condition

This audit closes when the manifest-declared human-readable files are restored to the canonical Analysis character folder (or another canonical Drive home explicitly registered by the corpus map), and readback verifies their names/content against the pinned manifest hashes where byte identity is expected.

Once closed, R2 can begin immediately. No new source crawl is required unless the governing source lock itself changes.
