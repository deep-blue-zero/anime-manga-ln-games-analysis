# Azur Lane Alignment Gap Audit

Generated: `2026-08-22T22:42:24.783522Z`

## Findings

- The denominator is sequence/slot/message-level stable-key candidates, so long stories and large regional script rewrites can produce hundreds or thousands of gap rows.
- Importance weighting separates substantive narrative/dialogue/social rows from type-4/5 auxiliary control payloads; an absolute gap count is not a literary-divergence measure.
- No dominant parser failure was identified in the current eight-character surface. IDENTITY_MAPPING_GAP/UNKNOWN remain explicit where deterministic evidence is insufficient.
- readiness-2.1.0 replaces the all-or-nothing fully-aligned fraction with importance-weighted locale presence, reducing over-penalization of harmless auxiliary/asymmetric records.

| Character | Candidates | Full | Partial | Gaps | Gap rate | Important-gap rate | Weighted coverage | Dominant family | Dominant missing | Dominant reason | Score delta |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|
| ATAGO_30312 | 1384 | 1132 | 72 | 252 | 18.21% | 18.46% | 86.74% | narrative | missing_CN | REGIONAL_CONTENT_ABSENCE | +0.74 |
| BALTIMORE_10316 | 3869 | 3560 | 308 | 309 | 7.99% | 8.03% | 97.50% | narrative | missing_KR | STRUCTURAL_REWRITE | +0.83 |
| ENTERPRISE_10706 | 13426 | 10972 | 1763 | 2454 | 18.28% | 18.32% | 90.27% | narrative | missing_CN | STRUCTURAL_REWRITE | +1.28 |
| KIRISHIMA_30404 | 772 | 747 | 25 | 25 | 3.24% | 3.29% | 98.09% | narrative | missing_KR | STRUCTURAL_REWRITE | +0.20 |
| NAGATO_30505 | 7767 | 6007 | 1536 | 1760 | 22.66% | 22.71% | 91.67% | narrative | missing_KR | STRUCTURAL_REWRITE | +2.15 |
| ST_LOUIS_10213 | 980 | 809 | 86 | 171 | 17.45% | 17.70% | 90.05% | narrative | missing_CN | STRUCTURAL_REWRITE | +1.13 |
| TAIHOU_30707 | 2541 | 1875 | 655 | 666 | 26.21% | 26.46% | 92.76% | narrative | missing_EN | STRUCTURAL_REWRITE | +2.84 |
| TAKAO_30311 | 3369 | 3167 | 175 | 202 | 6.00% | 6.04% | 96.69% | narrative | missing_TW | STRUCTURAL_REWRITE | +0.40 |

## Aggregate causes

- Source-family gap rows: `{'narrative': 5811, 'character_text': 18, 'social': 10, 'other': 0}`
- Missing-locale counts: `{'missing_CN': 3052, 'missing_EN': 2303, 'missing_JP': 1278, 'missing_KR': 3605, 'missing_TW': 2936}`
- Deterministic reason counts: `{'REGIONAL_CONTENT_ABSENCE': 1234, 'STRUCTURAL_REWRITE': 4605}`
- Importance distribution: `{'high': 5839}`

`RELEASE_LAG` is not assigned: the source lock does not contain sufficient per-record release chronology. These rows are candidates for review, not censorship labels.
