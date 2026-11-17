#!/usr/bin/env python3
"""Validate the Sigrika V0.2 audio additions. Read-only with respect to source data.

Without --work-dir: packet model, case, finding, probe and completion consistency.
With --work-dir: also verify original dependency hashes, full measurement rows,
source/semantic/render/object links, gate invariants, and published aggregates.
No network access. Mechanical checks are not a perceptual or predictive benchmark.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,math,statistics,sys
from pathlib import Path



# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_ACQUISITION_MANIFEST.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_ACQUISITION_MANIFEST.json', 'AUDIO_CLUSTER_RESULTS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_CLUSTER_RESULTS.json', 'AUDIO_CONTEXT_COHORTS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_CONTEXT_COHORTS.json', 'AUDIO_FIDELITY_PROBES.json': '04 Validation and Readiness/AUDIO_FIDELITY_PROBES.json', 'AUDIO_FINDING_INDEX.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_FINDING_INDEX.json', 'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_MATCHED_SEMANTIC_CASES.json', 'AUDIO_METHOD_PARAMETERS.json': '03 Audiovisual and Voice/Tooling and Reproduction/AUDIO_METHOD_PARAMETERS.json', 'AUDIO_OUTLIER_REVIEW_COHORT.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_OUTLIER_REVIEW_COHORT.json', 'AUDIO_PRIOR_CLAIM_SNAPSHOT.json': '04 Validation and Readiness/AUDIO_PRIOR_CLAIM_SNAPSHOT.json', 'AUDIO_REPRODUCTION_CHECK.json': '04 Validation and Readiness/AUDIO_REPRODUCTION_CHECK.json', 'AUDIO_REPRODUCTION_INSTRUCTIONS.txt': '03 Audiovisual and Voice/Tooling and Reproduction/AUDIO_REPRODUCTION_INSTRUCTIONS.txt', 'AUDIO_RETRIEVAL_QC_COHORT.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_RETRIEVAL_QC_COHORT.json', 'AUDIO_SOURCE_INPUT_MANIFEST.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_SOURCE_INPUT_MANIFEST.json', 'AUDIO_STAGE_VALIDATION_REPORT.json': '04 Validation and Readiness/AUDIO_STAGE_VALIDATION_REPORT.json', 'AUDIO_TO_VIDEO_TARGET_JOIN.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_TO_VIDEO_TARGET_JOIN.json', 'AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json', 'AV_RETRIEVAL_TARGETS.json': '03 Audiovisual and Voice/Machine Evidence and Manifests/AV_RETRIEVAL_TARGETS.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/Profiles and Plans/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'CLAIM_INDEX.json': '01 Evidence and Source-Facing/CLAIM_INDEX.json', 'DELIVERY_INVENTORY.json': '04 Validation and Readiness/DELIVERY_INVENTORY.json', 'EVIDENCE_BUNDLE_INDEX.json': '01 Evidence and Source-Facing/EVIDENCE_BUNDLE_INDEX.json', 'FIDELITY_PROBE_INDEX.json': '04 Validation and Readiness/FIDELITY_PROBE_INDEX.json', 'LOCAL_REVISION_REVIEW.json': '04 Validation and Readiness/LOCAL_REVISION_REVIEW.json', 'SHA256SUMS.txt': '04 Validation and Readiness/SHA256SUMS.txt', 'SHARD_ACQUISITION_AUDIT.json': '04 Validation and Readiness/SHARD_ACQUISITION_AUDIT.json', 'SOURCE_AND_AUDIO_AUDIT.json': '04 Validation and Readiness/SOURCE_AND_AUDIO_AUDIT.json', 'SOURCE_INPUT_MANIFEST.json': '04 Validation and Readiness/SOURCE_INPUT_MANIFEST.json', 'TOOLKIT_CAPABILITY_CHECK.json': '04 Validation and Readiness/TOOLKIT_CAPABILITY_CHECK.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_SIGRIKA_ANALYSIS_PACKET_README.md': 'WUWA_SIGRIKA_ANALYSIS_PACKET_README.md', 'WUWA_SIGRIKA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AUDIOVISUAL_EVIDENCE_NOMINATION_PLAN.md', 'WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AUDIO_METHOD_AND_RESULTS.md', 'WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md', 'WUWA_SIGRIKA_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_SIGRIKA_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json', 'WUWA_SIGRIKA_CURRENT_STATE.md': 'WUWA_SIGRIKA_CURRENT_STATE.md', 'WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_SIGRIKA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_SIGRIKA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_SIGRIKA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md', 'WUWA_SIGRIKA_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_SIGRIKA_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_SIGRIKA_RELATIONSHIP_AND_STATE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_RELATIONSHIP_AND_STATE_PROFILE.md', 'WUWA_SIGRIKA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_SIGRIKA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_SIGRIKA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/Profiles and Plans/WUWA_SIGRIKA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_SIGRIKA_TALENT_EXPECTATION_AND_INTERPRETIVE_AGENCY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SIGRIKA_TALENT_EXPECTATION_AND_INTERPRETIVE_AGENCY_PROFILE.md', 'analyze_audio.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/analyze_audio.py', 'check_audio_reproduction.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/check_audio_reproduction.py', 'requirements-audio.txt': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/requirements-audio.txt', 'summarize_audio.py': '03 Audiovisual and Voice/Tooling and Reproduction/audio_tools/summarize_audio.py', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py', 'validate_audio_stage.py': '04 Validation and Readiness/validate_audio_stage.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def load(p):
 s=p.read_text(encoding='utf-8',errors='strict')
 return [json.loads(l) for l in s.splitlines() if l.strip()] if p.suffix=='.jsonl' else json.loads(s)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--packet',type=Path,default=Path(__file__).resolve().parent.parent);ap.add_argument('--work-dir',type=Path);ap.add_argument('--output',type=Path);args=ap.parse_args();N=args.packet.resolve();errors=[];counts={}
 def check(ok,msg):
  if not ok:errors.append(msg)
 def close(a,b):return a is not None and b is not None and math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-8)
 D=load(packet_artifact(N, 'AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json'));F=load(packet_artifact(N, 'AUDIO_FINDING_INDEX.json'));P=load(packet_artifact(N, 'AUDIO_FIDELITY_PROBES.json'));C=load(packet_artifact(N, 'AUDIO_MATCHED_SEMANTIC_CASES.json'));AC=load(packet_artifact(N, 'AUDIO_CONTEXT_COHORTS.json'));J=load(packet_artifact(N, 'AUDIO_TO_VIDEO_TARGET_JOIN.json'));M=load(packet_artifact(N, 'WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json'));Q=load(packet_artifact(N, 'AUDIO_RETRIEVAL_QC_COHORT.json'));A=load(packet_artifact(N, 'AUDIO_ACQUISITION_MANIFEST.json'))
 check(D['total_unique_objects']==2809 and not D['failures'],'Full object completion')
 check(len(F)==12 and len({f['id'] for f in F})==12,'Finding identities')
 check(len(P)==12 and len({p['id'] for p in P})==12,'Audio-probe identities')
 check(len(C)==20 and len({c['id'] for c in C})==20,'Case identities')
 check(len(AC)==8 and len(J)==24,'Cohort or target join count')
 check(len(A['acquired_shards'])==19 and all(a['drive_file_id'] and a['status']=='sha256_verified' for a in A['acquired_shards']),'Verified acquired archive routes')
 check(M['audio_constraints']['direct_objects']==2652 and M['audio_constraints']['direct_pitch_comparison_objects']==2531,'Model measurement denominator')
 check(M['completion_states']['machine_voice_profiled'] is True,'Machine completion gate')
 for k in ['audiovisually_hardened','integrated_reconstruction_completed','human_performance_partially_reviewed','human_performance_hardened']:
  check(M['completion_states'][k] is False,'Unsupported completion '+k)
 check(not D['human_perceptual_review_performed'] and not D['video_review_performed'],'No fabricated review')
 fids={f['id'] for f in F};cids={c['id'] for c in C};acids={a['id'] for a in AC};eids={e['id'] for e in load(packet_artifact(N, 'EVIDENCE_BUNDLE_INDEX.json'))}
 for f in F:
  check(set(f['case_ids'])<=cids and set(f['cohort_ids'])<=acids and set(f['evidence_bundle_ids'])<=eids,'Finding source refs '+f['id'])
 for p in P:
  check(set(p['finding_ids'])<=fids and p['empirical_accuracy'] is None and p['result']=='constraint_checked','Probe integrity '+p['id'])
 for c in C:
  check({r['language'] for r in c['renders']}=={'zh','en','ja','ko'},'Four-language cases '+c['id'])
  check(c['perceptual_review_status']=='not_performed','Unperformed perception '+c['id'])
 check(all(q['acquisition_status']=='acquired' and q['perception_status']=='not_listened' for q in Q),'Original QC status')
 check(all(t['acquisition_status']=='deferred_owner_local_1080p_or_larger' and t['viewing_status']=='not_viewed' for t in load(packet_artifact(N, 'AV_RETRIEVAL_TARGETS.json'))),'Deferred-video state')
 # Explicit non-blind checks supporting the added model probes.
 bycase={c['id']:c for c in C}
 def case(i,l):return next(r for r in bycase[f'SIG-AM-{i:02}']['renders'] if r['language']==l)
 probe_checks={
 'SIG-AP-01':D['scopes']['direct_character']['unique_objects']==2652 and D['scopes']['dark_side_counterpart']['unique_objects']==157,
 'SIG-AP-02':D['scopes']['direct_character']['pitch_qc_qualified']==2531,
 'SIG-AP-03':all(AC[0]['languages'][l]['f0_percentile_median']>AC[2]['languages'][l]['f0_percentile_median'] for l in ['zh','en','ja','ko']),
 'SIG-AP-04':case(9,'zh')['f0_hz']>case(10,'zh')['f0_hz'] and all(AC[3]['languages'][l]['qc_f0_hz']['median']>AC[2]['languages'][l]['qc_f0_hz']['median'] for l in ['zh','en','ja','ko']),
 'SIG-AP-05':case(14,'zh')['f0_hz_within_language_percentile']>50 and case(14,'en')['f0_hz_within_language_percentile']<50,
 'SIG-AP-06':abs(case(8,'en')['f0_hz']-case(6,'en')['f0_hz'])<2 and all(case(8,l)['f0_hz']-case(6,l)['f0_hz']>50 for l in ['zh','ja','ko']),
 'SIG-AP-07':all(case(5,l)['duration']>6 and case(5,l)['silent_fraction']>.6 for l in ['zh','en','ja','ko']),
 'SIG-AP-08':any(g['row']==12967 and g['mapped_media_associations']==0 for g in D['diagnostic_unvoiced_boundaries']),
 'SIG-AP-09':any(g['row']==16901 and g['mapped_media_associations']==0 for g in D['diagnostic_unvoiced_boundaries']) and '/favorword.json#/' in bycase['SIG-AM-16']['source_locator'],
 'SIG-AP-10':D['scopes']['dark_side_counterpart']['channel_counts']['3']==32 and M['audio_constraints']['counterpart_objects_excluded_from_direct_baselines']==157,
 'SIG-AP-11':all(c['silhouette']<.3 for c in D['clustering']) and 'cluster to personality state' in M['audio_constraints']['forbidden_shortcuts'],
 'SIG-AP-12':M['completion_states']['machine_voice_profiled'] and not M['completion_states']['human_performance_partially_reviewed'] and not M['completion_states']['audiovisually_hardened']}
 for pid,ok in probe_checks.items():check(ok,'Probe predicate failed '+pid)
 counts.update(findings=len(F),added_nonblind_probes=len(P),source_defined_cohorts=len(AC),same_semantic_cases=len(C),selected_case_render_associations=sum(len(c['renders']) for c in C),video_target_joins=len(J),verified_archives=19)
 source_checks='not_run_without_work_directory'
 if args.work_dir:
  W=args.work_dir.resolve();S=W/'source';R=load(W/'AUDIO_OBJECT_MEASUREMENTS.jsonl');RM={r['canonical_pcm_sha256']:r for r in R};X=load(S/'DRIVE_AUDIO_OBJECT_CROSSWALK.jsonl');XM={x['canonical_pcm_sha256']:x for x in X};L=load(S/'COMPLETE_VOICE_LINE_ANALYSIS.jsonl');CL=load(S/'COUNTERPART_COMPLETE_VOICE_LINE_ANALYSIS.jsonl');LM={l['semantic_voice_occurrence_id']:l for l in L+CL};ref={r['render_analysis_id']:(l,r) for l in L+CL for r in l['renders']}
  for s in load(packet_artifact(N, 'AUDIO_SOURCE_INPUT_MANIFEST.json')):
   f=S/s['local_file_name'];check(f.is_file() and f.stat().st_size==s['bytes'] and sha(f)==s['sha256'],'Audio input hash '+s['local_file_name'])
  check(set(RM)==set(XM) and len(R)==2809,'Full source object identity set')
  for r in R:
   h=r['canonical_pcm_sha256'];x=XM[h]
   check(r['status']=='measured' and r['integrity']['flac_sha256_match'] and r['integrity']['native_pcm_payload_match'],'Object completion '+h)
   check(r['flac_sha256']==x['flac_sha256'] and r['archive_member_path']==x['archive_member_path'] and r['drive_relative_path']==x['drive_relative_path'],'Object source route '+h)
   check(r['perceptual_listening_performed'] is False,'Object perception '+h)
   check(set(r['semantic_occurrence_ids'])<=set(LM) and set(r['render_association_ids'])<=set(ref),'Object semantic/render identity '+h)
   dt=r['duration_seconds'];check(close(dt,r['frame_count']/r['sample_rate_hz']),'Sample duration '+h)
   for t,g in r['gates'].items():
    check(close(g['active_seconds']+g['silent_seconds'],dt),'Gate partition '+h+t)
    check(g['leading_seconds']+g['trailing_seconds']+g['internal_gap_seconds']<=g['silent_seconds']+1e-8,'Gap accounting '+h+t)
    check(all(0<=a<b<=dt for a,b in g['internal_gaps_ge_100ms']),'Gap bounds '+h+t)
   check(r['gates']['-50']['active_seconds']>=r['gates']['-45']['active_seconds']>=r['gates']['-40']['active_seconds'],'Gate monotonicity '+h)
   for q in r['source_linked_rate_proxies']:
    check(q['render_analysis_id'] in ref,'Rate association '+h)
    check(q['units'] is not None or q['units_per_object_second'] is None,'Nonlexical rate '+h)
  flat=load(W/'AUDIO_ASSOCIATION_FEATURES.jsonl');check(len(flat)==2837,'Association feature count')
  for a in flat:
   check(a['render_id'] in ref and a['pcm'] in RM,'Association routes')
   l,r=ref[a['render_id']]
   check(a['semantic_id']==l['semantic_voice_occurrence_id'] and a['source_locator']==l['source_locator'] and a['language']==r['voice_language'] and a['pcm']==r['canonical_pcm_sha256'],'Association identity '+a['render_id'])
   check(close(a['duration'],RM[a['pcm']]['duration_seconds']),'Association duration')
   check(close(a['active_frame_median_dbfs'],RM[a['pcm']]['gates']['-45']['active_frame_energy_dbfs']['median']),'Active-frame definition')
  for scope in ['direct_character','dark_side_counterpart']:
   rr=[r for r in R if scope in r['evidence_scopes']];s=D['scopes'][scope]
   check(len(rr)==s['unique_objects'] and sum(r['integrity']['flac_bytes'] for r in rr)==s['flac_bytes'] and close(sum(r['duration_seconds'] for r in rr),s['duration_sum_seconds']),'Scope aggregates '+scope)
  for key,g in D['by_language'].items():
   scope,lang=key.split(':');a=list({r['pcm']:r for r in flat if r['scope']==scope and r['language']==lang}.values())
   check(len(a)==g['unique_objects'],'Language count '+key)
   for k in ['duration','active_frame_median_dbfs','rms_dbfs','silent_fraction','internal_gap_seconds','gap_density','hnr_db','centroid_hz','spectral_tilt_db_octave']:
    vals=[r[k] for r in a if r.get(k) is not None];check(len(vals)==g[k]['n'] and close(statistics.median(vals),g[k]['median']),'Language median '+key+' '+k)
   p=[r['f0_hz'] for r in a if r['pitch_qc_qualified']];check(len(p)==g['pitch_qc_qualified'] and close(statistics.median(p),g['qc_f0_hz']['median']),'Pitch median '+key)
  for c in C:
   l=LM[c['semantic_id']];check(c['source_locator']==l['source_locator'] and c['text_key']==l['text_key'],'Selected source '+c['id'])
   for lang,txt in c['localized_texts'].items():
    w=l['text_witnesses'].get(lang,l['text_witnesses'].get('zh-Hans',{}));check(txt==w.get('content',w.get('text','')),'Selected canonical text '+c['id']+'/'+lang)
  for co in AC:
   check(set(co['semantic_ids'])<={l['semantic_voice_occurrence_id'] for l in L},'Direct cohort purity '+co['id'])
  for fn in ['AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json','AUDIO_MATCHED_SEMANTIC_CASES.json','AUDIO_CONTEXT_COHORTS.json','AUDIO_CLUSTER_RESULTS.json','AUDIO_OUTLIER_REVIEW_COHORT.json','AUDIO_REPRODUCTION_CHECK.json']:
   check(load(W/fn)==load(packet_artifact(N, fn)),'Published/work result mismatch '+fn)
  counts.update(all_objects_checked=len(R),all_render_associations_checked=len(flat),semantic_records_checked=len(L)+len(CL),audio_source_hashes_checked=len(load(packet_artifact(N, 'AUDIO_SOURCE_INPUT_MANIFEST.json'))))
  source_checks='completed'
 report={'schema_version':'sigrika.audio-stage-validation.v0.2','status':'PASS' if not errors else 'FAIL','scope':'mechanical source/measurement/model consistency; non-blind probe predicates','full_work_directory_checks':source_checks,'counts':counts,'nonblind_probe_predicates':probe_checks,'errors':errors,'no_claim_of_perceptual_listening_or_predictive_accuracy':True}
 if args.output:dump=json.dumps(report,indent=2,ensure_ascii=False)+'\n';args.output.write_text(dump)
 print(json.dumps(report,indent=2,ensure_ascii=False));return 0 if not errors else 1
if __name__=='__main__':
 try:raise SystemExit(main())
 except (OSError,ValueError,KeyError) as e:raise SystemExit('Audio validation failed: '+str(e))
