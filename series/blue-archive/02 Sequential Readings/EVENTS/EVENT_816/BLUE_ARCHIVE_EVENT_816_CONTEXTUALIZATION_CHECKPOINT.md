---
series: BLUE_ARCHIVE
artifact_type: arc_contextualization_checkpoint
scope: EVENT_816 complete source package and bounded social context
generation: V1
source_story_ids: ["BA:event:816:001", "BA:event:816:002", "BA:event:816:003", "BA:event:816:004", "BA:event:816:005", "BA:event:816:006", "BA:event:816:007", "BA:event:816:008", "BA:event:816:009", "BA:event:816:010", "BA:event:816:011", "BA:event:816:012", "BA:event:816:013", "BA:event:816:014", "BA:event:816:015", "BA:event:816:016", "BA:event:816:017"]
version: "1.0"
status: canonical
source_boundary: "Complete Japanese BA:event:816:001–017, electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, game v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1, corpus BA_REFRESH_20260928T032248159554Z; text only; no main-story timeline placement"
source_reading_state: COMPLETE
supplemental_admission_state: ADMIT_WITH_LIMITS
analytical_priority_proposal: CORE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Blue Archive EVENT 816 contextualization checkpoint

## 0 Purpose and proposed admission

All seventeen canonical story objects in EVENT_816 have been read completely and have individual source-facing deep readings. This checkpoint proposes their bounded admission for Kazusa and Reisa's contested relation, the Sweets Club's ordinary pleasures and imperfect care, Suzumi's voluntary patrol context, Sensei's assistance and errors, and attested written Japanese. It does not establish event placement against main, a whole-character portrait, a performed voice, a legal or health outcome, or completion of Phase 2.

**Proposed priority: CORE for Kazusa, Reisa and the Sweets Club; HIGH for Suzumi's institutional and interpersonal comparison.** Omitting the quiet E016 café memory would erase the positive ordinary desire behind Kazusa's earlier change. Omitting E017's food ordering and renewed friction would produce an artificially complete cure. The packet's value is therefore partly intrinsic ordinary characterization and partly event-local development, not a stakes score. The integrator accepted this packet with limits in [Phase 2 cycle 001](../../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md). Its exact source admission, seven-ledger effects and coverage/readiness decision are synchronized there. The proposals below preserve the contributing reader's recommendations; the cycle owns final acceptance.

## 1 Complete inspection and provenance

The source generation is `BA_REFRESH_20260928T032248159554Z`, with Japanese witness `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`. All seventeen story records route to `DB/ScenarioScriptExcelTable1.json`; its SHA256 is `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`, verified against the retained raw snapshot. The source manifest records the raw snapshot as `corpus/01_RAW_UPSTREAM/electricgoat_ba-data/a038020f1f5ac02dcfe76962426d38f86414cdd8`.

Each canonical path is `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_<NNN>_<raw group>.md` relative to the pinned generation. The following receipt records all **17 scenes, 969 numbered utterance/control units, 67 choice groups and 1,656 raw records**. A “unit” includes narration/control rather than implying every unit is spoken dialogue. Each table link opens the corresponding analytical reading; each reading states the source title or its absence, exact route, narrative argument and local limits.

| Story ID | Raw group | Units | Choice groups | Source-facing reading |
|---|---:|---:|---:|---|
| `BA:event:816:001` | 10014005 | 30 | 3 | [Episode 001](BLUE_ARCHIVE_EVENT_816_EPISODE_001_DEEP_READING.md) |
| `BA:event:816:002` | 10014010 | 34 | 1 | [Episode 002](BLUE_ARCHIVE_EVENT_816_EPISODE_002_DEEP_READING.md) |
| `BA:event:816:003` | 10014015 | 43 | 1 | [Episode 003](BLUE_ARCHIVE_EVENT_816_EPISODE_003_DEEP_READING.md) |
| `BA:event:816:004` | 10014020 | 85 | 6 | [Episode 004](BLUE_ARCHIVE_EVENT_816_EPISODE_004_DEEP_READING.md) |
| `BA:event:816:005` | 10014025 | 83 | 8 | [Episode 005](BLUE_ARCHIVE_EVENT_816_EPISODE_005_DEEP_READING.md) |
| `BA:event:816:006` | 10014030 | 73 | 7 | [Episode 006](BLUE_ARCHIVE_EVENT_816_EPISODE_006_DEEP_READING.md) |
| `BA:event:816:007` | 10014035 | 67 | 7 | [Episode 007](BLUE_ARCHIVE_EVENT_816_EPISODE_007_DEEP_READING.md) |
| `BA:event:816:008` | 10014040 | 87 | 4 | [Episode 008](BLUE_ARCHIVE_EVENT_816_EPISODE_008_DEEP_READING.md) |
| `BA:event:816:009` | 10014045 | 53 | 2 | [Episode 009](BLUE_ARCHIVE_EVENT_816_EPISODE_009_DEEP_READING.md) |
| `BA:event:816:010` | 10014050 | 56 | 5 | [Episode 010](BLUE_ARCHIVE_EVENT_816_EPISODE_010_DEEP_READING.md) |
| `BA:event:816:011` | 10014055 | 39 | 3 | [Episode 011](BLUE_ARCHIVE_EVENT_816_EPISODE_011_DEEP_READING.md) |
| `BA:event:816:012` | 10014060 | 46 | 3 | [Episode 012](BLUE_ARCHIVE_EVENT_816_EPISODE_012_DEEP_READING.md) |
| `BA:event:816:013` | 10014065 | 38 | 3 | [Episode 013](BLUE_ARCHIVE_EVENT_816_EPISODE_013_DEEP_READING.md) |
| `BA:event:816:014` | 10014070 | 80 | 3 | [Episode 014](BLUE_ARCHIVE_EVENT_816_EPISODE_014_DEEP_READING.md) |
| `BA:event:816:015` | 10014075 | 51 | 4 | [Episode 015](BLUE_ARCHIVE_EVENT_816_EPISODE_015_DEEP_READING.md) |
| `BA:event:816:016` | 10014080 | 56 | 4 | [Episode 016](BLUE_ARCHIVE_EVENT_816_EPISODE_016_DEEP_READING.md) |
| `BA:event:816:017` | 10014085 | 48 | 3 | [Episode 017](BLUE_ARCHIVE_EVENT_816_EPISODE_017_DEEP_READING.md) |

For exact evidence, prepend the story ID and `:scene:001:` to abbreviated unit/choice IDs. The route is canonical story → `03_STRUCTURED_DATA/utterances.jsonl` or `choices.jsonl` → `source_record_key` and raw group → raw table/commit. The example `BA:event:816:005:scene:001:u:0019` routes to `ScenarioScriptExcelTable1.json:DataList[279649]`. Its structured raw label is `레이사` and Japanese label `レイサ`; its self-addressing content is already contradictory in that record. Do not silently fix it in analysis.

E015 contains 51 actual units with nonmonotonic IDs: `u:0052` occupies the position after `u:0004`, and `u:0053` after `u:0007`; there are no `u:0005` or `u:0008`. No text was skipped because of that identifier irregularity.

## 2 Documentary order and story chronology

All seventeen records have one event context, content/original content ID 816, documentary order 1–17, and release metadata `2022-08-24 11:00:00` to `2022-09-07 10:59:59`. The metadata flags recollection, omnibus and return false. These facts identify the source package, not its story-world date. The global release table's chronology confidence remains `unresolved`.

| Narrative relation | Evidence | Permitted conclusion |
|---|---|---|
| Consultation → chase → disclosure → Suzumi enquiry | E001–005 connected dialogue/action | Event-local sequence; no date against a main arc |
| Earlier club encounter recalled as yesterday | `BA:event:816:006:scene:001:u:0023–0025` | Relative recalled encounter; do not force it to be the printed E002 chase |
| That evening, then following day | E007 `u:0001`; E008 `u:0001` | Relative local day change |
| Overheard refusal → Reisa consultation → protective withdrawal | E009 `u:0042–0053`; E010 `u:0008–0012`; E011 `u:0021–0032` | Event-local change in Reisa's choice and self-account |
| Late visit and night rescue → following-day reflection | E012 `u:0021–0022`; E013 `u:0007`; E014 `u:0015–0016`; E016 `u:0001` | Relative order; no exact calendar duration or verified police timetable |
| Earlier inspiration → gradual imitation → present reflection | E016 `u:0036–0049` | Reported prior cause, newly revealed here; exact school-year/date remains unprinted |
| Reflection → return to club with renewed challenge | E016 `choice:004,u:0056`; E017 `u:0020–0047` | Local afterstate includes continued friction; no lasting cure |

There is no supported transition edge from EVENT_816 to a named main-story checkpoint. Main readings remain usable as independently bounded comparisons, without assuming this event happened first or later. No prediction was frozen before these readings; any model comparison is retrospective.

## 3 Complete speaking roster and identity limits

The six named literary people already have coverage rows. Use the source's actual person IDs, including numeric CH IDs; do not fabricate `BA_PERSON_REISA` or `BA_PERSON_NATSU`.

| Person | Source person ID | First secure identification or labelled speech in this packet | Scope |
|---|---|---|---|
| Kazusa | `BA_PERSON_KAZUSA` | E001 `u:0004–0005` | Anonymous opening call identifies itself; same consultation role |
| Reisa | `BA_PERSON_CH0167` | E002 `u:0028` self-identification; first labelled E003 `u:0001` | Unknown label can carry explicit self-identification |
| Suzumi | `BA_PERSON_SUZUMI` | E004 `u:0048` | Previous unknown greeting is contextually linked |
| Airi | `BA_PERSON_AIRI` | E006 `u:0001` | Secure preference later E017 `u:0008` |
| Natsu | `BA_PERSON_CH0155` | E006 `u:0014` | Secure theatrical speech; drift excluded locally |
| Yoshimi | `BA_PERSON_YOSHIMI` | E006 `u:0004` | Skeptical greeting; later practical ordering and listening |
| Sensei | Special entity, not a student person ID | E001 `choice:001`; E002 inward `u:0001` | Choice-space and structural/inward roles remain separate |

Person-specific represented appearance routes for coverage are Kazusa **001–004, 007–009, 012–017**; Reisa **002–003, 005, 008–011, 014, 017** (002 has explicit self-identification under an unknown label; 009 contains silent responses); Suzumi **004–005**; Airi, Natsu and Yoshimi each **006, 008–009, 013–015, 017**. Sensei has a choice group in every story. These routes include the full contexts around their turns, with each reading's anomalous units separately limited.

The following **eight episode-local generic role buckets** preserve speech without asserting eight unique biographical people. Identically named delinquents in different encounters are not automatically the same individuals. None is automatically merged with previously tracked main-story NPCs.

| Local role | First secure printed locator | What the speech supplies | Coverage proposal |
|---|---|---|---|
| E005 delinquent A, `スケバンA` | `BA:event:816:005:scene:001:u:0004` | Shame at Reisa's changing heroic speech | New local role bucket, UNMODELED |
| E005 delinquent B, `スケバンB` | `BA:event:816:005:scene:001:u:0001` | Complains of surprise attack and inconsistent names | New local role bucket, UNMODELED |
| E008 Trinity bystander B, `トリニティの生徒B` | `BA:event:816:008:scene:001:u:0053` | Asks about then describes the legend | New local role bucket, UNMODELED; two lines under one label do not fix person count |
| E010 delinquent A, `スケバンA` | `BA:event:816:010:scene:001:u:0033` | Threatens adult and demands information | New local role bucket, UNMODELED; exclude discordant `u:0042–0043` from personal register |
| E010 delinquent B, `スケバンB` | `BA:event:816:010:scene:001:u:0031` | Calls reinforcements and seeks legend identity | New local role bucket, UNMODELED |
| E014 delinquent A, `スケバンA` | `BA:event:816:014:scene:001:u:0004` | Time/discovery constraint and explosion response | New local role bucket, UNMODELED |
| E014 delinquent B, `スケバンB` | `BA:event:816:014:scene:001:u:0005` | Recognizes endurance, threatens force, checks injuries | New local role bucket, UNMODELED |
| E014 delinquent C, `スケバンC` | `BA:event:816:014:scene:001:u:0008` | Seeks identity and reacts to legend | New local role bucket, UNMODELED |

Collective labels are not extra individuals: `スケバンたち` at E011 `u:0001` represents the encounter group; `放課後スイーツ部` at E006 `u:0073` and E015 `u:0051` is collective reaction. No guard or robot speaks in this packet. The café girl is described by Kazusa but has no direct speech or secure name here.

All sixteen `？？？` units remain accounted for: E001 `u:0001–0003` (Kazusa reveal), E002 `u:0027–0028,0033` (Reisa self-identification/challenge), E004 `u:0047` (Suzumi context), E005 `u:0003` (Reisa self-identification), E008 `u:0012–0013` (unassigned club role-play voices) and `u:0038` (Reisa context), E010 `u:0002` (Reisa context) and `u:0028` (unassigned delinquent arrival voice), E014 `u:0017,0020` (familiar aid voice contextually associated with Kazusa, exact label unassigned), and E017 `u:0025` (Reisa context). They do not warrant extra independent people merely because the label is unknown.

## 4 Literary result and contrary cases

Kazusa's desired change has a positive object: the café's warm laughter, food and companionship. She first explains cessation through shame at childish self-importance (E007 `u:0053–0059`), then reveals pleasure-inspired imitation and qualifies exact sameness (E016 `u:0036–0049`). This is a revision of her own explanatory account. The analysis should preserve both rather than deciding only the later explanation is true or that Sensei originated her earlier decision.

Reisa's rival schema supplies a public heroic purpose and a way to remain connected to someone she was happy to rediscover. Her reluctance to relinquish the legend is real; so are her response to trusted correction, heard boundaries, protective withdrawal and responsibility (E005 `u:0072–0075`; E009–011). Personal attachment explains part of the conduct without justifying unwanted pursuit. Kazusa's aversion persists while she chooses to seek and help Reisa (E012 `u:0035–0046`). “Secret friendship” is a plausible peer interpretation, not a mutually accepted title.

The club's care is heterogeneity-friendly in words and sometimes intrusive in action. Natsu's ingredient analogy and Airi's acceptance precede disclosure (E006 `u:0046–0054`); costume imitation then violates Kazusa's preferred relation to the past (E008–009). Yoshimi's insistence on listening (E009 `u:0024`) counters her earlier dismissiveness. Her enjoyment of Kazusa's frustration (E015 `u:0023–0026`) prevents a uniformly gentle account of friendship. Natsu's continuing delight in grand language is ordinary play with its own pleasure, not simply an instrument of rescue.

Sensei provides time, contacts, command support and contextual attention, while losing control of a private photograph and participating in jokes (E006–008). Kazusa's gratitude at E016 retains her criticism. The final return to snacks, names and a renewed challenge (E017) refuses both total erasure and complete resolution. No ending statement proves that Kazusa consented to all future duels, that Reisa's promise remains fulfilled, or that care's earlier mistakes are harmless.

## 5 Exact proposed seven ledger deltas

These are interpretive additions to named canonical homes, not replacements for earlier main entries. All claims remain source/state bounded to EVENT_816. No new global claim or operational rule ID is assigned here.

| Ledger | Addition and evidence | Counterevidence or limit |
|---|---|---|
| Character state | Kazusa initiates help while preferring reciprocity, avoids punitive solution, discloses a prior delinquent role, resists old-role publicity, chooses concern despite stated aversion, and revises exact-imitation/erasure. E001 `u:0014–0023`; E002 `u:0013–0019`; E003 `u:0018–0043`; E009 `u:0027–0033`; E012 `u:0035–0046`; E016 `u:0036–0049`. Reisa's old-rival appraisal yields to heard boundaries and protective action, alongside private reunion happiness and loss. E005 `u:0041–0075`; E010 `u:0009–0025`; E011 `u:0011–0032`; E014 `u:0011–0022`. Airi supplies acceptance and taste; Natsu supplies analogy/role-play; Yoshimi supplies listening, practical ordering and teasing pleasure; Suzumi supplies qualified judgment. | Reported history is REVEALED_NOT_NEW; present choice/knowledge changes are event-local. E017 renewed challenge and irritation narrow cure/cessation claims. No durable disposition claim or timeless “tsundere” label. |
| Relationship state | Record **directed** Kazusa→Reisa aversion with concern and help, and Reisa→Kazusa unwanted heroic rivalry followed by restraint/protection and sadness at exclusion. Kazusa→Sensei combines request, courtesy, criticism and growing ease. Reisa→Sensei privately discloses a complaint and requests it not be passed on. Club→Kazusa offers belonging yet misjudges consent; Yoshimi restores listening. Suzumi→Reisa tempers good intentions with social concerns and a nickname boundary. | E011 `u:0027` limits sharing; E009 `u:0028–0033` limits what acceptance permits. Friend/bad-friend/tsundere are peer labels, not agreed facts. E017 keeps friction. |
| School club institution | Sweets Club: pleasure and heterogeneous origins are positive belonging mechanisms (E006 `u:0051–0052`; E016 `u:0038–0045`; E017 `u:0001–0019`). Vigilante Crew: Suzumi describes voluntary local protection and incomplete membership/activity oversight (E004 `u:0056–0058`). Kazusa and attackers expect enforcement after large disturbance, with a territorial distinction (E013 `u:0005–0007`; E014 `u:0007–0010`; E015 `u:0052,0006`). | Testimony is not a charter. “Sweets Gang” is play/rumor, not a formally founded criminal institution. No police arrival, arrest, mandate audit or school-wide prevalence measure. |
| Sensei role and ethics | Retain help for the initial requester and concern for the disruptive student, time to reconsider, coordinated protection and ordinary meal offers. Preserve photograph/privacy lapse (E006 `u:0063–0073`), apology alternatives (E007 `choice:005`), teasing/escalation choices (E008 `choices:003–004`) and no-blame comfort resisted by Reisa (E011 `choice:002,u:0011–0012`). E016 `choice:003` supplies three possible explanations of watchful assistance. | No amalgamation of choices, no omniscient masterplan, no retroactive erasure of error. Inward E012 `u:0030` is not certified spoken. Reisa's private request and Kazusa's boundaries constrain disclosure. |
| Japanese voice and address | Kazusa: mixed casual apology/formal thanks early, direct protests under embarrassment, relaxed `やっほ` and critique later (E001 `u:0004,0017`; E004 `u:0005–0009`; E007 `u:0034–0046`; E016 `u:0002,0014`). Reisa: full-name heroic self-titling, `宿敵`/mission language, polite uncertainty and private sadness (E002 `u:0028`; E005 `u:0048,0054,0075`; E011 `u:0027–0032`). Airi: `ちゃん`, hesitant support and explicit chocomint preference. Natsu: theatrical analogy and self-naming. Yoshimi: direct correction and ordering. Suzumi: polite qualified judgment and nickname refusal. | Use the secure episode-level passages; preserve anomaly list in §6. No audio witness. Slang `サツ` in E015 `u:0052` is printed Airi, so not a secure Kazusa register item. |
| Motif theme callback | Photograph and public labels expose the distance between self and legend; challenge letter moves from demand to renunciation to return (E003; E006–007; E011 `u:0021–0024`; E015 `u:0043–0046`). Heterogeneous ingredients, café warmth and ordinary delivery reveal pleasure as a reason to change/belong (E006 `u:0051–0052`; E016 `u:0038–0049`; E017 `u:0001–0019`). Heroic/monster mythology has strategic, comic and humiliating effects. | Recurrence is within the event unless an independently located comparison is added. Identity jokes and violent comedy do not settle individual consent or health effects. |
| Claim revision | REVISE “stalker” generic-threat account to familiar challenge pattern (E001→E002). DOWNGRADE “misunderstanding resolved” after renewed apparent corroboration (E005→E008). REVISE “care means copying” after Kazusa's explicit refusal (E006→E009). STRENGTHEN personal attachment in Reisa's explicit account (E011). REVISE sudden-shame-only cessation through positive café desire and qualify exact imitation (E007→E016). DOWNGRADE permanent cure/withdrawal after E017. | These are local claim transitions without fabricated canonical IDs. Keep rival justice motive, Kazusa's actual annoyance, adult errors, continued teasing and E017's misinformation as counterevidence. |

### Observed conditional mechanisms

These candidates explain actions in this packet and use the reading/checkpoint as their reference; they are not assigned operational rule IDs. Explicit self-report, observable action and analyst appraisal hypothesis remain separate.

| Candidate and conditioning | Attention appraisal and competing motives | Observable choice and aftermath | Counterevidence and uncertainty |
|---|---|---|---|
| Kazusa under public old-role naming, with trusted help available | She explicitly calls the old legend embarrassing and wants the past erased; accepting care competes with controlling disclosure. Public names and the fallen photograph escalate the problem. | Discloses relevant history, asks the adult/peers to stop, criticizes the help's form, then continues the relationship. E003 `u:0018–0043`; E007 `u:0031–0059`; E009 `u:0027–0036`; E016 `u:0008–0014`. | She is capable of direct refusal and of gratitude; neither universal avoidance nor automatic compliance follows. The café account revises the erasure appraisal. |
| Kazusa after a familiar irritating peer ceases pursuit and may be at risk | The original nuisance has ended, but she notices the late letter delivery and asks about Reisa. Her statement that absence bothers her is explicit; a hidden affection motive is a hypothesis. | Initiates inquiry and seeks the location, approaches with allies, and returns Reisa's letter while protesting sentimental labels. E012 `u:0021–0046`; E013; E015 `u:0035–0046`. | Sensei arranged the suggestive meeting. Kazusa still states aversion and refuses the friend/tsundere labels; this is a specific relation, not a universal rescue rule. |
| Reisa facing evidence inconsistent with her old-rival schema | Old heroic categories make ordinary Kazusa difficult to believe. Suzumi/Sensei credibility inhibits certainty; apparently corroborating costume/rumor escalates it again. Directly heard boundaries and her own reunion happiness supply different considerations. | Requests thinking time, relapses under the costume cue, then promises cessation, assumes responsibility and protects Kazusa from information demands. E005 `u:0063–0078`; E008 `u:0043–0052`; E010 `u:0009–0025`; E011 `u:0011–0032`; E014 `u:0011`. | E017 reopens the challenge after friends supply a distorted report. Capacity to revise is attested, permanent success is not. The exact future consent/duel meaning is unresolved. |
| Sweets Club when a member's unfamiliar past becomes known | Acceptance is explicitly valued; matching an imagined delinquent identity becomes a proposed method. Individual pleasure in performance and teasing can compete with listening to the recipient. | Offers continuity, performs costume solidarity, hears Kazusa's refusal after Yoshimi intervenes, then joins aid while continuing some unwanted legend-play. E006 `u:0046–0054`; E008 `u:0018–0037`; E009 `u:0022–0033`; E013 `u:0022–0038`; E015 `u:0023–0026`; E017 `u:0036–0042`. | The group is not one mind: Airi hesitates/supports, Yoshimi listens and teases, Natsu delights in rhetoric. Continuing play does not certify that the prior boundary was fully understood. |

No predicted action was frozen before exposure. All reconstruction comparisons here are retrospective and remain conditional on the event-local knowledge, role and relationship states. Source limitations can lower readiness even when literary value is CORE.

## 6 Attribution health and naming limits

The episode readings preserve these material tag anomalies: E005 `u:0019–0020,0028,0032,0037`; E006 `u:0050,0071–0072`; E008 `u:0030–0032,0036,0063`; E010 `u:0042–0043`; E013 `u:0017–0018,0034`; E014 `u:0054–0055,0065`; E015 `u:0052,0028,0048–0050`; E017 `u:0003,0031,0038`. Some are strongly contradictory self-addresses; others are discourse/register mismatches. The list marks analytical caution, not corrected speaker identities. Secure adjacent statements can support a scene-level account without transferring every anomalous line to the person an analyst expects.

The rescue involves a blast, unconsciousness and reported lack of apparent injury. This does not prove harmlessness, a clinical diagnosis or a safe bench-care protocol (E014 `choice:001`; E015 `u:0029–0036`). Police intervention is anticipated, never shown. No performance, pitch, acting or visual staging claim is admitted; E001's video marker is uninspected media.

The overarching metadata title is still missing. E017 `u:0048` attests the narrator closing phrase `放課後スイーツ物語　～甘い秘密と銃撃戦～`. Preserve that phrase as source wording. It does not retroactively make the upstream null field non-null or justify changing the stable package name.

## 7 Coverage readiness and gap effects

The six named coverage rows should gain `EVENT_816 001–017 COMPLETE` with person-specific appearances and this checkpoint route, without changing their historical main evidence. Each episode reading preserves which named speaker is actually present; a package receipt is not a claim that each person speaks in every episode.

Propose **Kazusa and Reisa as distributed PARTIAL_MODEL only after interpretive acceptance**, limited to evidenced event-local choices and relations. Kazusa has recoverable attention/appraisal/action/aftermath around shame, help and a familiar irritating peer; Reisa has a rival schema, trusted correction, boundary response, protective action and self-account. Their familiar ordinary interaction, care and conflict domains have conditional source-facing candidates, while institutional professionalism remains limited and no standalone executable model exists. Written-register evidence is broader but still marked by local speaker uncertainty. Chronological transfer to main and whole-person/private predictions remain outside the envelope.

Natsu, Yoshimi, Airi and Suzumi gain substantial ordinary/relational or institutional observations here; retain UNMODELED in this packet's proposal until cross-source readiness is adjudicated. The eight generic role buckets remain UNMODELED. This checkpoint does not recalculate a global census while other contextualization packets are being integrated. No OPERATIONAL_CANDIDATE, BOUNDED_VALIDATED, standalone model or prediction register is warranted.

| Gap | Packet effect | Remaining debt |
|---|---|---|
| G01 ordinary/private breadth | Material improvement for the six named people: club play, care, taste, ordering, appointments and conflict | Other group/bond/MomoTalk/private contexts remain unread here; no one-scene coverage ceiling |
| G06 cross-school ordinary repertoire | Adds a complete Trinity ordinary packet and pressured comparisons | Other schools/contexts still need the independent rotation and inquiry-led work |
| G07 chronology | Several supported local relative anchors | Event-to-main placement and durability unresolved |
| G08 naming/repeat contexts | One context per story; attested closing phrase | Metadata title missing; no global gap closure |
| G09 attribution | Exact local contradictions and choice limits recorded | Raw labels themselves remain contradictory; no silent repairs |
| G10 performed voice | Written register only | No audio/video witness inspected |
| G13 outcomes | Retreat/protection and actor testimony distinguish local success from absent audits | No health certification, police result, legal mandate or durable safety claim |

G02–G05/G11/G12/G14 receive no closure from this packet. Nothing here supplies the missing Hina repair, Hoshino records, Yuuka/Serika breadth, identity-system evidence or unclassified-mode continuity.

## 8 Completion and next responsibility

The **packet reading** is complete and persisted as seventeen substantive readings plus this checkpoint. Scoped source admission, ledger/coverage acceptance and required repository publication remain integrator responsibilities. Once accepted, the event-priority index can record all seventeen objects as ADMITTED with CORE rationale and the bounded exclusions above. Remaining event objects stay visible and eligible.

Phase 2 continues with complete inquiry-led and independent ordinary packets, group stories, linked bond/MomoTalk, character-data written baselines and cumulative integration. This checkpoint cannot certify the entire phase, a mature monograph or operational reconstruction readiness.

## Integration acceptance — 2026-10-01

[Phase 2 cycle 001](../../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md) accepts exactly the source IDs declared above with **ADMIT_WITH_LIMITS**. The cycle owns final ledger, coverage and readiness adjudication; proposals in this reading remain source-facing contribution history. No cross-source chronology or performed-voice evidence is added.
