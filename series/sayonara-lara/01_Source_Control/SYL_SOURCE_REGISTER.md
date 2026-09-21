---
title: "Sayonara Lara: Source Register"
artifact_id: SYL_SOURCE_REGISTER
artifact_type: source_register
series: Sayonara Lara
generation: V1_JP_AUDITED
version: "1.3"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-20"
source_boundary: "Owner-supplied E01-E12 analytical bundles and complete FLAC derivatives"
---

# Source register

## Admitted evidence boundary

The admitted narrative corpus is the twelve-episode Japanese-language television anime, E01-E12. The owner supplied twelve exploded analytical bundles, matching ZIP transports, and twelve complete stereo FLAC files in a local evidence plane. This Git record contains public-safe identity, hashes, timing, and coverage only; no source media, subtitles, screenshots, audio, ZIPs, or private filesystem paths are committed.

Each bundle exposes source-encode identity, clean timestamped frames, frame/scene/dialogue indexes, contact sheets, aligned Japanese captions, paired English subtitles as a secondary aid, complete audio, and extraction QA. Source-video filenames identify 1080p SubsPlease encodes and their release CRC tags. The source MKV bytes and untouched ABEMA Japanese caption files are outside the supplied input root and were not independently hashed here.

## Bundle inventory

| Source ID | Episode | Encode tag | Duration s | JP cues | Frames / sheets | Scenes | JP offset s / onset MAD s | Bundle ZIP SHA-256 |
|---|---:|---|---:|---:|---:|---:|---|---|
| SYL-B01 | E01 | `B35CE9B2` | 1439.985 | 323 | 843 / 43 | 15 | -0.153 / 0.0180 | `360af8d669908916e73195292cbd1d0578ba625479af99e65af04c42de4adf52` |
| SYL-B02 | E02 | `6BA90D3E` | 1440.125 | 327 | 827 / 42 | 20 | -0.174 / 0.0190 | `a3f4a8622b40dea230dc3e31a18a4961f48fb0b25e24f231ed03f22be8d865ab` |
| SYL-B03 | E03 | `BDA70D82` | 1440.078 | 399 | 872 / 44 | 8 | -0.219 / 0.0185 | `e05c3a5597d4c8852259bf59182e90141f170f1baf210babd588377baebaed11` |
| SYL-B04 | E04 | `FC189C9E` | 1440.078 | 416 | 713 / 36 | 10 | -0.174 / 0.0170 | `c90d72e82425618a0100f1aa10f17e879715633a0cd70340cfb935e2e6603607` |
| SYL-B05 | E05 | `AAA4ECFF` | 1440.032 | 338 | 807 / 41 | 12 | -0.118 / 0.0180 | `5bd9f41c483c7860d07adc7248ff1c1c5a0b9ca07029b9a75cf176269d45b5c2` |
| SYL-B06 | E06 | `48A6E3AB` | 1440.032 | 279 | 772 / 39 | 17 | -0.123 / 0.0170 | `63c1fa708706e154dd948eadd63cae9488d9128081fd24e4d1c5375ab4f3c0a7` |
| SYL-B07 | E07 | `584CBF7E` | 1440.250 | 323 | 775 / 39 | 18 | -0.287 / 0.0190 | `ca53b3dd7f05e773a0e22e53dd8a3c07fb396e2c332cfc2c375b46b7b2552cfc` |
| SYL-B08 | E08 | `B6C8BA30` | 1440.125 | 336 | 771 / 39 | 17 | -0.121 / 0.0170 | `0d5f753ec390dfcbaddf5b9d0fb5bdd5fa6e7abf1f6413f861718eba22e6d69b` |
| SYL-B09 | E09 | `32419239` | 1440.250 | 320 | 728 / 37 | 18 | -0.125 / 0.0175 | `8b615617d7b427adbb437f5f3cf9b5afab9dba20accffe5f39a876fff5af1bb4` |
| SYL-B10 | E10 | `4D5D30D1` | 1440.125 | 341 | 789 / 40 | 16 | -0.139 / 0.0175 | `df74d01d2c28732fd5011f4305fdba8543734bf3fab425ad30b002bc74e54312` |
| SYL-B11 | E11 | `D783C7EA` | 1440.250 | 330 | 699 / 35 | 16 | -0.123 / 0.0140 | `0620ef2106bee77ca1526e8af096400d754cfd36c29300a9336c5e6eed512409` |
| SYL-B12 | E12 | `47938DD3` | 1440.125 | 376 | 757 / 38 | 12 | -0.137 / 0.0165 | `24290a642d5a43c498297838420b019d7627f2a0aa6b011b9c40f8ab92004433` |

The aligned-caption metadata reports constant-offset alignment from an ABEMA Japanese closed-caption SRT, robust matched-cue onset peaks, three-window drift audit, and no drift correction beyond the per-episode constant offsets above. Reported post-alignment activity F1 ranges from 0.878903 to 0.925633. This is timing QA, not proof that every caption exactly matches performed wording.

## Key derivative locks

| Episode | FLAC SHA-256 | Aligned JP ASS SHA-256 | Dialogue-index CSV SHA-256 | Manifest CSV SHA-256 |
|---:|---|---|---|---|
| E01 | `b8d55af9b59add964b590f874244cbbfad71ffea906bdf19a975f3c743e97a62` | `2236805a2def68fd24634d068b4fe44f6c0667e0a0054035f4a668f3d4948d71` | `1ca37a1e7986328411a69943889576d5688075cc6d8bd9fef18cff1ca43bd67a` | `85ce95f89bc338ba76ada9f7acd61e0423e3f1274510c591e8df856ced346cfd` |
| E02 | `042ba859c48be4a161692b8ea739c018cbd8422505f98e0d04bc75cd5dc474c9` | `48cd5cda7c6a7f4456c79cca2220caa18615508c08de2e0194c97790cbbdc2b1` | `7b0770fb8260e5929410767d2f2b9545eb734a5d5030849bf9a94438c49119c5` | `bc6c8df5c2fc09da3cbe1ae1b809111396a1406c257905f20acaf53626eb6752` |
| E03 | `be817d18049abc503b92eb57184597ade42cf1ad02e04b0269856a5dc3f1073e` | `8349afb4a02019c2a1828c840c640aa9451624e47d6a73120ad056e2acd7631f` | `5aba77d301e0b8c05d1ddb3dac192de0ffe015aec39e36320db0cd83e2b99a19` | `fbbcc8473f38cbb51c02ec1f6da96391eb1fd69c33e67b20b98370533bf457f7` |
| E04 | `c95e3b4846ec073228fa279faf79968118c59f821d9d2d23b2fa3d1ff0ddeca4` | `01a9cdef73ced5715d1c1e1ed78682a177a12f8672bf060b7001575f9baf2591` | `ffed7a5a38fda992228a8df4be9c8e9ef4b9765e7c9ca98b0ac318d012957bf7` | `20ebc1efb34fb116d50e015ecce0c523d124b605ee4fd9f8c89b4ea1acfa608b` |
| E05 | `1fe13ac357aad685db69b4f4925f27ce587b025948e5dcb74679d9dbf918d9fe` | `1398117cfc95be5668390652aa891dd8ec7340c5c7dd098acd63ca5fe5782e66` | `92cf196c4ab466702d25bff8af37987c264c45ba58c2c5dc858f4e162abce470` | `ca9a7e8a4bd6f41c3588a7402988da087f5e9a1ea087080c11a02f3657537d25` |
| E06 | `6661c8c737c76c529d71ab184086a36a25ca2b5aaca1d40b954b2ff68c1ea33f` | `fed4e8b4c9b7f116b0eaa7c55b12d2b4d5ff8e698eca38116475e35b5aaec32b` | `84400523d81c13436dd94d5d32aedcdf1c70cc5b5e493273a0169c544b38589a` | `455996004c969a8302ec3517453cb9ef67730f027a704f0cb6eca6f02e716bd9` |
| E07 | `ea43ca74c14a3d12c9105101f4957405361e1eb9110d505fc8f61a0da5bca329` | `a17d32158a21b561adcaa7b5030790b46b1366b7408b8edca0b8742d6fac0771` | `12deb4e3c3ee238685b191f9db0caea9167bc4c264e169dd60aee6a6c8642422` | `aa8d956b170f8dfd08b036df3557df3152349ba198f8bef8f0858b14a4e2992c` |
| E08 | `e87d3f7ed201d0f4adecbf136a02b1f1a5348dc4228f3a1b33e2f458c5178c76` | `6d1640c1798a7c9f9b7002bcd636cddfac162f4facbd702977c838165c0599c1` | `87861e6236d0a0a3fea49a4bd89f21e7a07e5cc99c5e1b58681064bbdcd2eb73` | `bc095a21fac6960a197077d54c49a8ad340c0c80b5c1f0c95cfd1aa343b04825` |
| E09 | `366c330f177823842e172c5b5e52158383b39978fccb9c915d08e3d0fa8ee6a9` | `16d974acdc671e6e861da0ffa4e3b23c92642dce3cbb98c0c367ad603cb4ac4f` | `db5bda496a0bb56bb660d102d3a853eaea0712b25f7cb761b33db0df9ce298fd` | `462bbf2b7f435dc3790cb66dfeabf67d4848305ba21d941b68aa017b9567a39d` |
| E10 | `cabe2420e0718de1c24ee869dd89ac76f1e43534db84e32cf3c963401e865acb` | `62788856d4c2e80f54b5b1a26baf9fe69f114a70f742ecfb4544884104c8ba1c` | `34b2a8d9f1326f3cd649a0902b514baec352211dace71f9982564dcde6201c04` | `0139923e7615ec7d1ed0d70fc1623ab0c3efcc169765487846f4574809e42186` |
| E11 | `2e629ce2c72c8582e879b3efaa16c81738b6920201f7deb143b08827e8290be5` | `7472a853b65a35c6669cec114fe3de9f0c92eb8a0e7cb9991a8e3fde3b6604fb` | `d15f13063ebe3c2633070f0749eb574dafff09c46220177238aec9459f012bb8` | `06f771ff8b5ce78c7ae51953f94e237d192f30941ff6c0e79a16ecd07e2b9fc6` |
| E12 | `171f209316e069ec0743d8b1de829d553204b0b9c6ae4101f09fea24d6c56fc3` | `ad1dd27e74c699c1d53a79f3421e6d1b4efbcd079054b044608c107310334eb9` | `3dd212862f09e30a37e53514070cd5bb294e26d8dea942ff582a0e5785f5f79c` | `c1a17bbe495e1a97e4a9b700d29c1de7b29c3a2839231db02f9d5ea2b9580b45` |

## Inspection state

All twelve containers and key derivatives are inventory-verified and hash-locked. E01-E03 narrative inspection is complete for each reading's declared Japanese-caption and static-visual scope. E03 coverage includes all 399 aligned Japanese cues, all 44 contact sheets, and selected original-resolution claim frames. Auditory interpretation and continuous-video inspection were not performed. E04-E12 remain available but narratively uninspected at this boundary. Per-episode completion is recorded in the execution record and episode reading; file availability must never be reported as inspection coverage.
