---
series: BLUE_ARCHIVE
artifact_type: event_analytical_priority_index
scope: Japanese event-source intake, analytical priority, and inspection state
version: "1.2"
status: canonical
source_boundary: "All 1010 pinned event objects; EVENT816/80000/807/814 complete43 objects admitted with limits; remaining967 objects unreviewed; electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8"
do_not_use_as_current_authority: false
created: 2026-09-28
updated: 2026-10-01
---

# Blue Archive event analytical priority index

## 0. Boundary and retrieval

This index covers **all 1,010 canonical event story objects under 61 `event_content_id` packages** in the [current source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md). It preserves complete metadata and records accepted content review:43 objects in EVENT816/EVENT80000/EVENT807/EVENT814 are admitted with limits through cycle005;967 remain unreviewed. Its intake cues alone do not establish priority or admission. The source root is `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/` in the title's extraction workspace. Every episode row gives its stable story ID and exact path relative to that generation. The source witness is `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`. Do not copy source text into this Git index.

The corpus supplies release metadata and canonical story objects, but `RELEASE_CHRONOLOGY.csv` marks **story-world chronology unresolved for all 4,864 source stories**. Event release order, numeric event ID, source path and rerun context cannot independently place an event before or after a main-story state. All 1,010 overarching `event_title_jp` fields are missing in the current raw source; retain event IDs and episode routes rather than inventing event names. Twenty-eight canonical event objects have two release contexts, which must not become duplicate story readings. See the [source-class crosswalk](BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md) for provenance and the [gap register](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) for claim effects.

## 1. Priority contract

**Priority** is analytical value after a complete, context-preserving reading: `CORE`, `HIGH`, `SUPPORTING`, or `UNASSESSED`. `CORE` means omission would materially weaken understanding of a character, relationship, institution, continuity state, or ordinary repertoire needed to interpret that subject. `HIGH` supplies a distinctive comparison, alternative, or substantial social-world account. `SUPPORTING` adds secure context or recurrence. `UNASSESSED` means no literary-priority judgment has been made; it is not a low score.

Record **evidence function** separately: continuity/state, institution/work, peer or Sensei relationship, ordinary desire/routine/play, written voice/humor, rival/negative case, or chronology/identity. A quiet scene can be `CORE` or `HIGH`. `LOW-STAKES / VOICE` from the historical architecture is an evidence-function description, **never a low-priority category**. Selection must consider intrinsic characterization, literary texture, group culture and underrepresented low-pressure contexts alongside plot consequence and model discrimination. A story need not change a durable state or test a model to matter.

Record **workflow state** separately: `INVENTORIED`, `INTAKE_CANDIDATE`, `REVIEWED_UNADMITTED`, `ADMITTED`, or `DEFERRED_WITH_REASON`. `UNRESOLVED` is a named provenance/chronology/identity problem, not a value rank. No row may be `DEFERRED_WITH_REASON` merely because it is comic, seasonal, quiet or apparently unrelated to main plot. A deferral names the affected inquiry, the reason, what remains uninspected, and a revisit trigger. A provisional intake cue from participant IDs can schedule reading but cannot assign literary priority or certify a relationship, chronology or claim.

For each selected package, inspect the complete relevant story sequence and record: the question; story IDs and source class; participants and source-label limits; release/source order; story-local chronological anchors and confidence; ordinary and pressured scenes; positive and contrary observations; priority with reasons; admitted claim scope; and unresolved gaps. Preserve episode-level identities and avoid sampling only dramatic episodes inside a package. If a named subject lacks a low-pressure group/dyad/routine sample, schedule a search across group, event, bond and MomoTalk before claiming broad characterization. A single ordinary scene is an entry point, not a coverage ceiling. At every contextualization cycle, schedule an independent complete-source review from still-unassessed packages, across different schools and contexts, alongside inquiry-led packets. Begin the stable-ID rotation at `EVENT_80000`; advance after each completed rotation review. Anthology-like packages require each contained story to be considered on its own terms. No package may be marked `DEFERRED_WITH_REASON` without a coherent content review and recorded reason. This rotation preserves material that no current main-plot question happens to request.

## 2. Metadata intake queue

The sixteen packages marked `INTAKE_CANDIDATE` below have participant-ID overlap with current [readiness questions](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#24-pilot-reassessment) or supply a deliberate ordinary-life search. They are **review prompts, not priority verdicts or source admissions**. All other packages remain `INVENTORIED` and eligible; their lack of a named prompt is not a decision to discard them. The **first event review packet** is all 17 objects in `EVENT_816`, chosen as a peer/ordinary-context probe on participant metadata; whether its actual stories support that function remains to be read. `EVENT_80000` (nine objects) is the first independent rotation packet; its episodes are separate contexts, not one invented plot. `EVENT_814` (16 objects) is the next Abydos/Serika comparison packet, and `EVENT_806` (11 objects) is a Yuuka/C&C question packet. Each is a complete event-content package; no episode is skipped because its title sounds comic or quiet. This is review order, not literary priority or source admission. Recheck all packages across schools and social contexts when a new subject or question is chosen.

| Event package | Objects | Release metadata (first; not story chronology) | Intake state | Question cue |
|---|---:|---|---|---|
| `EVENT_80000` | 9 | `2025-02-12 11:00:00` | `ADMITTED` | Complete independent rotation accepted: craft, reassurance, desire and private voice; seven HIGH, two CORE; cycle 001; G01/G06 |
| `EVENT_80001` | 16 | `2026-02-18 11:00:00` | `INTAKE_CANDIDATE` | Next independent rotation, all 16 complete objects; no story-level assessment yet |
| `EVENT_801` | 13 | `2021-02-25 12:30:00` | `INTAKE_CANDIDATE` | Peer and institutional routine; Group/club baseline beyond main-story crisis; G01, G06 |
| `EVENT_802` | 11 | `2021-04-29 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_803` | 21 | `2021-06-30 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_804` | 13 | `2021-07-29 12:30:00` | `INTAKE_CANDIDATE` | Hina and Prefect context; Mandate and ordinary/pressure comparison; G04 |
| `EVENT_805` | 9 | `2021-08-26 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_806` | 11 | `2021-09-29 12:30:00` | `INTAKE_CANDIDATE` | Yuuka and C&C overlap; Possible council/club interaction contrast; G02 |
| `EVENT_807` | 1 | `2021-11-03 12:30:00` | `ADMITTED` | HIGH; complete public joy/embodied rehearsal/invitation; no attended concert or audio |
| `EVENT_808` | 12 | `2021-11-30 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_809` | 20 | `2021-12-29 12:30:00` | `INTAKE_CANDIDATE` | PS68 and Abydos context; Possible work, scarcity, peer and role contrast; G03, G05, G06 |
| `EVENT_810` | 102 | `2022-01-26 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_811` | 12 | `2022-01-26 12:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_812` | 15 | `2022-02-23 11:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_813` | 19 | `2022-04-27 11:30:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_814` | 16 | `2022-06-22 11:30:00` | `ADMITTED` | CORE; complete16-object ordinary/peer/private and authority/boundary comparison; no stakes filter |
| `EVENT_815` | 13 | `2022-07-14 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_816` | 17 | `2022-08-24 11:00:00` | `ADMITTED` | Complete CORE Kazusa/Reisa/Sweets Club ordinary, boundary and counterevidence packet; Suzumi HIGH; cycle 001; G01/G06 |
| `EVENT_817` | 11 | `2022-09-28 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_818` | 19 | `2022-10-26 11:00:00` | `INTAKE_CANDIDATE` | Yuuka cross-school overlap; Possible council/social context contrast; G02 |
| `EVENT_819` | 11 | `2022-12-14 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_820` | 15 | `2022-12-28 11:00:00` | `INTAKE_CANDIDATE` | Food and work routines; Ordinary institutional/service interactions; G01, G06 |
| `EVENT_821` | 16 | `2023-01-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_822` | 9 | `2023-02-22 11:00:00` | `INTAKE_CANDIDATE` | Abydos ensemble; A second Abydos context; compare without assuming sequence; G02, G03 |
| `EVENT_823` | 6 | `2023-03-08 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_824` | 1 | `2023-03-12 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_825` | 16 | `2023-04-26 11:00:00` | `INTAKE_CANDIDATE` | Pavane ensemble; Game-club peer context; do not infer Yuuka appearance; G01, G06 |
| `EVENT_826` | 13 | `2023-05-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_827` | 14 | `2023-06-21 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_828` | 15 | `2023-07-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_829` | 15 | `2023-08-23 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_830` | 12 | `2023-09-27 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_831` | 12 | `2023-10-24 11:00:00` | `INTAKE_CANDIDATE` | Engineering club; Work/play group routines; G01, G06 |
| `EVENT_832` | 10 | `2023-12-27 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_833` | 10 | `2024-01-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_834` | 38 | `2024-02-21 11:00:00` | `INTAKE_CANDIDATE` | PS68 and Arius overlap; Persona, peer and aftermath contrast; G01, G05 |
| `EVENT_835` | 16 | `2024-03-27 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_836` | 47 | `2024-04-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_837` | 19 | `2024-06-26 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_838` | 21 | `2024-07-22 11:00:00` | `INTAKE_CANDIDATE` | Arius ensemble; Possible aftermath and peer-routine contrast; G01, G05 |
| `EVENT_839` | 15 | `2024-08-21 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_840` | 17 | `2024-09-25 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_841` | 19 | `2024-10-23 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_842` | 15 | `2024-12-24 11:00:00` | `INTAKE_CANDIDATE` | Yuuka and Veritas overlap; Possible institutional and ordinary context contrast; G02 |
| `EVENT_843` | 9 | `2025-01-20 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_844` | 10 | `2025-02-26 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_845` | 12 | `2025-03-26 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_846` | 13 | `2025-04-22 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_847` | 15 | `2025-06-25 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_848` | 30 | `2025-07-22 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_849` | 14 | `2025-08-20 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_850` | 12 | `2025-09-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_851` | 17 | `2025-10-22 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_852` | 10 | `2025-11-19 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_853` | 13 | `2025-12-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_854` | 29 | `2026-01-20 11:00:00` | `INTAKE_CANDIDATE` | Pavane ensemble; Second game-club context; do not infer Yuuka appearance; G01, G06 |
| `EVENT_856` | 15 | `2026-03-18 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_859` | 14 | `2026-06-24 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_860` | 27 | `2026-07-29 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_861` | 13 | `2026-08-26 11:00:00` | `INVENTORIED` | Open; no story-level assessment |
| `EVENT_862` | 15 | `2026-09-23 11:00:00` | `INVENTORIED` | Open; no story-level assessment |


## 3. Complete event object inventory

Each row remains `INVENTORIED` until a review/admission record for that exact story ID says otherwise. The package-level intake cues above do not upgrade episode rows. `Person IDs` come from structured source metadata and are neither a complete cast audit nor proof of who speaks in the scene. `Release` is documentary metadata only. `Contexts` counts distinct source release/event contexts retained under a single canonical object. The canonical path is relative to the pinned generation, and the story ID resolves through its manifest and source-to-raw trail.

| Event package | Story ID | Raw group ID(s) | Release | Person IDs from metadata | Contexts | Canonical path | Review |
|---|---|---|---|---|---:|---|---|
| `EVENT_80000` | `BA:event:80000:117` | `80000117` | `2025-02-12 11:00:00` | CH0110 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_117_80000117.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:118` | `80000118` | `2025-02-12 11:00:00` | KIRARA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_118_80000118.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:119` | `80000119` | `2025-02-12 11:00:00` | SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_119_80000119.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:120` | `80000120` | `2025-02-12 11:00:00` | CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_120_80000120.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:121` | `80000121` | `2025-02-12 11:00:00` | REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_121_80000121.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:122` | `80000122` | `2025-02-12 11:00:00` | CH0080 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_122_80000122.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:123` | `80000123` | `2025-02-12 11:00:00` | CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_123_80000123.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:124` | `80000124` | `2025-02-12 11:00:00` | CH0070 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_124_80000124.md` | `ADMITTED` |
| `EVENT_80000` | `BA:event:80000:125` | `80000125` | `2025-02-12 11:00:00` | CH0158 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80000/EPISODE_125_80000125.md` | `ADMITTED` |
| `EVENT_80001` | `BA:event:80001:126` | `80000126` | `2026-02-18 11:00:00` | CH0245 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_126_80000126.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:127` | `80000127` | `2026-02-18 11:00:00` | CH0242 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_127_80000127.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:128` | `80000128` | `2026-02-18 11:00:00` | CH0243 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_128_80000128.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:129` | `80000129` | `2026-02-18 11:00:00` | CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_129_80000129.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:130` | `80000130` | `2026-02-18 11:00:00` | CH0222 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_130_80000130.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:131` | `80000131` | `2026-02-18 11:00:00` | CH0109 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_131_80000131.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:132` | `80000132` | `2026-02-18 11:00:00` | CH0304 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_132_80000132.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:133` | `80000133` | `2026-02-18 11:00:00` | CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_133_80000133.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:134` | `80000134` | `2026-02-18 11:00:00` | CH0317 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_134_80000134.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:135` | `80000135` | `2026-02-18 11:00:00` | CH0318 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_135_80000135.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:136` | `80000136` | `2026-02-18 11:00:00` | CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_136_80000136.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:137` | `80000137` | `2026-02-18 11:00:00` | CH0166 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_137_80000137.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:138` | `80000138` | `2026-02-18 11:00:00` | CH0309 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_138_80000138.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:139` | `80000139` | `2026-02-18 11:00:00` | CH0229 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_139_80000139.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:140` | `80000140` | `2026-02-18 11:00:00` | CH0228 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_140_80000140.md` | `INVENTORIED` |
| `EVENT_80001` | `BA:event:80001:141` | `80000141` | `2026-02-18 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_80001/EPISODE_141_80000141.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:001` | `10000005` | `2021-02-25 12:30:00` | IZUNA, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_001_10000005.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:002` | `10000010` | `2021-02-25 12:30:00` | PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_002_10000010.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:003` | `10000025` | `2021-02-25 12:30:00` | IZUNA, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_003_10000025.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:004` | `10000030` | `2021-02-25 12:30:00` | CHISE, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_004_10000030.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:005` | `10000040` | `2021-02-25 12:30:00` | IZUNA, KAEDE, MIMORI, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_005_10000040.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:006` | `10000045` | `2021-02-25 12:30:00` | IZUNA, KAEDE, MIMORI, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_006_10000045.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:007` | `10000050` | `2021-02-25 12:30:00` | KAEDE, MIMORI, PINA, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_007_10000050.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:008` | `10000065` | `2021-02-25 12:30:00` | IZUNA, KAEDE, MIMORI, PINA, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_008_10000065.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:009` | `10000070` | `2021-02-25 12:30:00` | IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_009_10000070.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:010` | `10000080` | `2021-02-25 12:30:00` | IZUNA, KAEDE, MIMORI, PINA, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_010_10000080.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:011` | `10000085` | `2021-02-25 12:30:00` | KAEDE, MIMORI, PINA, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_011_10000085.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:012` | `10000090` | `2021-02-25 12:30:00` | KAEDE, MIMORI, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_012_10000090.md` | `INVENTORIED` |
| `EVENT_801` | `BA:event:801:013` | `10000095` | `2021-02-25 12:30:00` | IZUNA, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_801/EPISODE_013_10000095.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:001` | `10001005` | `2021-04-29 12:30:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_001_10001005.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:002` | `10001010` | `2021-04-29 12:30:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_002_10001010.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:003` | `10001025` | `2021-04-29 12:30:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_003_10001025.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:004` | `10001030` | `2021-04-29 12:30:00` | CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_004_10001030.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:005` | `10001045` | `2021-04-29 12:30:00` | CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_005_10001045.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:006` | `10001050` | `2021-04-29 12:30:00` | CHERINO, MOMIJI, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_006_10001050.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:007` | `10001065` | `2021-04-29 12:30:00` | CHERINO, MOMIJI, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_007_10001065.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:008` | `10001070` | `2021-04-29 12:30:00` | CH0214, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_008_10001070.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:009` | `10001085` | `2021-04-29 12:30:00` | CH0214, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_009_10001085.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:010` | `10001090` | `2021-04-29 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_010_10001090.md` | `INVENTORIED` |
| `EVENT_802` | `BA:event:802:011` | `10001105` | `2021-04-29 12:30:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_802/EPISODE_011_10001105.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:001` | `10002005` | `2021-06-30 12:30:00` | AZUSA, HASUMI, HIHUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_001_10002005.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:002` | `10002010` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_002_10002010.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:003` | `10002025` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_003_10002025.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:004` | `10002030` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_004_10002030.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:005` | `10002045` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_005_10002045.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:006` | `10002050` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_006_10002050.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:007` | `10002065` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_007_10002065.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:008` | `10002070` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, IZUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_008_10002070.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:009` | `10002085` | `2021-06-30 12:30:00` | IZUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_009_10002085.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:010` | `10002090` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, IZUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_010_10002090.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:011` | `10002105` | `2021-06-30 12:30:00` | HIHUMI, IZUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_011_10002105.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:012` | `10002110` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_012_10002110.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:013` | `10002120` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_013_10002120.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:014` | `10002135` | `2021-06-30 12:30:00` | AZUSA, HASUMI, HIHUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_014_10002135.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:015` | `10002140` | `2021-06-30 12:30:00` | HIHUMI, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_015_10002140.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:016` | `10002150` | `2021-06-30 12:30:00` | AZUSA, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_016_10002150.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:017` | `10002160` | `2021-06-30 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_017_10002160.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:018` | `10002170` | `2021-06-30 12:30:00` | IZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_018_10002170.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:019` | `10002180` | `2021-06-30 12:30:00` | AZUSA, HIHUMI, IZUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_019_10002180.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:020` | `10002190` | `2021-06-30 12:30:00` | HIHUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_020_10002190.md` | `INVENTORIED` |
| `EVENT_803` | `BA:event:803:021` | `10002200` | `2021-06-30 12:30:00` | AZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_803/EPISODE_021_10002200.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:001` | `10003005` | `2021-07-29 12:30:00` | AKO, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_001_10003005.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:002` | `10003010` | `2021-07-29 12:30:00` | AKO, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_002_10003010.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:003` | `10003020` | `2021-07-29 12:30:00` | CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_003_10003020.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:004` | `10003030` | `2021-07-29 12:30:00` | AKO, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_004_10003030.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:005` | `10003045` | `2021-07-29 12:30:00` | AKARI, AKO, CHINATSU, HARUNA, HINA, IORI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_005_10003045.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:006` | `10003050` | `2021-07-29 12:30:00` | AKARI, CHINATSU, HARUNA, IORI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_006_10003050.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:007` | `10003055` | `2021-07-29 12:30:00` | AKO, CHINATSU, HARUNA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_007_10003055.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:008` | `10003065` | `2021-07-29 12:30:00` | AKO, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_008_10003065.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:009` | `10003070` | `2021-07-29 12:30:00` | AKARI, AKO, CH0088, CHINATSU, HARUNA, HINA, IORI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_009_10003070.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:010` | `10003080` | `2021-07-29 12:30:00` | HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_010_10003080.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:011` | `10003095` | `2021-07-29 12:30:00` | AKARI, AKO, CH0088, CHINATSU, HARUNA, HINA, IORI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_011_10003095.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:012` | `10003105` | `2021-07-29 12:30:00` | AKO, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_012_10003105.md` | `INVENTORIED` |
| `EVENT_804` | `BA:event:804:013` | `10003110` | `2021-07-29 12:30:00` | AKO, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_804/EPISODE_013_10003110.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:001` | `10004005` | `2021-08-26 12:30:00` | SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_001_10004005.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:002` | `10004010` | `2021-08-26 12:30:00` | CH0137, SAYA, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_002_10004010.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:003` | `10004020` | `2021-08-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_003_10004020.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:004` | `10004030` | `2021-08-26 12:30:00` | CH0137 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_004_10004030.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:005` | `10004040` | `2021-08-26 12:30:00` | KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_005_10004040.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:006` | `10004050` | `2021-08-26 12:30:00` | SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_006_10004050.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:007` | `10004060` | `2021-08-26 12:30:00` | KIRINO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_007_10004060.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:008` | `10004075` | `2021-08-26 12:30:00` | CH0137, SAYA, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_008_10004075.md` | `INVENTORIED` |
| `EVENT_805` | `BA:event:805:009` | `10004085` | `2021-08-26 12:30:00` | SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_805/EPISODE_009_10004085.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:001` | `10005005` | `2021-09-29 12:30:00` | AKANE, ASUNA, KARIN, NERU, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_001_10005005.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:002` | `10005010` | `2021-09-29 12:30:00` | AKANE, ASUNA, KARIN, NERU, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_002_10005010.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:003` | `10005015` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_003_10005015.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:004` | `10005020` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_004_10005020.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:005` | `10005025` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_005_10005025.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:006` | `10005030` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_006_10005030.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:007` | `10005040` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_007_10005040.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:008` | `10005050` | `2021-09-29 12:30:00` | AKANE, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_008_10005050.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:009` | `10005055` | `2021-09-29 12:30:00` | AKANE, ASUNA, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_009_10005055.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:010` | `10005060` | `2021-09-29 12:30:00` | AKANE, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_010_10005060.md` | `INVENTORIED` |
| `EVENT_806` | `BA:event:806:011` | `10005065` | `2021-09-29 12:30:00` | AKANE, ASUNA, KARIN, NERU, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_806/EPISODE_011_10005065.md` | `INVENTORIED` |
| `EVENT_807` | `BA:event:807:001` | `10006010` | `2021-11-03 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_807/EPISODE_001_10006010.md` | `ADMITTED` |
| `EVENT_808` | `BA:event:808:001` | `10007005` | `2021-11-30 12:30:00` | CH0088, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_001_10007005.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:002` | `10007010` | `2021-11-30 12:30:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_002_10007010.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:003` | `10007025` | `2021-11-30 12:30:00` | CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_003_10007025.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:004` | `10007030` | `2021-11-30 12:30:00` | CH0124, NODOKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_004_10007030.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:005` | `10007045` | `2021-11-30 12:30:00` | CH0124, NODOKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_005_10007045.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:006` | `10007050` | `2021-11-30 12:30:00` | CH0214, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_006_10007050.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:007` | `10007065` | `2021-11-30 12:30:00` | CH0214, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_007_10007065.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:008` | `10007070` | `2021-11-30 12:30:00` | CHINATSU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_008_10007070.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:009` | `10007080` | `2021-11-30 12:30:00` | CH0088, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_009_10007080.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:010` | `10007090` | `2021-11-30 12:30:00` | CH0088, CH0214, CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_010_10007090.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:011` | `10007105` | `2021-11-30 12:30:00` | CH0088, CH0214, CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_011_10007105.md` | `INVENTORIED` |
| `EVENT_808` | `BA:event:808:012` | `10007115` | `2021-11-30 12:30:00` | CH0214, CHERINO, NODOKA, SHIGURE, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_808/EPISODE_012_10007115.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:001` | `10008005` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_001_10008005.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:002` | `10008010` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_002_10008010.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:003` | `10008025` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_003_10008025.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:004` | `10008030` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_004_10008030.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:005` | `10008035` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_005_10008035.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:006` | `10008040` | `2021-12-29 12:30:00` | ARU, KAYOKO, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_006_10008040.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:007` | `10008045` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_007_10008045.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:008` | `10008050` | `2021-12-29 12:30:00` | ARU, HARUKA, IORI, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_008_10008050.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:009` | `10008055` | `2021-12-29 12:30:00` | AKO, ARU, IORI, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_009_10008055.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:010` | `10008060` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_010_10008060.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:011` | `10008070` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_011_10008070.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:012` | `10008080` | `2021-12-29 12:30:00` | ARU, CH0088, HARUKA, HOSHINO, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_012_10008080.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:013` | `10008090` | `2021-12-29 12:30:00` | ARU, AYANE, CH0088, HOSHINO, KAYOKO, MUTSUKI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_013_10008090.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:014` | `10008100` | `2021-12-29 12:30:00` | ARU, AYANE, CH0088, HOSHINO, MUTSUKI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_014_10008100.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:015` | `10008110` | `2021-12-29 12:30:00` | AKO, ARU, CH0088, HARUKA, HOSHINO, IORI, KAYOKO, MUTSUKI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_015_10008110.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:016` | `10008115` | `2021-12-29 12:30:00` | ARU, AYANE, HARUKA, HOSHINO, KAYOKO, MUTSUKI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_016_10008115.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:017` | `10008120` | `2021-12-29 12:30:00` | ARU, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_017_10008120.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:018` | `10008125` | `2021-12-29 12:30:00` | ARU, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_018_10008125.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:019` | `10008130` | `2021-12-29 12:30:00` | IORI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_019_10008130.md` | `INVENTORIED` |
| `EVENT_809` | `BA:event:809:020` | `10008135` | `2021-12-29 12:30:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_809/EPISODE_020_10008135.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:001` | `10009000` | `2022-01-26 12:30:00` | CH0141, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_001_10009000.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:001:118` | `80000001` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_001_80000001.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:002` | `10009005` | `2022-01-26 12:30:00` | CH0081, CH0141, KIRINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_002_10009005.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:002:119` | `80000002` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_002_80000002.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:003` | `10009075` | `2022-01-26 12:30:00` | CH0081, CH0141, CH0160, KIRINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_003_10009075.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:003:120` | `80000003` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_003_80000003.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:004` | `10009080` | `2022-01-26 12:30:00` | CH0152, HANAE, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_004_10009080.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:004:121` | `80000004` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_004_80000004.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:005` | `10009090` | `2022-01-26 12:30:00` | CH0160, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_005_10009090.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:005:122` | `80000005` | `2022-01-26 12:30:00` | HIHUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_005_80000005.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:006` | `10009100` | `2022-01-26 12:30:00` | SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_006_10009100.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:006:123` | `80000006` | `2022-01-26 12:30:00` | MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_006_80000006.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:007` | `10009110` | `2022-01-26 12:30:00` | CH0152, HANAE, SERINA, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_007_10009110.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:007:124` | `80000007` | `2022-01-26 12:30:00` | HANAE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_007_80000007.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:008` | `10009120` | `2022-01-26 12:30:00` | WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_008_10009120.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:008:125` | `80000008` | `2022-01-26 12:30:00` | IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_008_80000008.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:009` | `10009130` | `2022-01-26 12:30:00` | CH0152, HANAE, SERINA, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_009_10009130.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:009:126` | `80000009` | `2022-01-26 12:30:00` | AKARI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_009_80000009.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:010` | `80000010` | `2022-01-26 12:30:00` | ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_010_80000010.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:011` | `80000011` | `2022-01-26 12:30:00` | KAYOKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_011_80000011.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:012` | `80000012` | `2022-01-26 12:30:00` | SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_012_80000012.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:013` | `80000013` | `2022-01-26 12:30:00` | HOSHINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_013_80000013.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:014` | `80000014` | `2022-01-26 12:30:00` | AYANE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_014_80000014.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:015` | `80000015` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_015_80000015.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:016` | `80000016` | `2022-01-26 12:30:00` | KOTAMA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_016_80000016.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:017` | `80000017` | `2022-01-26 12:30:00` | CH0160 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_017_80000017.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:018` | `80000018` | `2022-01-26 12:30:00` | YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_018_80000018.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:019` | `80000019` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_019_80000019.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:020` | `80000020` | `2022-01-26 12:30:00` | ARIS | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_020_80000020.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:021` | `80000021` | `2022-01-26 12:30:00` | HARE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_021_80000021.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:022` | `80000022` | `2022-01-26 12:30:00` | MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_022_80000022.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:023` | `80000023` | `2022-01-26 12:30:00` | HIBIKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_023_80000023.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:024` | `80000024` | `2022-01-26 12:30:00` | UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_024_80000024.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:025` | `80000025` | `2022-01-26 12:30:00` | CHERINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_025_80000025.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:026` | `80000026` | `2022-01-26 12:30:00` | TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_026_80000026.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:027` | `80000027` | `2022-01-26 12:30:00` | NODOKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_027_80000027.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:028` | `80000028` | `2022-01-26 12:30:00` | SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_028_80000028.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:029` | `80000029` | `2022-01-26 12:30:00` | SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_029_80000029.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:030` | `80000030` | `2022-01-26 12:30:00` | KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_030_80000030.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:031` | `80000031` | `2022-01-26 12:30:00` | CH0141 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_031_80000031.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:032` | `80000032` | `2022-01-26 12:30:00` | HANAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_032_80000032.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:033` | `80000033` | `2022-01-26 12:30:00` | HASUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_033_80000033.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:034` | `80000034` | `2022-01-26 12:30:00` | HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_034_80000034.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:035` | `80000035` | `2022-01-26 12:30:00` | AKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_035_80000035.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:036` | `80000036` | `2022-01-26 12:30:00` | IZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_036_80000036.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:037` | `80000037` | `2022-01-26 12:30:00` | ARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_037_80000037.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:038` | `80000038` | `2022-01-26 12:30:00` | MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_038_80000038.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:039` | `80000039` | `2022-01-26 12:30:00` | FUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_039_80000039.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:040` | `80000040` | `2022-01-26 12:30:00` | JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_040_80000040.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:041` | `80000041` | `2022-01-26 12:30:00` | SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_041_80000041.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:042` | `80000042` | `2022-01-26 12:30:00` | NONOMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_042_80000042.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:043` | `80000043` | `2022-01-26 12:30:00` | SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_043_80000043.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:044` | `80000044` | `2022-01-26 12:30:00` | MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_044_80000044.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:045` | `80000045` | `2022-01-26 12:30:00` | MIDORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_045_80000045.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:046` | `80000046` | `2022-01-26 12:30:00` | CHISE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_046_80000046.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:047` | `80000047` | `2022-01-26 12:30:00` | SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_047_80000047.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:048` | `80000048` | `2022-01-26 12:30:00` | IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_048_80000048.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:049` | `80000049` | `2022-01-26 12:30:00` | TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_049_80000049.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:050` | `80000050` | `2022-01-26 12:30:00` | WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_050_80000050.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:051` | `80000051` | `2022-01-26 12:30:00` | HARUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_051_80000051.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:052` | `80000052` | `2022-01-26 12:30:00` | AZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_052_80000052.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:053` | `80000053` | `2022-01-26 12:30:00` | KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_053_80000053.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:054` | `80000054` | `2022-01-26 12:30:00` | SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_054_80000054.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:055` | `80000055` | `2022-01-26 12:30:00` | MARI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_055_80000055.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:056` | `80000056` | `2022-01-26 12:30:00` | SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_056_80000056.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:057` | `80000057` | `2022-01-26 12:30:00` | SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_057_80000057.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:058` | `80000058` | `2022-01-26 12:30:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_058_80000058.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:059` | `80000059` | `2022-01-26 12:30:00` | YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_059_80000059.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:060` | `80000060` | `2022-01-26 12:30:00` | CH0155 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_060_80000060.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:061` | `80000061` | `2022-01-26 12:30:00` | CHINATSU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_061_80000061.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:062` | `80000062` | `2022-01-26 12:30:00` | CH0081 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_062_80000062.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:063` | `80000063` | `2022-01-26 12:30:00` | HARUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_063_80000063.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:064` | `80000064` | `2022-01-26 12:30:00` | ASUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_064_80000064.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:065` | `80000065` | `2022-01-26 12:30:00` | AKANE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_065_80000065.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:066` | `80000066` | `2022-01-26 12:30:00` | KARIN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_066_80000066.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:067` | `80000067` | `2022-01-26 12:30:00` | NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_067_80000067.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:068` | `80000068` | `2022-01-26 12:30:00` | KOTORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_068_80000068.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:069` | `80000069` | `2022-01-26 12:30:00` | PINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_069_80000069.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:070` | `80000070` | `2022-01-26 12:30:00` | TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_070_80000070.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:071` | `80000071` | `2022-01-26 12:30:00` | CH0137 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_071_80000071.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:072` | `80000072` | `2022-01-26 12:30:00` | HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_072_80000072.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:073` | `80000073` | `2022-01-26 12:30:00` | CH0169 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_073_80000073.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:074` | `80000074` | `2022-01-26 12:30:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_074_80000074.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:075` | `80000075` | `2022-01-26 12:30:00` | HIYORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_075_80000075.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:076` | `80000076` | `2022-01-26 12:30:00` | MISAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_076_80000076.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:077` | `80000077` | `2022-01-26 12:30:00` | ATSUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_077_80000077.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:078` | `80000078` | `2022-01-26 12:30:00` | SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_078_80000078.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:079` | `80000079` | `2022-01-26 12:30:00` | MIMORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_079_80000079.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:080` | `80000080` | `2022-01-26 12:30:00` | KAEDE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_080_80000080.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:081` | `80000081` | `2022-01-26 12:30:00` | CH0114 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_081_80000081.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:082` | `80000082` | `2022-01-26 12:30:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_082_80000082.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:083` | `80000083` | `2022-01-26 12:30:00` | CH0156 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_083_80000083.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:084` | `80000084` | `2022-01-26 12:30:00` | CH0113 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_084_80000084.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:085` | `80000085` | `2022-01-26 12:30:00` | MIYAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_085_80000085.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:086` | `80000086` | `2022-01-26 12:30:00` | MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_086_80000086.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:087` | `80000087` | `2022-01-26 12:30:00` | CH0144 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_087_80000087.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:088` | `80000088` | `2022-01-26 12:30:00` | CH0145 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_088_80000088.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:089` | `80000089` | `2022-01-26 12:30:00` | CH0095 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_089_80000089.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:090` | `80000090` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_090_80000090.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:091` | `80000091` | `2022-01-26 12:30:00` | SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_091_80000091.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:092` | `80000092` | `2022-01-26 12:30:00` | CH0152 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_092_80000092.md` | `INVENTORIED` |
| `EVENT_810` | `BA:event:810:093` | `80000093` | `2022-01-26 12:30:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_810/EPISODE_093_80000093.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:001` | `10009010` | `2022-01-26 12:30:00` | CH0081, CH0141, CH0160, KIRINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_001_10009010.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:002` | `10009015` | `2022-01-26 12:30:00` | CH0081, CH0141, CH0160, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_002_10009015.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:003` | `10009020` | `2022-01-26 12:30:00` | CH0141, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_003_10009020.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:004` | `10009025` | `2022-01-26 12:30:00` | CH0081, CH0141, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_004_10009025.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:005` | `10009030` | `2022-01-26 12:30:00` | CH0141, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_005_10009030.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:006` | `10009035` | `2022-01-26 12:30:00` | CH0081, CH0141, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_006_10009035.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:007` | `10009040` | `2022-01-26 12:30:00` | CH0081, CH0141, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_007_10009040.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:008` | `10009045` | `2022-01-26 12:30:00` | CH0081, CH0141, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_008_10009045.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:009` | `10009050` | `2022-01-26 12:30:00` | CH0081, CH0141 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_009_10009050.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:010` | `10009055` | `2022-01-26 12:30:00` | CH0081, CH0141, CH0160, CHINATSU, HASUMI, KIRINO, SUZUMI, WAKAMO, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_010_10009055.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:011` | `10009060` | `2022-01-26 12:30:00` | CH0141, CH0160, KIRINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_011_10009060.md` | `INVENTORIED` |
| `EVENT_811` | `BA:event:811:012` | `10009065` | `2022-01-26 12:30:00` | CH0081, CH0141, CH0160, KIRINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_811/EPISODE_012_10009065.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:001` | `10010005` | `2022-02-23 11:30:00` | HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_001_10010005.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:002` | `10010010` | `2022-02-23 11:30:00` | HINATA, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_002_10010010.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:003` | `10010020` | `2022-02-23 11:30:00` | CH0169, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_003_10010020.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:004` | `10010030` | `2022-02-23 11:30:00` | AIRI, CH0155, HINATA, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_004_10010030.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:005` | `10010045` | `2022-02-23 11:30:00` | AIRI, CH0155, HINATA, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_005_10010045.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:006` | `10010050` | `2022-02-23 11:30:00` | HINATA, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_006_10010050.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:007` | `10010065` | `2022-02-23 11:30:00` | HINATA, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_007_10010065.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:008` | `10010070` | `2022-02-23 11:30:00` | CH0169, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_008_10010070.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:009` | `10010085` | `2022-02-23 11:30:00` | HINATA, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_009_10010085.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:010` | `10010090` | `2022-02-23 11:30:00` | CH0169, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_010_10010090.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:011` | `10010105` | `2022-02-23 11:30:00` | CH0169, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_011_10010105.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:012` | `10010110` | `2022-02-23 11:30:00` | CH0169, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_012_10010110.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:013` | `10010125` | `2022-02-23 11:30:00` | CH0169, HINATA, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_013_10010125.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:014` | `10010130` | `2022-02-23 11:30:00` | AIRI, CH0155, HINATA, KAZUSA, MASHIRO, SAKURAKO, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_014_10010130.md` | `INVENTORIED` |
| `EVENT_812` | `BA:event:812:015` | `10010145` | `2022-02-23 11:30:00` | CH0169 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_812/EPISODE_015_10010145.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:001` | `10011005` | `2022-04-27 11:30:00` | CH0107, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_001_10011005.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:002` | `10011010` | `2022-04-27 11:30:00` | CH0107, CH0109, CH0113, CH0114, CHISE, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_002_10011010.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:003` | `10011020` | `2022-04-27 11:30:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_003_10011020.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:004` | `10011025` | `2022-04-27 11:30:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_004_10011025.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:005` | `10011030` | `2022-04-27 11:30:00` | CH0077, CH0079, CH0109, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_005_10011030.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:006` | `10011035` | `2022-04-27 11:30:00` | CH0109, CH0113, CH0114, CH0156, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_006_10011035.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:007` | `10011040` | `2022-04-27 11:30:00` | CH0077, CH0113, CH0114, IZUNA, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_007_10011040.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:008` | `10011045` | `2022-04-27 11:30:00` | CH0113, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_008_10011045.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:009` | `10011050` | `2022-04-27 11:30:00` | CH0077, CH0109, CH0113, CH0114, CH0156, IZUNA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_009_10011050.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:010` | `10011055` | `2022-04-27 11:30:00` | CH0113, CH0114, CH0156, IZUNA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_010_10011055.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:011` | `10011060` | `2022-04-27 11:30:00` | CH0109, CH0113, CH0114, CH0156, IZUNA, MIMORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_011_10011060.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:012` | `10011065` | `2022-04-27 11:30:00` | CH0113, CH0156, IZUNA, MIMORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_012_10011065.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:013` | `10011070` | `2022-04-27 11:30:00` | CH0107, CH0109, CH0113, CH0114, KAEDE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_013_10011070.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:014` | `10011075` | `2022-04-27 11:30:00` | CH0113, CH0114, IZUNA, KAEDE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_014_10011075.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:015` | `10011080` | `2022-04-27 11:30:00` | CH0107, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_015_10011080.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:016` | `10011085` | `2022-04-27 11:30:00` | CH0107, CH0113, CH0114, CH0156, IZUNA, KAEDE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_016_10011085.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:017` | `10011090` | `2022-04-27 11:30:00` | CH0109, CH0113, CH0114, CH0156, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_017_10011090.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:018` | `10011095` | `2022-04-27 11:30:00` | CH0077, CH0109, CH0113, CH0114, CH0156, IZUNA, KAEDE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_018_10011095.md` | `INVENTORIED` |
| `EVENT_813` | `BA:event:813:019` | `10011105` | `2022-04-27 11:30:00` | CH0077, CH0079, CH0107, CH0109, CH0113, CH0114, CH0156, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_813/EPISODE_019_10011105.md` | `INVENTORIED` |
| `EVENT_814` | `BA:event:814:001` | `10012005` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_001_10012005.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:002` | `10012010` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_002_10012010.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:003` | `10012015` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_003_10012015.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:004` | `10012020` | `2022-06-22 11:30:00` | CH0166, HOSHINO, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_004_10012020.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:005` | `10012025` | `2022-06-22 11:30:00` | AYANE, CH0166, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_005_10012025.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:006` | `10012030` | `2022-06-22 11:30:00` | AYANE, CH0166, HOSHINO, NONOMI, SERIKA, SHIROKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_006_10012030.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:007` | `10012035` | `2022-06-22 11:30:00` | AYANE, CH0166, SHIROKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_007_10012035.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:008` | `10012040` | `2022-06-22 11:30:00` | AYANE, CH0166, HOSHINO, NONOMI, SERIKA, SHIROKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_008_10012040.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:009` | `10012045` | `2022-06-22 11:30:00` | AYANE, CH0166, NONOMI, SERIKA, SHIROKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_009_10012045.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:010` | `10012050` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_010_10012050.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:011` | `10012055` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_011_10012055.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:012` | `10012065` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_012_10012065.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:013` | `10012070` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_013_10012070.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:014` | `10012080` | `2022-06-22 11:30:00` | HOSHINO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_014_10012080.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:015` | `10012090` | `2022-06-22 11:30:00` | AYANE, CH0166, HOSHINO, NONOMI, SERIKA, SHIROKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_015_10012090.md` | `ADMITTED` |
| `EVENT_814` | `BA:event:814:016` | `10012095` | `2022-06-22 11:30:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_814/EPISODE_016_10012095.md` | `ADMITTED` |
| `EVENT_815` | `BA:event:815:001` | `10013005` | `2022-07-14 11:00:00` | AYANE, CH0109, CH0110, CHISE, HOSHINO, IZUNA, MIMORI, NONOMI, PINA, SERIKA, SHIROKO, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_001_10013005.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:002` | `10013010` | `2022-07-14 11:00:00` | AYANE, CH0109, CH0110, CHISE, HOSHINO, IZUNA, MIMORI, NONOMI, SERIKA, SHIROKO, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_002_10013010.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:003` | `10013020` | `2022-07-14 11:00:00` | AYANE, CH0109, CH0110, CHISE, HOSHINO, IZUNA, MIMORI, NONOMI, SERIKA, SHIROKO, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_003_10013020.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:004` | `10013030` | `2022-07-14 11:00:00` | CH0088, CH0089, CH0110, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_004_10013030.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:005` | `10013035` | `2022-07-14 11:00:00` | CH0088, CH0089, CH0110, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_005_10013035.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:006` | `10013040` | `2022-07-14 11:00:00` | AYANE, HOSHINO, SERIKA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_006_10013040.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:007` | `10013050` | `2022-07-14 11:00:00` | CH0110, CHISE, IZUNA, KAEDE, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_007_10013050.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:008` | `10013055` | `2022-07-14 11:00:00` | CH0110, CHISE, KAEDE, MIMORI, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_008_10013055.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:009` | `10013060` | `2022-07-14 11:00:00` | CH0088, CH0110, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_009_10013060.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:010` | `10013065` | `2022-07-14 11:00:00` | CH0088, CH0089, CH0110, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_010_10013065.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:011` | `10013070` | `2022-07-14 11:00:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_011_10013070.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:012` | `10013080` | `2022-07-14 11:00:00` | CH0110, CH0166, CHISE, HOSHINO, IZUNA, MIMORI, SERIKA, SHIROKO, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_012_10013080.md` | `INVENTORIED` |
| `EVENT_815` | `BA:event:815:013` | `10013090` | `2022-07-14 11:00:00` | AYANE, CH0109, CH0110, CH0166, CHISE, HOSHINO, IZUNA, MIMORI, NONOMI, SERIKA, SHIROKO, SHIZUKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_815/EPISODE_013_10013090.md` | `INVENTORIED` |
| `EVENT_816` | `BA:event:816:001` | `10014005` | `2022-08-24 11:00:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_001_10014005.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:002` | `10014010` | `2022-08-24 11:00:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_002_10014010.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:003` | `10014015` | `2022-08-24 11:00:00` | CH0167, KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_003_10014015.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:004` | `10014020` | `2022-08-24 11:00:00` | KAZUSA, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_004_10014020.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:005` | `10014025` | `2022-08-24 11:00:00` | CH0167, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_005_10014025.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:006` | `10014030` | `2022-08-24 11:00:00` | AIRI, CH0155, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_006_10014030.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:007` | `10014035` | `2022-08-24 11:00:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_007_10014035.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:008` | `10014040` | `2022-08-24 11:00:00` | AIRI, CH0155, CH0167, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_008_10014040.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:009` | `10014045` | `2022-08-24 11:00:00` | AIRI, CH0155, CH0167, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_009_10014045.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:010` | `10014050` | `2022-08-24 11:00:00` | CH0167 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_010_10014050.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:011` | `10014055` | `2022-08-24 11:00:00` | CH0167 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_011_10014055.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:012` | `10014060` | `2022-08-24 11:00:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_012_10014060.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:013` | `10014065` | `2022-08-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_013_10014065.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:014` | `10014070` | `2022-08-24 11:00:00` | AIRI, CH0155, CH0167, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_014_10014070.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:015` | `10014075` | `2022-08-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_015_10014075.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:016` | `10014080` | `2022-08-24 11:00:00` | KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_016_10014080.md` | `ADMITTED` |
| `EVENT_816` | `BA:event:816:017` | `10014085` | `2022-08-24 11:00:00` | AIRI, CH0155, CH0167, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_816/EPISODE_017_10014085.md` | `ADMITTED` |
| `EVENT_817` | `BA:event:817:001` | `10015005` | `2022-09-28 11:00:00` | CH0095, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_001_10015005.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:002` | `10015010` | `2022-09-28 11:00:00` | CH0095, HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_002_10015010.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:003` | `10015020` | `2022-09-28 11:00:00` | CH0095, CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_003_10015020.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:004` | `10015030` | `2022-09-28 11:00:00` | CH0095, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_004_10015030.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:005` | `10015035` | `2022-09-28 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_005_10015035.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:006` | `10015040` | `2022-09-28 11:00:00` | CH0095, HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_006_10015040.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:007` | `10015045` | `2022-09-28 11:00:00` | CH0095, CH0160, HARE, HIBIKI, KOTAMA, KOTORI, MAKI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_007_10015045.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:008` | `10015050` | `2022-09-28 11:00:00` | CH0095, CH0160, KOTORI, MAKI, SUMIRE, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_008_10015050.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:009` | `10015060` | `2022-09-28 11:00:00` | CH0095, CH0160, HARE, HIBIKI, KOTAMA, KOTORI, MAKI, SUMIRE, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_009_10015060.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:010` | `10015070` | `2022-09-28 11:00:00` | CH0095, CH0160, HARE, HIBIKI, KOTAMA, KOTORI, MAKI, SUMIRE, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_010_10015070.md` | `INVENTORIED` |
| `EVENT_817` | `BA:event:817:011` | `10015075` | `2022-09-28 11:00:00` | CH0095, HARE, HIBIKI, KOTORI, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_817/EPISODE_011_10015075.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:001` | `10016005` | `2022-10-26 11:00:00` | AYANE, HANAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_001_10016005.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:002` | `10016010` | `2022-10-26 11:00:00` | AKO, CH0079, HASUMI, MARI, NAGISA, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_002_10016010.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:003` | `10016020` | `2022-10-26 11:00:00` | AKARI, CH0135, HARUNA, HASUMI, IZUMI, SHIZUKO, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_003_10016020.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:004` | `10016030` | `2022-10-26 11:00:00` | YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_004_10016030.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:005` | `10016035` | `2022-10-26 11:00:00` | AKO, CH0095, CH0144, MIYAKO, MOE, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_005_10016035.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:006` | `10016040` | `2022-10-26 11:00:00` | CH0081, MARI, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_006_10016040.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:007` | `10016050` | `2022-10-26 11:00:00` | CH0114, CH0141, CH0155, CHISE, HANAE, HASUMI, HIBIKI, KAEDE, KIRINO, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_007_10016050.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:008` | `10016060` | `2022-10-26 11:00:00` | AKO, CH0141, HASUMI, KIRINO, MARI, MASHIRO, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_008_10016060.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:009` | `10016070` | `2022-10-26 11:00:00` | AKO, AYANE, CH0144, CH0145, HASUMI, HIBIKI, HOSHINO, KOTORI, MARI, MIYAKO, MOE, NONOMI, SERIKA, SHIROKO, UTAHA, YUUKA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_009_10016070.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:010` | `10016080` | `2022-10-26 11:00:00` | AKO, CH0114, CHISE, HASUMI, IZUNA, KAEDE, MARI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_010_10016080.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:011` | `10016085` | `2022-10-26 11:00:00` | CH0114, CHISE, HASUMI, IZUNA, KAEDE, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_011_10016085.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:012` | `10016090` | `2022-10-26 11:00:00` | AKARI, AKO, CH0095, CH0155, HARUNA, HASUMI, HOSHINO, IZUMI, IZUNA, MASHIRO, SERIKA, TSURUGI, YUUKA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_012_10016090.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:013` | `10016100` | `2022-10-26 11:00:00` | AKO, CH0095, HASUMI, MARI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_013_10016100.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:014` | `10016110` | `2022-10-26 11:00:00` | AKARI, HARUNA, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_014_10016110.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:015` | `10016120` | `2022-10-26 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_015_10016120.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:016` | `10016130` | `2022-10-26 11:00:00` | AKO, HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_016_10016130.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:017` | `10016140` | `2022-10-26 11:00:00` | CH0160, MAKI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_017_10016140.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:018` | `10016150` | `2022-10-26 11:00:00` | CH0081, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_018_10016150.md` | `INVENTORIED` |
| `EVENT_818` | `BA:event:818:019` | `10016160` | `2022-10-26 11:00:00` | CH0095, HASUMI, MARI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_818/EPISODE_019_10016160.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:001` | `10017005` | `2022-12-14 11:00:00` | CH0152, HANAE, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_001_10017005.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:002` | `10017010` | `2022-12-14 11:00:00` | HANAE, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_002_10017010.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:003` | `10017025` | `2022-12-14 11:00:00` | HANAE, HASUMI, MASHIRO, SERINA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_003_10017025.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:004` | `10017030` | `2022-12-14 11:00:00` | HANAE, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_004_10017030.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:005` | `10017040` | `2022-12-14 11:00:00` | CH0152, HANAE, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_005_10017040.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:006` | `10017050` | `2022-12-14 11:00:00` | CH0152, HASUMI, MASHIRO, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_006_10017050.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:007` | `10017060` | `2022-12-14 11:00:00` | CH0152, HANAE, HASUMI, MASHIRO, SERINA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_007_10017060.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:008` | `10017065` | `2022-12-14 11:00:00` | CH0152, HASUMI, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_008_10017065.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:009` | `10017070` | `2022-12-14 11:00:00` | CH0152, HANAE, HASUMI, SERINA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_009_10017070.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:010` | `10017085` | `2022-12-14 11:00:00` | CH0152, HANAE, HASUMI, SERINA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_010_10017085.md` | `INVENTORIED` |
| `EVENT_819` | `BA:event:819:011` | `10017090` | `2022-12-14 11:00:00` | CH0152, HANAE, HASUMI, MASHIRO, SERINA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_819/EPISODE_011_10017090.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:001` | `10018005` | `2022-12-28 11:00:00` | AKARI, HARUNA, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_001_10018005.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:002` | `10018010` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_002_10018010.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:003` | `10018015` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_003_10018015.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:004` | `10018020` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_004_10018020.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:005` | `10018030` | `2022-12-28 11:00:00` | AKARI, HARUNA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_005_10018030.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:006` | `10018040` | `2022-12-28 11:00:00` | FUUKA, HARUNA, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_006_10018040.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:007` | `10018050` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_007_10018050.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:008` | `10018060` | `2022-12-28 11:00:00` | AKARI, IZUMI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_008_10018060.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:009` | `10018065` | `2022-12-28 11:00:00` | AKARI, IZUMI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_009_10018065.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:010` | `10018070` | `2022-12-28 11:00:00` | AKARI, HARUNA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_010_10018070.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:011` | `10018075` | `2022-12-28 11:00:00` | AKARI, HARUNA, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_011_10018075.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:012` | `10018080` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_012_10018080.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:013` | `10018090` | `2022-12-28 11:00:00` | FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_013_10018090.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:014` | `10018100` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_014_10018100.md` | `INVENTORIED` |
| `EVENT_820` | `BA:event:820:015` | `10018105` | `2022-12-28 11:00:00` | AKARI, FUUKA, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_820/EPISODE_015_10018105.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:001` | `10019005` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_001_10019005.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:002` | `10019010` | `2023-01-24 11:00:00` | ARU, AYANE, HARUKA, HOSHINO, MAKI, MUTSUKI, NONOMI, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_002_10019010.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:003` | `10019015` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_003_10019015.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:004` | `10019020` | `2023-01-24 11:00:00` | AKANE, CH0071, CHERINO, KARIN, NERU, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_004_10019020.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:005` | `10019025` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_005_10019025.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:006` | `10019030` | `2023-01-24 11:00:00` | ARIS, HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_006_10019030.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:007` | `10019035` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_007_10019035.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:008` | `10019040` | `2023-01-24 11:00:00` | ATSUKO, CH0152, HANAKO, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_008_10019040.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:009` | `10019045` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_009_10019045.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:010` | `10019050` | `2023-01-24 11:00:00` | CH0088, CH0089, CH0095, CH0160, CH0198, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_010_10019050.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:011` | `10019055` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_011_10019055.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:012` | `10019060` | `2023-01-24 11:00:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_012_10019060.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:013` | `10019070` | `2023-01-24 11:00:00` | AKARI, AZUSA, HARUNA, HIHUMI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_013_10019070.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:014` | `10019075` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_014_10019075.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:015` | `10019080` | `2023-01-24 11:00:00` | AKARI, AZUSA, CH0159, CH0160, HARUNA, HIHUMI, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_015_10019080.md` | `INVENTORIED` |
| `EVENT_821` | `BA:event:821:016` | `10019085` | `2023-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_821/EPISODE_016_10019085.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:001` | `10020005` | `2023-02-22 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_001_10020005.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:002` | `10020010` | `2023-02-22 11:00:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_002_10020010.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:003` | `10020015` | `2023-02-22 11:00:00` | AYANE, CH0159, CH0160, HOSHINO, NONOMI, SERIKA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_003_10020015.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:004` | `10020020` | `2023-02-22 11:00:00` | AYANE, HOSHINO, NONOMI, SERIKA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_004_10020020.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:005` | `10020025` | `2023-02-22 11:00:00` | AYANE, CH0159, CH0160, HOSHINO, NONOMI, SERIKA, SHIROKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_005_10020025.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:006` | `10020030` | `2023-02-22 11:00:00` | AYANE, CH0159, HOSHINO, NONOMI, SERIKA, SHIROKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_006_10020030.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:007` | `10020035` | `2023-02-22 11:00:00` | AKARI, ARIS, AYANE, CH0159, HARUNA, HOSHINO, IZUMI, NONOMI, SERIKA, SHIROKO, YUUKA, ZUNKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_007_10020035.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:008` | `10020040` | `2023-02-22 11:00:00` | AYANE, CH0158, CH0159, HIBIKI, HOSHINO, KOTORI, NONOMI, SERIKA, UTAHA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_008_10020040.md` | `INVENTORIED` |
| `EVENT_822` | `BA:event:822:009` | `10020045` | `2023-02-22 11:00:00` | AYANE, CH0160, HARE, HOSHINO, KOTAMA, MAKI, SHIROKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_822/EPISODE_009_10020045.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:001` | `10021005` | `2023-03-08 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_001_10021005.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:002` | `10021010` | `2023-03-08 11:00:00` | SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_002_10021010.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:003` | `10021015,10021016,10021017` | `2023-03-08 11:00:00` | AYANE, CH0158, CH0159, HANAKO, HARUNA, HOSHINO, KAYOKO, NONOMI, SERIKA, SHIROKO, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_003_10021015.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:004` | `10021020` | `2023-03-08 11:00:00` | AYANE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_004_10021020.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:005` | `10021021` | `2023-03-08 11:00:00` | AYANE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_005_10021021.md` | `INVENTORIED` |
| `EVENT_823` | `BA:event:823:006` | `10021022` | `2023-03-08 11:00:00` | SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_823/EPISODE_006_10021022.md` | `INVENTORIED` |
| `EVENT_824` | `BA:event:824:001` | `10022005` | `2023-03-12 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_824/EPISODE_001_10022005.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:001` | `10023005` | `2023-04-26 11:00:00` | CH0187 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_001_10023005.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:002` | `10023010` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_002_10023010.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:003` | `10023020` | `2023-04-26 11:00:00` | ARIS, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_003_10023020.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:004` | `10023030` | `2023-04-26 11:00:00` | ARIS, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_004_10023030.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:005` | `10023040` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_005_10023040.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:006` | `10023050` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_006_10023050.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:007` | `10023055` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_007_10023055.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:008` | `10023060` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_008_10023060.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:009` | `10023070` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_009_10023070.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:010` | `10023075` | `2023-04-26 11:00:00` | CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_010_10023075.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:011` | `10023080` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_011_10023080.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:012` | `10023090` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_012_10023090.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:013` | `10023095` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_013_10023095.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:014` | `10023100` | `2023-04-26 11:00:00` | ARIS, CH0187, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_014_10023100.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:015` | `10023105` | `2023-04-26 11:00:00` | ARIS, CH0187, MIDORI, MOMOI, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_015_10023105.md` | `INVENTORIED` |
| `EVENT_825` | `BA:event:825:016` | `10023110` | `2023-04-26 11:00:00` | AKANE, ARIS, ASUNA, CH0187, MIDORI, MOMOI, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_825/EPISODE_016_10023110.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:001` | `10024005` | `2023-05-24 11:00:00` | CH0135 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_001_10024005.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:002` | `10024010` | `2023-05-24 11:00:00` | CH0135, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_002_10024010.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:003` | `10024020` | `2023-05-24 11:00:00` | CH0135, CH0138, CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_003_10024020.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:004` | `10024025` | `2023-05-24 11:00:00` | CH0135, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_004_10024025.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:005` | `10024030` | `2023-05-24 11:00:00` | CH0135, REIZYO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_005_10024030.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:006` | `10024040` | `2023-05-24 11:00:00` | CH0135, CH0138, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_006_10024040.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:007` | `10024045` | `2023-05-24 11:00:00` | CH0135, CH0138, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_007_10024045.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:008` | `10024050` | `2023-05-24 11:00:00` | CH0135, CH0137, CH0138, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_008_10024050.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:009` | `10024060` | `2023-05-24 11:00:00` | CH0135, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_009_10024060.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:010` | `10024070` | `2023-05-24 11:00:00` | CH0135, CH0138, REIZYO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_010_10024070.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:011` | `10024080` | `2023-05-24 11:00:00` | CH0135, CH0138, REIZYO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_011_10024080.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:012` | `10024090` | `2023-05-24 11:00:00` | CH0135, CH0138, CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_012_10024090.md` | `INVENTORIED` |
| `EVENT_826` | `BA:event:826:013` | `10024100` | `2023-05-24 11:00:00` | CH0135, CH0137, CH0139, REIZYO, SAYA, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_826/EPISODE_013_10024100.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:001` | `10025005` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_001_10025005.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:002` | `10025010` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_002_10025010.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:003` | `10025020` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_003_10025020.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:004` | `10025030` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_004_10025030.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:005` | `10025040` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_005_10025040.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:006` | `10025050` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_006_10025050.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:007` | `10025060` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_007_10025060.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:008` | `10025070` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_008_10025070.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:009` | `10025075` | `2023-06-21 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_009_10025075.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:010` | `10025080` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_010_10025080.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:011` | `10025090` | `2023-06-21 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_011_10025090.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:012` | `10025100` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_012_10025100.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:013` | `10025105` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_013_10025105.md` | `INVENTORIED` |
| `EVENT_827` | `BA:event:827:014` | `10025110` | `2023-06-21 11:00:00` | CH0144, CH0145, MIYAKO, MOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_827/EPISODE_014_10025110.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:001` | `10026005` | `2023-07-24 11:00:00` | SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_001_10026005.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:002` | `10026010` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_002_10026010.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:003` | `10026020` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_003_10026020.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:004` | `10026030` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_004_10026030.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:005` | `10026035` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_005_10026035.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:006` | `10026040` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_006_10026040.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:007` | `10026045` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_007_10026045.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:008` | `10026050` | `2023-07-24 11:00:00` | HANAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_008_10026050.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:009` | `10026060` | `2023-07-24 11:00:00` | HINATA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_009_10026060.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:010` | `10026065` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_010_10026065.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:011` | `10026070` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_011_10026070.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:012` | `10026080` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_012_10026080.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:013` | `10026090` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_013_10026090.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:014` | `10026095` | `2023-07-24 11:00:00` | CH0169, HANAKO, HINATA, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_014_10026095.md` | `INVENTORIED` |
| `EVENT_828` | `BA:event:828:015` | `10026100` | `2023-07-24 11:00:00` | AZUSA, CH0169, HANAKO, HIHUMI, HINATA, KOHARU, MARI, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_828/EPISODE_015_10026100.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:001` | `10027005` | `2023-08-23 11:00:00` | CH0124, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_001_10027005.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:002` | `10027010` | `2023-08-23 11:00:00` | CH0124, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_002_10027010.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:003` | `10027020` | `2023-08-23 11:00:00` | CH0124, CH0229 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_003_10027020.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:004` | `10027030` | `2023-08-23 11:00:00` | CH0124, CH0228 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_004_10027030.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:005` | `10027045` | `2023-08-23 11:00:00` | CH0124, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_005_10027045.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:006` | `10027050` | `2023-08-23 11:00:00` | CH0124, CH0229 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_006_10027050.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:007` | `10027060` | `2023-08-23 11:00:00` | CH0124, CH0229 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_007_10027060.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:008` | `10027070` | `2023-08-23 11:00:00` | CH0124, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_008_10027070.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:009` | `10027080` | `2023-08-23 11:00:00` | CH0124, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_009_10027080.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:010` | `10027090` | `2023-08-23 11:00:00` | CH0124, MOMIJI, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_010_10027090.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:011` | `10027100` | `2023-08-23 11:00:00` | CH0124, CH0214, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_011_10027100.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:012` | `10027110` | `2023-08-23 11:00:00` | CH0124, MOMIJI, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_012_10027110.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:013` | `10027115` | `2023-08-23 11:00:00` | CH0124, CH0228, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_013_10027115.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:014` | `10027120` | `2023-08-23 11:00:00` | CH0124, CH0228, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_014_10027120.md` | `INVENTORIED` |
| `EVENT_829` | `BA:event:829:015` | `10027125` | `2023-08-23 11:00:00` | CH0124, CH0228, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_829/EPISODE_015_10027125.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:001` | `10028005` | `2023-09-27 11:00:00` | CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_001_10028005.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:002` | `10028010` | `2023-09-27 11:00:00` | CH0071, HASUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_002_10028010.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:003` | `10028020` | `2023-09-27 11:00:00` | CH0071 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_003_10028020.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:004` | `10028025` | `2023-09-27 11:00:00` | CH0071, CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_004_10028025.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:005` | `10028030` | `2023-09-27 11:00:00` | CH0071, CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_005_10028030.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:006` | `10028035` | `2023-09-27 11:00:00` | CH0071, CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_006_10028035.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:007` | `10028040` | `2023-09-27 11:00:00` | CH0071, CH0089, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_007_10028040.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:008` | `10028045` | `2023-09-27 11:00:00` | CH0071, CH0089, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_008_10028045.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:009` | `10028050` | `2023-09-27 11:00:00` | CH0071, CH0089, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_009_10028050.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:010` | `10028060` | `2023-09-27 11:00:00` | CH0071, CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_010_10028060.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:011` | `10028070` | `2023-09-27 11:00:00` | CH0071, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_011_10028070.md` | `INVENTORIED` |
| `EVENT_830` | `BA:event:830:012` | `10028080` | `2023-09-27 11:00:00` | CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_830/EPISODE_012_10028080.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:001` | `10029005` | `2023-10-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_001_10029005.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:002` | `10029010` | `2023-10-24 11:00:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_002_10029010.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:003` | `10029020` | `2023-10-24 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_003_10029020.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:004` | `10029025` | `2023-10-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_004_10029025.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:005` | `10029030` | `2023-10-24 11:00:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_005_10029030.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:006` | `10029040` | `2023-10-24 11:00:00` | CH0159, HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_006_10029040.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:007` | `10029050` | `2023-10-24 11:00:00` | KOTORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_007_10029050.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:008` | `10029055` | `2023-10-24 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_008_10029055.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:009` | `10029060` | `2023-10-24 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_009_10029060.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:010` | `10029065` | `2023-10-24 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_010_10029065.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:011` | `10029075` | `2023-10-24 11:00:00` | HIBIKI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_011_10029075.md` | `INVENTORIED` |
| `EVENT_831` | `BA:event:831:012` | `10029085` | `2023-10-24 11:00:00` | CH0159, HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_831/EPISODE_012_10029085.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:001` | `10030005` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_001_10030005.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:002` | `10030010` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_002_10030010.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:003` | `10030020` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_003_10030020.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:004` | `10030030` | `2023-12-27 11:00:00` | CH0160, HARE, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_004_10030030.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:005` | `10030040` | `2023-12-27 11:00:00` | CH0160, CH0245, KOTAMA, MAKI, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_005_10030040.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:006` | `10030050` | `2023-12-27 11:00:00` | CH0160, CH0245, HARE, KOTAMA, MAKI, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_006_10030050.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:007` | `10030060` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_007_10030060.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:008` | `10030070` | `2023-12-27 11:00:00` | CH0160, CH0245, HARE, KOTAMA, MAKI, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_008_10030070.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:009` | `10030075` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_009_10030075.md` | `INVENTORIED` |
| `EVENT_832` | `BA:event:832:010` | `10030080` | `2023-12-27 11:00:00` | CH0160, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_832/EPISODE_010_10030080.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:001` | `10031005` | `2024-01-24 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_001_10031005.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:002` | `10031010` | `2024-01-24 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_002_10031010.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:003` | `10031020` | `2024-01-24 11:00:00` | CH0079, CH0088, CH0089, HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_003_10031020.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:004` | `10031030` | `2024-01-24 11:00:00` | AKO, CH0079, CH0088, CH0089, HINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_004_10031030.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:005` | `10031040` | `2024-01-24 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_005_10031040.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:006` | `10031050` | `2024-01-24 11:00:00` | CH0076, CH0079, KIRARA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_006_10031050.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:007` | `10031060` | `2024-01-24 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_007_10031060.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:008` | `10031070` | `2024-01-24 11:00:00` | AKARI, AKO, CH0077, CH0079, CH0088, CH0156, CH0238, HARUNA, IZUMI, JURI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_008_10031070.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:009` | `10031080` | `2024-01-24 11:00:00` | AKO, CH0079, CH0080, CH0156, CH0238, CHINATSU, HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_009_10031080.md` | `INVENTORIED` |
| `EVENT_833` | `BA:event:833:010` | `10031081` | `2024-01-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_833/EPISODE_010_10031081.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:001` | `10032005` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_001_10032005.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:002` | `10032010` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_002_10032010.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:003` | `10032015` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_003_10032015.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:004` | `10032020` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_004_10032020.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:005` | `10032030` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_005_10032030.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:006` | `10032035` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_006_10032035.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:007` | `10032040` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_007_10032040.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:008` | `10032045` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_008_10032045.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:009` | `10032050` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_009_10032050.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:010` | `10032055` | `2024-02-21 11:00:00` | SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_010_10032055.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:011` | `10032060` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_011_10032060.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:012` | `10032065` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_012_10032065.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:013` | `10032070` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_013_10032070.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:014` | `10032075` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_014_10032075.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:015` | `10032080` | `2024-02-21 11:00:00` | ARU, HARUKA, KAYOKO, MUTSUKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_015_10032080.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:094` | `80000094` | `2024-02-21 11:00:00` | CH0071 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_094_80000094.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:095` | `80000095` | `2024-02-21 11:00:00` | CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_095_80000095.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:096` | `80000096` | `2024-02-21 11:00:00` | CH0198 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_096_80000096.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:097` | `80000097` | `2024-02-21 11:00:00` | SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_097_80000097.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:098` | `80000098` | `2024-02-21 11:00:00` | CH0167 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_098_80000098.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:099` | `80000099` | `2024-02-21 11:00:00` | CH0088 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_099_80000099.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:100` | `80000100` | `2024-02-21 11:00:00` | CH0135 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_100_80000100.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:101` | `80000101` | `2024-02-21 11:00:00` | CH0138 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_101_80000101.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:102` | `80000102` | `2024-02-21 11:00:00` | MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_102_80000102.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:103` | `80000103` | `2024-02-21 11:00:00` | NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_103_80000103.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:104` | `80000104` | `2024-02-21 11:00:00` | CH0214 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_104_80000104.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:105` | `80000105` | `2024-02-21 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_105_80000105.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:106` | `80000106` | `2024-02-21 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_106_80000106.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:107` | `80000107` | `2024-02-21 11:00:00` | CH0124 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_107_80000107.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:108` | `80000108` | `2024-02-21 11:00:00` | CH0187 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_108_80000108.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:109` | `80000109` | `2024-02-21 11:00:00` | CH0107 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_109_80000109.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:110` | `80000110` | `2024-02-21 11:00:00` | CH0170 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_110_80000110.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:111` | `80000111` | `2024-02-21 11:00:00` | CH0224 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_111_80000111.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:112` | `80000112` | `2024-02-21 11:00:00` | CH0225 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_112_80000112.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:113` | `80000113` | `2024-02-21 11:00:00` | CH0161 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_113_80000113.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:114` | `80000114` | `2024-02-21 11:00:00` | CH0077 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_114_80000114.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:115` | `80000115` | `2024-02-21 11:00:00` | CH0069 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_115_80000115.md` | `INVENTORIED` |
| `EVENT_834` | `BA:event:834:116` | `80000116` | `2024-02-21 11:00:00` | CH0079 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_834/EPISODE_116_80000116.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:001` | `10033005` | `2024-03-27 11:00:00` | CH0107, CH0109, CHISE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_001_10033005.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:002` | `10033010` | `2024-03-27 11:00:00` | CH0109, CH0110, CHISE, KAEDE, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_002_10033010.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:003` | `10033020` | `2024-03-27 11:00:00` | CH0076, CH0077, CH0079, CH0080, CH0110, CH0156, CH0238, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_003_10033020.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:004` | `10033030` | `2024-03-27 11:00:00` | CH0076, CH0110, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_004_10033030.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:005` | `10033040` | `2024-03-27 11:00:00` | CH0076, CH0088, CH0089, CH0110, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_005_10033040.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:006` | `10033045` | `2024-03-27 11:00:00` | CH0076, CH0088, CH0110, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_006_10033045.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:007` | `10033050` | `2024-03-27 11:00:00` | AKARI, CH0110, FUUKA, HARUNA, IZUMI, KAEDE, PINA, TSUBAKI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_007_10033050.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:008` | `10033055` | `2024-03-27 11:00:00` | CH0110, PINA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_008_10033055.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:009` | `10033060` | `2024-03-27 11:00:00` | CH0077, CH0079, CH0080, CH0110, CH0156, CH0238, KAEDE, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_009_10033060.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:010` | `10033065` | `2024-03-27 11:00:00` | CH0076, CH0077, CH0079, CH0080, CH0110, CH0156, CH0238, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_010_10033065.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:011` | `10033070` | `2024-03-27 11:00:00` | CH0076, CH0110, KIRARA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_011_10033070.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:012` | `10033080` | `2024-03-27 11:00:00` | CH0110, CHISE, KAEDE, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_012_10033080.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:013` | `10033090` | `2024-03-27 11:00:00` | CH0076, CH0110, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_013_10033090.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:014` | `10033095` | `2024-03-27 11:00:00` | CH0110, PINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_014_10033095.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:015` | `10033100` | `2024-03-27 11:00:00` | CH0076, CH0110, CH0161, CH0224, CHINATSU, CHISE, IORI, KAEDE, KIRARA, PINA, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_015_10033100.md` | `INVENTORIED` |
| `EVENT_835` | `BA:event:835:016` | `10033110` | `2024-03-27 11:00:00` | AKO, CH0076, CH0079, CH0107, CH0109, CH0110, CH0161, HINA, KAEDE, KIRARA, PINA, SHIZUKO, TSUBAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_835/EPISODE_016_10033110.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:001` | `10034005` | `2024-04-24 11:00:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_001_10034005.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:002` | `10034010` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_002_10034010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:003` | `10034020` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_003_10034020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:004` | `10034030` | `2024-04-24 11:00:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_004_10034030.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:005` | `10034040` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_005_10034040.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:006` | `10034050` | `2024-04-24 11:00:00` | CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_006_10034050.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:007` | `10034060` | `2024-04-24 11:00:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_007_10034060.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:008` | `10034070` | `2024-04-24 11:00:00` | AIRI, CH0071, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_008_10034070.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:009` | `10034080` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_009_10034080.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:010` | `10034081` | `2024-04-24 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_010_10034081.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:011` | `10034090` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_011_10034090.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:012` | `10034100` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_012_10034100.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:013` | `10034110` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_013_10034110.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:014` | `10034120` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_014_10034120.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:015` | `10034130` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_015_10034130.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:016` | `10034140` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_016_10034140.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:017` | `10034150` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_017_10034150.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:018` | `10034160` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_018_10034160.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:019` | `10034170` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_019_10034170.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:020` | `10034180` | `2024-04-24 11:00:00` | AIRI, CH0155, CH0167, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_020_10034180.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:021` | `10034190` | `2024-04-24 11:00:00` | AIRI, CH0155, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_021_10034190.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:022` | `11434010` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_022_11434010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:023` | `11434020` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_023_11434020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:024` | `11034030` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_024_11034030.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:025` | `11034060` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_025_11034060.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:026` | `11134030` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_026_11134030.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:027` | `11134060` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_027_11134060.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:028` | `11234030` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_028_11234030.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:029` | `11234060` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_029_11234060.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:030` | `11334030` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_030_11334030.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:031` | `11334060` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_031_11334060.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:032` | `11034010` | `2024-04-24 11:00:00` | AIRI, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_032_11034010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:033` | `11334020` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_033_11334020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:034` | `11234040` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_034_11234040.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:035` | `11134050` | `2024-04-24 11:00:00` | CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_035_11134050.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:036` | `11134010` | `2024-04-24 11:00:00` | CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_036_11134010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:037` | `11234020` | `2024-04-24 11:00:00` | CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_037_11234020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:038` | `11334040` | `2024-04-24 11:00:00` | CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_038_11334040.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:039` | `11034050` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_039_11034050.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:040` | `11334010` | `2024-04-24 11:00:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_040_11334010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:041` | `11134020` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_041_11134020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:042` | `11034040` | `2024-04-24 11:00:00` | AIRI, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_042_11034040.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:043` | `11234050` | `2024-04-24 11:00:00` | AIRI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_043_11234050.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:044` | `11234010` | `2024-04-24 11:00:00` | CH0155, KAZUSA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_044_11234010.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:045` | `11034020` | `2024-04-24 11:00:00` | AIRI, CH0155, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_045_11034020.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:046` | `11134040` | `2024-04-24 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_046_11134040.md` | `INVENTORIED` |
| `EVENT_836` | `BA:event:836:047` | `11334050` | `2024-04-24 11:00:00` | CH0155 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_836/EPISODE_047_11334050.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:001` | `10035005` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_001_10035005.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:002` | `10035010` | `2024-06-26 11:00:00` | CH0141, CH0170, CH0264, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_002_10035010.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:003` | `10035020` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_003_10035020.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:004` | `10035030` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_004_10035030.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:005` | `10035040` | `2024-06-26 11:00:00` | CH0141, CH0166, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_005_10035040.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:006` | `10035050` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_006_10035050.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:007` | `10035060` | `2024-06-26 11:00:00` | CH0141, CH0166, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_007_10035060.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:008` | `10035070` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_008_10035070.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:009` | `10035075` | `2024-06-26 11:00:00` | CH0141, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_009_10035075.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:010` | `10035080` | `2024-06-26 11:00:00` | CH0141, CH0166, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_010_10035080.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:011` | `10035090` | `2024-06-26 11:00:00` | CH0141, CH0166, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_011_10035090.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:012` | `10035095` | `2024-06-26 11:00:00` | CH0141, CH0166, CH0170, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_012_10035095.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:013` | `10035100` | `2024-06-26 11:00:00` | CH0141, CH0160, CH0166, CH0170, KIRINO, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_013_10035100.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:014` | `10035110` | `2024-06-26 11:00:00` | CH0141, CH0170, CH0264, KIRINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_014_10035110.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:015` | `10035120` | `2024-06-26 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_015_10035120.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:016` | `10035130` | `2024-06-26 11:00:00` | CH0160, HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_016_10035130.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:017` | `10035140` | `2024-06-26 11:00:00` | CH0166 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_017_10035140.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:018` | `10035150` | `2024-06-26 11:00:00` | CH0166 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_018_10035150.md` | `INVENTORIED` |
| `EVENT_837` | `BA:event:837:019` | `10035160` | `2024-06-26 11:00:00` | CH0264 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_837/EPISODE_019_10035160.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:001` | `10036005` | `2024-07-22 11:00:00` | SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_001_10036005.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:002` | `10036010` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_002_10036010.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:003` | `10036020` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_003_10036020.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:004` | `10036030` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_004_10036030.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:005` | `10036035` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_005_10036035.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:006` | `10036040` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_006_10036040.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:007` | `10036045` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_007_10036045.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:008` | `10036050` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_008_10036050.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:009` | `10036055` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_009_10036055.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:010` | `10036060` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_010_10036060.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:011` | `10036070` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_011_10036070.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:012` | `10036080` | `2024-07-22 11:00:00` | ATSUKO, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_012_10036080.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:013` | `10036090` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_013_10036090.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:014` | `10036095` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_014_10036095.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:015` | `10036100` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_015_10036100.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:016` | `10036110` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_016_10036110.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:017` | `10036120` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_017_10036120.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:018` | `10036130` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_018_10036130.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:019` | `10036140` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_019_10036140.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:020` | `10036150` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_020_10036150.md` | `INVENTORIED` |
| `EVENT_838` | `BA:event:838:021` | `10036160` | `2024-07-22 11:00:00` | ATSUKO, HIYORI, MISAKI, SAORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_838/EPISODE_021_10036160.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:001` | `10037005` | `2024-08-21 11:00:00` | CH0135, CH0139, CHERINO, REIZYO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_001_10037005.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:002` | `10037010` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_002_10037010.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:003` | `10037020` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_003_10037020.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:004` | `10037030` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_004_10037030.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:005` | `10037040` | `2024-08-21 11:00:00` | CH0135, CH0137, CH0138, CHERINO, SHUN, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_005_10037040.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:006` | `10037050` | `2024-08-21 11:00:00` | TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_006_10037050.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:007` | `10037060` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, SAYA, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_007_10037060.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:008` | `10037070` | `2024-08-21 11:00:00` | CH0139, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_008_10037070.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:009` | `10037080` | `2024-08-21 11:00:00` | CH0139, CHERINO, SAYA, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_009_10037080.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:010` | `10037090` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, SAYA, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_010_10037090.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:011` | `10037095` | `2024-08-21 11:00:00` | CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_011_10037095.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:012` | `10037100` | `2024-08-21 11:00:00` | CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_012_10037100.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:013` | `10037105` | `2024-08-21 11:00:00` | CH0138, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_013_10037105.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:014` | `10037110` | `2024-08-21 11:00:00` | CH0138, CH0139, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_014_10037110.md` | `INVENTORIED` |
| `EVENT_839` | `BA:event:839:015` | `10037115` | `2024-08-21 11:00:00` | CH0135, CH0138, CH0139, CH0355, REIZYO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_839/EPISODE_015_10037115.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:001` | `10038005` | `2024-09-25 11:00:00` | CH0138, CH0139, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_001_10038005.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:002` | `10038010` | `2024-09-25 11:00:00` | CH0135, CH0138, CH0139, REIZYO, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_002_10038010.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:003` | `10038020` | `2024-09-25 11:00:00` | CH0138, CH0139, CH0355, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_003_10038020.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:004` | `10038030` | `2024-09-25 11:00:00` | CH0137, CH0138, CH0139, CH0355, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_004_10038030.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:005` | `10038040` | `2024-09-25 11:00:00` | CH0138, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_005_10038040.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:006` | `10038045` | `2024-09-25 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_006_10038045.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:007` | `10038050` | `2024-09-25 11:00:00` | CH0138, CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_007_10038050.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:008` | `10038055` | `2024-09-25 11:00:00` | CH0138, CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_008_10038055.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:009` | `10038060` | `2024-09-25 11:00:00` | REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_009_10038060.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:010` | `10038070` | `2024-09-25 11:00:00` | CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_010_10038070.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:011` | `10038080` | `2024-09-25 11:00:00` | CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_011_10038080.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:012` | `10038085` | `2024-09-25 11:00:00` | CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_012_10038085.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:013` | `10038090` | `2024-09-25 11:00:00` | CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_013_10038090.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:014` | `10038095` | `2024-09-25 11:00:00` | CH0138, CH0139, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_014_10038095.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:015` | `10038100` | `2024-09-25 11:00:00` | CH0139, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_015_10038100.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:016` | `10038105` | `2024-09-25 11:00:00` | CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_016_10038105.md` | `INVENTORIED` |
| `EVENT_840` | `BA:event:840:017` | `10038110` | `2024-09-25 11:00:00` | CH0138, CH0139, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_840/EPISODE_017_10038110.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:001` | `10039005` | `2024-10-23 11:00:00` | MARI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_001_10039005.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:002` | `10039010` | `2024-10-23 11:00:00` | CH0152, HINATA, MARI, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_002_10039010.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:003` | `10039020` | `2024-10-23 11:00:00` | AYANE, HOSHINO, MARI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_003_10039020.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:004` | `10039025` | `2024-10-23 11:00:00` | AYANE, HOSHINO, MARI, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_004_10039025.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:005` | `10039030` | `2024-10-23 11:00:00` | CH0141, KIRINO, MARI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_005_10039030.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:006` | `10039035` | `2024-10-23 11:00:00` | CH0141, KIRINO, MARI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_006_10039035.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:007` | `10039040` | `2024-10-23 11:00:00` | CH0152, MARI, SAKURAKO, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_007_10039040.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:008` | `10039050` | `2024-10-23 11:00:00` | CH0152, MARI, NAGISA, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_008_10039050.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:009` | `10039060` | `2024-10-23 11:00:00` | AZUSA, CH0069, CH0152, HANAE, HANAKO, HIHUMI, KOHARU, MARI, NAGISA, SAKURAKO, SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_009_10039060.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:010` | `10039070` | `2024-10-23 11:00:00` | CH0069, CH0152, MARI, NAGISA, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_010_10039070.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:011` | `10039080` | `2024-10-23 11:00:00` | CH0152, MARI, SAKURAKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_011_10039080.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:012` | `10039090` | `2024-10-23 11:00:00` | AYANE, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_012_10039090.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:013` | `10039100` | `2024-10-23 11:00:00` | HIBIKI, KOTORI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_013_10039100.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:014` | `10039110` | `2024-10-23 11:00:00` | AIRI, CH0155, KAZUSA, YOSHIMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_014_10039110.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:015` | `10039120` | `2024-10-23 11:00:00` | CH0141, CH0170, KIRINO, MARI, UTAHA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_015_10039120.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:016` | `10039130` | `2024-10-23 11:00:00` | CH0071, CH0113, CH0114, CH0245, HASUMI, IZUNA, TSURUGI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_016_10039130.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:017` | `10039140` | `2024-10-23 11:00:00` | CH0166 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_017_10039140.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:018` | `10039150` | `2024-10-23 11:00:00` | CH0069, CH0070, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_018_10039150.md` | `INVENTORIED` |
| `EVENT_841` | `BA:event:841:019` | `10039160` | `2024-10-23 11:00:00` | AKARI, HARUNA, IZUMI, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_841/EPISODE_019_10039160.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:001` | `10040005` | `2024-12-24 11:00:00` | CH0198 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_001_10040005.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:002` | `10040010` | `2024-12-24 11:00:00` | CH0095, CH0198, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_002_10040010.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:003` | `10040020` | `2024-12-24 11:00:00` | CH0095, CH0160, HARE, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_003_10040020.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:004` | `10040030` | `2024-12-24 11:00:00` | CH0095, CH0198, HARE, KOTAMA, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_004_10040030.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:005` | `10040040` | `2024-12-24 11:00:00` | CH0095, CH0198, HARE, KOTAMA, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_005_10040040.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:006` | `10040050` | `2024-12-24 11:00:00` | CH0095, CH0198, HARE, KOTAMA, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_006_10040050.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:007` | `10040060` | `2024-12-24 11:00:00` | CH0198, HARE, KOTAMA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_007_10040060.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:008` | `10040065` | `2024-12-24 11:00:00` | CH0198, HARE, KOTAMA, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_008_10040065.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:009` | `10040070` | `2024-12-24 11:00:00` | CH0095, CH0160, CH0198, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_009_10040070.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:010` | `10040080` | `2024-12-24 11:00:00` | CH0095, CH0160, CH0198, HARE, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_010_10040080.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:011` | `10040090` | `2024-12-24 11:00:00` | CH0095, CH0198, HARE, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_011_10040090.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:012` | `10040100` | `2024-12-24 11:00:00` | CH0095, CH0160, HARE, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_012_10040100.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:013` | `10040110` | `2024-12-24 11:00:00` | CH0160, CH0198, HARE, KOTAMA, MAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_013_10040110.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:014` | `10040120` | `2024-12-24 11:00:00` | CH0095, CH0160, CH0198, HARE, KOTAMA, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_014_10040120.md` | `INVENTORIED` |
| `EVENT_842` | `BA:event:842:015` | `10040130` | `2024-12-24 11:00:00` | CH0095, CH0160, HARE, MAKI, YUUKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_842/EPISODE_015_10040130.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:001` | `10041005` | `2025-01-20 11:00:00` | CH0070 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_001_10041005.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:002` | `10041010` | `2025-01-20 11:00:00` | CH0069, CH0070, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_002_10041010.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:003` | `10041020` | `2025-01-20 11:00:00` | AKANE, ASUNA, CH0070, CH0187, KARIN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_003_10041020.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:004` | `10041030` | `2025-01-20 11:00:00` | CH0158, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_004_10041030.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:005` | `10041040` | `2025-01-20 11:00:00` | CH0070, CH0158, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_005_10041040.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:006` | `10041050` | `2025-01-20 11:00:00` | CH0158, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_006_10041050.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:007` | `10041060` | `2025-01-20 11:00:00` | CH0070, CH0158, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_007_10041060.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:008` | `10041070` | `2025-01-20 11:00:00` | AKANE, ASUNA, CH0070, CH0158, CH0187, KARIN, NERU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_008_10041070.md` | `INVENTORIED` |
| `EVENT_843` | `BA:event:843:009` | `10041080` | `2025-01-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_843/EPISODE_009_10041080.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:001` | `10042005` | `2025-02-26 11:00:00` | FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_001_10042005.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:002` | `10042010` | `2025-02-26 11:00:00` | CHINATSU, FUUKA, IORI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_002_10042010.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:003` | `10042020` | `2025-02-26 11:00:00` | CH0081, CHINATSU, FUUKA, IORI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_003_10042020.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:004` | `10042030` | `2025-02-26 11:00:00` | AKO, CH0081, CHINATSU, FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_004_10042030.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:005` | `10042040` | `2025-02-26 11:00:00` | AKO, CH0081, CHINATSU, FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_005_10042040.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:006` | `10042050` | `2025-02-26 11:00:00` | CH0081, CHINATSU, FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_006_10042050.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:007` | `10042055` | `2025-02-26 11:00:00` | CH0081, CHINATSU, FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_007_10042055.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:008` | `10042060` | `2025-02-26 11:00:00` | AKO, CH0081, CHINATSU, FUUKA, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_008_10042060.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:009` | `10042070` | `2025-02-26 11:00:00` | AKO, CH0081, CHINATSU, FUUKA, HINA, IORI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_009_10042070.md` | `INVENTORIED` |
| `EVENT_844` | `BA:event:844:010` | `10042080` | `2025-02-26 11:00:00` | AKO, CH0081, CHINATSU, FUUKA, HARUNA, HINA, IORI, JURI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_844/EPISODE_010_10042080.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:001` | `10043005` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_001_10043005.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:002` | `10043010` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_002_10043010.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:003` | `10043020` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_003_10043020.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:004` | `10043025` | `2025-03-26 11:00:00` | SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_004_10043025.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:005` | `10043030` | `2025-03-26 11:00:00` | CH0245 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_005_10043030.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:006` | `10043040` | `2025-03-26 11:00:00` | CH0245, HANAE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_006_10043040.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:007` | `10043050` | `2025-03-26 11:00:00` | CH0245, HANAE, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_007_10043050.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:008` | `10043060` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_008_10043060.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:009` | `10043070` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_009_10043070.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:010` | `10043075` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_010_10043075.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:011` | `10043080` | `2025-03-26 11:00:00` | CH0245, HANAE, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_011_10043080.md` | `INVENTORIED` |
| `EVENT_845` | `BA:event:845:012` | `10043090` | `2025-03-26 11:00:00` | CH0245, SUMIRE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_845/EPISODE_012_10043090.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:001` | `10044005` | `2025-04-22 11:00:00` | CH0242, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_001_10044005.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:002` | `10044010` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_002_10044010.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:003` | `10044020` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_003_10044020.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:004` | `10044030` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_004_10044030.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:005` | `10044040` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_005_10044040.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:006` | `10044050` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_006_10044050.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:007` | `10044055` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_007_10044055.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:008` | `10044060` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_008_10044060.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:009` | `10044070` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_009_10044070.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:010` | `10044075` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_010_10044075.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:011` | `10044080` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_011_10044080.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:012` | `10044090` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_012_10044090.md` | `INVENTORIED` |
| `EVENT_846` | `BA:event:846:013` | `10044100` | `2025-04-22 11:00:00` | CH0242, CH0243, CH0288 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_846/EPISODE_013_10044100.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:001` | `10045005` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_001_10045005.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:002` | `10045010` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_002_10045010.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:003` | `10045020` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_003_10045020.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:004` | `10045025` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_004_10045025.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:005` | `10045030` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_005_10045030.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:006` | `10045040` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, CHISE, IZUNA, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_006_10045040.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:007` | `10045050` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_007_10045050.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:008` | `10045060` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, MIMORI, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_008_10045060.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:009` | `10045070` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_009_10045070.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:010` | `10045080` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, CHISE, IZUNA, MIMORI, SHIZUKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_010_10045080.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:011` | `10045090` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_011_10045090.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:012` | `10045100` | `2025-06-25 11:00:00` | CH0107, CH0113, CH0114, CH0161, CH0222, CH0224, CH0225, CHISE, IZUNA, SHIZUKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_012_10045100.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:013` | `10045105` | `2025-06-25 11:00:00` | CH0224, CH0225, SHIZUKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_013_10045105.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:014` | `10045110` | `2025-06-25 11:00:00` | CH0161, CH0222, CH0224, CH0225, SHIZUKO, WAKAMO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_014_10045110.md` | `INVENTORIED` |
| `EVENT_847` | `BA:event:847:015` | `10045120` | `2025-06-25 11:00:00` | CH0110, CH0161, CH0222, CH0224, CH0225, IZUNA, MIMORI, PINA, SHIZUKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_847/EPISODE_015_10045120.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:001` | `10046005` | `2025-07-22 11:00:00` | CH0071, CH0089, HASUMI, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_001_10046005.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:002` | `10046010` | `2025-07-22 11:00:00` | CH0069, CH0070, CH0071, HASUMI, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_002_10046010.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:003` | `10046020` | `2025-07-22 11:00:00` | CH0069, CH0071, CH0088, HASUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_003_10046020.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:004` | `10046025` | `2025-07-22 11:00:00` | CH0069, CH0071, CH0089, HASUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_004_10046025.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:005` | `10046030` | `2025-07-22 11:00:00` | CH0069, CH0070, CH0071, HARUNA, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_005_10046030.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:006` | `10046040` | `2025-07-22 11:00:00` | AKARI, CH0069, CH0070, CH0071, HARUNA, HASUMI, IZUMI, NAGISA, ZUNKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_006_10046040.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:007` | `10046050` | `2025-07-22 11:00:00` | CH0069, CH0070, CH0071, HASUMI, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_007_10046050.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:008` | `10046060` | `2025-07-22 11:00:00` | CH0069, CH0071, CH0088, CH0089 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_008_10046060.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:009` | `10046070` | `2025-07-22 11:00:00` | CH0069, CH0070, CH0071, CH0088, CH0089, HASUMI, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_009_10046070.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:010` | `10046080,10046085` | `2025-07-22 11:00:00` | CH0069, CH0070, HASUMI, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_010_10046080.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:011` | `10046090` | `2025-07-22 11:00:00` | CH0069, CH0070, CH0071, CH0088, CH0089, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_011_10046090.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:012` | `10046100` | `2025-07-22 11:00:00` | AKARI, CH0071, CH0088, CH0089, HARUNA, NAGISA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_012_10046100.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:013` | `10046110` | `2025-07-22 11:00:00` | CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_013_10046110.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:014` | `10046120` | `2025-07-22 11:00:00` | CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_014_10046120.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:015` | `10046130` | `2025-07-22 11:00:00` | CH0071, HASUMI | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_015_10046130.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:016` | `10046140` | `2025-07-22 11:00:00` | CH0071, NAGISA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_016_10046140.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:017` | `10046150` | `2025-07-22 11:00:00` | CH0069, CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_017_10046150.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:018` | `10046160` | `2025-07-22 11:00:00` | CH0070, CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_018_10046160.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:019` | `10046170` | `2025-07-22 11:00:00` | AZUSA, CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_019_10046170.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:020` | `10046180` | `2025-07-22 11:00:00` | CH0071, HANAKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_020_10046180.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:021` | `10046190` | `2025-07-22 11:00:00` | CH0071, TSURUGI | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_021_10046190.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:022` | `10046200` | `2025-07-22 11:00:00` | CH0071, IORI | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_022_10046200.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:023` | `10046210` | `2025-07-22 11:00:00` | CH0071, HINA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_023_10046210.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:024` | `10046220` | `2025-07-22 11:00:00` | CH0071, HIHUMI | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_024_10046220.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:025` | `10046230` | `2025-07-22 11:00:00` | CH0071, KOHARU | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_025_10046230.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:026` | `10046240` | `2025-07-22 11:00:00` | CH0071, MASHIRO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_026_10046240.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:027` | `10046250` | `2025-07-22 11:00:00` | CH0071, SHIZUKO | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_027_10046250.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:028` | `10046260` | `2025-07-22 11:00:00` | CH0071, IZUNA | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_028_10046260.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:029` | `10046270` | `2025-07-22 11:00:00` | CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_029_10046270.md` | `INVENTORIED` |
| `EVENT_848` | `BA:event:848:030` | `10046280` | `2025-07-22 11:00:00` | CH0071 | 2 | `02_CANONICAL_STORIES/EVENT/EVENT_848/EPISODE_030_10046280.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:001` | `10047005` | `2025-08-20 11:00:00` | CH0304 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_001_10047005.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:002` | `10047010` | `2025-08-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_002_10047010.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:003` | `10047020` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_003_10047020.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:004` | `10047030` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_004_10047030.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:005` | `10047040` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_005_10047040.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:006` | `10047050` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_006_10047050.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:007` | `10047060` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_007_10047060.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:008` | `10047070` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_008_10047070.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:009` | `10047080` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306, CH0317 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_009_10047080.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:010` | `10047090` | `2025-08-20 11:00:00` | CH0304, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_010_10047090.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:011` | `10047095` | `2025-08-20 11:00:00` | CH0304, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_011_10047095.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:012` | `10047100` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_012_10047100.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:013` | `10047105` | `2025-08-20 11:00:00` | CH0304, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_013_10047105.md` | `INVENTORIED` |
| `EVENT_849` | `BA:event:849:014` | `10047110` | `2025-08-20 11:00:00` | CH0304, CH0305, CH0306 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_849/EPISODE_014_10047110.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:001` | `10048005` | `2025-09-24 11:00:00` | CH0317 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_001_10048005.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:002` | `10048010` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_002_10048010.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:003` | `10048020` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_003_10048020.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:004` | `10048030` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_004_10048030.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:005` | `10048040` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_005_10048040.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:006` | `10048050` | `2025-09-24 11:00:00` | CH0304, CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_006_10048050.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:007` | `10048060` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_007_10048060.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:008` | `10048070` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_008_10048070.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:009` | `10048080` | `2025-09-24 11:00:00` | CH0317, CH0318 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_009_10048080.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:010` | `10048090` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_010_10048090.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:011` | `10048100` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_011_10048100.md` | `INVENTORIED` |
| `EVENT_850` | `BA:event:850:012` | `10048110` | `2025-09-24 11:00:00` | CH0317, CH0318, CH0319 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_850/EPISODE_012_10048110.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:001` | `10049005` | `2025-10-22 11:00:00` | CH0166, CH0167, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_001_10049005.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:002` | `10049010` | `2025-10-22 11:00:00` | SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_002_10049010.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:003` | `10049020` | `2025-10-22 11:00:00` | CH0167, HASUMI, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_003_10049020.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:004` | `10049030` | `2025-10-22 11:00:00` | CH0167, MASHIRO, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_004_10049030.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:005` | `10049040` | `2025-10-22 11:00:00` | CH0167, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_005_10049040.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:006` | `10049050` | `2025-10-22 11:00:00` | CH0166, CH0167, MASHIRO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_006_10049050.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:007` | `10049055` | `2025-10-22 11:00:00` | CH0166, CH0167, MASHIRO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_007_10049055.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:008` | `10049060` | `2025-10-22 11:00:00` | CH0167, MASHIRO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_008_10049060.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:009` | `10049070` | `2025-10-22 11:00:00` | CH0166, CH0167, MASHIRO, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_009_10049070.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:010` | `10049075` | `2025-10-22 11:00:00` | CH0166, CH0167, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_010_10049075.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:011` | `10049080` | `2025-10-22 11:00:00` | CH0166, CH0167, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_011_10049080.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:012` | `10049090` | `2025-10-22 11:00:00` | CH0166, CH0167, MASHIRO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_012_10049090.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:013` | `10049100` | `2025-10-22 11:00:00` | CH0166, CH0167, MASHIRO, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_013_10049100.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:014` | `10049110` | `2025-10-22 11:00:00` | CH0166, CH0167, SHIMIKO, SUZUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_014_10049110.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:015` | `10049120` | `2025-10-22 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_015_10049120.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:016` | `10049130` | `2025-10-22 11:00:00` | CH0166 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_016_10049130.md` | `INVENTORIED` |
| `EVENT_851` | `BA:event:851:017` | `10049140` | `2025-10-22 11:00:00` | CH0169, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_851/EPISODE_017_10049140.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:001` | `10050005` | `2025-11-19 11:00:00` | CH0124, CH0228, CH0229, MOMIJI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_001_10050005.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:002` | `10050010` | `2025-11-19 11:00:00` | CH0228, CH0229, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_002_10050010.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:003` | `10050020` | `2025-11-19 11:00:00` | CH0069, NAGISA, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_003_10050020.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:004` | `10050030` | `2025-11-19 11:00:00` | CH0124, CH0228, CH0229, MASHIRO, MOMIJI, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_004_10050030.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:005` | `10050040` | `2025-11-19 11:00:00` | CH0228, CH0229, KOHARU, MASHIRO, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_005_10050040.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:006` | `10050050` | `2025-11-19 11:00:00` | CH0124, CH0228, CH0229, KOHARU, MASHIRO, NAGISA, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_006_10050050.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:007` | `10050060` | `2025-11-19 11:00:00` | CH0169, CH0228, CH0229, MASHIRO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_007_10050060.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:008` | `10050070` | `2025-11-19 11:00:00` | CH0169, CH0228, CH0229, KOHARU | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_008_10050070.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:009` | `10050080` | `2025-11-19 11:00:00` | CH0169, CH0228, CH0229, KOHARU, MASHIRO, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_009_10050080.md` | `INVENTORIED` |
| `EVENT_852` | `BA:event:852:010` | `10050090` | `2025-11-19 11:00:00` | CH0069, CH0070, CH0228, CH0229, CHERINO, MASHIRO, NAGISA, SHIMIKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_852/EPISODE_010_10050090.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:001` | `10051005` | `2025-12-24 11:00:00` | CH0109, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_001_10051005.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:002` | `10051010` | `2025-12-24 11:00:00` | CH0109, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_002_10051010.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:003` | `10051020` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_003_10051020.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:004` | `10051030` | `2025-12-24 11:00:00` | CH0109, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_004_10051030.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:005` | `10051040` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_005_10051040.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:006` | `10051045` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_006_10051045.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:007` | `10051050` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_007_10051050.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:008` | `10051060` | `2025-12-24 11:00:00` | ATSUKO, CH0113, CH0114, HIYORI, IZUNA, MISAKI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_008_10051060.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:009` | `10051070` | `2025-12-24 11:00:00` | CH0109, CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_009_10051070.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:010` | `10051080` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_010_10051080.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:011` | `10051090` | `2025-12-24 11:00:00` | CH0109, CH0113, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_011_10051090.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:012` | `10051100` | `2025-12-24 11:00:00` | CH0113, CH0114, IZUNA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_012_10051100.md` | `INVENTORIED` |
| `EVENT_853` | `BA:event:853:013` | `10051110` | `2025-12-24 11:00:00` | CH0113, CH0114 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_853/EPISODE_013_10051110.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:001` | `10052010` | `2026-01-20 11:00:00` | CH0158, CH0159, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_001_10052010.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:002` | `10052015` | `2026-01-20 11:00:00` | CH0159, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_002_10052015.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:003` | `10052020` | `2026-01-20 11:00:00` | CH0158, CH0159, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_003_10052020.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:004` | `10052030` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_004_10052030.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:005` | `10052040` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_005_10052040.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:006` | `10052050` | `2026-01-20 11:00:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_006_10052050.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:007` | `10052055` | `2026-01-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_007_10052055.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:008` | `10052060` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_008_10052060.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:009` | `10052065` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_009_10052065.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:010` | `10052070` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_010_10052070.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:011` | `10052075` | `2026-01-20 11:00:00` | ARIS, CH0159, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_011_10052075.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:012` | `10052080` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_012_10052080.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:013` | `10052090` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0187 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_013_10052090.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:014` | `10052095` | `2026-01-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_014_10052095.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:015` | `10052100` | `2026-01-20 11:00:00` | CH0159, CH0187 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_015_10052100.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:016` | `10052105` | `2026-01-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_016_10052105.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:017` | `10052110` | `2026-01-20 11:00:00` | ARIS | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_017_10052110.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:018` | `10052115` | `2026-01-20 11:00:00` | ARIS | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_018_10052115.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:019` | `10052120` | `2026-01-20 11:00:00` | ARIS | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_019_10052120.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:020` | `10052130` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_020_10052130.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:021` | `10052135` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, MIDORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_021_10052135.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:022` | `10052140` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_022_10052140.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:023` | `10052150,10052153,10052155` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_023_10052150.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:024` | `10052160` | `2026-01-20 11:00:00` | CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_024_10052160.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:025` | `10052170` | `2026-01-20 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_025_10052170.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:026` | `10052175` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_026_10052175.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:027` | `10052180` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_027_10052180.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:028` | `10052190` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0187 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_028_10052190.md` | `INVENTORIED` |
| `EVENT_854` | `BA:event:854:029` | `10052195` | `2026-01-20 11:00:00` | ARIS, CH0158, CH0159, CH0187, MIDORI, MOMOI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_854/EPISODE_029_10052195.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:001` | `10053005` | `2026-03-18 11:00:00` | CH0264 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_001_10053005.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:002` | `10053010` | `2026-03-18 11:00:00` | CH0170, CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_002_10053010.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:003` | `10053020` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_003_10053020.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:004` | `10053030` | `2026-03-18 11:00:00` | CH0170, CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_004_10053030.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:005` | `10053040` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_005_10053040.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:006` | `10053050` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_006_10053050.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:007` | `10053060` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_007_10053060.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:008` | `10053070` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_008_10053070.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:009` | `10053080` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_009_10053080.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:010` | `10053085` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_010_10053085.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:011` | `10053090` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_011_10053090.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:012` | `10053100` | `2026-03-18 11:00:00` | CH0264, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_012_10053100.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:013` | `10053110` | `2026-03-18 11:00:00` | CH0264, CH0304, CH0305 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_013_10053110.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:014` | `10053120` | `2026-03-18 11:00:00` | CH0159 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_014_10053120.md` | `INVENTORIED` |
| `EVENT_856` | `BA:event:856:015` | `10053130` | `2026-03-18 11:00:00` | CH0170 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_856/EPISODE_015_10053130.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:001` | `10054005` | `2026-06-24 11:00:00` | CH0135, REIZYO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_001_10054005.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:002` | `10054010` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, REIZYO, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_002_10054010.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:003` | `10054020` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, REIZYO, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_003_10054020.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:004` | `10054030` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_004_10054030.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:005` | `10054040` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_005_10054040.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:006` | `10054050` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_006_10054050.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:007` | `10054060` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, CH0355 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_007_10054060.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:008` | `10054070` | `2026-06-24 11:00:00` | CH0139, CH0355 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_008_10054070.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:009` | `10054080` | `2026-06-24 11:00:00` | CH0139, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_009_10054080.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:010` | `10054090` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, CH0355 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_010_10054090.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:011` | `10054095` | `2026-06-24 11:00:00` | CH0088, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_011_10054095.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:012` | `10054100` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_012_10054100.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:013` | `10054110` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, SAYA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_013_10054110.md` | `INVENTORIED` |
| `EVENT_859` | `BA:event:859:014` | `10054120` | `2026-06-24 11:00:00` | CH0135, CH0137, CH0138, CH0139, SHUN | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_859/EPISODE_014_10054120.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:001` | `10055005` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_001_10055005.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:002` | `10055010` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_002_10055010.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:003` | `10055020` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_003_10055020.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:004` | `10055030` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_004_10055030.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:005` | `10055040` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_005_10055040.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:006` | `10055050` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_006_10055050.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:007` | `10055060` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_007_10055060.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:008` | `10055070` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_008_10055070.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:009` | `10055080` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_009_10055080.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:010` | `10055085` | `2026-07-29 11:00:00` | CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_010_10055085.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:011` | `10055090,10055095` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_011_10055090.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:012` | `10055100` | `2026-07-29 11:00:00` | CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_012_10055100.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:013` | `10055110` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_013_10055110.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:014` | `10055120` | `2026-07-29 11:00:00` | CH0079, CH0080, CH0156 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_014_10055120.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:015` | `10055130` | `2026-07-29 11:00:00` | HINA, IORI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_015_10055130.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:016` | `10055140` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_016_10055140.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:017` | `10055150` | `2026-07-29 11:00:00` | AYANE, CH0077, CH0079, CH0080, CH0156, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_017_10055150.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:018` | `10055155` | `2026-07-29 11:00:00` | AYANE, CH0077, CH0079, CH0156, CH0238, HOSHINO, NONOMI, SERIKA, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_018_10055155.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:019` | `10055160` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0170, CH0238, CH0264 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_019_10055160.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:020` | `10055165` | `2026-07-29 11:00:00` | CH0079, CH0156, CH0170, CH0238, CH0264 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_020_10055165.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:021` | `10055170` | `2026-07-29 11:00:00` | CH0077, CH0080, CH0107, CH0109, CH0156, CHISE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_021_10055170.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:022` | `10055175` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0107, CH0109, CH0156, CH0238, CHISE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_022_10055175.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:023` | `10055180` | `2026-07-29 11:00:00` | CH0069, CH0070, CH0077, CH0079, CH0080, CH0156, CH0238, HIHUMI, NAGISA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_023_10055180.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:024` | `10055185` | `2026-07-29 11:00:00` | CH0069, CH0070, CH0077, CH0079, CH0156, CH0238, HIHUMI | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_024_10055185.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:025` | `10055190` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, CH0238, CHERINO, TOMOE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_025_10055190.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:026` | `10055195` | `2026-07-29 11:00:00` | CH0077, CH0079, CH0080, CH0156, HOSHINO, SERIKA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_026_10055195.md` | `INVENTORIED` |
| `EVENT_860` | `BA:event:860:027` | `10055200` | `2026-07-29 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_860/EPISODE_027_10055200.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:001` | `10056005` | `2026-08-26 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_001_10056005.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:002` | `10056010` | `2026-08-26 11:00:00` | — | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_002_10056010.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:003` | `10056020` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_003_10056020.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:004` | `10056030` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_004_10056030.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:005` | `10056040` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_005_10056040.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:006` | `10056050` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_006_10056050.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:007` | `10056060` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_007_10056060.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:008` | `10056070` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_008_10056070.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:009` | `10056080` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_009_10056080.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:010` | `10056090` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_010_10056090.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:011` | `10056100` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_011_10056100.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:012` | `10056105` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_012_10056105.md` | `INVENTORIED` |
| `EVENT_861` | `BA:event:861:013` | `10056110` | `2026-08-26 11:00:00` | CH0368, CH0369 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_861/EPISODE_013_10056110.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:001` | `10057005` | `2026-09-23 11:00:00` | SERINA | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_001_10057005.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:002` | `10057010` | `2026-09-23 11:00:00` | CH0320, CH0321, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_002_10057010.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:003` | `10057020` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_003_10057020.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:004` | `10057030` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_004_10057030.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:005` | `10057040` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_005_10057040.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:006` | `10057050` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_006_10057050.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:007` | `10057060` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_007_10057060.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:008` | `10057070` | `2026-09-23 11:00:00` | CH0320, CH0321, CHERINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_008_10057070.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:009` | `10057080` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_009_10057080.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:010` | `10057090` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_010_10057090.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:011` | `10057100` | `2026-09-23 11:00:00` | CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_011_10057100.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:012` | `10057110` | `2026-09-23 11:00:00` | CH0238, CH0320, CH0321, CHERINO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_012_10057110.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:013` | `10057120` | `2026-09-23 11:00:00` | CH0214, CH0320, CH0321, NODOKA, SHIGURE | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_013_10057120.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:014` | `10057130` | `2026-09-23 11:00:00` | CH0079, CH0156, CH0320, CH0321 | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_014_10057130.md` | `INVENTORIED` |
| `EVENT_862` | `BA:event:862:015` | `10057140` | `2026-09-23 11:00:00` | CH0320, CH0321, SHIROKO | 1 | `02_CANONICAL_STORIES/EVENT/EVENT_862/EPISODE_015_10057140.md` | `INVENTORIED` |


## 4. Update and admission rule

When a complete event reading is accepted, update the exact episode rows, package-level question and assessed priority, and route resulting state/relationship/ordinary-life claims to the seven ledgers and subject coverage index as warranted. Record chronology confidence and competing interpretations in the [source-class crosswalk](BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md) and [gap register](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md). A finding of no durable change is still a literary result and may establish preference, pleasure, humor, routine, care or a negative constraint. Reconcile inventory against the pinned `stories.jsonl` before any source refresh; additions receive `UNASSESSED` rather than inheriting a prior event's priority.

## Current content review and independent rotation — 2026-10-01

[Cycles001–005](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) accept **4 complete packages /43 event objects**, leaving **57 packages /967 objects** for complete review. All remaining objects retain eligibility. Initial intake prose above records the selection basis; the current rows and the [supplemental object crosswalk](BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv) own actual workflow.

| Package | Grounded priority / function | Accepted scope and limits |
|---|---|---|
| EVENT816 all 17 | CORE Kazusa/Reisa/Sweets Club; HIGH Suzumi. Café warmth, heterogeneous pleasures, attachment, privacy, listening and care errors. | Event-local repertoire and conditional mechanisms; E017 prevents permanent-cure inference; tag, health and main-chronology limits retained. |
| EVENT80000 all 9 | CORE E119 Shiroko visitor/E125 Rio; HIGH other 7. Independent gift craft, preferences, written voice and directed care. | Person-specific ordinary encounters; no fabricated shared plot, title, exact variant, public accountability repair or magical/legal/medical mechanism. |
| EVENT807 all1 | HIGH; public joy, unfamiliar embodiment, music/rhythm limits and invitation. | Complete rehearsal; secure full-name identity, empty join preserved, no actual attended concert, audio or main chronology. |
| EVENT814 all16 | CORE; chosen play/rest/gifts, peer cooperation/friction, resource and authority distinctions. | Complete quiet and conflict scenes; gaze/sleep/pressure and coerced return limits preserved; title, speaker, generic-role, outcome and chronology controls retained. |

Next independent rotation is EVENT80001 all16; its complete candidate still requires parent review and reconciliation. EVENT814 all16 is now accepted as the inquiry-led Abydos comparison. Quiet material is fully inspected within its complete packet and retained as affirmative literary evidence; no stakes filter or one-scene ceiling is applied.
