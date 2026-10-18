---
title: Yuru Camp Current Source Inventory
artifact_id: YURUCAMP_CURRENT_SOURCE_INVENTORY
artifact_type: source_inventory
series: YURUCAMP
status: canonical
source_boundary: Source metadata through V19 publication; literary analysis remains V15
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-17'
---

# Yuru Camp Current Source Inventory

## Current route and historical preservation

This is the current inventory for the [canonical current-state map](../CURRENT_STATE_AND_CORPUS_MAP.md). Its [machine manifest](YURUCAMP_CURRENT_SOURCE_MANIFEST.json) owns exact object identities, hashes, source classes and the V17/V18 spine maps; [quality and locator notes](YURUCAMP_CURRENT_SOURCE_QUALITY_AND_LOCATOR_NOTES.md) govern use. Current routing is canonical; it does not authorize narrative analysis beyond V15.

The nine Phase 0 files remain unchanged, including [the August 14 inventory](YURUCAMP_SOURCE_INVENTORY.md), [manifest](YURUCAMP_SOURCE_MANIFEST.json), [audit](YURUCAMP_PHASE0_CORPUS_AUDIT_AND_SOURCE_LOCK.md), gaps, quality/pagination notes, machine audit and checksums. Their V18-missing and old-V17 preference statements describe that historical observation. These new records reconcile later acquisitions without falsifying the original audit.

On 2026-10-17 the live root folder returned 32 direct children: 18 main manga objects, 10 supplementary objects, three ingestion records and one source archive. The archive returned the retained older V17 object. All current main manga V01–V18 bytes and the archived V17 were downloaded and independently hashed; the three prospective sources and archived V17 also received a fresh technical audit. V01–V15 technical quality properties carried from Phase 0 remain labeled historical, while selected literary-image checks are logged separately in the ledgers.

## Preferred main manga

| Volume | Preferred Drive ID | Format / current disposition | Literary boundary |
| --- | --- | --- | --- |
| V01 | 1RH-UyG9AQPv_qJXAU6S7TUfO45SJD08j | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V02 | 14S_RhAL3MVzfKC5E-ixS5WnGTcEgI_e4 | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V03 | 1MjTeALcesLykNlFX4x_a_tcAwbwFIYNV | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V04 | 12KI6uaPFmFveYK4nQcYZ4WJWyGsMIrpE | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V05 | 12SENoLFSwXVQ_bXu5kvPK7BcX5HHHUlY | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V06 | 1BY-q6dl8NCKcchfcWu1hA5sLXr-24Fp5 | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V07 | 1BklEAicC0YiiIHDgxU3eQVhL3RMIKnCZ | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V08 | 15btenYpQpad_B88EzR_Nk_zOSvsP9L4- | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V09 | 1oA_PCOi0QduPCkjy8w15KPgj1PDlimfG | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V10 | 1_BgrndXjlhQOHGnZtBs_XC5cYt2Ybouh | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V11 | 14lOx-vMWZhiBfTw1b01av2zDcmNj5H3s | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V12 | 16hiGhy-yTlWzHYI0ENGFhXOmphexmuui | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V13 | 1nKg7jQgphHLmVA_PyIAHqYL4UKqQiuYz | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V14 | 1u4mZ1SXozZfCFmMMQo3C1iYG9WtHgECJ | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V15 | 1KFvd5mfGEI9_MVfu-_KTwQJLZ00unJy2 | CBZ / LOCKED_CURRENT_PREFERRED | Accepted sequential reading |
| V16 | 1U_krzsI0k5fQkE4H8mAmNPBZD1ueWNKS | CBZ / LOCKED_WITH_QUALITY_FLAG | Available; NOT ANALYZED |
| V17 | 1sAvxxFVzSOtobfs2HTjPTK1QqNjxyu96 | EPUB / LOCKED_PRIMARY | Available; NOT ANALYZED |
| V18 | 1QEgPUH9Sr-3jVH2C5vr-3ZRJ7xKK4uH4 | EPUB / LOCKED_PRIMARY | Available; NOT ANALYZED |

## September acquisition reconciliation

The September 28 Calibre operation added nine works and upgraded one, confirmed by live readback of its summary (Drive ID `1rAQdA3UKEEwJUXhYbmOrDMqWl-ZKWbPs`), import manifest (`1coW2lCP-jgyEmOAO61LbpyPwf8RO0E_Q`) and propagation manifest (`147ep3c63qqHZvicX55FcFsrjlFIUaX7r`). Their reconciled identity records are in the [current repository manifest](YURUCAMP_CURRENT_SOURCE_MANIFEST.json); external acquisition records remain provenance, not migrated analytical authority. Drive creation timestamps are September 29 UTC; this is consistent with the named September 28 acquisition batch, not a second acquisition.

- V17: new Kobo EPUB is preferred; the older object retains its Drive ID in `Archive - Superseded Sources`. This is a source replacement, not byte-equivalent deduplication.
- V18: admitted as available main manga. It is no longer a current acquisition gap.
- Eight new supplementary works: two anthology comics, two Rurubu books and four anime/movie guidebooks. They remain separate from the narrative evidence lane.
- V16: unchanged pre-existing CBZ, now freshly identity/quality-checked; retain the existing quality flag.

## V19 publication and acquisition gap

[Houbunsha’s official catalog](https://houbunsha.co.jp/comics/detail.php?p=%25A4%25E6%25A4%25EB%25A5%25AD%25A5%25E3%25A5%25F3%25A2%25A4) lists Japanese V19 as released **2026-10-09**, ISBN **978-4-8322-9757-9** (checked 2026-10-17). No V19 primary object appears in the inspected source root or archive. Current state: **PUBLISHED_UNACQUIRED**. Its Drive ID and hash are null, not invented. V18 is the latest acquired main volume, not the latest published one. Marketing descriptions are not admitted as narrative evidence or used to interpret V01–V15.

Acquisition remediation: obtain the Japanese primary volume under separate source-acquisition authority, record object identity/hash/edition/quality, and admit its locator map before any later authorized reading. This gap does not block an individually authorized V16 reading.

## Supplementary lanes

| Source class | File | Drive ID |
| --- | --- | --- |
| anime_related_guidebook | Laid-Back Camp - TV Anime Official Guidebook - Outdoor Activity Record 1 [Japanese].epub | 1HFR-C5Rbm9Rf00BNhlXTcEKNy5ZBNuSy |
| anime_related_guidebook | Laid-Back Camp - TV Anime Official Guidebook - Outdoor Activity Record 3 [Japanese].epub | 1utfINLYgNBYHyYMo4NXApeoP8zusWL2y |
| anime_related_guidebook | Laid-Back Camp - TV Anime Official Guidebook - Outdoor Activity Record 2 [Japanese].epub | 1wvJ1KnuPxyNhgBJkly32pyjqRJuLx8er |
| anime_related_guidebook | Laid-Back Camp - Movie Official Guidebook - Campsite Reporting Record [Japanese].epub | 1EYFCAMk6Fik7Iz9AgFP7MGP9uPqve18Z |
| travel_guide | Laid-Back Camp - Rurubu Camp BOOK [Japanese].epub | 1xQiC46yg4CXUVfqvbMMOrnFeW96bgCFM |
| travel_guide | Laid-Back Camp - Rurubu Travel Guide - Season 3 [Japanese].epub | 1Xknc43DW5blhGuGTaiTfBtGVVOGx5RiJ |
| anthology_comic | Laid-Back Camp - Anthology Comic - Vol. 02 [Japanese].epub | 1PunN6yqtQh1iFC1gPKty1cHWNHxFXvsA |
| anthology_comic | Laid-Back Camp - Anthology Comic - Vol. 01 [Japanese].epub | 1n16ONBIyvIqfTyFOmF2vZdPFSQwESbm_ |
| travel_guide | Laid-Back Camp - Rurubu Travel Guide - Season 2 [Japanese].cbz | 1KSuz2XwVfwzdhiHDBNXDBWzqyKkNT5HB |
| travel_guide | Laid-Back Camp - Rurubu Travel Guide [Japanese].cbz | 1CTZqVFGA1mcn0CRlOhIYgyY3IugwDs_H |

Supplement identities/names/sizes were read back live. New supplement hashes are reported by the September propagation manifest; the two older Rurubu hashes are reported by Phase 0. They were **not independently recomputed in this repair**. No supplement was silently promoted to manga-canon behavior. Anthologies belong to a separately declared anthology continuity; travel guides may support separately labeled place/paratext work; anime/movie guidebooks may support adaptation/production work. The geography amendment still separates primary narrative, paratext and real-world layers.
