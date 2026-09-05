from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from nightly_integration import (
    AUDIT, AUDIT_WORKFLOW, AUTHOR, COMMITTER, GENERATED, OWNER, REPOSITORY,
    ApiError, Blocked, GitHub, Graph, Halt, Integrator, protection_method, scoped_paths,
)
from character_index_core import GitSnapshot, SnapshotEntry
from validate_repository import validate_nightly_integration

B, S, M, G = 'b'*40, 'a'*40, 'c'*40, 'd'*40
PROTECTION = {'required_status_checks': {'strict': True, 'contexts': [AUDIT]}, 'enforce_admins': {'enabled': True}}
METADATA = {'allow_merge_commit': True, 'allow_squash_merge': True}


def pull():
    return {'number': 8, 'state': 'open', 'draft': False, 'labels': [],
            'user': {'login': OWNER}, 'base': {'ref': 'main'},
            'head': {'sha': S, 'repo': {'full_name': REPOSITORY}}}


class FakeAPI:
    token = 'test-credential'

    def __init__(self):
        self.main = B
        self.source = S
        self.writes = []
        self.dispatched = False
        self.source_status = 'success'
        self.post_failure = False
        self.merge_error = False
        self.pr = pull()

    def head(self, branch):
        return self.main if branch == 'main' else self.source

    def pages(self, path):
        if path == 'branches':
            return [{'name': name, 'commit': {'sha': S}} for name in ('series/a', 'codex/repair', 'character-registry', 'studies/b')]
        return [self.pr]

    def status(self, sha):
        if sha == M and not self.dispatched:
            return None
        state = ('failure' if self.post_failure else 'success') if sha == M else self.source_status
        return {'id': 12 if sha == M else 1, 'state': state}

    def audit_run(self, sha, status):
        return {'event': 'repository_dispatch', 'actor': {'login': OWNER if sha == M else 'github-actions[bot]'}}

    def request(self, method, path, payload=None):
        if method != 'GET':
            self.writes.append((method, path, payload))
        if path == '/user':
            return {'login': OWNER}
        if path == 'branches/main/protection':
            return PROTECTION
        if path == '':
            return METADATA
        if path == 'pulls/8':
            return self.pr
        if path == 'pulls/8/merge':
            if self.merge_error:
                raise ApiError(method, path, 409)
            self.main = M
            return {'merged': True, 'sha': M}
        if path == 'dispatches':
            self.dispatched = True
            return None
        raise AssertionError((method, path, payload))


def graph_mock():
    graph = mock.Mock()
    graph.paths.return_value = {'series/a/analysis.md'}
    graph.ancestor.side_effect = lambda base, head: base == B and head == S
    graph.merge_tree.return_value = 'e' * 40
    graph.tree.side_effect = lambda sha: 'f' * 40 if sha == B else 'e' * 40
    return graph


class ControllerTests(unittest.TestCase):
    def worker(self, api=None, preview=False):
        worker = Integrator(api or FakeAPI(), graph_mock(), preview=preview, controller_sha=B)
        worker.save = mock.Mock()
        return worker

    def test_merge_binds_head_and_explicitly_audits_returned_main(self):
        worker = self.worker()
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), M)
        self.assertEqual(row['outcome'], 'merged_verified')
        self.assertEqual(worker.api.writes, [
            ('PUT', 'pulls/8/merge', {'sha': S, 'merge_method': 'merge'}),
            ('POST', 'dispatches', {'event_type': 'audit-generated-commit', 'client_payload': {'commit_sha': M, 'branch': 'main'}}),
        ])

    def test_preview_never_pushes_creates_pr_or_merges(self):
        worker = self.worker(preview=True)
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), B)
        self.assertEqual(row['outcome'], 'candidate')
        self.assertEqual(worker.api.writes, [])
        worker.graph.push.assert_not_called()

    def test_preview_transport_rejects_every_mutation(self):
        for method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            with self.assertRaises(Halt):
                GitHub('test', preview=True).request(method, 'pulls', {})

    def test_source_drift_is_preserved_before_any_write(self):
        worker = self.worker()
        worker.api.source = G
        with self.assertRaisesRegex(Blocked, 'Source advanced'):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])

    def test_main_drift_stops_integration(self):
        worker = self.worker()
        worker.api.main = M
        with self.assertRaises(Halt):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])

    def test_conflict_is_never_resolved_or_published(self):
        worker = self.worker()
        worker.graph.merge_tree.side_effect = Blocked('conflict')
        with self.assertRaises(Blocked):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])
        worker.graph.push.assert_not_called()

    def test_failed_source_and_out_of_scope_paths_block_before_writes(self):
        for failure in ('audit', 'scope'):
            worker = self.worker()
            if failure == 'audit':
                worker.api.source_status = 'failure'
            else:
                worker.graph.paths.return_value = {'tools/validate_repository.py'}
            with self.assertRaises(Blocked):
                worker.process('series/a', S, B, {})
            self.assertEqual(worker.api.writes, [])

    def test_pending_preflight_never_satisfies_final_integration(self):
        worker = self.worker()
        worker.api.source_status = 'pending'
        clock = [0]
        worker.wait_seconds = 10
        with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), mock.patch('nightly_integration.time.sleep', side_effect=lambda _: clock.__setitem__(0, 11)):
            with self.assertRaisesRegex(Blocked, 'Timed out'):
                worker.wait_final('series/a', S, B)
        self.assertEqual(worker.api.writes, [])

    def test_post_merge_failure_retains_integrated_receipt_and_halts(self):
        worker = self.worker()
        worker.api.post_failure = True
        row = {}
        with self.assertRaisesRegex(Halt, 'Already integrated'):
            worker.process('series/a', S, B, row)
        self.assertEqual(row['outcome'], 'integrated_unverified')
        self.assertEqual(row['integration_sha'], M)
        self.assertEqual(len(worker.api.writes), 2)

    def test_merge_conflict_response_is_read_back_without_retry(self):
        worker = self.worker()
        worker.api.merge_error = True
        with self.assertRaisesRegex(Blocked, 'not confirmed'):
            worker.process('series/a', S, B, {})
        self.assertEqual(len(worker.api.writes), 1)
        self.assertFalse(worker.api.dispatched)

    def test_holds_and_foreign_prs_are_respected(self):
        for changes in ({'draft': True}, {'labels': [{'name': 'nightly-hold'}]}, {'user': {'login': 'someone-else'}}):
            pr = pull()
            pr.update(changes)
            with self.assertRaises(Blocked):
                Integrator.allowed_pr(pr)

    def test_branch_inventory_is_filtered_and_halt_stops_next_candidate(self):
        worker = self.worker()
        worker.preflight = mock.Mock(return_value=B)
        worker.process = mock.Mock(side_effect=Halt('post-merge failure'))
        with self.assertRaises(Halt):
            worker.run()
        self.assertEqual(worker.process.call_count, 1)
        self.assertEqual(worker.process.call_args.args[0], 'series/a')

    def test_only_five_output_housekeeping_child_is_accepted(self):
        worker = self.worker()
        worker.api.request = mock.Mock(return_value={
            'parents': [{'sha': S}], 'message': 'housekeeping\n\nGenerated-From: ' + S,
            'author': AUTHOR, 'committer': COMMITTER,
        })
        worker.graph.paths.return_value = {'series/registry.json'}
        self.assertTrue(worker.generated_child(S, G))
        for path in ('characters/registry.jsonl', 'series/a/analysis.md', 'tools/tool.py'):
            worker.graph.paths.return_value = {path}
            self.assertFalse(worker.generated_child(S, G))

    def test_protection_requires_strict_status_and_owner_enforcement(self):
        self.assertEqual(protection_method(PROTECTION, METADATA), 'merge')
        for field in ('required_status_checks', 'enforce_admins'):
            invalid = copy.deepcopy(PROTECTION)
            invalid.pop(field)
            with self.assertRaises(Halt):
                protection_method(invalid, METADATA)
        linear = dict(PROTECTION, required_linear_history={'enabled': True})
        self.assertEqual(protection_method(linear, METADATA), 'squash')

    def test_scope_allows_only_named_root_and_reviewed_shared_paths(self):
        self.assertTrue(scoped_paths('series/a', {'series/a/doc.md'} | GENERATED))
        for path in ('series/ab/doc.md', 'series/b/doc.md', 'tools/runner.py', 'AGENTS.md'):
            self.assertFalse(scoped_paths('series/a', {path}))
        self.assertFalse(scoped_paths('codex/a', set()))

    def test_latest_status_and_trusted_workflow_identity(self):
        api = GitHub('test')
        api.pages = mock.Mock(return_value=[{'context': AUDIT, 'state': 'failure'}, {'context': AUDIT, 'state': 'success'}])
        self.assertEqual(api.status(S)['state'], 'failure')
        status = {'creator': {'login': 'github-actions[bot]'}, 'target_url': f'https://github.com/{REPOSITORY}/actions/runs/42'}
        api.request = mock.Mock(return_value={'path': AUDIT_WORKFLOW, 'conclusion': 'success', 'event': 'push', 'head_sha': S})
        self.assertIsNotNone(api.audit_run(S, status))
        self.assertIsNone(api.audit_run(B, status))
        api.request.return_value['path'] = '.github/workflows/other.yml'
        self.assertIsNone(api.audit_run(S, status))


    def test_reconciliation_is_a_nonforced_push_before_fresh_audit_and_merge(self):
        worker = self.worker()
        worker.graph.ancestor.side_effect = lambda base, head: base == B and head == G
        worker.graph.reconcile_commit.return_value = G
        def pushed(branch, sha, token):
            self.assertEqual((branch, sha), ('series/a', G))
            worker.api.source = G
            worker.api.pr['head']['sha'] = G
        worker.graph.push.side_effect = pushed
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), M)
        self.assertEqual(row['reconciled_sha'], G)
        self.assertEqual(row['final_source_sha'], G)
        self.assertEqual(worker.api.writes[0][2]['sha'], G)

    def test_no_content_change_produces_no_remote_write(self):
        worker = self.worker()
        worker.graph.merge_tree.return_value = 'f' * 40
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), B)
        self.assertEqual(row['outcome'], 'no_content_change')
        self.assertEqual(worker.api.writes, [])

    def test_post_merge_timeout_does_not_accept_an_older_success(self):
        worker = self.worker()
        worker.api.dispatched = True
        clock = [0]
        with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), mock.patch('nightly_integration.time.sleep', side_effect=lambda _: clock.__setitem__(0, 1801)):
            with self.assertRaisesRegex(Halt, 'did not finish'):
                worker.wait_post_merge(M, 12)

    def test_merge_requires_time_for_post_merge_validation(self):
        worker = self.worker()
        worker.deadline = __import__('time').monotonic() + 60
        with self.assertRaisesRegex(Halt, 'Insufficient time'):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])


class RealGitTests(unittest.TestCase):
    def test_clean_merge_preserves_both_histories_without_checkout(self):
        with tempfile.TemporaryDirectory() as temp:
            graph = Graph(Path(temp))
            graph.git('config', 'user.name', OWNER)
            graph.git('config', 'user.email', AUTHOR['email'])
            empty = graph.git('mktree', input_text='')
            root = graph.git('commit-tree', empty, input_text='root\n')
            blob = graph.git('hash-object', '-w', '--stdin', input_text='authored bytes\n')
            source_tree = graph.git('mktree', input_text=f'100644 blob {blob}\tanalysis.md\n')
            main_tree = graph.git('mktree', input_text=f'100644 blob {blob}\tother.md\n')
            source = graph.git('commit-tree', source_tree, '-p', root, input_text='source\n')
            base = graph.git('commit-tree', main_tree, '-p', root, input_text='main\n')
            combined = graph.merge_tree(source, base)
            merged = graph.reconcile_commit(source, base, combined)
            self.assertTrue(graph.ancestor(source, merged))
            self.assertTrue(graph.ancestor(base, merged))
            self.assertEqual(graph.git('show', merged + ':analysis.md'), 'authored bytes')
            self.assertEqual(graph.paths(base, merged), {'analysis.md'})
            other_blob = graph.git('hash-object', '-w', '--stdin', input_text='different\n')
            conflicting_tree = graph.git('mktree', input_text=f'100644 blob {other_blob}\tanalysis.md\n')
            conflicting = graph.git('commit-tree', conflicting_tree, '-p', root, input_text='conflict\n')
            with self.assertRaises(Blocked):
                graph.merge_tree(source, conflicting)


class ContractTests(unittest.TestCase):
    def snapshot(self, mutate=None, rebind=False):
        names = ('.github/workflows/nightly-integration.yml', 'tools/nightly_integration.py',
                 'governance/repository-controls/nightly-integration-policy.json')
        data = {path: (ROOT / path).read_bytes() for path in names}
        if mutate:
            data[names[0]] = mutate(data[names[0]])
        if rebind:
            policy = json.loads(data[names[2]])
            policy['workflow_sha256'] = hashlib.sha256(data[names[0]]).hexdigest()
            data[names[2]] = json.dumps(policy).encode()
        return GitSnapshot(ROOT, 'TEST', {p: SnapshotEntry(p, '100644', value) for p, value in data.items()})

    def test_reviewed_contract_validates(self):
        self.assertEqual(validate_nightly_integration(self.snapshot()), [])

    def test_changed_script_or_workflow_requires_reviewed_binding(self):
        errors = validate_nightly_integration(self.snapshot(lambda data: data + b'\n# changed\n'))
        self.assertTrue(any('SHA-256' in error for error in errors))

    def test_rebinding_does_not_allow_wider_permissions_or_different_timezone(self):
        for old, new in ((b'contents: read', b'contents: write'), (b'America/New_York', b'Etc/UTC'),
                         (b'cancel-in-progress: false', b'cancel-in-progress: true')):
            with self.subTest(old=old):
                self.assertTrue(validate_nightly_integration(self.snapshot(lambda data: data.replace(old, new), rebind=True)))


if __name__ == '__main__':
    unittest.main()
