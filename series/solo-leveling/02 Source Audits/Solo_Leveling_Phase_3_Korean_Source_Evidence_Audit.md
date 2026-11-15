---
title: Solo Leveling — Phase 3 Korean Source and Evidence Audit
date: '2026-11-15'
project: Solo Leveling definitive Korean novel–English manhwa synthesis
phase: 3
source_status_label: Korean omnibus loaded and audited at paragraph level; v1 corpus claims tested; corrections recorded here, not yet applied to v1
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Solo Leveling — Phase 3 Korean Source and Evidence Audit
## The v1 corpus tested against Chugong's Korean omnibus

## 1. Disposition

The v1 corpus says Chugong's Korean novel governs every prose claim. Its own source records show that the Korean EPUB was never loaded while Documents 00–13, the Phase 2 correspondence map and the five reconstruction models were written. Phase 1 revalidated the Korean boundaries from an earlier workspace's audit, and every paragraph-level locator was left "pending remount".

This audit closes that gap. The Korean omnibus was loaded, its integrity and boundaries were verified, and it was converted into a reproducible paragraph-locator layer. Seven independent specialists then tested the corpus against it, two independent critical reviewers checked every material or adverse finding, and a final pass settled the open manhwa-side items.

**Overall result.**

- **The architecture of the analysis survives.** The executive thesis (non-subordination over domination; the sword that recognizes constitutions without conceding final judgment) is supported by the Korean text. Two passages state it outright, in Jinwoo's own focalized thought: `타의에 휘둘리지는 않겠지` (ch.75 · s007¶1778) and `강한 힘에 휘둘리지 않기 위해서` (ch.191 · s024¶1908). The shadow-personhood conclusion, that no refusal or exit independent of the Monarch is demonstrated, also survives and gets stronger.
- **The evidence layer does not.** The corpus's source architecture rests on a false premise. Its Korean locator system assumes chapter headings disappear early, but numbered headings survive throughout. Most volume-to-chapter zones in the correspondence map are offset. Several load-bearing correspondence claims are wrong, the most visible being where the Go Gunhee "heart beat" ending is adapted and the V15 p061 manhwa-original boundary.
- **The corpus's reading of Jinwoo leans sympathetic in specific, correctable places.** Repeatedly, the Korean text shows calculation, appetite, cruelty toward enemies, private punishment, and memory manipulation where the corpus reports courage, restraint or non-possession. The text supports the corpus's broad thesis but not several of the specific proofs it cites.

**Counts.** Specialists examined about 700 claim instances. 109 material or adverse findings went to independent critical review, with final verdicts in §8. By primary final verdict: 24 CONTRADICTED, 62 QUALIFY, 10 LOCATED, 10 CONFIRMED and 3 NOT-FOUND in the prose. Some findings carry split verdicts; counting every verdict a row carries gives 24, 67, 12, 13 and 4.

**What this audit does not do.** It does not edit any v1 artifact. The v1 release is hash-bound by `05 Final Release/CORPUS_MANIFEST.md` and `ARTIFACT_CHECKSUMS.sha256`, so this record is the errata home until a correction route is chosen (§10). It does not audit manhwa visual grammar except where a claim says what the prose contains. It does not audit original Korean manhwa wording, which the project still does not possess.

## 2. Source identity and the paragraph-locator convention

**Korean omnibus.** `나 혼자만 레벨업.epub`, sha256 `ddb2527fd0e273ecf17dc54ced1bc5354c25e89b19929fb16fb584c64bd5d6f0`, 1,549,240 bytes. ZIP integrity passes. It contains 33 `index_split_000–032.html` bodies, a `titlepage.xhtml`, and a single-entry navigation (`Start`). It has about 1.61 million characters of markup-stripped text and 59,567 non-empty paragraphs. The source stays in the primary-source workspace and never enters Git.

**Locator convention.** `sNNN¶M` is the M-th `<p>` element with non-empty text (1-based) in `index_split_NNN.html`. It is deterministic from the EPUB bytes. Any reader with the same file can regenerate it by stripping markup, unescaping entities, and counting non-empty `<p>` elements in document order; `<hr>` scene breaks are not counted. Citations combine it with the surviving chapter heading: `ch.N · sNNN¶M`, `외전 N · sNNN¶M`, `후일담 N · s032¶M`.

**Official English manhwa.** The fifteen Yen Press digital CBZs whose hashes are recorded in the Phase 1 audit were cited by logical page (`Vnn pNNN`), never by ZIP member order. They are an English translation, so every prose–manhwa comparison here is an adaptation comparison, not a translation audit.

## 3. Structural findings

### 3.1 Chapter headings survive throughout (corrects Phase 1 §6.4 and README §2)

The omnibus preserves a complete, monotone main-story sequence of numbered headings, `2화`–`243화`, with no gaps or duplicates. 1화 begins under the title line at s000¶1. The side stories carry `외전 1화`–`외전 21화` and the postscripts `1화. 베르의 기억` and `2화. 다시 만날 때까지`.

This corrects three corpus claims:

- **README §2 and Phase 1 §6.4.** They say early headings survive only through `전직 퀘스트`, so later prose must be cited by split region. Split files are packaging, as Phase 1 rightly said, but chapter-level locators are available everywhere.
- **The Phase 2 map and Document 13.** Their eighteen named Korean headings (`프롤로그`, `E급 헌터`, `레벨 업!`, `이상한 레이드`, `대박의 예감`, … `전직 퀘스트`) do not occur in the body text or in the navigation. Every one was searched for and not found (findings P-01, S1-12, S2-01, S6-10, S6-11). Their source is unknown; they may come from another edition or a reader's table of contents.
- **Document 09's "first eighteen headings" claim** is contradicted.

What remains true: the navigation is non-literary (`Start`), and the file does not preserve Korean print-volume boundaries.

### 3.2 Corpus boundaries confirmed at paragraph level

| Boundary | Locator |
|---|---|
| Main story begins (1화, implicit) | s000¶1 |
| Main story ends (`[나 혼자만 레벨업 完]`) | ch.243 · s030¶1609 |
| 외전 1화 `나는 헌터협회 직원입니다` | s030¶1612 |
| 외전 4화 `귀환` | s030¶2136 |
| 외전 5화 `이그리트의 기억` | s031¶96 |
| 외전 14화 `나 혼자만 만렙` | s031¶2077 |
| 외전 15화 `지금 만나러 갑니다 (1)` | s032¶34 |
| 외전 18화 (bare heading, untitled) | s032¶650 |
| 외전 21화 `최종화. 12년 후 (완)` | s032¶1247 |
| `[나 혼자만 레벨업, 외전 完]` | s032¶1524 |
| `나 혼자만 레벨업 후일담` | s032¶1525 |
| 후일담 1화 `베르의 기억` | s032¶1526 |
| 후일담 2화 `다시 만날 때까지` | s032¶1748 |
| Final paragraph of the omnibus | s032¶1950 |

The Phase 1 boundary policy (§7 there) is confirmed in every respect. One small addition: an author's note at s031¶602 introduces `베르의 기억` as a 번외편 requested by readers.

### 3.3 Verified manhwa-volume to Korean-chapter correspondence

These replace the v1 split-zone assignments in the Phase 2 map, most of which are offset. V1 is the clearest case: the map anchors it to the first seven named headings, but it actually adapts ch.1–13.

Volumes break mid-chapter, so a chapter can appear at both ends of adjacent volumes.

| Manhwa volume | Korean chapters adapted | Volume-end anchor | Basis |
|---|---|---|---|
| V1 | ch.1–13 | instant-dungeon entry, s001¶80–111 (V1 p312–p313) | first/last story pages |
| V2 | ch.13–28 | `[지옥의 수문장 켈베로스]`, s002¶989 (V2 p296) | first/last story pages |
| V3 | ch.28–52 | Necromancer offer still pending, s004¶1352–1360 (V3 p310–p311) | first/last story pages |
| V4 | ch.52–78 | s008¶243–247 (V4 p320) | first/last story pages |
| V5 | ch.78–101 | s010¶1362–1363 (V5 p314) | first/last story pages |
| V6 | ch.101–116 | Baek Yoonho transforms in the queen's chamber, s013¶1–20 (V6 p301–p302) | sampled; may shift by one scene |
| V7 | ch.116–127 | Monarchs at Jeju, s014¶140–210, recomposed as the closing montage (V7 p295–p301) | sampled; may shift by one scene |
| V8 | ch.127–150 | Shinjuku gate, s016¶2187–2199 (V8 p301–p302) | first/last story pages |
| V9 | ch.150–171 | Jinwoo already in Japan, s019¶950–958 (V9 p305–p307) | first/last story pages |
| V10 | ch.171–192 | s024¶2111 (V10 p297) | first/last story pages |
| V11 | ch.192–216 | s027¶549 (V11 p306) | first/last story pages |
| V12 | ch.216–233 | s029¶1440–1489 (V12 p298–p299) | first/last story pages |
| V13 | ch.233–243 (excluding the ch.243 closing vignettes s030¶1464–1608) + 외전 2–4 | 외전 4 · s031¶94 (V13 p288) | page-by-page at boundaries |
| V14 | 외전 5–19 (interleaved) + ch.243 closing vignettes | see §3.4 | sampled every third page |
| V15 | 외전 20–21 + 후일담 1–2, then manhwa-original continuation with an embedded 외전 1 | prose ends s032¶1950 = V15 p058 | page-by-page at boundaries |

### 3.4 Side-story correspondence

| Korean unit | Manhwa | Notes |
|---|---|---|
| ch.243 closing vignettes: Yoo Jinho cider, Lee Juhee, Go Gunhee "heart beat" (s030¶1468–1608) | V14 Part 3 p229–p249 | Go's restored heartbeat is p247–p248 (S1-01) |
| 외전 1 `나는 헌터협회 직원입니다` (s030¶1612–1778) | V15 Part 6 p244–p251 | adapted nearly beat for beat inside a manhwa-original frame; not adapted elsewhere (S1-02) |
| 외전 2–4 `재회 (1)–(2)`, `귀환` | V13 p238–p288 | V13 c040; the dimensional-gap war is 외전 3, not main story (S1-06) |
| 외전 5 `이그리트의 기억` | V14 Part 2 p186–p215 | sampled |
| 외전 6–11 `너의 일상은 (1)–(6)` | V14 Part 1 p007–~p085 | order preserved; sampled |
| 외전 12 `결심` | V14 ~p086–~p106 | battle runs into 외전 15 |
| 외전 13 `어금니의 하루` | V14 Part 2 p173–p185 | |
| 외전 14 `나 혼자만 만렙` | V14 Part 3 p250–p281 | |
| 외전 15–17 `지금 만나러 갑니다 (1)–(3)` | V14 ~p107–p155 | 16 and 17 interleaved |
| 외전 18 (untitled) | split: s032¶650–751 (Sung Il-hwan's retained memory and his request to forget) = V14 Part 3 p218–p228; s032¶774–879 (Christmas Eve with Cha Hae-In) = V14 Part 2 p158–p170 | the exam-morning coda s032¶752–773 was not located in the manhwa |
| 외전 19 `최종화. 12년 후 (1)` | V14 p282–p292 | |
| 외전 20–21 | V15 Part 4 | Go's second visit and death, 외전 21 · s032¶1438–1478 = V15 p016–p028 |
| 후일담 2 `다시 만날 때까지` | V15 p052–p058 | the final prose paragraph (Suho's dream) is the first panel of p058 |
| — | V15 p059–p243, p252–p267 | manhwa-original adolescent-Suho continuation |

## 4. Material corrections by theme

Each item gives the decisive Korean locators. Full rows are in §8.

### 4.1 Correspondence and boundaries

- **Go Gunhee's formal ending is adapted, one-to-one, in V14 Part 3 p239–p249** (S1-01, CONTRADICTED). The map and ledger place it as omitted from V13 with "comparable" material in V15 Part 4. The V15 Go material is a different scene: his second visit and death in 외전 21.
- **The V15 p061 "hard boundary" needs rewriting** (S1-02/S1-04, QUALIFY). The prose ends at s032¶1950, the first panel of V15 p058. The jump to adolescent Suho begins at p059, still inside Part 4. Parts 5–6 are manhwa-original continuation, **except** p244–p251, which adapt 외전 1 nearly beat for beat.
- **`Beautiful World`'s support-department question is Chugong's** (S1-03, CONTRADICTED; S5-13). Document 11 credits it to the adaptation as "a more constitutional answer than Jinwoo's original solution". The question and its healer-recruitment answer are in 외전 1 (s030¶1765–1777). The adaptation's game frame remains manhwa-original.
- **V13's closing question about being needed is Chugong's** (S1-08): 외전 4 · s031¶77. V13 ends at s031¶94 and leaves out the ch.243 closing vignettes, which move to V14.
- **Misplaced rows.**
  - The first `일어나라` and the Necromancer class change are in V4, not V3 (S2-03).
  - Christopher Reed's death and Kamish (ch.182–187) are in V10, not V11 (S2-08).
  - The Min Byung-gu "conscious but happy servant" account is not at the V7 extraction scene. It first appears at ch.151 · s016¶2339, reported second-hand by Cha Hae-In from a near-death dream, and the manhwa keeps it almost verbatim at V9 p020 (S2-05, CONTRADICTED; S3-10).
- **Prose sources for supposedly manhwa-original material.**
  - The taunting "old self" voices during the Knights assault are in the prose (s004¶650–682), so S2-07 drops the label.
  - Jinwoo's quiet self-corruption worry is prose (ch.23 · s001¶2222–2229). The manhwa relocates it to the Taeshik scene at V3 p128 (S2-06, as qualified by R1).

### 4.2 Jinwoo: courage, calculation, appetite

- **`무력한 자의 용기` is System text** (S3-01, S4-02, S6-02). It is the title of the secret quest completed at the altar (ch.7 · s000¶1465), rewarded at ch.25 · s002¶353–367, and never used again in the prose. At the decisive moment the narrator calls Jinwoo's choice "not a grand meaning like sacrifice" (`희생같이 거창한 의미는 아니었다`, s000¶1407) and gives part of it as calculation: a death payout for his family instead of a crippled life (¶1408–1415). He also says it was his own choice (¶1394), and he had cast the deciding vote to enter, for the money (s000¶188–208) (S4-01, S4-18). The corpus's reading of moral agency before effective agency survives, but its anchor phrase is the System's evaluation, and the moment mixes care with calculation.
- **Cruelty toward enemies is understated** (S4-04, S4-05, S4-10).
  - Hwang Dongsuk is killed while down and begging, after Jinwoo had resolved on no mercy before any quest appeared (ch.22–23 · s001¶1975, ¶2191–2213).
  - A bound prisoner is fed alive to hobgoblins as bait, "without any pity" (ch.34 · s002¶2091–2118).
  - Kargalgan's terror is deliberately prolonged (ch.90 · s009¶708–759). R2 notes the narration frames this as retaliation (¶710), so the corpus's "rarely … merely for entertainment" can stand with the counterexample added.
- **"The weak get eaten"** (S4-09): Jinwoo explicitly agrees (ch.105 · s011¶640–641). The corpus's "never a social Darwinist" holds only if scoped to humans.
- **Event order in V5** (S3-06, CONTRADICTED). Re-examination (ch.75), S-rank confirmed and congratulated by Go Gunhee (ch.78 · s008¶198), then the mining team as a known S-rank (ch.89 · s009¶357). During the raid Jinwoo deliberately lets Son Kihoon be battered so he can keep the monsters (ch.91 · s009¶811–813; S3-07).
- **The Jeju refusal is relational in the prose** (S3-08). It turns on his mother's trauma (s012¶539–545), not sovereign self-direction. Self-direction does fit the Japan decision (s019¶666–690).
- **Japan.** The scene where his mother asks him not to go exists in neither medium (S4-08, S5-11, M1-01). In the prose, Go Gunhee is the one who wants to stop him (s019¶810–815), and Jinwoo's decision is about fighting giants, leveling, and claiming the monsters' rights (¶816–821). In the manhwa, his mother remembers the firefighter father and helps him pack (V9 p276–p277).

### 4.3 Shadows: consent, refusal, compelled loyalty

- **The refusal thesis is strengthened** (S5-04). The only shadow refusal in the text is a refusal to attack Jinwoo himself when ordered (ch.100 · s010¶1186–1190). Every exit is a release or erasure by Jinwoo. 외전 13 says shadow feelings derive from the Monarch's mind (s031¶1986–1990).
- **The narrator states compelled loyalty outright**: the dead are forced into absolute loyalty by the Monarch's power while each keeps its own consciousness (`절대적인 충성심을 강요받는`, ch.226 · s028¶1381). The same scene breaks Jinwoo's stated rule against making innocent dead into soldiers, with a promise to return them to rest after the war (¶1370–1380) (S3-11). This is the single most important passage the corpus omits on shadow ethics.
- **Min Byung-gu.**
  - Extraction rests on presumed consent: "he'd choose the same, 100 out of 100" (s013¶1635).
  - Release rests on Jinwoo's sense of duty to the war dead (s013¶1721).
  - After the release, Baek Yoonho says Min disliked fighting (`어지간히도 싸우는 걸 싫어했거든요`, s013¶1754). It is a true fact the corpus may keep, but it is not one of Jinwoo's reasons (S3-09 and S4-20, as reconciled by R2).
  - The romanization is Byung-gu (민병구), not Byung-Gyu.
- **`Jin-i` is resolved** (S5-01, S6-12). She is 서진이 (Seo Jin-i), the stepdaughter of an abusive doctor, who took her own life. In 외전 19–20 Detective Jinwoo raises her shadow from dried blood, returns her name, erases her memories of her stepfather, and declines to keep her as a soldier, releasing her instead (s032¶1049–1079, ¶1208–1219). The UA in README §12 and Document 12 closes. The shadow matrix should gain a row for a human, non-combat, released shadow.

### 4.4 Memory ethics

- **Kim Chul/Iron is the corpus's strongest proof of non-possessive restraint, and both of its legs fail** (S5-02, CONTRADICTED; S1-11).
  - Iron vanishes under the Cup's stated rule that shadows overlapping the past time-axis are annihilated (ch.243 · s030¶1455). Jinwoo did not choose that.
  - In 외전 17 Jinwoo hypnotizes the human Kim Chul, erases his memory and recites a false one (`지운 기억을 대신할 가짜 기억을 읊어 주었다`, s032¶564).
  - The scene keeps some care: he tells Kim Chul to live well and take pride in having fought for the world (¶570).
- **Jinwoo's own principle** is that he has no right to choose which memories others keep, because "that is God's work" (외전 10 · s031¶1305–1308). It is stated while returning Woo Jinchul without his memories. The Kim Chul and Seo Jin-i scenes break it. The corpus records neither the principle nor the breach.
- **Sung Il-hwan** remembered the erased timeline for about a year before asking to forget (외전 18 · s032¶651–751; S5-06). His "choice of forgetting" is a late, deliberate request, not an immediate one.

### 4.5 The detective era

- **The punishment is a routine, not a one-off exception** (S5-03, S4-07, S7-12).
  - The victim, Seo Jin-i, is already dead.
  - Jinwoo offers her stepfather the chance to surrender, then imprisons him under Beru, who keeps healing him so he cannot die (외전 20 · s032¶1162, ¶1195–1222).
  - ¶1162 refers to many earlier cases, and shadows had already killed criminals before the police career (s031¶486–492; s032¶1682–1722).
  - Woo Jinchul throws the case file in the bin (S7-11), and Jinwoo tells the victim's friend there was no foul play.
- **What this contradicts.** Document 04's claim that the testimony "supports ordinary investigation" and Document 11's "first protects the victim" are contradicted. Document 12's open question about police-era Jinwoo should be restated around a standing private justice practice, not a single exception.

### 4.6 Sovereignty, the Rulers and the reset

- **Antares's offer is refused out of distrust** ("trust a guy whose eyes say he wants to kill me?", ch.241 · s030¶957–959), not as an explicit rejection of political dominion (S5-08 and S3-13; R2 recommends CONTRADICTED for Document 08:1031). A better textual base for the non-dominion claim is 외전 12, where Jinwoo chooses to stay on Earth (s031¶1764–1774).
- **The Rulers perform the reset**, and earlier resets designed the hunter world (s028¶217–220). Jinwoo shares his war memories with Woo Jinchul at ch.230 (s029¶871–895), but the text does not show him disclosing the reset plan (S4-13, as qualified by R2).
- **Ashborn chose Jinwoo despite the Architect's objection** (ch.220 · s028¶275). The inheritance is worded as a fusion of personalities (`인격`, `동화`: "I became you and you became me", s028¶307, ¶319; s030¶1405), not as `자아`/`의식` (S5-07, S6-06, S4-12). Document 01's `자아/의식` wording comes from Min Byung-gu's testimony, not from the Ashborn scene.

### 4.7 Korean language and narration

- **`일어나라` was coined by Jinwoo.** The System asked him to designate a command word (`[그림자 추출 스킬의 명렁어를 지정하십시오.]`, sic, s004¶1474), and he chose it on instinct (¶1476–1477). Its final use is the System's deletion code (s028¶362–367) (S6-01).
- **`살의` and `살기` differ.** `살의` is mainly the System's trigger word for compulsory kill-quests (ch.22 · s001¶1985, ¶2018). The fear Jinwoo projects is `살기`, a skill he receives for those kills (s001¶2243). Document 09 never names `살기` (S6-05).
- **`형`→`형님` runs the other way.** Yoo Jinho begins with familiar `형` (ch.18 · s001¶1099) and switches to deferential `형님` immediately after watching Jinwoo kill the spider boss (ch.22 · s001¶1889). Kinship comes later (ch.67 · s006¶1565), and `형님` carries across the reset (ch.243 · s030¶1511–1517). The first `형님` in the book is gang hierarchy (s001¶1045).
- **`인류 최약병기` is a pun.** A newcomer mishears it as `최종병기`, "ultimate weapon" (s000¶60–71). It occurs once and is glossed in the text (S6-03).
- **Narration.** The main story is third person throughout, a fact Document 09 never states. Four side stories have first-person narrators, none of them Jinwoo (S6-08).
- **Interiority is not continuous.** This tests the corpus's adaptation thesis that "novel Jinwoo is psychologically continuous" (S6-07, reproduced by R1 and the principal). Counting paragraphs that open with a single quote, the standard thought marker, gives these rates per 1,000 paragraphs:

  | Chapters | Rate |
  |---|---|
  | ch.1–40 | 82.5 |
  | ch.41–80 | 116.4 |
  | ch.81–120 | 104.7 |
  | ch.121–160 | 88.9 |
  | ch.161–200 | 56.5 |
  | ch.201–240 | 48.9 |
  | 외전 1–21 | 46.6 |
  | 후일담 | 65.9 |

  The figure counts all speakers, so it is an upper bound on Jinwoo's interiority. The finding: interiority roughly halves after ch.160 and does not recover in the side stories. The adaptation contrast still holds (the prose keeps more cognition than the manhwa), but "continuous" should become "front-loaded and thinning", and the manhwa's "punctuated" Jinwoo partly follows a trend already in the prose. S6's further claim that the side stories are the lowest band does not reproduce.
- **Missing and misworded terms.** `거인왕` does not occur; the text has `거인들의 왕` (S6-14).

### 4.8 Character reconstruction models

- **Anchors.** Of the 106 cited `index_split` anchors, 84 are exact, 19 are in the right split but need a better passage or a qualified claim, and 3 are wrong. Every split assignment was right.
- **A death-realm illusion is used as real evidence** (S7-01, S7-02, CONTRADICTED). Ch.218 · s027¶1155–1257 is an illusion built from Jinwoo's wish to undo mistakes (`이 전부가 가짜라는 것을 알고 있다`, s027¶1225). The Go Gunhee model calls it a "reset encounter", and the Jinwoo model draws a "Jeju bargain" from it. The real reset-world Go scenes are ch.243 · s030¶1562–1606 and 외전 21 · s032¶1436–1484.
- **Go Gunhee against the Frost Monarch** (S7-03, CONTRADICTED with a caveat). The battle voice is marked as unlike Go's own: a Ruler, the Fragment of Brilliant Light, speaking through him (ch.200 · s025¶1541–1584). R1 adds that s025¶1861 describes a merging of consciousness, so the model should describe a vessel–Ruler fusion state, not Go's own "warrior layer" and not a clean takeover.
- **Yoo Jinho under torture** (S7-04, CONTRADICTED). Hwang Dongsoo wanted him to confirm that Jinwoo killed his brother, which is true (ch.23 · s001¶2203–2218; ch.189 · s024¶1513–1549). Jinho is protecting a true secret, not refusing to make a false accusation.
- **Register ledgers are missing** (S7-05, S7-13, S7-14).
  - Go uses four speech levels and drops to `하게체`/`자네` with Jinwoo at his death.
  - Jinwoo has an archaic register with cosmic beings (`그대`, `-겠나`, `-마`) and speaks to his mother in both plain speech and `해요체`.
  - Cha Hae-In's address terms for Jinwoo change in a non-steady order.
- **Behavioral rules with counterexamples** (S7-06–S7-12).
  - Jinwoo tells reset-world Go about the erased timeline.
  - He seizes a well-meaning agent who shows him his father's photographs.
  - He lies to Go about his summon count, about 100 against more than 300 (ch.119 · s013¶897–900).
  - He teases and flirts with Cha Hae-In early on.
  - As a detective he acts outside the law.
- **Withheld-scene probes.** Ten were run, two per character. They were strongest for Go Gunhee and Woo Jinchul and weakest where a trigger the models don't describe drives the scene (Jinwoo's father; Yoo Jinho enjoying attention). They indicate where to look and are not validation. The models remain `active_provisional`.

## 5. Manhwa-side items settled in the closing pass

Participant M1 checked the manhwa side of seven claims whose prose side had already been reviewed. The principal re-viewed the decisive pages for M1-01 (V9 p276–p277) and re-read the matching prose (s019¶810–815) before adopting it.

| ID | Corpus claim | Manhwa evidence | Verdict | Effect |
|---|---|---|---|---|
| M1-01 | Jinwoo's mother asks him not to go to Japan, then accepts (Doc05:155–163; Doc04:567) | The whole decision is in V9 p260–p307; V10 opens already in Japan, with no flashback. At dinner his mother recalls the firefighter father leaving mid-meal and offers to help him pack (V9 p276–p277); Jinah also accepts (p278–p281). No family member objects. In the prose the person who wants to stop him is Go Gunhee (ch.170 · s019¶810–815) | CONTRADICTED in both media | Closes S4-08 and S5-11. The objection scene does not exist; the manhwa's firefighter-father motif here is real and manhwa-added, which supports the corpus's adaptation claim in Doc00 §4 |
| M1-02 | The manhwa gives less access than the novel to Min Byung-gu's retained consciousness (Doc06:90; D13:734, :807) | Cha Hae-In's dream testimony keeps his restored identity and his frightening happiness in service (V9 p019–p021); only his vision of the army and its grand marshal is cut. At the extraction the manhwa adds Jinwoo wondering whether Min is resisting (V7 p163), and it moves the release to a plea from Baek Yoonho (V7 p168–p169); in the prose Jinwoo decides alone (ch.122 · s013¶1719–1721) | QUALIFY | Access is nearly equal. The real adaptation change is who prompts the release |
| M1-03 | Reset-world Lee Juhee "is allowed to live without the dungeon trauma" (Doc04:695) | Neither version shows her trauma or its absence; the manhwa adds that she is in a nursing program (V14 p236) | QUALIFY | With S4-21: keep only as an inference from the reset, not as shown evidence of restraint |
| M1-04 | The manhwa expands Esil Radiru (Doc10; Doc00 §4) | She refuses to be sent away at floor 96 (V6 p057–p058), throws her spear at Baran to open a gap for Jinwoo (p118), watches Kaisel's extraction and gets her own farewell (p130–p134). Most of the comedy is already in the prose | QUALIFY | The expansion is real but agentive and combat-centred, not the described characterization; record it precisely |
| M1-05 | The manhwa delays exposing Matsumoto's plan (Doc10; Map) | The manhwa first states the plan mid-raid (V7 p063–p064); the prose exposes it before the raid (ch.104 · s011¶355–395) | CONFIRMED | Adaptation claim stands |
| M1-06 | The English manhwa renders Yoo Jinho's `형님` as "Boss" (Doc09; Doc00 §10) | "Boss" from V2 p223–p224, with no variants; in the reset world Jinho moves from "sir" back to "Boss" (V14 p234), matching the prose's `형님` carrying across the reset | CONFIRMED | Adaptation claim stands |
| M1-07 | "Devour the System" is an adaptation-specific formulation (Doc01:295; Doc02:589) | Not in the V9 Architect fight (p102–p138) or the V12 deletion pages (p155–p164); V12 p162 adds an "Are you sure you want to delete the system?" prompt. The nearest wording is V2 p238, about using the System as it uses him (= ch.22 · s001¶2046) | NOT-FOUND | The formulation appears to be the corpus's own; relabel it as analytical vocabulary, not a quotation from either medium |

Coverage: the decisive pages for each item were viewed; the surrounding pages were sampled. The residual risk for each verdict is that a relevant panel sits on an unsampled page.

## 6. Participation, configuration and boundaries

The audit followed the multi-agent source-reading arrangement proposed in PR #599, §4.1 of the topology policy in that PR, at the owner's direction. That section is not yet on `main`. By its own §4.1.1 it targets sequential readings, not evidence audits, so this record treats it as a voluntary standard, not a binding one.

| Participant | Role | Assignment | Material inspected (summary) | Claims examined |
|---|---|---|---|---|
| Principal | Principal analyst and integrator | Source loading and integrity, locator layer, chapter index, structural findings P-01/P-02, packet construction, adjudication, this record | EPUB integrity and boundaries; all chapter headings; decisive passages behind reviewer disagreements (s000¶1405–1416, s004¶1472–1478, s013¶1750–1756, s028¶1378–1382, s030¶955–960, s031¶1304–1309, s032¶561–573); independent recount of interiority density | — |
| S1 | Independent specialist | Late correspondence: V13–V15 against ch.238–243, 외전 1–21, 후일담 1–2 | Read in full: ch.243, 외전 1–4, 18, 21, 후일담 2. V13 and V15 page by page at boundaries; V14 every third page; V15 Parts 5–6 about 45 of 207 pages | 24 |
| S2 | Independent specialist | Early correspondence: V1–V12; prose side of Documents 00 §4 and 10 | First and last story pages of each volume; 54 map rows with prose locators | 58 rows + 24 other claims |
| S3 | Independent specialist | Document 13 evidence ledger | 104 ledger claims, 46 of them Korean-term claims, spread across V1–V15 | 104 |
| S4 | Independent specialist | Documents 01–04 and the README executive thesis | Each passage read in context (±15–60 paragraphs) | 132 |
| S5 | Independent specialist | Documents 05–08, 11 and the dependent propositions in 12 | Read in full: ch.243 and 외전 1–21, 후일담 1–2 | 104 |
| S6 | Independent specialist | Korean language, narration, terminology; Document 09; glossary | Scripted term counts and density measures; Document 09 claim by claim | 74 |
| S7 | Independent specialist | The five character reconstruction models | All 106 anchors; at least 15 dialogue lines per character; 10 withheld-scene probes | about 186 |
| R1 | Independent critical reviewer | 52 material or adverse findings (P, S1, S2, S6, S7) | Sealed Phase 1 verdicts written from source before opening specialist verdicts; manhwa pages viewed for boundary items; EPUB navigation inspected | 52 |
| R2 | Independent critical reviewer | 57 material or adverse findings (S3, S4, S5) | Same sealed two-phase method | 57 |
| M1 | Independent specialist and self-reviewer (reduced configuration) | Seven manhwa-side items the specialists left open | Targeted manhwa pages | 7 |

**Execution facts.**

- Every participant other than the principal ran as a separately initialized Claude Code native subagent.
- Each had its own read access to the paragraph-locator layer and, where assigned, to the manhwa page extractor. Each received only the common brief and its own assignment, not the principal's working notes.
- No model override was requested for any subagent. The model and reasoning settings of the subagents were not separately observed and are not recorded here.
- Reviewers received the claims and cited locators first, with no verdicts. They wrote their own verdicts to disk before opening the specialists' verdicts.
- M1 used the reduced configuration because its work was bounded: seven pre-identified page checks on claims whose prose side had already been reviewed.

**Agreement.** R1 agreed with the specialists on 42 of 52 items, partly agreed on 9 and disagreed on 1. R2 agreed on 40 of 57, partly agreed on 15 and disagreed on 2. Neither reviewer found a fabricated locator. Every Korean anchor quoted by a specialist exists verbatim at the stated paragraph.

**Where the principal departs from a recommendation:** nowhere in §8. The principal's own recount confirms R1's qualification of S6-07.

**Mechanical verification of this record.** A script checked every `ch./외전/후일담 N · sNNN¶M` label against the chapter index, every cited paragraph against the split's paragraph count, and every backticked Korean anchor against the source text.

- It found and corrected three chapter labels inherited from participants' working files: ch.33→32 at s002¶1840, ch.131→129 at s014¶558, and ch.191→190 at s024¶1785.
- It replaced one elided anchor at s025¶1531 with a verbatim fragment.
- The remaining unmatched anchors are, by design, headings or terms the record reports as absent from the source, grammatical endings, or titles covering a range of side stories.

**Name-and-reference check (handoff contract §15.6).** Sampled: §1, §4.4–§4.5 and §10.

- Named characters are referred to by canonical name throughout. Seo Jin-i is named on first mention, then referred to as "the victim" only where the role carries the argument (`JUSTIFIED_ROLE_REFERENCE`).
- The agent who shows Jinwoo his father's photographs stays unnamed, following the participant's report, and is not given an invented name.
- No `AMBIGUOUS_REFERENT` or `INCORRECT_IDENTITY_OR_ATTRIBUTION` defects were found in the sample.

**Knowledge boundary.** This is a retrospective audit with the complete series admitted (initiation §3.8; topology §4.1.4). No participant altered Document 13's volume-local horizons. Where a horizon statement is factually misplaced, as with S3-10, which moves the Min Byung-gu testimony to ch.151, the finding is recorded as a claim-revision item, not a rewrite of the historical judgment.

**Private materials.** The paragraph-numbered text, the participants' working files and their transcripts stay outside Git. This record carries every material finding in sanitized form, with Korean quotations held to brief anchors.

## 7. Independent observations the corpus lacks

- **Jinwoo's own memory principle** (외전 10 · s031¶1305–1308) and its breaches.
- **The compelled-loyalty narration** (ch.226 · s028¶1381).
- **A reset-world alien invasion** in 외전 12, which bears on the reset-world stability claims (S5).
- **The Monarchs-at-Jeju scene** (ch.126–127), recomposed into the V7 closing montage and a V8 "Bryce Canyon" opener. No canyon appears in the prose (S2).
- **The archaic register** Jinwoo uses with cosmic beings, and **Go Gunhee's four speech levels** (S7).
- **An enjoyment-of-power counter-reading.** The text openly shows Jinwoo's appetite for growth and his pleasure in dominance alongside the non-subordination thesis (S4). A full reading should hold both, not subordinate the first to the second.

## 8. Findings register

Every row is a material or adverse specialist finding that went through independent critical review. "Final verdict" and "Disposition" are the reviewer's recommendation, which the principal adopts unless §5 or §6 says otherwise. "Review" shows the reviewer and its agreement with the specialist. Corpus references use these short names:

- `Doc00`–`Doc12`: the specialist documents
- `D13`: the evidence ledger
- `Map`: the Phase 2 correspondence map
- `Phase1Audit`: the Phase 1 source integrity audit
- `…Model`: the reconstruction models

Claims and evidence are abridged; the cited lines and locators are authoritative.

| ID | Corpus | Corpus claim (abridged) | What the Korean text shows (abridged) | Final verdict | Key locators | Disposition | Review |
|---|---|---|---|---|---|---|---|
| P-01 | Doc00:60; Phase1Audit:389-393 | "Early headings survive through `전직 퀘스트`; later prose is therefore referenced by verified `index_split_XXX` regions"; the omnibus's navigation is "essentially non-literary" and split files are the only stable locator layer. | principal finding: numbered chapter headings survive throughout | CONTRADICTED | s000¶192; s011¶86; s030¶13 | correct (keep "nav = Start" as true) | R1 AGREE |
| P-02 | Phase1Audit:326-383 | Main story ends at `[나 혼자만 레벨업 完]` inside split 030; 외전 1-4 in split 030 remainder, 5-14 in 031, 15-21 in 032 then `[나 혼자만 레벨업, 외전 完]`; 후일담 … | principal finding: corpus boundaries confirmed at paragraph level | CONFIRMED | s030¶1609; s030¶1612; s030¶2136 | locator-only | R1 AGREE |
| S1-01 | Map:344; D13:1368 | The Korean formal Go Gunhee/"heart beat" ending is omitted from V13. | The manhwa adapts the final prose scene one-to-one, and not in V15. | CONTRADICTED | ch.243 · s030¶1562–1608; V14 p239–p249; s030¶1468–1608 | correct (→ V14 p229–p249) | R1 AGREE |
| S1-02 | Doc00:264–266; Map:389–394; D13:1568 | "V15 p061–p267 (Parts 5–6) is manhwa-original relative to the supplied Chugong prose", stated as a hard boundary with "no counterpart". | Part 6 embeds a close, beat-by-beat adaptation of 외전 1 (the support-department employee's story from the erased timeline): - p246: the students' three-career survey (¶1613–1617) - p246–p247: the angry raid-leader call about "the Sung kid" (¶1659–1662), and hunters asking for snacks, a pay advance and … | QUALIFY (material) | 외전 1 · s030¶1613–1777; 외전 4 · s031¶43–48 | qualify (exception p244–p251) | R1 PARTIAL |
| S1-03 | Doc11:915 | "`Beautiful World` belongs entirely to the manhwa-original continuation". | In Chugong's 외전 1, the employee's dilemma about E-rank Sung Jinwoo is exactly this one. | CONTRADICTED | 외전 1 · s030¶1677–1683; V15 p247–p251 | correct (reattribute; keep insight) | R1 AGREE |
| S1-04 | Map:388; Doc00:264 | "V15 p055–p059 visually realizes the farewell/dream endpoint". | The prose ends on the night of the sealing (¶1949–1950). | QUALIFY | 후일담 2 · s032¶1949–1950; V15 p058 | qualify (terminal p058) | R1 AGREE |
| S1-05 | Map:387–388; Doc11:84; D13:1567 | In the terminal prose sequence, Jinwoo judges that Suho cannot live normally, seals his power and his shadow-related memories, and the shadows bid farewell, ending in the dream (V15 p053–p059). | The sealing is explicitly temporary (`잠시`, ¶1908), with the condition "until he can control it completely" (¶1899). | LOCATED/CONFIRMED | 후일담 2 · s032¶1876–1897; V15 p052–p053 | locator-only | R1 AGREE |
| S1-06 | Map:343 | The dimensional-gap war and the return to the peaceful timeline come from "main ending + adjacent epilogue material", which Chapter 40 integrates and "Recomposes". | Apart from relocating the ch.243 note (¶1463 → p250) and merging the two reset passages (ch.243 ¶1458–1462 and 외전 2 ¶1781–1807 both end in `준비됐어` and the Cup's light, rendered once at p237–p243), V13 Chapter 40 adapts 외전 2–4 largely in prose order. | QUALIFY | ch.243 · s030¶1462–1465; 외전 3 · s030¶1946–2134; V13 p251–p263 | correct source to 외전 2–4 | R1 AGREE |
| S1-07 | Map:60; D13:1368 | V13 = `index_split_029–030` main-story finale "plus epilogue/side-story material from the remainder of split 030". | V13 does reach side-story material, but it stops in split 031, not inside split 030. | QUALIFY | 외전 4 · s031¶94; V13 p288; s031¶85–94 | qualify (s029¶~1470–s031¶94 minus ¶1464–1608) | R1 AGREE |
| S1-08 | D13:1442; Doc11:629; Map:345 | "Chugong's formal main story closes around Go Gunhee's restored heartbeat; the manhwa closes around Jinwoo's reason to remain" (ledger). | The usefulness question is stated verbatim in the prose: the goal achieved, power as spent nuclear fuel (¶72–74), the question at ¶77, and the answer through the girl running past (Cha, ¶85–88) and "people I love remain" (¶91–94). | QUALIFY | 외전 4 · s031¶68–94; V13 p276–p288 | qualify (explicitness is Chugong's) | R1 AGREE |
| S1-09 | Map:61; D13:1468 | V14 draws on the "remainder of `index_split_030` and substantial material from `031`". | V14 contains nothing from 외전 1–4, which are the only side stories in split 030. | LOCATED (with correction) | s031¶334–1892; s032¶34–237; s030¶1468–1608 | correct (split 031+032 + coda) | R1 AGREE |
| S1-10 | Map:62; D13:1567 | "Part 4 draws on late `외전`/`후일담` material in `index_split_031–032`". | The scene explicitly reprises the main-story ending: "about ten years ago" Jinwoo used the `생명의 신수` on him (¶1439–1440). | LOCATED | 외전 21 · s032¶1247–1523; 외전 21 · s032¶1438–1478; V15 p016–p028 | locator; 032 only | R1 AGREE |
| S1-11 | Doc11:224–238 | Jinwoo "does not reclaim the restored man"; "Kim Chul's residual affect toward Jinwoo can survive… Jinwoo permits that affect to remain incomplete"; "Continuity need not become renewed subordination." | Jinwoo does more than leave Kim Chul's affect alone. | QUALIFY | 외전 17 · s032¶544–579; V14 p128–p133 | qualify (memory editing) | R1 AGREE |
| S1-12 | Map:17–18; Doc00:58 | Only the first eighteen Korean headings survive, so later prose is cited by split region. | Headings survive throughout (see `chapters.tsv`), so every boundary in this report can carry a chapter locator. | CONTRADICTED | s030¶1353; s032¶650; s032¶1748 | correct (dup of P-01) | R1 AGREE |
| S2-01 | Map:24–26; Map:48–50; Map:429 | "Only the first eighteen Korean headings survive as explicit metadata"; V1–V3 are anchored to named headings (`프롤로그`, `E급 헌터`, … `전직 퀘스트`). | None of the 18 named headings exists as a heading line. | CONTRADICTED | s000¶192; s000¶2545; s003¶1496 | correct; retire Map:440 | R1 AGREE |
| S2-02 | Map:48; Map:70; Map:74 | V1 adapts only the first part of split 000 and ends at the System/hospital selection. | V1 therefore covers all of s000 (ch.1–13), not "headings 1–7". | CONTRADICTED | ch.13 · s001¶80–111; s000¶1471–1487; s000¶1804 | correct | R1 AGREE |
| S2-03 | Map:125 | V3 contains the class change and the first Arise. | The Igris duel, the knights and the Necromancer offer are in V3. | CONTRADICTED | ch.52 · s004¶1352–1376; s004¶1434; s004¶1477 | correct (row → V4) | R1 AGREE |
| S2-04 | Map:51–59; Map:135 | Split zones per volume (V4 005–007 … V12 026–029). | Chapter counts per volume: 13, 15, 24, 26, 23, 15, 11, 23, 21, 21, 24, 17. | CONTRADICTED | s000¶1; s001¶80; s002¶989 | correct (adopt table) | R1 PARTIAL |
| S2-05 | Map:209 | "The novel's crucial interior account of retained consciousness and frighteningly transformed loyalty is substantially reduced/absent" in the manhwa, which weakens immediate shadow-personhood ambiguity. | The manhwa preserves the account in the same delayed position. | CONTRADICTED | ch.122 · s013¶1620–1720; ch.151 · s016¶2290–2369; s016¶2544–2550 | correct (V7 → Preserved; V9 row) | R1 PARTIAL |
| S2-06 | Map:121; Doc10:289–291; Doc00:115 | The prose carries a diffuse concern about self-corruption, which the manhwa concentrates. | The prose shows a sharper act of Jinwoo's own cruelty than the Map row mentions, and frames it as retributive judgment without self-doubt. | QUALIFY | ch.32 · s002¶1840–1928; ch.34 · s002¶2046–2047 | qualify (keep quiet prose concern at ch.23) | R1 PARTIAL |
| S2-07 | Map:124; Doc10:305 | There is no direct prose counterpart to the old-self/new-self confrontation. | The prose already has an interior old-self confrontation at the same dramatic point. | QUALIFY | ch.49 · s004¶650–682 | qualify (drop Manhwa-original) | R1 AGREE |
| S2-08 | Map:295; Map:298; Map:291 | These belong to V11. | The manhwa keeps the prose order, so these rows belong to V10. | CONTRADICTED | ch.182 · s024¶1–92; ch.187 · s024¶949; s024¶2111 | correct (→ V10; also Map:296) | R1 AGREE |
| S2-09 | Map:299 | Go's death lies in splits 026–028. | The Go confrontation is entirely in split 025. | CONTRADICTED (zone) | s025¶1486–1810; ch.203 · s025¶2084; ch.204 · s025¶2284 | locator correction | R1 AGREE |
| S3-01 | D13:162; D13:1666; D13:1607 | "the courage of the powerless," a later interpretive anchor for pre-power moral agency; exact locator pending. | `무력한 자의 용기` is the System's secret-quest title, and the narration at that moment disclaims sacrifice | LOCATED+QUALIFY | ch.7 · s000¶1465; ch.25 · s002¶353–367; ch.7 · s000¶1394 | qualify (System label; ¶1407–1415) | R2 AGREE |
| S3-02 | D13:132; D13:168 | "He rejects Kim Sangshik's attempt to move blame onto Song after the group's own decision." | Jinwoo does not "reject" Kim's scapegoating of Song. He is silenced and later indicts himself for not helping | QUALIFY | ch.5 · s000¶1083–1092; ch.6 · s000¶1098–1114; ch.12 · s000¶2432–2438 | correct wording; add tie-break vote | R2 AGREE |
| S3-03 | D13:237–238; D13:266; D13:1667 | It becomes the explicit reciprocal frame: care and harm both call for return. | `기브 앤 테이크` begins as withdrawal of unconditional kindness. The two-sided "good and bad" form is stated later | CONFIRMED (+origin note) | ch.12 · s000¶2440–2448; ch.23 · s001¶2205–2208; ch.24 · s002¶86–89 | locator + qualify origin | R2 AGREE |
| S3-04 | D13:240; D13:279 | "He does not hunt the Dongsuk party for pleasure…"; "Volume 2 itself supports a narrower defensive reading." | V2 later correction: the Dongsuk killing is retributive, not merely defensive | QUALIFY | ch.22 · s001¶1975; ch.23 · s001¶2191–2213; ch.24 · s002¶72–75 | claim revision D13:279 | R2 AGREE |
| S3-05 | D13:415; D13:427; D13:449 | "Kim Chul's aggression makes defensive force necessary; turning him into Iron adds punitive and instrumental dimensions after death." | Kim Chul → Iron: Jinwoo engineers the confrontation to acquire a strong shadow | QUALIFY | ch.58 · s005¶336; ch.60 · s005¶821–827; ch.63 · s006¶556–559 | qualify; align with 04:799 | R2 AGREE |
| S3-06 | D13:524–533; D13:530–531; D13:545 | Opening: "Officially E-rank… willing to enter through low-status labor rather than reveal himself." Close: "Has requested formal reevaluation." | V5 order: Jinwoo is already de facto S-rank before the porter/mining raid | CONTRADICTED | ch.75 · s007¶1775–1785; ch.76 · s007¶2071–2090; ch.78 · s008¶198–214 | correct (claim revision) | R2 AGREE |
| S3-07 | D13:540 | Jinwoo "waits before intervening"; he asks permission (a crucial jurisdictional act) and protects the team. | Son Kihoon: permission is real and jurisdictional, but Jinwoo deliberately let him be battered to keep the monsters | QUALIFY | ch.88 · s009¶281; ch.91 · s009¶811–813 | qualify (add ¶811–813) | R2 AGREE |
| S3-08 | D13:656; D13:662 | "The manhwa's family-vocation additions make the choice more relational; the Korean novel more strongly emphasizes sovereign self-direction." Also: Jinwoo "has reason to believe Korea has assembled an elite force…" | The Korean Jeju refusal is explicitly relational, which contradicts "the novel stresses sovereign self-direction" for V6 | CONTRADICTED (656) / QUALIFY (662) | ch.111 · s011¶1882–1890; ch.113 · s012¶533–551 | correct | R2 PARTIAL |
| S3-09 | D13:768; D13:770–771; D13:802 | "TF: Byung-Gyu's known wishes and healer identity matter to Jinwoo's decision to release him." Temporary service is unresolved as to consent and uses the dead without prior consent. | Byung-Gyu: the located interior shows presumed-consent reasoning and a duty to the war dead. "Known wishes" is misassigned | QUALIFY | ch.122 · s013¶1626–1637; ch.129 · s014¶558–559 | correct TF; add ¶1635, ¶1721, ¶1754 | R2 PARTIAL |
| S3-10 | D13:734; D13:807; D13:1682 | "…the manhwa provides less access than the novel to the retained consciousness and transformed allegiance." The novel's account of Byung-Gyu's retained consciousness is reduced in the manhwa. | V7 horizon: the "retained consciousness / blind slave" revelation is not in the V7 Korean range. It arrives at ch.151, second-hand | QUALIFY | ch.151 · s016¶2333–2363; ch.153 · s017¶66–68 | relocate to ch.151; manhwa OPEN | R2 AGREE |
| S3-11 | D13:1305–1307; D13:1697; D13:815 | Bellion's and the older shadows' allegiance is sincere but not demonstrably recusant. | Jinwoo's rule against extracting innocents, and its deliberate breach, are absent from D13's shadow ethics | CONFIRMED (+omission) | ch.122 · s013¶1627–1629; ch.165 · s018¶1371–1372; ch.226 · s028¶1370–1381 | add ch.226 | R2 AGREE |
| S3-12 | D13:1300; D13:1306; D13:1318 | Ashborn "allows Jinwoo's `자아` and `의식` to remain and presents a genuine `선택`". | V12: Ashborn's offer uses `인격` and `동화` (fusion), not `자아`/`의식`. The stated reason to return is belonging, and loved ones sit on the "rest" side | QUALIFY | ch.220 · s028¶269–280; ch.243 · s030¶1425–1434 | fix KC; motive | R2 AGREE |
| S3-13 | D13:1145; D13:1387; D13:1401 | "Antares later offers Earth itself and receives the same refusal of ownership-through-strength." Antares offers rule, and Jinwoo refuses to infer ownership from victory. | Antares' offer: Jinwoo refuses out of distrust, not as a principled refusal of ownership-through-strength | QUALIFY | ch.241 · s030¶937–968 | qualify (distrust) | R2 PARTIAL |
| S3-14 | D13:1295; D13:1670 | "`일어나라` shifts from a class command supplied by an interface to Jinwoo's own sovereign speech." | `일어나라` was never "supplied by an interface". Jinwoo coined it | QUALIFY | ch.52 · s004¶1473–1477; ch.220 · s028¶362; ch.221 · s028¶365–368 | correct | R2 AGREE |
| S3-15 | D13:345; D13:309 | "The first extraction raises no explicit consent debate in the contemporary narrative." | First extraction: the narration frames it as liberating suffering souls, a quasi-consent framing | CONFIRMED (+note) | ch.52 · s004¶1466–1472 | qualify | R2 AGREE |
| S3-16 | D13:913; D13:872; D13:884–889 | Korean discussion of guild mechanics is assigned to the split-region locator, pending. | V8 guild mechanics: locator found. The founding material sits in s014, before D13's V8 range | LOCATED | ch.26 · s002¶566–569; ch.129 · s014¶583–598; ch.132 · s014¶1362–1377 | locator-only + range flag | R2 AGREE |
| S3-17 | D13:1131; D13:1091–1092; D13:1098 | Korean passages separate political guilt from civilian rescue. | V10 political guilt vs civilian rescue: locator found and confirmed. Japan decision confirmed as self-directed | CONFIRMED | ch.165 · s018¶1350–1357; ch.169 · s019¶666–690; ch.169 · s019¶694–729 | adopt locators | R2 AGREE |
| S4-01 | Doc01:52; Doc01:44; Doc02:56 | 01:52 ("nevertheless becomes the expendable person left at the altar"); 01:44; 02:56 ("still becomes the expendable body left on the altar"); 03:164 ("final disposability once the group's survival requires a … | The altar "sacrifice" was Jinwoo's own choice, not the group discarding him | QUALIFY | ch.7 · s000¶1336–1348; ch.12 · s000¶2441–2444; s000¶2442–2444 | correct | R2 AGREE |
| S4-02 | Doc02:205–219; Doc03:155 | 02:205–219 (§8, "one of the most important Korean anchors for Jinwoo"); 03:155. | `무력한 자의 용기` is the System's name for a secret quest, not authorial characterization | QUALIFY | ch.7 · s000¶1465; ch.25 · s002¶351–367; ch.220 · s028¶269–280 | qualify | R2 AGREE |
| S4-03 | Doc01:100; Doc02:421–431; Doc04:95 | 01:100; 02:421–431; 04:95, 04:209–231; README §3, implicitly. | `기브 앤 테이크` begins as withdrawal from unconditional kindness and as retribution, not as "care deserves care" | CONFIRMED (+order) | ch.12 · s000¶2432–2449; ch.23 · s001¶2189–2213; ch.24 · s002¶84–90 | qualify order only | R2 PARTIAL |
| S4-04 | Doc04:293–311; Doc04:798 | 04:293–311 ("Jinwoo executes him rather than returning him to public custody"; "SI: Jinwoo regards the prisoner's continued life as an unresolved danger"); 04:798. | The surviving prisoner was not simply "executed": he was bound, gagged and fed alive to hobgoblins as bait | QUALIFY | ch.34 · s002¶2044–2120; ch.32 · s002¶1705–1739; s002¶1705–1739 | correct (method, bait, motive) | R2 AGREE |
| S4-05 | Doc04:237–253; Doc02:449 | 04:237–253 (immediate threat; "surrender would expose Jinwoo... | Dongsuk-party killings: the leader was killed incapacitated and begging, and Jinwoo had resolved on no mercy before the System quest appeared | QUALIFY | ch.22 · s001¶1972–1975; ch.23 · s001¶2176–2229 | qualify | R2 AGREE |
| S4-06 | Doc04:398–426; Doc01:356; Doc02:276 | 04:398–426 ("not compelled by fear, law..."; "He can stop when the threat has ended"); 01:356; 02:276, 02:533; 03:760 ("He repeatedly stops when threats are neutralized"). | Thomas "mercy": Jinwoo ignored the plea to stop and halted only when Thomas surrendered; his own reasoning cites legal exposure and deterrence | QUALIFY | ch.192 · s025¶70–87; ch.194 · s025¶355–361; ch.197 · s025¶900–911 | qualify | R2 AGREE |
| S4-07 | Doc04:720–750; Doc04:762–776; Doc01:446 | 04:720–750 (resurrection "can restore a victim's voice"; "a murdered person can become a witness"; "the information can support ordinary investigation rather than replace truth"); 04:762–776 ("prolonged supernatural terror"; "conditional supernatural … | Detective-era punishment is a recurring private program of indefinite torture, the case is publicly closed, and the "murdered witness" was a suicide | CONTRADICTED | 외전 20 · s032¶1059–1076 | correct | R2 AGREE |
| S4-08 | Doc04:567; Doc03:530; Doc04:552–559 | 04:567 ("His mother's objection still matters. | In prose, Jinwoo's mother does not ask him not to go to Japan; the motive given is sovereign will, wanting to fight, and monster rights | NOT-FOUND (prose) / QUALIFY | ch.154 · s017¶292–313; ch.169 · s019¶510–572; ch.170 · s019¶805–821 | correct or relabel; manhwa OPEN | R2 PARTIAL |
| S4-09 | Doc04:111; Doc04:225; Doc01:327 | 04:111 ("He rejects social Darwinism: weakness is never guilt"); 04:225 ("Jinwoo never becomes a social Darwinist"); 01:327. | "Never a social Darwinist": Jinwoo explicitly agrees that "the weak get eaten" and razes demon houses for experience | QUALIFY | ch.103 · s011¶194–225; ch.105 · s011¶624–642 | qualify (scope to humans) | R2 AGREE |
| S4-10 | Doc04:341–362; Doc04:792; Doc02:465 | 04:341–362; 04:792 ("He rarely prolongs combat merely for entertainment"); 02:465 ("rarely seeks suffering as entertainment"). | Kargalgan: deliberate prolongation and visible satisfaction cut against "not sadism" and "rarely prolongs combat for entertainment" | QUALIFY | ch.88 · s009¶175–188; ch.90 · s009¶700–759 | add counterexample; keep "merely" | R2 PARTIAL |
| S4-11 | Doc04:372–374; Doc04:855 | 04:372–374 ("Jinwoo's first ethical priority is correct: rescue the victim... | Hwang Dongsoo: Jinwoo beats Hwang while asking the battered Jinho to hold on; "punishment precedes healing" in the sequence | QUALIFY | ch.190 · s024¶1700–1758; ch.190 · s024¶1785–1832; ch.193 · s025¶250–262 | qualify | R2 AGREE |
| S4-12 | Doc01:378; Doc02:575; Doc03:556–568 | 01:378 ("continuity of `자아` and `의식`... | Inheritance is described as a fusion of Jinwoo's and Ashborn's consciousnesses; Ashborn chose Jinwoo against the Architect; `자아`/`의식` come from Min's testimony | QUALIFY | ch.220 · s028¶255–308; ch.243 · s030¶1405; ch.151 · s016¶2339 | correct KC; merger | R2 AGREE |
| S4-13 | Doc01:404; Doc03:582–614; Doc04:887 | 01:404 ("The people whose histories will be replaced do not vote, consent..."); 03:582–614; 04:887 (table: "Jinwoo alone can alter history"); 02:639; 04:980–1025. | The reset is executed by the Rulers, within a practice of repeated resets; Jinwoo informed Woo (and Selner) beforehand | QUALIFY | ch.243 · s030¶1376–1461; ch.220 · s028¶287; 외전 11 · s031¶1483–1502 | qualify; strike "plan disclosed" | R2 PARTIAL |
| S4-14 | Doc04:686–714; Doc04:337; Doc04:916 | 04:686–714 (the memory spectrum: "Kim Chul retains affective traces"; "Juhee's peaceful unawareness"); 04:337 and 04:916 ("avoids reclaiming restored Kim Chul as Iron"); 04:692. | Memory: Jinwoo states he has no right to choose others' memories, yet hypnotizes Kim Chul and implants false memories | QUALIFY | 외전 10 · s031¶1296–1319; 외전 17 · s032¶518–572; 외전 20 · s032¶1211 | qualify (memory editing) | R2 AGREE |
| S4-15 | Doc01:56–60; Doc01:295; Doc02:589 | 01:56–60 ("The instrument that widens Jinwoo's choices is itself an instrument designed to use him"); 01:295 and 02:589 (the "devour the System" formulation is adaptation-specific; "The Korean novel develops the … | The prose has an explicit appropriation formula toward the System, and an affectionate farewell to it | QUALIFY | ch.22 · s001¶2031–2048; ch.221 · s028¶365–372; ch.229 · s029¶623–641 | qualify | R2 AGREE |
| S4-16 | Doc01:124; Doc01:130; Doc02:469 | 01:124 and 01:130 (the manhwa's "broken inside" imagery "strengthens one danger without proving that the Korean novel states the same thoughts"); 02:469; 04:257. | The novel has its own "has something changed inside me" moment, at the first human killings | QUALIFY | ch.23 · s001¶2222–2229; ch.33 · s002¶1927–1932; s001¶2222–2229 | qualify | R2 AGREE |
| S4-17 | Doc02:272 | 02:272 ("Thomas Andre, whose own history of weakness has hardened into an expectation that superior force should settle jurisdiction"). | Thomas's backstory is poverty and innate dominance, not "weakness" | QUALIFY | ch.191 · s024¶1837–1862 | correct premise | R2 PARTIAL |
| S4-18 | Doc01:74; Doc02:83; Doc03:73 | 01:74 ("rejects an attempt to transfer the group's collective responsibility onto Song Chiyul"); 02:83; 03:73; 04:154. | The decisive tie-break vote to enter the Double Dungeon was Jinwoo's, cast for money; the "scapegoat" rejection is internal and silenced by powerlessness | QUALIFY | s000¶173–208; s000¶1082–1114 | qualify (tie-break vote) | R2 AGREE |
| S4-20 | Doc01:243; Doc04:447 | 01:243 ("Byung-Gyu's prior identity and known wishes matter"); 04:447 ("Min's prior life was defined partly by reluctance toward combat"). | Min's release: the prose reason is duty to the war dead and lack of "authority", not "known wishes" or "reluctance toward combat" | QUALIFY (both lines) | ch.122 · s013¶1626–1637; s013¶34–44; ch.129 · s014¶554–559 | qualify; keep 04:447 fact as post-hoc | R2 DISAGREE |
| S4-21 | Doc04:695; Doc04:708; Doc04:834 | 04:695 ("Lee Juhee is allowed to live without the dungeon trauma"); 04:708; 04:834; 04:917. | Juhee in the reset world: not found | NOT-FOUND |  | correct unless manhwa source | R2 AGREE |
| S4-23 | Doc02:258; Doc01:402; Doc03:400 | 02:258 ("the offer misunderstands Jinwoo because ownership of Earth is not one of his wants"); 01:402; 03:400; 04:530. | Antares's offer is refused because of detected deceit, and it was more than "ownership of Earth" | QUALIFY | ch.241 · s030¶937–966 | qualify | R2 PARTIAL |
| S4-25 | Doc00:97; Doc02:56; Doc02:260–264 | README 00:97; 02:56, 02:260–264; 03:233–237. | Executive thesis: "non-subordination over domination" is explicitly stated, but coexists with stated appetite and a kingship-as-will motif | QUALIFY | ch.75 · s007¶1778–1780; ch.191 · s024¶1908; ch.122 · s013¶1693–1694 | qualify (appetite co-motive) | R2 AGREE |
| S5-01 | Doc12:139; Doc12:292; Doc00:285 | `Jin-i` is an "unverified architecture label"; no identity established. | `Jin-i` resolved: a released human shadow in the final side story | LOCATED | 외전 19 · s032¶981; 외전 20 · s032¶1059–1079; s016¶2707 | correct (fill matrix row) | R2 AGREE |
| S5-02 | Doc06:160; Doc11:226–238; Doc08:852 | Jinwoo "does not insist on reclaiming" the restored Kim Chul, which the corpus calls "one of the strongest pieces of evidence for a more humane mature sovereign ethic" (06:233). | Iron/Kim Chul: the "restraint" is a mechanical reset rule, followed by hypnotic memory replacement | CONTRADICTED | ch.243 · s030¶1451–1458; 외전 5 · s031¶244–246; 외전 16 · s032¶431 | correct | R2 AGREE |
| S5-03 | Doc11:558–580; Doc12:194; Doc07:1074–1076 | "When confronted with an abusive offender, he first protects the victim… once immediate danger is controlled… prolonged supernatural punishment." The case "proves he still reserves a private exception." | The abuser case: there is no victim left to protect, and the punishment is a practice, not an exception | CONTRADICTED (11:562) / CONFIRMED (punishment) | 외전 19 · s032¶1004–1007; 외전 20 · s032¶1133–1134; 외전 21 · s032¶1423–1427 | correct + reframe as practice | R2 PARTIAL |
| S5-04 | Doc12:192; Doc12:147–151; Doc06:686–714 | `12_…:192` ("No clear mechanism of refusal, exit, or allegiance independent of Monarch ontology is demonstrated"); `12_…:147–151`; `06_…:686–714`, `:94`, `:267`, `:928`; `05_…:133`. | Shadow refusal/exit: confirmed in substance, but the text supplies counterexamples and its own mechanism | CONFIRMED (+evidence) | ch.100 · s010¶1186–1190; ch.122 · s013¶1719–1722; ch.124 · s013¶2240–2244 | adopt added wording | R2 PARTIAL |
| S5-05 | Doc06:90; Doc05:649; Doc12:138 | `06_…:90`, `:277–321`, `:678`, `:874`; `05_…:649`; `12_…:138`. | Min Byung-gu's "overwhelming pleasure in serving": located, but it is relayed near-death testimony | CONFIRMED | ch.122 · s013¶1620–1722; ch.122 · s013¶1745–1752; ch.129 · s014¶558 | locator; "relayed"; Byung-gu | R2 AGREE |
| S5-06 | Doc11:288; Doc05:461; Doc08:849 | `11_…:288`, `:305–317`; `05_…:461`, `:597`, `:800`; `08_…:849`; `12_…:112`. | Il-hwan "chooses forgetting": correct, but only after about a year of secret remembering | QUALIFY | 외전 18 · s032¶651–669 | qualify | R2 PARTIAL |
| S5-07 | Doc08:66; Doc12:79 | `08_…:66`, `:213–223`, `:498–524`, `:528–552`, `:1009–1019`, `:984–985`; `12_…:79`, `:209`. | Ashborn, not the Architect, chose Jinwoo; and the inheritance is framed as a fusion of personalities | QUALIFY | ch.220 · s028¶252–323; ch.243 · s030¶1405; s030¶1405 | qualify | R2 AGREE |
| S5-08 | Doc07:1001–1007; Doc08:757–775; Doc12:205 | `07_…:1001–1007`; `08_…:757–775`, `:1027–1031` ("He explicitly rejects political dominion"); `12_…:205`. | Antares's offer of Earth is refused out of distrust, not as a stated principle | CONTRADICTED (08:1031) / QUALIFY | ch.241 · s030¶934–962; s031¶1764–1768 | correct; rebase on 외전 12 | R2 PARTIAL |
| S5-09 | Doc05:511–517; Doc07:1101; Doc12:77 | Jinwoo "recognizes the strike-team leader's jurisdiction and asks before taking the monsters." | Son Kihoon's "jurisdiction" was engineered: Jinwoo let him be broken so he would hand over the kill | QUALIFY | ch.88 · s009¶277–317; ch.91 · s009¶811–813 | qualify | R2 AGREE |
| S5-10 | Doc11:29–39; Doc08:252–254; Doc07:1048–1084 | `11_…:29–39`, `:1080–1091`; `08_…:252–254`, `:872–904`; `07_…:1048–1084`. | The post-reset world is not emergency-free; Jinwoo's own presence draws an invasion | QUALIFY | 외전 4 · s031¶40–76; 외전 12 · s031¶1686–1891; 외전 15 · s032¶63–205 | qualify (self-caused emergency) | R2 AGREE |
| S5-11 | Doc05:58; Doc12:104 | `05_…:58`, `:155–163`, `:613`, `:643`, `:756–758`; `12_…:104`. | Mother asks him not to go to Japan: not in the prose | NOT-FOUND (prose) | ch.154 · s017¶298–312; ch.127 · s014¶252–255; ch.169 · s019¶658–691 | correct or relabel; manhwa OPEN | R2 PARTIAL |
| S5-12 | Doc11:463–507 | `11_…:463–507`. | 외전 14 ("나 혼자만 만렙") swaps the person rather than adding power | QUALIFY | 외전 14 · s031¶2078–2237; s032¶1–13; s032¶5–13 | qualify description | R2 AGREE |
| S5-13 | Doc11:915–968 | `11_…:915–968` (esp. | "Beautiful World" support-department question: Chugong's 외전 1 already contains it | QUALIFY (prose analogue LOCATED) | 외전 1 · s030¶1612–1777 | narrow boundary now; game frame OPEN | R2 DISAGREE |
| S5-14 | Doc11:171–183; Doc05:423–429; Doc12:196 | `11_…:171–183`, `:286`; `05_…:423–429`, `:798`; `12_…:196`. | Woo's memory: Jinwoo refused to restore it; it returned through an accidental touch | QUALIFY | 외전 6 · s031¶335–345; 외전 10 · s031¶1295–1319; 외전 11 · s031¶1425 | qualify | R2 AGREE |
| S5-16 | Doc11:513–538; Doc07:1062–1068; Doc12:194 | `11_…:513–538`, `:1105`; `07_…:1062–1068`; `12_…:194`. | Police career: "voluntary" entry was Woo's recruitment of the vigilante | QUALIFY (minor) | 외전 11 · s031¶1598–1612; 외전 19 · s032¶882–887; 후일담 2 · s032¶1827–1849 | qualify | R2 PARTIAL |
| S5-17 | Doc07:647–653; Doc07:1165 | `07_…:647–653`; `07_…:1165` (table row). | Goto Ryuji was not an association leader | CONTRADICTED | ch.104 · s011¶291–303; ch.105 · s011¶690; ch.106 · s011¶837–859 | correct | R2 AGREE |
| S5-19 | Doc08:779–800; Doc11:92–105; Doc06:744–766 | `08_…:779–800`, `:820`, `:1063`; `11_…:92–105`; `06_…:744–766`. | The Cup, the reset's conditions, and the length of the hidden war | CONFIRMED | ch.220 · s028¶206–208; ch.243 · s030¶1392–1458; 외전 3 · s030¶1966–1972 | locator; add figures | R2 AGREE |
| S5-20 | Doc06:553–560; Doc08:922–936; Doc11:84 | `06_…:553–560`; `08_…:922–936`, `:944`; `11_…:84`, `:760–796`; `12_…:197`. | Suho's seal: the conditions and the trigger | CONFIRMED | 후일담 2 · s032¶1752–1950 | locator-only | R2 AGREE |
| S6-01 | Doc09:251; D13:1295; Doc01:382 | after the System disappears, `일어나라` becomes "Jinwoo's own speech rather than an interface-enabled class function". | The command word was never supplied by the interface. | QUALIFY | ch.52 · s004¶1474–1477; ch.159 · s018¶174; ch.220 · s028¶362 | qualify | R1 AGREE |
| S6-02 | Doc09:119–135; Doc00:238; D13:162 | `무력한 자의 용기` is a moral phrase. | The phrase is the **title of a System secret quest**, not narratorial or character vocabulary. | QUALIFY | ch.7 · s000¶1450–1487; ch.25 · s002¶353–367; s000¶1465 | qualify/correct (keep ethic) | R1 AGREE |
| S6-03 | Doc09:77–109; Doc00:236; Doc01:54 | `인류 최약병기` means "humanity's weakest weapon", richer than "weakest hunter". | The joke is a **pun**. | QUALIFY | ch.1 · s000¶60–71; ch.11 · s000¶2324; s000¶64 | qualify (pun; bookend = interpretation) | R1 AGREE |
| S6-04 | Doc09:171–197; Doc09:486–490; Doc09:625 | `형님` marks "hierarchy becoming chosen kinship". | The lexical sequence runs the **opposite way** to the corpus's arrow. | QUALIFY | ch.18 · s001¶1045; ch.22 · s001¶1888–1909; ch.57 · s004¶2477 | qualify | R1 AGREE |
| S6-05 | Doc09:385–398; Doc09:504–508; Doc09:631 | `살의` = killing intent, part of Jinwoo's threat assessment; "later he can project fear or murderous pressure himself". | The gloss "intent to kill" is right. | QUALIFY | ch.22 · s001¶1979–2023; ch.23 · s001¶2216–2262; ch.101 · s010¶1464–1467 | correct (add 살기) | R1 AGREE |
| S6-06 | Doc09:416–418; Doc09:633; D13:1300 | Ashborn "allows Jinwoo's `자아` and `의식` to remain". | The inheritance passage does not use `자아` or `의식`. | QUALIFY | ch.220 · s028¶303–324; s028¶307; s017¶67 | qualify (인격/동화) | R1 AGREE |
| S6-07 | Doc09:39; Doc09:261–263; Doc09:341–351 | The novel's signature is "density of continuous thought". | Quoted interior thought peaks in ch.41–80 (~110 per 1,000 paragraphs, all speakers) and **roughly halves** from ch.161 onward (~45–55). | QUALIFY | ch.212 · s026¶1672; ch.231 · s029¶1030–1063; 후일담 2 · s032¶1749 | qualify (state method; main-story trend only) | R1 PARTIAL |
| S6-08 | Doc09:355–375 | The novel is organised around Jinwoo's perspective but is "not locked into a single uninterrupted first-person consciousness". | The main story is **third person throughout**. | QUALIFY/strengthen | ch.1 · s000¶19–25; 외전 1 · s030¶1621–1640; 외전 5 · s031¶97–103 | qualify (third person; 4 first-person narrators) | R1 AGREE |
| S6-09 | Doc09:201–219; Doc09:492–496; Doc09:627 | `군주` = monarch, lord, sovereign or ruler. | The gloss is fine, and the first use is indeed a game-like class change, `네크로맨서`→`그림자 군주` (s004¶1434–1447). | QUALIFY | ch.52 · s004¶1434–1447; ch.15 · s001¶482; ch.175 · s019¶1842 | qualify (왕/지배자/주군) | R1 AGREE |
| S6-10 | Doc09:29; Doc09:574–578; Doc09:647 | the omnibus is "bibliographically flattened after its first eighteen preserved headings"; later citation must use split + scene anchors. | Numbered `N화` headings survive throughout the main story, every 외전 heading survives with its subtitle, and both 후일담 headings survive. | CONTRADICTED | s001¶1884; s030¶1612; s032¶1526 | correct | R1 AGREE |
| S6-11 | D13:36; D13:90; D13:195 | surviving Korean headings include `프롤로그`, `페널티`, `일일 퀘스트`, `레벨 업!`, `도마뱀들`, `기브 앤 테이크`, `정리`, `거래`, `우연`, `B급 강태식`, `이상한 레이드`, `대박의 예감`, `전직 퀘스트`. | None of these strings is a heading in the body text. | CONTRADICTED | s000¶2445; s001¶1448 | correct (EPUB nav inspected) | R1 PARTIAL |
| S6-12 | Doc00:285 | the `Jin-i` shadow label cannot be identified. | `진이` is **서진이 (Seo Jin-i)**, a young woman whose death was ruled a suicide. | LOCATED | 외전 19 · s032¶1036–1056; 외전 20 · s032¶1059–1079; s032¶1056 | close UA; add to matrix + memory ledger | R1 AGREE |
| S6-13 | D13:1020 | `기브 앤 테이크` "remains more prominent" in the Architect/Black Heart volume. | The phrase does not occur in splits 017–019. | CONTRADICTED (minor) | ch.12 · s000¶2445; ch.23 · s001¶2205; ch.24 · s002¶86 | correct | R1 AGREE |
| S6-14 | D13:1126 | `거인왕` — King of Giants. | 0 hits for `거인왕`. | QUALIFY/NOT-FOUND | s019¶1842 | correct to 거인들의 왕 | R1 AGREE |
| S7-01 | GoGunheeModel:631; GoGunheeModel:575; GoGunheeModel:758 | `index_split_027` "reset encounter: negotiates with reset-world Jinwoo; personality continuity… concern over suicidal promise." | The s027 Go scene happens inside a world the Shadow Monarch says was built from Jinwoo's "desire to undo mistakes" (s027¶1243–1257). | CONTRADICTED | ch.218 · s027¶1155–1205; ch.218 · s027¶1220–1257; ch.243 · s030¶1562–1606 | correct (illusion) | R1 AGREE |
| S7-02 | SungJinwooModel:265 | He frames a regulatory bargain with Go: clearing Jeju's ants in exchange for summons counting as raid members (`index_split_027`). | The bargain exists only in the ch.218 illusion (see S7-01). | QUALIFY | ch.218 · s027¶1171–1205; ch.145 · s016¶974–1032; s016¶993 | qualify (label illusion) | R1 AGREE |
| S7-03 | GoGunheeModel:238–244 | Against the Frost Monarch "institutional language drops away… This is not a hidden alternate personality. | Go first speaks as himself, in polite 하오체 (`당신은 누구요?`, ¶1531), and does not understand the monster's references to a "vessel" (¶1553–1554). | CONTRADICTED (fusion caveat) | ch.200 · s025¶1529–1584; s008¶374–378; s013¶874 | correct (vessel–Ruler fusion state) | R1 PARTIAL |
| S7-04 | YooJinhoModel:67 | Jinho endures "torture rather than falsely implicating Jinwoo"; he "is asked to give a single false accusation." | Hwang Dongsoo wants confirmation that Jinwoo killed Hwang Dongsuk. | CONTRADICTED | ch.189 · s024¶1508–1549; ch.23 · s001¶2203–2218; s001¶2203–2218 | correct | R1 AGREE |
| S7-05 | GoGunheeModel:392; GoGunheeModel:755 | Go keeps "respectful adult-to-adult address" toward Jinwoo; the speech-level ledger is left open. | Go uses four distinct speech levels, chosen by relationship: honorific to Jinwoo and the public, 하게체 to juniors, 하오체 for adversarial diplomacy, plain speech in private. | QUALIFY/LOCATED | ch.78 · s008¶180–290; ch.145 · s016¶1026–1035; ch.201 · s025¶1840–1884 | add speech-level ledger | R1 AGREE |
| S7-06 | SungJinwooModel:995 | Reset-world Jinwoo "selectively reveals nothing about erased history"; do not have him explain the full truth because someone asks. | Jinwoo tells reset-world Go outright that they fought together in an erased timeline. | QUALIFY | ch.243 · s030¶1574–1576; 외전 21 · s032¶1456–1463; 외전 10 · s031¶1298–1319 | qualify | R1 AGREE |
| S7-07 | SungJinwooModel:263 | He "explicitly explains refusal without hostility" when declining Yujin (`index_split_003`). | The explanation (¶773, ¶778) is delivered as a planned warning. | QUALIFY | ch.42 · s003¶733–790; ch.43 · s003¶985–1004 | qualify | R1 AGREE |
| S7-08 | SungJinwooModel:1188 | With time, he observes before confronting; direct or hostile register is for established enemies. | When Hunter Bureau agent Adam White shows him photographs of his father, Jinwoo seizes him by the collar (telekinesis is confirmed at ¶288) before hearing the explanation. | QUALIFY | ch.183 · s024¶205–255; ch.183 · s024¶261–274 | qualify (father trigger) | R1 AGREE |
| S7-09 | SungJinwooModel:518–537 | Early romantic-social blindness; with Cha "initially guarded/practical." | The hypothesis order is exact: Association involvement, contract, money, then a hidden motive (¶1420–1455). | QUALIFY (minor) | ch.13 · s001¶9–42; ch.133 · s014¶1419–1492; ch.134 · s014¶1645–1654 | qualify (early teasing) | R1 PARTIAL |
| S7-10 | WooJinchulModel:729 | `index_split_030` "Reflects on Jinwoo's burden: humility, uncertainty, trust, prayer-like hope." | Three days after losing contact, Woo considers that Jinwoo may already have fled to another world. | QUALIFY | ch.238 · s030¶294–327 | qualify | R1 AGREE |
| S7-11 | WooJinchulModel:404–406 | Adult reset-world Woo "can state that he trusts Jinwoo whatever Jinwoo does" (an institutional risk). | Police chief Woo raises a disappearance in which every CCTV camera failed. | QUALIFY (stronger) | 외전 21 · s032¶1404–1434 | qualify (active suppression) | R1 AGREE |
| S7-12 | SungJinwooModel:1236 | He "is capable of living happily inside ordinary institutions." | Detective Jinwoo works around the institution: he meddles in colleagues' cases and is implied to be behind a disappearance with disabled CCTV, which his chief then buries. | QUALIFY | 외전 21 · s032¶1410–1428; 후일담 2 · s032¶1847 | qualify; cite 외전 20 ¶1195–1222 | R1 AGREE (+under-reach flag) |
| S7-13 | SungJinwooModel:687–712 | The register model (polite to legitimate authority, familiar with family, compressed shadow commands, enemy register); the speech-ending ledger is left open. | The model never names the archaic/sovereign level (하게체 `-나?`, `그대`; 해라체 `-마`, `-라`) that Jinwoo uses with shadows, monsters and cosmic agents. | LOCATED + QUALIFY | ch.229 · s029¶597; 외전 12 · s031¶1698–1764; ch.143 · s016¶585–587 | add register ledger + father exception | R1 PARTIAL |
| S7-14 | ChaHaeInModel:140–255 | Professional speech is economical and direct; intimate speech is compressed and hesitant; the address trajectory is left open. | Exact matches for `당신... | LOCATED/CONFIRMED | ch.134 · s014¶1700; ch.150 · s016¶2123; ch.165 · s018¶1430 | adopt | R1 AGREE |
| S7-22 | ChaHaeInModel:319 | "Asks others to investigate Jinwoo." | No such request was found. | LOCATED (minor) | ch.92 · s009¶1103–1108 | locator-only: ch.84 · s008¶1583–1595 | R1 DISAGREE |

## 9. Open items and remaining evidence obligations

1. **V14 correspondence was sampled** at every third page, and V15 Parts 5–6 at about 45 of 207 pages. Ranges marked `~` may be off by about two pages.
2. **The V6/V7 and V7/V8 boundaries** were sampled and may shift by a scene.
3. **The 외전 18 exam-morning coda** (s032¶752–773) was not located in the manhwa.
4. **About 300 claims were confirmed as stated** and did not need review. They are recorded only in the participants' working files, by count. Their locators can be regenerated on request but are not individually published here.
5. **No claims in Document 10 or Document 12 were audited for their own sake.** Document 12 propositions that depend on corrected claims are listed in the register rows.
6. **The reconstruction models still need full dialogue/register validation** and withheld-scene testing. This audit is a first pass, not that validation.
7. **The original Korean-language manhwa remains unavailable.** Translation claims about manhwa balloons remain out of scope.

## 10. Correction route (proposed, not executed)

The v1 release is hash-bound, and its analytical documents are current authority. Under routing §4.2 and the checklist's correction procedure, demonstrated errors should not stay presented as unqualified current authority. The narrowest legitimate routes, in increasing order of effort:

1. **Errata pointer (minimum).** A targeted entrypoint amendment in `00_README_AND_CORPUS_MAP.md` §12 that points to this audit as the current errata register. This changes one maintained file and its recorded checksum, both recorded as an administrative errata change.
2. **Claim revisions in the canonical homes.** Targeted edits in Documents 01–13, the map and the models, using the archive vocabulary (`REVISE`, `DOWNGRADE`, `REJECT`, `STRENGTHEN`), each citing a register ID, with the manifest and checksums regenerated as a v1.1 release.
3. **A v2 corrected edition.** Use this when the cumulative revisions to Documents 04, 06, 09, 11 and 12 justify a superseding release rather than inline edits.

Choosing a route is an owner decision. Until it is made, this record is the place to check before relying on any v1 claim listed in §8.
