# Anime, Manga, Light-Novel, and Games Analysis

This public, owner-maintained repository is a structured analytical research corpus for anime, manga, light novels, games, and related media. It is designed to be navigable by both human readers and analytical agents.

The corpus combines sequential primary-source analysis with durable longitudinal structures—such as evidence and character-state ledgers, checkpoints, and claim-revision records—and higher-level character, relationship, thematic, institutional, performance, and full-series synthesis. It is not a primary-source media archive or a collection of interchangeable essays: each artifact has a defined analytical responsibility, and each project retains the architecture appropriate to its source and questions.

## Browse the corpus

- [Corpus index](governance/MANGA_ANIME_CORPUS_INDEX.md) — the main human-readable catalog of registered series and studies.
- [Series](series/) and the [series registry](series/registry.json) — title-specific analytical roots and their canonical entrypoints.
- [Studies](studies/) and the [study registry](studies/registry.json) — comparative, taxonomic, and other non-series analytical work.
- [Character analysis index](CHARACTER_ANALYSIS_INDEX.md) — reviewed routes to character-focused work across the corpus.

To enter a project, find it in the corpus index or registry, open its registered root, and read the named canonical entrypoint—often `CURRENT_STATE_AND_CORPUS_MAP.md`, `00_README_AND_CORPUS_MAP.md`, or an established project-specific equivalent.

> **Each active analytical project should have one canonical current entrypoint. Start there rather than selecting whichever document looks newest, longest, or most definitive.**

The entrypoint records the project's current scope, governing method and architecture, source boundary, completed work, and next valid routes. A registry entry that explicitly declares its entrypoint missing is a known routing limitation, not permission to infer a substitute.

## How the analytical corpus works

A mature project may contain several distinct kinds of artifact:

- an analytical or deep-reading method;
- a synthesis or corpus architecture;
- sequential volume, episode, chapter, event, route, or commu readings;
- longitudinal character, relationship, claim, thematic, institutional, voice/performance, or other ledgers;
- checkpoints and readiness assessments;
- character monographs and relationship studies;
- specialist and full-series syntheses; and
- reconstruction or prediction-oriented artifacts where the project supports them.

The usual analytical progression is:

```text
Primary source / governed evidence
            |
            v
Sequential deep readings
            |
            v
Longitudinal ledgers and checkpoints
            |
            v
Character, relationship, and specialist synthesis
            |
            v
Full-series integration or reconstruction
```

This is a responsibility model, not a mandatory folder template. Projects share a common archival language without being forced into analytically inappropriate identical structures. The project-local entrypoint and architecture determine which artifacts are required and how they relate.

## Source and evidence model

This repository is the **analytical corpus**, not the primary-source media archive. Git normally contains analysis, corpus state, indexes, routing metadata, public-safe provenance, and selected structured analytical derivatives.

Depending on the project and source policy, governed evidence outside Git may include manga or light-novel source files, full-resolution video and audio, game-extraction corpora, large image or frame collections, transcripts, alignments, and other deterministic derivatives unsuitable for the public repository. A processed artifact can still be evidence when it selects, transforms, joins, or routes source material without asserting what that material means.

The boundary is therefore evidence versus interpretation, not simply raw versus processed. Consult [Git authority and change routing](governance/CHATGPT_AUTHORITY_AND_ROUTING.md), [authority scope](governance/AUTHORITY_SCOPE.json), and [artifact eligibility](governance/policies/ARTIFACT_ELIGIBILITY.md) for the controlling details. Public-safe references to externally retained artifacts live under [`provenance/`](provenance/).

## Analytical execution

Work may run in local, cloud, or staged/parallel hybrid environments according to source scale, evidence modality, verified tool capabilities, reasoning requirements, and repository access. These environments are capability profiles, not analytical authority tiers. See the [execution-topology policy](governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) and [long-series hybrid protocol](governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) for the current model.

Canonical analytical state resides in repository artifacts and governed evidence/state—not in the conversational memory of any one ChatGPT, Work, or Codex session. Long-running work is checkpointed and handed off through durable project state.

## Repository layout

```text
series/<stable-slug>/   Title-specific analysis and project-local entrypoints
studies/<stable-slug>/  Comparative, taxonomic, and other non-series work
characters/             Curated character-discovery registry and specifications
governance/             Authority records, policies, schemas, and corpus navigation
tools/                  Deterministic validation and repository-maintenance tooling
crosswalk/              Sanitized historical source-to-Git migration records
provenance/             Public-safe references to artifacts retained outside Git
```

See [Repository structure](governance/REPOSITORY_STRUCTURE.md) for the authoritative topology. Substantive character analysis remains in the relevant series or study tree; `characters/` supplies discovery metadata rather than a parallel analytical corpus.

## For analytical agents and maintainers

Reader navigation begins with the corpus index and project entrypoints above. Repository-changing sessions should instead bootstrap from:

1. [`AGENTS.md`](AGENTS.md)
2. [`governance/AUTHORITY_STATE.yaml`](governance/AUTHORITY_STATE.yaml) and [`governance/AUTHORITY_SCOPE.json`](governance/AUTHORITY_SCOPE.json)
3. [Git authority and change routing](governance/CHATGPT_AUTHORITY_AND_ROUTING.md)
4. the applicable project registry and canonical entrypoint
5. the [change-integration checklist](governance/policies/CHANGE_INTEGRATION_CHECKLIST.md) before staging or committing

The live governance documents control when they differ from conversation memory, copied instructions, filename similarity, or historical migration records.

## Repository status

Git is the epoch-1 primary analytical authority for the exact scope declared in [authority scope](governance/AUTHORITY_SCOPE.json), subject to the narrower Drive-native and external-evidence roles recorded there. The live [authority state](governance/AUTHORITY_STATE.yaml) currently records the approved 14-day stabilization lifecycle; that record, rather than this summary, controls the current status.

The repository originated from a sealed Drive-to-Git migration covering 2,939 representations of 2,924 unique source artifacts across 37 series roots and two study roots. Those are historical cutover figures, not the current corpus size. Governed Git-native work and later imports have expanded the live corpus; use the [corpus index](governance/MANGA_ANIME_CORPUS_INDEX.md) and machine-readable [series](series/registry.json) and [study](studies/registry.json) registries for current coverage.

## Publication, contribution, and license

This is an owner-maintained public repository. Upstream write and contribution authority follows the [publication and contribution policy](governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md); independent forks are permitted. Public-safe analytical content is governed separately from excluded source media, private migration evidence, credentials, personal data, and other ineligible material.

Covered original content is licensed under CC BY-NC 4.0 only within the scope stated in [`LICENSE.md`](LICENSE.md). Third-party material and repository software/tooling exclusions are described in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and the license file.
