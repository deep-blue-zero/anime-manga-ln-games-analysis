---
series: LYCORIS_RECOIL
artifact_type: ledger
scope: "V2 cumulative anime-native character state and microbehavior; later supplementary evidence added only with source-class provenance"
generation: V2
status: canonical
source_boundary: "SHORT01; A1 anime-native evidence through TV E01-E13 + Friends Short 01 only"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
mutable: true
current_sequential_boundary: SHORT01
e01_acoustic_performance_backfill: complete
e02_acoustic_performance_pass: complete
e03_acoustic_performance_pass: complete
e04_acoustic_performance_pass: complete
e05_acoustic_performance_pass: complete
e06_acoustic_performance_pass: complete
e07_acoustic_performance_pass: complete
e08_acoustic_performance_pass: complete
e09_acoustic_performance_pass: complete
e10_acoustic_performance_pass: complete
e11_acoustic_performance_pass: complete
e12_acoustic_performance_pass: complete
e13_acoustic_performance_pass: complete
short01_acoustic_performance_pass: complete
perceptual_voice_audition_state: unverified
---

# Lycoris Recoil Character State and Microbehavior Ledger

## 1. Responsibility

This is the canonical cumulative home for V2 character-state snapshots and atomic behavioral observations that support reusable reconstruction.

It is **not** a substitute for episode deep readings or character monographs.

Source-unit readings answer:

> What happened and what did it mean here?

This ledger answers:

> What character-state and behavioral evidence has accumulated across the sequence?

---

# 2. Current boundary

`SHORT01`

The ledger is now prospectively bounded through TV E01-E13 plus Friends Short 01. No Short 02-06 or supplementary narrative evidence is admitted. V1 conclusions remain revision/comparison input only, not observational evidence.

---

# 3. Character registry

| ID | Character | V2 reconstruction tier at initialization | Current V2 state |
|---|---|---|---|
| CHI | Nishikigi Chisato | Full target | `SHORT01_CONTEXTUAL_ROLE_CORRECTION_EXTENDED` |
| TAK | Inoue Takina | Full target | `SHORT01_CIVILIAN_OPTIMIZATION_EXTENDED` |
| FUK | Harukawa Fuki | Strong bounded target | `E12_INDEPENDENT_JUDGMENT_EXTENDED` |
| ERI | Janome Erika | Domain-limited unless evidence expands | `E12_ROLE_REPAIR_EXTENDED` |
| KUR | Kurumi | Strong bounded target | `SHORT01_SOCIAL_MEMBERSHIP_EXTENDED` |
| MIK | Mika | Strong bounded target | `SHORT01_CAFE_CAREGIVER_EXTENDED` |
| MIZ | Nakahara Mizuki | Strong bounded target | `SHORT01_ORDINARY_SOCIAL_EXTENDED` |
| KUS | Kusunoki | Domain-limited unless evidence expands | `E12_SELECTIVE_SUBVERSION_EXTENDED` |
| SAK | Otome Sakura | Domain-limited unless evidence expands | `E07_BOUNDED_EXTENDED` |
| MAJ | Majima | Adversarial/ideological target; mundane scope unknown | `E12_CLIFFHANGER_REENTRY_EXTENDED` |
| YOS | Shinji Yoshimatsu | Relationship/ideological target; general scope unknown | `E12_SELF_SACRIFICIAL_TELEOLOGY_EXTENDED` |
| HIG | Himegama | Domain-limited Alan/proxy target | `E09_PROXY_BODILY_COERCION_EXTENDED` |

Tier labels are analytical workload expectations, not personality claims.

---

# 4. Atomic observation schema

Each diagnostic record should preserve as many of the following as the source supports:

| Field | Meaning |
|---|---|
| Observation ID | Stable ID, e.g. `CHI-MB-E01-001` |
| Scope | Episode/short/prose source |
| Locator | Timestamp/page/spine route |
| Character | Stable character ID |
| Interlocutor | Named person/group |
| Setting/role | Café, assignment, DA, domestic, leisure, etc. |
| Relationship state | Current relationship phase |
| Stakes | Trivial/low/moderate/high/existential |
| Character state | Affect/operational state |
| Trigger | What prompted response |
| Initiator | Who began interaction/action |
| Appraisal | Fact/strong inference about perceived situation |
| Immediate goal | What character appears to want now |
| Behavior/tactic | Observable response |
| Speech/register | Textual form |
| Performance — acoustic | Measurable pitch/range/intensity/timing/pause/activation/nonverbal-event evidence; preserve extraction/signal limits |
| Performance — perceptual | Subjective heard delivery (e.g. deadpan, warm, wry, breathy, controlled irritation); use `UNVERIFIED` when trustworthy audition is unavailable |
| Body behavior | Gesture/proximity/action |
| Partner response | Immediate response |
| Recalibration | Persist/soften/escalate/reframe/withdraw/etc. |
| Outcome | Local result |
| Candidate policy | Policy ID or `NONE` |
| Negative evidence | Opportunity-sensitive non-action if any |
| Epistemic state | FACT / STRONG_INFERENCE / etc. |
| Source class | A1/A2/B1/etc. |
| Confidence | HIGH/MODERATE/LOW/OPEN |

Performance fields obey a strict non-entailment rule:

`ACOUSTIC-PERFORMANCE EVIDENCE != PERCEPTUAL PERFORMED-VOICE EVIDENCE`

A wider pitch range, greater intensity, shorter onset, or higher acoustic activation may establish a measurable state difference. It does not by itself establish labels such as `warm`, `mocking`, `deadpan`, `sarcastic`, `tender`, or `smiling through the line`. When direct perceptual audition is unavailable, preserve the acoustic observation and set the perceptual field to `UNVERIFIED` rather than filling the gap by inference.

Within-character comparisons are preferred to raw cross-character F0 comparisons because speakers differ physiologically and extraction windows can contain score/background contamination.

---

# 5. Observation register

| Observation ID | Scope | Character | Trigger / condition | Behavior | Candidate policy | Confidence |
|---|---|---|---|---|---|---|
| `CHI-MB-E01-001` | E01 00:48-01:33 | CHI | voices received Lycoris public-order doctrine | reproduces doctrine fluently but closes with distancing `なんだってさ`; FLAC confirms the appended phrase is acoustically set off but does not identify a specific subjective attitude | `CHI-INST-DIST-01` pending repetition | HIGH |
| `TAK-MB-E01-001` | E01 02:39-03:21 | TAK | Erika faces imminent execution while unit is ordered to wait | overrides command and uses overwhelming fire; defends action by survival outcome | `TAK-OPS-RISK-01` | HIGH |
| `FUK-MB-E01-001` | E01 02:39-03:21 | FUK | subordinate imposes severe risk on Erika | tries to obey standby, then condemns Takina and strikes her afterward | `FUK-CMD-CARE-01` pending repetition | MODERATE |
| `CHI-MB-E01-002` | E01 06:05-07:01 | CHI | first meeting with assigned partner | first-name use, honorific removal, age comparison, injury noticing, rapid shared-role incorporation; greeting is acoustically expansive relative to Takina's formal response | `CHI-SOC-INIT-01` | HIGH |
| `TAK-MB-E01-002` | E01 06:05-07:01 | TAK | first meeting/new workplace | maintains polite/formal self-presentation; defines assignment through learning and DA return; selected FLAC extraction is markedly more acoustically constrained than Chisato's greeting | `TAK-SOC-FORM-01`; `TAK-INST-01` | HIGH |
| `CHI-MB-E01-003` | E01 09:21-12:33 | CHI | heterogeneous neighborhood tasks seem unrelated to Takina | supplies person-specific rule `困ってる人を助ける仕事だよ`; asks Takina to help | `CHI-HLP-LOCAL-01` | HIGH |
| `CHI-MB-E01-004` | E01 ~10:30 | CHI | Takina interprets gang-office coffee as possible contraband | teases, confirms joke, restores ordinary-customer frame | `CHI-PLAY-01` | MODERATE-HIGH |
| `TAK-MB-E01-003` | E01 11:52-12:13 | TAK | Chisato says she likes the tower's `意味不明` quality | turns Chisato's wording back on her as concise teasing; selected extraction remains narrow (~174-223 Hz central F0) while Chisato's answer expands and includes explicit laughter | `TAK-TEASE-EMERG-01` | MODERATE-HIGH |
| `CHI-MB-E01-005` | E01 13:31-14:46 | CHI | Takina describes transfer injustice and rationality of disobedience | lowers blame threat, asks motive, validates teammate rescue, offers help returning to DA; support response occupies broader selected acoustic range than Takina's constrained rational account | `CHI-CONFRONT-01`; `CHI-SUPPORT-01` | HIGH |
| `TAK-MB-E01-004` | E01 13:31-14:46 | TAK | asked why she violated order | explains decision as `最も合理的`; seeks meaning/status of what she did; selected rational-defense extraction remains acoustically constrained (~182-257 Hz central F0) | `TAK-OPS-RISK-01`; `TAK-INST-01` | HIGH |
| `CHI-MB-E01-006` | E01 15:13-16:11 | CHI | minor stalking complaint contains anomalous photo | notices evidentiary anomaly, collaborates on gun-transfer inference, stays with frightened civilian | `CHI-HLP-LOCAL-01` | HIGH |
| `TAK-MB-E01-005` | E01 16:31-18:47 | TAK | detects tail while protecting Saori | uses Saori as bait; justifies by attacker intent and own precision; says `そんなミスはしませんよ` | `TAK-OPS-RISK-01` | HIGH |
| `CHI-MB-E01-007` | E01 18:47-20:05 | CHI | hostile armed adversaries / wounded enemy | uses nonlethal force, then treats wounded adversary; explicitly includes enemies in `命 大事に` | `CHI-LIFE-01` | HIGH |
| `TAK-MB-E01-006` | E01 ~20:00 | TAK | observes Chisato treating enemy | explicitly asks whether `命 大事に` includes enemies | `TAK-CLARIFY-01` | HIGH |
| `CHI-MB-E01-008` | E01 21:50-21:59 | CHI | captured attackers require disposition | uses Cleaner because she expects DA handoff to result in death | `CHI-LIFE-01` | HIGH |
| `CHI-MB-E01-009` | E01 22:00-22:43 | CHI | Takina joins café work / uniform | praises appearance, gathers group into photo, posts to café SNS, shares greeting | `CHI-SOC-INIT-01` | MODERATE-HIGH |
| `TAK-MB-E01-007` | E01 22:00-22:43 | TAK | gun recovery reframed as route to DA return | commits `やります！` with materially increased acoustic activation (~358 Hz estimated median F0 in selected extraction) relative to earlier controlled samples; participates in uniform/photo/service | `TAK-INST-01` | HIGH |
| `KUS-MB-E01-001` | E01 08:42-09:10 | KUS | Radiata breach must remain secret | orders Walnut killed; permits Takina's real misconduct to carry official failure narrative | `KUS-SEC-01` pending repetition | HIGH |
| `YOS-MB-E01-001` | E01 20:26-21:21 | YOS | Walnut challenges Alan's hidden involvement | confirms DA hack commission; states ignorance makes people happier | `YOS-IGN-01` pending repetition | HIGH |

| `CHI-MB-E02-001` | E02 03:11-03:19 | CHI | oversleeps/snoring immediately before urgent departure | wakes in highly activated rush and recovers into mission participation | `NONE` | MODERATE-HIGH |
| `TAK-MB-E02-001` | E02 05:15-06:25 | TAK | travel/extraction route under tight transfer timing | briefs route, catches Chisato not listening, chooses jelly around <10-minute transfer window | `TAK-SOC-FORM-01` | HIGH |
| `CHI-MB-E02-002` | E02 05:55-06:11 | CHI | Takina initially refuses shared train food | persists by converting offer into direct `あ～ん` invitation; boundary-forward but leaves final bodily acceptance to Takina | `CHI-SOC-INIT-01`; `CHI-PLAY-01` | HIGH |
| `TAK-MB-E02-002` | E02 06:03-06:11 | TAK | Chisato directly offers bite after initial refusal | voluntarily accepts `あ～ん`, says `おいしいです`; acoustic delivery remains controlled rather than Chisato-like | `NONE` / social-permission observation | HIGH |
| `CHI-MB-E02-003` | E02 11:13-11:29 | CHI | precision shot is required during hacked-car escape | says she lacks confidence and delegates target to Takina, who executes it | `CHI-CALIBRATE-01` | HIGH |
| `CHI-MB-E02-004` | E02 14:37-15:43 | CHI | wounded current enemy may die while extraction pressure is active | remains behind to give first aid, asks about family/dinner, accepts visible coordination cost; later formulates enemyhood as temporary | `CHI-LIFE-01` | HIGH |
| `TAK-MB-E02-003` | E02 14:37-15:05; 19:41-20:15 | TAK | Chisato stops active extraction to treat attacker | urges withdrawal before encirclement; later argues explicitly from team coordination, mission consequence, and licensed role | `TAK-MISSION-COORD-01` | HIGH |
| `TAK-MB-E02-004` | E02 16:29-17:39 | TAK | protected client appears killed | immediately reports mission failure and later apologizes; acoustic envelope contracts relative to prior escape urgency | `TAK-FAIL-ACCOUNT-01` | HIGH |
| `CHI-MB-E02-005` | E02 17:37-19:14 | CHI | Takina apologizes, then fake-death plan is revealed | immediately rejects Takina blame; after confirming nobody died shows strong visual/acoustic activation around survival relief | `CHI-CONFRONT-01`; `CHI-LIFE-01` | HIGH |
| `CHI-MB-E02-006` | E02 22:13-22:36 | CHI | Walnut identity is retired and Kurumi will remain locally | interrupts operational alias, asks for real name, accepts `クルミ`, invites her into shared dango with Takina | `CHI-SOC-INIT-01` | HIGH |
| `KUR-MB-E02-001` | E02 17:40-22:36 | KUR | fake-death plan succeeds / café offers new local role | reveals self behind Walnut, accepts `クルミ` as local name and reciprocal greeting with Chisato | `NONE` | HIGH |
| `YOS-MB-E02-001` | E02 opening/late café | YOS | Robota performs assigned clandestine work / Walnut elimination discussed | praises tool-like usefulness (`道具らしくてね`) and frames elimination as cleanup (`掃除`) | `YOS-INST-01` pending repetition | HIGH |

| `TAK-MB-E03-001` | E03 03:16-04:50 | TAK | off-hours cafe game is offered while DA return remains unresolved | declines leisure, then asks whether participating would help her return to DA; immediately seeks DA visit when Kusunoki becomes available | `TAK-INST-01` | HIGH |
| `CHI-MB-E03-001` | E03 03:16-04:50 | CHI | Takina declines ordinary group activity and remains DA-focused | repeatedly invites concrete participation without framing refusal as betrayal; later facilitates DA visit | `CHI-SOC-INIT-01`; `CHI-PLAY-01`; `CHI-SUPPORT-01` | HIGH |
| `FUK-MB-E03-001` | E03 07:47-08:16; 12:11-12:18 | FUK | Chisato questions DA obligation / Takina seeks return | frames DA as parent that rescued and raised orphans; later tells Takina she is no longer needed | `NONE` / institutional-belonging evidence | HIGH |
| `CHI-MB-E03-002` | E03 08:37-10:07 | CHI | Kusunoki's Takina account conflicts with rescue motive and abnormal comms failure | advocates Takina's return, challenges blame narrative, infers Radiata compromise from system behavior, presses commander directly | `CHI-SUPPORT-01`; `CHI-INST-CHALLENGE-01` | HIGH |
| `TAK-MB-E03-002` | E03 10:41-12:18 | TAK | DA access becomes actionable but successor already occupies her role | formally argues achievement/photo recovery as basis for reinstatement; shock/rejection intensifies when told her seat is gone and she is not needed | `TAK-INST-01` | HIGH |
| `TAK-MB-E03-003` | E03 13:21-14:15 | TAK | explains DA dorm/identity meaning after institutional rejection | states DA place was taken, fractures syntax, then assigns responsibility inward with `全部 自分のせい`; acoustic profile contracts markedly on self-blame | `TAK-FAIL-ACCOUNT-01` | HIGH |
| `CHI-MB-E03-003` | E03 14:45-15:52 | CHI | Takina exposes severe identity/belonging distress | validates her autonomous rescue choice, says she is glad they met, initiates strong embrace, offers cafe life as a trial while preserving later DA return and final self-choice | `CHI-VULN-AFFIRM-01`; `CHI-SUPPORT-01` | HIGH |
| `ERI-MB-E03-001` | E03 16:17-16:42; 21:31-21:45 | ERI | peers reduce Takina to dangerous rumor / direct repair feels difficult | explicitly says Takina is not at fault for Erika's capture and defends rescue motive, but remains unsure how to speak to Takina directly | `NONE` | HIGH |
| `TAK-MB-E03-004` | E03 20:39-20:49 | TAK | re-enters bounded mock battle against former partner | passes up easy rear shot, rushes Fuki and punches her, then says `これで おあいこですね`; symbolic reciprocity outranks scoring efficiency | `TAK-RECIP-CLOSURE-01` | HIGH |
| `TAK-MB-E03-005` | E03 21:54-22:09 | TAK | tactical opening can be created by firing through Chisato's line | does so and later justifies it with `きっと よけると思いましたから`; uses partner competence as implicit risk authorization | `TAK-OPS-RISK-01` | HIGH |
| `TAK-MB-E03-006` | E03 22:22-22:40 | TAK | after DA rejection and mock-battle closure, off-hours cafe gathering is still available | receives Chisato's `どうする～？`; next visual state places her voluntarily at the group game she refused earlier | `TAK-ORD-TRY-01` | HIGH |
| `KUR-MB-E03-001` | E03 03:16-04:04; 22:22-22:40 | KUR | post-Walnut cafe routine | participates as information-capable local member and ordinary board-game participant; asks whether Chisato is coming at episode end | `NONE` | HIGH |

## 5.1 E01 acoustic-performance backfill register

These records add an evidence modality already contained in E01; they do not advance the prospective narrative horizon.

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E01-AUD-001` | opening `なんだってさ` | short appended phrase is acoustically set off from preceding doctrine | strengthens segmentation/linguistic distancing; does not specify attitude | `UNVERIFIED` for sarcasm/wryness/mockery |
| `E01-AUD-002` | first café introduction | Chisato extraction is substantially more expansive (~499 Hz estimated median F0; ~-20.4 dBFS full-mix RMS) than Takina's constrained response (~289 Hz; ~-26.1 dBFS) | strengthens cross-channel social-initiation asymmetry | subjective warmth/coldness `UNVERIFIED` |
| `E01-AUD-003` | old-tower tease | Takina central F0 remains narrow (~174-223 Hz); Chisato response expands and contains explicit laugh | strengthens concise semantic-teasing observation and differentiated play styles | `deadpan` remains `UNVERIFIED` |
| `E01-AUD-004` | rational-defense -> support exchange | Takina rational account is constrained (~182-257 Hz central F0); Chisato support response spans broader selected range (~240-567 Hz) | specifies different performance envelopes for rational accounting vs interpersonal support | `tender/warm` remains `UNVERIFIED` |
| `E01-AUD-005` | closing `やります！` | estimated median F0 ~358 Hz, materially above several earlier controlled Takina samples in low-to-mid 200s | establishes state-conditioned activation; rejects invariant-flatness reconstruction | relational meaning beyond DA-return motive remains open |

## 5.2 E02 acoustic-performance register

These Layer-B records are derived from the canonical E02 FLAC. Full-mix pitch/RMS estimates are approximate; key contrasts were cross-checked with an independent pitch tracker. Layer-C affect labels remain `UNVERIFIED`.

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E02-AUD-001` | Chisato waking / field warning | wake panic ~419 Hz median F0; `たきな 出ないで！` substantially higher, with both trackers confirming high activation | rapid state-linked activation; ordinary disorganization does not imply field sluggishness | exact panic/protective texture `UNVERIFIED` |
| `E02-AUD-002` | Takina train ops / `あ～ん` / `おいしいです` | routine ops ~238 Hz; `あ～ん` ~151 Hz; `おいしいです` ~204 Hz/narrow | social participation expands while baseline vocal containment persists | shyness/warmth/deadpan `UNVERIFIED` |
| `E02-AUD-003` | play/correction cluster | Chisato `たきな様` ~408 Hz; Takina driving assertion ~274 Hz; movie/hacker correction ~211-222 Hz | differentiated low-stakes performance styles persist | subjective play tone `UNVERIFIED` |
| `E02-AUD-004` | Chisato task delegation | ~270 Hz median; more constrained than panic/urgent-relief states | supports straightforward competence calibration | admiration/bravado `UNVERIFIED` |
| `E02-AUD-005` | extraction conflict | Takina escape warning ~394 Hz vs routine ops ~238; Chisato `死んじゃうでしょ` ~509 Hz | both ethical/operational positions carry high urgency | exact affect `UNVERIFIED` |
| `E02-AUD-006` | Takina failure/apology | failure report ~225 Hz with narrow central span; apology ~214 Hz | state-conditioned contraction after perceived failure | guilt texture `UNVERIFIED` |
| `E02-AUD-007` | Chisato no-death confirmation/relief | confirmation ~512 Hz; following relief broad/high activation | survival is affectively load-bearing, not merely slogan | exact relief texture `UNVERIFIED` |
| `E02-AUD-008` | ethical dispute | mixed/tracker-sensitive contours; no robust monotonic escalation story | negative evidence against simplistic acoustic moral framing | all subjective dispute labels `UNVERIFIED` |
| `E02-AUD-009` | Kurumi naming / dango | Chisato naming ~341 Hz; dango invitation ~414 Hz; Kurumi name/greeting ~208-233 Hz | Chisato's invitation is acoustically activated while Kurumi remains comparatively contained | warmth/comfort `UNVERIFIED` |

## 5.3 E03 acoustic-performance register

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E03-AUD-001` | Takina `そうすればＤＡに戻れますか` | RMS ~-31.9 dBFS; median F0 ~245 Hz; 10-90 span ~85 Hz | controlled/instrumental DA-return baseline | exact affect `UNVERIFIED` |
| `E03-AUD-002` | Takina formal achievement/return appeal | RMS ~-27.9 dBFS; median F0 ~293 Hz; span ~247 Hz | activation increases under institutional stakes without abandoning formal framing | exact affect `UNVERIFIED` |
| `E03-AUD-003` | Takina `全部 自分のせい` | RMS ~-38.5 dBFS; median F0 ~197 Hz; span ~137 Hz | marked contraction under inward failure accounting | guilt texture `UNVERIFIED` |
| `E03-AUD-004` | Takina injustice / `なら どうすれば` | RMS ~-26.8 dBFS; median F0 ~354 Hz; span ~276 Hz | sharp activation when institutional cover-up/blocked agency becomes salient | anger/anguish label `UNVERIFIED` |
| `E03-AUD-005` | Chisato validates Takina's autonomous choice | RMS ~-31.3 dBFS; median F0 ~270 Hz; span ~244 Hz | support is prosodically active rather than acoustically neutral | warmth/tenderness `UNVERIFIED` |
| `E03-AUD-006` | Chisato offers cafe trial while retaining DA option | RMS ~-29.0 dBFS; median F0 ~284 Hz; span ~287 Hz | agency-restoring support carries broad Layer-B movement | exact affect `UNVERIFIED` |
| `E03-AUD-007` | Takina mock-battle entry | RMS ~-18.5 dBFS; median F0 ~367 Hz; span ~421 Hz | extremely high activation relative to routine speech; rejects invariant-flatness rule | exact battle affect `UNVERIFIED` |
| `E03-AUD-008` | Takina `これで おあいこですね` | RMS ~-32.0 dBFS; median F0 ~246 Hz; span ~75 Hz | returns to constrained delivery immediately after expressive action | perceptual dryness/satisfaction `UNVERIFIED` |

| `CHI-MB-E04-001` | E04 00:26-01:05 | CHI | Takina rejects Chisato's inaccurate nonlethal rounds as insufficient self-protection | preserves Takina's precision and proposes avoiding vital points rather than demanding use of Chisato's equipment; reframes existing skill toward a different moral purpose | `CHI-LIFE-01`; `CHI-CALIBRATE-01` | HIGH |
| `TAK-MB-E04-001` | E04 00:26-01:05 | TAK | shooting purpose is challenged | defines precision through former institutional function `急所を撃つのが仕事`; selected Layer-B windows remain controlled/moderately activated | `TAK-INST-01` | HIGH |
| `TAK-MB-E04-002` | E04 04:31-08:15 | TAK | clothing/underwear choice lacks an explicit rule | searches for `指定`, prioritizes work suitability, delegates skirt choice to Chisato, then directly requests comparative evidence rather than merely copying a norm | `TAK-PREF-GEN-01`; `TAK-CLARIFY-01` | HIGH |
| `TAK-MB-E04-003` | E04 09:08 | TAK | ordinary dessert discussion | states `私 あの かりんとう 好きです` without operational justification; delivery remains acoustically controlled (`E04-AUD-007`) | `TAK-PREF-GEN-01` | HIGH |
| `CHI-MB-E04-002` | E04 09:24-09:37 | CHI | Takina frames dessert through calorie/fitness cost | argues that lifetime meals are finite and that enjoyable eating can justify bounded compensatory cost | `CHI-TIME-01` | HIGH |
| `TAK-MB-E04-004` | E04 11:51-12:00 | TAK | Chisato behaves conspicuously at aquarium | invokes continuous Lycoris identity (`私たちリコリスですよ`); acoustic range broadens materially around the role assertion | `TAK-INST-01` | HIGH |
| `CHI-MB-E04-003` | E04 11:58 and 18:42-18:50 | CHI | off-duty partner treats Lycoris capability as continuously active | states that out of uniform they are not currently Lycoris, physically intercepts Takina's move toward the station emergency, and defers to civilian legal/context constraints | `CHI-ROLE-BOUND-01` | HIGH |
| `TAK-MB-E04-005` | E04 12:20-14:53 | TAK | Chisato's nonlethality/DA departure remain unexplained | initiates sustained personal questioning, persists through teasing deflection, and later gives direct person-specific positive evaluation | `TAK-PERS-INQ-01` | HIGH |
| `CHI-MB-E04-004` | E04 12:32-12:50 | CHI | Takina asks why she does not kill | says taking another person's time feels bad, then explicitly preserves painful nonlethal punishment; Layer-B expands strongly in the punitive continuation | `CHI-TIME-01`; `CHI-LIFE-01` | HIGH |
| `CHI-MB-E04-005` | E04 13:29-14:30 | CHI | Takina asks why Chisato left DA if nonlethality was possible there | discloses ten-year search for an important Alan benefactor and desire to say thanks; full-mix activation drops relative to punitive discussion | `CHI-SELF-AUTH-01` | HIGH |
| `YOS-MB-E04-001` | E04 15:28-16:02 | YOS | Mika challenges Yoshimatsu's continued proximity to Chisato | invokes Alan noninvolvement rule, checks Mika's promise, then says gifted talent must be delivered and names Chisato's killing genius | `YOS-TALENT-TELOS-01` | HIGH |
| `MAJ-MB-E04-001` | E04 16:35-18:20 | MAJ | encounters sanitized public order / hidden Lycoris counterforce | diagnoses society as a healthy-looking unhealthy lie, invokes balance, and uses organized lethal violence to expose/counter hidden power | `MAJ-BALANCE-01` | HIGH |
| `MAJ-MB-E04-002` | E04 23:21-23:55 | MAJ | sees subway violence reframed publicly as accident and learns Lycoris are information-controlled | concludes future disruption must be too large to conceal; converts successful information control into escalation criterion | `MAJ-BALANCE-01` | HIGH |
| `KUR-MB-E04-001` | E04 cafe/intercut | KUR | missing-gun inquiry coexists with group routine | investigates absence of guns from black market while also gaming/bathing/participating as ordinary cafe member | `NONE` | HIGH |
| `TAK-MB-E04-006` | E04 ending | TAK | Chisato is caught in underwear-disposal embarrassment | explicit laughter reaches markedly higher Layer-B activation (`E04-AUD-013`: ~-21.2 dBFS, ~496 Hz median F0 in selected full-mix window) than controlled baseline | `TAK-TEASE-EMERG-01`; state-conditioned-bandwidth evidence | HIGH |


## 5.4 E04 acoustic-performance register

The E04 claim/locator layer already carried `E04-AUD-001`–`013`; this compact register restores the cumulative ledger's episode-by-episode acoustic continuity without changing any E04 interpretation.

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E04-AUD-001/002` | Takina shooting critique / former vital-point job | selected medians ~201 / 263 Hz; controlled-to-moderate activation | operational precision remains a controlled baseline while role-purpose is challenged | Layer C `UNVERIFIED` |
| `E04-AUD-003/004` | civilian specification / skirt delegation | ~264 / 217 Hz selected medians | ordinary-choice uncertainty/delegation does not require Chisato-like expansion | Layer C `UNVERIFIED` |
| `E04-AUD-005/006` | preference uncertainty -> direct underwear verification | ~199 Hz constrained preference line vs ~259 Hz/broader direct request | evidence-seeking can raise activation inside the same Takina baseline | Layer C `UNVERIFIED` |
| `E04-AUD-007` | karinto preference | ~-31.9 dBFS, ~247 Hz median in selected window | explicit self-authored liking can remain acoustically controlled | Layer C `UNVERIFIED` |
| `E04-AUD-008` | `私たちリコリスですよ` | ~-28.8 dBFS, ~223 Hz median with broad selected span | role assertion produces expansion without replacing baseline | Layer C `UNVERIFIED` |
| `E04-AUD-009/010` | Chisato taking another's time / punitive nonlethal continuation | ~242 Hz then ~331 Hz median in selected windows | moral principle and forceful continuation occupy distinguishable Layer-B envelopes | Layer C `UNVERIFIED` |
| `E04-AUD-011/012` | Chisato important benefactor / gratitude-search close | selected medians ~233 / 224 Hz at lower intensity | personal disclosure can contract acoustically relative to playful/punitive states | Layer C `UNVERIFIED` |
| `E04-AUD-013` | Takina ending laughter | ~-21.2 dBFS, ~496 Hz median selected window | strong safe-frame activation; rejects globally flat voice model | Layer C `UNVERIFIED` |

## 5.5 E05 observations and acoustic-performance register

| Observation ID | Scope | Character | Trigger / condition | Behavior | Candidate policy | Confidence |
|---|---|---|---|---|---|---|
| `CHI-MB-E05-001` | E05 04:21-04:40 | CHI | terminal client describes being sustained by machinery | discloses complete artificial heart as an ordinary fact and immediately returns to shared activity; Takina visibly learns the fact for the first time | `CHI-SELF-AUTH-01` / biographical boundary | HIGH |
| `KUR-MB-E05-001` | E05 briefing + surveillance | KUR | ordinary group time overlaps technical mission work | plays while listening, then becomes central surveillance/intelligence node without a role-switch requiring withdrawal from ordinary participation | ordinary+utility recurrence | HIGH |
| `MIK-MB-E05-001` | E05 09:20-09:43 | MIK | Kurumi asks what mission Alan's life-gift assigns Chisato | acknowledges Alan mission claim but answers `それは千束が決めることだ` | self-authorship/parental permission evidence | HIGH |
| `TAK-MB-E05-001` | E05 10:50-11:06, 22:21-22:35 | TAK | Chisato's artificial heart creates a personal information gap | asks directly, attempts bodily verification, learns explicit public-context boundary, later reattempts only after stating privacy condition is satisfied | `TAK-PERS-INQ-01`; `TAK-BOUND-LEARN-01` | HIGH |
| `TAK-MB-E05-002` | E05 13:22-16:52 | TAK | veteran assassin threatens protected client | volunteers contact, identifies armor, draws threat away, warns Chisato, and directs client evacuation; urgent warning shows large Layer-B activation jump | `TAK-PROTECT-INIT-01` | HIGH |
| `CHI-MB-E05-002` | E05 16:22-19:09 | CHI | terminal client converts last-wish framing into revenge execution demand | first recommends evacuation, then forcefully incapacitates Jin but refuses killing even before revenge story is disproved | `CHI-TIME-01`; `CHI-LIFE-01` | HIGH |
| `CHI-MB-E05-003` | E05 18:41-19:09 | CHI | fake client invokes Alan life-gift as obligation to kill | rejects donor-purpose ownership; defines desired Lycoris work as helping and interprets giver as a model of aid | `CHI-SELF-AUTH-01`; `CHI-GIFT-RECIP-01` | HIGH |
| `YOS-MB-E05-001` | E05 20:58-21:05 | YOS | fake-client test has pressured Chisato toward assigned killing purpose | tour-monitor control apparatus is followed by Yoshimatsu instruction, Himegama response, and Alan emblem; Alan-side orchestration is strongly inferred, exact remote operator open | `YOS-PROXY-COERCE-01`; `YOS-TALENT-TELOS-01` | STRONG_INFERENCE |
| `MAJ-MB-E05-001` | E05 21:45 | MAJ | escalation after concealed subway attack | deliberately kills a Lycoris and names her category: `まずは１人目だ リコリス` | `MAJ-BALANCE-01` | HIGH |
| `TAK-MB-E05-003` | E05 21:58-22:10 | TAK | client identity/praise source is exposed as fabricated and Chisato globalizes the deception | preserves the narrower independently supportable proposition `いいガイドだったのは ウソじゃないと思います`; Chisato accepts with `ありがとう` | `TAK-EVID-PART-01` | HIGH |
| `CHI-MB-E05-004` | E05 21:58-22:10 | CHI | learns the interpersonal encounter was staged | voices disappointment (`ぜ～んぶ ウソか`) but accepts Takina's narrow evidentiary repair rather than generalizing to total distrust | `CHI-DECEPTION-AFFECT-01` | MODERATE-HIGH |

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E05-AUD-001` | Takina `この社長も気の毒ですね` | RMS ~-32.2 dBFS; median F0 ~254 Hz | low-activation early social-comment baseline | Layer C `UNVERIFIED` |
| `E05-AUD-002` | Chisato artificial-heart disclosure | RMS ~-25.9 dBFS; median F0 ~377 Hz | disclosure is more expansive than later moral-refusal lines; subjective attitude not inferred | Layer C `UNVERIFIED` |
| `E05-AUD-003` | Takina client enjoyment / duty correction | medians ~224 / 236 Hz; RMS ~-29.5 / -28.5 dBFS | positive social perception and operational correction coexist in controlled baseline | Layer C `UNVERIFIED` |
| `E05-AUD-004` | Takina personal heart inquiry | question ~223 Hz median; verification request ~291 Hz | personal curiosity can raise activation without baseline replacement | Layer C `UNVERIFIED` |
| `E05-AUD-005` | Takina `私に任せてください` | RMS ~-27.6 dBFS; median F0 ~251 Hz | operational commitment remains controlled before contact | Layer C `UNVERIFIED` |
| `E05-AUD-006` | Takina urgent `逃げて！` | early ~0.44 s RMS ~-18.7 dBFS; estimated median F0 ~575 Hz; very short/mixed window | exact high-intensity threat condition produces sharp activation; supports `PRED-CP1-006` | pitch supportive/lower-confidence; Layer C `UNVERIFIED` |
| `E05-AUD-007` | Chisato `人の命は奪いたくないんだ` | RMS ~-28.3 dBFS; median F0 ~276 Hz | objectively less activated than E05 playful briefing/talent lines | Layer C `UNVERIFIED` |
| `E05-AUD-008` | Chisato chosen helping purpose | RMS ~-27.4 dBFS; median F0 ~261 Hz | chosen-purpose statement remains comparatively constrained in Layer B | Layer C `UNVERIFIED` |
| `E05-AUD-009` | Takina `いいガイドだったのは...` | RMS ~-31.2 dBFS; median F0 ~209 Hz | precise reassurance occurs inside low-activation controlled envelope | Layer C `UNVERIFIED` |
| `E05-AUD-010` | Chisato `ありがとう` | RMS ~-31.2 dBFS; median F0 ~217 Hz | marked objective contraction relative to playful states | Layer C `UNVERIFIED` |
| `E05-AUD-011` | Takina `本当に鼓動 ないんですね` | RMS ~-27.5 dBFS; median F0 ~222 Hz | private bodily curiosity remains acoustically controlled despite increased permission | Layer C `UNVERIFIED` |


## 5.6 E06 observations and acoustic-performance register

| Observation ID | Scope | Character | Trigger / condition | Behavior | Candidate policy | Confidence |
|---|---|---|---|---|---|---|
| `TAK-MB-E06-001` | 01:05-01:32 | TAK | Lycoris are being individually targeted and Chisato is exposed | independently proposes constant pairing, sleep shifts, and `安全が確保されるまで 24時間 一緒にいます` | `TAK-PROTECT-INIT-01` | HIGH |
| `CHI-MB-E06-001` | 02:48-03:04 | CHI | protective cohabitation begins | reveals multiple safehouses and prior LilyBell pursuit context; current threat nonchalance is therefore experience-conditioned rather than ignorance of targeting | threat-familiarity boundary | HIGH |
| `TAK-MB-E06-002` | 03:48-04:55 | TAK | shared household needs labor allocation and Chisato rejects a fixed schedule as boring | begins with equitable chore schedule, then admits Chisato's play criterion by proposing rock-paper-scissors | `TAK-SYSTEM-ADAPT-01` | HIGH |
| `CHI-MB-E06-002` | household janken | CHI | repeated rock-paper-scissors under stable opening procedure | uses movement/muscle preparation prediction to remain effectively unbeatable after initial tie | `CHI-DODGE-VIS-01` / mundane generalization | HIGH |
| `TAK-MB-E06-003` | household janken + 22:19-22:36 | TAK | recurring game structurally disadvantages her and mechanism becomes legible | identifies the predictive mechanism, later removes the standard opening and wins the cohabitation wager | `TAK-SYSTEM-ADAPT-01` | HIGH |
| `KUR-MB-E06-001` | café/investigation | KUR | ordinary group participation overlaps DA/Lycoris targeting investigation | remains game/café participant while penetrating DA data, tracing leaked imagery, confessing causal involvement, and immediately helping identify Majima | ordinary+technical+repair recurrence | HIGH |
| `CHI-MB-E06-003` | 05:40-06:15 | CHI | Mika reports DA will not share extreme-secret information | mocks institutional secrecy and accepts Kurumi's unauthorized retrieval rather than choosing simple DA obedience or rejection | `CHI-INST-CHALLENGE-01` | HIGH |
| `MAJ-MB-E06-001` | 05:30-07:30 | MAJ | Robota asks whether Majima's objective is understood | dismisses ordinary pawns, defines DA as target (`そのＤＡとやらを ぶっ潰す`), and frames 26 dead comrades through a balance ledger | `MAJ-BALANCE-01` | HIGH |
| `YOS-MB-E06-001` | Robota/Himegama intercut | YOS | Majima lacks spontaneous interest in Chisato | boss-directed additional objective is relayed through Himegama; Robota is told to keep trying and later manufactures Majima interest using Chisato footage | `YOS-PROXY-COERCE-01` | STRONG_INFERENCE |
| `TAK-MB-E06-004` | 14:55-15:27 | TAK | Kurumi confesses her contracted DA hack and the resulting leak is tied to Takina's transfer | spikes in activation while naming guns/terrorists/dismissal, but later refuses to transfer authorship of her firing decision to Kurumi | `TAK-FAIL-ACCOUNT-01` | HIGH |
| `CHI-MB-E06-004` | 18:20-20:12 | CHI | Majima ambushes and severely threatens her | continues rubber/nonlethal fire despite injury and Majima's explicit live-round taunt | `CHI-LIFE-01` | HIGH |
| `CHI-MB-E06-005` | Majima fight + 22:08-22:18 | CHI | visually hostile fight conditions produce unusual injury | evasion advantage degrades when visual preparatory cues are compromised; post-fight Takina explicitly identifies eyes as weakness | `CHI-DODGE-VIS-01` | HIGH |
| `TAK-MB-E06-005` | 18:55-20:10 | TAK | Kurumi locates badly pressured Chisato | rapidly mobilizes to rescue; precise distant fire produces explicit attacker report `脚が！`; later calls `弾切れです！` | `TAK-PROTECT-INIT-01`; `TAK-FORCE-DISCRIM-01` | MODERATE-HIGH |
| `TAK-MB-E06-006` | 21:02-21:19 | TAK | café members invite retaliation against Kurumi after causal reveal | states `あれは私の行動の結果で クルミのせいじゃありません`, then requires Kurumi's continued cooperation through capture | `TAK-FAIL-ACCOUNT-01` expanded to differentiated causality/repair | HIGH |
| `MAJ-MB-E06-002` | 21:25-21:52 | MAJ | after direct fight with Chisato | revises appraisal, calls her worthy, states `あれじゃなきゃ 俺とはバランスが取れねえ`, and demands more information about her | `MAJ-BALANCE-01` | HIGH |
| `TAK-MB-E06-007` | 22:19-22:36 | TAK | Chisato proposes continuing `同棲` after safety crisis | conditions continuation on Chisato winning janken, changes the game structure, wins, and therefore exercises exit agency inside domestic closeness | `TAK-SYSTEM-ADAPT-01`; autonomy boundary | HIGH |

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E06-AUD-001` | Takina `安全が確保されるまで 24時間 一緒にいます` | RMS ~-26.4 dBFS; median F0 ~259 Hz; p10~223 / p90~337 | protective cohabitation initiative is activated but remains far below later threat/play peaks | Layer C `UNVERIFIED` |
| `E06-AUD-002` | Takina `可能性はゼロじゃありません` | RMS ~-28.1 dBFS; median F0 ~238 Hz; p10~215 / p90~275 | controlled risk assessment baseline | Layer C `UNVERIFIED` |
| `E06-AUD-003` | Takina `たきなはクビになりました` | RMS ~-22.1 dBFS; median F0 ~535 Hz; p10~375 / p90~658 | causal confrontation produces major activation without proving a specific heard emotion | Layer C `UNVERIFIED` |
| `E06-AUD-004` | Takina `とりあえず 組事務所へ向かいます！` | RMS ~-23.3 dBFS; median F0 ~375 Hz | partner-threat mobilization expands Layer B above routine speech | Layer C `UNVERIFIED` |
| `E06-AUD-005` | Takina `千束のポンチョとスマホが！` | RMS ~-21.0 dBFS; median F0 ~410 Hz | urgent Chisato-specific threat state strongly activated | Layer C `UNVERIFIED` |
| `E06-AUD-006` | Takina `弾切れです！` | very short/mixed; RMS ~-17.1 dBFS; rough median F0 ~458 Hz | supportive evidence for high combat activation; pitch treated cautiously | Layer C `UNVERIFIED` |
| `E06-AUD-007` | Takina `あれは私の行動の結果で クルミのせいじゃありません` | RMS ~-29.8 dBFS; median F0 ~239 Hz; p10~209 / p90~263 | differentiated accountability contracts back into narrow controlled envelope | Layer C `UNVERIFIED` |
| `E06-AUD-008` | Takina `最後まで協力してもらいますよ` | RMS ~-26.6 dBFS; median F0 ~271 Hz; p10~235 / p90~297 | forward repair obligation remains controlled rather than confrontation-level | Layer C `UNVERIFIED` |
| `E06-AUD-009` | Takina final cohabitation wager | RMS ~-23.8 dBFS; median F0 ~306 Hz | safe domestic negotiation can itself expand activation | Layer C `UNVERIFIED` |
| `E06-AUD-010` | Takina winning `ぽん！` / `よしよしっ！` | very short energetic cues; RMS ~-20.5/-18.4 dBFS; rough medians ~630/~599 Hz | strong safe-play activation proves high pitch/intensity is not specific to threat or negative affect | Layer C `UNVERIFIED` |


## 5.7 E07 observations and acoustic-performance register

| Observation ID | Scope | Character | Trigger / condition | Behavior | Candidate policy | Confidence |
|---|---|---|---|---|---|---|
| `TAK-MB-E07-001` | 03:15-03:22 | TAK | optional café leisure conflicts with Japanese-school work | declines the game and corrects the assumption that her reason is another DA task | `TAK-INDEP-OBLIG-01` | HIGH |
| `TAK-MB-E07-002` | 05:08-05:42 | TAK | DA need/branch staffing is discussed after E06 cohabitation | uses `必要とされてて`, proposes `じゃ 私が戻りますよ`, and later notes training-school return remains available | `TAK-INST-01`; autonomy boundary | HIGH |
| `CHI-MB-E07-001` | 05:25-05:30 | CHI | Takina proposes DA return | says the departure would be lonely and physically clings, but does not veto, shame, or convert the option into betrayal | `CHI-SUPPORT-01` | HIGH |
| `TAK-MB-E07-003` | 06:15-06:18 | TAK | Mika/Kusunoki secrecy invites interpersonal inference | directly asks whether they are `愛人関係`; novel adult relational content appears inside controlled speech | social-domain widening | MODERATE-HIGH |
| `MAJ-MB-E07-001` | 06:45-07:29 | MAJ | Chisato footage reconnects him to old-tower memory | identifies himself as the tower attacker, recognizes Chisato as the same opponent, and calls the recurrence `運命` | `MAJ-BALANCE-01` | HIGH |
| `KUR-MB-E07-001` | Forbidden infiltration | KUR | group needs access to a data-driven membership system | forges credentials while remaining ordinary café/group participant | ordinary+technical recurrence | HIGH |
| `CHI-MB-E07-002` | 14:54-14:56 | CHI | Takina reads Mika/Yoshimatsu encounter through same-sex romance | answers `愛の形は様々なんだよ たきな` without stigma or corrective distancing | queer-normalized social grammar | HIGH |
| `TAK-MB-E07-004` | 16:16-16:18 | TAK | Chisato recognizes the benefactor she has searched for | notices the personal significance and voluntarily leaves Chisato/Yoshimatsu one-to-one space | `TAK-PRIVACY-YIELD-01` | HIGH |
| `CHI-MB-E07-003` | 16:31-16:52 | CHI | she finally meets the person who funded her heart | expresses gratitude and says she wants to use `頂いた時間` to help others like him | `CHI-SELF-AUTH-01` | HIGH |
| `YOS-MB-E07-001` | 17:19-17:56 | YOS | Chisato/Mika challenge the meaning of Alan rescue | says Alan Children have roles and talent is God's property, not the individual's or patron's | `YOS-TALENT-TELOS-01` | HIGH |
| `MIK-MB-E07-001` | 18:06-18:47 | MIK | Yoshimatsu persists in assigning Chisato's talent | points gun, demands Chisato's freedom, claims trigger resolve, then explicitly admits `覚悟なんか あるわけないだろ` | `MIKA-CHI-FREEDOM-01`; `MIKA-YOSHI-CONSTRAINT-01` | HIGH |
| `YOS-MB-E07-002` | 18:58-19:20 | YOS | Takina advocates Chisato's happiness/continued café contact | reframes Chisato's proper `居場所` as elsewhere and tells Takina he expects something from her | `YOS-PROXY-COERCE-01` | HIGH |
| `CHI-MB-E07-004` | 19:45-20:19 | CHI | Mika's long concealment is disclosed | asks why, learns rescue required secrecy, interprets it as Mika keeping a promise, and repairs the current conflict | `CHI-PROMISE-REPAIR-01` | HIGH |
| `TAK-MB-E07-005` | 20:44-20:45 | TAK | manga artist asks whether bad people should be killed | answers `べきですね` without hedging in the fictional normative frame | `TAK-LETHAL-NORM-01` | HIGH |
| `CHI-MB-E07-005` | 21:38-21:41 | CHI | sees manga villain killed | immediately objects `ダメだよ 殺しちゃ` | `CHI-LIFE-01` | HIGH |
| `TAK-MB-E07-006` | 21:41-21:45 | TAK | major biography/revelation has just occurred | redirects Chisato to ongoing café work: business has started, go change | ordinary-routine stabilization | STRONG |

| Acoustic ID | Scope / cue | Objective finding | Character-model effect | Perceptual status |
|---|---|---|---|---|
| `E07-AUD-001` | Takina drawing protest | RMS ~-26.5 dBFS; median F0 ~458 Hz | low-stakes evaluative/comic activation; contamination present | Layer C `UNVERIFIED` |
| `E07-AUD-002` | Takina `必要とされてて` | RMS ~-25.6 dBFS; median F0 ~327 Hz | institutional/status topic is more activated than several controlled baseline samples | Layer C `UNVERIFIED` |
| `E07-AUD-003` | Takina `じゃ 私が戻りますよ` | RMS ~-25.8 dBFS; median F0 ~296 Hz | DA-return offer can remain comparatively controlled/matter-of-fact | Layer C `UNVERIFIED` |
| `E07-AUD-004` | Takina `愛人関係ということですか？` | RMS ~-28.5 dBFS; median F0 ~258 Hz | novel adult social content does not require Chisato-like acoustic expansion | Layer C `UNVERIFIED` |
| `E07-AUD-005` | Chisato `愛の形は様々なんだよ たきな` | RMS ~-29.6 dBFS; median F0 ~219 Hz | queer-normalizing statement is acoustically constrained; subjective attitude not inferred | Layer C `UNVERIFIED` |
| `E07-AUD-006` | Chisato `ヨシさんだよ！` | RMS ~-23.4 dBFS; median F0 ~500 Hz | benefactor recognition produces major objective activation | Layer C `UNVERIFIED` |
| `E07-AUD-007` | Chisato `私も頂いた時間で…` | RMS ~-27.7 dBFS; median F0 ~368 Hz | gifted-time/helping formulation remains distinct from discovery peak | Layer C `UNVERIFIED` |
| `E07-AUD-008` | Mika `千束を自由にしろ！…覚悟がある！` | RMS ~-24.8 dBFS; median F0 ~165 Hz | confrontation substantially activated | Layer C `UNVERIFIED` |
| `E07-AUD-009` | Mika `覚悟なんか あるわけないだろ` | RMS ~-29.7 dBFS; median F0 ~127 Hz | explicit no-resolve admission contracts relative to threat claim | Layer C `UNVERIFIED` |
| `E07-AUD-010` | Takina `でも 千束 喜んでました` | RMS ~-30.4 dBFS; median F0 ~238 Hz | Chisato-centered advocacy occurs in controlled envelope | Layer C `UNVERIFIED` |
| `E07-AUD-011` | Chisato `約束を守ったんだ…` | RMS ~-33.2 dBFS; median F0 ~191 Hz | current repair is strongly contracted relative to discovery state | Layer C `UNVERIFIED` |
| `E07-AUD-012` | Takina `べきですね` | RMS ~-31.8 dBFS; median F0 ~204 Hz | lethal-norm endorsement is acoustically controlled | Layer C `UNVERIFIED` |
| `E07-AUD-013` | Chisato `ダメだよ 殺しちゃ` | RMS ~-28.9 dBFS; median F0 ~407 Hz | anti-killing moral speech can be objectively high activation; no invariant moral-contraction rule | Layer C `UNVERIFIED` |
| `E07-AUD-014` | Majima mission tag | RMS ~-29.5 dBFS; median F0 ~112 Hz; effects/music contamination substantial | supports low male baseline only cautiously | Layer C `UNVERIFIED` |

## 5.8 E08 observations and acoustic-performance register

| Observation ID | Character | Scope/condition | Observation | Analytical use | State |
|---|---|---|---|---|---|
| `TAK-MB-E08-001` | TAK | café deficit | independently takes accounting responsibility and changes ammunition, cleanup, labor, menu, automation and investment procedures | civilian stewardship uses operational rationalism without personality replacement | FACT |
| `TAK-MB-E08-002` | TAK | menu/social feedback | originates new parfait, observes unintended fecal resemblance/social response, and withdraws it | self-authored civilian creation includes failure and revision | FACT |
| `TAK-MB-E08-003` | TAK | Chisato health/safety | schedules checkup, sets three-ring rule, relocation expectation, and escalates armed when routine breaks | care is often administrative/procedural and action-backed | FACT |
| `TAK-MB-E08-004` | TAK | Chisato important place | says `大切な場所なんでしょ？` after sustained work to keep café open | place-preservation is explicitly person-directed before own-home declaration | FACT |
| `CHI-MB-E08-001` | CHI | Alan purpose pressure | after learning violent Alan-recipient evidence, reasserts helping and `やりたいようにやります` | self-authorship survives ideological pressure | FACT |
| `CHI-MB-E08-002` | CHI | Takina practical care | interprets contact protocol as `どこにいても来てくれる`, resumes cohabitation/food play, later gives direct `ありがと` | translates procedural care into relational meaning | FACT |
| `CHI-MB-E08-003` | CHI | injection/clinic | says injection is painful, cannot be dodged, and involves unwanted foreign-object entry; Himegama exploits trusted medical access | bodily-control vulnerability is mechanism-specific, not cowardice | FACT |
| `MAJ-MB-E08-001` | MAJ | private encounter | suspends immediate violence for movies/drinks/mission exchange, claims moral category with Chisato, retains antagonist project | ordinary commonality does not remove ideological violence | FACT |
| `YOS-MB-E08-001` | YOS | role doctrine + proxy action | denies gifted person's choice, dismisses café life as `ままごと`, uses Himegama through medical trust, blames Mika | coercion escalates from teleology to bypass of agency | FACT/STRONG_INFERENCE |
| `HIG-MB-E08-001` | HIG | clinic | infiltrates trusted medical routine and incapacitates Chisato rather than defeating her through frontal combat | proxy exploits access/control rather than superior raw combat | FACT |

Representative Layer-B routes: `E08-AUD-001`–`015`. Takina's E08 topology again spans constrained practical care, activated responsibility/security, ordinary creation, and very high safe-play laughter. High activation is therefore not a valence label. Chisato's `やりたいようにやります` is acoustically dynamic while `ありがと` is more constrained; moral/relational seriousness has no single Layer-B signature. Layer C remains `UNVERIFIED`.

## 5.9 E09 observations and acoustic-performance register

| Observation ID | Character | Scope/condition | Observation | Analytical use | State |
|---|---|---|---|---|---|
| `TAK-MB-E09-001` | TAK | clinic nonresponse/threat | executes E08 check-in rule, physically searches, confronts Himegama, calls for Chisato | safety protocol is durable behavior; partner threat rapidly mobilizes action | FACT |
| `TAK-MB-E09-002` | TAK | prognosis / attacker | immediately states `あの看護師を始末します`; later constrains Chisato's running and apologizes for exertion | lethal independence and procedural care coexist under person-specific threat | FACT |
| `TAK-MB-E09-003` | TAK | DA reinstatement | initially cannot celebrate reinstatement; later says she had intended to refuse, then chooses return because it may help Chisato live | institutional return changes from identity end to person-directed instrument | FACT |
| `TAK-MB-E09-004` | TAK | separation conversation/outside day | insists on telling Chisato herself, designs a civilian outing with detailed schedule, persists through disruption | relational accountability and ordinary-life authorship become self-generated | FACT |
| `CHI-MB-E09-001` | CHI | two-month prognosis / revenge | accepts prognosis, rejects killing Himegama because it changes nothing, continues ordinary action | anti-killing and irreversible-loss policies survive direct self-harm | FACT |
| `CHI-MB-E09-002` | CHI | Kusunoki role pressure | rejects DA's definition of her role while bargaining for Takina's reinstatement | self-authorship + selective institutional cooperation remain compatible | FACT |
| `CHI-MB-E09-003` | CHI | childhood Alan gift | interprets `救世主` language and gifted gun as rescue/helping rather than intended killing role | direct historical origin for gift reinterpretation / helping vocation | FACT |
| `CHI-MB-E09-004` | CHI | final outing / mortality | says imperfect activity is fun because Takina is there; articulates `受け入れて 全力！` | finite-time practice values actually lived relation over perfect plan execution | FACT |
| `MIK-MB-E09-001` | MIK | Alan-heart flashback | knowingly accepts heart under killing-talent delivery condition; later narrates `親子ごっこ` with guilt | present fatherhood emerges from ethically compromised origin | FACT |
| `MIK-MB-E09-002` | MIK | current guilt | smokes as self-punishment and, after disclosure pressure, initiates contact with Yoshimatsu | guilt shifts toward active reckoning without yet establishing severance outcome | FACT |
| `YOS-MB-E09-001` | YOS | heart bargain + private promise | prioritizes bringing killing talent to world, then says Chisato is `私たちの娘` and care is `約束さ 君と私の` | teleological coercion is personally intimate, not merely bureaucratic | FACT |
| `KUR-MB-E09-001` | KUR | scrubbed Alan traces | moves from failed digital search to Mika as human source and frames disclosure as necessary for Chisato | technical method expands into contextual/human-source inference | FACT |
| `MAJ-MB-E09-001` | MAJ | episode tag | independently reaches Yoshimatsu and addresses him directly | Chisato/Alan and anti-DA conflict lines physically converge; alliance remains open | FACT |

Representative Layer-B routes: `E09-AUD-001`–`018`. Takina's E09 topology is especially diagnostic: threat/protection can be highly activated (`E09-AUD-002/005/010`), while the deliberate high-stakes decision to return to DA for Chisato is comparatively constrained (`E09-AUD-012`) and `分かりません` contracts further (`E09-AUD-015`). Importance therefore does not map monotonically to F0/intensity. Chisato's serious E09 speech likewise ranges from constrained mortality/role lines to highly activated `受け入れて 全力！`; Layer C remains `UNVERIFIED`.


## 5.10 E10 observations and acoustic-performance register

| Observation ID | Character | Scope/condition | Observation | Analytical use | State |
|---|---|---|---|---|---|
| `CHI-MB-E10-001` | CHI | impending death / cafe closure | closes LycoReco partly to avoid consuming others' time, insists the place remain enjoyable, yet later admits sadness | finite-time ethic includes others' time and chosen loss can remain painful | FACT |
| `CHI-MB-E10-002` | CHI | compromised-origin disclosure | thanks Mika for letting her decide and claims work/cafe as her own choices | strongest direct self-authorship statement so far | FACT |
| `CHI-MB-E10-003` | CHI | parental recognition | directly asks whether Mika likes the present Chisato and receives proud-daughter recognition | under origin vulnerability, actively seeks affirmation of present self | FACT |
| `CHI-MB-E10-004` | CHI | Yoshimatsu hostage / public crisis | refuses to abandon Yoshimatsu, seeks direct answer, trusts Takina/Fuki with Enkuboku | life preservation, epistemic separation, and distributed competence coexist | FACT |
| `TAK-MB-E10-001` | TAK | DA interrogation / expulsion threat | invokes prior firing and says outside life was fairly enjoyable, making another firing tolerable leverage | outside life reduces DA's coercive monopoly over belonging | FACT |
| `TAK-MB-E10-002` | TAK | restored DA access | pursues Alan/Yoshimatsu leads and tells Majima he is not her objective | DA access functions as person-specific rescue infrastructure | FACT |
| `TAK-MB-E10-003` | TAK | captured intermediary | uses severe controlled physical coercion while leaving captive alive | ethical development remains incomplete and distinct from Chisato's doctrine | FACT |
| `MIK-MB-E10-001` | MIK | confession | admits original commander-interest and strongest-killer bargain; explains concealment as protecting Chisato's decision-space | fatherhood explicitly reckons with original complicity | FACT |
| `MIK-MB-E10-002` | MIK | hostage crisis | after confession, equips/supports Chisato for Yoshimatsu rescue | protective policy becomes active/operational | FACT |
| `YOS-MB-E10-001` | YOS | Majima confrontation | calls Chisato's divergence his failure and offers his own life to Alan's ideal | teleology includes self-objectification | FACT |
| `MAJ-MB-E10-001` | MAJ | DA/Alan confrontation | attacks hidden moral-management systems yet forces civilians into armed exposure experiment | anti-paternal critique reproduces coercive self-authorization | FACT |
| `KUR-MB-E10-001` | KUR | heart-origin investigation | combines technical research with social/legal inference about unregistered Lycoris vulnerability | multi-method repair investigation persists | FACT |
| `KUS-MB-E10-001` | KUS | Enkuboku crisis | articulates DA's pre-legal guardianship and epistemic-peace ideal; constrained by higher command | institutionally coherent legitimacy doctrine with command-friction | FACT |

Representative Layer-B routes: `E10-AUD-001`-`019`. Takina again shows high activation in immediate command/threat speech while deliberate Yoshimatsu-focused decisions are comparatively controlled. Chisato's serious speech spans low-intensity sadness/gratitude and highly activated rescue refusal. Semantic importance therefore does not map monotonically to F0 or intensity; Layer C remains `UNVERIFIED`.


| `TAK-MB-E11-001` | E11 opening | TAK | Chisato/Mika fail expected contact during active crisis | treats nonresponse as operationally anomalous and leaves briefing to investigate while promising to return for operation | `TAK-PROTECT-INIT-01` | HIGH |
| `KUR-MB-E11-001` | E11 airport/research | KUR | free departure from closed LycoReco + Chisato rescue need | explicitly remembers LycoReco as fun, then voluntarily returns and produces improved-heart lead | `KUR-CHOSEN-RETURN-01` | HIGH |
| `YOS-MB-E11-001` | E11 historical recording | YOS | talented researcher needs human experiment for improved heart | calls girl a suitable experimental subject and discounts one life against talent/future patients | `YOS-TALENT-TELOS-01` | HIGH |
| `TAK-MB-E11-002` | E11 heart-lead briefing | TAK | highly desired rescue solution appears under adversarial conditions | says she has a bad feeling and explicitly suspects a trap | `TAK-THREAT-INFER-01` | HIGH |
| `TAK-MB-E11-003` | E11 DA departure | TAK | told leaving operation means no DA return | answers `分かってます`, says DA cannot save Chisato, and leaves | `TAK-INST-EXIT-01` | HIGH |
| `ERI-MB-E11-001` | E11 DA departure | ERI | Takina is leaving operation tied to Erika's old incident | accepts responsibility, apologizes, and offers to fill Takina's position | `ERI-DIRECT-REPAIR-01` | HIGH |
| `FUK-MB-E11-001` | E11 DA departure | FUK | Takina chooses Chisato over final institutional chance | states consequence, verifies understanding, then says `行けよ` | `FUK-COSTLY-PERMISSION-01` | HIGH |
| `KUS-MB-E11-001` | E11 Enkuboku/exposure | KUS | hidden terror assault followed by public Lycoris identification | assault side receives total-kill doctrine; exposure then forces `発砲禁止`, making secrecy a tactical constraint | institutional policy rather than personal preference | HIGH |
| `MIK-MB-E11-001` | E11 old-tower entrance | MIK | terminal daughter chooses solo rescue of Yoshimatsu | questions choice but does not overrule; answers `いってこい` to `いってきます` | autonomy-supportive fatherhood; `MIKA-PROTECT-ACT-01` partial | HIGH |
| `CHI-MB-E11-001` | E11 tower ascent | CHI | armed enemies obstruct personally urgent rescue | uses decisive force while warning about fatal falls and helping an endangered opponent stabilize | `CHI-LIFE-01`; `CHI-ENEMY-CONTINGENT-01` | HIGH |
| `CHI-MB-E11-002` | E11 Yoshimatsu line-of-fire | CHI | Majima weaponizes Yoshimatsu as ballistic constraint | accepts being hit rather than simply evade through a line that would expose Yoshimatsu | life-preservation under relational tactical cost | HIGH |
| `CHI-MB-E11-003` | E11 dark fight | CHI | visual information deliberately degraded | evasion advantage falls sharply while Majima exploits auditory orientation | `CHI-DODGE-VIS-01` | HIGH |
| `CHI-MB-E11-004` | E11 Majima recruitment | CHI | adversary claims shared rejection of imposed life-paths and proposes alliance | rejects grouping with `一緒にすんな！` while continuing fight | `CHI-ANTI-EQUIV-01` | HIGH |
| `MAJ-MB-E11-001` | E11 public exposure | MAJ | digital revelation can be dismissed as fabrication | engineers armed embodied witnesses and direct Lycoris encounters; later recruits Chisato through anti-coercion commonality | `MAJ-BALANCE-01`; coercive exposure modifier | HIGH |
| `TAK-MB-E11-004` | E11 closing fight | TAK | reaches Chisato/Majima crisis after leaving DA | enters firefight directly with severe/live-force willingness and repeats Majima is not her objective | `TAK-PROTECT-INIT-01`; lethal independence retained | HIGH |

Representative Layer-B routes: `E11-AUD-001`-`014`. Takina's decisive DA-exit criterion can be acoustically quieter or more expanded depending on line/state, and her crisis arrival spikes strongly. Chisato's serious lines range from quiet departure through expansive combat play and extreme `一緒にすんな`; Layer-B magnitude does not identify moral importance or subjective affect. Layer C remains `UNVERIFIED`.


| `CHI-MB-E12-001` | E12 Yoshimatsu confrontation | CHI | Yoshimatsu explicitly defines killing/world contribution as her happiness and proper role | rejects donor-purpose authority, says received life cannot authorize taking another life, and distinguishes her lived happiness from assigned contribution | strengthen `CHI-SELF-AUTH-01`; `CHI-LIFE-01` | HIGH |
| `YOS-MB-E12-001` | E12 heart reveal | YOS | Chisato refuses killing vocation despite direct confrontation | implants/holds improved heart in own body and offers his death as price of Chisato survival/purpose realization | strengthen `YOS-TALENT-TELOS-01`; self-sacrificial coercion modifier | HIGH |
| `TAK-MB-E12-001` | E12 Yoshimatsu confrontation | TAK | actionable replacement-heart route becomes available | inventories Yoshimatsu causality, then explicitly discards punishment/blame priority to focus on obtaining heart | `TAK-CHI-SURVIVAL-PRIORITY-01` | HIGH |
| `TAK-MB-E12-002` | E12 heart crisis | TAK | Chisato refuses to kill Yoshimatsu for implanted heart | says she will do it, threatens to tear heart out, resists Chisato restraint; severe/live force remains available | `TAK-CHI-SURVIVAL-PRIORITY-01`; strengthen `TAK-PROTECT-INIT-01` | HIGH |
| `CHI-MB-E12-002` | E12 heart crisis | CHI | Takina tries to kill Yoshimatsu to save her | physically restrains Takina and states `ヨシさんを殺して生きても それは もう私じゃない` | `CHI-IDENTITY-CONTINUITY-01` | HIGH |
| `TAK-MB-E12-003` | E12 heart crisis | TAK | force solution blocked; Chisato accepts mortality boundary | contracts from scream to `嫌だ 千束が死ぬのは嫌だ`; explicit person-specific survival desire | attachment-state evidence; `TAK-CHI-SURVIVAL-PRIORITY-01` | HIGH |
| `CHI-MB-E12-003` | E12 wounded Yoshimatsu | CHI | coercive benefactor is wounded after demanding lethal realization | checks wound, rejects self-disposal, says she hates his coercion, returns Alan pendant, preserves gratitude and asks him to live | strengthen `CHI-LIFE-01`; `CHI-SELF-AUTH-01` | HIGH |
| `KUR-MB-E12-001` | E12 rescue/Enkuboku | KUR | heart rescue and Lycoris liquidation crisis | provides transport/intelligence, control-room route, defeats/locates Robota, alerts police, takes over/restores Radiata, enables media reclassification | strengthen `KUR-CHOSEN-RETURN-01`; crisis-integration evidence | HIGH |
| `KUS-MB-E12-001` | E12 covert rescue | KUS | upper command orders exposed Lycoris liquidation | secretly requests LycoReco rescue through Mika while preserving deniability | `KUS-SELECTIVE-SUBVERSION-01` | HIGH |
| `KUS-MB-E12-002` | E12 post-cover command | KUS | Radiata/media reclassification changes exposure conditions; Chisato asks `続けますか？` | orders LilyBell withdrawal and resumes overt command through Fuki | strengthen `KUS-SELECTIVE-SUBVERSION-01` | HIGH |
| `FUK-MB-E12-001` | E12 Enkuboku | FUK | Takina has defected; upper-command crisis/standby constrains team | ratifies Takina's non-return in abrasive register, then breaks standby and redistributes rescue/assault tasks | strengthen `FUK-COSTLY-PERMISSION-01`; independent-judgment evidence | HIGH |
| `ERI-MB-E12-001` | E12 Enkuboku/post-crisis | ERI | Takina's position is vacant and prior guilt has been acknowledged | explicitly says she must fill Takina's role; later receives Takina's thanks and admits she should have told Kusunoki | strengthen `ERI-DIRECT-REPAIR-01` | HIGH |
| `CHI-MB-E12-004` | E12 LycoReco crisis restart | CHI | exposed Lycoris face liquidation and Kurumi offers a rescue route | declares `リコリコ営業再開だ` and mobilizes voluntary network toward rescue | strengthen `CHI-HLP-LOCAL-01`; crisis-scale modifier | HIGH |
| `CHI-MB-E12-005` | E12 Kusunoki contact | CHI | public interpretation and tactical conditions have shifted | contacts Kusunoki directly with `錦木千束です 続けますか？`, enabling institutional withdrawal/recommand rather than overthrow | strengthen `CHI-INST-CHALLENGE-01` | HIGH |
| `TAK-MB-E12-004` | E12 post-crisis repair | TAK | Erika explains withheld guilt/history | accepts repair and answers with dry literal `確かに ひどいヤツだ`; controlled baseline returns after extreme crisis | strengthen `TAK-TEASE-EMERG-01`; additive-development evidence | HIGH |
| `CHI-MB-E12-006` | E12 exit/cliffhanger | CHI | notices person-specific bag is missing while leaving danger zone | turns back because it was given by Takina; ordinary relational object remains highly salient under terminal/crisis conditions | person-specific attachment evidence | HIGH |

Representative Layer-B routes: `E12-AUD-001`-`020`. Takina spans very quiet DA-exit speech, controlled rescue planning, extreme blocked-rescue activation, a highly activated scream, and then a much quieter explicit `嫌だ 千束が死ぬのは嫌だ`. Chisato's serious ethical speech likewise ranges from constrained `世界よりも大切なものが`/institutional challenge to highly activated `それは もう私じゃない`. Layer-B magnitude therefore does not identify semantic importance or subjective affect. Layer C remains `UNVERIFIED`.


## 5.11 E13 observations and acoustic-performance register

| Observation ID | Context | Character | Trigger / premise | Observed response | Policy implication | Confidence |
|---|---|---|---|---|---|---|
| `TAK-MB-E13-001` | E13 Fuki task division | TAK | two simultaneous person-specific rescue tasks require different competent agents | proposes `私たちで決めましょう`; assigns herself Chisato and Fuki Sakura based on who can presently save whom | `TAK-NEGOTIATED-COMPETENCE-01` | HIGH |
| `FUK-MB-E13-001` | E13 task division | FUK | Takina proposes peer-authored division outside simple command hierarchy | accepts and says `千束を頼む` | costly mutual recognition now includes explicit trust in Takina's Chisato-specific competence | HIGH |
| `CHI-MB-E13-001` | E13 Majima duel | CHI | live-capable/less-familiar ammunition condition plus terminal physiological strain | retains target discrimination and refuses revenge killing; Majima survives | strengthen `CHI-LIFE-01`; ammunition is not ethical determinant | HIGH |
| `MAJ-MB-E13-001` | E13 duel/debate | MAJ | Chisato challenges moral self-certification | restates balance doctrine, conditional allegiance to weaker side and independent counterforce identity | strengthen `MAJ-BALANCE-01` | HIGH |
| `CHI-MB-E13-002` | E13 values/legacy dialogue | CHI | Majima presses world-historical justification and death is still expected | names concrete people/places/experiences as `私の全部` and wants to remain in memories of people who need her | `CHI-PARTICULARIST-WORLD-01`; `CHI-LEGACY-MEMORY-01` | HIGH |
| `TAK-MB-E13-002` | E13 Majima crisis | TAK | acute Chisato danger | enters without DA authorization, attacks Majima and rescues Chisato through collapse | strengthen `TAK-PROTECT-INIT-01` and `TAK-CHI-SURVIVAL-PRIORITY-01` | HIGH |
| `MIK-MB-E13-001` | E13 Yoshimatsu confrontation | MIK | protecting Chisato requires direct confrontation with former intimate/co-parent | reveals concealed physical capability, defeats Himegama, confronts Yoshimatsu at gunpoint and argues children must lead adults | protective severance; parenthood now explicitly choice-protective | HIGH |
| `CHI-MB-E13-003` | E13 post-surgery disappearance | CHI | expects death and dislikes others' somber farewell | leaves unilaterally for a good final place rather than permit relational accompaniment | `CHI-AVOID-SOMBRE-01` negative modifier on self-authorship | HIGH |
| `TAK-MB-E13-003` | E13 search/reunion | TAK | Chisato disappears without network/camera trail | uses civilian Saori photograph and person-centered information route to locate her, then directly challenges the avoidance | `TAK-PERSON-SEARCH-01` | HIGH |
| `CHI-MB-E13-004` | E13 heart/token aftermath | CHI | survives via replacement heart delivered after Yoshimatsu death | accepts life without accepting assigned vocation; discards recovered Alan token while retaining gratitude and relationships | `CHI-GIFT-WITHOUT-TOKEN-01`; strengthen `CHI-GRATITUDE-NONOWN-01` | HIGH |
| `TAK-MB-E13-004` | E13 beach future dialogue | TAK | Chisato now has an unexpectedly open future | proposes beginning with things terminal prognosis made Chisato give up | `TAK-FUTURE-RESTORE-01` | HIGH |
| `CHI-MB-E13-005` | E13 Hawaii/Kusunoki | CHI | DA requests work after prior rupture | remains selectively cooperable but refuses current job because she is in Hawaii; jokes about passport/LilyBell | strengthen `CHI-INST-CHALLENGE-01`; refusal agency preserved | HIGH |
| `KUR-MB-E13-001` | E13 post-crisis | KUR | Chisato survival and ensemble future require technical/logistical continuity | coordinates surgeon/heart information, shares Mika's secret, continues as mobile LycoReco participant | technical/social dual role fully integrated at TV endpoint | HIGH |

Representative Layer-B routes: `E13-AUD-001`-`025`. Takina shows extreme Chisato-threat activation (`千束～！`, rescue screams), comparatively controlled explicit care (`元気そうで何よりです`, `あなたは死にません`) and future advice, plus high safe-play activation. Chisato's serious philosophy also spans controlled and comparatively activated windows. Layer-B magnitude remains non-monotonic with semantic importance; Layer C remains `UNVERIFIED`.


## 5.12 Short 01 observations and acoustic-performance register

| Observation ID | Context | Character | Trigger / premise | Observed response | Policy implication | Confidence |
|---|---|---|---|---|---|---|
| `TAK-MB-SHORT01-001` | Short01 hanami service | TAK | seasonal operation needs additional stock | handles supplier call and has already placed an additional alcohol order before Chisato asks | strengthens portable civilian stewardship/optimization; competence serves ordinary institution | HIGH |
| `TAK-MB-SHORT01-002` | Short01 profit/expansion talk | TAK | discovers the event is profitable | proposes weekly repetition and independently proposes yakitori for next year; disappointment comes from Mika having proposed it first, not from rejecting the idea | strengthens `TAK-PREF-GEN-01` and civilian initiative; preference can be practical/profit-shaped | HIGH |
| `TAK-MB-SHORT01-003` | Short01 open-window dispute | TAK | mundane security cue in a safe festival setting | carries handgun plus multiple magazines under festival outfit and defends readiness with `平気ですよ` / `上手にやりますから` | operational grammar persists inside civilian life; context calibration remains distinct from competence | HIGH |
| `CHI-MB-SHORT01-001` | Short01 weapon dispute | CHI | discovers Takina is heavily armed in mundane setting | chases Takina and tries to take the weapon, framing Takina's response as the danger rather than challenging her general capability | strengthens role/context-bounding rather than competence suppression | HIGH |
| `MIK-MB-SHORT01-001` | Short01 cafe throughput | MIK | high seasonal customer demand plus Mizuki drinking | manages tea/dango throughput and tells Chisato not to keep feeding Mizuki alcohol | everyday father/proprietor regulation remains active | HIGH |
| `MIZ-MB-SHORT01-001` | Short01 party | MIZ | low-stakes hanami social setting | drinks and performs karaoke as ordinary group member | ordinary adult/social register independently recurs | HIGH |
| `KUR-MB-SHORT01-001` | Short01 party | KUR | Mizuki karaoke/social play | heckles and joins comic rhythm without technical task | utility does not exhaust ensemble membership | HIGH |

Representative Layer-B routes: `SHORT01-AUD-001`-`013`. Takina's business/profit statements can remain controlled while the safe `来年焼き鳥やりますか！` proposal expands strongly; Chisato's chase and Kurumi's heckling are also highly activated. Safe commerce/play therefore supplies another independent counterexample to threat-exclusive or semantically monotonic acoustic activation. Layer C remains `UNVERIFIED`.

# 6. Character-state snapshots

| Snapshot | Character | Source horizon | Stable observations at this boundary | Active state/development notes | Major unknowns |
|---|---|---|---|---|---|
| PRE-E01 | CHI | none | none admitted | `UNOBSERVED_IN_V2` | all policies open |
| E01 | CHI | E01 | proactive social initiation; local-help orientation; enemy-inclusive nonlethality; institutionally knowledgeable but not simply anti-DA; humor/teasing | first V2 baseline only | motive for nonlethality; self-risk limits; rejection response; Yoshimatsu history; private vulnerability |
| PRE-E01 | TAK | none | none admitted | `UNOBSERVED_IN_V2` | all policies open |
| E01 | TAK | E01 | formal/institution-oriented; DA-return goal; care can override orders; competence-validated third-party risk; direct clarification; emerging semantic teasing | first V2 baseline only | civilian preferences; emotional self-description; response to DA rejection; lethal-force baseline; intimacy register |
| E01 | FUK | E01 | chain-of-command orientation; Erika care; anger at Takina risk | bounded evidence | whether anger generalizes; relation to Chisato/Takina outside crisis |
| E01 | MIK | E01 | café authority; `先生` relation with Chisato; DA link; accepts Takina | bounded evidence | history, motives, deeper care structure |
| E01 | MIZ | E01 | ex-DA critical insider; pragmatic cleanup/cost awareness | bounded evidence | broader personality/ethics |
| E01 | KUS | E01 | capture when useful; lethal secrecy; organizational self-protection; narrative control | institutional baseline | personal versus role-derived motives |
| E01 | YOS | E01 | public-beneficence association; hidden hack commission; Chisato recognition; ignorance statement | minimal baseline | goals, Chisato relation, Alan doctrine |
| E02 | CHI | E01-E02 | E01 policies recur; calibrated delegation; costly enemy treatment; explicit contingent-enemyhood language; rapid Kurumi incorporation | social/life policies gain independent recurrence; survival relief visibly/acoustically load-bearing | motive for nonlethality still not causally established; hard self-risk limits open |
| E02 | TAK | E01-E02 | operational compression persists; safe social participation expands; dry correction recurs; urgent state raises acoustic activation; perceived failure produces self-accounting; mission-coordinate objection explicit | additive development supported; ethical divergence with Chisato explicit | DA-return trajectory not tested in E02; response to institutional rejection still open |
| E02 | KUR | E02 | seasoned hacker identity behind Walnut; participates in staged-death survival plan; transitions into named café role | first bounded V2 baseline | age/history, ordinary preferences, relational limits open |
| E02 | YOS | E01-E02 | hidden intervention plus explicit tool/cleanup language | instrumental orientation strengthened | Alan purpose and Chisato relation remain open prospectively |
| E03 | CHI | E01-E03 | support for another's DA goal now survives direct institutional challenge; severe vulnerability elicits explicit person-specific affirmation, strong initiated touch, widened options, and returned choice | social play remains baseline but gains a severe-distress modifier; selective DA challenge becomes explicit | limits under rejection/betrayal; own private vulnerability; deeper Yoshimatsu/Mika history remain open |
| E03 | TAK | E01-E03 | DA return remains central; DA loss is home/parent/status/place injury; social participation remains additive; symbolic reciprocity and voluntary ordinary-life trial now appear; competence-based imposed risk persists with Chisato | first major belonging fracture and self-authored participation; Layer-B envelope strongly state-conditioned | whether DA goal changes after E03; consent modifier for tactical risk; independent civilian preferences still sparse |
| E03 | FUK | E01-E03 | DA gratitude/parent logic explicit; Chisato familiarity and combative banter persist; Takina rejection remains harsh | bounded peer/institutional model expands | whether Takina/Fuki repair occurs; private motive mix open |
| E03 | ERI | E03 | explicitly rejects simple `Takina did not care` narrative and wants to address relationship but lacks route | first bounded V2 baseline | direct repair behavior and broader personality open |
| E03 | KUR | E02-E03 | information utility and ordinary board-game/cafe participation coexist | local integration gains recurrence | durable belonging/independent preferences open |
| E03 | KUS | E01-E03 | denies Radiata compromise while Takina remains displaced; refuses implied performance-for-reinstatement contract | institutional self-protection and discretionary evaluation strengthened | personal motives versus role/system logic remain open |
| E03 | SAK | E03 | new Fuki partner; uses rumor-based caricature to taunt Takina; high shooting precision | first bounded V2 baseline | relationship depth, independent motives, ordinary behavior open |

| E05 | CHI | E01-E05 | E04 self-authorship/time/nonlethality policies survive direct coercive test; artificial heart and Alan life-gift become explicit; Chisato refuses donor-purpose ownership and converts gratitude into chosen helping; accepts narrow repair after staged deception | biographical premise deepens without proving medical mortality caused finite-time ethic | exact medical chronology/prognosis; response to recognizing Yoshimatsu; limits under higher coercion |
| E05 | TAK | E01-E05 | controlled operational baseline persists alongside self-initiated personal bodily inquiry, explicit boundary learning, independent protection initiative, sharp threat activation, and precise post-deception reassurance | reciprocal curiosity and relationship-specific permissions expand without personality replacement or DA-state resolution | DA-return desire not tested; broader privacy rules; stable intimacy limits; risk-consent modifiers |
| E05 | KUR | E01-E05 | routine group participation and technical intelligence function remain simultaneous | ordinary+utility model strengthened | durable future role/dependence |
| E05 | MIK | E01-E05 | knows Alan/artificial-heart provenance and explicitly states Chisato's mission is hers to decide | self-authorship stance directly anchored | complete past promise/complicity remains outside E05 horizon |
| E05 | YOS | E01-E05 | assigned-purpose teleology is now paired with strongly inferred staged proxy coercion | ideology becomes operational method | exact remote operator and full plan remain open |
| E05 | MAJ | E01-E05 | post-concealment escalation now explicitly targets Lycoris | anti-hidden-order violence becomes person-targeted | target-selection/proportionality details remain open |

| E06 | CHI | E01-E06 | severe personal attack still does not dislodge nonlethality; evasion is now explicitly bounded by visual access; DA relation remains selectively cooperative/circumventing; domestic closeness with Takina is welcomed but not imposed as permanent | combat legend becomes mechanically bounded rather than mythical; life-preservation policy survives high self-risk | hard catastrophic-tradeoff limits; full LilyBell history; Alan recognition/confrontation remain open |
| E06 | TAK | E01-E06 | independently initiates 24h partner protection; adapts domestic rules after learning mechanism; distinguishes own action from Kurumi's causal contribution and requires repair; rescues Chisato with precision; retains exit agency after cohabitation | responsibility model becomes more differentiated; protection and domestic play both widen Layer-B state range without baseline replacement | DA-return state still not retested; general nonvital-force policy and future domestic preferences remain open |
| E06 | KUR | E01-E06 | ordinary café participation, deep technical access, causal confession, and immediate reparative intelligence work coexist | causal involvement increases rather than terminates group utility/participation | trust consequences and durable belonging remain open |
| E06 | MAJ | E01-E06 | DA destruction goal and balance logic explicit; after Chisato fight he selects her as personal counterweight while retaining broader anti-DA project | target logic gains person-specific worthy-opponent modifier | limits of balance proportionality and later treatment of Chisato open |
| E06 | YOS | E01-E06 | assigned-purpose ideology now has a clearer proxy architecture through Himegama/Robota and engineered Majima attention | coercion method strengthened beyond E05 strong inference, while exact knowledge distribution across intermediaries remains bounded | direct Chisato response/recognition and full plan remain open |

| E07 | CHI | E01-E07 | identifies Yoshimatsu as benefactor; preserves gratitude while interpreting gifted time as helping; normalizes plural/same-sex love; repairs Mika's past concealment through promise-context; anti-killing rule remains explicit | benefactor biography is integrated without replacing present vocation; same-sex normalization is worldview evidence, not dyad confession | direct completed killing mandate from Yoshimatsu not yet heard; future response to stronger coercion/new secrecy open |
| E07 | TAK | E01-E07 | independent civilian obligation/refusal, live DA-return option, adult relational inference, privacy-yielding care, Chisato-centered advocacy, and explicit lethal-norm difference coexist | ordinary/social bandwidth continues widening while DA/place vocabulary and moral independence remain live | response to Yoshimatsu `居場所` recruitment; real-stakes lethal policy; later DA choice open |
| E07 | MIK | E01-E07 | explicitly chooses Chisato's freedom against Yoshimatsu yet cannot honestly claim lethal severance; old promise/intimate history surface | fatherhood conflict is real but constrained by enduring bond/history | later threshold for direct severance/action open |
| E07 | YOS | E01-E07 | divine-property talent doctrine explicit; Alan role pressure direct; Takina recruited as placement proxy | coercion best modeled as teleological stewardship plus proxy shaping, not personal possession | exact next coercive step and Takina uptake open |
| E07 | MAJ | E01-E07 | identifies Chisato as old-tower opponent, calls recurrence fate, continues DA/visibility escalation | personalized counterweight becomes historical as well as tactical | Chisato reciprocal recognition/history and later escalation form open |
| E07 | KUR | E02-E07 | remains ordinary participant and principal technical facilitator, including forged Forbidden credentials | dual social/technical role remains stable after E06 repair | durability under deeper DA compromise open |

| E08 | CHI | E01-E08 | self-authored helping survives Alan violent-recipient evidence; benefactor model remains defended under indirect contradiction; Takina care is translated into domestic/personal meaning; injection/control vulnerability becomes explicit; trusted medical access successfully bypasses combat advantage | self-authorship is now tested against both ideology and bodily coercion; benefactor-defense and bodily-control modifiers added | direct proof of Yoshimatsu's responsibility has not yet been personally integrated; medical mortality as origin of finite-time ethic remains open |
| E08 | TAK | E01-E08 | takes café accounting/maintenance ownership, originates and revises civilian products, manages Chisato health/safety, rapidly mobilizes armed under partner threat, and preserves Chisato-valued place while retaining distinct lethal capability | operational rationalism becomes portable civilian stewardship and person-specific procedural care; ordinary agency increasingly generative | own permanent-home declaration and DA revocation remain open; general nonvital-force doctrine not established |
| E08 | YOS | E01-E08 | denies gifted-person choice, frames birth talent as role, dismisses ordinary alternative as play, and escalates through Himegama/medical trust | assigned-purpose coercion now includes explicit anti-choice doctrine plus agency bypass | Chisato has not yet directly attributed clinic harm to him |
| E08 | MAJ | E01-E08 | shares movies/drinks and anti-determinist talk with Chisato, reveals old-tower/Alan commonality, claims sameness, remains morally rejected | selected-opponent relation can host ordinary commonality without alliance | limits of temporary nonviolence and next public escalation open |
| E08 | HIG | E08 | uses trusted medical setting and incapacitating injection against Chisato | first bounded proxy-access baseline | motive interiority and exact technical intervention remain open |

| E09 | CHI | E01-E09 | explicit two-month prognosis; rejects revenge killing after direct bodily harm; rejects DA role ownership; child `救世主`/helping-gun reinterpretation revealed; continues ordinary action and person-specific enjoyment under known mortality | self-authorship now has a directly shown childhood interpretive origin; finite-time practice is strengthened while sole mortality causation is rejected | direct present attribution of Himegama/Yoshimatsu responsibility remains incomplete; deterioration threshold and response to explicit benefactor betrayal open |
| E09 | TAK | E01-E09 | safety protocol triggers physical search; lethal response to attacker remains available; prognosis immediately changes field care; DA reinstatement becomes a route to save Chisato; originates final civilian outing and owns separation conversation | DA moves from total identity/end toward selectively instrumental infrastructure; person-specific protection and ordinary-life authorship deepen without moral convergence | whether DA can again become an end, rescue-path conflict with orders, and later lethal escalation remain open |
| E09 | MIK | E01-E09 | flashback confirms conscious participation in killing-talent bargain and private shared-daughter promise; current guilt is self-punitive; initiates contact after harm | fatherhood is genuine transformation from compromised command/promise rather than original innocence | exact confrontation outcome and ability to sever Yoshimatsu remain open |
| E09 | YOS | E01-E09 | heart rescue was conditioned on realizing killing talent; Chisato framed as shared daughter and cultivation as private promise; present proxy harm is audience-known | personal affection and teleological coercion are integrated rather than mutually exclusive | Chisato still lacks direct present attribution; Yoshimatsu response to Majima open |
| E09 | KUR | E01-E09 | scrubbed Alan data leads her to human-source interrogation of Mika for Chisato's sake | repair-oriented intelligence work becomes multi-method rather than purely technical | ability to find a replacement/repair route remains open |


| E10 | CHI | E01-E10 | closes cafe to protect others' time while admitting sadness; learns full killing-purpose bargain; thanks Mika for letting her decide; recognizes two fathers; seeks direct answer from Yoshimatsu; trusts Takina/Fuki with Enkuboku | self-authorship is now explicit meta-principle over compromised origin | hostage outcome, direct Yoshimatsu answer, severe collapse, and E11+ consequences open |
| E10 | TAK | E01-E10 | uses outside-life enjoyment as leverage; applies severe bounded coercion; redirects DA access toward Yoshimatsu/Chisato | DA monopoly over belonging weakens; person-specific rescue objective governs institutional use | open defection/final DA place-value and later lethal choice open |
| E10 | MIK | E01-E10 | admits commander-interest/killing bargain, receives Chisato recognition, then actively supports rescue | guilt moves into truth-telling and operational protection | Yoshimatsu confrontation threshold open |
| E10 | YOS | E01-E10 | confirms stewardship-failure model and willingness to sacrifice own life for Alan ideal | self-objectifying teleology explicit | direct Chisato confrontation open |
| E10 | MAJ | E01-E10 | challenges DA law/legitimacy and Alan hidden influence; broadcasts hidden reality and distributes guns | political critique and coercive exposure coexist | E11 consequences open |
| E10 | KUR | E01-E10 | continues heart-origin/repair investigation through technical and contextual inference | repair/intelligence role persists | repair success open |
| E10 | KUS | E01-E10 | states DA pre-legal/trans-regime legitimacy and epistemic-peace doctrine under higher-command pressure | institutional ideology directly articulated | exposure-crisis limits open |


| E11 | CHI | E01-E11 | enters old tower alone to rescue Yoshimatsu; preserves enemy life while using decisive force; accepts ballistic vulnerability rather than expose Yoshimatsu; visual evasion fails under engineered darkness; rejects Majima moral equivalence | life-preservation and self-authorship survive personally urgent rescue; capability is explicitly conditional rather than mythic | direct Yoshimatsu purpose answer, physiological collapse and E12+ consequences open |
| E11 | TAK | E01-E11 | suspects trap, knowingly forfeits final DA return because DA cannot save Chisato, then enters Chisato/Majima firefight without authorization | institution becomes subordinate to person-specific rescue; outside-life fallback converts exit into survivable choice; severe force remains available | post-defection institutional identity and E12 lethal-choice limits open |
| E11 | FUK | E01-E11 | warns Takina of irreversible DA cost, then says `行けよ` and permits departure | command loyalty now includes costly peer-recognition and judgment | later practical cooperation after defection open |
| E11 | ERI | E01-E11 | directly accepts responsibility, apologizes to Takina and offers operational replacement support | long-running guilt moves into explicit repair behavior | durability/reciprocal Takina response beyond immediate crisis open |
| E11 | KUR | E01-E11 | explicitly remembers LycoReco as enjoyable, voluntarily returns from departure and identifies improved-heart rescue premise | ordinary belonging and technical repair role converge through chosen return | success of heart-rescue contribution open |
| E11 | MIZ | E01-E11 | challenges Kurumi's distancing and participates in voluntary return rather than treating dispersal as final | ordinary-network attachment persists without captivity | later contribution details open |
| E11 | MIK | E01-E11 | accompanies Chisato to old tower, questions solo entry, then permits self-authored departure through `いってきます / いってこい` | protective fatherhood remains autonomy-supportive under lethal risk | direct Yoshimatsu-facing threshold open |
| E11 | MAJ | E01-E11 | engineers embodied public witnesses, exploits DA secrecy and Chisato's visual/relational vulnerabilities, proposes anti-Alan alliance while retaining violent exposure | anti-coercion critique and coercive method remain integrated contradiction; sensory-counterpart role sharpened | E12 continuation/open outcome |
| E11 | YOS | E01-E11 | historical Alan audio explicitly discounts an experimental girl's life against talent realization; present Yoshimatsu is bound/shot yet still treated by Chisato as rescue-worthy | teleology extends to biomedical sacrifice while personhood remains ethically preserved by Chisato | direct answer and heart disposition open |
| E11 | KUS | E01-E11 | DA assault doctrine authorizes total lethal elimination while public Lycoris exposure forces firing restraint | secrecy/force governance now enters direct operational contradiction | restoration/containment strategy open |


| E12 | CHI | E01-E12 | directly rejects Yoshimatsu's killing-as-happiness claim; preserves wounded Yoshimatsu while returning Alan pendant; states survival via killing him would no longer be herself; names Takina among valued consequences of gifted time; reopens LycoReco for Lycoris rescue; directly pressures changed Kusunoki command conditions; returns for Takina-gifted bag | self-authorship now includes explicit identity-continuity boundary on rescue; gratitude and life preservation survive ideological rupture; ordinary/relational goods outrank abstract world-service | exact medical rescue outcome and E13 Majima resolution open |
| E12 | TAK | E01-E12 | treats DA exit as completed; deprioritizes revenge in favor of heart retrieval; becomes willing to kill Yoshimatsu/extract heart for Chisato; explicitly says she does not want Chisato to die; resumes stewardship/repair and dry baseline afterward; final Chisato threat again triggers extreme activation | person-specific Chisato survival becomes overriding outcome under existential stakes, but Chisato's direct refusal remains an effective relational constraint; institutional belonging no longer governs action | whether E13 rebalances survival priority with Chisato's identity boundary open |
| E12 | YOS | E01-E12 | explicitly defines killing/world contribution as Chisato's happiness, treats her as wound-up doll/function, puts improved heart in own body and offers death to force realization | teleology is self-sacrificial rather than merely possessive; own life and Chisato choice are subordinate to talent-purpose | immediate survival/relationship outcome open |
| E12 | KUR | E01-E12 | chosen return yields heart intelligence, helicopter/logistical support, control-room route, Robota defeat/police tip, Radiata takeover/restoration and narrative cover | ordinary belonging and technical capability now operate as integrated crisis solidarity | post-crisis place/identity and E13 contribution open |
| E12 | KUS | E01-E12 | upper command orders Lycoris extermination; Kusunoki secretly requests LycoReco rescue through Mika, then overtly withdraws LilyBell/resumes command after cover shifts conditions | institution is internally differentiated; Kusunoki can selectively subvert upper-command outcome while preserving formal structure | scope/generalizability of selective subversion open |
| E12 | FUK | E01-E12 | abrasive non-return ratification for Takina; breaks standby order; redistributes evacuation/control-room tasks; continues familiar Chisato conflict | command loyalty increasingly includes independent judgment and peer continuity rather than obedience alone | post-crisis institutional consequences open |
| E12 | ERI | E01-E12 | converts apology/guilt into filling Takina's operational place and later explicit reciprocal repair conversation | repair becomes forward responsibility rather than confession only | durable post-crisis friendship state open |
| E12 | MIK | E01-E12 | routes Kusunoki's covert rescue while remaining off on separate unresolved task | protective action is increasing but direct Yoshimatsu-facing threshold remains only partially tested within E12 proper | E13 outcome explicitly withheld |
| E12 | MAJ | E01-E12 | absent from ideological center until final ambush/reappearance | remains active unresolved adversary; E12 adds no new balance doctrine | E13 confrontation/open ideology test |

| E13 | CHI | TV E01-E13 | retains life-preserving target discrimination against Majima; articulates concrete particularist values and memory-after-death legacy; survives via replacement heart without accepting assigned vocation; discards Alan token; disappears to avoid somber farewell; resumes future play/helping and selectively refuses DA work | self-authorship, mortality, gratitude and ordinary life converge into open-future particularism; autonomy retains an avoidant/paternalistic modifier | shorts must test settled low-stakes baseline; legal Hawaii travel mechanism remains unexplained |
| E13 | TAK | TV E01-E13 | negotiates task division with Fuki; re-enters Chisato crisis without DA; rescues Chisato; uses civilian information to find runaway Chisato; offers controlled reassurance and future-restoration advice; retains high-energy safe banter | competence is no longer institution-owned or merely unilateral: it serves negotiated responsibility, person-specific care and coauthored future | shorts must test mundane initiative/care without crisis amplification |
| E13 | MIK | TV E01-E13 | directly confronts Yoshimatsu for Chisato, states children should lead adults and their choices must not be obstructed; later conceals exact death/heart history and keeps cane secret | fatherhood completes protective severance from assigned-purpose project but remains paternalistically secretive and morally compromised | exact lethal mechanics remain off-screen; shorts may test everyday fatherhood/secrecy |
| E13 | MAJ | TV E01-E13 | restates balance doctrine, seeks authentic Chisato contest, survives, remains independent counterforce amid loose guns | accurate institutional critique remains fused to self-authorized coercive method; moral self-conception is not exculpation | post-TV political trajectory open |

| SHORT01 | TAK | TV E01-E13 + Short01 | independently runs supply logistics, proposes repeated profitable civilian events and yakitori expansion, while carrying substantial concealed armament in the same ordinary setting | TV endpoint is validated in mundane form: competence acquires civilian/commercial objects without operational identity disappearing | later shorts must test breadth beyond commerce and weapon-readiness context |
| SHORT01 | CHI | TV E01-E13 + Short01 | works seasonal service, recognizes Takina's initiative, and challenges armed over-read of mundane context through playful physical correction rather than devaluing competence | role/context boundary remains active in ordinary life | broader low-stakes invitation/refusal tests remain open |
| SHORT01 | MIK/MIZ/KUR | TV E01-E13 + Short01 | food/cafe regulation, drinking/karaoke and heckling respectively operate as ordinary social roles | ensemble membership continues to exceed security/technical utility | technical/operational dual-role recurrence remains for later shorts |

# 7. Candidate-policy staging

| Policy ID | Character | Condition | Candidate response | Support | Counterevidence / untested modifier | State |
|---|---|---|---|---|---|---|
| `CHI-SOC-INIT-01` | CHI | socially safe new/weakly familiar person | rapidly personalize, reduce formality, assign shared role/activity, ask direct questions | E01 Takina/kindergarten/café; E02 food invitation/Kurumi naming; E03 repeated board-game invitation | severe distress now routes through `CHI-VULN-AFFIRM-01` rather than play alone | `CANDIDATE_POLICY` |
| `CHI-HLP-LOCAL-01` | CHI | concrete person in trouble below DA threshold | treat as legitimate work and mobilize local resources | E01 community circuit/Saori; E02 shows resulting photo correcting DA timeline | resource/conflict limits unknown | `CANDIDATE_POLICY` |
| `CHI-LIFE-01` | CHI | adversary can be stopped without necessary killing / wounded enemy after combat | nonlethal force, preserve/treat life even under operational cost; treat current enemyhood as contingent | E01 fight/treatment/Cleaner; E02 first aid/contingent enemyhood; E04 time rationale; E05 revenge-pressure refusal; E06 nonlethal fire under severe attack; E09 refuses revenge after Himegama apparently reduces her life to two months; E11 saves Yoshimatsu under fire; E12 treats wounded Yoshimatsu and blocks Takina from killing him | catastrophic third-party tradeoff threshold remains open; personal medical origin is separate from policy validity | `CANDIDATE_POLICY` |
| `CHI-CONFRONT-01` | CHI | partner faces blame/shame around consequential action/failure | lower blame threat, ask/reframe cause, separate person from failure | E01 transfer conversation; E02 immediate `たきなのせいじゃない` after apology | severe betrayal/intentional harm untested | `CANDIDATE_POLICY` |
| `CHI-PLAY-01` | CHI | low-stakes social interaction | tease/probe, exaggerate role framing, direct playful invitation, reward reciprocal pushback | E01 coffee/tower; E02 `たきな様`/food; E03 board-game invitation and Fuki banter | severe identity distress is a demonstrated modifier: direct affirmation replaces teasing as primary tactic | `CANDIDATE_POLICY` |
| `CHI-SUPPORT-01` | CHI | other person states important goal different from Chisato's path | support that goal without demanding ideological convergence | E01 offers DA-return help; E03 directly advocates return to Kusunoki and later preserves return as valid option after offering cafe trial | no test yet where other person's goal directly threatens Chisato | `CANDIDATE_POLICY` |
| `TAK-OPS-RISK-01` | TAK | urgent objective + confidence in tactical model/precision | accept high third-party risk without prior relational negotiation; justify by expected outcome/competence | E01 Erika + Saori; E03 fires through Chisato's line because she predicts Chisato will dodge | whether closeness/consent later modifies this rule remains open | `CANDIDATE_POLICY` |
| `TAK-INST-01` | TAK | assignment/opportunity/institutional access | evaluate through DA standing, legitimacy, usefulness, and return | E01-E02 return orientation; E03 conditions leisure on DA return, seeks commander, formally argues for reinstatement; E07 explicitly offers to return to DA/training after E06 cohabitation | survives explicit replacement/rejection at least through E03; later self-revision remains open | `CANDIDATE_POLICY` |
| `TAK-SOC-FORM-01` | TAK | unfamiliar people/new work or operational briefing | polite/formal, fact-focused, professionally framed presentation; controlled acoustic baseline | E01 café/Saori; E02 route briefing and travel logistics | safe social participation can coexist without erasing baseline | `CANDIDATE_POLICY` |
| `TAK-CLARIFY-01` | TAK | system/norm lacks explicit logic | ask direct clarifying question rather than simulate understanding | LycoReco function; enemy-life question | breadth untested | `CANDIDATE_POLICY` |
| `TAK-TEASE-EMERG-01` | TAK | safe shared semantic frame | concise literal/semantic correction or jab, generally without Chisato-like expansion | E01 tower; E02 `映画の見過ぎですね`, hacker/mascot corrections; `E02-AUD-003` | breadth across relationships untested | `CANDIDATE_POLICY` |
| `TAK-CARE-01` | TAK | teammate in imminent danger | care can override command; intervention remains operationally framed | E01 Erika crisis; E08-E09 Chisato safety protocol -> armed search/intervention | breadth is now supported across teammate and central-partner threat; exact command-conflict limit remains open | `CANDIDATE_POLICY` |
| `CHI-CALIBRATE-01` | CHI | partner is better suited to a concrete task | state own limitation and delegate task ownership without status competition | E02 hacked-car precision shot | only one diagnostic task | `CANDIDATE_POLICY` |
| `TAK-MISSION-COORD-01` | TAK | protection mission is endangered by partner deviation | prioritize extraction/team coordination and argue causal mission consequence explicitly | E02 wounded-enemy stop + later ethical dispute | whether she yields under other moral conflicts open | `CANDIDATE_POLICY` |
| `TAK-FAIL-ACCOUNT-01` | TAK | she perceives consequential loss/failure with potentially distributed causality | preserve authorship of her own choice rather than displace blame; with better causal information, distinguish external contribution from own action and assign forward repair | E02 apparent Walnut death; E03 `全部 自分のせい`; E06 Kurumi confession -> `私の行動の結果` + continued repair obligation | early state can over-attribute when institutional causality is hidden; behavior under intentional betrayal remains open | `CANDIDATE_POLICY` |
| `CHI-VULN-AFFIRM-01` | CHI | close other person exposes severe identity/belonging distress | suspend teasing as primary tactic; validate autonomous motive, make person-specific affirmation, widen available futures, and return final choice | E03 Takina atrium support/embrace/cafe-trial/DA-option sequence | only one severe-vulnerability case; rejection response open | `CANDIDATE_POLICY` |
| `CHI-INST-CHALLENGE-01` | CHI | institutional causal account or information boundary conflicts with observed need/evidence | challenge/circumvent selectively while retaining useful institutional cooperation rather than adopting binary loyalty/opposition | E03 Kusunoki/Radiata confrontation; E06 formal DA secrecy -> Chisato-sanctioned Kurumi circumvention; E07 accepts Fuki/LycoReco information exchange while criticizing cover-after-failure | legal/relational cost limits and response to direct institutional coercion remain open | `CANDIDATE_POLICY` |
| `TAK-RECIP-CLOSURE-01` | TAK | bounded low-stakes conflict with personally meaningful prior injury | permit symbolic interpersonal reciprocity/closure to outrank tactical efficiency | E03 punches Fuki instead of taking easy rear shot; `これで おあいこですね` | real-mission applicability should not be inferred | `CANDIDATE_POLICY` |
| `TAK-ORD-TRY-01` | TAK | ordinary-life option is available after belonging disruption without requiring irreversible commitment | test/participate in concrete ordinary activity while leaving larger identity decision open | E03 ending board-game participation after initial refusal | independent preference generation beyond offered activities remains open | `CANDIDATE_POLICY` |

| `CHI-SELF-AUTH-01` | CHI | institutional/donor role conflicts with a personally chosen high-value end | treat personal desire/meaning as legitimate grounds to exit, redirect, or redefine role rather than allowing assigned function or rescue debt to totalize life | E03 `したいこと 最優先`; E04 benefactor search; E05 rejection of donor ownership; E07 gifted-time helping formulation; E09 rejects Kusunoki role ownership and reveals childhood `救世主`/helping-gun reinterpretation; E10 compromised-origin ownership rejection; E12 direct Yoshimatsu confrontation/pendant return/identity-continuity refusal | response to direct benefactor coercion now demonstrated; other constitutive-conflict boundaries remain open | `CANDIDATE_POLICY` |
| `CHI-TIME-01` | CHI | another person's future time or a finite ordinary opportunity is at stake | treat lived time/opportunity as intrinsically valuable; avoid irreversible deprivation while accepting bounded costs or painful nonlethal force | E04 finite-meal / `誰かの時間を奪う`; E05 terminal-client experience support; E09 two-month prognosis + `受け入れて 全力！` + imperfect outing treated as successful lived time | mortality is strongly relevant context, but E09 directly shows a separate savior/helping origin for nonlethality; sole-cause formulation rejected | `CANDIDATE_POLICY` |
| `CHI-ROLE-BOUND-01` | CHI | off duty/out of uniform with civil response already present | treat Lycoris authority as context-bounded rather than continuous self-authorization; defer intervention unless a stronger modifier emerges | E04 aquarium identity line + station wrist interception / legal warning | emergency override threshold remains open | `CANDIDATE_POLICY` |
| `TAK-PREF-GEN-01` | TAK | ordinary-life choice lacks explicit institutional rule | begin with specification/function; use trusted delegation or concrete comparison; increasingly produce explicit personal preference | E04 clothing/underwear process + karinto preference | stable fashion/aesthetic taste remains open | `CANDIDATE_POLICY` |
| `TAK-PERS-INQ-01` | TAK | relational safety and unresolved partner/body information create information gap | initiate direct personal questions and evidence-seeking; persist through playful deflection; when a concrete boundary is supplied, potentially reroute rather than abandon the inquiry | E04 aquarium inquiry + positive evaluation; E05 artificial-heart verification and later boundary-compliant reattempt | generalization to stronger refusal/private topics remains open | `CANDIDATE_POLICY` |
| `YOS-TALENT-TELOS-01` | YOS | exceptional aptitude is identified | treat talent as a gift carrying objective obligation to be realized/delivered, subordinating preference where necessary | E04 divine-gift / killing-genius doctrine + E05 Alan-purpose pressure/staged test + E07 explicit `才能とは神の所有物だ` / Alan-child `役割`; use teleological stewardship, not crude personal ownership | limits/source of claimed authority and exact orchestration chain remain open | `CANDIDATE_POLICY` |
| `MAJ-BALANCE-01` | MAJ | hidden/sanitized power suppresses visible disruption or creates an imbalance he recognizes | act as self-authorized counterforce; scale conflict toward hidden order and select sufficiently strong opponents as balancing counterparts | E04 lie/balance declaration; E05 first Lycoris killing; E06 `ＤＡ...ぶっ潰す`, 26-comrade ledger, and Chisato as personal counterweight | exact proportionality rule, civilian limits, and persistence of personalized interest remain open | `CANDIDATE_POLICY` |


| `CHI-GIFT-RECIP-01` | CHI | receives life-changing aid whose giver/patron claims authority over its meaning | preserve gratitude/value of the gift while translating it into self-authored reciprocal helping rather than obedience to assigned purpose | E05 `これをくれた人みたいにね` paired with explicit refusal to kill under Alan-purpose pressure | response after recognizing actual giver/intent remains open | `CANDIDATE_POLICY` |
| `CHI-DECEPTION-AFFECT-01` | CHI | a personally meaningful interaction is exposed as staged/deceptive | register disappointment but remain capable of accepting narrower independently supported meaning rather than globalizing all associated content as false | E05 `ぜ～んぶ ウソか` -> accepts Takina's narrow guide-performance repair with `ありがとう` | repetition and higher-betrayal stakes open | `CANDIDATE_POLICY` |
| `TAK-BOUND-LEARN-01` | TAK | unfamiliar privacy/social norm blocks an information-seeking goal | respond to explicit concrete boundary by retaining the rule and rerouting the underlying goal into an allowed condition rather than necessarily abandoning it | E05 public heart-touch boundary -> private `今は ほかの人いませんよ` reattempt | response to categorical refusal rather than conditional boundary open | `CANDIDATE_POLICY` |
| `TAK-PROTECT-INIT-01` | TAK | concrete protection threat emerges and team roles are not fully preassigned | self-initiate protective structure, contact, or rescue; separate engagement from evacuation and issue concise coordination directions | E05 volunteers against Jin and directs evacuation; E06 independently proposes 24h pairing/sleep shifts and later mobilizes urgently to rescue Chisato | behavior when Chisato explicitly rejects protection or when objectives conflict remains open | `CANDIDATE_POLICY` |
| `TAK-EVID-PART-01` | TAK | broad premise/source is exposed as deceptive but local claims remain independently assessable | partition evidence and preserve narrower claims that remain supported instead of invalidating the entire experiential field | E05 fake-client reveal -> `いいガイドだったのは ウソじゃないと思います` | generalization beyond relational reassurance open | `CANDIDATE_POLICY` |
| `YOS-PROXY-COERCE-01` | YOS | direct ideology has not produced desired Chisato behavior or would expose coercion | use intermediaries, staged conditions, information asymmetry, or third parties to induce movement toward assigned killing purpose | E05 fake-client test/control chain; E06 explicit additional boss-directed request relayed through Himegama to Robota and engineered Majima interest | exact knowledge/motive distribution across intermediaries remains open | `CANDIDATE_POLICY` |

| `TAK-SYSTEM-ADAPT-01` | TAK | recurring low-stakes procedure/system disadvantages her and the mechanism becomes legible | analyze causal structure and alter procedure/rules rather than merely repeat failure or abandon participation | E06 household janken: learns Chisato's movement-reading mechanism, removes standard opening, wins final cohabitation wager | recurrence outside play/low stakes untested | `CANDIDATE_POLICY` |
| `CHI-DODGE-VIS-01` | CHI | incoming attack supplies visible preparatory/body/line cues | use exceptional visual prediction to evade; degraded sight/lighting/multi-angle conditions reduce advantage | E06 Majima fight + `千束の弱点は目ですね`; E11 old-tower darkness explicitly exploited by Majima while he functions through hearing | exact threshold and interaction with nonvisual partner compensation remain open | `CANDIDATE_POLICY` |
| `TAK-FORCE-DISCRIM-01` | TAK | precision rescue solution is available without area suppression | exploit accuracy for disabling/nonvital constraint when it serves rescue, without requiring Chisato's ammunition method | E06 rescue shot followed by attacker `脚が！`; consistent with E04 skill-redirection proposal | one strong instance; intent and generality remain bounded | `CANDIDATE_POLICY` |

| `TAK-INDEP-OBLIG-01` | TAK | optional group leisure conflicts with a self-chosen civilian obligation | decline participation directly and preserve the independent obligation without needing institutional justification | E07 Japanese-school work refusal | conflict with urgent partner need untested | `CANDIDATE_POLICY` |
| `TAK-PRIVACY-YIELD-01` | TAK | close partner enters a clearly personal one-to-one encounter | recognize the privacy need and voluntarily leave space rather than treating closeness as entitlement to remain | E07 Chisato/Yoshimatsu recognition | only one diagnostic case | `CANDIDATE_POLICY` |
| `TAK-LETHAL-NORM-01` | TAK | abstract/fictional frame asks whether clearly bad actors should be killed | endorse killing without Chisato's universal anti-killing rule | E07 manga `悪人は殺すべきかな？` -> `べきですね` | real-world thresholds, surrender, partner stakes, and later development open | `CANDIDATE_POLICY` |
| `CHI-PROMISE-REPAIR-01` | CHI | trusted caregiver's past concealment is explained as a life-saving promise and does not presently remove her choice | model motive/context, accept the fulfilled promise, and rapidly restore ordinary relation without denying the concealment occurred | E07 Mika reveal/repair | new secrecy constraining current agency remains an explicit open modifier | `CANDIDATE_POLICY` |
| `MIKA-CHI-FREEDOM-01` | MIK | Yoshimatsu/Alan teleology threatens Chisato's self-authored life | oppose the imposed purpose and demand Chisato's freedom | E07 gun confrontation | action under irreversible choice/cost open | `CANDIDATE_POLICY` |
| `MIKA-YOSHI-CONSTRAINT-01` | MIK | opposition to Yoshimatsu would require directly harming/severing him | moral/parental opposition can exceed Mika's present ability to execute lethal severance | E07 `覚悟なんか あるわけないだろ` | later development must not be back-projected | `CANDIDATE_POLICY` |

| `TAK-INST-MAINT-01` | TAK | person/place/system she has accepted practical responsibility for is at risk | audit causal structure and change procedures across domains until system becomes viable | E08 café accounting, ammunition/cleanup, menu, automation/investment | overcontrol/burnout thresholds and transfer to unwanted institutions open | `CANDIDATE_POLICY` |
| `TAK-ORD-CREATE-01` | TAK | civilian objective has no fixed assignment procedure | originate solution, observe social outcome, revise when ignored criterion becomes legible | E08 new parfait then withdrawal/revision | breadth beyond café/teaching open | `CANDIDATE_POLICY` |
| `TAK-CARE-ADMIN-01` | TAK | close person has foreseeable maintenance/safety need | express care through scheduling, monitoring, rules, logistics and follow-through | E08 checkup, three-ring rule, relocation, café maintenance | response when rules are rejected or autonomy conflict intensifies open | `CANDIDATE_POLICY` |
| `TAK-THREAT-PROTOCOL-01` | TAK | concrete threat exposes communication/location vulnerability | create explicit escalation rule and physically intervene when routine breaks | E08 three-ring/one-ring protocol and clinic response | false alarms/extended uncertainty open | `CANDIDATE_POLICY` |
| `TAK-PLACE-FOR-OTHER-01` | TAK | close person's valued place is materially endangered | invest heavily to preserve it because it matters to that person before requiring own belonging label | E08 `大切な場所なんでしょ？` | whether/when place becomes Takina's own declared home open | `CANDIDATE_POLICY` |
| `CHI-CARE-TRANSLATE-01` | CHI | close partner provides practical/procedural care | translate act into personal presence, domestic meaning, invitation, or explicit gratitude | E08 `どこにいても来てくれる`, `同棲`, `ありがと` | whether translation can misread unwanted obligation open | `CANDIDATE_POLICY` |
| `CHI-BODY-CONTROL-01` | CHI | bodily intervention is unavoidable/non-evadable | show disproportionate aversion/control distress compared with threats she can perceive and dodge | E08 injection explanation + clinic attack | sedation/medical-emergency variants open; artificial-heart causation not established | `CANDIDATE_POLICY` |
| `CHI-BENEFACTOR-DEFEND-01` | CHI | indirect evidence threatens foundational benefactor meaning while trusted alternative remains available | initially defend value/interpretation of benefactor rather than instantly invert relationship | E08 Majima accusation + Mika reassurance | direct incontrovertible betrayal evidence untested | `CANDIDATE_POLICY` |
| `YOS-TRUST-BYPASS-01` | YOS | direct purpose demand risks Chisato refusal | use trusted third-party routine/access and constrained bodily conditions to bypass ordinary choice | E08 Himegama medical infiltration | exact escalation ceiling/open willingness to kill open | `CANDIDATE_POLICY` |
| `MAJ-RIVAL-SOCIAL-01` | MAJ | selected counterweight is temporarily available outside immediate battle | permit ordinary-interest exchange while testing ideological category and retaining antagonism | E08 apartment movies/drinks/mission talk | generality to others and safety limits open | `CANDIDATE_POLICY` |

| `CHI-IRREV-01` | CHI | severe irreversible loss has already occurred | reject retaliatory killing when it cannot causally restore the lost future; redirect toward remaining actionable life | E09 Himegama heart sabotage + `あいつを殺したとこで 変わんないよ` | response when killing could prevent additional imminent victims remains open | `CANDIDATE_POLICY` |
| `CHI-UNCTRL-01` | CHI | an important constraint is genuinely outside present control | accept the uncontrollable condition rather than ruminate as primary response, then invest effort in remaining actionable experience/work | E09 two-month prognosis + `受け入れて 全力！` | can become over-control of others' grief; severe physical deterioration open | `CANDIDATE_POLICY` |
| `CHI-GIFT-INTERP-01` | CHI | a life-saving gift arrives with ambiguous or imposed purpose | preserve gratitude/value of rescue while authoring the gift toward helping rather than donor-intended role | E09 child `私もなる 救世主！` + `人を助ける銃だね`; E07 gifted-time helping formulation | response after direct present proof of donor betrayal remains open | `CANDIDATE_POLICY` |
| `TAK-INST-INSTRUMENT-01` | TAK | institutional access can materially advance a higher-priority person-specific objective | use/re-enter institution as infrastructure while subordinating prestige/belonging value to concrete rescue objective | E09 had intended to refuse DA return, then chooses it because Majima operation may help Chisato live | durability after re-entry and conflict with DA orders remain open | `CANDIDATE_POLICY` |
| `TAK-REL-ACCOUNT-01` | TAK | a difficult self-chosen role transition materially affects a close relationship | communicate the decision personally and own its relational consequence rather than outsource disclosure to authority/third party | E09 refuses Mika's offer to tell Chisato and asks for time to do it herself | behavior under direct rejection/anger remains open | `CANDIDATE_POLICY` |


| `CHI-ORIGIN-AUTHOR-01` | CHI | formative opportunity/relationship began in instrumental purpose | distinguish compromised origin from meaning of life actually authored | E10 confession + explicit thanks for decision-space + ownership of work/cafe choices | direct Yoshimatsu confrontation open | `CANDIDATE_POLICY` |
| `CHI-GRATITUDE-NONOWN-01` | CHI | benefactor/parent supplied indispensable good but claims assigned purpose | preserve gratitude without granting ownership over vocation/future | E05, E09, E10 | further betrayal/harm open | `CANDIDATE_POLICY` |
| `CHI-RECOGNITION-SEEK-01` | CHI | severe identity/origin vulnerability with trusted parent | directly ask whether present self is accepted | E10 proud-daughter exchange | one parental case | `CANDIDATE_POLICY` |
| `CHI-DISTRIBUTE-HERO-01` | CHI | macro mission and person-specific rescue compete while peers can cover one branch | entrust competent peers with public task rather than assume sole-hero responsibility | E10 Enkuboku/Takina-Fuki trust | outcome open | `CANDIDATE_POLICY` |
| `CHI-TIME-OTHER-01` | CHI | own mortality risks consuming friends' future time | reduce claims on others' time/permit dispersal while preserving care | E10 cafe closure/dispersal | may overcorrect by deciding shared institution unilaterally | `CANDIDATE_POLICY` |
| `TAK-DA-INSTRUMENT-01` | TAK | DA access can serve person-specific high-value objective | use institutional information/mobility/authority as means | E09 return-for-Chisato + E10 interrogation/Yoshimatsu focus | direct order conflict not yet tested | `CANDIDATE_POLICY` |
| `TAK-OUTSIDE-FALLBACK-01` | TAK | DA threatens status after meaningful civilian experience | treat outside life as credible fallback | E10 outside-life enjoyment / tolerable firing | final DA belonging open | `CANDIDATE_POLICY` |
| `TAK-COERCIVE-CONTROL-01` | TAK | urgent intelligence objective + controlled captive | severe bounded physical coercion without evidence lethality is required | E10 interrogation | other contexts/limits untested | `CANDIDATE_POLICY` |
| `MIKA-TRUTH-BREAK-01` | MIK | concealment about Chisato origin conflicts with impending death/agency | disclose compromised history despite relational risk | E10 confession | broader secrecy policy mixed | `CANDIDATE_POLICY` |
| `MIKA-PROTECT-ACT-01` | MIK | direct threat after truth disclosure | move from guilt/concealment toward material operational support | E10 rescue mobilization | lethal severance untested | `CANDIDATE_POLICY` |

| `TAK-INST-EXIT-01` | TAK | high-value institution blocks or cannot serve a person-specific rescue and credible outside life exists | accept loss of institutional standing and redirect action toward rescue without waiting for authorization | E11 `分かってます` + `ここでは千束を救えない それだけです`; continuation of E09-E10 DA instrumentalization/outside fallback | later regret/reintegration and other-person generality open | `CANDIDATE_POLICY` |
| `TAK-THREAT-INFER-01` | TAK | personally important rescue solution appears unusually convenient under active adversarial manipulation | test adversarial incentives and suspect trap rather than accept desired reassurance at face value | E11 `嫌な予感がします 罠かもしれない` / `絶対 何かある` | one high-stakes case | `CANDIDATE_POLICY` |
| `CHI-ANTI-EQUIV-01` | CHI | adversary shares one autonomy/anti-coercion premise but violates personhood/life constraints | reject alliance or moral sameness while preserving the factual common premise | E11 Majima recruitment + `一緒にすんな！` | behavior under temporary tactical necessity open | `CANDIDATE_POLICY` |
| `FUK-COSTLY-PERMISSION-01` | FUK | peer's autonomous choice conflicts with institutional duty but motive is legible | state real institutional cost, verify understanding, then permit action rather than use command as total veto | E11 warning + `行けよ` | one high-cost case | `CANDIDATE_POLICY` |
| `ERI-DIRECT-REPAIR-01` | ERI | prior guilt becomes actionable in a safe enough direct encounter | name responsibility, apologize explicitly and offer practical support | E11 `全部 私のせいよ` + apology + replacement offer | long-term dyad response open | `CANDIDATE_POLICY` |
| `KUR-CHOSEN-RETURN-01` | KUR | ordinary network has permitted genuine exit but faces acute person-specific need | voluntarily re-enter with concrete information/technical contribution rather than treat belonging as compulsory residence | E11 airport reflection/return + improved-heart discovery | later repeated exit/return pattern open | `CANDIDATE_POLICY` |

| `CHI-IDENTITY-CONTINUITY-01` | CHI | survival is offered only through an act she understands as constitutively violating her authored moral identity | reject biological continuation under that specific causal condition while continuing to seek life/action through non-self-betraying routes | E12 `ヨシさんを殺して生きても それは もう私じゃない`; later `それは今日じゃない` blocks passive-death reading | one extreme Yoshimatsu case; do not generalize to ordinary compromise | `CANDIDATE_POLICY` |
| `TAK-CHI-SURVIVAL-PRIORITY-01` | TAK | Chisato faces credible existential threat and a concrete rescue lever exists | prioritize Chisato's biological survival over punishment, status and potentially Chisato's preferred lethal boundary; escalate force if necessary | E12 discards blame, attempts Yoshimatsu killing/heart extraction, `心臓が逃げる`, explicit refusal of Chisato death | relationship-specific extreme condition; Chisato's direct restraint eventually stops action | `CANDIDATE_POLICY` |
| `KUS-SELECTIVE-SUBVERSION-01` | KUS | upper-command secrecy policy threatens Lycoris survival and overt opposition is initially constrained | route rescue through deniable/external actors, then resume overt command when information/authority conditions permit | E12 covert request through Mika + later LilyBell withdrawal/direct Fuki command | one crisis; generality beyond Lycoris-protection context open | `CANDIDATE_POLICY` |

# 8. Meaningful negative-evidence register

| ID | Scope | Character | Opportunity | Expected under oversimplified rule | Observed non-action / contrary action | Effect |
|---|---|---|---|---|---|---|
| `NEG-E01-CHI-001` | E01 | CHI | Takina defends Lycoris necessity / wants DA return | generic anti-DA dissident would condemn institution or redirect goal | Chisato lightly acknowledges defense and offers to help Takina return | excludes simple anti-DA model |
| `NEG-E01-CHI-002` | E01 | CHI | armed hostile encounter | ordinary pacifist/no-harm model predicts refusal of violence | Chisato uses armed force and incapacitates enemies nonlethally | constrains label to nonlethality/life preservation |
| `NEG-E01-CHI-003` | E01 | CHI | first meeting with reserved/formal Takina | perfectly boundary-respecting social model predicts waiting for reciprocal permission | Chisato removes honorific distance and rapidly assigns intimacy/roles | establishes boundary-forward tendency |
| `NEG-E01-TAK-001` | E01 | TAK | Erika hostage crisis | emotionless model predicts indifference to teammate danger | Takina disobeys specifically to stop imminent killing | rejects emotional-emptiness model |
| `NEG-E01-TAK-002` | E01 | TAK | old-tower conversation | socially incapable/literal-only model predicts no play | Takina makes semantic jab; Chisato recognizes it | preserves humor capacity |
| `NEG-E01-TAK-003` | E01 | TAK | end-of-episode café participation | instant-conversion model predicts LycoReco chosen over DA | Takina's enthusiastic work commitment is explicitly tied to DA-return opportunity | chosen belonging remains open |
| `NEG-E01-TAK-004` | E01 | TAK | comparison across formal, rational, teasing, and goal-activated speech | globally flat/low-activation model predicts little state-linked acoustic expansion | closing `やります！` shows materially greater activation than several earlier constrained samples | rejects invariant-flatness voice rule; supports state-conditioned elasticity |

| `NEG-E02-TAK-001` | E02 | TAK | low-stakes train intimacy/social invitation | personality-replacement model predicts broad Chisato-like vocal expansion | Takina voluntarily accepts direct feeding and enjoys food while remaining acoustically controlled | supports additive social development |
| `NEG-E02-CHI-001` | E02 | CHI | difficult precision task during active threat | status-competitive prodigy model predicts taking/contesting the shot | Chisato explicitly admits low confidence and delegates to Takina | supports calibrated competence rather than ego defense |
| `NEG-E02-CHI-002` | E02 | CHI | treating enemy risks mission coordination | consequence-free saint model predicts no meaningful cost | visual evidence shows partner/client extraction separation and Takina correctly identifies exposure | preserves real cost inside `CHI-LIFE-01` |
| `NEG-E02-TAK-002` | E02 | TAK | apparent client death after contentious operation | emotionally indifferent operator model predicts detached reporting or blame displacement | Takina immediately reports failure, later apologizes, and shows acoustic contraction | rejects emotional-emptiness/zero-accountability model |
| `NEG-E03-TAK-001` | E03 | TAK | ordinary cafe life is available while DA return becomes actionable | instant-conversion model predicts DA goal has already been replaced | Takina conditions leisure on whether it helps DA return and actively seeks reinstatement | preserves DA-return desire through E03 |
| `NEG-E03-TAK-002` | E03 | TAK | severe institutional rejection | globally flat/emotionless model predicts little state-linked performance change | syntax fractures; self-blame becomes acoustically quiet/constricted; injustice and mock battle produce large activation expansion | strongly rejects invariant-flatness/emotional-emptiness model |
| `NEG-E03-CHI-001` | E03 | CHI | Takina desperately wants DA | possessive/exclusive-belonging model predicts Chisato should redirect or demand LycoReco choice | Chisato advocates reinstatement, then explicitly says Takina may return later if she still wants it | supports influence without ownership |
| `NEG-E03-TAK-003` | E03 | TAK | bounded mock battle offers easy tactical rear shot | pure-efficiency model predicts taking the highest-value scoring action | Takina instead closes personal ledger with a punch and `おあいこ` | establishes noninstrumental reciprocity in low-stakes frame |

| `NEG-E04-TAK-001` | E04 | TAK | repeated civilian choice opportunities | no-preferences model predicts inability to state a personal like | Takina explicitly likes karinto, evaluates what suits her, and calls Chisato cute | rejects preference-absence; supports missing-procedure model |
| `NEG-E04-TAK-002` | E04 | TAK | growing leisure/social freedom | personality-replacement model predicts Chisato-like baseline expansion | function-first reasoning and controlled acoustic preference statements persist alongside inquiry/laughter peaks | supports additive self-authorship |
| `NEG-E04-CHI-001` | E04 | CHI | asked directly why she does not kill | generic pacifist model predicts aversion to harmful force | Chisato explicitly endorses painful nonlethal incapacitation and partly frames it as retaliatory | constrains `CHI-LIFE-01` to life/time preservation, not no-harm |
| `NEG-E04-CHI-002` | E04 | CHI | subway emergency encountered while armed/capable | always-on-duty hero model predicts reflexive intervention | Chisato stops Takina, invokes off-duty/uniform/legal boundary, and leaves the incident to active responders | supports context-bounded role identity |
| `NEG-E04-YOS-001` | E04 | YOS | Alan support could be framed as neutral enablement | neutral-patron model predicts recipient choice governs talent use | Yoshimatsu says gifted talent must be delivered and specifically names killing aptitude | excludes value-neutral support model |
| `NEG-E04-MAJ-001` | E04 | MAJ | large-scale violence and aftermath | random-thrill model predicts weak relation to political information state | Majima explicitly names sanitized lie/balance and escalates because his attack was concealed | establishes ideological/information-sensitive violence |


| `NEG-E05-CHI-001` | E05 | CHI | terminal client requests revenge execution under active assassin threat | generic pacifist model predicts no violent force | Chisato forcefully incapacitates Jin but refuses killing | reinforces life/time preservation, not no-harm |
| `NEG-E05-CHI-002` | E05 | CHI | Alan life-gift is invoked as a debt requiring killing | gratitude-as-obedience model predicts compliance or moral deference | Chisato preserves gratitude but explicitly authors helping rather than killing | separates gift value from donor ownership |
| `NEG-E05-TAK-001` | E05 | TAK | socially rich outing becomes live protection crisis | softening/personality-replacement model predicts diminished independent operational initiative | Takina volunteers threat contact and directs evacuation | ordinary expansion coexists with tactical agency |
| `NEG-E05-TAK-002` | E05 | TAK | Chisato explicitly blocks public bodily verification | invariant boundary-blindness predicts repeated violation/ignoring condition | Takina remembers and reattempts only in private after naming the condition | supports concrete boundary learning |
| `NEG-E05-INST-001` | E05 | institutional | police uncover bullet evidence contradicting accident story | coverup model based only on ignorant civilians predicts discovery automatically breaks narrative | informed Abe recognizes falsification/orders and conditionally accepts secrecy | requires mixed ignorance + informed compliance model |
| `NEG-E05-ALAN-001` | E05 | YOS/Alan | Alan support could remain benevolent patronage | neutral-enable model predicts no coercive behavioral engineering | Alan-purpose demand and strongly inferred staged fake-client test pressure Chisato toward killing | excludes philanthropy-only model |

| `NEG-E06-CHI-001` | E06 | CHI | Majima creates visually hostile combat conditions and seriously injures Chisato | invulnerability model predicts ordinary evasion remains sufficient regardless of information conditions | unusual injury plus explicit `弱点は目` and visually degraded fight conditions | rejects invariant-invulnerability model; bounds `CHI-DODGE-VIS-01` |
| `NEG-E06-TAK-001` | E06 | TAK | temporary cohabitation creates real domestic familiarity and Chisato asks to continue | dependency/permanent-fusion model predicts Takina will simply accept indefinite continuation | Takina conditions continuation on janken, changes the rule after learning mechanism, wins, and exits the wager on her own terms | preserves domestic/yuri coding while rejecting automatic permanence/dependency |
| `NEG-E06-TAK-002` | E06 | TAK | compare threat/confrontation and safe-play acoustic peaks | high-F0/intensity-as-negative-affect model predicts the largest activation should be threat/distress-specific | final safe janken victory reaches extremely high short-window activation comparable to/exceeding threat samples | Layer-B activation is not affective valence; Layer C remains required |
| `NEG-E06-KUR-001` | E06 | KUR/TAK | Kurumi's hack contributed causally to leak/transfer, while Takina made the firing decision | all-blame model predicts Kurumi owns outcome; no-blame model predicts involvement is irrelevant | Takina rejects scapegoating but requires Kurumi's repair cooperation | supports differentiated causal responsibility rather than binary blame |

| `NEG-E07-TAK-001` | E07 | TAK | E06 domestic closeness is followed by staffing/DA discussion | fusion model predicts Takina no longer treats institutional exit as viable | Takina offers `じゃ 私が戻りますよ` and notes training-school return | preserves exit/nonexclusive agency |
| `NEG-E07-CHI-001` | E07 | CHI | benefactor identity is finally known | rescue-debt model predicts purpose surrender | Chisato thanks Yoshimatsu while interpreting gifted time as helping others | strengthens gift-without-debt self-authorship |
| `NEG-E07-YOS-001` | E07 | YOS | talent ownership is discussed explicitly | personal-possession model predicts Yoshimatsu says Chisato/talent belongs to him | he says talent belongs to God, not the person or patrons | replace crude ownership with teleological stewardship/divine-property coercion |
| `NEG-E07-MIKA-001` | E07 | MIK | Mika points a gun and claims trigger resolve | threat-equivalence model predicts actual willingness to kill Yoshimatsu | Mika explicitly admits `覚悟なんか あるわけないだろ` | preserves opposition while rejecting current lethal-severance inference |
| `NEG-E07-REL-001` | E07 | CHI/TAK | partnership is domestically and emotionally closer | convergence model predicts shared lethal ethic | Takina says bad people should be killed; Chisato immediately says killing is wrong | closeness does not erase moral independence |
| `NEG-E07-AUD-001` | E07 | CHI | compare serious moral lines across states | simple moral-contraction model predicts uniformly low Layer-B activation | `ダメだよ 殺しちゃ` is highly activated while Mika repair is contracted | moral seriousness has no invariant Layer-B shape; Layer C required |

| `NEG-E08-TAK-001` | E08 | TAK | café faces ordinary financial failure | weapon-only competence model predicts civilian optimization should be weak/externally directed | Takina independently audits and redesigns finances, menu, labor, automation and investment | supports portable competence / civilian stewardship |
| `NEG-E08-TAK-002` | E08 | TAK | Chisato is directly threatened by Majima | universal-nonlethal-convergence model predicts Takina now mirrors Chisato | Takina arrives armed, fires, and regrets losing immediate opportunity | moral/force convergence remains false |
| `NEG-E08-CHI-001` | E08 | CHI | Majima supplies evidence Alan can support killing | biography-determinism model predicts Chisato's vocation should collapse into donor purpose | Chisato reasserts helping and `やりたいようにやります` | identity remains self-authored under pressure |
| `NEG-E08-BODY-001` | E08 | CHI | injection fear can be read symbolically through artificial-heart history | causal-symbolic model predicts heart history is stated cause | Chisato explicitly cites pain, inability to dodge, and foreign-object intrusion instead | thematic resonance must not be promoted into causal biography |
| `NEG-E08-AUD-001` | E08 | TAK/CHI | compare high-activation social, security, and moral states | simple F0/intensity-to-affect model predicts one valence/meaning | Takina safe-play laugh can exceed practical threat speech; Chisato serious lines span dynamic and constrained shapes | Layer-B activation is state energy, not subjective affect label |

| `NEG-E09-CHI-001` | E09 | CHI | own remaining life is cut to ~2 months by attacker | revenge model predicts direct self-harm should finally license retaliatory killing | Chisato rejects eliminating Himegama because it cannot restore the lost future | strengthens anti-revenge / irreversible-loss boundary |
| `NEG-E09-CHI-002` | E09 | CHI | mortality and childhood benefactor history are now explicit together | single-cause mortality model predicts nonlethal vocation should be explained solely by shortened lifespan | flashback directly shows child Chisato converting `救世主` and a killing-intended gun into helping meaning | requires layered-origin model |
| `NEG-E09-TAK-001` | E09 | TAK | long-desired DA reinstatement arrives | restoration model predicts uncomplicated happiness and return to earlier identity | Takina cannot say she is happy, had intended to refuse, and ultimately returns for Chisato's survival | DA changes from end toward instrument |
| `NEG-E09-REL-001` | E09 | CHI/TAK | Takina leaves for DA under Chisato's two-month horizon | captivity/dependency model predicts separation should be vetoed or relationally rupture | Chisato supports departure; Takina says `いってきます`; ordinary day is created before leaving | closeness remains noncaptive across separation |
| `NEG-E09-AUD-001` | E09 | TAK/CHI | compare threat, deliberate rescue, uncertainty and philosophy | simple activation=importance model predicts highest-stakes lines should always be loud/high | Takina's deliberate return decision is constrained while threat is highly activated; Chisato's serious philosophy ranges from constrained to highly activated | Layer-B energy cannot identify meaning/valence alone |


| `NEG-E10-CHI-001` | E10 | CHI | learns benefactor/parental origins were instrumentally compromised | contamination-by-origin predicts gratitude/identity collapse | preserves gratitude/fatherhood while claiming choices as hers | supports origin-authorship model |
| `NEG-E10-TAK-001` | E10 | TAK | restored DA status can again be threatened | DA-total-identity predicts expulsion remains existentially coercive | cites outside life as enjoyable and another firing as tolerable | institutional monopoly weakened |
| `NEG-E10-REL-001` | E10 | CHI/TAK | pair remains separated during crisis | dependency/proximity predicts trust requires reunion/supervision | Chisato entrusts Enkuboku to Takina/Fuki; Takina uses DA for Chisato | noncaptive trust-at-distance |
| `NEG-E10-MIK-001` | E10 | MIK | original motive/bargain exposed | fake-fatherhood model predicts later relationship invalidated | Chisato inventories Mika's fatherly life goods and calls him father | origin does not erase lived relation |
| `NEG-E10-MAJ-001` | E10 | MAJ | claims to restore free choice/truth | pure-liberation model predicts neutral agency | places guns and forces civilians into lethal uncertainty | anti-paternalism becomes coercive |
| `NEG-E10-AUD-001` | E10 | CHI/TAK | serious/high-stakes Layer-B speech | sincerity=low-energy predicts uniform contraction | Chisato gratitude/sadness contract while rescue expands; Takina threat spike exceeds deliberate rescue querying | Layer-B energy cannot identify sincerity/importance |


| `NEG-E11-TAK-001` | E11 | TAK | final DA-return opportunity conflicts with Chisato rescue | DA-total-identity predicts Takina will preserve institutional return at decisive cost | she knowingly forfeits DA because it cannot save Chisato | institutional belonging no longer sovereign |
| `NEG-E11-REL-001` | E11 | CHI/TAK | pair has been institutionally/physically separated | rupture model predicts crisis cooperation needs relational repair first | Takina enters Chisato's firefight immediately without renegotiation | separation is nonterminal to coordination |
| `NEG-E11-CHI-001` | E11 | CHI | Yoshimatsu is now known as coercive architect | enemy/betrayer-essentialism predicts his life becomes expendable | Chisato enters tower to save him and accepts tactical vulnerability to protect him | personhood remains separable from ideology |
| `NEG-E11-CHI-002` | E11 | CHI/MAJ | Majima shares anti-coercion premise | autonomy-alone model predicts alliance/moral sameness | Chisato explicitly says `一緒にすんな！` | self-authorship is necessary but not sufficient for morality |
| `NEG-E11-MAJ-001` | E11 | MAJ | claims first freedom/public truth | neutral-liberation model predicts citizens simply receive information/choice | he engineers armed witnesses, panic and lethal encounters | exposure remains coercively staged |
| `NEG-E11-AUD-001` | E11 | CHI/TAK | high-stakes moral/rescue speech | importance or sincerity predicts uniform acoustic contraction/expansion | quiet `分かってます`, expanded rescue criterion, playful combat and extreme `一緒にすんな` coexist | Layer-B energy cannot identify semantic/moral category |

| `NEG-E12-CHI-001` | E12 | CHI | donor holds literal route to continued life inside his own body | survival-at-all-costs model predicts she or Takina may kill him on her behalf without identity consequence | Chisato blocks Takina and says survival that way would no longer be herself | biological survival is bounded by authored identity continuity |
| `NEG-E12-TAK-001` | E12 | TAK | direct benefactor wrongdoing and chance for vengeance coincide | revenge-centered model predicts punishment remains objective | Takina says prior wrongdoing is now irrelevant once heart retrieval can save Chisato | optimization remains outcome-centered even under attachment crisis |
| `NEG-E12-REL-001` | E12 | CHI/TAK | pair reaches maximum-stakes disagreement over killing Yoshimatsu | value-conflict model predicts rupture or coercive ownership | Chisato stops Takina, Takina voices refusal of Chisato death, then pair continues together | intimacy does not require ethical convergence |
| `NEG-E12-DA-001` | E12 | KUS/DA | upper command orders Lycoris liquidation | monolithic-DA model predicts Kusunoki simply executes command | she covertly requests rescue then overtly withdraws LilyBell when conditions change | DA actors require differentiated agency model |
| `NEG-E12-EPI-001` | E12 | DA/KUR | public has visible embodied evidence of Lycoris violence | irreversible-exposure model predicts secrecy cannot recover | evidence is reclassified as staged attraction through Radiata/media intervention | epistemic order can recover through category change, not literal erasure |
| `NEG-E12-AUD-001` | E12 | CHI/TAK | compare morally/relationally maximal lines | importance=high-energy or sincerity=low-energy predicts monotonic profile | Takina scream is far louder than `嫌だ 千束が死ぬのは嫌だ`; Chisato central ethics span ~-20.6 to ~-31.5 dBFS | Layer-B magnitude cannot identify emotional/moral importance |

| `NEG-E13-CHI-001` | E13 | CHI | second heart gives survival after Yoshimatsu coercion | accepting rescue implies accepting donor purpose/symbolic affiliation | accepts medical survival, discards Alan token, retains own vocation | gift and ownership remain separable |
| `NEG-E13-CHI-002` | E13 | CHI | self-authorship after terminal prognosis | perfectly relational autonomy model predicts transparent farewell/coordination | disappears to avoid gloomy reactions and makes others search | autonomy has avoidant/paternalistic failure mode |
| `NEG-E13-TAK-001` | E13 | TAK | high-stakes operational choice with peer | early unilateral competence model predicts self-authorization | explicitly proposes `私たちで決めましょう` and distributes tasks | competence governance matures toward negotiated agency |
| `NEG-E13-AUD-001` | E13 | TAK/CHI | compare crisis, care, safe play and moral philosophy | emotional importance should track higher intensity or moral seriousness lower intensity | quiet life-changing reassurance/future advice coexist with extreme crisis and high safe-play activation; Chisato serious lines vary widely | rejects monotonic acoustic-importance mapping |
| `NEG-E13-PASSPORT-001` | E13 | ensemble | Hawaii presence after E02 civic exclusion | travel itself proves ordinary legal passport/civic-status normalization | dialogue jokes about passport and supplies no legal mechanism | E02 civic-status claim remains pressured but not prospectively erased |

# 9. Preference / affordance register

| Character | Domain | Evidence state | Current formulation | Evidence IDs |
|---|---|---|---|---|
| CHI | morning-city quiet | `DEMONSTRATED` | Likes the stillness before a large city starts moving | E01 00:48 |
| CHI | damaged/meaning-unclear urban object | `DEMONSTRATED_DOMAIN_SPECIFIC` | Says she likes the old tower's `意味不明` quality and entertains meaning produced by breakage | `E01-CLM-013` |
| CHI | idol/fandom knowledge | `UNKNOWN` | No E01 evidence | — |
| CHI | travel-food experience | `DEMONSTRATED_DOMAIN_SPECIFIC` | Treats station bento as part of what makes an express-train trip worth experiencing and presses Takina to sample it | E02 05:15-06:11 |
| CHI | food / finite experience | `DEMONSTRATED_PRINCIPLE` | Treats finite lifetime meals as experiences that should be enjoyable enough to justify bounded compensatory cost | `CHI-MB-E04-002`, `E04-CLM-007` |
| CHI | aquarium / leisure | `DEMONSTRATED_DOMAIN_SPECIFIC` | Treats aquarium leisure as intrinsically worthwhile and behaves as an off-duty civilian rather than continuous operative | `E04-CLM-008/012` |
| CHI | Tokyo sightseeing / guide work | `DEMONSTRATED_DOMAIN_SPECIFIC` | Invests in constructing a pleasurable last-day itinerary and values being a good guide; E05 deception later hurts because the experiential relation mattered | `E05-CLM-003/005/020` |
| TAK | DA return | `DEMONSTRATED_GOAL` | Strongly wants reinstatement through E03; E07 shows the DA/training return option still live even after E06 cohabitation, while ordinary/civilian obligations also independently govern her time | `TAK-MB-E01-002/004/007`, `TAK-MB-E03-001/002/003` |
| TAK | competition | `UNKNOWN` | No E01 evidence | — |
| TAK | clothing/style | `DEMONSTRATED_PROCESS / STABLE_STYLE_OPEN` | In unfamiliar style choice, first seeks specification/function and can delegate selection to trusted Chisato; E04 does not yet establish a stable aesthetic style preference | `TAK-MB-E04-002`, `E04-CLM-004/005` |
| TAK | travel meal selection | `DEMONSTRATED_CONSTRAINT` | Selects jelly because transfer time is under ten minutes; accepts offered bento and says it is delicious, but this remains constraint evidence rather than a stable preference | E02 05:15-06:11 |
| TAK | food / karinto | `DEMONSTRATED` | Explicitly states `私 あの かりんとう 好きです` without work justification | `TAK-MB-E04-003`, `E04-CLM-006` |
| TAK | off-hours group leisure | `DEMONSTRATED_PROVISIONAL_CHOICE` | Begins E03 declining the cafe game, but after identity disruption and Chisato's nonexclusive invitation voluntarily joins the still-running gathering; establishes willingness to try ordinary leisure, not a stable board-game preference | `TAK-MB-E03-001/006`, `E03-CLM-016` |

| TAK | civilian creation / menu design | `DEMONSTRATED_GENERATIVE_AND_REVISABLE` | Originates a new parfait on her own, then withdraws/revises it once unintended social meaning becomes legible | `E08-CLM-009` |
| TAK | LycoReco stewardship | `DEMONSTRATED_PERSON_DIRECTED_COMMITMENT` | Invests sustained administrative labor because the café is an important place to Chisato; this is strong attachment evidence but not yet a permanent-home declaration | `E08-CLM-025/026` |

| TAK | outside/civilian life | `DEMONSTRATED_AS_VIABLE_FALLBACK` | Explicitly says outside life was fairly enjoyable and can imagine another DA firing without identity collapse; stronger than provisional participation and weaker than permanent-home declaration | `E10-CLM-008/009` |

| TAK | seasonal commerce / hanami expansion | `DEMONSTRATED_SELF_INITIATED` | Treats profitable ordinary service as worth repeating weekly and independently proposes yakitori expansion for next year; preference is practical/commercial rather than Chisato-like pleasure vocabulary | `TAK-MB-SHORT01-001/002`, `SHORT01-CLM-004/005/006` |

# 10. Source-layer discipline

Anime-native observations use `A1_ORIGINATING_AUDIOVISUAL`.

After the anime-native freeze, supplementary entries may be added only with explicit source class and integration state.

Do not merge a Recollect-local observation into an anime-native policy row without routing through the multi-source integration method.

---

# 11. Update contract after each anime source unit

After every episode/short:

1. append diagnostic observations;
2. update state snapshot only where something materially changes;
3. stage or update candidate policies;
4. add meaningful negative evidence;
5. preserve unknowns;
6. route major relationship evidence to the relationship ledger;
7. route exact audiovisual locations to the primary-source locator index;
8. keep policy confidence proportional to coverage.

---

# 12. Current authority statement

At `SHORT01_OUTBOUND_FREEZE`, this ledger is the canonical cumulative A1 character-state authority through TV E01-E13 plus Friends Short 01. Short 01 independently validates settled mundane Takina: financial/logistical precision now generates civilian initiative and business planning while high armament readiness and concise baseline speech persist. Chisato's ordinary correction targets context/role overreach rather than competence itself. Mika, Mizuki and Kurumi retain ordinary social/caregiving functions beyond operational utility. `SHORT01-AUD-001`-`013` further strengthen state-conditioned, semantically non-monotonic performance bandwidth; Layer C remains `UNVERIFIED`. Short 02-06 and all supplementary narrative evidence remain inadmissible until opened prospectively.
