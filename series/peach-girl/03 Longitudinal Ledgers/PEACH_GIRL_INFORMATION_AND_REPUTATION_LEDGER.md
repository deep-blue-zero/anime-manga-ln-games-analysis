---
title: "Peach Girl — Information Circulation and Reputation"
artifact_id: PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER
artifact_type: information_reputation_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.8"
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

## Recipient audit boundary PG-AUDIT-20261019

New owner-authorized, non-blind V01–V04 correction pass; see the [source audit](../07%20Audits%20and%20Handoffs/PEACH_GIRL_CODEX_V01_V04_SOURCE_AUDIT_20261019.md). Learned after PG-FR-V04, before opening V05; narrative cutoff V04. Earlier frozen-boundary projections above are historical, not competing current authority. Submitted historical rows remain unchanged; original unsuffixed event rows have implicit version 1. The following successor versions and audit projections govern current retrieval until the next transaction. Corrections change the analyst's account, not characters' historical knowledge.

| Corrective version / original | Bounded proposition / source time | Current source-truth account | Evidence / issue |
| --- | --- | --- | --- |
| PG-IP-0018@2 / IP0018@1 | Broad sexualized promiscuity slur / V02 | UNRESOLVED as exhaustive biographical proposition; no source basis for slur, and depicted conduct/motives contradict its framing. Specific fabrications remain refuted. First kiss does not logically certify an entire sexual history | PG-EV-V02-0014; i0058–0067; A12 |
| PG-IP-0025@2 / IP0025@1 | Changing-room embrace / V03 | ESTABLISHED_AT_BOUNDARY: Kairi initiates after Momo's refusal; her response later softens. Rumor's 'Momo embraced him' is distorted agency, not an established initiation by her | PG-EV-V03-0021, -0022, -0028; i0086–0100; A13 |
| PG-IP-0029@2 / IP0029@1 | Sae's compound claim that Tōji kissed/loved/led her on / V03 | DISPUTED compound: depicted refusals contradict willing initiation; claimed declaration is unsupported, not exhaustively disproved solely by nondepiction. Her romantic/blame account is strongly discredited by source context | PG-EV-V01-0043, -0044; PG-EV-V03-0034; i0160–0167; A14 |

| Transmission correction / original | Sender / recipient / formulation | Corrected knowledge/truth distinction | Evidence / issue |
| --- | --- | --- | --- |
| PG-TX-0031@2 / TX0031 implicit @1 | Sae → class / IP0029@2 | Accusation and audience rejection established. Initiation distortion directly contradicted; exact alleged prior declaration UNKNOWN. No fabricated fact of universal refutation or new character knowledge | PG-EV-V03-0034; i0160–0167; A14 |

| Current projection / boundary | Active versions | Source versus audience state | Limits |
| --- | --- | --- | --- |
| Information / V02 slur @ PG-AUDIT-20261019 | IP0018@2; RP0007 | Harmful unsupported audience label and hostile treatment established; not verified biography | No exhaustive private-history assertion |
| Information / embrace @ PG-AUDIT-20261019 | IP0025@2; CM0016; TX0027 | Contact and later response differentiated from refusal/initiator and rumor grammar | Do not backdate later comfort as consent |
| Information / Sae's public claim @ PG-AUDIT-20261019 | IP0029@2; TX0031@2 | Blame-shifting claim discredited; public rejection does not establish every unshown utterance | Exact alleged love declaration remains UNKNOWN |

Historical knowledge frontiers remain unchanged. These are analyst truth-state corrections, not new messages received by the characters. Next IDs remain IP0043, KN0047, TX0043 and RP0022.

Revision history addendum: recipient source-audit successor corrections, 2026-10-19; original frozen states preserved.

## V05 successor transaction — PG-FR-V05

New Route B observations belong to [V05](../02%20Sequential%20Readings/PEACH_GIRL_V05_DEEP_READING.md); EV here means PG-EV-V05. All new rows have V05 learned-after boundary and within-volume frontier of cited evidence. Latest projections govern current retrieval, retaining historical audience truth/belief. No broad school knowledge inferred from a private scheme.

| Proposition / version | Bounded content / represented time | Source truth at V05 and limits | Evidence / claim |
| --- | --- | --- | --- |
| PG-IP-0010@2 | V01 practice kiss initiation/participation | ESTABLISHED initial Sae initiative and Tōji refusal; later acquiescence/motive now his retrospective self-report. Unshown motion not independently reconstructed | EV0017; V01 EV0043/0044; CM0008@3 |
| PG-IP-0020@2 | V01 practice-for-Momo framing | ESTABLISHED as Sae's earlier frame AND now Tōji's later self-account of seeking experience; not evidence prior willing initiation or romantic love for Sae | EV0017; CM0008@3 |
| PG-IP-0043@1 | L sign means love/like for Momo/Tōji | ESTABLISHED_AT_BOUNDARY; Momo tells Sae directly in V05 | EV0008 |
| PG-IP-0044@1 | V04 first affectionate kiss was on cheek | ESTABLISHED_AT_BOUNDARY as explicit Momo recollection with inset; stronger than inherited anatomy reading | EV0013; CS0035@3/RL0043@3 |
| PG-IP-0045@1 | Practice kiss was Sae's first | UNRESOLVED as exhaustive history, ESTABLISHED that she claims it to Tōji; not contradicted simply by later Jigoro contact | EV0014; no biography fabricated |
| PG-IP-0046@1 | Momo is Jigoro fan who bullies/controls Sae and steals her crushes | REFUTED_AT_BOUNDARY as staged causal account of this scheme: reader sees Sae rivalry and Momo choice to help; no fan choice shown | EV0022–0023/0030–0032; CL0003@5/0018@2; not exhaustive proof of every prior interaction |
| PG-IP-0047@1 | Sae needs help because Jigoro dumped her for Momo | REFUTED_AT_BOUNDARY; Sae previously rejected him and organized his approach, then performs emergency | EV0011/0021–0023/0030; not Momo's informed choice |
| PG-IP-0048@1 | Entrant in Tōji room is Adachi | REFUTED_AT_BOUNDARY; disguised Sae shown before approach and exposed in light | EV0033–0035/0038–0039; CL0019@1 |
| PG-IP-0049@1 | Momo freely chooses Jigoro over Tōji for birthday/intimacy | REFUTED_AT_BOUNDARY for alleged choice; her actual plan/help, attempted objection and incapacity contradict it; Sae's illustrated account is false | EV0030–0032/0037/0040–0041/0047–0048 |
| PG-IP-0050@1 | Momo becomes incapacitated after offered drink | ESTABLISHED_AT_BOUNDARY sequence; deliberate alteration strongly supported by scheme/aftermath, exact agent/administration UNRESOLVED | EV0031–0032/0037/0045; no chemical named as fact |
| PG-IP-0051@1 | Intended sexual act occurred during Momo's unconscious interval | UNRESOLVED: changed clothing, fear, plan and Jigoro assertion do not independently confirm; no inference nothing happened either | EV0041/0045/0047–0048 |
| PG-IP-0052@1 | Sae wants a manufactured fact of Momo/Jigoro intimacy regardless of waking | ESTABLISHED_AT_BOUNDARY as explicit instruction/intent; agreement prospective, not completed outcome | EV0045; CL0003@5 |

| Knowledge / prior | Subject and proposition | State / basis and scope | Evidence / time |
| --- | --- | --- | --- |
| PG-KN-0047 / — | Sae / IP0043 | KNOWS from Momo, copies code; no mysterious leak | EV0008–0010, before breakup |
| PG-KN-0048 / — | Momo / garden staging | KNOWS arrangement; produces summons and confronts Sae. Receipt route not invented | EV0019–0020, before birthday |
| PG-KN-0049 / KN0044 | Jigoro / IP0046 | BELIEVES false victim/fan account; proposes confrontation then is dissuaded; later conduct depends on account | EV0022–0023/0032, before removal |
| PG-KN-0050 / — | Momo / IP0047 | BELIEVES Sae needs urgent private help sufficiently to go; full belief in Jigoro attraction not independently established | EV0030–0031, birthday |
| PG-KN-0051 / — | Tōji / IP0048 | BELIEVES Adachi under disguise, then SUSPECTS mismatch, KNOWS false after light/name | EV0034–0035/0038–0039, birthday night |
| PG-KN-0052 / — | Jigoro / IP0050, sleep | KNOWS observable incapacity/sleep; exact chemical knowledge UNKNOWN. Directly says will not wake | EV0032/0041/0045 |
| PG-KN-0053 / — | Tōji / IP0049 | DENIES voluntary-choice account based on Momo knowledge, calls to verify, searches despite Sae insistence | EV0040–0044 |
| PG-KN-0054 / — | Tōji / danger and IP0051 | SUSPECTS something happened, knows Jigoro answers her phone/says sleeps; missing interval outcome UNKNOWN to him | EV0041–0044/0046 |
| PG-KN-0055 / — | Momo / IP0051 | SUSPECTS feared event on waking; asks; receives assertion only, no reliable resolution at cutoff | EV0047–0048 |
| PG-KN-0056 / — | Sae / IP0051 and Jigoro sleep report | KNOWS he reports not yet proceeding/continued sleep; urges regardless. This report not omniscient full account | EV0045 |
| PG-KN-0057 / — | Tōji / hotel whereabouts | BELIEVES inferred located from receptionist refusing transfer; sets out, not yet sees Momo | EV0046 |

| Transmission / prior | Sender → actual audience / formulation | Channel, knowledge/intent and reception | Evidence / timing |
| --- | --- | --- | --- |
| PG-TX-0043 / — | Honda/in-story magazine → Sae/observed peers and readers / win/feature | Announcement/publication, fan response observed/reported, not universal school reception | EV0004–0005, after proposal |
| PG-TX-0044 / — | Momo → Sae / IP0043 | Direct explanation knowingly given; Sae copies L | EV0008–0010 |
| PG-TX-0045 / — | Sae → Tōji / love, IP0045, reluctant model romance | Tearful appeal; claims attributed, capture and rivalry reader-visible; Tōji apologetic but later refuses | EV0014/0017 |
| PG-TX-0046 / — | Tōji → Sae / IP0010@2/0020@2, loves only Adachi | Retrospective self-report + new refusal; not a message to Momo or public class | EV0017 |
| PG-TX-0047 / — | Sae → Tōji / garden summons; Momo later displays summons | Written invitation; timing planned by Sae, exact route by which Momo obtained it UNKNOWN | EV0017/0019–0020 |
| PG-TX-0048 / — | Sae → Jigoro / IP0046 and night request | False victim/fan account; blocks proposed verification, emotional appeal; initial refusal distinct from later agreement | EV0022–0023/0030 |
| PG-TX-0049 / — | Sae → Momo / IP0047 | Crying phone emergency; insists only Momo, isolates her; Momo chooses help, not intimate arrangement | EV0030–0031 |
| PG-TX-0050 / — | Sae → Tōji / IP0048 implicitly | Sensory identity forgery via clothes/wig/scent/darkness, knowingly conceals self; believed until mismatch/light | EV0027/0033–0035/0038 |
| PG-TX-0051 / — | Sae → Tōji / IP0049 | False illustrated account, repeated choice story; he explicitly denies and checks | EV0040/0042 |
| PG-TX-0052 / — | Jigoro → Tōji / sleeps/her wish | Momo phone, denies access/hangs up then unreachable; true sleep and unsupported wish separated | EV0041–0042 |
| PG-TX-0053 / — | Tōji → Jigoro neighbor / fellow models unable to contact three days | Deliberate false expedient to enter apartment; neighbor accepts sufficiently to admit | EV0043 |
| PG-TX-0054 / — | Tōji/reluctant Sae → hotel staff / guest connection inquiries | Calls, scope bounded to actual search; no disclosed full scheme to all hotels. Refusal to transfer becomes location clue | EV0044/0046 |
| PG-TX-0055 / — | Sae → Jigoro / IP0052 | Private call, urges irrespective of waking; he agrees prospectively; not Momo assent | EV0045 |
| PG-TX-0056 / — | Jigoro → Momo / fulfilled wish | Direct final claim, she is stunned; truth/referent unresolved | EV0048 |

| Reputation / prior | Target / actual bounded audience | Treatment and awareness / source-truth distinction | Evidence / claim |
| --- | --- | --- | --- |
| PG-RP-0022 / RP0016 | Sae / observed school admirers, magazine audience | Adulation/followers after feature and celebrity tie, she knows; prior exposed lies do not prevent new prestige | EV0004–0007; CL0002@5; reported fan-club scope not universal |
| PG-RP-0023 / RP0014 | Kairi / girls comparing with celebrity | Verbal praise contradicted by rushing away; he notices empty room. Transient attention, not complete revised stable ranking | EV0006 |
| PG-RP-0024 / RP0017 | Momo / Jigoro | False cruel/fan account, hostile gaze/removal; she first notices enmity without cause, then harmed under scheme | EV0007/0022–0023/0032; CL0018@2; not school-wide new rumor |
| PG-RP-0025 / RP0019 | Jigoro / hotel bystanders | Celebrity recognition while checking in, no truth certification or Momo agreement | EV0036 |

| Current information/reputation @ PG-FR-V05 | Active state | Source versus participant distinction / unresolved |
| --- | --- | --- |
| V01 practice account | IP0010@2/0020@2; TX0046, CM0008@3 | Original refusal plus later self-reported acquiescence; Sae receives explanation, Momo receipt not shown |
| L and cheek | IP0043/0044, KN0047 | Sae directly knows L; cheek now verified for analyst; no backdated scene knowledge |
| Garden staging | KN0048, TX0047 | Momo knows first scheme, not automatically later plan |
| Momo/Jigoro choice | IP0046/0047/0049; KN0049/0050/0053 | Jigoro misled; Momo chooses help; Tōji rejects false voluntary-choice story; reader knows isolation/incapacity |
| Identity | IP0048, KN0051, TX0050 | Reader sees disguise before Tōji; he discovers by mismatch/light; response not informed acceptance of Sae |
| Incapacity/outcome | IP0050/0051/0052; KN0052/0054–0056 | Sleep/intent known, completed sexual act unresolved. Momo fear and Jigoro assertion not omniscient facts |
| Search | KN0057, TX0053/0054 | Tōji infers hotel, not arrived. Sae cooperates under pressure while obstructing |
| Sae / peers | RP0022 | Renewed prestige at observed reach, not universal moral rehabilitation |
| Momo / Jigoro | RP0024 | Hostile false belief acted upon, no truth correction shown |

Audit IP0018@2/0025@2/0029@2 and TX0031@2 remain active for their historical propositions, with no new exhaustive private-biography claim. Next IDs IP0053, KN0058, TX0057, RP0026. Revision history: 0.4 — V05 epistemic/transmission/reputation successor transaction, 2026-10-19 owner date.

## V06 successor transaction — PG-FR-V06

[V06 reading](../02%20Sequential%20Readings/PEACH_GIRL_V06_DEEP_READING.md) owns observations; EV means PG-EV-V06. Every row learned V06, with actual within-volume frontiers below. Evidence and audience belief differ. Earlier rows/freezes remain historical; private truths do not become whole-school reputation by inference.

| Proposition / prior | Bounded content | Current source truth / evidence |
| --- | --- | --- |
| PG-IP-0050@2 / IP0050@1 | Momo drink deliberately altered | STRONGLY_CONFIRMED: Sae explicitly admits sleeping pills before Jigoro arrives, sequence previously shown; specific compound/dose UNKNOWN. EV0031/0035; no retroactive prior participant knowledge |
| PG-IP-0051@2 / IP0051@1 | Intended sexual act occurred in missing hotel interval | Still UNRESOLVED: repeated assertions, wrapper, Momo fear and Misao explanation insufficient independent act history. EV0002/0006–0008/0028–0029/0034–0036; do not infer either completion or nonoccurrence |
| PG-IP-0053@1 | Tōji cannot face Momo because hates her as impure | REFUTED as explanation: he blames himself, denies her fault and restores love. EV0023/0025–0028; real overheard fragment not whole intended meaning |
| PG-IP-0054@1 | Tōji shame concerns own failure to protect/find earlier | ESTABLISHED as direct account after Momo leaves; no proof universal sole responsibility. EV0023 |
| PG-IP-0055@1 | Sae photographed staged hotel room | ESTABLISHED action, exact image contents/use/circulation UNKNOWN. EV0010/0013 |
| PG-IP-0056@1 | Sae knowingly invented Momo fan story | ESTABLISHED admitted lie, corroborating prior scheme. EV0035; Jigoro hears now, not in V05 |
| PG-IP-0057@1 | Pergola breakup is actual final rupture | REFUTED: explicitly scripted, relationship continues. EV0041/0044/0047–0048; classmates/Sae belief differs |
| PG-IP-0058@1 | Café confession establishes sincere Tōji love/choice of Sae | REFUTED as inference from these performed words; script and lure confirmed. EV0042–0044; not omniscient exhaustive measure of every feeling |
| PG-IP-0059@1 | Trio plans simulated punishment without actual sexual assault | ESTABLISHED as stated limit/assumed arrangement, not ensured result. EV0045/0050; their actual incapacitation/control still real |
| PG-IP-0060@1 | Intended man's being gay guarantees safety | UNSUPPORTED general inference asserted by Kairi, not analyst truth; actual identity/delivery also fails. EV0045/0050 |
| PG-IP-0061@1 | Actual receiver is intended waiting actor | REFUTED at least as successful planned receipt: intended contact still waiting says never arrived. EV0050; exact wrong-delivery mechanism UNKNOWN |
| PG-IP-0062@1 | Sae actual threatened hotel situation and outcome | ESTABLISHED waking restraint/threat by unidentified CHAR0018; completed sexual act/rescue/repentance UNRESOLVED at scream cutoff. EV0049–0050 |

| Knowledge / prior | Actual holder / proposition and frontier | Basis / limit |
| --- | --- | --- |
| PG-KN-0058 / KN0055 | Momo / IP0051: increasingly BELIEVES feared act after wrapper, still lacks memory | EV0002/0006–0008; belief not confirmed event |
| PG-KN-0059 / KN0057 | Tōji / location: KNOWS actual room/seeing Momo at41–42 after prior recheck | EV0003/0014–0016; PR0010 supported then |
| PG-KN-0060 / — | Momo / IP0053: BELIEVES rejection from partial overhearing then flees | EV0023–0025; misses IP0054, later corrected |
| PG-KN-0061 / — | Tōji, Kairi/Misao / IP0054: hear self-blame explanation after Momo departure | EV0023; Momo not recipient then |
| PG-KN-0062 / KN0060 | Momo / IP0053 and identity deception: KNOWS Tōji denies blame/hatred and reports disguised Sae contact | EV0025–0028; actual heard reassurance, missing interval still unknown |
| PG-KN-0063 / — | Misao / distress, no memory, wishes and general hurt; KNOWN from her consultation/context | EV0020/0022/0029; later drug-admission receipt not shown |
| PG-KN-0064 / KN0049,KN0052 | Jigoro / IP0056,IP0050@2: first SUSPECTS mismatch32, then KNOWS Sae admits fan lie/drugs113–114 | EV0011/0034–0035; not retroactive ignorance of observable sleep |
| PG-KN-0065 / — | Momo/Tōji/Kairi / IP0056,IP0050@2: OVERHEAR direct self-incriminating account113–115 | EV0035; hypothesized plan102 not equally confirmed in every part |
| PG-KN-0066 / — | Momo/Tōji/Kairi / IP0057–0059: KNOW script/plan, explicit to reader146 | EV0039/0044–0045; reader initially less certain than performers |
| PG-KN-0067 / — | Sae / IP0057–0058: BELIEVES breakup and confession sufficiently to rejoice/pursue intimacy | EV0041–0043; no proof she hears trio private plan |
| PG-KN-0068 / — | Trio / IP0059–0061: ASSUMES intended actor safe delivery, Momo checks/no real assault | EV0045/0047; Kairi assurance not omniscient safety |
| PG-KN-0069 / KN0067 | Sae / IP0062: KNOWS wakes restrained to unfamiliar man, no longer expected Tōji | EV0049; full trio responsibility/actual identity knowledge UNKNOWN |
| PG-KN-0070 / KN0068 | Trio / IP0061: KNOWS intended contact reports still waiting, visibly shocked165 | EV0050; no completed rescue, identity or harm knowledge yet |

| Transmission / prior | Sender → actual recipient / channel and content | Intent, reception and source truth / evidence |
| --- | --- | --- |
| PG-TX-0057 / TX0054 | Tōji → Sae / rechecked location in her assigned portion | Exposes withholding; she then spray/abandons, not shared sincere rescue. EV0003–0004 |
| PG-TX-0058 / TX0056 | Jigoro → Momo / claims initiative/awake and wrapper proof | She challenges then fears; assertion/object not full event confirmation. EV0002/0006–0008 |
| PG-TX-0059 / — | Misao → receptionist / false parent-contact pretext as teacher | Gains705; actual family call not yet. EV0014 |
| PG-TX-0060 / TX0051 | Sae → Momo privately / she chose Jigoro, betrayed Tōji | False blame in bathroom, no independent voluntary choice. EV0018 |
| PG-TX-0061 / — | Sae → Jigoro before rescue group / rejects for hurting best friend | Public self-exoneration opposite own recruitment; he protests, no full correction delivered. EV0019 |
| PG-TX-0062 / — | Misao ↔ Momo / options, wishes, no-memory discussion | Momo requests nondisclosure/solitude, respected locally. EV0020; advice not forensic finding |
| PG-TX-0063 / — | Misao → Momo household then Kairi/Tōji report / staying overnight | Actual notification reported at62; not full scheme disclosure proven. EV0022 |
| PG-TX-0064 / — | Tōji → Kairi/Misao; Momo only initial fragment / cannot face then self-blame | Momo leaves before explanation, false rejection inference. EV0023; asymmetrical access not lie |
| PG-TX-0065 / — | Tōji ↔ Momo / identity-deception disclosure/no-fault reassurance | Reciprocal comfort and continued affection, not offset guilt confession of mutual chosen betrayal. EV0028 |
| PG-TX-0066 / — | Misao → Kairi / secondary hurt/self-blame account | General attributed explanation, no independent unshown act proof. EV0029 |
| PG-TX-0067 / — | Kairi → trio / scheme reconstruction, later revenge rationale | i102 hypothesis precedes admission, i123–124 punitive lesson claim unproven. EV0032/0038–0039 |
| PG-TX-0068 / — | Sae → Jigoro, overheard trio / fan lie, sleeping pills, envy | Direct admission; actual recipient/overhear time preserved. EV0035–0036 |
| PG-TX-0069 / — | Kairi → studio staff / false Honda invitation with card | Access gained under pretext, not actual recorded invitation. EV0033 |
| PG-TX-0070 / — | Tōji → Momo staged breakup, then Sae staged love / Sae watches first scene | Intentional false narrative to lure; Sae believes, couple truly hurt. EV0041–0044/0047 |
| PG-TX-0071 / — | Intended contact → Kairi, trio observes / incoming call girl has not arrived | Contradicts assumed receiver, shock; later response unknown. EV0050 |

| Reputation / prior | Target / actual audience / treatment | Truth and scope / evidence |
| --- | --- | --- |
| PG-RP-0026 / RP0024 | Momo / Sae private blame, Jigoro and rescue group | False voluntary-choice blame persists in speech; Jigoro later learns fan/drug truth, group rejects her fault. Not school rumor. EV0018–0020/0028/0035 |
| PG-RP-0027 / RP0022 | Sae / shoot staff versus overhearing trio/Jigoro | Public angel image/gifts admired, private admissions discredit to bounded listeners; no whole-school downfall now established. EV0032/0034–0036 |
| PG-RP-0028 / — | Momo/Tōji couple / observing classmates and Sae | Classmates suspect quarrel/no talk; Sae takes apparent breakup as real. Script privately known, no universal announcement. EV0041–0044 |

Current information frontier: IP0050@2 admission strong, IP0051@2 missing act unresolved; Momo learns no-fault position then later causal truth, not one omniscient instant. Trio knows failed actor receipt, Sae knows immediate threat; neither side's whole knowledge merged. Photos acquired but no actual use/circulation known. Prior audit qualifiers and false-sexual-biography limits remain. Next IP0063, KN0071, TX0072, RP0029. Revision history0.5 — V06 state/knowledge/transmission/reputation successor transaction, owner date2026-10-19.

## V07 successor transaction — PG-FR-V07

[V07 reading](../02%20Sequential%20Readings/PEACH_GIRL_V07_DEEP_READING.md) owns EV=PG-EV-V07 observations. Every row learned V07 at stated within-volume frontier; all prior versions remain historical. Truth status, speaker certainty and actual recipient knowledge remain distinct. HIGH direct action/utterance support; unknown reach explicitly limited.

| Proposition / prior | Bounded content | Current source truth / evidence |
| --- | --- | --- |
| PG-IP-0051@3 / IP0051@2 | Momo missing hotel interval sexual-act outcome | MAINLINE_UNRESOLVED, with separately recorded EDITORIAL_RECAP_ASSERTS_LOSS at7 and profilequestion. No new independent mainline account; coercion/drugging/removal/hurt already established. EV0002/0016/0025–0026; CL0003@7, no nonoccurrence inference |
| PG-IP-0055@2 / IP0055@1 | Sae photographs staged hotel room | ESTABLISHED content now actual prints Momo blanket/Jigoro robe70; used blackmail/placement strongly attributed by present claim. EV0018/0023–0024. Still not act proof or established press publication |
| PG-IP-0061@2 / IP0061@1 | Actual receiver equals intended actor | REFUTED planned match, mechanism now explicit misheard307→301; Kairi admits error. EV0002/0012. Contact claimed role/biography not independently vetted |
| PG-IP-0062@2 / IP0062@1 | Sae threatened hotel situation/outcome | ESTABLISHED attempted resistance/caught, Momo/trio reaches and defeats immediate threat, Sae distressed exits; no accepted lesson or complete unshown act history. EV0004–0014 |
| PG-IP-0063@1 | Kairi misheard actor room number and delivered wrong | ESTABLISHED explanation/ownership7–10/53, matches failed receipt. EV0002/0012; no retroactive safe actor conduct |
| PG-IP-0064@1 | Revenge produced Sae repentance/reform | REFUTED achieved-reform inference by immediate destructive vow and renewed blackmail. EV0009/0011/0014/0017–0018; future change not ruled out |
| PG-IP-0065@1 | Sae conditions image nondistribution on breakup/date | ESTABLISHED direct demand/refusal/renewal and wheel/bargain sequence. EV0017–0019/0028/0033–0041; exact later inventory unknown |
| PG-IP-0066@1 | Hotel-image scandal actually disseminated to school/media | NOT_ESTABLISHED: bounded park spill/attention actual, threatened press distribution unshown; school coupling rumor actual but distinct. EV0023–0024/0030/0032/0043–0046 |
| PG-IP-0067@1 | Tōji freely prefers Sae over Momo now | STRONGLY_CONTRADICTED by explicit refusal and coercive sequence; public words/kiss real but insufficient for claimed cause. EV0017–0019/0038–0041/0044/0051–0054; CL0023@1 |
| PG-IP-0068@1 | Wheel breakup actual unilateral declaration | ESTABLISHED132 and repeated137/171; Momo unaware condition, no shared script/acceptance. EV0036/0038/0053. Actual utterance distinct from authentic changed feeling |
| PG-IP-0069@1 | Genuine negatives/whole photo inventory destroyed139–141 | REFUTED as warranted conclusion: Sae says delivered fake144/retains genuine until satisfied146. EV0039–0041. Burn real, original identity/exhaustive inventory not independently verified |
| PG-IP-0070@1 | Momo correctly infers core photograph blackmail169 | ESTABLISHED accusation matches reader-known coercive cause; she says school threat, not demonstrated press deadline/fake originals knowledge. EV0052; no confession confirmation received |
| PG-IP-0071@1 | Momo helped Sae only from guilt/hypocrisy | UNSUPPORTED_EXCLUSIVE_MOTIVE asserted by Sae111; Momo expressed empathy/support contrast/continued anger and actual risk23–42 counter reduction. EV0005–0008/0028; no omniscient pure-motive claim either |

| Knowledge / prior | Holder × proposition / actual frontier | Acquisition, status and limit |
| --- | --- | --- |
| PG-KN-0071 / KN0070 | Trio / IP0063 knows room-error account7–10, later Kairi owns | EV0002/0012; immediate receiver threat known to reader/Sae, not full details shared automatically |
| PG-KN-0072 / KN0069 | Sae / carrier identity suspects Tōji15 from young boy description | EV0004; false inference, actual Kairi carrier; not omniscient fact |
| PG-KN-0073 / KN0072 | Sae / sees Momo rescue31–42 and hears boundary46–48, later Kairi admits error53 | EV0007–0012; actual aid received does not mean accepts motives/reforms |
| PG-KN-0074 / NONE | Tōji / IP0065 knows demand/photos70–72/deadline, refuses then conceals from Momo | EV0017–0022/0028; reader access not shared with Momo |
| PG-KN-0075 / NONE | Momo / photos from basket86, fears meaning/circulation and recognizes Sae connection103–104 | EV0023–0026; at this stage not shown knowing breakup/date condition |
| PG-KN-0076 / NONE | Tōji / actual Momo voicemail request received161 | EV0047; earlier unanswered calls not proof he never received; deliberately hides next |
| PG-KN-0077 / NONE | Sae / hears wheel call, Momo voice129 and breakup132, treats condition performed | EV0033–0040; Momo unaware listener, no invented spoken preagreement |
| PG-KN-0078 / KN0074 | Tōji / IP0069 learns Sae claims fake144 after burning | EV0039–0041; provisional apparent recovery defeated, genuine inventory still unverifiable |
| PG-KN-0079 / KN0075 | Momo / knows actual breakup declaration132, later learns public Sae/Tōji claim from Kairi156, still disbelieves genuine motive | EV0036/0038/0042/0045–0046; denial not absence of heard declaration |
| PG-KN-0080 / NONE | Kairi / sees arm-linked arrival and hears class coupling rumor154–157 | EV0045; firsthand display not direct preference/bargain evidence |
| PG-KN-0081 / KN0079 | Momo / IP0070 SUSPECTS/accurately infers blackmail169, asks confirmation, receives denial/display instead | EV0050–0054; source truth accurate core, epistemic status inference not complete received fact |
| PG-KN-0082 / KN0080 | Kairi / hears Momo photo-blackmail accusation169 and sees final kiss | EV0052–0054; no independently demonstrated full press/negative bargain knowledge, exact belief UNKNOWN |

| Transmission / prior | Sender → actual recipient / channel and content | Intent, reception, time and limit |
| --- | --- | --- |
| PG-TX-0072 / TX0071 | Intended actor ↔ Kairi, trio present / room307 versus delivered301 account7–10 | Actual correction of assumed match; planned harmless role still reported. EV0002 |
| PG-TX-0073 / NONE | Momo → Sae, Tōji present / unforgiven but no further engagement, goodbye46–48 | Deliberate boundary, Momo relief; Sae later intrusive/destructive not acceptance. EV0010/0013–0014 |
| PG-TX-0074 / NONE | Kairi → Sae privately / happiness jointly built, own mistake53/blame him not Momo54 | Direct responsibility plus Momo protection, not full accurate absolution of her earlier choice. EV0011–0012 |
| PG-TX-0075 / NONE | Sae → Tōji privately / photo copies/press ultimatum65–74 | Knows manufacture, deliberate leverage; he refuses, Momo not recipient. EV0017–0019 |
| PG-TX-0076 / NONE | Momo → Tōji / speak/share so solve together85 | Actual collaboration request, condition still withheld. EV0022 |
| PG-TX-0077 / NONE | Sae → Tōji / basket present claim89, taunts crying, press travel93 | Strong self-attribution of covert placement; not depicted insertion. Momo nearby knows distress but exact receipt of condition absent. EV0024 |
| PG-TX-0078 / NONE | Tōji → Momo / no blame, holds requested hand, promises protect/prevent spread | Real local support, not completed future control. EV0025–0027 |
| PG-TX-0079 / NONE | Tōji ↔ Sae / actual108call retrieve originals, rescue appeal; renewed demand/mock rescue motive | No agreement then, friend account his rhetoric, hypocrisy hers. EV0028 |
| PG-TX-0080 / NONE | Tōji → Sae secretly via open phone125–132 / Momo voice and breakup audible | Deliberately connects; Momo unknown-listener, Sae receives. No fabricated spoken bargain. EV0033–0036 |
| PG-TX-0081 / NONE | Tōji → Momo, Sae overhears / breakup132 and to Momo everything unwanted137 | Actual withdrawal, changed-feeling reason contextually misleading; Momo shocked not agreed. EV0036/0038 |
| PG-TX-0082 / NONE | Sae → Tōji / burned negatives fake144, eventual originals when satisfied146 | Retains threat, he grabs/demands then releases. Independent inventory not certified. EV0041 |
| PG-TX-0083 / NONE | Sae → classmates/Tōji / public dating/preference claim153/168 | Coupling believed/contested, explicit earlier refusal withheld. Kairi sees display then informs Momo156. EV0044–0045/0051 |
| PG-TX-0084 / NONE | Momo → Sae/Tōji/Kairi / blackmail accusation169; Tōji denies/claims demonstrates real reason via kiss171–174 | Accurate core inference not verbally confirmed; staged message contradicts actual coercive cause. EV0052–0054 |

| Reputation / prior | Target / actual audience / response | Truth and reach |
| --- | --- | --- |
| PG-RP-0029 / RP0027 | Sae / rescue trio and herself / lesson claim contested, blame and renewed hostility | EV0009–0014; no public reform/vindication, no whole-school knowledge of revenge scene |
| PG-RP-0030 / RP0026 | Momo / bounded park bystanders / prints fall, people notice and hand picks print88 | EV0023; exact belief/further transmission unknown, not established mass hotel scandal |
| PG-RP-0031 / RP0028 | Momo/Tōji/Sae / observed classmates and Kairi / arm-linked arrival interpreted dating/betrayal, girls challenge hurt to Momo, Sae affirms, Momo later denies breakup | EV0043–0046; actual contested school coupling narrative, whole-school reach attributed to Kairi; not proof willing new affection or hotel-image publication |
| PG-RP-0032 / NONE | Jigoro/Sae / actual class discussants / drama interview loved-but-unloved allusion prompts inference Sae dumped model | EV0043; actual reported media allusion, inferred referent not explicit identified hotel disclosure |

Exit epistemic asymmetry: reader knows pressure; Tōji/Sae know bargain/call/fake claim; Momo accurately suspects core coercion169 but denied confirmation; Kairi hears allegation then kiss, full belief/negative knowledge unknown. School knows disputed coupling, not thereby hotel truth. IP0051@3 retains recap/mainline distinction. Next IP0072, KN0083, TX0085, RP0033. Revision history0.6 — V07 bounded successor state, closure owner date2026-10-20.

## V08 successor transaction — PG-FR-V08

[V08 reading](../02%20Sequential%20Readings/PEACH_GIRL_V08_DEEP_READING.md), EV=PG-EV-V08. All learned at stated V08 source frontier, not at earlier-volume freeze. HIGH direct acts/utterances, incomplete belief/reach identified. Reader, character knowledge and truth distinct.

| Proposition / prior | Bounded content | Source truth / limit |
| --- | --- | --- |
| PG-IP-0072@1 | Tōji gives Misao protective photo/media reason41–44 | ESTABLISHED_SELF_REPORT with strong independently known V07 coercive context. His imagined lifelong label not actual publication/unique possible response; EV0012 |
| PG-IP-0073@1 | Returned photos28 are birthday/couple history; scent breaks29–30 | ESTABLISHED_OBJECTS/CONTACT, birthday prints not blackmail images. Handslip attributed Tōji, deliberately cruel staging STRONGLY_SUPPORTED_INFERENCE, not explicit confession; EV0008 |
| PG-IP-0074@1 | Sae never threatened media, as denies58 | REFUTED by direct V07 ultimatum; EV0016 actual denial and proof challenge. Misao institutional proof/negative retrieval distinct, no false-balance truth reset |
| PG-IP-0075@1 | Momo healed/stopped loving Tōji because ended85/three months94 | REFUTED_AS_COMPLETE_ACCOUNT by explicit still-love123/154 and desk142; actual end acknowledgement/joy real. EV0023/0025/0033/0038/0041 |
| PG-IP-0076@1 | Momo presently has settled reciprocal Kairi romance | NOT_ESTABLISHED: particular affect80, current friend98, kiss ambiguity132/dog136, later more-than-friend-but-unsure155/continuedTlove154, later kisses168. EV0022/0026/0035–0036/0041–0046; no explicit dating pact |
| PG-IP-0077@1 | Identity/intent behind burn-causing push102/107 | UNRESOLVED: Momo felt push, notes Sae seated, no independent act/actor depicted. EV0027–0028; later proven sign cannot settle separate push |
| PG-IP-0078@1 | Fan claim Momo left with Ogawa/girls113 | FALSE_LOCATION_REPORT to Kairi, knowingly diversionary in sequence; actual friends contradict117–118. EV0030/0032; not friends' earlier unverified benevolent assumption |
| PG-IP-0079@1 | Sae turned foothills sign to misdirect Momo | ESTABLISHED depicted114–115 reveal, EV0031. Actor unknown at114, reader shown115, Momo/Kairi not thereby informed |
| PG-IP-0080@1 | Fan trio and Sae coordinated disappearance | NOT_ESTABLISHED despite distinct malicious acts contributing. EV0029–0032; preserve separate responsibility without invented alliance |
| PG-IP-0081@1 | Older brother funded/authorized shopping | KAIRI_REPORT74, EV0021; card shown, permission/income/name not independently verified, no fraud established |
| PG-IP-0082@1 | Seed grew to flowering peach tree in one week | REFUTED_LITERAL_MIRACLE: Kairi claim162, Momo identifies quince164, he reports neighbor gift; EV0044. Warmth/metaphor need not be fake because literal premise fails |

| Knowledge / prior | Holder × proposition / acquisition frontier | Actual status / limit |
| --- | --- | --- |
| PG-KN-0083 / KN0081 | Momo / photo-coercion cause still believes18/20, offers joint facing24 despite rejection | EV0004–0006; accurate core inference retained, not given press deadline/fake-negative details or new honest Tōji confirmation |
| PG-KN-0084 / NONE | Misao / IP0072 receives Tōji direct account41–44 after treats38 | EV0011–0012; learns source-specific ultimatum/affection reasoning, not all staff/class automatically know |
| PG-KN-0085 / KN0083 | Momo / knows actual phone by package50 and finds no Tōji visit54; later visitor Kairi83, acknowledges ended85 | EV0014–0015/0023; memory53 distinct present arrival. Ended not knows affection zero |
| PG-KN-0086 / NONE | Sae / Misao heard Tōji ultimatum story58 and questions; later rebukes him61 | EV0016–0017; denial deliberately contradicts prior act, home visit only reported; no allclass transmission |
| PG-KN-0087 / KN0082 | Kairi / explicitly says70 not Tōji/do not know reason | EV0020; Momo's earlier allegation did not give verified complete account. Later concern/rescue not automatic cure to ignorance |
| PG-KN-0088 / KN0085 | Momo / burn cause felt pushed107 but Sae sitting | EV0028, IP0077; SUSPECTED/UNRESOLVED not direct actor knowledge, no retroactive inference from sign reveal |
| PG-KN-0089 / NONE | Kairi / fan location report113 contradicted by actual Ogawa/girls117–118 | EV0030/0032; discovers missing Momo/false account and challenges fans, not shown learns Sae sign role |
| PG-KN-0090 / KN0088 | Momo / own still-Tlove123, Kairi kiss/care128–132, uncertainty/dog contrast133–136, desk141–142, direct own-account154–155 | EV0033–0042; particular internal access not narrator definitive diagnosis. Did not witness sign115 |
| PG-KN-0091 / KN0089 | Kairi / finds Momo124 sees injury, hears uncertain-more-than-friend/stillToji154–155 | EV0034–0035/0041–0042; direct disclosure now, not merely assumes grateful reciprocity from rescue/kiss |
| PG-KN-0092 / KN0091 | Kairi / Momo thanks willingness stay164 but rebuffs surprise quick kiss166 | EV0044–0045; proximity accepted, reaction specific, not blanket future permission |
| PG-KN-0093 / KN0091 | Kairi and Momo separately / flowering tree from neighbor claimed162–164, she identifies quince not peach | EV0044; his literal miracle corrected, no reliable new botanical expertise or magical growth |
| PG-KN-0094 / NONE | Reader / sees Sae sign actor115, later Momo uncertainty/direct speech154–155, separate Kairi self-declaration167/finalkiss168 | EV0031/0041–0042/0046; no unshown spy130, caption not securely Momo spoken confession; differentiated access retained |

| Transmission / prior | Sender → actual recipient / content/channel | Reception, intent and limit |
| --- | --- | --- |
| PG-TX-0085 / TX0083 | Sae → Momo/Kairi/class context10 / says initially refused but passionate Tōji insisted | EV0002; misleading preference account, prior refusal/pressure reader-known, no full truth received |
| PG-TX-0086 / TX0076 | Momo → Tōji / read-me note13, discarded14; shared problem-facing request24, door closed | EV0003/0006–0009; note content not depicted read, explicit request unmet |
| PG-TX-0087 / NONE | Sae → Momo20–21 / violent-retrieval counterfactual/no love/stalker framing | EV0005; manipulation, not narrator proof only strategy, Momo still belief retained |
| PG-TX-0088 / NONE | Kairi → Tōji35–36 / Momo sick after his snow-door refusal, confrontation/punch | EV0010; actual support action for original PR0012, not successful truth reception or full quiet counsel |
| PG-TX-0089 / NONE | Tōji → Misao41–44 / photo/media ultimatum and anticipated lasting label, only protective path thought | EV0012; actual trusted-adult recipient, hypothetical tabloid not actual event, Momo excluded |
| PG-TX-0090 / NONE | Misao → Sae56–60 / asks negatives, Tōji feelings/account, challenges fake cry; Sae denies/asks proof | EV0016; false denial against V07 direct evidence, no demonstrated handover |
| PG-TX-0091 / NONE | Sae → Tōji61–62 / complains teacher visits/telling, asserts property/grips chin | EV0017; hears consequences, actual visit offpanel report, no consensual reciprocal declaration |
| PG-TX-0092 / NONE | Kako/Ogawa → Momo home voicemail63 / concern one-week school absence | EV0018; actual limited message, not recipient full bargain knowledge |
| PG-TX-0093 / NONE | Kairi → Momo70/74 / admits not know Tōji reason, reports older brother extra income/spending permission | EV0020–0021; epistemic honesty on first, independent financing verification absent on second |
| PG-TX-0094 / NONE | Momo → Kairi69/78 / kiss refusal and gift-repayment intention | EV0019/0022; no kiss69, free gift refused, repayment not shown; respective terms not generic rejection of all help |
| PG-TX-0095 / NONE | Momo → classmates98 / Kairi is friend, not already dating | EV0026; current public category not final interior truth/earlier-pull correction |
| PG-TX-0096 / NONE | Fans → Momo111 / accuse using after rejection; fans → Kairi113 / false left-with-girls location | EV0029–0030; accusation prompts conditional self-doubt, actual lie diverts; separate from friends' assumption and Sae sign |
| PG-TX-0097 / NONE | Kairi → Momo126–132 / apology for fear-alone, embrace, kiss, direct affection; piggyback return | EV0034–0035; actual desire/care, Momo uncertainty not verbal dating acceptance |
| PG-TX-0098 / NONE | Momo → Kairi154–155 / still loves Tōji, more-than-friend importance/unsure love versus comfort | EV0041–0042; direct truthful uncertainty received, not simple no-feeling/friend-only or settled romantic confession |
| PG-TX-0099 / NONE | Kairi → Momo156–168 / rely/use okay, support metaphor, stay evenifTlove, flowering-plant claim corrected164, captive flower-language declaration167 | EV0042–0046; acceptance then contact includes surprise166/rebuff and final168 kiss, no automatic consent from speech. Repeated ending caption speaker uncertain |

| Reputation / prior | Target / actual audience / response | Truth, reach and boundary |
| --- | --- | --- |
| PG-RP-0033 / RP0031 | Sae/Tōji/Momo / observed classmates11/16 / criticize Sae clinging/replacement and Momo hurt, Sae claims preference | EV0002–0004; disputed coupling actual, not receipt of hotel photos/full protective cause |
| PG-RP-0034 / NONE | Momo/Kairi / outing peers98/110 / ask dating because smiles/closeness, Momo says friend, peers note hypercheerfulness | EV0026/0029; inference not actual couple pact or complete recovery proof |
| PG-RP-0035 / NONE | Momo / fan trio111 and her own response113 / labeled user of Kairi after prior rejection | EV0029–0030; allegation partly invokes actual history but exclusive motive not proved. No wholeclass adoption or Sae coordination established |
| PG-RP-0036 / NONE | Sae/Tōji / local peer99 / Sae calls besotted, peer sees servant-like obedience | EV0026; competing public readings of actual service, no freely reciprocal affection established |

No new IP0051 missing-act resolution, verified negative recovery or hotel-image media publication. No hidden observer130 or omniscient group knowledge. Next IP0083, KN0095, TX0100, RP0037. Revision0.7 — V08 successor2026-10-20, all old proposition/version/knowledge/transmission/reputation rows preserved.

## V09 successor transaction — PG-FR-V09

[V09 reading](../02%20Sequential%20Readings/PEACH_GIRL_V09_DEEP_READING.md), EV=PG-EV-V09. Acquisition times below are V09 occurrence frontiers; past-story reports distinct from current verification. Reader access not automatically character knowledge, image resemblance not unique identity, speech not narrator truth. No raw source dialogue archive.

| Proposition / prior | Content / class / truth at exit | Evidence and limit |
| --- | --- | --- |
| PG-IP-0083@1 / IP0076 related | Current Momo/Kairi dating public recognition9 and Momo two-month report151 / ESTABLISHED current category, attributed duration | EV0002/0033; no retroactive V08 explicit pact or settled affection at every prior moment |
| PG-IP-0084@1 / NONE | Garden invitation falsely signed Tōji draws Momo; Sae/fans waiting know lure12–14 / STRONGLY_SUPPORTED coordinated present deception | EV0003; actual author/inserter not shown, older note/graffiti authors not thereby solved |
| PG-IP-0085@1 / IP0072 | Misao retains Tōji confidence under remembered do-not-tell request17 and privately sides with him20 / ESTABLISHED choice/statements | EV0004–0005; Momo still not given full protective account, no classroom/general staff receipt |
| PG-IP-0086@1 / IP0011 | Kairi drowning/heart-stop/no-memory report24, death-intent27 then joke retraction29; CPR still disputed / ATTRIBUTED + UNRESOLVED past intent | EV0007; neither confirmed attempt nor certain fabrication; Momo water-fear label not diagnosis |
| PG-IP-0087@1 / NONE | Fan no-approach pledge, restraint/lighter hair singe31–37 and Kairi intervention / ESTABLISHED actual acts | EV0009–0010; slur not biography, no Sae lighter instruction established |
| PG-IP-0088@1 / NONE | Misao/brother university friends and former middle-school tutor history, comparison/rebellion report, age25/games work / ATTRIBUTED historical biography | EV0016–0017; no independent exhaustive proof or present habits/clinical model; brother actual calls separately verified |
| PG-IP-0089@1 / NONE | Brother calls Kairi71 to relay changed8pm OB party; no relay/3h wait reported103; he claims forgot / ESTABLISHED call/omission report, disputed complete motive | EV0017/0023–0024; Momo only receives content108, no proved brother/Misao encounter outcome |
| PG-IP-0090@1 / NONE | Kairi restrains/advances after repeated refusal, Misao stops; threat89 and apology91 / ESTABLISHED current conduct | EV0018/0020; no consent or completed intercourse; teacher-retention motive strongly supported hypothesis, not admission |
| PG-IP-0091@1 / NONE | Old worn photo in student handbook83–87; cross suggests Misao, Kairi141 explicitly expects Misao question / ESTABLISHED photo, STRONGLY_SUPPORTED identity Misao | EV0019/0030; no prior sexual act depicted; Morika necklace not unique identity proof |
| PG-IP-0092@1 / NONE | Momo lies did not inspect94, Kairi relieved;116 realizes did / ESTABLISHED temporary false denial | EV0021/0025; Misao not shown told photo or his guarded reaction, no permanent reader-only knowledge |
| PG-IP-0093@1 / NONE | Kairi watches Misao wait, missed message plus personality resemblance prompts Momo substitution/advance-purpose inference112 / ESTABLISHED observations + PLAUSIBLE_COMPETING_INTERPRETATION | EV0022–0024; resemblance not looks, exclusive every-kindness-fake cause unproved |
| PG-IP-0094@1 / NONE | Kairi disposes actual photo/calls past/reassures117; Momo rejects kiss as feelingless119–121 / ESTABLISHED gestures/speech, UNRESOLVED exhaustive feeling | EV0025–0026; material disposal not affection deletion, Momo subjective reading not perfect detector |
| PG-IP-0095@1 / NONE | Morika former girlfriend, dumped3years ago by her report, matching brother-gift cross137; Kairi reports brother took her144 / ATTRIBUTED + corroborated former relationship | EV0027–0030; precise all-motive chronology/mark act not independently verified, shared gift weakens unique necklace identity |
| PG-IP-0096@1 / NONE | Kairi141 expects Misao/photo, Momo means Morika; his144 account addresses latter, she trusts146 / ESTABLISHED asymmetric exchange, incomplete correction | EV0030–0031; no transmitted explicit photo correction, present Misao attachment unanswered despite Morika reassurance |
| PG-IP-0097@1 / NONE | Morika claims navel-side gourd mark/burn cause150; Momo not seen/reports2months151, probably-valued152 / ATTRIBUTED claim and insecurity | EV0033; not direct past injury/sex proof, no clinical/color hierarchy endorsement |
| PG-IP-0098@1 / NONE | Momo secretly completes case155; overhears actual tomorrow507 invitation/assent162 and sees commercial gift164, throws own gift/runs166 / ESTABLISHED current acts, future outcome UNKNOWN | EV0035–0038; no actual hotel attendance/sex, no prior Kairi knowledge of secret craft or completed breakup |

| Knowledge state / holder / prior | Actual acquisition/change | Source and limit |
| --- | --- | --- |
| PG-KN-0095 / Momo / KN0090 | Reads Tōji-signed note11, sees Sae/fans12 discovers lure; owns still-response14 | EV0003–0004; not independent note authorship/old pool explanation |
| PG-KN-0096 / Misao / KN0086 | Already knows Tōji account,17 recalls absolute confidence request/withholds,18 doubts rightness/20 sides Tōji | EV0004–0005; Momo not automatically receives because nurse knows |
| PG-KN-0097 / Kairi / KN0093 | Hears Momo note-lure apology21, later own liking37/want know43 | EV0006/0009–0011; no omniscient complete Tōji attachment change |
| PG-KN-0098 / Momo / KN0095 | Hears drowning-intent then retraction24–29, acknowledges little knowledge30 | EV0007–0008; original intent still unresolved/CPR not settled |
| PG-KN-0099 / Momo / KN0098 | Learns Misao tutor/brother/gift/history62–68 and25/game report74–75 | EV0016–0017; source-attributed, not firsthand past-life model |
| PG-KN-0100 / Kairi / NONE | Receives actual brother8pm message71 before approach/teacher steps75 | EV0017; not Momo/Misao receipt then |
| PG-KN-0101 / Momo / KN0099 | Experiences force/fear76–83, sees actual photo83–87/infers Misao, conceals inspection94 | EV0018–0021; imagination95 not additional historical knowledge |
| PG-KN-0102 / Misao / KN0096 | Sees coercive advance80/hears refusals, scolds outside88/hears repeat-threat89, prompts apology91 | EV0018–0020; no shown photo knowledge/Momo complete forgiveness or actual future phobia |
| PG-KN-0103 / Kairi / KN0097 |94 falsely reassured Momo did not look;116 infers she did after question, disposes photo | EV0021/0025; temporary mistaken belief then correction, no proof every private Momo inference known |
| PG-KN-0104 / Momo / KN0101 | Watches Kairi watching98–101, hears full missed-message history108 then infers prevented meeting/advance-purpose112 | EV0022–0024; causal inference not earlier omniscience or confessed total motive |
| PG-KN-0105 / Momo / KN0104 | New necklace/ex claim125–127 redirects photo guess to Morika, hears partial brother/Morika account144, trusts146 | EV0027/0030–0031; her new identity belief contradicted by Kairi Misao expectation141, not securely corrected to her |
| PG-KN-0106 / Kairi / KN0103 | Knows photo question about Misao as141 expectation, hears Momo Morika jealousy, gives Morika explanation143–144 | EV0030; reader sees mismatch, his actual exhaustive feeling still unknown |
| PG-KN-0107 / Morika / NONE | Sees Momo jealous, asks dating138/no direct answer; hears skin/body exchange and Kairi public refusal/hand-taking153–154 | EV0028–0029/0033–0034; no proved photo/craft/Misao knowledge or accepted exclusivity |
| PG-KN-0108 / Momo / KN0105 | Brother self-introduces157 after similar-voice mistake, says Kairi bookshop/left5min before158 | EV0035; name/face not yet known, friendly voice not full moral biography |
| PG-KN-0109 / Momo / KN0108 | Secretly hears proposed tomorrow507/actual assent161–162, sees commercial gift pleasure164, reveals anger165 | EV0036–0038; no hidden full explanation or visited hotel knowledge |
| PG-KN-0110 / Kairi / KN0106 | Sees Momo suddenly present165 after private conversation/gift; calls her166 | EV0038; source not establish knew she watched before, nor that he opened/identified handmade gift by exit |

| Transmission / prior | Sender → actual recipient / event | Truth/reach/qualification |
| --- | --- | --- |
| PG-TX-0100 / NONE | False Tōji-signed note → Momo10–11; Sae/fan arrival reveals lure12 | EV0003; forged invitation strong, actual writing/insertion unshown, not older note authors |
| PG-TX-0101 / NONE | Sae → fan trio report13 Momo still likes Tōji; gathered pressure heard by Momo/Misao interruption14 | EV0003; bounded present coordination, no later burn instruction or broad diffusion proved |
| PG-TX-0102 / NONE | Momo → Kairi21 admits note lure/response to Tōji name | EV0006; direct honest admission, not full affection-category resolution |
| PG-TX-0103 / NONE | Kairi → Momo24–29 drowning details/death-intent then joke retraction | EV0007; attributed inconsistent account, no independently verified past intent |
| PG-TX-0104 / NONE | Misao → Momo62–68 tutor/brother/gift/attachment history | EV0016; favorable portrait and old habits source-attributed |
| PG-TX-0105 / NONE | Brother → Kairi71 changed8pm message for Misao | EV0017; actual recipient Kairi, relay not made; no automatic Momo/Misao receipt |
| PG-TX-0106 / NONE | Momo → Kairi76–79 repeated refusal/fear, Misao actual interruption80 | EV0018; refusal directly received/overridden, no permission from prior kissing |
| PG-TX-0107 / NONE | Kairi → Misao89 threat may attack Momo again if she leaves | EV0020; Momo inside not shown hears, leverage after actual coercion despite comic tone |
| PG-TX-0108 / NONE | Kairi → Momo91 prompted apology/promise not ignore feeling; Misao present/report recurrence request | EV0020; commitment actual, reform/complete forgiveness not verified |
| PG-TX-0109 / NONE | Momo → Kairi94 false denial inspected handbook | EV0021; he relieved until116 inference corrects; Misao not given photo disclosure |
| PG-TX-0110 / NONE | Misao → Momo108 missed8pm-message history,110–111 necklace removal reason | EV0024; new recipient frontier supports later inference, not early knowledge |
| PG-TX-0111 / NONE | Kairi → local peers104 misleading firmly-joined innuendo; Momo immediately calls lie | EV0023; actual event interrupted advance, no completed intimacy/wholeclass belief proved |
| PG-TX-0112 / NONE | Momo → Kairi114–121 truth demand/Misao-substitution accusation, kiss rejected119 | EV0025–0026; her causal allegation not independently exhaustive truth |
| PG-TX-0113 / NONE | Kairi → Momo116–118 photo past/disposal/current-Momo reassurance/kiss | EV0025; answer insufficient to her119–121, no feeling erased by object disposal |
| PG-TX-0114 / NONE | Morika → Kairi/Momo126 ex-girlfriend claim; further135 regret to Kairi | EV0027–0029; former relation corroborated later144, detailed past acts not separately verified |
| PG-TX-0115 / NONE | Kairi → Momo141–144 Misao expectation then Morika/brother-resentment reassurance | EV0030; photo-question mismatch not plainly corrected; separate subjects despite Momo acceptance146 |
| PG-TX-0116 / NONE | Morika → Momo149–152 skin/age/mark/ashtray claim; Momo2months/not seen/valued response | EV0033; adversarial attributed claims, no past injury/sexual act independently shown |
| PG-TX-0117 / NONE | Kairi → Morika153 leave/never return, Momo and peers witness hand-taking154 | EV0034; actual public refusal, later private assent separate |
| PG-TX-0118 / NONE | Momo → brother157 phone, he → Momo158 brother identity/Kairi bookshop location | EV0035; similar-voice initial error corrected; no name/face yet |
| PG-TX-0119 / NONE | Morika → Kairi161 tomorrow507 one-time request; Kairi → her162 assent; gift163–164; Momo hidden actual listener until165 | EV0036–0038; proposal/assent/gift direct, future attendance/purpose beyond speech unverified, no prior listener-awareness proved |

| Reputation / prior | Target / actual audience and response | Truth/reach boundary |
| --- | --- | --- |
| PG-RP-0037 / RP0034 | Momo/Kairi / local classmates7–9 congratulate recognized dating, Momo accepts | EV0002; current category actual social recognition, not V08 pact proof/all school knowledge |
| PG-RP-0038 / RP0035 | Momo / Sae/fan garden gathering12–14 uses Tōji lure as proof still likes him | EV0003; current attachment has support, exclusionary entitlement not justified; no full school diffusion |
| PG-RP-0039 / NONE | Momo / fan trio31–37 sexual slur/rebound allegation/no-approach demand, she rebuts own liking | EV0009; slur not biography/consent or neutral motive diagnosis, lighter harm actual |
| PG-RP-0040 / NONE | Misao / observed peers50–51 admire caregiving/older-sister image; private weight self-critique54 shared accidentally with Momo | EV0014; public care image separate private disclosure, no analyst body-worth judgment or broader weight rumor |
| PG-RP-0041 / NONE | Momo/Misao/Kairi / bounded peers104–107 intimacy innuendo denied, double punch/compare personality-atmosphere | EV0023–0024; not appearance resemblance, unproved broad adoption of completed-sex rumor |
| PG-RP-0042 / NONE | Momo/Morika/Kairi / school spectators153–154 witness Kairi rejects Morika/leads Momo, Momo squeezes hand | EV0034; local public partner assertion distinct private agreement162, no universal reputation outcome |

IP0051@3 missing-act history unchanged, no proved negative retrieval/media publication, older graffiti/pool authorship/CPR still unresolved. Next IP0099, KN0111, TX0120, RP0043. Revision0.8 — V09 successors2026-10-20; all prior rows retained.
