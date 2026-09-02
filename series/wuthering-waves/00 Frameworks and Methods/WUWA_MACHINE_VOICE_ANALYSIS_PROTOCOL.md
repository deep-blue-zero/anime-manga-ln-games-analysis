---
series: WUWA
artifact_type: machine_voice_analysis_protocol
scope: CHARACTER_VOICE_AND_PERFORMANCE
source_boundary: "Official installed-client voice evidence routed through canonical semantic occurrences and content-addressed lossless derivatives"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# WUWA machine voice analysis protocol

## Purpose

Machine audio analysis is a comprehensive complementary layer between textual speech analysis and selective human performance review. It should ingest every usable voice object in the declared character/source boundary, summarize measurable behavior, identify contrasts and outliers, and make human listening more efficient.

It is not an emotion detector and does not replace listening.

## Required identity chain

Every measurement must remain bound to:

- character/lore entity;
- canonical semantic occurrence ID;
- source-generation occurrence and exact source locator;
- language/localization witness;
- runtime render association;
- WEM/source-media hash where retained;
- canonical decoded PCM hash;
- FLAC object hash and Drive shard/member path;
- scene, state, relationship, and source-class labels when available.

Friendly filenames are never identity authority.

## Corpus accounting

The profile must report:

- semantic line count;
- voiced and unvoiced source occurrences;
- render-association count by language;
- runtime object count;
- unique PCM/FLAC count;
- duplicate/variant structure;
- missing or unresolved playback routes;
- excluded files and reasons;
- human annotation count.

Do not confuse render variants with unique semantic lines.

## Baseline measurements

Where technically reliable, calculate at least:

- total and voiced duration;
- leading, trailing, and internal silence;
- pause count, duration, and density;
- speaking-rate and articulation-rate proxies;
- F0 median, quantiles, robust range, and variability;
- intensity/energy distribution and dynamic range;
- pitch and energy contour features;
- spectral centroid/tilt and harmonic-noise or breathiness proxies with tool/version disclosure;
- text-normalized duration where language/tokenization permits;
- within-utterance variability;
- clipping, decode, and low-signal quality flags.

Any proxy whose reliability is weak for the source format, actor, language, or recording conditions must be omitted or explicitly qualified.

## Normalization

Cross-actor raw measurements are easy to misuse. Prefer:

- within-language actor baselines;
- robust z-scores or percentile positions within that actor's corpus;
- state-conditioned changes relative to the same actor;
- matched-semantic-line comparisons;
- text-length and source-class controls;
- separate treatment of archive, story, message, combat, and processed/filtered voice where appropriate.

A higher mean F0 across actors is not by itself a character interpretation.

## Partitioning

Analyze distributions by supported labels such as:

- developmental state/persona;
- public, private, crisis, reflective, comic, or operational context;
- relationship or interlocutor;
- main story, archive/favor, message, combat/system source class;
- direct speech versus recording/mediated communication;
- multilingual witness.

Labels must come from source/context review or a declared provisional classifier. Do not infer intimate/private state solely from acoustic softness.

## Clustering and dimensional exploration

Unsupervised or semi-supervised analysis may identify recurring acoustic regimes. Report:

- features used and scaling;
- algorithm and parameters;
- stability/sensitivity checks;
- cluster size and representative lines;
- context distribution;
- counterexamples and mixed clusters.

Describe clusters first in measurements, not emotions. For example: "slower, lower-energy, longer-pause regime," not "sad voice."

## Outliers and cohort selection

Use the comprehensive pass to nominate:

- cluster medoids or representative lines;
- statistically unusual lines;
- major state transitions;
- high-value relationship scenes;
- lines supporting major claims;
- counterexamples that weaken proposed tendencies;
- matched four-language moments;
- quality-control samples.

The human cohort should be claim-driven and bounded. Exhaustive manual annotation is not the default.

## Machine hypothesis vocabulary

Allowed:

- measurable difference;
- recurring acoustic regime;
- possible performance correlate;
- hypothesis requiring listening;
- no stable difference detected;
- insufficient/contaminated evidence.

Disallowed without human review:

- sad, happy, angry, intimate, flirtatious, tender, ashamed, deceptive, sincere;
- actor intention;
- relationship status;
- personality trait inferred only from signal features;
- strongest/best/most authentic dub.

## Human-review integration

The canonical speech/voice/performance profile should preserve:

1. machine observation;
2. initial machine-assisted hypothesis;
3. human listening note;
4. counterexample;
5. confidence and language/state scope;
6. revision transition.

Human review may `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or leave `OPEN` a hypothesis. It does not erase reproducible measurements.

## Git/Drive boundary

Drive retains line-level machine tables, audio objects, manifests, and large worksheets. Git retains:

- method and corpus accounting;
- aggregate distributions and analytically material tables;
- cluster/contrast summaries;
- selected evidence IDs and locators;
- human-reviewed interpretations;
- limitations and revision history.

## Completion gate

A character is `machine_voice_profiled` only when:

- the usable corpus boundary is explicit;
- identity and hashes route every retained measurement;
- failures and missing routes are enumerated;
- aggregate outputs reproduce from declared inputs/tools;
- no acoustic proxy has been silently converted into emotion or character judgment.
