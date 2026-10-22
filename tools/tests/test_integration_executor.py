from __future__ import annotations

import copy
import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from nightly_integration import (
    AUTHOR, COMMITTER, CONTROLLER, OWNER, REPOSITORY, Blocked, Graph,
    Halt, Integrator, eligible_paths, main,
)
from test_nightly_integration import B, S, M, G, FakeAPI, graph_mock


class ExecutorTests(unittest.TestCase):
    def worker(self, api=None, candidates='open-prs'):
        worker = Integrator(api or FakeAPI(), graph_mock(), preview=False, candidates=candidates)
        worker.save = mock.Mock()
        return worker

    def test_missing_selected_branch_is_blocked_without_writes(self):
        """An absent selection is a blocked scan with no remote mutation."""
        for candidates in ('open-prs', 'analysis-branches'):
            with self.subTest(candidates=candidates):
                worker = self.worker(candidates=candidates)
                worker.run('series/missing')
                self.assertEqual(worker.rows[-1]['outcome'], 'blocked')
                worker.graph.push.assert_not_called()
                self.assertEqual(worker.api.writes, [])

    def test_completed_receipt_records_the_verified_integration(self):
        """A completed receipt names the merged PR, audited head and integration commit."""
        with tempfile.TemporaryDirectory() as directory:
            worker = self.worker()
            worker.save = Integrator.save.__get__(worker)
            worker.report_path = Path(directory) / 'receipt.json'
            worker.run('series/a')
            receipt = json.loads(worker.report_path.read_text(encoding='utf-8'))
            self.assertEqual(receipt['candidates'], 'open-prs')
            row = receipt['branches'][-1]
            self.assertEqual((row['outcome'], row['pr'], row['final_source_sha'], row['integration_sha']),
                             ('merged_verified', 8, S, M))

    def test_post_merge_failure_stops_the_run_and_keeps_the_integration_sha(self):
        """A failed main audit reports integrated-but-unverified and stops further merges."""
        worker = self.worker()
        worker.api.post_failure = True
        with self.assertRaises(Halt):
            worker.run('series/a')
        self.assertEqual(worker.rows[-1]['integration_sha'], M)
        self.assertEqual(worker.rows[-1]['outcome'], 'integrated_unverified')

    def test_ci_agent_integrates_cross_cutting_owner_pr(self):
        """The CI agent may merge tooling or governance changes outside the guardrails."""
        worker = self.worker()
        worker.api.pr['head']['ref'] = 'agent/validator-fix'
        worker.graph.paths.return_value = {'tools/validate_repository.py', 'governance/policies/BRANCH_LIFECYCLE.md'}
        worker.run('agent/validator-fix')
        self.assertEqual(worker.rows[-1]['outcome'], 'merged_verified')
        self.assertEqual(worker.api.writes, [('PUT', 'pulls/8/merge', {'sha': S, 'merge_method': 'merge'})])

    def test_guardrail_pr_is_left_for_the_owner(self):
        """Changes to workflows, the merge gate or the CI agent's rules are never auto-merged."""
        worker = self.worker()
        worker.api.pr['head']['ref'] = 'agent/gate-change'
        worker.graph.paths.return_value = {'tools/nightly_integration.py'}
        worker.run('agent/gate-change')
        self.assertEqual(worker.rows[-1]['outcome'], 'blocked')
        self.assertIn('the owner merges it', worker.rows[-1]['detail'])
        self.assertEqual(worker.api.writes, [])

    def test_final_audit_change_before_merge_blocks(self):
        """A final audit that stops being a trusted success immediately before merge blocks publication."""
        worker = self.worker()
        guard = worker.guard_mutation
        def fail_audit(*args, **kwargs):
            guard(*args, **kwargs)
            worker.api.source_status = 'failure'
        worker.guard_mutation = fail_audit
        worker.run('series/a')
        self.assertEqual(worker.rows[-1]['outcome'], 'blocked')
        self.assertFalse(any(path.endswith('/merge') for _, path, _ in worker.api.writes))

    def test_reconciliation_and_pr_creation_precede_the_merge(self):
        """A bulk run reconciles a stale analysis branch, opens its PR, then merges it."""
        worker = self.worker(candidates='analysis-branches')
        worker.graph.ancestor.side_effect = lambda base, head: base == B and head == G
        worker.graph.reconcile_commit.return_value = G
        observed = []
        def push(branch, sha, token):
            observed.append('push')
            worker.api.source = sha
            worker.api.pr['head']['sha'] = sha
        worker.graph.push.side_effect = push
        pages, request = worker.api.pages, worker.api.request
        created = False
        def no_pr(path):
            return [] if path.startswith('pulls?') and not created else pages(path)
        def create_pr(method, path, payload=None):
            nonlocal created
            if (method, path) == ('POST', 'pulls'):
                observed.append('create_pr')
                created = True
                return worker.api.pr
            if path.endswith('/merge'):
                observed.append('merge')
            return request(method, path, payload)
        worker.api.pages, worker.api.request = no_pr, create_pr
        worker.run('series/a')
        self.assertEqual(observed, ['push', 'create_pr', 'merge'])
        self.assertEqual(worker.rows[-1]['reconciled_sha'], G)
        self.assertEqual(worker.rows[-1]['outcome'], 'merged_verified')

    def test_new_hold_before_reconciliation_prevents_source_push(self):
        """A hold arriving after preparation is enforced before source publication."""
        worker = self.worker()
        worker.graph.ancestor.side_effect = lambda base, head: False
        def prepare(*args):
            worker.api.pr['draft'] = True
            return G
        worker.graph.reconcile_commit.side_effect = prepare
        worker.run('series/a')
        worker.graph.push.assert_not_called()
        self.assertEqual(worker.rows[-1]['outcome'], 'blocked')

    def test_ambiguous_merge_halts_without_retry(self):
        """A timed-out merge is not treated as absent while a request could still finish."""
        worker = self.worker()
        request = worker.api.request
        def ambiguous(method, path, payload=None):
            if path.endswith('/merge'):
                worker.api.writes.append((method, path, payload))
                raise OSError('timeout')
            return request(method, path, payload)
        worker.api.request = ambiguous
        with self.assertRaisesRegex(Halt, 'uncertain'):
            worker.run('series/a')
        self.assertEqual(sum(path.endswith('/merge') for _, path, _ in worker.api.writes), 1)

    def test_malformed_merge_acknowledgement_halts(self):
        """An invalid merge acknowledgement cannot become a harmless candidate deferral."""
        for response in ({'merged': True, 'sha': 'invalid'}, {'sha': M}):
            with self.subTest(response=response):
                worker = self.worker()
                request = worker.api.request
                def malformed(method, path, payload=None):
                    result = request(method, path, payload)
                    return response if path.endswith('/merge') else result
                worker.api.request = malformed
                with self.assertRaises(Halt):
                    worker.run('series/a')
                if response.get('merged'):
                    self.assertEqual(worker.rows[-1]['outcome'], 'integrated_unverified')

    def test_observed_hold_remains_binding_after_removal(self):
        """A hold observed during a cycle cannot be cleared by a later PR reread."""
        worker = self.worker()
        worker.api.pr['draft'] = True
        with self.assertRaises(Blocked):
            worker.candidate_pr('series/a')
        worker.api.pr['draft'] = False
        with self.assertRaises(Blocked):
            worker.candidate_pr('series/a')
        self.assertFalse(worker.api.writes)

    def test_capture_observes_holds_before_candidate_processing(self):
        """Initial inventory holds bind the whole cycle even if later removed."""
        worker = self.worker()
        worker.api.pr['labels'] = [{'name': 'nightly-hold'}]
        pages = worker.api.pages
        def inventory(path):
            result = copy.deepcopy(pages(path))
            if path == 'pulls?state=open&base=main':
                worker.api.pr['labels'] = []
            return result
        worker.api.pages = inventory
        worker.run('series/a')
        self.assertEqual(worker.rows[0]['outcome'], 'blocked')
        self.assertFalse(any(path.endswith('/merge') for _, path, _ in worker.api.writes))

    def test_foreign_fork_hold_does_not_block_owner_branch_with_same_name(self):
        """Only the owner same-repository PR can impose a hold on its source branch."""
        worker = self.worker()
        foreign = copy.deepcopy(worker.api.pr)
        foreign.update(number=9, draft=True, user={'login': 'other'})
        foreign['head']['repo']['full_name'] = 'other/fork'
        pages = worker.api.pages
        worker.api.pages = lambda path: [foreign, worker.api.pr] if path == 'pulls?state=open&base=main' else pages(path)
        worker.run('series/a')
        self.assertEqual(worker.rows[-1]['outcome'], 'merged_verified')

    def test_guardrail_paths_are_owner_merged_on_every_branch(self):
        """Workflows, the merge gate, the CI agent's rules, owner authorization records, provenance and legal files stay owner-merged."""
        for path in ('.github/workflows/a.yml', '.github/CODEOWNERS', 'tools/nightly_integration.py',
                     'governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md', 'crosswalk/a.json',
                     'provenance/a.md', 'AGENTS.md', 'LICENSE.md', 'THIRD_PARTY_NOTICES.md',
                     'governance/repository-controls/project-initiation-gate.json',
                     'governance/repository-controls/reconstruction-capability-policy.json',
                     'governance/repository-controls/tracked-file-policy.json',
                     'governance/AUTHORITY_SCOPE.json', 'governance/AUTHORITY_STATE.yaml',
                     'governance/cutovers/AUTHORITY_EPOCH_1.json'):
            for branch in ('series/a', 'agent/fix', 'character-registry'):
                with self.subTest(path=path, branch=branch):
                    self.assertFalse(eligible_paths(branch, {path}))
        for paths in ({'tools/validate_repository.py'}, {'governance/policies/BRANCH_LIFECYCLE.md'},
                      {'README.md'}, {'characters/registry.jsonl', 'CHARACTER_ANALYSIS_INDEX.md'}):
            with self.subTest(paths=paths):
                self.assertTrue(eligible_paths('agent/fix', paths))

    def test_reconstruction_outputs_come_only_from_the_evaluator_branch(self):
        """Only character-reconstruction may change reconstruction outputs, and it may change nothing else."""
        outputs = {'characters/reconstruction_capabilities.jsonl', 'characters/CHARACTER_RECONSTRUCTION_INDEX.md'}
        self.assertTrue(eligible_paths('character-reconstruction', outputs))
        for paths in (outputs | {'tools/validate_repository.py'}, {'series/a/analysis.md'}, {'README.md'}):
            with self.subTest(branch='character-reconstruction', paths=paths):
                self.assertFalse(eligible_paths('character-reconstruction', paths))
        for branch in ('agent/fix', 'series/a', 'character-registry'):
            with self.subTest(branch=branch):
                self.assertFalse(eligible_paths(branch, {'characters/reconstruction_capabilities.jsonl'}))

    def test_reconstruction_outputs_wait_for_the_owner_until_calibration_is_accepted(self):
        """Reconstruction PRs are owner-merged in any phase but ROUTINE, read from main's policy."""
        for phase, outcome in (('CALIBRATION', 'blocked'), (None, 'blocked'), ('ROUTINE', 'merged_verified')):
            with self.subTest(phase=phase):
                worker = self.worker()
                worker.api.pr['head']['ref'] = 'character-reconstruction'
                worker.graph.paths.return_value = {'characters/reconstruction_capabilities.jsonl',
                                                   'characters/CHARACTER_RECONSTRUCTION_INDEX.md'}
                worker.graph.reconstruction_phase.return_value = phase
                worker.run('character-reconstruction')
                self.assertEqual(worker.rows[-1]['outcome'], outcome)
                worker.graph.reconstruction_phase.assert_called_with(B)
                if outcome == 'blocked':
                    self.assertIn('calibration', worker.rows[-1]['detail'])
                    self.assertEqual(worker.api.writes, [])
        graph = object.__new__(Graph)
        graph.git = mock.Mock(return_value=json.dumps({'publication_phase': 'CALIBRATION'}))
        self.assertEqual(graph.reconstruction_phase(B), 'CALIBRATION')
        self.assertEqual(graph.git.call_args, mock.call(
            'show', f'{B}:governance/repository-controls/reconstruction-capability-policy.json'))

    def test_analysis_branches_stay_inside_their_root(self):
        """A series or study branch may change only its own root, routing outputs and curation files."""
        self.assertTrue(eligible_paths('series/a', {'series/a/analysis.md', 'series/registry.json'}))
        self.assertTrue(eligible_paths('series/a', {'characters/registry.jsonl'}))
        for path in ('series/b/analysis.md', 'tools/validate_repository.py', 'README.md'):
            with self.subTest(path=path):
                self.assertFalse(eligible_paths('series/a', {path}))

    def test_actions_apply_requires_owner_dispatch_on_main(self):
        """Inside GitHub Actions the CLI rejects scheduled, foreign or off-main apply."""
        for event, actor, ref in (('schedule', OWNER, 'refs/heads/main'), ('workflow_dispatch', 'other', 'refs/heads/main'),
                                  ('workflow_dispatch', OWNER, 'refs/heads/series/a')):
            with self.subTest(event=event, actor=actor, ref=ref), \
                    mock.patch.dict(os.environ, {'GITHUB_REPOSITORY': REPOSITORY, 'GITHUB_ACTIONS': 'true',
                                                 'GITHUB_REF': ref, 'GITHUB_EVENT_NAME': event,
                                                 'GITHUB_ACTOR': actor, 'OWNER_TOKEN': 'test'}), \
                    mock.patch.object(sys, 'argv', ['executor', '--mode', 'apply']), \
                    mock.patch('nightly_integration.Graph') as graph, self.assertRaises(SystemExit):
                main()
            graph.assert_not_called()

    def test_apply_requires_an_owner_token(self):
        """Apply cannot start without the owner's integration token."""
        environment = {key: value for key, value in os.environ.items() if key not in {'OWNER_TOKEN', 'GITHUB_ACTIONS'}}
        with mock.patch.dict(os.environ, environment, clear=True), \
                mock.patch.object(sys, 'argv', ['executor', '--mode', 'apply']), \
                mock.patch('nightly_integration.Graph') as graph, self.assertRaises(SystemExit):
            main()
        graph.assert_not_called()

    def test_unapproved_commit_identity_is_rejected(self):
        """Identity verification covers every source-only commit, not merely the tip."""
        graph = object.__new__(Graph)
        policy = {'allowed_author_identities': [AUTHOR], 'allowed_committer_identities': [COMMITTER]}
        log = f'{S}\tOther\tother@example.invalid\tGitHub\tnoreply@github.com'
        graph.git = mock.Mock(side_effect=[json.dumps(policy), log])
        with self.assertRaises(Halt):
            graph.verify_identities(B, S)

    def test_runtime_must_match_the_merge_script_on_current_main(self):
        """Apply runs only the exact script bytes on main, including trailing newlines."""
        graph = object.__new__(Graph)
        script = (ROOT / CONTROLLER).read_bytes()
        graph.git = mock.Mock(return_value=script)
        graph.verify_runtime(B)
        self.assertEqual(graph.git.call_args, mock.call('show', f'{B}:{CONTROLLER}', raw=True))
        for changed in (script + b'\n', b'changed code'):
            with self.subTest(changed=changed[-12:]):
                graph.git = mock.Mock(return_value=changed)
                with self.assertRaisesRegex(Halt, 'fresh checkout'):
                    graph.verify_runtime(B)
        self.assertEqual(hashlib.sha256(script).hexdigest(), __import__('nightly_integration').LOADED_SHA256)

    def test_mixed_character_commit_is_not_a_curator_repair(self):
        """A two-file curation repair cannot conceal analytical or control changes."""
        graph = object.__new__(Graph)
        graph.git = mock.Mock(side_effect=[S, 'characters/registry.jsonl\0series/a/analysis.md\0'])
        with self.assertRaises(Blocked):
            graph.verify_curation_commits(B, S)

    def test_receipt_is_written_atomically_outside_the_disposable_graph(self):
        """A receipt records an integration SHA before cleanup, without leaving a temporary file."""
        with tempfile.TemporaryDirectory() as directory:
            worker = self.worker()
            worker.save = Integrator.save.__get__(worker)
            worker.report_path = Path(directory) / 'state' / 'receipt.json'
            worker.rows = [{'integration_sha': M, 'outcome': 'integrated_unverified'}]
            worker.save()
            receipt = json.loads(worker.report_path.read_text())
            self.assertEqual(receipt['branches'][0]['integration_sha'], M)
            self.assertFalse(worker.report_path.with_suffix('.tmp').exists())


class CurationMergeTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.graph = Graph(Path(directory.name))
        self.files = {'characters/registry.jsonl': 'original registry\n',
                      'CHARACTER_ANALYSIS_INDEX.md': 'original index\n',
                      'series/a/analysis.md': 'original analysis\n'}
        self.base = self.commit(self.files)
        self.curated = dict(self.files, **{'characters/registry.jsonl': 'curated registry\n',
                                         'CHARACTER_ANALYSIS_INDEX.md': 'curated index\n'})

    def commit(self, files, *parents):
        self.graph.git('read-tree', '--empty')
        for path, content in files.items():
            blob = self.graph.git('hash-object', '-w', '--stdin', input_text=content)
            self.graph.git('update-index', '--add', '--cacheinfo', '100644', blob, path)
        tree = self.graph.git('write-tree')
        return self.graph.git('commit-tree', tree, *[arg for p in parents for arg in ('-p', p)],
                              input_text='curation provenance fixture\n', extra_env={
                                  'GIT_AUTHOR_NAME': AUTHOR['name'], 'GIT_AUTHOR_EMAIL': AUTHOR['email'],
                                  'GIT_COMMITTER_NAME': COMMITTER['name'], 'GIT_COMMITTER_EMAIL': COMMITTER['email']})

    def test_merge_cannot_author_character_outputs(self):
        """A merge cannot hide new character bytes beside ordinary analytical changes."""
        left_files = dict(self.files, **{'series/a/analysis.md': 'left analysis\n'})
        left = self.commit(left_files, self.base)
        right = self.commit(dict(self.files, **{'series/a/other.md': 'right analysis\n'}), self.base)
        merged = self.commit(dict(self.curated, **{'series/a/analysis.md': 'left analysis\n',
                                                 'series/a/other.md': 'right analysis\n'}), left, right)
        with self.assertRaises(Blocked):
            self.graph.verify_curation_commits(self.base, merged)

    def test_clean_merge_preserves_separate_curation_and_main_imports(self):
        """Clean imports retain curation-only provenance with either parent order."""
        analytical = self.commit(dict(self.files, **{'series/a/analysis.md': 'new analysis\n'}), self.base)
        curated = self.commit(self.curated, self.base)
        for parents in ((analytical, curated), (curated, analytical)):
            merged = self.commit(dict(self.curated, **{'series/a/analysis.md': 'new analysis\n'}), *parents)
            with self.subTest(parents=parents):
                self.graph.verify_curation_commits(self.base, merged)
                self.graph.verify_curation_commits(curated, merged)

    def test_character_conflict_resolution_requires_separate_curation(self):
        """Choosing one conflicting parent's character bytes is still a curation decision."""
        left = self.commit(self.curated, self.base)
        right = self.commit(dict(self.files, **{'characters/registry.jsonl': 'other registry\n',
                                               'CHARACTER_ANALYSIS_INDEX.md': 'other index\n'}), self.base)
        merged = self.commit(self.curated, left, right)
        with self.assertRaises(Blocked):
            self.graph.verify_curation_commits(self.base, merged)

    def test_unrelated_conflict_does_not_reject_preserved_curation(self):
        """Resolving analytical prose may preserve a clean, separately authored curation import."""
        left_files = dict(self.files, **{'series/a/analysis.md': 'left analysis\n'})
        left = self.commit(left_files, self.base)
        curated = self.commit(dict(self.curated, **{'series/a/analysis.md': 'left analysis\n'}), left)
        right = self.commit(dict(self.files, **{'series/a/analysis.md': 'right analysis\n'}), self.base)
        merged = self.commit(dict(self.curated, **{'series/a/analysis.md': 'reconciled analysis\n'}), curated, right)
        self.graph.verify_curation_commits(self.base, merged)


if __name__ == '__main__':
    unittest.main()
