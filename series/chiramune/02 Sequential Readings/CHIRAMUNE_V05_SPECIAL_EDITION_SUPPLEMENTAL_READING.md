---
series: CHIRAMUNE
artifact_type: supplemental_reading_and_checkpoint
scope: VOLUME_05_SPECIAL_EDITION_SS_BOOKLET
source_boundary: "Japanese regular-main Volumes 01-05 frozen; V03 bundled bonus and separate booklet integrated; exact V05 special-edition witness classified component by component; no V06+ evidence"
generation: V0.1
status: active_provisional
release_state: frozen_source_boundary
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune Volume 05 special-edition supplemental reading and checkpoint

## Responsibility and control state

This artifact classifies and integrates the appended short-story booklet in the exact Volume 05 Special Edition only after the regular Volume 05 main transaction was frozen, published, audited, and independently validated at commit `0f2fec67f1464244c98cfde3af35fd11dc578e55`.

The Special Edition's regular-main text was compared to the admitted regular Volume 05 witness before use. The ordered normalized text streams contain 5,479 rows each and have zero differences. No regular-main claim is re-read or double-counted here. `CHIRAMUNE_V05_DEEP_READING.md` and `CHIRAMUNE_V05_PROSPECTIVE_FREEZE.md` remain the historical main-volume boundary. This document treats the appended booklet as a multi-component later-admitted witness. No Volume 06 or later source entered the reading.

## 1. Exact source identity

| Field | Verified value |
|---|---|
| Source object | Volume 05 Special Edition EPUB |
| Drive file ID | `1CUzsfbC57YmOJ2gvYkBZfzfqGjR4cMds` |
| SHA-256 | `4cd54018dc4f9bde7fc34ee9efff01b5c22cfce2fedda5db579ac7c04aef767e` |
| OPF title | `千歳くんはラムネ瓶のなか　５　ＳＳ冊子付き電子特装版` |
| OPF creator / publisher / language | `裕夢` / `小学館` / `ja` |
| OPF publication date / ASIN | 2021-04-25 / `B091T3MBHQ` |
| Distinct supplemental contents | 17 republished bonus stories; one newly written long story; contents/dividers; creator commentary; profiles; colophon; advertising backmatter |
| Booklet colophon | 2021-04-25; 裕夢 / raemz / 伸童舎 / Gagaga Bunko editorial department / 小学館 `[V05S:p-0075#img01]` |

The locally generated whole-object retrieval table contains 6,858 non-empty text/image rows and has SHA-256 `9af70d8cd177491c59e249d089d4ac18819481cd3a69d0e0c30aab4f639bf00e`. Its reading projection contains 7,034 lines and has SHA-256 `7f9e950af457636d77dbef400b14fb3b66efd931eda9584ab6a81622515284f4`. Of the locator rows, 1,340 belong to the appended booklet: 1,306 text rows and 34 image rows.

Supplemental locators use the source-qualified prefix `V05S` plus XHTML resource and paragraph/image order, for example `[V05S:p-0058#p0060]` and `[V05S:p-0073#img01]`. The extraction resources and full source bytes remain outside Git.

## 2. Witness topology and component classes

The object cannot be assigned one blanket chronology or one undifferentiated analytical role.

| Component | Primary role | Treatment |
|---|---|---|
| Complete Volume 05 main text | `MAIN_LN` duplicate witness | text-equivalent to the regular witness; verified but not analytically counted again |
| Seventeen previously distributed stories | `SUPPLEMENTAL_MAINLINE` components | each retains its original Volume 1–4 association and receives an individual diegetic/prospective route |
| `シャンプーにキャップ` | revised `SUPPLEMENTAL_MAINLINE` witness | one shared event with the V03 booklet story; edition-specific additions preserved without double-counting |
| `夜更け前の月と夜明け前の太陽` | new `SUPPLEMENTAL_MAINLINE` component | first-year autumn prehistory; safe only after the complete V05 main freeze because first published here |
| Contents, creator notes, profiles, colophon | `PARATEXT` | support provenance, editorial method, names/readings, and limited creator-process claims, not independent diegetic events |
| Divider recap collages | visual paratext | confirm editorial grouping and character focus; not new scenes |
| Magazine advertising pages | advertising paratext | audited; excluded from narrative inference |

The contents pages explicitly identify original distribution channel and focal character(s) `[V05S:p-0037#img01]`, `[V05S:p-0038#img01]`. The creator's first-volume note states the initial bonus-story constraint as fiction that would not directly affect the main story if unavailable, while still deepening character understanding and remaining behind the main chronology `[V05S:p-0046#img01]`. The fourth-volume note describes supplements as a home for simultaneous character stories that the main volumes' page limits and focal choices cannot give equal space `[V05S:p-0071#img01]`.

These statements explain editorial responsibility; they do not reduce the stories to noncanonical trivia. The correct architecture is separate integration with explicit dependency, not silent absorption into numbered-main freezes.

## 3. Component inventory and safe insertion boundaries

| ID | Story / original association | Diegetic placement | Earliest safe prospective boundary |
|---|---|---|---|
| `V05S-01` | `たとえば最初に呼ぶ名前` — comics V1 tie-in / Yua | V01, after Kuranosuke assigns Kenta's case and before Saku's first visit | after V01 main; first acquired/published in this compilation, so current integration follows V05 main |
| `V05S-02` | `窓の外` — comics V1 / Yua | V01, after the failed first Kenta visit | same handling as `V05S-01` |
| `V05S-03` | `家の外` — comics V2 / Yuko | V01, after Kenta exits his room and before the former-friends confrontation | same handling as `V05S-01` |
| `V05S-04` | `雨、あめ、降れ、ふれ` — Melonbooks novel festival / Yua | V01, about two weeks into the Kenta intervention | same handling as `V05S-01` |
| `V05S-05` | `遠くに続く影法師` — Melonbooks youth fair / Asuka | V02 grouping; before V03 states the departure plan | after V02 main; current integration still follows V05 main |
| `V05S-06` | `いつものカフェラテ、いつものティーラテ` — V2 Toranoana / Yua | V01, immediately after Kenta's former-friends confrontation | after V02 main by original publication dependency; current integration follows V05 main |
| `V05S-07` | `ふたりの放課後ボーイフレンド` — V2 Animate / Yuzuki × Haru | early V02, after Yuzuki's late call and Saku/Haru one-on-one; before Yuzuki names love | after V02 main |
| `V05S-08` | `多分、友達の好きな人` — Melonbooks novel festival / Haru | after Saku helps Yuzuki in V02; exact position before the ending remains bounded rather than exact | after V02 main |
| `V05S-09` | `ナイショの青と青` — V2 Gamers / Yuko | during the decoy-underwear operation | after V02 main |
| `V05S-10` | `できればずっと、また今度` — V3 Animate / Yuko × Yua | V03 domestic interlude at Saku's apartment; exact day open | after V03 main |
| `V05S-11` | `たまにはネクタイをはずしたくなる` — V3 Gamers / Haru | several days after the lunchtime catch; before the proposed batting-center visit | after V03 main |
| `V05S-12` | `摑みたいのに摑めなくていつでも見てるだけ` — V3 Toranoana / Yuko | weekend after Yuzuki's stalking case resolves | after V03 main |
| `V05S-13` | `シャンプーにキャップ` — V3 BookWalker / Yuzuki | late V03, after the Tokyo return and before Monday; same event as the separate V03 booklet story | after V03 main, but this revised edition itself enters only at the current V05-special boundary |
| `V05S-14` | `あなたと見たいブルームーン` — Melonbooks novel festival / Asuka | the morning of Asuka and Saku's V03 escape | after V03 main |
| `V05S-15` | `うそつきは夏のはじまり` — V4 Toranoana / Yuko × Haru | immediately after Kuranosuke assigns Saku/Haru pool cleaning | after V04 main |
| `V05S-16` | `先輩と後輩の距離` — V4 Gamers / Asuka × Haru | after Saku's baseball return begins and before V04 closes | after V04 main |
| `V05S-17` | `私たちの１ on １` — V4 Animate / Yuzuki | during and immediately after the climactic girls' basketball game | after V04 main |
| `V05S-18` | `夜更け前の月と夜明け前の太陽` — newly written / Yuzuki × Haru | first-year autumn, after summer break and the first girls' basketball tournament | after complete regular V05 main by first-publication dependency |

Earlier diegetic placement does not reopen an earlier freeze. These stories test preserved historical states from a later acquisition/publication boundary.

## 4. Story-level evidence

### V05S-01 — Yua is selected as a social interpreter, not a generic caretaker

Saku chooses Yua for the Kenta visit because she can model hostile reactions and how others perceive Saku, whereas he characterizes Yuko's strengths as more instinctive `[V05S:p-0040#p0014-p0039]`. Yua calls their intervention presently annoying to Kenta but leaves open later changed meaning, then proposes forceful treatment by analogy to her own experience `[V05S:p-0040#p0040-p0047]`.

The address sequence—Uchida-san to Yua-chan to Yua, Chitose-kun to Saku-kun—uses names as an index of earned intimacy `[V05S:p-0040#p0052-p0055]`. The scene strengthens Yua's independent perceptual competence and her long relational history with Saku without deciding romance.

### V05S-02 — understanding begins with studying another person's chosen texts

After the failed first visit, Saku buys roughly twenty light novels Kenta mentioned, recognizes his own intrusive position, and hypothesizes that a first betrayal may be especially devastating `[V05S:p-0041#p0003-p0051]`. The preparation is genuine perspective-taking but remains Saku-authored intervention.

Saku and Yua share convenience-store drinks at the river because cafes are not ubiquitous in Fukui `[V05S:p-0041#p0033-p0036]`. Ordinary locality becomes a place where interpretation is shared rather than performed to an audience.

### V05S-03 — Yuko's hero/person problem is visible in Volume 01

After Kenta exits his room, Saku plans his glasses and next presentation step but insists that Kenta's courage belongs to Kenta `[V05S:p-0042#p0003-p0027]`. When Yuko recognizes Saku's vague old “biography” as personal history, he withholds it because he expects her to turn pain into a flattering hero narrative and absolve him `[V05S:p-0042#p0040-p0068]`.

This materially historicizes the concern he voices at the Volume 05 refusal: the fear that Yuko loves the heroic role more than the person was not invented to evade her confession. It does not prove that his judgment is complete or that her love is false. Yuko's wish for future mutual disclosure, complaint, and argument is itself counterevidence `[V05S:p-0042#p0074-p0084]`.

### V05S-04 — care can preserve the recipient's face

Saku gives an umbrella to a distressed first-year and calls it a self-interested excuse to share Yua's, allowing the recipient to accept help without debt `[V05S:p-0044#p0024-p0037]`. Yua then chooses present shared-umbrella time over buying a saxophone reed and makes that preference direct `[V05S:p-0044#p0039-p0055]`.

The scene supplies an early bounded Yua bid and a noncoercive care technique. It does not erase later failures of method in higher-stakes interventions.

### V05S-05 — finite time is foreshadowed inside ordinary play

At the river, Asuka and Saku share one earbud and a farewell/reunion song. Asuka asks about ten years ago and ten years ahead; Saku is no longer a professional-baseball aspirant, while her location, vocation, and possible marriage remain open `[V05S:p-0049#p0014-p0024]`. She teases that she might marry someone like him, he chases her, and he wishes the moment could continue `[V05S:p-0049#p0025-p0035]`.

The story gains meaning from later V03 departure evidence, but it also prevents departure from consuming Asuka's ordinary humor and play.

### V05S-06 — preference memory and return are ordinary recognition

Yuko narrates Saku's overt acts while Yua identifies Yuko's waiting support; Yuko grants that Yua's different method belongs to the same field of care `[V05S:p-0051#p0003-p0017]`. Saku later returns to the Starbucks where the confrontation occurred, finds Yua alone, and brings/switches to her preferred hojicha tea latte `[V05S:p-0051#p0032-p0056]`.

He recognizes possible loneliness without forcing Yua to explain it. The encounter strengthens initiated, ordinary Saku/Yua reciprocity while remaining below named love.

### V05S-07 — Yuzuki's own romantic theory is prospective evidence, not ground truth

Yuzuki thinks Haru can reach Saku's weakness while she can show him only her strongest self. She allows that Saku could become special but insists this cannot become ordinary love `[V05S:p-0052#p0003-p0016]`. She predicts that similarity prevents mutual choice and that Haru fits him because people love what they lack `[V05S:p-0052#p0023-p0030]`.

V02 later falsifies the prediction from Yuzuki's side. The story is therefore high-value historical evidence for how confidently she can misread a developing feeling. She also stops herself from demanding Haru's interiority and includes Haru in the photograph sent to Saku `[V05S:p-0052#p0044-p0049]`.

### V05S-08 — Haru's challenge protocol and Saku's preference for ambiguity predate Volume 05

Haru says she advised Yuzuki to consult Saku, distinguishing Yuzuki opening her heart to Haru from entrusting an important matter to him `[V05S:p-0053#p0044-p0050]`. She wants to defeat Yuzuki but not see Yuzuki lose. Haru asks Saku to accept if she ever challenges him, and he agrees `[V05S:p-0053#p0053-p0059]`.

This is an early form of the future-bid protocol stabilized in Volume 05. Saku's wish that their beautiful ambiguity continue `[V05S:p-0053#p0064-p0083]` shows that postponement is a durable desire, not only a response to Yuko's confession.

### V05S-09 — comic consent language still leaves an agency problem

Saku and Yuko use Kenta's broad “anything” promise to enlist him in an embarrassing underwear purchase. The scene is comic and comparatively low-stakes, but it remains counterevidence against treating generalized consent as consent to a specific method.

Yuko deliberately asks Saku's color and style preferences, then leaves with two bags—one for the decoy and one strongly implied to be for herself `[V05S:p-0054#p0027-p0048]`. This is early competitive and sexual self-presentation, not passive waiting.

### V05S-10 — female friendship is primary, and stasis can burden it

Yuko and Yua imagine a two-girl sleepover. Saku's narration calls them unique best friends and sisterlike, mutually considerate and trusting `[V05S:p-0058#p0029-p0043]`. When Yuko starts to ask about the person Yua likes, Yua stops the disclosure because Saku is listening and promises “next time” `[V05S:p-0058#p0044-p0052]`.

Saku suppresses the selfish wish that all three remain this way forever `[V05S:p-0058#p0053-p0060]`. The wish validates the present's value but also shows how the romantic structure can burden an independently valuable female friendship.

### V05S-11 — Haru's peer style does not erase gendered desire

Haru asks why Saku says neckties suit her better than ribbons. He calls the line embarrassment and an established “male-friend” convention; both then acknowledge mutual attractiveness `[V05S:p-0059#p0014-p0034]`. Saku explicitly says the peerlike ease is attractive without eliminating his perception of Haru as a girl `[V05S:p-0059#p0038-p0041]`.

Her wish to hit baseballs to clear her head and his replacing the tie make it both authentic style and a boundary she may sometimes want loosened `[V05S:p-0059#p0042-p0059]`. Tomboy directness is neither a complete identity nor a disguise to discard.

### V05S-12 — Yuko sees strain and provides relief without demanding disclosure

Yuko demands compensation for Saku's two weeks as fake boyfriend, but the arcade trip becomes her way of noticing and easing his lingering strain `[V05S:p-0060#p0003-p0064]`. Saku wins her a dog plush; their pet-role banter lets her ask after him and seek affection indirectly `[V05S:p-0060#p0047-p0075]`.

He again wishes the present could remain unchanged, even if that wish is someone's dependence or weakness, then buys the plush a companion so it will not cry alone `[V05S:p-0060#p0076-p0080]`. Yuko, loneliness, responsive care, and Saku's stasis desire are linked well before Volume 05.

### V05S-13 — the cap story is a revised witness, not a duplicate event

The Special Edition republishes the event previously admitted through the separate V03 booklet. After Unicode and punctuation normalization, the earlier narrative has 1,609 characters and the Special Edition 1,728, with seven non-equal edit blocks. Several are orthographic, segmentation, or minor location edits. Two additions are interpretively material:

- Yuzuki moves close and smells around Saku's cheek, lips, and ear before joking about whether Asuka rejected him `[V05S:p-0061#p0039-p0046]`;
- when she calls the cap gesture an overwrite, she now identifies its object as `記憶`, and Saku answers with an electromagnetic-wave joke `[V05S:p-0061#p0051-p0060]`.

The earlier booklet's omission of the object is an edition fact, not a continuing ambiguity in this later wording. `記憶` narrows the target to memory but does not prove one exhaustive memory-content referent. The creator's Volume 03 note also says the continuity from this cap story to later “remove the tie” and “forever / next time” language was not consciously planted as foreshadowing `[V05S:p-0064#img01]`. Treat the pattern as retrospective continuity, not proof of advance authorial planning.

### V05S-14 — Asuka converts a childhood signal into present choice

On the V03 escape morning, Saku touches his left ear, activating their childhood escape signal; Asuka is overwhelmed that he remembered `[V05S:p-0063#p0003-p0014]`. Her preparation includes two unused blue underwear sets, ink blue and the blue moon of their childhood night, which she had saved for an ordinary happy day `[V05S:p-0063#p0030-p0042]`.

She leaves her parents a note, sees the sleeping boy in the park as nostalgic and beloved, and nevertheless shifts from the childhood `朔兄` in thought toward the present relation as the adventure begins `[V05S:p-0063#p0043-p0052]`. The escape is not simple restoration of childhood.

### V05S-15 — Haru's attraction precedes the pool scene

Immediately after the pool-cleaning assignment, Yuko offers to replace Haru so Haru can practice and Yuko can be alone with Saku. Haru refuses with a reason she immediately recognizes as false `[V05S:p-0067#p0012-p0027]`.

She contrasts Yuko's conventionally feminine beauty, scent, warmth, and directness with herself, then admits she was already anticipating the cleaning and felt guilty about wanting it `[V05S:p-0067#p0028-p0039]`. The later pool encounter intensifies and clarifies attraction; it does not create it from nothing.

### V05S-16 — Asuka enters the baseball field despite distance

Asuka accidentally sees Saku practice and feels both exhilaration and grief: she was not the person who relit him and, as a senior, nearly missed the classmates' opportunity to help `[V05S:p-0069#p0017-p0030]`. She enters anyway because she has chosen to face the remaining nine months with everything she has `[V05S:p-0069#p0032-p0034]`.

Haru later says she found her answer. Asuka recognizes Haru's direct heat, briefly resents the sun/moon fit, then reasserts her own story and wish to write the last page `[V05S:p-0069#p0038-p0057]`. Rivalry neither erases agency nor guarantees romantic victory.

### V05S-17 — Yuzuki refuses spectatorship and makes rivalry explicit

During the decisive girls' game, Yuzuki is angry at Mai, Haru's tunnel vision, Saku's attention to Haru, and above all her own passivity `[V05S:p-0070#p0003-p0032]`. She and Haru name the start of their own match, and Yuzuki recognizes Haru as the one sun she truly acknowledges `[V05S:p-0070#p0036-p0055]`.

Yuzuki wants a fair contest precisely because Haru taught her striving and helped the man who had helped her. She discloses her prior kiss with Saku as an opening move `[V05S:p-0070#p0056-p0063]`. Friendship, gratitude, and competition coexist rather than cancel one another.

### V05S-18 — Yuzuki/Haru partnership supplies a pre-romantic relational grammar

In first-year autumn, Yuzuki rejects an attractive athlete because he does not know her. She truthfully invokes an admired partner—Haru—and thinks that “our beloved man” is present, while denying that her interest in a Saku-like peer can become love because similarity should create only calm `[V05S:p-0074#p0003-p0041]`.

In the locker room, Yuzuki distinguishes several genuine but partly strategic social modes. Haru diagnoses that Yuzuki wants someone who possesses all she has plus what she lacks and would not love someone easily won over `[V05S:p-0074#p0079-p0139]`. Their underwear wager converts Haru's embarrassment into an agency-preserving request for Yuzuki's instruction `[V05S:p-0074#p0142-p0150]`.

Captain Kei predicts Yuzuki may someday accept becoming calculating or needy to pursue a man `[V05S:p-0074#p0154-p0160]`. Yuzuki's imagined future partner resembles Haru; Haru's imagined future partner resembles Yuzuki `[V05S:p-0074#p0174-p0176]`, `[V05S:p-0074#p0311-p0317]`. Their partnership is an affirmative relational model, not romantic-rival scenery.

Kei also warns that they may one day contest something neither can yield, but should fight as the same Yuzuki and Haru until satisfied `[V05S:p-0074#p0189-p0200]`. When they meet Saku, Haru resents his post-baseball mask yet believes she lacks standing to ask what happened. Yuzuki reads the situation, creates a graceful exit, and later interprets Haru's pursuit/admiration as almost love `[V05S:p-0074#p0233-p0308]`.

The reciprocal closing thanks and explicit claim that first-year Haru still does not know love `[V05S:p-0074#p0309-p0317]` make later love a revision in self-knowledge and relationship, not merely an always-complete truth waiting to be confessed.

## 5. Cross-story findings

### S05S-F01 — Saku's wish for stasis predates the Volume 05 crisis

**Class:** FACT + INFERENCE
**Confidence:** high

Saku wishes the Yuko/Yua domestic arrangement could remain forever `[V05S:p-0058#p0053-p0060]`, wants the Yuko arcade rhythm to persist even if the wish reflects dependence or weakness `[V05S:p-0060#p0076-p0080]`, and earlier wants the Haru ambiguity to continue `[V05S:p-0053#p0064-p0083]`. Volume 05 therefore exposes a durable strategy: finite present forms are beautiful partly because they postpone adjudication.

That desire is not wholly cowardly. It preserves genuinely valuable ordinary relations. Its cost is that other people must eventually force transitions he would prefer not to name.

### S05S-F02 — Yuko's hero/person conflict has long mutual evidence

**Class:** FACT + REVISION
**Confidence:** high

Saku's Volume 01 refusal to disclose his past because Yuko might mythologize and absolve him materially strengthens the historical basis of his Volume 05 concern `[V05S:p-0042#p0040-p0068]`. Yuko's independent perception of his strain and her non-demanding arcade care prevent that concern from becoming a total model of her `[V05S:p-0060#p0054-p0065]`.

Current formulation: Saku detects a real asymmetry in how Yuko reads his heroic role, but he underestimates her capacity to see ordinary distress and care without extracting a confession.

### S05S-F03 — Haru's Volume 05 protocol is a repeated, maturing form

**Class:** FACT + REVISION
**Confidence:** high

Haru had already asked Saku to accept a future challenge in a V02-associated story `[V05S:p-0053#p0053-p0059]`. Her attraction also precedes the V04 pool scene `[V05S:p-0067#p0028-p0039]`. Volume 05's future consent protocol is thus neither sudden nor merely deferred confession; it is the matured form of a long challenge idiom.

### S05S-F04 — Yuzuki's theories are authored maps subject to revision

**Class:** FACT + INFERENCE
**Confidence:** high

First-year and V02-associated Yuzuki repeatedly predicts that similarity prevents love `[V05S:p-0074#p0122-p0125]`, `[V05S:p-0052#p0023-p0030]`. Her later named love falsifies that account. The error does not make her insight worthless: she correctly identifies similarity, performance, and Haru's distinct access, but overstates her ability to forecast her own development.

### S05S-F05 — Yuzuki/Haru is an independently primary relationship

**Class:** FACT + INFERENCE
**Confidence:** high

Their partnership predates named romantic feeling, supplies reciprocal recognition and practical care, tolerates direct contest, and becomes the language through which each imagines a worthy partner. Later competition over Saku is continuous with this relationship, not evidence that friendship was decorative or false.

### S05S-F06 — female friendship and romantic rivalry are structurally intertwined

**Class:** FACT + INFERENCE
**Confidence:** high

Yuko/Yua are independently best friends `[V05S:p-0058#p0029-p0052]`; Yuzuki/Haru are partners and fair rivals `[V05S:p-0070#p0036-p0063]`; Asuka and Haru recognize one another across distance and competition `[V05S:p-0069#p0038-p0057]`. No pair is reducible to a mechanism for delivering Saku's romance. Yet shared desire creates real burdens and withholding. “Friendship survives rivalry” is too static; friendship provides the norms by which rivalry becomes bearable.

### S05S-F07 — ordinary locality is relational infrastructure

**Class:** FACT + INFERENCE
**Confidence:** high

Convenience-store drinks by the river, Happiring, Hachiban Ramen, Route 8, Elpa/JINS planning, Starbucks scarcity, the batting center, and the European-ken/grandstand area do not merely decorate a generic romance. They distribute meetings, travel, memory, care, and chance discovery across a materially specific Fukui network.

## 6. Frozen-main claim audit

| Frozen claim / test | Supplemental result | Current formulation |
|---|---|---|
| Regular V05 establishes no couple and does not identify Saku's unnamed girl | `PRESERVE` | the booklet adds older directional evidence but no new post-refusal identification or reciprocal commitment |
| Saku's refusal of Yuko may partly protect his role | `STRENGTHEN / QUALIFY` | his concern has Volume 01 precedent; Yuko also demonstrates ordinary recognition that his model undercounts |
| Haru's future bid is a bounded protocol rather than present couple status | `STRENGTHEN` | the protocol grows from an earlier challenge agreement and long pre-confession attraction |
| Yuzuki's self-advocacy remains indirect but real | `STRENGTHEN / HISTORICIZE` | cap, photograph, contest, kiss disclosure, and partnership show a long repertoire of performed bounded bids |
| Yua's care is chosen and non-extractive | `STRENGTHEN / QUALIFY` | early preference, social interpretation, and Saku-initiated ordinary return are added; her romantic interiority remains open |
| Asuka's finite summer is deliberate practice rather than passive delay | `STRENGTHEN / HISTORICIZE` | she repeatedly knows time is finite and chooses entry, escape, and ordinary play |
| Female friendships are independently meaningful | `STRENGTHEN / PROMOTE` | Yuko/Yua and Yuzuki/Haru now have direct dyadic history, norms, and future-bearing conflict grammar |
| V03 cap story's overwrite object is open | `REVISE BY EDITION` | it remains open in the earlier witness; the V05 Special Edition explicitly says `記憶`, without specifying one exhaustive memory-content referent |

The prospective Volume 01–05 artifacts are not edited. These dispositions belong to the current rolling model and revision ledger.

## 7. Rival readings and hard limits

### “Because these stories are set earlier, they prove the earlier freezes were wrong”

**Rejected.** The freezes record what the then-admitted source boundary supported. Later publication/acquisition can revise the current model without falsifying the historical procedure.

### “The Special Edition identifies Saku's unnamed Volume 05 girl”

**Unsupported.** The booklet contains earlier directional attraction and intimacy but no post-refusal identification. It establishes no couple.

### “The Yuko hero/person issue proves her love is false”

**Rejected.** Saku's fear has precedent, but Yuko also notices ordinary strain, offers relief, and imagines mutual disagreement. The evidence supports partial misrecognition, not absence of love.

### “Yuzuki and Haru's partner symmetry means their relationship is secretly romantic”

**Unsupported.** The story calls them partners and has each imagine a future man with the other's qualities; both explicitly say they do not yet know love. The evidence establishes relational primacy and formative symmetry, not a mutually named romance.

### “Every bonus event was planned foreshadowing”

**Rejected.** The creator note explicitly describes at least the cap/tie/forever sequence as unconscious or retrospective continuity `[V05S:p-0064#img01]`.

### “The compilation can be treated as one clean canonical text”

**Rejected.** It contains a text-equivalent main duplicate, differently timed stories, a revised prior witness, new fiction, creator commentary, profiles, dividers, and advertising. Claim authority depends on component class.

## 8. Supplemental checkpoint and safe next operation

The Volume 05 Special Edition is fully disposed at this boundary:

- exact object identity and integrity: verified;
- regular-main duplicate: compared and excluded from double-counting;
- 18 fiction components: inventoried, read, classified, and individually placed;
- revised V03 cap story: modeled as an edition variant of one shared event;
- creator commentary, visual dividers, profiles, colophon, and advertising: audited and routed by class;
- regular V05 main freeze: preserved without retroactive rewriting;
- Volume 06+ evidence: unopened.

The safe horizon is now:

```yaml
H_main: V05_REGULAR_MAIN
H_supp:
  - V03_IN_EPUB_BIRTHDAY_BONUS__BONUS_FICTION
  - V03_ILLUSTRATION_SS_BOOKLET__SUPPLEMENTAL_MAINLINE
  - V05_SPECIAL_EDITION_18_STORY_BOOKLET__COMPONENT_ROUTED_SUPPLEMENTAL_MAINLINE
H_next: V06_MAIN
```

The next permitted source operation is verification and prospective reading of the exact locked Japanese Volume 06 main EPUB.
