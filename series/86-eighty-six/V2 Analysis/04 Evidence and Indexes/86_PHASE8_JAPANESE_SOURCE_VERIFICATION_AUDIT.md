---
series: 86-Eighty-Six
series_id: '86'
artifact_type: japanese_source_verification_audit
artifact_role: AUDIT
document_id: PHASE8
title: Phase 8 Japanese Source Verification Audit
scope: V01-V14+ALTER1
phase: 8
generation: V2
method_version: V2
status: canonical
date: '2026-08-16'
source_boundary: Locked original-Japanese Volumes 1-14; Alter.1 audited supplemental; Alter.2 excluded from mainline evidence
governing_method: 86_FULL_SERIES_ANALYTICAL_METHOD_V2.md
governing_architecture: 86_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md
source_inventory: 86_SOURCE_INVENTORY.md
locator_authority: 86_PHASE5_LOCKED_LOCATOR_INDEX.tsv
locator_correction_authority: 86_PHASE5_LOCATOR_CORRECTION_LEDGER.tsv
phase5_language_lock: 86_PHASE5_JAPANESE_CLAIM_AND_TERMINOLOGY_LOCK.tsv
primary_language_synthesis: 12_JAPANESE_VOICE_NARRATION_TERMINOLOGY_AND_TRANSLATION_SENSITIVE_FINDINGS.md
primary_language_index: 16_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md
phase7_audit: 86_PHASE7_CONTRADICTION_AND_ADVERSARIAL_AUDIT.md
phase7_audit_sha256: 20e2782310151862b5303ffb01b40a2eb1a60dddef8b7604cbe1a2a1c3eb9909
audit_target: 18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md
audit_target_sha256: 9f19fd985aaf292890adc1dffc31bf6253c970aa1dd0cb0eef8f3a379efb6704
audit_target_status: active_provisional
phase8_result: PASS_WITH_CORRECTIONS_APPLIED
source_integrity_verdict: 15/15 exact SHA-256 match and ZIP CRC PASS
locator_verdict: 1045/1045 current-source routes verified
exact_source_verified_locator_rows: 1023
paraphrase_coordinate_context_verified_rows: 21
exact_coordinate_only_verified_rows: 1
phase5_terminology_locks_verified: 28/28
document16_high_value_controls_verified: 55/55
document12_inline_japanese_spans_attested: 170/170 after one reference correction
document18_inline_japanese_spans_attested: 38/38
phase7_inline_japanese_spans_attested: 23/23
document12_corrections_applied: 1
document16_corrections_applied: 2
load_bearing_interpretations_overturned: 0
phase7_mandatory_revisions_confirmed: 9
canonical_capstone_promotion_authorized: false
next_action: Merge P7-R01 through P7-R09 into Document 18, revalidate against this audit and the Phase-5 locks, then explicitly promote Document 18 to canonical if clean
adversarial_constraints_preserved:
- T14-C01
- T14-C02
- T14-C03
- T14-C04
- T14-C05
- T14-C06
- T14-C07
- T14-C08
- T14-C09
- T14-C10
- T14-C11
- T14-C12
- T14-C13
- T14-C14
- T14-C15
- T14-C16
- T14-C17
- T14-C18
- T14-C19
- T14-C20
- T14-C21
- T14-C22
- T14-C23
- T14-C24
- T14-C25
- T14-C26
- T14-C27
- T14-C28
- T14-C29
- T14-C30
- T14-C31
- T14-C32
- T14-C33
- T14-C34
- T14-C35
- T14-C36
- T14-C37
- T14-C38
- T14-C39
- T14-C40
- T14-C41
open_questions_preserved:
- T14-OQ-01
- T14-OQ-02
- T14-OQ-03
- T14-OQ-04
- T14-OQ-05
- T14-OQ-06
- T14-OQ-07
- T14-OQ-08
- T14-OQ-09
- T14-OQ-10
- T14-OQ-11
- T14-OQ-12
- T14-OQ-13
- T14-OQ-14
- T14-OQ-15
- T14-OQ-16
- T14-OQ-17
- T14-OQ-18
- T14-OQ-19
- T14-OQ-20
- T14-OQ-21
- T14-OQ-22
- T14-OQ-23
- T14-OQ-24
- T14-OQ-25
- T14-OQ-26
- T14-OQ-27
- T14-OQ-28
- T14-OQ-29
- T14-OQ-30
- T14-OQ-31
- T14-OQ-32
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# 86 Phase 8 — Japanese Source Verification Audit

## Scope and authority note

This document is the canonical Phase-8 source-language verification layer for the V2 corpus through Japanese Volume 14. Its task is narrower than literary synthesis and stricter than ordinary quotation checking. It asks whether the Japanese-language claims on which the mature interpretation depends still survive direct comparison with the **current locked EPUB binaries**, their actual XHTML paragraph structure, and the source contexts surrounding the compact anchors preserved in Phase 5 and Document 16.

The audit was performed because the provisional capstone, `18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md`, has already passed a conceptual red-team review but remains `active_provisional`. Phase 7 found no fatal contradiction and froze nine mandatory revisions. Those revisions must not be merged until the Japanese evidence underneath them is independently checked. Phase 8 therefore treats the following hierarchy as controlling:

> **current locked Japanese binary → exact XHTML paragraph → Phase-5 locked locator/correction layer → Document 16 retrieval entry → Document 12 linguistic interpretation → specialist synthesis → provisional Document 18.**

The result is:

> **PASS WITH CORRECTIONS APPLIED.**

All fifteen admissible Japanese source binaries currently used by the V2 release match their locked SHA-256 identities and pass ZIP/CRC integrity testing. All 1,045 Phase-5 locator routes were rechecked against the current source files. All 28 Phase-5 terminology locks and all 55 Document-16 high-value language controls remain supported. Every Japanese inline-code span used in the current versions of Document 12, provisional Document 18, and canonical Phase 7 is source-attested after one reference-layer correction to Document 12. No load-bearing V2 literary, political, relational, military, or personhood interpretation is overturned.

Two important limits follow.

First, **source verification is not a license to collapse distinct Japanese systems into one English abstraction**. Exact wording can confirm that a passage exists while still leaving its best literary interpretation open. Second, this audit does **not** promote Document 18. It confirms the evidence on which the Phase-7 revision queue depends. The next operation is to merge P7-R01 through P7-R09 into a new capstone candidate, revalidate it, and only then decide whether `active_provisional` may become `canonical`.

---

# I. Executive verification verdict

Phase 8 establishes five high-confidence results.

### 1. The locked source boundary is materially intact

The Japanese EPUBs V01–V14 and Alter.1 were re-mounted from the canonical Drive primary-source hierarchy rather than reused from an unverified temporary cache. Every binary matches the SHA-256 recorded by the Phase-0/Phase-5 source lock. Every archive passes CRC testing. The accepted Japanese replacement Volume 14 is the governing V14 source; the earlier Chinese-dominant file remains rejection-history provenance only.

### 2. The Phase-5 locator layer remains current

The audit re-parsed the source EPUB XHTML and tested all 1,045 locked retrieval routes. The result is not merely “the files contain similar text.” It is a current-source coordinate check.

- **1,023** rows are quotation/anchor-grade source-exact after accounting for two intentionally compound two-coordinate locks.
- **21** rows are paraphrase routes whose coordinates and surrounding context verify but whose paraphrases remain paraphrases; Phase 8 does not silently upgrade them into direct quotations.
- **1** row is an exact coordinate-only provenance control tied to an English title reference rather than Japanese quotation text.

Thus **1,045/1,045 routes remain usable at their declared evidence state**.

### 3. The mature lexical distinctions survive direct source inspection

The governing distinctions among return, home, pride, support, obedience, trust, personality, selfhood, will, justice, forgiveness, title/address, and temporal modality are present in the Japanese as claimed. Several of these distinctions become stronger once the full paragraph is restored. None becomes weaker enough to require a specialist reinterpretation.

### 4. The Japanese evidence supports Phase 7 rather than dissolving it

P7-R01 through P7-R09 remain mandatory. In particular, the Japanese confirms why the capstone must stop treating “return” as one doctrine: `帰る`, `戻る`, `還る`, `帰還`, and `生還` occupy different relational, restorative, deathward, and operational fields. Likewise, the source confirms that V2 master terms such as **exhaustive foreclosure**, **living continuity**, **interruptible interdependence**, and **recoverability** are analytical glosses, not lexical discoveries hidden in the Japanese.

### 5. The defects found are archival/reference defects, not interpretive collapse

One Document-12 term had been written in a form that looked source-derived although the exact compound does not occur in the locked corpus: **兵科転換**. The source at V09 instead says `兵科が変わる`—“if the service branch changes.” That wording has been corrected. Document 16 also contained two malformed compact-anchor presentations; their stable IDs and locked coordinates were correct, so the displays were repaired without changing the underlying interpretation.

No direct Japanese quotation carrying a load-bearing Document-18 conclusion failed verification.

---

# II. Primary-source provenance and binary identity

The canonical primary-source route is the source Drive root → `86 - Eighty-Six` → `Japanese EPUBs`. Phase 8 directly re-fetched the current binaries from that hierarchy. The audit therefore does not rely on file names alone.

| Source | Phase-8 SHA-256 | Locked identity | ZIP/CRC | XHTML documents |
|---|---|---|---:|---:|
| V01 | `09f9ef31033945e54b11886197709de84748ef6ef4691b2d4e98cd5eecf10cd8` | MATCH | PASS | 36 |
| V02 | `aa78286d5036091efeda8c6e809cbecae7fcadb3e87dc93c194552c5b10324f1` | MATCH | PASS | 25 |
| V03 | `8d7708267ac15d1eb7eac1ebe08db4199d4d29fd495601c810be55ab38cb7446` | MATCH | PASS | 29 |
| V04 | `b01ea7cd93a09a7ac7457bbe65eb94dde911fbd28e63470d90f5065351981e1b` | MATCH | PASS | 27 |
| V05 | `6f415a58489855503e3ad6fa5dbedfdbafceec9d87b95a62a3a8433a5c860adf` | MATCH | PASS | 24 |
| V06 | `58b18e7e1205901499b5a25dc78bcb46257c85f829a25e4d46155b4a127b4fc7` | MATCH | PASS | 23 |
| V07 | `cbf40552883ad820eaf76485620c9dbdbd6e295343d25c01fb5e7d5f6ee2a7b1` | MATCH | PASS | 24 |
| V08 | `c3de5072add0336e680cb665947cfa683629e304502ab09e002e26433214bfef` | MATCH | PASS | 27 |
| V09 | `980e1fdb37bd3096b83909d452433a1c17035444e08b0db22f80219e207c42fc` | MATCH | PASS | 28 |
| V10 | `38038c0fb4495eb455bebaa86e5c5ee91f8f3b5a290c0e145571d194268cea86` | MATCH | PASS | 48 |
| V11 | `e79f5af1d3af6ab2da74e5abb52202df93024ffc87a9cf1406f0e0aabfb04e79` | MATCH | PASS | 47 |
| V12 | `5324b68ffb6a9be25bda7233edb0f1f66f1599580c5b62064aea7d7b08a5b9cd` | MATCH | PASS | 24 |
| V13 | `e9e02b6bdabaf0b48478ecaf7354ebd2e7551ef3b247713002473f2b53f0b66e` | MATCH | PASS | 25 |
| V14 | `0530e6d0ad217fe1b74f6802be32b842a0facc81e5418cd0e8826a510fa54aaa` | MATCH | PASS | 24 |
| Alter.1 | `226f1909fd53a39b8e30ff286ae1f914b505fe205d112efb4c24c7f9322a7150` | MATCH | PASS | 71 |

The binary result is **15/15 exact identity matches**. Phase 8 therefore verifies language against the same source objects on which the analytical corpus was locked, not replacements that merely share titles.

Alter.2 is not included. Its author-written counterfactual/AU status remains unchanged.

---

# III. XHTML extraction, ruby handling, and paragraph-number method

Phase 8 rebuilt the source text from EPUB XHTML rather than searching a flattened text dump. This matters because the Phase-5 locator system is path-and-paragraph based.

For each XHTML document, the audit:

1. parses the document as XML/XHTML;
2. enumerates non-empty paragraph elements in document order;
3. preserves the base text used by the reader;
4. separately retains a ruby-inclusive representation when older evidence captured reading text interleaved with base characters;
5. normalizes presentation-only punctuation variation for matching without rewriting source wording;
6. treats ellipsis inside compact anchors as an intentional gap rather than requiring a literal single Unicode form;
7. verifies compound locator routes at every named coordinate rather than stopping at the first coordinate.

This last rule explains the only two apparent failures in the first automated pass. `V07-L044` and `V09-L061` each contain two coordinates joined by `+`. A first-pass parser tested only the first paragraph and therefore reported the second clause as absent. Rechecking both coordinates resolves both rows exactly:

- `V07-L044`: the dance first converges toward shared tempo at one paragraph, then later records separate heartbeats at the second coordinate.
- `V09-L061`: Kurena’s past-tense confession and her later continuing-love statement occur at separate coordinates.

The correct result is not a locator correction but **compound-route verification**.

---

# IV. Complete Phase-5 locator re-verification

The Phase-5 lock contains 1,045 canonical routes. Phase 8 preserves their declared epistemic state rather than treating all routes as quotation-equivalent.

| Route class | Count | Phase-8 treatment |
|---|---:|---|
| Source-exact quotation/anchor | **1,023** | Exact wording verified against current source; includes two compound routes after second-coordinate recheck. |
| Paraphrase coordinate/context | **21** | Coordinate and surrounding source context verified; paraphrase status retained. |
| Exact coordinate-only provenance | **1** | Source coordinate verified; not promoted into Japanese quotation evidence. |
| **Total** | **1,045** | **1,045/1,045 PASS at declared state.** |

This distinction is methodologically important. A corpus becomes less reliable, not more, if a verification pass transforms every accurate paraphrase into a fabricated direct quote. Phase 8 therefore certifies routing and evidence state separately.

No new paragraph-scope relock is required. The Phase-5 locator and correction ledgers remain the current coordinate authority.

---

# V. The Japanese terminology lock: 28/28 current-source exact

All 28 rows in `86_PHASE5_JAPANESE_CLAIM_AND_TERMINOLOGY_LOCK.tsv` were checked against the current EPUB text. All remain source-exact.

The point of this lock is not to manufacture rigid dictionary equivalence. It preserves distinctions that later English synthesis must not erase. The following sections state the Phase-8 result for each high-value system.

---

# VI. Return is a family of systems, not one doctrine

The source strongly confirms the Phase-7 concern behind P7-R01, P7-R04, and P7-R05.

## 6.1 `帰る`

`帰る` repeatedly carries destination-, home-, or recipient-oriented force. Representative locked passages include the command `必ず帰れ` in V03 and Shin’s `帰らないと` in V08. In V06, the relational structure is especially explicit: a place or person who waits is part of what makes returning meaningful.

This vocabulary supports Document 10’s **return-address** argument. It does not make every military extraction, bodily recovery, or constitutional repair a literal instance of the same lexical act.

## 6.2 `戻る`

`戻る` marks re-entry, movement back to a prior condition, recovery, or restoration. Its normative value depends on what one is returning to.

V14’s `戻ってこられる` is especially important. The `-られる` potential construction makes Shin’s statement about others **capability or possibility**, not guarantee. Phase 8 therefore confirms that the capstone must not convert this sentence into a prophecy of political redemption.

The wider corpus supplies negative controls: movement “back” can also be regression or reactionary restoration. Return to an earlier condition is not automatically ethically positive.

## 6.3 `還る`

Direct current-source search makes the distinction especially clear. In the relevant narrative contexts, `還る` repeatedly appears with the dead, the bottom/depth of the world, or interrupted deathward movement. It belongs to the Legion/death continuum much more strongly than to Shin/Lena homecoming.

Representative contexts include dead persons who should have returned but were trapped and the recurring notion of the dead returning to the world’s depths.

Accordingly:

> **`還る` must not be used as proof that deathward release, romantic homecoming, civic restoration, and operational extraction are one metaphysical “return” structure.**

They can be compared after their properties have been named. They are not one Japanese master term.

## 6.4 `帰還` and `生還`

These forms protect the military distinction.

V13’s `帰還だけは、許可できません` concerns operational return to base being denied. V08’s use of `生還` concerns returning alive. These are crucial to Document 07’s military analysis because a humane force’s expected completion condition includes survival and extraction. They do not become identical to `帰る` as relational homecoming merely because English can render both as “return.”

### Phase-8 disposition

**P7-R01, P7-R04, and P7-R05 are CONFIRMED.** Document 18 should replace its unified return language with property-first distinctions.

---

# VII. Home and homeland: `故郷` and `祖国`

The source continues to resist a chosen-home versus inherited-home binary.

`故郷` can orient toward lived place, origin, or remembered home. `祖国` carries political or national-homeland weight. Neither should silently absorb citizenship, household, romantic destination, memorial site, or military base.

The mature corpus is therefore correct to allow multiple kinds of belonging to coexist. A character may reject one polity, retain memory of a birthplace, acquire citizenship elsewhere, build a household, and orient emotionally toward particular people without one of those meanings invalidating all others.

Phase 8 finds no Japanese basis for restoring the V1 simplification that “chosen home” is the singular healthy endpoint.

---

# VIII. Togetherness: `一緒` and `共`

V09 provides one of the strongest controls because Lena’s future-oriented desire moves among both ordinary togetherness and more elevated/shared language. The surrounding passage enumerates actual future experiences—seas, seasons, landscapes, flowers, emotional sharing—rather than an abstract doctrine of fusion.

The source supports three limits:

1. `一緒` and `共` overlap; they are not a rigid lexical opposition.
2. “Together” does not erase unequal risk or institutional asymmetry.
3. Desire to remain together can be intense and lifelong without proving that the two people are one subject or that all other relationships become secondary.

This remains consistent with the Phase-7 defense of **interruptible interdependence** as an analytical gloss rather than a Japanese keyword.

---

# IX. Pride: the crucial force of `しか` and `もう`

V08 contains the sentence that most directly disciplines the pride thesis:

`誇りしかないとはもう言わない`

The load-bearing elements are not merely the noun `誇り`.

- `しか` restricts the field: pride as the only available ground.
- `もう` marks a changed present relation to that earlier exclusivity.

The full context strengthens the conclusion because Shin immediately rejects two earlier claims simultaneously: that pride is all they have and that the battlefield is their only place. He then continues to choose combat for reasons that include destination and self-respect.

The correct interpretation is therefore not “pride was a trauma symptom and is cured.” It is:

> **Pride remains legitimate; pride-only selfhood loses exclusive jurisdiction.**

Phase 8 finds the V2 correction textually secure.

---

# X. Support, obedience, trust, reliance, and demand

V12 gives the clearest compact contrast:

`従うのではなく支えてくれた。求めるのではなく信じてくれた`

The sentence explicitly differentiates obedience from support and demand from trust. The surrounding address to `女王陛下` then states that the title expresses respect and trust without becoming worship or compulsion.

This confirms the relational architecture of Documents 03 and 10:

- `従う` does not equal `支える`;
- `支える` does not imply permanent jurisdiction;
- `信じる / 信頼` operate under uncertainty;
- `頼る` can name explicit dependence without surrendering all judgment;
- emergency intervention remains most defensible when it returns judgment rather than replacing it indefinitely.

Nothing in the Japanese supports turning support into disguised obedience or, conversely, claiming that every caring restriction is illegitimate.

---

# XI. Personhood vocabulary remains distributed across several properties

Phase 8 re-verifies the major personhood-related forms:

- `人格`
- `疑似人格`
- `自我`
- `自己同一性`
- `意志`
- `意思`

The source does not supply one recurring Japanese noun equivalent to the English philosophical category **personhood** used by Document 08.

The distinctions remain analytically productive:

- `人格` can establish personality/person-like organization without settling moral standing or numerical identity.
- `疑似人格` marks constructed provenance without automatically meaning morally counterfeit.
- `自我` supplies evidence of self-structure.
- `自己同一性` concerns identity continuity/integrity.
- `意志` can coexist with command constraint: Kiriya is the clearest case because the source explicitly combines `人格と意志` with inability to disobey a superior command.
- `意思` is context-sensitive and should not be forced into a universal metaphysical contrast with `意志`.

Phase 8 therefore confirms the property-by-property ontology of Documents 08, 11, 12, 14, and 16. Biological origin, intelligence, memory, personality, singular identity, local judgment, terminal-end revision, moral standing, and civic status remain separate questions.

---

# XII. Forgiveness: `赦す` and `許す` are evidentiary, not an absolute dictionary wall

The source verifies the corpus’s mature caution.

V07 contains `赦しではない`, while V11 contains `許してくれとは言わない`. V14 makes the overlap impossible to ignore: narrator-level prose can use `赦す` for Shin’s refusal to forgive one perpetrator, while Shin himself later uses `許す` when describing his relationship to Rei.

Thus orthography is meaningful evidence but not a complete semantic partition.

A safe rule is:

> **Track the written form, speaker, object, and context; do not equate `赦す` with all moral forgiveness and `許す` with permission only.**

This supports T14-C22. Nonrevenge still does not equal forgiveness, but the distinction cannot be outsourced to a one-line kanji dictionary.

---

# XIII. Justice and political self-authorization

Phase 8 directly verifies one of Document 12’s strongest political-language findings.

V14 opens with the revolutionary aspiration:

`我ら、世界に誇る正義たらん`

Later, the reactionary argument rewrites the slogan into identity:

`我らはすなわち正義である`

The surrounding lines make the shift explicit: if “we” are justice, then whatever “we” do can be declared correct. The difference is therefore not merely stylistic translation. It is a change in the grammatical and political relation between polity and normative standard.

- `正義たらん`: justice remains something toward which one strives.
- `正義である`: justice becomes something the group asserts itself to be.

The first leaves conceptual room for self-judgment against a standard. The second can make the institution self-certifying.

V13 supplies the complementary `幻想` passage. Rights, freedom, equality, and justice are called non-self-existing constructs whose value citizens must actively preserve and maintain. Translating `幻想` here as “therefore worthless delusion” would reverse the argument. The source says their lack of natural self-enforcement is precisely why civic effort matters.

This strengthens the constitutional-fallibilist reading of Document 06 and the V14 political conflict in Document 18.

---

# XIV. Lena’s titles and the address system

The source-language corpus continues to treat Lena’s titles as relationally variable rather than essential identities.

Tracked forms include:

- military rank;
- `女王`;
- `鮮血の女王`;
- `女王陛下`;
- `聖女`;
- full name;
- personal `レーナ`.

A particularly strong control occurs when Shiden switches from her usual teasing/relational `女王陛下` to the personal `レーナ`. The narration notices the change. That makes the address shift explicit evidence rather than analyst projection.

V13 offers another compact register transition inside one utterance: `〈アンダーテイカー〉` → `ヴラディレーナ・ミリーゼ大佐` → `シン`. Role, formal command identity, and personal relation coexist rather than replacing one another.

Phase 8 therefore confirms Document 03’s rule: Bloody Queen, Queen, Colonel, Saint, and Lena are roles/registers activated in different relations. None alone names her mature essence.

---

# XV. Shin’s voice: semantic expansion without stylistic replacement

The Japanese source supports the longitudinal claim that Shin does not “learn to speak like a therapist.” His voice remains terse, low-excess, and structurally recognizable while becoming capable of admitting more.

The V14 control is especially strong:

`痛かった`

The value of this line lies partly in its simplicity. It does not convert Shin into a new, floridly introspective narrator. The larger passage then expands what the compact admission names: strangulation, blame, abandonment, and long-lived pain.

Earlier source controls show the same pattern through:

- explicit requests not to be left behind;
- acknowledgment of weakness;
- future-oriented wishes;
- desire to show and share places;
- permission to rely on others.

Phase 8 therefore preserves the mature voice model: **development through semantic admission within a stable character register**.

---

# XVI. Dependence, request grammar, and the Shin/Lena relationship

The source confirms several distinctions that Phase 7 required the capstone to keep visible.

In V06, `おいていかないでください` is grammatically a request. It matters because Shin verbalizes dependence rather than converting it entirely into unilateral self-sacrifice or silent expectation. Lena’s corresponding command to return does not erase the request structure; it forms part of an asymmetrical but reciprocal relational pattern.

V09’s language of `頼る`, `一緒に`, and `共` confirms willingness to rely, carry burdens together, and imagine ordinary futures. These forms support reciprocal dependence. They do not establish perfect symmetry or immunity from possessiveness.

V14 prevents romantic purification through the explicit cry:

`その人はわたしのものだ！ 返せ！`

The possessive rhetoric is real and must remain in the synthesis. The surrounding action still supports a separate claim: Lena’s intervention returns Shin from No Face’s captured-purpose structure to a state in which his own judgment can resume. Language of possession and agency-restoring behavior coexist.

The correct finding therefore remains mixed:

> **Shin/Lena is neither a model of autonomous nondependence nor a purity model of nonpossessive love. Its ethical achievement lies in the repeated restoration of answer and judgment despite real dependency, fear, jealousy, asymmetry, and possessive impulses.**

---

# XVII. No Face, freedom, and purpose capture

V14’s rejection of No Face’s offer contains the phrase:

`心一つも自由にならない`

The surrounding speech does not reject machine embodiment simply for being machine embodiment. It rejects a supposed paradise in which there is no happiness and no freedom of the heart, only inexhaustible hatred continued by subjects who can no longer recognize the condition as suffering.

This source context matters because it prevents two overreadings:

1. **substrate essentialism** — that machine existence is intrinsically false or inferior;
2. **surface-intelligence equivalence** — that memory, speech, or strategic cognition by themselves establish unrestricted agency.

The passage remains strong evidence for **purpose capture** as an analytical description: substantial local intelligence can coexist with a terminal end that the subject cannot revise. Exact No Face/Vaclav continuity remains open.

---

# XVIII. Anti-hero language and military context

Phase 8 directly rechecks both of the high-risk `英雄` passages.

V07 says that heroes should not exist in the present age. Read in isolation, this can be made to sound like a rejection of heroic action. V05 supplies the technical context: modern weapons and distributed force make the solitary sword-wielding hero an inefficient mode of war; `英雄とはもはや、弱者の戦術だ` concludes a discussion of force design and killing efficiency.

The wider military corpus meanwhile repeatedly admires extraordinary courage and competence.

The language therefore supports Document 07’s narrower conclusion:

> **The series criticizes structural dependence on exceptional persons more strongly than it criticizes exceptional action itself.**

This also confirms P7-R08. A tactically admirable act, an operational necessity, a strategic dependency, and a political-constitutional claim on a person are different levels. The capstone must name the level before moving between them.

---

# XIX. Focalization: Lena’s insight does not become omniscient narration

V14’s Rei-wound sequence is an important epistemic control because three evidence states appear close together.

First, Lena speaks: she tells Shin that an old wound can still hurt because what happened mattered, not necessarily because he has failed to forgive. This is compassionate interpretation from outside Shin.

Second, Shin answers in his own words: `痛かった`, then elaborates what hurt.

Third, the narrator describes his crying and bodily dependence in the moment.

The sequence supports Lena’s insight without converting the first statement into an omniscient metaphysical ruling. The evidence becomes stronger because Shin subsequently confirms part of what she proposed in his own language.

This is representative of the broader focalization rule:

> **A character may be insightful, narratively privileged, and later corroborated without acquiring permanent interpretive sovereignty over another subject.**

Phase 8 finds Document 12’s narrator/focalizer distinction source-secure.

---

# XX. Temporal and modal grammar

The Japanese repeatedly carries analytical limits in small grammatical elements.

High-value examples include:

- `しか` — restrictive exclusivity in the pride system;
- `もう` — changed present relation to a former self-description;
- `まだ` — not-yetness rather than incapacity as essence;
- potential forms such as `戻ってこられる` — capability/possibility rather than certainty;
- `いつか` and other future markers — imagined horizon without guarantee;
- imperative/request contrasts — relevant to command, reliance, and intimacy.

These features matter because English synthesis naturally smooths them into nouns: “recovery,” “return,” “freedom,” “future.” Phase 8 confirms that the capstone should preserve modality whenever the claim is load-bearing.

In particular, V14 does not linguistically guarantee that everyone or every polity will recover. It asserts that changed conditions make return **possible** for others as well.

---

# XXI. Alter.1 as a metalinguistic control

Alter.1 remains supplemental rather than mainline chronological authority, but its direct metalinguistic statements can be unusually useful for voice analysis.

Frederica explicitly says that her way of choosing words is part of herself and not something she wishes simply to discard. The source therefore confirms a conclusion that might otherwise look like analyst aesthetic preference: her archaizing register is not merely ornamental comic speech that development should erase.

This supports the larger voice principle of Document 12:

> **Maturation in *86* need not mean convergence toward one neutral adult voice.**

Shin can remain terse; Kurena can remain emotionally transparent; Frederica can retain stylized imperial language; Fido and Lerche can retain formal or role-inflected registers. Development can occur through what those voices are able to admit and do.

---

# XXII. Document 12 source-verification result

Document 12 remains canonical, with one reference-layer correction applied.

## 22.1 Correction: **兵科転換**

The earlier document used **兵科転換** in a way that visually resembled a source lexeme. Direct search of the locked Japanese corpus found no such compound. The relevant V09 source says:

`兵科が変わるなら教育内容も変わるから`

The intended analytical point was correct: changing service branch can change training while military service continues. The defect was the presentation of an analyst-compressed noun as if it were source vocabulary.

Document 12 now uses the attested `兵科が変わる`, supplies the current source coordinate, and explicitly labels the Phase-8 correction.

## 22.2 Global inline-Japanese attestation

After correction, all **170/170 unique Japanese inline-code spans** in Document 12 are attested somewhere in the current locked V01–V14+Alter.1 corpus.

This global attestation check does not replace locator-specific context review, but it supplies a useful negative control: no remaining code-form Japanese analytical shorthand masquerades as source vocabulary.

### Document-12 verdict

**SOURCE VERIFIED WITH ONE REFERENCE CORRECTION; NO LOAD-BEARING INTERPRETATION OVERTURNED.**

---

# XXIII. Document 16 source-verification result

Document 16 remains the canonical Japanese passage/terminology retrieval index.

All **214 stable `JP-*` entries** still route to valid Phase-5 locator IDs, and the complete Phase-5 route layer now has current-source verification. All **55 high-value controls** and **28 terminology-lock rows** are covered.

Two presentation repairs were necessary.

## 23.1 `JP-ADDR-011`

The prior compact display had malformed nested-code formatting and did not cleanly expose the actual address sequence. It now displays the attested sequence:

`〈アンダーテイカー〉` → `ヴラディレーナ・ミリーゼ大佐` → `シン`

The stable ID and `V13-L082` route remain unchanged.

## 23.2 `JP-RETURN-015`

The prior compact display mixed a Japanese term with an English analytical suffix inside malformed code formatting. It now displays the source wording:

`帰還だけは、許可できません`

The stable ID and `V13-L115` route remain unchanged.

## 23.3 Quotation-state preservation

Document 16’s narrower `EXACT_ANCHOR` state remains intact. Phase 8 does not “upgrade” entries merely because the broader source context has now been checked. Stable quote-state distinctions are part of provenance.

### Document-16 verdict

**214/214 ROUTES CURRENT-SOURCE VERIFIED; TWO PRESENTATION DEFECTS REPAIRED; NO ID OR INTERPRETATION CHANGE.**

---

# XXIV. Provisional Document 18 source-language result

Document 18 remains byte-identical to the Phase-7 audit target at:

`9f19fd985aaf292890adc1dffc31bf6253c970aa1dd0cb0eef8f3a379efb6704`

Phase 8 deliberately did not revise it.

A global Japanese-span attestation check finds **38/38 unique Japanese inline-code spans** in the current provisional capstone present in the locked source corpus. More importantly, the Phase-7 P0/P1 queue was checked at full source context rather than by string existence alone.

The following load-bearing systems pass:

- opening administrative grammar (`その戦場に、死者はいない`);
- Theo’s names accusation;
- pride exclusivity (`誇りしか...もう`);
- V14 potential `戻ってこられる`;
- `正義たらん` versus `正義である`;
- Lena’s explicit possessive rhetoric;
- No Face and freedom of heart;
- anti-hero vocabulary in force-design context;
- Gentle World anti-theodicy / Undertaker contingency;
- Shin’s request not to be left behind;
- reliance and shared burden in V09;
- distributed personhood vocabulary;
- the V14 focalization sequence around Shin’s wound.

### Document-18 verdict

**NO LOAD-BEARING JAPANESE FAILURE.** The document remains `active_provisional` solely because the nine Phase-7 revisions have not yet been merged and revalidated.

---

# XXV. Phase-7 source-language result

The canonical Phase-7 artifact is verified at SHA-256:

`20e2782310151862b5303ffb01b40a2eb1a60dddef8b7604cbe1a2a1c3eb9909`

All **23/23 unique Japanese inline-code spans** in the current Phase-7 audit are source-attested. Its P0/P1 Japanese verification queue survives direct source review.

This matters because Phase 8 initially encountered a stale local post-conversation copy of Phase 7 whose bytes did not match the canonical Drive checksum. The audit did not treat that stale local file as authority. The canonical Drive artifact was re-fetched and matched its recorded checksum before Phase-8 adjudication continued.

This provenance correction changes no Phase-7 conclusion. It demonstrates why the project’s authority metadata and checksums matter.

---

# XXVI. Adjudication of P7-R01 through P7-R09

Phase 8 does not execute the revisions. It decides whether Japanese verification confirms, weakens, or overturns them.

| Revision | Phase-8 source result | Disposition before capstone merge |
|---|---|---|
| **P7-R01** | Multiple return systems are textually distinct; identity should not be pathologized as something from which people simply “return.” | **CONFIRMED MANDATORY** |
| **P7-R02** | No Japanese master term supports treating the capstone’s double claim as one causal explanation of every domain. | **CONFIRMED MANDATORY** |
| **P7-R03** | V01 language establishes administrative denial and person-erasing classification, not the creation of moral standing by recognition. | **CONFIRMED MANDATORY** |
| **P7-R04** | `生還 / 帰還 / 帰る` and related forms clearly distinguish operational survival/extraction from relational return. | **CONFIRMED MANDATORY** |
| **P7-R05** | `戻る`, `帰る`, `生還`, restoration of legal standing, and recovery of judgment are analogous only after their properties are specified. | **CONFIRMED MANDATORY** |
| **P7-R06** | Personhood vocabulary and disability evidence independently prove that claim-bearing standing, agency, identity continuity, health, and flourishing cannot be collapsed. | **CONFIRMED MANDATORY** |
| **P7-R07** | Japanese verification does not reduce the independent causal roles of the ensemble; no linguistic evidence supports protagonist causal monopoly. | **CONFIRMED MANDATORY** |
| **P7-R08** | Military vocabulary and return terminology become misleading when tactical/operational claims are promoted into political legitimacy without naming the level. | **CONFIRMED MANDATORY** |
| **P7-R09** | The source distributes relevant concepts across many lexemes and grammatical structures; the V2 master terms are demonstrably analytical glosses. | **CONFIRMED MANDATORY** |

All nine revisions should therefore be applied in one explicit post-Phase-8 capstone revision rather than piecemeal silent edits.

---

# XXVII. T14 adversarial constraints after source verification

All **41** T14 dispositions remain in force.

Phase 8 gives particular linguistic reinforcement to several of them:

- **C01–C03:** no source-language evidence makes endless revisability, open futurity, or weak identity the universal moral test.
- **C04–C05:** return vocabulary is heterogeneous and return to a prior state can be negative.
- **C07–C08:** pride and durable identity are not intrinsically pathological.
- **C10–C12:** support, obedience, trust, reliance, and possessiveness remain distinct.
- **C14–C15:** anti-hero language is situated within force design and institutional dependence, not a rejection of competence or courage.
- **C18–C21:** bodily function, medical authority, and combat competence do not determine standing or adulthood.
- **C22–C23:** nonrevenge, forgiveness, permission, and legal repair remain distinct.
- **C24–C26:** freedom and justice are maintained institutional achievements, not self-executing labels or warrant for guardianship.
- **C27:** later Sector comparison remains mechanism-specific rather than historical equivalence.
- **C30:** artificial origin does not settle standing; Japanese personhood terms remain property-specific.
- **C31:** home/homeland/return systems do not reduce to one chosen-versus-inherited binary.
- **C34–C35:** no Japanese word turns visual motifs or imagery into an omniscient symbolic dictionary.
- **C36–C41:** V14 remains an opening of final-arc problems, not their closure.

No T14 disposition is relaxed because a compact Japanese phrase “proves” the broader synthesis. Source language constrains interpretation; it does not replace argument.

---

# XXVIII. Open questions remain open

All **32** Phase-5/T14 final-arc questions remain unresolved at the V14 boundary.

Japanese verification cannot legitimately close questions that require later events or additional primary-source evidence, including:

- Federacy constitutional survival;
- consent behind the New Imperial Court and Shin’s War Emperor role;
- emergency-power expiry;
- postwar justice and repair;
- Fawn civic integration;
- artificial-subject civic standing;
- Lyudmila generalizability;
- No Face’s terminal-end revisability;
- exact Vaclav/No Face continuity;
- Zelene continuity;
- Phonix individuality;
- Shin’s medical honesty and postwar vocation;
- Undertaker after war;
- Lena’s overresponsibility and interpretive authority;
- Raiden’s own future;
- Theo’s post-disability choice;
- Kurena’s independent worth;
- Anju/Dustin alongside Daiya memory;
- Frederica’s self-rule;
- Spearhead divergence;
- military vocation versus conditioning;
- and the future meaning of Eighty-Six identity after war.

The fact that V14 uses potential, future, or aspirational grammar in several places makes this restraint more—not less—important.

---

# XXIX. Corrections ledger

Phase 8 applies exactly three reference-layer corrections to the Phase-6 language surface.

| Artifact | Defect | Correction | Analytical effect |
|---|---|---|---|
| Document 12 | **兵科転換** looked like a source lexeme but is not attested in the locked corpus. | Replaced with attested `兵科が変わる` at V09 source context. | **None to substantive interpretation.** Clarifies source/analysis boundary. |
| Document 16 `JP-ADDR-011` | Malformed compact display obscured the exact address sequence. | Displays `〈アンダーテイカー〉` → `ヴラディレーナ・ミリーゼ大佐` → `シン`. | **None.** Stable ID/locator unchanged. |
| Document 16 `JP-RETURN-015` | Malformed compact anchor combined Japanese with an English analytic suffix. | Displays source-exact `帰還だけは、許可できません`. | **None.** Stable ID/locator unchanged. |

No correction changes a T14 disposition, specialist thesis, or final-arc open question.

---

# XXX. What Phase 8 does not prove

A successful source audit can be overread just as easily as a thematic synthesis.

Phase 8 does **not** prove that:

- every English gloss has one fixed Japanese equivalent;
- an attested line has only one reasonable interpretation;
- narrator, focalizer, and character statement are interchangeable;
- later volumes will validate the current open questions;
- the V2 master thesis is a hidden authorial keyword;
- machine personhood is solved by vocabulary alone;
- love is healthy because its language is reciprocal;
- military necessity is political legitimacy;
- or Document 18 is already canonical.

Its narrower accomplishment is stronger precisely because it is narrower:

> **The current V2 language-sensitive claims have been checked against the actual locked Japanese source objects, at their retrieval coordinates and relevant local contexts, and the mature distinctions survive.**

---

# XXXI. Phase-8 release artifacts and machine-readable evidence

The canonical Phase-8 release should be accompanied by the following machine-readable sidecars:

1. `86_PHASE8_SOURCE_INTEGRITY_RECHECK.tsv`
   - fifteen admissible source objects;
   - exact Phase-5 SHA comparison;
   - CRC result;
   - XHTML-document count.

2. `86_PHASE8_TERMINOLOGY_VERIFICATION_LEDGER.tsv`
   - all 28 Phase-5 Japanese terminology locks;
   - source excerpt;
   - quote state;
   - later-synthesis constraint.

3. `86_PHASE8_HIGH_VALUE_PASSAGE_VERIFICATION_LEDGER.tsv`
   - all 55 high-value Document-12/16 controls;
   - stable JP ID;
   - locked locator route;
   - quote state;
   - source-verification excerpt.

4. `86_PHASE8_LOCATOR_SOURCE_VERIFICATION_SUMMARY.json`
   - aggregate current-source result for all 1,045 locator routes;
   - preserves exact/paraphrase/coordinate-only distinctions;
   - records the two compound-route rechecks.

5. `86_PHASE8_JAPANESE_SOURCE_CORRECTION_LEDGER.tsv`
   - records the one Document-12 source-form correction and two Document-16 compact-anchor presentation repairs;
   - preserves stable IDs, coordinates, quote states, and interpretive-effect classification.

These sidecars are audit infrastructure, not alternative literary authorities. The Japanese EPUB remains primary.

---

# XXXII. Final Phase-8 verdict

The Japanese-source verification gate passes.

The corpus enters the next step with the following state:

- **15/15** admissible Japanese source binaries re-hashed to the locked identities and CRC-clean;
- **1,045/1,045** Phase-5 locator routes verified against current source;
- **1,023** quotation/anchor-grade routes source-exact;
- **21** paraphrase routes context/coordinate verified without quote-state inflation;
- **1** coordinate-only provenance route preserved as coordinate-only;
- **28/28** Phase-5 Japanese terminology locks source-exact;
- **55/55** high-value passage controls verified;
- **170/170** current Document-12 Japanese inline-code spans source-attested after correction;
- **38/38** provisional Document-18 Japanese inline-code spans source-attested;
- **23/23** canonical Phase-7 Japanese inline-code spans source-attested;
- **3** reference-layer presentation/source-form corrections applied across Documents 12 and 16;
- **0** load-bearing interpretations overturned;
- **P7-R01 through P7-R09** all confirmed mandatory;
- **41/41** T14 constraints preserved;
- **32/32** open questions preserved.

The release verdict is therefore:

> **`PASS_WITH_CORRECTIONS_APPLIED` — Japanese source verification complete; Phase-7 revision queue confirmed; Document 18 remains `active_provisional` pending explicit audited revision and revalidation.**

The strongest practical consequence is that the project no longer needs another exploratory linguistic synthesis before revising the capstone. The source-language layer is sufficiently locked for the current boundary. Future V15+ work must reopen the source boundary rather than silently extending this audit.

---

# XXXIII. Next gate — audited capstone revision and promotion

The next operation is not another specialist monograph. It is an explicit revision of:

`18_FULL_SERIES_CONTINUOUS_SYNTHESIS.md`

The revision must:

1. apply **P7-R01 through P7-R09**;
2. preserve the current V14 source boundary;
3. keep all 32 final-arc questions open;
4. retain all 41 T14 adversarial constraints;
5. preserve Documents 12 and 16 as the source-language authorities;
6. avoid changing stable locator IDs;
7. re-run locator, Japanese-span, dependency, duplication, YAML, and checksum validation;
8. produce a revision crosswalk showing exactly where each P7 requirement was satisfied;
9. change authority from `active_provisional` to `canonical` only if the revised candidate passes every gate.

The current provisional Document-18 checksum remains the immutable pre-revision baseline:

`9f19fd985aaf292890adc1dffc31bf6253c970aa1dd0cb0eef8f3a379efb6704`

A new checksum after revision will make the authority transition explicit rather than silently mutating the audited target.

