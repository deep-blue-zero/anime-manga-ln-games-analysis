---
series: WUWA
character: Brant
artifact_type: echo_translation_puppet_troupe_aldric_intervention_profile
analytical_responsibility: "Separate admitted translation embellishment, an Echo/puppet-troupe localization fork, Aldric's coercion, and two player-choice graphs"
scope: BRANT_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: BRANT_PRE_AV_V0_1
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

# Brant — an embellished translation and an intervention that uses theatre

Two previously underused actions in the Brant character-line state family put a sharp limit on the simple claim that Brant is “a truthful captain beneath a playful mask.” No exact-state quest-node reference for these two states is retained in the selected `QUEST_CONTEXT_REFERENCES.jsonl`, so their runtime placement within the family is not pinned by that join alone. At `flow#/6820/2` he speaks for a Lottie Lost whose own utterances are short, then concedes that he embellished. At `flow#/6823/5` he hears Aldric promise riches by humiliating Ragunna nobles and ordering the capture of every nearby Echo; Brant's answer includes both a moral objection and a theatrical interruption. Neither action permits every tactical embellishment to be called harmless, nor every theatrical line to be treated as false. Exact recipient, speaker and branch matter [BRA-E39–E40].

## The short utterance and the large translation

The first action's technical speaker `100016` says “Lottie? Lost…” and later “Lost…” and “Lottie… Afraid…” in the English witness. Brant's named-speaker `1462` turn `Character_Brant_30_2` supplies a much more elaborate reported question about how a happy Lottie Lost can exist. The four localizations do not phrase that construction identically: Chinese asks how a “happy lonely lady” can be happy; Japanese asks what makes the glad Miss Lonely happy; Korean asks how she can be lonely and happy. English frames it as the speaker never having seen a happy one. The exact creature's affect and Brant's ability to render it word-for-word cannot be read off the English alone. The source **does** show Rover's doubt and Brant's self-correction.

At item 2, Rover's `Character_Brant_30_4` option asks whether he understands her, while `_30_5` asks whether he is improvising. These lead to different Brant replies: item 3/`_30_6` credits learning from Pan Cake; item 4/`_30_7` insists he understood or translated carefully. Both raw `JumpTalk` edges go to TalkId 6, item 5, after which he admits at item 6/`_30_9` that he added something. A generated conversation cannot have Rover ask both questions and receive both replies as one observed exchange. EN's “a few phrases in Echo-speak” is stronger and more specific than the ZH/JA/KO acknowledgment of learning from Pan Cake. Brant's admission licenses the bounded inference that his first translation was *not* strictly literal; it does not prove that his later danger warning is invented or that he has fluent access to every Echo utterance [BRA-E39/C35].

His item 8/`Character_Brant_30_11` warns about pirates and the companion group. Here the localization fork is analytically material. The Chinese anchor and JA/KO name a puppet troupe or performance group whose members cannot come out to play or perform; EN generalizes to “Echoes” forced to hide. Both point to restricted companions under pirate pressure, but EN alone does not establish that *all* nearby Echoes were targeted in this particular report. His promise at item 9/`_30_12` is to try to restore their time under moonlight. It is an undertaking, not proof that the group later danced or that he personally witnessed their every loss. One can write him as protective and theatrically buoyant without making the Lottie Lost a prop that says exactly what he wants [BRA-E39/C35].

## Aldric's dream changes other people's options

The second action is not Brant performing a villain. It opens with Aldric, technical speaker `100023`, addressing his crew, boasting that Drake's coin will obtain riches and imagining Ragunna nobles made to call him captain, kiss his boots or fetch his tea. The chanting “CAPTAIN!” at item 11/`Character_Brant_33_12` is technical speaker `100013`, **not** Brant, despite the key's `Character_Brant` prefix. After that turn, Rover's alternatives `_33_13` and `_33_14` lead to Brant's distinct responses at items 12/`_33_15` and 13/`_33_16`; each jumps to TalkId 15. Only the first contains the explicit ethical objection. Chinese says even a beautiful wish must not tread people underfoot; JA names human dignity; KO rejects making people servants; EN says it is wrong to treat them that way. The common ground is opposition to reducing other people to instruments of Aldric's wish. Brant can still make dramatic promises of his own, but his practical test asks whose freedom and bodily risk a dream consumes [BRA-E40/C36].

The common action continues: Aldric invokes Golden Fleece, Bell-Ringing Crab and the coin; when it does not perform as promised, another pirate suspects nearby Echoes. Aldric then orders all Echoes captured at item 21. A technical-speaker-`100016` Lottie Lost cue occurs at item 23, and Brant interrupts at item 24/`_33_31` with a deliberately theatrical “audience” rebuke. At item 27/`_33_34` he announces “Happy Lottie Lost”; the pirates at item 31 explicitly accuse the intruders of being **humans in disguise**, not the real Lottie Lost and Cuddle Wuddle. Thus his line is at least a role claim in the confrontation, not a verified renaming or affect report about the original creature. The exact staging and ownership of the item-23 cue still need runtime review. The source supports a model that uses play to contest a captor's framing while keeping the original Lottie Lost's speech and vulnerability separate. It cannot certify that she became happy, or that a staged name freed the troupe [BRA-E39–E40/C35–C36].

At item 27 Rover can accept an introduced “Captain Cuddle Wuddle” role (`_33_35`) or decline an introduction (`_33_36`). Brant's item 28/`_33_37` then announces the named company, while item 29/`_33_38` respects a modest unnamed friend; both jump to TalkId 31 before the pirates try to seize the disguised intruders. This is a small but useful counterexample to a captain who automatically assigns roles to companions. The branches do not prove that every Rover or hypothetical crossover partner enjoys public improvisation. The more consequential test is whether Brant adapts his story after the other person elects a role [BRA-E40/C36].

## Evidence and sound boundary

The two actions are pinned source graphs and four-language texts, not footage of an executed route. Five exact Brant turns—`_30_2`, `_30_9`, `_30_11`, `_33_15` and `_33_31`—have four selected `flac_roundtrip_pcm_identical` render associations each in the private complete-voice analysis (20 associations). Their render rows do **not contain** explicit event or numeric-media ID fields; a friendly text key or FLAC name must not be promoted to an event→bank proof. No listening or visual inspection was performed for this correction. A future retrieval should compare the short Lottie Lost source utterances with Brant's delivery *on the selected branch*, and observe whether the runtime disguises and optional role choice are presented as the graph suggests. It should not call a signal-integrity pass an audible finding or use EN's broader “Echoes” term as the four-text scope.
