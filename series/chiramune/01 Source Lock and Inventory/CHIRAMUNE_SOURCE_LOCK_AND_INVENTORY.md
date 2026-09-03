---
series: CHIRAMUNE
artifact_type: source_lock_and_inventory
scope: ACQUIRED_JAPANESE_EPUB_CORPUS
source_boundary_date: 2026-08-29
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune source lock and inventory

## Authority and location

This document is the Git-side routing record for the acquired Japanese *Chitose Is in the Ramune Bottle* source corpus. It does not contain or replace the EPUB source bytes.

- Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`
- Chiramune source folder: `1bI8p0tRpD7_u6Xi3vubqydl-jR7gJFxx`
- Drive audit manifest: `1Oq8MhiuNApwg-qv9PxEfJG9YTzLuZy52`
- `audit_manifest.json` SHA-256: `e4d302d662997ae67be9368d45dd2dc7fefd5918f5c8540cbe82a897c00a8231`
- Audit date recorded by manifest: `2026-08-29`
- Original series title: `千歳くんはラムネ瓶のなか`
- Author/creator metadata: `裕夢` (Hiromu)

## Locked inventory

| Role | Source object | Drive file ID | SHA-256 |
|---|---|---|---|
| main volume | Volume 01 | `11DXxG7Ca3ugbM6WyRLpAnLob31OH-HaE` | `440a634dac96f1a08ad698e1a6723dcf5075ff49ac8e2726be74c8ef50fce33d` |
| main volume | Volume 02 | `1YL_ucWYHXDmRlu7B7_FosaA3izp5a23u` | `521e764266f39d1f7be105711210badd6e0aba6d208878b5fe0d9961aeb7b056` |
| main volume | Volume 03 | `1pmpRNfflS675u6jxakP65mwYMYtUAj-w` | `7e161668c65aaaef324c07e64810227e880600b0db59111e6ce4219ed5f5e2af` |
| supplemental booklet | Volume 03 illustration and SS booklet | `1St3ayvwF-7uzbjk4xQT0074B9rwr4AyC` | `0edde35a6a9ec238c31aefc3ede00aca5ab1276a9d2c9eaa01a67da787eb70fd` |
| main volume | Volume 04 | `1k6G6EwwTthxdByyCwj5AkjUKOGFRBnI6` | `96113f9d92616084144ea06172ad5ea1dee54e1f5b53ed872a717d4e5bac4470` |
| main volume | Volume 05 | `1Tb9Oa2GbYykPqX0PcJqwU_wSX249yyEv` | `6266d27492bcc2a966ca3aa7fca98a47e9bd830a0e71cfeb62df4aeedf3efc7e` |
| alternate/supplemental edition | Volume 05 special edition | `1CUzsfbC57YmOJ2gvYkBZfzfqGjR4cMds` | `4cd54018dc4f9bde7fc34ee9efff01b5c22cfce2fedda5db579ac7c04aef767e` |
| main volume | Volume 06 | `1Ht_zhXrF3yaDW5Fr3zhvf72Q3JN9jBzt` | `f9bfe6dfd72ac2032b291c8b1a7b6e2a52e3a6e74f1b03cdcc0ffa33d3fb706b` |
| supplemental volume | Volume 06.5 | `1WzGkGeIr58Zj8fxuNqJm4n4thGGCeH9G` | `ab19b4561ad8486b95ba0bfdb489c2003736bcb8c3bcdade36bb9d1a3718b921` |
| main volume | Volume 07 | `1C9RUUVWKkt1gMUdjJS3WKH7fXvWq63XR` | `6c6018e65f021ecea9c9cafd464fa5b42e887e6317931162efedc01ac020edd1` |
| main + supplemental edition | Volume 08 special edition | `1yGrcEag09mib-lSly4WSXW0-vlP5Wsr4` | `124d66e237efd52873dca5bbff1141a56dcad30821365da69553b54e2955dc03` |
| main volume | Volume 09 | `1IQrypUsZEIgeqpMUpHVxU37BGSQfANot` | `3e2de8091542d4658884dd069ede4d64b9587248dbd1e3c30905684b435335eb` |
| side-story collection | Days of Endless Summer | `1YHn0YaSorG9SfZKw1JXjPMZeJQt0Yxpf` | `24a92c80666b95658a2c2e6ab03434996233cb9357cea9981da3fc6566455c39` |
| supplemental volume | Volume 09.5 | `1-lVx6za7q9cmGnWcI1j1xETFK-8g9reU` | `0f2ca4c31b19356f153a04b9c026ddba43f57a11c439b78d63f6cd44b9dbddb2` |

## Integrity state

The source audit records:

- 14 EPUB files;
- nine distinct numbered main volumes, Volumes 01–09;
- zero missing numbered main volumes through Volume 09;
- zero exact-duplicate groups;
- ZIP CRC checks passed for all 14;
- EPUB container checks passed for all 14;
- 11 packaging-conformant EPUBs and three packaging warnings.

Independent pre-bootstrap verification of the Drive-resident copies reproduced all 14 manifest SHA-256 values and confirmed that every EPUB container resolves to an existing OPF package. The three warnings affect Volumes 02, 03, and 04: their uncompressed `mimetype` member is not the first ZIP entry. Treat this as a packaging-order defect, not content corruption; preserve the original bytes rather than repacking merely to normalize the warning.

All 14 acquired EPUB package metadata records Japanese language (`ja`) and creator `裕夢`.

## Coverage decisions

### Volume 08

A separate regular Volume 08 EPUB is not held. The acquired special edition contains the complete Volume 08 novel plus its rough-illustration supplement, so the narrative witness is present. Do not count the absent regular-edition SKU as missing narrative content.

### Volume 05

Both the regular Volume 05 witness and a special-edition object are present. Use the regular witness for the clean mainline prospective reading unless a later source audit identifies a reason not to. Treat distinct special-edition SS/supplemental material separately after the Volume 05 mainline reading has frozen.

### Volume 03 booklet

The illustration/SS booklet is a separate acquired object. It should not be opened for analytical integration until the Volume 03 mainline reading has frozen and the booklet's story placement is classified.

### Half-volumes and side stories

Volume 06.5, *Days of Endless Summer*, and Volume 09.5 require publication/diegetic classification before longitudinal integration. Their existence does not authorize retroactive leakage into earlier prospective reading states.

## Completeness claim and limit

The current lock supports the claim **core Japanese light-novel corpus acquired through Volume 09/09.5 with the listed major supplements represented**.

It does **not** support the stronger claim that every retailer-exclusive purchase bonus or ephemeral promotional short story ever distributed has been acquired. Newly acquired official material must be added through a new source-lock revision with stable identity and integrity verification before it becomes part of the analytical source boundary.

## Git publication boundary

The EPUBs are primary-source artifacts and remain outside analytical Git. Git may contain original analysis, source hashes, stable Drive IDs, source locators, and narrowly necessary quotations under the project's publication policy. It must not become a mirror of copyrighted source text or illustrations.
