---
series: WUWA
artifact_type: audit
scope: WUWA_RINASCITA_CH2_SHARED_AV_V01
source_boundary: "Pinned Wuthering Waves 3.6.0 semantic commit 353f2eaed119bc9f680eab92807d20ac75a79b40, bounded 1080p60 English-dubbed Chapter II recording witness WUWA_CH2_FAYATO_1080P60_6076F127, and 107-moment (428-render) four-dub voice calibration over wuwa_voice_generation_v0_5_1; raw media and derived dataset remain restricted outside Git"
generation: V0.2
status: active_provisional
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Wuthering Waves Chapter II (*Rinascita*) — shared audiovisual examination and reconciliation audit

This audit records the bounded multi-character shared audiovisual examination and Git corpus reconciliation run `WUWA_RINASCITA_CH2_SHARED_AV_V01` over the complete recorded Chapter II (*Rinascita*: "Even When Divinity Remains Silent") main-storyline witness `WUWA_CH2_FAYATO_1080P60_6076F127`. Its machine-readable companion is [WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_MANIFEST.json](WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_MANIFEST.json), and its series-level routing home is [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md).

## 1. Witness provenance, authority split, and scope boundary

- **Primary moving-image witness (`WUWA_CH2_FAYATO_1080P60_6076F127`)**: read-only MP4 master recording (`50,518,925,664` bytes, SHA-256 `6076f1271e7a3c32b4b4d49bd5c50de23d2d2e7b1c9c9009fc4c3b3d19f1c3ed`, video duration `105,804.732367 s` / `29:23:24.732`, `1920x1080` H.264 High Profile at `60000/1001` fps across `6,341,942` frames, stereo `44,100 Hz` AAC LC audio, English voiceover + English UI/subtitles, PlayStation controller prompts, Female Rover named `Faz`, UID `709363278`, clean game audio with no commentary overlay).
- **Pinned structured semantic authority**: Arikatsu `WutheringWaves_Data` commit `353f2eaed119bc9f680eab92807d20ac75a79b40` (`zh-Hans` primary textual authority paired with official `en`, `ja`, and `ko` localization witnesses, `flowState` graphs, `MultiText`, and `Speaker_<id>_Name` bindings).
- **Restricted Drive evidence plane**: owner-authenticated Drive evidence root `19ZmRcjKQR3g0lhU1A3sXujsyihhdKs-2` (`wuwa-drive-evidence-v0.1`), retaining raw audio/video objects, contact sheets, extracted acoustic clips, and the sealed `WUWA_RINASCITA_CH2_SHARED_AV_V01` multi-character dataset outside Git.
- **Included narrative span**: Chapter II Prologue (`114000026`, *Through the Sea Thou Break*) continuously through Chapter II Act XI (`158800019`, *Dawn Breaks on Dark Tides*), covering Patches `2.0`, `2.2`, `2.4`, `2.5`, `2.6`, and `2.7` first-half main story (`0.0 s`–`105,804.732367 s`, `100.0%` inspected).
- **Explicitly excluded from this recording witness**:
  - Chapter II Segue *A Stranger in a Strange Land* (`175000000` / `936800000`, Patch `2.7` second-half Qiuyuan Segue) and Patch `2.8` Honami arcs;
  - Chapter I Huanglong / Mt. Firmament / Black Shores main-story quests (`121800001`–`121800005`, `125900000`, `145000004`);
  - Companion Story Quests (`114000018`, `106000005`, `122000009`, `880000033`, `155000000`, `158800014`, `121000035`), Side/Exploration Quests, and Limited/Permanent Events;
  - Character Menu / `FavorWord` / `FavorStory` / Forte / Ascension / overworld ecology animations outside active main-quest play;
  - Full-census human listening across every client voice line outside the calibrated `107`-moment (`428`-render) four-dub cohort documented in [WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md](WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md) (the master video witness itself carries the `en` dub track only).
- **Five-layer epistemic discipline**: every observation separates (1) direct 1080p60 visual staging/camera/gesture observation, (2) English-dub vocal and scene-audio delivery, (3) four-locale textual witness (`zh-Hans` anchor + `en`/`ja`/`ko`), (4) machine acoustic signal measurements (`f0_median`, `f0_iqr`, `rms_dbfs`, pause counts), and (5) bounded analytical inference.
- **Strict authority-state preservation**: owner-adopted [WUWA_CARTETHYIA_CURRENT_STATE.md](../04%20Character%20Analysis/Cartethyia/WUWA_CARTETHYIA_CURRENT_STATE.md) and its updated Cartethyia crosswalk/prior-generation revision ledger remain `active_provisional` / `canonical` (`do_not_use_as_current_authority: false`), while Cartethyia's imported V0.2 `WUWA_CARTETHYIA_CLAIM_REVISION_LEDGER.md` remains byte-untouched as a historical baseline record. All eleven reconciled `draft_noncurrent` character packets (`Augusta`, `Brant`, `Cantarella`, `Changli`, `Iuno`, `Jinhsi`, `Phoebe`, `Qiuyuan`, `Shorekeeper`, `Yinlin`, `Zani`) retain `status: draft_noncurrent` and `do_not_use_as_current_authority: true` byte-for-byte; audiovisual reconciliation does not constitute owner adoption.

## 2. Validated dataset and 13-segment Chapter II coverage

The restricted evidence run `WUWA_RINASCITA_CH2_SHARED_AV_V01` (`CKPT-014-FOUR-DUB-CALIBRATED`) passed automated referential, monotonicity, orphan, authority-veto, four-dub render/PCM-hash, multichannel `FC(ch=2)` LFE-exclusion, and SHA-256 verification with `0` errors across all `13` dataset control/ledger/voice files and `27` Markdown character evidence capsules:

| Dataset artifact (restricted evidence plane) | Records / count | Bytes | SHA-256 |
|---|---:|---:|---|
| `manifests/source_manifest.json` | `1` master + `5` supplemental descriptors | `5,293` | `f6d9fc14954b7774ac8cd9a1e745fec7cdeb0f00a333805b8eabe1009c633c89` |
| `manifests/checkpoint_manifest.json` | `CKPT-014-FOUR-DUB-CALIBRATED` (`0` errors) | `4,332` | `54c72c69b60e116c71cf0746115bbf692b53c2651de930e380695dcffe07a052` |
| `manifests/segment_manifest.jsonl` | `13` segments (`SEG-001`–`SEG-013`) | `14,963` | `0fdc42b4d933251104955a22f7c305ff586ce747f9c5e3a34081606a2ade3c02` |
| `manifests/character_authority_and_av_inventory.json` | `18` packet inventories (`483` crosswalk rows) | `63,997` | `b1ae5c714db57a3badba01e3b12fd148384bd3dfb74c20d27212c8cad13e4507` |
| `scenes/scene_index.jsonl` | `345` continuous scenes (`SCN-0001`–`SCN-0345`) | `503,094` | `0ae18b6e714065724e2fe21e89cf6dadb0a5e0addb98c7e42258211ad87ce47c` |
| `dialogue/dialogue_turns.jsonl` | `9,862` executed turns | `15,758,235` | `3e39d72259502d36935dfe49f516aa8c6fb044b79908e311047caa520e2e6b53` |
| `observations/av_observations.jsonl` | `348` five-layer AV observations | `817,461` | `81e924bf634dbe1061650a0a35a0a6ef44b09d304263ba8ff533339cf13a741a` |
| `index/character_evidence_index.json` | `373` entities (`0` orphans) | `971,324` | `fab0781df1fc87346b7729d7e0ed4b40c39b66b2476a75990c0231f70a16a367` |
| `capsules/character_evidence_capsules_index.jsonl` | `27` Markdown evidence capsules (with 4-dub calibration) | `14,778` | `33bbb564929f80859cd2f9b4382c2dd3aef7a2a8b25ff5813038564218619646` |
| `manifests/av_target_crosswalk.jsonl` | `483` dispositioned targets (`0` queued) | `598,085` | `5d1f0f9340894504ffe27bb29351c9a3c553333751f6fa0e67f1d5942707dd1a` |
| `manifests/coverage_and_gaps.json` | `100.0%` video coverage + 4-dub calibration & gap ledger | `518,167` | `fc4c20a6fcaa2064b49a6de4f418d9bc3bd50cf7521a87c33115cdd1044f591c` |
| `reconciliation/analysis_reconciliation_queue.jsonl` | `142` reconciliation items (`132` video + `10` four-dub) | `172,532` | `792c211b3a7db7955c0f03bace44320fb0703444dd95397f54dfc7277395cab2` |
| `voice/four_dub_cohort_manifest.json` | `107` moments / `428` renders (`0` shared PCM) | `12,885` | `91e1d7c883ec90eeba57f608fd438567a349dc011541f24e7815cff6af3b1d14` |
| `voice/four_dub_listening_annotations.jsonl` | `107` four-dub ear-listened records (`428` renders) | `675,237` | `4d41840de3f308a37cf6e8da688bda6e20b54768ed2985a8a5590446daa5bb2e` |

### Chapter II 13-segment runtime partition

| Segment | Chapter II unit | Patch | Quest IDs | Master range (`s`) | Master `HH:MM:SS.mmm` | Scenes | Turns | AV obs |
|---|---|---:|---|---|---|---:|---:|---:|
| `SEG-001` | Prologue: *Through the Sea Thou Break* | `2.0` | `114000026` | `0.0`–`1878.0` | `00:00:00.000`–`00:31:18.000` | `11` | `197` | `24` |
| `SEG-002` | Act I: *The Sacred Breeze So Often Breathes* | `2.0` | `114000027` | `1878.0`–`5372.0` | `00:31:18.000`–`01:29:32.000` | `15` | `368` | `22` |
| `SEG-003` | Act II: *Veils Off in Sun or Shadow* | `2.0` | `114000028`, `114000030` | `5372.0`–`13703.0` | `01:29:32.000`–`03:48:23.000` | `26` | `742` | `28` |
| `SEG-004` | Act III: *What Yesterday Wept, Today Doth Sing* | `2.0` | `114000030`, `140000011`, `114000029` | `13703.0`–`22682.0` | `03:48:23.000`–`06:18:02.000` | `22` | `739` | `30` |
| `SEG-005` | Act IV: *The Maiden, The Defier, The Death Crier* | `2.2` | `114000029`, `145000005` | `22682.0`–`34637.0` | `06:18:02.000`–`09:37:17.000` | `28` | `1,152` | `36` |
| `SEG-006` | Act V: *Shadow of Glory* | `2.4` | `125000125`, `125000126` | `34637.0`–`43300.0` | `09:37:17.000`–`12:01:40.000` | `30` | `753` | `28` |
| `SEG-007` | Act VI: *Flames of Heart* | `2.4` | `121000038` | `43300.0`–`48974.0` | `12:01:40.000`–`13:36:14.000` | `22` | `493` | `24` |
| `SEG-008` | Act VII: *Dreamcatchers in the Secret Gardens* | `2.5` | `171000004` | `48974.0`–`59474.0` | `13:36:14.000`–`16:31:14.000` | `27` | `962` | `28` |
| `SEG-009` | Overture/Segue: *Rust, Sword and the Sun* | `2.6` | `164000000` | `59474.0`–`63128.0` | `16:31:14.000`–`17:32:08.000` | `9` | `466` | `16` |
| `SEG-010` | Act VIII: *By Sun's Burning Hand* | `2.6` | `311000001`, `311000002` | `63128.0`–`75405.0` | `17:32:08.000`–`20:56:45.000` | `69` | `1,194` | `26` |
| `SEG-011` | Act IX: *By Moon's Fated Light* | `2.6` | `886000001` | `75405.0`–`84500.0` | `20:56:45.000`–`23:28:20.000` | `30` | `848` | `28` |
| `SEG-012` | Act X: *The Bygone Shall Always Return* | `2.7` | `168000001` | `84500.0`–`91075.0` | `23:28:20.000`–`25:17:55.000` | `24` | `614` | `26` |
| `SEG-013` | Act XI: *Dawn Breaks on Dark Tides* | `2.7` | `158800019` | `91075.0`–`105804.732367` | `25:17:55.000`–`29:23:24.732` | `32` | `1,334` | `32` |
| **Total** | **Chapter II Prologue – Act XI** | **`2.0`–`2.7`** | **18 main-story quests** | **`0.0`–`105804.732367`** | **`29:23:24.732`** | **`345`** | **`9,862`** | **`348`** |

## 3. Universal entity hygiene, speaker disambiguation, and avatar separation

`index/character_evidence_index.json` indexes **373 distinct entities** across Chapter II with `0` unindexed speakers or scene orphans: `42` `char:*` keys, `62` `echo:*` keys, `34` `ent:*` keys, `220` `npc:*` keys, `12` `td:*` keys, and `3` `sys:*` keys. Runtime verification enforces two hygiene controls across all downstream character ledgers:

1. **Counterpart, disguise, and possession speaker disambiguation**:
   - **Leviathan vs. Cartethyia**: `who=1626` (`Cartethyia?` in `SEG-012` `SCN-0313` and `SEG-013` `SCN-0337`–`0338`) and `who=1647` (`Threnodian: Leviathan` in `SCN-0338`–`0339`) route to `ent:leviathan` (`f0_median = 197.5 Hz`–`200.0 Hz` hollow contralto), never to `char:cartethyia` (`who=50074`, `228.6 Hz`–`275.9 Hz`), Cartethyia's frequency channel (`who=800343` / `1595`), or the Cartethyia+Galbrena unison pact (`who=1633`, `224.3 Hz`).
   - **Chaos remnant vs. living Iuno**: bleached Chaos remnant `"Iuno"` (`who=350026`, `f0_median = 228.6 Hz`, `rms = -22.95 dBFS`, `14` pauses in `SEG-011` `SCN-0270`) is tracked explicitly across its reintegration into restored `Iuno` (`who=250024`), while Gladiator Harelius's `124.4 Hz` plea is kept separate from Iuno's `289.2 Hz` response in `IUN-AV-12`.
   - **Past vs. present Rover**: `who=178` (`???`) -> `50077` (`"Rover" of the Past` in `SEG-001` `SCN-0002` and `SEG-008` `SCN-0175`–`0177`) routes to `char:rover_of_the_past`, closing Shorekeeper negative-control check `SHK-R07` and distinguishing pre-amnesia Arbiter choices from present-day Female Rover `Faz` (`char:rover_female`, `2,087` turns).
   - **Fractsidus disguises**: `Triss` (`who=300023`), `Devoted Watcher` (`who=300040` in `SEG-008`), and Styx ferryman `Kharon (Schwarzloch)` (`who=1560`/`1562` in `SEG-013` `SCN-0316`, `SCN-0322`, `SCN-0345`) are unmasked in-scene as `ent:grand_architect`; blind barefoot poet `Nestor` (`npc:nestor` in `SEG-009` `SCN-0188`) dissolves into white origami birds as `char:cristoforo`.
   - **Mya, Angel, and Fenrico**: human gladiator `npc:mya` is separated from Threnodian hybrid `npc:lady_of_the_sea` (`SEG-006`–`SEG-007`); childhood `npc:angel` (`SEG-010`) and `Girl Who Fell Into The Dark TIde` (`who=800332`, `SEG-012`) are unified by explicit Act XI self-disclosure (`flow#/9961`, `SCN-0328`) with `char:galbrena`; boss `Fenrico: Deliverance in the Deep` and redeemed spirit `who=50076` (`SCN-0341`) route to `ent:primus_fenrico` while Tidespawn mimic `False Fenrico` (`SEG-012`) routes to `td:*`.
2. **Non-diegetic avatar, Convene, and outro isolation**:
   - Player overworld/combat party avatars (`char:cartethyia_avatar`, `char:phoebe_avatar`, `char:changli_avatar`, `char:shorekeeper_avatar`, `char:zani_avatar`, `char:phrolova_avatar`, `char:camellya_avatar`, `char:xiangli_yao_avatar`, `char:zhezhi_avatar`), mid-recording Convene pull `char:jianxin_convene` (`SCN-0081`), and closing illustration `char:rover_male` (`105,786`–`105,804.732 s`) are strictly isolated from diegetic character presence and turn counts.

## 4. Complete 483-target crosswalk disposition across 16 character packets

All `483` nominated crosswalk rows across the `16` character packets carrying human-retrieval crosswalk tables (`0` remaining queued) were dispositioned against `WUWA_CH2_FAYATO_1080P60_6076F127`:

| Character | Git packet status | Authority veto (`do_not_use`) | Total targets | `inspected_resolved` | `not_triggered_optional_in_recording` | `out_of_scope_non_main_story` | `out_of_recording_scope` |
|---|---|---|---:|---:|---:|---:|---:|
| [Cartethyia](../04%20Character%20Analysis/Cartethyia/03%20Audiovisual%20and%20Voice/WUWA_CARTETHYIA_AV_HUMAN_RETRIEVAL_CROSSWALK.md) | `active_provisional` | `false` | `33` | `27` | `3` | `3` | `0` |
| Iuno | `draft_noncurrent` | `true` | `39` | `21` | `4` | `0` | `14` |
| Augusta | `draft_noncurrent` | `true` | `32` | `19` | `0` | `1` | `12` |
| Phoebe | `draft_noncurrent` | `true` | `24` | `7` | `1` | `9` | `7` |
| Brant | `draft_noncurrent` | `true` | `38` | `5` | `3` | `0` | `30` |
| Qiuyuan | `draft_noncurrent` | `true` | `27` | `5` | `0` | `0` | `22` |
| Cantarella | `draft_noncurrent` | `true` | `36` | `4` | `1` | `3` | `28` |
| Shorekeeper | `draft_noncurrent` | `true` | `14` | `2` | `0` | `0` | `12` |
| Zani | `draft_noncurrent` | `true` | `12` | `2` | `1` | `6` | `3` |
| Aemeath | `active_provisional` | `false` | `41` | `0` | `0` | `0` | `41` |
| Changli | `draft_noncurrent` | `true` | `39` | `0` | `0` | `0` | `39` |
| Jinhsi | `draft_noncurrent` | `true` | `35` | `0` | `0` | `0` | `35` |
| Yinlin | `draft_noncurrent` | `true` | `33` | `0` | `0` | `0` | `33` |
| Luuk Herssen | `draft_noncurrent` | `true` | `31` | `0` | `0` | `0` | `31` |
| Chisa | `active_provisional` | `false` | `25` | `0` | `0` | `0` | `25` |
| Sigrika | `active_provisional` | `false` | `24` | `0` | `0` | `0` | `24` |
| **Total (16 crosswalks)** | — | — | **`483`** | **`92`** | **`13`** | **`22`** | **`356`** |

`Denia` and `Lynae` (`active_provisional`) carry pre-AV nomination plans without `AV_HUMAN_RETRIEVAL_CROSSWALK.md` tables and have zero Chapter II main-story presence (`out_of_recording_scope`). `Aemeath`, `Chisa`, `Sigrika`, and `Luuk Herssen` likewise have `100%` `out_of_recording_scope` target sets and required zero packet-file edits. `Changli`, `Jinhsi`, and `Yinlin` (`draft_noncurrent`) have `100%` `out_of_recording_scope` crosswalk targets (`0` executed Chapter II main-story turns) and received targeted crosswalk reconciliation notes documenting Chapter II cross-references (`Changli` Mingting informant note in `SCN-0085`; `Jinhsi` Second Awakening benchmark in `SCN-0084` and memory projection/regards in `SCN-0322`, `SCN-0332`), non-diegetic `char:changli_avatar` separation, and `Yinlin`'s Companion Story scope boundary.

## 5. Key Chapter II runtime audiovisual, branch, and English-dub signal findings

- **Cartethyia (`active_provisional`, `27/33` resolved; see [WUWA_CARTETHYIA_AV_HUMAN_RETRIEVAL_CROSSWALK.md](../04%20Character%20Analysis/Cartethyia/03%20Audiovisual%20and%20Voice/WUWA_CARTETHYIA_AV_HUMAN_RETRIEVAL_CROSSWALK.md) and [WUWA_CARTETHYIA_PRIOR_GENERATION_CLAIM_REVISION_LEDGER.md](../04%20Character%20Analysis/Cartethyia/04%20Validation%20and%20Readiness/WUWA_CARTETHYIA_PRIOR_GENERATION_CLAIM_REVISION_LEDGER.md))**: resolves `AV01` (`Fl...` -> `Cartethyia` self-naming and canal water dance), all ten previously viewer-unavailable `V03_CLIP_A`–`V03_CLIP_J` anchors and `AV03`–`AV12` across Avinoleum (`Fleurdelys` cold royal contralto `205.2 Hz` vs. revived `Cartethyia` `246.2 Hz`), `AV15` (firm `198.3 Hz` `'No.'` refusing Lupa's surrender plea alongside peer-warmth combat partnership), `AV16` (passive Dark Tide frequency absorption and self-stabilization reflex), rescued `AV19` (post-collapse Fisalia shelter and `228.6 Hz` feathered-pendant trust line), and Act XI `AV20`–`AV22` (`224.3 Hz` Galbrena unison pact, `M0308` staged lethal strike, Leviathan `197.5 Hz` vs. Cartethyia `275.9 Hz` separation, and Ragunna Harbor humanistic faith reframing with Phoebe). Logs `AV02` (padlocked Rinascita dish option), `AV14`, and `AV18` honestly as `not_triggered_optional_in_recording`.
- **Iuno (`draft_noncurrent`, `21/39` resolved)**: resolves `IUN-R10` (purely divinatory Silva banishment proclamation, `230.8 Hz`, left-instep star-cross Tacet Mark), all five Act VIII targets including audible EN coughs on `IUN-R15` (`350_14`, omitted in printed EN text), rescues `IUN-R13` (`flow#/7761/5`) as an executed Act IX main-story scene (`SCN-0272`), quantifies Chaos remnant `"Iuno"` (`228.6 Hz`, `-22.95 dBFS`) vs. reawakened `Iuno` (`255.3 Hz`–`289.2 Hz`) and post-return wry confession (`150.9 Hz`), and confirms via Act XI `SCN-0317` that Septimont's public memories of her remained unrestored (`4` optional branches `IUN-AV-18/19`, `IUN-R06`, `IUN-R08` logged untriggered).
- **Augusta (`draft_noncurrent`, `19/32` resolved)**: resolves the pre-AV visual question on `AUG-R10` (`MAIN_RYAM_44_23`: sky-serpent projects three giant holographic bribery photographs), captures the unbroken high-angle overhead Senate Hall rebuke (`AUG-R02`) vs. sunset Palace roof intimacy and `-22.63 dBFS` fond chuckle (`AUG-AV-12`), proves `flow#/8416` (`530_4`, `'Ragunna's "Divinity" didn't get a seat on the ship'`) is **fully voiced in runtime EN audio** despite missing pre-AV voice-index linkage, confirms negative visual control on Angel's Oak Hollow fate (`AUG-R07`), anchors lived chronology (`flow#/7804` three-plus years before `flow#/7741`, `AUG-R03`), and verifies post-erasure re-befriending of Iuno without restored memory.
- **Phoebe, Cantarella, Brant, Qiuyuan, Shorekeeper, and Zani (`draft_noncurrent`)**:
  - **Phoebe (`7/24` resolved)**: verifies non-coercive customs admonition and two-stage hat-brim duck (`PHO-AV-06`, `PHO-R06`), moral outrage at Echo corruption and wordless *Aria* prayer (`PHO-AV-07`–`09`), Thessaleo Fells coalition with Cantarella (`SCN-0309`), and post-Leviathan personal blessing `'not as an Acolyte of the Order, but in my own name'` (`PHO-R11`, `PHO-AV-12`).
  - **Cantarella (`4/36` resolved)**: verifies nonlethal hallucinatory disarmament of Gilberto and `'Banquet'` trauma reframing (`CAN-R12`), Imperator's direct confirmation of her voluntary Second Awakening return (`CAN-R09`), Female-Rover `'Fisalia Head's consort'` parity (`CAN-R10`), Act V eternal-ally hologram, Act X sheltering of Cartethyia and Thessaleo shotgun restraint, and Act XI Fisalia vial ownership + mass coalition potion synthesis (`CAN-R08`).
  - **Brant (`5/38` resolved)**: verifies three-beat Prologue Cetus architecture (`BRA-R01`, `BRA-AV-07`), Act III civic-freedom credo (`BRA-AV-12`) and *Commedia Improvviso* control (`BRA-R03`), and Act X `-50.0 Hz` shift from rainy street-play verse (`206.9 Hz`) to sober evacuation synthesis (`156.9 Hz`, `BRA-R13`), with Fool's Elysium optional talk (`BRA-AV-08/09`, `BRA-R02`) logged untriggered.
  - **Qiuyuan (`5/27` resolved)**: indexes his complete Act XI Chapter II main-story debut (`QIU-AV-09`–`11`, `QIU-R04`–`05`: Napoli II lantern handoff, Fenrico counsel and Jinzhou Magistrate regards at `123.7 Hz`, lethal intercept against `Scar: Aberrant Nightmare`, and bamboo-flute coalition rescue) while keeping his remaining `22` targets (`15` Patch `2.7` Segue / coda `175000000` / `936800000` targets plus `7` archive / combat-trigger / `ShortMessage` targets) explicitly `out_of_recording_scope`.
  - **Shorekeeper (`2/14` resolved) & Zani (`2/12` resolved)**: closes `SHK-R07` (`"Rover" of the Past` holographic visual/vocal proof) and `SHK-R05` (clinical Tethys hypothesis framing + solo grand-piano continuity + Act XI astral butterfly & sanctum memory projection); resolves `ZAN-R01` and `ZAN-R12` (hospitality-to-candor shift, collar-touch sigh, Masked Reverie undercover restraint, Carnevale and Averardo Vault evacuations).

## 6. Unmodeled Chapter II cast and institutional evidence capsules (27 capsules)

To prevent unmodeled Chapter II speakers and factions from disappearing between character-scoped packets, `WUWA_RINASCITA_CH2_SHARED_AV_V01` maintains `27` longitudinal Markdown capsules (`605`–`2,087`-turn leads down to single-scene coalition cameos):

- **Protagonist & Threnodian-linked core (`4` capsules)**: `CAPS-ROVER-FEMALE-CH2` (`Faz` vs. `"Rover" of the Past` moral divergence on collateral sacrifice and `'Even when Divinity remains silent, humanity will always speak through action!'`); `CAPS-ABBY-CH2` (frequency sickness, Avinoleum split-energy harmonization, Chaos memory-erasure immunity via shared Tacet Mark, and Act XI Leviathan recognition of **`Abraxas`** alongside dormant **`Ovathrax`** in Jinzhou); `CAPS-GALBRENA-CH2` & `CAPS-ANGEL-AND-FABIANUM-CH2` (`Galbrena`'s birth identity as Augusta's childhood friend `Angel`, `C0021` Flame Demon conquest, Nemean `Chimera` pact, absorbed TDs, `M0308` purifying blood-flames, and Overclock rescue).
- **Fractsidus Overseers & metaphysical antagonists (`4` capsules)**: `CAPS-LOST-BEYOND-AND-FABRICATORIUM-CH2` (`Grand Architect` across `Triss`, `Devoted Watcher`, and `Kharon`, closing with the post-credits **`Lahai-Roi`** `"Waystones"` hook); `CAPS-CRISTOFORO-CH2` (`Nestor` origami reveal, reality-weaving constraint requiring real historical tragedies and existing roles, Avidius authorship, Gem seizure, and residual Leviathan power escape); `CAPS-PHROLOVA-CH2` (Ostina meteorite trauma, half-TD physiology, `Rover of the Past` concert promise, Lost Beyond homecoming, and Act XI departure from the Fractsidus); `CAPS-SCAR-CH2` (`M0277` silent Rinascita cameo, voiced Jinzhou `Ovathrax` flashback, and Act XI `Aberrant Nightmare` ambush).
- **Rinascita & cross-regional allies and institutions (`12` capsules)**: `CAPS-CARLOTTA-MONTELLI-CH2`, `CAPS-ROCCIA-AND-PERO-CH2`, `CAPS-CIACCONA-CH2`, `CAPS-LUPA-CH2`, `CAPS-BULING-CH2`, `CAPS-LORELEI-AND-NIMBUS-SANCTUM-CH2`, `CAPS-AALTO-CH2`, `CAPS-AVIDIUS-CH2`, `CAPS-ORDER-OF-THE-DEEP-AND-FENRICO-CH2` (`Primus Fenrico` & `Napoli II`), `CAPS-ACT4-AVINOLEUM-AND-FISALIA-ESTATE-CH2` (`Imperator` hippocampus form, single-Resonator law, and `Genesis Scroll` dissolution), `CAPS-ACT5-SEPTIMONT-AGON-AND-MYA-CH2`, and `CAPS-ACT11-FINALE-COALITION-AND-PARADISE-CH2` (Black Shores cross-sea reinforcements `Calcharo`, `Camellya`, `Encore`, and `Youhu`).
- **Act-level civic, sanctuary, and regional ensemble capsules (`7` capsules; `4 + 4 + 12 + 7 = 27` total)**: `CAPS-PROLOGUE-NPCS-AND-ECHOES` (`SEG-001` Prologue civic figures, Echoes, and preview voices), `CAPS-ACT1-RAGUNNA-CITIZENS-AND-ECHOES` (`SEG-002`, `SEG-004` Ragunna artisans including `Fulmine` and partner Echoes), `CAPS-ACT2-VAULT-AND-WHISPERWIND-NPCS-ECHOES` (`SEG-003` Montelli hierarchy and Averardo Vault staff/traitors), `CAPS-ACT3-PENITENTS-END-AND-FOOLS-TROUPE-CH2` (`SEG-001`, `SEG-004` Penitent's End castaways, Fool's Elysium crew, and Sonoro boss `Hecate`), `CAPS-SEGUE-BLAZING-SUN-AND-SENATE-CH2` (`SEG-009`–`SEG-011` blind poet `Nestor`, Epic of the Blazing Sun figures, Grandmother `Lillibet`, and Septimont Senate elders), `CAPS-ACT9-CHAOS-AND-SEPTIMONT-CH2` (`SEG-011` Bow-Forging Blacksmith, `Sibylla`, Cassos squad, and Hunter's Den cast), and `CAPS-ACT10-RAGUNNA-DARK-TIDE-AND-CAPSULE-CH2` (`SEG-012` Ragunna evacuees, Tidespawn mimics `False Fenrico` / `Scared Girl`, Genesis Scroll voices, and Thessaleo defenders).

## 7. Residual scope boundaries and open follow-up

1. **Stratified four-dub calibration completed (`107` moments / `428` renders); full-census human listening remains open**: [WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md](WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md) completes direct ear listening across `zh-Hans`, `ja`, `ko`, and `en` on `29` `Cartethyia` moments, `48` moments across the `8` Chapter II `draft_noncurrent` packets (`Augusta`, `Iuno`, `Phoebe`, `Brant`, `Cantarella`, `Qiuyuan`, `Shorekeeper`, `Zani`), and `30` moments across `19` unmodeled Chapter II subjects (resolving the `5.1` `LFE` `ch=3` subwoofer F0 trap on `FEN-DUB-02` and `LEV-DUB-01`, Phoebe's `FavorWord_150609` spoken `en` sour-berry punchline, Iuno's `350_14` 4-dub coughs and `7764/3` bandpass-vs-dry speaker split, and Augusta's `flow#/8416` `PlayVoice=false` 4-dub check). Exhaustive human listening across all remaining client voice lines (`757/786` Cartethyia lines, `837/845` Augusta lines, and non-Chapter-II packets) remains open.
2. **Untriggered optional branches (`13` crosswalk items)** — `Cartethyia` (`AV02`, `AV14`, `AV18`), `Iuno` (`IUN-AV-18`, `IUN-AV-19`, `IUN-R06`, `IUN-R08`), `Brant` (`BRA-AV-08`, `BRA-AV-09`, `BRA-R02`), `Cantarella` (`CAN-AV-11`), `Phoebe` (`PHO-R08`), and `Zani` (`ZAN-R06`) — remain open for targeted branch capture rather than extrapolated from text alone.
3. **Out-of-recording story and non-main-story scopes (`356 + 22 = 378` crosswalk items)** — including Patch `2.7` Segue *A Stranger in a Strange Land* and its coda (`175000000` / `936800000`, accounting for `15` of `Qiuyuan`'s `22` `out_of_recording_scope` targets alongside his `7` archive/combat/`ShortMessage` items), Patch `2.8` Honami (`Shorekeeper` `SHK-R12/R13`, `Chisa`), Chapter I Huanglong / Mt. Firmament / Black Shores (`Changli`, `Jinhsi`, `Shorekeeper`), `3.x` packets (`Aemeath`, `Denia`, `Luuk Herssen`, `Lynae`, `Sigrika`), Companion Stories (`Cantarella`, `Zani`, `Phoebe`, `Brant`, `Yinlin`, `Ciaccona`, `Carlotta`), Limited Events, and Menu/Archive items — remain unchanged in scope and pending their dedicated media witnesses.
