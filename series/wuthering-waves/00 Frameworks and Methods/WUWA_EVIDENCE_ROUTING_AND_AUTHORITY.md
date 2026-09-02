---
series: WUWA
artifact_type: evidence_routing_authority
scope: TITLE_WIDE
source_boundary: "Git analytical authority paired with owner-authenticated Google Drive evidence authority"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# WUWA evidence routing and authority

## Governing split

| Object class | Authority | Examples |
|---|---|---|
| Analytical interpretation | Git | monographs, deep readings, relationship/state analysis, specialist synthesis |
| Analytical method and routing | Git | protocols, corpus map, indexes, audits |
| Primary/deterministic derived evidence | Drive | raw mirror, normalized corpus, scene ledgers, identity crosswalks, voice mappings |
| Large performed/visual evidence | Drive/local source domain | FLAC shards, audiovisual clips, contact sheets, client packages |
| Build/extraction machinery | local or separately governed tooling home | caches, decoders, extraction scripts, working databases |

## Canonical Drive route

Evidence root: `https://drive.google.com/drive/folders/19ZmRcjKQR3g0lhU1A3sXujsyihhdKs-2`

Preferred evidence route:

`00 README` → `02 Normalized Semantic Corpus` → `03 Analysis Bridge Corpora` → exact identity/source locator → `04 Voice Evidence` or `05 Selected Audiovisual Evidence` → `01 Source Lock and Raw Semantic Mirror` for escalation.

## Source hierarchy

For current source generation 3.6.0:

1. official primary/client evidence for observed raw media/package facts;
2. pinned normalized semantic source at commit `353f2eaed119bc9f680eab92807d20ac75a79b40`;
3. official localization witnesses (`ja`, `ko`, `en`) alongside `zh-Hans` semantic anchor;
4. deterministic evidence bridges and crosswalks;
5. bounded third-party client-recorded audiovisual witnesses, explicitly lower-authority than official footage;
6. analytical inference in Git.

Official-client raw-media authority does not prove independently decoded semantic parity with the normalized corpus.

## Git evidence citation contract

An analytical claim should carry enough of the following to retrieve its basis:

- source generation/commit;
- text key or evidence ID;
- `wuwa://` exact source locator;
- semantic occurrence ID;
- character/story bridge artifact;
- language witness;
- render association and PCM/FLAC identity for voice claims;
- bounded AV witness and timestamp for visual claims.

Do not embed large source payloads merely to make a Git document self-contained.

## Escalation rule

Use the narrowest source capable of answering the question:

1. current Git synthesis;
2. claim/revision ledger;
3. Drive character/story bridge;
4. normalized semantic corpus;
5. pinned raw mirror;
6. client media or bounded audiovisual witness.

Exact wording, attribution, visual staging, and performance questions require deeper escalation than thematic orientation.

## Authority caveats

- `source_generation_frozen: true` does not make every interpretation canonical.
- Drive replication does not promote active-provisional analysis.
- A Git model package is subordinate to the monograph and claim ledger.
- A Drive machine table is measurement evidence, not interpretation.
- A later evidence package does not silently rewrite an earlier Git source boundary.

## Public-repository constraint

The Git repository is public. Do not add full scripts, large reproduced dialogue, raw audio, video, client assets, private review archives, secrets, or local paths. Use bounded excerpts only when analytically necessary and preserve evidence IDs/locators instead.
