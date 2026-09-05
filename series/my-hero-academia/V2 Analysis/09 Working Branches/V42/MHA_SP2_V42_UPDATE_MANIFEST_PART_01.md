---
series: MHA
corpus: MHA_SP2
artifact_type: update_manifest
scope: V42
generation: V2
method_generation: V2.1
status: PROVISIONAL
proposed_status_if_promoted: canonical
source_boundary: Japanese manga Volume 42, narrative V42:p005-p183; V42:p145 authorial paratext; V42:p184+ non-narrative publication/end matter
do_not_use_as_current_authority: true
supersedes: []
superseded_by: []
intended_canonical_home: series/my-hero-academia/V2 Analysis/08 Audits and Manifests/MHA_SP2_V42_UPDATE_MANIFEST.md
---

# MHA SP2 — Volume 42 Update Manifest (Provisional Working Draft)

## Tranche state

**PROVISIONAL WORKING PACKET / NOT CANONICAL MHA AUTHORITY.**

This manifest records the proposed canonical consequences of the Volume 42 second-pass reading. It does not mutate any canonical cumulative target.

The continuing MHA route is `series/my-hero-academia`.

### Critical dependency

Volume 41 is currently a provisional working tranche. Therefore the canonical cumulative high-water mark remains Volume 40 even though a full V41 draft exists on the series branch.

V42 must not be promoted by applying V42-only ledger changes directly onto V40 state.

A future promotion has two safe forms:

1. **Sequential promotion**
   - promote/reconcile V41 first;
   - re-fetch every resulting target blob;
   - regenerate V42 patches from that new V41-complete state;
   - then promote V42.

2. **Joint atomic reconciliation**
   - resolve V41 then V42 semantics in chronological order inside one reviewed transaction;
   - verify every final cumulative target contains both tranches without losing intervening changes.

The working proposal files deliberately avoid stale target SHA claims for this reason.

---

## Source closure

- Canonical source: `My Hero Academia - Vol. 42 [Japanese].cbz`
- Drive ID: `1HiFWIMVIizGLbqlfVmK1xvTSwA3Rqi9O`
- File size: **89,885,814 bytes**
- SHA-256: `969bd3ca1df7cea2f2e6e2aae16eae77c4717d82c09f7ee372f22a5d195b86c3`
- Archive topology: **193 JPEG logical pages + `ComicInfo.xml`**
- Narrative start: `V42:p005`
- Narrative endpoint: **`V42:p183`**
- Chapters: **423-431**
- `V42:p145`: authorial interstitial/paratext, not in-world source evidence.
- `V42:p184+`: non-narrative publication/end matter.
- No later adaptation or derivative source used.

### Chapter closure

| Chapter | Title | Start |
|---|---|---:|
| 423 | `OFA vs AFO` | `V42:p005` |
| 424 | `エピローグ` | `V42:p023` |
| 425 | `季節外れの` | `V42:p039` |
| 426 | `地獄の轟くん家・FINAL` | `V42:p055` |
| 427 | `死柄木弔とはなんだったのか` | `V42:p071` |
| 428 | `笑顔が好きな女の子` | `V42:p087` |
| 429 | `私が来た！` | `V42:p104` |
| 430 | `僕のヒーローアカデミア` | `V42:p124` |
| 431 | `More` | `V42:p146` narrative / `p148` chapter-title page |

---

## Governing analytical transition

**V41 provisional:** `agency without self-sufficiency`

**V42:** **shared responsibility that makes ordinary selfhood possible**

> Distributed heroism is not the endpoint for its own sake. Its social value is that responsibility can be spread across professionals, institutions, civilians, teachers, friends, families, technology, and memory, reducing the need for any one person to be totally consumed by power, crisis, inherited role, trauma, guilt, or heroic identity.

Supporting rules:

- recognition can succeed in one dimension while rescue fails in another;
- accountability does not require dehumanization;
- atonement does not entitle the offender to forgiveness;
- memory should prevent recurrence without erasing difficult persons or relationships;
- good institutions and ordinary initiative are complements, not substitutes;
- power can leave the body without erasing the self;
- mature heroic society preserves differentiated expertise and ordinary life.

---

## Major state closures

### Final AFO / Shigaraki / rescue state

1. AFO's final control trajectory is defeated.
2. Tomura Shigaraki re-emerges as meaningfully distinct from AFO before death.
3. Tomura preserves the `死柄木弔` identity and asks Midoriya to convey a message to Spinner.
4. Tomura dies; no rehabilitation future is available.
5. Midoriya explicitly refuses to forgive Tomura's acts.
6. Midoriya explicitly says he could not save Tenko's **life** (`命`).
7. A separate supportive interpretation says his **heart** may nevertheless have been reached/saved.
8. The final rescue result is therefore multidimensional rather than a binary success/failure.

### AFO

9. AFO's attachment to Yoichi is explicitly affective and intense.
10. The attachment remains structured through permission/ownership rather than respected separateness.
11. Midoriya rejects the Demon Lord self-mythology and reduces AFO to a lonely human moral actor.

### OFA / Midoriya

12. OFA embers remain immediately after the final transfer/expending process.
13. The embers later extinguish.
14. Midoriya spends years Quirkless.
15. He becomes a U.A. teacher.
16. He later receives an advanced support suit produced through combat data, engineering, international collaboration, and classmate funding/support.
17. He resumes direct hero work while remaining a teacher.
18. Teaching is explicitly shown as a vocation he believes he would value even if OFA had remained.

### Todoroki family

19. Toya is terminally dying in Chapter 426.
20. Endeavor explicitly recognizes his failure to see Toya.
21. Endeavor commits to lifetime compensation/apology.
22. The family does not provide a universal forgiveness/reconciliation certificate.
23. Shoto explicitly roots self-authorship in Class A support.
24. Shoto/Toya share an ordinary soba preference.
25. Chapter 431 references Toya's memorial/altar, strongly implying death during the intervening years; exact off-panel timing remains open.
26. Adult Shoto discovers ordinary preference and a self beyond even `なりたい自分`.

### Spinner / villain memory

27. Spinner states Tomura was his hero.
28. Spinner questions whether he might have done more to save Tomura.
29. Spinner chooses writing as historical preservation.
30. The final memory model distinguishes stopping propagated sorrow from erasing the past.

### Ochako / Toga / Midoriya

31. Toga's death remains a real grief object for Ochako.
32. Ochako's postmortem Toga experience is psychologically/relationally strong but literal vestige metaphysics remains unconfirmed.
33. Ochako's adult counseling work is both Toga-informed and self-chosen.
34. Midoriya recognizes a specific desire for more contact with Ochako.
35. Ochako reciprocates.
36. The ending provides strong mutual romantic closure without an explicit on-page formal dating/marriage label.

### Hero society

37. A new endangered child structurally tests whether society learned from Tenko's abandonment.
38. The old woman who previously failed to help Tenko intervenes this time.
39. Civilian initiative is paired with institutional reform rather than substituted for it.
40. Postwar society shows Quirk-counseling, anti-discrimination, reconstruction, education, professional-hero, public-safety, and technological adaptation.
41. Adult hero work remains necessary; `ヒーローが暇な社会` is directionally approached, not fully achieved.
42. `WE ARE HERE` persists as a plural social-action principle, not as an explicitly formalized slogan/doctrine.

### Kurogiri / Eri

43. Kurogiri does not resolve into a pure Shirakumo-restoration endpoint; final action remains consistent with mixed identity/continuity.
44. V42 does not establish a major later medical catastrophe from Eri's horn contribution; exhaustive Quirk-medical closure remains absent.

---

## Critical first-pass correction

The most important wording correction is:

`転弧の命を救ける事は できませんでした`

This means:

> Midoriya could not save Tenko's **life**.

It does **not** mean:

> Midoriya could not save Tenko's heart.

The text then separately allows the interpretation that the heart was saved/reached.

Any earlier note, summary, or derivative analysis that substitutes `心` for `命` at this point should be marked `REJECT / CORRECT`.

---

