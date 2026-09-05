# Tomozaki character analysis

## Responsibility

This directory is the canonical home for source-grounded individual character reconstruction once the sequential and longitudinal corpus is rich enough to justify dedicated character artifacts.

No character subdirectory or monograph is created at bootstrap. Global character discovery is maintained separately by the designated curation agent and must not be inferred from the existence of this directory.

## When to create `<Character>/`

Create a character subdirectory only when repeated evidence supports a model that can distinguish at least:

- stable tendency from developmental state;
- recipient-conditioned behavior from general behavior;
- competence/status effects from values and self-concept;
- explicit self-theory from independently corroborated behavior;
- relationship effects from role/group effects;
- ordinary-life evidence from crisis-only evidence;
- supporting evidence from material counterevidence and abstentions.

## Potential artifact responsibilities

Depending on evidence and retrieval need, a mature character directory may contain separate artifacts for:

- current state / reconstruction checkpoint;
- longitudinal character monograph;
- relationship and state ledger;
- ordinary-life and preferences profile;
- speech/register profile;
- claim and counterevidence ledger;
- reconstructive-model or comparative-framework output after the descriptive model is mature.

Do not create every artifact type mechanically. Each file must own a distinct analytical responsibility.

## Character discovery boundary

`characters/registry.jsonl` is the project-wide canonical character discovery registry, and `CHARACTER_ANALYSIS_INDEX.md` is its generated discovery view. Under the live repository policy, the designated character curation agent is the sole routine writer of both outputs.

This Tomozaki analytical branch therefore:

- does not independently edit either character output;
- does not create or maintain `.repository/character-registry-upserts.jsonl`;
- may merge new eligible character analysis before enrollment when existing character references remain valid;
- must stop for coordinated curation-agent repair before integration if a future Tomozaki change invalidates already referenced character evidence, anchors, authority, coverage, or generated output.

A router, plan, source lock, or name appearing in a volume reading does not by itself qualify a subject for discovery.
