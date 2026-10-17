---
title: "Peach Girl — Information Circulation and Reputation"
artifact_id: PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER
artifact_type: information_reputation_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.2"
status: active_provisional
scope: "Information Circulation and Reputation; source-derived records through the committed high-water mark named in the entrypoint"
source_boundary: "Original Japanese 新装版 mainline; admitted volumes through the entrypoint's committed high-water mark; prospective rows carry their own frontier"
canonical_home: series/peach-girl/03 Longitudinal Ledgers/PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Information Circulation and Reputation

This instrument owns consequential propositions, who knows or believes them, how they circulate and how an identifiable audience's account shapes reputation. These typed records share a home because transmissions connect individual belief to public standing; factual truth and social evaluation remain separate fields. It does not own general character traits or pair attachment.

Neither rumor nor deception is presumed to occur. Deliberate misinformation requires evidence of knowledge and intent, not merely a false statement.

## Records and allocation

| Type / stable identifier | Required fields |
| --- | --- |
| Proposition `PG-IP-####` | Bounded proposition; continuity; source-truth status and basis at cutoff; first observation/frontier; uncertainty; material claim/version |
| Knowledge/belief event `PG-KN-####` | Subject/audience; proposition; `KNOWS / BELIEVES / SUSPECTS / DENIES / UNAWARE_WITH_EVIDENCE / UNKNOWN`; attributed versus inferred status; acquisition basis; represented time/certainty; learned-after frontier; observation refs; prior/correction |
| Transmission `PG-TX-####` | Sender, actual recipients/audience, proposition/version, communicated formulation, channel/context; sender knowledge and intention basis or unknown; recipient reception evidence; omissions/distortion as supported; time/frontier; outcome and source refs |
| Reputation event `PG-RP-####` | Target subject; identifiable audience and its scope; attributed evaluation or label; observed treatment/consequence; linked proposition/transmission or independent basis; target awareness; time/frontier; evidence/claim/alternative/support; prior |
| Current information view | Proposition × subject/audience × cutoff; active belief/transmission refs; source-truth distinction; unresolved reach/identity |
| Current reputation view | Target × audience × cutoff; active RP refs; scoped social account; disagreement/unknown reach |

Proposition truth states: `ESTABLISHED_AT_BOUNDARY / REFUTED_AT_BOUNDARY / DISPUTED / UNRESOLVED`, with source support rather than an omniscient default. A character's certainty is not the truth state. Do not infer that every peer received a rumor from one observed recipient, that absence from a scene proves ignorance, or that one person's label represents the whole school.

An audience can remain a bounded unnamed group; do not invent its members. Reputation may arise from perceived appearance, performance, affiliation or an explicit judgment as well as transmitted propositions. Attribution and consequences are required before calling it an audience's social state. Link directional trust/affiliation consequences to the relationship ledger without making reputation itself a romantic fact.

## Evidence, update and history

Allocate monotonic IDs only after admitted observations. Every event includes `PG-EV-VNN-####` and exact locator, represented time/certainty, disclosure frontier and support strength/basis. Mark uncertainty separately for proposition truth, mental state, sender intent, recipient reach and timing. Material causal interpretations cite `PG-CL@version`, counterevidence and an alternative. Direct speech establishes a communication, not necessarily belief or successful persuasion.

A future VNN transaction adds a proposition when its identity must persist across encounters, appends belief/transmission/reputation changes that affect interpretation, and links corrected or newly disclosed information. Transient local facts stay in their reading. Deception, omission, misunderstanding and unreliable recollection remain competing explanations until evidence discriminates them.

Preserve original formulations and historical truth/belief states. Append later corrections/disclosures and update current views through targeted edits; never make an earlier reader or character know the later outcome. Different proposition versions remain linked if meaning changes. A unit freeze records active versions and its epistemic boundary. The closeout explicitly certifies update/no-material-change for this home.

Bootstrap source-derived propositions, belief events, transmissions, reputation events and current projections: **0**.

## Propositions

| Proposition / version | Formulation / continuity / first frontier | Truth at boundary / basis / uncertainty | Evidence / claim version |
| --- | --- | --- | --- |
| PG-IP-0001@1 | Momo has loved Tōji since middle school / V01 i0014 | ESTABLISHED_AT_BOUNDARY / narration | PG-EV-V01-0004, -0021, -0026 |
| PG-IP-0002@1 | Momo likes Kairi (decoy) / i0021 | REFUTED_AT_BOUNDARY / her narration shows a deliberate lie | PG-EV-V01-0007 |
| PG-IP-0003@1 | Momo and Kairi have kissed / i0035 | When first said: the speaker's belief rested on a disputed CPR memory. After i0053: ESTABLISHED as an unrequested kiss by Kairi | PG-EV-V01-0013, -0017, -0018 |
| PG-IP-0004@1 | Momo uses tanning salons, plays around, would do compensated dating / i0016 | REFUTED_AT_BOUNDARY / ex-swim-club tan (Tōji, Momo); conduct shown | PG-EV-V01-0005, -0014; PG-CL-0001@1 |
| PG-IP-0005@1 | Tōji dislikes dark-skinned girls / wants a girlfriend paler than him / i0077, i0104 | DISPUTED / second-hand report; Tōji does not recall saying it and disowns it | PG-EV-V01-0027, -0028, -0033; PG-CL-0008@1 |
| PG-IP-0006@1 | Momo and Tōji are dating / D-3 | ESTABLISHED_AT_BOUNDARY | PG-EV-V01-0033, -0036 |
| PG-IP-0007@1 | Tōji is Sae's boyfriend; he kissed her and tried to push her down at his house / i0123–i0126 | DISPUTED (leaning fabricated) / contradicted by Tōji's statement of inexperience and the chronology; no admission | PG-EV-V01-0040, -0043, -0048; PG-CL-0003@1 |
| PG-IP-0008@1 | Momo finds Tōji boring and prefers Kairi / i0173 | REFUTED_AT_BOUNDARY / Momo's depicted words at i0167–i0170 contradict it | PG-EV-V01-0050, -0052 |
| PG-IP-0009@1 | Momo moved the meeting to the cafeteria / i0162 | REFUTED_AT_BOUNDARY / i0161 | PG-EV-V01-0049 |
| PG-IP-0010@1 | Sae and Tōji kissed under the pergola on D0 morning / i0140 | ESTABLISHED (event); who initiated: Sae (reader-only i0138); Tōji's participation unresolved | PG-EV-V01-0043, -0044 |
| PG-IP-0011@1 | Momo gave Kairi mouth-to-mouth two years ago / i0049 | DISPUTED / Momo: a lifeguard did; Kairi: memory of hair | PG-EV-V01-0017, -0035; PG-CL-0007@1 |
| PG-IP-0012@1 | Kairi rejected Sae over a bag she took from someone / i0030–i0031 | Core ESTABLISHED (i0028); the 'sister' version distorted/UNRESOLVED | PG-EV-V01-0009, -0010 |
| PG-IP-0013@1 | Momo hit Sae (bruise) / i0028 | REFUTED_AT_BOUNDARY / bruise was makeup (i0063) | PG-EV-V02-0006, -0017 |
| PG-IP-0014@1 | Sae was injured by Momo's push / i0037 | REFUTED_AT_BOUNDARY / feigned (i0040) | PG-EV-V02-0009 |
| PG-IP-0015@1 | Tōji is hospitalized with appendicitis / i0055 | ESTABLISHED_AT_BOUNDARY | PG-EV-V02-0013 |
| PG-IP-0016@1 | Momo declined to visit Tōji / i0060 | REFUTED_AT_BOUNDARY / Momo did not know | PG-EV-V02-0015 |
| PG-IP-0017@1 | Momo seduced or stole her best friend Sae's boyfriend Tōji / i0078 | REFUTED_AT_BOUNDARY / Tōji is Momo's boyfriend | PG-EV-V02-0020 |
| PG-IP-0018@1 | Momo is promiscuous (ヤリマン) / i0058 | REFUTED_AT_BOUNDARY / conduct and first kiss | PG-EV-V02-0014; PG-CL-0001@1 |
| PG-IP-0019@1 | Momo two-timed Tōji with Kairi (stairs hug) / i0081 | REFUTED_AT_BOUNDARY / accident plus Kairi's unrequested hold | PG-EV-V02-0019, -0022 |
| PG-IP-0020@1 | The pergola kiss was 'practice' for kissing Momo / i0159 | DISPUTED as framing / Sae's framing; Tōji refused twice (V01 i0138); his assent is not shown | PG-EV-V02-0039 |
| PG-IP-0021@1 | Sae wants Tōji / i0122 | ESTABLISHED_AT_BOUNDARY as her statement | PG-EV-V02-0028 |
| PG-IP-0005@2 | (revision of IP-0005) Tōji dislikes dark-skinned girls | REFUTED_AT_BOUNDARY / the originating friend admits fabrication; Tōji's type was 'active and bright' (her report) | PG-EV-V03-0010; PG-CL-0008@2 |
| PG-IP-0022@1 | Tōji's wound reopened and his stay was extended because of Momo / i0022 | DISPUTED / the nurse says 2 more days to discharge (i0035); his fall after the fruit is depicted | PG-EV-V03-0003, -0007 |
| PG-IP-0023@1 | Momo is deliberately losing races out of spite / i0102 | REFUTED_AT_BOUNDARY / strap sabotage (i0064, i0073) | PG-EV-V03-0023 |
| PG-IP-0024@1 | Momo threatened to jump unless Tōji dated her / i0103 | REFUTED as framed / the actual demand was to be heard (V02 i0113–0116) | PG-EV-V03-0023 |
| PG-IP-0025@1 | Momo embraced Kairi in her underwear in the changing room / i0121 | ESTABLISHED (core) with distorted framing / Kairi entered and embraced her after refusal | PG-EV-V03-0021, -0028 |
| PG-IP-0026@1 | Sae instructed the swimsuit sabotage / i0067 | ESTABLISHED / Sae's own words; Kako's testimony | PG-EV-V03-0015, -0035 |
| PG-IP-0027@1 | Sae's method: 'whoever cries first wins' / i0110 | ESTABLISHED as her statement | PG-EV-V03-0025 |
| PG-IP-0028@1 | Sae has stolen other girls' boyfriends in the past / i0163 | STRONGLY_SUPPORTED (multiple testimony; not depicted) | PG-EV-V03-0035 |
| PG-IP-0029@1 | Tōji kissed Sae and said he loved her, leading her on / i0160 | REFUTED_AT_BOUNDARY / no such declaration depicted; kiss initiated by Sae (V01 i0138, V02 i0100) | PG-EV-V03-0034 |
| PG-IP-0030@1 | Kairi recruited Sae's past victims by phone the night before the swim meet to testify against her / V04 i0068 | TRUE_AT_BOUNDARY / Sumire's account; Kairi confirms (i0076) | PG-EV-V04-0014, -0016; PG-CL-0006@4 |
| PG-IP-0031@1 | Kairi organized the exposure to gain Momo's gratitude and win her while Tōji was away / i0076 | CONTESTED / his own statement, framed as a joke; Momo and Sumire read it as care for Momo | PG-EV-V04-0014, -0016 |
| PG-IP-0032@1 | The line about Momo being easily misjudged (V01 i0083) was originally Tōji's / i0026 | TRUE / V01 i0070 depiction; Kairi's disclosure | PG-EV-V04-0005 |
| PG-IP-0033@1 | Momo refused Tōji because she feared not being believed again / i0023, i0029 | TRUE (as her stated reason) / Momo later reinterprets it as fear of rejection | PG-EV-V04-0003, -0007; PG-CL-0012@2 |
| PG-IP-0034@1 | Tōji has never said 「好き」 since they started dating / i0108 | CONSISTENT_WITH_RECORD / only V01 i0101 (pre-dating confession) depicted | PG-EV-V04-0024 |
| PG-IP-0035@1 | Sae withdrew from the movie out of consideration for the couple / i0143 | CONTESTED / she did withdraw; her private fantasy and shoe stamping show hostility | PG-EV-V04-0032; PG-CL-0016@1 |
| PG-IP-0036@1 | Sae made the cookies she gave the studio staff / i0155 | FALSE / Momo bought them (i0145) | PG-EV-V04-0036 |
| PG-IP-0037@1 | Momo dominates Sae at school, insisted on coming to the studio, and is moody / i0158 | FALSE / Sae invited Momo (i0146); Momo wanted to leave (i0147, i0156) | PG-EV-V04-0037; PG-CL-0018@1 |
| PG-IP-0038@1 | Momo is jealous of Sae because Sae is cute / i0159 (Jigoro's inference) | UNSUPPORTED / no depicted jealousy | PG-EV-V04-0037 |
| PG-IP-0039@1 | Jigoro fell for Sae at first sight and asked to see her again / i0161 | EXAGGERATED_AT_TELLING; substantially vindicated by his confession (i0169–i0170) | PG-EV-V04-0038, -0040 |
| PG-IP-0040@1 | Sae was the first to befriend Momo at high school (entrance-exam eraser; partner offer) / i0112 | REVEALED_NOT_NEW / Momo's memory | PG-EV-V04-0025 |
| PG-IP-0041@1 | Sae was disliked among girls from the start and changed her manner in front of boys / i0014 | PLAUSIBLE / girls' retrospective claim; consistent with V03 testimony | PG-EV-V04-0001 |
| PG-IP-0042@1 | Jigoro has no girlfriend; rumored gay or too vain for ordinary women / i0150 | RUMOR / staff speculation | PG-EV-V04-0035 |

## Knowledge and belief events

| Event / prior | Subject or audience / proposition | State / attribution / acquisition basis | Story time / learned after | Evidence / uncertainty / correction |
| --- | --- | --- | --- | --- |
| PG-KN-0001 / — | Sae / IP-0001 | SUSPECTS (inferred from i0014–i0020; later claimed by her at i0079) | Opening day / V01 | PG-EV-V01-0004, -0028 |
| PG-KN-0002 / KN-0001 | Sae / IP-0001 | KNOWS / overheard | D-4 | PG-EV-V01-0026, -0028 |
| PG-KN-0003 / — | Kairi / IP-0001 | KNOWS / Momo told him; name from purikura | D-4 | PG-EV-V01-0026 |
| PG-KN-0004 / — | Tōji / IP-0001 | KNOWS / overheard | D-4 | PG-EV-V01-0026, -0032 |
| PG-KN-0005 / — | Classmates (bounded unnamed audience) / IP-0003 | BELIEVES / Kairi's statement and rumor | ~1 wk → DayA+1 | PG-EV-V01-0020; reach unknown |
| PG-KN-0006 / — | Tōji / IP-0003 | UNKNOWN → asks Kairi (i0069) | DayA+1 | PG-EV-V01-0024 |
| PG-KN-0007 / — | Momo / IP-0005 | BELIEVES (MS-friend report) → revised by Tōji's denial at D-3 | MS → D-3 | PG-EV-V01-0027, -0033 |
| PG-KN-0008 / — | Kairi / IP-0006 | KNOWS / Tōji's 「オレのだから」 | D-2 | PG-EV-V01-0036 |
| PG-KN-0009 / — | Sae / IP-0006 | KNOWS / witnessed the confession; later told by Momo | D-3; D0 | PG-EV-V01-0034, -0048 |
| PG-KN-0010 / — | Classmates of 1-3 / IP-0006 | UNAWARE_WITH_EVIDENCE; believe Sae–Tōji are dating | D0 | PG-EV-V01-0047 |
| PG-KN-0011 / — | Tōji / 'Momo told Sae about us' | BELIEVES (false) / Sae's affirmation | D-1 or D0 | PG-EV-V01-0042 |
| PG-KN-0012 / — | Momo / IP-0007 | SUSPECTS (after the packet) then DENIES in argument (i0150) — unstable | D-1 → D0 | PG-EV-V01-0041, -0045 |
| PG-KN-0013 / — | Tōji / IP-0008 | BELIEVES (inferred from action; not stated) | D0 | PG-EV-V01-0052, -0053 |
| PG-KN-0014 / — | Tōji / IP-0009 | BELIEVES / Sae's relay | D0 | PG-EV-V01-0049, -0051 |
| PG-KN-0015 / — | Momo; Kairi / IP-0010 | KNOW (witnesses) without the coercive prelude | D0 | PG-EV-V01-0044 |
| PG-KN-0016 / — | Momo / 'Sae wrote the graffiti' | BELIEVES / inference from a false exclusivity premise | ~1 wk | PG-EV-V01-0011; truth UNRESOLVED |
| PG-KN-0017 / — | Tōji / IP-0013 | BELIEVES (inferred; suspicion at i0039) / Sae's implication plus Momo's words | V02 day 1 | PG-EV-V02-0006, -0025 |
| PG-KN-0018 / — | Momo / IP-0015 | UNAWARE_WITH_EVIDENCE until day 3; then KNOWS via Kairi | V02 day 1–3 | PG-EV-V02-0013, -0021 |
| PG-KN-0019 / — | Class 3 (bounded audience) / IP-0015 + instruction to withhold | KNOWS; withholds (reported) | V02 day 1 | PG-EV-V02-0021 |
| PG-KN-0020 / — | Tōji / IP-0016 | BELIEVES (inferred from his reaction) | V02 | PG-EV-V02-0015 |
| PG-KN-0021 / — | Kairi / Sae's coercive plan and goal | KNOWS / told by Sae | Hospital day | PG-EV-V02-0030, -0032 |
| PG-KN-0022 / — | Sae / IP-0003 (Kairi–Momo kiss real) | KNOWS / Kairi's admission | Hospital day | PG-EV-V02-0032 |
| PG-KN-0023 / KN-0014 | Tōji / IP-0009 (cafeteria) | KNOWS false / Momo's disclosure | Hospital day | PG-EV-V02-0035 |
| PG-KN-0024 / — | Tōji / IP-0003 | KNOWS kiss occurred (Sae; Momo admits); lacks context of non-consent | Hospital day | PG-EV-V02-0037 |
| PG-KN-0025 / — | Momo / IP-0020 | BELIEVES Tōji accepted 'practice' / Sae's statement and Tōji's 「キスだけどキスじゃない」 | Hospital day | PG-EV-V02-0039 |
| PG-KN-0026 / KN-0011 | Tōji / 'Sae has no motive to lie' | Doubt emerging (i0149) | Hospital day | PG-EV-V02-0036 |
| PG-KN-0027 / KN-0007 | Momo / IP-0005@2 | KNOWS false / Kyō-chin's admission | Swim week | PG-EV-V03-0010 |
| PG-KN-0028 / — | Momo / IP-0026 | SUSPECTS → strongly infers the strap was cut underwater | Swim meet | PG-EV-V03-0018 |
| PG-KN-0029 / KN-0026 | Tōji / IP-0027 + Sae's plan for him | KNOWS / overheard | Swim meet | PG-EV-V03-0025 |
| PG-KN-0030 / — | Class 3 / IP-0028, IP-0026 | KNOWS (testimony) / revises belief about Sae | Swim meet | PG-EV-V03-0034, -0035 |
| PG-KN-0031 / — | Class 3 / Momo–Tōji relationship | KNOWS / Tōji's declaration | Swim meet | PG-EV-V03-0032 |
| PG-KN-0032 / — | Kako / Sae's deception toward her | KNOWS | Swim meet | PG-EV-V03-0035 |
| PG-KN-0033 / — | Momo / Tōji's overhearing of Sae | KNOWS (implied by his public quotation) | Swim meet | PG-EV-V03-0033 |
| PG-KN-0034 / — | Kairi / Momo's inner fluttering | UNAWARE_WITH_EVIDENCE (her narration only) | Swim meet | PG-EV-V03-0022 |
| PG-KN-0035 / — | Tōji / Momo's reason for refusing | UNKNOWN | End of V03 | PG-EV-V03-0037 |
| PG-KN-0036 / — | Momo / IP-0030 | KNOWS / Sumire's testimony, then Kairi's confirmation | Second term | PG-EV-V04-0014, -0016 |
| PG-KN-0037 / KN-0035 | Tōji / Momo's love and request | KNOWS (her declaration); her stated reason told only to Kairi | End of term | PG-EV-V04-0009 |
| PG-KN-0038 / — | Momo / IP-0032 | KNOWS / Kairi's disclosure | Day after the meet | PG-EV-V04-0005 |
| PG-KN-0039 / — | Kairi / IP-0033 | KNOWS / Momo told him | Day after the meet | PG-EV-V04-0003 |
| PG-KN-0040 / — | Kairi / Tōji's kiss was refused | KNOWS / guess confirmed by Tōji's reaction | Second term | PG-EV-V04-0023 |
| PG-KN-0041 / — | Tōji / Kairi often pressed kisses on Momo | BELIEVES / Kairi's boast; exaggeration likely | Second term | PG-EV-V04-0023 |
| PG-KN-0042 / — | Class / meaning of Tōji's L sign | UNAWARE / read as a joke | Second term | PG-EV-V04-0028 |
| PG-KN-0043 / — | Momo and Tōji / IP-0035 | BELIEVE considerate withdrawal / Sae's private conduct unwitnessed | Late September | PG-EV-V04-0032 |
| PG-KN-0044 / — | Jigoro / IP-0037, IP-0038 | BELIEVES (false) / visual impression plus Sae's account | Late September | PG-EV-V04-0036, -0037 |
| PG-KN-0045 / — | Classmates / IP-0039 | DISBELIEVE, then witness Jigoro's confession | Late September | PG-EV-V04-0038, -0040 |
| PG-KN-0046 / — | Momo / IP-0036 | KNOWS false (witness); says nothing | Late September | PG-EV-V04-0036 |

## Transmissions

| Event / prior | Sender / recipients / proposition / formulation | Channel / sender knowledge and intent basis | Reception / distortion / consequence | Time / frontier / evidence / uncertainty |
| --- | --- | --- | --- | --- |
| PG-TX-0001 / — | Unknown / boys / IP-0004 | Rumor / unknown | Repeated by boys; corrected by Tōji to that audience | Opening day / PG-EV-V01-0005 |
| PG-TX-0002 / — | Tōji / boys / correction (ex-swim club) | Speech / Tōji's MS knowledge | Boys accept (「よく知ってんじゃん」) | Opening day / PG-EV-V01-0005 |
| PG-TX-0003 / — | Momo / Sae / IP-0002 | Speech / deliberate lie (narration) | Sae later treats it as cover; turns it against Momo (i0127) | Opening day / PG-EV-V01-0007, -0040 |
| PG-TX-0004 / — | Unknown / neighboring class / IP-0012 (sister version) | Rumor / unknown | Distorted | ~1 wk / PG-EV-V01-0010 |
| PG-TX-0005 / — | Unknown author / blackboard viewers / Momo–Kairi pairing | Graffiti / unknown | Wide exposure; secondary rumor that Momo wrote it | ~1 wk / PG-EV-V01-0011, -0012 |
| PG-TX-0006 / — | Kairi / mocking girls → school / IP-0003 | Speech / believes the CPR memory; motive unknown | Fan-bloc confrontation; rumor spreads | ~1 wk / PG-EV-V01-0013, -0014 |
| PG-TX-0007 / — | MS friend / Momo / IP-0005 | Speech (flashback) / unknown | Momo's tan regimen and confession condition | Middle school / PG-EV-V01-0027 |
| PG-TX-0008 / — | Sae / Momo / IP-0007 | 'Consultation' / Sae knows of the D-3 confession; intent inferred from i0128 | Momo doubts Tōji; avoidance | D-1 / PG-EV-V01-0040 |
| PG-TX-0009 / — | Sae / Tōji / 'Momo told me' + false account of Momo's coldness | Speech / knows both false | Tōji confides; accepts advice | D0 / PG-EV-V01-0042 |
| PG-TX-0010 / — | Sae / Tōji / IP-0009 | Speech / overheard true location: deliberate | Tōji waits in the cafeteria | D0 / PG-EV-V01-0049 |
| PG-TX-0011 / — | Sae / Tōji / IP-0008 (fabricated quotations) | Speech / fabricated | Tōji's jealous approach | D0 / PG-EV-V01-0052 |
| PG-TX-0012 / — | Sae / Momo / 'Tōji wants you for sex' | Insinuation / no basis shown | Momo's fear at the pergola | D0 / PG-EV-V01-0048, -0053 |
| PG-TX-0013 / — | Sae / Tōji / IP-0013 (implied via 「ぶつけたの」) | Performance / knows it is makeup | Tōji suspects Momo | V02 day 1 / PG-EV-V02-0006, -0017 |
| PG-TX-0014 / — | Sae / Tōji & class / IP-0014 | Performance / feigned | Tōji condemns Momo | V02 day 1 / PG-EV-V02-0009 |
| PG-TX-0015 / — | Sae / class 3 / withhold IP-0015 from Momo | Request (Kairi's report) / deliberate | Momo uninformed for three days | V02 day 1 / PG-EV-V02-0021 |
| PG-TX-0016 / — | Sae / Tōji / IP-0016 | Implication / knows false | Tōji hurt | V02 days 1–3 / PG-EV-V02-0015 |
| PG-TX-0017 / — | Sae / Tōji / IP-0019 + secrecy as two-timing | Speech / framing distorted | Tōji's suspicion of Kairi | V02 day 3 / PG-EV-V02-0022 |
| PG-TX-0018 / — | Unknown / class 3 → Kairi's fans / IP-0017 | Rumor / unknown | Saturates class 3 | V02 / PG-EV-V02-0020 |
| PG-TX-0019 / — | Kairi / Momo / IP-0015 + blockade account | Speech / learned from others | Momo goes to hospital | V02 day 3 / PG-EV-V02-0021 |
| PG-TX-0020 / — | Momo / Tōji / IP-0009 false + Sae's lies | Speech (coerced hearing) / sincere | Tōji begins to doubt | Hospital day / PG-EV-V02-0035 |
| PG-TX-0021 / — | Sae / Tōji / IP-0003 framed as Momo's lie | Accusation / knows the kiss occurred; omits non-consent | Rupture | Hospital day / PG-EV-V02-0037 |
| PG-TX-0022 / — | Sae / Momo & Tōji / IP-0020 | Speech / her own framing | Momo's contempt for Tōji; breakup | Hospital day / PG-EV-V02-0039 |
| PG-TX-0023 / — | Sae / class 3 / IP-0022 | Speech / exaggeration | Class hostility toward Momo | Day after breakup / PG-EV-V03-0003 |
| PG-TX-0024 / — | Kyō-chin / Momo / IP-0005 refuted | Confession / sincere | Grief; regret of the breakup | Swim week / PG-EV-V03-0010 |
| PG-TX-0025 / — | Sae / three girls / sabotage instruction | Whisper (content later stated) / deliberate | Assault; Kako nearly drowns | Swim meet / PG-EV-V03-0014, -0015 |
| PG-TX-0026 / — | Sae / classmates / IP-0023, IP-0024 | Speech / distorted | Hostility; prostration demand | Swim meet / PG-EV-V03-0023 |
| PG-TX-0027 / — | Unknown other-class student / gossip circle → Sae / IP-0025 | Rumor | Sae weaponizes it | Swim meet / PG-EV-V03-0028 |
| PG-TX-0028 / — | Sae / Kairi (overheard by Tōji) / IP-0027 + plan | Boast / sincere, elicited by flattery | Tōji's disillusionment | Swim meet / PG-EV-V03-0025 |
| PG-TX-0029 / — | Tōji / class / Sae's metaphor; relationship claim | Public speech / sincere | Class reconsiders | Swim meet / PG-EV-V03-0032, -0033 |
| PG-TX-0030 / — | Past-victim girls, admirer, Kako / class / IP-0028, IP-0026 | Public testimony / sincere | Sae abandoned | Swim meet / PG-EV-V03-0035 |
| PG-TX-0031 / — | Sae / class / IP-0029 | Public claim / false | Rejected | Swim meet / PG-EV-V03-0034 |
| PG-TX-0032 / — | Kairi / Sumire and other past victims / Sae's misconduct; invitation to 「リベンジ」 | Phone, night before the meet / deliberate | Testimony at the meet (V03 TX-0030) | Swim week / PG-EV-V04-0014 / reported by Sumire |
| PG-TX-0033 / — | Sumire / Momo / IP-0030 | Conversation / sincere | Momo's reinterpretation of Kairi | Second term / PG-EV-V04-0014 |
| PG-TX-0034 / — | Kairi / Momo / IP-0032 | Conversation / sincere, against his interest | Momo shocked | Day after the meet / PG-EV-V04-0005 |
| PG-TX-0035 / — | Momo / Kairi / IP-0033 | Conversation / sincere | Kairi's confrontation | Day after the meet / PG-EV-V04-0003 |
| PG-TX-0036 / — | Kairi / Tōji / 'you take people's words at face value' | Conversation (reported by Tōji) / advice | Tōji adopts it as his self-account | Before the ceremony / PG-EV-V04-0008 |
| PG-TX-0037 / — | Kako / swim-club girls / Momo's 「モデルデビュー」 | Gossip / exaggeration | Teasing | Late September / PG-EV-V04-0031 |
| PG-TX-0038 / — | Sae / studio staff / IP-0036 | Speech / false | Praise for Sae | Late September / PG-EV-V04-0036 |
| PG-TX-0039 / — | Sae / Jigoro / IP-0037 | Private speech / false, self-serving | Jigoro's hostile belief and sympathy for Sae | Late September / PG-EV-V04-0037 |
| PG-TX-0040 / — | Sae / classmates / IP-0039 | Speech / exaggerated | Mocked as a liar; later vindicated | Late September / PG-EV-V04-0038 |
| PG-TX-0041 / — | Tōji / Momo (and the class) / 「好き」 | Public hand sign / private code | Momo receives; class reads a joke | Second term / PG-EV-V04-0028 |
| PG-TX-0042 / — | Girls of Class 3 / class / IP-0041 | Speech at the party / retrospective | Boys surprised | Day of the meet / PG-EV-V04-0001 |

## Reputation events

| Event / prior | Target / audience / attributed evaluation | Observed treatment / target awareness | Information links / time / frontier | Evidence / claim / support / alternative |
| --- | --- | --- | --- | --- |
| PG-RP-0001 / — | Momo / male classmates / 遊んでる; tanning salons | Mockery; Momo overhears | TX-0001 / opening day | PG-EV-V01-0005 / PG-CL-0001@1 / HIGH |
| PG-RP-0002 / — | Momo / Kairi's fan bloc / 失格; likely enkō | Confrontation; charm destroyed | TX-0006 / ~1 wk | PG-EV-V01-0014, -0015 / HIGH |
| PG-RP-0003 / — | Momo / hallway girls / 遊んでた; 今度は違う男 | Whispering | TX-0006; IP-0006 rumor / DayA+1, D-2 | PG-EV-V01-0037 / HIGH |
| PG-RP-0004 / — | Sae / male classmates / class No. 1; pale and cute | Admiration; gifts | Independent (appearance) / opening day onward | PG-EV-V01-0005, -0038 / HIGH |
| PG-RP-0005 / — | Sae / female onlookers / fawning (コビコビ) | Resentful talk | Independent / ~1 wk | PG-EV-V01-0009 / MODERATE |
| PG-RP-0006 / — | Kairi / female classmates / never serious with anyone | Talk | Independent / DayA+1 | PG-EV-V01-0019 context, i0065 / MODERATE |
| PG-RP-0007 / RP-0003 | Momo / class 3 / ヤリマン; best-friend's-boyfriend thief | Slurs, shoe defacement, exclusion; Momo aware | TX-0018 / V02 | PG-EV-V02-0014, -0020 / HIGH |
| PG-RP-0008 / — | Sae / class 3 / considerate friend nursing Tōji | Cooperation with the blockade | TX-0015 / V02 | PG-EV-V02-0021 / MODERATE |
| PG-RP-0009 / — | Momo / Tōji / 'friend-betraying, violent' (temporary) | 「見損なったよ」 | TX-0013, -0014 / V02 day 1 | PG-EV-V02-0010 / HIGH |
| PG-RP-0010 / RP-0007 | Momo / class 3 / violent, spiteful bully of Sae | Tacks, tripping, soaking, prostration demand | TX-0023, -0026 / swim week | PG-EV-V03-0003, -0005, -0030 / HIGH |
| PG-RP-0011 / RP-0010 | Momo / class 3 / swimming star; 'not such a bad girl' | Cheering after her wins; Kako's defense | Independent (performance) / swim meet | PG-EV-V03-0027 / HIGH |
| PG-RP-0012 / RP-0011 | Momo / class 3 / vindicated; wronged party | Class walks out on Sae | TX-0029, -0030 / swim meet | PG-EV-V03-0034–0036 / HIGH |
| PG-RP-0013 / RP-0008 | Sae / class 3 / liar, thief (サイテー女) | Abandonment | TX-0030 / swim meet | PG-EV-V03-0035, -0036 / HIGH |
| PG-RP-0014 / RP-0006 | Kairi / girls / playboy arranging summer dates | Talk | Independent / swim meet | PG-EV-V03-0017 context / MODERATE |
| PG-RP-0015 / RP-0012 | Momo / class 3 / swim-meet heroine, wronged and forgiving | Apologies, cheering, couple teasing | Independent / day of the meet | PG-EV-V04-0001 / HIGH |
| PG-RP-0016 / RP-0013 | Sae / class 3 and others / liar to be shunned and punished | Trampling, baking destroyed, ball, forced graffiti | TX-0030, -0042 / second term | PG-EV-V04-0011, -0022, -0025, -0039 / HIGH |
| PG-RP-0017 / — | Momo / Jigoro / cruel, domineering, jealous | Hostile remarks to Sae; Momo unaware | TX-0039 / late September | PG-EV-V04-0036, -0037; PG-CL-0018@1 / HIGH |
| PG-RP-0018 / — | Sae / studio staff / cute, young, considerate, good at baking | Praise | TX-0038 / late September | PG-EV-V04-0034, -0036 / HIGH |
| PG-RP-0019 / — | Jigoro / staff and fans / No. 1 model, 'pheromone', no girlfriend, rumored gay | Swooning fans; staff gossip | Independent / late September | PG-EV-V04-0035 / HIGH (rumor content LOW) |
| PG-RP-0020 / RP-0001 | Momo / drunk salaryman / girl available for compensated dating | Proposition | Appearance / day of the meet | PG-EV-V04-0004 / HIGH |
| PG-RP-0021 / — | Momo and Tōji / class / affectionate couple | Teasing (「2人の周りだけ常夏」) | Independent / second term | PG-EV-V04-0010 / HIGH |

## Current information and reputation projections

| Projection type / subject or target / audience / boundary | Active event versions | Truth versus belief or attributed reputation | Unresolved scope / reach / timing |
| --- | --- | --- | --- |
| Information / Momo–Tōji relationship / school / PG-FR-V01 | KN-0008, -0009, -0010 | True; known only to Kairi and Sae; classmates believe Sae–Tōji | — |
| Information / Sae's fabrications / Tōji / PG-FR-V01 | KN-0011, -0013, -0014 | Tōji holds three false beliefs from Sae | When he learns |
| Reputation / Momo / peers / PG-FR-V01 | RP-0001…0003 | Appearance-based labels contrary to depicted conduct | Reach beyond observed audiences |
| Reputation / Sae / peers / PG-FR-V01 | RP-0004, -0005 | Admired by boys; resented by some girls | — |
| Information / Tōji's beliefs / PG-FR-V02 | KN-0017, -0020, -0023, -0024, -0026 | Knows the cafeteria lie; still holds the bruise belief; knows of the Kairi kiss without context | — |
| Reputation / Momo / class 3 / PG-FR-V02 | RP-0007 | Severe false reputation | Reach beyond class 3 |
| Reputation / Momo / class 3 / PG-FR-V03 | RP-0012 | Vindicated | Durability over the summer |
| Reputation / Sae / class 3 / PG-FR-V03 | RP-0013 | Exposed | Spread beyond class 3 |
| Information / tan report / Momo / PG-FR-V03 | KN-0027 | Known false | — |
| Reputation / Momo / class 3 / PG-FR-V04 | RP-0015, -0021 | Vindicated; known couple | — |
| Reputation / Momo / Jigoro / PG-FR-V04 | RP-0017; KN-0044 | False belief seeded by Sae | Whether it spreads or is corrected |
| Reputation / Sae / school / PG-FR-V04 | RP-0016; KN-0045 | Shunned as a liar; Jigoro's confession disrupts this | Effect of the confession |
| Information / Kairi's orchestration / Momo / PG-FR-V04 | KN-0036 | Known | Whether Tōji knows |
| Information / Sae's private hostility / Momo and Tōji / PG-FR-V04 | KN-0043 | Unknown to them | — |

Revision history: 0.1 — bootstrap schema, zero rows, 2026-10-16 UTC. 0.2 — V01 transaction rows appended (frontier PG-FR-V01), 2026-10-16 UTC. V02 transaction rows appended (frontier PG-FR-V02), 2026-10-16 UTC. V03 transaction rows appended (frontier PG-FR-V03), 2026-10-17 UTC. V04 transaction rows appended (frontier PG-FR-V04), 2026-10-17 UTC.
