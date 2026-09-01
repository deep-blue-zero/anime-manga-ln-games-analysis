---
series: IDOLY_PRIDE
artifact_type: freshness_registry
artifact_role: LEDGER
scope: CHARACTER_AND_UNIT_FRESHNESS
generation: V2
version: '1.31'
status: canonical
phase: '2'
source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: Phase-2 freshness registry for IP-V2-SNAPSHOT-2026-08-13-A. P2-A/P2-B individual character validation, the frozen-minimum P2-C relationship set, and all five named P2-D unit validations remain complete. The optional Hoshimi Productions standalone P2-D ledger remains not warranted. P2-E-01 answerable interdependence, P2-E-02 autonomy/management/intervention/professional care, P2-E-03 grief/death/memory/inheritance/non-replacement, and P2-E-04 authenticity/persona/publicity/media/selective disclosure are complete/current as thematic ledgers. Theme-level completion does not advance any character, unit, or standalone institution freshness frontier; Hoshimi therefore remains validated_through null / provisional as a standalone entity while institution-level recurring mechanisms route through P2-E. P2-E-05 audience reciprocity/fandom/performance/creative governance is next.
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
integrity_status: P2_D_CLOSED_P2_E_04_COMPLETE
created: '2026-08-16'
updated: '2026-08-26'
next_operation: P2-E-05 — IDOLY_PRIDE_V2_THEME_AUDIENCE_RECIPROCITY_FANDOM_PERFORMANCE_AND_CREATIVE_GOVERNANCE_LONGITUDINAL_LEDGER.md
---

# IDOLY PRIDE V2 — CHARACTER / UNIT UPDATE STATUS

## 0. Freshness rule

This registry distinguishes **source availability** from **longitudinal analytical validation**.

All entities below participated in the Phase-1 snapshot survey/routing state, but P2-0 deliberately initializes:

> `validated_through: null`

for every entry.

A character or unit receives `validated_through: IP-V2-SNAPSHOT-2026-08-13-A` only after its relevant Phase-2 longitudinal ledger has actually retested the entity across the admitted source frontier.

This prevents a recently created administrative file from falsely implying that every character has already received a Phase-2 longitudinal reread.

---

## 1. Registry

```yaml
registry:
  - character_or_unit: "Mana Nagase"
    entity_type: character
    registry_id: IP-FRESH-CHAR-MANA
    stable_source_code: "mna"
    primary_group: "foundational"
    last_corpus_review: "2026-08-17 P2-A1 Mana longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-A1 Mana longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
  - character_or_unit: "Makino Kouhei"
    entity_type: character
    registry_id: IP-FRESH-CHAR-MAKINO
    stable_source_code: "makino"
    primary_group: "foundational/manager"
    last_corpus_review: "2026-08-18 P2-A2 Makino longitudinal validation + P2-A3 branch-canon companion"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-A2 Makino longitudinal ledger complete; P2-A3 branch-canon companion complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    branch_canon_status: complete
    branch_canon_ledger: IDOLY_PRIDE_V2_MAKINO_PLAYER_BRANCH_CANON_LEDGER.md
  - character_or_unit: "Sakura Kawasaki"
    entity_type: character
    registry_id: IP-FRESH-CHAR-SKR
    stable_source_code: "skr"
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-18 P2-B1 Sakura longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B1 Sakura longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_SAKURA_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Rei Ichinose"
    entity_type: character
    registry_id: IP-FRESH-CHAR-REI
    stable_source_code: "rei"
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-18 P2-B1 Rei longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B1 Rei longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_REI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Haruko Saeki"
    entity_type: character
    registry_id: IP-FRESH-CHAR-HRK
    stable_source_code: "hrk"
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-18 P2-B1 Haruko longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B1 Haruko longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_HARUKO_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Chisa Shiraishi"
    entity_type: character
    registry_id: IP-FRESH-CHAR-CHS
    stable_source_code: "chs"
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-18 P2-B1 Chisa longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B1 Chisa longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_CHISA_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Shizuku Hyodo"
    entity_type: character
    registry_id: IP-FRESH-CHAR-SZK
    stable_source_code: "szk"
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-18 P2-B1 Shizuku longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B1 Shizuku longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_SHIZUKU_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Kotono Nagase"
    entity_type: character
    registry_id: IP-FRESH-CHAR-KTN
    stable_source_code: "ktn"
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-18 P2-B2 Kotono longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B2 Kotono longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_KOTONO_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Nagisa Ibuki"
    entity_type: character
    registry_id: IP-FRESH-CHAR-NGS
    stable_source_code: "ngs"
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-18 P2-B2 Nagisa longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B2 Nagisa longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_NAGISA_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Saki Shiraishi"
    entity_type: character
    registry_id: IP-FRESH-CHAR-SKI
    stable_source_code: "ski"
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-18 P2-B2 Saki longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B2 Saki longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_SAKI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Suzu Narumiya"
    entity_type: character
    registry_id: IP-FRESH-CHAR-SUZ
    stable_source_code: "suz"
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-19 P2-B2 Suzu longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B2 Suzu longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_SUZU_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Mei Hayasaka"
    entity_type: character
    registry_id: IP-FRESH-CHAR-MEI
    stable_source_code: "mei"
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-19 P2-B2 Mei longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B2 Mei longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_MEI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Rio Kanzaki"
    entity_type: character
    registry_id: IP-FRESH-CHAR-RIO
    stable_source_code: "rio"
    primary_group: "LizNoir"
    last_corpus_review: "2026-08-19 P2-B3 Rio longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B3 Rio longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_RIO_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Aoi Igawa"
    entity_type: character
    registry_id: IP-FRESH-CHAR-AOI
    stable_source_code: "aoi"
    primary_group: "LizNoir"
    last_corpus_review: "2026-08-19 P2-B3 Aoi longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B3 Aoi longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_AOI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Ai Komiyama"
    entity_type: character
    registry_id: IP-FRESH-CHAR-AI
    stable_source_code: "ai"
    primary_group: "LizNoir"
    last_corpus_review: "2026-08-19 P2-B3 Ai longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B3 Ai longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_AI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Kokoro Akazaki"
    entity_type: character
    registry_id: IP-FRESH-CHAR-KKR
    stable_source_code: "kkr"
    primary_group: "LizNoir"
    last_corpus_review: "2026-08-19 P2-B3 Kokoro longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B3 Kokoro longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_KOKORO_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Rui Tendo"
    entity_type: character
    registry_id: IP-FRESH-CHAR-RUI
    stable_source_code: "rui"
    primary_group: "TRINITYAiLE"
    last_corpus_review: "2026-08-19 P2-B4 Rui longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B4 Rui longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_RUI_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Yu Suzumura"
    entity_type: character
    registry_id: IP-FRESH-CHAR-YU
    stable_source_code: "yu"
    primary_group: "TRINITYAiLE"
    last_corpus_review: "2026-08-20 P2-B4 Yu longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B4 Yu longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_YU_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Sumire Okuyama"
    entity_type: character
    registry_id: IP-FRESH-CHAR-SMR
    stable_source_code: "smr"
    primary_group: "TRINITYAiLE"
    last_corpus_review: "2026-08-20 P2-B4 Sumire longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B4 Sumire longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_SUMIRE_LONGITUDINAL_LEDGER.md
  - character_or_unit: "miho"
    entity_type: character
    registry_id: IP-FRESH-CHAR-MHK
    stable_source_code: "mhk"
    primary_group: "IIIX"
    last_corpus_review: "2026-08-20 P2-B5 miho longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B5 miho longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_MIHO_LONGITUDINAL_LEDGER.md
  - character_or_unit: "fran"
    entity_type: character
    registry_id: IP-FRESH-CHAR-KOR
    stable_source_code: "kor"
    primary_group: "IIIX"
    last_corpus_review: "2026-08-23 P2-B5 fran longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B5 fran longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_FRAN_LONGITUDINAL_LEDGER.md
  - character_or_unit: "kana"
    entity_type: character
    registry_id: IP-FRESH-CHAR-KAN
    stable_source_code: "kan"
    primary_group: "IIIX"
    last_corpus_review: "2026-08-24 P2-B5 kana longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-B5 kana longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_CHAR_KANA_LONGITUDINAL_LEDGER.md
  - character_or_unit: "SUNNY PEACE"
    entity_type: "unit"
    registry_id: IP-FRESH-UNIT-SUNNY_PEACE
    stable_source_code: null
    primary_group: "SUNNY PEACE"
    last_corpus_review: "2026-08-24 P2-D SUNNY PEACE unit longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D SUNNY PEACE unit longitudinal ledger complete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_UNIT_SUNNY_PEACE_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Tsuki no Tempest"
    entity_type: "unit"
    registry_id: IP-FRESH-UNIT-TSUKI_NO_TEMPEST
    stable_source_code: null
    primary_group: "Tsuki no Tempest"
    last_corpus_review: "2026-08-25 P2-D Tsuki no Tempest unit longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D Tsuki no Tempest unit longitudinal ledger complete; corrected member-code frontier ktn/ngs/ski/suz/mei"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_UNIT_TSUKI_NO_TEMPEST_LONGITUDINAL_LEDGER.md
  - character_or_unit: "LizNoir"
    entity_type: "unit"
    registry_id: IP-FRESH-UNIT-LIZNOIR
    stable_source_code: null
    primary_group: "LizNoir"
    last_corpus_review: "2026-08-25 P2-D LizNoir unit longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D LizNoir unit longitudinal ledger complete; verified member frontier rio/aoi/ai/kkr = 189 union / 24 exact all-four"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_UNIT_LIZNOIR_LONGITUDINAL_LEDGER.md
  - character_or_unit: "TRINITYAiLE"
    entity_type: "unit"
    registry_id: IP-FRESH-UNIT-TRINITYAILE
    stable_source_code: null
    primary_group: "TRINITYAiLE"
    last_corpus_review: "2026-08-25 P2-D TRINITYAiLE longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D TRINITYAiLE unit ledger complete; verified rui/yu/smr union 170 bundles / exact all-three 47; generated trinityaile.md quarantined as contaminated/incomplete"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_UNIT_TRINITYAILE_LONGITUDINAL_LEDGER.md
  - character_or_unit: "IIIX"
    entity_type: "unit"
    registry_id: IP-FRESH-UNIT-IIIX
    stable_source_code: null
    primary_group: "IIIX"
    last_corpus_review: "2026-08-26 P2-D IIIX longitudinal validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D IIIX unit ledger complete; canonical mhk/kor/kan union 127 unique member-bearing bundles; exact all-three frontier corrected to 28"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: IP-V2-SNAPSHOT-2026-08-13-A
    update_status: current
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: complete
    p2_ledger: IDOLY_PRIDE_V2_UNIT_IIIX_LONGITUDINAL_LEDGER.md
  - character_or_unit: "Hoshimi Productions"
    entity_type: "institution/ensemble"
    registry_id: IP-FRESH-UNIT-HOSHIMI_PRODUCTIONS
    stable_source_code: null
    primary_group: "Hoshimi Productions"
    last_corpus_review: "2026-08-26 P2-E-04 thematic institutional routing validation"
    latest_source_included: "IP-V2-SNAPSHOT-2026-08-13-A; P2-D standalone ledger not warranted; P2-E-01 through P2-E-04 now provide canonical recurring institution/theme owners without advancing standalone institution freshness"
    source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
    validated_through: null
    update_status: provisional
    new_material_pending: false
    requires_synthesis_revision: false
    p2_ledger_status: not_warranted_as_separate_p2d_ledger
    p2_routing_status: p2_e_theme_institution_family
    first_p2_e_owner: IDOLY_PRIDE_V2_THEME_ANSWERABLE_INTERDEPENDENCE_LONGITUDINAL_LEDGER.md
    second_p2_e_owner: IDOLY_PRIDE_V2_THEME_AUTONOMY_MANAGEMENT_INTERVENTION_AND_PROFESSIONAL_CARE_LONGITUDINAL_LEDGER.md
    third_p2_e_owner: IDOLY_PRIDE_V2_THEME_GRIEF_DEATH_MEMORY_INHERITANCE_AND_NON_REPLACEMENT_LONGITUDINAL_LEDGER.md
    fourth_p2_e_owner: IDOLY_PRIDE_V2_THEME_AUTHENTICITY_PERSONA_PUBLICITY_MEDIA_AND_SELECTIVE_DISCLOSURE_LONGITUDINAL_LEDGER.md
```

---

## 2. Status semantics

Recommended `update_status` values follow the governing evidence protocol:

- `current`
- `new-material-pending`
- `reanalysis-required`
- `provisional`
- `archived-at-release`

At initialization all entries are `provisional` **only in the Phase-2 freshness sense**. This does not downgrade the authority of the frozen Phase-1 findings.

`requires_synthesis_revision: false` means no new live-service delta currently forces revision; it does not mean the future Phase-3 V2 synthesis is already complete.

---

## 3. Advancement transaction

When a Phase-2 ledger passes:

1. set `p2_ledger_status: complete` for the affected entity;
2. set `validated_through` to the snapshot actually tested;
3. update `last_corpus_review` and `latest_source_included`;
4. set `update_status: current` if no newer material is pending;
5. route any unresolved Class-2/3 delta to `PENDING_REANALYSIS_QUEUE.md` rather than falsely marking the entity current.

All queued P2-A/P2-B individual character advancements, the frozen-minimum P2-C relationship set, and all five named P2-D unit validations are complete through `IP-V2-SNAPSHOT-2026-08-13-A`. P2-D is closed. The optional Hoshimi Productions entity remains `provisional` only because no standalone institution-wide longitudinal freshness pass exists; its separate P2-D ledger is explicitly **not warranted**, not pending. Institution-level recurrent mechanisms now route through P2-E. P2-E-01 through P2-E-04 completion do not by themselves advance entity freshness. P2-E-05 audience reciprocity/fandom/performance/creative governance is next.
