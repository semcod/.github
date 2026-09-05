import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run_event

CONFIG = json.loads((run_event.ROOT / 'managed-repositories.json').read_text())


class RoutingTests(unittest.TestCase):
    def select(self, kind, body, coordinator='semcod/.github'):
        return run_event.select_targets(kind, body, coordinator, CONFIG)

    def test_preserves_foreign_owner_with_same_name(self):
        self.assertEqual(self.select('repository_dispatch', {'action': 'org-repo-changed', 'client_payload': {'repository': 'autogrammar/imgl'}}), (['autogrammar/imgl'], False))

    def test_rejects_unmanaged_foreign_repository(self):
        with self.assertRaises(ValueError):
            self.select('repository_dispatch', {'action': 'org-repo-changed', 'client_payload': {'repository': 'other/imgl'}})

    def test_rejects_invalid_repository_inputs(self):
        for target in ('$(touch /tmp/injected)', 'owner/repo\nextra', '../repo', 'owner/repo/extra', 'owner/..', ''):
            with self.subTest(target=target), self.assertRaises(ValueError):
                self.select('repository_dispatch', {'action': 'org-repo-changed', 'client_payload': {'repository': target}})

    def test_legacy_manual_name_and_dry_run(self):
        self.assertEqual(self.select('workflow_dispatch', {'inputs': {'repository': 'goal', 'dry_run': 'true'}}), (['semcod/goal'], True))
        self.assertEqual(self.select('workflow_dispatch', {'inputs': {'repository': 'autogrammar/imgl', 'dry_run': False}}), (['autogrammar/imgl'], False))

    def test_numeric_boolean_is_rejected(self):
        with self.assertRaises(ValueError):
            self.select('workflow_dispatch', {'inputs': {'dry_run': 1}})

    def test_dispatch_cannot_request_whole_organization(self):
        with self.assertRaises(ValueError):
            self.select('repository_dispatch', {'action': 'org-repo-changed', 'client_payload': {'repository': 'semcod'}})

    def test_manual_empty_input_keeps_existing_full_org_behavior(self):
        self.assertEqual(self.select('workflow_dispatch', {}), (['semcod'], False))

    def test_schedule_covers_exact_managed_list(self):
        self.assertEqual(self.select('schedule', {}), (['semcod', *CONFIG['scheduled_repositories']], False))

    def test_other_installed_coordinators_keep_their_own_scope(self):
        self.assertEqual(self.select('schedule', {}, 'wronai/.github'), (['wronai'], False))
        with self.assertRaises(ValueError):
            self.select('workflow_dispatch', {'inputs': {'repository': 'autogrammar/imgl'}}, 'wronai/.github')

    def test_foreign_execution_preserves_homepage_pages_and_profile(self):
        with patch.object(run_event.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)) as call:
            self.assertEqual(run_event.run_targets(['autogrammar/imgl'], True, 'semcod/.github'), 0)
        args = call.call_args.args[0]
        self.assertIn('--metadata-only', args)
        self.assertIn('--skip-profile', args)
        self.assertIn('--dry-run', args)
        self.assertEqual(args[args.index('--org') + 1], 'autogrammar')

    def test_failure_does_not_hide_other_results_or_turn_green(self):
        with patch.object(run_event.subprocess, 'run', side_effect=[subprocess.CompletedProcess([], 1), subprocess.CompletedProcess([], 0)]) as call:
            self.assertEqual(run_event.run_targets(['semcod', 'autogrammar/imgl'], False, 'semcod/.github'), 1)
            self.assertEqual(call.call_count, 2)
