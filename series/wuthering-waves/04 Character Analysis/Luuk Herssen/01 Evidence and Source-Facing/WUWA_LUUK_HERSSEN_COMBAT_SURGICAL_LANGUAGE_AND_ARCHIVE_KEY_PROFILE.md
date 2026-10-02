---
series: WUWA
character: Luuk Herssen
artifact_type: character_specialist_profile
analytical_responsibility: "Resolve combat raw-ID/Content-key mismatches and bound Luuk's surgical, analgesic and death imagery by trigger and localization"
scope: LUUK_HERSSEN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: LUUK_HERSSEN_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Luuk Herssen — a surgeon's combat register is not a treatment record

The pinned `character_source_package.json` holds **77** Luuk favor-word rows. In one continuous source block, raw IDs `151038–151059` do **not** equal the suffixes of their actual localized `Content` keys. The first twenty-one shift one number forward; the final Hit I row points to `_151078_Content`. All 22 raw locators join 22 complete semantic voice rows and **88** distinct, locally PCM-valid EN/JA/KO/ZH render objects with 22 event IDs. The join proves what the frozen source and local audio map contain; it does not prove which bark fired in a playthrough or how it was acted. The [packet validator](../04%20Validation%20and%20Readiness/reproduce_validation.py) checks every row/key/text/event/media join. This source family was not among the [twenty selected listening cases](../03%20Audiovisual%20and%20Voice/AUDIO_MATCHED_SEMANTIC_CASES.json), so those cases remain a 20/80 sample, not an 108-render sample after adding these observations.

`favorword#/N` below expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/favor/favorword.json#/N`. The middle column is the suffix of the **actual** `FavorWord_{suffix}_Content` key; it must not be constructed from the raw ID. The trigger class comes from the pinned EN title metadata and needs runtime confirmation before a claim about frequency or played context.

| Raw row ID | Actual Content suffix | Exact source position | Trigger class |
|---:|---:|---:|---|
| 151038 | 151039 | `favorword#/3190` | Basic Attack VII |
| 151039 | 151040 | `#/3191` | Basic Attack VIII |
| 151040 | 151041 | `#/3192` | Aerial Attack I |
| 151041 | 151042 | `#/3193` | Aerial Attack II |
| 151042 | 151043 | `#/3194` | Aerial Attack III |
| 151043 | 151044 | `#/3195` | Resonance Skill I |
| 151044 | 151045 | `#/3196` | Resonance Skill II |
| 151045 | 151046 | `#/3197` | Resonance Skill III |
| 151046 | 151047 | `#/3198` | Resonance Skill IV |
| 151047 | 151048 | `#/3199` | Resonance Skill V |
| 151048 | 151049 | `#/3200` | Resonance Skill VI |
| 151049 | 151050 | `#/3201` | Resonance Skill VII |
| 151050 | 151051 | `#/3202` | Resonance Skill VIII |
| 151051 | 151052 | `#/3203` | Forte Circuit I |
| 151052 | 151053 | `#/3204` | Forte Circuit II |
| 151053 | 151054 | `#/3205` | Resonance Liberation I |
| 151054 | 151055 | `#/3206` | Resonance Liberation II |
| 151055 | 151056 | `#/3207` | Resonance Liberation III |
| 151056 | 151057 | `#/3208` | Intro Skill I |
| 151057 | 151058 | `#/3209` | Intro Skill II |
| 151058 | 151059 | `#/3210` | Intro Skill III |
| 151059 | 151078 | `#/3211` | Hit I |

This is a collision-prone map, not just a bookkeeping curiosity. A program that interpolates raw `151053` into `FavorWord_151053_Content` would get the *Forte Circuit II* text key, while the actual Liberation I key is `FavorWord_151054_Content`. Raw `151059` is Hit I/key `FavorWord_151078_Content`; a synthesized `_151059_Content` names Intro Skill III at the previous row. A lookup can therefore pass “key exists” and still attach a valid four-dub render to the wrong trigger and moral interpretation. Preserve raw ID, exact row locator, raw `Content`, semantic occurrence ID, event path/ID, language-specific media ID, runtime variant and WEM/PCM/FLAC hashes separately. Do not use a friendly filename or assumed integer offset; the final row breaks that offset anyway.

## Three meanings of the scalpel that must not be collapsed

**Procedure as attack syntax.** Basic/Aerial/Skill/Forte lines at `#/3190–3204` use vessels, incision, imbalance, pain and reconstruction. Raw `151044`/key `_151045_Content` at `#/3196` is titled Resonance Skill II and invokes incision; raw `151050`/key `_151051_Content` at `#/3202` refers to revealing a pulse or vessels, with EN leaning toward exposed veins and KO toward pulse analysis. Aerial Attack III at `#/3194` promises an end to suffering. The medical lexicon is genuine evidence that Luuk carries his clinical conceptual vocabulary into combat. It is *not* a patient chart, an observed medical intervention, or proof that he regards every combat target as a consenting patient. His story has real medical treatment, covert intelligence and force in different situations: he treats an enemy while undercover (`FavorStory_151003_Content`), restrains Rhein rather than kill him (`FavorStory_151005_Content`), and admits hatred while pursuing the Architect (`flow#/12320/5`). None can be replaced with a one-line sanitized or sadistic essence [LUK-E04, E06, E13–E14].

**Funeral and mercy as an enemy-facing battle register.** The three Liberation rows at `#/3205–3207` combine surgeon, funeral, execution, mercy and enduring quiet in different ways. Raw `151053`/key `_151054_Content` is explicitly titled Liberation I; raw `151054`/key `_151055_Content` uses merciful-death language in all four witnesses, with KO overtly phrasing it as executing a sentence; raw `151055`/key `_151056_Content` offers final quiet. This is darker than claiming he is a harmless doctor who would never kill. But a combat bark does not establish an actual killing in a dated scene, a policy of euthanizing patients, or a right to decide Rhein's fate against his wishes. The ethical tension remains live: Luuk can be capable of lethal rhetoric and violence while still opposing use of human bodies as experimental material and choosing restraint on a specific brotherly occasion. A future sourced encounter in which he deliberately harms someone seeking care would materially revise that account; the barks alone do not supply one [LUK-E02–E06; LUK-C08–C09].

**Analgesia as a localization fork, not one fixed bedside manner.** Intro Skill I, raw `151056`/key `_151057_Content` at `#/3208`, is not four identical promises of comfort. ZH and EN announce pain relief, JA asks whether pain has eased, and KO warns that it will hurt. Intro Skill II at `#/3209` warns that movement worsens pain; Intro Skill III at `#/3210` says immediate procedure in ZH/EN, while KO can sound closer to summary disposal/punishment. The source title and Wwise event class point to gameplay entry, not a named patient encounter. A model using only EN might make the line an unconditional analgesic assurance; using only KO could make him enjoy causing pain. Neither is a safe four-dub default. Direct listening may show whether a particular actor plays concern, threat, deadpan procedure or something mixed; wording and object completeness do not settle performance [LUK-C19, C31].

The Hit I row is a further causal reversal hazard. At `#/3211`, raw `151059`/actual key `FavorWord_151078_Content`, the **trigger title is Hit I**. ZH, JA and KO refer to a deep wound, and EN says “incision.” If an extractor guesses `_151059_Content`, it retrieves the preceding Intro Skill III; if an analyst trusts EN's surgical noun without the Hit trigger, they may write Luuk *inflicting* the cut. The source as retained is a reaction to being hit, though the exact animation and target of the blow need runtime observation. This fits his documented wound/pain constraints more naturally than a conclusion of perfect physical immunity, but it cannot be used as a dated story injury or a clinical case history [LUK-E01, E30].

## Reproduction and next perceptual test

The private complete-line analysis provides 22 semantic occurrence IDs and four render objects per row. Each render is `flac_roundtrip_pcm_identical`, with its explicit event path/ID, numeric media ID, source virtual WEM path/hash and canonical PCM/FLAC hashes. The 88 objects are already within the packet's 2,855-object measured corpus; they must not be added to that denominator again. The source-defined eleven-cohort acoustic study covers **127 story-action lines**, not this 22-line archive-trigger set. It cannot determine whether Luuk's combat voice is louder, colder or more surgical than his clinic voice; such an inference would require a separate matched, channel-aware and human-reviewed design.

For a bounded first listen, nominate `#/3194` (ending pain), `#/3196` (incision), `#/3205–3207` (three Liberations), `#/3208–3210` (three Intro Skills), and `#/3211` (Hit I). Log the exact raw ID, actual Content key, language, semantic occurrence, render variant, event, media and hashes; check subtitle/voice extent, then capture whether the runtime trigger label matches observed playback. A reviewer should ask *who is addressed* and *what action is being performed* before labeling a delivery reassuring, cruel or ironic. No human four-dub listening, trigger capture, patient event or canonical kill is claimed here. A new source generation could preserve the vocabulary while changing key alignment; it must receive a separate audit rather than silently replacing this frozen map.
