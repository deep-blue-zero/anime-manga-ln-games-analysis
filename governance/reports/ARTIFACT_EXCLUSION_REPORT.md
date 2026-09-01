# Artifact Exclusion Report

## Scope

This report covers the integrated U149 first tranche, the P02 large-structured-text boundary tranche, the partial P03 native-document/native-sheet tranche, the P04 ZIP/reference boundary, G5-T01 Maebashi Witches V1, G5-T02 Mass Effect comparative media, G5-T03 Genshin Impact Furina V1, and G5-T04 Cinderella Girls mobile-game analysis. It is not the final archive-wide exclusion review.

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

P04 records six archive identities totaling 814,501 bytes and materializes none of them. The frozen source slice has SHA-256 `4c2130e9608ec85ea9b1ca02fe5b0ed4c37f6108979eb950c9f87e12308a6c04`; the validated reference-only receipt has SHA-256 `a802b0765d51109b4c2fa1bc18a78d42e772589073e522f706aa49d8b9ffbce4`; and the representation slice is `null`. The two same-logical-path Temari objects and two same-logical-path Lilja objects remain distinct by Drive file ID, byte length, and SHA-256. No archive bytes, extracted members, LFS objects, or Gakuen Idolmaster analysis tree are tracked.

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

## Default exclusions retained

CBZ, ZIP, RAR, 7z, audio, video, scans, source media, large images, binary evidence, databases, model/cache files, executables, generated extraction outputs, superseded Office/PDF originals, large generated corpora, and duplicate release bundles remain `REFERENCE_DRIVE` or `VERIFIED_EXCLUDED` by default. A named owner-approved exception is required before any such object can enter Git; Git LFS does not itself make an out-of-scope artifact eligible.
