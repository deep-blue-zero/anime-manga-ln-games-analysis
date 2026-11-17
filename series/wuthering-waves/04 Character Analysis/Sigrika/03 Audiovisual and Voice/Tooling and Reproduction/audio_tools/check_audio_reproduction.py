from pathlib import Path
import json,sys,hashlib,collections
if len(sys.argv)!=2:
    raise SystemExit('Usage: python check_audio_reproduction.py WORK_DIRECTORY')
W=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(Path(__file__).parent))
from analyze_audio import analyze_one,read_jsonl
S=W/'source';X=read_jsonl(S/'DRIVE_AUDIO_OBJECT_CROSSWALK.jsonl'); XM={x['canonical_pcm_sha256']:x for x in X}
L=read_jsonl(S/'COMPLETE_VOICE_LINE_ANALYSIS.jsonl')+read_jsonl(S/'COUNTERPART_COMPLETE_VOICE_LINE_ANALYSIS.jsonl')
refs=collections.defaultdict(list)
for l in L:
 for r in l['renders']:refs[r['canonical_pcm_sha256']].append({'line':l,'render':r})
R=read_jsonl(W/'AUDIO_OBJECT_MEASUREMENTS.jsonl');RM={r['canonical_pcm_sha256']:r for r in R}
picks=[]
for lang in ['zh','en','ja','ko']:
 picks.append(next(r['canonical_pcm_sha256'] for r in R if lang in r['voice_languages'] and r['evidence_scopes']==['direct_character'] and r['channels']==1 and 4<r['duration_seconds']<6))
picks.append(next(r['canonical_pcm_sha256'] for r in R if r['channels']==3))
rep=[]
for h in picks:
 new=analyze_one((str(W/'objects'/f'{h}.flac'),XM[h],refs[h]));old=RM[h]
 diffs=[k for k in sorted(set(new)|set(old)) if new.get(k)!=old.get(k)]
 rep.append({'canonical_pcm_sha256':h,'identical_result':not diffs,'changed_top_level_fields':diffs})
errors=[]
for r in R:
 h=r['canonical_pcm_sha256'];dt=r['duration_seconds']
 if r['status']!='measured':errors.append([h,'failed'])
 for t,g in r['gates'].items():
  if abs(g['active_seconds']+g['silent_seconds']-dt)>1e-8:errors.append([h,'durationpartition'])
  if g['leading_seconds']+g['trailing_seconds']+g['internal_gap_seconds']>g['silent_seconds']+1e-8:errors.append([h,'gaps'])
  if any(not 0<=a<b<=dt for a,b in g['internal_gaps_ge_100ms']):errors.append([h,'gapbounds'])
 if not r['gates']['-50']['active_seconds']>=r['gates']['-45']['active_seconds']>=r['gates']['-40']['active_seconds']:errors.append([h,'thresholdmonotonicity'])
 for q in r['source_linked_rate_proxies']:
  if q['units'] is None and q['units_per_object_second'] is not None:errors.append([h,'nonlexicalrate'])
report={'objects_checked':len(R),'integrity_checks':'FLAC + native payload previously verified for all objects; deterministic five-object remeasurement here', 'remeasurement_cases':rep,'gate_invariant_errors':errors,'status':'PASS' if not errors and all(x['identical_result'] for x in rep) else 'FAIL'}
(W/'AUDIO_REPRODUCTION_CHECK.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
