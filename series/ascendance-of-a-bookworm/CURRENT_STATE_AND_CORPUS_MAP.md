---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_BOOTSTRAP
source_boundary: "Japanese-language light-novel EPUB corpus: numbered main Volumes 01-33 plus acquired Royal Academy Stories: First Year side-story volume; source audit dated 2026-08-30"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm — current state and corpus map

This is the canonical first read for the Git-side *Ascendance of a Bookworm* (Japanese: `本好きの下剋上～司書になるためには手段を選んでいられません～`) analytical corpus.

## Authority split

- **GitHub `main` is the analytical authority after this bootstrap merges.** Interpretive claims, methods, sequential readings, longitudinal ledgers, character work, syntheses, and analytical audits belong under `series/ascendance-of-a-bookworm/`.
- **Google Drive is the primary-source authority.** The Japanese EPUBs and their integrity/audit manifest remain in the governed primary-source Drive plane and are not copied into Git.
- **Local/Codex workspaces are working environments**, not authority unless an artifact is promoted through the governed Drive-evidence or Git-analysis route.

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Bookworm source folder: `1jijErFCqkxFfP1C8s5SJkaphiImF_vvJ`  
Source audit manifest: `1EWZLfUcopzCJT3iCZmCElOnq0jFUWgL0`  
Audited manifest SHA-256: `034f01acae4e14f58ad8f9ea925ef00813603c74b590f08c8ba4e628db147d82`

See `01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md` before any source-facing analysis.

## Current analytical state

**Bootstrap only. No volume deep reading, longitudinal ledger, character monograph, relationship synthesis, specialist synthesis, or full-series synthesis is yet canonical in this root.**

The source corpus is acquired and integrity-audited, but possession is not interpretation. This bootstrap deliberately does not promote synopsis knowledge, adaptation knowledge, fandom consensus, prior ChatGPT discussion, or general model knowledge into findings about the protagonist, other characters, institutions, social order, religion, magic/system mechanics, politics, economics, or themes.

The first analytical operation should therefore be a Japanese-primary reading of main Volume 01 under the method defined here, not a whole-series synthesis assembled from remembered plot knowledge.

## Locked source boundary

The current audit records **34 Japanese EPUB objects**:

- **33 numbered main volumes**, Volume 01 through Volume 33, with no gaps;
- **one side-story volume**, *Royal Academy Stories: First Year*;
- no byte-identical duplicate groups.

The Japanese source filenames encode the five-part numbered-main-series structure:

| Part | Japanese part title | Numbered volumes in this lock |
|---|---|---:|
| Part 1 | `第一部「兵士の娘」` | V01-V03 |
| Part 2 | `第二部「神殿の巫女見習い」` | V04-V07 |
| Part 3 | `第三部「領主の養女」` | V08-V12 |
| Part 4 | `第四部「貴族院の自称図書委員」` | V13-V21 |
| Part 5 | `第五部「女神の化身」` | V22-V33 |

The normalized English filenames are routing conveniences; the Japanese prose remains the semantic anchor.

This lock does **not** claim exhaustive possession of every adaptation, fanbook, web-publication witness, retailer-exclusive bonus, short story, or other supplemental item that may exist. Such material remains outside the analytical boundary until separately acquired, identified, audited, and intentionally integrated.

## Governing method

Read in this order for new Bookworm analytical work:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/BOOKWORM_ANALYTICAL_METHOD.md`
3. `01 Source Lock and Inventory/BOOKWORM_SOURCE_LOCK_AND_INVENTORY.md`
4. the relevant frozen sequential reading(s), once they exist;
5. only the longitudinal, character, or specialist artifact needed for the task.

The current project is **Japanese-light-novel primary**. Anime, manga, translated editions, production interviews, reception research, reference books, or other versions may later become separately labeled witnesses. They do not silently modify the locked source boundary or overwrite Japanese-primary findings.

## Corpus architecture

| Layer | Analytical responsibility | Bootstrap state |
|---|---|---|
| `00 Frameworks and Methods` | Governing evidence, focalization, prospective-freeze, identity/state, system-inference, and comparison rules | populated; canonical V0.1 |
| `01 Source Lock and Inventory` | Exact acquired-source boundary, integrity state, part routing, and Drive provenance | populated; canonical V0.1 |
| `02 Sequential Readings` | Volume-by-volume prospective deep readings | contract present; no readings yet |
| `03 Longitudinal Ledgers` | Recurring cross-volume state, relationship, institution, knowledge-transfer, and thematic tracking | routing contract present; no ledgers yet |
| `04 Character Analysis` | Character syntheses created only after evidence warrants them | routing contract present; no monographs yet |
| `05 Specialist Synthesis` | Dense recurring questions with independent analytical responsibility | not instantiated |
| `06 Full-Series Synthesis` | Source-bound integrated synthesis after adequate sequential coverage | not instantiated |
| `07 Evidence and Indexes` | Git-side claim/evidence routing if later needed | not instantiated; source lock is sufficient at bootstrap |
| `08 Audits and Manifests` | Bootstrap inventory and path-integrity records | populated |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of a directory is intentional. Do not create empty categories merely to make Bookworm resemble another project.

## Initial analytical questions — not findings

The sequential pass should test, rather than assume, questions including:

- how the protagonist's priorities, self-conception, and practical goals change when circumstances, roles, obligations, and available agency change;
- what remains continuous and what changes when names, titles, social roles, affiliations, or legal/institutional positions change;
- how imported knowledge is remembered, translated into local practice, constrained by materials and institutions, and altered by unintended consequences;
- how literacy, books, production, labor, commerce, education, religion, law, and political authority are represented as interacting systems rather than isolated worldbuilding facts;
- how changes in social position reshape power, responsibility, dependence, empathy, blind spots, and the kinds of refusal available to a character;
- when a focal character's explanation of the world is reliable, incomplete, self-serving, culturally bounded, or contradicted by alternate viewpoints and later evidence;
- how family, attachment, separation, friendship, patronage, service, mentorship, rivalry, and obligation change across long time horizons;
- how bodily limits, risk, competence, institutional privilege, and information asymmetry alter nominal choice and practical autonomy;
- how divine, religious, magical, legal, or political claims should be separated into what characters believe, what institutions teach, what events establish, and what remains unresolved;
- where ordinary routines, preferences, work habits, etiquette, gifts, leisure, discomfort, and small choices reveal character more reliably than explicit self-description.

Comparisons to other isekai/fantasy works or to titles already in this repository are downstream operations. They must not become templates imposed on the Bookworm text before its own evidence is read.

## Initial work order

1. Produce `02 Sequential Readings/BOOKWORM_V01_DEEP_READING.md` from the Japanese Volume 01 source.
2. Freeze the Volume 01 reading and its bounded expectations/open questions before opening Volume 02 for analysis.
3. Continue the numbered main volumes prospectively. Preserve global numbering V01-V33 while recording the part and part-volume identity encoded by the Japanese source metadata.
4. At each part boundary, permit a checkpoint synthesis only after the final volume of that part freezes. A checkpoint may update the current model but cannot rewrite the historical state of earlier volume freezes.
5. Keep *Royal Academy Stories: First Year* outside the numbered prospective chain until its publication/diegetic relationship and appropriate insertion boundary are explicitly verified. When integrated, record whether it confirms, extends, complicates, or revises prior interpretations without retroactively contaminating earlier predictions.
6. Instantiate longitudinal ledgers only when a responsibility recurs often enough that retrieval from separate volume files becomes unreliable.
7. Create character monographs only after sufficient longitudinal evidence exists; do not pre-create character directories from cast lists.
8. Treat any later adaptation or translation pass as a distinct witness unless a future source-lock revision explicitly expands the governing boundary.

## Bootstrap abstentions

- No character personality, relationship, political, ethical, religious, or thematic claim is canonical merely because it appears in a synopsis, marketing copy, adaptation, fandom discussion, wiki, or earlier conversation.
- A narrator's belief is not automatically a setting fact. Keep focalized interpretation distinct from independently corroborated world-model claims.
- Later titles, roles, identities, or institutional knowledge must not be projected backward into earlier source boundaries as though the earlier text already established them.
- No supplemental story is silently inserted into the numbered prospective chain without a verified source-placement decision.
- No translation is treated as the semantic anchor when the Japanese primary source is available for the question.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- No later volume is allowed to erase the record of what an earlier prospective reading reasonably supported at the time.
