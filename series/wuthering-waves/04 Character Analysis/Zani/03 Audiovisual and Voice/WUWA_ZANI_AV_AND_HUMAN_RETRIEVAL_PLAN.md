---
series: WUWA
character: Zani
artifact_type: av_human_retrieval_plan
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

# Zani — claim-driven AV and human retrieval plan

Current state: the local client-derived four-dub FLAC corpus was hash-verified and machine-measured (3,517/3,517 distinct objects, zero measurement failures). Fifteen exact source-key cases were joined to 63 render variants in [metadata only](AUDIO_MATCHED_SEMANTIC_CASES.json). **No human four-dub listening or runtime video/gesture review has been performed for this packet.** No recordings, WEMs, art or full scripts are included in Git. Local restricted roots: `_voice_media/character/complete_voice_corpus/Zani/v0_1/`, `_research/character_packets/Zani/audio_work/`, and the previously exported `_visual_media/character_visual_v0_2/` rasters. The installed client and private Drive evidence plane remain separate from analytical Git authority.

## Listening targets and competing questions

| Source key | Claim under test | Competing reading / what to annotate |
|---|---|---|
| `FavorWord_150703_Content` | Meaningful-work versus busywork distinction (ZAN-C02). | Is the line matter-of-fact, exasperated, playful or mixed within each localized wording? Record audible changes, not a global mood label. |
| `FavorWord_150704_Content` | Rest advice to Rover alongside self-warning (ZAN-C11, C16). | Does concern ride on a joke, admonition or practical instruction in each dub? |
| `FavorWord_150705_Content` | Rover changes her experience of everyday color (C11). | Check intimacy of address and pacing without converting archive affection to a canonical romance. |
| `FavorWord_150714_Content` | Civic agency and respect for Phoebe (C09, C12). | Distinguish conviction from hostility; align each dub with its own script length. |
| `Main_Linaxita_2_1_16_1` | Formal welcome register (C15). | Seven render variants across four languages; explicitly select the gender/player-variable variant before comparison. |
| `Main_Linaxita_2_1_16_41` | Relief when formality drops (C15). | Contrast against first welcome **within** a dub; do not attribute every difference to relationship state if variant/recording differs. |
| `Character_Zani_67_16` | Admission of earlier escalation (C03, C18). | Note hesitant or brisk delivery only if actually audible and repeatable. |
| `Character_Zani_67_35` | Stable conditions protect routines (C01, C18). | Is the reasoning emphasized more than the heroic self-image? Examine pauses and sentence boundaries. |
| `Character_Zani_67_38` | Hopes someday to sleep through the night (C16). | Do not infer imminent recovery from a short line. |
| `Character_Zani_59_2` | Acknowledges fabricated employee rule (C04). | Check the precise preceding question in runtime context before tagging tone or motive. |
| `Character_Zani_63_23` | Threat to Talos (C05). | Compare serious acoustic delivery without eliding the victim/perpetrator context or inventing a killing. |
| `Event_WWPDJSBF_1_16` | Real leave, difficulty enjoying it (C16). | Observe whether fatigue is performed, stated, joked about or a mixture; respect the later chronology. |
| `FavorWord_150728_Content` | Efficiency can increase demands instead of freeing time (C28). | Compare ZH/KO loafing, EN acting busy and JA extra-work wording before testing irony or frustration within each dub. |
| `FavorWord_150730_Content` | Strength is given a protective end (C29). | EN inserts a shield image that ZH/JA/KO do not; do not treat that wording as a four-language source fact. |
| `FavorWord_150731_Content` | Offers to fight for Rover as sword or shield (C29–C30). | Do not literalize maximal weapon imagery or call the menu question an observed choice; inspect each localized metaphor. |

The following are **additional source-defined targets**, not already joined in the fifteen-case JSON above. Retrieve their exact semantic occurrence and per-dub render identities from the complete restricted manifest before listening; a text key alone does not select a playable object.

| Source key | Why add it | Boundary |
|---|---|---|
| `Character_Zani_10_25`; `flow#/7297/7/17` | Compare Chinese/JA/KO explicit torture term with English's “more extreme methods,” then hear the line in its minor-offender context. | No tone can convert the sentence into an observed torture act, categorical ethical ban, or free-standing Talos threat. |
| `FavorWord_150718_Content` | Compare dawn-versus-midnight birthday wording and party-planning register. | The archive line gives no Rover response or proof that a full party took place. |
| `Main_Linaxita_2_1_16_17`; `flow#/4204/2/11` | Test her personally negative view of the efficient sightseeing scheme within formal guest service. | A route offered to a client is not necessarily her preferred leisure plan. |
| `Character_Zani_23_21`, `_33`, `_36`, `_42`, `_43`, `_45`; `flow#/7411/7` | Compare offer to step aside, the inferred Montelli-supplier worry, victim-right reply, Terminal duty, compensation request and leave-question deflection on exact four-dub renders. | Six Zani keys have 24 PCM-valid render joins outside the fifteen-case JSON. Rover's trust ultimatum and leave question are different-speaker text; no event/bank/media IDs, human tone or executed option path is claimed. |

For the fifteen preselected cases, follow the exact `text_key` plus `semantic_voice_occurrence_id` and `runtime_render_variant_id` from the case JSON. For additional targets, resolve the same identities from the private complete-line manifest first. Confirm source locator, language witness hash, source virtual path, WEM hash, canonical PCM SHA-256 and FLAC hash; check event/bank/media identity **where populated**, recording nulls rather than inventing them, before opening the local restricted FLAC. Friendly filenames and text similarity alone are insufficient. If a line uses multiple variants, record the chosen variant and why. The two textless `4657/1/0–1` occurrences are **not** in the selected fifteen; if listened to separately, keep any transcription as a new, lower-authority human witness, never an unmarked repair of the normalized source.

## Annotation protocol

1. Preserve original FLAC and hash. Use listening copies only locally; document playback chain, channel selection, any gain adjustment, and time offsets. Do not alter the evidence copy to “improve” delivery.
2. Read each language's actual localized text, then annotate that dub's audible phenomena: pause, stress, pitch movement as perceived, breath, laugh, intensity, phrase boundary, background sound and uncertainty. Distinguish acoustic *observation* from inference about intention.
3. Compare same-character contrasts within each dub first: bank formal/relaxed, vigilante self-account/threat, work joke/rest advice. Cross-language comparisons should note text length, variable substitutions and multi-render variants.
4. Sample at least two listeners or a re-listening pass for contestable affect labels. Store raw notes, adjudicated notes and disagreements separately; report any clip that cannot support a clean line-level inference because of overlap/stem contamination.
5. Keep a typed link from each accepted observation to `ZAN-Cxx` and the exact audio render. Downgrade claims when the performance contradicts the textual shorthand; do not reinterpret every performance to fit the draft.

## Runtime visual targets

| Scene | Visual question | Current status |
|---|---|---|
| `4204/2` bank welcome and work interruption | Does she physically transition from composed service to clipped staff command? How are alarm/tie/equipment staged? | Not acquired/reviewed for this packet. |
| `7301/4` Nightwalker retrospective | Gaze, posture, weapon transfer, distance to Rover and choice-dependent gesture. | Not acquired/reviewed. |
| `7435–7436`, `7555–7557` protection and Talos confrontation | Separate reassurance of survivors from intimidation of perpetrator; avoid conflating adjacent cuts. | Not acquired/reviewed. |
| `8585–8587` night city / economic aftermath | Ordinary public life and shared quiet; check whether duplicated source rows map to one runtime encounter. | Not acquired/reviewed. |
| `12439/7` actual holiday | Evidence for fatigue, inability to settle, and departure to rest; do not infer from an isolated screenshot. | Not acquired/reviewed. |
| `7297/7` sweets and minor-offender briefing | Distinguish the food purchase, recipient uncertainty, night-operation request and coercive-language context on a reachable path. | Text retained; exact branch and runtime staging not reviewed. |
| `7411/7` Colleen's Terminal concern | Observe Zani's offer to step out, Rover's distinct trust speech, staff dismissal, private disclosure and three response options without merging speakers or asserting a proven Montelli supplier. | Text/order and 17 Zani four-dub render joins checked; option realization, gesture and human delivery unreviewed. |
| `7552/2` missing-person inquiry and Colleen's offer to guide | Hear the source-linked fifteen Zani lines with adjacent gang member, Colleen and Rover speech; observe whether Zani's initial stay-behind command yields after the one-option safeguard replies and what rescue movement actually follows. | Thirty-two-item listed sequence and 60 distinct four-dub technical joins checked; no event/bank/media IDs, human listening, executed route or rescue outcome certified. |

The [visual profile](CHARACTER_VISUAL_DESIGN_PROFILE.md) is grounded in three decoded official-client UI rasters and already marks rear construction and runtime movement open. Future captures may use owner-approved video up to 1080p and sound if requested, but preserve source/scene identity, capture settings, hash and access restrictions. They should not silently replace client UI art authority with third-party footage or promotional composition.

## Closure tests

An AV revision is eligible only when a reviewer can produce a reproducible retrieval manifest, four-dub line-level notes with uncertainty, runtime scene/source mapping, and a claim-by-claim transition (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`). Unheard lines stay “not reviewed,” even when the whole 3,517-object corpus passes machine QC. The in-world chronology, identity crosswalk and two missing normalized text witnesses remain independent audit gates.
