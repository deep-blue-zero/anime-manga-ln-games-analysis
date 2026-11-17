---
title: "Year 2 volume-by-volume evidence ledger"
series: COTE
artifact_type: evidence_router
architecture_slot: Y2_12
scope: Y2_EVIDENCE_ROUTING
generation: V2
version: "1.0"
status: canonical
authority_state: canonical
snapshot_boundary: Y2SL
source_boundary: "Frozen Year 1 through First File; Year 2 through Y2SL; Volume 0 after Y2V08"
spoiler_boundary: "through Y2SL only; Year 3 narrative evidence excluded"
source_language: Japanese
method: COTE_Y2_ANALYTICAL_METHOD_V2.md
architecture: COTE_Multi_Document_Synthesis_Architecture_v1.md
corpus_entrypoint: COTE_Y2_00_README_AND_CORPUS_MAP.md
supersedes: []
superseded_by: []
source_local_artifacts_immutable: true
year3_information_used: false
do_not_use_as_current_authority: false
created_at: "2026-09-09"
updated_at: "2026-09-09"
---

# Year 2 — evidence routes into the locked Japanese sources

## 1. Responsibility and reading procedure

This index owns retrieval, not a second set of findings. Its route is **synthesis claim → responsible specialist/ledger → canonical volume artifact → existing evidence ID → original locator → hash-locked Japanese source**. The table below gives the year-level map; the complete machine-readable companion preserves all **2,697** owned evidence rows from the sixteen fiction/prequel readings and the Second List audit. No new source evidence IDs are minted.

1. Choose the claim's primary home in section 4. Read its qualification and counterevidence before selecting a passage.
2. Open the volume artifact linked in section 2; retrieve the original evidence row by ID. Its evidence type and confidence remain authoritative.
3. Find that same ID in [COTE_Y2_EVIDENCE_INDEX.json](../04%20Source%20Maps%20and%20Support/COTE_Y2_EVIDENCE_INDEX.json). `original_locator` is preserved verbatim; `artifact_line` is only a convenience at the artifact hash recorded in the source map. `resolved_targets` identifies the actual internal resource and paragraph bounds.
4. Use [COTE_Y2_SOURCE_LOCATOR_MAP.json](../04%20Source%20Maps%20and%20Support/COTE_Y2_SOURCE_LOCATOR_MAP.json) to verify the EPUB filename, byte size, SHA-256, canonical artifact hash, parser convention and OPF reading order. Open the independently held source; none of its prose or images is embedded in these JSON files.
5. Apply section 6's explicit correction overlays. The original record remains retrievable as a historical record, but its corrected error must not become a new current claim.

The [source lock](../04%20Source%20Maps%20and%20Support/COTE_Y2_SOURCE_INVENTORY_AND_LOCK.md) owns acquisition identity. [Y2_10](COTE_Y2_10_RETROSPECTIVE_PARATEXT_AND_REVISION.md) owns retrospective admissibility. An exact pointer proves where an assertion comes from; it does not promote a narrator's inference into event fact or make an institutional score exhaustive of a person.

## 2. Governed source order and volume-artifact map

The thesis column is a retrieval gloss of [Y2_01](COTE_Y2_01_YEAR_ARCHITECTURE_AND_VOLUME_PROGRESSION.md), not a replacement deep reading. Thread IDs are inherited controlled terms. Evidence selections are entry points into their owning sections; read the complete scene when evaluating a claim. “Later” below always ends at Y2SL.

| Source / owned IDs | Canonical artifact | Volume thesis / retrieval function | Major thread IDs | Key existing evidence IDs | Unresolved at that local boundary / later revision route |
|---|---|---|---|---|---|
| `Y2V01` / 69 | [COTE_Y2_V01_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V01_DEEP_READING.md) | Legibility creates markets and asymmetric exposure. | `JITSURYOKU; OAA_LEGIBILITY; HORIKITA_LEADERSHIP` | `E010, E019, E028, E037, E055` in `Y2V01` | Hidden operative and bounty knowledge remain local uncertainties. V02 reconstructs the knife route; V04/V07/V08 resolve distinct identity layers; V00 is not admissible here. |
| `Y2V02` / 98 | [COTE_Y2_V02_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V02_DEEP_READING.md) | Ability becomes binding through contracts, patronage and rescue prices. | `POINTS_POLITICAL_ECONOMY; STUDENT_COUNCIL; PROTECTION_OWNERSHIP` | `E015, E029, E043, E071, E085` in `Y2V02` | Tsukishiro intent and unseen authorship remain open. V04 tests competing jurisdictions; V09 discloses Nagumo patronage machinery. |
| `Y2V03` / 104 | [COTE_Y2_V03_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V03_DEEP_READING.md) | Records and visible events do not automatically establish causal authorship. | `TRUTH_PROOF_RECORD; SURVEILLANCE; WHITE_ROOM` | `E015, E029, E071, E085, E090` in `Y2V03` | Nanase receives a causal story; the source does not verify every premise. V04/V08 and the V00 retrospective ledger qualify that story. |
| `Y2V04` / 214 | [COTE_Y2_V04_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V04_DEEP_READING.md) | Overlapping plans reveal sovereignty limits and the value of independent provenance. | `ENVIRONMENTAL_AUTHORSHIP; RYUEN_FEAR_LEGITIMACY; HORIKITA_INDEPENDENCE` | `E001, E031, E091, E151, E162–E183` in `Y2V04` | Amasawa origin is revealed; Tsukishiro highest purpose remains unresolved. V07 identifies a different operative; V08 reopens intent rather than closing it. |
| `Y2V04.5` / 182 | [COTE_Y2_V04_5_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V04_5_DEEP_READING.md) | Ordinary embeddedness supplies meaning and leverage beyond formal scores. | `AYANOKOJI_ORDINARY_LIFE; RELATIONSHIP_RECIPROCITY; KOENJI_AUTONOMY` | `E001, E027, E053, E105, E131` in `Y2V04_5` | Romantic behavior and reciprocal knowledge are not equivalent. V09.5 audits felt desire; V12.5 tests actual separation; SL fiction occupies earlier scene-time. |
| `Y2V05` / 160 | [COTE_Y2_V05_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V05_DEEP_READING.md) | Independent judgment and ethical harm coexist under collective sacrifice. | `HORIKITA_INDEPENDENCE; EXPULSION_DISPOSABILITY; CLASS_CONSTITUTIONS` | `E001, E023, E067, E089, E111, E133` in `Y2V05` | Preserving Kushida transfers the cost to another person. V06/V07 show afterlives without retroactively legitimating the original coercion. |
| `Y2V06` / 180 | [COTE_Y2_V06_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V06_DEEP_READING.md) | The wounded class redistributes agency while succession becomes a project. | `KUSHIDA_INTEGRATION; SUDO_DEVELOPMENT; SUCCESSION_SEPARATION` | `E001, E051, E076, E101, E126, E151` in `Y2V06` | Operational absence does not prove independence from environmental authorship. V07 and V12.5 distinguish staged autonomy from the future durability test. |
| `Y2V07` / 168 | [COTE_Y2_V07_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V07_DEEP_READING.md) | Independent motives can converge within a hidden author's prepared setting. | `ENVIRONMENTAL_AUTHORSHIP; TRUTH_PROOF_RECORD; ICHINOSE_SOLIDARITY` | `E025, E049, E073, E094–E105, E113–E154` in `Y2V07` | Successful convergence is not omnipotence; the caller and adult authorization claims have different certainty. V08 identifies Ishigami; V00 adds genealogy. |
| `Y2V08` / 168 | [COTE_Y2_V08_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V08_DEEP_READING.md) | Relational knowledge exceeds scores while becoming usable political information. | `RELATIONSHIP_RECIPROCITY; OAA_LEGIBILITY; WHITE_ROOM` | `E001, E009, E057, E113, E145–E148, E162` in `Y2V08` | Pre-V00 hypotheses about Nanase, Tsukishiro and admission remain frozen as hypotheses. V00 is admitted next; Y2_10 owns the restricted revision. |
| `V00` / 176 | [COTE_V00_RETROSPECTIVE_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_V00_RETROSPECTIVE_DEEP_READING.md) | Political genealogy explains authored opportunity without exhausting emergent purpose. | `NATIONAL_POLITICS; WHITE_ROOM; AYANOKOJI_FREEDOM` | `E001, E026, E051, E076, E126, E151` in `V00` | Prequel chronology is not reading priority. The retrospective-revelation ledger maps prior claims; neither school-entry design nor childhood capacity settles later motive or ethics. |
| `Y2V09` / 168 | [COTE_Y2_V09_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V09_DEEP_READING.md) | Development becomes visible when established models fail to predict new answers. | `SUDO_DEVELOPMENT; STUDENT_COUNCIL; ICHINOSE_SELF_WORTH` | `E001, E021–E044, E057, E105, E143, E159` in `Y2V09` | Nagumo succession and Ichinose growth have unequal institutional and ethical tests. V11 closes specific rivalry business; V12/12.5 intensify the stakes. |
| `Y2V09.5` / 176 | [COTE_Y2_V09_5_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V09_5_DEEP_READING.md) | Ordinary desire generates purposes not assigned by institutional optimization. | `ORDINARY_LIFE_COUNTER_CURRICULUM; KEI_DEPENDENCY_AUTONOMY; HIYORI_QUIET_AGENCY` | `E001, E044, E098, E117, E133, E175` in `Y2V09_5` | Romantic learning is not established love; quieter agency is not universal moral redirection. V10/V11 develop irreplaceability; V12.5 tests departure. |
| `Y2V10` / 180 | [COTE_Y2_V10_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V10_DEEP_READING.md) | Scarcity exposes whom leaders value and what their models omitted. | `SAKAYANAGI_RIVALRY_GENIUS; CLASS_CONSTITUTIONS; PROTECTION_OWNERSHIP` | `E001, E061, E150, E164` in `Y2V10` | Recognition after loss does not by itself repair succession. V11 permits grief and disclosure; V12/12.5 expose political costs of private priority. |
| `Y2V11` / 180 | [COTE_Y2_V11_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V11_DEEP_READING.md) | Recognition can create an opening and then relinquish the answer. | `AYANOKOJI_IRREPLACEABILITY; GENERATIVE_ABILITY; PROTECTION_OWNERSHIP` | `E001, E061, E121, E147–E156` in `Y2V11` | A local jurisdictional stopping rule is not a global conversion. V12 supplies an explicit contrasting intervention; Y2_08 compares the two. |
| `Y2V12` / 180 | [COTE_Y2_V12_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V12_DEEP_READING.md) | Relational knowledge can author outcomes even where direct command is absent. | `EXPULSION_DISPOSABILITY; ENVIRONMENTAL_AUTHORSHIP; SAKAYANAGI_RIVALRY_GENIUS` | `E001, E061, E121, E150, E169` in `Y2V12` | Sakayanagi choice, encoded influence and fiduciary cost remain distinct. V12.5 adjudicates departure and counter-authorship; Y2_10 forbids a retrospective rewrite of local certainty. |
| `Y2V12.5` / 180 | [COTE_Y2_V12_5_DEEP_READING](../01%20Canonical%20Volume%20Deep%20Readings/COTE_Y2_V12_5_DEEP_READING.md) | Actual separation starts succession tests and meets a counter-authored answer. | `SUCCESSION_SEPARATION; ICHINOSE_SELF_WORTH; NATIONAL_POLITICS` | `E061, E121, E131, E143–E155, E169, E173–E179` in `Y2V12_5` | Transfer enters Sakayanagi's former polity. Post-transfer durability, informed reciprocity and freedom's conditions remain untested; Y2_11 preserves the questions, SL adds only its admissible layers. |
| `Y2SL` / 114 | [COTE_Y2_SECOND_LIST_PARATEXT_AUDIT](../01A%20Guidebook%20Paratext%20Audits/COTE_Y2_SECOND_LIST_PARATEXT_AUDIT.md) | The boundary archive measures and frames the year without exhausting its subjects. | `OAA_LEGIBILITY; TRUTH_PROOF_RECORD; RELATIONSHIP_RECIPROCITY` | `E001–E004, E084–E085, E100, E105, E112` in `Y2SL` | Separate earlier bonus-fiction scenes, documentary tables, editorial summaries and author interview. E085 is the younger cohort; Y2_10 corrects its later misrouting. No Year-3 answer is admitted. |

## 3. Source identity, fingerprints and spine conventions

Every filename and full source SHA-256 is recorded below; byte sizes and complete internal manifests are in the source map. A source replacement requires a new verification, not silent reassignment of an existing locator namespace.

| Source | Exact source filename | SHA-256 | Canonical spine convention |
|---|---|---|---|
| `Y2V01` | `Classroom of the Elite - Year 2 - Volume 01 [Japanese].epub` | `6f31df73f2bcd05954b6c2886f6be20a844a4db8cf9ca4f6085acfeb516ad531` | zero-based OPF position |
| `Y2V02` | `Classroom of the Elite - Year 2 - Volume 02 [Japanese].epub` | `e8b1024a70a8d5eed20f0c5b155c44bed7b4552366828a9cf7d6fba8b877025a` | zero-based OPF position |
| `Y2V03` | `Classroom of the Elite - Year 2 - Volume 03 [Japanese].epub` | `0c9eec27725ec03969f6eda94736fe234e7ce63fe4ba088f841b036d8ce5309b` | zero-based OPF position |
| `Y2V04` | `Classroom of the Elite - Year 2 - Volume 04 [Japanese].epub` | `ad3a8eb0a69a77fa959fbece462a3af65cc67fbcb6a2e9b2375de0b957e6f059` | zero-based OPF position |
| `Y2V04.5` | `Classroom of the Elite - Year 2 - Volume 04.5 [Japanese].epub` | `4f23997a4f72b7ed59df6d3c334178bcc7b17c34551b6c9621a9054cd9f2f9f3` | zero-based OPF position |
| `Y2V05` | `Classroom of the Elite - Year 2 - Volume 05 [Japanese].epub` | `829bf63db3496f654d8d9c871d0fbbacfd699d169eb0cc4d17235faadf24c719` | zero-based OPF position |
| `Y2V06` | `Classroom of the Elite - Year 2 - Volume 06 [Japanese].epub` | `b4daa5f1998a3d1e05a783371233b5bd6c9a3d7b6624971a227653b2f0ae436b` | one-based OPF position |
| `Y2V07` | `Classroom of the Elite - Year 2 - Volume 07 [Japanese].epub` | `db45b6e29206b048d9311d05214550ad4f2d0e5907034b27092103d848cbde0c` | zero-based OPF position |
| `Y2V08` | `Classroom of the Elite - Year 2 - Volume 08 [Japanese].epub` | `81059e92ce187302489bca9c2116745a1e6b31f46b736b908b11e308e391c263` | one-based OPF position |
| `V00` | `Classroom of the Elite - Volume 00 [Japanese].epub` | `ec30387a4de96870b53e88a4a2ca5d28ac27455e5ffb15936f4895852fcdb209` | one-based OPF position |
| `Y2V09` | `Classroom of the Elite - Year 2 - Volume 09 [Japanese].epub` | `da89761bfd848fbc0c1a846cc8c647a03778357a005f66fd491c4aeb38b590f3` | one-based OPF position |
| `Y2V09.5` | `Classroom of the Elite - Year 2 - Volume 09.5 [Japanese].epub` | `8a4cadb422d030e60dca2b3b65b5e65321be3c4cdb13b102f0acdce45ed6620b` | one-based OPF position |
| `Y2V10` | `Classroom of the Elite - Year 2 - Volume 10 [Japanese].epub` | `310bb57a23fe737f7dae1f5b91c7acb37b195658cfc6071c91a96c8a94fbfe7e` | zero-based OPF position |
| `Y2V11` | `Classroom of the Elite - Year 2 - Volume 11 [Japanese].epub` | `348f541675bfe30ad8d1894d43c32eef7641d366dee5a5544dbcded0886ffde5` | one-based OPF position |
| `Y2V12` | `Classroom of the Elite - Year 2 - Volume 12 [Japanese].epub` | `45a62f74e72c621162e9bbf8e7b8aae4a97ed719a1decb7b2fcf97462ddd7195` | one-based OPF position |
| `Y2V12.5` | `Classroom of the Elite - Year 2 - Volume 12.5 [Japanese].epub` | `d547dbfe5a57850b26b8d25201af8e0986126019fb0525fb733f23a8ca6da352` | one-based OPF position |
| `Y2SL` | `Classroom of the Elite - Year 2 Official Guidebook - Second List [Japanese].epub` | `fcc6f15ff674c9833263247816bf23ce67a7b337924fe87901567285331e98b5` | SL image/FIC/container namespaces; no synthetic spine locator |

**Spine numbers are not globally uniform.** For a numbered source, the zero-based OPF-array index equals the canonical spine integer minus that source's `canonical_spine_index_offset`. Thus V07 `spine18` maps to array element 18, while V08 `spine12` maps to array element 11. The source map lists both the one-based OPF position and original canonical label beside the exact XHTML path. Original dots/underscores in decimal-volume namespaces are retained. These distinctions are routing translations, not new source-local numbering.

Paragraphs are one-based nonempty XHTML `p`/`h1`–`h6` records after ruby `rt`/`rp` removal, NFKC normalization and whitespace collapse. Numbered volumes happen to yield the same record counts with `p` alone; Volume 0 does not. Headings matter there. The full OPF order includes front matter, image-only documents and afterwords; none is silently dropped before calculating spine position.

The source map preserves each **historical normalized fingerprint** and its declared parser where present. It also publishes a separately named **fresh router text fingerprint** with an explicit serialization: UTF-8 records `source_code<TAB>canonical_spine_integer<TAB>one_based_paragraph<TAB>normalized_text<LF>`, including final LF. The fresh digest is not claimed to reproduce an undocumented historical serialization. The primary identity remains the unchanged EPUB-byte SHA-256. Source paragraphs are processed in memory and are not exported with the digest.

Second List uses `IMG:...` for the original image resource, `FIC1:P...` and `FIC2:P...` for its two bonus stories, and container locators for acquisition facts. FIC1 resolves to `OEBPS/Text/part0241.xhtml` (82 nonempty records); FIC2 to `OEBPS/Text/part0242.xhtml` (142). The guidebook's documentary body remains image evidence, not OCR prose. Its printed page numbers may help inspect the actual surface; no print pagination is invented for reflowable novels.

## 4. Claim-to-home retrieval map

| Synthesis claim / question | Primary analytical home | Source entry points and qualification |
|---|---|---|
| Measured performance differs from capacity, political usability and generativity | [Ability ledger](../03%20Rolling%20Ledgers/COTE_ABILITY_MEASUREMENT_LEDGER_THROUGH_Y2.md); [Y2_06](COTE_Y2_06_ABILITY_MERITOCRACY_MEASUREMENT_POINTS_AND_EXAMS.md) | V01 E010/E019; V08 E009; V11 E061. A correct score can still be an incomplete ontology. |
| An independent choice may impose an ethically unjustified cost | [Ethics ledger](../03%20Rolling%20Ledgers/COTE_ETHICS_LEDGER_THROUGH_Y2.md); [Y2_08](COTE_Y2_08_ETHICS_AUTONOMY_PROTECTION_EXPULSION_AND_VIOLENCE.md) | V05 E111/E133 and the expulsion section; V12 E121/E169. Do not equate formal validity, agency, benefit and consent. |
| Horikita's independence is real; post-transfer reproduction remains untested | [Succession ledger](../03%20Rolling%20Ledgers/COTE_SUCCESSION_SEPARATION_LEDGER.md), SS-01; [Y2_03](COTE_Y2_03_HORIKITA_LEADERSHIP_SELF_AUTHORSHIP_AND_CLASS_FORMATION.md) | V01 E028; V05 E133; V06 E101; V12.5 E163–E179. A completed departure starts the durability test. |
| Ordinary life can generate purpose and provide material for manipulation | [Ordinary-life ledger](../03%20Rolling%20Ledgers/COTE_ORDINARY_LIFE_COUNTERCURRICULUM_LEDGER_THROUGH_Y2.md); [Y2_02](COTE_Y2_02_AYANOKOJI_CHARACTER_PSYCHOLOGY_ETHICS_AND_VOICE.md) | V04.5 E001/E053; V07 E094–E105; V09.5 E001/E133; V11 E121. Keep social surplus and environmental authorship in view together. |
| Chosen loyalty and delegation do not establish protected dissent | [Class-polity ledger](../03%20Rolling%20Ledgers/COTE_CLASS_POLITY_LEDGER_THROUGH_Y2.md); [Y2_05](COTE_Y2_05_CLASS_POLITICS_LEADERSHIP_AND_CONSTITUTIONAL_DEVELOPMENT.md) | V05 E089; V09.5 E098; V12 E150 and Ryūen's battle sections. A follower's option to object must be distinguished from protection against punishment. |
| Recognition can stop short of ownership; that limit is not generalized | [Relationship ledger](../03%20Rolling%20Ledgers/COTE_RELATIONSHIP_LEDGER_THROUGH_Y2.md); [Y2_04](COTE_Y2_04_RELATIONSHIPS_DEPENDENCY_FRIENDSHIP_ROMANCE_AND_RECOGNITION.md) | V11 E147–E156 against V12 E165–E170; V12.5 E133–E162. Ichinose's third answer exceeds a supplied binary without resolving every asymmetry. |
| Origin, office, allegiance and present mission are different propositions | [Identity/allegiance ledger](../03%20Rolling%20Ledgers/COTE_ACTOR_IDENTITY_ALLEGIANCE_LEDGER.md); [Y2_07](COTE_Y2_07_INSTITUTIONS_SURVEILLANCE_ADULT_POWER_AND_WHITE_ROOM.md) | V04 E001; V07 E127–E154; V08 E145–E148; V00 retrospective ledger. Reported authorization and confirmed institutional origin have different warrant. |
| Later revelation may change genealogy without erasing earlier autonomy | [Claim/revision ledger](../03%20Rolling%20Ledgers/COTE_LONGITUDINAL_CLAIM_AND_REVISION_LEDGER.md); Y2_10 | V00 E001/E051/E126/E151; V08 E057 retained at its earlier freeze. Neither biological exceptionalism nor environmental explanation settles moral ownership. |
| Narration and relational permissions must be read in Japanese context | [Written-voice ledger](../03%20Rolling%20Ledgers/COTE_JAPANESE_VOICE_LEDGER_THROUGH_Y2.md); [Y2_09](COTE_Y2_09_JAPANESE_NARRATION_VOICE_GENRE_HUMOR_AND_VISUAL_PARATEXT.md) | V08 E113; V09.5 E133; V12.5 focal-ownership and farewell sections; SL FIC1/FIC2. The passage index adds exact-language retrieval without turning written voice into audio evidence. |
| Terminal questions survive the completed corpus | [Y2_11](COTE_Y2_11_COMPARATIVE_MATRICES_OPEN_QUESTIONS_AND_NEXT_YEAR_HANDOFF.md); [inherited tracker](../03%20Rolling%20Ledgers/COTE_Y2_Y1_HANDOFF_QUESTION_TRACKER.md) | Preserve all 42 terminal inherited states and Y2H-001–012. No later-year observation is available in this release. |

## 5. Verification and reproducibility

The reviewed input [COTE_Y2_SOURCE_ROUTING_SPEC.json](../04%20Source%20Maps%20and%20Support/COTE_Y2_SOURCE_ROUTING_SPEC.json) fixes the seventeen source identities, source order, spine conventions, expected evidence census and illustration aliases. The designated project-local [generator](../04%20Source%20Maps%20and%20Support/generate_y2_evidence_router.py) derives the two JSON outputs from that specification, the frozen Markdown readings and independently held EPUBs. It writes only those outputs; `--check` compares exact generated bytes without writing. Python dependencies are `beautifulsoup4`, `lxml` and `PyYAML`.

Invoke `generate_y2_evidence_router.py --source-dir <source-tree>` from an environment holding the same source hierarchy. Use `--check` for verification. Sources remain outside the repository and delivery archive. The specification is reviewed input and must not be automatically rewritten to make a mismatch pass.

Verified coverage comprises seventeen source-byte identities and CRC-valid containers; all 2,697 contiguous owned evidence IDs; every parsed paragraph range and explicit internal resource; all referenced illustration aliases; and all 692 canonical Japanese anchor snippets present in V08, V09, V09.5 and V12.5. Anchor identity comparison permits whitespace differences and terminal excerpt ellipses after NFKC; it is not a claim of byte-identical quotation. Early-volume illustration aliases were visually compared to the source images; later explicit alias mappings were checked against canonical inventory rows and actual resources. Range validity alone is not semantic endorsement of every analytical sentence.

The machine index copies the first complete owning evidence row, excluding shorter duplicate locator tables. Each copied locator is checked against that original row. Broad existing evidence ranges remain broad. Later micro-routes point to short samples within larger owning sections: a cluster description is not a claim that every proposition appears in each two-paragraph sample. Read the owning scene before using a micro-route as support. No unquoted surrounding paragraph is falsely assigned to an existing ID.

## 6. Closeout corrections and preserved uncertainty

**V01 visual identity correction.** `Y2V01-E064`, `COTE:Y2V01:ill-13`, resolves to `images/00013.jpeg`. The companion pictured behind Hōsen is **Nanase Tsubasa**, not Horikita. Direct image inspection and the adjoining introductions in `text/part0012.html` identify Hōsen and Nanase as the visiting first-year D-class pair. The source-local section 18.2 and E064 retain their original wording as frozen historical analysis; current reuse must apply this explicit correction. The visible scale contrast remains, but the image cannot support a specifically Hōsen/Horikita compositional argument. No downstream specialist or rolling-ledger repetition of that identity claim was found in the targeted closeout search. The JSON entry carries a pointer to this correction.

**Transfer-destination correction.** Three occurrences in Y2_01 misnamed the destination as Ichinose's former class. The source ending explicitly identifies Sakayanagi's withdrawal and Hashimoto's contribution to the transfer financing: `COTE:Y2V12.5:spine22:para0075–0080`, within the final transfer section. This directly checked surrounding passage supplements the existing E173–E179 micro-routes; it is not relabelled as their exact excerpt. The three affected Y2_01 references are corrected to Sakayanagi's former class; the unaffected analytical argument and all source-local records remain intact.

**Second List cohort correction.** E084's endpoint table and E085's first-year table describe different cohorts. E085's `1年生のクラスポイント` heading, `新1年生` introduction and named younger students identify first-years during Ayanokōji's Year 2. It does not replace the frozen Year-1 First File table. Y2_10 owns the resolved misrouting; both original documentary rows and numerical values remain unchanged.

**Source defect retained.** Volume 0 `spine61:para0018` contains malformed cohort/percentage text. Source identity is valid; quantitative precision is not recoverable from that damaged surface. Retain the anomaly and avoid inventing a corrected denominator or elimination rate. It does not authorize a claim that the institution reproduced Kiyotaka.

All corrections are present-boundary dispositions, not a license to move later knowledge into an earlier local freeze. Year 3 remains excluded; release eligibility is decided by the final administrative gate, not by this router's completion.
