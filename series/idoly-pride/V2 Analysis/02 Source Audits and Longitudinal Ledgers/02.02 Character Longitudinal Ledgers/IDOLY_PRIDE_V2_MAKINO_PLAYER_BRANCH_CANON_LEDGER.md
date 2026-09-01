---
series: IDOLY_PRIDE
artifact_type: branch_canon_ledger
artifact_role: LEDGER
scope: MAKINO_PLAYER_BRANCH_CANON
character: 牧野航平 / Makino Kouhei
character_code: koh
generation: V2
version: '1.0'
status: canonical
phase: '2'
tranche: P2-A3
source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: Branch-canon adjudication for the Manager (player) / Makino Kouhei interface across the complete Phase-1-routed game snapshot. Fixed Makino characterization inherits P2-A2 and the Hoshimi anime-game expansion audit. Player-selectable or alternate-route material is classified only to the granularity supported by the mirrored ingest. The current bundle/JSONL projection preserves dialogue and provenance but does not preserve explicit branch_group_id/branch_option_id control-flow metadata for every selectable line; exact option IDs are therefore never invented.
validated_through: IP-V2-SNAPSHOT-2026-08-13-A
branch_semantic_status: PASS_WITH_EXPLICIT_BRANCH_LOCATOR_LIMITATION
manager_identity: MAKINO_KOUHEI_CONTINUITY
manager_identity_reopen_status: CLOSED_ABSENT_CONTRADICTORY_PRIMARY_EVIDENCE
branch_locator_completeness: PARTIAL_SOURCE_PROJECTION_LIMITATION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
inherits:
- IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL.md
- IDOLY_PRIDE_V2_PHASE2_LONGITUDINAL_LEDGER_SCHEMA.md
- IDOLY_PRIDE_V2_CHAR_MAKINO_LONGITUDINAL_LEDGER.md
- IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT.md
- IDOLY_PRIDE_V2_CORPUS_COVERAGE_AND_PRIORITY_LEDGER_v1.30.md
created: '2026-08-18'
updated: '2026-08-18'
next_operation: P2-B1 — SUNNY PEACE character longitudinal ledgers; begin with IDOLY_PRIDE_V2_CHAR_SAKURA_LONGITUDINAL_LEDGER.md
recommended_model: GPT-5.6 Sol
recommended_reasoning: Extra High
---

# IDOLY PRIDE V2 — MAKINO PLAYER-BRANCH CANON LEDGER

## P2-A3 — branch, interface, possibility-space, and continuity authority

---

# 0. Completion result

**P2-A3 RESULT: `PASS_WITH_EXPLICIT_BRANCH_LOCATOR_LIMITATION`.**

The branch-canon problem is analytically resolved for the locked snapshot even though the mirrored ingest does not preserve every original control-flow identifier.

The governing result is:

> **The game does not ask the analyst to choose between “Makino is a fixed character” and “the player can select some of Makino's expressions.” Both are true at different authority levels. Fixed biography, history, narration, professional decisions, relationships, and branch-invariant consequences are ordinary Makino canon. Selectable replies are authored Makino-compatible possibilities whose local selection can matter inside a route, but mutually exclusive alternatives cannot be accumulated into a single literal biography.**

The correct model is therefore **not union-all canon**. It is a layered canon stack:

1. **identity invariant** — the manager is Makino Kouhei;
2. **branch invariant** — fixed history, actions, narration, dialogue, and consequences;
3. **cross-branch recurrent characterization** — a tendency independently reproduced across multiple incompatible options or routes;
4. **player-selected Makino expression** — one authored option among alternatives;
5. **branch-only trait/action** — true only inside the selected branch unless later fixed evidence promotes it;
6. **interface parameterization** — `{user}` / editable name and comparable UI affordances;
7. **continuity tension** — reserved for actual primary-source contradiction, not ordinary route variation or anime/game retelling difference.

No current source requires reopening Makino's identity.

No branch-only romantic line is allowed to create a mainline romance by itself.

No anime/game retelling difference is automatically a player-branch contradiction.

No adjacent Manager lines in a flattened message bundle are assumed to be either sequential or alternative solely from adjacency when branch-control metadata is absent.

---

# 1. Why this ledger exists

P2-A2 established Makino as a highly authored longitudinal character and froze thirty character claims across the Phase-1-routed snapshot. That ledger deliberately left one issue unresolved by architecture: the game exposes the continuing Makino through a player-facing interface, and some source regions permit selectable expression.

Without a separate branch-canon ledger, two opposite errors become easy.

## Error A — avatar erasure

The analyst sees `Manager (player)` or `{user}` and treats the entire game manager as an empty self-insert. This destroys fixed evidence such as:

- Makino's school history with Mana;
- his `日陰組` self-conception;
- his ordinary adolescent attraction to Mana before closeness;
- Mana's recruitment of him into Hoshimi;
- his assistant-manager apprenticeship;
- his decision to remain in management after graduation;
- his grief after Mana's death;
- his pact with Saegusa;
- his recruitment and management of Sakura and Kotono;
- his private professional reasoning;
- his role in Hoshimi's unit architecture;
- his final farewell to Mana;
- his continuing later professional relationships.

Those facts exist independently of a custom player name.

## Error B — union-all characterization

The analyst recognizes Makino as a character and then treats every selectable reply as though the same Makino literally said all alternatives.

That creates impossible composites. A character may then appear simultaneously:

- direct and evasive in one instant;
- teasing and solemn in the same exchange;
- approving and disapproving of the same proposition;
- romantically interested and explicitly non-romantic toward the same person;
- willing and unwilling to take the same action.

The game authors the **space of permissible Makino expressions**. It does not authorize the analyst to merge mutually exclusive choices into one event history.

P2-A3 resolves this by separating **character identity**, **fixed event history**, **stable tendencies**, and **route-local expression**.

---

# 2. Governing source rule

`IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL.md` §2.1 already fixes the project rule:

```yaml
manager_identity: MAKINO_KOUHEI_CONTINUITY
manager_branch_status: IDENTITY_INVARIANT | BRANCH_INVARIANT | PLAYER_SELECTED | INTERFACE_PARAMETERIZATION
branch_group_id:
branch_option_id:
fixed_event_consequence:
```

Its interpretation is controlling:

- `IDENTITY_INVARIANT` — normal Makino evidence;
- `BRANCH_INVARIANT` — normal fixed characterization/action;
- `PLAYER_SELECTED` — authored possibility-space evidence, not proof that all alternatives happened;
- `INTERFACE_PARAMETERIZATION` — naming/UI customization without identity divergence.

The protocol additionally permits repeated traits across independent branches to strengthen stable characterization.

This ledger extends that rule operationally without changing it.

---

# 3. Source audit: what the snapshot preserves and what it loses

## 3.1 The fixed Makino substrate is enormous

The Hoshimi anime/game expansion audit counted approximately:

- **10,709** textual dialogue/narration lines across the 23 Hoshimi game blocks;
- **2,844** lines assigned to `Manager (player)` — about **26.6%** of the Hoshimi text;
- **1,178** parenthetical/internal Makino lines — about **41.4%** of his Hoshimi lines.

That quantity matters because the player-facing surface sits on top of a very large fixed first-person character substrate. It is not a replacement for that substrate.

The fixed Hoshimi layer repeatedly supplies:

- memory;
- internal observation;
- professional evaluation;
- uncertainty;
- explicit ethical reasoning;
- self-critique;
- grief;
- attraction;
- embarrassment;
- strategic judgment;
- decisions not delegated to the player;
- causal explanations for actions;
- relationships established before the player-facing present.

P2-A3 therefore begins from the presumption that a Manager line is ordinary Makino evidence **unless the source marks or context securely establishes selectable/alternate-route status**.

The inverse presumption is prohibited: `Manager (player)` does not mean `PLAYER_SELECTED` merely because the speaker label contains “player.”

## 3.2 The manager code and voice metadata remain Makino-specific

A reopened `hoshimi_001_shine_purity.jsonl` row records:

- `speaker: "Manager (player)"`;
- `code: "koh"`;
- Makino-specific voice identifiers such as `...-koh001`, `...-koh002`, and so on.

This is not by itself the sole proof of identity, but it is consistent with the governing identity decision: the interface label and custom name sit over a character-coded, voiced Makino presentation.

## 3.3 The ingest projection does not carry the required control-flow fields

The published `idoly-ingest/_meta/bundle_schema.md` states that Markdown bundles carry bundle/source metadata and JSONL bundles add:

- `bundle_id`;
- `bundle_part`;
- `source_arc`;
- `source_story_id`;
- `source_path`;
- `seq_in_bundle`.

A technical inspection of `hoshimi_001_shine_purity.jsonl` confirms row keys such as:

`seq`, `story_id`, `asset_id`, `asset_index`, `t`, `speaker`, `code`, `text`, `start`, `voice`, `cite`, `bundle_id`, `bundle_part`, `source_arc`, `source_story_id`, `source_path`, `seq_in_bundle`.

The mirrored row projection does **not** expose:

- `branch_group_id`;
- `branch_option_id`;
- route-control commands;
- selection-state predicates;
- explicit reconvergence markers.

This is the reason the Hoshimi expansion audit warned that the flattened dialogue is excellent for semantic reading but not sufficient for exact branch routing in every case.

### Consequence

P2-A3 may classify a source or line as `PLAYER_SELECTED` only when one of the following is available:

1. the source itself is explicitly named/marked as a route or alternate branch;
2. a higher-authority Phase-1 audit has already established selectable status;
3. context unmistakably establishes a set of alternatives and that inference is labeled as such;
4. original provenance with branch metadata is later recovered.

P2-A3 **does not invent branch IDs** merely to make the ledger look complete.

---

# 4. Canon stack and promotion rules

## 4.1 Level A — `IDENTITY_INVARIANT`

This is the highest branch-related stability class.

It covers facts establishing who the protagonist is across the interface:

- Makino Kouhei continuity from anime to game;
- continuing Hoshimi role;
- Mana history;
- fixed biography;
- role history and employment;
- character code / presentation continuity;
- relationships presupposed by all branches.

A selectable response cannot demote an identity-invariant fact.

### Promotion test

A fact belongs here when changing it would require a genuinely different protagonist rather than a different reply by Makino.

## 4.2 Level B — `BRANCH_INVARIANT`

This is ordinary fixed Makino canon.

It includes:

- fixed narration;
- fixed dialogue outside a choice group;
- actions every route requires;
- fixed event setup;
- branch-reconvergent consequence demonstrated to occur regardless of selection;
- professional decisions not delegated to the player;
- fixed reactions from others when the same reaction is reached in all options.

P2-A2's thirty-claim longitudinal model is primarily built from this level plus identity-invariant material.

## 4.3 Level C — `CROSS_BRANCH_RECURRENT_TRAIT`

This is not a raw source status in the governing protocol; it is an **analytical promotion state**.

A trait may be promoted here when independent mutually exclusive options repeatedly reproduce the same underlying disposition even though surface wording differs.

Examples of what could qualify if securely branch-routed:

- multiple options all express concern for an idol's health, one gently and one brusquely;
- multiple options all refuse to exploit an idol's vulnerability, one through a joke and one through direct boundary language;
- multiple routes independently show Makino deflecting praise;
- multiple selectable expressions independently show him adapting register to the interlocutor.

The stable claim is the **shared trait**, not all literal lines.

### Required test

A promoted trait must survive subtraction of option-specific wording.

If option A is “I am worried about you” and option B is “Get some rest before I make you,” the common stable trait may be **health concern / protective monitoring**. It is not evidence that Makino literally said both.

## 4.4 Level D — `PLAYER_SELECTED_MAKINO_EXPRESSION`

This is the normal authority state for a selectable response.

It supports statements such as:

- the writers allow Makino to respond teasingly here;
- Makino can be authored as more direct or more restrained in this interaction;
- this tone is compatible with the character;
- the relationship permits this possible expression.

It does **not** by itself support:

- Makino definitely said this;
- this exact exchange belongs to all timelines;
- Makino always holds the stated preference;
- the other party always heard this line;
- a romance is canonically reciprocal;
- two incompatible answers are both autobiographical fact.

## 4.5 Level E — `BRANCH_ONLY_TRAIT_OR_ACTION`

Some route-local material is stronger than a single line because later dialogue or consequences develop it within that branch.

It remains branch-only if it is not independently fixed elsewhere.

The clearest current example is the explicit alternate/bad route:

`st-love-23-0514-007-bad`

The route depicts a Makino-position character who:

- declined Rei's theme-park invitation;
- became estranged from her;
- later confesses `好きです、付き合って下さい`;
- says he realizes he likes Rei;
- is rejected because the timing has passed.

That is genuine authored route content.

But Phase 1 classifies the source:

`PHASE1_BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY`

Therefore the route can establish:

> the franchise authors a Makino-compatible alternate possibility in which a Rei romance is narratively articulated.

It cannot establish:

> mainline Makino is canonically romantically attracted to Rei.

The bad route is precisely why branch-only evidence must remain quarantined.

## 4.6 Level F — `INTERFACE_PARAMETERIZATION`

Examples:

- `{user}`;
- player-edited displayed name;
- UI-facing address that changes the string but not the person occupying the role.

These are not character divergences.

`{user}` can appear in scenes that otherwise contain fixed Makino biography, fixed narration, and Makino-coded speech. The placeholder is therefore not evidence for a separate protagonist.

## 4.7 Level G — `CONTINUITY_TENSION`

Use this only when primary evidence creates a contradiction that cannot be explained by:

- selectable expression;
- a branch-only route;
- comedy/parody status;
- source chronology;
- anime/game retelling variation;
- interface parameterization.

**Current state: NONE ESTABLISHED for Makino identity.**

---

# 5. Impossible co-occurrence doctrine

The central anti-flattening rule of this ledger is:

> **Mutually exclusive options do not co-occur unless an independent fixed source later establishes the same propositions in compatible contexts.**

This applies at five levels.

## 5.1 Exact utterance

If the player chooses A or B, Makino does not literally say both at that decision point.

## 5.2 factual preference

If one option claims preference X and another option claims not-X, neither preference becomes fixed biography merely because both are authored.

## 5.3 emotional state

If one branch explicitly names romantic interest while another does not—or negates it—the romantic state is route-local unless another fixed source settles it.

## 5.4 action history

If one branch accepts an invitation and another refuses it, the later consequences belong to different histories until reconvergence is demonstrated.

## 5.5 relationship status

Dating, confession, exclusivity, rupture, reconciliation, or other state changes in one optional route cannot be exported to the main continuity.

This is especially important in an idol-management work where optional intimacy can otherwise silently convert professional relationships into canon romances.

---

# 6. Branch convergence doctrine

A branch can reconverge.

When it does, P2-A3 separates **the fixed consequence** from **the route-specific means**.

Example abstract form:

```text
Option A -> Makino encourages directly -> idol decides to perform
Option B -> Makino jokes, then encourages -> idol decides to perform
Option C -> Makino asks a question -> idol decides to perform
```

If all routes demonstrably converge on the same decision, then:

- `idol decides to perform` may be branch-invariant;
- “Makino supports the decision” may become a cross-branch recurrent trait if supported across options;
- none of the three exact reply texts becomes branch-invariant merely because the event reconverges.

Conversely, if a later scene differs because of the reply, that downstream material remains branch-local until an explicit reconvergence point.

---

# 7. Messages: the highest-risk branch surface

Phase 1 routed **99 message bundles / 1,812 granular messages** at story level and explicitly froze the rule:

> Player-selectable manager replies remain `PLAYER_SELECTED_MAKINO_EXPRESSION`; mutually exclusive options may not be accumulated into a single literal Makino history.

This source layer deserves special caution for three reasons.

## 7.1 The flattened message presentation can visually resemble ordinary sequential chat

A generated message bundle may place multiple Manager lines next to one another. Without original choice metadata, adjacency alone does not prove whether they are:

- multiple sequential messages;
- selectable alternatives;
- a mixture of fixed and selectable segments.

Therefore:

> **No option grouping is inferred from adjacency alone.**

## 7.2 Message reactions can still carry branch-safe evidence

If a fixed character line describes Makino in general terms independently of the selected reply, that character-side statement may be ordinary evidence.

For example, Kotono's message-side descriptions of Makino as someone who works with many idols, adapts advice to different people, and is trusted can support her perception of him without requiring every selectable manager reply to be fixed.

The analyst must separate:

- **what Kotono fixedly says about Makino**;
- from **which of several possible Makino replies the player may choose**.

## 7.3 Message romance must be especially conservative

A playful, intimate, flirtatious, embarrassed, or affectionate selectable reply can establish **compatibility of expression**.

It cannot alone establish:

- reciprocal romantic attraction;
- confession;
- dating;
- exclusivity;
- relationship-status change.

This is controlling for Rui/Makino.

Rui-side attraction remains strongly established from fixed evidence.

Makino reciprocity remains open unless a fixed or appropriately corroborated source supports it.

The unavailable `tel-card-rui-05-fest-04` remains a **formal dependency gap**, not a branch permission slip.

---

# 8. Explicit alternate-route case study: Rei bad branch

## Source

`misc_001_st-love-23-0514-007-bad`

Phase-1 route:

- priority: `CONFLICTING`;
- status: `PHASE1_BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY`.

## What happens inside the route

The scene's own setup states that Makino's position declined Rei's theme-park invitation. Their relationship cools. On graduation day he attempts to repair the rupture and explicitly confesses:

`好きです、付き合って下さい`

He later says:

`俺、やっぱり怜のことが好きなんだなって思って`

Rei says she had liked him too, but that the timing has passed and she now has no affection for him.

## Correct authority use

### Allowed

- The writers authorize an alternate Makino/Rei romance possibility.
- Makino can be written as belatedly recognizing romantic feeling toward Rei inside this route.
- The bad ending explores timing, missed recognition, and route causality.
- The route demonstrates that a player-facing branch can contain emotionally substantial Makino characterization.

### Not allowed

- “Makino is canonically in love with Rei.”
- “Rei and Makino canonically liked each other.”
- “Makino canonically confessed to Rei.”
- importing the route's failed audition/university/relationship outcomes into the normal timeline.

## Why this matters methodologically

This source is not disposable fanservice. It is authored possibility-space evidence.

But possibility-space evidence is **not** the same thing as continuity fact.

The right response is neither to erase it nor to canonize it wholesale.

---

# 9. False-positive case study: Rei's in-story romance game

`card_rei_004_st-card-rei-05-casl-02` contains repeated discussion of `選択肢` and `ルート分岐`.

However, these words refer to a **diegetic romance game being made about Rei**.

Makino later plays that game and says things like:

- `この選択肢はどっちを選べば……`
- `ここはあえて怜の誘いを断ってみるか`

These are choices **inside the fictional game within the card story**.

They are not, merely because the Japanese says `選択肢`, evidence that the surrounding IDOLY PRIDE card scene itself branches.

Therefore P2-A3 establishes a false-positive guardrail:

> **Choice vocabulary inside dialogue is not branch metadata. Branch classification must come from source structure or established routing, not lexical coincidence.**

---

# 10. Anime/game retelling variation is not player branch variation

The Hoshimi game retelling and anime differ materially in some event architecture, especially the finale.

The anime finale:

- has separate SUNNY PEACE and Tsuki no Tempest final performances;
- produces the extraordinary tie;
- lets Mana witness the differentiated unit performances before disappearing;
- then produces the ten-person Hoshimi winner-stage performance.

The game finale:

- has the units decide before the final to perform together;
- uses the ten-person performance as the final itself;
- returns to `First Step` as memorial encore;
- does not reproduce the anime's tie architecture in the available Hoshimi text.

This is a **`RETELLING_CONTINUITY_VARIANT`** between media.

It is not evidence that:

- player choice created one finale versus the other;
- Makino became a different protagonist;
- all differences should be collapsed into branch-option logic.

P2-A3 therefore separates two axes:

| Axis | Question |
|---|---|
| player branch | Which selectable Makino expression/action occurred inside a game route? |
| cross-media variant | How does the game retelling differ from the anime telling? |

Confusing them would make the continuity model less precise, not more.

---

# 11. Romance and intimacy branch rule

Because IDOLY PRIDE contains real romance-adjacent and romantic material, branch discipline must be stricter here than for low-stakes jokes.

## 11.1 Fixed romance evidence outranks optional flirtation

Examples:

- Mana's fixed confession of having loved Makino is textual fact.
- Makino's fixed attempted kiss in the final ghost farewell supports strong inference of reciprocal feeling at that moment.
- Rui's fixed self-recognition material establishes Rui-side romantic attraction strongly.

A selectable line may refine the **range of compatible Makino expression** around those facts, but it cannot replace their authority.

## 11.2 Branch-only romance cannot create mainline reciprocity

The Rei bad-route confession is the controlling example.

A route-specific confession can be narratively real inside that route and still carry **no mainline relationship-status authority**.

## 11.3 Repeated flirtation can become a stylistic tendency without becoming a relationship state

If multiple independent choice groups allow teasing/flirtatious replies to a character, a later voice model may conclude:

> the relationship is authored to permit flirtatious or teasing Makino expression.

That is not equivalent to:

> Makino canonically desires the character romantically.

The former is register/possibility evidence. The latter is a psychological relationship claim requiring stronger support.

## 11.4 Professional-boundary claims remain fixed unless the mainline text revises them

P2-A2 found fixed evidence that Makino recognizes romantic/sexual pursuit of currently managed talent as incompatible with his professional pride.

An alternate-route romance or playful selectable reply does not silently overturn that fixed professional ethic.

If a future fixed mainline source deliberately changes the boundary, that would be a substantive longitudinal revision. It must not be inferred from optional fanservice.

---

# 12. Professional-character branch rule

Makino's stable professional model from P2-A2 is **ANSWERABLE_PROFESSIONAL_AUTHORITY**.

Player selection can legitimately modulate:

- warmth;
- bluntness;
- teasing;
- self-deprecation;
- reassurance style;
- how much he verbalizes an observation;
- whether he asks or states in a low-stakes exchange.

But a single selectable option cannot by itself overturn branch-invariant evidence concerning:

- duty of care;
- privacy;
- bodily safety;
- role boundaries;
- talent evaluation;
- accountability;
- willingness to revise a managerial hypothesis;
- the idol's self-authored vocational ends.

A contradiction at this level would need repeated branch evidence or fixed consequences strong enough to force revision.

---

# 13. Voice-modeling rule for later P2-F

P2-A3 is essential to reconstructing Makino's manner of speaking accurately.

The voice model should use three buckets.

## Bucket A — fixed voice

Use freely for baseline reconstruction:

- fixed anime speech;
- fixed game narration;
- fixed game dialogue;
- fixed messages where option status is known to be non-selectable;
- branch-invariant professional exchanges.

## Bucket B — repeated branch-safe expression

Use to widen the model when multiple independent options show the same trait:

- dry teasing;
- modest deflection;
- understated reassurance;
- serious professional framing;
- situational embarrassment;
- adaptive register.

Record that the evidence is cross-branch rather than one literal transcript.

## Bucket C — branch-only coloration

Use only as a conditional register possibility:

- unusually romantic declaration;
- unusual hostility;
- extreme joke response;
- alternate-life preference;
- route-specific confession.

The voice model may say “Makino can be authored this way under route condition X.” It may not normalize the expression into his everyday baseline without independent support.

---

# 14. Branch promotion and demotion transitions

Branch authority can change when later evidence arrives.

## 14.1 Promotion

A branch-only proposition may be promoted when a later fixed source independently establishes it.

Transition:

`PLAYER_SELECTED / BRANCH_ONLY -> BRANCH_INVARIANT`

The ledger must record:

- original route source;
- later fixed source;
- whether the wording or only the underlying trait is promoted.

## 14.2 Trait promotion without event promotion

If several options express the same underlying concern, the trait may be promoted while the utterances remain optional.

Transition:

`multiple PLAYER_SELECTED options -> CROSS_BRANCH_RECURRENT_TRAIT`

No event-history merge occurs.

## 14.3 Demotion

If a line was previously treated as fixed but source recovery later shows it was selectable, the claim must be narrowed:

`BRANCH_INVARIANT -> PLAYER_SELECTED`

Downstream syntheses must be re-audited if the line was load-bearing.

## 14.4 Rejection as mainline evidence

If a source is explicitly a bad/alternate branch with no continuity authority:

`BRANCH_ONLY -> NO_MAINLINE_CONTINUITY_AUTHORITY`

This is not deletion. The source remains available for possibility-space, genre, game-design, and alternate-characterization analysis.

---

# 15. Branch-canon claim register

The following claims are canonical P2-A3 outputs.

| Claim ID | Claim | Epistemic class | Transition | Authority destination |
|---|---|---|---|---|
| `IP-BRANCH-KOH-001` | `Manager (player)` / `{user}` is Makino Kouhei continuity by default; player naming does not create a separate protagonist. | TEXTUAL FACT + framework identity decision | PRESERVE | all Makino work |
| `IP-BRANCH-KOH-002` | Fixed Makino biography, history, narration, professional decisions, and relationships are ordinary canon and do not inherit optionality merely from the speaker label `Manager (player)`. | STRONG INFERENCE | STRENGTHEN | Makino synthesis |
| `IP-BRANCH-KOH-003` | `{user}` and editable displayed name are `INTERFACE_PARAMETERIZATION`, not diegetic identity evidence. | TEXTUAL FACT / INTERPRETATION | PRESERVE | source protocol |
| `IP-BRANCH-KOH-004` | Player-selected replies are authored Makino-compatible possibilities but mutually exclusive alternatives may not be accumulated into one literal event history. | INTERPRETATION | PRESERVE | all downstream ledgers |
| `IP-BRANCH-KOH-005` | A trait repeated across securely independent branches may be promoted to `CROSS_BRANCH_RECURRENT_TRAIT` while exact option wording remains optional. | INTERPRETATION | STRENGTHEN | P2-F voice; character syntheses |
| `IP-BRANCH-KOH-006` | A trait or action supported only by one route remains branch-limited unless later fixed evidence independently establishes it. | INTERPRETATION | PRESERVE | all downstream ledgers |
| `IP-BRANCH-KOH-007` | Contradictory selectable factual preferences cannot be averaged into one Makino biography. | INTERPRETATION | PRESERVE | character model |
| `IP-BRANCH-KOH-008` | Branch-convergent consequences may be fixed even when the selectable wording that leads to them is not. | INTERPRETATION | STRENGTHEN | source/claim routing |
| `IP-BRANCH-KOH-009` | Downstream reactions that depend on a selected option remain branch-local until a reconvergence point is established. | INTERPRETATION | PRESERVE | relationship ledgers |
| `IP-BRANCH-KOH-010` | `st-love-23-0514-007-bad` is authored Makino/Rei alternate-route possibility-space evidence with no ordinary continuity authority. | TEXTUAL FACT | PRESERVE | Rei/Makino comparison only |
| `IP-BRANCH-KOH-011` | The Rei bad-route confession cannot establish mainline Makino romantic attraction to Rei. | INTERPRETATION | PRESERVE | romance guardrail |
| `IP-BRANCH-KOH-012` | Player-selectable flirtation/intimacy can support relationship register possibility but cannot alone establish reciprocity, dating, exclusivity, or fixed romantic state. | INTERPRETATION | STRENGTHEN | P2-C relationships |
| `IP-BRANCH-KOH-013` | Rui/Makino post-recognition outcome remains open; branch mechanics cannot fill the unavailable formal evidence gap. | CONFLICT / AMBIGUITY | OPEN | Rui/Makino ledger |
| `IP-BRANCH-KOH-014` | Fixed professional-boundary evidence from P2-A2 outranks isolated optional fanservice unless a later fixed source revises it. | INTERPRETATION | STRENGTHEN | Makino ethics |
| `IP-BRANCH-KOH-015` | Anime/game Hoshimi finale differences are cross-media `RETELLING_CONTINUITY_VARIANT`, not player-branch identity evidence. | TEXTUAL FACT / INTERPRETATION | PRESERVE | cross-media synthesis |
| `IP-BRANCH-KOH-016` | Lexical references to `選択肢`/`ルート分岐` inside a story are not branch metadata; the Rei romance-game card is a concrete false positive. | TEXTUAL FACT / INTERPRETATION | STRENGTHEN | source protocol |
| `IP-BRANCH-KOH-017` | The current ingest bundle schema does not preserve explicit branch group/option identifiers for every selectable manager line, so exact option locators may not be fabricated. | TEXTUAL FACT | OPEN locator limitation | evidence infrastructure |
| `IP-BRANCH-KOH-018` | No primary evidence in the locked snapshot establishes a genuine identity discontinuity between anime Makino and game Manager (player). | STRONG INFERENCE | PRESERVE | identity rule |
| `IP-BRANCH-KOH-019` | Option-status uncertainty must cause evidence downgrade, not silent promotion to fixed canon. | INTERPRETATION | STRENGTHEN | all claim audits |
| `IP-BRANCH-KOH-020` | P2-F may use branch-safe selectable material to model Makino's expressive range only when source status is carried with the sample. | INTERPRETATION | STRENGTHEN | voice/register layer |
| `IP-BRANCH-KOH-021` | The stable Makino model is the fixed core plus independently recurrent compatible tendencies; it is not the union of all authored routes. | INTERPRETATION | STRENGTHEN | character synthesis |
| `IP-BRANCH-KOH-022` | Explicit alternate branches remain valuable analytical evidence for what the franchise considers Makino-compatible even when they lack mainline event authority. | INTERPRETATION | STRENGTHEN | comparative/paratext analysis |
| `IP-BRANCH-KOH-023` | A fixed later source may promote a previously optional trait, but must not retroactively make the exact optional event happen unless it references that event. | INTERPRETATION | STRENGTHEN | revision ledger |
| `IP-BRANCH-KOH-024` | P2-A3 closes the semantic branch-canon gate for Phase 2; exact per-option control-flow recovery remains a traceability task rather than a blocker for P2-B character ledgers. | INTERPRETATION | PRESERVE | project state |

---

# 16. Detailed claim records

## IP-BRANCH-KOH-001 — manager identity is invariant

- **claim:** `Manager (player)` / `{user}` is the continuing Makino Kouhei unless contradictory primary evidence appears.
- **scope:** identity / continuity.
- **epistemic class:** TEXTUAL FACT + governing project identity decision.
- **transition state:** PRESERVE.
- **prior authority:** Source Evidence and Ledger Protocol §2.1; Hoshimi expansion audit; P2-A2.
- **supporting evidence:** fixed Mana history; Makino-coded internal narration; Hoshimi employment history; character code `koh`; Makino-specific voice identifiers; continuing role/relationships.
- **counterevidence:** custom naming alone.
- **adjudication:** custom naming is insufficient counterevidence because the authored biography remains specific.
- **canonical destination:** all Makino character/relationship/voice work.
- **freshness:** current through `IP-V2-SNAPSHOT-2026-08-13-A`.

## IP-BRANCH-KOH-002 — fixed manager material is ordinary canon

- **claim:** fixed biography/narration/actions are not optional merely because the UI speaker label says `Manager (player)`.
- **scope:** source semantics.
- **epistemic class:** STRONG INFERENCE.
- **transition state:** STRENGTHEN.
- **supporting evidence:** 2,844 Hoshimi Makino lines, including 1,178 internal narration lines; fixed school/Mana/profession/grief material.
- **counterevidence:** some manager-bearing regions also contain selectable replies.
- **adjudication:** option-bearing interface does not contaminate the entire character substrate with optionality.

## IP-BRANCH-KOH-003 — naming is interface parameterization

- **claim:** `{user}` is a name slot, not a second identity.
- **scope:** interface.
- **epistemic class:** TEXTUAL FACT / INTERPRETATION.
- **transition state:** PRESERVE.
- **evidence:** sources alternate between fixed `Manager (player)` labeling and characters addressing `{user}` while all fixed Makino history remains unchanged.
- **forbidden inference:** “Because the player may rename him, this cannot be Makino.”

## IP-BRANCH-KOH-004 — option plurality is possibility space

- **claim:** mutually exclusive responses are alternative authored Makino expressions.
- **scope:** player-selected dialogue.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **authority:** governing protocol + Phase-1 message routing.
- **forbidden inference:** all options happened.

## IP-BRANCH-KOH-005 — recurrent tendency promotion

- **claim:** repeated independent branch behavior can support a stable trait.
- **scope:** characterization.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **required evidence:** branch independence + shared underlying disposition.
- **guardrail:** promote the trait, not literal wording.

## IP-BRANCH-KOH-006 — single-branch limitation

- **claim:** one route does not establish a global trait.
- **scope:** branch-only evidence.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **test case:** Rei bad route.

## IP-BRANCH-KOH-007 — no averaging contradictions

- **claim:** incompatible preferences are not averaged into a vague midpoint personality.
- **scope:** contradictory options.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **reason:** branch design often deliberately lets the player choose different shades of the same character.

## IP-BRANCH-KOH-008 — consequence/utterance split

- **claim:** a fixed convergent result can have higher authority than the route-specific reply that reaches it.
- **scope:** branch convergence.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **downstream use:** event ledgers must separately record selected expression and fixed consequence.

## IP-BRANCH-KOH-009 — downstream branch locality

- **claim:** a reaction caused by a selected option remains local until reconvergence.
- **scope:** relationship causality.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **reason:** otherwise later dialogue can accidentally canonize an optional earlier state.

## IP-BRANCH-KOH-010 — Rei bad route has no ordinary continuity authority

- **claim:** `st-love-23-0514-007-bad` is explicit alternate-route evidence.
- **scope:** Makino/Rei.
- **epistemic class:** TEXTUAL FACT.
- **transition state:** PRESERVE.
- **source status:** `PHASE1_BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY`.
- **use:** possibility-space / branch design / counterfactual characterization.

## IP-BRANCH-KOH-011 — Rei confession does not transfer to mainline

- **claim:** route-local `好きです、付き合って下さい` cannot establish mainline Makino romantic attraction.
- **scope:** romance.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **counterfactual value:** shows that such expression is authorially compatible under route conditions.

## IP-BRANCH-KOH-012 — intimacy is not relationship state

- **claim:** selectable affection may widen register without fixing romance.
- **scope:** relationship interpretation.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **applies to:** Rui, Rei, and any future manager/idol intimacy claim.

## IP-BRANCH-KOH-013 — branch rules cannot repair formal gaps

- **claim:** missing Rui telephone evidence remains missing.
- **scope:** formal dependency.
- **epistemic class:** CONFLICT / AMBIGUITY.
- **transition state:** OPEN.
- **formal dependency:** `tel-card-rui-05-fest-04`.
- **forbidden behavior:** reconstructing the call from nearby optional replies.

## IP-BRANCH-KOH-014 — professional ethics require stronger evidence to revise

- **claim:** optional fanservice cannot silently overturn fixed professional-boundary evidence.
- **scope:** managerial ethics.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **prior authority:** P2-A2 `ANSWERABLE_PROFESSIONAL_AUTHORITY` model.

## IP-BRANCH-KOH-015 — cross-media variant is a separate axis

- **claim:** Hoshimi anime/game retelling differences are not player-branch differences.
- **scope:** cross-media continuity.
- **epistemic class:** TEXTUAL FACT / INTERPRETATION.
- **transition state:** PRESERVE.
- **test case:** Grand Prix finale architecture.

## IP-BRANCH-KOH-016 — choice vocabulary false positive

- **claim:** `選択肢` and `ルート分岐` in dialogue do not prove the surrounding source branches.
- **scope:** source parsing.
- **epistemic class:** TEXTUAL FACT / INTERPRETATION.
- **transition state:** STRENGTHEN.
- **test case:** `card_rei_004_st-card-rei-05-casl-02`, where the choice terminology belongs to the in-story romance game.

## IP-BRANCH-KOH-017 — exact branch locator gap

- **claim:** the mirrored ingest omits universal explicit option-group/control-flow fields.
- **scope:** provenance.
- **epistemic class:** TEXTUAL FACT.
- **transition state:** OPEN locator limitation.
- **support:** bundle schema + inspected Hoshimi JSONL row keys.
- **impact:** exact per-option IDs may remain unavailable; analysts must not fabricate them.
- **non-impact:** fixed Makino characterization and semantic branch doctrine remain usable.

## IP-BRANCH-KOH-018 — no identity tension established

- **claim:** no source currently requires a separate game-manager identity.
- **scope:** continuity.
- **epistemic class:** STRONG INFERENCE.
- **transition state:** PRESERVE.
- **reopen condition:** explicit contradictory primary evidence only.

## IP-BRANCH-KOH-019 — uncertainty causes downgrade

- **claim:** when option status is uncertain, the claim receives lower authority.
- **scope:** epistemic control.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **preferred label:** `BRANCH_STATUS_UNRESOLVED` until provenance is recovered.

## IP-BRANCH-KOH-020 — voice modeling must carry branch status

- **claim:** selectable lines can be used for expressive-range modeling only with their source status preserved.
- **scope:** P2-F.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **reason:** branch material is especially valuable for register variation, but dangerous if treated as one transcript.

## IP-BRANCH-KOH-021 — stable character is core plus recurrent tendencies

- **claim:** Makino's current character model is fixed core + cross-branch recurrent compatible tendencies, not union-all routes.
- **scope:** character reconstruction.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **canonical relationship to P2-A2:** clarifies rather than revises the thirty Makino claims.

## IP-BRANCH-KOH-022 — alternate routes remain analytically useful

- **claim:** no-mainline-authority does not mean no analytical value.
- **scope:** possibility-space.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **uses:** genre conventions, counterfactual relationships, boundary testing, expressive range.

## IP-BRANCH-KOH-023 — later fixed evidence promotes traits carefully

- **claim:** later fixed corroboration can promote a trait without retroactively making an optional event happen.
- **scope:** revision behavior.
- **epistemic class:** INTERPRETATION.
- **transition state:** STRENGTHEN.
- **example:** if a later fixed scene says Makino likes a food that one optional reply also named, the preference may become fixed; the earlier optional conversation does not thereby become branch-invariant history.

## IP-BRANCH-KOH-024 — semantic gate closes here

- **claim:** P2-A3 supplies sufficient branch-canon discipline for P2-B character ledgers to proceed.
- **scope:** project architecture.
- **epistemic class:** INTERPRETATION.
- **transition state:** PRESERVE.
- **limitation:** exact control-flow locator recovery remains an evidence-infrastructure enhancement and may be reopened when upstream source metadata becomes available.

---

# 17. Operational decision tree

For every future `Manager (player)` line, apply this order.

## Step 1 — identity

Does the source present the continuing Hoshimi manager with Makino's fixed history/role?

- **Yes** -> `MAKINO_KOUHEI_CONTINUITY`.
- **No / contradictory primary evidence** -> open `CONTINUITY_TENSION` and stop automatic inheritance.

## Step 2 — interface

Is the only variation `{user}` or editable naming?

- **Yes** -> `INTERFACE_PARAMETERIZATION`.

## Step 3 — source structure

Is the line fixed, or securely identified as selectable/alternate?

- fixed -> `BRANCH_INVARIANT`;
- selectable -> `PLAYER_SELECTED`;
- explicit bad/alternate route -> `BRANCH_ONLY` plus continuity caveat;
- cannot tell -> `BRANCH_STATUS_UNRESOLVED`.

## Step 4 — consequence

Does the source demonstrate a fixed consequence regardless of option?

- **Yes** -> record consequence separately as branch-invariant.
- **No** -> keep downstream state branch-local.

## Step 5 — characterization

Does the same trait recur independently across alternatives?

- **Yes** -> may promote the shared trait to `CROSS_BRANCH_RECURRENT_TRAIT`.
- **No** -> keep the trait route-local.

## Step 6 — romance / ethics escalation

Would the line establish romance, sexual interest, serious professional misconduct, or another load-bearing state?

- **Yes** -> require exact branch locator or fixed corroboration before mainline use.

## Step 7 — downstream citation

Every synthesis that relies on optional material must preserve:

- source/story ID;
- branch status;
- known option/route locator if available;
- whether the claim is possibility-space, recurrent trait, or fixed consequence.

---

# 18. Required downstream field set

When branch-bearing Makino evidence is used in later ledgers, include:

```yaml
manager_identity: MAKINO_KOUHEI_CONTINUITY
manager_branch_status: IDENTITY_INVARIANT | BRANCH_INVARIANT | PLAYER_SELECTED | INTERFACE_PARAMETERIZATION
branch_analysis_status: FIXED | CROSS_BRANCH_RECURRENT_TRAIT | BRANCH_ONLY | BRANCH_STATUS_UNRESOLVED | NO_MAINLINE_CONTINUITY_AUTHORITY
branch_group_id: null  # populate only when actually recovered
branch_option_id: null # populate only when actually recovered
fixed_event_consequence:
impossible_cooccurrence_with: []
trait_promotion_status: NONE | RECURRENT_TRAIT_ONLY | PROMOTED_BY_LATER_FIXED_SOURCE
relationship_state_authority: NONE | POSSIBILITY_ONLY | FIXED
source_story_id:
source_path:
notes:
```

`null` is preferable to an invented option identifier.

---

# 19. Branch evidence register for the locked snapshot

| Source region | Current branch-canon status | Main use | Limitation |
|---|---|---|---|
| Anime E01-E12 | branch problem not applicable to ordinary dialogue | fixed Makino audiovisual characterization | anime prospective boundary must remain intact |
| Hoshimi `st-original-cmn` | large `IDENTITY_INVARIANT` + `BRANCH_INVARIANT` substrate; some branch-parameterized expression possible | Makino biography, POV, professional reasoning | flattened dialogue does not preserve universal option IDs |
| Mana origins | overwhelmingly fixed historical/relationship evidence | Mana/Makino history and professional formation | chronology/disclosure rules still apply |
| later main story | fixed Makino professional substrate plus any locally identified branch expression | professional development | exact option status must be source-grounded |
| cards | mostly fixed story scenes; player-facing expressions require local source check | character/relationship/professional texture | do not infer branch from `選択肢` vocabulary inside dialogue |
| messages | **known high-risk `PLAYER_SELECTED_MAKINO_EXPRESSION` layer** | relationship register, ordinary-life texture, situational voice | published aggregate does not universally label option groups |
| bonds | fixed story substrate with local player-interface risk | relationship development | preserve source-specific branch status |
| specials/misc ordinary | source-specific | texture / formal / comedy | parody/seasonal authority separately controlled |
| `st-love-23-0514-007-bad` | `BRANCH_ONLY` / `NO_MAINLINE_CONTINUITY_AUTHORITY` | explicit alternate Makino/Rei romance possibility | must not be exported to mainline |
| `{user}` everywhere | `INTERFACE_PARAMETERIZATION` | display name only | no identity divergence |

---

# 20. Open branch register

## `OPEN_BRANCH_CONTROL_FLOW_LOCATOR_RECOVERY`

**Status:** OPEN / NONBLOCKING FOR P2-B.

**Problem:** The mirrored ingest and analysis-bundle projections preserve text and source paths but do not expose universal original branch group/option fields. Exact enumeration of every selectable reply with provider-native control-flow IDs cannot be certified from this snapshot alone.

**Required future evidence:** upstream `script.jsonl` / scenario control-flow metadata or a regenerated ingest that preserves option-group and option-ID fields.

**Do not do:** infer IDs from sequence numbers, timestamps, line adjacency, or semantic guesswork.

## `OPEN_EXHAUSTIVE_MESSAGE_OPTION_GROUPING`

**Status:** OPEN / NONBLOCKING.

The message corpus is known to contain player-selectable replies, but the current aggregate representation is insufficient to certify all individual option groupings automatically.

This does not invalidate Phase-1 message routing. It limits how exact Makino reply text may be promoted to fixed character evidence.

## `OPEN_RUI_MAKINO_POST_RECOGNITION_OUTCOME`

**Status:** OPEN FORMAL DEPENDENCY.

This remains governed by the unavailable `tel-card-rui-05-fest-04` asset. P2-A3 does not change it.

## Identity continuity tension

**Status:** NONE CURRENTLY ESTABLISHED.

Reopen only for contradictory primary evidence.

---

# 21. What P2-A3 changes from P2-A2

P2-A3 **does not revise** the substantive thirty-claim Makino longitudinal model.

It strengthens its source semantics.

### P2-A2 said

- Makino is a fixed character before he is a branch surface;
- selectable expressions cannot be unioned into one biography;
- exact branch semantics belong here.

### P2-A3 now specifies

- the canon stack;
- promotion/demotion rules;
- impossible co-occurrence;
- branch convergence;
- message-layer caution;
- romance safeguards;
- professional-boundary safeguards;
- false-positive handling;
- cross-media/branch separation;
- explicit alternate-route handling;
- downstream field requirements;
- the precise source-projection limitation preventing invented branch IDs.

The result is enough to begin unit-by-unit character ledgers without treating Makino as either an empty avatar or an impossible union of all replies.

---

# 22. P2-A3 completion gate

| Gate | Requirement | Result |
|---|---|---|
| A3-01 | Makino identity fixed without reopening absent contradiction | **PASS** |
| A3-02 | branch-invariant facts/actions distinguished | **PASS** |
| A3-03 | player-selected expressions distinguished | **PASS** |
| A3-04 | repeated cross-branch trait promotion rule defined | **PASS** |
| A3-05 | branch-only trait/action rule defined | **PASS** |
| A3-06 | impossible co-occurrence rule defined | **PASS** |
| A3-07 | `{user}` parameterization classified | **PASS** |
| A3-08 | genuine continuity-tension trigger defined | **PASS** |
| A3-09 | explicit alternate/bad branch tested | **PASS** |
| A3-10 | romance and professional-boundary safeguards tested | **PASS** |
| A3-11 | cross-media variant separated from player branch | **PASS** |
| A3-12 | exact branch locator integrity | **PASS WITH EXPLICIT LIMITATION** — unavailable IDs are left null rather than invented |
| A3-13 | downstream P2-F/P2-C routing defined | **PASS** |
| A3-14 | semantic branch-canon gate sufficient for P2-B | **PASS** |

Overall:

> **`PASS_WITH_EXPLICIT_BRANCH_LOCATOR_LIMITATION`**

This limitation is provenance-specific, not a substantive uncertainty about whether the game manager is Makino or whether all selectable replies can be merged.

---

# 23. Next architecture-defined operation

P2-A foundational character work is now complete:

- P2-A1 — Mana longitudinal ledger — complete;
- P2-A2 — Makino longitudinal ledger — complete;
- P2-A3 — Makino player-branch canon ledger — complete.

Proceed to:

> **P2-B1 — SUNNY PEACE character longitudinal ledgers**

Recommended first artifact:

`IDOLY_PRIDE_V2_CHAR_SAKURA_LONGITUDINAL_LEDGER.md`

Sakura's ledger should inherit P2-A3 whenever Makino dialogue is used, so fixed managerial behavior and player-selected expression never become conflated.

Recommended execution environment:

- **Model:** GPT-5.6 Sol
- **Reasoning:** Extra High

---

# 24. Compact retrieval rule

For future agents, the entire P2-A3 result can be compressed to this:

> **Makino is fixed; his interface is partly selectable. Treat fixed history/narration/actions as canon. Treat selectable replies as authored Makino-compatible possibilities. Promote only independently repeated underlying traits, never mutually exclusive wording. Keep route-only events route-only. `{user}` is a name parameter. Alternate/bad routes are analytical possibility-space, not mainline history. If branch metadata is missing, downgrade and leave the locator null rather than guessing.**

