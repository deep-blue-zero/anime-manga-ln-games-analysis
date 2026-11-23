---
title: "FX Fighter Kurumi-chan — Character qualification at the V01–V10 boundary"
artifact_id: FX_KURUMI_CHARACTER_QUALIFICATION
artifact_type: character_qualification_audit
series: fx-fighter-kurumi-chan
version: "1.0"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Gate G2 person qualification under initiation policy §5.5.1: subject IDs, name forms, boundaries, outcomes, rationale and gaps, review triggers and intended monograph paths for every person with differentiated evidence in V01–V10"
source_boundary: "Accepted V01–V10 boundary (FXK-JP-V01-W01 to FXK-JP-V10-W01); V10 unit-end knowledge; no later volume"
created: 2026-11-23
last_updated: 2026-11-23
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
synthesis_id: FXK-SYN-20261123-V01-V10
snapshot_commit: bfeede591b04c2652e8cbbba14c1782e8a94f877
recommended_reasoning_class: DEEP_SYNTHESIS
---

# FX Fighter Kurumi-chan — Character qualification at the V01–V10 boundary

This record is the person qualification of gate G2 in the retrospective synthesis FXK-SYN-20261123-V01-V10. It assesses every person with differentiated evidence in the ten accepted volumes of the Japanese collected manga **FX戦士くるみちゃん** (原作 でむにゃん, 作画 炭酸だいすき) under initiation policy §5.5.1. It assigns stable subject IDs, records the name forms the pages use, decides an outcome for each subject, and names the monograph each qualified subject is owed in gate G3. The [decision and evidence ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md) carries the compact, mutable record of each outcome in its "Person-level qualification" section; this audit carries the arguments. The [synthesis architecture](../FX_KURUMI_SYNTHESIS_ARCHITECTURE.md) defines the gates, the [role-gap audit](FX_KURUMI_ARCHITECTURE_ROLE_GAP_AUDIT.md) the studies and the monograph duties, and the [source-completion and longitudinal reconciliation](FX_KURUMI_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md) the reconciled figures, claim states and usage rules this record relies on.

Inputs: the ledger's person section and claim rows, the readings' sections H (character evidence) and I (relationships) as the ledger cites them, the frozen entering states and checkpoints, and pages re-opened where an ID's order or a contested reading depended on them (section 8). The principal integrator wrote the assessments independently, then reconciled them with the character specialist's qualification recommendations, the financial specialist's evidence and the independent reviewer's diagnostics and challenges, verifying each adopted point against an accepted record or a re-opened page.

Result: twenty-one subjects receive IDs. Eight are QUALIFIED_PENDING and create an obligation to write a monograph in G3 (FXK-P001, FXK-P002, FXK-P003, FXK-P005, FXK-P006, FXK-P008, FXK-P020, FXK-P021). Thirteen are DEFERRED_EVIDENCE. No subject is COMPLETE_AT_BOUNDARY, because no monograph exists; none is REASSESS_AFTER_REVISION. Anonymous one-volume figures are assessed in group lines (section 4).

## 1. Rules applied

### 1.1 Assessment boundary and evidence

Every assessment uses one boundary: the V01–V10 main narrative of the ten witnesses FXK-JP-V01-W01 to FXK-JP-V10-W01, ending at V10 i0156 (present time Monday 24 April 2017). Nothing after i0156 is narrative evidence. Paratext that refers to persons (under-jacket boards and design notes in several volumes, flap comments, afterwords, bonus strips; the register classes each one) is classified only and is never evidence for a person, a motive or design intent. No knowledge from outside the admitted pages is used.

### 1.2 Who receives a subject ID, and in what order

A stable subject ID (FXK-P001, FXK-P002, …) is assigned to:

- **(a)** every person the pages name, however briefly. A person known only by a screen name counts as named when the account acts toward a subject on the page (a reply or message). Two exclusions: screen names that appear only in a feed or a list go to the group lines; a public office-holder named only in expository narration of market events is recorded with the unnamed office-holders and is not a qualification subject (section 5).
- **(b)** every unnamed person to whom the ledger's person section gives an entry of its own (Mebuki's parents; Mochiko's mother, grandmother and the bespectacled man of her flashback). An entry of its own is the run's record that the person's relation to a subject was tracked across scenes. Unnamed figures recorded only inside a "Minor figures (Vnn)" entry are assessed in group lines whatever the weight of a single act; their acts are recorded there and feed the studies. This decides alike the V06 salon customer, Inago's mother and the V05 fan who outs Yasuko.

IDs follow the order of first identifying appearance: the first occurrence at which the page identifies the person by name, name box, kin term or a unique description, whether the person is drawn, speaking or referred to as an individual. An appearance joined to the identifying one by continuous depiction within the same sequence counts. An earlier appearance that is identified only retrospectively, by analytic inference of any grade or by a later volume, is recorded in the subject's record but does not move the ID. Ties on one occurrence follow the reading order (panels right to left, top to bottom) of the first panel in which each person is identified; within one panel, a person who is drawn precedes a person who is only referred to, and persons only referred to in one piece of lettering follow the order of that lettering. The tie decisions are recorded where they apply (FXK-P002 and FXK-P003; FXK-P010 and FXK-P011; FXK-P014 and FXK-P015).

IDs are permanent. A later boundary appends the next free ID (FXK-P022 onward) and never renumbers.

### 1.3 Outcome vocabulary and test

The §5.5.1 vocabulary is used: QUALIFIED_PENDING, COMPLETE_AT_BOUNDARY, DEFERRED_EVIDENCE, REASSESS_AFTER_REVISION. Qualification needs (1) convergent evidence, across volumes or in one concentrated sequence; (2) meaningful variation across contexts or interlocutors; and (3) constraints or counterexamples that rule out a generic sketch. Prominence, page count and plot weight do not decide. Qualification is an evidential judgment and creates a production obligation: the character layer is not complete while a qualified subject lacks a monograph.

A qualified outcome changes only on evidence. If a G3 or G4 finding shows that the accepted evidence does not support a differentiated portrait of a qualified subject, the record moves to REASSESS_AFTER_REVISION and the outcome is decided at the next integration with the finding named. Difficulty in writing a monograph is not such a finding.

### 1.4 Monograph naming rule

The intended monograph path is `characters/<subject>-manga.md` under the project root, where `<subject>` is the lowercase ASCII kebab-case romanization of the fullest name the pages establish for the person within the boundary, in the order printed (family name first for Japanese names), in modified Hepburn without macrons (ū → u, ō → o) and without honorifics. A name component established only by analyst inference is not used unless the pages print it for that person elsewhere, or print it for a person whom the ledger identifies with the subject at INFERENCE HIGH or above; the monograph's identity section then states the inference. Examples: 福賀くるみ → `fukuga-kurumi`; 善波なな → `zenba-nana`. The path is written as plain text and is replaced by a link only when an accepted monograph exists.

### 1.5 Rules carried into every monograph

Each rule is tied to an accepted record; the reconciliation audit (sections 4.11 and 9) holds the figure and age usage rules.

- **Names and knowledge boundaries.** あふぃちゃん until V02 i0074, Yasuko after; the mother is "Kurumi's mother" for V01–V05 events and Kozue (梢) from V06 i0065, with the earlier concealment stated; the father's given name 郁夫 only with INFERENCE HIGH; "Nana" as the reference form for 善波なな (ばなな and Zenba recorded once). The V01 possessions lettered "Yasuko" are cited as lettering, never as identification.
- **Development and late revelation kept apart.** Mochiko's history (V05), Kozue's journal (V06), the father's account of the 300万 as saved for Kurumi (V09 i0074), Kurumi's account of greed since childhood staged by re-presenting a childhood beach memory with the winged figure added (V09 i0031; the V05 memory at i0161 has none; INFERENCE MODERATE-HIGH that it is the same memory) and Yasuko's 2013 origin (V10) re-read earlier pages: they are disclosure, not change.
- **Directed relationships dated.** Each state of a tie is given its volume; none is projected forward or back (for example Mochiko → Kurumi: private contempt V01; an inner account of use as the tie's origin, V07; force and care V08; employer and friend V09).
- **Ordinary conduct as well as crisis.** Kurumi's cooking, convenience-store work and 山口さん's recipes, sleeping at the office (V10 i0007); Mochiko's goods, cat, first game and company; Mebuki's Kansai speech at home and standard speech outward; Yasuko's brand dream, manga career and teaching of Nana.
- **Safety and labels.** No method, method step or item for the V08–V09 crisis; Kozue's death described as suicide without the V01 caption's detail; no clinical labels ("repeated chart-checking", never "compulsive"); psychological concepts are explanatory models, never diagnoses.
- **Intimate dimension.** Marked UNTESTED for each subject where the page does not test it, never filled.
- **Real persons.** The writer and the artist are named or referred to by role, or as they/them.

## 2. Roster

"Intended monograph path" names no document yet; the self-containment and fidelity results are decided separately in G4 (initiation §5.5.1), and the ledger's table repeats them.

| ID | Person | Name forms on the page, and where each is established | First identifying appearance | Ledger entry (base line) | Outcome | Intended monograph path (no document yet) | Self-containment | Fidelity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FXK-P001 | 福賀くるみ (Fukuga Kurumi) | くるみちゃん (a classmate, V01 i0007); 福賀くるみ (caption, V01 i0008); くるみ; 狂人(くるみ) as Mochiko's private label (V04 i0081); 「破産者 福賀 くるみ」 (V09 i0104) | V01 i0007 (the cold-open figure of i0003 is identified with her only by later analysis) | L2420 | QUALIFIED_PENDING | `characters/fukuga-kurumi-manga.md` | pending G4 | pending G4 |
| FXK-P002 | Kurumi's father (福賀; 郁夫 by INFERENCE HIGH) | ぱぱ (door sign, V01 i0010); お父さん, 父さん; 「郁夫(いくお)さん」 for Kozue's husband (V06 i0062, i0064, i0071, i0082); 「福賀さん」 (a colleague, V09 i0062) | V01 i0010 P1 (door sign 「ぱぱとままのへや♡」; ぱぱ precedes まま in the lettering); present from i0031 | L3040 | QUALIFIED_PENDING | `characters/fukuga-ikuo-manga.md` | pending G4 | pending G4 |
| FXK-P003 | 福賀梢 (Fukuga Kozue), Kurumi's mother | まま (same door sign, V01 i0010); お母さん, ママ (V01–V02); 梢(こずえ) (V06 i0065); "くるみの母・梢" (V06 i0066); 「福賀 梢 様」 (passbook, V06 i0075) | V01 i0010 P1 (door sign); drawn P2 | L2998 | QUALIFIED_PENDING | `characters/fukuga-kozue-manga.md` | pending G4 | pending G4 |
| FXK-P004 | 山口さん (Yamaguchi) | 山口さん (V01 i0049, in comparison; V08 i0079, in memory; V09 i0107, in speech); the V05 co-worker (i0083–i0084), the V07 convenience-store worker (i0076–i0077) and the V09 vignette co-worker identified at INFERENCE MODERATE-HIGH | V01 i0049 | L3276; V07 minor entry L3329 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P005 | 小金萌智子 (Kogane Mochiko) | 小金萌智子, "(20)【大学三年生】" (V01 i0058); もちこ (Kurumi's phone entry); "ともこ" (her comment name, V02 i0011); 萌智子先パイ (Mebuki's envelope, V05 i0144); 【代表取締役 社長】 of (株)もちもち企画 (V09 i0143) | V01 i0058 | L2663 | QUALIFIED_PENDING | `characters/kogane-mochiko-manga.md` | pending G4 | pending G4 |
| FXK-P006 | 山師芽吹 (Yamashi Mebuki) | 芽吹 (named offstage, V01 i0066); 山師芽吹, "(20)【大学三年生】" (V02 i0004); 若葉 (stage name on a salon profile, V04 i0146) | V01 i0066 (named); on the page from V02 i0004 | L3101 | QUALIFIED_PENDING | `characters/yamashi-mebuki-manga.md` | pending G4 | pending G4 |
| FXK-P007 | 優子 (Yūko) | 優子ちゃん (Kurumi's thought, V01 i0143); the 2008 classmate of V01 i0021 identified with her at INFERENCE MODERATE-HIGH (FXK-V01-C008) | V01 i0143 | L3089 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P008 | 高根やす子 (Takane Yasuko), handle あふぃちゃん | 「HN:あふぃちゃん(20)【ブロガー】」 (V01 i0144); 「あふぃちゃん改め 高根やす子(20)【フリーター】」 (V02 i0074); やす子; 「FX堕天使あふぃちゃん」 (her 2013 self-name, V10 i0079); 【漫画家】 (V09 i0142) | V01 i0144 | L2867 | QUALIFIED_PENDING | `characters/takane-yasuko-manga.md` | pending G4 | pending G4 |
| FXK-P009 | Mebuki's mother (unnamed) | "お母さん" (Mebuki, V03 i0027); "母より" (V04 i0010) | V03 i0027 | L3238 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P010 | Mebuki's father (unnamed) | drawn at the family table (V03 i0028 P1, first in reading order) | V03 i0028 | L3258 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P011 | 健斗 (Kento), Mebuki's younger brother | drawn at the family table (V03 i0028 P1); "ねーちゃん" (his line, i0029); 健斗 (ruby けんと, i0074) | V03 i0028 | L3267 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P012 | 千佳ちゃん (Chika) | 千佳ちゃん, a neighbour's daughter (the mother's line, V03 i0029) | V03 i0029 | L3289 (Minor figures V03) | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P013 | よしあき@漫画評論家 (screen name) | "よしあき@漫画評論家" (a reply to Yasuko, V03 i0156; replies again V04 i0039–i0040) | V03 i0156 | L3289, L3292 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P014 | Mochiko's paternal grandmother (unnamed) | an elderly woman seeing Mochiko off (V05 i0003, drawn and speaking); おばーちゃん | V05 i0003 (drawn speaker; precedes the person named in her balloon) | L3308 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P015 | Mochiko's mother (unnamed) | "お母さん" (the grandmother's line, V05 i0003); drawn from i0006 | V05 i0003 | L3300 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P016 | The bespectacled man of Mochiko's flashback (unnamed) | none in the story; addresses Mochiko as "娘さん" | V05 i0006 | L3303 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P017 | 増尾先生 (Masuo) | 増尾先生 (named once, V05 i0011) | V05 i0011 | L3315 (Minor figures V05) | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P018 | 毒島☆寿美 (Busujima Hiromi) | business card, editor at コミックプラッパー (V05 i0124); a cabaret card (i0140) | V05 i0124 | L3315 (Minor figures V05) | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P019 | 酒田いなご (Sakata Inago) | name box "酒田いなご (21)【短大卒 新社会人】" (V09 i0134); いなご, いなごちゃん | V09 i0133 | L3344 | DEFERRED_EVIDENCE | none | not applicable | not applicable |
| FXK-P020 | 善波なな (Zenba Nana) | name box 善波なな (V09 i0149); 善波さん (Mochiko, i0149); ばなな (Yasuko, i0150; "ばなな先輩", Inago, V10); 「ばなな @nana_mei_luv」 with a banana emoji (her fan account, V10 i0082) | V09 i0148 (the silhouette of V09 i0110 is identified with her only by V10) | L3368 | QUALIFIED_PENDING | `characters/zenba-nana-manga.md` | pending G4 | pending G4 |
| FXK-P021 | 月森きずな (Tsukimori Kizuna) | "きずなさん" (Kurumi, V09 i0157); name box 月森きずな, 27, 【営業】 (i0158); "月森さん" (Nana); "きずな先輩" (Inago) | V09 i0152 (drawn; named in the same sequence) | L3395 | QUALIFIED_PENDING | `characters/tsukimori-kizuna-manga.md` | pending G4 | pending G4 |

Ledger entries are append-only and correct as dated records, but several must be read with care: the person-section headings still read "Mother (unnamed)" (L2998) and "Father (unnamed)" (L3040), although V06 names 梢 and, for the father, 郁夫 at INFERENCE HIGH; the 山口さん entry records "does not appear" for V07 (L3276–L3286) while the V07 minor-figure entry (L3329) holds the worker later identified as 山口さん; the Mebuki (L3101) and 優子 (L3089) entries open with a V01 "Not eligible" line; the Kurumi entry's opening line uses a clinical-sounding phrase for her chart-checking (L2422) that later reconciliations removed elsewhere. The ledger's qualification table states the current names, the merged identity and the current outcome of each subject. Line numbers are those of the base snapshot.

## 3. Subject records

Every record uses the boundary of section 1.1. "Sufficiency" quotes the ledger's per-volume evidence-sufficiency labels.

### FXK-P001 Fukuga Kurumi

- **Subject.** FXK-P001, 福賀くるみ. Name forms and where established: section 2. Third-year from April 2014 and 21 by November 2014 (FXK-V05-C064); 23 in April 2017 (V09 i0152).
- **Boundary.** V01–V10 main narrative; present in every volume.
- **Outcome.** QUALIFIED_PENDING (confidence HIGH).
- **Rationale.** Sufficiency HIGH in every volume. (1) Convergence: ten volumes of decisions with printed figures (reconciliation audit, section 4.2), inner speech, the V08 crisis and the V09 restoration, read by independent roles and reconciled. (2) Variation: calm, euphoric, rationalizing and self-condemning cognition; distinct conduct with her father (concealment V01, assent without commitment V02, confession and refusal of his vow V09), Mochiko (trust, one lie, blame and clinging trust in V08), Mebuki (adviser, silent contrarian, refusal V04), Yasuko, her colleagues (V10) and her dead mother (identification, re-enactment, "似てるけど違う", V09 i0058, i0061). (3) Constraints and counterexamples: refusals of all-in and of a loan (V01 i0064–i0066); the refusal of Mebuki's 1,000,000 (V04 i0067–i0076); the 1,000,000 set aside for tax (V03 i0124); two realized loss-cuts made by hand, with no stop order shown (V06 i0013, i0046; the second closes a new short), later recast as mistakes (i0098–i0099); the declined second add (V04 i0115).
- **Largest gaps.** No trade of hers is shown after V08, so her V09 resolutions (FXK-V09-C030 "いつか"; FXK-V09-C032 "支配して コントロールしてみせる") are untested at V10; the purpose of taking her father's cash (V01 U-02; FXK-V01-C015) and the EUR/CHF entry (V06-U01) stay open; her residence, pay and remaining tax in 2017 (V10-U09; V10 i0045); the letter's fate (V09-U07); the V10 stock "study" (V10-U14). Her interior between V07's last page and V08's first deposit is short on the page.
- **Notes for the monograph.** Her V09 account of greed since childhood is self-understanding offered late, staged by re-presenting a V05 memory (section 1.5), not a change of disposition. Her failure to cut changes kind across the series (reconciliation audit, section 5.5 row 3). Her home is a flat in a two-storey block; the V01 detached-house frames are an art inconsistency (V04 reading, apartment re-inspected).
- **Review trigger.** Admission of any later volume; an accepted revision of a reading section about her; a G4 finding against the monograph.
- **Intended monograph path.** `characters/fukuga-kurumi-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P002 Father of Fukuga Kurumi

- **Subject.** FXK-P002, Kurumi's father: surname 福賀 (「福賀さん」, V09 i0062); given name 郁夫 by INFERENCE HIGH (「郁夫(いくお)さん」 is printed for Kozue's husband, V06 i0062, i0064, i0071, i0082, and his own V09 memory shows him as her husband, i0072). Name forms: section 2.
- **ID order.** He and FXK-P003 are first identified on the same panel, V01 i0010 P1, by the door sign 「ぱぱとままのへや♡」; ぱぱ precedes まま in the lettering (page re-opened, section 8). He is drawn in present time from V01 i0031.
- **Boundary.** V01–V10 main narrative; present-time scenes in V01, V02, V05, V07, V08 (one call) and V09; absent from present time in V03–V04 and V10.
- **Outcome.** QUALIFIED_PENDING (confidence MODERATE; the character specialist assessed LOW-MODERATE, the same outcome).
- **Rationale.** Sufficiency LOW-MODERATE (V01, V05–V08), MODERATE (V02–V04), MODERATE-HIGH (V09). (1) Convergence: two concentrated sequences, the V02 discovery (i0014, i0021–i0032) and the V09 confession, offer and settlement (i0062–i0098, i0122–i0123), with recurring traces between them (the transfer, V05 i0069; the departure, V07 i0030–i0031; the unanswered call, V08 i0035–i0036) and Kozue's account of him (V06). (2) Variation: anger, a slap and a bowed plea (V02); worry withheld (V05); a routine farewell (V07); relief, self-blame, a demanded vow withdrawn but opposition kept ("それでも俺はやめろと言うぞ 親としてな", V09 i0084); with a colleague (V09 i0062–i0066); as a husband in memory. (3) Constraints: his remembered "お金のことは全部俺に任せて / お前は家のことだけやってたらいいんだ" (V09 i0072) against his V09 support; the man who said needing borrowed money was failure (V02) offers his own 300万 for her bankruptcy (V09 i0074); "怒らないから" (V09 i0069) after the V02 slap.
- **Largest gaps.** Little direct interior (one narrator line, V08 i0035); whether he learns of the letter (V09-U07); when the returned cash was banked and whether it paid the costs (V09-U13, V09-U14); whether he knew of Kozue's losses before her death (V06-U09, advanced by his own "母さんのときは 相談もなかったからな…", V09 i0072).
- **Notes for the monograph.** A real change of stance between V02 and V09 (denial of her adulthood → acceptance of her freedom with his opposition kept), with the rival that the change is situational; his re-description of the 300万 as saved for her (V09 i0074) is a late revelation set against Kurumi's V01 surmise (V01 i0109); his knowledge states are dated by volume (discovery V02; the loss, debt and bankruptcy V09; never the letter). The identity section states the inference behind the given name.
- **Review trigger.** Any present-time scene in a later volume, especially his response if Kurumi returns to the market.
- **Intended monograph path.** `characters/fukuga-ikuo-manga.md` (naming rule, section 1.4). Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P003 Fukuga Kozue

- **Subject.** FXK-P003, 福賀梢, Kurumi's mother. Unnamed in V01–V05 ("お母さん", "ママ"); named 梢 at V06 i0065, "くるみの母・梢" at i0066 and 「福賀 梢 様」 on a passbook at i0075; 「母(故人)」 in V08. Dead since 13 February 2009 (accepted V01); her death is stated, never shown.
- **ID order.** Identified with FXK-P002 on V01 i0010 P1 (まま on the door sign, after ぱぱ) and drawn in P2.
- **Boundary.** V01–V10 main narrative. All evidence after V01 i0033 is retrospective or mediated (flashback, journal, memory, photograph, Kurumi's re-enactment).
- **Outcome.** QUALIFIED_PENDING (confidence MODERATE).
- **Rationale.** Sufficiency MODERATE (V01–V05), MODERATE-HIGH from V06. (1) Convergence: V01's 2008–09 scenes, V02 and V05 memories, the V06 flashback of 1998 and 2006–2008 (about 33 pages with decisions, figures and the journal's own voice; reconciliation audit, section 4.8), and her presence through photograph, voice, inset and memory in V07–V09, recorded by different readings and roles. (2) Variation: as a mother (warm, teasing, "くるみちゃん"), as a wife (concealment from her husband; objecting to his transfers in his memory, V09 i0072), as a daughter (her parents' cash taken, V06 i0077), as a trader (yen-carry, "バーゲンセール", household money, the 400× plan) and in the journal's plain hand. (3) Constraints: scepticism overridden (V06 i0060–i0064); "損切りしなければ勝っていた。でも損切りしないとダメらしい。" (i0087), self-knowledge set against her own acts; her husband's account that she did not consult him (V09 i0072) beside his own paternalism on the same page.
- **Largest gaps.** No 2009 scene; her parents' knowledge (V06-U09); the amounts of her 2006–2008 profits and pre-marriage savings; the ≈204,000 between the 6 October screen and the caption (reconciliation audit, section 4.8); the 「すみませんでした」 sheet of V08 i0042, whose first panel redraws the composition of her V01 i0030 note (pages re-opened in the synthesis; recall favoured at INFERENCE MODERATE only; status UNRESOLVED).
- **Notes for the monograph.** Her portrait arrives in three layers through three holders: a grieving fifteen-year-old's retrospective narration (V01), her own journal inside a flashback whose authority is partly the narrator's and partly her written self-report (V06 reading §L.7), and her husband's account (V09 i0072–i0073). The monograph keeps the layers apart, uses her self-reports with the reliability flag the V06 reading records (§F.10), follows the corpus's method-free recording of her death, and treats her as evidence in her own right, not only as Kurumi's mirror.
- **Review trigger.** Any later journal page or 2009 scene; admission of a later volume.
- **Intended monograph path.** `characters/fukuga-kozue-manga.md` (both components printed for her, V06 i0075). Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P004 Yamaguchi

- **Subject.** FXK-P004, 山口さん. The ledger opens the entry at V01 i0049, where the name is printed in a comparison beside Kurumi's convenience-store job; the name is printed again in a V08 memory (i0079: the recipes, "できなくてごめんね") and in Kurumi's V09 speech (i0107). Identity across appearances: the V07 convenience-store worker (V07 i0076–i0077; アタシ; "アレェ?福賀さんじゃん") is this person at INFERENCE MODERATE-HIGH (FXK-V08-C073, strengthened by FXK-V09-C063); the V07 worker is Kurumi's V05 co-worker (V05 i0083–i0084) at INFERENCE MODERATE-HIGH (ledger, V07 minor-figure entry); the V09 vignette co-worker at INFERENCE MODERATE-HIGH; the V01 namesake at INFERENCE MODERATE. No gendered pronoun is asserted from the pages (ledger, V09 line).
- **Boundary.** V01–V10 main narrative.
- **Outcome.** DEFERRED_EVIDENCE.
- **Rationale and gaps.** A few lines in five volumes; matters to Kurumi's ordinary life and work rather than as a portrait. Identity across volumes rests on inference, and no scene tests the person's choices, variation or constraints.
- **Review trigger.** A captioned appearance, or a scene of the person's own.

### FXK-P005 Kogane Mochiko

- **Subject.** FXK-P005, 小金萌智子. Name forms: section 2.
- **Boundary.** V01–V10 main narrative; present in every volume (V10: two present-time scenes and a memory image).
- **Outcome.** QUALIFIED_PENDING (confidence HIGH).
- **Rationale.** Sufficiency HIGH V03–V09 (MODERATE-HIGH V02; LOW in V10). (1) Convergence: the split between public speech and private thought from V01 (i0155–i0159) to V08, her figures (reconciliation audit, section 4.4), a biography (V05 第21話, about 70 pages), the V08 intervention and the V09 offer. (2) Variation: with Kurumi (teasing friend, silent witness V06–V07, rescuer V08, employer V09), Mebuki (adviser, creditor at 109.5%, concealed counterparty, confessor, V07 i0017), Yasuko (suspicion; confrontation, V05 i0129–i0139), her mother, grandmother and the bespectacled man (V05), her staff (V09–V10). (3) Constraints: no act exploiting Kurumi's vulnerability and no gain from her loss is shown (FXK-V07-C075, preserved in V10); she refuses to pay Kurumi's debt yet comes in person (V08 i0119, i0133–i0158); small kindnesses to Mebuki (V04); disgust at a gloating forum with "私もどちらかといえば蹴りたい側" (V07); her own question "私はいったい なにがしたかったんだろう…?" (V07 i0137–i0139).
- **Starting wording of her motive chain** (reconciliation audit, section 5.5 row 6). Toward Mebuki, use for advantage is SELF_REPORT HIGH (V03 i0150; V07 i0017). Toward Kurumi, a watching purpose and private contempt are SELF_REPORT HIGH (V01 i0155–i0159; V05 i0048), and Mochiko's own inner account names use as the origin of the friendship ("利用できると…思ったから 付き合っただけだ", V07 i0045, INFERENCE MODERATE-HIGH that it is unspoken; FXK-V07-C065); no act exploiting Kurumi's vulnerability and no gain from her loss is shown (FXK-V07-C075). Relish at a friend's plight is a V01–V03 private attitude that thins in V04 (i0109, i0145) and is absent from V05 on (FXK-V04-C031, FXK-V05-C052, FXK-V06-C057, FXK-V07-C061, FXK-V08-C063). Care-like acts run from V01 (i0116, i0119, i0155, i0162) and V04 (i0100, i0118, i0120) through V05 (i0108–i0112) to the costly V08 intervention and the V09 offer. The motive stays UNRESOLVED; each state is dated, and the V07 account describes how the tie began, not what it became (V07 reading §L, counterreading 8).
- **Largest gaps.** Her motive (FXK-V01-C005, extended through FXK-V09-C070, unsettled); the content of her "投資" (V08-U07; the V09 job offer is a completion at INFERENCE MODERATE); whether she held a position on 15 January (V07-U15); the source of her capital and her company's business (V09-U04); almost no V10 evidence.
- **Notes for the monograph.** V05's biography is a late revelation. Her mother's tie to the bespectacled man of the V05 flashback is a business dependence whose further character is unprinted (FXK-P016). Her tie with Kurumi is the spine of the series in both specialists' accounts; G4 applies a monograph-only probe to this monograph as well as to Kurumi's.
- **Review trigger.** Admission of a later volume; a G4 finding.
- **Intended monograph path.** `characters/kogane-mochiko-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P006 Yamashi Mebuki

- **Subject.** FXK-P006, 山師芽吹. Named offstage at V01 i0066; on the page from V02 i0004 ("(20)【大学三年生】"); 若葉 is her stage name on a salon profile (V04 i0146), an alias, not a second identity. Her "20" is printed at V02 i0004 only.
- **Boundary.** V01–V10 main narrative; ledger evidence before V02: none; absent after autumn 2015 (V10 does not show her).
- **Outcome.** QUALIFIED_PENDING (confidence HIGH).
- **Rationale.** Sufficiency HIGH V03–V07, MODERATE-HIGH V02 and V08 (flashback), MODERATE V09. (1) Convergence: the escalation from a 200,000 stake to the loss of all 3,600,000 of her FX deposits (reconciliation audit, section 4.5), with printed figures in V02–V07, her own words and inner voice. (2) Variation: Kansai speech inward and at home, polite standard speech outward, casual with Yasuko; with her family (concealment), Mochiko (trust, deception discovered, gratitude), Kurumi (admiration, envy and ill-wishes in V03, apology in V04), Yasuko (dismissal, reconciliation), at the salon; prompting Mochiko to act for Kurumi (V08 i0108–i0110). (3) Constraints: her own foreknowledge "これ借りてもきっとうまくいかへん" (V04); relief at liquidation and "案外ええもんやな" about work (V06); repayment near complete (V09 i0114); a restart in a domestic account with a swap rationale (V09 i0115–i0117).
- **Largest gaps.** Absent after autumn 2015; the amounts repaid and the interest paid are never printed; the rand position (V09-U06); what she told her parents (V06-U03); the claims about her own agency (FXK-V03-C001/C002, FXK-V04-C001/C002) are open pending their argument in G3 Study B.
- **Notes for the monograph.** She is not a closed cautionary tale (V09 i0114–i0117). She, Kurumi and Mochiko are all third-years in 2014, so her 先輩 marks investment seniority. Her salon work is never called sex work (V05-U19 open).
- **Review trigger.** Any reappearance in a later volume; the G3 decision on the agency claims.
- **Intended monograph path.** `characters/yamashi-mebuki-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P007 Yuko

- **Subject.** FXK-P007, 優子. Named only in Kurumi's thought "萌智子も 優子ちゃんも" (V01 i0143), as a current friend in 2014. The 2008 classmate who gives a sincere warning (V01 i0021) is this person at INFERENCE MODERATE-HIGH (FXK-V01-C008); that appearance is recorded here and does not move the ID (section 1.2). A V08 childhood memory (i0052–i0053).
- **Boundary.** V01–V10 main narrative.
- **Outcome.** DEFERRED_EVIDENCE.
- **Rationale and gaps.** Sufficiency LOW. No scene of her own after V01; no variation or counterexample.
- **Review trigger.** Any on-page appearance.

### FXK-P008 Takane Yasuko

- **Subject.** FXK-P008, 高根やす子, handle あふぃちゃん. Name forms: section 2. Knowledge boundary: in V01 she is only the handle (that Yasuko is her given name was then INFERENCE MODERATE-HIGH, FXK-V01-C009); she is named from V02 i0074; her blogger past stays hidden from the others until a fan outs her in V05 (i0110).
- **Boundary.** V01–V10 main narrative, including the V10 flashback to 2013.
- **Outcome.** QUALIFIED_PENDING (confidence HIGH; MODERATE-HIGH for interiority).
- **Rationale.** Sufficiency LOW-MODERATE (V01), MODERATE (V02), MODERATE-HIGH (V03–V04, V06–V07, V09–V10), HIGH (V05), LOW (V08). (1) Convergence: trader, quitter, manga artist and, in V10, the 2013 origin (i0066–i0079), across nine volumes. (2) Variation: the blogger persona (V01) against her guarded self; the only truth-teller to Mebuki (V03 i0141–i0142); her own responsibility claimed ("あたしの責任だよ", V04); confrontation and a demand for friendship with Mochiko (V05); the only spoken prompt to Kurumi to stop ("引き際…とかさ…", V06); the only direct question after the franc shock (V07 i0135); mentor to Nana (V10). (3) Constraints: she broke her own low-leverage creed on her first trade (V03); she could not object when told of the loan (V04 i0143); she rejects FX but holds shares (V10 i0090–i0092).
- **Largest gaps.** The origin of the 76,573 (V02-U05, advanced by the V10 flashback); her trading between December 2013 and V01; whether Mochiko registered the outing (V05-U22); her editor's identity and pen name (V10-U15); little interior in V08.
- **Notes for the monograph.** That she funded an account again after the 2013 liquidation is INFERENCE HIGH, not shown (the ledger's V10 note states it as shown); the 2013 liquidation did not end her FX (V01 as あふぃちゃん, V02's 76,573, the V03 contest). Her kanji 私 in asides (V03 i0088, i0093; V04 i0077, i0137) stays UNRESOLVED as an orthographic point (V04-U10); its location pattern is for the monograph to verify.
- **Review trigger.** Admission of a later volume.
- **Intended monograph path.** `characters/takane-yasuko-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P009 Mother of Yamashi Mebuki

- **Subject.** FXK-P009, Mebuki's mother (unnamed). Identified by Mebuki's "お母さんの声でかいねん!" at V03 i0027 (page re-opened); "母より" on a parcel note (V04 i0010).
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW-MODERATE.
- **Rationale and gaps.** A dinner scene and parcels with Kansai notes (V03 i0027–i0029, i0096; V04 i0010), calls (V06 i0005, i0044), the parents' opposition reported (V07 i0008). One relationship and no scene in which she learns of the FX or the debt. Her place in where the cost of Mebuki's choices lands is Study B material.
- **Review trigger.** Any scene in which she learns of the FX or the debt.

### FXK-P010 Father of Yamashi Mebuki

- **Subject.** FXK-P010, Mebuki's father (unnamed). Drawn at the family table at V03 i0028 P1, first in reading order (page re-opened); the lenient "学費くらい出したったらえぇがな…" (i0029).
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW.
- **Rationale and gaps.** One lenient line; asked for by Mebuki (V06 i0044), the content of that talk unseen.
- **Review trigger.** Any present-time scene.

### FXK-P011 Kento

- **Subject.** FXK-P011, 健斗, Mebuki's younger brother. Drawn at the family table at V03 i0028 P1 after the father in reading order; "どう考えてもねーちゃんには無理やろ!" (i0029); named with ruby けんと at i0074.
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW.
- **Rationale and gaps.** Teasing and "そろそろ進学" (V03 i0029, i0074); a vision (V04 i0107). No differentiated evidence.
- **Review trigger.** Any appearance.

### FXK-P012 Chika

- **Subject.** FXK-P012, 千佳ちゃん, a neighbour's daughter held up by Mebuki's mother as the model child (V03 i0029).
- **Outcome.** DEFERRED_EVIDENCE. Named once; no differentiated evidence.
- **Review trigger.** Any appearance.

### FXK-P013 Yoshiaki screen name

- **Subject.** FXK-P013, "よしあき@漫画評論家", a screen name whose account acts toward Yasuko: a reply advising cats over rabbits, rejected (V03 i0156); further replies (V04 i0039–i0040); a "よしあき" figure in an imagined panel (V04 i0148).
- **Outcome.** DEFERRED_EVIDENCE. No evidence beyond the replies.
- **Review trigger.** Any further post or appearance.

### FXK-P014 Grandmother of Kogane Mochiko

- **Subject.** FXK-P014, Mochiko's paternal grandmother (unnamed; おばーちゃん). Drawn and speaking at V05 i0003 P3 ("お母さん今日くらい来たらいいのにねぇ…"); as the drawn speaker she precedes the mother she names in her own balloon (tie rule, section 1.2; page re-opened).
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW-MODERATE.
- **Rationale and gaps.** Takes Mochiko in at twelve; sushi, mochi, "無理しちゃダメだよ?"; dies after the 平成24年度 exam (V05 i0003, i0020–i0040). One flashback sequence; a late revelation of Mochiko's history.
- **Review trigger.** None expected (deceased within the flashback); a later volume's further flashback.

### FXK-P015 Mother of Kogane Mochiko

- **Subject.** FXK-P015, Mochiko's mother (unnamed). Referred to by kin term at V05 i0003 P3; drawn from i0006.
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW-MODERATE.
- **Rationale and gaps.** Night work with drinking; absent from the 2006 ceremony; at the grandmother's funeral concerned with her own shame, demands money (V05 i0003, i0006–i0008, i0040–i0041); possibly the woman in Mochiko's V07 inner image (i0053, INFERENCE MODERATE). Flashback only.
- **Review trigger.** Any present-time appearance.

### FXK-P016 The bespectacled man of the V05 flashback

- **Subject.** FXK-P016, unnamed in the story: the man on whose business Mochiko's mother's work depends (accepted wording, FXK-V05-C003; V05 reading E001 and §H.1); his own job depends on her "売り上げ" (ledger, L3303). Whether the relation is also romantic, and where he lives, are not established (V05 checkpoint C-13).
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW.
- **Rationale and gaps.** Polite address ("娘さん"); humiliates Mochiko at a café and calls it "面白いもの"; his "他人の施し" and "友達" lines return in 2014 (V05 i0006–i0008, i0026–i0027; V05 E061). One flashback sequence.
- **Review trigger.** Any reappearance.

### FXK-P017 Masuo teacher

- **Subject.** FXK-P017, 増尾先生, named once (V05 i0011).
- **Outcome.** DEFERRED_EVIDENCE. No differentiated evidence.
- **Review trigger.** Any appearance.

### FXK-P018 Busujima Hiromi

- **Subject.** FXK-P018, 毒島☆寿美, editor at コミックプラッパー (business card, V05 i0124; a cabaret card, i0140).
- **Outcome.** DEFERRED_EVIDENCE. Sufficiency LOW-MODERATE.
- **Rationale and gaps.** Harsh, specific critique and encouragement to Yasuko in one sequence. Whether Yasuko's V10 editor is this person is not stated (V10-U15).
- **Review trigger.** An identified reappearance.

### FXK-P019 Sakata Inago

- **Subject.** FXK-P019, 酒田いなご, "(21)【短大卒 新社会人】" (name box, V09 i0134); いなご, いなごちゃん (Kurumi); クリエイター by her own word (V10 i0016).
- **Boundary.** V09–V10 main narrative.
- **Outcome.** DEFERRED_EVIDENCE.
- **Rationale (initiation §5.5.1 terms).** Sufficiency MODERATE in V09 and V10. Convergence is present: she is the viewpoint of 第45話 and 第46話 and appears in every V10 chapter, with some history (village, rejections, "何者にもなれなかった", V10 i0019). The variation is register within a single role, the newcomer: rustic with her siblings, humble at interview, polite at the office. The constraints the pages offer — her mother's warning (V10 i0034) and her own "勉強してから…" (i0040) — agree with the newcomer sketch rather than complicate it; her ties (admiration for Kizuna, being protected by her seniors) are not tested. The evidence does not yet support a differentiated portrait. She holds no account and places no order on the page; that is recorded as a gap, not used as the test.
- **Largest gaps.** Why she was hired (V09-U12); her work; any account or trade; what she counts at V10 i0123 (V10-U12). Fragile attribution: the thought "10万くらいの大損" (V10 i0044) is hers, not Nana's (V10 checkpoint C-01).
- **Review trigger.** A later volume in which she is focal again, or a scene that tests her outside the newcomer role.

### FXK-P020 Zenba Nana

- **Subject.** FXK-P020, 善波なな. Name forms: section 2. The NEET acquaintance of Yasuko at V09 i0110 (a silhouette) is identified with her only in V10 (V09-U15, resolved by her own "脱ニート", V10 i0088); that appearance does not move the ID.
- **Boundary.** V09–V10 main narrative, including the V10 flashback to 2013.
- **Outcome.** QUALIFIED_PENDING (confidence MODERATE; bounded V09–V10).
- **Rationale.** Sufficiency LOW in V09, HIGH in V10 (focal in 第48–50話). (1) Convergence: one concentrated sequence with a 2013 history (専門学校 with Yasuko, declining FX, witnessing Yasuko's liquidation, V10 i0067–i0079) and a complete, exactly reconciled money sequence (reconciliation audit, section 4.10). (2) Variation: office 敬語 and surnames; casual speech at home with her mother; menacing online and inner registers about fandom; a plea to Kizuna (V10 i0155–i0156). (3) Constraints: public caution and private fear of investing (i0038, i0060) before status-framed certainty (i0101, i0103); research before buying, a half-savings rule (i0132), cash shares; no averaging down at −8,000円 (i0145); a resolve to respect others' fandom (i0151).
- **Largest gaps.** Evidence comes almost wholly from V10; the Kani position after its first day and the カリフラワー plan face events after V10 (V10-U03, U04; NOT SCOREABLE); her household contribution (V10-U08); her rivalry with Kizuna unresolved.
- **Notes for the monograph.** Every outcome she faces lies beyond V10. The monograph does not give her Inago's V10 i0044 thought.
- **Review trigger.** Admission of a later volume.
- **Intended monograph path.** `characters/zenba-nana-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

### FXK-P021 Tsukimori Kizuna

- **Subject.** FXK-P021, 月森きずな, 27, 【営業】. Drawn from V09 i0152 and named in the same sequence ("きずなさん", i0157; name box, i0158).
- **Boundary.** V09–V10 main narrative, including the V10 flashback to 24 June 2016.
- **Outcome.** QUALIFIED_PENDING (confidence MODERATE; bounded V09–V10). The character specialist recommended DEFERRED_EVIDENCE; the disagreement is recorded below.
- **Rationale.** Sufficiency LOW-MODERATE in V09, HIGH in V10. (1) Convergence: V09's chart scene (i0154–i0156) and one concentrated V10 sequence with goals, asset figures, a 2016 flashback at 講報堂 (i0118–i0119) and a dated position (EUR/USD 30枚 short at 1.07230, i0122), with a consistent visual and verbal signature. (2) Variation: sing-song office speech against a cool first-person narration at home (i0109–i0110); private contempt in thought behind a sympathetic spoken line ("ブレグジットは やばかったね〜" spoken; "よっぽど 下手クソ なんだろうな…" in thought, i0114); polite delight at Kurumi's loss story (i0043); affection toward Inago, daily recruiting toward Nana, business with Mochiko. (3) Constraints: she says she does not expect the exit ("私もするとは思ってないよ", V10 i0119) and frames her euro short so that either result is acceptable — about 100万円 if 離脱派 wins; a small loss, or a profit from 事実売り, if 残留派 wins (i0123); that priced downside rules out the generic thrill-seeker the rest of her evidence invites. No gain from her recruiting is shown; she disclaims mocking Nana (i0149); net worth is the face she checks each day (i0109).
- **Largest gaps.** The short's outcome (V10-U01) and any purchase of カリフラワー (V10-U03) lie beyond V10 and are NOT SCOREABLE; the V09 chart's instrument; her living arrangement (not stated; a confidence disagreement preserved at V10); why falls please her (explanatory models only, never a diagnosis); the attribution of "私も" at V10 i0154 is fragile (V10 reading §L).
- **Disagreement.** The character specialist recommends DEFERRED_EVIDENCE: little interiority, market behaviour and the short's outcome unshown, motives for recruiting and teasing UNRESOLVED, a history of a few lines. This record keeps QUALIFIED_PENDING at MODERATE confidence because the three tests are met on accepted evidence: the ledger records sufficiency HIGH at V10 with counterexamples (L3395–L3418); her interiority is shown twice, in the home narration (i0109–i0110) and in private thought (i0114); her variation is the one the specialist itself calls unique among the newcomers; an unresolved motive does not bar qualification under §5.5.1, and an outcome withheld at the boundary applies equally to Nana, whom the specialist qualifies. The specialist's deficiencies become the monograph's stated scope limits: motive, her response to a large loss of her own, and her history stay UNRESOLVED. The outcome changes only under the rule of section 1.3.
- **Review trigger.** Admission of a later volume.
- **Intended monograph path.** `characters/tsukimori-kizuna-manga.md`. Self-containment result: pending G4. Fidelity result: pending G4.

## 4. Group lines (no IDs)

These figures act on one volume's pages without a name, or are named only in a feed or list, and the ledger records them only inside its "Minor figures (Vnn)" entries (section 1.2). None has differentiated evidence beyond its scene; all are DEFERRED_EVIDENCE as a class and none is eligible for a monograph.

- **V02** (ledger, Minor figures V02): a store co-worker (i0012), a security guard (i0138), students (i0139), pachinko players (i0098), a bookshop clerk (i0095); imagined tax and FSA officials (gag).
- **V03** (Minor figures V03): anonymous board posters (i0041), a TV horoscope presenter (i0075), a lecturer (i0157), a convenience-store customer (i0154).
- **V04** (Minor figures V04): two police officers at 大都西駅 (i0125–i0127), the salon's manager and receptionist (i0146, i0117), a look-alike dancer (i0092) and an elderly woman on the train (i0031).
- **V05** (Minor figures V05): the salon customer and the long-haired senior worker (i0057–i0059; the senior worker's aborted "あんたさぁ!" recurs in V06 i0043 without a stated identity); the editors of 月刊コミックカラーズ and 月刊まんが おんたま (i0114–i0119); the otaku fan who outs Yasuko (i0110, i0118), an act with consequences recorded here; two former bullies (i0011, i0030–i0031); a visitor in a cat-emblem jacket (i0111). Kurumi's co-worker (i0083–i0084) is recorded under FXK-P004.
- **V06** (Minor figures V06): the salon customer (a leveraged amateur, 5 + 2 lots long, "責任は僕にあるから", i0018–i0042), one of V06's shapes of responsibility (FXK-V06-C052) and an input to Study B; his identity with the V05 customer is not stated and is not assumed. Kozue's parents (an elderly couple, inset i0077; their cash taken); the off-panel voice "芽・吹・" (i0055; V06-U02); tax officials (gag, i0096).
- **V07** (Minor figures V07): the waitress (i0008, i0025), the exam proctor (i0133), forum posters and the aggregator (i0134), a light-haired woman passing Mochiko (i0138).
- **V08** (Minor figures V08): figures at the rubbish station (i0045–i0046), the home centre's cashier (i0082), police at an evoked cordon (i0038–i0039), the masked-number landline caller (V08-U03) and the voice "見ないほうがいい" (i0049).
- **V09** (Minor figures V09): the father's young colleague (i0062–i0066), the lawyer (i0098), the restaurant waitress (i0087, i0097), Inago's past interviewers (i0138), villagers and children (i0133), gag figures.
- **V10** (Minor figures V10): Inago's mother (flashback, i0034; her warning shapes Inago's stance, i0040), Nana's mother (i0056–i0057, INFERENCE MODERATE-HIGH), Yasuko's editor (a gag inset, i0086; identity with FXK-P018 not stated, V10-U15), fellow fans named by screen name only on Nana's screen (i0083–i0084, i0100), the restaurant waiter (i0052), students at the 2013 job fair (i0066), staff at 講報堂 (i0118).

Reassessment for the class: a figure from these lines receives the next free ID (FXK-P022 onward) if a later volume names it with an act toward a subject, or if the ledger opens an entry of its own for it.

## 5. Recorded, not qualification subjects

- **Public office-holders in expository narration.** "カーニー", the in-world central-bank governor named in narration (V03 i0041–i0042), is recorded with the unnamed office-holders of the run: the Bank of Japan's Policy Board as narrated (V03 i0160), the central-bank officials narrated in V06, the Swiss central bank's vice-chairman and his interviewer (V07 i0069–i0070) and the caricatured politicians of the V10 exposition (i0115–i0116). None is eligible for a monograph under this project's purpose; real identities are not considered (EXTERNAL_REFERENCE excluded) and the real-person naming rule applies.
- **Figures that are not persons.** The winged girl (Kurumi's personified greed; the V02 tempter at INFERENCE MODERATE-HIGH; V09), recorded under Kurumi; the winged Kurumi of V10 i0033; "ニンニクさん" and the "ロング騎士団" (a V06 vision); "セバスチャン", the butler in Yasuko's imagined vignette (V07 i0007); 綺羅メイ and the characters of 「ダンスのぷりんすさまっ!」 (in-world media, V10); the Death figure (V06 i0116–i0117); Mochiko's white cat (an animal, V04–V07).

## 6. Independent assessments compared

| Subject | Principal | Character specialist | Reviewer | Recorded outcome |
| --- | --- | --- | --- | --- |
| FXK-P001 Kurumi | QUALIFIED_PENDING | QUALIFIED_PENDING (HIGH) | agreed | QUALIFIED_PENDING |
| FXK-P002 the father | QUALIFIED_PENDING (MODERATE) | QUALIFIED_PENDING (LOW-MODERATE; the closest call) | agreed at MODERATE | QUALIFIED_PENDING (MODERATE) |
| FXK-P003 Kozue | QUALIFIED_PENDING | QUALIFIED_PENDING (MODERATE; rival DEFERRED_EVIDENCE inside Kurumi's monograph) | agreed | QUALIFIED_PENDING |
| FXK-P004 山口さん | DEFERRED_EVIDENCE | DEFERRED_EVIDENCE | agreed; split ledger entries to be merged | DEFERRED_EVIDENCE |
| FXK-P005 Mochiko | QUALIFIED_PENDING | QUALIFIED_PENDING (HIGH) | agreed | QUALIFIED_PENDING |
| FXK-P006 Mebuki | QUALIFIED_PENDING | QUALIFIED_PENDING (HIGH; V02–V09) | agreed; V09 return not to be omitted | QUALIFIED_PENDING |
| FXK-P007 優子 | DEFERRED_EVIDENCE | DEFERRED_EVIDENCE | agreed | DEFERRED_EVIDENCE |
| FXK-P008 Yasuko | QUALIFIED_PENDING | QUALIFIED_PENDING (HIGH) | agreed | QUALIFIED_PENDING |
| FXK-P009 – P018 | DEFERRED_EVIDENCE | DEFERRED_EVIDENCE or not eligible | agreed | DEFERRED_EVIDENCE |
| FXK-P019 Inago | DEFERRED_EVIDENCE | DEFERRED_EVIDENCE | agreed; rationale restated in §5.5.1 terms | DEFERRED_EVIDENCE |
| FXK-P020 Nana | QUALIFIED_PENDING | QUALIFIED_PENDING (MODERATE; bounded) | agreed | QUALIFIED_PENDING (MODERATE) |
| FXK-P021 Kizuna | QUALIFIED_PENDING (MODERATE) | DEFERRED_EVIDENCE | agreed on the outcome; rationale corrected | QUALIFIED_PENDING (MODERATE); disagreement recorded |
| Group lines; non-persons | as sections 4–5 | not eligible | agreed | as sections 4–5 |

Every person on the reviewer's list of persons not to overlook is assessed here. The character specialist's per-person evidence grids, directed-relationship maps and register notes are inputs to the G3 monographs and Study B; they were not re-verified line by line for this record and change no outcome.

## 7. Name-and-reference check (handoff contract §15.6)

- **Scope.** The introduction and rules (sections 1–2), every subject record in section 3 (a character-intensive document, so the sample is the whole of section 3), the group lines and section 5, and the comparison table.
- **Questions applied.** Whether known people are consistently identifiable; whether role labels serve a purpose; whether anyone is reduced to a functional label; whether pronouns are unambiguous; whether concealment is preserved; whether speaker, thinker and recipient are correctly attributed; whether each description respects its knowledge boundary.
- **Findings.** KNOWLEDGE_BOUNDARY_REQUIRED, kept: Kozue as "Kurumi's mother" for V01–V05 events with the V06 naming stated; the father's given name only with INFERENCE HIGH ("the father" otherwise; record heading by relation); あふぃちゃん before V02 i0074; Nana's and 優子's earlier appearances held as identifications by later evidence or inference. SOURCE_REQUIRED_ANONYMITY, kept: Mebuki's parents, Mochiko's mother and grandmother, the bespectacled man (headings by relation because the pages give no name). JUSTIFIED_ROLE_REFERENCE: office-holders in exposition (section 5). INCORRECT_IDENTITY_OR_ATTRIBUTION found and repaired before publication: Kizuna's counterexample had said she bets on an outcome she disclaims (corrected from V10 i0119, i0123); Kizuna's interiority had been called a single scene (V10 i0114 added). No UNNECESSARY_GENERICIZATION or AMBIGUOUS_REFERENT remains in the sample. No gendered pronoun is used for 山口さん, whose gender the pages do not assert in every appearance, or for the writer and the artist.

## 8. Pages re-opened for this record

| Page | Purpose | Finding |
| --- | --- | --- |
| V01 i0010 (reading copy) | Order of FXK-P002 and FXK-P003 | P1: Kurumi at a door signed 「ぱぱとままのへや♡」 ("…? 誰かいるの?"); P2: the mother drawn ("…上がれ!"); P3–P4: her chart and lines |
| V03 i0027 (reading copy) | First identification of Mebuki's mother | "芽吹ーっ!"; Mebuki: "お母さんの声でかいねん!" |
| V03 i0028 (reading copy) | Order of Mebuki's father and brother | P1: the family at table; the father drawn at upper right, the brother at left pouring a drink |
| V03 i0029 (reading copy) | Order of 健斗 and 千佳ちゃん | Top row: "近所の千佳ちゃんなんかー"; lower panel: the brother's "どう考えてもねーちゃんには無理やろ!"; the father's "学費くらい出したったらえぇがな…" |
| V05 i0003 (reading copy) | Order of Mochiko's grandmother and mother | P3: the elderly woman with a cane, "お母さん今日くらい来たらいいのにねぇ…"; Mochiko "いいよ別に来なくても" |

Pages re-opened earlier in the synthesis and cited here (V01 i0030 and V08 i0042 for FXK-P003; V09 i0031 and V05 i0161 with a crop for FXK-P001) are listed in the reconciliation audit, section 10.

## 9. Disposition of the reviewer's challenges concerning this record

| Challenge | Point | Disposition | Where it landed |
| --- | --- | --- | --- |
| C-02 (material) | Kizuna's counterexample misstated; a fallback that would let a production obligation lapse; Inago judged by a test the policy does not state; the "one interior scene" understated | ADOPT, verified in the V10 reading (i0114, i0119, i0123) and the ledger's Kizuna entry | FXK-P021 rationale and disagreement; section 1.3 (REASSESS_AFTER_REVISION on evidence only); FXK-P019 rationale |
| C-03 (material) | IDs departed from the stated first-appearance rule (優子); Kurumi's identifying appearance; the parents' tie at V01 i0010; 山口さん's row against the ledger; rule (b) inconsistent across three unnamed figures | ADOPT, verified in the ledger and on five re-opened pages | Section 1.2 (rule, tie rule, restated rule (b)); renumbered roster (section 2): the father FXK-P002, Kozue FXK-P003, 山口さん FXK-P004, Mochiko FXK-P005, Mebuki FXK-P006, 優子 FXK-P007, Yasuko FXK-P008; Mochiko's grandmother before her mother; the V06 salon customer moved to the group lines with Inago's mother and the V05 fan |
| C-04 (material) | Mochiko's motive wording omitted her V07 inner account of use | ADOPT, verified in the V07 reading and the ledger rows | FXK-P005 starting wording |
| C-06 (minor) | "Stop-losses" implied stop orders | ADOPT, verified in the V06 reading §M | FXK-P001 rationale |
| C-08 (minor) | Paratext content reproduced to exclude it | ADOPT | Section 1.1 (classes only); FXK-P016 |
| C-09 (minor) | A public office-holder given a qualification outcome | ADOPT (recorded, not a subject) | Section 5 |
| C-10 (minor) | Bare given name for the father | ADOPT | FXK-P002; section 1.5 |
| C-13 (minor, part) | Monograph-only probe limited to Kurumi | ADOPT | FXK-P005 notes; role-gap audit, G4 |
| C-15 (minor) | Intended paths presented as if documents existed | ADOPT | Section 2 column; every record; the ledger table |
