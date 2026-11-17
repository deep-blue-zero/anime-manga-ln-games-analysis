---
series: WUWA
character: Phoebe
artifact_type: audit
analytical_responsibility: "Source census, chronology, identity, branch and authority limits"
scope: PHOEBE_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: PHOEBE_PRE_AV_V0_1
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

# Phoebe — source census, chronology, and identity audit

This is a **noncurrent working reconstruction** of playable Phoebe (菲比, role 1506), not a replacement for the active source collection or existing visual profile. The primary textual witness is the pinned normalized Chinese semantic view; EN/JA/KO are localized witnesses. Installed-client audio is official-client raw evidence for the mapped media, not an independent proof of all normalized semantic claims. Source-generation freeze and analytical authority status are separate fields.

The full local collection is `ANALYSIS/Characters/Phoebe`, with the private voice view at `_voice_media/character/complete_voice_corpus/Phoebe/v0_1`. The collection's `COLLECTION_AUDIT.json`, `occurrence_identity_crosswalk.jsonl`, `RAW_RELEVANT_FLOW_STATES.jsonl`, `SCENE_AND_EVIDENCE_LEDGER.jsonl`, five favor stories, archive words, and four-language voice manifests are the reproducible inputs. The compact form `R/A/T` below means `BinData/flowState/flowstate.json#/R/Actions!/A/Params/TalkItems/T` under `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/`. A row number alone is neither diegetic order nor a complete playable graph.

## Recomputed selected-evidence census

| Surface | Count | What it establishes |
|---|---:|---|
| Complete selected raw flow rows | 185 | Selected context, not the whole game graph |
| Contextual localized text keys | 2,380 | Context witnesses, not Phoebe solo utterances |
| Quest-reference records / distinct quest IDs | 119 / 21 | Wrappers and joins, not certified graph completion |
| Direct identity candidates | 674 | 672 accepted solo, one rejected, one unresolved |
| Accepted direct story/message occurrences | 672 | 416 source-voiced and 256 explicitly unvoiced |
| Favor stories / archive voice entries | 5 / 60 | Separate archive families |
| Selected direct semantic voice lines | 476 | 416 story plus 60 archive; all locally rendered |
| Runtime render associations | 1,906 | Variant uses; not distinct lines or files |
| Distinct local PCM/FLAC objects | 1,818 | Full selected local object denominator |
| WavesLine messages | 0 | No selected matched contact/state messages; not proof none exist anywhere |
| Human listening / runtime video annotations | 0 / 0 | Performed and staged interpretation remains open |

The 60 archive entries are 60 distinct exact `BinData/favor/favorword.json` row locators, each with an actual raw `Content` key and an explicit event. They join 60 complete voice-analysis rows and 240 distinct, integrity-valid four-dub PCM/FLAC objects. The 30 combat/system entries at `favorword#/1927–1956` contribute 30 events and 120 of those objects; they are already included in the 476 selected semantic lines and 1,818 distinct objects above, not a new scene corpus. Seven Phoebe raw `Id` values do **not** match the numeric suffix of their actual `Content` key: the six skill rows `#/1929–1934` permute keys, and the nonlexical Phoebe greeting at `#/2235` uses `FavorWord_160719_Content`. Cantarella independently uses that same text key at `favorword#/1976` for a different role, title, event, semantic occurrence and four PCM hashes. A text-key-only owner lookup is invalid. The [archive skill/key profile](../01%20Evidence%20and%20Source-Facing/WUWA_PHOEBE_ARCHIVE_SKILL_KEY_SHARED_TEXT_AND_COMBAT_FAITH_PROFILE.md) preserves all seven raw IDs, actual keys and event IDs; no key is synthesized from the raw ID.

The collection audit reports valid selected voice completeness, with zero missing semantic voice lines. A separate local waveform pass measured all 1,818 distinct FLAC/native PCM objects, with zero failed objects. Four-language render association counts are EN 477, JA 477, KO 476, and ZH 476; the two excess associations over 476×4 are runtime variants, not new semantic occurrences. Twelve source-selected cases in `../03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json` retain 48 exact renders. These facts establish technical coverage inside the selected collection, not complete visual/aural interpretation, official semantic table parity, or future-version coverage.

## Identity and epistemic surfaces

The local crosswalk accepts named speaker IDs 1475 and 1597, supplemented by exact-context review; no generic ID is globally mapped to Phoebe. `4202/6/19` is an accepted hidden line because the immediate exchange identifies Acolyte Phoebe. `11917/1/0` is **rejected**: that opening belongs to Brant's multicharacter arrival, while Phoebe has a separate accepted utterance at `11917/1/5`. `4599/1/0` is **unresolved**: a hidden hostile reaction follows the chorale, but Abby's subsequent question to Phoebe does not establish that the hostile voice was hers. Neither rejected nor unresolved text may be mined for her beliefs or acoustic style.

The 4798 invitation contains alternative response paths and repeated guide language. Do not count every listed response as one continuous scene. The holiday's 4807 Echo exchange has other speakers and a consent sequence; the accepted Phoebe rows are not the whole scene. Religious history she explains in 4203, 4237, 4594, 4799 and elsewhere is often institutional teaching, reported legend, or an explicitly damaged inscription, not an omniscient narrator's confirmation. The source records her change of confidence after Lorelei's report; it does not license a retrospective claim that she knew the truth throughout. `FavorRoleInfo_1506_TalentDoc` and `_TalentCertification` are in-world Order records with institutional interpretation, not direct access to her motive or real-world medical advice.

The early `4203/2` guide action itself has 26 accepted Phoebe speaker-1475 turns, all `PlayVoice: true` with four selected render associations per turn. Its opening menu jumps to four *alternative* topics or finish, and explicit topic-end jumps return to the menu. Citizen use of Common Echoes and the Order's reserved armed/halo category belong to Phoebe's institutional account; Carnival's masked role-play is not proof of general legal equality. The two Carnival inner options have empty action arrays in this extracted row, so their exact runtime response mapping remains open. The [city-guide specialist](../01%20Evidence%20and%20Source-Facing/WUWA_PHOEBE_EARLY_CITY_GUIDE_COMMON_ECHO_AUTHORITY_AND_CARNEVALE_PROFILE.md) records the graph, exact quest candidate and multilingual qualification. These voiced rows are already **inside** the 416 accepted source-voiced occurrence denominator, not a new collection increment.

## Partial developmental chronology

| Slice | Source-backed state | Constraint |
|---|---|---|
| P0 — family loss and rescue | `FavorStory_150602–603_Content`: merchant parents die; attempts to place her with relatives fail; Isabella and the orphanage become home. On a later attempt to seek her parents by ship she nearly drowns, loses her father's locket, remembers a gentle rescuing presence, and is comforted by Echo friends. | The rescuer's identity is ambiguous. Orphanage kindness and adult rejection coexist; grief is not cured by doctrine. |
| P1 — vocation and hidden friendship | `FavorStory_150601,150604_Content`, `FavorWord_150603,150606,150608`: she handles a public brawl firmly and files its report; she plans orphanage service and loves Echo friends but conceals affectionate touch under an acolyte nonattachment rule. | A gentle manner is not passivity. She does not abandon either duty or friends here. The older acolyte silently permits the sleeping Echo huddle once, not a wholesale doctrinal repeal. |
| P2 — initial Ragunna guidance and investigation | `4202–4237`, `4585–4601`: she introduces visitors, teaches civic/religious context, including broad citizen Common Echo access and a guarded Order-only category, is drawn into missing-Echo inquiry, initially struggles to suspect a devout family, identifies a clerical connection, and offers Order testimony. Lorelei's disclosure shakes her trust in Fenrico. | The `4203/2` guide topics are options; its scriptures and legends are attributed teaching, not verified cosmology or a later reform charter. She is not infallible, instantly apostate, or knowingly complicit in the alleged deception. Her doubt and continued institutional loyalty overlap. |
| P3 — Carnival question and holiday repair | `FavorStory_150605_Content`, `4798–4808`: Carnival joy revives a question about threatened divine anger; on leave she adapts a tour invitation to one of Rover's three stated goals, initially frightens a vulnerable Echo, later acknowledges prying and the limits of her empathy, and treats after the Echo nods. Its later headshake/approach suggests Ragunna rather than the homeward plan. She names her own love of Ragunna without resolving every theological fact. | Holiday branches are alternatives and `4798/3` does not test categorical refusal. The Echo's destination preference is inferred from gesture and her question, not a second explicit yes; trust follows changed conduct, not forced capture. |
| P4 — applied conscience in later work | `5567/3/33`, `6587/3`, `5606/3/11–12`, `5643/2/3`, `5692/6/12–15`: she adapts a blessing to a nonbelieving sailor, consults pre-Order sea accounts while hypothesizing about the siren/Tidebreaker relationship, apologizes to Cetus in her own name rather than claiming Church authority, seeks noninjurious Echo solutions, and defends artistic expression even when it criticizes the Order. `QuestTree_Summary_230301` later reports that she uses her power to resolve the Order's evidence-erasure-device crisis at the Averardo Vault. | The ecology is Phoebe's uncertain account, not certified creature taxonomy or a completed direct whale conversation. The vault synopsis is a retrospective outcome, not Phoebe's direct line, precise power-mechanics demonstration, proof of advance knowledge or institution-wide restitution. EN calls the device a bomb; ZH/JA/KO do not require that mechanism. No universal renunciation of faith follows. |
| P5 — civic and doctrinal reform | `8869/5`, `9970/2`, `10625/6`, `11374/2`, `11375/2`, `11779/2`, `11983/1`: she coordinates protection/rebuilding, distinguishes physical cleansing from trauma care, argues for freedom of belief, prays with collective agency, can openly hug Echo friends, participates in discussing deletions from the Codex, and reports a less centralized civic arrangement. `QuestTree_Summary_240002` reports that postwar recovery exceeds her capacity and Rover takes some Septimont work. | The full `11779/2` talk order is informative: Phoebe's unspecified “this one” at T4 comes before Cartethyia names the Echo-distance rule at T5. It does not itself establish that Phoebe selected that rule for deletion, still less that every proposed reform was enacted. She remains a believer. A workload report is not a diagnosis or request for intimate rescue. |

An especially important correction is that faith, Church office, Fenrico's claims, and her own responsibility do not move in lockstep. In `4805/4` she says her doubt may be about herself rather than faith; in `4808/5` she interprets personal care and love of place as revelation while admitting unresolved questions. By `9970/2` she supports nonbelievers without coercion, and by `11375/2` a formerly hidden Echo affection can be public. This is a changing practice of faith, not a zero-to-one conversion into disbelief.

The source crosswalk marks all 26 accepted Phoebe turns in `4798/3` and all 23 in `4807/5` `play_voice: false`. Four localized text witnesses and the raw graph remain analyzable, but these actions do not contribute Phoebe lines to the selected four-dub performed-voice denominator. A future runtime capture can test staging and version-specific playback without changing this pinned mapping by assumption.

## Review performed and open checks

The Chinese profile, all five favor stories, all archive words, selected accepted Chinese direct dialogue across the major Ragunna, holiday, Cetus/vault, crisis, and reform families, and pivotal other-speaker context were reviewed. The English profile/archive and consequential English holiday/quest lines were read as witnesses. This is not an exhaustive line-by-line JA/KO semantic comparison, a complete branch realizability proof, or a human listening/visual pass. The separately existing visual profile is based on three client UI images; it does not prove runtime costume construction, facial acting, or animation.

Do not infer that Echo attachment is merely a charming quirk, that prayer is her only care method, that she has no institutional competence, that hesitation means indifference to abuse, that one holiday resolved all theology, or that warm Rover language establishes exclusive romance. Future scene generation must identify developmental phase, interlocutor, faith/institution distinction, branch, Echo consent, and what truths Phoebe has actually learned at that point.
