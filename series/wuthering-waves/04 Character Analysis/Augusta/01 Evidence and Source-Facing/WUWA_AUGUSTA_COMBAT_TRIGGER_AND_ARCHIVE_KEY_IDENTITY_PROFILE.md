---
series: WUWA
character: Augusta
artifact_type: character_specialist_profile
analytical_responsibility: "Keep combat-trigger text, raw archive IDs, localized Content keys and four-dub media identities distinct from dated character claims"
scope: AUGUSTA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: AUGUSTA_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Augusta — combat dispatch, archive-key identity, and the limits of a battle cry

The pinned `character_source_package.json` has **68** Augusta favor-word rows. Thirty-seven raw IDs in its combat, damage, traversal and reward portion differ from the numeric suffix of their actual `Content` text key. This is not a missing-text or missing-audio problem. All 37 source rows join by exact `favorword.json` locator and raw `Content` field to 37 complete semantic voice rows, with 148 four-language render associations, 148 distinct canonical PCM objects and 37 event IDs; all 148 have `flac_roundtrip_pcm_identical` status in the local restricted corpus. That is a technical source/media result, not proof of how any actor delivered a bark, how frequently it plays, or which event fired in a particular game session. The [packet validator](../04%20Validation%20and%20Readiness/reproduce_validation.py) checks the join; the [AV crosswalk](../03%20Audiovisual%20and%20Voice/WUWA_AUGUSTA_AV_HUMAN_RETRIEVAL_CROSSWALK.md) remains a selective listening plan, not an exhaustive combat review.

`favorword#/N` means `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/favor/favorword.json#/N`. A suffix `X` in the table means the **actual** localized key `FavorWord_X_Content`, not a number inferred from the raw row ID. The trigger is the pinned EN *title* metadata; it does not establish runtime frequency or a canonical story moment. Full localized lines and media remain in the local source/voice planes, outside this analytical Git draft.

| Raw row ID | Actual Content suffix | Exact source position | Trigger class |
|---:|---:|---:|---|
| 130632 | 130634 | `favorword#/2506` | Heavy Attack |
| 130633 | 130635 | `#/2507` | Resonance Skill I |
| 130634 | 130636 | `#/2508` | Resonance Skill II |
| 130635 | 130637 | `#/2509` | Resonance Skill III |
| 130636 | 130638 | `#/2510` | Resonance Skill IV |
| 130637 | 130639 | `#/2511` | Resonance Skill V |
| 130638 | 130640 | `#/2512` | Resonance Skill VI |
| 130639 | 130641 | `#/2513` | Resonance Liberation I |
| 130640 | 130642 | `#/2514` | Resonance Liberation II |
| 130641 | 130643 | `#/2515` | Resonance Liberation III |
| 130642 | 130667 | `#/2516` | Resonance Liberation IV |
| 130643 | 130668 | `#/2517` | Resonance Liberation V |
| 130644 | 130669 | `#/2518` | Resonance Liberation VI |
| 130645 | 130632 | `#/2519` | Resonance Liberation VII |
| 130646 | 130633 | `#/2520` | Resonance Liberation VIII |
| 130647 | 130644 | `#/2521` | Intro Skill I |
| 130648 | 130645 | `#/2522` | Intro Skill II |
| 130649 | 130646 | `#/2523` | Intro Skill III |
| 130651 | 130648 | `#/2524` | Intro Skill IV |
| 130652 | 130649 | `#/2525` | Intro Skill V |
| 130653 | 130650 | `#/2526` | Hit I |
| 130654 | 130651 | `#/2527` | Hit II |
| 130655 | 130652 | `#/2528` | Injured I |
| 130656 | 130653 | `#/2529` | Injured II |
| 130657 | 130654 | `#/2530` | Fallen I |
| 130658 | 130655 | `#/2531` | Fallen II |
| 130659 | 130656 | `#/2532` | Fallen III |
| 130660 | 130657 | `#/2533` | Echo Summon |
| 130661 | 130658 | `#/2534` | Echo Transform |
| 130662 | 130659 | `#/2535` | Enemies Near |
| 130663 | 130660 | `#/2536` | Glider |
| 130664 | 130661 | `#/2537` | Sensor |
| 130665 | 130662 | `#/2538` | Dash |
| 130666 | 130663 | `#/2539` | Supply Chest I |
| 130667 | 130664 | `#/2620` | Supply Chest II |
| 130668 | 130665 | `#/2621` | Supply Chest III |
| 130669 | 130666 | `#/2622` | Supply Chest IV |

The order is nonmonotonic: raw `130642` points to key `_130667`, then raw `130645` points back to `_130632`; there is no raw row `130650` in this set even though `_130650_Content` is the text key for Hit I at `#/2526`. The final three supply-chest rows are at `#/2620–2622`, not the next three indices after `#/2539`. Joining `FavorWord_{Id}_Content` can return another *valid but wrong* Augusta line, so a zero-missing-key check is inadequate. For example, raw `130645` is Liberation VII at `#/2519` but its actual key is `FavorWord_130632_Content`; `_130645` belongs to Intro Skill II at `#/2522`. A voice lookup must preserve raw ID, exact locator, raw `Content`, semantic occurrence ID, event path/ID, language-specific media ID and PCM/FLAC hashes as different fields. No friendly filename or integer arithmetic substitutes for that chain.

## What the trigger classes can and cannot say about character

**Conquest and royal language are battle-address compression.** Heavy Attack at `#/2506` calls to victory; the skills and Liberations at `#/2507–2520` include Septimont, glory, a ruler's path and several short claims of dominance. Raw `130639`/actual `_130641_Content` says more in EN's tautological “Rulers rule. Winners win” than the ZH line, which joins a kingly way to an earned victory; JA and KO also handle that premise differently. A model should not turn the EN bark into Augusta's considered theory of legitimate government. Her [ascension IV argument](WUWA_AUGUSTA_ASCENSION_SWORD_RULES_AND_SUCCESSION_PROFILE.md), the arena's nonlethal intervention (`FavorStory_130602_Content`) and her postvictory sharing of heroic credit (`flow#/8422/2`) are fuller, differently situated tests of what winning should authorize [AUG-E04, E19, E28]. Nor should those sources erase a genuine martial pride that the barks express. The bounded claim is that the battle register can sound more absolute than the story's governing ethic; not that one side is fake.

**The target and the ally are not the same listener.** Intro Skill III, raw `130649`/key `_130646_Content` at `#/2523`, invites another to fight at her side. Intro Skill V, raw `130652`/key `_130649_Content` at `#/2525`, honors a “friend” in all four witnesses, though the literal wording differs. These are dispatch barks associated with team-entry triggers; the source row does not name a unique partner, prove which player character was present, or establish an exclusive relationship with Rover. They do add a reusable *situational* social register beside her challenger's boasts. In a hypothetical scene, a known friend may receive martial respect; a stranger should not inherit an observed joint history merely because a generic team bark exists [AUG-C08, C11, C16].

**Being injured or falling is not a recorded death wish.** Raw `130655–130656`/keys `_130652–130653_Content` minimize pain and urge endurance under damage. Raw `130657–130659`/keys `_130654–130656_Content` are labeled Fallen I–III. The last ZH/EN/JA witness frames the line as advance-or-die/fight-or-fall; KO intensifies the deathward wording. This is a localization-sensitive *failure-state* utterance, not a dated decision to seek death, evidence that her sun is literally immortal, or proof she fell at a specific quest climax. The boast that pain barely registers is likewise not physiological immunity. Her childhood fear and defeats, later burden of public invincibility, and open post-victory future remain the relevant narrative controls [AUG-E02–E04, E07, E19]. A future performed-voice judgment would first have to listen to the exact render and identify the gameplay trigger.

**Traversal and loot are not policy scenes.** `#/2533–2538` includes command, control, awareness, distance and protection cues associated with Echo, enemy, glider, sensor and dash triggers. `#/2539` and `#/2620–2622` acknowledge loot in a hunt/supply-chest register. The source class does not demonstrate that she personally plundered a civilian, funded Septimont from chests, traveled to the sea in a dated story scene, or would speak that way at a diplomatic dinner. Conversely, removing these cues altogether would make the model unable to shift from magistrate-like reflection to practical field action. Their right use is conditional on encounter and trigger state, not global personality.

The direct future test is a four-dub **line-and-trigger** listen, not a sentiment score. Nominate `#/2513` for the royal-claim localization hinge, `#/2523` and `#/2525` for ally address, `#/2528–2532` for injury/fallen rhetoric, and `#/2622` for a reward-state control. Join each by locator and actual Content key into `COMPLETE_VOICE_LINE_ANALYSIS.jsonl`; record the semantic occurrence and every render variant, event path, numeric media ID, source WEM/hash and canonical PCM/FLAC hash before playback. Then log audible time span and whether the game triggered it as labeled. All 37 rows have complete local four-dub media joins, but no human four-dub listening or runtime dispatch observation is claimed here. None of these nominations has been added to the eighteen-case selected metadata JSON, so its 18/72 denominator remains unchanged. A direct source showing a bark reused in a different state, or a later scene endorsing the same rhetoric as explicit civic policy, could revise the narrow interpretation without changing the pinned row identities.
