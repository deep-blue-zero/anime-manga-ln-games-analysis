---
series: WUWA
character: Shorekeeper
artifact_type: av_and_human_retrieval_plan
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

# Shorekeeper — AV retrieval and human-review plan

This plan is **not** a claim of human listening or runtime visual inspection. Three static official-client UI rasters have a separate individualized visual profile and manifest. Private FLAC/WEM, decoded images and any authored review clips stay outside Git; the selected corpus currently has 543/543 technical voice resolution.

1. For each candidate, retain semantic occurrence ID, exact archive or flow action/item locator, graph route, technical speaker and EN/JA/KO/ZH text-witness hash. Distinguish narrator, live scene, favor address, message and event mode.
2. Follow the source text/occurrence → available event/media identity or external-source path → client virtual path → WEM SHA → PCM SHA → FLAC SHA for fifteen calibration cases; do not invent an event/bank edge for the 24/60 renders with null explicit IDs. Then sample the main five-register contrasts. If phrase-to-object alignment is imperfect, mark ambiguity instead of adjusting the text to the media filename. Rejected `3451/2/1`, `4214/1/0` and `5200/0/0–2` are deliberate negative controls for speaker identity.
3. Listen in all four languages to the fifteen **sound-resolved** cases below first. Creation, field encounter, Delone farewell and chosen-name *favor-story prose* are literary/visual-context targets, not automatically voice lines. If another exact voiced scene conveys those moments, add it by occurrence ID and media proof; do not attach a nearby FLAC to an unvoiced narrator. Record exact render ID, phrase time, heard owner, timbre/contour only when directly perceived, background/music, and reviewer confidence. Later full listening must state 543-line and 2,172-association denominators separately.
4. Inspect runtime staging/choice routes at `4020/4`, `3446/3`, `3756/2`, `3804/3`, `4198/2`, `4081/3` and later scenes. Verify whether projected/core/body states look different, how visual transformation is represented, and what Rover actually can answer. The UI stills do not settle physical mechanics, alternate form or performed intimacy. Review clips, if produced, should obey owner maximum 1080p and only include sound when requested.
5. Test key contradictions: Does she present an early absence of emotion or difficulty *naming* emotion? Which acts of concealment answer an old Rover request versus a present unilateral decision? At `4198/2/24–26`, how does performed pacing frame the no-more-harm promise beside her own proposed cost (SHK-C23)? That retained `ShowTalk` action has no player option or Rover reply between those lines. How is replacement-core danger resolved before later seaside scenes? The near-human-soul archive line (`FavorWord_150530_Content`) and the unvoiced four-language shared-world ending (`FavorStory_150505_Content`) require different review channels; neither is settled by aggregate pitch. Record observations against claim IDs and revise in place before owner adoption.

The selected sound corpus is machine complete, but human performance review, exact branch traversal, physical/visual acting review and newer-client comparison remain open. A source freeze is independent from draft analytical authority.

## Fifteen calibrated sound cases

Every row below is present in [the matched-case artifact](AUDIO_MATCHED_SEMANTIC_CASES.json) as one semantic occurrence with exactly four source-matched renders. The table gives the *question* for listening; it does not claim a heard answer. Review against each dub's localized text before comparing delivery across languages. Preserve any branch context and do not use pitch/energy summary as an emotion tag.

| Text key | Four-dub listening question | Claims most at stake |
|---|---|---|
| `FavorWord_150501_Content` | Is homecoming addressed as ceremonially welcoming, privately relieved, or a mixture? Does a dub's pause actually separate Black Shores from her side? | SHK-C11–C14 |
| `FavorWord_150503_Content` | How does she mark the one-sided memory asymmetry and the prior secrecy request, if at all? | C11, C16 |
| `FavorWord_150506_Content` | Is piano described with exploratory curiosity or already mastered emotional confidence? | C12, C19 |
| `FavorWord_150508_Content` | Does the unrecreated chowder memory sound wistful, practical, fond, or indeterminate? The text alone does not decide. | C12, C19 |
| `FavorWord_150510_Content` | How is the move from assigned duty to her own will voiced without assuming she repudiates Black Shores? | C06, C12, C17 |
| `FavorWord_150513_Content` | Is Camellya's free choice granted matter-of-factly or with a perceptible tension? Do not infer rivalry from the topic. | C06, C16 |
| `FavorWord_150518_Content` | Is a piece of her crystal offered as a modest refuge rather than unlimited wish fulfillment? Inspect softness/urgency only as heard. | C02, C19 |
| `FavorWord_150531_Content` | Does the confident four-dub love declaration contrast with the crisis-scene question? Distinguish vocal certainty from subtitle certainty. | C13, C16 |
| `Heihaian_main_1_3_28_4` (`flow#/4020/4/2`) | Does the reunion apology acknowledge unilateral action; what nearby player choice frames it? | C11 |
| `Heihaian_main_1_3_40_41` (`flow#/3756/2/5`) | This lie concerns a terminal Agent. Does the performed admission carry uncertainty or defensiveness? Do not substitute it for the Rover lie. | C11, C16 |
| `Heihaian_main_1_3_68_12` (`flow#/3804/3/11`) | Compare each localized reason for deception, especially the fuller English “best for both” wording. | C11, C14 |
| `Heihaian_main_1_3_5619_35` (`flow#/4198/2/30`) | The utterance asks whether the feeling is love. Compare hesitation without converting the question into a mutual vow. | C13 |
| `FavorWord_150530_Content` | Compare the qualified near-human-soul self-report across four dubs without turning it into an ontological or consent finding. | C24 |
| `Heihaian_main_1_3_5619_37` (`flow#/4198/2/24`) | How is the no-more-harm promise framed—shared agreement or her own assurance? The retained action contains no player response at this item. | C23 |
| `Heihaian_main_1_3_5619_25` (`flow#/4198/2/26`) | Does her proposed sole cost sound resigned, resolved or uncertain in each dub? Textual differences and a separate file cannot by themselves settle the acted relation to the promise. | C23 |

If a file has overlapping voices, music, a truncated phrase or multiple Wwise playback branches, mark that render `ambiguous` until a phrase-level event replay or continuous scene supplies the missing boundary. The exact WEM/PCM/FLAC hashes make the observation reproducible; a friendly basename alone does not.

## Runtime targets that sound files alone cannot settle

Beyond the fifteen calibrated cases, the [retrieval crosswalk](WUWA_SHOREKEEPER_AV_HUMAN_RETRIEVAL_CROSSWALK.md) now nominates exact keys in three additional source-voiced actions: `flow#/3456/2` (mediated Lament testimony, self-blame and localization of bodily cost), `3825/1` (bitter tea, proposals and two choice menus), and `4173/1` (warning/evacuation, deaths and uncertainty about a possible replica). Their 39 accepted semantic lines have 156 integrity-valid four-dub renders in the selected corpus, but no performed emotion or actual branch has been reviewed. These are separate from the unvoiced Aetherfin side quest and from the text-only Shorekeeper WavesLine action `flow#/14519/1`; neither expands the fifteen-case sound manifest or the 543-line voice denominator by implication.

The Honami [source study](../01%20Evidence%20and%20Source-Facing/WUWA_SHOREKEEPER_HONAMI_TASTE_DIAGNOSTIC_UNCERTAINTY_AND_RIFT_BOUNDARY_PROFILE.md) adds two further nominations, `flow#/9389/4` and `9395/4`: 17 already-selected voiced semantic lines/68 distinct PCM-valid renders, with explicit Wwise event/bank/numeric-media IDs still null. Retrieve both taste-response and normal-vitals opening branches separately; compare Abby's concern with the measured range and ZH/JA/KO similarity against EN “identical.” These actions do not change the frozen 543-line corpus, the nine measured cohorts or the fifteen-case sound manifest. They add no human listening, executed path, safe rift crossing or cure claim [SHK-E37–E38].

| Exact source scene | Claim-driven visual/temporal question | Acceptance boundary |
|---|---|---|
| `FavorStory_150501–150503_Content` | Which parts of crystal emergence, field walking and Delone's death are narrated prose versus an available runtime scene? | Do not claim visible animation or voiced narration merely from archive text. |
| `flow#/4020/4` | In the first reunion, where does her apology sit relative to choice and camera distance? | Map at least one observed route; preserve unchosen alternatives. |
| `flow#/3446/3` | What does the projection/core explanation show, and what is only verbally reported? | Separate visible form from her technical self-description. |
| `flow#/3756/2` | Does the Agent's condition and her reaction visibly support the textual lie/sorrow interpretation? | Keep the Agent's agency and identity distinct. |
| `flow#/3804/3` and `4198/2` | How is proposed self-sacrifice staged; does bodily fracture appear, what can Rover answer, and does the no-more-harm/sole-cost sequence visibly or audibly mark a tension? | A projected plan is not the post-resolution state; textual juxtaposition alone cannot decide her intended promise scope. |
| `flow#/4081/3` | Does the revised core permit demonstrable shared sun/sea experience, and what limits remain? | Do not infer unrestricted departure or human anatomy. |
| `flow#/4099/4` and `4215/4` | Does the later Abby lead unfold as hypothesis and travel plan? | No cure claim without later outcome evidence. |
| `flow#/17652/6` and `17653/10` | Does food/music interaction show present ordinary curiosity rather than a replayed archive mode? | Preserve event/quest continuity and exact branch. |
| `flow#/3456/2`, `3825/1` and `4173/1` | Which Sonoro reassurance and tea preference/burden replies are actually selected, and is the Guixu replica only discussed or also shown? | Source action and four-dub render joins are established; historical event causation, executed route and performed tone are not. |
| `flow#/9389/4` | Which taste reply is selected, is sugar visibly added, and how does the shared report frame Lahai-Roi's communication blockade? | Two Shorekeeper taste replies are alternatives; a regional report does not grant complete knowledge inside the sealed area. |
| `flow#/9395/4` | Which opening normal-vitals route appears with Abby's concern, how are the similar/“identical” signatures presented, and is rift entry attempted? | An unknown cause and present unsafe-entry judgment remain even with a probable destination; do not turn this into an already completed journey or treatment. |
| `ShortMessage#/72` ID `30073` → `flow#/14519/1` | What WavesLine unlock and receipt conditions display the two one-option captions, their sent Rover lines and the bouquet-labeled `EmojiId: 177`? | The raw message graph and four-language text are retained; all Shorekeeper-associated items are source-unvoiced. Do not attach a nearby voice file, infer a physical bouquet, or date postrepair travel from this backfill state. |

For each observed interval, retain quest/state key, flow locator, player branch, client build, capture hash, video resolution (owner maximum 1080p), audio inclusion state, and a time-coded note with *observation*, *inference* and *counterread* separated. Direct scene inspection can revise SHK-C02, C11, C13, C16–C20; a contact sheet cannot prove continuous gesture or timing.
