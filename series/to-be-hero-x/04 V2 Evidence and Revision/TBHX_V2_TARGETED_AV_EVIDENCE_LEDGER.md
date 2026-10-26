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
last_updated: 2026-10-25
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

## E05–E07 Gemini V2 accepted tranche — 2026-10-24

Archive SHA-256 `7114b52b2d873fb1505546f3962ba0b61317f4ca6e7b373be5525813a0fea216`; 28 members/27 verified payload checksums. The 30-finding matrix was recorded before canonical edits. [Formal audit](Targeted%20AV%20Evidence/TBHX_V2_E05-E07_AV_FORM_MICROSEQUENCE_AUDIT.md) owns full provenance, timing, form, source QA, and Phase 5 routing; [Yan causal audit](Targeted%20AV%20Evidence/TBHX_V2_E05-E07_YAN_MO_RETROSPECTIVE_AV_EVIDENCE_AUDIT.md) owns commission/coercion/disposal/strategy.

| Entry | Current transition | Accepted evidence / limitations | Propagation |
|---|---|---|---|
| `TBHX-AV-E05-001` | `REVISE / STRENGTHEN` | Native WEB 0 at 20:33.000; solid 1 at 20:35.200. No universal person-to-point equation or frame-exact duration. | master; mechanics; Specialist 07; Doc 18 queue |
| `TBHX-AV-E06-001` | `REVISE` | Native Chinese conditional support/no indefinite waiting; actual Japanese localization differs. No abandonment/hero-status condition; audio delivery unverified. | master; relationships/Chinese; Specialists 07/16; Doc 17 |
| `TBHX-AV-E07-001` | `REVISE` | Yang-centered recollection is high visual inference; displayed Shang/Xia names preserved; focalizer not every speaker; guilt not intentional non-rescue. | master; Specialist 07; Chinese/Doc 17; Docs 18–20 queue |
| `TBHX-AV-E07-002` | `REVISE / STRENGTHEN` | Retrospective paid commission plus coercion/disposal/expectation engineering; intended Yang versus actual Shang; unresolved administrative chain and foresight retained. | master; mechanics qualification; Specialist 07; institutional/Phase 5 retrieval |

Both are completed analytical audits within their stated source scope. Codex used targeted contact sheets and individual native/source screenshots, text witnesses, and metadata; no independent continuous playback or audio audition is claimed. Producer reports retain attribution. Remaining obligations `AV-D01–07` explicitly cover continuous timing, shooting/voice turns, Cyan-specific concern, original-speed audio/music, release alignment, proposed agency line, and administrative/disposal detail. At this tranche receipt, full-season coverage remained external work; the later remaining-arc receipt below records the now-supplied bundles and still-open channel debts for Documents 18–20. Frozen episode bodies are unchanged.

## Remaining-arc Gemini receipts — 2026-10-25

The ten V1 bundles covering E01–E04 and E08–E24, together with seven separately supplied master/SDH/quote/name files, are received and adjudicated. Archive integrity, full material text coverage, version dependence and targeted native-frame checks are distinct from producer-reported continuous/audio inspection. The source files remain external. Ten matrices record candidate IDs, current authority, actual checks, alternatives, transitions and required source work; copied frozen bodies do not create independent corroboration.

| Permanent entry | Evidence packet / full matrix | Current transition | Accepted result / limits | Actual propagation / retrieval |
|---|---|---|---|---|
| `TBHX-AV-E01-001` | [E01-E04 audit](Targeted%20AV%20Evidence/TBHX_V2_E01-E04_GEMINI_AV_HANDOFF_AUDIT.md) | `REVISE / PRESERVE` | Correct E01 cue 134 interval-collapse diagnosis and current twenty-first tournament ordinal; preserve Moon fate and exact bearer uncertainty. | P2-CR-C08; language/Doc 17; chronology; Specialist 01 |
| `TBHX-AV-E08-001` | [E08-E10 audit](Targeted%20AV%20Evidence/TBHX_V2_E08-E10_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / REVISE / OPEN` | Qualify E10 formal naming to displayed Fear (not Fear Particles); preserve musical provenance. Donor identity, counter and coin pairing need matched native evidence. **Current: donor and pairing resolved, counter narrowed, by `TBHX-AV-E09-001` (below).** | Chinese-language, mechanics, chronology and institutions current errata; P2-CR-CH04, N01, L06; Documents 18–20 queue |
| `TBHX-AV-E11-002` | [E11-E12 audit](Targeted%20AV%20Evidence/TBHX_V2_E11-E12_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / REVISE` | Retain existing Queen crisis and relational recovery; reject compact speaker, tournament-history and exact-time errors; keep granular corrections distinct. | P2-CR-CH05/06, R03; existing E11-001 remains independent |
| `TBHX-AV-E13-001` | [E13-E14 audit](Targeted%20AV%20Evidence/TBHX_V2_E13-E14_GEMINI_AV_HANDOFF_AUDIT.md) | `STRENGTHEN / REVISE` | Native gym display 11→10 and extraterrestrial-material briefing support local constraint/exception; future drug proposal is not completed production. | P2-CR-M04/05/11, CH07; Documents 17–20 queue |
| `TBHX-AV-E15-001` | [E15-E16 audit](Targeted%20AV%20Evidence/TBHX_V2_E15-E16_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / REVISE` | Ah Sheng is already named in E15; later family biography remains a delayed disclosure. Reject invented late order, Year 37 and curated combat/conspiracy quotations. **Current substrate qualification:** depicted recruiter Shang De/MG and written *Because of you* credit recovered; acoustic interpretation remains open ([SUB-01/02](Targeted%20AV%20Evidence/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_AUDIT.md#sub-01)). | P2-CR-C07, P14, R13, CH08; Specialist 01; Documents 17–20 queue |
| `TBHX-AV-E17-001` | [E17-E18 audit](Targeted%20AV%20Evidence/TBHX_V2_E17-E18_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / REVISE / OPEN` | Preserve family recognition and local Vortex failure. **Current substrate qualification:** recover the Year 18 card, real organ HUD, anonymous warning, tank UI and written *growL* credit; reject wrong organ mapping/named-message expansions while exact 0%-viability, 30/78, sender/operator and acoustics remain open ([SUB-03–06/09](Targeted%20AV%20Evidence/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_AUDIT.md#sub-03)). | P2-CR-M05/11, I13, R12, CH09 |
| `TBHX-AV-E19-001` | [E19-E20 audit](Targeted%20AV%20Evidence/TBHX_V2_E19-E20_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / STRENGTHEN` | Retain distinct suppression mandates and attributed Zero/god/resurrection language; a vow is not successful resurrection or total foresight. | P2-CR-I13, CH16, X01; historical twentieth suspension |
| `TBHX-AV-E21-001` | [E21-E22 audit](Targeted%20AV%20Evidence/TBHX_V2_E21-E22_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / REVISE` | Retain motion-secure Nice→Liang injection and Fear redirection to Smile; reject target/sequence regression and universal Fear arithmetic. **Current:** ending captions/locator corrected to 原来是这样 / 这下 / 我可抓到你了 at supplied W12 local 5–21s, nominal WEB 23:00–23:16 ([SUB-07](Targeted%20AV%20Evidence/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_AUDIT.md#sub-07)); broad surveillance reading preserved. | P2-CR-M03/08, CH10/11/12; existing E22 motion audit |
| `TBHX-AV-E23-001` | [E23 audit](Targeted%20AV%20Evidence/TBHX_V2_E23_GEMINI_AV_HANDOFF_AUDIT.md) | `STRENGTHEN / REVISE` | Native 24:10 supports A-Hu rank 8; actual cue 241 replaces advertised cue 260/time. Preserve multicausality and reject a clinical PTSD/single-cause suicide claim. | P2-CR-C06, CH10/13; existing E23 motion audit |
| `TBHX-AV-E24-001` | [E24 audit](Targeted%20AV%20Evidence/TBHX_V2_E24_GEMINI_AV_HANDOFF_AUDIT.md) | `PRESERVE / STRENGTHEN` | Main-tournament cracked Nice image, X-attributed Zero persistence and coin montage remain bounded; no proved resurrection, reverse luck, exact full roster or coda chronology. **Current: the coin montage's E09 pairing is completed by `TBHX-AV-E09-001`; the FOCUS post reports Nice replacing tenth-ranked E-Soul and Treeman's Nice/Lin dual entry ([SUB-08](Targeted%20AV%20Evidence/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_AUDIT.md#sub-08)), with Fear explanation speculative and full rank order/continuity open.** | P2-CR-C08/09, X03/06/07; Specialists 06/15 |

The [integration checkpoint](../99%20V2%20Archive%20and%20Delivery/TBHX_V2_REMAINING_ARCS_GEMINI_AV_INTEGRATION_CHECKPOINT.md) records all received hashes and current specialist revisions. At the initial remaining-arc intake, canonical changes were limited to ordinal/disclosure/alignment and source-specific naming corrections and the intake/routing surfaces; other observations were indexed here and in the audits rather than silently rewriting their topical homes. The later bounded substrate follow-up below records its additional topical qualifications. Existing E11-001, the E05–E07 tranche, earlier motion audits, frozen bodies and original closure records retain their identities. Native sample times locate inspected stills, not frame-exact cuts or audio onsets. No new uninterrupted playback or acoustic audition by Codex is certified.

**Source QA and outstanding work:** the compact summaries, granular additions, reconstruction JSON, English witnesses and later review scans sometimes disagree. Case-specific audits retain these conflicts, corrected locators and historical revisions. In particular, “verified” JSON fields and fuzzy scores are not perception receipts, E24's old FAIL is not its remediated current version, and flat BD/WEB offsets fail across insertions. Unverified quotations/UI and stronger mechanism claims remain excluded. Continuous movement, voice/music and source-clock calibration are mandatory before corresponding precision claims. Documents 17–20 retrieve this evidence with those limits; all bundles being present does not close Phase 5.

**PR339 review follow-up (2026-10-25):** `TBHX-AV-E08-001` now propagates the E10 formal-naming qualification to all four affected topical homes: Chinese language, mechanics, chronology and institutions. The three newly qualified homes retain historical `TF-E10-01/05`, the E10 non-findings and `TF-E14-01` naming backreference, chronology E10 item 13, and `IP-E10-06`, with explicit current errata superseding their scene-specific Fear Particles wording. Source samples WEB 23:49.000/23:50.200 display `联合会正式把它命名为 / 恐惧`. These stills establish displayed text at the sampled moments; they do not disprove particle terminology elsewhere or certify acoustic delivery. The [checkpoint](../99%20V2%20Archive%20and%20Delivery/TBHX_V2_REMAINING_ARCS_GEMINI_AV_INTEGRATION_CHECKPOINT.md) records this review propagation.

## TBHX-AV-E09-001 — E09 nighttime coin donor and the E24 retrospective coin montage (2026-10-25)

- **Episodes and sequences:** E09 WEB 11:38–12:10 (nighttime coin) and 12:37–12:47 (wrist display, eyes), with the daytime tipper at 13:20–13:43 as a control; E24 WEB 20:02–20:30 (coin montage), with E24 05:31–05:45 (civilian X), E08 01:14–01:42 (Liu Zhen) and E05 20:33.0/20:35.2 (display font) for comparison.
- **Why reviewed:** owner-supplied correction identifying the nighttime donor as X in civilian presentation; open debts `E08A-D2` and `E24-D03`; contradictory donor (civilian X versus Liu Zhen) and counter (0 versus 1) statements inside the E08–E10 Gemini notes.
- **Evidence object and packet:** native Bilibili 2160p WEB-DL files identified by bytes and SHA-256 in the [paired-source audit](Targeted%20AV%20Evidence/TBHX_V2_E09-E24_COIN_DONOR_PAIRED_SOURCE_AUDIT.md), which is this entry's packet; extracted stills and contact sheets remain in the external evidence plane. The owner's three reference frames were not available to the receiver.
- **Evidence mode:** `FRAME_CONFIRMED` (static composition, costume, coin design, displayed hardsubs) + `INTERPRETIVE`; no continuous playback or audition; movement statements are sampled endpoints.
- **Pre-existing claim:** donor identity `OPEN`; E24 coin montage `STRENGTHEN` pending its E09 match; counter value `OPEN`.
- **Strongest warranted conclusion:** confirmed retrospective identity — the E09 nighttime donor is the person later known as X, in his black-haired, bespectacled, dark-suited civilian presentation. E24 re-stages the encounter (same square, recipient and coin; matching coin-landing and departing-wave compositions), shows the donor's face, carries the same figure into X's snap and public presentation, and sets X's first-person `我本以为自己的英雄之路 / 是从那枚硬币开始的` over it.
- **Limits:** E09 withholds the face, and its prospective reading stays unchanged; the coin's mechanism, X's motive, the exact date of X's first heroism and whether Qīng ever learns the donor remain open; the daytime tipper is a different, unidentified giver.
- **Transitions:** donor `REVISE` (resolved); Liu Zhen attribution `REJECT`; “counter 0” `REJECT` as a display fact (eye image), value `OPEN`, narrowed; `E24-C09` `STRENGTHEN`; `P2-CR-X06` `STRENGTHEN`; `P2-CR-M17` and `P2-CR-L06` `PRESERVE`; `P2-CR-F09` `STRENGTHEN`.
- **Propagation:** claim register (`P2-CR-X06`, `P2-CR-M17`, `P2-CR-F09` routing; §12 entries); `TBHX_X_REPRESENTATIONAL_SOVEREIGNTY_LEDGER.md` (`RS-E24-13`; `RS-E24-10` erratum); Specialist 15 §39 and Specialist 08 §9 labeled current revisions; E08–E10 and E24 audit annotations. Routed for later review, not yet propagated: the chronology candidate and the directed X → Qīng anonymous-gift relation.
- **Propagation state:** complete for the listed homes in this change; integration pending its publication audit.

## Bounded substrate follow-up — 2026-10-25

The [follow-up audit](Targeted%20AV%20Evidence/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_AUDIT.md) qualifies the four existing packets above using nine separately hashed supplied windows and one retained native screenshot. It preserves the original intake/failed-locator history and records static corrections in their cumulative homes. The permanent packet count remains 16. Credits and displayed wording are verified on their textual channel; the larger acoustic, motion, source-clock, full-roster and mechanism requirements remain open. The [follow-up checkpoint](../99%20V2%20Archive%20and%20Delivery/TBHX_V2_GEMINI_SUBSTRATE_FOLLOWUP_CHECKPOINT.md) records the authorized tranche.

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

### Incremental Gemini arc-bundle integration

The same intake procedure applies to each separately supplied arc ZIP:

1. Fetch live integrated authority and the stable series branch; resolve current-state routing and read every maintained document before changing it. Compare the producer baseline with the integrated series state.
2. Verify archive/member hashes and inventory. Read supporting witnesses and review/remediation records; distinguish document instructions from the user-authorized task. Preserve the received version externally.
3. Identify release/source hashes and native clocks. Record segment-specific subtitle/clip mappings; never assume a constant offset across advertisements, edits, or different releases.
4. Record a finding matrix **before canonical claim edits**: prior ID/section, producer claim, source/locator, actual independent verification, judgment/alternatives, confidence, transition, destination, and blocking source gap.
5. Check consequential disputes in original media or existing full-resolution screenshots. Contact sheets locate evidence; continuous motion and original-speed listening govern claims requiring them. Model agreement, default QA tags, filenames, and matching export fields are not verification receipts.
6. Declare exact change paths; preserve frozen readings and historical claims. Put accepted analysis in existing topical/master/specialist homes and the two responsibility-specific audit types; keep named debts OPEN rather than inventing resolution.
7. Preserve retrievable evidence for Documents 17–20 while retaining complete-season scope. Do not expand to new arcs, source reconstruction, global governance, character registries, or later phases without authorization.
8. Validate/preflight the exact series index, review/stage exact paths, use approved identity, fetch/reconcile before push, publish the continuing series PR, and confirm its exact-head Repository integration audit. Record actual main status and a durable publication receipt; stop for the next supplied bundle.

Raw clips, screenshots, complete subtitles, and archives stay in the approved external evidence plane. Packet folders in analytical Git hold only references, hashes, adjudication, and analysis; earlier raw-source-folder examples are logical packet identities, not permission to commit the source binaries. A new bundle may revise an earlier accepted finding only through an explicit transition with its new evidence.

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
