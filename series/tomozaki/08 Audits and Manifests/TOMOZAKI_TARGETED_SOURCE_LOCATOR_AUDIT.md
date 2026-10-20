---
series: TOMOZAKI
artifact_type: targeted_source_locator_audit
scope: ESC_01_TO_ESC_12_AT_V11_BOUNDARY
source_boundary: "Locked Japanese V01–V11 plus story-locally routed V06.5/V08.5; no later or adaptation source"
analytical_generation: V2_REMEDIATION
generation: V1.0
status: canonical
release_state: mutable_active
created: "2026-09-13"
review_state: INDEPENDENT_REVIEW_PASS
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
execution_reasoning_control: Max
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Tomozaki — targeted Japanese source-locator audit

## 1. Responsibility and scope

This audit supplies the missing L2/L3 retrieval layer for **ESC-01–ESC-12** in the [claim-revision/evidence index](../03%20Longitudinal%20Ledgers/TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md#13-l2l3-source-escalation-queue). It records exact locked witnesses, recoverable package locations, minimal diagnostic wording, attribution, interpretive disposition, and unresolved limits. It complements the [Japanese voice/register/key-terms ledger](../03%20Longitudinal%20Ledgers/TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md); it is neither a new sequential reading nor an independent character or thematic synthesis.

The [method](../00%20Frameworks%20and%20Methods/TOMOZAKI_ANALYTICAL_METHOD.md), [architecture](../00%20Frameworks%20and%20Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md), and [source lock](../01%20Source%20Lock%20and%20Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md) govern this operation. The source-facing readings remain immutable historical states. A correction below changes a current downstream formulation, not the earlier reading's recorded horizon. The current R01–R03 authorization permits evidence reconciliation; it does not promote provisional monographs or authorize full-series rewriting.

**Retrieval and independent source/semantic review: PASS for all twelve queues.** Propagation into the mutable owners and repository publication remain separate completion requirements. A retrieved passage can establish that a question remains unanswerable. In particular, the school-year conflict discovered here is an actual unresolved source tension, not a failed search.

## 2. Witness integrity receipt

The source is the read-only local mirror of the source-lock witnesses. Before this authoring pass, the local `audit_manifest.json` SHA-256 was reverified as `64e5e9e722a24f578abc20b3de1b61269c1212e224b60786e7eab28d35b66257`, matching the source lock. All thirteen EPUB byte sizes and SHA-256 values matched that manifest; all thirteen ZIP CRC tests passed.

The table is an **operation receipt**, not a competing source inventory. Normalized filename and Drive-object identity remain owned by source-lock §4: `Bottom-Tier Character Tomozaki - Volume NN.epub`, with `.5` retained for supplements and the V07 exception `Bottom-Tier Character Tomozaki - Volume 07 - Special Edition.epub`. V07 evidence here is main-novel prose; its art-work extras supply no literary claims. The known V04/V11 mimetype-order warnings do not change the passed byte/CRC checks. Hash verification of V06.5 does not mean its image-only diary was reread in this operation.

| Witness | Bytes | SHA-256 | Verification |
|---|---:|---|---|
| V01 | 1366208 | `49d1577da47a22e0838b8430a52bfe24639effcfb519786149cba7ed1d0bc0c4` | MATCH / CRC PASS |
| V02 | 1951446 | `9eac14b30b4192e41c901e8194e7ab99e306ef8b6226cf8fa18ee71b75a57c5c` | MATCH / CRC PASS |
| V03 | 2293020 | `5672493f7007900154601a990bd205c7b24f1d502305dee14d21d4313f2f517d` | MATCH / CRC PASS |
| V04 | 20091317 | `7c6425a95c81aa9c917d1437ec1c40ea00011f8e846815f896f4d00303b03c11` | MATCH / CRC PASS |
| V05 | 4527468 | `f43355c286c8b33db529febb6389cb08fa9ef5a65a7e13e3c2a8490214965e89` | MATCH / CRC PASS |
| V06 | 3513283 | `b61815bb4077ce8cd2ae81413580fe3918638814fad55a2593d0327fbd002c43` | MATCH / CRC PASS |
| V06.5 | 4878698 | `8a5a1eedf1d0ae51d3c0f8a797ee33079139b1a5b0dbbf29a9e4593998fe77dd` | MATCH / CRC PASS |
| V07 | 9074460 | `055892e6b5378e0f1df7682a4e53a56ae4c6b67105fcefa771a51da1c899f205` | MATCH / CRC PASS |
| V08 | 4206304 | `05c238aeb33ed48ffe47ed1c9ba339c6d0e0e2a7b0dd32f78b166f46460de49e` | MATCH / CRC PASS |
| V08.5 | 4678504 | `59862bdcd7f0b885277dd3b6002116fa5b263dfb510089ecbc47fa697628a5dc` | MATCH / CRC PASS |
| V09 | 3576551 | `5740b7a68999f70daee42fd9235d88d68d9911a73dc7c02e59658de49bcf334d` | MATCH / CRC PASS |
| V10 | 3205928 | `316d510c2062119a1d3b77e3bb1cb6746340479db07c16579504bd1d5060b2d7` | MATCH / CRC PASS |
| V11 | 9177296 | `c8f3fa288d426c0f2c2e2816366df4d636492ff4ec5bcb71d2a7b79bdba12141` | MATCH / CRC PASS |

## 3. Locator convention and evidence classes

`VNN / exact ZIP member / Pn` identifies a passage in the verified EPUB, not a print page, EPUB CFI, sentence number, or original publisher paragraph ID. **P is a one-based enumeration of every HTML `<p>` element in document order, including empty and image-only paragraphs.** It resets in each ZIP member. A range identifies the reviewed local context; a marker identifies a short diagnostic string within it. HTML and XHTML extensions and case are retained exactly.

Reproduction uses BeautifulSoup's `html.parser`, `find_all('p')`, and one-based enumeration. For diagnostic text only, remove ruby `rt`/`rp` elements and concatenate each paragraph's `stripped_strings`. Removing ruby does not alter the paragraph count. Paragraph locations are edition-bound; they are not portable to another acquisition. The exact member plus short marker remains usable even without reproducing this enumeration. No source extraction, media, or image was added to the analytical corpus.

Labels below distinguish **SPEECH** (an attested utterance), **WRITTEN** (message/profile/manuscript wording), **NARRATION** (the telling voice), **INTERIOR** (represented thought), **INFERENCE** (an observer's or analyst's interpretation), and **OPEN** (not determined). “Direct” means direct evidence of the represented act or statement; it does not certify every proposition the character asserts. Unless separately specified, main-volume scenes are at that volume's current diegetic point and Tomozaki is the observer. V08.5's middle-school sequence is retrospective reader access, not an extra event after V08.

The DR/SR aliases and exact frozen reading links are owned by [claim-index §4](../03%20Longitudinal%20Ledgers/TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md#4-deterministic-l1-route-key). Each queue retains that L1 route and adds evidence below. Context ranges are deliberately selective: this audit does not claim sentence-by-sentence verification of every proposition in each reading.

## 4. Queue adjudications

### ESC-01 — modes, self-theory, and NO NAME

**Route:** `CRI-HIN-004`; SR08.5 §§8, 14; DR10 §§4.1, 8; DR11 §§4.2, 8.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-01A | V08.5 `text/part0017.html` P1–26 | P4 `誰でもない`; P18 `Aoi`; P26 `NO NAME` | Middle-school Hinami-centered narration and first-person interiority; renaming follows self-negation and a new competitive purpose. The “real self died” account is a self-theory, not literal death or a diagnosis. P25–26 prospectively separates this moment from meeting Tomozaki. |
| LOC-01B | V10 `text/part0015.html` P206–208; `text/part0018.html` P568–575 | P575 `もう一つの仮面` | Tomozaki's reconsideration of the private NO NAME mode. The second-mask model is observer inference; privileged access is not final access to a true essence. |
| LOC-01C | V11 `item/xhtml/p-0013.xhtml` P185–209 | P185 `私は、空っぽ` | Hinami's spoken self-description in the post-video rupture, received by Tomozaki. It does not erase demonstrated competence, attachment, or effects on others. |

**REVISE / retrieval PASS.** Keep retrospective self-theory, present private performance, and observer reconstruction distinct. The V08.5 formation scene is not automatically shared knowledge at its disclosure point. Nor does this audit establish that every detail remains unknown to Tomozaki after V11's later disclosure; actor access requires a particular communication route.

### ESC-02 — Nagisa, causal alternatives, and the school-year tension

**Route:** `CRI-EPI-002`, `CRI-OQ-HIN-001`; DR10 §§4.3–4.4, 8 and especially its directly relevant §4.6; DR11 §§4.3–4.5, 7–9.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-02A | V10 `text/part0024.html` P126–178 | P139 `渚が小学六年生`; P170 `んだって` | Hinami tells Tomozaki about three sisters, bullying, death, and the driver's account. Road entry is reported testimony, not an eyewitness scene narrated from Nagisa's mind. |
| LOC-02B | V10 `text/part0026.html` P1–33 | P5 `事故なのか、自殺なのか`; P8 `私にはわからない`; P17 `理由も原因もわからない` | Hinami explicitly presents alternatives and states inability to determine cause. Tomozaki recognizes the limits of his own understanding. Neither option becomes the audit's finding. |
| LOC-02C | V11 `item/xhtml/p-0030.xhtml` P826–827, P985–1018 | P826 `葵が小学六年生`; P827 `二つ年下`; P1010 `小学六年生と三年生` | Retrospective narration places Aoi in sixth grade, Nagisa two years younger, then identifies Aoi/Haruka as sixth/third graders at the hospital. The bullying-to-hospital sequence omits the road entry itself. |

**REVISE / retrieval PASS; chronology and causation OPEN.** V10's Nagisa-sixth-grade statement and V11's Aoi-sixth-grade account are incompatible as an unqualified single school-year timeline. Record `GENUINE_TEXTUAL_TENSION`; do not correct either locked witness, invent a date, or claim an authorized edition correction. A simple “Nagisa was in sixth grade” current formulation must be qualified as V10's account. A simple “Nagisa was in fourth grade” would likewise erase the conflicting testimony.

Both sources support a younger sister's bullying-related history, her death, and Hinami's inability to recover the decisive cause. The temporal adjacency and last distressed speech strengthen contextual explanation but do not determine intent, medical mechanism, a responsible individual, or singular causation of Hinami's whole personality.

### ESC-03 — inherited meaning and retrospective narrative person

**Route:** `CRI-HIN-002`; DR11 §§4.3–4.6, 8.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-03A | V11 `item/xhtml/p-0030.xhtml` P721–750 | P722 `私は。ね`; P733 `日南葵は` | Hinami begins to speak in the present frame; a section break precedes third-person Aoi-centered childhood narration. The entire following sequence is not a verbatim first-person speech transcript. |
| LOC-03B | V11 `item/xhtml/p-0030.xhtml` P1025–1076 | P1030 `これにも意味がある`; P1064 `本気で言ってるの` | Yoko's hospital speech assigns meaning to the death; Aoi directly challenges her. Narration also preserves Yoko's tears/care and considers that she may be using the belief to bear pain. Her love and the damaging explanatory form coexist. |
| LOC-03C | V11 `item/xhtml/p-0030.xhtml` P1092–1096 → `item/xhtml/p-0032.xhtml` P1–16 | P1092 `思えば私は`; following P9 `私のまんなか` | The represented sequence moves into first-person self-accusation/interiority. This is a mixed-person disclosure-framed retrospective, not simply third-person throughout either. |

**REVISE attribution / retrieval PASS.** The frozen DR11 formulation “first-person, internally focalized history” is too coarse for current reuse. The source grants reader access to a retrospectively represented inner process through changing narrative person. That does not prove every narrated qualification was literally spoken to Tomozaki. Yoko's words establish a depicted familial meaning practice, not a named religion, doctrine, cult, or supernatural truth. Aoi's rejection supplies strong formation evidence without becoming an omniscient moral verdict on every family interaction.

### ESC-04 — belief instruction and the defeated credential

**Route:** `CRI-REL-001`; DR11 §§4.7–4.8, 6–8.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-04A | V11 `item/xhtml/p-0032.xhtml` P153–194 | P169 `俺を信じろ`; P174 `唯一勝てなかった` | Tomozaki tells Hinami to believe him, grounding the instruction in the opponent she could not defeat. Plain imperative, first-person self-warrant, and competitive credential are all explicit. His declared lack of logical grounds does not remove that practical credential. |
| LOC-04B | V11 `item/xhtml/p-0032.xhtml` P256–257, P307, P350–352, P414–442 | P256 `三先`; P429 `あなたを信じる理由はなくなった`; P442 `人生は──クソゲーよ` | The agreed first-to-three set reaches two-all after Tomozaki's first two wins. After Boxman's final victory over Jack, Hinami rejects the stated reason and delivers the bad-game verdict. These are her addressed conclusions in crisis, not omniscient proof about life. |

**STRENGTHEN / retrieval PASS.** The result tests this warrant in this set. It does not demonstrate permanent skill hierarchy, universal worth, completed reconciliation, or the impossibility of care. Match contact and personal knowledge can coexist with rejection of the proposed authority.

### ESC-05 — V03 refusal and negotiated coaching terms

**Route:** `CRI-TOM-003`; DR03 §§10–12, 18–20; DR04 §2.3.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-05A | V03 `text/part0029.html` P297–372 | P333 `優先したい`; P364 `そもそもおかしい` | Tomozaki questions the priority of tactics and assigned objectives in deciding whether to confess. Hinami counters with an account of unstable desire and productive action. The objection concerns governing ends, not lack of technical feasibility alone. |
| LOC-05B | V03 `text/part0033.html` P293–315 | P300 `なしにしたい`; P301 `『目標』を作っていきたい`; P306 `ハイブリッド` | Tomozaki proposes excluding conflicting objectives; Hinami restates his proposed structure. Their NO NAME/nanashi exchange and gesture follow negotiation. A request and provisional working accommodation are supported; comprehensive equal governance is not. |

**PRESERVE with modality limits / retrieval PASS.** The repeated desiderative does real negotiating work. It does not instantly transfer all curriculum control, certify all future goals as owned, or prevent V09/V11 reversals. Skills remain valued as means; the disagreement is not cured by abandoning technique.

### ESC-06 — revenge, victory, and the Tama exception

**Route:** `CRI-HIN-003`; DR06 §§4–5, 16–19.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-06A | V06 `OEBPS/Text/part0008.xhtml` P97–105 | P103 `私の勝ち` | Hinami's written victory message to Tomozaki after her first individual-game win. P100 explicitly preserves his greater-than-90-percent win rate. It is personal competitive communication, not a won set or her ethical verdict on the harassment intervention. |
| LOC-06B | V06 `OEBPS/Text/part0008.xhtml` P202–210 | P202 `死体蹴り` | Tomozaki's spoken label for continuing punishment past the protective stopping point; narration at P210 records Hinami's acknowledgment. The metaphor and acknowledgment do not equal apology or restitution. |
| LOC-06C | V06 `OEBPS/Text/part0008.xhtml` P249 | `正しくて`; `自分を貫いている`; `好きなの` | Hinami explains to Tomozaki her valuation of Tama's uncalculated resistance. The attachment has explicit personal-evaluative content; it does not establish that every later act is reducible to this exception. |

**STRENGTHEN / retrieval PASS.** Winning, morally admiring a person, and justifying intervention belong to different acts. The lexeme “correct” must retain its local object and speaker. Hinami can recognize the extra attack while continuing to defend her larger approach.

### ESC-07 — romantic disclosure, normality, and future freedom

**Route:** `CRI-MIM-003`; DR06 §13, §§17–20; DR07 §§5–6, 12, 18–21.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-07A | V06 `OEBPS/Text/part0029.xhtml` P583–596 | P592 `そーいう意味の好き` | Mimimi first makes Tomozaki doubt the romantic reading, then confirms that reading. The tease carries actual disclosure; it is not a request to date or proof of reciprocity. |
| LOC-07B | V07 `OEBPS/Text/part0009.xhtml` P624–631 | P626 `忘れて`; P628 `いつもどおり` | Mimimi qualifies that she is not asking him to forget; she asks for ordinary interaction and he acknowledges. Preserve the negative qualification around the first marker. |
| LOC-07C | V07 `OEBPS/Text/part0031.xhtml` P139–169 | P151 `まだ好き`; P167 `いつまでも好きでいると思ったら大間違い` | After Tomozaki selects Kikuchi, Mimimi acknowledges continuing love while refusing a presumed permanent future. The playful insult and role nickname do not cancel the boundary. |

**PRESERVE / retrieval PASS; terminal pursuit rule OPEN.** Disclosure, conduct accommodation, and eventual non-selection are separate stages. Acknowledging her V06 feeling is not reciprocal confession. P167 protects future freedom; it specifies neither a deadline nor a later cessation of love. Supplementary private focalization does not retroactively communicate additional feelings to Tomozaki.

### ESC-08 — request, acceptance, and mutual reselection

**Route:** `CRI-REL-002`; DR07 §§13–15, 20; DR09 §§4.1–4.2, 6–9.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-08A | V07 `OEBPS/Text/part0029.xhtml` P311–377 | P319 `俺と付き合ってほしい`; P373 `鍵を開ける` | Tomozaki directly requests dating, then argues through their shared fictional analogy. Kikuchi smiles, nods, and answers through that analogy. The sequence supports acceptance; an invented separate literal “yes” is unnecessary. |
| LOC-08B | V09 `text/part0031.html` P117–168 | P127 `私は、友崎くんがいいです`; P132 `選ばせてください` | Kikuchi explicitly selects Tomozaki and asks to participate in choosing. She initiates hand contact; he responds affectively and physically. Polite grammar carries initiative, not passive acquiescence. |

**STRENGTHEN / retrieval PASS; durable governance OPEN.** The V07 request is not the final solution to asymmetry. V09 changes the distribution of choice while retaining separate interests and a still-developing practice. Neither literary complementarity nor touch establishes exhaustive future consent, privacy, or allocation rules.

### ESC-09 — loneliness, specialness, and unspoken qualification

**Route:** `CRI-REL-003`; DR09 §4.6, §§6–9; DR10 §§4.1–4.2, 6–9; DR11 §§5.1–5.3.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-09A | V09 `text/part0020.html` P625 | `私は、寂しくても平気` | Hinami's self-report to Tomozaki tolerates the condition of loneliness. The concessive does not mean she never feels it, nor does it request rescue. |
| LOC-09B | V10 `text/part0012.html` P396–401; `text/part0017.html` P146–147 | P396 `特別な存在`; later P146 `不誠実` | Tomozaki identifies Hinami as special in addressed speech to Mizusawa with Kikuchi present; later narration describes the conflict of holding a non-partner uniquely special. This is a bounded disclosure discussion, not public dissemination. The evaluative term is his interpretation, not a narratorial certification of a romantic category. |
| LOC-09C | V11 `item/xhtml/p-0019.xhtml` P237–242 | P239 `うん。好きだよ`; P240 `一人の人間として` | Haruka asks; Tomozaki says he likes Hinami. The as-a-person qualification is **unspoken narration**, which he decides need not be added. Do not attribute it to what Haruka hears. |

**REVISE attribution / retrieval PASS; romantic classification OPEN.** Lexical salience establishes meaningful attachment, but the same liking vocabulary can operate in distinct familial, romantic, admiring, and friendly acts. Context, qualification, and recipient matter. This audit establishes neither destined romance nor permanent non-romance.

### ESC-10 — fiction, authorial motive, and Haruka's reception

**Route:** `CRI-EPI-001`, `CRI-KIK-002`; DR11 §§4.4, 4.9–4.10, 6–9.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-10A | V11 `item/xhtml/p-0023.xhtml` P171–203 → `item/xhtml/p-0025.xhtml` P1–17 | P200 `神様を失ってしまった`; following P11 `おそらくは` | Kikuchi's addressed interpretation of Hinami is followed by Haruka's tears. Tomozaki infers the memory activated by those words; the precise content of Haruka's inner causal response is not independently confessed there. |
| LOC-10B | V11 `item/xhtml/p-0025.xhtml` P118–146 | P118 `抉ってしまった`; P146 `理由がない` | Kikuchi acknowledges hurting a younger girl through inquiry and says liking writing has not supplied the needed further reason. Self-acknowledgment is stronger than an analyst merely imputing motive, but it does not settle a consent rule. |
| LOC-10C | V11 `item/xhtml/p-0033.xhtml` P176–188, P261–272, P313–321, P419–448, P510–515 | P272 `無が無になる`; P321 `私は信じられるものがない` | Tomozaki opens Kikuchi's posted work; the Alcia-centered story depicts an inner crisis and inability to lose, then affects its reader. The fictional inner event is authored evidence about Kikuchi's model, not Hinami testimony. |
| LOC-10D | V11 `item/xhtml/p-0033.xhtml` P599–611 | P602 `書く理由`; P611 `私だけの理由` | Kikuchi explicitly says her own reason remains unfound and proposes beginning from the reason Tomozaki offers while searching for hers. The future plan is not a completed vocational settlement. |

**PRESERVE evidence layers / retrieval PASS; ethics and publication outcome OPEN.** The artwork's power to reach Tomozaki is an observed reception consequence. Its represented death-adjacent thought belongs to Alcia's fictional interior; it cannot establish Hinami's suicidal intent or Nagisa's intent. Haruka's distress is observed, its specific mechanism partly inferred. Neither accuracy nor helpful reception supplies permission to expose a recognizable person.

### ESC-11 — privacy, bodily refusal, and disclosure rights

**Route:** `CRI-REL-004`; DR08 §4.6, §§6–10; DR09 §§4.1–4.2, 6–9; DR10 §§4.2–4.3, 6–9; DR11 §5.3, §8.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-11A | V08 `text/part0035.html` P133–150 → V09 `text/part0010.html` P19–40 | V08 P135 `スマホを手に取っている`; V09 P39 `携帯を勝手に見る` | Tomozaki finds Kikuchi holding his phone; the following volume separately names the privacy wrong. The message and her departure do not prove the sexual inference she fears. No intimate image or explicit message is reproduced here. |
| LOC-11B | V09 `text/part0010.html` P274–287 → `text/part0016.html` P47–54 → `text/part0018.html` P164–175 | P274 `文面`; later P175 `触った` | Tomozaki's written request targets sudden message wording. Later image/contact behavior demonstrates why that narrow rule does not establish broad compliance. These are separate incidents; the audit does not convert inward protest into an outwardly stated prohibition. |
| LOC-11C | V10 `text/part0012.html` P377–401 | P377 `話す権利`; P401 `権利を侵害する` | Tomozaki states he lacks the right, then speaks Hinami's private history to Mizusawa with Kikuchi present. The rights-violation formulation at P401 is narration; specialness is his stated reason for proceeding, not Hinami's authorization. |
| LOC-11D | V11 `item/xhtml/p-0028.xhtml` P230–239 | P232 `すぐに払った`; P233 `やめてください`; P239 `彼女なので` | Rena takes Tomozaki's arm; he immediately brushes it away. Kikuchi then voices refusal and her relationship standing. Her stammer and polite form coexist with explicit agency. |
| LOC-11E | V11 `item/xhtml/p-0033.xhtml` P76–98 | P97 `届いてないんですね`; P98 `切れてしまった電話` | Kikuchi names failed reception of her words; the call then ends. The passage does not explicitly identify who disconnects it. |
| LOC-11F | V08 `text/part0017.html` P509–547; `text/part0028.html` P52–79 | In the call P52 `好きな相手となら`; P60 `うん。全然ならない`; P70 `土曜日は予定ある` | Earlier bodily proximity and renegotiated address are followed by Rena's sexualized call. Tomozaki immediately denies wanting that contact with her; narration preserves his unsettled response. He separately declines a Saturday invitation because of existing plans and Rena withdraws that invitation. His refusal is real but neither an absence of arousal nor a comprehensive contact rule. |

**REVISE precision / retrieval PASS; general rules OPEN.** Keep phone access, immediate V08 refusal, narrow V09 message refusal, unwelcome contact, third-party disclosure, and couple conflict distinct. The V08 phone endpoint and V09 apology conversation do not demonstrate exhaustive onward disclosure to Kikuchi of every earlier touch, invitation, or internal response. Tomozaki's candid ownership of a breach is not its ethical justification. Rena's broad internalized compliance is not established by one brushed-away contact. The source supports Kikuchi's resistance without requiring a categorical “she hung up” claim.

### ESC-12 — local atmosphere, status, and punishment

**Route:** `CRI-SOC-001`; DR01 §§7, 21 and its directly relevant §9; DR02 §§8–10, 28; DR04 §§7–10, 18; DR05 §§8–10, 17.

| Locator ID | Exact source / context | Minimal diagnostic | Attribution and supported distinction |
|---|---|---|---|
| LOC-12A | V01 `text/part0023.html` P191–197 | P191 `その場における善悪の基準` | Hinami defines atmosphere to Tomozaki as local evaluative standards. This is her explicit model, not universal narrator-certified morality. |
| LOC-12B | V02 `text/part0013.html` P142–208; `text/part0021.html` P184–241 | P142 `空気を操る`; P241 `別の土俵を作る` | Hinami proposes graded practice; Tomozaki later characterizes his electoral strategy as changing the competitive ground. The move from interpersonal to school-scale coordination preserves context rather than proving total control. |
| LOC-12C | V04 `OEBPS/Text/p-0012.xhtml` P30–60 | P46 `準備が得意`; P56 `私、やります` | Konno's labeling and supporters' responses pressure Hirabayashi toward volunteering. Tomozaki interprets the status mechanism; the teacher explicitly questions coercion at P58. Formal assent is therefore insufficient evidence of unconstrained choice. |
| LOC-12D | V05 `text/part0014.html` P34–48 | P34 `免罪符`; P46 `罰` | Mizusawa explains attack pretexts; **Tomozaki** supplies the attack-to-punishment wording at P46, and Mizusawa agrees at P47. Preserve the co-developed formulation. |
| LOC-12E | V05 `text/part0026.html` P173–200, P237–273 | P200 `正義`; P241 `たまだけに`; P256 `一番の被害者` | Tomozaki narrates punitive crowd escalation. Tama's joke and stop appeal receive ratification from previously befriended girls and a male sports-group member. Local affiliation, delivery, and the victim's standing support the change; a joke does not universally dissolve aggression. |

**REVISE attribution; STRENGTHEN contextual scope / retrieval PASS.** A field mechanism emerges across scenes, but observers' explanatory language is not every actor's motive or a moral endorsement of punishment. Stopping the crowd does not establish apology, restitution, durable accountability, or generalized reform by Konno/Akiyama.

## 5. Supplemental voice-locator records

These records support the voice ledger without enlarging the twelve claim queues into a full source reread.

| Locator ID | Exact source / context | Diagnostic and evidence limit |
|---|---|---|
| LOC-V01 | V01 `text/part0018.html` P42–52; `text/part0020.html` P19 | Tomozaki's spoken `共感能力` comment and subsequent differentiation of Mimimi/Tama. Abstract observation enters ordinary speech; its success is recipient-conditioned. |
| LOC-V02 | V02 `text/part0031.html` P2–7 | Tama's `私のヒーロー` addressed to Mimimi. Personal valuation particularizes an attachment; it does not replace every public ranking system. |
| LOC-V03 | V04 `OEBPS/Text/p-0012.xhtml` P15–22 | P18 `キャプテンやりたくないっていうか` — Yuzu contests Konno's proposed assignment. Her hesitation and refusal coexist; this is not extrapolated into a universal idiolect. |
| LOC-V04 | V05 `text/part0014.html` P468–515; `text/part0017.html` P49–99 | Mizusawa's `一貫した隙` model, then the joint discussion of Tama practicing borrowed speech and recorded feedback. A proposed presentation mechanism is not a diagnosis of false personality. |
| LOC-V05 | V07 `OEBPS/Text/part0020.xhtml` P885 | Kikuchi's `作家志望` is a written SNS profile label, not a spoken catchphrase. |
| LOC-V06 | V09 `text/part0015.html` P128–148 | Mimimi's P135 `二人で帰ったりしないほうがよさそー` is a locally hedged restraint proposal in the Kita-Yono scene; P148 follows with her departure announcement. No terminal no-contact rule. |
| LOC-V08 | V01 `text/part0031.html` P27–35 | Tomozaki's spoken `少なくとも絶対に、良ゲー`, addressed to Yuzu, qualifies his new evaluation: he has not simply adopted Hinami's maximal good-game verdict. Yuzu's response follows at P29–35. |
| LOC-V09 | V09 `text/part0010.html` P1–11 | Yuzu's P7 `私たちはお先に` closes her and Nakamura's engineered introduction of the couple to a repair conversation. A cheerful social formula coexists with a deliberate intervention; it supplies no general proof of consent to that setup. |
| LOC-V10 | V11 `item/xhtml/p-0021.xhtml` P195–215 | Mizusawa's P209 `幼稚なヒーロー願望かもしれねー` qualifies his account of why Hinami matters to him. Direct self-examination remains a hypothesis about his motive, not definitive access to Hinami's feelings. |
| LOC-V07 | V11 `item/xhtml/p-0016.xhtml` P43–70 | Mimimi distinguishes confidence in `スペック` at P43 from confidence in `『私』そのもの` at P53, in the group with Tomozaki, Kikuchi, and Mizusawa present; P58–64 identifies the participating listeners. It is direct self-report at this state, not evidence she lacks all competence or all confidence. |

## 6. Correction and propagation register

| Correction ID | Current formulation to retire or qualify | Surviving formulation / conflict class | Affected cumulative route |
|---|---|---|---|
| COR-01 | Unqualified sixth-grade placement for Nagisa across both volumes | V10 attributes sixth grade to Nagisa; V11 to Aoi. `GENUINE_TEXTUAL_TENSION / OPEN`. | `CRI-EPI-002`, `CRI-OQ-HIN-001`; Hinami/Nagisa character rows; family/causality and effort-history uses. |
| COR-02 | Entire V11 family history as first-person spoken testimony | Disclosure-framed mixed-person retrospective with internal access. `FOCALIZATION_LIMIT / KNOWLEDGE_STATE_DIFFERENCE`. | Hinami family/self-theory rows in character, relationship, claim, social and effort owners; later monograph/specialist handoff. |
| COR-03 | Tomozaki says “as a person” to Haruka | Spoken liking plus unspoken qualification. `FOCALIZATION_LIMIT`. | `CRI-REL-003`; Tomozaki–Hinami/Haruka relational and character state. |
| COR-04 | Explicit certainty that Kikuchi hangs up | Her failed-reception statement precedes the ended call; disconnect actor unspecified. `OPEN` action attribution. | Kikuchi agency and Tomozaki failure rows; relationship repair state. |
| COR-05 | Mizusawa speaks the exact attack-to-punishment sentence | His account is reformulated by Tomozaki and ratified by him. `ATTRIBUTION_CORRECTION`. | `CRI-SOC-001`; V05 social-system and peer-coaching cases. |
| COR-06 | Every V08.5 private detail categorically unknown to Tomozaki even after V11 | Supplemental reader access is not automatic actor access; assess any later disclosure specifically. `KNOWLEDGE_STATE_DIFFERENCE`. | `CRI-SRC-001`; relationship knowledge fields and Hinami formation rows. |

This audit supplies the corrections; the [longitudinal reconciliation audit](TOMOZAKI_LONGITUDINAL_RECONCILIATION_AUDIT.md) owns the propagation receipt required by the [execution inventory](TOMOZAKI_REMEDIATION_EXECUTION_INVENTORY.md#33-create-the-missing-verification-layer). Frozen readings preserve their historical wording; future literary work must route through the corrected current spine.

## 7. Completion and remaining limits

Author checks establish twelve distinct queue adjudications, exact locked-member routes, diagnostic wording with attribution, and explicit residual questions. The voice ledger supplies an evidence-proportionate home for the seven principals; its additional records share this locator convention. Independent parent review reopened source context across all twelve queues and all ten supplemental records, including LOC-11F's V08 call. It inspected and reran the mechanical verification of thirteen witness hashes/byte sizes/CRCs and 92 paragraph-specific diagnostic strings. Semantic review supplied the recipient corrections now incorporated in LOC-V08/JVL-02 (Yuzu) and LOC-V07/JVL-18 (the group including Tomozaki, Kikuchi, and Mizusawa). **Independent review PASS** records that bounded source and attribution review, not an exhaustive rereading or repository-publication verdict.

**Still OPEN as literature:** Nagisa's immediate cause/intent and school-year chronology; Hinami's affirmative future goal and consent to intervention; romantic classification of exceptional attachment; durable couple governance; terminal pursuit/stopping rules; Rena's general compliance; creative consent and publication outcomes; accountability for earlier harm. None prevents a truthful retrieval PASS. None can be closed by a hash match, a filename, or a mature-looking ledger.

No later volume, adaptation, translation, external commentary, or remembered canon was admitted. No Japanese habitual register, universal address rule, psychiatric diagnosis, named religious affiliation, invented quotation, print page, or EPUB CFI is established here. This audit does not certify the separate specialist, monograph, full-series, or repository-publication gates.
