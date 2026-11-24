---
title: "Psycho-Pass S1 New Edit — Evidence and local state"
artifact_id: PP_S01NE_EVIDENCE_AND_STATE_LEDGER
artifact_type: evidence_and_state_ledger
series: psycho-pass
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "PP-S01NE-E01 admitted and accepted"
canonical_home: series/psycho-pass/installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md
created: 2026-11-18
last_updated: 2026-11-23
---

# S1 New Edit — Evidence and local state

This is the current canonical source-observation and installment-state home for the intended eleven New Edit units. **Accepted records through `PP-S01NE-E01`: 26 anchored observations (`OBS-0001`–`0026`), 13 scene reconstructions (`SC-01`–`SC-13`), 14 local states (`STATE-0001`–`0014`).** The contract below governs all episode transactions.

## Identity and source-facing records

An observation uses `PP-S01NE-E##-OBS-####`; IDs never recycle or change with interpretation. Its mandatory payload is unit ID, exact witness ID and SHA-256 reference from the [source register](../../source-inventory/PP_SOURCE_REGISTER.md), source edition, clock convention, start/end locator, scene ID, observation type, inspectable description, inspector/date, actual modality and any sampling or access limit. Exact dialogue adds text-witness ID, cue/line locator, language, aligned audiovisual interval and whether original wording, subtitle transcription or analytical translation.

Observation types separate directly viewed action/image, directly heard performance/sound, inspected text, character/institution assertion and analyst inference. An inference links the observations from which it follows and its local claim ID; it does not overwrite the observed event. `REPORTED` AV locators are retrieval candidates until reinspected and `ANCHORED` under the [protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md). A timestamp precise to milliseconds does not establish perceptual timing accuracy.

Source coverage is recorded by meaningful scene/segment, including ordinary connective action, OP/ED, credits and post-credit material within the admitted source. List inspected versus missing intervals, continuity breaks, text route, audio route and visual route. Requirement (`REQUIRED`, `OPTIONAL`, `OUT_OF_SCOPE`) and inspection (`COMPLETE_FOR_DECLARED_SCOPE`, `PARTIAL`, `PENDING`, `UNAVAILABLE`, `NOT_APPLICABLE`) are independent. No checksum, extracted frame count or transcript cue count certifies perceptual completion.

Each scene reconstruction preserves presented order, relevant event-time constraint, persons and their information, action/choice, immediate consequence and changed state. It links the reading's narrative prose rather than replacing it. Unknown event dates and inferred offscreen actions remain marked.

## Local state and changes

A local state ID is `PP-S01NE-STATE-####` with versions tied to accepted unit boundaries. Record entity ID, state domain, entering state, source-supported change, resulting state, evidence and local claim IDs, counterevidence, uncertainty and review disposition. Preserve prior states and the transition mechanism. A later-looking summary without transition evidence is insufficient.

Character state separates goals, knowledge, affect, competencies/limits, public role, self-report and supported disposition. Directed relationship state carries subject → object, trust/dependence/obligation/authority/intimacy dimensions as supported, asymmetric information and the concrete exchange behind change. Institution state separates claimed norm, actual process, displayed measurement, enforcement, exception and affected person's consequence. These are installment-scoped records, never rival full biographies or automatically current franchise conclusions.

Known persons use a stable entity ID from the franchise state ledger, a proper name known at this boundary and any purposeful role/alias. If identity is not established, a local provisional ID is used and later linked without backfilling the earlier knowledge boundary. Do not replace recurring named subjects with generic role labels that make their actions hard to retrieve.

## Per-unit maintenance and dependencies

The principal proposes source and state updates with the completed reading. Independent specialists supply their actual source observations; the critical reviewer checks load-bearing source spans, significant omitted persons/scenes and disputed transitions. The integrator alone accepts shared changes. Every material state transition has a route into the [local claim/disclosure ledger](PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md).

At each accepted unit, identify potential franchise implications and existing portrait dependencies. A change that is merely new local detail stays local. A materially changed disposition, directed bond, institutional rule or contradiction becomes a numbered delta under the [reconciliation protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md). If master integration is batched, record the pending delta and the master's earlier boundary; never imply that the master already reflects it.

Corrections retain the original observation identity, describe corrected versus earlier content and link the claim revision. Changed source bytes create another witness. Frozen readings and independent logs remain intact; current ledger entries retain their lineage. The [franchise state ledger](../../franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) owns current reconciled conclusions and monograph qualification, not this document.

---

## Accepted Unit Records — `PP-S01NE-E01`

- **Reading & Checkpoint:** [`PP_S01NE_E01_DEEP_READING.md`](readings/PP_S01NE_E01_DEEP_READING.md) | [`PP_S01NE_E01_CHECKPOINT.md`](checkpoints/PP_S01NE_E01_CHECKPOINT.md)
- **Witness Basis:** `PP-S01NE-E01-AV01` (`1603b8b0...`, `00:00:00.000–00:45:53.194`), `PP-S01NE-E01-AUD-FLAC01` (`4005a1e3...`), `PP-S01NE-E01-TXT-BD01` (`e940679b...`, `0.000s` offset, `≤ ±0.4–0.5s`), `PP-S01NE-E01-BUNDLE-V1`. Coverage: `COMPLETE_FOR_DECLARED_SCOPE` across `SC-01`–`SC-13` (zero post-credit scene; `1.0 fps` video sampling compensated by 11 lossless MKV clips, 25+ 1080p `FRM` stills, and 50 ms `AM` checks).

### Anchored Key Observations (`PP-S01NE-E01-OBS-0001` – `OBS-0026`)

| Observation ID | Scene / Span (`HH:MM:SS`) | Modality & Status | Inspectable Source Description |
| --- | --- | --- | --- |
| `PP-S01NE-E01-OBS-0001` | `SC-01` (`00:00:00–00:01:13`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | White-haired prologue speaker (`Makishima Shōgo` in credits) delivers loneliness/network monologue in dim room and self-ironizes with `"何てね…"`; zero E01 main-timeline presence. |
| `PP-S01NE-E01-OBS-0002` | `SC-02` (`00:01:14–00:02:47`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | Integrated OP *abnormalize* establishing tonal/visual motif vocabulary without adding extra-narrative plot disclosures. |
| `PP-S01NE-E01-OBS-0003` | `SC-03` (`00:02:48–00:03:38`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | Flashforward tower standoff: Kōgami and Makishima confront each other (`"お前は狡噛慎也だ"`) near an unidentified prone figure (`00:03:17`), framed by Akane's retrospective VO (`"きっと彼らは…"`). |
| `PP-S01NE-E01-OBS-0004` | `SC-04` (`00:03:41–00:07:56`) | `CAV`+`AO`+`FRM`+`TXT` (`ANCHORED`) | Rainy first-night cordon: Akane arrives late, receives Ginoza's jacket (`00:06:02`) and blunt Enforcer briefing (`飼い主` / `猟犬`), meets Kōgami, Masaoka, Kagari, and Yayoi. |
| `PP-S01NE-E01-OBS-0005` | `SC-05` (`00:09:09–00:09:36`) | `CAV`+lossless MKV+1080p `FRM`+`TXT` (`ANCHORED`) | Akane's Dominator startup HUD displays `2092年4月1日生 20歳` (`00:09:20.0` `FRM`), `志向性音声` (sic), and uncaptioned overlapping voice prompts (`~00:09:28–00:09:36`); biometric lock verified. |
| `PP-S01NE-E01-OBS-0006` | `SC-05` (`00:09:37–00:11:45`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | Okura Nobuo (`2074.04.20 / age 39` HUD — 1-year prop arithmetic conflict with Akane's DOB) rants after street scan escalation (`29.3 → 126.3 → 193.6 → >300`), abducts Chika Shimazu, and consumes stimulants. |
| `PP-S01NE-E01-OBS-0007` | `SC-05` (`00:12:45–00:13:34`) | `CAV`+lossless MKV+1080p `FRM`+`TXT` (`ANCHORED`) | Akane scans Masaoka in the rain: Dominator reads `127.4` and unlocks Non-Lethal Paralyzer under `任意執行対象` (discretionary execution target), revealing Enforcers lack bodily immunity; Masaoka catches her gaze. |
| `PP-S01NE-E01-OBS-0008` | `SC-05` (`00:13:34–00:14:35`) | `CAV`+lossless MKV+50 ms `AM`+`TXT` (`ANCHORED`) | Block 3 pursuit & briefing (`TXT-BD01` calibrated `|error| ≤ ±0.4s`); Masaoka introduces Sibyl's `犯罪係数` logic while squad closes on KT Building. |
| `PP-S01NE-E01-OBS-0009` | `SC-06` (`00:14:35–00:15:35`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | KT Building entry: Kagari pleads urgently to preserve hostage life via Paralyzer (`00:14:48`), revealing protective empathy behind banter. |
| `PP-S01NE-E01-OBS-0010` | `SC-06` (`00:15:36–00:16:33`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | Okura traps and assaults Chika while fleeing through the derelict building; squad tracks movement across floors. |
| `PP-S01NE-E01-OBS-0011` | `SC-06` (`00:16:34–00:18:42`) | `CAV`+lossless MKV+1080p `FRM`+`TXT` (`ANCHORED`) | Stairwell & warehouse trap: Okura shows Chika a `STEELBLUE / 110` handheld scanner whose text politely advises drone therapy while he screams she will be tortured for life (`00:16:40`); in the warehouse Masaoka slides his biometric-locked Dominator (red LEDs) across the floor (`00:17:45`); Okura grabs it (`死ね！！ → 何だこりゃ！！`), enabling Kōgami's rear Lethal Eliminator shot (`00:18:13`). |
| `PP-S01NE-E01-OBS-0012` | `SC-07` (`00:19:10–00:19:50`) | `CAV`+lossless MKV+1080p `FRM`+`TXT` (`ANCHORED`) | Chika flees with fuel/lighter (`162.9` HUD `00:19:12`); Akane tackles **Masaoka** around the waist (`00:19:16`), revealing Masaoka's articulated metallic prosthetic left hand (`00:19:41`); Masaoka shouts `"そのためのパラライザーだろうが！…ドミネーターはシビュラの目だ"` while silent Kōgami descends the stairs after Chika. |
| `PP-S01NE-E01-OBS-0013` | `SC-07` (`00:20:30–00:21:33`) | `CAV`+lossless MKV+1080p `FRM`+50 ms `AM`+`TXT` (`ANCHORED`) | Chika's Crime Coefficient exceeds `300` (Lethal Eliminator unlocked); Kōgami's lips move silently (`00:20:59–00:21:02` verified unvoiced across `AO`/`AM`/`TXT`); Akane shoots Kōgami with Non-Lethal Paralyzer (`00:21:07`) to stop him from killing Chika. |
| `PP-S01NE-E01-OBS-0014` | `SC-07` (`00:21:34–00:22:35`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | Akane sits beside Chika with a trembling smile, coaxing Chika to extinguish and drop the lighter; Dominator downgrades to Paralyzer; right as Chika starts an answering smile (`00:22:13`), **Ginoza fires a Paralyzer blast from the overhead catwalk (`00:22:15`)** flanked by Yayoi and Kagari (dual-override structure). |
| `PP-S01NE-E01-OBS-0015` | `SC-08` (`00:22:56–00:24:50`) | `CAV`+lossless MKV+1080p `FRM`+`AO`+`TXT` (`ANCHORED`) | Midpoint utilitarian bridge (`bare hand` `00:22:57`); Kōgami's anesthetized flashback (`Isoflurane 2.3%` ECG `00:24:22`) shows past Ginoza and an unnamed smoking colleague (`00:23:50`), silver wrist clasp (`00:23:57`), `"abnormal"` death commentary (`00:24:00`), pale blood-spattered screaming face flash (`00:24:17`), and inverted eye-opening match cut (`00:24:24` vs. Akane `00:24:51`). |
| `PP-S01NE-E01-OBS-0016` | `SC-09` (`00:24:50–00:26:55`) | `CAV`+1080p `FRM`+`AO`+`TXT` (`ANCHORED`) | Akane's morning apartment (`11.05.Wed` alarm, Candy concierge AI, holographic wardrobe/décor, sleepless guilt despite clear `Powder Blue` Hue; `11/21 AM 9:15` TV-board prop artifact). |
| `PP-S01NE-E01-OBS-0017` | `SC-09` (`00:26:56–00:29:50`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | Rooftop café with Yuki Funahara (`C`-rank, recites Sibyl creed and undercuts it with `"なんちてね～"`) and Kaori Minase (`SE`, praises Akane as `"メンタル美人"` and invokes `"友人としての直感"`). |
| `PP-S01NE-E01-OBS-0018` | `SC-10` (`00:29:50–00:31:10`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | PSB arrival: Yayoi exits dimly lit Lab No. 2 adjusting her tie (`00:30:31`, ambiguous relation to Shion — strictly non-certified); Akane meets Shion Karanomori. |
| `PP-S01NE-E01-OBS-0019` | `SC-10` (`00:31:11–00:33:05`) | `CAV`+`AO`+`TXT` (`ANCHORED`) | Lab No. 2: Shion identifies herself as a Latent Criminal with a medical license (`00:31:30`), checks Akane's `Powder Blue` resilience, and softens teasing with genuine emotional tact (`00:32:32`). |
| `PP-S01NE-E01-OBS-0020` | `SC-10` (`00:33:06–00:34:46`) | `CAV`+1080p `FRM`+`AO`+`TXT` (`ANCHORED`) | CID office baseline: Form 71 (`10月4日 午後3時30分ころ / 晴れ` prop date artifact, `警察課` typo, `DXSETUP` filler text), desk props (Kagari game/toys, Yayoi guitar/tablet), bare hands (`00:33:08.5`), and street-scanner alert dispatch. |
| `PP-S01NE-E01-OBS-0021` | `SC-11` (`00:34:47–00:36:55`) | `CAV`+lossless MKV+1080p `FRM`+`AO`+`TXT` (`ANCHORED`) | Mall arrest: holographic Commissa-chan mascot (`Takamori Natsumi` voice modulator operated by Masaoka `00:36:09–00:36:42`) distracts and detains a juvenile Latent Criminal (`少年潜在犯`) protesting `"俺はまだ何も…"` (`00:36:44`); reused mirrored `126.3` scanner prop graphic. |
| `PP-S01NE-E01-OBS-0022` | `SC-11` (`00:36:56–00:37:55`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | Sunset waterfront talk: Masaoka explains hound-fatalism (`犯罪に関わる才能`), institutional division of labor, and his protective sidelining of Akane. |
| `PP-S01NE-E01-OBS-0023` | `SC-12` (`00:37:55–00:41:15`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | Cafeteria rupture: Kagari learns Akane was the sole `A` in CID out of 500+ (`00:39:22`), shifts from `朱ちゃん` to sharp `あんた`, contrasts Enforcers' `捕らわれの身` vs. `許可された社会活動`, and delivers uncorroborated age-5 Latent Criminal self-report (`00:40:37`). |
| `PP-S01NE-E01-OBS-0024` | `SC-12` (`00:41:16–00:43:45`) | `CAV`+lossless MKV+`AO`+`TXT` (`ANCHORED`) | Infirmary conversation: Kōgami separates `デカ` aspiration (`正義 > 役目`) from his personal obsessive `始末をつけなきゃならない役目` tied to an unnamed `"abnormal"` death, invoking Sibyl's `恩寵` / `ご託宣` / `成す` ("can implies ought") logic while thanking Akane for not letting him become a murderer. |
| `PP-S01NE-E01-OBS-0025` | `SC-13` (`00:43:45–00:44:35`) | `CAV`+lossless MKV+1080p `FRM`+50 ms `AM`+`TXT` (`ANCHORED`) | CID report: Akane calmly defends her Paralyzer shot before Ginoza (`一過性` `00:44:00`), citing Chika's recovered `56.3` / 7-day avg `58.7` (`退院も可能` `00:44:04`); Kagari visibly reacts (`00:44:05`); Kōgami backs Akane publicly using formal bureaucratic `"義務を果たした"` (`00:44:16`). |
| `PP-S01NE-E01-OBS-0026` | `SC-13` (`00:44:35–00:45:53`) | `CAV`+1080p `FRM`+`AO` (`ANCHORED`) | Ending credits (*Namae no Nai Kaibutsu*) with verified staff/cast billing (`Makishima Shōgo`, `Chika Shimazu`, `Nobuo Okura`, etc.) and confirmed zero post-credit scene. |

### Local Installment States (`PP-S01NE-STATE-0001` – `STATE-0014`)

- `PP-S01NE-STATE-0001` (`PP-ENT-0001` Akane Tsunemori): Entering unsure top graduate (`700` pts, solitary CID `A`, `2092.04.01 / age 20`) → Warehouse dual override & sleepless guilt despite `Powder Blue` → Closing composed clinical defense (`一過性`, `00:44:00`). (`OBS-0004`, `0005`, `0012–0014`, `0016`, `0017`, `0025`; `CLM-0001`, `0003`, `0012`).
- `PP-S01NE-STATE-0002` (`PP-ENT-0002` Shinya Kōgami): Detached tactical Enforcer → Paralyzed by Akane (`Isoflurane 2.3%` memory of unnamed `"abnormal"` death) → Split between `デカ` aspiration (`正義 > 役目`) and compulsive survival `役目` (`始末`), backing Akane publicly via `"義務を果たした"`. (`OBS-0003`, `0011–0013`, `0015`, `0024`, `0025`; `CLM-0004`, `0008`).
- `PP-S01NE-STATE-0003` (`PP-ENT-0003` Tomomi Masaoka): Veteran Enforcer (`127.4`, prosthetic left hand, biometric-lock decoy craft) combining gentle mentorship with fierce field enforcement (`シビュラの目`), internalized hound-fatalism (`犯罪に関わる才能`), and protective sidelining. (`OBS-0007`, `0011`, `0012`, `0021`, `0022`; `CLM-0006`).
- `PP-S01NE-STATE-0004` (`PP-ENT-0004` Shūsei Kagari): Playful desk-toy armor over captivity (`捕らわれの身`) → urgent hostage-rescue Paralyzer plea (`00:14:48`) → explosive cafeteria resentment over uncorroborated age-5 verdict (`朱ちゃん → あんた`) → startled silent reassessment (`00:44:05`). (`OBS-0009`, `0020`, `0023`, `0025`; `CLM-0005`).
- `PP-S01NE-STATE-0005` (`PP-ENT-0005` Nobuchika Ginoza): Rigid human/hound hierarchy (`貴様ら`/`飼い主`) and overhead catwalk Paralyzer override (`00:22:15`), balanced by pragmatic jacket toss (`00:06:02`), squad pairing, past flashback presence (`00:23:50`), and formal consultation of Kōgami (`00:44:12`). (`OBS-0004`, `0014`, `0015`, `0025`; `CLM-0011`, `0012`).
- `PP-S01NE-STATE-0006` (`PP-ENT-0006` Yayoi Kunizuka): Minimal-speech Enforcer (`Hound 2`, guitar hobby), silent practical solidarity (smacking Kagari, lending tablet, volunteering off-shift), ambiguous dim-lab exit (`00:30:31`). (`OBS-0014`, `0018`, `0020`).
- `PP-S01NE-STATE-0007` (`PP-ENT-0007` Shion Karanomori): Self-identified Latent Criminal medical analyst; flamboyant teasing over high emotional tact (`00:32:32`). (`OBS-0018`, `0019`).
- `PP-S01NE-STATE-0008` (`PP-ENT-0008` Shōgo Makishima — E01-bounded): Flashforward-only self-ironizing observer (`何てね…`), symmetrical future adversary to Kōgami; zero E01 proof of wider plot role. (`OBS-0001`, `0003`; `CLM-0008`).
- `PP-S01NE-STATE-0009` (`PP-ENT-0009` Nobuo Okura): `29.3 → 126.3 → 193.6 → >300` breakdown + stimulant-fueled predatory abduction → dead at scene via Lethal Eliminator (`00:18:15`). (`OBS-0006`, `0010`, `0011`).
- `PP-S01NE-STATE-0010` (`PP-ENT-0010` Chika Shimazu): Abducted victim (`110 Steelblue → 162.9 → >300 → Paralyzer → 56.3 / 58.7`), recovering with discharge feasible (`退院も可能`). (`OBS-0011–0014`, `0025`).
- `PP-S01NE-STATE-0011` (`PP-ENT-0011` Yuki Funahara & `PP-ENT-0012` Kaori Minase): Naturalized Sibyl aptitude cohort (`C`-rank / `SE`) preserving personal non-metric trust (`友人としての直感`) and irreverence (`なんちてね～`). (`OBS-0017`; `CLM-0009`).
- `PP-S01NE-STATE-0012` (`PP-ENT-0013` Youth Latent Criminal / `少年潜在犯`): Preemptively detained in mall Commissa-chan op while protesting `"俺はまだ何も…"` (`00:36:44`). (`OBS-0021`; `CLM-0002`, `0007`).
- `PP-S01NE-STATE-0013` (Directed Relationships Matrix — E01): Akane↔Kōgami, Akane↔Masaoka, Akane↔Kagari, Akane↔Ginoza, Akane↔Yuki/Kaori, Kōgami↔Masaoka, Yayoi↔Shion (ambiguity preserved), Kōgami↔Makishima (flashforward).
- `PP-S01NE-STATE-0014` (`PP-ENT-0016`/`0017`/`0018` Sibyl / PSB CID / Dominator): Adjudicated under `H3c` (unresolved ambivalence — real-time biometric/downgrade/therapy capability coexisting with near-fatal transient misclassification, pre-crime juvenile detention, staffing strain, and Enforcer captivity). (`CLM-0001`, `0002`, `0007`, `0011`, `0012`).
