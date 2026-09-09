---
series: CHIRAMUNE
artifact_type: supplemental_reading_and_checkpoint
scope: VOLUME_03_ILLUSTRATION_AND_SS_BOOKLET
source_boundary: "Japanese Volumes 01-03 with the main V03 state frozen at commit 3f35cef3908d22d45fcffa99a271f44c8bd97dfe; exact separate V03 illustration/SS booklet integrated as SUPPLEMENTAL_MAINLINE; no V04+ evidence"
generation: V0.1
status: active_provisional
release_state: frozen_source_boundary
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune Volume 03 supplemental booklet reading and checkpoint

## Responsibility and control state

This artifact classifies and integrates the separately packaged *『千歳くんはラムネ瓶のなか 3』イラスト＆SS小冊子* only after the complete main Volume 03 transaction was frozen, published, and independently verified at commit `3f35cef3908d22d45fcffa99a271f44c8bd97dfe`.

The booklet was not used to construct or silently rewrite `CHIRAMUNE_V03_DEEP_READING.md` or `CHIRAMUNE_V03_PROSPECTIVE_FREEZE.md`. It tests that frozen state as a later-admitted supplemental witness. No Volume 04 or later source entered this reading.

## 1. Exact source identity

| Field | Verified value |
|---|---|
| Source object | Volume 03 illustration and SS booklet EPUB |
| Drive file ID | `1St3ayvwF-7uzbjk4xQT0074B9rwr4AyC` |
| SHA-256 | `0edde35a6a9ec238c31aefc3ede00aca5ab1276a9d2c9eaa01a67da787eb70fd` |
| OPF title | `『千歳くんはラムネ瓶のなか 3』イラスト＆SS小冊子` |
| OPF creator / publisher / language | `裕夢` / `小学館` / `ja` |
| Colophon publication date | 2020-04-17 |
| Colophon production / cooperation | BOOK☆WALKER / Shogakukan Gagaga Bunko editorial department |
| Spine contents | cover; one untitled prose SS; one dedicated illustration; colophon |

The OPF's `dcterms:modified` value is 2018-01-12, which predates this Volume 03 object and is not used as publication evidence. The internal colophon controls the publication-date claim. The prose unit has no separate internal title; none is invented here.

The locally generated retrieval table contains 58 non-empty text/image rows and has SHA-256 `ef24def69765ad5203f707b176e24baa8e55477f00bfa7f08d12980fee496bea`. Supplemental locators use the source-qualified prefix `V03B` plus XHTML resource and paragraph/image order, for example `[V03B:p-001#p0053]` and `[V03B:p-002#img01]`. Unprefixed `[p-0031#...]` locators below refer to the main V03 witness.

## 2. Classification and insertion boundary

### Object class

**Primary analytical role: `SUPPLEMENTAL_MAINLINE`.**

The booklet is an official, separately acquired purchase-bonus object rather than prose embedded in the main Volume 03 EPUB. Its fiction adds an in-continuity scene to late Volume 03. It is therefore not classified as the main EPUB's `BONUS_FICTION`, and it is not made part of the numbered V03 prospective freeze after the fact.

The cover and colophon are `PARATEXT` components of this supplemental object. The dedicated Yuzuki image is visual evidence for the attached fiction, not an independent narrative source.

### Diegetic placement

The story opens while Saku is messaging Yuzuki on the return train from Tokyo. It then moves to Fukui after he has separated from Asuka and bought Kuranosuke Hachiban Ramen `[V03B:p-001#p0008-p0011]`. Those details align it precisely with the main novel after the station return, Asuka's meeting with her father, and Kuranosuke's request for Hachiban `[p-0031#p0452-p0508]`, but before the main novel advances to Monday after school `[p-0031#p0512]`.

**Diegetic insertion:** late V03, between `[p-0031#p0508]` and `[p-0031#p0512]`.

**Prospective reading boundary:** after the complete V03 main freeze. The booklet itself warns that it contains major spoilers and should be read only after the main volume `[V03B:p-001#p0004]`. Diegetic earliness does not override that dependency.

## 3. Scene structure

1. Saku reports the Tokyo outcome to Yuzuki because she was the person who pushed him to act `[V03B:p-001#p0008-p0009]`.
2. After the tense trip, Yuzuki's mock-criminal phone directions and their familiar improvisation make him feel he has returned home `[V03B:p-001#p0015-p0024]`.
3. Yuzuki is waiting beside Happiring in a cap, hoodie, shorts, and bubble-gum pose. She claims coincidence, then asks for a souvenir `[V03B:p-001#p0026-p0039]`.
4. Saku realizes he brought Tokyo Banana for Asuka's father but nothing for the person who enabled the trip `[V03B:p-001#p0040]`.
5. Yuzuki jokes that she would have consoled him if Asuka rejected him, then reads his relieved expression through a deliberately sexualized tease `[V03B:p-001#p0041-p0047]`.
6. She places her cap on him, surrounding him with her shampoo scent. In a slightly weaker voice she calls the act an “overwrite” without naming its object `[V03B:p-001#p0048-p0056]`.
7. Saku invites her for coffee; she accepts on the condition that he pay. As they leave in ordinary banter, he thinks her shampoo scent remains in his hair `[V03B:p-001#p0057-p0061]`.

## 4. Supplemental findings

### S03-B01 — Yuzuki's nonpossessive love remains competitive

**Class:** FACT + INFERENCE

**Confidence:** high for competition; medium-high for the precise referent of “overwrite”

The main V03 freeze established that Yuzuki can help Saku move toward Asuka even when doing so weakens her own romantic position. The booklet prevents “nonpossessive” from being misread as emotionally neutral or self-erasing. She seeks him immediately after the trip, checks whether he was rejected, and leaves a sensory trace she calls an overwrite `[V03B:p-001#p0041-p0056]`.

The most economical inference is that she is overwriting Asuka's recent romantic/sensory presence with her own. The text deliberately leaves the object unstated, so the claim must remain an inference rather than a quoted confession. What is explicit is Yuzuki's chosen intervention into the post-Asuka emotional field.

**Revision:** V03 `F36` is strengthened and qualified. Love is non-sabotaging, not noncompetitive.

### S03-B02 — familiar play becomes a form of homecoming

**Class:** FACT + INFERENCE

**Confidence:** high

Saku's return to Fukui is registered not only through air, landscape, or residence. Yuzuki's recognizable improvisational rhythm releases tension and produces the felt sense of being home `[V03B:p-001#p0018-p0019]`. This makes locality relational: “home” is also a practiced interaction in which he can answer theatricality with theatricality without directing a crisis.

The scene does not make Yuzuki the sole meaning of home. It does show that she is already embedded in Saku's ordinary belonging.

### S03-B03 — authored performance carries a vulnerable bid

**Class:** FACT + INFERENCE

**Confidence:** high

Yuzuki does not abandon her performed fluency in order to become sincere. She uses mock-criminal directions, claimed coincidence, sexual teasing, a cap, and an elliptical verb to make a vulnerable claim while preserving room to retreat. The text marks the emotional pressure through her slightly weaker voice rather than through a direct declaration `[V03B:p-001#p0048-p0056]`.

This extends the current authenticity model. Performance is not concealment opposed to intimacy; it is the authored form through which Yuzuki can risk intimacy. Its cost is ambiguity: Saku can receive the touch and scent without being forced to understand or answer the claim.

### S03-B04 — Saku reciprocates the ordinary encounter, not named love

**Class:** FACT + LIMIT

**Confidence:** high

Saku notices Yuzuki's welcome, joins her play, offers coffee, follows her, and retains awareness of her scent `[V03B:p-001#p0018-p0023]`, `[V03B:p-001#p0057-p0061]`. He also forgot a souvenir for her, asks what she means by overwrite, and supplies no reciprocal love language `[V03B:p-001#p0037-p0040]`, `[V03B:p-001#p0052-p0056]`.

The booklet therefore increases evidence for ordinary dyadic intimacy while preserving V02/V03 directional asymmetry. It does not establish a couple or transfer Saku's mutual love language with Asuka to Yuzuki.

### S03-B05 — care, hope, hurt, and self-interest coexist

**Class:** INFERENCE

**Confidence:** medium-high

Yuzuki says she had intended to comfort Saku if Asuka rejected him, but his expression shows relief instead `[V03B:p-001#p0041-p0047]`. The line can hold genuine care, a hoped-for opening, disappointment, and comic self-protection at once. Reducing it either to pure sacrifice or to cynical opportunism loses the scene's mixed motive structure.

The coffee request gives her a small compensatory claim without punishing Saku or attacking Asuka. She can ask for ordinary reciprocity while leaving the larger outcome intact.

### S03-B06 — the dedicated illustration fixes active, ordinary pursuit

**Class:** VISUAL FACT + INFERENCE

**Confidence:** high

The dedicated image shows Yuzuki alone with phone, cap, dark hoodie, white shorts, and bubble gum against glass architecture consistent with the named Happiring setting `[V03B:p-002#img01]`. It directly matches the prose outfit and waiting pose `[V03B:p-001#p0026-p0028]`. The combination is casual and boyish, while framing and color still make her conspicuous beauty visually dominant.

The phone and forward-facing wait matter more than glamour alone: she has actively placed herself in Saku's route while narrating the meeting as coincidence. The image contains no Saku and cannot by itself establish reciprocity.

The booklet cover reuses and reframes the main V03 Asuka/Ramune cover art with a purchase-bonus label `[V03B:p-cover#img01]`. It is paratextual packaging, not evidence that the story's focal girl is Asuka. The booklet's distinct story illustration is the Yuzuki image `[V03B:p-002#img01]`.

## 5. Frozen-main claim audit

| Frozen claim / test | Supplemental result | Current formulation |
|---|---|---|
| `F17` — Saku does not reciprocally name love toward Yuzuki | `PRESERVE` | ordinary warmth and sensory awareness increase; reciprocal naming remains absent |
| `F36` — Yuzuki's love becomes costly, nonpossessive action | `STRENGTHEN / REVISE` | she remains non-sabotaging while also seeking competitive, self-protective, and relationally meaningful reclamation |
| V04-Q05 — does Yuzuki's nonpossessive support persist? | `REVISE BEFORE V04` | test whether she can balance generosity, competition, hurt, and direct self-advocacy without converting any one mode into a compulsory role |

No transition is assigned to `F35`: the booklet presupposes the Asuka trip and jokes about its possible sexual result, but supplies no new evidence that changes the frozen classification of Saku/Asuka mutual love without exclusivity.

## 6. Rival readings and limits

### “Yuzuki has selflessly surrendered Saku to Asuka”

**Rejected.** Her earlier help persists, but the overwrite bid demonstrates continuing desire, competitive feeling, and an effort to recover presence.

### “The overwrite is possessive sabotage”

**Rejected as too strong.** Yuzuki does not undo the trip, disparage Asuka, demand a false report, or punish Saku. She makes a bounded sensory bid and accepts coffee.

### “The scene establishes reciprocal romance”

**Unsupported.** Saku participates warmly but neither understands the stated overwrite nor names love or commitment.

### “It is only a comedy tag with no analytical force”

**Insufficient.** The explicit homecoming response, weakened voice, tactile/sensory trace, and closing attention to scent make the scene a compact relationship-state test.

### “Overwrite has one certain object”

**Unsupported.** Asuka's recent presence is the strongest contextual referent, but the omitted object preserves interpretive latitude. It may include the trip's emotional residue, imagined physical contact, scent, memory, or Yuzuki's fear of displacement.

## 7. Supplemental checkpoint and safe next operation

The separate V03 booklet is fully disposed at this boundary:

- exact object identity and integrity: verified;
- publication relationship: official Volume 03 purchase bonus;
- primary class: `SUPPLEMENTAL_MAINLINE`;
- diegetic placement: late V03 between main `[p-0031#p0508]` and `[p-0031#p0512]`;
- prospective dependency: main V03 must be complete first;
- prose and visual evidence: integrated;
- frozen V03 main artifacts: preserved without retroactive rewriting;
- Volume 04+ evidence: unopened.

The safe horizon is now:

```yaml
H_main: V03
H_supp:
  - V03_IN_EPUB_BIRTHDAY_BONUS__BONUS_FICTION
  - V03_ILLUSTRATION_SS_BOOKLET__SUPPLEMENTAL_MAINLINE
H_next: V04_MAIN
```

The next permitted source operation is verification and prospective reading of the exact locked Japanese Volume 04 main EPUB.
