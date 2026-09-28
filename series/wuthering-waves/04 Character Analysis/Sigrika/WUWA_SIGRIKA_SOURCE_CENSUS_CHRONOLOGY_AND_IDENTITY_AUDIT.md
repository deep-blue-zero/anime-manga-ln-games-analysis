---
series: WUWA
character: Sigrika
artifact_type: audit
analytical_responsibility: "Source accounting, occurrence adjudication, chronology constraints, provenance gaps, and verification scope"
scope: SIGRIKA_COMMIT_PINNED_3_6_0_PRE_AV
analysis_generation: SIGRIKA_PRE_AV_V0_2
revises_local_generation: SIGRIKA_PRE_AV_V0_1
audio_revision: native_waveform_pass_completed
video_stage: deferred_owner_requested_local_1080p_or_larger
status: active_provisional
release_state: current_provisional_pre_video
analysis_authority_state: owner_adopted_current_provisional
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
intended_canonical_home: "series/wuthering-waves/04 Character Analysis/Sigrika/"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_current_git_authority: false
authority_adoption: owner_2026_09_23_text_audio_baseline
created: 2026-09-11
---

# Sigrika — source census, chronology, and identity audit

> **Current authority — owner adoption, 2026-09-23.** This document is current active-provisional authority for its declared analytical or planning scope and inspected text/audio evidence. Audiovisual and human-listening gaps limit only the corresponding claims. Chinese remains primary; source fact, inference, unresolved hypothesis, and value judgment remain distinct. [Packet entrypoint](WUWA_SIGRIKA_ANALYSIS_PACKET_README.md).

## Responsibility and scope

This document owns the input census, source-state conflicts, occurrence identity, chronological ordering rules, and mechanical audit. It does not replace the interpretive monograph or certify every possible Wuthering Waves source. “Complete” below means the selected, commit-pinned collection was accounted for, not that all game versions, all quest branches, or all audiovisual witnesses were acquired.

## 1. Evidence identity and authority

Sigrika is `西格莉卡 / シグリカ / 시그리카 / Sigrika`, playable role **1412**. Chinese `zh-Hans` governs semantic interpretation; EN, JA, and KO are official localized witnesses in this collection. Source commit is `353f2eaed119bc9f680eab92807d20ac75a79b40`. The lock reports game version 3.6.0 and resource version 3.6.6. These are source labels, not a claim about today’s public release.

The semantic bridge is `arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko`. The embedded source identifier also retains `arikatsu-3.6.0-353f2eae-4lang-v0.3.0`. These names are not silently collapsed. Installed-client raw audio authority remains separate from normalized semantic authority. The lock does not establish official-client normalized semantic parity or guaranteed future reacquisition. [SIG-E54](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e54)

### The freeze discrepancy

`SIGRIKA_READING_GUIDE.md`, `COLLECTION_AUDIT.json`, and `SIGRIKA_RELEASE_MANIFEST.json` describe a frozen, active-provisional collection. The downloaded `SOURCE_LOCK.json`, however, contains `source_generation_frozen: false` and `freeze_gate: pending_v0.5.1_phase_6_integration_and_freeze`.

The likely explanation is a later collection release retaining an earlier lock snapshot, but **that explanation remains an inference**. This packet does not edit source metadata or pronounce the earlier gate resolved. It binds its own claims to the downloaded bytes and pinned commit. A source-maintenance session should determine whether the lock is a deliberately historical dependency or stale metadata requiring a provenance-preserving correction. Textual interpretation is not blocked by that discrepancy; a claim of uniformly synchronized freeze metadata is blocked. [SIG-E54](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e54)

## 2. Census

| Evidence surface | Count | Denominator / qualification |
|---|---:|---|
| Contextual scene/action records | 252 | Includes other speakers, narration, projections, and relationship context |
| Contextual talk items | 2,584 | Not 2,584 direct Sigrika utterances |
| Contexts flagged with accepted technical speaker | 185 | Source relevance flag; occurrence adjudication still governs |
| Complete selected raw flow-state rows | 251 | One row may yield more than one selected action |
| Contextual text keys | 3,531 | Multilingual textmap projection, not independent events |
| Additional mention nominations | 546 | Includes repeats, summaries, mechanics, and other-character archive evidence |
| Direct identity candidates | 834 | 827 accepted, 4 rejected, 3 unresolved |
| Accepted direct story/message occurrences | 827 | 774 main speaker + 51 message speaker + 2 diary speaker |
| Source-voiced / explicitly unvoiced accepted occurrences | 593 / 234 | Unvoiced does not mean missing or nonexistent |
| Favor stories / favor-word archive entries | 5 / 73 | Narrative archive and semantic voice archive are distinct |
| Direct semantic voice lines | 666 | 593 story + 73 archive |
| Direct render associations | 2,668 | EN 668, JA 666, KO 667, ZH 667 |
| Direct runtime render-variant identities | 2,656 | Variants are not semantic lines |
| Direct unique PCM / FLAC identities | 2,652 / 2,652 | Actual FLAC and native PCM payload verified for every object in V0.2 |
| Direct retained FLAC bytes | 618,972,763 | Sum of unique acquired and verified FLAC objects |
| Counterpart accepted occurrences | 39 | Separate lore entity; upstream audit denominator |
| Counterpart voiced / unvoiced | 38 / 1 | Upstream occurrence audit; V0.2 voice rows checked separately |
| Counterpart semantic lines / render associations | 38 / 169 | Independently parsed in V0.2; excluded from direct totals |
| Counterpart unique FLAC identities | 157 | Separate scope in object routing and upstream audit |
| Combined unique audio objects / FLAC bytes | 2,809 / 665,901,951 | Both scopes, not direct-character behavior |
| Quest reference wrappers / distinct quest IDs | 128 / 24 | These do not constitute 24 fully collected quest graphs |
| WavesLine records | 11 | Wrapper records; 51 accepted direct message talk items above |
| Structured human-performance annotations | 0 | Every direct voice-line record is OPEN_unannotated |
| Acquired Sigrika image/video witnesses in this run | 0 | No Sigrika footage supplied or located in the inspected selected-AV branch |

All direct census values were recomputed from materialized records where the needed table was fetched. Counterpart occurrence counts remain attributed to the collection audit; V0.2 independently parses its 38 semantic voice rows and 169 embedded render associations. Its identity specification was separately read. The combined object crosswalk was parsed locally. V0.1 did not reenact the media checks. V0.2 acquired every routed archive and independently checked all 2,809 FLAC and native PCM payload digests; original WEM decoding was not repeated.

## 3. Occurrence identity: resolve before interpretation

| Technical ID / occurrence | Treatment | Reason |
|---|---|---|
| `150088` | 774 accepted direct occurrences | Main named identity, after exact exclusions |
| `200155` | 2 accepted diary occurrences | Authored internal self-address; not spoken performance |
| `300086` | 51 accepted message occurrences | Direct message surface, not 51 independent conversations |
| `200170` | Counterpart, not direct Sigrika | Nightmare interlocutor twists her thoughts |
| `12955/4/0`, `/1`, `/3`, technically `150088` | Rejected from direct; accepted for counterpart | The impersonation is exposed in the same scene |
| Generic `178` at `10663/3/6` | Rejected | Context identifies Aemeath’s introduction |
| Generic `178` at `12923/2/15–17` | Unresolved; context only | Observer identity is not established as Sigrika |

A compact locator `R/A/T` means source flow-state row **R**, decoded Actions-array index **A**, and TalkItems-array index **T**. It is not a chapter number. The full pattern is `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/flowState/flowstate.json#/R/Actions!/A/Params/TalkItems/T`. The exclamation mark records that `Actions` is a JSON-encoded field and must first be decoded. Action indices, action IDs, action GUIDs, scene IDs, text keys, and talk indices are preserved as different identifiers. [SIG-E24](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e24) [SIG-E52](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e52)

The counterpart is psychologically diagnostic because it uses recognizably painful material, but its attributed wishes are not interchangeable with Sigrika’s endorsed preferences. Her later direct admission that she has wished to escape corroborates that limited proposition. It does not authenticate every accusation. Likewise, a nightmare mother or friend is not a direct witness to the real person’s judgment. [SIG-E14](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e14) [SIG-E21](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e21) [SIG-E25](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e25)

The packet preserves the accepted classification of other nearby main-ID lines. It does not extend the exact impersonation decision to every ambiguous-looking scene by analogy. Where testimony occurs inside a manipulated space, the state tag and independent corroboration remain necessary even after speaker identity is accepted.

## 4. Chronology: partial order, not numerical sorting

| State | Source-relative position | What can be known / modeled |
|---|---|---|
| S0 — Home and anticipated responsibility | Earlier family formation narrated in the archive | Affection, expected future contribution, and anxiety about readiness; exact age unestablished |
| S1 — Gift, intervention, and school adjustment | Archive episodes before the central Dark Side crisis | Domain-limited rune ability, successful intervention with a remembered limit, and unfamiliar academic demands |
| S2 — Recognized student before the central confrontation | Early campus, tutoring, friendship, and festival participation before escalating ordeal | Public helpfulness and private pressure; later explicit refusal skills are not backdated |
| S3 — Escalating Dark Side ordeal | Distorted evaluations, rescue difficulty, and nightmare before supported final-entry choice | Self-blame and uncertainty; reflection speech does not establish real others’ opinions |
| S4 — Supported decision and confrontation | Final-entry deliberation → counterpart confrontation → immediate aftermath | Chosen action with uncertainty, refusal of hostile interpretation, and explicitly shared help; larger operation not wholly over |
| S5 — Bounded ordinary life and later work | Post-crisis ecology, research and optional activities | Saying no, modifying diary, fuller maternal conversation; not an omniscient or permanently symptom-free self |
| S6 — Denia’s outing, disappearance, and later understanding | Outing before the later reported letter and explicit nonreturn conversation | Suspicion precedes confirmation; friend-specific secrets remain gated; hope is not a witnessed reunion |
| S7 — Later academy/crossover/farewell material | Source families labeled 3.4/3.5 and later optional states | Ongoing academic limits, new peer learning, outward-facing plans; no invented adult biography |

The cooperation events are especially easy to misorder. `CoopActivity_Text1/2_501–505` and their corresponding actions show apology, overtraining, shared birdwatching, distressed retreat, and later joy. They interleave with the main arc. Treating the distressed rooftop as an automatically post-resolution relapse would manufacture a contradiction. Optional activities may be available in broad windows; not every pair receives a strict before/after edge. [SIG-E28](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e28) [SIG-E29](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e29) [SIG-E30](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e30) [SIG-E31](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e31)

The archive is another temporal layer. The early reassuring phone idle, later disclosure line, growth unlock, combat trigger, and narrative story cannot be sorted into biography solely by menu order. Birth date remains unknown despite a playable birthday greeting addressed to Rover. A culturally accelerated adulthood recognition does not supply a numerical age. [SIG-E06](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e06) [SIG-E17](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e17) [SIG-E55](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e55)

## 5. What was read, what was computed

The Chinese text of all 252 selected contextual actions was read, including narration and other-speaker passages. All five favor stories, all 73 favor-word entries, the profile fields and chain titles were inspected. The mention surface was read with duplicates, gameplay captions, other-character testimony, and summary-only records kept distinct. Raw action structure and additional text/choice keys were inspected; source summaries are distinguished from dramatized scenes. English archive content and selected contextual passages were compared, with targeted four-language close comparison at the decision, dependence, family-call, Denia, and photo-interpretation hinges. This is **not** an exhaustive close reading of every localization of every record.

The original V0.1 pass parsed the direct semantic/render tables and reaggregated existing signal fields. The V0.2 stage additionally fetched all nineteen routed archives, decoded and newly measured 2,652 direct plus 157 counterpart objects, verified their native payloads, and performed source-defined comparisons with explicit quality gates. No direct perceptual listening was performed. No screenshot, video frame, or character animation was reviewed; video is owner-deferred to a later full-resolution local stage. [Audio method](WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md); [acquisition manifest](AUDIO_ACQUISITION_MANIFEST.json). [SIG-E53](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e53)

### Mechanical results

All **2,584 contextual talk items** were aligned with the corresponding decoded raw action/talk item. Exact `TidTalk` equality was verified for the **2,555 items with text keys**; the remaining **29 option slots** do not contain a projected dialogue text key. Speaker IDs were checked for every item, and **10,104 localized content hashes** were recomputed. All **834 identity-candidate locators** resolved in the selected contextual ledger. Every direct render’s canonical PCM identity resolved in the fetched object crosswalk. These tests produced zero join errors. Sixteen downloaded evidence payloads matched their exact release-manifest SHA-256 entries. The release manifest’s own hash is recorded separately; it is not self-certified.

These checks prove correspondence among the fetched representations under the tested predicates. They do **not** prove interpretive correctness, completeness of the upstream game extraction, accurate diarization of uninspected audio, or the authenticity of every possible source beyond the declared collection.

## 6. Prior baseline and methodology reconstruction

Live Git inspection found the five exemplar character directories—Lynae, Aemeath, Denia, Cartethyia, and Chisa—but no Sigrika directory. Repository search found Sigrika discussed inside other characters’ packets; those discussions are interpretive precedents, not independent primary evidence. The Drive `Sigrika_v0_1` release folder contains a release manifest and tooling snapshot, not a prior character monograph. Therefore there is no invented “prior Sigrika dossier” to supersede and no empty reconciliation document.

The live reconstruction protocol, character-folder contract, and machine-voice protocol were read. Architectural inspection included Chisa, Denia, and Cartethyia packet entrypoints and a representative Denia specialist profile. The latest observed main head was `23a66270ba904338d7dbe0e95dd14abf18863e81`; individual method blob identities are recorded in the README. This was a read-only inspection, not a working-tree checkout or repository mutation.

The separately named AV collection/crosswalk/manifest specifications were referenced by the exemplars as proposed amendments; their standalone current files were not found in the inspected live framework tree/search. The supplied handoff’s AV rules therefore supply the explicit four-authority and multilingual planning contract used here. This limitation is disclosed rather than presenting uninspected specifications as read.

## 7. Residual gaps and abstentions

The canonical selected-AV branch inspected here contains a Cartethyia folder, not Sigrika footage. The supplied wheel and source ZIP contain software, documentation, tests, and reports—not Sigrika video samples. Absence from those inspected locations is not a claim that no official Sigrika footage exists anywhere. Those raw voice objects have now been retrieved and measured through their exact shard/member crosswalk. The earlier metadata-only limitation is closed, while direct perceptual listening and owner-deferred video remain separate responsibilities.

The aurora-flight quest is represented by a summary and soundtrack-unlock text, but its matching dramatized dialogue was not located in the 252 selected contexts. This packet preserves that summary-level narrative fact and does not manufacture a flight scene, camera analysis, or a detailed psychological transition from it. The raw selection and 24 quest IDs do not prove complete quest graphs. [SIG-E58](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e58)

Three identity candidates remain unresolved. The runes’ unknown civilization, exact chronological placement of some archive/optional lines, Sigrika’s full knowledge after the undisplayed Denia letter, and a future reunion remain bounded uncertainties. The text supports post-crisis change; it does not provide an indefinite follow-up study proving irreversibility.

## 8. Durable input identities

The analytical ZIP does not redistribute the raw game corpus or audio. The following manifest identifies downloaded inputs for reacquisition and exact reproduction. `SOURCE_INPUT_MANIFEST.json` preserves their full hashes, byte sizes, Drive IDs, and release comparisons; `SOURCE_AND_AUDIO_AUDIT.json` preserves the computed counts and acoustic aggregates.

| Downloaded input | Drive file ID | SHA-256 |
|---|---|---|
| `ACOUSTIC_RETRIEVAL_FEATURES.jsonl` | `1fDvYeHHBCUpQDXWrBYu4MtGqYLF-vZlm` | `f68c0e7b21259d76b85295bad8f75ac81712769b6e605a3d2807db9e761680a6` |
| `AV_Evidence_Toolkit_1.1.0-rc2-retiming.1.zip` | `user attachment` | `169d986c428eb123015f0a7d8a387f49c7c4870ed5e3e3a151fdd43fdb420e3d` |
| `COLLECTION_AUDIT.json` | `1DoQqBMxjfDXtOzFtzD5s0Uj7itiHAmx8` | `12f82e602c72cefb3a1dca0e3b5a49caaf3c2b2fc5a101d094ade825dc9a938d` |
| `COMPLETE_VOICE_LINE_ANALYSIS.jsonl` | `1GroeMrhr6KNRuEmdEsDgeMbbU6OZLItF` | `822c2cf36e06d1ec3c8759b08370d4cec698ff15664823f479b142800e63acc7` |
| `COMPLETE_VOICE_RENDER_ANALYSIS.jsonl` | `1vqieZn9onxLSATmKYWzyh86trxO_5_Xn` | `8500ce5bb9d3050b1f83ab808acfc1f754fe4968a9216cc7c8efce94dadfcad2` |
| `CONTEXT_TEXT_WITNESSES.jsonl` | `1sBhvUewk5FMFdKgH8oXgu18HXYQTcYGG` | `935ca052f62dbe37ce458ceb5782eedf76be6cf1e9ab8b0e97557612a4e19000` |
| `DRIVE_AUDIO_OBJECT_CROSSWALK.jsonl` | `1Y0H3QMRNJYu7uZBsW4UnlJbJOwveK1un` | `5bf9fe657778cf5450042431fa4c20523c6694b75263cd29b5db5dcf12676a96` |
| `FORM_IDENTITY.json` | `1bLQmntSbc1o0yclQkIfx4IsmPrzRHkVS` | `8a674b76d14600e0dd2df7508cbca87c0117858ef22037ae88108520960cd309` |
| `QUEST_CONTEXT_REFERENCES.jsonl` | `1DuFGrJRHg_qgQoGcIUwr0z9XyV5bb-m4` | `2973043268554427a80fdca5285021b286df5832930d8cf8076dff08099892d5` |
| `RAW_RELEVANT_FLOW_STATES.jsonl` | `1nUZ0NWlC-prLvopNAxwPJoO_mQYgmqyB` | `9c66758a5f461e12d1d19a0be73290ca0323b64aa162680cf835144d60c67ed9` |
| `SCENE_AND_EVIDENCE_LEDGER.jsonl` | `1LwfMzHzxE8svjS9CG4mwGdkQBzxy4sul` | `70f64f66d7ecf2536c8de511e2c2018b666d9bd2441ba990c4795cef9700e050` |
| `SIGRIKA_RELEASE_MANIFEST.json` | `1iJ95b9sEIetggqKQ-GDmtWvbb7agUEwF` | `aeb30ef56da7bf01181a1c5b8e78a2426fb80e43e9dbbd82ef139c7f9eae9cc1` |
| `SOURCE_LOCK.json` | `1fMQlMXpF1URONoiWI4em1AldeIfr04Ff` | `3d2873271b9b8b4b25eefd815526be0a27010de950089dde1f8a1bf3dc08b492` |
| `STATE_AND_FORM_MEMBERSHIP.jsonl` | `14DZhANkwdjMgQ6FNZw7vsiXhIMQvythG` | `edb2fdd02df54ab9b6aad1d313e39439a766fc56d49e8c9c11fa270af0737167` |
| `WAVESLINE_MESSAGES.jsonl` | `1eMz92ZJpLK_wIeUD1lNAJdM2sqnAqRTo` | `f2d37e3b9500f239d45b55d26d2cdd67456c7e0e3ab87ecd2af6e8ed438929a3` |
| `av_evidence_toolkit-1.1.0rc2+retiming.1-py3-none-any.whl` | `user attachment` | `27a844ac0c8876824617fb83a7ea3f5ab1c01392b607c436e21f86cd0809d784` |
| `character_source_package.json` | `1yXLvvpBYute8uO5fScV6WjqVc6H7uCya` | `36b31175eb37e33eb0baa0ce98c188c85da843d139e6df4bddc978787c7a5b28` |
| `occurrence_identity_crosswalk.jsonl` | `1UZnZ6h49wscMuNTLiZFqj2s75-Wr5sr3` | `d464269426dd6751d56b27f0f472d105d446b5d75c43e747c562d21dd7f290da` |
| `source_mentions.jsonl` | `1E4tXy2aNkn-Fhx7ibptMO731NeN46-jC` | `8b803602e2c69e91c2ff9a4532fb5f50ec46768487bf2175ceedbcee89faa560` |

## 9. V0.2 audio source and reproducibility extension

[AUDIO_ACQUISITION_MANIFEST.json](AUDIO_ACQUISITION_MANIFEST.json) identifies all nineteen actual Drive archives and their verified release hashes. [AUDIO_SOURCE_INPUT_MANIFEST.json](AUDIO_SOURCE_INPUT_MANIFEST.json) identifies the additional counterpart voice table and the exact machine-analysis inputs. [AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json](AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json) provides independent corpus totals, language/source partitions, quality exclusions, and source-unvoiced action boundaries. The [method](WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md) explains why native PCM payload verification is not the same as reimplementing the framed PCM identity hash or re-decoding original WEM.

All 2,809 objects have zero decode/hash failures and pass gate-duration invariants. Five selected remeasurements reproduce their full result records exactly. Detailed object/association measurements are staged in a separate local evidence supplement, not inserted as raw evidence into the analytical repository. No canonical Drive evidence was rewritten, and no Git or registry mutation occurred.
