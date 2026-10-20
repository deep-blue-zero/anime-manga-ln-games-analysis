---
title: "Peach Girl — Directional Relationships and Commitments"
artifact_id: PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER
artifact_type: relationship_commitment_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.7"
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

## V05 successor transaction — PG-FR-V05

New Route B reading owns PG-EV-V05; EV suffixes refer to that volume only. Latest boundary views below govern current retrieval. All new directional rows are @1, mainline continuity, learned in V05; same-direction predecessors explicit. Read [V05](../02%20Sequential%20Readings/PEACH_GIRL_V05_DEEP_READING.md) for participant knowledge, staging and counterreadings; no later consent backdated.

| Directional event / prior | From → to / represented time | Statement, behavior, transition / understanding | Evidence / claim / limit |
| --- | --- | --- | --- |
| PG-RL-0043@3 / RL0043@2 | Tōji → Momo / V04 contact, revealed V05 | Same private-sign affection; cheek directly named by Momo in V05. Dated descriptive erratum, no new V04 action/knowledge | EV0013; CL0017@2; forehead withdrawn, not frozen bytes rewritten |
| PG-RL-0050@1 / NONE ESTABLISHED | Sae → Jigoro / proposal through birthday | Enjoys heroine/status, goods and reassurance yet feels defeated; explicitly rejects him/wants Tōji, later deploys love/tears to recruit him conditionally. Some attraction to wounded allure shown | EV0001–0011/0015/0021–0023/0045; CL0002@5; no securely reestablished stable dating label |
| PG-RL-0051@1 / RL0046@1 | Jigoro → Sae / same span | Protective affection/gifts and distress after breakup; seeks reconciliation, initial boundary against unwanted intimacy, later pursues her condition. Misinformed about Momo | EV0002/0010–0011/0015/0021–0023/0045; CL0018@2; no inference Sae reciprocates equally |
| PG-RL-0052@1 / RL0042@1 | Momo → Tōji / pre-birthday/birthday | Explicitly prefers present changed partner; wants intimacy, exposes garden staging, initiates kiss/territorial claim, enjoys birthday and immediate consensual development. Later dream/misperception still addresses Tōji | EV0008–0009/0013/0016/0019–0020/0026/0028–0029/0037/0047; CL0015@3/0017@2; slap/jealous bargain retained, no voluntary Jigoro choice |
| PG-RL-0053@1 / RL0043@3 | Tōji → Momo / same span to search | Loves only Adachi, independent gift/party care; responds to presumed Momo under identity deception; detects substitution and searches, refusing false choice story | EV0017/0025/0028–0029/0034–0046; CL0005@5/0019@1; deception/vulnerability and guilt do not prove informed betrayal |
| PG-RL-0054@1 / RL0031@1 | Sae → Tōji / post-breakup through disguise | Repeatedly declares love, stages farewell kiss then disguises herself as Momo to obtain contact; knows her true identity is not accepted | EV0011/0014/0017–0020/0033–0035/0039–0042; CL0002@5/0003@5; specific desire not reduced to status alone |
| PG-RL-0055@1 / RL0030@1 | Tōji → Sae / same span | Apologetic but explicit romantic/kiss refusals; briefly hopes reformed at shop; after identity reveal rejects approach and offers, angrily demands assistance finding Momo | EV0017–0018/0025/0038–0044; CL0005@5; response while thinking Adachi is not willing Sae relationship |
| PG-RL-0056@1 / RL0044@1 | Momo → Sae / before/birthday | Counters blind-belief standard, sees garden staging; nevertheless chooses urgent help after Sae's crying claim, unaware of full plot | EV0009/0020/0030–0032; no wholesale trust reset implied; voluntary help distinct from consent |
| PG-RL-0057@1 / RL0045@1 | Sae → Momo / same span | Rival comparison and private hostility escalate into isolation, removal via Jigoro, impersonation and intended manufactured sexual fact | EV0010–0011/0022–0023/0027/0030–0035/0040/0045; CL0003@5; sexual outcome unresolved |
| PG-RL-0058@1 / RL0047@1 | Jigoro → Momo / same span | Hostile glare, false bully/fan belief, initially refuses intimacy, later carries incapacitated Momo and blocks calls; asserts her wish | EV0007/0022–0023/0032/0036–0037/0041/0045/0048; CL0018@2; sees incapacity, not solely unaware of all relevant facts |
| PG-RL-0059@1 / NONE ESTABLISHED | Momo → Jigoro / birthday | No fan/romantic choice established; tries to explain she came to talk, misperceives him as Tōji while impaired, then wakes frightened/confused | EV0030–0032/0037/0047–0048; no reciprocity or commitment established |

| Commitment / prior | Request, answer and status | Conduct / knowledge / consequence | Evidence / limits |
| --- | --- | --- | --- |
| PG-CM-0008@3 / CM0008@2 | Original practice request initially DECLINED; later acquiescence now SELF_REPORTED, not original initial permission | V01 represented time, learned V05: Tōji says he could have resisted and sought experience for Momo. Both phases retained; precise unshown conduct still limited | EV0017 plus PG-EV-V01-0043/0044; IP0010@2/0020@2 |
| PG-CM-0024@2 / CM0024 implicit @1 | Jigoro dating proposal ACCEPTED_WITH_EVIDENCE by conduct; later ENDED by Sae CM0026 | Public couple/date/gifts, explicit breakup; later request for reconciliation separately CM0030 | EV0001–0011; stable restart not established |
| PG-CM-0026 / CM0024@2 | Sae → Jigoro cannot date him, wants Tōji / ENDED | His subsequent depression and reconciliation plea support actual rupture, not only hypothetical comparison | EV0011/0015/0021 |
| PG-CM-0027 / — | Sae → Tōji romantic pursuit / DECLINED | Tōji loves only Adachi, apologizes but refuses; no compassionate obligation to date | EV0014/0017 |
| PG-CM-0028 / — | Sae → Tōji parting kiss / DECLINED repeatedly | Grabs despite refusal, head turn limits contact to cheek, push/stop; no consent imported from V01 account | EV0018 |
| PG-CM-0029 / — | Momo → Tōji initiated kiss / no prior express assent, then ACCEPTED_WITH_EVIDENCE by response; more-kisses forgiveness bargain | Initial surprise then responding embrace/affection. Slap and territorial/competitive demand retained, not generic authorization | EV0019–0020; each phase/context separate |
| PG-CM-0030 / CM0026 | Jigoro → Sae reconciliation/anything offer / PROPOSED conditionally, no secure final stable label | She makes condition about Momo, professes love; his wish to reconcile does not establish equal reciprocity | EV0021–0023 |
| PG-CM-0031@1 / — | Sae → Jigoro night with Momo / DECLINED at i0095 | He refuses someone he does not like; no request/assent by Momo | EV0022–0023 |
| PG-CM-0031@2 / CM0031@1 | Same third-party scheme / ACCEPTED_WITH_EVIDENCE prospectively at later phone exchange | Recruitment inferred at i0117 and removal shown; i0167 explicit agreement despite continued sleep. This is an agreement between schemers, NEVER Momo permission; completion UNKNOWN | EV0030/0032/0045; original refusal preserved |
| PG-CM-0032 / — | Momo → Tōji return/call if late / ACCEPTED_WITH_EVIDENCE as plan; performance interrupted by incapacity | Leaves to help Sae, Tōji waits; failure to call has external constraint, no voluntary betrayal/breach inferred | EV0030–0034/0041 |
| PG-CM-0033 / — | Tōji → Momo check after startling intimate advance / ACCEPTED_WITH_EVIDENCE for immediate context | Hesitant not-unwanted answer and mutual behavior; no unlimited permission or intercourse completion | EV0029 |
| PG-CM-0034 / — | Sae → Tōji disguised intimate approach / informed acceptance of Sae ABSENT; DECLINED upon identification | Tōji believes Adachi, responds to that identity, stops on mismatch then rejects known Sae | EV0034–0035/0038–0039; relationship label alone supplies no consent |
| PG-CM-0035 / — | Tōji → Sae accompany/assist search / ACCEPTED_WITH_EVIDENCE under pressure | She accompanies, calls reluctantly, withholds and secretly urges scheme; partial compliance, no sincere shared rescue goal established | EV0042–0046 |

| Current ordered pair / PG-FR-V05 | Active RL / CM | Current state and unresolved asymmetry |
| --- | --- | --- |
| Momo → Tōji | RL0052; CM0029/0033 | Chosen love/desire, agency in kisses and contextual assent; subsequent incapacity not voluntary betrayal |
| Tōji → Momo | RL0053 via RL0043@3; CM0032 | Caring/searching, rejects Sae narrative; no rescue completed yet, does not know missing interval |
| Sae → Tōji | RL0054; CM0027/0028/0034 | Pursues through refused and disguised contact; no informed acceptance |
| Tōji → Sae | RL0055; CM0035 | Refusal, distress/anger and compelled cooperation; not a second chosen romance |
| Sae → Jigoro | RL0050; CM0026/0030/0031@2 | Rejected him, later love claim/conditional recruitment; attraction and instrumentality coexist, stable reunion unknown |
| Jigoro → Sae | RL0051; CM0030/0031@2 | Wants her, cooperates after stated initial boundary; actual Momo assent absent |
| Momo → Sae | RL0056 | First trick detected, later emergency help chosen with incomplete knowledge |
| Sae → Momo | RL0057 | Deliberate hostile scheme, not ordinary friendship repair |
| Jigoro → Momo | RL0058 | False account plus his harmful control/knowledge of sleep; final outcome unverified |
| Momo → Jigoro | RL0059 | No reciprocal romantic agreement; fear/question at exit |
| Kairi → Momo | RL0040@2; CM0025@2 preserved | Care, withdrawal and continuing interest; V05 no material change |
| Momo → Kairi | RL0041@2; CL0013@3 preserved | Romantic pull/gratitude/possibility, present Tōji choice; not relabeled merely friendship |

Next new IDs RL0060 and CM0036. Earlier boundary projections and all initial request/answer terms remain historical. Revision history: 0.4 — V05 successor events and anatomy/practice testimony revisions, 2026-10-19 owner date.

## V06 successor transaction — PG-FR-V06

[V06 reading](../02%20Sequential%20Readings/PEACH_GIRL_V06_DEEP_READING.md) owns PG-EV-V06; EV below uses that volume unless V05 specified. All learned V06, prior frozen records unchanged. Priors are same-direction states; reciprocal context is not a predecessor. Current views are the newest rows below, not historical projections.

| Directional event / same-direction prior | Represented source time / feeling, conduct and mutual understanding | Evidence / claim / limits |
| --- | --- | --- |
| PG-RL-0053@2 / RL0053@1 | Tōji → Momo / V05 gift, corrected V06: refusal of joint shopping, but product/scent steered by Sae; real gift/party affection retained | V05 i0101–0106/EV0025; V06 EV0031; CS0044@2/CL0005@6/0019@2; no rewrite of V05 bytes |
| PG-RL-0060@1 / RL0052@1 | Momo → Tōji / hotel to café: fears shame/rejection, mishears then receives explicit love/no-fault reassurance; chooses continuing affection and feels deeper closeness; scripted breakup still hurts | EV0021/0023–0028/0047–0048; CL0015@4/0017@3/0020@1; CM0040 performance not true end |
| PG-RL-0061@1 / RL0053@2 | Tōji → Momo / search to reunion: reaches/rescues, regrets own failures, explicitly denies her fault/impurity rejection; honestly discloses deception, restores wanted affection | EV0003–0005/0016–0017/0023–0028/0030/0047–0048; CL0005@6; desperation/violence and later revenge retained |
| PG-RL-0062@1 / RL0040@2 | Kairi → Momo / night through revenge: advocates, helps couple, overhears privately, retains sexualized jokes, proposes/executes punitive scheme | EV0017–0018/0022/0030–0031/0038–0039/0044–0046; CL0006@6; pure selfless motive unproven, previous boundary history remains |
| PG-RL-0063@1 / RL0041@2 | Momo → Kairi / same span: receives advocacy, objects to private overhearing, joins plan/asks safety; no new chosen love declaration or reclassification | EV0031/0038–0039/0044–0045; CL0013@3 retained; prior supported romantic pull not erased by alliance |
| PG-RL-0064@1 / RL0057@1 | Sae → Momo / night to shoot: photographs staged scene, false blame, admits drugs/envy and treats model as compensation; later triumph over apparent breakup | EV0010/0018–0019/0035–0036/0041–0042; CL0002@6/0003@6; no genuine protective friendship inferred |
| PG-RL-0065@1 / RL0056@1 | Momo → Sae / morning to revenge: residual charity until direct admission, then unprecedented hatred, direct anger and conscious retaliation; anger and pity coexist later | EV0033/0035–0039/0044–0045/0048; CL0021@1; no passive-innocent-only compression or final forgiveness |
| PG-RL-0066@1 / RL0054@1 | Sae → Tōji / night obstruction, later café: tries prevent reaching Momo, then believes false confession, privately delights at winning and wants intimacy | EV0004/0015/0041–0043; CL0002@6; specific desire real, consent to drugging absent |
| PG-RL-0067@1 / RL0055@1 | Tōji → Sae / search to revenge: rejects delay; later performs love to lure her, drugs drink and allows punitive delivery | EV0003–0004/0015/0042–0045; CL0005@6/0021@1; scripted words not accepted genuine romance or ethical acquittal |
| PG-RL-0068@1 / RL0058@1 | Jigoro → Momo / hotel: insists her wish/initiative, presents wrapper, begins doubting Sae account when she cries; later hears fan/drug truth | EV0002/0006–0008/0011/0034–0035; CL0018@3; no verified act confession or innocence |
| PG-RL-0069@1 / RL0059@1 | Momo → Jigoro / hotel onward: challenges story, refuses approach, fears harmed; no chosen attraction/romantic agreement | EV0002/0006–0008/0021/0028; sexual outcome unknown, reassurance does not prove nothing occurred |
| PG-RL-0070@1 / RL0051@1 | Jigoro → Sae / hotel to shoot: recruited through conditional dating, shocked at public rejection, learns lie/drugging and voices disillusionment from idealized fragile-girl image | EV0019/0034–0037; CL0018@3; his perception not objective past biography |
| PG-RL-0071@1 / RL0050@1 | Sae → Jigoro / hotel/shoot: protects model face but blames/rejects him publicly and privately, repudiates implied reward; admits using false fan story | EV0017/0019/0034–0036; no equally reciprocal affection or restored dating established |
| PG-RL-0072@1 / RL0048@1 | Kairi → Tōji / night/morning/day: helps, permits then redirects violence, urges no blame, keeps teasing rival and directs joint revenge | EV0017/0022/0030/0038–0039/0044–0046; cooperation does not end rivalry |
| PG-RL-0073@1 / RL0049@1 | Tōji → Kairi / same span: accepts aid, distinguishes close rival from Jigoro, protests jokes, cooperates in revenge and wonders whether love persists | EV0030/0044/0046; question is not confirmation of other mind |
| PG-RL-0074@1 / NONE ESTABLISHED | Misao → Momo/Tōji/Kairi as bounded caregiving directions / night/morning: adult help, intervention, wishes/context, responsibility, also expedient lie | EV0005/0014/0017/0019–0020/0022/0029; institutional/group context, no romantic attachment inferred |

| Commitment / prior | Proposal, actual response and temporal scope | Evidence / boundary |
| --- | --- | --- |
| PG-CM-0036 / — | Momo → Misao no disclosure/leave alone for now / ACCEPTED_BY_CONDUCT, Misao leaves; family reassurance later not assumed full scheme disclosure | EV0020/0022; local wishes under distress, not permanent refusal or factual denial |
| PG-CM-0037 / CM0019 | Momo ↔ Tōji continue affection despite harm / ACCEPTED_WITH_EVIDENCE through reassurance, responsive intimacy and later hand-link | EV0025–0028/0047–0048; neither unlimited sexual permission nor compensated mutual fault |
| PG-CM-0038 / — | Kairi → Momo/Tōji revenge / ACCEPTED_BY_CONDUCT in script, cup interference and delivery; Momo explicitly hesitates then chooses | EV0038–0039/0041–0045; agreement among trio, not Sae consent |
| PG-CM-0039 / — | Sae → Tōji private intimacy after professed love / PROPOSED with his acting agreement, informed mutual agreement not established | EV0042–0043; his script conceals intentions; her desire no permission to drug/remove |
| PG-CM-0040 / CM0019 | Tōji → Momo breakup, her rejection/slap / STAGED_DECLARATION explicitly confirmed at146; **NOT_ACTUAL_ENDED** relationship | EV0041/0044/0047; real emotional pain despite planned false content |
| PG-CM-0041@1 / — | Trio → intended actor punitive performance/no actual assault / ASSURANCE_REPORTED_BY_KAIRI, delivery attempted | EV0045; actual recipient not yet identified, no omniscient agreement or safety proof |
| PG-CM-0041@2 / CM0041@1 | Intended arrangement / DELIVERY_DIVERGED, contact still waiting at165 | EV0050; actual man not confirmed actor, harm outcome UNKNOWN; no safe fulfilled status |
| PG-CM-0042 / — | Sae drink/incapacitated removal / informed permission ABSENT, BOUNDARY_VIOLATED | EV0043–0045; explicit desire for Tōji not permission for hidden drug/third-party threat |
| PG-CM-0043 / — | Momo → Kairi ensure no actual assault / ASSURANCE_RECEIVED, relied on intended actor claim; implementation fails confirmation | EV0045/0050; desire to limit harm and punitive participation coexist, result not guaranteed |

Current relationship at exit is Momo/Tōji continuing, RL0060/0061 and CM0037; supposed rupture was a script. Sae has no informed new Tōji partnership. No reciprocity assumed from direction alone. CM0031@2 remains earlier agreement between schemers, never Momo consent; no V06 completion proof. Next RL0075, CM0044. Revision history0.5 — V06 directions/commitments and dated gift-selection correction, owner date2026-10-19.

## V07 successor transaction — PG-FR-V07

[V07 reading](../02%20Sequential%20Readings/PEACH_GIRL_V07_DEEP_READING.md) owns EV=PG-EV-V07 observations. All rows learned V07 at stated scene frontiers; HIGH conduct/statement support, inferred motive MODERATE unless causal pressure directly established. Directions distinct; public label, affection and permission are separate.

| Direction / prior | From → to, observed state and temporal transition | Evidence / interpretation and knowledge limit |
| --- | --- | --- |
| PG-RL-0075 / RL0065 | Momo → Sae / after error chooses rescue despite unforgiven hurt, takes protective lead; declares end to engagement46–48, feels relief | EV0005–0010/0013; CL0022@1, CM0045. Empathic action revises revenge, not universal friendship/forgiveness |
| PG-RL-0076 / RL0064 | Sae → Momo / resents trio setup, condemns/slaps Momo; then destructive intent/photograph leverage/disparages rescue motive, displays claimed replacement | EV0009/0014/0016–0018/0024/0028/0044; CL0002@7/0003@7. Critique has valid coercion referent, motive accusations not narrator truth |
| PG-RL-0077 / RL0062 | Kairi → Momo / initially resists her aid choice, later asks Sae blame him and credits her rescue; locates her at bench, informs coupling, forces clarification encounter | EV0005–0006/0012/0045/0049; CL0006@7. Concrete support but selective protection not complete innocence; no new romantic declaration |
| PG-RL-0078 / NONE_ESTABLISHED | Kairi → Sae /11 dismisses danger deserved, then joins rescue and offers relational explanation/admits careless error53–54 | EV0003/0006–0007/0011–0012; CL0021@2. Initial withholding and later responsibility both, explanation not proof received/reform |
| PG-RL-0079 / RL0060 | Momo → Tōji / wants redo date, shares hand/embrace/company need, explicitly invites joint solution rather than secrecy | EV0015/0020/0022/0025–0027/0031/0033; CL0015@5/0017@4. Contextual need not limitless consent or entire character dependency |
| PG-RL-0080 / RL0061 | Tōji → Momo / comforting support and renewed promise prevent spread, pursues/calls Sae but withholds reason | EV0013/0015/0019–0022/0024–0029; CL0005@7/0023@1. Real care plus chosen information asymmetry; shared solution offered but not tried |
| PG-RL-0081 / RL0079 | Momo → Tōji / actual breakup132 resisted as inexplicable; repeated calls/bench/classroom search, correctly suspects blackmail169, begs truthful reason, final shock at kiss | EV0036/0038/0042/0045–0046/0050–0054; CL0015@5/0023@1. Correct inference not full bargain knowledge; public denial not proof no declaration occurred |
| PG-RL-0082 / RL0080 | Tōji → Momo / deliberately declares breakup with false changed-feeling account, hides despite receiving voicemail, repeats denial and performs preference kiss | EV0033–0040/0047–0054; CL0005@7/0015@5/0023@1. Actual withdrawal/deception injures; threat cause and Sae refusal counter freely changed love |
| PG-RL-0083 / RL0075 | Momo → Sae / after boundary Sae intrudes again; Momo tells stay out and accuses blackmail169 | EV0051–0052; CM0045. Situational confrontation does not make farewell forgiveness or freely renewed attachment |
| PG-RL-0084 / RL0066 | Sae → Tōji / break/date ultimatum, deadline control, rejects plea, hears actual breakup, fake-original leverage and public partnership claim | EV0017–0018/0028/0034–0035/0041/0044/0051; CL0002@7/0003@7. Possession claim not gained reciprocal affection; explicit refusal EV0040 |
| PG-RL-0085 / RL0067 | Tōji → Sae / refuses romance69/74/142–143, threatening grabs, attempts material recovery, coerced public coupling then initiates instrumental lip kiss | EV0017–0019/0039–0041/0044/0054; CL0005@7/0023@1. No sincere love established from contact; sudden instance explicit permission unshown |
| PG-RL-0086 / RL0072 | Kairi → Tōji / rescue cooperation, later physically catches/holds and insists face Momo rather than avoid | EV0006–0007/0048–0050; CL0006@7. Pressure for explanation not omniscient knowledge or successful truth exchange |

| Commitment/boundary / prior | Direction, terms and actual answer/consequence | Evidence / scoped state |
| --- | --- | --- |
| PG-CM-0044 / CM0041@2,CM0043 | Trio/Momo → endangered Sae / intended no-assault limit failed delivery; Momo reverses abandonment, trio actual visit and immediate rescue | EV0002–0008; RESCUE_PERFORMED, not retroactively safe consensual arrangement. Full unshown act history unproved |
| PG-CM-0045 / NONE | Momo → Sae / no engagement/talk/response anymore, explicit cannot forgive, goodbye46–48 | EV0010/0013; DECLARED/WITHDRAWN engagement, relief; Sae not respectful acceptance, later intrudes.169 confrontation does not undo meaning |
| PG-CM-0046 / CM0037,CM0040 | Tōji → Momo / actual breakup132, stated everything unwanted137; Momo asks why, later refuses authentic interpretation | EV0036/0038/0042/0046/0050–0054; UNILATERAL_WITHDRAWAL_DECLARED, reciprocal acceptance absent. Distinct from V06 jointly known STAGED_DECLARATION; continuing affection/cause separate |
| PG-CM-0047 / CM0039 | Sae → Tōji / break with Momo/date her for nondistribution; he refuses69/74, later performs breakup to her hearing but refuses date142–143; fake originals prolong coercion | EV0017–0019/0028/0033–0041/0044; INITIALLY_DECLINED then COERCIVE_CONDITIONAL_COMPLIANCE/PUBLIC_LABEL, no freely mutual romantic acceptance. Actual image destruction promise not fulfilled as represented |
| PG-CM-0048 / CM0037 | Tōji → Momo / promises protect and prevent spread despite threat; real local support/print burning, covert breakup and failed genuine-negative recovery | EV0019/0025–0029/0039–0041; PROTECTIVE_PROMISE_STRATEGY_COMPROMISED, actual mass dissemination not shown; not claimed simple fulfilled/breached solely by threat |
| PG-CM-0049 / NONE | Momo → Tōji / asks speak/solve together85, later actual voicemail meetup and direct request real reason; he conceals/hides/denies and supplies kiss display | EV0022/0042/0047–0054; REQUEST_UNMET_BY_CONDUCT, actual receipt confirmed161. No evidence Momo agreed to secrecy or sacrificial breakup |
| PG-CM-0050 / NONE | Tōji → Sae / suddenly pulls/initiates lip kiss172–174 as proof before Momo | EV0054; CONTACT_DEPICTED, EXPLICIT_PRIOR_PERMISSION_UNSHOWN for this instance; prior Sae desire/claimed relationship not automatic permission, no sincere affection entailed |

Exit: Momo/Tōji has actual unilateral breakup declaration and continuing disputed affection, RL0081/0082, not V06's mutually bounded script. Sae publicly claims Tōji while he explicitly rejected genuine dating and acts under leverage, RL0084/0085. Kairi advocacy does not establish reciprocity or full knowledge. Next RL0087, CM0051. Revision history0.6 — V07 directions/commitments, prior rows untouched, closure owner date2026-10-20.

## V08 successor transaction — PG-FR-V08

[V08 reading](../02%20Sequential%20Readings/PEACH_GIRL_V08_DEEP_READING.md) owns EV=PG-EV-V08. Learned at stated V08 frontier; snow/December, one-week absence, explicit three-month spring jump and later one-week plant interval, no invented exact date. HIGH actions/attributed statements, motive weighting bounded. Affection, public category, access and permission remain distinct.

| Direction / prior | From → to / actual transition | Evidence / scope |
| --- | --- | --- |
| PG-RL-0087 / RL0081 | Momo → Tōji / defends him18/believes coercion, seeks calls/read-note/joint action24, waits outside/pleads; after actual silence/phone-post, accepts enacted relationship end85 yet not affection's end | EV0003–0009/0014–0015/0018/0023; CL0023@2. Accurate core belief not full account; acts of seeking alongside injury |
| PG-RL-0088 / RL0082 | Tōji → Momo / rejected note/door/object, pained watch/tears, private protective explanation to Misao41–44, return phone by post; later starts aid103 before Kairi reaches | EV0003/0006–0014/0027; CL0005@8. Concealment persists, harm real; only-way-he-could-think not unique available response |
| PG-RL-0089 / RL0084 | Sae → Tōji / claims passionate preference10, resents telling Misao, asserts property62; orders towel99, demands/initiates kiss107–108 and resents wooden response109 | EV0002/0017/0026/0028; CL0002@8. Claims do not establish gained freely reciprocal love |
| PG-RL-0090 / RL0077 | Kairi → Momo / intercepts Sae, punches Tōji for Momo illness, repeated actual visit/outward activity/praise, buys despite objection, offers kiss69 but no kiss after stop | EV0006/0010/0019–0022; CL0006@8. Concrete aid/pressure coexist; no established full Tōji motive knowledge70 |
| PG-RL-0091 / RL0063 | Momo → Kairi / protests outing/purchase, later laughs/insists repayment, feels his words reach particularly80 and accepts comfort at realized end86 | EV0019–0023; CL0013@4. Prior romantic-pull history RL0041 and audit retained; no new settled dating label |
| PG-RL-0092 / NONE_ESTABLISHED_FOR_THIS_DIRECTION | Misao → Tōji / treats injuries, hears account and comforts, seeks negatives from Sae | EV0011–0012/0016. Care and advocacy not unqualified endorsement of his methods; no romantic inference |
| PG-RL-0093 / RL0091 | Momo → Kairi / relief at buffer96, tired of romance, publicly friend98; after Tōji/Sae kiss, unusually cheerful with him and worries whether leaning is cruel113 | EV0025–0030; CL0013@4. Current label/worry not complete generic-friend history or proof all enjoyment false |
| PG-RL-0094 / RL0090 | Kairi → Momo / cools burn first104, discovers absence118, finds124, embraces/apologizes, kisses and says loves131, carries132 | EV0027/0032/0034–0035. Actual care/desire, vulnerable encounter not verbal mutual pact, rescue not blank permission |
| PG-RL-0095 / NONE_ESTABLISHED_FOR_THIS_DIRECTION | Misao → Sae / asks negatives, confronts known threat/feelings, rejects fake cry; Sae denies then demands proof, later complains home visit | EV0016–0017. Direct source contradiction denial, institutional proof not established retrieval/action |
| PG-RL-0096 / RL0076 | Sae → Momo / false preference/stalker framing, unhappy laughter100, later actual turned foothills sign115 causes wrong route | EV0002/0005/0026/0031. Distinct from fans' harassment/lie; burn-push actor UNKNOWN |
| PG-RL-0097 / RL0093 | Momo → Kairi / kiss comfort/heartbeat then swept-along uncertainty, next-day dog/absence-of-flutter comparison, protests committee choice137 | EV0034–0037; CL0013@4. Counter settled romantic reciprocity, not proof all previous pull false; her will remains material |
| PG-RL-0098 / RL0087 | Momo → Tōji / still loves123, remembers kiss134, fine eraser/desk attachment141–142, hides rather than speaks144–146, tells Kairi love persists154 | EV0033/0036/0038–0041; CL0015@6. Public ended and private love coexist, no new actual Tōji conversation/reconciliation |
| PG-RL-0099 / RL0097 | Momo → Kairi / explicit154–155 still loves Tōji but Kairi more important than friend, fears losing/unsure love versus comfort; thanks continued presence164, warm laughter, rebuffs quick kiss166 then closing kiss168 | EV0041–0046; CL0013@4. Honest category uncertainty plus intensification, no explicit reciprocal dating pact/captive spoken confession securely assigned |
| PG-RL-0100 / RL0094 | Kairi → Momo / asks about kiss anger152, hears uncertainty, permits reliance156/support metaphor157, wants remain even while she loves Tōji163; sudden quick kiss166 and flower-language/closing kiss168 | EV0041–0046; CL0006@8/0017@5. Acceptance of actual position strong, not pure selflessness or blanket consent; quince substitution/error retains fallibility |
| PG-RL-0101 / NONE | V08 fan trio CHAR0019 → Momo / splash/using accusation111, lie to Kairi113 about her location; his118 contradiction challenge exposes account | EV0029–0032; CL0024@1. Social pressure affects self-doubt, not narrator verdict; Sae coordination not shown |
| PG-RL-0102 / RL0085 | Tōji → Sae / public presence/ordered compliance, pained reaction to Momo, passive unresponsive demanded kiss; she rebukes/shoves109 | EV0017/0026–0028. Actual coupling display not affirmative reciprocal affection, no new genuine consent/romance declaration |

| Commitment/boundary / prior | Actual terms and answer/consequence | Evidence / disposition |
| --- | --- | --- |
| PG-CM-0051 / CM0049 | Momo → Tōji / note/read request13 and shared-problem invitation24, continued causal belief; discarded note14/closed door, no full truthful answer | EV0003/0006–0009; REQUEST_UNMET. Receipt of content not proved because note not depicted read |
| PG-CM-0052 / CM0046 | Tōji → Momo / rejects restart14–15, says leave27, returns birthday prints/breaks scent and posts phone49–50 | EV0003/0007–0009/0014; UNILATERAL_RUPTURE_ENACTED_CONTINUES, not new freely changed love or prior joint script |
| PG-CM-0053 / NONE | Kairi → Momo / daily visits until well reportedly promised, actual visit66 plus repeatedness indicated; school reminder84 | EV0019/0023; PARTIALLY_OBSERVED_PERFORMANCE, not invented exact visit count/duration |
| PG-CM-0054 / NONE | Momo → Kairi / says stop to kiss offer69, no actual kiss follows there | EV0019; SPECIFIC_REFUSAL_HEEDED_AT_THIS_INSTANCE. Later kisses do not rewrite it; earlier outing pressure retained |
| PG-CM-0055 / NONE | Momo → Kairi / refuses free purchased outfit, intends repay with New Year cash78 despite his gift request | EV0021–0022; REPAYMENT_INTENT_DECLARED_NOT_PAYMENT_SHOWN. No silent gift debt/romantic obligation |
| PG-CM-0056 / NONE | Kairi → Momo / unilaterally volunteers both for beautification137, she objects her will ignored, both actual work139/151 | EV0037/0041; CHOICE_IMPOSED_WITH_PROTEST, practical buffering rationale not prior permission |
| PG-CM-0057 / NONE | Momo → Kairi / tells still loves Tōji154, more-than-friend importance but uncertain romantic feeling155/wants not lose | EV0041–0042; DISCLOSURE_RECEIVED, no false fully reciprocal confession/dated-couple agreement |
| PG-CM-0058 / NONE | Kairi → Momo / may rely/use him156, need not recover alone157, wants beside even if loves Tōji163; she thanks164 | EV0042–0044; UNCERTAIN_PROXIMITY_ACCEPTED_ON_DISCLOSED_TERMS. Not guarantee future feeling or unlimited contact permission |
| PG-CM-0059 / NONE | Kairi → Momo / sudden quick kiss166 after lip touch; surprised Momo rebukes getting carried away/strikes back comic panel | EV0045; CONTACT_ACTUAL_PRIOR_EXPLICIT_PERMISSION_UNSHOWN_REBUFF_DEPICTED. Accepted staying not permission for this instance |
| PG-CM-0060 / NONE | Kairi/Momo / actual128/130 kiss with no depicted explicit stop at that instance, Momo later swept-along/uncertain; final168 kiss after chin contact167, eyesclosed/hand-shirt | EV0035–0036/0046; CONTACT_AND_AMBIVALENCE_DISTINCT, no invented verbal refusal128 or automatic permanent consent/reciprocal dating. Earlier69/further166 responses retained |

Momo/Sae no new forgiveness or freely restored friendship; Sae violating boundary does not revoke Momo's V07 farewell. Directional histories do not collapse into triangles without individual frontiers. Next RL0103, CM0061. Revision0.7 — V08 successors2026-10-20, older rows retained.
