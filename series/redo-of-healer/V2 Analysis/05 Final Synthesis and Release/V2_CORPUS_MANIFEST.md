# Corpus Manifest — Frozen V2 Release

**Series:** 『回復術士のやり直し』 / *Redo of Healer*  
**Scope:** Japanese light novels, Volumes 1–10  
**Release date:** 2026-08-13  
**Release state:** **FROZEN V2**

## Delivery scope

This package contains the eleven audited analytical Markdown documents, reference analytical frameworks, V2 expansion protocol, Phase-6 audit, V1→V2 revision notes, source checksums, and artifact-integrity metadata. The ten Japanese EPUB source novels are **not redistributed**.

## Core analytical documents

| File | Bytes | Whitespace-delimited words | SHA-256 |
|---|---:|---:|---|
| `00_README.md` | 20,348 | 2,797 | `746336e8d59c4d6f10974a2577c7c93e2e99b574b712fad8755dbc6c2c0ee074` |
| `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md` | 49,682 | 7,003 | `34ed358eba75f90de84c47bd7a523309b1ec0e13c49b539eb26199957b30f90d` |
| `02_KEYARU_KEYARGA_CHARACTER_DEEP_DIVE.md` | 54,256 | 8,136 | `b2ac78d6d2284e545e153787e48e936b7f69dcd76e5480ca911fbe087cefed84` |
| `03_PERSONHOOD_HOUSEHOLD_AND_RELATIONSHIPS.md` | 65,641 | 9,671 | `14680ea46351c27c767c475c3944044ee31a0c839b6c09335a5fd4af9082d572` |
| `04_BULLET_ANTAGONISTS_AND_DARK_MIRRORS.md` | 41,792 | 5,892 | `66758a41971b36ff85a625af619a4caec67278c18053430cff98cac872e5b515` |
| `05_POLITICS_INSTITUTIONS_AND_STATECRAFT.md` | 48,692 | 6,778 | `de246e2d086dabc473a3b7c00c4f7e68336d812cec5255c8a85044920c9bd7af` |
| `06_HEALING_POWER_METAPHYSICS_AND_WORLD_SYSTEM.md` | 56,642 | 8,051 | `bbd1458268e233fcd5ce0a7dee86619c0e49ef8d1d398450fe551f25dfc699cf` |
| `07_ETHICS_REVENGE_AUTONOMY_AND_LOVE.md` | 57,782 | 8,392 | `c263ce9d68b74d202a8224d18935e8b47c8e077879a3ebcd42d0d1923ad783ee` |
| `08_NARRATION_LANGUAGE_GENRE_AND_MOTIFS.md` | 34,694 | 4,935 | `4120423b4dface5b7aae4b9bca05bb33ceff4b00d8687001156b795f59ab6d3c` |
| `09_COMPARATIVE_REFERENCE_AND_OPEN_QUESTIONS.md` | 36,395 | 5,244 | `c92cfe90cd0b13d7eab84086755d73e1320528e59c75ca328562f6ad089fd15c` |
| `10_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md` | 52,327 | 7,331 | `9bf72ffb0eeafba9e0a52aaf167f97d1dd2ba42fe5dcb804bd0995561aa82e9e` |

**Core document count:** 11  
**V2 frozen substantive word count:** **74,230**  
**V1 baseline word count:** **37,630**  
**Net V1→V2 change:** **+36,600 words** (97.3% increase)

## Release-support files

| File | Bytes | Whitespace-delimited words | SHA-256 |
|---|---:|---:|---|
| `REFERENCE_ANALYTICAL_METHOD.md` | 23,897 | 3,487 | `957a63378cb8b462b76a1794fc3982d13cad292ad182bc41d5d60eea3391c3c1` |
| `REFERENCE_ARCHITECTURE.md` | 22,366 | 3,236 | `e0e81909b5bfea843b67ff211b4e07d53bd8ac48d04181cd83a1e3b12cc0b94e` |
| `V2_SYNTHESIS_EXPANSION_PROTOCOL.md` | 38,609 | 5,297 | `cce744fd4d459511dc118679352e77dd00a4eb9791ed17c0ea68fa8b9db83792` |
| `PHASE6_CORPUS_WIDE_AUDIT.md` | 18,732 | 2,362 | `460aa8e7806bb89579a3dba3e113b6d180154e768e7ac035abf9dbc77e4a3903` |
| `V1_TO_V2_REVISION_NOTES.md` | 10,778 | 1,392 | `de4c4011f5e61a8080353ac7e09558d543c7dd4cdba5eb94d3141c6703526212` |
| `SOURCE_CHECKSUMS.txt` | 1,548 | 74 | `cfdb61697cd77538ee383ed2f0bc7f984158923b3474d53eac29d722389b7a3b` |

`ARTIFACT_SHA256SUMS.txt` is generated after the above files and does not self-hash. The ZIP archive has a separate external `.sha256` sidecar.

## Source boundary

The supplied Japanese light novels Volumes 1–10 govern the analysis and are frozen by `SOURCE_CHECKSUMS.txt`. Volume 10 narrative scope is `OEBPS/Text/p-001.xhtml` through `p-023.xhtml`; `p-024.xhtml` onward is unrelated promotional sample and excluded.

## Evidence and traceability

Contested claims distinguish **TF**, **SI**, **SP**, and **VJ**. EPUB locators use `V[volume] — [chapter title] — p-XXX.xhtml ¶[normalized paragraph number]`. Phase 6 verified 201 XHTML references and left no missing/out-of-bounds locator failures after correction.

## Provenance

V1 remains a separate historical artifact. Working checkpoints, project transcripts, source extracts, and temporary Drive-status helper files are excluded from this clean release. The V1 baseline above is the count frozen in the V1 corpus manifest.

## Frozen endpoint

> **The first redo is the victim seizing the pen. The second begins only after he discovers that the other people on the page are also authors of lives he does not own.**
