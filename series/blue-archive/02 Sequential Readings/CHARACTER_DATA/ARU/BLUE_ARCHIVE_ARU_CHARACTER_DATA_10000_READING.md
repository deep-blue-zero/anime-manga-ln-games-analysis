---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: ARU_CHARACTER_DATA_10000
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:10000:profile_and_dialog"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Aru — ordinary complete written profile and contextual baseline

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10000:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/ARU/VARIANT_10000.md` | 1 complete profiles; 37 complete written contextual records, including blanks; `efda862b2d0a82219fa9bd5a087c295842d5ba9502dab92a8b029c152385b522`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.

Positive exact-name identity witness: `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10000` / DevName `Aru_default`, `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10031` / DevName `Aru_Newyear`, `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10089` / DevName `CH0240`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## Whole profile, identity and source extent

This object includes the complete structured profile, raw `LocalizeCharProfileExcelTable` DataList12, normalized profile SHA-256 `9e68ccc873f9c247ae251c07acf709b16385baac03685c5f0a72b3d91c6d9027`, as well as all 37 contextual records, raw `CharacterDialog` DataList480–516. The abbreviated canonical profile is supplemented by the full Japanese structured fields, not a Korean-to-Japanese synthesis. All 36 nonempty entries and **one blank title** are retained. `UITitle441` / DataList480 has empty text, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; no spoken silence is inferred.

The full name is 陸八魔アル, family reading `りくはちま`. This ordinary `Aru_default` record describes a Gehenna second-year, sixteen years old, birthday March12, height160cm, hobby **studying management**. Literal `Club=None` coexists with the gacha club label 便利屋68 and registry Kohshinjo68; it is not evidence she lacks the locally named club. The status “I solve anything” is an advertised offer, not demonstrated universal competence.

The introduction is **editorial profile text**, calling her the self-styled president of the Gehenna club, saying she runs unlawful business as she likes and wants to act a cool villain but readily exposes gaps. It grounds the aspiration/performance distinction without proving a verdict for every particular commission. Designer/illustrator DoReMi and actor近藤玲奈 are metadata, with no acted voice supplied. The SSR acquisition line praises the adult's choice. The complete Japanese weapon description names **ワインレッド・アドマイアー**, an old-fashioned sniper rifle she cherishes, whose hard-boiled effect is hedged “apparently.” Unlike the Korean field, the Japanese description does not independently state semiautomatic specification. The weapon enthusiasm cannot prove one-shot universal technical effectiveness.

## All contextual partitions and actual conditions

| Pool | Exact IDs and raw indices | Written repertoire and limit |
|---|---|---|
| Title / acquisition | `UITitle441`, `CharacterGet442`;480–481; Idle/rank1 | Blank title retained; acquisition accepts cooperation while declaring she is costly to hire. Not a price schedule or employment contract. |
| Café |443–447;482–486; Idle/rank15 | Imagines decorating her own office, asks rent, predicts a bright company future, recalls middle school without specifics, and wants a staff celebration here. Wishes, questions and memory reference are not completed renovation, measured rent or a full childhood history. |
| Ordinary lobby |448–454;487–493; Enter448–449 / Idle450–454; rank0 | Protective/service assurances, collaboration, ability-showing premise then correction, a tonight-date question then acknowledgment that no date was promised. The correction matters; no actual scheduled date or performed exchange is shown. |
| Birthdays |455–459;494–498; Enter455–457 / Idle458–459; rank0 | Confident adult birthday research, reaction to a mediated “yesterday” correction, then insistence today is right; own birthday reminder and fantasy it will become a Kivotos holiday. No actual wrong date, calendar reform or universal observance is established. |
| Holidays |460–464;499–503; Enter/rank0 | New-Year success promise, recollection of a commission to eliminate “Santa Claus,” a Halloween-like startle and denial. The commission's target/outcome and the object provoking surprise are unprinted; denial coexists with the text's exclamation. |
| Weapon |465;504; Idle/rank25 | “Anything in one shot” is acquisition bravado, not a weapon test or casualty result. |
| Special |466–477;505–516; Idle/rank0 | Twelve written telephone/performance entries parallel ordinary bondE006, alternating parenthesized wrong-number irritation and polite scheduling/accounting language. A repeated written pool is not a new call or an observed performed rendition. |

The Special object starts inside the performance, not with an independent full telephone transcript. It preserves the sushi-shop error, refusal-in-thought to deliver, long-call impatience and outward acknowledgment. The question whether this is a wrong number is mediated by her printed reply. Source typology and parenthesized text matter: source-access thoughts are not automatically heard by the caller or Sensei. Actual raw phone dialogue appearance in E006 supports comparison; UI repetition does not supply callers' missing words.

## Ordinary pleasure, objections and epistemic correction

The baseline adds low-stakes wants—office decoration, a team celebration, shared collaboration and recognition—alongside expensive-hire/protection claims and fear of exposure. The date-not-promised correction is a contrary instance to simply treating every implied plan as established. The birthday exchange likewise dramatizes asserted certainty and defensive correction without an independently printed adult utterance or full calendar.

Management study is a positive preference, not merely an explanation for business failure. Middle-school reminiscence is retained as a lead without invented details. The profile's broad unlawful-business framing cannot adjudicate the legal status of an unseen Santa commission, and playful hard-boiled weapon language cannot certify capability. Her warmth, aspirational confidence, comic defensiveness and practical curiosity can coexist.

## Proposed maintained deltas

Character and relationship surfaces can add decoration/celebration/study preferences and written date correction, keeping acquisition/lobby eligibility separate from enacted history. Institution proposals preserve self-styled presidency, club labels, rent question and bright-future aspiration without a ledger of solvency. Sensei ethics receives only contextualized offers and mediated exchange; no actual guard job, date or employment is admitted. Japanese voice/motif proposals distinguish public assurance, inner telephone irritation, correction and genre performance, with the blank title counted and actor metadata quarantined.

Compare the paired ordinary readings for rewards, persuasion, film, adviser invitation and wallet attachment; the profile does not independently reproduce those whole encounters or date them. Coverage proposal is exactly one complete written object, not37 separate stories. G08 preserves UI/Special reuse, G09 literal blank and mediated forms, G10 performance and G13 legal/technical limits. Reconstruction readiness and all shared controls remain unchanged.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
