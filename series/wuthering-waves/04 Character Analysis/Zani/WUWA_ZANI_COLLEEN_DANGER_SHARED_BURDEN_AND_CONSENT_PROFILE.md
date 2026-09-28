---
series: WUWA
character: Zani
artifact_type: specialist_profile
analytical_responsibility: "Mixed-speaker missing-person inquiry, Colleen's risk-bearing agency, Rover's safeguard, and Zani's conditional concession"
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

# Zani — Colleen, danger, and the burden no one should carry alone

The earlier [survivor-distrust profile](WUWA_ZANI_SURVIVOR_DISTRUST_EMPLOYER_DUTY_AND_LEAVE_PROFILE.md) reads `7411/7`, where Colleen questions whether a dangerous Terminal might have a Montelli source and Zani recognizes the harmed person's right to suspect her employer. This separate `flow#/7552/2` action tests a different limit: when the same survivor wants to enter a dangerous rescue, does protecting her mean excluding her? The answer is neither automatic inclusion nor permanent veto. Zani first says to remain behind, insists that the risks are not equivalent, then accepts a plan after Colleen argues for her role and Rover offers to keep her safe. That is what this *listed text sequence* shows; its enacted movement and outcome have not been watched [ZAN-E42–E43; C41–C42].

The [matrix](WUWA_ZANI_EVIDENCE_AND_FALSIFICATION_MATRIX.md) indexes the questioning as ZAN-E42/ZAN-C41 and the participation decision as ZAN-E43/ZAN-C42.

## Exact source and speaker map

The pinned raw state is `BinData/flowState/flowstate.json#/7552`, `StateKey` `剧情_2_3_角色_赞妮副本_26_1`, action 2, a `ShowTalk` with 32 items in one `TalkSequence` numbered 1–32. The retained action has no explicit sequence transition targets. Items T28 and T29 each attach **one** player option, `Character_Zani_51_30` and `Character_Zani_51_32`, with an empty `Actions` array. Those are sequential prompts in the source, not evidence of an alternative Colleen-refusal branch. A quest title, exact executed traversal and camera staging are not inferred from the state name.

| Items | Technical speaker | What the record establishes | Negative control |
|---|---:|---|---|
| T0, T6–7, T9, T11–13, T15–17 | 1477, Zani | She demands the location of Talos and the missing people, pushes for an answer, remarks that the captive appears to have knocked himself unconscious rather than speak, then says delay could make matters worse. | Her observation is not a visual review proving how the blow occurred; it is not proof she tortured or killed him. |
| T1–5, T8, T10, T14 | 200124, gang member | He taunts Colleen about earlier harm, supplies Talos's hiding place, and refuses to reveal the other people's location. | His threats and taunts are not Zani's beliefs or independently certified history of the injury. |
| T18, T20, T24, T26–28 | 200001, Colleen | She volunteers to lead, says Hubert and others cared for her, and argues that even limited help may get rescuers to them sooner. | Her willingness is real dialogue, not proof that risk disappears or that everyone was eventually found. |
| T21–23, option `_51_30`, option `_51_32` | 750088 and player options, Rover | Rover articulates the likely danger ahead, then offers to safeguard Colleen and answers Zani's overburden warning with a time-limited refusal to stand down. | Do not transfer the protection promise or the risk explanation to Zani. |
| T19, T25, T29–31 | 1477, Zani | She initially orders Colleen to stay, contests the risk trade, warns that carrying everything alone will exhaust someone, then stops trying to change the plan and asks for help. | Her later concession does not show that she thought the risk had become trivial or that the mission succeeded. |

The exact occurrence crosswalk accepts fifteen Zani turns in this action as solo and source-voiced. Their selected `COMPLETE_VOICE_LINE_ANALYSIS.jsonl` rows join sixty distinct, four-language PCM/FLAC objects with successful roundtrip checks. All sixty render records have null explicit event, bank and numeric-media IDs, so this is a source-occurrence to external-media join, not an event-to-bank proof. None has been listened to by the analyst; these fifteen lines are **outside** the frozen fifteen-case sound sample and eight source-defined audio cohorts. The denominators in the [source census](WUWA_ZANI_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md) do not increase [ZAN-E42–E43].

## Force toward a captor is not the same decision as consent from a survivor

The action opens under urgency. A gang member has no difficulty mocking Colleen and disclosing Talos's location, but resists revealing where other people have gone. Zani's repeated short demands are forceful. Her subsequent line treats his self-incapacitation as preferable to disclosure; the textual sequence does not show her carrying out torture. A model that writes her as incapable of intimidating anyone would lose the scene. A model that turns the gang member's refusal into permission for invented abuse would exceed it. The later Talos threat at `7556/3` remains a separate, stronger instance with its own audience and consequence limits [ZAN-E20, E42; C05/C41].

She turns differently to Colleen. Her initial “stay here” is a protective command, not a request for Colleen's preference. Rover spells out the danger of further opposition; Colleen responds that Hubert's group helped her and that her knowledge may shorten the route. Zani still says the two possible harms are not equal. The Chinese and English line frame that as a comparison of bad outcomes or stakes; Japanese more directly says the proposed purpose does not warrant taking the risk, while Korean is briefer about the difference. None of these witnesses says she thinks Colleen is worthless or has no stake in the missing people [ZAN-E43; C42].

Colleen's next plea should not be replaced with a stock “brave victim” speech. She explicitly describes limited strength, a concrete navigation contribution and a debt to named people. The player option attached at T28 is Rover's protection assurance, not a guarantee supplied by the runtime. Zani's warning at T29—that taking everything upon oneself leads to exhaustion—follows that offer, but the retained text does not explicitly mark whether she addresses Rover, Colleen or both. It also reflects a problem in Zani's own labor profile without proving that she recognizes herself in the moment. Rover's following one-option reply limits the overburden objection to *today*, and Zani concedes, asking the group to proceed. The concession is conditional on the surrounding dialogue; it is not an unlimited policy that any volunteer should be sent into danger [ZAN-E43; C02/C42].

This source complicates two easy character-model rules. “Zani always decides for those she protects” ignores that she revises a direct order after hearing Colleen and Rover. “Zani never overrides a survivor's expressed wish” ignores her initial command and persistent risk judgment. A plausible future response should ask what the person contributes, what danger they understand, what safeguards others can genuinely provide, and whether delay itself harms those missing. It should also be able to say no if those factors change. That is a bounded inference from one scene, not a numerical trait or a validated prediction [ZAN-C42].

## Retrieval and revision conditions

For performed-voice study, nominate exact keys `Character_Zani_51_1`, `_51_7–8`, `_51_10`, `_51_12–14`, `_51_16–18`, `_51_20`, `_51_26`, `_51_31`, `_51_33–34` by their **source locators**, not key stem alone. Listen in each dub with Colleen, Rover and the gang member's adjacent lines present; retain render IDs and WEM/PCM/FLAC hashes and keep null event/bank/media fields null. A runtime capture should establish who Zani faces at T29, which options are displayed, whether Colleen leads after the exchange, and what happens to the missing people. None of those observations is currently claimed.

A later direct action showing Zani refuses Colleen despite these listed lines, or that the one-option prompts have nonobvious dispatch, would revise the route reading. A direct outcome showing a successful or harmful rescue would revise the consequence, not the fact that she initially resisted. A later general statement on consent or employee safety could refine the behavioral rule. Human listening could support a bounded delivery observation; it cannot manufacture a different speaker, a bank ID, or a completed outcome from silence [ZAN-E42–E43; C41–C42].
