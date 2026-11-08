---
title: "Gakuen Idolmaster V2 Historical-Source Analytical Coverage Audit — 2026-11-08"
series: GKM
artifact_type: audit
scope: THIRTEEN_CHARACTER_CORES_RELATIONSHIP_AND_ENSEMBLE_SYNTHESES_HISTORICAL_SOURCE_COVERAGE
generation: V2
status: active_provisional
audit_nature: "non-authoritative retrospective audit; does not revise any canonical conclusion"
audit_id: GKM-HSCA-20261108
source_boundary: "GAKUMAS V2 Source Lock 1.0 only — DreamGallery/Campus-adv-txts @ 00d150a069a3ffa723a1ff264752ba242024caad, revision 32, generated 2026-08-02T22:21:04Z; 3,777 scripts / 93,924 dialogue messages; manifest.csv SHA-256 82ed6510a74bfa278591ddcaefa35f771423228eb62c5e03d820d4f4362196b1"
source_lock: GAKUMAS V2 Source Lock 1.0
source_commit: 00d150a069a3ffa723a1ff264752ba242024caad
source_revision: 32
audit_baseline_commit: "f6826f810d3d31d80f0a0963c86d1aa37cc0e3de"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-11-08"
last_updated: "2026-11-08"
---

# Historical-source analytical coverage audit

**Status: retrospective, non-authoritative.** This audit assesses how completely the canonical V2 analytical corpus accounts for the admitted historical sources. It does not revise any character reading, synthesis, ledger, continuity map or registry; every deficiency is recorded in the companion [findings register](GKM_HSCA_FINDINGS_REGISTER.md), and what was examined is recorded in the [coverage ledger](GKM_HSCA_COVERAGE_LEDGER.tsv). Current authority remains the [current-state map](../../CURRENT_STATE_AND_CORPUS_MAP.md) and the canonical homes it routes to.

## Final disposition (one paragraph)

All thirteen character cores, both Relationship Systems syntheses, the four story-event tranche readings and the eight support-card tranche readings were assessed against a complete blind reading of Source Lock 1.0. **No P0 (interpretation-breaking) deficiency was found.** Six P1 findings survived adversarial verification; 94 P2 and 79 P3 findings are refinements, cross-reference gaps or traceability defects. 228 audit records were classified COVERED, including about 150 negative controls (at least three per assignment) across every source family. The corpus's central theses for all thirteen characters survive; the most consequential gaps cluster in **cross-track material** (a character's states inside other idols' Dear tracks and inside Unit Story 01) and in a small number of **attribution and branch-gating** errors. The PR #531 Saki correction calibrated correctly (historically OMITTED, now ALREADY_CORRECTED), and the audit found one further qualification to that correction (a choice-gated line, HSCA-046).

## 1. Purpose and evidence boundaries

Purpose: determine, character by character, whether the canonical corpus meaningfully accounts for the psychologically and developmentally significant material in the historical sources, and identify omissions, underweighted evidence, cross-character gaps, counterevidence and flawed interpretations.

Boundaries:

- **Primary source ceiling:** Source Lock 1.0 only (front matter). No newer transcripts, story content, audiovisual material or paratext were admitted; no audiovisual acquisition was performed. Any canonical claim relying on material beyond the lock would be marked `OUT_OF_SCOPE_POST_BOUNDARY`; none was found (§9).
- **Analytical corpus audited:** the repository at `f6826f81` (= `origin/main` at audit start; PR #531 merged as `1426ab76`). `main` later advanced to `870de40b` (PR #532), which changes no file under `series/gakuen-idolmaster/`; the audit baseline therefore equals the current Gakuen tree.
- **Historical states:** twelve character cores are unchanged in body since their Phase-3 delivery (migration commit `9957068c`; later diffs are YAML re-serialization). Saki's core was evaluated in two states: pre-PR #531 (`3beaa074` snapshot) and current v2.1. The Hiro and Misuzu AV addenda were revised in `e285ebb4` and were judged at their current state. Each tranche reading's body is unchanged since its 2026-08-23/24 delivery.
- **Declared scope rule:** Phase-3 cores declared their own source boundary (most: the character's complete bundle; some also relevant U1/shared material). Material outside a core's declared boundary is `SCOPE_LIMITED` for that core, and was then checked against the later canonical homes (tranche readings, ledgers, Relationship Systems I/II, side-characters synthesis).
- **Kaya Rinha** was treated provisionally: her files were used only to check routing; her dossier was not evaluated or completed.
- No psychiatric diagnoses are made or endorsed.

## 2. Historical source identity and checksums

| item | value |
|---|---|
| Source lock | GAKUMAS V2 Source Lock 1.0 |
| Upstream | `DreamGallery/Campus-adv-txts` @ `00d150a069a3ffa723a1ff264752ba242024caad`, revision 32 |
| Generated | 2026-08-02T22:21:04Z |
| Objects | 3,777 scripts; 93,924 dialogue messages |
| `manifest.csv` SHA-256 | `82ed6510a74bfa278591ddcaefa35f771423228eb62c5e03d820d4f4362196b1` (verified before indexing) |
| Source identity rule | `original_name` + `sorted_relative_path` (A1 raw script) |
| Layers used | A1 raw ADV scripts (`transcripts_raw/`), A2 dialogue-only (`transcripts_dialogue_only/`), A3 analysis bundles (`analysis_bundles/`) |

Boundary facts established from the manifest (recorded because canonical text could otherwise overreach): story events present are 001–026 (five parts each) and 029 main-01..04 only — no 027/028; whether 029 continued is not determinable from the lock. The support bundle labelled `part_051-074` holds stories 0051–0079 (minus 0055/0057/0078); `part_076-102` holds 0076–0098, 0100–0105 and 0108.

## 3. Method and actual inspection capabilities

**Stage A — blind primary-source reading.** The admitted sources were partitioned into 39 packets: for each of the 13 characters a Dear+Communications packet and a Produce Story/Events/live/growth packet (26); Unit Story 01 in two halves (U1-A lines 1–4675, U1-B 4676–end); story events in four tranches (EV-1..4); support cards in six (SP-1..6); and shared/tutorial (SH). Each packet was read **completely and sequentially** by an independent reader with no access to the repository or any analysis (blindness rule), recording candidate scenes with exact Japanese anchors, epistemic class (event / dream / memory / hypothetical / self-claim / observer claim / stage performance / inner monologue), continuity cues and salience. 3,377 source objects were read in full; **2,403 candidates (996 high-salience)** were recorded.

Every packet was validated mechanically: manifest identity of every `original_name`, presence of every anchor fragment in the cited script's dialogue (whitespace-, ruby- and emphasis-normalized; speaker labels stripped), and coverage reconciliation against the bundle's envelope list. Mismatches were bookkeeping only (anchors spanning two consecutive scripts were given the second script as `also_in`); no reader interpretation was altered.

The 400 manifest objects outside any packet carry 70 dialogue messages in total (produce-system prompts, gacha staging, empty staging files, the series-3 H.I.F. rules explanation and the request-system introduction). The orchestrator read all 26 that carry dialogue; they contain no character-psychology content, and the substantive ones are covered by `GKM_DEDUP_AND_EXCEPTION_AUDIT.md`, the shared/institutional spine and the institution ledger.

**Stage B — comparison against the canonical corpus.** Candidates were routed to 30 assignments: 14 character runs (Saki split into own-bundle and U1/Ume-bundle halves), 6 character supplements for late-arriving cross-character candidates, 4 event-tranche runs and 6 support-tranche runs. Auditors read each core, evidence matrix and AV addendum in full, the relevant tranche readings, ledgers and syntheses, grepped the whole series root, and judged **interpretive coverage, not citation**: a missing quotation is not a missing insight, and an uncited scene adequately synthesized under a broader claim is COVERED. Tranche auditors additionally checked **propagation**: whether a character-defining tranche finding reaches at least one cumulative or synthesis home.

**Severity** (actionable dispositions only): P0 interpretation-changing; P1 major underrepresentation of a significant development/motive/psychology/relationship finding; P2 meaningful refinement without changing a thesis; P3 documentation/traceability. Confidence was assessed separately.

**Adversarial verification.** Every P0/P1 required A1 re-inspection, context, speaker check, manifest check, continuity placement, full reading of the relevant canonical sections, a search for another canonical home, and the strongest adequacy defence. The orchestrator then **independently re-inspected the raw script** for every P1 (two borderline P1s were lowered to P2 — §7).

**Negative controls.** Each assignment reported at least three high-salience candidates that the corpus covers well, with the exact covering section (about 150 in total; every source family and character represented).

**Actual capabilities and limits** are stated in §9 and §11.

## 4. Source-to-analysis coverage results

| measure | count |
|---|---:|
| Manifest objects | 3,777 |
| Read in full by Stage-A readers | 3,377 |
| Residual objects read by orchestrator (with dialogue) | 26 |
| Residual objects without dialogue | 374 |
| Stage-A candidates (high) | 2,403 (996) |
| Stage-B audit records | 431 |
| COVERED | 228 |
| SCOPE_LIMITED (core boundary; checked elsewhere) | 3 |
| ALREADY_CORRECTED | 7 |
| Actionable assignment records | 193 |
| Register entries after merging duplicates | 180 |

Register entries by disposition: UNDERWEIGHTED 74, CROSS_REFERENCE_GAP 42, CONTINUITY_OR_ATTRIBUTION_ERROR 20, TRACEABILITY_GAP 19, OMITTED 14, POTENTIALLY_CORRECTIVE 11. By severity: P0 0, P1 6, P2 94, P3 79, evidence-only 1.

Source families cited by actionable entries (an entry can cite several): Dear 109, Idol Communications 51, Produce Story 34, story events 29, support cards 26, Unit Story 01 20, Produce Events 16, other 6. Dear dominance reflects where character interiority is concentrated, not a family-specific failure; see §6.

## 5. Character-by-character conclusions

Counts are register entries tagged to the character (an entry may concern two characters). "Survives / narrows" summarizes the auditor's adversarial pass over the core's strongest conclusions.

| character | entries (P1/P2/P3) | assessment |
|---|---|---|
| Hanami Saki | 32 (1/14/17) | Thesis (無敵 → 不屈; fear structure; action before recovery) survives; co-authorship claim narrows. Gaps are cross-track: Saki's trajectories inside Ume's and Sena's Dear tracks (HSCA-002, HSCA-058), Mao Dear 031's motive confession (HSCA-057), and the Producer's abandoned plan (HSCA-047). One qualification to the PR #531 correction (HSCA-046). |
| Tsukimura Temari | 23 (2/8/13) | Thesis and "reconciliation is not reunion" survive (strengthened by U1). Self-love is effort- and belief-anchored rather than win-anchored (HSCA-098); SyngUp collapse has a second self-blame (HSCA-100); Temari's early deference to Lilja rests partly on a dubbed line (HSCA-006). |
| Fujita Kotone | 11 (0/6/5) | Strongest-covered core. Producer's covert father search (HSCA-023), Kotone's own U1 leadership (HSCA-026), and rejection-of-succession scope (holds in D-KOTONE, not in D-SENA). |
| Arimura Mao | 16 (0/10/6) | Thesis survives and is strengthened. Last-chance third-year history (HSCA-009), Juo-family interest in keeping her from H.I.F. (HSCA-012), Sena-side reading already present in her bundle (HSCA-013); support readings misgender her (HSCA-015). |
| Katsuragi Lilja | 15 (2/8/5) | Five of six conclusions survive; Producer-dependence open questions partly answered in her own bundle. REVERSI invariants are track-specific (HSCA-079). |
| Kuramoto China | 13 (0/6/7) | Accountable-inheritance thesis survives; "not deprivation; needs reliably met" needs narrowing against her own childhood account (HSCA-073); a maid's identity is asserted without a source (HSCA-151). |
| Shinosawa Hiro | 12 (0/6/6) | Thesis survives; origin (owl) and dream timing narrow; the Producer's career cost of choosing her is underweighted (HSCA-086); "never had friends" is treated as biography (HSCA-089). |
| Himesaki Rinami | 16 (0/12/4) | Core conclusions survive; "competitive ambition is new" narrows (HSCA-040); Mao–Rinami bilateral never synthesized. |
| Shiun Sumika | 20 (2/10/8) | Thesis survives; the Dear 014 reconciliation is misread across four homes (HSCA-005); gyaru origin and mother friction unrecorded (HSCA-091); exit-testing pattern underweighted. |
| Hanami Ume | 22 (1/8/12) | Thesis, fear model, summit-as-invitation survive; career-agency claim narrows (HSCA-003); summer H.I.F. reversal in D-UME has no home (HSCA-059); her side of Hiro's track (HSCA-064). |
| Hataya Misuzu | 22 (1/10/11) | Night-sky thesis survives within her route; U1 arc absent (HSCA-001); universal appetite is co-original with Temari-directed desire (HSCA-030); cross-track dissolution-live pattern unmapped (HSCA-032). |
| Juo Sena | 33 (1/19/13) | Most cross-track exposure. U1 retirement arc absent (HSCA-004); post-summit abdication recurs across tracks (HSCA-069); named origin of her ceiling belief (Murasame Shuka) absent (HSCA-070); stat vision narrows (HSCA-071). |
| Amaya Tsubame | 18 (0/11/7) | Thesis survives and is strengthened by cross-route evidence; origin (HSCA-016) and the "love" attribution (HSCA-017) narrow. |

Event and support tranche readings were found accurate and well propagated: in every tranche run that reported a propagation table, at least 88% of high-salience candidates reached a cumulative or synthesis home; no tranche thesis was overturned.

## 6. Cross-character and cross-source patterns

1. **Cross-track states are the dominant gap.** Of the six P1s, four concern material that sits in another idol's track or in U1 (HSCA-001, -002, -003, -004). The same pattern recurs at P2: Saki in Sena's track, Ume in Hiro's, Misuzu/Temari skipping winter H.I.F. in three tracks, Sena's abdication in D-SAKI/D-TSUBAME. Phase-3 cores were scoped to their own bundles, and the later synthesis layer did not systematically harvest each character's appearances in other tracks.
2. **U1 Episode-04 sub-arcs.** Before PR #531, Saki's U1 nightmare/insomnia material had no character-facing home. The audit found the same structural gap for Misuzu (HSCA-001) and Sena (HSCA-004), and Kotone's own U1 leadership is likewise unrecorded from her side (HSCA-026).
3. **Attribution and branch gating.** A dubbed line treated as Lilja's influence (HSCA-006), a reconciliation mechanism misread (HSCA-005), a choice-gated line treated as fixed (HSCA-046), male pronouns for Mao across five support readings and two ledgers (HSCA-015), a self-report promoted to biography (HSCA-089), an unsourced identity assertion (HSCA-151).
4. **Independent convergence** strengthens confidence: two auditors separately found the Dear 014 misreading (Sumika and Lilja runs), the Dear 009 vs 011–012 ledger error (Saki and Ume runs), and the D-UME 100 Pro issue (Ume and Saki calibration runs).
5. **Not systemic:** dreams and subjective representations were generally handled correctly (dream vs waking belief kept distinct; the Saki nightmare is now covered); Japanese register/ruby nuances produced only P3 items (e.g. China's single first-name address in Dear 035; Misuzu's bare-name shifts).

## 7. Prioritized outstanding findings (P1)

All six survived auditor A1 verification and independent orchestrator re-inspection of the raw script.

| ID | subject | finding (anchor) | destination |
|---|---|---|---|
| HSCA-001 | Misuzu (Temari) | U1 Begrazia arc: «この手を取ってください。今度こそ、一緒に……» (`adv_unit_01-04_08.txt`); «（最初で最後の全力疾走……）» (04_20); «わたし、二度と全力疾走なんてしません。» / «徒歩で勝ちますね。» (04_22). No Misuzu-facing home; RS-I §5 and both state ledgers silent. | RS-I §5; Character/Relationship State Ledgers (Misuzu U1 rows) |
| HSCA-002 | Saki | D-UME Saki trajectory: «わたしはもう……逃げたりしない！！» (`adv_dear_hume_019.txt`); «待たせたわね――追いついたわよ！！！！！» (022); Rinha «……いまにも燃え尽きてしまいそうだった。» (024); «プロデューサーは……いらないわ。比べてしまいそうだもの。» (033). Answers the Saki core's own H-SAKI-05 test. | RS-I §3; state ledgers (D-UME Saki rows); Saki core open-hypothesis note |
| HSCA-003 | Ume | Dear 035 «100プロが第一志望です。» framed as choosing «against the obvious path», while Dear 033 has Saki «わたし、100プロ入りが決まったの。» and Ume's long pause «…………………………………そっか。». Outcome converges; reasoning is her own. | Ume core §19 / UME-C30 (addendum or correction note); Character State Ledger late-D-UME; Ume AV matrix UME-AV25/AV09 |
| HSCA-004 | Sena | U1 retirement arc: «言葉通りよ。私は……アイドルを引退して、» / «足手まといは要らない。» (04_14); «諦めにくく、するのだもの。» (04_16); «――引退を撤回するわ！» (04_23). Only shared spine §8.4 touches it (softened). | Sena-facing ledgers; RS-II §8; shared spine §8.4 qualification |
| HSCA-005 | Sumika, Lilja | Sumika Dear 014: Lilja's «違う……！わたしは約束を信じてるんじゃない！» answers the promise framing; to the prodigy charge she falters «それ、は……», half-confirms «清夏ちゃんはもっと、すごくて――» «あっ……。», and accepts «……わたしのせいなんだなって。». Canon says she "rejects" the charge. | Sumika core §8/§23, matrix C07; RS-I §4.2/§4.12; Relationship ledger (Lilja↔Sumika) |
| HSCA-006 | Temari, Lilja, Sumika | Event 001: the taunt is labelled `リーリヤ？` and is Sumika's dub («以心伝心でアテレコしてみた。»); Temari, frozen, later recalls it as Lilja's «『足を引っ張るなよ雑魚が』って？»; Event 004 «ま、また脅す気？» / Sumika «当分使えるわ～、この手♪». Canon models Temari's response as conviction-based respect only. | Events 001–005 reading §6.7/§9.1; Relationship ledger (Temari↔Lilja) |

Severity adjustments made during verification: two auditor P1s were lowered to P2 after orchestrator re-inspection because they qualify rather than supply an analysis — Sumika's gyaru origin (HSCA-091) and the Producer's career cost of choosing Hiro (HSCA-086). One P3 was raised to P2 (HSCA-046, the PR #531 choice-gating issue).

## 8. Already-corrected historical findings and calibration

**Calibration on PR #531 (Saki, U1 Episode 04).** Stage A was blind: the U1-B reader flagged `adv_unit_01-04_13.txt` (nightmare; DREAM; fear of becoming irrelevant to Ume) and `adv_unit_01-04_15.txt` (fear "less of losing again than of losing and no longer feeling frustrated") as high salience with no corpus access. Stage B evaluated the corpus at `3beaa074` and at current `main`: historically OMITTED/P1 (and the Selection-defeat arc UNDERWEIGHTED/P1); currently ALREADY_CORRECTED. Four Episode-04 scenes that were already covered stayed COVERED in both passes, and gaps the correction did not address (Sena's "mirror" talk; peers as recovery agents) stayed open. **Limitation:** the Stage-B pass-1 auditor had read the expected calibration outcome, so the Stage-B half shows consistency, not blind reproduction; the blind Stage-A half and the independent convergences in §6 partly compensate.

Other ALREADY_CORRECTED items: Ume's U1 evidence in RS-I §3.5.1 (PR #531); hski-DC-041's link between Ume's and Saki's fears (RS-I §3.5.1); Hiro AV addendum's misattribution of 「瞬間最大風速」 (fixed in `e285ebb4` — the voice/register ledger still carries it, HSCA register P3); Rinha-as-protector framing (already narrowed in the Rinha matrix and relationship ledger). The register lists all seven.

**Qualification to the PR #531 correction.** `adv_unit_01-04_04.txt` opens a three-way `choicegroup` (藤田さん / 月村さん / 咲季さん). Saki's «予感があるの。妹に、一度でも負けちゃったら、» / «もう二度と勝てないって。» occurs only on the 咲季さん branch, but the v2.1 nightmare analysis ("the nightmare is assembled from real words") and SAKI-L058 treat it as fixed (HSCA-046, P2). The nightmare (04_13) and insomnia scene (04_15) themselves are unconditional.

## 9. Unresolved evidence and scope limitations

- **Post-boundary check:** no canonical text in the audited tree relies on material beyond the lock; events 027/028 are mentioned only as absent.
- **Dialogue-only layer** omits player-choice prompts and narration; readers flagged where replies lacked visible prompts, and P0/P1 verification always used A1. Narration time-markers present only in A1 (e.g. Event 021's second-year flashback) were noted where relevant.
- **Unresolved identifications** left open by the source: the friend Temari defends in support S2-0001; Misuzu's «あの子» in S3-0041; the referent of China's «家族» in S3-0075; whether 「花海さん」 in Hiro's produce event activity_009 is Ume (auditor: Ume, from context).
- **Source anomaly:** `adv_live_hmsz_001_start-03-01.txt` labels two Misuzu lines 佑芽 in the raw script; no canonical text misattributes them.
- **Kaya Rinha:** routing gaps noted only (three Misuzu–Rinha mentions not routed in the crosswalk); dossier not evaluated.
- **Severity calibration** is a judgment; several P1/P2 boundaries are recorded with medium severity-confidence in the register.

## 10. Recommended correction batches

These are proposals for owner-reviewed follow-up; this audit performs none of them. Each uses the project's claim-revision vocabulary (addendum / correction note, not silent body edits).

| batch | scope | artifacts | primary sources to recheck | significance | dependencies / owner review |
|---|---|---|---|---|---|
| **B1 Attribution and branch fixes** | HSCA-005, -006, -046, -015, -089, -151 and the P3 locator errors | Sumika core §8/§23 + C07; RS-I §4.2/§4.12; Events 001–005 §6.7/§9.1; Saki core v2.1 L493/L508 + SAKI-L058; five support readings + two state ledgers (pronouns); Hiro friendship rows; China/NPC ledger (Kanae) | Sumika `dear_014`; `event_001` main-02/05, `event_004` main-01; `unit_01-04_04`; support readings' Mao passages | Removes statements that are wrong on the source; smallest edits | Pronoun fix should be one coordinated change; owner review advised for B1 because it touches a recent correction (PR #531) |
| **B2 U1 Episode-04 character homes** | HSCA-001, -004, -026 (+ Sena "mirror" talk, Temari U1 points) | RS-I §5; RS-II §8; Character/Relationship State Ledgers (U1 rows for Misuzu, Sena, Kotone); shared spine §8.4 | `unit_01-04_08`, `_14`, `_16`, `_20`, `_22`, `_23`, `_04`, `_10`, `_11` | Same class of gap PR #531 fixed for Saki | Keep U1 track-scoped (C-class per continuity map) |
| **B3 Cross-track state rows** | HSCA-002, -003, -058, -059, -064, -069, -032, -013 | State ledgers (new cross-track rows for Saki in D-UME/D-SENA, Sena in D-SAKI/D-TSUBAME, Misuzu/Temari in D-SENA/D-MAO/D-CHINA, Ume in D-HIRO); Ume core §19 note; Sena OPEN-SENA-12 / SN-R18 update | listed Dear files in each finding | Answers open hypotheses the corpus itself poses (H-SAKI-05, OPEN-SENA-12) | Non-additive continuity: rows must stay track-labelled |
| **B4 Core narrowings (P2)** | e.g. HSCA-030, -040, -047, -052, -071, -073, -079, -086, -091, -098, -100, -016, -017 | respective cores / matrices via addenda | per finding | Refines theses without reversal | Can be done per character independently |
| **B5 Traceability (P3)** | locator, section and citation fixes | ledgers, locator tables | per finding | Documentation | Batchable; low risk |

## 11. Reproducibility and validation

- Source verification: manifest SHA-256 recomputed and matched before indexing.
- Stage-A packets: 39/39 validated (identity, anchors, coverage). The coverage ledger records each object's packet, read status, candidate counts, explicit corpus citation count and linked register IDs.
- Stage-B outputs: 30 assignments; every routed candidate is assigned to exactly one primary record (checked by script in each assignment).
- Consolidation: duplicates merged into eight clusters; orchestrator overrides recorded per finding in the register.
- **Process limitations disclosed:** (a) the Stage-B calibration pass-1 was not fully blind (§8); (b) several runs were interrupted by usage limits and resumed from saved work — two readers wrote some candidates after resumption from already-read context (anchors validated); (c) Stage-B helpers shared a scratch area and at least two helper files were overwritten (canonical outputs unaffected; one per-candidate appendix lost, bucket counts preserved); (d) one auditor wrote its summary by script after a tool refusal before the brief forbade routing around refusals.
- Principal **false-positive mechanisms** observed (and filtered): character merely mentioned or dreamt of (counted COVERED/false positive); readers over-reading comic or branch-mixed lines in Produce Events; treating an uncited scene as an omission although its consequence was synthesized elsewhere; identifying unnamed referents too confidently.

## 12. Executive summary (questions A–E)

**A. How complete are the existing character reconstructions?** High for every character on its own-bundle material; COVERED dominates every assignment (e.g. Kotone 178 of 217 candidates, Temari 241 of 273, China 128 of 159, Tsubame 116 of 157). Completeness drops for material in other idols' tracks and U1, where Sena (33 entries), Saki (32), Ume and Misuzu (22 each) carry the most gaps. Kotone (11) and Hiro (12) are the most completely reconstructed. Document length was not used as a proxy.

**B. Most significant omissions.** The six P1s in §7 (HSCA-001 to -006), each with Japanese anchors and destinations. Newly discovered: all six. Historically corrected: Saki's U1 Episode-04 nightmare/insomnia (PR #531), Ume's U1 evidence in RS-I, the Hiro AV misattribution.

**C. Systemic failure modes.** Supported by the evidence: (1) cross-track states and U1 sub-arcs not harvested into character-facing homes; (2) attribution/branch-gating errors (dub, choice gate, pronouns, self-report as fact); (3) relationship asymmetries where only one side is recorded (Temari's mirror jealousy, Sena-side readings, Mao–Rinami). Not supported as systemic: dream handling, source-family bias, Japanese-nuance loss (only P3 items).

**D. Reliability of the strongest conclusions.** All thirteen core theses survive. Narrowing is needed for: Ume's career-agency claim; Sena's stat-vision accuracy and "perfect crown since childhood"; China's "not deprivation"; Tsubame's origin and "love" attribution; Rinami's "ambition is new"; Hiro's origin/dream timing; Misuzu's origin sequencing; Temari's win-anchored self-love; the Lilja–Sumika Dear 014 mechanism. These are findings; the cross-track generalizations (e.g. Sena's abdication as an invariant) are inferences flagged as such in the register.

**E. What to correct first.** B1 (attribution and branch fixes; smallest, removes wrong statements) → B2 (U1 Episode-04 homes for Misuzu, Sena, Kotone) → B3 (track-labelled cross-track state rows answering the corpus's own open hypotheses) → B4 (per-core narrowings) → B5 (traceability). No comprehensive rewrite is warranted.
