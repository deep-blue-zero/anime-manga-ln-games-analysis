---
series: AZUR_LANE
scope_character: BREMERTON_10324
generation: V1
semantic_authority: CN
azurlane_data_commit: 4cca5c2437007b62d30a6235fcfc0c0203231378
story_lua_witness_commit: d93f83db24195981c5f5ca90ac5e29ce0580b12c
source_package_generated_at: "2026-08-23T18:55:47.426186Z"
supersedes: null
superseded_by: AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md
do_not_use_as_current_authority: true
artifact_type: audit
scope: BREMERTON_10324_JP_AUDIO_PUBLICATION_GATE
status: historical_legacy
source_boundary: "Bremerton JP audio manifests/alignment, Primary Sources publication manifest, acquisition lock, and Drive source-bundle readback on 2026-08-23"
---

# Azur Lane — Bremerton JP Audio Publication Gap Audit

## Verdict

**`BREMERTON_101_WAV_ACOUSTIC_PASS_BLOCKED_BY_PUBLICATION_GAP`**

This is a hard evidence-availability gate, not a mapping-quality failure.

## 1. Mapping state

The current Bremerton JP alignment contains:

- **101 `MAPPED` spoken utterances**;
- **7 `TEXT_UNVOICED`** profile/drop-description text fields;
- **5 `ASSET_PRESENT_UNMAPPED`** auxiliary assets;
- **1 `ASSET_PRESENT_CLASSIFIED`** auxiliary review asset.

The 101 mapped spoken utterances reduce to only two original client bundles:

| Source bundle | Mapped utterances | SHA-256 |
|---|---:|---|
| `AssetBundles/cue/cv-10324.b` | **92** | `cc507128546ac676c142b171b8919104d3672f62910f9e3e4218cd39d4b3e75e` |
| `AssetBundles/cue/cv-10324-battle.b` | **9** | `7cb946f5962bfe920b0111e093a70a04391309fad0110aeacd287fbe50c99161` |

The mapping metadata reports CRI HCA, 44.1 kHz mono, AssetDownloader 4.7.1, JP client CV 1243 / AZL 9.3.386, and `acquisition_method = azlassets_direct_jp_cdn`.

## 2. Why the waveform pass cannot be reproduced now

The mapped records point to intended archival paths:

```text
Source Bundles/JP/cc/cc507128...b
Source Bundles/JP/7c/7cb946f5...b
```

But the current Drive source publication does not contain those exact files.

Direct inspection of the existing `cc/` prefix folder found only an unrelated `cc6dc...b`, not `cc507...b`. The mapped WAV manifest also has no Drive file IDs/readback verification for the 101 derivatives, and the Bremerton `WAV/` publication surface does not expose the mapped derivatives through the current connector.

## 3. Temporal reconciliation

The older global acquisition lock/audit was generated around `04:36 UTC` and states that 311 target-relevant source bundles had been archived and verified.

Bremerton's alignment records show the two required bundles were acquired at approximately **`2026-08-23T18:58:22Z`**—more than fourteen hours later.

Therefore the apparent contradiction is explained by chronology:

> **the 311-bundle publication was complete for its earlier target set, then Bremerton was acquired later and its new source bundles were never added to that frozen/publication manifest surface.**

The older audit is not false for its own run; it is stale as a statement about the later Bremerton package.

## 4. Why metadata is insufficient for the promised three-pass analysis

The planned combined pass requires waveform-derived evidence such as:

- F0 placement/range;
- temporal continuity/fragmentation;
- activity/pause structure;
- active level;
- text-normalized active speaking-rate proxy;
- matched state/skin comparisons.

Duration, stream name, codec, and mapping confidence cannot substitute for those measurements.

Accordingly this audit explicitly forbids generating claims such as:

- “Bremerton's pitch rises in intimacy”;
- “combat is more projected”;
- “she becomes breathier/warmer”; or
- “her bridal register is acoustically calmer”

without the actual decoded waveform evidence.

## 5. Exact remediation condition for a future run

The acoustic gate becomes runnable when either:

1. the two exact source bundles above are published/readable under Primary Sources; **or**
2. all 101 mapped lossless WAV derivatives are published with source-hash/stream-index provenance and verified Drive readback.

Then the already-frozen Takao-style method can run in one measurement job followed by:

- Pass 1 anchor contrasts;
- Pass 2 breadth challenge;
- Pass 3 exhaustive adversarial audit.

No new psychological model is needed before that repair.

## 6. Current authority consequence

- JP **text** speech model: usable.
- text ↔ audio **mapping**: complete for 101 spoken slots.
- JP **performed acoustic** model: **OPEN / blocked**.
- ear-dependent timbre: **OPEN**.
- semantic monograph: valid but held `active_provisional` because the user-selected production architecture made performed voice a formal V1 promotion gate.


## 7. Supersession note — 2026-08-25

This audit is retained as provenance for the original all-waveform publication block, but it is **no longer current authority**. Subsequent Drive publication exposed the Bremerton listening derivatives. A direct quantitative pass retrieved, SHA-256 verified, and measured **100/101** mapped WAVs.

Current authority for performed voice is `AZUR_LANE_BREMERTON_JP_VOICE_PERFORMANCE_PROFILE.md`. The remaining publication/readback exception is narrowed to one mapped file: `BREMERTON_103245_LOGIN_LOGIN_S042_cc507128.wav`.
