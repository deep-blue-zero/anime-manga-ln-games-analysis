---
series: IDOLY_PRIDE
artifact_type: source_audit
artifact_role: SOURCE_AUDIT
scope: PHASE1_LOWER_TIER_SPECIALS_CARDS_MESSAGES_ROUTING
generation: V2
version: "1.0"
status: canonical
phase: "1"
source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: "Frozen post-B3 authority; 27 specials/misc bundles / 52 stories; 363 card bundles as enumerated by the Phase-1 ledger and sampled through all 20 playable-character card dialogue corpora; 99 message bundles sampled through all 20 playable-character message corpora plus representative operational/group-chat bundles. B4 bonds remain indexed texture. No new lower-tier proposition is admitted by this routing operation."
inherits: IDOLY_PRIDE_V2_PHASE1_POST_BOND_B3_BASELINE.md
routing_output: IDOLY_PRIDE_V2_PHASE1_LOWER_TIER_CLOSE_READ_QUEUE.md
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
integrity_status: ROUTING_ONLY_NO_CLAIM_ADMISSION
created: "2026-08-16"
updated: "2026-08-16"
next_operation: "Phase 1 Card Close Read — C1-A: family, memory, vocation, and legacy"
recommended_model: "GPT-5.6 Sol"
recommended_reasoning: "Extra High"
---

# IDOLY PRIDE V2 — PHASE 1 LOWER-TIER SAMPLING AND ROUTING AUDIT

## 0. Operation and authority boundary

This operation performs the remaining Phase-1 reconnaissance over **specials/misc → cards → messages** after completion of the mandatory bond close-reading program.

It is a **routing audit**, not a close-read/admission tranche.

Therefore:

- `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B3_BASELINE.md` remains the current lower-tier analytical authority;
- B4 bonds remain indexed texture unless an exact later claim promotes one story;
- observations below explain why a source is routed, but they do **not** enter the canonical proposition set until a later prospective close-read freeze admits them;
- historical/Tier-H prose is not used to make a lower-tier source important merely because V1 discussed it heavily;
- vivid romance comedy, wedding themes, birthday sentiment, fanservice, or dramatic titles are not sufficient for escalation by themselves.

The governing selection question is:

> **Does this source change or materially sharpen a stable model, resolve a live ambiguity, establish unusually useful chronology or relationship evidence, or supply evidence that a planned specialist synthesis would otherwise lack?**

If not, the source remains support or indexed texture.

---

# 1. Corpus sampled

## 1.1 Specials/misc

The ledger enumerates **27 bundles / 52 granular stories**.

Direct reconnaissance used the consolidated `03_specials_misc.dialogue.txt` source layer, then descended to exact Drive bundles where missing assets, parody status, branch status, or unusually consequential content required verification.

The layer mixes several analytically different objects:

- anniversary/live-stage fragments;
- birthday and seasonal ordinary-life material;
- April Fool's comedy/parody;
- cross-unit birthday-trip prologues;
- manager-facing relational thank-you material;
- a deliberately non-mainline bad branch;
- stories whose key content is audiovisual and missing from the text extraction.

Treating the whole layer as one narrative tier would therefore be methodologically wrong.

## 1.2 Cards

The Phase-1 ledger enumerates **363 card bundles**. All 20 playable-character card-dialogue corpora were sampled directly rather than selecting only historically famous cards.

A ledger-format defect was found and corrected in successor ledger v1.27: `card_chs_009_st-card-chs-05-flow-00` contained literal newlines inside its Markdown table title. The underlying source identity and story count were correct; only the table cell formatting was malformed. This explains why a naive line-based table count can produce 362 rather than 363.

Cards proved heterogeneous in analytical value. Most are canonical but **not indispensable** because stronger origins/events already own the mature thesis. A smaller group contains unusually precise family history, memorial practice, vocational transition, relationship definition, or late-state authorship and therefore warrants mandatory close reading.

## 1.3 Messages

The ledger enumerates **99 message bundles / 1,812 granular messages**.

Reconnaissance sampled:

- all 20 playable-character message-group corpora;
- private character-to-manager threads;
- companion messages attached to candidate C1 cards;
- representative operational/group-chat formats including LizNoir work chat, IIIX announcement chat, Tsuki+manager chat, and kana/Kokoro chat.

The layer is strongest for:

- Japanese voice/register;
- private relationship grammar;
- ordinary-life continuity;
- short companion aftermath to cards/events;
- group-specific social rhythm;
- branch-sensitive Makino expression.

It is generally weaker than main story/origin/event/card narrative for major plot or endpoint authority.

---

# 2. Governing lower-tier routing vocabulary

## 2.1 Specials

### `SPECIAL_SUPPORT`

Canonical, useful supporting evidence that may be retrieved for ordinary-life, retrospective, cross-unit, or manager-relational synthesis, but does not currently justify a mandatory standalone close-read tranche.

### `SPECIAL_TEXTURE_INDEXED`

Low-stakes birthday/seasonal/social texture. Preserve for voice, ordinary life, and future claim-specific retrieval.

### `SPECIAL_FORMAL_INDEX_ONLY`

Text is absent or too incomplete because the meaningful payload is audiovisual/formal. Preserve the locator and missing-asset dependency; do not pretend the transcript is the work.

### `SPECIAL_COMEDY_CAVEATED`

April Fool's or comparable parody material. May reveal comic voice or cultural texture but has **interpretive value without ordinary continuity authority**.

### `BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY`

Explicit alternate/bad branch. Authored possibility space, not mainline event history.

## 2.2 Cards

### `C1_MANDATORY`

Mandatory Phase-1 close read. Candidate source materially affects a stable character/relationship/legacy/vocation model or a live open question.

### `C2_SELECTIVE`

Useful support that should be retrieved when its topical synthesis or open question is being written. It does not presently justify blocking Phase-1 closure.

### `C3_INDEXED_TEXTURE`

Canonical card source retained for character voice, ordinary life, situational behavior, visual/formal follow-up, and claim-specific retrieval.

## 2.3 Messages

### `M1_CLAIM_BEARING_COMPANION`

Exact message that materially clarifies a C1 card or live ambiguity. Retrieve during the relevant card tranche **after the card-only prospective freeze**.

### `M2_RELATIONAL_OR_VOICE_SUPPORT`

Useful private-state, relationship, register, or ordinary-life evidence; retrieve selectively for specialist synthesis.

### `M3_INDEXED_TEXTURE`

Default message status. Searchable canonical texture; no mandatory close read.

---

# 3. Specials/misc routing

No specials/misc source currently warrants delaying Phase 1 for its own mandatory close-read tranche. The layer should remain available to later ordinary-life, voice, performance, and comparative synthesis.

| Bundle | Route | Reason |
|---|---|---|
| `specials_001_st-ex-story-part-anniversary-01-23-0624` | `SPECIAL_FORMAL_INDEX_ONLY` | Only a tiny textual remnant; missing `adv-live-anniversary-01-23-0624-01`. |
| `specials_002_st-ex-story-part-anniversary-01-24-0624` | `SPECIAL_SUPPORT` | Unit retrospective/manager-directed gratitude; useful mature relational texture, not romance settlement. |
| `specials_003`–`specials_009` birthday bundles | `SPECIAL_TEXTURE_INDEXED` | Birthday/social voice and ordinary-life texture. |
| `specials_010_st-ex-story-part-special-01-21-1224-half-aniv` | `SPECIAL_FORMAL_INDEX_ONLY` | No meaningful dialogue payload in extracted text. |
| `specials_011_st-ex-story-part-special-01-22-0103-newyear` | `SPECIAL_TEXTURE_INDEXED` | Seasonal ordinary-life material. |
| `specials_012_st-ex-story-part-special-01-22-0401-april` | `SPECIAL_FORMAL_INDEX_ONLY` | Textually empty/incomplete formal payload. |
| `specials_013_st-ex-story-part-special-01-22-0624-aniv` | `SPECIAL_SUPPORT` | Anniversary retrospective; useful supporting continuity. |
| `specials_014_st-ex-story-part-special-01-23-0101-newyear` | `SPECIAL_TEXTURE_INDEXED` | Seasonal texture. |
| `specials_015_st-ex-story-part-special-01-23-0401-april` | `SPECIAL_FORMAL_INDEX_ONLY` | No usable dialogue payload. |
| `specials_016_st-ex-story-part-special-01-24-0103-newyear` | `SPECIAL_TEXTURE_INDEXED` | Seasonal texture. |
| `specials_017_st-ex-story-part-special-01-24-0401-april` | `SPECIAL_COMEDY_CAVEATED` | `魚見プロダクション` parody; missing `adv-live-eve-2404-april-03`; cannot be ordinary continuity authority. |
| `specials_018_st-ex-story-part-special-01-24-0624-aniv` | `SPECIAL_FORMAL_INDEX_ONLY` | Anniversary formal payload with insufficient text. |
| `specials_019_st-ex-story-part-special-01-25-0104-newyear` | `SPECIAL_TEXTURE_INDEXED` | Seasonal texture. |
| `specials_020_st-ex-story-part-special-01-25-0624-aniv` | `SPECIAL_FORMAL_INDEX_ONLY` | Formal anniversary material. |
| `specials_021_st-ex-story-part-special-01-26-0104-newyear` | `SPECIAL_TEXTURE_INDEXED` | Late-state seasonal texture. |
| `specials_022_st-ex-story-part-special-01-26-0401-april` | `SPECIAL_COMEDY_CAVEATED` | `ブリスケ` April parody; comic voice only unless independently corroborated. |
| `specials_023_st-ex-story-part-special-01-26-0624-aniv` | `SPECIAL_FORMAL_INDEX_ONLY` | Formal anniversary payload. |
| `specials_024_st-ex-story-part-special-01-birthday-trip-2024` | `SPECIAL_SUPPORT` | Cross-unit birthday-trip ordinary-life material; useful social mixing/relationship texture. |
| `specials_025_st-shelf-25-0128-001` | `SPECIAL_SUPPORT` | Sunny Peace manager-facing Valentine/thank-you material; relational support without romance settlement. |
| `specials_026_st-shelf-25-0401-001` | `SPECIAL_COMEDY_CAVEATED` | `ボジミプロ` April parody; no ordinary continuity authority. |
| `misc_001_st-love-23-0514-007-bad` | `BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY` | Explicit bad/alternate branch. Authored possibility only; do not flatten its Rei/manager outcome into mainline fact. |

Specials conclusion:

> **Preserve the layer, but do not manufacture a mandatory “S1” tranche.**

The analytically correct action is source-class routing, not exhaustive close reading for symmetry.

---

# 4. Card reconnaissance result

The card layer contains the most important remaining Phase-1 material. Eleven cards cross the escalation threshold.

## 4.1 C1 mandatory cards

### 1. `card_kan_007_st-card-kan-05-fest-02` — 「クソ記事をぶっ潰してやんのよ」

Routing reason:

- unusually direct Kana/father/family/private-public history;
- clarifies the difference between abandonment of co-residence and total disappearance;
- exposes the childhood wish beneath Kana's visibility strategy;
- gives media/privacy and self-authored counter-publicity evidence.

Mandatory question:

> How should Kana's father wound be revised once the source distinguishes absence, intermittent contact, public spectatorship, and Kana's abandoned wish for ordinary family life?

### 2. `card_kan_014_st-card-kan-05-snro-00` — 「はい、kanaと握手！」

Routing reason:

The card independently recalls Kana having met **Kuromi** at the earlier dream amusement park and explicitly links that encounter to a recovered happy childhood memory with her father.

This directly routes the long-standing:

> `OPEN_VERIFY_KANA_CARD_CORROBORATION`

toward resolution.

Critical boundary:

> **If the card close read confirms the memory reference, it corroborates Kana's retained memory of the encounter. It does not automatically grant every supernatural/crossover mechanism ordinary mainline continuity authority.**

### 3. `card_suz_003_st-card-suz-05-anml-00` — 「アメリカ留学」

Routing reason:

- direct family pressure around education and idol work;
- distinguishes earlier stubborn resistance to study abroad from later self-authored commitment to idolhood;
- shows overwork as proof-seeking under conditional parental approval;
- useful precursor for Suzu's mature vocation model.

### 4. `card_kor_005_st-card-kor-05-fest-02` — 「契約取れないで終わる！！」

Routing reason:

- post-US ERFOLG restart;
- fran simultaneously operates as idol and designer/businesswoman;
- actual sales risk, investment dependency, and remembered debt make fashion authorship materially concrete;
- tests whether idol-derived performance/sales competence transfers across industry contexts.

This is stronger than generic “fran likes fashion” texture because it shows the plural vocation under real commercial pressure.

### 5. `card_hrk_009_st-card-hrk-05-link-00` — 「ミュージカルのオーディション」

Routing reason:

- early-career Haruko failed an audition to stand beside Mana in a musical;
- Mana's encouragement creates a remembered promise/horizon;
- late Haruko later auditions for a revival and takes the lead role once played by Mana;
- the source sharply links delayed career development, succession, performance inheritance, and unrealized/counterfactual futures.

This card can materially strengthen Haruko's non-idol performance horizon while **not** answering the economic endpoint of long-term idol viability.

### 6. `card_mhk_011_st-card-mhk-05-pajm-00` — 「容赦なく刈りますから」

Routing reason:

The card directly ties miho's long black hair to praise from her deceased old friend Yō. The mundane care routine therefore becomes bodily memory: not only professional grooming but preservation of a part of herself that Yō taught her to value.

This is narrow, unusually precise memorial evidence and belongs in the mature miho/Yō model.

### 7. `card_mhk_006_st-card-mhk-05-fest-02` — 『Friend Glass』

Routing reason:

- Yō's hospitalization intersects with miho's Taiwan solo-tour duty;
- guilt, absence, and fear of being left alone recur under professional obligation;
- IIIX covering Sundance's signature `Friend Glass` converts private friendship/memory into later public performance.

This should be read with, but not collapsed into, the hair card: one is **memory as bodily maintenance**, the other **memory as re-performance**.

### 8. `card_ngs_007_st-card-ngs-05-fest-02` — 「二人の関係」

Routing reason:

This is mandatory paired evidence for the Nagisa/Kotono question after B3. It explicitly moves Nagisa from “support Kotono from behind” toward wanting her own radiance, uses a separated-and-reunited romantic couple as an analogy, and has Nagisa state that she and Kotono need each other and should become the people who illuminate one another from closest beside.

Boundary:

> Strong Nagisa-side romantic/yuri coding can strengthen again; mutual canonical romance still requires Kotono-side evidence and must not be inferred from analogy alone.

### 9. `card_ktn_007_st-card-ktn-05-fest-02` — 「想いに応えたい」

Routing reason:

Paired Kotono-side late-state evidence after Tsuki becomes BIG4. Kotono's conduct under rain/work pressure, her relief when the group arrives, and her Mana-grave framing test how much mature Kotono identity has become group-reliant without becoming passive.

Boundary:

> This is Kotono-side relational evidence, but it does **not** by itself establish romantic reciprocity toward Nagisa.

### 10. `card_szk_002_st-card-szk-05-angl-00` — 「あの頃の私の名前」

Routing reason:

- Shizuku takes authorship over lyrics/costume/staging;
- reincorporates former shut-in/fan identity and the old handle `ぷにもちどろっぷ` into `drop`;
- makes fan/idol reciprocity part of the performance concept;
- offers a compact capstone for identity integration without erasing the pre-idol self.

### 11. `card_rui_007_st-card-rui-05-fest-04` — 「こ、こ……恋！？」

Routing reason:

- late 2026 source;
- Rui's songwriting becomes self-authored rather than merely assigned labor;
- the card forces her to recognize that the feelings she put into the lyrics are genuine;
- her internal address to Makino strongly raises the Rui-side romantic question.

Boundary:

> The close read must separate Rui-side feeling, what she actually says aloud, what remains internal, and any reciprocal Makino claim. The associated telephone audio is unavailable and may not be invented.

---

# 5. C2 selective card set

The following are useful but do not currently block Phase 1. Retrieve them when their topical home is written or when a C1 result opens a new ambiguity.

| Card | Primary support use |
|---|---|
| `card_ai_002_st-card-ai-05-birt-00` | Ai family ramen-shop responsibility; wanting father to rely on her; family/professional-capital texture. |
| `card_aoi_001_st-card-aoi-05-arab-00` | Aoi US/dance recovery restatement; audience/performance support; stronger origin/event material retains mature authority. |
| `card_chs_006_st-card-chs-05-chsk-00` | Chisa craft/fashion authorship and sister/unit creation support. |
| `card_chs_014_st-card-chs-05-pajm-00` | Chisa role-model/embodiment aspirations; useful private-state support. |
| `card_hrk_001_st-card-hrk-05-adlt-00` | Haruko as training-school teacher; turns long failure into mentorship. Existing event/bond evidence already owns the broad intergenerational thesis. |
| `card_kan_010_st-card-kan-05-link-00` | Kana/Kokoro private support, family/bullying context, sibling analogy. |
| `card_ngs_006_st-card-ngs-05-casl-02` | Nagisa generic romance imagination; lower authority than Kotono-specific C1 evidence. |
| `card_rio_001_st-card-rio-05-birt-00` | Private appetite/food-memory/Aoi care texture. |
| `card_rio_002_st-card-rio-05-birt-01` | Adult Rio, responsibility, alcohol/rest, being cared for. |
| `card_rio_016_st-card-rio-05-past-00` | Rio/Aoi founding-dyad historical texture; stronger origin/event evidence retains thesis ownership. |
| `card_smr_006_st-card-smr-05-fest-04` | Hometown/origin-community reciprocity; event E3 already owns the broader mechanism. |
| `card_yu_008_st-card-yu-05-fest-04` | Creative authority and surprise-song authorship; event E2-A2 already owns distributed creative authority. |

All remaining cards route to `C3_INDEXED_TEXTURE` unless a later exact claim promotes them.

---

# 6. Message-layer routing

## 6.1 Default result

No message bundle as a whole becomes a new governing narrative source. The correct model is **story-level promotion inside a generally indexed layer**.

All 99 message bundles remain searchable. Exact messages may be promoted to M1/M2 without escalating every other message in the same bundle.

This matters because a character message group can contain, side by side:

- major relational aftermath;
- a birthday phone prompt;
- casual food talk;
- joke stamps;
- manager choice branches;
- professional logistics.

Bundle-wide elevation would therefore be too coarse.

## 6.2 M1 claim-bearing companions

### `message-card-kan-05-fest-02`

Companion to Kana's father/media C1 card. Haruko explicitly treats the father meeting as meaningful; Kana insists the matter remain private. Useful for `SELECTIVE_PERSONAL_JURISDICTION` and family/publicity boundary.

### `message-card-kor-05-fest-02`

Companion to fran's dual-vocation/business card. Use to refine post-exhibition brand authorship and how fran verbalizes the brand/self relation.

### `message-card-hrk-05-link-00`

Companion to Haruko's musical succession card. Preserve as aftermath/continuity support after the card-only freeze.

### `message-card-mhk-05-pajm-00` — 「思い出はいつも黒髪に」

Mostly comedic aftermath, but the title/editorial framing is useful corroboration that the black-hair card is memory-coded. It cannot substitute for the card's direct Yō-related evidence.

### `message-card-ngs-05-fest-02`

Companion to `二人の関係`; further Kotono-focused fan attention. Use as Nagisa-side support, not proof of Kotono reciprocity.

### `message-card-ktn-05-fest-02`

Kotono family/manager aftermath. Useful paired late-state context; does not supply Nagisa-romance reciprocity.

### `message-card-rui-05-fest-04` — 「ありのままの恩返し」

Mandatory companion because Rui revisits kiss-related relational understanding and then asks to call Makino.

Formal dependency:

- `Telephone: tel-card-rui-05-fest-04` is referenced;
- telephone audio is unavailable upstream in the sampled corpus;
- no official transcript is present.

Therefore:

> **Do not infer or reconstruct the phone call.**

The card/message text can establish only what exists before that missing call.

## 6.3 M2 examples

- `message-card-ngs-05-idol-00` — 「背中をあずけて」: Nagisa says leaning back-to-back with Kotono calms her, especially around early-debut anxiety; strong intimacy/support texture.
- `message-card-rio-05-casl-02` — 「もしも職場で恋をしたら」: Rio's lack of lived romance/cohabitation experience becomes an explicit blind spot she tries to research.
- `message-card-rio-05-past-00`: private Rio/Aoi hotel/sleepover history and founder-dyad relaxation.
- `message-card-yu-05-casl-02` — 「もしも芸能人と恋をしたら」: strong Yu-side possessive/yuri-coded Rui attachment; not mutual romance settlement.
- `message-card-rio-05-newy-00`: Rio explicitly frames herself as having put all her youth into idolhood; useful for youth/opportunity-cost synthesis.
- `message-card-suz-05-anml-00`: family/留学 aftermath useful beside the Suzu C1 card.
- selected unit/group chats such as `LizNoir業務連絡`, `ⅢX-announce-`, `月スト＆マネおしゃべり`, and `仲良しkana×こころ`: useful for group register, operational authority, banter, and maintenance labor rather than plot supremacy.

## 6.4 Makino branch discipline

Messages frequently include mutually exclusive player response choices.

The governing identity decision remains:

> the game manager is Makino Kouhei.

But selectable replies remain:

> `PLAYER_SELECTED_MAKINO_EXPRESSION`

They define plausible authored Makino responses inside the game's characterization envelope. They must **not** be accumulated as though every option literally occurred.

---

# 7. B4 bonds remain unchanged

No sampled lower-tier source creates a reason to rerank all B4 bonds.

Retain:

- `bond_ai_001_ai`;
- `bond_mei_001_mei`;
- `bond_yu_001_yu`;

as indexed texture.

If a later C1 card produces a precise ambiguity one B4 story can resolve, promote **that exact story**, not the entire bundle by default.

---

# 8. Open-register routing effects

No open item is resolved by this routing audit because sources have not yet passed the mandatory close-read/admission gate.

Routing effects:

- `OPEN_VERIFY_KANA_CARD_CORROBORATION` → **assigned to C1-A** via `card_kan_014_st-card-kan-05-snro-00`; likely resolvable at the narrow retained-memory level, but still open until freeze.
- Nagisa/Kotono reciprocity → **assigned to paired C1-B cards** `card_ngs_007` + `card_ktn_007`; do not treat Nagisa's language as automatic Kotono romantic reciprocity.
- Rui/Makino affect → **new explicit C1-B test** via `card_rui_007` + `message-card-rui-05-fest-04`; telephone gap remains formal/open.
- `OPEN-14` Haruko long-career horizon → `card_hrk_009` can expand the performance/vocational horizon; it does not settle material sustainability or eventual idol retirement.
- miho/Yō memorial practice → paired miho C1 cards route bodily-maintenance and public re-performance evidence without assuming they are the same mechanism.

---

# 9. Routing conclusion

Phase-1 reconnaissance is now sufficiently complete to stop broad sampling and return to selective close reading.

The result is intentionally asymmetric:

- **specials/misc:** no standalone mandatory tranche;
- **cards:** 11 mandatory C1 cards, a bounded C2 support set, remainder C3 indexed;
- **messages:** exact M1/M2 story promotions inside a predominantly M3/indexed layer;
- **B4 bonds:** unchanged indexed texture.

This is preferable to exhaustive equal-weight processing because it preserves the project's authority hierarchy and avoids making a large corpus important merely because it is large.

The next operation is fixed by `IDOLY_PRIDE_V2_PHASE1_LOWER_TIER_CLOSE_READ_QUEUE.md`:

> **Phase 1 Card Close Read — C1-A: family, memory, vocation, and legacy**

Use the established prospective gate:

> raw cards → card-only prospective freeze → exact primary companion messages → Tier-H comparison if useful → close-read audit → successor baseline → ledger → SHA manifest.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High
