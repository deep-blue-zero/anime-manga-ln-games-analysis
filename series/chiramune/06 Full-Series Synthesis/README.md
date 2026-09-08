---
series: CHIRAMUNE
artifact_type: series_synthesis_router
scope: ROLLING_AND_TERMINAL_SERIES_SYNTHESIS
source_boundary: "Japanese regular main analysis frozen through Volume 05; bundled V03 bonus labeled BONUS_FICTION; separate V03 booklet integrated as SUPPLEMENTAL_MAINLINE; V05 special edition unopened; current published-corpus synthesis updated through V05 main"
generation: V0.4
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chiramune series-synthesis router

This directory separates two responsibilities that must not be collapsed.

It is also the integration surface for a multi-document synthesis portfolio. Full-series work must remain distributed across the prospective readings and freezes, revision/thematic ledgers, warranted character monographs, promoted specialist syntheses, and the integration artifacts in this directory. No single synthesis file is expected to reproduce all supporting evidence.

## Document graph

```text
volume readings + prospective freezes
                |
                v
revision/thematic ledgers + character monographs
                |
                v
promoted specialist syntheses (only when earned)
                |
                v
current published-corpus synthesis
                |
                v
terminal full-series synthesis (only when eligible)
```

The integrator at each stage must preserve deterministic routes to the bounded documents beneath it. Material cross-document disagreement is resolved through the revision ledger; it is not hidden by silently harmonizing prose in the top-level synthesis.

## Current published-corpus synthesis

A rolling synthesis may be created when the analyzed corpus reaches a meaningful convergence boundary and the result has independent retrieval value beyond the deep readings, revision ledger, rolling thematic ledgers, and character monographs.

Preferred name:

`CHIRAMUNE_CURRENT_PUBLISHED_CORPUS_SYNTHESIS.md`

That artifact was promoted at V04 and is now updated through regular V05 main. Five ledgers, six character monographs, the promoted Fukui locality/departure specialist synthesis, and the prospective readings create independent cross-document retrieval value. It remains explicitly analyzed-to-date and mutable; it does not imply publication closure or terminal-series eligibility.

It must state at least:

- latest publication established by the current source audit;
- latest main and supplemental witnesses acquired;
- latest numbered main volume prospectively frozen;
- supplemental witnesses integrated and explicitly deferred;
- unresolved source, chronology, and interpretation gaps;
- which claims remain provisional or open.

It is a mutable, analyzed-to-date integration layer. It must not call itself final, complete-series, or exhaustive merely because every currently held source has been analyzed.

## Terminal full-series synthesis

A terminal synthesis is ineligible while Chiramune remains an ongoing publication or while source disposition, longitudinal reconciliation, specialist responsibilities, evidence routes, or architecture gaps remain unresolved.

Eligibility requires:

1. demonstrable publication closure for the governing series boundary;
2. every admitted source analyzed or explicitly disposed with rationale;
3. all numbered freezes intact;
4. ledgers and monographs reconciled through the terminal boundary;
5. an architecture/role-gap audit;
6. required specialist syntheses converged;
7. recoverable evidence routes for major mature claims;
8. validation and release audit under then-current repository governance.

Neither synthesis supersedes the historical prospective deep readings and freezes. Those remain the record of what each source boundary supported at the time.
