---
series: TBHX
artifact_type: evidence_ledger
artifact_role: targeted_av_evidence_ledger
scope: S01E01-S01E24_post_freeze_targeted_reinspection
generation: V2
status: active_provisional
phase: 2
canonical_home: 04 V2 Evidence and Revision
media_home: 04 V2 Evidence and Revision/Targeted AV Evidence
source_boundary: Targeted audiovisual clips, stills, and derived navigation surfaces supplied or generated after prospective episode freeze; source episodes remain E01-E24 Mandarin-primary audiovisual Season 1
prospective_freeze_rule: Never rewrite frozen episode bodies. New audiovisual evidence routes through this ledger, mutable topical ledgers, claim-revision infrastructure, and later specialist/full-series synthesis.
transition_vocabulary: PRESERVE | STRENGTHEN | REVISE | DOWNGRADE | REJECT | OPEN
legacy_tbhx_transition_crosswalk: PRESERVE=CONFIRMED; STRENGTHEN=STRENGTHENED; REVISE=NARROWED/CORRECTED as appropriate; DOWNGRADE=weakened confidence; REJECT=OVERTURNED; OPEN=UNRESOLVED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-16
last_updated: 2026-08-16
---

# To Be Hero X V2 — Targeted Audiovisual Evidence Ledger

## 1. Responsibility

This is the canonical intake and routing surface for **post-freeze targeted audiovisual evidence** in the *To Be Hero X* V2 corpus.

It exists for cases where the prospective episode reading is already frozen, but a later analytical question benefits from direct reinspection of a short source sequence in continuous motion and/or with synchronized audio. Typical triggers include:

- a supplied MP4 excerpt that makes duration, motion, blocking, editing, gesture, vocal delivery, music, or silence newly inspectable;
- high-resolution stills that expose small but consequential visual details;
- a later request to test whether a screenshot-based inference survives continuous video;
- a character or relationship claim whose **magnitude** is difficult to judge from transcript and contact-sheet evidence alone;
- a formal claim that depends on sequence rather than isolated composition;
- a mature synthesis claim that needs stronger primary-source routing before publication.

This artifact is **not** a substitute for the complete episode bundles, frozen `TBHX_V2_E##_DEEP_READING.md` documents, or the later Phase-7 primary-source locator ledger. It is an evidence bridge between them.

### Governing rule

> **Targeted reinspection may revise the current understanding of an episode without rewriting what the prospective episode pass originally established.**

The episode body remains historical evidence of what the V2 reader responsibly concluded at that broadcast boundary. New source inspection is recorded here with an explicit transition and then propagated to the appropriate mutable authority surface.

---

## 2. Why a separate layer is necessary

The V2 episode pipeline already contains extensive screenshot, contact-sheet, Mandarin-text, and synchronized-audio infrastructure. Later episodes—especially E19, E20, E22, E23, and E24—also received dedicated motion/video audits.

Earlier episodes do not uniformly have a standalone motion-audit artifact. Creating a new episode-specific document for every later 30–120 second reinspection would fragment the evidence corpus and produce near-duplicate analytical homes.

This ledger solves that problem by giving targeted clips one stable responsibility:

1. preserve the exact media supplied for reinspection;
2. distinguish raw source excerpts from derived navigation images;
3. document what continuous motion or audio adds beyond the frozen still/transcript reading;
4. state what the evidence **does not** establish;
5. assign a claim transition;
6. route the consequence into the canonical topical home.

The ledger is cumulative and mutable until the corpus is frozen.

---

## 3. Evidence packet architecture

Raw/derived media are stored under:

`04 V2 Evidence and Revision/Targeted AV Evidence/`

Each reviewed sequence receives a packet folder:

`TBHX_E##_SHORT_DESCRIPTIVE_SCOPE/`

Each packet should contain only evidence needed to recover the review:

- source clip(s), preferably MP4 with synchronized original audio;
- user-supplied stills when analytically relevant;
- generated contact sheets or frame strips for navigation;
- optional audio excerpt only if a later specialist pass requires it;
- no duplicate full-episode source when the complete source is already canonically retained elsewhere.

The ledger, not the folder tree, is the semantic authority.

### Stable entry identifier

Use:

`TBHX-AV-E##-NNN`

Example: `TBHX-AV-E11-001`.

IDs are permanent. A later correction updates the same entry and preserves its transition history.

---

## 4. Required evidence fields

Every substantive entry should contain:

- **Episode and sequence**
- **Why reinspection was requested**
- **Raw media inventory**
- **Drive packet location**
- **SHA-256 where locally recoverable at intake**
- **Nominal source timestamp / clip-local locator**
- **Evidence mode**
  - `MOTION_CONFIRMED`
  - `FRAME_CONFIRMED`
  - `AUDIO_CONFIRMED`
  - `AUDIOVISUAL_STRUCTURAL`
  - `INTERPRETIVE`
  - `OPEN`
- **Pre-existing claim**
- **New evidence**
- **Strongest warranted conclusion**
- **Limits / counterreadings**
- **Transition**
  - `PRESERVE`
  - `STRENGTHEN`
  - `REVISE`
  - `DOWNGRADE`
  - `REJECT`
  - `OPEN`
- **Downstream routing**
- **Propagation state**

### Transition semantics

| Transition | Meaning in this ledger | Legacy TBHX architecture equivalent |
|---|---|---|
| `PRESERVE` | prior formulation survives substantially as written | `CONFIRMED` |
| `STRENGTHEN` | direction survives and source confidence, magnitude, or scope increases | `STRENGTHENED` |
| `REVISE` | core insight survives but formulation, mechanism, scope, or emphasis changes materially | `NARROWED` or `CORRECTED` |
| `DOWNGRADE` | evidence is weaker or less discriminating than previously believed | confidence reduction |
| `REJECT` | prior claim no longer survives source inspection | `OVERTURNED` |
| `OPEN` | serious alternatives remain unresolved | `UNRESOLVED` |

This dual notation preserves the mature TBHX architecture while using the project's current cross-series revision vocabulary.

---

## 5. Locator discipline

When the supplied excerpt filename contains an episode-source range, record it as **nominal source-range metadata**, not automatically as a frame-perfect locator.

Continuous-video review should preferentially use a **clip-local offset** because extraction/transcoding may retain encoder delay, preroll, or other small duration differences.

For a mature Phase-7 locator, cross-check against the canonical episode bundle and convert to:

`S01E## | source HH:MM:SS.mmm | program +HH:MM:SS.mmm | CN cue if applicable | frame/motion ref`

Do not invent cue numbers or exact source milliseconds from a filename alone.

---

# 6. Active evidence entries

## TBHX-AV-E11-001 — Queen vs X and the immediate post-defeat collapse

### Status

- **Episode:** S01E11
- **Sequence:** eighteenth tournament final, Queen vs the unknown new X, followed by media reaction and Queen's private slump
- **Intake date:** 2026-08-16
- **Review reason:** test the earlier claim that X's victory is unusually destabilizing to Queen, and determine whether continuous motion/private aftermath supports a stronger psychological reading than the frozen E11 transcript/frame analysis alone
- **Current transition:** **STRENGTHEN**
- **Propagation state:** targeted evidence captured; formal addendum routed; claim-confidence and Queen specialist synthesis pending

### 6.1 Evidence packet

Drive packet:

`04 V2 Evidence and Revision/Targeted AV Evidence/TBHX_E11_QUEEN_X_AFTERMATH/`

- packet folder ID: `17s7Kf6xRvpOWkV4XwsKPXZcd5lWmBRAc`
- packet manifest: `TBHX_E11_QUEEN_X_AFTERMATH_MEDIA_MANIFEST.md` (Drive `17WeQSnSdYJPsCv-2M-yaqQMIJD9HrLSy`)

#### Raw source excerpt

`TBHX_E11_QUEEN_VS_X_AND_AFTERMATH_CLIP.mp4`

- source filename supplied in chat: `TO.BE.HERO.X.S01E11.2160p.HC.BILI.WEB-DL.AAC2.0.H.265-ZigZag-00.19.48.644-00.21.40.297.mp4`
- nominal episode-source range encoded in filename: `00:19:48.644–00:21:40.297`
- locally measured encoded duration: approximately `114.346 s`
- video: H.264, 3840×1636, approximately 24 fps
- audio: AAC synchronized track present
- local intake SHA-256: `a8c161313f1cca1530e01e797e3748d36d2c7e108945ac358ea60539182ec3ab`

**Locator warning:** the encoded clip duration is slightly longer than the nominal source-range difference in the supplied filename. Use clip-local offsets for this packet and backfill exact canonical source locators during Phase 7 rather than pretending the filename is frame-perfect.

#### User-supplied stills

`TBHX_E11_QUEEN_SLUMP_OVERHEAD.png`

- high-angle view of Queen seated/crouched on the floor beside the low table
- multiple bottle-like containers visible around the table/room
- local intake SHA-256: `d3ff706eec3f3782c848fad19ab492b7194eed2bf5995e48086e7c7ec25cc80d`

`TBHX_E11_QUEEN_SLUMP_CLOSE.png`

- Queen folded over her knees with face obscured by arms/hair
- multiple bottle-like containers visible in background
- local intake SHA-256: `032d45a1943813b520f50d17cf1dfc632b4ddb370c8096dbbe5363c70ad99ed6`

#### Derived navigation surfaces

`TBHX_E11_QUEEN_VS_X_CONTACT_SHEET.jpg`

- derived from the supplied clip for navigation only
- local intake SHA-256: `5d2d546916cabf438e73ce2d58c6a2ab6dc2e3565d936eb9d3fee00f415f3e33`

`TBHX_E11_QUEEN_AFTERMATH_CONTACT_SHEET.jpg`

- derived from the supplied clip for navigation only
- local intake SHA-256: `f287f6aa08b70c082fc4b791cec4b8da2d4a50a535279e84b07a814c11a0ce64`

Contact sheets are not substitutes for continuous video when sequence or causation matters.

### 6.2 Pre-existing E11 claim state

The frozen E11 reading already established several propositions that remain valid:

1. Queen enters the tournament expecting to reach X through a system she understands and intends to reform.
2. The unknown entrant is administratively illegible even though the tournament/public system can recognize him as X.
3. Queen is defeated by a mechanism E11 does not explain.
4. The encounter challenges Queen's assumption that control of the formal hierarchy is sufficient to make hero society governable.
5. **The defeat does not by itself disprove Queen's political diagnosis.**

The pre-existing visual ledger also identifies the contrast between Queen's elaborate gold/white authored hero image and X's comparatively under-branded presentation as a **legibility asymmetry**, not proof that simplicity is morally superior.

Those claims are preserved.

### 6.3 Motion-confirmed additions

The supplied clip strengthens the magnitude and embodiment of the event.

#### A. The final does not acquire the normal temporal grammar of a competitive exchange

Queen is presented in full authored hero regalia: gold/white costume, crown-like headpiece, staff/weapon, upright readiness, and a highly legible public silhouette. X is comparatively visually plain.

The sequence then gives Queen almost no usable contest through which to interpret the opponent. The decisive transition is experienced less as a conventional exchange of techniques than as a failure of comprehension. Queen is left supine, eyes widened, attempting to understand what has happened.

**Evidence mode:** `MOTION_CONFIRMED` + `INTERPRETIVE`.

#### B. The episode sustains incomprehension instead of letting Queen immediately recover composure

The clip continues through public media framing of the new X. The public field can name the result—an unknown entrant has become X—before Queen or the institutional knowledge system can explain its cause.

This prolongation matters. The defeat is not visually contained as one lost match before the episode moves on. The world begins narrating the result while Queen is still without an adequate causal account.

**Evidence mode:** `AUDIOVISUAL_STRUCTURAL`.

#### C. Queen's private body contracts after her public/sovereign image fails

The aftermath removes her crown, weapon, ceremonial costume, podium/rule geometry, and public posture. In private clothing she sits low on the floor despite a large, comfortable, status-coded room. Her knees are drawn inward, arms close around the body, and later her face is buried into the folded posture.

The spatial reversal is unusually strong:

> **Queen normally expands jurisdiction through rule and occupies public space as an authored sovereign image; after X, she contracts herself into the smallest available private bodily footprint.**

This is stronger evidence of destabilization than a transcript statement that she lost or was surprised.

**Evidence mode:** `MOTION_CONFIRMED` + `FRAME_CONFIRMED` + `INTERPRETIVE`.

#### D. Bottle imagery materially strengthens the coping/crisis reading

Several bottle-like containers are visible on/around the low table and in the room, and continuous footage includes Queen handling/drinking from a bottle-shaped container during the slump sequence.

The visual pattern strongly supports the inference that the scene is coding extended solitary drinking after the defeat.

However, the current packet does **not** contain an independently verified label or dialogue line identifying the beverages as alcoholic. Therefore:

- **fact:** multiple bottles/bottle-like containers are present and Queen drinks from one;
- **inference:** the scene is strongly alcohol-coded;
- **not yet promoted to fact:** exact beverage contents or degree of intoxication.

**Evidence mode:** `MOTION_CONFIRMED` / `FRAME_CONFIRMED`; alcohol identification = `INTERPRETIVE`, medium-high confidence rather than direct lexical fact.

### 6.4 Strongest warranted claim

> **X's victory produces a rare crisis of control in Queen. The event does more than frustrate her tournament ambition: it confronts her with an actor whom neither her own rule-authority nor the institutions she intends to reform can adequately predict, classify, or explain. The immediate private aftermath renders that epistemic and sovereign failure bodily—Queen abandons the public Queen presentation, withdraws into a closed posture on the floor, and is surrounded by a visual field strongly coded as solitary drinking.**

A useful causal formulation is:

`systemic diagnosis → confidence in self-authored ascent → encounter with administratively illegible X → instantaneous unexplained defeat → public system names result before cause is understood → private contraction / coping crisis`

The clip therefore **strengthens**, rather than replaces, the E11 thesis that Queen's confrontation with X attacks the assumption of *controllable legibility* underneath her sovereign reform project.

### 6.5 What the packet does not establish

Do **not** infer from this sequence that:

- Queen's political diagnosis is disproven;
- Queen abandons her reform project permanently;
- X intends to humiliate or psychologically break Queen;
- Queen is clinically depressed;
- Queen is alcohol-dependent;
- the bottles' contents are textually confirmed alcohol;
- Queen's later ideological development is caused only by X;
- Qīng's subsequent intervention can already be characterized from this packet.

The sequence establishes magnitude of destabilization, not a total psychological diagnosis.

### 6.6 Revision transition

**Primary transition:** `STRENGTHEN`

Legacy TBHX equivalent: `STRENGTHENED`.

Earlier formulation:

> X's defeat challenges Queen's assumption of controllable path/legibility.

Current formulation:

> X's defeat challenges that assumption **and produces a sustained, embodied private crisis of control**, making the epistemic wound psychologically concrete.

### 6.7 Downstream routing

#### `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md`

When stabilized, add a Queen/X claim transition for:

- magnitude of destabilization;
- distinction between political diagnosis and sovereign self-confidence;
- evidence grade: motion-confirmed + frame-confirmed + interpretive;
- alcohol-coded coping as a bounded inference rather than lexical fact.

#### `VISUAL_AUDIO_MOTIF_AND_FORM_LEDGER.md`

Add/retain a current Phase-2 formal proposition that Queen's post-X collapse is a strong case of **spatial contraction after representational/jurisdictional failure**: the public sovereign body loses crown, rule geometry, weapon, elevated posture, and legible control, then becomes physically small in private space.

#### `09_QUEEN_ORDER_GOVERNANCE_SOLITUDE_AND_REFORM.md`

Later specialist synthesis should use this sequence when distinguishing:

- Queen's serious institutional diagnosis;
- Queen's belief in sovereign mastery as the solution;
- X as a crisis of epistemic/control confidence;
- the later movement toward more relational, revisable, and self-binding rule.

#### `CHARACTER_RELATIONSHIP_AND_RECOGNITION_LEDGER.md`

No new Queen↔Qīng conclusion should be propagated from this packet alone. The following relational recovery belongs to a separate E12 targeted review if supplied.

---

# 7. Requested targeted-review queue

This queue records sequences where continuous audiovisual review is likely to change analytical confidence rather than merely illustrate an already secure screenshot claim.

| Priority | Episode | Requested sequence | Primary analytical question | Intended routing |
|---|---:|---|---|---|
| **1** | E12 | Queen's continued slump through Qīng/Lucky Cyan's intervention and clear emotional turn | How does Qīng enter Queen's closed state; what changes in voice, posture, distance, music, light, and self-understanding? | Queen specialist; relationship/recognition; visual/audio ledger |
| **2** | E10 | crash recorder / Luo testimony / Qīng recovery and public reversal | How do recording, music, faces, pauses, and media circulation restore provenance to the dead and to Qīng? | Lucky Cyan specialist; public narrative; audio/form |
| **3** | E14 | DJ Shindig's takeover of Glimmer Lab from onset through Luo Li's resistance | Is coercive synchronization principally rhythmic, vocal, spatial, or all three; how does Luo Li change the medium of efficacy? | Luo Li specialist; audio/form; mechanics |
| **4** | E15 | young Wang Yi noise/quiet formation plus an adult Ghostblade phone/silence sequence | What does negative space actually sound like, and how does silence force others to author meaning? | Ghostblade specialist; language/voice; audio/form |
| **5** | E09 | one musically complete Qīng/Luo performance, ideally including `My Color` context | How does relational musical space differ from later Lucky Cyan institutional performance? | Lucky Cyan specialist; Phase-5 music/voice |
| **6** | E04 | Lin's public self-disclosure/reclamation with Xiao Yueqing reaction | At what audiovisual point does public performance become answerable self-authorship rather than dispossession? | Lin/Nice/Moon specialist; personhood; language/voice |
| **7** | E16 | family/dinner sequence through onset of shared Fear contamination | Does individual distress visibly/sonically precede shared contamination, supporting amplification over invention? | mechanics; relationships; audio/form |

### Lower-priority rule

E19, E20, E22, E23, and E24 already have dedicated motion/video audits. Additional clips from those episodes should be requested only for a specific unresolved performance, sound, emotional-duration, or choreography question.

---

# 8. Intake workflow for future clips

When a new targeted clip is supplied:

1. identify the episode and narrow analytical question;
2. preserve the source excerpt in the relevant packet folder;
3. compute local file metadata/hash when possible;
4. inspect continuous motion before relying on contact sheets;
5. inspect user-supplied high-resolution stills for details the clip view may obscure;
6. distinguish direct visual/audio fact from inference;
7. compare against the frozen episode claim and current mutable topical authority;
8. assign `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`;
9. update this ledger entry;
10. propagate only the mature consequence to the relevant topical ledger, claim-revision ledger, or specialist synthesis;
11. never rewrite the prospective episode body merely to hide the earlier state of knowledge.

For an ambiguous clip, retain the media and mark the claim `OPEN`; evidence preservation does not require forced interpretation.

---

# 9. Retrieval order

For a mature claim affected by targeted AV evidence:

1. `TBHX_CURRENT_STATE_AND_CORPUS_MAP.md`
2. relevant stabilized longitudinal ledger
3. `TBHX_V2_TARGETED_AV_EVIDENCE_LEDGER.md`
4. frozen episode deep reading
5. referenced raw clip/stills inside `Targeted AV Evidence/`
6. episode-level motion/video audit if one exists
7. `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md` once stabilized
8. Phase-7 primary-source locator ledger for final citation-grade routing

This order preserves both the latest authority and the historical path by which it changed.
