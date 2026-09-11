---
series: GKM
generation: V2
artifact_type: historical_supporting_record
status: historical_legacy
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
source_boundary: "Preserved earlier-generation supporting record; not fresh AVE-FULL evidence."
last_updated: '2026-09-10'
---
> Historical record retained from the previous packet. “New/current” in this document refers to that earlier execution, not AVE-FULL-20260910. Fresh results are in [the current measurements](FULL_REBUILD_MEASUREMENTS.md) and [current claim review](FULL_REBUILD_CLAIM_REVIEW.md).

# Hiro — authorized execution review, 2026-09-10

This is **new work performed after the user authorized execution**. It supplements the supplied rebuild ZIP, whose measurements and earlier inspection log are retained as inherited records. It is not a recovered original or a new canonical release. The repository baseline is `400234a42d5811847367de94e6e8229fe816e99b`, branch `series/gakuen-idolmaster`; the governing method is v2.2, architecture v2.4, and textual lock is upstream commit `00d150a069a3ffa723a1ff264752ba242024caad`, revision 32. No repository integration was performed.

## What was actually inspected

The reviewer directly viewed **289 distinct timestamped frames** in 18 ordered contact sheets: 48 distinct timestamps from H01, 90 from H03, 110 from the original H04, and 41 from H09. Some timestamps recur in more than one sheet. The H03 frame at 720 s was also viewed separately at full resolution. The timestamp inventory below records those 289 frames; [the additional music/breadth review](EXECUTION_MUSIC_AND_BREADTH_REVIEW.md) records 240 more, for **529 distinct timestamps in 57 viewed sheets across all 33 source IDs**. This is bounded direct visual inspection, including a two-second sequence through the crisis performance insert. It is **not continuous video playback or direct listening**.

Twenty-one A1 scripts were newly retrieved from the exact frozen upstream commit: Dear 009 and 021–037, plus CIDOL018 parts01–03. Each download's Git blob SHA-1 was checked against the recursive tree returned for that commit, and its byte SHA-256 was recorded. Message-only working derivatives retain original file and line references. No raw script or transcript is included in this package. These upstream files corroborate the existing Source Lock 1.0 identity; they are not a post-lock corpus update.

EasyOCR was used on selected subtitle regions to locate likely chapter matches. The resulting guesses were checked against raw message text and actual viewed frames. Empty OCR results and partial generic phrases are not evidence. OCR match scores are retrieval aids, not confidence in an interpretation. Raw script clip times were **not** treated as video times: user interaction, transition behavior, and in-source inserts make such substitution unsafe.

## Materialized inputs and clock control

| Input | Existing Drive identity | Bytes | SHA-256 | Container duration s | Current role |
|---|---|---:|---|---:|---|
| H01, current inbox early-Dear MP4 | `1UELlTgEu9lKMysQKjnLbt4MEUg9XWcbi` | 147467932 | `d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3` | 2660.472744 | Newly rehashed/probed current inbox file; matches inherited hash; source of current H01 frames. |
| H09, current inbox ガラクタロード commu | `1bFRSUu8i-L7iU9OWTQa_9HJPEDmf08ul` | 46726213 | `479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370` | 508.795646 | Newly rehashed/probed current inbox file; matches inherited hash; source of current H09 frames. |
| H03, supplied STEP3 MP4 | `1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q` | 279435246 | `3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989` | 2687.454331 | Newly rehashed/probed input; matches the supplied rebuild's hash. |
| H04, original-length STEP4 MP4 | `1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO` | 545587232 | `4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468` | 3516.615692 | New source for every H04 frame in this execution review. Recorded original byte size matches; remote-object verification is recorded separately. |
| H04, retained trimmed derivative | same recorded source; distinct derivative | 519296380 | `de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e` | 3316.029383 | Preserved as the input of the supplied run's full-file H04 measurements and visual log. |

The current technical pass compared every retained compressed packet: **198,763 video packets and 142,809 audio packets** in the derivative match the original prefix in payload SHA-256, integer PTS/DTS, and packet duration, with zero mismatches. Thus the retained source clock is unchanged. The old derivative measurements still measure its shorter file, and must not be relabeled as whole-original measurements. Original/derivative equivalence is now resolved for the retained audio/video prefix. Current Drive identity verification and full probe detail are in [execution source verification](EXECUTION_SOURCE_VERIFICATION.md); new numerical work is in [execution measurements](EXECUTION_MEASUREMENTS.md).

The actual original source contains the final dialogue display at 3284 s, closing graphics at 3295/3310 s, and credits at 3330/3450 s. The original's additional duration is not additional Dear dialogue in those sampled regions. Packet comparison establishes the retained content; sampled credits alone would not have established equivalence.

## Chapter and passage alignment

These are **verified episode-presence anchors**, not exact chapter start/end times or a claim that every subtitle was inspected. Each anchor joins the supplied file clock to an A1 line. Other passage windows below are retrieval envelopes around viewed evidence, not measured speech onsets. Canonical textual paths remain `transcripts_raw/05_dear_idol/shro=Hiro_Shinosawa/dear_NNN.txt`; upstream retrieval uses the `Resource/adv_dear_shro_NNN.txt` names listed in the receipt.

| Chapter | Media | Viewed anchor s | A1 raw line | Identifying content |
|---|---|---:|---:|---|
| 021 | H03 | 40 | 110 | Producer agrees to address Hiro by given name before the meeting. |
| 022 | H03 | 320 | 15 | Aquarium recovery: Hiro says she has recovered a little. |
| 023 | H03 | 670 | 6 | Sena congratulates Hiro on N.I.A. victory. |
| 024 | H03 | 1095 | 17 | Hiro reports Sena's advice after returning. |
| 025 | H03 | 1450 | 5 | Hiro prepares to meet owl. |
| 026 | H03 | 1800 | 17 | Corridor exchange about entering a crisis together, today and here. |
| 027 | H03 | 2180 | 15 | Close-up embrace/leaning exchange, followed by China interrupting at 2200 s. |
| 028 | H04 original | 140 | 204 | Producer wagers his career on the winter H.I.F. |
| 029 | H04 original | 227 | 16 | Ume greets Hiro at school. |
| 030 | H04 original | 595 | 19 | After selection, Hiro says it was harder than FINALE. |
| 031 | H04 original | 915 | 24 | Producer asks whether rivals supplied useful stimulation. |
| 032 | H04 original | 1245 | 16 | Hiro announces H.I.F. qualification; the chapter closes with the dreamer/not-god declaration at 1561–1562 s. |
| 033 | H04 original | 1590 | 35 | China addresses her audience about expressing her world through song. |
| 034 | H04 original | 1925 | 234 | Sena says she wanted to talk before the main competition. |
| 035 | H04 original | 2225 | 12 | Hiro calls this their final meeting. |
| 036 | H04 original | 2718 | 410 | Onstage Hiro calls herself an impure idol. |
| 037 | H04 original | 3035 | 3 | Ume proposes visiting Hiro with China after the speech. |

**Source routing correction:** Dear 022–027 belongs to H03; Dear 028 belongs to H04. The old pending-request phrase assigning “Dear022–028” to H03 was wrong as a retrieval instruction. No chapter is newly declared missing because of that clerical error.

## Findings that change the precision of the review

**Sena's nonnumeric category is now precisely located.** At H03 1050 s she identifies Hiro's stage `神格`; at 1060 s she directs Hiro to raise it. These frames align to Dear023 lines 444 and 452. Her subsequent admission at 1070 s that she does not know how to do so (line 463) is counterpressure against treating the category as a measured mechanism. The exchange supports a route-level account of reception and uncertainty. It does not establish a repeatable acoustic signature.

**Cute desire and constructed persona have direct local evidence.** H03 1138 s displays Hiro's wish to become a cute idol (Dear024 line 59), followed by her challenge to her current direction. At 1560–1640 s the subtitle speaker is owl while Hiro remains the visible listener; this must not be described as a newly observed owl character model. Dear025 lines 117–178 describe a team-created idol artifact, performer participation, and reception. At 2150 s Hiro asks whether audiences find her cute (Dear026 line 343); at 2160 s Producer says the goddess-like image can also be loved as cute (line 348). These provide evidence for compatible forms of presentation, not a hidden true-self diagnosis.

**Crisis is enacted locally, but its artistic effect remains partly inferential.** H03 1880 s names Producer's cruelty; 1900–1920 s names possible failure and reputational loss (Dear026 lines 93, 108, 124). The ordered two-second sequence at 1970–2016 s shows corridor preparation, departure at 1976, a black transition at 1978, a widescreen stage/audience insert at 1980–2000, and backstage return from 2002. The insert alternates wide audience views and closer Hiro views, with changing arm positions and colored lighting. At 2040 s Producer praises the achieved `神格` (line 251). This confirms the source's staging and narrative evaluation; it is not a controlled comparison proving crisis-caused improvement, nor a judgment of heard concentration.

**The relationship wager and consent counterpressure are no longer full-source placeholders.** H04 130–210 s aligns to Dear028 lines 194–283. At 140 s Producer stakes his career, 150 s Hiro registers the loss condition, 160 s Producer explicitly agrees that he is pushing her, 180 s Hiro names their relationship among the stakes, and 200 s she accepts being cornered. The changing gestures and shot distances are directly visible. The passage preserves agency and asymmetric control together. It does not settle whether the method is ethically justified.

**Fear and accumulated relation are visible/textually anchored.** H04 557 s displays the wish not to lose what she has (Dear029 line 446). H04 950 s says her current power includes what others gave her (Dear031 line 57); 960 s explicitly links this with power that cannot be numerically represented (line 67). H04 1561–1562 s stages the denial that she is a god and the positive dreamer-idol formulation (Dear032 ending). These establish semantic/visual facets without supplying heard fear, breath or cadence.

**Bodily constraint survives the title within this route.** H04 2915 s has Sena tell Hiro to stand and stop her legs shaking (Dear036 line 830); 2922 s displays Hiro's admission that her limit is near (line 864), in a tight lower-face shot. These are precise late evidence against treating victory as erasing bodily constraint. They do not diagnose physiology or measure actual tremor from sampled images.

**The ending qualifies both stable supremacy and indefinite crisis.** At H04 3110 s the maximum-gust framing is explicit (Dear037 line 113); 3170 s Hiro says tomorrow's self will differ (line 186). At **3173 s Producer proposes using this method only this time** (line 194). This is material counterevidence to a claim that the pair straightforwardly endorses permanent emergency. However, Hiro's later accusation that he is bad at lying (line 210) and the lack of a later demonstrated refusal protocol prevent that promise from proving sustainable reform. The ethical question remains open, with this explicit boundary included.

**The own-dream declaration is now directly located.** At H04 **3252–3254 s** Hiro declares `トップアイドルになる、よ。` (Dear037 line 269). The sequence moves from a medium view to a frontal close-up with hand at chest; it is followed by her “this time” acknowledgment and the final promise at 3284 s (line 299). This supports the textual core's HIRO-C27 and the route-level account of dream ownership. This review does not infer vocal force, sincerity from timbre, or a unique canon across incompatible result branches.

**The early live has a precise and modest benchmark.** H01 2090 s displays the warning that many weaknesses remain (Dear009 line 81); 2134–2168 s contains a widescreen, strongly lit concert insert with alternating audience, leg/foot, medium and close views. The source returns backstage at 2170 s. At 2180 s Producer's visible assessment calls the result neither good nor bad (line 145); 2190 s says the minimum role of a small live's opening act was fulfilled (line 152). At 2220 s Hiro reports singing better than in practice (line 181). The rendered audience scale is not a reliable literal count of the diegetic small live, and the insert is not a controlled practice/live comparison. The evidence supports relative improvement as stated in the story, not a claim of ordinary technical superiority.

**H09 directly verifies the retrospective and exposes counterpressure.** At 142 s Hiro says she wanted to become cute (CIDOL018 part01 line 224), followed by close-up blushing/hand-at-chest frames at 144/147 s and a displayed inner account of embarrassment (line 235). The office exchange at 240/330 s matches part02 lines 34/135, establishing that part of the compilation's crosswalk too. At 389 s Hiro calls the relationship equal (part03 line 58); at 429 s she admits that the production sometimes goes too far (line 91). At 460 s she identifies receiving Producer's dream as his finest gift (line 131); 490 s says it made her hobby shine (line 160); 501–505 s joins dream and hobby in continuation (line 180). These are actual visible/textual matches, not inferred merely from the file title. The full affective interpretation remains bounded by the lack of direct listening.

**Displayed Producer text is a separate layer from heard performance.** Producer's raw A1 messages carry `speaker={user}` and `se=sud_se_adv_message-01`; this is an interface-message marker, not evidence of a recorded Producer voice. In particular, the one-time-method limit at H04 3173 s is a directly viewed textual proposition. It must not become an invented audible Producer line through ASR or model interpretation.

## Current claim dispositions

The 20 original claims and their historical transitions remain intact. A disposition describes the particular evidence renewed here, not a global re-certification of an older audiovisual pass. The supplied-run disposition inventory is retained: 12 QUALIFIED, 1 REVISED, 4 SUPPORTED, 3 UNRESOLVED. The new checks sharpen support and limitations within those dispositions.

| Existing claim ID | Authorized execution disposition | Source-clock / locked-text locator | Renewed finding and remaining boundary |
| --- | --- | --- | --- |
| H-AV-001 | QUALIFIED | H01 2090/2180/2220; H03 1050/1138/1880; H04 140/557/3170/3254; H09 142/429/501 | Renewed local gestural and shot variation. A stable low-force identity across 11 dialogue sources remains inherited acoustic analysis; stills and mixed-source measures do not establish it. |
| H-AV-002 | UNRESOLVED | H03 2180/2200/2210 (Dear027 lines 15/43–66); H09 30/60/330; H10 275.100/380.907; H11 43.967/153.884/285.785 | Visible China interruption and friend/Producer exchanges now have precise retrieval points. The added seasonal scenes supply further visible exchanges; heard comic underreaction, reaction magnitude and cadence are not directly renewed. |
| H-AV-003 | QUALIFIED | H04 2915/2922 (Dear036 lines 830/864); H09 360; H07 358.790 | Explicit post-victory limit, lesson effort and a bent-forward street pose with a question about her condition remain in the source. These are visual/textual evidence, not measured physiology, breath, or a medical diagnosis. |
| H-AV-004 | QUALIFIED | H01 2134–2168; H03 1980–2000; H12 30–52; H15 60–82; H17 120–142; H13 four proportional samples | Ordered scene and principal-performance sequences renew local staged activity, framing and light. They are not matched longitudinal skill tests. H13 remains a derivative comparison locator, not chronology authority. |
| H-AV-005 | QUALIFIED | H01 2090/2180/2190/2220 (Dear009 lines 81/145/152/181); H03 1880–1920, 1970–2016, 2040; H04 3110/3170 | Crisis/peak construction is anchored. Early outcome is adequate for a small opener despite stylized large-stage imagery; improved singing is a character report, not a new measured causal finding. |
| H-AV-006 | UNRESOLVED | H04 140–200 (Dear028 lines 204–268), 3173 (Dear037 line 194), line 210 counterpressure; H09 429 | Effectiveness and consent do not settle production ethics. The explicit one-time-only proposal must accompany the OPEN, without being treated as a demonstrated protocol. |
| H-AV-007 | QUALIFIED | H03 1050/1060/1070 (Dear023 lines 444/452/463); 2040 (Dear026 line 251) | Exact god-category passage is now resolved. Sena also admits not knowing how to raise it; reproducible acoustic mechanism remains unestablished. |
| H-AV-008 | QUALIFIED | H09 142/144/147 (CIDOL018 part01 lines 224/235); H03 1138/2150 (Dear024 line 59; Dear026 line 343) | Cute desire has direct local wording and visual presentation. Embarrassed timbre and hidden-true-self diagnosis do not follow from these frames. |
| H-AV-009 | QUALIFIED | H14 50–72; H24 100–122; H32 40–62; principal H12/H15/H17 sequences; inherited acoustic/song-form records | Curated musical experimentalism remains a historical qualitative thesis. Current authored-MV graphic changes are directly observed, but visual novelty also occurs in common H25; neither that nor floor-sensitive RMS ratios establishes the acoustic thesis. |
| H-AV-010 | QUALIFIED | H19 50–72; H23 70–92; H25 30–52; current H20/H21/H22 four-point controls | Preserve rejection of universal avant-garde classification, with musical audition still separate. Current common-source visuals range from bright concert spectacle to strong optical discontinuity; visual complexity is not a genre test. |
| H-AV-011 | QUALIFIED | H12 30–52; H15 60–82; H17 120–142; H05/H06/H08 four proportional commu anchors | Preserve the developmental reading as inherited analysis. Current visual differences among principal stages and commu contexts are renewed, but unmatched source states, mixes and edit forms do not prove a developmental acoustic sequence. |
| H-AV-012 | SUPPORTED | H09 142 (part01 line 224), 240/330 (part02 lines 34/135), 389/460/490/501–505 (part03 lines 58/131/160/180) | The CIDOL018 crosswalk now has direct visible matches in all three parts and newly retrieved frozen Git-blob-verified scripts. This does not claim listening. |
| H-AV-013 | REVISED | H28 139.055; H29 four proportional samples; shared China AV-CHINA-010, Drive 1cmKCgdek46iLWjcatXz7jhKIubJ0Kvfp | Shared communication remains accounted for; last stale baseline absence statement corrected. H28 has a directly viewed local two-body facing/reaching anchor, not a whole-song equality claim. No 34th source or new request is introduced. |
| H-AV-014 | QUALIFIED | H23 70–92; H30 10.117/35.409/65.760/91.052; H31 10.567/36.986/68.688/95.107; H03 1138/2150; H09 142 | Plural cute/god/seasonal modes remain compatible at the visual/textual level. New sung-register listening is not implied, and H23/H31 extreme RMS ratios are near-zero/zero-P10 denominator artifacts; H31 applies the numerical floor, while H23 does not. |
| H-AV-015 | QUALIFIED | H04 557/950/960/3150/3160 (Dear029/031/037); H09 460/490/501–505 (CIDOL018 part03) | Fear of losing accumulated relation and the dream/hobby bridge now have precise locators. Ordinary fan labor is not comprehensively reviewed; no causal acoustical mechanism is asserted. |
| H-AV-016 | SUPPORTED | H04 original 2915/2922, 3110/3170 (Dear036 lines 830/864; Dear037 lines 113/186) | Preserve rejection of stable conventional supremacy using exact bodily-limit and maximum-gust/tomorrow evidence. No fresh heard delivery claim. |
| H-AV-017 | SUPPORTED | H04 140/160/180/200; H09 389/429 (CIDOL018 part03 lines 58/91) | Visible relational reciprocity coexists with producer-controlled stakes and admission of excess. Preserve institutional-asymmetry qualification. |
| H-AV-018 | QUALIFIED | Current H01/H03 crisis inserts; H12/H15/H17 principal sequences; H14/H24/H32 authored imagery; common H25 control | Body/music homology remains inference. Actual visual contrasts strengthen source-form precision but do not prove creator intent or acoustic homology. Common-repertoire discontinuity and floor-sensitive measures prevent a visual/numerical shortcut. |
| H-AV-019 | SUPPORTED | H13 15.393/53.874/100.051/138.533; original authority_note; comparison candidate H12 113.922 | The fan edit visibly samples training/outdoor/stage forms and remains derivative reception/locator evidence. Resemblance to a primary stage image does not prove exact clip identity, skill chronology, or causal improvement. |
| H-AV-020 | UNRESOLVED | H04 3173 (Dear037 line 194), line 210 counterpressure, 3252–3254 (line 269) | The one-time proposal and own dream are explicit; neither establishes a sustainable ordinary floor or its later implementation. The longitudinal question stays OPEN. |

## Quantitative correction without rewriting inherited values

The inherited RMS percentile ratio is especially unstable when quiet tails or digital silence enter the lower decile. H23's P10 is `7.37756150279e-12`, P90 `0.263534618646`, giving `211.058496695 dB`. H31's P10 is zero and P90 `0.326725010906`; the `1e-12` denominator floor produces `230.283647623 dB`. These are **near-silence/floor effects, not expressive musical dynamic range**.

H23 is inside the common-3DMV group; H31 is individual-only. The preserved common-group mean `60.5825248389 dB` is heavily driven by H23. Its musical interpretation is withdrawn. The recorded arithmetic, sample membership and original values remain available; EBU LRA is a separate gated measure. No alternative composite or secretly changed nonsilent-window metric is introduced.

## Reproduction and remaining work

Current direct visual coverage now includes all 33 source IDs at the declared sampling resolution. The initial four-source targeted review remains distinguished from the 29-source breadth extension.

Current visual tooling used Python 3.12.4, OpenCV 4.13.0, Pillow 12.2.0, EasyOCR 1.7.2 and torch 2.12.1+cpu; ffmpeg/ffprobe 8.1.1. The inherited Linux/software versions in the earlier methods file belong to its earlier supplied run and are not the versions used for these frames. The common technical reports separately record their tools.

The normal first video stream was opened with OpenCV, sought by `CAP_PROP_POS_MSEC`, decoded and recorded with its reported time. The optional central crop was x=368:912, y=0:720 of the 1280×720 image, retaining the portrait viewport and dialogue area. Performance insert sheets used the full frame. JPEG quality was 95 for individual working frames and 93 for sheets; these are reading derivatives, not measurement inputs. A decoder `mmco: unref short failure` warning occurred in the H03 second performance sheet; the extracted frames were still inspected, and the warning is not concealed. Recorded original/derivative packet equivalence is independent of this decoder warning.

The bounded visual work is complete for the claimed frames. New direct listening remains unperformed by this reviewer. Automatic transcription or an audio model, if used elsewhere in this delivery, is separately labeled machine-assisted analysis; it cannot be relabeled as this reviewer's listening. Follow the [pending-work register](PENDING_DEPENDENCIES_AND_REQUESTS.md) for exact remaining dependencies.

## Exact viewed-frame inventory

Every sheet below was actually opened through `view_image`. Each pair is **requested seconds → decoder-reported seconds** from file zero. The source SHA-256 is given in the input table above. Sheet hashes identify the working reading derivative, not a newly added AV source. Duplicate timestamps across sheets are counted once per source in the 289-frame total. No frame image or contact sheet is packaged.

| Sheet / source | Frames shown | Working sheet SHA-256 | Requested → decoded seconds |
| --- | ---: | --- | --- |
| h01_overview | 11 | `7a9d22f48cf085c8d2a813ede8b70b921dbc6d9a1400ff27f953ff0320887532` | 1600→1600.000, 1700→1700.000, 1800→1800.000, 1900→1900.000, 2000→2000.000, 2100→2100.000, 2200→2200.000, 2300→2300.000, 2400→2400.000, 2500→2500.000, 2600→2600.000 |
| h01_dear009 | 24 | `2df39e4febe23660121e3f7e0db7709f8643bc6c4dbe6c7dd66fe5cefe6adc6b` | 2020→2020.000, 2030→2030.000, 2040→2040.000, 2050→2050.000, 2060→2060.000, 2070→2070.000, 2080→2080.000, 2090→2090.000, 2100→2100.000, 2110→2110.000, 2120→2120.000, 2130→2130.000, 2140→2140.000, 2150→2150.000, 2160→2160.000, 2170→2170.000, 2180→2180.000, 2190→2190.000, 2200→2200.000, 2210→2210.000, 2220→2220.000, 2230→2230.000, 2240→2240.000, 2250→2250.000 |
| h01_performance | 18 | `362c1b4bb1ab1bc92620caa108b51f113801a72042689c5395df2e37dbdaea37` | 2134→2134.000, 2136→2136.000, 2138→2138.000, 2140→2140.000, 2142→2142.000, 2144→2144.000, 2146→2146.000, 2148→2148.000, 2150→2150.000, 2152→2152.000, 2154→2154.000, 2156→2156.000, 2158→2158.000, 2160→2160.000, 2162→2162.000, 2164→2164.000, 2166→2166.000, 2168→2168.000 |
| h03_overview | 23 | `3a2e7321246fa61b8fd8906b50617ccf1cb361e81b84ae849634f1a5426cc31d` | 0→0.000, 120→120.000, 240→240.000, 360→360.000, 480→480.000, 600→600.000, 720→720.000, 840→840.000, 960→960.000, 1080→1080.000, 1200→1200.000, 1320→1320.000, 1440→1440.000, 1560→1560.000, 1680→1680.000, 1800→1800.000, 1920→1920.000, 2040→2040.000, 2160→2160.000, 2280→2280.000, 2400→2400.000, 2520→2520.000, 2640→2640.000 |
| h03_god | 12 | `805702c1f582c76de3c2084e89fa592132c735e29423f6d712582ceb37c251ae` | 980→980.000, 990→990.000, 1000→1000.000, 1010→1010.000, 1020→1020.000, 1030→1030.000, 1040→1040.000, 1050→1050.000, 1060→1060.000, 1070→1070.000, 1080→1080.000, 1090→1090.000 |
| h03_crisis | 16 | `bee21d9c199e697e872d78fda1b61d7cb2697ef7b32150ff3b67c2498a842d3c` | 1800→1800.000, 1820→1820.000, 1840→1840.000, 1860→1860.000, 1880→1880.000, 1900→1900.000, 1920→1920.000, 1940→1940.000, 1960→1960.000, 1980→1980.000, 2000→2000.000, 2020→2020.000, 2040→2040.000, 2060→2060.000, 2080→2080.000, 2100→2100.000 |
| h03_performance_a | 12 | `28f241942eda8161521b5a08e26348671fe8ac0886b42e63d76b893507863110` | 1970→1970.000, 1972→1972.000, 1974→1974.000, 1976→1976.000, 1978→1978.000, 1980→1980.000, 1982→1982.000, 1984→1984.000, 1986→1986.000, 1988→1988.000, 1990→1990.000, 1992→1992.000 |
| h03_performance_b | 12 | `02dc46f528408451056fc5e5cbc3b9c5e60a812faffeea0394a60c353ea1637b` | 1994→1994.000, 1996→1996.000, 1998→1998.000, 2000→2000.000, 2002→2002.000, 2004→2004.000, 2006→2006.000, 2008→2008.000, 2010→2010.000, 2012→2012.000, 2014→2014.000, 2016→2016.000 |
| h03_chapters | 8 | `37f76e8eb2521e967e8ab34b565c469697ffb990c349b4e1dd4195b73bbf6846` | 30→30.000, 320→320.000, 670→670.000, 1095→1095.000, 1450→1450.000, 1800→1800.000, 2180→2180.000, 2200→2200.000 |
| h03_cute | 16 | `1a980810a79582c20aad46908429915edd0b5d76a3f5e0caaed259d2401812f8` | 40→40.000, 1138→1138.000, 1145→1145.000, 1155→1155.000, 1160→1160.000, 1560→1560.000, 1565→1565.000, 1600→1600.000, 1615→1615.000, 1630→1630.000, 1640→1640.000, 2140→2140.000, 2150→2150.000, 2160→2160.000, 2170→2170.000, 2210→2210.000 |
| h04_overview | 24 | `fa440208a867b9bb480e52f269e38ea6acccf828f14db1c8afe74ebd483f10df` | 0→0.000, 150→150.000, 300→300.000, 450→450.000, 600→599.999, 750→749.999, 900→899.999, 1050→1049.999, 1200→1199.999, 1350→1349.999, 1500→1499.999, 1650→1649.998, 1800→1799.998, 1950→1949.998, 2100→2099.998, 2250→2249.998, 2400→2399.998, 2550→2549.997, 2700→2699.997, 2850→2849.997, 3000→2999.997, 3150→3149.997, 3300→3299.997, 3450→3449.997 |
| h04_wager | 16 | `6f35b9ff1f26989f17543748f532ffb207886d7b5b9640bc51114a5409264b36` | 130→129.997, 140→140.007, 145→144.995, 150→150.000, 155→155.005, 160→159.993, 165→164.998, 170→170.003, 180→179.996, 185→185.001, 190→190.006, 195→194.995, 200→200.000, 205→205.005, 210→209.993, 220→220.003 |
| h04_ending | 24 | `b7b21d05695d6b0d496857226d661ef07b0b4b66e34e074d1a1223f8c4b65db4` | 3095→3094.992, 3105→3105.002, 3110→3110.007, 3120→3120.000, 3130→3129.994, 3140→3140.004, 3150→3149.997, 3160→3160.007, 3170→3170.000, 3175→3175.005, 3180→3179.993, 3190→3190.003, 3200→3199.997, 3210→3210.007, 3220→3220.000, 3230→3229.993, 3240→3240.003, 3250→3249.997, 3255→3255.002, 3260→3260.007, 3270→3270.000, 3280→3279.993, 3290→3290.003, 3310→3310.007 |
| h04_exact | 12 | `accfa2f1bdc0cac2cafe11084edf2fa8f044c390b35338b97e8653e370a27067` | 3101→3100.998, 3172→3172.002, 3173→3173.003, 3187→3187.000, 3214→3213.994, 3217→3216.997, 3251→3250.998, 3252→3251.999, 3253→3253.000, 3254→3254.001, 3284→3283.997, 3286→3285.999 |
| h04_chapters | 12 | `27ed3edea27f38d3094a4ccd8ae55bfbe865f812dae15d48151461ad171ae61e` | 3→3.003, 227→226.993, 590→590.006, 915→914.997, 1245→1244.994, 1580→1579.995, 1825→1825.007, 2225→2225.006, 2595→2594.992, 3035→3034.999, 3295→3294.992, 3330→3329.993 |
| h04_claims | 24 | `bf921487f4ae5ae5ab42cf86875d3d233a101cb7f5bda80e9b641660936d958c` | 552→552.001, 557→557.006, 565→564.998, 595→594.994, 620→620.003, 640→640.006, 950→949.999, 955→955.004, 960→959.992, 1561→1560.993, 1562→1561.994, 1575→1575.007, 1590→1590.005, 1835→1835.000, 1925→1925.006, 1945→1944.993, 2718→2717.999, 2745→2744.992, 2765→2764.996, 2908→2908.005, 2915→2914.995, 2922→2922.002, 2950→2949.997, 3010→3010.007 |
| h09_overview | 18 | `3dc08f3ca800beb8ffa0320d6cd10681e3314236d2a1df040d6d416432798dd6` | 0→0.000, 30→29.997, 60→59.993, 90→90.007, 120→120.003, 150→150.000, 180→179.996, 210→209.993, 240→240.006, 270→270.003, 300→300.000, 330→329.996, 360→359.993, 390→390.006, 420→420.003, 450→450.000, 480→479.996, 500→500.000 |
| h09_claims | 24 | `904ce276cc826086210ff27be53fe5721c90531a8084d46e809adf2645c480ab` | 139→139.006, 142→141.992, 144→143.994, 147→146.997, 171→171.004, 174→174.007, 183→182.999, 187→187.003, 193→192.993, 198→197.998, 201→201.001, 215→214.998, 389→389.005, 420→420.003, 429→428.995, 438→438.004, 446→445.996, 460→459.993, 466→465.999, 470→470.003, 485→485.001, 490→490.006, 501→501.001, 505→505.005 |

The separate full-resolution H03 720 s viewing is the same timestamp already counted above. These sparse and ordered samples do not certify everything between them, despite a shorter interval in the performance inserts. Seek timestamps are not being promoted to exact dialogue onset/offset measurements.

## Frozen A1 retrieval receipt

All rows were retrieved from the exact commit `00d150a069a3ffa723a1ff264752ba242024caad` in `DreamGallery/Campus-adv-txts`. Git blob SHA-1 was recomputed as SHA1(`blob ` + ASCII byte length + NUL + raw bytes) and matched the commit's recursive tree entry. SHA-256 supplies an independent byte receipt. Line locators throughout this review refer to these raw, unmodified files, not message-only working derivatives. URLs make the text review reproducible without shipping raw transcripts in the Markdown-only package.

| Frozen upstream raw file | Bytes | SHA-256 | Git blob SHA-1 |
| --- | ---: | --- | --- |
| [adv_dear_shro_009.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_009.txt) | 126043 | `4ffab9564ccf332ad5e4e1513683db6fd4d092ab58cdcc73cf012b2f68c6e4f5` | `43f555384cad3662cb4671e10268f61c1b88aac8` |
| [adv_dear_shro_021.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_021.txt) | 279518 | `c688175f956fb92ed5103441c2b875eea234c607f6138df57d53f94abb765aa1` | `bca1d829de60688513b66a780fc3867038d10436` |
| [adv_dear_shro_022.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_022.txt) | 247340 | `8ef993b1b384fe0d027178d4eab8e0e695ff5f70e2becac0b2c2cd2cd1cea95d` | `57d33ad5f2b7da7c90a0ed229a80205b169cfc7d` |
| [adv_dear_shro_023.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_023.txt) | 277816 | `0984a616a4822398bae445391eb67856f3cd9bc52efde75a164b96d44bc87d1a` | `359ea5c81e4e14dc4e193142f38937cd8cbce84c` |
| [adv_dear_shro_024.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_024.txt) | 206746 | `cb489a3bf54f6dca771ff0b03518e9862a95f171dc545381624c6c4d5259012d` | `36876b050b5ea1b05eefd2a64f2533a031d98809` |
| [adv_dear_shro_025.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_025.txt) | 187827 | `698eea4974682e838dec6b4b7b08b9cb2c8fc872112bb1bed9164e8530e0e0c4` | `a5cc1aad633390907e1241d423c3db5e2317aa83` |
| [adv_dear_shro_026.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_026.txt) | 225234 | `9a747d2cde852de15331838c08b7f8f0dafd12151fabce0bc06033beaa2b5772` | `d53e6943023c628db7fdff96957a231490d94341` |
| [adv_dear_shro_027.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_027.txt) | 291672 | `647321952c36873ee51d4861cfef9de618fd24befebd82566da645d177a9e2a1` | `803f44017dadbdcbebabef3a8f91e2881209d4c6` |
| [adv_dear_shro_028.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_028.txt) | 168710 | `4581136aa6a19c005a3fad129cb179a89c6e3463bde7fe10a538839c7ac41bd8` | `fb89ccc690f1d95de282d1172bf4a175c756a80d` |
| [adv_dear_shro_029.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_029.txt) | 274711 | `848a724d2d5faace61eb9c45560da5f58215c210890408c0562ba8b800fb8333` | `99bd7e421a3806be06846e07e4a8414586dacd03` |
| [adv_dear_shro_030.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_030.txt) | 263763 | `cfc07c16794240d409c4923158327d5e63c2a602b0a00306d6e7103330ec7647` | `5d80ef13f6e84adcf7e35936109089fde3d030bf` |
| [adv_dear_shro_031.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_031.txt) | 212884 | `13aa8952892eb2a19c2f26ba09371d663014c55dd553f52c4ded2a1ee0fc1c7e` | `f92b699ec94edd2d68bb61bb83b3791f1d7cd877` |
| [adv_dear_shro_032.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_032.txt) | 261379 | `f125216e328c37453352400d5ea4778c0078a6d5d6be472a8929a7087c85e376` | `092192e80d87f161199313fdab063d8a6f82fd4b` |
| [adv_dear_shro_033.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_033.txt) | 176354 | `525e11bba11ade411ef83fa731ef2f6ef24298848308f2929f4611ec6181750b` | `54ec3063f4f31a4309692e59522e1d885330c515` |
| [adv_dear_shro_034.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_034.txt) | 355514 | `a15e6305cdbf88f1762d2872f42f4041d9cfbd88b0d574349654e952237fb35c` | `9f57869e61a997da5ed65d7377833a1a3da08f4e` |
| [adv_dear_shro_035.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_035.txt) | 196681 | `13d116002bcf8b6ace0e8fe89fc1cf812fcb35585f7a1f98bf005a41fc3ee6d9` | `0865c62d5edcd4068d90b379feb42bd5c0aa196a` |
| [adv_dear_shro_036.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_036.txt) | 1066003 | `f85628a8a15598f3d9f2b053be7078ba26d5a9124fa6543f8880c9d80b7a3eba` | `fdee631e08f8613295bc184a628f8387d9bbff48` |
| [adv_dear_shro_037.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_shro_037.txt) | 174133 | `f1174620128d8dbf7ab2352ffb0172fb2de6fc6f31d169ae475a5ef10afb6036` | `76774a26b523daa7576d9e963f7f0d09d9e4f698` |
| [adv_cidol-shro-3-018_01.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_cidol-shro-3-018_01.txt) | 194658 | `f344d0c4f6bf65d063f4ed9cf398da449ae3f7eb2418fdbf606c11eb914fab38` | `bbbf81895ef2d859bfbb6a97ad032d4e1947be65` |
| [adv_cidol-shro-3-018_02.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_cidol-shro-3-018_02.txt) | 88532 | `2ae8faa31f3e3dd7f7e754e9fdb944820827ab680c2c52f42cb9294fa81ac920` | `9272d63166c1672b3f2257deeea69c720b3e216c` |
| [adv_cidol-shro-3-018_03.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_cidol-shro-3-018_03.txt) | 108088 | `5363c611257ae4d499a9f9f08a7e4ca29eb625c866a4905d8242f92c3da3dac0` | `107bea101e565b144d4cf2b0a350a8533f62c4fa` |

## Frame-tool reproduction code

This is the exact bounded frame extraction tool used in this execution. Supply the corresponding source file from the input table and the comma-separated requested times above. `--crop` was used for central dialogue sheets; full-frame overviews/performance sheets omit it. The generated files are working aids and must actually be viewed before claiming visual inspection. This code performs no audio analysis.

```python
from pathlib import Path
import cv2
from PIL import Image, ImageDraw
import argparse, json

p=argparse.ArgumentParser()
p.add_argument('input'); p.add_argument('output'); p.add_argument('times')
p.add_argument('--crop', action='store_true');p.add_argument('--cols',type=int,default=5)
a=p.parse_args()
out=Path(a.output);out.mkdir(exist_ok=True,parents=True)
times=[float(t) for t in a.times.split(',')]
cap=cv2.VideoCapture(a.input)
cells=[]; records=[]
for t in times:
    cap.set(cv2.CAP_PROP_POS_MSEC,t*1000)
    ok,frame=cap.read()
    if not ok: continue
    stamp=float(cap.get(cv2.CAP_PROP_POS_MSEC))/1000
    im=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    if a.crop: im=im.crop((368,0,912,720))
    fn=out/f'{t:010.3f}.jpg';im.save(fn,quality=95)
    im.thumbnail((320,576) if a.crop else (320,180))
    cell=Image.new('RGB',(320,im.height+28),'#101010');cell.paste(im,((320-im.width)//2,28))
    ImageDraw.Draw(cell).text((7,7),f'{t:.3f}s / decoded {stamp:.3f}s',fill='white')
    cells.append(cell);records.append({'request_s':t,'decoded_s':stamp,'path':str(fn)})
cap.release()
if cells:
    h=max(c.height for c in cells); cols=a.cols
    sheet=Image.new('RGB',(cols*320,((len(cells)+cols-1)//cols)*h),'#101010')
    for n,c in enumerate(cells):sheet.paste(c,((n%cols)*320,(n//cols)*h))
    sheet.save(out/'sheet.jpg',quality=93)
(out/'samples.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(str(out/'sheet.jpg'))
```

## Authorized execution audio-trial outcome

The common [audio-model validation report](AUDIO_MODEL_REVIEW.md) records the local software/model trials. Even after input delivery was demonstrated, freeform models repeatedly confused Japanese spoken lines with song or other languages and supplied unsupported musical descriptions. Those auditory judgments were **rejected as evidence**, without selectively keeping convenient outputs. ASR has only a retrieval/alignment role checked against frozen A1 text and visible captions. It does not establish heard affect, musical form, or delivery quality. No acoustic disposition is upgraded, and the direct-listening dependency is not closed.
