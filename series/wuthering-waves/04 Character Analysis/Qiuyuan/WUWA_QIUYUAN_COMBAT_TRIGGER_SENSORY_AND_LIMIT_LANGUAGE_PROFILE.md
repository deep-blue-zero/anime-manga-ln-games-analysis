---
series: WUWA
character: Qiuyuan
artifact_type: combat_trigger_semantic_profile
analytical_responsibility: "Source-row-accurate four-language reading of battle, injury, fallen, and traversal archive voices"
scope: QIUYUAN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: QIUYUAN_PRE_AV_V0_1
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

# Qiuyuan — combat-trigger sensory and limit language

This is a four-language **text and provenance** reading of the 42 raw favor-word records from `Id` 141132 through 141174, except absent raw `Id` 141149. They span attacks, skills, liberation, entry, dodge, hit, injury, fallen, Echo, enemy-near, glider, sensor, dash, and supply-chest triggers. Every one joins to four locally materialized, PCM-roundtrip-identical dub renders: 42 source records, 42 semantic voice lines, 168 render associations. This does not establish how a player heard them in a particular battle, a dated story outcome, the actor's intent, or a listener's perception. No four-dub human listening or runtime combat capture was performed for this profile.

## The raw `Id` is not the text-key suffix

The [metadata-only crosswalk](FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json) joins all 73 archive records on the pinned `favorword.json` row locator, separately retaining raw `Id`, raw `Content` text key, source event path, event ID, and the matching semantic voice-line identity. **Thirty of 73 records have an `Id` whose number differs from the suffix of the actual `Content` key**; all thirty lie in this later trigger family. For example, raw `Id` 141162, labeled *Fallen: I*, lives at `favorword#/2683`, but its raw `Content` is `FavorWord_141157_Content`. Conversely, `FavorWord_141162_Content` is the *Enemies Near* text from raw `Id` 141167 at `favorword#/2688`. An `Id`-constructed text key would swap meanings even when it accidentally found a real key. The private voice-line analysis matches the actual `Content` field for all 73 rows by source locator; this is a source-schema irregularity, **not** evidence of 30 missing or wrongly decoded dub files. The crosswalk is reproducible by the packet validator from the frozen local package and voice analysis. Do not resolve battle text by raw `Id` or friendly title alone.

| Raw `Id` / trigger | Actual `Content` key and source row | Chinese-anchored content; localization check | Modeling limit |
|---|---|---|---|
| 141126 / Join Team III | `FavorWord_141126_Content`; `favorword#/2648` | He asks for the most dangerous place; EN similarly asks for dangers to be left to him. | A protective-risk invitation is not immunity, a guaranteed victory, or an order to abandon civilians. |
| 141141 / Skill III | `FavorWord_141141_Content`; `favorword#/2663` | `我听到你了` / “I hear you”; JA/KO also retain hearing. | A tactical auditory callout is not private-thought access. |
| 141142 / Skill IV | `FavorWord_141172_Content`; `favorword#/2664` | `剑及履及`; EN says “I move as the blade,” while JA/KO take different concise paths. | Neither a numbered key guessed from `Id` nor one English paraphrase establishes a universal movement law. |
| 141147 / Skill IX | `FavorWord_141173_Content`; `favorword#/2669` | `找到你了` / “Found you.” | Finding a combat target need not mean ordinary sight returned or the target's whole mind is known. |
| 141150 / Liberation I | `FavorWord_141145_Content`; `favorword#/2671` | `你的性命，我收下了` / an explicit life-taking threat in all four witnesses. | A combat bark supports lethal register, not proof that a named story target is actually killed. |
| 141157 / Hit I | `FavorWord_141152_Content`; `favorword#/2678` | `我听错了？` / “Did I mishear?”; JA/KO likewise question hearing. | The hit trigger is not evidence of a permanent sensory decline or a particular enemy's blow. |
| 141161 / Injured III | `FavorWord_141156_Content`; `favorword#/2682` | `舍身佯攻，亦须有度` warns that even a body-risking feint has limits; EN compresses this to “Feints demand restraint.” KO foregrounds bodily recklessness. | Do not replace the source's self-risk boundary with a painless invulnerability trait. |
| 141162 / Fallen I | `FavorWord_141157_Content`; `favorword#/2683` | `知遇之恩，来世……再报`; EN promises to repay trust in another life; JA/KO retain the later-life repayment. | Defeat-trigger gratitude does not date a canonical death, prove an afterlife, or give Rover ownership. |
| 141163 / Fallen II | `FavorWord_141158_Content`; `favorword#/2684` | `风……停了` / “The winds... settled.” | A wind image at defeat is not proof of a plot event or a stable acoustic motif without listening. |
| 141164 / Fallen III | `FavorWord_141159_Content`; `favorword#/2685` | `眼前只有……黑暗` / darkness before his eyes, echoed in EN/JA/KO. | It can resonate with established blindness without proving that sight was regained, lost again, or that he died in the story. |
| 141169 / Sensor | `FavorWord_141164_Content`; `favorword#/2690` | `我听到了` / “I hear it,” also auditory in JA/KO. | A sensor activation is a gameplay trigger, not a demonstration of omniscient Mindsight. |
| 141172 / Supply Chest I | `FavorWord_141167_Content`; `favorword#/2763` | `这个留给你吧` / he leaves the item to the addressee. | A practical allocation of loot does not establish exclusivity, romance, or a permanent provider role. |

The shorter attack and skill calls also resist a single “archaic warrior” template. Raw `Id` 141132–141135 uses compact and sometimes allusive Chinese phrasing; its first line's cup/call image is flattened to “Step forth” in EN while JA/KO retain a cup image. Other lines such as raw 141138's `势如破竹` are idiomatic across witnesses. Translators vary how much of that texture they retain. Without direct listening, a written line licenses observations about vocabulary and localization, not cadence, accent, breath, force, or the emotions assigned by an actor. The source-facing [speech profile](WUWA_QIUYUAN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) should keep live evacuation directives, reflective archive talk, and trigger-bark phrasing as different surfaces rather than averaging them into one speech style [QIU-E07/E20/E33; QIU-C15/C31].

## Behavioral synthesis and falsification

The triggering labels are analytically useful but carry different authority from a story scene. “Hit” and “Injured” imply a condition under which a bark might play, not an observed injury in the selected plot. “Fallen” means the game has a defeat/zero-health context for a playable character, not that the narrative confirms Qiuyuan's death or an afterlife. The three fallen texts are nevertheless informative as *available language*: repayment to a recognizer, wind cessation, and darkness. They put gratitude, environmental imagery and bodily limitation beside the practical commands and lethal threats, rather than replacing the latter. The self-risk limit in raw 141161 is particularly useful against a flat self-sacrificing-sword model: he can ask to take the dangerous position and still articulate a limit on reckless feinting. The exact magnitude or consistency of that limit in future action remains open.

The hearing calls in raw 141141, 141157 and 141169 are compatible with the source's bounded sensory practice, including frequency detection and read-aloud access, but cannot by themselves establish that he recognizes any concealed enemy, reads memories, or no longer needs medication. The dark-vision fallen line is a localized image under a defeat trigger, not clinical evidence. The lethal liberation call is genuine threatened wording, yet the story's Scar confrontation and reported escape remain better evidence for target-specific intent and outcome (`11919/1/14–16`, `11982/1/6–9`). Conversely, a source model that removes lethal language because he helps patients and civilians would also fail. A future falsification pass could check a captured battle for the correct trigger, exact source row, language and render variant, then compare the audible line against the text without assuming a story event. At present the source→event/media→PCM join is technically available, but event/bank playback semantics and performed meaning are not independently adjudicated here.
