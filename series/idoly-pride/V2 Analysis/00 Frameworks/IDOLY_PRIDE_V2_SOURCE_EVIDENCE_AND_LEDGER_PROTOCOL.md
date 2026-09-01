---
title: "IDOLY PRIDE V2 Source, Evidence, and Ledger Protocol"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL"
version: "2.4"
status: "governing-framework"
created: "2026-08-13"
updated: "2026-08-19"
live_corpus: true
priority_authority: "V2 corpus coverage and priority ledger"
historical_priority_lists: "advisory only"
---

# IDOLY PRIDE V2 SOURCE, EVIDENCE, AND LEDGER PROTOCOL

## 1. Purpose

This protocol defines how V2 converts a very large game-extracted corpus into stable, auditable analytical claims.

It is designed to prevent three failures:

1. overreliance on a preselected set of "important" events;
2. loss of source context when using character omnibus bundles;
3. synthesis claims becoming detached from the exact material that supports them.

The V2 ledger system is the determinative analytical layer.

Historical curated collections such as `idoly-ingest-selected-events-core-important` remain useful discovery aids, but they do not determine canonical importance.

---

# 2. Source identity

Every analytically meaningful source must receive or preserve a stable `SOURCE_ID`.

Prefer source-system identifiers when available.

Examples:

- `MAIN_HOSHIMI_...`
- `UNIT_IIIX_...`
- `EVENT_ST-EVE-2508-FREE-002`
- `CARD_MHK_05_...`
- `BOND_...`
- `MSG_...`
- `PHONE_...`
- `ANIME_E01`
- `3DMV_TSUKI_TSUKI_NO_HIKARI`
- `4KOMA_MAIN_042`

Do not create vague locators such as "miho event about America."

A locator must be machine-searchable.

## 2.1 Makino identity and player-branch source semantics

For V2, `Manager (player)` / `{user}` is **Makino Kouhei continuity by default**. The game exposes Makino through a player-facing interface; editable naming does not create a separate protagonist when the narrative role, history, appearance, and voiced presentation remain continuous with anime Makino. Treat this as a governing source-identity decision unless explicit primary evidence contradicts it.

Every manager-bearing source should distinguish these fields where relevant:

```yaml
manager_identity: MAKINO_KOUHEI_CONTINUITY
manager_branch_status: IDENTITY_INVARIANT | BRANCH_INVARIANT | PLAYER_SELECTED | INTERFACE_PARAMETERIZATION
branch_group_id:
branch_option_id:
fixed_event_consequence:
```

Interpretation rules:

- `IDENTITY_INVARIANT`: normal Makino evidence.
- `BRANCH_INVARIANT`: normal fixed characterization/action.
- `PLAYER_SELECTED`: evidence for Makino's **authored possibility space**, not proof that mutually exclusive alternatives all happened. Repeated traits across independent branches can strengthen a stable characterization claim.
- `INTERFACE_PARAMETERIZATION`: custom name / `{user}` / equivalent interface affordance; do not treat as identity divergence.

If a selectable line becomes load-bearing, preserve its branch locator. If a claim depends on a trait that appears only in one mutually exclusive option, label that limitation explicitly.

## 2.2 Anime-era Hoshimi cross-media relation field

For `st-original-cmn` and other direct anime-era retelling/expansion material, add a cross-media relation field where analytically useful:

```yaml
anime_relation: DIRECT_RETELLING | EXPANDED_MAKINO_POV | EXPLICITATED_MOTIVE_OR_PROFESSIONAL_REASONING | ADDED_SCENE_OR_CONTEXT | BRANCH_PARAMETERIZED_MAKINO_EXPRESSION | REFRAMING_OR_EMPHASIS_SHIFT | ANIME_ONLY_AUDIOVISUAL_FORM | CONTINUITY_TENSION
anime_episode_refs:
anime_prospective_boundary_preserved: YES | NO | N/A
```

This field exists to answer **what the game adds to the anime telling** without retroactively pretending an anime-only viewer possessed later explicit game information.

## 2.3 Unit-origin chronology and disclosure fields

Unit-origin stories must preserve both **diegetic chronology** and **disclosure chronology**. Add the following fields when routing origin material:

```yaml
diegetic_position:
disclosure_position:
prerequisite_main_story_state:
retrospective_targets: []
forward_inheritance_point:
origin_dependency_status: OPTIONAL_CONTEXT | INSERT_BEFORE_NEXT_ARC | HARD_PREREQUISITE
```

Interpretation rules:

- `diegetic_position` records when the depicted event occurs in-world; it does not by itself determine reading order.
- `disclosure_position` records when the game makes the history available and therefore protects first-impression states from later explanatory backfill.
- `retrospective_targets` names earlier claims or audit findings that the origin may confirm, qualify, split, weaken, overturn, or re-source.
- `forward_inheritance_point` marks the first later analytical unit that may treat the origin information as inherited knowledge.
- `HARD_PREREQUISITE` means the next governing main-story arc must not be read prospectively without first freezing that origin baseline.

For the current Phase-1B sequence, the SUNNY PEACE, Tsuki no Tempest, LizNoir, and TRINITYAiLE origin groups are inserted before Tokyo and may generate a Hoshimi audit addendum. The IIIX origin group is `HARD_PREREQUISITE` for Tokyo.

---

# 3. Source record schema

Recommended ledger entry:

```yaml
source_id:
source_type:
title:
story_id:
bundle_id:
corpus_path:
release_or_order:
characters:
units:
relationships:
themes:
narrative_function:
priority:
priority_reason:
v1_relevance:
v2_revision_potential:
audiovisual_dependency:
text_status:
source_confidence:
manager_identity:
manager_branch_status:
branch_group_id:
branch_option_id:
anime_relation:
anime_episode_refs:
diegetic_position:
disclosure_position:
prerequisite_main_story_state:
retrospective_targets:
forward_inheritance_point:
origin_dependency_status:
first_seen_snapshot:
last_seen_snapshot:
change_type:
notes:
```

For bundled stories preserve both bundle ID and granular story IDs.

---

# 4. Priority ledger authority

The V2 corpus coverage ledger is the authoritative classification of analytical priority.

Allowed values:

## FOUNDATIONAL

Without this source, the character/unit/series model becomes materially wrong or structurally incomplete.

## CORE

Necessary to a mature understanding.

## IMPORTANT

Meaningfully deepens, qualifies, or revises the model.

## TEXTURE

Low-stakes material valuable for voice, social rhythm, ordinary life, professional behavior, care grammar, unit culture, preferences, fandoms, hobbies, domestic habits, leisure, humor, mundane competencies, aversions, or conversational behavior. `TEXTURE` means lower expected narrative weight, not lower canonical reality for the narrow question it answers.

## REDUNDANT

Adds little that is not already better supported elsewhere. Redundant does not mean disposable; it may still corroborate.

## CONFLICTING

Introduces meaningful tension with the current model. These sources should be prioritized, not hidden.

## FORMAL-DEPENDENT

Transcript alone is insufficient. Audio, visuals, staging, or another formal source is required.

## UNRESOLVED

Source status or meaning remains uncertain.

---

# 5. Reassessment of historical `core-important` material

When a historically curated source is encountered, V2 should ask:

1. Why was it previously selected?
2. Does the extracted source support that importance?
3. Has later evidence changed its role?
4. Is its importance character-specific, relationship-specific, or series-wide?
5. Is a less famous source actually more determinative?
6. Does the old classification merely reflect what was previously available?

Historical labels are provenance, not inherited truth.

---

# 6. Character ledger schema

Each major character ledger should contain entries in chronological/source order.

Recommended entry:

```markdown
## Entry CHAR-MIHO-042

- Source ID:
- Source class:
- Story title:
- Approximate order:
- Epistemic class:
- Priority:
- Characters present:
- Relationship axes:
- Summary:
- What changes:
- Voice/register notes:
- Motifs/objects:
- Professional/idol implications:
- Counterevidence:
- V1 connection:
- Exact locator:
- Confidence:
```

Character ledgers should capture change, not merely quotations. They are not required to become exhaustive preference/lifestyle catalogues. Character-specific texture should be promoted here when it materially clarifies a longitudinal, relational, thematic, contradiction, or current voice claim; otherwise preserve routing for the later holistic modeling pass.

---

# 7. Relationship ledger schema

Recommended entry:

```markdown
## Entry REL-KOTONO-NAGISA-018

- Source ID:
- Relationship stage:
- Interaction type:
- Explicit self-definition:
- Care behavior:
- Conflict behavior:
- Dependence/asymmetry:
- Speech/address changes:
- Public/private difference:
- Performance consequence:
- Romantic/yuri coding status:
- Alternative reading:
- Exact locator:
- Confidence:
```

---

# 8. Theme ledger schema

Recommended entry:

```markdown
## Entry THEME-MEMORY-077

- Source ID:
- Characters/units:
- Theme:
- Concrete evidence:
- Local function:
- Possible series-level implication:
- Counterexample:
- Related motifs:
- Formal dependency:
- Exact locator:
- Confidence:
```

The distinction between `local function` and `series-level implication` is mandatory. It prevents one vivid story from being inflated into a franchise-wide thesis.

---

# 9. Claim IDs

Every consequential synthesis claim should receive a stable claim ID.

Examples:

- `CLM-MANA-001`
- `CLM-IIIX-014`
- `CLM-MIHO-008`
- `CLM-AUDIENCE-021`
- `CLM-MANAGER-006`

Claim record:

```yaml
claim_id:
claim:
document:
section:
epistemic_class:
supporting_ledger_entries:
supporting_source_ids:
counterevidence:
v1_status:
v2_status:
confidence:
open_questions:
validated_through:
last_retested:
source_snapshot_id:
update_status:
```

---

# 10. V1 revision vocabulary

Use standard revision labels:

- **CONFIRMED** - V2 independently reproduces the claim.
- **STRENGTHENED** - new evidence materially increases confidence or depth.
- **QUALIFIED** - core claim survives but needs narrower wording.
- **SPLIT** - one old claim actually contained multiple distinct phenomena.
- **WEAKENED** - evidence supports the claim less strongly than V1 suggested.
- **OVERTURNED** - source evidence contradicts or displaces the old conclusion.
- **RECONTEXTUALIZED** - factual compatibility remains, but meaning changes in later context.
- **UNRESOLVED** - evidence remains insufficient.

This vocabulary belongs primarily in ledgers, not repeatedly in polished prose.

---

# 11. Context descent protocol

When reading `analysis_bundles`, descend to `idoly-ingest` when:

- a claim will be quoted directly;
- exact surrounding dialogue matters;
- source ordering is ambiguous;
- an omnibus excerpt removes relevant setup/payoff;
- a story contains multiple scenes with different functions;
- a contradiction appears;
- speaker attribution is uncertain;
- the claim is foundational to a major synthesis section;
- the evidence will become a canonical locator.

Not every source needs a second read. The purpose is selective precision.

---

# 12. Audiovisual routing

Textual and audiovisual claims remain separately traceable.

Example:

`TXT-TSUKI-014`: Kotono explicitly describes the unit's relation to illumination.

`AV-TSUKI-007`: the 3DMV stages collective illumination through center redistribution, lighting, and group formation.

A synthesis may combine them, but the ledger preserves their different origins.

---

# 13. Telephone evidence

Use three confidence states.

## PHONE-AUDIO-VERIFIED

Audio personally checked for the relevant claim.

## PHONE-ASR-SUPPORTED

ASR is semantically useful, but exact wording has not been independently verified.

## PHONE-GAP

Audio or transcription is absent/incomplete.

Never use unverified ASR as the sole basis for subtle claims about particles, register, pronouns, sentence endings, ambiguous names, emotional micro-delivery, or exact quotation.

---

# 14. Japanese-language evidence

When language is analytically important, preserve:

- original Japanese where available;
- literal sense;
- natural English gloss;
- why the wording matters;
- source ID;
- context;
- confidence.

Do not make an argument from an English paraphrase when the Japanese distinction is the actual evidence.

---

# 15. Visual evidence

For card/scene/3DMV/anime claims record:

- source ID;
- image/frame/shot locator where available;
- visible fact;
- interpretation;
- recurring comparison;
- confidence.

Example:

```markdown
Visible fact:
miho's long black hair is foregrounded in the card art.

Interpretation:
the visual emphasis participates in the larger bodily-memory pattern established textually by Yo's compliment.
```

Do not collapse visible fact and interpretation into one category.

---

# 16. Contradiction handling

When sources conflict:

1. preserve both;
2. check chronology;
3. check source class;
4. check comedy/exaggeration;
5. check extraction/translation context;
6. ask whether the contradiction reflects character inconsistency rather than writing inconsistency;
7. check whether a later source intentionally revises the earlier one.

Do not harmonize automatically.

---

# 17. Sampling policy

The corpus is too large for equal-depth reading of everything.

Use a two-pass strategy.

## Pass A: broad coverage

Read enough of every source region to classify relevance and detect missing dimensions.

## Pass B: selective close reading

Deep-read:

- foundational sources;
- contradictions;
- turning points;
- unusual relationship evidence;
- voice-rich scenes;
- formal-dependent sources;
- sources supporting major synthesis claims.

This preserves breadth without pretending every birthday card and main-story climax deserve equal analytical bandwidth.

## 17.1 Late-phase character texture and experiential extraction

The project deliberately separates **literary importance** from **experiential modeling value**. A source can be low priority for the longitudinal literary argument while being highly informative about what the character is like to spend ordinary time with.

Phases 1-8 therefore need not exhaustively convert every texture source into character-ledger prose. Phase 8.5 performs a targeted re-sweep for the holistic character-modeling profiles.

For experiential evidence, preserve two independent dimensions:

1. the ordinary epistemic class (`TEXTUAL FACT`, `AUDIOVISUAL FACT`, `STRONG INFERENCE`, etc.);
2. a recurrence/predictiveness class:
   - `ONE_OFF` - directly evidenced once, minimal predictive force;
   - `REPEATED_PREFERENCE` - repeated choice or explicit liking across more than one context/source;
   - `STABLE_DISPOSITION` - behavior generalized across contexts with meaningful recurrence;
   - `BEHAVIORALLY_PREDICTIVE` - evidence strong enough to constrain likely future ordinary behavior or conversation.

Recommended texture-evidence fields:

```yaml
character:
category:
item_or_behavior:
epistemic_class:
recurrence_class:
source_ids:
exact_locators:
temporal_scope:
relationship_or_context:
confidence:
behavioral_relevance:
canonical_destination:
notes:
```

The default mature `canonical_destination` is the character's `IDOLY_PRIDE_V2_CHAR_<CHARACTER>_MODELING_PROFILE.md`. Promote the same evidence into a longitudinal ledger or numbered synthesis only when it is independently load-bearing there.

An optional cumulative `IDOLY_PRIDE_V2_CHARACTER_TEXTURE_EVIDENCE_LEDGER.md` may be created under `07 Evidence Indexes and Claim Routing` during Phase 8.5 if systematic extraction volume warrants it. It is a source-routing/audit surface, not a parallel per-character preference document and not a substitute for the modeling profile.

Document `15_ORDINARY_LIFE_MESSAGES_CARDS_BONDS_AND_SOCIAL_TEXTURE.md` remains series-level synthesis: it explains what ordinary-life material does across the work. It should not be forced to store every character-specific preference fact.

---

# 18. Ledger-to-document routing

Each ledger entry should name likely canonical destinations.

Example:

```yaml
canonical_destination:
  - "07_IIIX_UNIT_AND_CHARACTER_SYNTHESIS"
  - "10_GRIEF_DEATH_MEMORY_SURVIVAL_AND_CONTINUITY"
```

A source may support multiple documents, but the detailed prose should still have one primary analytical home to reduce duplication.

---

# 19. Final claim audit

Before release, sample each major section of the full-series synthesis backward.

For each sampled claim:

1. locate the specialist document;
2. locate the ledger entry;
3. locate the source ID;
4. locate the story/audiovisual source;
5. verify the epistemic label;
6. inspect counterevidence;
7. confirm no V1 claim survived merely through repetition.

The final literary corpus does not need a locator for every ordinary sentence. It does need robust routing for every load-bearing claim. Phase-8.5 modeling profiles may additionally preserve locators for otherwise low-stakes preference/behavior evidence when those particulars materially improve experiential reconstruction.

---

# 20. Live-corpus source-delta protocol

Every new extraction snapshot must be compared against the source manifest of the last audited snapshot. The output is a **delta**, not a replacement narrative of the entire corpus.

For each changed item record:

```yaml
delta_id:
source_id:
previous_snapshot:
current_snapshot:
change_type:  # added | modified | removed | replaced | asset-added | upstream-correction
characters:
units:
relationships:
initial_priority:
impact_class:
affected_claims:
affected_documents:
requires_reanalysis:
notes:
```

## 20.1 Impact classes

- **CLASS-1 ADDITIVE-TEXTURE** - ordinarily ledger-only until accumulation warrants prose revision.
- **CLASS-2 SIGNIFICANT-DEVELOPMENT** - specialist ledgers and affected synthesis documents must be re-audited.
- **CLASS-3 ARCHITECTURAL** - triggers broad claim routing and possible full-series synthesis revision.

Impact class is determined by what the source changes, not by whether it is formally a main story, event, card, or message.

## 20.2 Pending reanalysis queue

A source may be ingested before all downstream prose is updated. Such cases must be explicit. Maintain a queue containing:

- source/delta ID;
- affected character/unit;
- affected claim IDs;
- expected canonical destinations;
- impact class;
- status.

A frozen release may not claim coverage through a source cutoff while silently leaving Class-2 or Class-3 items pending. Either resolve them or state the limitation in the release manifest.

---

# 21. Character and unit freshness registry

Maintain `CHARACTER_UNIT_UPDATE_STATUS.md` with at least:

```yaml
character_or_unit:
last_corpus_review:
latest_source_included:
source_snapshot_id:
validated_through:
update_status:
new_material_pending:
requires_synthesis_revision:
```

Recommended `update_status` values:

- `current`
- `new-material-pending`
- `reanalysis-required`
- `provisional`
- `archived-at-release`

This prevents older character syntheses from appearing equally current with recently revalidated ones.

---

# 22. Temporal claim revalidation

When new material touches a claim, do not merely append a citation. Retest the claim.

Possible outcomes use the existing revision vocabulary:

- CONFIRMED
- STRENGTHENED
- QUALIFIED
- SPLIT
- WEAKENED
- OVERTURNED
- RECONTEXTUALIZED
- UNRESOLVED

Update `validated_through`, `last_retested`, `source_snapshot_id`, and `update_status`.

Claims untouched by the new delta may retain their previous validation frontier; do not falsely advance `validated_through` merely because an unrelated story was released.

---

# 23. New-character and new-unit protocol

A newly introduced character/unit enters the corpus as `provisional`.

Create a provisional ledger and gather breadth before drafting a definitive synthesis. Introductory characterization should remain explicitly provisional until enough later evidence tests it.

Promotion criteria should include some combination of:

- multiple independent source appearances;
- a stable relational position;
- enough material to distinguish public persona from longitudinal characterization;
- evidence of professional/performance philosophy where relevant;
- sufficient counterevidence testing.

---

# 24. Main-story automatic audit trigger

A substantial new main-story tranche automatically routes to review of:

- series architecture;
- affected character ledgers;
- affected unit/relationship ledgers;
- Mana/Makino inheritance where relevant;
- institution/industry themes;
- all relevant `OPEN`, `UNRESOLVED`, or `CONFLICTING` claims;
- the continuous full-series synthesis if the new material is architectural.

Other source classes use narrower routing unless their actual semantic impact warrants escalation.

---

# 25. Frozen-release integrity

The rolling workspace is mutable. A frozen release is not.

Every frozen release must record:

- source cutoff;
- source snapshot ID;
- release version;
- unresolved/pending limitations;
- changed claim IDs since the prior release;
- changed synthesis documents;
- checksums.

New sources may recontextualize an older release, but they do not retroactively rewrite what that release claimed to cover.

---

# 26. Minimum archival outputs

At final release preserve:

- `SOURCE_MANIFEST.md`
- `SOURCE_CUTOFF_AND_PROJECT_DECISIONS.md`
- `SOURCE_DELTA_LEDGER.md`
- `SOURCE_SNAPSHOT_HISTORY.md`
- `CHARACTER_UNIT_UPDATE_STATUS.md`
- `PENDING_REANALYSIS_QUEUE.md`
- `IDOLY_PRIDE_V2_CORPUS_COVERAGE_AND_PRIORITY_LEDGER.md`
- selected character/relationship/theme ledgers;
- `18_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`
- `CORPUS_MANIFEST.md`
- `DELIVERY_AUDIT.md`
- `SHA256SUMS.txt`

The analysis package should remain useful even if the chat history is lost.

---

# 27. Governing principle

The ledger exists to make selection explicit.

The project should never again rely on:

> "this event seemed important when we happened to analyze it."

Instead:

> **importance is a recorded conclusion produced by corpus-wide comparison, open to revision, and traceable to source evidence.**
