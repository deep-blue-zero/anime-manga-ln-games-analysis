---
series: WUWA
character: Zani
artifact_type: character_specialist_profile
analytical_responsibility: "Resolve the rotated archive skill keys and bound labor, force, defeat and efficiency claims by four-language text and gameplay trigger"
scope: ZANI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: ZANI_PRE_AV_V0_1
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

# Zani — the combat shift is not her employment contract

The pinned `character_source_package.json` has 72 Zani favor-word rows; all 72 join complete semantic voice records by exact `BinData/favor/favorword.json` locator and actual raw `Content` key, with 288 distinct four-dub PCM-valid renders. The 41 basic attack through supply-chest rows at raw IDs `150732–150772`, locators `favorword#/2193–2233`, contribute 41 explicit events and 164 distinct four-dub PCM objects **inside** that archive total and the packet's 912-line/3,517-object selected corpus. They are gameplay trigger addresses, not a new dated story-action cohort. Event/bank/media fields here are retained from the established local voice mapping; this profile does not independently parse Wwise banks, reproduce runtime playback or report human listening.

Seventeen consecutive raw IDs `150737–150753` do **not** name their own `Content` key. Skill I–IX and Liberation I–VI use a two-position key rotation, with the two Intro Skill rows wrapping to the vacated keys. Thus raw `150748` is Liberation III with actual `FavorWord_150750_Content` at `favorword#/2209`, while guessed `FavorWord_150748_Content` belongs to **Liberation I** at `#/2207`. Both are valid Zani lines and sound objects. A key-exists check would pass the wrong join. Preserve raw ID, exact row locator, raw `Content`, title/trigger, `RoleId: 1507`, event path and numeric ID, semantic occurrence ID, language-specific bank/media/render IDs and WEM/PCM/FLAC hashes independently. No arithmetic offset is an acceptable substitute for the source fields at the wrap.

`favorword#/N` in the table expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/favor/favorword.json#/N`. Every key shown is the raw `Content`, not one generated from the raw `Id`.

| Raw ID | Actual Content key | Source row | Raw EN trigger | Event ID |
|---:|---|---|---|---:|
| `150737` | `FavorWord_150739_Content` | `#/2198` | Resonance Skill I | `2045981504` |
| `150738` | `FavorWord_150740_Content` | `#/2199` | Resonance Skill II | `1196901668` |
| `150739` | `FavorWord_150741_Content` | `#/2200` | Resonance Skill III | `1196901671` |
| `150740` | `FavorWord_150742_Content` | `#/2201` | Resonance Skill IV | `1196901670` |
| `150741` | `FavorWord_150743_Content` | `#/2202` | Resonance Skill V | `908924405` |
| `150742` | `FavorWord_150744_Content` | `#/2203` | Resonance Skill VI | `908924406` |
| `150743` | `FavorWord_150745_Content` | `#/2204` | Resonance Skill VII | `908924407` |
| `150744` | `FavorWord_150746_Content` | `#/2205` | Resonance Skill VIII | `3387598989` |
| `150745` | `FavorWord_150747_Content` | `#/2206` | Resonance Skill IX | `3387598988` |
| `150746` | `FavorWord_150748_Content` | `#/2207` | Resonance Liberation I | `2452822985` |
| `150747` | `FavorWord_150749_Content` | `#/2208` | Resonance Liberation II | `2452822986` |
| `150748` | `FavorWord_150750_Content` | `#/2209` | Resonance Liberation III | `2452822987` |
| `150749` | `FavorWord_150751_Content` | `#/2210` | Resonance Liberation IV | `2371488700` |
| `150750` | `FavorWord_150752_Content` | `#/2211` | Resonance Liberation V | `2371488703` |
| `150751` | `FavorWord_150753_Content` | `#/2212` | Resonance Liberation VI | `2371488702` |
| `150752` | `FavorWord_150737_Content` | `#/2213` | Intro Skill I | `2217898941` |
| `150753` | `FavorWord_150738_Content` | `#/2214` | Intro Skill II | `2217898942` |

## Labor words under different source conditions

**Clock-out as a battle quip, not a universal refusal.** Liberation III at raw `150748`/actual `_150750_Content` has ZH “come together; don't delay my clocking out,” JA “it's almost leaving time,” KO “it's almost time to leave,” and the stronger EN “I don't do overtime.” The shared speaking action is an impatient challenge to combat opponents, with EN making the labor rule more categorical. It cannot erase Zani's ordinary archive statement that she does not dislike *meaningful* work or overtime (`FavorWord_150703_Content`), her later offer to stay longer for Carlotta (`flow#/9968/2`), or the distinct observation of actual paid leave (`12439/7`). Nor does it prove she actually rejected an assigned shift in a dated scene. Liberation IV's report-writing and V's “finished, off work” continue the battle-as-work joke; they do not date a completed bank shift. The English VIII–IX skill commands intensify removal and dust imagery, but a hit/target/outcome needs runtime or story evidence, not a command bark [ZAN-E08 E20 E24 E37–E38; ZAN-C02 C05 C35–C36].

**Efficiency depends on the task and language.** Dash raw `150769`/actual `FavorWord_150769_Content` at `favorword#/2230` says “efficiency above all” in EN and the compact Chinese maxim `效率至上`. JA says to move swiftly; KO says efficiency is important. A traversal trigger is too thin to make efficiency the master value in every private or civic decision. She criticizes empty work and declines to recommend a maximally efficient sightseeing checklist; she protects ordinary routines that are not themselves optimized away. Echo Transform raw `150765`/`#/2226` is likewise a temporary switch: EN says “I'm off duty, it's your turn,” ZH asks the Echo to let her leave work, JA briefly asks to switch, and KO asks it to cover the work for a moment. None is the later paid-leave scene or consent for another person to inherit her duties indefinitely [ZAN-E08 E23 E24 E30 E37 E39; ZAN-C01 C02 C37].

**Defense, defeat and justice are not guaranteed outcomes.** Injured I raw `150758`/`#/2219` speaks of the shield withstanding more in all four witnesses. It is a damage reaction, not a tested claim of invulnerability; the source already records injury and delayed rest. Fallen I raw `150761`/`#/2222` still refers to unfinished work, while Fallen III raw `150763`/`#/2224` looks toward justice. These defeat-class lines can inform a conditional battle register but do not prove canonical death, posthumous certainty, actual legal judgment or a private wish for endless labor. Talos's dated threat and subsequent civic repair remain the stronger actions for proportionality and consequence [ZAN-E06 E20–E24 E38; ZAN-C05 C18 C36].

## Negative controls and next observation

For a generated civilian or crossover scene, ask for **scene state, source surface, exact trigger, audience, stakes and language** before using a bark. A model fails if it selects a valid wrong skill by raw-ID-derived key, universalizes EN's no-overtime quip, makes a dash maxim override victim safety, treats a transformation as an actual holiday, or infers Talos was killed from dust/fallen wording. It also fails if it discards Zani's genuine capacity for force merely because game triggers do not prove their target. A better account permits curt impatience and work jokes in a fight while using her dated investigation, selective force, material restitution and actual leave for civic/ordinary behavior. The matrix and model must preserve both.

Nominate `#/2198` and `#/2213` as a **wrong-key control**, `#/2206` for the dust command, `#/2209` and `#/2210–2211` for the labor metaphor, `#/2219` for injury/shield, `#/2222–2224` for defeat, `#/2226` for a brief Echo switch, and `#/2230` for efficiency. Select each dub by semantic occurrence and runtime render variant; retain exact event/bank/media IDs, WEM/PCM hashes and source locator. Human four-dub listening should test audible wording and delivery, and runtime observation should establish which action fired, target and consequence. Neither has been done here. A later generation or contradictory scene would require a labeled source/claim revision, not silent reassignment of this frozen row map.
