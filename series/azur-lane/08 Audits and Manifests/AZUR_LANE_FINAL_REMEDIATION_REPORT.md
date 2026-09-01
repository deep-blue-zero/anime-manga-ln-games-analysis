# Azur Lane Final Remediation Report

Generated: `2026-08-23T04:36:09.441495Z`

## Social entity resolution

Raw `0` is subsystem-polymorphic: type-1 Fleet Chat and Dorm3D option rows are the Commander/player role; type-2 Juustagram posts are the `Port News` system account. Fleet group keys `101` and `107` are channel context, not ship participants. Raw IDs remain preserved in normalized messages and evidence provenance.

Unresolved normalized social entities remaining: **0**. Taihou raw-zero regression: **PASS**.

## Alignment-gap interpretation

The denominator is sequence/slot/message-level stable-key candidates, so long stories and large regional script rewrites can produce hundreds or thousands of gap rows.

Importance weighting separates substantive narrative/dialogue/social rows from type-4/5 auxiliary control payloads; an absolute gap count is not a literary-divergence measure.

No dominant parser failure was identified in the current eight-character surface. IDENTITY_MAPPING_GAP/UNKNOWN remain explicit where deterministic evidence is insufficient.

Warning format changed from a bare absolute count to `value`, `denominator`, `rate`, documented threshold, dominant source family, dominant missing locale, and dominant reason. readiness-2.1.0 replaces the all-or-nothing fully-aligned fraction with importance-weighted locale presence, reducing over-penalization of harmless auxiliary/asymmetric records.

| Character | Candidates | Gaps | Gap rate | Weighted coverage | Dominant family | Missing direction | Cause | Score delta |
|---|---:|---:|---:|---:|---|---|---|---:|
| ATAGO_30312 | 1384 | 252 | 18.21% | 86.74% | narrative | missing_CN | REGIONAL_CONTENT_ABSENCE | +0.74 |
| BALTIMORE_10316 | 3869 | 309 | 7.99% | 97.50% | narrative | missing_KR | STRUCTURAL_REWRITE | +0.83 |
| ENTERPRISE_10706 | 13426 | 2454 | 18.28% | 90.27% | narrative | missing_CN | STRUCTURAL_REWRITE | +1.28 |
| KIRISHIMA_30404 | 772 | 25 | 3.24% | 98.09% | narrative | missing_KR | STRUCTURAL_REWRITE | +0.20 |
| NAGATO_30505 | 7767 | 1760 | 22.66% | 91.67% | narrative | missing_KR | STRUCTURAL_REWRITE | +2.15 |
| ST_LOUIS_10213 | 980 | 171 | 17.45% | 90.05% | narrative | missing_CN | STRUCTURAL_REWRITE | +1.13 |
| TAIHOU_30707 | 2541 | 666 | 26.21% | 92.76% | narrative | missing_EN | STRUCTURAL_REWRITE | +2.84 |
| TAKAO_30311 | 3369 | 202 | 6.00% | 96.69% | narrative | missing_TW | STRUCTURAL_REWRITE | +0.40 |

## Corpus archival completion

The existing `Mobile games/Azur_Lane/` directory remains the sole canonical title root. `CURRENT_STATE_AND_CORPUS_MAP.md` is the single active first-read entrypoint. It links the source inventory/lock, schema discovery, extraction and pipeline methods, equivalence and hardening audits, this remediation set, the machine audit, validation summary, and `manifests/AZUR_LANE_BUILD_MANIFEST.json`.

The canonical `MANGA_ANIME_DRIVE_INDEX.md` is an external Drive artifact, not a file in this local title workspace. Drive publication must verify or update its Azur Lane route rather than infer that the global index does not exist.

## Eight-character regression results

| Character | Grade/score | Required regression result | Warnings retained |
|---|---|---|---|
| TAIHOU_30707 | A / 86.89 | Commander is normalized; no analyst-facing raw-zero entity remains; human artifacts intact. | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| ENTERPRISE_10706 | B / 72.48 | Large gap count is decomposed; the unmerged identity alternative remains explicit. | COMMANDER_HEAVY, IDENTITY_AMBIGUITY, MANY_UNALIGNED_RECORDS |
| BALTIMORE_10316 | A / 82.91 | Frozen evidence counts and complete human-readable artifact set preserved. | COMMANDER_HEAVY |
| ATAGO_30312 | A / 83.83 | Frozen evidence counts and relationship/category separation preserved. | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| ST_LOUIS_10213 | C / 57.3 | SKIN_HEAVY retained; skin and interactive-skin facet semantics remain distinct. | COMMANDER_HEAVY, SKIN_HEAVY, MANY_UNALIGNED_RECORDS |
| TAKAO_30311 | A / 89.21 | A-tier result remains explainable; high weighted regional coverage and readable artifacts preserved. | COMMANDER_HEAVY |
| NAGATO_30505 | B / 71.92 | Story-heavy evidence is preserved and its large alignment surface is decomposed. | COMMANDER_HEAVY, MANY_UNALIGNED_RECORDS |
| KIRISHIMA_30404 | C / 52.73 | Current sparse/moderate evidence profile and all required artifact layers preserved. | COMMANDER_HEAVY |

## Validation

- Automated tests: **PASS** (38 run; 0 failures; 0 errors).
- Provenance: **PASS** (126307 records checked).
- Character artifact hashes: **PASS** (1077 hashes checked).

## Remaining known limitations

- Dorm3D non-chat and Island non-relationship parsers are implemented; characters without linked records are `SUPPORTED_NOT_FOUND`.
- Authoritative JP client audio is acquired and hash-archived; per-character `AUDIO_PARTIAL` states preserve unresolved text/audio joins for later review.
- Structural gap reasons are deterministic triage, not claims of censorship or release lag.
- Community sources remain discovery/completeness validation only.

## Final recommendation

**READY_WITH_DOCUMENTED_LIMITATIONS.** The corpus is provenance-complete and suitable for character synthesis across the implemented narrative/dialogue/social surfaces. The explicit explicit residual JP audio mapping gaps and candidate-only regional interpretation prevent a stronger unqualified readiness claim.
