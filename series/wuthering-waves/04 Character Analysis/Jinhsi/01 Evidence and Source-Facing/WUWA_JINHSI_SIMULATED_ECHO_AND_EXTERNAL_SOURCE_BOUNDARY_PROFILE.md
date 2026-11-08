---
series: WUWA
character: Jinhsi
artifact_type: source_scene_specialist
analytical_responsibility: "Keep the Tethys-simulated Jinhsi image and external-source audio aliases separate from embodied character action and proved four-dub performance"
scope: JINHSI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: JINHSI_PRE_AV_V0_1
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

# Jinhsi's image is not automatically Jinhsi

The optional `剧情_团团团团转` event contains a useful test of this packet's source hierarchy. At `flow#/7844/1`, ten technical-speaker-186 text turns are accepted by the character-occurrence crosswalk; nine are `PlayVoice=true` and one ellipsis at T11 is not voiced. Yet contextual T6–7 explicitly say the Echo Cube's memory was simulated to match the spring of an earlier meeting and that the Cube image was simulated by Tethys; it feels much like the real Jinhsi. The distinction is written in the scene itself. An accepted source speaker label and lore-entity association can be correct for retrieving a *Jinhsi-like representation* without proving that the embodied magistrate is present or personally made every offer [JIN-E37].

The scene lets the simulated figure act in ways recognizable from stronger direct Jinhsi sources. At T4–5 she asks where Sanhua, Taoqi and Jiyan are and whether Jinzhou can run its emergency plan if important officeholders are trapped. After another speaker assures her that people outside are unaffected, T9 still treats the immediate cake crisis as urgent. At T12–13 she suggests seeing the place together *after* the crisis and says Rover needs rest. These are coherent **lines written for an image of Jinhsi**: public-resource awareness, practical division of labor, and conditional leisure coexist. They do not establish that actual Jinhsi knew this event occurred, personally promised Rover a walk, or formed a new romance. Even the reassurance that the outside is safe is a character's statement in a simulated-event context, not independently inspected operational status [JIN-E03, E09, E16, E37; C36].

The named later state `flow#/8329/1` contains seven more technical-speaker-186 voiced turns. The figure volunteers to repair the cake while Rover confronts Abbowser, says too much idleness would feel awkward, asks whether Rover has always been busy saving others, and proposes that Abbowser's confinement may be a temporary respite from mission. This is a *question and hypothesis*, not a solved motive or proof that the confinement is benign. Because `8329/1` shares the event family but its exact transition from `7844/1` is not proved by the retained action rows or an exact-state quest join, a runtime route remains open. Even if a capture confirms one path, it would show an in-world image's words, not transform them into the original Jinhsi's remembered private thoughts [JIN-E37; C36].

## Four texts, not four proved dubs

The sixteen source-voiced turns across those two actions produce 64 language-labeled render **associations** in the current complete voice-line analysis. For every one of these semantic lines, the EN/JA/KO/ZH render rows point to the same `WwiseExternalSource/gl_vo_*.wem` virtual path and have the same decoded PCM SHA-256. Two lines in the pair even reuse another line's object, leaving fourteen distinct PCM objects across the sixteen text keys. There is no evidence here for 64 independently localized performances. A successful PCM/FLAC roundtrip authenticates the decoded bytes of each object but not the language assignment, the intended text, or the event's played dispatch. Numeric event/media IDs are not populated for these lines [JIN-E38].

Four exact text-key/path disagreements sharpen the risk. `TZZNQ_7_4` describes the cake escape plan in ZH but its render rows point to `gl_vo_TZZNQ_77_3.wem`, whose separately keyed text is about duty and feeling at a loss when idle. `TZZNQ_7_7` asks about Jinzhou's emergency plan but points to `gl_vo_TZZNQ_77_9.wem`, whose keyed text speculates about Abbowser's motive. `TZZNQ_7_16` proposes a later stroll but points to `gl_vo_Side_TZJNSC_2_3.wem`, whose keyed text is a formal self-introduction; `TZZNQ_7_17` is the rest suggestion but points to `gl_vo_Side_TZJNSC_2_2.wem`, whose keyed text says the two kept an appointment. It is possible that the client's runtime dispatch uses a mechanism not represented by these friendly paths. It is **not** sound to label the retained PCM as a proved recording of the mismatched current line without container-level and listening evidence. The wider audit flags 31 Jinhsi lines and 224 lines across seven packet characters with the same four-label/one-PCM pattern [JIN-E38].

The localized *text* does permit a limited reading. At `TZZNQ_7_16`, ZH's “go around together” is somewhat open; EN and KO call it a stroll, while JA explicitly says to look around this Sonoro together. At `TZZNQ_77_3`, the figure describes duty and discomfort with inactivity, with JA making inability to settle without doing something more direct. Those differences are features of textual rendering for a simulated image. They cannot be translated into claims that the original Jinhsi has a uniquely Japanese inner compulsion, that the invitation is a canon date, or that the four dub actors perform the same moment differently [JIN-E37–E38; C36].

## Modeling and retrieval use

A reconstructive model should take `diegetic_instantiation` as an explicit input: actual Jinhsi, memory/Echo-Cube simulation, other projection or unknown. The event portrayal can be used as a lower-authority consistency probe: does a hypothetical image plausibly echo actual Jinhsi's documented public-duty and rest/care motifs? It should **not** become a new first-person biographical fact, an actual relationship state, or an acoustic personality feature. The corpus keeps the semantic occurrence IDs and text witnesses, while performed-voice comparisons for these lines remain `language_dispatch_unresolved`. A future bounded test should inspect exact installed package/container identities for the same virtual `gl_vo_` member under each language pack, then capture a small controlled runtime language switch or equivalent verified playback. Record the actual played source object, render hash, text/voice match and whether the scene's character is explicitly described as simulated. No such test has yet been completed [JIN-E37–E38; C36].
