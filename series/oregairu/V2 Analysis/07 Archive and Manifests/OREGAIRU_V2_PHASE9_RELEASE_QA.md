---
title: Oregairu V2 expanded corpus — release-candidate QA and owner review
artifact_type: release_qa_and_owner_review_record
generation: V2
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
release_id: OREGAIRU_V2_EXPANDED_v1.0-rc.1
release_state: candidate_pending_protected_main_integration_and_final_freeze
analytical_basis_commit: 8a2133822bf49077aa1eacb2a382ea16ab60b9ae
baseline_main_commit: cfddecb9b5b05ce7b5b25060673ed2e77639da6c
updated: 2026-10-17
---

# Expanded V2 release-candidate review

The intended literary expansion, original-suite audit and three additional bounded reconstruction specifications have been accepted and published on `series/oregairu`. This record prepares a versioned analytical release candidate. It does **not** certify protected integration, a post-merge main audit, global character enrollment or the final v1.0 freeze. Exact final package/source/audit state is recorded in the package's `PUBLICATION_RECEIPT.json` and `RELEASE_PROVENANCE.json`, rather than inferred from a local worktree.

The [registered corpus map](OREGAIRU_V2_DRIVE_CORPUS_MAP.md) remains the single current-state entrypoint. The [reader guide](../06%20Continuous%20Synthesis/00_README_AND_CORPUS_MAP.md) is subordinate navigation. The [completion record](OREGAIRU_V2_COMPLETION_AND_EXPANSION_STATUS.md) owns exact artifact responsibilities, claim transitions, candidate deferrals and the curator handoff. The [corpus manifest](OREGAIRU_V2_CORPUS_MANIFEST.json) supplies a reconciled inventory and payload checksums; its own bytes are covered by the package-level checksums, avoiding a self-referential digest.

## 1. Release identity and scope

No earlier materialized Oregairu ZIP, tracked release package or Git release-history event was found in the inspected repository history. This is not a claim about every external archive. The architecture's recommended `Oregairu_Definitive_V2_Multi_Document_Synthesis_v1.0.zip` remains a historical proposed final name. This expanded, unintegrated candidate instead uses **`Oregairu_V2_Expanded_Analytical_Corpus_v1.0-rc.1.zip`**. It preserves the intended v1.0 lineage while making its candidate status and additional scope explicit. A final freeze must bind the verified integrated state; it must not silently rename or mutate this candidate.

The package preserves the existing directories, identifiers, source locators and historical knowledge boundaries. It includes analysis and source metadata, never the Japanese EPUB/PDF/audio/image payloads or extracted source text. Repository license and third-party notices accompany it; their inclusion does not license the quoted fiction or underlying assets.

| Layer | Release responsibility |
|---|---|
| Mainline Japanese novels | Governing fictional evidence through V14.5, with story-level chronology rather than decimal-container ordering. |
| Qualified Watari-authored supplements | Existing Christmas prose/recording distinction and individually audited anthology stories retain their declared source authority and chronology. |
| Alternate continuities | Ketsu and other alternate-route fiction remain separate; no new alternate-continuity analytical scope is admitted. |
| Adaptations and guest-author fiction | Their own classified witnesses; neither silently becomes mainline character fact. |
| Interviews, production materials and paratext | Contextual evidence when separately acquired and classified; retrospective claims do not automatically override published fiction. |
| Literary corpus | Nineteen volume readings including the separately qualified Christmas study; six checkpoints; ten Phase-4 ledgers; twelve original specialists; Documents 13–14; six supporting monographs and one relationship/system study. |
| Reconstruction | Eight historically identifiable original models plus three additional bounded models. The 816-row shared everyday ledger comprises 722 original observations and 94 supporting additions. |

The original ending freeze remains Checkpoint E; post-ending durability belongs to the final post-14.5 checkpoint. V14.5 Stories 1–2 occur after V09 and before V10; Story 3 is late-V14 interstitial; only Stories 4–5 establish the true post-ending state. No source identity check supplies a new reading, listening, visual collation or admission.

## 2. Audit and reconciliation results

| Check | Result and actual boundary |
|---|---|
| Original Phase 8.5 suite | PASS for the audit's declared responsibility: complete eight-model specification review; representative Japanese verification; static 7×8 scenario discrimination; state/register, negative/OOD and risk-directed everyday-life checks. The audit is not an empirical external-generator benchmark. |
| Original model integrity | All eight current model SHA-256 values match the suite audit's acceptance table. Their supersession arrays are valid and empty; no prior authority edge was removed. |
| New literary/model acceptance | Complete-file independent reviews passed for SC01–07 and the three new models. Consequential claims were reopened at the exact Japanese source registers. Totsuka and Zaimokuza retain within-era knowledge limits; Miura retains Yui's lost V06 decision authority. |
| Shared evidence preservation | All 722 audited original row strings are byte-identical to `bcdd9d97b064e836970bd09a32815b796ea897da`; 94 reviewed observations were appended. All 816 exact cited members and normalized short anchors recover; new rows additionally passed exact fresh paragraph/source-hash checks. Anchor recovery is not blanket semantic recertification of 816 rows. |
| Frozen analysis | All 50 declared frozen items are byte-identical to baseline main: 19 readings, six checkpoints, ten Phase-4 ledgers, twelve original specialists, Documents 13–14 and the Phase-6 audit. |
| Authority/front matter | Eleven model authority quartets are canonical/empty/empty/false. New maintained artifacts have complete quartets. Older frozen artifacts with incomplete legacy metadata retain their bytes and scoped corpus roles; the inventory distinguishes machine classification from those roles. |
| Source identity | Fresh hashes for 53 unique payloads match the canonical inventory: 22 EPUBs, 17 governing PDFs, one alternate V7.5 PDF, three ancestor PDFs and ten Christmas recordings. This is byte identity, not fresh auditory or exhaustive visual inspection. |
| Source-record errata | The source inventory restores V12's complete digest and corrects the claimed unavailability of ancestor booklets. Available omitted stories remain unadmitted and substantively unanalyzed. |
| Synthesis qualification | `OREGAIRU-EXP-ERR-002` narrows frozen Document 14 §7's Kyoto certainty and object of avoided disclosure. SC04 preserves the ambiguous argument in Ebina's first understanding clause; no frozen active reading is falsely declared impossible. Document 13's current limits remain adequate. |
| Routing | Earlier model construction revisions/hashes in the maintained map are explicitly historical; current authority routes to the accepted audit/manifest. The original suite is closed, rather than mislabeled incomplete because later models qualify. |
| Duplicates | No byte-identical artifact duplicates. The deliberate shared SC04–06 acceptance paragraph is administrative provenance; no long exact duplicated analytical argument was found among the additions. |
| Truncation | Authors and independent reviewers read the new outputs completely and checked their endings, sections, tables, source registers and actor attribution. Ten missing final newlines are unchanged historical bytes, not new truncation; frozen files are not normalized. |
| Package/source boundary | All selected corpus members are regular UTF-8 text. Both Anthology 02 JSON files were recursively inspected and contain metadata/quality flags, not OCR body or encoded assets. No source containers, raw extraction, media or symlinks are selected. |
| Final candidate inventory and links | 85 corpus records; 83 selected corpus files plus two legal texts; 84 non-self artifact digests verified. All 136 relative Markdown file/directory links in that candidate selection pass. Four generated package records bring the expected archive to 89 members; actual post-publication build results belong to its receipt. |
| Advisory flag triage | Ten unchanged historical final-newline flags remain preserved. The historical handoff's local-path flag is excluded from the package. The scanner's additional extension flag is the explicitly reviewed UTF-8 reproduction helper; only that exact `.py` path is allowed by the packager. No unresolved advisory flag requires a frozen-byte edit. |

The applicable repository gate is:

```bash
python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/oregairu --repo .
git diff --cached --check
```

The authored milestones passed that gate and complete diff/path review before publication. Full source-audit → housekeeping → exact-head audit sequences are serialized; their actual run IDs and publication SHAs are in §5 and the final package receipt. Internal links/front matter must also pass for the final source tree, and the package builder independently checks links against the selected archive members. A local gate, successful source push or displayed workflow `main` label cannot substitute for the exact final status target.

## 3. Packaging and reproducibility

The manifest lists every corpus artifact, its role, byte count and SHA-256, with explicit package inclusion. Two retained Git artifacts are omitted from the reader package: the cold V1 conversation and obsolete Phase-4 handoff. No files are deleted or renamed in Git. All other current analytical/source-control records remain included, together with the final reader/release records and reproducible builder.

The historical transcript aliases `Manga and anime discussions - Oregairu Deep-dive - Full Transcript.md` and `Manga and anime discussions - Oregairu Deep-dive - Full Transcript(1).md` resolve to the [retained transcript at the verified baseline main commit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/cfddecb9b5b05ce7b5b25060673ed2e77639da6c/series/oregairu/V2%20Analysis/01%20Legacy%20V1%20and%20Source%20Control/Manga%20and%20anime%20discussions%20-%20Oregairu%20Deep-dive%20-%20Full%20Transcript.md). This provenance source is not current literary authority. No relative Markdown link in the included corpus requires either omitted file; frozen plain-text historical references are resolved by this alias note and the manifest.

[The release builder](OREGAIRU_V2_BUILD_RELEASE.py) reads only an explicit full Git commit plus the supplied publication receipt. It preserves the receipt's bytes, records its SHA-256 and distinguishes an observed main head from integrated source content. It does not query, grant or infer publication authority. The archive uses sorted paths, fixed `2026-10-17T00:00:00` timestamps, regular-file mode 0644 and ZIP_STORED compression. No creation clock or machine path enters its bytes. The builder creates the archive twice and requires equal SHA-256 values, then reopens the archive and verifies every member, CRC and checksum entry.

Reproduce with the included receipt and a checkout containing the exact published commit. Place the checkout in `anime-manga-ln-games-analysis/`, extract the receipt to its parent directory, and run there so receipt and ZIP stay outside Git:

```bash
OREGAIRU_RELEASE_SHA=$(python -c 'import json; print(json.load(open("PUBLICATION_RECEIPT.json"))["source_commit"])')
python "anime-manga-ln-games-analysis/series/oregairu/V2 Analysis/07 Archive and Manifests/OREGAIRU_V2_BUILD_RELEASE.py" \
  --repo anime-manga-ln-games-analysis --commit "$OREGAIRU_RELEASE_SHA" --receipt PUBLICATION_RECEIPT.json \
  --output Oregairu_V2_Expanded_Analytical_Corpus_v1.0-rc.1.zip
```

`PACKAGE_CHECKSUMS.json` covers the remaining archive members, including the Git corpus manifest, receipt and provenance. Its own digest is represented by the outer ZIP digest, avoiding a checksum cycle. Reproducing the analytical archive does not require bundling or redistributing the separately governed primary sources. Rechecking the source inventory itself requires lawful access to the same editions.

The builder also passed an isolated synthetic-Git fixture: exact-blob selection, two exclusions, self-byte binding, repeated deterministic output, full archive readback and representative Markdown forms. Invalid bytes, source-payload JSON, unapproved file types, unsafe/missing links, mismatched receipt source and failed audit states were rejected. These packaging tests are separate from literary/source acceptance and do not manufacture a production publication receipt.

## 4. OPEN work and exclusions

These limits remain visible rather than being converted into simulated facts:

- Numerical voice-marker calibration and empirical deployed-generator behavior remain unmeasured. Current scenario tests are static source/specification checks.
- Totsuka's private romantic/gender interiority and adult future, Miura's reciprocal romantic outcome and adult life, and Zaimokuza's prize/submission history, unobserved output and eventual vocation remain underdetermined. No new post-V14.5 state is invented for the three additions.
- Ebina, Kawasaki and Sagami have accepted literary studies but deferred full models. Their precise ELP, state/relationship, voice, schema and scenario obligations are recorded in their studies. Other candidates retain narrower evidence-governed responsibilities.
- Hayama-circle horizontal tie durability, private conversations, rumor originators, unperformed confession outcomes and later separations remain OPEN. A group mind or endpoint egalitarian conversion is not established.
- The available three omitted ancestor stories, other recordings/artwork and alternate layouts have only their declared inventory/genealogy or historical inspection authority. Availability is not admission or a fresh performance reading.
- 結3, `－刻－` and the campaign stories remain lawful acquisition/classification leads in the registered map. Another booklets and a V14.5 PDF were absent from the enumerated tree. These are not completion prerequisites for the admitted corpus. **Shin remains excluded.**

Final v1.0 freeze and global character enrollment are separate outstanding operations. The candidate must not be represented as a frozen, integrated main release.

## 5. Publication receipts and exact remaining route

| Milestone | Published series source | Validation / integration state |
|---|---|---|
| Administrative discovery repair | `122dc19ebe66d5ea0288eae8cc18ef67bbdb07ed` | Source 38983721021; housekeeping 38984161385; final audit 38984190231 succeeded. |
| Original-suite audit and source reconciliation | `bcdd9d97b064e836970bd09a32815b796ea897da` | Source 38984826780; housekeeping 38985086426; final audit 38985123066 succeeded. |
| Priority expansion | `be09809628ea216a56e766b73fb2acedada1a638` | Source 38985791247; housekeeping 38986223877; final audit 38986257362 succeeded. |
| Secondary expansion and attributable corrections | `8a2133822bf49077aa1eacb2a382ea16ab60b9ae` | Author preflight passed (`paths=7943`) and exact tree `f55e72503df8e54132f2cb592265bc62ce2f847e` was read back. Source 38986867127 and housekeeping 38987175270 succeeded; final audit 38987205689 must report successful exact-head status before release-metadata publication, with the result bound in the final receipt. |
| Release-candidate metadata/package | Exact source in packaged receipt | Must pass final author gate, published-tree readback, complete remote sequence and deterministic ZIP verification. No post-merge main success is inferred. |

All changes use the continuing `series/oregairu` branch and [PR #189](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/189). No force update, history rewrite, global-index authorship or primary-source redistribution is authorized by this record.

**Protected integration remains pending because the execution route is unavailable here.** The connected GitHub tools expose no targeted workflow-dispatch action. A manual merge cannot satisfy the publication policy's fresh access-surface review: collaborator enumeration, invitations, deploy keys, installed-app access and Actions-permission surfaces are unavailable through this connector. No controls are changed or bypassed. The [publication policy at the governing baseline](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/cfddecb9b5b05ce7b5b25060673ed2e77639da6c/governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md) requires checking every surface before a manual PR merge; user authorization for this analytical work is already present.

The legitimate next route is the existing `nightly-integration.yml` controller on main, `mode=apply`, `branch=series/oregairu`, or its existing 07:00 America/New_York schedule. An existing draft PR defers that route; the completed, audited release PR must be made ready deliberately. The controller then performs the live owner-only/access checks and protected integration. Completion still requires the returned main commit's exact reviewed-content comparison and successful explicit post-merge audit. The stable branch is retained; no unverified pruning occurs.

The configured character curator is paused and cannot be invoked here with an exact-tree assignment. Its documented handoff covers eight original and three additional models, their exact paths and the final published source SHA. Only that curator may enroll/review records and regenerate the character index. Existing outputs remain valid; global enrollment is explicitly pending. No reconstruction-capability registry or global capability grade is created.
