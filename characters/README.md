# Character analytical discovery

`characters/registry.jsonl` is the canonical structured source for the generated root `CHARACTER_ANALYSIS_INDEX.md`. One nonblank JSONL line is one schema-v2 **analysis subject**. The Markdown index is a deterministic discovery view and must never be edited as independent authority.

The production discovery registry contains YonaiP, the U149 anime Producer; seven reviewed Maebashi Witches anime subjects: Azu, Choco, Eiko, Keroppe, Kyouka, Mai, and Yuina; reviewed Paragon and Renegade Commander Shepard player-archetype subjects from the Mass Effect comparative study; the reviewed Genshin Impact game subject Furina; nine reviewed Cinderella Girls mobile-game subjects: Futaba Anzu, Hayami Kanade, Hisakawa Nagi, Hojo Karen, Kanzaki Ranko, Kobayakawa Sae, Ninomiya Asuka, Nitta Minami, and Takagaki Kaede; and eleven reviewed Blue Archive game subjects: Aru, Ayane, Haruka, Hifumi, Hoshino, Kayoko, Mutsuki, Nonomi, player-variable Sensei, Serika, and Shiroko. Reconstruction capability is specified separately and is deliberately not populated.

## What this registry answers

The discovery layer answers:

> Where does this repository contain reviewed, substantial analysis of this precisely scoped character subject?

It does not answer whether a character merely appears in source material, and it does not assign reconstruction or simulation capability. Cast lists, transcripts, source-text appearances, name counts, and incidental references do not qualify a record for inclusion.

Substantive monographs and analyses remain in their canonical homes:

```text
series-specific analysis                    -> series/<stable-slug>/
cross-series or taxonomy study              -> studies/<stable-slug>/
character discovery metadata                -> characters/registry.jsonl
future reconstruction capability metadata   -> characters/reconstruction_capabilities.jsonl
```

The `characters/` directory is global metadata and specification infrastructure, not a parallel home for analytical prose.

## Entity and analysis-subject identity

`character_entity_id` identifies the stable underlying character. `analysis_subject_id` identifies the exact continuity, incarnation, route, temporal state, player archetype, or approved composite being analyzed. Multiple subject rows may share one entity.

```text
character_entity_id = <namespace>:<entity-slug>
analysis_subject_id = <namespace>:<entity-slug>@<subject-slug>
```

All ontology IDs are lower-case ASCII. If `franchise_id` is non-null, it supplies the namespace; otherwise `series_id` does. The portion of `analysis_subject_id` before `@` must exactly equal `character_entity_id`.

The subject kinds are:

```text
SINGLE_CONTINUITY
ADAPTATION_INCARNATION
ALTERNATE_CONTINUITY
ROUTE_VARIANT
TEMPORAL_STATE
PLAYER_ARCHETYPE
COMPOSITE_MODEL
```

Temporary moods, costumes, ordinary chapter boundaries, and normal character development do not automatically create new subjects. Create a subject only when the evidence or analytical constraints require a stable, separately scoped model.

## Composite subjects

`COMPOSITE_MODEL` is an analytical aggregation, never a synthetic continuity.

- Its stored `continuity_id`, `incarnation_id`, and `state_id` are `null`.
- It has at least two unique `component_subject_ids`; non-composites prohibit that property.
- Every component shares the composite's `character_entity_id`.
- Recursive expansion must end in at least two distinct non-composite leaves without cycles, redundant branches, or duplicate leaf reachability.
- Every leaf has the same `series_id`, and the composite owns that same series. Cross-series composites are prohibited in schema v2, even when the analysis lives under `studies/`.
- `effective_continuity_ids` is derived from leaf continuities, deduplicated, and bytewise sorted. It is never stored.
- A composite does not inherit component aliases, evidence, dimensions, coverage, materialization, curation, or inclusion. It needs its own reviewed evidence.
- Composite coverage names one transitive leaf in `component_subject_id` and uses that leaf's continuity. Multi-leaf coverage uses multiple entries.

## Alias scope

The v1 `aliases` field is replaced by two required arrays using the same closed alias object:

- `entity_aliases` contains names intended to identify the underlying entity across all its subjects.
- `subject_aliases` contains adaptation-, continuity-, route-, incarnation-, state-, or archetype-specific names.

An alias object contains `value`, lower-case `language`, controlled `kind`, `ambiguous`, and nullable `note`. Values and notes must be strict UTF-8 and Unicode-15.0.0 NFC, contain no controls, and have no leading or trailing Unicode whitespace.

Within each scope, alias identity is the tuple `(folded NFC value, lower-case language, kind)`. The same normalized key cannot occur in both scopes of one row. `ambiguous` and `note` do not make an otherwise duplicate alias distinct.

Rows sharing one `character_entity_id` must agree exactly on `preferred_name`, the complete canonicalized `entity_aliases` set, `franchise_id`, and namespace. `subject_aliases` is deliberately row-local and is excluded from entity-drift checks.

## Repository materialization and curation

The durable repository field is:

```text
materialization_status = NOT_PRESENT | PRESENT_UNREVIEWED | PRESENT_REVIEWED
```

It is recomputed against the selected prospective Git index, tree, or commit:

- `NOT_PRESENT`: every declared evidence target is absent; the evidence array may be empty.
- `PRESENT_UNREVIEWED`: every target is present and at least one evidence item is `UNREVIEWED`.
- `PRESENT_REVIEWED`: every target is present and every evidence item is `REVIEWED`.
- Mixed present/absent evidence is invalid in the canonical registry and remains transient migration-ledger state.

Presence means an exact-case, tracked, regular, non-LFS-pointer blob. A worktree-only file, directory, symlink, submodule, unsafe path, or case-insensitive near-match is not present for this ontology.

Migration tooling may map old transient labels only after recomputation:

```text
NOT_YET_MIGRATED    -> NOT_PRESENT
MIGRATED_UNREVIEWED -> PRESENT_UNREVIEWED
MIGRATED_REVIEWED   -> PRESENT_REVIEWED
```

The canonical registry never stores `migration_status`.

`curation_status` is `CANDIDATE`, `INCLUDED`, or `EXCLUDED_REVIEWED`. Only `INCLUDED` rows appear in the generated index. Inclusion requires:

- `PRESENT_REVIEWED`;
- at least one reviewed, current-evidence-eligible target;
- `DEDICATED` or `DISTRIBUTED_SUBSTANTIAL` inclusion basis;
- support for every declared analytical dimension; and
- coverage references that resolve to reviewed evidence in the same row.

## Evidence and analytical coverage

Every evidence object has a stable local `evidence_id`, an exact repository path, human-readable label, optional verified anchor, review state, controlled analytical dimensions, and nullable provenance note. An omitted anchor has the same digest projection as `null`; migration tooling must not invent one. A future reconstruction reference is the exact concatenation:

```text
<analysis_subject_id>#<evidence_id>
```

`provenance_note` is informational and cannot override authority metadata. Migration tooling must not invent anchors. If heading-fragment equivalence cannot be verified robustly, only file existence and anchor syntax may be claimed as validated.

The discovery dimensions are fixed for schema v2:

```text
BEHAVIOR
PSYCHOLOGY
SPEECH
ETHICS
RELATIONSHIPS
IDEOLOGY
DECISION_MAKING
```

`analytical_coverage` describes where substantial analysis exists, not where the character appears. A coverage item is a structured `RANGE`, `DISCRETE`, or `DESCRIPTIVE` scope over an episode, chapter, volume, arc, route, quest, story chapter, or other bounded unit. Gaps use multiple entries rather than a misleading continuous range.

## Artifact authority

Present Markdown evidence is current-eligible only when its first byte begins a valid first YAML front-matter block containing the complete quartet:

```yaml
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
```

The exact status vocabulary is:

```text
canonical
active_provisional
superseded
historical_legacy
```

`canonical` and `active_provisional` are current-eligible only with a false veto flag, no successor, and a valid bounded supersession component. Provisional evidence remains visibly marked provisional. `superseded` and `historical_legacy` never qualify current evidence and require the veto flag to be true. Supersession pointers are reciprocal exact-case POSIX paths and form an acyclic predecessor-to-successor graph with exactly one current sink for a referenced superseded lineage.

If none of the four fields exists, the present target is `UNCLASSIFIED_LEGACY`: useful as provenance but ineligible for `INCLUDED` or reviewed reconstruction. A partial, malformed, contradictory, dangling, or cyclic authority surface is invalid, not legacy. A missing target is `MISSING`, not unclassified. Free text, filenames, timestamps, and recency cannot override these outcomes, and a validator never silently substitutes a successor for the named evidence path.

## Deterministic generation

All v2 implementations use canonicalization profile `CHARACTER_INDEX_V2_C14N_1`:

- strict UTF-8;
- Unicode Character Database 15.0.0;
- stored strings already in NFC;
- full default, non-Turkic case folding for comparison only;
- no locale-sensitive sorting or implicit trimming; and
- UTF-8 without BOM and LF-only generated output.

Define `fold(s) = NFC(full-default-case-fold(NFC(s)))` and `sort_key(s) = (UTF8(fold(s)), UTF8(NFC(s)))`. Character rows sort by preferred name, subject label, then ASCII subject ID. Alias, evidence, coverage, and diagnostic ordering is fixed in the schema specification and validator. A mismatched Unicode-data version fails; it is never accepted silently.

## Illustrative identity excerpts

These deliberately incomplete excerpts explain identity only. They are not valid full registry rows and must not be copied into `registry.jsonl` without all required schema-v2 fields and review.

### 1. Ordinary single-continuity anime subject

```json
{
  "character_entity_id": "example:akari",
  "analysis_subject_id": "example:akari@anime",
  "series_id": "example",
  "franchise_id": null,
  "continuity_id": "anime",
  "incarnation_id": null,
  "state_id": null,
  "subject_kind": "SINGLE_CONTINUITY"
}
```

### 2. One entity with light-novel and anime subjects

```json
[
  {
    "character_entity_id": "example:mei",
    "analysis_subject_id": "example:mei@light-novel",
    "continuity_id": "light-novel",
    "incarnation_id": null,
    "subject_kind": "SINGLE_CONTINUITY"
  },
  {
    "character_entity_id": "example:mei",
    "analysis_subject_id": "example:mei@anime",
    "continuity_id": "anime",
    "incarnation_id": "television-adaptation",
    "subject_kind": "ADAPTATION_INCARNATION"
  }
]
```

Both rows share the same `preferred_name`, entity aliases, franchise, and namespace. Adaptation-only names belong in the anime row's `subject_aliases`.

### 3. Alternate continuity

```json
{
  "character_entity_id": "example:rin",
  "analysis_subject_id": "example:rin@reboot",
  "continuity_id": "reboot",
  "incarnation_id": null,
  "state_id": null,
  "subject_kind": "ALTERNATE_CONTINUITY"
}
```

### 4. Player-variable protagonist

```json
{
  "character_entity_id": "example:protagonist",
  "analysis_subject_id": "example:protagonist@player-variable",
  "continuity_id": "game",
  "incarnation_id": null,
  "state_id": "player-variable",
  "subject_kind": "PLAYER_ARCHETYPE"
}
```

### 5. Paragon/Renegade-style analytical archetypes

```json
[
  {
    "character_entity_id": "mass-effect:commander-shepard",
    "analysis_subject_id": "mass-effect:commander-shepard@paragon-player-archetype",
    "continuity_id": "mass-effect-trilogy-games",
    "state_id": "paragon",
    "subject_kind": "PLAYER_ARCHETYPE"
  },
  {
    "character_entity_id": "mass-effect:commander-shepard",
    "analysis_subject_id": "mass-effect:commander-shepard@renegade-player-archetype",
    "continuity_id": "mass-effect-trilogy-games",
    "state_id": "renegade",
    "subject_kind": "PLAYER_ARCHETYPE"
  }
]
```

These identifiers now mirror the complete reviewed records in `registry.jsonl`; the records point to the Mass Effect comparative-study monographs and remain nonauthoritative before G8.

### 6. Same-series composite

```json
{
  "character_entity_id": "example:aya",
  "analysis_subject_id": "example:aya@cross-adaptation",
  "series_id": "example",
  "continuity_id": null,
  "incarnation_id": null,
  "state_id": null,
  "subject_kind": "COMPOSITE_MODEL",
  "component_subject_ids": [
    "example:aya@anime",
    "example:aya@light-novel"
  ]
}
```

If the two leaves have continuities `anime` and `light-novel`, the derived effective list is `["anime", "light-novel"]`. It is not stored. The composite must have its own evidence, and both leaves and the composite must have `series_id: example`.

## Separate reconstruction layer

Discovery says where substantial analysis exists. Reconstruction capability says what extrapolations an exact, commit-bound evidence set can responsibly support. The latter is defined in `RECONSTRUCTION_CAPABILITY_SPEC.md` and its schema, but these production files do not yet exist:

```text
characters/reconstruction_capabilities.jsonl
characters/CHARACTER_RECONSTRUCTION_INDEX.md
```

Creating or populating them, assigning grades, or scoring characters requires a separate owner-reviewed assessment phase. Migration does not perform reconstruction assessment.
