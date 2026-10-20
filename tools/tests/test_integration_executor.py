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
from integration_lock import IntegrationLock, LOCK_REF, LockError
from nightly_integration import (
    AUTHOR, COMMITTER, OWNER, REPOSITORY, ApiError, Blocked, GitHub, Graph,
    Halt, Integrator, eligible_paths, main, tag_protection,
)
from test_nightly_integration import B, S, M, G, FakeAPI, graph_mock


class LockServer(FakeAPI):
    """Model the server's atomic create/non-forced fast-forward operations."""
    def __init__(self):
        super().__init__()
        self.ref = None
        self.commits = {B: {'tree': {'sha': 'e' * 40}}}
        self.before_ref = None
        self.after_ref = None
        self.control_role = 'fallback'

    def request(self, method, path, payload=None):
        if path == 'actions/variables/INTEGRATION_EXECUTOR_MODE':
            return {'value': self.control_role}
        if path == 'git/ref/' + LOCK_REF:
            if self.ref is None:
                raise ApiError(method, path, 404)
            return {'ref': 'refs/' + LOCK_REF, 'object': {'type': 'commit', 'sha': self.ref}}
        if path.startswith('git/commits/'):
            return copy.deepcopy(self.commits[path.rsplit('/', 1)[1]])
        if (method, path) == ('POST', 'git/commits'):
            sha = hashlib.sha1(json.dumps(payload, sort_keys=True).encode()).hexdigest()
            self.commits[sha] = dict(copy.deepcopy(payload), sha=sha,
                                     tree={'sha': payload['tree']}, parents=[{'sha': p} for p in payload['parents']])
            self.writes.append((method, path, payload))
            return {'sha': sha}
        if path in ('git/refs', 'git/refs/' + LOCK_REF):
            self.writes.append((method, path, payload))
            if self.before_ref:
                hook, self.before_ref = self.before_ref, None
                hook()
            if method == 'POST':
                assert payload['ref'] == 'refs/' + LOCK_REF
                if self.ref is not None:
                    raise ApiError(method, path, 422)
            else:
                assert method == 'PATCH' and payload['force'] is False
                if [p['sha'] for p in self.commits[payload['sha']]['parents']] != [self.ref]:
                    raise ApiError(method, path, 422)
            self.ref = payload['sha']
            if self.after_ref:
                hook, self.after_ref = self.after_ref, None
                hook()
            return {'object': {'sha': self.ref}}
        return super().request(method, path, payload)

    def state(self):
        return json.loads(self.commits[self.ref]['message']) if self.ref else None


def lock(server, role='fallback'):
    return IntegrationLock(server, role=role, controller_sha=B, author=AUTHOR, committer=COMMITTER)


class SharedLockTests(unittest.TestCase):
    def test_two_first_claims_have_one_winner(self):
        """An atomic create rejects the losing initial claimant across both routes."""
        api = LockServer()
        first, second = lock(api, 'primary'), lock(api)
        api.before_ref = lambda: second.acquire(B)
        with self.assertRaises(LockError):
            first.acquire(B)
        second.assert_owned()
        self.assertIsNone(first.owned_sha)
        self.assertEqual(api.state()['run_id'], second.run_id)

    def test_two_reclaims_of_released_state_cannot_both_win(self):
        """Competing sibling claims cannot both fast-forward a released ref."""
        api = LockServer()
        initial = lock(api)
        initial.acquire(B)
        initial.release()
        first, second = lock(api, 'primary'), lock(api)
        api.before_ref = lambda: second.acquire(B)
        with self.assertRaises(LockError):
            first.acquire(B)
        second.assert_owned()
        self.assertEqual(api.state()['run_id'], second.run_id)

    def test_stalled_owner_never_expires_or_allows_takeover(self):
        """Old timestamps do not grant takeover; a paused writer retains exclusion."""
        api = LockServer()
        owner = lock(api, 'primary')
        owner.acquire(B)
        state = api.state()
        state['at'] = '2000-01-01T00:00:00+00:00'
        api.commits[api.ref]['message'] = json.dumps(state)
        before = len(api.writes)
        with self.assertRaises(LockError):
            lock(api).acquire(B)
        self.assertEqual(len(api.writes), before)
        owner.assert_owned()

    def test_lost_ownership_stops_mutation_and_release(self):
        """An old owner cannot proceed or release a successor's lock."""
        api = LockServer()
        old = lock(api)
        old.acquire(B)
        old_sha = old.owned_sha
        old.release()
        new = lock(api, 'primary')
        new.acquire(B)
        old.owned_sha = old_sha
        before = len(api.writes)
        for operation in (old.assert_owned, old.release):
            with self.assertRaises(LockError):
                operation()
        self.assertEqual(len(api.writes), before)
        new.assert_owned()

    def test_ambiguous_claim_reads_back_without_replaying_write(self):
        """A lost claim response is resolved only by its exact commit readback."""
        api = LockServer()
        api.after_ref = lambda: (_ for _ in ()).throw(OSError('response lost'))
        owner = lock(api)
        owner.acquire(B)
        self.assertEqual(sum(path == 'git/refs' for _, path, _ in api.writes), 1)
        owner.assert_owned()

    def test_unconfirmed_claim_is_not_retried(self):
        """An unconfirmed remote claim leaves apply forbidden without a retry."""
        api = LockServer()
        api.before_ref = lambda: (_ for _ in ()).throw(OSError('timeout'))
        owner = lock(api)
        with self.assertRaises(LockError):
            owner.acquire(B)
        self.assertEqual(sum(path == 'git/refs' for _, path, _ in api.writes), 1)
        self.assertIsNone(owner.owned_sha)

    def test_malformed_lock_or_unapproved_identity_fails_closed(self):
        """Malformed state and unapproved metadata cannot masquerade as a free lock."""
        for mutation in ('message', 'parents', 'author', 'tree', 'sha'):
            with self.subTest(mutation=mutation):
                api = LockServer()
                owner = lock(api)
                owner.acquire(B)
                owner.release()
                api.commits[api.ref][mutation] = {
                    'message': '{}', 'parents': [], 'author': {'name': 'other'},
                    'tree': {'sha': 'invalid'}, 'sha': '0' * 40,
                }[mutation]
                with self.assertRaises(LockError):
                    lock(api).acquire(B)

    def test_release_is_a_nonforced_commit_not_ref_deletion(self):
        """Successful release preserves the coordination ref and its immutable history."""
        api = LockServer()
        owner = lock(api)
        owner.acquire(B)
        acquired = owner.owned_sha
        owner.release()
        self.assertEqual(api.state()['state'], 'released')
        self.assertEqual(api.commits[api.ref]['parents'], [{'sha': acquired}])
        self.assertFalse(any(method == 'DELETE' or payload.get('force') for method, _, payload in api.writes))


class ExecutorTests(unittest.TestCase):
    def worker(self, api=None, role='fallback'):
        api = api or LockServer()
        api.control_role = role
        worker = Integrator(api, graph_mock(), preview=False, controller_sha=B, role=role)
        worker.save = mock.Mock()
        return worker

    def test_lock_covers_merge_and_post_merge_audit(self):
        """The real executor holds shared ownership through protected merge and final audit."""
        worker = self.worker()
        request = worker.api.request
        observed = []
        def wrapped(method, path, payload=None):
            if path in ('pulls/8/merge', 'dispatches'):
                observed.append(worker.api.state()['state'])
                worker.lock.assert_owned()
            return request(method, path, payload)
        worker.api.request = wrapped
        worker.run('series/a')
        self.assertEqual(observed, ['held', 'held'])
        self.assertEqual(worker.rows[-1]['outcome'], 'merged_verified')
        self.assertEqual(worker.api.state()['state'], 'released')

    def test_post_merge_failure_retains_lock_and_integration_sha(self):
        """Post-merge failure preserves ownership and the integrated-but-unverified receipt."""
        worker = self.worker()
        worker.api.post_failure = True
        with self.assertRaises(Halt):
            worker.run('series/a')
        self.assertEqual(worker.api.state()['state'], 'held')
        self.assertEqual(worker.rows[-1]['integration_sha'], M)
        self.assertEqual(worker.rows[-1]['outcome'], 'integrated_unverified')
        with self.assertRaises(LockError):
            lock(worker.api, 'primary').acquire(M)

    def test_primary_integrates_routine_pr_under_the_same_lock(self):
        """Primary routine PRs use the protected merge and exact-main audit sequence."""
        worker = self.worker(role='primary')
        worker.api.pr['head']['ref'] = 'codex/repair'
        worker.graph.paths.return_value = {'README.md'}
        audit = worker.api.audit_run
        worker.api.audit_run = lambda sha, status, **kwargs: dict(audit(sha, status, **kwargs), actor={'login': OWNER})
        worker.run('codex/repair')
        self.assertEqual(worker.rows[-1]['outcome'], 'merged_verified')
        self.assertEqual(worker.rows[-1]['integration_sha'], M)
        self.assertEqual(worker.api.state()['state'], 'released')

    def test_final_routine_certification_cannot_be_replaced_by_bot_audit(self):
        """A changed routine audit actor immediately before merge blocks publication."""
        worker = self.worker(role='primary')
        worker.api.pr['head']['ref'] = 'codex/repair'
        worker.graph.paths.return_value = {'README.md'}
        audit = worker.api.audit_run
        worker.api.audit_run = lambda sha, status, **kwargs: dict(audit(sha, status, **kwargs), actor={'login': OWNER})
        guard = worker.guard_mutation
        def replace_certificate(*args, **kwargs):
            guard(*args, **kwargs)
            worker.api.audit_run = audit
        worker.guard_mutation = replace_certificate
        worker.run('codex/repair')
        self.assertEqual(worker.rows[-1]['outcome'], 'blocked')
        self.assertFalse(any(path.endswith('/merge') for _, path, _ in worker.api.writes))

    def test_lock_covers_reconciliation_and_pr_creation(self):
        """Source synchronization and automatic stable PR creation require shared ownership."""
        worker = self.worker()
        worker.graph.ancestor.side_effect = lambda base, head: base == B and head == G
        worker.graph.reconcile_commit.return_value = G
        observed = []
        def push(branch, sha, token):
            worker.lock.assert_owned()
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
                worker.lock.assert_owned()
                observed.append('create_pr')
                created = True
                return worker.api.pr
            return request(method, path, payload)
        worker.api.pages, worker.api.request = no_pr, create_pr
        worker.run('series/a')
        self.assertEqual(observed, ['push', 'create_pr'])
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

    def test_ambiguous_merge_retains_lock_without_retry(self):
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
        self.assertEqual(worker.api.state()['state'], 'held')

    def test_malformed_merge_acknowledgement_never_releases_ownership(self):
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
                self.assertEqual(worker.api.state()['state'], 'held')
                self.assertFalse(any(path == 'dispatches' for _, path, _ in worker.api.writes))
                if response.get('merged'):
                    self.assertEqual(worker.rows[-1]['outcome'], 'integrated_unverified')

    def test_disable_or_mode_change_stops_next_mutation(self):
        """Owner disable and primary/fallback handoff are checked at every mutation."""
        for mode in ('disabled', 'primary', '', None):
            worker = self.worker()
            worker.lock.acquire(B)
            worker.api.control_role = mode
            before = len(worker.api.writes)
            with self.subTest(mode=mode), self.assertRaises(Halt):
                worker.guard_mutation('series/a', S, B)
            self.assertEqual(len(worker.api.writes), before)

    def test_apply_without_lock_cannot_publish(self):
        """Calling the merge path without acquiring ownership cannot write."""
        worker = self.worker()
        with self.assertRaises(LockError):
            worker.process('series/a', S, B, {})
        self.assertFalse(worker.api.writes)

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
        self.assertEqual(worker.api.state()['state'], 'released')

    def test_reserved_paths_and_specialized_branches_are_rejected(self):
        """Reserved controls and character routes cannot use routine integration authority."""
        for path in ('tools/a.py', '.github/a', 'governance/policies/a.md', 'crosswalk/a.json', 'provenance/a.md',
                     'AGENTS.md', 'LICENSE.md', 'characters/README.md', 'characters/reconstruction_capabilities.jsonl'):
            for branch in ('series/a', 'codex/fix'):
                with self.subTest(path=path, branch=branch):
                    self.assertFalse(eligible_paths(branch, {path}, 'primary'))
        for branch in ('character-registry', 'character-reconstruction', 'feature/anything'):
            self.assertFalse(eligible_paths(branch, {'README.md'}, 'primary'))

    def test_primary_routine_scope_does_not_broaden_fallback(self):
        """Only primary admits bounded routine documentation/routing PRs."""
        self.assertTrue(eligible_paths('codex/readme', {'README.md'}, 'primary'))
        self.assertTrue(eligible_paths('chatgpt/routing', {'series/registry.json'}, 'primary'))
        self.assertFalse(eligible_paths('codex/readme', {'README.md'}, 'fallback'))
        self.assertFalse(eligible_paths('codex/readme', {'series/a/analysis.md'}, 'primary'))
        self.assertFalse(eligible_paths('codex/readme', {'CHARACTER_ANALYSIS_INDEX.md'}, 'primary'))

    def test_tag_protection_requires_exact_no_bypass_rules(self):
        """Activation-tag scope and deletion/history protections fail closed."""
        valid = LockServer().request('GET', 'rulesets/21946617')
        tag_protection(valid)
        for field, value in (('bypass_actors', None), ('current_user_can_bypass', 'always'), ('target', 'branch'),
                             ('rules', []), ('conditions', {}), ('enforcement', 'disabled')):
            with self.subTest(field=field), self.assertRaises(Halt):
                tag_protection(dict(valid, **{field: value}))

    def test_fallback_rejects_schedule_and_nonowner_invocation(self):
        """The CLI independently rejects scheduled or foreign fallback apply."""
        for event, actor in (('schedule', OWNER), ('workflow_dispatch', 'other')):
            with mock.patch.dict(os.environ, {'GITHUB_REPOSITORY': REPOSITORY, 'GITHUB_ACTIONS': 'true',
                                              'GITHUB_REF': 'refs/heads/main', 'GITHUB_EVENT_NAME': event,
                                              'GITHUB_ACTOR': actor}), \
                    mock.patch.object(sys, 'argv', ['executor', '--mode', 'apply']), \
                    mock.patch('nightly_integration.Graph') as graph, self.assertRaises(SystemExit):
                main()
            graph.assert_not_called()

    def test_primary_requires_durable_receipt_destination(self):
        """Primary apply cannot start without an explicit durable receipt location."""
        with mock.patch.object(sys, 'argv', ['executor', '--role', 'primary', '--mode', 'apply']), \
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

    def test_runtime_must_be_integrated_and_match_loaded_bytes(self):
        """Unmerged or mismatched executor code cannot borrow an audited main's authority."""
        graph = object.__new__(Graph)
        graph.ancestor = mock.Mock(return_value=False)
        with self.assertRaises(Halt):
            graph.verify_runtime(S, B)
        graph.ancestor.return_value = True
        graph.git = mock.Mock(side_effect=[json.dumps({'controller': 'tools/nightly_integration.py',
                                                     'controller_sha256': '0' * 64}), b'changed code'])
        with self.assertRaises(Halt):
            graph.verify_runtime(S, B)

    def test_runtime_binding_uses_exact_bytes_without_newline_normalization(self):
        """Runtime trust compares complete Git blobs, including trailing newline bytes."""
        graph = object.__new__(Graph)
        graph.ancestor = mock.Mock(return_value=True)
        controller = (ROOT / 'tools/nightly_integration.py').read_bytes()
        shared_lock = (ROOT / 'tools/integration_lock.py').read_bytes()
        binding = {'controller': 'tools/nightly_integration.py', 'lock': 'tools/integration_lock.py',
                   'controller_sha256': hashlib.sha256(controller).hexdigest(),
                   'lock_sha256': hashlib.sha256(shared_lock).hexdigest()}
        graph.git = mock.Mock(side_effect=[json.dumps(binding), controller, shared_lock])
        graph.verify_runtime(B, B)
        graph.git = mock.Mock(side_effect=[json.dumps(binding), controller + b'\n'])
        with self.assertRaises(Halt):
            graph.verify_runtime(B, B)

    def test_mixed_character_commit_is_not_a_curator_repair(self):
        """A two-file curation repair cannot conceal analytical or control changes."""
        graph = object.__new__(Graph)
        graph.git = mock.Mock(side_effect=[S, 'characters/registry.jsonl\0series/a/analysis.md\0'])
        with self.assertRaises(Blocked):
            graph.verify_curation_commits(B, S)

    def test_receipt_survives_outside_disposable_graph(self):
        """A durable receipt records ownership and an integration SHA before cleanup."""
        with tempfile.TemporaryDirectory() as directory:
            worker = self.worker()
            worker.save = Integrator.save.__get__(worker)
            worker.report_path = Path(directory) / 'state' / 'receipt.json'
            worker.lock.acquire(B)
            worker.rows = [{'integration_sha': M, 'outcome': 'integrated_unverified'}]
            worker.save()
            receipt = json.loads(worker.report_path.read_text())
            self.assertEqual(receipt['lock']['ownership_commit'], worker.lock.owned_sha)
            self.assertEqual(receipt['branches'][0]['integration_sha'], M)
            self.assertFalse(worker.report_path.with_suffix('.tmp').exists())


if __name__ == '__main__':
    unittest.main()
