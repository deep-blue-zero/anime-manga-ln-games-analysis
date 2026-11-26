---
title: "Gakuen Idolmaster V2 - Voice Performance State Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.9"
source_lock: "GAKUMAS V2 Source Locks 1.0–1.2"
initialized: "2026-08-13"
last_updated: "2026-11-25 — Carbon character and claim write-through"
revised: "2026-11-25"
revision_note: "Adds the independently adjudicated support 3-0086 spoken register with its separate audio, picture and script clocks."
status: "active; cumulative through complete Phase-3 character audiovisual integration (13/13)"
---

# VOICE PERFORMANCE STATE LEDGER

> **Revision record — v2.6, 2026-11-15 (source-to-analysis audit corrections).** GKM-SAA-006, REVISE: the Temari T-DIA-04 Dear 035 row read "surname-to-given-name distance shift". A1 shows Temari asking only to drop `さん` (`adv_dear_ttmr_035.txt` L632–643), the Producer answering with the bare surname `月村` (single option, L647) and a plain imperative (L650), and the given name `手毬` arriving in Dear 037 on the Producer's initiative (`adv_dear_ttmr_037.txt` L417, single option L428). Her request remains her agency. Residual ambiguity: `呼び捨て` could in principle cover the given name, but A1 shows her naming only the honorific. The Dear 037 row gains the reception test. The earlier `last_updated` value read "2026-09-11 — RINHA-AV-20260911 bounded evidence integrated; perceptual review open".

This is a cumulative V2 project ledger. It is initialized in Phase 0 and must be updated rather than recreated as later phases add evidence.

## Recorded speech and performance at Source Lock 1.2, 2026-11-25

The following entries use reported listening on the named recordings and separately verified source clocks and frames. The earlier Phase 3 and September entries record what was available to those passes. The [receiver reconciliation](../05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_LOCAL_PLAYBACK_RECONCILIATION.md) identifies the reviewed editions, speaker corrections and limits of reviewer independence.

| Character and recording | What the scene contributes | Scope for later use |
| --- | --- | --- |
| Kaya Rinha, 11 P0 and seven P1 targets | Three consecutive support scenes share SRC-0083. Fifteen further scenes have paired reports on sixteen packet-verified audiovisual windows. In Temari Dear 016, SRC-0032 1847–2223 s, listeners hear distress while Rinha appears through still or replaced 2D portraits. In Saki Dear 026, SRC-0035 1967–2305 s, sustained disclosure reaches quiet encouragement. In Ume Dear 029, SRC-0011 299–588 s, she accepts the refusal and offers a technical suggestion before Ume initiates rehearsal. In Misuzu Dear 024, SRC-0014 941–1394 s, enthusiasm over merchandise and a statement of professional standards share one scene. | These different relationships support comparison of particular deliveries. The earlier zero listening count belongs to September. Five of six C073 controls fall within the eighteen targets. Two controls have paired historical whole-source coverage and four have paired native windows. The claim about a general register across original whole editions remains open. [All targets, source hashes, intervals and corrections](../05_AUDIOVISUAL_ANALYSIS/KAYA_RINHA/GKM_KAYA_RINHA_PERCEPTUAL_ADJUDICATION_20261125.md). |
| Hiwatari Kanae, SRC-0023 | At 1543–1610 s listeners describe hesitation in a sung fragment during a stand-in sound check. At 4125–4132 s they identify あなた様と共に where the player-specific display reads プロデューサー様と共に. Her restraint in the former scene and her formal address in the latter serve different recipients. | The sequence at 3274.5–3280.5 s shows the sprint back to the assessment. Her urgency in the Japanese inner wording and the accent of each delivered line require separate evidence. Seven transition-script and sixteen wrapper-take matches establish source correspondences. Run B's lesson and second supply endings and native B/D outcome and HUD displays remain open. [RES-01 and remaining gameplay questions](GKM_CARBON_RESIDUAL_EVIDENCE_REGISTER.md). |
| Shinosawa Hiro, SRC-0173 and SRC-0172 | Two independent listeners of the anonymous finished stereo at SRC-0173 2513.000–2525.800 s heard the engagement phrase in the credits. Hiro voices the claim around 2518.058 s. In the original dialogue she makes it at Dear 021 L134, the Producer denies it at L142 and she reformulates at L143. In SRC-0172 Dear 036 the display near 2984.5 and 2988.0 s reads ままらない while listeners report ままならない. Dear 037 near 3231.5 s supplies a separate full-form control. | Listeners can hear a comic engagement assertion over the credits music. The denial belongs to the script scene outside that excerpt. The closing vowel remains uncertain. The printed difference identifies an edition and supplies no recording date or client patch date. [Receiver PROP-0259 and PROP-0314](../05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_LOCAL_PLAYBACK_RECONCILIATION.md). |
| Hanami Saki, Unit Story 01 chapter 04 parts 7 and 21 | Part 7 brings broken delivery after Ume leaves. In part 21 paired soundtrack reports describe exertion moving toward steadier address. In context, the acknowledgment at L362 concerns Ume's physical ability. The score enters at SRC-0009 1877.451 s as the scene turns to Ume. | The change in backing belongs to the later scene. Each episode supplies its own interlocutors and cause for the change in delivery. [Receiver RES-05](../05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_LOCAL_PLAYBACK_RECONCILIATION.md). |

## Schema

| field | meaning |
| --- | --- |
| character |  |
| AV_source_id |  |
| text_source_id |  |
| voice_state_class |  |
| interlocutor |  |
| delivery_feature |  |
| story_state |  |
| confidence |  |
| notes |  |

## Seed entries

No substantive entries are asserted at Phase 0. The schema is intentionally initialized before close reading so later evidence can be added without changing data conventions.

## Phase 3 — Hanami Saki performed voice baseline

Voice-state labels describe repeatable performed states rather than immutable personality categories. Automated pitch/RMS summaries are comparative aids and may contain BGM contamination.

| character | AV_source_id | text_source_id | voice_state_class | interlocutor / arena | delivery feature | story state | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hanami Saki | `AV-DIA-SAKI-001` | `adv_dear_hski_023.txt` | `SV1 controlled containment` | Producer, private night aftermath | low, measured truth-management before first-loss admission | D-SAKI summer loss | high AV-A/B | older-sister role is evaluated rather than exposed as simple lie |
| Hanami Saki | `AV-DIA-SAKI-001` | same | `SV2 uncontained affect` | Producer | high cry of frustration; body and voice cease containment | same | high | immediate recommitment follows without emotional recovery |
| Hanami Saki | `AV-DIA-SAKI-001` | same | `SV3 relational exposure` | Producer | quieter explicit request for help, proximity, and permission to lean | same | high | chosen dependence, not passive collapse |
| Hanami Saki | `AV-DIA-SAKI-002` | `adv_dear_hski_027.txt` | `SV3 relational exposure` | Producer | tears, lowered extended self-doubt, no protective boast | D-SAKI Project Stardust return | high | daily crying and confidence/absence coexist |
| Hanami Saki | `AV-DIA-SAKI-002` | same | `SV4 reconstructed confidence` | Producer → imagined global audience | sharp rise into self-naming as `不屈のトップアイドル` | same | high | indomitability is received relationally, then made public |
| Hanami Saki | `AV-DIA-SAKI-003` | `adv_cidol-hski-3-018_01.txt` | `SV0 regulated intimate baseline` | Producer, nighttime call | softened pace, sleep/recovery routine, solicitous questioning | C-SAKI post-loss | high | creates physiological/social conditions for disclosure |
| Hanami Saki | `AV-DIA-SAKI-003` | same | `SV0/SV3 reciprocal witness` | Producer | lower supportive interpretation of his failure; teasing closure | same | high | revises one-way dependency model |
| Hanami Saki | `AV-DIA-SAKI-004` | `adv_dear_hski_035.txt` | `SV0 intimate observation` | Producer | quiet teasing; exact memory of trembling hand and stiff voice | D-SAKI pre-H.I.F. | high | she reads his constructed confidence |
| Hanami Saki | `AV-DIA-SAKI-004` | same | `SV4 accumulation/ignition` | Producer → stage | music clears before `違うわ`; voice expands as prior selves are gathered | same | high | actively accepts expectation rather than merely absorbing burden |
| Hanami Saki | `AV-DIA-SAKI-005` | `adv_dear_hski_036.txt` | `SV2 private rival affect` | Ume | huge laughter, frustration, softened mutual recognition | D-SAKI winter victory | high | rivalry and tenderness coexist without neutralization |
| Hanami Saki | `AV-DIA-SAKI-005` | same | `SV5 formal idol address` | H.I.F. audience | projected polite gratitude and distributed credit | same | high | public responsibility precedes challenge |
| Hanami Saki | `AV-DIA-SAKI-005` | same | `SV6 competitive command` | idols/rivals/world | BGM break at `だけどっ!`; rising projection into command | same | high | public older-sisterhood as generative hierarchy |
| Hanami Saki | `AV-DIA-SAKI-006` | `adv_cidol-hski-3-000_03.txt` | `SV2 exposure anxiety` | Producer, before live | high, fast, comic panic about Ume hearing the song | C-SAKI FMW | high | vulnerability need not be quiet |
| Hanami Saki | `AV-DIA-SAKI-006` | same | `SV4 stage ignition` | Producer → live audience | accurate praise, delighted melting, boast, self-naming | same | high | confidence production sequence directly observed |

### Current Saki voice thesis

Saki's performed maturity is not a permanent shift toward a quieter “authentic” voice. It is increased freedom to move among containment, rupture, exposure, reconstructed confidence, formal gratitude, and command without forcing one state to invalidate the others.
## Phase 3 — Temari provisional performance-state requests

No Temari AV has yet been inspected. These are hypotheses to test, not observed acting claims.

| character | AV request | script source | provisional state code | context | expected distinction to test | confidence/status |
| --- | --- | --- | --- | --- | --- | --- |
| Tsukimura Temari | T-DIA-01 | Dear 004 | `TV1 controlled resentment → rupture` | SyngUp support exposed | composure, rising anger, guilt, cry | PENDING |
| Tsukimura Temari | T-DIA-01 | Dear 009 | `TV2 reconciliation/intimate possession` | Misuzu/Producer | apology, `一緒に破滅` comedy/alarm, `私だけの` | PENDING |
| Tsukimura Temari | T-DIA-01 | Dear 010 | `TV3 lowered origin disclosure` | Producer | hated-child memory and artificial wings | PENDING |
| Tsukimura Temari | T-DIA-02 | Dear 016 | `TV4 childlike collapse` | Rinha retirement threat | cool persona breaking into raw pleading | PENDING |
| Tsukimura Temari | T-DIA-02 | Dear 019 | `TV5 rival command` | Misuzu | praise reception, command, response to refusal | PENDING |
| Tsukimura Temari | T-DIA-03 | Dear 022–023 | `TV6 fan/inferiority/loss` | Misuzu/Sena/Producer | admiration, shame, contained post-loss affect | PENDING |
| Tsukimura Temari | T-DIA-03 | Dear 027 | `TV7 artificial-flight confidence` | Misuzu/Producer | intimacy and rocket escalation | PENDING |
| Tsukimura Temari | T-DIA-04 | Dear 035 | `TV8 chosen name intimacy` | Producer | requested honorific drop (`月村さんじゃなくて`, L632–643) answered by the bare surname `月村` (L647) and a plain imperative (L650); the given name follows only in Dear 037, on the Producer's initiative (GKM-SAA-006) | PENDING |
| Tsukimura Temari | T-DIA-04 | Dear 036 | `TV9 formal title → attack` | public/Sena | gratitude, title receipt, noncustodial ambition | PENDING |
| Tsukimura Temari | T-DIA-04 | Dear 037 | `TV10 present self-love` | Producer/private | food pleasure, reciprocal `好き`, future orientation; reception of the Producer-initiated `手毬` (L428; silent line L441, `はいっ` L450; AV-CARBON-SAA-006) | PENDING |
| Tsukimura Temari | T-DIA-05 | cidol 000 | `TV11 song-self denial/recognition` | Producer/live | difference between spoken disavowal and singing | PENDING |
| Tsukimura Temari | T-DIA-07 | cidol 018 | `TV12 blue-flame cool` | Producer/live | cold image vs high-heat complete combustion | PENDING |

## Phase 3 — Kotone textual voice hypotheses (AV pending)

No acted-performance state has been promoted from text alone. Current hypotheses for direct AV testing:

| state | textual markers | AV question | status |
| --- | --- | --- | --- |
| performative cute/customer-facing | elongation, hearts, sugary Producer address | stable higher/brighter placement? deliberate breath/pacing? | PENDING |
| blunt private/peer | rough colloquial endings, profanity/comic threats | lower/flatter/faster delivery or merely lexical contrast? | PENDING |
| scarcity anxiety | compressed practical monologue, debt/work fixation | speech rate, breath, pitch instability? | PENDING |
| fanservice command | crowd-scale special-address language | cute intimacy scaled through projection rather than softness? | PENDING |
| grief after H.I.F. | professional rationalization → `一緒にいてください` | audible break between cognitive and affective states? | PENDING |
| debt-completion happiness | repeated `普通`, naming exchange | relaxation/brightness distinct from competitive exhilaration? | PENDING |


## Phase 3 — Mao integrated voice/performance states

The former provisional requests are closed. The observed model is **permeable theatrical poise**: Mao's recognizable identity lies in courteous stage-readable scene governance, while maturity permits fear, embarrassment, grief, dialect, need and tears to interrupt and rejoin the system.

| character | state code | source | observed state | function | disposition / limit |
| --- | --- | --- | --- | --- | --- |
| Arimura Mao | `MV1` | Dear 003–004 | composed prince narration → contracted body/category exposure → defensive/cute collision | shows role-category injury occupying timing, gaze and posture | CLOSED — INSPECTED |
| Arimura Mao | `MV2` | Dear 005–010; `雪解けに` | cute embarrassment / ordinary softness / fear | contradiction becomes increasingly survivable without installing “cute” as sole true self | CLOSED — INSPECTED |
| Arimura Mao | `MV3` | Dear 015 | reclaimed prince | `呪縛` is admitted before `ちゃんと本物` becomes opponent-facing command | CLOSED — INSPECTED |
| Arimura Mao | `MV4` | Dear 018–020; FJD | challenger / selected cool / humbled technical recognition | coolness becomes chosen pleasure and craft rather than defensive rigidity | CLOSED — INSPECTED |
| Arimura Mao | `MV5` | Dear 025–026 | authored dependence | firm professional argument, vulnerability and intimate necessity coexist | CLOSED — INSPECTED; enclosure risk OPEN |
| Arimura Mao | `MV6` | Dear 027 | public composure → private grief | proves recommitment and emotional recovery are separate variables | CLOSED — INSPECTED |
| Arimura Mao | `MV7` | Dear 033; `見て` | fear made princely / role archive | bravery includes visible failed composure; grief can precede chosen prince return | CLOSED — INSPECTED |
| Arimura Mao | `MV8` | Dear 036–037 | public Prima Stella → tears → intimate unfinished prince | succession, gratitude, title, `0番` and continued witness become interoperable | CLOSED — INSPECTED; D-MAO only |
| Arimura Mao | `MV9` | `ミラクルナナウ(ﾟ∀ﾟ)！` commu | Osaka/Kansai/local-family register | deliberate dialect play, child-actor embarrassment, filial vulnerability and homecoming projection widen the voice model | CLOSED — INSPECTED |
| Arimura Mao | `MV10` | `SUGAR FLAVOR` commu/MV/3DMV | differentiated duet co-performance | another performer can alter Mao's image without dissolving her legibility | CLOSED — INSPECTED; bilateral Rinami synthesis OPEN |

Mixed-scene source metrics are audit support only. BGM, effects, editing and other speakers prevent isolated claims about Nanase Tsumugi's F0, timbre, breath or resonance.

## Phase 3 - Lilja provisional voice-performance requests

No Lilja AV has been inspected. These are textual hypotheses only.

| character | AV request | script source | provisional state | context | distinction to test | status |
| --- | --- | --- | --- | --- | --- | --- |
| Katsuragi Lilja | `AV-DIA-LILJA-001` | Dear 001-010 | shy novice -> first delivered courage | STEP1 | hesitation, self-command, Sumika-directed performance | PENDING |
| Katsuragi Lilja | `AV-DIA-LILJA-002` | Dear 011-020 | fan confidence -> desperate proof -> governed return | N.I.A. | whether injury/overwork sounds desperate rather than heroic | PENDING |
| Katsuragi Lilja | `AV-DIA-LILJA-003` | Dear 021-027 | jealousy/technical humility -> charisma discovery -> unit ask | STEP3 | shame, excitement, chuuni world-authoring | PENDING |
| Katsuragi Lilja | `AV-DIA-LILJA-004` | Dear 028-037 | leader/teammate/rival -> Prima Stella -> intimate future request | H.I.F. | public authority versus private softness/dependence | PENDING |
| Katsuragi Lilja | `AV-DIA-LILJA-010` | cidol 010 | Producer-history/fallibility | modular | change from idealized authority to reciprocal care | PENDING |
## China integrated voice-performance states — direct AV complete

China’s performed voice is best modeled as **permeable cultivated continuity**. The high-polite `わたくし/ですわ` system survives panic, shame, delight, grief, rivalry and public command; state change appears primarily through attack, pace, breath, held vowels, laughter, gaze and bodily organization rather than pronoun replacement.

| state | principal sources | performed organization | disposition |
| --- | --- | --- | --- |
| cheerful beginner certainty | Dear 001–005; `Wonder Scale` commu | bright attack, open delight and comic overcommitment coexist with visible technical weakness | CLOSED — AV VERIFIED |
| privilege anxiety / ethical seriousness | Dear 006, 011 | pace and body narrow; juridical vocabulary is delivered as sincere self-binding rather than ornamental humility | CLOSED — AV VERIFIED |
| asking for help / receiving correction | Dear early/middle | embarrassment remains legible, but information is received before self-defense closes the scene | CLOSED — AV VERIFIED |
| fan gratitude / constitutive support | Dear 009–020; `Campus mode!!` | plural address expands after uncertainty; gratitude becomes public obligation without erasing individual agency | CLOSED — AV VERIFIED |
| `ふにゃ` receptive softness | Dear 034/037 | looser timing, breathier/flustered reaction, inward or collapsed posture; not a lower-status “true self” | CLOSED — AV VERIFIED |
| `きり` organized authority | Dear 028–036; `空と約束` | cleaner attack, completed clauses, direct gaze and scene control; effortful but explicitly owned | CLOSED — AV VERIFIED |
| nondelegable resolve | Dear 026/035 | delegation grammar stops at the point where China must face Sena and public comparison herself | CLOSED — AV VERIFIED |
| Prima Stella claim | Dear 036 | public projection names support and raw-skill asymmetry while still asserting `勝ったのは、わたくしです` | CLOSED — D-CHINA ONLY |
| post-victory incomplete self-name | Dear 037 | authority can recede into panic and uncertainty without invalidating the victory claim | CLOSED — AV VERIFIED; endpoint remains OPEN |
| Hiro reciprocity | Dear 032–033; `みちなるひろがる` commu/3DMV/MV | peer delight, shared naming and distributed focality weaken the patron-only model | CLOSED FOR PHASE 3; Phase 6 bilateral audit remains |

Complete-source loudness and dynamic metrics are audit support only. BGM, music, effects, UI, other speakers and mastering prevent isolated claims about the performer’s vocal instrument.

## Hiro voice-performance hypotheses — textual only, AV pending

| state hypothesis | textual anchors | verification question | status |
| --- | --- | --- | --- |
| difficulty curiosity / deadpan delight | Dear 004-007; Produce Events | does attraction to hardship sound calm, bright, mischievous, or affectively flat? | REQUESTED |
| bodily exhaustion | Dear 001-007; P1 | how does actual fatigue alter breath, pacing, pitch and articulation? | REQUESTED |
| first jealousy / competitive ignition | Dear 008 | does `悔しい` emerge as a perceptible break from usual underreaction? | REQUESTED |
| intimate Producer teasing | Dear 005/020/028; cidol | acoustic difference between playful sadism language and genuine attachment fear | REQUESTED |
| fear of loss | Dear 029-030; P3 failure fragments | whether fear narrows/lowers/accelerates delivery compared with enjoyable pressure | REQUESTED |
| goddess / `神格` public state | Dear 021-26 | whether the text's divine vocabulary corresponds to a stable performed register | REQUESTED |
| cute desire | cidol 018; Dear 024-26; comic repertoire | whether cuteness is vocally distinct or mainly conceptual/visual | REQUESTED |
| HIF `不純` / summit address | Dear 036 | projection, command, strain and vulnerability in public victory speech | REQUESTED |
| post-miracle ordinary Hiro | Dear 037 | how rapidly peak state collapses back into intimate/ordinary register | REQUESTED |

## Rinami voice-performance hypotheses — Phase 3 textual only

No acoustic claim is promoted yet. AV should test these candidate states:

| state | textual anchors | hypothesis to test |
| --- | --- | --- |
| ordinary care | Produce Events; Dear 004–008 | relaxed warmth distinct from consciously activated public onee-san mode |
| public onee-san activation | Dear 003–009; P1 | slightly more deliberate/fan-facing performance that becomes less effortful over time |
| receiving/dependence | Produce Event activity_020; Dear 020, 023–027 | softer or more exposed register without total regression into little-sister caricature |
| romantic hesitation | Dear 009–010; CIDOL 000 | intimacy/embarrassment distinct from fanservice warmth |
| competitive desire | Dear 017–019, 027 | sharper forward drive and less self-effacing pacing |
| technical/professional command | Dear 031–036 | veteran control, precision and audience-directed confidence |
| confession/vow | Dear 037 | possible movement through playful familiarity → direct romance → solemn vow → professional request |

AV priority: whole Dear 001–037 packets plus `clumsy trick` and `36℃ U･B･U`.

## Sumika voice-performance hypotheses — Phase 3 textual only

No acoustic claim is promoted yet. AV should test:

| state | textual anchors | hypothesis to test |
| --- | --- | --- |
| ordinary gyaru enjoyment | Produce Events / travel/social CIDOL | relaxed, rapid, playful register genuinely distinct from defensive brightness |
| defensive brightness | Dear 005–008, 012–014 | audible strain/overprojection or timing shifts when joking protects against stakes |
| trauma/fear | Dear 005–008, 021, 034 | breath/tempo/silence and bodily effort around injury/expectation |
| chosen strong-idol | Dear 008–010; CIDOL 007 | deliberate projection that is not simply false cheer |
| open dependence | Dear 014, 026–028, 034 | softer/intimate register without erasing agency |
| dance/professional command | Dear 023–025; CIDOL 012 | technical certainty/instruction and self-authorship |
| public testimony | Dear 032 | confession transforming into audience-directed encouragement |
| Prima Stella | Dear 036 | command/joy/fear residue in summit speech |
| reciprocal intimacy | Dear 037 | teasing familiarity -> request for true feelings -> emotional proof of vocation |

## Phase 3 audiovisual integration — Fujita Kotone / Iida Hikaru

| performance state | bounded finding | evidence | confidence |
| --- | --- | --- | --- |
| baseline mobility | the stable acting trait is fast, intelligible movement among sweet, blunt, anxious, calculating, intimate and public modes | Dear 1–10; 21–27; eight song commus | very high |
| delegated confidence | early uncertainty remains audible beside strong social competence; praise changes action without erasing doubt | Dear 1–10; `世界一可愛い私` | high |
| professional self-audit | complaint and rapid analysis are information-bearing rather than comic noise only | `Yellow Big Bang！`; late Dear | very high |
| scalable address | public warmth becomes more commanding while retaining service orientation | `Campus mode!!`; self-esteem song; 3DMVs | high |
| loss/grief | professional reframing and grief coexist; request for presence is not simply failure of professionalism | Dear 025 | very high |
| late ordinary relief | Dear 027 broadens timing and affect around `普通`, debt completion and career reciprocity | Dear 027 | very high |
| source boundary | Dear 11–20 remains exact-text aligned rather than directly rendered in this pass; no fine acoustic claim is routed solely through it | source manifest | explicit limitation |

Current voice-performance thesis: **register switching is character identity; no single register has privileged ontological truth.**

## Phase 3 Ume — integrated voice-performance baseline

Complete Dear 001–037 rendered coverage has been inspected. Exact wording and continuity remain controlled by Source Lock; the AV specialist governs delivery, timing, breath, embodied expression, and addressee-specific performance.

| state | observed delivery/behavior | source anchor | disposition |
| --- | --- | --- | --- |
| ordinary bright/direct Ume | high-commitment plain speech, fast affective commitment, laughter and bodily momentum; brightness is genuine but not constant | Dear 001–008; lower-stakes route states | PRESERVE / STRENGTHEN |
| equal-rival fear | onset slows, gaze and posture compress, and confidence becomes something deliberately performed; fear intensifies as parity becomes real | Dear 009; Dear 033 | REJECT literal fearlessness |
| mixed/boxed emotion | direct wording can coexist with held posture, chest-centered gesture, lowered gaze and pauses; simplification is an active container, not absence of complexity | mid-route `秘密の箱` cluster | STRENGTHEN emotional compartmentalization |
| Saki victory and aftermath | triumphant attack gives way to tears, pleading not to be left behind, then calmer differentiation in `もう、追いかけない` | Dear 019–020 | REVISE victory-as-closure |
| Producer attachment | affection, jealousy and reassurance-seeking remain direct, but uncertainty changes timing and physical scale rather than creating a wholly separate persona | P1/P2 endings; Dear 023; song commus | PRESERVE relational dependence with narrowing |
| fan-facing service | audience address becomes deliberate projection: held anxiety is converted into larger, outwardly available energy rather than private discharge | `Campus mode!!`; handshake/sign states | STRENGTHEN fan relation as learned craft |
| late strongest-idol address | private fear and public command remain recognizably continuous; refusal of false modesty honors rivals, and summit speech becomes invitation | Dear 036–037 | STRENGTHEN generative supremacy claim while keeping D-UME scope |

Current voice-performance thesis: **pressure-compressed directness**. Ume generally does not hide behind a polished alternate voice. Pressure instead changes onset, pace, breath, gaze and bodily scale. She compresses, then rebounds into direct speech that recruits an addressee.

Governing specialist: `GKM_UME_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` — Drive `1G6Vy6_TnzBxaYiG37APhyOkxsNMDpvRy`.

Measurement boundary: audio statistics are source-mix envelopes, not isolated performer-acoustic measurements.

## Hataya Misuzu — pending audiovisual performance hypotheses

| hypothesis | textual basis | required AV test | current status |
| --- | --- | --- | --- |
| soft delivery can carry coercive/possessive semantics without overt hardness | Dear 005; CIDOL 000/014 | compare acoustic delivery of care language with `埋め尽くす` / `わたしのもの` rhetoric | OPEN / requested |
| jealousy activates rather than simply destabilizes her | P2 / CIDOL / Producer-other-idol scenes | test tempo, pitch, consonant attack, facial timing | OPEN / requested |
| private defeat pain is deeper than her public composure suggests | Dear 022; Dear 032 retrospective crying | inspect acted defeat and confession scenes | OPEN / requested |
| Temari, Rinha, Producer and fans receive distinct intimacy registers | Dear 1–37 | longitudinal voice comparison across addressees | OPEN / requested |
| `VEIL` should sound/stage becoming rather than completed majesty | CIDOL 016 | singing, arrangement, choreography and camera progression | OPEN / requested |
| Misuzu's public stillness is active stage control rather than low energy | `ツキノカメ`, `Campus mode!!`, `Superlative` textual functions | MV/3DMV blocking, gesture economy and focal control | OPEN / requested |

## Juo Sena - Phase 3 pending voice-performance states

| state | textual anchors | AV question | priority |
| --- | --- | --- | --- |
| Perfect public crown | Dear 001-006; public work | authority through resonance, diction, tempo, stillness, brightness, or some combination | P0 |
| Ceiling / fatalism | Dear 001-002 | controlled despair versus audible fracture | P0 |
| Producer apprentice | Dear 003, 010, 012-027 | analytical, junior-coded, playful, possessive, or layered | P0 |
| Failed scout | Dear 003 | humiliation versus ordinary embarrassment | P0 |
| Human / cute Sena | Dear 004-007; Produce Events | accidental leakage, chosen supportability, strategic incorporation, or all three | P0 |
| Fangirl | Dear 009, 011 | magnitude of departure from command register | P0 |
| Strong-rival fear | Dear 005, 008, 011, 025-027 | whether fear remains inside authority rather than replacing it | P0 |
| Kotone reciprocal star | Dear 018-024 | professional, sisterly, romantic-coded, possessive, and fan registers | P0 |
| Institutional reformer | Dear 021-027 | command, invitation, manifesto, contest ritual | P0 |
| Post-victory openness | Dear 027 | relief, affection, greed, and renewed hunger in one state | P0 |

**Minimum whole-video packet:** Dear 1-10, 11-20, and 21-27. No acoustic conclusion is current before inspection.

## Phase-3 Tsubame voice-performance state — 2026-08-16

**Status: textual baseline complete; rendered voice acting pending.** Do not infer Yuna Ogata's timbre, pitch, breath, tempo, or breakdown/recovery patterns from the dialogue text. Priority tests: (1) formal vice-president vs close-rival `貴様` register; (2) Dear 006 Misuzu-loss collapse; (3) vulnerable Producer-directed lines; (4) Dear 024 separation/resolve; (5) `クライアイ` textual `余裕`/beckoning direction. Acquisition is routed through `GKM_TSUBAME_AUDIOVISUAL_BASELINE_AND_REQUESTS.md`.

## Phase 3 — Hataya Misuzu integrated voice-performance state

**Status: COMPLETE integrated baseline.**

Current performance model: Harusaki Non's Misuzu performance makes control feel hospitable. Care, teasing, jealousy, possession, anger, grief, and public command are differentiated mainly through timing, pressure, exposure, and degree of cushioning rather than through a simple gentle/dark binary.

Key longitudinal states:

1. post-SyngUp! weakened calm;
2. care and indispensability disclosure;
3. direct conflict with Temari/Rinha;
4. defeat pain stored under composure;
5. wrong-path acceleration and loss of identity congruence;
6. restored self-authored pace;
7. Prima Stella projection plus open tears and bodily rest.

Authority: `GKM_MISUZU_DIALOGUE_VOICE_ACTING_CLOSE_READING.md`; integrated synthesis: `GKM_MISUZU_COMPLETE_AUDIOVISUAL_BASELINE.md`.

## Phase 3 Hiro integrated audiovisual voice states

| character | state | sources | verified performance tendency | interpretation | limitation |
|---|---|---|---|---|---|
| Hiro | ordinary / early | Dear 001–007 | low-force speech, long pauses, quiet amusement, breath/recovery foregrounded | micro-affective deadpan; bodily floor remains real | scene mixes are not stem-isolated |
| Hiro | jealousy / positive desire | Dear 008–010; `ガラクタロード` | pauses become discovery; embarrassment around `かわいくなりたかった` | ordinary longing is more exposing than abstract strangeness | exact F0 not promoted without isolated track |
| Hiro | friend-secret | China/Ume and `ガラクタロード` | playful selective disclosure; friends provide larger reaction scale | social plurality beyond Producer dyad | event breadth pending |
| Hiro | `神格` / public image | Dear 022–026; principal songs | restraint and distance can become charisma | reception mode, not essence | staging source-dependent |
| Hiro | crisis | Dear 009, 025–028, 036 | attention appears more aligned/directional under stakes | crisis concentration is real but ethically unsafe to universalize | no claim of causal physiology |
| Hiro | cute/comic | Campus, Happy Mille-Feuille, 仮装狂騒曲, ミラクルナナウ | play and warmth without total voice replacement | cute desire compatible with Hiro continuity | song mix/choreography carry part of effect |
| Hiro | late fear/shared dream | Dear 028–037; `ガラクタロード` | calm can contain fear; gratitude/future language becomes direct | hobby becomes accountable attachment | later failure response still open |

## Sumika integrated voice-performance delta — 2026-08-17 (late Dear backfill closed)

Current voice model: **elastic social brightness with reversible register permeability**. Sumika's fast, affiliative gyaru sociality is authentic rather than a false baseline. The defensive mechanism is strategic continuity: teasing, joking, and conversational motion can keep a high-stakes moment from resting long enough to become a verdict. The complete Dear 001–037 spine and song commus now directly show a wider mature capacity: Sumika can allow fear/testimony/intimacy to remain visible, receive relational support, and then deliberately return to brightness without making the disclosure retroactively unserious.

| late state | direct AV evidence | current reading |
|---|---|---|
| Dear 032 public testimony | visible fracture → Lilja co-regulation → trauma naming → audience promise → tears → humor return | brightness changes from avoidance to social repair after vulnerability has counted |
| Dear 034 private fear | narrowed posture/delivery; explicit `今から本音を言うね`; requested hand contact; gradual reopening | courage can be relationally borrowed without being counterfeit |
| Dear 036 Prima Stella | initial shock/tearfulness → colloquial `紫雲清夏で～す！` → high-projection direct `キミ` address | summit projection integrates fear/support/history instead of restoring invulnerability |
| Dear 037 post-victory intimacy | explicit temporary suspension of Producer role → still reception of his insecurity → bright future return | professional/personal permeability is consciously managed, though dependency and authority asymmetry remain open |

Mixed-scene acoustic proxies broadly rise from several private fear/trauma segments toward public-promise/summit/future-facing segments, but remain **source-level corroboration**, not isolated measurements of Minato Miya's vocal F0, timbre, breath, or dynamics.

Primary AV authority: `GKM_SUMIKA_COMPLETE_AUDIOVISUAL_BASELINE.md`; specialist: `GKM_SUMIKA_DIALOGUE_VOICE_ACTING_CLOSE_READING.md`.

**Transition:** bright gyaru = fake mask — **REJECT**. Strategic unseriousness — **STRENGTHEN**. Technical/professional register — **STRENGTHEN**.


## Mao integrated voice-performance model — 2026-08-17

**Current specialist authority:** `GKM_MAO_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` — Drive `10rIzRjSsnPhdN-HR6IK96zui7XNZYbRz`.

| state | performed signature | function | direct controls | limit |
| --- | --- | --- | --- | --- |
| ordinary senior/prince | courteous completion, controlled smile, upright/presenting body, scene orientation | care, professional legibility, social organization; can also hide desire | early Dear; `Fluorite`; dorm commus | not a single pitch or fixed timbre |
| cute-embarrassment collision | stammer, repetition, blush, delayed response, self-touch, posture contraction, enlarged reaction | category alarm + social exposure + ordinary shyness | Dear 003–010; `雪解けに`; FJD commu | later embarrassment becomes playful/intimate rather than disappearing |
| chosen prince / stage command | direct address, strong line, formal clarity, opponent/crowd orientation after wound is admitted | voluntary role authorship and public command | Dear 015; FJD 3DMV; `見て`; Dear 036 | late command is not emotional uniformity |
| wounded child / defensive fixation | child `わたし` wonder → repeated `違う` → rejection of princess/cute objects → breathless recovery | shows authentic desire recruited into emergency continuity | `見て` commu | does not prove `ボク` or princehood false |
| reflective grief | reduced motion, withheld face, silence, tears before resilient interpretation | preserves loss as owned history rather than instantly solved material | Dear 027; `見て` theatre aftermath; Dear 037 | recommitment and recovery remain separate variables |
| Producer-directed flirtatious prince | deliberate escort/umbrella theatre, teasing challenge, intimate direct address | makes desire speakable through chosen performance | `見て` rain scene; Dear 037 | professional asymmetry remains |
| Osaka/Kansai play | performative Kansai-ben, comic demand-response, local slip under embarrassment, food pleasure | locality, childhood memory, familial recognition, de-formalization | `ミラクルナナウ(ﾟ∀ﾟ)！` | local resource, not the hidden sole “real” voice |
| public succession | formal gratitude + institutional metaphor + audience invitation | makes prince voice publicly answerable and generative | Dear 036; `Campus mode!!` | Mao ethic, not universal institutional rule |

## Phase 3 — Amaya Tsubame integrated voice-performance state

**Status:** integrated AV baseline COMPLETE.

**Canonical authority:** `GKM_TSUBAME_COMPLETE_AUDIOVISUAL_BASELINE.md`.

**Performed-voice formulation:** **armored declarative poise**. Tsubame's ordinary performance of authority is not simply a low or harsh voice; it is a scene-governing procedure built from decisive sentence attack, completed phrasing, controlled tempo, command-ready projection, and a tendency to convert emotion into challenge or declaration. The audiovisual corpus shows that this armor is permeable rather than total. Embarrassment, nerd enthusiasm, fear, dependence, grief, and intimate rivalry alter timing, breath, pitch behavior, and sentence completion without producing a separate hidden “real Tsubame.”

**Major register findings:**

- formal institutional/vendor speech and vice-presidential competence remain clearly distinct from close-rival/Producer `貴様` combat speech;
- Dear 006 renders defeat as loss of scene control before challenge language rebuilds structure;
- the outing corpus materially expands ordinary/private Tsubame through hobby enthusiasm, food, comedy, business courtesy, and chūnibyō play;
- mature vulnerability often remains declarative: dependence is voiced as reciprocal obligation rather than softened submission;
- Sena intimacy becomes renewable contest and ordinary familiarity rather than only summit-directed aggression;
- public idol address increasingly redirects combative force outward as courage, invitation, and responsibility.

**Song-performance contrast:** `理論武装して` formalizes antagonism as fan-facing rhetoric; `Campus mode!!` integrates institutional brightness without neutralizing Tsubame's weight and command; `クライアイ` demonstrates held, equal-facing invitation rather than pure upward attack.

**Revision state:** textual heroic-rivalry model **STRENGTHENED**; “heroic star quality” **REVISED/STRENGTHENED/OPEN** as an outward reorientation of technical command toward another person's recoverable future, not a mystical trait.


## Kuramoto China / 倉本千奈 — performed voice-state baseline (2026-08-21)

| state | performed markers | analytical implication |
|---|---|---|
| cultivated ordinary register | `わたくし`, `ですわ`, careful honorific phrasing, bright forward placement | elite upbringing is embodied habit, not occasional cosplay |
| cheerful incompetence / panic | elongated cries, breathy fluster, rapid pitch movement, sentence disruption while register morphology often survives | emotional disarray and cultivated identity coexist |
| accurate self-deprecation | comic certainty can shade into genuine shame; delivery and posture distinguish the mixture | never infer humility’s valence from wording alone |
| asking for help | softer attack, upward/relational orientation, visible dependence without total passivity | support is actively solicited rather than merely bestowed |
| delegation / leadership | firmer onset, longer clause control, clearer gaze and gesture completion | `きり` is constructed competence but not therefore inauthentic |
| nondelegable responsibility | reduced comic escape, held pauses, frontal exposure | mature leadership requires moments that cannot be outsourced |
| `ふにゃ／きり` integration | rapid but intelligible movement between softened collapse and gathered authority | one self with multiple regulatory states, not a binary persona system |
| D-CHINA summit | command and gratitude coexist; authority retains traces of effort and fragility | relationally ratified sovereignty rather than invulnerable regality |

Specialist authority: `GKM_CHINA_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` — Drive `1G5g5AfxZiKCR2EieELQXEjhknvB6Ysp2`.


<!-- LILJA_AV_R1_UPDATE_2026-08-22 -->
## Katsuragi Lilja — tremulous continuity

Lilja's voice does not develop by losing hesitation. Its mature signature is **tremulous continuity**: pauses, soft attacks, breathy uncertainty, and relational checking remain audible, but they cease to prevent completion, public projection, leadership, or challenge. Early tremor often interrupts action; late tremor can coexist with action.

Key contrasts:
- shy/private Lilja: reduced pace, softened attack, checking intonation, incomplete starts;
- excited/otaku Lilja: faster tempo and denser completion without losing politeness;
- overtraining crisis: determination hardens into bodily self-negation;
- Sumika-facing leadership: softness becomes directive without imitating Sumika's social speed;
- late public authority: visible/audible fragility remains inside completed projection.

Fine facial claims in Dear 028–037 are resolution-limited because the available file is 360p30. Voice timing and broad acting remain directly usable.

<!-- RINAMI_AV_R2_UPDATE_2026-08-22 -->
## Himesaki Rinami — voice/performance state after integrated AV R2

| state | speech/voice organization | body/visual organization | interpretation | caution |
| --- | --- | --- | --- | --- |
| ordinary care | warm mid register, light teasing, `くん`, responsive laughter, completed practical clauses | open torso, attentive head angle, small inviting gestures | care predates conscious idol branding | do not make every warm line strategic seduction |
| activated onee-san | slightly heightened melodic contour, polished reassurance, conscious role marking | frontal availability, softened gaze, readable hand shapes | achieved public technology rather than false mask | role can still become overfunctioning |
| receiving/depending | more delay, breath, repeated opening, reduced clause confidence | inward hands, lowered/averted gaze, contraction before reopening | lets the other person matter to her | dependence is not proof of regression |
| archive shame | compressed timing, self-monitoring, deflection, embarrassed laughter | held posture, sidelong gaze, face/hands partially guarded | old labor remains owned even when role-fit failed | involuntary exposure is not automatically truer |
| competition | sharper completion, more frontal projection, direct personal stakes | upright line, forward gaze, larger committed shapes | care tolerates zero-sum desire | do not rewrite competitiveness as coldness |
| dream crisis | private contraction, tears, running/breath disruption, delayed self-reference | hand-to-chest gathering, downward gaze, visible tear persistence, later direct claim | tests whether the dream is hers | family/home is a real alternative, not a false prison |
| technical authority | precise explanatory language and evaluative vocabulary | deliberate posture, whole-body demonstration, partner awareness | craft is one form of care | production remains collaborative |
| summit/public love | sustained projection, audience-directed completion, gratitude that permits reception | tears, closed-eye recollection, reopened gaze, expansive public address | audience love returns into self-recognition | approval dependence remains a pressure |
| confession/vow | blush-compatible hesitation followed by explicit `好きだよ`, mutual-aid and professional language | contraction, hand to sternum, averted gaze, direct-eye-contact recovery | romance intensifies the same relational grammar | personal/professional fusion requires governance |

Longitudinal textual corroboration remains comparative rather than psychometric: ellipsis-bearing lines fall markedly in D04 while desire/love/victory vocabulary rises. R2 audio-identity verification preserves all earlier timecode and selected-prosody locators; the new 720p files raise only the visual-evidence ceiling.

<!-- RINHA_AV_20260911 -->
## Kaya Rinha performance-state controls — not yet heard

The zero counters in this dated entry cover the September 2026 pass. The November [recorded speech comparison](#recorded-speech-and-performance-at-source-lock-12-2026-11-25) and [18-target addendum](../05_AUDIOVISUAL_ANALYSIS/KAYA_RINHA/GKM_KAYA_RINHA_PERCEPTUAL_ADJUDICATION_20261125.md) carry the subsequent evidence.

The [18-target baseline](../05_AUDIOVISUAL_ANALYSIS/KAYA_RINHA/GKM_KAYA_RINHA_COMPLETE_AUDIOVISUAL_BASELINE.md) has source-bound text, still observations and selected stereo-mix measurements. Direct listening and continuous-motion counters both remain 0 seconds. No acoustic emotion state or final speech-simulation register is promoted.

Keep separate: Temari’s 3D crying, Rinha’s bust expression and Temari’s report of Rinha crying (Dear016); Rinha’s internal/public framing change (Temari020); fan engagement versus self-disqualification poses (Misuzu024); recoded versus sustained versus accepted disclosure endings (Temari016/Saki026/support0097-03). Ume015’s imitation report and `krnh` voice-asset identifiers do not establish real performer identity or acoustic fidelity. Mixed-window LUFS/LRA values are recording controls, not Rinha-specific voice-state measurements.


## Source Lock 1.1 — transcript refresh, 2026-11-12

| character | AV source | text source | delivery question | story state | status |
| --- | --- | --- | --- | --- | --- |
| Rinha, Misuzu, Temari | AV-CARBON-RIN-001 | GKM-R86-08 | Compare café question, challenge and deflection, separating present speech and recalled incident. | M-MISUZU 018 | Text only. Supplemental, no change to 1.0 gate. |
| Rinami and Tsubame | AV-CARBON-E028-001 | GKM-R86-05 | Distinguish invitation, inner response and movement into public performance. | E028 | Text and script markers, synchronized AV pending. |
| Lilja, Saki and Ume | AV-CARBON-E030-001 | GKM-R86-06 | Compare the same line across failed and accepted takes. | E030 | Text and reported staff decisions, rendered delivery pending. |
| Kotone | AV-CARBON-KOT-001 | GKM-R86-01 | Mark imagined, recorded and public audience layers and delivery shifts. | D-KOTONE 035–036 | Text and script staging, voice and rendering pending. |
| Sena and Tsubame | AV-CARBON-TSB-003, AV-CARBON-SEN-001 | GKM-R86-02, 03 | Track private address and titleholder address inside their own outcomes. | D-TSUBAME and D-SENA | Synchronized AV pending. |

## Source Lock 1.2 — transcript refresh, 2026-11-15

| character | AV source | text source | delivery question | story state | status |
| --- | --- | --- | --- | --- | --- |
| Hiwatari Kanae | AV-HKNE-R88-04 | GKM-R88-01, Dear 004/005/008 | align technical performance instruction, courtesy with China, private speech and the explicit request to step on stage | Kanae Dear, multiple distinct scenes | AV-C script and register only |
| Hiwatari Kanae | AV-HKNE-R88-05 | GKM-R88-06, live 001 and seven common steps | resolve `{voice_asset_id}` where applicable and align voice cues to messages or non-message slots | separate live wrappers and common steps | AV-C cues, zero direct listening |

## Sena and Tsubame — support scene performed register, 2026-11-25

In exact `SRC-0093` Sena’s date reveal is bright, set up by a spoken passage with the score withheld around 203–213 s. Her declaration of unfamiliarity with romantic love is quieter and slower around 232–238 s. The closing liking at approximately 249–255 s uses the move from given name to `あなた` in one warm address. Tsubame stammers near 228–232 s, protests more loudly in the next exchange and gives a breath-caught, flustered reply near the ending. These are relation-specific performances in `adv_csprt-3-0086_03`, not isolated voices. Cue boundaries are approximate to the ear. The original also gives a verified native speaker nameplate at 254.867 s, a separate picture clock. **STRENGTHEN** the contextual affect range. Relationship category remains **OPEN**. [Original recording and cue scope](../05_AUDIOVISUAL_ANALYSIS/12_JUO_SENA/GKM_SENA_TSUBAME_SUPPORT_3_0086_PERCEPTUAL_ADJUDICATION_20261125.md).

## Carbon character and claim write-through — 2026-11-25

| Role | Paired/reconciled delivered state | Ceiling |
| --- | --- | --- |
| Sumika imitates Lilja, E001 part 2 | `ssmk-018` is higher and breathier under the display's question-mark role. The score has already receded before she speaks. Temari's response is accompanied by the 16-bar display. [Current source](../05_AUDIOVISUAL_ANALYSIS/09_SHIUN_SUMIKA/GKM_SUMIKA_CARBON_AV_UPDATE_20261125.md) | Owns one staged imitation. The box, script act, intentional effect and Temari's thought are distinct layers. |
| China Produce 003 selection failure | Blind and challenger accounts hear clear, steady narration in the whole recovered scene. Three Kanae-coded assets match recorded sound near 43.77, 50.77 and 55.02 s. [Current source](../05_AUDIOVISUAL_ANALYSIS/06_KURAMOTO_CHINA/GKM_CHINA_CARBON_AV_UPDATE_20261125.md) | Generic recorded narrator role. Do not credit it as China dialogue or named in-world Kanae narration. No separate underlying whisper identified. |
| Kotone Dear 037 | Masked phrase near 7944.7 s in first-choice watchalong. The audible continuation extends beyond 7967 s. Post-merge display and a different clean choice establish different scopes. [Current source](../05_AUDIOVISUAL_ANALYSIS/03_FUJITA_KOTONE/GKM_KOTONE_CARBON_AV_UPDATE_20261125.md) | Performance comparison across identical choices/editions remains OPEN. |
| Kanae Dear 004 | The requested `Wonder Scale` reference is declined. In the later open sound check, the paired hearing identifies the tentative opening words of `初`. [Integrated reading](../05_AUDIOVISUAL_ANALYSIS/14_HIWATARI_KANAE/GKM_KANAE_INTEGRATED_AUDIOVISUAL_READING.md#what-kanae-agrees-to-perform) | Preserve the difference between actual song fragment and requested music for an earlier use. |

## Recorded Event 016 parts 2 and 5 — 2026-11-25

Kotone addresses Saki more quietly after music recedes, and moves from bare name to Saki-chan before asking about loneliness. Saki's subsequent refusal to show weakness to Ume is firmer. In the other window, Saki's reverberant reflection precedes the drier exchange with Ume. Both sisters' deliberately assertive delivery and Saki's soft closing encouragement have scene-bounded support. No inferred reciprocal jealousy follows from the delivery. [Intervals and identities](../05_AUDIOVISUAL_ANALYSIS/01_HANAMI_SAKI/GKM_EVENT016_HANAMI_SISTERS_PERCEPTUAL_ADJUDICATION_20261125.md).

## Tsubame’s support-scene shifts — 2026-11-25

| Exact witness | Bounded performed change |
| --- | --- |
| `SRC-0085`, support 2-0056 part 01 | Strong running corrections sharpen into urgent intervention. Tsubame calls for rest, checks responsiveness and offers water. Hiro’s later fragmented speech asks for greater severity. The physical outcome remains open. |
| `SRC-0087`, support 3-0070 part 03 | Tsubame downplays her appearance and later becomes rapid and breathy while identifying the collectible before resuming a formal instruction. Tsubame’s private reason for being there remains open. |
| `SRC-0090`, support 3-0062 part 03 | Stammered interruption contrasts with academic direction. Rinami’s closing assessment is performed inner speech. China’s description of the support speaks for her own experience. |
| `SRC-0092`, support 3-0085 part 03 | Post-wipe exertion gives way to shared encouragement and a renewed audition challenge. The shift concerns these interlocutors in this support episode. |

[Four support-scene adjudications](../05_AUDIOVISUAL_ANALYSIS/13_AMAYA_TSUBAME/GKM_TSUBAME_FOUR_SUPPORT_SCENE_PERCEPTUAL_ADJUDICATION_20261125.md)

## Café recommendations, cinema cover and nickname exchange — 2026-11-25

On SRC-0088 at 127–222 s Lilja’s address stays polite as her recommendation speeds up and grows more emphatic. Tsubame pauses and reconsiders the intended audience of the show. At 234–322.65 s Tsubame stammers first in the excuse and Lilja rushes to corroborate. Their speech remains differentiated. On SRC-0039 at 1174–1225 s Temari moves from a flat example to a falling, puzzled direct address, while Sumika’s comment is lighter. Temari’s laugh and warmer reply follow Kotone’s joking nickname proposal. These are approximate paired listening spans. The sampled picture leaves interframe movements and private motives open. [Perceptual readback](../05_AUDIOVISUAL_ANALYSIS/GKM_CAFE_CINEMA_AND_NICKNAME_PERCEPTUAL_ADJUDICATION_20261125.md).

## Five support-card performed comparisons — 2026-11-25

The exact parent and line locators are in the [current receiving record](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FIVE_SUPPORT_PERCEPTUAL_ADJUDICATION_20261125.md). These support-continuity observations compare continuous heard Japanese and sampled visuals in bounded native-return windows.

- In `2-0018_02`, Saki’s practical instruction, apology and later teasing warmth have different turns. Audience-audible inward protest at 156–160 s belongs to Temari. Her separate spoken retort has a steadier delivery. The source leaves Saki’s motive and physical taping open.
- In `2-0011_02`, Kotone punctuates her refusal around 107–111 s. Polite, extended phrasing surrounds an explicit objection to debt and uncertain income. The underscore continues. Sena’s later vow is her own response after Kotone departs.
- In `1-0004_01`, Rinami’s retry at about 63–75 s is heard as smoother and less forceful than her first acting attempt. Punctuation, box structure, expression and score also change. The evidence supports guided variation within a role, with acoustic measurements, causes and generalized vocal identity open.
- In `3-0071_03`, Tsubame’s response to Student C breaks and warms in a particular recognition scene (L172–173). The students’ earlier and later captions remain unvoiced in the inspected edition. The sound of approach provides no independent speaker personality.
- In `2-0067_02`, Temari privately compares the expressions and later makes a separate spoken comparison. Ume’s teasing rise around 189–194 s and Temari’s subsequent nonlexical voice and denial have different cues. Ume names what she did in her last turn. Its onset as a planned joke remains open.

## Guards on five story-event voice comparisons — 2026-11-25

| Located performance | Observed variation and scope |
| --- | --- |
| [E002-05, 985–1046 s](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-unnamed-friend) | Misuzu’s quiet complaint and Hiro’s drier answer coexist with a warmer discussion of friends as the score changes. Hiro’s actual proposal crosses the upper bound. |
| [E003-02, 585.4–669 s](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-warning-at-the-beach-restaurant) | Mao’s blunt-to-grave warning, Sumika’s hesitation, formal thanks and bright boundary, and Rinami’s peer interruption are distinct deliveries. L540 and L617 carry nonlexical voice. |
| [E003-03, 920.5–1034 s](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#repair-at-the-beach-restaurant) | Mao’s subdued apology, Sumika’s qualified recognition and reciprocal apology, their change of score and the later nickname return belong to the shop meeting. |
| [E004-04, 733.5–931 s](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-coach-becomes-an-opponent) | Lilja’s breathlessness, expressed insistence and later triumphant claim belong to separate rounds. Saki’s instructions explicitly end before competing fully. |
| [E008-02, 246.2–404.6 s](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-fan-and-the-idol-image) | Public enthusiasm, quiet peer corrections, Temari’s effortfully polite invitation, and her quieter inner objection have distinct addressees. The customer’s words are shown as text. |

## Guarded sports-day and Hiroshima delivery — 2026-11-25

**STRENGTHEN.** Misuzu’s pre-race nostalgic turn, Hiro’s worried and then determined voice, China’s address change, and Rinami’s spoken response followed by voiced inward recognition form separate comparisons. Lilja–Temari–Lilja at the sports-day finish are three individually authored, heard inner turns. The effort and race effects sit alongside mixed voices. An unresolved foreground effect and exact musical fade retain separate statuses. [Sports day and Hiroshima adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_SPORTS_DAY_AND_HIROSHIMA_PERCEPTUAL_ADJUDICATION_20261125.md)

## 2026-11-25 recorded delivery in the fever, meal and Shibuya exchanges

The guarded Japanese audio supplies performed contrasts. Mao in fever and Kotone's echo have separate voices. At the meal, Kotone's hesitating approach and Mao's audible L547 reaction prepare, but do not determine the meaning of, Mao's explicit welcome. Sena's concluding laughter and proud challenge follow two juniors' refusal. At Shibuya their later title call is spoken over a soundtrack quotation, distinct from any sung ensemble, and the subsequent reception reaches these characters as reported speech. Sampled facial observations remain qualified. Exact performances in the official trio MV supply a separate mixed studio singing comparison. Distinguish the observed distributions of sung emphasis in that MV from individual spoken title allocation and from the unresolved sung Shibuya event.

[Guarded Event 022 and 024 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_MAO_KOTONE_AND_SHIBUYA_PERCEPTUAL_ADJUDICATION_20261125.md)

## Tsubame receives Mao’s account of her stage — 2026-11-25

The retained support 2-0066 part 01 recording supplies a bounded transition from Tsubame’s raised objection to qualified acceptance of the dragon. Mao offers to change it after explaining the stage image. The voice drop and throat-cleared onset come from separate reported accounts. Timing of the backing under Tsubame’s answer remains **OPEN**. [Costume exchange on the original recording](../05_AUDIOVISUAL_ANALYSIS/13_AMAYA_TSUBAME/GKM_TSUBAME_CARBON_PLAYBACK_SUCCESSOR.md#the-gold-dragon-on-tsubames-costume).

## Guarded Event 023 — 2026-11-25

**STRENGTHEN.** Misuzu's measured giving, gentle remembered request and brighter gift response distinguish present and remembered settings. Temari's quick disagreement precedes hesitant help-seeking. Hiro's support and dry report have separate delivery and audiences. The Temari and remembered Misuzu reverb disputes stay open. [Guarded Event 023 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_EVENT_023_PRIVATE_PERFORMANCE_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded care, chosen company and a summer photograph — 2026-11-25

**STRENGTHEN.** The contexts distinguish Mao’s projected polite reply, weakened reassurance, inward recognition of avoidance and later outward admission. Kotone’s directions and sibling-care explanation have guarded witnesses. In the separate beach scene a shutter effect marks a change from voiced thought for the player to present conversation. [Guarded care and summer adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_MAO_CARE_AND_LAST_SUMMER_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded comparisons of the Hanami sisters — 2026-11-25

**STRENGTHEN.** Saki speaks a lyric about an unseen future, then sets an audience goal and asks the group to rest. The listening scope includes the ending of her earlier conclusion. It leaves its opening outside the window. Ume says an idol should answer her own expectations and addresses herself by her full name. The scenario has no inward flag. Who else heard the turn remains open. Ume’s support part 01 recollection distinguishes following Saki from dreaming specifically of idolhood. Ume affirms her trust and says she wants to find her own answer. The onset of that aspiration remains undated. The next scene’s opening Saki call belongs to support part 02. [Guarded Event 026 and support comparison](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_HANAMI_SISTERS_EVENT_026_AND_SUPPORT_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded council speech — Event 025

China accepts responsibility for the paperwork lapse and explains Ume’s assistance. She later asks the seniors for a chance for all three juniors to answer their concerns. The two guarded scenes distinguish her earlier apology from the later request. Tsubame directs Ume to finish collecting the paperwork. Her recorded recollection of entrusting the school to the juniors differs from her present questions about their readiness. Her concern leaves the graduation decision outside this exchange. China promises to become a dependable president by spring and then asks Ume and Misuzu for continued help. The proposal to widen their group and invite Hiro is prospective. [Guarded Event 025 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_EVENT_025_COUNCIL_SUCCESSION_PERCEPTUAL_ADJUDICATION_20261125.md) The exact final sound of the L517 promise and the individual voices in the group calls remain distinct from the corresponding caption and authored take assignments.
