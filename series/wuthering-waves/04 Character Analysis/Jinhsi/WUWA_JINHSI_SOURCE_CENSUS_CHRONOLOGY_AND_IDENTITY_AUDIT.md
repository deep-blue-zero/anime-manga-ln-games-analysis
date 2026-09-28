---
series: WUWA
character: Jinhsi
artifact_type: source_census_chronology_identity_audit
scope: JINHSI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: JINHSI_PRE_AV_V0_1
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

# Jinhsi — source census, chronology and identity audit

## Reproducible selected-scope census

Private source roots: `ANALYSIS/Characters/Jinhsi`, `_voice_media/character/complete_voice_corpus/Jinhsi/v0_1`, `_research/character_packets/Jinhsi/audio_work`. The pinned collector reports 185 relevant *full* flow states, 3,465 contextual text keys, 142 quest references/44 distinct quest IDs and three message records. These are a retrieval denominator, not a claim that all contextual text is Jinhsi speech. Direct-identity nominations: 617; accepted solo: **584**; rejected: **33**; unresolved: zero. Among accepted occurrences, 472 carry source voice markers and 112 do not. The archive adds five favor stories and 75 voice entries. The selected voice corpus has 547 semantic lines; 539 complete and **eight missing**. It has 2,209 render associations (EN 553, JA/KO/ZH 552 each), 2,042 runtime rows, 2,038 distinct measured FLAC objects (526,464,066 bytes), four repeated PCM rows, and 32 `runtime_dispatch_unsupported` reason rows. Zero local measurement failures applies to the objects *that decoded*, not to the eight missing semantic lines. Collection integrity passes while `voice_completeness_valid` is false.

`semantic_voice_line`, `render_association`, `runtime_object_row` and `unique_FLAC` are different denominator types. No “547/547 complete” claim is licensed. Eight missing voice occurrences `flow#/3722/0/1–8` have four-language installed WEM membership (32 rows) but unproved runtime event-to-media resolution/playback. Their text is still available as normalized semantic evidence; their performed quality is not.

A separate external-source audit now finds **31** selected Jinhsi event-family lines for which the EN/JA/KO/ZH-labeled render rows all point to the *same* `WwiseExternalSource/gl_vo_*.wem` virtual path and have the *same* canonical PCM SHA-256 per line. That is one proved audio object per line, not four proved localized performances. Four of those lines also have a source WEM basename different from the current text key. This does not alter the 547 semantic-line denominator or erase valid PCM bytes, but it downgrades four-language performed completeness for that subset to `language_dispatch_unresolved` and leaves some text→audio joins unproved. The private `_research/character_packets/GLOBAL_EXTERNAL_SOURCE_LANGUAGE_ALIAS_AUDIT_2026-09-27.md` has the twelve-packet breakdown [JIN-E38].

Three additionally close-read actions contribute 18 already-selected voiced Jinhsi occurrences, not 18 new lines beyond the 547 denominator. `2515/3` has seven lines and 28 distinct localized PCM objects; `3157/2` has six and 24; the `7456/2` memory-handbook reprise has five and only five distinct `gl_vo` PCM objects despite 20 language labels. Thus the combined close read has 18 semantic lines, 72 associations and 57 distinct PCM identities. This object proof is not a human-heard or runtime-route proof [JIN-E39–E41].

The independently read `584/5` action has fifteen accepted technical-186 Jinhsi source-text occurrences, all `play_voice: false`, and therefore **zero selected voice-line/render objects**. They are already included in the 112 accepted source-unvoiced direct-occurrence denominator, not a new addition to the 547 semantic voice lines. A flow template carries camera and montage metadata, but no direct viewing; no exact-state quest reference was retained in this selected package. Its unvoiced status cannot be generalized into a claim that no client build could ever play sound at that point [JIN-E42].

## Attribution and false positives

Playable role is 1304. Source-named scene speaker 186, communications 1212 and message speaker 701099 are technical presentations of Jinhsi at reviewed occurrences, not a blanket equivalence for every row with the same integer. `IDENTITY_REVIEW.md`, `occurrence_adjudication.json` and reconciled `occurrence_identity_crosswalk.jsonl` provide per-occurrence decisions. Of 33 rejected nominations: `11247/1/0` and `11248/1/0` are Sanhua despite a Chinese Jinhsi label (English/Japanese and asset support Sanhua); `12554/4/0` is Copo addressing her; `16530/2` generic turns belong to Hsin; `17181/2/0,2,6,8,11` are an unnamed visitor seeking her; `17636/6/31–34` are unidentified remote speakers. In the *mixed-speaker* `2516/3/12–35` exchange, only indices `/13`, `/16–18`, `/20`, `/22`, `/24`, `/26`, `/28` and `/33` are the hidden Changli turns rejected from Jinhsi; Jinhsi's replies between them are accepted. She addresses “Teacher Changli” at `/34`, before contextually Changli-attributed generic-speaker-999 turns `/36–39`. Jinhsi's speaker-186 closing question and resolve at `/40–41` are accepted as hers. These are substantive disambiguations, not inconvenient missing data. Never promote `IDENTITY_DISCOVERY.json` nominations over adjudicated crosswalk.

The `7844/1` event shows a different ownership limit from the rejected-speaker cases. Its Jinhsi-labeled technical-186 rows are accepted *character associations*, but contextual T6–7 call the figure a Tethys-simulated Echo Cube image based on a memory, only resembling real Jinhsi. Nine of her ten accepted text rows there are source-voiced; the ellipsis T11 is `PlayVoice=false`. The related `8329/1` has seven voiced technical-186 rows. A technical speaker attribution is not, by itself, evidence of the actual magistrate's diegetic presence or a played route connecting the two states. Treat this as an explicit `diegetic_instantiation` boundary, not as a failed speaker ID [JIN-E37].

## Chronology and graph discipline

| Approximate narrative stratum | Anchors | What the packet may and may not assume |
|---|---|---|
| Infant/child past | `flow#/3722/0`; `FavorWord_130411–130412`; `flow#/3153/4` | Jué's rescue and snow/sea recollections precede public office; adult interpretation of childhood is retrospective. Eight narration lines lack proven sound. |
| Early magistracy | `FavorStory_130401–130404_Content`; `FavorWord_130425–130426` | Initially young and doubting, she builds policy capacity over years. Archive narrative compression is not a date-perfect day-by-day transcript. |
| Undated archive self-addresses | `FavorWord_130410_Content`; `130429_Content` | The first advocates a human route when prayer is the only apparent resource; Ascension V permits a personal reading of fate in meeting Rover. Menu order does not prove when a political conviction changed, that it changed, or that Rover reciprocated. EN's contrast is stronger than ZH/JA/KO. |
| Public invitation before the private alliance | `flow#/2948/1`; `FavorStory_130405_Content` | The one-sequence citywide message names one important but unidentified guest, calls the proposed meeting a request, grants freedom of action and asks the public to help. It does not disclose the token or guard, show guest assent, or publicly identify personal traits. |
| Rover arrival/Jinzhou crisis and Chapter-IV-labeled research exchange | `FavorStory_130405_Content`; `flow#/1191/3`; `2513/3`; `2514/6`; `2515/3`; `2516/3`; `584/5` | Planned token and covert guard precede disclosure. At `1191/3` Rover can join or consider, not categorically refuse at that node; the two replies rejoin before nonbarter, postcrisis-departure and secrecy lines. After Rover's Black Bloom report at `2515/3`, Jinhsi infers a Black Shores link, flags possible Fractsidus monitoring, and promises to share what she learns from Jué; fulfillment is not shown there. The separate `584/5` state offers a tentative Rover–Jué origin question and a limited data-card report, not an origin answer or a certified handover. Its fifteen Jinhsi turns are source-unvoiced. Hidden Changli is separate. |
| Memory-handbook retelling of first meeting (presentation order, not a second event) | `flow#/7456/2` contrasted with original `1191/3` | The side action reprises the three-day appointment and hand-offer narration but puts Rover's “hello” and projection question consecutively. Those are mutually exclusive opening options in the original graph. Do not invent a second meeting, original route combining both, completed handshake or four independent performances from the five shared-PCM voice rows. |
| Prepared Jinzhou defense before Firmament | `flow#/2301/4` | Jinhsi credits local shield work, names capital aid and says she cannot habitually rely on Jué's power while still using Jué's information. Three Rover response wordings yield exclusive Jinhsi replies at TalkIDs 17, 18–19 or 20, then rejoin at 21; do not stitch them into one memory. |
| Norfall Disruptor decision | `flow#/1693/3`, controller-linked quest `140000004` | One 18-item `ShowTalk` sequence; Jinhsi secures or issues firing permission, accepts decision risk and orders department-wide support for General/Rover. ZH/EN/KO explicitly assign her battle-outcome burden at TalkItem 10, while JA asks for trust there after broad responsibility at TalkItem 9. Authorization is not proof of a fired or successful shot. |
| Mt. Firmament | `flow#/3144/4`, `3153/4`, `3157/2`, `3209/3`, `3223/3`, `3160/5–3163/2` | Weakening Jué connection and temporal crisis drive high-risk intervention. At the chamber approach she treats still water as a possible shortcut while withholding a verdict on its cause and the next move until closer inspection. Her later plan includes survival and Jué's rescue, not simple suicide. Static row number is not absolute narrative chronology. |
| Companion/festival | `flow#/4130/8–4133/4` | Optional fair turns can express leisure/intimacy; explicit choice-path reconstruction required before quoting a continuous scene. |
| Later Xuanfang emergency and requested service | `flow#/17181/2`; `17636/6` | Initially attempted inquiry and emergency personal-key route do not license general intervention. After the immediate case, Yangyang asks to stay, Qiuhong welcomes the help and Jinhsi promises future Jiyan consultation for a temporary transfer; completion is not shown. The two `ShowTalk` actions each retain one sequence. |
| Later civic/ecology | `flow#/20166/7–20167/7` | Do not retroject later travel reflection into early crisis scenes. |

Two test-labeled states are deliberately quarantined from stylistic examples: `flow#/6617/2/0–2` and `12745/1/2,9` have blank English lines despite accepted technical identity. Card-game rows such as `14714/5–14716/1`, `15295/1`, `15420/1` are legitimate short event utterances, but thin evidence for broad temperament. Message records are pointers and should be followed into flow states, not counted as absent dialogue or extra independent utterances. Static text order, voice source keys and graph reachability are separate matters.

At `584/5`, this distinction is unusually visible: the raw item list starts with TalkIDs 1 then 0 and has no explicit `TalkSequence`/`SequenceTransitions`; several attached player captions have no action targets. Only `_202` and `_203` explicitly jump to distinct closing replies `_204` and `_205`. The authored union is readable, but one cannot certify the full played sequence, concatenate the two endings, or infer a four-dub performance from it [JIN-E42; C41].

## Localization and authority

Chinese normalized dialogue is the semantic anchor; EN/JA/KO are witnesses whose phrasing can shift self-reference, office vocabulary, certainty and intimacy. Particularly review the later EN “Hsi” self-reference (`flow#/20167/7`) against Chinese before asserting a birth name or second character. The game client supplies stronger raw authority for its own art and decoded media objects, but decoded WEM membership does not validate normalized speaker identity or reachable story branch. The frozen generation and `draft_noncurrent` analytical status are orthogonal. A fuller 3.6+ or live-client comparison could change coverage without retroactively making this packet current.
