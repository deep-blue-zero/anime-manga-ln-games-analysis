---
title: "Peach Girl — Information Circulation and Reputation"
artifact_id: PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER
artifact_type: information_reputation_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.15"
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

## V10 successor transaction — PG-FR-V10

[V10 reading](../02%20Sequential%20Readings/PEACH_GIRL_V10_DEEP_READING.md); EV=PG-EV-V10. Acquisition frontiers are current V10 occurrences. Reader correction not automatically character receipt; illustrated reports distinct independent history, unshown transmissions remain unshown.

| Proposition / prior | Content/class at exit | Evidence/limit |
| --- | --- | --- |
| PG-IP-0099@1 / IP0098 | Kairi first opens craft9, thanks/reports returning rival case12, wears/protects / ESTABLISHED opening/use; return/protection partly reported | EV0002–0003/0010; earlier secret labor not known by V09 assent |
| PG-IP-0100@1 / NONE | Street confrontation16–17, hospital bandage/IV22, contusions/mugging report23 / ESTABLISHED injury, attributed full mechanism | EV0004/0006/0010; Momo receipt39 only, unnamed visitor not merged |
| PG-IP-0101@1 / NONE | Hotel staff25 confirms Okayasu surname507 / ESTABLISHED statement, mistaken Kairi inference | EV0007–0008; Ryo room identity later, imaginary affair27 not actual act |
| PG-IP-0102@1 / NONE | Morika knife attack33 blocked guidebook37 / ESTABLISHED action/obstruction | EV0008; no fake prop or penetrating abdominal wound proved |
| PG-IP-0103@1 / IP0098 | Kairi38 says mediated Morika/brother encounter / ATTRIBUTED_PURPOSE direct to Momo | EV0009; PR0014 original test supported, not all past motive verified |
| PG-IP-0104@1 / NONE | Published Sae graduation48/Honda busy replacing50, entertainment ambition51 / ESTABLISHED transition and speech | EV0013; no verified firing cause/objective industry rank |
| PG-IP-0105@1 / NONE | Tōji follows to prevent acts52, Sae feels monitored/eludes/private breakup idea55 and free claim110 / ESTABLISHED behavior/statements | EV0014/0027; no actual breakup or mutual romantic love proved |
| PG-IP-0106@1 / IP0051@3 related | Sae sex boast59/trauma taunt61, hotel-exit memory / UNSUPPORTED_BOAST + adversarial diagnosis | EV0016; not independent missing-act evidence or clinical explanation |
| PG-IP-0107@1 / IP0095 | Ryo says Morika originally his girlfriend/played tutor Kairi, secrecy protective70–75 / ATTRIBUTED_COMPETING_HISTORY | EV0018; pictures illustrate report, neither universal truth nor automatically all false |
| PG-IP-0108@1 / NONE | Ryo answers Kairi mobile87 while he showers/lets Momo believe outing agreed / ESTABLISHED_IDENTITY_DECEPTION | EV0020; no Kairi apology receipt/date agreement |
| PG-IP-0109@1 / NONE | Morika tricks Kairi into passenger cabin90/drives / ESTABLISHED coercive diversion | EV0022; no locked trunk/unconsciousness/full earlier coordination proved |
| PG-IP-0110@1 / IP0108 | Ryo93 false Kairi-authorized proxy/doesnt know number / ESTABLISHED_FALSE_FRAME | EV0023; one partly true forced-ride reassurance97 does not make all honest |
| PG-IP-0111@1 / NONE | Paid game-research week102, Momo defers103/declines153 / ESTABLISHED_OFFER_AND_REFUSAL | EV0026/0037; not actual job accepted or verified company |
| PG-IP-0112@1 / NONE | Aki loved/dead/letter story119–123 / ATTRIBUTED_UNCORROBORATED_HISTORY | EV0029–0030; reported identity CHAR0022 only, no independent death proof |
| PG-IP-0113@1 / NONE | Momo explicitly permits hug126, returns127, Kairi witnesses129 without earlier talk / ESTABLISHED bounded permission/asymmetry | EV0031; not all later physical consent or full informed truth of premises |
| PG-IP-0114@1 / NONE | Ryo private whisper135 to Kairi, contents unknown / ESTABLISHED event, UNKNOWN message | EV0033; no exact invented confession, no Momo receipt |
| PG-IP-0115@1 / NONE | Morika157 says recruited by Ryo/executive, member/free-party/travel seminar pitch / ATTRIBUTED organizational link | EV0038; knowledge Kairi gains then, no verified full business/coordination |
| PG-IP-0116@1 / IP0111 | Questionnaire154 limited assent,159 income/loans/business interest,164 completed / ESTABLISHED purpose shift/conduct | EV0037/0039/0041; no proved membership/financial agreement, no physical permission |
| PG-IP-0117@1 / NONE | Refused necklace imposed165, assault/escape prevention166–169, Kairi corridor170 / ESTABLISHED harm, outcome UNKNOWN | EV0041–0043; no completed intercourse/rescue/safety by cutoff |
| PG-IP-0118@1 / IP0107 | Momo intends disclose146–147, Ryo permission153 / ESTABLISHED decision/release, actual Kairi receipt NOT_SHOWN | EV0035/0037; not permanent concealment or now confirmed genealogy |

| Knowledge / holder / prior | Actual acquisition/change | Evidence/limit |
| --- | --- | --- |
| PG-KN-0111 / Kairi / KN0110 | Opens gift9/learns craft, knows own injury, mediation explanation38 to Momo | EV0002–0010; not prior secret-labor knowledge, hospital visitor name not supplied |
| PG-KN-0112 / Momo / KN0109 | Hotel surname25→Ryo identity33/38, mediation38→injury/protection39; revises toward care42 | EV0007–0010; exact order, no earlier confirmed Kairi affair |
| PG-KN-0113 / Sae / NONE | Own career transition/monitoring, overhears trip56–57, sees Ryo ride63 | EV0013–0017; no omniscient knowledge of complete brother past/phone fraud |
| PG-KN-0114 / Momo / KN0112 | Receives Ryo genealogy70–75/confidence; adopts protective-brother reading, relays selectively79 | EV0018–0019; truth not verified by belief |
| PG-KN-0115 / Kairi / KN0111 | Hears Momo ride/only-care relay77–79, not full genealogy; warns/dispute | EV0019; no actual Momo call receipt85–87 |
| PG-KN-0116 / Ryo / NONE | Answers call meant Kairi87/knows outing agreement Momo believes | EV0020; no actual Kairi authorization shown |
| PG-KN-0117 / Momo / KN0114 | Believes call with Kairi/date, accepts false proxy93, sees car96 | EV0020–0023; recipient identity not corrected to her yet |
| PG-KN-0118 / Kairi / KN0115 | Experiences deceptive car ride90, sees Momo/Ryo96 without knowing false date | EV0022–0023; not knowingly abandoned outing he agreed |
| PG-KN-0119 / Momo / KN0117 | Receives research offer102, party escort/crowd, Aki report120–123, grants hug126 | EV0026–0031; independent biography not acquired, attraction possibility not new pact |
| PG-KN-0120 / Sae / KN0113 | Learns brother identity114, hears Aki120/sees hug127, later talks Ryo148 | EV0028–0031/0036; real tears/anger, not proved phone-fraud knowledge |
| PG-KN-0121 / Kairi and Morika separately / KN0118 and NONE | Witness hug129, Kairi hears private whisper135 contents not given reader | EV0031/0033; prior memorial permission not shown received before confrontation |
| PG-KN-0122 / Momo / KN0119 | Explains hug140, learns Kairi denies date141 but disbelieves fraud inference, asserts autonomy | EV0034; valid intention claim not guarantee Ryo intention |
| PG-KN-0123 / Kairi / KN0121 | Momo reveals call141, correctly infers Ryo impersonation; warns pursuit142 | EV0034; direct reader corroboration87, motive warning not exact confession |
| PG-KN-0124 / Momo / KN0122 | Overhears Ryo defense151, permission disclose153, declines week/limited form154 | EV0036–0037; not actual Kairi receipt/verified protective past |
| PG-KN-0125 / Kairi / KN0123 | Morika157 reveals Ryo executive/recruiter, runs158 | EV0038–0039; full organization/room outcome unknown |
| PG-KN-0126 / Momo / KN0124 | Notices form mismatch159, receives plausible Sae account/advocacy, sees third matching cross165 | EV0039–0041; owns growing alarm, not all relationships now proved identical |
| PG-KN-0127 / Momo / KN0126 | Experiences assault166–169, recalls Kairi warning166, tries escape/calls distressed170 | EV0042–0043; confirmed current danger not earlier omniscience, rescue unshown |
| PG-KN-0128 / reader / NONE | Hospital22 before Momo knows; phone87 before Kairi inference141; withheld whisper135 remains unknown; danger169/corridor170 parallel | EV0006/0020/0033–0034/0042–0043; reader not given all historical truth or future rescue |

| Transmission / prior | Sender → actual recipient / event | Truth/reach |
| --- | --- | --- |
| PG-TX-0120 / NONE | Kairi → Momo12 gift thanks/report commercial return | EV0003; direct gift circumstances, report not independent handback |
| PG-TX-0121 / NONE | Hotel staff → Momo25 Okayasu507 | EV0007; surname only, not Kairi identity |
| PG-TX-0122 / NONE | Kairi → Momo38 brother/mediated appointment | EV0009; substantive purpose explanation, PR0014 support |
| PG-TX-0123 / NONE | Ryo → Momo39 mugging/injury/case protection, Kairi41 happiness | EV0010; new recipient frontier, current bodily injury independently depicted |
| PG-TX-0124 / NONE | Tōji ↔ Sae52 monitored complaint/preventive following rationale | EV0014; no mutual love or breakup declaration |
| PG-TX-0125 / NONE | Sae → Momo59–62 sex boast/Jigoro taunt, Momo rejects comparison | EV0016; uncorroborated boast/adversarial claim, no clinical diagnosis |
| PG-TX-0126 / NONE | Ryo → Momo70–75 genealogy/protective secrecy/care Kairi | EV0018; historical report not independent fact |
| PG-TX-0127 / NONE | Momo → Kairi77–79 ride/care message only, Kairi → Momo warning | EV0019; genealogy deliberately not relayed then |
| PG-TX-0128 / NONE | Momo → RYO85–87 apology/date meant Kairi; Ryo agrees without correcting | EV0020; actual recipient Ryo, NOT Kairi |
| PG-TX-0129 / NONE | Ryo → Momo93 false Kairi-authorized proxy/number claim | EV0023; direct fraud, not true relay |
| PG-TX-0130 / NONE | Morika → Kairi98 request relay HER apology to Momo | EV0025; promised future relay not actual Momo receipt |
| PG-TX-0131 / NONE | Ryo → Momo102–103 game-research offer/week; let-think reply | EV0026; offer not accepted |
| PG-TX-0132 / NONE | Ryo → Sae/Momo111 full name; Momo → Sae114 brother identity | EV0027–0028; local participants, Sae actual tears115 |
| PG-TX-0133 / NONE | Ryo → Momo120–123 Aki likeness/death/letter; Sae hidden listener120 | EV0029–0030; no general public corroboration |
| PG-TX-0134 / NONE | Momo → Ryo124 Kairi support; hug request125/express assent126 | EV0030–0031; specific permission, Kairi not shown hears earlier speech |
| PG-TX-0135 / NONE | Ryo → Kairi135 private whisper | EV0033; content UNKNOWN to reader/Momo, not invented admission |
| PG-TX-0136 / NONE | Kairi ↔ Momo139–144 contact ban/autonomy/hug/date/impersonation dispute | EV0034; he learns call and correctly infers, she disbelieves, not shared settled truth |
| PG-TX-0137 / NONE | Sae → Ryo148–150 reversed hotel slander, he rebuts; Momo overhears151 | EV0036; actual bounded audience, no broad diffusion/belief proved |
| PG-TX-0138 / NONE | Momo ↔ Ryo153 permission disclose and week refusal,154 questionnaire assent | EV0037; no subsequent Kairi receipt, limited consent |
| PG-TX-0139 / NONE | Morika → Kairi155–157 member/seminar/Ryo recruiter-executive | EV0038; new role knowledge followed run, not prior informed joining |
| PG-TX-0140 / NONE | Ryo → Momo158–159 advertising questionnaire; visible income/loans/business fields | EV0039; changed frame not game interview, membership unproved |
| PG-TX-0141 / NONE | Ryo → Momo160–163 Sae analysis/offer persuade | EV0039–0040; plausible counsel/actual promise, not performed reform |
| PG-TX-0142 / NONE | Momo → Ryo165 gift refusal, he ignores; matching gift acknowledgment | EV0041; no free acceptance |
| PG-TX-0143 / NONE | Momo → Ryo168 leaving, Ryo169 will not let leave | EV0042; explicit boundary overridden by actual force |
| PG-TX-0144 / NONE | Momo distressed Okayasu text170 / intended Kairi orientation | EV0043; audibility/actual Kairi receipt NOT_ESTABLISHED, corridor not rescue |

| Reputation / prior | Target / actual audience | Limit |
| --- | --- | --- |
| PG-RP-0043 / NONE | Sae / magazine48 farewell and Honda professional transition50 | EV0013; real published career transition not proof punitive firing |
| PG-RP-0044 / NONE | Ryo / party crowd112 admires apparent success, Momo impressed | EV0027; social proof not independent game-company legitimacy |
| PG-RP-0045 / NONE | Momo / Sae calls best friend109, she protests | EV0027; false current affiliation not restored friendship |
| PG-RP-0046 / NONE | Ryo / Momo ideal kind brother from counsel/protective report/praise; Kairi disputes | EV0017–0019/0036; situated belief not narrator assessment |
| PG-RP-0047 / NONE | Momo / Sae hotel slander to Ryo148–150, Ryo rejects, Momo overhears | EV0036; bounded rejected accusation, not actual new victim/perpetrator history or broad rumor |
| PG-RP-0048 / NONE | Ryo / Momo trusts defender/advocate152/163, then refused gift/assault revise alarm165–169 | EV0036/0040–0042; no wider audience receipt of assault established |

IP0051@3 and earlier unresolved authorship/CPR/media questions unchanged. Intended truth disclosure not transmitted, unknown whisper not filled, no actual organization loan or rescue proof. Next IP0119, KN0129, TX0145, RP0049. Revision0.9 — V10 successors2026-10-20; all old rows retained.

## V11 successor transaction — PG-FR-V11

[V11 reading](../02%20Sequential%20Readings/PEACH_GIRL_V11_DEEP_READING.md); EV=PG-EV-V11. Actual recipient/time, depiction versus account and audience reach explicit. Unknown histories not automatically disproved by another lie.

| Proposition / prior | Actual content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0119@1 / IP0117 | Momo self-defense18/self-escape20, Kairi meets outside21/empty room27 / ESTABLISHED | EV0002–0006; PR0015 original encounter-interruption DISCONFIRMED, late comfort not success |
| PG-IP-0120@1 / NONE | Ryo conscious24/minimizes injury/hospital bandage43 / ESTABLISHED alive, attributed severity | EV0005/0010; Momo feared death22 not actual death |
| PG-IP-0121@1 / NONE | Ryo tells Sae Momo forced him/attacked on refusal25 / ESTABLISHED_FALSE_COUNTERSTORY | EV0002–0005; she believes/helps, Momo/Kairi receipt not shown |
| PG-IP-0122@1 / IP0114 | Kairi reports V10 private whisper35 access/breakup/claimed Momo agreement/resentment / ATTRIBUTED_REPORT_NEW_DISCLOSURE | EV0007; actual assault corroborates pursuit, claimed consent contradicted, not all past verified |
| PG-IP-0123@1 / IP0118 and IP0107 | Momo actually relays Ryo Morika-original history36; Kairi counters he first/Ryo uninterested / ESTABLISHED_TRANSMISSION_DISPUTED_HISTORY | EV0008; not backdated actual receipt to V10 intention |
| PG-IP-0124@1 / NONE | Ryo reported call47 says test Momo/keep trying / SELF_SERVING_PURPOSE_CLAIM | EV0012; not verified benevolent test, Kairi demands apology |
| PG-IP-0125@1 / NONE | Sae long-night/two-boyfriend claim55–58 and Ryo slept-once claim73 / ATTRIBUTED_ENCOUNTER_ACCOUNTS | EV0013/0016; not actual sex depiction or Tōji consent/breakup |
| PG-IP-0126@1 / IP0112 | Ryo scenarios boast74 under all-lies question / ESTABLISHED_STATEMENT_STRONG_FABRICATION_ACKNOWLEDGMENT | EV0017; independent Aki existence/death/letter remain unverified, not all specifically disproved |
| PG-IP-0127@1 / NONE | Cannot touch truly loved/Ryo says Momo not Kairi true love80/he still81 / ATTRIBUTED_DESTABILIZING_CLAIM | EV0017–0018; identity unspoken then; no clinical law/full cause proof even after164 |
| PG-IP-0128@1 / NONE | Spray floor beside toilet82, card83, Kairi arrives after Ryo84 / ESTABLISHED | EV0018–0019; no bowl/substitution rescue, printed credential not external audit |
| PG-IP-0129@1 / IP0088 related | Misao cross farewell to tutoring97, Momo cannot disclose assault96; defends Ryo / ESTABLISHED_ACCOUNT_AND_NONDISCLOSURE | EV0022; not informed rejection of actual assault testimony; Momo Ryo-love-Misao hypothesis unverified |
| PG-IP-0130@1 / NONE | Sae cancellation-because-Momo report99, Tōji who-Ryo101/continue104 / ATTRIBUTED_RELAY + ESTABLISHED_CHOICE | EV0023;102 Misao question Sae/Ryo not newly learned Momo/Kairi dating, no full Tōji sex receipt |
| PG-IP-0131@1 / NONE | Momo current permission119/setting revision120/love121, Kairi stop126/not her fault128 / ESTABLISHED distinct choices | EV0026–0028; no completed intercourse or exact stopping cause |
| PG-IP-0132@1 / NONE | Repeated avoidance133–135/denial137/excuses138/144; senior theory143/Momo hopeful card theory131 / ESTABLISHED behavior + COMPETING_HYPOTHESES | EV0029–0031; neither clinical proof nor solely imagined avoidance |
| PG-IP-0133@1 / IP0091 and IP0095 related | Album152–154 matches handbook picture: woman Misao NOT Morika / ESTABLISHED_NEW_IDENTIFICATION_TO_MOMO | EV0033; photograph not current reciprocal romance/act, prior guess revised now |
| PG-IP-0134@1 / IP0133 | Kairi actual home visit156/nods frequent159/affirms still loves Misao164/apologizes165 / ESTABLISHED_CURRENT_ATTACHMENT_DISCLOSURE | EV0034–0036; no Misao reciprocity/precise stop cause/explicit breakup or all-care-fake proof |

| Knowledge / holder / prior | Actual acquisition/change | Evidence / limit |
| --- | --- | --- |
| PG-KN-0129 / Momo / KN0127 | Own repeated refusals/assault, self-defense/escape18–20; fears death22, reaches Kairi outside21 | EV0002–0004; feared death not knowledge of death, no omniscient Sae counterstory |
| PG-KN-0130 / Sae / KN0120 | Sees conscious injured Ryo24/receives reversed victim story25, believes/help/hospital43/cross44 | EV0005/0010; not actual assault witness or reader's role knowledge |
| PG-KN-0131 / Kairi / KN0125 | Receives Momo crying/fear22, no ignored report30/self-blame32, accompanies empty-room check27 | EV0004/0006; learned aftermath, no self-claimed direct interruption attributed |
| PG-KN-0132 / Momo / KN0129 | Receives Kairi no-fault32/private-whisper report35/competing Morika history36, recognizes kinship confidence38 | EV0006–0009; old whisper newly received, complete history unresolved |
| PG-KN-0133 / Kairi / KN0131 | Receives Aki/dead-lover premise33, Momo actual Ryo genealogy relay36; one phone call test excuse47 | EV0007–0008/0012; past report not verified by reception |
| PG-KN-0134 / Momo / KN0132 | Sees Sae cross/claims55–58, confirms own Kairi priority/concern Tōji, self-analogy67 | EV0013–0015; maybe Tōji knows61 not actual receipt |
| PG-KN-0135 / Momo / KN0134 | Experiences Ryo washroom, scenarios74, sex claim73, not true beloved80/unspecified he-still81/card83 | EV0016–0019; Kairi precise claim receipt not shown |
| PG-KN-0136 / Kairi / KN0133 | Actual phone79 Ryo/washroom/come, arrives after84; Momo says nothing done85, asks love91/yes Ryo said something | EV0018–0021; no exact not-true-beloved/identity message transmitted |
| PG-KN-0137 / Misao / KN0102 | Hears Momo necklace/physical demand question96 and Kairi accusations, not her actual assault; Sae Ryo words99/102, Tōji continuation104 | EV0022–0023; partial knowledge shapes defense, not full omniscience |
| PG-KN-0138 / Momo / KN0135 | Receives tutoring-farewell account97/imagines Misao Ryo true love, Sae cancellation99, Tōji continuation104 | EV0022–0023; self-consoling couple projection105 not objective reciprocal bond |
| PG-KN-0139 / Tōji / KN0076 and KN0078 distinct propositions | Sae angry Ryo speech heard100, asks who101/evasion; hears Momo partial consolation103 | EV0023; name acquired not full Ryo sex/assault/attachment history |
| PG-KN-0140 / Momo and Kairi separately / KN0138 and KN0136 | Seminar invitation106/Morika canceled/no-involvement report107, rain refuge | EV0024–0025; no external whole-company/coordination proof |
| PG-KN-0141 / Momo / KN0140 | Kairi insecurity116–117, own desire119/love121, his cannot126/not her fault128; cause left unanswered | EV0026–0028; no identity supplied117, no medical inference |
| PG-KN-0142 / Kairi / KN0140 | Receives specific current permission119/changed setting120/direct love121, knows own stopping reason but does not state it126–129 | EV0026–0028; inaccessible cause UNKNOWN to reader/Momo, not analyst invention |
| PG-KN-0143 / Momo / KN0141 | Own hopeful theory131, sees avoidance133–135/denial137, senior advice143, private invitation148 | EV0029–0032; advice not clinical explanation; actual evidence of avoidance not insecurity alone |
| PG-KN-0144 / Momo / KN0143 | Album actual photograph154→Misao identification, Kairi arrival156, frequent nod159, still-love yes164 | EV0033–0036; acquisition sequence, no full cause/exclusive attachment/affair established |
| PG-KN-0145 / Misao / KN0137 | Momo seeks private consult148, sees her/Kairi mutual surprise157–158; family-like explanation | EV0032–0034; exact stopping encounter/assault or outside still-love confession NOT shown received |
| PG-KN-0146 / reader / KN0128 | Self-escape20 before Sae inverse story25, Kairi report35, Ryo partial fabrication74, Kairi stop126, album correction154 then own attachment yes164 | EV0004–0007/0017/0028/0033–0036; knowledge staged, not omniscient complete past/Misao reciprocity |

| Transmission / prior | Sender → actual recipient / content | Truth/reach |
| --- | --- | --- |
| PG-TX-0145 / TX0143 | Momo → Ryo5–16 repeated no/escape, physical refusal overridden | EV0002–0003; actual no, not seduction invitation |
| PG-TX-0146 / NONE | Momo → Kairi22 may killed brother,30 refusal/terror32 self-blame | EV0004/0006; fear not death fact, Kairi receives aftermath |
| PG-TX-0147 / NONE | Ryo → Sae25 Momo forced/attacked him after refusal | EV0005; FALSE_ROLE_REVERSAL, bounded recipient/belief not broader rumor |
| PG-TX-0148 / NONE | Kairi → Momo32 attacker wrong/not her fault | EV0006; explicit no-fault reassurance, not proof no harm |
| PG-TX-0149 / NONE | Kairi → Momo35 reports earlier Ryo whisper sexual access/claimed agreement/breakup wish | EV0007; report newly heard now, no retrodating V10 Momo receipt |
| PG-TX-0150 / NONE | Momo → Kairi33 dead-lover cross and36 Morika-original-Ryo story; Kairi competing history36 | EV0007–0008; actual delayed relay, complete genealogy not verified |
| PG-TX-0151 / NONE | Ryo → Kairi47 reported phone test excuse/keep trying; Kairi apology demand, relayed Momo | EV0012; self-serving report not benevolent purpose validated |
| PG-TX-0152 / NONE | Sae → Momo55–58 long night/fed up Tōji/two men; Momo only Kairi58 | EV0013; no Tōji agreement or act proof |
| PG-TX-0153 / NONE | Momo → Ryo73 stop Sae; he agrees/claims slept once | EV0016; promise and self-report, not independent depiction |
| PG-TX-0154 / NONE | Ryo → Momo74 scenarios/77 true beloved rule/80 she not Kairi true beloved81 unfinished | EV0017–0018; strong fabrication cue plus new allegation, no name81/no scientific rule |
| PG-TX-0155 / NONE | Momo → Kairi79 actual call with Ryo/women washroom/come; he coming | EV0018; actual specific receipt, late arrival84 |
| PG-TX-0156 / NONE | Momo ↔ Kairi85/91 nothing done/love question/of course/Ryo said something yes | EV0019–0021; precise destabilizing claim not transmitted |
| PG-TX-0157 / NONE | Momo ↔ Misao96 necklace/physical-demand question/Kairi accusations/defense; farewell97 | EV0022; actual assault NOT disclosed; Momo private Ryo-love guess not spoken fact |
| PG-TX-0158 / NONE | Sae → room99 cancellation because Momo, threat100; Tōji who-Ryo101/evasion | EV0023; exact relay attributed, actual Tōji name acquisition bounded |
| PG-TX-0159 / NONE | Misao ↔ Momo102 asks Sae dating Okayasu/Ryo; Momo speculative consolation103, Tōji continue104/Misao no overdo105 | EV0023; not first Momo/Kairi dating discovery, no mutual-happiness verification |
| PG-TX-0160 / NONE | Ryo email → Kairi106 invitation includes Momo; Morika → Kairi107 canceled/Ryo angry/no involve | EV0024; report not independently proved whole coordination/exact email time |
| PG-TX-0161 / NONE | Kairi → Momo116 insecurity/brother losses/117 truly wanted unavailable | EV0026; identity not specified |
| PG-TX-0162 / NONE | Momo → Kairi119 specific yes/120 revised setting/121 direct love | EV0026–0027; actual chosen permission/current love,122 no separate exclusive-love attribution invented |
| PG-TX-0163 / NONE | Kairi → Momo126 cannot/sorry128 not her fault | EV0028; explicit withdrawal/reassurance, precise reason unstated |
| PG-TX-0164 / NONE | Momo → Kairi136 avoidance question/he denies137/parent errand138; committee144 declined | EV0030–0031; denial contrasted depicted behavior, task facts not verified |
| PG-TX-0165 / NONE | Senior girl → Momo143 men sometimes cannot/leave space | EV0031; generalized character advice not diagnosis |
| PG-TX-0166 / NONE | Momo ↔ Misao148 private consultation/home invite150 album permission153 trip/name account | EV0032–0033; actual visit/permission, no guaranteed counseling truth |
| PG-TX-0167 / NONE | Misao → Momo/Kairi158 family-like tutor familiarity; Momo → Kairi outside159–163 photo/visits/still love question | EV0034–0035; outside confession not automatically Misao receipt |
| PG-TX-0168 / NONE | Kairi → Momo159 frequent-visit nod/164 YES still love Misao/165 sorry | EV0035–0036; secure current attachment, no explicit breakup/reciprocity or complete physical stopping explanation |

| Reputation / prior | Target / actual audience | Boundary |
| --- | --- | --- |
| PG-RP-0049 / RP0048 | Ryo / Momo learns threat directly, Sae instead receives innocent-victim counterstory25 | EV0002–0005; sharply split local judgments, no school-wide transmission |
| PG-RP-0050 / NONE | Momo / Ryo falsely defames as aggressor to Sae25 | EV0005; Sae belief bounded, no Momo/Tōji/Kairi receipt or wider adoption shown |
| PG-RP-0051 / RP0049 | Ryo / Misao defends from Kairi/Momo accusations96, while Momo withholds assault | EV0022; loyalty under incomplete evidence, not informed institutional finding |
| PG-RP-0052 / NONE | Sae / nurse-room Ryo speech99–102, Tōji name question/Misao shock/Momo partial consolation | EV0023; not school-wide sex rumor or unanimous official couple status |
| PG-RP-0053 / NONE | Kairi / Tōji sees avoidance134, Misao sees surprise157; Momo album then affirmation164 | EV0030/0034–0036; distinct observer access, no public confession to school |

IP0051@3 missing earlier hotel act, older authorship/media/CPR and other unresolved questions remain. Source i82 original verified floor beside toilet; i102 original resolves Sae/Ryo question; i122 no overclaimed speaker; i164 original yes to explicit162 question. Next IP0135, KN0147, TX0169, RP0054. Revision0.10 — V11 successors2026-10-20, all old rows/full body retained.

## V12 successor transaction — PG-FR-V12

[V12 reading](../02%20Sequential%20Readings/PEACH_GIRL_V12_DEEP_READING.md); EV=PG-EV-V12. Current direct exchanges, narrated past, nested Ryo reports and private interpretations have distinct truth/access states.

| Proposition / prior | Content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0135@1 / IP0134 | Apologies5–13/message sent25 versus Momo phone off24; no substantive reason actually received / ESTABLISHED_PARTIAL_CONTACT | EV0002/0004; album blow8/travel brochures14 distinct, all-care-false private verdict not established fraud |
| PG-IP-0136@1 / IP0129 | Misao returns bag16/says Kairi would not explain17/tutor-family reassurance18 / ESTABLISHED_STATEMENT_PARTIAL_ACCESS | EV0003; no actual full Momo intimacy/assault/attachment-confession disclosure to her |
| PG-IP-0137@1 / IP0130 | Tōji reports Sae recent breakup request/refuses31, own-wish counsel32–33 / ATTRIBUTED_REQUEST_ACTUAL_CURRENT_CHOICE | EV0005; no mutual breakup/romantic Momo return |
| PG-IP-0138@1 / NONE | Kairi actual water distress38–41/Momo retrieves42/conscious43 / ESTABLISHED_CURRENT_RESCUE | EV0006–0007; no CPR/resuscitation kiss or settled death intention |
| PG-IP-0139@1 / IP0134 | Kairi sudden confidence loss47/first individual recognition49–57/fullname Misao52/competing attachment78 / DIRECT_EXPLANATION_NARRATED_HISTORY | EV0009–0016; significant account but not clear link to specific V11 stop/avoidance, all-girls inventory not certified |
| PG-IP-0140@1 / IP0133 | Summer camp61 origin of handbook/album photo; Misao slip62/Ryo catch63/intrusive touch64/blush interpreted66/tutor ending67 / ILLUSTRATED_KAIRI_ACCOUNT | EV0011–0013; same Misao CHAR0005, no romantic reciprocity/consent from blush or objective betrayal |
| PG-IP-0141@1 / NONE | Recalled offshore death possibility/not-serious-I-think/retaliatory guilt71 / NEW_DISCLOSURE_OF_PAST_AMBIVALENCE | EV0014; qualifies V09 uncertainty later, not settled clinical plan or mere accident/joke |
| PG-IP-0142@1 / IP0011 | Ryo attributed old rescue to Adachi Momo74 as Kairi tells Momo; beach presence72 / NESTED_REPORT_STRONGLY_SUPPORTED_ATTRIBUTION | EV0014–0015; no old mouth-to-mouth depicted, other rescue steps/participants not exhaustively resolved |
| PG-IP-0143@1 / NONE | Ryo later told Kairi Misao searched four days75; illustrated phone76/don’t tell search/recipient unnamed / NESTED_REPORT | EV0016; Kairi not firsthand whole search, care not romantic preference, Aki surname52/65 not CHAR0022 identity proof |
| PG-IP-0144@1 / IP0134 | Asked kiss79–80/actual81, loves Momo yes82/Misao MORE yes83; fears confessing89 / ESTABLISHED_DIRECT_COMPARATIVE_DISCLOSURE | EV0017/0019; actual hierarchy now known, feared rejection not actual Misao answer |
| PG-IP-0145@1 / IP0131 | Momo informed continuation96–97; Kairi explicit breakup99/leaves106, hypothetical sex101 not actual; Momo later accepts144 / ESTABLISHED_SUCCESSIVE_CHOICES | EV0020–0021/0028; own refusal remains valid, breakup explanation not PR0016 substitution |
| PG-IP-0146@1 / NONE | Momo private124 confirms told Tōji yesterday dumped; Tōji punch117/yielded119, Kairi cover dictionary140 / ESTABLISHED_OFFPANEL_RECEIPT_AND_ACTS | EV0022–0024/0027; no complete assault/bed disclosure implied, Momo not witness punch, cover not accident truth |
| PG-IP-0147@1 / NONE | Tōji actual proposal127/near approach, Momo refuses134/loves Kairi136, Tōji counsel136; Momo maybe-feint138 / ESTABLISHED_ACTS_COMPETING_MOTIVE | EV0025–0027; no completed kiss, whole proposal performance only her hypothesis |
| PG-IP-0148@1 / IP0145 | New pursuit147–148/Kairi no149/Momo collar150/kiss154, later Kairi embrace157/second-for-now158/kiss158–159 / ESTABLISHED_DIFFERENT_CONSENT_FRONTIERS | EV0029–0031; later response not prior permission/exclusive choice/sex, ended old relation remains historical |
| PG-IP-0149@1 / NONE | Sae magazine163 under 安西かりん Anzai Karin; Momo/Kairi recognize, composite query/probably-not, other-class issue/rumor164 / DEPICTED_PUBLICATION_BOUNDED_CIRCULATION | EV0033; image authenticity/production consent/contract/acts not independently certified, no Tōji actual receipt |
| PG-IP-0150@1 / NONE | Sae phone165/recipient unshown, unsure Ryo dating166, unnamed adult waist embrace/leave167–168 seen Momo/Kairi / ESTABLISHED_CONTACT_UNKNOWN_CIRCUMSTANCES | EV0034; not Ryo/not securely Honda, no price/sex/compulsion established |

| Knowledge / holder / prior | Acquisition/frontier | Evidence / limit |
| --- | --- | --- |
| PG-KN-0147 / Momo / KN0144 | Knows Misao attachment from V11, receives apologies but withdraws11/phone off24; tears travel brochures14 | EV0002–0004; sent-success25 not substantive explanation receipt |
| PG-KN-0148 / Misao / KN0145 | Returned bag16, asked Kairi yesterday/he would not explain17, offers counsel19/Momo declines | EV0003; no demonstrated full confession/assault/bedroom account |
| PG-KN-0149 / Tōji / KN0139 | Sees classroom hurt23/pool29, asks Ryo contact30/Momo discarded card, knows own Sae request/refusal31 | EV0004–0005; not Momo current full knowledge, Sae sex still unverified |
| PG-KN-0150 / Momo / KN0147 | Receives Tōji request/refusal report/counsel31–33, experiences Kairi distress/rescues42 | EV0005–0007; no CPR, own swim avoidance not death intent |
| PG-KN-0151 / Kairi / KN0142 | Receives Momo refusal to hear36, experiences water distress/Momo rescue42/embrace44 | EV0006–0007; owns distress, cannot assign Momo punitive wish from silence |
| PG-KN-0152 / Momo / KN0150 | Receives confidence47/history49–78, full Misao name52/photo origin61/nested rescue74 and search75–77 | EV0009–0016; actual recipient now, not independent full past verification or precise V11 stopping answer |
| PG-KN-0153 / reader / KN0146 | New embedded account includes Kairi prior beliefs/revision58–59, intrusive Ryo64/death ambivalence71, nested rescuer/search74–77 | EV0010–0016; no omniscient current Misao preference or all dead-Aki history resolution |
| PG-KN-0154 / Momo / KN0152 | Requested kiss81, explicit Misao MORE yes83, Kairi fear of confessing89; own wish reflection92–93 | EV0017/0019; expected result not actual Misao rejection, earlier Tōji feelings not present choice |
| PG-KN-0155 / Kairi / KN0151 | Knows Momo offer continue96–97/accept hypothetical101, states own breakup99–103 and leaves | EV0020–0021; she cannot require him continue, no actual sex |
| PG-KN-0156 / Tōji / KN0149 | Momo breakup disclosure later confirmed124; by135 knows Misao attachment, exact prior relay unshown | EV0024/0026; not presumed full assault/bedroom detail, watches own punch120 |
| PG-KN-0157 / Kairi / KN0155 | Direct Tōji punch117/yielded-because-you119; later offers friends dictionary cover140 | EV0023/0027; Momo absent, cover not truthful cause |
| PG-KN-0158 / Momo / KN0154 | Actual ending99–107, Tōji wallet aid/proposal127, own refusal134/current Kairi love136; helper guess138 | EV0021–0027; no mind-reading Tōji entire proposal as pretend |
| PG-KN-0159 / Kairi / KN0157 | Momo accepts ending144 then renews pursuit147–148, hears his no149/continues collar/kiss154; he later second-for-now158 | EV0028–0031; knows own refusal/revised response, no exclusive pledge |
| PG-KN-0160 / Momo / KN0158 | Accepts ending144/own new pursuit, receives no149 then later responsive embrace157/second-for-now158/kiss | EV0028–0031; later intimacy does not backdate initial permission, future first-place wish not achievement |
| PG-KN-0161 / Momo and Kairi separately / KN0160 and KN0159 | Read/recognize Sae magazine163, hear bounded rumor164, witness adult companion168; both unsure Ryo dating166 | EV0033–0034; production/companion identity/phone recipient/actual sexual acts unknown; no Tōji receipt |
| PG-KN-0162 / reader / KN0153 | Enacted ending then new pursuit/refusal/reconnection, Sae phone unknown165/visible adult contact168 | EV0021/0029–0034; source no authorial full motive certification or V13 admission |

| Transmission / prior | Sender → actual recipient/content | Truth/reach |
| --- | --- | --- |
| PG-TX-0169 / TX0168 | Kairi → Momo apologies5–13; sent messages25/Momo phone off24 | EV0002/0004; actual contact attempt, not substantive explanation in unopened text |
| PG-TX-0170 / NONE | Misao → Momo bag16/Kairi would not explain17/tutor-family18/counsel19 | EV0003; actual partial reassurance, no confession receipt |
| PG-TX-0171 / NONE | Tōji → Momo asks Ryo contact30, Sae breakup request/refused31, own-wish counsel32–33 | EV0005; request attributed, his refusal/counsel uttered |
| PG-TX-0172 / NONE | Kairi → Momo confidence47/history49–78/full Misao name52/photo origin61 | EV0009–0016; direct current telling, past representations not all independently certified |
| PG-TX-0173 / NONE | Ryo → Kairi PAST rescuer Momo74/later Misao search75, now Kairi → Momo | EV0015–0016; nested report, no new present Ryo call or actual CPR depiction |
| PG-TX-0174 / NONE | Misao → UNIDENTIFIED phone recipient in illustrated past76 don’t blame Kairi/don’t tell search | EV0016; no invented recipient or direct Momo past knowledge |
| PG-TX-0175 / NONE | Momo → Kairi kiss request79–80/love and comparative question82 | EV0017; actual requested kiss81 not rescue mouth-to-mouth |
| PG-TX-0176 / NONE | Kairi → Momo loves her82/Misao MORE yes83/fears damaging Misao relation89 | EV0017/0019; comparative attachment actual, no Misao reply |
| PG-TX-0177 / NONE | Momo → Kairi customary/future kiss94–95/continue even Misao96–97 | EV0020; genuine informed offer, Kairi98 embrace not assent |
| PG-TX-0178 / NONE | Kairi → Momo breakup99/hypothetical casual relation101/hurt/still Misao102–103 | EV0021; actual ending, no sex/full past fraud or clear particular V11-stop link |
| PG-TX-0179 / NONE | Momo → Tōji yesterday Kairi dumped me, off-panel relay CONFIRMED by Momo private124 | EV0024; no exact all-detail transcript invented; by135 Tōji also knows Misao attachment |
| PG-TX-0180 / NONE | Tōji → Kairi punch117/because-you-I-yielded119 | EV0023; Momo absent, no legitimate ownership; friends later dictionary cover140 |
| PG-TX-0181 / NONE | Tōji → Momo waiting limit126/date-again127/redo128–129 | EV0025; actual proposal not established whole feint |
| PG-TX-0182 / NONE | Momo → Tōji cannot134/loves Kairi most136; Tōji → Momo tell honestly136/what-if-kissed137 | EV0026–0027; no completed kiss, Momo helper interpretation138 not his admission |
| PG-TX-0183 / NONE | Momo → Kairi breakup okay144/thanks145 then still love146/new chase147–148 | EV0028–0029; successive ending acceptance/new request distinct |
| PG-TX-0184 / NONE | Kairi → Momo no149/hurt150; Momo → Kairi don’t run/collar150/rejection accusation151–152/kiss154 | EV0029–0030; accusation not clinical truth, no affirmative prior permission to kiss |
| PG-TX-0185 / NONE | Kairi → Momo glad155/second most157/FOR NOW158, later initiated embrace/kiss | EV0030–0031; actual qualified reconnection, no exclusive first-place promise |
| PG-TX-0186 / NONE | Momo ↔ unnamed female peers160–161 redirect man/self-improvement/common interests | EV0032; advice not universal demonstrated method |
| PG-TX-0187 / NONE | Magazine → boys/Kairi/Momo162–164 Sae/Anzai Karin; Kairi → Momo rumors/other-class borrowing | EV0032–0033; bounded publication/recognition, authenticity query unresolved, no Tōji receipt |
| PG-TX-0188 / NONE | Sae → UNIDENTIFIED phone recipient165 waiting/hurry, then actual adult encounter167–168 | EV0034; no automatically Ryo recipient or witnessed transaction terms |

| Reputation / prior | Target / actual audience | Boundary |
| --- | --- | --- |
| PG-RP-0054 / RP0053 | Kairi/Momo / peers see tension22–23, Tōji sees hurt, Misao partial17 | EV0003–0004; no public Misao-love confession/full affair proof |
| PG-RP-0055 / NONE | Kairi/Ryo / Kairi self-report of brother comparison50 to Momo | EV0010; all-girls generalization not exhaustive independently certified social consensus |
| PG-RP-0056 / RP0054 | Kairi / bandage friends139–140 hear dictionary cover, actual Tōji punch117 reader/Kairi | EV0023/0027; cover and event distinct, no Momo punch receipt |
| PG-RP-0057 / NONE | Sae / fictional magazine163, boys162/other-class issue164/Momo-Kairi witnesses adult168 | EV0032–0034; bounded circulation/rumor, not nationwide certainty or known sexual contract, Tōji receipt unshown |

IP0051@3 earlier missing act remains unresolved; no later source act invented. New rescuer attribution IP0142 is not mouth-to-mouth proof; Aki surname not automatic identity merge. Next IP0151, KN0163, TX0189, RP0058. Revision0.11 — V12 successors2026-10-20, full prior body/rows preserved.

## V13 successor transaction — PG-FR-V13

[V13 reading](../02%20Sequential%20Readings/PEACH_GIRL_V13_DEEP_READING.md); EV=PG-EV-V13. An attributed account can materially resolve character uncertainty while remaining distinct from independent replay. All original rows retained.

| Proposition / prior | Content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0151@1 / IP0150 | Actual hotel DEEN/adult/money and direct question/Sae reply12 / ESTABLISHED_CONTACT_AND_REPLY | EV0002; past sex/exact total/adult name not established; no actual police call |
| PG-IP-0152@1 / IP0149 | Sae says not her24/face hers25, teacher supplies composite/Sae nods; peers no punishment27 / CLAIMED_COMPOSITE_REPORTED_OUTCOME | EV0003–0004; not verified digital forgery/official innocence or universal audience |
| PG-IP-0153@1 / NONE | Ryo accepts cash35/knows earnings37/Sae says no hardship38; Tōji business site/fees account60–62 / DEPICTED_TRANSFER_PLUS_ATTRIBUTED_MECHANISM | EV0006/0009; amount/final envelope disposition unknown, no legal/financial audit |
| PG-IP-0154@1 / IP0137 | Sae current breakup statement45/already asked/sorry46; Tōji goes after47 / ESTABLISHED_WITHDRAWAL | EV0007; earlier unilateral refusal not mutual prior assent, help not reunion |
| PG-IP-0155@1 / IP0148 | Momo no50/earlier casual words feared51; Kairi current waiting promise54, later Misao summer wish64 / ESTABLISHED_DISTINCT_CURRENT_CHOICES | EV0008/0010; not old V11 cause or exclusivity, Momo private hypothesis157 not his explanation |
| PG-IP-0156@1 / NONE | Sae thinks game74/crew collision79; Kairi recognizes Pocky80/Momo warns86–88/Sae dismisses / ESTABLISHED_WARNING_RECEIVED | EV0011–0014; rejection not consent; exact Ryo original job pitch unshown |
| PG-IP-0157@1 / NONE | Receipt500000 yen/Sae AV fee/Ryo signature94; crew rights/cancel fee/many girls and Morika DVD95 / ACTUAL_PAPER_OBJECT_AND_INTERESTED_CLAIMS | EV0015; no independent transfer/valid rights/all-girls chronology; DVD strongly supports Morika production appearance |
| PG-IP-0158@1 / NONE | Ryo thought agreed/communication error100/if no quit-I pay then never see me101 / ESTABLISHED_CONDITIONAL_ABANDONMENT | EV0016; prior disclosure/payment unverified; woman99 unnamed, not securely Misao |
| PG-IP-0159@1 / NONE | Sae no/leaving94/resists/hides97, forced restraint/filming111–112, group enters114 after harm / ESTABLISHED_ASSAULT_AND_LATER_RESCUE | EV0015/0018–0019; no completed intercourse/all footage erased; earlier work assent not permission |
| PG-IP-0160@1 / NONE | Sae tremor119/thanks122, Ryo shock-treatment excuse129, knowingly follows132–133, later apology140/146 / ESTABLISHED_ACTS_MIXED_ATTRIBUTED_MOTIVES | EV0020/0022–0025; concern rationale not fact, return not healthy reciprocity, remorse not global reform |
| PG-IP-0161@1 / NONE | Kairi takes Morika DVD135/Momo confiscates, claims no hidden things136 / ESTABLISHED_OBJECT_DISCLOSURE_NOT_EXHAUSTIVE_TRUTH | EV0023; not Sae footage/no destruction proven |
| PG-IP-0162@1 / NONE | Misao named143/collapse144, diet explanation154–155, sleeps156 / ESTABLISHED_CONTEXT_WITH_ATTRIBUTED_CAUSE | EV0025/0027; no clinical/full motive diagnosis or Misao Ryo-call knowledge |
| PG-IP-0163@1 / NONE | Jigoro apology150/no sexual act152, Sae confirmation153; Momo hidden wound156/old Kairi-virginity theory157 / NEW_PARTICIPANT_ACCOUNT_ACCEPTED_BY_MOMO | EV0026–0027; strong correction, not independent replay/purity worth/actual Kairi stated cause |
| PG-IP-0164@1 / NONE | Kairi leaning to sleeping Misao160/Momo opens161/startles162 / ESTABLISHED_INTIMATE_APPROACH_AND_WITNESS | EV0028; no secure completed kiss, sleeping consent, full explanation or next outcome |
| PG-IP-0051@4 / IP0051@3 | Old missing hotel interval sexual act / STRONGLY_DISCREDITED_BY_NEW_PARTICIPANT_ACCOUNT | EV0026: Jigoro directly says nothing happened152, remembered shampoo fabrication addresses condom, Sae yes153/Momo accepts. Earlier mainline uncertainty/editorial assertion preserved historically, not rewritten. No independent replay/full biography; drugging/removal/control/harm retained |

| Knowledge / holder | Receipt at frontier | Limit |
| --- | --- | --- |
| PG-KN-0163 / Momo, Kairi | Direct hotel contact/reply12/magazine answer13–15, sales pitch/affirmation20 | EV0002–0003; no full sex/production history |
| PG-KN-0164 / Momo, Kairi, Tōji | Witness cash/blow/love declaration/ending34–47 | EV0005–0007; each viewpoint bounded, no knowledge final envelope disposition |
| PG-KN-0165 / Momo | Tōji website/fees account60–62; plans Kairi relay then diverted63 | EV0009–0010; intent not receipt |
| PG-KN-0166 / Kairi | Actually says Ryo MLM executive76; recognizes Pocky80 | EV0011–0012; exact off-panel business relay unshown |
| PG-KN-0167 / Sae | Receives warning86–88/rejects, actual hotel mismatch93/receipt94/DVD95 | EV0014–0015; belief changes, no consent inferred from earlier dismissal |
| PG-KN-0168 / Ryo; unnamed woman separately | Ryo receives Sae call99–101; woman witnesses/hears his side100 | EV0016; not securely Misao; no automatic woman receipt entire Sae side |
| PG-KN-0169 / Momo, Kairi | Sae concession105/location room301106, adjacent exchange | EV0017; precise prior location previously unknown, no call to police |
| PG-KN-0170 / Tōji and friends separately | Actual urgent summons107/then see room114, peers118 not sure full events | EV0017/0019–0020; not automatically full history |
| PG-KN-0171 / Sae, Momo, Kairi, Tōji | Hear Ryo police boast/excuse126–129; see Sae follows133 | EV0022–0023; hear claim not verified motive/corruption |
| PG-KN-0172 / Momo | Kairi shows DVD135; Sae specific thanks/apology140/146; Jigoro account152/confirmation153 | EV0023–0026; strongest new old-incident receipt, not Kairi/Tōji automatically informed |
| PG-KN-0173 / Misao | Sees Momo/Sae leaving143/hears Kairi says reformed/dating Ryo; says not good | EV0025; no proven full AV/Ryo-call/assault history from this exchange |
| PG-KN-0174 / Kairi | Actual Misao collapse144/diet insecurity154–155/sleep and own approach160 | EV0025/0027–0028; no Momo Jigoro-relief receipt yet |
| PG-KN-0175 / Momo | Doorway161/close configuration/Kairi startled162 | EV0028; not every prior gesture/diet talk or actual completed kiss known |
| PG-KN-0176 / Reader | Full ordered cash/warnings/calls/harm/rescue/return/repair/parallel couch ending | EV0002–0028; attributed history and motive not omniscient fact, unnamed99 woman remains unassigned |

| Transfer / prior | Actual channel | Boundary |
| --- | --- | --- |
| PG-TX-0189 / NONE | Momo → Sae hotel/adult12/magazine13; Sae → Momo dismissal/sales15–18 | EV0002–0003; original PR0017 qualifies |
| PG-TX-0190 / NONE | Sae ↔ school staff22–26; peers → peers/Momo no punishment27 | EV0004; supplied composite theory not independent truth |
| PG-TX-0191 / NONE | Sae → Ryo cash34–35; Ryo → Momo knows/free37; Sae → witnesses love/ending44–46 | EV0006–0007; exact sum/final disposition unshown |
| PG-TX-0192 / NONE | Momo ↔ Kairi no50/trip52–53/wait54; Kairi → Momo Misao wish64 | EV0008/0010; present promise/ongoing asymmetry |
| PG-TX-0193 / NONE | Tōji → Momo business60–62; Kairi demonstrates knowledge76 | EV0009/0011; no invented exact Momo relay62 |
| PG-TX-0194 / NONE | Ryo → Sae short-job offer71; Sae → Momo game understanding74; Kairi → Momo Pocky recognition80 | EV0011–0012; no sexual agreement |
| PG-TX-0195 / NONE | Momo → Sae actual phone warning86–88/Sae reply/hangup | EV0014; receipt/rejection secure |
| PG-TX-0196 / NONE | Crew → Sae receipt/rights/Morika95; Sae → Ryo actual call99–101/conditional response | EV0015–0016; interested claim not valid entitlement |
| PG-TX-0197 / NONE | Sae → Momo actual105–106 location/help; Momo → Tōji107; Kairi → glasses friend/others107 | EV0017; distinct information depth |
| PG-TX-0198 / NONE | Momo → friends secrecy118/group assent; Sae → Momo defensive118/thanks122 | EV0020; no erasure proven |
| PG-TX-0199 / NONE | Sae → Ryo questions127–128; Ryo → group shock rationale129 | EV0022; explanation not verified motive |
| PG-TX-0200 / NONE | Sae → Momo/Kairi knows but love132; actual Ryo response133 | EV0023; no stable reform |
| PG-TX-0201 / NONE | Kairi → Momo Morika DVD135/no hidden things136 | EV0023; one object and statement, not exhaustive truth |
| PG-TX-0202 / NONE | Sae → Momo/Kairi gift139/apology140; Sae → Momo private acknowledgment145–146 | EV0024–0025; concrete content |
| PG-TX-0203 / NONE | Misao ↔ Kairi concern143/diet154–155 | EV0025/0027; not Momo receipt before return |
| PG-TX-0204 / NONE | Jigoro → Momo no old act152; Sae → Momo confirmation153 | EV0026; not automatic Kairi/Tōji receipt |
| PG-TX-0205 / NONE | Manager → Momo Kairi on break157; Momo actual visual doorway161 | EV0027–0028; seen arrangement not secure kiss |
| PG-TX-0206 / NONE | Kairi → Momo name162 | EV0028; no substantive explanation before cutoff |

| Reputation / prior | Target / actual audience | Boundary |
| --- | --- | --- |
| PG-RP-0058 / RP0057 | Sae / school staff22–26/questioned identity, peer account27 | EV0004; no verified national consensus/composite finding |
| PG-RP-0059 / NONE | Ryo / Momo-Kairi-Tōji hear allegations/excuses/cash and witness consequences | EV0006/0022; police-linked boast not public verified corruption |
| PG-RP-0060 / NONE | Sae / rescuing friends know bounded emergency and agree secrecy118 | EV0020; no secure universal dissemination/suppression |
| PG-RP-0061 / NONE | Momo sexual-history self-understanding / Momo hears Jigoro/Sae152–153 | EV0026–0027; private relief not public correction or moral worth |

IP0051@4 is a dated later disclosure, not silent repair of old freezes. Prior whole-row history retained. Next IP0165, KN0177, TX0207, RP0062. Revision0.12 — V13 successors2026-10-20.

## V14 successor transaction — PG-FR-V14

[V14 reading](../02%20Sequential%20Readings/PEACH_GIRL_V14_DEEP_READING.md); EV=PG-EV-V14. Actual hearing, private thoughts, conditional offers and later participant corrections are separated. All original rows retained.

| Proposition / prior | Content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0165@1 / IP0164 | M directly names sleeping approach13/K if awake hit response / ESTABLISHED_DIRECT_EXCHANGE | EV0002; no secure completed kiss/permission or Misao awareness |
| PG-IP-0166@1 / IP0163 | M actually tells K Jigoro outcome33–35/remaining undressing harm37 / ESTABLISHED_NEW_RECIPIENT | EV0005; prior correction not automatically earlier K knowledge/no harm |
| PG-IP-0167@1 / NONE | M actually asks why/how long41–42/K later says no strange words48 / ESTABLISHED_RECEIPT_AND_OMISSION | EV0006/0008; M later no recall not cancellation of K hearing |
| PG-IP-0168@1 / NONE | K confession57/59/Misao only younger brother now/future62 / ESTABLISHED_ACTUAL_REJECTION | EV0009; not an unmade confession, later happy137 not reversal |
| PG-IP-0169@1 / IP0155 | K tells M result65/distance67–69/M actual ticket/noon/five-minute deadline76/K understands / ESTABLISHED_BOUNDED_TERMS | EV0010–0011; private wait70 not all received, future attendance not yet |
| PG-IP-0170@1 / NONE | S falsely tells T she quits88/manager quarrel-reconcile story140; T unaware M87 / ESTABLISHED_SETUP_WITH_DIFFERENT_KNOWLEDGE | EV0012/0023; T not proven schemer, prior V13 repair not refuted |
| PG-IP-0171@1 / NONE | Wallet gone100/K infers skaters101/Ryo family call102/battery fails early / LOSS_ESTABLISHED_THEFT_INFERRED | EV0014; no depicted theft/full location-money receipt/help |
| PG-IP-0172@1 / NONE | Wife similar youth112/maps self M/husband Okayasu113; actual Sanae153 / ATTRIBUTED_ROLE_ANALOGY | EV0016/0025; NOT literal names/identity deception, owner real name unknown |
| PG-IP-0173@1 / IP0069@1 | S admits T burned real negative/bluff117/only one118/photo116 / NEW_PARTICIPANT_RETRACTION | EV0017; strongly discredits old retained-real claim, not independent all-copy destruction |
| PG-IP-0174@1 / IP0070 | M hears117–124/demands exact128/receives mass-media threat129 / ESTABLISHED_LATER_DETAILED_RECEIPT | EV0017–0020; V07 accurate partial suspicion not equivalent earlier full knowledge |
| PG-IP-0175@1 / NONE | Misao never actually told Ryo/chocolate not given upon first beloved136/new try intent137 / LATER_SELF_ACCOUNT_QUALIFIES_REPORTED_REJECTION | EV0021; illustrated woman not securely dead Aki, no actual new approach/reciprocity |
| PG-IP-0176@1 / NONE | Annual award146/expired supermarket148/owner never said this best149 / EXPECTATION_PRIMING_AND_ATTRIBUTED_ANALOGY | EV0024; no securely explicit this-dish-won claim, no universal romance rule |
| PG-IP-0177@1 / NONE | K influenza diagnosis158/pneumonia risk/helpless water162/contact display163 / ESTABLISHED_ILLNESS_NOT_COMMUNICATED_TO_MOMO | EV0027/0029; no actual pneumonia/death/completed M call; phone worked133 after102 failure |
| PG-IP-0178@1 / NONE | T learns M heard155/apologizes hurtful method156/M grateful157 / ESTABLISHED_MUTUAL_RECOGNITION | EV0026; gratitude not M sole-fault verdict or resumed couple |
| PG-IP-0179@1 / NONE | M probable give-up if K absent165/T conditional serious restart166 / ESTABLISHED_CONDITIONAL_PROPOSAL_UNANSWERED | EV0030; no actual deadline failure/M answer or new dating |
| PG-IP-0069@2 / IP0069@1 | Burned objects genuine versus later retained-original claim / STRONGLY_REVISED_BY_V14_PARTICIPANT_ADMISSION | EV0017; bounded V07_139–142/145–146 recheck confirms burn and earlier claim. S now says real burned/bluff117–118. Old REFUTED-as-warranted-conclusion row preserved historically; genuine-negative reading now strongly supported with attribution, exhaustive photo inventory still UNKNOWN |

| Knowledge / holder | Receipt at frontier | Limit |
| --- | --- | --- |
| PG-KN-0177 / Momo, Kairi separately | Direct sleeping-approach exchange13 | EV0002; not secure completed contact/Misao permission |
| PG-KN-0178 / Sae | Unequal relationship disclosed20/identity refused21, K first unaware29/stuck30 | EV0003–0004; no secure Misao name merely from adjacent M memory31 |
| PG-KN-0179 / Kairi | Actual Jigoro no-act report33–35/M undressed37, actual love-pain questions41–42 | EV0005–0006; later48 omission not lack of hearing |
| PG-KN-0180 / Misao | Actual K serious love59/credits M61, gives romantic refusal62 | EV0009; no automatic knowledge sleeping approach |
| PG-KN-0181 / Momo | K phone confession/rejection65/distance67–69; her actual communicated deadline76 | EV0010–0011; no current exclusive choice or illness knowledge |
| PG-KN-0182 / Kairi | Misao rejection62/M exact noon/five-minute terms76 | EV0009/0011; M private unlimited willingness70 not all heard |
| PG-KN-0183 / Sae; Tōji separately | S hears rejection outcome71/overhears deadline78; T job lead88/unaware M87 then distance/trip98–99 | EV0011–0013; different recipients/depth, full deadline not spoken T here |
| PG-KN-0184 / Ryo | K says not return awhile102/note actual; phone fails mid trouble | EV0014; no full shop location/money request or actual help |
| PG-KN-0185 / Owner, Sanae separately | K love account/counterfactual111, owner later call-side eavesdropping question145/counsel150 | EV0016/0024; not automatically complete phone content or all M history |
| PG-KN-0186 / Tōji | S real-negative/bluff admission117–118/apology119 | EV0017; M listening not yet known until155 |
| PG-KN-0187 / Momo | Overhears118–124/gets exact mass-media threat129; hears manager S story140/scandal model144 | EV0017–0020/0023; actual later information, private self-blame not T receipt |
| PG-KN-0188 / Kairi | Actual Misao call134/never told Ryo136/new confidence137; phone functions133 | EV0021; no rejection reversal/no automatic M knowledge |
| PG-KN-0189 / Kairi, owner, Sanae | Owner fever153/doctor influenza158/medicine/pneumonia risk | EV0025/0027; M not shown informed, risk not actual pneumonia |
| PG-KN-0190 / Tōji | M confirms overheard155; hears thanks156–157/probable give-up165 | EV0026/0030; current K illness unknown to him in shown source |
| PG-KN-0191 / Momo | T actual apology156/current fireworks159/conditional proposal166 | EV0026/0028/0030; no M answer, contact screen163 not completed call |
| PG-KN-0192 / Reader | Parallel waiting/work/blackmail correction/Misao call/illness/fireworks | EV0002–0030; reader excess does not grant characters omniscience; analogies/counterfactuals remain attributed |

| Transfer / prior | Actual channel | Boundary |
| --- | --- | --- |
| PG-TX-0207 / TX0206 | Momo ↔ Kairi direct encounter13 | EV0002; PR0018 qualifies response not full truth |
| PG-TX-0208 / NONE | Kairi → M phone17/S answers18–19 identifies self/M hangs | EV0003; interception not M impersonation, no full info transfer |
| PG-TX-0209 / NONE | M → S unequal relation20/identity refusal21; S → M encouragement23–25 | EV0003; bounded disclosure |
| PG-TX-0210 / NONE | S ↔ K outside27–30/hurting M/stuck admission | EV0004; no Misao name secure S receipt |
| PG-TX-0211 / TX0204 | M → K actual Jigoro report33–35 | EV0005; K newly receives |
| PG-TX-0212 / NONE | M → K why/how-long41–42; K → M nothing-strange48 | EV0006/0008; actual receipt followed omission |
| PG-TX-0213 / NONE | K → Misao serious confession57/59; Misao → K sibling-only62 | EV0009; actual refusal |
| PG-TX-0214 / NONE | K → M phone65/rejection/distance67–69 | EV0010; qualified request not current first pledge |
| PG-TX-0215 / NONE | M → K ticket/noon/five terms76/K understands/S overhears78 | EV0011; deadline actually communicated |
| PG-TX-0216 / NONE | S → T yesterday job call reported88; M → S actual why call90 | EV0012; no M impersonation |
| PG-TX-0217 / NONE | M → T distance/ticket98–99/T → M call-if-worried107 | EV0013/0015; not whole deadline terms |
| PG-TX-0218 / NONE | Ryo ↔ K call102/early battery death | EV0014; full trouble/location not received |
| PG-TX-0219 / NONE | K ↔ shop couple love111/role analogy112–113/lodging | EV0016; no literal name match |
| PG-TX-0220 / NONE | S → T photo116/retraction117–118/apology119; M overhears118 | EV0017; initially T unaware witness |
| PG-TX-0221 / NONE | M ↔ S direct exact-threat demand128/answer129/leave130 | EV0020; later confirmed mechanism |
| PG-TX-0222 / NONE | Misao → K actual phone134–137/never told Ryo136 | EV0021; no new K romance acceptance |
| PG-TX-0223 / NONE | Manager → M S quarrel-story140/scandal talk143–144 | EV0023; report/gossip not actual sexual history |
| PG-TX-0224 / NONE | Owner/Sanae → K soba/couple counsel149–151/fever153/doctor diagnosis158 | EV0024–0025/0027; attributed counsel, M absent |
| PG-TX-0225 / NONE | M ↔ T overheard acknowledgment155/actual apology156/thanks157 | EV0026; finally shared receipt |
| PG-TX-0226 / NONE | T → M conditional restart166/NO answer before exit | EV0030; contact display163 not added as actual K→M call |

| Reputation / prior | Target / actual audience | Boundary |
| --- | --- | --- |
| PG-RP-0062 / NONE | M/T relationship / manager hears S quarrel-and-reconciliation narrative140 | EV0023; manager calls S kind, misleading account not neutral history |
| PG-RP-0063 / NONE | Fictional idol Fujisaki Anri / shop customers/manager143–144 | EV0023; actual attributed scandal/slur, not verified sexual biography or external real-person claim |
| PG-RP-0064 / NONE | M media-exposure fear / M private counterfactual144/thanks157 | EV0023/0026; potential/imagined outcome not actual broad publication/inevitable lasting ruin |

Next IP0180, KN0193, TX0227, RP0065. Revision0.13 — V14 successors2026-10-20; IP0069@2 new later evidence, historical freeze/rows unchanged.

## V15 successor transaction — PG-FR-V15

[V15 reading](../02%20Sequential%20Readings/PEACH_GIRL_V15_DEEP_READING.md); EV=PG-EV-V15. Private certainty, third-party receipt and actual Momo receipt stay distinct.

| Proposition / prior | Content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0180@1 / IP0177 | Missed K call7/new hospital9/developing pneumonia / NEW_LATER_CONFIRMATION_AND_PROGRESSION | EV0001; V14 contact screen/risk not rewritten, M callback unconnected/no diagnosis receipt |
| PG-IP-0181@1 / IP0179 | M pretended nonhearing13/current T attraction22 / ESTABLISHED_PRIVATE_EVASION_AND_FEELING | EV0001–0002; no initial T proposal acceptance/absence of romantic pull |
| PG-IP-0182@1 / NONE | K companion insight25/owner puzzle27/K blank puzzle46/future plan48 / PRIVATE_OR_THIRD_PARTY_NOT_M_RECEIPT | EV0003/0007; joint effort metaphor not destined fit or achieved union |
| PG-IP-0183@1 / IP0169 | M actually reads soba/trip/want-see email33–34/rejoices35 | EV0005; GENERIC_ASSURANCE_RECEIVED_NO_FIRST_CHOICE_OR_ILLNESS_WORDS |
| PG-IP-0184@1 / IP0169 | M newly gives T full noon/five-minute/give-up terms39 | EV0006; NEW_RECIPIENT_FULL_TERMS_NOT_BACKDATED_TO_V14 |
| PG-IP-0185@1 / NONE | K directly tells Mis M most loved53–54/old attachment nearer admiration | EV0008; ACTUAL_NAMED_RECIPIENT_MISAO_NOT_MOMO, retrospective self-account not eternal proof |
| PG-IP-0186@1 / NONE | R hospital insurance/help and advanced bill account59–60 confirmed by K thanks | EV0009; BOUNDED_HELP_NOT_FULL_MORAL_REFORM_OR_BANK_AUDIT |
| PG-IP-0187@1 / NONE | Man alleges guaranteed profit/bankruptcy61–62/R business-risk defense/sword swing63/Mis interposes64 | EV0010; ALLEGATIONS_AND_ACTUAL_VIOLENCE_DISTINCT, weapon imitation later74/109 |
| PG-IP-0188@1 / NONE | M sees taxi/Mis/K66–67/bystander sword/one hurt68, not full attack | EV0011; TRUE_PARTIAL_WITNESS_NOT_R_INJURY_OR_POLICE_KNOWLEDGE |
| PG-IP-0189@1 / NONE | K vague delay71–72/R contusions/imitation74/questioning75/Mis offers cover/urges promise76 | EV0012; ACTUAL_M_OMISSION_AND_DISTINCT_CONSTRAINT, not unlimited wait agreement |
| PG-IP-0190@1 / IP0169 | K12:30_77/M12:50_78/log8/30 11:50_79/off80/M1:55_84/K2:15_88/home2:55_91 | EV0013–0014; ACTUAL_LATE_APPOINTMENT_NOT_M_LEAVE12_05, intercut seconds not fixed |
| PG-IP-0191@1 / NONE | M private second-place inference79/goodbye99; K private/third-party actual first choice | EV0008/0013–0015; READER_KNOWLEDGE_EXCESS_NOT_M_OMNISCIENCE_OR_RECEIVED_BREAKUP |
| PG-IP-0192@1 / NONE | T followed M102/M wanted alone103; actual sand grief97/old rescue95/foam98 | EV0015–0017; NO_PRESENT_DROWNING_OR_ESTABLISHED_SELF_HARM_INTENT, question not plan |
| PG-IP-0193@1 / NONE | K tells S R injury109/S panics110; train suspension landslide111 | EV0018–0019; NEW_S_RECEIPT_NOT_S_MECHANICAL_STOP_CAUSE, she wrongly assumes M alone |
| PG-IP-0194@1 / NONE | M/T stranded/existing Adachi-Okayasu booking115/actual companion T | EV0019; MISREGISTRATION_NOT_IDENTITY_OR_CONSENT, no initial planned joint night |
| PG-IP-0195@1 / NONE | T hug120/actual kiss129/M neck embrace130/unknown caller T phone132/earring137 | EV0020–0022; ACTUAL_RESPONSIVENESS_OBJECT_AND_CHANNEL, not K cross/M phone/blanket consent |
| PG-IP-0196@1 / NONE | K owns assumed endless waiting arrogance140/20km143/pays/climbs/falls144–145 | EV0023; ACTUAL_ACCOUNTABILITY_AND_EFFORT_NOT_M_OBLIGATION_OR_EXACT_FARE |
| PG-IP-0197@1 / NONE | K inn call147/staff says M+companion under Okayasu name148/battery dies before identity/M receipt | EV0024; TRUE_COMPANION_WITH_MISREGISTERED_NAME, K not securely knows T identity |
| PG-IP-0198@1 / NONE | Shared undressed night/morning150–156/M response155/happiness thought156 | EV0025; SEXUAL_ENCOUNTER_STRONGLY_IMPLIED_NOT_SPECIFIC_ACT_PROOF_OR_MERE_ROOM_SHARING |
| PG-IP-0199@1 / NONE | M handhold157/escape-flow questions158–159/private K hope161 | EV0026–0027; ACTUAL_MIXED_AFFECT_NOT_T_FULL_RECEIPT_OR_MOTIVE_VERDICT |
| PG-IP-0200@1 / NONE | K Shiranami160/M-T return train161, later L sign163/M returns embrace166 | EV0027–0028; ACTUAL_M_T_RESUMPTION_NOT_M_K_MEETING_OR_K_WITNESS |
| PG-IP-0201@1 / NONE | All161 V15 mainline lacks direct K-to-M first-choice-over-Misao words/receipt | EV0001–0028; PR0019_DISCONFIRMED_WHOLE_WINDOW, first-choice Mis53/private plans not substitutes |

| Knowledge / holder | Receipt at frontier | Limit |
| --- | --- | --- |
| PG-KN-0193 / Momo | Missed call7/callback unconnected; private evasion13/current T pull22 | EV0001–0002; no hospital/first-choice receipt |
| PG-KN-0194 / Kairi, owner, Sanae | Illness/hospital9/charger24/clarity25/puzzle counsel27 | EV0001/0003; M absent |
| PG-KN-0195 / Momo; Tōji separately | M actual email33–34/T sees relief35; T gets full terms39 | EV0005–0006; no automatically all K history shared |
| PG-KN-0196 / Shop couple | K cleared indecision47/M future masterpiece48 | EV0007; third-party vow not M receipt |
| PG-KN-0197 / Misao | K explicitly M first53–54; praise/own R intent56 | EV0008; no M receipt or K romance acceptance |
| PG-KN-0198 / Kairi, Misao, Ryo | Financial accusation/sword swing61–64/R injury74/police75 | EV0010–0012; complete business truth/precise impact not established |
| PG-KN-0199 / Momo | Partial K-Mis taxi66–67/bystander68/vague urgent call71 | EV0011–0012; lacks R injury/imitation/police/first-choice declaration |
| PG-KN-0200 / Kairi | Exact noon/five terms remembered77, empty plaza88/home mother91 | EV0013–0014; M saw taxi/interpretation not told in call |
| PG-KN-0201 / Tōji | M tells saw taxi/Mis84/cannot wait85; follows102 | EV0013–0016; not full attack/cause or K illness knowledge |
| PG-KN-0202 / Momo, Tōji separately | M says wanted solitude103/T apologizes following102/offer wait104 | EV0016–0017; concern not proof self-harm plan |
| PG-KN-0203 / Sae | K R injury explanation109/imitation; panics110 | EV0018; new receipt, M-alone guess wrong |
| PG-KN-0204 / Momo, Tōji; Kairi, Sae separately | Storm suspension111/room constraint112/taxi queue114 | EV0019; different places/channels, S arrival R unshown |
| PG-KN-0205 / Inn staff | Adachi/Okayasu booking115/actual M-T occupancy | EV0019/0024; presumed name does not prove staff knows T true identity |
| PG-KN-0206 / Momo, Tōji | Actual kissing129/earring exchange137/restart138/shared night/morning | EV0021–0022/0025; exact sexual act not depicted/private motives not automatically shared |
| PG-KN-0207 / Driver; Kairi separately | K admits arrogance140/road blocked/20km143/pays/leaves car | EV0023; M does not witness journey |
| PG-KN-0208 / Kairi | Inn staff M accompanied148/connection dies before identity/M relay | EV0024; T identity not secure; no evidence M received K call |
| PG-KN-0209 / Momo | Private flow/escape doubts158–159/K lingering hope161; T love gesture163–164 | EV0026–0028; no learned hospital/attack or above-Mis words |
| PG-KN-0210 / Tōji | M responsive night/morning/handhold/final returning embrace166 | EV0025–0028; complete private doubts not received |
| PG-KN-0211 / Reader | Parallel K realization/attack/accountability/journey and M partial knowledge/T intimacy | EV0001–0028; no transfer solely through adjacent panels; whole-window forecast fails |

| Transfer / prior | Actual channel | Boundary |
| --- | --- | --- |
| PG-TX-0227 / NONE | T proposal reprise5/M says unheard/private evasion13 | EV0001; actual private receipt not acceptance |
| PG-TX-0228 / NONE | K missed M call newly confirmed7/M callback7–10/phone left shop8 | EV0001; actual call attempt not connected speech |
| PG-TX-0229 / NONE | Owner charger24/K insight25/puzzle counsel27 | EV0003; third party not M |
| PG-TX-0230 / NONE | M manager shift28/T volunteer29/M retract30 | EV0004; request withdrawn |
| PG-TX-0231 / NONE | K → M actual soba/trip/want-see email33–34 | EV0005; no hospital/first-choice content |
| PG-TX-0232 / TX0217 | M → T exact noon/five/give-up39 | EV0006; full terms newly received |
| PG-TX-0233 / NONE | Couple → K wages44–45/K → couple blank puzzle46/future plan48 | EV0007; actual material gift not M pledge receipt |
| PG-TX-0234 / NONE | K → Misao explicitly M first53–54/Mis → K praise/R intent55–57 | EV0008; recipient crucial |
| PG-TX-0235 / TX0218 | R ↔ K insurance/hospital help/advanced money59–60 | EV0009; new bounded help confirmation |
| PG-TX-0236 / NONE | Man → R accusation61–62/R business-risk reply/sword attack63 | EV0010; no adjudication |
| PG-TX-0237 / NONE | M sees taxi66–67/calls K name/no secure receipt/bystander68 | EV0011; partial witness/hearsay |
| PG-TX-0238 / NONE | M → K call71/K urgent delay72/no R/Mis/police explanation | EV0012; actual incomplete exchange |
| PG-TX-0239 / NONE | K/Mis hospital74/Mis offers police/go75/urges singular-date76 | EV0012; K also questioning pending |
| PG-TX-0240 / NONE | K → M failed call77/M manual off80/failed later88 | EV0013–0014; intercut timing unresolved |
| PG-TX-0241 / NONE | M → T partial taxi/Mis account84/cannot wait85 | EV0013; no full cause |
| PG-TX-0242 / NONE | K → M home phone/mother91/asks relay if M calls | EV0014; not direct M receipt |
| PG-TX-0243 / NONE | T → M following apology102/M solitude103/T wait104 | EV0016–0017; no original joint travel agreement |
| PG-TX-0244 / NONE | K ↔ S deadline107–108/R injury109/S distress110 | EV0018; S new receipt/M-alone inference |
| PG-TX-0245 / NONE | Service announcements111/rooms full112/inn booking115 | EV0019; staff name assumption persists |
| PG-TX-0246 / NONE | K reads M want-see reply114/private going plan115 | EV0020; new arrival versus reread unknown/not K outgoing first-choice message |
| PG-TX-0247 / NONE | T → M renewal121/actual kiss129/M response130/earring137/restart138 | EV0020–0022; later response not blanket consent |
| PG-TX-0248 / NONE | Unknown caller → T phone132/T ignores133 | EV0022; caller not secured K/M phone |
| PG-TX-0249 / NONE | K → Uedaya staff147/companion answer148/battery dies before K identity/M call | EV0024; attempted direct transfer fails |
| PG-TX-0250 / NONE | T → M L love sign163/M recalls164/runs back/embraces166 | EV0028; actual nonverbal renewed affection/K not informed |

| Reputation / prior | Target / actual audience | Boundary |
| --- | --- | --- |
| PG-RP-0065 / NONE | Ryo business credibility / man publicly alleges guaranteed-profit bankruptcy61–62 with K/Mis nearby | EV0010–0011; attack actual/allegation not independently adjudicated, M only later vague bystander report |
| PG-RP-0066 / NONE | M-K priority / M partial taxi sighting79/S criticism107–108/T partial account84, versus Mis receives M-first53 | EV0008/0011–0014/0018; different bounded audiences, no broad public scandal/exhaustive shared truth |

Next IP0202, KN0212, TX0251, RP0067. Revision0.14 — V15 successors2026-10-20; original propositions/frontiers/forecasts retained.

## V16 successor transaction — PG-FR-V16

[V16 reading](../02%20Sequential%20Readings/PEACH_GIRL_V16_DEEP_READING.md);2026-10-20 owner date.171 directly inspected/157 mainline. EV=PG-EV-V16. Historical rows unchanged.

| Proposition / prior | Content/class | Evidence / limit |
| --- | --- | --- |
| PG-IP-0202@1 / NONE | Classmate K-search report8/new M receipt; Nami projection history27/apology33 | EV0001/0003/0005; ATTRIBUTED_REPORT_AND_PARTIAL_CORRECTION |
| PG-IP-0203@1 / IP0200 | M explicitly T-resumption YES18 to short friend; protective old history relay established23–24 | EV0002; SPECIFIC_RECIPIENT_NOT_K_OR_OMITTED_FULL_TRANSCRIPT |
| PG-IP-0204@1 / NONE | K says did not meet M/explain to Mis21/refuses relay22; bruise accident claim23 | EV0003; WITHHELD_EXPLANATION_AND_LATER_FALSE_CAUSE |
| PG-IP-0205@1 / NONE | M partial face-exam25 infers Mis priority26; K honmei38 public blame | EV0003/0005; ATTRIBUTED_INFERENCE_CONTRADICTED_CURRENT_PRIVATE_ATTACHMENT |
| PG-IP-0206@1 / NONE | M intended direct ending29/K back-T question39/M silent | EV0004–0005; UNDELIVERED_PRIVATE_INTENTION_NOT_RECEIPT |
| PG-IP-0207@1 / NONE | S nausea30–31/test42/pregnancy claim121–124 | EV0004/0006/0020; MEDICAL_TRUTH_AND_PATERNITY_UNCONFIRMED |
| PG-IP-0208@1 / NONE | K reverse-psychology breakup request56–57 intended stop S relay | EV0009; PRIVATE_ASIDE_REVERSES_LITERAL_PUBLIC_SCHEME_READING |
| PG-IP-0209@1 / NONE | Mis hospital narrative62–75: actual confession/R reciprocity/S slap/R hit; K hears74–75 | EV0011–0012; NEW_LATER_DISCLOSURE_NOT_RETRO_V15_KNOWLEDGE |
| PG-IP-0210@1 / NONE | R address Aki63/65/107 consistent Mis surname 安芸(V12_52) | EV0011/0017; NO_ESTABLISHED_DEAD_AKI_MISIDENTIFICATION |
| PG-IP-0211@1 / NONE | Actual M new portrait80 inside K ID book81/old Mis picture recalled89/98 | EV0013–0015; ACTUAL_OBJECT_VS_MEMORY_COMPOSITE; capture moment unshown |
| PG-IP-0212@1 / NONE | M tomorrow secret return96 not performed across V16 | EV0015/0026; PLAN_NOT_ACTION |
| PG-IP-0213@1 / NONE | M stops101/T stops102/apology104/patience105/M private relief-guilt106 | EV0016; ACTUAL_BOUNDARY_COMPLIANCE_NOT_T_PHOTO_RECEIPT |
| PG-IP-0214@1 / NONE | R denies ever datingS111/116/invalidating self-love114 | EV0017–0018; SELF_SERVING_REVISION_NOT_NEUTRAL_HISTORY |
| PG-IP-0215@1 / NONE | S sex/promises claim118/only R and no paid-customer sex130 | EV0019/0021; PARTICIPANT_CORROBORATION_NOT_EXHAUSTIVE_INDEPENDENT_HISTORY |
| PG-IP-0216@1 / NONE | All six hear pregnancy124; M/T arrived late/T explicitly middle133 | EV0019–0022; AUDIENCE_EXPANSION_NOT_OMNISCIENT_TRANSFER |
| PG-IP-0217@1 / NONE | M/K pregnancy-bluff suspicion135/M learns Mis confessed134 | EV0022; SUSPICION_NOT_FALSE_PREGNANCY_ADMISSION |
| PG-IP-0218@1 / NONE | K hypothetical explained/takenM hospital142–143 | EV0023; COUNTERFACTUAL_NOT_ACTUAL_RECEIPT_OR_GUARANTEED_RECONCILIATION |
| PG-IP-0219@1 / NONE | K actually witnesses M/T kiss151–152; T noticing K153 strong framing inference | EV0024–0025; WITNESS_NOT_EXACT_DIRECT_WORDS_TARGET |
| PG-IP-0220@1 / NONE | K got-lost face-saving lie158/M sees tears160/hears lingering161 | EV0026; ACTUAL_PARTIAL_EMOTIONAL_DISCLOSURE_NOT_MIS_COMPARISON |
| PG-IP-0221@1 / NONE | No direct M→K T-resumption words across157 mainline | EV0027; PR20_DISCONFIRMED_ORIGINAL_TERMS_NOT_REWRITTEN |

| Knowledge / holder | Receipt at frontier | Limit |
| --- | --- | --- |
| PG-KN-0212 / Momo | Learns K searched8/hears casual apology14, privately reads indifference | EV0001–0003; not complete late reason |
| PG-KN-0213 / Short supportive friend | M confirms T18/old protective account relayed23–24/later K book identity86 | EV0002/0014; not securely Rikko |
| PG-KN-0214 / Kairi | Girls gossip19/hears Nami/M dispute36/asks backT39/silence | EV0002/0005; inference not M direct confirmation |
| PG-KN-0215 / Misao | Knows K did not explain21/offer rejected22/hears school sexual slur44–45 | EV0003/0007; rumor not factual biography |
| PG-KN-0216 / Momo | Sees K examining Mis face25/infers current priority26 | EV0003; lacks cause/current K preference |
| PG-KN-0217 / Sae; reader separately | S actual test42/private distress, later public claim121 | EV0006/0020; clinical result unconfirmed |
| PG-KN-0218 / Kairi | S says no M relay56; hears Mis complete hospital narrative74–75 | EV0009/0011–0012; M absent |
| PG-KN-0219 / Momo | K handbook/M portrait80–81/old Mis photo contrast98; secret return plan96 | EV0013–0015; K intent not verbally explained |
| PG-KN-0220 / Tōji | M STOP101/unease; own rush/fear104/patience105 | EV0016; K photograph not explicitly received |
| PG-KN-0221 / Sae, Kairi, Misao | R no-relationship/invalidation remarks111–116; S/K actual overhear112 | EV0017–0018; M/T not full early recipients |
| PG-KN-0222 / Momo, Tōji | See group119/hear pregnancy124/Mis defense126; T says from middle133 | EV0019–0022; not full private/hospital speech |
| PG-KN-0223 / Ryo, Misao, Sae | Private only-partner account130/R doubt/Mis rebuke131–132 | EV0021; K/M/T not shown following private conversation |
| PG-KN-0224 / Momo; Kairi separately | M newly learns Mis confession134; both discuss possible pregnancy bluff135 | EV0022; possibility not verified fact |
| PG-KN-0225 / Kairi | Book missing138/private counterfactual142–143/actual M/T kiss151–152 | EV0023–0024; direct M resumption words absent |
| PG-KN-0226 / Tōji | Framing153 strongly suggests sees hidden K; no speech | EV0025; motive/full regret not transferred |
| PG-KN-0227 / Momo | Sees K tear160/hears lingering apology161 | EV0026; no explicit above-Misao declaration |
| PG-KN-0228 / Reader | Parallel private M photo joy106/K love142/T actual boundary compliance102/R selective tenderness and violence69/72 | EV0011–0012/0016/0023–0027; knowledge not automatically any characters |

| Transfer / channel | Content/disposition | Evidence / limit |
| --- | --- | --- |
| PG-TX-0251 / Classmates → Momo | K search report8/train sighting9–10 | EV0001; actual received report not full emergency |
| PG-TX-0252 / Momo → short friend | T resumption confirmed18; older protective story across ellipsis23–24 | EV0002; no invented omitted wording |
| PG-TX-0253 / Girls → Kairi | Couple gossip19; later public waiting debate36–39 | EV0002/0005; not M direct T-confirmation |
| PG-TX-0254 / Misao → Kairi | Offer M explanation22 rejected | EV0003; proposed relay NOT performed |
| PG-TX-0255 / Kairi → Momo/peers | Honmei blame38/asks back T39/M silent | EV0005; protects public face/conceals actual current attachment |
| PG-TX-0256 / School gossip → Misao | M sex-friend/bored-discard slur44–45 | EV0007; attributed rumor not fact |
| PG-TX-0257 / Sae ↔ Kairi | No M relay56/reverse request57/threat59 | EV0009; private intent stops transmission |
| PG-TX-0258 / Kairi → Ryo | Next-day meeting58; angry late sixpm call108 | EV0009/0017; actual R delay |
| PG-TX-0259 / Misao → Kairi | Hospital love/violence/reassessment62–75 | EV0011–0012; new full recipient not M |
| PG-TX-0260 / Kairi handbook → Momo/short friend | Portrait80/ID81/correction86; retained not returned96 | EV0013–0015; material evidence not spoken explanation |
| PG-TX-0261 / Momo ↔ Tōji | STOP101/compliance102/apologies103/patience105 | EV0016; actual heard boundaries |
| PG-TX-0262 / Misao → Ryo | Withdraw confession110 | EV0017; actual expressed request |
| PG-TX-0263 / Ryo → S/K/Mis | Denied relationship/invalidation111–116/S/K overhear112 | EV0017–0018; M/T not early recipients |
| PG-TX-0264 / Sae → Ryo/public | Sex-promises118/pregnancy121–124/responsibility122 | EV0019–0020; later M/T hear not whole early dispute |
| PG-TX-0265 / Misao → Ryo/Sae | Private talk129/defends S/rebukes R131–132/leaves | EV0021; K/M/T not private audience |
| PG-TX-0266 / Kairi → Momo/Tōji | Mis confession fact134/limited public setup133; pregnancy-bluff question135 | EV0022; not full hospital explanation or proven fabrication |
| PG-TX-0267 / Momo/Tōji kiss → hidden Kairi | Actual witness151–152/T visual notice153 implied | EV0024–0025; no M direct words |
| PG-TX-0268 / Kairi → Momo | Lost lie158/tear160/lingering apology161 | EV0026–0027; emotional receipt does not satisfy PR20 |

| Reputation / prior | Event/interpretation | Evidence / limit |
| --- | --- | --- |
| PG-RP-0067 / NONE | Nami insurance accusation33–36/personal projection admitted; short friend defends32 | EV0003–0005; multiple female voices, not one identical hostile chorus |
| PG-RP-0068 / NONE | M sex-friend/bored-discard rumor44–45/Mis hears; K protective self-blame38 does not stop sexualized compression | EV0005/0007; reputation not biography |
| PG-RP-0069 / NONE | Public R/S dispute/pregnancy and paternity slur124–125/Mis defense127/crowd applause | EV0019–0021; small crowd reaction not universal ethical vindication |

Next IP0222,KN0229,TX0269,RP0070. Revision0.15 — V16 successors; prior bodies retained.
