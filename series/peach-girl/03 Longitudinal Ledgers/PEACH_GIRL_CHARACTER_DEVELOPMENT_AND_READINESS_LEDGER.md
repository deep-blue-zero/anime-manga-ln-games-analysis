---
title: "Peach Girl — Character Development and Readiness"
artifact_id: PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER
artifact_type: character_development_readiness_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.3"
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
