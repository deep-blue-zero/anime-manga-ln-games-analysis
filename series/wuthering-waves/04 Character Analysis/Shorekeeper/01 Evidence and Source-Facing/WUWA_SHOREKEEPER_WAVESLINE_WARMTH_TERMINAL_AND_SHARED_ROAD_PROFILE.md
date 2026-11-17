---
series: WUWA
character: Shorekeeper
artifact_type: source_medium_specialist
analytical_responsibility: "Reconstruct one text-only WavesLine graph, distinguishing typed care, proposed technical mediation, reciprocal preference, an emoji, and unresolved chronology"
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

# Shorekeeper — what a typed message can and cannot carry

## The source is a message graph, not a voiced encounter

The selected `ShortMessage` row `30073` at `BinData/PhoneMsg/shortmessage.json#/72` has `WhichChat: 42`, whose four resolved contact-name witnesses identify Shorekeeper. Its `FlowParam` points to state `剧情_1.0至2.8剧情回填_6_1`, retained as `flowstate.json#/14519`, with `SetPlotMode` followed by `ShowTalk` action `1`. The short-message row has `QuestId: 0`, `ListenQuestId: 0`, and no direct quest link. `WAVESLINE_MESSAGES.jsonl` intentionally calls its **content extraction** `metadata_only_scope`; this study does not rewrite that collection status. It independently reads the already-retained full raw flow state and its `CONTEXT_TEXT_WITNESSES.jsonl` entries. The state title says plot backfill, but neither it nor row order establishes when a particular player received or opened the message relative to a quest, Ascension line or physical-core repair [SHK-E36/C35–C36].

The action has eleven raw TalkItems. Eight are ordinary `Talk` items attributed to Shorekeeper's message speaker `701100`, two are Rover/player-side `Talk` items under `701052`, and the final Shorekeeper-attributed item is `Type: PhoneMessage` with `MessageType: Emoji`, `EmojiId: 177` and localized key `phone_JL_5_9` (“Bouquet” in English). The pinned speaker table resolves the two IDs through Chinese name keys `{message}守岸人` and `{message}{PlayerName}`, respectively; adjacency alone is not the basis for ownership. The retained occurrence crosswalk accepts the nine technical `701100` items as Shorekeeper-associated and marks them source-unvoiced. **Nine accepted source occurrences are not nine recorded voice lines:** eight contain her typed propositions, while the ninth is an emoji item. No selected decoded voice row, performance, spoken tone, physically sent bouquet or visible emoji design is established by these records. The two Rover option *captions* are separate text keys from the two subsequent Rover `Talk` items; an option caption is not a second Shorekeeper reply.

| Raw zero-based positions | Exact keys and graph role | What may be claimed |
|---|---|---|
| 0–2 | Shorekeeper `phone_JL_5_1–3` | She questions whether cold characters transmit sunlight's warmth, encourages Rover to continue seeking world-connecting starlight, and says she will remain at the shore guarding what Rover left. This is a typed statement of intention, not proof of a permanent travel ban. |
| 2 → 3 → 4 | One option caption `phone_JL_5_4` jumps to TalkItem ID 4, Rover's actual item `phone_JL_5_6`; that item jumps to ID 5 | The graph offers one retained continuation, not two mutually exclusive thank-you routes. EN's “my Shorekeeper” belongs to Rover's option caption and is not a four-language possessive declaration by Shorekeeper. |
| 4–6 | Shorekeeper `phone_JL_5_10`, `_5_11`, `_5_7` | She begins from duty, then considers modifying the messaging Terminal and suggests a Tethys connection might make it easier for Rover. This is a possibility, not an implemented modification or independent proof the system is safe. |
| 6 → 7 → 8 | One option caption `_5_12` jumps to Rover item `_5_13`; it jumps to ID 9 | The only retained Rover continuation declines burdening Tethys and says written exchange can still feel face-to-face. It does not test every possible objection to connection or constitute a user-configurable veto policy for Tethys. |
| 8–10 | Shorekeeper `_5_14`, `_5_8`, then the `_5_9` emoji item | She accepts the stated preference, asks to share the road ahead, and sends an emoji-labeled item. The source does not show a joint journey, a relationship-status agreement, a delivered physical gift or anyone's response to the emoji. |

Both raw `Options` arrays contain **one** option, jumping to TalkItem IDs 4 and 8 respectively. The following Rover items have `JumpTalk` actions to IDs 5 and 9. The source is therefore a prompted linear exchange with two required continuation points, not evidence of multiple selectable emotional outcomes. There is no retained `TalkSequence` array, so the explicit IDs and jumps, alongside list order, provide the defensible path. A runtime capture could confirm display details, option-caption visibility, chat timing and the actual emoji artwork; none has been viewed here.

## Distance, duty and responsiveness

The first and last Shorekeeper messages create a productive tension. She says typed characters may fail to carry warmth and that she will stay at the shore guarding Rover's legacy; later she asks to share the road ahead. One reading turns her into a permanently stationary, self-erasing sentinel. Another converts the closing request into proof of unrestricted physical co-travel or exclusive romance. Neither follows. In this message she couples a locally situated duty with a relational request for future companionship. The medium permits someone to remain at one site and still participate in another person's travels by correspondence, support or future meetings, but the exact future arrangement is *not specified*. Her post-core mobility must be established from its own dated source, not assumed from an ambiguous road metaphor or denied by the shore promise [SHK-E06/E16/E27/E36; C09/C25/C36].

Her technical idea is similarly conditional. `_5_10–11` gives a duty statement and a tentative terminal-modification thought; `_5_7` proposes Tethys access as an ease-of-use possibility. Rover's text does not reject her person, but declines making Tethys part of this exchange. Her `_5_14` accepts what Rover prefers. Chinese frames the reply around what Rover *likes*; English “Then I suppose it's fine then” sounds somewhat more resigned, while Japanese and Korean also make the counterpart's preference decisive. That textual difference is a localization question, not a finding about voice acting—the entire message is source-unvoiced. A reconstruction may let her propose a technical bridge and then keep communicating in plain text when a counterpart prefers it. It should not insist that digitized feeling requires technological escalation or portray a hypothetical refusal as already tested in this one-choice graph [SHK-E36/C35].

The English Rover option caption `_5_4` adds “my” to “Shorekeeper,” whereas Chinese, Japanese and Korean simply thank or name her. This is a player-side localization fork, not a Shorekeeper confession or a universally possessive label. The last “share the road” request has relational and potentially romantic affordance alongside her separate explicit love declaration in `FavorWord_150531_Content`; it is not a mutual exclusivity contract. An emoji whose localized label is “Bouquet” adds an intimate gesture in this *message interface*. Without a viewed emoji, delivery animation or reply, it remains an emoji object, not a scene in which either character hands the other flowers [SHK-E10/E36; C11/C36].

## Reconstructive and review consequences

For a text-message scenario, preserve the medium: her measured concern about whether words convey warmth, a suggestion held as a question, Rover's stated preference, and her adjustment to it. Keep her Black Shores guardianship in view without rendering it a sentence of immobility. If the scene is staged in person, do not transplant the message's silence or emoji into performed voice and gesture as though observed. If an alternate Rover choice, an active Tethys connection, or a physically shared trip is desired, label it hypothetical rather than assigning it to the saved graph. If romance is explored, distinguish her unilateral explicit love statement, this relational invitation, Rover's EN-only option wording and an unproved mutual status.

The next review should inspect the actual WavesLine UI path and local unlock/version conditions, compare the four text witnesses in display order, identify `EmojiId: 177` visually, and check whether this message precedes or follows the post-core state in a real route. Until then, this is strong **source-text and graph** evidence but no voice, visual, delivery-time or enacted travel evidence. It adds no lines to the 543 selected semantic voice denominator and no PCM objects to the local audio corpus.
