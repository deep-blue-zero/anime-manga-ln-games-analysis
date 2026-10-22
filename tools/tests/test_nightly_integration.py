from __future__ import annotations

import copy
import errno
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from nightly_integration import (
    AUDIT, AUDIT_INTEGRATION_ID, AUDIT_WORKFLOW, AUTHOR, COMMITTER, GENERATED, MAIN_RULESET_ID, OWNER, REPOSITORY,
    ApiError, Blocked, Deferred, GitError, GitHub, Graph, Halt, Integrator, main, protection_method, scoped_paths,
    temporary_graph_directory,
)
from character_index_core import GitSnapshot, SnapshotEntry
from validate_repository import validate_nightly_integration

B, S, M, G = 'b'*40, 'a'*40, 'c'*40, 'd'*40
RULESET = {
    'id': 25199066, 'target': 'branch', 'enforcement': 'active',
    'conditions': {'ref_name': {'include': ['refs/heads/main'], 'exclude': []}},
    'bypass_actors': [], 'current_user_can_bypass': 'never',
    'rules': [
        {'type': 'deletion'}, {'type': 'non_fast_forward'},
        {'type': 'required_status_checks', 'parameters': {
            'strict_required_status_checks_policy': True,
            'required_status_checks': [{'context': AUDIT, 'integration_id': 15368}],
        }},
    ],
}
METADATA = {'allow_merge_commit': True, 'allow_squash_merge': True}


def pull():
    return {'number': 8, 'state': 'open', 'draft': False, 'labels': [], 'mergeable': True, 'mergeable_state': 'clean',
            'user': {'login': OWNER}, 'base': {'ref': 'main'},
            'head': {'sha': S, 'ref': 'series/a', 'repo': {'full_name': REPOSITORY}}}


class FakeAPI:
    token = 'test-credential'

    def __init__(self):
        self.main = B
        self.source = S
        self.writes = []
        self.source_status = 'success'
        self.post_failure = False
        self.merge_error = False
        self.pr = pull()
        self.ruleset = copy.deepcopy(RULESET)
        self.requests = []
        self.access = {'collaborators?affiliation=all': [{'login': OWNER}], 'invitations': [], 'keys': [{'read_only': True}]}

    def head(self, branch):
        return self.main if branch == 'main' else self.source

    def pages(self, path):
        if path == 'branches':
            return [{'name': name, 'commit': {'sha': S}} for name in ('series/a', 'codex/repair', 'character-registry', 'studies/b')]
        if path in self.access:
            if self.access[path] is None:
                raise ApiError('GET', path, 403)
            return self.access[path]
        return [self.pr]

    def status(self, sha):
        # main's push audit reports on the merge commit only once it exists.
        if sha == M and self.main != M:
            return None
        state = ('failure' if self.post_failure else 'success') if sha == M else self.source_status
        return {'id': 12 if sha == M else 1, 'state': state}

    def audit_statuses(self, sha):
        status = self.status(sha)
        return [status] if status else []

    def audit_run(self, sha, status, *, require_success=True):
        return {'event': 'push' if sha == M else 'repository_dispatch', 'conclusion': 'success',
                'actor': {'login': OWNER if sha == M else 'github-actions[bot]'}}

    def request(self, method, path, payload=None):
        self.requests.append((method, path, payload))
        if method != 'GET':
            self.writes.append((method, path, payload))
        if path == '/user':
            return {'login': OWNER}
        if path == f'rulesets/{MAIN_RULESET_ID}':
            return self.ruleset
        if path == '':
            return METADATA
        if path == 'pulls/8':
            return self.pr
        if path == 'pulls/8/merge':
            if self.merge_error:
                raise ApiError(method, path, 409)
            self.main = M
            return {'merged': True, 'sha': M}
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
        worker = Integrator(api or FakeAPI(), graph_mock(), preview=preview)
        worker.save = mock.Mock()
        return worker

    def test_merge_binds_head_and_verifies_main_audit_of_the_merge_commit(self):
        worker = self.worker()
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), M)
        self.assertEqual(row['outcome'], 'merged_verified')
        self.assertEqual(worker.api.writes, [('PUT', 'pulls/8/merge', {'sha': S, 'merge_method': 'merge'})])

    def test_preview_never_pushes_creates_pr_or_merges(self):
        worker = self.worker(preview=True)
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), B)
        self.assertEqual(row['outcome'], 'candidate')
        self.assertEqual(worker.api.writes, [])
        worker.graph.push.assert_not_called()

    def test_transport_uses_canonical_repository_metadata_url(self):
        # GitHub returns 404 for the repository root URL with a trailing slash.
        cases = {
            '': f'https://api.github.com/repos/{REPOSITORY}',
            '/user': 'https://api.github.com/user',
            f'rulesets/{MAIN_RULESET_ID}': f'https://api.github.com/repos/{REPOSITORY}/rulesets/{MAIN_RULESET_ID}',
        }
        for path, expected in cases.items():
            with self.subTest(path=path), mock.patch('nightly_integration.urllib.request.urlopen') as transport:
                transport.return_value.__enter__.return_value.read.return_value = b'{}'
                self.assertEqual(GitHub('test', preview=True).request('GET', path), {})
                request = transport.call_args.args[0]
                self.assertEqual(request.full_url, expected)

    def test_apply_preflight_checks_runtime_owner_ruleset_and_main_audit_before_writes(self):
        worker = self.worker()
        self.assertEqual(worker.preflight(), B)
        worker.graph.verify_runtime.assert_called_once_with(B)
        self.assertIn(('GET', f'rulesets/{MAIN_RULESET_ID}', None), worker.api.requests)
        for case in ('owner', 'ruleset', 'main_audit'):
            with self.subTest(case=case):
                api = FakeAPI()
                if case == 'owner':
                    request = api.request
                    api.request = lambda method, path, payload=None: {'login': 'other'} if path == '/user' else request(method, path, payload)
                elif case == 'ruleset':
                    api.ruleset['enforcement'] = 'disabled'
                else:
                    api.source_status = 'failure'
                with self.assertRaises(Halt):
                    self.worker(api).preflight()
                self.assertEqual(api.writes, [])

    def test_apply_preflight_requires_owner_only_access(self):
        cases = {
            'collaborator': ('collaborators?affiliation=all', [{'login': OWNER}, {'login': 'other'}]),
            'invitation': ('invitations', [{'id': 1}]),
            'writable_key': ('keys', [{'read_only': True}, {'read_only': False}]),
            'unreadable': ('collaborators?affiliation=all', None),
        }
        for case, (path, rows) in cases.items():
            with self.subTest(case=case):
                api = FakeAPI()
                api.access[path] = rows
                with self.assertRaisesRegex(Halt, 'owner-only'):
                    self.worker(api).preflight()
                self.assertNotIn(('GET', f'rulesets/{MAIN_RULESET_ID}', None), api.requests)
                self.assertEqual(api.writes, [])

    def test_preview_preflight_needs_no_owner_credential_or_ruleset(self):
        worker = self.worker(preview=True)
        self.assertEqual(worker.preflight(), B)
        worker.graph.verify_runtime.assert_not_called()
        self.assertEqual(worker.api.requests, [])

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

    def test_main_drift_defers_remaining_candidates_without_writes(self):
        worker = self.worker()
        worker.api.main = M
        with self.assertRaisesRegex(Deferred, 'main advanced'):
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
        self.assertEqual(len(worker.api.writes), 1)

    def test_merge_conflict_response_is_read_back_without_retry(self):
        worker = self.worker()
        worker.api.merge_error = True
        with self.assertRaisesRegex(Blocked, 'not confirmed'):
            worker.process('series/a', S, B, {})
        self.assertEqual(len(worker.api.writes), 1)

    def test_holds_and_foreign_prs_are_respected(self):
        for changes in ({'draft': True}, {'labels': [{'name': 'nightly-hold'}]}, {'user': {'login': 'someone-else'}}):
            pr = pull()
            pr.update(changes)
            with self.assertRaises(Blocked):
                Integrator.allowed_pr(pr)

    def test_branch_inventory_is_filtered_and_halt_stops_next_candidate(self):
        worker = Integrator(FakeAPI(), graph_mock(), preview=False, candidates='analysis-branches')
        worker.save = mock.Mock()
        worker.preflight = mock.Mock(return_value=B)
        worker.process = mock.Mock(side_effect=Halt('post-merge failure'))
        with self.assertRaises(Halt):
            worker.run()
        self.assertEqual(worker.process.call_count, 1)
        self.assertEqual(worker.process.call_args.args[0], 'series/a')

    def test_open_pr_inventory_contains_only_owner_same_repository_prs(self):
        api = FakeAPI()
        foreign = copy.deepcopy(api.pr)
        foreign['user'] = {'login': 'someone-else'}
        foreign['head'].update(ref='feature/x', sha=G)
        forked = copy.deepcopy(api.pr)
        forked['head'].update(ref='agent/y', sha=G, repo={'full_name': 'other/fork'})
        own = copy.deepcopy(api.pr)
        own['head'].update(ref='agent/docs', sha=G)
        api.pages = lambda path: [foreign, forked, own, api.pr]
        worker = Integrator(api, graph_mock(), preview=True)
        self.assertEqual(worker.inventory(), [('agent/docs', G), ('series/a', S)])

    def test_deferral_stops_the_scan_without_failing_the_run(self):
        worker = Integrator(FakeAPI(), graph_mock(), preview=False, candidates='analysis-branches')
        worker.save = mock.Mock()
        worker.preflight = mock.Mock(return_value=B)
        worker.process = mock.Mock(side_effect=Deferred('main advanced'))
        worker.run()
        self.assertEqual(worker.process.call_count, 1)
        self.assertEqual([row['outcome'] for row in worker.rows], ['deferred'])

    def test_expected_head_holds_back_a_head_pushed_after_review(self):
        for expected, calls in ((S, 1), (G, 0)):
            with self.subTest(expected=expected):
                worker = Integrator(FakeAPI(), graph_mock(), preview=False)
                worker.save = mock.Mock()
                worker.preflight = mock.Mock(return_value=B)
                worker.process = mock.Mock(return_value=M)
                worker.run('series/a', expected)
                self.assertEqual(worker.process.call_count, calls)
                self.assertEqual(worker.rows[-1]['outcome'], 'pending' if calls else 'blocked')
                self.assertEqual(worker.api.writes, [])

    def test_expected_head_requires_a_branch_and_a_full_sha(self):
        for argv in (['--expect-head', S], ['--branch', 'series/a', '--expect-head', 'abc123'],
                     ['--mode', 'apply'], ['--mode', 'apply', '--branch', 'series/a']):
            with self.subTest(argv=argv), mock.patch.object(sys, 'argv', ['gate', *argv]), \
                    mock.patch('sys.stderr', new_callable=io.StringIO), self.assertRaises(SystemExit):
                main()

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
        self.assertEqual(protection_method(RULESET, METADATA), 'merge')
        for field in ('rules', 'current_user_can_bypass'):
            invalid = copy.deepcopy(RULESET)
            invalid.pop(field)
            with self.assertRaises(Halt):
                protection_method(invalid, METADATA)

    def test_bypass_actors_may_be_hidden_from_a_nonadmin_token(self):
        visible = copy.deepcopy(RULESET)
        visible.pop('bypass_actors')
        self.assertEqual(protection_method(visible, METADATA), 'merge')

    def test_main_ruleset_requires_active_pinned_identity_and_exact_target(self):
        changes = (
            {'id': None}, {'id': MAIN_RULESET_ID + 1}, {'target': 'tag'},
            {'enforcement': 'disabled'}, {'enforcement': 'evaluate'},
            {'conditions': {'ref_name': {'include': ['refs/heads/*'], 'exclude': []}}},
            {'conditions': {'ref_name': {'include': ['refs/heads/main', 'refs/heads/other'], 'exclude': []}}},
            {'conditions': {'ref_name': {'include': ['refs/heads/main'], 'exclude': ['refs/heads/main']}}},
        )
        for value in (None, {}, *(dict(copy.deepcopy(RULESET), **change) for change in changes)):
            with self.subTest(value=value), self.assertRaises(Halt):
                protection_method(value, METADATA)

    def test_main_ruleset_rejects_bypass_or_unverifiable_owner_enforcement(self):
        for changes in (
            {'bypass_actors': [{'actor_type': 'RepositoryRole', 'actor_id': 5, 'bypass_mode': 'always'}]},
            {'bypass_actors': [{'actor_type': 'User', 'actor_id': 50891441, 'bypass_mode': 'pull_request'}]},
            {'bypass_actors': None}, {'current_user_can_bypass': 'always'},
            {'current_user_can_bypass': 'pull_request'}, {'current_user_can_bypass': None},
        ):
            with self.subTest(changes=changes), self.assertRaises(Halt):
                protection_method(dict(copy.deepcopy(RULESET), **changes), METADATA)

    def test_main_ruleset_requires_every_preservation_and_audit_rule(self):
        for rule in RULESET['rules']:
            invalid = copy.deepcopy(RULESET)
            invalid['rules'] = [row for row in invalid['rules'] if row['type'] != rule['type']]
            with self.subTest(missing=rule['type']), self.assertRaises(Halt):
                protection_method(invalid, METADATA)
        for rules in (None, [None], RULESET['rules'] + [RULESET['rules'][0]]):
            with self.subTest(rules=rules), self.assertRaises(Halt):
                protection_method(dict(copy.deepcopy(RULESET), rules=rules), METADATA)

    def test_main_ruleset_requires_strict_audit_from_trusted_app(self):
        for parameters in (
            None, {}, {'strict_required_status_checks_policy': False},
            {'strict_required_status_checks_policy': True, 'required_status_checks': []},
            {'strict_required_status_checks_policy': True, 'required_status_checks': [{'context': 'other', 'integration_id': AUDIT_INTEGRATION_ID}]},
            {'strict_required_status_checks_policy': True, 'required_status_checks': [{'context': AUDIT}]},
            {'strict_required_status_checks_policy': True, 'required_status_checks': [{'context': AUDIT, 'integration_id': 42}]},
        ):
            invalid = copy.deepcopy(RULESET)
            invalid['rules'][-1]['parameters'] = parameters
            with self.subTest(parameters=parameters), self.assertRaises(Halt):
                protection_method(invalid, METADATA)

    def test_linear_history_rule_stops_merge_commit_integration(self):
        linear = copy.deepcopy(RULESET)
        linear['rules'].insert(2, {'type': 'required_linear_history'})
        with self.assertRaisesRegex(Halt, 'linear history'):
            protection_method(linear, METADATA)

    def test_main_ruleset_requires_enabled_merge_commits(self):
        self.assertEqual(protection_method(RULESET, {'allow_merge_commit': True, 'allow_squash_merge': False}), 'merge')
        for metadata in (None, {}, {'allow_squash_merge': True}, {'allow_merge_commit': False}):
            with self.subTest(metadata=metadata), self.assertRaises(Halt):
                protection_method(RULESET, metadata)

    def test_ruleset_weakened_during_the_run_stops_the_merge(self):
        worker = self.worker()
        worker.preflight()
        guard = worker.guard_mutation
        def weaken(*args, **kwargs):
            guard(*args, **kwargs)
            worker.api.ruleset['rules'][-1]['parameters']['strict_required_status_checks_policy'] = False
        worker.guard_mutation = weaken
        with self.assertRaisesRegex(Halt, 'up-to-date'):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])

    def test_unreadable_main_ruleset_stops_apply_without_mutation(self):
        for status in (403, 404):
            worker = self.worker()
            request = worker.api.request
            def fail_ruleset(method, path, payload=None):
                if path == f'rulesets/{MAIN_RULESET_ID}':
                    raise ApiError(method, path, status)
                return request(method, path, payload)
            worker.api.request = mock.Mock(side_effect=fail_ruleset)
            with self.subTest(status=status), self.assertRaises(ApiError):
                worker.preflight()
            self.assertEqual(worker.api.writes, [])
            worker.graph.push.assert_not_called()
            self.assertEqual(worker.api.request.call_args, mock.call('GET', f'rulesets/{MAIN_RULESET_ID}'))

    def test_scope_allows_only_named_root_and_reviewed_shared_paths(self):
        self.assertTrue(scoped_paths('series/a', {'series/a/doc.md'} | GENERATED))
        for path in ('series/ab/doc.md', 'series/b/doc.md', 'tools/runner.py', 'AGENTS.md'):
            self.assertFalse(scoped_paths('series/a', {path}))
        self.assertFalse(scoped_paths('codex/a', set()))

    def test_latest_status_and_trusted_workflow_identity(self):
        api = GitHub('test')
        api.pages = mock.Mock(return_value=[{'context': AUDIT, 'state': 'failure'}, {'context': AUDIT, 'state': 'success'}])
        self.assertEqual(api.status(S)['state'], 'failure')
        status = {'creator': {'login': 'github-actions[bot]', 'id': 41898282}, 'target_url': f'https://github.com/{REPOSITORY}/actions/runs/42'}
        api.request = mock.Mock(return_value={'path': AUDIT_WORKFLOW, 'conclusion': 'success', 'event': 'push', 'head_sha': S,
                                             'workflow_id': 347147204, 'actor': {'login': OWNER}, 'head_repository': {'full_name': REPOSITORY}})
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

    def test_ambiguous_push_is_read_back_before_proceeding_or_halting(self):
        for published in (True, False):
            with self.subTest(published=published):
                worker = self.worker()
                worker.graph.ancestor.side_effect = lambda base, head: base == B and head == G
                worker.graph.reconcile_commit.return_value = G
                def pushed(*args):
                    if published:
                        worker.api.source = G
                        worker.api.pr['head']['sha'] = G
                    raise GitError('push', 1)
                worker.graph.push.side_effect = pushed
                worker.generated_child = mock.Mock(return_value=False)
                if published:
                    self.assertEqual(worker.process('series/a', S, B, {}), M)
                else:
                    with self.assertRaises(GitError):
                        worker.process('series/a', S, B, {})
                    self.assertEqual(worker.api.writes, [])
                self.assertEqual(worker.graph.push.call_count, 1)

    def test_no_content_change_produces_no_remote_write(self):
        worker = self.worker()
        worker.graph.merge_tree.return_value = 'f' * 40
        row = {}
        self.assertEqual(worker.process('series/a', S, B, row), B)
        self.assertEqual(row['outcome'], 'no_content_change')
        self.assertEqual(worker.api.writes, [])

    def test_post_merge_timeout_halts_without_a_main_audit_result(self):
        worker = self.worker()
        clock = [0]
        with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), mock.patch('nightly_integration.time.sleep', side_effect=lambda _: clock.__setitem__(0, 1801)):
            with self.assertRaisesRegex(Halt, 'did not finish'):
                worker.wait_post_merge(M)

    def test_merge_requires_time_for_post_merge_validation(self):
        worker = self.worker()
        worker.deadline = __import__('time').monotonic() + 60
        with self.assertRaisesRegex(Deferred, 'Too little time'):
            worker.process('series/a', S, B, {})
        self.assertEqual(worker.api.writes, [])

    def test_post_merge_requires_trusted_success_on_the_merge_commit(self):
        worker = self.worker()
        api = GitHub('test')
        worker.api = api
        trusted = {'id': 14, 'context': AUDIT, 'state': 'success',
                   'creator': {'login': 'github-actions[bot]', 'id': 41898282},
                   'target_url': f'https://github.com/{REPOSITORY}/actions/runs/41'}
        run = {'path': AUDIT_WORKFLOW, 'event': 'push', 'head_sha': M, 'actor': {'login': OWNER},
               'conclusion': 'success', 'workflow_id': 347147204, 'head_repository': {'full_name': REPOSITORY}}
        api.pages = mock.Mock(return_value=[trusted])
        api.request = mock.Mock(return_value=run)
        with mock.patch('nightly_integration.time.sleep', side_effect=AssertionError('unexpected wait')):
            worker.wait_post_merge(M)
        api.pages.assert_called_once_with(f'commits/{M}/statuses')
        for state in ('failure', 'error'):
            with self.subTest(state=state):
                api.pages.return_value = [dict(trusted, state=state)]
                with self.assertRaisesRegex(Halt, "main's audit failed"):
                    worker.wait_post_merge(M)
        for case in ('pending', 'wrong_reporter', 'wrong_workflow', 'other_commit'):
            with self.subTest(case=case):
                status, observed = dict(trusted), dict(run)
                if case == 'pending':
                    status['state'] = 'pending'
                elif case == 'wrong_reporter':
                    status['creator'] = {'login': 'someone-else', 'id': 1}
                elif case == 'wrong_workflow':
                    observed['path'] = '.github/workflows/other.yml'
                else:
                    observed['head_sha'] = B
                api.pages.return_value = [status]
                api.request.return_value = observed
                clock = [0]
                with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), \
                        mock.patch('nightly_integration.time.sleep', side_effect=lambda _: clock.__setitem__(0, 1801)):
                    with self.assertRaisesRegex(Halt, 'did not finish'):
                        worker.wait_post_merge(M)


class SquashRecognitionTests(unittest.TestCase):
    def worker(self, preview=False):
        api = FakeAPI()
        prior = pull()
        prior.update(state='closed', merged_at='2026-09-21T16:38:58Z', merge_commit_sha=M)
        prior['head']['ref'] = 'series/a'
        prior['base']['repo'] = {'full_name': REPOSITORY}
        api.pages = mock.Mock(side_effect=lambda path: [prior] if 'state=closed' in path else [])
        worker = Integrator(api, graph_mock(), preview=preview)
        worker.graph.ancestor.side_effect = lambda base, head: (base, head) == (M, B)
        worker.graph.merge_tree.side_effect = Blocked('merge conflict')
        return worker, prior

    def test_exact_merged_tip_is_recognized_without_any_write(self):
        for preview in (False, True):
            with self.subTest(preview=preview):
                worker, prior = self.worker(preview)
                row = {}
                self.assertEqual(worker.process('series/a', S, B, row), B)
                self.assertEqual(row['outcome'], 'already_integrated')
                self.assertEqual((row['pr'], row['integration_sha']), (prior['number'], M))
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()
                worker.graph.reconcile_commit.assert_not_called()
                query = urllib.parse.parse_qs(worker.api.pages.call_args.args[0].split('?', 1)[1])
                self.assertEqual(query, {'state': ['closed'], 'base': ['main'], 'head': [OWNER + ':series/a']})

    def test_prior_pr_requires_merged_exact_tip_and_repository_identity(self):
        cases = [
            (('state',), 'open'), (('merged_at',), None),
            (('user', 'login'), 'someone-else'),
            (('head', 'sha'), G), (('head', 'ref'), 'series/b'),
            (('head', 'repo', 'full_name'), 'other/repo'), (('head', 'repo'), None),
            (('base', 'ref'), 'other'), (('base', 'repo', 'full_name'), 'other/repo'),
            (('base', 'repo'), None),
        ]
        for path, value in cases:
            with self.subTest(path=path, value=value):
                worker, prior = self.worker()
                target = prior
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                with self.assertRaisesRegex(Blocked, 'merge conflict'):
                    worker.process('series/a', S, B, {})
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()

    def test_prior_integration_requires_reachable_commit_and_identical_whole_tree(self):
        for failure in ('unreachable', 'different-tree', 'invalid-sha'):
            with self.subTest(failure=failure):
                worker, prior = self.worker()
                if failure == 'unreachable':
                    worker.graph.ancestor.side_effect = None
                    worker.graph.ancestor.return_value = False
                elif failure == 'different-tree':
                    worker.graph.tree.side_effect = lambda sha: sha
                else:
                    prior['merge_commit_sha'] = None
                with self.assertRaises(Blocked):
                    worker.process('series/a', S, B, {})
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()

    def test_drift_during_preservation_proof_prevents_stale_success(self):
        for moving in ('source', 'main'):
            with self.subTest(moving=moving):
                worker, _ = self.worker()
                worker.graph.fetch.side_effect = lambda sha: setattr(worker.api, moving, G) if sha == M else None
                row = {}
                with self.assertRaises((Blocked, Deferred)):
                    worker.process('series/a', S, B, row)
                self.assertNotEqual(row.get('outcome'), 'already_integrated')
                self.assertEqual(worker.api.writes, [])

    def test_git_execution_and_pr_lookup_errors_still_fail(self):
        for failure in ('git', 'api'):
            with self.subTest(failure=failure):
                worker, _ = self.worker()
                if failure == 'git':
                    worker.graph.merge_tree.side_effect = GitError('merge-tree', 128)
                    expected = GitError
                else:
                    def pages(path):
                        if 'state=closed' in path:
                            raise ApiError('GET', path, 403)
                        return []
                    worker.api.pages.side_effect = pages
                    expected = ApiError
                with self.assertRaises(expected):
                    worker.process('series/a', S, B, {})
                if failure == 'git':
                    self.assertFalse(any('state=closed' in call.args[0] for call in worker.api.pages.call_args_list))
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()


class SourceAuditWaitTests(unittest.TestCase):
    def worker(self, preview=False):
        worker = Integrator(FakeAPI(), graph_mock(), preview=preview)
        worker.save = mock.Mock()
        worker.api.source_audit = mock.Mock(return_value={
            'id': 42, 'status': 'in_progress', 'conclusion': None,
        })
        worker.api.status = mock.Mock(return_value=None)
        return worker

    def test_queued_source_audit_finishes_before_any_write(self):
        worker = self.worker()
        worker.api.source_audit.side_effect = [
            {'id': 42, 'status': 'queued', 'conclusion': None},
            {'id': 42, 'status': 'in_progress', 'conclusion': None},
        ]
        polls = []
        def advance(seconds):
            self.assertEqual(worker.api.writes, [])
            worker.graph.push.assert_not_called()
            polls.append(seconds)
            if len(polls) == 2:
                worker.api.status.side_effect = lambda sha: FakeAPI.status(worker.api, sha)
        with mock.patch('nightly_integration.time.sleep', side_effect=advance):
            self.assertEqual(worker.process('series/a', S, B, {}), M)
        self.assertEqual(polls, [15, 15])
        self.assertEqual(worker.api.writes[0][0], 'PUT')

    def test_absent_failed_or_unreported_source_audits_never_allow_writes(self):
        for case in ('absent', 'failure_status', 'error_status', 'failure', 'cancelled',
                     'timed_out', 'skipped', 'success_without_reporter'):
            with self.subTest(case=case):
                worker = self.worker()
                if case == 'absent':
                    worker.api.source_audit.return_value = None
                elif case.endswith('_status'):
                    worker.api.status.return_value = {'state': case.removesuffix('_status')}
                else:
                    worker.api.source_audit.return_value.update(
                        status='completed', conclusion='success' if case == 'success_without_reporter' else case)
                with mock.patch('nightly_integration.time.sleep') as sleep, self.assertRaises(Blocked):
                    worker.process('series/a', S, B, {})
                sleep.assert_not_called()
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()

    def test_reporter_completing_between_reads_is_rechecked(self):
        worker = self.worker()
        worker.api.source_audit.return_value.update(status='completed', conclusion='success')
        worker.api.status.side_effect = [None, {'state': 'pending'}]
        with mock.patch('nightly_integration.time.sleep') as sleep:
            worker.wait_source('series/a', S, B, worker.deadline)
        self.assertEqual(worker.api.status.call_count, 2)
        sleep.assert_not_called()
        self.assertEqual(worker.api.writes, [])

    def test_source_or_main_drift_during_initial_wait_stops_before_writes(self):
        for field, error in (('source', Blocked), ('main', Deferred)):
            with self.subTest(field=field):
                worker = self.worker()
                with mock.patch('nightly_integration.time.sleep', side_effect=lambda _: setattr(worker.api, field, G)):
                    with self.assertRaises(error):
                        worker.process('series/a', S, B, {})
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()

    def test_initial_wait_timeout_is_bounded_by_source_and_run_deadlines(self):
        for budget, wait_seconds in ((100, 20), (20, 100)):
            with self.subTest(budget=budget, wait_seconds=wait_seconds):
                worker = self.worker()
                worker.deadline, worker.wait_seconds = budget, wait_seconds
                clock = [0]
                with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), \
                        mock.patch('nightly_integration.time.sleep', side_effect=lambda seconds: clock.__setitem__(0, clock[0] + seconds)):
                    with self.assertRaisesRegex(Blocked, 'Timed out awaiting the source audit'):
                        worker.process('series/a', S, B, {})
                self.assertEqual(clock[0], 20)
                self.assertEqual(worker.api.writes, [])
                worker.graph.push.assert_not_called()

    def test_initial_wait_and_housekeeping_share_one_source_budget(self):
        worker = self.worker()
        worker.deadline, worker.wait_seconds = 10000, 100
        clock = [0]
        def advance(seconds):
            clock[0] += seconds
            if clock[0] >= 60:
                # A passed authored-content audit permits waiting for housekeeping,
                # but does not itself certify integration readiness.
                worker.api.status.return_value = {'state': 'pending'}
        with mock.patch('nightly_integration.time.monotonic', side_effect=lambda: clock[0]), \
                mock.patch('nightly_integration.time.sleep', side_effect=advance):
            with self.assertRaisesRegex(Blocked, 'Timed out awaiting housekeeping'):
                worker.process('series/a', S, B, {})
        self.assertEqual(clock[0], 100)
        self.assertEqual(worker.api.writes, [])

    def test_preview_reports_unfinished_source_without_polling(self):
        worker = self.worker(preview=True)
        with mock.patch('nightly_integration.time.sleep') as sleep, self.assertRaises(Blocked):
            worker.process('series/a', S, B, {})
        sleep.assert_not_called()
        worker.api.source_audit.assert_not_called()
        self.assertEqual(worker.api.writes, [])

    def test_source_run_discovery_binds_identity_branch_and_exact_commit(self):
        api = GitHub('test')
        run = {'id': 42, 'path': AUDIT_WORKFLOW, 'head_sha': S, 'head_branch': 'series/a',
               'event': 'push', 'actor': {'login': OWNER}, 'triggering_actor': {'login': OWNER},
               'head_repository': {'full_name': REPOSITORY}, 'status': 'in_progress', 'conclusion': None}
        api.request = mock.Mock(return_value={'workflow_runs': [run]})
        self.assertEqual(api.source_audit('series/a', S), run)
        method, path = api.request.call_args.args
        endpoint, query = path.split('?')
        self.assertEqual(method, 'GET')
        self.assertEqual(endpoint, 'actions/workflows/repository-audit.yml/runs')
        self.assertEqual(urllib.parse.parse_qs(query), {
            'branch': ['series/a'], 'head_sha': [S], 'event': ['push'], 'per_page': ['1'],
        })
        for field, invalid in (
            ('path', '.github/workflows/other.yml'), ('head_sha', G), ('head_branch', 'series/b'),
            ('event', 'repository_dispatch'), ('actor', {'login': 'someone-else'}),
            ('triggering_actor', {'login': 'someone-else'}), ('head_repository', {'full_name': 'fork/repo'}),
        ):
            with self.subTest(field=field):
                api.request.return_value = {'workflow_runs': [dict(run, **{field: invalid})]}
                self.assertIsNone(api.source_audit('series/a', S))
        api.request.return_value = {'workflow_runs': []}
        self.assertIsNone(api.source_audit('series/a', S))
        # A completed failure must remain visible, not be hidden by a status filter.
        failed = dict(run, status='completed', conclusion='failure')
        api.request.return_value = {'workflow_runs': [failed]}
        self.assertEqual(api.source_audit('series/a', S), failed)


class PreviewResultTests(unittest.TestCase):
    def invoke(self, mode, failure):
        # Run the real CLI/result/report path, with only network and Git mocked.
        worker = Integrator(FakeAPI(), graph_mock(), preview=mode == 'preview', candidates='analysis-branches')
        worker.preflight = mock.Mock(return_value=B)
        worker.process = mock.Mock(side_effect=[failure, B])
        with tempfile.TemporaryDirectory() as directory:
            previous = Path.cwd()
            try:
                os.chdir(directory)
                with mock.patch.dict(os.environ, {
                    'GITHUB_REPOSITORY': REPOSITORY, 'GITHUB_SHA': B,
                    'GITHUB_REF': 'refs/heads/main', 'GITHUB_ACTIONS': 'true',
                    'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_ACTOR': OWNER,
                    'OWNER_TOKEN': 'test', 'GITHUB_STEP_SUMMARY': '',
                }), mock.patch.object(sys, 'argv', ['nightly_integration', '--candidates', 'analysis-branches',
                                                    '--mode', mode]), \
                        mock.patch('nightly_integration.Graph'), \
                        mock.patch('nightly_integration.Integrator', return_value=worker), \
                        mock.patch('sys.stdout', new_callable=io.StringIO) as output:
                    result = main()
                report = json.loads(Path('nightly-integration-report.json').read_text())
            finally:
                os.chdir(previous)
        return result, report, output.getvalue(), worker

    def test_preview_deferral_warns_continues_and_succeeds(self):
        result, report, output, worker = self.invoke('preview', Blocked('Audit pending 50%\r\nsecond line'))
        self.assertEqual(result, 0)
        self.assertTrue(report['preview'])
        self.assertEqual(report['candidates'], 'analysis-branches')
        self.assertEqual(report['branches'][0]['outcome'], 'blocked')
        self.assertEqual(worker.process.call_count, 2)
        self.assertIn('::warning::series/a: Audit pending 50%25%0D%0Asecond line\n', output)
        self.assertEqual(worker.api.writes, [])
        worker.graph.push.assert_not_called()

    def test_apply_deferral_still_fails(self):
        result, report, output, worker = self.invoke('apply', Blocked('Audit pending'))
        self.assertEqual(result, 1)
        self.assertFalse(report['preview'])
        self.assertEqual(worker.process.call_count, 2)
        self.assertNotIn('::warning::', output)

    def test_preview_execution_errors_fail_and_stop_scan(self):
        for error in (GitError('fetch', 128), ApiError('GET', 'branches', 403), OSError('disk failure')):
            with self.subTest(error=str(error)):
                result, report, output, worker = self.invoke('preview', error)
                self.assertEqual(result, 1)
                self.assertEqual(report['branches'][-1]['outcome'], 'halted')
                self.assertEqual(worker.process.call_count, 1)
                self.assertNotIn('::warning::', output)


class CleanupTests(unittest.TestCase):
    def invoke(self, errors, *, outcome='success', original=None):
        # Exercise the real CLI, integration, and receipt paths without network.
        worker = Integrator(FakeAPI(), graph_mock(), preview=False, candidates='analysis-branches')
        worker.graph.ancestor.side_effect = lambda base, head: base == B and head == G
        worker.graph.reconcile_commit.return_value = G
        def pushed(branch, sha, token):
            worker.api.source = sha
            worker.api.pr['head']['sha'] = sha
        worker.graph.push.side_effect = pushed
        request, pages = worker.api.request, worker.api.pages
        created = False
        def request_with_creation(method, path, payload=None):
            nonlocal created
            if (method, path) == ('POST', 'pulls'):
                created = True
                worker.api.writes.append((method, path, payload))
                return worker.api.pr
            return request(method, path, payload)
        worker.api.request = request_with_creation
        worker.api.pages = lambda path: pages(path) if path == 'branches' or created else []
        if outcome == 'blocked':
            status = worker.api.status
            worker.api.status = lambda sha: {'id': 1, 'state': 'failure'} if sha == S else status(sha)
        elif outcome == 'post_failure':
            worker.api.post_failure = True
        if original is not None:
            worker.run = mock.Mock(side_effect=original)

        with tempfile.TemporaryDirectory() as directory:
            temporary = tempfile.TemporaryDirectory(dir=directory)
            remove = temporary._rmtree
            pending, receipts = list(errors), []
            def cleanup(*args, **kwargs):
                receipts.append((Path('nightly-integration-report.json').read_bytes(),
                                 Path('summary.md').read_bytes()))
                if pending:
                    raise pending.pop(0)
                return remove(*args, **kwargs)
            previous = Path.cwd()
            result, failure = None, None
            try:
                os.chdir(directory)
                with mock.patch.dict(os.environ, {
                    'GITHUB_REPOSITORY': REPOSITORY, 'GITHUB_SHA': B,
                    'GITHUB_REF': 'refs/heads/main', 'GITHUB_ACTIONS': 'true',
                    'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_ACTOR': OWNER,
                    'OWNER_TOKEN': 'test', 'GITHUB_STEP_SUMMARY': 'summary.md',
                }), mock.patch.object(sys, 'argv', ['nightly_integration', '--candidates', 'analysis-branches',
                                                    '--mode', 'apply', '--branch', 'series/a']), \
                        mock.patch('nightly_integration.Graph'), \
                        mock.patch('nightly_integration.Integrator', return_value=worker), \
                        mock.patch('nightly_integration.tempfile.TemporaryDirectory', return_value=temporary), \
                        mock.patch.object(temporary, '_rmtree', side_effect=cleanup) as removal, \
                        mock.patch('nightly_integration.time.sleep') as sleep, \
                        mock.patch('sys.stdout', new_callable=io.StringIO, newline=os.linesep) as output:
                    try:
                        result = main()
                    except BaseException as exc:
                        failure = exc
                report_bytes = Path('nightly-integration-report.json').read_bytes()
                summary = Path('summary.md').read_bytes()
                self.assertTrue(all(pair == (report_bytes, summary) for pair in receipts))
                self.assertIn(report_bytes.decode().replace('\r\n', '\n'), output.getvalue().replace('\r\n', '\n'))
                if failure is None or failure is original:
                    self.assertFalse(Path(temporary.name).exists())
            finally:
                os.chdir(previous)
                temporary.cleanup()
        return result, failure, json.loads(report_bytes), worker, removal.call_count, sleep.call_args_list

    def assert_single_integration(self, worker):
        worker.graph.push.assert_called_once_with('series/a', G, worker.api.token)
        self.assertEqual([(method, path) for method, path, _ in worker.api.writes], [
            ('POST', 'pulls'), ('PUT', 'pulls/8/merge'),
        ])
        self.assertEqual(worker.api.writes[1][2], {'sha': G, 'merge_method': 'merge'})

    def test_transient_cleanup_preserves_success_and_never_replays_remote_mutations(self):
        errors = [OSError(errno.ENOTEMPTY, 'Directory not empty', 'pack') for _ in range(2)]
        result, failure, report, worker, attempts, sleeps = self.invoke(errors)
        self.assertEqual((result, failure, attempts, sleeps), (0, None, 3, [mock.call(1), mock.call(1)]))
        self.assertEqual(len(report['branches']), 1)
        row = report['branches'][0]
        self.assertEqual((row['outcome'], row['pr'], row['final_source_sha'], row['integration_sha']),
                         ('merged_verified', 8, G, M))
        self.assert_single_integration(worker)

    def test_persistent_cleanup_fails_after_bounded_attempts_without_losing_receipts(self):
        error = OSError(errno.ENOTEMPTY, 'Directory not empty', 'pack')
        result, failure, report, worker, attempts, sleeps = self.invoke([error] * 3)
        self.assertIsNone(result)
        self.assertIs(failure, error)
        self.assertEqual((attempts, sleeps), (3, [mock.call(1), mock.call(1)]))
        self.assertEqual(report['branches'][0]['outcome'], 'merged_verified')
        self.assertEqual(report['branches'][0]['integration_sha'], M)
        self.assert_single_integration(worker)

    def test_other_cleanup_errors_fail_immediately_even_after_a_retry(self):
        for code in (errno.EACCES, errno.EIO, errno.ENOENT):
            for transient_first in (False, True):
                with self.subTest(code=code, transient_first=transient_first):
                    error = OSError(code, 'cleanup failed')
                    errors = ([OSError(errno.ENOTEMPTY, 'race')] if transient_first else []) + [error]
                    result, failure, report, worker, attempts, sleeps = self.invoke(errors)
                    self.assertIsNone(result)
                    self.assertIs(failure, error)
                    self.assertEqual(attempts, len(errors))
                    self.assertEqual(sleeps, [mock.call(1)] if transient_first else [])
                    self.assertEqual(report['branches'][0]['outcome'], 'merged_verified')
                    self.assert_single_integration(worker)

    def test_transient_cleanup_does_not_turn_failed_operations_into_success(self):
        for outcome in ('blocked', 'post_failure'):
            with self.subTest(outcome=outcome):
                result, failure, report, worker, attempts, sleeps = self.invoke(
                    [OSError(errno.ENOTEMPTY, 'race')], outcome=outcome)
                self.assertEqual((result, failure, attempts, sleeps), (1, None, 2, [mock.call(1)]))
                if outcome == 'blocked':
                    self.assertEqual(report['branches'][0]['outcome'], 'blocked')
                    self.assertEqual(worker.api.writes, [])
                    worker.graph.push.assert_not_called()
                else:
                    self.assertEqual(report['branches'][0]['outcome'], 'integrated_unverified')
                    self.assertEqual(report['branches'][0]['integration_sha'], M)
                    self.assertEqual(report['branches'][-1]['outcome'], 'halted')
                    self.assertIn("main's audit failed", report['branches'][-1]['detail'])
                    self.assert_single_integration(worker)

    def test_persistent_cleanup_keeps_original_operation_failure_in_report(self):
        error = OSError(errno.ENOTEMPTY, 'race')
        _, failure, report, worker, attempts, _ = self.invoke([error] * 3, outcome='post_failure')
        self.assertIs(failure, error)
        self.assertEqual(attempts, 3)
        self.assertEqual(report['branches'][0]['outcome'], 'integrated_unverified')
        self.assertEqual(report['branches'][0]['integration_sha'], M)
        self.assertIn("main's audit failed", report['branches'][-1]['detail'])
        self.assert_single_integration(worker)

    def test_unhandled_original_exception_survives_successful_cleanup_retry(self):
        for original in (RuntimeError('unexpected operation failure'), KeyboardInterrupt()):
            with self.subTest(original=type(original).__name__):
                result, failure, _, worker, attempts, _ = self.invoke(
                    [OSError(errno.ENOTEMPTY, 'race')], original=original)
                self.assertIsNone(result)
                self.assertIs(failure, original)
                self.assertIsNotNone(original.__traceback__)
                self.assertEqual(attempts, 2)
                worker.run.assert_called_once_with('series/a', '')
                self.assertEqual(worker.api.writes, [])

    def test_simultaneous_operation_and_cleanup_exceptions_are_both_preserved(self):
        for original in (RuntimeError('unexpected operation failure'), KeyboardInterrupt()):
            with self.subTest(original=type(original).__name__):
                cause = ValueError('original cause')
                original.__cause__ = cause
                cleanup_error = OSError(errno.ENOTEMPTY, 'race')
                _, failure, _, worker, attempts, _ = self.invoke([cleanup_error] * 3, original=original)
                self.assertIsInstance(failure, BaseExceptionGroup)
                self.assertEqual(failure.exceptions, (original, cleanup_error))
                self.assertIs(original.__cause__, cause)
                self.assertIsNotNone(original.__traceback__)
                self.assertIsNotNone(cleanup_error.__traceback__)
                self.assertEqual(attempts, 3)
                worker.run.assert_called_once_with('series/a', '')
                self.assertEqual(worker.api.writes, [])

    def test_real_pack_directory_race_is_removed_on_retry(self):
        remove, raced = os.rmdir, False
        with mock.patch('nightly_integration.time.sleep') as sleep:
            with temporary_graph_directory() as directory:
                pack = Path(directory) / 'objects' / 'pack'
                pack.mkdir(parents=True)
                (pack / 'old.pack').write_bytes(b'old')
                def late_write(path, *args, **kwargs):
                    nonlocal raced
                    if Path(path).name == 'pack' and not raced:
                        raced = True
                        (pack / 'late.pack').write_bytes(b'late')
                    return remove(path, *args, **kwargs)
                patch = mock.patch('os.rmdir', side_effect=late_write)
                patch.start()
                self.addCleanup(patch.stop)
            patch.stop()
        self.assertTrue(raced)
        self.assertFalse(Path(directory).exists())
        sleep.assert_called_once_with(1)


class RealGitTests(unittest.TestCase):
    def test_automatic_maintenance_is_disabled_only_in_disposable_graph(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            config = directory / 'global-config'
            inherited = b'[maintenance]\n\tauto = true\n[gc]\n\tauto = 1\n'
            config.write_bytes(inherited)
            graph_path = directory / 'graph'
            graph_path.mkdir()
            with mock.patch.dict(os.environ, {'GIT_CONFIG_GLOBAL': str(config), 'GIT_CONFIG_NOSYSTEM': '1'}):
                graph = Graph(graph_path)
                self.assertEqual(graph.git('config', '--show-scope', '--get', 'maintenance.auto'), 'local\tfalse')
                self.assertEqual(graph.git('config', '--show-scope', '--get', 'gc.auto'), 'local\t0')
                self.assertEqual(graph.git('config', '--global', '--get', 'maintenance.auto'), 'true')
                self.assertEqual(graph.git('config', '--global', '--get', 'gc.auto'), '1')
            self.assertEqual(config.read_bytes(), inherited)

    def test_squashed_tip_with_later_main_index_edit_is_already_integrated(self):
        with tempfile.TemporaryDirectory() as temp:
            graph = Graph(Path(temp))
            graph.git('config', 'user.name', OWNER)
            graph.git('config', 'user.email', AUTHOR['email'])

            def tree(contents):
                blob = graph.git('hash-object', '-w', '--stdin', input_text=contents)
                series = graph.git('mktree', input_text=f'100644 blob {blob}\tREADME.md\n')
                return graph.git('mktree', input_text=f'040000 tree {series}\tseries\n')

            root = graph.git('commit-tree', tree('Catalog\n'), input_text='root\n')
            source = graph.git('commit-tree', tree('Catalog\nTitle A\n'), '-p', root, input_text='source\n')
            merged = graph.git('commit-tree', graph.tree(source), '-p', root, input_text='squash\n')
            base = graph.git('commit-tree', tree('Catalog\nTitle A\nTitle B\n'), '-p', merged, input_text='next title\n')
            self.assertFalse(graph.ancestor(source, base))
            self.assertTrue(graph.ancestor(merged, base))
            with self.assertRaises(Blocked):
                graph.merge_tree(source, base)

            api = FakeAPI()
            api.main, api.source = base, source
            prior = pull()
            prior.update(state='closed', merged_at='2026-09-21T16:38:58Z', merge_commit_sha=merged)
            prior['head'].update(ref='series/a', sha=source)
            prior['base']['repo'] = {'full_name': REPOSITORY}
            api.pages = mock.Mock(side_effect=lambda path: [prior] if 'state=closed' in path else [])
            worker = Integrator(api, graph, preview=False)
            worker.graph.verify_identities = mock.Mock()
            row = {}
            with mock.patch.object(graph, 'fetch'), mock.patch.object(graph, 'push') as push:
                self.assertEqual(worker.process('series/a', source, base, row), base)
                push.assert_not_called()
            self.assertEqual(row['outcome'], 'already_integrated')
            self.assertEqual(row['integration_sha'], merged)
            self.assertEqual(graph.git('show', base + ':series/README.md'), 'Catalog\nTitle A\nTitle B')
            self.assertEqual(api.writes, [])

    def test_missing_git_objects_are_execution_errors_not_conflicts(self):
        with tempfile.TemporaryDirectory() as temp:
            graph = Graph(Path(temp))
            with self.assertRaises(GitError):
                graph.merge_tree(S, B)
            with self.assertRaises(GitError):
                graph.tree(S)

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
    def snapshot(self, mutate=None, script=None):
        names = ('.github/workflows/nightly-integration.yml', 'tools/nightly_integration.py')
        data = {path: (ROOT / path).read_bytes() for path in names}
        if mutate:
            data[names[0]] = mutate(data[names[0]])
        if script is not None:
            data[names[1]] = script
        return GitSnapshot(ROOT, 'TEST', {p: SnapshotEntry(p, '100644', value) for p, value in data.items()})

    def test_reviewed_contract_validates(self):
        self.assertEqual(validate_nightly_integration(self.snapshot()), [])

    def test_editing_the_merge_script_needs_no_hash_rebinding(self):
        changed = (ROOT / 'tools/nightly_integration.py').read_bytes() + b'\n# changed\n'
        self.assertEqual(validate_nightly_integration(self.snapshot(script=changed)), [])

    def test_workflow_cannot_widen_permissions_or_schedule_apply(self):
        for old, new in ((b'contents: read', b'contents: write'), (b'on:\n', b'on:\n  schedule: [{cron: "0 7 * * *"}]\n'),
                         (b'cancel-in-progress: false', b'cancel-in-progress: true')):
            with self.subTest(old=old):
                self.assertTrue(validate_nightly_integration(self.snapshot(lambda data: data.replace(old, new))))


if __name__ == '__main__':
    unittest.main()
