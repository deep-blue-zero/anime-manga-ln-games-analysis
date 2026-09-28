---
series: WUWA
character: Iuno
artifact_type: character_specialist_profile
analytical_responsibility: "Resolve all archive raw-ID/Content-key offsets and bound combat fate, existence, and companion language by source trigger"
scope: IUNO_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: IUNO_PRE_AV_V0_1
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

# Iuno — the archive's moon and fate speech needs its own clock

All **80** favor-word rows in the pinned Iuno `character_source_package.json` have raw `Id` exactly **one greater** than the numeric suffix of their actual `Content` text key. That arithmetic describes this frozen source generation; it is **not** a retrieval API. Preserve the raw row's `Content`, exact `favorword.json` locator and text-map witnesses. A guessed key may exist and return an adjacent, valid but wrong voice line. Raw ID `141050`, for example, is Resonance Skill XII at `favorword#/2588` with actual `FavorWord_141049_Content` (“Fate... revealed” in EN); guessed `_141050_Content` is Liberation I (“Taste my resolve!”). Raw `141070` is Fallen II at `#/2608` with actual `_141069_Content`, whereas guessed `_141070_Content` is Fallen III. These errors could reverse both the trigger and the narrative inference without causing a missing-key error.

`favorword#/N` below expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/favor/favorword.json#/N`. Ranges are a compact census, not a direction to synthesize a key; the [private-source validator](reproduce_validation.py) joins and checks **each** of the 80 rows individually.

| Source family | Raw ID range | Actual Content-key suffix range | Exact source-index range | Rows |
|---|---|---|---|---:|
| Thoughts I–V | `141002–141006` | `141001–141005` | `2540–2544` | 5 |
| Preference, relations, greeting and team archive | `141007–141027` | `141006–141026` | `2545–2565` | 21 |
| Ascension I–V | `141028–141032` | `141027–141031` | `2566–2570` | 5 |
| Heavy/skill/liberation/intro/outro, damage and world-system triggers | `141033–141081` | `141032–141080` | `2571–2619` | 49 |

All 80 exact locators join 80 complete semantic archive-voice rows in the private complete-line analysis. The 49 combat/system rows join **49 event IDs and 196 distinct, locally PCM-valid EN/JA/KO/ZH objects**; the objects are already inside the packet's 2,155-object full selected corpus. A valid WEM/PCM/FLAC hash or event ID proves the local technical chain, not that the event played in a particular story scene. Official-client sound is a separate raw-evidence authority from the frozen normalized Arikatsu semantic view. Neither authority alone proves acted emotion or observed trigger execution. The 24 selected case JSON remains a separate 24-line/96-render sample; this specialist does not silently enlarge it.

## Three interpretive traps inside the trigger rows

**Fate rhetoric is not recovered clairvoyance.** At `favorword#/2586–2588`, actual keys `FavorWord_141047–141049_Content`, Resonance Skill X–XII speak of overturning causality, piercing or reshaping a future, and showing fate. ZH XII says “命运，如我所示”; EN shortens this to “Fate... revealed,” JA says fate as shown, and KO promises to show it. The lines are real evidence that Iuno's combat persona still speaks in the vocabulary of the Priestess and the Moon Arrow. They do not demonstrate that post-trade Iuno again sees the old clear fate-threads. Her direct quest explanation at `flow#/8386/4/19–20` says she exchanged that way of seeing for power against the Dark Tide. An observed later divination that accurately reads a new future would revise that ability claim; a skill bark, even a decoded one, cannot by itself. “I am the moon” at Skill IV, `#/2580`, is similarly an enacted combat assertion, not proof she literally became an omnipotent lunar being [IUN-E14 E36; IUN-C01 C31].

**A fall trigger is not a completed erasure or historical death.** Fallen I–III are raw IDs `141069–141071`, actual keys `_141068–141070_Content`, at `#/2607–2609`. Fallen II is especially sensitive: ZH “我，已存在过……” and KO use past-existence language, JA “私は、存在している……” is present-oriented, and EN substitutes “I've... left my mark…” for a literal existence claim. That variation matters for a future line-paired listening question about defiance, disappearance or a still-present self. It cannot be flattened into one verb tense across four dubs, and the source trigger is gameplay defeat rather than the dated Chaos return. Fallen III's falling moon imagery similarly does not show the story's Moon Arrow failed or that the returned Iuno canonically died. The story's partial remnant and social nonrecognition have their own graph and archive evidence, which must be read on their own clocks [IUN-E07 E17 E20 E33; IUN-C02 C12].

**Team/world barks are address and preference evidence with limited recipients.** Outro Skill IV at `#/2598`, raw `141060`/actual `_141059_Content`, addresses a “Hero of Heroes” in ZH/EN and changes the exact clause in JA/KO. Its event path includes `exitskill_double_01`, but a path suffix is not a dated partner encounter or proof that a specific ally received the line; runtime pairing remains to inspect. Sensor at `#/2614`, raw `141076`/actual `_141075_Content`, says the situation is expected in all four witnesses; it is a local expectation, not a fresh clear prophecy. Supply Chest III at `#/2618` offers more if the recipient likes the find, while IV at `#/2619` jokes that fate can occasionally be kind. Those lines make room for generosity, teasing and chance in her ordinary speech without turning a chest trigger into a dated private gift, exclusive affection or a claim that fate literally distributes treasure. “Miss me already?” at Outro V also needs a live recipient before it can be a relationship conclusion [IUN-E09 E23 E28–E29; IUN-C14 C23–C24].

## Retrieval and falsification sequence

For a first bounded four-dub listen, use exact positions `#/2580` (moon assertion), `#/2586–2588` (causality/future/fate), `#/2598` (Hero of Heroes), `#/2607–2609` (fallen set), `#/2614` (Sensor), and `#/2618–2619` (chests). Record raw ID, actual key, source locator, semantic occurrence, event path/ID, per-language bank/media object, runtime variant, WEM/PCM/FLAC hashes, channel and subtitle extent. Check the runtime trigger and reachable teammate/context before coding a delivery as proud, frightened, resigned, flirtatious or generous. In particular, contrast Fallen II's four different aspect choices against the *dated* `7759/3` return and `8386/4` ability explanation; do not conflate semantic resemblance with temporal co-occurrence.

The finding would change if a new pinned source generation changed the mapping, if an exact runtime capture contradicted a title/trigger association, if a later direct quest showed recovered clairvoyance, or if a recorded teammate response established the addressee of an Outro. Those require separately identified witnesses. No human four-dub listening, observed combat playback, new ability or canonical death is asserted by this profile.
