---
series: WUWA
character: Qiuyuan
artifact_type: source_scene_and_message_specialist
analytical_responsibility: "Separate an ordered harbor farewell from a later text-only message and preserve four-language home, obligation, boat-motion, and self-cultivation differences"
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

# Qiuyuan — a sheath offered to someone else, a crossing not yet settled

## Two different source surfaces

The harbor action `flow#/9932/3`, state `剧情_2_7_黎那汐塔主线_下半_5_4`, has an exact `QuestNodeData#/13480` join and a `PlotHandBook#/58` pointer `/50/Flow` to quest `175000000`. Its 39 raw `ShowTalk` items have one nested `TalkSequence` running IDs 1–39, no retained options or per-item jumps. The pinned speaker table distinguishes Qiuyuan `1563`, an elderly merchant `1650` and Rover/player `750088`. Twenty-four Qiuyuan items are accepted and source-voiced. They already belong to the selected 255-line corpus and join 96 distinct, PCM-valid four-dub render objects; all 96 retain null explicit event and numeric-media IDs. This proves source-to-local-audio retrieval at the selected scope, not a Wwise event→bank chain, human interpretation of delivery, visible gesture or a different path [QIU-E15/E36].

The separate `ShortMessage` ID `30084` at `PhoneMsg/shortmessage.json#/83` points to `flow#/14530/1`, state `剧情_1.0至2.8剧情回填_17_1`. Its contact is Qiuyuan, message speaker `701111`; the two raw `Talk` items `phone_JL_15_1–2` omit `PlayVoice` and are accepted source-unvoiced. The collector's `WAVESLINE_MESSAGES.jsonl` still calls body extraction `metadata_only_scope`; the already-retained full flow and four-language context-text records permit a narrow independent reading of these two keys. `QuestId: 0` and `ListenQuestId: 0` provide no direct event-time join. The title “backfill” does not independently establish when Rover received or opened them relative to the harbor scene. Neither item is one of Qiuyuan's 255 selected **voiced** lines; a nearby harbor FLAC cannot be assigned to this text [QIU-E16/E37].

## At the harbor, he still sees limits to what he knows

The action first stages a small public-world check. Qiuyuan asks the elderly merchant when the ship sails, then notices no Acolytes are supervising. When the merchant jokes that he must therefore be able to see, Qiuyuan answers in ZH/EN that he merely **senses** no one interfering (`HRT_Rinascita_Interludes_603_1–5`, items 0–4). This does not demonstrate restored ordinary sight, an all-range Mindsight or infallible knowledge of every Acolyte's location. The merchant then credits the city's rescue to multiple heroes, Fenrico and past presiding figures, and voices residual fear (items 5–9). This is the merchant's account, not a memory Qiuyuan personally witnessed in full or an independent proof of each supernatural mechanism. Qiuyuan reassures him and invites him aboard before Rover arrives (items 8–13). His ordinary courtesy is not a break from his lethal mission [QIU-E15/E36].

Qiuyuan tells Rover that his work is unfinished and Scar's faction escaped. His “goat head” line is explicitly violent or testing in every witness, but JA `_603_23` says he had intended to finish that target, where ZH/KO wonder whether the head would withstand his stroke and EN wishes to have tested a one-strike severing (items 14–18). The difference changes how neatly a generated line can pretend he knew the outcome. He also explains his Septimont service through both the limited target of Leviathan's influence and the Grand Marshal's commission; he redirects formal thanks to her (items 19–23). That modesty does not mean he did no work, that the merchant's plural account is false, or that an official assignment excuses every later act [QIU-E15/E36].

Rover asks about Geshu Lin. In one continuous source sequence Qiuyuan says corrupt officials deceived the Agency, Liang and him into going to Jinzhou to kill Geshu, then says Geshu **was not what they claimed at that time** and fell under Threnodian influence only later (`_603_43–44`, items 28–29). This preserves the original false accusation versus later danger without requiring him to call the earlier investigation a mistake. He then considers battlefield deaths and says death is insufficient compensation yet the death he can give is what he can or must do (`_603_34–35`, items 30–31). Chinese, English and Korean express a duty/necessity clause; Japanese `_603_35` is narrower—death is about all he can do—without the equally explicit *must*. This is a localization limit on the force of obligation, not a proof he has abandoned the pursuit in Japanese or a neutral judicial mandate to execute Geshu. The source reports his vow; it does not prove he alone caused the later casualties or that Geshu has been caught [QIU-E04/E15/E36; C04/C05].

## The other person's sheath and his own unfinished thought

Only after the merchant calls him to the ship does Qiuyuan name Rover's standing companions a home and sheath (`_603_37–38`, items 33–34). In ZH/EN/KO the claim about Rover having a place is comparatively present-tense: people beside Rover are the family who can fight for and with them. Japanese `_603_37` casts the sword's return to a sheath more toward an eventual future, while `_603_38` still names companions as family/sheath. No language here says a sheath makes a sword harmless or makes comrades into equipment. It is a relation of reciprocal aid, not Qiuyuan giving Rover a command to retire [QIU-E15/E36; C14/C15].

The unfinished `_603_39` deserves less completion by the analyst than the packet's first pass gave it. Chinese and English say only “perhaps/maybe one day”; context permits an inference that Qiuyuan imagines a home of his own, but the referent remains unspoken. Korean makes “perhaps **I too** someday” more explicit. Japanese says “someday, again,” which could point to reunion rather than a straightforward self-home declaration. Rover's ZH/EN/KO reply promises that this future will come; Japanese's gender-conditioned reply is a bare assent. Qiuyuan's parting line expects another meeting, but the action does not show a settled household, romance, completed revenge or promised return date. A character model may carry the *possibility of his own reciprocal refuge* without making the port an accomplished conversion from vengeance to domesticity [QIU-E15/E36; C15/C34].

## The boat reverses direction in Japanese

The two-item message is a useful falsification test for treating all four localizations as the same late emotional fact. At `phone_JL_15_1`, ZH says the departing boat is notably steadier than the arriving one; EN and KO likewise describe the return crossing as less rough. **JA says the returning boat rocks much more than the outbound one.** All four language witnesses for this one key resolve at textmap row `/106088` in their respective files, and the raw message action identifies the same Qiuyuan speaker. This is not merely a stronger adjective: the physical comparison reverses. A source-grounded English or Chinese rendering may report a smoother departing vessel; a four-language invariant account may not. Whether Japanese deliberately contrasts physical rocking with inward stillness, contains a localization error, or imagines a different comparison is open [QIU-E37/C35].

At `phone_JL_15_2`, all witnesses describe a calm sea and an opportunity to quiet, discipline or cultivate the mind. That line can coexist with a smoother boat in three languages and with a rocking boat in Japanese. The calm **sea** is not a direct clinical or mystical finding that Qiuyuan's mind is already calm, his Forte permanently restored, his guilt resolved or his vengeance abandoned. The message gives him an interval and a practice, not a completed cure. Nor does its source-unvoiced status support a sounded gentleness, cadence or breath that no one has reviewed [QIU-E16/E37; C15/C35].

## Model and review consequences

In an imagined departure scene, keep public courtesy, a continuing targeted pursuit and an ability to recognize someone else's shelter in the same person. For a ZH-anchored reconstruction, he can tentatively want such shelter for himself, but should not announce the port as the moment he found it; if using Japanese wording, avoid rewriting the elliptical “again” as an explicit self-home wish. In a text exchange on the boat, specify which localization is being imitated before asserting steadier versus rougher motion. Let the calm sea offer time to reflect without claiming the reflection has achieved peace. Keep merchant, Rover and Qiuyuan's respective lines owned by their speaker IDs, and do not turn either message key into audio.

A human reviewer should compare the four actual harbor dubs in sequence—especially `_603_35`, `_603_37–40`—and capture any runtime visual/branch context. The saved action is linear but no player playback or performed interpretation is recorded. The message requires separate UI receipt/order inspection and a check for any client-version correction to Japanese `phone_JL_15_1`. Until then, the textual inversion is real within the pinned witnesses and its cause is **OPEN**.
