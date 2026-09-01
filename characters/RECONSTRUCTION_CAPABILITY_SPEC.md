# Character Reconstruction Capability Specification

- Status: `SPECIFICATION_ONLY_NOT_POPULATED`
- Discovery schema: `../governance/schemas/character-analysis-index.schema.json`
- Capability schema: `../governance/schemas/character-reconstruction-capability.schema.json`
- Canonicalization profile: `CHARACTER_INDEX_V2_C14N_1`
- Evidence-set algorithm: `CHARACTER_EVIDENCE_SET_V1`

## Purpose and boundary

The character discovery registry answers:

> Where is reviewed, substantial analysis of this precisely scoped subject?

The future reconstruction capability registry answers:

> What kinds of extrapolation can this exact, commit-bound evidence set responsibly support?

These are related but distinct ontologies. Discovery never implies reconstruction readiness. Migration never assigns capability grades.

This hardening phase creates only this specification and the closed JSON Schema. It deliberately does not create or populate:

```text
characters/reconstruction_capabilities.jsonl
characters/CHARACTER_RECONSTRUCTION_INDEX.md
```

Creating either production file, assessing a character, or publishing an A-E grade requires a separately authorized, owner-reviewed assessment phase.

## Record identity and discovery binding

One future capability record is one assessment of one `analysis_subject_id`. It contains:

```text
schema_version
assessment_id
character_entity_id
analysis_subject_id
assessment_status
assessment_scope
overall_tier
dimensions
scenario_readiness
known_limits
evidence_refs
stale_reason
supersedes_assessment_id
superseded_by_assessment_id
```

The subject must resolve to exactly one discovery row. The entity ID must equal that row's entity ID, and continuity/incarnation/state scope must agree with the discovery subject. An assessment cannot broaden its subject implicitly.

### Composite subjects

A `COMPOSITE_MODEL` remains a same-series analytical aggregation, not a continuity:

- `assessment_scope.continuity_id`, `incarnation_id`, and `state_id` are `null`;
- `assessment_scope.component_subject_ids` is required and exactly equals the canonical component set on the composite discovery row;
- effective continuity is recursively derived from non-composite leaves and is never stored;
- cross-series composites remain prohibited;
- component membership does not inherit evidence; and
- every capability evidence reference still names reviewed evidence curated directly on the composite's own discovery row.

A leaf-subject, unrelated-subject, or cross-series evidence reference fails even when it names a component of the assessed composite.

## Assessment scope

`assessment_scope` is closed and binds:

- continuity, incarnation, and state;
- the exact component set for a composite;
- a human-readable source boundary;
- a temporal boundary, or `null` only when genuinely inapplicable;
- a full lower-case Git commit object ID;
- `evidence_set_algorithm: CHARACTER_EVIDENCE_SET_V1`;
- a lower-case 64-hex `evidence_set_sha256`;
- an assessment method; and
- an assessment-method version.

`basis_commit` matches either 40 or 64 lower-case hexadecimal characters, according to the repository object format. It must resolve directly to a commit object. Abbreviations, ref names, annotated-tag objects, trees, blobs, uppercase hashes, unavailable shallow history, and object-format length mismatches fail.

The method describes the controlled assessment procedure. A model or tool version may be recorded as procedural provenance, but no language model is itself treated as the character's evidentiary capability.

## Assessment status

```text
UNASSESSED
CANDIDATE
REVIEWED
STALE
SUPERSEDED
```

- `UNASSESSED` uses `NOT_ASSESSED` throughout, has no evidence references or known-limit claims, and uses the deterministic empty evidence-set hash.
- `CANDIDATE` may contain provisional grades but is visibly nonauthoritative and has a nonempty evidence union.
- `REVIEWED` has a human-reviewed A-E overall tier, a complete scope, supported assessed claims, and evidence current-eligible at its basis commit.
- `STALE` preserves its historical grades, basis, and digest and requires a nonempty `stale_reason`.
- `SUPERSEDED` preserves provenance and requires `superseded_by_assessment_id`.

`supersedes_assessment_id` and `superseded_by_assessment_id` are distinct nullable links. Present counterpart records must link reciprocally, resolve within the same entity and compatible subject scope, and form an acyclic graph. A successor is never substituted silently for the assessment or evidence path named by a record.

## Human capability judgments

The overall tier is categorical and never computed mechanically from dimension grades:

```text
A = reconstruction-grade for disciplined novel-scenario work
B = strong inferential model with explicit bounded uncertainty
C = specialist-supported interpretation without unconstrained simulation support
D = substantial distributed evidence without a strong operational model
E = limited/local evidence suitable for bounded canon questions only
```

Plus/minus grades and numeric pseudo-scores are not part of schema v1.

Every assessment contains exactly one structured claim for each dimension:

```text
PSYCHOLOGICAL_MODEL
LONGITUDINAL_STATE
VOICE_REGISTER
MUNDANE_BEHAVIOR
RELATIONSHIP_CONDITIONING
INTERIORITY
CONFLICT_BEHAVIOR
ETHICAL_DELIBERATION
HUMOR_PLAY
SOURCE_COMPLETENESS
NEGATIVE_EVIDENCE
TEMPORAL_SPECIFICITY
```

Each dimension uses `A | B | C | D | E | NOT_ASSESSED`, its own evidence references, and a nullable note. A-E requires evidence; `NOT_ASSESSED` prohibits it. `NEGATIVE_EVIDENCE` means affirmative evidence of a limitation or contradiction, not merely missing evidence.

Every assessment also contains exactly one structured readiness claim for:

```text
DIALOGUE
CROSS_SCENARIO
MUNDANE_SOCIAL
ETHICAL_DELIBERATION
ROMANCE_RELATIONSHIP
PROFESSIONAL_CONTEXT
```

The states are:

```text
READY | CONDITIONAL | NOT_READY | NOT_ASSESSED
```

An assessed state requires evidence. `CONDITIONAL` requires a nonempty `conditions` array; other states prohibit that field. `CROSS_SCENARIO` is a bounded counterfactual, crossover, or materially novel context—not permission for unconstrained role-play. An assessed cross-scenario claim additionally identifies assumed chronology, interlocutor relationship, and setting constraints in `cross_scenario_scope`.

## Known limits

Each known-limit object contains:

```text
limit_id
statement
support_kind
evidence_refs
```

`EVIDENCE_BACKED` requires evidence and contributes those references to the assessment union. `EVIDENCE_GAP` requires an empty reference array, is visibly a gap rather than negative evidence, and contributes nothing to the union. Limit IDs are unique within the assessment.

## Exact evidence references and claim union

An evidence reference is one ASCII string matching:

```regex
^[a-z0-9][a-z0-9-]*:[a-z0-9][a-z0-9-]*@[a-z0-9][a-z0-9-]*#[a-z0-9][a-z0-9-]*$
```

It is the literal concatenation:

```text
<analysis_subject_id>#<evidence_id>
```

It contains exactly one `#`. Parse once at that byte. URL decoding, Unicode normalization, alternate separators, and multiple-fragment interpretation are prohibited.

Every reference resolves to a `REVIEWED` discovery evidence item whose row's `analysis_subject_id` exactly equals the assessment subject. Candidate leads, unreviewed evidence, component-leaf evidence, and unrelated subjects do not qualify.

The top-level `evidence_refs` array:

1. is unique;
2. is ordered by parsed subject ID and then evidence ID under the frozen ordering below;
3. equals exactly the canonical set union of references on every assessed dimension, assessed scenario, and `EVIDENCE_BACKED` known limit;
4. contains no unclaimed extra reference and omits no claim reference; and
5. is the exact set hashed by `evidence_set_sha256`.

`CANDIDATE` and `REVIEWED` unions are nonempty. `UNASSESSED` has the empty union. The overall tier is supported by the same union; there is no separate hidden evidence set.

## Machine-readable artifact authority

Human review and artifact authority are independent. A `REVIEWED` evidence item is current-eligible only when its exact committed target and bounded supersession graph qualify.

### Recognized front matter

For Markdown, the opening `---` of the first YAML front-matter block must be the first bytes of the strict UTF-8, BOM-free, LF-normalized committed file. The recognized top-level quartet is:

```yaml
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
```

The four exact lower-case status values are:

```text
canonical
active_provisional
superseded
historical_legacy
```

`supersedes` and `superseded_by` are unique arrays of exact-case POSIX repository-relative artifact paths. Nonempty paths must be safe and resolve to tracked regular blobs in the selected snapshot. The veto is a real boolean. Duplicate YAML keys, aliases, anchors, merge keys, custom tags, malformed fences, wrong types, strings standing in for booleans, and partial quartets fail.

No status is inferred from a filename, directory, timestamp, prose statement, provenance note, adjacent file, Drive copy, or apparent recency.

### Bounded supersession graph

The validator indexes only first front-matter blocks of tracked regular Markdown blobs under `series/` and `studies/`. It normalizes both pointer directions to predecessor -> successor:

- if successor A lists predecessor B in `supersedes`, create B -> A;
- if predecessor B lists successor A in `superseded_by`, create B -> A.

Every edge must be reciprocal and exact-case. The graph is acyclic. A referenced superseded lineage's weakly connected component terminates in exactly one unsuperseded current sink. Zero or multiple current sinks, one-sided edges, dangling paths, case mismatches, self-links, and cycles fail closed.

A recognized incoming `supersedes` declaration creates an outgoing edge for its named predecessor immediately, so the predecessor is noncurrent even before its reciprocal field is repaired; the graph nevertheless remains invalid until reciprocal. A validator never swaps in the successor for the evidence path actually named.

### Classification

| Status | Required consistent state | Current evidence |
|---|---|---|
| `canonical` | veto false, `superseded_by` empty, no outgoing successor edge | Eligible after separate review |
| `active_provisional` | veto false, `superseded_by` empty, no outgoing successor edge | Eligible after separate review, always labeled provisional |
| `superseded` | veto true, `superseded_by` nonempty | Never |
| `historical_legacy` | veto true; successor optional but valid when present | Never |

`do_not_use_as_current_authority: true` is an absolute veto. Contradictory status/flag pairs fail rather than being downgraded.

If none of the quartet is present on a present target, classify it `UNCLASSIFIED_LEGACY`. It may remain provenance but cannot support `INCLUDED` discovery or a current `REVIEWED` reconstruction assessment. If any recognized field is present but the quartet is incomplete or invalid, validation fails; the artifact does not receive the fallback. A coherently absent path is `MISSING`, not unclassified, and cannot support a reviewed claim.

Superseded, historical, invalid, missing, and unclassified targets remain nonqualifying even beside canonical evidence. Free text cannot promote them.

## Frozen canonicalization profile

Every implementation uses `CHARACTER_INDEX_V2_C14N_1`:

1. Decode governed text as strict UTF-8. Invalid UTF-8 and lone surrogates fail.
2. Require stored strings already in NFC under Unicode Character Database 15.0.0. Reject NFD rather than rewriting it.
3. Prohibit NFKC/NFKD compatibility normalization.
4. Define `nfc(s) = Unicode-15.0.0-NFC(s)`.
5. Define `fold(s) = nfc(Unicode-15.0.0 full default case fold of nfc(s))`, using full common/default mappings and excluding Turkic mappings.
6. Define `sort_key(s) = (UTF8(fold(s)), UTF8(nfc(s)))`, compared lexicographically as unsigned bytes.
7. Use folding only for comparison, collision detection, and primary human-text ordering. Stored spelling, exact-case path lookup, IDs, and artifact hashes retain their NFC case and bytes.
8. Perform no implicit trimming or whitespace collapsing.
9. Fail clearly unless the implementation uses Unicode 15.0.0 data.

Deterministic collection order is:

- evidence references and digest entries: parsed `analysis_subject_id`, then parsed `evidence_id`, then exact ASCII reference as a tie-breaker;
- aliases: normalized language, ASCII kind, `sort_key(value)`, exact NFC value bytes, then RFC 8785 canonical alias-object bytes;
- evidence and coverage: ASCII `evidence_id` and `coverage_id`;
- derived composite continuities: ASCII `continuity_id`; and
- diagnostics: repository path, JSONL line, instance path, then schema path.

Generated Markdown and JSONL use UTF-8 without BOM and LF only. Generation rules never rewrite committed artifact bytes used for hashing.

## Exact artifact-byte hash

For each resolved reference, read the regular Git blob payload at the assessment's full `basis_commit` and exact-case `repository_path`:

```text
artifact_sha256 = lowercase_hex(SHA-256(exact committed Git blob payload bytes))
```

Hash the payload only. Exclude the Git `blob <length>\0` header. Never substitute:

- a SHA-1 or SHA-256 Git object ID;
- worktree or untracked bytes;
- checkout-converted line endings;
- normalized Unicode;
- BOM-stripped content;
- decompressed content; or
- an externally fetched Git LFS object.

Missing or wrong-case blobs, nonregular modes, symlinks, submodules, and Git LFS pointer blobs cannot qualify.

## `CHARACTER_EVIDENCE_SET_V1`

After validating the exact claim union, resolve each reference at `basis_commit`. For each reference construct this logical entry after NFC validation:

```json
{
  "analysis_subject_id": "example:alice@anime",
  "anchor": null,
  "artifact_sha256": "64 lowercase hexadecimal characters",
  "evidence_id": "profile",
  "repository_path": "series/example/ALICE.md"
}
```

`anchor` is its exact NFC value without a leading `#`, or JSON `null`; an omitted discovery anchor projects to `null`. Sort entries by subject ID and evidence ID under the frozen ordering. Then construct:

```json
{
  "canonicalization": "CHARACTER_EVIDENCE_SET_V1",
  "evidence": [],
  "hash_algorithm": "SHA-256",
  "unicode_version": "15.0.0"
}
```

Serialize the populated envelope with RFC 8785 JSON Canonicalization Scheme, encode it as UTF-8 without BOM or trailing newline, and compute:

```text
evidence_set_sha256 =
  lowercase_hex(SHA-256(RFC8785_canonical_serialization_bytes))
```

`basis_commit` is required in scope but excluded from this envelope. Therefore an unrelated commit does not change the evidence-set identity, while changed referenced bytes, path, anchor, subject ID, or evidence ID does. Labels, notes, dimensions, review flags, derived authority classifications, and Git object IDs are not payload fields and have their own validators. Authority front matter physically present in the artifact is naturally bound by the raw-byte artifact hash.

### Normative golden vector

For exact artifact bytes `alpha\n`:

```text
artifact_sha256 = b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060
```

With subject `example:alice@anime`, evidence ID `profile`, path `series/example/ALICE.md`, and null anchor, the exact RFC 8785 bytes interpreted as UTF-8 text are:

```json
{"canonicalization":"CHARACTER_EVIDENCE_SET_V1","evidence":[{"analysis_subject_id":"example:alice@anime","anchor":null,"artifact_sha256":"b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060","evidence_id":"profile","repository_path":"series/example/ALICE.md"}],"hash_algorithm":"SHA-256","unicode_version":"15.0.0"}
```

The required result is:

```text
174c697bb3e87f75bb1fc56d6aec718328e9e6670dc33859919d3a82e2d387d7
```

For the empty `UNASSESSED` envelope, the exact serialization is:

```json
{"canonicalization":"CHARACTER_EVIDENCE_SET_V1","evidence":[],"hash_algorithm":"SHA-256","unicode_version":"15.0.0"}
```

Its deterministic SHA-256 is:

```text
50dc6ac299e4602ee01b3b702a11e64c69cf52fe50182911eca4a377468b30d2
```

## Reproducibility and staleness

Historical `STALE` and `SUPERSEDED` records reproduce their stored evidence-set hash from committed bytes and authority state at their historical `basis_commit`. Currentness is then evaluated again at the comparison commit.

An assessment becomes stale when, among other governed causes:

- a referenced artifact's exact bytes, path, or anchor change;
- evidence membership changes;
- the discovery subject or scope changes;
- a referenced artifact stops qualifying current authority;
- a new supersession edge retires a predecessor, even if that predecessor's bytes and historical digest remain unchanged; or
- the basis history is unavailable and cannot be verified.

An unchanged digest alone does not prove currentness because an incoming authority edge lives outside the predecessor's bytes. Conversely, an unrelated commit with unchanged evidence and authority does not change evidence-set identity.

## Schema and application-validation boundary

The JSON Schema enforces closed objects, required fields, enums, constants, patterns, nullability, claim shapes, composite scope shape, known-limit rules, scenario conditions, and status-dependent local invariants.

Application validation remains mandatory for facts JSON Schema cannot prove:

- strict duplicate-key rejection before ordinary schema validation;
- Unicode 15.0.0 normalization and ordering;
- discovery-record and entity/subject resolution;
- exact composite component equality and same-series recursive leaves;
- exact controlled-dimension/scenario coverage;
- claim-union equality and deterministic ordering;
- Git object type, object-format length, exact path/mode, and raw blob bytes;
- artifact front-matter parsing and bounded authority graph;
- RFC 8785 digest recomputation;
- authority reevaluation and staleness;
- reciprocal assessment supersession and cycle rejection; and
- deterministic generated-output drift.

Schema validation and reference resolution perform no network retrieval. Any unavailable dependency, Unicode version, Git history, or governed evidence target fails closed rather than degrading to approximate validation.

## Deliberate nonpopulation

This specification does not assess, tier, or score any character. The intended later sequence is:

```text
1. migrate and stabilize canonical analytical artifacts
2. create reviewed discovery records
3. stabilize the Git corpus and authority state
4. calibrate the reconstruction method against mature anchor projects
5. perform a separate owner-reviewed capability assessment
```

No production capability registry, generated capability index, or assessment may be inferred from the existence of this schema and specification.
