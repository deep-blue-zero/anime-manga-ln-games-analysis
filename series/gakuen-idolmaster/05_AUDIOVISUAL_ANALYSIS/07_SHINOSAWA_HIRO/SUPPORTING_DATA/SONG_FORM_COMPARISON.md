---
series: GKM
generation: V2
artifact_type: historical_supporting_record
status: historical_legacy
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
source_boundary: "Preserved earlier-generation supporting record; not fresh AVE-FULL evidence."
last_updated: '2026-09-10'
---
> Historical record retained from the previous packet. “New/current” in this document refers to that earlier execution, not AVE-FULL-20260910. Fresh results are in [the current measurements](FULL_REBUILD_MEASUREMENTS.md) and [current claim review](FULL_REBUILD_CLAIM_REVIEW.md).

# Hiro song-form comparison — new standalone measurements

> **Authorized execution revision — 2026-09-10.** This complete document preserves the supplied rebuild and earlier canonical analysis as inherited work. Statements about “new,” “current,” or “session” processing in preserved historical sections refer to that supplied run, unless explicitly labeled **authorized execution**. They are not evidence that this reviewer performed those inspections. Current findings and source-clock controls are recorded in [the execution review](EXECUTION_20260910_REVIEW.md); source acquisition, numerical processing, direct visual inspection, and automated audio work have separate coverage. This remains an integration candidate; no canonical repository document was replaced.


The original experimental-proxy formula was not recovered. Composite, rank, and its two n=0 means are retired. This table does not reconstruct or validate the old composite. Structural novelty is also retired; no formula has been invented for it.

**Authorized execution numerical qualification:** H23 `rms_p90_p10_db = 211.058496695` is dominated by a near-zero P10 (`7.37756150279e-12`); H31 `230.283647623` uses P10 = 0 with the declared `1e-12` floor. These are silence/floor-sensitive source-span ratios, not expressive dynamic range. H23 is in the common group and strongly inflates its mean `60.5825248389 dB`; H31 is individual-only. Preserve the recorded values and memberships for reproducibility, but do not interpret the common-versus-principal difference as a musical result. No replacement mean or silent threshold change is introduced.

## Inputs and comparison design

Primary comparison: three Hiro-specific 3DMVs (光景, コントラスト, サンフェーデッド) against six common-repertoire Hiro 3DMVs (Campus mode!!, 初, Howling over the World, がむしゃらに行こう！, ミラクルナナウ, ENDLESS DANCE). These are newly declared groups, chosen to limit source-form confounding; they are not claimed to be the historical groups. Whole source duration remains unmatched and includes intros/endings. n=3 and n=6 are source counts, not independent songs sampled randomly from a population. No significance test, genre verdict or superiority claim follows. Other authored MVs, full mixes, duets, seasonal sources and the fan derivative are reported individually but excluded from these means. メクルメ and コンテンポラリ are secondary individual controls and do not silently enlarge either primary group.

| Row | Drive ID | Source | Group | Audio s | Beats n | Intervals n | Local-tempo n | Chroma n | Tonnetz transitions n | Flux transitions n | beat_interval_cv | local_tempo_cv | chroma_entropy_bits_mean | tonnetz_motion_mean | flux_cv | flatness_mean | rms_p90_p10_db |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H12 | 1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk | 光景 Hiro rendered performance | principal_3dmv | 175.264217687 | 338 | 337 | 7549 | 7549 | 7548 | 7544 | 0.0412258416348 | 0.218777184039 | 2.68107795715 | 0.121605089999 | 0.478275543145 | 0.104590364406 | 33.6979113977 |
| H13 | 1BJxsuu7p4m4eUFOgXlstQI9AgWGnyWbC | Fan comparative montage: progressively improving 光景 | individual_only | 153.925079365 | 306 | 305 | 6630 | 6630 | 6629 | 6625 | 0.0490898136225 | 0.103643190751 | 2.96762561798 | 0.136749084086 | 0.433953578629 | 0.0268559131017 | 11.5194255614 |
| H14 | 14mm43MjBvXxqXvEfgpxdgpzO_hYSyvLn | 光景 authored official MV | individual_only | 271.928888889 | 557 | 556 | 11712 | 11712 | 11711 | 11707 | 0.0290200982217 | 0.132263856747 | 3.10076713562 | 0.109429461527 | 0.403203706495 | 0.0312703577975 | 12.1305962388 |
| H15 | 1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR | コントラスト Hiro rendered performance | principal_3dmv | 200.782947846 | 344 | 343 | 8648 | 8648 | 8647 | 8643 | 0.0420315967417 | 0.147949412601 | 3.02042245865 | 0.126025856049 | 0.492392700639 | 0.0596543685452 | 30.1249180925 |
| H16 | 11LEGW6hntUwu7GhljqYbqWzcO2lZFwDz | コントラスト full/static presentation | individual_only | 217.511473923 | 538 | 537 | 9368 | 9368 | 9367 | 9363 | 0.0481390847305 | 0.149956717157 | 3.19150185585 | 0.115192160228 | 0.542975330409 | 0.0242325471298 | 10.7704101969 |
| H17 | 11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E | サンフェーデッド Hiro rendered performance | principal_3dmv | 183.275102041 | 369 | 368 | 7894 | 7894 | 7893 | 7889 | 0.049152636876 | 0.135883136043 | 3.10597395897 | 0.112915828541 | 0.352550955518 | 0.080251401523 | 7.51134694897 |
| H18 | 14gD5uR2AdNK274Z8Juh6u5pY3pWYpMfF | サンフェーデッド authored official MV | individual_only | 209.304671202 | 475 | 474 | 9015 | 9015 | 9014 | 9010 | 0.050923647479 | 0.130340085066 | 3.28962206841 | 0.104037019544 | 0.321705743784 | 0.0401880502569 | 2.70631533442 |
| H19 | 1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd | Campus mode!! Hiro rendered performance | common_3dmv | 160.728526077 | 304 | 303 | 6923 | 6923 | 6922 | 6918 | 0.051612062919 | 0.164607768208 | 2.89765429497 | 0.165536706464 | 0.375024324504 | 0.11238432908 | 10.9453120906 |
| H20 | 1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj | 初 Hiro rendered performance | common_3dmv | 155.178956916 | 282 | 281 | 6684 | 6684 | 6683 | 6679 | 0.0480737348702 | 0.202736073314 | 3.00636959076 | 0.151006129917 | 0.292487753673 | 0.0285001797725 | 8.64234414959 |
| H21 | 1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp | Howling over the World Hiro rendered performance | common_3dmv | 110.225124717 | 230 | 229 | 4748 | 4748 | 4747 | 4743 | 0.0392858787075 | 0.214716691445 | 3.0457918644 | 0.110332674652 | 0.478744188121 | 0.107394990016 | 35.2961981619 |
| H22 | 1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy | がむしゃらに行こう！ Hiro rendered performance | common_3dmv | 110.457324263 | 220 | 219 | 4758 | 4758 | 4757 | 4753 | 0.0519744416256 | 0.123285691095 | 2.87870287895 | 0.134461923872 | 0.492264588262 | 0.114155520212 | 30.9498908675 |
| H23 | 1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG | ミラクルナナウ(ﾟ∀ﾟ)！ Hiro rendered performance | common_3dmv | 116.657052154 | 199 | 198 | 5025 | 5025 | 5024 | 5020 | 0.0477612482638 | 0.250775712436 | 2.78012156487 | 0.141968575466 | 0.589226878075 | 0.170948281403 | 211.058496695 |
| H24 | 1oSoTZTGZNYN4Oq3R1Lwym0cZ8jWHtvxe | コンテンポラリのダンス authored official MV | individual_only | 205.055419501 | 353 | 352 | 8832 | 8832 | 8831 | 8827 | 0.0214044251781 | 0.0610728577028 | 2.59952545166 | 0.143240912416 | 0.558807873662 | 0.0273697495055 | 17.6274665814 |
| H25 | 1K9In8GKh9pP041E6A0zg3hyX-lKdug7G | ENDLESS DANCE Hiro rendered performance | common_3dmv | 109.435646259 | 241 | 240 | 4714 | 4714 | 4713 | 4709 | 0.0235282765151 | 0.210185844013 | 2.94575667381 | 0.106234503862 | 0.517910366951 | 0.143633225107 | 66.6029070685 |
| H26 | 1laiDZzcPX6UA-Hz9NHaoAvdc8bX2Q6nW | 標 China/Hiro duet rendering | individual_only | 228.182494331 | 542 | 541 | 9828 | 9828 | 9827 | 9823 | 0.0340197870909 | 0.160181897711 | 3.08997178078 | 0.115920839858 | 0.40200567332 | 0.0300203876575 | 18.6284859608 |
| H27 | 1obrkIYn5VQl-7hkwnbC0Jck6ILDQH7Tv | ガラクタロード Hiro rendered performance | individual_only | 163.863219955 | 352 | 351 | 7058 | 7058 | 7057 | 7053 | 0.0367706138621 | 0.141921264679 | 2.88589763641 | 0.15717122185 | 0.426078605637 | 0.113943995432 | 7.70738505013 |
| H28 | 19ZDDv3IlyKBryQL9U9Xi7akxuW_ZJ5zt | みちなるひろがる Hiro/China rendered performance | individual_only | 154.505578231 | 293 | 292 | 6655 | 6655 | 6654 | 6650 | 0.0514520586402 | 0.172458799276 | 3.07728672028 | 0.111590671091 | 0.570932220951 | 0.0787612718876 | 30.5417483211 |
| H29 | 1S15fh_ENDBLtY8IhjdsHo1D4B8YjKp3E | みちなるひろがる authored official MV | individual_only | 205.334058957 | 409 | 408 | 8844 | 8844 | 8843 | 8839 | 0.0494926221059 | 0.166930995954 | 3.12144231796 | 0.145606362743 | 0.372335560437 | 0.0287549183715 | 4.88467733231 |
| H30 | 1UaOzLCa1P0Yd0Npw86Tj65NFGubgbbhw | ハッピーミルフィーユ Hiro rendered performance | individual_only | 101.169342404 | 169 | 168 | 4358 | 4358 | 4357 | 4353 | 0.06209942642 | 0.189772174161 | 2.83473181725 | 0.140453773801 | 0.5048508176 | 0.150747087199 | 63.611106383 |
| H31 | 16urNa641Iy6wsq-EWxQaqYgyFX4r1sfM | 仮装狂騒曲 Hiro rendered performance | individual_only | 105.674013605 | 232 | 231 | 4552 | 4552 | 4551 | 4547 | 0.0350941665099 | 0.1801094397 | 2.89733242989 | 0.128076328216 | 0.501299720278 | 0.150604506976 | 230.283647623 |
| H32 | 1K1pfcfYCj7Xgs1Z5z0bbjwoo3Go7YRiq | メクルメ official Game Size lyric video | individual_only | 152.137142857 | 368 | 367 | 6553 | 6553 | 6552 | 6548 | 0.0386649387207 | 0.205583270664 | 3.03482151031 | 0.107780591755 | 0.811993120052 | 0.0971689039804 | 32.8790065747 |
| H33 | 10pmdSfOxpvp5x_zUh8KwmtgzZ9ALNI5C | メクルメ full/static presentation | individual_only | 196.892154195 | 336 | 335 | 8480 | 8480 | 8479 | 8475 | 0.049294376824 | 0.194971428572 | 3.14816975594 | 0.11179047473 | 0.728212493658 | 0.0551790417848 | 14.6013893929 |

## Equal-source arithmetic means

| Group | Source n | Members | beat_interval_cv | local_tempo_cv | chroma_entropy_bits_mean | tonnetz_motion_mean | flux_cv | flatness_mean | rms_p90_p10_db |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| principal_3dmv | 3 | H12, H15, H17 | 0.0441366917508 | 0.167536577561 | 2.93582479159 | 0.120182258197 | 0.441073066434 | 0.0814987114913 | 23.7780588131 |
| common_3dmv | 6 | H19, H20, H21, H22, H23, H25 | 0.0437059404835 | 0.194384630085 | 2.92573281129 | 0.134923419039 | 0.457609683265 | 0.112836087598 | 60.5825248389 |

No experimental-proxy mean or rank is available. Compare numerical differences only under the stated estimator assumptions; beat tracking has not been audition-validated. Per-source hashes, spectral window counts and loudness are in the source detail.

## Reproduce group means

```python
import json, statistics
from pathlib import Path
root=Path("measurements/HIRO")
manifest=json.loads(Path("repo/series/gakuen-idolmaster/05_AUDIOVISUAL_ANALYSIS/07_SHINOSAWA_HIRO/GKM_PHASE3_HIRO_AUDIOVISUAL_SOURCE_MANIFEST.json").read_text())
groups={'principal_3dmv': [12, 15, 17], 'common_3dmv': [19, 20, 21, 22, 23, 25]}
features=['beat_interval_cv', 'local_tempo_cv', 'chroma_entropy_bits_mean', 'tonnetz_motion_mean', 'flux_cv', 'flatness_mean', 'rms_p90_p10_db']
for group,indices in groups.items():
    values=[json.loads((root/(manifest["sources"][i-1]["drive_id"]+".json")).read_text())["audio_metrics"] for i in indices]
    print(group,len(values),{k:statistics.mean(v[k] for v in values) for k in features})
```
