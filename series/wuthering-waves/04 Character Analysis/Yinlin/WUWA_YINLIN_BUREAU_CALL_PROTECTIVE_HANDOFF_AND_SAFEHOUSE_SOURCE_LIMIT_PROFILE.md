---
series: WUWA
character: Yinlin
artifact_type: bureau_call_protective_handoff_safehouse_profile
analytical_responsibility: "Preserve the unheard caller, protection plan, and four-language safe-house information conflict"
scope: YINLIN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: YINLIN_PRE_AV_V0_1
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

# Yinlin — the unheard instruction and a protective handoff

The exact target is character-quest `114000018`, raw state `剧情_剧情_角色_吟霖线新_46_1`, `flow#/812/6/0–10`. Raw action 6 is one `ShowTalk` with eleven talk items, no stored `TalkSequence` and three single Rover option prompts attached to T3/T6/T8. Their option actions are empty, so this action records no alternative `JumpTalk` path; the prompts ask who she called, report that the puppets yielded no clue, and ask how to find the safe house. Ten talk items carry named speaker 370/Yinlin; T1 is a parenthetical stage cue under technical speaker 83 saying she *seems* to be speaking with someone. The remote caller's words are not among the eleven items or three prompts. This action should be read as a continuous displayed exchange with player acknowledgments, but the text does not give an omniscient recording of the call.

## A visible objection without its object

At T0/T2/T3, Yinlin asks whether it must be done, says she considers it unnecessary, then accepts the instruction and says she will handle it. Chinese `Character_YinLin_26_1–4` retains both hesitation and compliance. EN adds “our only option”; JA conveys “that far”; KO asks whether it must happen. None names the remote instruction or an affected person. T1's parenthetical clue does not reveal the caller's identity, exact order, authority or intention. Her subsequent explanation at T4 says she was contacting a Public Security Bureau liaison, but it does not quote what that liaison said in T0–3. It is reasonable to infer continuity of the call; it is not evidence that the objection specifically targeted transferring Li Rong/Yuanyuan, saving puppets, or destroying them.

This matters for a model of her institutional agency. “She unquestioningly follows the Bureau” erases the objection. “She defied an order to harm Yuanyuan” invents the order and an outcome. The narrower source fact is that she voiced reluctance about an unidentified proposed action, accepted responsibility to handle something, then presented a safety plan. A later direct record of the other side of the call could resolve the object and force revision [YIN-E39, YIN-C36].

## People, puppets and a safe route are not one object

At T4–10 she says Bureau-linked personnel will protect Li Rong and Yuanyuan, asks about the puppet bodies, defers fuller investigation until they reach safety, identifies a safe house and wolf-shaped route marks, and urges movement before Fractsidus find them. The Chinese `_26_7` places Li Rong/Yuanyuan under expected protection; `_26_10` moves the puppets for later investigation. A planned protective handoff and an evidence-carrying move are distinct from a confirmed completed custody transfer or a solved puppet ontology. The action does not show the Patrollers arriving, identify every puppet's status, prove Li Rong's later cooperation, or establish that the chosen route was safe in execution. Yinlin does not abandon investigation by deferring it; she sequences it after immediate safety.

Japanese `Character_YinLin_26_11` materially differs about safe-house information flow. ZH/EN/KO say a contact told Yinlin of a nearby safe house; JA says she informed the Bureau of a safe-house location and would rendezvous there. Thus the shared claim is a planned meeting at a covert-investigator safe house, not a four-language invariant claim about *who supplied its location*. The four witnesses agree on wolf-shaped wayfinding marks and urgency, but even that is an announced plan, not footage proving successful arrival. An analyst must not silently choose the JA version to imply she controlled all infrastructure, or use the others to prove she knew nothing of it before this call [YIN-E39, YIN-C37].

This scene pairs with, but does not resolve, the earlier tracker and later workshop ethics. She can impose unconsented surveillance on Rover and still arrange safety for Li Rong and Yuanyuan; the latter does not erase the former. She can move puppet bodies for inquiry without deciding that replicas are either returned human beings or worthless objects. Her early Bureau contact precedes the later erased-file confrontation and the still-later rebuilt-dossier holiday account; affiliation, live access and public role should be dated separately [YIN-E12, E18, E24, E33, E39].

## Audio and retrieval boundary

Exact keys `Character_YinLin_26_1`, `_26_3`, `_26_4`, `_26_7`, `_26_10` and `_26_11` have six accepted Yinlin semantic voice rows at `812/6/0,2,3,5,7,8`. Each has four language-specific external-source WEM/FLAC associations passing per-render PCM roundtrip checks: 24 render associations, not 24 different things said. These nominations are outside the packet's eighteen selected sound cases. The source stage cue T1 is *not* a Yinlin occurrence merely because its `PlayVoice` flag is true. Event, bank and numeric-media identities must stay null where the external-source mapping does not provide them. No human listening or runtime video has been performed for this packet. Compare the six exact lines with adjacent T1 and T4–10 before judging hesitation, directive force, concern or whether a dubbed performance supplies a clue not present in text.
