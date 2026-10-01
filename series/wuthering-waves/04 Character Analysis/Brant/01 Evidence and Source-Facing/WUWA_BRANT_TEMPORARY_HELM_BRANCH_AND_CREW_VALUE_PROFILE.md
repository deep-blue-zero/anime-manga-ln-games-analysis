---
series: WUWA
character: Brant
artifact_type: temporary_helm_branch_and_crew_value_profile
analytical_responsibility: "Trace the optional captain-for-a-day dialogue graph, speaker ownership, crew-value wording and resource limits without inventing an executed route"
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

# Brant — a temporary helm, three ways to answer, and a crew that is not one man

The captain-for-a-day sequence is an unusually useful test of Brant's authority because it gives the addressee a real authored choice without transferring the entire troupe's future. Brant says Battier's wager does not compel Rover to take the temporary helm: acceptance depends on Rover's willingness (`flow#/5238/2/2`; `Character_Brant_11_3`). A later line has him return to deck-scrubbing before dinner (`5238/2/11–12`). These are a local, time-limited reversal of roles and a material chore, not proof that the troupe permanently replaced its captain or that he abandons command in emergencies. The source text offers a possible response route; this packet has not observed a player choose one in the running client [BRA-E37; BRA-C33].

## What the pinned dialogue graph actually preserves

The following is a static reading of embedded `ShowTalk` actions in `BinData/flowState/flowstate.json`. `TalkItems.Id` and zero-based array locators differ by one in these rows; an option key is not automatically a voiced Brant `TalkItem`. The table records authored alternatives and reconvergence, not a claim that every alternative occurred on one playthrough.

| State / source action | Choice and authored branch | Common continuation and limit |
|---|---|---|
| `flow#/5238/2`, state `剧情_2_1_角色_布兰特线_1_5` | Brant's `TalkItems.Id=6` (array `/5`; `Character_Brant_11_8`) offers three Rover option keys: interested `_11_9` jumps to Id 9; challenged `_11_10` jumps to Id 7 (`_11_12`); tired `_11_11` jumps to Id 8 (`_11_13`). Ids 7 and 8 both explicitly `JumpTalk` to Id 9. | Id 9–13 (array `/8–12`) praises the members, names Battier/Tina/Lavito, says each contributes, and returns to ordinary deck work and a six-o'clock supper. The interested option has no separate Brant reply before this shared part. |
| `flow#/5239/3`, state `剧情_2_1_角色_布兰特线_1_7` | Sequence 0 contains TalkIds 1–22. Rover can ask whether the treasure exists (`Character_Brant_13_27` → sequence 1, Id 23/`_13_29`) or about the half-coin (`_13_28` → sequence 2, Id 24/`_13_30`). | Both routes lead to sequence 3, TalkIds 25–34. The two alternative responses are voiced by technical speaker `1545`, not Brant `1462`; their wealth speculation cannot be assigned to Brant by the quest-key prefix. |
| `flow#/5241/3`, state `剧情_2_1_角色_布兰特线_1_9` | Sequence 0 contains TalkIds 1–7. Rover's bet-loss explanation `Character_Brant_16_8` jumps straight to sequence 2 (Ids 9–29); “I am captain today” `_16_9` visits sequence 1, Id 8/`_16_10`, where Brant concedes he lost and is deckhand for the day. | Both then use sequence 2. The extra Brant concession is conditional on the second prompt, not a universal scene line. Elsewhere in this state Brant introduces Rover as today's captain (`_16_7`); neither path proves permanent promotion. |
| `flow#/5244/3`, state `剧情_2_1_角色_布兰特线_1_12` | After TalkId 1, applause `Character_Brant_26_2` goes to sequence 1 (Ids 2–3); suspicion about drunkenness `_26_3` goes to sequence 2 (Ids 4–5). | Both rejoin sequence 3 (Ids 6–27), which moves to questioning the “lucky” person about the coin. Applause and skeptical concern are alternative response frames, not evidence that Rover both applauded and accused him in one run. |

The graph establishes a limited but important affordance: a hypothetical counterpart may find his proposal exciting, difficult or tiring, and the tired route has its own answer rather than being silently overwritten. Brant's reply to fatigue in `Character_Brant_11_13` acknowledges it before pairing exertion with laughter and treasure. That is not the same as obtaining consent to an indefinite voyage. A compatible model can answer with warmth and a smaller offer, retain the other person's right to decline, and still let Brant enjoy the prospect of adventure. It must not manufacture a hidden “correct” option or treat these three options as three simultaneous Rover attitudes. Runtime choice selection, exact animation and audible delivery remain unreviewed [BRA-E37; BRA-C33].

## The linguistic hinge: who makes the troupe possible?

The shared `Character_Brant_11_14–16` continuation matters more than a convenient sea metaphor. In the Chinese anchor, the most interesting part is the troupe's people, followed by examples of Battier's fishing, Tina's knowledge of sea conditions and Lavito's stories; every member has a specialty and matters. Japanese calls the companions the greatest treasure, then says no one can be lost; the latter is stronger than the Chinese importance claim and should not become a verified zero-casualty record. Korean likewise foregrounds the members. English `_11_14` instead says none of it is possible without a captain **and** every member, and `_11_16` says each soul plays a role. The English is not anti-crew, but its added captain emphasis could make a monolingual reconstruction too singularly heroic. The four witnesses support distributed competence and collective attachment; they do not prove that every crew member held equal formal command or that Brant never acted alone [BRA-E38; BRA-C34].

The preceding line `Character_Brant_11_8` has a distinct source-text trap. Chinese displays pirate-facing words for adventure and “plunder” with embedded `<ano=...>` readings of seeking stories and bringing laughter; Korean retains a similar annotated contrast, while English and Japanese present legend-seeking and audience pleasure without the same literal plunder surface. The visible source markup is evidence of a double register, not proof of an actual raid or proof that no risky tactic ever occurred. No runtime review here establishes how the annotations appeared on screen or were performed. The separate bounty/escape story and Aldric confrontation still need their own cost analysis; a pun does not morally settle them [BRA-E38; BRA-C19/C34].

The later half-coin conversation is a useful attribution control. A non-Brant speaker `50098` imagines treasure for the troupe at `Character_Brant_13_26`, and speaker `1545` answers either treasure existence or half-coin location at `_13_29–30`. English `_13_29` turns weather shelter into “leisure and luxury,” whereas Chinese emphasizes no longer worrying about exposure to wind and rain. Brant's own common-path `_13_39–43` proposes finding Bella through the known dinner/escort routine and invites the day's captain to choose whether to ask. The package should not infer Brant's personal wealth doctrine from `50098`/`1545` or declare him opposed to all treasure because he later rejects Aldric's way of imposing prosperity. His criticism is about transferred human cost and control, not a taboo against provision [BRA-E38; BRA-C10/C34].

## Reconstruction and falsification boundary

If a crossover visitor says a sea adventure sounds exhausting, the source-supported tendency is to recognize the burden and offer a reason to continue; it is not a canonical promise to cancel every voyage. If the visitor accepts a temporary helm, ask whether this is the one-day wager or a different invented arrangement, and preserve the crew's individual expertise. If a narrator calls Brant the only person who makes the troupe possible, compare the ZH/JA/KO ensemble line and the EN addition before hardening that into his belief. If someone claims Brant explicitly promised his troupe Golden Captain luxury, check `WhoId`: the most lavish lines in this branch belong to other speakers. A future executed-route capture could refine gesture and delivery, but it would not turn an unchosen option into universal history or erase the common crew-recognition continuation [BRA-C33–C34].
