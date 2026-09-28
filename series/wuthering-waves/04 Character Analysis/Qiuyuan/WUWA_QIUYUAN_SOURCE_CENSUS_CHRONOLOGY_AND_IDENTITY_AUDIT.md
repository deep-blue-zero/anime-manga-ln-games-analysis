---
series: WUWA
character: Qiuyuan
artifact_type: audit
analytical_responsibility: "Source census, identity, partial chronology, and evidentiary limits for the Qiuyuan reconstruction"
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

# Qiuyuan — source census, chronology, and identity audit

This audit governs the scope of the accompanying working reconstruction. It is **not** a claim that all game versions, quest paths, visual staging, or possible disguised identities have been exhausted. It does not promote this new interpretation over the existing current visual profile or owner-adopted WUWA packets.

## Source and retrieval boundary

The playable Qiuyuan is **仇远**, role `1411`, with direct story speaker `1563` and message speaker `701111`. He is not the distinct NPC Qiuyan (秋艳). The collected source is normalized 3.6.0 semantics pinned to commit `353f2eaed119bc9f680eab92807d20ac75a79b40`; `zh-Hans` is the semantic anchor and EN/JA/KO are official localization witnesses. Installed-client media provides raw audio authority, not an independent proof that official-client semantic tables match the normalized source. The collection's frozen source-generation flag is separate from the authority status of this analytical draft.

The owner-authenticated private Drive evidence route begins at `03 Analysis Bridge Corpora/Characters/Qiuyuan/`. Its reading guide, release manifest, and audio-object crosswalk give the source-facing route and exact shard/member retrieval identities. The private collection audit retains their object identifiers; this Git packet deliberately omits direct Drive links. The replication does not make the underlying source public or license redistribution.

For compact citations, `R/A/T` below denotes `BinData/flowState/flowstate.json#/R/Actions!/A/Params/TalkItems/T` under the pinned `wuwa://` commit. The `!` records an embedded JSON Actions field; a compact address is **not** a chapter number. `FavorStory_14110x_Content` and `FavorWord_1411xx_Content` are exact normalized text keys. The source package preserves each key's full language-specific textmap locator. The evidence ledger preserves action GUIDs, technical speaker IDs, branch transitions, and the other speakers in each scene; none should be flattened into a free-standing Qiuyuan quotation.

## Recomputed selected-evidence census

| Surface | Count | Interpretation |
|---|---:|---|
| Selected contextual action/scene rows | 33 | Includes other speakers and contextual material |
| Contextual talk items | 450 | Not 450 Qiuyuan utterances |
| Selected complete raw flow-state rows | 33 | Source rows, not guaranteed complete quest graphs |
| Contextual localized text keys | 599 | Textmap keys, not independent narrative events |
| Identity candidates | 188 | 187 accepted solo, one unresolved, zero rejected in this selected set |
| Accepted direct story/message occurrences | 187 | 182 `PlayVoice=true`, five explicitly unvoiced |
| Favor stories / favor voice entries | 5 / 73 | Narrative archive and voice menu are distinct surfaces |
| Direct semantic voice lines | 255 | 182 story plus 73 archive |
| Runtime render associations | 1,022 | More than four per line in a small number of cases |
| Unique local PCM/FLAC objects | 1,018 | Object identity, not line identity |
| Quest-reference wrappers / quest IDs | 6 / 3 | Does not certify three full quest graphs |
| WavesLine wrapper records | 1 | Two accepted message talk items; not a broad correspondence history |
| Human performance annotations | 0 | No direct listening conclusions in this draft |

The selected collection audit reports `255/255` accepted semantic voice lines fully rendered and no missing direct-character media. It records one unresolved contextual identity. Its `1,022` FLAC-manifest rows contain four repeated PCM identities; each repeated pair has two distinct source-WEM hashes and render associations but one native PCM/FLAC object, so row count is not object count. The local waveform pass independently verified and measured all **1,018** distinct FLAC/native PCM objects with no failures; individual measurements remain outside Git. The written source audio audit should retain the difference between association, object, and semantic line.

The five accepted unvoiced occurrences are two photo/battle snippets (`10859/1/0`, `11244/1/0`), two post-journey message lines (`14530/1/0–1`), and one candy-event cameo (`16882/1/10`). `PlayVoice=false` is not a decoding failure. The collection's completeness statement is scoped to its reconciled denominator; it does not prove there is no unidentified future or disguised voice.

Within the selected denominator, ten short tower actions `flow#/9917/2–9926/1` contribute 21 accepted, source-voiced Qiuyuan lines and 85 distinct valid PCM renders. The extra object beyond a simple four-per-line count is a second Japanese runtime variant for `HRT_Rinascita_Interludes_3_1`. The separate `9927/2` encounter contributes nine accepted Qiuyuan lines and 36 renders; its anonymous opening T0 remains outside that count. The 21 and nine lines are **not additions** to the 255-line denominator. Numeric event/media IDs are absent for these story renders, so retrieval must retain their semantic occurrence, local virtual media path and hashes rather than invent a bank join. The [tower study](WUWA_QIUYUAN_TOWER_TRACE_DISGUISE_AND_INFERENCE_PROFILE.md) explains the semantic and runtime limits.

The port action `flowstate.json#/9932/Actions!/3` has one 39-item `ShowTalk` sequence, with no recorded options or jumps in this selected action. The local speaker joins are Qiuyuan `1563`, the elderly merchant `1650`, and Rover `750088`. Its 24 accepted Qiuyuan voice lines contribute 96 distinct four-language valid PCM renders **within** the same 255-line denominator. This action has a `QuestNodeData#/13480`/`PlotHandBook#/58/50/Flow` reference to quest `175000000`; that reference does not make the later phone message part of the quest. The story render rows retain virtual paths and hashes, but have null numeric Wwise event/media IDs. See the [harbor and message specialist](WUWA_QIUYUAN_HARBOR_SHEATH_AND_INVERTED_BOAT_MESSAGE_PROFILE.md).

The two source-unvoiced message lines are independently traceable to `ShortMessage#/83`, ID `30084`, `WhichChat: 52`, and `flowstate.json#/14530/Actions!/1`, state `剧情_1.0至2.8剧情回填_17_1`. The raw two-item action uses speaker `701111` and has no `PlayVoice`; the selected collection records both as unvoiced, not as missing audio. The wrapper lists `QuestId: 0` and `ListenQuestId: 0`, so its exact receipt time and quest prerequisite remain open. Its collector's `metadata_only_scope` flag is preserved: the narrow textual interpretation below comes from separately pinned raw flow and four-locale textmap witnesses, not a claim that the collector decoded a full correspondence history.

## Identity decisions and exclusions

The named direct speaker `1563` and message speaker `701111` are selected by source-specific identity, not by a global string match. A hidden `178` at **`8882/5/0`** is accepted only because the protagonist immediately asks who speaks and `8882/5/2–4` provides Qiuyuan's self-identification and mission. This one accepted generic occurrence does not make all `178` lines his. The one-word reaction at **`9927/2/0`** precedes the disguised visitor's address; Qiuyuan is plausible but unproven, so it remains `unresolved` and is not counted as his speech or voice. The supposed Leon at `9927/2/1–43` is contextual dialogue by a separate disguised speaker, not Qiuyuan and not the real Leon. The actual Leon in `9913/4` and `9916/3` is another person. The `10738/2` Geshu Lin retrospective and `17722/4` Jingran–Muyu scene likewise require speaker separation.

The positive Leon rescue and the later fate dispute must also be separated temporally. `9913/4/6` names Acolyte Leon; in `9916/3/1–7`, Qiuyuan sends him to safety and Leon credits the Huanglong man with saving his life in all four text witnesses. QuestTree `questtreenode.json#/26`, node `212000`, links quest `175000000` and `QuestTree_Summary_212000` (`MultiText.json#/275411`), which likewise reports an Acolyte rescued in Ragunna before the Fenrico relic handoff. That authored retrospective corroborates the **earlier rescue**, not the Acolyte's condition after the distinct impersonation confrontation at `9927/2/15–16`. The accused and accuser give conflicting later claims; no independently authenticated post-encounter Leon appearance was established in this selected audit [QIU-E35/E38, C36].

The profile's first-person and archive voice entries are Qiuyuan's own source-defined voice surface, but battle triggers, archive reminiscence, message text, and live story dialogue are not one continuous conversation. `ROLE_VARIANTS.json` retains trial/duplicate technical role variants; no unproven alternate personality or form is inferred from those rows. The existing [visual-design profile](CHARACTER_VISUAL_DESIGN_PROFILE.md) is based on three actual official-client UI images; it does not certify runtime animation or embodiment of the mindscape scene.

The later favor-word records have a separate **raw Id versus Content-key** hazard. A reproducible [73-row crosswalk](FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json) joins the source package's raw `Id`, raw `Content`, exact `favorword.json` row locator, event path, and local semantic voice-line record. Thirty Id values do not match the suffix of their actual Content key. The private voice analysis correctly joins all 73 actual Content keys by source locator, including the 42 combat/traversal trigger rows with 168 four-dub renders. Do not generate a text key by formatting the raw Id. This is a source-schema distinction, not evidence of 30 missing or mismapped audio objects. The [trigger-language profile](WUWA_QIUYUAN_COMBAT_TRIGGER_SENSORY_AND_LIMIT_LANGUAGE_PROFILE.md) uses both fields explicitly and does not turn a gameplay *Fallen* label into a plot death.

## Partial chronology, with epistemic states

| Slice | Warranted order and state | Retrieval anchors | Constraint |
|---|---|---|---|
| Q0 — Fire and apprenticeship | A five-year apprenticeship follows an earlier fire involving the Sword Specter, who is simultaneously an agent of devastation and his rescuer/trainer. Qiuyuan confronts him at the last test. | `FavorStory_141101_Content` | The archive does not make every detail of the off-page aftermath visible. Do not invent a witnessed killing shot. |
| Q1 — Exhaustion, medicine, and the hut | After leaving the mountain, he is badly wounded, accepts Doctor Zhang's care, sets aside the sword, tends medicine, and lives among patients. His Forte is impaired; special medicine can call forth the inner-eye faculty for full-force use. | `FavorStory_141102_Content`; `FavorWord_141111_Content` | EN's story adds an open-ended timing phrase absent from ZH/JA/KO; no permanent cure or exact cross-language duration is established. A peaceful interval does not prove revenge was permanently renounced. |
| Q2 — Institutional service | Liang Dongyuan recruits him to use his skill for public protection. The doctor endorses a broader reach while preserving his own local care. | `FavorStory_141103_Content` | Neither patron's invitation absolves Qiuyuan of earlier bloodshed. |
| Q3 — Geshu Lin and institutional collapse | Qiuyuan checks the Jinzhou case, concludes corrupt Censors deceived the Agency, and spares/warns Geshu Lin. Later Liang dies in a body-shedding attack and Qiuyuan is scapegoated; Minister Lin opens a procedural escape. | `10738/2/1–25`; `FavorStory_141104_Content` | The later battlefield catastrophe is not evidence that the original accusation was true. His later self-blame is a character judgment, not omniscient causal proof. |
| Q4 — Fugitive return and assignment | Five years after escape, a lead from the Grand Marshal sends him toward Scar, the Threnodian-linked case, Jinzhou, and Rinascita. | `FavorStory_141105_Content` | The mission carries overlapping official and personal objectives; it is not a formal exoneration. |
| Q5 — Rinascita inquiry | He protects civilians and earlier saves Acolyte Leon; investigates residual frequencies and Cartethyia's condition; works with Cantarella; encounters a later Leon-like disguised intruder; obtains Fenrico's lantern after moral confrontation. | `9913/4`, `9916/3`, `9927/2`, `11170/3`, `10735/2`, `10736/2`; QuestTree node `212000` | The past rescue is corroborated, but Leon's post-impersonation fate remains disputed. Flow row numbers and `上半`/`下半` labels do not certify the player's exact traversal. |
| Q6 — Handoff and defense | He passes Fenrico's lantern to Rover, warns of the Dark Tide risk, fights on the surface, confronts Scar, and credits local warriors after the defense holds. | `8882/5`, `11919/1`, `10977/1`, `11982/1` | Scar escapes. “Defended the line” is not “completed the Scar mission.” |
| Q7 — Departure and later coda | At the port he acknowledges the pursuit remains open and frames Rover's companions as home/sheath; a separate written message depicts a calm sea, and a later 3.6 coda lets Jingran decide his own revenge. | `9932/3`; `14530/1`; `17722/4` | His own home remains prospective. In `phone_JL_15_1`, ZH/EN/KO say the departing boat is steadier, while JA says the return boat rocks more; do not turn either reading into a panlocale psychological cure or precise message date. |

The `10738/2` Geshu encounter is a retrospective inserted into later material. `11170/3` shows Qiuyuan still seeking a means to help Rover, so it precedes the lantern handoff at `8882/5`; the raw row index reverses that narrative dependency. Similarly, `10735/2` and `10736/2` yield the lantern before it is delivered. Menus and unlock order do not establish strict timing for every archive line. The 3.6 coda is later-source evidence, not proof of a complete long-term arc.

For the tower segment, `PlotHandBook#/58` supplies selected state pointers but not every intermediate state: `4_5` appears at `/35/Flow` before `4_4` at `/36/Flow`. Treat that as a nonmonotonic source reference, not proof that either numeric state order or pointer order is the player's executed path. In particular, the earlier strange presence, black-flame trace and firearm sound cannot be assigned to the separately recognized `9927/2` individual merely by adjacency. The accuser and disguised speaker also contradict each other about an Acolyte's survival; that unresolved fate is an evidentiary question, not a missing Qiuyuan render [QIU-E34–E35].

## Review performed and residual uncertainty

All five Chinese and English favor stories were read; all 73 Chinese and English archive-word entries were inspected, including the later trigger family, and selected meaning-changing entries were compared directly across all four language witnesses. The 187 accepted story/message occurrences were projected and read in Chinese and English, with their source keys and surrounding English scene dialogue; pivotal archive/story lines were compared directly across all four language witnesses. A targeted four-witness comparison also covered harbor `_603_35–40` and both `phone_JL_15_*` keys: JA softens or shifts the explicit obligation/home wording and inverts the boat-motion comparison, while all four message witnesses describe a calm sea. This is not a line-by-line semantic review of every JA/KO localization, an auditory listening pass, or a visual review of the runtime scenes. The `450` contextual talk items were counted mechanically, not all accepted as direct speech.

The main interpretive hazards are (a) merging the Sword Specter, Doctor Zhang, Liang, and Minister Lin into one generic mentor; (b) treating later blame about Geshu as proof that sparing him was wrong at the time; (c) confusing Qiuyuan's sensory/mindscape ability with omniscient access to another mind; (d) turning his self-description as a sword into consent to any order; and (e) treating a localized wording shift as character development. One material example: at `8882/5/5`, English compresses Fenrico's inability to communicate into the Dark Tide “silencing” him, while Chinese says he is bound to seal the Tide and cannot pass on what he knows. The latter governs the causal account. At `10738/2/23`, English foregrounds deterrence, while Chinese stresses the value of keeping a blade sheathed; both support restraint, but they are not word-for-word equivalents. In `FavorStory_141102_Content`, English has Zhang say Qiuyuan *killed* dozens bare-handed, whereas Chinese says he *fought* dozens and JA/KO likewise say faced/fought them. The Chinese-anchored packet does not treat that English kill count as settled by the passage; it remains possible he killed people elsewhere, and the scene does not provide a canonical count.

The one unresolved generic occurrence remains open. Original WEM decoding was inherited from the collection; the new waveform pass verified FLAC/native PCM against retained hashes but did not re-decode every WEM. Eight measured objects are multichannel and not interpreted as isolated actor stems. No claim here has direct video, body-language, acting intention, romance, or post-3.6 future-state authority.
