#!/usr/bin/env python3
"""Validate the Sigrika analytical packet without network access.

Usage:
  python reproduce_validation.py
  python reproduce_validation.py --sources /path/to/downloaded/Drive/files
  python reproduce_validation.py --sources /path/to/inputs --output report.json

The original source files are not distributed with this analysis packet. Their
filenames and SHA-256 values are declared in SOURCE_INPUT_MANIFEST.json.
A successful mechanical check is not proof of interpretive correctness.
Only Python's standard library is required. Source files are read, never edited.
"""
from __future__ import annotations
import argparse
import collections
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import statistics
import sys
from urllib.parse import unquote




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_ACQUISITION_MANIFEST.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_ACQUISITION_MANIFEST.json', 'AUDIO_CLUSTER_RESULTS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_CLUSTER_RESULTS.json', 'AUDIO_CONTEXT_COHORTS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_CONTEXT_COHORTS.json', 'AUDIO_FIDELITY_PROBES.json': '04 Validation and Readiness/AUDIO_FIDELITY_PROBES.json', 'AUDIO_FINDING_INDEX.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_FINDING_INDEX.json', 'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_MATCHED_SEMANTIC_CASES.json', 'AUDIO_METHOD_PARAMETERS.json': '03 Audiovisual and Voice/Tooling and Reproduction/AUDIO_METHOD_PARAMETERS.json', 'AUDIO_OUTLIER_REVIEW_COHORT.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_OUTLIER_REVIEW_COHORT.json', 'AUDIO_PRIOR_CLAIM_SNAPSHOT.json': '04 Validation and Readiness/AUDIO_PRIOR_CLAIM_SNAPSHOT.json', 'AUDIO_REPRODUCTION_CHECK.json': '04 Validation and Readiness/AUDIO_REPRODUCTION_CHECK.json', 'AUDIO_REPRODUCTION_INSTRUCTIONS.txt': '03 Audiovisual and Voice/Tooling and Reproduction/AUDIO_REPRODUCTION_INSTRUCTIONS.txt', 'AUDIO_RETRIEVAL_QC_COHORT.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_RETRIEVAL_QC_COHORT.json', 'AUDIO_SOURCE_INPUT_MANIFEST.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_SOURCE_INPUT_MANIFEST.json', 'AUDIO_STAGE_VALIDATION_REPORT.json': '04 Validation and Readiness/AUDIO_STAGE_VALIDATION_REPORT.json', 'AUDIO_TO_VIDEO_TARGET_JOIN.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_TO_VIDEO_TARGET_JOIN.json', 'AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json', 'AV_RETRIEVAL_TARGETS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AV_RETRIEVAL_TARGETS.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'CLAIM_INDEX.json': '01 Evidence and Source-Facing/CLAIM_INDEX.json', 'DELIVERY_INVENTORY.json': '04 Validation and Readiness/DELIVERY_INVENTORY.json', 'EVIDENCE_BUNDLE_INDEX.json': '01 Evidence and Source-Facing/EVIDENCE_BUNDLE_INDEX.json', 'FIDELITY_PROBE_INDEX.json': '04 Validation and Readiness/FIDELITY_PROBE_INDEX.json', 'LOCAL_REVISION_REVIEW.json': '04 Validation and Readiness/LOCAL_REVISION_REVIEW.json', 'SHA256SUMS.txt': '04 Validation and Readiness/SHA256SUMS.txt', 'SHARD_ACQUISITION_AUDIT.json': '04 Validation and Readiness/SHARD_ACQUISITION_AUDIT.json', 'SOURCE_AND_AUDIO_AUDIT.json': '04 Validation and Readiness/SOURCE_AND_AUDIO_AUDIT.json', 'SOURCE_INPUT_MANIFEST.json': '04 Validation and Readiness/SOURCE_INPUT_MANIFEST.json', 'TOOLKIT_CAPABILITY_CHECK.json': '04 Validation and Readiness/TOOLKIT_CAPABILITY_CHECK.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_SIGRIKA_ANALYSIS_PACKET_README.md': 'WUWA_SIGRIKA_ANALYSIS_PACKET_README.md', 'WUWA_SIGRIKA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md', 'WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md', 'WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md', 'WUWA_SIGRIKA_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_SIGRIKA_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json', 'WUWA_SIGRIKA_CURRENT_STATE.md': 'WUWA_SIGRIKA_CURRENT_STATE.md', 'WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_SIGRIKA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_SIGRIKA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_SIGRIKA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md', 'WUWA_SIGRIKA_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_SIGRIKA_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_SIGRIKA_RELATIONSHIP_AND_STATE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_RELATIONSHIP_AND_STATE_PROFILE.md', 'WUWA_SIGRIKA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_SIGRIKA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_SIGRIKA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_SIGRIKA_TALENT_EXPECTATION_AND_INTERPRETIVE_AGENCY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_TALENT_EXPECTATION_AND_INTERPRETIVE_AGENCY_PROFILE.md', 'analyze_audio.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/analyze_audio.py', 'check_audio_reproduction.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/check_audio_reproduction.py', 'requirements-audio.txt': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/requirements-audio.txt', 'summarize_audio.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/summarize_audio.py', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py', 'validate_audio_stage.py': '04 Validation and Readiness/validate_audio_stage.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def load(path: Path):
    text = path.read_text(encoding='utf-8', errors='strict')
    if path.suffix == '.jsonl':
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    return json.loads(text)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--packet', type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--sources', type=Path, help='Directory of the exact original input filenames')
    ap.add_argument('--output', type=Path, help='Optional JSON report output; no source writes')
    args = ap.parse_args()
    root = args.packet.resolve()
    errors: list[str] = []
    counts: dict[str, object] = {}
    def check(condition: bool, description: str) -> None:
        if not condition:
            errors.append(description)
    # The repository adds a concise authority/routing file around the immutable
    # fourteen-document analytical packet. Validate the packet itself here.
    md = sorted(
        p for p in root.rglob('WUWA_SIGRIKA_*.md')
        if p.name != 'WUWA_SIGRIKA_CURRENT_STATE.md'
    )
    texts = {p.name: p.read_text('utf-8', errors='strict') for p in md}
    document_paths = {p.name: p for p in md}
    counts['markdown_documents'] = len(md)
    counts['markdown_whitespace_words'] = sum(len(t.split()) for t in texts.values())
    check(len(md) == 14, 'Expected fourteen Markdown documents')
    anchors: dict[str, set[str]] = {}
    for name, text in texts.items():
        check('\ufffd' not in text, f'Replacement character: {name}')
        check(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text), f'Control character: {name}')
        check(text.startswith('---\n') and '\n---\n' in text[4:], f'Missing front matter: {name}')
        front = text.split('---', 2)[1]
        for field, value in {
            'series': 'WUWA', 'character': 'Sigrika', 'status': 'active_provisional',
            'source_commit': '353f2eaed119bc9f680eab92807d20ac75a79b40',
            'analysis_generation': 'SIGRIKA_PRE_AV_V0_2',
            'analysis_authority_state': 'owner_adopted_current_provisional',
            'do_not_use_as_current_authority': 'false',
            'do_not_use_as_current_git_authority': 'false',
        }.items():
            check(re.search(rf'(?m)^{field}: {re.escape(value)}$', front) is not None,
                  f'Front-matter mismatch {field}: {name}')
        check(text.count('```') % 2 == 0, f'Unbalanced code fence: {name}')
        check('{DOC:' not in text, f'Unexpanded document reference: {name}')
        aa=set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
        aa |= {re.sub(r'[^\w\- ]', '', h.strip().lower()).replace(' ', '-')
               for h in re.findall(r'(?m)^#{1,6}\s+(.+)$', text)}
        anchors[name] = aa
    link_count = 0
    for name, text in texts.items():
        for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
                continue
            target, _, frag = unquote(url).partition('#')
            target = target or name
            link_count += 1
            resolved = (document_paths[name].parent / target).resolve()
            check(resolved.is_file(), f'Broken local link in {name}: {url}')
            if frag and resolved.name in anchors:
                check(frag in anchors[resolved.name], f'Broken fragment in {name}: {url}')
    counts['local_links_checked'] = link_count
    for p in root.rglob('*.json'):
        load(p)
    eb=load(packet_artifact(root, 'EVIDENCE_BUNDLE_INDEX.json'))
    claims=load(packet_artifact(root, 'CLAIM_INDEX.json'))
    model=load(packet_artifact(root, 'WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json'))
    probes=load(packet_artifact(root, 'FIDELITY_PROBE_INDEX.json'))
    targets=load(packet_artifact(root, 'AV_RETRIEVAL_TARGETS.json'))
    qc=load(packet_artifact(root, 'AUDIO_RETRIEVAL_QC_COHORT.json'))
    eids={e['id'] for e in eb};cids={c['id'] for c in claims};rids={r['id'] for r in model['rules']}
    check(len(eb)==60 and len(eids)==60, 'Evidence-bundle count/uniqueness')
    check(len(claims)==50 and len(cids)==50, 'Claim count/uniqueness')
    check(len(probes)==40 and len({p['id'] for p in probes})==40, 'Probe count/uniqueness')
    check(len(targets)==24 and len({t['id'] for t in targets})==24, 'AV-target count/uniqueness')
    check(len(model['rules'])==16, 'Model-rule count')
    check({x for p in probes for x in p['model_rule_ids']}==rids, 'Not all model rules covered by probes')
    for c in claims:
        check(set(c['evidence'])<=eids, f'Unknown claim evidence {c["id"]}')
    for r in model['rules']:
        check(set(r['evidence_ids'])<=eids, f'Unknown evidence in {r["id"]}')
    for p in probes:
        check(set(p['evidence_ids'])<=eids and set(p['model_rule_ids'])<=rids, f'Invalid probe refs {p["id"]}')
        check(p['empirical_accuracy'] is None, f'Unjustified empirical score {p["id"]}')
    for t in targets:
        check(t['evidence_bundle'] in eids and set(t['claim_ids'])<=cids, f'Invalid AV refs {t["id"]}')
        check(t['acquisition_status']=='deferred_owner_local_1080p_or_larger' and t['viewing_status']=='not_viewed', f'AV status {t["id"]}')
    check(not any(root.rglob('AV_EVIDENCE_MANIFEST.jsonl')), 'Unacquired plan must not have an empty witness manifest')
    counts.update(evidence_bundles=len(eb),claims=len(claims),model_rules=len(rids),nonblind_probes=len(probes),av_retrieval_targets=len(targets))
    # Confirm every cross-reference printed in Markdown names a real local identity.
    all_ids=eids|cids|rids|{p['id'] for p in probes}|{t['id'] for t in targets}|{q['id'] for q in qc}
    for name,text in texts.items():
        for rid in re.findall(r'\bSIG-(?:E|C|R|P)\d{2}\b|\bSIG-AV-\d{2}\b|\bSIG-AUDIO-QC-\d{2}\b',text):
            check(rid in all_ids, f'Unknown printed ID {rid} in {name}')
    source_status='not_run_without_original_inputs'
    if args.sources:
        src=args.sources.resolve()
        manifest=load(packet_artifact(root, 'SOURCE_INPUT_MANIFEST.json'))
        # A top-level list is the retained input-manifest contract.
        hashchecks=0
        for row in manifest:
            p=src/row['file']
            check(p.is_file(), f'Missing input {p.name}')
            if p.is_file():
                check(p.stat().st_size==row['bytes'] and digest(p)==row['sha256'],f'Input hash/size mismatch {p.name}')
                hashchecks+=1
        counts['input_hashes_checked']=hashchecks
        S=load(src/'SCENE_AND_EVIDENCE_LEDGER.jsonl')
        raw={int(r['source_locator'].split('#/')[1]):r['raw'] for r in load(src/'RAW_RELEVANT_FLOW_STATES.jsonl')}
        OC=load(src/'occurrence_identity_crosswalk.jsonl')
        V=load(src/'COMPLETE_VOICE_LINE_ANALYSIS.jsonl')
        R=load(src/'COMPLETE_VOICE_RENDER_ANALYSIS.jsonl')
        X=load(src/'DRIVE_AUDIO_OBJECT_CROSSWALK.jsonl')
        scene={(s['flow_state_row_index'],s['action_index']):s for s in S}
        talks={t['source_locator']:t for s in S for t in s['talk_items']}
        renderedkeys=0; hashtexts=0
        for s in S:
            items=json.loads(raw[s['flow_state_row_index']]['Actions'])[s['action_index']].get('Params',{}).get('TalkItems',[])
            for t in s['talk_items']:
                rt=items[t['talk_index']]
                if t.get('text_key'):
                    check(rt.get('TidTalk')==t['text_key'],f'Raw exact TidTalk mismatch {t["source_locator"]}')
                    renderedkeys+=1
                check(rt.get('WhoId')==t.get('technical_speaker_id'),f'Raw speaker mismatch {t["source_locator"]}')
                for lang,w in t.get('text_witnesses',{}).items():
                    content=w.get('content');expected=w.get('content_sha256')
                    if content is not None and expected:
                        check(hashlib.sha256(content.encode('utf-8')).hexdigest()==expected,
                              f'Content hash mismatch {t["source_locator"]}/{lang}')
                        hashtexts+=1
        for o in OC:
            check(o['source_locator'] in talks,f'Unresolved occurrence route {o["source_locator"]}')
        for e in eb:
            for a in e['anchors']:
                check(tuple(a[:2]) in scene,f'Missing evidence action {e["id"]}/{a}')
        # Assemble the same source-facing text-key universe used by the author.
        textkeys={r['text_key'] for r in load(src/'CONTEXT_TEXT_WITNESSES.jsonl')}
        textkeys|={r['text_key'] for r in load(src/'source_mentions.jsonl')}
        def gather(o):
            if isinstance(o,dict):
                if 'text_key' in o and 'values' in o:textkeys.add(o['text_key'])
                for v in o.values():gather(v)
            elif isinstance(o,list):
                for v in o:gather(v)
        gather(load(src/'character_source_package.json'))
        for e in eb:
            check(set(e['text_keys'])<=textkeys,f'Missing evidence text key {e["id"]}')
        printed_pairs=set()
        printed_keys=set()
        for name,body in texts.items():
            for row,act in re.findall(r'(?<!\d)(\d{4,5})/(\d{1,2})(?!\d)',body):
                pair=(int(row),int(act));printed_pairs.add(pair)
                check(pair in scene,f'Printed action not in scene ledger {pair}: {name}')
            for key in re.findall(r'`((?:Main_|MAIN_|FavorWord_|FavorStory_|FavorRoleInfo_|FavorGoods_|Side_|XGLK_|Zuoyequnxing_|InfoDisplay_|ItemInfo_|QuestTree_)[A-Za-z0-9_]+)`',body):
                printed_keys.add(key)
                check(key in textkeys,f'Printed text key unresolved {key}: {name}')
        counts['distinct_printed_action_pairs_checked']=len(printed_pairs)
        counts['distinct_printed_text_keys_checked']=len(printed_keys)
        for t in targets:
            ti=talks.get(t['source_locator'])
            check(ti is not None and ti['text_key']==t['text_key'] and ti['technical_speaker_id']==t['technical_speaker_id'],f'AV exact anchor mismatch {t["id"]}')
        # Preserve exact occurrence overrides, not a global reclassification of 150088.
        byocc={o['source_locator']:o for o in OC}
        prefix='wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/flowState/flowstate.json#/'
        for i in [0,1,3]:
            check(byocc[prefix+f'12955/Actions!/4/Params/TalkItems/{i}']['character_attribution']=='rejected',f'Impersonation incorrectly admitted {i}')
        XM={x['canonical_pcm_sha256']:x for x in X}
        vid={v['semantic_voice_occurrence_id'] for v in V}
        rids_source={r['render_analysis_id'] for r in R}
        nestedrids={r['render_analysis_id'] for v in V for r in v['renders']}
        check(nestedrids==rids_source,'Semantic embedded renders do not match complete render table')
        for r in R:
            x=XM.get(r['canonical_pcm_sha256'])
            check(x is not None and x['flac_sha256']==r['flac_sha256'],f'PCM/FLAC route mismatch {r["render_analysis_id"]}')
            check(r['semantic_voice_occurrence_id'] in vid,f'Unresolved semantic voice {r["render_analysis_id"]}')
        for q in qc:
            x=XM.get(q['canonical_pcm_sha256'])
            check(x is not None and x['drive_relative_path']==q['drive_relative_path'] and x['archive_member_path']==q['archive_member_path'],f'QC shard/member mismatch {q["id"]}')
        audit=load(packet_artifact(root, 'SOURCE_AND_AUDIO_AUDIT.json'))
        def summary(rows):
            result={'n':len(rows),'duration_sum_seconds':sum(r['machine_acoustic_observations']['duration_seconds'] for r in rows),
                    'channels':dict(collections.Counter(str(r['machine_acoustic_observations']['channels']) for r in rows))}
            for key in ['duration_seconds','rms_dbfs','peak_dbfs','silence_fraction_below_minus_50_dbfs_20ms']:
                vals=[r['machine_acoustic_observations'][key] for r in rows]
                result[key]={'median':statistics.median(vals),'min':min(vals),'max':max(vals)}
            return result
        for lang,g in audit['audio_summaries'].items():
            rr=[r for r in R if r['voice_language']==lang]
            unique=list({r['canonical_pcm_sha256']:r for r in rr}.values())
            check(summary(unique)==g['unique'],f'Unique acoustic summary mismatch {lang}')
            for cls,expected in g['classes'].items():
                uc=list({r['canonical_pcm_sha256']:r for r in rr if r['record_class']==cls}.values())
                check(summary(uc)==expected,f'Class acoustic summary mismatch {lang}/{cls}')
        counts.update(contextual_talk_items=len(talks),exact_raw_text_keys_checked=renderedkeys,
                      localized_text_hashes_checked=hashtexts,occurrence_routes_checked=len(OC),
                      voice_semantic_records=len(V),render_associations=len(R),
                      unique_direct_pcm=len({r['canonical_pcm_sha256'] for r in R}))
        source_status='completed'
    report={'schema_version':'sigrika.packet-validation.v0.2','checked_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'status':'PASS' if not errors else 'FAIL','scope':'local mechanical integrity and optional original-source joins',
            'original_source_validation':source_status,'counts':counts,'errors':errors,
            'interpretive_boundary':'Mechanical validity does not establish interpretive correctness, blind prediction accuracy, or direct audiovisual perception.'}
    if args.output:
        args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,TypeError,IndexError) as exc:
        print(f'Validation failed: {type(exc).__name__}: {exc}',file=sys.stderr)
        raise SystemExit(2)
