---
title: "Revue Starlight — V2 Audiovisual Reconciliation"
artifact_id: REVUE_STARLIGHT_ANIME_AV_RECONCILIATION_V2
artifact_type: claim_revision_ledger
series_id: revue-starlight
version: "2.0"
status: canonical
authority_scope: retrospective_revision_of_listed_animated_corpus_claims
source_boundary: "TV01–TV12, OVA01–OVA03, and the complete 2021 sequel film, including credits and post-credit material"
canonical_home: "series/revue-starlight/06 Evidence and Indexes/16_ANIME_AV_RECONCILIATION_V2.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Revue Starlight — V2 Audiovisual Reconciliation

**Spoilers through the film's post-credit scene.** This record applies to the listed claims in the original OpenAI synthesis. It integrates observations from [Gemini's CP16 freeze](../checkpoints/RS-AV-R2-GEMINI-CARBON/CP16_independent_freeze/07_freeze/RS_AV_R2_IMMUTABLE_FREEZE_MANIFEST.md) and [CP18 Track C handoff](../checkpoints/RS-AV-R2-GEMINI-CARBON/CP18_track_c_reconciliation/README.md) (archived with [CP17A](../checkpoints/RS-AV-R2-GEMINI-CARBON/CP17A_comparative_audit/README.md) under [checkpoints/RS-AV-R2-GEMINI-CARBON/](../checkpoints/RS-AV-R2-GEMINI-CARBON/PUBLICATION_README.md)) where they survived source review. The [verified witness inventory](../01%20Source%20Lock%20and%20Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md) gives the source identities and clocks. The [V1 erratum](../07%20Audits%20and%20Manifests/V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md) records the V1 package checksum mismatch and locates overlapping text.

## Review record

| Field | Recorded scope |
| --- | --- |
| Inspection route | Original bundle-mediated synthesis, then Gemini's continuous AV run, then selected frame, cue, and measurement checks on the supplied objects. |
| Clock and precision | See the [witness clocks](../01%20Source%20Lock%20and%20Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md#verified-audiovisual-containers). Caption times locate text. Sampled frames establish their contents at the stated times. Cross-object synchronization claims require their own calibration. |
| Sampling and authority | Gemini reported continuous Japanese audio and 1 fps native visual sampling. Direct local frame, credit, and stream checks support the observations specified below. Listening-only details retain their attribution or remain open. |
| Knowledge boundary | Gemini froze its independent run before accessing the V1 comparison. Prior familiarity with the TV07 reveal limits the TV06 reading. |
| Adjudication | The 22 CP18 items are routed below (`37` sub-claim transitions; `required_items_unresolved: []`). Open questions include TV05's formal bout result, an exact festival date, and disputed performed wording. |

### Reconciliation summary

```yaml
av_reconciliation:
  route: BUNDLE_MEDIATED -> CONTINUOUS_AV -> BUNDLE_MEDIATED
  av_object: "16 primary Japanese Matroska program containers (TV01-TV12, OVA01-OVA03, MOVIE; 25,842.313 s video-endpoint span) plus parallel 6-ch 5.1 film container MOVIE-MIX and 13 Japanese analysis ASS files; SHA-256 digests in ../01 Source Lock and Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md"
  clock_offset_seconds: 0.0
  calibration_anchors: "CP16: 10.01 s synthetic 23.976 fps / stereo sync ruler (3 flash-tone pairs), TV01 00:00-04:05 speech-to-ASS calibration window, beginning/middle/end ffprobe packet PTS anchors across TV/OVA/MOVIE containers (MOVIE video first_pts +0.021 s), and >=3 speech-onset anchors per unit across 16 units (48+ anchors; flagging TV10 +58.30 s ASS commercial-break drift). Stage 3 receiver: container stream/chapter bounds, ASS cue intervals, and 1920x1080 frame checks (including TV05 cues 268-272 and 352-355, Chapter #0:4 at 22:30.891 s, 22:31-22:32 picture cut, and 23:35 credit card)."
  alignment_precision_seconds: 0.5
  effective_visual_sampling: "1.000 fps native video pass (t = k + 0.46 s stride at 23.976 fps; +/-0.15 s verified speech-to-ASS alignment), supplemented by 2-4 fps frame grids and 23.976 fps frame-exact 1920x1080 stills (+/-0.042 s) on load-bearing cuts, props, and credits"
  blind_order_achieved: true
  queue_items: 37
  transitions: {PRESERVE: 9, STRENGTHEN: 13, REVISE: 4, DOWNGRADE: 2, REJECT: 0, OPEN: 9}
  new_findings_accepted: null
  contested_items:
    - "REC-02 / REC-18: standalone ontological inferences from MOVIE-MIX 0:a:1 LFE silence and center-channel dialogue routing downgraded under standard theatrical post-production conventions"
    - "REC-04: stale container and ASS digests in CP18 proposal replaced with rehashed physical witnesses matching CP16"
    - "REC-07: CP17A cross-bout hit retracted at CP18; CP18 Futaba/Kaoruko pairing transposition at TV05 15:56 and 16:21 corrected by local frame check"
    - "REC-08: CP17A conflation of TV05 21:57-22:03 reflection with Fly Me to the Star retracted at CP18 and verified by 22:01 frame, cues 352-355, and 22:30.891 chapter"
    - "REC-09: CP18 3m37s delay span narrowed (~2m38s from 17:38 to 20:15.5); exact song onset, waka allusion, and address shift held OPEN"
    - "REC-11: TV08 42.05 kg scale shot located at 02:45 (before 41.92 kg at 09:40.5) and London rank-eight board at 08:49 rather than 13:02; kidney-weight gloss held OPEN"
    - "REC-19: CP18 TV12 letterbox locator corrected from 10:20-11:40 to 19:47 and 20:28; MOVIE 01:22:31.5 'steps past' narrowed to movement at the pink T mark"
    - "REC-22 (with audio-only quotations in REC-10, REC-12, REC-13, REC-15, REC-21): transcript-divergence leads and uncorroborated Japanese/French transcriptions held OPEN"
  verification_routes:
    - "Local SHA-256 rehashing and ffprobe stream, chapter, and PTS inspection across all 17 Matroska containers and 13 Japanese ASS files"
    - "CP18 Stage 5.2 targeted native-AV and 2-4 fps frame-grid re-inspection on TV05 (16:35-17:05, 21:10-22:45) and OVA03 (03:25-04:00)"
    - "Stage 3 receiver unburned 1920x1080 frame, crop, credit-card, and ASS cue verification across TV02, TV03, TV05-TV12, OVA01-OVA03, and MOVIE"
  provisional_observations:
    - "REC-08: Gemini listening report of unpitched spoken inner narration over underscore at TV05 21:57-22:03 (corroborated visually by 22:01 closed mouth, ASS cues 352-355, and 22:30.891 chapter boundary)"
    - "REC-17: Gemini listening report of wordless solo violin in TV07 ending (corroborated visually by blank singer credit at 23:35) and episode-by-episode Stem I-III classifications"
    - "REC-02 / REC-18: CP18 reported dBFS channel measurements on MOVIE-MIX 0:a:1"
    - "REC-09, REC-10, REC-11, REC-12, REC-15, REC-21, REC-22: uncorroborated Japanese and French audio-only wording and lyric-divergence proposals"
  open_disputes:
    - "Source-indeterminate within anime boundary: REC-05 exact 2019 festival calendar day and curtain-splice frame-exactness; REC-07 formal Claudine-Hikari Day 4 bout result; REC-08 TV05 underscore cue title; REC-20 post-credit audition production and result"
    - "Pending dedicated listener or full-run measurement: REC-09 exact song-entry interval, waka lyric, and bare-name address; REC-10 OVA02 exact Japanese wording and TV07 reset-date details; REC-11 spoken kidney-weight gloss; REC-15 full picture-book transcription, cross-version goddess count, and OVA02 Japanese couplets; REC-17 full ED stem/onset table; REC-19 continuous TV12/MOVIE crop scan; REC-21 OVA02 exact Japanese wording and MOVIE 01:54:13 bare-name address; REC-22 seven subtitle-vs.-audio divergence leads"
  required_items_unresolved: []
```

- **Counting convention (`22` CP18 docket entries → `37` sub-claim transitions).** Twelve docket entries bundle distinct sub-claims—for example, strengthening a visual locus while leaving an unshown outcome or uncorroborated transcription `OPEN`, or preserving a V1 lyric-relay reading while downgrading a standalone `5.1` mix inference. Counting each explicit bold transition label once per adjudicated sub-claim yields `37` transitions across all `22` entries: `PRESERVE` (`9`: `REC-02, 03, 08, 10, 14, 15, 18, 20, 21`), `STRENGTHEN` (`13`: `REC-02, 05, 06, 07, 08, 09, 11, 12, 13, 15, 17, 18, 19`), `REVISE` (`4`: `REC-01, 04, 16, 19`), `DOWNGRADE` (`2`: `REC-02, 18`), `REJECT` (`0` on V1 analytical claims; non-analytical `CHECKSUM_AUDIT.md` findings are isolated in the [V1 erratum](../07%20Audits%20and%20Manifests/V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md), and two incoming `CP17A` assertions on TV05 were retracted at `CP18`), and `OPEN` (`9`: `REC-05, 07, 09, 10, 15, 17, 20, 21, 22`, with subsidiary open notes in `REC-08`, `REC-11`, `REC-12`, `REC-13`, and `REC-19` listed in `open_disputes` rather than double-counted).
- **Findings count.** The checkpoints preserve the independent readings, comparative audit, and CP18 docket. A separate out-of-queue acceptance tally under [Protocol §4.4](../../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md#44-new-findings) is unavailable from those records (`new_findings_accepted: null`). The count of 14 covers docket entries (`REC-04, 05, 06, 07, 08, 09, 11, 12, 13, 15, 16, 17, 18, 19`) where locally checked witness, frame, prop, signage, or credit observations entered V2, including evidence used in the listed transitions.
- **Blind-order qualification.** `blind_order_achieved: true` records that Gemini froze its `CP16` observation and unit-reading log (`corpus_exposure: false`) before opening any `V1` file or claim formulation at `CP17A`. Two explicit bounds apply: Gemini's disclosed pretraining familiarity with Daiba Nana's `TV07` loop reveal restricts `REC-01` (`TV06` `23:48.25` `今回の再演`) to retrospective foreshadowing, and `CP18`'s targeted `TV05` and `OVA03` re-inspections occurred post-exposure as bounded Stage 5.2 return checks.
- **Required vs. optional scope (`required_items_unresolved: []`).** Every `REQUIRED` obligation for this retrospective claim-revision release—verified witness digests and clocks (`REC-04`), `TV05` Day 4 pairing/strike and narration-vs.-ED separation (`REC-07`, `REC-08`), `TV06` stinger provenance and clasp/title-card checks (`REC-01`, `REC-09`), `OVA` timeline/`99.419` signage and `OVA03` four-speaker care attribution repair (`REC-05`, `REC-16`), frame-checked `TV`/`MOVIE` props, credits, and Scope windows (`REC-06, 11, 12, 13, 17, 18, 19`), `5.1` mix-inference bounding (`REC-02, 18`), V1 core preservation (`REC-03, 10, 14, 15, 20, 21`), and the V1 structural/checksum erratum—is resolved. Remaining `OPEN` items are either genuine primary-source indeterminacies (kept open without speculative inference) or `OPTIONAL` audio/measurement enrichments on which no V2 canonical claim depends; `REC-22` and uncorroborated Japanese or French transcriptions become `REQUIRED` only before a future revision quotes those contested intervals verbatim as canonical text.

## What the two readings establish together

The OpenAI reading of TV05's counterfeit duet identifies a relationship in which Mahiru has come to depend on being needed. The overhead shots sharpen the point. Even the underground audition cannot confine attention to one pair. Karen and Mahiru's bout draws Hikari's attention from Claudine, and Karen looks back when Hikari falls. The sequence stages both the contingency of caring about another person and the vulnerability that comes with it. Mahiru's reflection before the credits carries that insight into ordinary life. In OVA03, the girl who feared becoming superfluous can use what she knows to help Hikari directly, then leave room for Futaba, Junna, Maya, Claudine, Kaoruko, and Nana to contribute. Correctly assigning those actions makes the ensemble argument concrete.

The audition board first represents this ensemble as numbered places. The blank ninth row becoming Karen's row makes room for an entrant without settling what the school's play will do with nine performers. The [original intertext reading](../05%20Full-Series%20Synthesis/08_STARLIGHT_INTERTEXT_SCRIPT_REWRITE_REENACTMENT_AND_REPRODUCTION.md) shows where that further work happens, in the 99th class changing the inherited production. The film finally puts the familiar pink stage mark on an ordinary audition-room floor with other candidates and staff. The framing lets us recognize the mark while the scene changes what standing there promises. The earlier reading's distinction between destructive, defensive, and generative emptiness helps interpret the cut away from Karen's unshown result. She has a next stage whose outcome remains available to be made.

## Reviewed claims

Each numbered group below identifies its older home and the evidence for the scope of its revision. A sample time identifies a frame or cue and an interval identifies the relevant scene. Terms and titles read from the picture are distinguished from lyrics or speech. The local receiver used clean frames, selected higher-rate sequences, stream metadata, measurements, and supplied text layers. Listening observations are attributed to Gemini where the receiver did not independently hear the source. This is a retrospective comparison. Each primary witness is identified in the [source supplement](../01%20Source%20Lock%20and%20Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md).

### TV02–TV03 and TV09 — the ninth row

**REC-06 · STRENGTHEN.** The earlier synthesis links the move from eight to nine to Karen's interruption and the class's rewriting of *Starlight*. Its primary homes are the [ensemble study, § IX](../05%20Full-Series%20Synthesis/06_SEISHO_99TH_CLASS_ENSEMBLE_AND_CHARACTER_ECOLOGY.md) and [Karen and Hikari study, §§ IV–V](../05%20Full-Series%20Synthesis/02_KAREN_HIKARI_PROMISE_SELFHOOD_AND_RIVALRY.md).

In TV02 at `07:15` and again around `23:51`, the hanging board has eight visible rows. TV03 shows a blank ninth row at `23:17.5` and then Karen's name at rank nine around `23:24.5`, with Hikari at eight. TV09 around `14:13–14:22` links Hikari's arrival with an eight-person audition and says Karen, formerly last, was dropped from the cast. The TV02/03 board is an observation of the prop and the TV09 lines are a separate account of the replay. The pairing makes the ninth entry legible as a change in participation. It leaves the board's hardware, the audition's rule in every replay, and the school cast's criteria to their own evidence.

### TV05 — Day 4 bouts

**REC-07 · STRENGTHEN and OPEN.** Read the [chronological ledger, § VIII](./14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md) and [Revue system study, § VIII](../05%20Full-Series%20Synthesis/07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md) with this sequence.

| TV05 time | Reviewed observation |
| --- | --- |
| `15:56` | Maya and Futaba face one another on the stairs. |
| `16:21–16:25` | Kaoruko closes on Junna, who carries the bow. The picture confirms a second pairing. |
| `16:43–16:48` | Hikari and Claudine occupy the rooftop while Karen and Mahiru move below. The shots establish a shared line of sight, and Japanese ASS cue lines 268–269 locate the calls and reactions. |
| `16:49–16:55` | Claudine takes advantage of Hikari looking away and strikes from within their own contest. Hikari falls and is shown still wearing the blue cloak. Cue lines 270–272 support the sequence and show Karen's attention turning to Hikari. |

This supersedes the “cross-bout hit” description in CP17A and corrects CP18's transposition of Futaba and Kaoruko in the other matches. The formal Claudine–Hikari result stays **OPEN**. The fall and the day's closing announcement are evidence of action and closure of the session, with the result of the particular bout unestablished. The eyelines and cut support the distraction reading. A general claim about the hall's acoustics or an official bye for Nana would need further evidence.

### TV06 — the damaged clasp and the replay stinger

**REC-01 · REVISE provenance.** CP16's execution inventory records that Gemini knew the substance of TV07's reveal from pretraining. The frozen TV06 reading preceded inspection of TV07 and access to the OpenAI analysis, according to the run record. The `23:48.25–23:51.55` Japanese cue naming this replay (`今回の再演`) supports a retrospective foreshadowing reading. It supplies no independent blind forecast of the later reveal. The review keeps separate the point at which TV06 presents this wording and the significance assigned after TV07.

**REC-09 · STRENGTHEN and OPEN.** The earlier [Futaba and Kaoruko analysis, § XVIII](../05%20Full-Series%20Synthesis/05_MAHIRU_FUTABA_KAORUKO_CARE_DEPENDENCE_AND_DIFFERENT_ROADS.md) and [chronological ledger, § IX](./14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md) read the Revue as a shift in who can act and who can stand alongside the other. TV06's local frame sequence at `19:40–19:51` shows Kaoruko moving against her own clasp, Futaba intervening, and the clasp visibly marked around `19:49.5`. The `20:15.5` frame contains the Revue of Promise title card and the song label. This placement lets the scene postpone naming the promise until after the interruption. The packet gives incompatible starting points for the delay. Even `17:38` to `20:15.5` is about 2m38s. The exact song-entry interval, proposed waka allusion in the performed song, and address-form claim remain open pending dedicated verification.

### TV08 — the weight of Hikari's loss

**REC-11 · STRENGTHEN.** Carry forward the [Karen and Hikari study, §§ VIII–IX](../05%20Full-Series%20Synthesis/02_KAREN_HIKARI_PROMISE_SELFHOOD_AND_RIVALRY.md) and the [Revue system study, § IV](../05%20Full-Series%20Synthesis/07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md) on the cost of extraction. On the TV08 witness, the scale reads **42.05 kg** at `02:45` and **41.92 kg** at `09:40.5`. The shot reuses the scale composition for the visibly different reading. The 130 g difference is calculated from the two readings, several minutes apart in screen time. CP18's proposed `09:36–09:46` interval contains the later reading. Its `13:02` board locator lands on the Tower Bridge scene. The London board around `08:49` establishes Hikari's displayed entry at rank eight at that point in the montage.

The repeated shot gives a visible, measurable shape to Hikari's changed experience after the London defeat. Body-weight fluctuation remains a possible in-world reading of the scale alone. The wider juxtaposition of loss, dulled performance, and the Giraffe's explanation motivates the literary inference that extraction has embodied consequences. A literal mass conversion rate for radiance and CP18's specific kidney-weight attribution remain open.

### TV10–TV12 — cloaks, clasps, and who acts

**REC-12 · STRENGTHEN.** The [Maya and Claudine study](../05%20Full-Series%20Synthesis/04_MAYA_CLAUDINE_RIVALRY_PERFECTION_AND_EXPOSURE.md) carries the rivalry and chosen exposure argument. On TV10 around `18:36–18:38`, Karen's action and the ejected clasp belong to the decisive exchange with Maya. At `19:10–19:14.5`, Claudine starts with hers attached, puts her hand on it, and is then shown without the cloak. Distinguish the pair's formal result from the different ways Maya and Claudine come to stand without their cloaks. Choosing to share exposure is a reading of Claudine's action in context. The reported French response near `20:24` remains open as an exact quotation.

**REC-13 · STRENGTHEN.** TV11 `01:05.5` and `01:11.5` juxtapose the cut at Hikari's hand and the blood-marked fastener. TV12 `16:36.8` shows Karen's crown hairpin descending into the stage machinery. Her gold clasp at `18:05.6` is luminous and visibly marked. At `21:35` both figures reach the pink mark with garments still on their shoulders. Read these images alongside the [Karen and Hikari study, §§ XI–XII](../05%20Full-Series%20Synthesis/02_KAREN_HIKARI_PROMISE_SELFHOOD_AND_RIVALRY.md) and [visual grammar study, § VI](../05%20Full-Series%20Synthesis/10_VISUAL_CINEMATIC_GRAMMAR_MOTIFS_AND_STAGE_MACHINERY.md). The repeated use of bodily and personal objects makes choices visible at each stage. The cross-cut images leave the causal mechanics of theatrical fuel and the material process of clasp repair to interpretation. The disputed TV12 lyric is listed below.

### OVAs — festival time and backstage care

**REC-05 · STRENGTHEN and OPEN.** OVA01 at `00:09.5` displays fifty days until the festival, and at `01:20.5` the fitting board says `聖翔祭 2019`. OVA02 at `00:31.5` displays twenty-nine days. OVA03 at `00:16.5` shows the batting-cage marker `160 km/h / 99.419 mi/h`. At about `05:58`, OVA03 presents the production entrance signage also seen in TV12 around `23:14`. Supplement the [series architecture study](../05%20Full-Series%20Synthesis/01_SERIES_ARCHITECTURE_TV_OVAS_FILM_AND_DEVELOPMENT.md) and the [OVA sections of the chronological ledger](./14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md) with these visible anchors. A shared production is supported. Early March is an inference from season and precedent, with the exact day and the asserted frame-exact splice at the curtain left open.

**REC-16 · REVISE.** Correct four assignments in the [chronological ledger, § XVIII, lines 953–956](./14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md). The sampled shots, the timed English text, and Gemini's audio report agree on the attribution at the level stated here. The text is used as a timing and sense aid.

| OVA03 time | Earlier ledger | Reviewed assignment |
| --- | --- | --- |
| `03:28–03:37` | Junna provides the remedy | Futaba presses Hikari's wrist. |
| `03:38–03:44` | Maya brings tea | Junna brings tea. |
| `03:46–03:51` | Claudine brings chocolate | Maya brings chocolate. |
| `03:52–04:00` | Futaba and Kaoruko do hair and makeup | Claudine takes hair and asks Kaoruko to do the makeup. |

Mahiru warms Hikari's hands around `03:12–03:24`. Nana joins with banana therapy around `03:26`. The [ensemble study, § XIII](../05%20Full-Series%20Synthesis/06_SEISHO_99TH_CLASS_ENSEMBLE_AND_CHARACTER_ECOLOGY.md) correctly draws the larger conclusion about care distributed among classmates. Karen anticipates Hikari's nerves and involves them, and ordinary nervousness persists even after the extraordinary finale. The correction strengthens that reading by giving each action its performer.

### Film framing and Position Zero

**REC-19 · REVISE and STRENGTHEN.** The film's verified source stores `1920 × 1080` video. The active picture measures `1920 × 804` (about `2.388:1`) in sampled windows near `01:22:31`, `01:55:08`, and `02:00:01` on the MOVIE clock. TV12 at `10:25` fills its frame. The desert's new-chapter title at `19:47` and the shot near `20:28` visibly use bars, while `21:00` fills the frame again. This corrects CP18's claimed `10:20–11:40` letterbox placement. Leave its exact TV12 width, change boundaries, and all-film crop continuity to a full measurement.

The film frames show Junna's boot by a pink T (`01:22:31.5`), broken Tokyo Tower material amid the desert T (`01:55:08`), and a pink floor mark between white marks in the audition room (`02:00:01.5`). The sampled Junna sequence shows movement at the mark and then cuts away. “Steps past” overstates what the sequence establishes. The juxtaposition strengthens the account of theatrical marks changing function in the [Revue system study, § VII](../05%20Full-Series%20Synthesis/07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md) and the [visual grammar study, § XX](../05%20Full-Series%20Synthesis/10_VISUAL_CINEMATIC_GRAMMAR_MOTIFS_AND_STAGE_MACHINERY.md). In the room, the same shape serves the practical business of casting.

## Language and music

### TV05 narration and ending credits

**REC-08 · PRESERVE and STRENGTHEN.** Keep the statement cited by the [Mahiru study](../05%20Full-Series%20Synthesis/05_MAHIRU_FUTABA_KAORUKO_CARE_DEPENDENCE_AND_DIFFERENT_ROADS.md), [chronological ledger](./14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md), and [motif index](./15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md). At `21:57.06–22:03.40` the Japanese cues record Mahiru's reflection that wanting to make people dear to her happy gives her a way to shine again. The `22:01` frame holds on her closed mouth. Cue lines 352–355 distinguish the reflection from the subsequent exchange with Karen. Gemini's targeted listening reports spoken inner narration over underscore. The verified container's ending chapter begins `22:30.891`, the new ending image is present by `22:32`, and credits at `23:35` name *Fly Me to the Star* and Mahiru. This supports distinct narration and ending cues, retracting the earlier comparison's objection to V1's placement of the reflection. The name of the underscore stays open.

**REC-17 · STRENGTHEN and OPEN.** The [musical dramaturgy study](../05%20Full-Series%20Synthesis/09_MUSIC_SONG_JAPANESE_VOICE_AND_MUSICAL_DRAMATURGY.md) gains a concrete comparison. In the same ending-theme position at about `23:35`, TV07 still credits *Fly Me to the Star* but has no named singer, whereas TV05 credits Mahiru. This is a direct change in the credits. CP16 reports an instrumental performance in TV07, with violin in the place of the vocal. The absence of a credited singer supports the reported absence of vocals. Around TV12 `22:21.5–22:23.5`, the finale instead credits `星のダイアローグ` to Starlight Kukugumi, alongside distinct insert-song credits. The return of the opening-theme title alongside the class production makes a third, ensemble-level use of the ending. Episode-by-episode stem classifications and the reported instrumentation or exact performance onsets remain open.

### Film cue and credits song

**REC-02 and REC-18 · PRESERVE, STRENGTHEN, and DOWNGRADE.** Keep the [musical dramaturgy study, §§ XVIII–XIX](../05%20Full-Series%20Synthesis/09_MUSIC_SONG_JAPANESE_VOICE_AND_MUSICAL_DRAMATURGY.md) on the distribution of the worn-script stanza across Maya, Claudine, Junna, and Nana and on the limits of mix evidence. Nana's final place in that relay, around MOVIE `01:58:11–01:58:27`, remains important to the interpretation that she can allow a story to reach its end. This is an existing reading, retained with its voice-attribution basis. At MOVIE `01:58:52–01:58:56.5` the consecutive credits give a named cue for the climax, `スーパー スタァ スペクタクル`, and credit Tatsuya Katō for its composition and arrangement. The subsequent theme credit for `私たちはもう舞台の上` explicitly gives Yūki Honda the prelude and Jun'ichi Satō the composition and arrangement of the song.

Use MOVIE-MIX `0:a:1` for discrete channel measurements. Its verified stream identity is distinct from the stereo MOVIE listening witness. A cue title and credit identify the piece, while edit boundaries and constituent musical ideas need their own evidence. CP18's meter values are reported results. Low-frequency levels and dialogue routing by themselves have little force as evidence about the status of the Giraffe or the fictional stage. Center-channel dialogue and bass management admit ordinary production explanations. The worn-script claim depends on the succession of voices and scene context.

## Retained interpretations and open evidence

The V1 specialist homes carry their original arguments except where the claim-level decisions narrow or correct them. This crosswalk covers the rest of the CP18 docket, including proposals for which the receiver found insufficient corroboration.

| CP18 item | Decision and home |
| --- | --- |
| REC-03 | **PRESERVE** the [full-series method](../00%20Frameworks/RevueStarlight_Full_Series_Analytical_Method_v1.md), [synthesis architecture](../00%20Frameworks/RevueStarlight_Multi_Document_Synthesis_Architecture_v1.md), and their specialist homes. The current [corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md) routes the retrospective corrections. The [noncurrent checkpoint archive](../checkpoints/RS-AV-R2-GEMINI-CARBON/PUBLICATION_README.md) preserves publication derivatives of the frozen unit readings. New sequential publication follows the repository's project admission and architecture rules. |
| REC-04 | **REVISE** the new witness record with the [verified source supplement](../01%20Source%20Lock%20and%20Inventory/SOURCE_WITNESS_SUPPLEMENT_V2.md). The V1 inventory still defines the source boundary. |
| REC-10 | **PRESERVE** the [Junna and Nana study](../05%20Full-Series%20Synthesis/03_JUNNA_NANA_MEMORY_REPLAY_AND_AUTHORSHIP.md) on the shift from a shared *Starlight* to Nana's private replay and Junna's qualification “for now”. OVA02 `05:52–06:07` pairs Junna's defense of the value of a supporting role with an explicit claim of authorship in the auxiliary English cues and Gemini's reported listening. That supports the change from collecting other people's maxims to owning an insight. The exact Japanese wording, reset-date sequence, and roster details remain **OPEN**. |
| REC-14 | **PRESERVE** the [Revue system study](../05%20Full-Series%20Synthesis/07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md)'s spectator-role taxonomy, the Giraffe's ambivalence, and the different registers of the stage. The Day 4 scene supplies another instance where a spectator position can change within a performance. |
| REC-15 | **PRESERVE** the [intertext study](../05%20Full-Series%20Synthesis/08_STARLIGHT_INTERTEXT_SCRIPT_REWRITE_REENACTMENT_AND_REPRODUCTION.md)'s six distinct operations of repetition and its account of how the inherited play is reauthored. **STRENGTHEN** with the legible title `THE STARLIGHT GATHERER` on TV09's book at `05:32–05:34`. The complete page transcription, goddess count across versions, and OVA02 Japanese quotations remain **OPEN**. |
| REC-20 | **PRESERVE** the [endings study](../05%20Full-Series%20Synthesis/12_ENDINGS_GRADUATION_NEXT_STAGE_AND_REPRODUCTION.md)'s three forms of emptiness and its account of an ordinary audition with a new, uncertain future. The production Karen auditions for and the result are **OPEN**. |
| REC-21 | **PRESERVE** the [ethics study](../05%20Full-Series%20Synthesis/11_ETHICS_PERSONHOOD_DESIRE_MEMORY_AND_SELF_AUTHORSHIP.md)'s reading of `奪う`, agency, and possession. In OVA02 `06:17–06:32`, the English cue and Gemini's reported listening agree on the sense of Maya thanking Hikari for taking the lead and reserving the right to take Claire back. The scene supports a reading of taking a role within reciprocal challenge. Keep the proposed exact Japanese wording and the film's single bare-name address near `01:54:13` **OPEN** pending corroborated speech and addressee checks. The [motif index](./15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md) remains subject to the [erratum](../07%20Audits%20and%20Manifests/V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md). |
| REC-22 | **OPEN** the proposed audio corrections at TV03 `18:36`, TV10 `20:24`, TV12 `20:37.7`, and MOVIE `25:34`, `33:08`, `01:02:39`, and `01:59:36`. These are transcript-divergence leads. The [language index](./15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md)'s source recheck requirement applies to exact quotation. The open issues need a time-matched listen by a qualified Japanese listener, and a French listener for the TV10 response. |

The reader can reproduce the scene observations with the hashed source objects and the listed locators. The original Gemini observations, comparative audit, and CP18 proposals remain attributable to their frozen records, with the two TV05 retractions recorded at CP18.
