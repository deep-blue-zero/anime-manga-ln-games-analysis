---
title: "Peach Girl — Directional Relationships and Commitments"
artifact_id: PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER
artifact_type: relationship_commitment_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.3"
status: active_provisional
scope: "Directional Relationships and Commitments; source-derived records through the committed high-water mark named in the entrypoint"
source_boundary: "Original Japanese 新装版 mainline; admitted volumes through the entrypoint's committed high-water mark; prospective rows carry their own frontier"
canonical_home: series/peach-girl/03 Longitudinal Ledgers/PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Directional Relationships and Commitments

This instrument owns directional relationship state and offers, answers, commitments and transitions affecting that state. It separates affection/attraction from relationship labels and actual agreements. It does not own an actor's general personality, circulating propositions or the full argument for a motive. Those homes are linked by ID.

A romantic, friendly, familial, rivalrous, dependent or unresolved relation is classified only when evidence supports it. No pair or relationship type is assumed at initialization.

## Records and allocation

| Type / stable identifier | Required fields |
| --- | --- |
| Directional event `PG-RL-####` | From/to local subject IDs; prior row/version; continuity; represented time/certainty; learned-after frontier; setting/audience; expressed feeling/label; observed conduct; inferred attachment or motive with alternative; what each participant understands; actual transition and consequences; observation refs; claim/version; confidence/basis; correction link |
| Commitment/boundary event `PG-CM-####` | Participants and direction; exact offer/request/limit; answer or no evidenced answer; scope and conditions; knowledge link; acceptance evidence; actual conduct/permission/consequence; status; time/frontier; observations/claim; prior/revision link |
| Current directional view | Ordered pair + temporal/disclosure boundary; active RL/CM versions; private and public descriptions; reciprocity known/unknown; unresolved disagreements |

Commitment states may be `PROPOSED / ACCEPTED_WITH_EVIDENCE / DECLINED / AMBIGUOUS / BREACHED_WITH_EVIDENCE / WITHDRAWN / ENDED`. State the particular commitment and evidence; silence, attraction or the analyst's preferred label does not establish an agreement or breach. Public presentation and private understanding can differ. A statement of exclusivity, inferred expectation and reciprocal commitment must remain separately retrievable.

Direction matters: A→B does not establish B→A. A dyadic record can link both directional events, but cannot erase asymmetric access. A later reciprocal relation does not establish earlier consent or the same prior feeling. Nonromantic intimacy is permitted; explicit romantic evidence cannot be relabeled without a supported reason.

## Evidence, update and history

Allocate monotonically numbered IDs on actual admitted observations; never reuse a retired ID. Each event cites `PG-EV-VNN-####` with witness/page/panel and learned-after frontier. Track action, attributed statement and inference separately, with `HIGH / MODERATE / LOW / UNRESOLVED` support and basis. Unknown participant understanding remains unknown; link `PG-KN` rather than inventing it.

A future VNN transaction appends material changes in affection, affiliation, trust, jealousy, dependency, approach/withdrawal, relationship classification, promises, boundaries, rupture or repair. A source-supported stable relationship can receive an initial event; lack of change alone does not require a new row. Link actor-level choices in `PG-CS`, audience reputation in `PG-RP` and material interpretive arguments in `PG-CL@version`. Record each consequence once in its responsible home.

Original event/offer/answer wording and the then-known frontier remain preserved. Append later transitions or corrections, update only the current projection, and retain prior versions. The unit freeze records the precise current versions before later sources are opened. Later revelations revise the current interpretation through `PG-RV`; they do not rewrite prior prospective feelings or forecast terms.

The sequential closeout records updated/no-material-change status. Bootstrap source-derived relationship, commitment and current-view rows: **0**.

## Directional events

| Event / version / prior | From → to / continuity / time / learned after | Statement / conduct / inferred state / alternative | Audience / participant understanding / transition | Evidence / claim version / support / correction |
| --- | --- | --- | --- | --- |
| PG-RL-0001@1 / — | Momo → Tōji / mainline / since middle school (revealed) / V01 | Romantic love, long concealed; school chosen for him; confession conditional on losing her tan | Private; Tōji unaware until D-4 | PG-EV-V01-0004, -0006, -0021, -0026 / HIGH |
| PG-RL-0002@1 / — | Momo → Sae / opening day / V01 | Irritation at imitation; wary concealment (「エジキにされちゃう」); nominal friendship | Sae unaware of the depth of wariness | PG-EV-V01-0003, -0004 / HIGH |
| PG-RL-0003@1 / — | Sae → Momo / opening day → D0 / V01 | Imitation; competitive status-seeking; hostility in private (「色黒女」) | Momo partly aware; increasingly aware from D-1 | PG-EV-V01-0003, -0038, -0040 / PG-CL-0002@1 / HIGH (hostility) |
| PG-RL-0004@1 / — | Tōji → Momo / middle school → D-4 / V01 | Protective goodwill; defends her reputation twice | Momo grateful; does not know his feelings | PG-EV-V01-0005, -0024 / HIGH |
| PG-RL-0005@1 / — | Kairi → Momo / ~1 week after opening day / V01 (memory from 2 yrs before) | Interest rooted in the rescue memory; public claim of a kiss; unrequested kiss; later protective rescue; proposal D0. Alternative: game/provocation | Momo rejects; classmates read it as play | PG-EV-V01-0013, -0017, -0018, -0029, -0050 / PG-CL-0006@1 / MODERATE |
| PG-RL-0006@1 / — | Momo → Kairi / ~1 week → D0 / V01 | Anger at the rumor and kiss; physical rejection; grudging thanks for rescue; laughter while waiting together | No romantic interest expressed | PG-EV-V01-0016, -0019, -0029, -0050 / MODERATE |
| PG-RL-0007@1 / — | Tōji → Kairi / DayA+1 / V01 | Hostility; threat 「近づいたら ブッ殺す」 | Kairi amused but shaken | PG-EV-V01-0024 / HIGH |
| PG-RL-0008@1 / RL-0004 | Tōji → Momo / D-4 → D-3 / V01 | Romantic love declared after overhearing her | Momo accepts | PG-EV-V01-0032, -0033 / HIGH |
| PG-RL-0009@1 / — | Sae → Tōji / opening day → D0 / V01 | Desire for status with popular boys; attraction (「かわいいっ」 aside); kisses him over refusals | Tōji regards her as a friend and confidante | PG-EV-V01-0038, -0043 / PG-CL-0002@1 / MODERATE |
| PG-RL-0010@1 / — | Tōji → Sae / D-1 → D0 / V01 | Trust as mutual friend and adviser; follows her advice and reports | Unaware of her deceptions | PG-EV-V01-0042, -0043, -0051, -0052 / HIGH |
| PG-RL-0011@1 / RL-0001 | Momo → Tōji / D-1 → D0 / V01 | Doubt and fear induced by Sae's claim and the packet; avoidance; still declares him her 本命 to Sae and waits for him | Tōji perceives coldness without knowing why | PG-EV-V01-0041, -0048, -0050 / HIGH |
| PG-RL-0012@1 / RL-0008 | Tōji → Momo / D0 / V01 | Jealousy/hurt from Sae's fabricated report; forceful approach | Momo refuses; neither explains | PG-EV-V01-0052, -0053 / MODERATE (motive) |
| PG-RL-0013@1 / — | Momo → Sae / D0 / V01 | Open confrontation; tells Sae the truth; demands she stay away from Tōji | Sae rebuts with lies | PG-EV-V01-0048 / HIGH |
| PG-RL-0014@1 / — | Kairi → Sae / ~1 week / V01 | Rebuff; criticism of her selfishness | Sae humiliated | PG-EV-V01-0009 / HIGH |
| PG-RL-0015@1 / RL-0012 | Tōji → Momo / V01 D0 evening / V02 | Apology; jealousy acknowledged; reconciliation | Momo reassured: 「ちゃんとあたしの気持ち考えてくれてる」 | PG-EV-V02-0004 / HIGH |
| PG-RL-0016@1 / RL-0010 | Tōji → Sae / V02 day 1–3 / V02 | Protective trust; sides with her against Momo | Unaware of her staging | PG-EV-V02-0009, -0010, -0025 / HIGH |
| PG-RL-0017@1 / RL-0011 | Momo → Tōji / V02 / V02 | Frustration at disbelief; persistence; disclosure; 'only you make my heart race' | Tōji alternately reassured and doubting | PG-EV-V02-0011, -0034 / HIGH |
| PG-RL-0018@1 / RL-0013 | Momo → Sae / V02 / V02 | Open enmity; 「友だちじゃない」; recalls origins | Sae publicly casts herself as the wronged friend | PG-EV-V02-0010, -0023 / HIGH |
| PG-RL-0019@1 / RL-0003 | Sae → Momo / V02 / V02 | Private taunting; public victim performance; slander | — | PG-EV-V02-0008, -0009, -0022 / HIGH |
| PG-RL-0020@1 / RL-0009 | Sae → Tōji / V02 / V02 | Stated desire 「とーじが欲しい」; staged kiss; coercive plan | Tōji does not perceive her interest | PG-EV-V02-0024, -0028, -0030 / PG-CL-0002@2 / HIGH (goal stated) |
| PG-RL-0021@1 / RL-0006 | Momo → Kairi / V02 / V02 | Trust as 'my only ally'; still no romance (self-report) | Kairi delighted | PG-EV-V02-0002, -0003, -0034 / HIGH |
| PG-RL-0022@1 / RL-0005 | Kairi → Momo / V02 / V02 | Supportive advice; practical help; continued physical advances; vows not to give up | Momo accepts help, rejects advances | PG-EV-V02-0002, -0019, -0026, -0032 / PG-CL-0006@2 |
| PG-RL-0023@1 / — | Kairi → Sae / V02 / V02 | Contempt for her schemes (「マネッコ」); refuses alliance | Sae: 「大ッキライ」 | PG-EV-V02-0032 / HIGH |
| PG-RL-0024@1 / RL-0004 | Tōji → Kairi / V02 / V02 | Long-standing jealousy and insecurity | Kairi aware of Tōji's hostility | PG-EV-V02-0025, -0033 / HIGH |
| PG-RL-0025@1 / RL-0015 | Tōji → Momo / hospital day / V02 | Hurt, distrust (believes she hid a kiss and may prefer Kairi); proposes breakup | Momo stunned | PG-EV-V02-0037, -0039, -0040 / HIGH |
| PG-RL-0026@1 / RL-0017 | Momo → Tōji / hospital day / V03 | Anger and contempt (「ゲンメツ」); then regret; still loves him (i0057) but feels unbelieved | Tōji unaware of her regret | PG-EV-V03-0001, -0003, -0011, -0012 / HIGH |
| PG-RL-0027@1 / RL-0021 | Momo → Kairi / swim week / V03 | Reliance, gratitude, irritation at his flirting, fluttering (self-report); public defense of his character | Kairi unaware of her inner admission | PG-EV-V03-0009, -0017, -0022, -0029 / PG-CL-0013@1 |
| PG-RL-0028@1 / RL-0022 | Kairi → Momo / swim week / V03 | Supportive; promotes her reunion with Tōji; embraces her after refusal; public flirting with others | Momo moved and confused | PG-EV-V03-0002, -0019, -0021, -0031, -0037 / PG-CL-0006@3 |
| PG-RL-0029@1 / RL-0025 | Tōji → Momo / swim meet / V03 | Shame; apology; public protection; request to restart | Momo refuses | PG-EV-V03-0032, -0033, -0037 / HIGH |
| PG-RL-0030@1 / RL-0016 | Tōji → Sae / swim meet / V03 | Trust broken after overhearing her method | Sae claims he led her on | PG-EV-V03-0025, -0033 / HIGH |
| PG-RL-0031@1 / RL-0020 | Sae → Tōji / swim week / V03 | Plan to 'make him hers' over the summer; public claim that he led her on | Rejected | PG-EV-V03-0025, -0034 / PG-CL-0002@3 |
| PG-RL-0032@1 / RL-0019 | Sae → Momo / swim week / V03 | Organized harassment and sabotage; threats; final victim claim | Momo predicted her isolation | PG-EV-V03-0004, -0014, -0015 / HIGH |
| PG-RL-0033@1 / RL-0018 | Momo → Sae / swim meet / V03 | Slap; warning; 「間違ってる」 | — | PG-EV-V03-0029, -0030 / HIGH |
| PG-RL-0034@1 / — | Kako → Momo / swim meet / V03 | Gratitude for rescue; swimsuit gift; public support; testimony against Sae | Defection from Sae | PG-EV-V03-0020, -0027, -0035 / HIGH |
| PG-RL-0035@1 / RL-0023 | Kairi → Sae / swim week / V03 | Feigned admiration to extract her method; public mockery (「性格直して出直せば?」) | Sae threatened him | PG-EV-V03-0024, -0025, -0036 / HIGH |
| PG-RL-0036@1 / RL-0024 | Kairi → Tōji / swim week / V03 | Provocation and practical help: shows him the truth, ties and taunts him to spur action | Tōji furious, then acts | PG-EV-V03-0019, -0031 / HIGH |
| PG-RL-0037@1 / RL-0026 | Momo → Tōji / end of term / V04 | Apology for a victim's mindset; lists faults; 「今でもとーじが好き」; asks to go out again | Tōji speechless; reunion follows | PG-EV-V04-0009; PG-CL-0015@1 / HIGH |
| PG-RL-0038@1 / RL-0029 | Tōji → Momo / end of term / V04 | Penance without a bid to win her back; accepts her request | Momo moved; reunion | PG-EV-V04-0008, -0010 / HIGH |
| PG-RL-0039@1 / RL-0028 | Kairi → Momo / day after the meet / V04 | Defends Tōji; confronts Momo: 「信じてないのはももちゃんのほうじゃん」; leaves | Momo angry, then concedes | PG-EV-V04-0005, -0006, -0007 / HIGH |
| PG-RL-0040@1 / RL-0039 | Kairi → Momo / second term / V04 | Avoids her; on being found out jokes about opportunism; urges her toward Tōji; cuts off her counterfactual; joking standing offer | Momo reads it as tact and as love | PG-EV-V04-0013, -0016, -0017; PG-CL-0006@4 / MODERATE–HIGH; alternative: opportunism |
| PG-RL-0041@1 / RL-0027 | Momo → Kairi / second term / V04 | Apology; gratitude (「あんたがいなかったら…学校やめちゃってたかも」); unfinished 「もしとーじより先に出会ってたら」; tears; wishes to keep him as before | Kairi deflects | PG-EV-V04-0015…0018; PG-CL-0013@2 / HIGH (feelings exist), category UNRESOLVED |
| PG-RL-0042@1 / RL-0037 | Momo → Tōji / second term / V04 | Refuses a kiss she wants; demands verbal 「好き」; quarrels; delighted by the public sign | Tōji hurt, then complies | PG-EV-V04-0019…0021, -0024, -0028; PG-CL-0017@1 / HIGH |
| PG-RL-0043@1 / RL-0038 | Tōji → Momo / second term / V04 | Kiss attempt; silent after refusal; stomach pain (Kairi's reading); public sign; forehead kiss | Momo receives the private meaning; class does not | PG-EV-V04-0019, -0023, -0028, -0029 / HIGH |
| PG-RL-0044@1 / RL-0033 | Momo → Sae / second term / V04 | Leaves her at the drill; does not retaliate; partners her; tolerates the servility; warns her about lying | Sae servile | PG-EV-V04-0011, -0022, -0025, -0026, -0038 / HIGH |
| PG-RL-0045@1 / RL-0032 | Sae → Momo / second term / V04 | Public servility; private hostility (fantasy, shoe stamping); exploits Momo's gift and presence; misrepresents her to Jigoro | Momo unaware of the hostility and the false account | PG-EV-V04-0027, -0032, -0036, -0037; PG-CL-0016@1 / HIGH |
| PG-RL-0046@1 / — | Jigoro → Sae / late September / V04 | Struck by her lightness; sympathizes; rescues her; 「おれと つきあってほしい」 | Sae astonished | PG-EV-V04-0035, -0037, -0039, -0040 / HIGH (conduct), motive PLAUSIBLE |
| PG-RL-0047@1 / — | Jigoro → Momo / late September / V04 | 「ひでー女だな」; sees her as jealous of Sae | Momo unaware | PG-EV-V04-0036, -0037; PG-CL-0018@1 / HIGH |
| PG-RL-0048@1 / RL-0036 | Kairi → Tōji / end of term and second term / V04 | Counsel (he takes words at face value); defends him to Momo; teases him as the fake nurse and boasts about Momo | Tōji jealous | PG-EV-V04-0005, -0008, -0023 / HIGH |
| PG-RL-0049@1 / RL-0024 | Tōji → Kairi / second term / V04 | Jealous rage at the boast of frequent kiss attempts | Comic chase | PG-EV-V04-0023 / HIGH |

## Commitments and boundaries

| Event / prior | Participants / offer or limit / conditions | Answer / acceptance basis / status | Conduct / permission / consequence / time / frontier | Evidence / knowledge / claim / uncertainty / revision |
| --- | --- | --- | --- | --- |
| PG-CM-0001 / — | Tōji ↔ Momo / mutual declaration → dating | Momo: 「本当に… あたしで…… いいの…?」; nonverbal acceptance; label 彼女 (i0114); public claim to Kairi 「オレのだから」 / ACCEPTED_WITH_EVIDENCE | D-3; strained at D0 | PG-EV-V01-0032, -0033, -0036 / HIGH |
| PG-CM-0002 / — | Momo → Tōji / keep relationship secret; do not tell Sae | Tōji: 「安達がそーゆーんなら……」 / ACCEPTED_WITH_EVIDENCE (reluctant) | D-2. Momo herself discloses to Sae at D0 (i0157). Tōji believes Momo told Sae (i0135); he did not breach | PG-EV-V01-0037, -0042, -0048; PG-KN-0011 |
| PG-CM-0003 / — | Tōji → Momo / meet at the poolside after class | Momo: 「う… うん……」 / ACCEPTED_WITH_EVIDENCE | D0; frustrated by Sae's false relay; Momo waits as agreed; Tōji waits at the cafeteria | PG-EV-V01-0049, -0050, -0051; PG-TX-0010 |
| PG-CM-0004 / — | Tōji → Momo / 「なんかあったら… オレにいえよ」 | 「うん……」 / ACCEPTED_WITH_EVIDENCE | D-2; Momo does not invoke it when troubled by Sae's claims | PG-EV-V01-0036, -0041 |
| PG-CM-0005 / — | Kairi → Momo / kiss (i0053) | No request or assent; she knees him and rejects it / DECLINED (after the fact) | Momo's classification: taken 「有無をいわせず」 (i0149) | PG-EV-V01-0018, -0019, -0045 / HIGH |
| PG-CM-0006 / — | Kairi → Momo / 「つきあおっか」 (i0055); serious proposal (i0168) | First: rejected with violence. Second: turned aside by her 「とーじを好きなままでいーのね」 / DECLINED | D0 | PG-EV-V01-0019, -0050 / PG-CL-0006@1 |
| PG-CM-0007 / — | Kairi → Momo / attempted kiss while she cries (i0148) | Protest 「いや」 / DECLINED | She strikes him | PG-EV-V01-0046 / contact ambiguous |
| PG-CM-0008 / — | Sae → Tōji / 「練習台」 kiss | Tōji refused twice; Sae proceeded / AMBIGUOUS (his participation after the grab is not shown) | D0 morning; witnessed by Momo and Kairi | PG-EV-V01-0043, -0044 / UNRESOLVED participation |
| PG-CM-0009 / — | Tōji → Momo / unrequested kiss at the pergola | 「いやっ」 and shove / DECLINED | D0 end; consequence pending | PG-EV-V01-0053 / PG-CL-0005@1 |
| PG-CM-0010 / — | Momo → Tōji / sexual timing: 「使うのはまだまだ先のことだからね」 | Tōji confused, no answer / AMBIGUOUS | V01 D0 evening; Tōji did not understand the context | PG-EV-V02-0005 |
| PG-CM-0011 / CM-0002 | Momo → Tōji / stop talking to Sae; ignore her | Tōji refuses (「友だちだろ……?」) / DECLINED | V02 day 1 | PG-EV-V02-0007, -0010 |
| PG-CM-0012 / — | Momo → Tōji / promise to hear her out fully, under a window-jump threat | 「約束する…最後まで聞く」 / ACCEPTED_WITH_EVIDENCE (coerced) | Hearing begins (i0136); interrupted by Sae (i0150) | PG-EV-V02-0027, -0035 |
| PG-CM-0013 / CM-0001 | Tōji → Momo / 「別れよう」 | No answer shown / PROPOSED | End of V02 | PG-EV-V02-0040 / PG-CL-0009@1 |
| PG-CM-0014 / CM-0013 | Tōji → Momo / 「別れよう」 | Momo: 「こっちから別れてやるわよ」 / ACCEPTED_WITH_EVIDENCE (breakup); CM-0001 ENDED | Hospital day | PG-EV-V03-0001 |
| PG-CM-0015 / — | Kairi → Momo / summer trip to the sea where they met | 「いこーかな…」 / AMBIGUOUS (tentative acceptance) | Pending | PG-EV-V03-0009; PR-0007 |
| PG-CM-0016 / — | Kairi → Momo / 「抱かせて?」 in the changing room | 「くるなくるな」 / DECLINED; he embraced her anyway | Her later reflection: she did not resist while held | PG-EV-V03-0021, -0022 |
| PG-CM-0017 / — | Kairi → Sae / promise not to 喋る (talk) | ACCEPTED under her threat | Literal promise kept; exposure achieved by arranging overhearing and witnesses | PG-EV-V03-0024, -0025, -0035 |
| PG-CM-0018 / CM-0014 | Tōji → Momo / 「やり直さないか?」 | 「とーじとはつきあえない」 / DECLINED | End of V03 | PG-EV-V03-0037; PG-CL-0012@1 |
| PG-CM-0019 / CM-0018 | Momo → Tōji / 「もう一度あたしとつきあってください」 | Answer not shown; ACCEPTED_BY_CONDUCT (「元サヤに戻りました」, i0052) | Relationship resumed at end of first term | PG-EV-V04-0009, -0010 |
| PG-CM-0020 / — | Swim-club girls → Momo / join to save the club | ACCEPTED_BY_CONDUCT (member by i0094) | Second term | PG-EV-V04-0012, -0020 |
| PG-CM-0021 / — | Momo → Tōji / the L sign means 「好き」 | Refused (「恥ずかしすぎ」), then performed publicly / ACCEPTED_BY_CONDUCT | Second term | PG-EV-V04-0024, -0028 |
| PG-CM-0022 / — | Momo → Sae / 「この埋め合わせはきっとするから」 | Redeemed by Sae the next day (studio visit) / FULFILLED | Late September | PG-EV-V04-0032, -0034 |
| PG-CM-0023 / — | Honda → Sae / candidacy in the magazine's girlfriend feature | ACCEPTED (shoot) | Late September; deadline 9月29日 | PG-EV-V04-0034 |
| PG-CM-0024 / — | Jigoro → Sae / 「おれと つきあってほしい」 | PENDING (answer not shown) | End of V04 | PG-EV-V04-0040 |
| PG-CM-0025 / — | Kairi → Momo / 「とーじに飽きたらいつでもオレんとこ来なよ」 | 「…バカ!!」 / DECLINED (joking standing offer) | Second term | PG-EV-V04-0017 |

## Current directional state

| Ordered pair / boundary | Active event versions | Private/public state / reciprocity basis | Unresolved disagreement |
| --- | --- | --- | --- |
| Momo → Tōji @ PG-FR-V01 | RL-0001, RL-0011 | Loves him; dating (secret); currently fearful/doubting; refused his kiss | Whether she will ask him directly |
| Tōji → Momo @ PG-FR-V01 | RL-0004, RL-0008, RL-0012 | Loves her; believes she prefers Kairi; refused | His interpretation of her refusal |
| Momo ↔ Sae @ PG-FR-V01 | RL-0002, RL-0003, RL-0013 | Nominal friendship in open rupture; Momo knows Sae lies | Whether friendship formally ends |
| Kairi → Momo @ PG-FR-V01 | RL-0005 | Pursuing; proposal declined | Sincerity |
| Momo → Kairi @ PG-FR-V01 | RL-0006 | Hostile-familiar; no romance | — |
| Tōji → Sae @ PG-FR-V01 | RL-0010 | Trusting friend | When or whether he learns of her deceptions |
| Sae → Tōji @ PG-FR-V01 | RL-0009 | Pursuing through manipulation | Weight of attraction vs rivalry |
| Momo → Tōji @ PG-FR-V02 | RL-0001, -0017 | Loves him; furious at the 'practice' kiss; breakup proposed | Her answer |
| Tōji → Momo @ PG-FR-V02 | RL-0008, -0015, -0025 | Loves her but has lost confidence; believes she hid a Kairi kiss | Whether he learns the context |
| Momo ↔ Sae @ PG-FR-V02 | RL-0018, -0019 | Open enmity; Sae's public victim role | — |
| Sae → Tōji @ PG-FR-V02 | RL-0020 | Pursuing; planned coercion | Tōji's awareness |
| Kairi → Momo @ PG-FR-V02 | RL-0022 | Ally-suitor | — |
| Momo → Kairi @ PG-FR-V02 | RL-0021 | Trusted ally; no romance | — |
| Kairi ↔ Sae @ PG-FR-V02 | RL-0023 | Adversarial; Kairi knows her plan | — |
| Momo → Tōji @ PG-FR-V03 | RL-0026; CM-0018 | Still loves him; refused to restart | Reason |
| Tōji → Momo @ PG-FR-V03 | RL-0029 | Wants to restart; publicly protective | — |
| Momo → Kairi @ PG-FR-V03 | RL-0027 | Reliance; disavowed fluttering | Category |
| Kairi → Momo @ PG-FR-V03 | RL-0028 | Ally-suitor who promotes her reunion with Tōji | — |
| Sae ↔ class @ PG-FR-V03 | RL-0032, RP-0013 | Isolated | — |
| Kako → Momo @ PG-FR-V03 | RL-0034 | Ally | — |
| Momo → Tōji @ PG-FR-V04 | RL-0037, -0042; CM-0019, -0021 | Dating again, publicly known; loving; wants more intimacy and words | — |
| Tōji → Momo @ PG-FR-V04 | RL-0038, -0043 | Dating; reticent but responsive | — |
| Momo → Kairi @ PG-FR-V04 | RL-0041 | Grateful; unfinished counterfactual; wants friendship as before | Category of feeling |
| Kairi → Momo @ PG-FR-V04 | RL-0040; CM-0025 | Withdrawn; jokes | Depth of feeling (Misao: 「結構マジ」) |
| Sae → Momo @ PG-FR-V04 | RL-0045 | Public servility, private hostility | Sincerity |
| Momo → Sae @ PG-FR-V04 | RL-0044 | Tolerant, condescending; believes Sae is changing | Accuracy of Momo's model |
| Jigoro → Sae @ PG-FR-V04 | RL-0046; CM-0024 | Pursuing | Sae's answer |
| Jigoro → Momo @ PG-FR-V04 | RL-0047 | Hostile belief | — |

Revision history: 0.1 — bootstrap schema, zero rows, 2026-10-16 UTC. 0.2 — V01 transaction rows appended (frontier PG-FR-V01), 2026-10-16 UTC. V02 transaction rows appended (frontier PG-FR-V02), 2026-10-16 UTC. V03 transaction rows appended (frontier PG-FR-V03), 2026-10-17 UTC. V04 transaction rows appended (frontier PG-FR-V04), 2026-10-17 UTC.

## Recipient audit boundary PG-AUDIT-20261019

New owner-authorized, non-blind V01–V04 correction pass; see the [source audit](../07%20Audits%20and%20Handoffs/PEACH_GIRL_CODEX_V01_V04_SOURCE_AUDIT_20261019.md). Learned after PG-FR-V04, before opening V05; narrative cutoff V04. Earlier frozen-boundary projections above are historical, not competing current authority. Submitted historical rows remain unchanged; original unsuffixed event rows have implicit version 1. The following successor versions and audit projections govern current retrieval until the next transaction. Corrections change the analyst's account, not characters' historical knowledge.

| Corrective version / original | Ordered pair / source time | Corrected state / predecessor | Evidence / claim / issue |
| --- | --- | --- | --- |
| PG-RL-0024@2 / RL-0024@1 | Tōji → Kairi / V02 | Same jealousy/insecurity observation; same-direction predecessor RL0007@1 replaces wrong-target RL0004 | PG-EV-V02-0025, -0033; A01 / HIGH |
| PG-RL-0036@2 / RL-0036@1 | Kairi → Tōji / V03 | Same provocative practical assistance; same-direction predecessor NONE ESTABLISHED. RL0024@2 is reciprocal context only, not predecessor | PG-EV-V03-0019, -0031; A01 / HIGH |
| PG-RL-0037@2 / RL-0037@1 | Momo → Tōji / V04 end of term | Same-direction prior RL0026@1; her self-criticism and continuing love lead to request after his independently stated accountability; earlier harm not erased | PG-EV-V04-0003, -0006…0009; PG-CL-0015@2; A05 |
| PG-RL-0040@2 / RL-0040@1 | Kairi → Momo / V04 second term | Prior RL0039@1; withdraws/helps reunion and deflects thanks, but makes a sexualized joking standing offer. Continuing interest established; purely disinterested motive not established | PG-EV-V04-0013, -0016, -0017; PG-CL-0006@5; A04 |
| PG-RL-0041@2 / RL-0041@1 | Momo → Kairi / V04 second term | Prior RL0027@1; gratitude, grief, supported romantic possibility and wish for continuing closeness, with explicit present choice of Tōji. No friendship-only label or completed love declaration | PG-EV-V03-0022; PG-EV-V04-0015…0018; PG-CL-0013@3; A03 |
| PG-RL-0043@2 / RL-0043@1 | Tōji → Momo / V04 second term | Prior RL0038@1; private sign made public and affectionate interrupted contact. Exact anatomy UNKNOWN at audit; 'forehead' withdrawn as secure description pending V05 | PG-EV-V04-0019, -0023, -0028, -0029; A09 |

| Commitment correction / original | Request / answer / permission | Later conduct or consequence | Evidence / issue |
| --- | --- | --- | --- |
| PG-CM-0008@2 / CM0008 implicit @1 | Sae → Tōji practice kiss; two refusals; DECLINED permission | Sae proceeds; participation after grab remains UNKNOWN. Ambiguity about later conduct does not erase refusal | PG-EV-V01-0043, -0044; i0134–0140; A02 |
| PG-CM-0025@2 / CM0025 implicit @1 | Kairi → Momo sexualized joking standing offer; teasing rebuff; no acceptance or commitment evidenced | Present offer rebuffed (DECLINED); teasing wording does not prove a permanent limit or exhaust her feeling | PG-EV-V04-0017; i0081–0083; A04 |

| Current ordered pair / boundary | Active corrected versions | Current directional retrieval | Unknown |
| --- | --- | --- | --- |
| Momo → Tōji @ PG-AUDIT-20261019 | RL0037@2, RL0042@1; CM0019, CM0021 | Loving/chosen renewed relationship after accountability; desire does not imply permission to each approach | Future resilience |
| Tōji → Momo @ PG-AUDIT-20261019 | RL0038@1, RL0043@2 | Dating; remorse/accountability and reticent affection evidenced | Contact anatomy pending V05 |
| Momo → Kairi @ PG-AUDIT-20261019 | RL0041@2; CL0013@3 | Gratitude, grief, romantic pull/possibility and desire for closeness; presently chooses Tōji | Not established as merely friendship or as chosen love |
| Kairi → Momo @ PG-AUDIT-20261019 | RL0040@2; CM0025@2 | Considerate withdrawal and continuing sexual/romantic interest; earlier refused advances remain refused | Care/opportunism weighting |
| Tōji → Kairi @ PG-AUDIT-20261019 | RL0049@1 via corrected RL0024@2 | Current V04 conduct preserved; prior direction corrected | No new motive claimed |
| Kairi → Tōji @ PG-AUDIT-20261019 | RL0048@1 via corrected RL0036@2 | Current V04 conduct preserved; reciprocal rivalry is separate causal context | No earlier same-direction predecessor established |

EVV03-0021 descriptive erratum: the changing-room embrace was requested, refused, then performed (i0088–0089); CM0016 correctly retains that refusal. Momo's subsequent softening does not rewrite initiation. Next new IDs remain RL0050 and CM0026.

Revision history addendum: recipient source-audit successor corrections, 2026-10-19; original frozen states preserved.
