---
title: "Medalist Official Fanbook 01 — Paratext Audit"
artifact_id: "MEDALIST_FB01_PARATEXT_AUDIT"
artifact_type: "guidebook_paratext_audit"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.0"
status: "canonical"
scope: "Complete delivered Japanese witness of メダリスト公式ファンブック; all components classified by source layer; adaptation information inventoried and excluded"
canonical_home: "series/medalist/02 Sequential Readings/MEDALIST_FB01_PARATEXT_AUDIT.md"
source_boundary: "Mainline manga unchanged at V15 / Score 61 (MD-FR-V15); supplemental evidence set advanced by Official Fanbook 01, whose own coverage ends at V12"
continuity: "Official supplement to the Japanese manga; documentary, creator, technical and bonus-fiction layers kept apart from collected-volume continuity"
language: "Japanese"
source_key: "MD-SUP-JP-FB01-W01"
edition: "Delivered Japanese EPUB carrying a Kodansha print colophon (first impression 2025-01-22) and a digital-edition colophon dated 2025-02-01 with issue marker (02)"
entering_freeze: "MD-FR-V15"
exit_freeze: "MD-FR-FB01"
created: "2026-10-13"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_FB01"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: false
recommended_reasoning_class: "SUBSTANTIVE_ANALYSIS"
---

# Official Fanbook 01 — paratext audit

This is an audit of a supplement and not a reading of a volume. The first official fanbook is a 159-page guide published on the same day as Volume 12. It describes the cast of Volumes 1 to 4 in detail, summarizes the story through Volume 12 in a table, reconstructs four early programs, and prints two new short manga and two unpublished storyboards by the author. Most of its interest for this project lies in one recurring box on the character pages, in which an editorial writer reports what the author told him about each character's unwritten history.

The audit asks one question of every component: what does it add to, confirm, reframe or dispute in the state frozen at `MD-FR-V15`? The answer is that it disputes almost nothing, confirms a great deal, and adds a small number of reported creator statements that bear directly on the claims Volume 15 changed. They are recorded as what they are. A statement by the author about a character's past, relayed by an editor and expressly labelled as her conception at the time of interview, is not a story page. Where one differs from a later story page, the story page governs and the difference is kept.

## Witness, admission and coverage

The [source map](../00%20Frameworks%20and%20Methods/MEDALIST_SOURCE_AND_SCOPE_MAP.md) owns witness identity. This audit uses `Medalist - Official Fanbook 01 [Japanese].epub`, source key `MD-SUP-JP-FB01-W01`, local route `MD-LOCAL-001`, 72,171,652 bytes, SHA-256 `f976c90184d32bea0c81a720cab082e3748099a306f4c3af649940de8b5154f0`. A full ZIP CRC test, a parse of the package document and spine, a complete decode of all 171 referenced images and a container hash matching the retained prior audit manifest were run before admission. The audit found no unresolved reference, no unreferenced image and no duplicated image occurrence; page progression is right to left. The ordered logical image manifest has SHA-256 `1032915311be5d06e74975ce4f043cf288a10eb7fe8e38572ea788396063257e`. The package carries almost no text layer; every page is an image, and every statement below was read from the page image. Authorization is the owner's 2026-10-12 instruction, which permits coverage reconnaissance and a conditional audit at a verified safe manga checkpoint.

Locator version `medalist-epub-spine-image-occurrence-v1`. **Printed page = occurrence − 2** at every anchor checked (contents at occurrences 0004–0006 are printed pages 2–4; the afterword at 0160 is printed page 158).

**Coverage basis.** Three statements on the book's own pages bound it. The contents page and the opening page of the story guide both say that the story overview covers the series through Volume 12 and warn readers who have not read that far. The relationship chart is headed as covering Volumes 1 to 4. The author's afterword says that the book's content goes up to Volume 4 and that she hopes for a second book for the characters from Volume 5 on. Page-by-page inspection found nothing that presupposes or reveals any event after Volume 12. `covered_manga_boundary` is therefore **V12**, `admit_after` is **V12**, and the condition was already met when this run reached `MD-FR-V15`. An editorial note dates the author's remarks to interviews of October 2024 and says that details may change with the main story.

**Inspection.** All 171 image occurrences were inspected: 0001–0063 and 0170–0171 singly, 0064–0169 as two-page greyscale spreads built for the purpose outside the source tree and the repository. Durable private batch notes cover every occurrence.

| Image occurrences | Component | Source layer | Disposition |
| --- | --- | --- | --- |
| 0001–0006 | Jacket front, title, contents, editorial note | FB-EDITORIAL | Admitted; carries the coverage statements. |
| 0007–0011 | A primer on the sport: classes, badge tests, the season, costumes, jumps | FB-TECHNICAL | Admitted as the fanbook's own summary. Not an external rule reference. |
| 0012–0013 | Relationship chart, Volumes 1–4 | FB-EDITORIAL | Admitted. |
| 0014–0075 | Character guide: twenty-six profiles | FB-EDITORIAL digests; FB-DATA sheets; FB-RATING charts; FB-CREATOR reported back stories | Admitted, each layer at its own weight. |
| 0076–0095 | Story guide: clubs; a table through Volume 12; three board-game digests; four reconstructed programs | FB-EDITORIAL; FB-TECHNICAL | Admitted. Reprinted panels are not independent evidence. |
| 0096–0097 | Translations abroad | FB-EDITORIAL | Admitted as reception paratext. |
| 0098–0108 | Two newly drawn short manga by the author | FB-FICTION | Admitted as bonus fiction with its own evidence identity. |
| 0109–0113 | Five pages by the assistant team | FB-CREATOR, third-party production | Admitted as production context only. |
| 0114, 0131 | Two gag pages of re-captioned panels | FB-EDITORIAL | Admitted; no evidential use. |
| 0115–0119 | Costume design settings | FB-CREATOR | Admitted. |
| 0120–0130 | Promotion, advertising art, magazine covers, the author's comment on the animation | FB-EDITORIAL; FB-CREATOR | Admitted as publication paratext; the comment is not used. |
| 0132–0149 | Two unpublished storyboards by the author | FB-FICTION at storyboard weight | Admitted; editorially placed in Volume 2. |
| 0150–0153 | The author's magazine cuts; a popularity poll | FB-CREATOR; FB-RATING | Admitted as publication and reception data. |
| **0154–0157** | **Animation information and cast** | Adaptation paratext | **Inventoried and excluded.** The adaptation lane is unadmitted. |
| 0158–0161 | Publication chronology; afterword; credits | FB-EDITORIAL; FB-CREATOR | Admitted; carries the author's coverage statement. |
| 0162–0171 | Print colophon, flaps, two autobiographical under-jacket comics, spreads, notices, digital colophon | Production paratext; FB-CREATOR | Admitted. |

The credits name an editorial writer for composition and text and a figure-skating supervisor. The creator boxes are therefore reported speech. This audit writes "the creator box says" and never "the story shows" for them.

## Entering state and exposure

The entering state is `MD-FR-V15`: mainline complete through Score 61, claim versions as listed there, seven ledgers at version 1.14, open questions `MD-OQ-V15-01`–`08`. No supplement had been admitted. Because the book covers only through Volume 12 and the project stands three volumes later, it could expose nothing ahead of the reader. The reverse risk was the live one: reading a 2024 conception of a character's past as if it were established, when Volumes 13 to 15 have since told part of that past on story pages. Every such overlap is entered in the delta register.

## What the book adds

### The Yuitsuka household

The creator box for the heroine's family is the most consequential page in the book for this project.

Her elder sister did not stop skating because of her fracture. By the box, she loved skating and was more devoted to her family. Her small sister was not settling at kindergarten. Her own skating needed support, and all of it fell on their mother. She judged that if she stopped, her mother's load would lighten, and that her skating was not worth making her mother endure. She cried over it. Her mother, who saw the tears, and her sister, who heard of them, took them for grief at a setback. (`MD-EV-FB01-0007`.)

The box then gives the mother. She was the child of a mother who was not motherly, in a household of two where she was neither cherished nor well dressed, and she resolved to be otherwise. She thinks her husband and elder daughter better people than herself. Her younger daughter is clumsy and close to her own temperament, so she over-identifies with her and over-protects her, and speaks against each new attempt in order to spare her a needless failure. She makes the costumes by hand because clothes matter to her, not to save money. A costume page adds that the first costume she made from nothing was the one for the free skate of the test in Volume 4. (`0006`, `0008`, `0026`.)

None of this is on a story page through Volume 15. The manga gives the fracture, the heroine's memory of a sister who stopped, and a mother who opposed and then apologized. What the box supplies, at a creator statement's weight, is a precedent inside the family for the pattern Volume 15 put at the centre: a child who gives something up so that an adult will not have to bear its cost, and whose act is misread by the people it was meant to spare. The heroine told her mother in Beijing that she would not mind vanishing if her gift made everyone happy. By this box her sister, years earlier, did a version of that, and nobody knew.

The audit records the parallel and limits it. The work has not said this on the page. The heroine does not know it. A reading may say that the author conceived the family so; it may not say that the heroine repeats her sister.

### The boy at the rink desk

Two creator boxes concern adults who failed to help a boy and later helped someone else.

The clerk who let the heroine onto the ice in exchange for worms is said to act from an old regret. There was once a boy who came to that rink constantly and plainly had no money, and the clerk did nothing. Out of that he gives the girl everything he can without asking questions. The box does not name the boy. Volume 15 puts the coach, as a boy, at that rink's rental counter asking how to learn without fees. The identification is an inference of this audit, strongly supported and unstated by the source. (`0020`.)

The patron's box overlaps Volume 15 and differs from it. By the box his wife, a skating enthusiast, saw at once that the boy who helped her at a bus stop was a skater, and the family backed him quietly through his high-school years because he would not say that he skated. In Volume 15 the patron says that the first they knew of his skating was in Yokohama, and his wife says only that she had guessed he liked it. The two can be reconciled as a guess left unspoken on both sides, but the box says more than the story does. The story governs. The box is recorded as an earlier or softer conception, and the difference is not smoothed. (`0010`, `0011`.)

Both boxes agree with Volume 15 on the larger point, and precede it by a year and a half. The adults around this boy did little when it would have counted, knew it, and made it good later on someone else or on him. Volume 15 has the patron say exactly that of himself.

### Why there is an adult in the story

A special box on the patron's family reports the series' first conception. It centred on the heroine and the patron's daughter, a rich child who was to buy her friend's skates and back her: the part the coach now plays. An editor objected that two children facing a hard fate alone left the question of what the adults were doing. The coach was created in answer, and the series' description of itself as a story of adults and children followed. (`0012`.)

This is a statement about design and not about any event. It is recorded because the claim this project registered at Volume 15, that the work refuses to sentence the adults while naming what they did, concerns the very question the editor is said to have asked.

### The coach

His sheet and box add particulars and one image. He is twenty-six, born on 4 September, 186 centimetres tall, the second of **four** brothers, with both parents living. He was a great admirer of the tall skater who later became his colleague, out of a complex about his own height. His obsession with muscle dates from dropping his partner once and hurting her slightly. The box says that skaters in the series carry a character for an animal or a bird in their names and that the two principals do not, because they were flicked out of skating's fate. (`0009`.)

The number of brothers corrects this project. The character ledger's Volume 15 identity row called him the second of three sons. The story pages of Volume 15 speak of two younger brothers and one elder, which is four. The frozen reading does not state a number and is unaffected. The ledger row receives an erratum.

### The champion and his pupil

The box on Yodaka says that he smokes partly as self-harm, so that he could not return to competition once he had decided to stop; that he breaks things when irritated, usually his telephone, which holds one contact and it is not his pupil's; that he has watched his friend's son since birth as a nephew and does not know the boy dislikes him. The editorial text glosses his retirement at twenty as following from having proved his talent on the largest stage. (`0014`.)

The box on Hikaru says she is not someone who goes her own way. She is modelled on a wolf, an animal of the pack that keeps its rank; she minds her position in every group; she never defies her two adults and does not think her coach always right; she dislikes adults who seem lax, the heroine's coach among them, though both of them adapt to others. A pendant she was looking for in Volume 1 had been thrown away by her coach, who regretted it and searched as well. (`0013`.)

These were written before Volumes 12 and 13 disclosed that her manner in her guardian's house was a performance and that she had hidden behind her coach. They corroborate those disclosures from the design side. The statement about smoking bears on a motive this project has kept open, his reason for leaving her; it is entered as context and resolves nothing.

### Other creator statements

Ryoka's dislike of children who lean on adults has a family history: parents who eloped and divorced, years with a rough father under another surname, a child blamed for every trouble. Her coach's body failed her in adolescence; her club exists on the backing of the head coach she left and of her pupil's mother. The head coach of the Kyoto club was the heir of a temple, skated on his parishioners' support, and went on only because his younger brother took the temple; his rule that a pupil must not carry other people's wishes, which is on story pages, is thereby given a biography. The Okayama head coach once coached Yodaka, could not do it well and feels guilt; his wife is the former ice dancer whom Volume 15 named. The head coach of the heroine's club succeeded her father, who had been asked to take it over and does not want to coach. (`0015`–`0019`, `0021`.)

### Bonus fiction

Two short manga by the author are new narrative. In one the heroine's week is laid out hour by hour: her mother drives her from school to the rink every day and she changes in the car; her club has hired ice on two evenings and one dawn; she is at the rink two hours and twenty minutes on an ordinary day and thinks it too little; the dawn session is shared with adult hobby skaters and ends with breakfast together, and she thinks that she loves all of her time. In the other, Hikaru asks what an exhibition is, orders a costume of frills, and is rolled up in it at her first jump while her guardian's wife laughs; a caption says her coach has no part in her exhibitions and watches them with mixed feelings. (`0022`, `0023`.)

Two unpublished storyboards, placed by the editor in Volume 2, show how Ryoka met her coach at six, as a paying customer who wanted no manners taught, and lost a race and a bet to her; and Suzu telling the heroine what it was to lose to Hikaru and refusing the thought that second place is natural. (`0024`, `0025`.)

All four are consistent with the mainline. They are entered as fiction at their own weight. The first gives the mother's routine labour from the daughter's side, three years before the daughter names that labour as a cost.

### Technical and documentary layers

The primer agrees with the in-story statements this project recorded in Volumes 10 to 15 on classes, the badge grades, the series, the final and the season's order. It is the fanbook's summary, with a note that it follows the rules of one season. It names a real Olympic Games as an example of the age rule; that is an editorial frame, and no calendar year of the story is inferred from it.

The program reconstructions give start orders, element lists and scores for two programs at each of two early competitions. Every score matches the frozen readings. The publication chronology gives release dates for Volumes 1 to 12; those for Volumes 6 to 12 are the first-impression dates this project read from print colophons. That supports treating the earlier date in each digital colophon as a convention of the digital edition. The witnesses themselves still do not say so.

## Canonical observations

All rows refer to `MD-SUP-JP-FB01-W01`, locator version `medalist-epub-spine-image-occurrence-v1`. Descriptions are paraphrases. Creator rows are reported statements dated by the book to October 2024. Linked claims are the versions in force at this freeze.

| Observation / exact locator | Inspected feature and attribution | Source layer | Confidence and limits | Linked claims |
| --- | --- | --- | --- | --- |
| MD-EV-FB01-0001 — 0004–0006, 0076, 0160 | Three coverage statements: story overview through Volume 12; chart for Volumes 1–4; the author's "up to Volume 4"; remarks dated to October 2024 and liable to change. | FB-EDITORIAL, FB-CREATOR | HIGH. | 0013 |
| MD-EV-FB01-0002 — 0007–0011 | Primer: classes and ages, badge grades, season calendar, costume rules, jump types. | FB-TECHNICAL | HIGH as the book's summary. | 0013 |
| MD-EV-FB01-0003 — 0012–0013 | Relationship chart; "contract" on the arrow from Yodaka to Hikaru. | FB-EDITORIAL | HIGH. | 0016 |
| MD-EV-FB01-0004 — 0015–0017 | Inori: the name; school marks and a teacher's unpaid lessons; tenacity; the cold feeling; a data sheet (born 16 April; 134 cm at eleven). | FB-CREATOR, FB-EDITORIAL, FB-DATA, FB-RATING | HIGH as stated. | 0015 |
| MD-EV-FB01-0005 — 0018–0019 | Her father's career; her mother's maiden name and upbringing. | FB-CREATOR | HIGH as stated. | 0014 |
| MD-EV-FB01-0006 — 0019, 0021 | Why her mother resisted: over-identification with a child like herself. | FB-CREATOR | HIGH as stated. | 0014 |
| MD-EV-FB01-0007 — 0020–0021 | Mika's career and her reason for stopping; the misreading by mother and sister. | FB-CREATOR | HIGH as stated; not on any story page. | 0014, 0026, 0029 |
| MD-EV-FB01-0008 — 0115, 0119 | Costumes: a sister's, altered; the first one her mother made, for the Volume 4 test. | FB-CREATOR | HIGH. | 0014 |
| MD-EV-FB01-0009 — 0023–0025 | Tsukasa: names; muscle; four brothers; parents living; a data sheet; a fan of Sonidori. | FB-CREATOR, FB-DATA | HIGH as stated. | 0010 |
| MD-EV-FB01-0010 — 0028 | Meiko saw that he skated and the family backed him quietly in his school years; he left without thanks. | FB-CREATOR | HIGH as stated; differs in degree from V15 story pages. | 0010, 0011 |
| MD-EV-FB01-0011 — 0029 | Yokohama: live-in help; he stayed after her death and cared for the daughter; the family's return to Nagoya. | FB-CREATOR | HIGH as stated; agrees with V15. | 0011 |
| MD-EV-FB01-0012 — 0027 | The first conception: the patron's daughter as supporter; an editor's objection; the coach created. | FB-CREATOR | HIGH as stated; a statement of design. | 0011, 0031 |
| MD-EV-FB01-0013 — 0030–0033 | Hikaru: a wolf of the pack; minds her rank; dislikes lax adults; the pendant. | FB-CREATOR, FB-DATA | HIGH as stated. | 0003, 0023 |
| MD-EV-FB01-0014 — 0035–0037, 0039 | Yodaka: smoking as self-harm against return; one telephone contact; fondness for his friend's son; retirement as proof achieved. | FB-CREATOR, FB-EDITORIAL | HIGH as stated. | 0016 |
| MD-EV-FB01-0015 — 0043, 0045, 0077 | Sonidori and his wife; Hitomi's career; her father as teacher of three; the club's succession; "does not want to coach". | FB-CREATOR, FB-EDITORIAL | HIGH as stated. | 0011 |
| MD-EV-FB01-0016 — 0049–0051 | Ryoka's family history and her dislike of adult-backed children. | FB-CREATOR | HIGH as stated. | 0006 |
| MD-EV-FB01-0017 — 0053 | Nachi's failed adolescence as a skater; the club's backers. | FB-CREATOR | HIGH as stated. | 0009 |
| MD-EV-FB01-0018 — 0055–0059 | Ema, Jakuzure as "the opposite style" to Tsukasa, Suzu. | FB-CREATOR | HIGH as stated. | 0020, 0024 |
| MD-EV-FB01-0019 — 0063 | Kameganya: a temple's heir, parishioners' support, a brother who took his place. | FB-CREATOR | HIGH as stated. | 0024, 0026 |
| MD-EV-FB01-0020 — 0073 | Sekoma's regret over a boy he did not help. | FB-CREATOR | HIGH as stated; the boy is unnamed. | 0011, 0031 |
| MD-EV-FB01-0021 — 0065–0071, 0075 | Minor figures: two Hiroshima skaters' later paths; Kyōboku's guilt and his wife; the Fukuoka trainer named; a ballet teacher's later post. | FB-CREATOR, FB-DATA | HIGH as stated. | 0016 |
| MD-EV-FB01-0022 — 0099–0102 | Short manga: the heroine's timetable; her mother's driving; a small club's ice. | FB-FICTION | HIGH; undated within Volumes 3–4. | 0011, 0014 |
| MD-EV-FB01-0023 — 0103–0108 | Short manga: Hikaru and the exhibition; her coach kept out. | FB-FICTION | HIGH; undated. | 0003, 0016 |
| MD-EV-FB01-0024 — 0133–0143 | Storyboard: how Ryoka met Nachi; a race, a bet, a club's origin. | FB-FICTION, storyboard | HIGH as drawn; rough. | 0006, 0009 |
| MD-EV-FB01-0025 — 0144–0149 | Storyboard: Suzu on losing to Hikaru. | FB-FICTION, storyboard | HIGH as drawn; rough. | 0023 |
| MD-EV-FB01-0026 — 0078–0095 | Story table through Volume 12; four reconstructed programs with scores. | FB-EDITORIAL, FB-TECHNICAL | HIGH; all scores match the readings. | 0013 |
| MD-EV-FB01-0027 — 0158–0159, 0162, 0171 | Publication chronology; colophons. | FB-EDITORIAL, production | HIGH. | 0013 |
| MD-EV-FB01-0028 — 0152–0153 | First popularity poll. | FB-RATING | HIGH; reception only. | 0013 |
| MD-EV-FB01-0029 — 0109–0113, 0120–0130, 0150–0151, 0165–0166 | Assistants' pages; promotion; cover art; the author's magazine cuts and autobiographical comics. | FB-CREATOR, FB-EDITORIAL | HIGH; production context. | 0012 |
| MD-EV-FB01-0030 — 0154–0157 | Animation information and cast. | Adaptation paratext | Excluded. | — |

## Retrospective delta register

Prior versions are those of `MD-FR-V15`. Revisions are recorded in the claims ledger as `MD-RV-0263`–`0269`.

| Later observation | Layer | Prior claim / earlier best inference | New evidence | Transition | Affected homes | Unresolved limits |
| --- | --- | --- | --- | --- | --- | --- |
| 0007 | FB-CREATOR | MD-CL-0014@9: a family whose care works at a distance; the sister stopped after a fracture | She stopped to lighten her mother's load; it was misread | REVISE → @10 | Character, chronology, claims | Not on a story page; the heroine does not know. |
| 0005, 0006, 0008, 0022 | FB-CREATOR, FB-FICTION | MD-CL-0014@9: the mother opposed, then supported | Her own upbringing; over-identification; costumes made as care; daily driving | within @10 | Character, institutions | Reported conception. |
| 0010 | FB-CREATOR | MD-CL-0010@15, MD-CL-0011@15: the patrons first learned of his skating in Yokohama | The wife knew at once and the family backed him quietly | OPEN conflict; story governs | Chronology | A difference of degree, kept. |
| 0011, 0012, 0020 | FB-CREATOR | MD-CL-0011@15: adults who share a burden late | A second adult with the same regret about the same boy; the coach created to answer where the adults were | STRENGTHEN → @16 | Institutions, claims | The boy is unnamed in the source. |
| 0009 | FB-CREATOR, FB-DATA | MD-CL-0010@15 | Four brothers; parents living; particulars | PRESERVE @15; erratum to one ledger row | Character | — |
| 0013, 0023, 0025 | FB-CREATOR, FB-FICTION | MD-CL-0003@12: her manner an act; hid behind her coach | Designed as a keeper of rank who performs; a field that refuses to excuse itself | STRENGTHEN → @13 | Character, claims | Written before V12–V13. |
| 0003, 0014, 0023 | FB-CREATOR, FB-EDITORIAL | MD-CL-0016@12: his motive beyond his stated reason unknown | Smoking as a bar to his own return; retirement as proof achieved; kept out of her play | REVISE → @13, still LOW for motive | Character, claims | Context; resolves nothing. |
| 0016, 0024 | FB-CREATOR, FB-FICTION | MD-CL-0006@2 | A family cause for her stance toward adults; a first meeting as a transaction | STRENGTHEN → @3 | Claims | Storyboard weight. |
| 0017, 0024 | FB-CREATOR, FB-FICTION | MD-CL-0009@2 | Her coach's own failed body; the club's backers and stated purpose | REVISE → @3 | Claims | Storyboard weight. |
| 0019 | FB-CREATOR | MD-CL-0026@8, MD-CL-0024@9 | A biography for the doctrine that forbids carrying others' wishes | PRESERVE; noted as a counter-voice | Readiness (MD-RD-0076) | — |
| 0001, 0026, 0027 | FB-EDITORIAL | MD-CL-0013@15 | A supplement admitted with its coverage bounded; publication dates corroborate print colophons | REVISE → @16 | Source map, claims | The digital-colophon convention is still not stated by a witness. |
| 0002, 0026 | FB-TECHNICAL | MD-CL-0005, 0008 | Agreement with in-story rules and scores | PRESERVE | — | Not an external reference. |
| all | — | MD-CL-0001, 0002, 0004, 0007, 0012, 0015, 0017–0023, 0025, 0027–0031 | No material evidence | PRESERVE | — | — |

No prediction existed to adjudicate. No earlier freeze is altered. One erratum is entered in the character ledger.

## Ledger reconciliation

All seven homes were reviewed. Each moves to version 1.15 and carries an FB01 section; two record no material change.

| Canonical home | FB01 effect |
| --- | --- |
| [Character/readiness](../03%20Longitudinal%20Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md) | Supplemental identity data for fourteen keys; one erratum; MD-RD-0077. |
| [Directional relationships](../03%20Longitudinal%20Ledgers/MEDALIST_RELATIONSHIP_RIVALRY_AND_MENTORSHIP_LEDGER.md) | Three annotations to existing pairs; no transition added. |
| [Skating/training](../03%20Longitudinal%20Ledgers/MEDALIST_SKATING_TRAINING_AND_COMPETITION_LEDGER.md) | No material change; reconstructions agree with existing rows. |
| [Institutions/resources](../03%20Longitudinal%20Ledgers/MEDALIST_INSTITUTIONS_RESOURCES_AND_AUTHORITY_LEDGER.md) | MD-IN-0155–0157. |
| [Chronology/information](../03%20Longitudinal%20Ledgers/MEDALIST_CHRONOLOGY_INFORMATION_AND_RETROSPECTION_LEDGER.md) | MD-TM-0122–0123; MD-PROP-0058; MD-KN-0154–0156; MD-RT-0114–0117. |
| [Visual form](../03%20Longitudinal%20Ledgers/MEDALIST_VISUAL_FORM_AND_PERFORMANCE_LEDGER.md) | No material change. |
| [Claims/revisions](../03%20Longitudinal%20Ledgers/MEDALIST_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md) | Seven claims advanced a version; MD-RV-0263–0269; no new claim; no MD-PR. |

## Frozen combined state — MD-FR-FB01

Entering freeze `MD-FR-V15`. This freeze changes the admitted evidence set and seven claim versions. It does not change the mainline boundary.

- **Mainline manga endpoint:** unchanged: V15, Score 61, occurrence 0208 of the V15 witness.
- **Supplemental endpoint:** Official Fanbook 01 audited in full, 171 image occurrences inspected; animation pages 0154–0157 inventoried and excluded. One completed paratext audit.
- **Combined evidence set:** `MD-MG-JP-TB-V001-W01` through `-V015-W01` and `MD-SUP-JP-FB01-W01`. Official Fanbook 02 unadmitted at this freeze.
- **What the supplement changes:** creator-reported back story for the heroine's sister and mother; a second adult's regret about the boy the coach was; the stated origin of the coach as the series' answer to absent adults; particulars for the coach, the champion, his pupil and several early figures; four pieces of bonus fiction; one recorded conflict of degree with Volume 15 over what the patron's wife knew.
- **Claim versions:** MD-CL-0001@15; 0002@15; **0003@13**; 0004@13; 0005@14; **0006@3**; 0007@12; 0008@14; **0009@3**; 0010@15; **0011@16**; 0012@15; **0013@16**; **0014@10**; 0015@14; **0016@13**; 0017@11; 0018@2; 0019@12; 0020@2; 0021@6; 0022@11; 0023@9; 0024@9; 0025@9; 0026@8; 0027@7; 0028@5; 0029@5; 0030@2; 0031@1.
- **Ledger versions:** all seven at 1.15. Readiness MD-RD-0077 records the supplement's effect on the monographs.
- **Debts:** MD-OQ-V15-01–08 unchanged. The creator statements are reported, dated and revisable. One conflict with a story page is open and resolved for use in the story's favour. The boy in the clerk's regret is unnamed.
- **Next candidate:** the paratext audit of Official Fanbook 02, whose coverage reconnaissance places its admission condition at or before V13.

## Verification and transaction recovery

Closure review: witness hashes and structure matched the retained audit; all 171 occurrences covered by durable batch notes; three on-page coverage statements recorded and checked against content; every component assigned a source layer; adaptation pages excluded; all 30 observation IDs present; each revised claim version named in the freeze present in the claims ledger; every score in the reconstructions compared with the frozen readings; no dialogue reproduced; no raw page, bulk transcript or private path in this artifact.

The containing commit is recovered from this path's Git history. Author preflight and publication are followed by housekeeping and the exact-head `Repository integration audit`; this text claims no future audit result.
