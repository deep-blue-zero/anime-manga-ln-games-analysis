"""Bounded retrospective reconstruction probe; no fitted probabilities or language simulation."""
from pathlib import Path
import json,sys,hashlib
def evaluate(spec,case):
 model=spec['models'][case['subject']]
 unknown=set(case.get('known_facts',[]))-set(model['allowed_facts'])
 if unknown:return {'decision':'ABSTAIN_FORBIDDEN_OR_UNVERIFIED_KNOWLEDGE','rule':None,'rejected_facts':sorted(unknown)}
 if case.get('domain')!=model['domain']:return {'decision':'ABSTAIN_UNSUPPORTED_DOMAIN','rule':None}
 features=set(case.get('features',[]))
 for rule in model['rules']:
  if set(rule['if_all'])<=features:return {'decision':rule['then'],'rule':rule['id']}
 return {'decision':'ABSTAIN_NO_RULE','rule':None}
def main():
 specpath=Path(sys.argv[1]);casespath=Path(sys.argv[2]);output=Path(sys.argv[3])
 raw=specpath.read_bytes();spec=json.loads(raw);cases=json.loads(casespath.read_text(encoding='utf-8'))
 assert spec['version']=='1.0' and spec['validation_design']=='RETROSPECTIVE_FULL_SOURCE_EXPOSED_NOT_HELD_OUT'
 results=[]
 for case in cases['cases']:
  actual=evaluate(spec,case);results.append({'case_id':case['id'],'subject':case['subject'],'frontier':case['frontier'],'source_outcome':case['source_outcome'],'kind':case['kind'],'context':case['context'],'prediction':actual,'matched_declared_category':actual['decision']==case['expected_category'],'limitation':case['limitation']})
 output.write_text(json.dumps({'spec_sha256':hashlib.sha256(raw).hexdigest(),'spec_evidence_snapshot':spec['g2_input_commit'],'rule_freeze_commit':cases['rule_freeze_commit'],'design':spec['validation_design'],'result':'RETROSPECTIVE_PROBES_EXECUTED_OPERATIONAL_ACCEPTANCE_BLOCKED','cases':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({'cases_executed':len(results),'results':[{'id':x['case_id'],'decision':x['prediction']['decision'],'matched_category':x['matched_declared_category']} for x in results]},indent=2))
if __name__=='__main__':main()
