---
series: WUWA
character: Shorekeeper
artifact_type: battle_embodiment_and_limit_language_profile
scope: SHOREKEEPER_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: SHOREKEEPER_PRE_AV_V0_1
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

# Shorekeeper — battle injury, pain and operational-limit language, pre-listening

The archive's eight Hit/Injured/Fallen entries `FavorWord_150545–150552_Content` are playable-character combat-response records, not a dated conversation. Their pinned `favorword.json#/1520–1527` rows each carry an explicit Wwise event path; the selected line analysis maps each to four localized text witnesses and four PCM-valid EN/JA/KO/ZH renders with event and numeric-media IDs. These joins establish recoverable sound objects, **not** an observed performance, an event-to-bank proof for every object, or a story chronology. The record makes a narrower literary contribution: Shorekeeper may name a bodily feeling and still use technical language for damage and limits. Neither vocabulary cancels the other [SHK-E01, E05, E08, E30; SHK-C02, C27].

| Archive key / source row | In-source trigger label | Four-text reading and model limit |
|---|---|---|
| `FavorWord_150545_Content`; `favorword#/1520` | Hit I | Brief reassurance that she is all right. This is a momentary utterance, not a medical clearance or proof every following hit is harmless. |
| `FavorWord_150546_Content`; `favorword#/1521` | Hit II | ZH names the *feeling* of pain; EN's pause and JA/KO's demonstrative phrasing can make it sound like recognition. No recorded chronology says this is the first pain she has ever felt. |
| `FavorWord_150547_Content`; `favorword#/1522` | Injured I | ZH/KO refer to bodily damage; EN calls it physical damage detected, JA specifies machine/body damage. The nouns differ in technicality but all identify a harmful state, not an absence of sensation. |
| `FavorWord_150548_Content`; `favorword#/1523` | Injured II | ZH speaks of reduced usability, JA of reduced function, KO of reduced operating rate, EN of lower durability. English's durability is not a four-language anatomical or mechanical specification. |
| `FavorWord_150549_Content`; `favorword#/1524` | Injured III | ZH/EN/JA warn against interference or obstruction; KO instead says she cannot fail. Do not impose one universal addressee or turn the Korean resolve into a cross-dub command to bystanders. |
| `FavorWord_150550_Content`; `favorword#/1525` | Fallen I | All four deny that this is the end. A combat fall is not automatically a lore-confirmed resurrection or permanent death. |
| `FavorWord_150551_Content`; `favorword#/1526` | Fallen II | She asks the addressee not to grieve. This addresses another person's feeling; it does not prove she cannot be hurt or that mourning for her is irrational. |
| `FavorWord_150552_Content`; `favorword#/1527` | Fallen III | ZH/JA/KO describe reaching or exceeding a limit; EN renders depletion as durability. This is an operational failure phrase in a gameplay slot, not a complete account of crystal dissipation or Tethys repair. |

## What this changes about embodiment

The [central analysis](WUWA_SHOREKEEPER_CHARACTER_DEEP_DIVE_PRE_AV.md) already separates Shorekeeper's constructed crystal origin, painful core service, projection-era limitations and postrepair access to sun and sea. These battle lines add a different kind of evidence: she has a combat register in which a hurt can be a *feeling*, a damaged body can be assessed by function, and a fall can prompt reassurance directed outward. The source does not need to call her ordinarily human for the pain line to matter. Nor should an EN term such as “durability” make her only replaceable hardware. Her profile certification reports dissipation, crystal replacement and monitoring risk; `FavorStory_150504_Content` argues that a duplicate with the same material could not simply substitute for her continuity. The combat lexicon fits a materially vulnerable person who also has technical knowledge of her body. It does not settle the mechanism of pain or how much each line belongs to an early versus postrepair state.

The eight entries should not be placed in a developmental sequence because their numerical order is a menu/list order under trigger categories, not a timeline. A model should not say she first discovers pain at Hit II, learns to say “body damage” only after that, and becomes emotionally protective at Fallen II. The same character can use these registers under different pressure and addressees. Conversely, a single isolated “I'm fine” must not nullify the other seven. In a hypothetical fight, she may make a quick functional assessment, protect someone, acknowledge a limit and still want them not to suffer; which line would actually trigger is a game-state question not answered by the packet.

The fallen reassurance also interacts with the deep-shore self-exclusion question without solving it. At `flow#/4198/2/24–26`, a no-more-harm promise and her proposed sole core cost stand together, but the promise's scope is unresolved. “Do not grieve for me” in a separate battle slot could be protective reassurance, self-minimization, tactical composure or several things at once. It cannot adjudicate that she knowingly excluded herself from welfare, secretly sought injury or considered herself unreal. Delone's bedside memory and Black Shores memorial stars show that she treats others' grief as substantial; they do not tell us whether the fallen line is gentle, automatic, strained or ironic in any dub. Only an exact-render four-language listen and, for live combat, a contextual capture could test delivery. Neither has been performed here [SHK-E04, E15, E25, E30; SHK-C15, C23, C27].

## Retrieval and falsification controls

For a bounded human review, retrieve the exact five-line contrast `150546–150548`, `150551–150552` from the [AV crosswalk](../03%20Audiovisual%20and%20Voice/WUWA_SHOREKEEPER_AV_HUMAN_RETRIEVAL_CROSSWALK.md), not by a friendly audio stem alone. Each source row has an explicit event path and four render associations; the private `COMPLETE_VOICE_LINE_ANALYSIS.jsonl` preserves semantic occurrence ID, source locator, language, runtime render variant, event ID, numeric media ID, WEM/PCM/FLAC hashes and local path. Preserve short-bark timing, channel and in-game trigger. Do not compare levels as if different dubs had common mastering, or infer a stable “robotic” versus “human” acting mode from a single damage call. JA's more mechanical Injured I and EN's durability noun are textual contrasts to be checked in performance, not a reason to recode Chinese as machine speech.

This reading would need revision if an exact source ties particular barks to a dated form/state, if a translation or attribution row changes, or if reviewed runtime/video shows a different speaker or use. The present text and render joins already reject two shortcuts: that she is invulnerable because she reassures others, and that a technical damage noun proves she lacks painful experience or personhood. They do **not** establish the reverse shortcuts of normal human physiology, permanent death at a fall, or a fully heard emotional performance. Keep this as a draft semantic and retrieval profile until those witnesses exist.
