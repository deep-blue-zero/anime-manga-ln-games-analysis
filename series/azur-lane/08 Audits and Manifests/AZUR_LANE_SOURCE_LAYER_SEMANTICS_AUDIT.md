# Azur Lane Source-Layer Semantics Audit

## Decision

The physical source layer and presentation capability are separate axes.

- `base_secretary`: records attached to the character's base skin.
- `skin`: every record attached to a non-base skin.
- `special_secretary`: character-bound records from `secretary_special_ship`.
- `live2d_skin`: overlapping capability facet when skin metadata exposes Live2D animations.
- `interactive_skin`: overlapping capability facet when skin metadata exposes a non-empty `ship_l2d_id`.

A non-base record can therefore have `source_layer: skin` and both capability facets. Coverage for the skin corpus is not reduced merely because a skin is interactive.

## St. Louis diagnosis

The former exporter made `interactive_skin` mutually exclusive with `skin`, and treated either `ship_l2d_id` or the generic `l2d_animations` field as proof of interactivity. St. Louis's 44 non-base lines were consequently moved out of the skin bucket and the report incorrectly said that the skin layer was not found.

The hardened rule keeps all 44 records in `skin`. Live2D and interaction are reported independently. This was a categorization failure, not primary-source absence.

## Catch-all audit

The pre-change five-character fixture had five locale records in the `other` category. All were the St. Louis `vote` slot in `ship_skin_words`, one per locale. The slot is now classified as `vote_or_campaign` with interaction register `PUBLIC_CAMPAIGN`.

`other` remains a regression signal. A newly observed non-empty slot must be inventoried and either assigned an operational category or explicitly documented before a release.

The `unlock` field had also been treated as metadata even when it contained source text. It is now retained as base/skin dialogue and classified with Commander-facing secretary material. Identity fields `id`, `voice_key`, and `voice_key_2` remain metadata.

After regeneration, the eight current character corpora contain zero `other` records. The broader targeted discovery scan found 310 locale/table/slot candidate rows outside the current category registry. They are enumerated in `AZUR_LANE_NEW_SOURCE_SURFACE_CANDIDATES.md` rather than silently normalized. Each candidate must be resolved as metadata, mapped to an existing semantic category, assigned a new operational category, or marked as a schema/parser limitation.

This candidate count is a work queue across the whole client surface, not an absence or coverage claim for the eight current characters.

## Status taxonomy

Every audited subsystem uses one of these statuses:

| Status | Operational meaning |
|---|---|
| `PRESENT` | At least one in-scope primary-source record was parsed and linked. |
| `CONFIRMED_ABSENT` | The complete applicable source surface was checked and proves absence. |
| `NOT_APPLICABLE` | The system does not apply to the entity or client context. |
| `NOT_FOUND` | Supported in-scope sources were checked and no matching record was found. |
| `PARSER_UNSUPPORTED` | A known source surface has no parser. |
| `SUPPORTED_PRESENT` | The dedicated parser ran and linked one or more in-scope records. |
| `SUPPORTED_NOT_FOUND` | The dedicated parser ran successfully and found no safely linked record. |
| `SOURCE_REGIONALLY_ABSENT` | The source system is supported but not published in that regional client. |
| `PARSER_ERROR` | The dedicated parser ran but failed on the applicable source. |
| `SCHEMA_VARIANT_UNSUPPORTED` | A source was found but its schema variant is not handled. |
| `IDENTITY_MAPPING_FAILED` | Records exist but cannot be safely linked. |
| `SOURCE_UNAVAILABLE` | The required upstream source or locale is unavailable. |
| `NOT_AUDITED` | The surface has not been checked. |
| `UNKNOWN` | Evidence cannot support a more specific status. |

`CONFIRMED_ABSENT` is intentionally rare. Missing character-memory groups are `NOT_FOUND`, not proof that no relevant material can exist. Dorm3D non-chat and Island non-relationship now use the source-status 2 extension: `SUPPORTED_PRESENT`, `SUPPORTED_NOT_FOUND`, `SOURCE_REGIONALLY_ABSENT`, `IDENTITY_AMBIGUITY`, or `PARSER_ERROR`. `PARSER_UNSUPPORTED` remains valid only for a known surface that still lacks a parser. Parser limitation is never reported as source absence.
