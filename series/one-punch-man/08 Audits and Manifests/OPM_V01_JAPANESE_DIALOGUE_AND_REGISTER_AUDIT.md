---
series: OPM
artifact_type: audit
scope: V01
generation: V2
status: canonical
source_boundary: "Japanese tankobon Volume 1; Drive CBZ SHA-256 be3a749342e6c617ce0b9e55ed353ca5874c70df4f0467c27daf5b5215b7b3a0"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: 2026-08-24
---

# One Punch Man — V01 Japanese Dialogue and Register Audit

## Result

**PASS WITH MINOR MODEL REFINEMENT.** The V01 deep reading's substantive character conclusions survive line-level Japanese readback. Two voice descriptions required tightening:

1. Saitama's adult speech is not adequately captured by `plain/deadpan`. His default is low-formality, colloquial masculine speech, but he moves readily into rough contractions, insults, imperatives, and shouted forms when irritated; his twelve-year-old school speech also demonstrates context-appropriate polite forms.
2. Genos is not globally `formal`. He uses masculine `俺`, plain/rough tactical language toward enemies, and polite/deferential request forms toward Saitama. His unusually high information density is more stable across contexts than his politeness level.

No correction overturns the V01 publication-boundary thesis, Saitama's domain-specific engagement model, Genos's risk model, or the directional Saitama/Genos relationship state.

## Saitama — adult/current register

| Context | Japanese anchor | Register consequence | Locator |
|---|---|---|---|
| hero self-definition | `趣味でヒーローをやっている者だ` | deliberately ungrandiose self-presentation; lexical plainness contrasts with monster rhetoric | `OPM|V01|chapter:1|image:0020` |
| casual praise after Genos battle | `いやー助かったよ / すごいなお前！今の何？` | friendly colloquial praise; `お前` is familiar/plain here rather than intrinsically hostile | `OPM|V01|chapter:6|image:0130` |
| Genos arrives at apartment | `マジで来やがったか` | rough colloquial surprise; `〜やがる` marks irritation/resentful incredulity | `OPM|V01|chapter:7|image:0140` |
| hospitality with boundary | `飲んだら帰れよ` | minimal social accommodation paired with blunt imperative | `OPM|V01|chapter:7|image:0141` |
| Genos asks about body parts | `使ってねーよ` / `変わってんなお前` | contraction `〜てねー` and casual `お前`; direct but not ceremonially hostile | `OPM|V01|chapter:7|image:0141` |
| Genos comments on baldness | `ハゲてんだようるせーな!! / 何なんだテメーは!!` | sharp escalation under irritation: contracted rough forms plus hostile `テメー` | `OPM|V01|chapter:7|image:0142` |
| Genos's overlong history | `バカヤロウ / 20文字以内で簡潔にまとめて出直してこい！` | low tolerance for informational overload expressed as comic command, not passive deadpan | `OPM|V01|chapter:7|image:0143` |

### Diachronic caution

Pre-hero Saitama already uses `俺` and can become aggressively colloquial under chosen danger: `就活はやめだ` and `かかって来いコラ！` (`image:0042`). The twelve-year-old Saitama, however, uses ordinary school politeness to a teacher: `完全に忘れていたので今からやります` and `わかりません` (`image:0185`). Adult roughness should therefore be modeled as a developed/contextual register, not a timeless inability to use polite Japanese.

## Genos — conditional register

| Context | Japanese anchor | Register consequence | Locator |
|---|---|---|---|
| tactical judgment | `言葉を話すから人間程度の知能は持っていると思ったが… / 所詮は虫か` | plain internal/enemy-directed register; analytical and dismissive rather than polite | `OPM|V01|chapter:6|image:0129` |
| self-identification and request | `俺は単独で正義活動をしているサイボーグ ジェノスという者だ！` / `ぜひ名前を教えてほしい / 弟子にしていただきたい` | masculine `俺` coexists with deferential request morphology; politeness is relational, not globally formal | `OPM|V01|chapter:6|image:0138` |
| arrival at Saitama's home | `ジェノスです サイタマ先生!!` | explicit polite self-presentation plus immediate status assignment | `OPM|V01|chapter:7|image:0140` |
| Saitama rejects `先生` | Genos immediately substitutes `師匠！`; Saitama answers `師匠はやめろ` | Genos actively searches for a master label rather than merely mirroring Saitama's preference; strengthens directional asymmetry | `OPM|V01|chapter:7|image:0140` |
| request for instruction | `先生のように強くなる方法 教えてください` | direct deferential request; `先生` is relationship-defining from Genos's side | `OPM|V01|chapter:7|image:0146` |

### Information-density finding

Genos's long autobiographical explanation across `images:0142-0143` is not just exposition. The speech is syntactically continuous, causally ordered, and far denser than Saitama's preferred conversational bandwidth. Saitama's interruption therefore provides a partner-specific interaction rule: Genos defaults toward exhaustive explanatory completeness; Saitama prefers radical compression.

## Relationship-language finding

The language strengthens rather than weakens the directional relationship ledger.

- **Genos -> Saitama:** capability recognition is immediately translated into honorific/role language (`先生`, then attempted `師匠`) and deferential requests.
- **Saitama -> Genos:** he resists the imposed labels verbally while continuing to permit Genos's presence and eventually the apprenticeship structure.

Thus the relationship begins with **linguistic commitment from Genos preceding equivalent role commitment from Saitama**.

## Antagonist contrast

Vaccine Man's extended ideological first-person rhetoric (`私は…`) presents himself through explanatory/grandiose justification before Saitama answers with minimalist hobby-hero self-definition. This supports the V01 deep reading's rhetoric-versus-plainness contrast. The audit does not require a full antagonist voice model because most V01 monsters remain reconstruction-insufficient.

## Required corrections propagated

- `OPM_V01_DEEP_READING.md`: refine Saitama and Genos voice descriptions; add childhood/register contrast and `先生 -> 師匠` exchange.
- `OPM_SAITAMA_CHARACTER_STATE_LEDGER.md`: refine adult register from generic low-formality to conditional colloquial/rough behavior; add teacher-directed childhood politeness atom.
- `OPM_HERO_CHARACTER_STATE_LEDGER.md`: replace globally `formal` characterization with partner-conditioned mixed register; add enemy/Saitama contrast.
- `OPM_RELATIONSHIP_STATE_LEDGER.md`: add role-label negotiation as evidence of initial asymmetry.
- `OPM_CHARACTER_MODEL_READINESS_INDEX.md`: no readiness tier change; language breadth is better specified but still only V01.

## Promotion decision

**PROMOTE V01 TO CANONICAL.** Source identity, volume map, publication-boundary interpretation, line/register claims, character propagation, and relationship propagation have passed readback. Future volumes may revise longitudinal claims normally, but V01 no longer requires `active_provisional` status.
