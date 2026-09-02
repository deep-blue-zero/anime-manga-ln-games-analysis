# Artifact Exclusion Report

## Scope

This report summarizes the complete approved G5 migration boundary. The authoritative row-level review remains local migration evidence because it contains source-environment paths and identifiers that are not required as public repository content.

## Final aggregate disposition

| Terminal action | Records | Git treatment |
|---|---:|---|
| `REFERENCE_DRIVE` | 2,536 effective in the frozen review; 249 files in the final live snapshot | No payload committed; public-safe provenance and hashes only where needed |
| `OMIT_EMPTY` | 84 | Empty structural source omitted |
| `VERIFIED_EXCLUDED` | 7 | No payload committed after review |

The complete sealed 2,752-row TSV has SHA-256 `8462bce2293aa06ee2ed92678272fff802c3e40fb1870d18a71691bcaac03ab8` and records 2,661 original `REFERENCE_DRIVE` dispositions. G7 correction overlays promote three Shokugeki artifacts and 122 additional human-readable analytical or small structured-support artifacts to Git materialization, yielding the 2,536 effective frozen-review count above without mutating the sealed base review. The final live snapshot has only 249 current `REFERENCE_DRIVE` files because the separately retained Azur Lane generated corpus was moved outside the analytical root. Binary archives, source media, scans, large generated corpora, redundant release bundles, and native Office/PDF originals with sufficient text derivatives remain outside Git unless explicitly named by a future exception.

## G7 Shokugeki analytical-classification repair

| Artifact | Drive file ID | Bytes | Source SHA-256 | Corrected disposition |
|---|---|---:|---|---|
| `SHOKUGEKI_SOMA_BEHAVIORAL_MODEL_LEDGER.md` | `1SydrqDMZFoXyU0p6QAI_JqLcflAOjSoL` | 65,510 | `31bbd94ab47497c2e9d7d7aba7334311cbf549bc55ad5e6598c05edbfd784730` | `MIGRATE_TEXT` |
| `SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md` | `1fy19pvClZ6-HKlpxF4-ozgGBH8fo0JCT` | 73,516 | `26a018568317b4c2ad5b25430310a7a463e43248f78b084612cdb47f4f7acf23` | `MIGRATE_TEXT` |
| `SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md` | `1My5KOqCG2_4lWkZZOPAxVP_YiwCyQkfu` | 57,410 | `6cb2d830c6352259727231c0c65779bea6a5cba79a87eadb0e19b262f5cadf50` | `MIGRATE_TEXT` |

This repair introduces no binary, LFS, large-text, or rights exception. The false positive arose from filename tokens (`MODEL`, `AUDIT`), not from the files' content class.

## G7 final stale-disposition repair

The repository-wide recheck promoted 122 additional false-positive exclusions: human-readable analytical Markdown and, for the 86 - Eighty-Six character-reference package, the small machine-readable integrity and verification companions needed to make the profiles independently checkable. Source identity, revision, size, and acquisition SHA-256 were verified before materialization. No internal Drive link required rewriting, and no binary, archive, LFS, over-1-MiB generated-table, primary-source, rights, or large-text exception was introduced.

| Repository scope | Artifacts promoted |
|---|---:|
| 86 - Eighty-Six | 84 |
| AoButa | 1 |
| Attack on Titan | 5 |
| Gakuen Idolmaster | 1 |
| KonoSuba | 3 |
| Love Live! Superstar!! | 1 |
| My Hero Academia | 2 |
| One Punch Man | 2 |
| Oregairu | 8 |
| Repository governance | 1 |
| Solo Leveling | 5 |
| Sound! Euphonium | 9 |
| **Total** | **122** |

The local materialization receipt has SHA-256 `a96308c35a9075f54ff546926740f893b9921bcb857efe0284eeaab979f3109b`. The final convergent reconciliation summary has SHA-256 `9dc77d7f19301b0ee34ba50165964bfe8358c6988b446ad6413b3ba87ad3f5fa`; it closes all 3,185 current Drive files with no ambiguous disposition or Git hash failure.

## U149 tranche

The P01 U149 source slice contains 15 Markdown artifacts and no binary artifact. All 15 were materialized as prospective Git content after deterministic authority-front-matter normalization. The conversation transcript remains present for provenance but is marked `historical_legacy` and barred from current authority.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Markdown analytical artifacts | 14 | `MIGRATE_TEXT` | Human- and LLM-readable analysis |
| Markdown historical transcript | 1 | `MIGRATE_TEXT_HISTORICAL_ONLY` | Provenance retained; current-authority veto applied |
| Binary artifacts in P01 U149 slice | 0 | Not applicable | None were present in the approved source slice |

## P02 large-structured-text boundary

The P02 slice contains exactly two artifacts. The IDOLY PRIDE source-to-bundle provenance ledger is the archive's named large-text exception: it exceeds 1 MiB, remains below 25 MiB, passed content-safety review, and is admitted as an exact byte-preserved CSV. The much larger Azur Lane structural-alignment JSONL is generated extraction output over the 10 MiB default-external threshold and remains outside Git.

| Artifact | Drive file ID | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| IDOLY PRIDE source-to-bundle provenance CSV | `1EySpUScZKZ2irfYamER1e8FCrnjniGjk` | 1,377,633 | `7dde60c452627a694307dda68abfb0d4d434ec1c2ce934bf85a0b81db483c366` | `MIGRATE_EXACT`; named large-text exception; content-safety postreview passed |
| Azur Lane `structural_alignment.jsonl` | `1US_aDBA1ttPuUx-WlMfr7559PB8vq6we` | 86,490,198 | `ce3d0b9a6df171fdb5d52e7c509d08c35f49ddbc3cbb03e27ca12a079b247a37` | `REFERENCE_DRIVE`; generated/extracted corpus over 10 MiB; no Git destination |

The P02 frozen source slice has SHA-256 `c3e42495cf2a80d93e29245a494ab29533fd30113ceb418ba8f2caa2920c4f19`; its representation slice has SHA-256 `28ec52b8524a49484071cab3660b548ee2c83b24f6402079ace1a19ccebdb005`; and its validated local materialization receipt has SHA-256 `3207c68b9c9b1a51c0e368d50ad8009176db1a1ce926e7b03bd1e0fb03e88de2`.

## P03 native document and sheet

| Artifact | Drive file ID | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| DJFW current-state/corpus-map DOCX export | `10hQeZP3j1AUQ00YsOmt4xYIJmUOant0NsdXXkbmfs3Y` | 13,427 | `76600ca58154f45a2e597d1d34d09f5dacb60ec9235cde1c9a93fbca74439228` | Private conversion evidence; a normalized Markdown derivative is tracked |
| DJFW project-control workbook (`.xlsx`) | `1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg` | 56,138 | `5cebbd385b260e349ac54befbc22b5edc80bb8e9e96b4997eac507f123eb72af` | `REFERENCE_DRIVE`; 17 TSV projections plus a structure manifest are tracked |

The tracked derivatives contain one Markdown corpus map, 17 UTF-8/LF TSV worksheet projections, and one structure manifest. This is a partial control-state pilot, not a complete DJFW study migration. The source XLSX and DOCX are not tracked. Six DOCX render PNGs, one DOCX render PDF, seventeen worksheet preview PNGs, the earlier equivalent DOCX/XLSX export envelopes, and the superseded faulty TSV derivatives remain private validation evidence outside Git. The frozen representation slice's earlier XLSX `MIGRATE_TRANSFORMED` row is superseded by the approved X1 disposition and is not current policy. The P03 frozen source slice has SHA-256 `4de71ba55b23bc6e429dd6e4ac942efb47d6370f3cd6e589cc3970f9087d0c54`; its representation slice has SHA-256 `9f116606266962dfc869513ee6b984108bab56ed6af1301b9ea93ffd6a89a193`.

## P04 ZIP/reference boundary

P04 records six archive identities totaling 814,501 bytes and materializes none of them. The frozen source slice has SHA-256 `4c2130e9608ec85ea9b1ca02fe5b0ed4c37f6108979eb950c9f87e12308a6c04`; the validated reference-only receipt has SHA-256 `a802b0765d51109b4c2fa1bc18a78d42e772589073e522f706aa49d8b9ffbce4`; and the representation slice is `null`. The two same-logical-path Temari objects and two same-logical-path Lilja objects remain distinct by Drive file ID, byte length, and SHA-256. At the P04 pilot checkpoint, no archive bytes, extracted members, LFS objects, or Gakuen Idolmaster analysis tree were tracked. The later aggregate migration adds eligible Gakuen Idolmaster text while the six named archives remain destination-free references.

| Drive file ID | Source archive identity | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| `1KjeSZCwRGXuNn4Lyo1S-VmgIP3_PlDrd` | `Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/GAKUEN_IDOLMASTER_PHASE3_TEMARI_CHARACTER_CORE.zip` | 122,672 | `40b355004c1b176f39779303b60dbd33415a0bb88810d3132df7e22c86376a1b` | `REFERENCE_DRIVE`; no Git destination |
| `1_FOnm73lxvcx1QwLxS-1AA896C_2_1Ik` | `Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/GAKUEN_IDOLMASTER_PHASE3_LILJA_CHARACTER_CORE.zip` | 129,983 | `8b28d8a806763472826b800c2a0e5b34f749c86154cf5a251a82036ac81dadd2` | `REFERENCE_DRIVE`; no Git destination |
| `1j6EvtMB11kG3E1s-eoB6RcRWyhrfDZyc` | `Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/GAKUEN_IDOLMASTER_PHASE3_TEMARI_COMPLETE_AUDIOVISUAL_BASELINE.zip` | 131,808 | `af05ee2c76b35e2d84344e2070fb24b84c0c26e6e44a835d6835cd94bc4206d7` | `REFERENCE_DRIVE`; no Git destination |
| `1oVFv4UQJbqqhY1nCnG9wmkduSh7mgM8U` | `Gakuen Idolmaster/05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/05_KATSURAGI_LILJA/GAKUEN_IDOLMASTER_PHASE3_LILJA_INTEGRATED_AV_R1.zip` | 398 | `03a863418e09542118a4afed9f23d034b9f0ee6a4f83f755d79826d29c641b91` | `REFERENCE_DRIVE`; no Git destination |
| `1u3Yc2D3rhzUrhE1XKpTBdE0jj863xD6d` | `Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/GAKUEN_IDOLMASTER_PHASE3_TEMARI_COMPLETE_AUDIOVISUAL_BASELINE.zip` | 429,394 | `7656ee5e8fd5cdf4909da218f35138d8f074754b19cf04b282186656df727294` | `REFERENCE_DRIVE`; no Git destination |
| `1xajzp2rB8zhw0wcCykogJAKGahsPJdgA` | `Gakuen Idolmaster/05_AUDIOVISUAL_ANALYSIS/00_MUSICAL_IDENTITY_BASELINES/05_KATSURAGI_LILJA/GAKUEN_IDOLMASTER_PHASE3_LILJA_INTEGRATED_AV_R1.zip` | 246 | `cd71a44a4d598beb7138171e6c1ae2cfa28cb3da53fc900633f6e127e8d5b221` | `REFERENCE_DRIVE`; no Git destination |

## G5-T01 Maebashi Witches V1

The frozen Maebashi source slice contains exactly 18 Markdown artifacts totaling 1,478,455 source bytes. All are below 1 MiB, passed targeted publication-safety review, and were deterministically transformed into 1,476,404 candidate bytes. No binary, archive, Office/PDF original, generated corpus, LFS object, or named artifact exception is present.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Current analytical Markdown | 16 | `MIGRATE_TEXT` | Human- and LLM-readable reviewed analysis; authority arrays normalized |
| Historical conversation transcript | 1 | `MIGRATE_TEXT_HISTORICAL_ONLY` | Provenance retained; current-authority veto applied |
| Manifest | 1 | `MIGRATE_TEXT` | Post-transform sibling byte/hash integrity table |
| Binary or excluded artifact | 0 | Not applicable | None occurs in the frozen tranche |

Source verification receipt SHA-256: `47ca555a313ef0464323df3d84dbb80c628dad7e879ca62553c193c3b26ada45`. Transformation receipt SHA-256: `8310635453d699ade2c5346ad934562af17c328dbab4537a9d486ced0f7eebf7`.

## G5-T02 Mass Effect comparative media

The frozen Mass Effect group contains exactly three Markdown artifacts totaling 88,990 source bytes. The complete compact corpus passed publication-safety review and was deterministically transformed into 88,926 Git bytes through authority-array normalization, one repository-tree path repair, and one stale related-artifact pointer repair. No binary, archive, original Office/PDF, generated corpus, LFS object, or named artifact exception is present.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Canonical corpus map | 1 | `MIGRATE_TEXT` | Human- and LLM-readable control map; Git tree path repaired |
| Canonical character monographs | 2 | `MIGRATE_TEXT` | Reviewed Paragon/Renegade analytical archetypes; current-authority arrays normalized |
| Binary or excluded artifact | 0 | Not applicable | None occurs in the frozen tranche |

Source verification receipt SHA-256: `1fbe488a500180af2577b2037af5ff9fc4cb83481357f648eb2c9f8a46c82458`. Transformation receipt SHA-256: `abfefc964172556ff038e402f4a970dca4b41241325b02bcbe1be66d215e1f02`.

## G5-T03 Genshin Impact Furina V1

The frozen ordinary-object group contains 40 objects totaling 533,859 source bytes: 39 Git-eligible text and integrity artifacts totaling 367,030 source bytes, plus one 166,829-byte duplicate release ZIP. The 39 text artifacts passed publication-safety review and were deterministically transformed into 366,883 Git bytes. Thirty-seven Markdown files received authority-array normalization; the Markdown manifest, SHA256SUMS, and JSON corpus manifest were regenerated from exact destination bytes.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Reviewed Markdown analysis/control artifacts | 37 | `MIGRATE_TEXT` | Human- and LLM-readable bounded Furina corpus; authority arrays normalized |
| Structured integrity manifest | 1 | `MIGRATE_TEXT` | Machine-readable JSON regenerated from exact Git candidates |
| Checksum ledger | 1 | `MIGRATE_TEXT` | Human- and machine-readable SHA-256 closure over Markdown members |
| Duplicate release ZIP | 1 | `REFERENCE_DRIVE` | Members duplicate the standalone payload; no binary, LFS, or release-bundle exception granted |

Source/revision receipt SHA-256: `707ddb6c072e718fa6e26e6db4c63ee8fb1296e5c90729c662ae46d974e28f67`. Transformation/output-anchor receipt SHA-256: `3c9eb76634cefb047cdb969576c477acba70e11d16319d3fe8b90ac2c0e6440f`. The final 39-output table has SHA-256 `0c982199ad9939da12e329ee249c13f7447d62ceec99e222d797a0621b211858`.

## G5-T04 Cinderella Girls mobile-game analysis

The frozen source boundary contains 26 Drive objects: 23 ordinary Markdown artifacts and three structural folders. All 23 Markdown artifacts passed the existing publication-safety boundary and materialize after the declared authority-array and twelve-line publication-format normalization, totaling 1,424,973 Git bytes. The three folders carry hierarchy/provenance only and remain destination-free `REFERENCE_DRIVE` structural records. No binary, archive, LFS, large-text, rights, or new artifact exception is introduced.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Reviewed Markdown monographs, audits, addendum, and corpus map | 23 | `MIGRATE_TEXT` | Human- and LLM-readable analysis; exact output hashes frozen |
| Structural Drive folders | 3 | `REFERENCE_DRIVE` | Hierarchy/provenance metadata only; folders have no content bytes |
| Binary or archive artifacts | 0 | Not applicable | None are in the exact T04 source boundary |

Source/structural binding SHA-256: `9ab050532d8114ef4e1cbec0423f20f341b61a7ea1f7f70057f256568fff5b74`. Inert preparation receipt SHA-256: `c37d34d559e46234c0dd0353a8e75c67685903ce900543a00aa06cbaeb1ae595`. The final 23-output table has SHA-256 `0b3333c5b5ed0afe39064e8199518401c93ff3d0bb21278efddf7d0a64097923`.

## G5-T05 Blue Archive Prologue/Chapter 1 analysis

The frozen source boundary contains 48 Drive objects: 35 Markdown artifacts, one machine-readable CSV, nine structural folders, and three empty folders. All 36 ordinary analytical artifacts passed the existing publication-safety boundary and materialize after the declared authority-array and publication-format normalizations, totaling 1,925,640 Git bytes. The nine structural folders remain destination-free `REFERENCE_DRIVE` provenance records; the three verified empty folders are `VERIFIED_EXCLUDED`. No binary, archive, LFS, large-text, rights, or named artifact exception is introduced.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Reviewed analytical Markdown | 35 | `MIGRATE_TEXT` | Human- and LLM-readable analysis; exact output hashes frozen |
| Machine-readable analytical CSV | 1 | `MIGRATE_TEXT` | Structured text; CRLF normalized to LF with exact output hash frozen |
| Structural Drive folders | 9 | `REFERENCE_DRIVE` | Hierarchy/provenance metadata only; folders have no content bytes |
| Verified empty folders | 3 | `VERIFIED_EXCLUDED` | No artifact bytes or analytical content |
| Binary or archive artifacts | 0 | Not applicable | None are in the exact T05 source boundary |

Source-selection receipt SHA-256: `e5a5aea807cf711691e0788881aeb5b9223ec4edb92da43cb9e71cf0adefbce1`. Inert materialization receipt SHA-256: `c91539cc3065cd56575c836b638bb795e448eff65392c1689554ff359f1678c5`. The final 36-output table has SHA-256 `0452531eb1a07058ade65e7c1b252ffaaf684ffce22cb3f8aedcc6461ad631e3`.

## G5-T06 Youjo Senki V2 analysis

The frozen full-prefix boundary contains 44 selected objects. Sixteen reviewed Markdown artifacts materialize after only the exact frozen authority-array, CommonMark hard-break, and terminal-LF normalizations, totaling 810,912 Git bytes. Twenty generated or extracted ordinary files totaling 57,369,073 bytes and eight structural folders remain `REFERENCE_DRIVE`; no binary, archive, LFS, large-text, rights, or named artifact exception is introduced. The 52,894,654-byte CMR locator index remains outside Git. Tanya's dedicated legacy monograph is migrated as analysis but remains ineligible for Character Index v2 materialization because the recognized authority quartet is absent.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Reviewed analytical Markdown | 16 | `MIGRATE_TEXT` | Human- and LLM-readable analysis with exact frozen output hashes |
| Generated or extracted reconstruction outputs | 20 | `REFERENCE_DRIVE` | Downstream generated material, including a 52,894,654-byte locator index |
| Structural Drive folders | 8 | `REFERENCE_DRIVE` | Hierarchy/provenance metadata only |

Source-selection receipt SHA-256: `b62ea48fd1742006a78ad6502fc2378f840375a6c9e5e8cb6bf56460b56dc762`. Inert materialization receipt SHA-256: `e47f15c4365ac397136927bbbfda9bfbf2951f142bc4877b155a68b34a7047bd`. The final 16-output table has SHA-256 `fab10f114df2b2132813647122b3e7e4391cd2a914f1c10314a76621cc391fbb`.

Reference-only ordinary artifacts:

| Drive ID | Source path | Bytes | SHA-256 | Disposition |
|---|---|---:|---|---|
| `16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh` | `Youjo Senki/06 Character Modeling and Reconstruction/00 Frameworks and Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md` | 43630 | `405d89789d730ec3ccdff1de020d318dc39c9910b36577d2b3e1f63a52737361` | `REFERENCE_DRIVE` |
| `1d6vk6xFzkML17mwbUmBrWyxNxftptkv4` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/README.md` | 7294 | `cbb374eb7d6a55602300004bd3dda3a13bc3b773c7db46ee0dfef152aeb38059` | `REFERENCE_DRIVE` |
| `1C95SxSuba7Fr9diTMyc1N8q58TbzxsLs` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CHARACTER_ALIAS_MAP.tsv` | 25311 | `567426240c2072a21e6abea40775fd2428a6aec433f85417da2c8de08a8161a9` | `REFERENCE_DRIVE` |
| `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_AUDIT.md` | 26319 | `30ace4c0f4a0b03aa003aea8e7377cb1595450bed326451908a59bf13c5c3417` | `REFERENCE_DRIVE` |
| `13pEqvLZiv8Pc0SjvbsWSYpk_G4VMKZ0b` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_METRICS.tsv` | 5034 | `e5299ffeb29f542c7015003a3f0f8bb8f957793620eaa2d37957ea3a0eeeb6fb` | `REFERENCE_DRIVE` |
| `1keRBa1MAecQmFefKgmnUMroSeOarf1B1` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CMR1_READINESS_AUDIT_SCRIPT.py` | 11609 | `7a563001eef1e24259cb1637077665c5f47cd4690c5e8d9e2d417daeb0a13836` | `REFERENCE_DRIVE` |
| `1zWogK3vzZ0Tj1_92r3NaESIj1NzV1Biv` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md` | 9049 | `67120306369bb343f691f0007d5fbc968eb7de4a083a391f7adeb5914606eaad` | `REFERENCE_DRIVE` |
| `1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CMR_SOURCE_EXTRACTION_SCRIPT.py` | 14916 | `e21635d9f19d5925e2ad3f40aaaf2ac8cfff4d0f1dee8082c49415be09f04adc` | `REFERENCE_DRIVE` |
| `140ow12czVj4J8Q_JR44MSWI98LUxj3uk` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CMR_SOURCE_LOCATOR_INDEX.tsv` | 52894654 | `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe` | `REFERENCE_DRIVE` |
| `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_CMR_SOURCE_MEMBER_INDEX.tsv` | 203927 | `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220` | `REFERENCE_DRIVE` |
| `1JxHeRuCRltCmQsyIs2nQruzewx1U8Bmd` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_MANIFEST.md` | 14888 | `43c1cf9bb04e2883e473a85d2db306b1242741569263778974db1b6229d5b02b` | `REFERENCE_DRIVE` |
| `1whdImFw-vUblagWfpiqEmY58hT1vd3LZ` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2B_ADJUDICATION_SCRIPT.py` | 98103 | `23078662fed83e7aa8ba7c5e59fe9e0946a58ab75abab61a7de0a326e5e6909f` | `REFERENCE_DRIVE` |
| `1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2_ADJUDICATION_LEDGER.tsv` | 648524 | `4391f1042668cdc2148f6e09b975317cb5ab9d20c9e0e1679d491c450a8e6fa0` | `REFERENCE_DRIVE` |
| `1v3oLyOSuwD9WgZX_TvAPekRo20g4m_Rh` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_MANIFEST.md` | 9142 | `2edb901c91698f8bc460909193fc87175dff766181dddc2cf67bf7735121828b` | `REFERENCE_DRIVE` |
| `1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2_CANDIDATE_RETRIEVAL_SCRIPT.py` | 17909 | `95e52f0e50f42c16eec4bb421245d7f150959478451559e6e47614052c87a074` | `REFERENCE_DRIVE` |
| `1LRcSX-k739E4O4xQ2ImZnawzx6IylARo` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2_CANDIDATE_SCENE_POOL.tsv` | 2290984 | `8344b6196565645cfe373d3468fa4f3c618d1c4d3afb363667c64a073a5c469a` | `REFERENCE_DRIVE` |
| `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators/YOUJO_SENKI_TANYA_CMR2_DIAGNOSTIC_EVIDENCE_INDEX.tsv` | 1043995 | `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68` | `REFERENCE_DRIVE` |
| `1VJj8j-KwC2ODJT7mkJcX1zvExrY4Cvl2` | `Youjo Senki/06 Character Modeling and Reconstruction/02 Character Models/README.md` | 1401 | `b937176e3c85e5b86a88b40e3343b9c66846bbb8d05be5c866464f0eca13e416` | `REFERENCE_DRIVE` |
| `1B9k4mqImDwLNhZz4jrbXi85h5fSsN7dP` | `Youjo Senki/06 Character Modeling and Reconstruction/03 Relationship Registers/README.md` | 1160 | `4149b405131c6752d343badea04ec7f83d1c231e9d328e2292009740fc665bf0` | `REFERENCE_DRIVE` |
| `1Z7UPnnWeFoO2tpXxv1NfvWtcMkPwt63V` | `Youjo Senki/06 Character Modeling and Reconstruction/04 QA and Simulation/README.md` | 1224 | `43a09f35d735cd04edff32e127cc843e0b3d6626ade794687c1c29f6a06263b1` | `REFERENCE_DRIVE` |

Reference-only structural folders:

| Drive ID | Source path | Revision-record SHA-256 | Disposition |
|---|---|---|---|
| `17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH` | `Youjo Senki` | `3b8505bee9a6a629e32a371d939c79e2b8ced0002609fcd857c8254674b7d307` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4` | `Youjo Senki/06 Character Modeling and Reconstruction` | `7acf416b2bb5df2db3421f1efa65920e4dfc070f06daf1cee940793a15f3e8c8` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1Ul_BbZkw9UkSOrDik3hmWVfcK84WWGvW` | `Youjo Senki/06 Character Modeling and Reconstruction/00 Frameworks and Methods` | `6c6d377bdb5d4a3473eb90adc61d3c8b54fe7ff5893e7acd964fb63ed450db8b` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1aDiFqWjWHZ53xX-lBvjMLfA6eN89Z7SZ` | `Youjo Senki/06 Character Modeling and Reconstruction/01 Evidence and Locators` | `4694c2765e4f9a457d6afd8caf46b1752986ef9e30eb6413ac9b86da2e8c2a1c` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1AMNfngVWTSm_4O0XadlJjHWjR8hMw21X` | `Youjo Senki/06 Character Modeling and Reconstruction/02 Character Models` | `ff4dd10ae7d3de408e1ff6004dc1eea461877e65e74fe05a7d7e2aeee51565a3` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1TomsYaw1BmQMRp-JuMils2PeHzl375uo` | `Youjo Senki/06 Character Modeling and Reconstruction/03 Relationship Registers` | `553c8cc09c491a282515fa8e430db5caa8272ce681c23e699985d028dffa6fc1` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1dPqF3RjqawccCi8LA59QVMXsp2KDvH63` | `Youjo Senki/06 Character Modeling and Reconstruction/04 QA and Simulation` | `13b0f0eff615c0875ad759c985e3ecdbf07359ef4233cf72ee22e00a03bd1fa6` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs` | `Youjo Senki/V2 Analysis` | `bdba3156297b9a2761f0ab9301620a77c38098bb8af758e5e8a98ac1faaa2e18` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |

## G5-T07 Legend of the Galactic Heroes analysis

The frozen full-prefix boundary contains 33 selected objects. Twenty reviewed text artifacts totaling 1,212,175 Git bytes materialize after the exact frozen authority-quartet and relative-link transformations. Five ZIP archives, one primary-source pointer, and seven structural folders remain `REFERENCE_DRIVE`; no archive, LFS, primary-source, large-text, rights, or named artifact exception is introduced. Two dedicated current-eligible monographs create Character Index v2 records for Reinhard von Lohengramm and Yang Wen-li, scoped only to the original novels.

| Class | Count | Disposition | Reason |
|---|---:|---|---|
| Reviewed analytical text | 20 | `MIGRATE_TEXT` | Human- and LLM-readable analysis with exact frozen output hashes |
| ZIP archives | 5 | `REFERENCE_DRIVE` | Binary release/source bundles excluded under the standing policy |
| Primary-source pointer | 1 | `REFERENCE_DRIVE` | Deliberately not acquired under the primary-source boundary |
| Structural Drive folders | 7 | `REFERENCE_DRIVE` | Hierarchy/provenance metadata only |

Source-selection receipt SHA-256: `52b54972987e4f5f5eaa78e8f64ccaa768d1f54b34d27f2f807500b420325a63`. Inert materialization receipt SHA-256: `d30dcb4b570458448ab3cc2912e04755564bdd3ed9efbbdc49b38771cddb4b4c`. The final 20-output table has SHA-256 `ef40a427c745624d4dd14b7a4051a3f5427807f4fe50e1cc66b00ebcfd372065`.

Reference-only ordinary artifacts:

| Drive ID | Source path | Bytes | SHA-256 | Reason | Disposition |
|---|---|---:|---|---|---|
| `1QZEzzoL0fFxZwjQKEJNlmMeiravgFeZN` | `Legend of the Galactic Heroes/01 Primary Sources/LOGH_PRIMARY_SOURCE_POINTER.md` | 702 | `1c42cd3f11b692814739466c7b79cfb34f75b4aa04794763532a5b58e7a73b72` | `PRIMARY_SOURCE_POINTER_NOT_ACQUIRED_BY_POLICY` | `REFERENCE_DRIVE` |
| `1cU4EAu8n1VtQ-tDEG6JGGEmYXjXi_mwu` | `Legend of the Galactic Heroes/02 Source Audits/LOGH_Source_Audits_v1.zip` | 14360 | `bac304df6551907eb06b30c954d30b8946e17bd5daff665cfab8703d8c134e22` | `BINARY_ARCHIVE_REFERENCE_DRIVE` | `REFERENCE_DRIVE` |
| `1JGXiu3Hca8mzSEXJo9QekM43gxx2eHKl` | `Legend of the Galactic Heroes/03 Evidence and Crosswalk/LOGH_Evidence_and_Crosswalk_v1.zip` | 238412 | `4c46ab4e0f60af8b8082951680c490802e4b2b62fa9dca743ce77f40b532b344` | `BINARY_ARCHIVE_REFERENCE_DRIVE` | `REFERENCE_DRIVE` |
| `1arKCKniMDN2i5unIN4bpItlC1_gK53F5` | `Legend of the Galactic Heroes/04 Specialist Synthesis/LOGH_Specialist_Synthesis_Documents_v1_compressed.zip` | 339145 | `7dff52bf5a31af93162f516788fbaff406333d89a85bc31da21e2318a7123b74` | `BINARY_ARCHIVE_REFERENCE_DRIVE` | `REFERENCE_DRIVE` |
| `1KUJ2mugYPBTMZQ90xw_t3WG2LDtIzmOz` | `Legend of the Galactic Heroes/05 Final Release/LOGH_Definitive_Full_Series_Synthesis_v1.zip` | 486192 | `56688a1f5f08d9afc1ad6bb982abb2f52c0a9a79406a1b4e3cfcf20878731a73` | `BINARY_ARCHIVE_REFERENCE_DRIVE` | `REFERENCE_DRIVE` |
| `194x1iUfaA-nZzetuqLtyc8wdtnUejyK3` | `Legend of the Galactic Heroes/05 Final Release/LOGH_Final_Release_Controls_v1.zip` | 29885 | `b6f77a883a660f49e84c839112036327282171040e0a643ea1d9cb5222213c34` | `BINARY_ARCHIVE_REFERENCE_DRIVE` | `REFERENCE_DRIVE` |

Reference-only structural folders:

| Drive ID | Source path | Revision-record SHA-256 | Disposition |
|---|---|---|---|
| `1VeLiZ-ZhEIJuWuphla3ndySbYrZKaTP4` | `Legend of the Galactic Heroes` | `c7ee5aef4da6260c961c82dcc1d6652ac4a3d1c597cd728b331e457bb6bff211` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1CRxWpRwQexhj7xZHvHEc3TredmwOkUva` | `Legend of the Galactic Heroes/00 Frameworks` | `0bc4757874a188fb3e17e52742688b547b2ca3a2482b19d9822aa55f631e2821` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1NfMpMzA00jOXoaZdjdYXkIEp_0MYHF-_` | `Legend of the Galactic Heroes/01 Primary Sources` | `6755710d4a2a0026b04191d599ee7878a7fa13d9f2c9ad561ea8951ec02ccd35` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1rDCzTmvlV8kwLdSg-VUpyVw4QaCLR37V` | `Legend of the Galactic Heroes/02 Source Audits` | `5be65d037955f0ac685988c392a3951659ddb4bab8cf5e33e7f8a8817285c6cf` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `157kfSOJFoSsrKSRBNOzd-Owh0stYW-wW` | `Legend of the Galactic Heroes/03 Evidence and Crosswalk` | `a6347e40159ee46cee2bfa3acb3e1e17fc1a4a7dc31dee38a33a03670fb86714` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `1MaljNU7dotPtpKLarFt4MMQZn0252xEG` | `Legend of the Galactic Heroes/04 Specialist Synthesis` | `cc566425923d2704f98b7eaa225c7cab27e979875ecb5669f83d6f3c9eb4d012` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |
| `16tUwWtNZYAGDuEkXKo8GUYB2hrYRrS_J` | `Legend of the Galactic Heroes/05 Final Release` | `111464aaa3c36a395f936b90db458f65f26fd63be50504fe8db4db229c0d98f2` | `REFERENCE_DRIVE_STRUCTURAL_FOLDER` |

## Default exclusions retained

CBZ, ZIP, RAR, 7z, audio, video, scans, source media, large images, binary evidence, databases, model/cache files, executables, generated extraction outputs, superseded Office/PDF originals, large generated corpora, and duplicate release bundles remain `REFERENCE_DRIVE` or `VERIFIED_EXCLUDED` by default. A named owner-approved exception is required before any such object can enter Git; Git LFS does not itself make an out-of-scope artifact eligible.
