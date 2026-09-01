---
title: "AoButa Phase 8 — Final Japanese Verification Report"
series: "青春ブタ野郎シリーズ / Rascal Does Not Dream"
artifact_type: "phase8_final_japanese_verification_report"
version: "1.0"
date: "2026-08-12"
status: "phase8_complete_phase9_not_locked"
source_boundary: "Volumes 1-15 + Animal Land + Spring Days"
primary_source_language: "Japanese"
source_epubs_redistributed: false
phase9_immutable_lock_performed: false
related_documents:
  - "00_README_AND_CORPUS_MAP.md"
  - "15_JAPANESE_NARRATION_CHARACTER_VOICE_HUMOR_TITLES_AND_DIALOGUE.md"
  - "21_JAPANESE_TERMINOLOGY_DIALOGUE_AND_PASSAGE_INDEX.md"
  - "PHASE8_CORRECTIONS_AND_NORMALIZATIONS.md"
  - "PHASE8_WORKING_STATE.md"
---

# Phase 8 — Final Japanese Verification Report

## 1. Purpose and governing boundary

Phase 8 is the **source-language verification layer** of the definitive AoButa synthesis. Its purpose is not to reopen the literary argument or to perform another volume-by-volume interpretation. It tests whether the mature synthesis is actually supported by the Japanese wording, speakers, source locations, chronology, and epistemic status assigned to the relevant passages.

The audit therefore rechecked the architecture-defined targets:

1. direct Japanese quotations;
2. translation-sensitive terminology;
3. speaker and narrator attribution;
4. world-state claims;
5. Adolescence Syndrome mechanics;
6. forms of address;
7. bonus-novel chronology and provenance.

Phase 8 also reverified the source-routing infrastructure used to reach the original Japanese EPUBs. It deliberately **does not** create the immutable corpus manifest, final artifact checksum set, final corpus index, or final delivery ZIP. Those are Phase 9 operations. The Phase-8 directory must therefore be understood as a **Japanese-verified but still mutable working corpus**.

## 2. Executive result

The audit found **no source-language problem that overturns the mature full-series thesis**.

The principal interpretation remains supported:

> Growing up does not require Sakuta to declare his adolescent supernatural experiences unreal. The finale instead changes their mode of presence: they can become memory, ethical knowledge, and a disposition to believe another person without requiring shared perception.

The final recognition inversion also survives exact-language review:

- Volume 1 establishes Sakuta as the person willing to reject the ambient `空気` and recognize Mai when the social world does not.
- Volume 15 culminates in `僕には見えない。でも、君を信じるよ`, separating **shared perception** from **epistemic trust**.

Likewise, the final adulthood formulation is exact and remains central:

> `僕は思春期症候群を思い出に変えるだけだ`

The audit strengthened several important distinctions rather than weakening them. Most significantly, Volume 14 requires a sharper distinction between **`認識`** and **`観測`**: Rio's Chapter 4 explanatory model uses recognition-language when describing dreamed possibilities becoming conditions of actuality, whereas the explicit observation-language `僕には霧島透子を観測できなかった` belongs to counterpart Sakuta's earlier written message. Neither statement becomes narrator-certified physics merely because it uses quasi-scientific language.

## 3. Final verification counts

| Audit layer | Result |
|---|---:|
| Controlled Document-21 entries | **90/90 verified** |
| Individual Japanese phrases in those entries | **92/92 verified against source and stated XHTML** |
| Controlled V1–V7 backfill rows | **120/120 verified** |
| Individual phrases in V1–V7 backfills | **148 verified anchors** |
| Native V8–V15 + bonus locator rows carrying Japanese anchors | **170/170 verified** |
| Japanese phrases in those native locator rows | **440/440 verified** |
| Visual-text locator rows | **3 manually verified** |
| Direct Japanese blockquote items in the active analytical layer | **374 audited** |
| Exact direct-source blockquote matches | **372** |
| Intentionally lexical/schematic blockquote items | **2** |
| Unmatched direct-quotation candidates | **0** |
| Translation-sensitive lexical targets | **18/18 verified** |
| Representative forms-of-address claims | **11/11 verified** |
| Speaker/narrator attributions in the controlled Japanese index | **90/90 verified** |
| Speaker-attribution precision corrections | **6** |
| Controlled working translations reviewed | **90/90** |
| Material mistranslations remaining | **0** |
| Translation-gloss consistency edits | **1** |
| Controlled world-state claims | **11/11 verified** |
| Controlled Adolescence Syndrome cases | **17/17 verified** |
| Controlled bonus story-position chronology claims | **3/3 verified** |
| Thesis reversals caused by Phase 8 | **0** |

These counts describe different audit layers and should not be arithmetically combined into one inflated “quotation total.” They overlap by design: Document 21 is a controlled high-value index, early volumes use targeted backfill, and native-v2 volumes already contain their own evidence/locator ledgers.

## 4. Direct quotation and exact-language audit

The active retrospective analytical layer contains **374 Japanese blockquote code-span items** subject to the direct-quotation audit. Of these:

- **372** were exact source matches;
- **2** were intentionally lexical or schematic rather than attempts at verbatim sentence quotation;
- **0** remained unmatched.

This audit was supplemented by the locator-ledger verification of the canonical sequential artifacts. Native-v2 Volumes 8–15 and both bonuses yielded **170 locator rows carrying Japanese anchors**, all of which verified after the Phase-8 corrections. The migrated Volumes 1–7 were handled through the provenance-backfill architecture rather than having their historical essays silently rewritten.

Three native locator rows are visual text rather than reflowable XHTML prose. Those were manually checked against the image payload:

- Volume 8 front-matter text associated with `kuchie-003-005.jpg`;
- Volume 8 front-matter text associated with `kuchie-006-008.jpg`;
- Volume 9's front-matter `謎の少女` descriptor associated with `kuchie-003-005.jpg`.

The correction principle was conservative:

> **repair wording and provenance; preserve the historical interpretation.**

A repaired quotation does not retroactively give an early volume knowledge that only a later volume supplies.

## 5. Translation-sensitive terminology

Eighteen controlled lexical targets were rechecked at source level. The final corpus preserves several distinctions that should not be flattened in later scholarship.

### `空気`

`空気を読む` is the ordinary social idiom “read the atmosphere/room,” but AoButa uses it longitudinally. Sakuta's early rejection of ambient social jurisdiction and his later instruction to Uzuki do not produce a simple “social awareness bad/good” reversal. The mature distinction is between:

- unaccountable anonymous consensus;
- and concrete attention to the people and commitments actually present.

### `認識` and `観測`

These are related but not interchangeable.

- `認識` covers recognition/cognition/apprehension and is central to social identity and rewritten awareness.
- `観測` is more explicitly observational and appears inside the series' quasi-scientific character models.

The final synthesis may compare them, but it must not claim that Rio and counterpart Sakuta use the same technical term at the same argumentative moment.

### `同一性`

In the relevant clinical context, `同一性` is best handled as **identity/continuity**. It should not be transformed into an unsupported metaphysical claim about a soul-substance.

### `思い出に変える`

The phrase is not equivalent to “admit it was imaginary,” “forget it,” or “grow out of delusion.” The grammatical and narrative action is reclassification: an experience that had immediate jurisdiction over the present becomes something remembered that can still shape the future.

### `同じ景色`

The final Sakuta/Mai formulation is relational rather than fusional. They want to inhabit the same scenery/world while remaining distinct subjects.

### `＃夢見る` / `#夢見る`

The Japanese prose normally uses the **full-width hash** `＃夢見る`. The analytical corpus frequently normalizes this to ASCII `#夢見る` for searchability. Phase 8 explicitly records this as an **orthographic normalization only**. No semantic distinction is inferred.

## 6. Speaker and narrator attribution

All **90 controlled Japanese-index entries** were reread in surrounding source context. Six labels required precision corrections:

1. **JP-001** — Sakuta's `もう、空気なんて読んでやるか` is spoken aloud, not internal narration.
2. **JP-019** — the sentence is focalized narration immediately after Sakuta addresses the red-randoseru girl, not a spoken line to her.
3. **JP-025** — Sakuta's line is specifically addressed to Shoko during the service-area conversation about the Toko/Miori diary.
4. **JP-046** — the forgetting sentence is focalized narration, not Sakuta dialogue.
5. **JP-049** — the *Animal Land* wording is Sakuta speaking to Mai, not narration.
6. **JP-090** — the source explicitly marks the line as `独り言`; it is spoken aloud to himself rather than purely internal narration.

These corrections matter because AoButa often places Sakuta's voice very close to narration. Treating focalized prose as dialogue, or dialogue as interiority, can change what the text says about social performance, disclosure, and self-consciousness.

## 7. Forms of address

The controlled address matrix was rechecked in representative source contexts:

| Direction | Verified form |
|---|---|
| Mai → Sakuta | `咲太` |
| Sakuta → Mai | `麻衣さん` |
| current Shoko → Sakuta | `咲太さん` |
| Sara → Sakuta | `咲太せんせ` |
| Sakuta → Rio | `双葉` |
| Sakuta → Tomoe | `古賀` |
| Sakuta → Uzuki | `づっきー` |
| Sakuta → Miori | `美東` |
| Miori → Sakuta | `梓川君` |
| Kaede → Sakuta | `お兄ちゃん` |
| Hanakaede → Sakuta | `お兄ちゃん` |

One caution is now explicit: `梓川君` is a verified Miori form of address, but it is not exclusive to Miori; Ikumi also uses it. It therefore cannot function as a unique speaker identifier without context.

## 8. World-state verification

All **11 controlled world-state entries** were rechecked against their source anchors and retained at their appropriate epistemic levels.

The Phase-8 audit does **not** collapse the different temporal/world phenomena into one “timeline” model. The final notation remains useful precisely because the series presents mechanically different structures:

- Tomoe's recursive/prospective state;
- Shoko future states;
- the Volume-7 revision;
- the Volume-9 adjacent possibility;
- W1/counterpart access;
- Miori's serially remembered variants;
- R0;
- R1;
- RF.

The strongest final in-world model still comes from counterpart Sakuta: Miori is treated as unusually singular across possibilities, while current Sakuta's observation has unusual world-selecting significance. Phase 8 confirms the wording but **does not promote this model from CB/SI to omniscient TF**.

R1 remains best described as a **synthetic/composite rewritten state** at SI level rather than confidently identified as one simple pre-existing branch. RF remains a useful name for the final stabilized adult history; calling it ethically preferable is an interpretation, not an objective cosmological ranking certified by the narrator.

## 9. Adolescence Syndrome mechanics

All **17 controlled phenomenon cases** remain source-grounded.

The audit reinforces the Phase-3 conclusion that the phenomena are **literally real within the fiction but mechanically heterogeneous**. It found no textual basis for reducing the whole series to one hard-magic equation.

The corpus therefore continues to distinguish:

- observed event;
- character explanation;
- strong inference;
- thematic interpretation;
- unresolved mechanics.

Important cautions retained after verification include:

- Rio's quantum vocabulary is character-theory language.
- Shoko's explanatory models remain character models where the narrator does not independently certify them.
- Toko “gift” formulations remain character belief where appropriate.
- Counterpart Sakuta supplies the strongest final observer model, not an omniscient textbook.
- The smartphone clue remains unfinished.
- The red-randoseru girl remains ontologically unresolved.
- The final Ebina ghost remains unresolved.

## 10. Bonus chronology and publication position

The bonus chronology audit verified the supplied EPUB colophons and the story-position anchors used by the synthesis.

### *Animal Land*

- electronic colophon: **2023-08-12**;
- version: `ver.001`;
- SHA-256 retained in the source inventory;
- story-position anchor: `春休みの最終日`.

### *Spring Days*

- electronic colophon: **2024-02-03**;
- version: `ver.001`;
- story anchors place the narrative across late April/early May of Sakuta's third high-school year, including May 6 and May 9 and the Golden Week employment period.

The project reading order remains:

> **V9 → Animal Land → Spring Days → V10**

This is an **analytical story-position order**, not a claim about historical publication order.

The supplied EPUBs establish their recorded electronic/publication dates. They do **not** independently establish the exact first physical theatrical handout date, so Phase 8 does not invent one.

## 11. Corrections and their interpretive significance

The source/locator correction registry contains **39 exact-language, locator, visual-text, or provenance corrections**. Six additional changes refine speaker attribution, and one working-translation gloss was normalized for consistency.

Most repairs are small—punctuation, full source anchors instead of ellipsis shorthand, paragraph positions, or exact spelling. Several are analytically important:

### Volume 7 locator repair

The `牧之原さん！` evidence route was moved from an incorrect spine/XHTML position to the actual source location. This changes provenance, not the interpretation that recognition precedes full explanatory recollection.

### Volume 13 locator repair

The Nene/Toko/trophy/Takumi-memory evidence block was relocated to the correct XHTML. Again, the analytical conclusion survives; its source route is now correct.

### Volume 14 song line

The epigraph is `君に出会えてよかった`, not a shortened paraphrase. That exact wording matters because Volume 15 completes the song's grief architecture by holding `君に出会わなければよかった` and `君に出会えてよかった` together rather than replacing one with the other.

### Volume 14 `認識` versus `観測`

This is the most conceptually important precision correction. Rio's later explanation uses `認識`; counterpart Sakuta's message uses `観測`. The synthesis may analyze their relationship but should no longer blur their immediate speakers or lexical functions.

### Volume 15 paratext

The Yokotani and Masui farewell material now has explicit page routing rather than a page range that obscures the middle item. It remains paratext/reception evidence, not omniscient canon explanation.

The complete exact correction registry is preserved in:

> `support/PHASE8_APPLIED_CORRECTIONS.json`

and summarized in:

> `PHASE8_CORRECTIONS_AND_NORMALIZATIONS.md`

## 12. What Phase 8 did not change

Phase 8 found no reason to reverse the core full-series propositions:

1. **Recognition exceeds perception.**
2. **Personhood cannot be reduced to body, memory, name, role, or social recognition alone.**
3. **Possible lives can possess moral significance without gaining automatic jurisdiction over the present.**
4. **Continuing bonds become sustainable when remembrance does not require substitution.**
5. **The final history favors authored futures over magically preserved optimal outcomes.**
6. **Adulthood is memory reclassification rather than supernatural denial.**
7. **The series supplies stronger ethical closure than cosmological closure.**

It also found no source basis for “solving” the remaining metaphysical ambiguities. Those remain deliberately preserved.

## 13. Phase-8 evidence artifacts

The machine-readable and review artifacts are in `support/`:

- `PHASE8_FINAL_VERIFICATION_SUMMARY.json`
- `PHASE8_JP_INDEX_VERIFICATION.json`
- `PHASE8_SOURCE_ANCHOR_QC.json`
- `PHASE8_BLOCKQUOTE_QUOTATION_AUDIT.json`
- `PHASE8_TRANSLATION_SENSITIVE_TERMS_QC.json`
- `PHASE8_SPEAKER_ATTRIBUTION_QC.json`
- `PHASE8_SPEAKER_ATTRIBUTION_QC.md`
- `PHASE8_WORKING_TRANSLATION_QC.json`
- `PHASE8_WORKING_TRANSLATION_QC.md`
- `PHASE8_FORM_OF_ADDRESS_QC.json`
- `PHASE8_FORM_OF_ADDRESS_REVIEW.md`
- `PHASE8_WORLD_STATE_MECHANICS_QC.json`
- `PHASE8_BONUS_CHRONOLOGY_QC.json`
- `PHASE8_APPLIED_CORRECTIONS.json`

These are verification records, not substitutes for the primary sources.

## 14. Phase-9 boundary

Phase 8 is now complete.

The corpus is **source-language verified but not yet immutable**. Phase 9 should perform the final archival operations:

1. editorial cleanup of administrative/historical artifacts;
2. final manifest regeneration;
3. final corpus-index regeneration;
4. final link and duplication audit;
5. UTF-8 and front-matter validation;
6. final source and artifact checksum generation;
7. final delivery audit;
8. immutable archive creation and external archive checksum.

No Phase-8 hash should be treated as the final archival lock simply because a file happened to retain a valid earlier content hash.
