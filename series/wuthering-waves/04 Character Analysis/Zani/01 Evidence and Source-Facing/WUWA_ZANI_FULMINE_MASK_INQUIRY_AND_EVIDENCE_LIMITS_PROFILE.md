---
series: WUWA
character: Zani
artifact_type: specialist_profile
analytical_responsibility: "Branch-specific inquiry with Fulmine, limited projection evidence, Montelli suspicion, and privacy-aware follow-up"
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

# Zani — a useful image is not a solved case

At the Pioneer Association, Zani seeks help tracing a Vitreum Dancer that disturbed the area near Trattoria Margherita. This early Chapter 2.0 investigation is a better test of her competence than a generic claim that she is “observant.” She knows whom to ask, explains what Fulmine and C-MOSS can record or project, notices the limit of the resulting evidence, and changes the next investigative question. She is neither an all-knowing detective nor a corporate employee who automatically declares the Montellis innocent. The [matrix](WUWA_ZANI_EVIDENCE_AND_FALSIFICATION_MATRIX.md) registers the bounded source as ZAN-E44 and the interpretive claim as ZAN-C43.

## Source, graph and speakers

The pinned source is `BinData/flowState/flowstate.json#/4245`, state `剧情_2_0_黎那汐塔主线_第一幕_20_1`, action 2 (`ShowTalk`). `QuestNodeData#/5960` and `PlotHandBook#/21` both point to quest `114000027` and the same flow state; this is a navigation candidate, not a watched traversal. The action has 35 mixed-speaker TalkItems and seven authored `TalkSequence` blocks. The occurrence crosswalk identifies Zani by technical speaker **1477** in sixteen source-voiced items. A Pioneer staff greeting belongs to 200052; the speaker 50068 introduces himself as Fulmine; the projection partner's short utterance and a sleepy response occupy other technical IDs. Neither those turns nor player-option captions become Zani's speech.

| Fork | Authored routes | Interpretive consequence |
|---|---|---|
| Rover's response to Fulmine's praise | Option `_26_8` goes to sequence 1 (Zani's surprised celebrity remark, return to business, and investigation request at TalkIDs 7–10); `_26_9` goes to sequence 2 (direct request at TalkID 11). Both rejoin sequence 3. | Zani's playful surprise is route-dependent. Her request at `_26_45` versus `_26_13` is duplicated wording on **alternative** paths, not two requests heard in one path. |
| Rover's response to a Montelli-looking figure | `_26_32` goes to sequence 4 (Zani notices a pre-Carnevale mask and suggests concealment); `_26_33` goes to sequence 5 (she notes the mask is atypical Montelli style). Both rejoin sequence 6. | The two remarks cannot be concatenated as one witnessed deduction. The first is more suspicion-forward; the second keeps the odd mask salient without settling identity. |
| Later attached captions | `_26_46` follows her conditional Montelli-interest inference; `_26_39` and `_26_40` follow her privacy concern. Their option `Actions` arrays are empty in this row. | “Spy or disguise” is a **Rover option**, not Zani's verdict. An enacted reply, route-specific staging, and a successful mask-shop outcome are not proved by this source. |

The longer first fork contains three Zani items where the shorter contains one; the second fork contains one Zani item on either route. Thus the authored union has sixteen accepted Zani occurrences, while a traversal through the listed sequences contains **fourteen or twelve**, subject to runtime confirmation. Counting all sixteen as one performed conversation would merge exclusive branches [ZAN-E44; C43].

## What the projected evidence establishes

Fulmine reports seeing the Echo leave the city, with Order personnel following it. Zani describes his recording Forte and C-MOSS's projection role (`_26_19–20`). That explanation is her account of an in-world method, not a certification that the projection reveals every cause, every unseen actor or the present whereabouts of a small moving target. After viewing, she says the search area outside is too broad and disturbed by Tacet Discords (`_26_22`). Fulmine says he can record only what he saw; Zani credits the help without pretending it solves the search (`_26_26`). The player can ask Abby to track by scent, but the sleepy refusal is not a failure of Zani's skill or an enacted search result. This is a bounded chain of witness, projection, insufficiency and revised inquiry—not an omniscient replay [ZAN-E44; C43].

The image then suggests someone in Montelli-like clothing. Fulmine asks whether the family might be involved (`_26_31`), a **question by another speaker**, not a confirmed source attribution. Zani's route-dependent mask remarks note an unusual pre-Carnevale disguise, but their epistemic strength differs. Her next shared line (`_26_36`) says the Montellis' desire to promote Reserved Terminals gives them a reason to avoid a scandal, *if* the pictured person is connected to the Echo disturbance. Incentive is not exculpatory evidence; clothing is not a verified identity; a mask does not prove conspiracy. The option “spy or disguise” is Rover's wording. Zani then accepts Fulmine's suggestion to consult mask-maker Nyarla while warning that direct questions about a noble customer's private order may arouse suspicion (`_26_38`). The two subsequent player captions offer a plan or a custom-mask pretext. The text does not demonstrate that either approach works or that privacy concerns dissolve [ZAN-E44; C39/C43].

The multilingual boundary is material. Chinese `_26_34` says the mask looks **as if** intended to conceal identity; EN's “must have wanted” and JA/KO's closer-to-conclusion phrasing are stronger. Chinese `_26_36` retains the conditional **if** the image's person is involved, as do the other witnesses. English `_26_22` says they cannot start searching “just yet,” while Chinese emphasizes not knowing where to begin under the wide area and interference. None licenses a model to announce a culprit or a completed search. An investigator may make provisional inferences without becoming strictly agnostic, but should distinguish observation, witness report, candidate explanation and verified consequence.

## Media and revision gate

The sixteen Zani source occurrences have **64** language-labeled render associations in the restricted complete-line manifest. All point to verified source WEMs and `flac_roundtrip_pcm_identical` output; there are **60** distinct WEM and PCM hashes because `_26_45` and `_26_13` reuse the same per-language objects on the two alternate request routes. The story render rows do not populate numeric event, bank or media IDs. These joins prove available playable bytes, not that all 64 represent distinct utterance performances or that any route has been watched. No four-dub human listening or runtime visual review is claimed.

A future runtime pass should capture both first-choice routes and both mask-choice routes (or document proven equivalence of the shared path), the precise projection shown, the later choice display, and any mask-maker result. A contrary primary scene verifying the pictured person's identity or Fulmine's method could revise the factual case. It would not retroactively turn Zani's conditional earlier speech into knowledge she did not yet have. Her later response to Colleen's fear of a Montelli-supplied Terminal (`7411/7`) is a separate, later knowledge state: both scenes allow institutional ties and serious investigation to coexist without automatic conviction or automatic acquittal [ZAN-E41, E44; C39/C43].
