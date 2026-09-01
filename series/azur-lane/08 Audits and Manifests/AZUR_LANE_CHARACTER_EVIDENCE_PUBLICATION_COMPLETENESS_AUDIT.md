# Azur Lane Character Evidence Publication Completeness Audit

Status: **PASS WITH DOCUMENTED VOICE LIMITATIONS**

Generated: 2026-08-26

## Scope and source lock

This audit compares each target character's local `CHARACTER_MANIFEST.json` output set with the recursively enumerated canonical Google Drive Analysis tree, repairs the existing canonical objects in place, and performs post-publication readback. It does not change semantic conclusions or refresh upstream repositories.

- Build: `AZL-2026-08-22-4cca5c24-cc8e9fdf`
- AzurLaneData: `4cca5c2437007b62d30a6235fcfc0c0203231378`
- AzurLaneLuaScripts: `cc8e9fdf6a1a2e5d20c9a8ff6c0369832bb33336`
- Character manifest: `character-build-2.1.0`
- Semantic authority: CN / origin
- Regional witnesses: JP, EN, TW, KR

## Aggregate result

| Measure | Result |
|---|---:|
| Characters audited | 17 |
| Manifest-declared outputs audited | 1,629 |
| Canonical character objects after remediation, including 17 manifests | 1,646 |
| Initial missing/local-only character outputs | 809 |
| Initial stale generated metadata objects | 61 |
| Additional latent same-size mismatches found by readback | 5 |
| Readable nested social objects parent-routed into canonical character trees | 105 |
| Artifacts newly published from existing local bytes | 809 |
| Artifacts regenerated from upstream | 0 |
| Final missing character objects | 0 |
| Final unreadable character objects | 0 |
| Final unresolved hash mismatches | 0 |
| New-character Analysis readbacks | 871 SHA-256 matches + 1 complete streamed-size match |
| Earlier-character refreshed metadata readbacks | 61 SHA-256 matches |
| New listening/source supporting readbacks | 61 SHA-256 matches |
| JP WAV readbacks retained from the audio publication pass | 841 SHA-256 matches |
| JP source bundles in publication manifest | 344 / 344 |
| Publication-blocked characters | 0 |
| Pipeline-blocked characters | 0 |
| Source-identity-blocked characters | 0 |
| E2E_READY | 0 |
| E2E_READY_WITH_DOCUMENTED_SOURCE_ABSENCE | 2 |
| E2E_READY_WITH_VOICE_LIMITATION | 15 |

One Akagi human-readable narrative artifact exceeds the connector's 64 MiB inline frame ceiling. It was downloaded through the Drive streaming path and its complete byte count matched the local file; the other 871 new-character Analysis objects were raw-byte SHA-256 matched.

## Publication accounting

“Manifest outputs” excludes the manifest file itself. “Drive objects” includes it. “Restored” means the exact existing local bytes were published; no character evidence was semantically regenerated.

The byte-readback pass also revealed 105 social-family objects whose IDs were readable but whose parents were outside their canonical character trees. The same verified objects were attached to the correct `social/fleet_chat`, `social/juustagram`, and applicable `social/island_relationship_trigger` folders. No replacement copies were created.

| Character | ID | Manifest outputs | Drive before | Missing/local-only | Restored | Drive after | Readback result |
|---|---:|---:|---:|---:|---:|---:|---|
| Akagi | 30701 | 89 | 7 | 83 | 83 | 90 | 89 SHA-256 + 1 streamed-size; 0 final mismatches |
| Atago | 30312 | 103 | 104 | 0 | 0 | 104 | 8 refreshed files SHA-256 verified |
| Ayanami | 30105 | 88 | 7 | 82 | 82 | 89 | 89 SHA-256; 0 final mismatches |
| Baltimore | 10316 | 89 | 90 | 0 | 0 | 90 | 8 refreshed files SHA-256 verified |
| Bremerton | 10324 | 89 | 7 | 83 | 83 | 90 | 90 SHA-256; 0 final mismatches |
| Cheshire | 29903 | 110 | 7 | 104 | 104 | 111 | 111 SHA-256; 2 stale objects repaired |
| Enterprise | 10706 | 89 | 90 | 0 | 0 | 90 | 8 refreshed files SHA-256 verified |
| Formidable | 20705 | 94 | 7 | 88 | 88 | 95 | 95 SHA-256; 1 stale object repaired |
| Kaga | 30702 | 89 | 7 | 83 | 83 | 90 | 90 SHA-256; 1 stale object repaired |
| Kirishima | 30404 | 84 | 85 | 0 | 0 | 85 | 8 refreshed files SHA-256 verified |
| Le Malin | 90111 | 105 | 7 | 99 | 99 | 106 | 106 SHA-256; 0 final mismatches |
| Nagato | 30505 | 89 | 90 | 0 | 0 | 90 | 8 refreshed files SHA-256 verified |
| Owari | 30513 | 89 | 7 | 83 | 83 | 90 | 90 SHA-256; 1 stale object repaired |
| Prinz Eugen | 40303 | 110 | 7 | 104 | 104 | 111 | 111 SHA-256; 0 final mismatches |
| St. Louis | 10213 | 89 | 90 | 0 | 0 | 90 | 8 refreshed files SHA-256 verified |
| Taihou | 30707 | 124 | 125 | 0 | 0 | 125 | 8 refreshed files SHA-256 verified |
| Takao | 30311 | 99 | 100 | 0 | 0 | 100 | 5 refreshed files SHA-256 verified |

## Evidence and readiness

All rows have a published CN dialogue ledger, complete contextual narrative corpus and scene index where scenes exist, social and relationship evidence, multilingual regional crosswalk, explicit Dorm3D/Island status, and JP audio mapping/index. Memory chapter counts of zero are explicit `NOT_FOUND` states rather than publication gaps. Regional crosswalk state is `PUBLISHED`; the number shown is the manifest's regional alignment-record count.

| Character | Scenes | Memory chapters | Dialogue records | Social threads | Regional | Dorm3D | Island | JP mapping / waveform publication | Final state |
|---|---:|---:|---:|---:|---|---|---|---|---|
| Akagi | 163 | 7 | 109 | 21 | PUBLISHED / 14,046 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 101 mapped; 1 text-side unresolved; 102 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Atago | 31 | 7 | 92 | 5 | PUBLISHED / 1,384 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_PARTIAL; 71 mapped; 14 unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Ayanami | 183 | 19 | 217 | 17 | PUBLISHED / 7,126 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 109 mapped; 96 text-side unresolved; 110 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Baltimore | 81 | 4 | 105 | 9 | PUBLISHED / 3,869 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_READY mapping; 100 mapped; 0 text-side unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Bremerton | 41 | 7 | 108 | 17 | PUBLISHED / 1,675 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_READY; 101 mapped; 0 text-side unresolved; 102 WAVs readback verified | E2E_READY_WITH_DOCUMENTED_SOURCE_ABSENCE |
| Cheshire | 16 | 0 | 107 | 10 | PUBLISHED / 1,279 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_PARTIAL; 99 mapped; 2 text-side unresolved; 100 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Enterprise | 178 | 0 | 156 | 12 | PUBLISHED / 13,426 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 120 mapped; 25 unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Formidable | 41 | 0 | 119 | 10 | PUBLISHED / 2,331 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 101 mapped; 12 text-side unresolved; 102 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Kaga | 87 | 0 | 119 | 9 | PUBLISHED / 6,627 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 71 mapped; 40 text-side unresolved; 73 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Kirishima | 13 | 0 | 71 | 5 | PUBLISHED / 772 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 65 mapped; 1 unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Le Malin | 28 | 7 | 75 | 18 | PUBLISHED / 2,087 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_PARTIAL; 70 mapped; 1 text-side unresolved; 71 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Nagato | 74 | 0 | 113 | 6 | PUBLISHED / 7,767 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_READY mapping; 106 mapped; 0 text-side unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Owari | 23 | 0 | 67 | 11 | PUBLISHED / 1,862 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 65 mapped; 1 text-side unresolved; 66 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| Prinz Eugen | 127 | 0 | 125 | 17 | PUBLISHED / 5,902 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_PARTIAL; 114 mapped; 1 text-side unresolved; 115 WAVs readback verified | E2E_READY_WITH_VOICE_LIMITATION |
| St. Louis | 18 | 0 | 77 | 5 | PUBLISHED / 980 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_NOT_FOUND | AUDIO_PARTIAL; 71 mapped; 1 unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Taihou | 28 | 7 | 116 | 25 | PUBLISHED / 2,541 | chat PRESENT; non-chat SUPPORTED_PRESENT | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_PARTIAL; 152 mapped; 57 unresolved; WAV pack readback pending | E2E_READY_WITH_VOICE_LIMITATION |
| Takao | 43 | 7 | 120 | 5 | PUBLISHED / 3,369 | chat NOT_FOUND; non-chat SUPPORTED_NOT_FOUND | relationship NOT_FOUND; non-relationship SUPPORTED_PRESENT | AUDIO_READY; 114 mapped; 0 text-side unresolved; 115 WAVs including one non-text review asset readback verified | E2E_READY_WITH_DOCUMENTED_SOURCE_ABSENCE |

## Boundary and validation

- Analysis contains no source audio binaries; original JP client bundles remain under the canonical Primary Sources root.
- The source-bundle publication manifest records 344 assets / 159,277,728 bytes. The 33 newly ledgered bundles were downloaded from Drive and SHA-256 matched.
- The nine new listening metadata packages were updated in place and all 27 files were SHA-256 readback verified.
- No connector-retry character folders or parallel corpus roots were created.
- Final recursive Drive enumeration found exactly 1,646 character objects and zero duplicate relative paths.
- Pipeline validation checked 237,755 records with zero failures.
- Test result: 100 passed, 10 skipped, 210 subtests passed.
- All 1,629 manifest-declared local hashes validate against local emitted bytes.

## Remaining limitations

There are no remaining publication blockers. Voice limitations are source/mapping or waveform-readback states explicitly represented in each character's audio coverage and listening pack. They do not prevent R0-R9 semantic reconstruction. Enterprise's existing `IDENTITY_AMBIGUITY` composition warning remains documented; it did not produce a manifest identity-validation failure and was not normalized or silently merged by this remediation.

## Prinz Eugen gate

`PRINZ_EUGEN_40303` is ready for `AZUR_LANE_PRINZ_EUGEN_NARRATIVE_DEEP_READING.md` across all 127 CN scenes. The character folder now exposes the dialogue ledger, complete/raw CN narrative corpora, scene index, social reconstruction, relationship evidence, regional crosswalk, Island evidence, and JP audio index. All 111 Drive objects in the character tree were read back and SHA-256 matched to the local canonical bytes. R10 remains explicitly partial because one text-side voice record is unresolved.
