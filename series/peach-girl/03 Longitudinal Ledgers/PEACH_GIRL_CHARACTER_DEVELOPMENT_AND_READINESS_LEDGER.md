---
title: "Peach Girl — Character Development and Readiness"
artifact_id: PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER
artifact_type: character_development_readiness_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.14"
status: active_provisional
scope: "Character Development and Readiness; source-derived records through the committed high-water mark named in the entrypoint"
source_boundary: "Original Japanese 新装版 mainline; admitted volumes through the entrypoint's committed high-water mark; prospective rows carry their own frontier"
canonical_home: series/peach-girl/03 Longitudinal Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character Development and Readiness

This instrument owns verified local subject identity, character-level developmental/decision state and readiness derived from that evidence. The [architecture](../00%20Frameworks%20and%20Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md#character-reconstruction-contract) owns the reconstruction contract. Pair feelings/commitments belong in the relationship ledger; proposition knowledge and public reputation belong in the information ledger; arguments and revisions belong in the claims ledger.

Development and readiness share a home because promotion depends on this same subject's state coverage and gaps. They are distinct record types. No character name, trait, psychological conclusion or readiness assessment is prepopulated.

## Records and allocation

| Type / stable identifier | Required fields |
| --- | --- |
| Subject `PG-CHAR-####` | Source-spelled name or bounded unnamed identity; alias/language/basis if inspected; continuity; first observation; identity uncertainty; any actually curated global IDs, otherwise null |
| Development event `PG-CS-####` | Subject; represented time/range and certainty; learned-after source frontier; previous state; event kind; observed action; attributed intention/self-report; options and constraints; recipient/response/consequence where relevant; observation refs; claim/version; interpretation and alternative; support strength/basis; correction link |
| Current subject view | Subject + temporal/disclosure boundary; active event IDs/versions; scoped formulation; unresolved contradictions and unobserved contexts |
| Readiness decision `PG-RD-####` | Subject + target artifact/domain; source and Git evidence cutoff; context diversity; supporting/counterevidence; written-language/form coverage; missing domains; validation status; assessment/reviewer/date; prior decision; governing claim versions |

Event kinds: `DISPOSITION_CHANGE / KNOWLEDGE_CHANGE / RELATIONSHIP_CHANGE / CONTEXT_CHANGE / REVEALED_NOT_NEW / UNRESOLVED`. Link the authoritative knowledge or relationship row; do not restate its entire proposition. Actor-level agency records actual choice processes; the relationship ledger owns their pair-state consequences. A new disclosure of an old habit does not establish newly developed behavior.

Readiness states: `UNASSESSED / INSUFFICIENT_EVIDENCE / BOUNDED_PROVISIONAL / DOMAIN_READY`. These are local scoped assessments, not artifact authority or global capability grades. No row is needed merely to assign every mentioned subject UNASSESSED.

## Evidence, update and history

Allocate an ID only on actual admitted evidence, monotonically within its prefix; never recycle it. Distinguish identity uncertainty, source legibility, timing and interpretation uncertainty. Every state event requires a reading's `PG-EV-VNN-####` with exact locator and disclosure frontier. A self-report can be recorded without being endorsed as a stable trait. A consequential interpretation also points to a `PG-CL-####@version`, supporting evidence, strongest available counterevidence and plausible alternative.

A future VNN transaction appends events for material goal/choice/development changes, newly disclosed state or a consequential contradiction. Ordinary momentary mood stays local unless it changes the model. Update readiness only when an actual proposal is assessed or evidence materially changes an existing assessment. Independent contexts and failures matter; repeated shots of one encounter are not independent tests.

Preserve original names/identity allocation, event formulations, source frontiers and assessment history. Amend the current view through targeted edits with an appended event/revision; retain old versions. Later retrospective explanation has its actual learned-after frontier. A frozen `PG-FR-VNN` cites the versions then active and contains enough state to recover them after this ledger advances. Errata append a reason and replacement link.

The sequential closeout certifies this instrument updated or records no material change without a dummy row. Bootstrap source-derived subject, event, current-state and readiness rows: **0**.

## Subject register

| Subject | Source identity / aliases and basis | Continuity / first observation | Identity uncertainty / global IDs |
| --- | --- | --- | --- |
| PG-CHAR-0001 | 安達もも (Adachi Momo). Surname from classmates at i0007; given name written もも at i0031; called ももちゃん / もも; first-person narrator | Original mainline; PG-EV-V01-0001 (i0007) | None; global ID null |
| PG-CHAR-0002 | 東寺ヶ森 (Tōjigamori), called とーじ by Momo; given name カズヤ called at i0065 (kanji 一矢 shown as a label at i0016, MODERATE) | Original mainline; PG-EV-V01-0004 (i0013) | Kanji of given name MODERATE; global ID null |
| PG-CHAR-0003 | 柏木沙絵 (Kashiwagi Sae), called さえ / さえちゃん; full name at i0015 | Original mainline; PG-EV-V01-0002 (i0009) | None; global ID null |
| PG-CHAR-0004 | 岡安浬 (Okayasu Kairi), furigana カイリ, i0024; called カイリ, 岡安; Momo calls him バカ安 | Original mainline; PG-EV-V01-0007 (i0022) | None; global ID null |
| PG-CHAR-0005 | School nurse, called 操ちゃん by Kairi (i0098); surname not given | Original mainline; i0097 | Given name only; global ID null |
| PG-CHAR-0006 | Leader of Kairi's female fan bloc (wavy hair), unnamed | Original mainline; PG-EV-V01-0014 (i0036–i0041) | Unnamed; may be one of the hallway girls elsewhere; not merged |
| PG-CHAR-0007 | Unnamed middle-school friend who reported Tōji's alleged dislike of dark skin | Reported in flashback, PG-EV-V01-0027 (i0077) | Unnamed; identity unknown |
| PG-CHAR-0008 | Tōji's mother (unnamed); answers the family phone, calls her son 一矢 (furigana かずや) | Mainline; PG-EV-V02-0012 (i0050) | Unnamed; global ID null |
| PG-CHAR-0009 | Momo's mother (unnamed); works, wakes Momo for school | Mainline; i0054 | Unnamed; global ID null |
| PG-CHAR-0010 | 小川 (Ogawa), called カコ; classmate in Sae's group (i0065–i0066) | Mainline; PG-EV-V03-0015 | Given name only by nickname; global ID null |
| PG-CHAR-0011 | Unnamed male admirer of Sae whose movie ticket she tore (V01 i0118–0119); testifies at V03 i0164 | Mainline; V01 i0118 | Unnamed; link V01/V03 by depiction (MODERATE) |
| PG-CHAR-0012 | Bounded group: girls whose boyfriends Sae reportedly stole (i0162–i0163) | Mainline; PG-EV-V03-0035 | Group; members unnamed |
| PG-CHAR-0007 (identity update, appended) | Identified as キョーちん, Momo's middle-school friend, who admits fabricating the report (V03 i0044–i0046) | First identified PG-EV-V03-0010 | Nickname only |
| PG-CHAR-0013 | すみれ (Sumire), class 1-1; a girl Sae hurt in her first year of middle school; recruited by Kairi for the V03 testimony | Mainline; PG-EV-V04-0014 (i0067) | Given name only; probably one of the V03 i0162–i0163 testifiers (PG-CHAR-0012), not merged; global ID null |
| PG-CHAR-0014 | 本田 (Honda), editor of the magazine MEN'S MON×2 (business card i0132; addressed 本田さん i0147) | Mainline; PG-EV-V04-0030 (i0130) | Given name on card partly legible; global ID null |
| PG-CHAR-0015 | 大路吾郎 (Ōji Gorō), 19, called ジゴロー (Jigoro) and 吾郎ちゃん; MEN'S MON×2 No. 1 model (in-story profile box i0136) | Mainline; PG-EV-V04-0030, -0035 (i0136, i0149) | None; global ID null |
| PG-CHAR-0016 | Bounded group: second-year girls of the swim club (水泳同好会), four shown; one called レイ | Mainline; PG-EV-V04-0012 (i0058) | Group; members mostly unnamed |
| PG-CHAR-0017 | Bounded group: Mayu's (マユ) group, classmates Sae used to mock, who bully her after the exposure | Mainline; PG-EV-V04-0022 (i0099) | Group; may overlap the gym and spray-paint bullies; not merged |

## Developmental events

| Event / version | Subject / prior | Story time / learned after | Kind / action / intention / options / consequences | Evidence / claim version | Uncertainty / counterreading / correction |
| --- | --- | --- | --- | --- | --- |
| PG-CS-0001@1 | PG-CHAR-0001 / — | Before series start (middle school → high-school entry) / V01 | REVEALED_NOT_NEW: chose her high school because Tōji applied there; long concealed love; two-year sun-avoidance regimen as a precondition for confessing | PG-EV-V01-0006, -0021, -0027; PG-CL-0008@1 | Self-report via narration; durations are her own |
| PG-CS-0002@1 | PG-CHAR-0001 / CS-0001 | Opening day / V01 | DISPOSITION_CHANGE (local): under threat of exposure she tells a deliberate decoy lie to Sae (Kairi). Options: deny, deflect, tell the truth. Chose deception. Consequence: premise for the graffiti accusation; later used against her | PG-EV-V01-0007, -0011, -0040 | Panic response; one instance |
| PG-CS-0003@1 | PG-CHAR-0004 / — | Two years before story (both in 2nd year of middle school) / V01 i0048 | REVEALED_NOT_NEW: was rescued from drowning by Momo; believes she gave him mouth-to-mouth; afraid of water since | PG-EV-V01-0017, -0022; PG-CL-0007@1 | Who gave CPR is disputed |
| PG-CS-0004@1 | PG-CHAR-0004 / CS-0003 | ~1 week after opening day / V01 | DISPOSITION_CHANGE: from flirtatious stranger to active pursuer of Momo (public kiss claim, kiss, repeated advances, proposal i0168) | PG-EV-V01-0013, -0018, -0019, -0029, -0050; PG-CL-0006@1 | Sincerity vs game unresolved |
| PG-CS-0005@1 | PG-CHAR-0002 / — | DayA+1 (D-4) / V01 | KNOWLEDGE_CHANGE: learns by overhearing that Momo has loved him since middle school, and of the tan report → link PG-KN-0004 | PG-EV-V01-0026, -0028 | Acquired without Momo's consent |
| PG-CS-0006@1 | PG-CHAR-0002 / CS-0005 | D-3 / V01 | RELATIONSHIP_CHANGE: confesses (「オレも安達のことが好きだ」); see PG-CM-0001 | PG-EV-V01-0032, -0033 | — |
| PG-CS-0007@1 | PG-CHAR-0003 / — | D-4 to D0 / V01 | DISPOSITION_CHANGE (revealed through action): moves from imitation and competitive flirting to engineered misinformation aimed at the Momo–Tōji relationship (TX-0006…0011) | PG-EV-V01-0034, -0038, -0040, -0042, -0043, -0049, -0052; PG-CL-0002@1, PG-CL-0003@1 | Motive mix unresolved |
| PG-CS-0008@1 | PG-CHAR-0001 / CS-0001 | D-2 / V01 | CONTEXT_CHANGE: asks Tōji to keep their relationship secret, especially from Sae; option to tell Sae refused | PG-EV-V01-0037; PG-CM-0002 | Rationale given: rumor; underlying distrust of Sae |
| PG-CS-0009@1 | PG-CHAR-0001 / CS-0008 | D-1 to D0 / V01 | KNOWLEDGE_CHANGE: receives Sae's claim and finds the packet; doubts Tōji; avoids him without asking; at D0 refuses his kiss | PG-EV-V01-0040, -0041, -0053 | Her inference is reasonable from her information; the information was false or engineered |
| PG-CS-0010@1 | PG-CHAR-0002 / CS-0006 | D0 / V01 | KNOWLEDGE_CHANGE + action: believes Sae's fabricated report that Momo prefers Kairi; forcibly takes Momo to the pergola and attempts a kiss | PG-EV-V01-0051, -0052, -0053; PG-CL-0005@1 | Interior withheld at i0175–i0178 |
| PG-CS-0011@1 | PG-CHAR-0002 / CS-0010 | V01 D0 evening / V02 | DISPOSITION_CHANGE (repair): apologizes in person at Momo's house for the pergola attempt; attributes it to jealousy | PG-EV-V02-0001, -0004; PG-CL-0005@2 | Omits Sae's report |
| PG-CS-0012@1 | PG-CHAR-0002 / — | Before the relationship / V02 i0137 | REVEALED_NOT_NEW: long-standing insecurity about Kairi; confession hurried by fear after the pool rescue | PG-EV-V02-0033; PG-CL-0005@2 | Self-report |
| PG-CS-0013@1 | PG-CHAR-0002 / CS-0011 | V02 day 1–2 / V02 | KNOWLEDGE_CHANGE + choice: believes Sae's staged injury and bruise; sides with Sae; 「見損なったよ」 | PG-EV-V02-0009, -0010; PG-CL-0003@2 | Trust heuristic: Sae has no motive (i0111) |
| PG-CS-0014@1 | PG-CHAR-0001 / CS-0009 | V02 / V02 | KNOWLEDGE_CHANGE: accurate model of Sae as liar and imitator; decides on full disclosure to Tōji, including her own decoy lie | PG-EV-V02-0010, -0011, -0012 | — |
| PG-CS-0015@1 | PG-CHAR-0001 / CS-0014 | Hospital day / V02 | DISPOSITION_CHANGE (escalation): threatens to jump from a fourth-floor window to compel a hearing; falls and is caught | PG-EV-V02-0027, -0029; PG-CL-0011@1 | Comic register; real risk |
| PG-CS-0016@1 | PG-CHAR-0001 / — | Before the series (first week of high school) / V02 i0092 | REVEALED_NOT_NEW: rubella absence, isolation, rumors; Sae befriended her | PG-EV-V02-0023 | Momo's account; abortion rumor heard via Sae |
| PG-CS-0017@1 | PG-CHAR-0003 / CS-0007 | V02 / V02 | DISPOSITION_CHANGE (escalation): fabricated injuries; information blockade; staged kiss; planned coercive 'fait accompli'; states goal 「あたしはとーじが欲しい」 | PG-EV-V02-0009, -0017, -0021, -0028, -0030, -0031; PG-CL-0002@2, PG-CL-0003@2 | Plan not executed in V02 |
| PG-CS-0018@1 | PG-CHAR-0004 / CS-0004 | V02 / V02 | Choice: refuses alliance with Sae against Momo–Tōji; acts as Momo's main ally; admits he exploited the kiss rumor | PG-EV-V02-0026, -0032; PG-CL-0006@2 | Still pursuing Momo |
| PG-CS-0019@1 | PG-CHAR-0002 / CS-0013 | Hospital day / V02 | RELATIONSHIP_CHANGE: proposes breaking up (「別れよう」), citing loss of confidence | PG-EV-V02-0040; PG-CL-0009@1 | Momo's response unshown |
| PG-CS-0020@1 | PG-CHAR-0001 / CS-0015 | Hospital day / V03 | RELATIONSHIP_CHANGE: answers the breakup proposal with 「こっちから別れてやる」 and throws fruit at Tōji; then regrets it | PG-EV-V03-0001, -0011 | — |
| PG-CS-0021@1 | PG-CHAR-0001 / CS-0001 | Middle school / V03 | REVEALED_NOT_NEW: crush origin (ball return); sunscreen began after the friend's report | PG-EV-V03-0008 | Visual flashback only |
| PG-CS-0022@1 | PG-CHAR-0001 / CS-0021 | Before the swim meet / V03 | KNOWLEDGE_CHANGE: learns the tan report was a lie; tan-avoidance motive dissolved | PG-EV-V03-0010; PG-CL-0008@2 | — |
| PG-CS-0023@1 | PG-CHAR-0001 / CS-0022 | Swim-meet day / V03 | DISPOSITION_CHANGE: chooses to swim fully, out of defiance of Sae; recovers the pleasure of swimming; rescues Kako, her assailant | PG-EV-V03-0013, -0015 | Local to the meet; complexion concerns may return |
| PG-CS-0024@1 | PG-CHAR-0001 / — | Swim-meet day / V03 | DISPOSITION_CHANGE: self-reported fluttering and reliance toward Kairi, framed as a lapse; irritation at his flirting | PG-EV-V03-0017, -0022; PG-CL-0013@1 | Category of the feeling unresolved |
| PG-CS-0025@1 | PG-CHAR-0001 / CS-0024 | Swim-meet day / V03 | Choice: slaps Sae and publicly defends Kairi's character; refuses forced apology | PG-EV-V03-0029, -0030 | — |
| PG-CS-0026@1 | PG-CHAR-0001 / CS-0020 | Swim-meet day / V03 | RELATIONSHIP_CHANGE: refuses Tōji's request to restart while wanting it | PG-EV-V03-0037; PG-CL-0012@1 | Reason unstated |
| PG-CS-0027@1 | PG-CHAR-0002 / CS-0019 | Swim-meet day / V03 | KNOWLEDGE_CHANGE + choice: overhears Sae's method; publicly frees and claims Momo; apologizes; privately retracts the claim and asks to restart | PG-EV-V03-0025, -0032, -0033, -0037; PG-CL-0005@3 | — |
| PG-CS-0028@1 | PG-CHAR-0003 / CS-0017 | Swim meet / V03 | CONTEXT_CHANGE: instructs sabotage; threatens a false accusation; explains her method; exposed by testimony; abandoned by her coalition | PG-EV-V03-0014, -0015, -0024, -0025, -0035, -0036 | Still asserts victimhood |
| PG-CS-0029@1 | PG-CHAR-0001 / CS-0026 | Day after the swim meet to end of term / V04 | DISPOSITION_CHANGE + RELATIONSHIP_CHANGE: states the reason for refusing (fear of not being believed); after Kairi's confrontation recognizes her 被害者意識 as avoidance of rejection; apologizes and asks Tōji to go out again | PG-EV-V04-0003, -0006, -0007, -0009; PG-CL-0012@2, PG-CL-0015@1 | — |
| PG-CS-0030@1 | PG-CHAR-0001 / CS-0024 | Start of second term / V04 | KNOWLEDGE_CHANGE: learns from Sumire that Kairi organized the V03 testimony; reinterprets his changing-room embrace as farewell; apologizes, thanks him and leaves a counterfactual unfinished | PG-EV-V04-0014…0018; PG-CL-0013@2 | Category of feeling still unresolved |
| PG-CS-0031@1 | PG-CHAR-0001 / CS-0023 | Start of second term / V04 | CONTEXT_CHANGE: joins the swim club despite tan worries; Tōji accepts her however tanned; reports being happy at school | PG-EV-V04-0012, -0031 | Complexion worry persists (i0025, i0061) |
| PG-CS-0032@1 | PG-CHAR-0001 / — | Second term / V04 | Choice: pushes away Tōji's kiss though she wants it; proposes the L sign; demands verbal 「好き」 | PG-EV-V04-0019…0021, -0024; PG-CL-0017@1 | 'Second time' referent unlocated |
| PG-CS-0033@1 | PG-CHAR-0001 / CS-0025 | Second term / V04 | Choice: declines to retaliate against Sae; partners with her in gym, recalling Sae's first approach; predicts Sae will learn others' pain | PG-EV-V04-0022, -0025, -0026 | Prediction contradicted by private Sae conduct |
| PG-CS-0034@1 | PG-CHAR-0002 / CS-0027 | End-of-term ceremony / V04 | Choice: shaves his head as 「けじめと戒め」; names his error (believing Sae without seeing or hearing for himself); accepts Momo's request | PG-EV-V04-0008, -0009; PG-CL-0005@4 | Verbal acceptance not shown |
| PG-CS-0035@1 | PG-CHAR-0002 / CS-0034 | Second term / V04 | Choice: overcomes embarrassment to make the private sign publicly; forehead kiss | PG-EV-V04-0028, -0029; PG-CL-0017@1 | — |
| PG-CS-0036@1 | PG-CHAR-0003 / CS-0028 | Second term / V04 | CONTEXT_CHANGE: ostracized and bullied; outwardly servile to Momo; privately fantasizes Momo's humiliation and stamps on her shoes | PG-EV-V04-0011, -0022, -0025, -0027, -0032, -0033; PG-CL-0016@1 | Sincerity of relief at Momo's kindness unresolved |
| PG-CS-0037@1 | PG-CHAR-0003 / CS-0036 | Late September / V04 | CONTEXT_CHANGE: becomes a magazine candidate; deceives staff and Jigoro; exaggerates at school; rescued and asked out by Jigoro | PG-EV-V04-0034…0040; PG-CL-0003@4, PG-CL-0018@1 | Her answer not shown |
| PG-CS-0038@1 | PG-CHAR-0004 / — | Day after the meet to second term / V04 | Choice: tells Misao he lost; discloses that the V01 line was Tōji's; confronts Momo; counsels Tōji; withdraws; deflects Momo's thanks with jokes | PG-EV-V04-0002, -0005, -0006, -0008, -0013, -0016, -0017; PG-CL-0006@4 | Stated opportunism versus considerate cover |
| PG-CS-0039@1 | PG-CHAR-0015 / — | Late September / V04 | Introduction: reputed aloof with women; attracted to Sae on contact; forms a hostile belief about Momo from Sae's account; rescues Sae and asks her out | PG-EV-V04-0035, -0037, -0039, -0040; PG-CL-0018@1 | Basis of attraction thin |

## Current subject state

| Subject / boundary | Active event versions | Scoped state | Unresolved evidence / contexts |
| --- | --- | --- | --- |
| PG-CHAR-0001 @ PG-FR-V01 | CS-0001, -0002, -0008, -0009 | Combative in public, anxious and planful in romance; relies on second-hand reports about Tōji; in crisis after refusing his kiss | No family, home or non-romantic daily-life context yet |
| PG-CHAR-0002 @ PG-FR-V01 | CS-0005, -0006, -0010 | Protective, private, inexperienced; trusts Sae; misinformed about Momo | Interior largely withheld |
| PG-CHAR-0003 @ PG-FR-V01 | CS-0007 | Imitative and status-seeking; deliberately deceives both Momo and Tōji | Motive weighting; authorship of graffiti, notes, packet |
| PG-CHAR-0004 @ PG-FR-V01 | CS-0003, -0004 | Provocative, intrusive, attentive; protective in danger; pursuing Momo with stated seriousness | Sincerity; family background (claimed sister unverified) |
| PG-CHAR-0001 @ PG-FR-V02 | CS-0001, -0002, -0008, -0009, -0014, -0015, -0016 | Accurate about Sae; escalates when disbelieved; candid with Tōji about her own lie; harassed at school | Home life thin (mother appears once) |
| PG-CHAR-0002 @ PG-FR-V02 | CS-0005, -0006, -0010…0013, -0019 | Sincere, insecure about Kairi, trusting of Sae but beginning to doubt; proposes breakup | Response to proof of Sae's lies |
| PG-CHAR-0003 @ PG-FR-V02 | CS-0007, -0017 | Strategic deceiver with stated goal Tōji; physically staged deceptions; self-describes 'mind control' | Imitation vs desire weighting |
| PG-CHAR-0004 @ PG-FR-V02 | CS-0003, -0004, -0018 | Ally and suitor; refuses foul play | Sincerity tested further |
| PG-CHAR-0001 @ PG-FR-V03 | CS-0020…0026 | Vindicated; tan motive dissolved; new feelings for Kairi she disavows; refuses Tōji for now | Reason for refusal |
| PG-CHAR-0002 @ PG-FR-V03 | CS-0027 | Disillusioned with Sae; accountable; seeking to restart | Response to refusal |
| PG-CHAR-0003 @ PG-FR-V03 | CS-0028 | Socially isolated; exposed | Next strategy |
| PG-CHAR-0004 @ PG-FR-V03 | CS-0018 + V03 actions | Strategist ally; still suitor; publicly flirtatious with others | Sea trip; feelings |
| PG-CHAR-0001 @ PG-FR-V04 | CS-0029…0033 | Self-aware about her victim complex; reunited and happy; swim club; grateful to Kairi; tolerant of Sae | Category of Kairi feeling; Jigoro's hostility unknown to her |
| PG-CHAR-0002 @ PG-FR-V04 | CS-0034, -0035 | Accountable, reticent but willing to pay small public costs; jealous of Kairi | — |
| PG-CHAR-0003 @ PG-FR-V04 | CS-0036, -0037 | Isolated at school; performatively servile; deceiving outsiders; asked out by a celebrity | Her answer and next use of Jigoro |
| PG-CHAR-0004 @ PG-FR-V04 | CS-0038 | Withdrawn ally; feelings deflected through jokes | Feelings; next role |
| PG-CHAR-0015 @ PG-FR-V04 | CS-0039 | Misinformed about Momo; pursuing Sae | Whether he learns the truth |

## Readiness assessments

| Assessment / prior | Subject / target / domain / cutoff | Evidence diversity / counterevidence | Gaps / validation | Assessment / reviewer / date / claim versions |
| --- | --- | --- | --- | --- |

Revision history: 0.1 — bootstrap schema, zero rows, 2026-10-16 UTC. 0.2 — V01 transaction rows appended (frontier PG-FR-V01), 2026-10-16 UTC. V02 transaction rows appended (frontier PG-FR-V02), 2026-10-16 UTC. V03 transaction rows appended (frontier PG-FR-V03), 2026-10-17 UTC. V04 transaction rows appended (frontier PG-FR-V04), 2026-10-17 UTC.

## Recipient audit boundary PG-AUDIT-20261019

New owner-authorized, non-blind V01–V04 correction pass; see the [source audit](../07%20Audits%20and%20Handoffs/PEACH_GIRL_CODEX_V01_V04_SOURCE_AUDIT_20261019.md). Learned after PG-FR-V04, before opening V05; narrative cutoff V04. Earlier frozen-boundary projections above are historical, not competing current authority. Submitted historical rows remain unchanged; original unsuffixed event rows have implicit version 1. The following successor versions and audit projections govern current retrieval until the next transaction. Corrections change the analyst's account, not characters' historical knowledge.

| Corrective version / original | Subject / represented source time | Corrected state and limits | Evidence / claim / issue |
| --- | --- | --- | --- |
| PG-CS-0024@2 / CS-0024@1 | PG-CHAR-0001 / swim meet, V03 | Self-reported fluttering, reliance and desire for Kairi's attention, with self-disavowal. Romantic pull is supported; chosen love/relationship not established | PG-EV-V03-0017, -0022; i0100, i0104–0106; PG-CL-0013@3; A03 |
| PG-CS-0029@2 / CS-0029@1 | PG-CHAR-0001 / end of first term, V04 | Names fear of renewed disbelief and adopts Kairi-prompted self-criticism; then hears Tōji's independent accountability; still names his faults while choosing to restart with the remorseful present person. Earlier injury remains real | PG-EV-V04-0003, -0006…0009; i0029–0048; PG-CL-0015@2; A05 |
| PG-CS-0030@2 / CS-0030@1 | PG-CHAR-0001 / second term, V04 | Learns Kairi's orchestration; gratitude and grief coexist with an unfinished romantic counterfactual and wish for continuing closeness. No friendship-only category or love declaration established | PG-EV-V04-0014…0018; i0074–0085; PG-CL-0013@3; A03 |
| PG-CS-0032@2 / CS-0032@1 | PG-CHAR-0001 / second term, V04 | Refuses approach despite desire; seeks expression/initiative. V01 i0177 is a known earlier refusal candidate, but swim-club girls' exact referent remains UNKNOWN | PG-EV-V01-0053; PG-EV-V04-0019…0021, -0024; A08 |
| PG-CS-0035@2 / CS-0035@1 | PG-CHAR-0002 / second term, V04 | Publicly makes private sign; affectionate interrupted staging/contact at i0128. Exact contact anatomy uncertain; inherited 'forehead' over-specific. Disclosed V05 warning not yet directly inspected | PG-EV-V04-0028, -0029; i0125–0128; PG-CL-0017@1; A09 |
| PG-CS-0038@2 / CS-0038@1 | PG-CHAR-0004 / end of first term to second term, V04 | Supports reunion, withdraws/deflects gratitude and retains desire in a sexualized joking standing offer. Care and opportunism may coexist; motive weighting UNKNOWN | PG-EV-V04-0002, -0005, -0006, -0008, -0013, -0016, -0017; PG-CL-0006@5; A04 |

| Current subject / boundary | Active corrective versions | Scoped current retrieval | Unresolved |
| --- | --- | --- | --- |
| PG-CHAR-0001 @ PG-AUDIT-20261019 | CS0024@2, CS0029@2, CS0030@2, CS0032@2; unchanged CS0031@1/0033@1 | Chooses Tōji after real injury and new repair; romantic pull/gratitude/grief toward Kairi remain; refuses particular approaches despite desire; rejects peer retaliation against Sae | Kairi feeling's extent/category; motive/knowledge limits in audit |
| PG-CHAR-0002 @ PG-AUDIT-20261019 | CS0034@1, CS0035@2 | Credulity has caused harm; independently acknowledges it; reticent but responsive in current relationship | Exact i0128 contact pending sequential V05 |
| PG-CHAR-0004 @ PG-AUDIT-20261019 | CS0038@2 | Helpful ally and continuing suitor; restraint, deflection, humor and desire coexist with earlier boundary-crossing conduct | Mixed motives; deeper contexts unavailable |

Readiness remains UNASSESSED: narrative evidence exists, but no operational reconstruction proposal/testing has been completed. Next new IDs remain CS0040 and RD0001; these corrections consumed versions, not new event numbers.

Revision history addendum: recipient source-audit successor corrections, 2026-10-19; original frozen states preserved.

## V05 successor transaction — PG-FR-V05

New Codex Route B evidence, learned after PG-AUDIT-20261019; [V05 reading](../02%20Sequential%20Readings/PEACH_GIRL_V05_DEEP_READING.md) owns all PG-EV-V05 observations. Current views here supersede earlier boundary projections for retrieval, preserving their historical meanings. All new events are @1 unless stated; story time runs from proposal to Momo's sixteenth-birthday night. Abbreviated EV/CL/RL/CM IDs retain their PG prefixes.

| Event / subject / prior | Time and kind / observed choice, self-report and consequences | Evidence / governing claim / alternatives and limits |
| --- | --- | --- |
| PG-CS-0035@3 / CHAR0002 / CS0035@2 | REVEALED_NOT_NEW / V04 contact: V05 i0051 explicitly calls first kiss cheek, not forehead. Analyst erratum learned V05; original versions unchanged | EV0013; CL0017@2; disclosed warning non-blind; audit uncertainty now resolved |
| PG-CS-0040@1 / CHAR0003 / CS0037@1 | CONTEXT_CHANGE / public heroine, magazine win and goods restore prestige but not comparative satisfaction; explicitly rejects Jigoro and wants Tōji | EV0001–0011/0015; CL0002@5; specific desire plus rivalry, not a timeless inability to feel |
| PG-CS-0041@1 / CHAR0002 / — | REVEALED_NOT_NEW / V01 practice encounter: says could seriously resist but wanted experience for Momo; new retrospective account, not new V05 action | EV0017; CM0008@3/IP0020@2; initial refusals and guilt-colored testimony retained |
| PG-CS-0042@1 / CHAR0002 / CS0034@1 | DISPOSITION_CHANGE tested locally / refuses new Sae love/kiss requests, turns head and pushes away; no willing affair established | EV0014/0017–0018; CL0005@5; compassion/self-blame coexist with actual refusal |
| PG-CS-0043@1 / CHAR0001 / CS0032@2 | RELATIONSHIP_CHANGE / knowingly contests garden staging, slaps Tōji, initiates kiss, uses territorial/competitive language and receives affection; chooses more intimacy | EV0019–0020; RL0052/CM0029; no idealized permanent solution or ignored initial surprise |
| PG-CS-0044@1 / CHAR0002 / CS0035@3 | CONTEXT_CHANGE / independently selects gift, prepares party mainly with delivery, checks Momo's response during intimacy; ordinary care beyond crisis apology | EV0024–0029; CL0005@5/0017@2; limited-context assent, no completed intercourse claim |
| PG-CS-0045@1 / CHAR0001 / CS0033@1 | Choice under false information / offers joint help, then goes alone for Sae's supposed emergency; intends return/call, drinks offered can without knowledge of scheme; loses capacity, carried away | EV0030–0032; RL0056/CM0032/IP0050; helping is not choosing Jigoro |
| PG-CS-0046@1 / CHAR0003 / CS0040@1 | DISPOSITION_CHANGE escalation / isolates Momo, recruits Jigoro, copies clothes/wig/scent, impersonates Momo, obstructs search and urges act regardless of waking; frightened by Tōji but continues | EV0022–0023/0027/0030–0035/0040/0044–0045; CL0002@5/0003@5; fear does not establish remorse, chemical means unshown |
| PG-CS-0047@1 / CHAR0015 / CS0039@1 | Choice/context / initial refusal and proposed direct confrontation yield to Sae appeal; later sees incapacity, removes Momo, controls access and agrees prospectively; final wish claim | EV0022–0023/0032/0036–0037/0041/0045/0048; CL0018@2; misinformation and personal responsibility coexist, outcome unknown |
| PG-CS-0048@1 / CHAR0002 / CS0042@1 | KNOWLEDGE_CHANGE + choice / fooled by copied identity, detects tune mismatch, identifies Sae and refuses her; distressed, denies false Momo choice, calls/verifies, lies for apartment access and compels search assistance; infers hotel | EV0034–0046; CL0005@5/0019@1; no physical rescue yet, harsh/possessive conduct retained |
| PG-CS-0049@1 / CHAR0001 / CS0045@1 | UNRESOLVED / impaired perception substitutes Tōji, loses interval, wakes afraid and bewildered by unfamiliar hotel and Jigoro assertion | EV0037/0047–0048; IP0051; fear not confirmation of feared act, no voluntary choice of Jigoro established |

| Current subject / boundary | Active material events | Scoped state / remaining gaps |
| --- | --- | --- |
| CHAR0001 @ PG-FR-V05 | CS0029@2/0030@2/0031@1/0033@1, CS0043/0045/0049 | Chooses changed Tōji and wanted intimacy, sees first staging; later helps under deception and is incapacitated. Wakes uncertain. Kairi feeling not resolved; off-panel interval UNKNOWN |
| CHAR0002 @ PG-FR-V05 | CS0034@1/0035@3, CS0041/0042/0044/0048 | Remorseful partner, new boundaries/care and verification evidenced; self-reported past acquiescence after initial refusal; identity victim, searching. No universal invulnerability or informed Sae choice |
| CHAR0003 @ PG-FR-V05 | CS0040/0046 | Prestige fails to end rivalry/desire; escalates into organized deprivation of agency. Exact internal affection weighting and later response unverified |
| CHAR0015 @ PG-FR-V05 | CS0047 | Initially states boundary; later active harmful choices under false belief, knows sleep. Final assertion unverified; no generic clinical/personality diagnosis |
| CHAR0004 @ PG-FR-V05 | CS0038@2 preserved; EV0006 local scene | Ally/continuing suitor with mixed motives unchanged; passing celebrity comparison insufficient for developmental reclassification |

No new subject allocation: incidental sales assistant, hotel staff/bystanders and neighbor retain source-required bounded descriptions in observations; no durable model need established. Readiness remains UNASSESSED; no model proposal, held-out test or new assessment warrants RD0001. Narrative evidence exists. Next new IDs: CHAR0018, CS0050, RD0001.

Revision history: 0.4 — V05 source-derived successor transaction and dated CS0035 anatomy correction, 2026-10-19 owner date; no historical freeze rewritten.

## V06 successor transaction — PG-FR-V06

New [V06 reading](../02%20Sequential%20Readings/PEACH_GIRL_V06_DEEP_READING.md), owner date2026-10-19. EV below expands PG-EV-V06; all events learned V06, source times specified. Latest projection governs retrieval; earlier rows/freezes unchanged. This is new Codex Route B, not recovered Work V06.

| Newly bounded subject | Actual identity / first observation | Limits |
| --- | --- | --- |
| PG-CHAR-0018 | Unidentified actual hotel receiver who threatens restrained Sae; unseen voice EV0045, depicted EV0049/i0162–0163 | Name/biography UNKNOWN; **not merged** with intended actor who calls from another waiting situation at EV0050. Global ID null |

| Event / subject / prior | Time and kind / observed choices, constraints and consequences | Evidence / claim / counteraccount and limits |
| --- | --- | --- |
| PG-CS-0044@2 / CHAR0002 / CS0044@1 | REVEALED_NOT_NEW + analyst correction / V05 gift: refuses joint shopping but Sae places perfume in hand and steers scent/product choice; ordinary care/party/checking remain | V05 i0101–0106/EV0025 plus V06 EV0031; CL0005@6/0019@2. Corrects own overstatement learned V06, not new V06 shopping or edited V05 freeze |
| PG-CS-0050@1 / CHAR0001 / CS0049@1 | CONTEXT_CHANGE / birthday night: challenges Jigoro account, seeks bodily/object certainty, refuses approach, cries and self-blames; no reliable missing-interval memory | EV0002/0006–0008/0012/0021; IP0051@2; lore/fear not proof, choice to help not consent |
| PG-CS-0051@1 / CHAR0002 / CS0048@1 | KNOWLEDGE_CHANGE + action / rechecks hotel, recognizes Sae withholding, survives obstruction, enlists Misao and reaches Momo; repeatedly hits Jigoro until stopped | EV0003–0005/0014–0017; CL0005@6; care/verification plus violence, not ideal savior |
| PG-CS-0052@1 / CHAR0005 / NONE ESTABLISHED | REVEALED_NOT_NEW habit + CONTEXT_CHANGE care / driving fear; uses parent pretext, stops violence/treats injuries, offers Momo choices, later actual family contact; explains secondary hurt | EV0005/0009/0014/0017/0019–0020/0022/0029; no romantic inference, diagnosis or new habit caused by episode. Role now evidenced across contexts |
| PG-CS-0053@1 / CHAR0004 / CS0038@2 | CONTEXT_CHANGE / joins search, watches Momo, initially permits blows, warns against blame, overhears private account and jokes sexually; rivalry persists | EV0005/0009/0017–0018/0022/0030–0031; CL0006@6; assistance does not prove purely selfless motive |
| PG-CS-0054@1 / CHAR0003 / CS0046@1 | DISPOSITION_CHANGE escalation / sprays Tōji, photographs staged room, privately blames Momo and publicly repudiates Jigoro; expects breakup; fan/drug admission and explicit envy | EV0004/0010/0013/0018–0019/0032/0035–0036; CL0002@6/0003@6; fear/public performance not remorse; photo use unknown |
| PG-CS-0055@1 / CHAR0001 / CS0050@1 | KNOWLEDGE_CHANGE false inference + crisis / hears rejection-sounding fragment, misses self-blame explanation, flees into danger and fears impurity-based loss; Tōji reaches and brings her clear | EV0023–0026; CL0020@1; no invented earlier premeditation or actual breakup, no objective impurity finding |
| PG-CS-0056@1 / CHAR0002 / CS0051@1 | RELATIONSHIP_CHANGE / blames own failure, denies her fault, acts to rescue, discloses identity deception and explicitly separates love from compensation guilt; gives reassurance/intimacy | EV0023/0025–0026/0028/0030/0047–0048; CL0005@6/0015@4/0017@3; shared-death pressure, prior violence and later choices retained |
| PG-CS-0057@1 / CHAR0015 / CS0047@1 | KNOWLEDGE_CHANGE / notices mismatch with Sae account, shocked by public blame, demands promised dating, then hears admitted lies/drugging | EV0011/0019/0034–0035; CL0018@3; no backdated knowledge or full missing-interval confession |
| PG-CS-0058@1 / CHAR0001 / CS0055@1 | KNOWLEDGE_CHANGE + action / begins reconstructing with couple/Kairi but retains charity, then overhears Sae admission; shock becomes wall strike and demand for confrontation | EV0031/0033/0035–0036/0038–0039; CL0003@6/0021@1; regained agency, not completed forgiveness or mere helplessness |
| PG-CS-0059@1 / CHAR0002 / CS0056@1 | CONTEXT_CHANGE / participates staged breakup and love confession, tampers with cup, permits incapacitated removal as revenge; performance confirmed | EV0041–0045; CL0005@6/0021@1; prior desire by Sae supplies no permission, care for Momo does not erase active harmful agency |
| PG-CS-0060@1 / CHAR0004 / CS0053@1 | CONTEXT_CHANGE / false studio invitation, proposes matching suffering, directs script and unconscious delivery, assumes actor safety; sexual joke/retraction and serious ambiguity remain | EV0033/0038–0039/0044–0046; CL0006@6/0021@1; motive hypothesis by Tōji not proof; safety assumption fails at EV0050 |
| PG-CS-0061@1 / CHAR0001 / CS0058@1 | CONTEXT_CHANGE + self-report / explicitly hesitates over same-level retaliation then chooses it; staged breakup truly hurts, renewed kisses/deeper closeness, anger plus pity for Sae | EV0044–0048; CL0015@4/0021@1; not passive plan prop, moral cure or endorsed punishment |
| PG-CS-0062@1 / CHAR0003 / CS0054@1 | KNOWLEDGE_CHANGE/context / believes breakup and Tōji confession, privately triumphs; drugged then wakes restrained to unknown threat, screams | EV0041–0043/0049–0050; CL0002@6/0021@1; real desire and loss of agency, not established repentance or completed sexual harm |
| PG-CS-0063@1 / CHAR0015 / CS0057@1 | REVEALED_NOT_NEW self-account / says Sae changed, recalls fragile injured girl he wanted protect | EV0037; CL0018@3; retrospective idealization, not neutral earlier biography or new first meeting |
| PG-CS-0064@1 / CHAR0001/0002/0004 separately affected / CS0061/0059/0060 | KNOWLEDGE_CHANGE / intended contact says girl never came, each visibly shocked; plan control contradicted | EV0050; CL0021@1; no rescue step/outcome yet, no presumption same motive/response for all three |

| Current subject @ PG-FR-V06 | Active material state | Gaps / qualification |
| --- | --- | --- |
| CHAR0001 | CS0050/0055/0058/0061/0064; loves Tōji, understands no-fault position, chooses revenge after pain, then delivery error | Missing interval unresolved; Kairi feeling category remains CL0013@3; no all-context recovery model |
| CHAR0002 | CS0044@2/0051/0056/0059/0064; verification/protective trust and affectionate repair, also repeated blows and deliberate drugging | Bounded change, not uniform improvement; new harm/outcome open |
| CHAR0003 | CS0054/0062; explicit envy and specific desire, now harmed by mirrored incapacitation/danger | No remorse, actual man identity or subsequent outcome established |
| CHAR0004 | CS0053/0060/0064; advocate/ally/rival and revenge director, safety claim fails | Care/desire/punitive motive weights open; no pure altruistic category |
| CHAR0005 | CS0052; institutional care with lies/habits/limits, respects requested solitude | No later drug-admission receipt or full biography shown |
| CHAR0015 | CS0057/0063; story questioned then truth heard, disillusioned | Own hotel act unknown, not absolved by deception |
| CHAR0018 | EV0045/0049; actual threatening receiver distinct from waiting intended contact | Stable bounded identity only; no model or invented name |

Readiness remains UNASSESSED: no operational proposal, assessment or actual predictive model test. Narrative diversity is not automatic reconstruction readiness. Next IDs CHAR0019, CS0065, RD0001. Revision history0.5 — V06 successor transaction and dated CS0044 correction; historical V01–V05 preserved.

## V07 successor transaction — PG-FR-V07

New [V07 reading](../02%20Sequential%20Readings/PEACH_GIRL_V07_DEEP_READING.md); all183 images inspected. EV means PG-EV-V07; CHAR means PG-CHAR. Every event learned V07 at stated range, scene time after V06 revenge night through later Sunday/next school morning; exact calendar UNKNOWN. HIGH action/self-report evidence, motive qualifications separately linked. No new subject identity required. CHAR0018 actual receiver remains distinct from intended contact.

| State / subject / previous | Event kind, actual choice/constraint and time | Evidence / claim / counterreading and scope |
| --- | --- | --- |
| PG-CS-0065@1 / CHAR0001 / CS0061/0064 | DISPOSITION_CHANGE in response / learns error, briefly tries deserved-punishment explanation, rejects cruelty; decides help23–25 knowing pain and contrasting her support with Sae isolation | EV0003/0005–0006; CL0021@2/0022@1. Explicit still cannot forgive, does not erase willing V06 revenge |
| PG-CS-0066@1 / CHAR0003 / CS0062 | CONTEXT_CHANGE / restrained/threatened, strategically flatters then attacks/escapes/caught; suspects Tōji carrier, rescued trembles/cries then condemns trio/slaps Momo | EV0004/0007–0009; IP0062@2. Tactical agency under coercion, not permission/remorse; completed act history not established |
| PG-CS-0067@1 / CHAR0001 / CS0065 | CONTEXT_CHANGE + boundary / personally breaks door, sprays/kicks/strikes threatening man, relieves immediate danger; refuses forgiveness and abandons changing Sae, ends engagement46–48; cries relief | EV0007–0010/0013; CL0022@1, CM0045. Rescuer is Momo, not boys alone; protective violence severity unknown; lasting boundary performance not guaranteed |
| PG-CS-0068@1 / CHAR0004 / CS0060/0064 | CONTEXT_CHANGE + responsibility / initially excuses danger, joins rescue with tool; explains joint-made happiness, admits careless room error/did not intend extent, asks resentment directed to himself not Momo | EV0003/0006–0007/0011–0013; CL0006@7. Accountability/care coexist with prior callousness/complicity; no proved pure motive |
| PG-CS-0069@1 / CHAR0002 / CS0059/0064 | CONTEXT_CHANGE / immediately follows Momo to hotel, aids entry and advances lesson claim, comforts relief, offers birthday redo; later refuses Sae's first dating demand | EV0006–0007/0009/0013/0015/0017–0019; CL0005@7. Help and teaching rationale do not erase own drugging/violence or prove reform |
| PG-CS-0070@1 / CHAR0001 / CS0067 | CONTEXT_CHANGE continuing hurt / model cue freezes body/withdraws; desired ordinary date threatened by image spill, remembers hotel, fears possible rumors and solitude; wants Tōji company/affection | EV0015–0016/0023/0025–0027/0031; CL0017@4. Represented distress, no diagnosis or unseen act confirmation, no total dependency essence |
| PG-CS-0071@1 / CHAR0002 / CS0069 | KNOWLEDGE_CHANGE + protective choice / learns photograph ultimatum, grabs/threatens Sae, explicitly refuses, pursues/phones to stop her, conceals condition from Momo despite her invitation solve together | EV0017–0022/0024/0027–0029; CL0005@7/0023@1. Love/support real, solitary protection chosen not proven only option; no free new Sae preference |
| PG-CS-0072@1 / CHAR0003 / CS0066 | DISPOSITION_CHANGE escalation / after rescue/counsel resolves destroy if cannot obtain, observes Momo cue, threatens exposure with copies/deadline, claims basket present, disparages rescue motive | EV0014/0016–0018/0024/0028; CL0002@7/0003@7/0021@2. Strong no-reform evidence now, not invariant personality diagnosis; actual publication unshown |
| PG-CS-0073@1 / CHAR0001 / CS0070 | CONTEXT_CHANGE / asks Tōji speak/share problem, holds hand/asks final wheel rather than home alone, then receives abrupt breakup without condition knowledge | EV0022/0026/0031/0033/0035–0038; CL0015@5/0023@1. Active needs/alternative articulation, not passive plot object; wanted affection not unlimited permission |
| PG-CS-0074@1 / CHAR0002 / CS0071 | CONTEXT_CHANGE + rupture / secretly calls so Sae hears breakup, tells Momo everything unwanted; attempts retrieve/burn originals, expressly refuses Sae date, learns fake negatives, grabs/releases her | EV0033–0041; CL0005@7/0015@5/0023@1. Coercive cause established by context, false motive harms Momo; actual burning not successful eradication |
| PG-CS-0075@1 / CHAR0003 / CS0072 | KNOWLEDGE_CHANGE + leverage / hears wheel breakup, anticipated reunion and supplies alleged fake originals, retains threat until satisfied; displays new couple publicly and claims preferred girl | EV0034–0035/0041/0044/0051; CL0002@7/0003@7. Public label not sincere reciprocal love; genuine material inventory independent confirmation absent |
| PG-CS-0076@1 / CHAR0001 and CHAR0004 separately / CS0073 and CS0068 | KNOWLEDGE_CHANGE + action / Momo repeatedly calls/waits, denies authentic rupture, seeks truth, accurately infers blackmail169. Kairi first learns/sees public coupling, locates/informs her, catches Tōji and forces encounter, hears allegation | EV0042–0046/0049–0052; CL0020@2/0023@1. Distinct frontiers KN0079–0082, not shared omniscience; no new declared romance |
| PG-CS-0077@1 / CHAR0002 / CS0074 | CONTEXT_CHANGE / hears voicemail, waits then hides, caught by Kairi, answers Momo with self-denigration/denial despite accurate inference, suddenly pulls/kisses Sae as claimed proof of real reason | EV0047–0054; CL0005@7/0023@1. Actual contact/agency, not established sincere preference; Sae explicit prior permission unshown; Momo final shock, next outcome unknown |

| Current subject @ PG-FR-V07 | Active material state | Gaps |
| --- | --- | --- |
| CHAR0001 | CS0065/0067/0070/0073/0076; rescue and firm nonforgiveness, continuing fear/affection, wants shared action, correctly identifies coercion, final kiss hurts | Missing interval unresolved with separately asserted recap; next response unknown; no new Kairi romance category conclusion |
| CHAR0002 | CS0069/0071/0074/0077; help/resistance/affection, concealment and actual breakup under threat, unsuccessful originals recovery, avoidance and staged preference | Protective motive does not cure harm, free Sae love contradicted; future choice/control unknown |
| CHAR0003 | CS0066/0072/0075; tactical defense/distress, no accepted reform, renewed destructive leverage and public couple claim | Actual inventory/publication unknown; no all-context immutable diagnosis |
| CHAR0004 | CS0068/0076; initial dismissal then accountability/help, joint-happiness explanation, later clarification intervention | Not pure selfless model; only hears blackmail allegation at169, exact bargain not independently known |
| CHAR0005 / CHAR0015 / CHAR0018 | Misao no material new scene; Jigoro press account contextualized not new core development; receiver threatened then collapsed after intervention | No filler state change; no medical outcome/death asserted for receiver |

Readiness remains UNASSESSED; no proposed operational model, assessment or held-out model test. No RD row warranted. Next CHAR0019, CS0078, RD0001. Revision history0.6 — V07 successors with original states retained, closure owner date2026-10-20.

## V08 successor transaction — PG-FR-V08

New [V08 reading](../02%20Sequential%20Readings/PEACH_GIRL_V08_DEEP_READING.md),177/177 directly inspected,159 mainline. EV=PG-EV-V08, CHAR=PG-CHAR. All events learned at stated V08 frontier, scene time snow/December and one-week absence, later explicit three months/spring class2-3, later one-week plant interval; exact dates UNKNOWN except visible board/markers. HIGH depicted conduct/attributed speech, qualifications on inferred motives retained.

| Subject / first observed in this transaction | Source identity / certainty | Limit |
| --- | --- | --- |
| PG-CHAR-0019 | Bounded V08 trio of Kairi fans, harass Momo111 and give location lie113; EV0029–0030 | Individual names UNKNOWN, black-bob patterned-jacket member not Sae. Not automatically merged with wavy-haired V01 leader CHAR0006 or all fans historically; no proved Sae coordination |
| PG-CHAR-0020 | Kairi's unnamed older brother, reported74 as authorizing spending after unexpected income; EV0021 | Reported relation/permission only, not independent biography, name, wealth or fraud. Global ID null; actual later identity must be verified |

| State / subject / prior | Event kind, actual choice/constraint and time | Evidence / claim / qualification |
| --- | --- | --- |
| PG-CS-0078@1 / CHAR0001 / CS0076 | CONTEXT_CHANGE persistent belief and injury / sees departure/new couple, still believes photo coercion, defends Tōji, phones/seeks conversation, offers joint action at door24; waits snow/pleads, sick after rejection | EV0002–0009/0014–0015/0018; CL0023@2. Active causal belief/requests with actual hurt; birthdays prints not hotel evidence, no new self-harm plan/diagnosis |
| PG-CS-0079@1 / CHAR0002 / CS0077 | REVEALED_NOT_NEW protective reasoning + CONTEXT_CHANGE / discards note, closes door, returns photos/breaks scent staging; watches pained, tells Misao media ultimatum/fear, cries; phone returned by post | EV0003/0006–0009/0011–0014; CL0005@8/0023@2. Hand-slip his claim, deliberate cruelty strong staging inference; risk model his, not sole possible loving choice |
| PG-CS-0080@1 / CHAR0004 / CS0076 | CONTEXT_CHANGE support/pressure / confronts Sae22, explicitly confronts Tōji35 for Momo illness and punches; Tōji retaliates, Misao treats both, Kairi leaves | EV0006/0010–0011; PR0012@2, CL0006@8. Concrete support, violent method and unshown Sae conversation retained; not peaceful successful clarification |
| PG-CS-0081@1 / CHAR0005 / CS0052 | KNOWLEDGE_CHANGE + advocacy / treats boys, receives Tōji photo/media account41–44, comforts; asks Sae negatives/considers feelings56–60, challenges fake cry; Sae later reports home visit | EV0011–0012/0016–0017; KN0084/0086. Distinct acquisition, not all teacher/class knowledge; no independently shown recovery of originals or official finding |
| PG-CS-0082@1 / CHAR0003 / CS0075 | CONTEXT_CHANGE continued coercion / false preference account10, stalker framing21, denies known threat to Misao then proof demand, scolds Tōji and asserts property62 | EV0002/0005/0016–0017; CL0002@8/0003@8. Direct V07 contradiction makes denial false; distress/history retained, no immutable type assertion |
| PG-CS-0083@1 / CHAR0001 and CHAR0004 separately / CS0078 and CS0080 | CONTEXT_CHANGE care/response / Kairi visits and takes Momo out awkwardly, stops actual kiss offer at her69 refusal, reports brother funds and buys/style; Momo laughs, insists repayment, registers particular warmth80; later accepts ended Tōji relationship/embrace86 | EV0019–0023; CL0006@8/0013@4. Support/cost/boundaries, not perfect care or settled romance. Kairi explicitly full-reason ignorance70 |
| PG-CS-0084@1 / CHAR0003 and CHAR0019 separately / CS0082 and NONE | CONTEXT_CHANGE disruptive acts / Sae squeezed cup100 at Momo joy, later actual trail-sign turn115. Distinct fan trio harasses111 and lies113 to divert Kairi; his118 challenge follows contradictions | EV0026/0029–0032; CL0024@1. Both causes source-supported, coordination UNKNOWN; felt push107 not proven Sae or fans |
| PG-CS-0085@1 / CHAR0001 and CHAR0002 separately / CS0083 and CS0079 | CONTEXT_CHANGE spring / Momo says three months/no talk94, fed up romance96/current friend label98, hurt seeing Sae kiss108 then unusually cheerful110. Tōji starts to help burn103 but Kairi first, unresponsive to Sae-initiated kiss | EV0025–0029; CL0005@8/0015@6/0017@5. Smile not total recovery, movement not complete aid, actual kiss not free new preference |
| PG-CS-0086@1 / CHAR0004 / CS0083 | KNOWLEDGE_CHANGE + support / learns actual friends did not have Momo117–118, searches/finds124, teasing then notices injury, embraces/apologizes fear, actual kiss/affection/carries132 | EV0032/0034–0035; CL0006@8. Rescuer actually Kairi; source does not give him sign-actor/full blackmail knowledge; no formal couple agreement |
| PG-CS-0087@1 / CHAR0001 / CS0085 | CONTEXT_CHANGE response / injured walks using staff, cries under cherry tree/still loves Tōji123, relieved heartbeat with Kairi but asks swept along132; next morning uncertain, compares unlike Tōji/dog lick136; protests unasked committee137 | EV0032–0037; CL0013@4/0017@5. Agency/comfort and strong counterevidence to settled romantic reciprocity together; no retroactive permission from later contact |
| PG-CS-0088@1 / CHAR0001 / CS0087 | CONTEXT_CHANGE reflective attachment / finger cut accidental, notices Tōji eraser141, rests against his desk142; hides when he enters144, cannot speak and remains unseen as he leaves146; fears hurting/losing Kairi147–148 | EV0037–0040; CL0013@4/0015@6. Actual longing not new Tōji reconciliation; self-criticism not universal recovery rule |
| PG-CS-0089@1 / CHAR0001 and CHAR0004 separately / CS0088 and CS0086 | KNOWLEDGE_CHANGE + direct negotiation / after flowerbed repair, Momo says still loves Tōji154/Kairi more important than friend but unsure love155. Kairi hears, accepts remaining close/use156, says support needed157 | EV0040–0043; CL0013@4/0006@8. Honest uncertain position, not full romantic confession or blanket future consent. Permission to rely not proof no cost for him |
| PG-CS-0090@1 / CHAR0001 and CHAR0004 separately / CS0089 | CONTEXT_CHANGE accepted proximity/intensification / one-week flowering tree revealed quince/neighbor gift164; Momo thanks Kairi willing stay even if loves Tōji163, actual laughter, quick surprise kiss/rebuff166, flower-language declaration and closing kiss168 | EV0044–0046; CL0013@4/0017@5. Plant metaphor comic/error-staging not miraculous growth, warmth real; caption not securely Momo spoken confession, no explicit dating pact |

| Subject @ PG-FR-V08 | Current projection | Gap/disposition |
| --- | --- | --- |
| CHAR0001 | CS0078/0083/0085/0087–0090; recognizes enacted breakup yet loves Tōji; actual relief/particular warmth and uncertain more-than-friend value toward Kairi, communicates it, later kisses | No settled reciprocal category; missing hotel act/inventory unresolved; retained refusals/repayment/shared-action requests prevent passivity compression |
| CHAR0002 | CS0079/0085; explicit private protective reasoning to Misao, actual public rejection/avoidance and injury; starts help at burn, unresponsive to Sae kiss | No honest disclosure to Momo/verified negative recovery. Actual preference cause not Sae story |
| CHAR0003 | CS0082/0084; denies actual threat, possessive claim, unhappy Momo joy, demands contact and tampers trail | Coordination with fan trio and burn push unproved, no achieved reform |
| CHAR0004 | CS0080/0083/0086/0089–0090; concrete care, anger/pressure, rescue and affection, accepts declared uncertainty/Toji love | Motive weights open; permission to stay not all-contact consent, brother funding only report |
| CHAR0005 | CS0081; receives private account, treats, challenges Sae and seeks negatives | Official proof/retrieval result absent; no diffuse institutional omniscience |
| CHAR0019 / CHAR0020 | Bounded fans harassment/lie; reported unnamed brother finance | No inferred identity merge or invented brother conduct beyond report |

Readiness UNASSESSED, no operational model or actual held-out reconstruction test, no RD row warranted. No substantive new Jigoro/receiver development; nonappearance not confirmation of unshown outcomes. Next CHAR0021, CS0091, RD0001. Revision0.7 —2026-10-20 V08 successor, historical rows preserved.

## V09 successor transaction — PG-FR-V09

[V09 reading](../02%20Sequential%20Readings/PEACH_GIRL_V09_DEEP_READING.md),175/175 directly inspected,160 mainline; EV=PG-EV-V09, CHAR=PG-CHAR. Learned at stated V09 frontier, current second school year with Momo151 reporting two months dating; no invented date. Past ages/dates/tutor habits remain attributed. HIGH depicted acts/speech, MODERATE inferred motives. No operational model/RD created; readiness UNASSESSED.

| Subject / prior | Identity update and basis | Limit |
| --- | --- | --- |
| PG-CHAR-0021 / NONE | 森香, Morika; kanji128, furiganaもりか153, Kairi former girlfriend by her126/135 and his143–144 accounts; BMW arrival, about21 by his approximate142 report | Distinct Misao CHAR0005, not photo identity merely by necklace. Global ID null; current former relationship supported, exhaustive past acts/age not independently verified |
| PG-CHAR-0020 / same V08 subject | Unnamed Kairi older brother; actual call71 and self-introduction157; Misao tutor/university history62–68, Kairi age25/games-work report74–75, necklace-giving/romantic rivalry reports137/144 | Name/visual identification UNKNOWN at V09 exit. Voice and multiple reports not all-seeing biography or confirmed benevolent character |
| PG-CHAR-0019 / same bounded fan group | V09 fan trio coordinates garden pressure with Sae12–14, then acts without her31–39 | Individual names UNKNOWN; no automatic V01 individual merge, no proof Sae ordered later lighter threat or coordinated V08 trail acts |

| State / subject / prior | Actual event/change and frontier | Evidence / uncertainty / dependencies |
| --- | --- | --- |
| PG-CS-0091@1 / CHAR0001 / CS0090 | CONTEXT_CHANGE publicly recognized couple9, says happened before knew15/forget Tōji for Kairi16, still lured Tōji note but admits to Kairi21; refuses further contact7 | EV0002–0006; CL0013@5/0017@6. New public category not frozen V08 dating pact; mixed feelings not no affection |
| PG-CS-0092@1 / CHAR0005 / CS0081 | CHOICE + REVEALED_NOT_NEW / interrupts pressure14, withholds Tōji account17 under remembered confidence, questions rightness18; warns Kairi19 and privately Tōji ally20 | EV0003–0005; CL0026@1. Actual care, confidence and partisanship coexist, not neutral omniscient counsel |
| PG-CS-0093@1 / CHAR0003 and CHAR0019 separately / CS0084 | CONTEXT_CHANGE / Sae/fans current joint garden lure; later fans alone restrain Momo/lighter singes hair/demand pledge31–37; Momo refuses and Kairi intervenes | EV0003/0009–0010; CL0003@9. Sae no confirmed lighter instruction; new coordination not old historical proof |
| PG-CS-0094@1 / CHAR0004 / CS0090 | REVEALED_NOT_NEW + CHOICE / lip substitution22, water refusal/drowning statement then retraction27–29; actual lighter intervention37–39, pool-gasping after Momo kick41, laughter/embrace44 | EV0006–0011; CL0006@9. Rescue real, drowning intent unresolved, known fear/bodily harm not mere joke |
| PG-CS-0095@1 / CHAR0001 / CS0091 | CHOICE + self-reflection / wants understand Kairi30/43, states liking37, kicks him pool40; secretly crafts case49, cramps/rest/embarrassed laughter/apology55; asks his history | EV0008–0016; CL0013@5. Reciprocal curiosity and own harmful act both retained; physical assertiveness not proof could freely escape later restraint |
| PG-CS-0096@1 / CHAR0005 and CHAR0020 separately / CS0092 and NONE | REVEALED_NOT_NEW attributed history / university friends, recruited tutor of troubled middle-school Kairi, brother praise/affection62–68; actual brother message71, age/work report74–75 | EV0016–0017; CL0025@1/0026@1. Old habits not present diagnoses, favorable portrait partial, no verified mutual dating pact |
| PG-CS-0097@1 / CHAR0004 / CS0094 | CHOICE boundary violation / hears Misao steps75 then restrains Momo despite repeated no76–79, Misao stops80; outside repeat-threat89, prompted apology91 | EV0017–0020; CL0006@9/0017@6. Explicit coercion established, teacher-audience purpose strong hypothesis not confessed; no completed intercourse shown/promise not reform |
| PG-CS-0098@1 / CHAR0001 / CS0095 | KNOWLEDGE_CHANGE + CHOICE / frightened says could not move83, finds worn photo/infers Misao87, falsely denies inspection94, imagines then rejects tutor-intimacy scenario95, watches Kairi watch Misao98–101 | EV0018–0022; CL0020@4. Imagination not actual past event; photo concealment temporary and source-qualified |
| PG-CS-0099@1 / CHAR0004 / CS0097 | KNOWLEDGE_CHANGE + CHOICE / did not relay8pm message, Misao3h wait103, says forgot; public misleading intimacy innuendo104; at116 realizes Momo saw photo/discards actual photo, reassures/kisses117–118 | EV0022–0025; CL0006@9/0025@1. Motive not exhaustively verified, disposal not affection erased, peer innuendo not mutual act proof |
| PG-CS-0100@1 / CHAR0001 / CS0098 | KNOWLEDGE_CHANGE + CHOICE / hears message history108, infers prevented meeting/bed advance to keep Misao112; demands truth114, stops kiss119, asks substitution120–121; new matching-necklace woman prompts changed photo guess127 | EV0024–0027; CL0020@4/0025@1. Strong competing motive, replacement-only allegation not final author account |
| PG-CS-0101@1 / CHAR0021 / NONE | CONTEXT_CHANGE / arrives/ex-girlfriend claim, embraces/drives Kairi away despite school-return objection, cheek kiss133; says dumped3years ago/regrets, necklace from brother implicated; later body/skin rivalry149–152 | EV0027–0029/0033; CL0001@4/0025@1. Attributed mark/burn history not independently shown, unwanted car detour not his free choice of reunion |
| PG-CS-0102@1 / CHAR0004 / CS0099 | CHOICE + REVEALED_NOT_NEW / avoids Morika lean/exitscar138, returns school139, photo question expects Misao141 but explains Morika/brother resentment144, assures only Momo143; publicly tells Morika leave153/leads Momo154 | EV0029–0030/0034; CL0006@9/0020@4/0025@1. Partial actual explanation and actual protective public action; Misao attachment/photo identity not explicitly cleared to Momo |
| PG-CS-0103@1 / CHAR0001 / CS0100 | DISPOSITION_CHANGE + CHOICE / accepts partial assurance, explicitly asks how came to like Kairi so much145/chooses trust146; resists Morika hierarchy, reports2months, finishes/wraps own gift155, calls brother/seeks Kairi158 | EV0031–0035; CL0013@5/0001@4. Romantic feeling now strong, not backdated; no-harm thought not objective history after actual coercion |
| PG-CS-0104@1 / CHAR0001 / CS0103 | KNOWLEDGE_CHANGE + CHOICE / secretly witnesses hotel proposal/assent161–162 and commercial case delight164, throws own gift/runs165–166 | EV0036–0038; CL0020@4. Actual painful knowledge/response not formal breakup, full motive or attended hotel; her labor unknown to him before reveal |
| PG-CS-0105@1 / CHAR0004 and CHAR0021 separately / CS0102 and CS0101 | CHOICE / Morika asks one time tomorrow507, Kairi agrees162, accepts commercial phone case163–164; sees Momo165/calls after her166 | EV0036–0038; CL0006@9/0025@1. Agreement/gift actual, no witnessed hotel/sex/explanation. Subsequent conduct needed; not erase earlier car resistance |

No material new Tōji inner-state evidence after V08: background/looking-away do not support new preference model. No new Sae reform. Next CHAR0022, CS0106, RD0001. Revision0.8 — V09 successors2026-10-20; all older character/state/readiness rows preserved.

## V10 successor transaction — PG-FR-V10

[V10 reading](../02%20Sequential%20Readings/PEACH_GIRL_V10_DEEP_READING.md),179/179 directly inspected,163 mainline. EV=PG-EV-V10; CHAR=PG-CHAR. Learned at stated occurrence frontier, not backdated. HIGH direct conduct/speech, MODERATE motive/pattern, attributed histories not omniscient biography. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED; no RD/model created.

| Subject / prior | Identity update | Limit |
| --- | --- | --- |
| PG-CHAR-0020 / same V09 brother | 岡安涼, Okayasu Ryō/Ryo: Morika callsりょう33, Kairi identifies older brother38, full self-introduction111. Actual driver/party companion/phone impersonator; Morika157 calls recruiter/executive | Hospital visitor22 not explicitly named/merged. Work/age/past accounts attributed; name does not verify good-brother persona |
| PG-CHAR-0022 / NONE | アキ Aki, woman Ryo names119 and claims once loved/died121 | Reported person/mental portrait only; independent existence, death, letter and chronology UNVERIFIED. No invented global identity or character model |

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0106@1 / CHAR0001 / CS0104 | CHOICE/KNOWLEDGE: punches/leaves5–7, tears Kairi photos10, hangs up12–13, private uncommunicated deadline18–20; hotel surname inference25/imagined betrayal27 | EV0002–0007; CL0020@5. Actual anger/violence, no mutual breakup or known freely missed promise |
| PG-CS-0107@1 / CHAR0004 / CS0105 | KNOWLEDGE/CHOICE: opens handmade gift9, thanks/reports return12/wears14; street/hospital injury, protects case by report39–40; directly explains mediator38 | EV0002–0010; CL0006@10. Genuine costly care, incomplete prior explanation not all fake; injury acquisition not Momo early knowledge |
| PG-CS-0108@1 / CHAR0001 / CS0106 | KNOWLEDGE/DISPOSITION: hears mediation38/injury39, chosen embrace42/more important than anyone | EV0009–0010; CL0013@6. New strong current priority, not proof V09 coercion absent |
| PG-CS-0109@1 / CHAR0004 / CS0107 | CHOICE: love-hotel amusement trick45–47, trip proposal57, extensive brochure labor76–83 | EV0012/0015/0019; CL0006@10/0017@7. Care/desire/effort coexist with manipulative setting; no booking/sex or blanket permission |
| PG-CS-0110@1 / CHAR0003 / CS0093 | CONTEXT/CHOICE: magazine graduation/model career frustration, entertainment aim51, feels monitored52/eludes55, breakup idea not act; taunts Momo58–62 | EV0013–0016; CL0002@9/0003@10. Ambition/distress actual, sex boast unsupported, no clinical trauma proof |
| PG-CS-0111@1 / CHAR0002 / CS0085 | CHOICE: follows Sae, states cannot leave her to harmful acts52/dating entitlement; loses chase54 | EV0013–0014; CL0027@1. Direct new behavior, not new romantic-love disclosure or global mind-reading |
| PG-CS-0112@1 / CHAR0020 / NONE | REVEALED_NOT_NEW/CHOICE: offers ride/counsel, competing Morika genealogy70–75/protective secrecy request, credits Momo effect | EV0017–0018; CL0025@2/0027@1. Historical illustrations tied to report, counsel real not global sincerity |
| PG-CS-0113@1 / CHAR0001 / CS0108 | KNOWLEDGE/CHOICE: believes kind Ryo, withholds genealogy79, disputes Kairi warnings; sees brochure labor83, calls apology85 | EV0017–0020; CL0020@5. Own choice under confidence, call recipient not Kairi, no source of confirmed full history |
| PG-CS-0114@1 / CHAR0020 / CS0112 | CHOICE: answers Kairi phone87 without correcting Momo, later false proxy93; party/game offer, adult charm, Aki bereavement narrative | EV0020/0023/0026–0030; CL0027@1. Fraud direct; Aki account not automatically disproved by separate lie |
| PG-CS-0115@1 / CHAR0001 / CS0113 | CHOICE/AFFECT: party accepts97, research let-think103, escort/awe107/117 attraction possibility, Kairi support124, expressly permits compassionate hug126 | EV0023/0026–0031; CL0013@6/0017@7. Attraction and care actual, not completed new love/sex, permission specific |
| PG-CS-0116@1 / CHAR0021 and CHAR0004 separately / CS0101 and CS0109 | CHOICE/CONTEXT: Morika deceptive car ride89–91/job details withheld101; Kairi protests/suspicious, later garden witness129 | EV0022/0025/0031; CL0027@1. Not free romantic outing, no locked trunk/unconsciousness/full common plan |
| PG-CS-0117@1 / CHAR0004 / CS0116 | CHOICE/KNOWLEDGE: dodged swing133/collar-grab/threat134, private unknown whisper135; contact ban139, learns Momo call141/correctly infers fraud, argument/exit145 | EV0033–0035; CL0006@10/0020@5. Concern factually supported, control not vindicated; no explicit breakup or secure punch impact |
| PG-CS-0118@1 / CHAR0003 / CS0110 | AFFECT/CHOICE: actual tears115 after brother link, later spies hug/party and slanders Momo to Ryo148–150; embarrassed leaves151 | EV0028–0031/0036; CL0002@9/0003@10. Real distress does not cancel actual harm, motive mixture unresolved |
| PG-CS-0119@1 / CHAR0001 / CS0115 | CHOICE/REFLECTION: asserts autonomy140, privately only Kairi146, decides disclose146–147, hears Ryo defense151, gains permission153, declines week/accepts questionnaire154 | EV0034–0037; CL0013@6/0027@1. Agency actual, no Kairi receipt of history; task assent limited |
| PG-CS-0120@1 / CHAR0020 / CS0114 | CHOICE: defense/advocacy reassures Momo, changes game form to financial/business questions159; drapes refused gift165, unwanted kiss/touch166–167, pulls/pins her after leave168–169 | EV0036–0042; CL0017@7/0027@1. Actual sexual assault/blocked exit, no completed intercourse by cutoff; prior good counsel not erased or excuse |
| PG-CS-0121@1 / CHAR0004 / CS0117 | KNOWLEDGE/CHOICE: learns Ryo executive/recruiter157, immediately runs158, still corridor170 | EV0038–0039/0043; CL0006@10. No actual room entry/rescue/safety verified |
| PG-CS-0122@1 / CHAR0001 / CS0119 | KNOWLEDGE/CHOICE: completes form164, recognizes repeated gifts/refuses necklace165, alarm/recalls warning166, pushes away167/declares leaving168, held against will169/distressed170 | EV0039–0043; CL0017@7/0020@5. New confirmed danger not her earlier knowledge; refusal and escape initiative actual, final outcome unresolved |

Misao absent as present actor; remembered praise/necklace reports do not establish a new preference. Aki no independent inner access. No fan-trio/earlier model promotion. Next CHAR0023, CS0123, RD0001. Revision0.9 — V10 successors2026-10-20; prior rows and full prior body preserved.

## V11 successor transaction — PG-FR-V11

[V11 reading](../02%20Sequential%20Readings/PEACH_GIRL_V11_DEEP_READING.md);175 inspected/159 mainline. EV=PG-EV-V11, CHAR=PG-CHAR. Direct acts/speech HIGH, attributed history and motive limited as stated. No new securely named subject, RD or operational model. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED.

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0123@1 / CHAR0001 / CS0122 | CHOICE/CONTEXT: repeated no, failed first escape7–10, forced kiss16, writing-implement self-defense18/self-escape20, fear killed brother22 | EV0002–0004; CL0017@8. Her agency material, harm real; no knife subtype/death fact or Kairi-interrupted rescue |
| PG-CS-0124@1 / CHAR0020 / CS0120 | CHOICE: continued forced contact/locked exit, injured18–19, alive24; falsely reverses roles to Sae25, accepts help/hospital43 | EV0002–0005/0010; CL0027@2. Minor wound not death, counterstory contradicted by depiction; not Momo/Kairi receipt |
| PG-CS-0125@1 / CHAR0004 / CS0121 | CHOICE/KNOWLEDGE: meets Momo AFTER escape21, supports her chosen return26/empty room27, no-fault attacker-blame32, reports prior whisper35; kiss then hotel pitch42 | EV0004/0006–0009; CL0006@11/0017@8. Actual comfort not original rescue success; renewed pitch not no-fault care erased |
| PG-CS-0126@1 / CHAR0001 / CS0123 | KNOWLEDGE/REFLECTION: repeated-assault self-blame32 countered; learns whisper35, finally relays Morika genealogy36, recognizes kinship/future-Kairi trust38; love relief41 | EV0006–0009; CL0013@7/0020@6/0025@3. Kairi competing account not all past verified; no permanent cure |
| PG-CS-0127@1 / CHAR0003 / CS0118 | KNOWLEDGE/CHOICE: receives false reversed-assault account25/believes/helps hospital, accepts cross44, long-night/both-boyfriends claim55–58, canceled-date report99/threat100 | EV0005/0010/0013/0023; CL0002@10/0027@2. Aid actual, prior sex only attributed, Tōji agreement/breakup unshown |
| PG-CS-0128@1 / CHAR0001 / CS0126 | CHOICE/REFLECTION: not ready visit51 refusal heeded, only Kairi58 yet concern Tōji59–62 prompts accompany; self-analogy to Tōji67 | EV0012–0015; CL0013@7. Not romantic re-choice or duty forgive ex; self-critique not objective equivalence |
| PG-CS-0129@1 / CHAR0020 / CS0124 | CHOICE/STATEMENT: call-as-test excuse47, minimizing apology72/claimed Sae sex73, scenarios boast74, cruelty-as-affection75, true-beloved rule77/80, feigned pain/disarms82/card83 | EV0012/0016–0019; CL0027@2/0028@1. Fabrication strongly acknowledged, not every Aki detail independently false; no mental diagnosis |
| PG-CS-0130@1 / CHAR0001 / CS0128 | CHOICE/KNOWLEDGE: spray raised/distance70–71, demands stop Sae73, calls Kairi79; hears not true beloved80/unspecified he-still81, crumples card89/generic love question91 | EV0016–0021; CL0020@6/0028@1. Spray floor beside toilet82, recovered84; precise Ryo claim not relayed to Kairi |
| PG-CS-0131@1 / CHAR0005 / CS0096 | CHOICE/CONTEXT: Misao tea/care93–94, necklace tutoring farewell97, defends Ryo96 without receiving Momo assault; shock Sae/Ryo102, warns Tōji no overdo105 | EV0022–0023; CL0026@2. Warm care/partisan loyalty, not full informed assault denial or mutual romance proof |
| PG-CS-0132@1 / CHAR0002 / CS0111 | KNOWLEDGE/CHOICE: enters100/asks who Ryo101, Sae evades, says not break up for this104/okay105 | EV0023; CL0015@6 unchanged. Name learned, not full sex/assault receipt or happy reciprocal love |
| PG-CS-0133@1 / CHAR0004 / CS0125 | CHOICE/REFLECTION: love assurance91, seminar suspicion107, house invitation110, own brother-competition insecurity116/truly wanted unavailable117 | EV0021/0024–0026; CL0006@11. No identity specified117 or actual affair; invitation not sexual contract |
| PG-CS-0134@1 / CHAR0001 / CS0130 | CHOICE/AFFECT: accepts house refuge, current specific willingness119/revises setting120/direct love121, chosen intimacy123 | EV0025–0027; CL0013@7/0017@8. No completed intercourse, no blanket permanent permission/clinical cure |
| PG-CS-0135@1 / CHAR0004 / CS0133 | CHOICE: halts124/gets up125/cannot126/not her fault128; later repeated avoidance133–135/denial137/errand excuses138/144 | EV0028–0031; CL0006@11/0028@1. Own right to stop valid; avoidance real, stopping cause not medically diagnosed |
| PG-CS-0136@1 / CHAR0001 / CS0134 | AFFECT/CHOICE: hurt/pillow130, hopeful alternative from torn card131, confronts avoidance136, swimming/club advice143, flowering-quince lonely love146, seeks Misao consult148 | EV0029–0032; CL0013@7/0028@1. Figurative embarrassment not death plan, unnamed seniors not Tōji/Sae, advice not clinical fact |
| PG-CS-0137@1 / CHAR0005 / CS0131 | CHOICE/STATEMENT: invites Momo home148/tea149/album permission150, summer-trip/tutor-name account153, recurring Kairi visitor/family-like explanation155–158 | EV0032–0034; CL0026@2. Actual support/visits, no mutual romantic or sexual relationship established; outside confession not received |
| PG-CS-0138@1 / CHAR0001 / CS0136 | KNOWLEDGE/CHOICE: album154 identifies handbook woman Misao, sees Kairi156, asks outside159–163; receives frequent-visit nod159 and still-love-Misao yes164/apology165 | EV0033–0036; CL0025@3/0028@1. New actual knowledge now; no explicit breakup or all history/precise stop cause solved |
| PG-CS-0139@1 / CHAR0004 / CS0135 | REVEALED_NOT_NEW/CHOICE: arrives Misao home156, silence then outside nod frequent visits159, affirms still loves Misao164/apologizes165 | EV0034–0036; CL0006@11/0025@3/0028@1. Present attachment admitted, onset not newly created164, no exclusivity/full conscious fraud or Misao reciprocity proved |

CHAR0005 Misao identity verified against existing cast before closure. No new actor ID for unnamed club pair. Aki remains reported/unverified, no death/existence adjudication by absence; Morika only phone report, no new stable inner-state row. Next CHAR0023, CS0140, RD0001. Revision0.10 — V11 successors2026-10-20, prior full body/rows retained.

## V12 successor transaction — PG-FR-V12

[V12 reading](../02%20Sequential%20Readings/PEACH_GIRL_V12_DEEP_READING.md);177 inspected/162 mainline. EV=PG-EV-V12; CHAR=PG-CHAR. Direct acts/speech HIGH; nested recollection and motive limited below. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED, no new RD.

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0140@1 / CHAR0001 / CS0138 | AFFECT/CHOICE: album blow8/fists9/pulls away11, tears travel brochures14, all-care-false hurt judgment15, declines Misao counsel19/jealous self-reproach20–21, classroom/phone avoidance22–24 | EV0002–0004; CL0013@8/0017@9. Physical anger retained, objects distinct, judgment not omniscient fraud finding |
| PG-CS-0141@1 / CHAR0005 / CS0137 | CHOICE/KNOWLEDGE: returns forgotten bag16, reports Kairi would not explain17, family/tutor reassurance18/offer counsel19 | EV0003; CL0026@3. Not shown receiving outside confession, actual Momo assault or bedroom story |
| PG-CS-0142@1 / CHAR0002 / CS0132 | CHOICE/STATEMENT: watches hurt, returns cap29, seeks Ryo contact30; reports Sae breakup request31/refuses, cannot forgive but own-wish counsel32–33 | EV0004–0005; CL0015@7. Actual continued choice, no mutual Tōji/Sae breakup or Momo reunion |
| PG-CS-0143@1 / CHAR0004 / CS0139 | CHOICE/CONTEXT: apologizes/messages25, pursues pool35 despite asked leave36, enters water38/actual distress/sinks40–41 | EV0004/0006. Danger real, no established harmless trick or intent diagnosis; original conduct explanation still absent |
| PG-CS-0144@1 / CHAR0001 / CS0140 | CHOICE: swim to avoid thought26, avoids explanation35–37 then retrieves/supports Kairi42/holds head44 and listens | EV0004/0006–0007; CL0013@8/0007@2. No CPR, settled death plan or stated wish let him die |
| PG-CS-0145@1 / CHAR0004 / CS0143 | REVEALED_NOT_NEW: direct insecurity47/competing attachment48–49, narrated recognition/tutor/camp49–68, ambivalent offshore death/guilt thoughts71, nested rescuer/search reports74–77, continuing Misao devotion78 | EV0009–0016; CL0006@12/0025@4/0028@2. Reported past not all independently verified; later disclosure not V09 foreknowledge/clinical diagnosis or precise V11 stopping link |
| PG-CS-0146@1 / CHAR0005 / CS0141 | REVEALED_NOT_NEW via Kairi account: full name 安芸操52, individual recognition56, photo61, practical tutoring departure67, reported storm search75–77 and relief hug74 | EV0010–0016; CL0026@3. Actual source account, not new current events/romantic reciprocity. Aki surname not merged with CHAR0022 |
| PG-CS-0147@1 / CHAR0001 / CS0144 | KNOWLEDGE/CHOICE: receives Kairi history, asks kiss79–80/receives81, gets explicit Misao-more yes83; compares own past Tōji feelings92, informed continuation offer96–97 | EV0009–0020; CL0013@8/0020@7. Empathy and chosen offer actual, not current Tōji love or Kairi agreement |
| PG-CS-0148@1 / CHAR0004 / CS0145 | CHOICE: requested kiss81/ranks Misao more83, admits fear confessing89, declines continuation99–103/leaves105–106 | EV0017/0019–0021; CL0006@12/0028@2. Actual breakup, hypothetical sex not consummation/all previous care false; own refusal valid |
| PG-CS-0149@1 / CHAR0002 / CS0142 | KNOWLEDGE/CHOICE: finds crying Momo108/returns wallet110; breakup disclosure later confirmed124, actual punch Kairi117/yielded claim119 | EV0022–0024; CL0015@7. Momo absent punch, possession claim not legitimate ownership or all inner motives |
| PG-CS-0150@1 / CHAR0001 / CS0147 | CHOICE/AFFECT: hurt by enacted ending107, confides breakup off-panel124; old Tōji memories131 but pushes him away134/only Kairi136, grateful maybe-helper interpretation138 | EV0021–0027; CL0013@8/0015@7. No completed Tōji kiss or renewed dating, her helper theory not his admission |
| PG-CS-0151@1 / CHAR0002 / CS0149 | CHOICE: unrequested hug125/waiting-limit126/date-again127, approaches kiss130 but refused134; knows Misao135, advises honest Kairi disclosure136/smiles137 | EV0025–0027; CL0015@7/0017@9. Care/romantic stake coexist, no proof whole proposal a feint |
| PG-CS-0152@1 / CHAR0001 / CS0150 | CHOICE: accepts breakup144, thanks145, renews pursuit146–148 after distinguishing ended relation; collar grab150/accusation151–152/kiss154 after Kairi no149, sexual challenge156, later responds158/resolve first159 | EV0028–0031; CL0013@8/0017@9. Active agency and pressure both recorded, intense dependence language not enacted death plan; later response not retroactive consent |
| PG-CS-0153@1 / CHAR0004 / CS0148 | CHOICE: accepts ending144, declines new request149, lowers face154, glad-but-cannot-stop155, laughs/initiates embrace157/second-for-now158/later kiss158–159 | EV0028–0031; CL0006@12/0017@9/0028@2. Later responsive reconnection actual, no exclusive preference, all prior refusal erased or completed sex |
| PG-CS-0154@1 / CHAR0003 / CS0127 | CONTEXT/CHOICE: Tōji reports her breakup request31; magazine163 presents her as 安西かりん, reported absences/rumors164; actual phone165 and unnamed adult companion/waist embrace167–168 | EV0005/0033–0034; CL0002@11. Publication actual in fiction, authenticity/production consent/sexual acts/contract unknown; no secure companion identity or Ryo phone receipt |
| PG-CS-0155@1 / CHAR0001 / CS0152 | KNOWLEDGE/CHOICE: asks peers how turn Kairi160–161, sees Sae magazine163/questions composite, hears bounded rumor164, sees adult companion168 | EV0032–0034; CL0020@7/0002@11. No complete Sae motive/production or Tōji receipt; own first-place project unachieved |
| PG-CS-0156@1 / CHAR0020 / CS0129 | REVEALED_NOT_NEW through Kairi account: intrusive contact Misao64/minimizes, rescuer attribution74/later search report75; current rarely-home report166 | EV0012/0015–0016/0034; CL0025@4/0026@3. Past reports not new present assault; naming Aki surname65 not proof dead-woman identity/history |

Misao remains CHAR0005, now full name 安芸操 Aki Misao52. CHAR0022 reported アキ remains unmerged/unverified. Anonymous peers/photographer/phone recipient/adult companion are not given invented named identities; adult is not Ryo and not securely Honda CHAR0014. Next CHAR0023, CS0157, RD0001. Revision0.11 — V12 successors2026-10-20; complete prior body/rows retained.

## V13 successor transaction — PG-FR-V13

[V13 reading](../02%20Sequential%20Readings/PEACH_GIRL_V13_DEEP_READING.md);171 inspected/157 mainline. EV=PG-EV-V13; CHAR=PG-CHAR. Acts/speech HIGH, self-serving explanations and inner motive qualified. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED; no new RD.

| Local subject | Verified identity/admission | Limit |
| --- | --- | --- |
| PG-CHAR-0023 | ポッキー鈴木 / Pocky Suzuki; Kairi recognizes/names adult-video actor80, visible filming costar77–82 and hotel actor | EV0012/0015/0018; actual recognition claim, not independent credits audit. Not Jigoro CHAR0015/Honda CHAR0014/opening adult. Global ID null |

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0157@1 / CHAR0003 / CS0154 | CHOICE/CONTEXT: adult hotel/denies Momo6, pushes11/dismisses12, whitening pitch16–18; school denial24/accepts teacher composite25; pays Ryo cash34–35 | EV0002–0006; CL0002@12/0003@11. No verified image forgery/sex/efficacy or exact cash total |
| PG-CS-0158@1 / CHAR0001 / CS0155 | CHOICE: challenges adult/Sae, rejects sales pitch, seeks Tōji/Ryo, takes envelope35/swings at Ryo39 but hits interposed Sae | EV0002–0007; CL0013@9. Protective purpose does not erase actual physical blow/misjudgment |
| PG-CS-0159@1 / CHAR0003 / CS0157 | CHOICE/STATEMENT: protects Ryo39/love44/own choice45, current Tōji ending/sorry46; claims modeling/game job74, dismisses actual warning86–88 | EV0006–0007/0011–0014; CL0002@12. Stated volition not all-informed sexual consent or safe reciprocity |
| PG-CS-0160@1 / CHAR0002 / CS0151 | KNOWLEDGE/CHOICE: sees ending/conflict47; reports missed exams/makeups58/internet business60–62; actually joins rescue/punch114/carries Sae116 | EV0005/0007/0009/0019; CL0015@8. No Momo reunion, own romantic stake erased or full Sae details from summons alone |
| PG-CS-0161@1 / CHAR0004 / CS0153 | CHOICE/STATEMENT: appearance affirmation20/affection50, asks home after refusal, sea trip52/wait for aligned feelings54, summer Misao wish64, joint job68–70 | EV0003/0008/0010; CL0006@13/0028@3. Current restraint/liking actual, not exclusivity or old stopping-cause disclosure |
| PG-CS-0162@1 / CHAR0001 / CS0158 | CHOICE/REFLECTION: no50, fears casual claim51/accepts trip53/relieved55, jealousy/second-place lie67, works69–70; refuses abandon endangered Sae91 | EV0008/0010/0014; CL0013@9/0017@10. Mixed desire/limits and ordinary effort, not passive ignorance or permanent consent |
| PG-CS-0163@1 / CHAR0020 / CS0156 | CHOICE/STATEMENT: accepts/counts Sae cash35/knows earnings37; offers high pay71, answers Sae99/excuse100/conditional abandonment101 | EV0006/0011/0016; CL0027@3. Actual knowledge and conduct stronger than earlier speculation; no independently verified contract validity/payment or Misao call receipt |
| PG-CS-0164@1 / CHAR0003 / CS0159 | CHOICE/HARM: protests filming93/leaving94, resists96–97/hides; receives abandonment101, calls Momo104/acknowledges right105/location106; forced restraint/filming111–112 | EV0015–0018; CL0002@12/0017@10. Own escape/help-seeking real; actual assault before rescue, no completed intercourse established |
| PG-CS-0165@1 / CHAR0001 / CS0162 | CHOICE: warns86–88, seeks location106/summons Tōji107, enters rescue114/covers Sae115/secrecy118/first aid120, accepts thanks122 | EV0014/0017/0019–0020; CL0013@9. Moral agency without duty to forgive, rescue not erasure or no harm |
| PG-CS-0166@1 / CHAR0004 / CS0161 | KNOWLEDGE/CHOICE: recognizes Pocky80, initially leave-Sae stance91 then calls Ryo92/friends107/joins rescue114; took Morika DVD135 | EV0012/0014/0017/0019/0023; CL0006@13. Genuine assistance plus early punitive judgment; DVD not all Sae footage secured |
| PG-CS-0167@1 / CHAR0003 / CS0164 | AFFECT/CHOICE: trembles119/thanks cries122, directly questions Ryo127–128, knows yet chases132/embraced133; specific Momo apology/gift139–140 | EV0020/0022–0024; CL0002@12/0003@11. Not all gratitude acting or complete lasting reform, return not safe reciprocity |
| PG-CS-0168@1 / CHAR0020 / CS0163 | CHOICE/STATEMENT: boasts police link126; sorry/MLM-like/AV shock-treatment rationale129/leaves130, accepts Sae arm/walks133 | EV0022–0023; CL0027@3. Claim of concern not established justification, conflicting excuse retained; no actual police report/corruption verification |
| PG-CS-0169@1 / CHAR0005 / CS0146 | CHOICE/CONTEXT: sees Momo/Sae leaving143, concern/Ryo pairing not good, collapses144/caught by Kairi; diet/slenderness discussion154–155/rests/sleeps156 | EV0025/0027–0028; CL0026@4. Diet attribution not clinical diagnosis, no full love confession or consent from sleep |
| PG-CS-0170@1 / CHAR0003 / CS0167 | CHOICE/REVEALED_REPAIR: admits suspects fooled/first true love/hope change Ryo145; understands earlier Momo hurt/apologizes146; arranges Jigoro meeting147–150/studio visit reported150–151 | EV0025–0026; CL0002@12/0003@11. Concrete reparative act, not permanent reform/verified ability change him |
| PG-CS-0171@1 / CHAR0015 / CS0063 | REVEALED_NOT_NEW/REPAIR: apologizes150–152, says no sexual act with Momo on old day152/should have said earlier | EV0026; CL0018@4. Strong participant account accepted Momo, not omniscient replay or absolution for drugged removal/control |
| PG-CS-0172@1 / CHAR0001 / CS0165 | KNOWLEDGE/AFFECT: first fears trap149, receives Jigoro account152/Sae confirmation153, relief154/156; admits hidden lasting wound and old virginity explanation hypothesis157 | EV0026–0027; CL0013@9/0018@4. Later evidence revises suspicion, sexual history not analyst worth metric or verified Kairi motive |
| PG-CS-0173@1 / CHAR0004 / CS0166 | CHOICE: catches Misao144, reassuring care/diet counsel155, pokes sleeping cheek158/watches/touches brow159/leans close160/startles161–162 | EV0025/0027–0028; CL0006@13/0026@4/0028@3. Intimate approach exceeds neutral-care-only reading; completed lip contact/consent/explanation unresolved |
| PG-CS-0174@1 / CHAR0001 / CS0172 | KNOWLEDGE/AFFECT: returns joyful157, opens door161/sees Kairi over sleeping Misao, shocked162 | EV0027–0028; CL0013@9/0020@8. Sees configuration, not automatically prior diet/cheek sequence, no next response yet |

Pre-canonical identity check: Ryo-call woman99–100 remains UNNAMED; no Misao state/receipt inferred there. Jigoro CHAR0015 and Pocky CHAR0023 distinct. Next CHAR0024, CS0175, RD0001. Revision0.12 — V13 successors2026-10-20; all prior rows/body retained.

## V14 successor transaction — PG-FR-V14

[V14 reading](../02%20Sequential%20Readings/PEACH_GIRL_V14_DEEP_READING.md);175 inspected/159 mainline. EV=PG-EV-V14; CHAR=PG-CHAR. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED; no new RD.

| Local subject | Verified identity/admission | Limit |
| --- | --- | --- |
| PG-CHAR-0024 | Unnamed soba-shop owner; actual105/108–113/145–153, married to CHAR0025 | Name unknown. Wife113 maps husband onto Kairi's ROLE, not literal Okayasu identity. Aggression/help/counsel all retained; global ID null |
| PG-CHAR-0025 | 早苗 / Sanae, shopkeeper's wife, addressed153; actual108–113/132/151–153 |113 maps herself onto Momo's ROLE, not her actual name. Attributed comparable youth not independently replayed; global ID null |

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0175@1 / CHAR0001 / CS0174 | CHOICE/AFFECT: leaves doorway6, silent work11, names sleeping approach13, second-place no-right thought14/private should-end15 | EV0002–0003; CL0013@10/0017@11. Self-suppression not analyst duty or communicated breakup |
| PG-CS-0176@1 / CHAR0004 / CS0173 | CHOICE/KNOWLEDGE: encounter response13, hurting M28/stuck agrees30; receives actual Jigoro outcome33–35/relieved hug/anger undressing37 | EV0002/0004–0005; CL0006@14/0028@4. No secure completed kiss, no-act not no harm |
| PG-CS-0177@1 / CHAR0003 / CS0170 | CHOICE: intercepts call as SELF18–19, unequal relation known20/identity withheld21, counsels M23–25/confronts K28–30 | EV0003–0004; CL0002@13/0003@12. Heard-all boast not complete knowledge, useful insight not permanent reform |
| PG-CS-0178@1 / CHAR0001 / CS0175 | CHOICE/AFFECT: actual intoxicated why-not-love41/how-long42, sleeps43; later asks weird words48/receives denial | EV0006/0008; CL0013@10. Speech actually heard K, intoxication not consent/clinical diagnosis |
| PG-CS-0179@1 / CHAR0004 / CS0176 | CHOICE: carries46/omits actual M questions48, reflects49–51, visits Misao/confesses57/59/receives rejection62/thanks63 | EV0008–0009; CL0006@14/0026@5. Care plus omission, rejection not instant feeling erased |
| PG-CS-0180@1 / CHAR0005 / CS0169 | CHOICE/STATEMENT: domestic visit52–56/initial joke58/never imagined60/only younger brother/future too62 | EV0009; CL0026@5. Actual romantic rejection, no sleep-consent inference or blanket lack of care |
| PG-CS-0181@1 / CHAR0004 / CS0179 | CHOICE/STATEMENT: actually tells M rejection65/cannot immediate redirect67/distance68/wait69; quits74/receives exact noon/five-minute terms76/walks | EV0010–0011; CL0006@14/0028@4. Current qualified attachment, not settled first-choice pledge |
| PG-CS-0182@1 / CHAR0001 / CS0178 | KNOWLEDGE/CHOICE: receives result65, private wait70, books trip/actual terms76, K only79/no-contact81–82 | EV0010–0012; CL0013@10. Boundary communicated, future attendance not yet; no unlimited waiting commitment |
| PG-CS-0183@1 / CHAR0003 / CS0177 | CHOICE: reports rejection71, arranges T job88/false self-quitting, manager reconciliation story140; answers M90 | EV0011–0012/0023; CL0002@13/0003@12. New meddling real, not retrospective proof V13 repair fake |
| PG-CS-0184@1 / CHAR0002 / CS0160 | CONTEXT/KNOWLEDGE: takes S job lead/unaware M87, accepts work, receives partial K-distance/ticket account98–99/phone counsel107 | EV0012–0013/0015; CL0015@9. Full deadline terms not recited to him; brief brush not established strategy |
| PG-CS-0185@1 / CHAR0004 / CS0181 | CONTEXT/CHOICE: hot walking95/wallet loss100/skater inference101, Ryo call interrupted102/runs unpaid104/hit sandal105/dishwork108–109 | EV0013–0016; CL0006@14. Theft unshown/no actual Ryo help; flight and owner aggression both actual |
| PG-CS-0186@1 / CHAR0020 / CS0168 | STATEMENT/CONTEXT: phones K102/parents worry/note in hand; call dies before full trouble-location account | EV0014; CL0025@6. Bounded concern, not reform or actual financial aid |
| PG-CS-0187@1 / CHAR0024 / NONE | CHOICE: sandal throw105, meal/work109/lodging context113; puzzle quarrel139, award priming/expired soba146–149/idealization counsel150–151/notices fever153 | EV0014/0016/0022/0024–0025. Useful counsel not infallibility, no explicit this-dish-won lie |
| PG-CS-0188@1 / CHAR0025 / NONE | CHOICE/STATEMENT: empathy108/similar past112/role analogy/lodging113, towels132, puzzle completion account139/couples sharing151 | EV0016/0021–0022/0025. Sanae153; care can misattune, not literal Momo identity/independent full past history |
| PG-CS-0189@1 / CHAR0003 / CS0183 | CHOICE/REPAIR: photo to T116/real-negative/bluff admission117–118/apology119; confirms media threat to M128–129/leaves when asked130 | EV0017–0020; CL0003@12/0023@3. Concrete delayed truth after new meddling, not all copies destroyed/full reform |
| PG-CS-0190@1 / CHAR0001 / CS0182 | KNOWLEDGE/AFFECT: overhears118–124/demands exact128/gets129/asks S leave, new sympathy/self-blame130–143/scandal counterfactual144 | EV0017–0020/0023; CL0013@10/0023@3. Old correct suspicion not full prior receipt; self-blame countered by T156 |
| PG-CS-0191@1 / CHAR0005 / CS0180 | CHOICE/STATEMENT: phones K134/never actually told Ryo136/chocolate withheld on discovering beloved; K confession restored confidence/try Ryo137 | EV0021; CL0026@5. Not revocation of sibling-only rejection; woman136 not securely dead Aki |
| PG-CS-0192@1 / CHAR0004 / CS0185 | KNOWLEDGE/CONTEXT: hears Misao136–137/weak139, soba counsel149–151/M memory152/unfinished I153, actual influenza diagnosis158/helpless water/help162–163 | EV0021–0022/0024–0025/0027/0029; CL0006@14. Risk not pneumonia/death; contact screen not completed call or spoken first-choice pledge |
| PG-CS-0193@1 / CHAR0002 / CS0184 | KNOWLEDGE/CHOICE: learns M overheard155/actual own-fault apology156, returns phone154/fireworks invite158/watch159/conditional restart166 | EV0026–0030; CL0005@9/0015@9/0023@3. Protective intention plus harmful method, no M acceptance/current reunion |
| PG-CS-0194@1 / CHAR0001 / CS0190 | CHOICE/AFFECT: thanks T155–157/watch159/past-memory/current-feelings question160, would probably give up if K absent165/receives conditional proposal166 | EV0026–0030; CL0013@10. No answer before exit; no shown K-illness knowledge, completed call, deadline failure or current T choice |

Pre-canonical Japanese recheck113 corrected private literal-name misparse: wife uses role analogy, actual Sanae153 consistent. No canonical identity-lie claim admitted. Next CHAR0026, CS0195, RD0001. Revision0.13 — V14 successors2026-10-20; prior bodies/rows preserved.

## V15 successor transaction — PG-FR-V15

[V15 reading](../02%20Sequential%20Readings/PEACH_GIRL_V15_DEEP_READING.md);175 inspected/161 mainline. EV=PG-EV-V15; CHAR=PG-CHAR. Readiness UNASSESSED_NO_OPERATIONAL_MODEL_TESTED; no new RD.

| Local subject | Verified identity/admission | Limit |
| --- | --- | --- |
| PG-CHAR-0026 | Unnamed aggrieved man at florist61–66, alleges Ryo-related bankruptcy, swings sword, escorted by police | Weapon imitation74/109; financial allegation not adjudicated truth, no global identity |
| PG-CHAR-0027 | Unnamed persistent beach young man99–102, refuses to leave/grabs M wrist, departs after T intervention | Not Jigoro/Ryo; no consensual date or actual T strike; no global identity |

| State / subject / prior | Actual transition/frontier | Basis / limit |
| --- | --- | --- |
| PG-CS-0195@1 / CHAR0001 / CS0194 | KNOWLEDGE/CHOICE: missed K call7/callback, privately admits pretended nonhearing13, shared T history/current attraction22, K outage/waiting distress23 | EV0001–0002; CL0013@11/0020@10. No illness receipt or answer accepting T yet |
| PG-CS-0196@1 / CHAR0004 / CS0192 | CONTEXT/AFFECT: hospital9/developing pneumonia, charger24, death fear/current companion insight25/puzzle counsel27 | EV0001/0003; CL0006@15/0028@5. New diagnosis progression not V14 rewrite; private resolve not M receipt |
| PG-CS-0197@1 / CHAR0024 / CS0187 | CHOICE: carries ill K8/hospital support/charger24/puzzle27, wages/parting generosity45/receives blank puzzle46–48 | EV0001/0003/0007; CL0006@15. Prior sandal aggression retained, useful counsel not universal law |
| PG-CS-0198@1 / CHAR0025 / CS0188 | CHOICE: assists emergency8, hospital context9, departure/wages44–47/joint puzzle acceptance47 | EV0001/0007. Sanae known; no new husband name/past-history audit |
| PG-CS-0199@1 / CHAR0001 / CS0195 | CHOICE/AFFECT: tries avoid T shifts28/retracts30, receives generic K email33–34/relief35/private K love37, full deadline to T39 | EV0004–0006; CL0013@11. No above-Misao pledge or hospital knowledge |
| PG-CS-0200@1 / CHAR0002 / CS0193 | CHOICE/KNOWLEDGE: volunteers shift29, sees M relief, learns full deadline39/support40, still next-day work42 | EV0004–0006; CL0015@10. Not K attendance guarantee or M relationship acceptance |
| PG-CS-0201@1 / CHAR0004 / CS0196 | CHOICE/STATEMENT: thanks couple/gift46/plans M masterpiece48/early station50, directly tells Mis M first53–54/buys rose58 | EV0007–0008; CL0006@15/0028@5. Actual resolve/counsel heard Mis, not M |
| PG-CS-0202@1 / CHAR0005 / CS0191 | KNOWLEDGE/CHOICE: hears M-first53–54/praises K55/plans R confession56/flowers57 | EV0008; CL0026@6. No reciprocal K romance or actual completed R confession/answer |
| PG-CS-0203@1 / CHAR0020 / CS0186 | STATEMENT/CONTEXT: actual hospital-help account59/repayment demand60, accused61–62/business-risk defense, attacked/R contusions74/questioning75 | EV0009–0012; CL0025@7. Bounded care not full reform; business self-defense not forensic verdict |
| PG-CS-0204@1 / CHAR0026 / NONE | CHOICE/STATEMENT: bankruptcy/guaranteed-profit allegation61–62, sword swing63/Mis interposes64/police escort66 | EV0010–0011; weapon imitation later74, grievance not permission for violence/complete financial proof |
| PG-CS-0205@1 / CHAR0005 / CS0202 | CHOICE/AFFECT: interposes64/shaken/taxi67, calmer74/offers speak police75/urges K keep singular promise76/call77 | EV0010–0013; CL0026@6. Not securely physically injured; continuing R attachment no K-priority demand |
| PG-CS-0206@1 / CHAR0004 / CS0201 | CHOICE/KNOWLEDGE: helps Mis/urgent vague M call71–72/stays/police obligation75, recognizes has not told M76/failed call77/empty plaza2:15_88 | EV0011–0014; CL0006@15. Real obligation plus available alternative and own assumption, not solely unavoidable misfortune |
| PG-CS-0207@1 / CHAR0001 / CS0199 | KNOWLEDGE/CHOICE: partial taxi/Mis witness67/bystander68, vague call71/manual off80/waits beyond deadline84/leaves/private goodbye99 | EV0011–0015; CL0013@11. Cannot infer she knows R injury/police/first-choice preference |
| PG-CS-0208@1 / CHAR0002 / CS0200 | CHOICE/KNOWLEDGE: arrives81/hears partial witness84/suggests circumstances85/follows M train90/admits102 | EV0013–0016; CL0015@10. No prior M trip invitation or full K reason known |
| PG-CS-0209@1 / CHAR0003 / CS0189 | CHOICE/AFFECT: criticizes broken promise107–108/travels K, learns R injury109/panics110/plans home114 | EV0018–0019; CL0002@14/0003@13. M-alone inference wrong; no new proven scheme/actual arrival R/train-stop mechanism |
| PG-CS-0210@1 / CHAR0027 / NONE | CHOICE: persists after refusal99–100/grabs wrist101, leaves102 when T challenges | EV0016; unwanted contact not mutual flirting/sex implication |
| PG-CS-0211@1 / CHAR0001 / CS0207 | CHOICE/STATEMENT: refuses stranger100/thanks T, says wanted solitude103/reflects with T at distance105–106, storm prevents planned return111 | EV0016–0019; CL0013@11/0017@12. No actual present self-harm plan; concern not T travel invitation |
| PG-CS-0212@1 / CHAR0002 / CS0208 | CHOICE: intervenes101/apologizes following102/offers wait104/sits apart105, accepts stranded inn115/initiates hug120/renewal question121/actual kiss129 | EV0016–0021; CL0015@10. Care/intrusion/stake distinct; initial prior affirmative permission unshown |
| PG-CS-0213@1 / CHAR0004 / CS0206 | CHOICE/ACCOUNTABILITY: tells S family injury109/spends/road125–146, owns arrogance140/pays/climbs/falls/inn call147/battery dies148/seaside alone165 | EV0018–0024/0027–0028; CL0006@15/0028@5. No M words receipt/meeting or secure T identity from inn registration |
| PG-CS-0214@1 / CHAR0001 / CS0211 | CHOICE/AFFECT: responds kiss/neck embrace130/pleased earring137/shared intimate night150–156/turns toward T155, handhold157/questions relief/flow158–159 | EV0021–0022/0025–0026; CL0013@11. Sexual encounter strongly implied, specific act not depicted; uncertainty not absence of attraction |
| PG-CS-0215@1 / CHAR0002 / CS0212 | CHOICE: ignores unknown caller133/birthday regret134/recognizes earring137/restart138/affection morning/handhold157/L love sign163 | EV0022/0025–0028; CL0005@10/0015@10. No known K caller or complete M private uncertainty receipt; wish not forever guarantee |
| PG-CS-0216@1 / CHAR0001 / CS0214 | CHOICE/AFFECT: return train161 still K hope/no clear breakup, sees T old sign163–164/runs back165/embraces166/wishes happiness | EV0027–0028; CL0013@11. Actual romantic return T, no direct K breakup message or permanent K feeling eradication |

Pre-canonical weapon recheck62/74 corrects private bat label to sword/imitation; actual later R contusions not Misao injury. Final partition recomputed161 mainline, all175 viewed. Next CHAR0028, CS0217, RD0001. Revision0.14 — V15 successors2026-10-20; all prior bodies/rows retained.
