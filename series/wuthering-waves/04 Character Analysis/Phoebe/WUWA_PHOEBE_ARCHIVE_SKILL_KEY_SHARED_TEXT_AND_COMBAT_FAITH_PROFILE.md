---
series: WUWA
character: Phoebe
artifact_type: character_specialist_profile
analytical_responsibility: "Resolve permuted skill keys and cross-character nonlexical key reuse; bound combat faith, pain and farewell claims by trigger and localization"
scope: PHOEBE_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: PHOEBE_PRE_AV_V0_1
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

# Phoebe — a combat prayer is not a decree, and a shared text key is not a shared voice

The pinned `character_source_package.json` has 60 Phoebe favor-word rows. **Seven** raw IDs differ from the suffix of their actual localized `Content` key. Six form a permutation across Resonance Skill I–VI; the seventh is a nonlexical *Greeting* row whose `Content` key is also used by a Cantarella idle row. This is not a harmless uniform offset. A guessed key can return a valid *different Phoebe skill*; matching the shared text key alone can join **two different characters' sound**. Preserve `RoleId`, raw row ID, exact `favorword.json` locator, actual raw `Content`, semantic occurrence ID, title/trigger, event path/ID, language-specific bank/media and WEM/PCM/FLAC hashes as separate fields. The [validator](reproduce_validation.py) checks all 60 exact source-to-voice joins and the two cross-character rows independently.

`favorword#/N` below expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/favor/favorword.json#/N`. The key column is the actual `Content`, not a key synthesized from raw `Id`.

| Raw Phoebe ID | Actual Content key | Source row | Raw EN title | Event ID |
|---:|---|---|---|---:|
| `150632` | `FavorWord_150634_Content` | `favorword#/1929` | Resonance Skill I | `2953016277` |
| `150633` | `FavorWord_150635_Content` | `#/1930` | Resonance Skill II | `2953016278` |
| `150634` | `FavorWord_150636_Content` | `#/1931` | Resonance Skill III | `3013562366` |
| `150635` | `FavorWord_150637_Content` | `#/1932` | Resonance Skill IV | `3013562365` |
| `150636` | `FavorWord_150632_Content` | `#/1933` | Resonance Skill V | `2324455528` |
| `150637` | `FavorWord_150633_Content` | `#/1934` | Resonance Skill VI | `2324455531` |
| `150660` | `FavorWord_160719_Content` | `#/2235` | Greeting, nonlexical | `1168224278` |

The skill event paths use Phoebe's `play_favor_word_feibi_*` family. In particular, raw `150632`/Skill I points to `skill_skill02_01`, whereas raw `150636`/Skill V points to `skill_skill01_01`: neither title numbering nor key suffix can replace the row's explicit event path. The greeting is raw `RoleId: 1506`, event `play_favor_word_feibi_sys_gacha`, with four distinct PCM-valid Phoebe renders. Cantarella's raw ID `160719`, `RoleId: 1607`, at `favorword#/1976` separately uses the same `FavorWord_160719_Content` text-map entry for an *Idle I* effort sound, but its `play_favor_word_kanteleila_idle_idle01` event, semantic occurrence ID and four PCM hashes all differ. Both rows legitimately use nonlexical labels (EN “Effort sound”; JA no-line marker); the shared text key does not identify owner, gameplay function, audio bytes or a spoken sentence. A global `text_key → character voice` map would be lossy. The exact row/role/event/render chain resolves the ambiguity [PHO-E26; PHO-C20].

All **60** Phoebe archive locators join 60 complete semantic voice records, 60 explicit event IDs and **240 distinct PCM-valid four-dub objects**. The 30 combat/system rows at `favorword#/1927–1956` account for 30 of those events and 120 objects, already inside the packet's full **selected** voice corpus. These joins prove local technical mapping, not that any bark played in a dated quest scene or how it sounded to a person. The existing twelve-case metadata JSON remains a separate 12-line/48-render retrieval sample. Official-client sound is raw media authority; the frozen normalized Chinese semantic view supplies the current text/source interpretation, subject to explicit source-class limits.

## What the shorter words can and cannot carry

**Skill prayer, command and direction.** Skills I–VI at `#/1929–1934` include an invocation to descend, an order for quiet, a directional cue, a call for response and a judgment cry. These belong to combat triggers, where a devout acolyte's religious vocabulary and procedural decisiveness can coexist. They do not show Phoebe enforcing an Order rule on a civilian or choosing sedation without consent. Skill III is unusually translation-sensitive: ZH, JA and KO refer to the wind's direction or guidance, while EN says “To the Sentinel.” The English witness makes the moment more overtly devotional than the Chinese anchor; it cannot make every dub pray to a named being at that trigger. Skill IV is “over there” in ZH/EN, a near-pointing expression in JA, and directs toward a magic circle in KO. A physical magic circle or fixed target still needs runtime observation. Her dated restaurant restraint, holiday Echo apology and later invitation to nonbelievers remain stronger evidence for conduct and consent than a terse battle command [PHO-E03 E15–E16 E20 E27; PHO-C01 C08 C19].

**Help and penance are not identical four-dub motives.** Injured III at `favorword#/1945`, actual `FavorWord_150648_Content`, has ZH and KO formulations about bearing suffering to bring rescue, JA about suffering accompanying rescue, and an EN version that calls pain penitence. EN's self-punishment frame is not a neutral paraphrase of the other three. It is a localization witness worth hearing, not enough to diagnose that Phoebe seeks injury as expiation or that all protective action arises from guilt. Injured II speaks of shielding others as duty in all four; the game-state title still indicates a damage reaction, not a patient outcome. The later story herself acknowledges that cleansing corruption does not cure grief, a more concrete bound on her helping power than any bark [PHO-E21; PHO-C10 C20].

**The rescuer's imagery and a fall are not settled theology or death.** Liberation II at `#/1936` invokes light's blessing in ZH, whereas EN/JA/KO address a bluebird and salvation. The bluebird may be a meaningful localized image, but it is not present in the exact Chinese line and cannot by itself identify a witnessed animal, intermediary or new deity. Fallen III at `#/1948` offers light to another in ZH/JA/KO, while EN adds a first-person light/farewell image. This is a gameplay fall trigger, not a canonical death or final renunciation of faith. Source-linked later reform and daytime Echo friendship contradict a timeline that ends Phoebe at the fall bark. A performance account must mark the four distinct texts and exact render, not assume one scene or one intention across dubs [PHO-E17 E22; PHO-C05 C21].

## Next bounded observation

Nominate `#/1931` (wind/Sentinel), `#/1932` (direction/magic circle), `#/1933–1934` (response/judgment), `#/1936` (light/bluebird), `#/1945` (rescue/penitence), `#/1948` (fall/farewell), and `#/2235` (nonlexical Phoebe greeting). Retrieve the Cantarella `#/1976` row as a **negative identity control**, not an extra Phoebe line. For each, record the actual raw key, source locator, role, semantic occurrence, event/bank/media ID, language, render variant and hashes, then observe if and when the trigger fires. Human four-dub listening should distinguish words, breath/effort, mix and channel before labeling devotion, coercion, guilt, fear or humor. No such listening or runtime capture has yet been performed for this packet. A later source generation or direct contradictory scene would warrant a separately labeled revision rather than a silent overwrite of this frozen map.
