# Character Registry Comprehensive Audit — 2026-09-04

## Result

The audit confirms that `characters/registry.jsonl` was substantially underbuilt. It contained 34 reviewed subjects in 8 series/study scopes even though the repository held many more current-eligible, substantial character analyses.

The registry now contains 162 reviewed subjects across 25 scopes. This pass added 128 subjects: 103 supported by dedicated analysis and 25 supported by distributed analysis whose own current readiness authority explicitly places the subject at a high inclusion threshold. The generated `CHARACTER_ANALYSIS_INDEX.md` is the public discovery view.

No reconstruction-capability record was created. Discovery inclusion means only that substantial reviewed analysis can be found in Git.

## Audit boundary and method

The audit evaluated all 40 roots in `series/registry.json` and all 2,405 Markdown artifacts under `series/` at commit `2a412523e640db0c8d3e63b4bcb78d385b22d575`. The repository contained 2,948 files under `series/` in total.

Selection was fail-closed:

1. Evidence had to be a tracked regular Git blob with exact-case path resolution.
2. Markdown evidence had to begin with a complete current-authority quartet: `status: canonical` or `status: active_provisional`, `supersedes: []`, `superseded_by: []`, and `do_not_use_as_current_authority: false`.
3. A dedicated inclusion required a substantial character monograph, character reference profile, source-facing character core, character-specific longitudinal ledger, or an intentionally shared character study with a substantial independent section for the enrolled subject.
4. A distributed inclusion required an explicit high threshold in the series' own current readiness authority: Attack on Titan Class A, My Hero Academia `specialist_ready`, or One Punch Man `strong`. General cast presence, name frequency, a merely `emerging` model, or a plan for a future monograph was insufficient.
5. Identity, continuity, aliases, analytical dimensions, and coverage were bounded to what the evidence itself supports. Multi-subject artifacts were split into individual analysis-subject records only where the document deliberately gives each subject substantial analytical responsibility.
6. Historical, superseded, unclassified, incomplete-authority, evidence-only, and planned artifacts were not promoted.

The scan found 1,372 Markdown artifacts with the simple complete empty-supersession current quartet, 704 with nonconforming or incomplete authority metadata, 204 explicitly historical/superseded artifacts, and 125 without a usable first front-matter authority block. Those corpus-wide counts are inventory context, not character-candidate counts.

## Registry delta by scope

| Scope | Before | Added | After | Inclusion basis or disposition |
| --- | ---: | ---: | ---: | --- |
| `86-eighty-six` | 0 | 16 | 16 | Canonical V01-V14 character reference profiles |
| `a-sisters-all-you-need` | 0 | 2 | 2 | Active-provisional V01-V06 character monographs |
| `aobuta` | 0 | 0 | 0 | Distributed ledgers exist; no dedicated or explicit high-readiness subject surface |
| `ascendance-of-a-bookworm` | 0 | 0 | 0 | Character-analysis router exists; no completed qualifying analysis |
| `attack-on-titan` | 0 | 9 | 9 | Class-A distributed substantial subjects from the current readiness authority |
| `azur-lane` | 0 | 5 | 5 | Current character monographs; Prinz Eugen remains evidence-ready without a monograph |
| `blue-archive` | 11 | 0 | 11 | Existing reviewed distributed subjects retained |
| `chiramune` | 0 | 0 | 0 | Character-analysis router exists; no completed qualifying analysis |
| `classroom-of-the-elite` | 0 | 2 | 2 | Canonical Year-2 Ayanokōji and Horikita specialist syntheses |
| `gakuen-idolmaster` | 0 | 10 | 10 | Current Phase-3 source-facing character cores; Saki, Temari, and Kotone cores remain blocked by noncanonical/incomplete authority metadata |
| `genshin-impact` | 1 | 0 | 1 | Existing Furina monograph subject retained |
| `girls-band-cry` | 0 | 0 | 0 | Sequential V2 analysis is active, but the current state says character ledgers remain due and no dedicated/high-readiness subject surface exists |
| `henshin-metamorphosis` | 0 | 0 | 0 | Yoshida Saki analysis is substantial but uses non-vocabulary status strings and incomplete authority quartets |
| `idoly-pride` | 0 | 22 | 22 | Canonical V2 character-specific longitudinal ledgers; historical V1 deep dives remain excluded |
| `kimishinu` | 0 | 3 | 3 | Canonical Haru, Mimi, and Sheena monographs |
| `konosuba` | 0 | 0 | 0 | Distributed ledgers and checkpoints do not declare a high-readiness subject threshold |
| `legend-of-the-galactic-heroes` | 2 | 0 | 2 | Existing Reinhard and Yang monographs retained |
| `love-live-superstar` | 0 | 0 | 0 | Current distributed ledgers lack explicit high-readiness subject promotion; V1 monographs are historical |
| `lycoris-recoil` | 0 | 0 | 0 | V2 character reconstruction is initialized but unfinished; no qualifying monograph or high-readiness promotion |
| `maebashi-witches` | 7 | 0 | 7 | Existing reviewed subjects retained |
| `monogatari-series` | 0 | 5 | 5 | Canonical Araragi, Senjōgahara, Shinobu, Hanekawa, and Nadeko monographs |
| `my-hero-academia` | 0 | 12 | 12 | Current V2 subjects explicitly marked `specialist_ready`; historical V1 monographs are not used |
| `nana` | 0 | 0 | 0 | Two definitive character studies exist, but their status strings and authority quartets do not satisfy the discovery contract |
| `one-punch-man` | 0 | 4 | 4 | Current subjects at the explicit `strong` distributed-readiness tier; legacy monographs remain historical |
| `oregairu` | 0 | 0 | 0 | Eight current reconstruction models declare `canonical` and a false veto but omit both supersession fields |
| `oreimo` | 0 | 8 | 8 | Eight substantial subject sections split from the canonical shared core-character monograph |
| `redo-of-healer` | 0 | 0 | 0 | The substantive Keyaru/Keyarga deep dive is not materialized in Git; only its Drive-status pointer is present |
| `revue-starlight` | 0 | 0 | 0 | Ensemble ecology synthesis is substantial at group level but does not provide a dedicated or high-readiness individual-subject surface |
| `shine-post` | 0 | 7 | 7 | Five single-subject monographs plus separate Momiji and Yukine enrollments from their shared study |
| `shokugeki-no-soma` | 1 | 0 | 1 | Existing validated Soma model retained; current V2 additional subjects are only `emerging` |
| `shuukura` | 0 | 0 | 0 | Present corpus is historical/legacy and the series registry records no current entrypoint |
| `solo-leveling` | 0 | 5 | 5 | Whole-novel Jinwoo, Hae-In, Gunhee, Jinchul, and Jinho character models |
| `sound-euphonium` | 0 | 1 | 1 | Current active-provisional Kaori monograph; four other monographs are historical |
| `the-idolmaster-cinderella-girls-2015-anime` | 0 | 0 | 0 | Ensemble syntheses do not provide a dedicated or explicit high-readiness individual-subject surface |
| `the-idolmaster-cinderella-girls-mobile-games` | 9 | 3 | 12 | Added current Hayate, Mika, and Rika monographs |
| `the-idolmaster-cinderella-girls-u149` | 1 | 0 | 1 | Existing YonaiP anime subject retained |
| `to-be-hero-x` | 0 | 13 | 13 | Substantial co-primary subjects in nine canonical Phase-3 character syntheses; the X/Zero document remains blocked by an incomplete quartet |
| `wuthering-waves` | 0 | 1 | 1 | Cartethyia's current Git analytical corpus; the title-local index says Chisa and Lynae have no Git monograph |
| `youjo-senki` | 0 | 0 | 0 | Tanya deep dive is substantial but lacks the required first front-matter authority block |
| `yuru-camp` | 0 | 0 | 0 | Active sequential/ledger analysis has not promoted a dedicated or high-readiness individual-subject surface |
| `mass-effect` | 2 | 0 | 2 | Existing Paragon and Renegade Shepard study subjects retained |

## Important corrections to the earlier backfill audit

The earlier `CHARACTER_INDEX_V2_BACKFILL_AUDIT.md` was intentionally a filename-oriented owner-review candidate set. It remains historical evidence of that pass, but it is not a complete registry audit.

This audit corrects four material limitations:

- It recognizes character-specific artifact types and front-matter scope, not only filenames containing a narrow set of tokens.
- It splits shared multi-character studies into individual subjects where each has substantial analysis, rather than treating a filename such as `OREIMO_CORE_CHARACTER_DEEP_DIVE.md` or the Momiji/Yukine study as one synthetic character.
- It evaluates current V2 replacement evidence, notably IDOLY PRIDE's 22 canonical longitudinal ledgers, instead of promoting historical V1 deep dives.
- It applies explicit series-local readiness thresholds to distributed corpora instead of adding every character who appears in a ledger.

## Remaining remediation queue

The following are plausible future additions only after their current evidence contract changes:

- Oregairu's eight reconstruction models need complete supersession quartets.
- Henshin/Metamorphosis and NANA need exact status-vocabulary and quartet remediation before Yoshida Saki, Osaki Nana, or Komatsu Nana/Hachi can be reviewed for inclusion.
- Youjo Senki's Tanya deep dive needs a valid first authority block.
- Gakuen Idolmaster's Saki, Temari, and Kotone character cores need current-vocabulary, complete authority metadata or an eligible successor.
- To Be Hero X's X/Zero synthesis needs a complete quartet.
- Redo of Healer needs the substantive Keyaru/Keyarga artifact materialized, not only its status pointer.
- Wuthering Waves' Chisa and Lynae need substantive Git analytical artifacts; evidence readiness alone is insufficient.

These are not registry defects that can be repaired by inventing metadata inside `characters/registry.jsonl`. The qualifying analysis must first become current, materialized, and reviewable at its canonical path.
