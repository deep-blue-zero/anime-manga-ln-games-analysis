---
series: IMOSAE
artifact_type: evidence_index
scope: V01-V14_primary_identity_normalization_and_attribution_corrections
generation: V1
status: canonical
source_boundary: Locked Japanese main-series EPUBs and frozen paragraph/ruby/gaiji routes; no new primary release
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.5'
date: '2026-10-13'
---

# Primary identity and normalization errata

This is an analytical correction layer for current retrieval. It preserves all frozen source/normalized bytes and prospective documents. It is not another current series entrypoint, a new normalized release, or authority to edit the curation-owned character registry.

| Japanese identity | Primary reading / current retrieval | Historical analytical hazard | Original ruby witness |
|---|---|---|---|
| 三田洞彩音 | Ayane Mitahora / みたほらあやね | Mitsudou surname misreading | `V03\|chapter:番外編 羽島伊月の誕生\|spine:049\|xhtml:OEBPS/Text/p-0049.xhtml\|p:0069\|fp:2cc5b0f61725` |
| 相生初 | Ui Aioi / あいおいうい | Hajime misreading; never merge with Aoba | `V06\|chapter:新人賞授賞式\|spine:050\|xhtml:OEBPS/Text/p-0050.xhtml.xhtml\|p:0126\|fp:7d44a2d7bad5` |
| 笠松青葉 | Aoba Kasamatsu / かさまつあおば | Aoba/Hajime conflation joins two different authors | `V06\|chapter:新人賞授賞式\|spine:050\|xhtml:OEBPS/Text/p-0050.xhtml.xhtml\|p:0140\|fp:267d07345ca9` |
| 白川京 | Miyako Shirakawa / しらかわみやこ | Kyo is a legacy analytical alias, not the given-name reading | `V13\|chapter:新人編集者、白川京\|spine:010\|xhtml:text/part0009.html\|p:0005\|fp:ced1e28357a8` |

The named witnesses were reopened in original XHTML; their ruby matches the frozen sidecar. Current work uses corrected names and maps older aliases explicitly. Frozen readings/checkpoints keep historical formulations. Targeted mutable-ledger fixes must log identity/citation repair separately from thematic revision. The global registry/index remain sole-writer curation outputs; a reviewed discovery handoff will carry these corrections rather than a manual upsert.

## G005: replacement-semantic exception

- Canonical paragraph: `V14|chapter:青い小鳥たち|spine:042|xhtml:text/part0041.html|p:0166|fp:f825ffa55e0b`.
- Original asset: `images/00027.jpeg`; SHA-256 `553f0fe232d962939fce54a6313b04c16471ef5b253ca08cfdaa65d57cb348b5`.
- Frozen map/retrieval replacement: **吐**.
- Primary witness: the original mouth-plus-seven scolding glyph, ruby **しか**, and Takashina's corrective coaching context.
- Analytical correction: read **scold**, with an original-glyph notation where quoting; never describe vomiting.
- Status: **confirmed analytical exception**; raw/NORM/GAIJI-MAP releases unchanged. A future source-domain correction needs its own versioned release/delta; this document does not quietly publish one.

The error demonstrates that stable fingerprints and valid locators are compatible with a wrong semantic substitution. Audit status must therefore be scoped to what was actually tested.

## Narrative nesting is not a normalization mutation

The package class MAIN_NARRATIVE for 青い小鳥たち remains unchanged. Its apparent future is revealed in the same volume to be Itsuki's manuscript. Register TF means that the text represents those events within a draft, not that their future occurrence is canon. LF remains linguistic fact. Chihiro's actual secret astronaut goal and Kazuko's actual pregnancy are in the returned present; achieved astronaut career, divorce, Miyako CEO status and teenagers' private lives stay draft-only.

## Further identity audit boundaries

Other significant figures require name-ruby and role review before broad reconstruction. This wrapper does not certify every romanization in inherited prose. Shiori is 栞; Natsume is 棗; alternate/fictional identities must retain their levels. Newly corrected current identities are routed here while earlier source-bounded monographs remain intact.


## Extended V14 roster and identity witnesses

These corrections include mistakes discovered in the newly authored reading; they are not all assertions that old project prose used the same spelling.

| Identity | Original reading / distinction | Witness |
|---|---|---|
| 神戸聖 | Gōdo Satoshi / ごうどさとし; Kanbe/Kobe/Hijiri are not supported here | V14 roster p0221, and novice-feedback p0035 |
| 城ヶ峰信長 | Shirogamine Nobunaga / しろがみねのぶなが | V14 roster p0221 |
| 木曽撫子 | Nadeshiko Kiso / きそなでしこ; なでこ is nickname | V14 household p0071 and roster p0221 |
| 八坂優羽 | Yū Yasaka / やさかゆう; no final ha syllable | V14 roster p0221 |
| 和泉颯太 | Sōta Izumi / いずみそうた | V14 industry p0024 |
| 神坂蒼真 | Misaka Sōma / みさかそうま, former pen name of Izumi | V14 ３年後 p0010 |
| 漬物ステーキ | Current pen name of the same writer, Tsukemono Steak | Same two identity passages |
| 熊野愛果 | Manaka Kumano / くまのまなか; Mana is nickname | V14 Comiket p0055 |

Exact roster route: `V14|chapter:報いの虹|spine:036|xhtml:text/part0035.html|p:0221|fp:62a9a44e4823`.
Izumi identity route: `V14|chapter:仁義なき業界|spine:022|xhtml:text/part0021.html|p:0024|fp:e47d6617d02e`.
Former pen name: `V14|chapter:３年後|spine:011|xhtml:text/part0010.html|p:0010|fp:b7658b9a93ad`.
Nickname witness: `V14|chapter:おっぱい|spine:014|xhtml:text/part0013.html|p:0071|fp:84860febe55b` is the observed canonical route.
Manaka witness: `V14|chapter:パンツをかぶる日|spine:028|xhtml:text/part0027.html|p:0055|fp:fef956e6963e`, including exact ruby in the validation. Current references should use those exact audited coordinates, not the short table's paragraph label alone.

## E023 attribution refinement: a requested division is not an explicit reply

The frozen V14 reading's E023 register labels the speaker field “Nayuta direct request and Itsuki response.” The exact five paragraphs directly show Kazuko receiving the completed book, asking Itsuki to take housework and Sora's care, stating the wish to write, and rising as 可児那由多. They do **not** explicitly narrate his answer. The next scene jumps roughly a year to the award. Subsequent creative production is established; exact acceptance wording and sustained household allocation are unshown.

Current retrieval must therefore read the speaker field as **Nayuta/Kazuko's direct request; Itsuki is its addressee; no explicit reply in this unit**. Retain the stable E identifier, source coordinates and all frozen prose/checkpoint bytes. This is an attribution/precision correction, not a changed claim that the sequel exists or a retrospective invention of refusal. Mature specialist drafts that had said he explicitly agreed were tightened before release.

Primary route: `V14|chapter:報いの虹|spine:036|xhtml:text/part0035.html|p:0035|fp:1f6988b28f1d` through `V14|chapter:報いの虹|spine:036|xhtml:text/part0035.html|p:0039|fp:2ebde1f8319d`. Immediate continuation: `V14|chapter:報いの虹|spine:036|xhtml:text/part0035.html|p:0041|fp:5c3d91335cc0`. Fresh original-XHTML base/ruby readback matches the five frozen surface paragraphs. The unquoted dash-led wish is attributed as speech by the following そう言って; quotation marks alone do not distinguish spoken from internal language.

## Reconstruction-stage additional identity witnesses

| Identity / address | Original ruby and current use | Exact witness |
|---|---|---|
| 羽島和花 | のどか / Nodoka Hashima, Itsuki's deceased birth mother; do not guess Waka from the kanji | `V10\|chapter:墓参り２\|spine:047\|xhtml:OEBPS/Text/p-0047.xhtml.xhtml\|p:0002\|fp:1a3146f5e5a7` |
| 絹恵 | きぬえ / Kinue, the name used by Kaiko's parents; same subject, not another creator | `V05\|chapter:実際にこういうミスが何度もあったので各編集部はもっと気をつけてくださいマジで\|spine:035\|xhtml:OEBPS/Text/p-0035.xhtml\|p:0128\|fp:81e322abf775`; explicit parental name assertion at p0134, fp:69a26f3e7609 |
| 木曽義弘 | きそよしひろ / Yoshihiro Kiso, older writer; distinguish from 木曽撫子 | `V06\|chapter:新人賞授賞式\|spine:050\|xhtml:OEBPS/Text/p-0050.xhtml.xhtml\|p:0158\|fp:8f27a8a68337` |

All three witnesses were reopened in original XHTML and compared to sidecar ruby during Phase D. A newly drafted readiness row's unsupported Nagisa label was corrected before model publication. This does not assert that the frozen prospective readings had used that label. Original source and historical analytical bytes remain unchanged.

## Kasuka Sekigahara and Yū Yasaka: separate identities

Original ruby verifies **関ヶ原幽 / せきがはらかすか / Kasuka Sekigahara**, the deceased female author. The inherited English analytical label **Yuu** is a legacy misreading for her. Current retrieval uses Kasuka and maps that alias explicitly; it never merges her with the actual child **八坂優羽 / Yū Yasaka**.

Primary name witness: `V07|chapter:ＴＨＥ ＬＡＳＴ ＣＲＹ ＩＮ ＨＡＤＥＳ|spine:039|xhtml:OEBPS/Text/p-0039.xhtml|p:0047|fp:10a43efe606a`; the next paragraph at p0048, fp:9ecd22773e55 supplies the cohort/award ages. Original V12 p0005 of ロストマン also gives 幽 / かすか, and V14 mainline recollection repeats that reading at `V14|chapter:ママ友とパパ友|spine:026|xhtml:text/part0025.html|p:0029|fp:2013c8cea642`.

The actual V14 family roster calls Yū the **daughter** of Kaizu/Ashley: `V14|chapter:ママ友とパパ友|spine:026|xhtml:text/part0025.html|p:0004|fp:9c1f590c48b7`. A new visual-specialist draft's son label was corrected before publication.

Inside Itsuki's draft, adolescent Yū says she received the parents' deceased friend's name and fears being a substitute: `V14|chapter:青い小鳥たち|spine:042|xhtml:text/part0041.html|p:0307|fp:05a0f58e0a86`. This does not establish Kasuka's legal name, an actual mainline naming history, a homophony of 幽 / かすか and 優羽 / ゆう, or actual parental replacement intent. A new family-specialist draft's unsupported sound/gender inference was corrected. Frozen V14/prior readings and checkpoints retain their bytes; this layer governs present interpretation.

## Setsuna: no supported later female reclassification

Fresh original checks verify that V01 introduces 恵那刹那 as a 少年 and uses 彼, with age16 at `V01|chapter:神|spine:033|xhtml:OEBPS/Text/p-0033.xhtml.xhtml|p:0018|fp:f220991e272b`. V14 again uses 彼 at the offer acceptance and gives age22: `V14|chapter:シリウス|spine:034|xhtml:text/part0033.html|p:0001|fp:6889d7b24f14` through p0002, fp:c31efcde9d15. No gender-change event is established here.

An unsupported later-female assertion entered new narration/readiness drafts from private continuation notes; it was corrected before publication. The frozen V14 reading already used he and its bytes did not need correction. Self-reference 自分, appearance change and artist skill are not independent gender evidence. Current models must preserve the actual dated source rather than manufacture a reclassification.

## Final source audit: both G005 occurrences

The all-volume sidecar/asset audit identifies exactly **two** occurrences of the shared G005 image: the V14 route above and `V01|chapter:メインテーマ|spine:027|xhtml:OEBPS/Text/p-0027.xhtml.xhtml|p:0007|fp:d3407c9304cc`, original block `/html/body/div/p[9]`, asset `OEBPS/Images/embed0018.jpg`. Both original blocks resolve, both assets have SHA-256 `553f0fe232d962939fce54a6313b04c16471ef5b253ca08cfdaa65d57cb348b5`, and both carry **しか** ruby. The graphic was visually inspected as mouth-plus-七, conventionally scolding 𠮟/叱 rather than the frozen 吐 substitution.

The [exact two-occurrence exception](machine_readable/IMOSAE_G005_ANALYTICAL_EXCEPTION.json) is metadata for current interpretation. Ordinary Unicode 吐 elsewhere is unaffected. All fourteen RAW/NORM payloads and the frozen gaiji map/inventory retain their bytes; this exception does not publish a new normalization release.

## Late voice/role distinctions confirmed during terminal review

| Unit | Current primary-supported reading | Hazard / ceiling |
|---|---|---|
| E008 | Haruto recognizes **Miyako's** accomplishment; she acknowledges her own work and sets the next Itsuki-book publication gate, whether or not it surpasses the cherished work | Not Haruto's own adequacy, not his book as the condition, not universal editorial competence |
| E009 | Haruto knowingly gives a different condition in LINE to **Itsuki and Chihiro**, for a mixture of spurring and irritation | Not the real promise to Miyako; private fit appraisal is not her knowledge |
| E024 p0066 | Miyako reports that Ui and Chihiro have drawn back from **romantic pursuit** | A candidate-review interpretation briefly confused this with career retirement. Ui's opening high-output work and this romantic report coexist; complete private emotional release is unprinted |
| E024 p0118–0125 | Nayuta actually writes the nominated fictional sequel 『どんな星空よりも、どんな思い出よりも』; GF asks Itsuki's publication permission and he agrees | Fourteen-year-later setting is inside a fictional world. The publication assent answers a different question from E023's unprinted care reply; it does not document the household division |

Exact withdrawal route: `V14|chapter:報いの虹|spine:036|xhtml:text/part0035.html|p:0066|fp:853396bf0e1e`. Ui's dedicated-writer report: `V14|chapter:３年後|spine:009|xhtml:text/part0008.html|p:0035|fp:fe689786bf44`; Aoba's student/reduced-output report is preceding p0034, fp:b74c78385777. The latter belongs to E002's cohort context rather than E003's household scene. Native base/ruby and attribution were checked; new models/terminal references were synchronized before publication.

V12 Aoba's E063/E064 dream-frame evidence is distinct from the awake E065/E066/E068 refusal. The direct refusal is `V12|chapter:笠松青葉ルート（罠）|spine:011|xhtml:text/part0010.html|p:0120|fp:59def94b752a`. No alternate sexual event becomes actual romance. Current treatment is non-graphic and does not expand the source's continuity.
