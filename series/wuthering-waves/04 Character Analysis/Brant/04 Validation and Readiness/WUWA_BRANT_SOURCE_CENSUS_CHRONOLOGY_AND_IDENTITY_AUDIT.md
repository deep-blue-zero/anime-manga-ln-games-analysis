---
series: WUWA
character: Brant
artifact_type: source_census_chronology_identity_audit
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

# Brant — source census, chronology, and identity audit

This is a selected-collection audit, not a claim of every route or version. `flow#/N/A/I` expands to the pinned `wuwa://.../BinData/flowState/flowstate.json#/N/Actions!/A/Params/TalkItems/I` locator; `FavorStory_...`, `FavorWord_...` and `FavorRoleInfo_...` are exact local package keys. Chinese is the semantic anchor; EN/JA/KO are witnesses. Official-client FLAC is raw-media evidence, whereas Arikatsu is the current normalized semantic view. Source freeze and authority status are separate.

## Denominators

| Selected scope | Count | Meaning / caution |
|---|---:|---|
| Relevant raw flow states | 219 | Full embedded actions, transitions and other speakers preserved. |
| Contextual text keys | 3,163 | Scene context, not 3,163 Brant utterances. |
| Quest references / distinct IDs | 127 / 28 | Retrieval links, not 28 fully independent character arcs. |
| Direct identity candidates | 662 | 636 accepted solo, 18 rejected, eight unresolved. |
| Accepted direct occurrences | 636 | 544 source-voiced and 92 source-unvoiced. |
| Favor stories / archive voice entries | 5 / 62 | Five prose units are not audio units. |
| Semantic voice lines | 606 | 544 accepted voiced direct plus 62 archive. |
| Render associations / runtime object rows | 2,432 / 2,328 | EN/JA have 610 associations each; KO/ZH 606 each. Variants and reuse differ. |
| Unique native PCM/FLAC objects | 2,324 | 550,554,288 FLAC bytes; 2,324/2,324 locally integrity-checked and measured, zero failures. |
| WavesLine shells | 0 | No Brant message shell was selected; do not infer he cannot communicate by other channels. |

`COLLECTION_AUDIT.json` reports the selected source and voice corpus valid, `source_generation_frozen: true`, and normalized source status `active_provisional`. This interpretive packet is `draft_noncurrent`. The 23 metadata-only selected cases span 92 EN/JA/KO/ZH render records, not all 606 lines; 48 retain paired null event/numeric-media IDs. All five newly selected ascension cases have explicit event and numeric-media IDs in their four renders, but this does not independently establish every bank edge.

## Identity boundary

- Playable Brant is role 1206, Chinese 布兰特, with `ROLE_VARIANTS.json` preserving trial/duplicate role candidates without counting them as extra people. Named scene speaker IDs include 1462 and 1572; communications IDs include 100058 and 700103. These are source records, not a rule that any surrounding unnamed speaker is Brant.
- Seven opening rescuer talk items `flow#/4220/3/0–8` are accepted for those occurrences because the speaker immediately identifies himself in the same exchange. `4371/1/0–1`, `5682/6/3–4`, and `11917/1/0` have similarly local continuation support. The opening rescue should be checked against exact branching before inferring one universal delivery.
- Cristoforo at `4104/10/20–22`, the inverted-tower disembodied voice at `4357/3/3–8`, Pero/Roccia at `4360/2`, reinforcements at `4372/2/32–33`, Bardolino at `4383/1`, Starbuck at `5682/6/10–11`, and Galbrena at `9507/1/10–11` are not Brant merely because he appears nearby.
- The anonymous theatrical quotation `8842/4/27–29` and five anonymous relic-donor items `9965/5` remain unresolved. A captain-like style or Brant's later offer to carry an object does not resolve their speaker.
- The character-quest text-key prefix is not a speaker label. At `flow#/5238/2/5`, `Character_Brant_11_9–11` are Rover option keys, not three Brant lines. At `5239/3`, speaker `50098` voices the treasure joke `Character_Brant_13_26` and `1545` gives the two alternative `_13_29–30` reactions; Brant is `1462`. Do not transfer another speaker's wealth claim into Brant's behavioral model.
- The same prefix trap recurs at `flow#/6823/5/11`: `Character_Brant_33_12` is the pirates' chant from technical speaker `100013`, whereas Brant's branch-specific replies at items 12–13 are `1462`. At `6820/2` the short Lottie Lost turns belong to `100016` and Brant's reported translation to `1462`; his admitted embellishment does not transfer the creature's own utterances into his voice.

## Working source-time order

1. **Childhood and the cost of pilgrimage.** `flow#/4381/2/22–27`, `FavorStory_120603_Content` and `flow#/5239/3/15–17` connect an irreverent question about an unseen Sentinel to banishment, older Fools' care, companion loss and a vow that his own crew should come home. The parent's tern-carved box and ammonoid are personal memory objects, not a magical origin proof. This arc explains a motive; it does not establish exact dates or all bereavements.
2. **Troupe building and a workable sanctuary.** `flow#/4379/1` and `4381/2` situate Penitent's End refuge amid wreckage, Tacet threats and people whose departure is honored. `FavorStory_120602_Content` shows dinner, rehearsal labor and a definition of “Fool” as a pursuer of freedom. `FavorStory_120604_Content` places a later storm/beast episode and the Lario stage origin; the narrated storm is not a guarantee of never fearing future danger.
3. **Ragunna/Carnevale and public claims.** `flow#/4220/3`, `4372/2`, `4378/1` and `4384/2` move from rescue and coastal intelligence to a festival intervention that contests punishment. `4385–4387` documents improvisational performance training and branch-sensitive stage narration. A play's hero/maiden imagery is stage fiction, not a relationship outcome for Rover and Carlotta.
4. **The Drake/Aldric character quest.** `flow#/5238/2` offers Rover the helm conditionally; `5239/3` gives the Drake tale and crew-safety vow. Bella's coin and Aldric's departure lead through tactical theater at `5241/3`, `5244/3`, the Egla disguise at `5245/3` and `5248/5`, Aldric's wealth-for-crew claim at `5350/5`, his later small-share offer at `5355/5`, and the aftermath at `5357/3`: Brant rejects prosperity imposed by force and crew sacrifice, but acknowledges his own treasure curiosity and uncertain gambles. At Egla the source explicitly joins quest node `155000000_34` and handbook pointer 27; twelve Brant authored-union turns contain two mutually exclusive replies to Rover's role options and 48 distinct four-dub PCM-valid renders. The quest synopsis's costume object and earlier consent are not directly seen. The interposed full-source row `5356` is Aldric-only and not among the 219 Brant-selected flow rows. Neither that row nor the selected dialogue independently declares Aldric's final fate. Separately, quest-tree node `220030` links quest `155000000` to `QuestTree_Summary_220030`, whose four-language retrospective text reports his end at the treasure site. This source-class distinction corrects the earlier selection-scope omission; the death mechanism and Brant's knowledge remain unobserved. Numeric flow-row order is not a substitute for quest graph order or branch reachability.

The [static choice audit](../01%20Evidence%20and%20Source-Facing/WUWA_BRANT_TEMPORARY_HELM_BRANCH_AND_CREW_VALUE_PROFILE.md) resolves only the *authored* alternatives at `5238/2`, `5239/3`, `5241/3` and `5244/3`: each has a bounded Rover response fork and a shared continuation. It does not establish which option any player selected, a universal response from Brant, or the complete quest's executed route. `TalkItems.Id`, zero-based array index and sequence number are recorded separately to prevent an off-by-one voice/text join.

The [wager/exchange/honorary-helm study](../01%20Evidence%20and%20Source-Facing/WUWA_BRANT_WAGER_EXCHANGE_AND_HONORARY_HELM_PROFILE.md) adds `5236/3` and `6281/6–6283/2` within quest `155000000`. The first action has two independent Rover choice pairs and a crew-adjudicated fish-bet outcome, not automatic permanent Rover command. At the painting, three `JumpTalk` alternatives converge; the later inscription action retains option text but no explicit `TalkSequence` or option actions, so its exact runtime selections remain open. At the closing map exchange, two opening options get separate brief Brant replies before rejoining at a scripted honorary title. Exact quest-node joins are `155000000_8`, `_120`, `_123` and `_115` respectively; PlotHandBook `#/35` pointers are `1`, `72`, `73` and `81`. Node numeric order is not the handbook order and neither is a playthrough transcript. The four actions contain 42 selected Brant voiced lines, 168 distinct PCM-valid four-language objects and paired-null numeric event/media fields: selected-scope technical proof, not event→bank or human AV proof [BRA-E41–E43].

Two additional Brant character-line states, `flow#/6820/2` and `6823/5`, show his admitted Lottie Lost paraphrase and an intervention against Aldric's Echo-capture order. Their prefix and subject matter place them in this character-line source family; the selected `QUEST_CONTEXT_REFERENCES.jsonl` has **no exact-state quest-node join** for either, so this packet does not assign them a more precise node or executed time position. The first has an option/jump split over whether Rover asks about comprehension or improvisation; the second separates Brant's dignity objection from his surprise reply, then a named from an unnamed introduction. The [source study](../01%20Evidence%20and%20Source-Facing/WUWA_BRANT_ECHO_TRANSLATION_PUPPET_TROUPE_AND_ALDRIC_INTERVENTION_PROFILE.md) preserves those independent choices and the EN “Echoes” versus ZH/JA/KO puppet-troupe scope.
5. **After Carnevale and later appearances.** `FavorStory_120605_Content` explicitly permits different futures for troupe members, an unmasked return to Ragunna, a sold parental home, and learning a new instrument. `8703–8705` is a later event duel/prize/debt cluster with 8703/8704 variants, not a second independently proven Carnevale resolution. `11366–11367` later shows rehearsal craft and children; voiced status must be checked per occurrence.

Ascension I–V (`FavorWord_120626–120630_Content`, `favorword#/1861–1865`) are ordered *archive unlocks*, not a sixth dated story-time step. The five lines invite stage preparation and a shared horizon, but II's English safety absolute and IV's Japanese past-versus-ZH/KO prospective wave wording are localization/temporal forks. Neither a completed voyage nor literal power transfer can be read back into this chronology. See the [ascension specialist](../01%20Evidence%20and%20Source-Facing/WUWA_BRANT_ASCENSION_RISK_AND_INVITATION_PROFILE.md).

Two later-labeled 2.7 main-story actions need their own media/state distinction rather than being folded into post-Carnevale rest. `flow#/8850/5` has an exact QuestNodeData state match `168000001_49` and PlotHandBook `#/56`; ten accepted Brant turns are source-voiced, with 40 distinct four-dub PCM-valid objects. Roccia says Brant proposed a new play amid citywide destruction-dream reports; she says neither of them has yet had the common dream, and Brant keeps collecting information about apparently exceptional Rover experience and other anomalies. The raw action has opening empty-action Rover captions and later `JumpTalk` question alternatives, not one proven executed interview. Separately, `flow#/11777/2` has no exact-state quest wrapper retained: its fourteen-item template action includes eight accepted Brant text rows, all `play_voice: false` and absent from the 606-line selected voice corpus. He makes a recipe-derived drink and toasts fallen people and tomorrow; Roccia's regional-history account and speaker 702's repeated toast are other speakers. KO dates the recipe before the city's founding, unlike ZH/EN/JA's founding-period wording. These are two source states, not demonstrated performance cure followed by audiovisual memorial [BRA-E44–E45; C40–C41].

## Genre, graph, and performance limits

The map's earlier losses are not Aldric's present crew casualties, and Brant's coin payment for the map is not a repayment of those deaths. At `flow#/5357/3/1`, English is stronger about Aldric choosing treasure over life; Chinese/Korean report return for money and Japanese describes fixation. At `flow#/5355/5/16`, ZH/KO name the Fools' ship where EN/JA name Pilgrim's Sail; the four-language `5357/3/5` agreement that he left the Troupe does not settle the ship wording. Those are dialogue-witness tensions, not a license to derive the global outcome from the most dramatic line. The independently linked synopsis does report Aldric's end; it is not a filmed death or evidence that Brant witnessed the mechanism. The [cost-and-fate specialist](../01%20Evidence%20and%20Source-Facing/WUWA_BRANT_DRAKE_ALDRIC_COST_AND_FATE_PROFILE.md) gives the specific cost ledger and counterreadings.

The tavern's Wanted “Returned” tale is knowingly embellished; the crew's theatrical hero story is in-world art; Benir's Forte notes and a permit are in-world documents; Brant's Drake account shifts from legend to a map's reported voyage to his own interpretation. Keep those evidence classes distinct. The source package retains full flow actions/transitions and the occurrence crosswalk, including rejected and unresolved rows. Ninety-two accepted direct talk items are source-unvoiced; even a perfect 2,324-object FLAC audit cannot give those an acoustic performance. Selected objects include four multichannel flags, so source text identity should not be projected automatically onto every waveform. Human four-dub listening and runtime gesture inspection remain open. The three official-client UI rasters in the separate visual profile do not prove unseen rear construction or persistent animation habits.
