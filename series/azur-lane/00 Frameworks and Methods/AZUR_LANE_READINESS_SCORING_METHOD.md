# Azur Lane Readiness Scoring Method

Model version: `readiness-2.1.0`.

The score measures evidence amount and context diversity. It does not measure popularity, literary quality, canon importance, or whether a character is well written.

| Component | Maximum | Deterministic basis |
|---|---:|---|
| Narrative depth | 25 | Direct-presence story count, saturated at 40 scenes |
| Dedicated story depth | 15 | Chapters in complete character-memory groups, saturated at seven |
| Dialogue breadth | 15 | Distinct semantic dialogue categories, saturated at eight |
| Social-context diversity | 10 | Distinct parsed social systems, saturated at four |
| Relationship-context diversity | 10 | Presence of direct, explicit, social, and Commander-facing categories |
| Regional coverage | 15 | Importance-weighted locale presence across relevant stable alignments |
| Source-system diversity | 10 | Fraction of supported audited subsystems with linked records |

Grades are A (80–100), B (60–79.99), C (40–59.99), D (20–39.99), and E (below 20). Every component is exposed in `SOURCE_COVERAGE.json`.

## Regional weighting change in 2.1.0

The earlier 2.0.0 regional component counted only records present in every requested locale. Version 2.1.0 instead gives each alignment credit for the fraction of requested locales in which it is present, weighted by analytical importance:

- high (`3.0`): narrative; secretary, affinity, oath, relationship-specific, and special-secretary dialogue; substantive social text;
- medium (`1.5`): other character dialogue, including combat/profile/campaign surfaces;
- low (`0.25`): auxiliary/control records and unsupported residual categories.

This formula prevents type-4/5 routing payloads and presentation-only asymmetry from dominating character readiness while retaining stronger penalties for missing narrative and character-defining dialogue.

Composition warnings report evidence skew separately from the score. `MANY_UNALIGNED_RECORDS` includes `value`, `denominator`, `rate`, threshold, dominant source family, dominant missing locale, and deterministic reason. It triggers when the structural-gap rate is at least 10% and either the high-importance gap rate is at least 5% or narrative gaps are at least 10%. Warnings are descriptive and never alter normalized source text.

## JP performed-voice readiness

JP performed-voice collection is intentionally separate from `readiness-2.1.0`. Source augmentation does not change existing character scores. `JP_VOICE_PERFORMANCE_READINESS` reports one of `AUDIO_READY`, `AUDIO_PARTIAL`, `AUDIO_SPARSE`, `AUDIO_NOT_FOUND`, or `AUDIO_MAPPING_BLOCKED` from objective acquisition and mapping coverage only.
